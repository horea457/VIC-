import sqlite3
from pathlib import Path
import gzip, shutil, os
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / 'data' / 'processed'
RAW_DB = PROCESSED / 'vic_dashboard.db'
GZ_DB = PROCESSED / 'vic_dashboard.db.gz'
TMP_DB = Path('/tmp/vic_falsification_lab/vic_dashboard.db')

def resolved_db_path():
    # 로컬 개발에서는 원본 DB 우선. GitHub/Streamlit 배포본은 gzip DB를 자동 해제.
    if RAW_DB.exists():
        return RAW_DB
    if not GZ_DB.exists():
        raise FileNotFoundError('vic_dashboard.db 또는 vic_dashboard.db.gz가 없습니다.')
    TMP_DB.parent.mkdir(parents=True, exist_ok=True)
    if (not TMP_DB.exists()) or TMP_DB.stat().st_size == 0 or TMP_DB.stat().st_mtime < GZ_DB.stat().st_mtime:
        with gzip.open(GZ_DB, 'rb') as src, open(TMP_DB, 'wb') as dst:
            shutil.copyfileobj(src, dst)
    return TMP_DB

@st.cache_resource
def conn():
    return sqlite3.connect(resolved_db_path(), check_same_thread=False)

def rows(sql, params=()):
    cur = conn().execute(sql, params)
    cols = [x[0] for x in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]

def row(sql, params=()):
    cur = conn().execute(sql, params)
    r = cur.fetchone()
    return None if r is None else dict(zip([x[0] for x in cur.description], r))
