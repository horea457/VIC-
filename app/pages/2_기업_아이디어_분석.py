import json
import streamlit as st
from components.ui import apply_css, page_header, pills, empty_analysis
from components.db import rows, row

st.set_page_config(page_title='기업·아이디어 분석', layout='wide')
apply_css()
page_header('RESEARCH TERMINAL', '기업·아이디어 분석', '기업이 무엇을 하는지 → 당시 투자논지 → 핵심 가정 → 실제 전개 → 성공·실패 판정 → 실패 해부 순서로 읽습니다.')
q = st.text_input('티커 또는 기업명', placeholder='예: PGR')
if not q:
    st.info('기업이나 티커를 검색하세요.'); st.stop()
ideas = rows('SELECT * FROM ideas_master WHERE ticker LIKE ? OR company_name LIKE ? ORDER BY date DESC LIMIT 100', (f'%{q}%',f'%{q}%'))
if not ideas:
    st.warning('검색 결과가 없습니다.'); st.stop()
labels = [f"{x['date'][:10]} · {x['ticker']} · {x['direction_ko']} · {x['author']}" for x in ideas]
idx = st.selectbox('VIC 아이디어 선택', range(len(ideas)), format_func=lambda i: labels[i])
I = ideas[idx]
A = row('SELECT * FROM analysis WHERE idea_id=?',(I['idea_id'],))

st.header(f"{I['company_name'] or I['ticker']}  ·  {I['ticker']}")
pills(json.loads(I['narrative_tags_ko'] or '[]'))
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric('게시일',I['date'][:10]); m2.metric('방향',I['direction_ko']); m3.metric('유형',I['idea_type_ko']); m4.metric('예상기간',I['horizon_raw'] or '미추출'); m5.metric('분석상태',A['analysis_status_ko'])

T = st.tabs(['① 기업 설명','② 당시 투자논지','③ 논지 검증','④ 성공·실패','⑤ 실패 해부','⑥ 반증 질문'])
with T[0]:
    st.subheader('회사는 무엇을 하는가')
    if A['company_description_ko']: st.write(A['company_description_ko'])
    else: empty_analysis()
    st.subheader('사업모델'); st.write(A['business_model_ko'] or '분석 대기')
    st.subheader('산업구조와 경쟁역학'); st.write(A['industry_structure_ko'] or '분석 대기')
with T[1]:
    st.subheader('당시 투자논지 요약'); st.write(A['thesis_summary_ko'] or '분석 대기')
    st.subheader('핵심 가정'); st.write(A['key_assumptions_ko'] or '분석 대기')
    st.subheader('예상 Catalyst'); st.write(A['catalyst_expected_ko'] or f"원 데이터 기준 1차 유형: {I['idea_type_ko']}")
with T[2]:
    st.subheader('무엇이 이 논지를 반증할 수 있었나'); st.write(A['falsifiers_ko'] or '분석 대기')
    st.subheader('실제 전개'); st.write(A['actual_development_ko'] or '분석 대기')
    st.subheader('최초 반증 신호'); st.write(A['first_contradictory_signal_ko'] or '분석 대기')
with T[3]:
    st.subheader('결과를 한 덩어리로 보지 않습니다')
    st.dataframe([
        {'평가축':'투자논지 시점','판정':A['outcome_thesis_ko'] or '미검증'},
        {'평가축':'사업 결과','판정':A['outcome_business_ko'] or '미검증'},
        {'평가축':'Catalyst/Event','판정':A['catalyst_outcome_ko'] or '미검증'},
        {'평가축':'밸류에이션','판정':A['outcome_valuation_ko'] or '미검증'},
        {'평가축':'주가 결과','판정':A['outcome_stock_ko'] or '미검증'},
        {'평가축':'현재','판정':A['outcome_current_ko'] or '미검증'},
        {'평가축':'종합','판정':A['overall_verdict_ko'] or '미검증'},
    ], use_container_width=True, hide_index=True)
    vals=[]
    for lab,k in [('1Y','idea_return_1y'),('3Y','idea_return_3y'),('5Y','idea_return_5y')]:
        vals.append(f"{lab} {I[k]:.1%}" if I[k] is not None else f"{lab} 없음")
    st.caption('원 데이터 방향조정 수익률: ' + ' · '.join(vals))
with T[4]:
    st.subheader('Failure Anatomy')
    st.dataframe([
        {'층위':'실패 영역','내용':A['failure_domain_ko'] or '미분석'},
        {'층위':'실패 메커니즘','내용':A['failure_mechanism_ko'] or '미분석'},
        {'층위':'근본 분석 오류','내용':A['root_analytical_error_ko'] or '미분석'},
        {'층위':'전달 경로','내용':A['transmission_mechanism_ko'] or '미분석'},
        {'층위':'당시 알 수 있었나','내용':A['knowable_at_t0_ko'] or '미분석'},
        {'층위':'피할 수 있었나','내용':A['avoidability_ko'] or '미분석'},
    ], use_container_width=True, hide_index=True)
with T[5]:
    st.subheader('당시 이 질문 하나를 했더라면?')
    st.info(A['counterfactual_question_ko'] or '정밀 분석 후 가장 중요한 반증 질문을 저장합니다.')
    st.subheader('검증 가능한 Claim')
    C = rows('SELECT * FROM claims WHERE idea_id=? ORDER BY claim_order',(I['idea_id'],))
    if C: st.dataframe(C,use_container_width=True,hide_index=True)
    else: empty_analysis()
