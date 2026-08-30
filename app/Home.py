import streamlit as st
from components.ui import apply_css, page_header, pills
from components.db import rows

st.set_page_config(page_title='VIC 허구 반증 연구소', page_icon='◈', layout='wide', initial_sidebar_state='expanded')
apply_css()
page_header('VIC FALSIFICATION LAB', 'VIC 허구 반증 연구소', 'VIC 13,656개 아이디어를 성공·실패 패턴으로 묶고, 각 기업에서 어떤 가정이 맞고 무엇이 깨졌는지 추적하는 투자 사례 연구 DB입니다.')

stats = {x['metric_ko']: x for x in rows('SELECT * FROM dataset_stats')}
c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric('전체 아이디어', stats['전체 아이디어']['value_text'])
c2.metric('롱', stats['롱 아이디어']['value_text'])
c3.metric('숏', stats['숏 아이디어']['value_text'])
c4.metric('Contest Winner', stats['Contest Winner']['value_text'])
c5.metric('본문 보유', stats['본문 보유']['value_text'])
c6.metric('기존 성과데이터', stats['기존 성과데이터 보유']['value_text'])

st.markdown('---')
st.subheader('패턴부터 탐색')
a,b=st.columns(2)
with a:
    st.markdown('### 주요 성공 패턴 후보')
    s=rows('''SELECT p.pattern_id,p.pattern_name_ko,p.category_ko,s.matched_ideas,s.median_return
              FROM pattern_catalog p JOIN pattern_stats s USING(pattern_id)
              WHERE p.polarity_ko='성공' ORDER BY s.matched_ideas DESC LIMIT 6''')
    for x in s:
        r='—' if x['median_return'] is None else f"{x['median_return']:+.0%}"
        st.write(f"**{x['pattern_name_ko']}** · {x['matched_ideas']:,}건 · 중앙값 {r}")
with b:
    st.markdown('### 주요 실패 패턴 후보')
    f=rows('''SELECT p.pattern_id,p.pattern_name_ko,p.category_ko,s.matched_ideas,s.median_return
              FROM pattern_catalog p JOIN pattern_stats s USING(pattern_id)
              WHERE p.polarity_ko='실패' ORDER BY s.matched_ideas DESC LIMIT 6''')
    for x in f:
        r='—' if x['median_return'] is None else f"{x['median_return']:+.0%}"
        st.write(f"**{x['pattern_name_ko']}** · {x['matched_ideas']:,}건 · 중앙값 {r}")

if st.button('성공·실패 패턴 연구소 열기', type='primary'):
    st.switch_page('pages/3_실패_패턴_연구소.py')
st.caption('현재 패턴 수치는 당시 서사 태그와 방향조정 주가성과를 결합한 자동 후보입니다. 정밀 논지 판정과는 분리합니다.')

st.markdown('---')
left, right = st.columns([1.6, 1])
with left:
    st.subheader('아이디어 탐색')
    q = st.text_input('회사명·티커·작성자', placeholder='예: PGR, Progressive, author')
    ys = [x['year'] for x in rows('SELECT DISTINCT year FROM ideas_master WHERE year IS NOT NULL ORDER BY year')]
    a,b,c = st.columns([2,1,1])
    with a: yr = st.select_slider('연도 범위', options=ys, value=(min(ys), max(ys)))
    with b: direction = st.selectbox('방향', ['전체','롱','숏'])
    with c: winner = st.checkbox('Contest Winner만')
    sql = '''SELECT idea_id,date,ticker,company_name,author,direction_ko,contest_winner,idea_type_ko,analysis_status_ko
             FROM ideas_master JOIN analysis USING(idea_id) WHERE year BETWEEN ? AND ?'''
    ps = [yr[0], yr[1]]
    if q:
        sql += ' AND (ticker LIKE ? OR company_name LIKE ? OR author LIKE ?)'; ps += [f'%{q}%'] * 3
    if direction != '전체':
        sql += ' AND direction_ko=?'; ps.append(direction)
    if winner:
        sql += ' AND contest_winner=1'
    sql += ' ORDER BY date DESC LIMIT 300'
    data = rows(sql, ps)
    st.dataframe([{
        '게시일': x['date'][:10] if x['date'] else '', '티커': x['ticker'], '기업': x['company_name'],
        '방향': x['direction_ko'], '작성자': x['author'], '유형': x['idea_type_ko'], '분석상태': x['analysis_status_ko']
    } for x in data], use_container_width=True, hide_index=True, height=430)
with right:
    st.subheader('이 DB에서 보는 순서')
    st.markdown('''**성공·실패 패턴**  
↓  
**해당 기업·VIC 아이디어**  
↓  
**당시 투자논지와 핵심 가정**  
↓  
**어떤 부분이 성공/실패했는가**  
↓  
**최초 반증 신호**  
↓  
**Failure Anatomy / 반증 질문**''')
    st.subheader('상위 자동 논지 태그')
    tg = rows('SELECT tag_ko,ideas FROM tag_summary ORDER BY ideas DESC LIMIT 10')
    pills([f"{x['tag_ko']} · {x['ideas']:,}" for x in tg])
