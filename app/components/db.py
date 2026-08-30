import sqlite3
from pathlib import Path
import gzip
import shutil
import tempfile
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / 'data' / 'processed'
RAW_DB = PROCESSED / 'vic_dashboard.db'
GZ_DB = PROCESSED / 'vic_dashboard.db.gz'
TMP_DB = Path('/tmp/vic_falsification_lab/vic_dashboard.db')


def _has_required_schema(path: Path) -> bool:
    """현재 앱이 요구하는 V4 핵심 테이블이 있는지 확인."""
    if not path.exists() or path.stat().st_size == 0:
        return False
    try:
        with sqlite3.connect(path) as c:
            tables = {
                r[0]
                for r in c.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                ).fetchall()
            }
        return {'pattern_catalog', 'pattern_stats', 'idea_auto_profile', 'postmortems', 'postmortem_claims'}.issubset(tables)
    except sqlite3.Error:
        return False


def _unpack_gz() -> Path:
    """GitHub/Streamlit 배포용 gzip DB를 /tmp에 원자적으로 해제."""
    if not GZ_DB.exists():
        raise FileNotFoundError('vic_dashboard.db.gz가 없습니다.')

    TMP_DB.parent.mkdir(parents=True, exist_ok=True)
    # 프로세스 시작 시 최신 배포 DB를 사용하도록 항상 새로 해제한다.
    with tempfile.NamedTemporaryFile(dir=TMP_DB.parent, delete=False) as tmp:
        tmp_path = Path(tmp.name)
        with gzip.open(GZ_DB, 'rb') as src:
            shutil.copyfileobj(src, tmp)
    tmp_path.replace(TMP_DB)

    if not _has_required_schema(TMP_DB):
        raise sqlite3.DatabaseError('압축 해제한 DB가 V4 필수 스키마를 포함하지 않습니다.')
    return TMP_DB


def resolved_db_path() -> Path:
    # 배포본에 gzip DB가 있으면 그것을 최우선 사용한다.
    # 이렇게 하면 이전 버전의 vic_dashboard.db가 저장소에 남아 있어도 오염되지 않는다.
    if GZ_DB.exists():
        return _unpack_gz()
    if _has_required_schema(RAW_DB):
        return RAW_DB
    raise FileNotFoundError('사용 가능한 V4 vic_dashboard.db(.gz)가 없습니다.')


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
