import streamlit as st
from components.ui import apply_css, page_header, idea_quick_view
from components.db import rows, row

st.set_page_config(page_title='성공·실패 패턴', layout='wide')
apply_css()
page_header(
    'PATTERN LAB',
    '성공·실패 패턴',
    '검증 완료 패턴을 먼저 보고 → 해당 기업·VIC 아이디어를 선택 → 팝업에서 실제 사후전개와 Claim별 성공·실패를 확인합니다.'
)

verified_tab, auto_tab = st.tabs(['✓ 사후검증 완료 패턴', '자동 스크리닝 후보'])

with verified_tab:
    st.success('이 탭은 VIC 원문을 읽고 후속 기업 공시·SEC·IR 자료로 실제 사후전개를 확인한 사례만 포함합니다. 현재 1차 배치이며 계속 확장할 수 있습니다.')
    polarity = st.radio('패턴 구분', ['전체','성공','실패','혼합'], horizontal=True, key='vpol')
    sql='''
    SELECT p.pattern_id,p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,p.counterfactual_question_ko,
           COUNT(m.idea_id) AS verified_ideas
    FROM verified_pattern_catalog p LEFT JOIN verified_pattern_map m USING(pattern_id)
    '''
    ps=[]
    if polarity!='전체':
        sql += ' WHERE p.polarity_ko=?'; ps.append(polarity)
    sql += ' GROUP BY p.pattern_id ORDER BY verified_ideas DESC,p.pattern_name_ko'
    vp=rows(sql,ps)

    st.subheader('주요 검증 패턴')
    cols=st.columns(4)
    for i,p in enumerate(vp):
        with cols[i%4]:
            st.markdown(
                f"<div class='pattern-card'><div class='pattern-kicker'>{p['polarity_ko']} · {p['category_ko']}</div>"
                f"<div class='pattern-name'>{p['pattern_name_ko']}</div>"
                f"<div class='pattern-meta'>검증 사례 {p['verified_ideas'] or 0}건</div>"
                f"<div class='pattern-desc'>{p['definition_ko']}</div></div>", unsafe_allow_html=True)
            if st.button('검증 사례 보기', key=f"vpat_{p['pattern_id']}", use_container_width=True):
                st.session_state['verified_pattern_id']=p['pattern_id']; st.rerun()

    selected=st.session_state.get('verified_pattern_id')
    valid={x['pattern_id'] for x in vp}
    if selected not in valid:
        selected=vp[0]['pattern_id'] if vp else None
        st.session_state['verified_pattern_id']=selected

    if selected:
        P=row('SELECT * FROM verified_pattern_catalog WHERE pattern_id=?',(selected,))
        st.markdown('---')
        st.header(P['pattern_name_ko'])
        st.write(P['definition_ko'])
        st.info(f"**핵심 반증 질문**  \n\n{P['counterfactual_question_ko']}")

        q=st.text_input('검증된 기업·티커·작성자 검색',key='verified_pattern_search')
        qsql='''
        SELECT m.idea_id,i.date,i.ticker,i.company_name,i.author,
               p.research_direction_ko,p.overall_verdict_ko,p.thesis_verdict_ko,
               p.corrected_return_1y,p.corrected_return_3y,p.corrected_return_5y,p.research_asof
        FROM verified_pattern_map m
        JOIN ideas_master i ON i.idea_id=m.idea_id
        JOIN postmortems p ON p.idea_id=m.idea_id
        WHERE m.pattern_id=?
        '''
        params=[selected]
        if q:
            qsql += ' AND (i.ticker LIKE ? OR i.company_name LIKE ? OR i.author LIKE ?)'; params += [f'%{q}%']*3
        qsql += ' ORDER BY i.date DESC'
        data=rows(qsql,params)
        if data:
            table=[]
            for x in data:
                table.append({
                    '게시일':x['date'][:10] if x['date'] else '', '티커':x['ticker'], '기업':x['company_name'],
                    '실제 논지방향':x['research_direction_ko'], '작성자':x['author'],
                    '핵심논지':x['thesis_verdict_ko'], '종합판정':x['overall_verdict_ko'],
                    '1년':'—' if x['corrected_return_1y'] is None else f"{x['corrected_return_1y']:+.1%}",
                    '3년':'—' if x['corrected_return_3y'] is None else f"{x['corrected_return_3y']:+.1%}",
                    '5년':'—' if x['corrected_return_5y'] is None else f"{x['corrected_return_5y']:+.1%}",
                    '검증기준일':x['research_asof']
                })
            st.caption('행을 클릭하면 기업 설명 → 원 투자논지 → 실제 전개 → Claim별 판정 → 패턴/반증 질문이 팝업으로 열립니다.')
            ev=st.dataframe(table,use_container_width=True,hide_index=True,height=min(470,110+len(table)*42),
                            on_select='rerun',selection_mode='single-row',key=f'verified_ideas_{selected}')
            srows=ev.selection.rows if ev and hasattr(ev,'selection') else []
            if srows:
                idea_quick_view(data[srows[0]]['idea_id'])
        else:
            st.info('이 패턴의 검증 사례가 없습니다.')

