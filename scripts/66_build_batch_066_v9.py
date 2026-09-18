#!/usr/bin/env python3
"""Build Batch 066 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
CATALOG = ROOT / "data/curated/batch_066_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_066_aetna_aetc_aether_ampex_aey_aeye_deep_v7.json"

spec = importlib.util.spec_from_file_location("batch64_base", ROOT / "scripts/64_build_batch_064_v9.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "aetna": (
        "Aetna는 당시 고용주·개인·정부 고객에게 health-benefit plan과 관련 관리서비스를 제공했다. 보험료와 fee revenue에서 "
        "medical claims, selling expense, tax와 자본비용을 차감한 underwriting margin이 핵심이다. membership growth만으로는 부족하고 "
        "premium yield와 medical cost trend의 차이, 즉 medical benefit ratio(MBR)가 주당이익을 결정한다."
    ),
    "aetc": (
        "Applied Extrusion Technologies는 식품·소비재 포장에 쓰이는 oriented polypropylene film을 생산했다. volume×price에서 resin·energy·"
        "conversion cost와 고정비를 뺀 spread 사업으로, 낮은 가동률과 원재료 급등 때 EBITDA가 빠르게 줄었다. 공장자산이 있어도 senior debt "
        "뒤의 common에는 충분한 잔여가치가 남지 않을 수 있다."
    ),
    "aether": (
        "Aether Systems는 무선 데이터 소프트웨어·서비스와 여러 지분투자를 가진 닷컴시대 회사였다. 이 아이디어의 대상은 common이 아니라 "
        "6% convertible subordinated notes due 2005다. 전환가치, 현금·투자자산으로 뒷받침되는 상환가치와 senior claims를 함께 봐야 하며, "
        "높은 주가 upside 없이도 par redemption이 수익의 주된 원천이었다."
    ),
    "ampex": (
        "Ampex는 data-storage 장비와 digital-imaging 특허 licensing으로 수익을 냈다. 특허 royalty는 높은 incremental margin을 가질 수 있지만 "
        "만기·소송·licensee volume에 따라 흔들리고, legacy storage의 손실과 debt service가 먼저 현금을 흡수한다. common은 모든 고정청구권 뒤의 잔여다."
    ),
    "aey": (
        "ADDvantage Technologies는 cable-TV 사업자에 새·수리·중고 네트워크 장비를 공급한 소형 유통·서비스 회사였다. 매출은 operator capex, "
        "OEM product cycle과 중고장비 가용성에 민감했다. receivable·inventory 중심의 NCAV와 tangible book은 청산계획·회수기간·haircut 없이 "
        "common의 영구적 floor가 되지 않는다."
    ),
    "audioeye": (
        "AudioEye는 웹사이트 접근성 진단·교정·모니터링 소프트웨어를 subscription으로 제공한다. partner channel과 direct enterprise 고객의 MRR, "
        "retention·ARPU·gross margin에서 sales/R&D와 remediation labor를 뺀 현금흐름이 가치다. 빠른 매출성장과 큰 TAM이 있어도 duration이 길면 "
        "entry revenue multiple과 자금소요가 주주수익을 좌우한다."
    ),
}

ENGINE = {
    "aetna": "premium + administrative fees - medical claims - SG&A - tax = earnings; membership·premium yield·MBR·share count를 EPS bridge로 연결한다.",
    "aetc": "film pounds × unit spread - fixed conversion cost - interest - maintenance capex = common cash; refinancing 뒤에도 through-cycle EBITDA와 debt paydown을 추적한다.",
    "aether": "unrestricted cash + realizable investments + operating value - senior claims - note principal = coverage; coupon·call price·accrued interest를 채권 payoff로 계산한다.",
    "ampex": "royalty receipts + storage gross profit - litigation/R&D/SG&A - interest - capex = residual cash; patent expiry와 debt waterfall을 common 가치에 적용한다.",
    "aey": "equipment volume × gross spread - personnel/warehouse cost - working-capital loss - capex = FCF; AR·inventory haircut 뒤 순현금을 주당가치로 본다.",
    "audioeye": "subscription MRR × retention + new bookings - service delivery - sales/R&D/G&A = FCF; revenue growth·gross margin·dilution과 terminal multiple을 분리한다.",
}

KPI = {
    "aetna": "membership, premium yield, medical cost trend, commercial MBR, SG&A ratio, operating EPS, FCF/share, buyback price, statutory capital",
    "aetc": "film volume, resin pass-through lag, unit spread, capacity utilization, EBITDA, interest coverage, net debt, maintenance capex, liquidity",
    "aether": "unrestricted cash, realizable investments, cash burn, senior claims, note coverage, coupon, call price, maturity, conversion value",
    "ampex": "royalty revenue, license concentration, patent life, storage gross margin, operating cash burn, interest, liquidity, net debt, restructuring priority",
    "aey": "sales, gross margin, inventory turns, receivable days, NCAV haircut, tangible book, operating cash flow, net cash/debt, supplier concentration",
    "audioeye": "MRR, ARR, customer count, organic growth, gross retention, gross margin, sales efficiency, adjusted EBITDA, FCF, diluted shares",
}


AETNA_SOURCES = [
    S("ING acquisition of Aetna Financial Services", "https://www.financial-planning.com/news/ing-buys-aetna-for-77-billion", "Financial Planning", "2000-07-20", "$5bn cash와 $2.7bn debt assumption의 거래구조 검증.", "2차자료"),
    S("Aetna FY2008 results", "https://media.corporate-ir.net/media_files/irol/11/110617/Aetna4Q08PressRelease.pdf", "Aetna", "2009-02-12", "2008 operating EPS $3.93과 2009 출발점 검증."),
    S("Aetna 2010 annual report", "https://oci.wi.gov/Documents/Companies/FinAetnaFormAEx9-E.pdf", "Aetna", "2011-02", "2009 operating EPS $2.75, commercial MBR와 membership·repurchase 후속 검증."),
    S("Aetna SEC filings", "https://www.sec.gov/edgar/browse/?CIK=1122304&owner=exclude", "SEC", "2000-2011", "거래·실적·자본환원 공시의 issuer-level 교차검증."),
]

AETC_SOURCES = [
    S("AETC senior-notes indenture", "https://contracts.justia.com/companies/applied-extrusion-technologies-inc-73721/contract/1050514/", "AETC / Justia SEC mirror", "2001", "$275m 10.75% senior notes due 2011 조건 검증."),
    S("AETC restructuring case", "https://www.youngconaway.com/experience/applied-extrusion-technologies-inc/", "Young Conaway", "2005", "2004-12-01 petition, 2005 plan confirmation·effective date 검증.", "전문가 사건자료"),
    S("AETC SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=755020&owner=exclude", "SEC", "2001-2004", "FY2002 실적과 refinancing·Chapter 11 공시 검증."),
]

AETHER_SOURCES = [
    S("Aether Systems SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=1086844&owner=exclude", "SEC", "2001-2004", "6% notes, cash/investment coverage와 2004 redemption 검증."),
    S("Aether corporate reorganization no-action letter", "https://www.sec.gov/divisions/corpfin/cf-noaction/aether042605.htm", "SEC", "2005-04-26", "후속 법인 재편과 security identity 교차검증."),
]

AMPEX_SOURCES = [
    S("Ampex 2008 Form 10-Q", "https://www.sec.gov/Archives/edgar/data/887433/000119312508178320/d10q.htm", "SEC / Ampex", "2008-08-18", "Chapter 11 plan, old common cancellation, contingent payment rights의 별도 취급 검증."),
    S("Ampex Chapter 11 8-K", "https://www.sec.gov/Archives/edgar/data/887433/000119312508168066/d8k.htm", "SEC / Ampex", "2008-08-06", "restructuring 절차와 capital-structure outcome 검증."),
    S("Ampex SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=887433&owner=exclude", "SEC", "2005-2008", "royalty·storage·debt 공시 교차검증."),
]

AEY_SOURCES = [
    S("ADDvantage SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=874292&owner=exclude", "SEC", "2010-2024", "연차실적, balance sheet, 영업중단과 Chapter 7 공시 검증."),
    S("ADDvantage annual reports", "https://www.annualreports.com/Company/addvantage-technologies-group-inc", "AnnualReports / company filings", "2010-2023", "FY별 sales·EPS·inventory·tangible equity 교차검증.", "공시 미러"),
]

AEYE_SOURCES = [
    S("AudioEye FY2023 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1362190/000141057824000150/aeye-20231231x10k.htm", "SEC / AudioEye", "2024-03-07", "FY2023 revenue $31.316m과 사업·risk-factor 검증."),
    S("AudioEye FY2024 results", "https://www.audioeye.com/post/audioeye-reports-record-fourth-quarter-and-full-year-2024-results/", "AudioEye", "2025-03", "FY2024 revenue $35.2m, gross profit $27.9m과 79% margin 검증."),
    S("AudioEye FY2025 results", "https://www.audioeye.com/post/audioeye-reports-fourth-quarter-and-full-year-2025-results/", "AudioEye", "2026-03", "FY2025 revenue $40.3m, gross profit $31.6m과 78% margin 검증."),
    S("AudioEye FY2025 annual report", "https://www.sec.gov/Archives/edgar/data/1362190/000110465926061290/aeye-20251231xars.pdf", "SEC / AudioEye", "2026", "장기 매출·gross margin·profitability 경로 교차검증."),
]

GROUP_SOURCES = {"aetna": AETNA_SOURCES, "aetc": AETC_SOURCES, "aether": AETHER_SOURCES, "ampex": AMPEX_SOURCES, "aey": AEY_SOURCES, "audioeye": AEYE_SOURCES}


IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


def scorecard(business, valuation, catalyst, security, timing):
    return [("Business thesis", business), ("Valuation thesis", valuation), ("Catalyst thesis", catalyst), ("Security payoff", security), ("Timing / path", timing)]


def lessons(group):
    return {
        "aetna": ["managed care의 낮은 P/E는 E가 MBR 변화에 얼마나 민감한지 확인한 뒤 판단한다.", "membership보다 premium yield와 medical cost trend의 spread를 우선한다.", "EPS 적중과 exit multiple 적중을 독립 claim으로 둔다.", "buyback은 normalized earnings가 아니라 실제 FCF·statutory capital로 제한한다."],
        "aetc": ["refinancing은 maturity를 옮길 뿐 earning power를 고치지 않는다.", "asset value는 senior debt와 shutdown cost 뒤의 common recovery로 계산한다.", "resin pass-through lag와 utilization을 through-cycle로 stress한다.", "다음 만기 전에 debt를 현금으로 얼마나 줄이는지 추적한다."],
        "aether": ["같은 issuer라도 common과 cash-covered convert의 payoff는 전혀 다르다.", "distressed bond는 conversion upside보다 hard coverage와 redemption terms를 먼저 본다.", "headline cash에서 burn·senior claims·restricted cash를 차감한다.", "정확한 IRR은 coupon settlement ledger가 있을 때만 계산한다."],
        "ampex": ["특허 royalty는 만기·소송·licensee volume을 반영한 declining asset로 본다.", "높은-margin revenue와 common FCF를 혼동하지 않는다.", "CPR은 old common 보존과 별도 청구권이다.", "legacy business와 debt가 royalty cash를 먼저 흡수하는지 본다."],
        "aey": ["NCAV는 정적 숫자가 아니라 회수시간 동안 녹을 수 있는 자산 묶음이다.", "inventory는 SKU obsolescence와 liquidation discount를 적용한다.", "tactical rerating과 durable business success를 분리한다.", "book floor에는 청산계획·현금 burn·senior claims가 필요하다."],
        "audioeye": ["성장률 적중과 시작 multiple의 정당화는 다른 문제다.", "MRR·customer count에서 revenue·gross profit·FCF까지 bridge한다.", "TAM보다 retention·sales efficiency·dilution을 우선한다.", "초기 price spike를 장기 earnings forecast의 증거로 소급하지 않는다."],
    }[group]


def checklist(group):
    return {
        "aetna": ["commercial MBR", "premium yield-cost trend gap", "membership mix", "operating vs GAAP EPS", "FCF/share", "repurchase price"],
        "aetc": ["resin lag", "utilization", "unit spread", "EBITDA-interest", "maintenance capex", "maturity schedule", "recovery waterfall"],
        "aether": ["unrestricted cash", "quarterly burn", "senior claims", "note coverage", "call price", "accrued coupon", "conversion value"],
        "ampex": ["patent expiry", "license concentration", "cash royalty", "legacy burn", "interest", "liquidity", "priority waterfall"],
        "aey": ["inventory aging", "AR collection", "NCAV haircut", "cash burn", "supplier concentration", "net debt", "liquidation plan"],
        "audioeye": ["MRR/ARR", "organic growth", "retention", "gross margin", "sales efficiency", "FCF", "FDSO", "EV/revenue"],
    }[group]


add(
    id="826d2a8a-6588-4de1-9c0f-a8a9737ce84f", date="2000-06-02", author="rich44", ticker="AET", company="Aetna Inc.", filename="analysis/ideas/2000/2000-06-02_AET_long.md", source="", group="aetna", direction="Long", raw_direction="Short", security="old Aetna common / breakup Long", entry="거래 전 old Aetna common", horizon="ING 거래 종결과 health-company 분리", raw_horizon="$35.33 cash + new health share; bull SOTP ~$134",
    title="Financial Services sale·health spin SOTP Long", verdict="거래 촉매 성공 / $134 SOTP는 미검증·과도", score=7.8, process=7.8,
    conclusion="원 SQL의 Short와 달리 원문은 breakup Long이다. ING 거래로 주주는 약 $35.33 현금과 신설 health company 한 주를 받아 핵심 촉매는 실현됐다. 다만 $134 bull SOTP는 거래 자체와 다른 multiple 가정이며 단기 실현값으로 소급하지 않는다.",
    t0="보험복합기업 Aetna는 health와 Financial Services가 함께 있어 sum-of-parts discount를 받았다. 원문은 금융사업 매각이 debt·복잡성을 낮추고 health franchise를 독립 평가하게 만든다고 봤다.", reverse="시장은 규제·거래종결 위험, debt assumption, stranded cost와 health underwriting 변동성을 할인했다. 매각 headline value가 모두 common에 현금으로 귀속되는 것도 아니었다.",
    valuation="$35.33 현금 + 신설 health share의 독립가치가 base payoff다. $134 bull case는 health earnings와 높은 multiple을 더한 SOTP로, 거래 consideration과 분리해야 한다.", actual="ING는 Financial Services를 약 $5bn cash와 $2.7bn debt assumption에 인수했고 old holders는 약 $35.33 cash와 신설 health share를 받았다. health 사업은 이후 독립 Aetna가 됐다.",
    price="corporate-action ledger가 기준이다. exact total return은 old share의 basis, cash timing, 신설주 opening/holding price와 세금이 필요해 만들지 않는다.", drivers="가치실현은 multiple 예측보다 signed asset sale과 legal distribution이 만들었다.", counterfactual="ING 거래가 깨져도 standalone health와 financial assets의 cash burn·debt를 차감한 downside가 entry를 지지했는가?", error="거래 촉매 적중과 공격적인 health-company terminal multiple을 한 성공으로 묶을 위험이다.", warning="거래조건 변경·규제지연 또는 신설 health MBR 악화가 최초 경고였으나 거래는 종결됐다.", first_signal_date="2000-12-13", lessons=lessons("aetna"), checklist=checklist("aetna"), scorecard=scorecard("분리 후 생존", "base 성공·bull 미검증", "강한 성공", "common 적절", "거래 horizon 성공"),
    scenarios=[("Bear", "거래 실패·health MBR 악화", "SOTP discount 지속", "미발생"), ("Base", "$35.33 cash+health share", "분리 가치", "실현"), ("Bull", "health 고배수", "~$134 SOTP", "단기 검증 불가")],
    metrics=[("Cash distribution", "약 $35.33/old share", "수령", "약 $35.33", "성공"), ("ING headline value", "$7.7bn", "거래 종결", "$5bn cash+$2.7bn debt", "성공"), ("New health share", "1 share", "분리", "1 share 배분", "성공"), ("Bull SOTP", "~$134", "rerating", "거래 payoff와 별도", "미검증"), ("Direction audit", "raw Short", "breakup Long", "Long", "교정")],
    timeline=[("2000-06-02", "VIC 게시", "breakup Long"), ("2000-07", "ING 거래 발표", "촉매 구체화"), ("2000-H2", "주주·규제 절차", "closing risk 감소"), ("2000-12-13", "거래 종결", "cash consideration 확정"), ("2000-12", "health company 분리", "standalone valuation 시작"), ("2001", "독립 Aetna 운영", "SOTP 현실화"), ("2002", "health underwriting 관찰", "business denominator 검증"), ("후속", "$134와 거래가치 분리", "과장 방지")],
    claims=[
        C("Financial Services 매각", "강한 성공", "ING 매각이 conglomerate discount를 해소한다.", "asset sale이 cash와 debt transfer를 만든다.", "협상·사업분리 가능성.", "regulatory·financing close.", "거래 철회·가격삭감이면 반증.", "$5bn cash+$2.7bn debt assumption으로 종결.", "headline $7.7bn 실현.", "headline EV와 equity cash 혼용 위험.", "debt assumption과 cash distribution을 분리한다."),
        C("$35.33 cash distribution", "성공", "old holder가 주당 약 $35.33 현금을 받는다.", "매각대금이 legal distribution으로 귀속된다.", "거래 terms.", "closing adjustment가 제한적이다.", "$30 미만이면 반증.", "약 $35.33 지급.", "대체로 일치.", "세금·지급일 ledger 부족.", "corporate action은 실제 consideration으로 검증한다."),
        C("health share 분리", "성공", "old holder가 신설 health 한 주를 받는다.", "spin이 standalone price discovery를 만든다.", "reorganization plan.", "spin이 종결된다.", "신설주 미배분이면 반증.", "한 주 배분.", "구조 일치.", "opening value를 bull value로 오해할 수 있음.", "분배 수량과 이후 valuation을 분리한다."),
        C("conglomerate discount 해소", "방향 성공", "분리 후 health가 독립 multiple을 받는다.", "복잡성·자본혼합 감소.", "SOTP discount.", "health economics가 안정적이다.", "MBR 악화로 독립가치 하락이면 제한.", "독립 Aetna가 형성됨.", "법적 분리는 확인·multiple magnitude 미확정.", "business risk를 구조 할인으로만 봄.", "spin 후 MBR를 새 출발점으로 본다."),
        C("~$134 SOTP", "미검증·과도", "health multiple까지 더해 큰 upside.", "earnings×higher multiple.", "bull SOTP.", "earnings와 multiple 동시 적중.", "독립주 가치가 크게 미달하면 반증.", "거래 consideration만으로는 증명되지 않음.", "정확한 terminal ledger 부재.", "촉매 성공으로 target를 소급 정당화.", "base consideration과 terminal multiple을 독립 평가한다."),
        C("raw Short", "metadata 실패", "SQL은 Short로 저장.", "방향 오류는 payoff를 반전시킨다.", "본문 breakup upside.", "원문 읽기.", "매각 실패에 베팅했다면 Short.", "실제 논지는 Long.", "완전 반대.", "metadata를 그대로 신뢰.", "원문 payoff와 security를 먼저 고정한다."),
    ],
)


add(
    id="8dc47f5d-3c8c-4cc9-9053-4de14a3892bf", date="2006-12-22", author="thistle933", ticker="AET", company="Aetna Inc.", filename="analysis/ideas/2006/2006-12-22_AET_long.md", source="", group="aetna", direction="Long", raw_direction="Long", security="Aetna common equity / Long", entry="2006 year-end AET common", horizon="2008", raw_horizon="2008 EPS $3.83, FCF/share $3.60, $65 target @17x",
    title="managed-care quality·FCF·buyback Long", verdict="EPS 성공 / multiple·$65 target 실패", score=6.8, process=7.5,
    conclusion="2008 operating EPS $3.93은 원문 $3.83을 2.6% 웃돌았지만 주가는 2008 고점 약 $59.19, 연말 $28.50로 $65 target를 달성하지 못했다. 기업 예측은 맞고 security outcome은 금융위기·multiple compression으로 실패했다.",
    t0="Aetna는 pricing discipline, scale과 buyback으로 두 자릿수 EPS 성장과 FCF/share $3.60을 낼 것으로 기대됐다. 원문은 quality managed-care franchise에 17x를 적용했다.", reverse="시장은 medical cost 재가속, 고용감소에 따른 membership mix, 규제와 cycle에서 17x가 유지되지 않을 위험을 가격에 넣었다.",
    valuation="2008 EPS $3.83×17x≈$65. denominator와 exit multiple 두 개의 동시 예측이다.", actual="FY2008 operating EPS는 $3.93로 forecast를 넘었다. 그러나 credit crisis와 risk-premium 상승 속에 주가는 연말 $28.50였고 17x multiple은 유지되지 않았다.",
    price="연중 고점 약 $59.19도 $65에 미달했고 year-end $28.50였다. exact total return은 배당·entry execution 없이 주장하지 않는다.", drivers="earnings는 underwriting·buyback이 지켰지만 주주수익의 병목은 exit multiple과 macro path였다.", counterfactual="EPS $3.83이 맞아도 8~10x stress multiple에서 downside가 견딜 만했는가?", error="quality와 EPS visibility를 17x terminal multiple의 안정성으로 번역했다.", warning="2008년 시장 multiple 급락과 주가가 EPS 증가를 따라가지 못한 것이 첫 결정적 경고였다.", first_signal_date="2008-09-15", lessons=lessons("aetna"), checklist=checklist("aetna"), scorecard=scorecard("성공", "실패", "EPS 적중", "common path 실패", "2008 target 실패"),
    scenarios=[("Bear", "MBR·multiple 동시 악화", "$30 이하", "year-end 현실화"), ("Base", "$3.83×17x", "$65", "미달"), ("Bull", "FCF·buyback rerating", "$65+", "미실현")],
    metrics=[("2008 operating EPS", "$3.83", "$3.83", "$3.93", "+2.6% 성공"), ("FCF/share", "$3.60", "$3.60", "exact comparable 제한", "미검증"), ("Target", "$65", "$65", "2008 high ~$59.19", "미달"), ("2008 year-end", "17x 기대", "$65", "$28.50", "실패"), ("Exit P/E", "17x", "유지", "약 7.3x on op EPS", "실패")],
    timeline=[("2006-12-22", "VIC Long", "$65 target"), ("2007", "earnings growth", "denominator 진행"), ("2008-H1", "operating EPS path", "forecast 유지"), ("2008", "주가 high ~$59.19", "target 미달"), ("2008-09", "credit crisis", "multiple 압축"), ("2008-12-31", "주가 $28.50", "stock thesis 실패"), ("2009-02", "FY2008 EPS $3.93", "EPS 성공"), ("2009", "MBR pressure", "다음 vintage 문제")],
    claims=[
        C("2008 operating EPS $3.83", "성공", "$3.83 EPS.", "pricing·scale·buyback.", "historical growth.", "MBR 안정.", "$3.45 미만이면 반증.", "$3.93.", "+$0.10/+2.6%.", "GAAP와 operating 구분.", "동일 EPS 정의로 비교한다."),
        C("FCF/share $3.60", "미검증", "$3.60 FCF/share.", "earnings cash conversion.", "low capital intensity.", "statutory cash upstream 가능.", "FCF가 EPS 크게 하회하면 반증.", "공개 비교치의 정의가 불완전.", "정량 판정 보류.", "보험 FCF 정의 불명확.", "parent cash와 statutory earnings를 분리한다."),
        C("pricing discipline", "기간 내 성공", "medical trend보다 premium을 높인다.", "spread가 MBR을 지킨다.", "underwriting history.", "cost trend 예측 정확.", "MBR 급등이면 반증.", "2008 EPS는 방어.", "2009에는 압력 발생.", "cycle 지속성을 과대평가.", "MBR를 분기별 falsifier로 둔다."),
        C("buyback accretion", "부분 성공", "FCF로 주당이익 가속.", "낮은 가격에 shares 감소.", "capital return capacity.", "statutory capital 충분.", "고가환매·capital constraint면 반증.", "EPS에 기여했으나 crisis 방어 못함.", "stock target 미달.", "buyback을 floor로 간주.", "price와 stress capital을 함께 본다."),
        C("17x multiple", "실패", "quality에 17x 부여.", "visibility가 risk premium을 낮춘다.", "peer valuation.", "macro·regulatory regime 안정.", "12x 아래면 반증.", "year-end 약 7.3x.", "-9.7 turns.", "regime risk 과소평가.", "stress multiple로 downside를 먼저 계산한다."),
        C("$65 target", "실패", "2008 $65.", "EPS×multiple.", "$3.83×17.", "두 축 동시 적중.", "horizon 내 미도달이면 실패.", "high ~$59.19, YE $28.50.", "high도 -8.9%, YE -56.2%.", "EPS 성공을 price 성공으로 혼동.", "target attribution을 분리한다."),
    ],
)


add(
    id="dc5c5284-22c4-4895-b229-5533c3c17608", date="2009-01-16", author="mitch395", ticker="AET", company="Aetna Inc.", filename="analysis/ideas/2009/2009-01-16_AET_long.md", source="", group="aetna", direction="Long", raw_direction="Short", security="Aetna common equity / crisis Long", entry="약 $25", horizon="2009~2010", raw_horizon="Street EPS $4.03, 11x target $44",
    title="crisis managed-care low-P/E Long", verdict="near-term earnings 실패 / $44는 2011로 지연", score=4.8, process=6.0,
    conclusion="낮은 6x P/E는 싸 보였지만 2009 operating EPS가 $2.75로 $4.03 기대를 31.8% 하회했다. commercial MBR은 80.3%에서 84.5%로 악화했다. 주가는 2011년에야 $44를 넘어 target timing이 실패했다.",
    t0="약 $25에서 Street 2009 EPS $4.03 대비 6.2x였다. membership 성장, balance-sheet strength와 약 $773m buyback이 downside를 막고 11x로 정상화될 것으로 봤다.", reverse="시장은 recession으로 pricing lag·unemployment·COBRA/mix가 claims ratio를 악화시켜 E 자체가 무너질 가능성을 반영했다.",
    valuation="$4.03×11x≈$44. 낮은 multiple만 강조하면 denominator downside를 놓친다.", actual="2009 operating EPS $2.75, commercial MBR 84.5% vs 80.3%, membership 약 +1.2m였다. buyback 약 $773m에도 underwriting deterioration가 컸다. 2011 operating EPS는 $5.17, 주가 high는 약 $46였다.",
    price="near-term target는 실패했고 약 2년 뒤에야 가격이 회복했다. exact total return은 별도 ledger 없이 주장하지 않는다.", drivers="회복은 원래 2009 EPS가 아니라 후속 repricing·cost control과 cycle 정상화가 만들었다.", counterfactual="$2.75 EPS와 8x multiple을 T0 base로 썼어도 충분한 margin of safety가 있었는가?", error="낮은 P/E의 E를 cyclically stable하다고 가정했다.", warning="2009 commercial MBR 84.5%와 operating EPS $2.75가 최초의 명확한 반증이었다.", first_signal_date="2009-12-31", lessons=lessons("aetna"), checklist=checklist("aetna"), scorecard=scorecard("장기 회복", "지연", "near-term 실패", "common 생존", "horizon 실패"),
    scenarios=[("Bear", "MBR 84%+·EPS <$3", "$20대", "현실화"), ("Base", "$4.03×11x", "$44", "2009 실패"), ("Recovery", "repricing·EPS $5+", "$44+", "2011 지연")],
    metrics=[("2009 op EPS", "$4.03 Street", "$4.03", "$2.75", "-31.8%"), ("Commercial MBR", "80.3% prior", "안정", "84.5%", "+4.2ppt 실패"), ("Membership", "성장", "증가", "+~1.2m", "성공"), ("Repurchase", "support", "대규모", "~$773m", "실행"), ("Price target", "$25→$44", "2009~10", "2011 high ~$46", "지연")],
    timeline=[("2009-01-16", "VIC Long", "6x P/E"), ("2009-H1", "recession claims pressure", "denominator 위험"), ("2009", "membership +~1.2m", "volume 성공"), ("2009", "repurchase ~$773m", "capital return"), ("2009-12", "op EPS $2.75", "forecast 반증"), ("2009-12", "MBR 84.5%", "첫 경고"), ("2010", "repricing·recovery", "새 thesis"), ("2011", "EPS $5.17/high ~$46", "지연 회복")],
    claims=[
        C("EPS $4.03", "강한 실패", "2009 EPS $4.03.", "membership·pricing·buyback.", "Street estimate.", "MBR 안정.", "$3.60 미만이면 반증.", "$2.75.", "-$1.28/-31.8%.", "cyclical E 고정.", "low P/E는 stress E로 재계산한다."),
        C("commercial MBR 안정", "실패", "underwriting 유지.", "premium trend가 claims를 상쇄.", "80.3% prior.", "pricing lag 제한.", "83% 초과면 반증.", "84.5%.", "+4.2ppt.", "lagged medical trend 과소평가.", "MBR를 핵심 falsifier로 둔다."),
        C("membership growth", "성공·무가치", "membership 증가.", "scale이 earnings를 높임.", "employer reach.", "mix와 margin 유지.", "growth 중 MBR 악화면 질 낮음.", "+~1.2m이나 EPS 하락.", "volume 성공/margin 실패.", "회원 수를 economics와 동일시.", "회원당 margin을 본다."),
        C("$773m buyback", "실행·방어 실패", "환매가 per-share downside를 막는다.", "share count 감소.", "capital capacity.", "earnings base 유지.", "EPS 하락이 accretion 상쇄하면 반증.", "환매 실행에도 EPS miss.", "floor 역할 못함.", "capital return 과대평가.", "stress earnings 뒤 accretion을 계산한다."),
        C("11x normalization", "지연", "11x 회복.", "crisis premium 소멸.", "historical multiple.", "earnings가 유지.", "horizon 내 미회복이면 실패.", "2011 회복.", "약 2년 지연.", "E와 multiple의 상관을 무시.", "동시 stress를 쓴다."),
        C("$44 target", "지연 성공·원 thesis 실패", "$44 near term.", "$4.03×11.", "명시 target.", "2009~10 실현.", "2010까지 미도달이면 실패.", "2011 high ~$46.", "horizon 밖.", "delayed recovery를 소급 성공 처리.", "가격·날짜·driver를 함께 판정한다."),
    ],
)


add(
    id="7de7d136-8f14-42f8-ac66-6f33af6f9419", date="2001-06-12", author="grah141", ticker="AETC", company="Applied Extrusion Technologies", filename="analysis/ideas/2001/2001-06-12_AETC_long.md", source="", group="aetc", direction="Long", raw_direction="Short", security="AETC common equity / Long", entry="약 $6.10", horizon="FY2002", raw_horizon="0.9x TBV, 0.28x sales, FY2002 EPS $1.50",
    title="refinancing·cheap industrial common Long", verdict="refinancing 성공 / earnings·common terminal 실패", score=2.8, process=3.2,
    conclusion="$275m 10.75% notes로 당장 만기벽은 넘겼지만 FY2002 sales 약 $252.1m, net loss -$31.8m, EPS -$2.55로 $1.50 기대가 완전히 무너졌다. 2004 Chapter 11과 2005 plan에서 old common은 취소됐다.",
    t0="주가 약 $6.10, 0.9x tangible book와 0.28x sales였다. 원문은 capacity·customer franchise와 refinancing이 정상 EPS $1.50을 회복시킬 것으로 봤다.", reverse="시장은 resin spread, pricing power 부족, 과잉설비, 높은 fixed cost와 refinancing 이후에도 남는 leverage를 할인했다.",
    valuation="TBV·sales multiple은 assets가 경제적으로 생산적이고 debt 뒤에 잔여가치가 있을 때만 의미가 있다. $1.50 EPS 회복은 refinancing과 산업 정상화를 동시에 요구했다.", actual="$275m 10.75% senior notes due 2011 발행으로 2001 maturity wall은 연장됐다. 그러나 FY2002 sales 약 $252.1m, net loss -$31.8m, EPS -$2.55. 2004-12-01 Chapter 11, 2005 plan에서 old common cancellation.",
    price="terminal payoff는 old common 0이다. 중간 거래가격 없이 exact holding-period return은 만들지 않지만 common의 최종 impairment는 명확하다.", drivers="loss는 refinancing 실패가 아니라 불량한 unit economics가 debt service를 감당하지 못한 데서 났다.", counterfactual="refinancing 후 resin shock과 80% utilization에서도 interest와 maintenance capex를 낼 수 있었는가?", error="liquidity catalyst를 solvency와 earnings catalyst로 오인하고 book·sales를 debt waterfall 앞에서 평가했다.", warning="FY2002 EPS -$2.55가 $1.50 예상과 반대로 나온 시점이 최초의 결정적 반증이었다.", first_signal_date="2002-09-30", lessons=lessons("aetc"), checklist=checklist("aetc"), scorecard=scorecard("실패", "강한 실패", "refinancing만 성공", "common 0", "FY2002부터 반증"),
    scenarios=[("Bear", "spread 압박·high leverage", "Chapter 11/common 0", "현실화"), ("Base", "FY02 EPS $1.50", "$6.10 rerating", "강한 미달"), ("Bull", "asset value+deleveraging", "TBV 이상", "미실현")],
    metrics=[("Senior notes", "refinancing 필요", "$275m 발행", "$275m 10.75% due 2011", "촉매 성공"), ("FY2002 sales", "회복", "성장", "~$252.1m", "margin 미달"), ("FY2002 net income", "흑자", "EPS $1.50", "-$31.8m", "강한 실패"), ("FY2002 EPS", "$1.50", "$1.50", "-$2.55", "-$4.05"), ("Old common", "TBV floor", "보존", "2005 취소", "terminal 0")],
    timeline=[("2001-06-12", "VIC Long", "refinancing thesis"), ("2001", "$275m notes", "maturity 연장"), ("2002", "resin/spread 압박", "economics 악화"), ("2002-09", "EPS -$2.55", "핵심 반증"), ("2003", "leverage 지속", "solvency 위험"), ("2004-12-01", "Chapter 11", "waterfall 현실화"), ("2005-01-24", "plan confirmed", "common 취소 승인"), ("2005-03-08", "plan effective", "terminal 0")],
    claims=[
        C("2001 refinancing", "성공", "maturity wall 해소.", "장기채로 단기부채 상환.", "capital-market plan.", "10.75% 이자 감당.", "deal 미종결이면 반증.", "$275m notes 발행.", "촉매 일치.", "만기연장을 가치창출로 봄.", "refinancing 뒤 interest coverage를 다시 계산한다."),
        C("FY2002 EPS $1.50", "강한 실패", "정상화 EPS $1.50.", "volume·spread 회복.", "capacity와 historical margin.", "resin pass-through 가능.", "$0.75 미만이면 반증.", "-$2.55.", "-$4.05.", "cycle/operating leverage 과소평가.", "through-cycle spread로 본다."),
        C("0.9x TBV floor", "실패", "tangible assets가 downside 보호.", "매각가치가 book 근처.", "공장자산.", "가동·saleability·debt coverage.", "impairment/common cancellation이면 반증.", "old common 취소.", "recovery 0.", "gross asset와 equity value 혼동.", "net liquidation waterfall을 계산한다."),
        C("0.28x sales 저평가", "실패", "낮은 P/S가 rerating.", "정상 margin 회복.", "매출기반 유지.", "positive unit margin.", "매출 있어도 손실이면 반증.", "$252.1m sales에도 -$31.8m loss.", "revenue multiple 무의미.", "sales quality 미검증.", "unit spread와 FCF로 대체한다."),
        C("pricing power", "실패", "resin을 고객에게 전가.", "pass-through로 spread 방어.", "포장재 고객관계.", "lag·경쟁 제한.", "gross margin 붕괴면 반증.", "손실·파산.", "economics 반대.", "contract 구조를 추정.", "lag와 volume elasticity를 측정한다."),
        C("common survival", "강한 실패", "refinancing으로 equity 보존.", "시간을 벌어 debt paydown.", "만기연장.", "영업현금 흑자.", "재파산·취소면 반증.", "2005 cancellation.", "terminal 100% loss.", "liquidity와 solvency 혼동.", "security waterfall을 먼저 본다."),
    ],
)


add(
    id="b319da47-1ea4-4ce0-a6c4-cc797616b439", date="2001-04-29", author="gumpster335", ticker="AETH Corp", company="Aether Systems", filename="analysis/ideas/2001/2001-04-29_AETH_convert_long.md", source="https://www.valueinvestorsclub.com/idea/Aether_Systems_6_percen_05_Co/6957633241", group="aether", direction="Long", raw_direction="Long", security="6% convertible subordinated notes due 2005 / Long", entry="약 59 cents on par", horizon="2005 maturity", raw_horizon="6% coupon, conversion $243.95, cash-covered par recovery",
    title="cash-covered distressed convert Long", verdict="강한 성공 — security selection과 par redemption", score=9.0, process=9.2,
    conclusion="common 약 $13.89에서 $243.95 conversion은 사실상 out-of-the-money였지만 note는 약 59에 샀고 6% coupon을 받았다. 회사는 2004-10-04에 101.2% par+accrued interest로 조기상환했다. 정확한 IRR은 coupon settlement ledger 없이 과장하지 않는다.",
    t0="닷컴 붕괴로 common은 크게 하락했지만 issuer의 cash·investments가 note principal을 상당히 덮는다는 논지였다. upside는 전환보다 credit recovery였다.", reverse="시장은 cash burn, 투자자산 가치하락, subordination과 2005 전 유동성 소진을 할인했다.",
    valuation="59 purchase price에서 6 coupon의 current yield는 약 10.2%. par 또는 101.2 call이면 가격 recovery가 크지만 conversion value는 거의 0으로 두는 것이 보수적이다.", actual="6% convertible subordinated notes는 2004-10-04에 101.2% of par plus accrued interest로 redeemed됐다. common이 전환가를 회복할 필요가 없었다.",
    price="확정 terminal consideration은 101.2+accrued interest다. 개별 coupon dates와 reinvestment가 없어 exact annualized return은 보류한다.", drivers="수익은 사업 turnaround가 아니라 discounted fixed claim과 cash coverage, issuer의 조기 redemption에서 나왔다.", counterfactual="분기 burn이 두 배이고 투자자산을 50% haircut해도 senior claims 뒤 note principal이 덮였는가?", error="결론은 맞았지만 headline cash에서 operating burn과 senior/restricted claims를 더 명시적으로 차감했어야 한다.", warning="note coverage가 1x 아래로 떨어지거나 분기 burn이 가속되면 첫 경고였으나 redemption이 먼저 일어났다.", first_signal_date="2004-10-04", lessons=lessons("aether"), checklist=checklist("aether"), scorecard=scorecard("common 불필요", "강한 성공", "redemption 성공", "convert 적절", "만기 전 성공"),
    scenarios=[("Bear", "cash burn·asset haircut", "par 미달 recovery", "미발생"), ("Base", "maturity par", "coupon+41pt gain", "조기 초과실현"), ("Bull", "conversion", "$243.95+ common", "불필요")],
    metrics=[("Purchase price", "59", "par recovery", "101.2 redemption", "강한 성공"), ("Coupon", "6%", "지급", "redemption 전 지급", "성공"), ("Current yield", "~10.2%", "유지", "coupon/59", "성공"), ("Conversion price", "$243.95", "optionality", "common ~$13.89 at T0", "무가치 option"), ("Maturity", "2005", "상환", "2004-10-04 조기상환", "조기 성공")],
    timeline=[("2001-04-29", "VIC note Long", "59 purchase"), ("2001", "common ~$13.89", "conversion far OTM"), ("2002", "cash coverage 추적", "credit thesis"), ("2003", "burn·asset monetization", "coverage 유지"), ("2004-H1", "redemption 여력", "catalyst 접근"), ("2004-10-04", "101.2 call", "principal recovery"), ("2004-10-04", "accrued interest 지급", "coupon settlement"), ("2005", "원 maturity", "그 전에 종료")],
    claims=[
        C("cash covers note", "성공", "cash·investments가 principal을 덮는다.", "hard assets가 credit floor.", "balance sheet.", "burn 제한·assets realizable.", "coverage <1x면 반증.", "101.2 redemption 가능.", "principal 전액+premium.", "restricted/senior 차감 부족.", "net hard coverage를 쓴다."),
        C("6% coupon", "성공", "보유 중 6% coupon.", "contractual cash payment.", "indenture.", "default 없음.", "coupon 중단이면 반증.", "상환 전 지급.", "current yield ~10.2%.", "settlement dates 미복원.", "exact IRR은 ledger 후 계산한다."),
        C("par recovery", "강한 성공", "59→100.", "maturity/redemption.", "discounted note.", "issuer solvent.", "recovery <80이면 반증.", "101.2+accrued.", "+42.2 points before coupon.", "none material.", "fixed claim의 terminal term을 기준으로 판정한다."),
        C("conversion upside", "불필요·미실현", "$243.95 conversion option.", "common rally 때 upside.", "convert feature.", "common 17x+ 상승.", "far OTM 지속이면 0 가치.", "T0 common ~$13.89; credit payoff로 종료.", "option 거의 0.", "convert 명칭이 upside를 과장.", "straight bond로도 매력적인지 본다."),
        C("cash burn manageable", "성공", "운영 burn이 coverage를 소진하지 않는다.", "cost cuts·asset monetization.", "large cash base.", "분기 burn 감소.", "redemption 전 liquidity crisis면 반증.", "조기상환.", "위기 없음.", "burn path 단순화.", "quarterly sources/uses를 갱신한다."),
        C("security beats common", "강한 성공", "common 대신 note가 downside를 제한.", "priority와 contractual maturity.", "subordinated라도 common보다 선순위.", "senior claims 과도하지 않음.", "common 상승 없고 note도 haircut이면 반증.", "common recovery 불필요, note 101.2.", "구조적 payoff 적중.", "issuer thesis보다 security thesis가 핵심.", "capital structure 전체에서 최적 claim을 고른다."),
    ],
)


add(
    id="425a90ba-11d6-4ef8-9f56-a8ab158b9d59", date="2005-02-01", author="gearl1818", ticker="AEXCA", company="Ampex Corporation", filename="analysis/ideas/2005/2005-02-01_AEXCA_long.md", source="https://www.valueinvestorsclub.com/idea/Ampex_Corporation/6253988944", group="ampex", direction="Long", raw_direction="Long", security="Ampex Class A common / Long", entry="2005 common", horizon="2014 patent cash-flow window", raw_horizon="minimum EPS ~$6.25 through 2014 from royalty+storage",
    title="IP royalty·deleveraging common Long", verdict="강한 실패 — royalty를 common annuity로 오인", score=2.2, process=2.5,
    conclusion="digital-imaging royalty의 높은 margin은 맞았지만 legacy storage 손실·debt·patent duration이 common 현금을 흡수했다. 2008 Chapter 11 plan에서 existing Class A common은 취소됐고 distribution은 없었다. CPR은 별도 contingent claim이다.",
    t0="원문은 licensing stream과 storage turnaround를 합쳐 최소 EPS 약 $6.25가 2014까지 지속될 것으로 봤다. 특허가치를 common per-share annuity처럼 평가했다.", reverse="시장은 royalty concentration·patent expiry/litigation, legacy cash burn, leverage와 small-cap governance를 할인했다.",
    valuation="$6.25 minimum EPS×multiple 접근은 royalty의 유한수명과 debt priority, storage losses를 충분히 haircut하지 않았다.", actual="영업·자본구조 압력이 이어져 2008 Chapter 11. SEC 공시상 old common, options와 restricted shares는 취소되고 분배가 없었다. CPR은 약 $83.8m threshold 이후 조건부로 설계돼 common 보존과 다르다.",
    price="old Class A common terminal payoff는 0이다. CPR을 common recovery로 합산하지 않는다.", drivers="loss는 특허자산 자체보다 그 cash flow가 debt·legacy burn·restructuring priority 뒤 common까지 도달하지 않은 데서 났다.", counterfactual="royalty가 50% 감소하고 storage가 계속 손실이어도 debt service 뒤 common FCF가 양수였는가?", error="gross royalty를 durable per-share earnings로 자본화하고 claim priority와 patent duration을 누락했다.", warning="cash burn과 debt pressure가 royalty cash를 상쇄한 시점이 첫 경고였고 2008 filing이 terminal break였다.", first_signal_date="2007-12-31", lessons=lessons("ampex"), checklist=checklist("ampex"), scorecard=scorecard("실패", "강한 실패", "deleveraging 실패", "common 0", "2008 terminal") ,
    scenarios=[("Bear", "royalty decline+storage burn", "restructuring/common 0", "현실화"), ("Base", "EPS $6.25 지속", "큰 upside", "실패"), ("Bull", "new licenses+debt paydown", "2014 annuity", "미실현")],
    metrics=[("Minimum EPS", "~$6.25", "through 2014", "지속되지 않음", "강한 실패"), ("Royalty duration", "2014", "현금 annuity", "patent/litigation risk", "과대"), ("Legacy storage", "turnaround", "흑자", "cash drain", "실패"), ("Chapter 11", "배제", "없음", "2008", "terminal 반증"), ("Old common", "가치 보존", "distribution", "취소/no distribution", "0")],
    timeline=[("2005-02-01", "VIC Long", "IP annuity thesis"), ("2005", "royalty receipts", "headline strength"), ("2006", "legacy losses", "cash conversion 약화"), ("2007", "liquidity pressure", "first break"), ("2008-03-30", "Chapter 11", "capital structure 실패"), ("2008-08-06", "plan disclosure", "old common treatment"), ("2008", "common cancellation", "terminal 0"), ("후속", "CPR 별도", "common recovery 아님")],
    claims=[
        C("EPS ~$6.25", "강한 실패", "최소 EPS $6.25.", "royalty+storage earnings.", "license economics.", "cash royalty 지속·loss 축소.", "EPS/FCF가 크게 미달하면 반증.", "파산·common 취소.", "terminal 0.", "gross royalty를 EPS로 직결.", "cash-to-common bridge가 필요하다."),
        C("royalty annuity through 2014", "실패", "특허 cash가 장기간 지속.", "licenses·settlements.", "patent portfolio.", "expiry·challenge 제한.", "royalty 하락·소송비 증가면 반증.", "common까지 지속되지 않음.", "duration 부족.", "유한 특허를 perpetuity처럼 봄.", "license별 expiry와 net cash를 본다."),
        C("storage turnaround", "실패", "legacy storage가 흑자 전환.", "cost cuts·product demand.", "installed base.", "매출·margin 회복.", "반복 operating loss면 반증.", "cash drain 지속.", "common FCF 악화.", "optional upside를 base에 포함.", "loss business는 0이 아니라 closure cost를 둔다."),
        C("deleveraging", "실패", "royalty로 debt를 줄인다.", "cash sweep이 interest를 낮춤.", "high-margin receipts.", "burn보다 royalty 큼.", "liquidity stress면 반증.", "Chapter 11.", "완전 반대.", "cash gross와 net 혼동.", "sources/uses waterfall을 분기별로 만든다."),
        C("common retains IP value", "강한 실패", "특허가 common floor.", "sale/reorg 잔여가치.", "IP asset.", "claims보다 value 큼.", "common cancellation이면 반증.", "취소/no distribution.", "recovery 0.", "EV와 equity 혼동.", "senior claims 뒤 recovery를 계산한다."),
        C("CPR as recovery", "분리 필요", "후속권리가 주주가치 보완.", "threshold 이후 contingent payment.", "plan terms.", "threshold 달성·old holder entitlement.", "무조건 common recovery로 보면 오류.", "약 $83.8m threshold의 별도 CPR.", "즉시 common 분배 0.", "다른 security를 합산.", "CPR을 독립 option으로 평가한다."),
    ],
)


add(
    id="d8f41b2d-ca72-4538-acdf-17ceb68bd542", date="2010-09-02", author="clancy836", ticker="AEY", company="ADDvantage Technologies Group", filename="analysis/ideas/2010/2010-09-02_AEY_long.md", source="https://www.valueinvestorsclub.com/idea/ADDVANTAGE_TECHNOLOGIES_GP/2921140968", group="aey", direction="Long", raw_direction="Long", security="AEY common equity / Long", entry="약 $2.94", horizon="12~24개월", raw_horizon="cable-equipment cycle rebound; recent sales +45%, EPS $0.14",
    title="cable-equipment cycle-value Long", verdict="tactical rerating 일부 성공 / durable thesis terminal 실패", score=5.0, process=5.5,
    conclusion="FY07 EPS $0.64→FY09 $0.30으로 약해진 가운데 최근 분기 sales +45%, EPS $0.14를 회복 신호로 봤다. 2011 high 약 $3.90은 entry 대비 약 +33% peak magnitude였지만 매도 가능·배당을 복원한 수익률은 아니다. 2024 Chapter 7은 durable franchise·asset floor가 없었음을 보여준다.",
    t0="작은 cable-equipment distributor가 cycle trough 뒤 주문 회복과 보유 inventory의 monetization으로 earnings rebound를 낼 것으로 기대됐다.", reverse="시장은 OEM/product cycle, customer capex와 inventory obsolescence 때문에 최근 한 분기 개선이 지속되지 않을 가능성을 할인했다.",
    valuation="$2.94 entry에서 과거 EPS $0.44~0.64 회복을 기대했다. peak historical earnings 대신 normalized gross margin·working-capital cash conversion으로 평가해야 했다.", actual="2011 high 약 $3.90이 관찰돼 tactical rerating은 있었다. 그러나 cable legacy가 약해지고 diversification을 반복했으며 2024-01-26 영업중단, 2024-01-31 Chapter 7 filing으로 terminal common economics는 실패했다.",
    price="2011 high/entry 단순 peak magnitude는 약 +32.7%다. 이는 실현수익률이 아니며 장기 terminal은 Chapter 7이다.", drivers="단기 수익은 cycle rebound와 낮은 기대가 만들었고 장기 손실은 product relevance와 working-capital quality 약화가 만들었다.", counterfactual="최근 분기 매출 +45%를 제거하고 FY09 EPS $0.30과 inventory haircut을 쓰면 $2.94가 충분히 쌌는가?", error="한 분기 rebound와 과거 peak EPS를 durable earnings로 사용했다.", warning="후속 매출·margin이 최근 분기 run-rate를 유지하지 못한 것이 첫 경고였고 사업전환 반복이 구조적 약화를 확인했다.", first_signal_date="2011-12-31", lessons=lessons("aey"), checklist=checklist("aey"), scorecard=scorecard("단기 부분", "부분", "cycle rerating", "common terminal 실패", "peak와 terminal 혼합"),
    scenarios=[("Bear", "cycle rebound 실패·inventory haircut", "$2 이하", "장기 현실화"), ("Base", "EPS $0.30~0.44", "$3~4", "peak 부분 실현"), ("Bull", "FY07 EPS $0.64", "큰 rerating", "지속 안 됨")],
    metrics=[("Entry", "$2.94", "rerating", "$3.90 2011 high", "+32.7% peak"), ("FY07 EPS", "$0.64", "회복 anchor", "지속 못함", "과대"), ("FY09 EPS", "$0.30", "trough", "$0.30 base", "cycle"), ("Recent quarter", "sales +45%/EPS $0.14", "run-rate", "지속성 제한", "부분"), ("Terminal", "going concern", "생존", "2024 Chapter 7", "실패")],
    timeline=[("2010-09-02", "VIC Long", "$2.94 cycle value"), ("2010", "recent sales +45%", "rebound signal"), ("2011", "high ~$3.90", "tactical upside"), ("2012", "run-rate 둔화", "first break"), ("2015", "legacy cable 압력", "asset quality 약화"), ("2019", "diversification", "원 thesis 변경"), ("2024-01-26", "operations ceased", "terminal distress"), ("2024-01-31", "Chapter 7", "common impairment")],
    claims=[
        C("recent sales +45%", "단기 성공·지속 실패", "회복분기 성장 지속.", "operator capex rebound.", "recent quarter.", "order visibility.", "다음해 둔화면 반증.", "초기 rerating 후 지속성 부족.", "peak +32.7%뿐.", "한 분기 extrapolation.", "LTM organic volume로 확인한다."),
        C("EPS $0.14 run-rate", "부분", "분기 EPS를 연환산.", "fixed-cost leverage.", "reported quarter.", "margin 정상화.", "연간 EPS가 run-rate 크게 하회하면 반증.", "durable EPS로 정착하지 못함.", "FY07 peak 회복 실패.", "seasonality·mix 미분해.", "3년 평균을 쓴다."),
        C("inventory supports value", "장기 실패", "재고가 downside 보호.", "판매 가능한 장비 monetization.", "working capital.", "SKU relevance·turns 유지.", "write-down·cash burn이면 반증.", "2024 terminal distress.", "book floor 소멸.", "재고를 cash처럼 봄.", "aging별 haircut을 적용한다."),
        C("cable capex recovery", "tactical 부분", "업황 회복이 earnings를 정상화.", "customer capex→orders.", "sales rebound.", "vendor/product share 안정.", "매출 회복에도 margin 미달이면 제한.", "단기 price rerating, 장기 legacy 약화.", "duration mismatch.", "cycle과 secular를 혼동.", "product relevance를 별도 추적한다."),
        C("$2.94 undervaluation", "부분 성공", "과거 EPS 대비 저평가.", "mean reversion.", "FY07~09 EPS.", "earnings mean 유효.", "rebound 없이 book 감소면 반증.", "high ~$3.90.", "+32.7% peak.", "peak price를 실현수익으로 오해.", "MFE와 executable return을 분리한다."),
        C("durable common value", "강한 실패", "small-cap asset value가 장기 floor.", "cash·inventory·earnings.", "balance sheet.", "burn 제한.", "Chapter 7이면 반증.", "2024 Chapter 7.", "terminal impairment.", "tactical와 franchise 혼합.", "각 horizon을 독립 판정한다."),
    ],
)


add(
    id="b8bf3367-b7c9-41b7-a379-c2b92990fb71", date="2013-01-18", author="alex981", ticker="AEY", company="ADDvantage Technologies Group", filename="analysis/ideas/2013/2013-01-18_AEY_long.md", source="", group="aey", direction="Long", raw_direction="Long", security="AEY common equity / NCAV Long", entry="$2.17", horizon="1~3년", raw_horizon="61% TBV, 79% NCAV, $4~5 fair value",
    title="NCAV·tangible-book asset Long", verdict="부분 rerating / $4~5 미달 / 장기 floor 붕괴", score=5.3, process=6.0,
    conclusion="$2.17은 TBV의 61%, NCAV의 79%였고 2014 high 약 $3.55까지 약 +63.6% peak magnitude가 있었다. 하지만 $4~5에는 못 미쳤고 2024 Chapter 7은 inventory·receivable book가 영구 floor가 아니었음을 보여준다.",
    t0="profitable cable distributor의 cash·AR·inventory에서 liabilities를 뺀 NCAV보다 낮게 거래돼 liquidation-like margin of safety가 있다고 봤다.", reverse="시장은 자산을 청산하지 않고 운영하면서 발생할 burn, inventory obsolescence와 customer/product concentration을 haircut했다.",
    valuation="$2.17 / 0.79≈$2.75 NCAV, /0.61≈$3.56 TBV. 원문 $4~5는 asset recovery 외에 earnings·multiple 개선까지 요구했다.", actual="2014 high 약 $3.55로 TBV implied value 근처까지 갔지만 $4~5 미달. 이후 asset quality와 business mix가 변했고 2024 Chapter 7.",
    price="high/entry 단순 peak magnitude 약 +63.6%. exact IRR·realized return은 확인하지 않으며 terminal common은 impaired됐다.", drivers="수익은 discount narrowing이 만들었지만 완전한 asset realization 계획이 없어 book가 계속 변했다.", counterfactual="inventory 50%, AR 15% haircut과 2년 SG&A burn을 차감하면 NCAV가 여전히 $2.17을 넘었는가?", error="ongoing company의 NCAV를 static liquidation value로 보고 burn·time·haircut을 과소평가했다.", warning="가격이 TBV 부근에서 멈추고 earnings가 asset discount를 닫지 못한 것이 첫 경고였다.", first_signal_date="2014-12-31", lessons=lessons("aey"), checklist=checklist("aey"), scorecard=scorecard("부분", "부분", "rerating 부분", "common terminal 실패", "$4~5 미달"),
    scenarios=[("Bear", "haircut+cash burn", "$2 이하", "장기 현실화"), ("Base", "NCAV ~$2.75", "$2.75~3.55", "실현"), ("Bull", "earnings+book", "$4~5", "미달")],
    metrics=[("Entry/TBV", "$2.17 / 61%", "TBV 회복", "high ~$3.55", "대체로"), ("Implied TBV", "~$3.56", "회복", "high ~$3.55", "근접"), ("Entry/NCAV", "79%", "NCAV 이상", "peak 상회", "tactical 성공"), ("Fair value", "$4~5", "$4~5", "high ~$3.55", "-11%~-29%"), ("Terminal", "asset floor", "보존", "2024 Chapter 7", "실패")],
    timeline=[("2013-01-18", "VIC Long", "61% TBV/79% NCAV"), ("2013", "asset discount 유지", "catalyst 대기"), ("2014", "high ~$3.55", "TBV convergence"), ("2014-12", "$4 미달", "first warning"), ("2016", "legacy business 약화", "book quality 하락"), ("2019", "사업 mix 변경", "원 NCAV 소멸"), ("2024-01-26", "영업중단", "floor 붕괴"), ("2024-01-31", "Chapter 7", "terminal impairment")],
    claims=[
        C("61% TBV", "tactical 성공", "TBV discount가 닫힌다.", "price/book mean reversion.", "implied TBV ~$3.56.", "book realizable.", "TBV 자체 감소면 반증.", "high ~$3.55.", "근접.", "price hit과 liquidation recovery 혼동.", "book components를 haircut한다."),
        C("79% NCAV", "tactical 성공·장기 실패", "NCAV가 floor.", "current assets cover liabilities.", "NCAV ~$2.75.", "inventory/AR 회수.", "burn으로 NCAV 하락이면 반증.", "peak는 상회, terminal은 Chapter 7.", "horizon별 상반.", "static NCAV.", "매 분기 liquidation NAV를 갱신한다."),
        C("profitable operations", "지속 실패", "영업이 book를 보존.", "positive earnings offsets burn.", "historical profits.", "product relevance 유지.", "반복 손실이면 반증.", "장기 사업 약화.", "2024 terminal.", "profit persistence 과대.", "normalized FCF를 본다."),
        C("inventory realizability", "실패", "재고가 현금 근처.", "장비 resale.", "working capital.", "turns와 SKU 수요 유지.", "aging/write-down이면 반증.", "book floor 소멸.", "회수부족.", "obsolescence 미반영.", "age bucket별 recovery를 둔다."),
        C("$4~5 fair value", "실패", "asset+earnings로 $4~5.", "book convergence+multiple.", "원문 target.", "catalyst 존재.", "3년 내 $4 미달이면 실패.", "high ~$3.55.", "최소 -11.3%.", "두 단계 rerating 과대.", "NCAV/TBV/earnings value를 분리한다."),
        C("common downside protected", "장기 강한 실패", "discount가 permanent loss 방지.", "liquidation assets.", "low P/B.", "청산 또는 profitable operation.", "Chapter 7 low recovery면 반증.", "2024 Chapter 7.", "terminal impairment.", "catalyst 없는 asset value.", "realization mechanism이 필수다."),
    ],
)


add(
    id="b406a9ec-8925-4a27-be17-a2c3bad28cd0", date="2018-03-21", author="anton613", ticker="AEY", company="ADDvantage Technologies Group", filename="analysis/ideas/2018/2018-03-21_AEY_long.md", source="https://www.valueinvestorsclub.com/idea/ADDVANTAGE_TECHNOLOGIES_GP/2652878136", group="aey", direction="Long", raw_direction="Long", security="AEY common equity / NCAV-turnaround Long", entry="$1.32", horizon="12~36개월", raw_horizon="NCAV $1.89, TBV $2.59, Triton turnaround",
    title="deep-NCAV·Triton turnaround Long", verdict="tactical peak 성공 / TBV convergence·durability 실패", score=5.6, process=6.2,
    conclusion="$1.32에서 NCAV $1.89와 TBV $2.59는 큰 할인처럼 보였고 후속 high 약 $2.20은 약 +66.7% peak magnitude였다. 하지만 TBV $2.59에는 못 갔고 2024 Chapter 7로 liquidation floor가 녹았다.",
    t0="기존 cable 자산 할인에 Triton Datacom turnaround optionality를 더했다. market cap가 current asset value보다 작아 downside가 제한된다고 봤다.", reverse="시장은 inventory·AR haircut, turnaround 추가자금과 legacy decline이 book를 소모할 가능성을 가격에 넣었다.",
    valuation="$1.89 NCAV와 $2.59 TBV가 단계별 anchor였다. 실제 청산계획이 없으면 operating burn과 자본재배치로 두 숫자는 계속 움직인다.", actual="주가는 후속 약 $2.20까지 상승해 NCAV를 넘었지만 TBV에는 미달. diversification과 사업구조 변화 후 2024 영업중단·Chapter 7.",
    price="$2.20/$1.32-1≈66.7% peak magnitude. exact realized return은 아니며 terminal floor는 실패했다.", drivers="낮은 starting price와 optionality가 tactical rerating을 만들었지만 asset quality와 cash burn이 장기 가치를 훼손했다.", counterfactual="Triton 가치를 0, inventory 50% haircut, 3년 burn을 차감해도 $1.32 아래 downside가 제한됐는가?", error="NCAV와 turnaround optionality를 더하면서 turnaround funding cost를 자산가치에서 빼지 않았다.", warning="주가가 NCAV를 넘었어도 TBV에 도달하지 못하고 underlying asset base가 축소된 것이 첫 경고였다.", first_signal_date="2019-12-31", lessons=lessons("aey"), checklist=checklist("aey"), scorecard=scorecard("tactical 부분", "NCAV 성공·TBV 실패", "turnaround 불완전", "common terminal 실패", "peak/terminal 분리") ,
    scenarios=[("Bear", "Triton 실패+asset haircut", "$1 이하", "장기 현실화"), ("Base", "NCAV $1.89", "$1.89~2.20", "실현"), ("Bull", "TBV+turnaround", "$2.59+", "미달")],
    metrics=[("Entry", "$1.32", "rerating", "$2.20 high", "+66.7% peak"), ("NCAV", "$1.89", "floor/target", "high 상회", "tactical 성공"), ("TBV", "$2.59", "convergence", "$2.20 high", "약 -15.1%"), ("Triton", "turnaround", "value creation", "durability 제한", "실패"), ("Terminal", "asset protection", "survival", "2024 Chapter 7", "실패")],
    timeline=[("2018-03-21", "VIC Long", "$1.32 deep value"), ("2018", "NCAV $1.89", "floor 주장"), ("2019", "Triton execution", "turnaround test"), ("2019-12", "TBV convergence 미달", "first warning"), ("2020", "사업전환 지속", "cash needs"), ("2022", "legacy economics 약화", "floor 감소"), ("2024-01-26", "영업중단", "terminal break"), ("2024-01-31", "Chapter 7", "common impairment")],
    claims=[
        C("NCAV $1.89", "tactical 성공", "가격이 NCAV로 수렴.", "asset discount closure.", "T0 balance sheet.", "assets recoverable.", "NCAV 하락이면 반증.", "high ~$2.20.", "+$0.31 vs NCAV.", "price와 liquidation 회수 혼동.", "NCAV의 구성품을 검증한다."),
        C("TBV $2.59", "실패", "TBV까지 회복.", "turnaround가 book earning power 복원.", "T0 TBV.", "positive ROE.", "3년 내 $2.59 미달이면 실패.", "high ~$2.20.", "-$0.39/-15.1%.", "unprofitable book에 full value.", "ROE 없는 book은 haircut한다."),
        C("Triton turnaround", "실패", "새 사업이 growth와 margin을 만든다.", "sales expansion·overhead leverage.", "acquired platform.", "integration·capital sufficient.", "cash burn 지속이면 반증.", "durable value 미확인·후속 distress.", "terminal 실패.", "optionality 비용 누락.", "funding-adjusted option으로 본다."),
        C("inventory/AR floor", "장기 실패", "current assets가 downside 방어.", "liquidation proceeds.", "balance sheet.", "collection·turns 안정.", "write-down·cessation이면 반증.", "Chapter 7.", "floor 소멸.", "gross carrying value 사용.", "recovery haircut과 time cost를 반영한다."),
        C("$1.32 margin of safety", "tactical 성공", "큰 discount가 rerating 여지.", "낮은 expectations.", "30~49% asset discounts.", "near-term solvency.", "추가자금 조달이면 훼손.", "peak +66.7%.", "실현 가능성 미확정.", "MFE를 outcome으로 봄.", "exit discipline을 사전 정의한다."),
        C("durable liquidation value", "강한 실패", "book가 장기 보존.", "자산 처분/현금화.", "NCAV/TBV.", "청산 catalyst.", "operation cessation/Chapter 7이면 반증.", "2024 발생.", "terminal impairment.", "catalyst 부재.", "asset value에는 realization mechanism이 필요하다."),
    ],
)


add(
    id="edda24f6-92b1-472f-806c-2a104759271a", date="2020-08-17", author="Ares", ticker="AEYE", company="AudioEye, Inc.", filename="analysis/ideas/2020/2020-08-17_AEYE_long.md", source="https://www.valueinvestorsclub.com/idea/AUDIOEYE_INC/8147253173", group="audioeye", direction="Long", raw_direction="Long", security="AEYE common equity / Long", entry="market cap 약 $145m", horizon="3~4년", raw_horizon="revenue ~$50m, gross margin ~75%, accessibility SaaS rerating",
    title="digital-accessibility SaaS·partner distribution Long", verdict="초기 성장·가격 강한 성공 / 3~4년 매출 forecast 미달", score=7.2, process=7.8,
    conclusion="FY2020 revenue $20.475m(+90%), year-end MRR 약 $1.9m, customers 약 32k, Q4 gross margin 73%로 메커니즘이 빠르게 확인됐고 2021-02 high $44.37를 기록했다. 그러나 2021 year-end $7.02로 round-trip했고 FY2023 revenue $31.316m은 $50m에 37.4% 미달했다. FY2025 $40.3m·78% GM은 장기 방향을 지지하지만 원 horizon은 구제하지 않는다.",
    t0="market cap 약 $145m, LTM revenue 약 $15.9m, MRR $1.6m, run-rate sales 약 7.5x였다. accessibility 규제와 partner distribution이 낮은 CAC로 subscription growth를 만들 것으로 봤다.", reverse="시장은 micro-cap execution, partner concentration, remediation labor, cash burn과 이미 높은 revenue multiple을 할인했다. 성장률이 낮아지면 duration multiple이 빠르게 압축될 수 있었다.",
    valuation="$145m / ~$19.2m MRR run-rate≈7.5x sales. 3~4년 revenue $50m·75% GM에서 SaaS multiple을 적용하려면 retention·FCF와 dilution이 따라야 했다.", actual="FY2020 revenue $20.475m, gross profit $14.514m; year-end MRR ~$1.9m, customers ~32k, Q4 GM 73%. FY2023 revenue $31.316m, FY2024 $35.2m/79% GM, FY2025 $40.3m/78% GM.",
    price="2021-02 high $44.37 뒤 2021 year-end $7.02였다. early catalyst trade는 성공했지만 long-duration hold는 큰 path risk를 보였다. exact entry share price·total return은 별도 ledger 없이는 주장하지 않는다.", drivers="초기 수익은 MRR acceleration과 scarcity multiple이, 이후 손실은 growth deceleration과 multiple compression이 만들었다. 장기에는 gross margin·revenue가 재개선됐다.", counterfactual="3~4년 revenue가 $31m에 그치고 exit multiple이 3x면 $145m entry에서 downside가 얼마나 되는가?", error="TAM·partner distribution의 초기 증거를 장기간 같은 성장률과 multiple이 유지된다는 가정으로 확장했다.", warning="2021년 price round-trip과 성장률 둔화가 첫 market/business warning이었고 FY2023 $31.316m이 $50m forecast를 확정 미달시켰다.", first_signal_date="2021-12-31", lessons=lessons("audioeye"), checklist=checklist("audioeye"), scorecard=scorecard("성공", "초기 성공·duration 혼합", "MRR/GM 성공", "common path 혼합", "3~4년 매출 미달"),
    scenarios=[("Bear", "growth 둔화·3x sales", "큰 multiple compression", "2021 round-trip"), ("Base", "$50m revenue·75% GM", "SaaS rerating", "2023 revenue 미달"), ("Bull", "partner flywheel", "high-teens growth 지속", "2025 방향만 부분")],
    metrics=[("FY2020 revenue", "LTM ~$15.9m", "빠른 성장", "$20.475m/+90%", "강한 성공"), ("YE2020 MRR", "$1.6m T0", "성장", "~$1.9m", "+18.8%"), ("Q4 2020 GM", "scale-up", "~75%", "73%", "근접"), ("FY2023 revenue", "$50m target", "$50m", "$31.316m", "-37.4%"), ("FY2025", "장기 성장", "$50m path", "$40.3m/78% GM", "지연·부분")],
    timeline=[("2020-08-17", "VIC Long", "$145m/7.5x run-rate"), ("2020-12-31", "revenue $20.475m", "+90% growth"), ("2020-12", "MRR ~$1.9m/customers ~32k", "distribution 확인"), ("2021-02", "high $44.37", "초기 price success"), ("2021-12-31", "price $7.02", "round-trip warning"), ("2023-12-31", "revenue $31.316m", "$50m miss"), ("2024-12-31", "$35.2m/79% GM", "장기 개선"), ("2025-12-31", "$40.3m/78% GM", "지연 성장")],
    claims=[
        C("MRR·partner growth", "강한 초기 성공", "MRR $1.6m이 빠르게 성장.", "partner distribution lowers CAC.", "T0 MRR.", "retention·partner economics.", "MRR 정체면 반증.", "YE2020 ~$1.9m.", "+$0.3m/+18.8% in months.", "organic/partner mix 제한.", "MRR cohort와 channel margin을 분리한다."),
        C("FY2020 growth", "강한 성공", "high growth 지속.", "subscription additions.", "LTM ~$15.9m.", "conversion and retention.", "FY20 <$18m이면 반증.", "$20.475m/+90%.", "기대 상회.", "acquisition/organic mix 주의.", "reported와 organic growth를 구분한다."),
        C("gross margin ~75%", "성공", "software scale로 75% GM.", "automation spreads delivery cost.", "SaaS model.", "manual remediation 제한.", "70% 아래 지속이면 반증.", "Q4 2020 73%, 2024 79%, 2025 78%.", "초기 -2ppt, 장기 상회.", "GM만으로 FCF 판단.", "sales/R&D 뒤 contribution을 본다."),
        C("3~4년 revenue $50m", "실패·지연", "$50m revenue.", "TAM+partner compounding.", "MRR trajectory.", "높은 growth 지속.", "FY2023 <$40m이면 반증.", "$31.316m; 2025 $40.3m.", "2023 -$18.684m/-37.4%.", "초기 growth extrapolation.", "cohort-based forecast를 쓴다."),
        C("7.5x sales justified", "path 혼합", "scarcity/growth가 multiple 지지.", "high growth lowers forward multiple.", "$145m/~$19.2m run-rate.", "growth duration·capital market.", "growth 둔화와 price collapse면 반증.", "$44.37 spike 후 $7.02 YE2021.", "큰 round-trip.", "terminal multiple sensitivity 부족.", "3x/5x/8x cases를 둔다."),
        C("accessibility secular demand", "장기 성공", "regulation·digital adoption이 category growth.", "web compliance spend.", "large underserved base.", "competitive pricing 유지.", "revenue 장기 정체면 반증.", "2025 revenue $40.3m, GM 78%.", "방향 성공·속도 미달.", "TAM을 company share로 직결.", "share·retention·CAC로 conversion을 검증한다."),
    ],
)


def idea_sources(i):
    return [S("VIC source-DB preserved original", i["source"], "Value Investors Club / source SQL", i["date"], "T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.", "원문"), *GROUP_SOURCES[i["group"]]]


def render_index():
    rows = []
    for n, i in enumerate(IDEAS, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(f"| {n} | {i['date']} | {i['ticker']} | {i['raw_direction']} | {i['direction']} | [{i['company']}]({rel}) | {i['verdict']} |")
    return "\n".join([
        "# Batch 066 — Aetna / AETC / Aether / Ampex / ADDvantage / AudioEye V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. 아이디어 1건 = canonical Markdown 1개다.",
        f"> Research as-of {ASOF}. 방향·법인·증권·horizon과 terminal corporate action을 먼저 고정했다.", "",
        "## Canonical idea files", "", "| # | 날짜 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## Entity / direction / security audit", "",
        "- Aetna 2000·2009는 raw Short지만 원문은 breakup/crisis Long이다.",
        "- Aether는 common이 아니라 6% convertible subordinated notes due 2005다. conversion보다 cash coverage·101.2% redemption이 payoff를 만들었다.",
        "- AETC·Ampex의 기존 common은 각각 재편에서 취소됐다. refinancing·IP asset의 존재를 common recovery와 혼동하지 않는다.",
        "- AEY 세 vintage는 같은 법인이지만 entry asset base·catalyst·horizon이 다른 date-specific ideas다.", "",
        "## 핵심 비교", "",
        "1. Aetna 2000은 signed breakup consideration이 실현됐지만 $134 bull SOTP를 거래성공으로 소급하지 않는다.",
        "2. Aetna 2006은 EPS $3.83 대비 $3.93로 적중했어도 17x multiple과 $65 target는 실패했다.",
        "3. Aetna 2009는 낮은 P/E의 E가 31.8% 무너졌다. 2011 target hit는 near-term thesis를 구제하지 않는다.",
        "4. AETC는 refinancing이 성공해도 FY2002 EPS -$2.55와 common cancellation을 막지 못했다.",
        "5. Aether convert는 issuer common보다 priority·maturity가 나은 security selection의 성공이다.",
        "6. Ampex의 royalty는 debt·legacy burn 뒤 common까지 도달하지 않았고 CPR은 별도 claim이다.",
        "7. AEY의 NCAV/TBV는 tactical rerating을 만들었지만 청산계획 없는 working-capital book는 2024 Chapter 7까지 녹았다.",
        "8. AudioEye는 초기 MRR·GM·price catalyst가 맞았지만 FY2023 revenue는 $50m 예상보다 37.4% 낮았다.", "",
        "## 구조화 데이터", "",
        "- data/curated/batch_066_aetna_aetc_aether_ampex_aey_aeye_deep_v7.json: 10 postmortems, 60 claims, 50 metrics, 80 timeline events와 sources.",
        "- data/curated/batch_066_source_catalog.json: raw metadata source packet이며 production glob에는 포함되지 않는다.",
        "- analysis/batch_066_aetna_aetc_aether_ampex_aey_aeye_10.md: Streamlit wrapper.", "",
    ])


def main():
    if len(IDEAS) != 10 or len({i["id"] for i in IDEAS}) != 10:
        raise ValueError("Batch 066 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) != 8:
            raise ValueError(f"{idea['id']}: six claims, five metrics and eight timeline events required")

    base.ASOF = ASOF
    base.CATALOG = CATALOG
    base.OUTPUT = OUTPUT
    base.BUSINESS = BUSINESS
    base.ENGINE = ENGINE
    base.KPI = KPI
    base.GROUP_SOURCES = GROUP_SOURCES
    base.IDEAS = IDEAS
    base.idea_sources = idea_sources

    for idea in IDEAS:
        report = base.render_report(idea).replace(
            "**B** — source SQL price-only ratios; dividends·tax 제외.",
            "**C/제한** — verified corporate action·reported high/period-end price만 사용; exact total-return ledger가 없으면 IRR·MFE를 만들지 않음.",
        )
        (ROOT / idea["filename"]).write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_066_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 066 — Aetna / AETC / Aether / Ampex / ADDvantage / AudioEye V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 066 V9 Index](batch_066_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_066_aetna_aetc_aether_ampex_aey_aeye_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 66
    payload["title"] = "Aetna / AETC / Aether / Ampex / ADDvantage / AudioEye — Denominator, Asset Floors and Security Payoff V9"
    payload["metadata_audit"] = {
        "direction_corrections": 3,
        "security_type_corrections": 1,
        "cross_batch_duplicates_removed": 0,
        "performance_rows_rejected": 10,
        "corporate_action_terminal_payoffs": 5,
        "notes": [
            "Aetna 2000·2009와 AETC raw Short를 original-text Long으로 교정.",
            "Aether를 common이 아니라 6% convertible subordinated notes due 2005로 교정.",
            "가격행이 없는 아이디어에 임의 exact return을 만들지 않고 corporate action·reported high만 제한적으로 사용.",
            "AETC·Ampex old common cancellation, Aether 101.2% redemption, AEY Chapter 7을 security payoff로 분리.",
        ],
    }
    payload["batch_lessons"] = [
        "낮은 P/E는 multiple보다 denominator stress를 먼저 계산한다.",
        "거래 고려사항과 공격적인 SOTP target을 분리한다.",
        "refinancing은 liquidity를 연장하지만 unit economics와 solvency를 고치지 않는다.",
        "같은 issuer에서도 cash-covered note와 common의 payoff는 전혀 다르다.",
        "IP royalty와 working-capital book는 debt·burn·duration 뒤 common recovery로 변환한다.",
        "NCAV/TBV는 청산 catalyst와 recovery haircut이 없으면 영구적 floor가 아니다.",
        "초기 성장과 price spike는 3~4년 revenue forecast의 증거가 아니다.",
    ]
    failures = {
        "aetna": "denominator; medical_cost_trend; multiple; timing; capital_return",
        "aetc": "refinancing_without_earning_power; resin_spread; leverage; waterfall",
        "aether": "cash_burn; subordination; coverage; redemption; conversion_option",
        "ampex": "finite_ip; legacy_burn; debt; patent_duration; waterfall",
        "aey": "static_ncav; inventory_obsolescence; no_realization_catalyst; cash_burn",
        "audioeye": "growth_duration; partner_concentration; multiple_compression; dilution",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failures[idea["group"]]
        row["success_pattern_ko"] = "security_mapping; claim_level_falsifier; quantitative_gap; terminal_payoff_separation"
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
