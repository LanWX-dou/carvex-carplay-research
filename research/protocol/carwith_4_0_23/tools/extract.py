"""Offline APK inventory, using only Python's standard library and Android SDK.

DEX annotations/values are read directly from APK bytes. Existing dexdump
archives may be reused only after exact DEX hashes match the APK.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
APP = ('Lcom/carwith/', 'Lcom/miui/carlink/', 'Lcom/ucar/', 'Lcom/baidu/carlife/mixing/', 'Lnet/easyconn/carman/')
SDK = Path(r'C:\Users\admin\AppData\Local\Android\Sdk\build-tools\36.0.0')

def sha(b): return hashlib.sha256(b).hexdigest()
def save(name, data):
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    # DEX uses modified UTF-8, which may contain unpaired UTF-16 surrogates.
    # Escape those code units so the inventory remains valid UTF-8 JSON.
    p.write_bytes(json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8', 'backslashreplace'))
def csvfile(name, rows, keys):
    p = ROOT / 'inventory' / name
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', encoding='utf-8-sig', errors='backslashreplace', newline='') as f:
        w = csv.DictWriter(f, keys, extrasaction='ignore')
        w.writeheader()
        for row in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k,v in row.items()})
def jtype(s):
    n = len(s)-len(s.lstrip('[')); s=s[n:]
    return ({'V':'void','Z':'boolean','B':'byte','S':'short','C':'char','I':'int','J':'long','F':'float','D':'double'}.get(s, s.strip('L;').replace('/','.')) + '[]'*n)
def signature(name, desc):
    args, ret=desc.split(')'); args=args[1:]
    parts=re.findall(r'\[*L[^;]+;|\[*[ZBSCIJFD]',args)
    return f'{jtype(ret)} {name}('+', '.join(jtype(x) for x in parts)+')'

class Dex:
    def __init__(self,b,name):
        self.b,self.name=b,name
        assert b[:4]==b'dex\n'
        assert self.u(32)==len(b)
        assert hashlib.sha1(b[32:]).digest()==b[12:32]
        import zlib
        assert zlib.adler32(b[12:]) & 0xffffffff == self.u(8)
        self.strings=[]
        for i in range(self.u(56)):
            p=self.u(self.u(60)+4*i); _,p=self.uleb(p)
            e=b.index(0,p)
            self.strings.append(b[p:e].replace(b'\xc0\x80',b'\0').decode('utf-8','surrogatepass'))
        self.types=[self.strings[self.u(self.u(68)+4*i)] for i in range(self.u(64))]
        self.protos=[]
        for i in range(self.u(72)):
            p=self.u(76)+12*i; po=self.u(p+8)
            pars=[self.types[self.h(po+4+2*j)] for j in range(self.u(po))] if po else []
            self.protos.append('('+''.join(pars)+')'+self.types[self.u(p+4)])
        self.fields=[]
        for i in range(self.u(80)):
            p=self.u(84)+8*i
            self.fields.append((self.types[self.h(p)],self.strings[self.u(p+4)],self.types[self.h(p+2)]))
        self.methods=[]
        for i in range(self.u(88)):
            p=self.u(92)+8*i
            self.methods.append((self.types[self.h(p)],self.strings[self.u(p+4)],self.protos[self.h(p+2)]))
    def u(self,p): return struct.unpack_from('<I',self.b,p)[0]
    def h(self,p): return struct.unpack_from('<H',self.b,p)[0]
    def uleb(self,p):
        v=0; shift=0
        while True:
            x=self.b[p]; p+=1; v|=(x&127)<<shift
            if x<128: return v,p
            shift+=7
    def value(self,p):
        header=self.b[p]; p+=1; typ=header&31; size=(header>>5)+1
        if typ==0x1e: return None,p
        if typ==0x1f: return bool(header>>5),p
        if typ==0x1c:
            n,p=self.uleb(p); out=[]
            for _ in range(n):
                v,p=self.value(p); out.append(v)
            return out,p
        if typ==0x1d: return self.annotation(p)
        raw=self.b[p:p+size]; p+=size; v=int.from_bytes(raw,'little')
        if typ==0x17: v=self.strings[v]
        elif typ==0x18: v=self.types[v]
        elif typ in (0x19,0x1b): v={'field':self.fields[v]}
        elif typ==0x1a: v={'method':self.methods[v]}
        elif typ in (0,2,4,6): v=int.from_bytes(raw,'little',signed=True)
        elif typ in (0x10,0x11):
            full=4 if typ==0x10 else 8
            v=struct.unpack('<f' if full==4 else '<d', bytes(full-size)+raw)[0]
        return v,p
    def annotation(self,p):
        t,p=self.uleb(p); n,p=self.uleb(p); values={}
        for _ in range(n):
            key,p=self.uleb(p); v,p=self.value(p); values[self.strings[key]]=v
        return {'type':self.types[t],'values':values},p
    def aset(self,p):
        return [self.annotation(self.u(p+4+4*i)+1)[0] for i in range(self.u(p))] if p else []
    def classes(self):
        for i in range(self.u(96)):
            p=self.u(100)+32*i; owner=self.types[self.u(p)]; data=self.u(p+24)
            fields=[]; methods=[]; static=[]
            if data:
                counts=[]
                for _ in range(4): n,data=self.uleb(data); counts.append(n)
                for kind,n in enumerate(counts):
                    idx=0
                    for _ in range(n):
                        delta,data=self.uleb(data); idx+=delta; access,data=self.uleb(data)
                        if kind<2:
                            _,name,t=self.fields[idx]; f={'index':idx,'name':name,'type':t,'access':access,'static':kind==0,'annotations':[]}; fields.append(f)
                            if kind==0: static.append(f)
                        else:
                            co,data=self.uleb(data); _,name,t=self.methods[idx]
                            methods.append({'index':idx,'name':name,'type':t,'access':access,'code_offset':f'{co:08x}' if co else None,'annotations':[],'parameter_annotations':[]})
            vals=self.u(p+28)
            if vals:
                n,vals=self.uleb(vals)
                for k in range(n): v,vals=self.value(vals); static[k]['value']=v
            ann=self.u(p+20); ca=[]
            if ann:
                ca=self.aset(self.u(ann)); fc,mc,pc=[self.u(ann+x) for x in (4,8,12)]; ap=ann+16
                fm={f['index']:f for f in fields}; mm={m['index']:m for m in methods}
                for n,target in ((fc,fm),(mc,mm)):
                    for _ in range(n):
                        idx,off=self.u(ap),self.u(ap+4); ap+=8
                        if idx in target: target[idx]['annotations']=self.aset(off)
                for _ in range(pc):
                    idx,off=self.u(ap),self.u(ap+4); ap+=8
                    if idx in mm: mm[idx]['parameter_annotations']=[self.aset(self.u(off+4+4*k)) for k in range(self.u(off))]
            io=self.u(p+12); interfaces=[self.types[self.h(io+4+2*k)] for k in range(self.u(io))] if io else []
            yield {'dex':self.name,'class':owner,'access':self.u(p+4),'superclass':self.types[self.u(p+8)] if self.u(p+8)!=0xffffffff else None,'interfaces':interfaces,'annotations':ca,'fields':fields,'methods':methods}

def axml(b):
    def u(p):return struct.unpack_from('<I',b,p)[0]
    def h(p):return struct.unpack_from('<H',b,p)[0]
    strings=[]; stack=[]; root=None; p=8
    def st(i):return strings[i] if i!=0xffffffff else ''
    while p<len(b):
        kind,hs,size=h(p),h(p+2),u(p+4)
        if kind==1:
            n,flags,start=u(p+8),u(p+16),u(p+20)
            for i in range(n):
                q=p+start+u(p+hs+4*i)
                if flags&256:
                    for _ in range(2):
                        x=b[q]; q+=1
                        if x&128:x=((x&127)<<8)|b[q];q+=1
                    strings.append(b[q:q+x].decode('utf-8','replace'))
                else:
                    x=h(q);q+=2
                    if x&32768:x=((x&32767)<<16)|h(q);q+=2
                    strings.append(b[q:q+x*2].decode('utf-16-le'))
        elif kind==0x102:
            name=st(u(p+20)); node=ET.Element(name); start,asz,n=h(p+24),h(p+26),h(p+28)
            for i in range(n):
                q=p+16+start+i*asz; ns,key,raw=u(q),st(u(q+4)),u(q+8);typ=b[q+15];value=u(q+16)
                if raw!=0xffffffff:v=st(raw)
                elif typ==3:v=st(value)
                elif typ==18:v='true' if value else 'false'
                elif typ in (16,17):v=str(value) if typ==16 else hex(value)
                elif typ==1:v=f'@0x{value:08x}'
                else:v=f'0x{value:08x}'
                if ns!=0xffffffff:key='{'+st(ns)+'}'+key
                node.set(key,v)
            if stack:stack[-1].append(node)
            else:root=node
            stack.append(node)
        elif kind==0x103:stack.pop()
        p+=size
    ET.register_namespace('android','http://schemas.android.com/apk/res/android');ET.indent(root)
    return root

def proto_rows(text,source):
    fields=[];enums=[];stack=[];pending=''
    for lineno,line in enumerate(text.splitlines(),1):
        # Keep comments exactly as supplied; corrupted source comments are not repaired.
        code,_,comment=line.partition('//'); code=code.strip()
        m=re.match(r'(message|enum)\s+(\w+)\s*\{',code)
        if m:stack.append((m[1],m[2]));continue
        if code.startswith('}'):
            if stack:stack.pop()
            continue
        if not stack:continue
        if stack[-1][0]=='enum':
            m=re.match(r'(\w+)\s*=\s*(-?(?:0x[0-9A-Fa-f]+|\d+))\s*;',code)
            if m:enums.append({'source':source,'enum':'.'.join(x[1] for x in stack),'name':m[1],'value':int(m[2],0) if 'x' in m[2] else int(m[2]),'line':lineno,'comment':comment.strip()})
        else:
            m=re.match(r'(?:(optional|repeated)\s+)?(\w+(?:\.\w+)*)\s+(\w+)\s*=\s*(\d+)\s*;',code)
            if m:fields.append({'source':source,'message':'.'.join(x[1] for x in stack),'cardinality':m[1] or 'singular','type':m[2],'name':m[3],'number':int(m[4]),'line':lineno,'comment':comment.strip()})
    return fields,enums

def main():
    ap=argparse.ArgumentParser();ap.add_argument('apk',type=Path);ap.add_argument('--cache',type=Path);args=ap.parse_args()
    z=zipfile.ZipFile(args.apk); (ROOT/'source').mkdir(parents=True,exist_ok=True)
    manifest={'apk':str(args.apk.resolve()),'apk_bytes':args.apk.stat().st_size,'apk_sha256':sha(args.apk.read_bytes()),'analysis_date':'2026-11-12','dex':[],'entries':len(z.infolist()),'native':[]}
    classes=[];urls=[];http=[];serialized=[]
    for name in z.namelist():
        if not re.fullmatch(r'classes\d*\.dex',name):continue
        b=z.read(name);d=Dex(b,name);cs=list(d.classes());classes+=cs
        manifest['dex'].append({'name':name,'sha256':sha(b),'bytes':len(b),'classes':len(cs),'strings':len(d.strings),'method_ids':len(d.methods),'field_ids':len(d.fields)})
        if args.cache:assert sha((args.cache/name).read_bytes())==sha(b),f'Cache mismatch {name}'
        for i,s in enumerate(d.strings):
            for u in re.findall(r'(?:https?|wss?|content)://[^\s\x00<>"\x27]+',s):urls.append({'dex':name,'string_index':i,'url':u,'context':s[:600]})
        for c in cs:
            for f in c['fields']:
                for a in f['annotations']:
                    if 'SerializedName' in a['type'] or 'JsonProperty' in a['type']:
                        serialized.append({'dex':name,'class':c['class'],'field':f['name'],'type':jtype(f['type']),'annotation':a})
            for m in c['methods']:
                anns=[a for a in m['annotations'] if a['type'].startswith('Lretrofit2/http/')]
                if anns:http.append({'dex':name,'class':c['class'],'method':m['name'],'descriptor':m['type'],'signature':signature(m['name'],m['type']),'annotations':anns,'parameters':m['parameter_annotations']})
        print(name,len(cs),flush=True)
    root=axml(z.read('AndroidManifest.xml')); ET.ElementTree(root).write(ROOT/'source'/'AndroidManifest.xml',encoding='utf-8',xml_declaration=True)
    ns='{http://schemas.android.com/apk/res/android}'
    manifest['package']=root.get('package'); manifest['versionCode']=root.get(ns+'versionCode');manifest['versionName']=root.get(ns+'versionName');manifest['sdk']=root.find('uses-sdk').attrib
    components=[]
    for node in root.find('application'):
        if node.tag not in ('activity','activity-alias','service','receiver','provider'):continue
        components.append({'kind':node.tag,'name':node.get(ns+'name'),'exported':node.get(ns+'exported','unspecified'),'permission':node.get(ns+'permission',''),'authorities':node.get(ns+'authorities',''),'actions':[x.get(ns+'name') for x in node.findall('intent-filter/action')],'attributes':node.attrib})
    manifest['application_attributes']=root.find('application').attrib
    permissions=[{'kind':x.tag,**{k.replace(ns,''):v for k,v in x.attrib.items()}} for x in root if x.tag in ('permission','uses-permission')]
    pf=[];pe=[];jsonrows=[];asset_info=[]
    for name in z.namelist():
        if name in ('ucar.proto','share.proto'):
            text=z.read(name).decode('utf-8').replace('\r\r\n','\n').replace('\r\n','\n')
            (ROOT/'source'/name).write_text(text,encoding='utf-8');f,e=proto_rows(text,name);pf+=f;pe+=e
        if name.endswith('.json'):
            try: obj=json.loads(z.read(name).decode('utf-8-sig'))
            except (ValueError,UnicodeDecodeError):continue
            asset_info.append({'source':name,'bytes':len(z.read(name)),'sha256':sha(z.read(name))})
            def walk(v,path):
                if isinstance(v,dict):
                    for k,x in v.items():walk(x,path+'.'+k)
                elif isinstance(v,list):
                    jsonrows.append({'source':name,'path':path,'type':'array','sample':None})
                    for x in v:walk(x,path+'[]')
                else:jsonrows.append({'source':name,'path':path,'type':type(v).__name__,'sample':str(v)[:250]})
            walk(obj,'$')
            # Original human-readable configuration is evidence, not a live response.
            p=ROOT/'source'/'assets'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(name))
        if name.endswith('.so'):
            b=z.read(name); strings=[x.decode('ascii') for x in re.findall(rb'[\x20-\x7e]{5,}',b)]
            relevant=sorted(set(x for x in strings if re.search(r'https?://|wss?://|Java_|JNI_OnLoad|ucar|carlink|carlife|socks|auth',x,re.I)))
            manifest['native'].append({'name':name,'bytes':len(b),'sha256':sha(b),'relevant_strings':len(relevant)})
            (ROOT/'source'/(Path(name).name+'.strings.txt')).write_text('\n'.join(relevant),encoding='utf-8')
    allfields=[];allmethods=[];binders=[];interfaces=[]
    for c in classes:
        for f in c['fields']:allfields.append({'dex':c['dex'],'class':c['class'],**f,'java_type':jtype(f['type'])})
        for m in c['methods']:allmethods.append({'dex':c['dex'],'class':c['class'],**m,'signature':signature(m['name'],m['type'])})
        if c['access']&0x200:interfaces.append(c)
        if 'Landroid/os/IInterface;' in c['interfaces']:binders.append(c)
    save('inventory/classes.json',classes)
    save('inventory/http_annotations.json',http);save('inventory/binder_interfaces.json',binders);save('inventory/components.json',components);save('inventory/permissions.json',permissions)
    save('inventory/proto_fields.json',pf);save('inventory/proto_enums.json',pe);save('inventory/serialized_fields.json',serialized)
    save('inventory/assets.json',asset_info)
    csvfile('all_dex_fields.csv',allfields,['dex','class','name','type','java_type','access','static','value','annotations'])
    csvfile('all_dex_methods.csv',allmethods,['dex','class','name','type','signature','access','code_offset','annotations','parameter_annotations'])
    csvfile('application_fields.csv',[f for f in allfields if f['class'].startswith(APP)],['dex','class','name','type','java_type','access','static','value','annotations'])
    csvfile('binder_methods.csv',[{'dex':c['dex'],'class':c['class'],**m,'signature':signature(m['name'],m['type'])} for c in binders for m in c['methods']],['dex','class','name','type','signature'])
    csvfile('application_interfaces.csv',[{'dex':c['dex'],'class':c['class'],**m,'signature':signature(m['name'],m['type'])} for c in interfaces if c['class'].startswith(APP) for m in c['methods']],['dex','class','name','type','signature'])
    csvfile('urls.csv',urls,['dex','string_index','url','context'])
    csvfile('proto_fields.csv',pf,['source','message','number','name','type','cardinality','line','comment']);csvfile('proto_enums.csv',pe,['source','enum','name','value','line','comment'])
    dedup={}
    for row in jsonrows:
        key=(row['source'],row['path'],row['type'])
        if key not in dedup:dedup[key]=row
    csvfile('asset_json_fields.csv',dedup.values(),['source','path','type','sample'])
    csvfile('components.csv',components,['kind','name','exported','permission','authorities','actions'])
    # Method references and exact assembly for application interop classes.
    if args.cache:
        refs=[];keywords=re.compile(r'https?://|wss?://|content://|mix_notify|hud_info|turn_icon|left_distance|left_time|remainDistance|LANE|navi',re.I)
        for rp in sorted(args.cache.glob('classes*/references.jsonl')):
            with rp.open(encoding='utf-8') as f:
                for line in f:
                    row=json.loads(line)
                    if any(keywords.search(s) for s in row['strings']):refs.append({'dex':rp.parent.name+'.dex',**row})
        save('inventory/string_references.json',refs)
        selected={c['class'] for c in binders if c['class'].startswith(APP)}
        selected|={c['class']+'$Stub;' for c in binders if c['class'].startswith(APP)}
        selected|={x['class'] for x in http}
        selected|={'Lcom/miui/carlink/databus/ControlChannel;','Lcom/miui/carlink/databus/DataBusService;','Lcom/miui/carlink/databus/DataBusService$DataBusServiceStub;','Lcom/carwith/launcher/LauncherDataBusClient;','Lp6/l;','Lr9/a;','Lr9/a$d;','Lcom/carwith/launcher/map/wms/j$b0;','Lcom/carwith/launcher/map/m$a;'}
        saved=[]
        for zp in sorted(args.cache.glob('classes*/all-classes.zip')):
            with zipfile.ZipFile(zp) as archive:
                for c in selected:
                    name=c.strip('L;').replace('/','.')+'.txt'
                    if name in archive.namelist():
                        p=ROOT/'source'/'dexdump'/zp.parent.name/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(archive.read(name));saved.append(str(p.relative_to(ROOT)))
        save('inventory/assembly_sources.json',saved)
    manifest['counts']={'classes':len(classes),'fields':len(allfields),'methods':len(allmethods),'application_fields':sum(f['class'].startswith(APP) for f in allfields),'binder_interfaces':len(binders),'binder_methods':sum(len(c['methods']) for c in binders),'retrofit_methods':len(http),'proto_fields':len(pf),'proto_enum_values':len(pe),'asset_json_field_paths':len(dedup),'url_occurrences':len(urls),'components':len(components)}
    save('manifest.json',manifest)
    print(json.dumps(manifest['counts']),flush=True)

if __name__=='__main__':main()
