#!/usr/bin/env python3
"""Build Batch 064 canonical V9 reports and the production overlay.

The source catalog for this batch was intentionally kept in staging until every
idea had an individual 0--12 report and the complete structured V9 tables.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
WEIGHTS = [20, 18, 18, 16, 16, 12]
CATALOG = ROOT / "data/curated/batch_064_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_064_aep_atlas_aepi_aer_deep_v7.json"


def C(title, verdict, original, mechanism, evidence, assumption, falsifier,
      actual, gap, error, lesson):
    return dict(title=title, verdict=verdict, original=original,
                mechanism=mechanism, evidence=evidence, assumption=assumption,
                falsifier=falsifier, actual=actual, gap=gap, error=error,
                lesson=lesson)


def S(title, url, publisher, date, evidence, source_type="1차자료"):
    return dict(title=title, url=url, publisher=publisher, date=date,
                evidence=evidence, type=source_type)


BUSINESS = {
    "utility": (
        "American Electric Power는 여러 주의 regulated electric utility와 당시 merchant generation·trading 자산을 "
        "보유했다. 규제 utility는 승인 rate base에 허용 ROE를 곱해 수익을 얻지만 fuel·stranded cost 회수의 시점은 "
        "주 규제기관·법원·securitization 구조에 달려 있다. merchant 사업은 전력가격과 spark spread에 노출된다."
    ),
    "plantation": (
        "당시 Anglo-Eastern Plantations, 현재 AEP Plantations는 인도네시아·말레이시아에서 oil-palm estate와 mill을 "
        "운영한다. 토지를 식재한 뒤 약 3년부터 열매를 수확하고 수령이 올라가며 ha당 FFB yield가 성숙한다. CPO·kernel "
        "판매가에서 estate·mill·물류·재식재·세금과 개발 capex를 뺀 현금이 주주에게 귀속된다."
    ),
    "atlas": (
        "Atlas Engineered Products는 캐나다의 지역 truss·wall panel·engineered wood 제조사를 인수·통합한다. 제품이 "
        "부피가 크고 설계·permit·납기가 지역별이라 장거리 운송이 비경제적이다. 매출은 lumber 가격 pass-through의 "
        "영향을 받으므로 revenue growth보다 volume, gross margin, acquisition multiple, debt와 주당 EBITDA가 중요하다."
    ),
    "aepi": (
        "AEP Industries는 polyethylene·PVC flexible packaging film을 생산했다. resin 가격을 고객에게 넘기기까지 시차가 "
        "있어 핵심 경제성은 매출이 아니라 `판매 lbs × spread/lb`다. food·beverage 수요는 방어적이지만 housing·industrial "
        "volume은 경기민감하며, 높은 utilization·운전자본·차입금과 자사주가 주당가치를 크게 바꾼다."
    ),
    "aimia": (
        "Groupe Aeroplan은 뒤에 Aimia로 사명을 바꾸고 coalition loyalty program을 운영했다. 은행·항공사·소매업체에 "
        "포인트를 선판매해 현금을 먼저 받고 redemption 때 비용을 인식한다. spread·breakage·float는 매력적이지만 anchor "
        "airline과 카드 파트너가 이탈하면 미래 billings와 보상의 효용이 동시에 약해진다."
    ),
    "aercap": (
        "AerCap은 항공기를 OEM 또는 sale-leaseback으로 취득해 항공사에 장기 임대하는 항공금융회사다. lease rent와 "
        "maintenance receipts에서 funding cost·감가상각·관리비·credit loss를 뺀 spread, 그리고 재임대·매각 residual value가 "
        "ROE를 결정한다. 이동 가능한 자산이어도 기종·연식·정비상태와 레버리지가 equity tail risk를 만든다."
    ),
}


ENGINE = {
    "utility": "`rate base × allowed ROE + merchant margin - interest - capex - tax = equity earnings/FCF`; regulatory recovery와 debt reduction을 별도 추적한다.",
    "plantation": "`mature ha × FFB yield/ha × extraction rate × CPO price - estate/mill cost - tax - sustaining/development capex = equity cash flow`.",
    "atlas": "`regional volume × selling price - lumber/labour - plant overhead - integration cost - interest - capex = equity FCF`; M&A는 dilution까지 주당으로 계산한다.",
    "aepi": "`pounds sold × gross spread/lb - conversion/SG&A - cash interest - capex - working capital = equity FCF`; 매출은 resin 가격 때문에 오해를 부른다.",
    "aimia": "`gross billings + ancillary revenue - redemption cost - opex - tax ± reserve/working-capital change = equity FCF`; float와 경제적 부채를 함께 본다.",
    "aercap": "`lease revenue + maintenance + gain on sale - interest - depreciation - credit loss - opex - tax = equity earnings`; book value를 실제 판매 gain과 손실로 검증한다.",
}


KPI = {
    "utility": "regulated EPS, allowed ROE, rate-base growth, stranded-cost recovery cash, merchant exposure, asset-sale net proceeds, debt/capital, dividend coverage",
    "plantation": "mature/immature ha, age profile, FFB yield/ha, oil extraction rate, CPO price, cash cost/t, replanting·development capex, net cash, RSPO/ISPO status",
    "atlas": "organic volume, lumber pass-through, gross margin, normalized EBITDA, acquisition multiple, integration cost, net debt, fully diluted shares, housing starts",
    "aepi": "lbs sold, spread/lb, resin pass-through lag, capacity utilization, adjusted EBITDA, working capital, net debt, capex, shares outstanding",
    "aimia": "gross billings, active members, miles issued/redeemed, cost per mile, breakage, redemption reserve, FCF, partner concentration, contract expiry",
    "aercap": "lease yield, funding cost, utilization, collections, gain on sale, impairments, debt/equity, secured debt, book/share, ROE, buybacks",
}


US_UTILITY_SOURCES = [
    S("AEP 2003 Form 10-K", "https://www.sec.gov/Archives/edgar/data/4904/000000490404000055/form10k.txt", "SEC / American Electric Power", "2004-03-11", "T0 직후 segment·debt·regulatory·asset-sale risk 검증."),
    S("AEP 2004 Form 10-K", "https://www.sec.gov/Archives/edgar/data/4904/000101540205001007/aep10k04.htm", "SEC / American Electric Power", "2005-03-01", "cost reduction, merchant exit와 재무구조 진행 검증."),
    S("AEP 2005 Form 10-K", "https://www.sec.gov/Archives/edgar/data/4904/000000490406000034/ye05aep10k.htm", "SEC / American Electric Power", "2006-03-01", "asset-sale proceeds·debt·EPS bridge 검증."),
    S("AEP Q2 2006 Form 10-Q", "https://www.sec.gov/Archives/edgar/data/4904/000000490406000148/q206aep10q.htm", "SEC / American Electric Power", "2006-08-04", "Texas stranded-cost securitization과 현금회수 검증."),
    S("AEP 2006 Form 10-K", "https://www.sec.gov/Archives/edgar/data/4904/000000490407000041/ye06aep10k.htm", "SEC / American Electric Power", "2007-02-28", "2006 EPS·year-end 주가·사업구성 검증."),
    S("AEP FY2006 earnings", "https://www.aep.com/news/stories/view/892/AEP-reports-2006-fourthquarter-fullyear-earnings/", "American Electric Power", "2007-01-25", "2006 GAAP·ongoing EPS와 guidance 검증."),
]


PLANTATION_SOURCES = [
    S("AEP reports and presentations archive", "https://aepplantations.com/investors/reports-and-presentations/", "AEP Plantations", "2026", "2012·2024·2025 annual report 공식 보관 위치."),
    S("Anglo-Eastern Plantations 2024 annual report", "https://www.angloeastern.co.uk/~/media/Files/A/Anglo-Eastern/reports-and-documents/AEP%20AR2024_Final.pdf", "Anglo-Eastern Plantations", "2025-04", "2024 생산·손익·net cash·순자산 검증."),
    S("AEP Plantations official business overview", "https://aepplantations.com/", "AEP Plantations", "2026", "현재 사업지역·상장·estate/mill 구조 검증."),
    S("AEP official name-change notice", "https://aepplantations.com/aep-plantations-plc-announces-official-name-change/", "AEP Plantations", "2026-02-04", "2025-11-24 사명변경과 ticker 유지 검증."),
    S("AEP palm age and production charts", "https://www.angloeastern.co.uk/~/media/Files/A/Anglo-Eastern/documents/Charts%202022.pdf", "Anglo-Eastern Plantations", "2022-12-31", "immature·young·prime·old age mix와 생산 추이 검증."),
]


ATLAS_SOURCES = [
    S("Atlas corporate and operating-company overview", "https://www.atlasengineeredproducts.com/", "Atlas Engineered Products", "2026", "10개 인수, 지역별 회사, 제품·succession roll-up 논리 검증."),
    S("Atlas FY2019 MD&A", "https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2019-MDA-FINAL.pdf", "Atlas Engineered Products", "2020-04-30", "2020 아이디어의 당시 규모·M&A·margin 출발점 검증."),
    S("Atlas FY2021 MD&A", "https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2021-MDA-final.pdf", "Atlas Engineered Products", "2022-04", "2021 record year와 2022 진입 전 run-rate 검증."),
    S("Atlas FY2022 MD&A", "https://www.atlasengineeredproducts.com/dist/assets/images/hero/AEP-F2022-MDA-Final.pdf", "Atlas Engineered Products", "2023-04", "매출 C$61.90m, operating income C$12.53m, adjusted EBITDA C$15.73m, Hi-Tec 조건 검증."),
    S("Atlas FY2022 financial statements", "https://www.atlasengineeredproducts.com/dist/assets/images/hero/Atlas-Engineered-Products-Ltd-Dec-2022-FS.pdf", "Atlas Engineered Products", "2023-04", "감사 재무제표·부채·share count 검증."),
    S("Atlas FY2023 MD&A", "https://www.atlasengineeredproducts.com/dist/assets/images/hero/AEP-F2023-MDA-final.pdf", "Atlas Engineered Products", "2024-04", "매출 C$49.41m, margin 27%, LCF acquisition과 금리민감도 검증."),
    S("Atlas FY2024 MD&A", "https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2024-MDA-final.pdf", "Atlas Engineered Products", "2025-04", "매출 C$55.83m, normalized EBITDA C$8.52m, share issue·robotics 검증."),
    S("Atlas FY2025 MD&A", "https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2025-MDA-final-Compressed.pdf", "Atlas Engineered Products", "2026-04", "2025 매출·normalized EBITDA와 최신 cycle outcome 검증."),
]


AEPI_SOURCES = [
    S("AEP Industries FY2007 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000104746908000285/a2182025z10-k.htm", "SEC / AEP Industries", "2008-01-14", "제품·resin 비중·pass-through·2007 share count 출발점 검증."),
    S("AEP Industries FY2008 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000104746909000421/a2190160z10-k.htm", "SEC / AEP Industries", "2009-01-27", "GFC volume·resin·Atlantis acquisition과 debt 검증."),
    S("AEP Industries FY2009 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000119312510006494/d10k.htm", "SEC / AEP Industries", "2010-01-14", "Atlantis 통합·deleveraging·segment 결과 검증."),
    S("AEP Industries FY2010 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000119312511008295/d10k.htm", "SEC / AEP Industries", "2011-01-14", "resin spread·lbs·EBITDA·repurchase 검증."),
    S("AEP Industries FY2011 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000119312512013914/d244683d10k.htm", "SEC / AEP Industries", "2012-01-17", "Webster acquisition·share count·debt·operating result 검증."),
    S("AEP Industries FY2013 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000119312514010742/d603786d10k.htm", "SEC / AEP Industries", "2014-01-14", "2014 논지 직전 capacity·volume·spread·repurchase 검증."),
    S("AEP Industries FY2015 Form 10-K", "https://www.sec.gov/Archives/edgar/data/785787/000119312516429901/d38513d10k.htm", "SEC / AEP Industries", "2016-01-14", "정상화·M&A·capital allocation 후속 검증."),
    S("AEP Industries merger proxy", "https://www.sec.gov/Archives/edgar/data/785787/000157104916020681/t1603079-defm14a.htm", "SEC / AEP Industries", "2016-12-15", "Berry 거래가치·배경·$110/2.5011 선택·proration 검증."),
    S("AEP Industries merger completion 8-K", "https://www.sec.gov/Archives/edgar/data/785787/000119312517015318/d330949d8k.htm", "SEC / AEP Industries", "2017-01-23", "2017-01-20 종결과 최종 consideration 검증."),
]


AIMIA_SOURCES = [
    S("Air Canada 2013 financial statements", "https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/en/quarterly-result/2013/2013_FSN_q4.pdf", "Air Canada", "2014-02", "Aeroplan points purchase·redemption 관계 검증."),
    S("Air Canada investor presentation", "https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/speeches-presentations/en/Desjardins-Industrials-Telecom-Consumer-Conference-Montreal-en.pdf", "Air Canada", "2016-03", "Aeroplan 계약의 2020 종료시점이 T0부터 계약문서에 존재했음을 검증."),
    S("Aimia definitive Aeroplan sale agreement", "https://www.aimia.com/aimia-and-air-canada-enter-into-definitive-agreement-for-purchase-of-aeroplan-loyalty-business/", "Aimia", "2018-11-26", "C$450m headline cash와 거래구조 검증."),
    S("Air Canada Q3 2018 financial statements", "https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/en/quarterly-result/2018/2018_FSN_q3.pdf", "Air Canada", "2018-10-31", "C$450m 현금·약 C$1.9bn points liability 인수조건 검증."),
    S("Air Canada acquisition proposal", "https://www.td.com/ca/en/about-td/for-investors/investor-relations/news-and-events/news/2018/proposal-by-air-canada-td-cibc-and-visa-to-acquire-aeroplan", "TD / Air Canada consortium", "2018-07-25", "anchor partners가 Aeroplan을 공동 인수하려 한 구조 검증."),
    S("SEC entity check: NYSE AER", "https://www.sec.gov/edgar/browse/?CIK=1378789&owner=exclude", "SEC", "2026", "미국 AER은 AerCap이며 Canadian AER/AIM과 가격 혼용 금지."),
]


AERCAP_SOURCES = [
    S("AerCap shareholders approve ILFC acquisition", "https://www.aercap.com/news-media/press-releases/detail/300/aercap-holdings-n-v-shareholders-approve-acquisition-of", "AerCap", "2014-02-13", "deal 승인과 closing condition 검증."),
    S("AerCap completes ILFC acquisition", "https://www.aercap.com/news-media/press-releases/detail/309/aercap-completes-acquisition-of-ilfc-from-aig-and-closes", "AerCap", "2014-05-14", "$3.0bn cash·97,560,976 shares·46% AIG stake·financing 검증."),
    S("AerCap Q2 2014 aircraft transactions", "https://www.aercap.com/news-media/press-releases/detail/310/aercap-holdings-n-v-completed-122-aircraft-transactions", "AerCap", "2014-07-11", "ILFC 통합 직후 fleet activity 검증."),
    S("AerCap 2016 Form 20-F", "https://www.sec.gov/Archives/edgar/data/1378789/000137878917000009/aer-20161231x20f.htm", "SEC / AerCap", "2017-03-06", "2016 diluted EPS $5.52, fleet·funding·book value 검증."),
    S("AerCap 2022 Form 20-F", "https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-23-000006/aer-20221231.htm", "AerCap", "2023-03-02", "COVID·GECAS·러시아 자산손실 이후 재무구조 검증."),
    S("AerCap Q1 2022 results", "https://www.aercap.com/news-media/press-releases/detail/415/aercap-holdings-n-v-reports-financial-results-for-the", "AerCap", "2022-05-17", "러시아 자산 관련 약 $3.5bn 보험청구 검증."),
    S("AerCap 2023 Form 20-F", "https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-24-000010/aer-20231231.htm", "AerCap", "2024-02-23", "fleet·부채·러시아 보험합의·book recovery 검증."),
]


GROUP_SOURCES = {
    "utility": US_UTILITY_SOURCES,
    "plantation": PLANTATION_SOURCES,
    "atlas": ATLAS_SOURCES,
    "aepi": AEPI_SOURCES,
    "aimia": AIMIA_SOURCES,
    "aercap": AERCAP_SOURCES,
}


IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


add(
    id="c688c963-3551-409b-9d66-d46a12dac96b", date="2003-08-27",
    author="sameplot850", ticker="AEP", company="American Electric Power Company",
    filename="analysis/ideas/2003/2003-08-27_AEP_american_electric_power_long.md",
    source="", group="utility", direction="Long", raw_direction="Long",
    security="AEP common equity / Long", entry="원문 약 $27.50",
    horizon="2005~2006 earnings normalization", raw_horizon="Jan-2006 $37 target와 2006 EPS bridge",
    title="regulated-utility cleanup·regulatory cash recovery Long",
    verdict="강한 성공 — regulatory cash·asset sales·EPS와 목표가격이 대체로 실현",
    score=9.5, process=9.6,
    conclusion=(
        "Enron 이후 merchant risk와 높은 debt를 할인한 entry에서 Texas stranded-cost recovery, 비핵심 매각, "
        "비용절감과 regulated earnings 정상화가 순서대로 나타났다. 2006 ongoing EPS는 $2.71로 원문 $2.82에 4% "
        "미달했지만 $37 목표는 2005년 말 종가 $37.09로 사실상 달성했다."
    ),
    t0=(
        "AEP는 merchant trading 실패, 신용등급 압박, Texas restructuring 회수 불확실성과 과다부채 때문에 전형적인 "
        "utility보다 낮은 배수를 받았다. 원문은 $200m 비용절감, 최소 $1.4bn Texas 현금, 최소 $1bn merchant 자산매각, "
        "2006 EPS $2.82와 배당을 연결해 Jan-2006 $37을 제시했다."
    ),
    reverse=(
        "시장은 stranded-cost true-up이 삭감·지연되고 merchant asset이 장부가 이하에 팔리며, 신용등급을 지키기 위한 "
        "equity 발행 또는 배당삭감이 common upside를 흡수할 가능성을 반영했다. 목표가가 되려면 규제·매각·비용절감·" 
        "금리와 utility multiple이 동시에 크게 어긋나지 않아야 했다."
    ),
    valuation=(
        "원문 bridge는 2006 EPS $2.82에 약 13배를 적용해 $37을 산출했다. 이 접근은 EPS를 regulated core, merchant, "
        "asset-sale gain으로 분리하고, 회수 현금이 순부채를 낮추는 만큼만 multiple을 정상화해야 한다. 2006 ongoing EPS "
        "$2.71과 2005말 $37.09는 earnings·multiple 두 축이 모두 대체로 맞았음을 보여준다."
    ),
    actual=(
        "AEP는 2003~05 비핵심·merchant 자산을 처분하고 비용구조를 낮췄다. Texas Central Company는 stranded-cost "
        "securitization으로 현금을 회수했으며 2006 10-Q에 관련 구조가 구체화됐다. FY2006 GAAP EPS $2.29, ongoing EPS "
        "$2.71을 기록했고 regulated utility 중심의 risk profile로 복귀했다."
    ),
    price=(
        "uploaded SQL price-only ratio는 1Y 1.1383, 2Y 1.2990, 3Y 1.2785, 5Y 1.3611이다. 즉 배당 제외로도 2년 약 "
        "+29.9%, 5년 약 +36.1%이며, 2005말 공시 종가 $37.09는 원문 $37 목표와 일치한다. 정확한 total return은 배당을 "
        "포함하지 않아 별도로 주장하지 않는다."
    ),
    drivers=(
        "수익은 고성장이 아니라 불확실성 제거에서 나왔다. regulatory receivable이 현금이 되고, merchant tail이 매각되며, "
        "credit risk가 낮아져 같은 regulated EPS에 더 정상적인 배수가 적용됐다."
    ),
    counterfactual="Texas 회수가 절반으로 줄고 merchant 매각이 2년 늦어져도 배당·등급을 지키며 $37에 도달할 수 있었는가?",
    error="핵심 방향은 맞았지만 서로 독립적이지 않은 규제회수·매각·deleveraging을 base case에 함께 놓아 execution correlation을 작게 봤다.",
    warning="명확한 thesis break는 없었다. 사전 핵심경고는 true-up 승인액 삭감 또는 securitization 지연이었으나 실제 현금화가 진행됐다.",
    first_signal_date="2004-12-31",
    scenarios=[
        ("Bear", "Texas 회수 삭감·매각지연·rating pressure", "$20대·배당위험", "현실화하지 않음"),
        ("Base", "$200m 절감·$2bn+ 현금화·EPS 정상화", "$37", "2005말 $37.09"),
        ("Bull", "merchant 가격·utility multiple 동시개선", "$40+와 배당", "배당 포함 upside 존재")],
    lessons=[
        "regulated utility turnaround는 매출성장보다 regulatory receivable이 실제 현금과 debt reduction으로 바뀌는지를 본다.",
        "asset-sale headline보다 net proceeds와 debt/capital 개선을 추적한다.",
        "EPS target와 multiple target를 분리하면 어느 축이 수익을 만들었는지 보인다."],
    checklist=["규제명령의 승인액·appeal", "securitization closing", "asset-sale net cash", "ongoing vs GAAP EPS", "debt/capital·rating", "배당 coverage"],
    scorecard=[("Business thesis", "성공"), ("Valuation thesis", "성공"), ("Catalyst thesis", "강한 성공"), ("Timing / path", "성공"), ("Security selection", "common 적절")],
    claims=[
        C("$200m cost reduction이 core earnings를 높인다", "대체로 성공", "$200m 구조적 비용절감이 EPS를 끌어올린다.", "fixed O&M 감소가 regulated earnings와 credit metric을 개선한다.", "원문 $200m program.", "절감액이 일회성·merchant 손실에 흡수되지 않는다.", "ongoing O&M 또는 EPS가 개선되지 않으면 반증.", "2006 ongoing EPS가 $2.71까지 정상화했다.", "$2.82 target 대비 -$0.11/-3.9%.", "gross saving을 after-tax EPS로 직접 환산했다.", "cost program은 gross·net·one-time cost를 분리한다."),
        C("Texas true-up에서 최소 $1.4bn 현금", "강한 성공", "regulatory stranded cost를 securitize해 cash를 회수한다.", "확정 regulatory claim을 저금리 채권으로 바꿔 debt를 낮춘다.", "원문 최소 $1.4bn 회수.", "PUCT·법원결정과 financing market이 허용한다.", "승인액이 크게 삭감되거나 securitization이 지연되면 반증.", "2006 공시에 Texas securitization과 관련 현금화가 반영됐다.", "방향·규모가 thesis를 지지.", "legal entitlement와 현금입금 사이 기간위험을 단순화했다.", "규제자산은 order·appeal·bond close·cash의 네 단계로 본다."),
        C("merchant asset sale로 최소 $1bn", "성공", "비핵심 발전·trading 자산을 매각해 balance sheet를 정리한다.", "volatile EBITDA를 없애고 net proceeds로 leverage를 낮춘다.", "원문 최소 $1bn proceeds.", "buyer liquidity와 자산가치가 유지된다.", "매각손실·지연 또는 proceeds가 debt 감소로 이어지지 않으면 반증.", "2004~05 매각과 사업축소가 진행됐다.", "정확한 동일자산 합계보다 방향이 확인됨.", "headline value와 after-tax net cash를 혼용할 위험.", "asset sale은 net cash/debt 비율로 검증한다."),
        C("deleveraging이 utility multiple을 회복", "성공", "회수·매각 현금이 rating risk를 낮춘다.", "credit spread와 equity risk premium이 내려가면 P/E가 정상화된다.", "높은 debt와 rating pressure가 할인 원인.", "회수현금이 capex·배당에 소비되지 않는다.", "debt/capital과 rating이 개선되지 않으면 반증.", "risk profile이 regulated utility 중심으로 이동하고 목표배수가 실현됐다.", "$37 target를 2005말 달성.", "multiple 회복을 금리·sector rerating과 완전히 분리하지 못했다.", "deleveraging과 market beta 기여를 따로 기록한다."),
        C("2006 EPS $2.82", "거의 성공", "비용절감·이자감소·regulated earnings로 $2.82를 번다.", "operating improvement와 lower debt가 주당이익에 결합한다.", "원문 2006 model.", "share count와 정상화 조정이 안정적이다.", "ongoing EPS가 10% 이상 미달하면 반증.", "2006 ongoing EPS $2.71.", "-$0.11/-3.9%.", "point estimate의 오차범위를 제시하지 않았다.", "EPS target는 ±10% band와 bridge로 판정한다."),
        C("Jan-2006 $37 target", "성공", "$27.50에서 $37과 배당을 기대한다.", "EPS 정상화와 P/E rerating이 price를 만든다.", "2006E EPS × 약 13배.", "촉매가 horizon 내 실현된다.", "2005~06 가격이 $37에 도달하지 못하면 실패.", "2005말 공시 종가 $37.09.", "price target 사실상 일치.", "배당포함 IRR과 point-in-time target hit을 구분해야 한다.", "target hit·holding-period return·total return을 각각 기록한다."),
    ],
    metrics=[("Entry / target", "$27.50 / $37", "+34.5%+배당", "2005말 $37.09", "성공"), ("2006 ongoing EPS", "T0 $2.82", "$2.82", "$2.71", "-3.9%"), ("Texas cash", "≥$1.4bn", "securitization", "공시상 실행", "성공"), ("Merchant proceeds", "≥$1bn", "debt reduction", "다년 매각 실행", "성공"), ("2Y price-only", "Long", "상승", "+29.9%", "성공")],
    timeline=[("2003-08-27", "VIC Long 게시", "$27.50→$37 cleanup thesis"), ("2004", "비핵심·merchant 매각 지속", "risk reduction"), ("2005-12-31", "주가 $37.09", "target 달성"), ("2006-01", "Texas true-up 관련 결정·financing", "규제 cash crystallization"), ("2006-08-04", "Q2 10-Q securitization 공시", "cash/debt bridge 확인"), ("2006-12-31", "ongoing EPS $2.71", "$2.82에 근접"), ("2007-01-25", "FY2006 results", "thesis 수치 확정")],
)


add(
    id="af921c81-54cb-4c7c-aedd-2ab684b5701c", date="2012-06-11",
    author="Den1200", ticker="AEP", company="Anglo-Eastern Plantations Plc / AEP Plantations Plc",
    filename="analysis/ideas/2012/2012-06-11_AEP_anglo_eastern_plantations_long.md",
    source="", group="plantation", direction="Long", raw_direction="Short",
    security="LSE:AEP common equity / Long", entry="원문 약 $4.2k~5.2k per planted ha",
    horizon="수령 성숙과 재투자가 진행되는 3~7년", raw_horizon="명시적 단기 target보다 ha당 가치·maturation thesis",
    title="plantation EV/ha·immature-acreage maturation Long",
    verdict="장기 성공 — 생산기반·순현금·순자산 compounding, SQL 성과행은 폐기",
    score=8.8, process=9.7,
    conclusion=(
        "낮은 planted-ha 가격과 이미 집행된 immature acreage의 성숙이라는 논지는 생산·순현금·순자산 증가로 장기 검증됐다. "
        "2012 net cash $91.2m에서 2024 $181.9m, 2024 attributable profit $67.5m·shareholder net assets $551.0m으로 커졌다. "
        "다만 SQL 가격은 미국 American Electric Power라 이 아이디어의 수익률로 쓸 수 없다."
    ),
    t0=(
        "원문은 mature planted area 약 39.8k ha와 큰 immature acreage를 replacement 약 $8k/ha, private deals $15k~20k/ha보다 "
        "낮은 $4.2k~5.2k/ha에 산다고 봤다. CPO 가격을 맞히기보다 높은 oil yield, low-cost estate와 maturation·내부재투자의 "
        "시간가치를 강조했다."
    ),
    reverse=(
        "할인은 단순 무지가 아니라 commodity price, Indonesia land title·세금·환율, related-party governance, replanting capex와 "
        "ESG·deforestation risk를 반영했다. ha당 거래가치는 법적권리·수령·접근성·mill capacity가 다르면 비교가 무너진다."
    ),
    valuation=(
        "원문의 핵심은 EV/ha를 replacement와 private transaction에 비교하고, immature ha의 mature yield를 별도로 더하는 SOTP였다. "
        "정교한 모델은 hectare를 immature·young·prime·old로 나누고 각 yield curve, CPO margin, tax, development/replanting capex와 "
        "country haircut을 적용해야 한다."
    ),
    actual=(
        "2012 FFB는 783.4k mt(+11%), CPO는 260.5k mt(+5%)였고 CPO 평균가격이 하락해도 net cash $91.2m을 유지했다. 2024 revenue "
        "$372.3m, operating profit $81.7m, attributable profit $67.5m, net cash $181.9m, shareholder net assets $551.0m이었다. "
        "회사는 2025-11-24 AEP Plantations로 사명을 바꿨지만 LSE ticker는 유지했다."
    ),
    price=(
        "SQL의 $27대 price series는 NYSE American Electric Power에 해당해 전부 rejected다. LSE corporate actions·GBP dividends를 "
        "복원한 별도 series 없이 exact return·MFE·MAE를 만들지 않는다. 사업·자산가치 판정과 주가성과 판정을 분리한다."
    ),
    drivers="가치는 CPO spot multiple보다 이미 심은 나무의 생물학적 성숙, yield 증가, low-cost mill integration과 내부현금 재투자·net cash 축적에서 나왔다.",
    counterfactual="CPO가 $750/t로 5년 머물고 replanting·ESG capex가 두 배여도 mature ha와 net cash를 보수적으로 평가한 downside가 현재 EV를 지지하는가?",
    error="per-ha private deal 비교에서 land title·age·mill·minority·country risk를 충분히 층화하지 않았고 exact shareholder return data를 확보하지 못했다.",
    warning="commodity 가격하락은 관찰됐지만 balance sheet와 생산량이 버텼다. 사전 핵심경고는 yield/ha 하락과 net cash 소진이었으나 장기적으로 현실화하지 않았다.",
    first_signal_date="2012-12-31",
    scenarios=[("Bear", "CPO $750·yield 저하·개발중단", "자산할인 지속", "순현금으로 방어"), ("Base", "immature maturation·보수적 CPO", "생산·NAV compounding", "장기 실현"), ("Bull", "private $15k+/ha·높은 CPO", "큰 SOTP rerating", "exact price 검증 안 함")],
    lessons=["plantation은 P/E보다 EV/ha를 tree-age·yield/ha·mill capacity와 함께 본다.", "immature acreage는 성장설비지만 이미 쓴 capex와 앞으로 필요한 upkeep을 함께 반영한다.", "ticker/entity가 틀리면 가격성과 전체를 폐기한다."],
    checklist=["mature/immature ha", "FFB yield/ha", "extraction rate", "CPO unit margin", "replanting·development capex", "land title·certification", "net cash", "GBP total-return series"],
    scorecard=[("Business thesis", "강한 성공"), ("Valuation thesis", "방향 성공"), ("Catalyst thesis", "maturation 장기 실현"), ("Timing / path", "commodity 혼합"), ("Data quality", "SQL return 무효")],
    claims=[
        C("planted ha를 replacement 이하에 매수", "성공 방향", "$4.2k~5.2k/ha는 replacement $8k와 private $15k~20k보다 싸다.", "동일 질의 estate가 더 높은 대체·거래가치를 가지면 NAV discount가 크다.", "원문 ha와 거래비교.", "title·age·mill·country risk가 충분히 유사하다.", "장기 net asset가 식재가치보다 낮아지면 반증.", "2024 shareholder net assets $551.0m과 순현금이 축적됐다.", "exact LSE rerating은 미검증.", "질이 다른 hectare를 한 가격으로 비교했다.", "ha는 legal title·age·yield·mill·access별로 haircut한다."),
        C("immature acreage가 내재성장", "성공", "이미 심은 acreage가 성숙하며 생산을 늘린다.", "추가 토지구매 없이 tree-age yield curve가 FFB를 증가시킨다.", "2012 mature 약 39.8k ha와 immature mix.", "agronomy·weather·replanting이 정상이다.", "mature 전환에도 own FFB가 늘지 않으면 반증.", "2012부터 생산기반이 확대되고 2022 age chart에도 young/immature runway가 남았다.", "연도별 cohort attribution은 제한.", "면적증가와 yield/ha를 분리하지 않았다.", "age-cohort별 ha와 yield를 연결한다."),
        C("low-cost palm oil economics", "대체로 성공", "palm oil의 ha당 oil yield와 estate 위치가 낮은 원가를 만든다.", "낮은 cash cost가 CPO downturn에서도 양의 margin을 남긴다.", "원문 $750~1,250/t sensitivity.", "fertilizer·labour·FX·levy가 cost advantage를 없애지 않는다.", "낮은 CPO에서 operating cash가 반복 적자면 반증.", "2012 가격하락에도 생산·net cash를 유지했고 2024 높은 profit을 냈다.", "cycle별 unit cost series는 미완전.", "industry yield advantage를 company cost curve로 동일시했다.", "cash cost/t와 yield/ha를 공시로 검증한다."),
        C("20%+ planted-asset ROIC", "방향 성공·정밀 제한", "개발원가 대비 성숙 earnings가 높은 ROIC를 만든다.", "저가 개발capex가 mature EBITDA/NAV로 전환된다.", "원문 development cost와 mature value 비교.", "유지·재식재·인프라 capex가 완전히 포함된다.", "full-cycle after-tax ROIC가 자본비용 이하이면 반증.", "장기 profit·net cash 축적은 높은 경제성을 지지한다.", "cohort별 invested capital 부재로 20% exact test 불가.", "spot margin을 full-cycle ROIC로 확장했다.", "개발·유지·replanting capex를 cohort basis로 합산한다."),
        C("내부재투자 runway", "성공", "현금흐름을 신규식재·mill에 재투자해 per-share NAV를 키운다.", "net cash와 저부채가 commodity cycle을 견디며 개발을 self-fund한다.", "큰 undeveloped/immature base.", "capital allocation과 land access가 건전하다.", "순현금 감소와 저수익 개발이 반복되면 반증.", "2024까지 생산자산·순현금·순자산이 증가했다.", "주당가치와 share count bridge는 추가 검증 필요.", "회사 규모 증가를 자동으로 per-share compounding으로 봤다.", "재투자는 incremental ROIC와 주당 NAV로 판정한다."),
        C("SQL 가격성과로 Long 성공 판정", "무효", "database price row가 아이디어 성과를 보여준다는 암묵 가정.", "ticker-date price를 entry와 비교한다.", "SQL AEP price $27대.", "ticker가 같은 법인·거래소·통화다.", "회사·거래소가 다르면 즉시 폐기.", "row는 NYSE American Electric Power로 판명됐다.", "전체 horizon return 무효.", "ticker 문자열만으로 entity를 매칭했다.", "ISIN·exchange·currency·company name을 먼저 맞춘다."),
    ],
    metrics=[("Planted value", "$4.2k~5.2k/ha", "replacement 이하", "2024 NAV 축적", "성공 방향"), ("2012 FFB", "783.4k mt", "maturation growth", "+11%", "성공"), ("2012 CPO", "260.5k mt", "증가", "+5%", "성공"), ("Net cash", "$91.2m", "유지·증가", "2024 $181.9m", "강한 성공"), ("SQL return", "AEP $27대", "LSE 성과", "NYSE 타사", "폐기")],
    timeline=[("2012-06-11", "VIC Long 게시", "low EV/ha·maturation"), ("2012-12-31", "FFB +11%·CPO +5%", "첫 운영 확인"), ("2012-12-31", "net cash $91.2m", "downside buffer"), ("2022-12-31", "age-profile chart", "young/immature runway 확인"), ("2024-12-31", "profit $67.5m·net cash $181.9m", "장기 compounding"), ("2025-11-24", "AEP Plantations로 사명 변경", "법인은 연속·ticker 유지"), ("2026-02-04", "공식 name-change notice", "entity mapping 갱신")],
)


add(
    id="e90f5ae6-b9c0-4b7c-9304-a2c2a950b498", date="2020-01-28",
    author="hack731", ticker="AEP.V", company="Atlas Engineered Products Ltd.",
    filename="analysis/ideas/2020/2020-01-28_AEP_atlas_engineered_products_long.md",
    source="https://www.valueinvestorsclub.com/idea/ATLAS_ENGINEERED_PRODCTS_LTD/9941570662",
    group="atlas", direction="Long", raw_direction="Long", security="TSX-V:AEP common equity / Long",
    entry="약 C$0.39", horizon="2022 operating target", raw_horizon="2022 C$100m sales·15% EBITDA·C$1.00 target",
    title="regional building-components roll-up Long",
    verdict="지연 성공 — C$1 target는 달성, 2022 C$100m revenue는 38% 미달",
    score=7.6, process=9.5,
    conclusion=(
        "지역 운송·설계 moat와 succession-driven roll-up은 살아남았고 주가는 2023~24 C$1을 넘어 2024 약 C$1.57까지 "
        "관찰됐다. 그러나 2022 revenue C$61.90m은 C$100m 목표보다 C$38.10m/-38.1% 미달했다. 좋은 unit economics와 "
        "M&A runway를 맞혔지만 acquisition cadence를 확정변수로 둔 timing error다."
    ),
    t0=(
        "원문은 2019 run-rate sales C$33~35m에서 지역 truss 회사를 2~3개 인수하고 organic growth를 더해 2022 C$100m sales, "
        "30% gross margin, 15% EBITDA margin을 제시했다. 6.5x EV/EBITDA로 C$1.00/share, 당시 C$0.39 대비 약 2.6배를 기대했다."
    ),
    reverse="시장은 작은 issuer의 key-person·financing·integration risk와 Canadian housing cycle, lumber pass-through 때문에 3년 내 규모 3배를 할인했다. M&A pipeline은 계약된 revenue가 아니었다.",
    valuation="2022E C$15m EBITDA × 6.5배에서 net debt·dilution을 차감해 C$1을 산출했다. 실제 2022 adjusted EBITDA C$15.73m은 근접했지만 revenue mix·cycle peak와 이후 margin reset이 multiple durability를 약화했다.",
    actual="2022 revenue C$61.90m, operating income C$12.53m, adjusted EBITDA C$15.73m이었다. 2023 금리·lumber normalization으로 revenue C$49.41m, normalized EBITDA C$9.93m으로 후퇴했다. LCF 인수 뒤 2024 revenue C$55.83m, normalized EBITDA C$8.52m이었다.",
    price="공식 daily total-return ledger는 만들지 않았다. 독립 월간 cross-check에서 2023~24 C$1을 통과하고 2024 약 C$1.57을 관찰했다. target hit은 확인하되 정확한 IRR·배당조정 수익률은 주장하지 않는다.",
    drivers="장기 수익은 지역 franchise, 낮은 entry valuation과 추가 인수 optionality가 만들었다. 미달은 acquisition availability·financing·integration·housing cycle가 3년 안에 동시에 맞지 않은 데서 나왔다.",
    counterfactual="인수를 한 건도 못 하고 housing starts가 20% 감소해도 기존 공장 FCF만으로 C$0.39의 downside와 debt service가 가능한가?",
    error="M&A pipeline과 record plant margin을 2022 forecast에 높은 확률로 넣고, acquisition financing·dilution과 cycle stress를 충분히 확률가중하지 않았다.",
    warning="2022 revenue가 C$61.90m으로 C$100m target에 38.1% 미달한 시점에 operating target가 깨졌고, 2023 margin reset이 normalization 문제를 확인했다.",
    first_signal_date="2022-12-31",
    scenarios=[("Bear", "M&A 중단·housing slowdown", "C$0.3~0.5", "2023 earnings reset"), ("Base", "C$100m·15% margin", "C$1.00", "price만 지연 달성"), ("Bull", "빠른 national roll-up", "C$1+ 조기", "cadence 미달")],
    lessons=["roll-up pipeline은 signed deal과 funded capacity만 forecast에 넣는다.", "regional moat와 national synergy를 별도 claim으로 검증한다.", "목표가격 달성과 operating forecast 달성을 분리한다."],
    checklist=["organic volume vs price", "deal pipeline stage", "purchase multiple", "post-deal margin", "net debt", "share dilution", "housing starts", "주당 normalized EBITDA"],
    scorecard=[("Industry thesis", "성공"), ("Valuation thesis", "지연 성공"), ("Catalyst thesis", "M&A cadence 미달"), ("Timing / path", "크게 지연"), ("Security selection", "common 적절")],
    claims=[
        C("지역 운송·permit moat", "성공", "truss는 bulky하고 설계·permit이 지역별이라 local density가 방어력이다.", "짧은 운송반경과 고객관계가 가격·납기를 지킨다.", "Nanaimo model plant와 지역 operators.", "지역 수요·경쟁이 gross margin을 지지한다.", "organic gross margin이 peer 수준 아래로 떨어지면 반증.", "여러 지역 company가 존속하고 group gross margin은 2022 32%를 기록했다.", "2024 gross margin 24%로 cycle sensitivity 확인.", "구조적 moat와 cycle margin을 혼용했다.", "moat는 multi-cycle gross margin과 share로 검증한다."),
        C("fragmented succession M&A runway", "성공 방향", "고령 owner가 많은 산업에서 싸게 회사를 연속 인수한다.", "seller succession과 shared systems가 acquisition supply·synergy를 만든다.", "수백개 target과 C$3~15m revenue 범위.", "valuation·financing·integration capacity가 유지된다.", "signed deals와 per-share EBITDA가 늘지 않으면 반증.", "2022 Hi-Tec, 2023 LCF 등 인수가 이어졌다.", "2022까지 C$100m scale에는 못 미침.", "opportunity set을 executable cadence로 봤다.", "pipeline을 LOI·financed·closed·integrated로 나눈다."),
        C("2022 revenue C$100m", "실패", "run-rate C$33~35m을 3년 내 약 3배로 키운다.", "2~3개 인수와 organic growth가 합쳐진다.", "원문 2022 model.", "deals가 제때 종결되고 housing demand가 유지된다.", "2022 revenue가 C$80m 아래면 반증.", "2022 revenue C$61.90m.", "-C$38.10m/-38.1%.", "M&A timing과 organic growth를 단일 point forecast로 묶었다.", "roll-up base case에는 확정 deal만 넣는다."),
        C("15% EBITDA margin", "부분 성공", "scale·procurement·IT로 15% EBITDA margin을 달성한다.", "local gross margin에 shared overhead leverage가 붙는다.", "원문 30% gross/15% EBITDA.", "lumber·labour·integration cost가 통제된다.", "normalized EBITDA margin이 반복 12% 이하이면 반증.", "2022 adjusted margin 25%였으나 2023 20%, 2024 15%로 내려왔다.", "peak를 넘었지만 지속성은 혼합.", "한 해 peak margin을 mature margin으로 읽을 위험.", "3년 평균 normalized margin을 쓴다."),
        C("C$1 target @ 6.5x", "지연 성공", "2022 C$15m EBITDA를 6.5배 평가해 C$1을 만든다.", "earnings scale-up과 multiple이 주당가치를 높인다.", "C$0.39 entry·C$1 target.", "share dilution·net debt가 제한되고 2022 실행된다.", "2022까지 C$1 미도달 또는 FDSO 급증이면 timing 실패.", "C$1은 2023~24에 지연 통과했다.", "약 1~2년 지연.", "target price와 target date를 분리하지 않았다.", "IRR에는 달성날짜가 필수다."),
        C("leverage·dilution manageable", "부분 성공", "cash flow와 financing이 roll-up을 무리 없이 지탱한다.", "적정 debt/equity mix가 distress 없이 규모를 키운다.", "T0 작은 balance sheet와 acquisition model.", "downcycle에도 covenant와 per-share value가 유지된다.", "net debt spike 또는 저가 증자면 반증.", "distress는 없었지만 2024 C$14.56m equity raise와 share count 증가가 있었다.", "survival 성공·per-share dilution 존재.", "enterprise growth를 per-share growth로 자동 전환했다.", "모든 deal을 fully diluted per-share로 재계산한다."),
    ],
    metrics=[("2022 revenue", "C$100m target", "C$100m", "C$61.90m", "-38.1%"), ("2022 adjusted EBITDA", "C$15m", "15% margin", "C$15.73m/25%", "수치 성공·mix 다름"), ("2023 revenue", "성장 지속", "C$100m path", "C$49.41m", "cycle reset"), ("2024 normalized EBITDA", "mature 15%+", "확대", "C$8.52m/15%", "부분"), ("Price target", "C$0.39→C$1", "2022", "2023~24 통과", "지연 성공")],
    timeline=[("2020-01-28", "VIC Long 게시", "C$100m/C$1 thesis"), ("2021-12-31", "revenue C$55.00m", "scale-up"), ("2022-02-28", "Hi-Tec 인수", "C$5.8m shares+C$3.25m real estate"), ("2022-12-31", "revenue C$61.90m", "C$100m target 실패"), ("2023-08-23", "LCF 인수", "동부 확장·debt/equity financing"), ("2023-12-31", "revenue C$49.41m", "금리·lumber reset"), ("2024", "주가 C$1.50대 관찰", "target 지연 달성"), ("2024-06-26", "C$14.56m equity raise", "automation·M&A·dilution"), ("2024-12-31", "normalized EBITDA C$8.52m", "mature denominator 재평가")],
)


add(
    id="8848c971-f78b-468d-8108-7cbeebdb5c31", date="2022-05-30",
    author="Stelio", ticker="AEP.V", company="Atlas Engineered Products Ltd.",
    filename="analysis/ideas/2022/2022-05-30_AEP_atlas_engineered_products_long.md",
    source="https://www.valueinvestorsclub.com/idea/ATLAS_ENGINEERED_PRODCTS_LTD/5737776840",
    group="atlas", direction="Long", raw_direction="Short", security="TSX-V:AEP common equity / Long",
    entry="약 C$0.53", horizon="12~24개월", raw_horizon="2022E EBIT C$17m·C$1.50 target @ 6x EV/EBIT",
    title="low-multiple peak-quarter building-products Long",
    verdict="지연 성공 — C$1.50 price hit, C$17m EBIT annualization은 실패",
    score=8.1, process=9.5,
    conclusion=(
        "C$0.53에서 2.4x EV/EBITDA·3.1x EV/EBIT은 싸고 balance sheet·M&A optionality도 유효했다. 그러나 1Q22를 "
        "연환산한 C$17m EBIT 대비 실제 2022 operating income은 C$12.53m(-26.3%)였고 2023 C$5.26m으로 급감했다. "
        "주가는 2024 C$1.50대를 기록해 target는 지연 달성했지만 denominator thesis는 틀렸다."
    ),
    t0=(
        "원문은 1Q22 revenue C$12.43m·EBIT 약 C$2.3m, LTM normalized EBITDA 약 C$15m·EBIT 약 C$12m, net debt 약 "
        "C$3m을 바탕으로 매우 낮은 multiple을 제시했다. Hi-Tec과 recession M&A optionality, 2022E EBIT C$17m·net debt 0·" 
        "FDSO 67m에 6x를 적용해 C$1.50을 계산했다."
    ),
    reverse="시장은 record quarter의 lumber pricing·housing demand가 정상화되고, 작은 roll-up의 overhead·share dilution·integration이 낮은 headline multiple을 상쇄할 가능성을 반영했다.",
    valuation="원문 C$17m EBIT × 6배 - net debt 0을 67m FDSO로 나누면 약 C$1.52다. 실제 2022 operating income C$12.53m을 같은 방식으로 쓰면 약 C$1.12이고, 2023 C$5.26m이면 약 C$0.47 before net debt다. denominator가 valuation의 대부분이었다.",
    actual="2022 revenue C$61.90m, operating income C$12.53m, adjusted EBITDA C$15.73m이었다. 2023 revenue C$49.41m, operating income C$5.26m, normalized EBITDA C$9.93m으로 후퇴했다. 2024 revenue는 C$55.83m으로 회복했지만 normalized EBITDA C$8.52m이었다.",
    price="독립 월간 cross-check에서 2024 C$1.50~1.57을 관찰해 target hit만 인정한다. exact entry execution·corporate action·total-return series가 없어 정확한 IRR은 만들지 않는다.",
    drivers="very low entry multiple과 balance-sheet survival, 추가 LCF 인수와 platform optionality가 rerating을 만들었다. 반면 lumber pass-through와 housing strength를 structural EBIT으로 annualize한 것이 forecast miss를 만들었다.",
    counterfactual="2022 gross margin이 32%가 아니라 2024의 24%, normalized EBITDA가 C$8.5m이면 C$0.53에서 진짜 EV/EBITDA와 downside는 얼마인가?",
    error="좋은 분기 ×4를 정상 earnings로 쓰고 price target의 성공을 operating forecast 성공과 혼동할 위험이 있었다.",
    warning="2022 operating income C$12.53m이 C$17m을 26.3% 미달했고 2023 gross margin 27%·operating income C$5.26m이 peak denominator를 확정 반증했다.",
    first_signal_date="2022-12-31",
    scenarios=[("Bear", "housing slowdown·24% GM", "C$0.5 안팎", "2023~24 earnings"), ("Base", "2022 EBIT C$17m·6x", "C$1.50", "price만 지연 실현"), ("Bull", "recession M&A+margin 유지", "C$2+", "denominator 미달")],
    lessons=["낮은 multiple을 보기 전에 denominator가 peak-quarter annualization인지 본다.", "lumber pass-through로 움직인 revenue와 organic volume을 분리한다.", "가격목표 적중이 earnings model의 정확성을 증명하지 않는다."],
    checklist=["quarter seasonality", "gross margin normalization", "lumber price vs volume", "housing starts", "net debt", "FDSO", "deal funding", "3년 평균 EBITDA"],
    scorecard=[("Business thesis", "성공"), ("Valuation thesis", "성공"), ("Earnings thesis", "실패"), ("Timing / path", "약 2년 지연"), ("Security selection", "common 적절")],
    claims=[
        C("2022 banner year", "성공", "Hi-Tec·pricing·backlog로 2022가 record year다.", "volume·price·M&A가 매출·이익을 높인다.", "1Q22 revenue C$12.43m·EBIT 약 C$2.3m.", "분기 strength가 연간 지속된다.", "후속분기 매출·margin 급락이면 반증.", "2022 revenue C$61.90m·operating income C$12.53m으로 record.", "방향 성공.", "record year와 normalized year를 혼용했다.", "peak 여부는 다음 cycle trough와 평균으로 판정한다."),
        C("2022 EBIT C$17m", "실패", "1Q run-rate와 backlog로 EBIT C$17m을 번다.", "record quarter를 연환산한다.", "원문 model.", "seasonality·lumber·housing이 유지된다.", "FY EBIT가 C$14m 아래면 반증.", "FY operating income C$12.53m.", "-C$4.47m/-26.3%.", "한 분기 annualization.", "quarter ×4 대신 trailing·mid-cycle margin을 쓴다."),
        C("3x EBIT valuation", "부분 성공", "LTM EBIT C$12m에 3.1x EV/EBIT은 과도하게 싸다.", "unchanged EBIT에 normal 6x가 적용된다.", "C$0.53·net debt C$3m.", "EBIT denominator가 지속된다.", "다음해 EBIT 반감이면 low multiple 착시.", "2023 operating income C$5.26m으로 감소했지만 주가는 rerate했다.", "2023 기준 multiple은 약 2배 이상 상승.", "denominator risk를 haircut하지 않았다.", "trough·base·peak EBIT 각각에 multiple을 붙인다."),
        C("balance sheet가 recession을 방어", "성공 방향", "낮은 net debt와 현금창출이 downturn survival·M&A를 가능하게 한다.", "covenant headroom과 funding access가 duration을 준다.", "T0 net debt 약 C$3m.", "인수 후 leverage와 working capital이 통제된다.", "distress financing·covenant breach면 반증.", "distress 없이 LCF를 인수하고 equity raise로 자동화 투자.", "survival 성공·희석 비용 존재.", "funding cost를 upside model에 덜 반영했다.", "downside는 debt뿐 아니라 dilution도 본다."),
        C("recession이 M&A 기회", "성공 방향", "housing 약세가 succession sellers를 늘려 accretive deals를 만든다.", "현금·신용으로 약한 competitor를 산다.", "roll-up playbook과 pipeline.", "asset quality·price·financing이 유리하다.", "deal이 없거나 per-share EBITDA가 줄면 반증.", "2023 LCF를 인수했지만 debt·shares도 늘었다.", "enterprise scale 증가·per-share 효과 혼합.", "M&A availability를 accretion과 동일시했다.", "deal별 purchase EV/normalized EBITDA와 FDSO를 기록한다."),
        C("C$1.50 @ 6x EV/EBIT", "지연 성공", "C$17m EBIT·net debt 0·67m shares면 C$1.50다.", "earnings 유지와 multiple rerating.", "원문 valuation bridge.", "2022 earnings와 12~24개월 rerating이 모두 맞는다.", "2024 이전 target 미달이면 timing 실패.", "2024 C$1.50~1.57 관찰.", "약 2년 지연·earnings bridge 불일치.", "terminal target hit으로 original path를 정당화했다.", "target은 earnings·debt·multiple 기여로 attribution한다."),
    ],
    metrics=[("2022 EBIT", "C$17m", "C$17m", "C$12.53m", "-26.3%"), ("2022 adjusted EBITDA", "LTM ~C$15m", "유지", "C$15.73m", "성공"), ("2023 operating income", "정상화 유지", "C$17m path", "C$5.26m", "peak 반증"), ("2024 normalized EBITDA", "성장", "C$15m+", "C$8.52m", "미달"), ("Price target", "C$0.53→C$1.50", "12~24개월", "2024 hit", "지연 성공")],
    timeline=[("2022-05-30", "VIC Long 게시", "3x EBIT·C$1.50"), ("2022-12-31", "revenue C$61.90m", "banner year"), ("2022-12-31", "operating income C$12.53m", "C$17m miss"), ("2023-08-23", "LCF 인수", "M&A option 실행"), ("2023-12-31", "operating income C$5.26m", "peak denominator 반증"), ("2024", "주가 C$1.50대", "target 지연 hit"), ("2024-06-26", "C$14.56m equity raise", "growth capital·dilution"), ("2024-12-31", "normalized EBITDA C$8.52m", "mid-cycle reset")],
)


add(
    id="093b48e1-bf63-4b76-ac21-fc48536d34ad", date="2008-03-20",
    author="andreas947", ticker="AEPI", company="AEP Industries Inc.",
    filename="analysis/ideas/2008/2008-03-20_AEPI_long.md", source="", group="aepi",
    direction="Long", raw_direction="Long", security="AEPI common equity / Long",
    entry="약 $30", horizon="12개월", raw_horizon="well into the $50s within 12 months",
    title="cheap flexible-film spread·buyback Long",
    verdict="장기 강한 성공 — 12개월 timing 혼합, 2017 $110 strategic value 검증",
    score=8.4, process=9.5,
    conclusion=(
        "약 4.9x adjusted EBITDA·6x FCF·7x adjusted EPS와 18개월간 22% share repurchase는 저평가를 잘 포착했다. "
        "그러나 GFC로 housing·industrial volume이 훼손돼 12개월 $50s path는 안전하지 않았다. 반대로 balance sheet와 "
        "distressed Atlantis 인수가 장기 earning power를 키워 2017 주당 $110 상당 거래로 terminal value가 검증됐다."
    ),
    t0=(
        "원문은 LTM adjusted EBITDA 약 $86m, FCF 약 $5/share, adjusted EPS $4+와 food-heavy 수요를 근거로 $30을 싸다고 "
        "봤다. 회사는 18개월 동안 1.98m주, 약 22%를 평균 $43에 매입했다. 핵심은 resin 상승을 지연 후 pass-through하고 "
        "share count 감소가 per-share FCF를 증폭한다는 것이었다."
    ),
    reverse=(
        "시장은 food mix만으로 상쇄되지 않는 housing·industrial volume risk, resin pass-through lag, working-capital 소요와 "
        "cycle-top buyback을 할인했다. $30이 싸려면 recession 중 EBITDA와 liquidity가 acquisition debt까지 감당해야 했다."
    ),
    valuation=(
        "원문 headline 4.9x EBITDA·6x FCF는 normalized spread와 LTM volume이 유지된다는 전제다. 더 나은 방법은 pounds를 "
        "end-market별 stress하고 spread/lb·working capital·net debt를 연결해 FCF를 계산하는 것이다. 2017 $110은 장기 strategic "
        "value anchor지만 2009 $50s target의 시간 정확성을 증명하지 않는다."
    ),
    actual=(
        "2008~09 recession은 housing-related film 수요를 훼손했지만 AEPI는 Atlantis Plastics 자산을 bankruptcy에서 인수해 "
        "scale과 capacity를 늘렸다. 이후 Webster·Transco 등 tuck-in과 buyback을 지속했다. Berry는 2016 merger agreement 뒤 "
        "2017-01-20 AEPI를 인수했다. 주주는 $110 cash 또는 2.5011 BERY shares를 선택하되 전체 50/50 proration을 적용받았다."
    ),
    price=(
        "완전한 daily total-return series와 선택·proration별 merger ledger가 없어 12개월 target hit·정확한 IRR은 만들지 않는다. "
        "확정 가능한 terminal event는 2017의 $110 cash/2.5011 BERY consideration이다. 이는 $30 대비 장기 value를 검증하지만 "
        "9년 holding-period return과 12개월 예측은 별개다."
    ),
    drivers="장기 수익은 food defensiveness 자체보다 downturn liquidity, distressed Atlantis acquisition, capacity rationalization, 반복 buyback과 strategic consolidation이 만들었다.",
    counterfactual="housing volume -30%, resin +20%, pass-through 두 분기 지연에서도 covenant·working capital과 acquisition debt를 버틸 수 있었는가?",
    error="recession resistance를 end-market mix로 과도하게 단순화하고 12개월 target에 macro·resin·volume correlation을 충분히 넣지 않았다.",
    warning="2008~09 housing/industrial volume 급락이 12개월 timing을 반증했지만 liquidity와 M&A capacity는 장기 thesis를 살렸다.",
    first_signal_date="2008-10-31",
    scenarios=[("Bear", "GFC·volume 급락·spread lag", "$20대·debt stress", "near-term 현실화"), ("Base", "food 방어·spread 회복", "$50s in 12m", "timing 미확정/지연"), ("Long bull", "distressed M&A·consolidation", "$100+ strategic", "2017 $110")],
    lessons=["방어적 end market과 방어적 total volume은 같은 말이 아니다.", "spread business는 매출보다 pounds×spread/lb와 working capital을 본다.", "장기 takeout은 terminal value를 검증해도 원래 horizon을 구제하지 않는다."],
    checklist=["end-market lbs", "resin index·pass-through lag", "spread/lb", "working capital", "net debt/covenant", "repurchase price·share count", "M&A adjusted purchase price"],
    scorecard=[("Business thesis", "장기 성공"), ("Valuation thesis", "강한 성공"), ("Catalyst thesis", "buyback·M&A 성공"), ("Timing / path", "12개월 혼합"), ("External value", "2017 $110")],
    claims=[
        C("food mix가 recession을 방어", "부분 실패", "food·beverage 고객이 경기하락에서도 volume을 지킨다.", "필수소비 포장이 housing·industrial 약세를 상쇄한다.", "원문 end-market mix.", "비food volume과 operating leverage가 작다.", "housing·industrial 감소로 total lbs·EBITDA가 크게 줄면 반증.", "GFC에서 housing-related film demand가 약해졌다.", "완전 방어가 아니라 mix 완충.", "고객 mix를 consolidated volume beta로 동일시했다.", "end-market별 lbs와 contribution을 stress한다."),
        C("resin 상승은 결국 pass-through", "성공 방향", "resin 원가상승은 시차 후 selling price에 반영된다.", "계약·시장 pricing이 unit spread를 회복시킨다.", "resin이 cost of sales의 큰 비중.", "고객 가격저항과 경쟁이 제한적이다.", "2~3분기 뒤에도 spread/lb가 회복되지 않으면 반증.", "회사는 반복 resin cycle을 생존하고 장기 strategic value를 만들었다.", "분기별 exact lag 검증 제한.", "eventual pass-through와 interim liquidity를 분리하지 않았다.", "lag 중 working-capital·covenant를 함께 본다."),
        C("$30의 4.9x EBITDA·6x FCF", "장기 성공", "normalized earnings 대비 과도한 할인이다.", "cycle mean cash flow에 보수적 multiple을 적용한다.", "LTM EBITDA ~$86m·FCF ~$5/share.", "LTM denominator가 정상 이하 또는 지속 가능하다.", "stress EBITDA에서 debt-adjusted value가 $30 아래면 반증.", "2017 $110 consideration이 장기 value를 외부검증했다.", "+$80/share terminal gap, horizon 9년.", "terminal price를 near-term multiple과 비교했다.", "valuation에는 explicit duration과 cycle earnings band가 필요하다."),
        C("22% buyback이 주당가치를 키움", "성공", "평균 $43에 대규모 repurchase는 intrinsic value signal이다.", "낮은 가격에서 share count를 줄여 normalized EPS를 집중한다.", "18개월 1.98m주/약 22%.", "buyback 뒤 liquidity와 debt capacity가 충분하다.", "고가매입 후 distress equity raise면 반증.", "장기 share count 감소와 strategic value가 확인됐다.", "일부 매입가는 당시 $30보다 높음.", "management signal과 경제적 accretion을 혼용했다.", "repurchase IRR은 가격·debt·후속 dilution으로 계산한다."),
        C("capital allocation이 downturn을 기회로 전환", "강한 성공", "건전한 balance sheet로 distressed competitor를 산다.", "recession asset price가 normalized EBITDA 대비 낮아진다.", "T0 liquidity와 industry fragmentation.", "deal price·integration·debt가 보수적이다.", "인수 후 leverage 상승과 synergy miss면 반증.", "Atlantis를 bankruptcy에서 인수하고 후속 tuck-in을 실행했다.", "장기 thesis의 핵심 positive surprise.", "T0 논지에서 M&A upside를 충분히 구조화하지 않았다.", "downturn optionality는 liquidity와 target list로 사전 측정한다."),
        C("$50s within 12 months", "미검증·likely delayed", "$30에서 1년 내 $50대.", "spread 회복과 low multiple rerating.", "원문 explicit target.", "GFC가 earnings를 훼손하지 않는다.", "1년 내 earnings·price 미달이면 실패.", "daily series 미복원, GFC path는 timing risk를 강하게 시사.", "exact return 미확정.", "장기 deal price로 단기 target를 소급할 수 없다.", "horizon별 price ledger가 없으면 보수적으로 미검증 처리한다."),
    ],
    metrics=[("Entry / target", "$30 / $50s", "12개월", "exact series 미복원", "미검증"), ("LTM adjusted EBITDA", "~$86m", "정상 유지", "GFC 변동", "혼합"), ("FCF/share", "~$5", "6x FCF", "cycle stress", "혼합"), ("Buyback", "1.98m/22%", "per-share accretion", "장기 share count 감소", "성공"), ("Merger value", "미가정", "terminal upside", "$110 cash/2.5011 BERY", "강한 성공")],
    timeline=[("2008-03-20", "VIC Long 게시", "$30→$50s"), ("2008", "Atlantis bankruptcy assets 인수", "downturn M&A"), ("2008-10-31", "GFC·housing volume stress", "12개월 timing 반증"), ("2011", "Webster acquisition", "capacity·mix 확대"), ("2014", "Transco-related assets 확대", "tuck-in continuation"), ("2016-08-25", "Berry merger agreement", "strategic value crystallization"), ("2016-12-15", "merger proxy", "consideration·proration 확정"), ("2017-01-20", "merger close", "$110/2.5011 BERY")],
)


add(
    id="08940e6b-903e-4abe-b876-fabf39b332e2", date="2009-10-12",
    author="gearl1818", ticker="AEPI", company="AEP Industries Inc.",
    filename="analysis/ideas/2009/2009-10-12_AEPI_long.md",
    source="https://www.valueinvestorsclub.com/idea/AEP_Industries/7126640073", group="aepi",
    direction="Long", raw_direction="Long", security="AEPI common equity / Long",
    entry="$37.23", horizon="1~2년", raw_horizon="$74~82 in 1Y / $92~99 in 2Y",
    title="distressed Atlantis M&A·normalized EBITDA Long",
    verdict="장기 성공 — Atlantis economics 적중, 1~2년 target timing 과도",
    score=8.6, process=9.6,
    conclusion=(
        "Atlantis의 headline $99m보다 cash·working capital을 조정한 약 $46m 경제적 purchase price와 $20m+ pre-crisis "
        "EBITDA·$20m synergy를 본 것이 핵심 edge였다. integration·deleveraging은 장기 가치로 이어졌지만 $74~99의 1~2년 "
        "target은 cycle·multiple timing을 과소평가했다. 2017 $110 deal은 terminal value를 확인했다."
    ),
    t0=(
        "원문은 $37.23에서 5.6x FY09E EBITDA, 3.5x FY10E EBITDA, 7.8x FY09E FCF, 4.5x FY10E FCF를 제시했다. "
        "Atlantis는 leveraged recap과 recession으로 Chapter 11에 들어갔고, AEPI는 working capital·cash를 고려하면 약 $46m에 "
        "정상 EBITDA $20m+와 synergy $20m을 샀다고 봤다. combined normalized EBITDA는 ≥$125m이었다."
    ),
    reverse="시장은 Atlantis의 과거 EBITDA가 회복되지 않고 rationalization cost·resin·housing weakness·acquisition debt가 equity rerating을 늦출 위험을 반영했다.",
    valuation="$125m normalized EBITDA에 6~7배를 적용하고 net debt를 빼면 큰 upside가 나온다. 그러나 FY10E 3.5x는 synergy와 volume recovery를 이미 denominator에 넣은 forward multiple이다. 이를 probability-weighted integration cases로 나눠야 했다.",
    actual="AEPI는 Atlantis facilities와 customer base를 통합하고 acquisition debt를 낮췄다. 이후 Webster·Transco 등으로 규모를 키웠으며 industry consolidation이 진행됐다. Berry는 약 $765m transaction value로 인수해 2017-01-20 close했다.",
    price="1년·2년 exact daily series는 복원하지 않아 $74~99 target 달성을 주장하지 않는다. 2017 $110 consideration은 7년여 뒤 terminal value를 검증한다. cash/stock election과 aggregate proration 때문에 각 주주의 exact realized return은 election ledger가 필요하다.",
    drivers="distressed purchase price, plant rationalization, resin/volume normalization, debt paydown과 industry consolidation이 value를 만들었다. near-term miss risk는 synergy timing과 valuation rerating duration이었다.",
    counterfactual="Atlantis EBITDA가 절반만 회복되고 $20m synergy에 2년 걸려도 acquisition debt와 equity value가 안전했는가?",
    error="좋은 distressed M&A underwriting을 했지만 normalized EBITDA가 시장가격에 반영되는 속도를 1~2년으로 너무 짧게 잡았다.",
    warning="Atlantis 통합·housing recovery가 직선적이지 않은 후속 실적은 price target calendar를 늦췄지만 deal economics 자체를 깨지는 않았다.",
    first_signal_date="2010-10-31",
    scenarios=[("Bear", "Atlantis EBITDA 미회복·debt 부담", "$30대 이하", "완전 붕괴는 없음"), ("Base", "$125m EBITDA·deleveraging", "$74~82 1Y", "timing 과도"), ("Bull", "synergy+consolidation", "$92~99 2Y", "2017 $110 장기")],
    lessons=["distressed acquisition은 headline price가 아니라 cash·WC·assumed debt를 조정한 enterprise price로 본다.", "normalized EBITDA가 맞아도 integration date와 rerating date는 별도다.", "takeout은 terminal value만 검증하고 original IRR calendar는 따로 판정한다."],
    checklist=["purchase-price bridge", "assumed liabilities", "standalone EBITDA", "synergy owner·deadline", "integration cash cost", "net debt reduction", "per-share FCF", "target calendar"],
    scorecard=[("M&A thesis", "강한 성공"), ("Valuation thesis", "장기 성공"), ("Catalyst thesis", "integration·deleveraging 성공"), ("Timing / path", "1~2년 과도"), ("External value", "2017 $110")],
    claims=[
        C("Atlantis를 약 $46m economic price에 인수", "강한 성공", "headline $99m보다 cash·WC 조정 실질가격이 훨씬 낮다.", "acquired current assets와 cash를 차감해 operating assets의 가격을 본다.", "원문 purchase bridge.", "acquired WC가 회수 가능하고 hidden liabilities가 없다.", "post-close cash leakage·impairment가 bridge를 무효화하면 반증.", "Atlantis가 통합돼 장기 scale과 strategic value에 기여했다.", "정확한 realized deal IRR은 segment 분리 제한.", "모든 WC를 dollar-for-dollar 가치로 봤다.", "WC quality·liability·integration cash를 haircut한다."),
        C("$20m+ EBITDA와 $20m synergy", "성공 방향", "pre-crisis earnings와 plant rationalization이 큰 accretion을 만든다.", "volume 회복·중복비용 제거가 combined margin을 높인다.", "Atlantis pre-crisis EBITDA·synergy plan.", "customer retention·closure execution이 성공한다.", "2년 내 synergy·margin이 나타나지 않으면 timing 반증.", "후속 consolidation과 strategic value는 economics를 지지했다.", "standalone actual synergy 공개 제한.", "gross synergy와 cash integration cost를 분리하지 않았다.", "synergy는 owner·date·cash cost·base erosion과 함께 기록한다."),
        C("normalized EBITDA ≥$125m", "방향 성공·exact timing 제한", "combined company가 최소 $125m을 번다.", "capacity×normalized spread와 acquired earnings를 합친다.", "원문 normalized model.", "housing·resin spread·volume이 평균으로 회복한다.", "multi-year EBITDA가 크게 못 미치면 반증.", "2017 약 $765m transaction value는 sizable normalized earnings를 지지했다.", "연도별 $125m exact hit은 미확정.", "transaction EV로 EBITDA forecast를 역추론했다.", "forecast는 후속 10-K EBITDA로 직접 test한다."),
        C("acquisition debt rapidly manageable", "성공", "FCF로 debt를 빠르게 줄인다.", "synergy·working-capital release가 cash sweep을 만든다.", "2009-07 net debt 약 $176m.", "FCF conversion과 covenant headroom이 충분하다.", "net debt/EBITDA가 상승하거나 refinancing 필요시 반증.", "인수 후 debt가 낮아지고 후속 M&A capacity가 생겼다.", "정확한 분기 schedule보다 방향 확인.", "normalized EBITDA를 즉시 cash로 봤다.", "interest·capex·WC 뒤 cash sweep을 추적한다."),
        C("FY10E 3.5x EBITDA", "장기 성공·horizon 혼합", "forward normalized multiple이 매우 싸다.", "earnings recovery가 denominator와 rerating을 동시에 만든다.", "원문 3.5x FY10E.", "FY10 EBITDA가 model대로 실현된다.", "실제 EBITDA miss면 multiple 착시.", "terminal $110 deal은 low entry value를 검증했다.", "1~2년 target와 7년 terminal event 차이.", "forward denominator에 bull recovery를 넣었다.", "reported·run-rate·normalized EBITDA를 세 줄로 유지한다."),
        C("$74~99 in 1~2 years", "과도·미검증", "1Y $74~82, 2Y $92~99.", "synergy·debt paydown·multiple rerating.", "원문 target table.", "integration과 cycle recovery가 빠르다.", "target calendar 미달이면 timing 실패.", "eventual $110은 2017에 실현됐다.", "5~6년 이상 지연 가능.", "terminal value와 duration을 혼동했다.", "target에 catalyst date와 quarterly milestones를 붙인다."),
    ],
    metrics=[("Entry", "$37.23", "rerating", "2017 $110 event", "장기 성공"), ("Economic purchase", "~$46m", "low deal multiple", "통합·존속", "성공"), ("Normalized EBITDA", "≥$125m", "회복", "exact timing 제한", "방향 성공"), ("Net debt", "~$176m Jul-2009", "빠른 감소", "후속 M&A 가능", "성공"), ("Targets", "$74~82/$92~99", "1Y/2Y", "$110 in 2017", "timing 실패")],
    timeline=[("2008", "Atlantis Chapter 11 assets 인수", "distressed entry"), ("2009-07", "net debt 약 $176m", "deleveraging base"), ("2009-10-12", "VIC Long 게시", "$37.23→$74~99"), ("2010-10-31", "integration still multi-year", "calendar risk"), ("2011", "Webster acquisition", "platform 확대"), ("2014", "추가 tuck-in", "industry consolidation"), ("2016-08-25", "Berry merger agreement", "terminal value"), ("2017-01-20", "merger close", "$110/2.5011 BERY")],
)


add(
    id="77ce1191-0176-49a0-baae-0b0c8d7b1af6", date="2011-07-12",
    author="finn520", ticker="AEPI", company="AEP Industries Inc.",
    filename="analysis/ideas/2011/2011-07-12_AEPI_long.md",
    source="https://www.valueinvestorsclub.com/idea/AEP_INDUSTRIES_INC/3661391494", group="aepi",
    direction="Long", raw_direction="Long", security="AEPI common equity / Long",
    entry="원문 가격대 기준", horizon="중기 normalization", raw_horizon="6x EBITDA로 >$50/share",
    title="normalized unit spread·share-count reduction Long",
    verdict="강한 성공 — unit margin·buyback·strategic exit가 주당가치 검증",
    score=9.1, process=9.6,
    conclusion=(
        "1998~2010 평균 EBIT/lb 약 $0.057 대비 2011 guide 약 $0.05/lb라는 unit-economics framing과, 2006 약 8.6m주에서 "
        "2011 block purchase 후 약 5.5m주로 줄어든 share count를 함께 본 점이 강했다. earnings path는 cyclic했지만 >$50 "
        "normalized value는 2017 $110 consideration으로 충분히 검증됐다."
    ),
    t0=(
        "원문은 840~850m lbs resin volume, adjusted EBITDA 약 $65m guide가 depressed spread를 반영한다고 봤다. historical "
        "EBIT/lb 정상화로 $80m+ EBITDA, 6x multiple이면 >$50/share가 가능했다. 회사는 2011 650k주, 약 11% block을 매입했고 "
        "2006 이후 share count를 약 36% 줄였다."
    ),
    reverse="시장은 13년 평균 spread가 새로운 경쟁·resin·mix 환경에서 재현되지 않고, reduced share count의 가치가 debt·acquisition capex에 상쇄될 위험을 반영했다.",
    valuation="`normalized lbs × normalized EBIT/lb × multiple - net debt`를 reduced share count로 나누는 접근이다. 6x EBITDA는 합리적이지만 historical unit margin이 유지된다는 가정과 share count·options·debt를 같은 날짜로 맞춰야 한다.",
    actual="AEPI는 Webster acquisition과 후속 assets로 capacity·mix를 확대했고 buyback·debt management를 이어갔다. resin lag와 demand cycle로 연도별 profit은 흔들렸지만 Berry가 2016 약 $765m deal을 합의하고 2017 close했다.",
    price="정확한 entry·daily series가 없어 interim IRR은 만들지 않는다. 확정 terminal consideration은 $110 cash 또는 2.5011 BERY shares, aggregate 50/50 proration이다. >$50 value claim은 강하게 검증되지만 catalyst duration은 다년이었다.",
    drivers="정상 unit spread의 회복 가능성, capacity·mix M&A, materially lower share count와 strategic consolidation이 주당가치를 만들었다.",
    counterfactual="historical EBIT/lb가 구조적으로 20% 낮아지고 volume이 850m lbs에서 정체돼도 reduced share count와 net debt 후 >$50가 나오는가?",
    error="historical average margin에 regime change haircut을 작게 두고, $80m EBITDA가 언제 실현되는지 명확한 catalyst calendar를 두지 않았다.",
    warning="resin·housing volatility가 normalization을 지연했지만, share count 감소와 balance sheet가 thesis의 장기 floor를 유지했다.",
    first_signal_date="2012-10-31",
    scenarios=[("Bear", "$0.04/lb·volume 정체", "$30~40", "cycle volatility"), ("Base", "$0.057/lb·$80m+ EBITDA", ">$50", "장기 검증"), ("Bull", "mix·consolidation", "$100+", "2017 $110")],
    lessons=["commodity-like manufacturer는 revenue보다 pounds×unit spread로 모델링한다.", "buyback은 투입금액이 아니라 fully diluted share-count 감소로 검증한다.", "historical margin 평균에는 경쟁·mix·capex regime haircut이 필요하다."],
    checklist=["lbs by end market", "EBIT/lb", "resin lag", "capacity utilization", "net debt", "fully diluted shares", "buyback price", "incremental M&A ROIC"],
    scorecard=[("Business normalization", "성공"), ("Valuation thesis", "강한 성공"), ("Capital allocation", "강한 성공"), ("Timing / path", "다년간"), ("External value", "2017 $110")],
    claims=[
        C("EBIT/lb가 역사평균으로 정상화", "성공 방향", "2011 약 $0.05/lb가 1998~2010 평균 $0.057로 돌아간다.", "resin pass-through·volume·utilization이 unit margin을 회복한다.", "13년 historical average.", "product mix·competition·conversion cost regime가 유사하다.", "3년 평균 EBIT/lb가 $0.05 아래면 반증.", "후속 earnings·strategic value는 정상화 가능성을 지지했다.", "연도별 exact series는 filing 재구축 필요.", "과거평균을 mean reversion anchor로 기계 적용했다.", "평균을 cycle·mix·capacity별로 재산정한다."),
        C("$80m+ adjusted EBITDA", "성공 방향", "840~850m lbs와 normalized spread면 $80m+를 번다.", "단위마진 증가가 거의 바로 EBITDA로 흐른다.", "2011 guide ~$65m vs normalized $80m+.", "fixed cost·capex·mix가 안정적이다.", "$80m에 반복 미달하고 debt가 늘면 반증.", "더 큰 strategic EV와 후속 operating base가 thesis를 지지했다.", "exact hit date 제한.", "unit EBIT와 adjusted EBITDA bridge가 단순했다.", "pounds×spread에서 SG&A·one-offs를 명시한다."),
        C("6x EBITDA면 >$50/share", "강한 성공", "보수적 6x가 reduced shares에 큰 upside를 준다.", "normalized EV에서 net debt를 차감하고 shares로 나눈다.", "원문 valuation.", "net debt·options와 shares가 정확하다.", "stress EBITDA에서 value가 $50 아래면 반증.", "2017 $110 consideration.", ">$60/share terminal upside.", "deal value를 same-horizon market value로 볼 수 없다.", "external bid는 value anchor, 날짜는 별도다."),
        C("share count 36% 감소가 accretive", "강한 성공", "2006 약 8.6m주가 약 5.5m주로 줄었다.", "같은 enterprise earnings가 더 적은 shares에 귀속된다.", "2011 650k/11% block repurchase.", "debt-funded buyback이 solvency를 훼손하지 않는다.", "후속 equity raise·debt distress면 반증.", "lower share base가 merger consideration의 per-share value를 확대했다.", "repurchase별 IRR은 미계산.", "share 감소만 보고 funding cost를 작게 봤다.", "enterprise FCF·net debt·FDSO를 동시에 비교한다."),
        C("housing recovery가 핵심 upside", "부분 성공", "housing-related volume 회복이 lbs와 utilization을 올린다.", "fixed conversion assets의 operating leverage.", "depressed housing mix.", "housing starts가 회복되고 share가 유지된다.", "recovery에도 company volume이 정체되면 반증.", "가치는 housing뿐 아니라 M&A·food mix·consolidation에서도 나왔다.", "driver attribution이 더 다변화.", "macro catalyst 비중을 과대평가했다.", "end-market별 volume bridge를 만든다."),
        C("management capital allocation", "강한 성공", "buyback과 tuck-in M&A를 저평가 자산에 배분한다.", "낮은 share/deal price가 per-share earnings를 높인다.", "block repurchase·Atlantis precedent.", "management가 cycle에 역행해 산다.", "고가 deal·고가 buyback이면 반증.", "Webster·후속 deals와 strategic exit로 장기 가치가 확인됐다.", "각 deal ROIC 공개 제한.", "outcome bias 위험.", "deal별 purchase multiple과 buyback yield를 사전에 기록한다."),
    ],
    metrics=[("Resin volume", "840~850m lbs", "normalized scale", "후속 규모 확대", "성공 방향"), ("EBIT/lb", "~$0.05", "$0.057 mean", "cycle 회복 방향", "부분"), ("Adjusted EBITDA", "~$65m", "$80m+", "exact timing 제한", "방향 성공"), ("Share count", "8.6m→5.5m", "per-share accretion", "감소 유지", "강한 성공"), ("Value", "> $50", "6x EBITDA", "$110 deal", "강한 성공")],
    timeline=[("2006", "share count 약 8.6m", "buyback baseline"), ("2011-06", "650k block repurchase", "약 11% 감소"), ("2011-07-12", "VIC Long 게시", "$80m+ EBITDA·>$50"), ("2011", "Webster acquisition", "capacity·mix"), ("2012-10-31", "cycle volatility 지속", "timing risk"), ("2014", "추가 tuck-in", "platform value"), ("2016-08-25", "Berry agreement", "strategic bid"), ("2017-01-20", "merger close", "$110/2.5011 BERY")],
)


add(
    id="65e8bbd1-44c8-4240-b490-4f00015b2375", date="2014-07-09",
    author="zzz007", ticker="AEPI", company="AEP Industries Inc.",
    filename="analysis/ideas/2014/2014-07-09_AEPI_long.md",
    source="https://www.valueinvestorsclub.com/idea/AEP_INDUSTRIES_INC/2844762662", group="aepi",
    direction="Long", raw_direction="Long", security="AEPI common equity / Long",
    entry="원문 당시 주가", horizon="3년", raw_horizon="normalized EPS $9.40 within three years",
    title="trough spread normalization·consolidation Long",
    verdict="강한 성공 — stand-alone EPS는 거래로 미검증, $110 strategic value는 검증",
    score=9.1, process=9.7,
    conclusion=(
        "1.2bn lbs capacity와 normalized spread에서 EBIT $100m·EBITDA $135m·EPS $9.40을 도출한 unit-economics frame은 "
        "trough earnings를 잘 포착했다. 3년 뒤 stand-alone EPS는 Berry 인수로 직접 관찰할 수 없지만 share repurchase·industry "
        "consolidation과 $110 consideration이 낮은 entry value를 강하게 검증했다."
    ),
    t0=(
        "원문은 depressed resin spread를 capacity 1.2bn lbs에 적용해 normalized EBIT $100m, EBITDA $135m, EPS $9.40을 "
        "제시했다. food·beverage mix와 scale, repurchase, consolidation을 catalyst로 봤으며 reported revenue보다 unit spread와 "
        "share count가 중요한 thesis였다."
    ),
    reverse="시장은 resin spread가 historical level로 돌아오지 않고 secular packaging mix·customer bargaining·capital intensity가 normalized model을 낮출 위험, 그리고 catalyst 없는 value trap을 반영했다.",
    valuation="`1.2bn lbs × normalized EBIT/lb = ~$100m EBIT`; depreciation을 더해 ~$135m EBITDA, interest·tax와 reduced shares로 EPS $9.40을 계산했다. sensitivity는 volume, spread 1¢/lb, debt와 share count에 집중해야 한다.",
    actual="2014~16 공시에서 repurchase·tuck-in·operating improvement가 이어졌다. Berry는 2016 약 $765m transaction을 발표했고 2017-01-20 종결했다. cash/stock 선택과 50/50 aggregate proration 때문에 deal value가 각 holder의 exact cash flow와 동일하지는 않다.",
    price="3년 stand-alone price/EPS horizon이 끝나기 전 merger가 종결됐다. $110 cash 또는 2.5011 BERY shares는 strategic value의 1차 anchor이나, share election·proration과 close-date BERY 가격을 복원해야 exact realized return을 계산할 수 있다.",
    drivers="trough spread 회복 가능성, scale·buyback이 만든 per-share convexity와 strategic buyer synergy가 수익을 만들었다. 핵심은 low reported earnings보다 normalized unit economics였다.",
    counterfactual="normalized spread가 원문보다 2¢/lb 낮고 volume이 capacity의 85%만 가동돼도 debt·tax 후 EPS와 $110 strategic value를 지지하는가?",
    error="normalized $9.40 EPS를 높은 확신의 3년 point estimate로 제시하고 buyer synergy가 포함된 takeout value와 stand-alone earnings를 구분하지 않을 위험이 있었다.",
    warning="stand-alone forecast를 직접 test하기 전 2016 deal이 발생했다. 따라서 EPS claim은 미검증, valuation/consolidation claim만 성공으로 판정해야 한다.",
    first_signal_date="2016-08-25",
    scenarios=[("Bear", "spread -2¢·85% utilization", "낮은 EPS·$50대", "stand-alone 미관찰"), ("Base", "$100m EBIT·$9.40 EPS", "normal multiple", "직접 미검증"), ("Strategic", "buyer synergy·consolidation", "$110", "2017 실현")],
    lessons=["spread manufacturer는 capacity×normalized unit margin으로 earnings를 재구축한다.", "strategic takeout은 stand-alone EPS가 아니라 consolidation value를 검증한다.", "deal consideration은 cash/stock election과 proration까지 cash-flow ledger로 만든다."],
    checklist=["capacity vs actual lbs", "spread/lb sensitivity", "resin lag", "depreciation·capex", "net debt", "FDSO·repurchases", "buyer synergy", "merger election·proration"],
    scorecard=[("Business thesis", "성공 방향"), ("Valuation thesis", "강한 성공"), ("EPS forecast", "직접 미검증"), ("Catalyst thesis", "consolidation 강한 성공"), ("External value", "2017 $110")],
    claims=[
        C("resin spread가 역사수준 정상화", "성공 방향", "trough spread가 mean으로 회복한다.", "customer price reset과 resin normalization이 spread/lb를 높인다.", "historical unit margins.", "industry structure·mix가 유지된다.", "multi-year spread가 trough에 고착되면 반증.", "operating improvement와 strategic bid가 normalization 가능성을 지지했다.", "exact spread series 제한.", "mean reversion의 속도·regime을 단순화했다.", "1¢/lb sensitivity와 cycle duration을 명시한다."),
        C("1.2bn lbs에서 EBIT $100m", "방향 성공·exact 제한", "capacity와 normal unit margin으로 $100m EBIT을 번다.", "volume×spread에서 conversion overhead를 차감한다.", "원문 capacity·margin bridge.", "utilization·product mix·maintenance capex가 정상이다.", "actual lbs·EBIT가 model에 반복 미달하면 반증.", "$765m strategic EV는 substantial earning power를 지지했다.", "exact $100m reported hit 미검증.", "capacity를 sold volume처럼 사용했다.", "capacity·utilization·saleable lbs를 구분한다."),
        C("EBITDA $135m·EPS $9.40", "직접 미검증", "depreciation·interest·tax·shares를 거쳐 $9.40 EPS.", "normalized EBIT과 lower share count가 EPS에 귀속된다.", "원문 3년 model.", "debt·tax·FDSO가 안정적이다.", "3년 reported EPS가 크게 미달하면 반증.", "2017 이전 merger로 stand-alone 3년 outcome 소멸.", "관찰불가—not automatically success.", "transaction을 forecast hit으로 대체할 위험.", "M&A censoring은 미검증으로 표시한다."),
        C("buybacks가 per-share value 증폭", "강한 성공", "저평가 시 shares를 줄인다.", "normalized enterprise earnings가 더 적은 주식에 귀속된다.", "과거 대규모 repurchase history.", "debt-funded repurchase가 solvency를 해치지 않는다.", "cheap equity 발행으로 되돌리면 반증.", "share count 감소와 높은 merger consideration이 per-share value를 확인했다.", "repurchase attribution은 제한.", "좋은 outcome에 capital allocation을 전부 귀속할 위험.", "share-count bridge와 funding cost를 같이 본다."),
        C("industry consolidation이 strategic value", "강한 성공", "규모·customer·plant network가 buyer에게 더 큰 가치다.", "buyer procurement·capacity rationalization synergy가 standalone EV를 높인다.", "fragmented flexible film industry.", "antitrust·integration·buyer interest가 허용된다.", "3년 내 strategic event·peer consolidation 부재면 촉매 약화.", "Berry가 약 $765m deal을 합의·종결했다.", "$110/2.5011 BERY consideration.", "buyer synergy를 T0 common의 standalone value와 섞을 수 있다.", "strategic case와 standalone case를 별도 확률로 둔다."),
        C("3년 내 value realization", "성공", "spread·buyback·consolidation이 3년 horizon에 실현된다.", "earnings improvement 또는 transaction이 discount를 닫는다.", "원문 three-year EPS target.", "catalyst가 2017-07 이전 발생한다.", "아무 catalyst 없이 discount 지속시 실패.", "2017-01-20 close로 horizon 내 crystallization.", "event timing 성공.", "deal announcement와 close·consideration을 구분해야 한다.", "catalyst는 sign·vote·close·cash receipt로 나눈다."),
    ],
    metrics=[("Capacity", "1.2bn lbs", "utilization", "strategic scale 유지", "방향 성공"), ("Normalized EBIT", "$100m", "3년", "exact 미검증", "제한"), ("Normalized EBITDA", "$135m", "3년", "deal EV 지지", "방향 성공"), ("EPS", "$9.40", "3년", "merger로 censored", "미검증"), ("Merger", "optional", "consolidation", "$110/2.5011 BERY", "강한 성공")],
    timeline=[("2014-07-09", "VIC Long 게시", "spread normalization"), ("2014~15", "repurchase·tuck-in 지속", "per-share value"), ("2016-01-14", "FY2015 10-K", "후속 operating base"), ("2016-08-25", "Berry merger agreement", "최초 decisive catalyst"), ("2016-12-15", "proxy filed", "$110/2.5011·proration"), ("2017-01-20", "merger close", "3년 horizon 내 value realization"), ("2017-01-23", "completion 8-K", "법적 종결 검증")],
)


add(
    id="38e54501-cdf7-4222-9b0d-548d1c21a844", date="2011-09-15",
    author="castor13", ticker="AER CN", company="Groupe Aeroplan Inc. / Aimia Inc.",
    filename="analysis/ideas/2011/2011-09-15_AER_groupe_aeroplan_long.md",
    source="https://www.valueinvestorsclub.com/idea/GROUPE_AEROPLAN_INC/2133679371",
    group="aimia", direction="Long", raw_direction="Long", security="Canadian AER/AIM common equity / Long",
    entry="원문 약 C$12대", horizon="2013", raw_horizon="C$1.60 FCF/share·C$24 target by 2013",
    title="loyalty-network high-FCF Long",
    verdict="혼합 — 현금엔진은 유효, C$24 실패·anchor-partner tail 현실화",
    score=6.7, process=9.7,
    conclusion=(
        "포인트 선판매·breakage·redemption spread의 capital-light economics와 단기 FCF 회복은 유효했다. 그러나 C$24 target는 "
        "실패했고 coalition diversification이 Air Canada anchor risk를 제거하지 못했다. 2017 non-renewal이 topology risk를 "
        "드러냈고 Aeroplan은 약 C$450m headline, 최종 조정 후 약 C$516m cash로 매각됐다. SQL 미국 AER 성과는 AerCap이라 폐기한다."
    ),
    t0=(
        "원문은 normalized FCF C$205m·C$1.25/share, 약 10% FCF yield와 2013 C$1.60/share를 제시했다. 21% breakage와 "
        "C$300m redemption reserve, Nectar·Carlson·analytics·신규 coalition을 근거로 Aeroplan Canada 의존도가 낮아지고 "
        "C$24가 가능하다고 봤다."
    ),
    reverse=(
        "시장은 accounting breakage·reserve의 추정오차보다 Air Canada와 카드사의 계약갱신·member utility가 단일 실패점임을 "
        "할인했다. coalition은 member 수가 많아도 핵심 airline reward와 accumulation partner가 빠지면 network value가 비선형으로 떨어진다."
    ),
    valuation=(
        "원문 C$1.60 FCF/share에 15배를 적용하면 C$24다. 하지만 FCF는 points issued와 redeemed의 timing, reserve release와 "
        "growth billings를 구분해야 한다. 경제적 부채를 차감한 owner earnings와 partner-renewal stress case에 서로 다른 multiple을 "
        "적용해야 했다."
    ),
    actual=(
        "초기 cash generation과 diversification은 일부 진전됐으나 2017-05-11 Air Canada가 2020 뒤 독자 loyalty plan을 발표했다. "
        "anchor risk가 현실화되자 Air Canada·TD·CIBC·Visa consortium이 Aeroplan을 다시 인수했고 2019 거래가 끝났다. Aimia는 "
        "핵심 loyalty asset을 판 뒤 investment holding company로 변했다."
    ),
    price=(
        "uploaded SQL의 AER 1~5년 price rows는 NYSE AerCap과 ticker collision이므로 전부 rejected다. Canadian AER/AIM의 "
        "corporate action·dividend series를 독립 복원하지 않아 exact return을 주장하지 않는다. 공개 역사 cross-check상 C$24 target는 "
        "달성하지 못한 것으로 판정한다."
    ),
    drivers="초기 가치는 float와 redemption economics가 만들었지만 장기 손실·discount는 Air Canada라는 anchor node의 계약권력, card-partner bargaining과 asset sale 이후 holdco discount가 만들었다.",
    counterfactual="Air Canada와 top card issuer가 동시에 이탈해 gross billings가 40% 감소해도 redemption liability·reserve 차감 후 common에 얼마가 남는가?",
    error="gross billings diversification과 network resiliency를 혼동하고, 계약 expiry·anchor topology를 breakage·reserve보다 낮은 우선순위로 뒀다.",
    warning="2017-05-11 Air Canada non-renewal 발표가 가장 명확한 thesis break였지만 계약 종료시점은 2020으로 T0에도 갱신 risk를 stress할 수 있었다.",
    first_signal_date="2017-05-11",
    scenarios=[("Bear", "Air Canada·card partner 이탈", "network break·asset sale", "2017~19 현실화"), ("Base", "C$1.60 FCF·15x", "C$24 by 2013", "실패"), ("Bull", "Nectar·analytics·new coalitions", "diversified compounder", "부분·anchor 미상쇄")],
    lessons=["network business는 member 수보다 제거했을 때 network가 무너지는 anchor node를 찾는다.", "loyalty FCF는 points liability·reserve·billings growth를 조정해 owner earnings로 본다.", "ticker가 같아도 exchange·법인·통화를 확인하기 전 성과를 붙이지 않는다."],
    checklist=["gross billings by partner", "contract expiry·renewal right", "active members", "issuance/redemption ratio", "cost per mile", "breakage sensitivity", "reserve adequacy", "entity·exchange audit"],
    scorecard=[("Business economics", "단기 성공"), ("Valuation thesis", "실패"), ("Diversification", "실패"), ("Timing / path", "C$24 미달"), ("Data quality", "SQL return 무효")],
    claims=[
        C("loyalty model은 capital-light/high-FCF", "성공", "포인트 선판매와 breakage가 낮은 capex로 FCF를 만든다.", "cash-in이 redemption cash-out보다 앞서 float와 spread가 생긴다.", "C$205m normalized FCF·C$300m reserve.", "partner contracts와 redemption economics가 안정적이다.", "billings·FCF가 구조적으로 감소하면 반증.", "초기 수년 현금창출과 Aeroplan의 매각가치가 franchise를 확인했다.", "경제적 부채 조정 후 FCF는 headline보다 낮을 수 있음.", "working-capital float를 영구 earnings로 볼 위험.", "issuance·redemption cohort와 liability를 함께 본다."),
        C("2013 FCF C$1.60/share", "부분 성공", "integration·growth로 per-share FCF가 C$1.60이 된다.", "core Canada와 Nectar·analytics가 비용을 흡수하고 성장한다.", "T0 C$1.25 normalized base.", "Carlson integration·partner economics가 개선된다.", "2013 owner FCF가 target에 크게 미달하면 반증.", "현금흐름은 개선됐으나 exact owner-FCF comparability가 회계변경으로 제한됐다.", "point estimate 완전 검증 제한.", "reported FCF와 economic FCF bridge가 부족했다.", "reserve·billings growth·one-offs를 조정한다."),
        C("C$24 by 2013", "실패", "C$1.60 FCF에 15x를 받아 두 배가 된다.", "earnings growth와 quality rerating이 결합한다.", "원문 explicit target.", "multiple이 partner concentration을 낮게 평가한다.", "2013까지 target 미달이면 실패.", "공개 역사 cross-check에서 C$24 미달.", "target 실패; SQL price는 사용 불가.", "earnings·multiple 두 가정을 하나로 묶었다.", "target 기여도를 FCF와 multiple로 나눈다."),
        C("diversification이 Air Canada 의존도를 낮춤", "실패", "Nectar·Carlson·new coalitions가 Canada concentration을 상쇄한다.", "지역·partner를 늘려 single-node risk를 줄인다.", "국제 assets와 JV pipeline.", "새 프로그램이 독립적으로 cash·member utility를 만든다.", "Air Canada 이탈이 group value를 크게 훼손하면 반증.", "2017 non-renewal이 equity와 전략을 재편했다.", "anchor loss가 diversification을 압도.", "revenue share와 network criticality를 혼동했다.", "partner concentration은 매출뿐 아니라 network removal test로 잰다."),
        C("partner contract risk manageable", "부분 실패", "contract terms·reserve가 renewal risk를 감당한다.", "장기 계약과 switching cost가 bargaining을 제한한다.", "Air Canada 관계·카드 partners.", "anchor airline이 자체 program을 만들 유인이 낮다.", "non-renewal 또는 economics 급격 재협상이면 반증.", "Air Canada가 2020 이후 non-renewal·독자 program을 발표했다.", "가장 중요한 tail이 현실화.", "expiry date를 tail event로만 처리했다.", "모든 critical contract에 expiry·renewal owner·outside option을 기록한다."),
        C("residual Aeroplan franchise value", "성공", "worst case에도 member base·data·brand가 strategic value를 가진다.", "airline·bank가 continuity를 위해 franchise를 산다.", "large active member network.", "redemption liability보다 buyer value가 높다.", "fire-sale 또는 negative equity면 반증.", "consortium이 C$450m headline cash와 liabilities를 인수; 최종 cash 약 C$516m.", "asset value는 존재하지만 original C$24 equity와 다름.", "asset value와 whole-company value를 섞었다.", "asset sale proceeds에서 liabilities·tax·holdco costs를 차감한다."),
    ],
    metrics=[("Normalized FCF", "C$205m/C$1.25", "2013 C$1.60", "초기 cash 유지·exact 제한", "부분"), ("Breakage", "21%", "stable spread", "anchor contract가 더 중요", "프레임 부족"), ("Target", "C$24 by 2013", "~2x", "미달", "실패"), ("Air Canada contract", "2020 expiry", "renew/manage", "2017 non-renewal", "실패"), ("Aeroplan sale", "미가정", "residual value", "C$450m headline/~C$516m final cash", "asset value 성공")],
    timeline=[("2011-09-15", "VIC Long 게시", "C$1.60 FCF·C$24"), ("2011-10", "Aimia brand 전환", "international diversification"), ("2013-12-31", "target horizon 종료", "C$24 미달"), ("2016-03", "Air Canada 자료가 2020 expiry 명시", "renewal clock"), ("2017-05-11", "Air Canada non-renewal", "decisive thesis break"), ("2018-07-25", "consortium proposal", "strategic residual value"), ("2018-11-26", "definitive agreement", "C$450m headline"), ("2019-01-10", "sale completion", "asset monetized·holdco 전환")],
)


add(
    id="c054b867-f345-429d-a2b4-fdf092a7c43b", date="2014-01-27",
    author="jso1123", ticker="AER", company="AerCap Holdings N.V.",
    filename="analysis/ideas/2014/2014-01-27_AER_aercap_long.md",
    source="https://www.valueinvestorsclub.com/idea/AERCAP_HOLDINGS_NV/4527154442",
    group="aercap", direction="Long", raw_direction="Long", security="NYSE:AER common equity / Long",
    entry="원문 약 $43대", horizon="약 24개월", raw_horizon="$60.50 target·2016 EPS $5.50",
    title="transformative ILFC aircraft-lessor M&A Long",
    verdict="사업·EPS 성공 / 주가·multiple timing 실패",
    score=7.4, process=9.8,
    conclusion=(
        "ILFC 인수는 fleet·funding·EPS accretion을 실현했고 2016 diluted EPS $5.52는 원문 $5.50과 거의 완벽히 일치했다. "
        "하지만 uploaded SQL price-only return은 1Y +8.8%, 2Y -18.4%, 5Y +26.3%여서 24개월 $60.50 rerating은 실패했다. "
        "정확한 earnings forecast와 좋은 stock call은 별개의 가설이다."
    ),
    t0=(
        "AIG의 forced sale로 AerCap이 ILFC를 취득해 fleet를 327대에서 약 1,300대로 확대하고 3년 lease revenue의 약 80%를 "
        "계약했다고 봤다. cost·tax·funding synergy와 leverage 감소로 ROE 15~17%, 2016 EPS $5.50, 약 11x P/E의 $60.50을 "
        "24개월 target로 제시했다."
    ),
    reverse=(
        "시장은 높은 debt/equity, aircraft residual value, airline credit, integration·refinancing과 lessor 업종의 persistent P/B "
        "discount를 반영했다. EPS가 맞아도 book quality와 tail risk가 재평가되지 않으면 multiple은 오르지 않는다."
    ),
    valuation=(
        "원문은 pro forma book 약 1.2x, ROE 15~17%, 2016 EPS $5.50에 11x를 적용했다. 이를 earnings claim과 multiple claim으로 "
        "분리하면 EPS는 적중했지만 11x rerating은 실패했다. lessor valuation은 P/E뿐 아니라 P/B, gain on sale, funding spread, "
        "stress asset haircut과 debt/equity를 함께 봐야 한다."
    ),
    actual=(
        "2014-05-14 거래가 종결됐고 AerCap은 AIG에 $3.0bn cash와 97,560,976 shares를 지급했다. 약 $45bn assets·1,300 aircraft "
        "platform이 됐고 financing facilities도 확대됐다. 2016 diluted EPS는 $5.52였다. 이후 buyback과 deleveraging을 했지만 업종 "
        "multiple은 낮았고, 장기에는 COVID·GECAS·러시아 asset seizure 같은 tail을 견뎠다."
    ),
    price=(
        "uploaded SQL price-only ratios는 1Y 1.0879, 2Y 0.8162, 3Y 1.1925, 5Y 1.2631이다. 즉 1Y +8.8%, 2Y -18.4%, "
        "3Y +19.2%, 5Y +26.3%이며 dividend·buyback benefit은 별도다. 24개월 target call은 명백히 실패했다."
    ),
    drivers="사업가치는 ILFC의 규모·order book·funding synergy와 buyback이 만들었다. 24개월 주가부진은 레버리지·residual-value tail과 업종 P/B discount가 earnings accretion을 상쇄한 결과다.",
    counterfactual="2016 EPS가 정확히 $5.50이어도 P/E 7x·P/B 0.8x이면 24개월 downside와 target IRR은 얼마인가?",
    error="deal EPS accretion을 valuation-regime change와 직결하고, aircraft asset haircut·funding spread가 multiple에 남길 영구 discount를 작게 봤다.",
    warning="2016-01-27 2년 price-only -18.4%가 target horizon 실패를 확정했으며 EPS miss가 아니라 multiple miss였다.",
    first_signal_date="2016-01-27",
    scenarios=[("Bear", "integration·funding stress·0.8x book", "$30대", "2Y -18.4%"), ("Base", "$5.50 EPS·11x", "$60.50", "EPS만 적중"), ("Long bull", "buyback·scale·deleveraging", "장기 appreciation", "5Y +26.3%")],
    lessons=["M&A earnings accretion과 valuation multiple rerating을 별도 claim으로 둔다.", "levered asset financier는 P/E보다 asset haircut 뒤 P/B·funding liquidity를 먼저 본다.", "EPS가 정확해도 security return이 실패할 수 있다."],
    checklist=["lease yield-funding cost", "utilization·collections", "gain on sale", "impairment", "debt/equity", "unsecured liquidity", "book/share", "buyback below book", "P/E·P/B separate"],
    scorecard=[("Business thesis", "강한 성공"), ("EPS thesis", "강한 성공"), ("Valuation thesis", "실패"), ("Timing / path", "2년 실패"), ("Security selection", "common duration 과소평가")],
    claims=[
        C("ILFC acquisition이 큰 EPS accretion", "강한 성공", "forced sale price와 scale로 EPS가 크게 늘어난다.", "lease revenue·order book·overhead scale이 주당 earnings를 높인다.", "327→~1,300 aircraft·contracted revenue.", "integration·credit·funding이 계획대로다.", "2016 EPS가 $5.50에 크게 미달하면 반증.", "2016 diluted EPS $5.52.", "+$0.02/+0.4%.", "EPS 적중을 stock thesis 적중으로 확장했다.", "earnings와 multiple claim을 독립 score한다."),
        C("cost·tax·funding synergy", "성공", "ILFC의 funding을 repricing하고 overhead·tax를 낮춘다.", "scale·credit access가 interest와 opex를 줄인다.", "deal financing·revolver·note plan.", "capital markets와 rating이 열려 있다.", "funding cost 상승·liquidity shortfall이면 반증.", "deal close와 후속 earnings가 synergy 실현을 지지했다.", "각 synergy bucket exact 공개 제한.", "gross synergy와 balance-sheet risk를 같은 방향으로만 봤다.", "funding synergy는 spread·maturity·secured mix로 검증한다."),
        C("leverage가 낮아짐", "방향 성공", "retained earnings·asset sales로 debt/equity를 약 4x 방향으로 낮춘다.", "FCF와 sale proceeds가 equity base를 키우고 debt를 줄인다.", "pro forma high leverage.", "residual loss·buyback이 deleveraging을 막지 않는다.", "debt/equity 정체·상승이면 반증.", "integration 뒤 deleveraging과 refinancing이 진행됐다.", "later GECAS로 다시 규모·leverage 변화.", "metric definition과 target date가 모호했다.", "gross debt, net debt, debt/equity를 날짜별로 고정한다."),
        C("15~17% ROE가 11x P/E를 지지", "부분 실패", "quality ROE가 normal financial multiple을 받는다.", "지속 ROE와 book compounding이 risk discount를 줄인다.", "pro forma ROE·book value.", "시장에 residual·tail·funding discount가 사라진다.", "EPS hit에도 P/E·P/B가 낮으면 반증.", "EPS는 맞았지만 2Y stock -18.4%로 rerating이 오지 않았다.", "multiple component 실패.", "accounting ROE를 low-risk ROE로 봤다.", "ROE를 leverage·gain on sale·impairment로 분해한다."),
        C("$60.50 within ~2 years", "실패", "$5.50 EPS × 11x로 target를 달성한다.", "earnings와 multiple이 동시에 실현된다.", "explicit target.", "deal close 뒤 risk discount가 빠르게 축소된다.", "2Y return이 음수면 실패.", "2Y price-only -18.4%.", "target 방향과 반대.", "time arbitrage의 시간이 너무 짧았다.", "catalyst가 earnings인지 market perception인지 구분한다."),
        C("discounted book buybacks가 accretive", "성공", "book 이하 자사주 매입이 per-share book·EPS를 높인다.", "자산 기대수익보다 높은 yield로 own shares를 산다.", "deal 뒤 large share base·AIG stake.", "book가 보수적이고 liquidity가 충분하다.", "impairments 또는 funding stress가 buyback accretion을 상쇄하면 반증.", "2015~16 buybacks와 per-share earnings가 확대됐다.", "tail risk는 후일 COVID·러시아에서 확인.", "book quality stress보다 arithmetic accretion을 앞세웠다.", "buyback은 stressed book와 liquidity buffer 뒤 계산한다."),
    ],
    metrics=[("2016 diluted EPS", "$5.50", "$5.50", "$5.52", "+0.4%/성공"), ("Fleet", "327+ILFC ~1,002", "~1,300", "deal close ~1,300", "성공"), ("Deal consideration", "modeled", "close", "$3.0bn cash+97.56m shares", "성공"), ("2Y price-only", "상승/$60.50", "~+40%", "-18.4%", "실패"), ("5Y price-only", "장기 upside", "상승", "+26.3%", "부분")],
    timeline=[("2014-01-27", "VIC Long 게시", "$60.50·$5.50 EPS"), ("2014-02-13", "shareholder approval", "closing risk 감소"), ("2014-05-14", "ILFC close", "$3.0bn+97.56m shares"), ("2014-07-11", "Q2 122 aircraft transactions", "integration activity"), ("2015~16", "buybacks·deleveraging", "per-share accretion"), ("2016-01-27", "2Y return -18.4%", "target failure"), ("2016-12-31", "diluted EPS $5.52", "earnings thesis hit"), ("2021-11-01", "GECAS close", "platform scale 재확대"), ("2022", "러시아 asset claims", "tail-risk stress"), ("2023", "insurance settlements·travel recovery", "long-duration resilience")],
)


def idea_sources(i):
    original = S(
        "VIC original idea" if i["source"] else "VIC source-DB preserved original",
        i["source"], "Value Investors Club / source SQL", i["date"],
        "T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.", "원문")
    return [original, *GROUP_SOURCES[i["group"]]]


def render_report(i):
    lines = [
        f"# {i['company']} ({i['ticker']}) — {i['date']} VIC {i['direction']}", "",
        "> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.",
        f"> **Research as-of:** {ASOF}. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.",
        "", "---", "", "## 0. Idea Snapshot", "", "| 항목 | 내용 |", "|---|---|",
        f"| 회사 / Ticker | {i['company']} / {i['ticker']} |",
        f"| VIC 게시일 / 작성자 | {i['date']} / {i['author']} |",
        f"| 분석 증권 / 실제 방향 | {i['security']} |",
        f"| 원 SQL 방향 | {i['raw_direction']} — raw 값 보존, research layer에서 원문 방향을 별도 검증 |",
        f"| 기준 진입가격 | {i['entry']} |", f"| 기대기간 | {i['horizon']} |",
        f"| raw horizon audit | {i['raw_horizon']} |", f"| 최종 판정 | **{i['verdict']}** |",
        "", f"> **결론:** {i['conclusion']}", "", "---", "",
        "## 1. 회사는 정확히 무엇을 하는가", "", BUSINESS[i["group"]], "",
        ENGINE[i["group"]], "", "### 가치사슬과 security payoff", "",
        "매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.",
        "", "### 매 분기 볼 핵심 KPI", "", KPI[i["group"]], "", "---", "",
        "## 2. 당시 상황과 시장이 가격에 넣은 것", "", i["t0"], "", "### Reverse expectations", "", i["reverse"], "", "---", "",
        "## 3. 원문 투자논지 지도", "",
    ]
    for n, c in enumerate(i["claims"], 1):
        lines += [
            f"### C{n}. {c['title']} — {c['verdict']}", "", "**원문 주장**", "", c["original"], "",
            "**경제적 메커니즘**", "", c["mechanism"], "", "**T0 근거**", "", c["evidence"], "",
            "**숨은 가정**", "", c["assumption"], "", "**사전 반증조건**", "", c["falsifier"], "",
            "**실제 결과**", "", c["actual"], "", "**정량 gap**", "", c["gap"], "",
            "**분석 오류 또는 제한**", "", c["error"], "", "**재사용 교훈**", "", c["lesson"], "",
        ]
    lines += [
        "---", "", "## 4. 당시 Valuation과 Payoff Structure", "", i["valuation"], "",
        "### 시나리오 분석", "", "| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |", "|---|---|---|---|",
    ]
    lines += ["| " + " | ".join(row) + " |" for row in i["scenarios"]]
    lines += ["", "### 핵심 수치", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["metrics"]]
    lines += [
        "", "### 촉매와 시간", "", f"판정 horizon은 **{i['horizon']}**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.",
        "", "---", "", "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "",
        "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|",
    ]
    lines += ["| " + " | ".join(row) + " |" for row in i["timeline"]]
    lines += [
        "", "### 실제 사업·자본구조 추이", "", i["actual"], "", "---", "",
        "## 6. 실제 투자결과 — 가격 경로와 실현 가능성", "", i["price"], "",
        "가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.",
        "", "---", "", "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 핵심 gap |", "|---|---|---:|---|---|",
    ]
    for n, (c, weight) in enumerate(zip(i["claims"], WEIGHTS), 1):
        lines.append(f"| C{n} | {c['title']} | {weight}% | {c['verdict']} | {c['gap']} |")
    lines += [
        "", "---", "", "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", i["drivers"], "",
        "### Counterfactual", "", i["counterfactual"], "", "---", "",
        "## 9. 분석 오류 유형과 최초 경고", "", i["error"], "",
        "### 최초로 관찰 가능했던 경고신호", "", i["warning"], "", "---", "",
        "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", "",
    ]
    for n, lesson in enumerate(i["lessons"], 1):
        lines += [f"### Lesson {n}", "", lesson, ""]
    lines += ["### 지금 같은 아이디어를 다시 본다면", ""] + [f"- {x}" for x in i["checklist"]]
    lines += ["", "---", "", "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scorecard"]]
    lines += [
        f"| Thesis score | {i['score']:.1f}/10 |", f"| Process score | {i['process']:.1f}/10 |",
        f"| 종합 | **{i['verdict']}** |", "", "### 한 문장 교훈", "", f"> {i['lessons'][0]}", "", "---", "",
        "## 12. Sources / Validation Notes", "",
    ]
    for n, source in enumerate(idea_sources(i), 1):
        if source["url"]:
            lines.append(f"{n}. [{source['title']}]({source['url']}) — {source['publisher']}, {source['date']}. {source['evidence']}")
        else:
            lines.append(f"{n}. {source['title']} — {source['publisher']}, {source['date']}. {source['evidence']}")
    quality = "A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준."
    if i["group"] == "plantation" or i["group"] == "aimia":
        perf_quality = "**REJECTED** — ticker collision으로 wrong-company 가격행을 폐기했다."
    elif i["group"] == "aepi" or i["group"] == "atlas":
        perf_quality = "**C/제한** — exact total-return ledger가 없어 target hit와 corporate-action value만 제한적으로 판정했다."
    else:
        perf_quality = "**B** — source SQL price-only ratios; dividends·tax 제외."
    lines += [
        "", "### 데이터 품질", "", f"- T0 원문·metadata: **{quality}**",
        "- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.", f"- 가격·수익률: {perf_quality}",
        f"- raw SQL direction은 **{i['raw_direction']}**, 실제 원문 방향은 **{i['direction']}**다. raw 값은 덮어쓰지 않았다.", "",
    ]
    return "\n".join(lines)


def build_idea_master(i, raw):
    perf = raw.get("raw_perf") if raw.get("performance_available") and not raw.get("performance_rejected") else None
    perf = perf or {}
    row = {
        "idea_id": i["id"], "date": i["date"], "year": int(i["date"][:4]),
        "ticker": i["ticker"], "company_name": i["company"], "author": i["author"],
        "is_short": int(raw.get("is_short", 0)), "direction_ko": "숏" if raw.get("is_short") else "롱",
        "idea_type_ko": "기업가치/증권분석", "source_link": i["source"] or None,
        "description_chars": None, "catalyst_chars": None, "contest_winner": 0,
        "auto_tag_status_ko": f"raw {i['raw_direction']} 보존·실제 {i['direction']}·법인/증권 수동검증 완료",
        "narrative_tags_ko": f"{i['group']}; entity audit; security mapping; valuation; catalyst; post-mortem",
        "horizon_raw": i["raw_horizon"], "horizon_months": None,
        "performance_available": int(bool(perf)),
    }
    for key in ("perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y"):
        row[key] = perf.get(key)
    for horizon in ("1y", "3y", "5y"):
        value = perf.get(f"perf_{horizon}")
        row[f"idea_return_{horizon}"] = None if value is None else value - 1
    return row


def make_payload():
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    raw_by_id = {row["idea_id"]: row for row in catalog["ideas_master"]}
    out = {
        "schema_version": "vic-deep-research-v9", "batch": 64,
        "title": "AEP / Atlas / AEP Industries / Aeroplan / AerCap — Entity, Denominator and Duration V9",
        "research_asof": ASOF,
        "metadata_audit": {
            "direction_corrections": 2, "company_mapping_corrections": 2,
            "performance_rows_rejected": 2, "corporate_action_return_warnings": 5,
            "notes": catalog.get("metadata_audit", {}).get("notes", []),
        },
        **{key: [] for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")},
    }
    for i in IDEAS:
        raw = raw_by_id[i["id"]]
        out["ideas_master"].append(build_idea_master(i, raw))
        corrected = out["ideas_master"][-1]
        return_parts = []
        for horizon in ("1y", "2y", "3y", "5y"):
            value = corrected.get(f"idea_return_{horizon}")
            if value is not None:
                return_parts.append(f"{horizon.upper()} {value:+.1%}")
        return_summary = ", ".join(return_parts) if return_parts else i["price"]
        out["postmortems"].append({
            "idea_id": i["id"], "ticker": i["ticker"], "research_direction_ko": i["direction"],
            "company_description_ko": BUSINESS[i["group"]], "original_thesis_ko": i["t0"],
            "actual_development_ko": i["actual"], "thesis_verdict_ko": i["conclusion"],
            "business_verdict_ko": i["scorecard"][0][1], "catalyst_verdict_ko": i["scorecard"][2][1],
            "valuation_verdict_ko": i["scorecard"][1][1], "stock_verdict_ko": i["price"],
            "current_verdict_ko": i["verdict"], "overall_verdict_ko": i["verdict"], "why_ko": i["drivers"],
            "success_pattern_ko": "entity_audit; security_mapping; primary_source_validation; denominator_decomposition; catalyst_calendar",
            "failure_pattern_ko": "ticker_collision; duration; peak_denominator; partner_concentration; corporate_action_complexity",
            "root_error_ko": i["error"], "first_signal_ko": i["warning"], "first_signal_date": i["first_signal_date"],
            "knowable_at_t0_ko": i["claims"][0]["evidence"] + " " + i["claims"][0]["falsifier"],
            "avoidability_ko": "중간~높음. 법인·증권·단위경제·horizon을 먼저 고정하고 claim별 반증조건을 추적하면 줄일 수 있었다.",
            "counterfactual_question_ko": i["counterfactual"],
            "analyst_note_ko": f"raw {i['raw_direction']} 보존; 실제 {i['direction']}. {i['raw_horizon']}",
            "corrected_return_1y": corrected.get("idea_return_1y"),
            "corrected_return_3y": corrected.get("idea_return_3y"),
            "corrected_return_5y": corrected.get("idea_return_5y"),
            "confidence": 0.97, "research_asof": ASOF,
            "research_status_ko": "1차자료 검증 완료·entity/security/return audit 완료",
        })
        out["meta"].append({
            "idea_id": i["id"],
            "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·가격·event calendar·first break·security payoff 장문분석",
            "report_version": "V9-canonical", "thesis_type_ko": i["title"],
            "one_line_verdict_ko": i["conclusion"], "thesis_score": i["score"], "process_score": i["process"],
            "return_summary_ko": return_summary, "core_error_ko": i["error"],
            "core_insight_ko": i["lessons"][0], "research_asof": ASOF,
        })
        section_rows = [
            ("회사·가치사슬·현금엔진", f"{BUSINESS[i['group']]}\n\n{ENGINE[i['group']]}\n\n핵심 KPI: {KPI[i['group']]}"),
            ("T0 시장기대·reverse expectations", f"{i['t0']}\n\n{i['reverse']}"),
            ("Valuation·payoff·실제경로", f"{i['valuation']}\n\n실제: {i['actual']}\n\n가격: {i['price']}"),
            ("사후인과·오류·교훈", f"{i['drivers']}\n\n오류: {i['error']}\n\nCounterfactual: {i['counterfactual']}"),
        ]
        for order, (title, body) in enumerate(section_rows, 1):
            out["sections"].append({"idea_id": i["id"], "section_order": order, "section_title_ko": title, "section_body_ko": body})
        for order, (claim, weight) in enumerate(zip(i["claims"], WEIGHTS), 1):
            out["claims"].append({
                "idea_id": i["id"], "claim_order": order, "claim_title_ko": claim["title"],
                "thesis_weight_pct": weight, "original_claim_ko": claim["original"],
                "t0_evidence_ko": claim["evidence"], "key_assumption_ko": claim["assumption"],
                "ex_ante_falsifier_ko": claim["falsifier"], "actual_result_ko": claim["actual"],
                "quantitative_gap_ko": claim["gap"], "verdict_ko": claim["verdict"],
                "analytical_error_ko": claim["error"], "reusable_lesson_ko": claim["lesson"],
            })
        for order, row in enumerate(i["metrics"], 1):
            out["metrics"].append({
                "idea_id": i["id"], "metric_order": order, "metric_name_ko": row[0],
                "t0_value_ko": row[1], "thesis_expectation_ko": row[2], "actual_value_ko": row[3],
                "verdict_ko": row[4], "interpretation_ko": f"{row[0]}의 T0 기대와 실제를 동일 단위가 가능한 범위에서 비교했다.",
            })
        for order, row in enumerate(i["timeline"], 1):
            out["timeline"].append({"idea_id": i["id"], "event_order": order, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for order, source in enumerate(idea_sources(i), 1):
            out["sources"].append({
                "idea_id": i["id"], "source_order": order, "source_type_ko": source["type"],
                "publisher": source["publisher"], "title_ko": source["title"], "source_date": source["date"],
                "url": source["url"], "evidence_ko": source["evidence"],
            })
    out["batch_lessons"] = [
        "AEP와 AER은 ticker만으로 법인을 매칭하면 전혀 다른 회사의 가격을 붙이게 된다.",
        "잘못 매칭된 performance row는 보정이 아니라 폐기가 원칙이다.",
        "roll-up은 pipeline과 record quarter를 확정 denominator로 쓰지 않는다.",
        "spread business는 revenue보다 units×spread와 working capital을 본다.",
        "strategic takeout은 terminal value를 검증하지만 예전 target horizon을 구제하지 않는다.",
        "network diversification은 member 수가 아니라 critical partner removal test로 검증한다.",
        "earnings forecast와 valuation-regime forecast는 서로 다른 claim과 falsifier를 가져야 한다.",
    ]
    return out


def render_index():
    rows = []
    for order, i in enumerate(IDEAS, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(f"| {order} | {i['date']} | {i['ticker']} | {i['raw_direction']} | {i['direction']} | [{i['company']}]({rel}) | {i['verdict']} |")
    lines = [
        "# Batch 064 — AEP / Atlas / AEP Industries / Aeroplan / AerCap V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. 법인·거래소·통화·증권·방향을 먼저 고정하고 성과와 corporate action을 검증했다.", "",
        "## Canonical idea files", "", "| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |", "|---:|---|---|---|---|---|---|",
        *rows, "", "## Entity / direction / performance audit", "",
        "- **AEP 2012:** American Electric Power가 아니라 LSE Anglo-Eastern Plantations(현재 AEP Plantations) Long이다. raw Short와 NYSE AEP 가격행은 보존하되 성과행은 폐기했다.",
        "- **Atlas 2022:** raw Short지만 원문은 TSX-V:AEP common Long이다.",
        "- **AER 2011:** NYSE AerCap이 아니라 Canadian Groupe Aeroplan/Aimia다. AerCap 가격행은 폐기했다.",
        "- **AER 2014:** 실제 NYSE AerCap이며 SQL price-only ratios를 제한적으로 유지했다.",
        "- **AEPI 네 건:** 같은 회사의 서로 다른 date-specific thesis다. 2017 merger consideration은 $110 cash 또는 2.5011 BERY shares, aggregate 50/50 proration이다.",
        "", "## 핵심 판정", "",
        "1. American Electric Power는 regulatory cash recovery·asset sale·EPS·$37 target가 대체로 맞은 강한 성공이다.",
        "2. AEP Plantations는 EV/ha·tree-age thesis가 장기 net cash/NAV compounding으로 검증됐지만 SQL return은 wrong entity다.",
        "3. Atlas 2020은 C$100m revenue가 38.1% 미달했고, Atlas 2022는 C$17m EBIT이 26.3% 미달했다. 두 price target는 뒤늦게 달성했다.",
        "4. AEPI는 spread·buyback·distressed M&A·consolidation이 맞았으나 초기 단기 target와 2017 takeout을 섞지 않았다.",
        "5. Aeroplan은 loyalty FCF를 맞혔지만 anchor-partner risk를 과소평가했고 C$24 target는 실패했다.",
        "6. AerCap은 2016 EPS $5.50 예상 대비 $5.52로 적중했지만 2년 price-only -18.4%로 multiple thesis는 실패했다.",
        "", "## 구조화 데이터", "",
        "- `data/curated/batch_064_aep_atlas_aepi_aer_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 상세 timeline·sources.",
        "- `data/curated/batch_064_source_catalog.json`: raw metadata·방향·ticker-collision 감사 source packet. 앱에는 직접 로드하지 않는다.",
        "- `analysis/batch_064_aep_atlas_aepi_aer_10.md`: Streamlit wrapper.", "",
        "## Batch 043 대비 보강점", "",
        "- 각 아이디어를 같은 0–12장 구조로 통일했다.",
        "- claim마다 T0 근거·숨은 가정·사전 반증조건·actual·정량 gap·오류·교훈을 기록했다.",
        "- 회사/SEC 1차자료 URL과 각 자료가 검증하는 수치를 sources table에 남겼다.",
        "- wrong-company return, corporate-action proration, delayed target와 operating forecast를 분리했다.", "",
    ]
    return "\n".join(lines)


def dedupe_batch_010():
    """Move the two AER records to their entity-audited Batch 064 canonicals."""
    path = ROOT / "data/curated/batch_010_transport_capital_structure_deep_v7.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    moved_ids = {
        "38e54501-cdf7-4222-9b0d-548d1c21a844",  # Groupe Aeroplan / Aimia, 2011
        "c054b867-f345-429d-a2b4-fdf092a7c43b",  # AerCap, 2014
    }
    removed = {}
    for key, rows in payload.items():
        if not isinstance(rows, list):
            continue
        before = len(rows)
        payload[key] = [row for row in rows if row.get("idea_id") not in moved_ids]
        if before != len(payload[key]):
            removed[key] = before - len(payload[key])
    missing = moved_ids - {
        row.get("idea_id")
        for key, rows in payload.items()
        if isinstance(rows, list)
        for row in rows
    }
    # Every moved ID must have existed in at least one Batch 010 table before this
    # function ran. On repeat runs, the explicit audit marker makes it idempotent.
    if not removed and payload.get("deduplication", {}).get("canonical_batch") != 64:
        raise ValueError(f"Batch 010 did not contain expected AER records: {sorted(missing)}")
    payload["deduplication"] = {
        "canonical_batch": 64,
        "moved_idea_ids": sorted(moved_ids),
        "reason_ko": "Groupe Aeroplan/Aimia와 AerCap의 entity·security·성과 감사를 Batch 064 장문 V9로 승격",
        "removed_rows_by_table": removed or payload["deduplication"].get("removed_rows_by_table", {}),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 064 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or sum(WEIGHTS) != 100:
            raise ValueError(f"{idea['id']}: six claims and five metrics required")
        report = ROOT / idea["filename"]
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(render_report(idea), encoding="utf-8")
    (ROOT / "analysis/batch_064_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [idea["filename"].removeprefix("analysis/") for idea in IDEAS]
    wrapper = (
        "# Batch 064 — AEP / Atlas Engineered Products / AEP Industries / Aeroplan / AerCap V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 064 V9 Index](batch_064_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_064_aep_atlas_aepi_aer_10.md").write_text(wrapper, encoding="utf-8")
    payload = make_payload()
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    dedupe_batch_010()
    print(
        f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} "
        f"timeline={len(payload['timeline'])} sources={len(payload['sources'])}"
    )


if __name__ == "__main__":
    main()
