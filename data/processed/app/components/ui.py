import json
import streamlit as st

CSS = """
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 3rem; max-width: 1500px;}
[data-testid="stSidebar"] {border-right: 1px solid rgba(128,128,128,.18);}
.vic-eyebrow {font-size:.78rem; letter-spacing:.08em; text-transform:uppercase; opacity:.62; margin-bottom:.2rem;}
.vic-title {font-size:2.05rem; font-weight:760; line-height:1.14; margin:0 0 .35rem 0;}
.vic-subtitle {font-size:.98rem; opacity:.68; max-width:960px; line-height:1.55; margin-bottom:1.25rem;}
.vic-pill {display:inline-block; border:1px solid rgba(128,128,128,.25); border-radius:999px; padding:.14rem .5rem; margin:.08rem .12rem .08rem 0; font-size:.77rem;}
.verified-pill {display:inline-block; border-radius:999px; padding:.22rem .62rem; font-size:.78rem; font-weight:720; background:rgba(46,160,67,.12); border:1px solid rgba(46,160,67,.34); margin-bottom:.45rem;}
.auto-pill {display:inline-block; border-radius:999px; padding:.22rem .62rem; font-size:.78rem; background:rgba(128,128,128,.08); border:1px solid rgba(128,128,128,.22); margin-bottom:.45rem;}
.quick-note {font-size:.82rem; opacity:.68; margin:.15rem 0 .7rem 0;}
.quick-section {font-size:1.05rem; font-weight:740; margin-top:.85rem; margin-bottom:.3rem;}
.quick-box {border:1px solid rgba(128,128,128,.18); border-radius:12px; padding:.75rem .9rem; margin:.25rem 0 .6rem 0; background:rgba(128,128,128,.025);}
.verdict-success {font-weight:740;}
hr {margin:1.15rem 0 1rem 0 !important;}
</style>
"""

CSS_PATTERN = """
<style>
.pattern-card {border:1px solid rgba(128,128,128,.22); border-radius:14px; padding:14px 15px 12px 15px; min-height:172px; margin-bottom:8px; background:rgba(128,128,128,.035);}
.pattern-kicker {font-size:.72rem; text-transform:uppercase; letter-spacing:.06em; opacity:.58; margin-bottom:.35rem;}
.pattern-name {font-size:1.03rem; font-weight:720; line-height:1.28; margin-bottom:.38rem;}
.pattern-meta {font-size:.76rem; opacity:.66; margin-bottom:.52rem;}
.pattern-desc {font-size:.83rem; opacity:.78; line-height:1.45;}
</style>
"""


def apply_css():
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(CSS_PATTERN, unsafe_allow_html=True)


