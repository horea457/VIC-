import json
import streamlit as st
from components.ui import apply_css, page_header
from components.db import rows
st.set_page_config(page_title='투자논지 라이브러리', layout='wide'); apply_css()
page_header('NARRATIVE LIBRARY','투자논지 라이브러리','VIC에서 반복해서 등장한 서사를 모아 같은 주장이 과거에 어떤 기업에서 나타났는지 탐색합니다.')
tags=rows('SELECT tag_ko,ideas FROM tag_summary ORDER BY ideas DESC')
st.dataframe([{'자동 논지태그':x['tag_ko'],'아이디어 수':x['ideas']} for x in tags],use_container_width=True,hide_index=True,height=300)
tag=st.selectbox('태그를 선택해 사례 보기',[x['tag_ko'] for x in tags])
data=rows('SELECT date,ticker,company_name,author,direction_ko,idea_type_ko,narrative_tags_ko FROM ideas_master WHERE narrative_tags_ko LIKE ? ORDER BY date DESC LIMIT 500',(f'%"{tag}"%',))
st.subheader(f'{tag} · 사례')
st.dataframe([{'게시일':x['date'][:10],'티커':x['ticker'],'기업':x['company_name'],'작성자':x['author'],'방향':x['direction_ko'],'유형':x['idea_type_ko'],'동시 태그':', '.join(json.loads(x['narrative_tags_ko']))} for x in data],use_container_width=True,hide_index=True,height=560)
st.warning('현재는 키워드 기반 1차 태그입니다. 이후 Claim 정밀분석에서 실제 명제와 결과 통계를 별도 생성합니다.')
