import json
import streamlit as st
from components.ui import apply_css, page_header, idea_quick_view
from components.db import rows

st.set_page_config(page_title='투자논지 라이브러리', layout='wide')
apply_css()
page_header('NARRATIVE LIBRARY','투자논지 라이브러리','반복되는 투자 서사를 고르고 → 해당 기업·VIC 아이디어를 클릭해 → 기업 설명, 당시 논지, 성공·실패 여부를 즉시 확인합니다.')

tags=rows('SELECT tag_ko,ideas FROM tag_summary ORDER BY ideas DESC')
st.dataframe([{'자동 논지태그':x['tag_ko'],'아이디어 수':x['ideas']} for x in tags],use_container_width=True,hide_index=True,height=300)
tag=st.selectbox('태그를 선택해 사례 보기',[x['tag_ko'] for x in tags])
data=rows('''SELECT idea_id,date,ticker,company_name,author,direction_ko,idea_type_ko,narrative_tags_ko
             FROM ideas_master WHERE narrative_tags_ko LIKE ? ORDER BY date DESC LIMIT 500''',(f'%"{tag}"%',))

st.subheader(f'{tag} · 사례')
st.caption('아래 행을 클릭하면 기업 설명·투자논지·성공/실패 분석이 팝업으로 열립니다.')
table=[{
    '게시일':x['date'][:10], '티커':x['ticker'], '기업':x['company_name'], '작성자':x['author'],
    '방향':x['direction_ko'], '유형':x['idea_type_ko'],
    '동시 태그':', '.join(json.loads(x['narrative_tags_ko']))
} for x in data]
event=st.dataframe(table,use_container_width=True,hide_index=True,height=560,
                   on_select='rerun',selection_mode='single-row',key=f'narrative_{tag}')
sel=event.selection.rows if event and hasattr(event,'selection') else []
if sel:
    idea_quick_view(data[sel[0]]['idea_id'])

st.warning('자동 논지태그와 예비 성공·실패 판정은 탐색용입니다. 외부 사후자료 검증이 끝난 항목만 최종 판정으로 승격합니다.')