def page_header(kicker, title, subtitle):
    st.markdown(
        f'<div class="vic-eyebrow">{kicker}</div>'
        f'<div class="vic-title">{title}</div>'
        f'<div class="vic-subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )


def pills(items):
    if not items:
        return
    html = ''.join(f'<span class="vic-pill">{x}</span>' for x in items)
    st.markdown(html, unsafe_allow_html=True)


def empty_analysis():
    st.info('이 항목은 아직 정밀 검증 전입니다. 자동 1차 태그와 원본 메타데이터는 탐색용이며, 성공·실패 최종 판정으로 사용하지 않습니다.')


def _fmt_return(v):
    return '—' if v is None else f'{v:+.1%}'


def _verified_badge(P):
    st.markdown('<span class="verified-pill">✓ 사후분석 완료 · 외부 자료 검증</span>', unsafe_allow_html=True)
    st.caption(f"분석 기준일 {P.get('research_asof') or '—'} · 신뢰도 {P.get('confidence',0):.0%}")


def render_verified_postmortem(idea_id: str, compact: bool = False):
    """검증 완료 아이디어의 사후분석을 렌더링. 완료 건이 아니면 False 반환."""
    from components.db import row, rows

    I = row('SELECT * FROM ideas_master WHERE idea_id=?', (idea_id,))
    P = row('SELECT * FROM postmortems WHERE idea_id=?', (idea_id,))
    if not I or not P:
        return False

    claims = rows('''
        SELECT claim_order,claim_type_ko,original_claim_ko,key_assumption_ko,
               actual_result_ko,verdict_ko,explanation_ko
        FROM postmortem_claims WHERE idea_id=? ORDER BY claim_order
    ''', (idea_id,))
    sources = rows('''
        SELECT source_order,title_ko,publisher,source_date,url,evidence_ko
        FROM postmortem_sources WHERE idea_id=? ORDER BY source_order
    ''', (idea_id,))
    vpats = rows('''
        SELECT p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,p.counterfactual_question_ko
        FROM verified_pattern_map m JOIN verified_pattern_catalog p USING(pattern_id)
        WHERE m.idea_id=? ORDER BY m.is_primary DESC,p.pattern_name_ko
    ''', (idea_id,))

    _verified_badge(P)
    st.markdown(f"## {I.get('company_name') or I.get('ticker')} · {I.get('ticker') or '—'}")
    pills([
        I.get('date','')[:10] if I.get('date') else '날짜 미상',
        f"실제 논지 방향 {P.get('research_direction_ko') or '미상'}",
        f"작성자 {I.get('author') or '미상'}",
        f"종합 {P.get('overall_verdict_ko') or '—'}",
    ])
    if I.get('direction_ko') and I.get('direction_ko') != P.get('research_direction_ko'):
        st.caption(f"※ 원 덤프의 Long/Short 메타데이터는 {I.get('direction_ko')}으로 저장돼 있으나, VIC 본문을 읽어 실제 논지 방향을 **{P.get('research_direction_ko')}**으로 교정했습니다.")

    st.markdown('<div class="quick-section">1. 무슨 기업인가</div>', unsafe_allow_html=True)
    st.write(P.get('company_description_ko'))

    st.markdown('<div class="quick-section">2. 당시 VIC 투자논지는 무엇이었나</div>', unsafe_allow_html=True)
    st.write(P.get('original_thesis_ko'))

    st.markdown('<div class="quick-section">3. 실제로 이후 무슨 일이 일어났나</div>', unsafe_allow_html=True)
    st.write(P.get('actual_development_ko'))

    st.markdown('<div class="quick-section">4. 투자논지는 어디서 맞고 어디서 틀렸나</div>', unsafe_allow_html=True)
    outcome_table = [
        {'평가축':'핵심 투자논지', '판정':P.get('thesis_verdict_ko') or '—'},
        {'평가축':'사업/산업구조', '판정':P.get('business_verdict_ko') or '—'},
        {'평가축':'Catalyst/Event', '판정':P.get('catalyst_verdict_ko') or '—'},
        {'평가축':'밸류에이션', '판정':P.get('valuation_verdict_ko') or '—'},
        {'평가축':'주가 결과', '판정':P.get('stock_verdict_ko') or '—'},
        {'평가축':'현재 상태', '판정':P.get('current_verdict_ko') or '—'},
        {'평가축':'종합', '판정':P.get('overall_verdict_ko') or '—'},
    ]
    st.dataframe(outcome_table, use_container_width=True, hide_index=True, height=282)

    c1,c2,c3 = st.columns(3)
    c1.metric('1년 수익률¹', _fmt_return(P.get('corrected_return_1y')))
    c2.metric('3년 수익률¹', _fmt_return(P.get('corrected_return_3y')))
    c3.metric('5년 수익률¹', _fmt_return(P.get('corrected_return_5y')))
    st.caption('¹ 원 VIC 성과 데이터가 존재하는 경우에만 표시하며, 본문에서 교정한 실제 Long/Short 방향을 적용했습니다.')

    st.markdown('**왜 이런 결과가 나왔나**')
    st.write(P.get('why_ko'))

    if claims:
        st.markdown('<div class="quick-section">5. Claim별 사후검증</div>', unsafe_allow_html=True)
        if compact:
            for c in claims:
                with st.expander(f"{c['verdict_ko']} · {c['claim_type_ko']} · {c['original_claim_ko']}"):
                    st.markdown(f"**당시 핵심 가정**  \n{c['key_assumption_ko']}")
                    st.markdown(f"**실제 결과**  \n{c['actual_result_ko']}")
                    st.markdown(f"**판단**  \n{c['explanation_ko']}")
        else:
            st.dataframe([{
                'Claim':c['original_claim_ko'], '가정':c['key_assumption_ko'],
                '실제 결과':c['actual_result_ko'], '판정':c['verdict_ko'], '해석':c['explanation_ko']
            } for c in claims], use_container_width=True, hide_index=True, height=min(520, 90+len(claims)*95))

    st.markdown('<div class="quick-section">6. 성공·실패 패턴과 반증 질문</div>', unsafe_allow_html=True)
    if vpats:
        for p in vpats:
            icon = '✅' if p['polarity_ko']=='성공' else ('⚠️' if p['polarity_ko']=='실패' else '◐')
            st.markdown(f"**{icon} {p['pattern_name_ko']}** · {p['category_ko']}")
            st.write(p['definition_ko'])
    if P.get('failure_pattern_ko') and P.get('failure_pattern_ko') != '해당 없음':
        st.markdown(f"**실패/혼합 패턴:** {P.get('failure_pattern_ko')}")
        st.markdown(f"**근본 분석 오류:** {P.get('root_error_ko')}")
        st.markdown(f"**최초 반증 신호:** {P.get('first_signal_ko')} ({P.get('first_signal_date') or '시점 미상'})")
        st.markdown(f"**당시 알 수 있었나:** {P.get('knowable_at_t0_ko')} · **피할 수 있었나:** {P.get('avoidability_ko')}")

    st.info(f"**당시 이 질문 하나를 했더라면?**  \n\n{P.get('counterfactual_question_ko')}")
    if P.get('analyst_note_ko'):
        st.markdown('**사후분석 메모**')
        st.write(P.get('analyst_note_ko'))

    if sources:
        with st.expander(f"근거 자료 {len(sources)}개 보기"):
            for s in sources:
                st.markdown(f"**{s['source_order']}. {s['title_ko']}** · {s['publisher']} · {s['source_date']}")
                st.write(s['evidence_ko'])
                if s.get('url'):
                    st.markdown(f"[원문 자료 열기]({s['url']})")

    return True


@st.dialog('투자 아이디어 빠른 분석', width='large')
def idea_quick_view(idea_id: str):
    """테이블에서 아이디어를 선택했을 때 띄우는 미니 리서치 리포트."""
    from components.db import row, rows

    # 실제 사후분석 완료 건은 자동 태그보다 우선한다.
    if render_verified_postmortem(idea_id, compact=True):
        if st.button('전체 상세 분석 페이지로 이동', type='primary', use_container_width=True):
            st.session_state['selected_idea_id'] = idea_id
            st.switch_page('pages/2_기업_아이디어_분석.py')
        return

    I = row('SELECT * FROM ideas_master WHERE idea_id=?', (idea_id,))
    A = row('SELECT * FROM analysis WHERE idea_id=?', (idea_id,))
    if not I:
        st.error('아이디어 데이터를 찾지 못했습니다.')
        return
    A = A or {}

    patterns = rows('''
        SELECT p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,
               p.counterfactual_question_ko,m.performance_horizon_ko,
               m.direction_adjusted_return,m.stock_verdict_ko,m.thesis_verdict_ko
        FROM idea_pattern_map m JOIN pattern_catalog p USING(pattern_id)
        WHERE m.idea_id=?
        ORDER BY CASE p.polarity_ko WHEN '실패' THEN 0 ELSE 1 END, p.pattern_name_ko
        LIMIT 8
    ''', (idea_id,))
    claims = rows('''
        SELECT claim_order,claim_type_ko,claim_ko,implicit_assumption_ko,
               falsifier_ko,leading_indicator_ko,outcome_ko,review_status_ko
        FROM claims WHERE idea_id=? ORDER BY claim_order LIMIT 5
    ''', (idea_id,))

    st.markdown('<span class="auto-pill">자동 예비분석 · 사후검증 전</span>', unsafe_allow_html=True)
    st.markdown(f"## {I.get('company_name') or I.get('ticker')} · {I.get('ticker') or '—'}")
    meta = [
        I.get('date', '')[:10] if I.get('date') else '날짜 미상',
        I.get('direction_ko') or '방향 미상',
        f"작성자 {I.get('author') or '미상'}",
        I.get('idea_type_ko') or '일반 아이디어',
    ]
    pills(meta)
    try:
        tags = json.loads(I.get('narrative_tags_ko') or '[]')
    except Exception:
        tags = []
    if tags:
        st.caption('자동 논지 태그 · ' + ' · '.join(tags[:8]))

    st.markdown('<div class="quick-section">1. 무슨 기업인가</div>', unsafe_allow_html=True)
    st.write(A.get('company_description_ko') or '기업 설명은 아직 외부자료 정밀 검증 전입니다.')

    st.markdown('<div class="quick-section">2. 당시 투자 논지는 무엇이었나</div>', unsafe_allow_html=True)
    st.write(A.get('thesis_summary_ko') or '투자논지 요약 대기')

    st.markdown('<div class="quick-section">3. 자동 스크리닝 결과</div>', unsafe_allow_html=True)
    outcome_table = [
        {'평가축':'핵심 투자논지', '판정':A.get('outcome_thesis_ko') or '미검증'},
        {'평가축':'사업/산업구조', '판정':A.get('outcome_business_ko') or '미검증'},
        {'평가축':'Catalyst/Event', '판정':A.get('catalyst_outcome_ko') or '미검증'},
        {'평가축':'밸류에이션', '판정':A.get('outcome_valuation_ko') or '미검증'},
        {'평가축':'주가 결과', '판정':A.get('outcome_stock_ko') or '미검증'},
        {'평가축':'현재 상태', '판정':A.get('outcome_current_ko') or '미검증'},
        {'평가축':'종합', '판정':A.get('overall_verdict_ko') or '미검증'},
    ]
    st.dataframe(outcome_table, use_container_width=True, hide_index=True, height=282)

    c1,c2,c3 = st.columns(3)
    c1.metric('1년 방향조정 수익률', _fmt_return(I.get('idea_return_1y')))
    c2.metric('3년 방향조정 수익률', _fmt_return(I.get('idea_return_3y')))
    c3.metric('5년 방향조정 수익률', _fmt_return(I.get('idea_return_5y')))

    if patterns:
        st.markdown('<div class="quick-section">4. 자동 성공·실패 패턴 후보</div>', unsafe_allow_html=True)
        for p in patterns:
            icon = '✅' if p['polarity_ko'] == '성공' else '⚠️'
            st.markdown(f"**{icon} {p['pattern_name_ko']}** · {p['category_ko']}")
            st.caption(p['definition_ko'])

    if claims:
        st.markdown('<div class="quick-section">5. 자동 Claim과 반증 조건</div>', unsafe_allow_html=True)
        for c in claims[:3]:
            with st.expander(f"Claim {c['claim_order']} · {c['claim_type_ko']} · {c['outcome_ko'] or '미검증'}"):
                st.markdown(f"**주장**  \n{c['claim_ko'] or '—'}")
                st.markdown(f"**암묵적 가정**  \n{c['implicit_assumption_ko'] or '—'}")
                st.markdown(f"**반증 조건**  \n{c['falsifier_ko'] or '—'}")
                st.markdown(f"**먼저 볼 지표**  \n{c['leading_indicator_ko'] or '—'}")

    st.warning('이 건은 아직 외부 사후자료로 검증하지 않았습니다. 위 내용은 VIC 원문과 제한적 주가 데이터로 만든 탐색용 자동 분석입니다.')

    if st.button('전체 상세 분석 페이지로 이동', type='primary', use_container_width=True):
        st.session_state['selected_idea_id'] = idea_id
        st.switch_page('pages/2_기업_아이디어_분석.py')
