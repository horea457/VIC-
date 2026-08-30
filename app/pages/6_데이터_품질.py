import streamlit as st
from components.ui import apply_css, page_header
from components.db import rows
st.set_page_config(page_title='데이터 품질', layout='wide'); apply_css()
page_header('DATA QUALITY','데이터 품질 및 검증상태','원본 데이터와 자동 1차 처리, 정밀 검증 결과를 섞지 않기 위한 품질 관리 화면입니다.')
st.subheader('원본 커버리지')
st.dataframe([{'항목':x['metric_ko'],'값':x['value_text']} for x in rows('SELECT * FROM dataset_stats')],use_container_width=True,hide_index=True)
st.subheader('연도별 커버리지')
st.dataframe(rows('SELECT year AS 연도,ideas AS 아이디어,long_ideas AS 롱,short_ideas AS 숏,contest_winners AS Contest_Winner,performance_covered AS 기존_성과데이터 FROM year_summary ORDER BY year'),use_container_width=True,hide_index=True,height=450)
st.subheader('판정 레벨')
st.markdown('''1. **원본**: VIC 데이터셋에서 직접 가져온 메타데이터/본문/기존 성과값  
2. **자동 1차 태깅**: 키워드·정규식 기반 탐색용 분류  
3. **자동 예비판정**: 외부 사후 데이터가 추가된 후 생성하는 예비 결과  
4. **정밀 검증**: 투자논지 시점과 실제 결과를 근거로 검증한 결과  
5. **고신뢰 판정**: 근거 출처와 반증 가능성을 재검토한 결과''')
st.warning('현재 제공 DB에서 성공/실패 정밀분석 필드는 의도적으로 “미분석” 상태입니다. 원문만 보고 사후 결과를 추정해 가짜 정답을 만드는 것을 방지하기 위한 설계입니다.')
