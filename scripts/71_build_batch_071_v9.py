#!/usr/bin/env python3
"""Build Batch 071 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-19"
CATALOG = ROOT / "data/curated/batch_071_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_071_agc_agc1_agco_agfx_agfy_agi_deep_v7.json"

spec = importlib.util.spec_from_file_location("batch64_base", ROOT / "scripts/64_build_batch_064_v9.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "agc_cef": (
        "AGC는 convertible securities와 non-convertible income securities를 보유하고 covered calls를 병행한 leveraged closed-end fund였다. "
        "보통주는 portfolio NAV에서 leverage와 비용을 부담한 residual claim이며, 거래가격은 NAV와 별개로 할인·할증된다. 따라서 수익은 underlying NAV, "
        "분배금, 할인율 변화와 tender·합병 같은 구조적 촉매의 합이다."
    ),
    "agf_credit": (
        "American General Finance와 후신 Springleaf Finance는 branch 기반 consumer finance lender였다. 높은 수익률의 personal·retail·real-estate receivables에서 "
        "credit loss, servicing cost와 funding cost를 차감해 unsecured debt service를 만든다. 채권자는 common upside가 아니라 만기별 coupon·principal과 secured·structural "
        "subordination 뒤 recovery를 산다."
    ),
    "agco": (
        "AGCO는 Massey Ferguson·Fendt·Valtra 등 농기계와 parts를 dealer망에 판매한다. farmer income, crop price, 금리와 dealer inventory가 unit demand를 만들고, "
        "price/mix·factory utilization·material cost·working capital과 finance JV가 주당 현금을 결정한다. cycle trough에서의 생존력과 정상화 margin을 분리해야 한다."
    ),
    "argentex": (
        "Argentex는 기업·기관 고객에게 spot FX, forwards, options와 international payments를 제공했다. fixed asset과 capex는 적지만 client collateral 부족, prime broker·bank "
        "margin calls와 settlement timing 때문에 급격한 시장변동 시 큰 단기유동성이 필요하다. 정상시 높은 margin과 stress시 liquidity capital을 함께 모델링해야 한다."
    ),
    "agrify": (
        "Agrify는 cannabis cultivator에게 Vertical Farming Units, extraction equipment, software와 Total Turn-Key 프로젝트를 제공했다. TTK는 고객 construction financing, "
        "equipment sale와 장기 service·production fee를 결합했으므로 SaaS가 아니라 vendor finance·project execution·customer credit가 섞인 모델이었다."
    ),
    "alliance": (
        "Alliance Gaming은 slot machines, casino-management systems와 participation games를 공급했고 2006년 Bally Technologies로 이름을 바꿨다. 기기 판매 외에도 installed base, "
        "replacement cycle와 shared-revenue games가 recurring cash를 만들지만, 2000년 common은 큰 debt·interest burden 뒤의 매우 convex한 residual claim이었다."
    ),
    "alamos": (
        "Alamos Gold는 금광을 개발·운영한다. 생산량×realized gold price에서 mining·processing cost, royalties, sustaining·growth capex와 세금을 뺀 현금이 가치의 핵심이다. "
        "개발자산 NAV에는 permit·financing·construction·start-date probability를, 가동광산에는 grade·throughput·reserve replacement와 bottleneck removal을 적용한다."
    ),
}

ENGINE = {
    "agc_cef": "`common return = NAV return + distributions + discount change - leverage/expense drag`; 분배금 중 return of capital과 NAV-for-NAV corporate action을 따로 기록한다.",
    "agf_credit": "`receivable collections - credit losses - opex - secured funding cost = unsecured debt capacity`; maturity별 coupon·exchange·repurchase·principal cash flow를 추적한다.",
    "agco": "`units × price/mix + parts - materials/labour/warranty - SG&A/R&D - tax - capex ± working capital = equity cash`; finance exposure와 cycle multiple을 분리한다.",
    "argentex": "`client flow × spread + interest income - staff/tech/compliance cost - credit loss - liquidity buffer cost = equity cash`; stressed collateral need를 excess cash에서 먼저 차감한다.",
    "agrify": "`hardware gross profit + recurring fees - customer-financing loss - project overruns - opex - capex = equity cash`; nominal contract value가 아니라 collected cash와 gross margin으로 검증한다.",
    "alliance": "`equipment margin + participation/system recurring cash - interest - capex ± working capital = residual equity cash`; enterprise improvement가 debt hurdle을 넘을 때 common convexity가 커진다.",
    "alamos": "`ounces × realized gold price - cash cost - sustaining capex - growth capex - tax = equity cash`; project NPV, operating FCF와 gold beta를 별도 claim으로 관리한다.",
}

KPI = {
    "agc_cef": "NAV/share, market price, discount/premium, NAV·market total return, distribution composition, leverage ratio/cost, expense ratio, Level 1/2/3 mix, tender acceptance, merger ratio",
    "agf_credit": "receivable balance, 60+ delinquency, charge-off, reserve coverage, cash, unencumbered assets, secured/unsecured debt, maturity wall, securitization yield, exchange/repurchase price",
    "agco": "retail units, dealer inventory, crop/farmer income, sales, price/mix, gross·operating margin, working capital, finance receivables, net debt, EPS/share count",
    "argentex": "client count/flow, revenue, operating margin, net cash, client collateral, margin-call liquidity, bank facilities, counterparty concentration, stress VaR, suspended balances",
    "agrify": "VFU/TTK units, contract cash collected, customer loans, revenue, gross margin, backlog conversion, receivable reserve, operating cash burn, liquidity, dilution/reverse splits",
    "alliance": "machine shipments, installed base, participation units, recurring revenue, EBITDA, interest coverage, net debt, replacement orders, tribal gaming exposure, strategic consideration/share",
    "alamos": "production ounces, grade, recovery, throughput, cash cost/AISC, sustaining/growth capex, mine-site FCF, reserves/resources, net cash/debt, permit and commissioning dates",
}


SOURCES = {
    "agc_cef": [
        S("AGC/AVK 2017 tender final results", "https://www.sec.gov/Archives/edgar/data/1391461/000139146117000002/avkagctenderfinalresultspr.htm", "SEC / Guggenheim", "2017-09-12", "AGC 15% tender, oversubscription, 33% proration과 $6.4876/98% NAV purchase price 검증."),
        S("AGC/LCM-to-AVK merger proxy", "https://www.sec.gov/Archives/edgar/data/1219120/000089180418000253/gug74131-497.htm", "SEC / Guggenheim", "2018-05-29", "NAV-for-NAV merger 구조, expense-ratio savings와 shareholder vote 검증."),
        S("AVK report and completed mergers", "https://www.sec.gov/Archives/edgar/data/1219120/000089180419000224/gug76254-ncsr.htm", "SEC / Guggenheim", "2019", "2018-08-27 completion, AGC NAV $6.36과 AVK conversion ratio 0.36302760 검증."),
    ],
    "agf_credit": [
        S("AIG/Fortress AGF transaction announcement", "https://www.sec.gov/Archives/edgar/data/25598/000134100410001987/ex99-1.htm", "SEC / AIG", "2010-08-11", "Fortress affiliate의 AGF 80% acquisition agreement 검증."),
        S("Springleaf Finance 2010 Form 10-K", "https://www.sec.gov/Archives/edgar/data/25600/000002560011000014/inc1210.htm", "SEC / Springleaf", "2011-03-31", "2010-11-30 Fortress 80% closing, company lineage, cash·receivables·debt와 going-concern context 검증."),
        S("2013 Springleaf exchange and notes", "https://www.sec.gov/Archives/edgar/data/25598/000110465913072173/a13-20760_58k.htm", "SEC / Springleaf", "2013-09-25", "$700m 2017 notes exchange, 2021/2023 notes와 약 $184m cash repurchase 계획 검증."),
        S("2017 Springleaf note repurchase", "https://www.sec.gov/Archives/edgar/data/25598/000104746917003674/a2232287z424b5.htm", "SEC / OneMain", "2017-05-25", "약 $466m 6.90% 2017 notes repurchase와 refinancing 조건 검증."),
    ],
    "agco": [
        S("AGCO 2019 Form 10-K", "https://www.sec.gov/Archives/edgar/data/880266/000088026620000006/a2019agco10-k.htm", "SEC / AGCO", "2020-02", "2018·2019 sales와 operating income, regional/cycle results 검증."),
        S("AGCO SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=880266&owner=exclude", "SEC / AGCO", "2015-2020", "buybacks, balance sheet와 multi-year annual filings 교차검증."),
    ],
    "argentex": [
        S("IFX recommended acquisition of Argentex", "https://data.fca.org.uk/artefacts/NSM/RNS/5630285.html", "UK National Storage Mechanism / IFX·Argentex", "2025-04-25", "2.49p cash offer, 약 £3m equity value, £6.5m bridge, margin-call liquidity deterioration와 suspension 검증."),
    ],
    "agrify": [
        S("Agrify 2022 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1800637/000121390023090353/f10k2022_agrify.htm", "SEC / Agrify", "2023-11", "2021·2022 revenue, gross loss, operating cost, $69.9m impairment와 customer-financing reserves 검증."),
        S("Agrify 2023 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1800637/000121390024033048/ea0203682-10k_agrify.htm", "SEC / Agrify", "2024-04", "2023 revenue contraction, liquidity·debt·dilution 경로 검증."),
        S("2022 1-for-10 reverse split", "https://www.sec.gov/Archives/edgar/data/1800637/000121390022064269/ea167213ex99-1agrifycorp.htm", "SEC / Agrify", "2022-10-17", "첫 reverse split과 Nasdaq minimum-bid 목적 검증."),
        S("2023 1-for-20 reverse split", "https://www.sec.gov/Archives/edgar/data/1800637/000121390023053790/ea181262ex99-1_agrify.htm", "SEC / Agrify", "2023-07-03", "두 번째 reverse split과 share-count 변화 검증."),
        S("2024 1-for-15 reverse split", "https://www.sec.gov/Archives/edgar/data/1800637/000121390024085199/ea0216705-8k_agrify.htm", "SEC / Agrify", "2024-10-04", "세 번째 reverse split과 continued-listing 목적 검증."),
        S("Green Thumb secured financing", "https://www.sec.gov/Archives/edgar/data/1800637/000121390024094613/ea022010001ex99-1_agrify.htm", "SEC / Agrify", "2024-11-05", "최대 $20m secured convertible note, 첫 $10m draw와 leadership change 검증."),
    ],
    "alliance": [
        S("Alliance Gaming name change", "https://www.sec.gov/Archives/edgar/data/2491/000110465906032286/a06-11460_18k.htm", "SEC / Bally Technologies", "2006-05-08", "Alliance Gaming Corporation에서 Bally Technologies로의 사명변경 검증."),
        S("Scientific Games/Bally merger agreement", "https://www.sec.gov/Archives/edgar/data/2491/000110465914056205/a14-18280_28k.htm", "SEC / Bally Technologies", "2014-08-04", "$83.30 cash/share merger consideration 검증."),
        S("Scientific Games completes Bally acquisition", "https://www.sec.gov/Archives/edgar/data/2491/000110465914083450/a14-25061_28k.htm", "SEC / Bally Technologies", "2014-11-21", "거래 종결, $83.30 cash/share와 약 $3.2bn total consideration 검증."),
    ],
    "alamos": [
        S("Alamos FY2018 results", "https://www.alamosgold.com/news-and-events/news/news-details/2019/Alamos-Reports-Fourth-Quarter-and-Year-End-2018-Results/default.aspx", "Alamos Gold", "2019-02-20", "2018 production 505koz, debt-free balance sheet, cash $206m과 operating context 검증."),
        S("Young-Davidson lower-mine completion", "https://www.alamosgold.com/news-and-events/news/news-details/2020/Alamos-Gold-Announces-Completion-of-Lower-Mine-Expansion-at-Young-Davidson-Mine/default.aspx", "Alamos Gold", "2020-07", "Northgate shaft·crusher/conveyor commissioning과 약 8,000 tpd design path 검증."),
        S("Alamos 2020 reserves and resources", "https://www.alamosgold.com/news-and-events/news/news-details/2021/Alamos-Gold-Reports-Mineral-Reserves-and-Resources-for-the-Year-Ended-2020/default.aspx", "Alamos Gold", "2021", "Island Gold reserves가 2017 acquisition 이후 depletion 순감 후 74% 증가했음을 검증."),
        S("Alamos FY2025 results", "https://www.alamosgold.com/news-and-events/news/news-details/2026/Alamos-Gold-Reports-Fourth-Quarter-and-Year-End-2025-Results/", "Alamos Gold", "2026-02", "2025 production 545.4koz, free cash flow $351.7m과 mine별 cash generation 검증."),
        S("Alamos Q1 2026 results", "https://www.alamosgold.com/news-and-events/news/news-details/2026/Alamos-Gold-Reports-First-Quarter-2026-Results/default.aspx", "Alamos Gold", "2026-04-29", "Q1 FCF $101.7m, net cash·liquidity와 operating follow-through 검증."),
    ],
}


IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


def claim(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson):
    return C(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson)


def scorecard(business, valuation, catalyst, security, timing):
    return [("Business thesis", business), ("Valuation thesis", valuation), ("Catalyst thesis", catalyst), ("Security payoff", security), ("Timing / path", timing)]


add(
    id="debdba95-f3d2-4ac6-a115-22fd561777e4", date="2016-01-17", author="jcoviedo", ticker="AGC",
    company="Advent Claymore Convertible Securities and Income Fund II", filename="analysis/ideas/2016/2016-01-17_AGC_closed_end_fund_long.md",
    source="https://www.valueinvestorsclub.com/idea/ADVENT_CLAYMORE_CV_SECandIN_II/1392331342", group="agc_cef", direction="Long", raw_direction="Short",
    security="NYSE:AGC leveraged closed-end-fund common shares / Long", entry="NAV 대비 약 18.95% 할인", horizon="1~3년 discount closure와 distributions",
    raw_horizon="liquid marked portfolio, 월 $0.047 distribution, activist/tender·liquidation optionality",
    title="liquid-NAV discount·catalyst CEF Long", verdict="강한 성공 — 할인 축소·tender·NAV merger 실현", score=9.2, process=8.8,
    conclusion="대부분 Level 1/2인 portfolio를 약 18.95% 할인에 산 thesis였다. FY2017 말 할인은 약 8%로 줄었고, 2017년 15% tender와 2018년 AVK NAV-for-NAV 합병이 이어졌다. 분배금의 return-of-capital과 leverage 위험을 감안해도 discount catalyst는 명확히 적중했다.",
    t0="AGC는 convertibles·high yield를 보유했지만 보통주는 NAV보다 약 18.95% 낮게 거래됐다. 월 $0.047 distribution은 약 11.4% headline yield를 제공했고, 투자자 activism·tender·liquidation이 discount를 닫을 선택지였다. investments가 net assets의 약 174.5%로 leverage가 높다는 점이 핵심 반대항이었다.",
    reverse="시장은 credit-sensitive assets, expensive leverage, covered-call drag, management fee와 distribution 중 return of capital을 할인했다. 즉 19% discount가 공짜가 아니라 NAV 변동성과 지속적으로 소모될 수 있는 분배정책의 가격일 수 있었다.",
    valuation="CEF common은 headline yield가 아니라 `NAV × (1-discount)`에서 시작한다. NAV return, distribution composition과 할인율 변화를 분리하고, tender는 accepted shares에만 98% NAV를 적용한다. merger는 market price가 아니라 aggregate NAV-equivalent exchange이므로 discount가 자동으로 전부 현금화되는 것은 아니다.",
    actual="FY2016 market return +6.68% 대 NAV -0.65%, FY2017 market +21.79% 대 NAV +14.03%로 discount closure가 추가 수익을 만들었다. 2017 tender는 AGC outstanding shares의 최대 15%를 98% NAV에 샀고 초과청약됐다. 2018-08-27 AGC holders는 AGC NAV $6.36당 AVK 0.36302760 shares를 받았다.",
    price="정확한 investor total-return ledger는 보유기간·재투자·tender 참여가 필요해 만들지 않는다. 다만 공식 fund return에서 FY2016·17 market return이 NAV return을 합계 약 15.1%p 상회했고, 할인은 약 18.95%에서 약 8%로 축소됐다. tender accepted portion은 98% NAV에 현금화됐다.",
    drivers="underlying credit만이 아니라 discount normalization이 수익의 핵심이었다. oversubscribed tender가 marginal liquidity를 제공했고 NAV-equivalent merger가 tiny-fund 구조비용을 줄였다. leverage와 ROC는 손실 가능성을 높였지만 catalyst가 먼저 작동했다.",
    counterfactual="NAV가 15% 하락하고 leverage cost가 올라가며 discount가 20%에 남아도 distribution과 tender probability를 합친 기대수익이 양수였는가?",
    error="좋은 방향에도 headline 11.4% yield를 economic earning yield처럼 보일 위험이 있었다. tender 15%를 전 보유지분의 확정 exit로 간주하거나 leverage를 단순 upside amplifier로 보는 것도 오류다.",
    warning="명확한 thesis break는 없었다. 사전 경고는 NAV 하락과 함께 distribution의 ROC 비중·leverage cost가 상승하고 discount가 20% 이상에 고착되는 조합이었다.", first_signal_date="2016-10-31",
    scenarios=[("Bear", "credit loss·leverage drag·discount 20%+", "distribution 포함 손실", "FY2016 NAV 약세만 일부"), ("Base", "NAV 보합·discount 10%", "carry+10%p closure", "FY2017말 약 8%"), ("Bull", "tender·NAV merger", "NAV 근접 realization", "2017 tender·2018 merger")],
    metrics=[("T0 discount", "~18.95%", "~10%", "FY2017말 ~8%", "강한 성공"), ("Distribution", "$0.047/month", "carry", "지속·ROC 포함", "혼합 성공"), ("FY2017 market/NAV", "closure 기대", "market>NAV", "+21.79%/+14.03%", "+7.76%p"), ("Tender", "activist option", "실행", "15% @98% NAV", "강한 성공"), ("Merger", "liquidation option", "NAV 보존", "AGC NAV $6.36; ratio .36302760", "성공")],
    timeline=[("2016-01-17", "VIC Long", "~18.95% discount"), ("2016-10-31", "FY2016 종료", "market +6.68%/NAV -0.65%"), ("2017-08-09", "15% tender 개시", "할인 catalyst"), ("2017-09-07", "tender 만료", "초과청약"), ("2017-09-12", "final results", "$6.4876·98% NAV"), ("2017-10-31", "FY2017 종료", "discount ~8%"), ("2018-05-29", "AVK merger proxy", "expense/liquidity rationale"), ("2018-08-27", "merger 완료", "NAV-equivalent AVK shares")],
    lessons=["CEF는 headline yield보다 NAV quality·leverage·discount catalyst를 함께 산다.", "distribution에서 income·gain·return of capital을 분리한다.", "tender의 size·price·proration을 실제 payoff에 반영한다.", "NAV-for-NAV merger와 market-price exit를 혼동하지 않는다."],
    checklist=["NAV asset-level liquidity", "Level 1/2/3 mix", "distribution tax character", "leverage ratio·cost", "expense ratio", "activist standstill", "tender price·proration", "merger conversion ratio"],
    scorecard=scorecard("성공", "강한 성공", "강한 성공", "CEF common 적절", "성공"),
    claims=[
        claim("약 18.95% NAV discount", "강한 성공", "liquid portfolio에 비해 market discount가 과도하다.", "NAV가 유지되면 할인 19%→10%만으로 약 11% 가격 uplift가 생긴다.", "원문 NAV·price와 mostly Level 1/2 holdings.", "NAV marks가 realizable하고 fees가 value를 소모하지 않는다.", "NAV 하락과 discount 20%+ 고착이면 반증.", "FY2017말 discount 약 8%.", "약 11%p 축소.", "point NAV의 credit beta를 작게 봤다.", "discount와 NAV를 두 개의 독립 return driver로 기록한다."),
        claim("NAV quality는 충분히 투명", "성공", "portfolio가 사모·Level 3가 아니라 marked securities 중심이다.", "observable marks는 liquidation-value uncertainty를 줄인다.", "Level 1/2 비중과 listed fixed-income holdings.", "marks가 stressed bid와 크게 다르지 않다.", "Level 3·illiquid 비중 급증 시 반증.", "tender와 merger가 NAV 근접 기준으로 실행됐다.", "NAV conversion까지 검증.", "market liquidity와 credit liquidity를 혼동할 수 있다.", "valuation hierarchy와 position liquidity를 따로 본다."),
        claim("11.4% distribution carry", "부분 성공", "월 $0.047가 waiting return을 제공한다.", "현금분배가 discount catalyst를 기다리는 carry가 된다.", "연환산 headline yield 약 11.4%.", "분배가 portfolio income·realized gain으로 충당된다.", "ROC 확대·NAV erosion이면 약화.", "분배는 지속됐지만 2015 distributions 일부는 ROC였다.", "headline yield 전부가 economic return은 아님.", "yield를 earning power로 등치했다.", "NAV total return과 tax character를 같이 본다."),
        claim("15% tender optionality", "강한 성공", "activism이 NAV 근접 tender를 유도할 수 있다.", "일부 shares를 98% NAV에 매입하면 accepted holder payoff와 전체 discount anchor가 생긴다.", "activist pressure와 board options.", "board가 action하고 shareholders가 참여한다.", "tender 부재·deep haircut이면 실패.", "2017 최대 15% tender, oversubscribed, 33% proration.", "$6.4876·98% NAV.", "15%를 전체 exit처럼 보면 안 된다.", "size·proration·tax를 position cash-flow에 넣는다."),
        claim("merger/liquidation option", "강한 성공", "fund consolidation이 structural discount를 줄인다.", "larger fund는 expense ratio와 liquidity를 개선하고 NAV-equivalent exchange를 제공한다.", "small fund와 overlapping mandate.", "shareholder approval·tax-free NAV exchange가 가능하다.", "dilutive exchange·vote failure면 반증.", "2018 AGC가 AVK에 NAV-equivalent로 합병됐다.", "AGC NAV $6.36, ratio 0.36302760.", "합병 후 AVK discount는 남는다.", "terminal event 뒤 successor discount까지 추적한다."),
        claim("leverage는 감당 가능", "부분 성공", "leverage가 income과 recovery를 증폭한다.", "asset return이 funding cost를 넘으면 common NAV가 더 빨리 증가한다.", "investments 약 174.5% of net assets.", "credit loss와 rates가 동시 악화하지 않는다.", "asset coverage·funding cost 악화면 반증.", "horizon 내 fund는 tender·merger까지 유지됐다.", "distress 없음; expense 부담은 존재.", "upside amplifier만 강조했다.", "leverage는 asset coverage와 downside NAV beta로 stress한다."),
    ],
)


add(
    id="604072e8-d449-41cb-8a21-76eb2513f1a5", date="2009-01-22", author="madmax989", ticker="AGC1",
    company="American General Finance Corporation", filename="analysis/ideas/2009/2009-01-22_AGC1_american_general_finance_bonds_long.md",
    source="https://www.valueinvestorsclub.com/idea/AMERICAN_GENERAL_FINANCE_CP/2611550110", group="agf_credit", direction="Long", raw_direction="Short",
    security="2011~2012 American General Finance senior unsecured notes / Long", entry="약 50~60 cents on par", horizon="2~4년 maturity·refinancing",
    raw_horizon="near-term senior unsecured claims, no large secured layer, consumer-loan runoff와 AIG/strategic support",
    title="panic-priced near-term senior credit Long", verdict="강한 성공 — issuer survival·strategic sale·refinancing", score=9.0, process=8.4,
    conclusion="AIG crisis 때 50~60c로 내려간 AGF near-term senior unsecured bonds를 산 거래다. 2010 Fortress가 80% economic interest를 인수해 Springleaf로 재편했고 near-term claims는 going-concern path를 통과했다. 다만 원문에서 exact CUSIP·purchase settlement가 보존되지 않아 35~45% IRR을 재현하지 않는다.",
    t0="시장은 AIG liquidity crisis를 AGF consumer-finance subsidiary의 급격한 default로 번역했다. 원문은 2011~12 maturities가 50~60c이면 상당한 loan losses를 반영하고, 큰 secured debt layer가 앞서지 않아 asset runoff와 AIG 또는 buyer의 franchise-preservation incentive가 unsecured recovery를 지지한다고 봤다.",
    reverse="AGF는 2008 이후 funding strain, real-estate losses와 new-originations 축소를 겪었다. parent support는 법적 guarantee가 아니며, receivables가 생각보다 빨리 손상되거나 자산이 담보화되면 unsecured recovery가 급감할 수 있었다. strategic buyer가 equity를 사도 채권조건이 자동 보장되는 것은 아니다.",
    valuation="credit payoff는 enterprise multiple이 아니라 maturity별 cash waterfall이다. receivables를 collateral·delinquency별 haircut하고 cash, secured claims, operating cost와 tax를 차감한 뒤 unsecured recovery를 계산한다. 50~60c entry에서 par repayment가 크더라도 exact IRR은 coupon·trade date·maturity/CUSIP가 있어야 한다.",
    actual="Fortress affiliate는 2010-11-30 AGF parent의 80% economic interest를 인수했고 AIG는 20%를 유지했다. 회사는 Springleaf로 이름을 바꾸고 $14.5bn net finance receivables와 $1.49bn cash를 가진 going concern으로 재편됐다. 이후 capital-markets refinancing은 near-term unsecured survival thesis를 지지했다.",
    price="50~60c에서 par path는 price appreciation만으로 약 67~100% 잠재 upside지만 이것을 realized return으로 쓰지 않는다. 어떤 2011·2012 note를 얼마에 사고 언제 매도·상환받았는지, coupon과 accrued interest가 없기 때문이다. 방향은 강한 성공, exact IRR은 미확정이다.",
    drivers="parent-name fear와 subsidiary asset/recovery를 분리한 security selection이 수익을 만들었다. 짧은 maturity와 unsecured 앞의 제한적 secured layer가 시간을 줄였고, Fortress transaction이 franchise continuation과 refinancing bridge를 제공했다.",
    counterfactual="Fortress 거래 없이 AIG가 support를 중단하고 receivables recovery가 20%p 낮아져도 50~60c unsecured entry가 손실을 피할 수 있었는가?",
    error="AIG 또는 buyer support를 recovery source로 세면서 법적 의무와 economic incentive를 충분히 분리하지 않았다. exact maturity/CUSIP가 없는 상태에서 35~45%를 정밀한 IRR로 제시한 것도 재현성을 낮춘다.",
    warning="사전 반증은 secured funding 급증, unencumbered receivables 급감과 2011 maturity funding 미확보였다. 2010 Fortress closing은 오히려 긍정적 첫 확정신호였다.", first_signal_date="2010-08-11",
    scenarios=[("Bear", "deep asset loss·담보화·지원 중단", "30~50c recovery", "미실현"), ("Base", "runoff+buyer·refinancing", "coupon+par", "survival 경로 실현"), ("Bull", "rapid spread normalization", "조기 80~100c", "방향상 실현")],
    metrics=[("Entry", "50~60c", "par recovery", "near-term claims survived", "강한 성공"), ("Cash 2010", "liquidity 핵심", "maturity buffer", "$1.49bn", "지지"), ("Net receivables", "asset recovery", "debt cover", "$14.52bn after push-down", "지지"), ("Fortress stake", "strategic option", "franchise continuation", "80% @2010-11-30", "강한 성공"), ("IRR", "35~45%", "HTM", "CUSIP ledger 없음", "미확정")],
    timeline=[("2009-01-22", "VIC bond Long", "50~60c panic price"), ("2009", "loan runoff·liquidity preservation", "survival test"), ("2010-08-11", "AIG/Fortress agreement", "strategic bridge"), ("2010-11-30", "80% acquisition completed", "control transfer"), ("2010-12-31", "$1.49bn cash", "near-term liquidity"), ("2011-03-07", "Springleaf name", "franchise continuation"), ("2011~12", "near-term maturities", "claims serviced/refinanced"), ("2013", "public debt access 확대", "credit normalization 확인")],
    lessons=["distressed financial credit는 parent headlines보다 legal issuer·seniority·maturity를 먼저 본다.", "strategic support는 guarantee와 분리해 recovery scenario에 넣는다.", "unencumbered assets와 secured-debt creep를 함께 추적한다.", "CUSIP와 dated cash ledger 없이는 exact YTM·IRR을 확정하지 않는다."],
    checklist=["legal issuer", "CUSIP·coupon·maturity", "secured claims", "unencumbered receivables", "delinquency/charge-off", "cash burn", "parent guarantee", "refinancing calendar"],
    scorecard=scorecard("survival 성공", "강한 성공", "성공", "near-term debt 적절", "성공"),
    claims=[
        claim("50~60c는 recovery를 과도하게 할인", "강한 성공", "near-term bonds가 liquidation recovery보다 싸다.", "receivable runoff와 cash가 secured claims 뒤 unsecured principal을 지지한다.", "panic pricing과 consumer-loan asset base.", "asset loss가 price-implied 수준보다 낮다.", "recovery estimate 50c 미만이면 반증.", "issuer는 going concern으로 유지되고 claims가 refinanced됐다.", "principal impairment evidence 없음.", "portfolio별 vintage haircut가 거칠었다.", "price-implied recovery와 own recovery를 표로 맞춘다."),
        claim("unsecured 앞 secured layer가 작다", "성공", "큰 secured debt가 없어 noteholders가 asset value에 가깝다.", "담보선순위가 작으면 unsecured waterfall residual이 커진다.", "T0 capital-structure review.", "위기 중 assets가 새 담보로 빠져나가지 않는다.", "secured debt·encumbrance 급증 시 실패.", "Fortress 구조와 후속 funding 속에서도 unsecured notes가 존속했다.", "정확한 date-by-date encumbrance 부족.", "정적 capital structure를 쓰지 않는다.", "매 분기 encumbered/unencumbered bridge를 만든다."),
        claim("near-term maturity 선택", "강한 성공", "2011~12 bonds가 장기채보다 path risk가 작다.", "짧은 maturity는 asset runoff cash와 refinancing catalyst를 앞당긴다.", "원문 maturity focus.", "company가 maturity 전에 cash를 고갈하지 않는다.", "12개월 내 funding gap이면 반증.", "2010 control transaction 뒤 near-term claims가 survival path를 통과했다.", "정확한 CUSIP별 payoff 미복원.", "issuer view만으로 개별 bond를 뭉쳤다.", "각 maturity를 별도 security unit로 기록한다."),
        claim("consumer-loan collections가 debt service", "성공 방향", "높은-yield receivables가 신규대출 축소 중에도 현금을 낸다.", "amortizing book의 collections가 opex·loss 뒤 bond cash를 만든다.", "large branch receivable base.", "charge-offs가 collections를 압도하지 않는다.", "delinquency·net charge-off 재악화면 반증.", "2010 year-end net finance receivables $14.52bn와 cash $1.49bn.", "going-concern value 유지.", "accounting receivable와 cash recovery를 동일시할 위험.", "cohort cash collection을 본다."),
        claim("AIG/strategic buyer가 franchise 보존", "강한 성공", "AIG 매각 또는 지원이 disorderly liquidation을 피한다.", "operating platform value가 debt continuity incentive를 만든다.", "national branch network와 franchise value.", "buyer가 liabilities를 유지할 유인이 있다.", "bankruptcy sale·liability rejection이면 실패.", "Fortress가 80%를 인수하고 AIG가 20%를 유지했다.", "franchise continuation 확정.", "economic incentive를 legal guarantee로 오해할 수 있다.", "support를 계약·담보·option value로 나눈다."),
        claim("35~45% held-to-maturity IRR", "방향 성공·정확치 미확정", "50~60c에서 coupon과 par을 받으면 35~45% IRR이다.", "large pull-to-par와 coupon이 short duration에 결합한다.", "원문 price·maturity range.", "정확한 note·settlement·cash flow가 맞다.", "principal haircut·coupon interruption이면 실패.", "principal-survival 방향은 맞았지만 exact holder ledger가 없다.", "IRR 재현 불가.", "range를 security-specific 산식 없이 제시했다.", "투자결과는 CUSIP별 XIRR로만 확정한다."),
    ],
)


add(
    id="3fbf61ca-ad89-448a-9f3f-22a821e543c8", date="2012-11-22", author="creditguy", ticker="AGC1",
    company="Springleaf Finance Corporation", filename="analysis/ideas/2012/2012-11-22_AGC1_springleaf_6_90_2017_notes_long.md",
    source="https://www.valueinvestorsclub.com/idea/SPRINGLEAF_FINANCE_CORP/6086881565", group="agf_credit", direction="Long", raw_direction="Long",
    security="6.90% Medium-Term Notes Series J due 2017 / Long", entry="약 87; YTM 약 10%", horizon="12개월 spread tightening·2017 pull-to-par",
    raw_horizon="delinquency normalization, securitization access, Fortress alignment와 maturity management",
    title="normalizing non-prime credit·pull-to-par Long", verdict="매우 강한 성공 — exchange·repurchase·maturity 해결", score=9.5, process=9.0,
    conclusion="6.90% 2017 notes를 약 87에 사 coupon, pull-to-par와 spread tightening을 노렸다. 2013 회사는 $700m principal을 2021/2023 notes로 교환하고 약 $184m 현금매입을 계획했으며, 2017 약 $466m을 추가 repurchase했다. holder 선택별 exact IRR은 다르지만 maturity-wall thesis는 매우 강하게 적중했다.",
    t0="60+ delinquency는 non-real-estate loans 2.90%로 5.09% peak보다 낮았고 retail finance 2.71%도 약 6.1% peak에서 개선됐다. 2012 cash 약 $1.5bn과 $500m note receivable, 약 $200m FCF가 약 $15bn debt를 받쳤고 securitization yields는 4.38%→3.59%→2.80%로 하락했다. 원문은 liquidity가 2016까지 확보됐다고 판단했다.",
    reverse="equity FCF가 양수여도 large debt stack의 maturity concentration과 secured funding은 unsecured note를 위협할 수 있었다. delinquency 개선이 loan sales·forbearance 효과일 수 있고 Fortress는 equity sponsor이지 bond guarantee가 아니었다. exchange는 par cash repayment가 아니라 duration 연장일 수 있었다.",
    valuation="87 price의 bond return은 coupon 6.90%, pull-to-par 13 points와 spread duration이다. base는 2017 par, bull은 12개월 spread tightening, bear는 exchange coercion·recovery haircut이다. exchange holder는 2021/2023 notes를 받으므로 original 2017-note IRR과 successor cash flows를 연결해야 한다.",
    actual="2013-09 Springleaf는 $500m 7.75% 2021 notes와 $200m 8.25% 2023 notes를 $700m 2017 notes와 교환했고 약 $184m 2017 notes cash repurchase를 계획했다. 2017에는 약 $466m principal을 추가 repurchase하기 위한 financing을 조달했다. remaining maturity가 해결되며 principal impairment thesis는 발생하지 않았다.",
    price="원문 low-to-mid teens 12개월 return은 spread/coupon 방향상 타당했지만 trade·exchange election 자료가 없어 exact realized total return을 확정하지 않는다. 87에서 principal impairment 없이 exchange·cash repurchase·maturity path를 통과한 점은 payoff의 핵심을 입증한다.",
    drivers="delinquency 개선이 funding access 회복으로 이어졌고 securitization yield 하락이 public unsecured refinancing을 가능하게 했다. 2013 exchange는 maturity wall을 분산했고 2017 cash repurchase가 잔여 tail을 줄였다.",
    counterfactual="securitization yield가 다시 6%로 오르고 delinquency가 peak의 80%까지 반등해도 2017 principal을 현금·자산매각 없이 상환할 수 있었는가?",
    error="liquidity through 2016을 2017 maturity solution과 거의 같은 것으로 봤다. exchange는 default avoidance에는 긍정적이지만 holder에게 duration·coupon·liquidity risk를 바꾸므로 par repayment와 동일하지 않다.",
    warning="2013 exchange pricing이 punitive하거나 participation이 사실상 강제였다면 return thesis를 다시 계산해야 했다. 실제 exchange와 cash repurchase는 긍정적 de-risking 신호였다.", first_signal_date="2013-09-25",
    scenarios=[("Bear", "credit 재악화·funding shut", "60~80 recovery", "미실현"), ("Base", "carry+2017 par", "low-mid teens 1Y 후 par", "principal path 실현"), ("Bull", "rapid spread tightening", "90s/100 조기", "refinancing이 지지")],
    metrics=[("Bond price/YTM", "~87/~10%", "low-mid teens 1Y", "principal impairment 없음", "강한 성공"), ("Non-RE 60+ delinquency", "2.90% vs 5.09% peak", "계속 개선", "funding 회복", "성공"), ("Securitization yield", "4.38→3.59→2.80%", "access 개선", "public notes 발행", "강한 성공"), ("2013 exchange", "$700m", "wall 완화", "2021/23로 교환", "성공"), ("2017 repurchase", "maturity risk", "상환", "~$466m", "강한 성공")],
    timeline=[("2012-11-22", "VIC bond Long", "~87·~10% YTM"), ("2012-12", "credit metrics 개선", "delinquency down"), ("2013-09-24", "new notes issued", "$650m 2021+$300m 2023"), ("2013-09-25", "$700m exchange", "2017 wall 분산"), ("2013", "~$184m cash repurchase plan", "principal reduction"), ("2015", "OneMain transaction era", "platform scale"), ("2017-05", "~$466m repurchase", "tail 제거"), ("2017 maturity", "remaining notes 해결", "credit thesis 완료")],
    lessons=["normalizing credit는 delinquency가 funding cost로 이어지는 bridge를 본다.", "bond pull-to-par와 spread tightening을 분리한다.", "exchange는 default 해결과 holder return을 별도로 판정한다.", "maturity wall은 amount·date·committed liquidity로 추적한다."],
    checklist=["CUSIP", "dirty price·accrued", "60+ delinquency", "charge-off", "securitization yield", "unencumbered assets", "maturity ladder", "exchange consideration"],
    scorecard=scorecard("성공", "강한 성공", "강한 성공", "2017 note 적절", "강한 성공"),
    claims=[
        claim("87 price·10% YTM", "강한 성공", "2017 note는 normalized credit에 비해 싸다.", "coupon+13-point pull-to-par+spread tightening이 return을 만든다.", "price ~87와 6.90% coupon.", "principal impairment가 없다.", "expected recovery 87 미만이면 반증.", "exchange·repurchase·maturity가 principal을 보존했다.", "exact holder IRR 미확정.", "quoted YTM와 realized path를 혼용할 수 있다.", "dirty price와 cash-flow election을 저장한다."),
        claim("delinquency normalization", "성공", "consumer book credit가 2009 peak에서 회복한다.", "lower delinquency·charge-off가 cash collection과 funding access를 개선한다.", "non-RE 2.90% vs 5.09%; retail 2.71% vs ~6.1%.", "improvement가 seasoning·sale effect만은 아니다.", "두 분기 재악화면 반증.", "후속 securitization와 public issuance가 market validation을 제공했다.", "asset-level loss curve 없음.", "delinquency 수준만으로 ultimate loss cash를 완전히 설명할 수 없다.", "credit KPI와 capital-market KPI를 연결한다."),
        claim("liquidity through 2016", "부분 성공", "$1.5bn cash·$500m note·FCF가 runway를 준다.", "cash+collections가 near-term maturities를 넘어 refinancing window를 연다.", "원문 liquidity bridge.", "cash가 restricted가 아니고 burn이 관리된다.", "2015 이전 funding gap이면 실패.", "2013 exchange로 2017 wall 일부가 장기화됐다.", "2017까지 자동 보장된 것은 아님.", "runway 끝과 maturity date를 혼동했다.", "월별 sources/uses를 maturity까지 연장한다."),
        claim("securitization funding 회복", "강한 성공", "yield 4.38%→2.80%는 시장 접근 개선이다.", "lower asset funding cost가 equity cash와 unsecured refinance capacity를 높인다.", "2012 sequential transaction yields.", "collateral performance와 advance rates가 유지된다.", "deal 취소·haircut 급증이면 반증.", "2013 unsecured 2021/23 notes까지 발행했다.", "public funding으로 확장.", "headline yield만 보고 structural subordination을 작게 봤다.", "advance rate·tranche와 recourse를 함께 본다."),
        claim("Fortress alignment·platform value", "성공", "sponsor가 franchise를 유지하고 capital markets를 연다.", "equity sponsor의 option value와 IPO/scale plan이 default avoidance를 지지한다.", "Fortress control과 operating franchise.", "sponsor가 추가 capital·refinancing을 선택한다.", "asset strip·bankruptcy면 실패.", "Springleaf/OneMain platform이 확대되고 debt market 접근이 회복됐다.", "support 방향 적중.", "sponsor alignment를 guarantee처럼 볼 위험.", "sponsor incentives와 legal claims를 분리한다."),
        claim("2017 maturity management", "강한 성공", "회사는 2017 notes를 exchange·repurchase·pay할 수 있다.", "new long-term notes와 cash tender가 wall을 줄인다.", "improving liquidity·funding market.", "new debt terms가 지속 가능하다.", "2017 payment default면 실패.", "2013 $700m exchange, ~$184m cash plan, 2017 ~$466m repurchase.", "wall 대부분 구체적으로 해결.", "gross issuance만 보고 net debt를 놓칠 수 있다.", "maturity별 beginning-to-ending principal roll-forward를 만든다."),
    ],
)


add(
    id="24cf0eb8-cf98-4327-9b5f-f9440b5fee39", date="2015-10-16", author="fiftycent501", ticker="AGCO",
    company="AGCO Corporation", filename="analysis/ideas/2015/2015-10-16_AGCO_long.md",
    source="https://www.valueinvestorsclub.com/idea/AGCO_CORP/9193108982", group="agco", direction="Long", raw_direction="Long",
    security="NYSE:AGCO common equity / Long", entry="원문 약 $44; source DB next-session close $38.6545", horizon="2~5년 agriculture cycle normalization",
    raw_horizon="2018/19 sales $10bn, operating margin 10%, EPS $7.25와 downside ~$38",
    title="trough-cycle agriculture equipment Long", verdict="강한 주가 성공 / 10% margin bull case 실패", score=8.6, process=8.5,
    conclusion="농기계 downturn 뒤 싼 valuation과 Europe mix·cost cuts·buybacks를 산 거래는 1Y +18.4%, 2Y +66.7%, 5Y +92.3%로 성공했다. 그러나 2018 sales $9.352bn와 operating margin 약 5.2%는 $10bn·10% bull case에 크게 못 미쳤다. cycle direction은 맞고 peak earnings bridge는 과했다.",
    t0="North American large-ag weakness가 이미 반영된 가운데 Europe 비중, cost reduction, strong balance sheet와 buybacks가 downside를 약 $38로 제한한다고 봤다. normalized EPS 약 $4.50, 2018/19 bull sales $10bn·operating margin 10%·EPS $7.25를 제시했다.",
    reverse="농기계 replacement는 미뤄질 수 있고 dealer inventory·farmer income·FX가 동시에 악화할 수 있었다. AGCO는 scale·margin이 Deere보다 낮았으며 10% margin은 volume recovery뿐 아니라 pricing, mix, factory utilization과 cost execution이 모두 필요했다.",
    valuation="trough EPS와 peak EPS 사이 normalized bridge가 필요하다. downside는 2016 EPS $2.50×15x≈$38, base는 normalized $4.50, bull은 $7.25였지만 bull margin을 확률가중해야 한다. source DB return은 next-session close 기준 price-only라 원문 $44 entry와 완전히 같지 않다.",
    actual="source DB price-only return은 1Y +18.4%, 2Y +66.7%, 3Y +30.7%, 5Y +92.3%였다. AGCO 2018 sales는 $9.352bn, operating income $489m로 약 5.2% margin이었다. 2019 sales는 $9.041bn, operating income $348.1m로 bull margin은 실현되지 않았다.",
    price="source DB는 next-session close $38.6545를 기준으로 1Y 1.1840x, 2Y 1.6671x, 5Y 1.9230x다. 배당·세금 제외 price-only이며 원문 약 $44와 entry가 다르다. 따라서 thesis outcome은 강한 성공이지만 original-price exact IRR로 부르지 않는다.",
    drivers="주가 수익은 10% realized margin보다 downturn이 더 악화하지 않고 cycle expectation이 개선된 데서 나왔다. entry multiple, balance sheet와 buyback이 시간을 제공했고 market은 peak numbers가 나오기 전에 recovery 확률을 가격에 넣었다.",
    counterfactual="operating margin이 5~6%에 머물러도 $44 entry에서 downside가 제한되고 50% upside가 가능했는가? 그렇다면 10% margin은 thesis가 아니라 optionality였어야 한다.",
    error="bull-case 10% margin을 base-like target에 가깝게 사용했고 source DB의 next-session close와 원문 quote를 섞을 위험이 있었다. price success가 forecast accuracy를 증명하는 것은 아니다.",
    warning="2018 sales가 $9.35bn인데 operating margin이 약 5.2%에 머문 시점이 margin claim의 명확한 반증이었다. 다만 stock thesis는 이미 cycle rerating으로 성공했다.", first_signal_date="2019-02-26",
    scenarios=[("Bear", "cycle 장기화·EPS $2.50", "~$38", "source path 큰 downside 없음"), ("Base", "normalized EPS ~$4.50", "mid-$50s~$60s", "2Y +66.7%"), ("Bull", "$10bn sales·10% margin·$7.25 EPS", "50%+", "price는 성공·margin 실패")],
    metrics=[("1Y price-only", "$38.6545 DB base", "downside 제한", "+18.4%", "성공"), ("2Y price-only", "cycle recovery", "+50% 안팎", "+66.7%", "강한 성공"), ("5Y price-only", "normalization", "상승", "+92.3%", "강한 성공"), ("2018 sales", "$10bn", "$10bn", "$9.352bn", "근접"), ("2018 op margin", "10% bull", "10%", "~5.2%", "실패")],
    timeline=[("2015-10-16", "VIC Long", "trough thesis"), ("2016-10", "1Y", "+18.4% price-only"), ("2017-10", "2Y", "+66.7%"), ("2018-10", "3Y", "+30.7%"), ("2018-12-31", "sales $9.352bn", "scale 근접"), ("2018-12-31", "op income $489m", "margin ~5.2%"), ("2019-12-31", "sales $9.041bn", "bull sales 미달"), ("2020-10", "5Y", "+92.3%")],
    lessons=["cyclical Long은 peak margin보다 trough survival과 direction을 먼저 맞힌다.", "bull-case denominator를 base valuation에 넣지 않는다.", "source return의 entry timestamp를 원문 quote와 분리한다.", "stock success와 operating forecast accuracy를 따로 점수화한다."],
    checklist=["dealer inventory", "retail vs wholesale units", "farmer income", "regional mix", "price/mix", "factory utilization", "working capital", "normalized vs peak margin"],
    scorecard=scorecard("cycle 성공", "강한 성공", "성공", "common 적절", "성공"),
    claims=[
        claim("trough downside 약 $38", "성공", "2016 EPS $2.50×15x가 downside를 제한한다.", "balance sheet와 replacement demand가 loss-tail을 막는다.", "원문 downside bridge·Europe mix.", "15x가 trough에도 유지된다.", "EPS <$2 또는 leverage 급증이면 실패.", "DB 1Y +18.4%; large downside가 나타나지 않았다.", "원문 $44와 DB base 차이.", "multiple floor를 고정값으로 썼다.", "bear case에는 multiple compression도 넣는다."),
        claim("ag cycle normalization", "강한 성공", "farmer economics와 replacement가 회복한다.", "volume·mix 개선이 fixed-cost absorption과 EPS를 높인다.", "multi-year downturn과 replacement age.", "dealer inventory가 먼저 소진된다.", "retail decline·inventory build가 지속되면 반증.", "2Y +66.7%, 5Y +92.3% price-only.", "price direction 강한 적중.", "commodity beta와 company execution을 분리하지 않았다.", "retail units·inventory·margin을 동시 추적한다."),
        claim("2018/19 sales 약 $10bn", "근접", "cycle 회복 시 sales가 $10bn에 접근한다.", "volume+price/mix+FX가 top line을 회복시킨다.", "brand portfolio와 geographic mix.", "currency·downcycle가 완화된다.", "$9bn 아래 지속이면 실패.", "2018 $9.352bn, 2019 $9.041bn.", "target 대비 -6.5%/-9.6%.", "nominal sales가 margin을 보장한다고 봤다.", "sales와 contribution margin을 분리한다."),
        claim("operating margin 10%", "실패", "scale·cost cuts로 10% margin이 가능하다.", "higher utilization·mix가 operating leverage를 만든다.", "cost programs와 premium brands.", "pricing과 volume이 fixed/variable cost를 상회한다.", "margin 7% 미만이면 bull case 반증.", "2018 operating income $489m, margin 약 5.2%.", "약 -4.8%p.", "best-in-cycle aspiration을 normalized outcome으로 썼다.", "incremental margin과 peer ceiling으로 stress한다."),
        claim("EPS $7.25", "미달 가능성 큼", "$10bn×10% economics가 $7.25 EPS를 만든다.", "operating profit에서 interest·tax·share count를 차감한다.", "원문 earnings bridge.", "10% margin과 buyback이 실현된다.", "margin miss면 EPS bridge도 반증.", "10% margin이 실현되지 않아 bridge의 핵심 전제가 깨졌다.", "공식 2018/19 operating result가 반증.", "EPS target의 driver sensitivity가 부족했다.", "sales·margin·tax·shares를 별도 claim으로 둔다."),
        claim("buyback이 per-share value를 높임", "성공 방향", "downcycle에 저가 자사주를 매입한다.", "share count 감소가 recovery EPS와 intrinsic value/share를 높인다.", "balance sheet·capital return plan.", "buyback이 debt/working-capital 안전을 해치지 않는다.", "고가 매입·leverage 상승이면 실패.", "capital return은 price recovery를 지원했으나 단독 attribution은 제한적이다.", "정확한 buyback alpha 미분리.", "authorization를 value creation으로 등치할 수 있다.", "average price·shares retired·net debt를 잇는다."),
    ],
)


add(
    id="3af1399f-2fde-41f0-90b1-910f4bbfbb7f", date="2021-11-06", author="MickyS", ticker="AGFX",
    company="Argentex Group Plc", filename="analysis/ideas/2021/2021-11-06_AGFX_argentex_long.md",
    source="", group="argentex", direction="Long", raw_direction="Long", security="AIM:AGFX common equity / Long", entry="약 88p; market cap ~£100m",
    horizon="3~5년 client growth·margin·platform rerating", raw_horizon="~£20m free cash, ~7x 2022E EV/EBITDA, ~10% FCF yield, rising-rate·technology optionality",
    title="capital-light FX broker compounder Long", verdict="매우 강한 실패 — liquidity tail이 -97% terminal loss", score=1.0, process=5.8,
    conclusion="88p에서 high-margin·low-capex FX broker를 샀지만 원문 risk section의 client default/collateral risk가 2025 terminal event가 됐다. 급격한 FX 움직임과 margin calls가 liquidity를 훼손해 trading이 정지됐고 IFX가 2.49p cash offer를 제시했다. 단순 price loss는 약 97.2%다.",
    t0="revenue가 2013 £1m 미만에서 2020 약 £29m으로 성장했고 operating profit 약 £12.4m, insider ownership 30%+, free cash 약 £20m이었다. 88p·market cap £100m에서 EV 약 £80m, 2022E 약 7x EV/EBITDA와 10% FCF yield로 보였다. 금리상승과 technology platform은 upside였다.",
    reverse="FX broker는 inventory와 PP&E가 없어도 derivatives collateral과 settlement liquidity가 필요하다. client가 variation margin을 제때 내지 못하면 Argentex가 banks/prime brokers에 먼저 현금을 내야 한다. reported net cash 전부를 배당 가능한 excess로 보면 stress liquidity를 이중계산에서 빠뜨린다.",
    valuation="normalized EBITDA/FCF multiple에 앞서 stressed liquidity reserve를 enterprise value에서 차감해야 한다. `free cash - peak variation margin - counterparty default loss - regulatory buffer`가 진짜 excess cash다. terminal offer 2.49p는 평시 earnings multiple이 아니라 insolvency alternative 아래 rescue value였다.",
    actual="2025-04 rapid FX volatility, 특히 USD 약세가 forward·options book의 margin calls를 불렀다. 회사는 4월 22일 suspension을 요청했고 다음 날 liquidity가 더 악화됐다고 밝혔다. IFX는 £6.5m secured bridge와 추가 지원 논의를 제공했고 4월 25일 2.49p/share, 약 £3m equity value의 recommended offer를 발표했다.",
    price="2.49p / 88p - 1 = 약 -97.2%다. 중간 dividends를 포함하지 않아도 terminal capital loss가 결과를 지배한다. offer가 insolvency 시 very limited or nil return의 대안이었다는 공식 설명은 net cash downside-floor 가정이 왜 틀렸는지 보여준다.",
    drivers="loss의 원인은 spread margin 악화가 아니라 path-dependent collateral liquidity였다. 고객 collateral 수취와 bank margin 지급의 timing mismatch가 평시 cash를 며칠 만에 필요자본으로 바꿨다. emergency secured financing 뒤 common은 residual rescue value만 받았다.",
    counterfactual="상위 stress week에서 clients가 variation margin의 절반만 제때 내고 banks는 전액을 당일 요구할 때 필요한 cash가 £20m free cash보다 작았는가?",
    error="low capex를 low capital intensity로, cash balance를 excess cash로 간주했다. 이미 원문에 식별한 risk를 정량 liquidity waterfall·limit·position sizing으로 연결하지 않아 tail risk를 footnote로 남겼다.",
    warning="첫 명확한 공개 break는 2025-04-22 margin-call liquidity pressure와 trading suspension이었다. 하지만 사전에는 gross derivatives exposure·client collateral gap이 net cash에 근접하는 순간이 경고였어야 했다.", first_signal_date="2025-04-22",
    scenarios=[("Bear", "client default·£20m+ margin calls", "near-zero/rescue", "2.49p·약 £3m"), ("Base", "client growth·stable volatility", "7x EBITDA rerating", "terminal 전에 붕괴"), ("Bull", "rates+platform", "double-digit compounding", "미실현")],
    metrics=[("Entry/offer", "88p", "상승", "2.49p", "-97.2%"), ("Free cash", "~£20m", "downside floor", "stress collateral에 소진", "강한 실패"), ("Bridge", "불필요 가정", "self-funded", "£6.5m secured", "반증"), ("Equity value", "~£100m", "compound", "~£3m offer", "강한 실패"), ("Liquidity event", "tail risk", "관리 가능", "suspension·urgent funding", "강한 실패")],
    timeline=[("2021-11-06", "VIC Long", "88p compounder thesis"), ("2022", "international/platform expansion", "growth investment"), ("2024", "financial year ends", "cash·risk baseline"), ("2025-04-02", "FY24 results", "roadshow 뒤 volatility"), ("2025-04-22", "liquidity warning·suspension", "thesis break"), ("2025-04-23", "further deterioration", "immediate finance 필요"), ("2025-04-24", "IFX £6.5m bridge", "secured rescue"), ("2025-04-25", "2.49p recommended offer", "terminal common value")],
    lessons=["low-capex broker도 collateral 때문에 liquidity-capital intensive일 수 있다.", "free cash에서 stressed margin requirement를 먼저 차감한다.", "risk disclosure를 probability×cash need×time-to-fund로 계량한다.", "trading suspension과 secured rescue는 common thesis의 즉시 재인수점이다."],
    checklist=["gross/net derivatives", "client collateral timing", "variation-margin stress", "top counterparties", "bank facilities", "liquidity headroom", "regulatory buffer", "suspension/secured-finance triggers"],
    scorecard=scorecard("평시 일부 타당", "강한 실패", "실패", "common 취약", "매우 강한 실패"),
    claims=[
        claim("capital-light high-margin model", "stress에서 실패", "낮은 capex와 높은 margins가 compounder economics를 만든다.", "client flow spread가 fixed cost를 넘어 FCF로 전환된다.", "historical revenue·operating profit·low capex.", "collateral funding이 구조적으로 작다.", "stress liquidity가 annual FCF를 넘으면 반증.", "2025 margin calls가 business continuity를 위협했다.", "평시 margin보다 liquidity가 지배.", "accounting capital intensity만 봤다.", "operational·liquidity capital을 합산한다."),
        claim("£20m cash downside floor", "강한 실패", "market cap £100m 중 £20m cash가 downside를 지지한다.", "net cash를 EV에서 빼면 operating business가 싸다.", "reported free cash.", "cash가 unrestricted excess다.", "stress collateral·working capital need가 cash와 비슷하면 실패.", "£6.5m secured bridge와 추가 즉시지원이 필요했다.", "floor가 사라짐.", "cash의 functional purpose를 분류하지 않았다.", "minimum liquidity와 tail margin을 restricted-like로 본다."),
        claim("7x 2022E EV/EBITDA", "실패", "normalized earnings 대비 multiple이 낮다.", "growth와 durable margins가 multiple normalization을 만든다.", "EV ~£80m와 forecast EBITDA.", "EBITDA가 distributable cash에 가깝다.", "cash conversion·liquidity cost 붕괴면 반증.", "terminal equity value 약 £3m.", "multiple thesis 소멸.", "tail capital cost를 EBITDA에 반영하지 않았다.", "stress-adjusted FCF로 value한다."),
        claim("rising rates tailwind", "부차적", "client balances의 interest income이 증가한다.", "higher rates가 float yield를 높인다.", "rate sensitivity와 cash balances.", "FX volatility·hedging losses가 통제된다.", "liquidity shock이 interest benefit을 압도하면 반증.", "2025 FX move와 margin calls가 모든 rate benefit을 압도했다.", "driver ranking 오류.", "positive carry가 tail liquidity loss를 상쇄한다고 암묵적으로 가정했다.", "작은 recurring tailwind보다 low-frequency ruin risk를 우선한다."),
        claim("technology/platform optionality", "미실현", "platform 투자로 client acquisition과 operating leverage가 커진다.", "automation이 sales capacity와 margin을 높인다.", "growth plans와 international footprint.", "funding runway가 충분하다.", "core liquidity event가 platform payoff 전 도착하면 실패.", "terminal rescue가 platform optionality보다 먼저 발생했다.", "option value 사실상 0.", "funded-to-inflection을 검증하지 않았다.", "optionality에는 cost·date·survival probability를 붙인다."),
        claim("insider ownership alignment", "보호 실패", "30%+ insiders가 prudent risk management를 유도한다.", "owner-operators가 dilution·tail risk를 피한다.", "high insider holdings.", "risk limits와 liquidity governance가 강하다.", "emergency financing·near-zero sale이면 반증.", "board가 insolvency 대안으로 2.49p offer를 권고했다.", "alignment가 downside 못 막음.", "ownership을 competence·controls로 대체했다.", "risk governance와 exposure limits를 직접 확인한다."),
    ],
)


def agrify_common(id_, date, author, filename, source, entry, horizon, raw_horizon, title, conclusion, t0, valuation, counterfactual, score, process, second=False):
    if second:
        metrics = [("Entry/net cash", "~$6/~$4 per share", "floor", "누적 1:3000 split·희석", "실패"), ("2024 TTK EBITDA", "$56m", "$56m", "미실현", "강한 실패"), ("2024 software EBITDA", "$27m", "$27m", "미실현", "강한 실패"), ("FY2022 gross profit", "positive scale", "상승", "-$31.8m", "강한 실패"), ("Target", "$55", "~9x", "legacy model exit", "강한 실패")]
        claims = [
            claim("$4/share net cash floor", "실패", "주가 $6 중 약 $4가 net cash다.", "cash를 차감하면 operating optionality를 $2에 산다.", "원문 cash/share.", "cash가 committed capital이 아니다.", "cash burn·customer loans가 floor를 먹으면 실패.", "2022 losses·financing으로 cash가 소진됐다.", "floor 소멸.", "net cash를 liquidation cash로 봤다.", "cash uses와 runway를 먼저 모델링한다."),
            claim("TTK EBITDA $56m", "강한 실패", "2024 TTK recurring economics가 $56m EBITDA를 낸다.", "deployed VFUs와 production fees가 high-margin stream을 만든다.", "contract/backlog bridge.", "customers가 projects를 완공·운영·지불한다.", "loan reserves·project delay·gross loss면 반증.", "TTK loans와 projects가 reserves·litigation을 만들었다.", "$56m 미실현.", "nominal contracts에 realization 확률이 없었다.", "customer-by-customer collected cash로 bridge한다."),
            claim("software EBITDA $27m", "강한 실패", "installed base가 software fees를 scale한다.", "low incremental cost subscription이 높은 contribution margin을 낸다.", "VFU deployments와 Agrify Insights concept.", "installed base가 성장·유지된다.", "hardware/TTK deployment 실패 시 반증.", "core installed-base growth가 무너져 software scale도 오지 않았다.", "$27m 미실현.", "software를 독립 사업처럼 valued했다.", "attach·retention·collected ARR을 확인한다."),
            claim("2024 total EBITDA $83m", "강한 실패", "TTK $56m+software $27m으로 $83m이다.", "두 high-margin streams가 fixed opex를 흡수한다.", "원문 segment bridge.", "gross margins와 opex가 계획대로 움직인다.", "current gross loss면 즉시 반증.", "FY2022 gross loss -$31.8m, operating loss -$193.3m.", "방향부터 반대.", "먼 미래 EBITDA가 현재 unit economics를 가렸다.", "near-term gross-profit gate를 둔다."),
            claim("$55/share target", "강한 실패", "$83m EBITDA와 high multiple이 $55를 지지한다.", "earnings scale×multiple이 equity value를 만든다.", "원문 target bridge.", "share count·debt·business perimeter가 안정된다.", "dilution·reverse splits·secured debt면 반증.", "세 차례 split·financing·legacy sale로 original security가 훼손됐다.", "target 미실현.", "enterprise value를 original shares로 고정했다.", "fully diluted share waterfall를 동적으로 갱신한다."),
            claim("낮은 entry가 2021 thesis를 개선", "실패", "$9.26에서 ~$6 하락해 margin of safety가 커졌다.", "같은 business value에서 lower price가 expected return을 높인다.", "35%가량 lower nominal entry.", "intrinsic value와 unit economics가 유지된다.", "negative gross economics면 lower price도 무의미.", "2022 gross loss가 intrinsic value 가정을 파괴했다.", "가격 하락보다 value 하락이 큼.", "price anchoring을 했다.", "새 entry마다 thesis를 처음부터 다시 underwrite한다."),
        ]
    else:
        metrics = [("Entry/EV", "$9.26/~$76m", "cash floor+upside", "cash consumed", "실패"), ("FY2021 revenue", "$48~50m guide", "guide 상회", "$59.9m", "초기 성공"), ("FY2022 revenue", "rapid growth", "상승", "$58.3m", "실패"), ("FY2022 gross profit", "positive scaling", "증가", "-$31.8m", "강한 실패"), ("FY2022 op loss", "platform leverage", "개선", "-$193.3m", "강한 실패")]
        claims = [
            claim("$138m cash·$76m EV", "강한 실패", "cash-rich balance sheet가 downside를 제한한다.", "market cap에서 excess cash를 빼면 operating platform이 싸다.", "$213m market cap, ~$138m cash, < $1m LT debt.", "cash가 customer financing·losses에 투입되지 않는다.", "cash burn·receivable reserves 급증이면 반증.", "cash는 TTK loans·acquisitions·operating losses에 소진됐다.", "headline floor 소멸.", "cash를 risk capital이 아닌 excess로 봤다.", "cash commitments와 burn runway를 차감한다."),
            claim("TTK recurring fee pool", "강한 실패", "construction+VFU 뒤 10년 fees가 EV보다 크다.", "upfront vendor finance가 long-duration recurring fees를 산다.", "Bud & Mary's loan ~$13.5m, VFU ~$24m, nominal fees ~$268m.", "customer project가 완공·수익화·지불한다.", "litigation·loan reserve·negative project margin이면 실패.", "customer-related reserves와 litigation이 gross loss에 기여했다.", "nominal fee pool 미현금화.", "contract value를 risk-adjusted NPV로 바꾸지 않았다.", "default·delay·price scenarios를 고객별 적용한다."),
            claim("VFU technical superiority", "상업성 미검증", "controlled VFU가 yield·quality를 개선한다.", "better crop consistency가 customer ROI와 pricing을 지지한다.", "company performance claims.", "technical yield가 full project cash economics로 전환된다.", "customer payback·repeat order 부재면 약화.", "company-level gross loss로 superior technology가 profitable sales를 만들지 못했다.", "technical-to-economic bridge 실패.", "product metric을 customer ROI로 직결했다.", "independent cohort yield·all-in cost를 요구한다."),
            claim("2021/22 rapid revenue growth", "초기 후 실패", "2021 guide $48~50m 이후 고성장이 계속된다.", "backlog conversion과 acquisitions가 scale을 만든다.", "signed projects·guide.", "revenue quality와 collection이 유지된다.", "flat revenue·receivable reserve면 반증.", "2021 $59.9m이나 2022 $58.3m으로 정체했다.", "초기 guide 상회 후 성장 중단.", "acquired/project revenue를 recurring과 혼용했다.", "organic·acquired·cash-collected revenue를 나눈다."),
            claim("high-margin platform scale", "강한 실패", "software·service mix가 margins를 확대한다.", "installed base recurring fees가 low incremental cost로 쌓인다.", "SaaS-like narrative.", "hardware/project loss가 recurring margin보다 작다.", "gross margin 음수면 즉시 반증.", "2022 gross loss -$31.8m, -54.6% margin.", "방향 반대.", "future mix가 current losses를 자동 치유한다고 봤다.", "gross-profit gate 없이 TAM을 value하지 않는다."),
            claim("picks-and-shovels lowers cannabis risk", "실패", "plant-touching operator가 아니어서 commodity risk가 작다.", "equipment·software vendor는 customer 생산가격과 분리된다.", "non-plant-touching positioning.", "customers가 downturn에도 capex와 debt를 지불한다.", "customer distress·project cancellation이면 반증.", "cannabis downturn이 customer loans·inventory·projects를 훼손했다.", "risk 이전이 아니라 집중.", "vendor finance가 고객 commodity risk를 되가져왔다.", "end-customer solvency를 직접 stress한다."),
        ]
    add(
        id=id_, date=date, author=author, ticker="AGFY", company="Agrify Corporation", filename=filename, source=source, group="agrify",
        direction="Long", raw_direction="Long", security="Nasdaq:AGFY common equity / Long", entry=entry, horizon=horizon, raw_horizon=raw_horizon,
        title=title, verdict="매우 강한 실패 — negative gross economics·cash burn·희석", score=score, process=process, conclusion=conclusion, t0=t0,
        reverse="TTK는 SaaS가 아니라 Agrify가 고객의 financing, construction, cannabis price와 collection risk를 선순위로 떠안는 구조였다. backlog와 nominal 10-year fee는 customer가 facility를 완공하고 positive unit economics로 운영해야만 cash가 된다. cash-rich balance sheet는 그 위험을 떠받치는 capital이었다.",
        valuation=valuation,
        actual="FY2021 revenue는 약 $59.9m, FY2022는 $58.3m에 그쳤고 FY2022 gross loss -$31.8m, operating expenses $161.5m, operating loss 약 -$193.3m, goodwill/intangible impairment $69.9m이 발생했다. 2022 1:10, 2023 1:20, 2024 1:15 reverse splits는 누적 1:3,000이고 2024 Green Thumb secured convertible financing과 legacy business exit가 이어졌다.",
        price="2021/2022 nominal entry를 현재 quote와 직접 비교하지 않는다. 1:10×1:20×1:15 reverse splits, 중간 issuance·warrants·convertibles와 business-perimeter change가 있어 original-share cash-flow ledger가 필요하다. 다만 반복된 minimum-bid splits와 secured rescue는 original common의 대규모 impairment를 명확히 보여준다.",
        drivers="revenue가 아니라 customer-financed projects의 collectability와 gross economics가 손실을 만들었다. inventory·facility build-out reserves, customer loan allowances와 fixed opex가 cash를 소모했고, debt·warrants·reverse splits가 common의 residual claim을 계속 희석했다.", counterfactual=counterfactual,
        error="nominal contract value·backlog와 future high-margin fees를 확률가중 없이 더했고, headline cash를 committed project capital과 분리하지 않았다. current gross margin이 음수인데도 먼 미래 EBITDA와 software multiple이 thesis를 지배했다.",
        warning="FY2022에 gross loss -$31.8m과 TTK-related loan reserves가 확인된 시점이 가장 늦은 명백한 break다. 그 전에는 project별 cash collection이 milestone을 못 따라가는 것이 조기 경고였어야 했다.", first_signal_date="2022-06-30",
        scenarios=[("Bear", "customer default·negative gross margin", "cash burn·희석", "실현"), ("Base", "일부 TTK conversion", "cash runway 내 break-even", "미실현"), ("Bull", "VFU+software high-margin scale", "multi-bagger", "미실현")],
        metrics=metrics,
        timeline=[(date, "VIC Long", entry), ("2021-12-31", "revenue ~$59.9m", "초기 growth"), ("2022-06-30", "impairment trigger", "$69.9m"), ("2022-12-31", "gross loss -$31.8m", "model break"), ("2022-10-18", "1:10 split", "listing stress"), ("2023-07-05", "1:20 split", "further impairment"), ("2024-10-08", "1:15 split", "누적 1:3000"), ("2024-11-05", "secured financing·new leadership", "original thesis 종료")],
        lessons=["vendor-financed recurring revenue는 SaaS가 아니라 customer-credit investment다.", "headline cash에서 committed loans·inventory·burn을 차감한다.", "negative gross margin은 장기 TAM보다 빠른 falsifier다.", "reverse split·dilution을 original-share ledger로 복원한다."],
        checklist=["project별 cash out/in", "customer equity contribution", "loan collateral", "gross margin cohort", "receivable reserves", "cash runway", "fully diluted shares", "secured debt·covenants"],
        scorecard=scorecard("강한 실패", "강한 실패", "실패", "common 매우 취약", "강한 실패"), claims=claims,
    )


agrify_common(
    "a7f28838-2f64-4887-ad13-6390fce24e75", "2021-05-28", "bdon99", "analysis/ideas/2021/2021-05-28_AGFY_long.md",
    "https://www.valueinvestorsclub.com/idea/AGRIFY_CORP/7200503701", "$9.26; market cap ~$213m; EV ~$76m", "2~4년 TTK/VFU scale",
    "$138m cash, 2021 revenue guide $48~50m, VFU·software·10년 fee stream", "VFU/TTK recurring-platform Long",
    "cash-rich EV와 picks-and-shovels framing은 downside를 지키지 못했다. FY2022에 revenue가 정체한 채 gross loss -$31.8m, operating loss 약 -$193.3m과 $69.9m impairment가 나타났고 세 차례 reverse split·secured financing으로 original common economics가 붕괴했다.",
    "첫 TTK는 customer construction loan 약 $13.5m, VFU sale 약 $24m과 10년 nominal fee pool 약 $268m을 결합했다. $138m cash와 $1m 미만 long-term debt 때문에 operating business EV가 약 $76m로 보였고 2021 revenue guide $48~50m 상회 가능성이 강조됐다.",
    "headline EV $76m에 nominal fee pool을 비교한 방식은 cash가 project risk capital이라는 점을 빠뜨렸다. valuation은 `unrestricted cash - committed financing - expected burn + risk-adjusted project NPV + proven hardware/software value`여야 한다.",
    "첫 대형 TTK 고객의 cannabis price가 40% 하락하고 project가 12개월 지연될 때 Agrify loan recovery와 fee NPV, 추가현금 필요액은 얼마였는가?", 1.0, 4.5, False,
)


agrify_common(
    "5e6bf60d-f811-406d-bfda-ba23e0a3b785", "2022-02-21", "moneyball", "analysis/ideas/2022/2022-02-21_AGFY_long.md",
    "https://www.valueinvestorsclub.com/idea/AGRIFY_CORP/9360613418", "약 $6; net cash 약 $4/share", "2024 EBITDA bridge",
    "TTK EBITDA $56m + software $27m = $83m; target $55", "lower-entry net-cash·TTK EBITDA Long",
    "가격이 $6까지 내려와도 business value가 더 빨리 붕괴했다. 2024 TTK $56m+software $27m EBITDA bridge는 FY2022 negative gross profit에서 조기 반증됐고, reverse splits·secured financing·legacy sale로 $55 target의 security denominator도 유지되지 않았다.",
    "2021 idea 뒤 주가가 약 35% 내려 net cash가 $4/share로 보였다. 원문은 2024 TTK EBITDA $56m, software $27m, 합계 $83m에 hardware·brands optionality를 더하고 약 $55/share target를 제시했다. 당시 FactSet 2024 EBITDA 약 $33m보다도 훨씬 높은 독자 추정이었다.",
    "lower price는 동일 intrinsic value일 때만 margin of safety를 높인다. `net cash - forward burn - project losses + probability-weighted EBITDA`로 재평가하면 current gross economics가 확인되기 전 $83m에 high multiple을 줄 수 없다.",
    "2021 entry보다 35% 싸졌다는 사실을 모두 잊고, FY2022 gross margin과 customer-loan recovery만으로 새로 underwrite해도 이 common을 샀을 것인가?", 0.8, 4.2, True,
)


add(
    id="f1132f28-06d4-41ac-b7b9-a01ca4dd15e9", date="2000-08-29", author="david88", ticker="AGI",
    company="Alliance Gaming Corporation", filename="analysis/ideas/2000/2000-08-29_AGI_alliance_gaming_long.md",
    source="https://www.valueinvestorsclub.com/idea/Alliance_Gaming/1840155701", group="alliance", direction="Long", raw_direction="Short",
    security="Alliance Gaming common equity / Long", entry="historical nominal quote; exact split-adjusted basis 미복원", horizon="3~5년 gaming replacement·deleveraging",
    raw_horizon="debt ~$345m, equity ~$25m, TTM EBITDA ~$51.7m, interest ~$33.6m; tribal gaming·participation upside",
    title="leveraged gaming-equipment recovery Long", verdict="장기 매우 강한 성공 — Bally로 성장 후 $83.30 cash sale", score=9.5, process=8.0,
    conclusion="이 AGI는 Alamos Gold가 아니라 Alliance Gaming이다. debt 약 $345m 뒤 $25m equity가 gaming replacement·tribal casino·participation growth의 call option처럼 거래됐다. 회사는 살아남아 Bally Technologies가 되었고 2014 Scientific Games가 $83.30 cash/share에 인수했다. split ledger가 없어 exact multiple/IRR은 만들지 않는다.",
    t0="TTM EBITDA 약 $51.7m에 interest expense 약 $33.6m, debt 약 $345m, equity value 약 $25m으로 common cushion이 매우 얇았다. 원문은 replacement demand, California Native American casinos, cashless systems와 Betty Boop 등 participation games의 recurring economics가 조금만 개선돼도 equity residual이 비선형적으로 커진다고 봤다.",
    reverse="enterprise value가 debt hurdle 아래로 조금만 내려가도 common은 0에 가까워질 수 있었다. management void·governance, product acceptance, casino capex와 regulatory timing이 모두 위험했고, 7.1x EV/EBITDA는 low equity market cap만큼 싸지 않을 수 있었다.",
    valuation="common을 EBITDA multiple로 바로 value하지 않고 debt·interest·maintenance capex 뒤 residual을 본다. base는 interest coverage 개선, bull은 recurring participation mix와 replacement upcycle, bear는 covenant/refinancing failure다. $83.30 takeout은 terminal event지만 2000 share basis를 복원해야 entry multiple이 된다.",
    actual="Alliance는 industry survivor가 되어 2006 Bally Technologies로 사명을 변경했다. gaming equipment·systems platform은 strategic value를 키웠고 2014-08 Scientific Games와 $83.30 cash/share merger agreement를 체결, 2014-11-21 거래가 완료됐다. total merger-related consideration은 약 $3.2bn이었다.",
    price="$83.30 terminal cash는 common value가 크게 창출됐음을 검증하지만 2000 nominal quote와 직접 나누지 않는다. 14년 동안의 split·issuance·distribution을 완전히 복원하지 않았기 때문이다. 장기 판정은 매우 강한 성공, exact multiple·IRR은 미확정이다.",
    drivers="operating franchise가 debt service hurdle을 넘자 thin equity의 convexity가 작동했다. installed base·systems·participation revenues와 consolidation value가 enterprise value를 키웠고, 최종 strategic buyer가 cash로 crystallize했다.",
    counterfactual="EBITDA가 15% 감소하고 refinancing spread가 500bp 넓어질 때 interest coverage와 covenant headroom이 얼마였으며 common recovery가 0이 되는 enterprise value는 어디였는가?",
    error="$25m equity가 작다는 사실을 cheapness처럼 볼 수 있지만 실제 exposure는 $345m debt를 포함한 enterprise였다. governance와 refinancing risk에 명확한 position-size·stop rule이 부족했다.",
    warning="사전 핵심경고는 EBITDA/interest가 1x에 가까워지거나 maturities가 막히는 것이었다. 반대로 2006 사명변경·확장된 platform은 survival과 thesis 진전의 확인신호였다.", first_signal_date="2006-03-06",
    scenarios=[("Bear", "EBITDA 하락·refinancing failure", "common near-zero", "미실현"), ("Base", "replacement·coverage 개선", "deleveraging rerating", "실현"), ("Bull", "recurring mix·strategic sale", "large convex upside", "$83.30 cash")],
    metrics=[("Debt/equity", "$345m/$25m", "equity convexity", "survival·strategic value", "강한 성공"), ("TTM EBITDA", "$51.7m", "성장", "platform scaled", "성공 방향"), ("Interest", "$33.6m", "coverage 개선", "insolvency 회피", "성공"), ("Name/entity", "Alliance AGI", "lineage 유지", "Bally 2006", "교정 완료"), ("Terminal", "없음", "deleveraging/upside", "$83.30 cash 2014", "매우 강한 성공")],
    timeline=[("2000-08-29", "VIC Alliance Long", "leveraged call option"), ("2001~03", "gaming recovery", "survival test"), ("2004", "installed base 확대", "recurring mix"), ("2006-03-06", "Bally Technologies 사명", "entity lineage"), ("2013", "SHFL acquisition", "platform scale"), ("2014-08-01", "Scientific Games agreement", "$83.30 cash"), ("2014-11-21", "merger completed", "common crystallized"), ("2014-11-25", "completion 8-K", "delisting·$3.2bn")],
    lessons=["historical ticker는 날짜·제품·legal entity로 다시 식별한다.", "thin equity는 low market cap이 아니라 debt hurdle 위 residual이다.", "replacement cycle과 participation recurring economics를 분리한다.", "장기 corporate-action return은 split ledger 없이 정밀화하지 않는다."],
    checklist=["legal entity/CIK", "debt maturity", "EBITDA/interest", "maintenance capex", "participation installed base", "replacement orders", "covenants", "split-adjusted share history"],
    scorecard=scorecard("강한 성공", "성공", "강한 성공", "high-risk common", "장기 성공"),
    claims=[
        claim("replacement cycle recovery", "성공", "aging casino floor가 new machines 수요를 만든다.", "installed base replacement가 new casino openings와 별도 volume driver다.", "aging units·product cycle.", "Alliance products가 competitive하다.", "orders·market share 악화면 반증.", "Bally는 major equipment supplier로 성장했다.", "장기 방향 적중.", "industry demand와 company share를 섞었다.", "shipments·share·ASP를 분리한다."),
        claim("tribal gaming expansion", "성공 방향", "California/Native American casinos가 addressable units를 늘린다.", "new floors가 machines·systems와 recurring service를 요구한다.", "regulatory/compact expansion.", "regulation과 financing이 실제 openings로 이어진다.", "opening 지연·caps면 반증.", "tribal gaming은 업계 장기 성장축이 됐다.", "company-specific attribution 제한.", "industry growth와 Alliance share gain을 충분히 분리하지 않았다.", "jurisdiction별 approved/open units를 추적한다."),
        claim("participation games recurring value", "성공", "shared-revenue titles가 equipment sale보다 질 높은 cash를 만든다.", "daily win share가 installed base recurring revenue로 누적된다.", "Betty Boop 등 product pipeline.", "game performance와 casino retention이 유지된다.", "win/unit·installed units 감소면 반증.", "gaming operations·systems가 Bally franchise value의 일부가 됐다.", "개별 title cohort 미복원.", "몇 개의 초기 title을 durable portfolio economics로 일반화했다.", "installed units×win/day×share를 본다."),
        claim("leverage가 common convexity 제공", "매우 강한 성공", "작은 EBITDA 개선이 $25m equity를 크게 키운다.", "enterprise value 상승이 fixed debt hurdle 위 residual로 집중된다.", "$345m debt·$25m equity.", "refinancing 전 EBITDA가 debt service를 감당한다.", "coverage<1x·covenant breach면 실패.", "company survived and terminal common received $83.30/share.", "convex upside 현실화.", "동일 leverage의 zero-risk처럼 서술할 위험.", "default probability와 position sizing을 함께 둔다."),
        claim("management/governance discount는 해소", "성공", "management void와 governance 문제가 repairable하다.", "better leadership·controls가 products와 cash conversion을 살린다.", "low valuation과 identifiable operating assets.", "governance failure가 liquidity를 먼저 고갈시키지 않는다.", "fraud·refinancing failure면 반증.", "Bally로 rebrand·scale되고 strategic buyer에 매각됐다.", "terminal outcome 지지.", "governance 개선의 정확한 causal proof 부족.", "person risk를 board·incentive·controls로 검증한다."),
        claim("strategic terminal value", "매우 강한 성공", "industry asset가 standalone multiple 이상 가치를 가질 수 있다.", "buyer synergies·installed base·systems가 premium을 지지한다.", "scarce gaming platform.", "antitrust·financing·license approvals이 가능하다.", "bid 부재·discount sale이면 미실현.", "2014 $83.30 cash/share, 약 $3.2bn consideration.", "cash terminal 확정.", "takeout은 T0 base가 아니었다.", "strategic upside를 standalone survival 뒤에만 얹는다."),
    ],
)


add(
    id="4c932189-e6bd-4e47-8b2a-92e6eba0e467", date="2014-03-31", author="andrew152", ticker="AGI",
    company="Alamos Gold Inc.", filename="analysis/ideas/2014/2014-03-31_AGI_alamos_gold_long.md",
    source="https://www.valueinvestorsclub.com/idea/ALAMOS_GOLD_INC/0481433134", group="alamos", direction="Long", raw_direction="Long",
    security="TSX/NYSE:AGI common equity / Long", entry="원문 약 C$10; source DB next-session close 8.47491", horizon="2016 Turkey start·production >400koz",
    raw_horizon="0.9x NAV→1.5x, target ~C$18; Kirazli/Agi Dagi permits와 debt-free cash",
    title="Turkey development-NAV rerating Long", verdict="실패 — permit·production·horizon 미실현", score=3.5, process=6.5,
    conclusion="debt-free balance sheet는 회사를 지켰지만 투자 thesis의 clock은 Turkey였다. Kirazli/Agi Dagi가 2016 생산을 만들지 못했고 2015 AuRico merger로 perimeter가 바뀌었다. source DB price-only return은 1Y -34.8%, 2Y -41.4%, 3Y -9.8%로 원 horizon에서 실패했다.",
    t0="Alamos는 cash 약 $475m, no debt와 Mulatos cash flow를 가졌고 Turkey projects·Esperanza를 포함한 NAV 약 C$1.678bn 대비 약 0.9x에 거래된다고 봤다. permits와 construction이 진행되면 2016 production 400koz+, 1.5x NAV와 약 C$18 target가 가능하다는 논지였다.",
    reverse="development NAV는 permit, local opposition, litigation, financing, construction와 start-up timing을 모두 통과해야 한다. 현금은 delay survival을 주지만 NPV timing loss와 gold-price beta를 제거하지 않는다. 1.5x NAV는 execution뿐 아니라 sector multiple rerating도 필요했다.",
    valuation="project NAV에는 `permit probability × build probability × start-date discount`를 적용하고 cash는 corporate G&A·care-and-maintenance·future capex를 차감한다. acquired production은 original organic forecast와 분리한다. source DB returns는 price-only이며 original C$ quote와 통화·listing basis가 다를 수 있다.",
    actual="Turkey는 원래 2016 production schedule를 달성하지 못했다. 2015 AuRico merger로 Young-Davidson 등 새 assets가 들어오며 original company perimeter가 변경됐고 combined 2016 production도 약 392koz였다. 이후 Alamos 성공을 이 2014 Turkey thesis의 horizon 성공으로 소급하지 않는다.",
    price="source DB next-session base 8.47491에서 1Y ratio 0.651929(-34.8%), 2Y 0.585638(-41.4%), 3Y 0.901842(-9.8%)다. dividend·tax 제외이며 5Y row는 없다. 원문 약 C$10 quote와 DB price의 단위 차이 때문에 exact original-position IRR이 아니라 horizon 판정에만 쓴다.",
    drivers="손실은 gold weakness와 project timing discount 확대가 만들었다. cash/no debt는 insolvency를 막았지만 permit delay로 NPV가 멀어졌고, merger는 assets를 바꿔 original Turkey catalyst의 direct payoff를 희석했다.",
    counterfactual="Turkey가 3년 늦어지고 금값이 15% 낮아져도 0.9x stated NAV가 실제 risk-adjusted NAV 대비 할인인가, 오히려 premium인가?",
    error="unrisked project NAV를 높은 weight로 쓰고 permit/legal clock을 binary catalyst처럼 봤다. no-debt를 share-price floor로, M&A production을 organic thesis validation으로 볼 위험도 있었다.",
    warning="2014~15 Turkey schedule가 미끄러지고 주가가 1Y -34.8%가 된 시점에 timing thesis는 반증됐다. 2015 merger는 original idea를 새 security/perimeter로 재인수할 사건이었다.", first_signal_date="2015-03-31",
    scenarios=[("Bear", "Turkey multi-year delay·gold weakness", "NAV discount 확대", "1Y -34.8%, 2Y -41.4%"), ("Base", "permits·2016 >400koz", "~C$18", "미실현"), ("Bull", "1.5x NAV·projects on time", "C$18+", "미실현")],
    metrics=[("1Y price-only", "Long", "상승", "-34.8%", "실패"), ("2Y price-only", "Long", "target 접근", "-41.4%", "강한 실패"), ("3Y price-only", "Long", "rerating", "-9.8%", "실패"), ("2016 production", ">400koz organic framing", ">400koz", "~392koz combined", "실패"), ("Turkey start", "2016", "production", "미실현", "강한 실패")],
    timeline=[("2014-03-31", "VIC Long", "~0.9x NAV"), ("2014-09", "gold weakness", "NAV beta"), ("2015-03-31", "1Y -34.8%", "timing break"), ("2015", "AuRico merger", "perimeter change"), ("2016-03-31", "2Y -41.4%", "security failure"), ("2016", "combined production ~392koz", ">400koz miss"), ("2017-03-31", "3Y -9.8%", "미회복"), ("2020", "Turkey still non-producing", "original clock failure")],
    lessons=["development-mine NAV에는 permit·build·time probability를 곱한다.", "debt-free cash는 survival asset이지 share-price floor가 아니다.", "M&A 뒤 acquired ounces로 original organic forecast를 구제하지 않는다.", "commodity beta와 company execution을 각각 score한다."],
    checklist=["permit/legal milestones", "local opposition", "capex funding", "construction critical path", "organic vs acquired ounces", "gold sensitivity", "risked NAV", "cash after commitments"],
    scorecard=scorecard("survival 성공", "실패", "강한 실패", "common 손실", "실패"),
    claims=[
        claim("debt-free cash downside", "부분 성공", "~$475m cash·no debt가 downside를 제한한다.", "cash가 project delay와 gold downturn을 self-fund한다.", "strong balance sheet.", "cash가 capex·G&A에 과도하게 소모되지 않는다.", "large drawdown에도 floor 부재면 valuation claim 약화.", "company survived·merged했지만 2Y price -41.4%.", "survival 성공/price floor 실패.", "balance sheet와 equity volatility를 혼동했다.", "cash는 per-share commitments 차감 후 본다."),
        claim("Turkey permits·2016 start", "강한 실패", "Kirazli/Agi Dagi가 permit을 받아 2016 생산한다.", "low-cost new ounces가 NAV와 cash flow를 현실화한다.", "project studies·EIA progress.", "legal·social license가 schedule 내 해결된다.", "permit delay 12개월+면 반증.", "Turkey는 2016 production asset가 되지 못했다.", "start date 수년 miss.", "binary approval만 보고 local/legal duration을 축소했다.", "permit tree에 dates와 probabilities를 둔다."),
        claim("2016 production >400koz", "실패", "Turkey+Mulatos growth로 >400koz다.", "new mine ramp가 ounces를 늘린다.", "project schedule와 base operations.", "construction·ramp가 계획대로다.", "organic production <360koz면 실패.", "AuRico merger 후 combined production도 약 392koz.", "acquired 포함 target 미달.", "organic/acquired denominator를 섞었다.", "mine별 ounce bridge를 유지한다."),
        claim("0.9x NAV는 cheap", "실패", "stated NAV 대비 10% 할인이다.", "de-risking이 1.0~1.5x multiple을 만든다.", "NAV ~$1.678bn.", "project NAV가 timely realizable하다.", "risked NAV가 market value 이하이면 반증.", "delay와 gold weakness로 1~2Y price가 크게 하락했다.", "2Y -41.4%.", "unrisked NAV를 denominator로 썼다.", "project마다 probability·time haircut를 적용한다."),
        claim("1.5x NAV·C$18 target", "강한 실패", "permit·production 뒤 premium rerating이 온다.", "growth scarcity와 balance sheet가 premium을 지지한다.", "peer multiple와 asset pipeline.", "sector multiple과 gold price가 유지된다.", "discount 지속·price target miss면 실패.", "source horizons 모두 target 미달, 2Y 큰 손실.", "target 미실현.", "execution success와 sector rerating을 동시에 요구했다.", "EPS/FCF와 NAV multiple catalysts를 분리한다."),
        claim("M&A optionality", "현실화·원논지 구제 아님", "cash와 management가 consolidation option을 가진다.", "merger가 operating assets와 scale을 추가한다.", "strong balance sheet.", "deal terms가 value accretive하다.", "dilutive perimeter change면 재인수.", "2015 AuRico merger가 발생했다.", "option 현실화, original Turkey path 대체.", "event를 자동 success로 볼 위험.", "deal 후 thesis를 new idea unit로 다시 쓴다."),
    ],
)


add(
    id="e730e79a-5248-410c-a2a9-7214e57ce1f6", date="2018-11-18", author="EITR210", ticker="AGI.",
    company="Alamos Gold Inc.", filename="analysis/ideas/2018/2018-11-18_AGI_alamos_gold_long.md",
    source="https://www.valueinvestorsclub.com/idea/ALAMOS_GOLD_INC/4349354391", group="alamos", direction="Long", raw_direction="Long",
    security="NYSE:AGI common equity / Long", entry="약 US$3.60", horizon="2~4년 Young-Davidson fix·Island Gold reserve growth",
    raw_horizon="$1,200 gold에서 $5.15 target; lower-mine infrastructure와 debt-free balance sheet",
    title="operating-bottleneck repair·asset-quality Long", verdict="매우 강한 성공 — operational fix·reserve growth·target 초과", score=9.6, process=8.8,
    conclusion="2014의 Turkey option이 아니라 가동광산 repair를 샀다. Young-Davidson lower-mine expansion은 2020 완료됐고 Island Gold reserves는 acquisition 이후 2020까지 depletion 순감 후 74% 늘었다. 2025 production 545.4koz·FCF $351.7m, 2026-09 market check $35.72로 $3.60 entry와 $5.15 target를 크게 넘었다. 다만 gold beta를 company alpha와 분리한다.",
    t0="Young-Davidson bottleneck과 acquisition complexity 때문에 shares가 약 $3.60, 0.5x book 이하로 보였다. debt-free balance sheet, Island Gold의 high-grade reserve potential과 lower-mine shaft/crusher/conveyor가 완료되면 $1,200 gold에서도 $5.15가 가능하다는 thesis였다. 2018 production은 505koz였다.",
    reverse="Young-Davidson expansion은 capital·commissioning risk가 있었고 Island Gold reserve additions가 economic ounces로 전환되지 않을 수 있었다. mine valuation은 gold price에 민감하며 low book multiple 일부는 cost·jurisdiction·asset-quality 차이를 반영한다. 장기 return 대부분이 gold 상승일 가능성도 있었다.",
    valuation="mine별 risked NAV와 through-cycle FCF를 사용한다. $5.15 target는 $1,200 gold base에서 operating fix의 value를 테스트하고, 실제 장기 price는 realized gold price·new acquisitions·share count를 별도 attribution한다. 2026 market price는 시점 cross-check이며 total return·IRR이 아니다.",
    actual="2018 production은 505koz, year-end cash $206m·debt 없음이었다. Young-Davidson lower-mine expansion은 2020-07 완료돼 roughly 8,000 tpd design path를 열었다. Island Gold reserves는 2017 acquisition 이후 2020까지 74% 증가했다. 2025 production 545.4koz와 record FCF $351.7m, Q1 2026 FCF $101.7m을 기록했다.",
    price="2026-09-18 market cross-check $35.72는 $3.60의 약 9.9x이고 $5.15 target를 크게 초과한다. 이는 price-only point comparison이며 배당·세금·holding ledger가 없어 IRR로 쓰지 않는다. 또한 2018 $1,200 assumption보다 높은 gold prices와 후속 portfolio changes가 장기 payoff에 크게 기여했다.",
    drivers="company-specific value는 lower-mine bottleneck removal, Island Gold reserve growth와 debt-free funding capacity에서 왔다. macro value는 gold-price 상승에서 왔다. 좋은 entry는 execution과 commodity beta 모두에 option value를 줬지만 두 기여를 전부 management alpha로 귀속하면 안 된다.",
    counterfactual="gold가 계속 $1,200이고 lower-mine ramp가 12개월 늦어졌어도 mine-level FCF와 risked NAV만으로 $5.15 target가 성립했는가?",
    error="핵심 mechanism은 좋았지만 long-run outcome에서 gold beta와 later acquisitions를 원 thesis alpha로 과대귀속할 수 있다. book value discount 역시 mine-quality와 future capex를 충분히 반영해야 한다.",
    warning="명확한 thesis break는 없었다. 사전 경고는 lower-mine commissioning 지연, sustained throughput 8,000 tpd 미달과 Island Gold reserve replacement 실패였는데 핵심 milestone은 반대로 달성됐다.", first_signal_date="2020-07-14",
    scenarios=[("Bear", "lower-mine delay·$1,100 gold", "$2.5~3.5", "미실현"), ("Base", "fix·$1,200 gold", "$5.15", "target 초과"), ("Bull", "Island growth·gold upside", "multi-bagger", "$35.72 point check")],
    metrics=[("Entry/target", "$3.60/$5.15", "+43%", "$35.72 point check", "매우 강한 성공"), ("2018 production", "505koz", "stable/grow", "505koz", "기반 확인"), ("YD lower mine", "under construction", "completion", "2020-07 완료", "강한 성공"), ("Island reserves", "growth thesis", "replace depletion", "+74% since 2017 by 2020", "강한 성공"), ("2025 production/FCF", "long-run quality", "cash generation", "545.4koz/$351.7m", "성공")],
    timeline=[("2018-11-18", "VIC Long", "$3.60→$5.15"), ("2018-12-31", "505koz production", "base established"), ("2019", "lower-mine construction", "execution period"), ("2020-07", "lower mine completed", "bottleneck catalyst"), ("2020-12-31", "Island reserves +74%", "asset quality"), ("2021", "8,000 tpd framework", "throughput validation"), ("2025-12-31", "545.4koz·$351.7m FCF", "cash realization"), ("2026-09-18", "$35.72 market check", "target far exceeded")],
    lessons=["가동광산 bottleneck fix는 distant permit optionality보다 검증 가능하다.", "reserve growth는 acquisition quality를 depletion 순감 후 평가한다.", "debt-free balance sheet는 growth-capex 동안 option value를 준다.", "commodity beta와 company execution return을 분리한다."],
    checklist=["mine throughput", "grade/recovery", "commissioning date", "reserve additions net depletion", "mine-site FCF", "growth capex", "net cash", "gold-price attribution"],
    scorecard=scorecard("강한 성공", "강한 성공", "강한 성공", "common 적절", "강한 성공"),
    claims=[
        claim("Young-Davidson lower-mine fix", "강한 성공", "shaft·crusher·conveyor가 bottleneck을 제거한다.", "ore-handling reliability와 throughput가 cost/oz와 FCF를 개선한다.", "defined infrastructure project.", "commissioning이 budget·schedule에 가깝다.", "completion delay·throughput miss면 반증.", "2020-07 lower-mine expansion이 완료됐다.", "dated catalyst 실현.", "ramp와 mechanical completion을 같게 볼 위험.", "completion 뒤 sustained throughput를 확인한다."),
        claim("~8,000 tpd sustainable rate", "성공", "lower mine가 약 8,000 tpd를 지원한다.", "higher steady mining rate가 fixed-cost absorption과 ounces를 안정화한다.", "design/ramp plan.", "grade·equipment availability가 유지된다.", "sustained rate 크게 미달하면 실패.", "후속 reserve framework와 operations가 8,000 tpd path를 지지했다.", "정확한 매분기 rate는 별도 추적 필요.", "design을 realized average로 부르지 않는다.", "quarterly tonnes·grade·cost를 같이 본다."),
        claim("Island Gold reserve quality", "강한 성공", "high-grade asset가 acquisition value를 키운다.", "reserve additions net depletion이 mine life·NPV를 높인다.", "exploration potential과 grades.", "drilling success가 economic reserve로 전환된다.", "reserve replacement <100%면 약화.", "2020 reserves는 2017 acquisition 이후 net depletion 기준 +74%.", "강한 초과달성.", "resource와 reserve를 섞을 수 있다.", "reserve conversion·grade·cost를 따로 기록한다."),
        claim("debt-free balance sheet", "성공", "cash/no debt가 projects를 self-fund한다.", "funding stress 없이 lower mine·exploration을 지속한다.", "2018 cash $206m·no debt.", "capex와 gold downside를 cash flow가 감당한다.", "dilutive equity·distress debt면 실패.", "growth investment 뒤 record 2025 FCF와 positive net liquidity를 확보했다.", "resilience 확인.", "후속 portfolio 변화 영향 존재.", "project-level sources/uses로 본다."),
        claim("$5.15 at $1,200 gold", "강한 성공", "operating repair만으로 43% upside다.", "risk discount 축소와 mine FCF 정상화가 target를 만든다.", "mine NAV·low entry.", "gold가 base 근처이고 fix가 성공한다.", "fix 뒤 target 미달이면 실패.", "장기 market check $35.72로 target 초과.", "초과분 상당 부분 gold beta.", "target hit와 attribution을 혼용할 수 있다.", "base-gold and actual-gold value를 분리한다."),
        claim("long-run FCF compounding", "강한 성공", "quality assets가 capital investment 뒤 cash를 낸다.", "reserve growth·throughput·price가 mine-site FCF로 전환된다.", "asset quality와 low leverage.", "capex가 끝나고 cash conversion이 나타난다.", "persistent negative FCF면 실패.", "2025 company FCF $351.7m, Q1 2026 $101.7m.", "cash outcome 확인.", "high gold price 도움 큼.", "volume·margin·price bridge로 attribution한다."),
    ],
)


ORDER = [
    "debdba95-f3d2-4ac6-a115-22fd561777e4",
    "604072e8-d449-41cb-8a21-76eb2513f1a5",
    "3fbf61ca-ad89-448a-9f3f-22a821e543c8",
    "24cf0eb8-cf98-4327-9b5f-f9440b5fee39",
    "3af1399f-2fde-41f0-90b1-910f4bbfbb7f",
    "a7f28838-2f64-4887-ad13-6390fce24e75",
    "5e6bf60d-f811-406d-bfda-ba23e0a3b785",
    "f1132f28-06d4-41ac-b7b9-a01ca4dd15e9",
    "4c932189-e6bd-4e47-8b2a-92e6eba0e467",
    "e730e79a-5248-410c-a2a9-7214e57ce1f6",
]


def idea_sources(i):
    original = S(
        "VIC original idea" if i["source"] else "VIC source-DB preserved original",
        i["source"], "Value Investors Club / source SQL", i["date"],
        "T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.", "원문",
    )
    sources = [original, *SOURCES[i["group"]]]
    if i["id"] == "e730e79a-5248-410c-a2a9-7214e57ce1f6":
        sources.append(S("AGI market-price cross-check", "", "market data", "2026-09-18", "$35.72 point-in-time price; total return·IRR이 아닌 target comparison에만 사용.", "시장데이터"))
    return sources


def render_index():
    rows = []
    for n, i in enumerate(IDEAS, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(f"| {n} | {i['date']} | {i['ticker']} | {i['raw_direction']} | {i['direction']} | [{i['company']}]({rel}) | {i['verdict']} |")
    return "\n".join([
        "# Batch 071 — AGC / American General / Springleaf / AGCO / Argentex / Agrify / Alliance / Alamos V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. 회사 identity·증권·방향·corporate action을 먼저 교정하고 official filings로 actual을 검증했다.", "",
        "## Canonical idea files", "", "| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## Metadata / security / return audit", "",
        "- AGC 2016, AGC1 2009, AGI 2000의 raw Short를 실제 Long으로 교정했다.",
        "- AGC1 2009·2012는 common이 아니라 senior unsecured debt다.",
        "- 2000 AGI는 Alamos Gold가 아니라 Alliance Gaming이며 2006 Bally Technologies로 사명이 바뀌었다.",
        "- AGCO 2015·Alamos 2014만 source-DB performance row를 보존했다. 나머지는 complete ledger 없이 exact IRR을 만들지 않았다.",
        "- Agrify는 2022·2023·2024 reverse splits가 누적 1-for-3,000이고 중간 dilution도 있어 nominal price comparison을 폐기했다.", "",
        "## 핵심 판정", "",
        "1. AGC는 liquid NAV discount가 약 19%에서 8%로 좁혀지고 15% tender·NAV merger까지 이어진 강한 성공이다.",
        "2. AGF/Springleaf 두 credit는 equity가 아니라 maturity·seniority·refinancing을 산 성공 사례다.",
        "3. AGCO는 주가와 cycle call은 성공했지만 10% operating-margin bull case는 실패했다.",
        "4. Argentex는 low-capex와 low-liquidity-risk를 혼동해 2.49p rescue offer로 끝난 실패다.",
        "5. Agrify 두 vintage는 headline cash·backlog·software optionality가 negative gross economics를 구하지 못했다.",
        "6. AGI ticker는 Alliance/Bally 장기 성공, Alamos 2014 실패, Alamos 2018 강한 성공이라는 서로 다른 entity·mechanism을 담는다.", "",
        "## 구조화 데이터", "",
        "- `data/curated/batch_071_agc_agc1_agco_agfx_agfy_agi_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.",
        "- `data/curated/batch_071_source_catalog.json`: raw metadata source packet이며 production payload glob에는 포함되지 않는다.",
        "- `analysis/batch_071_agc_agc1_agco_agfx_agfy_agi_10.md`: Streamlit wrapper.", "",
    ])


def main():
    IDEAS.sort(key=lambda i: ORDER.index(i["id"]))
    if [i["id"] for i in IDEAS] != ORDER:
        raise ValueError("Batch 071 idea order or IDs do not match catalog boundary")
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
            "**B/C** — AGCO 2015·Alamos 2014는 source SQL price-only ratios, 그 외는 verified corporate action·official operating actual·제한적 market cross-check만 사용. complete dated ledger 없이는 total return·IRR을 만들지 않음.",
        )
        report_path.write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_071_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 071 — AGC / AGC1 / AGCO / AGFX / AGFY / AGI V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 071 V9 Index](batch_071_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_071_agc_agc1_agco_agfx_agfy_agi_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 71
    payload["title"] = "AGC / American General / Springleaf / AGCO / Argentex / Agrify / Alliance / Alamos — Discount, Credit, Liquidity and Execution V9"
    payload["metadata_audit"] = {
        "direction_corrections": 3,
        "security_type_corrections": 2,
        "company_mapping_corrections": 1,
        "split_adjustments": 2,
        "performance_rows_preserved": 2,
        "performance_rows_missing": 8,
        "cross_batch_duplicates_removed": 0,
        "corporate_action_terminal_payoffs": 4,
        "notes": [
            "AGC 2016, AGC1 2009, AGI 2000 raw Short를 실제 Long으로 교정하고 raw flag를 보존했다.",
            "AGC1 2009·2012를 senior unsecured debt로 교정했다.",
            "AGI 2000은 Alliance Gaming/Bally이며 Alamos Gold mapping을 폐기했다.",
            "AGCO 2015·Alamos 2014 source-DB price-only rows만 사용했다.",
            "Agrify 두 idea의 세 reverse split 누적 1:3,000과 dilution 때문에 raw nominal return을 만들지 않았다.",
            "AGC tender/merger, Springleaf exchange/repurchase, Bally cash merger와 Argentex rescue offer를 security별 payoff로 반영했다.",
        ],
    }
    payload["batch_lessons"] = [
        "CEF는 NAV return·discount·distribution·leverage·tender를 분해한다.",
        "distressed financial credit는 issuer headlines보다 maturity·seniority·encumbrance를 먼저 본다.",
        "exchange offer는 default avoidance와 holder return을 분리한다.",
        "cyclical stock success가 peak-margin forecast를 검증하지 않는다.",
        "low capex와 low liquidity capital은 다른 개념이다.",
        "vendor-financed recurring revenue는 customer-credit exposure다.",
        "historical ticker는 date·legal entity·security로 식별한다.",
        "mine NAV는 permit clock, operating thesis는 throughput·reserve·FCF로 검증한다.",
    ]
    failure_patterns = {
        "agc_cef": "distribution_quality; leverage; discount_duration; tender_proration",
        "agf_credit": "maturity_wall; encumbrance; support_vs_guarantee; exchange_duration",
        "agco": "peak_margin; cycle_denominator; source_entry_mismatch; forecast_vs_stock",
        "argentex": "liquidity_tail; collateral_timing; excess_cash_error; low_capex_fallacy",
        "agrify": "vendor_financing; negative_gross_margin; cash_burn; dilution; backlog_quality",
        "alliance": "ticker_collision; leverage; governance; refinancing; split_history",
        "alamos": "permit_duration; unrisked_nav; commodity_beta; perimeter_change",
    }
    success_patterns = {
        "agc_cef": "liquid_nav; discount_catalyst; tender; nav_merger",
        "agf_credit": "security_selection; maturity_focus; funding_normalization; pull_to_par",
        "agco": "trough_entry; balance_sheet; cycle_inflection; capital_return",
        "argentex": "stress_liquidity; collateral_waterfall; counterparty_limits; rescue_trigger",
        "agrify": "cash_commitments; project_collections; gross_profit_gate; fully_diluted_ledger",
        "alliance": "entity_audit; enterprise_residual; recurring_mix; strategic_exit",
        "alamos": "risked_nav; operating_bottleneck; reserve_replacement; fcf_attribution",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failure_patterns[idea["group"]]
        row["success_pattern_ko"] = success_patterns[idea["group"]]
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
