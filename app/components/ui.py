import html
import json
import re
import streamlit as st

CSS = """
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 4rem; max-width: 1240px;}
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
.report-kicker {font-size:.78rem; font-weight:760; letter-spacing:.08em; color:#2563eb; margin-top:.2rem;}
.report-title {font-size:1.85rem; font-weight:780; line-height:1.2; margin:.15rem 0 .5rem 0;}
.section-number {font-size:.78rem; font-weight:760; color:#2563eb; letter-spacing:.06em; margin-top:1.9rem; margin-bottom:.15rem;}
.section-title {font-size:1.42rem; font-weight:780; line-height:1.3; margin-bottom:.75rem;}
.thesis-card {border-left:4px solid #2563eb; border-radius:8px; padding:.85rem 1rem; margin:.45rem 0 .8rem 0; background:rgba(37,99,235,.055); line-height:1.65;}
.result-card {border-left:4px solid #d97706; border-radius:8px; padding:.85rem 1rem; margin:.45rem 0 .8rem 0; background:rgba(217,119,6,.055); line-height:1.65;}
.lesson-card {border:1px solid rgba(37,99,235,.25); border-radius:12px; padding:.9rem 1rem; margin:.65rem 0; background:rgba(37,99,235,.035);}
.muted-label {font-size:.76rem; font-weight:740; opacity:.58; text-transform:uppercase; letter-spacing:.04em; margin-bottom:.22rem;}
hr {margin:1.15rem 0 1rem 0 !important;}
</style>
"""


def _literal_dollars(value):
    """Keep financial dollar figures out of Streamlit's inline-LaTeX parser."""
    if value is None:
        return value
    return re.sub(r'(?<!\\)\$', r'\\$', str(value))

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



