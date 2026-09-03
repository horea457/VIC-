#!/usr/bin/env python3
"""Build Batch 012: Apollo, KKR and Blackstone alternative-manager ideas."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASOF = "2024-01-31"
ANALYSIS_DATE = "2026-09-03"

DESCRIPTIONS = {
    "APO": (
        "Apollo Global Management은 사모펀드 하나가 아니라 자산운용(Asset Management)과 Athene 중심의 퇴직연금·보험(Retirement Services)을 결합한 대체자산 플랫폼이다. "
        "운용부문은 yield·hybrid·equity 전략에서 관리보수와 성과보수(carry)를 받고, Athene은 연금보험료와 재보험 부채를 장기 자금원으로 조달해 Apollo가 발굴한 투자등급 사모신용·asset-backed 자산 등에 투자한 스프레드를 번다. "
        "따라서 돈 버는 구조는 ① fee-paying AUM×보수율에서 비용을 뺀 FRE, ② 보험자산 수익률에서 계약자 원가·헤지·운영비를 뺀 SRE, ③ 펀드 성과에서 발생하는 carry, ④ 대차대조표 투자수익이다. "
        "Athene은 환매가 거의 없는 영구자본과 대규모 origination 수요를 주지만, 상장주주가 단순 asset-light 운용사만 소유하는 것이 아니라 금리·신용·ALM·규제·보험자본 위험도 함께 부담한다. "
        "핵심 지표는 총 AUM보다 fee-generating AUM, FRE margin, 순유입, origination, Athene spread·RBC와 신용손실, 주당 ANI 및 실제 자사주 상쇄다."
    ),
    "KKR": (
        "KKR은 private equity에서 출발해 credit·real assets·infrastructure·capital markets·보험으로 확장한 글로벌 대체자산 운용사다. "
        "Asset Management는 장기·폐쇄형 또는 영구자본에 관리보수를 부과하고 성과가 hurdle을 넘으면 carry를 받는다. Capital Markets는 인수금융·신디케이션·자문에서 거래수수료를 벌며, 자체 대차대조표는 펀드와 공동투자하고 신규 전략을 seed한다. "
        "2021년 편입한 Global Atlantic은 연금·생명보험 부채를 장기 투자자금으로 제공해 보험 spread earnings와 영구자본 AUM을 더했다. "
        "경제성은 AUM 그 자체보다 FPAUM, 미투자 약정의 fee 전환, FRE margin, 실현 carry, balance-sheet NAV, 보험자산의 신용·duration 관리와 주당 희석에 달려 있다. "
        "좋은 운용성과도 투자자가 높은 가격을 내거나 carry를 영구 반복수익으로 보거나 보험·연결회계 위험을 무시하면 낮은 주주수익으로 이어질 수 있다."
    ),
    "BX": (
        "Blackstone은 부동산·private equity·credit & insurance·infrastructure·secondaries·hedge-fund solutions를 운용하는 글로벌 대체자산 플랫폼이다. "
        "관리보수는 장기 약정 또는 영구자본에 반복적으로 붙고, 투자성과가 기준을 넘으면 incentive fee와 carried interest가 발생한다. 운용자산 대부분은 고객자본이어서 전통 은행처럼 전액을 자체 조달하지 않지만, GP commitment·seed·보험 및 리테일 상품에는 시장·유동성 위험이 남는다. "
        "Blackstone의 핵심 flywheel은 우수한 실현성과→LP 재약정→더 큰 flagship·인접전략→보수·carry 증가이며, 개인자산가·보험 채널이 자금원을 넓힌다. "
        "핵심 지표는 fee-earning AUM, FRE·DE, 실현가능 carry, 펀드수익률, 영구자본 비중, 순유입과 분배다. 특히 ENI에는 미실현 평가이익이 섞이므로 배당·현금전환과 분리해야 한다."
    ),
}

SOURCES = {
    "APO": [
        ("공시", "Apollo 2023 Form 10-K", "SEC", "2024-02-27", "https://www.sec.gov/Archives/edgar/data/1858681/000185868124000031/apo-20231231.htm", "2023 AUM·FRE·SRE와 Athene 위험 검증"),
        ("기업발표", "Apollo Reports Fourth Quarter and Full Year 2023 Results", "Apollo", "2024-02-08", "https://ir.apollo.com/news-events/press-releases/detail/486/apollo-reports-fourth-quarter-and-full-year-2023-results", "AUM $651bn·유입·수익성 확인"),
        ("기업발표", "Apollo and Athene Announce Transaction Close", "Apollo", "2022-01-03", "https://ir.apollo.com/news-events/press-releases/detail/28/apollo-and-athene-announce-transaction-close", "전액주식 합병 실행 확인"),
        ("공시", "Apollo 2020 Form 10-K", "SEC", "2021-02-25", "https://www.sec.gov/Archives/edgar/data/1411494/000141149421000013/apo-20201231.htm", "합병 전 AUM·FRE·Athene 지분 구조"),
        ("가격", "Apollo historical prices", "Digrin", ASOF, "https://www.digrin.com/stocks/detail/APO/price", "월말 실가격 경로 교차검증"),
    ],
    "KKR": [
        ("공시", "KKR 2023 Form 10-K", "SEC", "2024-02-26", "https://www.sec.gov/Archives/edgar/data/1404912/000140491224000005/kkr-20231231.htm", "사업·보험·자본구조 검증"),
        ("기업발표", "KKR Fourth Quarter 2023 Financial Results", "KKR/SEC", "2024-02-06", "https://www.sec.gov/Archives/edgar/data/1404912/000140491224000002/q423earningsrelease_vf.htm", "AUM $553bn·FPAUM $446bn·FRE $2.4bn 확인"),
        ("기업발표", "KKR Completes Acquisition of Global Atlantic", "KKR", "2021-02-01", "https://ir.kkr.com/news-releases/news-release-details/kkr-completes-acquisition-global-atlantic", "보험 플랫폼·약 $90bn AUM 편입 확인"),
        ("기업발표", "KKR Acquires Remaining Stake in Global Atlantic", "KKR", "2024-01-02", "https://ir.kkr.com/news-releases/news-release-details/kkr-completes-acquisition-remaining-37-global-atlantic", "Global Atlantic 100% 소유 전환 확인"),
        ("가격", "KKR historical prices", "Digrin", ASOF, "https://www.digrin.com/stocks/detail/KKR/price", "월말 실가격 경로 교차검증"),
    ],
    "BX": [
        ("공시", "Blackstone 2023 Form 10-K", "SEC", "2024-02-23", "https://www.sec.gov/Archives/edgar/data/1393818/000139381824000010/bx-20231231.htm", "사업부·AUM·FRE·DE 검증"),
        ("기업발표", "Blackstone Fourth Quarter and Full Year 2023 Results", "Blackstone", "2024-01-25", "https://www.blackstone.com/news/press/blackstone-reports-fourth-quarter-and-full-year-2023-earnings-results/", "$1tn+ AUM과 사업구조 확인"),
        ("공시", "Blackstone 2014 Form 10-K", "SEC", "2015-02-27", "https://www.sec.gov/Archives/edgar/data/1393818/000119312515064920/d856336d10k.htm", "글 이후 AUM·ENI·분배 검증"),
        ("공시", "Blackstone 2013 Form 10-K", "SEC", "2014-02-28", "https://www.sec.gov/Archives/edgar/data/1393818/000119312514073756/d640229d10k.htm", "글 당시 사업·성과보수 구조"),
        ("가격", "Blackstone historical prices", "Digrin", ASOF, "https://www.digrin.com/stocks/detail/BX/price", "월말 실가격·배당조정가격 교차검증"),
    ],
}


def C(name, claim, condition, falsifier, actual, verdict):
    return (name, claim, condition, falsifier, actual, verdict)


IDEAS = [
    dict(id="617e3e9e-12f4-4948-8f16-babdf449f654", date="2014-06-22", ticker="APO", company="Apollo", author="rosco37", source_short=1, link="https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MANAGEMENT_LLC/6264557856", dchars=12634, cchars=128,
         title="가치투자형 대체운용사와 Athene 영구자본 롱", price="$27대", verdict="매우 성공", score=8.6, process=8.3,
         thesis="AUM $158bn 중 credit $101bn·PE $48bn·real estate $9bn인 Apollo를 ‘레버리지 바이아웃 한 종류’가 아니라 가치·distressed 철학의 다전략 운용사로 봤다. PE의 역사적 gross/net IRR 39%/26%, Athene의 약 $49bn 영구자본, sole-sponsored deal 역량이 장기 AUM·분배를 키운다고 주장했다. 보수적 펀드수익률(PE 15%·credit 6%·real estate 4%)에서도 연평균 incentive income $911m, management income $171m과 순투자자산 $5.62/주를 합산해 가격이 싸다고 봤다.",
         actual="Apollo는 2023년 말 AUM $651bn으로 당시의 네 배 이상이 됐고 Athene은 단순 제휴가 아니라 2022년 완전 합병돼 영구자본·origination 엔진이 됐다. 2024-01 월말 주가 $100.40은 2014년 6월 $27대 대비 약 3.6배이며 중간 분배금도 있었다. 다만 변동 배당과 carry에 의존한 원 계산보다 실제 성공은 보험·private credit 확대와 기업구조 단순화에서 더 크게 왔다.",
         why="저평가된 관리보수·carry와 Athene의 전략가치를 함께 본 핵심 인과가 맞았다. 다만 Athene을 단순 asset-light AUM으로 본 시각은 합병 후 보험 대차대조표 위험을 충분히 반영하지 못했다.", first="Athene AUM 성장과 신규 credit 자금유입", first_date="2015-02-27", stock="$27대→$100.40; 가격만 약 +260%대, 분배 제외", valuation="순투자자산 $5.62/주+정상 incentive/management income SOTP",
         claims=[C("운용성과", "value/distressed 규율과 강한 PE track record가 재모금을 만든다.", "후속 빈티지가 벤치마크를 이기고 LP가 재약정", "두 빈티기 연속 저성과·fund size 축소", "AUM과 flagship 규모가 장기 확대됐다.", "적중"), C("Athene 영구자본", "$49bn Athene 자산이 안정적 credit fee base다.", "보험부채가 안정적이고 origination 수익이 자본비용을 상회", "해약·신용손실·자본부족으로 외부자본 필요", "Athene은 완전 합병돼 SRE와 대규모 영구자본을 제공했다.", "적중"), C("분배 경제성", "보수적 수익률에서도 관리보수와 carry가 큰 현금분배를 만든다.", "carry 실현과 FRE가 cycle 전체에서 현금화", "평가이익은 늘지만 실현·분배가 장기 부진", "분배는 변동했으나 이익·주가는 크게 증가했다.", "부분~적중"), C("싼 청구권", "전통운용사보다 빠른 성장·높은 margin인데 낮은 배수다.", "AUM 증가가 주당 FRE/DE로 전환", "보상·희석이 성장 대부분 흡수", "주당가치와 가격이 크게 상승했다.", "적중")],
         metrics=[("AUM", "$158bn", "장기 성장", "$651bn FY2023", "적중"), ("Athene AUM", "약 $49bn", "영구자본 확대", "합병 후 핵심 SRE 엔진", "적중"), ("가격", "$27대", "재평가+분배", "$100.40", "매우 성공"), ("구조", "LP·변동분배", "인지도 개선", "C-corp·Athene 완전합병", "초과")]),

    dict(id="5208c892-2941-475f-ab2a-0acb87a923c2", date="2017-08-15", ticker="APO", company="Apollo", author="humkae848", source_short=0, link="https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MANAGEMENT_LLC/2870139803", dchars=9842, cchars=211,
         title="Fund IX FRE step-up와 $42 SOTP 롱", price="$29.5", verdict="매우 성공", score=9.0, process=8.8,
         thesis="AUM $230bn+, fee-generating AUM $160bn+인 Apollo를 FRE·carry·순투자자산의 세 청구권으로 나눴다. 2018 after-tax FRE $1.50/주에 17배를 적용한 $25.50, cycle-average carry $2.28/주에 6배를 적용한 $13.70, 순자산 $2.78을 합쳐 목표 $42를 계산했다. Fund IX가 연 $200m management fee를 추가하고 incremental margin 80%를 낼 것과 Athene·AGER가 영구 fee base를 확대할 것을 촉매로 봤다.",
         actual="목표 $42는 2020년에 넘어섰고 2024-01 월말 $100.40으로 진입가 대비 약 +240%였다. Apollo AUM은 $651bn까지 늘고 Athene 합병으로 영구자본 논지가 강화됐다. 다만 ‘Fund IX 한 건의 고증분 margin’보다 보험·private credit 확대와 구조개편이 장기 rerating의 더 큰 원인이었다.",
         why="FRE·carry·balance sheet를 분리한 SOTP와 fee 전환 스케줄이 좋았다. Athene concentration과 계약해지 위험을 명시한 점도 강점이다. 실제 보험 위험을 단순 fee asset보다 더 깊게 stress했으면 완성도가 높았다.", first="Fund IX investment period 진입과 fee step-up", first_date="2018-02-01", stock="$29.53 월말 근사→$100.40; 가격 약 +240%, 분배 제외", valuation="$25.50 FRE+$13.70 carry+$2.78 순자산=$42",
         claims=[C("Fund IX FRE", "신규 flagship이 연 $200m fee와 80% incremental margin을 더한다.", "약정자금이 fee-paying period에 진입", "활성화 지연·fee offset·비용이 증가분 흡수", "FRE 규모는 장기 크게 확대됐다.", "적중"), C("Athene/AGER", "보험·재보험 자금이 장기 fee-generating AUM을 만든다.", "안정적 liabilities와 적정 spread", "보험자본 훼손·mandate 해지", "Athene 완전합병과 보험 AUM 확대가 현실화됐다.", "적중"), C("carry 정상화", "cycle carry $2.28/주에 6배만 줘도 $13.70 가치다.", "성과와 realization이 cycle 내 현금화", "공모시장 폐쇄로 수년간 실현 부재", "carry는 변동했지만 core valuation에 더해졌다.", "부분~적중"), C("SOTP 하방", "FRE만으로 가격 대부분을 방어하고 나머지는 낮게 산다.", "보수·비용·희석 후 주당 FRE 증가", "보상비와 주식증가가 FRE 성장 상쇄", "목표가와 장기 가격 모두 달성했다.", "적중")],
         metrics=[("목표가", "$42", "중기 달성", "$100.40 종착", "성공"), ("FGAUM", "$160bn+", "Fund IX 증가", "총 AUM $651bn", "적중"), ("Fund IX fee", "$200m/년", "80% 증분마진", "FRE 대폭 확대", "방향 적중"), ("가격", "$29.53", "+42%", "$100.40", "매우 성공")]),

    dict(id="c3f0c2de-8880-4fbd-b2c3-aebe721dcf80", date="2020-06-10", ticker="APO", company="Apollo", author="CataBrit", source_short=1, link=None, dchars=35714, cchars=13,
         title="look-through 10.7배와 Athene 옵션 롱", price="$50", verdict="성공", score=8.8, process=8.7,
         thesis="headline core P/E 약 26배가 아니라 FRE·carry·Athene을 분리하면 현재 look-through 10.7배, 5년 후 5.3배라고 주장했다. 2020 post-tax FRE $1.96/주가 5년 후 $3.94가 되고 25배를 받으면 $98.56, 누적배당 약 $14로 FRE만 연 18% 수익을 제시했다. carry 약 $2/주에 6배, Athene 35% 지분을 1배 장부가 약 $14/주로 더해 현재 SOTP $78, 5년 intrinsic $150을 계산했다.",
         actual="2020년 말 AUM은 $455.5bn이었고 2023년 말 $651bn으로 증가했다. Athene 합병은 지분 discount를 없애고 보험수익을 직접 귀속시켰으며 $78 목표는 2023년에, $100.40은 2024-01에 도달했다. 다만 2024 기준에서는 $150·5년 가설을 아직 판정할 수 없고, 합병 후 보험자본을 25배 FRE와 단순 합산하는 위험은 더 커졌다.",
         why="코어 보수이익·carry·Athene을 분해해 이중계산을 줄이고 C-corp/합병 촉매를 포착했다. 다만 25배 FRE, AUM 두 배, Athene 장부가 복리라는 세 낙관가정을 동시에 적용해 장기 목표의 가시성은 원문보다 낮다.", first="Athene 합병 발표로 지분·governance discount 축소", first_date="2021-03-08", stock="$49.92 월말 근사→$100.40; 가격 약 +101%, 배당 제외", valuation="현재 $78 SOTP; 5년 FRE $98.56+배당+carry+Athene으로 $150",
         claims=[C("FRE 복리", "post-tax FRE가 $1.96에서 5년 $3.94로 두 배가 된다.", "FPAUM 성장과 margin·주당수 방어", "FRE/주 CAGR이 한 자릿수로 하락", "AUM·FRE가 증가했으나 5년치는 기준일 미도래다.", "부분~적중"), C("Athene 가치", "35% 지분만 $14/주 이상이며 장부가가 복리한다.", "보험 spread·자본이 안정", "신용손실·ALM 문제로 장부가 훼손", "완전합병으로 전략가치는 입증됐다.", "적중"), C("구조 촉매", "C-corp·지수편입·보험거래가 discount를 줄인다.", "구조 단순화가 투자자층 확대", "합병이 오히려 conglomerate discount 확대", "합병과 단순화 뒤 가격이 재평가됐다.", "적중"), C("$150 장기값", "FRE 25배와 Athene 복리로 5년 $150이다.", "여러 성장가정이 동시에 실현", "배수 정상화 또는 보험자본비용 상승", "2024-01에는 $100.40; 아직 미판정 구간이 남는다.", "미판정~부분")],
         metrics=[("AUM", "$455.5bn FY2020", "5년 두 배", "$651bn FY2023", "진행"), ("현재 목표", "$78", "+53%", "2023년 달성", "성공"), ("5년 목표", "$150", "약 30% IRR", "$100.40 기준일", "미판정"), ("Athene", "35% 지분", "1x book 이상", "100% 합병", "적중")]),

    dict(id="2d87c9b2-10ed-4734-88a2-ef109c7549c3", date="2021-11-29", ticker="APO", company="Apollo", author="afgtt2008", source_short=1, link="https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MGMT_INC/3123156096", dchars=19636, cchars=163,
         title="Athene 합병 복잡성 할인과 $100+ 롱", price="$70.8", verdict="성공", score=9.1, process=9.0,
         thesis="Apollo $300bn+ AUM과 Athene $150bn+를 합치는 전액주식 거래가 2022년 1월 닫히면 복잡한 이중지배구조가 사라진다고 봤다. 경영진의 5년 normalized earnings 성장 약 13%와 누적 distributable FCF $15bn을 인용했고, pro forma recurring FRE를 $2.40/주로 계산했다. 1년 forward earnings $6에 KKR의 17배를 적용해 $100+ 목표, 배당·재투자 포함 약 20% 연수익을 주장했다.",
         actual="합병은 2022-01-01 완료돼 핵심 이벤트가 정확히 실현됐다. Apollo는 2023년에 FRE와 SRE 합산 성장 25% 이상, AUM $651bn을 기록했고 주가는 2024-01 $100.40으로 원 목표에 도달했다. 다만 고정배당 $1.60은 높은 payout보다 재투자형 모델로의 전환이었고, 2022년 금리·신용 우려 중 큰 drawdown을 감수해야 했다.",
         why="거래 종결, one-share-one-vote, earnings 결합과 상대배수 rerating을 구체적 일정에 연결했다. merger가 단순 multiple 이벤트가 아니라 보험 위험의 완전 인수라는 점을 stress했어야 하지만 2024 기준 투자결론은 성공이다.", first="Apollo-Athene 합병 완료", first_date="2022-01-01", stock="$70.78 월말→$100.40; 가격 약 +42%, 배당 제외", valuation="forward earnings $6×17=$102+; 약 40% upside",
         claims=[C("합병 종결", "2022년 1월 합병과 dual-share collapse가 discount를 없앤다.", "규제승인·주주승인·운영통합", "종결 지연 또는 교환비율 재협상", "예정대로 2022-01-01 완료됐다.", "정확히 적중"), C("13% earnings", "normalized earnings가 5년 약 13% 성장한다.", "FRE·SRE 동시 성장과 신용손실 억제", "보험손실로 SRE 감소", "2023년 관련이익 성장 25%+로 초기 경로는 강했다.", "적중"), C("$15bn FCF", "5년 누적 distributable FCF가 equity 가치로 귀속된다.", "재투자와 buyback의 높은 수익률", "보험 자본투입·SBC가 현금 대부분 흡수", "2024 기준 전체 5년은 미도래다.", "미판정"), C("rerating", "$6 EPS에 KKR 17배로 $100+가 합리적이다.", "구조 단순화 후 peer multiple 접근", "보험 conglomerate discount 지속", "$100.40으로 기준일까지 목표 달성했다.", "적중")],
         metrics=[("AUM", "$300bn+ APO", "Athene 결합", "$651bn FY2023", "적중"), ("합병", "예정", "2022-01", "2022-01-01 완료", "적중"), ("목표가", "$100+", "1년 forward", "$100.40 기준일", "성공"), ("가격", "$70.78", "약 +40%", "$100.40", "성공")]),

    dict(id="72feccd5-c42a-41f3-b59d-25443952bd91", date="2022-09-10", ticker="APO", company="Apollo", author="Jumpman23", source_short=1, link="https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MGMT_INC/4366592262", dchars=10624, cchars=15,
         title="FRE 20배·SRE 10배의 post-merger 롱", price="$46.5", verdict="매우 성공", score=9.2, process=9.1,
         thesis="합병 뒤 asset-light 운용사와 보험사가 섞여 회계가 복잡해지고 금리·credit 우려가 커진 때 약 10배 2022 EPS $5.50에 거래된다고 봤다. 시장이 SRE에 5~6배만 주고 있다고 역산했으며, 경영진 2026 EPS $9+만 달성해도 현 multiple에서 5년 12%+ IRR, FRE 20배와 SRE 10배를 적용하면 약 20% IRR이라고 주장했다. 3% 배당과 초과자본·buyback을 하방으로 제시했다.",
         actual="진입 시점의 공포 뒤 Apollo는 2023년 AUM $651bn, FRE+SRE 성장 25%+를 기록했고 주가는 $46.50에서 $100.40으로 약 116% 상승했다. 보험 spread와 origination 결합은 작동했다. 다만 기준일은 2026 목표 전이므로 $9 EPS와 5년 IRR 자체는 아직 완결 판정할 수 없다.",
         why="복잡한 결합회사를 FRE와 SRE로 분리하고 보험이익에 더 낮은 배수를 준 점이 뛰어났다. 낮은 진입가격이 forecast 오차를 흡수했다. 초과자본이 무조건 buyback으로 귀속된다는 가정은 별도 검증이 필요하다.", first="2023년 FRE·SRE 동시 성장과 대규모 유입", first_date="2024-02-08", stock="$46.50 월말 근사→$100.40; 가격 약 +116%, 배당 제외", valuation="2026 EPS $9+; FRE 20x+SRE 10x에서 약 20% 5년 IRR",
         claims=[C("FRE 성장", "FRE가 장기 두 자릿수로 성장한다.", "FPAUM·capital solutions 확대와 비용규율", "순유입 둔화·margin 압박", "2023 FRE가 강하게 성장했다.", "적중"), C("SRE 정상화", "Athene spread earnings에 5~6배는 과도한 할인이다.", "credit/ALM 손실 없이 spread 유지", "대규모 impairments·RBC 압박", "초기 실적은 강했고 multiple도 상승했다.", "적중"), C("2026 EPS", "$9+ EPS 목표가 달성 가능하다.", "origination·보험유입·운용보수 동반성장", "두 부문 중 하나가 구조적으로 정체", "기준일 현재 목표연도 미도래다.", "진행"), C("낮은 가격", "10배 안팎 EPS와 3% 배당이 forecast risk를 보상한다.", "earnings 하방 제한·자본건전성", "신용손실로 book와 earnings 동시훼손", "가격이 두 배 이상 상승했다.", "적중")],
         metrics=[("2022 EPS", "$5.50E", "지속", "2023 ANI 성장", "적중"), ("2026 EPS", "$9+", "달성", "목표연도 미도래", "진행"), ("SRE 배수", "5~6x implied", "10x 재평가", "주가 rerating", "방향 적중"), ("가격", "$46.50", "12~20% IRR", "$100.40", "매우 성공")]),

    dict(id="96258fc0-17cf-4db9-9219-986f839a2beb", date="2015-01-27", ticker="KKR", company="KKR", author="trev62", source_short=0, link="https://www.valueinvestorsclub.com/idea/KKR_and_CO_LP/3593801772", dchars=23681, cchars=75,
         title="대차대조표+반복보수 하방과 carry 무료옵션 롱", price="$24", verdict="매우 성공", score=8.8, process=8.6,
         thesis="$96bn AUM의 KKR을 balance-sheet investments, 반복 fee earnings, carry의 세 부분으로 봤다. 자체 투자자산과 안정적 관리보수만으로 가격 대부분이 설명되고, 높은 장기성과·locked capital·신규전략 seed 능력이 AUM을 늘리며 carry와 성장에는 낮은 값을 지불한다는 롱이었다. 동종사 중 큰 balance sheet가 downside protection과 상품 확장의 전략자산이라는 점을 강조했다.",
         actual="KKR은 Global Atlantic과 credit·real assets 확장으로 2023년 AUM $553bn, FPAUM $446bn이 됐고 FRE $2.4bn을 기록했다. 2024-01 월말 $86.58로 $24 대비 약 3.6배이며 누적분배는 제외한 수치다. balance sheet는 가치와 성장 seed 역할을 했지만 보험 편입 뒤 단순 청산가치가 아니라 신용·ALM 위험을 포함한 운영자본이 됐다.",
         why="반복보수로 하방을 만들고 carry·신규전략을 upside로 둔 구조가 맞았다. 하지만 balance sheet의 시장가치는 할인과 보상·세금·보험자본을 빼야 주주 청구권이 된다는 점은 더 엄격히 봐야 했다.", first="AUM·관리보수 증가와 투자회수", first_date="2016-02-26", stock="$24.01 월말→$86.58; 가격 약 +261%, 분배 제외", valuation="순투자자산+fee earnings이 가격 대부분; carry·성장 무료옵션",
         claims=[C("locked capital", "장기약정 자본이 경기중에도 fee를 지킨다.", "LP default·조기상환 없이 계약 유지", "AUM 감소와 fee base 급락", "FPAUM과 perpetual capital이 크게 성장했다.", "적중"), C("balance sheet", "큰 자체투자자산이 하방이자 신규전략 seed다.", "NAV가 실현 가능하고 가치파괴 없음", "할인·부채·보상으로 주주 몫 축소", "seed 기능은 맞았으나 보험 편입으로 복잡해졌다.", "부분~적중"), C("carry option", "현재가격은 성과보수를 거의 반영하지 않는다.", "펀드성과와 realization 지속", "성과악화·exit 폐쇄", "누적 carry가 큰 추가가치를 만들었다.", "적중"), C("AUM 성장", "브랜드·성과가 인접전략 재모금을 만든다.", "후속펀드 확대·신규전략 채택", "LP 이탈·fund 축소", "$96bn에서 $553bn으로 확대됐다.", "적중")],
         metrics=[("AUM", "$96bn", "장기 증가", "$553bn FY2023", "적중"), ("FPAUM", "장기 locked", "반복보수", "$446bn FY2023", "적중"), ("FRE", "가격 하방", "증가", "$2.4bn FY2023", "적중"), ("가격", "$24.01", "상승+분배", "$86.58", "매우 성공")]),

    dict(id="51c0005d-78f2-401d-b488-011f6c7b0fd9", date="2016-11-16", ticker="KKR", company="KKR", author="TR1898", source_short=1, link=None, dchars=16129, cchars=413,
         title="65% 순자산 하방과 12% FCF yield 롱", price="$15.3", verdict="초대형 성공", score=9.4, process=9.2,
         thesis="$15 주가에서 순현금·투자자산 $9.75/주가 65%를 덮고 나머지 $5만 반복 fee business 값이라고 계산했다. 향후 FCF $1.85~2.10/주, EV $4.3bn/EBITDA $1.27bn=3.4배, 73% AUM의 8년 이상 lock-up, 아직 fee를 내지 않는 $20bn 약정을 근거로 carry와 AUM 성장·balance-sheet return을 거의 공짜로 샀다. 현재가치 최소 $20/주를 제시했다.",
         actual="$20 목표는 빠르게 달성됐고 2024-01 $86.58로 진입가 대비 약 +466%였다. AUM $553bn·FPAUM $446bn, $39bn fee 미발생 약정, FRE $2.4bn으로 fee conversion 논지가 반복됐다. C-corp 전환과 Global Atlantic 편입도 투자자층과 영구자본을 확대했다.",
         why="순자산·FRE·carry를 분리하고 아직 fee를 내지 않는 약정의 시간표까지 본 것이 강했다. ‘순자산’은 즉시 현금화 가치가 아니며 세금·보상·할인을 적용해야 하지만 진입가격의 margin of safety가 그 오류를 충분히 흡수했다.", first="North America XII fee 활성화와 AUM 성장", first_date="2017-02-09", stock="$15.30 월말 근사→$86.58; 가격 약 +466%, 분배 제외", valuation="$9.75 순자산+$5 fee business; 최소 $20/주",
         claims=[C("순자산 하방", "$9.75/주 순현금·투자가격이 주가 65%를 덮는다.", "NAV 회수와 제한된 holdco 부채", "NAV 30%+ 손상·주주비귀속", "장부·전략투자가치가 장기 커졌다.", "적중"), C("FRE 저평가", "잔여 EV는 3.4x EBITDA·12%+ FCF yield다.", "관리보수 증가가 주당현금으로 전환", "보상·SBC가 FCF 흡수", "FRE $2.4bn으로 규모가 크게 증가했다.", "적중"), C("fee shadow", "$20bn 미수수 약정이 비용 적게 fee로 전환된다.", "투자기간 진입·deployment", "약정 취소·fee holiday", "2023에도 같은 fee-shadow가 $39bn 존재했다.", "적중"), C("구조 촉매", "세제 명확화·C-corp가 discount를 줄인다.", "기관투자자 접근성·지수 적격성 확대", "세금비용이 rerating 상쇄", "2018 C-corp 전환 뒤 장기 rerating했다.", "적중")],
         metrics=[("순자산/주", "$9.75", "하방 65%", "BVPS $30.95 FY2023", "적중"), ("FCF/주", "$1.85~2.10E", "12%+ yield", "FRE/주 $2.68 FY2023", "방향 적중"), ("목표가", "$20+", "+33%", "대폭 초과", "성공"), ("가격", "$15.30", "상승", "$86.58", "초대형 성공")]),

    dict(id="d511f486-ec3e-460b-ad20-f3fe9f630cc7", date="2018-02-01", ticker="KKR", company="KKR", author="rickey824", source_short=0, link="https://www.valueinvestorsclub.com/idea/KKR_andamp%3B_CO_LP/6637431692", dchars=29890, cchars=97,
         title="$34 SOTP와 brand/LP inertia 롱", price="$24.1", verdict="매우 성공", score=9.0, process=9.3,
         thesis="SOTP $34/주로 약 40% upside를 제시했다. FPAUM $114bn의 management fee earnings와 할인한 book value만으로 현 가격을 설명해 carry를 거의 0으로 두었다. 2011년 이후 FPAUM +150%, book value/주 +60%, 누적분배 $7.75를 근거로 복리성을 보였다. 동시에 deal multiple 9.3배, 경쟁심화, realizations 변동, 비지배 구조를 지적하고 balance sheet 20%+ 손상 시 약 $3/주 하방을 stress했다.",
         actual="$34 목표는 2019~20년에 넘어섰고 2024-01 $86.58로 약 +260%였다. FPAUM은 $446bn으로 약 네 배, perpetual capital은 $224bn으로 늘었다. Global Atlantic 인수로 영구자본 논지는 강화됐으나 보험과 전략보유지분 때문에 SOTP·GAAP가 더 복잡해졌다.",
         why="carry를 0으로 두고도 upside가 남는 구조, book value stress, PE 업황 과열을 동시에 적은 process가 좋았다. 브랜드와 LP inertia는 실제로 강했지만 ‘6년은 안전’이 아니라 펀드성과와 fundraising lag를 계속 확인해야 한다.", first="FPAUM 성장·C-corp 전환", first_date="2018-07-02", stock="$24.08 월말→$86.58; 가격 약 +260%, 분배 제외", valuation="management fee value+discounted book; SOTP $34, carry 0",
         claims=[C("fee floor", "FPAUM $114bn fee earnings과 할인 book만으로 가격을 설명한다.", "fee margin·FPAUM 유지", "fundraising 감소·비용급증", "FPAUM은 $446bn으로 증가했다.", "적중"), C("carry 무료", "carry를 0으로 둬도 40% upside다.", "carry가 음의 가치가 아니고 clawback 제한", "성과보상·세금이 가치 상쇄", "실현성과가 추가 수익원이 됐다.", "적중"), C("브랜드 inertia", "LP는 한 번의 나쁜 빈티지보다 긴 기록을 보고 재약정한다.", "상대성과·조직 안정", "핵심인력 이탈·연속 저성과", "fundraising과 전략확장이 지속됐다.", "적중"), C("cycle stress", "높은 9.3x deal multiple과 경쟁에도 book 손상은 약 $3다.", "레버리지·운영개선으로 손실 제한", "경기침체와 exit 폐쇄 동시발생", "2020·2022 변동은 있었지만 장기 thesis를 훼손하지 않았다.", "적중")],
         metrics=[("FPAUM", "$114bn", "성장", "$446bn FY2023", "적중"), ("SOTP", "$34", "약 +40%", "대폭 초과", "성공"), ("누적분배", "$7.75 since 2011", "계속", "추가 분배", "적중"), ("가격", "$24.08", "상승", "$86.58", "매우 성공")]),

    dict(id="8d650efa-8ddd-4371-b3f3-269e6d4b3d99", date="2022-04-21", ticker="KKR", company="KKR", author="juice835", source_short=1, link=None, dchars=5537, cchars=17,
         title="$23.75 비FRE 가치와 15배 core FRE 롱", price="$51", verdict="성공", score=8.8, process=8.7,
         thesis="$112bn dry powder(+67% YoY), 2004~20 organic AUM CAGR 19%, high-teens FRE 성장 전망을 근거로 장기 복리를 주장했다. 주가에서 net balance-sheet assets $13.25, 보험 $6.50, embedded carry $4.00, 합계 $23.75를 빼면 after-tax·after-SBC 2023 FRE $2.15가 약 15배에 불과하다고 계산했다. Global Atlantic의 장기부채와 KKR origination 결합, capital markets의 숨은 수익성을 강조했다.",
         actual="2022년 금리충격으로 단기 하락했지만 2024-01 $86.58로 약 +70%였다. 2023 AUM $553bn, FPAUM $446bn, FRE $2.4bn/$2.68주, perpetual capital $224bn이 됐고 Global Atlantic 잔여 37% 인수도 2024-01-02 완료됐다. 반면 dry powder는 배치 시점보다 $99bn으로 낮아졌고 carry·보험·balance sheet를 액면 합산하는 valuation은 haircut이 필요하다.",
         why="after-SBC FRE와 비FRE 자산을 분리하고 보험·capital markets를 growth engine으로 본 방향이 맞았다. 다만 $23.75가 모두 독립적으로 회수 가능한 현금은 아니며 보험 book·carry에는 자본비용·실현·세금 할인이 필요하다.", first="Global Atlantic 성장과 2023 FRE 증가", first_date="2024-01-02", stock="$50.97 월말→$86.58; 가격 약 +70%, 배당 제외", valuation="$23.75 비FRE 가치 차감 후 2023 after-SBC FRE $2.15의 15x",
         claims=[C("FRE 복리", "high-teens FRE 성장과 15배 core valuation이 매력적이다.", "organic FPAUM 성장·margin 유지", "순유입·FRE/주 한 자릿수", "2023 FRE는 10% 성장, 장기 방향은 유지됐다.", "부분~적중"), C("보험 시너지", "Global Atlantic liabilities가 영구자본과 origination 수요를 만든다.", "보험 spread·자본건전성 유지", "신용·ALM 손실", "perpetual capital $224bn, 잔여지분 인수로 강화됐다.", "적중"), C("비FRE 가치", "$23.75/주의 BS·보험·carry가 별도 청구권이다.", "중복 없이 세후 주주에게 귀속", "할인·부채·보상·실현지연", "가치는 존재하지만 액면합산보다 haircut이 필요하다.", "부분"), C("capital markets", "거래·조달 플랫폼이 고ROE hidden gem이다.", "KKR fund flow와 제3자 거래 지속", "딜 시장 장기폐쇄", "2023 transaction fee $578m으로 의미있는 이익축이었다.", "적중")],
         metrics=[("dry powder", "$112bn", "deployment+성장", "$99bn FY2023", "부분"), ("FRE/주", "$2.15 2023E", "high-teens 성장", "$2.68 FY2023", "적중"), ("perpetual capital", "보험 편입", "증가", "$224bn FY2023", "적중"), ("가격", "$50.97", "장기 복리", "$86.58", "성공")]),

    dict(id="4d8a6934-1a07-4a17-8a69-73270e62c006", date="2014-07-18", ticker="BX", company="Blackstone", author="Shoe", source_short=1, link="https://www.valueinvestorsclub.com/idea/BLACKSTONE_GROUP_LP/5974072490", dchars=86254, cchars=407,
         title="FRE·ENI·DDM 삼각검증 롱", price="$33.84", verdict="매우 성공", score=9.3, process=9.4,
         thesis="AUM $272bn, 2005~13 CAGR 23%, ENI/주 CAGR 13%인 Blackstone을 PE $66bn·Real Estate $83bn·BAAM $61bn·Credit $69bn·Advisory로 분해했다. 2015 management FRE $0.77에 18배를 적용한 $13.88와 carry·투자자산을 합친 SOTP $43.25, 2015 ENI 13배 $45.50, DDM $47.50의 세 방법으로 35~40% upside를 제시했다. 2014 예상 분배수익률 6.8%, 장기 11~12% ENI/DE 성장+5~6% yield로 약 17% 수익을 기대했다.",
         actual="Blackstone은 2023년 AUM $1tn을 넘겨 당시의 약 네 배가 됐고, 부동산·credit·보험·infrastructure·private wealth로 확장했다. 2024-01 실가격 $124.45로 진입가 대비 약 +268%이며 큰 누적분배를 제외한 가격수익이다. 2015 $43~47.5 목표는 달성됐다. 다만 ENI는 미실현 평가와 exit cycle에 민감해 매년 직선으로 성장하지 않았다.",
         why="FRE, ENI multiple, 배당현금흐름을 교차검증하고 downside $25까지 제시한 점이 가장 강하다. 성공의 핵심은 실제 AUM·FRE 복리였으며, 당시 6.8% 배당을 채권처럼 자본화하지 않고 carry·시장주기를 분리한 것이 유효했다.", first="펀드성과·fundraising과 BCP carry catch-up", first_date="2015-02-27", stock="$33.84→$124.45; 가격 약 +268%, 대규모 분배 제외", valuation="SOTP $43.25; 13x 2015 ENI $45.50; DDM $47.50; downside $25",
         claims=[C("AUM flywheel", "성과와 브랜드가 재모금·인접전략 확대를 만든다.", "상대성과·LP 재약정·인재 유지", "flagship 축소·대규모 순유출", "$272bn에서 $1tn+로 성장했다.", "적중"), C("FRE floor", "2015 management FRE $0.77×18=$13.88이 안정적 가치축이다.", "fee-earning AUM·margin 지속", "보수율 하락·비용 급증", "FRE와 영구자본이 장기 확대됐다.", "적중"), C("carry/ENI", "성과실현이 11~12% ENI/DE 성장을 만든다.", "exit 시장이 cycle 내 열리고 carry 현금화", "미실현가치 하락·realization 장기폐쇄", "직선은 아니지만 cycle 전체 현금화됐다.", "부분~적중"), C("분배+rerating", "5~6% yield와 성장으로 약 17% 장기수익이다.", "분배가 earnings로 커버되고 성장 유지", "분배삭감·AUM 정체", "가격과 누적분배 모두 목표를 크게 넘었다.", "적중")],
         metrics=[("AUM", "$272bn", "11~12% earnings 성장", "$1tn+ FY2023", "적중"), ("분배 yield", "6.8% 2014E", "5~6% 장기", "변동분배 지속", "부분~적중"), ("목표가", "$43.25~47.50", "35~40%", "달성", "성공"), ("가격", "$33.84", "약 17% 장기", "$124.45", "매우 성공")]),
]


def idea_sources(idea):
    return [("VIC 원문", f"VIC {idea['company']} {idea['date']} 원문", "Value Investors Club", idea["date"], idea["link"], "당시 주장·증권·가격·촉매의 1차 자료")] + SOURCES[idea["ticker"]]


def build_payload():
    out = {k: [] for k in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")}
    company_names = {"APO": "APOLLO GLOBAL MANAGEMENT", "KKR": "KKR & CO", "BX": "BLACKSTONE"}
    for i in IDEAS:
        out["ideas_master"].append({"idea_id": i["id"], "date": i["date"], "year": int(i["date"][:4]), "ticker": i["ticker"], "company_name": company_names[i["ticker"]], "author": i["author"], "direction_ko": "숏" if i["source_short"] else "롱", "is_short": i["source_short"], "contest_winner": 0, "source_link": i["link"], "description_chars": i["dchars"], "catalyst_chars": i["cchars"], "narrative_tags_ko": "원본 방향 교정; 대체자산운용; 심층검증", "idea_type_ko": "기업가치", "performance_available": 0, "auto_tag_status_ko": "수동 심층검증"})
        note = f"원 SQL의 is_short={str(bool(i['source_short'])).lower()}는 보존했다. 본문·추천증권·상승 목표상 실제 방향은 Long이다. 가격 비교는 게시월 또는 원문 가격과 2024-01 월말 실가격의 근사치이며 배당·분배는 제외했다."
        out["postmortems"].append({"idea_id": i["id"], "ticker": i["ticker"], "research_direction_ko": "Long", "company_description_ko": DESCRIPTIONS[i["ticker"]], "original_thesis_ko": i["thesis"], "actual_development_ko": i["actual"], "thesis_verdict_ko": i["why"], "business_verdict_ko": i["actual"], "catalyst_verdict_ko": i["first"], "valuation_verdict_ko": i["valuation"], "stock_verdict_ko": i["stock"], "current_verdict_ko": i["actual"], "overall_verdict_ko": i["verdict"], "why_ko": i["why"], "success_pattern_ko": "locked_capital; fee_related_earnings; permanent_capital; sum_of_parts; valuation_discipline", "failure_pattern_ko": "carry_cyclicality; insurance_balance_sheet; nav_haircut; forecast_stacking", "root_error_ko": "보험·carry·balance-sheet 청구권에는 자본비용·실현·세금·희석 haircut이 필요", "first_signal_ko": i["first"], "first_signal_date": i["first_date"], "knowable_at_t0_ko": "FPAUM·fee shadow·FRE margin·실현 carry·순자산·보험 spread를 분리하면 당시에도 가설을 검증할 수 있었다.", "avoidability_ko": "높음. 총 AUM이나 ENI 하나 대신 각 earnings stream과 주주 귀속을 분리해야 한다.", "counterfactual_question_ko": i["claims"][0][3], "analyst_note_ko": note, "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None, "confidence": 0.96, "research_asof": ASOF, "research_status_ko": "외부검증 완료"})
        out["meta"].append({"idea_id": i["id"], "analysis_depth_ko": "기업·증권·논지·실제결과·인과·반증조건 심층분석", "report_version": "V7-detailed", "thesis_type_ko": i["title"], "one_line_verdict_ko": i["why"], "thesis_score": i["score"], "process_score": i["process"], "return_summary_ko": i["stock"], "core_error_ko": "청구권별 haircut 필요", "core_insight_ko": i["claims"][0][4], "research_asof": ASOF})
        bodies = [DESCRIPTIONS[i["ticker"]], i["thesis"], i["actual"], f"종합판정은 {i['verdict']}다. {i['why']}"]
        for n, (t, b) in enumerate(zip(("기업과 돈 버는 구조", "원 투자논지", "실제 전개", "투자 결론과 학습"), bodies), 1): out["sections"].append({"idea_id": i["id"], "section_order": n, "section_title_ko": t, "section_body_ko": b})
        for n, c in enumerate(i["claims"], 1):
            out["claims"].append({"idea_id": i["id"], "claim_order": n, "claim_title_ko": c[0], "thesis_weight_pct": 25, "original_claim_ko": c[1], "t0_evidence_ko": i["thesis"], "key_assumption_ko": c[2], "ex_ante_falsifier_ko": c[3], "actual_result_ko": c[4], "quantitative_gap_ko": i["stock"] if n == 4 else i["valuation"], "verdict_ko": c[5], "analytical_error_ko": "중대한 오류 없음" if "적중" in c[5] else "청구권·시간·cycle 분리 필요", "reusable_lesson_ko": f"{c[0]}는 주장과 함께 ‘{c[3]}’를 사전 경보로 저장한다."})
        for n, m in enumerate(i["metrics"], 1): out["metrics"].append({"idea_id": i["id"], "metric_order": n, "metric_name_ko": m[0], "t0_value_ko": m[1], "thesis_expectation_ko": m[2], "actual_value_ko": m[3], "verdict_ko": m[4], "interpretation_ko": f"당시 {m[1]}, 기대 {m[2]}, 실제 {m[3]}."})
        timeline = [(i["first_date"], i["first"], "첫 핵심 검증 신호"), ("2022-01-01" if i["ticker"] == "APO" else "2021-02-01" if i["ticker"] == "KKR" else "2023-06-30", "영구자본·전략 확대", "사업모델 확장"), ("2023-12-31", "FY2023 사업규모 확인", i["actual"]), (ASOF, "평가기준일", i["stock"])]
        for n, e in enumerate(timeline, 1): out["timeline"].append({"idea_id": i["id"], "event_order": n, "event_date_ko": e[0], "event_ko": e[1], "thesis_implication_ko": e[2]})
        for n, s in enumerate(idea_sources(i), 1): out["sources"].append({"idea_id": i["id"], "source_order": n, "source_type_ko": s[0], "title_ko": s[1], "publisher": s[2], "source_date": s[3], "url": s[4], "evidence_ko": s[5]})
    return out


def company_report(ticker, ideas):
    name = {"APO": "Apollo Global Management", "KKR": "KKR & Co.", "BX": "Blackstone"}[ticker]
    lines = [f"# {name} ({ticker}) — 기업과 비즈니스", "", DESCRIPTIONS[ticker], "", "## 돈을 버는 구조", "", "- 반복이익: fee-paying AUM × 보수율 − 보상·운영비 = FRE", "- 성과이익: 펀드수익이 hurdle을 넘고 실제 회수될 때 carry 발생", "- 자체자본: balance-sheet 투자수익과 신규전략 seed, 단 할인·세금·부채 필요", "- 보험자본: APO의 Athene·KKR의 Global Atlantic은 장기자금과 spread를 제공하지만 신용·ALM·규제자본 위험 동반", "", "## 아이디어 전체 판정", "", "| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |", "|---|---|---|---|---|---|"]
    for i in ideas: lines.append(f"| {i['date']} | {'Short' if i['source_short'] else 'Long'} | Long | {i['title']} | {i['stock']} | {i['verdict']} |")
    for n, i in enumerate(ideas, 1):
        lines += ["", f"## {n}. {i['date']} — {i['title']}", "", "### 원 투자논지", "", i["thesis"], "", "### 논지를 구성한 핵심 주장", ""]
        for j, c in enumerate(i["claims"], 1): lines += [f"#### {j}. {c[0]} — {c[5]}", "", f"**핵심 주장:** {c[1]}", "", f"**이 주장이 성립하려면:** {c[2]}", "", f"**사전 반증조건:** {c[3]}", "", f"**실제 결과:** {c[4]}", ""]
        lines += ["### 논지 구조와 검증", "", "| 축 | 당시 주장 | 실제 검증 |", "|---|---|---|", f"| 사업·경제성 | {i['thesis']} | {i['actual']} |", f"| 밸류에이션·청구권 | {i['valuation']} | {i['stock']} |", f"| 촉매·시간 | {i['first']} | 첫 확인 {i['first_date']} |", f"| 사전 반증 | {i['claims'][0][3]} | {i['why']} |", "", "### 실제 전개와 투자 결론", "", i["actual"], "", f"**종합판정: {i['verdict']}.** {i['why']}", "", "### 핵심 수치", "", "| 지표 | 글 당시 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
        for m in i["metrics"]: lines.append(f"| {m[0]} | {m[1]} | {m[2]} | {m[3]} | {m[4]} |")
        lines += ["", f"재사용 질문: **{i['claims'][0][3]}**"]
    conclusions = {"APO": "Apollo 다섯 롱은 모두 성공했다. 초기 글들의 Athene 영구자본 통찰은 특히 정확했고, 2021~22 글은 합병과 FRE/SRE 분리를 촉매·배수에 직접 연결했다. 반복 오류는 보험자산을 단순 asset-light fee base로 보고 신용·ALM·규제자본을 충분히 할인하지 않은 것이다.", "KKR": "KKR 네 롱은 모두 성공했다. 순자산·FRE를 하방으로 두고 carry와 신규전략을 무료 또는 저가 option으로 산 구조가 반복됐다. Global Atlantic은 permanent capital 논지를 강화했지만 보험 book와 전략보유지분을 액면가로 SOTP에 넣어서는 안 된다.", "BX": "Blackstone 2014 롱은 AUM·FRE 복리와 분배를 정확히 잡아 매우 성공했다. 가장 좋은 점은 SOTP·ENI multiple·DDM을 교차검증하고 $25 downside까지 적은 것이다. ENI는 미실현 carry가 섞이는 만큼 직선형 EPS처럼 취급하지 않는 규율이 핵심이다."}
    lines += ["", f"## {ASOF} 기준 기업 결론", "", conclusions[ticker], "", "## 주요 근거", ""]
    seen = set()
    for i in ideas:
        for s in idea_sources(i):
            if s[4] and s[4] not in seen: seen.add(s[4]); lines.append(f"- [{s[1]}]({s[4]})")
    return "\n".join(lines)


def build_report():
    head = f"""# Batch 012 — Apollo·KKR·Blackstone 10건

