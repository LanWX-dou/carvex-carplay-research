"""Supplement the static inventory with ELF exports, path candidates and wire evidence."""
import argparse
import json
from pathlib import Path
import re
import struct
import zipfile
from extract import ROOT, Dex, APP, csvfile, save, jtype, sha

def elf_symbols(b):
    if b[:5]!=b'\x7fELF\x02': return []
    order='<' if b[5]==1 else '>'
    shoff=struct.unpack_from(order+'Q',b,40)[0]; shsize,shnum=struct.unpack_from(order+'HH',b,58)
    sections=[struct.unpack_from(order+'IIQQQQIIQQ',b,shoff+i*shsize) for i in range(shnum)]
    result=[]
    for s in sections:
        if s[1]!=11:continue
        strings=sections[s[6]]; st=b[strings[4]:strings[4]+strings[5]]
        for p in range(s[4],s[4]+s[5],s[9] or 24):
            name,info,other,section,value,size=struct.unpack_from(order+'IBBHQQ',b,p)
            if name==0 or section==0:continue
            end=st.find(b'\0',name); nm=st[name:end].decode('utf-8','replace')
            if info>>4 not in (1,2):continue
            result.append({'symbol':nm,'type':info&15,'binding':info>>4,'address':f'0x{value:x}','size':size})
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('apk',type=Path);ap.add_argument('--cache',type=Path,required=True);args=ap.parse_args()
    cs=json.loads((ROOT/'inventory/classes.json').read_text(encoding='utf-8')); cmap={c['class']:c for c in cs}
    entries=[];symbols=[];paths=[];uuids=[];nested=[]; actions=[]
    serial=[];markers=[];sdkfields=[]
    for c in cs:
        for f in c['fields']:
            for a in f['annotations']:
                if a['type'] in ('Lcom/google/gson/annotations/SerializedName;','Lcom/fasterxml/jackson/annotation/JsonProperty;'):
                    serial.append({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'wire_name':a['values'].get('value',''),'annotation':a})
                if a['type']=='Lcom/fasterxml/jackson/annotation/g;':
                    markers.append({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'annotation':a,'status':'obfuscated enum field marker; not a JSON property name'})
            if not f['static'] and c['class'].startswith('Lcom/xiaomi/ai/api/'):
                sdkfields.append({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'required_annotation':any(a['type']=='Lcom/xiaomi/ai/api/common/Required;' for a in f['annotations']),'annotations':f['annotations'],'status':'SDK model definition; active CarWith use not established'})
    csvfile('serialized_fields.csv',serial,['dex','class','field','type','wire_name','annotation'])
    csvfile('enum_annotation_markers.csv',markers,['dex','class','field','type','annotation','status'])
    csvfile('sdk_ai_model_fields.csv',sdkfields,['dex','class','field','type','required_annotation','annotations','status'])
    with zipfile.ZipFile(args.apk) as z:
        for i in z.infolist():
            entries.append({'name':i.filename,'bytes':i.file_size,'compressed_bytes':i.compress_size,'crc32':f'{i.CRC:08x}'})
            if i.filename.endswith('.so'):
                symbols.extend({'library':i.filename,**s} for s in elf_symbols(z.read(i.filename)))
            if i.filename.endswith(('.rpk','.zip')):
                import io
                b=z.read(i.filename)
                if zipfile.is_zipfile(io.BytesIO(b)):
                    with zipfile.ZipFile(io.BytesIO(b)) as inner:
                        nested.extend({'archive':i.filename,'name':x.filename,'bytes':x.file_size} for x in inner.infolist())
            if re.fullmatch(r'classes\d*\.dex',i.filename):
                d=Dex(z.read(i.filename),i.filename)
                for idx,s in enumerate(d.strings):
                    if re.fullmatch(r'/(?:[A-Za-z0-9_.~-]+/)*[A-Za-z0-9_.~-]+/?(?:\?[^\s]{0,150})?',s) and len(s)<=220:
                        paths.append({'dex':i.filename,'string_index':idx,'path':s,'status':'literal candidate; may be API, file path, or SDK route'})
                    if re.fullmatch(r'[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}',s):uuids.append({'dex':i.filename,'string_index':idx,'uuid':s})
                    if re.fullmatch(r'(?:mix_|carlife_|ucar\.|com\.miui\.carlink\.(?:action|intent)\.)[A-Za-z0-9_.$]+',s):actions.append({'dex':i.filename,'string_index':idx,'value':s})
    csvfile('apk_entries.csv',entries,['name','bytes','compressed_bytes','crc32'])
    csvfile('native_exports.csv',symbols,['library','symbol','type','binding','address','size'])
    csvfile('relative_path_candidates.csv',paths,['dex','string_index','path','status'])
    csvfile('uuid_literals.csv',uuids,['dex','string_index','uuid'])
    csvfile('action_literals.csv',actions,['dex','string_index','value'])
    csvfile('nested_archive_entries.csv',nested,['archive','name','bytes'])
    models=[];consts=[]
    for c in cs:
        if c['class'].startswith(('Lcom/carwith/common/bean/','Lcb/','Lx1/','Lcom/miui/carlink/databus/p2cdatastructure/','Lcom/miui/carlink/databus/sensor/')) or c['class'] in ('Lcom/ucar/map/UCarMapInfo;','Lcom/baidu/carlife/mixing/CastConfig;','Lcom/baidu/carlife/mixing/MusicInfo;'):
            models.extend({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'annotations':f['annotations']} for f in c['fields'] if not f['static'])
        if c['class']=='Lcom/miui/carlink/databus/ControlChannel;':
            consts.extend({'dex':c['dex'],'class':c['class'],'field':f['name'],'type':jtype(f['type']),'value':f['value']} for f in c['fields'] if 'value' in f)
    csvfile('business_model_fields.csv',models,['dex','class','field','type','annotations'])
    csvfile('control_constants.csv',consts,['dex','class','field','type','value'])
    checks=[]
    for row in json.loads((ROOT/'inventory/proto_fields.json').read_text(encoding='utf-8')):
        prefix='Lcom/miui/carlink/databus/proto/UCarProto' if row['source']=='ucar.proto' else 'Lcom/ucar/databus/proto/ShareProto'
        classname=prefix+'$'+row['message'].replace('.','$')+';'; c=cmap.get(classname)
        norm=lambda s: re.sub('[^A-Z0-9]','',s.upper())
        f=next((f for f in c['fields'] if norm(f['name'])==norm(row['name']+'_FIELD_NUMBER')),None) if c else None
        checks.append({**row,'class':classname,'dex_number':f.get('value') if f else None,'status':'match' if f and f.get('value')==row['number'] else 'embedded schema only; no matching compiled field'})
    save('inventory/proto_schema_validation.json',checks)
    sourceowners={'Lca/a;','Lca/b;','Lca/c;','Lca/d;','Lca/h;','Lca/j;','Lca/k;','Lca/l;','Lca/n;','Lmr/r$a;','Leb/a;','Leb/b;','Leb/d;','Lhj/c;','Lyi/a;','Lsh/b;','Lth/a;','Ll2/a;','Ll2/d;','Lx1/a;','Lcom/carwith/launcher/map/a$a;','Lcom/xiaomi/micloudsdk/request/utils/b;'}
    sourceowners|={c['class'] for c in cs if c['class'].startswith(('Lcom/miui/carlink/databus/protocol/','Lcom/miui/carlink/databus/p2cdatastructure/')) and '$' not in c['class']}
    asm=json.loads((ROOT/'inventory/assembly_sources.json').read_text(encoding='utf-8')); service=[]
    for zp in args.cache.glob('classes*/all-classes.zip'):
        with zipfile.ZipFile(zp) as z:
            for owner in sourceowners:
                fn=owner[1:-1].replace('/','.')+'.txt'
                if fn not in z.namelist():continue
                text=z.read(fn).decode('utf-8');p=ROOT/'source/dexdump'/zp.parent.name/fn;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');asm.append(str(p.relative_to(ROOT)))
                if owner not in ('Lca/j;','Lca/h;'):continue
                current='';offset='';regs={}
                for line in text.splitlines():
                    h=re.match(r'^[0-9a-f]+:[^|]*\|\[([0-9a-f]+)\]\s*(.*)',line)
                    if h: offset,current=h.groups();regs={};continue
                    m=re.search(r'\|[0-9a-f]+:\s*const(?:/4|/16)?\s+(v\d+),.*// #([0-9a-f]+)$',line)
                    if m:regs[m[1]]=int(m[2],16)
                    m=re.search(r'invoke-virtual \{(v\d+), (v\d+)\}, Lca/l;\.f:\(I\)',line)
                    if m and m[2] in regs:
                        message=re.search(r'UCarProto\$([^;$]+)[;$]',current)
                        if message:service.append({'dex':zp.parent.name+'.dex','method':current,'code_offset':offset,'message':message[1],'service_id':regs[m[2]],'category':'AUTH' if owner=='Lca/h;' else 'CONTROL'})
    save('inventory/assembly_sources.json',sorted(set(asm)))
    csvfile('wire_service_ids.csv',service,['dex','method','code_offset','message','service_id','category'])
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    manifest['enrichment_counts']['serialized_fields']=len(serial)
    manifest['supplement_counts']={'native_exports':len(symbols),'relative_path_candidates':len(paths),'uuid_literals':len(uuids),'action_literals':len(actions),'nested_archive_entries':len(nested),'compiled_proto_fields_matched':sum(x['status']=='match' for x in checks),'wire_service_id_records':len(service),'business_model_fields':len(models),'sdk_ai_model_fields':len(sdkfields),'enum_annotation_markers':len(markers)}
    save('manifest.json',manifest);print(json.dumps(manifest['supplement_counts']))

if __name__=='__main__':main()
