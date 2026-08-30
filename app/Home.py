import streamlit as st
from components.ui import apply_css, page_header, pills
from components.db import rows

st.set_page_config(page_title='VIC 허구 반증 연구소', page_icon='◈', layout='wide', initial_sidebar_state='expanded')
apply_css()
page_header('VIC FALSIFICATION LAB', 'VIC 허구 반증 연구소', '과거 투자자가 무엇을 믿었는지, 그 믿음이 언제·어떤 데이터로 깨졌는지, 그리고 주가 결과와 별개로 투자논지가 실제로 맞았는지를 추적합니다.')

stats = {x['metric_ko']: x for x in rows('SELECT * FROM dataset_stats')}
c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric('전체 아이디어', stats['전체 아이디어']['value_text'])
c2.metric('롱', stats['롱 아이디어']['value_text'])
c3.metric('숏', stats['숏 아이디어']['value_text'])
c4.metric('Contest Winner', stats['Contest Winner']['value_text'])
c5.metric('본문 보유', stats['본문 보유']['value_text'])
c6.metric('기존 성과데이터', stats['기존 성과데이터 보유']['value_text'])

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
    } for x in data], use_container_width=True, hide_index=True, height=480)
with right:
    st.subheader('데이터 구조')
    st.markdown('''**원본 투자 아이디어**  
↓  
**검증 가능한 Claim**  
↓  
**핵심 가정 / Falsifier**  
↓  
**최초 반증 신호**  
↓  
**투자논지 시점·이벤트 시점·현재**  
↓  
**실패 메커니즘 / 근본 분석 오류**''')
    st.caption('주가 수익률은 결과의 한 축일 뿐, 투자논지의 정답으로 취급하지 않습니다.')
    st.subheader('상위 자동 논지 태그')
    tg = rows('SELECT tag_ko,ideas FROM tag_summary ORDER BY ideas DESC LIMIT 12')
    pills([f"{x['tag_ko']} · {x['ideas']:,}" for x in tg])
    st.warning('자동 태그는 영어 원문 키워드 기반 초벌 분류입니다. 정밀 분석 결과와 분리되어 있습니다.')
