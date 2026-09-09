#!/usr/bin/env python3
"""Build Batch 043 Level 3 / Nexstar canonical V9 artifacts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-09"
WEIGHTS = [20, 18, 18, 16, 16, 12]
NXST_IDS = [
    "7b8c3ad5-3249-4756-901a-9d267e0a8a4b",
    "52de43f8-b373-4daa-bbf9-6655b52da336",
]


def C(title, original, mechanism, evidence, assumption, falsifier, actual, gap, verdict, error, lesson):
    return dict(title=title, original=original, mechanism=mechanism, evidence=evidence,
                assumption=assumption, falsifier=falsifier, actual=actual, gap=gap,
                verdict=verdict, error=error, lesson=lesson)


def S(title, url, publisher, date, evidence, source_type="1차자료"):
    return dict(title=title, url=url, publisher=publisher, date=date,
                evidence=evidence, type=source_type)


BUSINESS = (
    "Level 3 Communications는 북미·유럽·중남미의 장거리·도시 광섬유망, IP backbone, enterprise buildings와 "
    "data center를 연결해 기업·통신사·콘텐츠 사업자에게 wavelength, transport, IP transit, VPN, voice, "
    "colocation을 팔았다. 선행 network cost는 크고 incremental on-net traffic의 비용은 낮다. 따라서 traffic "
    "증가만으로는 충분하지 않고, 단위가격 하락보다 volume·on-net 전환이 빨라야 하며 gross margin과 EBITDA가 "
    "cash interest·capex를 넘은 뒤에야 common equity 가치가 생긴다."
)

ENGINE = (
    "Common의 현금엔진은 `Core Network Services 매출 - access/network cost - SG&A - cash interest - capex - tax = equity FCF`다. "
    "Bank debt·채권은 enterprise value에서 senior claim, 담보, coupon, 만기, exchange/tender 조건을 적용한 회수액이 payoff다. "
    "같은 회사라도 common, secured bank debt, subordinated convert의 손익은 서로 반대일 수 있다."
)

KPI = (
    "CNS organic·constant-currency revenue, enterprise buildings·on-net connects, churn, price decline 대비 traffic volume, "
    "incremental gross/EBITDA margin, capex/revenue, FCF, cash interest, liquidity, 순레버리지, maturity wall, debt-for-equity dilution"
)


LVLT_SOURCES = [
    S("Level 3 2002 Form 10-K/A", "https://www.sec.gov/Archives/edgar/data/794323/000104746903013081/a2108070z10-ka.htm", "SEC / Level 3", "2003-04", "2001~02 liquidity, debt repurchase와 junior convert financing 검증."),
    S("Level 3 2004 Form 10-K", "https://www.sec.gov/Archives/edgar/data/794323/000104746905006668/a2153221z10-k.htm", "SEC / Level 3", "2005-03", "$1.125bn secured facility 전액상환과 2008 notes 할인매입 검증."),
    S("Level 3 2007 Form 10-K", "https://www.sec.gov/Archives/edgar/data/794323/000104746908002075/a2182924z10-k.htm", "SEC / Level 3", "2008-02", "인수통합, debt/equity financing, 2008 cash consumption 전망 검증."),
    S("Level 3 2011 Form 10-K", "https://www.sec.gov/Archives/edgar/data/794323/000079432312000003/lvlt-123111_10k.htm", "SEC / Level 3", "2012-02", "Global Crossing 종결, $958m adjusted EBITDA, $716m interest, 1-for-15 reverse split 검증."),
    S("Global Crossing acquisition announcement", "https://www.sec.gov/Archives/edgar/data/794323/000119312511093638/dex991.htm", "SEC / Level 3", "2011-04-11", "pro-forma revenue·EBITDA와 synergy 기대 검증."),
    S("Level 3 2014 proxy", "https://www.sec.gov/Archives/edgar/data/794323/000104746915003240/a2223988zdef14a.htm", "SEC / Level 3", "2015-04", "2014 sustainable FCF $325m과 2013 대비 $372m 개선 검증."),
    S("Level 3 2015 Form 10-K", "https://www.sec.gov/Archives/edgar/data/794323/000079432316000025/lvlt-123115_10k.htm", "SEC / Level 3", "2016-02", "2015 FCF $626m과 성숙기 cash conversion 검증."),
    S("Level 3 2016 Form 10-K", "https://www.sec.gov/Archives/edgar/data/794323/000079432317000002/lvlt-123116_10k.htm", "SEC / Level 3", "2017-02", "2016 FCF $1.009bn과 merger 전 재무상태 검증."),
    S("CenturyLink / Level 3 merger proxy", "https://www.sec.gov/Archives/edgar/data/794323/000119312517040682/d282157ddefm14a.htm", "SEC", "2017-02", "$26.50 cash + 1.4286 CTL shares의 계약조건 검증."),
    S("Level 3 merger completion 8-K", "https://www.sec.gov/Archives/edgar/data/794323/000119312517329395/d459582d8k.htm", "SEC / Level 3", "2017-11-01", "거래 종결과 실제 consideration 검증."),
    S("CenturyLink 2017 Form 10-K", "https://www.sec.gov/Archives/edgar/data/18926/000001892618000012/ctl2017123110k.htm", "SEC / CenturyLink", "2018-02", "former LVLT ownership 약 49%와 acquisition accounting 검증."),
    S("CenturyLink FY2018 results and 2019 outlook", "https://www.sec.gov/Archives/edgar/data/18926/000001892619000003/ctl4q20188-kexhibit991.htm", "SEC / CenturyLink", "2019-02", "2019 FCF guidance와 dividend reset 검증."),
    S("Lumen Q3 2022 results", "https://ir.lumen.com/news/news-details/2022/Lumen-Technologies-reports-third-quarter-2022-results/default.aspx", "Lumen Technologies", "2022-11-02", "common dividend elimination과 capital-allocation 전환 검증."),
]


RAW = {
    "552a0c54-5417-4cb8-ae6e-e3b5a0079976": (2878, 343),
    "15f30c2f-a0a7-41f3-b97f-2c7dff55fdd6": (3825, 127),
    "6c53c36e-b9ee-4b7d-bc12-9eb3f7c84886": (10541, 308),
    "6c4d3871-880a-45e2-8fc6-3706b125ddeb": (6437, 153),
    "107fd97a-4482-4f35-af20-b8f2ee3e325f": (4705, 58),
    "44312f7c-f1b7-4f46-b92b-dc8d08c79832": (12739, 229),
    "e32af27d-688a-4ce1-8cf4-f5df3499ae50": (9622, 139),
    "3df8999b-4ddc-4eea-bc10-d0c9949e3170": (9839, 19),
}


IDEAS = [
    dict(
        id="552a0c54-5417-4cb8-ae6e-e3b5a0079976", date="2000-08-29", author="dave143",
        filename="analysis/ideas/2000/2000-08-29_LVLT_long.md", source="https://www.valueinvestorsclub.com/idea/Level_Three_Communications_In/0716564972",
        direction="Long", security="LVLT common equity / Long", entry="원문 약 $81", horizon="네트워크 완공 이후 수년", raw_horizon="명시 종료일 없음; 4Q00 network completion catalyst",
        title="all-IP fiber 원가우위와 prefunding을 산 common Long", verdict="강한 실패 — 6개월 약 -70%, 자산가치가 equity를 보호하지 못함", score=1.5, process=4.0,
        conclusion="all-fiber/IP architecture와 장기 strategic asset value는 남았지만, $7bn prefunding·replacement cost·매출성장을 common의 floor로 본 논지는 실패했다. 같은 작성자의 2001-03 후속 글은 약 70% 하락을 기록했고 2004 원문은 2000년 추천가를 $81, 2001-07 주가를 약 $5로 회고한다.",
        t0="원문은 12개 conduit 중 하나만 사용하고 96~244 fibers를 수용하는 end-to-end all-IP network가 silicon economics와 낮은 단위비용을 만든다고 봤다. 약 $7bn 현금으로 Phase 6까지 prefunded됐고 투자액의 85%가 hard asset이라고 주장했다. Gateway 6.5m sqft, build cost $450/sqft, rent $35/sqft/month, 임대 1달러당 telecom revenue 8달러라는 계산으로 잠재매출 $24.5bn을 제시했다. Q2 sales는 전년 대비 120%, 전분기 대비 32% 증가했다.",
        reverse="시장은 fiber glut, 통신사업자 자금경색, 대규모 burn과 bandwidth price collapse를 가격에 넣었다. 기술적으로 낮은 cost per bit가 업계 전반에 퍼지면 고객가치는 커져도 공급자의 가격결정력은 사라진다. $7bn cash와 hard asset은 debt·추가 capex·운전자금보다 뒤에 있는 common의 floor가 아니다.",
        valuation="원문의 $24.5bn revenue potential은 `6.5m sqft × $35 × 12 × $8`의 capacity extrapolation이다. occupancy, ramp time, churn, traffic price, access cost, SG&A, capex, interest를 거치지 않은 매출 TAM이므로 equity DCF가 아니다. 85% hard-asset 주장도 liquidation haircut과 senior claims를 차감하지 않았다.",
        actual="네트워크 완공이라는 물리적 촉매와 매출증가는 있었지만 주가는 6개월 만에 약 70% 하락했다. 2001년 communications revenue는 성장했어도 대규모 순손실·현금소진과 약 $6bn 부채가 equity economics를 압도했다. 회사는 이후 채무교환·희석·통합을 거쳐 생존하고 2017년 인수됐지만 원 horizon과 초기 common의 손실은 복구된 것으로 볼 수 없다.",
        price="원 DB에 일관된 event-date 가격 series가 없다. 후속 VIC 원문의 약 -70%와 $81→약 $5 회고만 사용한다. split·정확한 execution·dividend를 복원하지 못해 exact return, MFE·MAE, IRR은 만들지 않는다.",
        drivers="손실의 핵심은 network quality가 아니라 공급과잉 속 가격하락, 낮은 utilization, 큰 fixed cost, cash burn, debt financing이었다. network completion은 비용을 일부 줄였지만 backlog가 gross margin·FCF로 전환되기 전에 자본구조 위험이 현실화됐다.",
        counterfactual="traffic가 폭증해도 price per bit가 더 빨리 하락하고 외부접속비·이자·capex가 남는다면 $24.5bn TAM 중 common에 귀속되는 현금은 얼마인가?",
        error="capacity·replacement cost·cash balance를 equity value로 직결하고, industry supply와 price elasticity, debt waterfall, burn duration을 명시적으로 모델링하지 않았다.",
        warning="2001-03-01 같은 작성자의 후속 글에서 약 -70%를 인정한 시점이 가장 이른 명확한 경고다.", first_signal_date="2001-03-01",
        scenarios=[("Bear", "fiber glut·가격하락·burn 지속", "현금과 common 급감", "6개월 -70%, 2001-07 약 $5"), ("Base", "4Q00 완공·backlog 전환", "성장과 margin 개선", "매출성장만 확인"), ("Bull", "$24.5bn capacity revenue", "대규모 equity upside", "FCF bridge 부재")],
        lessons=["좋은 network와 좋은 common entry는 debt waterfall 이후 FCF로 연결될 때만 같다.", "TAM·capacity revenue는 occupancy와 가격·비용·시간을 통과시킨다.", "prefunded는 전체 사업기간이 아니라 특정 build phase의 표현일 수 있다."],
        checklist=["price/bit vs traffic", "on-net gross margin", "분기 cash burn", "남은 build capex", "cash interest", "maturity wall", "희석 후 share count"],
        scorecard=[("Business thesis", "기술·장기 자산가치 일부 적중"), ("Valuation thesis", "실패"), ("Catalyst thesis", "완공은 발생·payoff 실패"), ("Timing / path", "강한 실패"), ("Security selection", "common 부적절")],
        claims=[
            C("all-IP fiber가 구조적 원가우위", "end-to-end IP·빈 conduit의 upgradeability가 legacy 망보다 싸다.", "낮은 electronics·construction cost가 incremental gross margin을 높인다.", "12 conduit, 96~244 fibers, all-IP design.", "경쟁사는 같은 optics를 채택하지 못하고 가격경쟁도 제한된다.", "price/bit 하락이 unit-cost 개선을 넘거나 gross margin이 악화되면 반증.", "망은 생존했지만 업계 공급과잉과 가격하락이 equity cash flow를 훼손했다.", "기술우위와 common payoff가 분리됐다.", "부분 성공", "상대원가와 절대수익성을 혼동했다.", "원가우위는 price-cost spread로 검증한다."),
            C("$7bn이면 Phase 6까지 prefunded", "추가 equity financing 없이 network를 완성할 수 있다.", "충분한 liquidity가 dilution과 distress를 막는다.", "원문 cash 약 $7bn, 투자 85% hard asset.", "forecast burn과 영업손실이 계획 범위 안이다.", "cash가 빠르게 감소하거나 신규 고비용자금이 필요하면 반증.", "2001년 손실·cash burn과 약 $6bn debt가 equity를 압박했다.", "특정 phase funding이 enterprise solvency를 보장하지 못함.", "실패", "runway를 phase completion까지만 계산했다.", "liquidity는 EBITDA 흑자·FCF 흑자·만기까지 세 구간으로 본다."),
            C("Gateway capacity가 $24.5bn 매출", "6.5m sqft의 telecom hotel capacity가 임대료의 8배 매출을 만든다.", "network node에 고객 장비가 모이면 high-margin traffic이 따라온다.", "6.5m sqft, $35 월임대, 8x telecom revenue.", "높은 occupancy와 8x attach ratio가 빠르게 실현된다.", "occupancy·attach revenue·margin이 계획보다 낮으면 반증.", "capacity TAM이 FCF로 전환되기 전에 가격과 자금환경이 악화됐다.", "TAM 대비 실제 recurring cash conversion 미확인.", "실패", "capacity arithmetic를 forecast로 사용했다.", "부동산 capacity는 leased sqft·revenue attach·cash margin으로 단계화한다."),
            C("매출 모멘텀이 operating leverage를 연다", "Q2 sales +120% YoY/+32% QoQ가 backlog 전환을 보여준다.", "고정망에 매출이 붙으면 EBITDA margin이 급개선된다.", "원문 분기 sales growth.", "매출 품질과 가격이 유지되고 incremental margin이 양수다.", "매출증가에도 손실·burn이 확대되면 반증.", "communications revenue는 늘었지만 2001 전체 손실과 cash burn이 컸다.", "매출 성장과 equity cash generation 불일치.", "실패", "headline growth를 contribution margin 없이 읽었다.", "고정비 사업은 incremental EBITDA와 incremental FCF를 따로 잰다."),
            C("4Q00 완공이 backlog를 현금화", "leased fiber 비용을 멈추고 수요를 자체망에 올린다.", "on-net migration이 access cost를 낮추고 provisioning을 가속한다.", "4Q00 network completion catalyst.", "고객 연결·billing이 완공 직후 따라온다.", "완공 후에도 churn·access cost·burn이 높으면 반증.", "물리적 구축은 진행됐지만 주가는 6개월 약 -70%였다.", "event occurrence와 economic payoff가 반대.", "촉매 실패", "완공과 수익화를 같은 날짜로 봤다.", "촉매는 ready-for-service, connected, billed, collected로 나눈다."),
            C("hard asset이 common downside를 보호", "투자액의 85%가 hard asset이라 손실가치가 제한된다.", "재조달원가·매각가치가 enterprise floor를 만든다.", "원문 asset composition 주장.", "자산이 debt보다 충분히 높은 가격에 매각 가능하다.", "distress EV가 senior claims 아래면 common floor는 0이다.", "$81 추천 뒤 2001-07 약 $5라는 후속 회고.", "약 94% 가격하락 회고.", "강한 실패", "enterprise asset floor를 common floor로 오인했다.", "자산가치는 utilization haircut과 senior debt를 차감한다."),
        ],
        metrics=[("후속 가격회고", "약 $81", "상승", "2001-07 약 $5", "강한 실패"), ("6개월 경로", "Long", "상승", "같은 작성자 약 -70%", "실패"), ("현금", "약 $7bn", "Phase 6 prefunded", "2001 큰 cash burn", "실패"), ("Gateway capacity", "6.5m sqft", "$24.5bn potential revenue", "FCF 전환 미확인", "미달"), ("Q2 sales", "+120% YoY/+32% QoQ", "operating leverage", "매출과 cash flow 분리", "실패")],
        timeline=[("2000-08-29", "VIC common Long", "all-IP network·prefunding"), ("2000-Q4", "network completion catalyst", "물리적 완공과 경제성 분리"), ("2001-03-01", "같은 작성자 약 -70% 회고", "첫 명확한 반증"), ("2001-07", "주가 약 $5 회고", "$81 entry 대비 대폭 하락"), ("2002", "채무할인매입·교환 확대", "자본구조 stress"), ("2011-10-04", "Global Crossing 결합", "장기 consolidation"), ("2017-11-01", "CenturyLink 거래 종결", "자산 생존은 확인")],
    ),
    dict(
        id="15f30c2f-a0a7-41f3-b97f-2c7dff55fdd6", date="2001-03-01", author="dave143",
        filename="analysis/ideas/2001/2001-03-01_LVLT_long.md", source="https://www.valueinvestorsclub.com/idea/Level_3_Communications_Inc./7923868895",
        direction="Long", security="LVLT common equity / Long", entry="첫 글 대비 약 -70% 이후; 원문 시가총액 $10.6bn", horizon="2001~2002 EBITDA 전환", raw_horizon="2001 EBITDA-positive run-rate·2002 margin 목표",
        title="replacement cost 아래에서 EBITDA inflection을 산 common Long", verdict="실패 — 싼 PP&E보다 cash burn·부채·공급과잉이 우선", score=2.5, process=5.0,
        conclusion="첫 글 이후 70% 하락한 entry는 개선됐지만 $10~12bn PP&E와 $10.6bn market cap을 직접 비교한 valuation은 debt·earning power를 놓쳤다. 2001년 communications revenue 성장에도 연말 cash와 손실·부채가 equity를 압박했고, 2004 원문이 회고한 2001-07 약 $5는 near-term Long 실패를 확인한다.",
        t0="원문은 revenue +292% YoY/+38% QoQ, 2001 revenue guide $1.7bn, 2002 $2.9bn, 2001년 EBITDA-positive run-rate를 제시했다. gross margin은 2000 27%에서 2001 50%, 2002 55%로 상승할 것으로 봤다. market cap $10.6bn은 주장상 $10~12bn PP&E보다 낮고, cash $4~5bn, $4bn dark-fiber sales deferred over 20 years, $5.1bn backlog가 downside와 성장을 지지한다고 했다.",
        reverse="시장은 PP&E를 reproduction cost가 아니라 earning power와 distress sale value로 평가했다. 경쟁사가 fiber를 light할 돈이 부족하다는 사실은 기존 capacity의 oversupply와 customer credit risk를 없애지 않는다. deferred dark-fiber revenue와 backlog는 현금·반복 gross profit·cancellation risk가 서로 다르다.",
        valuation="`market cap $10.6bn < PP&E $10~12bn`은 EV와 asset value를 같은 층에서 비교하지 않았다. 올바른 bridge는 operating asset value에서 net debt, future burn, incremental capex, dilution을 차감한다. 50~55% gross margin 기대도 access cost·SG&A·interest·capex를 통과해야 equity FCF가 된다.",
        actual="2001 communications revenue는 성장했지만 연말 현금은 약 $1.3bn, 장기부채는 약 $6.2bn이었고 큰 순손실이 발생했다. 이후 회사는 채권 할인매입과 신규자본으로 생존했다. 2011 Global Crossing 결합과 2017 매각은 네트워크의 장기 strategic value를 보여주지만 2001~02 EBITDA·가격 경로의 실패를 소급해 성공으로 바꾸지 않는다.",
        price="원 DB에는 가격 series가 없다. 동일 작성자가 2000년 글 대비 -70% 후속이라고 밝혔고, 2004년 VIC 글은 2000년 $81에서 2001-07 약 $5로 하락했다고 적었다. 이 회고 외의 exact entry·exit·corporate action이 없어 IRR은 계산하지 않는다.",
        drivers="매출은 증가했지만 예상보다 낮은 revenue quality, fiber pricing, 고객·산업 distress와 고정비·이자가 gross margin 개선을 먹었다. replacement cost 할인은 realization catalyst가 아니었고 cash runway도 EBITDA·FCF inflection 전에 좁아졌다.",
        counterfactual="PP&E를 오늘 새로 짓는 데 $12bn이 들어도 그 망이 cash interest와 유지·성장 capex를 못 벌면 common은 왜 $10.6bn이어야 하는가?",
        error="PP&E와 market cap을 직접 비교하고 deferred revenue·backlog·cash를 모두 같은 질의 margin of safety로 합쳤다.",
        warning="2001 FY cash 약 $1.3bn·장기부채 약 $6.2bn과 대규모 손실이 EBITDA 전환·runway 가정을 무너뜨렸다.", first_signal_date="2001-12-31",
        scenarios=[("Bear", "revenue miss·margin 지연·financing", "common 추가 급락", "2001-07 약 $5"), ("Base", "$1.7bn/$2.9bn 매출·50~55% GM", "EBITDA 전환", "timing·cash flow 미달"), ("Bull", "PP&E floor·short covering", "큰 rerating", "실패")],
        lessons=["replacement cost는 earning power와 utilization을 반영한 뒤 debt를 차감한다.", "backlog·deferred revenue·cash receipt를 서로 바꿔 쓰지 않는다.", "gross margin inflection과 equity FCF inflection 사이에 SG&A·interest·capex가 있다."],
        checklist=["revenue recognition vs cash", "backlog cancellation", "gross-to-EBITDA bridge", "cash burn", "debt maturities", "incremental financing cost", "fully diluted shares"],
        scorecard=[("Business thesis", "매출성장·망가치 일부"), ("Valuation thesis", "실패"), ("Catalyst thesis", "EBITDA timing 실패"), ("Timing / path", "실패"), ("Security selection", "common 부적절")],
        claims=[
            C("2001~02 revenue guide 달성", "$1.7bn에서 $2.9bn으로 고성장한다.", "망 완공과 backlog가 billed traffic으로 전환된다.", "+292% YoY/+38% QoQ, $5.1bn backlog.", "backlog 품질과 고객 solvency가 높다.", "revenue miss·cancellation·receivable stress면 반증.", "communications revenue는 성장했지만 enterprise cash economics는 악화됐다.", "성장만으로 Long payoff 부족.", "부분 성공", "매출규모를 quality보다 우선했다.", "backlog는 고객신용·기간·현금회수로 haircut한다."),
            C("gross margin 27%→50%→55%", "on-net mix가 크게 올라 margin이 계단식 개선된다.", "leased capacity를 자체망으로 옮겨 access cost를 줄인다.", "원문 2000/01/02 gross margin forecast.", "가격하락과 provisioning cost가 절감보다 작다.", "margin inflection 지연 시 runway 재산정.", "대규모 손실·financing need가 expected cash conversion을 부정했다.", "예상 equity FCF로 연결되지 않음.", "실패", "gross margin과 FCF를 동일시했다.", "margin waterfall을 interest·capex까지 이어간다."),
            C("EBITDA-positive run-rate가 1년 앞당겨짐", "2001년에 EBITDA breakeven에 도달한다.", "fixed-cost absorption이 cash burn을 빠르게 낮춘다.", "회사 guide와 sales momentum.", "adjusted EBITDA가 현금수익성을 대표한다.", "현금소진이 계속되면 accounting breakeven도 재검토.", "2001 cash·loss·debt는 runway 악화를 보였다.", "FCF inflection은 적시에 오지 않음.", "실패", "EBITDA와 cash runway를 분리하지 않았다.", "breakeven은 EBITDA, CFO, FCF 날짜를 각각 둔다."),
            C("PP&E가 equity floor", "$10.6bn market cap이 $10~12bn asset cost 아래다.", "재조달원가가 strategic buyer와 lender에게 담보가 된다.", "원문 market cap·PP&E 비교.", "asset value가 debt·burn보다 충분히 크다.", "distress EV 또는 earning value가 debt 아래면 반증.", "주가는 후속 회고상 약 $5까지 하락했다.", "replacement cost discount가 더 확대.", "실패", "EV와 equity를 혼용했다.", "asset valuation은 EV 기준으로 하고 모든 senior claim을 차감한다."),
            C("$4~5bn cash가 downside를 제한", "망이 완성돼 큰 추가 financing 없이 버틴다.", "liquidity가 EBITDA·FCF 전환까지 runway를 산다.", "원문 cash estimate.", "burn forecast가 정확하고 신규 capex가 제한된다.", "cash가 예상보다 빨리 줄면 즉시 반증.", "2001년 말 cash 약 $1.3bn, 부채 약 $6.2bn.", "원문 $4~5bn 대비 큰 축소.", "실패", "gross cash를 net liquidity로 봤다.", "cash runway에는 restricted cash·interest·mandatory capex를 뺀다."),
            C("fiber glut은 funding 부족으로 제한", "경쟁사는 dark fiber를 light할 자본이 없어 실질공급이 적다.", "financing constraint가 LVLT의 completed network moat를 강화한다.", "industry capital scarcity.", "LVLT 고객·경쟁사 distress가 LVLT 수요와 가격을 해치지 않는다.", "capacity price collapse와 customer bankruptcy면 반증.", "통신업 자금경색은 경쟁뿐 아니라 수요·가격·LVLT 자금조달도 훼손했다.", "한쪽 효과만 모델링.", "실패", "산업 distress를 경쟁우위로만 해석했다.", "경쟁사 약화의 수요·신용·공급 효과를 함께 계산한다."),
            C("short covering이 catalyst", "70% 하락 뒤 낮은 asset valuation이 short covering을 부른다.", "positive guide와 technical positioning이 빠른 rerating을 만든다.", "낮아진 시가총액과 성장 guide.", "fundamental estimate가 안정된다.", "현금·부채 지표 악화면 covering 논지 무효.", "2001-07 약 $5 회고와 FY stress.", "기술적 촉매가 fundamental deterioration을 못 이김.", "실패", "positioning을 독립 catalyst로 과대평가했다.", "short interest는 earnings revision과 liquidity 개선 뒤에 둔다."),
        ],
        metrics=[("Market cap / PP&E", "$10.6bn / $10~12bn", "asset discount 해소", "earning-value floor 아님", "실패"), ("2001/02 revenue guide", "$1.7bn/$2.9bn", "고성장", "cash economics 미달", "부분"), ("Gross margin", "27%", "50%/55%", "FCF 전환 지연", "실패"), ("Cash", "$4~5bn 주장", "충분한 runway", "2001 말 약 $1.3bn", "실패"), ("후속 가격", "첫 글 대비 -70%", "반등", "2001-07 약 $5 회고", "실패")],
        timeline=[("2001-03-01", "두 번째 VIC Long", "첫 글 대비 약 -70%"), ("2001-07", "주가 약 $5 회고", "근기 Long 실패"), ("2001-12-31", "cash 약 $1.3bn·debt 약 $6.2bn", "runway 반증"), ("2002", "채권 할인매입·신규 financing", "자본구조 방어"), ("2003", "secured facility 상환", "credit 생존"), ("2011-10-04", "Global Crossing 결합", "규모 확대"), ("2017-11-01", "CenturyLink 거래", "장기 자산가치")],
    ),
    dict(
        id="6c53c36e-b9ee-4b7d-bc12-9eb3f7c84886", date="2002-04-19", author="nish697",
        filename="analysis/ideas/2002/2002-04-19_LVLT_bonds_long.md", source="",
        direction="Long", security="Level 3 bonds / Long — 원문이 여러 issue를 열거해 단일 CUSIP 미확정", entry="원문 YTM 약 25~35%", horizon="6~8년", raw_horizon="25%+ annual return for 6~8 years 주장",
        title="25~35% YTM과 생존을 산 다종 채권 Long", verdict="성공 — bankruptcy 회피·여러 2008/2010 채무 상환, exact issue IRR은 미검증", score=8.0, process=7.5,
        conclusion="Level 3가 파산하지 않고 2008·2010 만기채무를 실제 상환·상환전 매입했으므로 broad bond Long과 seniority 선택은 성공했다. 다만 원문이 하나의 CUSIP·매입가·coupon path를 고정하지 않아 모든 채권이 25~35% YTM으로 par 상환됐다고 일반화하거나 exact IRR을 만들 수 없다.",
        t0="주가는 고점 대비 97% 하락한 약 $4.50, 채권은 25~35% YTM이었다. 논지는 IP dominance, optics-to-optics, dark fiber lighting에 향후 10년 $500bn 필요, outsourcing, data traffic 고성장의 다섯 전제를 바탕으로 모든 Level 3 bonds가 지급될 것이라 봤다. 2001말 debt는 secured $1.357bn, senior unsecured $3.370bn, subordinated $1.340bn, 합계 $6.067bn. cash $1.5bn+unused revolver $650m으로 $2.1bn liquidity가 있었고 2004 FCF+를 기대했다.",
        reverse="25~35% YTM은 시장이 default, coercive exchange, subordination, duration을 크게 가격에 넣었다는 뜻이다. network cost $10bn은 recovery value가 아니며 dark-fiber replacement spending이 실제 수요로 전환되지 않을 수 있다. bond별 담보·만기·exchange 조건을 구분해야 한다.",
        valuation="1998~2001 revenue는 $392m→$515m→$1.2bn→$1.5bn으로 늘었지만 FCF는 1999 -$2.9bn, 2000 -$4.4bn, 2001 -$2.1bn이었다. 원문은 2002 burn <$1bn, 2003 <$500m, 2004 positive를 예상했다. 핵심 coverage는 $2.1bn liquidity가 inflection까지 burn·interest·maturity를 덮는지였다.",
        actual="회사는 2002~04 할인매입과 신규자본으로 maturity를 관리했다. 2004년에는 일부 2008 notes를 83~89에 매입했고, 2006년 남은 9.125% 2008 notes 약 $398m과 10.5% 2008 notes 약 $62m을 상환했다. 2008년 남은 11% 2008 notes 약 $20m과 euro notes를 지급했다. 6% converts는 2008~09 매입·교환 후 2010년 잔액 약 $111m을 만기에 상환했다.",
        price="원문이 특정 CUSIP, clean price, accrued interest, trade/exit date를 고정하지 않았다. 따라서 observed outcome은 'broad bond basket의 principal survival 성공'으로 판정하되 25~35% realized YTM, MFE·MAE는 계산하지 않는다.",
        drivers="성공은 network TAM보다 liquidity 확보, 할인 debt retirement, maturity extension, 신규 junior capital과 점진적 operating improvement가 만들었다. common dilution은 bondholder survival에 오히려 긍정적일 수 있었다.",
        counterfactual="같은 enterprise가 생존해도 특정 subordinated issue가 강제교환·할인 tender를 겪었다면 '모든 채권 25~35% 수익' 주장은 유지되는가?",
        error="회사 생존 분석은 강했지만 여러 채권을 하나의 수익률로 묶고 Buffett association과 management ethics를 credit protection처럼 사용했다.",
        warning="2004 FCF 전환이 지연되거나 $2.1bn liquidity가 예상 burn보다 빨리 줄면 핵심 반증이었다. 실제로 회사는 단순 cash burn 종료 대신 적극적 liability management를 택했다.", first_signal_date="2003-12-31",
        scenarios=[("Bear", "FCF 지연·exchange haircut", "sub debt 손실", "issue별 일부 교환"), ("Base", "liquidity bridge·할인매입", "높은 carry+par 회수", "여러 2008/2010 채무 상환"), ("Bull", "2004 FCF+·rerating", "25~35% YTM 온전 실현", "exact issue 미확인")],
        lessons=["distressed debt는 회사가 아니라 CUSIP·seniority·문서 단위로 분석한다.", "equity dilution은 채권 회수율을 높일 수 있다.", "replacement cost는 recovery waterfall에서 담보가능성과 매각비용을 반영한다."],
        checklist=["CUSIP·매입 clean price", "seniority·guarantee", "restricted cash·revolver", "분기 burn", "mandatory maturities", "exchange/tender terms", "coupon·exit cash-flow dates"],
        scorecard=[("Business thesis", "장기 생존 성공"), ("Valuation thesis", "높은 YTM 보상 적중"), ("Catalyst thesis", "liability management로 변경"), ("Timing / path", "대체로 성공"), ("Security selection", "채권 Long 우수·issue 모호")],
        claims=[
            C("IP·data traffic 장기성장", "IP가 지배하고 data traffic이 고성장한다.", "트래픽이 fiber capacity 수요를 채운다.", "다섯 산업 전제와 revenue growth.", "price/bit 하락보다 volume 성장이 빠르다.", "CNS revenue·margin이 계속 축소되면 반증.", "회사는 생존·통합됐고 망은 전략자산이 됐다.", "방향은 맞지만 bond payoff의 충분조건 아님.", "성공", "산업방향을 issue coverage와 혼합했다.", "traffic thesis는 cash interest coverage로 번역한다."),
            C("$2.1bn liquidity가 FCF+까지 연결", "cash $1.5bn과 revolver $650m이면 2004까지 버틴다.", "liquidity가 burn·interest·maturity를 흡수한다.", "2001말 liquidity와 burn forecast.", "revolver 가용성과 burn forecast가 유지된다.", "liquidity runway가 2004 이전 소진되면 반증.", "신규자본·discount repurchase를 병행해 bankruptcy를 피했다.", "단독 liquidity보다 liability management 기여 큼.", "부분 성공", "static cash bridge로 봤다.", "credit runway는 신규자본과 교환확률을 포함한다."),
            C("FCF burn이 -$2.1bn→0으로 축소", "2002 <-$1bn, 2003 <-$500m, 2004 positive다.", "망 완공과 매출성장이 자금수요를 줄인다.", "1999~01 burn history와 원문 forecast.", "가격·고객신용·통합비가 안정된다.", "2004에도 큰 burn이면 timing 반증.", "단순 forecast보다 전환이 늦었고 debt actions가 생존을 보완했다.", "timing miss, terminal survival hit.", "부분 실패", "operating path를 낙관했다.", "credit는 peak funding need를 stress한다."),
            C("network value가 debt를 덮음", ">$10bn 구축비가 $6.1bn debt에 recovery cushion을 준다.", "strategic/reproduction value가 creditor recovery를 지지한다.", "network cost와 debt stack.", "distress sale haircut 뒤에도 EV가 debt 이상이다.", "asset sale bid가 senior claims 아래면 반증.", "파산 없이 debt를 관리했고 장기 strategic sale이 성사됐다.", "기업수준 방향 확인·당시 liquidation value 미확인.", "부분 성공", "cost와 sale value를 동일시했다.", "recovery는 cash EBITDA와 comparable sale value를 함께 쓴다."),
            C("debt retirement가 accretive", "회사가 할인채를 사면 face debt와 interest가 줄어든다.", "cash 1달러로 1달러 이상 claim을 제거한다.", "6개월간 face $2.1bn retirement 주장.", "현금소진보다 discount capture가 크다.", "repurchase 뒤 liquidity가 위험수준이면 반증.", "2004 83~89 매입, 이후 상환·교환이 이어졌다.", "실제 liability management 확인.", "성공", "issue별 우선순위 차이를 덜 봤다.", "discount repurchase는 runway와 함께 평가한다."),
            C("모든 bonds가 전액지급", "25~35% YTM 채권은 모두 par로 갚힌다.", "기업생존과 maturity extension이 principal을 보존한다.", "원문 debt list와 liquidity.", "모든 issue가 coercive exchange 없이 동일 회수한다.", "어느 issue라도 haircut이면 표현 반증.", "여러 2008/2010 채무는 상환됐지만 일부는 교환·할인매입됐다.", "broad survival 성공, all-issue literal claim 미확인.", "부분 성공", "security specificity 부족.", "채권 thesis는 issue matrix가 필수다."),
            C("25%+ annual return 6~8년", "매입 YTM이 realized return으로 이어진다.", "coupon 재투자와 par repayment가 복리수익을 만든다.", "원문 quoted YTM.", "매입가·coupon·exit와 tender가 명확하다.", "교환·조기상환·가격차이로 realized cash flow가 바뀌면 재계산.", "principal survival은 확인됐으나 거래 cash-flow가 없다.", "exact IRR 계산불가.", "성과 방향 성공·수치 미검증", "quoted YTM을 realized IRR로 취급할 위험.", "수익률에는 cash-flow 날짜와 security ID를 남긴다."),
        ],
        metrics=[("Debt stack", "$6.067bn", "전액 service", "bank debt·2008/2010 notes 상환/관리", "성공"), ("Liquidity", "$2.1bn", "2004까지 bridge", "신규자본·교환 병행", "부분"), ("FCF", "2001 -$2.1bn", "2004 positive", "전환 지연", "미달"), ("Quoted YTM", "25~35%", "realized", "exact issue IRR 없음", "미검증"), ("2008/2010 maturities", "distressed", "par recovery", "여러 issue 실제 지급", "성공")],
        timeline=[("2002-04-19", "VIC bond Long", "25~35% YTM"), ("2002", "junior convert financing·discount retirements", "liquidity 연장"), ("2003", "$1.125bn secured facility 상환", "senior credit 개선"), ("2004", "2008 notes 83~89에 매입", "liability management"), ("2006", "2008 notes 약 $460m 상환", "principal recovery"), ("2008", "잔여 2008 notes 지급", "maturity 통과"), ("2009", "6% converts 일부 교환", "경로 분기"), ("2010", "잔여 6% converts 약 $111m 만기상환", "생존 확인")],
    ),
    dict(
        id="6c4d3871-880a-45e2-8fc6-3706b125ddeb", date="2003-03-17", author="jon64",
        filename="analysis/ideas/2003/2003-03-17_LVLT_bank_debt_long.md", source="https://www.valueinvestorsclub.com/idea/Level_3_Bank_Debt/9040413468",
        direction="Long", security="$1.125bn senior secured purchase-money bank debt / Long", entry="약 83; L+325~450", horizon="3.5~4.5년 maturity", raw_horizon="원문 12% unlevered·20%+ 2:1 levered",
        title="담보·noncore resale·Genuity 개선을 산 bank debt Long", verdict="강한 성공 — 2003년 facility 전액상환", score=9.0, process=8.5,
        conclusion="83에 매입한 $1.125bn senior secured facility는 회사가 2003년에 현금·restricted cash와 신규 10.75% notes proceeds로 전액상환했다. 원문의 3.5~4.5년보다 빨리 credit event가 해소돼 security selection은 강하게 성공했다. 정확한 settlement date·coupon carry가 없어 12%/levered IRR은 재계산하지 않는다.",
        t0="원문은 $1.125bn outstanding, 최대 $1.275bn의 purchase-money senior secured bank debt를 83에 매수해 L+325~450, 약 12% unlevered yield를 제시했다. minimum cash covenant $400~500m이 약 31c coverage, noncore software resale 사업 $60m EBITDA를 $350~450m으로 평가해 약 30c, core post-Genuity EBITDA $550~650m을 더해 3~4x coverage를 주장했다. Genuity는 $130m+약 $50m burn으로 샀고 $660m run-rate revenue의 margin을 30%→64%→80%로 높일 것으로 봤다.",
        reverse="가격 83은 secured claim인데도 refinancing·cash-burn·담보가치 불확실성을 반영했다. 3~4x coverage는 software resale valuation과 예상 EBITDA를 합친 going-concern 수치라 liquidation coverage가 아니다. leverage를 얹으면 recovery는 같아도 margin-call과 funding risk가 추가된다.",
        valuation="unlevered payoff는 par accretion 17포인트+floating coupon이다. maturity까지 약 4년이면 단순 price accretion만 연 4.8% 수준이고 coupon을 더해 약 12% 주장에 접근한다. 다만 실제 조기상환일·LIBOR fixing·accrued interest가 없어 exact IRR을 만들지 않는다. 2:1 leverage의 20%+는 repo rate·haircut·margin call을 차감해야 한다.",
        actual="Level 3는 2003년에 cash·restricted cash와 신규 10.75% senior notes proceeds를 사용해 $1.125bn purchase-money Senior Secured Credit Facility를 전액상환했다. 이는 enterprise turnaround를 기다리지 않고 해당 senior claim이 현금으로 회수된 직접적 security outcome이다.",
        price="83 매입, par repayment라는 방향은 확인된다. 그러나 exact purchase settlement, floating coupon cash dates, repayment date와 leverage financing cost가 없어 unlevered 12% 및 levered 20%+ IRR은 수치 확정하지 않는다.",
        drivers="수익의 직접 driver는 높은 담보순위, par까지 17포인트 discount, 회사의 refinancing 능력과 신규 unsecured capital이었다. Genuity margin 80%나 2004 FCF+가 완전히 실현돼야만 회수되는 구조가 아니었다.",
        counterfactual="Genuity synergy가 실패해도 신규 unsecured 자본으로 secured facility를 par 상환할 수 있다면 가장 중요한 thesis는 enterprise turnaround인가 seniority/refinancing인가?",
        error="원문은 좋은 security를 골랐지만 going-concern asset values를 단순 합산했고 2:1 leverage의 financing·margin-call risk를 작게 다뤘다.",
        warning="minimum cash covenant 하회 또는 10.75% notes 발행 실패가 즉시 반증이었으나, 실제로 refinancing이 먼저 성사됐다.", first_signal_date="2003-12-31",
        scenarios=[("Bear", "refinancing 실패·담보가치 하락", "83 아래 recovery", "미발생"), ("Base", "new notes·cash로 takeout", "coupon+17pt accretion", "2003 전액상환"), ("Bull", "빠른 상환+2:1 leverage", "20%+ 주장", "exact IRR 미확인")],
        lessons=["distress에서 좋은 회사보다 먼저 갚히는 증권을 찾는다.", "senior claim은 equity FCF가 아니라 refinancing capacity로도 상환된다.", "levered bond IRR은 asset yield와 funding·margin-call risk를 분리한다."],
        checklist=["facility principal", "collateral·guarantee", "cash covenant", "new-money issuance", "restricted cash", "coupon fixing", "exact repayment date"],
        scorecard=[("Business thesis", "일부 불필요·방향 적중"), ("Valuation thesis", "83→par 적중"), ("Catalyst thesis", "refinancing 조기 성공"), ("Timing / path", "예상보다 빠른 성공"), ("Security selection", "탁월")],
        claims=[
            C("secured debt가 3~4x covered", "cash·resale·core value가 claim을 여러 번 덮는다.", "담보와 seniority가 downside recovery를 높인다.", "$400~500m cash covenant, resale $350~450m, core EBITDA.", "going-concern values가 stress에서도 유지된다.", "coverage가 1x 아래면 반증.", "facility는 2003년 par 전액상환됐다.", "recovery 100% 직접 확인.", "성공", "coverage 구성요소 중복 가능성.", "recovery bridge는 중복 없는 자산·현금으로 만든다."),
            C("Genuity 인수가 EBITDA를 만든다", "$180m 이하 투입으로 $200~300m EBITDA를 얻는다.", "망 통합과 access-cost 절감이 margin을 30→64→80%로 높인다.", "$660m run-rate revenue와 synergy estimate.", "customer churn과 integration cost가 낮다.", "margin·revenue가 계획보다 크게 낮으면 반증.", "상환은 Genuity 완전 정상화 전에 refinancing으로 이뤄졌다.", "credit 성공의 필요조건이 아니었음.", "미검증/비핵심", "extreme margin을 base에 넣었다.", "security payoff의 필수·보조 claim을 구분한다."),
            C("cash covenant가 31c floor", "$400~500m minimum cash가 principal 일부를 보호한다.", "covenant breach 전 lender가 통제권·remedy를 얻는다.", "원문 covenant와 principal.", "cash가 unrestricted이며 lender가 선순위 접근 가능하다.", "waiver·restricted cash면 haircut.", "cash·restricted cash가 실제 takeout 재원에 포함됐다.", "floor mechanism 확인.", "성공", "covenant cash와 recovery cash를 동일시할 위험.", "현금의 법적 가용성과 pledge를 확인한다."),
            C("resale 사업이 약 30c coverage", "$60m EBITDA 사업이 $350~450m 가치다.", "비핵심 매각이 secured debt를 줄일 수 있다.", "원문 EBITDA·multiple.", "분리가능하고 buyer·tax leakage가 작다.", "매각불가·multiple 압축이면 반증.", "직접 매각회수보다 refinancing이 facility를 갚았다.", "30c valuation은 직접 검증되지 않음.", "미검증", "예상 asset sale을 현금처럼 합산했다.", "coverage는 realizability·tax·timing haircut을 둔다."),
            C("2004 FCF+가 takeout을 돕는다", "Q2 2004부터 FCF positive다.", "burn 종료가 refinancing과 par repayment 확률을 높인다.", "원문 operating forecast.", "integration·pricing이 계획대로다.", "FCF+ 지연 시 maturity coverage 재산정.", "2003년 facility가 먼저 전액상환됐다.", "forecast 검증 전 payoff 완료.", "비핵심", "느린 촉매를 핵심처럼 제시했다.", "채권은 가장 빠른 상환경로를 우선순위화한다."),
            C("83 매입은 12% unlevered", "coupon과 par accretion으로 연 12%를 번다.", "floating coupon과 17-point pull-to-par가 수익을 만든다.", "83 price, L+325~450, 3.5~4.5년.", "par repayment와 coupon 전액지급.", "haircut·payment block이면 반증.", "par 전액상환 확인.", "exact carry/date 없어 IRR 미확인.", "성공·수치 제한", "headline yield만 남길 위험.", "bond return은 cash-flow 날짜로 검산한다."),
            C("2:1 leverage로 20%+", "은행채권을 차입해 equity IRR을 높인다.", "asset yield와 funding spread 차이가 equity return을 증폭한다.", "원문 leverage illustration.", "financing이 maturity까지 유지되고 margin call이 없다.", "haircut·repo rate 상승이면 thesis 훼손.", "asset은 par 상환됐지만 financing record가 없다.", "levered realized IRR 미검증.", "미검증", "회수성공을 레버리지 성공으로 일반화할 수 없다.", "financing terms 없는 levered IRR은 확정하지 않는다."),
        ],
        metrics=[("매입가/상환", "약 83", "par", "2003 전액상환", "성공"), ("Principal", "$1.125bn", "covered", "전액상환", "성공"), ("Coupon", "L+325~450", "지급", "exact cash dates 없음", "제한"), ("Unlevered return", "약 12% 주장", "실현", "방향 성공·IRR 미확인", "제한"), ("Genuity EBITDA", "$200~300m 예상", "margin 80%", "payoff에 불필요", "미검증")],
        timeline=[("2003-03-17", "VIC bank debt Long", "83·12% unlevered"), ("2003", "10.75% senior notes 조달", "secured takeout 재원"), ("2003", "$1.125bn facility 전액상환", "security payoff 성공"), ("2004", "다른 2008 notes 할인매입", "credit 개선 지속"), ("2006", "2008 notes redemption", "maturity 관리"), ("2011", "Global Crossing 결합", "enterprise 생존")],
    ),
    dict(
        id="107fd97a-4482-4f35-af20-b8f2ee3e325f", date="2004-12-30", author="doggy835",
        filename="analysis/ideas/2004/2004-12-30_LVLT_convert_pair.md", source="https://www.valueinvestorsclub.com/idea/Level_3/2370352061",
        direction="Pair Long", security="Long 6% subordinated convertible notes / Short 100 LVLT common per bond / optional Jan-2006 $7.50 calls", entry="bond just below 60; common 약 $3.45; call 약 $0.05", horizon="2009~2010 bond maturity", raw_horizon="maturity 또는 restructuring까지",
        title="6% convert를 사고 common을 판 capital-structure pair", verdict="성공 가능성 높음 — principal survival·dilution은 적중, exact pair IRR은 미검증", score=8.0, process=8.5,
        conclusion="회사는 bankruptcy를 피했고 6% converts를 2008~09 매입·교환한 뒤 2010 잔액 약 $111m을 만기에 갚았다. 따라서 bond survival과 equity dilution을 함께 산 구조는 논리적으로 성공 가능성이 높다. 다만 어느 6% tranche를 몇 주 short했고 tender/exchange에 어떻게 응했는지 없어 exact pair IRR은 확정하지 않는다.",
        t0="capital structure는 secured $875m, senior unsecured $3.4bn, 6% subordinated converts $875m, debt $5.15bn, cash $850m, net debt $4.3bn, common market cap $2.35bn, TEV $6.65bn이었다. bond는 60 아래로 10%+ current yield, bond당 common 100주를 short하고 $7.50 Jan-2006 calls를 $0.05에 사 tail risk를 제한하자는 구조였다. fully diluted shares는 5년 전 360m에서 700m 이상으로 늘어 dilution을 핵심으로 봤다.",
        reverse="pair는 방향중립처럼 보여도 완전 hedge가 아니다. convert delta, borrow availability·fee, coupon blockage, exchange ratio, call expiry, tender 선택이 수익을 바꾼다. bankruptcy에서 subordinated recovery가 0이고 common도 0이면 coupon과 short gain이 bond loss를 얼마나 상쇄하는지가 핵심이다.",
        valuation="원문 stress case는 YE2008 Chapter 11에서 bond -585, coupon +240, common short +345로 breakeven이다. maturity·common flat이면 +715, maturity·common 급등은 cheap call로 cap을 씌워 +310에서 call cost 25~50을 뺀다고 했다. 이는 borrow fee·margin·tax·conversion adjustment 전 payoff다.",
        actual="2008년 6% converts due 2009 약 $39m과 due 2010 약 $32m을 매입했고, 2009년에는 각각 약 $126m·$55m을 더 매입했다. 2010 issue 약 $142m 등은 새 7% converts $200m와 cash $78m으로 교환됐고, 2010년 남은 6% converts 약 $111m은 만기에 상환됐다. 회사는 지속적으로 debt-for-equity를 사용해 common dilution thesis도 확인했다.",
        price="bond coupon·principal survival과 희석 방향은 확인된다. 하지만 정확한 issue, short entry·cover, borrow fee, call 수량·만기, tender 선택, exchange consideration이 없어 pair의 realized IRR·MFE·MAE는 계산하지 않는다.",
        drivers="수익은 60 아래 bond의 coupon·pull-to-par, company survival, refinancing과 common dilution/약세에서 나왔을 가능성이 크다. 핵심은 enterprise direction을 맞히는 것이 아니라 같은 enterprise 안에서 더 싼 claim을 사고 비싼 residual을 판 것이다.",
        counterfactual="common이 급등하고 bond가 강제교환되며 short borrow가 회수됐다면 5센트 call만으로 실제 hedge를 유지할 수 있었는가?",
        error="payoff table은 훌륭하지만 dynamic delta·borrow·tender path와 subordinated recovery timing을 정적으로 처리했다.",
        warning="short borrow recall, conversion ratio 조정, coupon blockage 중 하나라도 발생하면 정적 arbitrage가 깨진다. 실제 liability management가 시작된 2008년부터 position-level 재계산이 필요했다.", first_signal_date="2008-12-31",
        scenarios=[("Bear", "YE08 Ch11·sub recovery 0", "원문 거의 breakeven", "bankruptcy 미발생"), ("Base", "bond maturity·common flat/약세", "+715 전 비용", "principal survival·dilution"), ("Bull risk", "common 급등", "call hedge 후 +310 전 비용", "경로자료 없음")],
        lessons=["capital-structure pair는 두 다리의 cash flow와 path dependency를 함께 기록한다.", "convert hedge는 고정 주식수보다 delta·borrow·corporate action이 중요하다.", "정확한 issue와 tender 선택이 없으면 realized arbitrage IRR을 만들지 않는다."],
        checklist=["exact note tranche", "conversion ratio", "short borrow·fee", "coupon dates", "call expiry·strike", "tender/exchange election", "margin requirements"],
        scorecard=[("Business thesis", "생존 성공"), ("Valuation thesis", "bond/common 상대가치 적중"), ("Catalyst thesis", "liability management"), ("Timing / path", "경로 복잡·대체로 성공"), ("Security selection", "우수")],
        claims=[
            C("6% converts below 60은 싸다", "10%+ current yield와 par upside가 있다.", "coupon·pull-to-par가 common보다 먼저 지급된다.", "bond price·coupon·capital stack.", "회사 생존·coupon 지급·maturity refinancing.", "coupon block·haircut exchange면 반증.", "다수 notes가 매입·교환되고 잔액은 2010 par 상환됐다.", "principal survival 확인.", "성공", "tranche별 path를 뭉쳤다.", "각 note를 별도 cash-flow ledger로 관리한다."),
            C("common short가 bankruptcy loss를 상쇄", "100주 short gain이 zero sub recovery를 메운다.", "같은 EV 하락에서 residual common이 먼저 소멸한다.", "원문 stress payoff -585+240+345=0.", "common entry·cover와 short 유지가 가능하다.", "borrow recall·common squeeze면 반증.", "회사 bankruptcy는 없었고 common dilution이 계속됐다.", "정확한 short gain 미복원.", "방향 성공·수치 미검증", "borrow friction을 제외했다.", "short leg는 locate·fee·recall을 손익에 넣는다."),
            C("cheap call이 upside tail을 막음", "$0.05 Jan06 $7.50 calls가 common 급등을 제한한다.", "out-of-the-money option이 short convexity를 보완한다.", "원문 call 가격·strike.", "급등이 option expiry 전 발생한다.", "expiry 뒤 급등하거나 volatility repricing이면 실패.", "position path와 option exercise 기록이 없다.", "hedge effectiveness 미검증.", "미검증", "만기 mismatch를 작게 봤다.", "tail hedge는 exposure horizon과 만기를 맞춘다."),
            C("dilution이 common upside를 제한", "share count 360m→700m+가 per-share value를 희석한다.", "debt-for-equity가 creditor를 보호하고 common claim을 넓힌다.", "원문 fully diluted share comparison.", "operating value growth가 dilution보다 작다.", "FCF 급증이 share growth를 압도하면 반증.", "이후 debt-for-equity와 convert issuance가 계속됐다.", "메커니즘 확인.", "성공", "gross shares와 economic dilution을 혼용 가능.", "per-share EV·FCF로 dilution을 추적한다."),
            C("Chapter 11 downside도 breakeven", "zero bond recovery에서도 coupon+short가 원금을 메운다.", "cross-capital-structure hedge가 tail loss를 상쇄한다.", "원문 payoff table.", "coupon 4년 수령·short 100주 유지가 동시에 가능하다.", "조기 default·coupon stop이면 반증.", "Chapter 11은 발생하지 않아 stress case 자체는 시험되지 않았다.", "모델 robustness 미검증.", "미검증", "default timing을 YE08로 고정했다.", "distress payoff는 default date별로 만든다."),
            C("maturity면 큰 absolute profit", "common flat이면 bond+coupon에서 +715다.", "bond discount와 carry가 pair 수익의 주축이다.", "원문 base payoff.", "full coupon·par payment·low borrow cost.", "discount tender·비싼 borrow면 수익 감소.", "notes survival은 확인되나 tender/exchange path가 달랐다.", "exact +715 미확인.", "부분 성공", "corporate actions를 단순 maturity로 처리했다.", "tender consideration을 실제 cash flow로 대체한다."),
            C("pair가 directional risk를 낮춤", "enterprise outcome과 무관하게 양의 payoff를 만든다.", "senior/sub claim relative mispricing을 거래한다.", "three-scenario payoff.", "basis·delta·liquidity가 안정적이다.", "두 다리가 동시에 손실이면 반증.", "관찰 outcome은 thesis 방향과 일치하나 trade ledger가 없다.", "robustness 방향만 확인.", "부분 성공", "market-neutral 표현이 과했다.", "pair는 residual factor exposures를 명시한다."),
        ],
        metrics=[("Convert price", "<60", "par+coupon", "매입·교환·잔액 par 상환", "성공"), ("Current yield", "10%+", "지속", "coupon path issue별 상이", "부분"), ("Common hedge", "100 shares/bond", "downside 상쇄", "exact cover 없음", "미검증"), ("Diluted shares", "700m+ vs 360m", "common 압박", "debt-for-equity 지속", "성공"), ("2010 잔액", "6% notes", "지급", "약 $111m 만기상환", "성공")],
        timeline=[("2004-12-30", "VIC convert/common pair", "bond <60·common short"), ("2008", "6% converts 일부 매입", "discount exit 가능"), ("2009", "추가 매입", "principal 축소"), ("2009", "일부 새 7% convert로 교환", "cash-flow path 변경"), ("2010", "잔여 약 $111m 만기상환", "bond survival"), ("2011", "reverse split", "누적 dilution/가격 흔적")],
    ),
    dict(
        id="44312f7c-f1b7-4f46-b92b-dc8d08c79832", date="2007-11-11", author="biv930",
        filename="analysis/ideas/2007/2007-11-11_LVLT_long.md", source="https://www.valueinvestorsclub.com/idea/Level_3_Communications/1821042905",
        direction="Long", security="LVLT common equity / Long", entry="약 $3; target $9", horizon="2~3년", raw_horizon="2~3년 3배 주장",
        title="industry consolidation과 60% incremental EBITDA를 산 common Long", verdict="실패 — integration 경고 현실화·2011 EBITDA forecast 대폭 미달", score=3.0, process=7.0,
        conclusion="$3에서 $9, 2~3년 3배 논지는 실패했다. 원문이 스스로 경고한 CFO 이탈·과도한 인력감축·integration/service 문제는 실제 2008 cash consumption으로 이어졌다. 2011 adjusted EBITDA는 Global Crossing 3개월분을 포함해 $958m으로 원문 2011E $2.2bn보다 약 56% 낮았다.",
        t0="원문은 20개가 넘던 network가 소수로 통합되면 price decline이 둔화되고 traffic volume 60%+가 성장을 만든다고 봤다. 7개 인수 뒤 2008 이후 core revenue mid-teens, noncore -25~30%, annual enterprise buildings 700~1,000, traffic +80%, incremental gross margin 70~75%, incremental EBITDA margin 60~65%, capex/revenue 12~14%, maintenance capex 3%를 가정했다. 2011 EBITDA $2.2bn·after-tax FCF $0.30/share, SOTP $8.50을 제시했다.",
        reverse="시장은 인수 통합 실패, 고객 churn, 서비스 저하, 고레버리지와 capex를 가격에 넣었다. 60~65% incremental EBITDA는 revenue mix·pricing·integration cost가 모두 맞아야 한다. reproduction value $20~25bn도 수익성이 없으면 common에 귀속되지 않는다.",
        valuation="SOTP는 EV $18.4bn에서 net debt 등을 차감해 equity 약 $13bn, 주당 $8.50을 산출했다. 별도 접근은 2011 FCF $0.30에 7배와 NOL $0.90을 더했다. 양쪽 모두 $2.2bn EBITDA와 integration 성공에 민감하며 share count·reverse split 전후 단위를 엄격히 맞춰야 한다.",
        actual="2008년 회사는 integration·provisioning 문제를 인정했고 cash를 소비할 것으로 전망했다. 2011 adjusted EBITDA는 $958m, interest expense는 $716m이었다. 2011년 1-for-15 reverse split 후 Q4 low $16.51은 pre-split 약 $1.10에 해당해 원문 약 $3보다 현저히 낮다. 2014 이후 FCF 전환과 2017 매각은 원 2~3년 horizon 밖이다.",
        price="정확한 daily price series는 없으나 2011 Q4 split-adjusted low $16.51, 즉 pre-split 약 $1.10은 약 $3 entry 대비 약 -63%다. 이 비교는 low-to-entry라 realized return이 아니며, target $9와 2~3년 성과를 충족하지 못했다는 판정에만 쓴다.",
        drivers="손실은 산업 traffic 성장보다 인수통합·고객서비스·매출 mix, 지속 capex와 interest가 우선한 데서 나왔다. 고객 획득 IRR 74% 같은 unit economics도 churn·provisioning delay·shared cost를 통과하지 못했다.",
        counterfactual="traffic +80%가 맞아도 pricing -10%, noncore -30%, churn·integration 비용이 동시에 오면 60~65% incremental EBITDA가 가능한가?",
        error="좋은 산업구조 논지 위에 다수의 bull operating assumption을 동시에 쌓고, 원문에 적힌 execution red flags를 valuation downside에 충분히 반영하지 않았다.",
        warning="2008년 integration 문제와 cash consumption 전망이 첫 명확한 thesis break였다.", first_signal_date="2008-02-29",
        scenarios=[("Bear", "integration 실패·cash burn", "common $1대", "2011 pre-split low 약 $1.10"), ("Base", "core mid-teens·60% incremental margin", "$8.50~$9", "EBITDA 대폭 미달"), ("Bull", "traffic 80%·pricing 안정", "3x 이상", "미실현")],
        lessons=["traffic growth는 price·mix·service cost를 통과한 incremental EBITDA로 검증한다.", "연속 인수에서는 synergy보다 provisioning·churn·인력지표가 선행한다.", "2~3년 thesis를 10년 뒤 M&A로 구제하지 않는다."],
        checklist=["CNS organic growth", "provisioning interval", "enterprise churn", "incremental EBITDA", "capex/revenue", "cash interest", "split-adjusted per-share model"],
        scorecard=[("Business thesis", "산업통합 장기 일부"), ("Valuation thesis", "실패"), ("Catalyst thesis", "integration 실패"), ("Timing / path", "강한 실패"), ("Security selection", "common 부적절")],
        claims=[
            C("산업통합이 pricing을 안정", "20+ networks가 소수로 줄어 price decline이 둔화된다.", "공급규율과 scale이 unit economics를 개선한다.", "7개 acquisitions와 산업구조.", "경쟁사·고객 consolidation이 가격압박을 키우지 않는다.", "organic revenue와 price/mix 악화면 반증.", "장기 consolidation은 진행됐지만 horizon 내 cash economics는 부진했다.", "산업방향 적중·투자시점 실패.", "부분 성공", "구조변화를 timing catalyst로 봤다.", "industry thesis에는 earnings inflection 날짜가 필요하다."),
            C("core revenue mid-teens 성장", "2008 이후 core가 mid-teens로 성장한다.", "traffic·enterprise buildings가 noncore decline을 상쇄한다.", "700~1,000 buildings, traffic +80% 계획.", "churn·provisioning이 통제된다.", "core organic growth가 mid-teens에 못 미치면 반증.", "integration·service 문제와 cash consumption이 나타났다.", "성장 bridge 훼손.", "실패", "gross sales capacity를 billed organic growth로 취급했다.", "installed building보다 activated revenue를 본다."),
            C("incremental EBITDA margin 60~65%", "gross margin 70~75%, 낮은 SG&A 증가로 고수익 전환한다.", "고정 network에 매출이 붙어 operating leverage가 난다.", "원문 cost model.", "price/mix·service cost·integration가 안정적이다.", "EBITDA가 revenue보다 느리면 반증.", "2011 EBITDA $958m으로 $2.2bn forecast보다 크게 낮았다.", "약 -56% forecast gap.", "실패", "steady-state margin을 ramp에 적용했다.", "incremental margin은 실제 분기 delta로 측정한다."),
            C("2011 EBITDA $2.2bn·FCF $0.30", "integration 뒤 현금창출이 급증한다.", "EBITDA가 interest·capex를 넘어 common FCF가 된다.", "원문 2011 model.", "capex 12~14%, interest와 share count가 안정된다.", "EBITDA·FCF가 forecast 절반이면 반증.", "2011 EBITDA $958m, interest $716m.", "EBITDA 약 $1.24bn/-56% 미달.", "실패", "cash interest 부담을 작게 봤다.", "고레버리지 FCF는 EBITDA보다 interest sensitivity가 우선이다."),
            C("고객당 pre-tax IRR 74%", "12% churn·8년 life에도 연결 economics가 높다.", "upfront sales/connect cost 뒤 반복 gross profit이 남는다.", "원문 customer cohort 계산.", "churn definition·shared capex·bad debt가 완전하다.", "actual cohort payback 지연이면 반증.", "provisioning·service 문제가 고객경제를 훼손했다.", "모델 입력의 실행품질 미달.", "실패", "cohort 밖 shared cost를 제외했다.", "customer IRR을 consolidated FCF와 reconcile한다."),
            C("reproduction value $20~25bn", "망을 다시 짓는 비용이 EV floor다.", "strategic scarcity가 long-term sale value를 지지한다.", "원문 network valuation.", "earning value와 buyer demand가 cost를 지지한다.", "cash burn 지속 시 floor를 할인.", "2017 strategic sale은 자산가치를 확인했지만 horizon 밖이다.", "terminal asset value 일부, timing payoff 실패.", "부분 성공", "duration과 debt를 무시했다.", "replacement value에는 monetization date와 carrying cost를 붙인다."),
            C("$3→$9 in 2~3 years", "operating leverage와 rerating으로 3배가 된다.", "EBITDA 성장·deleveraging·multiple이 결합한다.", "SOTP $8.50, FCF approach.", "execution red flags가 빠르게 해소된다.", "2008 cash burn 또는 2011 $2.2bn EBITDA miss면 실패.", "2011 pre-split low 약 $1.10, EBITDA $958m.", "target 방향과 반대.", "강한 실패", "여러 bull 조건을 base로 묶었다.", "target 기여도를 earnings·debt·multiple로 분해한다."),
        ],
        metrics=[("Entry / target", "약 $3 / $9", "3x", "2011 pre-split low 약 $1.10", "실패"), ("2011 EBITDA", "T0 base", "$2.2bn", "$958m", "-56%"), ("2011 interest", "고레버리지", "FCF 흡수 가능", "$716m", "부담"), ("Incremental EBITDA margin", "60~65%", "실현", "integration로 미달", "실패"), ("Capex/revenue", "12~14%", "안정", "FCF inflection 지연", "실패")],
        timeline=[("2007-11-11", "VIC common Long", "$3→$9"), ("2008-02", "cash consumption·integration 문제", "첫 반증"), ("2008", "금융위기·telecom stress", "refinancing risk"), ("2011-10-04", "Global Crossing 결합", "추가 통합"), ("2011-Q4", "split-adjusted low $16.51", "pre-split 약 $1.10"), ("2011-12-31", "adjusted EBITDA $958m", "$2.2bn forecast 미달"), ("2014", "positive sustainable FCF", "horizon 밖 turnaround")],
    ),
    dict(
        id="e32af27d-688a-4ce1-8cf4-f5df3499ae50", date="2011-10-11", author="biv930",
        filename="analysis/ideas/2011/2011-10-11_LVLT_long.md", source="",
        direction="Long", security="LVLT common equity / Long", entry="원문 implied pre-split 약 $1.80; 2011-10-03 split-adjusted reference $21.15", horizon="2013~2014", raw_horizon="2013 FCF inflection·2~3x upside",
        title="Global Crossing synergy와 2013 FCF inflection을 산 common Long", verdict="혼합 — 2013 forecast 실패, 2014~17 delayed capital appreciation 성공", score=6.5, process=7.5,
        conclusion="2013 EBITDA $2.2bn·FCF $900m은 크게 빗나갔고 2013 sustainable FCF는 약 -$47m이었다. 그러나 2014 $325m, 2015 $626m, 2016 $1.009bn으로 cash engine이 뒤늦게 전환됐고 2017 거래의 현금+주식 가치는 2011 split-adjusted reference 대비 대략 2~3배였다. 논지의 방향은 장기 성공, magnitude·timing은 실패다.",
        t0="Global Crossing 결합 직후 원문은 2013 FCF $0.30/share 대 Street $0.10, 약 6배 자체 FCF·5.5배 EBITDA에서 2~3x upside를 주장했다. revenue growth 6%, incremental EBITDA margin 60%, leverage 6~7x에서 <3.5x, opex savings $350m, interest savings $200m을 가정했다. 2013 EBITDA $2.2bn·FCF $900m 대 consensus $1.6bn·$300m, 2014 FCF $0.50/share와 pre-split reproduction value $11~17을 제시했다.",
        reverse="시장은 integration, voice/noncore decline, leverage, cash interest와 고객이탈을 가격에 넣었다. $900m FCF는 $350m opex·$200m interest savings, 6% growth와 60% incremental margin이 동시에 실현돼야 했다. 높은 operating leverage는 downside에도 대칭적이다.",
        valuation="원문 2013 FCF $900m과 당시 주가 implied 약 $1.80 pre-split을 쓰면 6배 자체 FCF 주장에 맞는다. 하지만 2011 reverse split 1:15 전후 per-share 단위를 혼용하면 큰 오류가 난다. 실제 2013 sustainable FCF 약 -$47m에서는 해당 multiple 논지가 성립하지 않는다.",
        actual="Global Crossing 거래는 2011-10-04 종결됐다. 2011 adjusted EBITDA는 $958m이었다. 회사 proxy가 2014 sustainable FCF $325m, 전년 대비 +$372m이라고 밝혀 2013은 약 -$47m이다. 이후 FCF는 2015 $626m, 2016 $1.009bn으로 늘었다. 2016-10-31 CenturyLink 거래가 발표되고 2017-11-01 $26.50 cash+1.4286 CTL shares로 종결됐다.",
        price="2011-10-03 split-adjusted $21.15를 근사 reference로 사용한다. 2017 consideration은 $26.50+1.4286 CTL로 CTL 시가에 따라 대략 $60~66 범위였다. 약 2~3배 장기 appreciation을 시사하지만 exact VIC execution과 CTL valuation date가 없어 exact IRR은 확정하지 않는다.",
        drivers="장기 수익은 consolidation, synergy의 지연 실현, CNS enterprise mix, refinancing과 2014 이후 FCF inflection, strategic sale이 만들었다. 원 horizon 실패는 integration duration과 interest/capex 부담을 과소평가한 결과다.",
        counterfactual="$900m 2013 FCF가 아니라 -$47m이어도 balance sheet가 버틸 수 있다는 별도 runway 분석이 T0에 있었는가?",
        error="올바른 consolidation direction을 잡았지만 $350m opex·$200m interest savings와 60% incremental margin을 같은 horizon에 겹쳐 2013 FCF를 과대평가했다.",
        warning="2013 sustainable FCF 약 -$47m이 $900m thesis를 수치상 확정 반증했다.", first_signal_date="2013-12-31",
        scenarios=[("Bear", "integration 지연·FCF 음수", "희석·낮은 주가", "2013 -$47m FCF"), ("Base", "$350m synergy·2013 $900m FCF", "2~3x", "2~3년 timing 미달"), ("Delayed bull", "2014~16 FCF ramp·sale", "장기 2~3x", "2017 대략 실현")],
        lessons=["좋은 consolidation thesis도 synergy calendar가 틀리면 IRR이 크게 낮아진다.", "per-share telecom 모델은 reverse split과 dilution을 완전 조정한다.", "장기 승자는 원래 horizon 실패와 분리해 평가한다."],
        checklist=["standalone vs acquired revenue", "realized cost synergy", "cash interest", "FCF definition", "net leverage", "share count/split", "deal consideration mark date"],
        scorecard=[("Business thesis", "지연 성공"), ("Valuation thesis", "장기 성공·2013 무효"), ("Catalyst thesis", "GLBC 종결·synergy 지연"), ("Timing / path", "실패"), ("Security selection", "common 장기 성공")],
        claims=[
            C("GLBC가 scale·enterprise mix 개선", "결합이 더 글로벌한 고마진 network를 만든다.", "중복망·SG&A를 줄이고 on-net revenue를 확대한다.", "pro-forma revenue $6.26bn·EBITDA $1.27bn pre-synergy.", "churn과 integration disruption이 낮다.", "organic CNS·margin이 악화되면 반증.", "결합은 종결되고 장기 FCF가 개선됐다.", "방향 성공·속도 지연.", "성공", "deal close와 synergy realization을 붙였다.", "거래와 통합 KPI를 분리한다."),
            C("opex savings $350m", "중복 network·SG&A를 제거한다.", "비용절감이 EBITDA와 FCF로 직접 흐른다.", "원문 synergy model.", "revenue dis-synergy·one-time cost가 작다.", "cash cost와 churn이 savings를 상쇄하면 반증.", "장기 cash flow는 개선됐으나 2013 FCF는 음수였다.", "동시점 실현 실패.", "지연 성공", "run-rate와 realized cash를 혼용했다.", "synergy는 gross, cost-to-achieve, revenue leakage를 구분한다."),
            C("interest savings $200m", "deleveraging/refinancing으로 cash interest가 준다.", "절감액이 common FCF를 키운다.", "원문 capital structure forecast.", "credit market와 EBITDA가 refinancing을 허용한다.", "interest가 높게 유지되면 반증.", "2011 interest $716m, 2013 FCF 음수로 초기 부담이 컸다.", "2013 bridge 미달.", "실패/지연", "refinancing duration을 낙관했다.", "interest savings는 debt schedule별로 모델링한다."),
            C("2013 EBITDA $2.2bn", "6% growth·60% incremental margin으로 consensus를 크게 이긴다.", "고정망 operating leverage가 EBITDA를 증폭한다.", "원문 vs consensus $1.6bn.", "revenue mix와 pricing이 안정된다.", "actual이 $1.8bn 아래면 thesis 약화.", "2013 FCF proxy가 크게 미달했고 2011 base도 $958m이었다.", "forecast magnitude 과대.", "실패", "incremental margin을 너무 높게 적용했다.", "bull bridge를 consensus delta별로 검증한다."),
            C("2013 FCF $900m", "Street $300m의 3배 현금을 만든다.", "synergy·interest savings·capex discipline이 결합한다.", "원문 FCF bridge.", "모든 개선이 24개월 내 cash로 실현된다.", "FCF가 $300m 아래면 반증.", "2013 sustainable FCF 약 -$47m.", "$947m forecast gap.", "강한 실패", "다수 촉매의 상관을 무시했다.", "현금 forecast는 가장 늦는 구성요소를 기준으로 한다."),
            C("leverage 6~7x→<3.5x", "FCF와 EBITDA 성장으로 equity risk가 빠르게 낮아진다.", "debt paydown과 denominator 성장이 rerating을 만든다.", "원문 target leverage.", "FCF가 양수이고 debt가 늘지 않는다.", "FCF 음수·추가 refinancing이면 지연.", "2014 이후 FCF ramp로 장기 deleveraging path가 열렸다.", "2013 timing 실패.", "지연 성공", "target date를 빠르게 잡았다.", "leverage는 gross debt·lease·average EBITDA로 측정한다."),
            C("2~3x common upside", "6배 FCF·5.5배 EBITDA와 replacement value가 큰 upside를 준다.", "earnings growth·deleveraging·M&A optionality가 주당가치를 키운다.", "원문 valuation과 pre-split $11~17 reproduction range.", "희석·duration이 upside를 먹지 않는다.", "2014까지 FCF inflection 부재면 horizon 실패.", "2017 deal value는 2011 reference의 대략 2~3배.", "magnitude 장기 적중·5~6년 소요.", "지연 성공", "목표수익과 기간을 분리하지 않았다.", "성과는 multiple뿐 아니라 elapsed time을 기록한다."),
        ],
        metrics=[("2013 FCF", "원문", "$900m", "약 -$47m", "-$947m"), ("2014 sustainable FCF", "turnaround", "높은 성장", "$325m", "지연"), ("2015 FCF", "성장", "확대", "$626m", "성공"), ("2016 FCF", "성장", "확대", "$1.009bn", "성공"), ("Deal consideration", "$21.15 reference", "2~3x", "$26.50+1.4286 CTL", "장기 성공")],
        timeline=[("2011-10-04", "Global Crossing 거래 종결", "T0 operating platform"), ("2011-10-11", "VIC common Long", "2013 $900m FCF"), ("2011", "1-for-15 reverse split", "per-share audit 필요"), ("2013-12-31", "sustainable FCF 약 -$47m", "핵심 반증"), ("2014", "sustainable FCF $325m", "turnaround 시작"), ("2015", "FCF $626m", "deleveraging"), ("2016", "FCF $1.009bn·deal announcement", "장기 thesis 확인"), ("2017-11-01", "merger completion", "현금+주식 exit")],
    ),
    dict(
        id="3df8999b-4ddc-4eea-bc10-d0c9949e3170", date="2017-07-29", author="VQRP99",
        filename="analysis/ideas/2017/2017-07-29_LVLT_merger_long.md", source="https://www.valueinvestorsclub.com/idea/LEVEL_3_COMMUNICATIONS_INC/3863570505",
        direction="Long", security="LVLT common into CTL merger / post-close hold", entry="$58.61", horizon="deal close 후 1~2년; standalone 5년", raw_horizon="2017-09-30 예상 close·1~2년 $75~90",
        title="2% merger spread와 post-close synergy rerating을 함께 산 Long", verdict="혼합 — 거래종결 성공, post-close $75~90·dividend thesis 실패", score=5.5, process=7.5,
        conclusion="2017-11-01 계약대로 $26.50 cash+1.4286 CTL shares를 받은 event leg는 성공했다. 그러나 post-close combined EBITDA $10bn, dividend safety와 LVLT-equivalent $75~90 rerating은 이어진 CenturyLink/Lumen의 2019 dividend cut과 2022 dividend elimination으로 반증됐다. arb와 장기 hold를 하나의 성공으로 묶으면 안 된다.",
        t0="LVLT는 $58.61, 360m shares, market cap $21bn, net debt $9bn, NOL 약 $9bn이었다. offer는 $26.50 cash+1.4286 CTL shares로 당시 약 $59.80, 2% spread였고 2017-09-30 close를 기대했다. 결합 EBITDA는 CTL $6bn+LVLT $3bn+$1bn synergy=$10bn, strategic mix 65%, mid-single digit EBITDA growth, 7~8배에서 LVLT-equivalent $75~90을 제시했다.",
        reverse="시장 spread는 regulatory·timing risk와 CTL 주가변동을, 낮은 CTL multiple은 legacy consumer decline·integration·capex·leverage·dividend risk를 반영했다. half-cash consideration은 deal-break downside를 낮추지만 post-close CTL exposure를 제거하지 않는다.",
        valuation="원문 FCF bridge는 $10bn EBITDA-$4bn capex-$2.2bn interest-$650m pension/tax로 약 $3.15bn, 주당 약 $2.80에서 $3를 기대했다. 7~8배 EBITDA rerating과 $1bn synergy가 $75~90을 만들었다. standalone은 replacement value $95, FCF 20~25% CAGR으로 5년 $120~150을 주장했다.",
        actual="거래는 예상보다 약 한 달 늦은 2017-11-01 종결됐고 former LVLT holders가 combined company 약 49%를 보유했다. CenturyLink는 2019 FCF $3.1~3.4bn을 안내했지만 연 dividend를 $1.00으로 낮추는 capital-allocation reset을 발표했다. Lumen은 2022-11-02 common dividend를 완전히 없앴다.",
        price="contractual consideration은 직접 확인된다. 그러나 $75~90 LVLT-equivalent의 exact 1~2년 total return은 CTL share-price·배당·mark date가 필요해 여기서는 임의 계산하지 않는다. dividend cut·elimination은 long-hold thesis의 명확한 fundamental failure signal이다.",
        drivers="event 수익은 small merger spread와 확정 consideration이 만들었다. 장기 손실은 legacy CTL decline, integration/capital intensity, leverage와 dividend-capital allocation이 $1bn synergy·FCF보다 크게 작용한 데서 나왔다.",
        counterfactual="2% arb spread만 원했다면 close 즉시 CTL shares를 매도했어야 하는가, 아니면 $75~90 long을 정당화할 별도 downside·dividend test가 있었는가?",
        error="낮은 deal-break downside와 post-close operating upside를 하나의 포지션으로 묶고, dividend를 FCF output이 아니라 사실상 고정 claim처럼 취급했다.",
        warning="2019년 annual dividend를 $1.00으로 낮춘 결정이 combined-company hold 논지의 첫 명확한 반증이다.", first_signal_date="2019-02-13",
        scenarios=[("Deal break", "LVLT standalone", "원문 downside 제한", "미발생"), ("Arb", "계약대로 close", "2% spread", "2017-11-01 성공"), ("Post-close bull", "$10bn EBITDA·7~8x", "$75~90", "dividend cut·rerating 실패")],
        lessons=["merger arb와 post-close fundamental Long은 entry·exit·반증조건을 분리한다.", "배당안전은 headline FCF보다 leverage·capex·management priority로 검증한다.", "주식대가 거래는 target 가격이 아니라 acquirer exposure를 산다."],
        checklist=["regulatory approvals", "deal consideration mark", "CTL hedge ratio", "realized synergy", "legacy revenue decline", "capex/EBITDA", "dividend coverage·priority"],
        scorecard=[("Business thesis", "LVLT cash engine 성공·결합 실패"), ("Valuation thesis", "arb 성공·rerating 실패"), ("Catalyst thesis", "deal close 성공"), ("Timing / path", "1~2년 hold 실패"), ("Security selection", "arb 적절·unhedged CTL 부적절")],
        claims=[
            C("거래가 2017년 종결", "$26.50+1.4286 CTL을 예정대로 받는다.", "승인과 financing 완료로 2% spread가 수렴한다.", "signed merger·small spread.", "regulatory remedies와 CTL price risk가 관리된다.", "deal delay·break면 반증.", "2017-11-01 계약조건대로 종결.", "예상 9월말 대비 약 한 달 지연.", "성공", "close date를 과도하게 정확히 잡았다.", "arb는 calendar buffer와 share hedge를 둔다."),
            C("LVLT deal-break downside가 낮음", "half cash와 standalone quality가 downside를 줄인다.", "LVLT FCF·replacement value가 break price를 지지한다.", "2016 FCF $1.009bn, NOL·network.", "standalone operating trend가 유지된다.", "CNS/FCF 급락이면 floor 약화.", "deal이 완료돼 직접 시험되지 않았다.", "counterfactual 미검증.", "미검증", "unobserved downside를 성공으로 볼 수 없다.", "deal-break value는 독립 standalone model로 보관한다."),
            C("combined EBITDA $10bn", "$6bn+$3bn+$1bn synergy가 실현된다.", "망·SG&A 중복 제거로 strategic mix와 margin이 오른다.", "원문 pro-forma bridge.", "legacy decline·integration cost가 synergy보다 작다.", "EBITDA·FCF가 계획을 못 따르면 반증.", "2019 FCF guide는 강했지만 자본정책은 방어적으로 바뀌었다.", "headline FCF만으로 equity rerating 부재.", "부분 실패", "synergy와 quality를 같은 것으로 봤다.", "결합 EBITDA는 organic mix와 cost synergy를 분리한다."),
            C("FCF $2.80→$3/share", "$10bn EBITDA에서 capex·interest·tax 후 충분한 현금이 남는다.", "FCF가 deleveraging·dividend·equity value를 동시에 지지한다.", "원문 $10-$4-$2.2-$0.65bn bridge.", "working capital·restructuring·integration cash가 작다.", "배당 cut 또는 leverage 악화면 반증.", "2019 FCF guide $3.1~3.4bn에도 dividend를 낮췄다.", "gross FCF와 distributable FCF 괴리.", "부분 실패", "현금의 경쟁용도를 과소평가했다.", "FCF allocation waterfall을 별도 모델링한다."),
            C("dividend는 안전", "FCF coverage가 높아 CTL payout이 유지된다.", "배당수익이 rerating 대기기간을 보상한다.", "원문 FCF bridge와 payout.", "board가 debt·capex보다 dividend를 우선한다.", "dividend cut이면 즉시 반증.", "2019 annual dividend $1로 cut, 2022 완전 elimination.", "명시적 반증.", "강한 실패", "배당을 discretionary equity distribution이 아닌 coupon처럼 봤다.", "배당안전에는 board priority와 leverage covenant를 포함한다."),
            C("7~8x에서 LVLT $75~90", "strategic mix 65%와 mid-single digit EBITDA growth가 rerating을 만든다.", "질 높은 enterprise mix가 legacy telco discount를 줄인다.", "원문 multiple sensitivity.", "시장과 경영진이 mix 개선을 신뢰한다.", "dividend cut·multiple compression이면 실패.", "post-close capital allocation stress로 rerating thesis가 훼손됐다.", "$75~90 실현 근거 없음.", "실패", "acquirer legacy exposure를 과소평가했다.", "blended company는 segment별 duration multiple을 쓴다."),
            C("standalone $120~150 in 5y", "replacement $95와 FCF CAGR 20~25%가 break downside·optionality를 준다.", "독립 cash growth가 장기 per-share value를 복리화한다.", "LVLT 2014~16 FCF ramp.", "deal break 후 financing·competition이 안정된다.", "FCF growth 둔화면 반증.", "deal이 완료돼 standalone path는 관찰되지 않았다.", "counterfactual이라 outcome 없음.", "미검증", "대체경로를 base upside에 중복가산했다.", "standalone은 deal probability와 별도 확률가중한다."),
        ],
        metrics=[("Entry / implied deal", "$58.61 / 약 $59.80", "2% spread", "계약조건 종결", "성공"), ("Consideration", "$26.50+1.4286 CTL", "수령", "2017-11-01 수령", "성공"), ("Combined EBITDA", "$10bn 예상", "$1bn synergy", "rerating 미실현", "부분"), ("FCF", "약 $2.80/share", "$3", "2019 $3.1~3.4bn guide", "headline 일부"), ("Dividend", "안전 주장", "유지", "2019 cut·2022 제거", "실패")],
        timeline=[("2017-07-29", "VIC merger/post-close Long", "$58.61"), ("2017-11-01", "거래 종결", "$26.50+1.4286 CTL"), ("2017-12-31", "former LVLT holders 약 49%", "CTL exposure 현실화"), ("2019-02", "2019 FCF $3.1~3.4bn guide", "현금력 일부"), ("2019-02", "annual dividend $1로 cut", "첫 hold 반증"), ("2022-11-02", "dividend elimination", "장기 thesis 실패")],
    ),
]

# V9 canonical claim map is fixed at six weighted claims per idea.  A few raw
# thesis decompositions above retain a seventh candidate so the exclusion is
# explicit instead of silently deleting the underlying research judgment.
_CLAIM_KEEP = {
    "2001-03-01": [0, 1, 2, 3, 4, 5],
    "2002-04-19": [1, 2, 3, 4, 5, 6],
    "2003-03-17": [0, 1, 2, 3, 5, 6],
    "2004-12-30": [0, 1, 2, 3, 4, 5],
    "2007-11-11": [0, 1, 2, 3, 4, 6],
    "2011-10-11": [0, 1, 2, 4, 5, 6],
    "2017-07-29": [0, 1, 2, 3, 4, 5],
}
for _idea in IDEAS:
    if _idea["date"] in _CLAIM_KEEP:
        _idea["claims"] = [_idea["claims"][n] for n in _CLAIM_KEEP[_idea["date"]]]


def idea_sources(i):
    raw = S("VIC original idea" if i["source"] else "VIC source-DB preserved original", i["source"],
            "Value Investors Club / source SQL", i["date"],
            "T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준.", "원문")
    return [raw, *LVLT_SOURCES]


def render_report(i):
    lines = [
        f"# Level 3 Communications (LVLT) — {i['date']} VIC {i['direction']}", "",
        "> **Idea unit:** 이 게시일·증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.",
        f"> **Research as-of:** {ASOF}. 원 SQL 방향은 Short로 보존하고 실제 원문 방향·증권은 research layer에서 교정했다.",
        "", "---", "", "## 0. Idea Snapshot", "", "| 항목 | 내용 |", "|---|---|",
        "| 회사 / Ticker | Level 3 Communications / LVLT |",
        f"| VIC 게시일 / 작성자 | {i['date']} / {i['author']} |",
        f"| 분석 증권 / 실제 방향 | {i['security']} |", "| 원 SQL 방향 | Short — raw 값 보존, 실제 원문은 매수 논지 |",
        f"| 기준 진입가격 | {i['entry']} |", f"| 기대기간 | {i['horizon']} |", f"| raw horizon audit | {i['raw_horizon']} |",
        f"| 최종 판정 | **{i['verdict']}** |", "", f"> **결론:** {i['conclusion']}", "", "---", "",
        "## 1. 회사는 정확히 무엇을 하는가", "", BUSINESS, "", ENGINE, "", "### 가치사슬과 security payoff", "",
        "고객 traffic와 계약매출이 access/network cost, SG&A, cash interest, capex, tax를 통과한 뒤 common에 남는다. Debt 아이디어는 enterprise value보다 담보·선순위·만기·refinancing source가 먼저다. Pair는 long bond와 short common, option hedge의 각 cash flow를 별도로 기록해야 한다.",
        "", "### 매 분기 볼 핵심 KPI", "", KPI, "", "---", "", "## 2. 당시 상황과 시장이 가격에 넣은 것", "", i["t0"], "", "### Reverse expectations", "", i["reverse"], "", "---", "", "## 3. 원문 투자논지 지도", "",
    ]
    for n, c in enumerate(i["claims"], 1):
        lines += [f"### C{n}. {c['title']} — {c['verdict']}", "", "**원문 주장**", "", c["original"], "",
                  "**경제적 메커니즘**", "", c["mechanism"], "", "**T0 근거**", "", c["evidence"], "",
                  "**숨은 가정**", "", c["assumption"], "", "**사전 반증조건**", "", c["falsifier"], "",
                  "**실제 결과**", "", c["actual"], "", "**정량 gap**", "", c["gap"], "",
                  "**분석 오류 또는 제한**", "", c["error"], "", "**재사용 교훈**", "", c["lesson"], ""]
    lines += ["---", "", "## 4. 당시 Valuation과 Payoff Structure", "", i["valuation"], "", "### 시나리오 분석", "",
              "| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |", "|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scenarios"]]
    lines += ["", "### 핵심 수치", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["metrics"]]
    lines += ["", "### 촉매와 시간", "", f"판정 horizon은 **{i['horizon']}**다. 이후 사건은 장기 가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.",
              "", "---", "", "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "", "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["timeline"]]
    lines += ["", "### 실제 사업·자본구조 추이", "", i["actual"], "", "---", "", "## 6. 실제 투자결과 — 가격 경로와 실현 가능성", "", i["price"], "",
              "가격 series가 없으면 수익률·MFE·MAE를 추정하지 않는다. Bond·pair는 exact issue, coupon, exchange, short borrow와 cash-flow date가 있어야 IRR을 계산한다.",
              "", "---", "", "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 핵심 gap |", "|---|---|---:|---|---|"]
    for n, (c, w) in enumerate(zip(i["claims"], WEIGHTS), 1):
        lines.append(f"| C{n} | {c['title']} | {w}% | {c['verdict']} | {c['gap']} |")
    lines += ["", "---", "", "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", i["drivers"], "",
              "### Counterfactual", "", i["counterfactual"], "", "---", "", "## 9. 분석 오류 유형과 최초 경고", "", i["error"], "",
              "### 최초로 관찰 가능했던 경고신호", "", i["warning"], "", "---", "", "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", ""]
    for n, lesson in enumerate(i["lessons"], 1):
        lines += [f"### Lesson {n}", "", lesson, ""]
    lines += ["### 지금 같은 아이디어를 다시 본다면", ""] + [f"- {x}" for x in i["checklist"]]
    lines += ["", "---", "", "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scorecard"]]
    lines += [f"| Thesis score | {i['score']:.1f}/10 |", f"| Process score | {i['process']:.1f}/10 |", f"| 종합 | **{i['verdict']}** |",
              "", "### 한 문장 교훈", "", f"> {i['lessons'][0]}", "", "---", "", "## 12. Sources / Validation Notes", ""]
    for n, source in enumerate(idea_sources(i), 1):
        if source["url"]:
            lines.append(f"{n}. [{source['title']}]({source['url']}) — {source['publisher']}, {source['date']}. {source['evidence']}")
        else:
            lines.append(f"{n}. {source['title']} — {source['publisher']}, {source['date']}. {source['evidence']}")
    lines += ["", "### 데이터 품질", "",
              "- T0 원문·metadata: **A/B** — source SQL과 공개 VIC URL을 기준으로 했다. 공개 URL이 없는 글도 source DB 본문은 보존돼 있다.",
              "- 사업·거래·자본구조: **A** — SEC·회사 1차자료를 우선했다.",
              "- 가격·수익률: **C 또는 미검증** — 원 DB에 performance row가 없어 원문 회고·공시가격만 제한적으로 썼다.",
              "- raw SQL direction은 **Short**, 실제 research direction은 위 snapshot의 매수·pair 방향이다. raw 값을 덮어쓰지 않았다.", ""]
    return "\n".join(lines)


def make_payload(ideas):
    out = {"schema_version": "vic-deep-research-v9", "batch": 43,
           "title": "Level 3 / Nexstar — Security Selection and Timing V9", "research_asof": ASOF,
           **{k: [] for k in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")}}
    for i in ideas:
        desc_chars, catalyst_chars = RAW[i["id"]]
        out["ideas_master"].append({
            "idea_id": i["id"], "date": i["date"], "year": int(i["date"][:4]), "ticker": "LVLT", "company_name": "Level 3 Communications",
            "author": i["author"], "is_short": 1, "direction_ko": "숏", "idea_type_ko": "기업가치/증권분석", "source_link": i["source"] or None,
            "description_chars": desc_chars, "catalyst_chars": catalyst_chars, "contest_winner": 0,
            "auto_tag_status_ko": "raw 방향 보존·본문 증권/방향 수동검증 완료",
            "narrative_tags_ko": "fiber; telecom; leverage; security selection; capital structure; merger",
            "horizon_raw": i["raw_horizon"], "horizon_months": None, "performance_available": 0,
            "perf_1m": None, "perf_3m": None, "perf_6m": None, "perf_1y": None, "perf_2y": None, "perf_3y": None, "perf_5y": None,
            "idea_return_1y": None, "idea_return_3y": None, "idea_return_5y": None})
        out["postmortems"].append({
            "idea_id": i["id"], "ticker": "LVLT", "research_direction_ko": i["direction"], "company_description_ko": BUSINESS,
            "original_thesis_ko": i["t0"], "actual_development_ko": i["actual"], "thesis_verdict_ko": i["conclusion"],
            "business_verdict_ko": i["scorecard"][0][1], "catalyst_verdict_ko": i["scorecard"][2][1], "valuation_verdict_ko": i["scorecard"][1][1],
            "stock_verdict_ko": i["price"], "current_verdict_ko": i["verdict"], "overall_verdict_ko": i["verdict"], "why_ko": i["drivers"],
            "success_pattern_ko": "security_mapping; capital_structure; primary_source_validation; catalyst_calendar",
            "failure_pattern_ko": "replacement_cost; duration; leverage; gross_net_confusion; integration",
            "root_error_ko": i["error"], "first_signal_ko": i["warning"], "first_signal_date": i["first_signal_date"],
            "knowable_at_t0_ko": i["claims"][0]["evidence"] + " " + i["claims"][0]["falsifier"],
            "avoidability_ko": "중간 이상. T0 자료로 debt waterfall·cash runway·security payoff를 분리할 수 있었다.",
            "counterfactual_question_ko": i["counterfactual"], "analyst_note_ko": f"raw SQL Short 보존; 실제 방향 {i['direction']}. {i['raw_horizon']}",
            "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None,
            "confidence": 0.95, "research_asof": ASOF, "research_status_ko": "1차자료 검증 완료·가격성과 제한 명시"})
        out["meta"].append({
            "idea_id": i["id"], "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·가격·event calendar·first break·security payoff 장문분석",
            "report_version": "V9-canonical", "thesis_type_ko": i["title"], "one_line_verdict_ko": i["conclusion"],
            "thesis_score": i["score"], "process_score": i["process"], "return_summary_ko": i["price"],
            "core_error_ko": i["error"], "core_insight_ko": i["lessons"][0], "research_asof": ASOF})
        section_rows = [
            ("회사·가치사슬·현금엔진", f"{BUSINESS}\n\n{ENGINE}\n\n핵심 KPI: {KPI}."),
            ("T0 시장기대·reverse expectations", f"{i['t0']}\n\n{i['reverse']}"),
            ("Valuation·payoff·실제경로", f"{i['valuation']}\n\n실제: {i['actual']}\n\n가격: {i['price']}"),
            ("사후인과·오류·교훈", f"{i['drivers']}\n\n오류: {i['error']}\n\nCounterfactual: {i['counterfactual']}"),
        ]
        for n, (title, body) in enumerate(section_rows, 1):
            out["sections"].append({"idea_id": i["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, (c, w) in enumerate(zip(i["claims"], WEIGHTS), 1):
            out["claims"].append({"idea_id": i["id"], "claim_order": n, "claim_title_ko": c["title"], "thesis_weight_pct": w,
                                  "original_claim_ko": c["original"], "t0_evidence_ko": c["evidence"], "key_assumption_ko": c["assumption"],
                                  "ex_ante_falsifier_ko": c["falsifier"], "actual_result_ko": c["actual"], "quantitative_gap_ko": c["gap"],
                                  "verdict_ko": c["verdict"], "analytical_error_ko": c["error"], "reusable_lesson_ko": c["lesson"]})
        for n, row in enumerate(i["metrics"], 1):
            out["metrics"].append({"idea_id": i["id"], "metric_order": n, "metric_name_ko": row[0], "t0_value_ko": row[1],
                                   "thesis_expectation_ko": row[2], "actual_value_ko": row[3], "verdict_ko": row[4],
                                   "interpretation_ko": f"{row[0]}의 T0 기대와 실제를 동일 단위가 가능한 범위에서 비교했다."})
        for n, row in enumerate(i["timeline"], 1):
            out["timeline"].append({"idea_id": i["id"], "event_order": n, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for n, source in enumerate(idea_sources(i), 1):
            out["sources"].append({"idea_id": i["id"], "source_order": n, "source_type_ko": source["type"], "publisher": source["publisher"],
                                   "title_ko": source["title"], "source_date": source["date"], "url": source["url"], "evidence_ko": source["evidence"]})

    nxst_payload = json.loads((ROOT / "data/curated/batch_039_nexstar_sinclair_deep_v7.json").read_text(encoding="utf-8"))
    for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources"):
        by_id = {iid: [row for row in nxst_payload[key] if row["idea_id"] == iid] for iid in NXST_IDS}
        for iid in NXST_IDS:
            out[key].extend(by_id[iid])
    # Batch 039's narrative correctly audits these two source rows as raw Short,
    # but its ideas_master layer stored the research direction.  Preserve the
    # source flag here while leaving postmortem.research_direction_ko as Long.
    for row in out["ideas_master"]:
        if row["idea_id"] in NXST_IDS:
            row["is_short"] = 1
            row["direction_ko"] = "숏"
            row["auto_tag_status_ko"] = "raw 방향 보존·본문 Long 수동검증 완료"
    return out


def render_index(ideas):
    rows = []
    for n, i in enumerate(ideas, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(f"| {n} | {i['date']} | LVLT | Short | {i['direction']} | [{i['date']} LVLT]({rel}) | {i['verdict']} |")
    rows += [
        "| 9 | 2005-12-20 | NXST | Short | Long | [2005-12-20 NXST](ideas/2005/2005-12-20_NXST_long.md) | 사업논지 성공·가격성과 미검증 |",
        "| 10 | 2011-12-14 | NXST | Short | Long | [2011-12-14 NXST](ideas/2011/2011-12-14_NXST_long.md) | 강한 성공·촉매 경로 변경 |",
    ]
    lines = [
        "# Batch 043 — Level 3 / Nexstar V9 Index", "",
        "> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. raw 방향, 실제 증권, 회사 생존, 해당 security payoff를 분리했다.", "",
        "## Canonical idea files", "", "| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |", "|---:|---|---|---|---|---|---|", *rows,
        "", "## Direction / security audit", "",
        "10건 모두 raw SQL은 Short지만 원문은 모두 매수 논지다. LVLT 2000·2001·2007·2011은 common Long, 2002는 복수 채권 Long, 2003은 senior secured bank debt Long, 2004는 convert Long/common Short pair, 2017은 merger Long과 post-close CTL hold다. NXST 두 건은 common Long이다.",
        "", "## 핵심 판정", "",
        "1. **LVLT 2000·2001 common:** fiber/IP 자산은 생존했지만 -70% 및 $81→약 $5 회고가 near-term Long을 강하게 반증했다. replacement cost는 common floor가 아니었다.",
        "2. **LVLT 2002 bonds:** 회사가 파산을 피하고 여러 2008·2010 채무를 지급해 broad credit thesis는 성공했다. 원문이 단일 CUSIP을 고정하지 않아 exact 25~35% IRR은 미검증이다.",
        "3. **LVLT 2003 bank debt:** 83에 산 $1.125bn senior secured facility는 2003년 전액상환돼 가장 깨끗한 성공 사례다.",
        "4. **LVLT 2004 convert/common pair:** bond survival과 dilution은 적중했지만 tender·exchange·borrow ledger가 없어 exact pair IRR은 만들지 않았다.",
        "5. **LVLT 2007 common:** 2011 EBITDA $958m은 $2.2bn forecast보다 약 56% 낮았고 2~3년 $9 target은 실패했다.",
        "6. **LVLT 2011 common:** 2013 FCF $900m 기대 대비 실제 약 -$47m으로 timing은 실패했다. 2014~16 FCF와 2017 매각은 delayed thesis success다.",
        "7. **LVLT 2017 merger:** 계약대가 수령은 성공했으나 post-close $75~90·dividend safety는 2019 cut과 2022 elimination으로 실패했다.",
        "8. **NXST 2005·2011:** Batch 039 V9 정본을 그대로 재사용했다. 2005는 사업논지 성공·가격성과 미검증, 2011은 retransmission·M&A·deleveraging이 강하게 적중했다.",
        "", "## 공통 분석식", "",
        "`CNS revenue - access/network cost - SG&A - cash interest - capex - tax = common equity FCF`", "",
        "Debt는 `enterprise recovery × seniority + coupon + tender/exchange consideration - purchase price`로 계산한다. Pair는 bond·short·option·borrow의 날짜별 cash flow를 합산한다.",
        "", "## 상위 교훈", "",
        "1. traffic·TAM·replacement cost보다 price-cost spread와 debt waterfall이 먼저다.",
        "2. distress에서 좋은 company call보다 좋은 security selection이 더 높은 확률의 수익을 만든다.",
        "3. EBITDA, FCF, dividend capacity는 같은 숫자가 아니다.",
        "4. merger arb와 post-close long은 별도의 position·horizon·falsifier를 가져야 한다.",
        "5. 정확한 CUSIP·borrow·cash-flow dates가 없으면 exact IRR을 만들지 않는다.",
        "", "## 중복·정본 처리", "",
        "- LVLT 2000·2001은 Batch 035의 짧은 구판을 이번 개별 V9 정본으로 승격했다.",
        "- NXST 2005·2011은 Batch 039에 이미 완성된 V9 canonical 파일과 overlay row를 재사용해 내용 충돌을 막았다.",
        "", "## 앱/DB 반영", "",
        "- `analysis/batch_043_level3_nexstar_10.md`는 10개 canonical 파일을 불러오는 wrapper다.",
        "- `data/curated/batch_043_level3_nexstar_deep_v7.json`은 V9 상세 overlay다.", "",
    ]
    return "\n".join(lines)


def main():
    if len(IDEAS) != 8 or len({i["id"] for i in IDEAS}) != 8:
        raise ValueError("Batch 043 must contain eight unique LVLT ideas plus two reused NXST ideas")
    for i in IDEAS:
        if len(i["claims"]) != 6 or sum(WEIGHTS) != 100:
            raise ValueError(f"{i['id']}: six weighted claims required")
        path = ROOT / i["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_report(i), encoding="utf-8")
    (ROOT / "analysis/batch_043_v9_index.md").write_text(render_index(IDEAS), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS] + [
        "ideas/2005/2005-12-20_NXST_long.md", "ideas/2011/2011-12-14_NXST_long.md"]
    wrapper = "# Batch 043 — Level 3 / Nexstar V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + \
              "> Streamlit 호환 wrapper다. canonical index: [Batch 043 V9 Index](batch_043_v9_index.md).\n"
    (ROOT / "analysis/batch_043_level3_nexstar_10.md").write_text(wrapper, encoding="utf-8")
    payload = make_payload(IDEAS)
    output = ROOT / "data/curated/batch_043_level3_nexstar_deep_v7.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports=10 claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
