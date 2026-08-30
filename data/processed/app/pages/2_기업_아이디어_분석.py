import json
import streamlit as st
from components.ui import apply_css, page_header, pills, empty_analysis, render_verified_postmortem
from components.db import rows, row

st.set_page_config(page_title='기업·아이디어 분석', layout='wide')
apply_css()
page_header('RESEARCH TERMINAL', '기업·아이디어 분석', '기업이 무엇을 하는지 → 당시 투자논지 → 무엇이 맞고 틀렸는지 → 성공·실패 메커니즘 → 반증 질문 순서로 읽습니다.')

selected_id = st.session_state.get('selected_idea_id')
I = row('SELECT * FROM ideas_master WHERE idea_id=?',(selected_id,)) if selected_id else None

if I:
    top1,top2=st.columns([1,5])
    with top1:
        if st.button('다른 기업 검색', use_container_width=True):
            st.session_state.pop('selected_idea_id',None)
            st.session_state.pop('selected_pattern_context',None)
            st.rerun()
    with top2:
        st.caption('패턴 페이지나 아이디어 탐색에서 선택한 아이디어를 보고 있습니다.')
else:
    q = st.text_input('티커 또는 기업명', placeholder='예: PGR')
    if not q:
        st.info('기업이나 티커를 검색하세요.'); st.stop()
    ideas = rows('SELECT * FROM ideas_master WHERE ticker LIKE ? OR company_name LIKE ? ORDER BY date DESC LIMIT 100', (f'%{q}%',f'%{q}%'))
    if not ideas:
        st.warning('검색 결과가 없습니다.'); st.stop()
    labels = [f"{x['date'][:10]} · {x['ticker']} · {x['direction_ko']} · {x['author']}" for x in ideas]
    idx = st.selectbox('VIC 아이디어 선택', range(len(ideas)), format_func=lambda i: labels[i])
    I = ideas[idx]

P_verified = row('SELECT * FROM postmortems WHERE idea_id=?',(I['idea_id'],))
if P_verified:
    st.success('이 아이디어는 외부 공시·SEC·IR 자료까지 대조한 **사후분석 완료** 사례입니다. 아래 내용은 자동 태그보다 우선합니다.')
    render_verified_postmortem(I['idea_id'], compact=False)
    with st.expander('자동 탐색 레이어도 같이 보기'):
        auto_patterns = rows('''SELECT p.polarity_ko,p.category_ko,p.pattern_name_ko,m.performance_horizon_ko,m.direction_adjusted_return
                                FROM idea_pattern_map m JOIN pattern_catalog p USING(pattern_id)
                                WHERE m.idea_id=? ORDER BY p.polarity_ko,p.pattern_name_ko''',(I['idea_id'],))
        if auto_patterns:
            st.dataframe(auto_patterns,use_container_width=True,hide_index=True)
        else:
            st.caption('자동 패턴 후보 없음')
    st.stop()

A = row('SELECT * FROM analysis WHERE idea_id=?',(I['idea_id'],))
patterns = rows('''SELECT p.pattern_id,p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,
                          p.counterfactual_question_ko,m.performance_horizon_ko,m.direction_adjusted_return,
                          m.stock_verdict_ko,m.match_type_ko,m.thesis_verdict_ko
                   FROM idea_pattern_map m JOIN pattern_catalog p USING(pattern_id)
                   WHERE m.idea_id=? ORDER BY p.polarity_ko DESC,p.pattern_name_ko''',(I['idea_id'],))

st.header(f"{I['company_name'] or I['ticker']}  ·  {I['ticker']}")
pills(json.loads(I['narrative_tags_ko'] or '[]'))
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric('게시일',I['date'][:10]); m2.metric('방향',I['direction_ko']); m3.metric('유형',I['idea_type_ko']); m4.metric('예상기간',I['horizon_raw'] or '미추출'); m5.metric('분석상태',A['analysis_status_ko'])

if patterns:
    st.subheader('현재 연결된 성공·실패 패턴 후보')
    for p in patterns:
        icon='✓' if p['polarity_ko']=='성공' else '⚠'
        ret='—' if p['direction_adjusted_return'] is None else f"{p['direction_adjusted_return']:+.1%}"
        st.markdown(f"**{icon} {p['pattern_name_ko']}**  ·  {p['match_type_ko']}  ·  {p['performance_horizon_ko']} 방향조정 수익률 {ret}")
        st.caption(p['definition_ko'])
    st.caption('위 패턴은 현재 자동 후보입니다. 정밀 분석이 완료되면 투자논지 성공·실패 판정과 분리해 표시됩니다.')

