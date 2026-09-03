import streamlit as st
from components.db import rows,row
from components.ui import apply_css,page_header,render_verified_postmortem

st.set_page_config(page_title='사후분석 DB',layout='wide')
apply_css()
page_header('POSTMORTEM DATABASE','심층 사후분석 DB','위 목록에서 아이디어를 선택하면 아래에 검토 완료된 Batch 원문이 같은 구조와 분량으로 펼쳐집니다.')

q=st.text_input('기업·티커·작성자 검색',placeholder='예: APH, AMRN')
verdict_values=[x['overall_verdict_ko'] for x in rows(
    '''SELECT DISTINCT overall_verdict_ko FROM postmortems
       WHERE overall_verdict_ko IS NOT NULL AND TRIM(overall_verdict_ko)<>''
       ORDER BY overall_verdict_ko''')]
verdict=st.selectbox('종합 판정',['전체',*verdict_values])
sql='''SELECT i.idea_id,i.date,i.ticker,i.company_name,i.author,p.research_direction_ko,p.overall_verdict_ko,
              p.success_pattern_ko,p.failure_pattern_ko,d.thesis_type_ko,d.thesis_score,d.process_score,d.research_asof
       FROM deep_analysis_meta d JOIN ideas_master i USING(idea_id) JOIN postmortems p USING(idea_id) WHERE 1=1'''
ps=[]
if q:
    sql+=' AND (i.ticker LIKE ? OR i.company_name LIKE ? OR i.author LIKE ?)';ps += [f'%{q}%']*3
if verdict!='전체':
    sql+=' AND p.overall_verdict_ko=?';ps.append(verdict)
sql+=' ORDER BY i.date DESC'
data=rows(sql,ps)

c1,c2,c3=st.columns(3)
c1.metric('심층 완료',f'{len(data):,}건')
c2.metric('Claim',f"{rows('SELECT COUNT(*) n FROM deep_analysis_claims')[0]['n']:,}개")
c3.metric('분석 기준','VIC 원문 → Claim → 사후검증')

if not data:
    st.info('검색 조건에 맞는 심층 리포트가 없습니다.')
else:
    st.markdown('### 분석 아이디어 목록')
    st.caption('한 행을 누르면 바로 아래에서 기업 설명부터 최종 교훈까지 전체 리포트를 볼 수 있습니다.')
    table=[{'게시일':x['date'][:10],'티커':x['ticker'],'기업':x['company_name'],'방향':x['research_direction_ko'],'종합판정':x['overall_verdict_ko'],'논지 유형':x['thesis_type_ko'],'Thesis':x['thesis_score']} for x in data]
    ev=st.dataframe(table,use_container_width=True,hide_index=True,on_select='rerun',selection_mode='single-row',height=min(440,100+len(table)*40),key='v11_postmortem')
    sr=ev.selection.rows if ev and hasattr(ev,'selection') else []
    if sr:
        st.session_state['v11_post_id']=data[sr[0]]['idea_id']
    visible_ids={x['idea_id'] for x in data}
    iid=st.session_state.get('v11_post_id')
    if iid not in visible_ids:
        iid=data[0]['idea_id']
        st.session_state['v11_post_id']=iid
    st.markdown('---')
    st.markdown('## 선택한 아이디어 · Batch 원문 상세 분석')
    render_verified_postmortem(iid,compact=False)

st.caption('자동·초벌 분석은 DB에서 제거했습니다. 외부자료 검증을 마친 심층분석만 표시합니다.')