with auto_tab:
    st.info('이 탭은 13,656개 전체 corpus를 탐색하기 위한 자동 후보입니다. 인과관계를 확정한 자료가 아니며, 검증 완료 사례와 구분합니다.')
    polarity = st.radio('먼저 볼 패턴', ['성공 패턴','실패 패턴'], index=1, horizontal=True, key='apol')
    pol = '성공' if polarity == '성공 패턴' else '실패'

    patterns = rows('''
    SELECT p.*, s.matched_ideas, s.median_return, s.positive_rate, s.strong_success, s.strong_failure
    FROM pattern_catalog p
    LEFT JOIN pattern_stats s USING(pattern_id)
    WHERE p.polarity_ko=?
    ORDER BY s.matched_ideas DESC, p.pattern_name_ko
    ''',(pol,))

    st.subheader('자동 주요 패턴 후보')
    cols = st.columns(4)
    for i,p in enumerate(patterns[:8]):
        with cols[i % 4]:
            med = p['median_return']
            med_txt = '—' if med is None else f"{med:+.0%}"
            st.markdown(
                f"<div class='pattern-card'><div class='pattern-kicker'>{p['category_ko']}</div>"
                f"<div class='pattern-name'>{p['pattern_name_ko']}</div>"
                f"<div class='pattern-meta'>후보 {p['matched_ideas'] or 0:,}건 · 대표수익률 중앙값 {med_txt}</div>"
                f"<div class='pattern-desc'>{p['definition_ko']}</div></div>", unsafe_allow_html=True)
            if st.button('자동 후보 보기', key=f"apat_{p['pattern_id']}", use_container_width=True):
                st.session_state['selected_pattern_id'] = p['pattern_id']; st.rerun()

    selected = st.session_state.get('selected_pattern_id')
    valid_ids = {p['pattern_id'] for p in patterns}
    if selected not in valid_ids:
        selected = patterns[0]['pattern_id'] if patterns else None
        st.session_state['selected_pattern_id'] = selected

    if selected:
        P = row('''SELECT p.*,s.matched_ideas,s.median_return,s.positive_rate,s.strong_success,s.strong_failure
                   FROM pattern_catalog p LEFT JOIN pattern_stats s USING(pattern_id) WHERE p.pattern_id=?''',(selected,))
        st.markdown('---'); st.header(P['pattern_name_ko']); st.write(P['definition_ko'])
        mc1,mc2,mc3,mc4 = st.columns(4)
        mc1.metric('자동 후보', f"{P['matched_ideas'] or 0:,}건")
        mc2.metric('대표 수익률 중앙값', '—' if P['median_return'] is None else f"{P['median_return']:+.1%}")
        mc3.metric('강한 성공 후보', f"{P['strong_success'] or 0:,}")
        mc4.metric('강한 실패 후보', f"{P['strong_failure'] or 0:,}")
        st.markdown(f"**반증 질문:** {P['counterfactual_question_ko']}")

        q = st.text_input('기업·티커·작성자 검색', key='pattern_search')
        direction = st.selectbox('방향', ['전체','롱','숏'], key='pattern_direction')
        sql = '''
        SELECT m.idea_id, i.date, i.ticker, i.company_name, i.author, i.direction_ko,
               m.performance_horizon_ko, m.direction_adjusted_return, m.stock_verdict_ko,
               a.analysis_status_ko, a.overall_verdict_ko
        FROM idea_pattern_map m JOIN ideas_master i ON i.idea_id=m.idea_id
        LEFT JOIN analysis a ON a.idea_id=m.idea_id WHERE m.pattern_id=?
        '''
        ps=[selected]
        if q:
            sql += ' AND (i.ticker LIKE ? OR i.company_name LIKE ? OR i.author LIKE ?)'; ps += [f'%{q}%']*3
        if direction != '전체':
            sql += ' AND i.direction_ko=?'; ps.append(direction)
        sql += ' ORDER BY ABS(m.direction_adjusted_return) DESC, i.date DESC LIMIT 250'
        data=rows(sql,ps)
        if data:
            table=[{
                '게시일':x['date'][:10] if x['date'] else '', '티커':x['ticker'], '기업':x['company_name'],
                '방향(원DB)':x['direction_ko'], '작성자':x['author'], '성과기간':x['performance_horizon_ko'],
                '방향조정 수익률':'—' if x['direction_adjusted_return'] is None else f"{x['direction_adjusted_return']:+.1%}",
                '자동 판정':x['stock_verdict_ko'], '분석상태':x['analysis_status_ko'] or '미분석'
            } for x in data]
            ev=st.dataframe(table,use_container_width=True,hide_index=True,height=480,on_select='rerun',selection_mode='single-row',key=f'auto_ideas_{selected}')
            sr=ev.selection.rows if ev and hasattr(ev,'selection') else []
            if sr: idea_quick_view(data[sr[0]]['idea_id'])
