import streamlit as st
from components.ui import apply_css, page_header, idea_quick_view
from components.db import rows

st.set_page_config(page_title='검증 우선순위', layout='wide')
apply_css()
page_header('RESEARCH QUEUE','검증 우선순위','자동 예비분석 중 실제 외부 데이터 검증 가치가 높은 사례를 우선순위로 정렬합니다. Contest Winner, 큰 사후성과, 반복 패턴, 충분한 사후기간을 반영합니다.')

c1,c2,c3,c4=st.columns(4)
c1.metric('전체 자동 예비분석', rows("SELECT COUNT(*) n FROM analysis WHERE analysis_status_ko='자동 예비분석'")[0]['n'])
c2.metric('우선순위 70+', rows('SELECT COUNT(*) n FROM analysis WHERE research_priority>=70')[0]['n'])
c3.metric('우선순위 50+', rows('SELECT COUNT(*) n FROM analysis WHERE research_priority>=50')[0]['n'])
c4.metric('Claim', rows('SELECT COUNT(*) n FROM claims')[0]['n'])

st.caption('우선순위 점수는 “정답 확률”이 아니라 **다음에 실제 결과를 조사할 가치**를 뜻합니다. 아래 행을 클릭하면 빠른 분석 팝업이 열립니다.')

left,right=st.columns([1,1])
with left:
    minp=st.slider('최소 우선순위',0,100,50,5)
with right:
    direction=st.selectbox('방향',['전체','롱','숏'])

sql='''SELECT idea_id,date,ticker,company_name,author,direction_ko,contest_winner,research_priority,overall_verdict_ko,failure_mechanism_ko,representative_horizon_ko,representative_return
       FROM verification_queue WHERE research_priority>=?'''
ps=[minp]
if direction!='전체': sql+=' AND direction_ko=?'; ps.append(direction)
sql+=' ORDER BY research_priority DESC,ABS(COALESCE(representative_return,0)) DESC LIMIT 500'
data=rows(sql,ps)

table=[{
 '게시일':x['date'][:10] if x['date'] else '', '티커':x['ticker'],'기업':x['company_name'],'방향':x['direction_ko'],
 'Contest':bool(x['contest_winner']),'우선순위':x['research_priority'],'현재 예비판정':x['overall_verdict_ko'],
 '실패패턴 후보':x['failure_mechanism_ko'] or '—','성과기간':x['representative_horizon_ko'] or '—',
 '방향조정 수익률':'—' if x['representative_return'] is None else f"{x['representative_return']:+.1%}"
} for x in data]

event=st.dataframe(table,use_container_width=True,hide_index=True,height=600,on_select='rerun',selection_mode='single-row')
sel=event.selection.rows if event and hasattr(event,'selection') else []
if sel:
    chosen=data[sel[0]]
    idea_quick_view(chosen['idea_id'])
