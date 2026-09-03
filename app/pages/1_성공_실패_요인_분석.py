from collections import defaultdict

import streamlit as st

from components.db import rows
from components.ui import apply_css, idea_quick_view, page_header

st.set_page_config(page_title='성공·실패 요인 분석', layout='wide')
apply_css()
page_header(
    'PATTERN LAB',
    '성공·실패 요인 분석',
    '심층 검증 사례의 성공·실패 태그를 직접 집계합니다. 자동 분류나 미분석 후보는 포함하지 않습니다.',
)

ideas = rows('''
    SELECT i.idea_id,i.date,i.ticker,i.company_name,i.author,
           p.research_direction_ko,p.overall_verdict_ko,
           p.success_pattern_ko,p.failure_pattern_ko,
           d.one_line_verdict_ko,d.thesis_score,d.research_asof
    FROM deep_analysis_meta d
    JOIN ideas_master i USING(idea_id)
    JOIN postmortems p USING(idea_id)
    ORDER BY i.date DESC
''')

def tags(value):
    excluded = {'해당 없음', '없음'}
    return [x.strip() for x in (value or '').split(';') if x.strip() and x.strip() not in excluded]

groups = defaultdict(list)
for idea in ideas:
    for tag in tags(idea['success_pattern_ko']):
        groups[('성공', tag)].append(idea)
    for tag in tags(idea['failure_pattern_ko']):
        groups[('실패', tag)].append(idea)

mode = st.radio('구분', ['전체', '성공', '실패'], horizontal=True)
patterns = [
    (kind, tag, items)
    for (kind, tag), items in groups.items()
    if mode == '전체' or kind == mode
]
patterns.sort(key=lambda x: (-len(x[2]), x[0], x[1]))

st.subheader('심층분석에서 반복된 패턴')
cols = st.columns(3)
for i, (kind, tag, items) in enumerate(patterns):
    with cols[i % 3]:
        icon = '✅' if kind == '성공' else '❌'
        st.markdown(
            f"<div class='pattern-card'><div class='pattern-kicker'>{kind}</div>"
            f"<div class='pattern-name'>{icon} {tag}</div>"
            f"<div class='pattern-meta'>심층 사례 {len(items)}건</div></div>",
            unsafe_allow_html=True,
        )
        if st.button('기업·아이디어 보기', key=f'{kind}:{tag}', use_container_width=True):
            st.session_state['deep_pattern'] = (kind, tag)
            st.rerun()

selected = st.session_state.get('deep_pattern')
if selected and selected in groups:
    kind, tag = selected
    selected_ideas = groups[selected]
    st.markdown('---')
    st.header(f"{'✅' if kind == '성공' else '❌'} {tag}")
    st.caption(f'심층 검증 완료 {len(selected_ideas)}건')
    table = [
        {
            '게시일': x['date'][:10], '티커': x['ticker'], '기업': x['company_name'],
            '방향': x['research_direction_ko'], '종합판정': x['overall_verdict_ko'],
            'Thesis': x['thesis_score'], '한 줄 결론': x['one_line_verdict_ko'],
        }
        for x in selected_ideas
    ]
    event = st.dataframe(
        table, use_container_width=True, hide_index=True, on_select='rerun',
        selection_mode='single-row', height=min(520, 100 + len(table) * 46),
    )
    picked = event.selection.rows if event and hasattr(event, 'selection') else []
    if picked:
        idea_quick_view(selected_ideas[picked[0]]['idea_id'])