def _render_deep_postmortem(I, P, D):
    from components.db import rows
    idea_id = I['idea_id']
    sections = rows('SELECT section_order,section_title_ko,section_body_ko FROM deep_analysis_sections WHERE idea_id=? ORDER BY section_order', (idea_id,))
    claims = rows('''
        SELECT claim_order,claim_title_ko,thesis_weight_pct,original_claim_ko,t0_evidence_ko,key_assumption_ko,
               ex_ante_falsifier_ko,actual_result_ko,quantitative_gap_ko,verdict_ko,analytical_error_ko,reusable_lesson_ko
        FROM deep_analysis_claims WHERE idea_id=? ORDER BY claim_order
    ''', (idea_id,))
    metrics = rows('''
        SELECT metric_order,metric_name_ko,t0_value_ko,thesis_expectation_ko,actual_value_ko,verdict_ko,interpretation_ko
        FROM deep_analysis_metrics WHERE idea_id=? ORDER BY metric_order
    ''', (idea_id,))
    timeline = rows('SELECT event_order,event_date_ko,event_ko,thesis_implication_ko FROM deep_analysis_timeline WHERE idea_id=? ORDER BY event_order', (idea_id,))
    sources = rows('SELECT source_order,source_type_ko,title_ko,publisher,source_date,url,evidence_ko FROM deep_analysis_sources WHERE idea_id=? ORDER BY source_order', (idea_id,))

    st.markdown('<span class="verified-pill">◆ 심층 사후분석 · 원문 산식 + 외부 primary source 검증</span>', unsafe_allow_html=True)
    st.caption(f"리포트 {D.get('report_version') or '—'} · 분석 기준일 {D.get('research_asof') or P.get('research_asof') or '—'} · 신뢰도 {P.get('confidence',0):.0%}")
    st.markdown(f"## {I.get('company_name') or I.get('ticker')} · {I.get('ticker') or '—'}")
    pills([I.get('date','')[:10] if I.get('date') else '날짜 미상', f"실제 논지 방향 {P.get('research_direction_ko') or '미상'}", f"작성자 {I.get('author') or '미상'}", D.get('thesis_type_ko') or ''])
    if I.get('direction_ko') and I.get('direction_ko') != P.get('research_direction_ko'):
        st.caption(
            f"※ 원 SQL의 방향값은 **{I.get('direction_ko')}**이지만, VIC 본문·기대수익·보유공시를 근거로 "
            f"실제 논지 방향을 **{P.get('research_direction_ko')}**으로 교정했습니다. 원본값은 감사 추적을 위해 보존합니다."
        )
    st.info(f"**사후분석 결론**  \n\n{D.get('one_line_verdict_ko')}")

    a,b,c,d = st.columns(4)
    a.metric('종합 판정', P.get('overall_verdict_ko') or '—')
    b.metric('Thesis 점수', f"{D.get('thesis_score',0):.1f}/10")
    c.metric('분석 프로세스', f"{D.get('process_score',0):.1f}/10")
    d.metric('분석 깊이', D.get('analysis_depth_ko') or '심층')
    st.warning(f"**주가 결과**  {D.get('return_summary_ko')}")

    if metrics:
        st.markdown('### 당시 숫자 vs 실제 결과')
        st.caption('원 투자논지의 숫자를 사후 실적과 같은 표에 놓습니다. “주가가 내렸다”가 아니라 어느 가정이 몇 배 틀렸는지 보기 위한 표입니다.')
        table=[{
            '지표':m['metric_name_ko'], '당시':m['t0_value_ko'], 'VIC 기대':m['thesis_expectation_ko'],
            '실제':m['actual_value_ko'], '판정':m['verdict_ko'], '해석':m['interpretation_ko']
        } for m in metrics]
        st.dataframe(table, use_container_width=True, hide_index=True, height=min(720, 85+len(table)*52))

    if sections:
        for sec in sections[:2]:
            st.markdown(f"### {sec['section_title_ko']}")
            st.markdown(sec['section_body_ko'])

    if claims:
        st.markdown('### 핵심 투자논지 · Claim별 사후검증')
        st.caption('각 Claim에서 당시 근거와 숨은 가정, 사전에 정할 수 있었던 반증조건, 실제 결과를 분리합니다.')
        for c in claims:
            verdict=c.get('verdict_ko') or '미판정'
            icon='✅' if ('성공' in verdict and '실패' not in verdict) else ('❌' if '실패' in verdict else '◐')
            with st.expander(f"{c['claim_order']}. {c['claim_title_ko']} · {icon} {verdict} · thesis 비중 {c['thesis_weight_pct']}%", expanded=True):
                st.markdown(f"**당시 주장**  \n{c['original_claim_ko']}")
                st.markdown(f"**당시 근거**  \n{c['t0_evidence_ko']}")
                st.markdown(f"**숨은 가정**  \n{c['key_assumption_ko']}")
                st.markdown(f"**사전에 정했어야 할 반증조건**  \n{c['ex_ante_falsifier_ko']}")
                st.markdown(f"**실제 결과**  \n{c['actual_result_ko']}")
                st.markdown(f"**정량적 괴리**  \n{c['quantitative_gap_ko']}")
                if '실패' in verdict:
                    st.error(f"**분석 오류**  {c['analytical_error_ko']}")
                else:
                    st.info(f"**분석상 핵심**  {c['analytical_error_ko']}")
                st.success(f"**재사용할 교훈**  {c['reusable_lesson_ko']}")

    if sections:
        for sec in sections[2:]:
            st.markdown(f"### {sec['section_title_ko']}")
            st.markdown(sec['section_body_ko'])

    if timeline:
        st.markdown('### 사건 타임라인 · 언제부터 논지가 깨졌나')
        for e in timeline:
            st.markdown(f"**{e['event_date_ko']} · {e['event_ko']}**")
            st.caption(e['thesis_implication_ko'])

    st.markdown('### 최종 Failure Anatomy')
    st.markdown(f"**근본 오류**  \n{D.get('core_error_ko')}")
    st.markdown(f"**가장 중요한 인사이트**  \n{D.get('core_insight_ko')}")
    st.info(f"**당시 이 질문 하나를 했더라면?**  \n\n{P.get('counterfactual_question_ko')}")

    if sources:
        with st.expander(f"근거 자료 {len(sources)}개 · 원문 링크와 어떤 판단에 썼는지"):
            for s in sources:
                st.markdown(f"**{s['source_order']}. [{s['source_type_ko']}] {s['title_ko']}** · {s['publisher']} · {s['source_date']}")
                st.write(s['evidence_ko'])
                if s.get('url'):
                    st.markdown(f"[원문 자료 열기]({s['url']})")
    return True


