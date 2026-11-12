"""Validate evidence counts, internal links, CSV hashes and the standalone HTML data."""
import csv
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import zipfile
from extract import ROOT, sha, save

def main():
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    classes=json.loads((ROOT/'inventory/classes.json').read_text(encoding='utf-8'))
    counts={'classes':len(classes),'fields':sum(len(c['fields']) for c in classes),'methods':sum(len(c['methods']) for c in classes),'methods_with_code':sum(bool(m['code_offset']) for c in classes for m in c['methods'])}
    for key in ('classes','fields','methods'):assert counts[key]==manifest['counts'][key]
    assert counts['methods_with_code']==222476
    csvs=json.loads((ROOT/'inventory/file_manifest.json').read_text(encoding='utf-8'))
    for row in csvs:
        p=ROOT/row['path'];assert sha(p.read_bytes())==row['sha256'],row['path']
        with p.open(encoding='utf-8-sig',newline='') as f:n=sum(1 for _ in csv.DictReader(f))
        assert n==row['rows'],(row['path'],n,row['rows'])
    fp={x['path']:x['rows'] for x in csvs}
    assert fp['inventory/all_dex_fields.csv']==counts['fields']
    assert fp['inventory/all_dex_methods.csv']==counts['methods']
    assert fp['inventory/serialized_fields.csv']==266
    assert fp['inventory/binder_methods.csv']==616
    assert fp['inventory/proto_fields.csv']==342
    assert fp['inventory/proto_enums.csv']==157
    assert fp['inventory/key_usage.csv']==2185
    audit=json.loads((ROOT/'inventory/assembly_verification.json').read_text(encoding='utf-8'))
    assert audit['apk_sha256']==manifest['apk_sha256'];assert audit['classes_verified']==counts['classes']
    schema=json.loads((ROOT/'inventory/proto_schema_validation.json').read_text(encoding='utf-8'))
    assert len(schema)==342 and sum(x['status']=='match' for x in schema)==300
    tagsets={}
    for row in schema:
        key=(row['source'],row['message']); tags=tagsets.setdefault(key,set());assert row['number'] not in tags,(key,row['number']);tags.add(row['number'])
        line=(ROOT/'source'/row['source']).read_text(encoding='utf-8').splitlines()[row['line']-1]
        assert re.search(r'\b'+re.escape(row['name'])+r'\s*=\s*'+str(row['number'])+r'\s*;',line),row
    missing=[];linkcount=0
    for p in ROOT.glob('*.md'):
        for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if link.startswith(('http:','https:','#')):continue
            linkcount+=1
            if not (p.parent/link.split('#')[0]).exists():missing.append((p.name,link))
    assert not missing,missing
    doc=(ROOT/'CarWith字段与接口分析.html').read_text(encoding='utf-8')
    embedded=re.search(r'<script type="application/json" id="data">(.*?)</script>',doc,re.S); assert embedded
    data=json.loads(embedded[1]);searchrows=sum(len(v['rows']) for v in data.values());assert searchrows==5364
    assert len(data['Protobuf 字段']['rows'])==342 and len(data['JSON 序列化名称']['rows'])==266
    assert 'script src=' not in doc and '<iframe' not in doc
    class Parser(HTMLParser):
        def __init__(self):super().__init__();self.ids=[];self.links=[]
        def handle_starttag(self,tag,attrs):
            d=dict(attrs)
            if 'id' in d:self.ids.append(d['id'])
            if tag=='a' and 'href' in d:self.links.append(d['href'])
    parser=Parser();parser.feed(doc);assert len(parser.ids)==len(set(parser.ids))
    for link in parser.links:
        if link.startswith('#'):assert link[1:] in parser.ids,link
        elif not link.startswith(('http:','https:')):assert (ROOT/link).exists(),link
    apk=Path(manifest['apk']);assert sha(apk.read_bytes())==manifest['apk_sha256']
    with zipfile.ZipFile(apk) as z:assert len(z.infolist())==manifest['entries']
    result={'status':'passed','apk_sha256':manifest['apk_sha256'],'definition_counts':counts,'csv_files_validated':len(csvs),'markdown_links_validated':linkcount,'html_searchable_rows':searchrows,'proto_fields_source_line_checks':342,'proto_fields_compiled_tag_matches':300,'assembly_classes_byte_compared':audit['classes_verified'],'limitations':'HTML syntax/data/internal links checked; no live APK execution or remote API validation'}
    save('inventory/report_validation.json',result);print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
