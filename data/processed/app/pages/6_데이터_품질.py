import streamlit as st
from components.ui import apply_css, page_header
from components.db import rows
st.set_page_config(page_title='데이터 품질', layout='wide'); apply_css()
page_header('DATA QUALITY','데이터 품질 및 검증상태','원본 데이터, 자동 추출, 주가 기반 예비판정, 외부 사실검증을 서로 섞지 않기 위한 품질 관리 화면입니다.')

st.subheader('원본 커버리지')
st.dataframe([{'항목':x['metric_ko'],'값':x['value_text']} for x in rows('SELECT * FROM dataset_stats')],use_container_width=True,hide_index=True)

c1,c2,c3,c4=st.columns(4)
c1.metric('자동 프로필', rows('SELECT COUNT(*) n FROM idea_auto_profile')[0]['n'])
c2.metric('자동 Claim', rows('SELECT COUNT(*) n FROM claims')[0]['n'])
c3.metric('패턴 후보 연결', rows('SELECT COUNT(*) n FROM idea_pattern_map')[0]['n'])
c4.metric('자동 예비분석', rows("SELECT COUNT(*) n FROM analysis WHERE analysis_status_ko='자동 예비분석'")[0]['n'])

st.subheader('연도별 커버리지')
st.dataframe(rows('SELECT year AS 연도,ideas AS 아이디어,long_ideas AS 롱,short_ideas AS 숏,contest_winners AS Contest_Winner,performance_covered AS 기존_성과데이터 FROM year_summary ORDER BY year'),use_container_width=True,hide_index=True,height=420)

st.subheader('자동 태그 커버리지')
st.dataframe(rows('SELECT tag_ko AS 태그,ideas AS 아이디어수 FROM tag_summary ORDER BY ideas DESC'),use_container_width=True,hide_index=True,height=420)

st.subheader('판정 레벨')
st.markdown('''1. **원본**: VIC에서 가져온 메타데이터·본문·Catalyst·기존 성과값  
2. **자동 V3 태깅**: 강한 문구·반복 빈도·Catalyst 가중치로 논지 후보 분류  
3. **자동 Claim 추출**: 주장 → 암묵적 가정 → 반증조건 → 선행지표 구조화  
4. **자동 예비판정**: 기존 방향조정 주가성과와 당시 논지의 정합성을 보는 탐색용 결과  
5. **정밀 검증**: 실제 사업·산업·이벤트 데이터를 이용해 원래 Claim의 성립 여부를 판정  
6. **고신뢰 판정**: 근거 출처와 최초 반증 시점을 재검토한 결과''')
st.warning('현재 V3의 성공/실패는 **자동 예비판정**입니다. 주가가 올랐다는 이유만으로 원래 투자논지가 맞았다고 확정하지 않습니다. 사업 결과·이벤트 실행 여부·현재 상태는 외부 사실검증 전까지 명시적으로 “외부 검증 필요”로 유지합니다.')
