#!/usr/bin/env python3
"""Build Batch 045 ePlus / Plus500 / Brink's canonical V9 artifacts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-09"
WEIGHTS = [20, 18, 18, 16, 16, 12]


def claim(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return dict(title=title, original=original, evidence=evidence, assumption=assumption,
                falsifier=falsifier, actual=actual, verdict=verdict, lesson=lesson)


def source(title, url, publisher, date, evidence, kind="1차자료"):
    return dict(title=title, url=url, publisher=publisher, date=date, evidence=evidence, kind=kind)


EPLUS_BUSINESS = (
    "ePlus는 기업·공공기관의 서버·네트워크·보안·클라우드 장비를 설계·조달·구축하는 VAR/IT services와 장비 금융·리스를 결합한다. "
    "현금엔진은 `product gross profit + service gross profit + lease spread·residual recovery - 인력·판관비 - 운전자본 - 세금·capex`다. "
    "따라서 총매출보다 gross profit dollars, service mix, 매출채권·재고 회전, lease credit와 recourse/non-recourse debt 구분이 중요하다."
)
PLUS500_BUSINESS = (
    "Plus500은 자체 플랫폼에서 CFD·주식·선물 거래를 제공한다. 경제엔진은 `active customers × ARPU - AUAC × 신규고객 - platform/compliance cost "
    "+ customer trading P&L`이다. Customer income과 market P&L을 분리해야 반복 가능한 spread/premium 수익을 볼 수 있다. 핵심 KPI는 active/new customers, "
    "ARPU, AUAC, churn, 지역별 규제·leverage cap, customer deposits, cash return과 비-OTC 매출이다."
)
BCO_BUSINESS = (
    "Brink's는 현금·귀중품 운송, ATM replenishment, cash processing, vault outsourcing, smart safe와 국제 valuables logistics를 제공한다. "
    "노선 밀도가 높은 지역일수록 같은 차량·인력·시설에 더 많은 stop을 얹어 단위비용이 낮아진다. 현금엔진은 `organic revenue·price/mix + route density savings "
    "- labor·fleet·security - restructuring·integration - capex·pension·interest`이며, adjusted EBITDA보다 FCF conversion과 인수 후 순부채가 common equity를 결정한다."
)


EPLUS_SOURCES = [
    source("ePlus FY2009 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm", "SEC / ePlus", "2009-06-16", "filing 정상화·2008-09-03 NASDAQ 재상장과 당시 balance sheet 검증"),
    source("ePlus FY2010 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm", "SEC / ePlus", "2010-06", "technology/financing segment와 recourse/non-recourse 구조 검증"),
    source("ePlus FY2025 results", "https://www.eplus.com/who-we-are/investor-relations/press-releases/2025/05/eplus-reports-fourth-quarter-and-fiscal-year-2025-financial-results", "ePlus", "2025-05-22", "장기 technology/services scale와 financing mix 검증"),
]
PLUS500_SOURCES = [
    source("Plus500 2019 Annual Report", "https://cdn.plus500.com/media/Investors/Reports/Plus500_Annual_Report_19.pdf", "Plus500", "2020-03", "2019 revenue $354.5m·EBITDA $192.3m·margin 54%·EPS $1.35"),
    source("Plus500 2020 Annual Report", "https://cdn.plus500.com/media/Investors/Reports/Plus500_Annual_Report_20.pdf", "Plus500", "2021-03", "revenue $872.5m·customer income $997.5m·market P&L -$125m·EBITDA $515.9m"),
    source("Plus500 FY2023 results", "https://cdn.plus500.com/media/Investors/Reports/Plus500_Preliminary_Results_FY2023.pdf", "Plus500", "2024-02", "$365.1m shareholder returns와 2023 실행 검증"),
    source("Plus500 FY2025 results", "https://cdn.plus500.com/Media/Investors/Reports/Plus500_Preliminary_Results_FY2025.pdf", "Plus500", "2026-02", "revenue $792.4m·EBITDA $348.1m·active/new customers·AUAC 검증"),
]
BCO_SOURCES = [
    source("Brink's 2010 Form 10-K", "https://www.sec.gov/Archives/edgar/data/78890/000007889010000008/form_10-k.htm", "SEC / Brink's", "2010-02", "2009 revenue $3.1bn·segment operating profit $213m·6.8% margin"),
    source("Brink's 2012 Form 10-K", "https://www.sec.gov/Archives/edgar/data/78890/000007889012000013/form_10-k.htm", "SEC / Brink's", "2012-02", "revenue $3.9bn·operating profit $231m·5.9% margin"),
    source("Brink's 2014 Form 10-K", "https://www.sec.gov/Archives/edgar/data/78890/000007889015000009/form_10k.htm", "SEC / Brink's", "2015-02", "2014 revenue $3.6bn·operating margin 6.7%와 지역별 실행 검증"),
    source("Brink's Q2 2017 investor presentation", "https://investors.brinks.com/static-files/30e67d67-1ab3-46c8-95f6-611c1064ee77", "Brink's", "2017-07", "Q2 margin 7.9%, FY17 guidance와 2019 target bridge"),
    source("Brink's 2020 Form 10-K", "https://www.sec.gov/Archives/edgar/data/78890/000007889021000014/bco-20201231.htm", "SEC / Brink's", "2021-02", "COVID 충격·business resilience·leverage 경로 검증"),
    source("Brink's FY2025 results", "https://investors.brinks.com/news-releases/news-release-details/brinks-announces-fourth-quarter-and-full-year-2025-results/", "Brink's", "2026-02-26", "FY2025 revenue $5.261bn·adjusted EBITDA $977m·18.6% margin·FCF conversion 45%"),
]


IDEAS = [
    dict(id="cbe4657d-58c3-4f96-a9ee-619f5836ee99", date="2008-06-09", author="zach721", ticker="PLUS", company="ePlus inc.", raw_short=False, direction="Long", entry="$10.80", horizon="12~24개월", filename="analysis/ideas/2008/2008-06-09_PLUS_eplus_long.md", link="https://www.valueinvestorsclub.com/idea/ePlus/3940078240", desc=6370, cat=9, business=EPLUS_BUSINESS, sources=EPLUS_SOURCES,
         title="현금·TBV 할인과 filing/relisting의 마지막 구간을 산 Long", verdict="filing·재상장 촉매 성공, $28~30 목표·정확한 투자수익은 미검증", score=8.0, process=8.0,
         summary="$90m 시가총액에서 cash $65m, 첫 9개월 EBIT $24.2m, TBV 대비 70%라는 극단적 자산·이익 할인을 샀다. 세 개 분기와 한 개 10-K 제출로 공시는 current 상태였고 3/31/08 10-K와 NASDAQ relisting이 마지막 gate였다. Raw와 실제 방향은 모두 Long이다.",
         valuation="Cash 약 $8/share, 2007-12-31 TBV $15.75와 예상 $18.50+, FY2008 EPS 약 $2를 근거로 120% TBV는 $28, 10x EPS+cash는 $30을 제시했다. 청산 bridge는 A/R $108.45m+lease investment $161m-unguaranteed residual $18m-AP $85m-nonrecourse debt $104.7m으로 약 $14.77/share cash 가능성을 계산했다. 다만 영업운전자본과 lease runoff timing을 즉시 배분가능 현금으로 보면 과대평가다.",
         actual="회사는 2008-06 말 FY2008 10-K를 제출했고 2008-09-03 NASDAQ에 재상장했다. 이익·book·현금으로 버티는 special situation의 핵심 event는 적중했다. 장기적으로 ePlus는 대형 technology/services 회사로 성장했지만, 그 사실은 당시 $28~30 target의 1~2년 달성 증거와 별개다.",
         price="SQL performance row가 없다. 직전 원문이 명시한 $10.80을 entry anchor로 쓰되 corporate-action-adjusted 일별 total-return series를 복원하지 못했으므로 1/3/5년 수익률·IRR은 비워 둔다.",
         drivers="수익의 직접 driver는 싸다는 사실보다 remaining filing을 끝내 buyer universe와 liquidity를 회복한 것이었다. Cash/TBV는 duration을 견디게 했지만 macro와 thin margin 때문에 target multiple까지 자동으로 보장하지 않았다.",
         error="forecast TBV와 lease runoff cash에 충분한 working-capital·credit·duration haircut을 적용하지 않았고, relisting 성공과 $30 rerating을 하나의 사건처럼 묶었다.", first_signal="2008-06-30 10-K deadline가 밀리거나 relisting application이 지연되면 timing thesis를 낮춰야 했다.",
         metrics=[("시가총액/현금", "$90m / $65m", "현금가치 실현", "balance sheet 생존", "성공"),("첫 9개월 EBIT", "$24.2m", "정상수익 지속", "장기 사업성장", "장기 성공"),("TBV/share", "$15.75→$18.50+E", "$28 target", "target return 미복원", "미검증"),("EPS", "$2 run-rate", "$2.30·10x+cash", "exact horizon 미검증", "미검증"),("NASDAQ", "Pink Sheets/current filings", "재상장", "2008-09-03", "성공")],
         timeline=[("2007-12-31","TBV $15.75","asset anchor"),("2008-06-09","VIC Long","$10.80·$28~30 target"),("2008-06","FY2008 10-K","filing gate 통과"),("2008-09-03","NASDAQ relisting","핵심 catalyst"),("2009-03-31","FY2009","사업·balance sheet 생존"),("2025","financing mix 전환","장기 core value 확인")],
         claims=[
             claim("현금·TBV가 common 하방을 지지", "$90m market cap의 $65m이 cash이고 price는 TBV의 70%다.", "$8 cash/share·$15.75 TBV", "현금이 영업에 묶이지 않고 lease asset이 회수된다.", "credit loss·WC 소요로 adjusted TBV가 price 아래면 반증.", "balance sheet는 event duration을 버텼다.", "성공/재해석", "cash는 excess와 operating minimum을 분리한다."),
             claim("FY08 약 $2 EPS는 반복 가능", "첫 3분기 NI $1.65/share로 연간 $2 수준이다.", "first-nine-month EBIT $24.2m", "professional fee·license gain을 정상화해도 earnings가 유지된다.", "다음 4분기 core gross profit·CFO가 꺾이면 반증.", "사업은 장기 성장했지만 해당 horizon EPS bridge는 제한적이다.", "부분 성공", "reported EPS를 gross profit·WC·one-off로 분해한다."),
             claim("마지막 10-K가 listing gate", "3Q와 1K를 냈고 3/31/08 10-K 뒤 재상장한다.", "filings current·마지막 연차보고서", "감사·거래소 요건에 추가 결함이 없다.", "10-K/신청이 지연되면 catalyst timing 실패.", "2008-09-03 재상장했다.", "강한 성공", "event tree는 filing과 exchange approval을 분리한다."),
             claim("non-recourse debt 감소가 순자산을 연다", "recourse debt 상환, non-recourse debt 33% 감소다.", "lease-backed funding 구조", "fraud recourse·residual loss가 없다.", "lender claim이 corporate recourse로 전환되면 반증.", "회사는 net-cash 형태로 생존했다.", "성공", "debt는 법적 recourse와 asset coverage로 분류한다."),
             claim("고객승리와 VAR scale이 EPS를 키운다", "Dow Chemical·Coca-Cola Bottling 수주가 성장근거다.", "대형고객 wins", "매출이 gross profit과 cash로 전환된다.", "sales만 늘고 margin/CFO가 정체하면 반증.", "장기 scale은 커졌으나 개별 고객 기여는 미분리다.", "장기 성공", "수주는 backlog보다 gross profit dollars로 검증한다."),
             claim("$28~30 rerating", "120% TBV 또는 10x EPS+cash를 적용한다.", "NSIT 10x EPS·180% TBV 비교", "OTC 할인 제거 후 peer multiple이 적용된다.", "재상장 후에도 target 미달이면 valuation catalyst 실패.", "재상장은 성공했지만 exact target 달성은 미검증이다.", "미검증", "event 성공과 multiple target을 별도 claim으로 둔다."),
         ]),
    dict(id="4ac6396a-4fcc-43d2-9d86-0ac0c4dc9ee3", date="2014-02-07", author="conway968", ticker="BCO", company="The Brink's Company", raw_short=True, direction="Short", entry="$27.73 next-day close", horizon="12~24개월", filename="analysis/ideas/2014/2014-02-07_BCO.md", link="https://www.valueinvestorsclub.com/idea/BRINKS_CO/4247926128", desc=19145, cat=0, business=BCO_BUSINESS, sources=BCO_SOURCES,
         title="13x forward EBIT에 완전한 turnaround가 반영됐다는 Short", verdict="1년 Short 성공, 3/5년 보유 시 self-help rerating으로 큰 실패", score=7.0, process=8.0,
         summary="원문과 raw가 일치하는 Short다. Legacy pension과 Venezuela GAAP를 조정하면 BCO가 peer range 상단인 약 13x forward EBIT에 거래되고, turnaround를 전부 인정한 SOTP도 $28이라는 주장이다. NA는 barely profitable·capital intensive·pricing power가 약하고 Loomis/Garda 대비 실행이 뒤처진다고 봤다.",
         valuation="Full-credit turnaround SOTP $28이 market value와 비슷하므로 downside가 크고 upside가 제한적이라는 구조다. Short의 핵심은 단순 낮은 margin이 아니라 market price가 margin closure를 이미 base에 넣었는데 management가 목표를 반복 수정했다는 expectations gap이다.",
         actual="Short corrected return은 1년 +17.49%로 초기 valuation/timing이 적중했다. 그러나 3년 -48.65%, 5년 -151.23%로 장기 보유하면 손실이 커졌다. 이후 CEO 교체와 강한 self-help가 원문의 '실행 불가/commodity' 판단을 반박했다. 단순 short return은 `1-price ratio`이며 borrow·dividend·position rebalancing을 제외한다.",
         price="DB next-day close $27.7328. Short corrected: 1개월 +1.85%, 3개월 +19.04%, 6개월 +12.95%, 1년 +17.49%, 2년 +1.42%, 3년 -48.65%, 5년 -151.23%. Short 손실은 100%를 넘을 수 있다.",
         drivers="초기 수익은 과도한 turnaround 기대와 계속된 execution miss가 만들었다. 장기 손실은 management regime change·route optimization·M&A가 margin ceiling을 높이고 multiple을 재평가한 데서 나왔다.",
         error="현 management의 실패를 business의 영구적 구조로 외삽했고, short의 가장 큰 위험인 새로운 실행주체·activist/self-help option과 기간별 cover rule을 충분히 두지 않았다.", first_signal="CEO/board change와 구체적 margin KPI가 등장하고 2개 분기 연속 margin beat가 나면 Short를 축소해야 했다.",
         metrics=[("Entry", "$27.73", "$28 full-credit FV 이하", "1Y short +17.49%", "성공"),("Forward EBIT", "약 13x", "multiple 압축", "초기 압축", "성공"),("2014 margin", "turnaround 의심", "미달/실망", "6.7%", "초기 지지"),("3Y Short", "Short", "하락", "-48.65%", "실패"),("5Y Short", "Short", "하락", "-151.23%", "대실패")],
         timeline=[("2014-02-07","VIC Short","$28 SOTP"),("2014-05","3M short +19.04%","초기 적중"),("2015-02","1Y +17.49%","horizon 성공"),("2016","leadership/self-help reset","반증 시작"),("2017","Pertz margin plan","구조 변화"),("2017-02","3Y -48.65%","cover 실패"),("2019-02","5Y -151.23%","장기 short 실패")],
         claims=[
             claim("13x forward EBIT에 turnaround가 반영", "legacy 조정 뒤 peer range 상단이다.", "full-credit SOTP $28", "multiple/earnings 기대가 더 오르지 않는다.", "guidance 상향·credible new plan이면 반증.", "1년은 성공, 장기는 rerating했다.", "기간부 성공", "Short는 price expectations와 catalyst window를 명시한다."),
             claim("NA franchise가 commodity", "barely profitable·capital intensive·pricing power가 약하다.", "Loomis/Garda margin gap", "route density와 brand가 구조를 바꾸지 못한다.", "pricing·route productivity가 개선되면 반증.", "후속 self-help가 margin을 크게 개선했다.", "장기 실패", "현재 poor execution과 structural ceiling을 구분한다."),
             claim("management가 반복적으로 miss", "turnaround outlook을 여러 번 수정했다.", "목표 하향·실행 기록", "동일 team/process가 계속된다.", "CEO/board/compensation reset이면 thesis 재작성.", "새 leadership이 들어와 반증했다.", "초기 성공/구조 반증", "사람이 바뀌면 base rate도 갱신한다."),
             claim("high-value service 전환 실패", "higher-value mix가 margin을 못 올렸다.", "NA profit·capital intensity", "고객이 추가서비스에 지불하지 않는다.", "smart safe/CMS mix와 retention이 개선되면 반증.", "후속 서비스·outsourcing 전략이 성장했다.", "장기 실패", "product label보다 revenue/stop·ROIC를 본다."),
             claim("LatAm/Venezuela가 quality discount", "GAAP와 pension 조정 뒤에도 비싸다.", "high-inflation accounting·legacy claims", "현금 remittance·FX가 earnings를 소진한다.", "지역 mix가 cash earnings로 전환되면 반증.", "business는 장기 확장했다.", "부분", "고인플레 P&L은 현금·통화별로 재작성한다."),
             claim("$28 SOTP가 cover anchor", "turnaround를 전부 줘도 upside가 없다.", "probability-weighted SOTP", "새 전략 옵션이 없다.", "credible plan이 FV를 상향하면 cover.", "5년 ratio 2.51x로 anchor가 무너졌다.", "장기 실패", "Short valuation에는 explicit stop/cover rule이 필요하다."),
         ]),
    dict(id="88c3b3a4-83c8-43be-91ba-1b3941a7337a", date="2017-05-12", author="oldyeller", ticker="BCO", company="The Brink's Company", raw_short=True, direction="Long", entry="$56.95 next-day close", horizon="2~3년", filename="analysis/ideas/2017/2017-05-12_BCO.md", link="https://www.valueinvestorsclub.com/idea/Brinks/2434628612", desc=6694, cat=277, business=BCO_BUSINESS, sources=BCO_SOURCES,
         title="Doug Pertz 실행력과 peer margin gap closure Long", verdict="방향교정·1/2년 execution 성공, 3년 COVID 경로로 thesis 수익 소멸", score=7.5, process=8.5,
         summary="Raw Short지만 원문은 CEO Doug Pertz의 운영개선과 rerating을 산 Long이다. Recall·Culligan·IMC·Danaher 등 reference check에서 top 5% CEO 평가를 받고, 더 작은 peer도 높은 margin을 내므로 BCO gap은 구조보다 실행 문제라고 봤다.",
         valuation="가치는 revenue growth보다 margin bridge와 FCF/share에서 나왔다. Q2 2017 actual revenue $760m, operating margin 7.9% vs 5.5%, EBITDA $91m/12%였다. FY17 guidance는 revenue $3.18bn, op margin 8.5~8.8%, EBITDA $415~425m, EPS $2.95~3.05; 2019 target은 op profit $400m/margin 11.3%, EBITDA $560m, EPS $4.25였다.",
         actual="Long corrected return은 1년 +22.29%, 2년 +27.92%로 operating thesis가 적중했다. 3년 -35.25%는 2020 COVID shock이 cash logistics volume·leverage 우려를 때린 시점이고, 5년 -2.67%로 초기 이익이 소멸했다. 1~2년 성공과 장기 path risk를 분리해야 한다.",
         price="DB next-day close $56.9486. Long corrected: 1개월 +7.66%, 3개월 +23.82%, 6개월 +29.76%, 1년 +22.29%, 2년 +27.92%, 3년 -35.25%, 5년 -2.67%.",
         drivers="초기 수익은 Pertz team의 빠른 cost/route execution과 guidance credibility가 만들었다. 이후 acquisition/leverage와 COVID volume shock이 common equity duration을 훼손했다. 이 exogenous shock은 T0 business thesis 오류와 구분하지만 position sizing에는 포함해야 한다.",
         error="CEO reference check를 구체 KPI로 잘 번역했지만, operating leverage의 downside·M&A leverage·tail event에서 cash handling volume이 동시에 꺾이는 경로를 약하게 봤다.", first_signal="organic growth보다 acquisitions가 커지고 net leverage가 상승하거나, FCF conversion이 EBITDA 증가를 따라가지 못하면 risk budget을 낮춰야 했다.",
         metrics=[("Entry", "$56.95", "margin rerating", "+22.29% 1Y", "성공"),("Q2 op margin", "7.9% vs 5.5%", "2019 11.3%", "초기 빠른 개선", "성공"),("FY17 EBITDA", "$415~425m guide", "execution", "guidance 신뢰 상승", "성공"),("3Y Long", "Long", "상승", "-35.25%", "path 실패"),("5Y Long", "Long", "compound", "-2.67%", "실패/회복 미완")],
         timeline=[("2016","Doug Pertz 취임","새 execution regime"),("2017-05-12","VIC Long","margin gap thesis"),("2017-Q2","margin 7.9%","초기 증거"),("2018-05","1Y +22.29%","성공"),("2019-05","2Y +27.92%","지속"),("2020-05","3Y -35.25%","COVID shock"),("2022-05","5Y -2.67%","회복 불충분")],
         claims=[
             claim("raw Short가 아니라 Long", "improved operations와 valuation을 기대했다.", "earnings beats·rerating catalysts", "common equity 상승 payoff다.", "원문이 decline을 목표로 하면 반증.", "1/2년 성과가 Long 논지와 일치했다.", "교정 성공", "본문의 catalyst 방향으로 flag를 감사한다."),
             claim("Pertz는 high-quality operator", "다수 reference가 top 5% CEO라고 평가했다.", "과거 기업 운영기록·Recall team 영입", "과거 playbook이 BCO에 이식된다.", "key hires 이탈·KPI miss면 반증.", "2017 margin/guide가 빠르게 개선됐다.", "성공", "CEO thesis는 100일·1년 KPI로 바꾼다."),
             claim("peer margin gap은 구조적이지 않다", "작고 brand가 약한 peers도 더 높은 margin이다.", "고객·경쟁사·공급자 fieldwork", "country/labor mix가 gap을 설명하지 않는다.", "동일 density 조정 뒤 gap 지속이면 반증.", "self-help가 margin을 올렸다.", "성공", "peer gap은 mix-adjusted unit economics로 검증한다."),
             claim("earnings beat가 credibility를 만든다", "execution이 consensus보다 빠르면 multiple이 오른다.", "Q2 7.9% margin·FY guide", "savings가 일회성 cut이 아니다.", "organic service quality/retention 악화면 반증.", "1/2년 rerating이 발생했다.", "성공", "beat의 질을 organic·cash로 분해한다."),
             claim("M&A와 asset swaps가 density를 높인다", "accretive acquisitions·asset swaps가 local routes를 강화한다.", "management playbook", "purchase multiple·integration cash가 synergy 아래다.", "leverage 상승·FCF dilution이면 반증.", "scale은 커졌지만 tail exposure도 확대됐다.", "혼합", "deal은 post-synergy multiple이 아니라 realized ROIC로 본다."),
             claim("buyback이 per-share upside", "opportunistic repurchases가 cheap equity를 줄인다.", "capital allocation catalyst", "share price가 intrinsic value 아래다.", "debt-funded 고가 buyback이면 반증.", "COVID 시기 common path가 약해졌다.", "미검증/혼합", "buyback은 leverage와 cycle-adjusted value를 함께 본다."),
         ]),
    dict(id="16123d39-11e5-4118-970c-14c4aad7a689", date="2018-05-17", author="mryoshi", ticker="BCO", company="The Brink's Company", raw_short=True, direction="Short", entry="$66.81 next-day close", horizon="12~24개월", filename="analysis/ideas/2018/2018-05-17_BCO.md", link="https://www.valueinvestorsclub.com/idea/The_Brinks_Company_/9393602176", desc=31799, cat=309, business=BCO_BUSINESS, sources=BCO_SOURCES,
         title="완전한 turnaround·LatAm 19.3% margin 기대를 판 Short", verdict="1년 timing 실패, 2년 COVID 수익은 논지와 분리, 3년 다시 실패", score=6.0, process=8.5,
         summary="BCO stock이 Starboard/new management로 3년간 약 150% 오른 뒤 full turnaround가 가격에 반영됐다고 본 Short다. 핵심 differentiated claim은 South America 2019E revenue CAGR 9%와 EBITDA margin 19.3%가 경쟁·cashless·은행지점 축소에 비해 과도하다는 것이었다.",
         valuation="LatAm revenue growth 5%, EBIT margin 13%를 적용했다. Scenario는 40%: 5.5x EV/EBITDA·$51.70, 30%: 7x·$77.37, 30%: DCF $35.58로 weighted target $54.56이었다. 당시 약 $66.81 대비 단순 downside 약 18%. Bull/short risk에는 outsourcing, smart safe, LBO, M&A roll-up과 real estate가 있었다.",
         actual="Short corrected return은 1년 -11.23%, 2년 +40.32%, 3년 -17.00%다. 2년 성과는 2020 COVID 충격과 겹쳐 cashless/LatAm margin thesis의 순수한 검증으로 볼 수 없다. 3년에는 주가가 다시 entry 위로 회복해 short의 지속가능성이 약했다. 5년 값은 SQL에 없다.",
         price="DB next-day close $66.8137. Short corrected: 1개월 -11.46%, 3개월 -9.26%, 6개월 +4.72%, 1년 -11.23%, 2년 +40.32%, 3년 -17.00%; 5년 null. Borrow·dividend·rebalancing 제외 단순 short return이다.",
         drivers="원문이 지적한 valuation과 LatAm 경쟁은 합리적이었지만, route outsourcing·smart safe·M&A가 terminal decline을 늦췄다. 2년 수익은 thesis-specific catalyst보다 pandemic beta가 컸고, cover하지 않으면 3년 손실로 되돌아갔다.",
         error="cashless adoption을 BCO revenue 감소로 직접 연결해 outsourcing share gain과 nominal pricing을 과소평가했고, probability-weighted target만 있고 catalyst별 cover/stop rule이 약했다.", first_signal="LatAm local-currency growth·margin이 guidance에 근접하고 high-value services/outsourcing이 core CIT 약화를 상쇄하면 Short conviction을 낮춰야 했다.",
         metrics=[("Entry/target", "$66.81 / $54.56", "약 18% downside", "1Y short -11.23%", "실패"),("LatAm growth", "mgmt 9% vs 5%", "miss", "exact attribution 제한", "혼합"),("LatAm EBIT margin", "19.3% vs 13%", "하향", "사업은 장기 성장", "부분"),("2Y Short", "Short", "하락", "+40.32%", "외생 shock 포함"),("3Y Short", "Short", "하락", "-17.00%", "실패")],
         timeline=[("2016-18","stock 약 +150%","expectations 상승"),("2018-05-17","VIC Short","$54.56 target"),("2018-08","3M short -9.26%","초기 adverse"),("2019-05","1Y -11.23%","timing 실패"),("2020-05","2Y +40.32%","COVID shock"),("2021-05","3Y -17.00%","회복·short reversal"),("2025","EBITDA margin 18.6%","self-help durability")],
         claims=[
             claim("turnaround가 가격에 전부 반영", "3년 +150% 뒤 consensus가 management target과 같다.", "약 8.5x EV/EBITDA·high expectations", "추가 option보다 execution miss 확률이 크다.", "guide 상향·FCF beat이면 반증.", "1년 주가가 더 올라 Short가 손실이었다.", "초기 실패", "좋은 expectations thesis에도 catalyst timing이 필요하다."),
             claim("LatAm 19.3% margin은 과도", "Brazil 13% EBIT이면 rest-of-LatAm EBITDA가 28.8%여야 한다.", "Brazil $56m/$434m·LatAm $178m/$924m", "Loomis/Prosegur 경쟁이 price를 낮춘다.", "margin이 guidance에 근접하면 반증.", "장기 consolidated margin은 크게 상승했다.", "혼합/장기 반증", "지역 mix·inflation을 같은 단위로 bridge한다."),
             claim("9% LatAm growth는 시장보다 높다", "시장 4%, Prosegur 6%인데 BCO 9%다.", "Brazil이 LatAm revenue 약 47%", "share gain·pricing이 gap을 못 메운다.", "local-currency organic growth가 9%에 근접하면 반증.", "exact T0 forecast audit은 제한적이다.", "미검증/부분", "nominal 고인플레 성장과 volume을 분리한다."),
             claim("cashless·e-commerce가 TAM을 줄인다", "Brazil fintech·mobile payment·은행지점 폐쇄가 현금수요를 낮춘다.", "branch/ATM decline·15% e-commerce growth", "outsourcing·cash circulation 증가가 상쇄하지 않는다.", "revenue/stop·CMS mix가 성장하면 반증.", "Brink's revenue는 2025 $5.261bn으로 확대됐다.", "직접 연결 실패", "TAM headwind와 outsource penetration을 함께 모델링한다."),
             claim("$54.56 probability-weighted value", "bear/base/DCF를 40/30/30으로 가중했다.", "$51.70/$77.37/$35.58", "scenario 확률과 5.5~7x multiple이 현실적이다.", "upside scenario probability 상승이면 반증.", "1Y·3Y에서 target 방향이 실패했다.", "실패", "확률은 catalyst 데이터로 갱신하고 cover rule을 둔다."),
             claim("M&A roll-up이 underlying miss를 가린다", "$400m/year deal guidance가 synergy를 부풀릴 수 있다.", "7.5x post-synergy spend·leverage risk", "integration cash와 debt가 EBITDA 증가를 상쇄한다.", "FCF/share·ROIC가 개선되면 반증.", "scale·margin은 장기 개선됐지만 path risk는 존재했다.", "혼합", "adjusted EBITDA보다 acquisition cohort ROIC를 본다."),
         ]),
    dict(id="d65501e4-930a-4c40-afc4-484cb651f3a8", date="2007-02-12", author="pirate681", ticker="BCO", company="The Brink's Company", raw_short=True, direction="Long", entry="$29.13 next-day close", horizon="12~24개월", filename="analysis/ideas/2007/2007-02-12_BCO.md", link="https://www.valueinvestorsclub.com/idea/The_Brinks_Company/8194665443", desc=16695, cat=462, business=BCO_BUSINESS, sources=BCO_SOURCES,
         title="보안물류+BHS SOTP와 activist value realization Long", verdict="방향교정·corporate action은 성공, 1/3/5년 common return은 부진", score=6.0, process=7.5,
         summary="SQL raw Short와 달리 원문은 2007E EV/EBITDA 7x 미만에서 $80 SOTP, 25%+ upside를 제시한 Long이다. BAX Global 매각대금으로 VEBA·부채를 정리하고 1천만주 이상 Dutch tender를 실행한 뒤 secure logistics와 고마진 Brink's Home Security를 분리/매각하는 activist 구조였다.",
         valuation="8.5~9x 2007E EV/EBITDA SOTP로 $80/share를 계산했고 consolidated 회사는 약 6.7x로 보았다. BAX 매각 $1.1bn에서 VEBA $225m, debt $185m 등을 정리한 자본배분과 BHS 1.1m subscribers·22%+ margin이 핵심이다. 다만 SQL next-day close $29.13은 원문 $80/25% 문맥과 큰 괴리가 있어 split/spin adjustment 가능성이 높다. 성과 multiplier는 corporate-action-adjusted DB 값을 그대로 사용하고 target gap 산술은 만들지 않는다.",
         actual="회사는 2008년 Brink's Home Security를 분리해 conglomerate simplification을 실행했다. 그러나 DB Long 성과는 1년 +3.76%, 3년 -27.43%, 5년 -26.21%였다. 자산가치·촉매를 맞혔어도 common의 실제 경로는 macro, 남은 cash-logistics economics와 분리 후 가치 귀속 때문에 약했다.",
         price="DB next-day close $29.1319. Long corrected return은 1개월 -3.63%, 3개월 +7.68%, 6개월 -5.90%, 1년 +3.76%, 3년 -27.43%, 5년 -26.21%다. 배당·세금·거래비용은 별도 반영하지 않은 DB multiplier 기반이다.",
         drivers="corporate action 자체보다 분할 뒤 각 security의 배분·잔여부채·시장환경이 수익을 결정했다. Activist와 SOTP는 방향을 열었지만 duration과 2008 crisis가 common compounding을 훼손했다.",
         error="gross SOTP에서 pension·tax leakage·stranded overhead와 분할 후 security별 beta를 충분히 빼지 않았고, strategic alternative 실행을 즉시 $80 value realization로 연결했다.", first_signal="Dutch tender와 strategic review가 끝난 뒤에도 consolidated discount가 닫히지 않거나 Europe margin이 회복되지 않으면 기대수익을 낮춰야 했다.",
         metrics=[("Next close", "$29.13", "$80 SOTP", "price scale 불일치", "target 산술 보류"),("EV/EBITDA", "약 6.7x", "8.5~9x", "corporate action 실행", "부분"),("1Y Long", "Long", "25%+", "+3.76%", "미달"),("3Y Long", "Long", "rerating", "-27.43%", "실패"),("5Y Long", "Long", "SOTP realization", "-26.21%", "실패")],
         timeline=[("2006","BAX Global sale $1.1bn","capital reset"),("2007-02-12","VIC Long","$80 SOTP"),("2007","Pirate board/strategy pressure","catalyst"),("2008","BHS separation","구조 단순화"),("2008 crisis","market/path shock","common 훼손"),("2010-02","3Y -27.43%","장기 outcome 실패"),("2012-02","5Y -26.21%","SOTP만으로 불충분")],
         claims=[
             claim("raw Short가 아니라 Long", "$80 SOTP와 25%+ upside를 제시했다.", "buy/undervaluation language", "security가 pre-spin BCO common이다.", "하락 payoff면 반증.", "원문은 명백한 Long이다.", "교정 성공", "raw boolean은 원문 payoff로 재검증한다."),
             claim("secure logistics가 6.7x로 저평가", "industry 약 8x보다 싸다.", "2007E EV/EBITDA", "margin·growth·liability가 peer와 유사하다.", "Europe/NA margin이 구조적으로 낮으면 반증.", "장기 common return은 peer gap을 충분히 닫지 못했다.", "부분 실패", "peer multiple 전에 quality gap을 bridge한다."),
             claim("BHS가 숨은 고마진 자산", "1.1m subscribers·22%+ margin의 #2 alarm platform이다.", "recurring subscriber economics", "분리비용·churn·capex가 제한적이다.", "subscriber value나 separation proceeds가 낮으면 반증.", "2008 separation은 실현됐다.", "촉매 성공", "자산 분리는 valuation과 distribution mechanics를 함께 본다."),
             claim("BAX proceeds가 per-share value", "$1.1bn sale 뒤 VEBA/debt와 tender를 실행한다.", "$225m VEBA·$185m debt·10m+ shares", "매입가격이 intrinsic value 아래다.", "proceeds가 liabilities에 더 많이 소진되면 반증.", "자본구조는 단순화됐지만 장기 return은 부진했다.", "부분 성공", "gross sale price보다 equity waterfall을 본다."),
             claim("activist가 strategic alternatives를 연다", "Pirate board seat·strategy committee가 sale/tender를 촉진한다.", "공개 activism", "다른 주주와 인센티브가 일치한다.", "review 종료·deal 부재면 반증.", "BHS 분리가 뒤따랐다.", "성공", "activist catalyst는 milestone·기간을 둔다."),
             claim("Europe recovery와 BHS growth가 upside", "margin recovery·subscriber growth가 earnings를 높인다.", "원문 catalyst", "macro와 경쟁이 개선을 허용한다.", "organic margin·subscribers 정체면 반증.", "corporate action과 달리 common return은 약했다.", "실패/혼합", "SOTP와 operating delivery를 독립 claim으로 둔다."),
         ]),
    dict(id="d3cab447-dd55-4112-9c72-c14ca05078e8", date="2010-06-13", author="AAOI", ticker="BCO", company="The Brink's Company", raw_short=True, direction="Long", entry="$17.86 next-day close", horizon="1~3년", filename="analysis/ideas/2010/2010-06-13_BCO.md", link="https://www.valueinvestorsclub.com/idea/BRINKS_CO/2908281389", desc=28749, cat=1085, business=BCO_BUSINESS, sources=BCO_SOURCES,
         title="일시비용 뒤 7~7.5% margin·12.2% FCF yield 정상화 Long", verdict="방향교정·margin normalization 성공, 1/3/5년 모두 양호", score=8.5, process=8.5,
         summary="Raw Short가 아니라 pure-play cash logistics의 normalized earnings를 산 Long이다. Venezuela·healthcare write-off, CIT contract loss와 Europe 우려가 2009/10 reported numbers를 눌렀지만 정상 margin 7~7.5%, depressed-base FCF yield 12.2%, dividend 2%, ROIC/ROE 15~20%를 제시했다.",
         valuation="2009 revenue 약 $3.1bn, operating profit $213m, margin 6.8%에서 7~7.5% 회복을 underwriting했다. 핵심은 one-off add-back만이 아니라 route density·가격·cost가 실제 cash margin으로 복귀하는지다. Unlevered balance sheet는 buyback/dividend/deal optionality를 만들었다.",
         actual="DB Long return은 1년 +33.93%, 3년 +30.89%, 5년 +61.51%다. 3개월 +8.03%, 6개월 +28.61%로 정상화가 비교적 빨리 가격에 반영됐다. 원문 방향·valuation·촉매 판정 모두 대체로 적중했다.",
         price="DB next-day close $17.8618. Corrected Long return: 1개월 -0.15%, 3개월 +8.03%, 6개월 +28.61%, 1년 +33.93%, 2년 +8.29%, 3년 +30.89%, 5년 +61.51%.",
         drivers="일시적 손실의 소멸, stand-alone cost discipline과 capital return 기대가 multiple·earnings를 함께 회복시켰다. 2년 수익이 +8.3%로 낮아진 경로는 좋은 thesis에도 holding-period volatility가 큼을 보여준다.",
         error="7.5% destination은 합리적이었지만 country inflation/FX, pension·UMWA cash와 contract pricing의 bridge를 더 명시했어야 한다. Insider buy와 potential buyout은 보조증거이지 core value가 아니다.", first_signal="분기 normalized margin이 6%대에 머물고 FCF conversion이 restructuring/pension 현금으로 소진되면 반증이었다.",
         metrics=[("Entry", "$17.86", "normalization", "+33.93% 1Y", "성공"),("Margin", "6.8% 2009", "7~7.5%", "후속 정상화", "성공"),("FCF yield", "12.2%", "rerating", "5Y +61.51%", "성공"),("3Y Long", "Long", "상승", "+30.89%", "성공"),("5Y Long", "Long", "상승", "+61.51%", "성공")],
         timeline=[("2009","margin 6.8%","depressed base"),("2010-06-13","VIC Long","normalization"),("2010-09","3M +8.03%","초기 확인"),("2010-12","6M +28.61%","rerating"),("2011-06","1Y +33.93%","성공"),("2013-06","3Y +30.89%","지속"),("2015-06","5Y +61.51%","장기 성공")],
         claims=[
             claim("raw Short가 아니라 Long", "mispricing·buyout upside를 제시했다.", "higher profits와 rerating payoff", "BCO common 매수다.", "원문이 하락을 목표로 하면 반증.", "성과도 Long 부호로 해석된다.", "교정 성공", "direction error는 postmortem 전체 부호를 바꾼다."),
             claim("write-off는 일시적", "Venezuela·healthcare·contract loss가 정상수익을 가렸다.", "one-off expense bridge", "같은 종류의 country/contract loss가 반복되지 않는다.", "조정항목이 매년 재발하면 반증.", "6~12개월 주가가 강하게 회복했다.", "성공", "one-off는 빈도와 cash nature를 추적한다."),
             claim("margin 7~7.5% 정상화", "stand-alone network가 historical earning power를 회복한다.", "2009 6.8% margin", "pricing·density·labor productivity가 개선된다.", "4Q rolling margin이 개선되지 않으면 반증.", "후속 결과와 1Y return이 지지했다.", "성공", "margin destination은 지역별 bridge로 만든다."),
             claim("12.2% FCF yield가 하방", "depressed base에서도 double-digit yield다.", "low leverage·2% dividend", "FCF가 pension/restructuring 전 숫자가 아니다.", "cash conversion이 낮으면 반증.", "5Y +61.5%로 valuation support가 작동했다.", "성공", "FCF는 legacy cash claim 뒤 equity cash로 측정한다."),
             claim("capital return 또는 accretive deal", "buyback·dividend increase·acquisition이 value를 연다.", "unlevered balance sheet", "management가 hurdle rate를 지킨다.", "비싼 deal·현금유보면 반증.", "주가성과는 좋았지만 촉매별 attribution은 불완전하다.", "부분 성공", "optionality는 실제 allocation으로만 점수화한다."),
             claim("insider buying/buyout이 signal", "Chairman 매수와 financial buyer 가능성이다.", "open-market purchase", "정보우위와 financing availability가 있다.", "거래 부재·후속 매도면 약화.", "operating normalization이 더 중요한 driver였다.", "보조 성공", "insider/LBO는 core thesis가 아니라 확률 가중 촉매다."),
         ]),
    dict(id="bda1795d-018f-4885-a3f3-60bd16772f48", date="2012-11-28", author="xanadu972", ticker="BCO", company="The Brink's Company", raw_short=True, direction="Long", entry="$24.34 next-day close", horizon="2~5년", filename="analysis/ideas/2012/2012-11-28_BCO.md", link="", desc=18870, cat=48, business=BCO_BUSINESS, sources=BCO_SOURCES,
         title="NA rationalization·LatAm hidden value·2014 FCF bridge Long", verdict="방향교정·장기 value realization 성공, 2년 drawdown 뒤 5년 +217%", score=8.5, process=9.0,
         summary="원문은 30~60% upside 뒤에도 2014 FCF yield 9~12%를 제시한 Long이다. Headline GAAP를 그대로 쓰지 않고 pension expected return, UMWA와 unallocated expense를 조정하고 NA excess capacity·LatAm EBIT mix·digital-wallet 공포를 분해했다.",
         valuation="2014E revenue $4.760bn, adjusted EBIT $432m, margin 9.1%, EPS $5.32, FCFF $287m/maintenance FCFF $289m을 전망했다. LatAm은 2014E revenue $2.202bn·EBIT $286m·13% margin, 전체 EBIT의 약 66%로 추정했다. 당시 upside 뒤에도 9~12% FCF yield라는 margin-of-safety였다.",
         actual="DB Long return은 1년 +23.33%, 2년 -18.95%, 3년 +21.91%, 5년 +217.37%다. 2014 actual company margin은 6.7%로 원문 9.1% forecast에 미달했지만, 이후 management/self-help와 rerating이 5년 성과를 크게 만들었다. 숫자 target의 시간은 틀렸고 구조적 optionality는 맞았다.",
         price="DB next-day close $24.3379. Corrected Long return: 1개월 +1.84%, 3개월 -4.66%, 6개월 -0.92%, 1년 +23.33%, 2년 -18.95%, 3년 +21.91%, 5년 +217.37%.",
         drivers="즉시 2014 forecast delivery가 아니라 오랜 NA cost reset, LatAm franchise value와 이후 Pertz 체제의 강한 self-help가 terminal value를 키웠다. 2년 drawdown은 valuation이 싸도 catalyst duration을 버틸 자본이 필요함을 보여준다.",
         error="2014 margin 9.1%로 정상화를 너무 앞당겼고, LatAm inflation/FX와 capital lease·maintenance capex를 정밀하게 stress하지 않았다. 반면 legacy liability와 unallocated expense를 명시적으로 조정한 점은 강했다.", first_signal="2013~14 NA rationalization에도 consolidated margin이 9.1%로 가지 못한 것이 timing 반증이었다. Exit보다 horizon reset이 합리적이었다.",
         metrics=[("2014E revenue", "$4.760bn", "6% growth", "2014 $3.6bn", "미달"),("2014E margin", "9.1%", "cost rationalization", "6.7%", "미달"),("2014E EPS", "$5.32", "30~60% upside", "exact comparable 미복원", "미검증"),("2Y Long", "Long", "상승", "-18.95%", "timing 실패"),("5Y Long", "Long", "value realization", "+217.37%", "강한 성공")],
         timeline=[("2012-11-28","VIC Long","30~60% upside"),("2013","margin 6.8%","bridge 지연"),("2014","margin 6.7%","9.1% 미달"),("2014-11","2Y -18.95%","duration test"),("2015-11","3Y +21.91%","회복"),("2017","Pertz plan 가속","self-help"),("2017-11","5Y +217.37%","강한 outcome")],
         claims=[
             claim("raw Short가 아니라 Long", "30~60% upside와 높은 residual FCF yield를 제시했다.", "upside·buy thesis", "BCO common security다.", "하락 target이면 반증.", "Long corrected 성과가 적용된다.", "교정 성공", "direction은 valuation payoff로 확정한다."),
             claim("NA 30% excess capacity를 rationalize", "Brink's trucks는 Garda보다 revenue productivity가 40% 높아 cost가 문제다.", "CEO change·cost/capex cuts", "가격경쟁이 완화되고 labor/fleet를 줄일 수 있다.", "margin이 2014에도 정체하면 timing 반증.", "2014 6.7%로 forecast는 미달, 이후 개선했다.", "지연 성공", "self-help에는 실행주체·현금비용·기간을 붙인다."),
             claim("LatAm이 숨은 EBIT 65%", "revenue mix보다 EBIT contribution이 훨씬 높다.", "2014E LatAm EBIT $286m·13% margin", "FX/inflation·competition에도 pricing power가 유지된다.", "local-currency organic margin 악화면 반증.", "LatAm은 핵심 가치였지만 exact 2014 forecast는 공격적이었다.", "부분 성공", "고인플레 지역은 nominal growth와 real economics를 분리한다."),
             claim("Mexico ownership가 moat", "외국 보안회사 제한 전 1965 지분으로 operating right가 희소하다.", "Serpaprosa remaining 80% acquisition", "regulatory right가 pricing/ROIC로 이어진다.", "underinvestment·related-party 문제가 지속되면 반증.", "지역 franchise는 지속됐다.", "성공", "규제 moat는 실제 margin과 cash remittance로 검증한다."),
             claim("Digital-wallet 공포가 과도", "현금 대체 우려가 valuation을 누른다.", "outsourcing·emerging-market cash circulation", "payment digitization보다 outsourced wallet share가 빠르다.", "cash logistics volume 구조감소면 반증.", "Brink's는 2025까지 더 큰 cash-management 사업으로 남았다.", "성공/재해석", "TAM 감소와 outsourcing share gain을 동시에 모델링한다."),
             claim("2014 $432m EBIT·$287m FCFF", "9.1% margin이면 9~12% yield가 남는다.", "pension/UMWA/unallocated 조정", "normalization이 2년 안에 실현된다.", "2014 margin·FCF 미달이면 timing 실패.", "2014 margin 6.7%, 2Y return -18.95%였다.", "timing 실패", "좋은 terminal thesis도 연도별 bridge가 틀릴 수 있다."),
         ]),
    dict(id="cda3b447-bd2c-4793-a346-63187380e487", date="2019-08-26", author="avahaz", ticker="PLUS", company="Plus500 Ltd.", raw_short=True, direction="Long", entry="공시 배수 기준", horizon="약 2년", filename="analysis/ideas/2019/2019-08-26_PLUS500_long.md", link="", desc=14240, cat=84, business=PLUS500_BUSINESS, sources=PLUS500_SOURCES,
         title="ESMA 후 정상수익과 과도한 규제 공포를 산 contrarian Long", verdict="방향·entity 교정 및 2년 total return 약 150%로 강한 성공", score=9.0, process=8.5,
         summary="SQL의 ePLUS/Short는 모두 틀린 분류다. 실제 회사는 영국 Plus500이고 원문은 Long이다. ESMA leverage 제한 이후 네 분기 데이터를 보고 2019E 3x EV/EBIT·6x P/E, 2020 run-rate 2x EBIT, 배당+buyback 12%를 근거로 시장이 earnings power를 과소평가했다고 주장했다.",
         valuation="IG/CMC의 forward EBIT 6x/8x 대비 Plus500 3x, 다음 해 run-rate 2x였다. 12% current-market-cap cash return과 향후 mid-teens를 기대했다. valuation의 관건은 reported EBITDA에서 volatile customer trading P&L을 빼고 spread/premium earnings를 normalise하는 것이다.",
         actual="2021년 같은 작성자의 follow-up은 주가가 두 배가 됐고 배당 포함 약 150% total return이라고 명시했다. FY2019 revenue $354.5m·EBITDA $192.3m 뒤 FY2020 revenue $872.5m·EBITDA $515.9m으로 earnings power가 강하게 확인됐다. 이는 SQL performance 대체 계산이 아니라 후속 원문에 기록된 검증치다.",
         price="SQL performance row는 없지만 2021-09-03 후속 원문이 약 2년 total return nearly 150%를 직접 기록한다. 따라서 1년·3년·5년은 null, 원 horizon 2년은 정성/원문 검증으로만 사용한다.",
         drivers="핵심 driver는 ESMA 이전 매출을 되찾는 것이 아니라 더 낮은 AUAC·churn과 잔존 고객 economics가 만든 post-regulation earnings였다. 2020 변동성은 추가 upside였지만 thesis success를 전부 시장 P&L로 설명하면 안 된다.",
         error="규제 후 네 분기 관찰은 강점이지만 Australia impact·advertising channel concentration·customer P&L tail을 완전히 제거하지 못했고, 낮은 배수의 일부는 governance/communication discount였다.", first_signal="professional conversion·EEA retail run-rate·AUAC/churn이 두 분기 연속 악화되면 post-ESMA unit economics 반증이었다.",
         metrics=[("2019E EV/EBIT", "3x", "peer gap 축소", "2년 total return 약 150%", "성공"),("2019E P/E", "6x", "rerating", "earnings 급증", "성공"),("Cash return", "12% market cap", "mid-teens 지속", "대규모 환원 지속", "성공"),("Q2 EBITDA", "$54m", "$200m+ run-rate", "FY19 $192.3m", "근접"),("2년 total return", "Long", "강한 upside", "nearly 150%", "강한 성공")],
         timeline=[("2018-08","ESMA leverage caps","새 economics 시작"),("2019-Q1","-$28m market P&L","sentiment 저점"),("2019-Q2","EBITDA $54m·AUAC 956","unit economics 증거"),("2019-08-26","VIC Long","raw Short/entity 교정"),("2020","revenue $872.5m","earnings inflection"),("2021-09-03","follow-up","2년 total return 약 150%")],
         claims=[
             claim("raw Short/ePlus가 아니라 Plus500 Long", "Shares가 지나치게 싸고 규제 후 성장한다고 주장했다.", "3x EV/EBIT·6x P/E·cash return", "entity와 런던 상장 security가 정확하다.", "원문 payoff가 하락을 목표로 하면 반증.", "2021 follow-up이 약 150% total return을 확인했다.", "교정·투자 성공", "ticker collision은 company identity와 거래소로 해결한다."),
             claim("ESMA 후 earnings power가 $200m+", "Q2 $54m EBITDA가 consensus run-rate를 넘는다.", "active 108k·new 26.2k·churn 16%", "낮은 volatility에도 cohort economics가 유지된다.", "customer income·EBITDA가 연속 하락하면 반증.", "FY19 EBITDA $192.3m, FY20 $515.9m이었다.", "성공", "규제 shock은 post-rule cohort로 다시 underwriting한다."),
             claim("EEA retail이 다시 성장", "Q2 $31.5m, annualized $126m으로 Q4 exit보다 성장했다.", "post-ESMA four-quarter data", "professional 전환 없이 retail ARPU·retention이 안정된다.", "EEA revenue가 다시 구조적 감소하면 반증.", "전체 platform earnings는 강하게 회복했다.", "성공", "규제 전 절대액보다 규제 후 저점 대비 slope를 본다."),
             claim("AUAC 하락이 margin을 회복", "AUAC 956은 YoY -25%, QoQ -22%다.", "new customers 26.2k", "낮은 cost가 질 나쁜 cohort 때문이 아니다.", "12개월 LTV/AUAC가 악화되면 반증.", "FY20 scale economics가 강하게 나타났다.", "성공", "CAC는 retention·ARPU cohort와 함께 본다."),
             claim("12% cash return이 기다림을 보상", "dividend+buyback이 market cap 12%다.", "현금창출·순현금", "규제 capital·acquisition으로 payout이 막히지 않는다.", "환원 축소·dilutive deal이면 반증.", "회사는 이후에도 대규모 buyback/dividend를 지속했다.", "성공", "싼 financial platform은 실제 share count와 dividend로 검증한다."),
             claim("Founder 매수는 정보신호", "Alon Gonen이 IPO 후 처음 $14m을 매수했다.", "H1 results 뒤 open-market buy", "내부자가 sustainable earnings를 더 잘 안다.", "insider 매수 뒤 unit economics 악화면 신호 무효.", "성과와 방향은 일치했다.", "성공", "insider signal은 thesis evidence의 보강이지 대체가 아니다."),
         ]),
    dict(id="fccdf24a-81ed-4330-803f-26da2a529b35", date="2021-09-03", author="avahaz", ticker="PLUS", company="Plus500 Ltd.", raw_short=False, direction="Long", entry="약 6x sustainable P/E", horizon="2년", filename="analysis/ideas/2021/2021-09-03_PLUS500_long.md", link="https://www.valueinvestorsclub.com/idea/Plus500/5585479211", desc=5740, cat=112, business=PLUS500_BUSINESS, sources=PLUS500_SOURCES,
         title="기존 CFD cash cow와 Invest·US futures 옵션을 함께 산 Long", verdict="사업·환원·다각화는 성공, 2년 100% target은 데이터로 미확정", score=7.5, process=8.0,
         summary="2019 Long의 약 150% 수익 뒤에도 추가 2년 double을 제시했다. 기존 business sustainable EPS >$3를 6x에 사고, net cash 약 $700m의 절반이 excess, 최소 50% payout으로 8% dividend yield를 받으면서 Plus500 Invest와 Cunningham/US futures를 무료 옵션처럼 보았다.",
         valuation="2023 ex-USA EPS 약 $4에 10x exit P/E를 적용해 100% upside를 계산했다. Base downside는 Invest·US 실패와 trading stagnation에도 6x P/E+double-digit shareholder return이다. 핵심 오류 가능성은 peak 2020/21 customer activity를 sustainable EPS에 포함하고, new vertical의 CAC·regulatory capital·execution cost를 option value에서 빼지 않는 것이다.",
         actual="FY2023 회사는 $365.1m을 dividend/buyback으로 돌려줬고 추가 $175m을 발표했다. FY2025 revenue $792.4m·EBITDA $348.1m, active customers 242,440, new 104,902, AUAC $1,267로 platform은 2020 peak 아래에서도 큰 이익을 유지했다. 비-OTC/US diversification은 진전됐지만 원문 2년 double의 exact total return은 SQL로 확인되지 않는다.",
         price="SQL performance row가 없고 런던 상장 가격·배당·통화의 2년 total-return series를 이 payload에서 복원하지 않았다. 따라서 target 성공을 임의 판정하지 않는다.",
         drivers="가장 확실한 value realization은 new-business narrative보다 지속된 core customer income과 buyback/dividend였다. Invest·US는 duration이 긴 옵션이고 base value와 섞으면 target의 검증가능성이 낮아진다.",
         error="2020 extraordinary activity가 만든 earnings base와 정상수익을 충분히 stress하지 않았고, 10x rerating·$4 EPS·US option을 동시에 bull이 아니라 base에 가깝게 놓았다.", first_signal="ex-market-P&L customer income, active customers와 AUAC가 정상화되면서 EPS $3 floor를 깨면 core thesis 반증이었다.",
         metrics=[("Sustainable EPS", ">$3", "2023 ex-US ~$4", "FY25 EBITDA $348.1m", "사업 유지"),("P/E", "약 6x", "10x exit", "exact rerating 미복원", "미검증"),("Net cash", "약 $700m", "절반 excess", "대규모 환원", "성공"),("Dividend yield", "8%", "buyback 추가", "FY23 $365.1m total return", "성공"),("2년 target", "+100%", "2023", "SQL price row 없음", "미검증")],
         timeline=[("2019-08","선행 VIC Long","후속 기준"),("2020","EBITDA $515.9m","peak earnings"),("2021-09-03","follow-up Long","2년 double"),("2021","Plus500 Invest·Cunningham","옵션 투자"),("2023","$365.1m capital return","확실한 value realization"),("2025","revenue $792.4m·EBITDA $348.1m","core durability")],
         claims=[
             claim("Core business가 sustainable EPS >$3", "규제 종료 뒤 6개 분기 revenue가 $200m+다.", "active customers 두 배·2020 op profit $500m+", "pandemic activity를 빼도 고객 income이 유지된다.", "normalized EPS가 $3 아래로 지속되면 반증.", "FY25에도 EBITDA $348.1m을 냈다.", "성공", "peak와 floor를 cohort·volatility별로 분리한다."),
             claim("6x P/E와 net cash가 하방", "현금 조정 전에도 6x이며 $700m cash 절반이 excess다.", "50% minimum payout", "regulatory capital·M&A·growth cash가 절반 이하다.", "현금이 묶이거나 core EPS가 하락하면 반증.", "대규모 환원이 지속됐다.", "성공", "excess cash는 규제·운영 stress floor를 차감한다."),
             claim("Plus500 Invest가 cross-sell", "7개국 주식 플랫폼으로 CFD 고객 acquisition을 확장한다.", "$50m R&D center·licenses", "브랜드·KYC·traffic을 낮은 CAC로 재사용한다.", "active users·revenue가 CAC/opex를 못 덮으면 반증.", "다각화는 진행됐으나 별도 ROIC는 제한적이다.", "진행/미검증", "무료 옵션도 누적 투자액과 milestone을 기록한다."),
             claim("Cunningham이 US futures 진입", "인수로 미국 futures clearing·execution 기반을 얻는다.", "Cunningham acquisition", "규제면허와 distribution이 매출 scale로 전환된다.", "3년 내 material revenue/FCF 부재면 반증.", "US와 비-OTC revenue는 확대됐다.", "부분 성공", "인수 옵션은 organic KPI와 acquisition ROIC로 평가한다."),
             claim("$4 EPS×10x가 2년 double", "2023 ex-USA EPS $4와 10x exit를 가정했다.", "core growth+multiple normalization", "earnings와 multiple이 동시에 달성된다.", "둘 중 하나 미달이면 100% target 실패.", "exact price/total return row가 없다.", "미검증", "EPS delivery와 rerating을 독립 확률로 곱한다."),
             claim("환원이 기다림의 수익", "8% dividend와 buyback이 downside를 제한한다.", "minimum 50% payout", "고점 buyback·희석·세금이 효과를 훼손하지 않는다.", "net share count가 줄지 않으면 반증.", "FY23 $365.1m을 반환했다.", "강한 성공", "capital return은 gross announcement보다 net share count로 본다."),
         ]),
    dict(id="1f6793f5-26f0-44b5-bcd6-7a2c70ffe1f1", date="2010-02-22", author="paddy788", ticker="PLUS", company="ePlus inc.", raw_short=True, direction="Long", entry="$16", horizon="수년", filename="analysis/ideas/2010/2010-02-22_PLUS_eplus_long.md", link="", desc=11079, cat=55, business=EPLUS_BUSINESS, sources=EPLUS_SOURCES,
         title="non-recourse debt를 EV에서 제거한 balance-sheet Long", verdict="방향교정·회계해석·장기 사업논지 성공, 원 horizon 가격성과 미검증", score=8.5, process=9.0,
         summary="SQL은 Short지만 원문 첫 문장이 ePlus 매수를 권한다. $16 가격, cash $9.59/share, TBV $19.51, FY10 EPS 약 $2와 수년 내 $3 EPS/$30+를 제시했다. 핵심 edge는 database가 lease-backed non-recourse notes를 corporate debt로 잡아 EV를 $59m 과대계상한다는 회계 교정이다.",
         valuation="표면 EV는 equity $129m+debt $121m-cash $82m=$168m이지만 non-recourse notes $59m을 제외한 economic EV는 $109m이다. $16에서 cash 제외 P/E는 약 3.2x, TBV 대비 0.82x다. Direct-finance lease $107.6m의 약 60%인 $64.6m이 non-recourse였고, net economic lease investment는 2009-03 $34.3m에서 2009-12 $66.2m으로 늘어 cash 약 $25m 감소를 설명했다.",
         actual="Company는 VAR와 financing을 계속 확장해 장기 earnings·book value를 크게 키웠다. 원문의 debt taxonomy와 cash-flow 해석은 높은 재사용 가치가 있다. 그러나 SQL에 performance가 없어 $16→$30+의 실제 달성일·IRR을 이 데이터만으로 확정하지 않는다.",
         price="performance row가 없다. 따라서 장기 기업성공을 투자수익으로 대체하지 않고 1/3/5년 corrected return을 null로 유지한다.",
         drivers="headline EV 오류가 해소되고 lease investment가 earnings로 회수되며 VAR gross profit이 회복되는 것이 driver였다. 반면 현금은 전부 excess가 아니라 lease·working-capital에 재투자되는 운영자산이었다.",
         error="좋은 회계 교정 뒤에도 $3 EPS의 시간표와 buyback/특별배당을 base case로 묶었고, insider concentration이 minority-friendly payout을 보장한다고 보았다.", first_signal="lease credit loss·residual recovery와 gross profit/CFO가 악화되거나, 현금이 낮은 ROIC lease growth에 계속 묶이면 반증이었다.",
         metrics=[("Entry/cash", "$16 / $9.59", "downside 지지", "정확한 return 없음", "미검증"),("TBV/share", "$19.51", "liquidation 이하", "장기 equity 성장", "성공"),("reported/adjusted EV", "$168m / $109m", "debt 오류 해소", "구조해석 유효", "성공"),("FY10 EPS", "약 $2", "수년 내 $3", "장기 earning power 확대", "장기 성공"),("Target", "$30+", "수년", "달성일/IRR 미복원", "미검증")],
         timeline=[("2009-03","net lease investment $34.3m","cash 사용 시작"),("2009-12","net lease investment $66.2m","$25m cash decline 설명"),("2010-02-22","VIC Long","raw Short 교정"),("2010-03","FY10 close","약 $2 EPS 기대"),("2010s","VAR/services scale","장기 thesis 확인"),("2025","financing 사업 재편","원 cash engine 변화")],
         claims=[
             claim("raw Short가 아니라 Long", "I am recommending the purchase라고 명시했다.", "$16→$30+ payoff", "ticker가 미국 ePlus다.", "원문이 하락 payoff를 목표로 하면 반증.", "본문·valuation·촉매가 모두 Long이다.", "교정 성공", "direction은 flag보다 action verb·payoff로 확정한다."),
             claim("non-recourse debt가 EV를 $59m 과대계상", "lease notes를 corporate funded debt처럼 보면 안 된다.", "$168m reported vs $109m adjusted EV", "채권자가 corporate asset에 청구할 수 없다.", "representation/fraud recourse가 material하면 반증.", "법적·경제적 분류는 타당했다.", "강한 성공", "EV debt는 recourse와 matched asset을 함께 감사한다."),
             claim("cash 감소는 burn이 아니라 lease 투자", "$25m cash 감소는 lease book 확대로 설명된다.", "net lease investment $34.3m→$66.2m", "credit quality·spread·residual 회수가 양호하다.", "loss rate·residual shortfall이 spread를 소진하면 반증.", "financing은 수익엔진으로 존속했다.", "성공", "cash-flow 변동을 asset build와 operating loss로 분리한다."),
             claim("VAR 회복으로 FY10 EPS 약 $2", "Q4 $0.50로 연간 약 $2를 예상한다.", "$20m open orders·$10m deferred revenue", "backlog가 gross profit과 cash로 전환된다.", "orders 취소·margin compression이면 반증.", "장기 technology earnings는 크게 성장했다.", "장기 성공", "매출가시성을 gross margin과 conversion까지 연결한다."),
             claim("$19.51 TBV가 liquidation support", "price $16은 cash·WC·lease 중심 TBV 아래다.", "cash $9.59/share·TBV $19.51", "asset haircut과 corporate cost가 제한적이다.", "claim-adjusted TBV가 price 아래면 반증.", "기업은 장기 equity를 키웠다.", "성공", "TBV를 asset별 recovery rate로 재작성한다."),
             claim("insider 50%가 capital return", "좋은 용처가 없으면 buyback/특별배당한다.", "CEO 26%·insiders 50%+", "지배주주와 minority의 유동성·세금 선호가 같다.", "현금유보·저수익 deal이면 반증.", "장기 buyback은 있었으나 원 horizon payout은 미검증이다.", "부분 성공", "ownership은 actual allocation record로 검증한다."),
         ]),
]


ORDER = [
    "cbe4657d-58c3-4f96-a9ee-619f5836ee99", "1f6793f5-26f0-44b5-bcd6-7a2c70ffe1f1",
    "cda3b447-bd2c-4793-a346-63187380e487", "fccdf24a-81ed-4330-803f-26da2a529b35",
    "d65501e4-930a-4c40-afc4-484cb651f3a8", "d3cab447-dd55-4112-9c72-c14ca05078e8",
    "bda1795d-018f-4885-a3f3-60bd16772f48", "4ac6396a-4fcc-43d2-9d86-0ac0c4dc9ee3",
    "88c3b3a4-83c8-43be-91ba-1b3941a7337a", "16123d39-11e5-4118-970c-14c4aad7a689",
]

# Raw database price multipliers. They are not percentages. Direction-adjusted
# returns are calculated from the manually verified research direction.
PERF = {
    "d65501e4-930a-4c40-afc4-484cb651f3a8": [29.5078,29.1319,1.0245229456369134,1.00122202808605,0.9636583950926647,1.0767612136523879,0.9410371448480874,1.037563632993385,0.8247007575887599,0.7256993193028947,0.7379264654897209],
    "d3cab447-dd55-4112-9c72-c14ca05078e8": [17.559,17.8618,0.9760158550649991,0.9562418121353953,0.9985051898464882,1.0803278504965907,1.2860629947709639,1.3392995106876127,1.0828751861514516,1.3088882419465004,1.6150611920411158],
    "bda1795d-018f-4885-a3f3-60bd16772f48": [24.2726,24.3379,1.0319542770740286,1.0435370348304496,1.0184198307988774,0.9533649164471872,0.990808574281265,1.2333233352096935,0.8105424050554896,1.2191314780650753,3.1736797340773033],
    "4ac6396a-4fcc-43d2-9d86-0ac0c4dc9ee3": [28.0178,27.7328,1.0252949575953383,1.0086648300928862,0.981520077309179,0.8096189349795188,0.870481884267005,0.8251024058154964,0.985796601857728,1.486474499509606,2.5123427854381815],
    "88c3b3a4-83c8-43be-91ba-1b3941a7337a": [57.2742,56.9486,0.9777448435958039,1.0329279385270227,1.076590118106503,1.2381551082906341,1.2975964290605915,1.2229378773139288,1.2792131852231663,0.6475031870844937,0.973332092448278],
    "16123d39-11e5-4118-970c-14c4aad7a689": [67.1925,66.8137,0.9589620092885142,1.1217459892207735,1.114609728244357,1.0926022657029921,0.9528315300604517,1.112327262223167,0.5968147251237396,1.1699816055689178,None],
}
PERF_KEYS = ["next_open", "next_close", "1w", "2w", "1m", "3m", "6m", "1y", "2y", "3y", "5y"]


def ordered_ideas():
    by_id = {i["id"]: i for i in IDEAS}
    return [by_id[idea_id] for idea_id in ORDER]


def corrected(idea, key):
    row = PERF.get(idea["id"])
    if not row:
        return None
    value = dict(zip(PERF_KEYS, row))[key]
    if value is None:
        return None
    return (1 - value) if idea["direction"] == "Short" else (value - 1)


def idea_sources(idea):
    raw = source("VIC original idea" if idea["link"] else "VIC source SQL original",
                 idea["link"], "Value Investors Club / supplied SQL", idea["date"],
                 "원문 description·catalyst·작성자·raw direction·valuation 수치의 기준", "원문")
    return [raw, *idea["sources"]]


def report(idea):
    raw_direction = "Short" if idea["raw_short"] else "Long"
    actual_direction = idea["direction"]
    claim_rows = []
    claim_sections = []
    for n, (c, weight) in enumerate(zip(idea["claims"], WEIGHTS), 1):
        mechanism = f"{c['original']}라는 기대가 {c['evidence']}를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다."
        claim_sections.extend([
            f"### C{n}. {c['title']} — {c['verdict']}", "", "**원문 주장**", "", c["original"], "",
            "**경제적 메커니즘**", "", mechanism, "", "**T0 근거**", "", c["evidence"], "",
            "**숨은 가정**", "", c["assumption"], "", "**사전 반증조건**", "", c["falsifier"], "",
            "**실제 결과**", "", c["actual"], "", "**판정과 재사용 교훈**", "", f"**{c['verdict']}** — {c['lesson']}", "",
        ])
        claim_rows.append(f"| C{n} | {c['title']} | {weight}% | {c['verdict']} | {c['lesson']} |")
    score = max(1.0, min(10.0, idea["score"] - (0.5 if "실패" in idea["verdict"] else 0)))
    lines = [
        f"# {idea['company']} ({idea['ticker']}) — {idea['date']} VIC {actual_direction}", "",
        f"> **Idea unit:** {idea['date']} 게시물 한 건만 분석한다. 같은 ticker의 다른 entity·다른 시점과 섞지 않는다.",
        f"> **Research as-of:** {ASOF}. SQL raw direction과 원문상 실제 direction, 사업결과와 투자수익을 분리한다.", "", "---", "",
        "## 0. Idea Snapshot", "", "| 항목 | 내용 |", "|---|---|",
        f"| 회사 / Ticker | {idea['company']} / {idea['ticker']} |", f"| Idea ID | `{idea['id']}` |",
        f"| 게시일 / 작성자 | {idea['date']} / {idea['author']} |", f"| 원 SQL 방향 | {raw_direction} |",
        f"| 원문 검증 방향 | **{actual_direction}** |", f"| 기준가격/valuation anchor | {idea['entry']} |",
        f"| 원 horizon | {idea['horizon']} |", f"| 최종 판정 | **{idea['verdict']}** |", "",
        f"> **결론:** {idea['summary']} 결과적으로 **{idea['verdict']}**.", "", "---", "",
        "## 1. 회사는 정확히 무엇을 하는가", "", idea["business"], "",
        "### Common equity까지의 현금 waterfall", "",
        "보고 EBITDA에서 restructuring·integration, maintenance/growth capex, 운전자본, pension/legacy cash, interest·tax를 차감한 뒤의 FCF가 주주가치다. "
        "배수 비교 전에 회계상 debt의 recourse, 고객·지역 mix, 자본집약도와 희석을 같은 기준으로 맞춘다.", "",
        "### 매 분기 확인할 KPI", "",
        "- Organic/local-currency growth와 price·volume·mix\n- Gross/segment margin과 route·customer unit economics\n- EBITDA→CFO→FCF conversion\n- Net debt, pension·legacy·regulatory cash claims\n- Share count, dividend·buyback과 acquisition ROIC", "", "---", "",
        "## 2. 당시 상황과 시장이 가격에 넣은 것", "", idea["summary"], "",
        "### Reverse expectations", "",
        f"시장은 {idea['entry']}에 원문이 기회로 본 요소의 실패·지연 가능성을 상당 부분 반영했다. 핵심은 좋은 회사/나쁜 회사라는 서술이 아니라 원문 기대와 가격에 내재된 기대 중 어느 쪽이 실제 KPI에 가까웠는지다.", "", "---", "",
        "## 3. 원문 투자논지 지도", "", *claim_sections, "---", "",
        "## 4. 당시 Valuation과 Payoff Structure", "", idea["valuation"], "",
        "### 시나리오 구조", "", "| 시나리오 | 조건 | payoff 해석 |", "|---|---|---|",
        f"| Bear | 핵심 falsifier가 조기에 발생 | {actual_direction}의 손실·duration 확대 |",
        f"| Base | 핵심 KPI가 원문 bridge의 절반 이상 달성 | valuation gap 일부 축소 |",
        f"| Bull | earnings/FCF 개선과 multiple·capital return 동시 실현 | {idea['verdict']}와 비교할 상단 |", "",
        "### 핵심 수치 감사", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|",
        *["| " + " | ".join(row) + " |" for row in idea["metrics"]], "", "---", "",
        "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "", "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|",
        *["| " + " | ".join(row) + " |" for row in idea["timeline"]], "", "### 실제 사업·자본구조", "", idea["actual"], "", "---", "",
        "## 6. 실제 투자결과 — 방향 교정과 가격 경로", "", idea["price"], "",
        "성과값은 SQL의 multiplier를 사용했다. Long은 `multiplier-1`, Short는 `1-multiplier`로 부호를 교정했다. Short 수익률은 borrow fee·배당·margin call·position resizing을 제외한 단순치이므로 실제 운용수익과 다를 수 있다.", "", "---", "",
        "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 재사용 교훈 |", "|---|---|---:|---|---|", *claim_rows, "",
        f"가중치는 {sum(WEIGHTS)}%이며, 방향·사업·valuation·catalyst·timing을 한 점수로 뭉개지 않고 별도로 판정했다.", "", "---", "",
        "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", idea["drivers"], "",
        "### Counterfactual", "", f"원문 방향을 반대로 두었을 때가 아니라, 핵심 catalyst를 제거하고도 {idea['entry']}에서 충분한 expected return이 남았는지를 묻는다. 남지 않으면 cheapness보다 event timing에 의존한 아이디어였다.", "", "---", "",
        "## 9. 분석 오류 유형과 최초 경고", "", idea["error"], "", "### 최초 관찰 가능한 경고/반증", "", idea["first_signal"], "", "---", "",
        "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", "",
        f"1. **Entity·direction audit:** raw {raw_direction}와 실제 {actual_direction}을 원문 action/payoff로 확정한다.\n2. **Expectation bridge:** valuation 배수와 정상 margin을 수량·가격·원가·현금으로 연결한다.\n3. **Catalyst clock:** event 성공 여부와 target price/IRR 성공을 분리한다.\n4. **Security waterfall:** debt·pension·규제자본·분리비용을 common 앞에서 차감한다.\n5. **Path risk:** 1/2/3/5년 결과가 다르면 사후에 가장 좋은 시점만 고르지 않는다.", "",
        "### 다시 분석한다면", "", "- 원문 수치와 공시 actual을 같은 통화·회계기준으로 맞춘다.\n- 각 claim마다 분기 KPI, 날짜와 exit/cover rule을 둔다.\n- 매출 성장과 FCF/share 증가를 분리한다.\n- M&A·buyback은 발표가 아니라 실제 ROIC·net share count로 검증한다.", "", "---", "",
        "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|",
        f"| Direction / entity | raw {raw_direction} → research {actual_direction} |", f"| Business thesis | {idea['claims'][1]['verdict']} |",
        f"| Valuation thesis | {idea['metrics'][0][4]} |", f"| Catalyst / timing | {idea['verdict']} |", f"| Thesis score | {idea['score']:.1f}/10 |",
        f"| Process score | {idea['process']:.1f}/10 |", f"| Outcome-adjusted score | {score:.1f}/10 |", "",
        "### 한 문장 교훈", "", f"> {idea['claims'][0]['lesson']}", "", "---", "",
        "## 12. Sources / Validation Notes", "",
    ]
    for n, s in enumerate(idea_sources(idea), 1):
        label = f"[{s['title']}]({s['url']})" if s["url"] else s["title"]
        lines.append(f"{n}. {label} — {s['publisher']}, {s['date']}. {s['evidence']}")
    quality = "A/B" if idea["id"] in PERF else "B/C"
    lines.extend(["", "### 데이터 품질", "",
                  f"- 원문·metadata: **A/B** — 첨부 SQL description/catalyst와 공개 VIC link를 우선했다.",
                  f"- 사업·공시: **A** — SEC 또는 회사 공식 보고서를 사용했다.",
                  f"- 가격성과: **{quality}** — " + ("SQL performance row 존재; direction 수동교정." if idea["id"] in PERF else "SQL row 부재; 임의 수익률을 만들지 않음."),
                  f"- 데이터 교정: ticker={idea['ticker']}, entity={idea['company']}, raw={raw_direction}, research={actual_direction}.", ""])
    return "\n".join(lines)


def make_payload(ideas):
    keys = ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")
    out = {"schema_version": "vic-deep-research-v9", "batch": 45,
           "title": "ePlus / Plus500 / Brink's — Entity, Direction, Expectations and Path V9",
           "research_asof": ASOF, **{key: [] for key in keys}}
    for idea in ideas:
        p = dict(zip(PERF_KEYS, PERF[idea["id"]])) if idea["id"] in PERF else {}
        out["ideas_master"].append({
            "idea_id": idea["id"], "date": idea["date"], "year": int(idea["date"][:4]), "ticker": idea["ticker"],
            "company_name": idea["company"], "author": idea["author"], "direction_ko": "숏" if idea["raw_short"] else "롱",
            "is_short": int(idea["raw_short"]), "contest_winner": 0, "source_link": idea["link"] or None,
            "description_chars": idea["desc"], "catalyst_chars": idea["cat"],
            "narrative_tags_ko": "entity_resolution; direction_audit; valuation; catalyst; cash_conversion; path_dependency",
            "idea_type_ko": "기업가치/특수상황", "horizon_raw": idea["horizon"], "horizon_months": None,
            "performance_available": int(idea["id"] in PERF),
            "idea_return_1y": corrected(idea, "1y"), "idea_return_3y": corrected(idea, "3y"), "idea_return_5y": corrected(idea, "5y"),
            "auto_tag_status_ko": "raw metadata 보존·본문 entity/direction 수동검증 완료",
            "perf_1m": p.get("1m"), "perf_3m": p.get("3m"), "perf_6m": p.get("6m"), "perf_1y": p.get("1y"),
            "perf_2y": p.get("2y"), "perf_3y": p.get("3y"), "perf_5y": p.get("5y")})
        out["postmortems"].append({
            "idea_id": idea["id"], "ticker": idea["ticker"], "research_direction_ko": idea["direction"],
            "company_description_ko": idea["business"], "original_thesis_ko": idea["summary"], "actual_development_ko": idea["actual"],
            "thesis_verdict_ko": idea["verdict"], "business_verdict_ko": idea["claims"][1]["verdict"],
            "catalyst_verdict_ko": idea["verdict"], "valuation_verdict_ko": idea["metrics"][0][4], "stock_verdict_ko": idea["price"],
            "current_verdict_ko": idea["verdict"], "overall_verdict_ko": idea["verdict"], "why_ko": idea["drivers"],
            "success_pattern_ko": "direction_correction; expectation_gap; catalyst; operating_leverage; capital_return",
            "failure_pattern_ko": "duration; entity_collision; peak_normalization; leverage; terminal_value; path_dependency",
            "root_error_ko": idea["error"], "first_signal_ko": idea["first_signal"], "first_signal_date": idea["timeline"][2][0],
            "knowable_at_t0_ko": idea["claims"][0]["evidence"] + "; " + idea["claims"][0]["falsifier"],
            "avoidability_ko": "중간 이상. 원문 direction·entity·현금 waterfall과 사전 KPI로 상당 부분 방지 가능했다.",
            "counterfactual_question_ko": f"핵심 catalyst 없이도 {idea['entry']}에서 충분한 expected return이 남았는가?",
            "analyst_note_ko": f"raw {'Short' if idea['raw_short'] else 'Long'} 보존; 실제 {idea['direction']}; entity={idea['company']}",
            "corrected_return_1y": corrected(idea, "1y"), "corrected_return_3y": corrected(idea, "3y"), "corrected_return_5y": corrected(idea, "5y"),
            "confidence": 0.97 if idea["id"] in PERF else 0.85, "research_asof": ASOF,
            "research_status_ko": "SQL 원문·공식자료 검증 완료; 가격 row 부재 시 미검증 유지"})
        out["meta"].append({"idea_id": idea["id"], "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·timeline·성과·first break·counterfactual 장문분석",
                            "report_version": "V9-canonical", "thesis_type_ko": idea["title"], "one_line_verdict_ko": idea["summary"],
                            "thesis_score": idea["score"], "process_score": idea["process"], "return_summary_ko": idea["price"],
                            "core_error_ko": idea["error"], "core_insight_ko": idea["claims"][0]["lesson"], "research_asof": ASOF})
        sections = [("회사·가치사슬·현금엔진", idea["business"]), ("T0 기대·reverse expectations", idea["summary"]),
                    ("Valuation·payoff·실제경로", idea["valuation"] + "\n\n" + idea["price"]),
                    ("사후인과·오류·교훈", idea["drivers"] + "\n\n" + idea["error"])]
        for n, (title, body) in enumerate(sections, 1):
            out["sections"].append({"idea_id": idea["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, (c, weight) in enumerate(zip(idea["claims"], WEIGHTS), 1):
            out["claims"].append({"idea_id": idea["id"], "claim_order": n, "claim_title_ko": c["title"], "thesis_weight_pct": weight,
                                  "original_claim_ko": c["original"], "t0_evidence_ko": c["evidence"], "key_assumption_ko": c["assumption"],
                                  "ex_ante_falsifier_ko": c["falsifier"], "actual_result_ko": c["actual"],
                                  "quantitative_gap_ko": c["actual"], "verdict_ko": c["verdict"],
                                  "analytical_error_ko": idea["error"], "reusable_lesson_ko": c["lesson"]})
        for n, row in enumerate(idea["metrics"], 1):
            out["metrics"].append({"idea_id": idea["id"], "metric_order": n, "metric_name_ko": row[0], "t0_value_ko": row[1],
                                   "thesis_expectation_ko": row[2], "actual_value_ko": row[3], "verdict_ko": row[4],
                                   "interpretation_ko": "T0와 actual을 가능한 동일 단위로 비교하고 불가능하면 미검증으로 남겼다."})
        for n, row in enumerate(idea["timeline"], 1):
            out["timeline"].append({"idea_id": idea["id"], "event_order": n, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for n, s in enumerate(idea_sources(idea), 1):
            out["sources"].append({"idea_id": idea["id"], "source_order": n, "source_type_ko": s["kind"], "publisher": s["publisher"],
                                   "title_ko": s["title"], "source_date": s["date"], "url": s["url"], "evidence_ko": s["evidence"]})
    return out


def make_index(ideas):
    rows = []
    for n, idea in enumerate(ideas, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        perf = "DB 없음"
        if idea["id"] in PERF:
            r1, r3, r5 = corrected(idea, "1y"), corrected(idea, "3y"), corrected(idea, "5y")
            fmt = lambda value: "null" if value is None else f"{value:+.1%}"
            perf = f"1Y {fmt(r1)} / 3Y {fmt(r3)} / 5Y {fmt(r5)}"
        elif idea["id"] == "cda3b447-bd2c-4793-a346-63187380e487":
            perf = "후속 원문: 2Y 약 +150% total return"
        rows.append(f"| {n} | {idea['date']} | {idea['company']} | {raw}→**{idea['direction']}** | {perf} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 045 — ePlus / Plus500 / Brink's — V9 Index", "",
        f"> **Research as-of:** {ASOF}. 첨부 `VIC_IDEAS(4).sql`의 원문·metadata·성과를 기준으로 entity와 direction을 수동 교정했다.", "",
        "## 0. 배치 결론", "",
        "이번 10건의 핵심은 종목코드나 raw direction을 그대로 믿으면 투자판정이 뒤집힌다는 점이다. `PLUS`는 미국 ePlus와 영국 Plus500 두 회사가 충돌하고, raw Short 8건 중 실제 Short는 BCO 2014·2018 두 건뿐이다. BCO 성과 multiplier는 실제 Long/Short 방향으로 다시 부호를 계산했다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | 실제 회사 | raw→연구 방향 | 성과 감사 | Canonical report |", "|---:|---|---|---|---|---|",
        *rows, "", "## 2. 기업별 투자논지", "",
        "### ePlus — balance sheet와 accounting edge", "",
        "2008년은 cash/TBV와 filing·NASDAQ relisting을 결합한 event Long이고, 2010년은 lease-backed non-recourse notes 때문에 database EV가 $59m 과대계상되는 구조를 교정한 Long이다. 둘 다 사업 방향은 맞았지만 SQL performance row가 없어 exact return은 만들지 않았다.", "",
        "### Plus500 — 규제 후 cohort economics와 capital return", "",
        "2019년은 ESMA 이후 실제 네 분기의 AUAC·churn·EEA retail run-rate로 과도한 규제공포를 반박했고, 2년 후 원문이 배당 포함 약 150% 수익을 확인했다. 2021년은 core CFD의 6x P/E와 현금환원 위에 Invest·US futures 옵션을 얹었으나, 2년 double은 SQL price row가 없어 미확정이다.", "",
        "### Brink's — 같은 기업, 서로 다른 expectations", "",
        "2007 SOTP Long은 분리 촉매를 맞혔지만 common 장기수익은 부진했다. 2010 normalization Long과 2012 self-help/LatAm Long은 성과가 좋았고 특히 2012는 2년 -19% drawdown 뒤 5년 +217%였다. 2014 Short는 1년만 성공하고 regime change 뒤 큰 손실, 2017 Long은 1~2년 성공 뒤 COVID 경로로 소멸, 2018 Short는 2년 pandemic 수익을 thesis 성공으로 오인하면 안 된다.", "",
        "## 3. 배치 공통 교훈", "",
        "1. **Entity resolution이 valuation보다 먼저다.** ticker collision은 exchange·company name·원문 business description으로 해소한다.\n2. **Direction은 action/payoff로 검증한다.** raw flag가 틀리면 return과 verdict 부호가 모두 뒤집힌다.\n3. **Event 성공과 주식 성공은 다르다.** BHS spin이나 NASDAQ relisting이 일어나도 target price/IRR은 별도다.\n4. **Margin gap은 사람과 기간의 함수다.** 현재 team의 실패를 영구 구조로 외삽한 2014 Short는 새 CEO 뒤 무너졌다.\n5. **Short는 cover rule이 논지 일부다.** BCO 2014·2018처럼 horizon에 따라 +17%에서 -151%, +40%에서 -17%로 바뀐다.\n6. **SQL 값이 없으면 비워 둔다.** 공시상 장기 기업성공을 특정 기간 투자수익으로 대체하지 않는다.", "",
        "## 4. 데이터·앱 산출물", "",
        "- DB payload: `data/curated/batch_045_eplus_plus500_brinks_deep_v7.json`\n- Streamlit wrapper: `analysis/batch_045_eplus_plus500_brinks_10.md`\n- 원문: `data/source_batch045/`\n- Builder: `scripts/45_build_batch_045_v9.py`", "",
        "## 5. 검증 기준", "",
        "각 보고서는 0~12절, 6개 claim/100% weight, 5개 핵심 metric, 최소 6개 event, 원문+공식자료 source를 포함한다. Payload와 문서의 direction·return·verdict를 동일하게 유지한다.", "",
    ])


def main():
    ideas = ordered_ideas()
    if len(ideas) != 10 or len({i["id"] for i in ideas}) != 10:
        raise ValueError("Batch 045 requires ten unique idea units")
    for idea in ideas:
        if len(idea["claims"]) != 6 or sum(WEIGHTS) != 100 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(i["filename"]).relative_to("analysis").as_posix() for i in ideas]
    wrapper = "# Batch 045 — ePlus / Plus500 / Brink's V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + \
              "> Streamlit 호환 wrapper다. canonical index: [Batch 045 V9 Index](batch_045_v9_index.md).\n"
    (ROOT / "analysis/batch_045_eplus_plus500_brinks_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_045_v9_index.md").write_text(make_index(ideas), encoding="utf-8")
    payload = make_payload(ideas)
    output = ROOT / "data/curated/batch_045_eplus_plus500_brinks_deep_v7.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {"batch": "045", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql",
              "record_count": 10, "direction_audit": "complete", "performance_rule": "raw multiplier; research direction adjusted",
              "candidates": [{"idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["company"],
                              "author": i["author"], "raw_direction": "Short" if i["raw_short"] else "Long",
                              "research_direction": i["direction"], "performance_available": i["id"] in PERF,
                              "corrected_return_1y": corrected(i, "1y"), "corrected_return_3y": corrected(i, "3y"),
                              "corrected_return_5y": corrected(i, "5y"), "canonical_report": i["filename"]} for i in ideas]}
    (ROOT / "data/curated/batch_045_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ideas={len(payload['ideas_master'])} postmortems={len(payload['postmortems'])} sections={len(payload['sections'])} "
          f"claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