def _render_batch_postmortem(I, P, D):
    """Batch markdown과 같은 순서로 한 아이디어를 세로형 리포트로 표시한다."""
    from components.db import rows

    idea_id = I['idea_id']
    claims = rows('''
        SELECT claim_order,claim_title_ko,thesis_weight_pct,original_claim_ko,
               key_assumption_ko,ex_ante_falsifier_ko,actual_result_ko,
               quantitative_gap_ko,verdict_ko,analytical_error_ko,reusable_lesson_ko
        FROM deep_analysis_claims WHERE idea_id=? ORDER BY claim_order
    ''', (idea_id,))
    metrics = rows('''
        SELECT metric_order,metric_name_ko,t0_value_ko,thesis_expectation_ko,
               actual_value_ko,verdict_ko
        FROM deep_analysis_metrics WHERE idea_id=? ORDER BY metric_order
    ''', (idea_id,))
    timeline = rows('''
        SELECT event_order,event_date_ko,event_ko,thesis_implication_ko
        FROM deep_analysis_timeline WHERE idea_id=? ORDER BY event_order
    ''', (idea_id,))
    sources = rows('''
        SELECT source_order,source_type_ko,title_ko,publisher,source_date,url,evidence_ko
        FROM deep_analysis_sources WHERE idea_id=? ORDER BY source_order
    ''', (idea_id,))

    st.markdown('<div class="report-kicker">VIC DEEP POSTMORTEM</div>', unsafe_allow_html=True)
    company = html.escape(str(I.get('company_name') or I.get('ticker') or '기업 미상'))
    ticker = html.escape(str(I.get('ticker') or '—'))
    st.markdown(
        f'<div class="report-title">{company} ({ticker})</div>',
        unsafe_allow_html=True,
    )
    pills([
        I.get('date', '')[:10] if I.get('date') else '날짜 미상',
        f"{P.get('research_direction_ko') or '방향 미상'}",
        f"작성자 {I.get('author') or '미상'}",
        D.get('thesis_type_ko') or '투자논지',
        f"기준일 {D.get('research_asof') or P.get('research_asof') or '—'}",
    ])

    def normalized_direction(value):
        value = str(value or '').strip().lower()
        if value in {'롱', 'long'}:
            return 'long'
        if value in {'숏', 'short'}:
            return 'short'
        return value

    if I.get('direction_ko') and normalized_direction(I.get('direction_ko')) != normalized_direction(P.get('research_direction_ko')):
        st.caption(
            f"※ 원 SQL 방향은 {I.get('direction_ko')}이지만 VIC 본문·추천 증권·목표수익을 근거로 "
            f"실제 방향을 {P.get('research_direction_ko')}으로 교정했습니다."
        )

    st.markdown('<div class="section-number">CONCLUSION</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">결론부터</div>', unsafe_allow_html=True)
    st.info(_literal_dollars(D.get('one_line_verdict_ko') or P.get('why_ko') or '결론 미기재'))
    summary = [{
        '실제 방향': P.get('research_direction_ko') or '—',
        '종합 판정': P.get('overall_verdict_ko') or '—',
        '주가·증권 결과': D.get('return_summary_ko') or P.get('stock_verdict_ko') or '—',
        '논지 / 프로세스': f"{D.get('thesis_score', 0):.1f} / {D.get('process_score', 0):.1f}",
        '신뢰도': f"{P.get('confidence', 0):.0%}",
    }]
    st.dataframe(summary, use_container_width=True, hide_index=True, height=82)

    st.markdown('<div class="section-number">01 · BUSINESS</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">이 기업은 무엇을 하고 어떻게 돈을 버나</div>', unsafe_allow_html=True)
    st.markdown(_literal_dollars(P.get('company_description_ko') or '기업 설명 미기재'))

    st.markdown('<div class="section-number">02 · ORIGINAL THESIS</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">당시 VIC 투자논지</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(_literal_dollars(P.get('original_thesis_ko') or '투자논지 미기재'))

    if claims:
        st.markdown('#### 투자논지를 구성한 핵심 주장')
        st.caption('각 주장마다 당시 생각, 성립 조건, 사전에 확인할 반증조건과 실제 결과를 분리했습니다.')
        for claim in claims:
            verdict = claim.get('verdict_ko') or '미판정'
            icon = '✅' if ('성공' in verdict and '실패' not in verdict) else ('❌' if '실패' in verdict else '◐')
            with st.container(border=True):
                st.markdown(
                    f"#### {claim['claim_order']}. {claim['claim_title_ko']}  "
                    f"`비중 {claim['thesis_weight_pct']}%` · {icon} **{verdict}**"
                )
                st.markdown(_literal_dollars(f"**당시 주장**  \n{claim['original_claim_ko']}"))
                st.markdown(_literal_dollars(f"**이 주장이 성립하려면**  \n{claim['key_assumption_ko']}"))
                st.markdown(_literal_dollars(f"**실제 결과**  \n{claim['actual_result_ko']}"))
                with st.expander('반증조건·정량 괴리·재사용 교훈'):
                    st.markdown(_literal_dollars(f"**사전 반증조건**  \n{claim['ex_ante_falsifier_ko']}"))
                    st.markdown(_literal_dollars(f"**정량적 괴리**  \n{claim['quantitative_gap_ko']}"))
                    st.markdown(_literal_dollars(f"**분석 오류·핵심**  \n{claim['analytical_error_ko']}"))
                    st.markdown(_literal_dollars(f"**재사용할 교훈**  \n{claim['reusable_lesson_ko']}"))

    st.markdown('<div class="section-number">03 · WHAT HAPPENED</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">실제로 무슨 일이 일어났나</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(_literal_dollars(P.get('actual_development_ko') or '실제 전개 미기재'))
    if timeline:
        st.markdown('#### 사건 타임라인')
        for event in timeline:
            with st.container(border=True):
                st.markdown(f"**{event['event_date_ko']} · {event['event_ko']}**")
                st.write(event['thesis_implication_ko'])

    st.markdown('<div class="section-number">04 · VERDICT</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">왜 성공했고, 왜 실패했나</div>', unsafe_allow_html=True)
    verdict_rows = [
        ('사업 판단', P.get('business_verdict_ko')),
        ('밸류에이션 판단', P.get('valuation_verdict_ko')),
        ('촉매·시간 판단', P.get('catalyst_verdict_ko')),
        ('주가·증권 결과', P.get('stock_verdict_ko')),
    ]
    for label, value in verdict_rows:
        if value:
            st.markdown(_literal_dollars(f"**{label}**  \n{value}"))
    with st.container(border=True):
        st.markdown('**ROOT ERROR / CORE LESSON**')
        st.markdown(_literal_dollars(P.get('why_ko') or D.get('core_error_ko') or '—'))
    if P.get('first_signal_ko'):
        st.warning(_literal_dollars(f"**논지가 처음 확인되거나 깨진 신호 · {P.get('first_signal_date') or '—'}**  \n\n{P.get('first_signal_ko')}"))
    st.info(_literal_dollars(f"**당시에 이 질문을 했어야 합니다**  \n\n{P.get('counterfactual_question_ko') or '—'}"))

    if metrics:
        st.markdown('<div class="section-number">05 · NUMBERS</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">당시 숫자와 실제 결과</div>', unsafe_allow_html=True)
        metric_table = [{
            '지표': m['metric_name_ko'], '글 당시': m['t0_value_ko'],
            'VIC 기대': m['thesis_expectation_ko'], '실제': m['actual_value_ko'],
            '판정': m['verdict_ko'],
        } for m in metrics]
        st.dataframe(metric_table, use_container_width=True, hide_index=True, height=min(410, 82 + len(metric_table) * 40))

    st.markdown('<div class="section-number">06 · PATTERNS</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">이 사례에서 남길 성공·실패 유형</div>', unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        st.markdown('#### 성공·유효했던 부분')
        st.write((P.get('success_pattern_ko') or '없음').replace(';', ' · '))
    with right:
        st.markdown('#### 실패·주의할 부분')
        st.write((P.get('failure_pattern_ko') or '없음').replace(';', ' · '))

    if sources:
        st.markdown('<div class="section-number">07 · SOURCES</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">주요 근거자료</div>', unsafe_allow_html=True)
        for source in sources:
            title = f"{source['source_order']}. [{source['source_type_ko']}] {source['title_ko']}"
            with st.expander(title):
                st.caption(f"{source['publisher']} · {source['source_date']}")
                st.write(source['evidence_ko'])
                if source.get('url'):
                    st.markdown(f"[원문 자료 열기]({source['url']})")
    return True

def render_verified_postmortem(idea_id: str, compact: bool = False):
    """사후검증 완료 아이디어의 심층 리서치 노트를 렌더링한다."""
    from components.db import row, rows

    I = row('SELECT * FROM ideas_master WHERE idea_id=?', (idea_id,))
    P = row('SELECT * FROM postmortems WHERE idea_id=?', (idea_id,))
    if not I or not P:
        return False

    D = row('SELECT * FROM deep_analysis_meta WHERE idea_id=?', (idea_id,))
    if D:
        from components.batch_report import render_batch_source_report
        if render_batch_source_report(I):
            return True
        return _render_batch_postmortem(I, P, D)
    # V5: 이전 표준 초안은 더 이상 '사후분석 완료'로 렌더링하지 않는다.
    return False

    L = row('SELECT * FROM postmortem_longform WHERE idea_id=?', (idea_id,)) or {}
    claims = rows('''
        SELECT claim_order,claim_type_ko,original_claim_ko,key_assumption_ko,
               actual_result_ko,verdict_ko,explanation_ko
        FROM postmortem_claims WHERE idea_id=? ORDER BY claim_order
    ''', (idea_id,))
    metrics = rows('''
        SELECT metric_order,metric_name_ko,t0_period,t0_value,post_period,post_value,change_ko,interpretation_ko
        FROM postmortem_metrics WHERE idea_id=? ORDER BY metric_order
    ''', (idea_id,))
    timeline = rows('''
        SELECT event_order,date_ko,event_ko,significance_ko
        FROM postmortem_timeline WHERE idea_id=? ORDER BY event_order
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

    if L.get('one_line_ko'):
        st.info(f"**사후분석 한 줄 결론**  \n\n{L['one_line_ko']}")

    st.markdown('<div class="quick-section">1. 무슨 기업인가</div>', unsafe_allow_html=True)
    st.write(P.get('company_description_ko'))
    if L.get('business_economics_ko'):
        st.markdown('**이 사업의 경제성은 어디서 나오는가**')
        st.write(L['business_economics_ko'])

    st.markdown('<div class="quick-section">2. 당시 VIC 투자논지는 무엇이었나</div>', unsafe_allow_html=True)
    st.write(P.get('original_thesis_ko'))
    if claims:
        st.markdown(f"**핵심 논지는 {len(claims)}개로 분해할 수 있습니다.**")
        for c in claims:
            verdict = c.get('verdict_ko') or '미판정'
            icon = '✅' if '성공' in verdict and '실패' not in verdict else ('❌' if '실패' in verdict else '◐')
            st.markdown(f"#### ②-{c['claim_order']} {c['claim_type_ko']} · {icon} {verdict}")
            st.markdown(f"**당시 주장**  \n{c['original_claim_ko']}")
            st.markdown(f"**이 주장이 성립하려면**  \n{c['key_assumption_ko']}")
            st.markdown(f"**실제 결과**  \n{c['actual_result_ko']}")
            st.caption(f"사후 판단 · {c['explanation_ko']}")

    if L.get('valuation_at_t0_ko'):
        st.markdown('<div class="quick-section">3. 당시 밸류에이션과 기대수익 구조</div>', unsafe_allow_html=True)
        st.write(L['valuation_at_t0_ko'])

    st.markdown('<div class="quick-section">4. 실제로 이후 무슨 일이 일어났나</div>', unsafe_allow_html=True)
    st.write(P.get('actual_development_ko'))
    if metrics:
        st.markdown('**숫자로 비교하면**')
        mt=[{
            '지표':m['metric_name_ko'],
            '당시/기준 시점':m['t0_period'], '당시/기준 값':m['t0_value'],
            '사후 시점':m['post_period'], '사후 값':m['post_value'],
            '변화':m['change_ko'], '의미':m['interpretation_ko']
        } for m in metrics]
        st.dataframe(mt, use_container_width=True, hide_index=True, height=min(500, 90+len(mt)*55))
    if L.get('stock_return_summary_ko'):
        st.markdown('**주가 결과는 어떻게 봐야 하나**')
        st.write(L['stock_return_summary_ko'])

    if timeline:
        st.markdown('<div class="quick-section">5. 시간축으로 보면</div>', unsafe_allow_html=True)
        for e in timeline:
            st.markdown(f"**{e['date_ko']} · {e['event_ko']}**  ")
            st.caption(e['significance_ko'])

    st.markdown('<div class="quick-section">6. 투자논지는 어디서 맞고 어디서 틀렸나</div>', unsafe_allow_html=True)
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
    st.caption('¹ 원 VIC 성과 데이터가 존재하는 경우에만 표시. 실제 Long/Short 방향으로 교정한 값이며, 현재까지의 총수익률과는 별개입니다.')

    st.markdown('**왜 이런 결과가 나왔나**')
    st.write(P.get('why_ko'))
    if L.get('earnings_bridge_ko'):
        st.markdown('**실적·가치가 움직인 전달경로**')
        st.write(L['earnings_bridge_ko'])
    if L.get('what_was_right_ko'):
        st.success('**잘 본 부분**\n\n' + L['what_was_right_ko'])
    if L.get('what_was_wrong_ko'):
        st.warning('**틀렸거나 과도했던 부분**\n\n' + L['what_was_wrong_ko'])

    st.markdown('<div class="quick-section">7. 성공·실패 패턴과 반증 질문</div>', unsafe_allow_html=True)
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

    if L.get('lesson_ko') or L.get('current_watch_ko'):
        st.markdown('<div class="quick-section">8. 이 사례에서 현재 투자에 재사용할 것</div>', unsafe_allow_html=True)
        if L.get('lesson_ko'):
            st.markdown('**투자 교훈**')
            st.write(L['lesson_ko'])
        if L.get('current_watch_ko'):
            st.markdown('**지금 같은 회사를 본다면 무엇을 추적할까**')
            st.write(L['current_watch_ko'])
    if P.get('analyst_note_ko'):
        st.markdown('**사후분석 메모**')
        st.write(P.get('analyst_note_ko'))

    if sources:
        with st.expander(f"9. 근거 자료 {len(sources)}개 보기"):
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

    # V5 심층 웹 사후분석이 있으면 최우선한다.
    if render_ai_deep_postmortem(idea_id, compact=True):
        if st.button('전체 상세 분석 페이지로 이동', type='primary', use_container_width=True):
            st.session_state['selected_idea_id'] = idea_id
            st.switch_page('pages/2_사후분석_DB.py')
        return

    # 수동/curated 사후분석 완료 건은 자동 태그보다 우선한다.
    if render_verified_postmortem(idea_id, compact=True):
        if st.button('전체 상세 분석 페이지로 이동', type='primary', use_container_width=True):
            st.session_state['selected_idea_id'] = idea_id
            st.switch_page('pages/2_사후분석_DB.py')
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

    if not render_deep_thesis_reconstruction(idea_id, compact=True):
        from components.source_dossier import render_source_dossier
        render_source_dossier(idea_id, expanded=False)

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
        st.switch_page('pages/2_사후분석_DB.py')

def render_deep_thesis_reconstruction(idea_id: str, compact: bool=False):
    from components.db import row
    R=row('SELECT * FROM deep_thesis_reconstruction WHERE idea_id=?',(idea_id,))
    if not R: return False
    try: claims=json.loads(R.get('thesis_claims_json') or '[]')
    except: claims=[]
    try: nums=json.loads(R.get('numeric_facts_json') or '[]')
    except: nums=[]
    st.markdown('<span class="verified-pill">◆ 원문 기반 심층 투자논지 복원</span>',unsafe_allow_html=True)
    st.markdown('### 회사와 사업의 경제성')
    st.write(R.get('company_description_ko') or '—')
    st.write(R.get('business_economics_ko') or '—')
    st.markdown('### 당시 VIC 투자모델')
    st.write(R.get('thesis_overview_ko') or '—')
    if R.get('what_market_was_missing_ko'):
        st.info('**당시 시장이 놓쳤다고 본 것**\n\n'+R['what_market_was_missing_ko'])
    if claims:
        st.markdown('### 핵심 Claim')
        for i,c in enumerate(claims,1):
            wt=c.get('thesis_weight_pct')
            wt_txt=f" · 논지 비중 {wt:.0f}%" if isinstance(wt,(int,float)) else ''
            with st.expander(f"{i}. {c.get('claim_title_ko','Claim')}{wt_txt}",expanded=not compact):
                st.markdown(f"**당시 주장**  \n{c.get('claim_ko','—')}")
                st.markdown(f"**당시 근거**  \n{c.get('t0_evidence_ko','—')}")
                st.markdown(f"**숫자·산식**  \n{c.get('model_math_ko','—')}")
                st.markdown(f"**숨은 가정**  \n{c.get('key_assumptions_ko','—')}")
                st.markdown(f"**사전 반증조건**  \n{c.get('ex_ante_falsifier_ko','—')}")
                st.markdown(f"**먼저 볼 지표**  \n{c.get('leading_indicators_ko','—')}")
                st.markdown(f"**예상 시간축**  \n{c.get('expected_horizon_ko','—')}")
    if nums and not compact:
        st.markdown('### 원 논지의 핵심 숫자')
        st.dataframe([{'지표':x.get('metric_ko'),'값':x.get('value_ko'),'논지에서 역할':x.get('role_in_thesis_ko')} for x in nums],use_container_width=True,hide_index=True)
    st.markdown('### 당시 밸류에이션 모델')
    st.write(R.get('valuation_model_ko') or '—')
    st.markdown('### Catalyst · 리스크 · 시간축')
    st.write('**Catalyst**  \n'+(R.get('catalysts_ko') or '—'))
    st.write('**리스크**  \n'+(R.get('risks_ko') or '—'))
    st.write('**시간축**  \n'+(R.get('time_horizon_ko') or '—'))
    if R.get('thesis_dependency_map_ko'):
        st.markdown('### 논지 의존관계')
        st.write(R['thesis_dependency_map_ko'])
    if R.get('uncertainty_ko'):
        st.caption('불확실성 · '+R['uncertainty_ko'])
    return True


def render_ai_deep_postmortem(idea_id: str, compact: bool=False):
    from components.db import row
    I=row('SELECT * FROM ideas_master WHERE idea_id=?',(idea_id,))
    P=row('SELECT * FROM deep_postmortem_ai WHERE idea_id=?',(idea_id,))
    if not I or not P:return False
    try: claims=json.loads(P.get('claim_outcomes_json') or '[]')
    except:claims=[]
    try: metrics=json.loads(P.get('metrics_json') or '[]')
    except:metrics=[]
    try: timeline=json.loads(P.get('timeline_json') or '[]')
    except:timeline=[]
    try: sources=json.loads(P.get('sources_json') or '[]')
    except:sources=[]
    st.markdown('<span class="verified-pill">◆ 심층 사후분석 완료 · 웹/원자료 검증</span>',unsafe_allow_html=True)
    st.caption(f"분석 기준일 {P.get('research_asof') or '—'} · 신뢰도 {(P.get('confidence') or 0):.0%} · 모델 {P.get('model') or '—'}")
    st.markdown(f"## {I.get('company_name') or I.get('ticker')} · {I.get('ticker') or '—'}")
    st.info(f"**종합 판정: {P.get('overall_verdict_ko') or '—'}**\n\n{P.get('why_ko') or ''}")
    st.markdown('### 실제로 이후 무슨 일이 일어났나')
    st.write(P.get('actual_development_ko') or '—')
    st.write('**현재 상태**  \n'+(P.get('company_current_state_ko') or '—'))
    if metrics:
        st.markdown('### 당시 기대 vs 실제 숫자')
        st.dataframe([{'지표':x.get('metric_ko'),'당시/기대':x.get('t0_or_expected_ko'),'실제':x.get('actual_ko'),'해석':x.get('interpretation_ko')} for x in metrics],use_container_width=True,hide_index=True)
    if claims:
        st.markdown('### Claim별 성공·실패')
        for i,c in enumerate(claims,1):
            v=c.get('verdict_ko','미판정');icon='✅' if ('성공' in v and '실패' not in v) else ('❌' if '실패' in v else '◐')
            with st.expander(f"{i}. {c.get('claim_title_ko','Claim')} · {icon} {v}",expanded=not compact):
                st.markdown(f"**당시 주장**  \n{c.get('original_claim_ko','—')}")
                st.markdown(f"**실제 결과**  \n{c.get('actual_result_ko','—')}")
                st.markdown(f"**정량 gap**  \n{c.get('quantitative_gap_ko','—')}")
                st.markdown(f"**성공/실패 메커니즘**  \n{c.get('failure_or_success_mechanism_ko','—')}")
                st.markdown(f"**최초 신호**  \n{c.get('first_signal_ko','—')}")
                st.success('**재사용할 교훈**\n\n'+(c.get('reusable_lesson_ko') or '—'))
    axes=[('핵심 투자논지','thesis_verdict_ko'),('사업/산업구조','business_verdict_ko'),('Catalyst/Event','catalyst_verdict_ko'),('밸류에이션','valuation_verdict_ko'),('주가','stock_verdict_ko'),('현재','current_verdict_ko'),('종합','overall_verdict_ko')]
    st.markdown('### 어디서 맞고 어디서 틀렸나')
    st.dataframe([{'평가축':a,'판정':P.get(k) or '—'} for a,k in axes],use_container_width=True,hide_index=True)
    st.markdown('### Failure / Success Anatomy')
    st.write(f"**성공 패턴:** {P.get('success_pattern_ko') or '—'}")
    st.write(f"**실패 패턴:** {P.get('failure_pattern_ko') or '—'}")
    st.write(f"**근본 분석 오류:** {P.get('root_error_ko') or '—'}")
    st.write(f"**최초 반증·확인 신호:** {P.get('first_signal_ko') or '—'} · {P.get('first_signal_date_ko') or '—'}")
    st.write(f"**당시 알 수 있었나:** {P.get('knowable_at_t0_ko') or '—'} · **피할 수 있었나:** {P.get('avoidability_ko') or '—'}")
    st.info('**당시 이 질문 하나를 했더라면?**\n\n'+(P.get('counterfactual_question_ko') or '—'))
    if timeline and not compact:
        st.markdown('### 타임라인')
        for x in timeline: st.markdown(f"**{x.get('date_ko','')} · {x.get('event_ko','')}**  \n{x.get('thesis_implication_ko','')}")
    if P.get('stock_return_summary_ko'):
        st.warning('**주가 결과**\n\n'+P['stock_return_summary_ko'])
    if P.get('current_watch_ko'):
        st.markdown('### 지금 같은 회사를 본다면')
        st.write(P['current_watch_ko'])
    if sources and not compact:
        with st.expander(f"근거자료 {len(sources)}개",expanded=False):
            for s in sources:
                title=s.get('title') or '자료';url=s.get('url') or ''
                st.markdown(f"**{title}** · {s.get('publisher','')} · {s.get('date','')}")
                st.write(s.get('evidence_ko',''))
                if url: st.markdown(f"[원문 열기]({url})")
    return True
