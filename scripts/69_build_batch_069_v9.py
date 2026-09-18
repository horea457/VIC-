#!/usr/bin/env python3
"""Build Batch 069 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
CATALOG = ROOT / "data/curated/batch_069_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_deep_v7.json"

spec = importlib.util.spec_from_file_location("batch64_base", ROOT / "scripts/64_build_batch_064_v9.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "afmi": "Affinity Media는 IPO proceeds를 trust에 보관한 blank-check company였다. merger 승인 전 common의 가치는 trust cash와 redemption/liquidation rights, deal 성공 시 교부될 operating-company equity, sponsor dilution과 청산 뒤 residual shell 가치의 합이다.",
    "alphamin": "Alphamin은 DRC Mpama Bisie에서 초고품위 tin ore를 채굴·선광한다. grade와 recovery가 생산량을, tin price와 물류·보안·tax가 현금마진을 결정하며 Mpama South는 단일광산 위험을 낮추고 처리량을 확대하는 두 번째 ore source다.",
    "agi": "Ag Growth Income Fund는 grain handling·storage·conditioning 장비를 만드는 niche manufacturer였다. replacement demand와 dealer network가 매출을 지지하고, 높은 market share·margin에서 maintenance capex와 cash distribution을 뺀 unit-holder cash가 가치의 핵심이었다.",
    "afop": "Alliance Fiber Optic Products는 telecom·datacenter용 passive optical components를 설계·제조했다. 매출 mix와 utilization이 gross margin을 좌우하고, R&D·capex 뒤 현금과 net cash, 고객 qualification 및 strategic scarcity가 common의 payoff를 결정했다.",
    "aluflex": "Aluflexpack은 식품·pet food·pharma용 aluminum·flexible packaging을 생산했다. volume·price/mix에서 aluminum·energy·labour와 conversion cost를 빼고, 신규 capacity ramp와 working capital·capex를 반영한 현금이 equity에 귀속된다.",
    "afr": "American Financial Realty Trust는 금융기관이 사용하던 office·operations properties를 매입·임대하는 REIT였다. occupancy와 rent에서 property cost·G&A·interest·maintenance capex를 뺀 AFFO와 주당 dividend가 가치의 핵심이며, debt-funded acquisition은 반드시 주당 기준으로 검증해야 한다.",
    "afrisam_note": "AfriSam은 남아공 cement producer였지만 이 아이디어의 증권은 common이 아니라 senior secured floating-rate notes였다. enterprise value에서 secured claims와 구조조정 비용을 차감한 recovery, coupon·swap·maturity와 debt-to-equity 교환조건이 수익을 결정한다.",
    "affirm": "Affirm은 merchant checkout에 BNPL installment loans를 제공한다. merchant fee·consumer interest에서 funding cost·credit loss·servicing·technology 비용을 빼며, GMV growth보다 revenue less transaction costs, funding access, vintage loss와 merchant concentration이 경제성을 보여준다.",
    "amtrust": "AmTrust는 small-commercial P&C, warranty와 specialty risk를 인수하던 보험사였다. earned premium과 investment income에서 losses·expenses·reinsurance cost를 뺀 underwriting result, reserve adequacy와 statutory capital이 book-value growth를 결정한다.",
}

ENGINE = {
    "afmi": "trust cash + merger equity value - sponsor/promote dilution - transaction cost + liquidation residual = common payoff; vote·redemption·liquidation date를 실제 ledger로 잇는다.",
    "alphamin": "ore tonnes × grade × recovery × payable tin price - mining·processing·logistics·security - tax - sustaining/growth capex = distributable cash.",
    "agi": "units sold × price - steel·labour·factory overhead - SG&A - tax - maintenance capex ± working capital = distributable cash; acquisition은 incremental FCF/unit로 본다.",
    "afop": "optical-component volume × ASP × gross margin - R&D - SG&A - tax - capex ± working capital = FCF; net cash와 split-adjusted shares를 적용한다.",
    "aluflex": "volume × price/mix - aluminum·energy·labour - plant overhead - SG&A - tax - capex ± working capital = equity FCF; ramp utilization과 acquisition consideration을 분리한다.",
    "afr": "occupied area × rent - property opex - G&A - cash interest - recurring capex = AFFO; acquisition debt와 issued shares를 반영해 AFFO/share와 dividend coverage를 본다.",
    "afrisam_note": "restructuring enterprise value - super-priority/secured claims - costs = noteholder recovery; cash/PIK coupon·principal·equity conversion을 날짜별로 합산한다.",
    "affirm": "GMV × merchant/interest take rate - funding cost - provision/credit loss - processing·servicing - opex = equity economics; securitization gain과 fair-value 변동을 분리한다.",
    "amtrust": "earned premium × (1-loss ratio-expense ratio) + investment income - tax = book growth; reserve development·related-party reinsurance·capital actions을 common에 반영한다.",
}

KPI = {
    "afmi": "trust cash/share, redemption terms, vote threshold, sponsor promote, merger exchange ratio, liquidation deadline, residual shares, cash settlement",
    "alphamin": "ore grade, recovery, contained tin, payable price, AISC/cash cost, EBITDA, net debt, capex, Mpama South ramp, dividend/share, security interruptions",
    "agi": "organic volume, market share, gross/EBITDA margin, maintenance capex, working capital, FCF/unit, payout ratio, leverage, acquisition multiple",
    "afop": "revenue mix, gross margin, operating income, R&D, capex, net cash/share, customer concentration, split factor, dividends/distributions",
    "aluflex": "volume, price/mix, aluminum pass-through, EBITDA margin, utilization, expansion capex, working capital, leverage, bid price",
    "afr": "occupancy, same-property NOI, AFFO/share, dividend coverage, acquisition cap rate, cost of debt, shares issued, leverage, asset-sale value",
    "afrisam_note": "exact note class, quoted price/par, collateral, senior debt, EBITDA, leverage, swap cost, coupon, maturity, recovery and equity conversion",
    "affirm": "GMV, active consumers/merchants, take rate, RLTC margin, funding cost, delinquency/charge-offs, provision, concentration, liquidity",
    "amtrust": "gross/earned premium, loss and expense ratios, reserve development, ceded premium, statutory capital, tangible book/share, ROE, related-party balances",
}


SOURCES = {
    "afmi": [
        S("Affinity proxy supplement before vote", "https://www.sec.gov/Archives/edgar/data/1343305/000114420408034845/v116747_defa14a.htm", "SEC / Affinity Media", "2008-06-10", "Hotels at Home vote와 trust/redemption context 검증."),
        S("Affinity liquidation distribution", "https://www.sec.gov/Archives/edgar/data/1343305/000114420408057586/v128968_defa14a.htm", "SEC / Affinity Media", "2008-10-10", "IPO common당 $6 cash와 7주당 residual common 1주의 최종 구조 검증."),
    ],
    "alphamin": [
        S("Alphamin announcements archive", "https://alphaminresources.com/announcements/", "Alphamin Resources", "2021-2026", "FTR, debt, Mpama South, 생산·배당·security updates의 공식 보관처."),
        S("Alphamin record FY2025 production", "https://www.alphaminresources.com/", "Alphamin Resources", "2026-01-19", "FY2025 tin 18,576t, dividend C$0.11/share와 약 20kt run-rate 검증."),
    ],
    "agi": [
        S("Ag Growth 2005 annual report", "https://www.annualreports.com/HostedData/AnnualReportArchive/a/TSX_AFN_2005.pdf", "Ag Growth", "2006", "2005 Edwards acquisition, 매출·EBITDA·distribution 검증."),
        S("AGI corporate history / AIF", "https://www.aggrowth.com/globalassets/investors-section/shareholder-information-pdfs/agi-aif-2018.pdf", "Ag Growth International", "2018", "bolt-on acquisition과 장기 사업확장 검증."),
    ],
    "afop": [
        S("AFOP SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=1365487&owner=exclude", "SEC / Alliance Fiber Optic Products", "2006-2016", "reverse split, cash distribution, stock split와 재무공시 교차검증."),
        S("Corning acquisition announcement", "https://investor.corning.com/news-and-events/news-releases/news-releases-details/2016/Corning-to-Acquire-Alliance-Fiber-Optic-Products-Inc/default.aspx", "Corning", "2016-04-07", "$18.50 cash/share, 약 $305m acquisition 검증."),
    ],
    "aluflex": [
        S("Aluflexpack 2023 annual report", "https://www.aluflexpack.com/investors/reports-presentations/", "Aluflexpack", "2024", "2023 revenue €380.3m와 EBITDA 약 €51m 검증."),
        S("Constantia and Aluflexpack join forces", "https://www.cflex.com/", "Constantia Flexibles", "2025-03-04", "거래 completion·지배권 이전의 공식 발표 검증."),
        S("EU merger case archive", "https://competition-cases.ec.europa.eu/", "European Commission", "2025", "Constantia/Aluflexpack 기업결합 절차 교차검증."),
    ],
    "afr": [
        S("AFR merger proxy", "https://www.sec.gov/Archives/edgar/data/1193558/000089322007003606/w42308e8vk.htm", "SEC / American Financial Realty Trust", "2007-11-09", "$5.50 cash + 0.12096 GKK share merger consideration 검증."),
        S("Gramercy merger completion", "https://www.sec.gov/Archives/edgar/data/1287701/000110465908023029/a08-9959_18k.htm", "SEC / Gramercy", "2008-04-01", "거래 종결과 $0.2419 dividend-related adjustment 검증."),
    ],
    "afrisam_note": [
        S("PIC agreement with AfriSam noteholders", "https://cisp.cachefly.net/assets/articles/attachments/36845_public_investment_corporation.pdf", "Public Investment Corporation", "2011-12-09", "80% 초과 noteholder 지지와 R15bn 초과 debt reduction 검증."),
        S("AfriSam restructuring completion", "https://businessreport.co.za/companies/2013-04-02-afrisam-cuts-debt-by-r15bn/", "AfriSam statement / Business Report", "2013-04-02", "R15bn 초과 deleveraging 완료와 ownership change 검증.", "회사발표 재게시"),
    ],
    "affirm": [
        S("Affirm investor filings", "https://investors.affirm.com/financials/sec-filings/default.aspx", "Affirm Holdings", "2021-2026", "FY2021·FY2022 Peloton concentration, credit·funding·GMV 공시 검증."),
        S("Affirm FY2022 Form 10-K", "https://www.sec.gov/edgar/browse/?CIK=1820953&owner=exclude", "SEC / Affirm", "2022-08-29", "Peloton revenue share 약 8%와 FY2022 사업·credit 결과 검증."),
    ],
    "amtrust": [
        S("AmTrust restatement notice", "https://www.sec.gov/Archives/edgar/data/1365555/000136555517000051/amtrustform8-kedgarcopy.htm", "SEC / AmTrust", "2017-04-10", "2014·2015 및 2016 interim statements 재작성과 internal-control issue 검증."),
        S("AmTrust restatement results", "https://www.sec.gov/Archives/edgar/data/1365555/000136555517000061/ex991pressrelease.htm", "SEC / AmTrust", "2017-04-11", "2014·2015 net income 감소 폭과 오류 성격 검증."),
        S("Amended take-private agreement", "https://www.sec.gov/Archives/edgar/data/1365555/000119312518186313/d556924d8k.htm", "SEC / AmTrust", "2018-06-07", "$14.75/share cash amended merger price 검증."),
    ],
}


IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


def sc(business, valuation, catalyst, security, timing):
    return [("Business thesis", business), ("Valuation thesis", valuation), ("Catalyst thesis", catalyst), ("Security payoff", security), ("Timing / path", timing)]


def claim(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson):
    return C(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson)


LESSONS = {
    "afmi": ["SPAC common은 deal quality와 trust-floor payoff를 별도 claim으로 쪼갠다.", "trust cash는 vote·redemption·deadline·tax와 expenses 뒤 주당액으로 계산한다.", "실패한 merger라도 downside thesis는 성공할 수 있다.", "residual share 가치가 없으면 exact total return을 만들지 않는다."],
    "alphamin": ["광산 quality는 grade가 아니라 recovery·logistics·cash conversion까지 통과해야 한다.", "resource optionality는 resource·FID·construction·commissioning을 단계별로 판정한다.", "commodity cash windfall이 debt와 dividend로 실제 배분되는지 본다.", "jurisdiction risk는 단순 discount가 아니라 shutdown scenario로 둔다."],
    "agi": ["income trust의 높은 yield는 maintenance capex와 working capital 뒤 coverage로 검증한다.", "시장점유율은 pricing power보다 replacement demand·dealer economics와 함께 본다.", "M&A는 headline EBITDA가 아니라 unit당 distributable cash accretion으로 본다.", "배당을 포함한 ledger 없이 exact return을 주장하지 않는다."],
    "afop": ["net cash는 사업손실이 없을 때만 downside protection이다.", "reverse split·stock split·cash distribution을 날짜별로 모두 보정한다.", "small-cap strategic value는 실제 bid 이전에는 bull case로만 둔다.", "takeout multiple과 standalone operating success를 구분한다."],
    "aluflex": ["operating target 적중과 주식 payoff 적중을 분리한다.", "capacity expansion은 utilization·working capital·leverage를 함께 본다.", "원재료 pass-through의 시차가 EBITDA와 cash를 다르게 움직인다.", "cash offer는 entry price와 interim dividends가 있어야 total return이 된다."],
    "afr": ["REIT acquisition growth는 asset가 아니라 AFFO/share와 dividend coverage로 판정한다.", "occupancy 개선이 leverage·dilution을 상쇄하는지 본다.", "NAV discount는 forced sale과 refinancing 조건에서 다시 stress한다.", "stock consideration은 closing value와 후속 가격을 분리한다."],
    "afrisam_note": ["distressed credit은 회사의 질보다 collateral·priority·recovery를 먼저 본다.", "par-for-new-paper는 현금 회수가 아니다.", "swap 제거와 coupon reduction을 restructuring economics에 포함한다.", "holder별 cash·PIK·equity ledger 없이는 exact IRR을 만들지 않는다."],
    "affirm": ["고성장 lender는 sales multiple보다 funding·credit·unit economics를 본다.", "merchant concentration은 revenue와 subsidy economics를 같이 추적한다.", "macro tailwind를 underwriting edge로 오인하지 않는다.", "short target hit 뒤에는 생존·rebound risk를 재평가한다."],
    "amtrust": ["보험 short는 맞는 governance 우려보다 catalyst clock과 borrow path가 중요하다.", "관련자 reinsurance는 economics·collateral·counterparty credit을 분해한다.", "높은 ROE를 reserve·leverage·acquisition contribution으로 분해한다.", "후행 restatement는 큰 adverse excursion을 소급해 없애지 않는다."],
}

CHECKLIST = {key: values for key, values in {
    "afmi": ["trust cash/share", "vote·redemption", "deal exchange ratio", "sponsor dilution", "deadline", "liquidation ledger"],
    "alphamin": ["grade·recovery", "contained tin", "cash cost", "net debt", "capex", "Mpama South ramp", "dividend", "security status"],
    "agi": ["organic volume", "EBITDA margin", "maintenance capex", "working capital", "FCF/unit", "payout", "leverage", "M&A multiple"],
    "afop": ["revenue mix", "gross margin", "net cash", "R&D·capex", "customer concentration", "split ledger", "capital return"],
    "aluflex": ["volume", "pass-through", "EBITDA margin", "utilization", "capex", "working capital", "leverage", "offer terms"],
    "afr": ["occupancy", "same-property NOI", "AFFO/share", "dividend coverage", "debt maturity", "shares issued", "asset sales"],
    "afrisam_note": ["CUSIP/note class", "collateral", "senior claims", "coupon/swap", "maturity", "restructuring vote", "cash/equity recovery"],
    "affirm": ["GMV", "RLTC margin", "funding cost", "delinquency", "charge-offs", "concentration", "liquidity", "valuation"],
    "amtrust": ["reserve triangles", "combined ratio", "ceded recoverable", "related parties", "statutory capital", "TBV/share", "catalyst clock"],
}.items()}


add(
    id="f0eefbcc-1ae2-4b53-aa04-94430fbdbba6", date="2008-06-04", author="scrooge833", ticker="AFMI.OB", company="Affinity Media Inc.", filename="analysis/ideas/2008/2008-06-04_AFMI_OB_long.md", source="https://www.valueinvestorsclub.com/idea/Affinity_Media/8205028420", group="afmi", direction="Long", raw_direction="Long", security="SPAC IPO common equity / Long", entry="약 $5.85", horizon="2008 deal vote 또는 liquidation", raw_horizon="Hotels at Home merger 성공 시 effective basis 약 $3.84, 2009 target $7.60; 실패 시 trust $6+",
    title="trust-floor SPAC event Long", verdict="downside thesis 성공 — deal 실패에도 $6 cash + residual", score=7.5, process=8.5,
    conclusion="Hotels at Home business-combination thesis는 vote 실패로 무너졌다. 그러나 $5.85 common은 liquidation에서 IPO share당 $6 cash와 취소된 7주당 residual common 1주를 받았다. 따라서 operating deal claim은 실패했지만 핵심 trust-floor 비대칭은 작동했다. residual의 최종 현금가치가 완전하지 않아 exact total return·IRR은 계산하지 않는다.",
    t0="$5.85에 SPAC common을 사면 merger 성사 시 Hotels at Home equity를 약 $3.84 effective basis로 얻고 2009년 $7.60을 기대하며, 부결 시 trust cash $6 이상으로 원금이 방어된다는 event-driven thesis였다.", reverse="시장은 transaction dilution, Hotels at Home valuation·execution, 낮은 vote certainty와 청산비용 때문에 trust보다 낮은 가격을 붙였다. 핵심은 deal 성공확률보다 실제 redemption 문서가 $5.85 downside를 지키는지였다.",
    valuation="binary tree로 계산한다. 성공가치는 merger exchange 뒤 fully diluted shares로, 실패가치는 trust 현금·비용·tax·residual rights로 계산한다. $7.60 target와 $6 floor를 한 기대값으로 섞지 않는다.",
    actual="deal vote가 실패했고 proposed merger는 닫히지 않았다. 2008-10 공시는 IPO common each를 $6 cash와 residual common 1/7주로 전환했다. operating upside는 사라졌지만 $5.85 entry 대비 cash만으로도 nominal downside를 막았다.",
    price="$6 cash / $5.85 = 1.0256x, 즉 cash component만 약 +2.6%다. residual 1/7 share의 후속 현금화와 정확 settlement·tax가 빠졌으므로 이는 total return이나 IRR이 아니다.",
    drivers="수익의 원천은 Hotels at Home execution이 아니라 trust 계약이었다. vote 실패가 business thesis를 제거했지만 liquidation waterfall이 common을 보호했다.", counterfactual="trust cash가 $5.50으로 줄거나 liquidation이 18개월 지연되어도 $5.85 entry의 expected value가 충분했는가?", error="merger 성공 뒤 $7.60을 자세히 모델링한 반면 vote mechanics, trust leakage와 residual share liquidation의 기간을 상대적으로 덜 정량화했다.", warning="2008-06 deal vote 실패가 operating thesis의 즉시 break였지만 동시에 trust-floor thesis를 실제 payoff 단계로 전환한 신호였다.", first_signal_date="2008-06-13", lessons=LESSONS["afmi"], checklist=CHECKLIST["afmi"], scorecard=sc("deal thesis 실패", "trust discount 성공", "vote 실패·liquidation", "SPAC common 적절", "짧은 event 성공"),
    scenarios=[("Bear", "deal 실패·trust leakage", "$5.5 이하", "미실현"), ("Base", "deal 실패·$6 cash", "원금+소폭", "실현"), ("Bull", "deal close·2009 execution", "$7.60", "미실현")],
    metrics=[("Entry", "$5.85", "$6 floor / $7.60 bull", "$6 cash+1/7 residual", "floor 성공"), ("Deal vote", "승인 가능", "통과", "실패", "operating claim 실패"), ("Effective merger basis", "$3.84", "Hotels at Home ownership", "거래 미종결", "미실현"), ("Cash floor", "$6+", ">entry", "$6", "+$0.15/+2.6%"), ("Residual", "추가 upside", "양의 가치", "1/7 share", "가치 ledger 불완전")],
    timeline=[("2008-06-04", "VIC Long", "$5.85 event entry"), ("2008-06-10", "proxy supplement", "vote mechanics"), ("2008-06-13", "deal vote 실패", "operating thesis break"), ("2008-07", "청산 준비", "trust payoff 중심"), ("2008-09", "deadline 경과", "business combination 종료"), ("2008-10-10", "liquidation terms 공시", "$6+residual"), ("2008-10", "IPO shares 취소", "cash conversion"), ("2026-09-18", "research cutoff", "residual exact value 미복원")],
    claims=[
        claim("Hotels at Home merger", "실패", "vote 뒤 Hotels at Home과 결합한다.", "승인·closing이 operating equity를 만든다.", "signed transaction과 예정 vote.", "주주 승인과 financing 충족.", "vote 부결이면 즉시 실패.", "vote가 실패했다.", "closing 0%.", "deal probability를 과신.", "event claim과 trust claim을 분리한다."),
        claim("effective basis $3.84", "미실현", "merger equity를 $3.84 basis로 취득한다.", "trust cash와 exchange ratio가 implied basis를 낮춘다.", "원문 pro forma 계산.", "거래가 동일 조건으로 닫힌다.", "deal break면 계산 무효.", "거래가 닫히지 않았다.", "$3.84 basis 적용 불가.", "conditional valuation을 확정값처럼 봄.", "closing 조건부 수치는 확률가중한다."),
        claim("2009 target $7.60", "실패", "운영개선 뒤 $7.60.", "merger EBITDA와 multiple이 equity를 높인다.", "원문 operating case.", "closing 뒤 plan 달성.", "deal failure 또는 target miss.", "underlying equity를 받지 못했다.", "$7.60 미실현.", "business와 security event 혼합.", "target는 security tree 각 branch에 둔다."),
        claim("trust floor $6+", "성공", "부결 시 $6 이상을 회수한다.", "IPO cash가 trust에 보관된다.", "trust/redemption terms.", "비용·tax leakage가 제한적.", "$5.85 미만 지급이면 반증.", "$6 cash가 지급됐다.", "$0.15/+2.6% cash spread.", "settlement time 비용 미포함.", "floor는 날짜·비용 포함 IRR로 본다."),
        claim("residual upside", "부분 성공", "청산 뒤 residual shell도 가치가 있다.", "취소 주식 7주당 residual 1주.", "liquidation filing.", "residual assets·listing이 가치 보존.", "residual이 무가치면 upside 0.", "1/7주 교부는 확인, 최종 가치 미복원.", "수량 확인·가치 미확정.", "nominal security를 현금으로 간주.", "residual은 실현 ledger가 있을 때만 수익에 넣는다."),
        claim("asymmetric downside", "성공", "$5.85에서 손실은 제한되고 upside가 크다.", "trust branch가 downside를 지킨다.", "entry below trust.", "fraud·비용·지연이 없음.", "cash recovery <entry면 실패.", "cash만 $6.", "cash spread +2.6%.", "opportunity cost를 작게 봄.", "event time과 annualized floor yield를 같이 본다."),
    ],
)


add(
    id="b3a18d0f-17bf-4636-b562-3896bb122e2a", date="2021-01-10", author="Veritas500", ticker="AFMJF", company="Alphamin Resources Corp.", filename="analysis/ideas/2021/2021-01-10_AFMJF_long.md", source="", group="alphamin", direction="Long", raw_direction="Long", security="Alphamin common equity / Long", entry="원문 post-tax NPV8 대비 약 48% discount", horizon="2021 deleveraging·FTR; 2022~2025 Mpama South", raw_horizon="debt-free, FTR recovery, Mpama South resource/development, 20%+ forward dividend yield",
    title="high-grade tin de-risking·expansion Long", verdict="매우 강한 성공 — 생산·Mpama South·배당 실현", score=9.4, process=8.8,
    conclusion="운영 bottleneck 제거, debt reduction, Mpama South와 dividend라는 네 축이 순서대로 현실화됐다. 2025 생산 18,576t와 C$0.11/share 배당, 2026 약 20kt guidance는 thesis를 강하게 지지한다. 다만 2025 보안상 운영중단은 DRC risk가 단순 valuation discount가 아니라 실제 tail임을 확인했다.",
    t0="Mpama North의 탁월한 grade에도 과거 project mistakes·metallurgy·DRC risk 때문에 estimated post-tax NPV8 대비 약 48% 할인됐다. FTR plant, net debt 제거, Mpama South discovery와 dividend가 discount를 좁힐 촉매였다.", reverse="시장은 remote logistics, recovery miss, tin-price cyclicality, DRC security·tax risk와 single-asset concentration을 가격에 반영했다. 높은 grade만으로는 지속가능한 free cash가 보장되지 않는다.",
    valuation="NPV discount는 tin price·recovery·capex·tax sensitivity를 모두 포함해야 한다. 원문의 48% discount와 20%+ forward yield는 spot tin과 rapid deleveraging에 민감하므로 base·stress price에서 배당가능현금을 별도 계산한다.",
    actual="FTR improvements와 strong tin price가 debt를 낮췄고 회사는 dividend를 시작했다. Mpama South는 resource·development·construction을 거쳐 2024 commissioning됐으며 FY2025 contained tin production은 18,576t, dividend는 C$0.11/share였다. 2026 run-rate guidance는 약 20kt다.",
    price="공개 source catalog에 신뢰할 수 있는 entry/exit·FX·배당 ledger가 없어 exact stock return을 만들지 않는다. 운영량·배당과 project milestones로 thesis를 판정한다.",
    drivers="고품위 ore에 FTR recovery, 두 번째 mine과 높은 tin price가 결합해 unit cash generation을 늘렸고, 그 현금이 debt reduction·dividend·expansion으로 재투자됐다.", counterfactual="tin price 25% 하락, recovery 5ppt 저하와 6개월 security shutdown에서도 debt·Mpama South capex·배당이 공존할 수 있었는가?", error="spot tin 기반 forward dividend yield를 장기 normal로 보기 쉽고, security interruption과 single-road logistics의 correlated downside를 더 크게 stress했어야 한다.", warning="2025 regional security에 따른 일시 중단은 thesis를 깨지는 않았지만 jurisdiction risk를 observable cash-flow interruption으로 바꾼 최초 신호였다.", first_signal_date="2025-03", lessons=LESSONS["alphamin"], checklist=CHECKLIST["alphamin"], scorecard=sc("매우 강한 성공", "NPV discount 축소 근거", "모든 주요 촉매 실현", "common 적절", "단계적 성공"),
    scenarios=[("Bear", "tin -25%·shutdown", "capex/dividend 축소", "일시 security shock"), ("Base", "FTR·debt-free·South ramp", "17~18kt+dividend", "실현"), ("Bull", "20kt·강한 tin", "큰 distributions", "2026 guidance")],
    metrics=[("NPV discount", "48%", "discount 축소", "운영 de-risking", "성공 방향"), ("Net debt", "빠른 상환 기대", "2021 debt-free 방향", "강한 cash로 축소", "성공"), ("Mpama South", "exploration option", "resource→production", "2024 commissioned", "강한 성공"), ("FY2025 tin", "North base", "확장", "18,576t", "강한 성공"), ("FY2025 dividend", "20%+ forward yield 기대", "현금환원", "C$0.11/share", "성공·yield 미복원")],
    timeline=[("2021-01-10", "VIC Long", "48% NPV discount"), ("2021", "FTR/debt reduction", "de-risking"), ("2022", "배당 개시", "cash conversion"), ("2022", "Mpama South resource·decision", "option crystallization"), ("2023", "South construction", "capex execution"), ("2024", "Mpama South commissioning", "second mine"), ("2025", "security interruption·resume", "jurisdiction tail"), ("2026-01-19", "FY2025 18,576t·C$0.11", "thesis 확정")],
    claims=[
        claim("FTR recovery", "성공", "Fine Tin Recovery plant가 recoveries를 높인다.", "tailings/fines 회수가 payable tin을 늘린다.", "commissioning plan과 high-grade ore.", "plant ramp와 metallurgy가 맞는다.", "회수율·생산이 개선되지 않으면 실패.", "운영개선과 production 증가에 기여했다.", "방향 성공; 단일 plant attribution 제한.", "tin price 효과와 혼용.", "recovery와 price bridge를 분리한다."),
        claim("2021 deleveraging", "성공", "강한 cash로 net debt를 제거한다.", "EBITDA-cash tax-capex가 debt를 상환한다.", "tin price와 cash-cost spread.", "생산·price가 유지된다.", "net debt가 줄지 않으면 실패.", "debt가 빠르게 축소되고 distributions로 전환됐다.", "방향·sequence 적중.", "spot price 지속 가정.", "debt paydown을 realized cash로 검증한다."),
        claim("Mpama South", "강한 성공", "South가 resource·production을 확대한다.", "두 번째 orebody가 mill feed와 mine life를 늘린다.", "drilling program.", "grade·capex·permit가 경제적이다.", "resource가 mine으로 전환되지 않으면 실패.", "2024 commissioning, 2025 ramp.", "option→operating asset.", "exploration을 너무 일찍 NPV에 포함 위험.", "단계별 probability를 둔다."),
        claim("production step-up", "강한 성공", "expansion 뒤 contained tin이 크게 늘어난다.", "North+South feed가 throughput을 높인다.", "plant·mine plan.", "recovery·logistics 안정.", "17kt 미달 지속이면 실패.", "FY2025 18,576t.", "17~18kt 수준 상회.", "grade variability 과소평가.", "ore source별 grade·recovery를 추적한다."),
        claim("20%+ dividend yield", "부분 성공", "debt-free 뒤 매우 높은 forward yield.", "surplus cash를 배당한다.", "spot-price FCF.", "tin price와 payout 유지.", "배당 미개시 또는 capex 흡수면 실패.", "배당 개시·2025 C$0.11.", "배당 실현; entry-based yield 미복원.", "forward yield를 확정처럼 제시.", "price·FX·dates 없이는 yield/IRR을 제한한다."),
        claim("DRC risk manageable", "부분 성공", "discount가 과도하고 operations는 유지된다.", "security·government relations가 cash continuity를 지킨다.", "operating history.", "transport corridor가 열려 있다.", "장기 shutdown이면 반증.", "2025 일시중단 후 재개.", "tail 현실화·terminal failure 아님.", "country discount를 추상적으로 처리.", "shutdown duration별 liquidity를 모델링한다."),
    ],
)


add(
    id="31a1b41b-df44-440e-b8b0-ba7c55537bee", date="2004-10-12", author="dylex849", ticker="AFN UN", company="Ag Growth Income Fund", filename="analysis/ideas/2004/2004-10-12_AFN_UN_long.md", source="https://www.valueinvestorsclub.com/idea/Ag_Growth/7929689393", group="agi", direction="Long", raw_direction="Short", security="income trust units / Long", entry="11.5% indicated cash distribution yield", horizon="2005~2007 operating growth·distributions", raw_horizon="double-digit FCF yield, 30%+ EBITDA margin, replacement demand와 bolt-on M&A",
    title="high-yield niche industrial Long", verdict="강한 성공 — margin·distribution·bolt-ons 실현", score=9.0, process=8.4,
    conclusion="raw Short를 실제 Long으로 교정했다. 2005 H1 revenue C$40.4m·EBITDA C$12.0m, 2007 revenue C$130.7m·EBITDA C$32.4m과 distribution 증가는 high-margin niche thesis를 확인했다. Edwards와 후속 bolt-ons가 규모를 늘렸지만 완전한 distribution·unit-price ledger가 없어 exact total return은 계산하지 않는다.",
    t0="약 35% market share, 다음 경쟁자의 약 3배 규모와 replacement-driven grain equipment를 가진 사업을 11.5% distribution yield·double-digit FCF yield에 산다는 논지였다. EBITDA margin 30%+와 EBITDA-capex margin 29%+가 payout을 지지했다.", reverse="시장은 작은 Canadian income trust의 seasonality, steel·ag cycle, key-person risk와 acquisition deployment를 할인했다. 높은 yield가 maintenance capex·working capital 또는 temporary peak margin을 놓친 것일 수 있었다.",
    valuation="distribution yield만 보지 않고 EBITDA에서 cash tax·maintenance capex·working capital·interest를 빼 unit당 distributable cash를 계산한다. acquisitions는 debt·issued units 뒤 증분 cash/unit가 양수일 때만 가치창출이다.",
    actual="2005 Edwards acquisition이 product breadth를 넓혔다. 2005 H1 revenue C$40.4m, EBITDA C$12.0m으로 약 29.7% margin을 기록했고 distribution은 8% 이상 인상됐다. 2007 revenue C$130.7m, EBITDA C$32.4m이었으며 Hi Roller, Twister와 Union Iron 등 bolt-ons가 이어졌다.",
    price="distribution record dates, unit prices와 세금처리가 완전하지 않아 exact total return·IRR을 만들지 않는다. operating margin·distribution increase·scale growth로 thesis를 판정한다.",
    drivers="replacement demand, dominant dealer position과 높은 factory margin이 현금을 만들었고, management가 그 현금을 distributions와 adjacent acquisitions에 배분했다.", counterfactual="steel +20%, farm capex -20%, working-capital build와 acquisition debt를 반영해도 11.5% distribution이 1.2x 이상 covered였는가?", error="높은 역사적 margin과 CEO alignment를 구조적 moat의 충분조건으로 보고 cycle·integration·payout coverage sensitivity를 덜 계량화했다.", warning="thesis break는 없었다. 사전 핵심 경고는 EBITDA margin 25% 이하 또는 distribution coverage 1.0x 미만이었지만 초기 결과는 반대로 강했다.", first_signal_date="2005-08", lessons=LESSONS["agi"], checklist=CHECKLIST["agi"], scorecard=sc("강한 성공", "11.5% yield 지지", "results·M&A 실현", "trust units 적절", "2005~07 성공"),
    scenarios=[("Bear", "ag downcycle·margin 20%", "distribution cut", "미실현"), ("Base", "replacement·30% EBITDA", "yield+성장", "2005 실현"), ("Bull", "bolt-on accretion", "매출·EBITDA scale", "2007 실현")],
    metrics=[("Distribution yield", "11.5%", "covered·증가", "2005 8%+ 인상", "성공"), ("EBITDA margin", "30%+", "약 30%", "2005 H1 29.7%", "근접"), ("Market share", "35%", "지위 유지", "product expansion", "방향 성공"), ("2005 H1", "성장", "strong results", "revenue C$40.4m/EBITDA C$12m", "성공"), ("2007", "bolt-on 성장", "scale", "revenue C$130.7m/EBITDA C$32.4m", "강한 성공")],
    timeline=[("2004-10-12", "VIC Long", "raw Short 교정"), ("2005", "Edwards acquisition", "product breadth"), ("2005-H1", "C$40.4m revenue", "growth"), ("2005-H1", "C$12.0m EBITDA", "29.7% margin"), ("2005", "distribution 8%+ 인상", "coverage 확인"), ("2006", "Hi Roller·Twister", "bolt-ons"), ("2007", "Union Iron", "platform 확대"), ("2007-FY", "C$130.7m/C$32.4m", "scale success")],
    claims=[
        claim("raw Short", "metadata 실패", "source SQL은 Short다.", "방향 오류는 yield payoff를 반전시킨다.", "원문은 upside·distribution을 샀다.", "본문이 실제 payoff를 확정한다.", "하락으로 수익이면 Short다.", "실제 income-trust Long.", "완전 반대.", "raw flag 의존.", "원문 cash-flow 방향으로 교정한다."),
        claim("30%+ EBITDA margin", "성공", "niche 지위가 30%+ margin을 지킨다.", "scale·dealer network가 price/cost spread를 보호한다.", "T0 margin history.", "cycle·steel pass-through 관리.", "25% 이하 지속이면 실패.", "2005 H1 29.7%, 2007 약 24.8%.", "초기 적중·scale 뒤 완화.", "peak margin 영구화 위험.", "organic margin과 acquired mix를 분리한다."),
        claim("11.5% distribution", "성공", "double-digit cash yield가 covered된다.", "FCF가 unit cash distribution을 지불한다.", "EBITDA-capex spread.", "working capital·tax·interest가 작다.", "cut 또는 coverage<1x면 실패.", "2005 distribution 8%+ 인상.", "cut 대신 인상.", "complete coverage bridge 부재.", "DCF보다 cash coverage 표를 먼저 만든다."),
        claim("35% share/moat", "대체로 성공", "다음 경쟁자 3배 규모가 방어력이다.", "distribution·installed base가 replacement sales를 만든다.", "T0 share estimates.", "customers가 switching하지 않는다.", "share·margin 급락이면 실패.", "매출·제품군이 확대됐다.", "share exact follow-up 제한.", "규모를 moat로 바로 등치.", "dealer retention·price realization을 추적한다."),
        claim("bolt-on M&A", "강한 성공", "adjacent acquisitions가 accretive growth를 만든다.", "shared channel·manufacturing이 FCF/unit를 늘린다.", "Edwards pipeline.", "multiple·integration·debt 통제.", "unit당 cash 희석이면 실패.", "Edwards, Hi Roller, Twister, Union Iron 실행.", "다수 거래 실현.", "deal quantity를 accretion으로 대체.", "deal별 pro forma FCF/unit를 기록한다."),
        claim("management alignment", "부분 검증", "CEO 순자산 90%가 units에 묶여 있다.", "ownership이 payout·capital allocation을 정렬한다.", "원문 ownership.", "control benefit·risk-taking이 과하지 않다.", "과대 M&A·희석이면 반증.", "distribution과 bolt-ons가 가치를 늘렸다.", "결과 지지·인과 단정 불가.", "ownership을 governance quality로 동일시.", "related-party·compensation을 별도 본다."),
    ],
)


add(
    id="ccaba7d9-3979-46a6-84ef-7cac99f42499", date="2010-05-26", author="anton613", ticker="AFOP", company="Alliance Fiber Optic Products Inc.", filename="analysis/ideas/2010/2010-05-26_AFOP_long.md", source="", group="afop", direction="Long", raw_direction="Long", security="AFOP common equity / Long", entry="$1.35 pre 1-for-5 reverse split", horizon="2~5년 operating normalization·capital return", raw_horizon="cash $0.97/share, EV 약 $16m, operating earnings 약 $4m; telecom/datacenter growth·strategic value",
    title="net-cash optical-component deep-value Long", verdict="매우 강한 성공 — split-adjusted 5.48x takeout", score=9.5, process=9.0,
    conclusion="2010 entry $1.35는 1-for-5 reverse split 뒤 $6.75, 2013 2-for-1 split 뒤 2016 기준 $3.375다. Corning의 $18.50 cash acquisition은 5.48x price multiple이며 2012 cash distribution과 ordinary dividends는 별도다. net cash·profitability·strategic scarcity thesis가 모두 실현됐지만 complete ledger가 없어 exact IRR은 만들지 않는다.",
    t0="주당 cash $0.97, EV 약 $16m와 operating earnings 약 $4m인 profitable optical component vendor를 거의 cash에 샀다. telecom core upgrade, datacenter demand, dividends·buyback과 strategic buyer가 upside였다.", reverse="시장은 small scale, customer concentration, telecom capex cyclicality, Asian manufacturing·price erosion과 현금이 장기간 idle할 위험을 할인했다.",
    valuation="split을 두 단계 적용한다: $1.35×5÷2=$3.375 2016 basis. $18.50/$3.375=5.48x. cash distribution·dividends는 separate ledger이며 acquisition price multiple에 중복 가산하지 않는다.",
    actual="2010-08 1-for-5 reverse split, 2012 $1.25/share cash distribution, 2013 2-for-1 split이 있었다. AFOP은 성장·현금환원을 이어갔고 Corning은 2016-04 $18.50/share cash, 약 $305m에 인수를 발표·완료했다.",
    price="2016-basis entry $3.375 대비 $18.50는 5.48x, 단순 price gain 약 +448.1%다. 2012 distribution의 당시 share basis와 ordinary dividends·tax·settlement ledger가 완전하지 않아 exact total return·IRR은 아니다.",
    drivers="cash-rich downside, low EV/operating earnings와 optical demand가 rerating을 만들었고 Corning이 product·customer fit에 strategic premium을 지급했다.", counterfactual="revenue flat, gross margin -500bp, cash burn 3년과 strategic bid 없음에서도 $1.35 pre-split entry가 보호됐는가?", error="net cash를 hard floor로 보기 쉽고 고객집중·technology substitution과 cash governance를 충분히 haircut하지 않았다. 결과적으로 맞았지만 takeout은 base가 아니라 bull case였다.", warning="명확한 thesis break는 없었다. 2010 reverse split은 경제손실이 아니라 단위변경이므로 경고가 아니며, 이후 영업·현금환원은 확인 신호였다.", first_signal_date="2012-08", lessons=LESSONS["afop"], checklist=CHECKLIST["afop"], scorecard=sc("강한 성공", "deep value 실현", "capital return·takeout", "common 적절", "장기 성공"),
    scenarios=[("Bear", "cash burn·telecom slump", "$1 이하 pre-split", "미실현"), ("Base", "profit 유지·cash return", "2~3x", "실현"), ("Bull", "strategic buyer", "$18.50 2016 basis", "실현")],
    metrics=[("Entry basis", "$1.35 pre-RS", "$6.75 post-RS", "$3.375 after later split", "단위 교정"), ("Cash/share", "$0.97 pre-RS", "downside support", "$1.25 distribution later", "성공 방향"), ("EV/op earnings", "$16m/$4m", "약 4x", "strategic premium", "성공"), ("Takeout", "optional", "strategic value", "$18.50 cash", "강한 성공"), ("Price multiple", "$3.375 basis", "upside", "5.48x", "배당 제외")],
    timeline=[("2010-05-26", "VIC Long", "$1.35 pre-split"), ("2010-08", "1-for-5 reverse split", "$6.75 equivalent"), ("2012", "$1.25 cash distribution", "capital return"), ("2013-08", "2-for-1 split", "$3.375 basis"), ("2014", "optical growth", "operating confirmation"), ("2015", "strategic scarcity", "rerating"), ("2016-04-07", "Corning $18.50 bid", "terminal value"), ("2016", "acquisition completion", "cash payoff")],
    claims=[
        claim("net cash floor", "성공", "$0.97 cash/share가 $1.35 downside를 지지한다.", "cash less liabilities lowers EV.", "balance-sheet cash.", "cash가 burn·bad M&A로 사라지지 않는다.", "cash/share 급감이면 실패.", "cash distribution과 deal value로 환원됐다.", "capital return 확인.", "cash를 unrestricted로 가정.", "net cash quality와 burn을 stress한다."),
        claim("약 4x operating earnings", "강한 성공", "$16m EV/$4m earnings는 싸다.", "profit 유지 시 FCF yield가 rerating을 만든다.", "T0 estimate.", "earnings가 cash로 전환된다.", "영업적자면 실패.", "성장·takeout까지 이어졌다.", "multiple rerating 크게 실현.", "normalized earnings 범위 부족.", "cycle-low/normal/high를 둔다."),
        claim("telecom/datacenter demand", "성공", "network upgrade가 volume을 늘린다.", "40G/100G·datacenter optics 수요.", "industry upgrade path.", "qualification·ASP가 유지된다.", "revenue·margin 축소면 실패.", "2010s optical growth가 strategic value를 높였다.", "방향 적중.", "industry TAM을 company share로 직결.", "customer/design wins로 검증한다."),
        claim("capital return", "성공", "dividend·buyback으로 excess cash를 돌려준다.", "idle cash discount를 제거한다.", "cash-rich balance sheet.", "board가 현금을 보유하지 않는다.", "무환원·bad M&A면 실패.", "2012 $1.25 distribution.", "명시적 현금환원.", "distribution basis 혼동 위험.", "ex-date share basis를 고정한다."),
        claim("strategic takeout", "강한 성공", "larger optical vendor가 인수한다.", "product·customers·IP가 buyer에게 더 가치 있다.", "small scale와 innovative products.", "buyer가 premium 지급.", "독립 유지면 catalyst 지연.", "Corning $18.50 cash.", "약 $305m transaction.", "buyer optionality를 base에 포함 위험.", "standalone value로 먼저 underwriting한다."),
        claim("split-adjusted payoff", "검증 성공", "entry와 exit를 같은 share basis로 비교한다.", "1:5 reverse·2:1 forward split은 주당 단위를 바꾼다.", "corporate actions.", "동일 share class.", "factor 누락이면 return 무효.", "$1.35×5÷2=$3.375; 5.48x.", "raw $18.50/$1.35 과대 오류 방지.", "분할·분배 혼용.", "corporate-action ledger를 먼저 만든다."),
    ],
)


add(
    id="ee7d3bda-2526-406c-a821-2381fc5664d7", date="2012-08-07", author="cobia72", ticker="AFOP", company="Alliance Fiber Optic Products Inc.", filename="analysis/ideas/2012/2012-08-07_AFOP_long.md", source="https://www.valueinvestorsclub.com/idea/ALLIANCE_FIBER_OPTIC_PRODUCT/1868352466", group="afop", direction="Long", raw_direction="Long", security="AFOP common equity / Long", entry="$9.29 pre 2013 2-for-1 split", horizon="2012~2016 telecom upgrade·strategic outcome", raw_horizon="net cash $5.70, tangible book $7.20, TEV/EBIT 약 5x; 100G cycle와 acquisition",
    title="net-cash profitable optical Long", verdict="매우 강한 성공 — 3.98x split-adjusted takeout + distributions", score=9.3, process=8.8,
    conclusion="2013 2-for-1 split을 적용하면 $9.29 entry는 2016 기준 $4.645다. Corning $18.50 cash offer는 3.98x price multiple이다. 2012 $1.25 cash distribution과 dividends는 추가 payoff지만 exact ex-date share basis·tax ledger가 없어 IRR을 만들지 않는다.",
    t0="$9.29 중 net cash $5.70, tangible book $7.20이 받치고 TEV/EBIT 약 5x인 profitable optical vendor였다. 100G core upgrade, datacenter growth와 acquisition이 catalyst였다.", reverse="시장은 telecom carrier capex 지연, lumpy orders, ASP erosion·customer concentration과 small vendor discount를 반영했다. net cash도 operating losses나 poor allocation으로 소진될 수 있었다.",
    valuation="$9.29÷2=$4.645로 2016 share basis를 맞춘다. $18.50/$4.645=3.98x다. $1.25 distribution은 당시 basis로 별도 cash ledger에 기록하고 price basis에서 임의 차감하지 않는다.",
    actual="2012 $1.25/share cash distribution, 2013 2-for-1 split과 영업확대가 이어졌다. 2016 Corning이 $18.50/share cash, 약 $305m로 AFOP을 인수했다.",
    price="$18.50/$4.645=3.9828x, 단순 price gain 약 +298.3%다. cash distribution·ordinary dividends·settlement dates와 tax가 빠져 exact total return·IRR은 아니다.",
    drivers="net cash와 tangible book가 downside를 낮췄고 optical upgrade와 profitable scale이 standalone value를 높였다. 최종적으로 strategic buyer가 control premium을 지급했다.", counterfactual="100G upgrade가 3년 늦고 EBIT가 절반이며 takeout이 없어도 ex-cash valuation이 충분히 싸고 cash burn을 견딜 수 있었는가?", error="industry upgrade timing과 strategic interest의 확률을 높게 잡았고 net cash를 고객집중·technology risk보다 단단한 floor로 볼 위험이 있었다.", warning="명확한 break는 없었다. 2012 distribution과 2013 split 후 operating momentum은 확인 신호였으며 terminal validation은 2016 bid였다.", first_signal_date="2013-08", lessons=LESSONS["afop"], checklist=CHECKLIST["afop"], scorecard=sc("강한 성공", "net cash·5x EBIT 지지", "100G·takeout 성공", "common 적절", "4년 성공"),
    scenarios=[("Bear", "upgrade delay·cash burn", "$5~7 pre-split", "미실현"), ("Base", "profit·100G ramp", "rerating+cash return", "실현"), ("Bull", "strategic takeout", "$18.50 2016 basis", "실현")],
    metrics=[("Entry", "$9.29 pre-split", "$4.645 adjusted", "$18.50 cash", "3.98x"), ("Net cash", "$5.70/share", "downside", "distribution+deal", "성공"), ("Tangible book", "$7.20/share", "asset support", "takeout above", "성공"), ("TEV/EBIT", "약 5x", "rerating", "strategic premium", "강한 성공"), ("Cash distribution", "$1.25/share", "capital return", "2012 지급", "성공·ledger 제한")],
    timeline=[("2012-08-07", "VIC Long", "$9.29"), ("2012", "$1.25 cash distribution", "capital return"), ("2013-08", "2-for-1 split", "$4.645 basis"), ("2013", "100G cycle", "demand catalyst"), ("2014", "datacenter growth", "diversification"), ("2015", "profit·cash accumulation", "standalone value"), ("2016-04-07", "Corning $18.50 bid", "3.98x price multiple"), ("2016", "deal completion", "cash terminal")],
    claims=[
        claim("net cash $5.70", "성공", "net cash가 entry 대부분을 지지한다.", "enterprise value가 낮아 operating downside를 줄인다.", "T0 balance sheet.", "cash가 unrestricted·보존된다.", "cash burn·dilution이면 실패.", "cash return과 takeout으로 가치화.", "floor thesis 지지.", "cash governance haircut 부족.", "cash minus burn·obligations를 쓴다."),
        claim("tangible book $7.20", "성공", "entry가 tangible book에 가깝다.", "working assets·cash가 residual을 지지한다.", "T0 book.", "inventory·receivables 회수 가능.", "write-down이면 실패.", "$18.50 takeout.", "terminal value가 book 상회.", "book와 liquidation value 혼동.", "asset별 recovery를 적용한다."),
        claim("TEV/EBIT 5x", "강한 성공", "profit stream이 5x로 저평가됐다.", "EBIT 유지·성장이 multiple expansion을 만든다.", "T0 EBIT estimate.", "margin·customers 유지.", "EBIT 급락이면 실패.", "standalone 성장 뒤 strategic premium.", "큰 rerating.", "peak EBIT 가능성.", "normalized EBIT band를 쓴다."),
        claim("100G upgrade", "성공", "carrier upgrade가 demand를 촉진한다.", "higher-speed network가 passive components를 요구한다.", "industry capex timing.", "AFOP content·qualification 확보.", "upgrade 지연·share loss면 실패.", "2013~15 growth에 기여.", "방향 적중; attribution 제한.", "industry cycle timing 과신.", "order·design-win data로 추적한다."),
        claim("cash return", "성공", "excess cash가 shareholder에게 돌아온다.", "distribution이 cash discount를 줄인다.", "balance-sheet excess.", "board 승인.", "현금이 계속 idle면 실패.", "2012 $1.25 distribution.", "명시적 지급.", "per-share basis 혼동.", "ex-date split basis로 ledger화한다."),
        claim("strategic acquisition", "강한 성공", "larger vendor가 premium을 지불한다.", "technology·customers의 synergy.", "small profitable target.", "buyer interest·antitrust 통과.", "bid 없음이면 지연.", "Corning $18.50 cash.", "3.98x adjusted entry.", "takeout을 core valuation에 과도 반영 위험.", "standalone과 control value를 분리한다."),
    ],
)


add(
    id="c32c272b-06de-4d82-b435-a646a7f66879", date="2022-05-29", author="MrTwister", ticker="AFP SW", company="Aluflexpack AG", filename="analysis/ideas/2022/2022-05-29_AFP_SW_long.md", source="https://www.valueinvestorsclub.com/idea/Aluflexpack/3093562527", group="aluflex", direction="Long", raw_direction="Long", security="Aluflexpack registered shares / Long", entry="2022 depressed Swiss-listed valuation; exact entry ledger unavailable", horizon="2022~2025 capacity ramp·margin normalization", raw_horizon="2025 revenue €425m, EBITDA margin 14%, EBITDA 약 €59.5m",
    title="capacity-expansion flexible-packaging Long", verdict="운영 성공 / security outcome 혼합 — 2025 CHF16 takeout", score=6.8, process=7.8,
    conclusion="2023 revenue €380.3m와 EBITDA 약 €51m은 2025 목표 €425m·€59.5m에 상당히 접근해 operating thesis를 지지했다. 그러나 Constantia의 최종 CHF16/share acquisition·delisting이 각 투자자의 충분한 return이었는지는 T0 entry와 배당 ledger 없이는 단정할 수 없다. 사업 예측 성공과 security payoff를 분리한다.",
    t0="aluminum·energy inflation과 expansion capex가 earnings를 눌러 valuation이 낮았지만, defensive end markets, pass-through와 new capacity ramp로 2025 revenue €425m·14% EBITDA margin·약 €59.5m EBITDA를 달성한다는 논지였다.", reverse="시장은 raw-material pass-through lag, capex overrun, utilization ramp, working-capital funding과 controlling-shareholder/low-liquidity discount를 반영했다. 성장 capex가 revenue는 늘려도 FCF/share를 만들지 못할 수 있었다.",
    valuation="2025 €59.5m EBITDA target에는 net debt·minority·maintenance capex를 연결해야 한다. terminal CHF16 cash offer는 operating forecast 검증과 별개이며, entry price·FX·dividends가 없으면 realized return을 계산하지 않는다.",
    actual="FY2023 revenue는 €380.3m, EBITDA는 약 €51m으로 target trajectory에 접근했다. Constantia Flexibles가 지배권을 취득하고 최종 offer CHF16/share로 2025 거래·delisting이 진행됐다.",
    price="terminal cash consideration CHF16/share는 검증했다. 그러나 source catalog에 exact entry·purchase date·dividend·FX ledger가 없으므로 price gain·total return·IRR은 제시하지 않는다.",
    drivers="volume·pricing과 capacity ramp가 EBITDA를 키웠고 strategic buyer가 platform value를 인정했다. 다만 control transaction price가 minority investor의 원래 upside를 얼마나 실현했는지는 entry별로 다르다.", counterfactual="volume ramp 2년 지연, aluminum pass-through 6개월 lag와 working-capital peak를 넣어도 equity가 추가 debt 없이 2025까지 버틸 수 있었는가?", error="EBITDA target를 equity payoff와 가깝게 봤고 expansion capex·working capital·control shareholder가 terminal multiple을 제한할 가능성을 덜 반영했다.", warning="takeover terms가 CHF16으로 정해진 시점은 운영 thesis의 상단과 minority payoff가 달라질 수 있음을 보여준 최초의 security-level 신호였다.", first_signal_date="2024-02", lessons=LESSONS["aluflex"], checklist=CHECKLIST["aluflex"], scorecard=sc("운영 성공", "entry 없어 혼합", "capacity·takeout 실현", "common 적절·control risk", "2025 종료"),
    scenarios=[("Bear", "inflation·ramp miss", "margin<10%·debt", "미실현"), ("Base", "€425m·14%", "€59.5m EBITDA", "근접"), ("Bull", "strategic premium", "cash exit", "CHF16 실현")],
    metrics=[("2025 revenue", "€425m", "€425m", "2023 €380.3m", "목표의 89.5% two years early"), ("EBITDA margin", "14%", "14%", "2023 약 13.4%", "근접"), ("EBITDA", "€59.5m", "€59.5m", "2023 약 €51m", "85.7%"), ("Capacity", "expansion", "ramp", "operating scale 증가", "성공"), ("Terminal price", "upside", "rerating", "CHF16 cash", "entry 없어 혼합")],
    timeline=[("2022-05-29", "VIC Long", "2025 targets"), ("2022-H2", "inflation/pass-through", "margin test"), ("2023", "revenue €380.3m", "trajectory 확인"), ("2023", "EBITDA ~€51m", "margin 근접"), ("2024", "Constantia transaction", "control event"), ("2025-03-04", "join-forces announcement", "completion"), ("2025", "final CHF16 offer", "terminal cash"), ("2025", "delisting", "public-equity 종료")],
    claims=[
        claim("revenue €425m", "대체로 성공", "2025 revenue €425m.", "capacity·volume·price/mix가 sales를 늘린다.", "expansion plan과 defensive demand.", "ramp·pass-through가 작동.", "€350m 아래면 실패.", "2023 €380.3m.", "목표의 89.5%를 2년 전 달성.", "price inflation과 real volume 혼용.", "volume·price·FX bridge를 만든다."),
        claim("EBITDA margin 14%", "대체로 성공", "scale·pass-through로 14% margin.", "utilization과 price recovery가 input cost를 상쇄.", "historical margin·contracts.", "원재료 lag와 ramp cost 축소.", "12% 미만 지속이면 실패.", "2023 약 13.4%.", "-0.6ppt.", "adjusted EBITDA definition risk.", "reported·adjusted bridge를 고정한다."),
        claim("EBITDA €59.5m", "대체로 성공", "2025 약 €59.5m.", "€425m×14%.", "explicit target.", "revenue·margin 동시 달성.", "€45m 미만이면 실패.", "2023 약 €51m.", "-€8.5m/-14.3% two years early.", "point target 과신.", "range와 date를 같이 판정한다."),
        claim("capacity expansion", "성공", "new capacity가 demand를 수용한다.", "installed lines가 volume·mix를 높인다.", "announced capex.", "customer qualification·utilization 확보.", "low utilization·cash burn이면 실패.", "revenue·EBITDA scale-up 확인.", "방향 성공.", "capex return를 EBITDA로만 평가.", "incremental ROIC·cash payback을 본다."),
        claim("inflation reversal", "부분 성공", "commodity inflation 완화가 margin을 회복한다.", "aluminum·energy cost와 pass-through lag가 줄어든다.", "2022 inflation spike.", "selling price stickiness 유지.", "cost 재상승·price reset이면 실패.", "margin이 13%대로 회복.", "결과 지지·driver attribution 제한.", "macro timing 의존.", "contract별 pass-through lag를 추적한다."),
        claim("equity rerating", "혼합", "operating delivery가 depressed stock을 재평가한다.", "higher EBITDA와 strategic interest가 equity value를 높인다.", "low valuation.", "debt·control discount가 제한하지 않는다.", "offer가 intrinsic value 아래면 미달.", "CHF16 cash exit.", "entry 미복원으로 payoff 판정 제한.", "business success=stock success 등치.", "entry·FX·dividend·offer를 별도 ledger화한다."),
    ],
)


add(
    id="4613b14a-a509-480e-93c6-c1eca6c04c89", date="2003-12-11", author="dle413", ticker="AFR", company="American Financial Realty Trust", filename="analysis/ideas/2003/2003-12-11_AFR_long.md", source="https://www.valueinvestorsclub.com/idea/American_Financial_Realty/4242099557", group="afr", direction="Long", raw_direction="Short", security="REIT common equity / Long", entry="약 $16; annual dividend $1", horizon="2004~2006 occupancy·AFFO rerating", raw_horizon="AFFO/share $1.30~1.40, occupancy 88%→95%, target $19~20",
    title="acquisition-led financial-property REIT Long", verdict="실패 — asset growth가 주당가치로 전환되지 않음", score=2.5, process=4.5,
    conclusion="raw Short를 실제 Long으로 교정했다. 원문은 $16 entry, $1 dividend, occupancy 88→95%와 AFFO/share $1.30~1.40으로 $19~20을 기대했다. 그러나 leverage·dilution과 portfolio quality가 per-share value를 훼손했고 2007 Gramercy merger announcement value는 약 $8.43이었다. closing consideration은 $5.50 cash+0.12096 GKK shares와 adjustment였다.",
    t0="financial-institution properties를 대규모로 매입하고 vacancy를 lease-up해 occupancy를 88%에서 95%로 높이면 AFFO/share $1.30~1.40, dividend $1과 $19~20 target가 가능하다는 roll-up REIT thesis였다.", reverse="시장은 낮은 occupancy, acquisition integration, external financing·equity issuance, tenant/asset quality와 interest-rate risk를 할인했다. 자산규모가 커져도 AFFO/share와 NAV/share가 희석될 수 있었다.",
    valuation="$1.30~1.40 AFFO에 약 14~15x와 $1 dividend를 적용한 target였다. 그러나 acquisition cap rate에서 cost of debt·G&A·recurring capex·issued shares를 빼야 하며, vacancy lease-up cost까지 포함해야 한다.",
    actual="occupancy와 acquisition pipeline이 기대만큼 주당가치를 만들지 못했다. 2007 Gramercy merger는 $5.50 cash+0.12096 GKK share를 제시했고 announcement implied value는 약 $8.43이었다. 2008 closing에는 dividend-related cash adjustment $0.2419가 더해졌다.",
    price="announcement implied 약 $8.43은 $16 entry 대비 약 0.527x, -47.3% price comparison이다. interim dividends, exact dates, GKK closing/exit price와 tax ledger가 없으므로 total return·IRR은 아니다.",
    drivers="손실은 acquisition volume보다 financing cost·dilution·asset quality가 AFFO/share를 누른 데서 나왔다. merger는 upside catalyst가 아니라 distressed terminal outcome에 가까웠다.", counterfactual="occupancy가 95%여도 cost of capital이 cap rate를 웃돌고 equity가 발행되면 AFFO/share와 NAV/share가 늘 수 있었는가?", error="management의 asset pipeline과 gross acquisitions를 per-share compounding으로 오인했고 leverage·share issuance·lease-up capex의 denominator를 충분히 모델링하지 않았다.", warning="AFFO/share가 acquisition 규모만큼 늘지 않고 occupancy improvement가 지연된 첫 해가 핵심 break였으며 추가 equity-funded deals가 이를 강화했다.", first_signal_date="2005-03", lessons=LESSONS["afr"], checklist=CHECKLIST["afr"], scorecard=sc("실패", "AFFO/share 과대", "lease-up·rerating 실패", "common downside 노출", "경로 실패"),
    scenarios=[("Bear", "vacancy·dilution·refi", "$8~10", "merger 값 $8.43"), ("Base", "AFFO $1.30·$1 dividend", "$16~18", "미달"), ("Bull", "95% occupancy", "$19~20", "미실현")],
    metrics=[("Entry/target", "$16 / $19~20", "+19~25%+dividend", "announcement ~$8.43", "실패"), ("Dividend", "$1/year", "covered", "interim ledger 불완전", "판정 제한"), ("AFFO/share", "$1.30~1.40", "성장", "per-share thesis 미실현", "실패"), ("Occupancy", "88%", "95%", "lease-up 지연", "실패"), ("Merger", "upside optional", "value creation", "$5.50+0.12096 GKK", "distressed outcome")],
    timeline=[("2003-12-11", "VIC Long", "raw Short 교정"), ("2004", "acquisition expansion", "assets 증가"), ("2005-03", "per-share lag", "초기 break"), ("2005~06", "vacancy·financing", "AFFO pressure"), ("2007-07", "Gramercy merger", "implied ~$8.43"), ("2007-11-09", "merger proxy", "terms 확정"), ("2008-04-01", "deal close", "$5.50+0.12096"), ("2008", "$0.2419 adjustment", "closing ledger")],
    claims=[
        claim("raw Short", "metadata 실패", "source SQL은 Short다.", "방향이 payoff 해석을 바꾼다.", "원문은 upside·dividend를 샀다.", "본문이 실제 방향을 정한다.", "하락 베팅이면 Short다.", "실제 REIT common Long.", "완전 반대.", "raw metadata 의존.", "원문 cash-flow로 방향을 고정한다."),
        claim("occupancy 88→95%", "실패", "vacant space를 lease-up한다.", "higher occupied area가 NOI·AFFO를 높인다.", "portfolio vacancy와 pipeline.", "tenant demand·TI cost가 경제적이다.", "occupancy 정체·leasing cost 과다이면 실패.", "개선이 target value를 만들지 못했다.", "95% thesis 미실현.", "occupancy를 free growth로 봄.", "TI/LC·free rent 뒤 NOI를 본다."),
        claim("AFFO/share $1.30~1.40", "실패", "portfolio growth가 주당 AFFO를 높인다.", "NOI less interest·G&A over shares.", "management projections.", "cap rate>fully loaded capital cost.", "share growth가 AFFO를 앞서면 실패.", "terminal merger value가 큰 impairment를 반영.", "target multiple 미지지.", "asset growth와 per-share growth 혼동.", "denominator까지 pro forma한다."),
        claim("$1 dividend floor", "부분 성공", "6%+ dividend가 기다림을 보상한다.", "AFFO coverage가 cash distribution을 유지한다.", "declared dividend.", "coverage·liquidity 유지.", "cut 또는 uncovered payout이면 실패.", "interim dividends는 있었으나 capital loss를 상쇄 못함.", "price -47% before full ledger.", "yield를 downside floor로 오인.", "yield+NAV erosion을 같이 본다."),
        claim("$19~20 target", "실패", "AFFO growth·rerating으로 target.", "higher occupancy와 scale이 P/AFFO를 지지.", "explicit target.", "execution·capital market 정상.", "$19 미도달·downside merger면 실패.", "announcement value 약 $8.43.", "target 대비 -56%~-58%.", "bull execution을 base에 둠.", "bear NAV와 refinancing을 우선한다."),
        claim("M&A value creation", "실패", "대형 purchases가 platform value를 키운다.", "scale·leasing capability가 cost synergies를 낸다.", "deal pipeline.", "financing accretive.", "AFFO/NAV per share 하락이면 반증.", "Gramercy deal은 낮은 terminal value로 종료.", "$16→~$8.43 comparison.", "size를 moat로 봄.", "deal별 cap rate-cost of capital spread를 본다."),
    ],
)


add(
    id="293a1fae-c24d-4a12-ad7f-c1ccf110227c", date="2010-11-01", author="lvampa1070", ticker="AFRISJ", company="AfriSam Investment Holdings", filename="analysis/ideas/2010/2010-11-01_AFRISJ_secured_frn_long.md", source="", group="afrisam_note", direction="Long", raw_direction="Short", security="senior secured floating-rate notes / Long", entry="약 75~80 cents on par", horizon="2011~2013 restructuring", raw_horizon="issuer leverage 약 7x, market-price leverage 약 3.5x EBITDA; base return 14~15% annual",
    title="distressed secured-credit restructuring Long", verdict="구조조정 성공 / holder-level IRR 미확정", score=8.0, process=8.2,
    conclusion="raw Short를 실제 Long으로, security를 senior secured floating-rate notes로 교정했다. PIC와 80% 초과 noteholders가 합의했고 R15bn 초과 debt reduction·대규모 debt-to-equity conversion으로 capital structure가 정상화됐다. 다만 각 holder가 받은 cash/new notes/equity와 coupon ledger가 없어 14~15% IRR을 확정하지 않는다.",
    t0="AfriSam issuer leverage는 약 7x였지만 notes를 75~80c에 매입하면 market-price debt/EBITDA가 약 3.5x로 내려가고, collateral·restructuring에서 par보다 높은 recovery와 14~15% annual return을 기대한다는 distressed-credit thesis였다.", reverse="시장은 cement cycle, LBO overleverage, swap·interest burden, cross-border documentation, PIC의 policy objectives와 recovery timing을 할인했다. secured라는 표지만으로 collateral control과 priority가 보장되지 않는다.",
    valuation="enterprise value waterfall에서 super-priority·working-capital facilities, secured notes, swap termination, restructuring fees와 equity conversion을 순서대로 반영한다. quoted 75~80c와 par exchange를 cash recovery로 혼동하지 않는다.",
    actual="2011 PIC와 80% 초과 senior noteholders가 restructuring을 지지했다. 2013 완료된 package는 debt를 R15bn 이상 줄이고 상당액을 equity로 전환했으며 remaining senior debt를 새로운 notes로 재편했다. Lazard가 noteholders를 자문했다.",
    price="restructuring headline은 claim preservation을 지지하지만 exact purchase price, accrued coupon, new-note principal/price, equity realization과 dates가 없다. 따라서 14~15% annual return이나 exact recovery percentage를 재구성하지 않는다.",
    drivers="secured creditor coordination과 PIC의 going-concern incentive가 liquidation 대신 deleveraging을 만들었다. swap·interest burden 축소와 debt-to-equity conversion이 enterprise continuity를 보존했다.", counterfactual="cement EBITDA -25%, collateral value -30%, two-year delay와 super-priority funding을 반영해도 75c purchase가 principal·coupon을 충분히 회수했는가?", error="market-price leverage 3.5x를 recovery coverage처럼 사용했고 collateral perfection·swap priority·new-money priming과 equity exit liquidity를 더 명시적으로 다뤄야 했다.", warning="2011 majority support agreement는 촉매 확인이었지만 cash realization이 아니라 restructuring path의 확정일 뿐이었다.", first_signal_date="2011-12-09", lessons=LESSONS["afrisam_note"], checklist=CHECKLIST["afrisam_note"], scorecard=sc("issuer 정상화", "75~80c coverage 지지", "restructuring 성공", "secured notes 정확", "실현수익 미확정"),
    scenarios=[("Bear", "EBITDA -25%·liquidation", "recovery<75c", "미실현"), ("Base", "debt-to-equity·new notes", "claim 보존", "실현"), ("Bull", "operating recovery·equity upside", "14~15%+", "ledger 불완전")],
    metrics=[("Purchase", "75~80c", "par-near recovery", "package 완료", "cash recovery 미확정"), ("Issuer leverage", "약 7x", "대폭 감소", "R15bn+ debt reduction", "강한 성공"), ("Market-price leverage", "약 3.5x", "coverage", "EV ledger 제한", "방향 성공"), ("Support", "협상 필요", ">75%", ">80% noteholders", "성공"), ("Base return", "14~15% annual", "1~3년", "holder ledger 없음", "미확정")],
    timeline=[("2010-11-01", "VIC note Long", "raw Short 교정"), ("2011-H1", "restructuring talks", "coordination"), ("2011-12-09", "PIC agreement", ">80% support"), ("2012", "terms implementation", "debt conversion"), ("2012", "swap/interest reset", "cash burden 감소"), ("2013-04-02", "completion 발표", "R15bn+ reduction"), ("2013", "new debt/equity", "claim rollover"), ("2026-09-18", "research cutoff", "exact holder IRR 미복원")],
    claims=[
        claim("raw Short", "metadata 실패", "source SQL은 Short다.", "방향 오류는 creditor payoff를 반전시킨다.", "원문은 discount notes를 매수했다.", "본문 security가 실제 방향을 정한다.", "default 이익을 노리면 Short다.", "실제 secured-note Long.", "완전 반대.", "raw flag 의존.", "증권·방향을 원문으로 교정한다."),
        claim("senior secured status", "대체로 성공", "notes가 collateral 우선권을 갖는다.", "secured priority가 EV recovery를 보호한다.", "indenture/원문 구조.", "lien perfection·priority 유지.", "priming·collateral shortfall이면 실패.", "restructuring에서 senior group이 핵심 협상자였다.", "claim influence 확인; exact recovery 제한.", "secured를 full coverage로 오인.", "collateral별 waterfall을 만든다."),
        claim("75~80c recovery asymmetry", "방향 성공", "discount가 loss를 흡수하고 upside를 준다.", "purchase discount와 coupon이 recovery cushion.", "quoted price와 EBITDA.", "EV가 senior claims를 커버.", "recovery<75c면 실패.", "claims가 new structure로 보존·전환됐다.", "cash equivalent 미확정.", "new paper를 par로 표시.", "market value와 realized cash를 구분한다."),
        claim("deleveraging", "강한 성공", "구조조정이 debt를 크게 줄인다.", "debt-to-equity와 terms reset.", "PIC·noteholder incentives.", "supermajority·court/consents 확보.", "deal collapse면 실패.", "R15bn 초과 debt reduction.", "규모·방향 강한 적중.", "equity dilution은 creditor별 상이.", "issuer와 holder 성과를 분리한다."),
        claim("swap·interest relief", "성공 방향", "Euribor swap 종료와 interest 감소.", "cash coupon burden 축소가 going concern을 높인다.", "원문 catalyst.", "termination cost manageable.", "swap claim이 recovery를 잠식하면 실패.", "new structure가 historic burden을 낮췄다.", "exact swap settlement 미공개.", "gross debt reduction과 cash interest 혼용.", "coupon·swap cash dates를 별도 둔다."),
        claim("14~15% annual return", "미확정", "restructuring으로 mid-teens annual 수익.", "discount accretion+coupon+equity option.", "75~80c entry.", "1~3년 내 liquid recovery.", "지연·illiquid paper면 미달.", "package 완료, holder ledger 없음.", "IRR 산출 불가.", "par exchange를 실현으로 볼 위험.", "cash·PIK·equity를 날짜별로 추적한다."),
    ],
)


add(
    id="b35657a5-2f7a-46d2-9ba6-fce1d64f5466", date="2021-02-08", author="ril1212", ticker="AFRM", company="Affirm Holdings Inc.", filename="analysis/ideas/2021/2021-02-08_AFRM_short.md", source="", group="affirm", direction="Short", raw_direction="Short", security="Affirm Class A common equity / Short", entry="약 $122", horizon="12~24개월 valuation reset", raw_horizon="$30 target, 약 33x FY2022 sales; Peloton concentration·credit normalization·BNPL competition",
    title="valuation·concentration BNPL Short", verdict="매우 강한 성공 — $30 target 초과 하락", score=9.0, process=8.5,
    conclusion="$122에서 $30을 본 short는 2022 low close 약 $8.91로 target를 크게 넘어섰다. Peloton revenue share도 FY2021 약 20%에서 FY2022 약 8%로 낮아졌다. multiple compression·rates·merchant normalization이 함께 작동했다. 이후 회사가 생존·재성장한 사실은 original 12~24개월 short 성공과 분리한다.",
    t0="Affirm은 consumer lender인데 fintech platform으로 평가되어 FY2022 sales 약 33x를 받았다. Peloton concentration, stimulus/WFH demand, subprime credit와 BNPL competition이 정상화되면 $30까지 reprice될 수 있다는 short였다.", reverse="시장은 network expansion, superior underwriting data, no-late-fee brand, merchant conversion lift와 abundant funding이 높은 growth를 오래 유지한다고 봤다. short에는 borrow·squeeze·timing risk가 컸다.",
    valuation="sales multiple은 시작점일 뿐 GMV×take rate에서 funding·credit loss·processing을 뺀 RLTC economics를 본다. $30 target는 growth·margin·dilution과 lender multiple을 연결해야 한다.",
    actual="Peloton concentration은 FY2021 revenue 약 20%에서 FY2022 약 8%로 하락했다. 2022 rates와 long-duration multiple compression, consumer/merchant normalization이 겹치며 주가는 single digits로 내려갔다. 이후 merchant diversification과 product expansion으로 사업은 살아남고 주가도 반등했다.",
    price="$122→$30은 short price move 기준 약 75.4% 하락, $122→$8.91은 약 92.7% 하락이다. borrow cost·entry/cover date·position sizing이 없어 realized short return이나 IRR로 부르지 않는다.",
    drivers="초기 valuation duration이 너무 길었고 Peloton concentration unwind와 rates가 동시에 multiple을 압축했다. business insolvency가 아니라 expectations reset만으로 target를 넘었다.", counterfactual="GMV growth가 50%, credit losses가 안정되고 Peloton 없이도 merchants가 확대될 때 $30 target가 정당했는가, 아니면 rates만으로도 충분했는가?", error="credit deterioration를 크게 강조했지만 실제 빠른 driver는 rates·valuation compression이었다. borrow·squeeze와 target hit 뒤 cover rule도 더 명시했어야 한다.", warning="2021-H2 Peloton contribution 둔화와 2022 초 multiple collapse가 최초 확인 신호였고 $30 도달은 thesis review/cover trigger였다.", first_signal_date="2022-01", lessons=LESSONS["affirm"], checklist=CHECKLIST["affirm"], scorecard=sc("사업 생존", "매우 강한 성공", "Peloton·rates 실현", "short path 성공", "12~24개월 성공"),
    scenarios=[("Bear for short", "growth·funding 지속", "$150+ squeeze", "2021 volatility"), ("Base", "multiple 8x sales", "$50~70", "하회"), ("Bull for short", "normalization·rates", "$30 이하", "$8.91")],
    metrics=[("Entry/target", "$122/$30", "-75.4% price", "low ~$8.91", "target 초과"), ("Sales multiple", "33x FY2022E", "compression", "2022 reset", "성공"), ("Peloton share", "FY2021 ~20%", "decline", "FY2022 ~8%", "-12ppt"), ("Credit", "normalization risk", "worse", "mixed vs valuation", "부분"), ("Business survival", "not required", "reprice", "survived/rebounded", "short horizon와 양립")],
    timeline=[("2021-02-08", "VIC Short", "$122→$30"), ("2021-H2", "Peloton 둔화", "concentration unwind"), ("2021-FY", "Peloton ~20% revenue", "high concentration"), ("2022-01", "growth multiple collapse", "first signal"), ("2022-FY", "Peloton ~8%", "diversification/decline"), ("2022-H1", "$30 하회", "target hit"), ("2022-12", "low close ~$8.91", "maximum thesis expression"), ("2023~26", "business rebound", "cover discipline 중요")],
    claims=[
        claim("33x sales", "강한 성공", "consumer lender에 33x sales는 과도하다.", "rates·risk premium 상승 시 duration multiple이 압축된다.", "T0 valuation.", "growth가 극단적 multiple을 정당화 못한다.", "multiple 유지·FCF 급증이면 실패.", "2022 대폭 compression.", "$122→single digits.", "sales와 RLTC economics bridge 부족.", "lender는 credit-adjusted margin으로 평가한다."),
        claim("Peloton concentration", "성공", "Peloton 의존이 성장취약점이다.", "merchant slowdown이 GMV·revenue를 직접 낮춘다.", "FY2021 약 20% revenue.", "대체 merchants가 즉시 못 채운다.", "share 유지·대체 성장 시 약화.", "FY2022 약 8%.", "-12ppt/-60% relative.", "decline과 diversification을 구분하지 않음.", "merchant별 GMV·economics를 본다."),
        claim("stimulus/WFH normalization", "성공", "pandemic demand가 되돌아간다.", "durables·fitness checkout volume이 정상화.", "2020~21 pull-forward.", "new categories가 상쇄 못함.", "ex-Peloton growth가 가속하면 약화.", "2022 merchant/consumer normalization.", "방향 적중.", "macro와 company-specific attribution 혼용.", "cohort·category별 GMV를 본다."),
        claim("credit risk", "부분 성공", "subprime exposure가 losses를 높인다.", "stimulus 종료·rates가 delinquencies/funding cost를 올린다.", "borrower mix.", "underwriting model이 cycle을 못 막는다.", "loss stable이면 실패.", "credit/funding 압력은 증가했지만 collapse 핵심은 valuation.", "driver가 예상보다 작음.", "stock thesis와 solvency thesis 혼동.", "vintage loss·funding spread를 분리한다."),
        claim("competition", "성공", "Klarna·Afterpay·PayPal 등이 economics를 압박한다.", "merchant fee·customer acquisition이 경쟁으로 낮아진다.", "BNPL entrants.", "Affirm differentiation 제한.", "take rate·share 상승이면 반증.", "경쟁 심화 속에서도 회사는 생존·확장.", "valuation pressure 지지, terminal failure 아님.", "competition을 commoditization으로 과장.", "merchant conversion lift와 unit margin을 비교한다."),
        claim("$30 target", "강한 성공", "$122에서 $30.", "growth/multiple normalization이 target를 만든다.", "explicit price target.", "12~24개월 내 reset.", "$30 미도달이면 실패.", "2022 $30 하회, low ~$8.91.", "target 대비 70% 추가 하락.", "cover rule 미정.", "target hit 시 thesis·risk를 재설정한다."),
    ],
)


add(
    id="6710e82a-933f-47cc-b05e-95860517a3d4", date="2010-01-13", author="lvampa1070", ticker="AFSI", company="AmTrust Financial Services Inc.", filename="analysis/ideas/2010/2010-01-13_AFSI_short.md", source="https://www.valueinvestorsclub.com/idea/AmTrust_Financial_Services_Inc/4991867320", group="amtrust", direction="Short", raw_direction="Short", security="AmTrust common equity / Short", entry="약 $12", horizon="1~3년 governance·ROE normalization", raw_horizon="20%+ ROE unsustainable; Maiden related-party reinsurance·family control·SEC/litigation catalysts",
    title="governance·related-party insurer Short", verdict="실패 — concerns 후행 적중, stock path 치명적", score=3.0, process=5.5,
    conclusion="related-party·accounting 우려는 2017 restatement와 internal-control 문제로 일부 검증됐고 2018 take-private는 $14.75였다. 그러나 2010 약 $12 short 뒤 주가는 2011 약 $19, 2012 약 $27로 두 배 이상 역행했다. 수년 뒤 문제 발견은 path-dependent short를 성공으로 바꾸지 않는다.",
    t0="20%+ ROE와 premium growth가 Maiden reinsurance·family control·aggressive accounting에 기대고 있어 정상화되며 multiple이 낮아진다는 short였다. 소송, SEC follow-up 또는 Maiden minority pressure가 촉매였다.", reverse="시장은 niche underwriting, acquisition growth와 reinsurance access가 높은 ROE·book growth를 지속한다고 봤다. insurer accounting concern은 catalyst 없이 여러 해 지속될 수 있고 short의 carry·squeeze가 컸다.",
    valuation="reported ROE를 underwriting, leverage, reserve releases, acquisition accounting와 related-party reinsurance로 분해해야 한다. 낮은 quality에 할인 multiple을 적용하더라도 catalyst timing·book growth가 short carry를 압도할 수 있다.",
    actual="주가는 2011 약 $19, 2012 약 $27로 entry 대비 2배 이상 올랐다. 2017 회사는 2014·2015와 2016 interim statements를 restate하고 internal-control issues를 밝혔다. 2018 take-private price는 $14.75였다.",
    price="$12→$27은 short에 약 125% adverse price move이며 단순 short P&L은 initial capital 기준 -125% before borrow/cover mechanics가 될 수 있다. $14.75 terminal도 entry보다 22.9% 높다. exact realized return은 position ledger가 없어 제시하지 않는다.",
    drivers="fundamental concern보다 premium·book growth와 delayed catalyst가 먼저 작동했다. short는 eventual accounting validation 전에 adverse excursion과 years of carry를 견뎌야 했다.", counterfactual="restatement가 7년 뒤에야 나온다면 borrow cost·margin calls·2.25x adverse excursion을 감수하고도 expected value가 양수였는가?", error="governance red flags를 imminent earnings collapse로 번역했고 reserve/accounting catalyst의 법적·감사 timeline과 explicit stop-loss/position size를 두지 않았다.", warning="2011 주가 약 $19와 계속된 premium/book growth가 timing thesis의 첫 명확한 반증이었고 2012 $27은 trade-level failure를 확정했다.", first_signal_date="2011-12", lessons=LESSONS["amtrust"], checklist=CHECKLIST["amtrust"], scorecard=sc("우려 일부 후행 적중", "timing 실패", "촉매 7년 지연", "short path 부적합", "명확한 실패"),
    scenarios=[("Bear for short", "ROE·growth 지속", "$20~30", "2011~12 실현"), ("Base", "gradual normalization", "$10~14", "2018 $14.75"), ("Bull for short", "SEC·restatement early", "$6~8", "수년 지연·미실현")],
    metrics=[("Entry", "$12 short", "하락", "2012 ~$27", "125% adverse"), ("ROE", "20%+ unsustainable", "급락", "수년 지속", "timing 실패"), ("Catalyst", "SEC/lawsuit", "1~3년", "2017 restatement", "약 7년 지연"), ("Restatement", "accounting concern", "material", "2014/15 NI -7.2%/-11.2%", "부분 적중"), ("Take-private", "downside", "below entry", "$14.75", "entry보다 +22.9%")],
    timeline=[("2010-01-13", "VIC Short", "~$12"), ("2011", "stock ~$19", "timing break"), ("2012", "stock ~$27", "2.25x adverse"), ("2013~16", "growth 지속", "carry·squeeze"), ("2017-04-10", "restatement notice", "concerns validation"), ("2017-04-11", "net income reductions", "quantification"), ("2018-06-07", "$14.75 amended deal", "terminal price"), ("2018", "take-private", "public short 종료")],
    claims=[
        claim("20%+ ROE unsustainable", "후행 부분 성공", "ROE가 reserve·related-party 구조로 과대다.", "normalization이 earnings/book growth를 낮춘다.", "peer gap와 disclosures.", "reported profitability가 곧 mean revert.", "ROE 지속·book growth면 timing 실패.", "수년 지속 후 accounting issues.", "1~3년 horizon miss.", "quality와 timing 혼동.", "ROE driver마다 catalyst clock을 둔다."),
        claim("Maiden related-party risk", "부분 검증", "family-linked reinsurance가 economics를 왜곡한다.", "ceding commission·recoverables가 earnings/capital을 이동시킨다.", "ownership·transactions.", "arm's-length terms가 아니다.", "independent economics가 우수하면 약화.", "governance scrutiny는 커졌지만 immediate collapse 없음.", "red flag≠near-term loss.", "관계 자체를 손실로 간주.", "terms·collateral·counterparty를 계량한다."),
        claim("accounting/internal control", "후행 성공", "aggressive accounting가 restatement를 부른다.", "revenue/reserve errors가 earnings를 낮춘다.", "SEC comments·complex structure.", "errors가 material하다.", "clean audits 지속이면 실패.", "2017 restatement·control issues.", "2014 NI -7.2%, 2015 -11.2%.", "발현 연도 예측 실패.", "accounting claim과 trade clock을 분리한다."),
        claim("near-term catalyst", "실패", "소송·SEC·Maiden holders가 1~3년 내 촉발한다.", "external scrutiny가 terms·valuation을 바꾼다.", "complaint·comment letter.", "regulators/holders가 행동한다.", "3년 내 무사건이면 실패.", "material event는 2017.", "약 7년 지연.", "가능성을 imminence로 번역.", "dated catalyst가 없으면 position을 줄인다."),
        claim("valuation compression", "실패", "quality discount로 stock이 entry 아래 간다.", "lower ROE·multiple가 price를 낮춘다.", "$12 entry.", "book growth가 discount를 상쇄 못함.", "$18 이상 지속이면 실패.", "2011 $19, 2012 $27.", "+58%·+125% adverse.", "fundamental target에 path 무시.", "MAE·borrow·stop을 사전 정의한다."),
        claim("terminal downside", "실패", "eventual resolution이 short profit을 준다.", "restatement·control change가 equity value를 낮춘다.", "governance thesis.", "terminal price<entry.", "take-private above entry면 실패.", "2018 $14.75.", "$2.75/+22.9% above entry.", "후행 문제를 성공으로 소급.", "entry-to-terminal payoff로 최종 판정한다."),
    ],
)


ORDER = [
    "f0eefbcc-1ae2-4b53-aa04-94430fbdbba6",
    "b3a18d0f-17bf-4636-b562-3896bb122e2a",
    "31a1b41b-df44-440e-b8b0-ba7c55537bee",
    "ccaba7d9-3979-46a6-84ef-7cac99f42499",
    "ee7d3bda-2526-406c-a821-2381fc5664d7",
    "c32c272b-06de-4d82-b435-a646a7f66879",
    "4613b14a-a509-480e-93c6-c1eca6c04c89",
    "293a1fae-c24d-4a12-ad7f-c1ccf110227c",
    "b35657a5-2f7a-46d2-9ba6-fce1d64f5466",
    "6710e82a-933f-47cc-b05e-95860517a3d4",
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
        "# Batch 069 — AFMI / Alphamin / Ag Growth / AFOP / Aluflexpack / AFR / AfriSam / Affirm / AmTrust V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. 방향·증권·corporate action·payoff를 먼저 고정하고 1차자료로 actual을 검증했다.", "",
        "## Canonical idea files", "", "| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## Direction / security / return audit", "",
        "- AFN.UN 2004, AFR 2003, AFRISJ 2010의 raw Short를 실제 Long으로 교정했다.",
        "- AFRISJ는 common이 아니라 AfriSam senior secured floating-rate notes Long이다.",
        "- AFOP 2010은 1-for-5 reverse split과 2-for-1 split을, AFOP 2012는 2-for-1 split을 반영했다. 2012 cash distribution은 별도 payoff다.",
        "- source SQL performance row가 10건 모두 없어 verified operating actual·cash consideration·split-adjusted price comparison만 사용했다. complete ledger 없는 exact total return·IRR은 만들지 않았다.", "",
        "## 핵심 판정", "",
        "1. AFMI는 deal thesis는 실패했지만 $6 cash+residual share로 trust-floor thesis가 성공했다.",
        "2. Alphamin은 FTR·deleveraging·Mpama South·배당이 순차적으로 실현된 강한 성공이다.",
        "3. Ag Growth는 high-margin replacement niche와 distribution·bolt-on M&A가 작동했다.",
        "4. AFOP 두 vintage는 net cash·profitability·strategic value가 Corning $18.50 cash deal로 crystallize됐다.",
        "5. Aluflexpack은 운영 target에 접근했지만 CHF16 takeout의 투자수익은 entry ledger가 없어 혼합 판정이다.",
        "6. AFR은 asset growth가 AFFO/share로 전환되지 않았고, AfriSam note는 restructuring이 성공했지만 holder-level IRR은 미확정이다.",
        "7. Affirm short는 빠른 valuation reset으로 성공했지만 AmTrust short는 우려가 훗날 맞아도 2배 adverse path 때문에 실패했다.", "",
        "## 구조화 데이터", "",
        "- `data/curated/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.",
        "- `data/curated/batch_069_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.",
        "- `analysis/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_10.md`: Streamlit wrapper.", "",
    ])


def main():
    IDEAS.sort(key=lambda i: ORDER.index(i["id"]))
    if [i["id"] for i in IDEAS] != ORDER:
        raise ValueError("Batch 069 idea order or IDs do not match catalog boundary")
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
            "**C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·corporate-action payoff만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.",
        )
        report_path.write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_069_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 069 — AFMI / Alphamin / Ag Growth / AFOP / Aluflexpack / AFR / AfriSam / Affirm / AmTrust V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 069 V9 Index](batch_069_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 69
    payload["title"] = "AFMI / Alphamin / Ag Growth / AFOP / Aluflexpack / AFR / AfriSam / Affirm / AmTrust — Structure, Splits, Per-Share Value and Short Timing V9"
    payload["metadata_audit"] = {
        "direction_corrections": 3,
        "company_mapping_corrections": 0,
        "security_type_corrections": 1,
        "split_adjustments": 2,
        "cross_batch_duplicates_removed": 0,
        "performance_rows_rejected": 10,
        "corporate_action_terminal_payoffs": 6,
        "notes": [
            "AFN.UN 2004, AFR 2003, AFRISJ 2010 raw Short를 실제 Long으로 교정하되 raw flag를 보존했다.",
            "AFRISJ를 common이 아니라 senior secured floating-rate notes로 교정했다.",
            "AFOP 두 vintage는 reverse/forward split을 같은 주당 기준으로 맞추고 cash distribution을 별도 처리했다.",
            "source SQL performance row가 10건 모두 부재해 exact total return·IRR을 생성하지 않았다.",
            "AFMI liquidation residual과 AfriSam new claims는 nominal security를 cash recovery로 간주하지 않았다.",
            "Affirm·AmTrust short는 eventual concern보다 horizon과 adverse path를 우선해 판정했다.",
        ],
    }
    payload["batch_lessons"] = [
        "SPAC operating deal과 trust-floor payoff는 별도 claim이다.",
        "resource optionality는 discovery에서 production까지 단계별 probability를 적용한다.",
        "income yield는 maintenance capex·working capital 뒤 coverage로 검증한다.",
        "split·distribution·cash acquisition은 하나의 corporate-action ledger로 맞춘다.",
        "operating forecast 적중이 곧 common return 적중은 아니다.",
        "distressed exchange의 par-for-paper는 realized cash recovery가 아니다.",
        "short는 eventual diagnosis보다 catalyst clock·MAE·cover rule이 더 중요하다.",
    ]
    failure_patterns = {
        "afmi": "deal_probability; trust_leakage; residual_value; event_duration",
        "alphamin": "commodity_price; recovery; single_asset; jurisdiction_shutdown",
        "agi": "peak_margin; payout_coverage; cycle; acquisition_integration",
        "afop": "split_basis; cash_burn; customer_concentration; takeout_dependency",
        "aluflex": "ebitda_vs_equity; capex_ramp; working_capital; control_discount",
        "afr": "asset_vs_per_share; dilution; leverage; occupancy_cost",
        "afrisam_note": "security_mapping; nominal_par; priority; illiquid_recovery",
        "affirm": "valuation_duration; concentration; credit; short_cover",
        "amtrust": "catalyst_delay; related_party; reserve_opacity; adverse_excursion",
    }
    success_patterns = {
        "afmi": "trust_audit; branch_payoff; vote_calendar; liquidation_ledger",
        "alphamin": "recovery; deleveraging; staged_expansion; distributions",
        "agi": "replacement_demand; cash_coverage; unit_economics; bolt_on",
        "afop": "net_cash; normalized_profit; corporate_action; strategic_exit",
        "aluflex": "target_bridge; capacity_ramp; operating_actual; terminal_terms",
        "afr": "affo_per_share; coverage; cost_of_capital; nav_stress",
        "afrisam_note": "exact_security; collateral; creditor_coordination; waterfall",
        "affirm": "expectation_reset; concentration_tracking; target_discipline; cover",
        "amtrust": "reserve_audit; catalyst_clock; position_size; terminal_payoff",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failure_patterns[idea["group"]]
        row["success_pattern_ko"] = success_patterns[idea["group"]]
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