T = st.tabs(['① 기업 설명','② 당시 투자논지','③ 성공·실패 분해','④ 논지 검증','⑤ 실패 해부','⑥ 반증 질문'])
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
    st.subheader('어떤 부분에서 성공·실패했나')
    outcome_rows=[
        {'평가축':'사업모델/산업구조','판정':A['outcome_business_ko'] or '미검증','무엇을 보는가':'수요·경쟁·해자·수익풀의 실제 전개'},
        {'평가축':'핵심 투자논지','판정':A['outcome_thesis_ko'] or '미검증','무엇을 보는가':'원래 Claim이 예상기간 내 실제로 성립했는가'},
        {'평가축':'Catalyst/Event','판정':A['catalyst_outcome_ko'] or '미검증','무엇을 보는가':'이벤트 발생·시점·조건이 예상과 같았는가'},
        {'평가축':'밸류에이션','판정':A['outcome_valuation_ko'] or '미검증','무엇을 보는가':'저평가 해소·멀티플 정상화 가정이 타당했는가'},
        {'평가축':'주가 결과','판정':A['outcome_stock_ko'] or '자동 성과만 존재','무엇을 보는가':'논지와 별개로 실제 투자수익이 어땠는가'},
        {'평가축':'현재 상태','판정':A['outcome_current_ko'] or '미검증','무엇을 보는가':'장기적으로 경쟁력과 thesis가 어떻게 변했는가'},
        {'평가축':'종합','판정':A['overall_verdict_ko'] or '미검증','무엇을 보는가':'주가와 논지를 분리한 최종 판단'},
    ]
    st.dataframe(outcome_rows,use_container_width=True,hide_index=True)
    r1,r3,r5=I['idea_return_1y'],I['idea_return_3y'],I['idea_return_5y']
    cc=st.columns(3)
    cc[0].metric('1년 방향조정 수익률','—' if r1 is None else f'{r1:+.1%}')
    cc[1].metric('3년 방향조정 수익률','—' if r3 is None else f'{r3:+.1%}')
    cc[2].metric('5년 방향조정 수익률','—' if r5 is None else f'{r5:+.1%}')
    if patterns:
        st.subheader('패턴 관점의 예비 해석')
        for p in patterns:
            st.write(f"- **{p['pattern_name_ko']}**: {p['stock_verdict_ko']} / 논지 판정은 {p['thesis_verdict_ko']}")

with T[3]:
    st.subheader('무엇이 이 논지를 반증할 수 있었나'); st.write(A['falsifiers_ko'] or '분석 대기')
    st.subheader('실제 전개'); st.write(A['actual_development_ko'] or '분석 대기')
    st.subheader('최초 반증 신호'); st.write(A['first_contradictory_signal_ko'] or '분석 대기')
    C = rows('SELECT * FROM claims WHERE idea_id=? ORDER BY claim_order',(I['idea_id'],))
    st.subheader('검증 가능한 Claim')
    if C:
        claim_table=[{
            '순서':x['claim_order'],'유형':x['claim_type_ko'],'핵심 주장':x['claim_ko'],
            '암묵적 가정':x['implicit_assumption_ko'],'반증 조건':x['falsifier_ko'],'선행지표':x['leading_indicator_ko'],
            '예비 결과':x['outcome_ko'] or '미검증','검증상태':x['review_status_ko']
        } for x in C]
        st.dataframe(claim_table,use_container_width=True,hide_index=True,height=min(460,95+len(claim_table)*58))
        with st.expander('VIC 원문 근거 보기 (영문 원문)'):
            for x in C:
                st.markdown(f"**Claim {x['claim_order']} · {x['claim_type_ko']}**")
                st.write(x.get('source_excerpt_en') or '원문 근거 문장 미추출')
    else: empty_analysis()

with T[4]:
    st.subheader('Failure Anatomy')
    st.dataframe([
        {'층위':'표면적 결과','내용':A['actual_development_ko'] or '미분석'},
        {'층위':'실패 영역','내용':A['failure_domain_ko'] or '미분석'},
        {'층위':'실패 메커니즘','내용':A['failure_mechanism_ko'] or '미분석'},
        {'층위':'2차 패턴','내용':A['secondary_failure_patterns_ko'] or '미분석'},
        {'층위':'근본 분석 오류','내용':A['root_analytical_error_ko'] or '미분석'},
        {'층위':'전달 경로','내용':A['transmission_mechanism_ko'] or '미분석'},
        {'층위':'최초 반증 신호','내용':A['first_contradictory_signal_ko'] or '미분석'},
        {'층위':'당시 알 수 있었나','내용':A['knowable_at_t0_ko'] or '미분석'},
        {'층위':'피할 수 있었나','내용':A['avoidability_ko'] or '미분석'},
    ], use_container_width=True, hide_index=True)

with T[5]:
    st.subheader('당시 이 질문 하나를 했더라면?')
    if A['counterfactual_question_ko']:
        st.info(A['counterfactual_question_ko'])
    elif patterns:
        for p in patterns:
            st.info(f"**{p['pattern_name_ko']}** → {p['counterfactual_question_ko']}")
    else:
        st.info('정밀 분석 후 가장 중요한 반증 질문을 저장합니다.')
    st.subheader('이 질문을 현재 기업 분석에 재사용')
    st.write('같은 패턴의 신규 기업을 볼 때, 과거 실패사례에서 도출된 질문을 체크리스트로 재사용하는 것이 이 DB의 최종 목적입니다.')
