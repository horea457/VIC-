import json
import streamlit as st
from components.ui import apply_css, page_header, idea_quick_view
from components.db import rows

st.set_page_config(page_title='아이디어 탐색', layout='wide')
apply_css()
page_header('IDEA EXPLORER', '아이디어 탐색', '13,656개의 VIC 아이디어를 탐색하고, 행을 클릭하면 기업 설명·당시 논지·성공/실패 분석을 바로 확인합니다.')
q = st.text_input('검색', placeholder='회사 / 티커 / 작성자')
yrs = [x['year'] for x in rows('SELECT DISTINCT year FROM ideas_master WHERE year IS NOT NULL ORDER BY year')]
a,b,c,d = st.columns([2,1,1,1])
with a: yr = st.select_slider('연도', yrs, value=(min(yrs), max(yrs)))
with b: di = st.selectbox('방향', ['전체','롱','숏'])
with c: typ = st.selectbox('유형', ['전체'] + [x['idea_type_ko'] for x in rows('SELECT DISTINCT idea_type_ko FROM ideas_master ORDER BY idea_type_ko')])
with d: win = st.checkbox('Contest Winner')
sql = 'SELECT * FROM ideas_master WHERE year BETWEEN ? AND ?'; p = [yr[0],yr[1]]
if q:
    sql += ' AND (ticker LIKE ? OR company_name LIKE ? OR author LIKE ?)'; p += [f'%{q}%']*3
if di != '전체':
    sql += ' AND direction_ko=?'; p.append(di)
if typ != '전체':
    sql += ' AND idea_type_ko=?'; p.append(typ)
if win:
    sql += ' AND contest_winner=1'
sql += ' ORDER BY date DESC LIMIT 1000'
data = rows(sql,p)
st.caption(f'현재 조건에서 최대 1,000건 표시 · 조회 {len(data):,}건 · **행 클릭 = 빠른 분석 팝업**')
table=[{
    '게시일': x['date'][:10] if x['date'] else '', '티커':x['ticker'], '기업':x['company_name'], '작성자':x['author'],
    '방향':x['direction_ko'], 'Contest':bool(x['contest_winner']), '이벤트/유형':x['idea_type_ko'], '예상기간':x['horizon_raw'],
    '태그':', '.join(json.loads(x['narrative_tags_ko'] or '[]')), '1Y 방향조정 수익률':x['idea_return_1y']
} for x in data]
event=st.dataframe(table, use_container_width=True, hide_index=True, height=650,
                   on_select='rerun', selection_mode='single-row', key='idea_explorer_table')
sel=event.selection.rows if event and hasattr(event,'selection') else []
if sel:
    idea_quick_view(data[sel[0]]['idea_id'])
st.caption('기존 수익률 데이터는 원 데이터셋의 제한적 커버리지를 그대로 보존한 값입니다. 최종 성과평가에는 별도 최신 검증이 필요합니다.')
