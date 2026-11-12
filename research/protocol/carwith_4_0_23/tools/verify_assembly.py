"""Verify every cached class against a fresh Android SDK dexdump of APK DEX bytes."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile
from extract import ROOT, SDK, save, sha

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('apk',type=Path);ap.add_argument('--cache',type=Path,required=True);args=ap.parse_args()
    with zipfile.ZipFile(args.apk) as apk:
        dexes=[name for name in apk.namelist() if re.fullmatch(r'classes\d*\.dex',name)]
        for name in dexes: assert sha(apk.read(name))==sha((args.cache/name).read_bytes())
    def check(name):
        count=0; block=[]; checksum=hashlib.sha256()
        with zipfile.ZipFile(args.cache/Path(name).stem/'all-classes.zip') as archive:
            proc=subprocess.Popen([str(SDK/'dexdump.exe'),'-d','-n',str(args.cache/name)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',errors='replace')
            def flush():
                nonlocal count
                text=''.join(block);m=re.search(r"Class descriptor\s*: '([^']+)'",text)
                if not m:return
                fn=m[1][1:-1].replace('/','.')+'.txt';b=text.encode('utf-8')
                assert archive.read(fn)==b, f'{name}: assembly mismatch: {fn}'
                checksum.update(b);count+=1
            for line in proc.stdout:
                if re.match(r'^Class #\d+',line):flush();block=[]
                block.append(line)
            flush();error=proc.stderr.read();code=proc.wait();assert code==0,(name,code,error)
            assert count==len(archive.namelist()),(name,count,len(archive.namelist()))
        result={'dex':name,'classes_verified':count,'assembly_stream_sha256':checksum.hexdigest(),'comparison':'byte-for-byte equal','tool':'Android SDK 36.0.0 dexdump -d -n'}
        print(json.dumps(result),flush=True);return result
    with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(check,dexes))
    save('inventory/assembly_verification.json',{'apk_sha256':sha(args.apk.read_bytes()),'results':results,'classes_verified':sum(x['classes_verified'] for x in results)})

if __name__=='__main__':main()