평가기준일: {ASOF}

분석일: {ANALYSIS_DATE}

대상: Apollo 5건·KKR 4건·Blackstone 1건

## 결론부터

이번 10건의 실제 방향은 **모두 Long**이며 10건 모두 2024-01-31 가격 기준 성공했다. 공통 승리공식은 ‘총 AUM이 크다’가 아니라 **오래 잠긴 fee-paying capital, 성장하는 FRE, 할인된 balance sheet와 carry option을 분리해 샀다**는 것이다. 가장 큰 장기 변화는 Apollo의 Athene, KKR의 Global Atlantic처럼 보험부채가 영구자본과 origination 수요를 제공한 점이다. 동시에 이는 asset-light 운용사에 신용·ALM·규제자본 위험을 더했으므로 같은 배수를 적용하면 안 된다.

| 기업 | 건수 | 가장 강한 성공 | 남는 핵심 위험 | 반복 학습 |
|---|---:|---|---|---|
| Apollo | 5 | Athene 영구자본·2022 합병·FRE/SRE 분리 | 보험 신용·ALM·복합기업 할인 | FRE와 SRE를 다른 자본비용으로 평가 |
| KKR | 4 | 순자산+FRE 하방, carry·신규전략 옵션 | balance sheet·보험 book의 회수 haircut | AUM보다 FPAUM·FRE/주·희석 확인 |
| Blackstone | 1 | SOTP·ENI·DDM 삼각검증 | 미실현 carry와 exit cycle | 분배와 실현수익으로 ENI 검증 |

