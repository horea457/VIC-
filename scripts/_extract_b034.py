#!/usr/bin/env python3
import csv,gzip,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OLD='4add72b903e1d656f4664a2a256718640edd5b8b'
ids=[
'25bcc787-c584-4abe-8e41-23fd8ee83478',
'a87067b2-9f8f-4173-9a61-d8f39fc254c6',
'3ba1503d-ef82-4cee-ab2e-58ae5520533a',
'ced6ca2f-6dfd-4468-8884-22b4847ff276',
'70110b71-5ac1-4d66-8ad3-e51d19ce327a',
'201c288b-ea74-4e34-ba1e-da027699c778',
'42d64c6e-9e1c-4af5-880e-3b0df6054946',
'4c79f62c-fa91-488e-8da0-4b4fd51b8456',
'a1e08992-29d4-4dd1-8806-22e15fee1823',
'0a597f9f-d3a8-4a72-9834-c76fb457e159']
tmp=Path('/tmp/ideas_master.csv.gz')
with tmp.open('wb') as f:
    subprocess.run(['git','show',f'{OLD}:data/processed/ideas_master.csv.gz'],cwd=ROOT,check=True,stdout=f)
found={}
with gzip.open(tmp,'rt',encoding='utf-8-sig',errors='replace',newline='') as f:
    for row in csv.DictReader(f):
        iid=str(row.get('idea_id') or '')
        if iid in ids: found[iid]=row
rows=[found[i] for i in ids if i in found]
out=ROOT/'.vic_tmp'/'b034_source.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'count':len(rows),'rows':rows},ensure_ascii=False,indent=2),encoding='utf-8')
print('matched',len(rows))
for r in rows:
    print(r.get('date'),r.get('ticker'),r.get('company_name'),r.get('author'),r.get('direction_ko'),r.get('is_short'),r.get('source_link'))
