import sqlite3
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / 'data' / 'processed' / 'vic_dashboard.db'

@st.cache_resource
def conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def rows(sql, params=()):
    cur = conn().execute(sql, params)
    cols = [x[0] for x in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]

def row(sql, params=()):
    cur = conn().execute(sql, params)
    r = cur.fetchone()
    return None if r is None else dict(zip([x[0] for x in cur.description], r))