> 데이터 경고: 원 SQL의 `is_short`는 10건 중 7건에서 실제 추천 방향과 반대다. Apollo 2014·2020·2021·2022, KKR 2016·2022, Blackstone 2014는 SQL상 Short지만 본문·기대수익·증권은 명백한 Long이다. 원본 flag는 감사추적용으로 보존하고 분석 방향만 교정했다. 또 2001~2007년 티커 APO는 **American Community Properties**로 현 Apollo와 다른 기업이어서 이 배치에서 제외했다.

---
"""
    blocks = [head]
    for t in ("APO", "KKR", "BX"):
        blocks.append(company_report(t, sorted([i for i in IDEAS if i["ticker"] == t], key=lambda x: x["date"])))
        blocks.append("\n\n---\n")
    blocks.append("""# 배치 공통 패턴과 DB 학습 태그

| 패턴 | 성공 메커니즘 | 실패를 부르는 오용 |
|---|---|---|
| locked/permanent capital | 환매 압박이 낮아 fee visibility와 contrarian deployment 확보 | 보험부채 위험까지 asset-light로 착각 |
| FRE floor + carry option | 반복보수로 하방을 만들고 성과보수에 낮은 값만 지불 | carry를 정상 EPS처럼 고배수 적용 |
| fee shadow | 미수수 약정의 투자기간 진입이 비용 적은 성장 | deployment 지연·fee offset 무시 |
| balance-sheet SOTP | 현가격에서 숨은 투자자산·seed 능력 발견 | NAV를 세금·부채·보상·유동성 할인 없이 합산 |
| structure catalyst | C-corp·지배구조 단순화가 투자자층 확대 | 구조개편만으로 사업위험까지 사라진다고 가정 |

