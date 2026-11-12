"""Package all locally extracted documents and evidence without the original APK."""
from pathlib import Path
import zipfile
from extract import ROOT, sha

def main():
    out=ROOT/'CarWith_4.0.23_字段接口与证据.zip'
    files=[p for p in ROOT.rglob('*') if p.is_file() and p!=out and '__pycache__' not in p.parts and p.suffix!='.pyc']
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(files):z.write(p,str(p.relative_to(ROOT)).replace('\\','/'))
    with zipfile.ZipFile(out) as z:assert z.testzip() is None;assert len(z.infolist())==len(files)
    print({'path':str(out),'files':len(files),'bytes':out.stat().st_size,'sha256':sha(out.read_bytes())})

if __name__=='__main__':main()
