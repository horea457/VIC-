import streamlit as st
from components.db import rows,row
from components.ui import apply_css,page_header,render_verified_postmortem

st.set_page_config(page_title='사후분석 DB',layout='wide')
apply_css()
page_header('POSTMORTEM DATABASE','사후분석 DB','기업이 무엇을 하는지 → 당시 VIC 투자모델 → 숫자·밸류에이션 → Claim별 가정과 반증조건 → 실제 결과 → 성공·실패 원인까지 한 화면에서 봅니다.')

q=st.text_input('기업·티커·작성자 검색',placeholder='예: APH, AMRN')
verdict=st.selectbox('종합 판정',['전체','매우 성공','성공','대체로 성공','혼합','판정 제한','대체로 실패','실패','매우 실패'])
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
    table=[{'게시일':x['date'][:10],'티커':x['ticker'],'기업':x['company_name'],'방향':x['research_direction_ko'],'종합판정':x['overall_verdict_ko'],'성공 패턴':x['success_pattern_ko'],'실패/혼합 패턴':x['failure_pattern_ko'],'Thesis':x['thesis_score'],'프로세스':x['process_score'],'기준일':x['research_asof']} for x in data]
    ev=st.dataframe(table,use_container_width=True,hide_index=True,on_select='rerun',selection_mode='single-row',height=min(520,100+len(table)*44),key='v6_postmortem')
    sr=ev.selection.rows if ev and hasattr(ev,'selection') else []
    if sr:
        st.session_state['v6_post_id']=data[sr[0]]['idea_id']
    iid=st.session_state.get('v6_post_id') or data[0]['idea_id']
    st.markdown('---')
    render_verified_postmortem(iid,compact=False)

with st.expander('심층화 대기 초안은 어디 갔나?'):
    n=row('''SELECT COUNT(*) n FROM postmortems WHERE idea_id NOT IN (SELECT idea_id FROM deep_analysis_meta)''')['n']
    st.write(f'기존 짧은 사후분석 초안 {n:,}건은 이 페이지 메인 목록에서 제외했습니다. 숫자·산식·Claim별 실제 결과를 채운 뒤에만 심층 완료로 승격합니다.')
