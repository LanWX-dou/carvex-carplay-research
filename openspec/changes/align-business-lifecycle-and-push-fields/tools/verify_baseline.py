"""Verify planning inputs and capture an independent execution baseline.

Only --capture writes execution-baseline.json. No implementation or firmware
files are modified. Hash checks do not establish protocol semantics.
"""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

CHANGE = Path(__file__).resolve().parents[1]
ROOT = CHANGE.parents[2]
DOCSET = ROOT / 'research/protocol/iap2_input_business_lifecycle'
EXPECTED_IMAGE = '2b0a2010e6d2605e07d87f05659c932e03de34476a76431196a9bb58da7dc4fe'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo, *args):
    return subprocess.check_output(
        ['git', '-c', f'safe.directory={repo.as_posix()}', '-C', str(repo), *args],
        text=True, encoding='utf-8').strip()


def inspect():
    historical = json.loads((CHANGE / 'baseline.json').read_text(encoding='utf-8'))
    result = {
        'capturedAtUtc': datetime.now(timezone.utc).isoformat(),
        'researchHead': git(ROOT, 'rev-parse', 'HEAD'),
        'historicalBaselinePreserved': True,
        'scope': 'Input identity and availability only; no firmware execution or vehicle acceptance.',
        'repositories': {},
        'evidence': {},
    }
    for name, record in historical['inputs'].items():
        repo = Path(record['root'])
        files = {}
        for relative, previous_sha in record['files'].items():
            path = repo / relative
            if not path.is_file():
                raise FileNotFoundError(path)
            actual = sha(path)
            files[relative] = {
                'sha256': actual,
                'matchesPlanningInput': actual == previous_sha,
            }
        result['repositories'][name] = {
            'root': repo.as_posix(),
            'head': git(repo, 'rev-parse', 'HEAD'),
            'planningHead': record['head'],
            'worktree': git(repo, 'status', '--porcelain', '--ignore-submodules=all'),
            'files': files,
        }
    candidates = [
        DOCSET / 'source/firmware/accessoryd',
        ROOT / 'firmware/ipsw/iPhone18,1_27.0.1_24A446_Restore.ipsw',
        DOCSET / 'tools/verify-nowplaying-audit.py',
        DOCSET / 'tools/verify-lifecycle-audit.py',
    ]
    functions = [
        0x1001499f0, 0x10014a93c, 0x10014aa20, 0x10017527c,
        0x10017593c, 0x1000027f4, 0x1001777c0,
        0x10003021c, 0x1000302a0, 0x100103210,
    ]
    candidates.extend(DOCSET / f'source/asm/accessoryd/f_{address:x}.s' for address in functions)
    for path in candidates:
        key = path.relative_to(ROOT).as_posix()
        result['evidence'][key] = {
            'available': path.is_file(),
            'sha256': sha(path) if path.is_file() else None,
        }
    image = result['evidence']['research/protocol/iap2_input_business_lifecycle/source/firmware/accessoryd']
    if image['sha256'] != EXPECTED_IMAGE:
        raise ValueError('Original accessoryd image differs from the audited 24A446 input')
    return result


def check_links():
    count = 0
    for path in CHANGE.rglob('*.md'):
        body = path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
            if '://' in target or target.startswith('#'):
                continue
            if not (path.parent / target.split('#', 1)[0]).resolve().exists():
                raise FileNotFoundError(f'{path}: {target}')
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture', action='store_true')
    args = parser.parse_args()
    actual = inspect()
    if args.capture:
        (CHANGE / 'execution-baseline.json').write_text(
            json.dumps(actual, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    else:
        recorded = json.loads((CHANGE / 'execution-baseline.json').read_text(encoding='utf-8'))
        for name, repo in recorded['repositories'].items():
            if actual['repositories'][name]['files'] != repo['files']:
                raise ValueError(f'Execution source inputs changed: {name}')
        if actual['evidence'] != recorded['evidence']:
            raise ValueError('Execution evidence availability or hashes changed')
    links = check_links()
    print(json.dumps({
        'result': 'PASS',
        'inputHashes': sum(len(repo['files']) for repo in actual['repositories'].values()),
        'planningInputDifferences': sum(
            not file['matchesPlanningInput']
            for repo in actual['repositories'].values() for file in repo['files'].values()),
        'evidenceAvailable': sum(file['available'] for file in actual['evidence'].values()),
        'evidenceMissing': sum(not file['available'] for file in actual['evidence'].values()),
        'localLinks': links,
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
