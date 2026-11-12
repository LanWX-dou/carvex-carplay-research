"""Read-only original-byte audits used by task 0.2, with optional JSON report.

Requires Capstone 5.0.7. Reuses C16/C18 and compares the nine message bodies
and registration/constructor points directly with the pinned Mach-O image.
This is static verification, not native execution or vehicle interoperability.
"""
import argparse
import contextlib
import hashlib
import io
import json
import re
import runpy
import struct
import sys
from pathlib import Path

CHANGE = Path(__file__).resolve().parents[1]
ROOT = CHANGE.parents[2]
DOCSET = ROOT / 'research/protocol/iap2_input_business_lifecycle'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--deps', type=Path)
    parser.add_argument('--report', action='store_true')
    args = parser.parse_args()
    if args.deps:
        sys.path.insert(0, str(args.deps.resolve()))
    import capstone
    if capstone.__version__ != '5.0.7':
        raise RuntimeError(f'Expected Capstone 5.0.7, got {capstone.__version__}')
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        now = runpy.run_path(str(DOCSET / 'tools/verify-nowplaying-audit.py'))
        now['main']()
        life = runpy.run_path(str(DOCSET / 'tools/verify-lifecycle-audit.py'))
        life['main']()
    image = now['Image']()
    messages = {
        0x5000: ('accessory-to-phone', 0x1001499f0),
        0x5001: ('phone-to-accessory', 0x1001465c4),
        0x5002: ('accessory-to-phone', 0x10014a93c),
        0x5003: ('accessory-to-phone', 0x10014aa20),
        0x5200: ('accessory-to-phone', 0x10017527c),
        0x5201: ('phone-to-accessory', 0x1000027f4),
        0x5202: ('phone-to-accessory', 0x1001777c0),
        0x5203: ('accessory-to-phone', 0x10017593c),
        0x5204: ('phone-to-accessory', 0x100177d80),
    }
    records = {}
    instructions = {}
    for message, (direction, address) in messages.items():
        source = DOCSET / f'source/asm/accessoryd/f_{address:x}.s'
        text = source.read_text(encoding='utf-8')
        rows = re.findall(r'^(0x[0-9a-f]+):[ \t]*(\S+)[ \t]*([^\n]*)', text, re.M)
        expected = {int(a, 16): (m, operands.strip()) for a, m, operands in rows}
        actual = image.dis(address, max(expected) + 4)
        if actual != expected:
            raise ValueError(f'Original full slice differs: {address:x}')
        instructions.update(actual)
        records[f'{message:04x}'] = {
            'direction': direction, 'function': hex(address),
            'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'instructionCount': len(actual), 'fullSliceMatchesImage': True,
        }
    for table, entries in (
        (0x10021c038, [(0x5000, 0x1001499f0), (0x5002, 0x10014a93c), (0x5003, 0x10014aa20)]),
        (0x10021f620, [(0x5200, 0x10017527c), (0x5203, 0x10017593c), (0x0d01, 0x100175c70)]),
    ):
        for index, (message, handler) in enumerate(entries):
            raw_id, raw_pointer = struct.unpack('<QQ', image.read(table + index * 16, 16))
            if raw_id != message or 0x100000000 + (raw_pointer & 0xffffffffff) != handler:
                raise ValueError(f'Original handler registration differs: {message:04x}')
    anchors = {
        0x100146ac8: ('mov', 'w1, #0x5001'),
        0x100002a2c: ('mov', 'w1, #0x5201'),
        0x1001779fc: ('mov', 'w1, #0x5202'),
        0x100177f80: ('mov', 'w1, #0x5204'),
        0x100002abc: ('mov', 'w2, #1'),
        0x100002b0c: ('mov', 'w2, #3'),
        0x100002ba4: ('mov', 'w2, #7'),
        0x100002c0c: ('mov', 'w2, #0xa'),
    }
    for address, expected in anchors.items():
        if instructions[address] != expected:
            raise ValueError(f'Constructor/parameter identity differs: {address:x}')
    report = {
        'result': 'PASS', 'capstone': capstone.__version__,
        'imageSha256': hashlib.sha256(image.data).hexdigest(),
        'existingAuditOutput': output.getvalue().splitlines(),
        'messages': records, 'handlerRegistrations': 6,
        'anchors': {hex(address): list(value) for address, value in anchors.items()},
        'boundary': 'Static image/slice/branch checks; units, full field schemas, platform execution and vehicle behavior remain separately classified.',
    }
    if args.report:
        (CHANGE / 'protocol-audit.json').write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(output.getvalue(), end='')
    print(f'Protocol audit PASS: {len(records)} original message bodies, 6 registrations, {len(anchors)} constructor/parameter anchors')


if __name__ == '__main__':
    main()
