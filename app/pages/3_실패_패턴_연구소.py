import streamlit as st
from components.ui import apply_css, page_header
from components.db import rows
st.set_page_config(page_title='실패 패턴 연구소', layout='wide'); apply_css()
page_header('FAILURE LAB','실패 패턴 연구소','실패를 “매출 둔화” 같은 결과가 아니라, 근본 분석 오류 → 경제적 메커니즘 → 전달 경로 → 선행 신호로 분해합니다.')
doms=[x['domain_ko'] for x in rows('SELECT DISTINCT domain_ko FROM failure_patterns ORDER BY domain_ko')]
d=st.selectbox('실패 영역',['전체']+doms)
data=rows('SELECT domain_ko,mechanism_ko,definition_ko FROM failure_patterns '+('ORDER BY domain_ko,mechanism_ko' if d=='전체' else 'WHERE domain_ko=? ORDER BY mechanism_ko'), () if d=='전체' else (d,))
st.dataframe([{'영역':x['domain_ko'],'실패 메커니즘':x['mechanism_ko'],'정의':x['definition_ko']} for x in data],use_container_width=True,hide_index=True,height=510)
st.subheader('근본 분석 오류')
e=rows('SELECT error_ko,definition_ko FROM analytical_errors')
st.dataframe([{'오류':x['error_ko'],'설명':x['definition_ko']} for x in e],use_container_width=True,hide_index=True)
st.caption('향후 정밀 분석이 누적되면 각 실패 패턴의 빈도·성공률·대표 사례·최초 반증 신호 선행기간이 이 화면에 붙습니다.')
