#!/usr/bin/env python3
"""Build Batch 056 Stamps.com / Weight Watchers canonical V9 artifacts."""
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
    "stmp56": (
        "Stamps.com은 USPS PC Postage에서 출발해 Endicia·ShipStation·ShipWorks·ShippingEasy·MetaPack을 묶은 shipping-software platform으로 확장했다. "
        "현금엔진은 `유료고객×subscription/transaction ARPU+carrier·insurance·supplies monetization-CAC-support·processing-R&D-G&A-capex-tax`다. "
        "2007년에는 SOHO postage 구독과 마케팅 cohort가 핵심이었지만 2016년 이후에는 e-commerce parcel volume, multi-carrier workflow, high-volume shipper와 partner economics가 더 중요했다. "
        "USPS 우편물 감소만으로 TAM을 정의하면 parcel software를 놓치고, 반대로 USPS reseller economics를 영구화하면 platform value를 과대평가한다."
    ),
    "wtw56": (
        "당시 WTW는 현재 Willis Towers Watson이 아니라 Weight Watchers International common stock이다. 회사는 대면 meetings와 digital/online 체중관리 구독을 판매했다. "
        "현금엔진은 `meeting attendance×fee+digital subscribers×ARPU-products/licensing-leader·rent·marketing·technology-corporate-interest-tax`다. "
        "meetings는 지역별 고정비와 operating leverage가 크고, online은 margin이 높지만 free apps·wearables·self-directed tracking이 소비자의 지불의사를 낮출 수 있다. "
        "큰 debt-funded tender 이후 common payoff는 EBITDA보다 attendance·digital net adds·interest coverage·borrow cost와 refinancing runway에 더 민감했다."
    ),
})

m.SOURCES.update({
    "stmp56": [
        m.S("Stamps.com SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1082923&owner=exclude", "SEC / Stamps.com", "1999-2021", "사업모델·고객·인수·USPS 관계·자본배분 연속성"),
        m.S("Stamps.com 2004 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1082923/000114420405007345/stampscom10k.htm", "SEC / Stamps.com", "2005-03", "초기 PC postage·NetStamps·고객획득 economics"),
        m.S("Stamps.com 2016 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1082923/000114036117010000/form10k.htm", "SEC / Stamps.com", "2017-03", "Endicia 포함 고객·ARPU·shipping revenue와 비용"),
        m.S("Stamps.com 2020 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1082923/000108292321000033/stmp-20201231.htm", "SEC / Stamps.com", "2021-03", "2020 revenue·paid customers·multi-carrier segment 검증"),
        m.S("Thoma Bravo acquisition release", "https://www.sec.gov/Archives/edgar/data/1082923/000114036121023931/brhc10026739_ex99-1.htm", "SEC / Stamps.com", "2021-07-09", "$330/share·약 $6.6bn terminal event"),
        m.S("USPS PC Postage", "https://postalpro.usps.com/operations/pc-postage", "U.S. Postal Service", "2000s-2026", "PC Postage 승인·운영 framework"),
    ],
    "wtw56": [
        m.S("WeightWatchers SEC archive", "https://www.sec.gov/edgar/browse/?CIK=105319&owner=exclude", "SEC / Weight Watchers", "2001-2018", "attendance·online·debt·tender·실적 공시 연속성"),
        m.S("WeightWatchers annual reports", "https://corporate.ww.com/financials/annual-reports-and-proxy/default.aspx", "WW International", "2008-2025", "2008·2013·2014 annual reports와 proxy archive"),
        m.S("WeightWatchers investor overview", "https://corporate.ww.com/overview/default.aspx", "WW International", "2000s-2026", "법인·brand·investor materials 연속성"),
        m.S("Weight Watchers 2017 proxy", "https://www.sec.gov/Archives/edgar/data/105319/000119312517107775/d264156ddef14a.htm", "SEC / Weight Watchers", "2017-04", "meetings·online 정의와 Oprah agreement·common security 확인"),
        m.S("Oprah partnership release", "https://corporate.ww.com/news/news-details/2015/Oprah-Winfrey-And-Weight-Watchers-Join-Forces-In-Groundbreaking-Partnership/default.aspx", "Weight Watchers", "2015-10-19", "10% equity investment·board role·brand catalyst"),
    ],
})


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**x):
    x["claims"] = [C(*row) for row in x.pop("claimdata")]
    x.setdefault("security", "Common stock")
    x.setdefault(
        "waterfall",
        "고객이 지급한 subscription·transaction 현금에서 고객획득·서비스·기술투자·운전자본·이자·세금을 차감하고 debt와 계약상 senior claim을 먼저 지급한 뒤의 per-share 현금만 common payoff로 본다.",
    )
    return x


