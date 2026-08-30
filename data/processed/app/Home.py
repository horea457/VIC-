import streamlit as st
from components.ui import apply_css, page_header, pills, idea_quick_view
from components.db import rows

st.set_page_config(page_title='VIC 허구 반증 연구소', page_icon='◈', layout='wide', initial_sidebar_state='expanded')
apply_css()
page_header('VIC FALSIFICATION LAB', 'VIC 허구 반증 연구소', 'VIC 13,656개 아이디어를 탐색하고, 사후검증 완료 사례에서는 당시 Claim과 실제 결과를 분리해 무엇이 맞고 무엇이 깨졌는지 추적합니다.')

stats = {x['metric_ko']: x for x in rows('SELECT * FROM dataset_stats')}
verified_n = rows('SELECT COUNT(*) AS n FROM postmortems')[0]['n']
verified_claims = rows('SELECT COUNT(*) AS n FROM postmortem_claims')[0]['n']
c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric('전체 아이디어', stats['전체 아이디어']['value_text'])
c2.metric('사후분석 완료', f'{verified_n:,}건')
c3.metric('검증 Claim', f'{verified_claims:,}개')
c4.metric('Contest Winner', stats['Contest Winner']['value_text'])
c5.metric('본문 보유', stats['본문 보유']['value_text'])
c6.metric('기존 성과데이터', stats['기존 성과데이터 보유']['value_text'])

st.markdown('---')
st.subheader('✓ 실제 사후검증 패턴부터 탐색')
st.caption('아래는 자동 키워드 분류가 아니라 VIC 원문과 후속 기업 공시·SEC·IR 자료를 대조해 사후분석한 사례군입니다.')
vp=rows('''SELECT p.pattern_id,p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,COUNT(m.idea_id) n
           FROM verified_pattern_catalog p LEFT JOIN verified_pattern_map m USING(pattern_id)
           GROUP BY p.pattern_id ORDER BY n DESC,p.polarity_ko,p.pattern_name_ko LIMIT 12''')
cols=st.columns(3)
for i,x in enumerate(vp):
    with cols[i%3]:
        icon='✅' if x['polarity_ko']=='성공' else ('⚠️' if x['polarity_ko']=='실패' else '◐')
        st.markdown(f"**{icon} {x['pattern_name_ko']}**  \n{x['category_ko']} · 검증 {x['n']}건")
        st.caption(x['definition_ko'])
if st.button('검증 완료 성공·실패 패턴 열기', type='primary'):
    st.switch_page('pages/3_실패_패턴_연구소.py')
if st.button('사후분석 완료 기업만 보기'):
    st.switch_page('pages/8_사후분석_완료.py')

st.markdown('---')
left, right = st.columns([1.6, 1])
with left:
    st.subheader('전체 VIC 아이디어 탐색')
    q = st.text_input('회사명·티커·작성자', placeholder='예: PGR, Progressive, author')
    ys = [x['year'] for x in rows('SELECT DISTINCT year FROM ideas_master WHERE year IS NOT NULL ORDER BY year')]
    a,b,c = st.columns([2,1,1])
    with a: yr = st.select_slider('연도 범위', options=ys, value=(min(ys), max(ys)))
    with b: direction = st.selectbox('방향(원 DB)', ['전체','롱','숏'])
    with c: verified_only = st.checkbox('사후분석 완료만')
    sql = '''SELECT i.idea_id,i.date,i.ticker,i.company_name,i.author,i.direction_ko,i.idea_type_ko,
                    a.analysis_status_ko,p.research_direction_ko,p.overall_verdict_ko
             FROM ideas_master i JOIN analysis a USING(idea_id)
             LEFT JOIN postmortems p ON p.idea_id=i.idea_id
             WHERE i.year BETWEEN ? AND ?'''
    ps = [yr[0], yr[1]]
    if q:
        sql += ' AND (i.ticker LIKE ? OR i.company_name LIKE ? OR i.author LIKE ?)'; ps += [f'%{q}%'] * 3
    if direction != '전체':
        sql += ' AND i.direction_ko=?'; ps.append(direction)
    if verified_only:
        sql += ' AND p.idea_id IS NOT NULL'
    sql += ' ORDER BY CASE WHEN p.idea_id IS NOT NULL THEN 0 ELSE 1 END,i.date DESC LIMIT 300'
    data = rows(sql, ps)
    st.caption('행을 클릭하면 사후분석 완료 건은 실제 검증 리포트, 나머지는 자동 예비분석 팝업이 열립니다.')
    home_table=[{
        '게시일': x['date'][:10] if x['date'] else '', '티커': x['ticker'], '기업': x['company_name'],
        '실제 논지방향': x['research_direction_ko'] or x['direction_ko'], '작성자': x['author'],
        '분석상태': x['analysis_status_ko'], '종합판정':x['overall_verdict_ko'] or '미검증'
    } for x in data]
    home_event=st.dataframe(home_table, use_container_width=True, hide_index=True, height=430,
                            on_select='rerun', selection_mode='single-row', key='home_idea_table')
    home_sel=home_event.selection.rows if home_event and hasattr(home_event,'selection') else []
    if home_sel:
        idea_quick_view(data[home_sel[0]]['idea_id'])
with right:
    st.subheader('이 DB에서 보는 순서')
    st.markdown('''**검증된 성공·실패 패턴**  
↓  
**해당 기업·VIC 아이디어**  
↓  
**당시 투자논지와 핵심 가정**  
↓  
**후속 공시로 실제 전개 확인**  
↓  
**Claim별 성공/실패**  
↓  
**최초 반증 신호 / 근본 오류**  
↓  
**현재 분석에 재사용할 질문**''')
    st.subheader('전체 corpus 자동 태그')
    tg = rows('SELECT tag_ko,ideas FROM tag_summary ORDER BY ideas DESC LIMIT 10')
    pills([f"{x['tag_ko']} · {x['ideas']:,}" for x in tg])
    st.caption('자동 태그는 13,656개 전체를 훑기 위한 탐색 레이어이며, 사후분석 완료 판정과 분리합니다.')
