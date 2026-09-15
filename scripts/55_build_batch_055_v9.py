#!/usr/bin/env python3
"""Build Batch 055 Rosetta Stone / Sinclair / Diamond / Stamps.com V9 artifacts."""
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
    "rst55": (
        "2019년 Rosetta Stone은 legacy Consumer Language, Enterprise & Education Language, K-12 literacy SaaS인 Lexia를 함께 보유했다. "
        "핵심 현금엔진은 `district/learner 수×subscription price×renewal+신규 product attach-sales·implementation·content/R&D-corporate cost-tax`다. "
        "Lexia의 bookings·recurring mix·retention·sales productivity가 consolidated EBITDA보다 중요했고, SOTP에서는 legacy language의 현금 또는 wind-down cost, "
        "standalone public-company cost와 세금을 차감해야 했다. strategic buyer는 school distribution과 cross-sell로 standalone보다 더 높은 가치를 만들 수 있었다."
    ),
    "sbgi55": (
        "Sinclair Broadcast Group은 local television stations, digital assets와 시기별 비핵심 미디어 투자를 보유했다. 방송 현금엔진은 "
        "`local/national/political 광고+MVPD/vMVPD 가입자×retrans fee-network reverse compensation-station opex-corporate-maintenance capex-interest-tax`다. "
        "retrans와 정치광고가 성장을 만들 수 있지만 cord-cutting, network fees, 규제 ownership cap과 acquisitive capital allocation이 duration을 줄인다. "
        "따라서 levered FCF yield는 영구수익률이 아니라 even/odd 정치주기 평균과 runoff 기간, debt·legal reserve·share count를 거쳐 common에 귀속시켜야 한다."
    ),
    "diamond55": (
        "Diamond Sports Group은 지역 스포츠 네트워크에서 `MVPD/vMVPD 가입자×affiliate fee+광고-sports rights escalator-production-distribution-corporate cost-interest`를 번다. "
        "가입자와 carriage가 줄어도 다년간 rights payment는 빠르게 내려가지 않아 operating leverage가 역방향으로 작동한다. credit 분석에서는 positive EBITDA나 FCF보다 "
        "secured/unsecured priority, current asset value 대비 LTV, cash interest, rights commitments, distribution renewal과 liability-management transaction을 먼저 본다. "
        "Sinclair parent에 non-recourse라는 문구는 Diamond 채권자에게 protection이 아니라 parent support가 제한될 수 있다는 뜻이다."
    ),
    "stmp55": (
        "2003년 Stamps.com은 USPS가 승인한 PC postage software와 NetStamps·shipping labels를 개인·소기업에 subscription으로 판매했다. 현금엔진은 "
        "`유료고객×월 구독료+label/supplies-customer acquisition cost-customer support·postage processing-product/R&D-G&A-capex-tax`다. "
        "turnaround의 핵심은 비용절감만이 아니라 주소 입력 없이 우표처럼 쓰는 NetStamps가 product friction을 낮추고, paid churn과 CAC 대비 cohort NPV가 양수로 바뀌는지였다. "
        "large cash balance는 burn·소송·마케팅 재투자를 차감한 runway이며 영구적인 주가 floor는 아니다."
    ),
})

m.SOURCES.update({
    "rst55": [
        m.S("Rosetta Stone SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1351285&owner=exclude", "SEC / Rosetta Stone", "2009-2020", "segment·strategic review·transaction filing 연속성"),
        m.S("Rosetta Stone 2020 proxy", "https://www.sec.gov/Archives/edgar/data/1351285/000156459020017251/rst-pre14a_20200611.htm", "SEC / Rosetta Stone", "2020-04-16", "2019 Literacy revenue·segment mix·governance"),
        m.S("Cambium acquisition agreement", "https://www.sec.gov/Archives/edgar/data/1351285/000119312520235565/d60457dex991.htm", "SEC / Rosetta Stone", "2020-08-31", "$30/share cash·약 $792m equity value"),
        m.S("Cambium acquisition completion", "https://www.sec.gov/Archives/edgar/data/1351285/000119312520269980/d84157dex991.htm", "SEC / Rosetta Stone", "2020-10-15", "거래 종결과 standalone RST terminal event"),
        m.S("Lexia acquisition", "https://www.sec.gov/Archives/edgar/data/1351285/000110465913056496/a13-17097_1ex99d1.htm", "SEC / Rosetta Stone", "2013-07-22", "$22.5m Lexia 인수와 hidden asset origin"),
    ],
    "sbgi55": [
        m.S("Sinclair SEC archive", "https://www.sec.gov/edgar/browse/?CIK=912752&owner=exclude", "SEC / Sinclair", "1995-2025", "방송·부채·M&A·Diamond 연속성"),
        m.S("Sinclair 2015 Form 10-K", "https://www.sec.gov/Archives/edgar/data/912752/000091275216000020/sbgi-20151231x10k.htm", "SEC / Sinclair", "2016-02", "broadcast·retrans·leverage와 지배구조"),
        m.S("Sinclair FY2016 results", "https://sbgi.net/sinclair-reports-fourth-quarter-2016-financial-results/", "Sinclair", "2017-03", "2016 매출·영업이익·정치광고"),
        m.S("Sinclair 2017 Form 10-K", "https://www.sec.gov/Archives/edgar/data/912752/000091275218000006/sbgi-20171231x10k.htm", "SEC / Sinclair", "2018-03", "spectrum $310.8m·사업·자본배분"),
        m.S("Tribune merger termination", "https://www.sec.gov/Archives/edgar/data/726513/000119312518248520/d560189d8k.htm", "SEC / Tribune Media", "2018-08-09", "Sinclair 거래 종료와 소송"),
        m.S("RSN acquisition announcement", "https://sbgi.net/sinclair-broadcast-group-to-acquire-21-regional-sports-networks-from-disney-at-a-valuation-of-10-6-billion/", "Sinclair", "2019-05-03", "21 RSN·$10.6bn enterprise value"),
        m.S("2021 Diamond A/R facility", "https://www.sec.gov/Archives/edgar/data/912752/000091275221000078/arfacilitypressrelease11521.htm", "SEC / Sinclair", "2021-11-05", "Sinclair의 약 $184.4m lender-obligation 인수"),
        m.S("2022 Diamond exchange", "https://www.sec.gov/Archives/edgar/data/912752/000091275222000014/dsgexchangeofferandconsent.htm", "SEC / Sinclair", "2022", "Diamond debt exchange와 restructuring"),
        m.S("2024 Sinclair-Diamond settlement", "https://www.sec.gov/Archives/edgar/data/912752/000197121324000003/pressreleasedated11724.htm", "SEC / Sinclair", "2024-01-17", "$495m cash settlement·litigation resolution"),
        m.S("Sinclair 2024 annual report", "https://www.sec.gov/Archives/edgar/data/1971213/000197121325000031/finalannualreport2024.pdf", "SEC / Sinclair", "2025", "Diamond emergence·parent exposure 후속검증"),
    ],
    "diamond55": [
        m.S("Sinclair RSN acquisition", "https://sbgi.net/sinclair-broadcast-group-to-acquire-21-regional-sports-networks-from-disney-at-a-valuation-of-10-6-billion/", "Sinclair", "2019-05-03", "$10.6bn purchase value와 financing context"),
        m.S("2020 Diamond exchange completion", "https://www.sec.gov/Archives/edgar/data/912752/000091275220000054/exhibit991-pressreleas.htm", "SEC / Sinclair", "2020-06", "2027 unsecured와 secured exchange"),
        m.S("2022 Diamond exchange", "https://www.sec.gov/Archives/edgar/data/912752/000091275222000014/dsgexchangeofferandconsent.htm", "SEC / Sinclair", "2022", "추가 liability management"),
        m.S("Diamond Chapter 11 case", "https://cases.ra.kroll.com/DSG/", "Kroll Restructuring Administration", "2023-2025", "Chapter 11 docket·plan·final decree"),
        m.S("Diamond Chapter 11 announcement", "https://www.businesswire.com/news/home/20230314006050/en/Diamond-Sports-Group-Commences-Voluntary-Chapter-11-Proceedings-to-Strengthen-Balance-Sheet-and-Continue-Broadcasting-Local-Sports-Nationwide", "Diamond Sports Group", "2023-03-14", "약 $8bn debt elimination 계획"),
        m.S("Sinclair-Diamond settlement", "https://www.sec.gov/Archives/edgar/data/912752/000197121324000003/pressreleasedated11724.htm", "SEC / Sinclair", "2024-01-17", "intercompany litigation과 cash settlement"),
    ],
    "stmp55": [
        m.S("Stamps.com SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1082923&owner=exclude", "SEC / Stamps.com", "1999-2021", "제품·고객·cash·capital allocation 연속성"),
        m.S("Stamps.com 2004 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1082923/000114420405007345/stampscom10k.htm", "SEC / Stamps.com", "2005-03", "2003/04 revenue·customers·NetStamps 검증"),
        m.S("Thoma Bravo acquisition release", "https://www.sec.gov/Archives/edgar/data/1082923/000114036121023931/brhc10026739_ex99-1.htm", "SEC / Stamps.com", "2021-07-09", "$330/share·약 $6.6bn transaction"),
        m.S("Stamps.com merger filing", "https://www.sec.gov/Archives/edgar/data/1082923/000114036121023954/brhc10026745_8k.htm", "SEC / Stamps.com", "2021-07-09", "merger agreement와 cash consideration"),
        m.S("USPS PC Postage", "https://postalpro.usps.com/operations/pc-postage", "U.S. Postal Service", "2000s-2026", "PC postage authorization framework"),
    ],
})


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**x):
    x["claims"] = [C(*row) for row in x.pop("claimdata")]
    x.setdefault("security", "Sinclair Class A common stock" if x.get("ticker") == "SBGI" else "Common stock")
    x.setdefault("waterfall", "사업 현금에서 운전자본·maintenance/growth investment·interest·tax·법적 준비금을 차감하고, debt와 계약상 senior claim을 먼저 지급한 뒤의 per-share 현금만 common payoff로 본다.")
    x.setdefault("contest", False)
    return x