IDEAS = [
I(id="827f69e9-a39a-4025-9ba2-7260fcdbc3bf", date="2007-07-03", author="thomas434", ticker="STMP", entity="Stamps.com Inc.", group="stmp56", raw_short=True, direction="Long", entry="약 $13.78", horizon="2009년", filename="analysis/ideas/2007/2007-07-03_STMP_long.md", link=None, desc=17911, cat=46,
title="marketing-as-growth-capex·NOL Long", verdict="2009 stated horizon 실패·장기 unit economics 성공·exact return 미검증", score=6.4, process=8.5,
summary="raw Short가 아니라 약 $13.78에서 고객획득 마케팅을 growth capex로 보고 cash·NOL·높은 pre-tax return과 repurchase를 산 Long이다. 2009 downside/base/upside $17.47/$23.30/$28.40은 해당 horizon에 실현되지 않았지만, 장기 shipping-software economics는 후속 성장과 2021 strategic sale로 검증됐다.",
valuation="cash 약 $104m과 NOL deferred-tax asset 약 $103m의 present value 약 $61m을 반영한 adjusted EV는 약 $137m, TTM EBIT은 약 $11m이었다. 원문은 2009 $17.47/$23.30/$28.40을 제시했지만 NOL은 과세소득·사용시점에 종속되고 marketing 자산화는 cohort payback이 유지될 때만 가능하다.",
actual="2007 매출은 종전 기대와 2007 guide를 밑돌았고 마케팅 지출은 늘어 2009 가격 시나리오가 깨졌다. 그러나 SOHO subscription과 shipping workflow는 생존했고 이후 multi-carrier platform으로 확장됐다. 2021 $330 cash transaction은 장기 사업가치의 종착점이지 2007 아이디어의 exact return은 아니다.",
price="현재 SQL에는 이 아이디어의 description 17,911자와 catalyst 46자가 있지만 performance COPY가 없다. $13.78과 원문 target은 T0 anchor일 뿐이며 배당·정확 posting close·중간 corporate action을 복원하지 않아 return/IRR은 null이다.",
drivers="단기 실패는 매출 기대와 marketing productivity가 2009 clock 안에 맞지 않은 데서 왔다. 장기 성공은 광고 자체가 아니라 유지되는 subscription cohort, low marginal fulfillment cost와 shipping use case 확대가 만들었다. 좋은 LTV/CAC와 정해진 날짜의 rerating은 별개다.",
error="marketing을 전부 growth capex로 재분류하면 성숙 cohort의 유지광고와 실패한 acquisition spend까지 자산화하게 된다. NOL PV도 earnings timing과 Section 382류 제약을 더 크게 haircut하고 2007 revenue miss를 target 확률에 반영했어야 한다.", first_signal="2007 revenue가 $87~97m guide 하단을 밑돌거나 marketing/revenue가 40%에 접근하면서 paid-customer growth·churn이 개선되지 않으면 2009 target을 폐기하고 cohort payback을 다시 계산한다.",
metrics=[("Entry/targets", "$13.78", "$17.47/$23.30/$28.40", "2009 horizon 미달", "실패"),("Cash", "약 $104m", "downside support", "운영·환원에 사용", "부분"),("NOL DTA/PV", "$103m/$61m", "과세소득으로 실현", "장기 value 일부", "부분"),("Adjusted EV/EBIT", "$137m/$11m", "operating leverage", "장기 scale", "성공 방향"),("Pre-tax ROC", "95.7%", "높은 reinvestment return", "shipping platform 확장", "성공 방향")],
timeline=[("2006", "revenue 약 $84.6m", "기준점"),("2007-07-03", "VIC Long", "$13.78·2009 targets"),("2007-FY", "revenue 기대 미달", "첫 반증"),("2008-2009", "recession·marketing 부담", "stated horizon 실패"),("2010-2011", "사업·주가 회복", "duration 연장"),("2014-2018", "shipping-software M&A", "TAM 확대"),("2021-07", "$330 cash deal", "장기 terminal event")],
claimdata=[("marketing은 growth capex", "고객획득비를 비용 처리해 earnings가 과소표시된다.", "LTV가 CAC의 2배 이상이라는 원문 cohort", "churn·gross margin·channel saturation이 안정적이다.", "payback 악화·marketing/revenue 상승 시 반증.", "2007~09에는 수익화 지연, 장기는 성장", "혼합", "marketing은 cohort별로만 자산화한다."),("subscription moat", "PC postage 시장지위와 편의성이 고객을 붙잡는다.", "약 85% online-postage subscription share 추정", "USPS·경쟁·무료대안이 churn을 높이지 않는다.", "paid churn 상승·share 하락이면 반증.", "shipping platform으로 생존·확장", "성공 방향", "share보다 retention과 workflow 깊이를 본다."),("NOL value", "$103m DTA가 숨은 자산이다.", "$270m NOL과 PV 약 $61m", "과세이익이 충분하고 사용 제약이 없다.", "소진 지연·ownership limitation이면 반증.", "장기 수익성으로 일부 가치화", "부분", "tax asset은 사용 달력으로 할인한다."),("cash floor", "$104m cash가 하방을 지지한다.", "무차입성 balance sheet", "cash가 가치파괴 없이 보존된다.", "burn·과다마케팅·비효율 환원이면 반증.", "runway와 repurchase 제공", "성공/조건부", "cash에는 use-of-cash를 붙인다."),("2009 operating leverage", "고정비 위 매출이 늘면 EBIT이 크게 증가한다.", "TTM EBIT 약 $11m·높은 ROC", "revenue guide와 margin이 실현된다.", "guide miss·CAC 상승이면 반증.", "2009 시나리오 미달", "실패", "좋은 unit economics와 horizon을 분리한다."),("Long direction", "downside보다 upside가 큰 common Long이다.", "세 개 target 모두 entry 상회", "동일 common payoff다.", "borrow/negative target이면 반증.", "raw Short→Long 교정", "성공", "방향은 action과 payoff로 확정한다.")]),

I(id="ba7b0dc3-12ed-4cf4-9b66-6cabf46aa43c", date="2008-03-07", author="rskfrarb210", ticker="STMP", entity="Stamps.com Inc.", group="stmp56", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="2~4년", filename="analysis/ideas/2008/2008-03-07_STMP_long.md", link="https://www.valueinvestorsclub.com/idea/Stamps.com/8715706478", desc=0, cat=63,
title="expectation reset·10.5x FCF Long", verdict="단기 정체 후 장기 회복·정확 수익률 미검증", score=7.2, process=8.7,
summary="raw Short가 아니라 2007 실적 미달과 marketing 과투자를 인정한 뒤 EV 약 $91.5m, TTM FCF 약 $8.7m·10.5x에서 재심사한 Long이다. NOL, insider buying과 repurchase가 기다릴 수 있는 구조를 만들었고, 단기 회복은 늦었지만 장기 business recovery는 맞았다.",
valuation="EV/TTM FCF 약 10.5x는 성장 기대가 거의 없는 가격이었다. 2007 revenue 약 $85m은 종전 약 $95m 기대를 밑돌고 marketing은 약 $27m에서 $33m, revenue 대비 33%에서 39%로 늘었다. 정상화 FCF를 쓰려면 marketing 유지비와 growth acquisition을 분리하고 NOL·cash의 사용가치를 별도 bridge해야 한다.",
actual="2008~09에는 recession과 약한 고객획득으로 빠른 rerating이 없었다. 이후 business는 회복하고 shipping use case가 성장해 2010년대 platform으로 확대됐다. 이전 thesis가 틀린 사실을 인정한 더 낮은 expectation과 entry가 새 투자논지를 만들었다.",
price="현재 SQL에는 catalyst 63자만 있고 description·performance COPY는 없다. EV $91.5m와 FCF $8.7m은 valuation anchor이며 exact 1/3/5년 return과 IRR은 null이다.",
drivers="결과 차이는 entry expectation과 duration에서 나왔다. 2007 bull case를 반복한 것이 아니라 revenue miss와 marketing burden을 새 base로 낮췄다. cash·NOL은 시간을 샀고 후속 shipping TAM이 장기 payoff를 만들었다.",
error="10.5x trailing FCF가 싸다는 결론은 churn과 acquisition productivity가 더 나빠지지 않는다는 전제에 민감하다. insider buying과 repurchase도 정보 edge라기보다 capital-allocation evidence로만 제한했어야 한다.", first_signal="두 분기 연속 marketing/revenue가 40%를 넘는데 paid customers·ARPU가 성장하지 않거나 TTM FCF가 $6m 아래로 내려가면 cheap multiple이 아니라 melting cash flow로 재분류한다.",
metrics=[("Revenue", "약 $85m", "종전 기대 약 $95m", "expectation reset", "실패 반영"),("Marketing", "$27m→$33m", "효율 정상화", "단기 부담", "혼합"),("Marketing/revenue", "33%→39%", "하락", "빠른 개선 부재", "부분 실패"),("TTM FCF", "$8.7m", "보존·성장", "장기 회복", "성공 방향"),("EV/FCF", "$91.5m/10.5x", "rerating", "장기 multiple 회복", "성공 방향")],
timeline=[("2007-07", "선행 Long", "높은 2009 기대"),("2007-FY", "revenue miss·marketing 증가", "thesis reset"),("2008-03-07", "VIC Long", "10.5x FCF"),("2008-2009", "recession·정체", "horizon 압박"),("2010-2011", "사업 회복", "장기 thesis 전개"),("2014-2018", "shipping M&A", "TAM 재정의"),("2021", "$330 cash deal", "terminal value")],
claimdata=[("expectation reset", "2007 실패가 가격에 과도하게 반영됐다.", "$85m revenue와 낮아진 EV", "추가 하향이 제한적이다.", "revenue·FCF 재차 급락이면 반증.", "단기 약세 뒤 장기 회복", "성공/지연", "같은 회사도 새 expectation이면 새 투자다."),("10.5x FCF", "$8.7m FCF 대비 EV $91.5m은 싸다.", "trailing cash conversion", "FCF가 유지비 차감 후 반복 가능하다.", "TTM FCF<$6m이면 반증.", "장기 earnings power 확대", "성공 방향", "trailing FCF의 acquisition spend를 해부한다."),("marketing normalize", "$33m 지출이 고객기반을 키운다.", "39% revenue 비중", "marginal cohort payback이 양수다.", "CAC 상승·customer 정체면 반증.", "빠른 개선은 없었음", "부분 실패", "규모보다 marginal payback을 본다."),("cash·NOL runway", "balance sheet가 기다릴 시간을 준다.", "현금과 tax asset", "경영진이 value-destructive spend를 피한다.", "cash burn·NOL 만료면 반증.", "생존과 성장자금 제공", "성공", "floor는 runway와 배분으로 분해한다."),("insider/buyback", "내부자 매수와 환원이 저평가를 확인한다.", "공시된 매수·repurchase", "정보우위와 per-share accretion이 있다.", "고가 환매·실적 하향이면 반증.", "장기 per-share value 확대", "부분", "행동을 operating evidence 대신 쓰지 않는다."),("Long direction", "낮아진 가격에서 downside보다 upside가 크다.", "FCF multiple·NOL·repurchase", "동일 common payoff다.", "Short payoff면 반증.", "raw Short→Long 교정", "성공", "raw flag보다 추천 action을 우선한다.")]),

I(id="e879e0a9-9dae-4cee-bb85-56aa4599cb19", date="2016-02-06", author="obvious617", ticker="STMP", entity="Stamps.com Inc.", group="stmp56", raw_short=True, direction="Short", entry="원문 가격 미복원", horizon="12~24개월", filename="analysis/ideas/2016/2016-02-06_STMP_short.md", link="https://www.valueinvestorsclub.com/idea/STAMPS.COM_INC/0599109745", desc=0, cat=107,
title="declining-mail TAM·M&A masking Short", verdict="e-commerce parcel TAM을 놓친 강한 실패", score=2.8, process=6.5,
summary="postal volume 감소, churn과 Endicia 인수가 organic weakness를 가린다는 약 32x EV/FCF Short였다. 그러나 회사를 letter-mail vendor로 정의한 것이 핵심 오류였다. 실제 성장엔진은 e-commerce parcel shipping workflow와 고 ARPU 고객이었고 2016~17 고객·ARPU·revenue가 함께 증가했다.",
valuation="약 32x EV/FCF가 비싸다는 논리는 FCF denominator가 acquisition synergies와 parcel growth 없이 정체한다는 전제였다. Endicia purchase price가 revenue의 3배 이상이라는 지적은 맞을 수 있으나 paid customers, ARPU, churn과 shipping volume이 동반 개선되면 multiple은 earnings growth로 빠르게 내려간다.",
actual="2016 total revenue는 $364.3m으로 2015 $214.0m에서 증가했다. 당시 공개자료는 paid customers와 ARPU, mailing/shipping revenue의 큰 성장을 보여줬고 2017에도 고객과 ARPU가 늘었다. 인수는 단순 숫자 masking이 아니라 shipping ecosystem을 확장했다.",
price="현재 SQL에는 catalyst 107자만 있고 description·performance COPY는 없다. valuation multiple과 후속 KPI는 thesis 검증에 쓰되 exact Short return·borrow·IRR은 null이다.",
drivers="손실을 만든 것은 multiple 그 자체보다 denominator와 TAM 오판이다. letter-mail 감소는 맞았지만 parcel labels, marketplace integrations와 high-volume shippers가 더 빠르게 커졌다. 고객 수와 ARPU가 동시에 상승해 organic weakness narrative를 반증했다.",
error="postal pieces를 company TAM의 proxy로 썼고 acquisitions를 전부 quality dilution으로 보았다. Endicia·ShipStation 고객의 더 높은 ARPU, parcel volume과 churn 개선을 별도 cohort로 분석했어야 한다.", first_signal="paid customers·ARPU·mailing/shipping revenue가 두 분기 연속 모두 두 자릿수 성장하고 churn이 하락하면 Short를 즉시 종료한다. 2016 공개 KPI는 이 조건을 충족했다.",
metrics=[("EV/FCF", "약 32x", "de-rate", "earnings growth가 denominator 확대", "실패"),("Endicia price/revenue", ">3x", "M&A impairment", "ecosystem 확장", "실패 방향"),("2016 revenue", "$364.3m", "weakness", "+70% vs 2015", "강한 반증"),("Paid customers", "감소 우려", "정체", "2016 증가", "반증"),("ARPU/churn", "quality 악화 우려", "ARPU 둔화·churn 상승", "ARPU 상승·churn 개선", "반증")],
timeline=[("2014", "ShipStation·ShipWorks 인수", "shipping stack"),("2015-Q4", "Endicia 인수", "규모 확대"),("2016-02-06", "VIC Short", "32x EV/FCF"),("2016-FY", "revenue $364.3m", "핵심 반증"),("2017", "고객·ARPU 성장", "Short 실패"),("2018", "shipping platform 고성장", "TAM 확인"),("2021", "$330 cash takeout", "장기 terminal proof")],
claimdata=[("postal decline", "우편물 감소가 Stamps.com TAM을 줄인다.", "USPS letter volume trend", "revenue가 letter pieces와 같이 움직인다.", "parcel/software revenue가 더 빠르게 성장하면 반증.", "shipping revenue 고성장", "강한 실패", "legacy category와 company TAM을 분리한다."),("M&A masks weakness", "Endicia가 organic decline을 가린다.", "대형 acquisition contribution", "acquired cohorts의 economics가 열위다.", "고객·ARPU·churn 동시 개선이면 반증.", "세 KPI가 개선", "실패", "M&A bridge와 cohort quality를 함께 본다."),("Endicia overpay", "3x+ revenue는 과도하다.", "deal multiple", "synergy·retention이 낮다.", "shipping ecosystem FCF 확대면 반증.", "platform earnings 확대", "실패", "deal multiple을 incremental FCF로 연결한다."),("churn risk", "고객 획득이 churn을 못 이긴다.", "subscription history", "acquired customers가 덜 끈끈하다.", "churn 하락이면 반증.", "2016 churn 개선", "실패", "고객수보다 gross adds와 churn을 분리한다."),("32x multiple", "정체 FCF에 과도한 배수다.", "reported EV/FCF", "earnings denominator가 고정된다.", "FCF 고성장이면 반증.", "operating income·revenue 성장", "실패", "multiple Short는 denominator catalyst가 필요하다."),("Short direction", "downside가 borrow와 squeeze를 보상한다.", "valuation·decline thesis", "반증 KPI 전 exit 가능하다.", "고객·ARPU 동시 증가면 종료.", "반증 뒤에도 business 성장", "실패", "Short는 hard stop을 먼저 둔다.")]),

I(id="d3dcfac9-be86-40f2-b862-24768133c133", date="2016-09-06", author="avahaz", ticker="STMP", entity="Stamps.com Inc.", group="stmp56", raw_short=True, direction="Short", entry="원문 가격 미복원", horizon="12~30개월", filename="analysis/ideas/2016/2016-09-06_STMP_short.md", link="https://www.valueinvestorsclub.com/idea/STAMPS.COM_INC/1523234195", desc=0, cat=57,
title="USPS reseller economics reset Short", verdict="mechanism은 2019 적중했지만 2016 trade timing은 실패", score=5.2, process=8.0,
summary="USPS reseller/NSA 보상이 구조적으로 지속 불가능하고 약 $90m EBIT이 위험해 약 80% downside가 있다는 Short다. 실제 USPS monetization reset은 2019 발생했지만 그 전 2년 이상 고객·earnings·주가가 크게 성장했다. mechanism과 investable timing을 분리해야 한다.",
valuation="약 $90m EBIT을 제거하는 stress는 reseller economics가 갑자기 사라지고 고객·volume·subscription value도 보전되지 않는 경우다. 80% downside에는 P(change), effective date, migration retention, 대체 carrier monetization과 남는 software value를 곱해야 한다.",
actual="2016~18 회사는 shipping growth와 인수 platform을 통해 earnings를 확대했다. 2019 USPS 관계 reset과 guidance shock가 발생해 구조적 의존성은 뒤늦게 드러났다. 그러나 Short는 그 전 duration·squeeze·borrow 비용을 버텨야 했으므로 원 horizon의 trade는 실패다.",
price="현재 SQL에는 catalyst 57자만 있고 description·performance COPY는 없다. $90m EBIT risk와 80% downside는 scenario anchor이며 exact Short return·borrow cost·IRR은 null이다.",
drivers="논지의 좋은 부분은 hidden counterparty concentration을 EBIT로 번역한 점이다. 실패는 contract change의 날짜와 전환경로를 제시하지 못하고 2016 growth를 무시한 것이다. 2019 shock는 mechanism 확인이지 2016 Short의 자동 성공이 아니다.",
error="USPS가 경제성을 바꿀 유인은 봤지만 company와 customers의 migration option, carrier diversification과 software franchise residual을 거의 0으로 뒀다. Short에는 6~12개월짜리 observable contract gate가 필요했다.", first_signal="USPS 공지·계약 renewal·회사 disclosure에서 보상조건 변경일이 12개월 내 특정되지 않고, paid customers·ARPU가 두 분기 연속 성장하면 Short를 닫는다. 반대로 partner revenue concentration이 커지며 formal notice가 나오면 재진입한다.",
metrics=[("EBIT at risk", "약 $90m", "소멸", "2019 일부 reset", "mechanism 성공"),("Downside", "약 80%", "계약 변화", "software residual 큼", "과대"),("Timing", "12~30개월", "USPS reset", "2019 발생", "지연/실패"),("Customer/ARPU", "성장 위험", "둔화", "2016~18 성장", "반증"),("Residual platform", "낮게 평가", "제한적", "multi-carrier 가치 확대", "실패")],
timeline=[("2015", "Endicia 인수", "USPS exposure 확대"),("2016-09-06", "VIC Short", "$90m EBIT risk"),("2017", "고객·ARPU 증가", "첫 trade 반증"),("2018", "earnings·shipping 성장", "Short duration 악화"),("2019-02", "USPS strategy reset", "mechanism 현실화"),("2019", "guidance shock", "주가 충격"),("2020-2021", "multi-carrier 회복·sale", "residual value 확인")],
claimdata=[("USPS concentration", "reseller economics가 EBIT의 큰 부분이다.", "약 $90m EBIT 추정", "partner terms가 business 전체로 귀속된다.", "subscription/software residual이 크면 반증.", "2019 shock는 material", "성공", "counterparty exposure를 profit bridge로 만든다."),("terms unsustainable", "USPS가 보상을 낮출 경제적 유인이 있다.", "NSA/reseller structure", "USPS가 계약상 실행할 수 있다.", "renewal 지속·volume benefit이면 반증.", "2019 reset", "성공/지연", "유인과 실행일을 분리한다."),("80% downside", "보상 제거 시 equity 대부분이 사라진다.", "$90m stress", "고객과 software value도 훼손된다.", "migration·대체 monetization이면 반증.", "장기 residual이 큼", "실패", "broken earnings와 남는 자산을 분리한다."),("near-term catalyst", "계약 변화가 investable horizon 안에 온다.", "정책 risk", "12~30개월 내 formal action", "공식 gate 부재면 반증.", "약 2.5년 뒤 발생", "실패", "Short mechanism에는 expiry date가 필요하다."),("growth masks risk", "reported growth가 low-quality partner economics다.", "높은 ARPU와 acquired volume", "고객 retention과 alternatives가 약하다.", "customer·carrier diversification이면 반증.", "2016~18 성장 후 2020 회복", "혼합", "quality risk도 KPI가 좋아지면 sizing을 줄인다."),("Short payoff", "downside가 borrow·squeeze를 보상한다.", "80% headline downside", "carry 기간이 짧다.", "주가·earnings 상승 지속이면 반증.", "trade timing 실패", "실패", "나중에 맞은 사건으로 과거 Short를 성공 처리하지 않는다.")]),

I(id="b5cf7b42-cc0f-4d85-af68-aeaa7931f6af", date="2017-04-06", author="bluewater12", ticker="STMP", entity="Stamps.com Inc.", group="stmp56", raw_short=True, direction="Long", entry="약 $110", horizon="5년", filename="analysis/ideas/2017/2017-04-06_STMP_long.md", link="https://www.valueinvestorsclub.com/idea/STAMPS.COM_INC/7795872038", desc=0, cat=3,
title="shipping-software ecosystem·$25 EPS Long", verdict="platform 재정의와 Long은 강한 성공·$500 target 미달", score=8.6, process=8.8,
summary="작성자가 short seller라고 소개해 raw가 잘못 붙었지만 STMP는 biggest Long이라고 명시했다. 약 $110에서 Endicia·ShipStation·ShipWorks·ShippingEasy를 포함한 shipping-software ecosystem, 5년 EPS 약 $25와 20x=$500을 주장했다. 2021 $330 cash exit으로 방향은 성공했지만 target과 USPS risk map은 과했다.",
valuation="5년 EPS $25×20x=$500은 약 4.5배 가격으로 customer·ARPU·parcel volume·margin이 동시에 compounding해야 한다. 더 보수적인 base는 USPS monetization haircut, acquisition integration cost와 share dilution을 반영하고 multi-carrier software value를 별도 SOTP로 둔다.",
actual="2017~18 shipping platform은 빠르게 성장했으나 2019 USPS reset이 earnings concentration을 드러냈다. 2020 revenue는 $758.0m으로 32.5% 증가하고 연평균 paid customers는 934k, Q4는 1,016k에 달했다. 2021 Thoma Bravo가 $330/share cash에 인수했다.",
price="현재 SQL catalyst는 `n/a` 3자뿐이고 description·performance COPY는 없다. 약 $110 entry, $500 target과 $330 terminal deal은 사건 anchors다. 정확한 total return·IRR은 null이다.",
drivers="성공의 핵심은 회사 이름이 아니라 e-commerce seller workflow를 묶는 multi-product ecosystem으로 산업을 다시 정의한 것이다. 실패 부분은 USPS 수익 집중과 5년 multiple durability를 충분히 haircut하지 않은 $500 target이다.",
error="$25 EPS에 도달하는 organic/acquired bridge, USPS/partner contribution과 stock compensation을 세분하지 않았다. 2019 contract reset 같은 single-counterparty tail을 확률가중하면 $500의 base 확률은 낮아져야 했다.", first_signal="paid customers·ARPU가 두 분기 연속 동반 감소하거나 USPS/partner contribution이 EBIT의 30%를 넘고 계약가시성이 12개월 미만이면 20x/$500 case를 제거한다.",
metrics=[("Entry", "약 $110", "$500", "$330 cash event", "방향 성공"),("5Y EPS", "$25", "compound", "정확 EPS bridge 미복원", "부분"),("Target multiple", "20x", "duration 유지", "USPS shock", "과대"),("2020 revenue", "$758.0m", "platform 성장", "+32.5%", "성공"),("2020 paid customers", "성장 가정", "scale", "934k avg/1,016k Q4", "성공")],
timeline=[("2014", "ShipStation·ShipWorks", "ecosystem 구축"),("2015", "Endicia", "USPS scale"),("2017-04-06", "VIC Long", "$110→$500"),("2018", "고성장", "thesis 강화"),("2019", "USPS reset", "risk 반증"),("2020", "revenue·customers 급증", "multi-carrier proof"),("2021-07", "$330 cash deal", "Long terminal success")],
claimdata=[("ecosystem definition", "STMP는 단일 postage site가 아니라 shipping software suite다.", "Endicia·ShipStation·ShipWorks·ShippingEasy", "제품들이 merchant workflow를 깊게 점유한다.", "cross-sell·retention 약화면 반증.", "2020 platform scale", "강한 성공", "company TAM은 고객 job-to-be-done으로 정의한다."),("e-commerce parcel TAM", "parcel shipping이 declining mail을 압도한다.", "seller·marketplace integrations", "e-commerce volume이 장기 성장한다.", "parcel volume·merchant count 감소면 반증.", "revenue·customers 증가", "성공", "legacy와 growth volume을 분리한다."),("M&A integration", "인수 브랜드가 distribution·ARPU를 강화한다.", "고 ARPU acquired customers", "기술·영업 통합 비용이 제한적이다.", "churn·margin 악화면 반증.", "ecosystem으로 확장", "성공", "M&A는 cohort와 contribution으로 본다."),("$25 EPS", "5년 내 earnings가 크게 compounding한다.", "volume·ARPU·operating leverage", "USPS terms와 margin이 유지된다.", "partner reset·EPS bridge 이탈이면 반증.", "2019 shock로 path 훼손", "부분 실패", "장기 EPS는 counterparty bridge를 붙인다."),("20x/$500", "quality platform에 20x를 적용할 수 있다.", "software-like duration", "terminal growth·risk가 유지된다.", "single-partner risk 현실화면 반증.", "$330 exit로 target 미달", "부분", "좋은 방향과 과한 target을 분리한다."),("Long direction", "STMP는 biggest Long이다.", "원문 explicit action", "common stock payoff다.", "short recommendation이면 반증.", "raw Short→Long 교정", "성공", "작성자 스타일이 아니라 개별 action을 읽는다.")]),

I(id="ee7fdd2a-707e-4053-8d1f-da462cbe11fd", date="2019-06-24", author="regency435", ticker="STMP", entity="Stamps.com Inc.", group="stmp56", raw_short=True, direction="Long", entry="시가총액 약 $750m", horizon="2~3년", filename="analysis/ideas/2019/2019-06-24_STMP_long.md", link="https://www.valueinvestorsclub.com/idea/STAMPS.COM_INC/5454189345", desc=0, cat=31,
title="broken earnings=0·asset SOTP Long", verdict="multi-carrier 회복과 $330 takeout으로 매우 강한 성공", score=9.7, process=9.6,
summary="raw Short가 아니라 두 번의 USPS shock 뒤 시가총액 약 $750m에서 산 Long이다. 2018 EBITDA 약 $258m을 정상화하지 않고, Street 2020 EBITDA 약 $100m조차 사실상 0으로 둔 뒤 cash/HQ, 575k SOHO subscribers, 160k e-commerce shippers, MetaPack과 기타 자산만으로 $37~47/share를 산정했다.",
valuation="zero-monetization SOTP는 $37~47/share, midpoint 약 $42였다. 대체 carrier monetization을 더하면 midpoint 약 $72였다. 중요한 점은 old USPS earnings 회복을 base에 넣지 않은 것이다. 각 subscriber asset은 retention·gross contribution·migration capex를 차감하고 MetaPack은 standalone loss와 integration cost를 반영해야 한다.",
actual="2020 revenue는 $758.0m으로 32.5% 증가했고 annual average paid customers는 743k에서 934k로 25.7%, ARPU는 $750에서 $799로 6.5% 증가했다. multi-carrier 전략과 e-commerce volume이 residual asset 가치를 검증했고 2021 $330/share cash transaction이 발표됐다.",
price="현재 SQL에는 catalyst 31자만 있고 description·performance COPY는 없다. market cap $750m, SOTP $37~47/$72와 $330 deal은 검증 anchors다. exact entry close·배당이 없어 return/IRR은 null이다.",
drivers="가장 좋은 부분은 깨진 earnings를 억지로 정상화하지 않고 0으로 둔 것이다. 시장이 같은 shock를 두 번 자본화한 뒤에도 남은 subscriber relationships와 shipping software가 positive value였고, 2020 e-commerce acceleration과 multi-carrier 실행이 option을 현실화했다.",
error="SOHO 575k와 e-commerce 160k의 중복·churn·unit contribution, MetaPack의 standalone cost와 USPS 이탈 투자비를 더 명시적으로 차감할 수 있었다. 2020 pandemic boost는 T0에 알 수 없는 upside이므로 process 점수와 결과를 분리해야 한다.", first_signal="paid customers가 700k 아래로 내려가고 ARPU도 하락하거나, carrier diversification 후 segment operating loss가 두 분기 지속돼 zero-monetization SOTP의 net cash burn이 $10/share를 넘으면 Long을 재평가한다.",
metrics=[("Market cap", "약 $750m", "asset floor", "2021 $6.6bn deal", "강한 성공"),("2018 EBITDA", "$258m", "base에서 미사용", "2019 reset", "보수적"),("2020 Street EBITDA", "$100m", "사실상 0 처리", "2020 operating recovery", "강한 성공"),("Zero SOTP", "$37~47", "floor", "residual value 입증", "성공"),("Alt-carrier SOTP", "midpoint $72", "monetization", "multi-carrier+$330 exit", "강한 성공")],
timeline=[("2018", "EBITDA 약 $258m", "old peak"),("2019-02", "첫 USPS shock", "earnings reset"),("2019-05", "두 번째 shock", "capitulation"),("2019-06-24", "VIC Long", "SOTP $37~47/$72"),("2020", "revenue $758m·paid customers 934k", "asset proof"),("2021-07", "$330 deal 발표", "strategic value"),("2021-Q4", "거래 완료", "terminal cash event")],
claimdata=[("broken earnings zero", "USPS earnings 회복 없이도 downside가 지지된다.", "Street 2020 EBITDA $100m을 거의 0 처리", "남은 자산의 cash burn이 제한적이다.", "net burn>$10/share면 반증.", "2020 earnings 회복", "강한 성공", "불확실한 earnings를 0으로 두고 asset를 센다."),("SOHO subscribers", "575k 관계에 residual value가 있다.", "subscription base", "churn 후 contribution이 양수다.", "고객·ARPU 동시 급락이면 반증.", "2020 paid customer 증가", "성공", "고객 수를 retention cash flow로 바꾼다."),("e-commerce shippers", "160k high-value shippers가 crown jewel이다.", "higher usage·ARPU", "carrier migration에도 남는다.", "volume 이탈이면 반증.", "e-commerce acceleration", "강한 성공", "거래상대방보다 workflow ownership을 본다."),("MetaPack·other assets", "MetaPack·HQ·cash가 추가 floor다.", "acquired software·hard assets", "standalone losses·tax가 제한적이다.", "integration burn이면 반증.", "whole-company strategic bid", "성공 방향", "SOTP에는 standalone cost를 뺀다."),("multi-carrier option", "USPS 밖 monetization이 $72 midpoint를 만든다.", "carrier-neutral integrations", "고객이 migration한다.", "non-USPS volume이 정체하면 반증.", "2020 multi-carrier 확대", "성공", "option은 KPI가 보이면 base로 올린다."),("Long direction", "두 shock 뒤 purchase를 추천한다.", "positive SOTP payoff", "common security다.", "Short recommendation이면 반증.", "raw Short→Long 교정", "성공", "payoff language로 direction을 정한다.")]),

I(id="e6e81eb8-bda8-4065-b872-ef0e083f3d56", date="2008-05-11", author="claude535", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw56", raw_short=True, direction="Short", entry="약 $44 implied", horizon="12~18개월", filename="analysis/ideas/2008/2008-05-11_WTW_short.md", link="https://www.valueinvestorsclub.com/idea/Weight_Watchers_International/9697115100", desc=0, cat=322,
title="attendance decline·debt-funded tender Short", verdict="recession·leverage의 전술적 성공, online offset로 secular collapse는 과대", score=8.3, process=8.8,
summary="meeting attendance 감소와 $1.025bn debt-funded tender로 debt가 약 $830m에서 $1.8bn 수준으로 뛴 뒤의 common Short다. 약 $31 target/30% downside는 약 $44 entry를 암시한다. recession과 fixed-cost deleverage는 적중했지만 online subscription 성장으로 franchise의 장기 0가치 논리는 과했다.",
valuation="meeting attendance 감소를 price/mix가 상쇄하지 못하면 leader·rent·marketing 고정비가 EBITDA를 빠르게 압박한다. target 약 $31은 delevered multiple이 아니라 leverage 확대 후 lower earnings에 낮은 multiple을 적용한 결과다. online revenue와 subscriber growth는 downside에서 별도 positive segment로 남겨야 한다.",
actual="2008 downturn은 discretionary enrollment와 attendance를 압박해 Short의 cycle·leverage 메커니즘을 검증했다. 동시에 online revenue는 약 22.6%, subscribers는 약 16.3% 성장해 digital channel이 회사를 완전히 무너뜨리지는 않았다. 따라서 전술적 Short는 성공하되 secular terminal Short로 확대하면 안 된다.",
price="현재 첨부 SQL에는 catalyst 322자만 있고 performance COPY가 없다. 기존 payload의 WTW 성과값은 후대 Willis Towers Watson ticker series와 섞여 폐기했다. target $31과 implied entry $44는 원문 anchor이며 exact Short return·borrow·IRR은 null이다.",
drivers="수익 driver는 비만 prevalence가 아니라 소비심리 충격과 leverage가 meeting attendance 감소를 common에 증폭한 것이다. 반면 online은 fixed-location exposure가 낮고 subscription economics가 있어 downside를 제한했다.",
error="meetings weakness를 전체 category collapse로 일반화했고 online 성장의 margin·retention을 충분히 credit하지 않았다. tender가 만든 leverage는 핵심 edge였지만 refinancing calendar와 interest covenant를 더 구체화할 수 있었다.", first_signal="meeting attendance가 두 분기 연속 5% 이상 감소하고 net debt/EBITDA가 상승하면 Short를 유지한다. 반대로 online contribution이 meeting decline을 상쇄하고 consolidated EBITDA가 안정되면 cover한다.",
metrics=[("Implied entry/target", "약 $44/$31", "30% downside", "exact 성과 null", "방향 성공"),("Tender", "$1.025bn", "share shrink", "leverage 확대", "Short 성공"),("Debt", "$830m→약 $1.8bn", "coverage 압박", "recession 민감", "성공"),("Online revenue", "+22.6%", "낮게 평가", "성장", "Short 완충"),("Online subscribers", "+16.3%", "정체 우려", "증가", "secular 반증")],
timeline=[("2007", "$1.025bn tender", "debt-funded recap"),("2008-05-11", "VIC Short", "$31 target"),("2008-H2", "recession 심화", "attendance 압박"),("2009", "meeting weakness", "operating leverage"),("2009-2010", "online 성장", "downside offset"),("2011 이후", "digital 대안 확대", "category 변화"),("2015", "Oprah partnership", "brand optionality")],
claimdata=[("attendance decline", "meeting attendance 감소가 revenue를 압박한다.", "지역별 enrollment·attendance trend", "pricing이 volume 감소를 못 메운다.", "attendance 안정·price/mix 상쇄면 반증.", "recession 중 weakness", "성공", "consumer subscription은 cohort volume을 본다."),("fixed-cost deleverage", "meeting model은 volume 감소 시 margin이 급락한다.", "leader·rent·marketing network", "비용을 빠르게 줄이기 어렵다.", "variableization·closure로 margin 유지면 반증.", "cycle 압박 확대", "성공", "unit decline을 cost elasticity로 번역한다."),("tender leverage", "$1.025bn tender가 common risk를 키운다.", "debt $830m→$1.8bn", "FCF가 debt service를 감당한다.", "coverage 악화면 Short 강화.", "downturn 민감도 확대", "강한 성공", "share shrink와 enterprise risk를 함께 본다."),("$31 target", "earnings·multiple 하락이 30% downside를 만든다.", "implied $44 entry", "borrow·timing이 허용된다.", "online offset·multiple 유지면 반증.", "전술적 방향 성공", "성공/수익 null", "target과 exact return을 구분한다."),("online insufficient", "digital 성장도 meeting 감소를 못 메운다.", "segment mix", "online scale·margin이 작다.", "online revenue·subs 두 자릿수 성장 시 반증.", "+22.6%/+16.3%", "부분 실패", "상쇄 segment를 따로 가치평가한다."),("secular franchise decline", "무료/self-directed 대안이 장기 franchise를 훼손한다.", "consumer alternatives", "brand와 intervention efficacy가 방어 못 한다.", "brand relaunch·digital retention이면 반증.", "회사는 생존·후일 rebound", "과대", "cycle Short를 terminal Short로 늘리지 않는다.")]),

I(id="8655169b-6c07-4b55-ba24-24f1193ca588", date="2013-03-21", author="abra399", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw56", raw_short=True, direction="Long", entry="$41.73", horizon="12~24개월", filename="analysis/ideas/2013/2013-03-21_WTW_long.md", link="https://www.valueinvestorsclub.com/idea/WEIGHT_WATCHERS_INTL_INC/3892239359", desc=0, cat=161,
title="temporary recruitment reset·11.2% FCF yield Long", verdict="free apps·category redefinition을 일시요인으로 본 강한 실패", score=3.6, process=7.2,
summary="raw Short가 아니라 $41.73에서 2012 FCF yield 11.2%, target $53·upside $65·downside $37을 제시한 Long이다. payroll tax, Jessica Simpson pregnancy와 약한 campaign을 일시적 recruitment 문제로 봤지만 free apps·activity monitors가 paid program의 지불의사를 구조적으로 바꾸고 있었다.",
valuation="$41.73에서 downside $37은 약 -11%, base $53은 약 +27%, upside $65는 약 +56%다. 11.2% trailing FCF yield가 유지되려면 meeting recruitment가 회복되고 digital pricing power가 지켜져야 한다. debt와 share repurchase로 인한 per-share accretion보다 enterprise FCF decline을 먼저 stress해야 한다.",
actual="2013 후반 recruitment와 attendance는 약해졌고 company는 dividend를 중단했다. 2014 revenue와 attendance decline은 temporary marketing explanation보다 category substitution을 지지했다. 무료 tracking과 wearable behavior가 acquisition funnel을 바꾸면서 2014 recovery base는 실현되지 않았다.",
price="현재 SQL에는 catalyst 161자만 있고 description·performance COPY는 없다. 기존 WTW performance flag/value는 Willis Towers Watson ticker contamination으로 폐기했다. $41.73·$37/$53/$65와 11.2% FCF yield만 T0 anchor이며 exact return/IRR은 null이다.",
drivers="손실 원인은 단순 weak ad가 아니라 customer problem을 해결하는 대체재의 가격이 0에 가까워진 것이다. levered buyback은 줄어드는 enterprise cash flow를 적은 주식에 나눠 일시적으로 EPS를 방어했지만 common duration을 더 짧게 했다.",
error="세 가지 temporary excuse를 base에 넣고 free apps·wearables를 product category change가 아닌 marketing noise로 처리했다. trial, paid conversion, attendance, digital net adds와 CAC를 월별 cohort로 봤어야 한다.", first_signal="North America meeting recruitment·attendance가 두 분기 연속 high-single-digit 감소하고 online net adds/ARPU도 둔화하면 temporary thesis를 폐기한다. dividend suspension은 capital-allocation 반증으로 즉시 반영한다.",
metrics=[("Entry", "$41.73", "$53/$65", "recovery 미실현", "실패"),("Downside", "$37", "limited", "fundamental 악화", "과소"),("2012 FCF yield", "11.2%", "유지", "FCF duration 훼손", "실패"),("Recruitment", "temporary weakness", "2014 회복", "지속 감소", "실패"),("Digital substitutes", "낮게 평가", "paid moat 유지", "free apps·wearables 확대", "강한 실패")],
timeline=[("2012", "FCF yield 11.2%", "cheapness anchor"),("2013-03-21", "VIC Long", "$41.73"),("2013-H1", "weak campaign/recruitment", "temporary thesis"),("2013-Q3", "revenue·profit decline", "첫 반증"),("2013", "dividend suspension", "debt priority"),("2014", "attendance·revenue 추가 감소", "structural proof"),("2015", "Oprah partnership", "후일 optionality")],
claimdata=[("temporary recruitment", "payroll tax·campaign·spokesperson 문제가 일시적이다.", "2013 guide와 marketing reset", "category demand는 intact다.", "두 분기 attendance 감소면 반증.", "weakness 지속", "실패", "temporary claim에는 회복일을 둔다."),("11.2% FCF yield", "현금수익률이 downside를 지지한다.", "2012 FCF", "FCF가 반복 가능하다.", "recruitment·attendance 동반 감소면 반증.", "duration 훼손", "실패", "yield보다 cash flow half-life를 본다."),("brand moat", "Weight Watchers 신뢰와 efficacy가 무료앱을 이긴다.", "long operating history", "소비자가 coaching에 premium을 낸다.", "free conversion·paid churn 악화면 반증.", "지불의사 약화", "실패", "brand awareness와 willingness-to-pay를 분리한다."),("online crown jewel", "online이 meetings weakness를 보완한다.", "digital subscription margin", "digital net adds와 ARPU가 유지된다.", "free apps가 acquisition을 잠식하면 반증.", "대체재 압력 확대", "실패", "digital channel도 digital substitute에 취약하다."),("levered buyback", "낮은 가격 환매가 per-share FCF를 높인다.", "debt capacity·share shrink", "enterprise FCF가 안정적이다.", "dividend 중단·coverage 압박이면 반증.", "capital flexibility 감소", "실패", "shrinking denominator보다 enterprise decline을 본다."),("Long direction", "$37 downside 대비 $53/$65 upside다.", "positive recommendation", "common payoff다.", "Short action이면 반증.", "raw Short→Long 교정", "성공", "방향 교정과 아이디어 성공을 구분한다.")]),

I(id="310d7a03-57a0-4111-be06-288a9a8c53e7", date="2013-09-30", author="MSLM28", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw56", raw_short=True, direction="Long", entry="$37 이하", horizon="12~24개월", filename="analysis/ideas/2013/2013-09-30_WTW_long.md", link=None, desc=0, cat=174,
title="43% share·online crown jewel Long", verdict="category redefinition과 debt optionality를 오판한 강한 실패", score=3.3, process=7.3,
summary="raw Short가 아니라 $37 이하 매수, fair value $48~60을 주장한 Long이다. 미국 시장 약 43% share, online crown jewel과 느슨한 covenant·낮은 amortization을 들어 debt를 quasi-asset처럼 봤다. 그러나 Q3 실적·dividend suspension과 2014 attendance 급락이 paid category 자체의 축소를 확인했다.",
valuation="$37 entry에서 $48~60은 약 +30~62%다. share moat와 online value를 합산하면서 debt의 낮은 near-term amortization을 equity option으로 봤지만, enterprise value가 하락하면 장기만기는 common의 손실을 지연할 뿐 없애지 않는다. refinance spread와 covenant headroom을 downside에 넣어야 한다.",
actual="2013 Q3 revenue는 약 8.5%, net income 10.5%, EPS 11.2% 감소했고 dividend가 중단됐다. 2014 초에도 revenue와 attendance가 크게 줄어 temporary recruitment가 아니라 category disruption을 확인했다. 높은 historical share는 shrinking paid market의 방어가 아니었다.",
price="현재 SQL에는 catalyst 174자만 있고 description·performance COPY는 없다. link도 prior overlay에 없다. 후대 Willis Towers Watson ticker 성과는 제거했고 $37/$48~60만 anchor로 사용한다. exact return/IRR은 null이다.",
drivers="손실은 competitor가 share를 빼앗아서가 아니라 consumer가 paid meetings/online program을 우회한 데서 왔다. 느슨한 covenant는 채무불이행 시점을 늦췄지만 interest와 refinancing claim을 common 앞에 남겼다.",
error="43% share를 넓은 weight-management 시장이 아니라 기존 paid-program category 안에서 측정했다. online을 기술자산으로 높게 보면서 무료 디지털 대안이 가격을 0으로 만드는 위험을 과소평가했다.", first_signal="quarterly revenue -5%, attendance -8%와 online net adds 둔화가 함께 나타나거나 dividend가 중단되면 $48~60 target을 폐기한다. 2013 Q3가 사실상 이 조건이었다.",
metrics=[("Entry/fair value", "≤$37/$48~60", "+30~62%", "fundamental decline", "실패"),("US share", "약 43%", "moat", "shrinking category", "오판"),("Q3 revenue", "recovery 기대", "안정", "-8.5%", "반증"),("Q3 net income/EPS", "stability", "회복", "-10.5%/-11.2%", "반증"),("Debt terms", "loose covenant/low amortization", "optionality", "common senior claim 지속", "실패")],
timeline=[("2013-03", "선행 Long", "temporary thesis"),("2013-09-30", "VIC Long", "buy ≤$37"),("2013-Q3", "revenue -8.5%", "반증"),("2013-Q3", "dividend suspension", "capital priority"),("2014-02", "revenue·attendance 추가 감소", "structural disruption"),("2014", "free apps·wearables 확대", "category 우회"),("2015", "Oprah partnership", "unexpected brand option")],
claimdata=[("43% share moat", "미국 share가 pricing과 recovery를 지지한다.", "paid category share", "category size가 안정적이다.", "category participation 감소면 반증.", "paid category 축소", "실패", "share의 denominator를 검증한다."),("online crown jewel", "online segment가 높은 독립가치를 가진다.", "subscription margin·brand", "무료앱과 차별화된다.", "net adds·ARPU 하락이면 반증.", "free alternatives 확산", "실패", "digital label이 moat를 보장하지 않는다."),("marketing reset", "새 campaign이 recruitment를 회복한다.", "brand awareness·creative change", "problem이 message이지 product다.", "두 campaign 뒤 attendance 감소면 반증.", "weakness 지속", "실패", "funnel 어느 단계가 깨졌는지 본다."),("debt optionality", "낮은 amortization·loose covenant가 equity 시간을 준다.", "maturity terms", "enterprise FCF가 회복한다.", "dividend 중단·refi spread 상승이면 반증.", "capital flexibility 악화", "실패", "긴 만기는 가치가 아니라 option expiry다."),("$48~60 value", "normalized FCF에 정상 배수를 적용한다.", "historical cash generation", "attendance가 정상화된다.", "revenue -5% 이상 지속이면 반증.", "Q3부터 조건 충족", "강한 실패", "normalization 전에 leading KPI를 확인한다."),("Long direction", "$37 이하 매수다.", "positive fair-value gap", "common stock payoff다.", "Short recommendation이면 반증.", "raw Short→Long 교정", "성공", "direction accuracy와 investment quality를 분리한다.")]),

I(id="72d5d91e-1363-4fb9-85fb-741a2601c4c7", date="2014-02-22", author="murman", ticker="WTW", entity="Weight Watchers International, Inc.", group="wtw56", raw_short=True, direction="Short", entry="원문 가격 미복원", horizon="12~24개월", filename="analysis/ideas/2014/2014-02-22_WTW_short.md", link=None, desc=0, cat=189,
title="free-app substitution·$2.2bn leverage Short", verdict="fundamentals 적중·50~60% borrow와 Oprah squeeze로 trade economics 위험", score=8.0, process=9.0,
summary="약 6x earnings인데도 meetings 70%/online 30%, online 약 $19/month 대 무료앱, internet revenue -5.3%와 debt 약 $2.2bn을 근거로 한 Short다. category substitution과 leverage는 적중했지만 borrow 50~60%와 2015 Oprah partnership의 violent rebound 때문에 좋은 fundamental call과 좋은 tradable Short는 다르다.",
valuation="stress는 meetings revenue -5%, internet -50%를 적용해 EBITDA와 interest coverage가 빠르게 악화하는 구조다. 낮은 P/E는 debt service 뒤 common duration이 짧아서 생긴 것이고 cheapness가 floor가 아니었다. 다만 50~60% borrow fee는 1년 carry만으로 gross downside의 절반 이상을 소진할 수 있다.",
actual="2014 attendance·revenue weakness는 continued됐고 free digital alternatives가 paid online의 가격권을 압박했다. leverage는 common downside를 증폭했다. 그러나 2015 Oprah가 지분·전략 파트너로 참여하며 brand option이 현실화돼 crowded/expensive Short에 큰 squeeze를 만들었다.",
price="현재 SQL에는 catalyst 189자만 있고 description·performance COPY는 없다. legacy WTW performance values 4건은 Willis Towers Watson contamination으로 폐기했다. fundamental outcome은 질적으로 판정하지만 exact Short return·borrow path·IRR은 null이다.",
drivers="fundamental edge는 paid intermediation을 무료 self-tracking이 우회하고 meetings fixed cost와 debt가 이를 증폭한다는 구조였다. trade risk는 높은 borrow, brand optionality와 단일 celebrity event가 equity duration을 갑자기 늘릴 수 있다는 점이었다.",
error="internet -50% stress는 방향은 좋지만 전환 속도와 cost cuts를 더 세분했어야 한다. 무엇보다 borrow 50~60%는 valuation thesis와 별도 security hurdle이다. catalyst가 늦거나 squeeze가 오면 옳은 terminal view도 negative IRR이 된다.", first_signal="borrow가 25%를 넘거나 days-to-cover가 급증하면 fundamental conviction과 무관하게 position을 줄인다. attendance/internet decline이 멈추거나 strategic equity partner가 등장하면 즉시 cover한다.",
metrics=[("Earnings multiple", "약 6x", "더 낮아짐", "value trap", "Short 지지"),("Revenue mix", "meetings 70%/online 30%", "두 부문 decline", "동반 압박", "성공"),("Online price", "약 $19/month", "free substitution", "지불의사 하락", "성공"),("Debt", "약 $2.2bn", "coverage stress", "downside 증폭", "성공"),("Borrow", "50~60%", "빠른 catalyst 필요", "Oprah squeeze", "위험/실패 가능")],
timeline=[("2013-Q3", "revenue decline·dividend 중단", "precondition"),("2014-02-22", "VIC Short", "6x P/E에도 sell"),("2014", "attendance·internet weakness", "fundamental confirmation"),("2014-2015", "debt/coverage pressure", "common convexity"),("2015-10-19", "Oprah partnership", "unexpected catalyst"),("2015-Q4", "violent rally", "borrow·squeeze risk"),("이후", "digital-first repositioning", "brand option")],
claimdata=[("free-app substitution", "무료 tracking이 $19/month online을 대체한다.", "apps·wearables adoption", "self-directed users가 paid coaching을 떠난다.", "paid net adds·ARPU 회복이면 반증.", "online revenue 압박", "성공", "가격이 0인 대체재는 willingness-to-pay를 본다."),("meeting decline", "70% revenue meetings가 구조적으로 감소한다.", "attendance trend", "cost cuts가 volume decline보다 느리다.", "attendance 안정·margin 유지면 반증.", "2014 weakness 지속", "성공", "fixed-cost channel은 unit decline이 핵심이다."),("leverage convexity", "$2.2bn debt가 작은 EBITDA 하락을 common에 증폭한다.", "interest burden", "refinancing·coverage가 악화한다.", "deleveraging·capital injection이면 반증.", "downside 확대", "성공", "P/E보다 enterprise waterfall을 본다."),("internet -50% stress", "digital economics도 빠르게 훼손된다.", "revenue -5.3% 선행", "decline이 가속한다.", "retention·cost cuts로 FCF 유지면 반증.", "방향 맞으나 속도 불확실", "부분 성공", "stress에는 전환 속도를 붙인다."),("borrow hurdle", "50~60% carry를 감수할 만큼 catalyst가 빠르다.", "높은 borrow", "12개월 안에 큰 downside가 온다.", "catalyst 지연·squeeze면 반증.", "Oprah rally가 tail 현실화", "실패 위험", "좋은 Short도 borrow-adjusted IRR을 통과해야 한다."),("brand optionality", "brand rescue는 downside를 바꾸지 못한다.", "weak operations", "외부 파트너·celebrity가 없다.", "strategic equity partner면 반증.", "Oprah partnership", "실패", "deeply levered brand에는 rescue option을 둔다.")]),
]


