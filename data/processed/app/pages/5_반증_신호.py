import streamlit as st
from components.ui import apply_css, page_header
from components.db import rows
st.set_page_config(page_title='반증 신호', layout='wide'); apply_css()
page_header('EARLY SIGNALS','무엇이 먼저 깨졌나','최종 손익계산서나 주가보다 먼저 나타나는 공개 데이터를 축적하기 위한 모니터링 기준입니다.')
s=rows('SELECT signal_ko,category_ko,definition_ko FROM signal_taxonomy')
st.dataframe([{'선행 신호':x['signal_ko'],'범주':x['category_ko'],'관찰할 데이터':x['definition_ko']} for x in s],use_container_width=True,hide_index=True)
st.subheader('향후 이 화면에 붙일 통계')
st.markdown('''- 실패 아이디어에서 **최초로 깨진 신호의 빈도**
- 해당 신호가 주가 급락 또는 이익 추정치 하향보다 **몇 개월 선행했는지**
- 당시 공개정보만으로 **알 수 있었는지**
- 같은 신호가 성공 사례에서도 얼마나 자주 발생했는지(오탐률)
- 산업별로 가장 유효했던 반증 신호''')
