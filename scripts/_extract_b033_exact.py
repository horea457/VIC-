#!/usr/bin/env python3
import csv,gzip,json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
tmp=Path('/tmp/ideas_master.csv.gz')
with tmp.open('wb') as f:
    subprocess.run(['git','show','4add72b9:data/processed/ideas_master.csv.gz'],cwd=root,check=True,stdout=f)
rows=[]
with gzip.open(tmp,'rt',encoding='utf-8-sig',errors='replace',newline='') as f:
    for row in csv.DictReader(f):
        if str(row.get('ticker') or '').strip().upper() in ('PICO','GRA'):
            rows.append(row)
out=root/'.vic_tmp'/'b033_exact.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'count':len(rows),'rows':rows},ensure_ascii=False,indent=2),encoding='utf-8')
print(len(rows))
