#!/usr/bin/env python3
import csv,gzip,json,subprocess
from pathlib import Path
from collections import defaultdict, Counter
ROOT=Path(__file__).resolve().parents[1]
OLD='4add72b903e1d656f4664a2a256718640edd5b8b'
tmp=Path('/tmp/ideas_master.csv.gz')
with tmp.open('wb') as f:
    subprocess.run(['git','show',f'{OLD}:data/processed/ideas_master.csv.gz'],cwd=ROOT,check=True,stdout=f)
reviewed=set()
for p in (ROOT/'data/curated').glob('*_deep_v7.json'):
    try:
        j=json.loads(p.read_text(encoding='utf-8'))
        for x in j.get('ideas_master',[]): reviewed.add(str(x.get('idea_id') or ''))
        for x in j.get('postmortems',[]): reviewed.add(str(x.get('idea_id') or ''))
    except Exception:
        pass
rows=[]
with gzip.open(tmp,'rt',encoding='utf-8-sig',errors='replace',newline='') as f:
    rows=list(csv.DictReader(f))
groups=defaultdict(list)
for r in rows:
    iid=str(r.get('idea_id') or '')
    if not iid or iid in reviewed: continue
    ticker=(r.get('ticker') or '').strip().upper()
    company=(r.get('company_name') or '').strip()
    key=(ticker,company)
    groups[key].append(r)
rank=[]
for (ticker,company),rs in groups.items():
    dates=sorted(str(x.get('date') or '')[:10] for x in rs)
    rank.append({
        'ticker':ticker,'company_name':company,'count':len(rs),
        'first_date':dates[0] if dates else None,'last_date':dates[-1] if dates else None,
        'idea_ids':[x.get('idea_id') for x in sorted(rs,key=lambda x:str(x.get('date') or ''))],
        'authors':[x.get('author') for x in sorted(rs,key=lambda x:str(x.get('date') or ''))]
    })
rank.sort(key=lambda x:(-x['count'],x['ticker'],x['company_name']))
out=ROOT/'.vic_tmp'/'next_unreviewed_rank.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'reviewed_ids':len(reviewed),'raw_rows':len(rows),'unreviewed_rows':sum(x['count'] for x in rank),'top':rank[:120]},ensure_ascii=False,indent=2),encoding='utf-8')
print('reviewed',len(reviewed),'raw',len(rows),'unreviewed',sum(x['count'] for x in rank))
print([(x['ticker'],x['company_name'],x['count']) for x in rank[:30]])