IDEAS = [
I(id="16a5635a-fb3d-4b31-ac8d-cab816ec3200", date="2019-10-16", author="SlackTide", ticker="RST", entity="Rosetta Stone Inc.", group="rst55", raw_short=True, direction="Long", entry="$16.90", horizon="6~18개월", filename="analysis/ideas/2019/2019-10-16_RST_long.md", link="https://www.valueinvestorsclub.com/idea/ROSETTA_STONE_INC/2553065619", desc=0, cat=91, contest=True,
title="Lexia standalone value·strategic review Long", verdict="Lexia asset proof와 $30 cash sale 강한 성공·exact return 미검증", score=9.7, process=9.6,
summary="raw Short와 달리 $16.90에서 Bear -17%, Base +90%, Bull +244%를 제시한 contest-winning Long이다. EV 약 $404m·2020 recurring revenue 약 2.0x에서 Lexia의 90% recurring mix, 100%+ retention, 2020 billings 약 $100m와 activist/strategic review를 묶어 standalone $600~800m를 주장했다.",
valuation="$16.90와 EV $404m에서 Base는 약 $32, Bear 약 $14, Bull 약 $58의 구조다. Lexia $600~800m에 legacy language와 net cash를 더하고 corporate cost·tax를 빼야 한다. 2020 whole-company cash bid $30/약 $792m equity value는 Base와 asset-value band에 근접했지만 deal price는 exact holding-period return이 아니다.",
actual="2019 Literacy revenue는 $62.6m으로 19% 증가했고 consolidated revenue도 5% 늘었다. 2020-08-31 Cambium Learning/Veritas가 Rosetta Stone 전부를 $30/share cash, 약 $792m equity value에 인수하기로 했고 2020-10-15 종결했다. Lexia의 observable growth와 buyer route가 동시에 검증됐다.",
price="첨부 SQL에는 catalyst 91자만 있고 description·performance COPY는 없다. $16.90·Base $32·$30 cash는 prior metadata와 공시의 T0/event anchor다. 배당·정확 posting timestamp가 없어 return/IRR은 null이며, 단순 $16.90→$30 계산을 공식 성과로 저장하지 않는다.",
drivers="가치를 만든 원인은 RST 브랜드의 회복이 아니라 Lexia라는 distinct asset의 recurring bookings, retention, school distribution과 sale route였다. consolidated loss가 가리던 asset economics를 분리했고, board/activist pressure가 private-market value를 common cash로 전환했다.",
error="private EdTech multiple과 2020 billings $100m을 base에 가깝게 둔 점, corporate/standalone cost와 tax leakage가 얇은 점은 약점이다. ELL launch와 buyer demand가 기대보다 약할 수 있었고 strategic review가 곧 sale을 뜻하지는 않았다.", first_signal="Lexia bookings growth<15%, net retention<100%, 2020 billings target 철회 또는 strategic review가 두 분기 넘게 구체적 buyer/process 없이 지연되면 $600~800m를 3~5x stress로 낮춘다.",
metrics=[("Entry/EV", "$16.90/$404m", "Base 약 $32", "$30 cash event", "강한 성공 방향"),("Lexia value", "$600~800m", "whole EV 초과", "$792m whole-company equity", "강한 성공"),("Recurring mix", "약 90%", "유지", "strategic SaaS sale", "성공 방향"),("Retention", ">100%", "growth 지속", "2019 Literacy +19%", "성공 방향"),("Catalyst", "strategic alternatives", "2020 unlock", "2020-08 agreement", "강한 성공")],
timeline=[("2013-07", "Lexia $22.5m 인수", "hidden asset seed"),("2018-09", "선행 Lexia SOTP Long", "asset proof"),("2019-10-16", "VIC Long", "$16.90·Base +90%"),("2019-FY", "Literacy $62.6m/+19%", "운영 검증"),("2020-07", "sale process", "catalyst 구체화"),("2020-08-31", "$30 cash agreement", "가치 현실화"),("2020-10-15", "거래 종결", "terminal cash event")],
claimdata=[("Lexia crown jewel", "Lexia가 whole-company value를 좌우한다.", "recurring mix·retention·bookings", "school renewal과 sales efficiency가 지속된다.", "growth<15%·retention<100%면 반증.", "$30 whole-company sale", "강한 성공", "legacy label보다 segment cash engine을 본다."),("$600~800m standalone", "Lexia만으로 EV를 넘는다.", "2020 billings와 private comps", "corporate cost·tax가 제한적이다.", "3x stress value<EV면 반증.", "$792m whole-company equity value", "강한 성공 방향", "gross multiple에서 standalone drag를 뺀다."),("legacy language residual", "language 사업은 zero 이상이다.", "subscription transition", "cash burn이 Lexia를 잠식하지 않는다.", "negative FCF 확대면 반증.", "buyer가 전체 회사를 인수", "부분 성공", "free option에도 wind-down cost를 둔다."),("strategic review", "2020 sale/split/spin이 가능하다.", "activist·board representation·SQL catalyst", "board가 process를 실행한다.", "두 분기 무진전이면 반증.", "2020 sale 완료", "강한 성공", "asset discount에는 실행주체가 필요하다."),("ELL growth", "신제품이 billings를 가속한다.", "district adjacency", "cross-sell CAC가 낮다.", "attach·renewal 약화면 반증.", "takeout이 빨라 장기효과 미관측", "미검증", "제품 옵션과 sale catalyst를 분리한다."),("Long direction", "raw Short가 아니라 Base +90% Long이다.", "positive payoff cases", "동일 common 기준이다.", "negative target/borrow 확인 시 반증.", "Long으로 교정", "성공", "방향은 payoff로 확정한다.")]),

I(id="90e1d392-4d7f-46c0-9f5e-10f1818b49c3", date="2019-12-09", author="Cries", ticker="RST", entity="Rosetta Stone Inc.", group="rst55", raw_short=True, direction="Long", entry="$20 이하", horizon="1~2년", filename="analysis/ideas/2019/2019-12-09_RST_long.md", link="https://www.valueinvestorsclub.com/idea/ROSETTA_STONE_INC/1602994739", desc=0, cat=38,
title="private EdTech takeout multiple Long", verdict="buyer 이름은 틀렸지만 9개월 내 $30 strategic sale 강한 성공", score=9.2, process=8.8,
summary="첫 문장이 Buy RST이며 $20 이하는 좋은 entry라고 한 Long이다. no-growth EdTech annuity도 약 4x bookings, 20%+ 성장하는 Lexia는 5~6x가 가능하고 school distribution과 product adjacency를 가진 strategic buyer가 cross-sell synergy를 지불해 1년 +70%, 2년 double이 가능하다고 봤다.",
valuation="공개시장 consolidated EBITDA가 아니라 Lexia bookings×4x floor 또는 5~6x strategic multiple을 사용했다. $20 entry에서 $30 cash는 nominal 50% 사건 격차지만 정확 total return은 아니다. buyer synergy를 standalone value와 별도 layer로 두고 corporate cost·tax·legacy language를 차감해야 한다.",
actual="예상 매수자는 Renaissance였으나 실제 buyer는 Cambium Learning/Veritas였다. 2019-12 글 뒤 약 9개월 만인 2020-08-31 $30/share cash 계약이 발표되고 10월 완료됐다. buyer identity는 틀렸지만 distribution·product adjacency·private scarcity라는 buyer economics는 맞았다.",
price="현 SQL에는 catalyst 38자만 있고 description·performance는 없다. $20 이하·1Y +70%·2Y double과 $30 cash는 thesis/event anchors다. 실제 fill price·배당이 없어 exact return/IRR은 null이다.",
drivers="결과를 만든 것은 public multiple rerating보다 strategic buyer가 district access, renewal base와 cross-sell를 내부화한 것이다. 매수자 이름 하나에 의존하지 않고 여러 EdTech buyer가 공유하는 synergy를 본 것이 강점이었다.",
error="‘손실이 불가능’하다는 확신 표현은 process상 틀렸다. 4x floor도 retention·implementation cost·school-budget risk가 악화하면 깨질 수 있고 buyer financing·board willingness·tax leakage를 더 크게 haircut했어야 한다.", first_signal="Lexia growth<15%, bookings retention<100%, district implementation churn 증가 또는 strategic contact가 12개월 내 전혀 구체화되지 않으면 4x floor와 5~6x takeout case를 재평가한다.",
metrics=[("Entry", "$20 이하", "1Y +70%/2Y double", "$30 cash event", "방향 성공"),("Floor multiple", "4x bookings", "annuity floor", "whole-company transaction", "성공 방향"),("Takeout multiple", "5~6x", "strategic synergy", "Lexia-only 분해 불가", "부분 검증"),("Growth", "20%+", "유지", "2019 Literacy +19%", "근접 성공"),("Timing", "1~2년", "sale", "약 9개월 내 발표", "강한 성공")],
timeline=[("2013-07", "Lexia 인수", "scarce asset 형성"),("2018~19", "Literacy 성장", "buyer economics 강화"),("2019-12-09", "VIC Long", "$20 이하"),("2020-H1", "strategic process", "exit route"),("2020-08-31", "Cambium agreement", "$30 cash"),("2020-10-15", "거래 종결", "terminal event"),("2020 이후", "buyer가 school portfolio 통합", "synergy thesis 방향 확인")],
claimdata=[("private-market lens", "Lexia는 public FCF보다 bookings multiple로 봐야 한다.", "EdTech transaction comps", "retention·growth·gross margin이 유사하다.", "renewal 급락이면 반증.", "strategic cash sale", "성공", "시장별 buyer economics를 맞춘다."),("4x floor", "no-growth annuity도 4x 가치다.", "recurring school revenue", "cash contribution이 양수다.", "standalone FCF 음수 지속이면 반증.", "whole-company $30 bid", "성공 방향", "floor에도 cost와 tax를 뺀다."),("5~6x takeout", "성장 Lexia는 상단 multiple을 받는다.", "20%+ growth·scarcity", "buyer 경쟁이 존재한다.", "process 무산·multiple 하락이면 반증.", "Lexia-only multiple은 미공개", "부분 검증", "deal value와 segment value를 구분한다."),("distribution moat", "district trust·sales access가 진입장벽이다.", "school sales cycle", "buyer cross-sell가 CAC를 낮춘다.", "renewal·sales productivity 하락이면 반증.", "EdTech buyer가 전체 인수", "성공 방향", "software code보다 distribution을 본다."),("Renaissance buyer", "Renaissance가 자연스러운 buyer다.", "product adjacency", "특정 buyer가 실행한다.", "다른 buyer/무매각이면 반증.", "Cambium/Veritas가 인수", "이름 실패", "buyer identity보다 공통 synergy를 본다."),("loss impossible", "이 가격에서 손실 가능성이 거의 없다.", "4x floor", "asset·market·process risk가 제한된다.", "growth 둔화·process failure면 반증.", "결과는 성공", "표현 실패", "좋은 결과가 무위험 주장을 정당화하지 않는다.")]),

I(id="2035e135-0601-4545-9f0c-0f1562365ac0", date="2013-01-14", author="sas7", ticker="SBGI", entity="Sinclair Broadcast Group, Inc.", group="sbgi55", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="12~24개월", filename="analysis/ideas/2013/2013-01-14_SBGI_long.md", link="https://www.valueinvestorsclub.com/idea/Sinclair_Broadcast_Group/3016974975", desc=0, cat=291,
title="$1.1bn acquisition estimate gap·21% FCF yield Long", verdict="retrans·acquisition FCF 방향 성공·exact return 미검증", score=8.8, process=8.9,
summary="raw Short와 Diamond Sports mapping은 모두 틀렸고 실제 대상은 2013 Sinclair common Long이다. 최근 12개월 약 $1.1bn 인수의 FCF가 consensus 2014 EBITDA에 덜 반영됐고 normalized FCF yield 약 21%를 12%로 정상화하면 $23 target이라는 estimate-gap thesis였다.",
valuation="station EBITDA에서 maintenance capex·cash interest·tax를 뺀 normalized levered FCF에 12% yield를 적용해 $23을 제시했다. 21% yield가 구조적 decline을 보상하는지, 단순 pro-forma estimate lag인지가 핵심이다. 인수 EBITDA는 closing timing·synergy·incremental debt와 share count를 같은 bridge에 넣어야 한다.",
actual="후속 공식 자료에서 2015 revenue $2.219bn은 2016 $2.737bn으로 23.3% 늘었고 2016 operating income은 $602.9m으로 42.6% 증가했다. retrans·정치광고·M&A cash engine은 성공 방향이었다. 다만 장기적으로 Diamond capital allocation이 core 방송가치와 별개의 큰 손실을 만들었다.",
price="첨부 SQL에는 291자 catalyst만 있고 description·performance는 없다. 21%/12% FCF yield와 $23 target은 prior metadata anchor다. 역사적 차트로 target 도달을 대체하지 않으며 exact return/IRR은 null이다.",
drivers="초기 가치상승의 원인은 old-media narrative 반박 자체가 아니라 already-closed acquisitions의 EBITDA가 estimate에 들어오는 기계적 bridge, retrans 성장과 낮은 maintenance capex였다. 당시 cord-cutting 속도는 이 현금증가보다 느렸다.",
error="pro-forma FCF의 network reverse compensation, integration cost와 debt funding을 더 명확히 분해하지 않았다. owner-controlled acquisition machine이 core에서 번 현금을 더 위험한 인수로 옮길 수 있다는 장기 capital-allocation option을 할인하지 않았다.", first_signal="인수 station revenue/EBITDA가 pro-forma guide의 90% 미만이거나 retrans growth가 reverse-comp 증가보다 느리고 net leverage가 두 정치주기 동안 줄지 않으면 12% yield rerating을 폐기한다.",
metrics=[("Normalized FCF yield", "약 21%", "12%", "후속 cash growth", "성공 방향"),("Target", "원문 가격 미복원", "$23", "exact 성과 없음", "미검증"),("Recent acquisitions", "약 $1.1bn", "consensus 반영", "2015~16 규모 확대", "성공 방향"),("Revenue", "$2.219bn 2015", "accretion", "$2.737bn 2016", "성공"),("Operating income", "2015 base", "증가", "$602.9m/+42.6% 2016", "성공")],
timeline=[("2012", "약 $1.1bn acquisitions", "estimate gap 형성"),("2013-01-14", "VIC Long", "21% yield·$23"),("2013~15", "station consolidation", "scale 확대"),("2015-FY", "revenue $2.219bn", "운영 base"),("2016-FY", "revenue $2.737bn", "accretion 확인"),("2016-FY", "operating income $602.9m", "현금엔진 성공"),("2019 이후", "Diamond capital allocation", "장기 별도 실패")],
claimdata=[("acquisition estimate gap", "$1.1bn 인수 FCF가 consensus에 덜 반영됐다.", "SQL catalyst·company guide", "closing·integration이 계획대로다.", "EBITDA<90% guide면 반증.", "2015~16 revenue·profit 급증", "성공", "closed-deal contribution을 consensus와 대조한다."),("retrans engine", "retrans가 광고 decline을 상쇄한다.", "subscriber-based fee 성장", "reverse-comp보다 빠르다.", "net retrans contribution 감소면 반증.", "2010년대 core driver", "성공", "gross retrans가 아니라 net contribution을 본다."),("local ad resilience", "local ad는 생각보다 sticky하다.", "local relationships", "digital substitution이 완만하다.", "non-political ad 지속 감소면 반증.", "단기 scale growth", "부분 성공", "cyclical과 secular를 분리한다."),("low maintenance capex", "EBITDA가 높은 비율로 FCF가 된다.", "station asset 특성", "spectrum·technology capex가 제한된다.", "capex/EBITDA 급등이면 반증.", "초기 FCF thesis 지지", "성공 방향", "FCF yield에는 true maintenance를 넣는다."),("12% yield rerating", "21% yield discount가 좁혀진다.", "peer와 estimate lag", "duration이 충분하다.", "cord-cutting 가속이면 반증.", "exact price 미검증", "미검증", "yield와 duration을 함께 본다."),("Long direction/entity", "raw Short/Diamond가 아니라 SBGI Long이다.", "$23 target·2013 법인", "동일 common 기준이다.", "bond/negative payoff 확인 시 반증.", "Sinclair common으로 교정", "성공", "ticker·법인·security를 날짜로 고정한다.")]),

I(id="8bdb5e43-ba08-4a61-8e15-7733116ba20d", date="2015-08-16", author="JSTC", ticker="SBGI", entity="Sinclair Broadcast Group, Inc.", group="sbgi55", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="12~18개월", filename="analysis/ideas/2015/2015-08-16_SBGI_long.md", link="https://www.valueinvestorsclub.com/idea/SINCLAIR_BROADCAST_GP__-CL_A/4023476089", desc=0, cat=67,
title="16~18% core FCF yield+spectrum option Long", verdict="core 현금흐름은 부분 성공·$2bn spectrum/double 핵심 실패", score=5.8, process=7.3,
summary="raw Short/Diamond mapping과 달리 potential double을 제시한 Sinclair common Long이다. core FCF yield 16%, growth investment 제외 18%를 9x FCF로 rerate해 50~65% upside를 만들고, management의 약 $2bn spectrum monetization을 추가 40~50% equity upside로 더했다.",
valuation="Base layer는 core FCF를 약 11% yield/9x로 정상화하는 50~65% upside다. 두 번째 layer는 spectrum $2bn pre-tax와 약 3% broadcast cash-flow sacrifice다. 실제 auction-dependent value는 clearing price·market·tax·repack cost의 확률분포여야 했는데 maximum-like estimate가 base에 가까이 들어갔다.",
actual="2017 FCC incentive auction에서 Sinclair가 받은 gross proceeds는 $310.8m이었다. 이는 $2bn의 약 15.5%이며 회사는 operations에 material change가 없다고 밝혔다. core retrans·정치광고와 방송 cash는 유지됐지만 double thesis의 큰 부분인 spectrum layer는 약 84% 작게 실현됐다.",
price="첨부 SQL에는 catalyst 67자만 있고 description·performance는 없다. 16/18% yield, 50~65%, 추가 40~50%와 $2bn/$310.8m은 thesis/event anchors다. exact return/IRR은 null이다.",
drivers="core 가치는 retrans·2016 정치광고·낮은 capex가 만들었지만 incremental upside는 spectrum clearing price가 좌우했다. 옵션이 공짜였는지보다 최대 추정치를 NAV에 얼마나 반영했는지가 성과를 결정했다.",
error="management의 $2bn 잠재값을 독립적인 Bear/Base/Bull로 분해하지 않았다. 세금·repack·timing·clearing-price sensitivity와 sacrifice되는 station cash를 차감하지 않아 optionality를 사실상 base-case 자산으로 바꿨다.", first_signal="auction stage별 clearing cost가 $1bn 이하 implied proceeds를 가리키거나 company bid exit가 늘면 spectrum layer를 $0.3~0.7bn base로 낮춘다. core FCF만으로 목표수익이 남지 않으면 position을 축소한다.",
metrics=[("Core FCF yield", "16%/18%", "약 11%", "core cash 유지", "부분 성공"),("Core upside", "저평가", "50~65%", "exact return 없음", "미검증"),("Spectrum", "$2bn E", "40~50% 추가", "$310.8m gross", "강한 실패"),("Realization", "100% 가정 근접", "auction 2Q16", "15.5% of estimate", "대실패"),("Political cycle", "2016 catalyst", "cash uplift", "2016 operating growth", "성공 방향")],
timeline=[("2015-08-16", "VIC Long", "16~18% yield"),("2016-H2", "정치광고 주기", "core catalyst"),("2016", "revenue·operating income 증가", "core 검증"),("2017-02", "auction 결과 발표", "$313m 예상"),("2017-07", "$310.8m 수취", "option miss 확정"),("2018-Q1", "잔여 deferred gain", "회계 인식"),("2019", "대형 RSN 인수", "capital allocation risk")],
claimdata=[("core FCF cheap", "16~18% yield는 과도하다.", "retrans·low capex", "duration이 충분하다.", "net retrans·FCF 감소면 반증.", "core cash는 유지", "부분 성공", "고 yield에는 duration을 붙인다."),("2016 political uplift", "정치주기가 cash를 높인다.", "even-year history", "core ad가 동시에 무너지지 않는다.", "비정치광고 급락이면 반증.", "2016 growth", "성공 방향", "정치광고는 normalized two-year 평균으로 본다."),("$2bn spectrum", "저사용 spectrum을 $2bn에 판다.", "management estimate", "clearing price·tax가 유리하다.", "implied proceeds<$1bn이면 반증.", "$310.8m gross", "강한 실패", "management 최대값을 base에 넣지 않는다."),("3% sacrifice", "cash-flow 손실은 3%뿐이다.", "channel sharing plan", "repack·reach 영향이 제한된다.", "운영 훼손/비용 증가면 반증.", "material operating change 없음", "성공", "option cost와 option value를 따로 검증한다."),("buyback/dividend", "core cash가 per-share value를 높인다.", "capital return capacity", "M&A보다 환원 우선이다.", "대형 비핵심 인수면 반증.", "후일 RSN 인수", "장기 실패", "owner cash와 capital allocator를 분리한다."),("Long direction/entity", "raw Short/Diamond가 아니라 SBGI Long이다.", "potential double payoff", "common equity 기준이다.", "bond/negative payoff면 반증.", "방향·법인 교정", "성공", "raw flag를 payoff로 감사한다.")]),

I(id="f35ee617-acdb-4fb7-b64b-3f989b2f7066", date="2017-07-21", author="ruby831", ticker="SBGI", entity="Sinclair Broadcast Group, Inc.", group="sbgi55", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="12~24개월", filename="analysis/ideas/2017/2017-07-21_SBGI_long.md", link="https://www.valueinvestorsclub.com/idea/SINCLAIR_BROADCAST_GP__-CL_A/4857707836", desc=0, cat=139,
title="Tribune pro-forma $59 merger Long", verdict="FCC gate·deal close 실패로 pro-forma valuation 무효", score=2.5, process=5.8,
summary="raw Short/Diamond가 아니라 Tribune acquisition을 전제로 $59와 70%+ upside를 제시한 Sinclair Long이다. 220+ stations, 108 markets, 72% household reach, pro-forma EBITDA 최소 $1.83bn과 FCF/share 약 $7에 8.5x를 적용했다.",
valuation="close 뒤 $1.83bn+ EBITDA×8.5x 또는 FCF/share 약 $7의 high-single-digit multiple로 $59를 계산했다. 올바른 event value는 `P(close)×close value+P(break)×standalone value-legal/reputation cost`다. 원문은 close case를 정교하게 만들었지만 FCC/DOJ·divestiture·candor gate와 break value를 충분히 가격화하지 않았다.",
actual="2018-07 FCC가 transaction 관련 misrepresentation/candor와 divestiture 구조를 Administrative Law Judge hearing으로 보냈다. 2018-08-09 Tribune은 merger를 종료하고 Sinclair를 상대로 소송을 제기했다. 거래가 닫히지 않아 $1.83bn EBITDA, synergies와 deleveraging bridge는 실현되지 않았다.",
price="현 SQL에는 catalyst 139자만 있고 description·performance는 없다. $59, 70%+, $1.83bn, 8.5x와 $7 FCF/share는 prior metadata anchors다. deal break를 정확 주가수익률로 바꾸지 않고 return/IRR은 null이다.",
drivers="결과를 결정한 것은 방송 cash-flow 숫자가 아니라 승인확률과 applicant conduct였다. close probability가 사실상 0으로 가면서 accretion model 전체가 사라졌고, standalone에는 legal·reputation·future M&A option 손실이 남았다.",
error="친화적 FCC와 deregulation 방향을 개별 거래구조 승인으로 외삽했다. divestiture buyer의 independence와 candor risk를 governance 변수로 넣지 않았고, close case의 숫자 정밀도가 낮은 확률추정을 가렸다.", first_signal="FCC/DOJ가 divestiture buyer의 real-party-in-interest 또는 disclosure candor를 문제 삼는 순간 P(close)를 50% 아래로 내린다. ALJ referral 가능성이 생기면 close case가 아니라 break liquidity와 legal cost로 재평가한다.",
metrics=[("Pro-forma EBITDA", "$1.83bn+", "close 후 실현", "거래 미종결", "실패"),("FCF/share", "약 $7", "deleveraging", "pro-forma 미실현", "실패"),("Target", "원문 가격 미복원", "$59/70%+", "exact 성과 없음", "실패 방향"),("Multiple", "8.5x", "rerating", "regulatory discount", "실패"),("Close gate", "높게 가정", "2017~18 approval", "FCC HDO·termination", "대실패")],
timeline=[("2017-05", "Tribune deal 발표", "event 시작"),("2017-07-21", "VIC Long", "$59 target"),("2017~18", "divestiture 구조 제시", "승인 gate"),("2018-07-16", "FCC chairman 우려", "first decisive break"),("2018-07", "Hearing Designation Order", "P(close) 급락"),("2018-08-09", "Tribune termination", "thesis 무효"),("2020-01", "litigation settlement", "후속 legal 종결")],
claimdata=[("Tribune close", "FCC/DOJ가 거래를 승인한다.", "deregulation·divestiture", "구조와 candor가 acceptable하다.", "ALJ/HDO면 반증.", "FCC HDO·termination", "대실패", "M&A Long은 close probability부터 쓴다."),("$1.83bn EBITDA", "결합 후 EBITDA가 최소 $1.83bn이다.", "company pro-forma·synergy", "deal close·retention이 전제다.", "close 실패면 무효.", "미실현", "실패", "conditional earnings에 확률을 곱한다."),("8.5x value", "scale broadcaster는 8.5x를 받는다.", "peer/deal comps", "governance discount가 없다.", "규제·평판 discount면 반증.", "discount 확대", "실패", "multiple은 governance와 event state별로 둔다."),("deregulation tailwind", "friendly FCC가 consolidation을 돕는다.", "policy direction", "applicant conduct가 문제없다.", "candor issue면 반증.", "friendly 환경에서도 차단", "실패", "정책 방향과 개별 승인을 구분한다."),("deleveraging", "정치광고·asset sales가 debt를 줄인다.", "2018 cash·real estate", "거래가 닫힌다.", "break cost/무종결이면 반증.", "거래 전제 소멸", "실패", "deleveraging source의 선행조건을 본다."),("Long direction/entity", "raw Short/Diamond가 아니라 SBGI Long이다.", "$59 positive target", "Sinclair common 기준이다.", "short/bond payoff면 반증.", "방향·법인 교정", "성공", "방향교정과 thesis 성공은 별개다.")]),

I(id="7a3adc85-2f3c-4244-a076-98fc1553101c", date="2018-08-09", author="JSTC", ticker="SBGI", entity="Sinclair Broadcast Group, Inc.", group="sbgi55", raw_short=True, direction="Short", entry="원문 가격 미복원", horizon="6~18개월", filename="analysis/ideas/2018/2018-08-09_SBGI_short.md", link=None, desc=0, cat=95,
title="Tribune break·governance overhang Short", verdict="legal size·timing은 실패, capital-allocation 경고는 후일 적중", score=5.3, process=7.2,
summary="raw Short와 실제 방향은 일치하지만 Diamond mapping은 틀렸고 대상은 Sinclair common이다. Tribune이 거래를 종료·소송한 당일 legal damages, $1bn buyback의 실질성 부족, regulator credibility와 future M&A franchise 훼손을 근거로 standalone Short 또는 peer hedge를 제안했다.",
valuation="Short payoff는 claim amount가 아니라 expected settlement×지급시기, buyback 실행 cash, standalone broadcast FCF와 reputation이 future deal multiple에 주는 영향을 합쳐야 한다. 소송이 길어져도 현금손실이 작거나 주가에 선반영되면 carry·squeeze가 커진다.",
actual="litigation은 2020까지 이어졌지만 $1bn 현금배상으로 끝나지 않았다. Sinclair는 후속 repurchase를 실제 수행했고 2019에는 $10.6bn 가치의 RSN 인수를 발표해 M&A capacity가 완전히 사라지지 않았다. 다만 바로 그 aggressive capital allocation이 Diamond 파산과 parent settlement로 이어져 governance 우려는 다른 경로로 적중했다.",
price="첨부 SQL에는 95자 catalyst만 있고 description·performance는 없다. intraday 반응·후속 2019 반등을 exact short return으로 계산하지 않는다. borrow, cover date와 distribution이 없어 return/IRR은 null이다.",
drivers="단기 Short의 직접 catalyst였던 cash damages는 과대평가됐고 buyback·새 deal이 squeeze를 만들 수 있었다. 장기 손실은 Tribune lawsuit보다 management가 core 방송 현금을 고레버리지 RSN에 재투자한 데서 발생했다. 후일의 다른 실패로 원 Short timing을 사후 정당화하면 안 된다.",
error="complaint claim과 expected cash settlement를 혼동하고, event break 당일 이미 반영된 damage와 앞으로 새로 발생할 damage를 분리하지 않았다. buyback ability와 대체 M&A, borrow/carry·relative hedge 실행을 수치화하지 않았다.", first_signal="소송에서 현금 damages probability가 낮아지거나 분기 buyback이 authorization의 10% 이상 실행되고 새 accretive deal financing이 열리면 cover한다. governance thesis는 별도 장기 관찰로 넘긴다.",
metrics=[("Legal damages", "최대 약 $1bn 우려", "equity hit", "$1bn cash 배상 아님", "실패"),("Buyback", "$1bn authorization", "실행 제약", "후속 repurchase 실행", "부분 실패"),("M&A franchise", "훼손", "future deals 감소", "2019 $10.6bn RSN deal", "단기 실패"),("Governance", "공격적 배분", "discount 확대", "Diamond value destruction", "장기 성공"),("Short timing", "deal-break 당일", "6~18개월", "2019 반등 구간", "혼합")],
timeline=[("2018-07", "FCC HDO", "deal risk 현실화"),("2018-08-09", "Tribune termination·lawsuit", "Short 시작"),("2018-08", "$1bn buyback authorization", "squeeze/credibility 변수"),("2019-05", "$10.6bn RSN deal", "M&A franchise 지속"),("2020-01", "Tribune litigation settlement", "cash-damage thesis 약화"),("2020~22", "Diamond restructuring", "governance 우려 현실화"),("2023-03", "Diamond Chapter 11", "다른 경로의 장기 적중")],
claimdata=[("deal is dead", "Tribune 거래는 되살아나지 않는다.", "termination filing", "새 합의가 없다.", "deal revival이면 반증.", "종료 확정", "성공", "종료 사실과 추가 downside를 분리한다."),("$1bn damages", "큰 cash damages가 equity를 훼손한다.", "Tribune complaint", "claim이 settlement로 실현된다.", "low-cash settlement면 반증.", "$1bn cash 배상 아님", "실패", "claim amount에 probability·time을 곱한다."),("buyback empty", "$1bn authorization은 실행하기 어렵다.", "leverage·legal overhang", "현금보존이 우선이다.", "material repurchase면 반증.", "실제 repurchase", "부분 실패", "authorization와 execution을 분기별로 본다."),("M&A franchise lost", "규제평판이 future deals를 막는다.", "FCC candor issue", "seller/lender도 회피한다.", "새 대형 deal이면 반증.", "2019 RSN 인수", "단기 실패", "option impairment와 완전소멸을 구분한다."),("capital allocation risk", "owner-control이 나쁜 다음 거래를 부를 수 있다.", "aggressive Tribune structure", "governance가 바뀌지 않는다.", "deleveraging·환원 우선이면 반증.", "Diamond 파산 경로", "장기 강한 성공", "governance는 반복행동으로 검증한다."),("Short direction/entity", "실제 Sinclair common Short다.", "standalone short 문구", "borrow와 hedge가 가능하다.", "positive target이면 반증.", "raw direction 일치·entity 교정", "성공", "security resolve 후 성과를 본다.")]),

I(id="82eaec90-3559-4161-a7d7-7f12b8506646", date="2020-02-05", author="burlap", ticker="SBGI", entity="Diamond Sports Group, LLC", group="diamond55", raw_short=True, direction="Short", entry="약 95 cents", horizon="12~36개월", filename="analysis/ideas/2020/2020-02-05_Diamond_Sports_2027_bond_short.md", link=None, desc=0, cat=287, contest=True, security="6.625% senior unsecured notes due 2027",
title="Diamond 6.625% 2027 unsecured bond Short", verdict="2023 Chapter 11·대규모 debt elimination으로 credit thesis 강한 성공", score=9.8, process=9.8,
waterfall="Affiliate-fee·광고 현금에서 rights payment·production·opex·cash interest·필수 capex를 빼고, first-lien/secured debt와 DIP·administrative claim을 먼저 지급한다. 남는 enterprise recovery를 unsecured face에 배분하며 Sinclair parent support는 계약상 보장되지 않는다.",
summary="raw ticker는 SBGI지만 실제 security는 Diamond Sports 6.625% unsecured notes due 2027 Short @ 약 95다. Base 80, short에 불리한 case 104, severe case insolvency를 두고 acquisition LTV가 80%에서 100%+로 악화됐으며 FCF/debt<5%, DISH blackout·subscriber churn과 rights-cost escalator가 unsecured par을 위협한다고 봤다.",
valuation="95에서 80은 15-point gross downside지만 coupon carry·borrow·cover date가 필요하다. 핵심은 maturity yield가 아니라 current enterprise value가 secured+unsecured debt와 fixed rights commitments를 덮는지다. >100% LTV이면 시간이 많아도 unsecured recovery는 rights renegotiation·carriage·priority에 민감하다.",
actual="2020 2027 unsecured를 12.75% secured debt로 바꾸는 exchange가 시작됐고 2022 추가 liability management가 이어졌다. Diamond는 2023-03-14 Chapter 11을 신청해 약 $8bn debt elimination을 추진했고 2025 emergence 때 debt는 대폭 축소됐다. par-credit가 principal impairment asset으로 바뀌었다.",
price="첨부 SQL에는 catalyst 287자만 있고 description·performance는 없다. 95/80/104와 Chapter 11·debt elimination은 thesis/event anchors다. coupon, trade price, borrow/cover를 복원하지 못해 exact short return/IRR은 null이다.",
drivers="수익 방향을 만든 것은 EBITDA가 아직 positive인지가 아니라 subscriber revenue duration보다 rights cost와 debt가 길고 고정돼 있었다는 점이다. non-recourse는 parent를 보호하지만 Diamond unsecured에는 support 부재를 뜻했고, liability management가 priority를 더 악화시켰다.",
error="Base 80은 강한 credit deterioration에 비해 보수적이었으나 timing은 exchange·liquidity runway에 따라 길어질 수 있었다. team별 rights termination value, secured priming capacity와 restructuring recovery waterfall을 더 세밀히 모델링해야 했다.", first_signal="DISH blackout 지속, 다른 주요 MVPD renewal 악화, FCF/debt<5% 유지와 secured exchange 제안 중 하나가 발생하면 insolvency weight를 높인다. 반대로 subscriber stabilization·rights reset·LTV<80%가 확인되면 cover한다.",
metrics=[("Bond", "6.625% 2027 @95", "Base 80", "Chapter 11", "강한 성공"),("LTV", ">100%", "coverage 악화", "대규모 debt elimination", "강한 성공"),("FCF/debt", "<5%", "deleveraging 불충분", "restructuring 지속", "성공"),("Distribution", "DISH blackout", "추가 renewal risk", "carriage pressure 지속", "성공"),("Priority", "unsecured", "priming 위험", "secured exchanges", "강한 성공")],
timeline=[("2019-08", "RSN acquisition close", "약 $10.6bn top-tick"),("2020-02-05", "bond Short", "95→80"),("2020-06", "12.75% secured exchange", "priority deterioration"),("2021~22", "subscriber·renewal 압력", "cash duration 감소"),("2022", "추가 debt exchange", "distress 심화"),("2023-03-14", "Chapter 11", "insolvency 현실화"),("2024~25", "plan·emergence", "debt 대폭 제거")],
claimdata=[("top-tick LTV", "purchase 뒤 LTV가 100%를 넘는다.", "carriage loss·lower asset value", "rights value가 회복되지 않는다.", "LTV<80% 회복이면 반증.", "Chapter 11·debt elimination", "강한 성공", "credit LTV는 current value로 갱신한다."),("FCF is insufficient", "positive FCF라도 debt의 5% 미만이면 안전하지 않다.", "FCF/debt<5%", "rights·interest가 경직적이다.", "sustained deleveraging이면 반증.", "restructuring", "성공", "positive FCF와 debt service capacity를 구분한다."),("distribution erosion", "DISH drop과 renewals가 structural하다.", "blackout·cord-cutting", "다른 MVPD도 강경해진다.", "subscriber 안정·renewal 개선이면 반증.", "carriage pressure 지속", "성공", "revenue contract duration을 본다."),("rights escalator", "sports-rights cost가 revenue보다 느리게 내려간다.", "long-term contracts", "termination/renegotiation이 어렵다.", "cost reset이 revenue decline을 앞서면 반증.", "Chapter 11에서 계약조정", "성공", "fixed cost duration을 debt처럼 본다."),("unsecured mispricing", "95의 unsecured는 priority risk를 반영하지 못한다.", "secured debt ahead·exchange capacity", "priming이 가능하다.", "asset coverage 충분 시 반증.", "secured exchanges·principal impairment", "강한 성공", "liability management 전 priority를 그린다."),("Short security", "SBGI common이 아니라 Diamond 2027 bond Short다.", "coupon/maturity/payoff", "동일 instrument를 추적한다.", "common thesis면 반증.", "security 교정", "성공", "issuer·security·seniority를 분리한다.")]),

I(id="7503adc8-4558-4dd3-bfb5-dcfe0e6735a6", date="2020-12-07", author="taiidea", ticker="SBGI", entity="Sinclair Broadcast Group, Inc.", group="sbgi55", raw_short=True, direction="Long", entry="high-$20s", horizon="12~24개월", filename="analysis/ideas/2020/2020-12-07_SBGI_long.md", link="https://www.valueinvestorsclub.com/idea/Sinclair_Broadcast_Group/4490840228", desc=0, cat=1721,
title="non-recourse Diamond·2.6x core EBITDA Long", verdict="$99.17와 ring-fence thesis 강한 실패", score=2.8, process=6.3,
summary="raw Short/Diamond가 아니라 Sinclair common에서 Dec-2021 $99.17와 243% upside를 제시한 Long이다. Diamond leverage 12.7x와 legacy Sinclair 1.6x를 분리하고, parent guarantee가 없는 debt silo, restricted-payment cash extraction, 2.6x 2022E core EBITDA, Bally sports-betting synergy와 Diamond restructuring을 value-unlock으로 봤다.",
valuation="combined/adjusted business에 NXST 7.8x multiple, Diamond debt haircut, tax shield, sports betting과 parent cash extraction을 합산해 $99.17을 만들었다. 여러 optionality가 cord-cutting·rights-cost·affiliate litigation이라는 같은 failure mode에 노출됐는데 독립적인 upside처럼 더해졌다.",
actual="legal non-recourse는 형식상 맞았지만 economic ring-fence는 실패했다. Sinclair는 2021-11 Diamond A/R facility lender obligations 약 $184.4m을 인수했고, 2023 Diamond Chapter 11 뒤 제기된 affiliate litigation을 끝내기 위해 2024 $495m cash settlement에 합의했다. $99.17 target은 실현되지 않았다.",
price="현 SQL에는 catalyst 1,721자만 있고 description·performance는 없다. high-$20s·$99.17·243%와 $184.4m/$495m은 prior metadata/event anchors다. exact return/IRR은 null이다.",
drivers="손실은 Diamond debt를 직접 보증해서가 아니라 ownership·service·preferred·receivable·reputation과 affiliate transfer가 parent cash를 다시 subsidiary에 연결했기 때문이다. betting/restructuring option은 core RSN economics 붕괴와 같은 원인에 동조했다.",
error="legal entity map을 cash-flow·incentive·litigation map과 동일시했다. restricted-payment capacity를 upside로 잡으면서 fraudulent-transfer/clawback을 충분히 차감하지 않았고, sports betting·tax·multiple rerating의 높은 상관관계를 무시했다.", first_signal="parent가 Diamond receivable/working-capital을 매입하거나 affiliate fee·preferred·management payment가 정상계약을 벗어나면 ring-fence를 폐기한다. DTC/betting revenue가 rights-cost decline을 상쇄하지 못하면 optionality를 zero로 둔다.",
metrics=[("Target", "high-$20s", "$99.17/243%", "target 미실현", "강한 실패"),("Core multiple", "2.6x 2022E EBITDA", "NXST 7.8x", "rerating 차단", "실패"),("Leverage split", "Diamond 12.7x/core 1.6x", "legal ring-fence", "economic contagion", "실패"),("Parent support", "제한적 가정", "cash extraction", "$184.4m A/R support", "반대"),("Legal settlement", "낮게 반영", "limited downside", "$495m cash", "강한 실패")],
timeline=[("2019-08", "RSN acquisition close", "debt silo 형성"),("2020-12-07", "VIC Long", "$99.17 target"),("2021-11", "$184.4m A/R facility obligation 인수", "first ring-fence break"),("2022", "Diamond exchange", "distress 지속"),("2023-03", "Diamond Chapter 11", "restructuring 실패"),("2023-07", "affiliate litigation", "parent exposure"),("2024-01~03", "$495m settlement", "economic contagion 확정")],
claimdata=[("legal non-recourse", "Diamond debt는 parent에 직접 recourse가 없다.", "financing documents", "intercompany exposure도 제한된다.", "parent support/claim이면 반증.", "형식상 맞음", "법률 성공", "법적 보증과 경제적 노출을 구분한다."),("economic ring-fence", "Diamond 실패가 SBGI common을 거의 훼손하지 않는다.", "separate debt silo", "affiliate transfer·소송이 작다.", "new money·settlement면 반증.", "$184.4m+$495m 경로", "강한 실패", "entity map과 cash map을 함께 그린다."),("cash extraction", "Diamond cash가 parent로 이동한다.", "restricted-payment capacity", "solvency·fraudulent transfer 문제가 없다.", "reverse support/claim이면 반증.", "parent가 오히려 cash 지급", "실패", "basket capacity는 distributable value가 아니다."),("core rerating", "2.6x core EBITDA가 7.8x로 간다.", "peer multiple", "core duration·governance가 유사하다.", "cord-cutting·legal discount면 반증.", "discount 지속", "실패", "peer multiple은 duration과 governance를 맞춘다."),("betting synergy", "RSN이 sportsbook CAC channel이 된다.", "Bally partnership", "규제·conversion·rights가 유리하다.", "material revenue 부재면 반증.", "core decline 상쇄 못함", "실패", "adjacency는 KPI 전에는 option이다."),("Long direction/entity", "raw Short/Diamond가 아니라 SBGI common Long이다.", "$99.17 positive target", "same security", "bond/short payoff면 반증.", "방향·법인 교정", "성공", "direction audit와 investment verdict를 분리한다.")]),

I(id="32a51968-bfbf-4fd9-bd22-f5dd7590f050", date="2022-08-30", author="phn19", ticker="SBGI", entity="Sinclair Broadcast Group, Inc.", group="sbgi55", raw_short=True, direction="Long", entry="<$24", horizon="2~4년", filename="analysis/ideas/2022/2022-08-30_SBGI_long.md", link="https://www.valueinvestorsclub.com/idea/SINCLAIR_BROADCAST_GP__-CL_A/5230006850", desc=0, cat=151,
title="Diamond=0·25~30% core FCF yield Long", verdict="framework 개선에도 Diamond<0와 runoff duration으로 실패", score=4.5, process=8.0,
summary="raw Short/Diamond와 달리 <$24의 Sinclair common Long이다. 2020 글보다 개선돼 Diamond equity는 zero로 두고 core broadcast만 평가했다. non-political levered FCF $400~500m, political $500~600m, 평균 25~30% yield와 약 6x core EBITDA를 근거로 buyback과 optional assets를 제시했다.",
valuation="정상화 2년 FCF에 finite duration을 붙여야 하지만 원문은 높은 yield와 6x EBITDA를 중심으로 봤다. BALY warrants $2~3/share, tax asset 최대 $1.1bn, spectrum 최대 $1.7bn, JV $3/share를 별도 option으로 더했다. 핵심 downside는 Diamond=0가 아니라 affiliate claim을 반영한 Diamond<0다.",
actual="2023-03 Diamond가 Chapter 11에 들어가고 2023-07 Sinclair 관련 $1.5bn litigation이 제기됐다. 2024 global settlement에서 Sinclair는 $495m cash를 지급했고 2025 emergence에서 Sinclair equity interest는 소멸했다. core 방송은 cash를 냈지만 cord-cutting과 법적 reserve가 multiple을 막았다.",
price="첨부 SQL에는 151자 catalyst만 있고 description·performance는 없다. <$24, 25~30% yield, FCF $400~600m와 $495m은 anchors다. exact return/IRR은 null이다.",
drivers="2020보다 좋은 점은 Diamond upside를 제거한 것이지만 floor를 zero로 둔 것이 남은 오류였다. runoff-like FCF의 존속기간이 짧아지면 30% yield도 낮은 가치일 수 있고, buyback은 debt·legal reserve와 같은 cash를 경쟁했다.",
error="fraudulent conveyance를 인식했지만 claim size·probability·legal duration을 충분히 reserve하지 않았다. FCF를 perpetuity-like multiple로 보면서 가입자·net retrans·affiliate fee의 finite-life decay를 명시적으로 DCF하지 않았다.", first_signal="Diamond affiliate claim이 $250m을 넘거나 parent cash 지급 가능성이 높아지면 zero floor를 negative로 바꾼다. core net retrans contribution과 non-political FCF가 2년 평균 10% 이상 감소하면 6x가 아니라 runoff DCF를 쓴다.",
metrics=[("Entry", "<$24", "rerating", "exact 성과 없음", "실패 방향"),("Core FCF yield", "25~30%", "cash harvest", "duration 압력", "부분"),("Core FCF", "$400~500m/$500~600m", "유지", "cash generative이나 감소위험", "부분"),("Diamond value", "$0", "ring-fenced", "-$495m settlement 포함", "강한 실패"),("Optional assets", "$2~3+$1.1bn+$1.7bn", "monetization", "near-term 미실현", "실패")],
timeline=[("2022-08-30", "VIC Long", "<$24·25~30% yield"),("2022-H2", "Diamond restructuring", "zero floor 시험"),("2023-03", "Chapter 11", "equity zero 현실화"),("2023-07", "$1.5bn litigation", "negative value risk"),("2024-01", "global settlement 발표", "$495m"),("2024-03", "court approval", "parent cash outflow"),("2025-01", "Diamond emergence", "Sinclair interest 소멸")],
claimdata=[("Diamond non-recourse", "funded debt 대부분은 parent 책임이 아니다.", "debt documents", "affiliate exposure가 작다.", "large claim/settlement면 반증.", "직접보증은 제한", "법률 성공", "funded debt와 affiliate claim을 분리한다."),("Diamond equals zero", "sub를 zero로 두면 충분히 보수적이다.", "equity impairment 인식", "negative parent value가 없다.", "cash settlement면 반증.", "$495m 지급", "강한 실패", "distressed sub의 floor는 음수일 수 있다."),("clawback manageable", "fraudulent-transfer risk는 제한적이다.", "known transfers·preferred", "settlement가 작다.", "claim>$250m이면 반증.", "$1.5bn suit/$495m settlement", "실패", "legal scenario를 amount×probability로 만든다."),("core FCF duration", "25~30% yield cash가 충분히 오래 간다.", "retrans·political cash", "cord-cutting보다 price가 빠르다.", "2년 평균 FCF -10%면 반증.", "duration discount 지속", "부분 실패", "고 yield는 finite-life 연금일 수 있다."),("buyback accretion", "낮은 가격 repurchase가 per-share value를 높인다.", "cash generation", "debt/legal reserve가 충분하다.", "external cash need면 반증.", "$495m settlement와 경쟁", "혼합", "환원 전 contingent liability를 뺀다."),("option assets", "warrant·tax·spectrum이 추가 upside다.", "asset inventory", "monetization 가능하다.", "3년 내 미현금화면 제거.", "near-term catalyst 아님", "실패", "옵션은 cash date·tax를 붙인다.")]),

I(id="a45e9d1d-6355-48f2-800c-d6d89c2462a2", date="2003-12-06", author="pgu103", ticker="STMP", entity="Stamps.com Inc.", group="stmp55", raw_short=True, direction="Long", entry="약 $5.52 implied", horizon="2~5년", filename="analysis/ideas/2003/2003-12-06_STMP_long.md", link="https://www.valueinvestorsclub.com/idea/Stamps.com/8567348885", desc=0, cat=109,
title="NetStamps product inflection·3.2x LTV/CAC Long", verdict="2004 unit/revenue inflection과 2021 strategic value 강한 성공·exact IRR 미검증", score=9.5, process=9.5,
summary="raw Short와 달리 downside limited·huge option value를 주장한 Long이다. cash $165m/$3.63 per share, debt 없음, EV $86m/$1.89 per share에서 313k users, CAC $69, Power Plan NPV $220, paid monthly churn 1.8%를 근거로 NetStamps·shipping labels와 Microsoft Office distribution이 product-market fit을 바꾼다고 봤다.",
valuation="cash/share $3.63+EV/share $1.89로 implied price 약 $5.52다. Power cohort의 LTV/CAC는 $220/$69≈3.2x였고 existing subscriber cash run-rate는 약 $5.8~8m으로 EV의 11~15x였다. cash는 burn·소송·마케팅을 차감해야 하지만 positive cohort economics가 재투자 가치를 만들었다.",
actual="2004 revenue는 $21.2m에서 $38.1m으로 약 80% 증가했고 gross customers acquired는 140k에서 241k로 늘었으며 postage printed도 53% 증가했다. 장기적으로 e-commerce shipping platform으로 확장했고 2021 Thoma Bravo가 $330/share cash, 약 $6.6bn에 인수했다.",
price="현 SQL에는 catalyst 109자만 있고 description·performance는 없다. $5.52 implied와 $330 cash는 18년 떨어진 thesis/event anchors다. 중간 buyback·acquisitions·배당·holding path가 없어 이를 60x 또는 특정 IRR로 저장하지 않고 exact return/IRR은 null이다.",
drivers="진짜 turnaround는 lease·headcount 축소가 아니라 주소 없이 일반 우표처럼 쓰는 NetStamps가 utility를 높이고 CAC 대비 cohort NPV가 양수가 된 것이다. cash runway가 실험을 버티게 했고 Office/eBay/SMB distribution이 scalable channel을 제공했다.",
error="NPV는 churn·gross margin·discount rate와 support cost에 민감하고 trial churn 20%와 paid churn 1.8%를 섞으면 크게 왜곡된다. Microsoft distribution의 conversion과 patent litigation을 option으로 두되 base에 과도하게 넣지 말았어야 한다.", first_signal="Power-plan share가 60% 아래로 떨어지거나 paid monthly churn>2.5%, blended CAC>$100, cohort contribution payback>18개월이면 marketing scale-up을 중단하고 cash floor에서 burn reserve를 늘린다.",
metrics=[("Cash/EV per share", "$3.63/$1.89", "downside+option", "2004 growth runway", "성공"),("Power LTV/CAC", "$220/$69=3.2x", ">3x 유지", "customer growth", "성공 방향"),("Paid churn", "1.8% monthly", "≤2%", "장기 subscription 확장", "성공 방향"),("Revenue", "$21.2m 2003", "inflection", "$38.1m 2004", "강한 성공"),("Gross acquisitions", "140k 2003", "marketing scale", "241k 2004", "강한 성공")],
timeline=[("1999", "IPO·과투자", "dot-com legacy"),("2001", "management/cost reset", "cash burn 축소"),("2002", "USPS NetStamps approval", "product unlock"),("2003-12-06", "VIC Long", "약 $5.52 implied"),("2004", "revenue $38.1m·customers 241k", "unit inflection"),("2005 이후", "shipping/e-commerce 확장", "distribution option 실현"),("2021-07", "$330 Thoma Bravo deal", "장기 strategic endpoint")],
claimdata=[("NetStamps utility", "주소 없이 출력하는 postage가 product-market fit을 바꾼다.", "USPS approval·lower friction", "customers가 반복 사용한다.", "activation/usage 정체면 반증.", "2004 postage +53%", "강한 성공", "turnaround는 product utility 변화부터 본다."),("Power LTV/CAC", "$69 CAC로 $220 NPV를 산다.", "cohort model", "churn·margin이 유지된다.", "CAC>$100·churn>2.5%면 반증.", "customer acquisition 확대", "성공 방향", "회계손실 아래 incremental unit economics를 본다."),("paid churn", "trial 후 monthly churn 1.8%다.", "paid cohorts", "cohort 정의가 안정적이다.", "2.5% 초과면 반증.", "subscription category 성장", "성공 방향", "trial과 paid churn을 분리한다."),("marketing scale", "양수 unit economics에 spend를 늘리면 성장한다.", "140k acquisition base", "channel saturation이 멀다.", "CAC 상승·payback 악화면 반증.", "241k customers 2004", "강한 성공", "성장률보다 marginal cohort return을 본다."),("distribution option", "Office·eBay·SMB가 저비용 channel이다.", "integration·shipping labels", "conversion과 retention이 높다.", "partner traffic이 paid user로 안 바뀌면 반증.", "e-commerce shipping 확장", "성공 방향", "distribution은 CAC 변화로 측정한다."),("cash/downside", "$165m cash·무차입이 시행착오를 버틴다.", "balance sheet", "burn·소송이 제한된다.", "cash burn 재가속이면 반증.", "turnaround runway 제공", "성공", "cash floor에는 use-of-cash를 붙인다.")]),
]