핵심 학습 태그: `alternative_asset_manager`, `fee_paying_aum`, `locked_capital`, `permanent_capital`, `fre_floor`, `carry_option`, `fee_shadow`, `insurance_spread`, `nav_haircut`, `sum_of_parts`, `structure_catalyst`, `forecast_stacking`.

# 데이터 품질·방법론

- 평가기준일은 2024-01-31로 고정했다. 2023 회계연도 결과가 기준일 뒤 발표됐더라도 2023-12-31 현재의 사업상태 확인에만 사용했다.
- 가격은 원문 가격 또는 게시월 실가격과 2024-01 월말을 비교한 근사치다. APO·KKR·BX는 과거 분배가 커서 **배당 제외 가격수익은 실제 총수익을 과소평가**한다.
- 판정은 주가방향, FRE·SRE·carry의 사업인과, valuation 청구권, 촉매·시간을 분리했다.
- 총 AUM 성장만으로 성공 처리하지 않고 FPAUM·FRE/주·영구자본·희석과 보험위험을 함께 확인했다.
""")
    return "\n".join(blocks)


def main():
    payload = build_payload(); report = build_report()
    jp = ROOT / "data/curated/batch_012_alt_managers_deep_v7.json"
    mp = ROOT / "analysis/batch_012_alt_managers_10.md"
    jp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    mp.write_text(report, encoding="utf-8")
    print({k: len(v) for k, v in payload.items()}); print({"report_chars": len(report), "json": str(jp), "markdown": str(mp)})


if __name__ == "__main__": main()