def idea_sources(idea):
    status = f"description {idea['desc']:,} chars" if idea["desc"] else "description absent"
    raw = m.S(
        "첨부 SQL 원문/metadata와 prior curated overlay",
        idea["link"],
        "VIC_IDEAS(4).sql / VIC / repository prior overlay",
        idea["date"],
        f"idea_id·raw Short·catalyst {idea['cat']} chars·{status}; 현재 SQL에 없는 원문 anchor는 lower-provenance overlay로 분리",
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
        "Batch 056 중 이 아이디어만 첨부 SQL description 17,911자가 있다. catalyst도 직접 확인했고 원문 수치를 SQL 우선으로 검증했다."
        if idea["desc"] else
        "첨부 SQL에는 catalyst만 있고 description은 없다. date·author·raw flag와 원문 수치는 prior curated overlay로 provenance를 분리했다."
    )
    text = text.replace("Batch 046 canonical report.", "Batch 056 canonical report.")
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
        "기업·사건: **A/B** — SEC·회사·USPS 자료로 operating KPI와 terminal event를 교차검증했다.",
    )
    text = text.replace(
        "가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
        "가격성과: **C** — 현재 SQL에 performance COPY가 없다. WTW legacy 값 4건은 ticker contamination으로 폐기했고 corporate event를 exact return으로 바꾸지 않았다.",
    )
    return text


