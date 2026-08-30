"""VIC_IDEAS.sql(PostgreSQL COPY dump)을 로컬 SQLite 원문 DB로 변환합니다."""
import argparse, re, sqlite3
from pathlib import Path

ESC={'b':'\b','f':'\f','n':'\n','r':'\r','t':'\t','v':'\v','\\':'\\'}
def unescape(s):
    if s == r'\N': return None
    out=[]; i=0
    while i < len(s):
        if s[i] != '\\' or i+1 >= len(s):
            out.append(s[i]); i+=1; continue
        i+=1; c=s[i]
        if c in ESC:
            out.append(ESC[c]); i+=1
        elif c in '01234567':
            o=c; j=i+1
            while j<len(s) and len(o)<3 and s[j] in '01234567': o+=s[j]; j+=1
            out.append(chr(int(o,8))); i=j
        else:
            out.append(c); i+=1
    return ''.join(out)
def as_bool(s):
    x=unescape(s); return 1 if x=='t' else 0 if x=='f' else None
def as_float(s):
    x=unescape(s)
    try: return float(x) if x is not None else None
    except: return None

def main(src,dst):
    dst=Path(dst); dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists(): dst.unlink()
    con=sqlite3.connect(dst); con.execute('PRAGMA synchronous=OFF'); con.execute('PRAGMA journal_mode=OFF')
    con.executescript('''
    CREATE TABLE catalyst(idea_id TEXT PRIMARY KEY,catalysts TEXT);
    CREATE TABLE companies(ticker TEXT PRIMARY KEY,company_name TEXT);
    CREATE TABLE descriptions(idea_id TEXT PRIMARY KEY,description TEXT);
    CREATE TABLE ideas(id TEXT PRIMARY KEY,link TEXT,company_id TEXT,user_id TEXT,date TEXT,is_short INTEGER,is_contest_winner INTEGER);
    CREATE TABLE performance(idea_id TEXT PRIMARY KEY,nextDayOpen REAL,nextDayClose REAL,oneWeekClosePerf REAL,twoWeekClosePerf REAL,oneMonthPerf REAL,threeMonthPerf REAL,sixMonthPerf REAL,oneYearPerf REAL,twoYearPerf REAL,threeYearPerf REAL,fiveYearPerf REAL);
    CREATE TABLE users(user_link TEXT PRIMARY KEY,username TEXT);
    ''')
    specs={
      'catalyst':('INSERT OR REPLACE INTO catalyst VALUES (?,?)',lambda x:(x[0],unescape(x[1]))),
      'companies':('INSERT OR REPLACE INTO companies VALUES (?,?)',lambda x:(x[0],unescape(x[1]))),
      'descriptions':('INSERT OR REPLACE INTO descriptions VALUES (?,?)',lambda x:(x[0],unescape(x[1]))),
      'ideas':('INSERT OR REPLACE INTO ideas VALUES (?,?,?,?,?,?,?)',lambda x:(x[0],unescape(x[1]),unescape(x[2]),unescape(x[3]),unescape(x[4]),as_bool(x[5]),as_bool(x[6]))),
      'performance':('INSERT OR REPLACE INTO performance VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',lambda x:tuple([x[0]]+[as_float(v) for v in x[1:]])),
      'users':('INSERT OR REPLACE INTO users VALUES (?,?)',lambda x:(x[0],unescape(x[1]))),
    }
    current=None; batch=[]
    with open(src,encoding='utf-8',errors='replace') as fh:
        for line in fh:
            if current is None:
                m=re.match(r'^COPY public\.(\w+) \(',line)
                if m and m.group(1) in specs: current=m.group(1)
                continue
            if line.rstrip('\r\n') == r'\.':
                if batch: con.executemany(specs[current][0],batch); con.commit(); batch=[]
                current=None; continue
            batch.append(specs[current][1](line.rstrip('\r\n').split('\t')))
            if len(batch)>=1000:
                con.executemany(specs[current][0],batch); con.commit(); batch=[]
    con.close()
    print(f'생성 완료: {dst}')
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('src'); p.add_argument('--dst',default='data/raw/vic_full_local.db'); a=p.parse_args(); main(a.src,a.dst)
