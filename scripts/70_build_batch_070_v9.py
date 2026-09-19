#!/usr/bin/env python3
"""Build Batch 070 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
CATALOG = ROOT / "data/curated/batch_070_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_070_afsi_aft_afx_afya_ag_ag1_aga_deep_v7.json"

spec = importlib.util.spec_from_file_location("batch64_base", ROOT / "scripts/64_build_batch_064_v9.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "amtrust": "AmTrust는 small-commercial P&C, warranty와 specialty risk를 인수하던 보험사였다. earned premium과 investment income에서 losses·expenses·reinsurance cost를 빼며, reserve adequacy와 statutory capital이 common의 실질 book-value growth를 결정한다.",
    "aft": "Advanced Fiber Technologies Income Fund는 제지공장의 stock-preparation 과정에 쓰이는 screen basket·rotor 등 소모성 정밀부품을 공급했다. installed base와 마모에 따른 replacement demand가 매출을 만들고 가격·mix에서 합금·가공·판매비·유지 capex를 뺀 현금이 trust distribution의 재원이었다.",
    "zeiss": "Carl Zeiss Meditec는 ophthalmology와 microsurgery 장비·소모품을 판매한다. VisuMax 설치장비는 SMILE 시술용 patient interface와 service를, IOL 사업은 수술 건수와 premium mix를 recurring revenue로 바꾼다. 장비 출하·소모품 mix·R&D와 규제 품질비용이 EBITA를 좌우한다.",
    "afya": "Afya는 브라질의 의과대학·전문의 교육과 physician digital services를 운영한다. 승인된 의대 seats×등록률×tuition이 핵심이며, campus maturation·가격인상·M&A에서 교직원·임차·금융비용·capex를 뺀 현금이 common에 귀속된다.",
    "agco": "AGCO는 Massey Ferguson·Fendt·Valtra·Challenger 등의 농기계와 부품을 전 세계 dealer망을 통해 판다. farmer income·crop price·금리와 dealer inventory가 장비수요를, volume·mix·공장가동률·working capital과 finance JV가 equity cash flow를 결정한다.",
    "arctic": "Arctic Glacier Income Fund는 북미 packaged ice를 제조·유통했다. route density와 지역 plant network가 유통비를 낮추지만 수요 계절성, fuel·packaging, working capital, 높은 debt와 refinancing이 distributable cash와 trust-unit recovery를 결정한다.",
    "auto1": "AUTO1 Group은 유럽에서 소비자에게 중고차를 매입해 dealer에게 판매하는 Merchant 플랫폼과 소비자에게 직접 판매하는 Autohero를 운영한다. unit volume×GPU에서 refurbishment·logistics·inventory funding·CAC·fixed cost를 뺀 cash가 가치의 핵심이다.",
    "algoma": "구 Algoma Steel은 캐나다 Sault Ste. Marie의 integrated steel producer였다. 출하량×steel price에서 coal·iron ore·energy·labour·freight와 maintenance capex를 뺀 cycle cash flow가 가치의 핵심이며, post-bankruptcy clean balance sheet와 strategic scarcity가 common payoff를 바꾼다.",
}

ENGINE = {
    "amtrust": "earned premium × (1-loss ratio-expense ratio) + investment income - tax = book growth; reserve development·ceded recoverables·related parties·statutory capital을 common payoff에 연결한다.",
    "aft": "installed machines × replacement frequency × price - metal·machining·selling cost - tax - maintenance capex ± working capital = distributable cash; distribution과 takeover cash를 날짜별로 합산한다.",
    "zeiss": "device volume×ASP + installed base×procedure/consumable revenue - manufacturing·R&D·SG&A·quality cost - tax - capex = equity FCF; recurring mix와 acquisition amortization을 분리한다.",
    "afya": "approved seats×occupancy×tuition + digital revenue - faculty·campus·platform cost - cash interest - tax - capex ± working capital = equity FCF; acquisition price와 earn-outs를 반영한다.",
    "agco": "units×price/mix + parts - material·labour·warranty - SG&A/R&D - interest - tax - capex ± working capital = equity cash; finance-JV exposure와 pension을 함께 stress한다.",
    "arctic": "ice volume×net price - plant·route·fuel·packaging - cash interest - maintenance capex ± working capital = pre-distribution cash; insolvency에서는 asset-sale proceeds의 creditor waterfall 뒤 unit recovery만 센다.",
    "auto1": "Merchant units×GPU + Autohero units×GPU + financing contribution - logistics·refurbishment·CAC - fixed opex - inventory funding - capex = equity cash; volume와 margin을 따로 판정한다.",
    "algoma": "steel shipments×realized spread - fixed conversion cost - pension/environmental cash - maintenance capex ± working capital = cycle FCF; strategic bid는 debt·claims 뒤 주당 cash로 확인한다.",
}

KPI = {
    "amtrust": "gross/earned premium, accident-year loss ratio, prior-year development, combined ratio, ceded recoverables, statutory surplus, tangible book/share, NPW/tangible equity, related-party balances",
    "aft": "installed base, replacement share, order intake, gross/EBITDA margin, maintenance capex, working capital, distributable cash/unit, payout coverage, takeover consideration",
    "zeiss": "VisuMax installed base, SMILE procedures, recurring revenue mix, IOL volume/mix, order intake, gross margin, EBITA margin, R&D ratio, FCF, EPS",
    "afya": "approved seats, occupancy, tuition price, mature-campus margin, adjusted EBITDA, FCF conversion, net debt, acquisition consideration, digital revenue/users",
    "agco": "retail units, dealer inventory, crop/farmer income, price/mix, gross margin, working capital, finance receivables, pension, net debt, EPS",
    "arctic": "volume, route density, normalized EBITDA, maintenance capex, FCF, payout, leverage, debt maturity, litigation, insolvency distribution/unit",
    "auto1": "Merchant/Autohero units, revenue, GPU by segment, inventory turns, logistics/refurbishment cost, CAC, financing attach, gross profit, adjusted EBITDA, net cash",
    "algoma": "shipments, utilization, realized steel spread, cash cost/tonne, maintenance capex, pension/environmental obligations, net cash, book/share, strategic bid/share",
}


SOURCES = {
    "amtrust": [
        S("AmTrust restatement notice", "https://www.sec.gov/Archives/edgar/data/1365555/000136555517000051/amtrustform8-kedgarcopy.htm", "SEC / AmTrust", "2017-04-10", "2014·2015와 2016 interim statements 재작성 및 controls issue 검증."),
        S("AmTrust restatement results", "https://www.sec.gov/Archives/edgar/data/1365555/000136555517000061/ex991pressrelease.htm", "SEC / AmTrust", "2017-04-11", "2014·2015 net income 감소와 오류 성격 검증."),
        S("Amended take-private agreement", "https://www.sec.gov/Archives/edgar/data/1365555/000119312518186313/d556924d8k.htm", "SEC / AmTrust", "2018-06-07", "$14.75/share cash terminal consideration 검증."),
    ],
    "aft": [
        S("Aikawa corporate history", "https://aikawagroup.com/index.php/en/about-us/aikawa-group", "Aikawa Group", "2006", "Advanced Fiber Technologies 인수와 private ownership 복귀 검증."),
        S("AFT takeover record", "", "Ontario Securities Commission / issuer materials", "2006", "Aikawa의 C$3.00/unit acquisition 조건 교차검증."),
    ],
    "zeiss": [
        S("Carl Zeiss Meditec FY2024/25 annual report", "https://reports.zeiss.com/meditec-ag/2425/en/", "Carl Zeiss Meditec", "2025-12-11", "Revenue €2,227.6m, EBITA €257.7m, EPS €1.61, FCF €203.7m 검증."),
        S("H1 FY2025/26 results", "https://www.zeiss.com/meditec-ag/en/media-news/press-releases/2026/half-year-financial-communication-2025-26.html", "Carl Zeiss Meditec", "2026-05-12", "Revenue €991.0m, adjusted EBITA margin 6.1%, EPS €0.17와 restructuring 검증."),
        S("9M FY2025/26 statement", "https://www.zeiss.com/meditec-ag/en/media-news/press-releases/2026/statement-q3-fy-2025-26.html", "Carl Zeiss Meditec", "2026-08", "9개월 adjusted EBITA margin 8.0%와 outlook 검증."),
    ],
    "afya": [
        S("Afya FY2025 results", "https://www.sec.gov/Archives/edgar/data/1771007/000129281426000823/ex99-1.htm", "SEC / Afya", "2026-03", "2025 revenue R$3.697bn, adjusted EBITDA R$1.680bn, FCF R$1.056bn 검증."),
        S("Afya SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=1771007&owner=exclude", "SEC / Afya", "2019-2026", "Annual results, seat expansion, acquisition와 shareholder-return filings 검증."),
    ],
    "agco": [
        S("AGCO FY2005 Form 10-K", "https://www.sec.gov/Archives/edgar/data/880266/000095014406002147/g99944e10vk.htm", "SEC / AGCO", "2006-03", "2003~05 sales, dealer/finance network, debt와 historical stock range 검증."),
        S("AGCO SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=880266&owner=exclude", "SEC / AGCO", "2003-2008", "연도별 영업·재무·주가 공시 교차검증."),
    ],
    "arctic": [
        S("Arctic Glacier CCAA case", "https://www.alvarezandmarsal.com/arctic-glacier-income-fund-arctic-glacier-inc-and-subsidiaries", "Alvarez & Marsal / court monitor", "2012-2022", "2012-02-22 CCAA 개시, asset sale와 creditor process 검증."),
        S("Arctic Glacier final distribution", "https://www.globenewswire.com/news-release/2022/11/07/2550327/0/en/arctic-glacier-income-fund-announces-final-distribution-and-delisting-from-the-cse.html", "Arctic Glacier Income Fund", "2022-11-07", "C$0.00549502/unit final distribution과 delisting 검증."),
    ],
    "auto1": [
        S("AUTO1 FY2025 results", "https://www.auto1-group.com/press/pressrelease/auto1-group-achieves-record-breaking-2025-results/", "AUTO1 Group", "2026-02-25", "842,271 units, gross profit €990.6m, adjusted EBITDA €197.5m과 segment units/GPU 검증."),
        S("AUTO1 financial reports", "https://ir.auto1-group.com/websites/auto1/English/3000/financial-reports.html", "AUTO1 Group", "2021-2026", "IPO 이후 annual·quarterly reports와 cash·segment economics 검증."),
    ],
    "algoma": [
        S("Essar to acquire Algoma Steel", "https://www.aist.org/essar-global-to-acquire-algoma-steel", "Association for Iron & Steel Technology / Essar", "2007-04", "C$56/share all-cash offer와 약 C$1.85bn equity value 검증."),
        S("Essar closes Algoma acquisition", "https://www.aist.org/essar-global-closes-acquisition-of-algoma-steel", "Association for Iron & Steel Technology / Essar", "2007-06-20", "거래 종결과 C$56/share consideration 검증."),
    ],
}


IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


def sc(business, valuation, catalyst, security, timing):
    return [("Business thesis", business), ("Valuation thesis", valuation), ("Catalyst thesis", catalyst), ("Security payoff", security), ("Timing / path", timing)]


def claim(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson):
    return C(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson)


add(
    id="279b93f2-bf11-41f1-9211-7fc026e43a29", date="2013-08-19", author="Francisco432", ticker="AFSI", company="AmTrust Financial Services Inc.", filename="analysis/ideas/2013/2013-08-19_AFSI_short.md", source="", group="amtrust", direction="Short", raw_direction="Short", security="AmTrust common equity / Short", entry="약 $18", horizon="1~3년 capital·reserve catalyst", raw_horizon="tangible-book depletion, reserve development, captive scrutiny와 rating/covenant catalyst",
    title="reserve·capital-quality insurer Short", verdict="fundamental concern 부분 적중 / trade 실패에 가까움", score=5.5, process=6.5,
    conclusion="tangible book·reserve·internal-control 우려는 2017 restatement로 일부 검증됐고 2018 take-private는 $14.75였다. 그러나 약 $18 short 뒤 주가가 약 $36까지 올라 약 100% adverse excursion을 만들었다. 후행 accounting validation은 catalyst clock과 생존경로가 틀린 short를 소급해 성공으로 만들지 않는다.",
    t0="reported earnings가 tangible book으로 축적되지 않고, life-settlement contract의 Level 3 valuation, aggressive reserving·acquisition accounting, related-party reinsurance와 balance-sheet leverage가 premium growth를 떠받친다는 논지였다. NPW/tangible equity가 mid-2010 약 150%에서 2Q13 약 336%로 상승한 점을 catalyst 압력으로 봤다.",
    reverse="시장은 niche premium growth, acquisitions, reinsurance access와 reported ROE가 capital을 계속 보충한다고 봤다. 보험 short에서는 accounting quality가 낮아도 statutory intervention·rating action·reserve charge의 날짜가 없으면 book growth와 multiple expansion이 수년간 short를 압도할 수 있다.",
    valuation="reported P/E가 아니라 tangible book, statutory surplus와 normalized accident-year loss ratio로 equity를 다시 계산해야 한다. Level 3 assets·ceded recoverables를 haircut하고 adverse reserve development를 surplus에서 차감하되, downside target와 catalyst timing·borrow·MAE를 하나의 position rule로 묶는다.",
    actual="주가는 먼저 약 $36까지 올랐다. 2017 회사는 2014·2015와 2016 interim financials를 restate했고 internal controls 문제를 공시했다. 2018 amended take-private price는 $14.75 cash였다. diagnosis의 일부는 맞았지만 원 horizon보다 훨씬 늦었고 path가 치명적이었다.",
    price="$18→$36은 short에 약 100% adverse price move다. $14.75 terminal은 entry보다 약 18.1% 낮지만 exact borrow·cover·dividend ledger가 없어 realized return이나 IRR은 제시하지 않는다.",
    drivers="fundamental red flags보다 premium growth, book accretion과 catalyst latency가 먼저 작동했다. 최종 가격만 보면 하락이지만 실제 short는 두 배 adverse path·carry·margin risk를 견뎌야 했다.",
    counterfactual="회계 문제가 4년 뒤에야 드러나고 그 전에 주가가 2배가 되어도 이 position size와 borrow terms에서 expected value가 양수였는가?",
    error="여러 quality concern을 하나의 임박한 collapse로 묶었고 statutory capital·rating·reserve review 각각의 독립된 catalyst clock과 MAE/cover rule을 두지 않았다.",
    warning="주가와 premium/book growth가 2014~15에도 계속 올라 $30대를 통과한 시점이 trade-level timing thesis의 명확한 반증이었다.", first_signal_date="2014-12-31",
    scenarios=[("Bear for short", "growth·capital access 지속", "$30~40", "약 $36 실현"), ("Base", "reserve·capital 정상화", "$14~18", "2018 $14.75"), ("Bull for short", "rating/covenant 조기 촉발", "$8~12", "기간 내 미실현")],
    metrics=[("Entry / peak", "~$18 short", "하락", "~$36", "~100% adverse"), ("NPW/tangible equity", "~150%→336%", "capital constraint", "즉시 collapse 없음", "timing 실패"), ("Restatement", "회계 우려", "1~3년 catalyst", "2017", "약 4년 지연"), ("2014/15 income", "질 낮음", "하향수정", "restated lower", "부분 적중"), ("Terminal", "entry 아래", "short payoff", "$14.75", "price-only -18.1%")],
    timeline=[("2013-08-19", "VIC Short", "~$18 entry"), ("2014", "premium·book growth 지속", "catalyst 지연"), ("2015", "stock $30대", "MAE 확대"), ("2016", "stock 약 $36", "trade-level failure"), ("2017-04-10", "restatement notice", "accounting concern 확인"), ("2017-04-11", "revised results", "정량 조정"), ("2018-06-07", "$14.75 amended deal", "terminal price"), ("2018", "take-private", "public short 종료")],
    lessons=["보험 short는 red flag의 수보다 statutory·rating·reserve catalyst의 날짜가 중요하다.", "eventual restatement와 investable short payoff를 분리한다.", "reserve·Level 3·related-party claim을 각각 별도 falsifier로 관리한다.", "100% adverse excursion을 허용하는 thesis에는 position-size와 cover rule이 필수다."],
    checklist=["accident-year loss ratio", "prior-year reserve development", "statutory surplus", "NPW/surplus와 tangible equity", "ceded recoverable collateral", "Level 3 marks", "rating triggers", "borrow·MAE·cover"],
    scorecard=sc("우려 일부 적중", "terminal 일부 적중", "촉매 지연", "short path 취약", "실패에 가까움"),
    claims=[
        claim("earnings와 tangible book 불일치", "부분 성공", "reported earnings가 tangible book을 만들지 못한다.", "low-quality gains·intangibles·capital leakage가 common cushion을 약화한다.", "earnings와 tangible book divergence.", "차이가 경제적 손실을 선행한다.", "tangible book가 지속 성장하면 약화.", "2017 restatement가 일부 earnings quality 우려를 확인했다.", "방향 적중·4년 지연.", "회계 divergence를 즉시 가격 catalyst로 봤다.", "quality claim과 timing claim을 분리한다."),
        claim("life-settlement Level 3 가치", "미확정", "life-settlement contracts가 과대평가됐다.", "unobservable mortality·discount assumptions이 asset와 income을 부풀린다.", "복잡한 Level 3 disclosures.", "mark haircut이 capital에 material하다.", "cash realization이 carrying value를 지지하면 반증.", "공개 자료만으로 동일 portfolio의 full cash realization을 복원하지 못했다.", "정량 gap 미확정.", "불투명성을 손실액으로 등치했다.", "asset별 cash-vs-mark roll-forward를 요구한다."),
        claim("reserve underestimation", "부분 성공", "초기 loss picks가 낮아 adverse development가 온다.", "성장기에 낮은 picks가 earnings·surplus를 앞당긴다.", "peer 대비 빠른 성장과 reserve mechanics.", "claims maturation이 unfavorable하다.", "다년 favorable development면 반증.", "후속 accounting·control 문제는 질 우려를 지지했지만 reserve collapse 단독증거는 제한적이다.", "claim-specific 증거 부족.", "회계 문제를 전부 reserve 문제로 묶었다.", "accident year·line별 triangle로 검증한다."),
        claim("acquisition accounting", "부분 성공", "인수회계가 organic profitability를 과장한다.", "purchase accounting·bargain gains가 recurring earnings처럼 보인다.", "연속 acquisitions와 높은 reported ROE.", "organic cohorts가 인수 후에도 profitable하다.", "organic combined ratio가 안정되면 약화.", "restatement는 quality 우려를 지지했지만 acquisition별 economics는 혼합이다.", "정확한 deal ROIC 미복원.", "복잡성을 자동으로 value destruction으로 봤다.", "deal별 cash price·reserve·earn-out·organic result를 잇는다."),
        claim("related-party reinsurance·capital", "부분 검증", "affiliate 구조가 risk와 capital을 가린다.", "ceding·recoverables·collateral이 earnings와 statutory capital을 이동시킨다.", "Maiden 등 related-party links.", "terms가 arm's length가 아니다.", "collateral·cash settlement가 충분하면 약화.", "governance scrutiny는 커졌지만 즉시 capital failure는 없었다.", "red flag와 loss 사이 gap.", "관계 자체를 손실로 간주했다.", "terms·collateral·counterparty credit을 계량한다."),
        claim("NPW/tangible equity 150%→336%", "timing 실패", "leverage가 성장의 끝과 rating/covenant catalyst를 부른다.", "premium risk가 capital cushion보다 빠르게 커진다.", "mid-2010 ~150%, 2Q13 ~336%.", "외부 capital과 reinsurance가 닫힌다.", "growth·rating이 3년 지속되면 timing 반증.", "즉시 collapse 없이 stock이 약 2배 오른 뒤 2017 event가 왔다.", "1~3년 horizon miss.", "stress indicator를 dated catalyst로 오인했다.", "ratio threshold에 실제 rating/covenant 문구를 붙인다."),
    ],
)


add(
    id="01ce2cae-c9a7-42af-87b0-69887be1ba7a", date="2021-09-30", author="Hastan", ticker="AG1", company="AUTO1 Group SE", filename="analysis/ideas/2021/2021-09-30_AG1_long.md", source="", group="auto1", direction="Long", raw_direction="Short", security="Xetra:AG1 common equity / Long", entry="약 €31.57", horizon="5~10년 European digitization", raw_horizon="1.3x forward sales, terminal net margin 5%+, 10x sales potential",
    title="pan-European used-car network Long", verdict="운영 성공 / 높은 entry의 stock 실패", score=6.0, process=7.0,
    conclusion="raw Short를 실제 Long으로 교정했다. European sourcing·dealer network와 Autohero growth는 2025 842,271 units, gross profit €990.6m, adjusted EBITDA €197.5m으로 의미 있게 진전됐다. 그러나 약 €31.57 entry 대비 2026 약 €20.2는 약 -36% price-only다. 사업 논지와 entry valuation의 판정이 갈렸다.",
    t0="유럽 중고차 시장의 fragmentation·소비자 friction을 pan-European digital inventory, inspection·pricing data와 logistics network로 해결한다는 논지였다. Merchant sourcing base에서 Autohero DTC와 financing을 붙여 장기 net margin 5%+, 1.3x forward sales의 큰 upside를 기대했다.",
    reverse="시장은 inventory·working-capital intensity, refurbishing/logistics, CAC, used-car price volatility와 national regulation이 software-like network effect를 제한한다고 봤다. 5% net margin은 아직 증명되지 않았고 1.3x sales도 low-margin auto retail에는 비쌀 수 있었다.",
    valuation="sales multiple보다 segment units×GPU에서 fixed opex·inventory funding·capex를 차감한 cash earnings를 평가해야 한다. Merchant와 Autohero의 mature margin·capital turns를 따로 두고 dilution·net cash를 반영한다.",
    actual="FY2025 total units 842,271(+22.1%), Merchant 740,732, Autohero 101,539, gross profit €990.6m, adjusted EBITDA €197.5m을 기록했다. company는 European used-car share 3.1%를 제시했다. business proof는 강해졌지만 original high entry는 회복하지 못했다.",
    price="2021-09 monthly reference 약 €31.57에서 2026 약 €20.2는 약 0.64x, -36% price comparison이다. exact purchase·dividends·tax ledger가 없어 total return·IRR은 아니다.",
    drivers="network·execution은 unit growth와 GPU를 만들었지만 2021 valuation, cash burn 우려와 multiple compression이 initial investors의 payoff를 눌렀다. 같은 company라도 lower entry와 결과가 달라진다.",
    counterfactual="net margin이 장기 5%가 아니라 2~3%이고 inventory funding cost가 높아도 €31.57 entry에서 충분한 equity return이 나오는가?",
    error="huge TAM과 sales growth를 margin·capital intensity보다 앞에 놓고, Autohero의 성공확률과 terminal multiple을 높은 entry에 동시에 낙관적으로 적용했다.",
    warning="2022 주가가 급락하고 Autohero cash investment가 valuation 부담으로 드러난 시점이 entry-price thesis의 최초 반증이었다.", first_signal_date="2022-03-31",
    scenarios=[("Bear", "GPU 낮음·cash burn·multiple 0.2x", "€8~15", "2022 일부"), ("Base", "Merchant growth·Autohero breakeven", "€25~35", "2026 €20대"), ("Bull", "5%+ net margin·share gains", "€60+", "미실현")],
    metrics=[("Entry / current", "€31.57", "compound", "~€20.2", "-36% price-only"), ("2025 units", "rapid growth", "platform scale", "842,271", "성공"), ("Autohero units", "fast ramp", "material DTC", "101,539", "성공 방향"), ("Gross profit", "operating leverage", "증가", "€990.6m", "성공"), ("Adj EBITDA", "loss→profit", "positive", "€197.5m", "성공")],
    timeline=[("2021-09-30", "VIC Long", "raw Short 교정"), ("2022-03", "growth-stock selloff", "entry break"), ("2022", "Autohero investment reset", "cash discipline"), ("2023", "GPU·profitability focus", "model repair"), ("2024", "positive EBITDA scale", "operating proof"), ("2025-12-31", "842,271 units", "record scale"), ("2026-02-25", "FY2025 results", "adj EBITDA €197.5m"), ("2026-09-18", "stock ~€20", "entry not recovered")],
    lessons=["TAM과 network effect보다 unit economics·capital turns를 먼저 본다.", "business execution과 entry-price return을 별도 score로 준다.", "sales multiple은 low-margin inventory business에서 위험한 shortcut이다.", "same company의 다른 vintage는 별도 idea unit이다."],
    checklist=["Merchant/Autohero units", "GPU by segment", "inventory turns", "refurbishment·logistics", "CAC", "financing attach", "adjusted EBITDA-to-FCF", "net cash·share count"],
    scorecard=sc("성공", "높은 entry 실패", "profitability 실현", "common 적절", "stock 실패"),
    claims=[
        claim("European digitization", "성공", "fragmented used-car flow가 online platform으로 이동한다.", "better search·pricing·liquidity가 consumers와 dealers를 모은다.", "large fragmented TAM과 consumer friction.", "trust·regulation·offline habits가 극복된다.", "unit share가 정체하면 반증.", "2025 units 842,271, share 3.1%로 확대됐다.", "+22.1% units YoY.", "TAM을 company capture로 곧장 번역했다.", "market share와 cohort retention을 본다."),
        claim("sourcing·data network effect", "성공 방향", "더 많은 cars·dealers가 pricing과 liquidity를 개선한다.", "data density가 conversion·GPU·turns를 높인다.", "pan-European sourcing/dealer base.", "cross-border logistics cost가 scale benefit보다 작다.", "GPU·turns 악화면 반증.", "Merchant 740,732 units와 group gross profit €990.6m이 scale을 지지했다.", "직접 causal attribution 제한.", "scale을 moat로 자동 간주했다.", "GPU·turns·repeat dealer rate로 검증한다."),
        claim("Autohero rapid ramp", "부분 성공", "B2C가 group growth와 margin을 가속한다.", "direct retail spread·financing이 Merchant보다 높은 GPU를 준다.", "초기 fast growth와 Merchant sourcing.", "CAC·refurbishment·inventory가 통제된다.", "unit growth가 cash burn만 키우면 반증.", "2025 Autohero 101,539 units(+36.4%), GPU 약 €2.6k 수준.", "scale-up 성공·long-term share는 미완.", "revenue growth를 mature profit으로 봤다.", "segment contribution after fixed/capital cost를 본다."),
        claim("terminal net margin 5%+", "미확정", "규모와 services로 5% 이상 net margin이 가능하다.", "GPU 확대·CAC 감소·financing이 fixed cost를 흡수한다.", "IPO targets와 analogs.", "working capital·tax·interest가 낮다.", "multi-year net margin 3% 미만이면 실패.", "2025 adjusted EBITDA는 positive지만 5% net margin은 아직 검증되지 않았다.", "FY2025 revenue €8.2bn 대비 adj EBITDA 2.4%.", "EBITDA를 net margin으로 점프했다.", "EBITDA→FCF→net income bridge를 둔다."),
        claim("1.3x forward sales 저평가", "실패", "growth platform에 1.3x sales는 싸다.", "10x topline과 mature margin이 multiple을 정당화한다.", "T0 sales multiple.", "capital intensity와 dilution이 낮다.", "strong growth에도 stock가 entry 아래면 반증.", "운영기록에도 2026 price는 entry보다 약 36% 낮다.", "multiple compression.", "sales quality를 과대평가했다.", "gross profit·FCF multiple을 병행한다."),
        claim("€31.57 entry compounding", "실패", "장기 winner를 합리적 가격에 산다.", "market-share·earnings growth가 price를 높인다.", "IPO 후 pullback.", "valuation derating이 실행을 상쇄하지 않는다.", "5년 뒤 entry 미회복이면 실패.", "2026 약 €20.2.", "-36% price-only.", "좋은 company와 좋은 price를 혼동했다.", "entry별 implied mature margin을 역산한다."),
    ],
)


add(
    id="c6149029-5a3f-455c-8fb8-03ed16d9a9a2", date="2022-03-04", author="crestone", ticker="AG1-ETR", company="AUTO1 Group SE", filename="analysis/ideas/2022/2022-03-04_AG1_ETR_long.md", source="https://www.valueinvestorsclub.com/idea/Auto1_Group_SE/6559612238", group="auto1", direction="Long", raw_direction="Long", security="Xetra:AG1 common equity / Long", entry="원문 약 €11; 2022-03 monthly reference €10.34", horizon="2027 Autohero target", raw_horizon="Merchant≈current price, net cash ~€3.70/share, Autohero free option; 2027 750k units·€2,500 GPU·8% margin·€3.74 EPS, €36 target",
    title="Merchant SOTP·free-Autohero-option Long", verdict="부분 성공·진행 중 — entry rerating, 2027 volume target은 미도달", score=8.0, process=8.2,
    conclusion="약 €10~11 entry에서 Merchant value와 net cash가 downside를 지지했고 Autohero GPU·group profitability는 실제 개선됐다. 2025 Autohero units 101,539, GPU €2,605, group adjusted EBITDA €197.5m, 2026 price 약 €20.2로 price-only 약 1.84~1.95x다. 다만 2027 750k units·8% margin·€3.74 EPS는 아직 미래이자 현재 run-rate와 큰 gap이므로 최종 성공으로 앞당기지 않는다.",
    t0="폭락 뒤 group EV에서 Merchant business를 보수적으로 평가하면 current price 대부분을 설명하고 net cash 약 €3.70/share, Autohero는 사실상 free option이라는 SOTP였다. 2027 Autohero 750k units, GPU €2,500+, 8% operating margin과 EPS €3.74에 €36 target를 제시했다.",
    reverse="시장은 Autohero의 cash burn·inventory·refurbishment/logistics와 CAC, equity funding 필요를 우려했다. Merchant value도 used-car price·dealer liquidity에 민감하고 cash는 growth losses로 소진될 수 있었다.",
    valuation="Merchant units×GPU와 normalized opex에 독립 multiple을 적용하고 net cash를 더한 뒤 Autohero는 probability-weighted 2027 cases로 평가해야 한다. cash burn·dilution을 €3.70/share에서 차감하고 target year의 distance를 명시한다.",
    actual="FY2025 Merchant 740,732 units, Autohero 101,539 units, Autohero GPU €2,605, group gross profit €990.6m, adjusted EBITDA €197.5m이었다. profitability turn과 GPU claim은 강하게 확인됐지만 Autohero volume은 750k target의 13.5%다.",
    price="원문 약 €11 대비 2026 약 €20.2는 약 +83.6%, monthly €10.34 대비는 약 +95.4% price-only다. exact trade·tax·capital actions가 없어 total return·IRR은 계산하지 않는다.",
    drivers="낮은 entry, Merchant survival과 group profitability turn이 rerating을 만들었다. 수익은 750k bull case 달성보다 valuation floor와 early unit-economics proof에서 먼저 나왔다.",
    counterfactual="Autohero가 2027 750k가 아니라 150~200k units에 머물러도 Merchant+net cash만으로 €10~11 entry의 downside와 €20 value를 지킬 수 있는가?",
    error="valuation floor는 좋았지만 5년 내 Autohero units를 7배 이상 키우는 logistics·capital·market-share path와 dilution을 너무 매끄럽게 봤다.",
    warning="실패 신호가 아니라 목표 재보정 신호는 2025 Autohero 101,539 units로, GPU는 달성했어도 2027 750k volume과 큰 gap이 남았다는 점이다.", first_signal_date="2026-02-25",
    scenarios=[("Bear", "Merchant margin 압박·Autohero burn", "€6~10", "미실현"), ("Base", "Merchant value+profitability", "€18~25", "2026 ~€20.2"), ("Bull", "2027 750k·8% margin", "€36+", "아직 미판정")],
    metrics=[("Entry / price", "€10.34~11", "€36", "~€20.2", "+84~95% price-only"), ("Autohero units", "early ramp", "750k in 2027", "101,539 in 2025", "13.5% of target"), ("Autohero GPU", "bridge to €2,500+", "≥€2,500", "€2,605", "성공"), ("Group adj EBITDA", "loss-making", "positive", "€197.5m", "성공"), ("2027 EPS", "€3.74", "€3.74", "아직 미래", "미판정")],
    timeline=[("2022-03-04", "VIC Long", "~€11"), ("2022-H2", "cash-burn reset", "downside test"), ("2023", "GPU·cost discipline", "unit economics 개선"), ("2024", "group profitability", "catalyst 확인"), ("2025-12-31", "Autohero 101,539 units", "volume gap"), ("2025-12-31", "Autohero GPU €2,605", "target hit"), ("2026-02-25", "FY2025 results", "adj EBITDA €197.5m"), ("2027", "original target year", "아직 미도래")],
    lessons=["같은 회사도 entry price가 thesis 결과를 바꾼다.", "SOTP floor와 long-dated growth option을 별도 확률로 둔다.", "GPU target 달성과 volume target 달성을 분리한다.", "미래 목표는 horizon 전 최종 실패·성공으로 판정하지 않는다."],
    checklist=["Merchant units·GPU", "Autohero units·GPU", "inventory days", "segment contribution", "cash burn", "net cash/share", "dilution", "2027 milestone cadence"],
    scorecard=sc("성공", "강한 성공", "profitability 성공", "common 적절", "2027 미완"),
    claims=[
        claim("Merchant≈current price", "성공 방향", "Merchant standalone가 €10~11 price 대부분을 지지한다.", "dealer network의 units·GPU가 normalized EBITDA를 만든다.", "existing scale와 SOTP.", "Merchant volume·GPU가 유지된다.", "segment contraction·loss면 반증.", "2025 Merchant 740,732 units와 group profit이 floor를 지지했다.", "standalone EBITDA 공시 제한.", "group costs 배분을 단순화했다.", "segment contribution과 central cost를 분리한다."),
        claim("net cash €3.70/share", "부분 성공", "cash가 downside와 Autohero funding을 제공한다.", "losses를 버틸 duration과 residual value가 생긴다.", "T0 balance sheet.", "cash burn·dilution이 제한된다.", "cash가 대부분 소진되면 floor 약화.", "회사는 distress 없이 profitability로 전환했다.", "정확한 per-share cash path는 변동.", "cash를 고정자산처럼 봤다.", "분기별 burn·working capital·FDSO를 갱신한다."),
        claim("Autohero free option", "성공", "시장가격이 Autohero value를 거의 주지 않는다.", "DTC units·GPU·financing이 positive contribution으로 전환된다.", "낮은 residual valuation.", "funding cost가 option value를 먹지 않는다.", "unit economics 악화·증자면 반증.", "Autohero 101,539 units, GPU €2,605로 실질가치가 생겼다.", "full mature value는 미확정.", "free option에도 carrying cost가 있음을 축소했다.", "option burn과 milestone을 함께 가격화한다."),
        claim("GPU €2,500+", "성공", "retail GPU가 규모와 services로 €2,500를 넘는다.", "pricing·refurbishment·financing이 per-unit profit을 높인다.", "원문 GPU bridge.", "competitive pricing과 inventory losses가 통제된다.", "GPU €2,000 아래면 실패.", "2025 Autohero GPU €2,605.", "+€105/+4.2% vs target.", "GPU를 segment margin과 동일시했다.", "GPU 뒤 fixed·capital cost까지 본다."),
        claim("2027 Autohero 750k·8% margin", "큰 gap·미판정", "유럽 scale로 750k units와 8% operating margin을 달성한다.", "network density와 fixed-cost leverage가 volume·margin을 함께 높인다.", "TAM과 expansion plan.", "약 5년간 logistics·capital이 병목이 아니다.", "2026 run-rate가 목표와 크게 괴리되면 확률 하향.", "2025 units 101,539, target의 13.5%; margin target 미검증.", "648,461 units gap.", "S-curve 속도를 과대평가했다.", "연도별 units·capacity·capital gates를 둔다."),
        claim("€36 / EPS €3.74", "부분 성공·미판정", "2027 target economics가 €36 value를 만든다.", "EPS×multiple와 net cash가 target를 지지한다.", "원문 explicit model.", "volume·margin·share count가 모두 맞는다.", "target year EPS가 크게 미달하면 실패.", "2026 price ~€20.2로 entry 대비 상승했지만 2027 EPS는 아직 미래다.", "target price의 56% 수준.", "중간 rerating을 final thesis와 혼동할 수 있다.", "horizon까지 milestone-based 확률을 갱신한다."),
    ],
)


add(
    id="f407b250-5fa4-4ac4-a3b2-dd85150a9681", date="2003-02-28", author="nigel92", ticker="AGA CN", company="Algoma Steel Inc. (legacy)", filename="analysis/ideas/2003/2003-02-28_AGA_CN_algoma_long.md", source="https://www.valueinvestorsclub.com/idea/Algoma_Steel_Inc./3277645466", group="algoma", direction="Long", raw_direction="Long", security="legacy Algoma common equity / Long", entry="C$3.30", horizon="2~5년 cycle recovery·strategic value", raw_horizon="book C$11.47, P/B 0.29x; post-bankruptcy clean balance sheet and steel-price catalysts",
    title="post-bankruptcy steel deep-value Long", verdict="매우 강한 성공 — C$56 cash takeout, 약 16.97x price multiple", score=9.8, process=9.0,
    conclusion="2002 restructuring 뒤 clean balance sheet와 C$11.47 book를 C$3.30, 0.29x에 산 논지는 steel cycle 회복과 strategic scarcity가 결합해 크게 성공했다. Essar는 2007 C$56/share cash, 약 C$1.85bn equity value로 Algoma를 인수했다. 단순 terminal/entry는 16.97x이나 interim distributions·tax 없이 IRR을 만들지는 않는다.",
    t0="bankruptcy stigma, steel-price weakness와 thin coverage 때문에 C$11.47 book value의 29%에 거래됐지만 new common은 과거 debt 대부분이 제거된 operating asset을 소유한다는 thesis였다. steel pricing, anti-dumping relief와 analyst coverage가 catalyst였다.",
    reverse="시장은 book가 cycle-top replacement value가 아니고 pensions·environmental liabilities, single-site labour·energy와 commodity spread가 다시 equity를 훼손할 수 있다고 봤다. post-bankruptcy company도 재차 distress할 수 있었다.",
    valuation="P/B만이 아니라 normalized tonnes×steel spread에서 pension/environmental cash와 sustaining capex를 뺀 cycle FCF, net cash/debt와 strategic replacement value를 triangulate해야 한다. terminal C$56 bid는 external value check다.",
    actual="steel market과 company earnings가 회복했고 strategic consolidation이 진행됐다. Essar Global은 2007 C$56/share all-cash, 약 C$1.85bn equity value로 인수를 발표하고 2007-06-20 거래를 종결했다.",
    price="C$56 / C$3.30 = 16.97x, price gain은 약 +1,597%다. 이는 단순 entry-to-cash ratio이며 exact purchase/closing date, interim distributions와 tax가 없어 annualized total return은 계산하지 않는다.",
    drivers="post-bankruptcy balance-sheet reset, extreme discount to asset/book, steel-cycle operating leverage와 strategic buyer의 replacement value가 동시에 작동했다. 낮은 entry가 pension·commodity downside를 충분히 흡수했다.",
    counterfactual="steel spread가 30% 낮고 pension·environmental cash가 book의 절반을 소모해도 C$3.30에서 liquidation·going-concern value가 남는가?",
    error="결과는 탁월했지만 book value의 realizability, maintenance capex·pension cash와 steel-spread bear case를 더 명시적으로 haircut했어야 한다.",
    warning="명확한 thesis break는 없었다. 사전 경고는 liquidity 악화·labour disruption·steel spread 하락으로 clean balance sheet가 다시 debt로 바뀌는 경우였다.", first_signal_date="2004-12-31",
    scenarios=[("Bear", "steel slump·liabilities", "C$0~5", "미실현"), ("Base", "book discount 축소", "C$10~15", "초과 달성"), ("Bull", "cycle+strategic takeout", "C$30+", "C$56 실현")],
    metrics=[("Entry / book", "C$3.30 / C$11.47", "0.29x P/B", "book discount 해소", "성공"), ("Takeout", "미가정", "strategic upside", "C$56 cash", "매우 강한 성공"), ("Price multiple", "1.0x", "rerating", "16.97x", "+1,597%"), ("Equity value", "deep value", "cycle recovery", "~C$1.85bn", "성공"), ("Balance sheet", "post-bankruptcy", "clean 유지", "strategic sale 가능", "성공")],
    timeline=[("2002-02", "bankruptcy exit", "new equity·debt reset"), ("2003-02-28", "VIC Long", "C$3.30"), ("2004", "steel pricing recovery", "FCF inflection"), ("2004-12-31", "balance sheet validation", "thesis confirmation"), ("2005", "cycle earnings·coverage", "discount 축소"), ("2006", "global steel consolidation", "strategic option"), ("2007-04", "Essar C$56 bid", "value crystallization"), ("2007-06-20", "deal close", "cash terminal")],
    lessons=["post-bankruptcy equity는 old debt가 아니라 new capital structure를 분석한다.", "deep P/B는 book realizability와 normalized FCF를 함께 검증한다.", "commodity downside가 커도 entry discount가 충분하면 비대칭이 생긴다.", "cash takeout는 terminal value를 검증하지만 exact IRR에는 full ledger가 필요하다."],
    checklist=["new capital structure", "net cash/debt", "steel shipments·spread", "cash cost/tonne", "maintenance capex", "pension/environmental cash", "labour contract", "strategic replacement value"],
    scorecard=sc("강한 성공", "극단적 저평가", "cycle·takeout 성공", "new common 적절", "매우 강한 성공"),
    claims=[
        claim("post-bankruptcy clean balance sheet", "강한 성공", "new common은 old leverage가 제거된 steel asset을 소유한다.", "lower interest·claims가 cycle recovery cash를 equity에 남긴다.", "2002 restructuring.", "hidden liabilities가 다시 leverage를 만들지 않는다.", "liquidity crisis·new debt면 반증.", "회사는 strategic sale까지 equity value를 보존했다.", "C$1.85bn bid 가능.", "legacy stigma가 과도했음을 잘 포착.", "old/new capital structure를 절대 혼용하지 않는다."),
        claim("C$11.47 book의 0.29x", "강한 성공", "C$3.30은 asset/book 대비 극단적 할인이다.", "cycle normalization이 impairment risk보다 크면 discount가 닫힌다.", "book C$11.47.", "book assets가 economic earning power를 가진다.", "persistent losses·asset write-down이면 실패.", "C$56 cash bid가 asset value를 외부 검증했다.", "bid/book도 크게 상회.", "book composition haircut가 더 필요했다.", "inventory·PP&E·liabilities별 realizability를 본다."),
        claim("steel pricing recovery", "성공", "economy·trade relief가 realized steel spread를 높인다.", "높은 fixed cost에서 spread 상승이 EBITDA·FCF를 증폭한다.", "depressed cycle와 anti-dumping catalysts.", "imports·input costs가 price 상승을 상쇄하지 않는다.", "realized spread와 utilization이 회복하지 않으면 반증.", "spread·utilization 회복이 strategic interest를 만들었다.", "방향 강한 적중.", "macro timing은 불확실했다.", "price보다 realized spread/tonne을 본다."),
        claim("pension·legacy liabilities manageable", "성공", "remaining obligations이 deep discount를 소모하지 않는다.", "cleaner capital structure와 FCF가 payments를 감당한다.", "restructuring terms와 low entry.", "cash contributions이 cycle cash보다 작다.", "liability funding이 재차 distress를 부르면 실패.", "2007 cash sale까지 common이 큰 value를 받았다.", "terminal outcome 지지.", "정확한 downside cash schedule 제한.", "5년 liability cash schedule을 만든다."),
        claim("coverage·catalyst rerating", "성공", "analyst attention과 cycle data가 bankruptcy discount를 줄인다.", "uncertainty 감소가 P/B·earnings multiple을 정상화한다.", "thin coverage와 catalysts.", "business results가 narrative를 지지한다.", "coverage 증가에도 discount 지속이면 실패.", "industry consolidation과 Essar bid가 discount를 제거했다.", "C$3.30→C$56.", "coverage 자체보다 fundamentals가 핵심이었다.", "attention은 catalyst이지 value source가 아니다."),
        claim("strategic value", "매우 강한 성공", "integrated asset의 scarcity가 public price 이상 가치를 가진다.", "buyer synergies·replacement cost가 premium cash bid를 허용한다.", "single-site integrated asset와 clean equity.", "labour·environmental risk가 buyer를 막지 않는다.", "bid가 없거나 book 이하이면 미실현.", "Essar C$56/share all-cash, ~C$1.85bn.", "entry의 16.97x.", "takeout은 원문 base가 아니라 upside였다.", "strategic case도 standalone downside 위에만 얹는다."),
    ],
)


ORDER = [
    "279b93f2-bf11-41f1-9211-7fc026e43a29",
    "310ba840-8c00-4893-b2d7-cb15dc6678a9",
    "25a41a32-cb61-4857-92a2-20d3d9d32c4c",
    "fb1b28c2-534a-4321-a9a4-23b2782a5f8b",
    "a011f87e-a53e-43bc-9881-680d0941a8c2",
    "9683c5d2-a736-4988-9af3-5a6fafadcbd5",
    "e8624dcd-69c5-47cd-a830-c21effa1e3d0",
    "01ce2cae-c9a7-42af-87b0-69887be1ba7a",
    "c6149029-5a3f-455c-8fb8-03ed16d9a9a2",
    "f407b250-5fa4-4ac4-a3b2-dd85150a9681",
]


def idea_sources(i):
    original = S(
        "VIC original idea" if i["source"] else "VIC source-DB preserved original",
        i["source"], "Value Investors Club / source SQL", i["date"],
        "T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.", "원문",
    )
    return [original, *SOURCES[i["group"]]]


def render_index():
    rows = []
    for n, i in enumerate(IDEAS, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(f"| {n} | {i['date']} | {i['ticker']} | {i['raw_direction']} | {i['direction']} | [{i['company']}]({rel}) | {i['verdict']} |")
    return "\n".join([
        "# Batch 070 — AmTrust / AFT / Carl Zeiss / Afya / AGCO / Arctic Glacier / AUTO1 / Algoma V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. 방향·증권·corporate action·payoff를 먼저 고정하고 1차자료로 actual을 검증했다.", "",
        "## Canonical idea files", "", "| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## Direction / security / return audit", "",
        "- AFT-U 2004와 AG1 2021의 raw Short를 실제 Long으로 교정했다.",
        "- AFT-U와 AG-U는 ordinary common이 아니라 Canadian income-trust units다.",
        "- source SQL performance row가 10건 모두 없어 corporate-action cash·official operating actual·제한적 historical price comparison만 썼다.",
        "- Arctic Glacier의 mixed-currency distributions와 AFSI/AFT/Algoma의 corporate actions는 complete dated ledger 없이 exact total return·IRR을 만들지 않았다.", "",
        "## 핵심 판정", "",
        "1. AmTrust short는 accounting 우려가 후행 적중했지만 약 2배 adverse path 때문에 trade 실패에 가깝다.",
        "2. AFT와 Arctic Glacier는 yield·enterprise cash flow가 capital loss와 creditor priority를 막지 못했다.",
        "3. Carl Zeiss는 product moat가 살아도 earnings duration·entry multiple이 무너지면 common이 실패함을 보여준다.",
        "4. Afya는 operating success / stock rerating failure, AUTO1 두 vintage는 같은 business의 entry-price 차이를 보여준다.",
        "5. AGCO 2003은 중기 partial win 뒤 장기 실패, 2005는 약 325% adverse로 명확한 short failure다.",
        "6. Algoma는 post-bankruptcy balance-sheet reset과 deep discount가 C$56 cash takeout으로 crystallize된 강한 성공이다.", "",
        "## 구조화 데이터", "",
        "- `data/curated/batch_070_afsi_aft_afx_afya_ag_ag1_aga_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.",
        "- `data/curated/batch_070_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.",
        "- `analysis/batch_070_afsi_aft_afx_afya_ag_ag1_aga_10.md`: Streamlit wrapper.", "",
    ])


def main():
    IDEAS.sort(key=lambda i: ORDER.index(i["id"]))
    if [i["id"] for i in IDEAS] != ORDER:
        raise ValueError("Batch 070 idea order or IDs do not match catalog boundary")
    for i in IDEAS:
        if len(i["claims"]) != 6 or len(i["metrics"]) != 5 or len(i["timeline"]) != 8:
            raise ValueError(f"{i['id']}: six claims, five metrics and eight timeline events required")

    base.ASOF = ASOF
    base.CATALOG = CATALOG
    base.OUTPUT = OUTPUT
    base.BUSINESS = BUSINESS
    base.ENGINE = ENGINE
    base.KPI = KPI
    base.GROUP_SOURCES = SOURCES
    base.IDEAS = IDEAS
    base.idea_sources = idea_sources

    for i in IDEAS:
        report_path = ROOT / i["filename"]
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report = base.render_report(i).replace(
            "**B** — source SQL price-only ratios; dividends·tax 제외.",
            "**C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·제한적 price comparison만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.",
        )
        report_path.write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_070_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 070 — AmTrust / AFT / Carl Zeiss / Afya / AGCO / Arctic Glacier / AUTO1 / Algoma V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 070 V9 Index](batch_070_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_070_afsi_aft_afx_afya_ag_ag1_aga_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 70
    payload["title"] = "AmTrust / AFT / Carl Zeiss / Afya / AGCO / Arctic Glacier / AUTO1 / Algoma — Business vs Security, Short Timing and Entry Price V9"
    payload["metadata_audit"] = {
        "direction_corrections": 2,
        "company_mapping_corrections": 0,
        "security_type_corrections": 2,
        "split_adjustments": 0,
        "cross_batch_duplicates_removed": 0,
        "performance_rows_rejected": 10,
        "corporate_action_terminal_payoffs": 3,
        "insolvency_terminal_payoffs": 1,
        "notes": [
            "AFT-U 2004와 AG1 2021 raw Short를 실제 Long으로 교정하되 raw flag를 보존했다.",
            "AFT-U와 AG-U를 ordinary common이 아닌 Canadian income-trust units로 분류했다.",
            "source SQL performance row가 10건 모두 부재해 exact total return·IRR을 생성하지 않았다.",
            "Arctic Glacier의 USD·CAD distributions는 지급일 FX 없이 합산하지 않았다.",
            "AUTO1 2027 target는 research cutoff 뒤이므로 milestone progress만 판정했다.",
            "같은 AGCO·AUTO1 회사라도 게시일·entry별 canonical idea unit와 payoff를 분리했다.",
        ],
    }
    payload["batch_lessons"] = [
        "business quality와 security entry price는 별도 판정축이다.",
        "보험·cyclical short는 diagnosis보다 catalyst clock·MAE·cover rule이 중요하다.",
        "income-trust yield와 enterprise FCF는 creditor claims 뒤 unit cash로 검증한다.",
        "installed base·TAM·market share를 cash margin으로 직접 번역하지 않는다.",
        "same company의 다른 vintage는 entry별 implied expectations를 다시 계산한다.",
        "mixed-currency distributions와 corporate actions는 dated ledger 없이 IRR을 만들지 않는다.",
        "future target는 horizon 전에는 milestone gap으로만 판정한다.",
    ]
    failure_patterns = {
        "amtrust": "catalyst_delay; reserve_opacity; capital_quality; adverse_excursion",
        "aft": "yield_trap; margin; payout_coverage; low_takeout",
        "zeiss": "duration; product_vs_earnings; mix; multiple_compression",
        "afya": "business_vs_stock; fx; country_discount; optionality",
        "agco": "cycle_call; liability_double_count; macro_offset; short_path",
        "arctic": "enterprise_vs_equity; refinancing; creditor_priority; mixed_currency",
        "auto1": "entry_price; sales_multiple; capital_intensity; target_duration",
        "algoma": "commodity_cycle; book_realizability; legacy_liabilities; single_asset",
    }
    success_patterns = {
        "amtrust": "reserve_audit; dated_catalyst; statutory_capital; cover_rule",
        "aft": "maintenance_capex; coverage; terminal_cash; downside_bid",
        "zeiss": "installed_base_bridge; procedure_economics; margin_stress; downside_multiple",
        "afya": "seat_cohorts; cash_conversion; fx_bridge; capital_allocation",
        "agco": "farm_income; normalized_earnings; finance_netting; cycle_scenarios",
        "arctic": "maturity_map; legal_cash; liquidation_waterfall; distribution_ledger",
        "auto1": "segment_gpu; capital_turns; sotp_floor; milestone_gates",
        "algoma": "new_capital_structure; deep_discount; normalized_spread; strategic_exit",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failure_patterns[idea["group"]]
        row["success_pattern_ko"] = success_patterns[idea["group"]]
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


add(
    id="9683c5d2-a736-4988-9af3-5a6fafadcbd5", date="2005-10-18", author="chris815", ticker="AG", company="AGCO Corporation", filename="analysis/ideas/2005/2005-10-18_AGCO_short.md", source="https://www.valueinvestorsclub.com/idea/AGCO_Corp/8174480323", group="agco", direction="Short", raw_direction="Short", security="NYSE:AGCO common equity / Short", entry="약 $16", horizon="12~24개월 rate·farm-cost pressure", raw_horizon="EV $2.6bn vs adjusted EV 약 $5bn; 86% variable-rate debt, higher LIBOR·energy·fertilizer",
    title="rates·leverage·farmer-cost AGCO Short", verdict="강한 실패 — ag upcycle이 leverage·rate headwind를 압도", score=1.8, process=4.8,
    conclusion="약 $16 short 뒤 2006말 약 $31, 2007말 약 $68로 올랐다. 86% variable-rate debt, higher LIBOR·energy·fertilizer는 실제 위험이었지만 farm income·commodity cycle, product mix와 operating leverage를 압도하지 못했다. 약 325% adverse price move는 명확한 trade failure다.",
    t0="headline EV 약 $2.6bn에 finance-company exposure와 pension·dealer financing 등을 더하면 adjusted EV가 약 $5bn이고, debt의 86%가 variable rate라 LIBOR 상승이 earnings를 훼손한다는 논지였다. energy·fertilizer 상승도 farmer 구매력을 낮춘다고 봤다.",
    reverse="시장은 높은 crop prices·farm income과 replacement demand가 장비 가격·volume을 끌어올리고 Fendt·Massey·Valtra franchise가 fixed-cost leverage를 만든다고 봤다. financing은 risk이면서 동시에 dealer/customer sales를 지탱하는 distribution asset이었다.",
    valuation="reported EV와 finance receivables·nonrecourse debt·JV guarantees를 무조건 합산하지 않고 exposure별 expected loss와 earnings contribution을 분리해야 한다. rate sensitivity와 farm-income upside를 EPS bridge에 함께 넣고 short의 stop/MAE를 정해야 한다.",
    actual="2005 sales는 $5.450bn으로 2004 $5.273bn 수준을 유지했다. 이후 agriculture upcycle, farm economics와 product demand가 강해지며 stock은 2006말 약 $31, 2007말 약 $68로 상승했다.",
    price="$16→$31은 약 93.8% adverse, $16→$68은 약 325% adverse price move다. short borrow·cover가 없으므로 exact realized P&L은 제시하지 않지만 thesis 실패 여부는 명확하다.",
    drivers="rate와 input-cost headwind보다 crop/farm cash-flow tailwind가 훨씬 컸다. adjusted EV 논리는 liabilities를 포착했지만 cyclic earnings power와 finance assets의 상쇄를 빠뜨렸다.",
    counterfactual="corn·soy prices와 farm income이 급등할 때 LIBOR +200bp가 장비 수요·pricing·margin에 주는 순효과는 정말 음수인가?",
    error="rate·fertilizer·leverage를 각각 독립된 negative로 더하고 모두 farmer demand와 company EPS를 같은 방향으로 움직인다고 가정했다. cycle bull case와 cover discipline이 없었다.",
    warning="2006 stock이 약 $31로 entry 대비 거의 두 배가 되고 sales·demand가 유지된 시점이 명확한 반증이자 cover 신호였다.", first_signal_date="2006-12-31",
    scenarios=[("Bear for short", "farm boom·pricing", "$30~70", "2006~07 실현"), ("Base", "rates offset demand", "$14~20", "미실현"), ("Bull for short", "farmer squeeze·credit stress", "$8~12", "미실현")],
    metrics=[("Entry / 2006", "$16", "하락", "~$31", "93.8% adverse"), ("2007 price", "entry 이하", "short profit", "~$68", "325% adverse"), ("2005 sales", "$5.45bn", "pressure", "$5.450bn", "안정"), ("Variable-rate debt", "86%", "interest shock", "cycle이 상쇄", "driver miss"), ("Adjusted EV", "~$5bn", "equity 압박", "distress 없음", "분류 오류")],
    timeline=[("2005-10-18", "VIC Short", "~$16"), ("2005-12-31", "sales $5.450bn", "수요 안정"), ("2006-H1", "rates·inputs 상승", "예상 headwind"), ("2006-H2", "farm-income 개선", "cycle offset"), ("2006-12-31", "stock ~$31", "cover signal"), ("2007-H1", "commodity boom", "equipment demand"), ("2007-H2", "operating leverage", "earnings rerating"), ("2007-12-31", "stock ~$68", "강한 실패")],
    lessons=["cyclical short는 cost headwind보다 customer cash-flow cycle을 먼저 본다.", "finance-company debt는 related assets·income·recourse를 함께 분류한다.", "여러 macro negatives를 더하기 전에 상관관계와 상쇄효과를 모델링한다.", "주가가 두 배가 되는 short에는 사전 cover rule이 있어야 한다."],
    checklist=["crop prices·farm income", "retail units·dealer inventory", "price/mix", "finance assets vs debt", "rate sensitivity", "gross margin", "working capital", "MAE·cover"],
    scorecard=sc("실패", "adjusted EV 과장", "rate catalyst 무효", "short 부적합", "강한 실패"),
    claims=[
        claim("adjusted EV 약 $5bn", "실패", "finance·pension 등을 더하면 headline $2.6bn보다 훨씬 비싸다.", "hidden claims가 equity의 enterprise cushion을 줄인다.", "원문 balance-sheet adjustments.", "claims가 recourse이고 상쇄 assets·income이 적다.", "finance book이 self-funding·profitable이면 약화.", "distress 없이 cycle을 통과하고 equity가 급등했다.", "terminal value 반증.", "gross liabilities를 EV에 중복 합산했다.", "recourse·assets·earnings을 net으로 분류한다."),
        claim("86% variable-rate debt", "mechanism 적중·trade 실패", "LIBOR 상승이 interest expense를 크게 높인다.", "floating debt×rate change가 pretax earnings를 낮춘다.", "원문 86% exposure.", "hedges·debt paydown·operating profit이 상쇄 못한다.", "EBIT growth가 interest를 압도하면 반증.", "rate headwind에도 stock은 $16→$68였다.", "price thesis 완전 반대.", "sensitivity를 total EPS bridge 없이 사용했다.", "EBIT·interest 동시 sensitivity를 만든다."),
        claim("energy·fertilizer가 farmer demand를 훼손", "실패", "input inflation이 equipment affordability를 낮춘다.", "farm margin 감소가 capex를 지연한다.", "당시 energy·fertilizer 상승.", "crop revenue가 cost 상승을 못 따라간다.", "crop prices·farm income 상승이면 반증.", "commodity boom이 equipment demand를 강화했다.", "direction 반대.", "cost만 보고 output price를 빠뜨렸다.", "farm gross margin을 통합 변수로 본다."),
        claim("sales·margin pressure", "실패", "macro·integration이 operating earnings를 낮춘다.", "lower units가 fixed-cost deleverage를 만든다.", "2005 cycle concern.", "dealer inventory가 높고 retail 약세다.", "sales·pricing·mix 개선이면 반증.", "2005 sales가 유지되고 이후 upcycle이 operating leverage를 만들었다.", "예상과 반대.", "cycle bottom을 연장했다.", "retail/wholesale와 inventory를 분리한다."),
        claim("valuation compression", "강한 실패", "높은 adjusted EV가 equity multiple을 낮춘다.", "earnings miss와 risk premium이 price를 누른다.", "$16 entry.", "cycle earnings가 늘지 않는다.", "$25 이상이면 반증.", "2006 ~$31, 2007 ~$68.", "+94%, +325% adverse.", "upside scenario가 없었다.", "short target과 max-loss를 함께 둔다."),
        claim("12~24개월 catalyst", "실패", "rates·input costs가 빠르게 실적에 반영된다.", "quarterly EPS misses가 rerating을 촉발한다.", "macro conditions.", "farm boom이 상쇄하지 않는다.", "2006 earnings·price 강세면 실패.", "2006말 주가가 거의 두 배였다.", "horizon 내 반증.", "macro exposure를 dated company catalyst로 봤다.", "catalyst에는 company-specific milestone이 필요하다."),
    ],
)


add(
    id="e8624dcd-69c5-47cd-a830-c21effa1e3d0", date="2009-08-27", author="PGTenny", ticker="AG-U", company="Arctic Glacier Income Fund", filename="analysis/ideas/2009/2009-08-27_AG_UN_long.md", source="", group="arctic", direction="Long", raw_direction="Long", security="Canadian income-trust units / Long", entry="C$1.72", horizon="refinancing·DOJ resolution 후 2~3년", raw_horizon="P/E 3.7x, TEV/EBITDA 5.3x, normalized EBITDA ~C$60m, ~50% equity FCF yield; C$5.40 value",
    title="high-FCF packaged-ice trust Long", verdict="강한 실패 — refinancing failure와 CCAA가 equity를 훼손", score=2.0, process=5.0,
    conclusion="route-density cash flow와 낮은 multiple을 샀지만 capital structure가 사업가치를 흡수했다. Fund는 2012-02-22 CCAA에 들어가 assets를 매각했다. 2015 US$0.155570, 2019 C$0.042818335, 2020 C$0.01427278, 2022 C$0.00549502의 distributions는 C$1.72 entry에 크게 못 미친다. 통화·날짜가 달라 exact IRR은 계산하지 않는다.",
    t0="normalized EBITDA 약 C$60m, 3.7x earnings·5.3x TEV/EBITDA와 약 50% equity FCF yield에 packaged-ice route network를 사는 thesis였다. DOJ plea, customer/shareholder suits와 refinancing이 해결되면 C$5.40 value로 rerate한다고 봤다.",
    reverse="시장은 leverage·debt maturity, antitrust fines·lawsuits, seasonality와 maintenance fleet capex가 apparent FCF를 채권자에게 귀속시킬 위험을 반영했다. equity FCF yield는 refinancing 전에는 distribution capacity가 아니라 residual claim의 숫자일 수 있었다.",
    valuation="C$60m EBITDA에서 normalized maintenance capex·cash interest·tax·seasonal working capital과 litigation cash를 빼고 maturity별 debt를 상환해야 한다. CCAA downside에서는 asset-sale proceeds를 secured creditors부터 배분한 뒤 unit recovery를 계산한다.",
    actual="예상과 달리 refinancing·legal overhang이 해소돼 common rerating으로 이어지지 않았다. 2012-02-22 CCAA가 개시되고 operating assets가 매각됐다. 잔여 estate가 여러 해에 걸쳐 소액 distributions를 지급한 뒤 2022 final distribution과 delisting으로 종료됐다.",
    price="verified distributions는 2015 US$0.155570, 2019 C$0.042818335, 2020 C$0.01427278, 2022 C$0.00549502/unit다. USD distribution의 지급일 FX와 기타 ledger가 없어 단순 합계·IRR은 만들지 않지만 C$1.72 principal recovery에 크게 미달한 것은 명확하다.",
    drivers="operating EBITDA보다 maturity wall, legal cash claims와 creditor priority가 payoff를 지배했다. route network의 economic value가 있어도 overleveraged trust units에는 residual이 거의 남지 않았다.",
    counterfactual="normalized EBITDA가 C$60m보다 20% 낮고 refinancing spread가 500bp 오르며 litigation cash가 즉시 나가도 units에 가치가 남는가?",
    error="enterprise-level FCF를 equity yield로 취급했고 debt maturity·seasonal liquidity·legal claims를 terminal waterfall보다 뒤에 놓았다.",
    warning="2012-02-22 CCAA filing이 definitive break였지만 그 전 debt maturity/refinancing 조건 악화가 더 이른 position-reduction 신호였다.", first_signal_date="2011-12-31",
    scenarios=[("Bear", "refi 실패·CCAA", "unit recovery <C$0.3", "실현"), ("Base", "DOJ settlement·refi", "C$3~4", "미실현"), ("Bull", "C$60m EBITDA·rerating", "C$5.40", "미실현")],
    metrics=[("Entry / target", "C$1.72 / C$5.40", "3.14x", "소액 distributions", "강한 실패"), ("Normalized EBITDA", "~C$60m", "유지", "creditor value로 귀속", "equity 실패"), ("TEV/EBITDA", "5.3x", "rerate", "CCAA", "multiple trap"), ("Equity FCF yield", "~50%", "cash recovery", "distribution 크게 미달", "실패"), ("Final distribution", "없음", "full recovery", "C$0.00549502", "residual 종료")],
    timeline=[("2009-08-27", "VIC Long", "C$1.72→C$5.40"), ("2010", "DOJ/legal process", "cash overhang"), ("2011", "refinancing pressure", "first warning"), ("2012-02-22", "CCAA filing", "thesis break"), ("2012", "operating assets sale", "creditor waterfall"), ("2015", "US$0.155570 distribution", "partial recovery"), ("2019~20", "C$0.042818335 + C$0.01427278", "residual distributions"), ("2022-11", "C$0.00549502 final·delist", "종료")],
    lessons=["distressed income trust는 EBITDA보다 debt maturity와 creditor waterfall을 먼저 본다.", "enterprise FCF yield를 equity distributable cash로 부르지 않는다.", "legal settlement와 refinancing을 독립된 cash claims·dates로 모델링한다.", "혼합통화 distributions는 지급일 FX 없이 단순 합산하지 않는다."],
    checklist=["debt maturity·covenant", "seasonal liquidity", "maintenance fleet capex", "cash interest", "legal claims", "refinancing spread", "secured waterfall", "distribution date·currency"],
    scorecard=sc("사업가치 존재", "multiple trap", "refi 실패", "residual unit 취약", "강한 실패"),
    claims=[
        claim("normalized EBITDA C$60m", "부분", "route network가 C$60m EBITDA를 번다.", "density와 local scale이 recurring cash earnings를 만든다.", "historical operations.", "legal·fuel·weather를 정상화할 수 있다.", "EBITDA 급락이면 반증.", "asset value는 있었지만 equity recovery로 전환되지 않았다.", "enterprise와 equity gap.", "EBITDA를 payoff로 등치했다.", "debt·capex 뒤 residual을 본다."),
        claim("TEV/EBITDA 5.3x", "실패", "stable route business에 낮은 multiple이다.", "legal/refi 해소 후 rerating된다.", "T0 enterprise valuation.", "debt가 refinance되고 EBITDA가 유지된다.", "CCAA 또는 forced sale이면 실패.", "2012 CCAA와 asset sale.", "multiple rerating 대신 insolvency.", "capital structure를 충분히 stress하지 않았다.", "maturity-adjusted EV와 liquidation EV를 함께 본다."),
        claim("~50% equity FCF yield", "강한 실패", "interest·capex 뒤 cash가 unit value 절반이다.", "cash accrual이 deleveraging·distribution을 만든다.", "원문 normalized cash bridge.", "현금이 covenant·legal reserve에 묶이지 않는다.", "distribution 중단·refi failure면 반증.", "units는 CCAA residual이 됐다.", "cash yield가 실현되지 않음.", "available cash와 equity-distributable cash를 혼동했다.", "restricted cash·maturity sweep을 반영한다."),
        claim("DOJ·lawsuits manageable", "실패", "settlements가 valuation overhang을 제거한다.", "known cash cost가 uncertainty discount를 줄인다.", "plea/settlement 기대.", "금액과 timing이 liquidity를 해치지 않는다.", "legal cash가 refinancing을 막으면 실패.", "overhang은 capital structure와 함께 CCAA path를 막지 못했다.", "catalyst가 구제가 되지 못함.", "legal resolution을 무조건 positive로 봤다.", "settlement cash·covenant 효과를 모델링한다."),
        claim("refinancing", "실패", "debt를 연장하면 equity duration이 살아난다.", "maturity extension이 normalized FCF realization 시간을 준다.", "lender negotiations.", "시장·lender가 acceptable terms를 준다.", "CCAA filing이면 반증.", "2012-02-22 CCAA.", "binary failure.", "refi probability와 downside recovery를 과대평가했다.", "maturity별 signed commitment만 base에 넣는다."),
        claim("C$5.40 value", "강한 실패", "normal multiple로 units가 3배 이상 오른다.", "C$60m EBITDA와 deleveraging이 equity를 만든다.", "explicit target.", "creditor claims 뒤 residual이 충분하다.", "recovery가 entry 이하이면 실패.", "verified later distributions는 entry에 크게 못 미쳤다.", "C$5.40 미실현·principal impairment.", "bull EV를 units에 직접 배분했다.", "waterfall과 dilution을 먼저 계산한다."),
    ],
)



add(
    id="25a41a32-cb61-4857-92a2-20d3d9d32c4c", date="2022-03-12", author="taiidea", ticker="AFX.GY", company="Carl Zeiss Meditec AG", filename="analysis/ideas/2022/2022-03-12_AFX_GY_long.md", source="", group="zeiss", direction="Long", raw_direction="Long", security="Xetra:AFX common equity / Long", entry="약 €151", horizon="2025 earnings realization", raw_horizon="base €263 / bull €514; VisuMax installed base, consumables와 premium IOL compounding",
    title="SMILE installed-base·premium-IOL Long", verdict="강한 실패 — product moat 생존, earnings duration·multiple 붕괴", score=3.0, process=6.8,
    conclusion="SMILE·VisuMax franchise와 recurring revenue 논리는 살아 있지만 원문의 earnings·margin·multiple 경로는 실패했다. FY2024/25 revenue €2.228bn에도 EBITA margin은 11.6%, EPS €1.61이었고 H1 FY2025/26 adjusted margin은 6.1%, EPS €0.17로 악화됐다. €151 entry에서 high-€20s 가격은 operating moat가 entry valuation을 구제하지 못했음을 보여준다.",
    t0="약 1,500대 VisuMax installed base와 SMILE procedure consumables, 신형 VisuMax 800 replacement cycle, premium IOL mix가 장기간 두 자릿수 성장과 높은 incremental margin을 만든다는 논지였다. sell-side가 order intake와 APAC adoption을 과소평가해 base €263, bull €514 rerating을 기대했다.",
    reverse="시장은 elective procedure·China/APAC 규제와 procurement, device order volatility, IOL product quality·mix, R&D 부담과 이미 높은 duration multiple을 할인했다. installed base가 커도 시술 utilization·consumable price와 device cycle이 동시에 둔화될 수 있다.",
    valuation="installed devices×procedures/device×consumable contribution과 equipment replacement, IOL units·mix를 각각 모델링하고 R&D·SG&A·tax·capex를 빼 EPS·FCF로 연결해야 한다. €263/€514 target는 earnings와 multiple 기여를 분리하고 15~20% margin 하방에서 stress했어야 한다.",
    actual="FY2024/25 revenue €2,227.6m, EBITA €257.7m, margin 11.6%, EPS €1.61, FCF €203.7m이었다. H1 FY2025/26 revenue €991.0m, adjusted EBITA €60.5m, margin 6.1%, EPS €0.17로 약해졌고 회사는 최대 1,000개 positions와 net savings >€160m p.a.를 포함한 구조조정을 제시했다. 9M adjusted margin은 8.0%였다.",
    price="약 €151에서 2026 high-€20s는 대략 80%+ price decline이다. exact trade date·dividends·tax ledger가 없으므로 total return·IRR은 계산하지 않는다.",
    drivers="product innovation보다 earnings duration과 entry multiple이 payoff를 지배했다. China·IOL mix·장비 투자둔화와 cost base가 recurring growth를 상쇄했고, market은 long-duration quality multiple을 재평가했다.",
    counterfactual="revenue가 늘어도 EBITA margin이 8~12%, EPS가 €1.5 안팎이면 €151 entry에서 어떤 terminal multiple이 손실을 막을 수 있었는가?",
    error="installed base와 clinical moat를 predictable earnings duration으로 곧바로 번역했고 downside valuation, product-quality/regulatory shock와 fixed-cost deleverage를 작게 봤다.",
    warning="FY2024/25 EPS가 €1.61에 그치고 EBITA margin이 11.6%로 내려간 시점이 base-case earnings path의 명확한 break였으며 H1 FY2025/26가 이를 확정했다.", first_signal_date="2025-12-11",
    scenarios=[("Bear", "China·IOL·device weakness, margin<10%", "€30~60", "high-€20s"), ("Base", "SMILE·IOL compounding", "€263", "미실현"), ("Bull", "VisuMax800·premium mix", "€514", "미실현")],
    metrics=[("Entry / base target", "€151 / €263", "+74%", "high-€20s", "강한 실패"), ("FY24/25 revenue", "고성장", "target path", "€2,227.6m", "scale 성장"), ("FY24/25 EBITA margin", "high-teens 기대", "확대", "11.6%", "미달"), ("FY24/25 EPS", "earnings compounding", "상승", "€1.61", "미달"), ("H1 FY25/26 adj margin", "회복", "mid/high teens", "6.1%", "반증")],
    timeline=[("2022-03-12", "VIC Long", "~€151"), ("2022", "VisuMax 800 rollout", "product catalyst"), ("2023", "China·device normalization", "duration pressure"), ("2024", "IOL/portfolio challenges", "mix risk"), ("2025-09-30", "FY2024/25 close", "margin 11.6%"), ("2025-12-11", "annual report", "EPS €1.61"), ("2026-05-12", "H1 results·restructuring", "adj margin 6.1%"), ("2026-08", "9M statement", "adj margin 8.0%")],
    lessons=["product moat와 entry-price moat는 별개다.", "installed base는 procedures/device·consumable contribution으로 풀어야 한다.", "high-duration medical devices에는 margin·multiple 동시 stress가 필요하다.", "company restructuring은 과거 earnings-quality 가정의 반증일 수 있다."],
    checklist=["VisuMax installed base", "procedures/device", "recurring mix", "IOL volume·recall", "China/APAC revenue", "gross·EBITA margin", "R&D ratio", "downside P/E·FCF"],
    scorecard=sc("product moat 부분 성공", "entry 실패", "upgrade cycle 실패", "common 적절", "강한 실패"),
    claims=[
        claim("SMILE razor-and-blade", "부분 성공", "VisuMax 설치가 procedure consumables를 누적한다.", "installed base×utilization이 recurring revenue와 high margin을 만든다.", "약 1,500대 installed base와 procedure model.", "utilization·pricing·clinical adoption이 계속 오른다.", "recurring mix·procedure growth가 정체되면 반증.", "H1 FY25/26 recurring revenue는 49.9%였으나 total earnings가 약화됐다.", "recurring mix 존재·profit 보호 실패.", "recurring을 recession-proof로 봤다.", "installed base와 utilization을 따로 추적한다."),
        claim("VisuMax 800 replacement cycle", "부분 성공", "빠른 신형 장비가 installed base 교체·확장을 촉진한다.", "throughput 개선이 surgeon ROI와 placements를 높인다.", "제품 출시·order intake.", "capital budgets와 approvals가 원활하다.", "device shipments·orders 약세면 반증.", "제품은 출시됐지만 2025/26 diagnostic device shipments가 계획보다 낮았다.", "product success≠forecast success.", "출시를 매출로 즉시 환산했다.", "orders·shipment·installation·utilization을 구분한다."),
        claim("premium IOL compounding", "실패", "premium mix와 APAC 수요가 성장·margin을 높인다.", "higher ASP lenses가 recurring surgical revenue를 키운다.", "portfolio와 demographic demand.", "tender·quality·channel risk가 낮다.", "recall·tender exclusion·mix 악화면 반증.", "2025/26 bifocal IOL tender exclusion·channel recall과 unfavorable mix가 earnings를 눌렀다.", "H1 adj margin 6.1%.", "product/regulatory downside를 과소평가했다.", "IOL는 country·tender·SKU별로 stress한다."),
        claim("multi-quarter earnings upgrades", "실패", "order intake가 consensus 상향을 부른다.", "backlog가 shipment와 EPS로 전환된다.", "당시 order book +24% vs revenue +11%.", "cancellations·mix·cost가 안정적이다.", "EPS·margin 하락이면 반증.", "FY24/25 EPS €1.61, H1 FY25/26 EPS €0.17로 악화됐다.", "upgrade가 아닌 downgrade path.", "orders를 margin-adjusted revenue로 연결하지 않았다.", "backlog conversion과 gross margin을 함께 본다."),
        claim("APAC가 절반 이상 성장엔진", "실패 구간", "Asia adoption이 company growth를 가속한다.", "SMILE·IOL penetration이 western maturity를 상쇄한다.", "APAC exposure와 underpenetration.", "China procurement·FX·regulation이 우호적이다.", "APAC decline이면 반증.", "H1 FY25/26 APAC revenue는 -10.0%(-8.6% FX-adjusted)였다.", "명확한 반증.", "TAM을 realized demand로 봤다.", "country별 volume·price·policy를 분리한다."),
        claim("€263 base / €514 bull", "강한 실패", "earnings growth와 premium multiple로 큰 upside가 난다.", "higher EPS×quality multiple이 target를 만든다.", "원문 valuation cases.", "margin이 확대되고 multiple이 유지된다.", "EPS·margin·price가 동시 하락하면 실패.", "주가는 high-€20s, margin·EPS도 미달했다.", "base 대비 약 -90% 수준.", "downside multiple과 duration을 과소평가했다.", "target를 earnings와 multiple bridge로 분해한다."),
    ],
)


add(
    id="fb1b28c2-534a-4321-a9a4-23b2782a5f8b", date="2022-01-13", author="om730", ticker="AFYA", company="Afya Limited", filename="analysis/ideas/2022/2022-01-13_AFYA_long.md", source="https://www.valueinvestorsclub.com/idea/AFYA_LTD/3795299111", group="afya", direction="Long", raw_direction="Long", security="Nasdaq:AFYA Class A common / Long", entry="약 $14.50", horizon="2025~2026 seat maturation", raw_horizon="2026 education FCF $175m, $28 core target; digital optionality $6+",
    title="Brazil medical-seat scarcity·digital option Long", verdict="운영 성공 / stock rerating 실패", score=6.8, process=7.8,
    conclusion="의대 seats scarcity와 tuition·M&A compounding은 작동했다. 2025 revenue R$3.697bn, adjusted EBITDA R$1.680bn, margin 45.4%, FCF R$1.056bn은 강한 운영 성과다. 그러나 2026 주가는 약 $13.5~13.7로 $14.5 entry와 비슷하거나 낮고 $28 target는 미실현이다. business success와 public-market payoff를 분리해야 한다.",
    t0="브라질 의대 공급규제와 interior-city scarcity, 이미 승인된 seats의 maturation·tuition escalator로 education revenue가 15%+ 성장하고 45% EBITDA margin·75% cash conversion을 유지한다는 논지였다. digital services는 현재 valuation에 거의 무료인 M3형 option으로 보았다.",
    reverse="시장은 Brazil regulation·currency·country risk, acquisition leverage·minority 구조와 digital integration을 할인했다. 높은 local-currency growth가 USD per-share value나 multiple rerating으로 자동 전환되지 않으며, regulated scarcity는 policy change에 취약하다.",
    valuation="core education의 R$ 또는 US$ FCF를 seat cohorts·FX·net debt·fully diluted shares에 맞춘 뒤 multiple을 적용해야 한다. digital은 users가 아니라 standalone revenue·margin·retention으로 별도 평가하고, core $28와 digital $6를 중복 없이 합산한다.",
    actual="2025 revenue R$3.697bn, adjusted EBITDA R$1.680bn, margin 45.4%, FCF R$1.056bn으로 core model의 질을 지지했다. acquisitions·seat maturation이 scale을 키웠지만 public-market multiple은 country·regulatory·capital-allocation risk를 계속 할인했다.",
    price="약 $14.50 entry와 2026 약 $13.5~13.7 비교는 price-only로 소폭 손실/정체다. buybacks·dividends·exact dates·FX가 완전하지 않아 total return·IRR은 제시하지 않는다.",
    drivers="local-currency cash flow는 성장했지만 USD listing의 multiple·FX·regulatory discount가 이를 상쇄했다. digital optionality도 core와 동급의 검증된 earnings engine으로 재평가되지 않았다.",
    counterfactual="core FCF가 계획대로 성장해도 Brazil risk premium과 FX가 30~40% 악화되면 $28 target에 도달할 수 있는가?",
    error="operating execution을 stock rerating과 가깝게 봤고 digital TAM·users를 standalone cash flow보다 앞세웠으며 FX·governance·capital allocation discount의 지속성을 낮게 잡았다.",
    warning="2025까지 EBITDA·FCF가 성장했는데도 주가가 entry 부근에 머문 사실이 multiple rerating claim의 명확한 반증이었다.", first_signal_date="2025-12-31",
    scenarios=[("Bear", "FX·regulation·multiple 6~8x", "$8~14", "entry 부근"), ("Base", "core 15% growth·15x FCF", "$28", "미실현"), ("Bull", "digital half-target", "$34+", "미실현")],
    metrics=[("Entry / core target", "$14.5 / $28", "+93%", "~$13.5~13.7", "rerating 실패"), ("2025 revenue", "2021 ~$290m equivalent base", "15%+ CAGR", "R$3.697bn", "운영 성공"), ("Adj EBITDA", "~45% margin", "유지", "R$1.680bn/45.4%", "성공"), ("FCF", "75% education EBITDA conversion", "강한 cash", "R$1.056bn", "성공"), ("Digital", "2026 $250m revenue case", "option value", "동급 scale 미확인", "미달")],
    timeline=[("2022-01-13", "VIC Long", "~$14.5"), ("2022", "seat·M&A expansion", "core growth"), ("2023", "tuition·campus maturation", "margin support"), ("2024", "cash flow·buyback focus", "capital allocation"), ("2025-12-31", "revenue R$3.697bn", "scale success"), ("2025-12-31", "adj EBITDA R$1.680bn", "45.4% margin"), ("2026-03", "FY2025 release", "FCF R$1.056bn"), ("2026-09-18", "stock entry 부근", "rerating failure")],
    lessons=["local-currency operating success와 USD-listed stock payoff를 분리한다.", "regulated scarcity에는 policy bear case를 명시한다.", "digital option은 users가 아니라 standalone cash conversion으로 평가한다.", "FCF 성장만으로 country-risk multiple이 정상화된다고 가정하지 않는다."],
    checklist=["approved seats", "occupancy", "tuition/mix", "mature-campus margin", "M&A price·earn-outs", "FCF conversion", "net debt", "BRL/USD·buybacks"],
    scorecard=sc("강한 성공", "stock target 실패", "seat maturation 성공", "common 적절", "혼합"),
    claims=[
        claim("medical-seat scarcity", "성공", "승인제약과 수요가 높은 occupancy·pricing을 지킨다.", "limited seats가 tuition과 campus utilization을 높인다.", "100%에 가까운 capacity와 regulation.", "신규 supply가 제한된다.", "occupancy·tuition 급락이면 반증.", "2025 revenue·margin 성장은 scarcity economics를 지지했다.", "margin 45.4%.", "policy stability를 당연시했다.", "seat awards·competitor supply·occupancy를 추적한다."),
        claim("education revenue 15%+ CAGR", "성공 방향", "awarded seats와 price로 education이 compound한다.", "seat cohorts가 maturation되며 revenue가 쌓인다.", "contracted expansion과 escalators.", "retention·occupancy·price가 유지된다.", "organic growth가 high-single digit 이하이면 약화.", "2025 group revenue R$3.697bn까지 성장했다.", "group/M&A mix 분리 제한.", "organic과 acquisition growth를 섞었다.", "seat cohort별 revenue bridge를 만든다."),
        claim("45% EBITDA margin", "성공", "education mix가 mid-40s margin을 유지한다.", "high utilization과 tax structure가 cash margin을 지지한다.", "mature campus economics.", "acquisition dilution·cost inflation이 통제된다.", "40% 아래 지속이면 실패.", "2025 adjusted EBITDA margin 45.4%.", "+0.4ppt vs 45% anchor.", "adjusted metric quality를 덜 stress했다.", "reported·adjusted·cash margin을 함께 본다."),
        claim("75% cash conversion", "성공 방향", "education EBITDA가 높은 FCF로 전환된다.", "low capex·tax benefits가 cash를 만든다.", "원문 75% assumption.", "interest·earn-outs·WC가 제한적이다.", "FCF/EBITDA가 60% 아래면 반증.", "2025 FCF R$1.056bn은 adj EBITDA의 약 62.9%였다.", "75% 대비 -12.1ppt, 절대액 강함.", "acquisition financing과 cash definitions 차이.", "FCF definition·earn-outs를 고정한다."),
        claim("digital services option", "미달", "2026 core의 절반 규모만 가도 $6/share 이상이다.", "education distribution이 physician apps의 CAC를 낮춘다.", "약 200k ecosystem users와 acquisitions.", "cross-sell·retention·30% margin이 실현된다.", "revenue·margin scale이 크게 미달하면 실패.", "2025까지 core와 동급 earnings engine으로 검증되지 않았다.", "원문 half-target 미확인.", "TAM·users를 monetization으로 번역했다.", "digital standalone P&L과 cohort retention을 본다."),
        claim("$28 core target", "실패", "2026 education FCF $175m×15x로 $28다.", "FCF compounding과 rerating이 주당가치를 높인다.", "entry ~$14.5, explicit target.", "FX·net debt·share count·multiple이 협조한다.", "2026 price가 entry 부근이면 실패.", "2026 약 $13.5~13.7.", "target 대비 약 -51%.", "operating success를 multiple success로 등치했다.", "FX·multiple·net debt attribution을 분리한다."),
    ],
)


add(
    id="a011f87e-a53e-43bc-9881-680d0941a8c2", date="2003-01-13", author="chris815", ticker="AG", company="AGCO Corporation", filename="analysis/ideas/2003/2003-01-13_AGCO_short.md", source="", group="agco", direction="Short", raw_direction="Short", security="NYSE:AGCO common equity / Short", entry="$21.74", horizon="2003~2005 integration·cycle", raw_horizon="90x TTM GAAP earnings, leverage·working capital·pension·Challenger integration",
    title="leveraged acquisition-cycle AGCO Short", verdict="중기 부분 성공 / 장기 thesis 실패", score=5.5, process=6.5,
    conclusion="$21.74 short는 2005말 약 $16.6에서 약 24% favorable price move를 보였다. 그러나 AGCO sales는 2003 $3.495bn에서 2004 $5.273bn, 2005 $5.450bn으로 커졌고 2007말 주가는 약 $68까지 상승했다. valuation·balance-sheet concern은 중기 trade에 일부 맞았지만 enduring business failure thesis는 틀렸다.",
    t0="90x TTM GAAP earnings, 높은 debt와 finance JV·working capital, underfunded pension, Caterpillar Challenger integration cost 때문에 acquisitions가 earnings quality와 liquidity를 악화시킨다는 short였다. agricultural equipment weakness가 deleveraging을 막는다고 봤다.",
    reverse="시장은 Challenger·Valtra 등 product portfolio와 dealer network가 sales·scale·parts economics를 키우고 cycle 회복이 fixed cost와 debt를 빠르게 흡수한다고 봤다. trailing GAAP P/E는 restructuring·integration trough 때문에 과장될 수 있었다.",
    valuation="TTM GAAP P/E보다 normalized EBIT by region/product, finance-JV exposure, pension cash, working capital과 net debt를 써야 한다. short payoff는 2005 target뿐 아니라 2007 cycle upside와 stop/cover rule을 포함해야 한다.",
    actual="AGCO net sales는 2003 $3.495bn, 2004 $5.273bn, 2005 $5.450bn으로 증가했다. 2005말 주가는 약 $16.6로 entry 아래였으나 agriculture upcycle과 integration 뒤 2007말 약 $68로 올랐다.",
    price="$21.74→$16.6은 short에 price-only 약 +23.6% favorable다. 계속 보유해 $68을 맞으면 약 212.8% adverse move다. borrow·cover ledger가 없어 realized return은 특정하지 않는다.",
    drivers="중기에는 integration·earnings noise와 valuation compression이 작동했지만 장기에는 sales scale, product breadth와 farm-cycle operating leverage가 압도했다.",
    counterfactual="trailing earnings가 trough이고 sales가 50% 늘어날 때도 90x P/E가 유효한 short valuation 지표인가?",
    error="trailing GAAP denominator와 balance-sheet static view에 의존했고 acquisition 뒤 revenue·margin synergy와 cycle-up operating leverage를 충분히 확률가중하지 않았다.",
    warning="2004 sales가 $5.273bn으로 50% 이상 늘고 integration이 매출기반을 확대했다는 공시는 terminal-failure thesis의 최초 반증이었다.", first_signal_date="2004-12-31",
    scenarios=[("Bear for short", "integration·cycle 성공", "$40~70", "2007 ~$68"), ("Base", "earnings pressure", "$15~20", "2005 ~$16.6"), ("Bull for short", "liquidity/pension stress", "$10 이하", "미실현")],
    metrics=[("Entry / 2005", "$21.74", "하락", "~$16.6", "short +23.6% price-only"), ("2003 sales", "$3.495bn", "weak", "$3.495bn", "base"), ("2004 sales", "integration risk", "압박", "$5.273bn", "thesis 반대"), ("2005 sales", "cycle 약세", "감소", "$5.450bn", "thesis 반대"), ("2007 price", "downside 지속", "entry 이하", "~$68", "장기 실패")],
    timeline=[("2003-01-13", "VIC Short", "$21.74"), ("2003-12-31", "sales $3.495bn", "base year"), ("2004", "Challenger·Valtra scale", "integration 진행"), ("2004-12-31", "sales $5.273bn", "business break"), ("2005-12-31", "sales $5.450bn", "scale 유지"), ("2005-12-31", "stock ~$16.6", "중기 short 이익"), ("2006", "ag cycle 강화", "cover signal"), ("2007-12-31", "stock ~$68", "장기 thesis 실패")],
    lessons=["trailing GAAP P/E가 높은 이유가 trough charges인지 먼저 분해한다.", "acquisition leverage와 acquired earning power를 같은 pro forma에 넣는다.", "중기 price win과 장기 business thesis를 분리한다.", "cyclical short는 cover rule과 upside cycle scenario가 필수다."],
    checklist=["organic vs acquired sales", "dealer inventory", "normalized EBIT", "working capital", "finance JV exposure", "pension cash", "net debt", "cover·MAE"],
    scorecard=sc("장기 실패", "중기 일부 적중", "distress 미실현", "short path 취약", "부분 성공 후 실패"),
    claims=[
        claim("90x TTM GAAP P/E", "중기 성공·분모 오류", "valuation이 극단적으로 높다.", "earnings normalization이나 multiple compression이 price를 낮춘다.", "T0 trailing GAAP earnings.", "earnings가 trough가 아니다.", "normalized EPS 급증이면 반증.", "2005까지 주가는 약 24% 하락했지만 이후 earnings/cycle로 크게 상승했다.", "중기 hit·장기 miss.", "trough denominator를 정상 earnings로 봤다.", "reported·normalized·cycle EPS를 나눈다."),
        claim("debt·finance JV risk", "실패", "차입과 off-balance-sheet financing이 equity를 압박한다.", "판매둔화가 receivable·funding loss로 번진다.", "debt와 Rabobank JVs.", "credit access가 악화된다.", "sales·funding이 확대되면 반증.", "회사는 sales를 확대하고 distress 없이 cycle을 통과했다.", "default catalyst 미실현.", "gross exposure를 expected loss로 오인했다.", "JV receivables·loss-sharing·liquidity를 모델링한다."),
        claim("working-capital squeeze", "부분", "inventory·receivables가 cash를 흡수한다.", "dealer demand 약화가 cash conversion을 나쁘게 한다.", "cyclical equipment balance sheet.", "inventory turns가 악화한다.", "growth와 funding이 cash need를 흡수하면 약화.", "scale-up 과정의 cash need는 있었지만 terminal stress는 없었다.", "정확한 short catalyst 부족.", "seasonal WC를 structural insolvency와 혼동했다.", "quarterly turns와 committed liquidity를 본다."),
        claim("pension 부담", "부분", "underfunded pension이 equity cash를 소모한다.", "contributions가 deleveraging·EPS를 제한한다.", "T0 benefit obligations.", "funding gap·rates가 악화한다.", "contribution이 cash flow 대비 작으면 약화.", "pension은 drag였지만 cycle upside를 막지 못했다.", "price driver로는 2차적.", "liability 존재와 catalyst를 혼동했다.", "5년 cash contribution schedule로 본다."),
        claim("Challenger integration 실패", "실패", "인수 통합비용·dealer conflict가 value를 훼손한다.", "중복비용과 channel disruption이 margin을 누른다.", "Caterpillar deal transition.", "sales synergy가 제한된다.", "sales·portfolio가 크게 확대되면 반증.", "2004~05 sales가 $5.3~5.45bn으로 확대됐다.", "2003 대비 +56% in 2005.", "cost만 보고 acquired revenue를 덜 봤다.", "cost·revenue·working capital synergy를 함께 본다."),
        claim("ag equipment weakness 지속", "실패", "industry weakness가 earnings를 계속 누른다.", "farmer income·replacement delay가 unit demand를 낮춘다.", "당시 weak conditions.", "commodity/farm cycle이 회복하지 않는다.", "farm income·stock 급등이면 반증.", "2006~07 ag upcycle과 stock ~$68가 반증했다.", "entry 대비 +213% adverse.", "cycle mean reversion을 배제했다.", "short에는 crop-price·farm-income bull case를 둔다."),
    ],
)



add(
    id="310ba840-8c00-4893-b2d7-cb15dc6678a9", date="2004-11-18", author="dylex849", ticker="AFT-U", company="Advanced Fiber Technologies Income Fund", filename="analysis/ideas/2004/2004-11-18_AFT_UN_long.md", source="", group="aft", direction="Long", raw_direction="Short", security="Canadian income-trust units / Long", entry="약 C$5.50", horizon="1~3년 distribution·rerating", raw_horizon="C$0.60/unit distribution, 약 11% yield, cost savings와 M&A",
    title="replacement-niche income-trust Long", verdict="실패 — C$3.00 takeout가 capital loss를 확정", score=3.0, process=5.5,
    conclusion="raw Short를 실제 income-trust unit Long으로 교정했다. 85~90% replacement demand와 약 30% global share, C$0.60 distribution은 매력적이었지만 margin·competition을 견디지 못했고 2006 Aikawa가 C$3.00/unit에 인수했다. distributions가 손실을 줄여도 C$5.50 entry를 회복했다는 complete ledger는 없다.",
    t0="약 C$118m EV와 2004E EBITDA C$16.2m, C$0.60/unit annual distribution, 약 11% yield에 niche replacement franchise를 샀다. installed paper machines의 wear parts는 생산량보다 교체주기에 좌우되고 cost savings·distribution increase·M&A가 upside catalyst였다.",
    reverse="시장은 small-cap trust의 customer concentration, pricing competition, metal input·currency, payout의 maintenance capex coverage와 sponsor/manager quality를 할인했다. high replacement share가 곧 pricing power나 stable EBITDA를 뜻하지 않았다.",
    valuation="C$16.2m EBITDA에서 cash tax·maintenance capex·working capital·interest를 차감해 distributable cash/unit를 만든 뒤 C$0.60 payout coverage를 봐야 한다. headline 11% yield를 bond coupon처럼 보지 않고 terminal C$3 cash와 실제 distribution dates를 합산한다.",
    actual="운영 압력과 낮은 public-market value 뒤 Aikawa가 2006 fund를 인수해 private ownership으로 돌렸다. verified consideration은 C$3.00/unit였다. 정확한 interim distributions와 tax ledger가 완전하지 않아 total return·IRR을 만들지 않는다.",
    price="C$5.50→C$3.00은 terminal price-only 0.545x, -45.5%다. C$0.60 annual distribution이 일부 기간 지급됐더라도 지급일·삭감·세금의 complete ledger 없이 손실을 임의로 상쇄하지 않는다.",
    drivers="replacement demand는 매출 floor를 줬지만 pricing·margin·capital intensity와 낮은 exit price를 막지 못했다. income security의 핵심은 yield가 아니라 payout after maintenance capex와 terminal capital value였다.",
    counterfactual="EBITDA가 25% 줄고 maintenance capex와 working capital이 두 배가 되어도 C$0.60 distribution과 C$5.50 unit value가 유지되는가?",
    error="market share·replacement 비중을 stable margin으로 번역했고, trust payout를 사업가치와 별개인 안전한 carry처럼 취급했다.",
    warning="distribution 증가가 아니라 낮은 C$3 bid가 나온 2006 takeover terms는 intrinsic value와 payout sustainability에 대한 최종 반증이었다.", first_signal_date="2006-03",
    scenarios=[("Bear", "margin 압박·payout cut", "C$2.5~3.5", "C$3 bid"), ("Base", "C$16m EBITDA·C$0.60 payout", "C$5~6", "미실현"), ("Bull", "cost savings·M&A premium", "C$7+", "미실현")],
    metrics=[("Entry / takeout", "C$5.50", "rerating", "C$3.00", "-45.5% price-only"), ("2004E EBITDA", "C$16.2m", "stable/grow", "takeout value 낮음", "미달"), ("Distribution", "C$0.60", "증가", "complete ledger 없음", "미확정"), ("Yield", "~11%", "carry", "capital loss 우세", "실패"), ("Replacement mix", "85~90%", "defensive", "margin 방어 불충분", "부분")],
    timeline=[("2004-11-18", "VIC Long", "raw Short 교정"), ("2004", "C$16.2m EBITDA estimate", "valuation base"), ("2005-H1", "replacement demand 지속", "business support"), ("2005-H2", "margin·pricing pressure", "coverage risk"), ("2006-03", "Aikawa bid", "C$3 terminal value"), ("2006", "unitholder approval process", "cash exit"), ("2006", "acquisition close", "public trust 종료"), ("2026-09-18", "ledger audit", "exact IRR 보류")],
    lessons=["income trust는 yield보다 maintenance capex 뒤 distribution coverage를 먼저 본다.", "replacement 비중이 높아도 pricing power와 customer bargaining을 따로 검증한다.", "M&A는 upside가 아니라 낮은 terminal bid가 될 수도 있다.", "interim distributions가 불완전하면 exact total return을 만들지 않는다."],
    checklist=["installed base", "replacement frequency", "price/mix", "gross margin", "maintenance capex", "working capital", "distribution coverage", "bid terms·cash ledger"],
    scorecard=sc("niche 일부 유효", "entry 과대", "M&A 역방향", "trust unit 정확", "실패"),
    claims=[
        claim("85~90% replacement demand", "부분 성공", "sales 대부분이 필수 교체수요다.", "wear parts가 paper output보다 installed base에 연동된다.", "원문 replacement mix.", "교체주기·가격이 안정적이다.", "volume 또는 price 급락이면 반증.", "사업은 인수될 만큼 존속했지만 unit value를 지키지 못했다.", "demand floor≠margin floor.", "수요 안정성을 이익 안정성으로 봤다.", "volume·price·gross margin을 분리한다."),
        claim("global share 약 30%", "실패에 가까움", "규모·기술이 높은 margin을 보호한다.", "qualification·installed knowledge가 switching cost를 만든다.", "원문 market share estimate.", "경쟁자가 가격을 깨지 못한다.", "margin erosion·low bid면 반증.", "C$3 takeout는 durable excess return 기대를 지지하지 못했다.", "entry 대비 -45.5% terminal.", "share를 moat로 자동 변환했다.", "share와 incremental gross margin을 함께 본다."),
        claim("2004E EBITDA C$16.2m", "미달", "earnings가 안정돼 valuation을 지지한다.", "replacement volume과 cost actions가 EBITDA를 유지한다.", "T0 estimate와 C$118m EV.", "cash conversion이 높다.", "payout pressure 또는 low EV bid면 반증.", "takeout economics는 T0 earnings 지속가치를 크게 낮게 평가했다.", "직접 FY bridge 제한.", "forecast를 distributable cash로 잇지 않았다.", "EBITDA-to-cash bridge를 필수화한다."),
        claim("C$0.60 distribution", "부분·ledger 제한", "annual distribution이 기다림을 보상한다.", "distributable cash가 unit payout을 커버한다.", "원문 payout과 11% yield.", "maintenance capex·WC 후 coverage>1x.", "cut·borrowed distribution이면 실패.", "일부 distributions 가능하나 complete ledger가 없다.", "terminal capital loss C$2.50/unit.", "yield를 downside floor로 오인했다.", "payout source와 balance-sheet cost를 본다."),
        claim("cost savings", "실패", "운영 개선이 margin과 payout를 높인다.", "procurement·plant efficiency가 unit cost를 낮춘다.", "management initiatives.", "savings가 price pressure보다 크다.", "EBITDA·distribution 미개선이면 반증.", "최종 C$3 bid는 의미 있는 rerating을 만들지 못했음을 보여준다.", "C$5.50 value 미회복.", "gross savings에 실행확률을 과대 적용했다.", "owner·deadline·cash cost를 명시한다."),
        claim("M&A upside", "역방향 실현", "strategic interest가 premium을 만든다.", "buyer synergy가 standalone value보다 높은 bid를 허용한다.", "niche global footprint.", "bid가 entry보다 높다.", "entry 아래 bid면 실패.", "Aikawa가 C$3.00/unit에 인수했다.", "entry 대비 -C$2.50/-45.5% before payouts.", "M&A existence와 premium을 혼동했다.", "strategic value는 buyer economics와 downside bid로 stress한다."),
    ],
)


if __name__ == "__main__":
    main()
