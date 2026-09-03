import streamlit as st
from components.db import rows,row
from components.ui import apply_css,page_header

st.set_page_config(page_title='VIC 허구 반증 DB',page_icon='◈',layout='wide',initial_sidebar_state='expanded')
apply_css()
page_header('VIC FALSIFICATION DB','외부자료 검증 심층분석 DB','자동·초벌 분석은 제외하고, 기업·증권·논지·실제 결과까지 검증 완료한 사례만 보여줍니다.')

S=row('''SELECT
 (SELECT COUNT(DISTINCT ticker) FROM ideas_master) companies,
 (SELECT COUNT(*) FROM deep_analysis_meta) deep,
 (SELECT COUNT(*) FROM deep_analysis_claims) claims,
 (SELECT COUNT(*) FROM deep_analysis_sources) sources''')
c1,c2,c3,c4=st.columns(4)
c1.metric('심층 사후분석',f"{S['deep']:,}건")
c2.metric('분석 기업·티커',f"{S['companies']:,}개")
c3.metric('검증 Claim',f"{S['claims']:,}개")
c4.metric('연결 근거자료',f"{S['sources']:,}개")

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
        st.session_state['v11_post_id']=data[sr[0]]['idea_id']
        st.switch_page('pages/2_사후분석_DB.py')
else:
    st.info('검색 조건에 맞는 심층 완료 사례가 없습니다.')

st.caption('Production DB에는 심층 검증 완료 사례만 저장됩니다. 새 연구 배치가 GitHub main에 반영되면 목록과 수치가 함께 증가합니다.')
