import sqlite3
from pathlib import Path
import gzip
import shutil
import tempfile
import streamlit as st

from components.curated_overlay import apply_deep_payload

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / 'data' / 'processed'
GZ_DB = PROCESSED / 'vic_dashboard.db.gz'
PARTS = sorted(PROCESSED.glob('vic_dashboard.db.gz.part*'))
TMP_ROOT = Path('/tmp/vic_falsification_lab_v6_1')
TMP_GZ = TMP_ROOT / 'vic_dashboard.db.gz'
TMP_DB = TMP_ROOT / 'vic_dashboard.db'

REQUIRED = {
    'ideas_master','analysis','pattern_catalog','pattern_stats','idea_pattern_map',
    'postmortems','verified_pattern_catalog','verified_pattern_map',
    'deep_analysis_meta','deep_analysis_claims','deep_analysis_sections',
    'deep_analysis_metrics','deep_analysis_timeline','deep_analysis_sources'
}

def _schema_tables(path: Path):
    try:
        with sqlite3.connect(path) as c:
            return {r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    except sqlite3.Error:
        return set()

def _schema_ok(path: Path) -> bool:
    if not path.exists() or not path.stat().st_size:
        return False
    return REQUIRED.issubset(_schema_tables(path))

def _assemble_gz() -> Path:
    """V6 분할 DB를 최우선 사용한다.

    과거 버전의 vic_dashboard.db.gz가 repo에 남아 있어도 무시한다.
    """
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    if PARTS:
        with open(TMP_GZ, 'wb') as w:
            for p in PARTS:
                with open(p, 'rb') as r:
                    shutil.copyfileobj(r, w)
        return TMP_GZ
    if GZ_DB.exists():
        return GZ_DB
    raise FileNotFoundError('대시보드 DB 또는 분할 DB 조각을 찾지 못했습니다.')

def _unpack() -> Path:
    gz = _assemble_gz()
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=TMP_ROOT, delete=False) as tmp:
        temp = Path(tmp.name)
        try:
            with gzip.open(gz, 'rb') as src:
                shutil.copyfileobj(src, tmp)
        except Exception:
            temp.unlink(missing_ok=True)
            raise
    temp.replace(TMP_DB)
    if not _schema_ok(TMP_DB):
        tables = sorted(_schema_tables(TMP_DB))
        missing = sorted(REQUIRED - set(tables))
        raise sqlite3.DatabaseError(
            'V6 DB 스키마 불일치. 누락 테이블: ' + ', '.join(missing)
        )
    # Human-reviewable research batches are overlaid after the large base DB is
    # unpacked. This keeps each research commit small, auditable and reversible.
    for payload in sorted((ROOT / 'data' / 'curated').glob('*_deep_v7.json')):
        apply_deep_payload(TMP_DB, payload)
    return TMP_DB

@st.cache_resource
def conn():
    return sqlite3.connect(_unpack(), check_same_thread=False)

def rows(sql, params=()):
    cur = conn().execute(sql, params)
    cols = [x[0] for x in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]

def row(sql, params=()):
    cur = conn().execute(sql, params)
    r = cur.fetchone()
    return None if r is None else dict(zip([x[0] for x in cur.description], r))
