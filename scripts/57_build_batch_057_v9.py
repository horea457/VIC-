#!/usr/bin/env python3
"""Build Batch 057 Weight Watchers / Asbury / ADA-ES canonical V9 artifacts."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-15"
spec = importlib.util.spec_from_file_location("batch46", ROOT / "scripts/46_build_batch_046_v9.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.ASOF = ASOF


m.BUSINESS.update({
    "wtw57": (
        "당시 WTW는 Willis Towers Watson이 아니라 Weight Watchers International common과 그 차입금이다. 회사는 대면 meetings, digital 체중관리 구독, 제품·라이선싱을 판매했다. "
        "현금엔진은 `meeting attendance×fee+digital subscribers×ARPU+products/licensing-leader·rent·marketing·technology-interest-tax`다. 고정비가 큰 만큼 subscriber gross additions와 retention이 동시에 좋아질 때 operating leverage가 크지만, free apps·wearables·낮은 category relevance는 gross additions를 빠르게 훼손한다. "
        "2012 debt-funded tender 뒤에는 enterprise value가 맞아도 common, 2016년 만기 B-1, 2020년 만기 B-2의 payoff가 달랐으므로 security별 waterfall이 분석의 출발점이다."
    ),
    "abg57": (
        "Asbury Automotive Group은 franchised new-vehicle dealers, used vehicles, Parts & Service(P&S), finance & insurance(F&I)를 운영한다. "
        "현금엔진은 `vehicle units×GPU+P&S repair orders×gross profit+F&I per unit-SG&A-floorplan interest-capex-cash tax`다. 매출 대부분은 차량 판매지만 gross profit과 downside protection은 P&S·F&I 및 variable SG&A에서 나온다. "
        "floorplan debt는 재고와 함께 움직이는 operating financing이므로 corporate leverage와 분리해야 하고, franchise rights·owned real estate·M&A는 세금·통합비·mortgage·working-capital need를 차감한 뒤에만 common 가치다."
    ),
    "ades57": (
        "ADA-ES/Advanced Emissions Solutions는 발전소용 ACI·DSI 등 배출저감 장비와 Section 45 refined-coal JV 지분을 보유했다. "
        "당시 핵심 현금엔진은 장비 매출보다 `적격 석탄 tonnage×inflation-adjusted tax credit×monetizer 계약조건×JV ownership-운영비·세금·본사비`에서 나오는 Tinuum 분배금이었다. "
        "이 현금은 만기 있는 세제 claim이며 회계·세무·배출감축 인증·monetizer 지급·JV waterfall을 통과해야 한다. 분배금이 실재해도 restatement, 내부통제, filing 지연, 재투자와 2021년 credit 만료가 common payoff를 바꿀 수 있다."
    ),
})


m.SOURCES.update({
    "wtw57": [
        m.S("WeightWatchers SEC archive", "https://www.sec.gov/edgar/browse/?CIK=105319&owner=exclude", "SEC / Weight Watchers", "2001-2019", "annual filings·debt·attendance·digital subscriber 연속성"),
        m.S("WeightWatchers annual reports", "https://corporate.ww.com/financials/annual-reports-and-proxy/default.aspx", "WW International", "2008-2025", "2012 tender·2014 실적·2016 B-1·2018~19 subscriber 검증"),
        m.S("WeightWatchers SEC filings", "https://corporate.ww.com/financials/sec-filings/default.aspx", "WW International", "2001-2025", "공식 10-K·10-Q·8-K archive"),
        m.S("Weight Watchers 2017 proxy", "https://www.sec.gov/Archives/edgar/data/105319/000119312517107775/d264156ddef14a.htm", "SEC / Weight Watchers", "2017-04", "meetings·online 정의와 Oprah 주식·option 계약"),
        m.S("Oprah partnership release", "https://corporate.ww.com/news/news-details/2015/Oprah-Winfrey-And-Weight-Watchers-Join-Forces-In-Groundbreaking-Partnership/default.aspx", "Weight Watchers", "2015-10-19", "10% 지분·option·board·협업 catalyst"),
    ],
    "abg57": [
        m.S("Asbury SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1144980&owner=exclude", "SEC / Asbury", "2002-2026", "dealer economics·leverage·acquisition·실적 연속성"),
        m.S("Asbury 2009 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1144980/000119312510044910/d10k.htm", "SEC / Asbury", "2010-03", "GFC trough·unit sales·P&S·liquidity·cost reset"),
        m.S("Asbury 2019 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1144980/000114498020000059/abg201910-k.htm", "SEC / Asbury", "2020-02", "pre-COVID revenue·EPS·dealer segment economics"),
        m.S("Park Place acquisition announcement", "https://www.sec.gov/Archives/edgar/data/1144980/000119312519312051/d841648dex991.htm", "SEC / Asbury", "2019-12", "$1bn·약 $100m EBITDA·luxury portfolio"),
        m.S("Asbury 2020 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1144980/000114498021000075/abg-20201231.htm", "SEC / Asbury", "2021-03", "COVID stress·Park Place·Clicklane·liquidity"),
        m.S("Asbury 2020 results", "https://www.sec.gov/Archives/edgar/data/1144980/000114498021000010/a2020q4ex991.htm", "SEC / Asbury", "2021-02", "$12.90 adjusted EPS·SG&A leverage·2025 plan"),
        m.S("Larry H. Miller/TCA acquisition", "https://www.sec.gov/Archives/edgar/data/1144980/000114498021000129/a991guardianpressrelease.htm", "SEC / Asbury", "2021-09", "$3.48bn 거래·dealership·revenue·EBITDA 규모"),
        m.S("Asbury 2025 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1144980/000114498026000051/abg-20251231.htm", "SEC / Asbury", "2026-02", "2025 revenue·P&S·GPU·SAAR·cash flow"),
        m.S("Asbury 2025 results", "https://investors.asburyauto.com/press-releases/21341", "Asbury Automotive", "2026-02", "2025 net income·adjusted operating cash flow"),
    ],
    "ades57": [
        m.S("Advanced Emissions SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1515156&owner=exclude", "SEC / ADES", "2011-2023", "JV ownership·분배금·split·restatement·법인연속성"),
        m.S("ADES 2021 results/10-K filing", "https://www.sec.gov/Archives/edgar/data/1515156/000151515622000007/a991pressrelease3822.htm", "SEC / ADES", "2022-03-08", "Tinuum ownership·2021 분배금·refined-coal 종료"),
        m.S("SEC cease-and-desist order", "https://www.sec.gov/files/litigation/admin/2017/33-10329.pdf", "U.S. SEC", "2017-03-29", "2011~14 reporting·internal-control failures와 material misstatement"),
        m.S("Joint Committee tax legislation explanation", "https://www.jct.gov/CMSPages/GetFile.aspx?guid=36515752-453a-473b-8242-c291855d9306", "U.S. Joint Committee on Taxation", "2016-03", "refined-coal Section 45 credit의 2021-12-31 종료 구조"),
        m.S("EIA refined-coal review", "https://www.eia.gov/todayinenergy/detail.php?id=53159", "U.S. EIA", "2022", "refined-coal 생산·세액공제·2021 종료 맥락"),
        m.S("ADES 2019 results", "https://www.globenewswire.com/news-release/2020/03/16/2001470/0/en/advanced-emissions-solutions-reports-fourth-quarter-and-full-year-2019-results.html", "Advanced Emissions Solutions", "2020-03-16", "2019 Tinuum distributions·royalties·remaining cash projection"),
    ],
})


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**x):
    x["claims"] = [C(*row) for row in x.pop("claimdata")]
    x.setdefault("security", "Common stock")
    x.setdefault(
        "waterfall",
        "영업 gross profit에서 SG&A·working capital·capex·interest·tax를 차감하고 floorplan·term debt 등 senior claim을 먼저 지급한 뒤 남는 per-share 현금만 common payoff다.",
    )
    return x


IDEAS = [
I(id="be3754ee-1951-434d-a1cd-1bf7f106f800", date="2015-05-05", author="pistolpete", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw57", raw_short=True, direction="Pair", entry="common 약 $8.46 / B-1 약 89", horizon="12~18개월", filename="analysis/ideas/2015/2015-05-05_WTW_capital_structure_pair.md", link=None, desc=32273, cat=2073,
title="common Short·B-1 first-lien loan Long pair", verdict="B-1 성공·common Short 실패·pair 혼합/실패·exact return 미검증", score=6.0, process=9.2, security="Short common + Long Tranche B-1 first-lien term loan",
waterfall="동일 enterprise cash에서 2016-04-02 만기 B-1 first-lien 약 $292.3m이 common보다 먼저 지급된다. B-2 약 $2.1bn과 common은 그 뒤의 residual claim이다. 따라서 포지션은 회사 전망 하나가 아니라 `B-1 repayment probability·carry/pull-to-par`와 `common downside·borrow/squeeze` 두 payoff를 sizing 후 합쳐야 한다.",
summary="raw 단순 Short가 아니라 common을 Short하고 89에 거래된 2016년 만기 B-1 first-lien loan을 Long한 자본구조 pair다. cash $301m·undrawn revolver $50m과 B-1의 짧은 만기는 credit leg을 지지했지만, 2015년 10월 Oprah의 10% 투자와 board/brand 참여가 common bankruptcy narrative를 뒤집었다.",
valuation="원문 base는 common Short 약 +35%, B-1 YTM/pull-to-par 약 +16.4%, 두 leg의 단순 합 약 +52%였다. 그러나 이는 notional·duration·borrow fee·short squeeze·loan accrued interest를 조정한 pair IRR이 아니다. B-1은 89에서 par 상환 여지가 있었지만 common은 option-like residual이라 촉매 전 무한대 손실 꼬리를 갖는다.",
actual="2015-10-19 Oprah는 약 $43.2m에 6,362,103주, 약 10%를 취득하고 options·board role·협업을 받았다. common은 강하게 반등해 Short leg을 훼손했다. 반면 회사는 2016-04-01 B-1 잔액 약 $144.3m을 cash로 par 상환해 senior credit 판단을 확인했다. 기업 분석은 양쪽 leg에서 달랐고 pair 전체는 sizing/borrow 자료 없이 exact 성과를 낼 수 없다.",
price="현재 SQL은 description 32,273자와 catalyst 2,073자를 포함하지만 performance COPY는 없다. common $8.46·B-1 89·원문 +35%/+16.4%/+52%는 T0 payoff model이며, 실제 borrow·notional·cover/repayment cash flow가 없어 pair return과 IRR은 null이다.",
drivers="credit leg은 짧은 maturity, first-lien priority와 당시 cash/revolver가 만들었다. equity leg 실패는 손익의 완만한 개선보다 외부 전략투자자가 refinancing probability와 brand relevance를 한 번에 바꾼 데서 왔다. 같은 enterprise에서 senior debt와 common의 duration·convexity가 반대였다.",
error="B-1 repayment와 common bankruptcy를 함께 놓고 상관이 낮다고 본 것이 오류다. B-1을 지키는 liquidity·refinancing catalyst가 common option value도 급등시킬 수 있었다. 또한 leg별 notional, borrow availability/fee, stop-loss와 Oprah 같은 rescue catalyst의 확률을 base payoff에 반영하지 않았다.", first_signal="전략투자·brand partnership가 발표되거나 common의 borrow cost/short interest가 급등하는 동시에 B-1 price가 par 쪽으로 움직이면 pair의 두 leg가 동시에 이기는 전제가 깨진 것으로 보고 common Short를 우선 재승인한다.",
metrics=[("Common/B-1 entry", "$8.46 / 89", "Short 하락 / par 수렴", "common squeeze / B-1 par 상환", "leg 분리"),("B-1 principal/maturity", "$292.3m / 2016-04-02", "11개월 내 지급", "$144.3m 잔액 cash 상환", "성공"),("Liquidity", "$301m cash+$50m revolver", "B-1 cover", "상환자금 제공", "성공"),("B-2/leverage", "$2.1bn·약 56 / 6.5x", "common 압박", "refinancing option 유지", "혼합"),("원문 base payoff", "+35%/+16.4%/합 +52%", "12~18개월", "sizing·borrow 미복원", "미검증")],
timeline=[("2012", "$1.5bn debt-funded tender", "common leverage 상승"),("2014", "adjusted EBITDA $361.7m·제품매출 하락", "denominator 약화"),("2015-05-05", "VIC pair 게시", "common Short/B-1 Long"),("2015-10-19", "Oprah 10% 투자", "equity 핵심 반증"),("2015-Q4", "brand/refinancing narrative 반전", "Short squeeze"),("2016-04-01", "B-1 $144.3m par 상환", "credit leg 성공"),("2017-2018", "subscriber·주가 회복", "common Short 최종 실패")],
claimdata=[("attendance·product decline", "meetings와 제품의 구조적 쇠퇴가 EBITDA를 낮춘다.", "attendance 약 62.0%→48.3%, products $442.7m→$298.0m", "digital/brand rescue가 gross adds를 못 되돌린다.", "gross additions·attendance의 지속 반등이면 반증.", "Oprah 이후 subscriber narrative가 반전했다.", "부분→실패", "구조적 decline에도 rescue option을 가격화한다."),("B-1 money-good", "89의 B-1은 cash와 짧은 만기로 par 상환된다.", "$301m cash+$50m revolver 대 $292.3m principal", "cash가 common보다 senior maturity에 배정된다.", "liquidity burn·교차가속·refinancing 실패면 반증.", "2016-04-01 잔액 $144.3m cash 상환.", "성공", "enterprise distress 속에서도 maturity별 claim을 산다."),("B-2가 common 압박", "$2.1bn B-2와 6.5x leverage가 equity를 훼손한다.", "B-2 약 56·2020 maturity", "운영회복 전 refinancing이 불가능하다.", "sponsor/전략투자·EBITDA 반등이면 반증.", "외부 투자와 후속 회복으로 option value 유지.", "실패", "distressed debt는 common zero의 충분조건이 아니다."),("pair convexity", "credit carry와 equity downside가 함께 발생한다.", "원문 base +35%와 +16.4%", "B-1 보호 요인이 common에는 도움이 되지 않는다.", "동일 rescue catalyst가 두 security를 올리면 반증.", "Oprah가 정확히 이 상관을 깨뜨렸다.", "실패", "pair는 각 leg보다 cross-catalyst를 먼저 stress한다."),("common downside", "2015 guide와 category decline으로 common이 더 내려간다.", "Q4 guide shock와 $8.46 price", "borrow와 squeeze cost가 제한적이다.", "strategic capital·subscriber inflection이면 cover.", "Oprah 발표 뒤 squeeze.", "실패", "Short payoff에는 borrow와 rescue 확률을 넣는다."),("security selection", "common보다 B-1이 훨씬 좋은 risk/reward다.", "first-lien·짧은 maturity·현금 cover", "claim priority가 실제 지급으로 이어진다.", "B-1 default/restructuring이면 반증.", "B-1은 par 상환, common은 생존.", "강한 성공", "회사보다 cash-flow claim을 선택한다.")]),

I(id="c1243cb1-9afa-476c-9147-ad1becbc5683", date="2015-11-10", author="piggybanker", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw57", raw_short=True, direction="Long", entry="약 $24", horizon="2016년 말", filename="analysis/ideas/2015/2015-11-10_WTW_long.md", link=None, desc=11268, cat=12,
title="Oprah subscriber acquisition·fixed-cost leverage Long", verdict="2016 target 실패·2017~18 사업논지 지연 성공·exact return 미검증", score=7.2, process=8.3,
summary="Oprah 투자 직후 약 $24에서 celebrity headline가 아니라 1.5~2.0m incremental subscribers가 meeting/digital 고정비 위에서 만드는 contribution을 산 Long이다. $87 upside, $16 downside, 확률가중 $50을 2016년 말까지 제시했으나 실제 turnaround clock은 더 길었다.",
valuation="upside/base/downside subscriber additions를 2.0m/1.5m/0.75m으로 두고 10x/9x/8x EBITDA를 적용해 $87/$50 인근/$16을 만들었다. 이 bridge의 핵심은 subscriber 수가 아니라 acquisition cost, meeting/digital mix, retention, interest와 희석 후 incremental EBITDA/share다.",
actual="2016년 말 $50 target은 실현되지 않았다. 하지만 product·mobile·Oprah marketing의 누적 효과로 2017~18 subscriber와 이익이 가속했고 2018년 초 subscriber는 약 4.6m에 이르렀다. operating mechanism은 맞았지만 catalyst duration과 당시 높은 leverage의 equity clock을 과소평가했다.",
price="현재 SQL에는 description 11,268자와 catalyst 12자가 있으나 performance COPY는 없다. $24·$16/$50/$87은 원문 anchor이고 후대 Willis Towers Watson ticker series는 사용하지 않았다. exact 1/3/5년 return과 IRR은 null이다.",
drivers="장기 성과를 만든 것은 Oprah 이름 자체보다 gross additions, retention과 high-fixed-cost platform의 incremental margin이었다. 지연은 brand campaign을 subscriber·revenue로 바꾸는 데 여러 enrollment season이 필요했고 debt service가 equity rerating을 늦췄기 때문이다.",
error="Oprah audience를 즉시 paid subscribers로 바꾸고 2016 한 해에 operating leverage와 multiple rerating을 함께 넣었다. gross additions, churn, CAC와 cohort margin을 분리하고 target date가 지나면 자동 재승인했어야 한다.", first_signal="2016년 첫 두 enrollment season에 gross additions가 base의 1.5m run-rate를 향하지 않거나 CAC가 상승하고 retention이 개선되지 않으면 $50/YE2016 target을 폐기하고 duration을 늘린다.",
metrics=[("Entry/targets", "$24", "$16/$50/$87", "2016 $50 미달", "timing 실패"),("Incremental subs", "0.75/1.5/2.0m", "base 1.5m", "2017~18 누적 성장", "지연 성공"),("Oprah stake", "약 10%·$43.2m", "alignment+acquisition", "board/brand catalyst", "성공"),("Fixed-cost leverage", "meeting+digital platform", "EBITDA 급증", "turnaround 뒤 현실화", "성공/지연"),("2018 subscribers", "T0 미관찰", "bull 경로", "약 4.6m", "성공 방향")],
timeline=[("2015-10-19", "Oprah partnership", "핵심 catalyst"),("2015-11-10", "VIC Long", "$24·$50 PW"),("2016-H1", "recruitment ramp 완만", "clock 압박"),("2016-12", "$50 target 미달", "stated horizon 실패"),("2017", "subscriber·earnings inflection", "지연된 검증"),("2018-Q1", "subscriber 약 4.6m", "operating leverage 확인"),("2018-H2", "높은 기대·변동성", "exit discipline 필요")],
claimdata=[("Oprah recruitment", "Oprah가 대규모 신규 subscriber를 유입한다.", "10% 자기자금 투자·board·개인 사용", "audience가 낮은 CAC의 paid conversion으로 이어진다.", "두 season 동안 gross adds가 계획 미달이면 반증.", "효과는 2017~18에 크게 누적.", "성공/지연", "celebrity reach를 CAC·conversion cohort로 번역한다."),("subscriber operating leverage", "1.5m base adds가 EBITDA를 급증시킨다.", "meeting/digital 고정비 구조", "retention과 mix가 기존 수준을 지킨다.", "churn·meeting deleverage가 contribution을 상쇄하면 반증.", "후속 이익성장에서 현실화.", "성공", "gross adds와 retention을 따로 모델링한다."),("new product fit", "Oprah와 새 프로그램이 category relevance를 되살린다.", "brand/product relaunch", "free apps 대비 지불의사가 회복된다.", "trial 후 renewal 약화면 반증.", "turnaround는 왔지만 시간이 더 필요했다.", "부분 성공", "제품 fit은 첫 가입보다 renewal로 본다."),("$16 downside", "실패해도 brand·subscriber base가 하방을 지지한다.", "downside 0.75m adds·8x", "debt와 category erosion이 더 악화하지 않는다.", "EBITDA 하락·refinancing stress면 하방 재계산.", "초기 변동성과 높은 leverage 지속.", "미검증", "levered equity downside는 residual option으로 stress한다."),("$50 YE2016", "base case가 한 해 안에 가격에 반영된다.", "1.5m adds·9x EBITDA", "두 enrollment cycle이면 충분하다.", "2016 target 미달 시 실패.", "명확히 미달.", "실패", "business thesis와 market clock을 분리한다."),("Long direction", "$24에서 downside보다 upside가 크다.", "$16 대 $50/$87 payoff", "borrow가 아닌 common Long이다.", "subscriber thesis 파손 시 반증.", "raw Short를 Long으로 교정.", "성공", "방향은 추천 action과 payoff로 확정한다.")]),

I(id="f132b76e-3d24-4d61-beae-a2d728104289", date="2018-12-11", author="aaron16", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw57", raw_short=True, direction="Long", entry="약 $48", horizon="약 10개월", filename="analysis/ideas/2018/2018-12-11_WTW_long.md", link="https://www.valueinvestorsclub.com/idea/WEIGHT_WATCHERS_INTL_INC/8524345507", desc=0, cat=22,
title="digital retention·customer-life extension Long", verdict="10개월 horizon 실패·retention/digital 논지 일부 성공", score=4.8, process=7.4,
summary="약 $48에서 customer life가 8개월에서 10개월로 늘고 digital 전환이 net subscriber compounding을 지탱한다는 Long이다. 보수적 2021 EBIT·10x에서 $72.85, 약 1.45x MOIC를 제시했지만 gross additions와 2019 marketing execution이 retention 개선을 압도했다.",
valuation="2021 EBIT에 10x를 적용하고 net debt를 차감해 약 $72.85를 제시했다. subscriber equation은 `beginning subs+gross adds-churn`인데, 원문은 retention 개선을 자세히 보면서 recruiting productivity와 wellness rebrand의 CAC/response risk를 상대적으로 약하게 다뤘다.",
actual="2019 revenue는 약 6.7%, gross profit은 약 9.2% 감소했고 recruiting·marketing 실행이 부진했다. 반면 2019년 말 total subscribers는 약 4.2m, digital은 약 3.0m으로 늘었고 2020년 초 members는 5m을 넘었다. product/retention은 일부 맞았으나 revenue·valuation·10개월 clock은 실패했다.",
price="현재 SQL에는 catalyst 22자만 있고 description·performance COPY는 없다. $48·$72.85·1.45x는 prior overlay의 원문 anchor이며 exact return/IRR은 null이다. WTW ticker 재사용 성과값은 폐기했다.",
drivers="손실 경로는 churn보다 gross additions가 결정했다. customer life가 늘어도 acquisition funnel과 brand message가 약하면 ending subscribers·revenue가 기대에 못 미친다. 높은 시작 기대와 10개월 horizon이 운영상 부분 성공을 나쁜 security outcome으로 바꿨다.",
error="net adds를 retention 중심으로 설명해 gross additions의 분산과 CAC를 충분히 stress하지 않았다. 2021 EBIT target을 10개월 price target으로 당겨 쓰고 wellness rebrand가 category specificity를 흐릴 가능성을 낮게 뒀다.", first_signal="2019 첫 enrollment season에 gross additions·revenue guide가 하향되고 marketing spend 대비 recruits가 감소하면 retention 개선과 무관하게 10개월 target을 즉시 폐기한다.",
metrics=[("Entry/target", "$48", "$72.85", "10개월 미달", "실패"),("Customer life", "8→10개월", "retention 지속", "digital engagement 일부 유지", "부분 성공"),("2019 revenue", "$1.514bn prior", "성장/안정", "$1.413bn·-6.7%", "실패"),("2019 gross profit", "안정 기대", "operating leverage", "약 -9.2%", "실패"),("2019 YE subscribers", "net-add slowdown 우려", "mid-single-digit 성장", "4.2m·digital 3.0m", "부분 성공")],
timeline=[("2015", "Oprah turnaround 시작", "precedent"),("2018", "customer life 8→10개월", "quality 개선"),("2018-12-11", "VIC Long", "$48·10개월"),("2019-02", "guidance/marketing 우려", "첫 반증"),("2019-FY", "revenue·gross profit 하락", "valuation 실패"),("2019-12", "subscribers 4.2m", "retention 일부 검증"),("2020-Q1", "members 5m+", "digital 논지 잔존")],
claimdata=[("retention compounding", "customer life 8→10개월이 base를 compounding한다.", "mobile engagement·cohort data", "gross additions가 크게 악화하지 않는다.", "recruits 감소가 churn 개선을 초과하면 반증.", "2019 recruits 약화가 결과를 압도.", "부분/실패", "subscriber model은 gross adds와 churn의 2변수다."),("digital conversion", "physical에서 digital로의 전환이 margin과 scale을 높인다.", "app 개선·digital 비중 상승", "ARPU·engagement가 discount 없이 유지된다.", "digital growth에도 revenue/GP가 하락하면 반증.", "digital subs 증가는 맞고 revenue는 감소.", "부분 성공", "digital mix 상승과 monetization을 분리한다."),("net-add concern priced", "둔화 우려가 $48에 충분히 반영됐다.", "고점 대비 하락", "시장 기대가 2019 miss를 포함한다.", "guide cut 뒤 multiple 재하락이면 반증.", "2019 miss가 추가 하락을 만들었다.", "실패", "고점 대비 하락은 reverse DCF가 아니다."),("2021 EBIT bridge", "retention만으로 2021 EBIT가 target을 지지한다.", "flat net adds+retention +3% 예시", "CAC·marketing·rebrand 비용이 안정적이다.", "gross profit·revenue 동반 하락이면 반증.", "두 수치 모두 하락.", "실패", "subscriber 수를 EBIT로 잇는 비용 bridge가 필요하다."),("10x/$72.85", "보수 배수에도 1.45x다.", "2021 EBIT·net debt", "10개월 안에 forward confidence가 회복된다.", "2019 guide 하향이면 clock 실패.", "specified horizon 실패.", "실패", "terminal year와 holding period를 맞춘다."),("Long direction", "개선된 business quality를 common Long으로 산다.", "$48→$72.85", "높은 leverage가 운영 miss를 증폭하지 않는다.", "recruitment miss·debt ratio 상승이면 반증.", "raw Short→Long 교정은 맞음.", "방향 교정 성공", "metadata와 투자결과를 분리한다.")]),

I(id="8264961d-a7d0-4ae3-83aa-0d0d2364d53d", date="2008-04-24", author="bedrock346", ticker="ABG", entity="Asbury Automotive Group, Inc.", group="abg57", raw_short=True, direction="Long", entry="약 $14", horizon="3~5년", filename="analysis/ideas/2008/2008-04-24_ABG_long.md", link="https://www.valueinvestorsclub.com/idea/Asbury_Automotove/8156709057", desc=0, cat=319,
title="P&S/F&I 방어력·14m SAAR recession Long", verdict="SAAR floor·단기 path 실패·장기 사업회복", score=5.2, process=7.2,
summary="약 $14, 7.5x P/E와 6.4% dividend yield에서 imports/luxury mix와 P&S·F&I의 약 60% gross-profit contribution을 산 Long이다. 그러나 population-adjusted 14m SAAR를 deep recession floor로 둔 것이 치명적이었고 실제 2009 미국 light-vehicle sales는 약 10.3m이었다.",
valuation="recession EPS $1.47 @ 14m SAAR와 normalized EPS $2.50×15=$37.50을 사용했다. 이 산식은 SAAR가 4m 더 낮아질 때 new/used GPU, F&I volume, P&S absorption, floorplan availability와 fixed cost가 동시에 나빠지는 nonlinear stress를 담지 못했다.",
actual="GFC에서 vehicle credit와 floorplan confidence가 붕괴해 원문의 recession floor가 깨졌다. P&S와 variable cost는 기업 생존에 도움을 줬지만 common의 급격한 path loss를 막지 못했다. 이후 경기와 판매가 회복하며 dealer franchise durability는 확인됐으나 현재 SQL이 없어 exact total return은 산출하지 않는다.",
price="현재 SQL에는 catalyst 319자만 있고 description·performance COPY는 없다. $14·$1.47·$2.50·$37.50은 원문/prior overlay anchor다. 기존 price-only series는 current attachment로 검증되지 않아 전부 null이다.",
drivers="오류는 dealer economics보다 macro floor에서 왔다. 높은 P&S/F&I mix는 loss severity를 낮췄지만 credit availability와 unit collapse가 common valuation clock을 압도했다. 장기 회복은 franchise와 service installed base가 살아남았기 때문이다.",
error="1991 SAAR trough에 population growth를 더해 2008 floor를 추정했고 credit-market discontinuity를 빠뜨렸다. dividend와 book/earnings multiple도 liquidity stress에서 하방이 아니었다. SAAR 10m·GPU/F&I·floorplan haircut을 함께 넣은 survival case가 필요했다.", first_signal="SAAR가 13m 아래로 내려가고 consumer credit approval·floorplan terms가 동시에 악화하면 $1.47 recession EPS와 dividend floor를 폐기하고 monthly liquidity를 재계산한다.",
metrics=[("Entry/yield/P-E", "$14 / 6.4% / 7.5x", "rerating", "GFC path 훼손", "실패"),("Recession SAAR", "14m", "floor", "2009 약 10.3m", "강한 실패"),("Recession EPS", "$1.47", "양의 earnings", "stress 과소", "실패"),("Normalized EPS/target", "$2.50×15", "$37.50", "장기 회복", "방향 일부 성공"),("P&S+F&I GP mix", "약 60%", "방어력", "생존·회복 기여", "성공")],
timeline=[("2007", "P&S 41%·F&I 18% GP", "방어 pool"),("2008-04-24", "VIC Long", "$14·14m SAAR"),("2008-H2", "credit/floorplan crisis", "첫 핵심 반증"),("2008-Q4", "ABG loss", "operating deleverage"),("2009", "US sales 약 10.3m", "SAAR floor 파손"),("2010", "cost-reset 후 회복", "business survival"),("2011-2013", "업황 정상화", "장기 franchise 검증")],
claimdata=[("14m SAAR floor", "population-adjusted trough는 13.6~14m다.", "1991 11.3m에 인구 증가 적용", "credit availability가 과거와 유사하다.", "SAAR<13m이면 즉시 반증.", "2009 약 10.3m.", "강한 실패", "macro floor는 금융조건과 함께 stress한다."),("P&S recession defense", "P&S가 vehicle sales 감소를 완충한다.", "gross profit 41%·높은 margin", "miles/repair 수요가 유지된다.", "repair orders·gross profit 동반 급락이면 반증.", "기업 생존과 후속 회복에 기여.", "성공", "installed-base cash engine을 분리한다."),("F&I low risk", "F&I는 credit risk 없이 fee를 번다.", "gross profit 18%·lender에 대출 양도", "approval rate·unit volume이 유지된다.", "credit approval collapse면 반증.", "volume/financing shock에 노출.", "부분 실패", "balance-sheet risk가 없어도 volume beta는 남는다."),("import/luxury mix", "brand mix가 domestic downturn을 방어한다.", "import·luxury franchise 비중", "segment 상관이 낮다.", "전 브랜드 동시 unit 하락이면 반증.", "systemwide credit shock가 mix를 압도.", "실패/장기 유효", "mix는 system shock의 hedge가 아니다."),("dividend floor", "6.4% yield가 기다릴 보상이다.", "당시 배당", "liquidity stress에서도 유지된다.", "cut/suspension이면 floor 제거.", "배당은 common 보호가 아니었다.", "실패", "cyclical yield는 residual distribution이다."),("$37.50 normalization", "$2.50 EPS×15x가 장기 가치다.", "정상 SAAR·peer multiple", "희석 없이 정상화까지 생존한다.", "liquidity raise·지속 저SAAR이면 반증.", "사업은 회복했으나 경로가 극단적.", "부분 성공", "normal value에 survival probability를 곱한다.")]),

I(id="38005e68-af15-44b4-aa2e-94e545c78704", date="2010-03-12", author="baileyb906", ticker="ABG", entity="Asbury Automotive Group, Inc.", group="abg57", raw_short=True, direction="Long", entry="약 6.5x normalized EPS", horizon="3~5년", filename="analysis/ideas/2010/2010-03-12_ABG_long.md", link=None, desc=13914, cat=124,
title="관찰된 trough cost reset·$2.03 EPS Long", verdict="사업·정상화 논지 강한 성공·exact return 미검증", score=9.0, process=9.3,
summary="2008처럼 recession floor를 예측한 것이 아니라 실제 10.3m SAAR에서 ABG가 비용을 줄이고 다시 이익을 내는 것을 본 뒤 산 Long이다. 2009 EPS $0.82에 unit recovery $0.95, heavy-truck loss 제거 $0.06, SG&A 효율 $0.20을 더해 normalized $2.03, 9~10x로 $18~20을 제시했다.",
valuation="normalized EPS bridge는 `$0.82+$0.95+$0.06+$0.20=$2.03`; 9~10x가 $18~20이다. 2009 new units 약 62k에서 14.5m SAAR로 약 40% unit recovery를 가정했지만, 핵심 차이는 이미 8~10m SAAR 구간에서 4Q08 -$0.02에서 2Q09 $0.22로 돌아온 cost base를 관찰했다는 점이다.",
actual="미국 판매와 ABG unit economics가 회복되면서 normalized earnings bridge가 현실화됐다. P&S 약 50% gross margin과 감축된 SG&A가 incremental vehicle gross profit을 EPS로 전달했다. 현재 SQL 성과 데이터가 없으므로 기존 overlay의 큰 1~5년 price series는 버리고 operating thesis만 강한 성공으로 판정한다.",
price="현재 SQL에는 description 13,914자와 catalyst 124자가 있으나 performance COPY는 없다. $0.82/$2.03/$18~20은 원문 anchor이고 exact return/IRR은 null이다.",
drivers="성공의 원인은 macro 예측이 아니라 관찰된 stress response였다. SAAR가 거의 개선되지 않은 구간에도 profit이 돌아왔고, 이후 unit recovery가 reset된 SG&A 위에 얹혔다. 같은 회사라도 정보 set과 starting expectation이 달라지면 완전히 다른 투자다.",
error="14.5m normalized SAAR와 40% unit 회복을 단일 base로 두고 GPU·F&I·P&S mix와 floorplan rate의 범위를 더 넓게 두지 않았다. cost cuts가 customer service나 후속 capex를 훼손할 가능성도 별도 claim으로 만들 수 있었다.", first_signal="SAAR가 낮은 상태에서도 두 분기 연속 P&S gross profit과 SG&A leverage가 악화하고 EPS가 다시 적자로 가면 observed cost reset claim을 폐기한다.",
metrics=[("2009 EPS", "$0.82", "정상화 base", "양의 trough earnings", "성공"),("Normalized EPS", "$2.03", "$18~20 @9~10x", "후속 earnings 회복", "성공"),("Unit recovery", "+$0.95 EPS", "14.5m SAAR", "판매 회복", "성공 방향"),("SG&A efficiency", "+$0.20 EPS", "cost reset 유지", "stress 후 leverage", "성공"),("Liquidity", "$85m cash+$158m capacity", "survival runway", "회복까지 유지", "성공")],
timeline=[("2008-Q4", "EPS -$0.02", "trough"),("2009-Q2", "EPS $0.22", "SAAR 개선 없이 profit"),("2009-FY", "EPS $0.82·sales 10.3m", "stress evidence"),("2010-03-12", "VIC Long", "$2.03 bridge"),("2010-2011", "SAAR·unit recovery", "incremental profit"),("2012-2013", "earnings normalization", "thesis 검증"),("2014+", "dealer consolidation", "franchise durability")],
claimdata=[("observed trough survival", "10m대 SAAR에서도 ABG가 흑자로 돌아섰다.", "4Q08 -$0.02→2Q09 $0.22", "비용절감이 반복 가능하고 일회성이 아니다.", "낮은 SAAR에서 재적자면 반증.", "후속 흑자와 회복.", "강한 성공", "forecast floor보다 observed stress를 산다."),("unit recovery $0.95", "14.5m SAAR가 EPS $0.95를 더한다.", "2009 62k units·약 40% 회복", "GPU·share가 유지된다.", "units 회복에도 EPS bridge 미달이면 반증.", "업황 회복이 earnings에 전달.", "성공", "unit×incremental gross profit으로 bridge한다."),("P&S engine", "50% gross margin P&S가 trough를 방어한다.", "2009 segment economics", "repair demand와 technician capacity 유지.", "same-store P&S GP 하락이면 반증.", "회복 기반으로 작동.", "성공", "dealer EBITDA는 revenue보다 P&S에서 시작한다."),("SG&A reset", "감축된 overhead가 정상화 EPS에 $0.20을 더한다.", "위기 중 흑자전환", "revenue 회복 때 비용이 전부 되돌아오지 않는다.", "SG&A/GP 재상승이면 반증.", "operating leverage 현실화.", "성공", "cost cut은 ratio와 service KPI로 검증한다."),("liquidity runway", "$85m cash와 $158m capacity가 기다릴 시간을 준다.", "2009 balance sheet", "가용성이 covenant·collateral로 막히지 않는다.", "cash burn/line restriction이면 반증.", "회복까지 생존.", "성공", "liquidity는 trough evidence와 결합할 때 강하다."),("$18~20 value", "$2.03에 9~10x면 50%+ upside다.", "정상화 bridge", "share count·interest가 안정적이다.", "희석·금리상승이면 target 하향.", "사업 정상화 방향은 맞음.", "성공/수익 미검증", "target과 exact return은 분리한다.")]),

I(id="60573ef4-57de-4558-8542-85f242de813f", date="2020-02-18", author="manatee", ticker="ABG", entity="Asbury Automotive Group, Inc.", group="abg57", raw_short=True, direction="Long", entry="market cap 약 $2bn / EV 약 $4bn", horizon="2~3년", filename="analysis/ideas/2020/2020-02-18_ABG_long.md", link=None, desc=0, cat=170,
title="P&S resilience·Park Place accretion Long", verdict="극단적 COVID path 후 사업논지 성공·exact return 미검증", score=8.0, process=8.6,
summary="COVID 직전 market cap 약 $2bn, EV 약 $4bn에서 pro forma revenue $9.4bn·EBITDA $455m·FCF $223m, 10x 미만 EPS와 double-digit FCF yield를 산 Long이다. Park Place가 luxury/P&S mix와 scale을 높인다는 논지는 맞았지만 한 달 뒤 유동성 tail이 현실화됐다.",
valuation="Park Place pro forma 기준 revenue $9.4bn, EBITDA $455m, FCF $223m으로 equity FCF yield는 두 자릿수였다. $1bn acquisition은 synergies 포함 약 $100m EBITDA의 10x였다. downside EPS 약 $11을 사용했지만 pandemic shutdown·inventory liquidation·deal financing을 하나의 severe state로 충분히 묶지 않았다.",
actual="2020년 3월 dealership shutdown은 극단적인 경로를 만들었으나 P&S, variable SG&A와 이후 inventory scarcity/GPU가 현금흐름을 방어했다. Park Place는 조건을 재협상해 완료됐다. 2020 adjusted EPS는 $12.90으로 2019 $9.46보다 높았고 pro forma net leverage는 약 2.1x였다.",
price="현재 SQL에는 catalyst 170자만 있고 description·performance COPY는 없다. 기존 overlay의 단기 급락·후속 상승 수익률은 검증되지 않아 null로 폐기한다. corporate operating facts만으로 exact Long return을 만들지 않는다.",
drivers="수익 엔진은 unit volume보다 P&S, 비용변동성과 공급부족 GPU였다. management의 deal repricing과 liquidity 관리가 Park Place optionality를 살렸다. 반대로 posting 직후의 COVID path는 valuation margin이 liquidity timing을 보장하지 않음을 보여준다.",
error="moderate recession EPS를 downside로 두고 전국적 shutdown, acquisition commitment와 floorplan/working-capital swing을 동시 stress하지 않았다. enterprise quality가 좋아도 margin call·forced sale을 피할 liquidity bucket과 position sizing이 필요했다.", first_signal="store closures와 SAAR 급락이 시작될 때 unrestricted liquidity, monthly cash burn, Park Place termination/repricing rights를 즉시 재산정하고 12개월 survival buffer가 없으면 thesis와 별개로 포지션을 줄인다.",
metrics=[("Market cap/EV", "$2bn/$4bn", "rerating", "COVID 후 회복", "사업 성공"),("Pro forma revenue", "$9.4bn", "scale", "Park Place 완료", "성공"),("EBITDA/FCF", "$455m/$223m", "cash yield", "2020 stress 견딤", "성공 방향"),("Park Place", "$1bn/~$100m EBITDA", "accretion", "재협상 후 완료", "성공"),("2020 adjusted EPS", "2019 $9.46", "downside ~$11", "$12.90", "성공")],
timeline=[("2019-12", "Park Place $1bn 발표", "M&A thesis"),("2020-02-18", "VIC Long", "pre-COVID entry"),("2020-03", "COVID shutdown", "극단적 path risk"),("2020-Q2", "비용·재고 reset", "survival evidence"),("2020", "Park Place 재협상/완료", "catalyst 보존"),("2020-Q4", "adjusted EPS $12.90", "business 반증 회피"),("2021-2022", "dealer cash flow 확대", "thesis 검증")],
claimdata=[("P&S downside defense", "P&S가 recession에도 EBITDA를 지킨다.", "GP 약 50%·높은 margin", "shutdown 뒤 repair demand가 재개된다.", "P&S GP 장기 급락이면 반증.", "COVID stress 뒤 빠르게 회복.", "성공", "dealer defense는 installed-base service다."),("variable SG&A", "commissions 등 비용이 sales와 함께 내려간다.", "dealer compensation structure", "fixed occupancy/tech cost가 감당 가능하다.", "SG&A/GP 급등이면 반증.", "2020 cost flex가 확인됨.", "성공", "비용은 고정/변동/반고정으로 나눈다."),("Park Place accretion", "luxury portfolio가 EBITDA·mix를 높인다.", "$1bn/~$100m EBITDA", "financing과 integration이 통제된다.", "closing 실패·leverage 급등이면 반증.", "재협상 후 완료.", "성공", "deal option과 원계약 가격을 분리한다."),("double-digit FCF yield", "$223m FCF가 equity 하방을 지지한다.", "$2bn market cap", "working capital·floorplan을 정상화한다.", "FCF burn·liquidity squeeze면 반증.", "단기 path는 위험, 연간 cash engine 생존.", "성공/경로 위험", "cyclical FCF에는 liquidity stress를 붙인다."),("franchise scarcity", "dealer rights와 luxury mix는 희소자산이다.", "OEM territorial franchises", "DTC/EV가 economics를 빠르게 우회하지 않는다.", "OEM termination·direct share 급증이면 반증.", "후속 consolidation 지속.", "성공", "법적 moat를 service/used/F&I cash로 검증한다."),("Long direction", "10x 미만 EPS에서 common upside가 크다.", "$11 downside EPS", "severe state에서도 생존한다.", "12개월 liquidity 부족이면 반증.", "raw Short→Long 교정.", "방향 성공", "valuation과 path solvency를 각각 승인한다.")]),

I(id="3f24c47a-f169-4acb-a525-a019619af0a7", date="2020-09-10", author="regency435", ticker="ABG", entity="Asbury Automotive Group, Inc.", group="abg57", raw_short=True, direction="Long", entry="약 8.5x 2021E EPS", horizon="12~24개월", filename="analysis/ideas/2020/2020-09-10_ABG_long.md", link="https://www.valueinvestorsclub.com/idea/ASBURY_AUTOMOTIVE_GROUP_INC/2732715678", desc=0, cat=19,
title="COVID stress-test 통과 후 8.5x EPS Long", verdict="운영·valuation thesis 강한 성공·exact return 미검증", score=9.1, process=9.2,
summary="COVID를 예측하지 않고 실제 stress에서 P&S·variable SG&A·inventory economics가 버틴 뒤 약 8.5x 2021E EPS에 산 Long이다. ex-Park Place 약 $10.50와 accretion 약 $2.50을 합친 2021E EPS 약 $13이 핵심이었다.",
valuation="2019 EPS 약 $9.46, 2020 pre-Park Place 약 $9.30, 2021 ex-deal 약 $10.50+Park Place $2.50=$13을 약 8.5x에 샀다. 2020 full-year adjusted EPS $12.90은 원문의 normalized bridge가 과하지 않았음을 보여줬고 Q4 SG&A/gross profit 61.4%, operating margin 6.0%가 cost structure를 확인했다.",
actual="2020 revenue는 약 $7.1bn으로 1% 감소했지만 adjusted EPS는 $12.90으로 약 36% 증가했다. liquidity 약 $462m, pro forma net leverage 약 2.1x였고 Park Place를 완료했다. 실제 위기를 통과한 정보의 질과 아직 낮은 multiple의 조합이 좋았다.",
price="현재 SQL에는 catalyst 19자만 있고 description·performance COPY는 없다. 8.5x·$13·$2.50은 valuation anchor이며 legacy price series를 exact return으로 쓰지 않는다.",
drivers="핵심은 바닥 가격이 아니라 uncertainty가 크게 줄었는데 multiple은 여전히 낮았다는 점이다. inventory scarcity가 GPU를 올리고 variable SG&A가 margin을 지켰으며 Park Place accretion이 EPS denominator를 확대했다.",
error="inventory scarcity GPU가 얼마나 정상화될지와 Park Place integration 비용을 낙관적으로 둘 위험은 남았다. 2021E $13을 peak와 normalized로 분리하고 supply recovery·floorplan rate 상승 시나리오를 더 명시했어야 한다.", first_signal="new/used GPU가 정상화되는데 P&S growth와 SG&A leverage가 이를 상쇄하지 못하거나 pro forma net leverage가 3x를 넘으면 $13 normalized EPS를 하향한다.",
metrics=[("2021E EPS", "$13", "multiple 8.5x", "2020 adj. $12.90", "강한 검증"),("Park Place accretion", "$2.50/share", "integration", "deal 완료", "성공"),("2020 revenue", "2019 약 $7.2bn", "resilience", "$7.1bn·-1%", "성공"),("Q4 SG&A/GP", "cost-flex thesis", "낮은 ratio", "61.4%", "성공"),("Liquidity/leverage", "$462m / 2.1x", "safe runway", "stress 통과", "성공")],
timeline=[("2020-03", "COVID shutdown", "실제 stress"),("2020-Q2", "inventory·cost reset", "first evidence"),("2020-09-10", "VIC Long", "8.5x 2021E"),("2020-H2", "Park Place 완료", "$2.50 accretion"),("2020-Q4", "margin 6.0%", "cost model 검증"),("2020-FY", "adjusted EPS $12.90", "earnings proof"),("2021", "Clicklane·scale plan", "후속 growth option")],
claimdata=[("observed stress resilience", "COVID가 dealer quality를 입증했다.", "P&S·GPU·cost flex의 실제 분기", "정책지원 종료 뒤에도 유지된다.", "현금 burn 재발이면 반증.", "2020 연간 EPS 증가.", "강한 성공", "불확실성 감소 자체가 edge다."),("$13 EPS bridge", "$10.50 core+$2.50 Park Place다.", "post-stress run-rate", "GPU와 SG&A가 급반전하지 않는다.", "bridge가 두 분기 연속 $13 run-rate 미달이면 반증.", "$12.90 연간 adj. EPS로 근접.", "성공", "core와 deal accretion을 분리한다."),("P&S durability", "60%+ margin service가 downside를 막는다.", "installed base·repair need", "pandemic 지연수요가 사라져도 유지된다.", "same-store P&S GP 하락이면 반증.", "후속 성장 지속.", "성공", "service gross profit이 dealer quality 지표다."),("inventory scarcity", "낮은 inventory가 discount를 줄여 GPU를 높인다.", "2020 production constraints", "volume 손실보다 GPU 이익이 크다.", "supply 정상화와 GPU 급락이면 반증.", "2020 margin 확대.", "성공/일시적", "temporary tailwind를 normalized EPS에서 뺀다."),("Park Place quality", "luxury mix가 P&S와 multiple을 높인다.", "Lexus·Mercedes 등 portfolio", "integration과 leverage가 안정적이다.", "same-store margin 악화면 반증.", "deal·실적에 기여.", "성공", "M&A quality는 post-close cohort로 본다."),("8.5x rerating", "확인된 quality에 multiple이 낮다.", "$13×8.5x", "earnings 정상화가 급격하지 않다.", "EPS peak 판정 시 multiple thesis 제거.", "사업/valuation 방향 성공.", "성공/수익 미검증", "낮은 multiple은 stress proof 뒤 더 강하다.")]),

I(id="4745376b-0493-4ee0-a237-312c75b950e1", date="2021-09-16", author="Cupmachine314", ticker="ABG", entity="Asbury Automotive Group, Inc.", group="abg57", raw_short=True, direction="Long", entry="pullback / 원문 $360 target", horizon="2025년", filename="analysis/ideas/2021/2021-09-16_ABG_long.md", link=None, desc=0, cat=130,
title="$20bn scale·Clicklane·real estate rerating Long", verdict="scale execution 부분 성공·$20bn/$360 target 미달", score=6.8, process=8.0,
summary="best-run dealer, Clicklane, owned real estate와 M&A runway를 묶어 2025 revenue 약 $20bn·normalized EPS $33, margin 유지 시 $43을 제시한 Long이다. 11x $33으로 $360, rerating 없는 8.5x로 약 $280을 기대했으나 scale은 커졌어도 target과 rerating은 완결되지 않았다.",
valuation="owned real estate gross 약 $942m에서 mortgage 약 $512.7m을 빼 net 약 $430m으로 봤다. 2025 $33×11=$360, 8.5x=$280이고 margin 유지 $43은 상단이었다. M&A price, financing, share count, GPU normalization과 real-estate 세금/lease cost를 한 bridge로 연결해야 한다.",
actual="게시 직후 발표된 Larry H. Miller/TCA 약 $3.48bn 거래는 54 new dealerships, 7 used locations, 11 collision centers와 약 $5.7bn annual revenue를 더했다. 2022 revenue는 약 $15.4bn, 2025는 약 $18.0bn으로 커졌지만 원문 $20bn에 미달했다. 운영 scale은 성공했으나 $360 price/11x rerating은 별도 성공으로 볼 수 없다.",
price="현재 SQL에는 catalyst 130자만 있고 description·performance COPY는 없다. legacy 1년 price path와 $360 도달 여부를 exact return으로 쓰지 않는다. 원 entry close·배당·share changes가 없어 return/IRR은 null이다.",
drivers="회사는 대형 M&A를 실제로 실행해 revenue와 P&S base를 키웠다. 그러나 deal scale만큼 debt·integration·GPU normalization이 common per-share earnings와 multiple을 제한했다. 좋은 roll-up execution과 좋은 stock payoff는 다르다.",
error="management scale plan을 organic·acquired revenue와 per-share FCF로 충분히 분해하지 않았다. $430m real estate를 full value에 가깝게 더하고 $33/$43 EPS에 11x rerating까지 겹쳐 double counting 위험이 있었다.", first_signal="대형 인수 후 pro forma leverage와 interest가 오르고 acquired same-store margins·P&S growth가 core를 밑돌거나 2025 revenue run-rate가 $20bn에서 10% 이상 이탈하면 $360 target을 제거한다.",
metrics=[("2025 revenue", "$20bn", "scale target", "약 $18.0bn", "미달"),("Normalized EPS", "$33 / margin-hold $43", "11x", "peak-normalization 부담", "부분/미검증"),("Target", "$280/$360", "2025", "exact path 없음", "미검증/미달"),("Owned RE net", "$942m-$512.7m=$430m", "downside/SOTP", "세금·lease haircut 필요", "부분"),("LHM/TCA", "$3.48bn·$5.7bn revenue", "scale accretion", "거래 완료", "성공")],
timeline=[("2021-09-16", "VIC Long", "$20bn/$360 framework"),("2021-09-29", "LHM/TCA 발표", "scale catalyst"),("2021-12", "대형 거래 완료", "integration 시작"),("2022", "revenue 약 $15.4bn", "scale 진전"),("2023-2024", "GPU 정상화·금리 부담", "EPS/multiple 압박"),("2025", "revenue 약 $18.0bn", "$20bn 미달"),("2026", "2025 10-K", "cash-flow durability 재검증")],
claimdata=[("M&A runway", "fragmented dealer 시장에서 accretive roll-up이 가능하다.", "운영 track record·capital access", "deal multiple·integration·funding이 통제된다.", "acquired ROIC<WACC이면 반증.", "LHM/TCA로 scale 급증.", "성공", "deal 수보다 per-share ROIC를 본다."),("$20bn revenue", "2025까지 revenue scale이 크게 확대된다.", "management plan·pipeline", "vehicle mix와 acquisition close가 지속된다.", "run-rate 10% 이상 미달이면 반증.", "2025 약 $18bn.", "부분/미달", "scale target을 organic/M&A로 분해한다."),("$33 normalized EPS", "GPU 정상화 후에도 $33이 가능하다.", "P&S·F&I·scale synergy", "금리·debt·share count가 상쇄하지 않는다.", "normalized FCF/share가 후퇴하면 반증.", "사업은 강하나 지속성 부담.", "부분", "peak EPS를 mid-cycle FCF로 교차검증한다."),("Clicklane", "digital funnel이 share와 효율을 높인다.", "온라인 구매 플랫폼", "CAC·conversion·omnichannel 비용이 우수하다.", "digital volume 성장에도 margin 저하 시 반증.", "전략은 유지됐으나 독립 성과 제한.", "미검증", "digital label보다 funnel unit economics다."),("real estate buffer", "net $430m owned RE가 하방을 지지한다.", "gross $942m·mortgage $512.7m", "매각가·세금·leaseback이 유리하다.", "net proceeds가 추정치 크게 하회하면 반증.", "숨은 자산은 남지만 즉시 cash 아님.", "부분", "real estate는 after-tax net proceeds로 본다."),("11x rerating", "best operator에 $360이 정당하다.", "$33×11", "cycle peak 인식과 leverage가 해소된다.", "multiple이 8.5x 아래에 머물면 반증.", "rerating target은 완결되지 않음.", "실패에 가까움", "좋은 기업과 좋은 multiple을 분리한다.")]),

I(id="76a8daa6-36fa-4fae-9f64-61f416033010", date="2022-09-26", author="cubbie", ticker="ABG", entity="Asbury Automotive Group, Inc.", group="abg57", raw_short=False, direction="Long", entry="normalized FCF $30~50/share의 약 3~5x", horizon="5~10년", filename="analysis/ideas/2022/2022-09-26_ABG_long.md", link=None, desc=0, cat=56,
title="dealer terminal-value fear·normalized FCF Long", verdict="durability 확인·revenue target 미달·장기 horizon 진행 중", score=7.8, process=8.7,
summary="peak GPU 정상화와 EV direct-to-consumer가 dealer terminal value를 파괴한다는 공포에 맞서 P&S·F&I·used·trade-in·financing 기능을 산 Long이다. normalized FCF $30~50/share에 주가가 약 3~5x라고 봤고, 보수적 2025 revenue $20bn을 사용했지만 horizon은 5~10년이다.",
valuation="normal FCF를 $30~50/share로 넓게 두고 낮은 3~5x를 제시했다. 이 범위는 new/used GPU 정상화, P&S growth, F&I/unit, interest, acquisition capex와 share repurchase를 분리해야 한다. $20bn revenue는 management의 더 높은 plan보다 보수적이지만 실제 2025 약 $18bn보다 높았다.",
actual="2025 revenue는 약 $18bn으로 5% 증가했고 adjusted operating cash flow는 약 $651.4m, net income은 $492m이었다. P&S gross profit은 9% 늘었지만 new-vehicle gross profit은 3% 감소하고 same-store new GPU는 11% 줄었다. dealer cash engine은 유지됐으나 $20bn target은 미달했고 장기 horizon은 진행 중이다.",
price="현재 SQL에는 catalyst 56자만 있고 description·performance COPY는 없다. 3~5x와 $30~50/share는 원문 valuation framing이며 exact 1/3/5년 return은 null이다. 2025 operating results는 기업 thesis 검증이지 total return이 아니다.",
drivers="terminal collapse는 아직 나타나지 않았다. new GPU가 정상화되는 동안 P&S와 규모가 gross profit을 받쳤고 cash generation이 지속됐다. 다만 acquisition-funded scale과 금리, vehicle affordability가 per-share FCF 상단을 제한한다.",
error="EV disruption을 너무 binary하게 반박할 위험과 $30~50 FCF 범위가 넓다는 약점이 있다. maintenance capex, acquisition spend, working-capital reversal과 debt paydown을 분리한 owner FCF가 필요하다.", first_signal="same-store P&S gross profit이 감소하면서 EV mix가 높은 지역의 service retention·F&I/unit·trade-in capture가 동시에 악화하면 franchise terminal thesis를 하향한다. net leverage 상승 시 buyback accretion도 제거한다.",
metrics=[("Normalized FCF/share", "$30~50", "3~5x", "기업 OCF 유지", "방향 성공/정확치 미검증"),("2025 revenue", "$20bn 보수 case", "scale", "약 $18bn", "미달"),("2025 adj. OCF", "T0 미관찰", "durable cash", "$651.4m", "성공"),("P&S gross profit", "terminal defense", "성장", "2025 +9%", "성공"),("New vehicle GP/GPU", "정상화 우려", "manageable", "GP -3% / SS GPU -11%", "우려 일부 현실화")],
timeline=[("2021-2022", "record GPU", "peak fear"),("2022-09-26", "VIC Long", "3~5x normalized FCF"),("2023", "inventory 정상화", "GPU 압박 시작"),("2024", "금리·affordability 부담", "cash-flow test"),("2025", "revenue 약 $18bn", "$20bn 미달"),("2025", "P&S GP +9%", "terminal defense"),("2026-02", "2025 results/10-K", "5~10년 horizon 진행")],
claimdata=[("dealer function persists", "EV 시대에도 delivery·trade-in·finance·used 기능이 남는다.", "OEM/local franchise economics", "OEM이 모든 기능을 더 싸게 내재화하지 못한다.", "direct share 상승과 dealer take-rate 급락이면 반증.", "2025까지 terminal collapse 없음.", "성공/진행", "법적 moat보다 고객기능의 비용을 본다."),("P&S durability", "EV에서도 tires·collision·warranty·diagnostics가 남는다.", "installed base·service network", "ICE maintenance 감소를 다른 service가 상쇄한다.", "EV cohort service revenue가 구조적으로 급락하면 반증.", "2025 P&S GP +9%.", "성공", "powertrain별 service cohort를 추적한다."),("GPU normalization manageable", "peak new/used GPU가 내려가도 FCF는 견딘다.", "P&S/F&I·variable SG&A", "volume·cost가 일부 상쇄한다.", "GPU 하락이 owner FCF를 크게 훼손하면 반증.", "new GPU -11%, 기업 cash는 유지.", "성공/부분", "peak profit을 segment bridge로 정상화한다."),("consolidation", "fragmented 시장에서 scale과 buyback이 per-share value를 높인다.", "ABG capital allocation history", "deal ROIC와 leverage가 disciplined하다.", "debt-funded growth가 FCF/share를 낮추면 반증.", "scale 확대·금리 부담 병존.", "혼합", "revenue보다 post-deal FCF/share다."),("$20bn revenue", "보수적으로도 2025 $20bn이 가능하다.", "footprint·acquisition runway", "industry volume과 close가 뒷받침된다.", "2025 10% 이상 미달이면 반증.", "약 $18bn.", "미달", "보수적이라는 라벨도 actual로 검증한다."),("3~5x FCF", "$30~50/share에 terminal fear가 과도하다.", "낮은 implied multiple", "owner FCF 범위가 실제 반복 가능하다.", "maintenance/M&A capex 후 FCF가 하단 미달이면 반증.", "cash engine은 유지, 정확 per-share 미복원.", "방향 성공/진행", "wide range는 driver별 확률로 좁힌다.")]),

I(id="4f0b8933-884b-4a25-8745-3167b865945f", date="2012-07-15", author="leverage", ticker="ADES", entity="ADA-ES, Inc. / Advanced Emissions Solutions, Inc.", group="ades57", raw_short=False, direction="Long", entry="원문 SOTP $60~85+ pre-split", horizon="2014~2021", filename="analysis/ideas/2012/2012-07-15_ADES_long.md", link="https://www.valueinvestorsclub.com/idea/ADA-ES_INC/0117855876", desc=0, cat=390,
title="Section 45 refined-coal distribution·MATS SOTP Long", verdict="현금분배 논지 성공·governance/security path 혼합", score=7.4, process=8.2, security="Common stock / indirect JV distribution residual",
waterfall="tax monetizer가 적격 tonnage의 Section 45 credit을 사용한 뒤 계약상 payment와 JV operating cost를 반영하고 Tinuum Group 42.5%·Tinuum Services 50% 지분에 따라 분배한다. 여기서 본사비·세금·debt·재투자와 governance leakage를 차감한 현금만 common에 귀속된다. 2014 split과 이후 distributions도 total-return bridge에 포함해야 한다.",
summary="MATS가 ACI/DSI 장비 수요를 만들고, 더 중요한 Section 45 refined-coal JV가 2012 약 $6.47/ton credit을 monetizer와 나눠 ADA에 약 $1.50~1.70/ton cash를 준다는 Long이다. 2014 이후 실제 분배금은 커졌지만 reporting·internal-control failure가 security path를 훼손했다.",
valuation="원문 refined-coal run-rate cash는 2012 $30m, 2013 $80m, 2014 이후 $94m이고 15% DCF NPV는 약 $404m이었다. emission-control을 더한 SOTP는 pre-split $60~85+ 범위다. 핵심은 credit expiry, tonnage ramp, monetizer 계약·세금, JV ownership과 본사 cash conversion이다.",
actual="Tinuum 분배금은 2013 $13.8m, 2014 $43.6m로 커졌고 후년에도 수천만 달러가 이어졌다. 2019에는 회사 발표 기준 Tinuum distributions $73.9m과 royalties $16.9m이었다. Section 45 refined-coal operations는 2021-12-31 종료됐다. 그러나 SEC는 2011~14 reporting/internal-control failures와 material misstatements를 지적했고 filing 지연·restatement가 valuation realization을 훼손했다.",
price="현재 SQL에는 catalyst 390자만 있고 description·performance COPY는 없다. 2014 2-for-1 split, distributions, successor company와 정확 price path를 연결하지 않았으므로 total return/IRR은 null이다. 분배금의 실재를 common return으로 대체하지 않는다.",
drivers="경제적 성공은 법정 만기가 있는 tax credit와 실제 tonnage/distribution 계약이 만들었다. security의 혼합 결과는 회계·통제 실패, 보고 지연과 받은 현금의 자본배분에서 왔다. special situation에서는 cash entitlement와 그것을 소유한 상장 wrapper의 governance를 따로 심사해야 한다.",
error="세제·환경규정과 tonnage economics는 깊었지만 accounting close, internal control, auditor·filing capacity와 JV cash-to-parent reconciliation을 별도 핵심 claim으로 두지 않았다. 15% discount rate도 governance tail과 시설별 ramp/expiry를 충분히 반영하지 못했다.", first_signal="분기별 qualified tonnage와 cash distributions가 모델에서 15% 이상 이탈하거나 auditor 교체·filing 지연·material weakness가 나타나면 NPV보다 먼저 governance haircut과 position limit을 적용한다.",
metrics=[("2012 credit", "$6.47/ton", "inflation-adjusted cash pool", "2021까지 제도 운영", "성공"),("ADA economics", "$1.50~1.70/ton", "facility ramp", "실제 대규모 distributions", "성공 방향"),("Run-rate cash", "$30m/$80m/$94m", "2012/13/14+", "2013 $13.8m·2014 $43.6m", "ramp 과대/방향 성공"),("RC NPV", "$404m @15%", "SOTP $60~85+", "governance discount 발생", "혼합"),("2019 distributions/royalties", "T0 미관찰", "지속 cash", "$73.9m/$16.9m", "강한 경제 검증")],
timeline=[("2012-07-15", "VIC Long", "RC+MATS SOTP"),("2013", "Tinuum distributions $13.8m", "cash ramp 시작"),("2014", "distributions $43.6m·2:1 split", "경제성/보안 bridge"),("2015-2016", "restatement·filing 지연", "governance 반증"),("2017-03", "SEC cease-and-desist order", "통제 실패 확인"),("2019", "distributions $73.9m", "cash thesis 검증"),("2021-12-31", "refined-coal credit 종료", "asset expiry")],
claimdata=[("Section 45 cash engine", "적격 tonnage가 반복 cash distributions를 만든다.", "$6.47/ton credit·ADA $1.50~1.70 economics", "배출감축·monetizer·facility eligibility가 유지된다.", "qualified tons·cash가 15% 이상 미달이면 반증.", "후년 수천만 달러 분배.", "강한 성공", "세제 asset은 contract-to-cash로 모델링한다."),("facility ramp", "17개에서 28개로 ramp해 $94m run-rate가 된다.", "JV pipeline·qualified facilities", "각 facility close와 tonnage가 일정대로 온다.", "2013/14 cash가 model 크게 미달하면 하향.", "2013 $13.8m·2014 $43.6m로 원문보다 느림.", "방향 성공/속도 미달", "시설별 확률·날짜를 합산한다."),("MATS equipment", "MATS가 ACI/DSI retrofit 수요를 만든다.", "규제 compliance deadline·system 가격", "coal plants가 retrofit을 선택한다.", "폐쇄·대체 compliance가 주문을 줄이면 반증.", "장비보다 RC가 가치 실현을 주도.", "부분", "규제 TAM을 실제 order/backlog로 좁힌다."),("$404m NPV", "15% 할인해도 RC가 시총 대비 크다.", "$30/$80/$94m cash schedule", "tax·parent leakage·governance가 제한적이다.", "restatement·cash reconciliation failure면 haircut.", "cash는 실재했으나 governance discount 발생.", "혼합", "contract NPV와 wrapper discount를 분리한다."),("governance adequate", "경제성이 common에 정상 귀속된다.", "공시 JV ownership·계약", "internal control과 filing이 신뢰 가능하다.", "material weakness·지연이면 반증.", "2011~14 material misstatement·통제 실패.", "실패", "special situation에도 accounting claim을 필수화한다."),("expiry-aware SOTP", "2021 만기 전 현금과 장비를 합치면 $60~85+다.", "법정 credit 기간", "분배·split·재투자를 common이 보존한다.", "capital leakage·후속 사업 손실이면 반증.", "cash distribution 성공, security path 혼합.", "혼합", "만기 자산은 distribution calendar로 평가한다.")]),
]


def idea_sources(idea):
    status = f"description {idea['desc']} chars" if idea["desc"] else "description absent"
    raw = m.S(
        "첨부 SQL 원문/metadata",
        idea["link"],
        "VIC_IDEAS(4).sql / VIC",
        idea["date"],
        f"idea_id·raw {'Short' if idea['raw_short'] else 'Long'}·catalyst {idea['cat']} chars·{status}; 현재 SQL에 없는 원문 수치는 lower-provenance overlay로 분리",
        "원문/metadata",
    )
    return [raw, *m.SOURCES[idea["group"]]]


def report(idea):
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        text = m.report(idea)
    finally:
        m.idea_sources = old
    generic = (
        "회계이익에서 운전자본·담보·규제자본·maintenance/growth investment·interest·tax를 차감하고, common보다 선순위인 계약·채권자 청구권을 먼저 배치한다. "
        "자산가치와 계약상 수취액은 현금화 날짜·세금·재투자 의무를 반영한다. 기업가치가 맞아도 security와 duration이 틀리면 투자결과는 실패할 수 있다."
    )
    desc_note = (
        f"첨부 SQL description {idea['desc']:,}자와 catalyst {idea['cat']:,}자를 직접 확인했다."
        if idea["desc"] else
        f"첨부 SQL에는 catalyst {idea['cat']:,}자만 있고 description은 없다. 원문 수치는 prior curated overlay로 provenance를 분리했다."
    )
    text = text.replace("Batch 046 canonical report.", "Batch 057 canonical report.")
    text = text.replace("### Common equity cash waterfall", "### Security cash waterfall")
    text = text.replace(generic, idea["waterfall"])
    text = text.replace(
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |",
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |\n| 실제 Security | **{idea['security']}** |",
    )
    text = text.replace(
        f"`ATH`를 회사로 보지 말고 {idea['entity']} 법인·exchange·날짜로 고정한다.",
        f"`{idea['ticker']}`를 단일 회사명으로 보지 말고 {idea['entity']} 법인·날짜·security로 고정한다.",
    )
    text = text.replace(
        "원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.",
        f"원문·metadata: **{'A/B' if idea['desc'] else 'C'}** — {desc_note}",
    )
    text = text.replace(
        "기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.",
        "기업·사건: **A/B** — SEC·회사·정부기관 자료로 operating·capital·regulatory event를 교차검증했다.",
    )
    text = text.replace(
        "가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
        "가격성과: **C** — 현재 SQL에 performance COPY가 없다. legacy ABG 수치와 WTW ticker 오염값을 폐기했고 corporate event를 exact return으로 바꾸지 않았다.",
    )
    return text


def payload():
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(IDEAS)
    finally:
        m.idea_sources = old
    out["batch"] = 57
    out["title"] = "Weight Watchers / Asbury / ADA-ES — Security Selection, Stress Evidence and Expiring Cash Claims V9"
    null_keys = (
        "perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y",
        "idea_return_1y", "idea_return_3y", "idea_return_5y",
    )
    for idea, master, post in zip(IDEAS, out["ideas_master"], out["postmortems"]):
        master["security_ko"] = idea["security"]
        master["performance_available"] = 0
        master["auto_tag_status_ko"] = "current SQL catalyst 감사·direction/security 수동교정·legacy performance 폐기·exact return null"
        for key in null_keys:
            master[key] = None
        post["research_direction_ko"] = f"{idea['direction']} / {idea['security']}"
        post["research_status_ko"] = "SQL 원문 provenance·공식 filings 검증; performance COPY 부재로 exact return null"
        post["confidence"] = 0.95 if idea["desc"] else (0.91 if idea["link"] else 0.85)
    return out


def make_index():
    rows = []
    for n, idea in enumerate(IDEAS, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['ticker']} | {raw}→**{idea['direction']}** | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 057 — Weight Watchers / Asbury / ADA-ES — V9 Index", "",
        f"> Research as-of {ASOF}. 10 idea = 10 canonical reports다. 현재 SQL에는 catalyst 10건과 description 3건만 있고 performance COPY는 없다. 실제 방향은 Long 9건과 capital-structure Pair 1건이다.", "",
        "## 0. 배치 결론", "",
        "이 배치의 공통점은 회사 이름이 아니라 **어떤 현금흐름을 어느 security로 소유하는가**가 결과를 갈랐다는 점이다. WTW B-1 loan은 같은 회사 common보다 먼저 cash를 받았고, ABG의 공포는 vehicle revenue보다 P&S/F&I와 관찰된 stress evidence로 판단해야 했으며, ADES의 refined-coal cash는 만기와 governance를 가진 계약 claim이었다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | Ticker | raw→연구 방향 | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|", *rows, "",
        "## 2. SQL·Direction·Security·Performance Audit", "",
        "첨부 `VIC_IDEAS(4).sql`의 COPY table은 catalyst·companies·descriptions뿐이다. catalyst 10건은 모두 확인했고 description은 WTW 2015-05 32,273자, WTW 2015-11 11,268자, ABG 2010 13,914자만 있다. raw Short→Long 단순 direction correction은 7건이다. WTW 2015-05는 단순 correction이 아니라 common Short+B-1 Long의 Pair/security correction이다. ABG 2022와 ADES는 raw Long이 맞다.", "",
        "현재 attachment가 controls다. legacy overlay의 performance_available 9건을 모두 nullified했고, 그중 ABG numeric series 6건과 WTW ticker-reuse contamination flag 3건을 폐기했다. 따라서 정확한 1/3/5년 return, pair return과 IRR은 모두 null이다.", "",
        "## 3. Weight Watchers — operating view보다 security map", "",
        "2015-05 pair는 $301m cash+$50m revolver와 짧은 maturity를 근거로 B-1을 정확히 골랐지만, 그 상환가능성을 높이는 rescue가 common도 살릴 수 있다는 cross-catalyst를 놓쳤다. 2015-11 Long은 Oprah×subscriber operating leverage를 맞혔으나 YE2016 clock이 빨랐다. 2018 Long은 retention을 맞혔어도 gross additions·marketing miss가 revenue와 주가를 결정했다.", "",
        "## 4. Asbury — 예측한 floor보다 관찰된 stress", "",
        "2008 Long은 P&S/F&I 구조를 맞히고도 14m SAAR floor를 틀렸다. 2010 Long은 실제 10m대 SAAR에서 흑자로 돌아온 cost base를 관찰해 훨씬 강했다. 2020-02는 같은 economics를 사면서 COVID path를 겪었고, 2020-09는 stress가 이미 통과된 뒤 8.5x에 사 정보의 질이 가장 좋았다. 2021은 scale과 rerating을 겹쳐 target이 과했고, 2022는 terminal fear와 normalized FCF에 집중해 더 견고했지만 5~10년 horizon은 진행 중이다.", "",
        "## 5. ADA-ES — cash entitlement와 상장 wrapper", "",
        "Section 45 tonnage와 Tinuum distributions는 실재했고 2019 회사 발표상 distributions $73.9m, royalties $16.9m까지 확대됐다. 하지만 2011~14 material misstatement·internal-control failure와 filing 지연은 좋은 세제 economics를 나쁜 security path로 바꿀 수 있음을 보여줬다. 2021-12-31 만료가 정해진 asset은 terminal multiple보다 distribution calendar로 평가해야 한다.", "",
        "## 6. 투자논지 재사용 규칙", "",
        "1. 자본구조마다 maturity·priority·catalyst를 별도 claim으로 쓴다.\n2. pair trade는 각 leg뿐 아니라 두 leg를 동시에 움직이는 rescue catalyst를 stress한다.\n3. subscriber는 gross additions와 churn/retention을 분리한다.\n4. macro floor를 예측하기보다 실제 stress에서 비용·liquidity 반응을 관찰한다.\n5. dealer revenue가 아니라 P&S·F&I·SG&A와 owner FCF를 본다.\n6. M&A revenue와 per-share FCF accretion을 구분한다.\n7. 세제 cash claim은 eligibility·contract·JV·expiry·parent distribution 순으로 추적한다.\n8. NPV와 상장 wrapper의 accounting/governance discount를 분리한다.\n9. corporate event와 operating success는 exact return이 아니다.\n10. performance table이 없으면 수익률은 null이다.", "",
        "## 7. 산출물", "",
        "- Payload: `data/curated/batch_057_wtw_abg_ades_deep_v7.json`\n- Wrapper: `analysis/batch_057_wtw_abg_ades_10.md`\n- Source packet: `data/curated/batch_057_source_packet.json`\n- SQL inventory: `data/curated/batch_057_sql_inventory.json`\n- Builder: `scripts/57_build_batch_057_v9.py`", "",
        "## 8. 검증 기준", "",
        "각 보고서는 0~12절, 6 weighted claims/100%, 5 metrics, 최소 6 timeline events와 원문 provenance+공식자료를 포함한다. Payload·문서·앱 popup의 idea_id, entity, direction, security와 verdict를 동일하게 유지한다.", "",
    ])


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 057 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or len(idea_sources(idea)) < 5:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(idea["filename"]).relative_to("analysis").as_posix() for idea in IDEAS]
    wrapper = "# Batch 057 — Weight Watchers / Asbury / ADA-ES V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit wrapper. [Batch 057 V9 Index](batch_057_v9_index.md).\n"
    (ROOT / "analysis/batch_057_wtw_abg_ades_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_057_v9_index.md").write_text(make_index(), encoding="utf-8")
    out = payload()
    (ROOT / "data/curated/batch_057_wtw_abg_ades_deep_v7.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {
        "batch": "057", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + prior curated overlay + official filings",
        "record_count": 10, "raw_descriptions_present": 3, "raw_catalysts_verified": 10,
        "current_attachment_performance_rows_found": 0, "legacy_overlay_performance_flags_nullified": 9,
        "legacy_overlay_numeric_series_discarded": 6, "wtw_ticker_contamination_flags_nullified": 3,
        "direction_corrections": 7, "entity_corrections": 0, "security_type_corrections": 1, "security_normalizations": 10,
        "performance_rule": "No performance COPY in current attachment; all exact returns and IRRs remain null",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"],
            "raw_direction": "Short" if i["raw_short"] else "Long", "research_direction": i["direction"], "security": i["security"],
            "description_chars": i["desc"], "catalyst_chars": i["cat"], "performance_available": False,
            "canonical_report": i["filename"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_057_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10,
        "copy_tables_present": ["catalyst", "companies", "descriptions"], "idea_rows_in_attachment": 0,
        "raw_descriptions_present": 3, "raw_descriptions_absent": 7, "raw_catalysts_verified": 10,
        "description_chars_by_idea": {i["id"]: i["desc"] for i in IDEAS},
        "catalyst_chars_by_idea": {i["id"]: i["cat"] for i in IDEAS},
        "performance_copy_present": False, "performance_rows_found": 0, "legacy_overlay_rows_nullified": 9,
        "legacy_numeric_series_discarded": 6, "wtw_ticker_contamination_rows": 3,
        "note": "Current attachment controls. Three descriptions and ten catalysts are present; seven descriptions and all performance are absent. Legacy performance was discarded.",
    }
    (ROOT / "data/curated/batch_057_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(out[key]) for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
