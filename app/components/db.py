import sqlite3
from pathlib import Path
import gzip
import shutil
import tempfile
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / 'data' / 'processed'
GZ_DB = PROCESSED / 'vic_dashboard.db.gz'
PARTS = sorted(PROCESSED.glob('vic_dashboard.db.gz.part*'))
TMP_ROOT = Path('/tmp/vic_falsification_lab_v6')
TMP_GZ = TMP_ROOT / 'vic_dashboard.db.gz'
TMP_DB = TMP_ROOT / 'vic_dashboard.db'

REQUIRED = {
    'ideas_master','analysis','pattern_catalog','pattern_stats','idea_pattern_map',
    'postmortems','verified_pattern_catalog','verified_pattern_map',
    'deep_analysis_meta','deep_analysis_claims','deep_analysis_sections',
    'deep_analysis_metrics','deep_analysis_timeline','deep_analysis_sources'
}

def _schema_ok(path: Path) -> bool:
    if not path.exists() or not path.stat().st_size:
        return False
    try:
        with sqlite3.connect(path) as c:
            tables={r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        return REQUIRED.issubset(tables)
    except sqlite3.Error:
        return False

def _assemble_gz() -> Path:
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    if GZ_DB.exists():
        return GZ_DB
    if not PARTS:
        raise FileNotFoundError('대시보드 DB 조각 파일을 찾지 못했습니다.')
    with open(TMP_GZ,'wb') as w:
        for p in PARTS:
            with open(p,'rb') as r:
                shutil.copyfileobj(r,w)
    return TMP_GZ

def _unpack() -> Path:
    gz=_assemble_gz()
    TMP_ROOT.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=TMP_ROOT,delete=False) as tmp:
        temp=Path(tmp.name)
        with gzip.open(gz,'rb') as src:
            shutil.copyfileobj(src,tmp)
    temp.replace(TMP_DB)
    if not _schema_ok(TMP_DB):
        raise sqlite3.DatabaseError('압축 해제한 DB 스키마가 현재 앱과 맞지 않습니다.')
    return TMP_DB

@st.cache_resource
def conn():
    return sqlite3.connect(_unpack(),check_same_thread=False)

def rows(sql,params=()):
    cur=conn().execute(sql,params)
    cols=[x[0] for x in cur.description]
    return [dict(zip(cols,r)) for r in cur.fetchall()]

def row(sql,params=()):
    cur=conn().execute(sql,params)
    r=cur.fetchone()
    return None if r is None else dict(zip([x[0] for x in cur.description],r))