def idea_sources(idea):
    raw = m.S(
        "첨부 SQL catalyst / prior curated metadata",
        idea["link"],
        "VIC_IDEAS(4).sql / VIC / repository prior overlay",
        idea["date"],
        f"idea_id·catalyst {idea['cat']} chars·description absent; date·author·raw flag·원문 anchor는 prior overlay 대조",
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
    text = text.replace("Batch 046 canonical report.", "Batch 055 canonical report.")
    text = text.replace("### Common equity cash waterfall", "### Security cash waterfall")
    text = text.replace(generic, idea["waterfall"])
    text = text.replace(
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |",
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |\n| 실제 Security | **{idea['security']}** |",
    )
    text = text.replace(
        f"`ATH`를 회사로 보지 말고 {idea['entity']} 법인·exchange·날짜로 고정한다.",
        f"`{idea['ticker']}`를 단일 회사로 보지 말고 {idea['entity']} 법인·날짜·실제 security로 고정한다.",
    )
    text = text.replace(
        "원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.",
        "원문·metadata: **C** — 첨부 SQL에는 Batch 055 catalyst만 있고 description은 0건이다. date·author·raw flag·원문 수치는 prior curated overlay로 provenance를 분리했다.",
    )
    text = text.replace(
        "기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.",
        "기업·사건: **A/B** — SEC·FCC·회사·법원/구조조정 자료로 segment 결과와 terminal event를 검증했다.",
    )
    text = text.replace(
        "가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
        "가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. 거래가·채권 사건을 exact return으로 바꾸지 않고 return/IRR을 null로 유지했다.",
    )
    return text


def payload():
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(IDEAS)
    finally:
        m.idea_sources = old
    out["batch"] = 55
    out["title"] = "Rosetta Stone / Sinclair / Diamond Sports / Stamps.com — Asset Proof, Capital Allocation and Credit Waterfall V9"
    null_keys = (
        "perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y",
        "idea_return_1y", "idea_return_3y", "idea_return_5y",
    )
    for idea, master, post in zip(IDEAS, out["ideas_master"], out["postmortems"]):
        master["security_ko"] = idea["security"]
        master["performance_available"] = 0
        master["contest_winner"] = int(idea["contest"])
        master["auto_tag_status_ko"] = "current SQL catalyst 감사·entity/direction/security 수동교정·성과 null"
        for key in null_keys:
            master[key] = None
        post["research_direction_ko"] = f"{idea['direction']} / {idea['security']}"
        post["research_status_ko"] = "SQL catalyst·prior metadata·공식 filings 검증; description/performance COPY 부재로 exact return null"
        post["confidence"] = 0.92 if idea["link"] else 0.86
    return out


def make_index():
    rows = []
    for n, idea in enumerate(IDEAS, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['ticker']} | {idea['entity']} | {raw}→**{idea['direction']}** | {idea['security']} | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 055 — Rosetta Stone / Sinclair / Diamond Sports / Stamps.com — V9 Index", "",
        f"> Research as-of {ASOF}. Batch 054 다음 10건이다. 10 idea = 10 canonical reports이며 첨부 SQL에 없는 description·성과값을 만들지 않았다.", "",
        "## 0. 배치 결론", "",
        "RST 2건은 Lexia의 segment proof가 9개월 내 strategic sale로 전환된 성공이다. Sinclair 6건은 retrans·M&A로 시작한 고 FCF thesis가 spectrum 과대평가, Tribune 규제실패, Diamond capital allocation로 어떻게 무너졌는지 보여준다. Diamond bond Short는 같은 asset을 common narrative가 아니라 priority·LTV·계약 duration으로 봐 가장 강했다. Stamps.com은 비용절감보다 product utility와 3.2x LTV/CAC가 진짜 turnaround였던 사례다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | Raw ticker | 실제 회사 | raw→연구 방향 | 실제 security | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|---|---|", *rows, "",
        "## 2. SQL / Entity / Direction / Security Audit", "",
        "첨부 `VIC_IDEAS(4).sql`에는 catalyst·companies·descriptions COPY만 있고 ideas·performance COPY는 없다. Batch 055의 catalyst 10건은 모두 확인됐지만 description은 0건이다. exact return/IRR은 모두 null이다. raw direction 오류는 8건이며, raw `Diamond Sports`를 Sinclair parent common으로 교정한 entity 오류는 6건이다. 2020-02 아이디어는 SBGI common이 아니라 Diamond 6.625% 2027 unsecured bond Short다.", "",
        "## 3. Rosetta Stone — hidden asset에서 cash sale로", "",
        "2019-10 글은 $16.90·EV $404m에서 Lexia $600~800m, 90% recurring, 100%+ retention과 strategic review를 연결했다. 2019-12 글은 buyer 이름보다 district distribution·cross-sell가 만드는 private 4~6x bookings economics를 봤다. 실제 2020 Cambium/Veritas가 $30 cash·약 $792m equity value에 인수했다. 사건은 강한 성공이지만 exact holding return은 별도 데이터가 없어 null이다.", "",
        "## 4. Sinclair — cash engine보다 capital allocator", "",
        "| 시점 | 핵심 논지 | 실제 검증 | 판정 |", "|---|---|---|---|",
        "| 2013 | $1.1bn 인수 estimate gap·21% FCF yield | 2016 revenue +23.3%·operating income +42.6% | 성공 방향 |",
        "| 2015 | 16~18% core yield+$2bn spectrum | $310.8m, 추정의 15.5% | 부분/option 실패 |",
        "| 2017 | Tribune close·$59 | FCC HDO·termination | 강한 실패 |",
        "| 2018 Short | legal damages·buyback 회의·governance | damages 과대, 후일 Diamond 우려 적중 | 혼합 |",
        "| 2020 Long | non-recourse·$99.17 | $184.4m support·$495m settlement | 강한 실패 |",
        "| 2022 Long | Diamond=0·25~30% core FCF yield | Diamond<0·runoff duration | 실패 |", "",
        "## 5. Diamond credit — 같은 asset, 더 좋은 security lens", "",
        "2020 bond Short는 95의 unsecured를 80 base로 보고 >100% LTV, FCF/debt<5%, DISH blackout, rights escalator와 secured priming을 추적했다. 2023 Chapter 11과 대규모 debt elimination은 positive FCF가 par recovery를 보장하지 않음을 확인했다. non-recourse는 parent equity 방화벽일 수 있어도 subsidiary unsecured의 보호가 아니다.", "",
        "## 6. Stamps.com — product-first turnaround", "",
        "현금 $165m보다 중요한 것은 NetStamps가 usage friction을 제거하고 $69 CAC 대비 $220 Power-plan NPV, monthly paid churn 1.8%를 만들었다는 점이다. 2004 revenue는 $21.2m→$38.1m, gross customer acquisitions는 140k→241k로 늘었다. 2021 $330 cash takeout은 장기 strategic endpoint지만 중간 경로 없이 원 논지의 IRR로 만들지 않았다.", "",
        "## 7. 공통 투자 교훈", "",
        "1. hidden asset는 bookings·retention·standalone cost와 sale route로 증명한다.\n2. buyer 이름보다 여러 buyer에게 공통인 synergy를 본다.\n3. management optionality 최대값을 base NAV에 넣지 않는다.\n4. merger accretion보다 P(close)와 break value가 먼저다.\n5. claim amount와 expected settlement를 구분한다.\n6. non-recourse는 legal map이지 economic cash firewall이 아니다.\n7. distressed subsidiary floor는 zero보다 작을 수 있다.\n8. 30% FCF yield도 finite-life runoff면 싸지 않을 수 있다.\n9. credit는 positive EBITDA보다 LTV·priority·계약 duration을 본다.\n10. turnaround는 cost cut보다 incremental LTV/CAC 개선을 확인한다.", "",
        "## 8. 산출물", "",
        "- Payload: `data/curated/batch_055_rst_sbgi_stmp_deep_v7.json`\n- Wrapper: `analysis/batch_055_rst_sbgi_stmp_10.md`\n- Source packet: `data/curated/batch_055_source_packet.json`\n- Builder: `scripts/55_build_batch_055_v9.py`", "",
    ])


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 055 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or len(idea_sources(idea)) < 5:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(idea["filename"]).relative_to("analysis").as_posix() for idea in IDEAS]
    wrapper = "# Batch 055 — Rosetta Stone / Sinclair / Diamond Sports / Stamps.com V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit wrapper. [Batch 055 V9 Index](batch_055_v9_index.md).\n"
    (ROOT / "analysis/batch_055_rst_sbgi_stmp_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_055_v9_index.md").write_text(make_index(), encoding="utf-8")
    out = payload()
    (ROOT / "data/curated/batch_055_rst_sbgi_stmp_deep_v7.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {
        "batch": "055", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + prior curated metadata + official filings",
        "record_count": 10, "raw_descriptions_present": 0, "raw_catalysts_verified": 10,
        "current_attachment_performance_rows_found": 0, "legacy_overlay_performance_values_discarded": 0,
        "direction_corrections": 8, "entity_corrections": 6, "security_type_corrections": 1, "security_normalizations": 10,
        "performance_rule": "No performance COPY in current attachment; transaction prices and bankruptcy events are not exact returns",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"],
            "raw_direction": "Short" if i["raw_short"] else "Long", "research_direction": i["direction"], "security": i["security"],
            "description_chars": 0, "catalyst_chars": i["cat"], "performance_available": False,
            "canonical_report": i["filename"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_055_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10,
        "copy_tables_present": ["catalyst", "companies", "descriptions"], "idea_rows_in_attachment": 0,
        "raw_descriptions_present": 0, "raw_descriptions_absent": 10, "raw_catalysts_verified": 10,
        "description_chars_by_idea": {i["id"]: 0 for i in IDEAS},
        "catalyst_chars_by_idea": {i["id"]: i["cat"] for i in IDEAS},
        "performance_copy_present": False, "performance_rows_found": 0, "legacy_overlay_rows_nullified": 0,
        "note": "Current attachment controls. Batch 055 descriptions and performance are absent; prior metadata is lower provenance. Official filings control outcomes; events are not exact returns.",
    }
    (ROOT / "data/curated/batch_055_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(out[key]) for key in ("ideas_master", "postmortems", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
