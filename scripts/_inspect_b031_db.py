#!/usr/bin/env python3
import json, sqlite3, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FULL="4add72b903e1d656f4664a2a256718640edd5b8b"
subprocess.run(["git","fetch","origin",FULL,"--depth=1"],cwd=ROOT,check=True)
db=Path("/tmp/vic_dashboard.db")
with db.open("wb") as f:
    subprocess.run(["git","show",f"{FULL}:data/processed/vic_dashboard.db"],cwd=ROOT,check=True,stdout=f)
targets=["RCII","WRLD"]
with sqlite3.connect(db) as c:
    tables=[r[0] for r in c.execute("select name from sqlite_master where type='table' order by name")]
    schemas={t:[r[1] for r in c.execute(f"pragma table_info({t})")] for t in tables}
    out={"tables":tables,"schemas":schemas,"rows":{}}
    for t in tables:
        cols=schemas[t]
        if "ticker" in cols or "idea_id" in cols:
            try:
                if "ticker" in cols:
                    rs=c.execute(f"select * from {t} where upper(ticker) in ('RCII','WRLD')").fetchall()
                elif "idea_id" in cols:
                    ids=[r[0] for r in c.execute("select idea_id from ideas_master where upper(ticker) in ('RCII','WRLD')")]
                    if not ids: continue
                    q=",".join("?" for _ in ids)
                    rs=c.execute(f"select * from {t} where idea_id in ({q})",ids).fetchall()
                else: continue
                if rs:
                    out["rows"][t]=[dict(zip(cols,r)) for r in rs]
            except Exception as e:
                out["rows"][t]={"error":str(e)}
p=ROOT/".vic_tmp"/"b031_old_db.json"
p.write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
print("tables",len(tables),"dumped",list(out["rows"]))
