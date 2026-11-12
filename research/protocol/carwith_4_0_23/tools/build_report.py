"""Build Chinese Markdown appendices and a standalone searchable HTML report."""
from collections import defaultdict
import csv
import html
import json
from pathlib import Path
import re
from urllib.parse import urlparse
from extract import ROOT, APP, jtype, signature, save, sha

def readcsv(name):
    with (ROOT/'inventory'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def table(head,rows):
    def cell(v):
        if v is None or v=='':return '—'
        return str(v).replace('|','\\|').replace('\n','<br>').replace('\r','')
    return '| '+' | '.join(head)+' |\n| '+' | '.join('---' for _ in head)+' |\n'+''.join('| '+' | '.join(cell(x) for x in row)+' |\n' for row in rows)+'\n'

def write(name,text): (ROOT/name).write_text(text,encoding='utf-8')

def inline(s):
    tokens=[]
    def stash(text):tokens.append(text);return f'\x01{len(tokens)-1}\x02'
    s=re.sub(r'`([^`]+)`',lambda m:stash('<code>'+html.escape(m[1])+'</code>'),s)
    s=html.escape(s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:'<a href="'+html.escape(html.unescape(m[2]),quote=True)+'">'+m[1]+'</a>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=s.replace('&lt;br&gt;','<br>')
    return re.sub(r'\x01(\d+)\x02',lambda m:tokens[int(m[1])],s)

def markdown(text):
    out=[];paragraph=[];intable=False;inlist=False;incode=False
    def flush():
        if paragraph:out.append('<p>'+inline(' '.join(paragraph))+'</p>');paragraph.clear()
    for line in text.splitlines():
        if line.startswith('```'):
            flush();out.append('</code></pre>' if incode else '<pre><code>');incode=not incode;continue
        if incode:out.append(html.escape(line)+'\n');continue
        if line.startswith('|'):
            flush()
            if not intable:out.append('<div class="table-wrap"><table>');intable=True;thead=True
            cells=re.split(r'(?<!\\)\|',line.strip())[1:-1]
            if all(re.fullmatch(r'\s*[:-]+\s*',c) for c in cells):continue
            tag='th' if thead else 'td';out.append('<tr>'+''.join('<'+tag+'>'+inline(c.strip().replace('\\|','|'))+'</'+tag+'>' for c in cells)+'</tr>');thead=False;continue
        if intable:out.append('</table></div>');intable=False
        if line.startswith('- '):
            flush()
            if not inlist:out.append('<ul>');inlist=True
            out.append('<li>'+inline(line[2:])+'</li>');continue
        if inlist:out.append('</ul>');inlist=False
        h=re.match(r'^(#{1,6})\s+(.*)',line)
        if h:flush();level=len(h[1]);out.append(f'<h{level}>'+inline(h[2])+f'</h{level}>');continue
        if not line.strip():flush()
        else:paragraph.append(line)
    flush()
    if intable:out.append('</table></div>')
    if inlist:out.append('</ul>')
    return '\n'.join(out)

def main():
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    classes=json.loads((ROOT/'inventory/classes.json').read_text(encoding='utf-8'))
    fields=json.loads((ROOT/'inventory/proto_fields.json').read_text(encoding='utf-8'))
    enums=json.loads((ROOT/'inventory/proto_enums.json').read_text(encoding='utf-8'))
    checks=json.loads((ROOT/'inventory/proto_schema_validation.json').read_text(encoding='utf-8'))
    verified={(x['source'],x['message'],x['name']):x['status']=='match' for x in checks}
    proto='# 附录：完整 Protobuf 字段与枚举\n\n日期：2026-11-12。字段直接取自 APK 内的 `ucar.proto`、`share.proto`；字段 tag 与编译类 `*_FIELD_NUMBER` 逐项核对。\n\n300 个 ucar.proto 字段与编译类匹配；42 个 share.proto 字段只有包内 schema 证据，没有对应的 ShareProto 编译类匹配。后者仍保留为定义，不能声明其当前通道已启用。\n\n`singular` 表示未显式 optional/repeated 的声明，不等于已经确认业务必填。消息字段编号不是封包头 serviceId。\n\n'
    fg=defaultdict(list);eg=defaultdict(list)
    for f in fields:fg[(f['source'],f['message'])].append(f)
    for e in enums:eg[(e['source'],e['enum'])].append(e)
    for source in ('ucar.proto','share.proto'):
        proto+=f'## {source}\n\n原始文件：[source/{source}](source/{source})。\n\n'
        declarations=re.findall(r'(?m)^message\s+(\w+)\s*\{',(ROOT/'source'/source).read_text(encoding='utf-8'))
        for message in declarations:
            proto+=f'### {message}\n\n';fs=fg.get((source,message),[])
            if not fs:proto+='空 message；不添加字段。\n\n';continue
            proto+=table(['tag','字段名','类型','声明','源码行','编译核对','包内注释'],[(f['number'],f['name'],f['type'],f['cardinality'],f['line'],'匹配' if verified[(source,message,f['name'])] else '仅包内 schema',f['comment']) for f in fs])
        proto+='### 枚举\n\n'
        for (src,name),es in eg.items():
            if src!=source:continue
            proto+=f'#### {name}\n\n'+table(['名称','十进制值','十六进制值','源码行','包内注释'],[(e['name'],e['value'],hex(e['value']),e['line'],e['comment']) for e in es])
    write('APPENDIX_PROTO.md',proto)
    binders=json.loads((ROOT/'inventory/binder_interfaces.json').read_text(encoding='utf-8'));tx=readcsv('binder_transactions.csv');txmap={(r['class'],r['method']):r['transaction'] for r in tx}
    core=[c for c in binders if c['class'].startswith(APP)];others=[c for c in binders if c not in core]
    binder='# 附录：完整 Binder 接口与方法\n\n日期：2026-11-12。总计 122 个接口、616 个方法。签名来自 DEX；参数名称多数未保留，按参数类型/顺序记录。事务编号来自 `$Stub.TRANSACTION_*` 常量；`—` 表示未恢复，不按方法排列推断。\n\nBinder 是 Android 本地跨进程接口。接口定义、exported 属性与权限需要结合；存在定义不代表普通第三方应用可绑定。\n\n'
    binder+=f'核心包前缀组：{len(core)} 个接口，{sum(len(c["methods"]) for c in core)} 个方法。包前缀归类只表示直接相关，不能证明全部方法运行时使用。\n\n'
    for group,title in ((core,'CarWith / CarLink / UCar / CarLife / EasyConn'),(others,'系统镜像与其它 SDK')):
        binder+=f'## {title}\n\n'
        for c in group:
            name=jtype(c['class']);binder+=f'### {name}\n\nDEX：`{c["dex"]}`。接口描述符：`{c["class"]}`。\n\n'
            binder+=table(['方法','完整 Java 签名','事务编号'],[(m['name'],signature(m['name'],m['type']),txmap.get((c['class'][:-1]+'$Stub;',m['name']),'')) for m in c['methods']]) if c['methods'] else '无方法定义。\n\n'
    write('APPENDIX_BINDER.md',binder)
    models=readcsv('business_model_fields.csv');serial=readcsv('serialized_fields.csv');assets=readcsv('asset_json_fields.csv')
    modeldoc='# 附录：业务模型、序列化名称与配置字段\n\n日期：2026-11-12。这里逐项列出重点业务实例字段、显式序列化名称和 APK JSON 配置路径。类字段属于定义证据；若未同时找到发送/消费代码，不能当作已输出接口。\n\n'
    modeldoc+='## 重点业务模型\n\n'
    mg=defaultdict(list)
    for r in models:mg[r['class']].append(r)
    for classname,rs in mg.items():modeldoc+=f'### {jtype(classname)}\n\n'+table(['DEX','成员原名','类型','注解'],[(r['dex'],r['field'],r['type'],r['annotations']) for r in rs])
    modeldoc+='## 明确 JSON 名称\n\n共 266 个字段。名称来自 `SerializedName`。另有 883 个无 JSON 名称的枚举字段标记，见机器清单，未纳入本表。\n\n'
    modeldoc+=table(['DEX','类','成员原名','JSON 名称','类型'],[(r['dex'],jtype(r['class']),r['field'],r['wire_name'],r['type']) for r in serial])
    modeldoc+='## APK 内 JSON 配置字段\n\n共 1,128 条去重路径。类型名为 Python 解析类型：str/string、int/integer、float/number、bool/boolean、NoneType/null、array。静态样例为同路径/类型的第一个值，不代表 API 返回值。\n\n'
    ag=defaultdict(list)
    for r in assets:ag[r['source']].append(r)
    for source,rs in ag.items():modeldoc+=f'### {source}\n\n'+table(['字段路径','类型','包内静态样例'],[(r['path'],r['type'],r['sample']) for r in rs])
    write('APPENDIX_MODELS.md',modeldoc)
    uris=readcsv('urls.csv');refs=readcsv('url_references.csv');refmap=defaultdict(list)
    for r in refs:
        for url in re.findall(r'(?:https?|wss?|content)://[^\s\x00<>"\x27]+',r['value']):refmap[url].append(r['dex']+':'+r['method']+'@0x'+r['code_offset'])
    udoc='# 附录：URL 与本地 URI 字面量\n\n日期：2026-11-12。来自所有 8 个 DEX 字符串表。不是可调用接口白名单；XML namespace、文档地址、错误提示、环境分支与页面资源保留并归类。候选 URL 可能来自大段文本，因此需参考原 context 和调用代码。\n\n'
    urows=[]
    for url in sorted(set(r['url'] for r in uris)):
        host=urlparse(url).netloc
        if url.startswith('content://'):category='本地 Content URI'
        elif any(x in host for x in ('w3.org','schemas.','xml.','apache.','github.com','slf4j.org','youtrack.','jmdns.','caltech.')):category='文档/namespace/错误说明'
        elif any(x in url.lower() for x in ('privacy','protocol.html','policy.html','supportedcarmodels.html','disclaimer','service_new.html','helpcenter','beian.')):category='页面或隐私相关资源/API；需看代码'
        elif url.startswith(('ws://','wss://')):category='WebSocket SDK 候选'
        else:category='HTTP(S) 地址候选'
        env='preview/staging/test 字面量' if re.search(r'preview|staging|p4t|preview4test',url,re.I) else '生产命名或未明确环境；非运行时选择结果'
        urows.append({'url':url,'category':category,'environment':env,'references':refmap[url]})
    udoc+=table(['URL / URI','分类','环境标记','代码出处（最多三条，完整见 CSV）'],[(r['url'],r['category'],r['environment'],'<br>'.join(r['references'][:3])) for r in urows]);write('APPENDIX_URLS.md',udoc)
    save('inventory/url_catalog.json',urows)
    descriptions={
        'all_dex_fields.csv':'全 8 个 DEX 的所有定义字段；含资源/SDK/Protobuf，非网络参数计数',
        'all_dex_methods.csv':'全 DEX 的所有定义方法；含类型、权限标志、偏移、方法及参数注解',
        'application_fields.csv':'指定应用/集成 SDK 包前缀字段；含大量生成代码',
        'application_interfaces.csv':'指定包前缀的全部 Java 接口方法；含 Protobuf OrBuilder 等',
        'business_model_fields.csv':'158 个重点业务模型实例成员',
        'serialized_fields.csv':'266 个明确 JSON 属性名称',
        'enum_annotation_markers.csv':'883 个无 JSON 名称的枚举字段标记',
        'sdk_ai_model_fields.csv':'10,828 个小爱 SDK 实例模型字段；未确认当前业务使用',
        'proto_fields.csv':'342 个包内 Protobuf 字段/tag/类型/源码行',
        'proto_enums.csv':'157 个包内 Protobuf 枚举值',
        'http_routes.csv':'4 个混淆 Retrofit 注解接口；另外三条代码构造路径见主报告',
        'binder_methods.csv':'122 个 Binder 接口中的 616 个方法',
        'binder_transactions.csv':'576 条 Stub 事务常量；可按类/方法联表',
        'wire_service_ids.csv':'23 条直接从封包构造代码恢复的消息/serviceId 映射',
        'control_constants.csv':'ControlChannel 静态常量',
        'key_usage.csv':'Intent/Bundle/JSONObject/Map/Preference/Cursor 的常量键使用和调用类型',
        'application_literals.csv':'已选择应用与入口类中的 const-string 原字面量/偏移',
        'action_literals.csv':'239 条 action/调用标识字面量，候选集',
        'urls.csv':'318 次 DEX 字符串表中的 URL/URI 候选出现',
        'url_references.csv':'297 条已选择类中的 URL/URI 引用指令，部分为 SDK/文档',
        'relative_path_candidates.csv':'291 个相对路径候选；含文件路径，未全部判为 API',
        'uuid_literals.csv':'123 条 UUID 字面量；未全部判为蓝牙业务 UUID',
        'asset_json_fields.csv':'1,128 条包内 JSON 配置路径/类型/首个静态样例',
        'components.csv':'115 个 Manifest 组件、导出状态、权限、authority 与 action',
        'javascript_interfaces.csv':'7 个 JavascriptInterface Java 方法',
        'native_methods.csv':'182 个 DEX native 方法定义与签名',
        'native_exports.csv':'21,265 条 ELF 动态符号表定义的全局/弱符号；含支持库符号',
        'apk_entries.csv':'4,969 条顶层 ZIP 文件条目/尺寸/CRC',
        'nested_archive_entries.csv':'321 条嵌套 ZIP/RPK 文件条目'}
    files=[]
    for p in sorted((ROOT/'inventory').glob('*.csv')):
        with p.open(encoding='utf-8-sig',newline='') as f:count=sum(1 for _ in csv.DictReader(f))
        files.append({'path':str(p.relative_to(ROOT)).replace('\\','/'),'rows':count,'bytes':p.stat().st_size,'sha256':sha(p.read_bytes()),'description':descriptions.get(p.name,'提取清单')})
    save('inventory/file_manifest.json',files)
    inv='# 完整机器清单与复现说明\n\n日期：2026-11-12。所有清单为离线静态结果。全量 DEX 表含依赖 SDK/资源类/生成代码，不应把这些行数当作业务 API 或线上参数数量。\n\n'
    inv+=table(['文件','数据行数','字节数','说明'],[(f'[{Path(r["path"]).name}]({r["path"]})',r['rows'],r['bytes'],r['description']) for r in files])
    inv+='## JSON、源码和验证证据\n\n'
    inv+='- `manifest.json`：APK SHA-256、各 DEX/原生库尺寸与哈希、覆盖统计。\n- `inventory/classes.json`：全部类定义、字段、方法、访问标志和注解；体积较大，可按 class 查询。\n- `inventory/assembly_verification.json`：33,418 类与重新生成的 dexdump 逐字节对比结果。\n- `inventory/proto_schema_validation.json`：每个包内 Protobuf 字段的编译 tag 核对结果。\n- `inventory/http_annotations.json`：4 个混淆后 HTTP 定义的原注解和参数注解。\n- `inventory/file_manifest.json`：每份 CSV 的行数、尺寸与 SHA-256。\n- `source/AndroidManifest.xml`：从二进制 AXML 解析的可读 Manifest。\n- `source/ucar.proto`、`source/share.proto`：包内 schema；仅规范换行，未修复原注释乱码。\n- `source/assets/`：包内可解析 JSON 的原始文件。\n- `source/dexdump/`：被报告引用的关键类原始反汇编。\n- `source/*.so.strings.txt`：原生库相关可打印字符串，不是完整函数反编译。\n\n'
    inv+='## 复现\n\n本机 Python 标准库与 Android SDK 36.0.0 即可完成；没有下载安装依赖。运行位置为仓库根目录。\n\n'
    inv+='```powershell\npython -X utf8 research/protocol/carwith_4_0_23/tools/extract.py "C:\\Users\\admin\\Desktop\\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk\npython -X utf8 research/protocol/carwith_4_0_23/tools/verify_assembly.py "C:\\Users\\admin\\Desktop\\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk\npython -X utf8 research/protocol/carwith_4_0_23/tools/enrich.py "C:\\Users\\admin\\Desktop\\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk\npython -X utf8 research/protocol/carwith_4_0_23/tools/supplement.py "C:\\Users\\admin\\Desktop\\CarWith_4.0.23-20261016.apk" --cache local-backups/carwith-navigation-apk\npython -X utf8 research/protocol/carwith_4_0_23/tools/build_report.py\n```\n\n'
    inv+='缓存使用现有的 `local-backups/carwith-navigation-apk/classes*/all-classes.zip` 与 `references.jsonl`。先核对 APK DEX 哈希，再逐类核验缓存反汇编。缓存未随文档包重复拷贝；主报告涉及的类已保存到 source/dexdump。`extract.py` 不带 cache 也能提取基本定义、Manifest、原生字符串与资源；跨引用与补充工具需要已核验缓存。\n\n'
    inv+='`tools` 的 SDK 路径可根据本机修改。输出都写在本分析目录，不改 APK。复现工具与文档的所有计数均来自实际清单，不声明网络可用性。\n'
    write('INVENTORY.md',inv)
    countrows=[('类定义',manifest['counts']['classes']),('全量字段定义',manifest['counts']['fields']),('全量方法定义',manifest['counts']['methods']),('Binder 接口/方法','122 / 616'),('明确 JSON 名称',len(serial)),('Protobuf 字段/枚举值','342 / 157'),('实际编译 Protobuf tag 匹配',300),('静态键使用/不同键','2185 / 1137'),('JSON 配置路径',len(assets)),('native 方法',182)]
    maintext=(ROOT/'REPORT.md').read_text(encoding='utf-8')
    # Insert generated counts once without modifying hand-maintained interpretation.
    summary=table(['静态提取项目','数量'],countrows)
    maintext=maintext.replace('统计以所有 DEX 中的实际类定义、字段定义和方法定义为准，',summary+'统计以所有 DEX 中的实际类定义、字段定义和方法定义为准，') if '| 静态提取项目 |' not in maintext else maintext
    write('REPORT.md',maintext)
    dataset={
        'Protobuf 字段':([{**r,'compiled_status':'matched' if verified[(r['source'],r['message'],r['name'])] else 'embedded schema only'} for r in fields],['source','message','number','name','type','cardinality','compiled_status','line']),
        'Protobuf 枚举':(enums,['source','enum','name','value','line']),
        'Binder 方法':(readcsv('binder_methods.csv'),['dex','class','name','signature']),
        'JSON 序列化名称':(serial,['dex','class','field','wire_name','type']),
        '业务模型':(models,['dex','class','field','type']),
        '配置 JSON 路径':(assets,['source','path','type','sample']),
        '键使用':(readcsv('key_usage.csv'),['dex','class','method','key','category','operation','target','instruction_offset']),
        'HTTP 注解接口':(readcsv('http_routes.csv'),['dex','class','method','http_method','path','signature','parameters']),
        '封包服务编号':(readcsv('wire_service_ids.csv'),['dex','method','message','service_id','category','code_offset']),
        'URL/URI 候选':(urows,['url','category','environment','references']),
        'JNI 方法':(readcsv('native_methods.csv'),['dex','class','method','signature'])}
    data=json.dumps({k:{'rows':v[0],'columns':v[1]} for k,v in dataset.items()},ensure_ascii=True).replace('</','<\\/')
    css='''body{margin:0;background:#f3f6fa;color:#203044;font:16px/1.75 "Microsoft YaHei","Noto Sans SC",sans-serif}header{background:#17334a;color:white;padding:30px max(24px,calc((100vw - 1140px)/2))}header h1{margin:0;font-size:28px}header p{color:#cce0ef}nav{display:flex;flex-wrap:wrap;gap:9px;margin-top:18px}nav a{color:white;text-decoration:none;background:#294d68;padding:7px 15px;border-radius:6px}main{max-width:1140px;margin:24px auto;padding:0 22px}.panel{background:white;padding:25px;border-radius:10px;box-shadow:0 2px 14px #17334a0b;margin-bottom:24px}h1{font-size:28px}h2{font-size:23px;border-bottom:2px solid #e3ebf3;padding-bottom:8px;margin-top:34px}h3{font-size:19px;margin-top:27px}a{color:#126b9e}code{font:13px/1.7 Consolas,monospace;background:#eef3f8;padding:2px 4px;overflow-wrap:anywhere}pre{overflow:auto;background:#eef3f8;padding:18px}pre code{white-space:pre}table{width:100%;border-collapse:collapse;font-size:13px;line-height:1.6}th,td{text-align:left;vertical-align:top;border:1px solid #dce5ed;padding:8px 10px;overflow-wrap:anywhere;min-width:60px}th{background:#eaf1f7}tr:nth-child(even){background:#f8fafc}.table-wrap{overflow:auto;margin:16px 0}input,select,button{font:inherit;border:1px solid #c2d1de;border-radius:6px;padding:9px 12px}input{flex:1;min-width:180px}.controls{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}button{background:#17334a;color:white;cursor:pointer}#count{color:#52697a;font-size:14px}.catalog td{max-width:420px}.hint{background:#eef5fa;padding:12px 16px;border-left:4px solid #126b9e}.appendix{margin-top:25px}footer{text-align:center;font-size:13px;color:#6f8190;padding:24px}@media(max-width:700px){main{padding:0 10px}.panel{padding:16px}header{padding:22px 18px}header h1{font-size:23px}th,td{min-width:90px}}@media print{header,nav,.controls,button,#catalogPanel{display:none}.panel{box-shadow:none;padding:0}body{background:white;font-size:11px}h2,h3{break-after:avoid}table{font-size:10px}tr{break-inside:avoid}main{max-width:none}}'''
    js='''const DATA=JSON.parse(document.getElementById('data').textContent);const select=document.getElementById('kind');for(const name of Object.keys(DATA)){const o=document.createElement('option');o.textContent=name;select.append(o)}let page=0;const size=100;let filtered=[];function render(){const item=DATA[select.value];const q=document.getElementById('query').value.toLowerCase().trim();filtered=item.rows.filter(row=>!q||JSON.stringify(row).toLowerCase().includes(q));const pages=Math.max(1,Math.ceil(filtered.length/size));page=Math.min(page,pages-1);document.getElementById('count').textContent=`共 ${item.rows.length} 条，匹配 ${filtered.length} 条，第 ${page+1} / ${pages} 页`;const table=document.getElementById('results');table.replaceChildren();const head=document.createElement('tr');for(const key of item.columns){const th=document.createElement('th');th.textContent=key;head.append(th)}table.append(head);for(const row of filtered.slice(page*size,(page+1)*size)){const tr=document.createElement('tr');for(const key of item.columns){const td=document.createElement('td');const v=row[key];td.textContent=v==null?'—':typeof v==='object'?JSON.stringify(v):String(v);tr.append(td)}table.append(tr)}document.getElementById('prev').disabled=page===0;document.getElementById('next').disabled=page>=pages-1}select.onchange=()=>{page=0;render()};document.getElementById('query').oninput=()=>{page=0;render()};document.getElementById('prev').onclick=()=>{page--;render()};document.getElementById('next').onclick=()=>{page++;render()};document.getElementById('download').onclick=()=>{const blob=new Blob([JSON.stringify(filtered,null,2)],{type:'application/json;charset=utf-8'});const u=URL.createObjectURL(blob);const a=document.createElement('a');a.href=u;a.download=select.value+'-筛选结果.json';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)};render();'''
    htmltext='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CarWith 4.0.23 字段与接口分析</title><style>'+css+'</style></head><body><header><h1>CarWith 4.0.23 字段与接口分析</h1><p>2026-11-12 · 离线静态分析 · 所有 8 个 DEX · 原始 APK 未修改</p><nav><a href="#report">分析报告</a><a href="#catalogPanel">搜索字段/接口</a><a href="#proto">完整 Protobuf</a><a href="#binder">完整 Binder</a><a href="INVENTORY.md">机器清单目录</a></nav></header><main><section class="panel" id="report">'+markdown(maintext)+'</section><section class="panel" id="catalogPanel"><h2>可搜索字段与接口</h2><p class="hint">数据全部内嵌在此文件，无需联网。候选、SDK 定义和已确认代码出处保留各自状态；筛选结果支持导出 JSON。完整 DEX 字段/方法及 ELF 符号因体积较大，使用配套 CSV。</p><div class="controls"><select id="kind" aria-label="清单类型"></select><input id="query" aria-label="搜索关键字" placeholder="搜索字段、类名、接口、消息名或 URL"><button id="download">导出筛选 JSON</button></div><p id="count"></p><div class="table-wrap"><table class="catalog" id="results"></table></div><div class="controls"><button id="prev">上一页</button><button id="next">下一页</button></div></section><section class="panel appendix" id="proto">'+markdown(proto)+'</section><section class="panel appendix" id="binder">'+markdown(binder)+'</section></main><footer>输入 APK SHA-256：'+manifest['apk_sha256']+'</footer><script type="application/json" id="data">'+data+'</script><script>'+js+'</script></body></html>'
    write('CarWith字段与接口分析.html',htmltext)
    write('README.md','# CarWith 4.0.23 字段与接口分析\n\n分析输入：`CarWith_4.0.23-20261016.apk`，日期 2026-11-12。\n\n[打开 HTML 阅读版与搜索表](CarWith字段与接口分析.html) · [主报告 Markdown](REPORT.md) · [完整机器清单](INVENTORY.md)\n\n'+summary+'\n[Protobuf 附录](APPENDIX_PROTO.md) · [Binder 附录](APPENDIX_BINDER.md) · [模型/配置附录](APPENDIX_MODELS.md) · [URL 附录](APPENDIX_URLS.md)\n\n本目录包含文档、CSV/JSON 清单、关键原始反汇编和可复现工具。所有结果为静态分析，未测试远端接口。\n')
    print(json.dumps({'report_bytes':len(maintext.encode('utf-8')),'html_bytes':len(htmltext.encode('utf-8')),'csv_files':len(files),'searchable_rows':sum(len(v[0]) for v in dataset.values()),'core_binder_interfaces':len(core),'core_binder_methods':sum(len(c['methods']) for c in core)}))

if __name__=='__main__':main()
