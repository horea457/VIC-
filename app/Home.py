import streamlit as st
from components.db import rows,row
from components.ui import apply_css,page_header,idea_quick_view

st.set_page_config(page_title='VIC 허구 반증 DB',page_icon='◈',layout='wide',initial_sidebar_state='expanded')
apply_css()
page_header('VIC FALSIFICATION DB','VIC 투자 아이디어 사후검증 DB','메인은 전체 현황과 검색만 보여줍니다. 패턴 연구와 개별 심층 리포트는 각각 한 페이지로 통합했습니다.')

S=row('''SELECT
 (SELECT COUNT(*) FROM ideas_master) total,
 (SELECT COUNT(*) FROM deep_analysis_meta) deep,
 (SELECT COUNT(*) FROM postmortems) drafts,
 (SELECT COUNT(*) FROM deep_analysis_claims) claims''')
c1,c2,c3,c4=st.columns(4)
c1.metric('전체 VIC 아이디어',f"{S['total']:,}")
c2.metric('심층 사후분석 완료',f"{S['deep']:,}")
c3.metric('심층 Claim',f"{S['claims']:,}")
c4.metric('심층화 대기 초안',f"{max(0,S['drafts']-S['deep']):,}")

st.markdown('---')
st.subheader('바로 탐색')
a,b=st.columns(2)
with a:
    st.markdown('### 성공·실패 요인 분석')
    st.write('반복되는 성공·실패 메커니즘을 먼저 보고, 해당 기업과 VIC 아이디어로 들어갑니다.')
    if st.button('성공·실패 요인 분석 열기',type='primary',use_container_width=True):
        st.switch_page('pages/1_성공_실패_요인_분석.py')
with b:
    st.markdown('### 사후분석 DB')
    st.write('기업·티커를 검색해 당시 투자논지와 실제 결과, Claim별 성공·실패를 한 번에 봅니다.')
    if st.button('사후분석 DB 열기',use_container_width=True):
        st.switch_page('pages/2_사후분석_DB.py')

st.markdown('---')
st.subheader('심층 사후분석 빠른 검색')
q=st.text_input('기업·티커·작성자',placeholder='예: APH, Amarin, Jumbo52')
sql='''SELECT i.idea_id,i.date,i.ticker,i.company_name,i.author,p.research_direction_ko,p.overall_verdict_ko,
              d.one_line_verdict_ko,d.thesis_score,d.research_asof
       FROM deep_analysis_meta d JOIN ideas_master i USING(idea_id) JOIN postmortems p USING(idea_id) WHERE 1=1'''
ps=[]
if q:
    sql+=' AND (i.ticker LIKE ? OR i.company_name LIKE ? OR i.author LIKE ?)';ps=[f'%{q}%']*3
sql+=' ORDER BY i.date DESC'
data=rows(sql,ps)
if data:
    table=[{'게시일':x['date'][:10],'티커':x['ticker'],'기업':x['company_name'],'방향':x['research_direction_ko'],'종합판정':x['overall_verdict_ko'],'Thesis 점수':x['thesis_score'],'분석기준일':x['research_asof']} for x in data]
    ev=st.dataframe(table,use_container_width=True,hide_index=True,on_select='rerun',selection_mode='single-row',height=min(380,100+len(table)*42))
    sr=ev.selection.rows if ev and hasattr(ev,'selection') else []
    if sr:
        idea_quick_view(data[sr[0]]['idea_id'])
else:
    st.info('검색 조건에 맞는 심층 완료 사례가 없습니다.')

st.caption('현재 “심층 완료”는 Amarin/Amphenol급 기준을 충족한 사례만 집계합니다. 기존 짧은 초안과 자동 태그는 완료로 세지 않습니다.')
