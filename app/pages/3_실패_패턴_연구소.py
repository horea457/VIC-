import streamlit as st
from components.ui import apply_css, page_header
from components.db import rows, row

st.set_page_config(page_title='성공·실패 패턴', layout='wide')
apply_css()
page_header(
    'PATTERN LAB',
    '성공·실패 패턴',
    '패턴을 먼저 고르고 → 해당 기업·VIC 아이디어를 보고 → 개별 아이디어에서 무엇이 맞고 무엇이 깨졌는지 추적합니다.'
)

st.info('현재 패턴 수치는 **VIC 당시 서사 태그 + 방향조정 주가성과**로 만든 자동 후보입니다. 인과관계나 원래 투자논지의 성공·실패를 확정한 값이 아니며, 정밀 검증 결과가 쌓이면 별도 표기로 대체됩니다.')

polarity = st.radio('먼저 볼 패턴', ['성공 패턴','실패 패턴'], index=1, horizontal=True)
pol = '성공' if polarity == '성공 패턴' else '실패'

patterns = rows('''
SELECT p.*, s.matched_ideas, s.median_return, s.positive_rate, s.strong_success, s.strong_failure
FROM pattern_catalog p
LEFT JOIN pattern_stats s USING(pattern_id)
WHERE p.polarity_ko=?
ORDER BY s.matched_ideas DESC, p.pattern_name_ko
''',(pol,))

# 상단: 주요 패턴 카드
st.subheader('주요 패턴')
cols = st.columns(4)
for i,p in enumerate(patterns[:8]):
    with cols[i % 4]:
        med = p['median_return']
        med_txt = '—' if med is None else f"{med:+.0%}"
        st.markdown(
            f"<div class='pattern-card'><div class='pattern-kicker'>{p['category_ko']}</div>"
            f"<div class='pattern-name'>{p['pattern_name_ko']}</div>"
            f"<div class='pattern-meta'>후보 {p['matched_ideas'] or 0:,}건 · 대표수익률 중앙값 {med_txt}</div>"
            f"<div class='pattern-desc'>{p['definition_ko']}</div></div>",
            unsafe_allow_html=True
        )
        if st.button('이 패턴 보기', key=f"pat_{p['pattern_id']}", use_container_width=True):
            st.session_state['selected_pattern_id'] = p['pattern_id']
            st.rerun()

selected = st.session_state.get('selected_pattern_id')
valid_ids = {p['pattern_id'] for p in patterns}
if selected not in valid_ids:
    selected = patterns[0]['pattern_id'] if patterns else None
    st.session_state['selected_pattern_id'] = selected

if not selected:
    st.stop()
P = row('''SELECT p.*,s.matched_ideas,s.median_return,s.positive_rate,s.strong_success,s.strong_failure
           FROM pattern_catalog p LEFT JOIN pattern_stats s USING(pattern_id) WHERE p.pattern_id=?''',(selected,))

st.markdown('---')
st.header(P['pattern_name_ko'])
st.write(P['definition_ko'])
mc1,mc2,mc3,mc4 = st.columns(4)
mc1.metric('자동 후보', f"{P['matched_ideas'] or 0:,}건")
mc2.metric('대표 수익률 중앙값', '—' if P['median_return'] is None else f"{P['median_return']:+.1%}")
mc3.metric('강한 성공 후보', f"{P['strong_success'] or 0:,}")
mc4.metric('강한 실패 후보', f"{P['strong_failure'] or 0:,}")
st.markdown(f"**반증 질문:** {P['counterfactual_question_ko']}")

# 기업 / 아이디어 목록
st.subheader('이 패턴에 해당하는 기업·투자 아이디어')
q = st.text_input('기업·티커·작성자 검색', key='pattern_search')
direction = st.selectbox('방향', ['전체','롱','숏'], key='pattern_direction')

sql = '''
SELECT m.idea_id, i.date, i.ticker, i.company_name, i.author, i.direction_ko, i.contest_winner,
       m.performance_horizon_ko, m.direction_adjusted_return, m.stock_verdict_ko, m.match_type_ko,
       a.analysis_status_ko, a.overall_verdict_ko
FROM idea_pattern_map m
JOIN ideas_master i ON i.idea_id=m.idea_id
LEFT JOIN analysis a ON a.idea_id=m.idea_id
WHERE m.pattern_id=?
'''
ps=[selected]
if q:
    sql += ' AND (i.ticker LIKE ? OR i.company_name LIKE ? OR i.author LIKE ?)'
    ps += [f'%{q}%']*3
if direction != '전체':
    sql += ' AND i.direction_ko=?'; ps.append(direction)
sql += ' ORDER BY ABS(m.direction_adjusted_return) DESC, i.date DESC LIMIT 250'
data=rows(sql,ps)

if not data:
    st.warning('조건에 맞는 아이디어가 없습니다.'); st.stop()

table=[{
    '게시일':x['date'][:10] if x['date'] else '',
    '티커':x['ticker'], '기업':x['company_name'], '방향':x['direction_ko'], '작성자':x['author'],
    '성과기간':x['performance_horizon_ko'], '방향조정 수익률':'—' if x['direction_adjusted_return'] is None else f"{x['direction_adjusted_return']:+.1%}",
    '주가 기준 예비판정':x['stock_verdict_ko'],
    '논지 정밀판정':x['overall_verdict_ko'] or '미검증',
    '분석상태':x['analysis_status_ko'] or '미분석'
} for x in data]

event = st.dataframe(
    table,
    use_container_width=True,
    hide_index=True,
    height=480,
    on_select='rerun',
    selection_mode='single-row',
    key=f"ideas_for_{selected}"
)

sel_rows = event.selection.rows if event and hasattr(event,'selection') else []
if sel_rows:
    chosen = data[sel_rows[0]]
    st.session_state['selected_idea_id'] = chosen['idea_id']
    st.session_state['selected_pattern_context'] = selected
    c1,c2 = st.columns([1,3])
    with c1:
        if st.button('선택 아이디어 상세 분석 열기', type='primary', use_container_width=True):
            st.switch_page('pages/2_기업_아이디어_분석.py')
    with c2:
        st.caption(f"{chosen['date'][:10]} · {chosen['ticker']} · {chosen['company_name']} · {chosen['direction_ko']} · {chosen['author']}")

with st.expander('전체 패턴 분류 보기'):
    allp=rows('''SELECT p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,s.matched_ideas,s.median_return
                 FROM pattern_catalog p LEFT JOIN pattern_stats s USING(pattern_id)
                 ORDER BY p.polarity_ko DESC,s.matched_ideas DESC''')
    st.dataframe([{
        '구분':x['polarity_ko'],'카테고리':x['category_ko'],'패턴':x['pattern_name_ko'],'설명':x['definition_ko'],
        '자동 후보':x['matched_ideas'],'대표수익률 중앙값':'—' if x['median_return'] is None else f"{x['median_return']:+.1%}"
    } for x in allp],use_container_width=True,hide_index=True)
