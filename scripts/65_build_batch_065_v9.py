#!/usr/bin/env python3
"""Build Batch 065 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
CATALOG = ROOT / "data/curated/batch_065_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_065_aer_aeri_aeromex_aes_deep_v7.json"
AER_IDS = {
    "a080516f-7836-4664-a4cd-7de23c6b7f22",
    "d4fd0257-fa37-46b8-a90a-a04e398e136a",
    "667db72f-294f-4aca-99ff-44362efd7a15",
    "99625fca-d4da-4371-b14e-d973d40149e6",
    "953a3d6e-56bb-4cbe-8817-9a2f3d2b7d33",
    "cdb4f141-bcc2-40b1-9d27-089f1093d4cd",
}

spec = importlib.util.spec_from_file_location(
    "batch64_base", ROOT / "scripts/64_build_batch_064_v9.py"
)
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "aercap": (
        "AerCap은 항공기를 OEM·sale-leaseback·portfolio 거래로 취득해 전 세계 항공사에 장기 임대하고, "
        "중고 항공기와 엔진을 매각·재임대하는 항공금융회사다. lease rent와 maintenance receipts에서 "
        "funding cost·감가상각·credit loss·관리비를 뺀 spread, 그리고 실제 매각가와 장부가의 차이가 ROE를 만든다. "
        "common은 높은 자산 이동성과 장기 계약의 혜택을 받지만 항공사 부도, 자본시장 폐쇄, 잔존가치와 관할권 회수위험을 "
        "부채 뒤에서 흡수한다."
    ),
    "aerie": (
        "Aerie Pharmaceuticals는 녹내장·고안압 치료제 Rhopressa와 복합제 Rocklatan을 개발·상업화한 안과 전문 바이오텍이었다. "
        "가치는 승인확률×시장침투×순가격에서 임상·영업조직·R&D·자금조달비용을 뺀 현금흐름과 후속 파이프라인·전략적 인수가치로 구성된다. "
        "따라서 작은 상업 TAM을 맞혀도 FDA binary와 buyer option value가 short payoff를 뒤집을 수 있다."
    ),
    "aeromex": (
        "Grupo Aeroméxico는 Mexico City hub를 중심으로 국내선과 미주·유럽·아시아 노선을 운영한 full-service airline이다. "
        "Delta와 JV 및 지분관계를 맺었지만 common의 가치는 RASM×capacity에서 fuel·CASK·aircraft rent·interest를 차감한 잔여현금이다. "
        "높은 operating·financial leverage 때문에 수요가 사라지면 brand·slot·partner의 enterprise value가 있어도 old common은 "
        "DIP·secured debt·lease claim 뒤에서 소멸할 수 있다."
    ),
    "aes": (
        "The AES Corporation은 미국·중남미 등에서 발전소, regulated utility, 재생에너지와 storage 자산을 운영한다. "
        "project debt 상당수는 non-recourse지만 parent equity에는 각 프로젝트의 배당·세금·minority·FX·parent interest를 거친 현금만 올라온다. "
        "2009 논지는 대형 건설 program의 EPS 전환, 2020 논지는 signed renewable backlog·coal exit·credit upgrade·Fluence 외부가치에 초점을 뒀다."
    ),
}

ENGINE = {
    "aercap": "lease revenue + maintenance + sale gain - interest - depreciation - impairment - opex - tax = equity earnings; retained earnings와 below-book buyback을 더해 BVPS를 추적한다.",
    "aerie": "net product revenue × gross margin - commercial SG&A - R&D - interest = cash burn/FCF; approval확률·희석·borrow·M&A consideration을 common short payoff에 적용한다.",
    "aeromex": "RASM × ASK - fuel - non-fuel CASK - aircraft rent - interest - tax = common cash flow; stress에서는 liquidity와 claim waterfall을 먼저 계산한다.",
    "aes": "project/utility operating cash - local debt service - capex - tax - minority = parent distribution; parent interest·overhead 뒤의 주당 EPS/FCF로 변환한다.",
}

KPI = {
    "aercap": "lease yield, funding cost, utilization, cash collection, gain on sale, impairments, liquidity/sources-to-uses, debt/equity, unencumbered assets, BVPS, ROE, repurchase price",
    "aerie": "FDA/label, prescription growth, net price, product revenue, gross margin, commercial SG&A, cash burn, cash runway, diluted shares, borrow cost, strategic interest",
    "aeromex": "ASK/RPK, load factor, yield/RASM, CASK ex-fuel, EBITDAR margin, net debt/EBITDAR, fleet commitments, MXN/USD, unrestricted cash, JV contribution",
    "aes": "adjusted EPS, proportional FCF, parent FCF, project distributions, recourse debt, signed backlog/COD, coal mix, FX, credit rating, Fluence ownership/value",
}


AERCAP_SOURCES = [
    S("AerCap FY2017 results", "https://www.aercap.com/investors/news-events/news/detail/206/aercap-holdings-n-v-reports-financial-results-for-full", "AerCap", "2018-02", "2017 BVPS·repurchase·leverage 검증."),
    S("AerCap FY2018 results", "https://www.aercap.com/investors/news-events/news/detail/378/aercap-holdings-n-v-reports-financial-results-for-full", "AerCap", "2019-02-14", "EPS $6.83, BVPS $62.95, liquidity $10bn, utilization 99.0%, 95% lease rents contracted 검증."),
    S("AerCap FY2019 results", "https://www.aercap.com/investors/news-events/news/detail/486/aercap-holdings-n-v-reports-record-eps-for-full-year-2019", "AerCap", "2020-02", "BVPS $72.08, 15% 증가, BBB rating과 repurchase 검증."),
    S("AerCap FY2020 results", "https://www.aercap.com/news-media/press-releases/detail/446/aercap-holdings-n-v-reports-financial-results-for-the", "AerCap", "2021-02", "BVPS $69.34, liquidity $9bn+, sources/uses 2.3x, unencumbered assets $26bn 검증."),
    S("AerCap FY2021 results", "https://www.aercap.com/investors/news-events/news/detail/420/aercap-holdings-n-v-reports-financial-results-for-the", "AerCap", "2022-03", "GECAS 이후 2021 book·fleet·funding 출발점 검증."),
    S("AerCap 2022 Form 20-F", "https://www.sec.gov/Archives/edgar/data/1378789/000137878923000006/aer-20221231.htm", "SEC / AerCap", "2023-03", "러시아 항공기·엔진, 약 $2.7bn pre-tax net charge와 2022 BVPS 검증."),
    S("AerCap FY2023 results", "https://www.aercap.com/investors/news-events/news/detail/556/aercap-holdings-n-v-reports-record-3-1-billion-2023-net", "AerCap", "2024-02", "BVPS $83.81, 2023 net income $3.1bn, Ukraine recoveries와 capital return 검증."),
]

AERIE_SOURCES = [
    S("Rhopressa FDA approval announcement", "https://www.sec.gov/Archives/edgar/data/1337553/000119312517372035/d705067dex991.htm", "SEC / Aerie Pharmaceuticals", "2017-12-18", "Rhopressa approval로 core binary short catalyst 반증."),
    S("Rocklatan FDA approval package", "https://www.accessdata.fda.gov/drugsatfda_docs/nda/2019/208259Orig1s000Approv.pdf", "U.S. FDA", "2019-03", "fixed-dose combination approval 검증."),
    S("Aerie 2021 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1337553/000133755322000013/aeri-20211231.htm", "SEC / Aerie Pharmaceuticals", "2022-02", "제품매출 $112.1m, 순손실 $74.8m, commercial economics 검증."),
    S("Alcon acquisition announcement", "https://www.alcon.com/media-release/alcon-acquire-aerie-pharmaceuticals-inc-enhancing-its-ophthalmic-pharmaceutical/", "Alcon", "2022-08-22", "$15.25 cash, 37% premium, equity value 약 $770m 검증."),
    S("Alcon completes Aerie acquisition", "https://www.alcon.com/media-release/alcon-completes-acquisition-aerie-pharmaceuticals-inc/", "Alcon", "2022-11-22", "현금 인수 종결과 terminal payoff 검증."),
]

AEROMEX_SOURCES = [
    S("Aeroméxico FY2020 results", "https://ir.aeromexico.com/static-files/ddb2e746-8f9f-4f60-b526-77fdd381515c", "Grupo Aeroméxico", "2021-02", "2019 비교치, 2020 revenue -58.5%, EBITDAR -MXN6.8bn, Chapter 11 검증."),
    S("Delta Q1 2022 Form 10-Q", "https://www.sec.gov/Archives/edgar/data/27904/000002790422000006/dal-20220331.htm", "SEC / Delta Air Lines", "2022-04", "Aeroméxico reorganization과 Delta post-emergence interest 검증."),
    S("Delta 2022 Form 10-K", "https://www.sec.gov/Archives/edgar/data/27904/000002790423000010/dal-20221231.htm", "SEC / Delta Air Lines", "2023-02", "재편 후 strategic relationship·ownership context 검증."),
    S("Aeroméxico restructuring emergence", "https://aeromexico.com/en-us/information-about-aeromexico/restructuring", "Grupo Aeroméxico", "2022-03", "Chapter 11 emergence와 재편 절차 검증."),
]

AES_SOURCES = [
    S("AES FY2010 results", "https://www.sec.gov/Archives/edgar/data/874761/000119312511048458/dex991.htm", "SEC / AES", "2011-02-28", "2010 adjusted EPS $0.94와 2011 guidance 검증."),
    S("AES FY2011 results", "https://www.sec.gov/Archives/edgar/data/874761/000119312512079761/d305830dex991.htm", "SEC / AES", "2012-02", "2011 adjusted EPS $1.04와 cash-flow outcome 검증."),
    S("S&P upgrades AES to BBB-", "https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/11723943", "S&P Global Ratings", "2020-11-02", "두 번째 investment-grade rating catalyst 검증."),
    S("AES FY2020 results", "https://www.sec.gov/Archives/edgar/data/874761/000087476121000017/q42020earningsreleaseexs.htm", "SEC / AES", "2021-02", "adjusted EPS $1.44, backlog 6.9GW, pro-forma coal 25% 검증."),
    S("AES 2022 Annual Report", "https://www.aes.com/sites/aesvault.com/files/2023-05/2022%20Annual%20Report.pdf", "AES", "2023-02", "2022 adjusted EPS $1.67과 transformation 진행 검증."),
    S("Fluence IPO pricing", "https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-announces-pricing-initial-public-offering", "Fluence Energy", "2021-10-27", "31m shares at $28 IPO로 외부 valuation 형성 검증."),
]

GROUP_SOURCES = {
    "aercap": AERCAP_SOURCES,
    "aerie": AERIE_SOURCES,
    "aeromex": AEROMEX_SOURCES,
    "aes": AES_SOURCES,
}


IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


def common_lessons(group):
    shared = {
        "aercap": [
            "BVPS 성장과 terminal P/B rerating은 서로 다른 예측이다.",
            "book는 실제 aircraft sale gain·impairment·cash collection으로 검증한다.",
            "liquidity는 12~24개월 maturities와 purchase commitments를 함께 놓고 본다.",
            "계약된 rent와 실제 현금회수는 같지 않다.",
            "delayed recovery를 원래 horizon의 성공으로 소급하지 않는다.",
        ],
        "aerie": [
            "작은 TAM을 맞혀도 전략적 buyer가 option value에 premium을 지불하면 biotech short는 실패할 수 있다.",
            "FDA binary, borrow cost와 M&A tail을 별도 payoff로 모델링한다.",
            "매출과 owner earnings 사이의 commercial fixed cost를 명시한다.",
            "제품 실패 확률과 회사가치 하락 확률을 동일시하지 않는다.",
            "terminal cash consideration이 있으면 정확한 short ledger의 기준점으로 사용한다.",
        ],
        "aeromex": [
            "좋은 network와 strategic partner는 회사를 살려도 기존 common을 살린다는 뜻은 아니다.",
            "airline은 EV/EBITDAR보다 liquidity와 fixed-claim waterfall을 먼저 본다.",
            "과거 strategic 매입가는 bankruptcy recovery floor가 아니다.",
            "JV synergy는 실제 margin·parent cash로 검증한다.",
            "zero-revenue stress와 FX·lease claim을 반드시 넣는다.",
        ],
        "aes": [
            "project MW를 parent EPS로 바로 번역하지 말고 leakage bridge를 만든다.",
            "non-recourse debt는 solvency를 보호할 수 있지만 주당수익 성장을 보장하지 않는다.",
            "transformation은 narrative보다 관찰 가능한 milestone으로 평가한다.",
            "backlog는 signed MW·ownership·COD·margin을 함께 기록한다.",
            "earnings denominator와 exit multiple을 분리한다.",
        ],
    }
    return shared[group]


def scorecard(business, valuation, catalyst, security, timing):
    return [
        ("Business thesis", business),
        ("Valuation thesis", valuation),
        ("Catalyst thesis", catalyst),
        ("Security payoff", security),
        ("Timing / path", timing),
    ]


add(
    id="a080516f-7836-4664-a4cd-7de23c6b7f22", date="2015-12-28", author="nassau799",
    ticker="AER", company="AerCap Holdings N.V.", filename="analysis/ideas/2015/2015-12-28_AER_long.md",
    source="", group="aercap", direction="Long", raw_direction="Long", security="AER common equity / Long",
    entry="약 $43~44", horizon="2018", raw_horizon="2018 BVPS ~$60, EPS $7~8, 1.2x P/B target ~$72",
    title="ILFC integration·BVPS compounding·rerating Long",
    verdict="사업·BVPS 예측 성공 / 3년 stock thesis 실패", score=7.6, process=7.2,
    conclusion="ILFC 통합과 per-share book compounding은 정확했다. 2018 BVPS $62.95는 ~$60 예상보다 높았고 EPS $6.83은 $7~8 하단에 근접했다. 그러나 3년 price-only return은 -11.0%였다. denominator 적중과 multiple 적중을 하나로 묶은 것이 stock thesis를 실패시켰다.",
    t0="2015 Q3 BVPS 약 $40.80, mid-$40s 주가였다. appraiser market value는 carrying value보다 약 $3.3bn 높았고 AIG overhang 해소·ILFC integration·deleveraging·below-book repurchase가 2018 BVPS를 약 $60으로 올릴 것으로 봤다.",
    reverse="시장은 ILFC integration과 aircraft residual values를 불신하고 lessor에 구조적 discount를 요구했다. 원문은 operational de-risking이 곧 1.2x P/B로 이어진다고 봤지만, market trust와 book growth는 별도 상태변수였다.",
    valuation="2018 BVPS ~$60 × 1.2x = ~$72. mid-$40s entry에서 book growth와 multiple expansion을 동시에 요구했다. 실제 BVPS는 넘었으나 exit P/B가 목표에 미달했다.",
    actual="2018 net income $1.016bn, diluted EPS $6.83, BVPS $62.95였다. 2019 BVPS는 $72.08까지 늘었지만 lessor discount가 지속됐고 2020 COVID가 tail-risk premium을 재확인했다.",
    price="SQL price-only: 1Y -2.7%, 2Y +21.4%, 3Y -11.0%, 5Y +1.8%. 배당·세금 제외. stated 3년 horizon은 실패다.",
    drivers="retained earnings와 book 이하 buyback은 내재가치를 높였지만, 항공금융의 funding·residual·airline-credit tail discount가 multiple을 눌렀다. 수익률의 병목은 EPS가 아니라 exit P/B였다.",
    counterfactual="2018 BVPS를 정확히 맞혀도 exit P/B를 0.7~0.8x로 두었다면 기대수익이 충분했는가?",
    error="appraised value와 earnings forecast가 맞으면 시장이 1.2x book을 줄 것이라는 valuation-regime 오류다.",
    warning="2018 operating numbers가 적중했는데도 P/B가 확대되지 않은 것이 최초의 결정적 경고였다.", first_signal_date="2018-12-31",
    lessons=common_lessons("aercap"), checklist=["BVPS bridge와 P/B bridge 분리", "sale gain/impairment 검증", "buyback 평균가격", "liquidity runway", "tail-risk premium의 역사적 범위"],
    scorecard=scorecard("강한 성공", "실패", "통합·deleveraging 성공", "3Y 실패", "stated horizon 실패"),
    scenarios=[("Bear", "book discount 지속", "BVPS 성장에도 낮은 return", "실제 stock path에 근접"), ("Base", "$60 × 1.0x", "$60 안팎", "business는 적중"), ("Bull", "$60 × 1.2x", "~$72", "multiple 실패")],
    metrics=[("2018 BVPS", "$40.80 출발", "~$60", "$62.95", "강한 성공"), ("2018 diluted EPS", "통합 후 성장", "$7~8", "$6.83", "대체로 성공"), ("2018 liquidity", "deleveraging 필요", "충분", "$10.0bn", "성공"), ("2018 utilization", "높은 가동", "안정", "99.0%", "성공"), ("3Y price-only", "높은 teens IRR", "상승", "-11.0%", "실패")],
    timeline=[("2015-12-28", "VIC Long", "BVPS+rerating thesis"), ("2016", "ILFC integration 진행", "operating risk 감소"), ("2017", "BVPS $57.20", "book compounding 확인"), ("2018-12-31", "BVPS $62.95", "핵심 forecast 적중"), ("2018", "EPS $6.83", "범위 하단 근접"), ("2019", "BVPS $72.08", "내재가치 추가 증가"), ("2018-12-28", "3Y return -11.0%", "stock thesis 실패"), ("2020", "COVID shock", "discount 원인 재부각")],
    claims=[
        C("2018 BVPS ~$60", "강한 성공", "ILFC 통합·retention·buyback으로 BVPS가 약 $60이 된다.", "retained earnings와 book 이하 환매가 분모를 줄인다.", "2015 Q3 BVPS ~$40.80.", "impairment가 작고 capital return 여력이 있다.", "2018 BVPS가 $55 아래면 반증.", "실제 $62.95.", "+$2.95 / +4.9%.", "book quality와 multiple을 혼합했다.", "BVPS 자체와 market multiple을 따로 점수화한다."),
        C("2018 EPS $7~8", "대체로 성공", "integration·funding synergy로 $7~8 EPS.", "spread와 비용 절감이 주당이익을 높인다.", "ILFC 규모·synergy.", "lease spread·credit cost가 안정적이다.", "$6.5 미만이면 반증.", "실제 $6.83.", "하단 $7 대비 -2.4%.", "point range의 구성요소를 덜 분해했다.", "lease spread·sale gain·share count로 EPS bridge를 만든다."),
        C("deleveraging·funding 개선", "성공", "ILFC 이후 leverage를 낮추고 IG funding을 강화한다.", "retained cash와 asset sales가 funding risk를 낮춘다.", "통합 직후 높은 leverage.", "capital markets가 열려 있고 큰 impairment가 없다.", "liquidity 부족·secured mix 급증이면 반증.", "2018 liquidity $10bn, funding profile 개선.", "solvency issue 없음.", "rating과 equity rerating을 동일시했다.", "credit de-risking과 equity multiple은 별도다."),
        C("aircraft market value > book", "방향 성공", "appraised premium과 sale gain이 book의 보수성을 검증한다.", "실제 매각가격이 장부가 이상이면 hidden reserve가 확인된다.", "appraisal +$3.3bn.", "sale market가 정상 작동한다.", "반복 loss-on-sale이면 반증.", "평시 sale gains가 방향을 지지했다.", "exact appraisal 회수는 제한.", "appraisal을 현금 catalyst로 보았다.", "appraisal보다 실제 sale margin을 우선한다."),
        C("below-book buyback accretion", "성공", "할인된 자사주 매입이 BVPS를 가속한다.", "book보다 낮은 가격에 분모를 줄인다.", "AIG stake·repurchase capacity.", "stressed book가 과대계상되지 않았다.", "impairment가 accretion을 상쇄하면 반증.", "BVPS가 2017~19 빠르게 증가.", "2019 $72.08.", "arithmetic accretion만 강조했다.", "liquidity buffer 뒤의 excess capital만 환매한다."),
        C("1.2x P/B rerating", "실패", "operating 정상화로 1.2x book을 받는다.", "risk perception 하락이 multiple을 확장한다.", "명시적 $72 target.", "lessor discount가 일시적이다.", "3Y 주가가 BVPS 성장을 못 따라가면 반증.", "3Y -11.0%.", "방향 반대.", "normal multiple을 상수로 가정했다.", "terminal P/B에 구조적 tail premium을 반영한다."),
    ],
)

add(
    id="d4fd0257-fa37-46b8-a90a-a04e398e136a", date="2017-07-14", author="MarAzul",
    ticker="AER", company="AerCap Holdings N.V.", filename="analysis/ideas/2017/2017-07-14_AER_long.md",
    source="https://www.valueinvestorsclub.com/idea/AERCAP_HOLDINGS_NV/3404047623", group="aercap",
    direction="Long", raw_direction="Long", security="AER common equity / Long", entry="mid-$40s",
    horizon="3~5년", raw_horizon="0.9x accounting / 0.7x appraised book, buyback·takeover optionality",
    title="deleveraging·below-book buyback Long", verdict="메커니즘 성공 / COVID 포함 가격경로 혼합",
    score=7.8, process=6.8,
    conclusion="deleveraging과 below-book buyback은 강하게 작동해 BVPS가 2017 $57.20에서 2019 $72.08로 늘었다. 그러나 sustained 1x+ rerating은 없었고 COVID로 3Y -38.0%, 5Y -17.4%였다. per-share compounding과 투자자의 holding-period return이 분리됐다.",
    t0="ILFC 이후 leverage는 약 3.7x에서 2.7x 방향으로 낮아졌고, share count는 2014 약 215m에서 2017 Q1 약 176m으로 줄었다. 주가는 accounting BV의 약 0.9x, appraised BV의 약 0.7x였다.",
    reverse="시장은 stated book가 항공 cycle에서 손상되거나, lessor discount가 구조적이며, aggressive buyback이 liquidity를 약화시킬 가능성을 반영했다.",
    valuation="low-teens ROE와 0.9x 이하 buyback이 BVPS를 늘리고 1x+ book에 수렴하는 구조였다. takeover는 보조 option이었지 base payoff가 아니어야 했다.",
    actual="2017에 19.2m주를 평균 $46.37에 환매했고 BVPS는 $57.20, 2018 $62.95, 2019 $72.08로 늘었다. 2020 COVID가 airline-credit와 asset-risk를 동시에 재가격화했다.",
    price="SQL price-only: 1Y +14.2%, 2Y +5.0%, 3Y -38.0%, 5Y -17.4%. COVID path를 포함한다.",
    drivers="buyback accretion은 내재가치를 키웠지만 market discount와 tail event가 그 전달시점을 지배했다. takeover optionality는 현실화되지 않았다.",
    counterfactual="P/B가 끝까지 0.7~0.8x에 머물고 3년에 한 번 큰 stress가 온다는 가정에서도 IRR이 충분했는가?",
    error="valuation gap의 closing time을 과신하고 tail premium의 지속성을 낮게 봤다.",
    warning="2019 BVPS $72.08에도 sustained premium이 형성되지 않은 점.", first_signal_date="2019-12-31",
    lessons=common_lessons("aercap"), checklist=["ROE와 buyback accretion 분리", "repurchase price/book", "stress liquidity", "covenant headroom", "takeover는 option으로만"],
    scorecard=scorecard("강한 성공", "불완전", "buyback 성공", "3Y·5Y 실패", "COVID path 실패"),
    scenarios=[("Bear", "book 손상·funding stress", "discount 확대", "COVID에 현실화"), ("Base", "ROE+buyback", "BVPS compounding", "강한 성공"), ("Bull", "1x+ book/takeover", "큰 rerating", "미실현")],
    metrics=[("T0 BVPS", "~$51.20", "증가", "2017 $57.20", "성공"), ("2017 repurchase", "할인 환매", "대규모", "19.2m주 @$46.37", "강한 성공"), ("2019 BVPS", "$51.20 출발", "복리성장", "$72.08", "강한 성공"), ("3Y price-only", "rerating", "상승", "-38.0%", "실패"), ("5Y price-only", "compounding", "상승", "-17.4%", "실패")],
    timeline=[("2017-07-14", "VIC Long", "buyback Long"), ("2017-12-31", "BVPS $57.20", "분모 accretion"), ("2017", "19.2m주 환매", "평균 $46.37"), ("2018", "BVPS $62.95", "mechanism 지속"), ("2019", "BVPS $72.08", "intrinsic growth"), ("2020-03", "COVID grounding", "tail risk 현실화"), ("2020-07", "3Y -38.0%", "horizon 실패"), ("2022-07", "5Y -17.4%", "multiple/path 실패")],
    claims=[
        C("deleveraging", "성공", "ILFC 이후 leverage를 정상화한다.", "retained earnings·sales가 debt/equity를 낮춘다.", "3.7x→2.7x 방향.", "asset values가 안정적이다.", "leverage 상승·funding 폐쇄면 반증.", "평시 profile 개선.", "solvency 유지.", "deleveraging을 rerating과 동일시.", "credit와 equity multiple 분리."),
        C("below-book buyback", "강한 성공", "할인 환매가 BVPS를 가속한다.", "분모를 book 이하에서 줄인다.", "큰 discount·cash generation.", "book가 보수적이다.", "repurchase 후 liquidity 약화면 반증.", "2017 19.2m주 @$46.37.", "BVPS $57.20.", "tail buffer를 덜 봄.", "buyback 전 stress capital을 차감."),
        C("BVPS compounding", "강한 성공", "low-teens ROE+buyback으로 per-share book 성장.", "retention과 denominator 감소.", "T0 ~$51.20.", "impairment가 제한적이다.", "2019 $65 미만이면 반증.", "2019 $72.08.", "예상 이상.", "BVPS를 주가와 혼동.", "book와 price를 별도 시계열로."),
        C("aircraft sales validate book", "성공 방향", "book 이상 매각이 residual value를 증명한다.", "market clearing price가 장부가를 검증.", "historical sale gains.", "cycle 내 거래 유동성.", "loss-on-sale 반복이면 반증.", "평시 gains 지속.", "exact vintage bridge 제한.", "평시 sale만 봄.", "stress sale haircut도 기록."),
        C("P/B convergence", "부분 실패", "0.9x/0.7x discount가 닫힌다.", "risk premium 하락.", "IG·deleveraging.", "discount가 일시적이다.", "BVPS 성장에도 주가 정체면 반증.", "지속적 1x+ 미실현.", "3Y -38.0%.", "closing time 과신.", "multiple mean reversion에 catalyst 필요."),
        C("takeover optionality", "미실현", "scale platform이 인수대상이 될 수 있다.", "buyer synergy가 premium을 만든다.", "world-scale fleet.", "규제·funding·buyer appetite.", "horizon 내 bid 부재면 base에서 제거.", "인수 없음.", "0.", "option을 valuation support로 사용.", "M&A는 확률가중 별도."),
    ],
)

add(
    id="667db72f-294f-4aca-99ff-44362efd7a15", date="2018-06-21", author="Seastreak",
    ticker="AER", company="AerCap Holdings N.V.", filename="analysis/ideas/2018/2018-06-21_AER_long.md",
    source="", group="aercap", direction="Long", raw_direction="Long", security="AER common equity / Long",
    entry="약 $54", horizon="2020", raw_horizon="2020 BVPS $80~85, 1.0~1.2x book",
    title="contracted-rent·0.8x-book Long", verdict="2020 horizon 실패 / franchise resilience 후행 확인",
    score=5.2, process=5.5,
    conclusion="2019까지 BVPS $72.08로 경로는 좋았지만 COVID로 2020 BVPS는 $69.34, 2Y price-only -41.6%였다. 95% contracted rent는 평시 visibility였지 counterparty solvency와 asset impairment를 제거하는 보증이 아니었다.",
    t0="약 0.8x 2018E book, 8.5x reported earnings. lease rents의 약 95%가 2020까지 계약됐고 젊은 fleet·buyback·sale gains를 근거로 2020 BVPS $80~85를 예상했다.",
    reverse="시장은 lessor book가 airline cycle과 funding shock에 취약하다고 봤다. 원문은 contract coverage를 현금회수 확실성과 가깝게 해석했다.",
    valuation="$80~85 BVPS × 1.0x면 17~19% 연환산, 1.2x면 $96~102 수준이었다. book와 multiple 모두 정상 항공 cycle에 의존했다.",
    actual="2018 BVPS $62.95, 2019 $72.08로 진행됐지만 2020 $69.34로 후퇴했다. 회사는 $9bn+ liquidity와 2.3x sources/uses로 생존했으나 horizon forecast는 깨졌다.",
    price="SQL price-only: 1Y -7.5%, 2Y -41.6%, 3Y +1.9%. 후행 회복을 2020 target 성공으로 소급하지 않는다.",
    drivers="counterparty default·rent deferral·impairment·capital-market shock가 동시에 발생해 contracted-rent protection을 압도했다.",
    counterfactual="계약 상대가 동시에 deferral 또는 파산할 때 cash collection과 book가 얼마나 훼손되는가?",
    error="contract를 현금과 동일시하고 global grounding의 상관된 tail을 누락했다.",
    warning="2020-03 airline grounding과 deferral 요청이 계약가치의 첫 결정적 반증이었다.", first_signal_date="2020-03-31",
    lessons=common_lessons("aercap"), checklist=["contracted vs collected rent", "airline concentration", "10/20/30% book haircut", "12~24m sources/uses", "horizon 고정"],
    scorecard=scorecard("평시 성공", "실패", "buyback 성공", "2Y 실패", "2020 실패"),
    scenarios=[("Bear", "defaults·impairment", "book·multiple 동시 하락", "COVID 현실화"), ("Base", "ROE+buyback", "$80~85 book", "미달"), ("Bull", "1.2x book", "$96~102", "실패")],
    metrics=[("Entry P/B", "~0.8x", "정상화", "discount 확대", "실패"), ("2019 BVPS", "$60대 출발", "target 접근", "$72.08", "성공"), ("2020 BVPS", "$80~85", "$80~85", "$69.34", "실패"), ("2020 liquidity", "계약 보호", "충분", "$9bn+ / 2.3x", "생존 성공"), ("2Y price-only", "17~29% CAGR", "강한 상승", "-41.6%", "강한 실패")],
    timeline=[("2018-06-21", "VIC Long", "contracted-rent thesis"), ("2018", "BVPS $62.95", "경로 진행"), ("2019", "BVPS $72.08", "target 접근"), ("2020-03", "global grounding", "tail 현실화"), ("2020", "rent deferrals·impairments", "cash certainty 약화"), ("2020", "liquidity $9bn+", "solvency 유지"), ("2020-06", "2Y -41.6%", "horizon 실패"), ("2021-06", "3Y +1.9%", "후행 회복 제한")],
    claims=[
        C("contracted rent visibility", "평시 성공·stress 제한", "95% 계약이 earnings를 보호한다.", "장기 lease가 revenue를 고정한다.", "2020까지 95%.", "airlines가 계약을 이행한다.", "deferral/default 급증이면 반증.", "COVID에 collection certainty 약화.", "계약≠현금.", "counterparty 상관을 누락.", "contract와 collected cash를 분리."),
        C("2020 BVPS $80~85", "실패", "ROE+buyback으로 target book.", "retention·분모감소.", "2019까지 $72.08.", "대규모 impairment 없음.", "$75 미만이면 반증.", "실제 $69.34.", "-$10.66~-15.66.", "tail distribution 과소평가.", "book stress를 명시."),
        C("below-book buyback", "평시 성공", "0.8x book에서 환매.", "per-share accretion.", "2015 이후 대규모 환매.", "liquidity 여유.", "stress에서 중단되면 catalyst 지연.", "평시 BVPS 증가, 위기엔 방어 우선.", "시점 지연.", "환매를 연속으로 가정.", "stress capital 뒤에 환매."),
        C("sale gains validate assets", "부분 성공", "book 이상의 sales.", "시장가 검증.", "historical premium.", "거래시장 유동성.", "stress sale loss면 반증.", "평시 지지, 위기 impairments.", "regime 차이.", "평시 자료 외삽.", "stress bid를 따로 본다."),
        C("1.0~1.2x book", "실패", "quality platform rerating.", "risk discount 축소.", "young fleet.", "cycle 정상.", "2Y negative면 반증.", "2Y -41.6%.", "방향 반대.", "normal multiple 과신.", "multiple은 tail premium 함수."),
        C("tail downside 제한", "실패", "young fleet·leases가 큰 downside를 막는다.", "재임대성과 residual value.", "평균기령·term.", "global grounding이 없다.", "simultaneous airline stress면 반증.", "COVID로 동시충격.", "BVPS -3.8%, stock -41.6%.", "상관 tail 누락.", "portfolio diversification이 systemic risk를 없애지 않는다."),
    ],
)

add(
    id="99625fca-d4da-4371-b14e-d973d40149e6", date="2019-02-06", author="rickey824",
    ticker="AER", company="AerCap Holdings N.V.", filename="analysis/ideas/2019/2019-02-06_AER_long.md",
    source="https://www.valueinvestorsclub.com/idea/AERCAP_HOLDINGS_NV/0237827691", group="aercap",
    direction="Long", raw_direction="Long", security="AER common equity / Long", entry="약 $46",
    horizon="1~3년", raw_horizon="6.9x EPS / 0.77x book, liquidity·covenant falsifier",
    title="liquidity-fear aircraft-lessor Long", verdict="강한 process 성공 / volatile price path",
    score=8.8, process=8.8,
    conclusion="원문은 cheap P/B보다 run-on-the-bank 가능성을 먼저 검증했다. 약 $11bn liquidity와 NTM $10.1bn uses, 추가 operating cash, covenant headroom은 2020 COVID에서도 solvency를 지켰다. 2Y -5.4%였지만 3Y +36.4%로 회복했다.",
    t0="약 952 owned·105 managed aircraft, 평균기령 6.6년, 잔여 lease 7.1년. available liquidity 약 $11bn과 NTM debt maturities+aircraft purchases 약 $10.1bn을 비교하고 operating CF 약 $3.1bn을 추가했다.",
    reverse="시장은 자본시장 폐쇄 시 maturity와 purchase commitments를 못 버틸 수 있다고 봤다. 원문은 debt/equity 2.7x vs covenant 3.75x, coverage 3.6x vs 2x, unencumbered assets 148% vs 135%를 반증표로 만들었다.",
    valuation="0.77x book·6.9x EPS가 liquidity reality보다 과도한 insolvency discount라는 논지였다. aggressive target보다 survival+continued compounding에 payoff가 있었다.",
    actual="2019 BVPS $72.08과 BBB rating, 2020 BVPS $69.34·liquidity $9bn+·sources/uses 2.3x가 stress survivability를 확인했다.",
    price="SQL price-only: 1Y +26.9%, 2Y -5.4%, 3Y +36.4%. stock path는 volatile했지만 solvency falsifier는 통과했다.",
    drivers="liquidity·covenant·unencumbered asset headroom이 forced deleveraging과 dilution을 막았고, book 손상이 주가 낙폭보다 작아 회복의 기반이 됐다.",
    counterfactual="capital markets가 24개월 닫히고 rent cash가 절반으로 줄어도 sources가 uses를 덮는가?",
    error="빠른 rerating은 과신했지만, 핵심 process는 tail event에서도 유효했다.",
    warning="2020-03 price collapse는 valuation 반증이 아니라 liquidity model을 재실행해야 하는 신호였다.", first_signal_date="2020-03-31",
    lessons=common_lessons("aercap"), checklist=["NTM maturities+commitments", "unrestricted liquidity", "covenant absolute headroom", "unencumbered assets", "cash collection stress"],
    scorecard=scorecard("성공", "혼합", "liquidity 검증", "3Y 성공", "2Y 변동"),
    scenarios=[("Bear", "funding closure+shortfall", "dilution/distress", "미발생"), ("Base", "book compounding", "rerating", "2019·2021 확인"), ("Stress", "airline crisis", "book 손상", "COVID 생존")],
    metrics=[("Available liquidity", "~$11bn", "NTM uses 커버", "충분", "성공"), ("NTM uses", "~$10.1bn", "liquidity 이하", "operating CF 추가", "성공"), ("Covenant D/E", "2.7x vs 3.75x", "headroom", "유지", "성공"), ("2020 BVPS", "$72.08 전년", "resilience", "$69.34", "성공"), ("3Y price-only", "rerating", "상승", "+36.4%", "성공")],
    timeline=[("2019-02-06", "VIC Long", "liquidity falsifier"), ("2019", "record EPS·BVPS $72.08", "base 성공"), ("2019", "S&P BBB", "funding 개선"), ("2020-03", "COVID collapse", "extreme test"), ("2020", "liquidity $9bn+", "runway 유지"), ("2020", "BVPS $69.34", "book 손상 제한"), ("2021-02", "2Y -5.4%", "가격 변동"), ("2022-02", "3Y +36.4%", "후행 회복")],
    claims=[
        C("liquidity coverage", "강한 성공", "$11bn sources가 $10.1bn uses를 덮는다.", "현금·facilities·OCF가 maturities를 충당.", "숫자 sources/uses.", "시설 가용·OCF 유지.", "coverage <1x면 반증.", "COVID에도 $9bn+, 2.3x.", "극단 stress 통과.", "committed/available 구분 제한.", "sources quality를 분류."),
        C("covenant headroom", "성공", "D/E·coverage·unencumbered tests 여유.", "breach와 forced action 방지.", "2.7/3.75x 등.", "definitions 안정.", "headroom 급감이면 반증.", "breach 없이 생존.", "성공.", "covenant cure를 덜 모델링.", "각 covenant 식을 재계산."),
        C("young fleet durability", "성공", "젊은 fleet이 residual downside를 낮춘다.", "수요 회복 시 재임대 용이.", "6.6년·7.1년 term.", "기종 obsolescence 제한.", "큰 impairment면 반증.", "BVPS 감소 약 4%.", "주가보다 작음.", "systemic grounding은 누락.", "asset quality와 macro tail 분리."),
        C("ROE/BVPS compounding", "성공", "low-double-digit ROE가 book를 키운다.", "spread·sale·buyback.", "0.77x book.", "credit losses 제한.", "BVPS 구조하락이면 반증.", "2019 $72.08.", "+15%.", "평시 결과에 의존.", "stress-adjusted ROE 사용."),
        C("below-book buyback", "성공", "환매로 per-share value 증가.", "분모 감소.", "discount·cash.", "liquidity 우선순위 유지.", "funding 부족 중 환매면 반증.", "평시 accretive, 위기엔 유동성 우선.", "방향 성공.", "continuity 과신.", "repurchase는 residual cash."),
        C("rapid rerating", "혼합", "insolvency discount가 빠르게 닫힌다.", "survival 확인.", "6.9x/0.77x.", "시장 인식 개선.", "2Y 정체면 반증.", "1Y +26.9%, 2Y -5.4%, 3Y +36.4%.", "path 의존.", "horizon 단순화.", "기간별 결과를 따로 기록."),
    ],
)

add(
    id="953a3d6e-56bb-4cbe-8817-9a2f3d2b7d33", date="2020-08-17", author="StaminaVIC",
    ticker="AER", company="AerCap Holdings N.V.", filename="analysis/ideas/2020/2020-08-17_AER_long.md",
    source="https://www.valueinvestorsclub.com/idea/AERCAP_HOLDINGS_NV/6190944255", group="aercap",
    direction="Long", raw_direction="Long", security="AER common equity / Long", entry="약 $30.6",
    horizon="1~2년", raw_horizon="~0.4x book, normalized fair value $60~75",
    title="COVID implied-impairment Long", verdict="매우 강한 성공 — crisis implied loss 과도",
    score=9.8, process=9.8,
    conclusion="약 0.4x book 가격은 40~50% 영구손상을 요구했지만 2020 BVPS는 $72.08에서 $69.34로 약 4%만 감소했다. liquidity가 유지되며 1Y +76.7%, 2Y +60.3%를 기록했다.",
    t0="900+ aircraft, 평균기령 약 6.2년, 잔여 lease 7년+, contracted rent 약 $40bn. 여행 붕괴에도 order commitments를 줄이고 debt financing을 확보했다. 과거 asset sales는 평균 약 1.3x carrying value라는 원문 근거가 있었다.",
    reverse="시장은 rent deferral·airline bankruptcy·fleet impairment가 equity book의 절반가량을 영구 파괴할 가능성을 가격에 넣었다.",
    valuation="Price ~$30.6 / book ~$70 ≈ 0.4x. 정상 EPS를 맞히지 않아도 book 손상이 40~50%보다 작으면 payoff가 컸다. $60~75는 book largely intact 시나리오였다.",
    actual="2020 BVPS $69.34, liquidity $9bn+, sources/uses 2.3x, unencumbered assets $26bn이었다. 영구 book 손상은 시장 암시치보다 훨씬 작았다.",
    price="SQL price-only: 1M -6.1%, 3M +28.5%, 6M +42.3%, 1Y +76.7%, 2Y +60.3%. crisis rerating이 빠르게 실현됐다.",
    drivers="entry discount가 0.8x가 아니라 0.4x라서 recovery timing의 정밀도보다 survival과 impairment ceiling이 중요했다.",
    counterfactual="book를 10/20/30/50% haircut했을 때 현재 가격보다 downside와 upside가 어떻게 비대칭인가?",
    error="원문도 recovery timing 불확실성을 인정했고 치명적 오류는 제한적이었다. 다만 exact sale history의 cycle adjustment는 필요했다.",
    warning="2020 liquidity coverage가 1x 아래로 내려가거나 BVPS가 30% 이상 훼손되면 즉시 반증.", first_signal_date="2020-12-31",
    lessons=common_lessons("aercap"), checklist=["implied book haircut", "liquidity duration", "order 취소·연기", "collection rate", "기종별 residual"],
    scorecard=scorecard("강한 성공", "매우 강한 성공", "liquidity 성공", "1Y·2Y 성공", "빠른 성공"),
    scenarios=[("Extreme bear", "50%+ book 손상", "$30 이하", "미발생"), ("Base", "moderate impairment", "$50~60", "현실화"), ("Normalized", "book intact", "$60~75", "1Y 방향 적중")],
    metrics=[("Entry price", "$30.6", "mispricing", "저점권", "성공"), ("Entry P/B", "~0.4x", "정상화", "book 유지", "강한 성공"), ("2020 BVPS", "2019 $72.08", "제한 손상", "$69.34", "강한 성공"), ("Liquidity coverage", "장기 stress", ">1x", "$9bn+ / 2.3x", "강한 성공"), ("1Y price-only", "$60~75 방향", "큰 상승", "+76.7%", "강한 성공")],
    timeline=[("2020-03", "global grounding", "위기 발생"), ("2020-08-17", "VIC Long", "0.4x book"), ("2020 H2", "commitments 축소·financing", "runway 확대"), ("2020-12", "liquidity $9bn+", "2.3x coverage"), ("2020-12", "BVPS $69.34", "손상 제한"), ("2021-02", "6M +42.3%", "rerating 진행"), ("2021-08", "1Y +76.7%", "강한 성공"), ("2022-08", "2Y +60.3%", "지속 성공")],
    claims=[
        C("implied impairment 과도", "강한 성공", "0.4x book가 과도한 영구손상을 반영.", "실제 book 손상이 작으면 rerating.", "price/book gap.", "reported book quality.", "BVPS -30% 이상이면 반증.", "약 -4%.", "시장 암시보다 훨씬 작음.", "accounting book를 완전 현금가치로 볼 위험.", "haircut ladder 사용."),
        C("liquidity survives", "강한 성공", "prolonged downturn을 버틴다.", "financing·commitment cuts.", "capital access.", "시장 접근 유지.", "sources/uses <1x면 반증.", "$9bn+·2.3x.", "큰 buffer.", "facility quality 상세 제한.", "liquidity source별 haircut."),
        C("young fleet protects value", "성공", "젊은 기종은 recovery 수요가 높다.", "fuel efficiency·재임대성.", "6.2년 age.", "항공수요 정상화.", "older/obsolete impairment면 반증.", "book damage 제한.", "방향 성공.", "systemic risk는 남음.", "기종별 exposure."),
        C("order flexibility", "성공", "future capex를 줄여 현금을 보존.", "취소·연기·financing.", "약 $5bn commitments 조정.", "OEM 협상 가능.", "uses 고정이면 반증.", "runway 강화.", "성공.", "cancellation economics 제한.", "penalty까지 계산."),
        C("$60~75 normalized value", "성공", "book intact 시 두 배 가치.", "P/B 정상화.", "historical book/sales.", "survival 확인.", "1~2Y target 미달이면 반증.", "1Y +76.7%.", "방향·magnitude 적중.", "배당 제외.", "total-return ledger 별도."),
        C("impairments manageable", "성공 방향", "loss가 discount보다 작다.", "maintenance reserves·sale values.", "historical premium.", "mass defaults 제한.", "large cumulative impairment면 반증.", "BVPS -4%.", "성공.", "후속 GECAS·Russia는 별도 vintage.", "idea-date risk state 고정."),
    ],
)

add(
    id="cdb4f141-bcc2-40b1-9d27-089f1093d4cd", date="2022-02-05", author="rickey824",
    ticker="AER", company="AerCap Holdings N.V.", filename="analysis/ideas/2022/2022-02-05_AER_long.md",
    source="", group="aercap", direction="Long", raw_direction="Long", security="AER common equity / Long",
    entry="약 $63", horizon="1년", raw_horizon="economic BV ~$84, normalized EPS >$8, +33%",
    title="GECAS accretion·buyback Long", verdict="1Y 실패 / 장기 mechanism 회복",
    score=6.6, process=7.0,
    conclusion="GECAS accretion·deleveraging·buyback mechanism은 장기적으로 살아남았지만 게시 19일 뒤 러시아 침공으로 약 $2.7bn pre-tax net charge가 발생했다. 1M -30.5%, 1Y -2.6%로 horizon은 실패했고, 2023 BVPS $83.81은 delayed recovery다.",
    t0="GECAS 약 $34bn assets를 cash 약 $24bn+equity 약 $6.6bn에 취득한 뒤 pro forma leverage 2.8x를 2.7x로 낮추고 buyback을 재개하는 논지였다. accounting BVPS 약 $69.17, estimated economic BV 약 $84.",
    reverse="$63은 integration·leverage·cycle risk를 반영했지만 특정 jurisdiction에서 legal title과 physical recovery가 분리되는 confiscation scenario는 핵심 bear에 없었다.",
    valuation="normalized EPS >$8 × sub-10x 또는 economic BV ~$84 × ~1.0x. base case는 $80대 가치였지만 balance-sheet shock가 먼저 발생했다.",
    actual="러시아 lessees의 135 aircraft·14 engines 회수가 막혀 2022 약 $2.7bn net pre-tax charge. BVPS $66.85 후 2023 보험회수·earnings·buyback으로 $83.81 회복.",
    price="SQL price-only: 1M -30.5%, 3M -26.7%, 6M -29.4%, 1Y -2.6%. 1년 thesis는 실패다.",
    drivers="jurisdictional recovery risk가 acquisition accretion과 normal aviation recovery를 압도했다. 후속 insurance recovery는 손실을 줄였지만 원 horizon을 구제하지 않는다.",
    counterfactual="러시아·중국 등 회수불능 관할의 aircraft를 100% write-off해도 equity와 liquidity가 버티는가?",
    error="airline credit만 보고 sovereign confiscation·repatriation을 독립 tail로 두지 않았다.",
    warning="2022-02-24 침공과 항공기 반출 제한이 즉시 decisive signal이었다.", first_signal_date="2022-02-24",
    lessons=common_lessons("aercap"), checklist=["jurisdiction map", "legal title vs possession", "100% country writeoff", "insurance counterparty", "horizon 분리"],
    scorecard=scorecard("장기 성공", "1Y 실패", "buyback 지연 성공", "1Y 실패", "tail shock"),
    scenarios=[("Bear", "integration delay", "discount 지속", "Russia가 더 심각"), ("Base", "deleveraging+buyback", "$80대", "2023 지연 실현"), ("Tail", "jurisdiction loss", "large book charge", "현실화")],
    metrics=[("Entry price", "$63", "+33% 기대", "1Y -2.6%", "실패"), ("Economic BV", "~$84", "~1x", "2023 BVPS $83.81", "지연 성공"), ("Russia net charge", "미모델링", "0", "~$2.7bn", "강한 실패"), ("2022 BVPS", "~$84 방향", "상승", "$66.85", "실패"), ("2023 BVPS", "장기 회복", "상승", "$83.81", "지연 성공")],
    timeline=[("2021-11", "GECAS close", "platform 확대"), ("2022-02-05", "VIC Long", "economic book thesis"), ("2022-02-24", "Russia invasion", "tail 발생"), ("2022-03", "aircraft 회수 제한", "legal/physical 분리"), ("2022", "$2.7bn net charge", "book 손실"), ("2023", "insurance recoveries", "손실 일부 회수"), ("2023", "BVPS $83.81", "delayed recovery"), ("2023", "large buybacks", "mechanism 재개")],
    claims=[
        C("GECAS accretion", "장기 성공", "discounted acquisition이 earnings/book accretive.", "scale·funding·purchase accounting.", "deal economics.", "integration 성공.", "earnings dilution이면 반증.", "2023 record earnings.", "지연 성공.", "tail risk 별도 누락.", "deal accretion과 country risk 분리."),
        C("economic BV ~$84", "지연 성공", "embedded gains 포함 book.", "assets less liabilities.", "transaction marks.", "recoverable assets.", "material writeoff면 반증.", "2022 $66.85, 2023 $83.81.", "1Y 실패.", "economic book의 recoverability 과신.", "jurisdiction haircut."),
        C("leverage 2.8→2.7x", "지연 성공", "earnings·sales로 deleverage.", "cash retention.", "pro forma leverage.", "큰 one-off 없음.", "charge로 ratio 악화면 반증.", "Russia로 지연 후 정상화.", "timing miss.", "straight-line 가정.", "tail capital buffer."),
        C("~10% buyback capacity", "후행 강한 성공", "excess cash로 할인 환매.", "per-share accretion.", "GECAS cash engine.", "deleveraging 우선 충족.", "환매 중단이면 지연.", "2023 대규모 환매.", "horizon 뒤 실현.", "시점 과신.", "capital priority calendar."),
        C("asset downside 제한", "단기 실패", "diversified mobile assets가 downside를 제한.", "재임대·회수.", "global fleet.", "법적 소유권 집행.", "country assets 회수불능이면 반증.", "135 aircraft·14 engines 노출.", "$2.7bn charge.", "sovereign tail 누락.", "physical control을 본다."),
        C("+33% rerating in 1Y", "실패", "book 근처로 복귀.", "de-risking·buyback.", "$63 vs $84.", "tail event 없음.", "1Y target 미달이면 실패.", "1Y -2.6%.", "약 36ppt 이상 gap.", "duration 과신.", "delayed recovery 분리."),
    ],
)

add(
    id="840e3835-b192-45b6-8724-ed459b7d9183", date="2016-02-11", author="Napoleon",
    ticker="AERI", company="Aerie Pharmaceuticals", filename="analysis/ideas/2016/2016-02-11_AERI_short.md",
    source="", group="aerie", direction="Short", raw_direction="Short", security="AERI common equity / Short",
    entry="약 $14.16", horizon="승인·상업화 및 terminal outcome", raw_horizon="Rhopressa TAM ~$100m vs bull ~$350m",
    title="ophthalmic-biotech TAM Short", verdict="fundamental 일부 적중 / terminal Short 실패",
    score=5.7, process=5.8,
    conclusion="Rhopressa+Rocklatan 2021 제품매출 $112.1m과 순손실 $74.8m은 작은 TAM·cash burn 논지를 지지했다. 그러나 두 제품이 승인됐고 Alcon이 $15.25 cash에 인수해 $14.16 short는 borrow 전에도 terminal loss였다.",
    t0="bull은 Rhopressa를 $350m급 franchise로 평가했다. 원문은 efficacy·side effects·physician adoption과 약 100명 salesforce 비용을 반영하면 약 $100m 사업에 가깝고 dilution이 필요하다고 봤다.",
    reverse="가격은 approval·commercial platform·Rocklatan option과 strategic buyer value를 반영했다. short는 TAM뿐 아니라 FDA binary와 M&A premium을 이겨야 했다.",
    valuation="낙관적 $350m revenue에서도 commercial opex를 차감한 EPS 약 $1.58, 약 9x라는 역산이었다. 하지만 strategic buyer는 standalone EPS가 아니라 portfolio·pipeline value를 지불했다.",
    actual="Rhopressa 2017, Rocklatan 2019 승인. 2021 combined product revenue $112.1m, net loss $74.8m. 2022 Alcon이 $15.25 cash, 약 $770m equity value로 인수했다.",
    price="중간 SQL performance row는 없어 exact borrow-adjusted IRR을 만들지 않는다. terminal $15.25는 entry $14.16보다 7.7% 높아 borrow 전 short 손실이다.",
    drivers="commercial forecast의 edge보다 regulatory success와 strategic option value가 security payoff를 지배했다.",
    counterfactual="$100m revenue와 지속 손실을 정확히 맞혀도 buyer가 $15.25를 낼 확률을 반영한 expected short return은 양수였는가?",
    error="business-size forecast를 stock short payoff로 직결하고 M&A/approval convexity를 충분히 가격화하지 않았다.",
    warning="2017-12 Rhopressa FDA approval이 core binary short thesis의 첫 명확한 반증이었다.", first_signal_date="2017-12-18",
    lessons=common_lessons("aerie"), checklist=["approval probability", "label/efficacy", "gross-to-net", "cash runway/dilution", "borrow+M&A premium"],
    scorecard=scorecard("부분 성공", "부분 성공", "approval 실패", "terminal 실패", "장기 보유 불리"),
    scenarios=[("Bear/short", "approval·TAM 부진", "큰 하락", "TAM만 부분 적중"), ("Base", "~$100m business", "제한 가치", "$112.1m"), ("Strategic", "buyer premium", "short loss", "$15.25 takeout")],
    metrics=[("Short entry", "$14.16", "하락", "$15.25 terminal", "실패"), ("Bull TAM", "~$350m", "과대", "combined $112.1m", "bearish view 지지"), ("Bear TAM", "~$100m", "~$100m", "$112.1m", "근접"), ("2021 net loss", "cash burn", "지속 손실", "$74.8m", "성공"), ("Takeout premium", "미모델링", "없음", "37% to prior close", "tail 실패")],
    timeline=[("2016-02-11", "VIC Short", "TAM·burn thesis"), ("2017-12-18", "Rhopressa FDA approval", "binary 반증"), ("2018-04", "commercial launch", "revenue 시작"), ("2019-03", "Rocklatan approval", "option value 확대"), ("2020", "제품매출 $83.1m", "상업화 진행"), ("2021", "매출 $112.1m", "TAM 근접"), ("2021", "순손실 $74.8m", "burn 지속"), ("2022-11", "Alcon $15.25 close", "terminal short 실패")],
    claims=[
        C("Rhopressa TAM 과대", "대체로 성공", "$350m bull TAM은 과도.", "효능·adoption이 penetration 제한.", "bear ~$100m.", "combined revenue 비교 가능.", "revenue $250m+면 반증.", "2021 combined $112.1m.", "bear와 근접.", "combination 포함 비교.", "제품별 매출을 분리."),
        C("차별성 제한", "부분 성공", "임상차별성이 adoption을 제한.", "의사 처방·side effect.", "원문 clinical view.", "승인·label은 가능.", "빠른 broad adoption이면 반증.", "승인됐지만 ramp 제한.", "약은 성공, blockbuster 아님.", "approval와 commercial success 혼동.", "label·persistence 추적."),
        C("commercial cash burn", "성공", "salesforce가 owner earnings를 압박.", "SG&A fixed cost.", "독립 commercialization.", "gross margin이 opex 못 덮음.", "FCF breakeven이면 반증.", "2021 net loss $74.8m.", "손실 지속.", "손실의 R&D/launch 분해 제한.", "매출 대비 SG&A·R&D bridge."),
        C("dilution/financing", "부분 성공", "장기 손실로 자금조달 필요.", "cash burn→shares/convert.", "임상단계 balance sheet.", "capital access.", "self-funded 전환이면 반증.", "손실 지속, 그러나 sale로 종결.", "collapse 미발생.", "financing을 terminal로 과신.", "runway와 buyer option 병행."),
        C("FDA downside", "실패", "regulatory/clinical risk가 value 훼손.", "approval binary.", "개발자산.", "FDA 승인 실패 가능.", "두 제품 승인 시 반증.", "Rhopressa·Rocklatan 승인.", "핵심 binary 반대.", "확률 calibration 부족.", "base rate와 label 확률."),
        C("common short payoff", "실패", "fundamental miss가 주가하락으로 전환.", "cash burn·dilution.", "$14.16 entry.", "M&A premium 제한.", "takeout above entry면 실패.", "$15.25 cash.", "+7.7% underlying, borrow 전.", "M&A tail 누락.", "strategic value를 확률가중."),
    ],
)

add(
    id="4d1db626-f89b-4363-99da-e4a4a08ff53e", date="2017-11-01", author="flubber926",
    ticker="Aeromex", company="Grupo Aeroméxico", filename="analysis/ideas/2017/2017-11-01_Aeromex_long.md",
    source="", group="aeromex", direction="Long", raw_direction="Long", security="Aeroméxico legacy common equity / Long",
    entry="약 MXN32.7", horizon="2019", raw_horizon="2019 fair value MXN71.4, Delta JV synergy ~$200m",
    title="strategic-airline/JV Long", verdict="강한 실패 — Chapter 11 old equity near-wipeout",
    score=1.8, process=3.2,
    conclusion="Mexico demand와 Delta partnership는 franchise를 살렸지만 margin·deleveraging은 미달했고 COVID 뒤 Chapter 11에서 old equity는 reorganized equity의 0.01% 미만을 받았다. Delta의 MXN49 과거 매입가는 common floor가 아니었다.",
    t0="MXN32.7, 2017E EV/EBITDAR 약 4.6x. Delta가 약 MXN49에 strategic stake를 취득했고, low penetration·slot hub·fleet simplification·2021까지 $200m JV synergy로 margin doubling과 MXN71.4를 기대했다.",
    reverse="시장은 fuel·FX·labor·airport constraints와 leverage를 할인했다. 원문은 strategic sponsor price와 enterprise franchise value가 common downside를 보호한다고 보았다.",
    valuation="traffic·margin expansion·deleveraging을 통해 lower exit EV/EBITDAR에도 equity가 두 배 이상 되는 구조였다. levered common이라 EBITDA miss가 residual에 비선형으로 작용했다.",
    actual="2019 revenue MXN68.8bn·EBITDAR MXN14.9bn에도 net loss MXN2.4bn. 2020 revenue MXN28.5bn(-58.5%), EBITDAR -MXN6.8bn, Chapter 11. 2022 emergence에서 old equity <0.01%.",
    price="SQL performance row가 없어 exact interim return을 만들지 않는다. reorganization treatment가 terminal payoff를 사실상 0으로 고정한다.",
    drivers="zero-demand shock가 operating leverage와 lease/debt claims를 폭발시켰고 enterprise value는 DIP·creditors·new money에 귀속됐다.",
    counterfactual="12개월 zero-revenue stress에서 unrestricted cash와 DIP 없이 old common에 잔여가치가 남는가?",
    error="strategic partner의 past purchase price와 network value를 legacy common의 floor로 오해했다.",
    warning="2019에도 consolidated net loss가 지속된 것이 COVID 이전 첫 경고였다.", first_signal_date="2019-12-31",
    lessons=common_lessons("aeromex"), checklist=["unrestricted cash runway", "lease-adjusted leverage", "zero-revenue stress", "DIP waterfall", "partner incentives"],
    scorecard=scorecard("franchise 생존", "실패", "JV 불충분", "near-wipeout", "2019부터 실패"),
    scenarios=[("Bear", "margin 미달·FX/fuel", "equity 압박", "2019 이미 진행"), ("Base", "JV+deleveraging", "MXN71.4", "미실현"), ("Tail", "zero demand/Chapter 11", "old equity 소멸", "현실화")],
    metrics=[("Entry price", "MXN32.7", "MXN71.4", "old equity near-zero", "강한 실패"), ("Delta anchor", "~MXN49", "floor", "floor 아님", "강한 실패"), ("2017E EV/EBITDAR", "~4.6x", "rerating", "earnings 붕괴", "실패"), ("2020 revenue", "성장", "증가", "-58.5%", "강한 실패"), ("Old equity", "보존", "큰 upside", "<0.01% new equity", "near-wipeout")],
    timeline=[("2017-11-01", "VIC Long", "Delta/JV thesis"), ("2018", "JV 운영", "strategic value 유지"), ("2019", "net loss MXN2.4bn", "margin 반증"), ("2020-06-30", "Chapter 11 filing", "waterfall 현실화"), ("2020", "revenue -58.5%", "zero-demand shock"), ("2020", "EBITDAR -MXN6.8bn", "fixed-cost 폭발"), ("2022-03-17", "Chapter 11 emergence", "franchise 생존"), ("2022", "old equity <0.01%", "legacy common 실패")],
    claims=[
        C("Mexico aviation growth", "장기 방향만 성공", "낮은 penetration이 traffic 성장.", "소득·노선 확대.", "시장 구조.", "yield·capacity discipline.", "traffic가 margin으로 안 이어지면 제한.", "franchise는 생존.", "equity 구제 못함.", "TAM을 profit으로 직결.", "RASM-CASK conversion."),
        C("Delta JV synergy ~$200m", "실패·불충분", "revenue $160m+cost $40m synergy.", "network·sales·cost.", "JV plan.", "규제·execution.", "2019 margin/net income 미달이면 반증.", "2019 net loss.", "synergy가 equity 부족.", "gross synergy 강조.", "standalone counterfactual 필요."),
        C("margin doubling", "실패", "CASK 개선과 mix로 margin 확대.", "operating leverage.", "fleet simplification.", "fuel·FX 안정.", "2019 margin/earnings 미달.", "net loss 지속.", "target 미달.", "EBITDAR와 net income 혼동.", "lease·interest까지 bridge."),
        C("Delta MXN49 floor", "강한 실패", "strategic purchase price가 downside anchor.", "partner incentive.", "49% stake.", "partner가 old equity 보호.", "restructuring dilution이면 반증.", "old equity <0.01%.", "floor 소멸.", "enterprise와 security 혼동.", "waterfall을 먼저 본다."),
        C("deleveraging·MXN71.4", "실패", "growth가 debt burden을 낮춰 fair value 실현.", "EBITDAR growth.", "4.6x entry.", "shock 없음.", "leverage 상승·target 미달이면 반증.", "Chapter 11.", "terminal near-zero.", "path risk 과소평가.", "liquidity calendar."),
        C("brand/slots protect common", "실패", "quality assets가 downside 방어.", "franchise sale/reorg value.", "hub·partner.", "claims보다 잔여가치 큼.", "company survives but old equity wiped면 반증.", "정확히 발생.", "business 생존/common 실패.", "security selection 오류.", "enterprise survival과 common recovery 분리."),
    ],
)

add(
    id="9678c95b-ef8e-407a-be1c-a94e357edc1c", date="2009-10-15", author="leob710",
    ticker="AES", company="The AES Corporation", filename="analysis/ideas/2009/2009-10-15_AES_long.md",
    source="", group="aes", direction="Long", raw_direction="Long", security="AES common equity / Long",
    entry="약 $10~11", horizon="2011", raw_horizon="2011 adjusted EPS $1.20~1.30, target $19~20",
    title="contracted-project growth Long", verdict="실패 — project-to-parent EPS bridge 미달",
    score=3.1, process=4.0,
    conclusion="non-recourse debt와 contracted assets는 corporate survival을 지켰지만 3,500MW program이 parent EPS로 전환되는 속도는 과대평가됐다. 2010 adjusted EPS $0.94, 2011 $1.04로 $1.20~1.30을 하회했고 2Y price-only -30.7%였다.",
    t0="consolidated debt 약 $19bn 중 약 $13.7bn이 non-recourse. 3,500MW construction program의 96%가 contracted됐고 2011까지 EPS $0.25, cash flow $300~400m 기여를 기대했다.",
    reverse="시장은 leverage·emerging-market·FX와 project execution을 할인했다. 원문은 계약성과 non-recourse structure를 earnings certainty에 가깝게 번역했다.",
    valuation="2011 EPS midpoint $1.25 × 16x ≈ $20. construction contribution과 utility-like multiple을 동시에 요구했다.",
    actual="2010 adjusted EPS $0.94, 2011 $1.04. project contributions·operations는 있었지만 FX·tax·share count·financing·parent leakage로 주당 denominator가 예상에 못 미쳤다.",
    price="SQL price-only: 1Y -16.6%, 2Y -30.7%, 3Y -27.3%, 5Y -8.2%. target와 반대다.",
    drivers="project-level 계약은 downside를 줄였지만 parent distribution과 주당 EPS로 올라오는 과정의 leakage가 성장률을 낮췄다.",
    counterfactual="각 project EBITDA에서 local debt·tax·minority·capex를 뺀 parent cash가 실제 몇 달러 EPS를 만드는가?",
    error="MW under construction과 contracted 비율을 parent EPS certainty로 너무 빨리 변환했다.",
    warning="2010 adjusted EPS $0.94가 원문 2010 $1.05~1.15에 미달한 것이 첫 경고였다.", first_signal_date="2010-12-31",
    lessons=common_lessons("aes"), checklist=["project별 ownership", "local debt service", "parent distribution", "FX/tax/minority", "fully diluted shares"],
    scorecard=scorecard("생존 성공", "실패", "commissioning 일부", "2Y 실패", "2010부터 경고"),
    scenarios=[("Bear", "project leakage", "EPS 정체", "현실화"), ("Base", "$1.20~1.30", "$19~20", "미달"), ("Bull", "16x+ multiple", "큰 upside", "미실현")],
    metrics=[("Consolidated debt", "~$19bn", "관리 가능", "생존", "구조 성공"), ("Non-recourse debt", "~$13.7bn", "parent 보호", "distress 회피", "성공"), ("Construction", "3,500MW/96% contracted", "EPS +$0.25", "bridge 미달", "실패"), ("2011 adj EPS", "$1.20~1.30", "$1.20~1.30", "$1.04", "-13~20%"), ("2Y price-only", "$19~20 target", "큰 상승", "-30.7%", "강한 실패")],
    timeline=[("2009-10-15", "VIC Long", "project EPS thesis"), ("2009", "3,500MW program", "96% contracted"), ("2010", "adjusted EPS $0.94", "첫 miss"), ("2011 guidance", "$1.08~1.14", "원문보다 낮음"), ("2011", "adjusted EPS $1.04", "denominator 실패"), ("2011-10", "2Y -30.7%", "stock 실패"), ("2012", "portfolio actions", "structure 조정"), ("2014", "5Y -8.2%", "장기 target도 미달")],
    claims=[
        C("non-recourse protects parent", "대체로 성공", "project debt가 parent insolvency를 제한.", "법적 ring-fence.", "$13.7bn non-recourse.", "cross-default 제한.", "parent distress면 반증.", "회사는 생존.", "solvency 성공.", "distribution blockage 간과.", "protection과 cash access 분리."),
        C("3,500MW/96% contracted", "운영 일부 성공", "건설 program이 실행된다.", "COD 후 contracted cash.", "project list.", "delay/cost overrun 제한.", "COD 지연이면 반증.", "projects 진행.", "EPS 전환은 약함.", "MW를 value로 직결.", "ownership·margin 적용."),
        C("2011 EPS $1.20~1.30", "실패", "신규사업이 주당이익을 끌어올린다.", "project contributions.", "EPS bridge.", "FX·tax·shares 안정.", "$1.15 미만이면 반증.", "$1.04.", "-$0.16~-0.26.", "leakage 과소평가.", "parent EPS bridge."),
        C("proportional cash flow", "부분 성공", "cash flow $1.1~1.3bn.", "project distributions.", "guidance.", "local cash upstream 가능.", "distribution 미달이면 반증.", "cash generation은 유지됐으나 EPS 미달.", "conversion 약함.", "cash와 distributable cash 혼동.", "restricted cash 차감."),
        C("16x / $19~20", "실패", "utility-like multiple.", "contracted mix rerating.", "midpoint valuation.", "complexity discount 축소.", "target 미달이면 실패.", "2Y -30.7%.", "방향 반대.", "multiple 과대.", "complexity·EM discount 반영."),
        C("contracted mix downside", "stock 실패", "85% 해외/contracted mix가 downside 제한.", "revenue visibility.", "PPAs·regulated.", "FX·parent leakage 제한.", "price drawdown >25%면 반증.", "2Y -30.7%.", "실패.", "business stability를 equity floor로 봄.", "capital structure 뒤 residual 계산."),
    ],
)

add(
    id="f28865bc-5e49-4a6b-b575-3971a2024503", date="2020-09-18", author="Gator19",
    ticker="AES", company="The AES Corporation", filename="analysis/ideas/2020/2020-09-18_AES_long.md",
    source="", group="aes", direction="Long", raw_direction="Short", security="AES common equity / Long",
    entry="SQL next-day close $17.30", horizon="2022", raw_horizon="7~9% EPS CAGR, $32 target",
    title="renewables·credit·Fluence transformation Long", verdict="강한 성공 — measurable catalysts 실현",
    score=9.6, process=9.8,
    conclusion="raw SQL Short와 달리 원문은 명백한 Long이다. S&P BBB-, backlog 6.9GW, coal 25%, adjusted EPS $1.44→$1.67(약 7.7% CAGR), Fluence $28 IPO가 순차 실현됐고 2Y price-only +52.8%였다.",
    t0="next-year EPS 약 12x vs utility index 약 19x. +6GW renewable/storage backlog, 두 번째 IG rating, coal <30%, Fluence external mark가 complex/coal discount를 줄일 것으로 봤다.",
    reverse="시장은 emerging-market·FX·coal·complexity와 execution risk를 반영했다. 이 thesis는 여러 독립 milestone으로 반증 가능했다.",
    valuation="Core EPS × rerated multiple + Fluence value/share = ~$32. EPS growth·credit de-risking·hidden asset crystallization의 세 경로가 있었다.",
    actual="2020 adjusted EPS $1.44, backlog 6.9GW, coal 25%, S&P BBB-. 2021 Fluence 31m shares를 $28에 IPO. 2022 adjusted EPS $1.67로 2Y CAGR 약 7.7%.",
    price="SQL price-only: 1Y +33.6%, 2Y +52.8%. $17.30 단순 적용은 약 $26대라 exact $32 hit를 과장하지 않는다.",
    drivers="signed backlog·rating·coal mix·external JV price라는 관찰 가능한 catalyst stack가 earnings와 risk perception을 동시에 개선했다.",
    counterfactual="Fluence mark를 0으로 두고도 core EPS 성장과 credit upgrade만으로 충분한 IRR이 나왔는가?",
    error="$32 magnitude는 공격적이었지만 핵심 catalyst decomposition은 우수했다.",
    warning="signed backlog가 COD로 전환되지 않거나 EPS CAGR이 5% 아래면 최초 반증.", first_signal_date="2021-12-31",
    lessons=common_lessons("aes"), checklist=["signed MW·COD", "ownership/margin", "rating milestone", "coal exit cash cost", "Fluence stake dilution"],
    scorecard=scorecard("강한 성공", "성공", "매우 강한 성공", "2Y 성공", "양호"),
    scenarios=[("Bear", "backlog delay·IG 실패", "discount 지속", "미발생"), ("Base", "7~9% EPS+coal exit", "core rerating", "현실화"), ("Bull", "Fluence mark+$32", "큰 upside", "방향 성공·magnitude 제한")],
    metrics=[("Entry price", "$17.30", "$32", "~$26대 at 2Y ratio", "방향 성공"), ("Backlog", "~6GW", "확대·실행", "6.9GW", "강한 성공"), ("Adj EPS", "$1.44", "7~9% CAGR", "$1.67 in 2022", "7.7% 성공"), ("Coal mix", ">30% 우려", "<30%", "25% pro forma", "성공"), ("2Y price-only", "큰 상승", "$32 방향", "+52.8%", "강한 성공")],
    timeline=[("2020-09-18", "VIC Long", "raw Short 교정"), ("2020-11-02", "S&P BBB-", "credit catalyst"), ("2020-12", "backlog 6.9GW", "growth 확인"), ("2020-12", "coal 25%", "mix 전환"), ("2020", "adj EPS $1.44", "출발점"), ("2021-10-27", "Fluence IPO $28", "hidden value mark"), ("2022", "adj EPS $1.67", "7.7% CAGR"), ("2022-09", "2Y +52.8%", "security 성공")],
    claims=[
        C("EPS 7~9% CAGR", "강한 성공", "2022까지 7~9% 성장.", "backlog·cost·deleveraging.", "$1.44 base.", "COD·margin 실현.", "CAGR <5%면 반증.", "$1.67, 약 7.7%.", "범위 내.", "non-GAAP dependence.", "GAAP/adjusted bridge."),
        C("renewable backlog", "강한 성공", "+6GW가 earnings에 기여.", "signed PPAs→COD.", "pipeline/backlog.", "계약·execution.", "signed MW 정체면 반증.", "6.9GW.", "+0.9GW vs marker.", "MW margin 상세 제한.", "COD와 ownership 추적."),
        C("second IG rating", "강한 성공", "rating upgrade로 funding·investor base 확대.", "risk premium 하락.", "deleveraging plan.", "agency 기준 충족.", "upgrade 미발생이면 반증.", "S&P BBB- 6주 후.", "빠른 적중.", "rating 자체를 equity catalyst로 단순화.", "funding spread도 확인."),
        C("coal below 30%", "성공", "coal exit로 mix·ESG discount 개선.", "retire/sale 4.5GW.", "asset plan.", "exit 비용 통제.", "30% 이상이면 반증.", "25% pro forma.", "-5ppt 이상.", "pro forma와 actual 차이.", "actual generation mix 추적."),
        C("Fluence crystallization", "강한 성공", "IPO/private mark로 hidden value.", "external price discovery.", "50% JV at T0.", "IPO market open.", "no transaction이면 반증.", "$28 IPO.", "외부 mark 형성.", "gross stake value와 AES net value 차이.", "dilution·tax·holdco discount 차감."),
        C("$32 by 2022", "방향 성공·magnitude 제한", "core+Fluence로 $32.", "EPS와 multiple 상승.", "SOTP.", "모든 catalyst 결합.", "target 미달이면 magnitude 실패.", "2Y +52.8%, 단순 약 $26대.", "약 $6 미달 가능.", "point target 과도.", "driver별 value contribution 분리."),
    ],
)


def idea_sources(i):
    original = S(
        "VIC original idea" if i["source"] else "VIC source-DB preserved original",
        i["source"], "Value Investors Club / source SQL", i["date"],
        "T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.", "원문",
    )
    return [original, *GROUP_SOURCES[i["group"]]]


def render_index():
    rows = []
    for n, i in enumerate(IDEAS, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(
            f"| {n} | {i['date']} | {i['ticker']} | {i['raw_direction']} | "
            f"{i['direction']} | [{i['company']}]({rel}) | {i['verdict']} |"
        )
    return "\n".join([
        "# Batch 065 — AerCap / Aerie Pharmaceuticals / Aeroméxico / AES V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. 아이디어 1건 = canonical Markdown 1개다.",
        f"> Research as-of {ASOF}. 같은 회사도 entry date·price·risk state·horizon별로 분리했다.", "",
        "## Canonical idea files", "",
        "| # | 날짜 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |",
        "|---:|---|---|---|---|---|---|", *rows, "",
        "## Entity / direction / duplicate audit", "",
        "- AerCap 6건은 기존 Batch 010 중복 구조화 행을 제거하고 Batch 065를 정본으로 승격했다.",
        "- AerCap 2014는 Batch 064에 남긴다. ILFC closing 전 thesis로 별도 idea unit이다.",
        "- AERI는 실제 Short이며 terminal $15.25 cash consideration을 payoff anchor로 사용했다.",
        "- Aeroméxico는 legacy common과 reorganized company를 분리하고 old equity <0.01% treatment를 우선했다.",
        "- AES 2020은 raw Short지만 원문은 $32 target의 명백한 Long이다.", "",
        "## 핵심 비교", "",
        "1. AerCap 2015·2017은 book compounding을 맞혔어도 persistent discount와 COVID path 때문에 stock outcome이 약했다.",
        "2. 2018 vintage는 contracted rent를 cash certainty로 과대평가해 2020 horizon이 실패했다.",
        "3. 2019 vintage는 sources/uses와 covenant를 먼저 봐 extreme stress에서도 process가 유효했다.",
        "4. 2020 vintage는 0.4x book가 요구한 impairment가 과도해 빠른 성공이었다.",
        "5. 2022 vintage는 legal title과 physical recovery를 혼동해 Russia tail에 맞았고, 2023 회복은 delayed outcome이다.",
        "6. AERI는 TAM을 맞히고도 M&A로 Short가 실패했고, Aeroméxico는 franchise가 살아도 old common은 사라졌다.",
        "7. AES 2009는 MW→EPS bridge가 실패했지만 2020은 observable catalyst stack로 성공했다.", "",
        "## 구조화 데이터", "",
        "- data/curated/batch_065_aer_aeri_aeromex_aes_deep_v7.json: 10 postmortems, 60 claims, 50 metrics, 상세 timeline·sources.",
        "- data/curated/batch_065_source_catalog.json: raw metadata source packet이며 production glob에는 포함되지 않는다.",
        "- analysis/batch_065_aer_aeri_aeromex_aes_10.md: Streamlit wrapper.", "",
    ])


def dedupe_batch_010():
    path = ROOT / "data/curated/batch_010_transport_capital_structure_deep_v7.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    removed = {}
    for key, rows in payload.items():
        if not isinstance(rows, list):
            continue
        before = len(rows)
        payload[key] = [row for row in rows if row.get("idea_id") not in AER_IDS]
        if before != len(payload[key]):
            removed[key] = before - len(payload[key])
    previous = payload.get("deduplication", {})
    prior_ids = set(previous.get("moved_idea_ids", []))
    payload["deduplication"] = {
        "canonical_batches": [64, 65],
        "moved_idea_ids": sorted(prior_ids | AER_IDS),
        "reason_ko": "Aeroplan/AerCap entity audit와 date-specific AerCap 장문 V9를 Batch 064·065 정본으로 승격",
        "removed_rows_by_table": {
            **previous.get("removed_rows_by_table", {}),
            **{f"batch65_{key}": value for key, value in removed.items()},
        },
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    if len(IDEAS) != 10 or len({i["id"] for i in IDEAS}) != 10:
        raise ValueError("Batch 065 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5:
            raise ValueError(f"{idea['id']}: six claims and five metrics required")

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
        report = base.render_report(idea)
        if idea["group"] in {"aerie", "aeromex"}:
            report = report.replace(
                "**B** — source SQL price-only ratios; dividends·tax 제외.",
                "**미사용** — reliable interim price ledger가 없어 terminal corporate-action payoff만 사용.",
            )
        path = ROOT / idea["filename"]
        path.write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_065_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 065 — AerCap / Aerie Pharmaceuticals / Aeroméxico / AES V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 065 V9 Index](batch_065_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_065_aer_aeri_aeromex_aes_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 65
    payload["title"] = "AerCap / Aerie Pharmaceuticals / Aeroméxico / AES — Price, Tail Risk and Security Payoff V9"
    payload["metadata_audit"] = {
        "direction_corrections": 1,
        "cross_batch_duplicates_removed": 6,
        "performance_rows_rejected": 0,
        "corporate_action_terminal_payoffs": 2,
        "notes": [
            "AES 2020 raw Short를 original-text Long으로 교정.",
            "AERI는 $15.25 cash takeout, Aeroméxico는 old equity <0.01%를 terminal payoff anchor로 사용.",
            "AerCap 여섯 vintage는 Batch 010에서 제거하고 Batch 065를 정본으로 사용.",
        ],
    }
    payload["batch_lessons"] = [
        "같은 회사도 entry P/B와 risk state가 다르면 전혀 다른 투자다.",
        "BVPS forecast와 terminal multiple forecast를 분리한다.",
        "계약된 rent는 counterparty solvency shock에서 현금과 같지 않다.",
        "crisis long은 정상 EPS보다 현재 가격이 요구하는 permanent impairment를 계산한다.",
        "biotech short에는 approval·borrow·M&A premium을 별도 tail로 넣는다.",
        "strategic partner의 매입가는 bankruptcy common recovery floor가 아니다.",
        "project MW는 parent EPS까지의 leakage bridge로 검증한다.",
    ]
    failures = {
        "aercap": "duration; persistent_discount; airline_credit; funding; residual_value; jurisdiction_recovery",
        "aerie": "regulatory_binary; commercial_scale; cash_burn; dilution; borrow; strategic_takeout",
        "aeromex": "operating_leverage; liquidity; lease_claims; bankruptcy_waterfall; strategic_anchor",
        "aes": "project_to_parent_leakage; fx; tax; minority; multiple; execution",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failures[idea["group"]]
        row["success_pattern_ko"] = "security_mapping; reverse_expectations; primary_source_validation; falsifier_calendar; payoff_separation"
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    dedupe_batch_010()
    print(
        f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} "
        f"timeline={len(payload['timeline'])} sources={len(payload['sources'])}"
    )


if __name__ == "__main__":
    main()
