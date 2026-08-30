import streamlit as st
from components.ui import apply_css, page_header, idea_quick_view
from components.db import rows

st.set_page_config(page_title='사후분석 완료', layout='wide')
apply_css()
st.caption('V4.1 · 사후분석 완료 전용 페이지 · 17건')
page_header('VERIFIED POSTMORTEMS','사후분석 완료 사례','기업이 무엇을 하는지부터 당시 투자논지·밸류에이션·후속 실적·Claim별 성공/실패·반증 질문까지 깊게 재구성한 사례만 모았습니다.')

all_rows=rows('''
SELECT p.idea_id,i.date,i.ticker,i.company_name,i.author,p.research_direction_ko,
       p.overall_verdict_ko,p.thesis_verdict_ko,p.business_verdict_ko,p.current_verdict_ko,
       p.success_pattern_ko,p.failure_pattern_ko,p.corrected_return_1y,p.corrected_return_3y,p.corrected_return_5y,
       p.confidence,p.research_asof
FROM postmortems p JOIN ideas_master i ON i.idea_id=p.idea_id
ORDER BY i.date DESC
''')

vopts=['전체']+sorted({x['overall_verdict_ko'] for x in all_rows})
patopts=['전체']+sorted({x['success_pattern_ko'] for x in all_rows if x['success_pattern_ko']!='해당 없음'} | {x['failure_pattern_ko'] for x in all_rows if x['failure_pattern_ko']!='해당 없음'})
q=st.text_input('기업·티커·작성자 검색')
a,b=st.columns(2)
with a: verdict=st.selectbox('종합 판정',vopts)
with b: pattern=st.selectbox('성공·실패 패턴',patopts)

def keep(x):
    if q and q.lower() not in ' '.join([x['ticker'] or '',x['company_name'] or '',x['author'] or '']).lower(): return False
    if verdict!='전체' and x['overall_verdict_ko']!=verdict: return False
    if pattern!='전체' and pattern not in (x['success_pattern_ko'],x['failure_pattern_ko']): return False
    return True

data=[x for x in all_rows if keep(x)]

m1,m2,m3,m4=st.columns(4)
m1.metric('사후분석 완료',len(all_rows))
m2.metric('현재 표시',len(data))
m3.metric('성공/매우 성공',sum('성공' in x['overall_verdict_ko'] and '실패' not in x['overall_verdict_ko'] for x in all_rows))
m4.metric('실패/대체로 실패',sum('실패' in x['overall_verdict_ko'] for x in all_rows))

st.caption('행을 클릭하면 실제 사후 리서치 팝업이 열립니다.')
table=[]
for x in data:
    table.append({
        '게시일':x['date'][:10] if x['date'] else '', '티커':x['ticker'], '기업':x['company_name'],
        '실제 논지방향':x['research_direction_ko'],'작성자':x['author'], '핵심논지':x['thesis_verdict_ko'],
        '종합판정':x['overall_verdict_ko'],'성공 패턴':x['success_pattern_ko'],'실패/혼합 패턴':x['failure_pattern_ko'],
        '1년':'—' if x['corrected_return_1y'] is None else f"{x['corrected_return_1y']:+.1%}",
        '3년':'—' if x['corrected_return_3y'] is None else f"{x['corrected_return_3y']:+.1%}",
        '5년':'—' if x['corrected_return_5y'] is None else f"{x['corrected_return_5y']:+.1%}",
        '검증기준일':x['research_asof'],'신뢰도':f"{x['confidence']:.0%}"
    })
if table:
    ev=st.dataframe(table,use_container_width=True,hide_index=True,height=560,on_select='rerun',selection_mode='single-row',key='postmortem_table')
    sr=ev.selection.rows if ev and hasattr(ev,'selection') else []
    if sr:
        selected_idea_id=data[sr[0]]['idea_id']
        st.session_state['v41_selected_postmortem']=selected_idea_id
        idea_quick_view(selected_idea_id)
    fallback_id=st.session_state.get('v41_selected_postmortem')
    if fallback_id:
        st.markdown('### 선택한 아이디어 · 사후분석 미리보기')
        from components.ui import render_verified_postmortem
        render_verified_postmortem(fallback_id, compact=True)
else:
    st.info('조건에 맞는 사례가 없습니다.')

st.markdown('---')
st.subheader('현재 검증 배치의 의미')
st.write('이 페이지의 사례는 단순히 주가가 올랐는지 내렸는지로 판정하지 않습니다. 원 VIC Claim, 예상했던 메커니즘과 시간축, 실제 후속 사업·재무·이벤트 결과를 분리해 판정합니다. 이후 배치에서 검증 사례 수를 늘리면 패턴별 base rate와 최초 반증신호 통계도 더 신뢰할 수 있게 됩니다.')
