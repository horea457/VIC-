#!/usr/bin/env python3
"""Build Batch 053 NERA / Owens Corning / Office Depot V9 artifacts."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-10"
spec = importlib.util.spec_from_file_location("batch46", ROOT / "scripts/46_build_batch_046_v9.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.ASOF = ASOF

m.BUSINESS.update({
    "nen": (
        "New England Realty Associates(NERA/NEN)는 Greater Boston의 아파트와 일부 상업용 부동산을 보유·운영하는 limited partnership이다. "
        "현금엔진은 `occupied units×rent-property opex-recurring capex-property mortgage interest·principal-G&A+NEN 지분만큼의 JV cash`다. "
        "Gross property NAV가 receipt holder 가치가 되려면 자산별 mortgage, unconsolidated JV debt, GP·related-party 비용과 세금을 차감해야 한다. "
        "NEN은 REIT의 의무배당 구조가 아니어서 현금을 인수·개선·buyback에 재투자할 수 있다. 2012년 3-for-1 forward split 뒤 한 depositary receipt는 Class A Unit의 1/30이다."
    ),
    "oc": (
        "Owens Corning은 당시 Roofing, Insulation, Composites 세 축의 건자재 제조사였다. 현금엔진은 "
        "`출하량×실현가격-asphalt·glass·energy·freight-plant fixed cost-SG&A-운전자본-capex-interest·tax`다. Roofing은 replacement/storm demand와 asphalt spread, "
        "Insulation은 housing starts·capacity utilization·price/cost, Composites는 산업생산·utilization·mix가 수익을 좌우한다. 높은 고정비 때문에 trough multiple보다 "
        "segment별 정상 출하·margin과 다음 downturn의 현금전환을 함께 봐야 한다. 2006 재편 뒤 asbestos 청구는 trust로 이전됐지만 영업 cycle은 그대로 common에 남았다."
    ),
    "odp": (
        "Office Depot은 당시 북미 retail superstore, Business Services/contract delivery, International/Viking direct 사업을 운영했다. 현금엔진은 "
        "`매장·계약고객·direct 매출×gross margin-store·warehouse·salesforce·delivery opex-inventory·receivable investment-remodel·new-store capex-interest·tax`다. "
        "재고와 매입채무는 성장기에 현금을 만들 수 있지만 매출이 꺾이면 reverse된다. SOTP는 각 사업의 독립 SG&A·working capital·폐점비를 차감해야 하며, "
        "turnaround 2단계에서는 과거 비용절감보다 신규매장·remodel·salesforce의 incremental ROIC가 common 가치의 핵심이다."
    ),
})

m.SOURCES.update({
    "nen": [
        m.S("NERA investor relations", "https://www.thehamiltoncompany.com/Investor-Relations.aspx", "New England Realty Associates / Hamilton", "2026", "2,943 apartments·130k sf commercial·1/30 receipt·37년 연속/증가 배당"),
        m.S("NERA 2025 Form 10-K — company host", "https://www.thehamiltoncompany.us/nera/nen-20251231x10k.htm", "NERA", "2026-03", "portfolio·mortgages·JV·repurchase·related-party와 receipt 구조"),
        m.S("NERA 2025 Form 10-K — SEC", "https://www.sec.gov/Archives/edgar/data/746514/000110465926027586/nen-20251231x10k.htm", "SEC / NERA", "2026-03", "감사 재무제표와 2012 3-for-1 receipt split"),
        m.S("Hamilton management", "https://www.thehamiltoncompany.com/About-us/Management", "The Hamilton Company", "2026", "Harold Brown 1925~2019와 Jameson Brown 승계"),
        m.S("Hamilton operating platform", "https://www.thehamiltoncompany.com/About-us/About-us.aspx", "The Hamilton Company", "2026", "Greater Boston 5,600+ residential units·1.5m sf 관리 플랫폼"),
    ],
    "oc": [
        m.S("Owens Corning SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=1370946&owner=exclude", "SEC / Owens Corning", "2006-2026", "재편 뒤 10-K·8-K와 segment·capital allocation 연속성"),
        m.S("Owens Corning 2007 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1370946/000119312508040193/d10k.htm", "SEC / Owens Corning", "2008-02-27", "housing downturn·Saint-Gobain composites 인수·segment economics"),
        m.S("Owens Corning 2013 results", "https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2014/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2013-Results/default.aspx", "Owens Corning", "2014-02-12", "adjusted EBIT·EPS·Roofing·Insulation와 dividend"),
        m.S("Owens Corning 2015 results", "https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2016/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2015-Results/default.aspx", "Owens Corning", "2016-02-10", "asphalt cost·selling price·volume/mix와 FCF bridge"),
        m.S("Owens Corning 2017 results", "https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2018/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2017-Results/default.aspx", "Owens Corning", "2018-02-21", "세 segment EBIT·operating cash·FCF"),
        m.S("Owens Corning 2018 results", "https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2019/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2018-Results/default.aspx", "Owens Corning", "2019-02-20", "2018 input-cost/storm 환경과 segment 결과"),
        m.S("Owens Corning 2019 results", "https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2020/Owens-Corning-Reports-Full-Year-and-Fourth-Quarter-2019-Results/default.aspx", "Owens Corning", "2020-02-19", "2019 Roofing EBIT·operating cash·FCF"),
    ],
    "odp": [
        m.S("Office Depot SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=800240&owner=exclude", "SEC / Office Depot", "1994-2020", "Retail·BSD·International와 capital allocation filings"),
        m.S("Office Depot 2001 annual report", "https://media.corporate-ir.net/media_files/nys/odp/reports/AR2001/od2001ar24.html", "Office Depot", "2002", "International reported/local-currency growth와 Viking comps"),
        m.S("Office Depot 2002 annual report", "https://media.corporate-ir.net/media_files/nys/odp/reports/ar02/report/10_01.htm", "Office Depot", "2003", "business segment·multichannel 후속 운영"),
        m.S("Office Depot 2008 operating results", "https://www.sec.gov/Archives/edgar/data/800240/000095014409001557/g17789exv99w1w1.htm", "SEC / Office Depot", "2009-02-24", "Retail·BSD sales와 operating profit collapse"),
        m.S("Office Depot–OfficeMax merger completion", "https://www.sec.gov/Archives/edgar/data/12978/000119312513433122/d624667dex991.htm", "SEC / OfficeMax / Office Depot", "2013-11-05", "후속 법인 결합과 legacy asset 경로"),
    ],
})


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**x):
    x["claims"] = [C(*row) for row in x.pop("claimdata")]
    x.setdefault("security", "Common stock")
    x.setdefault(
        "waterfall",
        "Segment operating cash에서 운전자본·maintenance/growth capex·interest·tax를 차감한다. normalized EBITDA와 historical margin은 현금이 아니며, cycle trough까지 필요한 자본과 구조조정비를 먼저 뺀다.",
    )
    x.setdefault("contest", False)
    return x


IDEAS = [
I(id="157ce960-e48c-49cb-8ed3-7b936d9bc882", date="2019-01-15", author="eigenvalue", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="약 $53", horizon="10년", filename="analysis/ideas/2019/2019-01-15_NEN_long.md", link="https://www.valueinvestorsclub.com/idea/NEW_ENGLAND_REALTY_ASSC__-LP/0457584467", desc=0, cat=684, security="Depositary Receipt = 1/30 Class A Unit", title="replacement-cost discount·rent reset·buyback compounder Long", verdict="사업·자본배분 방향 성공, 200%/정확 수익률 미검증", score=8.7, process=9.0,
summary="약 $53에서 market cap 약 $198m, replacement cost 대비 55%+, NAV 대비 67% discount, rent roll 약 7x와 10~11% FCF yield를 제시한 장기 Long이다. Boston Class-B 공급제약과 under-market rent reset이 NOI를 키우고, Brown family가 credit line 상환 뒤 할인된 receipt를 재매입해 10년 15%+ 복리를 만든다는 구조다.",
valuation="원문은 약 $53에서 200% upside를 제시했지만 attached SQL에는 catalyst만 있고 description은 없다. 선행 curated metadata의 replacement-cost 55%+ 할인, NAV 67% 할인, 10~11% FCF yield는 provenance B로 보존한다. NAV는 cap rate 하나가 아니라 `property NOI/stress cap-mortgage-JV debt-recurring capex-GP·tax`로 계산하고 buyback은 매입 receipt당 NAV accretion으로 본다.",
actual="NERA는 2026년 공식 IR 기준 2,943 apartments와 약 130k sf commercial space를 보유하고 37년 연속 또는 증가 배당을 기록한다. 2019 founder 사망 뒤 Jameson Brown 체제로 운영 플랫폼이 이어졌고 repurchase authorization과 property/JV 운용도 지속됐다. business durability와 succession은 확인됐지만 10년 200% total return은 아직 현재 SQL로 검증할 수 없다.",
price="현 첨부 SQL에는 performance COPY가 없다. 기존 초안의 1개월~3년 수익률을 폐기했다. 약 $53·200% upside는 T0 anchor일 뿐이며 distribution과 1/30 receipt 기준을 연결한 total-return series가 없어 exact return/IRR은 null이다.",
drivers="수익논지의 핵심은 cap-rate compression이 아니라 under-market rent→NOI 성장과 NAV 아래 buyback→receipt당 ownership 증가다. 2019 succession과 2020 pandemic은 이를 시험했고 운영 플랫폼은 지속됐다. 다만 저유동성 LP·related-party·refinancing cost는 구조적 discount를 정당화할 수 있다.",
error="200% upside를 단일 NAV discount로 제시하면 cap rate·세금·JV debt·GP governance·liquidity discount가 겹친다. replacement cost는 수익가치가 아니며, Class-B 공급제약도 rent control·repair capex·금리 상승을 막지 못한다. buyback 재개는 credit line 상환만이 아니라 가격·유동성·GP 선택에 달렸다.", first_signal="same-property occupancy가 95% 아래로 내려가고 rent growth가 mortgage/reset cost보다 낮아지거나, NAV 50%+ 할인에도 4개 분기 이상 repurchase 없이 related-party acquisition이 늘면 15% 복리 가정을 낮춘다.",
waterfall="Property NOI에서 recurring capex·property mortgage service·JV debt·GP/related-party cost와 세금을 차감하고 1/30 Unit receipt당 가치를 계산한다. replacement cost와 gross JV appraisal은 common cash가 아니다.",
metrics=[("Entry/NAV", "약 $53·NAV 67% 할인", "200% upside", "business 지속·수익률 null", "가치 방향/성과 미검증"),("FCF yield", "10~11%", "rent reset으로 성장", "공식 장기 운영 지속", "방향 성공"),("Replacement cost", "55%+ 할인", "신규공급 억제", "Class-B stock 지속", "부분 검증"),("Buyback", "credit line 상환 뒤 재개 기대", "NAV/share accretion", "program·authorization 지속", "방향 성공"),("Security", "1/30 Unit receipt", "10년 total return", "분배 포함 series 없음", "미검증")],
timeline=[("2012-01-03", "3-for-1 receipt split", "1/10→1/30 basis"),("2017-12", "원문 비교가격 약 $75", "discount history"),("2019-01-15", "VIC Long", "약 $53·장기 compound"),("2019", "Harold Brown 사망", "succession test"),("2020", "COVID Boston rental shock", "occupancy·rent stress"),("2021~25", "운영·repurchase·배당 지속", "platform durability"),("2026", "2,943 apartments·37년 배당", "business outcome")],
claimdata=[("Class-B 공급제약", "높은 토지·건축비가 경쟁공급을 막는다.", "replacement cost 대비 55%+ 할인", "rent 규제·신규 Class-A가 B급 rent를 압박하지 않는다.", "Class-B vacancy>5% 또는 concession 급증이면 반증.", "Greater Boston 운영 stock과 platform 지속", "방향 성공", "replacement moat는 실제 supply·occupancy로 검증한다."),("under-market rent reset", "임대차 갱신이 acquisition 없는 NOI 성장을 만든다.", "rent roll 약 7x·under-market units", "turnover/renovation 비용보다 rent uplift가 크다.", "same-unit NOI가 mortgage cost보다 낮으면 반증.", "장기 운영은 지속됐으나 cohort bridge 미복원", "부분 검증", "lease mark-to-market에서 capex·vacancy를 뺀다."),("NAV discount", "약 67% 할인은 governance를 감안해도 과도하다.", "property/JV appraisal", "stress cap·net debt 뒤에도 큰 residual이 남는다.", "7~8% cap에서 NAV≤price면 반증.", "자산은 지속됐지만 liquidation은 없음", "가치 방향", "NAV discount와 실현 가능한 net proceeds를 구분한다."),("10~11% FCF yield", "현재 cash yield가 시간을 보상한다.", "owner FCF estimate", "maintenance capex와 JV cash가 정확하다.", "분배 전 FCF coverage<1x면 반증.", "37년 dividend record가 cash durability 지지", "방향 성공", "부동산 FCF는 recurring capex 후 계산한다."),("할인 buyback", "credit line 상환 뒤 자사주를 재개한다.", "SQL catalyst·과거 repurchase", "GP가 외부자산보다 receipt를 선택한다.", "NAV 50% 할인에도 4Q 미매입이면 반증.", "repurchase framework 지속", "방향 성공", "owner alignment는 실제 체결가격으로 본다."),("15%+ 장기복리", "NOI·buyback·discount 축소로 10년 200%+다.", "세 driver 결합", "금리·세금·liquidity가 compounding을 훼손하지 않는다.", "5년 NAV/share CAGR<8%면 반증.", "현재 SQL로 total return 미검증", "미검증", "장기 목표는 NAV/share·distribution·price를 분리한다.")]),

I(id="b1523971-cf57-413f-be4f-788b762c15e4", date="2007-01-31", author="jet551", ticker="OC", entity="Owens Corning", group="oc", raw_short=False, direction="Long", entry="$28.50", horizon="12~24개월", filename="analysis/ideas/2007/2007-01-31_OC_long.md", link="https://www.valueinvestorsclub.com/idea/Owens_Corning/9709277856", desc=0, cat=178, title="post-asbestos 재편·fresh-start discount Long", verdict="재편 성공, housing-cycle timing 실패·정확 수익률 미검증", score=4.5, process=6.5,
summary="2006년 Chapter 11 출구 뒤 $28.50에서 약 6.1x trailing EBITDA·1.0x fresh-start book으로 평가한 Long이다. asbestos liability가 trust로 이전되고 clean financials·analyst coverage가 나오면 할인율이 줄며, distressed investors의 cost basis와 #1/#2 시장지위가 하방을 지지한다고 봤다.",
valuation="핵심은 6.1x trailing EBITDA와 1.0x fresh-start book이 정상 housing/materials cycle에 싸다는 것이었다. 그러나 emergence accounting의 book는 청산가치가 아니고 trailing EBITDA는 2006 housing peak의 영향을 받는다. 올바른 bridge는 segment별 volume·price·utilization을 2008형 stress까지 낮춘 뒤 net debt와 asbestos trust separation을 반영하는 것이다.",
actual="법적 재편과 asbestos trust 이전은 성공했지만 2007~09 housing starts와 insulation utilization이 더 깊게 하락했다. post-reorg balance sheet가 새로워도 earnings cycle은 새로 시작하지 않았다. 이후 business는 회복했지만 원 12~24개월 thesis의 timing은 실패로 판정한다.",
price="첨부 SQL에 performance table/data가 없다. 기존 초안의 1~5년 수익률은 폐기했다. $28.50과 valuation multiple만 T0 anchor이며 exact total return/IRR은 null이다.",
drivers="손실위험은 asbestos가 아니라 housing volume과 plant operating leverage였다. clean balance sheet·distressed-holder sponsorship은 survivability를 높였지만 insulation fixed cost의 역레버리지와 composites deal funding을 상쇄하지 못했다.",
error="법적 tail 제거를 cycle bottom과 혼동했고 trailing EBITDA를 normalized로 취급했다. sophisticated holder cost basis는 매도압력의 설명이지 fundamental floor가 아니다. Roofing repair demand와 composites가 new-residential insulation을 완전히 hedge한다고 본 것도 segment 상관을 낮게 잡은 오류다.", first_signal="housing starts 하락과 함께 insulation capacity utilization이 80% 아래로 내려가 price cutting이 나타나거나, clean 10-Q 공개 뒤 normalized EBITDA 추정이 20% 이상 낮아지면 rerating보다 earnings reset을 우선한다.",
metrics=[("Entry", "$28.50", "post-reorg rerating", "exact return null", "timing 실패"),("EV/EBITDA", "6.1x trailing", "normalized discount", "denominator 하락", "실패"),("P/book", "약 1.0x fresh-start", "하방 floor", "cycle book는 hard floor 아님", "실패"),("Legal", "2006 asbestos trust 이전", "tail 제거", "재편 유지", "성공"),("Catalyst", "clean filings·coverage", "12~24개월", "공개돼도 cycle 악화", "불충분")],
timeline=[("2000", "asbestos Chapter 11 신청", "old equity/legal overhang"),("2006-10-31", "재편 완료", "new common 출범"),("2007-01-31", "VIC Long", "$28.50"),("2007", "housing·insulation 약화", "첫 반증"),("2007-10", "Saint-Gobain composites 인수 전환", "capital need"),("2008~09", "housing/GFC trough", "earnings cycle 실패"),("2013", "housing·segment recovery", "장기 business 회복")],
claimdata=[("asbestos tail 제거", "524(g) trust로 legacy claims가 new common에서 분리된다.", "confirmed plan·2006 emergence", "fraudulent transfer·추가 claim tail이 없다.", "trust funding 재개방이면 반증.", "재편 구조 유지", "성공", "legal clean-up과 operating bottom은 별도 claim이다."),("fresh balance sheet", "fresh-start book가 하방을 지지한다.", "약 1.0x book", "asset marks와 net debt가 stress에도 보존된다.", "impairment·cash burn이면 반증.", "housing stress로 book floor 약화", "부분/실패", "cyclical book에는 replacement·forced-sale haircut을 둔다."),("6.1x EBITDA", "시장지위 대비 낮은 배수다.", "trailing EBITDA", "2006 EBITDA가 정상치와 가깝다.", "segment EBIT -20%면 반증.", "downcycle로 denominator 하락", "실패", "emergence 직후 trailing은 peak-cycle 여부를 감사한다."),("repair/replace 완충", "Roofing·remodel이 new housing 하락을 상쇄한다.", "사업 mix", "segment shock 상관이 낮다.", "Insulation 손실이 Roofing cash를 압도하면 반증.", "완충은 있었지만 부족", "부분", "각 segment downside dollar를 합산한다."),("distressed holder floor", "plan sponsor의 cost basis가 매도하방을 제한한다.", "smart-money ownership", "보유자에게 추가 유동성 압력이 없다.", "lock-up 종료·forced sale이면 반증.", "cycle floor가 되지 못함", "실패", "holder basis는 catalyst도 intrinsic value도 아니다."),("disclosure rerating", "clean numbers와 coverage가 valuation gap을 닫는다.", "SQL catalyst", "정보 부족이 할인 원인이다.", "공개 뒤 estimates 하향이면 반증.", "영업악화가 정보효과를 압도", "실패", "information catalyst는 earnings direction에 종속된다.")]),

I(id="0886fe04-c4de-4734-b212-05ea2806dac8", date="2007-12-26", author="conway968", ticker="OC", entity="Owens Corning", group="oc", raw_short=False, direction="Long", entry="$20.60", horizon="3~5년", filename="analysis/ideas/2007/2007-12-26_OC_long.md", link=None, desc=13193, cat=117, title="segment 정상마진·3.7x normalized EBITDA Long", verdict="심한 경로손실 뒤 정상화 방향 성공·정확 수익률 미검증", score=7.6, process=8.8,
summary="$20.60에서 debt $1.85bn·cash $450m·market cap $2.7bn, net EV $3.4bn을 놓고 normalized EBITDA $911m 대비 3.7x라 본 Long이다. Insulation 18%, Roofing 5%, Composites 10% 안팎의 정상 EBIT margin을 사업별 산업구조와 capacity로 재구성해 $42.50/share를 제시했다.",
valuation="원문 normalized EBIT은 Insulation $325m, Roofing $80m, Other $23m, Composites $203m, corporate -$40m로 총 $591m이다. 이자 $108m와 세금 $179m을 빼 net income $304m, 16x=$4.864bn에 NOL NPV $700m을 더해 $5.564bn/$42.50를 계산했다. NOL은 full-value가 아니며 18% insulation margin 도달 전 cash burn과 duration을 별도 할인해야 한다.",
actual="2008~09 housing/GFC는 원문이 예상한 것보다 깊어 초기 경로는 악화됐다. 그러나 industry concentration, capacity rationalization과 housing 회복 뒤 Insulation·Roofing profitability는 살아났고 2013에는 Insulation이 흑자전환했다. 장기 정상화 방향은 성공했지만 현 SQL로 보유기간 수익률은 검증하지 않는다.",
price="현 첨부 SQL에서 description 13,193자와 catalyst 117자는 확인되지만 performance COPY는 없다. $20.60·$42.50를 T0 anchor로 보존하고 기존 수익률은 모두 null로 재설정한다.",
drivers="2007-01과 달리 하락한 entry, 사업부별 trough 인식, utilization→price→margin의 인과가 margin of safety를 키웠다. 다만 GFC path와 timing risk는 여전히 과소평가됐고 투자자가 견뎌야 할 중간 손실은 컸다.",
error="Insulation 18%를 conservative normal로 불렀지만 starts·capacity·price가 동시에 회복되는 시점을 확률화하지 않았다. NOL $700m을 100% 가산했고 Saint-Gobain synergies와 cyclicality를 중복했다. Johns Manville transaction multiple도 2001 margin·capital structure 차이를 더 haircut해야 했다.", first_signal="capacity utilization 70~75%에서 추가 하락하고 plant closure보다 price cutting이 먼저 나타나거나, normalized EBIT bridge의 두 segment 이상이 25% 하향되면 $42.50 target과 position size를 낮춘다.",
metrics=[("Entry/target", "$20.60", "$42.50", "normalization 방향", "성과 null"),("Net EV", "$3.4bn", "3.7x normal EBITDA", "GFC path 후 회복", "방향 성공"),("Normal EBITDA", "$911m", "segment margin 회귀", "장기 profitability 회복", "방향 성공"),("Insulation", "10.4% 9M07", "18%/$325m EBIT", "2008~09 악화 후 회복", "timing 실패"),("NOL NPV", "$700m", "full add", "사용 timing 미복원", "과대 가능")],
timeline=[("2006-10", "재편 출구", "new common"),("2007-01", "선행 VIC Long $28.50", "entry 비교"),("2007-12-26", "VIC Long", "$20.60·3.7x"),("2008~09", "housing/GFC 심화", "path 반증"),("2010~12", "capacity·수요 점진 회복", "normalization 시작"),("2013", "Insulation 흑자전환", "핵심 방향 확인"),("2014", "capital return 시작", "FCF 전환")],
claimdata=[("Insulation 정상화", "10.4% margin은 18%로 회귀한다.", "3사 80%+·역사 16~22%", "capacity가 low-90% utilization로 회복한다.", "plant closure 없이 utilization<70%면 반증.", "GFC 후 장기 회복", "방향 성공/지연", "margin은 utilization·price·volume gate로 나눈다."),("Roofing 방어성", "70~85% reroof mix가 5% EBIT를 지지한다.", "20~30년 replacement cycle", "asphalt pass-through가 작동한다.", "price-cost spread<0 지속이면 반증.", "replacement cash가 완충", "성공 방향", "new roof와 reroof volume을 분리한다."),("Composites $203m", "10% margin과 synergy가 정상 EBIT를 만든다.", "global GDP+ 성장·Saint-Gobain", "인수통합·capacity discipline이 성공한다.", "synergy 지연·utilization 하락이면 반증.", "사업은 회복했으나 경로 변동", "부분 성공", "인수 synergy는 base와 분리한다."),("3.7x normalized EBITDA", "downturn을 감안해도 배수가 과도하게 낮다.", "$3.4bn/$911m", "$911m이 full-cycle cash proxy다.", "normal EBITDA<$650m이면 반증.", "장기 rerating 방향", "성공 방향", "normal E의 오차범위를 multiple보다 먼저 둔다."),("NOL $700m", "세금자산을 equity에 전액 더한다.", "fresh-start tax asset", "충분한 taxable income이 빨리 발생한다.", "usage delay·limitation이면 반증.", "정확 실현가치 미복원", "미검증/과대", "NOL은 사용시점·제한을 할인한다."),("housing stabilization", "starts가 멈추면 빠른 snapback이다.", "SQL catalyst", "GFC형 추가수축이 없다.", "starts 재급락이면 반증.", "추가 급락 뒤 회복", "timing 실패", "cycle bottom은 방향보다 runway로 관리한다.")]),

I(id="671f9ef0-c9d7-49de-a9c3-ff2901c3dd46", date="2013-03-14", author="cnm3d", ticker="OC", entity="Owens Corning", group="oc", raw_short=False, direction="Long", entry="$40.61", horizon="12~36개월", filename="analysis/ideas/2013/2013-03-14_OC_long.md", link=None, desc=0, cat=135, title="Roofing discipline·Insulation 흑자전환·$60 base Long", verdict="사업논지 강한 성공, 단기 target·정확 수익률 미검증", score=8.7, process=9.0,
summary="$40.61에서 Bear $29, Base $60, Bull $96을 제시한 housing recovery Long이다. 핵심은 Roofing top-4 집중과 winter pre-buy 축소가 margin을 지키고, 적자 Insulation이 volume·price의 높은 incremental margin으로 흑자전환하며, Composites와 $2.2bn NOL·환원이 추가 upside를 만든다는 것이었다.",
valuation="Bear/Base/Bull은 각각 $29/$60/$96이다. Base는 Roofing 정상 margin을 유지하면서 Insulation 흑자전환과 Composites 개선을 반영했고, Bull은 더 강한 housing·price와 NOL/capital return을 중첩했다. 역산상 $40.61은 base의 상당 부분을 할인했지만 Roofing peak margin이 꺾일 때 Insulation 회복이 상쇄하는지를 dollar EBIT로 봐야 한다.",
actual="공식 2013 결과에서 adjusted EBIT은 $293m에서 $416m, adjusted EPS는 $1.10에서 $1.86으로 늘었다. Roofing EBIT $386m로 약 20% margin을 유지했고 Insulation은 -$38m에서 +$40m으로 흑자전환했다. 이사회는 분기배당을 승인해 2014 지급을 시작했다. 사업 claim은 빠르게 맞았지만 exact stock return과 $60 도달시점은 현 SQL로 검증하지 않는다.",
price="첨부 SQL에는 catalyst 135자만 있고 description·performance는 없다. 기존 초안의 1·3·5년 수익률은 폐기했으며 $40.61과 $29/$60/$96만 provenance B의 T0 anchor로 남긴다.",
drivers="가장 큰 earnings delta는 적자 Insulation의 흑자전환이었다. Roofing cash가 downside를 지지하고 fixed-cost segment의 개선이 upside를 만들었다. capital return은 결과의 확인이지 주된 2013 EBIT driver는 아니었다.",
error="Roofing의 20% margin과 Insulation 정상화를 동시에 bull에 넣으면 cycle correlation을 과소평가한다. $2.2bn NOL과 buyback은 활용기간·price를 붙여야 하고, 원문 가격목표는 business success와 12개월 rerating을 구분하지 않았다.", first_signal="Roofing price increase realization이 asphalt/freight보다 낮아 margin<15%로 내려가고, 동시에 Insulation price/volume 개선에도 EBIT가 계속 음수면 $60 base를 철회한다.",
metrics=[("Entry/scenarios", "$40.61", "$29/$60/$96", "business 성공·price null", "방향 성공"),("Adjusted EBIT", "$293m 2012", "$416m+", "$416m 2013", "성공"),("Adjusted EPS", "$1.10", "회복", "$1.86", "성공"),("Roofing", "margin 지속 우려", "discipline", "$386m/~20%", "성공"),("Insulation", "-$38m", "흑자전환", "+$40m", "강한 성공")],
timeline=[("2012", "adjusted EBIT $293m", "T0 base"),("2013-03-14", "VIC Long", "$40.61"),("2013", "Roofing price·volume 실행", "cash anchor"),("2013", "Insulation +$40m", "turnaround"),("2013-Q4", "dividend 승인", "capital return"),("2014-Q1", "첫 분기배당", "cash realization"),("2015", "asphalt deflation cycle", "다음 thesis로 진화")],
claimdata=[("Roofing discipline", "winter buy와 oligopoly가 가격붕괴를 막는다.", "top-4 75%+·channel mechanics", "inventory가 가격전쟁을 만들지 않는다.", "realized price-cost spread 급락이면 반증.", "2013 약 20% margin", "성공", "산업집중은 realized price와 재고로 확인한다."),("Insulation leverage", "housing 회복이 적자를 빠르게 흑자로 바꾼다.", "고정비·낮은 utilization", "price·volume이 incremental cost보다 빠르다.", "housing 증가에도 EBIT 음수면 반증.", "-$38m→+$40m", "강한 성공", "cyclical catalyst는 적자부문의 dollar EBIT다."),("Composites 회복", "volume·margin이 정상화된다.", "SQL catalyst", "global 산업수요와 capacity가 개선된다.", "utilization·margin 동시 하락이면 반증.", "후속 개선", "방향 성공", "모든 segment 동시회복은 peak risk도 만든다."),("$60 base", "segment 회복과 보수적 multiple로 48% upside다.", "Bear/Base/Bull $29/$60/$96", "business improvement가 price에 반영된다.", "12개월 target 지연·multiple 축소면 반증.", "사업 성공, price path 없음", "미검증", "target date와 operating target을 분리한다."),("NOL 가치", "$2.2bn NOL이 cash tax를 낮춘다.", "tax asset", "사용 제한 없이 taxable income이 생긴다.", "tax rate 정상화가 빨라지면 반증.", "정확 NPV 미복원", "부분", "NOL은 cash-tax bridge로만 센다."),("환원 촉매", "buyback·dividend가 잉여현금을 주주에게 돌린다.", "cleaner balance sheet·SQL catalyst", "cycle capex보다 우선한다.", "고가 M&A·share 증가면 반증.", "분기배당 도입", "성공", "환원은 발표보다 실제 cash/share로 본다.")]),

I(id="a345ad16-b6ab-4187-b8d5-958c5d4188b8", date="2015-01-06", author="booM()", ticker="OC", entity="Owens Corning", group="oc", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="12~18개월", filename="analysis/ideas/2015/2015-01-06_OC_long.md", link="https://www.valueinvestorsclub.com/idea/OWENS_CORNING/3293915995", desc=0, cat=141, title="asphalt deflation·Roofing spread surprise Long", verdict="earnings 인과 일부만 적중·방향 성공, 정확 수익률 미검증", score=8.1, process=9.1,
summary="prior metadata의 raw Short와 달리 후속 2015-04 글이 '1/6/2015 Long thesis'라고 명시한 Long이다. consensus EPS 약 $2.30에 crude/asphalt 20% 하락의 약 $0.50 EPS benefit이 빠졌고, 2014 inventory shock 뒤 winter pre-buy discipline과 stable shingle pricing을 적용하면 $2.80×18=$50이라는 논지다.",
valuation="원문 bridge는 `consensus EPS $2.30 + asphalt benefit 약 $0.50 = $2.80`, 18x에서 약 $50다. 핵심 sensitivity는 asphalt 하락률이 아니라 realized shingle price의 pass-through다. 원재료 $68m benefit과 selling-price -$114m을 동시에 보면 gross cost saving 전액이 EBIT로 남지 않는다.",
actual="2015 Roofing selling price는 $114m 감소해 stable-price claim은 실패했다. 반면 asphalt cost deflation은 $68m benefit, volume/mix가 보완해 Roofing EBIT은 $34m 늘었다. 회사 adjusted EPS는 $1.76에서 $2.57로 46% 증가하고 FCF는 $50m에서 $341m으로 개선됐다. Long의 earnings direction은 맞았지만 원문 causal bridge는 부분 적중이다.",
price="현 SQL에는 catalyst 141자만 있고 description·performance는 없다. 기존 초안의 1~5년 수익률을 폐기했다. $50 target과 EPS bridge만 T0 anchor이고 exact return/IRR은 null이다.",
drivers="실제 개선은 lower asphalt 하나가 아니라 lower realized price, lower raw-material cost, volume/mix의 합이었다. 따라서 성공의 재사용 가능한 edge는 commodity price 예측보다 channel inventory와 price-cost lag를 dollar bridge로 만든 점이다.",
error="top-4 concentration을 flat price로 바로 연결했고 customer price deflation을 충분히 반영하지 않았다. $0.50 EPS는 gross sensitivity에 가까우며 tax·inventory layer·hedge·lag를 빼야 한다. 18x는 cyclical Roofing surprise에 다소 높은 terminal multiple이다.", first_signal="monthly/quarterly realized shingle price 감소액이 asphalt saving을 초과하거나 distributor inventory가 재상승해 winter discount가 복원되면 $0.50 EPS uplift를 절반 이하로 낮춘다.",
metrics=[("Consensus EPS", "$2.30", "$2.80", "$2.57 2015", "방향 성공"),("Asphalt", "20% 하락 가정", "+$0.50 EPS", "+$68m EBIT benefit", "성공"),("Selling price", "stable", "margin 유지", "-$114m", "실패"),("Roofing EBIT", "2014 base", "확대", "+$34m", "성공"),("FCF", "$50m 2014", "현금전환", "$341m 2015", "강한 성공")],
timeline=[("2014", "shingle inventory·price shock", "discipline 학습"),("2014-H2", "crude/asphalt 급락", "cost catalyst"),("2015-01-06", "VIC Long", "$50 target"),("2015-04-07", "후속 Long update", "channel evidence"),("2015", "selling price -$114m", "flat-price 반증"),("2015", "asphalt +$68m·FCF $341m", "earnings 성공"),("2016-02", "공식 FY15 결과", "causal audit")],
claimdata=[("asphalt deflation", "20% 하락이 약 $0.50 EPS를 더한다.", "crude collapse·roofing asphalt", "lag·inventory·hedge 후 benefit이 남는다.", "realized saving<$35m이면 반증.", "$68m benefit", "성공", "raw material thesis는 realized cost로 닫는다."),("stable shingle price", "업체 discipline이 price를 유지한다.", "top-4·2014 inventory lesson", "고객 pass-through가 제한된다.", "selling-price loss>$50m이면 반증.", "-$114m", "실패", "oligopoly도 commodity deflation을 일부 돌려준다."),("winter pre-buy 축소", "discount/rebate가 줄어 margin이 개선된다.", "channel checks", "distributor가 낮은 inventory를 유지한다.", "pre-buy 재확대면 반증.", "volume/mix가 결과를 보완", "부분", "channel claim은 realized invoice로 검증한다."),("consensus surprise", "$2.30가 cost tailwind를 놓쳤다.", "$0.50 sensitivity", "다른 segment가 상쇄하지 않는다.", "adjusted EPS<$2.30이면 반증.", "$2.57", "성공", "consensus gap은 항목별로 합계검산한다."),("$50 target", "$2.80×18x가 합리적이다.", "quality·cycle recovery", "multiple이 유지된다.", "earnings는 맞아도 multiple<15x면 반증.", "price path 없음", "미검증", "EPS 성공과 rerating 성공을 나눈다."),("raw direction", "metadata Short가 아니라 Long payoff다.", "후속 글의 명시적 Long", "후속 글이 같은 idea를 지칭한다.", "반대 payoff/borrow가 확인되면 반증.", "Long으로 교정", "성공", "direction은 flag가 아니라 payoff 문장으로 판정한다.")]),

I(id="8a1f7ef6-2064-40ff-95d9-aeaec1336894", date="2015-04-07", author="booM()", ticker="OC", entity="Owens Corning", group="oc", raw_short=False, direction="Long Update", entry="2015-01-06 이후 약 +17% (선행 metadata)", horizon="6~18개월", filename="analysis/ideas/2015/2015-04-07_OC_long_update.md", link=None, desc=0, cat=1, title="Roofing channel-check·asphalt flux Long update", verdict="channel 방향·earnings 성공, realized-price 가정 부분 실패·정확 수익률 미검증", score=8.0, process=9.3,
summary="1월 6일 Long을 업데이트한 별도 idea unit이다. 일부 지역 roofing flux가 약 30% 하락했고, OC의 asphalt 구매가 이미 진행됐으며, winter discount/rebate가 거의 없고 distributor inventory가 낮아 May price increase가 가능하다고 봤다. price letter보다 cost·inventory·survey라는 near-term evidence를 추가했다.",
valuation="이 update는 새 terminal multiple보다 기존 `$2.30 consensus+$0.50 asphalt benefit→$2.80 EPS×18=$50`의 확률을 높였다. 1월 이후 약 +17%는 선행 metadata이며 정확 가격은 복원하지 않는다. update 시점에서는 이미 오른 가격 때문에 upside가 줄었으므로 expected value는 realized selling price가 flat인지에 더 민감해졌다.",
actual="2015 공식 결과에서 asphalt cost deflation $68m과 FCF $341m은 Long을 지지했다. 그러나 selling price는 $114m 감소해 survey와 price-increase letter가 실제 invoice price를 완전히 예측하지 못했다. Roofing EBIT +$34m·adjusted EPS $2.57로 방향은 성공했지만 pricing claim은 부분 실패다.",
price="첨부 SQL에서 이 idea는 catalyst가 `.` 한 글자이고 description·performance도 없다. 기존 초안의 수익률은 전부 폐기한다. 후속 원문 성격과 약 +17% 진행은 prior curated metadata 등급으로만 남기며 exact return/IRR은 null이다.",
drivers="edge는 upstream asphalt quote, manufacturer buying, distributor inventory와 rebate를 한 chain으로 연결한 점이다. 손익은 price 고정보다 cost decline이 price decline을 얼마나 앞섰는지에서 나왔다. update는 conviction을 높였지만 valuation margin은 초기 글보다 좁아졌다.",
error="channel 응답과 announced price increase를 realized price로 취급했다. 지역별 flux -30%가 OC blended cost에 그대로 들어오지 않고 inventory layer·contract lag가 있다. 이미 +17% 오른 뒤에도 payoff를 같은 $50로 둬 upside compression을 명시적으로 다시 계산하지 않았다.", first_signal="Q2/Q3 price-volume bridge에서 selling-price decline이 asphalt saving보다 크거나, distributor 재고일수가 정상 이상으로 오르면 price-increase letter와 무관하게 Long update를 철회한다.",
metrics=[("Idea status", "1월 Long update", "확률 상향", "Long으로 일관", "성공"),("Asphalt flux", "일부 지역 -30%", "cost benefit", "FY15 +$68m", "성공"),("Distributor inventory", "낮음", "flat/up price", "selling price -$114m", "부분 실패"),("Roofing EBIT", "개선 기대", "+$34m", "+$34m", "성공"),("FCF", "$50m prior year", "현금전환", "$341m", "강한 성공")],
timeline=[("2015-01-06", "원 Long", "$50 framework"),("2015-Q1", "flux·inventory channel check", "evidence 강화"),("2015-04-07", "VIC update", "약 +17% 뒤"),("2015-05", "price increase letters", "announced catalyst"),("2015", "selling price 감소", "channel claim 반증"),("2015", "asphalt benefit·FCF 개선", "earnings 성공"),("2016-02", "FY15 공시", "realized bridge")],
claimdata=[("flux 하락", "roofing asphalt input가 약 30%까지 하락한다.", "지역 supplier quote", "blended OC purchase cost에 반영된다.", "FY saving<$35m이면 반증.", "$68m benefit", "성공", "quote를 weighted realized cost로 변환한다."),("inventory shortage", "낮은 distributor 재고가 가격을 지지한다.", "channel survey", "sell-through가 유지된다.", "inventory build·rebate 재개면 반증.", "price는 실제 하락", "부분 실패", "재고와 invoice price를 함께 본다."),("winter discipline", "rebate 부재가 industry behavior 변화를 뜻한다.", "manufacturer/distributor checks", "경쟁사가 share를 위해 이탈하지 않는다.", "discount 재도입이면 반증.", "cost 우위는 남았지만 price 고정 실패", "부분", "일시 행동과 구조 discipline을 구분한다."),("May price hike", "announced 인상이 실현된다.", "letters·survey", "customer가 수용한다.", "realized price negative면 반증.", "FY price -$114m", "실패", "price letter는 catalyst가 아니라 가설이다."),("earnings update", "추가 증거가 consensus beat를 높인다.", "cost·inventory chain", "타 segment가 상쇄하지 않는다.", "EPS<$2.30이면 반증.", "$2.57", "성공", "update는 새 evidence의 incremental value를 기록한다."),("payoff compression", "17% 상승 뒤에도 충분한 upside가 남는다.", "$50 기존 target", "target multiple이 유지된다.", "remaining upside<15%면 반증.", "정확 entry/path 없음", "미검증", "후속 글은 가격상승 뒤 EV를 다시 계산한다.")]),

I(id="5a72a215-ae22-4a32-b310-ed589f1aea3d", date="2017-05-12", author="85bears", ticker="OC", entity="Owens Corning", group="oc", raw_short=False, direction="Long", entry="원문 가격 미복원", horizon="1~3년", filename="analysis/ideas/2017/2017-05-12_OC_long.md", link="https://www.valueinvestorsclub.com/idea/Owens_C/2597952917", desc=0, cat=258, title="three-segment normalization·10% FCF yield Long", verdict="2017 사업·FCF 성공 뒤 peak-expectation 노출, 정확 수익률 미검증", score=7.2, process=8.4,
summary="Roofing distributor consolidation과 winter-buy rationalization, Insulation utilization 회복의 높은 incremental margin, Composites capacity discipline이 동시에 작동하는데도 약 10% FCF yield라고 본 Long이다. management의 보수적 guidance와 price increase realization을 추가 catalyst로 두고 50%+ optional upside를 기대했다.",
valuation="원문은 약 10% FCF yield와 50%+ optional upside를 제시했다. 그러나 세 segment가 동시에 정상화되는 시점의 FCF는 trough가 아니라 peak에 가까울 수 있다. 올바른 denominator는 2017 $679m FCF에서 storm working capital·cycle capex와 다음 해 asphalt/freight inflation을 normalize한 mid-cycle FCF다.",
actual="2017 net sales는 12% 늘고 adjusted EBIT $855m, Roofing $535m, Composites $291m, Insulation $177m(+40%)이었다. operating cash flow $1.0bn, FCF $679m으로 business thesis는 강하게 맞았다. 2018에는 storm normalization, asphalt/freight inflation과 housing 우려가 겹쳐 당시의 동시 정상화가 peak-expectation risk였음이 드러났다.",
price="현 SQL에는 catalyst 258자만 있고 description·performance가 없다. 기존 초안의 6개월~5년 수익률은 폐기했다. 10% FCF yield·50% upside만 T0 anchor이며 exact return/IRR은 null이다.",
drivers="2017 수익성은 all-three-segment improvement와 cash conversion이 만들었다. 그러나 같은 동시개선은 비교기준을 높여 2018 normalization에 취약하게 했다. '좋은 business year'와 '좋은 multi-year entry'가 다를 수 있는 사례다.",
error="management beat와 세 segment 개선을 지속 가능한 alpha로 외삽했다. Roofing weather와 inventory working capital을 normal cash로 보고, inflation·acquisition integration·housing affordability가 다음 cycle FCF에 미칠 영향을 충분히 haircut하지 않았다.", first_signal="Roofing price hike가 asphalt/freight를 따라가지 못하고 storm volumes가 정상화되는 동시에 Insulation incremental margin이 둔화하면 10% FCF yield denominator를 20~30% 낮춘다.",
metrics=[("Adjusted EBIT", "개선 기대", "$855m", "$855m 2017", "성공"),("Roofing EBIT", "price·storm 우호", "$535m", "$535m", "성공"),("Insulation EBIT", "operating leverage", "증가", "$177m/+40%", "강한 성공"),("Composites EBIT", "5년 연속 개선", "$291m", "$291m", "성공"),("FCF", "약 10% yield", "$679m", "$679m", "사업 성공/normality 주의")],
timeline=[("2012~16", "Composites 연속 개선", "normalization base"),("2017-05-12", "VIC Long", "10% FCF yield"),("2017", "세 segment 동시 성장", "thesis validation"),("2017", "FCF $679m", "cash conversion"),("2018-H1", "storm demand 정상화", "comparison risk"),("2018", "asphalt·freight inflation", "spread 압박"),("2018-12", "큰 drawdown 뒤 새 Long", "expectation reset")],
claimdata=[("Roofing rationalization", "consolidated distribution과 winter discipline이 margin을 높인다.", "channel structure", "storm·inventory가 왜곡하지 않는다.", "realized price-cost spread 하락이면 반증.", "$535m EBIT 뒤 2018 headwind", "기간 성공", "구조 개선과 weather benefit을 분리한다."),("Insulation leverage", "utilization·price가 높은 incremental EBIT를 만든다.", "housing growth·capacity", "labor/material이 가격보다 낮다.", "volume 성장에도 margin flat이면 반증.", "$177m/+40%", "성공", "fixed-cost thesis는 dollar incremental margin으로 검증한다."),("Composites discipline", "capacity 합리화가 5년 연속 개선을 잇는다.", "global utilization", "신규공급이 제한된다.", "capacity addition·price decline이면 반증.", "$291m", "성공", "연속개선은 supply response를 부른다."),("보수적 guidance", "경영진 beat가 반복된다.", "과거 guide-and-beat", "cycle shock가 없다.", "guidance 상향 뒤 miss면 반증.", "2017 숫자는 성공", "기간 성공", "management conservatism은 영구 moat가 아니다."),("10% FCF yield", "현재 FCF에 비해 싸다.", "$679m 수준 cash", "working capital·storm·capex가 정상이다.", "normalized FCF -25%면 반증.", "peak-normality 위험", "부분", "cyclical FCF yield는 다음 downturn으로 stress한다."),("50%+ upside", "동시 정상화와 rerating이 큰 payoff를 준다.", "세 segment catalyst", "기대가 아직 가격에 낮다.", "모든 KPI 최고치면 peak flag.", "business 성공·price path 없음", "미검증", "동시호전은 upside이자 exit signal이다.")]),

I(id="a02384d0-dd3c-43ec-bee4-b160f305d8e5", date="2018-12-12", author="WeighingMachine", ticker="OC", entity="Owens Corning", group="oc", raw_short=False, direction="Long", entry="원문 가격 미복원·전년 대비 약 48% 하락", horizon="1~3년", filename="analysis/ideas/2018/2018-12-12_OC_long.md", link="https://www.valueinvestorsclub.com/idea/OWENS_CORNING/9361303979", desc=0, cat=83, title="48% drawdown·8.5x normalized EPS Long", verdict="earnings-resilience·expectation-reset 성공 방향, 정확 수익률 미검증", score=9.0, process=9.3,
summary="storm demand 정상화, asphalt/freight inflation, housing 우려와 Insulation acquisitions 때문에 전년 대비 약 48% 하락한 뒤 normalized EPS의 약 8.5x에 산 Long이다. Roofing replacement 수요·노후 housing stock·industry concentration과 낮은 obsolescence risk를 cash anchor로 두고 13x에서 약 50% upside를 봤다.",
valuation="원문 valuation은 약 8.5x normalized EPS에서 13x rerating 시 약 +50%다. 2017처럼 모든 segment가 좋아질 것을 요구하지 않고 2018 cost shock이 영구적이지 않으며 replacement Roofing cash가 유지된다는 낮아진 기대를 샀다. Bear는 housing/price-cost stress에서 EPS를 다시 깎고 8~9x를 유지하는 경우다.",
actual="2018 net sales는 record $7.1bn, adjusted EBIT $861m이었다. Roofing EBIT $434m, Insulation $290m(+64%), Composites $251m으로 earnings collapse는 나타나지 않았다. 2019 operating cash flow는 record $1.0bn, FCF $590m, Roofing EBIT $455m이었다. business resilience와 cost normalization 방향은 확인됐다.",
price="첨부 SQL에는 catalyst 83자만 있고 description·performance는 없다. 기존 1~3년 수익률을 전부 폐기했다. 48% drawdown·8.5x·13x/+50%는 prior curated T0 anchor이며 exact return/IRR은 null이다.",
drivers="이 아이디어의 edge는 2017의 높은 동시개선 기대가 2018에 cost·weather 악재로 reset된 뒤, replacement Roofing과 FCF의 절대 하방을 산 것이다. business quality는 같아도 starting expectation이 달라지면 payoff가 달라진다.",
error="8.5x normalized EPS가 싸다는 결론은 맞아도 normalized earnings에 acquisition synergy와 high Insulation growth를 과도하게 넣으면 안 된다. Roofing replacement도 storm timing과 distributor inventory에 따라 변동하며, 13x rerating은 금리·cycle discount 조건부다.", first_signal="Roofing replacement volume과 realized price-cost spread가 두 분기 연속 악화하고 company FCF<$400m으로 내려가거나 acquired Insulation assets의 ROIC가 WACC를 밑돌면 13x case를 제거한다.",
metrics=[("Drawdown", "약 -48%", "expectation reset", "성과 series 없음", "T0 safety margin"),("Normalized P/E", "약 8.5x", "13x/+50%", "earnings 유지", "방향 성공"),("2018 EBIT", "collapse 우려", "resilience", "$861m", "성공"),("Insulation EBIT", "integration 우려", "안정", "$290m/+64%", "성공"),("2019 FCF", "정상화 기대", "cash anchor", "$590m", "성공")],
timeline=[("2017", "세 segment 호조", "높은 comparison"),("2018-H1", "storm normalization", "Roofing 우려"),("2018", "asphalt·freight inflation", "cost shock"),("2018-12-12", "VIC Long", "48% drawdown·8.5x"),("2019-02", "FY18 EBIT $861m", "collapse 반증"),("2019", "Roofing $455m·FCF $590m", "cash resilience"),("2020-02", "FY19 공시", "normalization 확인")],
claimdata=[("replacement Roofing", "노후 housing stock이 수요를 지지한다.", "reroof 중심 mix", "storm 이후에도 base demand가 유지된다.", "replacement volume -10% 지속이면 반증.", "2019 Roofing $455m", "성공", "new construction과 replacement를 분리한다."),("cost shock 일시성", "asphalt·freight inflation이 정상화된다.", "2018 급격한 input move", "price lag가 따라잡는다.", "price-cost spread 악화 지속이면 반증.", "2019 cash·Roofing 회복", "성공", "cost shock는 lagged price bridge로 본다."),("industry structure", "집중시장·낮은 obsolescence가 cash를 보호한다.", "few suppliers·physical product", "capacity 전쟁이 없다.", "공격적 신규공급·price war면 반증.", "earnings collapse 부재", "성공 방향", "moat는 downturn margin으로 확인한다."),("acquired Insulation", "mineral wool mix가 cyclicality를 낮춘다.", "portfolio diversification", "integration ROIC가 양수다.", "impairment·ROIC<WACC면 반증.", "2018 EBIT +64%", "기간 성공", "mix 변화는 incremental ROIC로 평가한다."),("8.5x normalized EPS", "bad news가 과반영됐다.", "48% drawdown", "normalized E가 크게 훼손되지 않는다.", "FCF<$400m이면 반증.", "$590m FCF 2019", "강한 방향 성공", "multiple보다 denominator resilience를 검증한다."),("13x rerating", "우려 해소 시 약 50% upside다.", "quality/cycle comp", "market risk premium이 안정된다.", "earnings 유지에도 multiple≤9x면 반증.", "exact price path 없음", "미검증", "business de-risk와 market rerating을 분리한다.")]),

I(id="3c518f28-71f4-41a3-a77e-cd3f5770081f", date="2000-07-28", author="kyle36", ticker="ODP", entity="Office Depot, Inc.", group="odp", raw_short=True, direction="Long", entry="약 $6", horizon="12~24개월", filename="analysis/ideas/2000/2000-07-28_ODP_long.md", link="https://www.valueinvestorsclub.com/idea/Office_Depot/4277729045", desc=0, cat=239, title="BSG+International SOTP·Retail free-option Long", verdict="사업회복·SOTP 방향 성공, 정확 수익률 미검증", score=8.0, process=8.8,
summary="raw Short와 달리 원문이 purchase를 권한 명백한 Long이다. 약 $6·market cap $1.9bn에서 Business Services $1.0bn과 International $1.3bn만으로 equity를 설명하고 Retail $1.0bn을 free option으로 봤다. internet은 incumbent의 order-processing cost를 낮추고 Viking·contract delivery를 강화할 수 있다는 반론이었다.",
valuation="원문 rough SOTP는 BSG $1.0bn+International $1.3bn+Retail $1.0bn=$3.3bn 대 market cap 약 $1.9bn이다. 다만 shared corporate cost·working capital·store lease·tax를 각 사업에 배분해야 한다. Base는 BSG+International의 net value가 시총을 지지하고 retail stabilization이 upside를 만드는 구조다.",
actual="2001 International sales는 reported +6%, FX 제외 +11%, Viking local-currency comparable sales +11%였다. fixed-cost leverage와 mailing efficiency가 개선되고 direct/internet channel은 retail을 단순 대체하기보다 multichannel로 흡수됐다. tactical SOTP·회복 방향은 확인됐지만 long-term office-supply secular decline은 후속 기간에 남았다.",
price="현 첨부 SQL에는 catalyst 239자만 있고 description·performance는 없다. 기존 수익률이나 '2001 강한 반등'의 정확 수치는 사용하지 않는다. 약 $6와 SOTP $3.3bn만 T0 anchor이며 exact return/IRR은 null이다.",
drivers="시장 전체를 low-quality retailer로 묶었지만 International/Viking의 local-currency growth와 BSG의 delivery economics가 달랐다. 극단적 SOTP discount가 단기 하방을 만들고 retail stabilization이 option 역할을 했다. 장기에는 digitization·Amazon/marketplaces라는 다른 thesis가 필요했다.",
error="BSG·International에 독립 multiple을 주면서 corporate overhead·lease·inventory capital을 중복 누락할 수 있다. internet을 기회로 보는 것은 맞았지만 customer acquisition과 price transparency가 장기 gross margin을 낮출 가능성은 과소평가했다.", first_signal="International local-currency comps가 5% 아래로 내려가고 BSG delivery margin도 악화하거나, Retail comps 안정에도 consolidated FCF가 재고·capex 때문에 음수면 SOTP floor를 낮춘다.",
metrics=[("Entry", "약 $6", "SOTP discount 축소", "exact return null", "방향 성공"),("Market cap", "$1.9bn", "SOTP $3.3bn", "자산 운영 지속", "가치 방향"),("BSG", "$1.0bn", "시총 지원", "후속 운영", "부분 검증"),("International", "$1.3bn", "local growth", "+11% FX 제외 2001", "성공"),("Viking comps", "성장 기대", "double digit", "+11% local currency", "성공")],
timeline=[("1999~2000", "superstore saturation 우려", "multiple 압축"),("2000-07-28", "VIC Long", "약 $6 SOTP"),("2000-H2", "Retail comps 약 -1%", "stabilization test"),("2001", "International +11% ex-FX", "hidden asset 확인"),("2001", "Viking local comps +11%", "direct engine"),("2002", "multichannel 운영 확대", "internet 반론"),("2013", "OfficeMax 결합", "legacy consolidation path")],
claimdata=[("International hidden gem", "Viking/International이 $1.3bn 가치다.", "local growth·direct model", "FX·country cost 뒤 cash가 남는다.", "local comps<5%면 반증.", "+11% ex-FX/local comps", "성공 방향", "해외사업은 reported와 local currency를 나눈다."),("BSG floor", "contract delivery $1.0bn이 equity를 지지한다.", "customer relationships·warehouse", "standalone overhead 후 cash가 난다.", "retention·margin 동시 하락이면 반증.", "사업은 지속했으나 독립 매각 없음", "부분", "SOTP는 shared cost를 완전 배분한다."),("Retail free option", "Retail $1.0bn을 거의 무료로 얻는다.", "-1% comps는 collapse 아님", "lease·inventory가 negative value가 아니다.", "store four-wall cash 음수면 반증.", "단기 stabilization 방향", "부분 성공", "free option에도 closure liability가 있다."),("internet 기회", "ODP.com이 주문비용을 낮춘다.", "incumbent fulfillment·customer base", "price transparency가 margin을 더 깎지 않는다.", "online CAC+fulfillment>store saving이면 반증.", "multichannel로 통합", "방향 성공", "disruption은 incumbent의 own-channel economics도 본다."),("$3.3bn SOTP", "세 사업 합계가 $1.9bn 시총보다 크다.", "rough segment values", "net debt·tax·overhead가 제한적이다.", "net SOTP<$1.9bn이면 반증.", "사업회복이 가치방향 지지", "방향 성공", "gross SOTP를 common net value로 변환한다."),("raw direction", "flag Short가 아니라 purchase Long이다.", "원문 action·upside", "동일 security를 산다.", "short payoff 문장이 확인되면 반증.", "Long으로 교정", "성공", "direction은 원문 payoff로 정한다.")]),

I(id="535c4dae-c4b8-41d1-a42a-44aa5a84e109", date="2007-03-22", author="mark778", ticker="ODP", entity="Office Depot, Inc.", group="odp", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="6~12개월", filename="analysis/ideas/2007/2007-03-22_ODP_long.md", link="https://www.valueinvestorsclub.com/idea/Office_Depot/3196828671", desc=0, cat=230, title="Odland turnaround 2단계·margin expansion Long", verdict="매출·margin·투자·buyback 핵심 실패, 정확 수익률 미검증", score=3.4, process=6.7,
summary="raw Short와 달리 약 13x 2008E EPS, low-$40s target과 +25%를 제시한 Long이다. Odland 체제에서 US Retail margin +210bp, BSD +120bp, G&A 절감과 17% share repurchase가 이미 나타났고, 150개 신규매장·remodel·salesforce 투자 뒤에도 연 30bp margin expansion과 mid-high teens EPS growth가 이어진다고 봤다.",
valuation="원문은 약 13x 2008E EPS에서 6~12개월 +25%, low-$40s를 기대했다. forward P/E의 denominator는 mid-high single-digit sales growth, 연 30bp margin expansion과 buyback을 동시에 요구했다. cycle stress에서는 comps +1%가 negative로 바뀌고 fixed store/salesforce cost가 남으므로 EPS와 buyback capacity가 함께 무너진다.",
actual="2008 North American Retail sales는 10% 감소하고 operating profit은 2007 $354.5m에서 -$29.2m으로 붕괴했다. BSD sales는 8% 감소, operating profit은 $220.1m에서 $119.8m으로 줄었다. cost-cutting 1단계 뒤 expansion investment가 operating leverage가 아니라 reverse leverage가 됐고 buyback은 liquidity를 소모했다.",
price="첨부 SQL에는 catalyst 230자만 있고 description·performance가 없다. 기존 성과값은 사용하지 않는다. 13x 2008E·+25%·low-$40s target만 T0 anchor이고 exact return/IRR은 null이다. 다만 공식 영업실적은 thesis의 강한 실패를 판정하기 충분하다.",
drivers="손실원인은 단순 GFC 예측 실패가 아니라 T0에 이미 보인 comps 둔화와 높은 fixed-cost investment를 정상화 EPS에 넣지 않은 것이다. store expansion·remodel·salesforce와 buyback을 동시에 실행해 downturn의 cash runway를 줄였다.",
error="peer margin gap을 자동 upside로 보고 1단계 cost cut의 쉬운 개선을 2단계 growth investment ROIC로 외삽했다. +1% comps에서 150 stores를 더하고 buyback까지 하는 capital allocation을 stress하지 않았고, 13x forward P/E를 마치 current cash yield처럼 취급했다.", first_signal="Retail comps가 0% 아래로 내려가고 new/remodeled-store cohort의 four-wall return이 hurdle을 밑돌거나, BSD margin이 두 분기 연속 감소하면서 buyback이 계속되면 2008E EPS와 target을 즉시 폐기한다.",
metrics=[("Valuation", "약 13x 2008E", "+25%/low-$40s", "E 붕괴·price null", "실패"),("Retail margin", "과거 +210bp", "+30bp/년", "$354.5m→-$29.2m", "대실패"),("BSD margin", "과거 +120bp", "빠른 rebound", "$220.1m→$119.8m", "실패"),("Store plan", "150 신규매장", "positive ROIC", "downturn fixed-cost", "실패"),("Buyback", "55m주/17% 선행", "$200~250m/년", "liquidity 방어와 충돌", "실패")],
timeline=[("2004", "Steve Odland 취임", "turnaround 시작"),("2005~06", "margin 개선·55m주 repurchase", "1단계 성공"),("2007-03-22", "VIC Long", "13x·+25%"),("2007", "Retail comps 약 +1%", "첫 경고"),("2007", "150 store/remodel 투자", "fixed-cost 확대"),("2008", "Retail sales -10%·영업적자", "핵심 반증"),("2009-02", "FY08 결과 공시", "강한 실패 확정")],
claimdata=[("margin +30bp", "비용절감·scale로 매년 margin이 오른다.", "선행 Retail +210bp", "쉬운 cost cut 뒤에도 개선 여지가 같다.", "comps≤0에서 margin 하락이면 반증.", "Retail profit→-$29.2m", "대실패", "turnaround 1·2단계의 driver를 분리한다."),("new-store/remodel ROIC", "150 stores와 remodel이 성장·returns를 만든다.", "management plan", "cohort sales가 fixed cost를 넘는다.", "cohort payback 지연이면 반증.", "downturn에 reverse leverage", "실패", "incremental ROIC를 cohort별로 본다."),("BSD rebound", "salesforce 투자 뒤 margin이 빠르게 돌아온다.", "과거 +120bp", "business spending이 유지된다.", "sales·profit 동시 하락이면 반증.", "sales -8%·profit -46%", "실패", "B2B도 credit/business cycle에 민감하다."),("buyback accretion", "$200~250m/년 repurchase가 EPS를 높인다.", "55m주/17% 선행", "business cash가 안정적이다.", "FCF 약화에도 매입 지속이면 반증.", "cycle buffer를 소모", "실패", "cyclical buyback은 downturn liquidity 뒤에 둔다."),("13x forward EPS", "reset된 기대에서 13x는 싸다.", "mid-high teens EPS growth", "2008E denominator가 견조하다.", "EPS estimate -20%면 반증.", "영업이익 붕괴", "실패", "forward P/E는 sales·margin bridge로 되푼다."),("raw direction", "Short flag와 달리 low-$40s upside Long이다.", "+25% payoff 문장", "동일 common 기준이다.", "borrow/negative target가 확인되면 반증.", "Long으로 교정", "성공", "metadata보다 payoff를 우선한다.")]),
]


def idea_sources(idea):
    link = idea["link"]
    desc_note = f"description {idea['desc']} chars" if idea["desc"] else "description absent"
    raw = m.S(
        "첨부 SQL catalyst / prior curated metadata",
        link,
        "VIC_IDEAS(4).sql / VIC / repository prior overlay",
        idea["date"],
        f"idea_id·catalyst {idea['cat']} chars·{desc_note}; date·author·raw flag·원문 anchor는 prior overlay 대조",
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
    text = text.replace("Batch 046 canonical report.", "Batch 053 canonical report.")
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
        "원문·metadata: **B/C** — 첨부 SQL에는 catalyst 10건과 description 1건만 있다. 누락된 date·author·raw flag·원문 수치는 prior curated overlay를 별도 provenance로 대조했다.",
    )
    text = text.replace(
        "기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.",
        "기업·사건: **A/B** — SEC·회사 IR·감사보고서로 segment 결과와 후속 사건을 검증했다.",
    )
    text = text.replace(
        "가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
        "가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. 기존 overlay 성과값을 폐기하고 exact return/IRR을 모두 null로 재설정했다.",
    )
    return text


def payload():
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(IDEAS)
    finally:
        m.idea_sources = old
    out["batch"] = 53
    out["title"] = "New England Realty / Owens Corning / Office Depot — Cycle, Causal Claims and Turnaround V9"
    null_keys = (
        "perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y",
        "idea_return_1y", "idea_return_3y", "idea_return_5y",
    )
    for idea, master, post in zip(IDEAS, out["ideas_master"], out["postmortems"]):
        master["security_ko"] = idea["security"]
        master["performance_available"] = 0
        master["contest_winner"] = int(idea["contest"])
        master["auto_tag_status_ko"] = "current SQL catalyst 감사·원문 direction 수동교정·성과 null"
        for key in null_keys:
            master[key] = None
        post["research_direction_ko"] = f"{idea['direction']} / {idea['security']}"
        post["research_status_ko"] = "SQL catalyst·available description·공식 실적 검증; performance COPY 부재로 exact return null"
        post["confidence"] = 0.94 if idea["desc"] else (0.90 if idea["link"] else 0.84)
    return out


def make_index():
    rows = []
    for n, idea in enumerate(IDEAS, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['entity']} | {raw}→**{idea['direction']}** | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 053 — New England Realty / Owens Corning / Office Depot — V9 Index", "",
        f"> Research as-of {ASOF}. Batch 052 다음 10건이다. **10 idea = 10 canonical reports**이며 현재 첨부 SQL에 없는 성과값은 모두 null 처리했다.", "",
        "## 0. 배치 결론", "",
        "이 배치는 같은 기업이라도 `법적 재편`, `cycle earnings`, `entry expectation`을 분리해야 한다는 사례다. NEN 2019는 NAV 할인 자체보다 rent reset과 discount buyback의 주당가치 복리이고, OC 7건은 2007 post-reorg timing 실패에서 2018 expectation reset까지 normalized earnings의 질이 어떻게 달라지는지를 보여준다. ODP는 2000 SOTP tactical Long과 2007 turnaround extrapolation 실패를 대비한다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | 실제 회사 | raw→연구 방향 | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|", *rows, "",
        "## 2. SQL / Direction / Security Audit", "",
        "첨부 `VIC_IDEAS(4).sql`에는 `catalyst·companies·descriptions` COPY만 있고 `ideas·performance` data COPY는 없다. Batch 053의 catalyst는 10건 모두 있으나 description은 OC 2007-12 한 건(13,193자)뿐이다. 기존 overlay의 성과비율 8건은 provenance가 없어 모두 폐기했다. date·author·raw flag·source link는 prior curated metadata로 남기되 현재 attachment보다 낮은 등급으로 표시했다.", "",
        "방향은 실제 payoff로 재감사했다. OC 2015-01은 2015-04 후속 글이 직접 Long thesis라고 명시하고, ODP 2000·2007은 purchase·상승 target을 제시하므로 raw Short→실제 Long이다. NEN 2019는 2012 split 이후 **Depositary Receipt=1/30 Class A Unit**이고 나머지는 common이다.", "",
        "## 3. NEN — NAV discount보다 주당가치 복리", "",
        "약 $53의 10~11% FCF yield, replacement cost/NAV 할인은 출발점이다. 장기 payoff는 `under-market rent reset→NOI 증가→NAV 아래 buyback→receipt당 ownership 증가`다. 반증은 cap-rate 하나가 아니라 occupancy·same-unit NOI·mortgage reset·repurchase 실행이다. 200%/10년 total return은 현 데이터로 미검증이다.", "",
        "## 4. Owens Corning — 같은 company, 다른 expectation", "",
        "| 시점 | 무엇을 샀나 | 핵심 오류/edge | 판정 |", "|---|---|---|---|",
        "| 2007-01 | asbestos 제거·fresh start | legal clean-up을 cycle bottom과 혼동 | timing 실패 |",
        "| 2007-12 | $20.60·3.7x normalized EBITDA | segment margin을 재구축·GFC path 과소평가 | 장기 방향 성공 |",
        "| 2013 | Roofing cash+Insulation 흑자전환 | dollar EBIT bridge | 사업 성공 |",
        "| 2015-01/04 | asphalt deflation | cost 적중, flat selling price 실패 | causal 부분 성공 |",
        "| 2017 | 세 segment 동시 정상화·10% FCF | 좋은 실적이 peak expectation일 수 있음 | 기간 사업 성공 |",
        "| 2018-12 | 48% drawdown·8.5x normal EPS | 악재가 보인 뒤 낮아진 기대 | 강한 방향 성공 |", "",
        "## 5. Office Depot — tactical SOTP와 turnaround 2단계", "",
        "2000 Long은 BSG $1.0bn+International $1.3bn이 $1.9bn 시총을 설명하고 Retail $1.0bn을 option으로 둔 SOTP였다. 2001 International/Viking local-currency growth가 이를 지지했다. 2007 Long은 이미 달성한 cost-cutting margin을 150 신규매장·remodel·salesforce 투자와 buyback 뒤에도 외삽했다. 2008 Retail 영업이익 $354.5m→-$29.2m, BSD $220.1m→$119.8m으로 denominator가 붕괴했다.", "",
        "## 6. 공통 투자 교훈", "",
        "1. post-reorg legal clean-up은 earnings-cycle bottom이 아니다.\n2. normalized multiple은 segment volume·price·utilization에서 다시 만든다.\n3. 결과가 좋아도 price·cost·volume claim을 각각 사후검증한다.\n4. channel check와 price letter는 realized invoice가 아니다.\n5. 모든 segment 동시호전은 upside이자 peak-expectation 경고다.\n6. cyclical FCF yield는 다음 downturn의 운전자본·capex로 stress한다.\n7. SOTP에는 shared cost·lease·tax·working capital을 완전 배분한다.\n8. turnaround 2단계는 과거 cost cut이 아니라 incremental investment ROIC다.\n9. buyback은 downturn liquidity 이후에만 accretive하다.\n10. performance COPY가 없으면 exact return은 null이다.", "",
        "## 7. 산출물", "",
        "- Payload: `data/curated/batch_053_nen_oc_odp_deep_v7.json`\n- Wrapper: `analysis/batch_053_nen_oc_odp_10.md`\n- Source packet: `data/curated/batch_053_source_packet.json`\n- Builder: `scripts/53_build_batch_053_v9.py`", "",
    ])


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 053 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or len(idea_sources(idea)) < 5:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(idea["filename"]).relative_to("analysis").as_posix() for idea in IDEAS]
    wrapper = "# Batch 053 — New England Realty / Owens Corning / Office Depot V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit wrapper. [Batch 053 V9 Index](batch_053_v9_index.md).\n"
    (ROOT / "analysis/batch_053_nen_oc_odp_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_053_v9_index.md").write_text(make_index(), encoding="utf-8")
    out = payload()
    (ROOT / "data/curated/batch_053_nen_oc_odp_deep_v7.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {
        "batch": "053", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + prior curated metadata + official filings",
        "record_count": 10, "raw_descriptions_present": 1, "raw_catalysts_verified": 10,
        "current_attachment_performance_rows_found": 0, "legacy_overlay_performance_values_discarded": 8,
        "direction_corrections": 3, "security_normalizations": 10,
        "performance_rule": "No performance COPY in current attachment; all exact returns remain null",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"],
            "raw_direction": "Short" if i["raw_short"] else "Long", "research_direction": i["direction"], "security": i["security"],
            "description_chars": i["desc"], "catalyst_chars": i["cat"], "performance_available": False,
            "canonical_report": i["filename"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_053_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10,
        "copy_tables_present": ["catalyst", "companies", "descriptions"], "idea_rows_in_attachment": 0,
        "raw_descriptions_present": 1, "raw_descriptions_absent": 9, "raw_catalysts_verified": 10,
        "description_chars_by_idea": {i["id"]: i["desc"] for i in IDEAS},
        "catalyst_chars_by_idea": {i["id"]: i["cat"] for i in IDEAS},
        "performance_copy_present": False, "performance_rows_found": 0, "legacy_overlay_rows_nullified": 8,
        "note": "Current attachment controls. Missing original descriptions rely on prior curated metadata at lower provenance; official filings control actual outcomes.",
    }
    (ROOT / "data/curated/batch_053_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(out[key]) for key in ("ideas_master", "postmortems", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
