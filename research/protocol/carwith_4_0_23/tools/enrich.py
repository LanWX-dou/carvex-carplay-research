"""Recover obfuscated annotations and indexed literals; no network or APK execution."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import zipfile
from extract import ROOT, APP, Dex, csvfile, save, jtype, signature, sha

HTTP = {'Lpr/f;': 'GET', 'Lpr/o;': 'POST', 'Lpr/b;': 'DELETE', 'Lpr/g;': 'HEAD',
        'Lpr/m;': 'OPTIONS', 'Lpr/n;': 'PATCH', 'Lpr/p;': 'PUT'}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('apk', type=Path); ap.add_argument('--cache', type=Path, required=True); args = ap.parse_args()
    classes = json.loads((ROOT/'inventory/classes.json').read_text(encoding='utf-8'))
    cmap = {c['class']: c for c in classes}
    route_rows=[]; serial=[]; models=[]; transactions=[]; natives=[]; js=[]
    for c in classes:
        for m in c['methods']:
            a = next((a for a in m['annotations'] if a['type'] in HTTP or a['type'].startswith('Lretrofit2/http/')),None)
            if a:
                route_rows.append({'dex':c['dex'],'class':c['class'],'method':m['name'],'http_method':HTTP.get(a['type'],a['type'].split('/')[-1].strip(';')),'path':a['values'].get('value',''),'signature':signature(m['name'],m['type']),'annotations':m['annotations'],'parameters':m['parameter_annotations']})
            if m['access'] & 0x100: natives.append({'dex':c['dex'],'class':c['class'],'method':m['name'],'signature':signature(m['name'],m['type'])})
            if any(a['type']=='Landroid/webkit/JavascriptInterface;' for a in m['annotations']): js.append({'dex':c['dex'],'class':c['class'],'method':m['name'],'signature':signature(m['name'],m['type']),'code_offset':m['code_offset']})
        for f in c['fields']:
            for a in f['annotations']:
                if a['type'] in ('Lcom/google/gson/annotations/SerializedName;','Lcom/fasterxml/jackson/annotation/JsonProperty;'):
                    serial.append({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'wire_name':a['values'].get('value',''),'annotation':a})
            if f['name'].startswith('TRANSACTION_'):
                transactions.append({'dex':c['dex'],'class':c['class'],'method':f['name'][12:],'transaction':f.get('value'),'field':f['name']})
            if not f['static'] and (c['class'].startswith('Lcom/carwith/common/bean/') or c['class'].startswith(('Lcb/','Lx1/')) or c['class'] in ('Lcom/ucar/map/UCarMapInfo;', 'Lcom/miui/carlink/bean/NavigationInfo;', 'Lcom/miui/carlink/bean/MusicInfo;')):
                models.append({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'annotations':f['annotations']})
    csvfile('http_routes.csv',route_rows,['dex','class','method','http_method','path','signature','annotations','parameters'])
    save('inventory/http_annotations.json',route_rows)
    csvfile('serialized_fields.csv',serial,['dex','class','field','type','wire_name','annotation'])
    csvfile('business_model_fields.csv',models,['dex','class','field','type','annotations'])
    csvfile('binder_transactions.csv',transactions,['dex','class','method','transaction','field'])
    csvfile('native_methods.csv',natives,['dex','class','method','signature'])
    csvfile('javascript_interfaces.csv',js,['dex','class','method','signature','code_offset'])
    z=zipfile.ZipFile(args.apk); dexes={name:Dex(z.read(name),name) for name in z.namelist() if re.fullmatch(r'classes\d*\.dex',name)}
    literal_rows=[]; keys=[]; urlrefs=[]; relevant=[]; evidence=[]
    selector=re.compile(r'https?://|wss?://|content://|mix_notify|carlife_show_|ucar\.map\.bundle|LANE_GUIDANCE|remainDistance|remainTime')
    chosen={r['class'] for r in route_rows}|{'Lnr/n$b;', 'Lso/a0$a;', 'Ll2/a;', 'Ll2/d;', 'Lx1/a;', 'Lfb/d;'}
    for c in classes:
        if c['class'].startswith(('Lcb/','Lcom/carwith/common/bean/','Lcom/ucar/map/UCarMapInfo','Lcom/miui/carlink/bean/NavigationInfo','Lcom/miui/carlink/bean/MusicInfo')):
            chosen.add(c['class'])
    for rp in sorted(args.cache.glob('classes*/references.jsonl')):
        for line in rp.open(encoding='utf-8'):
            row=json.loads(line)
            if any(selector.search(s) for s in row['strings']):
                relevant.append({'dex':rp.parent.name+'.dex',**row}); chosen.add(row['owner'])
    save('inventory/string_references.json',relevant)
    # Linear register tracking is deliberately bounded to straight-line blocks.
    # Values through joins, reflection or calls are excluded rather than invented.
    insn=re.compile(r'^([0-9a-f]+):[^|]*\|([0-9a-f]+):\s*(\S+)\s*(.*)$')
    header=re.compile(r'^[0-9a-f]+:[^|]*\|\[([0-9a-f]+)\]\s*(.+)$')
    targets=re.compile(r'(L[^;]+;)\.([^:]+):(\([^ ]+)')
    binderowners={c['class'] for c in classes if 'Landroid/os/IInterface;' in c['interfaces'] and c['class'].startswith(APP)}
    for zp in sorted(args.cache.glob('classes*/all-classes.zip')):
        dexname=zp.parent.name+'.dex'; d=dexes[dexname]
        assert sha((args.cache/dexname).read_bytes())==sha(z.read(dexname))
        with zipfile.ZipFile(zp) as archive:
            for name in archive.namelist():
                owner='L'+name[:-4].replace('.','/')+';'
                # Nested class names retain '$'; dexdump archive uses dotted package names.
                if owner not in cmap: continue
                if not owner.startswith(APP+('Lcom/xiaomi/ucar/',)) and owner not in chosen: continue
                text=archive.read(name).decode('utf-8'); method=''; code=''; regs={}; block=[]
                joins={}; scan_code=''
                for scan_line in text.splitlines():
                    scan_head=header.match(scan_line)
                    if scan_head: scan_code=scan_head[1]; joins[scan_code]=set(); continue
                    scan_insn=insn.match(scan_line)
                    if scan_insn and scan_insn[3].startswith(('if-','goto')):
                        target=re.search(r'([0-9a-f]+)\s*//',scan_insn[4])
                        if target: joins.setdefault(scan_code,set()).add(int(target[1],16))
                if owner in chosen or owner in binderowners:
                    p=ROOT/'source/dexdump'/zp.parent.name/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8'); evidence.append(str(p.relative_to(ROOT)))
                for line in text.splitlines():
                    h=header.match(line)
                    if h: code,method=h.groups(); regs={}; continue
                    m=insn.match(line)
                    if not m: continue
                    addr,pc,op,operands=m.groups()
                    if int(pc,16) in joins.get(code,set()): regs={}
                    dest=re.match(r'(v\d+)',operands)
                    if op.startswith('const-string'):
                        index=re.search(r'string@([0-9a-f]+)',operands)
                        if index and dest:
                            value=d.strings[int(index[1],16)]; regs[dest[1]]=value
                            row={'dex':dexname,'class':owner,'method':method,'code_offset':code,'instruction_offset':addr,'string_index':int(index[1],16),'value':value}
                            literal_rows.append(row)
                            if re.search(r'(?:https?|wss?|content)://',value):urlrefs.append(row)
                        continue
                    if op.startswith('move') and not op.startswith(('move-result','move-exception')):
                        rr=re.findall(r'v\d+',operands)
                        if len(rr)>1 and rr[1] in regs: regs[rr[0]]=regs[rr[1]]
                        elif rr: regs.pop(rr[0],None)
                        continue
                    if op.startswith('invoke-'):
                        tar=targets.search(operands); registerpart=operands.split('}',1)[0]; rr=re.findall(r'v\d+',registerpart)
                        if '..' in registerpart and len(rr)==2: rr=['v'+str(i) for i in range(int(rr[0][1:]),int(rr[1][1:])+1)]
                        if tar and len(rr)>1:
                            cls,mn,desc=tar.groups()
                            category=None
                            if cls in ('Landroid/content/Intent;','Landroid/os/Bundle;','Landroid/os/BaseBundle;') and (mn.startswith(('put','get','has','contains')) or mn in ('setAction','<init>')):category='Intent/Bundle'
                            elif cls=='Lorg/json/JSONObject;' and mn.startswith(('put','get','opt','has','isNull')):category='JSON'
                            elif cls in ('Ljava/util/Map;','Ljava/util/HashMap;','Ljava/util/LinkedHashMap;') and mn in ('put','get','containsKey'):category='Map'
                            elif cls=='Landroid/content/ContentValues;' and mn=='put':category='ContentValues'
                            elif cls=='Landroid/database/Cursor;' and mn.startswith('getColumnIndex'):category='Cursor column'
                            elif cls in ('Landroid/content/SharedPreferences;','Landroid/content/SharedPreferences$Editor;') and mn.startswith(('put','get','contains')):category='Preference'
                            key=regs.get(rr[1])
                            if category and isinstance(key,str) and len(key)<500:
                                keys.append({'dex':dexname,'class':owner,'method':method,'code_offset':code,'instruction_offset':addr,'category':category,'key':key,'operation':mn,'target':cls+'.'+mn+':'+desc,'literal_value':regs.get(rr[2]) if len(rr)>2 else None,'confidence':'straight-line literal reference'})
                        continue
                    if op.startswith(('if-','goto','packed-switch','sparse-switch','return','throw')):
                        regs={};continue
                    if dest and not op.startswith(('iput','sput','aput','monitor','check-cast','nop')):regs.pop(dest[1],None)
    csvfile('key_usage.csv',keys,['dex','class','method','code_offset','instruction_offset','category','key','operation','target','literal_value','confidence'])
    csvfile('application_literals.csv',literal_rows,['dex','class','method','code_offset','instruction_offset','string_index','value'])
    csvfile('url_references.csv',urlrefs,['dex','class','method','code_offset','instruction_offset','string_index','value'])
    save('inventory/assembly_sources.json',sorted(set(evidence)))
    stats={'http_annotated_routes':len(route_rows),'serialized_fields':len(serial),'business_model_fields':len(models),'binder_transaction_constants':len(transactions),'native_methods':len(natives),'javascript_interfaces':len(js),'literal_key_usages':len(keys),'distinct_literal_keys':len(set(x['key'] for x in keys)),'url_reference_methods':len(urlrefs),'assembly_sources':len(set(evidence))}
    save('inventory/enrichment_counts.json',stats)
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'));manifest['counts']['retrofit_methods']=len(route_rows);manifest['enrichment_counts']=stats;save('manifest.json',manifest)
    print(json.dumps(stats,ensure_ascii=False))

if __name__=='__main__':main()
