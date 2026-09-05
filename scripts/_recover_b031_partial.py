#!/usr/bin/env python3
import base64, subprocess, zlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FULL="da03e7080cc916ce435ad87541bcd1944982e840"
subprocess.run(["git","fetch","origin",FULL,"--depth=1"],cwd=ROOT,check=True)
parts=[]
for name in (".vic_tmp/b031_00.b64",".vic_tmp/b031_01.b64"):
    parts.append(subprocess.check_output(["git","show",f"{FULL}:{name}"],cwd=ROOT))
raw=base64.b64decode(b"".join(parts))
d=zlib.decompressobj(16+zlib.MAX_WBITS)
tar=d.decompress(raw)
off=0
found=None
while off+512 <= len(tar):
    hdr=tar[off:off+512]
    name=hdr[:100].split(b"\0",1)[0].decode("utf-8","replace")
    if not name: break
    try: size=int(hdr[124:136].split(b"\0",1)[0].strip() or b"0",8)
    except: break
    data=tar[off+512:off+512+min(size,max(0,len(tar)-off-512))]
    if name.endswith("batch_031_rcii_wrld_10.md"):
        found=data
        break
    off += 512 + ((size+511)//512)*512
if found is None:
    raise SystemExit("markdown entry not found")
p=ROOT/".vic_tmp"/"b031_partial.md"
p.write_bytes(found)
print("recovered",len(found),"bytes")
