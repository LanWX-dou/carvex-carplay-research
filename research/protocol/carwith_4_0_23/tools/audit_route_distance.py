"""Verify route-distance candidates against APK DEX bytes and cached call indexes.

Writes only to the requested output directory. No app installation or provider activation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

EXPECTED_APK = 'c897a45d92c84f06e670fc4edd323824093a093f67d8e7d7b058fee2a737d06c'
CLASSES = {
    'classes2.dex': ('com.carwith.launcher.LauncherDataBusClient',
                     'com.carwith.launcher.map.m$a',
                     'com.carwith.launcher.card.v2.widget.NavProgressBaseView',
                     'com.carwith.launcher.notification.view.UcarNotifyMapView'),
    'classes5.dex': ('com.ucar.map.UCarMapInfo',),
    'classes8.dex': ('net.easyconn.carman.sdk_communication.P2C.ECP_P2C_PHONE_HUDINFO',
                     'net.easyconn.carman.sdk_communication.P2C.ECP_P2C_PHONE_HUDINFO$HUDINFO',
                     'net.easyconn.carman.bridge.BMapBridge$NavigationInfo',
                     'net.easyconn.carman.bridge.BMapBridge'),
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apk', type=Path, required=True)
    parser.add_argument('--cache', type=Path, required=True)
    parser.add_argument('--dexdump', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert sha(args.apk.read_bytes()) == EXPECTED_APK, 'Unexpected APK identity'
    args.output.mkdir(parents=True, exist_ok=True)
    dex_hashes = {}
    with zipfile.ZipFile(args.apk) as apk:
        for name in apk.namelist():
            if re.fullmatch(r'classes\d*\.dex', name):
                data = apk.read(name)
                assert data == (args.cache / name).read_bytes(), f'Cached DEX differs: {name}'
                dex_hashes[name] = sha(data)

    verified = {}
    texts = {}
    for dex, names in CLASSES.items():
        wanted = {name + '.txt' for name in names}
        seen = set()
        with zipfile.ZipFile(args.cache / Path(dex).stem / 'all-classes.zip') as cached:
            process = subprocess.Popen([str(args.dexdump), '-d', '-n', str(args.cache / dex)],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True, encoding='utf-8', errors='replace')
            block = []
            def flush():
                text = ''.join(block)
                match = re.search(r"Class descriptor\s*: '([^']+)'", text)
                if not match:
                    return
                name = match[1][1:-1].replace('/', '.') + '.txt'
                if name not in wanted:
                    return
                data = text.encode('utf-8')
                assert cached.read(name) == data, f'Cached disassembly differs: {dex}:{name}'
                dest = args.output / Path(dex).stem / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
                texts[name] = text
                verified[dex + ':' + name] = sha(data)
                seen.add(name)
            for line in process.stdout:
                if re.match(r'^Class #\d+', line):
                    flush()
                    block = []
                block.append(line)
            flush()
            error = process.stderr.read()
            assert process.wait() == 0, error
            assert seen == wanted, (dex, wanted - seen)
        print(f'PASS fresh DEX disassembly: {dex}, {len(seen)} selected classes', flush=True)

    def instruction(name, offset, *needles):
        rows = [line for line in texts[name].splitlines() if line.startswith(offset + ':')]
        assert len(rows) == 1 and all(needle in rows[0] for needle in needles), (name, offset, rows)
    hud = 'net.easyconn.carman.sdk_communication.P2C.ECP_P2C_PHONE_HUDINFO.txt'
    model = 'net.easyconn.carman.sdk_communication.P2C.ECP_P2C_PHONE_HUDINFO$HUDINFO.txt'
    instruction(model, '200454', 'iget ', '.k:I')
    instruction(model, '2005dc', 'iput ', '.k:I')
    instruction(model, '20049c', 'iget ', '.i:I')
    instruction(hud, '200dc2', 'const-string', '"roadRemainingDistance"')
    instruction(hud, '200dee', 'const-string', '"destinationRemainingDistance"')
    instruction(hud, '200df6', 'getDestinationRemainingDistance:()I')
    instruction(hud, '200dfe', 'JSONObject;.put:(Ljava/lang/String;I)')
    instruction(hud, '200cec', '#00020110')
    instruction(hud, '200e50', 'Calendar;.add:(II)V')
    launcher = 'com.carwith.launcher.LauncherDataBusClient.txt'
    instruction(launcher, '17ae84', 'Intent;.putExtra:(Ljava/lang/String;I)')
    instruction(launcher, '17afd0', 'UCarMapInfo;.getTitle1')
    instruction(launcher, '17afd8', 'UCarMapInfo;.getTitle2')

    queries = {
        'destination_distance_setter': 'ECP_P2C_PHONE_HUDINFO$HUDINFO;.setDestinationRemainingDistance:',
        'destination_distance_getter': 'ECP_P2C_PHONE_HUDINFO$HUDINFO;.getDestinationRemainingDistance:',
        'hudinfo_input': 'ECP_P2C_PHONE_HUDINFO;.setHudinfo:',
        'hudinfo_constructor': 'ECP_P2C_PHONE_HUDINFO;.<init>:',
        'navigation_distance_getter': 'BMapBridge$NavigationInfo;.getRemainDistance:',
        'navigation_distance_setter': 'BMapBridge$NavigationInfo;.setRemainDistance:',
    }
    refs = {key: [] for key in queries}
    index_hashes = {}
    methods_scanned = 0
    for path in sorted(args.cache.glob('classes*/references.jsonl')):
        index_hashes[path.parent.name] = sha(path.read_bytes())
        for line in path.open(encoding='utf-8'):
            row = json.loads(line)
            methods_scanned += 1
            for key, target in queries.items():
                if any(target in actual for actual in row['targets']):
                    refs[key].append({'dex': path.parent.name, 'method': row['method'], 'offset': row['offset']})
    assert len(index_hashes) == 8, 'Incomplete call index'
    report = {'scope': 'Static APK dataflow and cached full-DEX call index; no live provider/unit/vehicle claim',
              'apk_sha256': EXPECTED_APK, 'dex_sha256': dex_hashes,
              'fresh_class_disassembly_sha256': verified, 'references_index_sha256': index_hashes,
              'methods_scanned': methods_scanned, 'callers': refs,
              'destination_remaining_distance': {'command': '0x20110', 'json_key': 'destinationRemainingDistance',
                  'type': 'int', 'model_field': 'HUDINFO.k', 'getter_code_item': 'classes8:200444',
                  'setter_code_item': 'classes8:2005cc', 'json_put_instruction': 'classes8:200dfe',
                  'unit': 'OPEN', 'current_mixing_provider': 'not found'},
              'native_text_candidates': ['ucar.map.bundle.TITLE_1', 'ucar.map.bundle.TITLE_2']}
    (args.output / 'route-distance-audit.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS candidate dataflow; scanned', methods_scanned, 'methods; caller counts:', {key: len(value) for key, value in refs.items()})

if __name__ == '__main__':
    main()
