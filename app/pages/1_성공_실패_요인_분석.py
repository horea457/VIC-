import streamlit as st
from components.db import rows,row
from components.ui import apply_css,page_header,idea_quick_view

st.set_page_config(page_title='성공·실패 요인 분석',layout='wide')
apply_css()
page_header('PATTERN LAB','성공·실패 요인 분석','성공/실패 요인을 카테고리화하고 → 패턴을 누르면 기업·투자 아이디어 → 행을 누르면 실제 심층 사후분석으로 이어집니다.')

mode=st.radio('구분',['전체','성공','실패','혼합'],horizontal=True)
sql='''SELECT p.pattern_id,p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,p.counterfactual_question_ko,
       COUNT(DISTINCT CASE WHEN d.idea_id IS NOT NULL THEN m.idea_id END) deep_n,
       COUNT(DISTINCT m.idea_id) mapped_n
       FROM verified_pattern_catalog p
       LEFT JOIN verified_pattern_map m ON m.pattern_id=p.pattern_id
       LEFT JOIN deep_analysis_meta d ON d.idea_id=m.idea_id'''
ps=[]
if mode!='전체': sql+=' WHERE p.polarity_ko=?';ps=[mode]
sql+=' GROUP BY p.pattern_id ORDER BY deep_n DESC,mapped_n DESC,p.pattern_name_ko'
patterns=rows(sql,ps)

st.subheader('주요 성공·실패 패턴')
cols=st.columns(3)
for i,p in enumerate(patterns):
    with cols[i%3]:
        icon='✅' if p['polarity_ko']=='성공' else ('❌' if p['polarity_ko']=='실패' else '◐')
        st.markdown(f"<div class='pattern-card'><div class='pattern-kicker'>{p['polarity_ko']} · {p['category_ko']}</div><div class='pattern-name'>{icon} {p['pattern_name_ko']}</div><div class='pattern-meta'>심층 완료 {p['deep_n']}건 · 기존 연결 {p['mapped_n']}건</div><div class='pattern-desc'>{p['definition_ko']}</div></div>",unsafe_allow_html=True)
        if st.button('기업·아이디어 보기',key='p_'+p['pattern_id'],use_container_width=True):
            st.session_state['v6_pattern']=p['pattern_id'];st.rerun()

pid=st.session_state.get('v6_pattern') or (patterns[0]['pattern_id'] if patterns else None)
if pid:
    P=row('SELECT * FROM verified_pattern_catalog WHERE pattern_id=?',(pid,))
    st.markdown('---')
    st.header(P['pattern_name_ko'])
    st.write(P['definition_ko'])
    st.info(f"**이 패턴을 반증하는 핵심 질문**  \n\n{P['counterfactual_question_ko']}")

    deep=rows('''SELECT i.idea_id,i.date,i.ticker,i.company_name,i.author,p.research_direction_ko,p.overall_verdict_ko,
                        d.one_line_verdict_ko,d.thesis_score,d.research_asof
                 FROM verified_pattern_map m JOIN deep_analysis_meta d ON d.idea_id=m.idea_id
                 JOIN ideas_master i ON i.idea_id=m.idea_id JOIN postmortems p ON p.idea_id=m.idea_id
                 WHERE m.pattern_id=? ORDER BY i.date DESC''',(pid,))
    st.subheader('심층 검증 완료 사례')
    if deep:
        table=[{'게시일':x['date'][:10],'티커':x['ticker'],'기업':x['company_name'],'방향':x['research_direction_ko'],'종합판정':x['overall_verdict_ko'],'Thesis 점수':x['thesis_score'],'한 줄 결론':x['one_line_verdict_ko']} for x in deep]
        ev=st.dataframe(table,use_container_width=True,hide_index=True,on_select='rerun',selection_mode='single-row',height=min(420,100+len(table)*46))
        sr=ev.selection.rows if ev and hasattr(ev,'selection') else []
        if sr: idea_quick_view(deep[sr[0]]['idea_id'])
    else:
        st.info('이 패턴은 아직 Amarin/Amphenol급 심층 검증 사례가 없습니다.')

    with st.expander('심층화 대기 후보 보기'):
        cand=rows('''SELECT i.date,i.ticker,i.company_name,i.author,i.direction_ko,p.overall_verdict_ko
                     FROM verified_pattern_map m JOIN ideas_master i ON i.idea_id=m.idea_id
                     LEFT JOIN postmortems p ON p.idea_id=m.idea_id
                     WHERE m.pattern_id=? AND m.idea_id NOT IN (SELECT idea_id FROM deep_analysis_meta)
                     ORDER BY i.date DESC LIMIT 150''',(pid,))
        st.caption('기존 표준 초안/패턴 연결입니다. 심층 검증 완료 전에는 확정 사례로 세지 않습니다.')
        st.dataframe(cand,use_container_width=True,hide_index=True,height=min(420,100+len(cand)*36))