def payload():
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(IDEAS)
    finally:
        m.idea_sources = old
    out["batch"] = 56
    out["title"] = "Stamps.com / Weight Watchers — TAM Definition, Expectation Reset and Leverage V9"
    null_keys = (
        "perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y",
        "idea_return_1y", "idea_return_3y", "idea_return_5y",
    )
    for idea, master, post in zip(IDEAS, out["ideas_master"], out["postmortems"]):
        master["security_ko"] = idea["security"]
        master["performance_available"] = 0
        master["auto_tag_status_ko"] = "current SQL catalyst 감사·direction 수동교정·WTW ticker 성과오염 제거·exact return null"
        for key in null_keys:
            master[key] = None
        post["research_direction_ko"] = f"{idea['direction']} / {idea['security']}"
        post["research_status_ko"] = "SQL 원문 provenance·공식 filings 검증; performance COPY 부재로 exact return null"
        post["confidence"] = 0.94 if idea["desc"] else (0.91 if idea["link"] else 0.84)
    return out


def make_index():
    rows = []
    for n, idea in enumerate(IDEAS, 1):
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(
            f"| {n} | {idea['date']} | {idea['ticker']} | Short→**{idea['direction']}** | {idea['verdict']} | [{idea['title']}]({link}) |"
        )
    return "\n".join([
        "# Batch 056 — Stamps.com / Weight Watchers — V9 Index", "",
        f"> Research as-of {ASOF}. 10 idea = 10 canonical reports다. 현재 SQL에는 catalyst 10건, description 1건만 있고 performance COPY는 없다. raw 10건은 모두 Short지만 실제는 Long 6 / Short 4다.", "",
        "## 0. 배치 결론", "",
        "이 배치는 digital이 기존 산업을 없애는 방식이 서로 반대일 수 있음을 보여준다. Stamps.com은 우편물 감소 속에서도 e-commerce shipping workflow를 소프트웨어로 중개해 TAM을 넓혔다. Weight Watchers는 free apps와 wearables가 paid meetings/online을 우회하면서 중개가치를 잃었다. 단순히 'digital disruption'을 붙이지 말고 누가 workflow를 더 깊게 소유하는지 봐야 한다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | Ticker | raw→연구 방향 | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|", *rows, "",
        "## 2. SQL·Direction·Performance Audit", "",
        "첨부 `VIC_IDEAS(4).sql`의 COPY table은 catalyst·companies·descriptions뿐이다. Batch 056 catalyst 10건을 모두 확인했고 2007 STMP description 17,911자만 존재한다. direction correction은 STMP 2007·2008·2017·2019, WTW 2013-03·2013-09의 6건이다. 성과 테이블이 없으므로 모든 exact return/IRR은 null이다. 기존 WTW 4건의 performance flag/value는 후대 Willis Towers Watson ticker series가 섞인 값이라 폐기했다.", "",
        "## 3. Stamps.com — 좋은 분석과 나쁜 clock을 분리", "",
        "2007 Long은 marketing LTV/CAC·NOL·cash를 잘 봤지만 2009의 세 target을 모두 놓쳤다. 2008 Long은 그 실패를 인정하고 EV/FCF 약 10.5x에서 expectation을 낮춰 새 투자로 만들었다. 2016-02 Short는 회사 TAM을 declining letter mail로 오정의해 실패했다. 2016-09 Short는 USPS 의존 메커니즘을 맞혔지만 사건이 2019에 와 trade timing은 실패했다.", "",
        "2017 Long은 STMP를 Endicia·ShipStation·ShipWorks·ShippingEasy의 shipping-software ecosystem으로 재정의해 방향을 맞혔지만 $500 target은 과했다. 2019 Long은 깨진 USPS earnings를 회복시키지 않고 0으로 둔 뒤 customer assets와 MetaPack만 사서 가장 좋은 payoff를 만들었다. 2020 revenue $758.0m·paid customers 934k, 2021 $330 cash deal은 residual asset value를 검증한다.", "",
        "## 4. Weight Watchers — leverage보다 먼저 category denominator", "",
        "2008 Short는 attendance 감소와 $1.025bn tender 뒤 약 $1.8bn debt가 recession을 증폭한다는 전술적 논지로 성공했다. 다만 online revenue·subscriber 성장은 terminal collapse를 막았다. 2013의 두 Long은 historical share와 online을 moat로 보고 free apps·wearables를 temporary marketing noise로 오판했다. 2014 Short는 meetings 70%/online 30%, $2.2bn debt와 free substitution을 맞혔지만 50~60% borrow와 Oprah rescue가 좋은 fundamental call을 위험한 trade로 만들었다.", "",
        "## 5. 투자논지 재사용 규칙", "",
        "1. TAM은 제품 이름이 아니라 customer job과 대체경로로 정의한다.\n2. marketing 자산화는 channel별 cohort LTV/CAC와 payback으로만 한다.\n3. 같은 회사라도 expectation reset과 entry가 바뀌면 새 투자다.\n4. structural mechanism에는 observable contract date와 position expiry를 붙인다.\n5. broken earnings를 0으로 두고 남는 자산을 사는 SOTP가 정상화보다 안전할 수 있다.\n6. market share는 shrinking category의 denominator를 확인한다.\n7. 긴 만기·loose covenant는 enterprise loss를 없애지 않는다.\n8. Short는 borrow-adjusted IRR과 squeeze catalyst를 valuation과 별도로 본다.\n9. corporate event는 exact return이 아니다.\n10. ticker가 재사용되면 issuer/date/security부터 resolve한다.", "",
        "## 6. 산출물", "",
        "- Payload: `data/curated/batch_056_stmp_wtw_deep_v7.json`\n- Wrapper: `analysis/batch_056_stmp_wtw_10.md`\n- Source packet: `data/curated/batch_056_source_packet.json`\n- SQL inventory: `data/curated/batch_056_sql_inventory.json`\n- Builder: `scripts/56_build_batch_056_v9.py`", "",
        "## 7. 검증 기준", "",
        "각 보고서는 0~12절, 6 weighted claims/100%, 5 metrics, 최소 6 timeline events와 원문 provenance+공식자료를 포함한다. Payload·문서·앱 popup의 idea_id, entity, direction, security와 verdict를 동일하게 유지한다.", "",
    ])


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 056 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or len(idea_sources(idea)) < 5:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(idea["filename"]).relative_to("analysis").as_posix() for idea in IDEAS]
    wrapper = "# Batch 056 — Stamps.com / Weight Watchers V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit wrapper. [Batch 056 V9 Index](batch_056_v9_index.md).\n"
    (ROOT / "analysis/batch_056_stmp_wtw_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_056_v9_index.md").write_text(make_index(), encoding="utf-8")
    out = payload()
    (ROOT / "data/curated/batch_056_stmp_wtw_deep_v7.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {
        "batch": "056", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + prior curated overlay + official filings",
        "record_count": 10, "raw_descriptions_present": 1, "raw_catalysts_verified": 10,
        "current_attachment_performance_rows_found": 0, "legacy_overlay_performance_values_discarded": 4,
        "direction_corrections": 6, "entity_corrections": 0, "security_type_corrections": 0,
        "ticker_performance_contaminations": 4, "security_normalizations": 10,
        "performance_rule": "No performance COPY in current attachment; four legacy WTW values belong to/rely on ticker-reuse series and were nullified",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"],
            "raw_direction": "Short", "research_direction": i["direction"], "security": i["security"],
            "description_chars": i["desc"], "catalyst_chars": i["cat"], "performance_available": False,
            "canonical_report": i["filename"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_056_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10,
        "copy_tables_present": ["catalyst", "companies", "descriptions"], "idea_rows_in_attachment": 0,
        "raw_descriptions_present": 1, "raw_descriptions_absent": 9, "raw_catalysts_verified": 10,
        "description_chars_by_idea": {i["id"]: i["desc"] for i in IDEAS},
        "catalyst_chars_by_idea": {i["id"]: i["cat"] for i in IDEAS},
        "performance_copy_present": False, "performance_rows_found": 0, "legacy_overlay_rows_nullified": 4,
        "note": "Current attachment controls. One STMP description is present; nine descriptions and all performance are absent. Four WTW legacy performance values were discarded due to ticker-reuse contamination.",
    }
    (ROOT / "data/curated/batch_056_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(out[key]) for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
