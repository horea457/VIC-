#!/usr/bin/env python3
"""Build Batch 067 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
CATALOG = ROOT / "data/curated/batch_067_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_067_aezs_af_afc_afce_deep_v7.json"

spec = importlib.util.spec_from_file_location("batch64_base", ROOT / "scripts/64_build_batch_064_v9.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "aezs": (
        "Aeterna Zentaris는 임상·규제 단계의 의약품을 개발하고 license하는 소형 biotech였다. T0 common의 가치는 "
        "현금에서 burn과 부채를 뺀 runway, Macrilen과 Zoptrex의 임상·규제 성공확률, 승인 뒤 milestone·royalty의 "
        "risk-adjusted present value로 구성됐다. 각 프로그램의 clinical, regulatory, financing outcome을 분리해야 한다."
    ),
    "astoria": (
        "Astoria Financial은 Long Island·NYC에서 예금과 wholesale funding으로 주택담보대출·multifamily/CRE·MBS를 "
        "보유한 thrift였다. earning assets×yield에서 deposits·FHLB·CD funding cost를 뺀 NIM이 핵심이며, mortgage "
        "prepayment와 asset/liability repricing 속도가 대손보다 먼저 EPS를 흔들 수 있다."
    ),
    "alarmforce": (
        "AlarmForce는 월 모니터링료를 받는 residential security 회사였다. 신규 고객 CAC를 먼저 지출하고 장기간 "
        "monthly recurring revenue와 높은 gross margin으로 회수한다. 고객 lifetime, churn, 지역별 설치·광고 CAC와 "
        "현금전환이 subscriber growth보다 중요하며, contracted base는 전략적 인수자에게 별도 가치가 있다."
    ),
    "allmerica": (
        "Allmerica Financial은 당시 P&C 보험과 자본집약적 life·annuity blocks를 함께 보유했다. P&C underwriting·float "
        "가치에서 life reserve, guarantee와 holding-company claims를 차감한 SOTP가 common 가치다. life book을 "
        "coinsurance·매각하면 불확실성이 줄지만, headline asset value가 곧 common recovery는 아니다."
    ),
    "allied_note": (
        "Allied Capital은 중소기업 대출·지분을 보유한 BDC였다. 이 아이디어의 대상은 common이 아니라 거래소 상장 "
        "6.875% senior unsecured notes due 2047이다. asset coverage, seniority, coupon, change of control와 call 조건이 "
        "payoff를 만들며 common NAV 회복은 필요한 조건이 아니었다."
    ),
    "afce": (
        "AFC Enterprises는 Church's·Cinnabon을 매각한 뒤 Popeyes 중심의 asset-light restaurant franchisor가 됐다. "
        "franchise royalty·advertising fees와 company-store margin에서 G&A를 뺀 현금이 핵심이다. SSS, unit growth, "
        "franchisee economics, buyback과 asset-sale distribution이 주당가치를 결정한다."
    ),
}

ENGINE = {
    "aezs": "cash + risk-adjusted program value - quarterly burn - debt/dilution = common value; program별 PoS와 승인 뒤 경제조건을 따로 둔다.",
    "astoria": "earning assets × asset yield - interest-bearing liabilities × funding cost - provision - opex - tax = earnings; repricing bucket과 prepayment를 월별로 잇는다.",
    "alarmforce": "subscriber additions × lifetime gross profit - CAC - service/installation cost - G&A - capex = FCF; 지역별 cohort payback과 churn을 분리한다.",
    "allmerica": "P&C value + realizable life value - reserve/guarantee risk - debt = common SOTP; transaction proceeds와 retained liabilities를 같이 본다.",
    "allied_note": "realizable portfolio value - senior/secured claims - burn = unsecured-note coverage; coupon과 par redemption을 실제 cash dates로 계산한다.",
    "afce": "franchised units × sales × royalty rate + company-store profit - G&A - tax - capex = FCF; buyback·dividend·M&A를 fully diluted share 기준으로 연결한다.",
}

KPI = {
    "aezs": "unrestricted cash, quarterly burn, fully diluted shares, trial endpoint, p-value/CI, FDA milestone, launch/license terms, royalty rate, patent life",
    "astoria": "NIM, asset yield, deposit beta, wholesale funding cost, repricing gaps, prepayment speed, premium amortization, NII, operating EPS, tangible capital",
    "alarmforce": "subscribers, net adds, churn, ARPU, gross margin, CAC/SAC, payback, cohort IRR, recurring-revenue mix, FCF/share",
    "allmerica": "P&C combined ratio, reserve development, life capital, guarantee exposure, transaction proceeds, holding debt, book/share, statutory capital",
    "allied_note": "portfolio fair value, nonaccruals, secured claims, unsecured coverage, liquidity, coupon, quoted price/par, call price, accrued interest",
    "afce": "global SSS, net unit growth, franchise mix, royalty revenue, restaurant margin, G&A, adjusted EPS, FCF/share, buyback price, leverage",
}


SOURCES = {
    "aezs": [
        S("Zoptrex Phase III results", "https://www.sec.gov/Archives/edgar/data/1113423/000110465917028299/a17-11254_5ex99d1.htm", "SEC / Aeterna Zentaris", "2017-05-01", "OS 10.9개월 대 10.8개월, primary endpoint 실패와 추가개발 중단 검증."),
        S("Macrilen license to Strongbridge", "https://www.sec.gov/Archives/edgar/data/1113423/000114420418002797/tv483609_ex99-1.htm", "SEC / Aeterna Zentaris", "2018-01-16", "2017-12-20 FDA 승인과 $24m upfront, 15%/18% royalty 조건 검증."),
        S("Aeterna Q2 2018 results", "https://www.sec.gov/Archives/edgar/data/1113423/000162828018010941/q2-2018xex991fsxquarterly1.htm", "SEC / Aeterna Zentaris", "2018-08", "Macrilen license 후 현금·사업전개 교차검증."),
    ],
    "astoria": [
        S("Astoria 2005 results", "https://www.sec.gov/Archives/edgar/data/910322/000127528706001133/af4938ex991.htm", "SEC / Astoria Financial", "2006-01", "2004 operating EPS $2.09, 2005 diluted EPS $2.26와 repurchase 검증."),
        S("Astoria FY2007 results", "https://www.sec.gov/Archives/edgar/data/910322/000114420408003676/v100570_ex99-1.htm", "SEC / Astoria Financial", "2008-01-24", "2007 operating EPS $1.50, GAAP $1.36, NIM과 NII 감소 검증."),
    ],
    "alarmforce": [
        S("AlarmForce FY2010 results", "https://www.newswire.ca/news-releases/alarmforce-closes-2010-fiscal-year-with-over-113500-subscribers-547257212.html", "AlarmForce / CNW", "2011", "FY2010 subscriber 113,500명 검증."),
        S("AlarmForce FY2015 results", "https://www.globenewswire.com/news-release/2016/01/21/1279609/0/en/AlarmForce-Reports-Q4-2015-Financial-Results.html", "AlarmForce", "2016-01-21", "FY2015 subscriber 144,200명과 운영성과 검증."),
        S("BCE acquisition announcement", "https://www.globenewswire.com/news-release/2017/11/06/1324295/0/en/alarmforce-to-be-acquired-by-bce.html", "BCE / AlarmForce", "2017-11-06", "C$16 현금 거래조건 검증."),
        S("BCE completes AlarmForce acquisition", "https://www.globenewswire.com/news-release/2018/01/05/1324311/0/en/bce-completes-acquisition-of-alarmforce.html", "BCE", "2018-01-05", "인수 종결과 terminal payoff 검증."),
    ],
    "allmerica": [
        S("Allmerica FY2003 Form 10-K", "https://www.sec.gov/Archives/edgar/data/944695/000119312504037515/d10k.htm", "SEC / Allmerica", "2004-03", "life restructuring, P&C와 자본구조 후속 검증."),
        S("Allmerica SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=944695&owner=exclude", "SEC", "2002-2005", "coinsurance·asset sale·Hanover 전환 공시 교차검증."),
    ],
    "allied_note": [
        S("Ares assumes Allied notes", "https://www.sec.gov/Archives/edgar/data/1287750/000104746910003449/a2197910z8-k.htm", "SEC / Ares Capital", "2010-04-01", "Allied 인수와 2047 notes assumption, coupon·call 조건 검증."),
        S("2047 notes redemption", "https://www.sec.gov/Archives/edgar/data/1287750/000128775021000014/arcc-2047seniornotesredemp.htm", "SEC / Ares Capital", "2021-02-23", "$229.56m 잔액을 $25 par+accrued interest로 상환한 조건 검증."),
    ],
    "afce": [
        S("AFC Enterprises FY2004 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1041379/000095014405003142/g93770ke10vk.htm", "SEC / AFC Enterprises", "2005-03", "Church's·Cinnabon divestiture와 Popeyes 전환 검증."),
        S("AFC Enterprises Q2 2005 filing", "https://www.sec.gov/Archives/edgar/data/1041379/000095014405011657/g98284e10vq.htm", "SEC / AFC Enterprises", "2005", "$12 special dividend와 후속 자본구조 검증."),
        S("Popeyes FY2008 results", "https://www.sec.gov/Archives/edgar/data/1041379/000095014409002109/g18056exv99w1.htm", "SEC / AFC Enterprises", "2009", "2008 adjusted EPS $0.76와 SSS 약세 검증."),
        S("Popeyes FY2010 results", "https://www.sec.gov/Archives/edgar/data/1041379/000095012311001632/g25746exv99w1.htm", "SEC / AFC Enterprises", "2011", "2010 global SSS +2.6%와 turnaround 진전 검증."),
        S("Popeyes FY2011 results", "https://www.sec.gov/Archives/edgar/data/1041379/000119312512101764/d312134dex991.htm", "SEC / AFC Enterprises", "2012", "2011 adjusted EPS $0.99 검증."),
        S("Popeyes FY2012 results", "https://www.sec.gov/Archives/edgar/data/1041379/000119312513080821/d491588dex991.htm", "SEC / AFC Enterprises", "2013", "2012 adjusted EPS $1.24와 성장경로 검증."),
        S("Popeyes FY2015 results", "https://www.sec.gov/Archives/edgar/data/1041379/000119312516428000/d118371dex991.htm", "SEC / AFC Enterprises", "2016", "2015 adjusted EPS 약 $1.89~1.91 검증."),
        S("RBI acquisition announcement", "https://www.sec.gov/Archives/edgar/data/1041379/000119312517050863/d332271dex991.htm", "SEC / RBI", "2017-02-21", "$79 cash/share, $1.8bn 거래 검증."),
        S("RBI acquisition completion", "https://www.sec.gov/Archives/edgar/data/1041379/000119312517097222/d269346d8k.htm", "SEC / AFC Enterprises", "2017-03-27", "합병 종결과 common terminal payoff 검증."),
    ],
}

GROUP_SOURCES = SOURCES
IDEAS = []


def add(**kwargs):
    IDEAS.append(kwargs)


def sc(business, valuation, catalyst, security, timing):
    return [("Business thesis", business), ("Valuation thesis", valuation), ("Catalyst thesis", catalyst), ("Security payoff", security), ("Timing / path", timing)]


def lessons(group):
    return {
        "aezs": ["biotech option basket은 프로그램별 clinical·regulatory·financing 확률을 독립적으로 둔다.", "trial headline miss와 FDA 결론을 같은 사건으로 취급하지 않는다.", "EV≈0도 burn·희석을 빼면 공짜가 아닐 수 있다.", "승인 뒤 실제 license economics까지 common value로 연결한다."],
        "astoria": ["thrift는 liability saving보다 asset/liability repricing gap을 먼저 모델링한다.", "premium amortization·loan growth·buyback을 독립 EPS 항목처럼 단순 합산하지 않는다.", "Street EPS 차이는 NIM bridge로 설명한다.", "M&A optionality는 원 horizon earnings thesis와 분리한다."],
        "alarmforce": ["subscriber economics는 지역·channel별 CAC와 churn cohort로 검증한다.", "좋은 recurring franchise와 공격적 subscriber forecast를 분리한다.", "founder removal은 운영개선의 보증이 아니라 governance catalyst다.", "전략적 takeout은 customer base 가치의 별도 실현경로다."],
        "allmerica": ["복합보험사는 좋은 P&C와 위험한 life stub을 별도 waterfall로 평가한다.", "negative stub은 책임을 계약으로 이전할 때만 해소된다.", "SOTP는 holding debt와 retained guarantee를 차감한다.", "entity rename 뒤 가격을 이어 붙일 때 corporate-action continuity를 확인한다."],
        "allied_note": ["distressed debt는 issuer 이름보다 exact security·seniority·par를 먼저 고정한다.", "35 cents와 $8.75를 혼용하지 말고 $25 par 단위를 명시한다.", "principal gain과 coupons를 분리하고 ledger 없이 IRR을 만들지 않는다.", "M&A debt assumption은 duration risk를 바꾸는 핵심 event다."],
        "afce": ["asset sale은 net proceeds와 실제 distribution으로 검증한다.", "turnaround의 방향 적중과 목표연도 적중은 별도 판정한다.", "asset-light franchisor는 SSS·unit growth·royalty·buyback을 주당 EPS로 잇는다.", "후기 takeout은 장기 quality를 검증하지만 과거 단기 horizon을 구제하지 않는다."],
    }[group]


def checklist(group):
    return {
        "aezs": ["program별 endpoint", "FDA meeting/minutes", "cash runway", "quarterly burn", "FDSO", "license upfront·royalty", "patent life"],
        "astoria": ["asset repricing buckets", "deposit beta", "wholesale funding", "prepayment speed", "premium amortization", "NIM/NII", "operating EPS"],
        "alarmforce": ["regional net adds", "CAC", "churn", "ARPU", "cohort payback", "FCF/share", "strategic-buyer synergies"],
        "allmerica": ["P&C combined ratio", "life reserve stress", "coinsurance counterparty", "retained liabilities", "holding debt", "statutory capital", "SOTP/share"],
        "allied_note": ["CUSIP/security terms", "asset coverage", "nonaccruals", "senior claims", "liquidity", "coupon ledger", "call/redemption price"],
        "afce": ["SSS", "net openings", "franchisee cash returns", "royalty growth", "G&A", "adjusted EPS", "FCF/share", "buyback leverage"],
    }[group]


def claim(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson):
    return C(title, verdict, original, mechanism, evidence, assumption, falsifier, actual, gap, error, lesson)


add(
    id="6ef9e50a-07f4-4dc1-860d-83a0d40e14dd", date="2016-07-25", author="styx1003", ticker="AEZS", company="Aeterna Zentaris Inc.", filename="analysis/ideas/2016/2016-07-25_AEZS_long.md", source="", group="aezs", direction="Long", raw_direction="Long", security="Aeterna Zentaris common equity / Long", entry="market cap 약 $33m, 원문상 EV≈0", horizon="2017 두 Phase III·FDA outcome", raw_horizon="Macrilen·Zoptrex 두 독립 late-stage options",
    title="cash-backed biotech option-basket Long", verdict="혼합 — Zoptrex 실패, Macrilen 승인·license 성공", score=6.5, process=7.5,
    conclusion="두 자산이 모두 성공하지는 않았다. Zoptrex는 OS 10.9개월 대 10.8개월로 Phase III endpoint를 놓쳐 중단됐지만, Macrilen은 confirmatory headline miss 뒤에도 2017-12-20 FDA 승인을 얻고 2018년 $24m upfront와 royalty로 license됐다. option basket 논리는 부분 성공이다.",
    t0="약 $33m market cap와 EV≈0에서 cash runway가 common downside를 받치고 Macrilen·Zoptrex 두 late-stage program 중 하나만 성공해도 upside가 크다는 논지였다.", reverse="시장은 작은 cash buffer가 임상 지연·추가시험·희석으로 빠르게 사라질 수 있고 두 자산의 확률·상업가치가 모두 낮을 가능성을 반영했다.",
    valuation="현금을 floor로 놓고 두 program의 risk-adjusted NPV를 더하는 방식이다. 다만 burn·희석을 현금에서 먼저 빼고, 승인확률과 승인 뒤 license economics를 별도 단계로 둬야 한다.",
    actual="2017-01 Macrilen confirmatory study는 objective를 충족하지 못했지만 FDA 재검토 경로가 이어졌고 2017-12-20 승인됐다. Zoptrex는 2017-05 Phase III OS endpoint 실패로 추가개발이 중단됐다. 2018 Strongbridge license는 $24m upfront, net sales $75m 이하 15%·초과 18% royalty와 milestone을 포함했다.",
    price="원 SQL performance row가 없고 reverse split·financing ledger도 복원되지 않아 exact common return은 주장하지 않는다. 승인·license의 실제 경제조건으로 thesis를 판정한다.",
    drivers="가치는 두 trial의 단순 승패가 아니라 Macrilen의 regulatory salvage와 license monetization에서 나왔다. Zoptrex의 실패는 basket downside를 현실화했다.",
    counterfactual="Zoptrex를 0, Macrilen 승인확률을 절반, 18개월 burn·희석을 차감해도 $33m market cap에 margin of safety가 있었는가?", error="EV≈0를 정적 floor처럼 취급하고 clinical miss·FDA 재평가·commercial license의 서로 다른 확률단계를 충분히 분리하지 않았다.", warning="2017-01 Macrilen confirmatory objective miss가 첫 경고였고 2017-05 Zoptrex 실패가 basket 절반의 terminal break였다.", first_signal_date="2017-01-04", lessons=lessons("aezs"), checklist=checklist("aezs"), scorecard=sc("한 자산 생존", "현금 floor 제한", "Macrilen 성공·Zoptrex 실패", "common 희석경로 불확정", "2017 혼합"),
    scenarios=[("Bear", "두 자산 실패·burn 지속", "cash 소진·희석", "Zoptrex만 현실화"), ("Base", "두 자산 중 하나 승인", "license value", "Macrilen 실현"), ("Bull", "두 자산 승인", "두 franchise 가치", "미실현")],
    metrics=[("T0 market cap", "약 $33m", "EV≈0 downside", "burn·희석으로 이동", "정적 floor 아님"), ("Zoptrex OS", "유의한 개선", "Phase III 성공", "10.9m vs 10.8m", "실패"), ("Macrilen FDA", "승인 option", "positive outcome", "2017-12-20 승인", "성공"), ("License upfront", "미정", "monetization", "$24m", "성공"), ("Royalty", "승인 뒤 가치", "상업 upside", "15%/18% tier", "성공")],
    timeline=[("2016-07-25", "VIC Long", "EV≈0 option basket"), ("2017-01", "Macrilen study objective miss", "첫 경고"), ("2017-05-01", "Zoptrex Phase III 실패", "program 0 처리"), ("2017-H2", "Macrilen FDA 재검토", "regulatory salvage"), ("2017-12-20", "Macrilen FDA 승인", "핵심 성공"), ("2018-01-16", "Strongbridge license", "$24m upfront"), ("2018", "royalty terms 발효", "commercial payoff"), ("후속", "두 program 분리 판정", "basket 혼합")],
    claims=[
        claim("EV≈0 downside", "제한적", "현금이 시가총액을 받쳐 common downside가 작다.", "net cash가 개발가치를 공짜로 만든다.", "원문 cash·market cap 비교.", "burn·restricted cash·희석이 작다.", "12개월 내 대규모 조달이면 반증.", "임상·규제 기간 동안 cash와 share count가 변했다.", "exact net-cash floor 미복원.", "headline cash를 고정값으로 봄.", "현금에서 runway와 dilution을 먼저 뺀다."),
        claim("두 독립 options", "부분 성공", "Macrilen·Zoptrex 중 하나만 성공해도 된다.", "낮은 상관의 binary payoff를 합산한다.", "서로 다른 적응증·시험.", "failure modes와 자금수요가 독립적이다.", "둘 다 실패하거나 financing이 payoff를 흡수하면 반증.", "Macrilen 승인, Zoptrex 실패.", "1승 1패.", "공통 cash runway 상관을 축소.", "program PoS와 shared financing을 함께 본다."),
        claim("Zoptrex Phase III", "강한 실패", "OS 개선으로 승인경로를 연다.", "positive pivotal endpoint가 신청가치를 만든다.", "late-stage trial.", "임상효과가 control 대비 유의하다.", "OS 차이가 미미하면 반증.", "OS 10.9m vs 10.8m, 추가개발 중단.", "약 +0.1개월.", "binary success probability 과대.", "endpoint 숫자와 중단결정을 terminal 처리한다."),
        claim("Macrilen confirmatory trial", "headline 실패", "confirmatory study가 objective를 충족한다.", "재현된 진단성능이 FDA 승인을 지지한다.", "기존 data와 unmet need.", "사전 objective 충족.", "objective miss면 claim 반증.", "2017-01 objective miss.", "사전 claim 실패.", "trial과 regulation을 한 claim으로 묶음.", "clinical claim은 즉시 실패 판정한다."),
        claim("Macrilen FDA approval", "강한 성공", "Macrilen이 규제자산이 된다.", "FDA 승인이 상업화·license를 가능하게 한다.", "재검토 가능성.", "FDA가 전체 evidence를 수용한다.", "CRL/추가 대형시험이면 반증.", "2017-12-20 승인.", "승인 실현.", "headline miss 뒤 확률 update 부족.", "FDA 경로를 trial outcome과 별도 추적한다."),
        claim("승인 뒤 monetization", "성공", "승인자산이 common value로 전환된다.", "upfront·royalty가 cash를 만든다.", "파트너링 가능성.", "경제적인 license terms.", "무상·저가 license면 반증.", "$24m upfront, 15%/18% royalty.", "T0 market cap 대비 upfront 약 73%.", "milestone probability는 미확정.", "계약 cash와 contingent value를 분리한다."),
    ],
)


add(
    id="17b17e74-47df-4240-97cc-e7f5cb8c560e", date="2004-01-09", author="evan73", ticker="AF", company="Astoria Financial Corporation", filename="analysis/ideas/2004/2004-01-09_AF_astoria_long.md", source="", group="astoria", direction="Long", raw_direction="Short", security="Astoria Financial common equity / Long", entry="2004-01 AF common", horizon="FY2004 earnings", raw_horizon="LTM EPS $2.59→2004E $3.57; target $43~57",
    title="liability-refinancing·NIM recovery Long", verdict="실패 — additive EPS bridge 과대", score=3.8, process=5.5,
    conclusion="raw Short와 current-company mapping은 모두 틀렸다. 원문은 Astoria Long이지만 2004E EPS $3.57 대비 실제 operating diluted EPS $2.09로 41.5% 미달했고 2005도 $2.26에 그쳤다. refinancing savings를 prepayment·asset-yield 변화와 독립적으로 더한 것이 핵심 오류다.",
    t0="LTM EPS $2.59, NIM 약 2.40%에서 $7.7bn liabilities의 낮은 금리 refinancing, premium amortization 정상화, loan growth와 buyback이 2004 EPS를 $3.57로 높인다고 봤다.", reverse="시장은 저금리 refinancing 이익이 asset yield 하락, mortgage prepayment와 deposit competition으로 상쇄되고 thrift의 convexity가 나빠질 가능성을 가격에 넣었다.",
    valuation="원문은 refinancing +$0.51, premium amortization +$0.45, loan growth +$0.32, buyback +$0.08을 더해 EPS를 만들고 $43~57 target를 제시했다. 상호의존 변수를 단순 합산한 bridge였다.",
    actual="2004 operating diluted EPS는 $2.09, 2005 diluted EPS는 $2.26이었다. repurchase는 진행됐지만 NIM·asset yield와 mortgage dynamics가 refinancing benefit을 흡수했다. 2017 Sterling merger는 원 horizon과 13년 떨어진 별도 사건이다.",
    price="performance row가 없어 exact return이나 target hit를 만들지 않는다. 2004 earnings denominator와 공시 결과로 판정한다.",
    drivers="earnings miss는 funding cost 한 항목이 아니라 asset yield·prepayment·deposit beta가 같은 방향으로 움직이지 않은 데서 왔다.",
    counterfactual="refinancing 절감액을 절반만 반영하고 asset yield -25bp·prepayment stress를 넣어도 $3.57 EPS가 가능한가?", error="서로 상관된 네 EPS lever를 선형 합산하고 balance-sheet repricing을 총액이 아닌 속도 문제로 보지 않았다.", warning="FY2004 operating EPS $2.09가 예상 $3.57에 크게 미달한 시점이 명확한 first break였다.", first_signal_date="2005-01-31", lessons=lessons("astoria"), checklist=checklist("astoria"), scorecard=sc("franchise 생존", "denominator 실패", "refi 일부", "common 방향 교정", "FY2004 실패"),
    scenarios=[("Bear", "asset yield 하락·prepayment 지속", "EPS ~$2", "현실화"), ("Base", "네 lever 일부 상쇄", "EPS $2.5~3", "상단 미달"), ("Bull", "모든 lever 합산", "EPS $3.57/$43~57", "실패")],
    metrics=[("LTM EPS", "$2.59", "상승 출발점", "FY2004 $2.09", "하락"), ("2004 EPS", "$3.57E", "$3.57", "$2.09 operating", "-41.5%"), ("2005 EPS", "회복 지속", ">$3", "$2.26", "미달"), ("Liabilities", "$7.7bn", "refinancing benefit", "부분 상쇄", "과대"), ("Target", "$43~57", "FY2004 rerating", "return ledger 없음", "미검증")],
    timeline=[("2004-01-09", "VIC Long", "raw Short 교정"), ("2004-H1", "liability refinancing", "funding benefit"), ("2004-H2", "asset yield pressure", "상쇄효과"), ("FY2004", "operating EPS $2.09", "핵심 실패"), ("FY2005", "EPS $2.26", "회복 미달"), ("2005", "6.6m shares repurchased", "buyback claim 성공"), ("2006-07", "추가 authorization", "capital return 지속"), ("2017", "Sterling merger", "원 horizon 밖")],
    claims=[
        claim("FHLB refinancing +$0.40", "부분 성공", "$5bn refinancing이 EPS $0.40를 더한다.", "funding coupon 하락이 NII를 높인다.", "$5bn maturity opportunity.", "asset yield가 유지된다.", "NIM·EPS가 하락하면 과대.", "EPS는 $2.09로 하락.", "net +$0.40 미확인.", "gross saving만 계산.", "asset-side offset을 동시에 넣는다."),
        claim("CD refinancing +$0.11", "부분 성공", "$2.7bn CDs 재가격으로 EPS $0.11.", "deposit cost 하락.", "high-cost CD book.", "deposit mix·balance 유지.", "deposit competition이 saving을 지우면 반증.", "총 EPS bridge는 실패.", "+$0.11 분리 검증 불가.", "funding 항목을 독립시킴.", "deposit beta와 runoff를 모델링한다."),
        claim("premium amortization +$0.45", "실패", "prepayment 정상화로 EPS $0.45 회복.", "premium write-off 감소.", "refi wave 완화 기대.", "mortgage speed가 빠르게 정상화.", "amortization·yield 압박 지속이면 반증.", "2004 EPS가 출발점보다 낮음.", "예상 회복 미실현.", "convexity를 선형화.", "rate scenarios별 CPR과 yield를 잇는다."),
        claim("loan growth +$0.32", "미달", "loan growth가 EPS $0.32.", "earning asset 확대.", "지역 franchise.", "incremental spread가 양수.", "성장해도 NIM 하락이면 반증.", "$3.57 bridge를 채우지 못함.", "+$0.32 효과 미실현.", "volume과 spread 혼동.", "growth는 marginal NIM으로 계산한다."),
        claim("buyback +$0.08", "방향 성공", "repurchase가 EPS/share를 높인다.", "share count 감소.", "capital availability.", "내재가치 이하 매입.", "고가 매입·capital pressure면 반증.", "2005 6.6m주 repurchase.", "행동은 실현·총 EPS는 미달.", "EPS accretion을 영업개선과 혼용.", "share count bridge를 별도 둔다."),
        claim("2004 EPS $3.57·$43~57", "강한 실패", "EPS 급증과 rerating.", "네 lever 합산×multiple.", "LTM $2.59.", "상쇄가 작다.", "EPS <$2.7이면 반증.", "operating EPS $2.09.", "-$1.48/-41.5%.", "상관·denominator 오류.", "target보다 earnings bridge를 먼저 stress한다."),
    ],
)


add(
    id="d8c623a0-24c6-48f4-b5a2-b6b44560b27b", date="2006-09-18", author="skyhawk887", ticker="AF", company="Astoria Financial Corporation", filename="analysis/ideas/2006/2006-09-18_AF_astoria_short.md", source="", group="astoria", direction="Short", raw_direction="Short", security="Astoria Financial common equity / Short", entry="2006-09 AF short", horizon="FY2007", raw_horizon="Street 2007 EPS ~$1.94 vs own ~$1.35; target 2005 low ~$24.43",
    title="inverted-curve NIM-compression Short", verdict="성공 — NIM·NII·EPS 압박 적중", score=8.2, process=8.5,
    conclusion="회사 mapping만 교정하면 raw Short는 맞다. 2007 operating EPS $1.50은 자체 $1.35보다 11.1% 높았지만 Street $1.94보다 22.7% 낮았고, NIM은 1.87%에서 1.62%, NII는 $390.4m에서 $333.5m로 감소했다. short의 핵심 spread mechanism이 실현됐다.",
    t0="inverted curve에서 wholesale·deposit liabilities가 asset보다 빠르게 재가격되며 Street 2007 EPS 약 $1.94가 과대이고 자체 추정 $1.35가 현실적이라는 논지였다.", reverse="시장은 curve 정상화, deposit repricing relief와 asset growth가 spread를 회복시키거나 낮은 valuation이 downside를 제한할 가능성을 반영했다.",
    valuation="earnings miss와 2005 저점 약 $24.43 재방문을 연결했다. short valuation은 price target보다 NIM·NII·EPS의 동시 하향으로 검증하는 편이 안전하다.",
    actual="FY2007 NIM 1.62% 대 1.87%, NII $333.5m 대 $390.4m, operating EPS $1.50, GAAP EPS $1.36이었다. own EPS는 다소 보수적이었지만 Street miss 방향과 메커니즘은 맞았다.",
    price="검증된 entry·borrow·cover ledger가 없어 exact short return은 보류한다. fundamental short outcome은 2007 공시수치로 판정한다.",
    drivers="asset/liability duration mismatch가 funding cost를 더 빨리 올려 NIM과 NII를 눌렀고 Street denominator가 하향됐다.",
    counterfactual="curve가 6개월 안에 정상화되고 deposits가 즉시 낮은 금리로 재가격돼도 EPS $1.94가 가능한가?", error="방향은 맞았으나 $1.35 EPS와 특정 price target를 정밀값처럼 둔 점, short squeeze·borrow·dividend cost를 덜 모델링했다.", warning="2007 중간결과에서 NIM과 NII가 동시에 전년 대비 하락한 것이 조기 확인 신호였다.", first_signal_date="2007-06-30", lessons=lessons("astoria"), checklist=checklist("astoria"), scorecard=sc("spread 압박", "earnings miss 성공", "curve catalyst 성공", "short costs 미복원", "FY2007 성공"),
    scenarios=[("Bear for short", "curve 정상화·deposit relief", "EPS ~$1.94", "미발생"), ("Base", "NIM 압박", "EPS ~$1.50", "실현"), ("Bull for short", "severe compression", "EPS ~$1.35/$24.43", "EPS 근접")],
    metrics=[("Operating EPS", "Street ~$1.94", "own ~$1.35", "$1.50", "short 성공"), ("GAAP EPS", "Street ~$1.94", "하향", "$1.36", "강한 miss"), ("NIM", "1.87% prior", "압축", "1.62%", "-25bp"), ("NII", "$390.4m prior", "감소", "$333.5m", "-14.6%"), ("Price target", "~$24.43", "2005 low retest", "ledger 없음", "미검증")],
    timeline=[("2006-09-18", "VIC Short", "funding spread thesis"), ("2006-H2", "curve inversion 지속", "liability pressure"), ("2007-Q1", "NIM 하락", "초기 확인"), ("2007-Q2", "NIM·NII 동반감소", "first signal"), ("2007-H2", "earnings revisions", "Street gap 축소"), ("FY2007", "operating EPS $1.50", "short 성공"), ("FY2007", "GAAP EPS $1.36", "own estimate 근접"), ("2008-01-24", "연간결과 공시", "검증 완료")],
    claims=[
        claim("Street EPS ~$1.94 과대", "성공", "2007 consensus가 높다.", "NIM compression이 earnings를 낮춘다.", "repricing mismatch.", "curve inversion 지속.", "EPS가 $1.85 이상이면 반증.", "operating EPS $1.50.", "Street 대비 -22.7%.", "none material.", "consensus gap을 NIM bridge로 설명한다."),
        claim("own EPS ~$1.35", "근접", "2007 EPS가 약 $1.35.", "spread 압박의 bottom-up estimate.", "funding mix.", "credit·opex 안정.", "$1.70 이상이면 과도한 bearish.", "operating $1.50, GAAP $1.36.", "operating +11.1%; GAAP 근접.", "EPS 정의 혼용 위험.", "operating/GAAP를 사전 고정한다."),
        claim("NIM compression", "강한 성공", "NIM이 의미 있게 하락.", "liabilities가 assets보다 빨리 재가격.", "inverted curve.", "deposit beta가 높다.", "NIM 안정/상승이면 반증.", "1.87%→1.62%.", "-25bp/-13.4%.", "none material.", "repricing table이 short의 중심이다."),
        claim("NII decline", "강한 성공", "balance growth로도 NII 감소를 못 막는다.", "spread loss가 volume을 압도.", "low NIM.", "asset growth 제한.", "NII 증가면 반증.", "$390.4m→$333.5m.", "-$56.9m/-14.6%.", "none material.", "NIM과 dollars NII를 함께 본다."),
        claim("2005 low retest", "미검증", "주가가 약 $24.43으로 하락.", "earnings revision과 de-rating.", "historical support.", "multiple이 유지된다.", "earnings miss에도 price 견조면 실패.", "verified price ledger 없음.", "정확한 hit 불명.", "fundamental과 price claim 혼용.", "가격은 별도 source로 검증한다."),
        claim("short payoff", "fundamental 성공", "common short가 수익을 낸다.", "EPS miss가 price에 반영.", "Street gap.", "borrow·dividend·timing 감당.", "borrow recall/price rally면 손실.", "business mechanism 적중.", "exact net return 없음.", "implementation cost 누락.", "short는 borrow와 cover rule까지 기록한다."),
    ],
)


add(
    id="27a297bf-be6c-497e-b08a-3a07677ee599", date="2009-11-08", author="hb190", ticker="AF", company="AlarmForce Industries Inc.", filename="analysis/ideas/2009/2009-11-08_AF_alarmforce_long.md", source="", group="alarmforce", direction="Long", raw_direction="Long", security="AlarmForce common equity / Long", entry="2009 AF common; 약 100k subscribers", horizon="3~5년", raw_horizon="200~250k subscribers, 26% new-customer IRR, steady-state EV/EBITDA 3.2x",
    title="subscription unit-economics·geographic expansion Long", verdict="부분 성공 — recurring franchise 성공, growth 과대", score=6.5, process=7.2,
    conclusion="SAC 약 $662, after-tax 신규고객 IRR 26%, gross margin 78%라는 recurring economics는 가치 있는 franchise를 포착했다. 그러나 subscribers는 2010 113.5k, 2015 144.2k로 200~250k 목표에 크게 못 미쳤다. 2018 BCE C$16 takeout은 strategic value를 검증하지만 원 3~5년 growth forecast를 구제하지 않는다.",
    t0="약 100k subscribers에서 낮은 churn과 월 $25+ recurring fee, SAC 회수 economics를 미국 확장에 재투자하면 3~5년 200~250k subscribers가 가능하다는 논지였다.", reverse="시장은 지역별 브랜드·광고효율, 설치 economics와 incumbent competition 때문에 기존 market의 CAC·churn을 새 지역에 복제하기 어렵다고 봤다.",
    valuation="원문은 steady-state EV/EBITDA 약 3.2x와 customer IRR 26%를 저평가 근거로 삼았다. growth capex를 비용처리하더라도 cohort economics가 재현돼야 multiple이 싸다.",
    actual="FY2010 subscribers는 113.5k, FY2015는 144.2k였다. recurring customer base는 남았지만 200~250k expansion은 미달했다. BCE는 2018-01 C$16/share 현금으로 인수를 완료했다.",
    price="T0 share price와 배당 ledger가 완전하지 않아 exact return은 보류한다. subscriber forecast와 terminal C$16 takeout을 별도 판정한다.",
    drivers="운영 가치는 sticky monthly revenue가 만들었지만 성장속도는 geographic CAC의 불리한 재현성 때문에 낮아졌다. 최종 payoff는 strategic buyer가 customer base와 bundling synergy를 평가해 만들었다.",
    counterfactual="새 지역 SAC가 50% 높고 churn이 2ppt 높아도 신규고객 IRR이 hurdle을 넘고 200k subscribers에 도달하는가?", error="기존 cohort economics를 다른 지역에 일정하게 적용하고 subscriber count가 두 배가 될 때 필요한 CAC·설치자본을 과소평가했다.", warning="2010 113.5k의 성장속도가 200~250k 목표에 필요한 run-rate에 못 미친 것이 첫 경고였다.", first_signal_date="2010-10-31", lessons=lessons("alarmforce"), checklist=checklist("alarmforce"), scorecard=sc("franchise 성공", "growth denominator 과대", "takeout 장기 성공", "common 적절", "3~5년 미달"),
    scenarios=[("Bear", "CAC 상승·churn 악화", "성장정체", "부분 현실화"), ("Base", "지속 net adds", "200k 접근", "144.2k에 그침"), ("Bull", "미국 확장", "250k+·rerating", "실패")],
    metrics=[("Subscribers T0", "약 100k", "200~250k", "2015 144.2k", "42~58% 미달"), ("FY2010 subscribers", "약 100k", "고성장", "113.5k", "초기 미달"), ("SAC", "~$662", "stable", "지역별 불확실", "복제 미확인"), ("Gross margin", "~78%", "유지", "recurring model 지속", "방향 성공"), ("Terminal", "성장 rerating", "전략가치", "BCE C$16", "장기 성공")],
    timeline=[("2009-11-08", "VIC Long", "unit economics thesis"), ("2010", "113.5k subscribers", "성장속도 경고"), ("2011", "미국확장", "CAC test"), ("2013", "subscriber growth 둔화", "target risk"), ("2015", "144.2k subscribers", "200k 미달"), ("2017-11-06", "BCE deal 발표", "strategic value"), ("2018-01-05", "C$16 deal 종결", "terminal payoff"), ("후속", "growth와 takeout 분리", "혼합 판정")],
    claims=[
        claim("SAC ~$662", "지역별 미검증", "낮은 SAC로 고객을 확보한다.", "upfront CAC를 recurring margin으로 회수.", "기존 cohort.", "새 지역 CAC도 유사.", "CAC 급등이면 반증.", "성장목표 미달로 복제성 제한.", "정확한 후속 SAC 없음.", "평균을 지역에 외삽.", "channel·region cohort를 분리한다."),
        claim("new-customer IRR 26%", "부분 성공", "신규고객 투자수익이 높다.", "낮은 churn과 높은 gross margin.", "SAC·monthly fee.", "lifetime/churn 안정.", "payback 연장·net adds 둔화면 약화.", "franchise는 유지·성장은 둔화.", "IRR 방향만 지지.", "terminal churn 가정 민감.", "IRR보다 payback·retention curve를 본다."),
        claim("gross margin 78%", "성공", "recurring monitoring이 고마진이다.", "fixed platform에 월 fee가 쌓인다.", "T0 margin.", "service cost 통제.", "margin 급락이면 반증.", "BCE가 recurring base를 인수.", "전략가치 확인.", "gross margin과 FCF 혼동.", "CAC·G&A 뒤 cash를 본다."),
        claim("200~250k subscribers", "실패", "3~5년 subscriber 두 배.", "geographic reinvestment.", "약 100k base.", "net adds 가속.", "2015 <180k면 반증.", "2015 144.2k.", "하단 대비 -55.8k/-27.9%.", "growth extrapolation.", "필요 net adds를 사전 calendar로 둔다."),
        claim("steady-state 3.2x EV/EBITDA", "제한적 성공", "growth spend 정상화 시 매우 싸다.", "CAC 지출 감소가 EBITDA로 전환.", "recurring margin.", "subscriber base 유지.", "churn/decline이면 무효.", "base는 유지되고 takeout 발생.", "정확 multiple 미복원.", "성장비용을 선택재로 봄.", "maintenance acquisition spend를 분리한다."),
        claim("strategic takeout", "장기 성공", "customer base가 인수매력이 있다.", "telco bundle·cross-sell synergy.", "contracted revenue.", "buyer synergy.", "독립가치만 남으면 미실현.", "BCE C$16 acquisition.", "terminal price 확인.", "원 horizon 밖 event.", "later takeout으로 growth miss를 지우지 않는다."),
    ],
)


add(
    id="620d4256-cc74-425b-930d-1850677c90b8", date="2014-03-10", author="thistle933", ticker="AF", company="AlarmForce Industries Inc.", filename="analysis/ideas/2014/2014-03-10_AF_alarmforce_long.md", source="", group="alarmforce", direction="Long", raw_direction="Short", security="AlarmForce common equity / Long", entry="C$10.70", horizon="2~3년 운영개선·전략대안", raw_horizon="142.4k customers, downside FCF/share C$0.58, upside C$1.07",
    title="founder-removal·recurring-FCF special-situation Long", verdict="성공 — C$10.70→C$16 takeout", score=8.5, process=8.2,
    conclusion="raw Short는 실제 Long으로 교정했다. 142.4k customers, 91% recurring revenue와 net cash가 downside를 지지했고 운영성장은 강하지 않았지만 BCE가 C$16 cash로 인수했다. 단순 price comparison은 약 +49.5%이며 배당·세금·정확 IRR은 별도다.",
    t0="founder 제거와 실패한 sale process 뒤 C$10.70에 거래됐다. 142.4k customers, 14% churn, CAC $746, 91% recurring revenue와 net cash를 바탕으로 professionalization과 재매각 optionality를 샀다.", reverse="시장은 높은 churn·CAC, 정체된 subscriber base, governance disruption과 이전 sale 실패가 intrinsic FCF와 strategic value를 훼손할 가능성을 반영했다.",
    valuation="downside FCF/share C$0.58와 upside C$1.07을 두고 cash-flow multiple을 적용했다. sale은 base가 아니라 option이어야 하며 C$10.70이 downside FCF에도 감당 가능한지 봐야 했다.",
    actual="subscriber growth는 크게 가속되지 않았지만 contracted customer base와 recurring revenue가 유지됐다. BCE는 2017-11 C$16 cash acquisition을 발표했고 2018-01-05 종결했다.",
    price="C$16/C$10.70-1≈+49.5%의 단순 corporate-action comparison이다. 보유기간 배당·세금·정확 settlement dates를 넣은 total return/IRR은 주장하지 않는다.",
    drivers="완벽한 operating turnaround보다 recurring cash flow의 보존과 telco buyer의 bundle synergy가 terminal value를 만들었다.",
    counterfactual="sale을 0으로 두고 churn 16%, CAC C$850, FCF/share C$0.58만 적용해도 C$10.70에 충분한 downside protection이 있었는가?", error="운영개선과 재매각 가능성을 함께 base에 넣을 위험이 있었고 customer additions보다 churn·CAC sensitivity를 더 강하게 봤어야 했다.", warning="subscriber growth 정체가 운영 bull case의 첫 경고였지만 recurring base·cash flow가 무너지지 않아 전체 thesis break는 아니었다.", first_signal_date="2015-10-31", lessons=lessons("alarmforce"), checklist=checklist("alarmforce"), scorecard=sc("recurring base 유지", "downside 지지", "takeout 성공", "common 적절", "운영 지연·event 성공"),
    scenarios=[("Bear", "churn↑·CAC↑·sale 없음", "FCF $0.58×저배수", "미발생"), ("Base", "안정 customer base", "운영가치 유지", "대체로 실현"), ("Bull", "professionalization·takeout", "C$16+", "실현")],
    metrics=[("Entry", "C$10.70", "downside 보호", "C$16 consideration", "+49.5% 단순"), ("Customers", "142.4k", "재성장", "대체로 정체", "미달"), ("Churn", "14%", "개선", "구조적 부담 지속", "혼합"), ("CAC", "$746", "효율개선", "성장제약", "미달"), ("Recurring revenue", "91%", "가치보존", "buyer가 인수", "성공")],
    timeline=[("2014-03-10", "VIC Long", "raw Short 교정"), ("2014", "founder 이후 governance", "professionalization"), ("2015", "growth 정체", "운영 bull 경고"), ("2016", "recurring base 유지", "downside 지지"), ("2017-H1", "전략대안", "takeout option"), ("2017-11-06", "BCE C$16 발표", "가치 실현"), ("2018-01-05", "거래 종결", "terminal payoff"), ("후속", "+49.5% 단순 비교", "IRR 과장 방지")],
    claims=[
        claim("raw Short", "metadata 실패", "SQL은 Short다.", "방향 오류는 payoff를 반전시킨다.", "원문 upside·FCF 논리.", "원문 읽기.", "하락 베팅이면 Short.", "실제는 Long.", "완전 반대.", "metadata 의존.", "원문 payoff를 우선한다."),
        claim("downside FCF $0.58", "방향 성공", "보수적 FCF가 valuation floor다.", "recurring fees가 cash를 만든다.", "91% recurring revenue.", "churn·CAC 안정.", "FCF 붕괴면 반증.", "base 유지 후 takeout.", "정확 FCF bridge 제한.", "reported metric 정의 부족.", "maintenance CAC 뒤 FCF를 쓴다."),
        claim("upside FCF $1.07", "운영 미달", "전문화로 FCF/share가 크게 상승.", "CAC·opex 효율화.", "founder removal.", "subscriber growth 재개.", "성장정체면 미달.", "growth는 강하게 회복하지 않음.", "upside denominator 미확인.", "governance catalyst 과대.", "KPI milestones를 사전 둔다."),
        claim("142.4k customer base", "성공", "sticky customers가 downside를 지지.", "월 반복청구·낮은 service cost.", "contracted base.", "churn 폭증 없음.", "base 급감이면 반증.", "BCE가 base를 인수.", "전략가치 확인.", "고객 수와 quality 혼용 위험.", "cohort churn·ARPU를 추적한다."),
        claim("professionalization", "부분 성공", "founder 제거 뒤 운영개선.", "governance·capital allocation 개선.", "board change.", "management execution.", "CAC/churn 악화면 반증.", "운영 개선은 혼합.", "성장 bull 미실현.", "사람 교체를 결과로 봄.", "운영 KPI가 확인될 때만 credit한다."),
        claim("sale optionality", "강한 성공", "전략적 buyer가 premium을 지불.", "telco synergy+recurring base.", "이전 sale interest.", "asset remains attractive.", "장기 독립·저가 거래면 실패.", "BCE C$16 cash.", "entry 대비 +49.5% 단순.", "매각을 base에 넣을 위험.", "standalone downside와 option을 분리한다."),
    ],
)


add(
    id="98bd14c6-2b9b-45b7-97cd-a612f297efff", date="2002-10-04", author="pomfret626", ticker="AFC", company="Allmerica Financial Corporation", filename="analysis/ideas/2002/2002-10-04_AFC_allmerica_long.md", source="", group="allmerica", direction="Long", raw_direction="Short", security="Allmerica Financial common equity / Long", entry="약 $10", horizon="12~24개월 life restructuring", raw_horizon="P&C ~$20/share + life conservative $3; target $23",
    title="negative-life-stub SOTP Long", verdict="매우 강한 성공 — life uncertainty 해소·P&C rerating", score=9.0, process=8.8,
    conclusion="raw Short와 SQL의 Allied Capital mapping을 모두 교정했다. 약 $10에서 P&C ~$20와 life $3의 SOTP를 샀고 life blocks가 coinsurance·매각되며 negative stub이 해소됐다. 주가는 2004-02 $37.16까지 상승했고 2005 The Hanover로 사명을 바꿨다.",
    t0="시장은 P&C franchise 가치보다 life·annuity reserve와 capital risk를 더 큰 음수로 가격에 반영했다. 원문은 conservative life value $3을 둬도 P&C 약 $20과 합쳐 $23이 된다고 봤다.", reverse="life guarantees와 statutory capital의 tail loss, holding-company liquidity, reserve uncertainty가 P&C 가치까지 흡수할 가능성이 있었다.",
    valuation="P&C $20/share + life $3/share = $23 target의 two-part SOTP다. 핵심은 life gross assets가 아니라 retained guarantees와 transaction 뒤 common에 남는 순가치다.",
    actual="Allmerica는 life blocks를 coinsure·매각하고 P&C 중심으로 재편했다. uncertainty discount가 줄며 2004-02 주가 $37.16이 관찰됐고 2005 The Hanover Insurance Group으로 사명을 변경했다.",
    price="$10 entry와 2004-02 $37.16 관찰값의 단순 magnitude는 약 +271.6%다. exact purchase date, dividends와 realized exit ledger가 없어 IRR·total return으로 표현하지 않는다.",
    drivers="life tail risk를 계약으로 이전하면서 시장이 음수로 보던 stub이 제거되고 P&C earnings·capital이 독립적으로 평가됐다.",
    counterfactual="life block을 $0이 아니라 -$10/share로 두고 retained guarantee·holding debt를 stress해도 $10 entry가 P&C value로 보호됐는가?", error="결론은 강했지만 life $3 가치를 정밀하게 두기보다 negative tail distribution과 counterparty/retained-liability를 더 넓게 stress했어야 한다.", warning="coinsurance가 holding company에 material guarantee를 남기거나 statutory capital이 더 악화되면 반증이었으나 실제 restructuring이 진행됐다.", first_signal_date="2003-12-31", lessons=lessons("allmerica"), checklist=checklist("allmerica"), scorecard=sc("P&C 가치 확인", "SOTP 상회", "life restructuring 성공", "common 적절", "2년 내 강한 성공"),
    scenarios=[("Bear", "life tail -$10+/share", "P&C 가치 흡수", "미발생"), ("Base", "P&C $20+life $3", "$23", "상회"), ("Bull", "life risk 제거·P&C rerating", "$30+", "$37.16 관찰")],
    metrics=[("Entry", "~$10", "$23 target", "$37.16 Feb-2004", "강한 상회"), ("P&C value", "~$20/share", "보존", "focused franchise", "성공"), ("Life value", "$3 conservative", "0 이상", "blocks transferred/sold", "성공"), ("Simple magnitude", "$10→$37.16", "rerating", "+271.6% peak comparison", "실현률 아님"), ("Identity", "AFC", "Allmerica", "2005 Hanover rename", "교정")],
    timeline=[("2002-10-04", "VIC Long", "raw Short 교정"), ("2002-Q4", "life risk discount", "negative stub"), ("2003-H1", "restructuring 진전", "tail 축소"), ("2003-H2", "life blocks transaction", "P&C 분리"), ("2003-12-31", "focus 확인", "first positive signal"), ("2004-02", "stock $37.16", "target 상회"), ("2005", "The Hanover rename", "entity continuity"), ("후속", "P&C 중심 운영", "SOTP 실현")],
    claims=[
        claim("P&C ~$20/share", "강한 성공", "P&C franchise가 주당 약 $20 가치.", "underwriting·float를 독립 평가.", "standalone comparables.", "reserve quality 유지.", "P&C deterioration이면 반증.", "restructuring 뒤 P&C 중심 가치가 부각.", "$20 floor 상회.", "reserve stress 제한.", "combined ratio·reserve development로 검증한다."),
        claim("life value $3/share", "방향 성공", "life를 보수적으로도 양수 평가.", "coinsurance·sale로 value 회수.", "book assets와 contracts.", "retained liabilities 제한.", "추가 capital call이면 반증.", "blocks가 이전·매각됨.", "negative stub 해소.", "정밀 $3은 미검증.", "point estimate보다 range를 쓴다."),
        claim("market implies negative stub", "강한 성공", "$10 price가 life를 큰 음수로 본다.", "P&C $20 대비 discount.", "SOTP gap.", "P&C estimate 유효.", "P&C도 과대면 반증.", "$37.16로 rerating.", "discount closure 큼.", "두 사업 risk 상관 가능.", "implied stub을 역산한다."),
        claim("life restructuring", "강한 성공", "coinsurance·sale가 uncertainty를 제거.", "tail risk·capital need transfer.", "strategic process.", "counterparty와 terms 확정.", "거래 실패·guarantee 잔존이면 반증.", "transactions 진행.", "catalyst 실현.", "headline sale만 볼 위험.", "retained obligations를 확인한다."),
        claim("$23 target", "강한 성공", "SOTP가 $23으로 수렴.", "negative stub 제거.", "$20+$3.", "multiple·execution 안정.", "2년 내 $15 미만이면 실패.", "2004-02 $37.16.", "+$14.16 vs target.", "peak price는 exit 보장 아님.", "target hit와 realized return을 분리한다."),
        claim("entity/direction", "metadata 실패", "SQL Short·Allied mapping.", "wrong entity는 모든 가격·fundamental을 오염.", "원문 life/P&C 서술.", "historical identity 확인.", "Allied debt 내용이면 기존 mapping.", "Allmerica common Long.", "법인·방향 모두 교정.", "ticker-only join.", "date+legal entity+security를 key로 쓴다."),
    ],
)


add(
    id="bfc22ed5-176c-4033-add8-942cf13274e2", date="2008-12-29", author="doggy835", ticker="AFC", company="Allied Capital Corporation", filename="analysis/ideas/2008/2008-12-29_AFC_allied_capital_2047_notes_long.md", source="", group="allied_note", direction="Long", raw_direction="Long", security="6.875% senior unsecured notes due 2047 / Long", entry="약 35~36 cents on par; $25 par 기준 약 $8.75~9.00", horizon="credit normalization·change of control", raw_horizon="credit-crunch easing, issuer buyback/equity raise; par recovery",
    title="distressed senior-note coverage Long", verdict="매우 강한 성공 — Ares assumption 후 par redemption", score=9.5, process=9.2,
    conclusion="common이 아닌 6.875% senior unsecured notes due 2047이다. 약 $8.75~9.00에 산 $25 par claim은 2010 Ares가 인수하며 assumption됐고 2021 $25 par+accrued interest로 상환됐다. principal-only 단순 gain은 약 +178%이며 coupons와 exact IRR은 ledger 없이 만들지 않는다.",
    t0="GFC 중 Allied portfolio와 liquidity 불신으로 장기 senior note가 par의 35~36%에 거래됐다. 원문은 asset coverage와 credit-market 정상화, issuer action이 default보다 높은 recovery를 만든다고 봤다.", reverse="NAV write-down, nonaccrual, leverage와 refinancing failure가 unsecured claim의 recovery를 par 아래로 낮출 수 있었다. 2047 maturity는 catalyst가 없으면 duration risk가 매우 컸다.",
    valuation="$25 par claim을 약 $8.75~9.00에 매입했다. payoff는 coupon+principal이고, common upside가 아니라 senior/secured claims 뒤 realizable asset coverage와 issuer liquidity가 결정한다.",
    actual="Ares Capital은 2010-04-01 Allied acquisition을 완료하며 notes를 assumed했다. 2021-03 잔여 약 $229.56m를 $25 par와 accrued interest에 redeem했다.",
    price="$9 기준 $25/$9-1≈+177.8% principal-only 단순 gain이다. 2009~2021 coupon 지급일·세금·reinvestment가 완전하지 않아 total return과 annualized IRR은 보류한다.",
    drivers="deep discount, seniority와 change-of-control assumption이 default tail과 매우 긴 maturity를 줄였고 최종 call이 par를 현금화했다.",
    counterfactual="portfolio를 40% haircut하고 secured debt·fees를 먼저 빼도 unsecured notes가 최소 80 cents recovery를 얻는가?", error="원문 catalyst 중 issuer buyback·equity raise보다 실제 핵심은 Ares assumption이었다. 2047 duration과 coupon settlement를 더 명시적으로 시나리오화할 필요가 있었다.", warning="Ares가 notes를 assume하지 않거나 coverage가 1x 아래로 내려가면 thesis break였지만 2010 assumption이 반대로 위험을 낮췄다.", first_signal_date="2010-04-01", lessons=lessons("allied_note"), checklist=checklist("allied_note"), scorecard=sc("issuer 정상화", "deep discount 성공", "M&A assumption 성공", "note 선택 우수", "장기 hold·2021 종결"),
    scenarios=[("Bear", "asset haircut·default", "$10 미만 recovery", "미발생"), ("Base", "credit normalize", "$20~25+coupon", "실현"), ("Bull", "M&A assumption·call", "$25+accrued", "실현")],
    metrics=[("Entry", "35~36c/par", "par convergence", "$25 redemption", "강한 성공"), ("Dollar price", "$8.75~9/$25 par", "$25", "$25+accrued", "+~178% principal"), ("Coupon", "6.875%", "지속 지급", "redemption 전 contractual", "ledger 제한"), ("Assumption", "불확실", "credit catalyst", "2010 Ares assumption", "성공"), ("Maturity", "2047", "duration 단축", "2021 redemption", "26년 단축")],
    timeline=[("2008-12-29", "VIC note Long", "35~36c entry"), ("2009", "credit stress 완화", "coverage 개선"), ("2010-04-01", "Ares acquisition", "debt assumption"), ("2010", "coupon continuity", "default tail 감소"), ("2012-04-15", "par call window", "contractual option"), ("2020", "notes outstanding", "duration 지속"), ("2021-02-23", "redemption notice", "$25+accrued"), ("2021-03-25", "expected redemption", "terminal payoff")],
    claims=[
        claim("35~36c mispricing", "강한 성공", "note가 recovery보다 싸다.", "asset coverage가 market panic을 이긴다.", "quoted discount.", "unsecured recovery >36.", "coverage 붕괴면 반증.", "par redemption.", "+64~65 points.", "quoted cents/par 단위 주의.", "$25 par dollars로 변환한다."),
        claim("senior-note identity", "강한 성공", "common보다 선순위 fixed claim을 산다.", "contractual coupon·principal과 priority.", "indenture terms.", "security 정확히 식별.", "common으로 분류되면 분석 무효.", "6.875% senior unsecured due 2047.", "security 교정.", "ticker-only mapping.", "CUSIP·par·maturity를 저장한다."),
        claim("asset coverage", "성공", "haircut 후에도 note principal을 지지.", "portfolio recoveries가 unsecured claims를 덮는다.", "BDC assets.", "marks realizable.", "nonaccrual·secured claims가 coverage <1x면 반증.", "Ares assumption과 par repayment.", "최종 100 recovery.", "중간 coverage 수치 제한.", "waterfall을 분기별 갱신한다."),
        claim("credit-market easing", "성공", "liquidity 정상화가 default risk를 낮춘다.", "funding access·asset sales.", "GFC panic entry.", "markets reopen.", "refinancing failure면 반증.", "2010 M&A 종결.", "liquidity exit.", "macro catalyst 광범위.", "issuer-specific liquidity를 본다."),
        claim("Ares assumption", "강한 성공", "change of control이 credit를 보존한다.", "stronger acquirer가 obligations를 assume.", "deal structure.", "indenture 존속.", "notes haircut/cancel이면 반증.", "2010 notes assumed.", "duration risk 감소.", "T0 exact catalyst는 아님.", "deal debt treatment를 직접 읽는다."),
        claim("par+coupon payoff", "강한 성공", "coupon을 받고 par 회수.", "contractual redemption.", "6.875% note.", "no default.", "below-par exchange면 반증.", "2021 $25+accrued.", "principal 약 +178% before coupons.", "exact IRR ledger 없음.", "principal·coupon·reinvestment를 분리한다."),
    ],
)


add(
    id="7e85648d-bd5e-40a9-9407-88cf02528b48", date="2004-06-24", author="rylflush803", ticker="AFCE", company="AFC Enterprises Inc.", filename="analysis/ideas/2004/2004-06-24_AFCE_long.md", source="", group="afce", direction="Long", raw_direction="Long", security="AFC Enterprises common equity / Long", entry="약 $21", horizon="12개월 asset sales·distribution", raw_horizon="~6x FY04E EBITDA; Church's/Cinnabon sale; ~$28 target",
    title="restaurant SOTP·asset-sale Long", verdict="강한 성공 — divestitures와 $12 special dividend", score=9.2, process=8.8,
    conclusion="약 $21에서 Church's·Cinnabon 매각으로 Popeyes pure-play와 cash distribution을 기대했다. Cinnabon은 약 $21m, Church's는 약 $379m cash+$7m note에 매각됐고 2005-06 $12/share special dividend가 지급됐다. 1년 내 value crystallization이 직접 확인됐다.",
    t0="여러 restaurant brands와 복잡한 balance sheet 때문에 약 6x FY04E EBITDA로 할인됐다. noncore brands를 매각하고 Popeyes franchise 중심으로 단순화하면 약 $28 가치가 보인다는 논지였다.", reverse="매각가격이 낮거나 tax·debt·transaction cost가 proceeds를 흡수하고 Popeyes standalone earnings가 약하면 distribution과 rerating이 작을 수 있었다.",
    valuation="기업가치에서 Church's·Cinnabon net proceeds와 잔존 Popeyes EBITDA를 분리했다. headline sale price가 아니라 debt·tax 뒤 주당 distribution으로 검증한다.",
    actual="Cinnabon은 약 $21m cash, Church's는 약 $379m cash와 $7m note 조건으로 매각됐다. AFCE는 2005-06 $12/share special cash dividend를 지급해 SOTP 가치의 상당 부분을 직접 반환했다.",
    price="$12 dividend는 약 $21 entry의 57%에 해당하는 gross cash distribution이다. ex-dividend 가격·세금·정확 exit ledger가 없어 이를 +57% total return으로 표현하지 않는다.",
    drivers="비핵심 브랜드의 signed sales가 불투명한 SOTP를 현금으로 바꾸고 대규모 special dividend가 holding-company discount를 직접 줄였다.",
    counterfactual="매각대금에서 tax·debt·fees를 30% 차감하고 Popeyes EBITDA를 5x만 적용해도 $21을 보호하는가?", error="좋은 event thesis였지만 headline gross proceeds와 common distribution 사이 bridge, ex-dividend price 조정을 더 명시적으로 제시했어야 한다.", warning="sale close 지연·net proceeds 감소가 경고였으나 실제 두 거래와 dividend가 예정 horizon 안에 진행됐다.", first_signal_date="2004-11-30", lessons=lessons("afce"), checklist=checklist("afce"), scorecard=sc("Popeyes 생존", "SOTP 성공", "asset sales 성공", "common distribution", "1년 내 성공"),
    scenarios=[("Bear", "sale discount·tax leakage", "낮은 distribution", "미발생"), ("Base", "두 brands 매각", "~$28 SOTP", "현금화"), ("Bull", "high proceeds+Popeyes rerating", "$12 dividend+stub", "실현")],
    metrics=[("Entry", "~$21", "~$28 target", "$12 dividend+stub", "강한 성공"), ("Cinnabon sale", "예정", "현금화", "~$21m cash", "성공"), ("Church's sale", "예정", "현금화", "~$379m cash+$7m note", "성공"), ("Special dividend", "미정", "proceeds distribution", "$12/share", "성공"), ("EV/EBITDA", "~6x FY04E", "pure-play rerating", "event value crystallized", "성공")],
    timeline=[("2004-06-24", "VIC Long", "SOTP thesis"), ("2004-H2", "Cinnabon sale process", "cash catalyst"), ("2004-11", "Cinnabon disposition", "~$21m cash"), ("2004-12", "Church's agreement", "major catalyst"), ("2005-Q1", "Church's close", "$379m+$7m note"), ("2005-06", "$12 special dividend", "direct payoff"), ("2005-H2", "Popeyes pure-play", "simplified business"), ("후속", "ex-dividend stub", "total-return 분리")],
    claims=[
        claim("Cinnabon sale", "성공", "noncore Cinnabon을 매각.", "cash realization·complexity 감소.", "sale process.", "buyer·terms 확정.", "deal break면 반증.", "약 $21m cash.", "현금화 성공.", "gross/net 차이.", "net proceeds로 평가한다."),
        claim("Church's sale", "강한 성공", "Church's 매각이 큰 현금을 만든다.", "major asset sale.", "strategic interest.", "financing·approval.", "저가·지연이면 반증.", "$379m cash+$7m note.", "구체적 consideration.", "note collectability 별도.", "cash와 note를 분리한다."),
        claim("Popeyes pure-play", "성공", "잔존회사가 단순한 franchisor가 된다.", "conglomerate discount 감소.", "Popeyes franchise.", "standalone earnings 유지.", "Popeyes 악화면 반증.", "pure-play로 전환.", "구조 실현.", "사업 quality 검증은 후속.", "stub earnings를 별도 추적한다."),
        claim("~6x EBITDA cheap", "성공", "asset sales 전 valuation이 싸다.", "net proceeds와 stub value 합이 price 초과.", "FY04E EBITDA.", "EBITDA quality·debt 정확.", "net SOTP <$21이면 실패.", "$12 dividend+잔존 stub.", "entry의 57% 현금반환.", "gross EV/EBITDA만 사용.", "cash-to-equity bridge를 만든다."),
        claim("~$28 target", "방향 성공", "SOTP가 약 $28.", "sales+pure-play rerating.", "segment values.", "close와 multiple.", "1년 내 value 미실현이면 실패.", "대규모 dividend로 crystallize.", "exact adjusted price 없음.", "ex-dividend 비교 제한.", "distribution+adjusted stub로 검증한다."),
        claim("$12 special dividend", "강한 성공", "매각대금을 주주에게 반환.", "현금 distribution.", "net sale proceeds.", "board authorization.", "debt retention만 하면 반증.", "2005-06 지급.", "$21 entry의 57% gross.", "세금·ex-date 미반영.", "cash received와 price adjustment를 함께 본다."),
    ],
)


add(
    id="51bdfbe0-1a47-44a7-809d-b069e416043a", date="2007-12-05", author="glg919", ticker="AFCE", company="AFC Enterprises Inc.", filename="analysis/ideas/2007/2007-12-05_AFCE_long.md", source="", group="afce", direction="Long", raw_direction="Short", security="AFC Enterprises common equity / Long", entry="2007-12 AFCE common", horizon="18~24개월", raw_horizon="97% franchised Popeyes; 2009 EPS $1; $14 target",
    title="Popeyes management-turnaround Long", verdict="지연 성공 — mechanism 적중, 2009 horizon 실패", score=7.0, process=7.3,
    conclusion="raw Short는 원문 Long으로 교정했다. 2008 adjusted EPS $0.76과 negative SSS로 2009 EPS $1 target는 제때 성립하지 않았지만, Cheryl Bachelder 체제의 franchisee alignment와 operations가 개선돼 2010 global SSS +2.6%, 2011 adjusted EPS $0.99에 도달했다. 약 2년 지연된 성공이다.",
    t0="97% franchised Popeyes가 새 leadership 아래 menu·marketing·franchisee returns를 개선하면 capital-light royalty growth와 2009 EPS $1, 18~24개월 $14 target를 낼 것으로 봤다.", reverse="brand fatigue, franchisee underinvestment와 weak SSS가 management change만으로 빠르게 회복되지 않고 recession이 turnaround를 지연할 가능성이 있었다.",
    valuation="2009 EPS $1에 약 14x를 적용한 $14 target다. EPS와 multiple을 별도 claim으로 두고 18~24개월이라는 시간조건을 지켜야 한다.",
    actual="2008 adjusted EPS는 $0.76, SSS는 약했다. 2010 global SSS +2.6%로 전환했고 2011 adjusted EPS $0.99에 도달했다. mechanism은 맞았지만 target earnings가 약 2년 늦었다.",
    price="verified entry·exit ledger가 없어 $14 hit나 exact return을 만들지 않는다. EPS·SSS와 명시 horizon을 기준으로 지연 성공 판정한다.",
    drivers="franchisee economics와 brand execution 개선이 royalty base를 회복시켰지만 조직·매장 수준 변화에는 원문보다 더 긴 시간이 필요했다.",
    counterfactual="2008 negative SSS가 2010까지 이어지고 EPS가 $0.75에 머물러도 entry valuation이 downside를 견디는가?", error="turnaround direction은 맞았지만 97% franchised 구조가 실행속도도 빠르게 만든다고 가정했다. franchisee alignment에는 더 긴 lag가 있었다.", warning="2008 adjusted EPS $0.76과 negative SSS가 2009 $1 target의 최초 명확한 경고였다.", first_signal_date="2008-12-28", lessons=lessons("afce"), checklist=checklist("afce"), scorecard=sc("turnaround 성공", "EPS 지연", "management catalyst 성공", "common 적절", "2년 지연"),
    scenarios=[("Bear", "SSS 부진 지속", "EPS <$0.75", "2008 접근"), ("Base", "점진 회복", "$1 EPS 2011", "실현"), ("Bull", "2009 $1·$14", "18~24개월 target", "시간 실패")],
    metrics=[("Franchise mix", "97%", "asset-light leverage", "유지", "성공"), ("2008 adjusted EPS", "$1 path", "가속", "$0.76", "미달"), ("2009 EPS target", "$1.00", "$1.00", "2011 $0.99", "약 2년 지연"), ("2010 global SSS", "turnaround", "positive", "+2.6%", "성공"), ("Price target", "$14", "18~24개월", "verified ledger 없음", "미검증")],
    timeline=[("2007-12-05", "VIC Long", "raw Short 교정"), ("2008", "recession·negative SSS", "horizon risk"), ("2008-12", "adjusted EPS $0.76", "first break"), ("2009", "$1 EPS deadline", "미달"), ("2010", "global SSS +2.6%", "mechanism 확인"), ("2011", "adjusted EPS $0.99", "target 거의 달성"), ("2012", "growth 지속", "turnaround 정착"), ("후속", "timing과 direction 분리", "지연 성공")],
    claims=[
        claim("97% franchised leverage", "성공", "asset-light model이 회복을 증폭.", "SSS·unit sales가 royalty로 전환.", "franchise mix.", "franchisees 재투자.", "closures·royalty decline이면 반증.", "turnaround 뒤 growth.", "구조 유지.", "asset-light가 속도를 보장하지 않음.", "franchisee ROI를 함께 본다."),
        claim("management turnaround", "성공", "새 leadership이 brand를 고친다.", "menu·marketing·operations alignment.", "Cheryl Bachelder 체제.", "franchisee buy-in.", "SSS 악화 지속이면 반증.", "2010 SSS +2.6%.", "방향 실현.", "time lag 과소평가.", "leading KPI calendar를 둔다."),
        claim("2009 EPS $1", "시간 실패", "2009 EPS가 $1.", "SSS와 G&A leverage.", "turnaround plan.", "빠른 execution.", "2009 <$0.90이면 실패.", "2011 $0.99.", "약 2년 지연.", "horizon 무시 위험.", "맞은 숫자도 늦으면 실패로 기록한다."),
        claim("positive SSS", "지연 성공", "same-store sales가 개선.", "traffic·ticket 회복.", "brand initiatives.", "consumer response.", "2년 negative면 반증.", "2008 약세 후 2010 +2.6%.", "2년 lag.", "company/global 정의 주의.", "SSS 정의와 시점을 고정한다."),
        claim("$14 target", "미검증·지연", "18~24개월 $14.", "EPS $1×14x.", "turnaround multiple.", "EPS와 multiple 동시 적중.", "기한 내 EPS 미달이면 target thesis 실패.", "EPS가 기한 후 근접.", "price ledger 없음.", "later success로 target 소급.", "earnings와 price claim을 분리한다."),
        claim("raw Short", "metadata 실패", "SQL은 Short.", "direction 오류가 결론을 뒤집는다.", "원문 upside·target.", "원문 확인.", "downside thesis면 Short.", "실제 Long.", "완전 반대.", "raw flag 신뢰.", "본문 payoff로 방향을 확정한다."),
    ],
)


add(
    id="1d73c8b5-7c7e-4d4f-8e89-52a16d3bc538", date="2011-03-25", author="juice835", ticker="AFCE", company="AFC Enterprises Inc.", filename="analysis/ideas/2011/2011-03-25_AFCE_long.md", source="", group="afce", direction="Long", raw_direction="Short", security="AFC Enterprises common equity / Long", entry="약 $14.65", horizon="3~5년 compounding", raw_horizon="2011 EPS $0.91~0.95; FCF ~$1/share; 5Y EPS CAGR 13~15%",
    title="asset-light franchisor compounding Long", verdict="매우 강한 성공 — EPS compounding·$79 takeout", score=9.5, process=9.0,
    conclusion="raw Short를 Long으로 교정했다. 2011 adjusted EPS $0.99로 guidance를 넘고 2012 $1.24, 2015 약 $1.89~1.91로 compounding했다. RBI가 2017 $79 cash로 인수해 entry 대비 5.39x price multiple을 만들었다. dividends·tax를 포함한 exact IRR은 별도다.",
    t0="약 $14.65에서 2011 EPS guide $0.91~0.95, FCF 약 $1/share와 5년 EPS CAGR 13~15%를 제시했다. franchised unit growth·SSS·buyback이 capital-light per-share compounding을 만든다는 논지였다.", reverse="restaurant competition, commodity inflation, franchisee unit economics와 높은 starting multiple이 성장률을 낮추거나 capital return을 제한할 수 있었다.",
    valuation="$14.65는 약 $1 FCF의 14.7x였다. 13~15% EPS CAGR이 실현되면 multiple 유지로도 수익이 나지만 growth miss 시 downside를 별도 stress해야 했다.",
    actual="adjusted EPS는 2011 $0.99, 2012 $1.24, 2015 약 $1.89~1.91로 성장했다. RBI는 2017-02 $79 cash deal을 발표했고 2017-03 종결했다.",
    price="$79/$14.65≈5.39x price multiple, 즉 단순 +439%다. 약 6년 보유의 대략적 annualization을 만들 수는 있어도 정확 dates·dividends·tax가 없어 exact IRR은 주장하지 않는다.",
    drivers="asset-light royalty growth, positive SSS, net unit additions와 disciplined capital allocation이 EPS를 복리화했고 strategic buyer가 global brand value에 premium을 지불했다.",
    counterfactual="EPS CAGR이 8%, exit multiple이 12x에 그치고 takeout이 없어도 $14.65에서 만족할 수 있는가?", error="강한 결론이지만 eventual $79 strategic premium을 T0 intrinsic-value 적중으로 모두 돌리면 안 된다. operating compounding과 terminal multiple을 분리해야 한다.", warning="2011 EPS가 guide를 상회해 초기 thesis break는 없었다. 사전 경고는 negative SSS·net closures·franchisee return 저하였다.", first_signal_date="2012-02-29", lessons=lessons("afce"), checklist=checklist("afce"), scorecard=sc("quality 확인", "FCF multiple 성공", "growth·takeout 성공", "common 적절", "5년 강한 성공"),
    scenarios=[("Bear", "8% EPS CAGR·12x", "제한적 upside", "미발생"), ("Base", "13~15% CAGR", "EPS compounding", "실현"), ("Bull", "global brand premium", "$79 takeout", "실현")],
    metrics=[("Entry", "$14.65", "compounding", "$79 cash", "5.39x"), ("2011 adjusted EPS", "$0.91~0.95 guide", "guide 달성", "$0.99", "상회"), ("2012 adjusted EPS", "13~15% CAGR", "~$1.12", "$1.24", "상회"), ("2015 adjusted EPS", "5Y CAGR path", "~$1.7~1.9", "$1.89~1.91", "성공"), ("FCF/share", "~$1", "growth·capital return", "EPS/royalty 성장", "방향 성공")],
    timeline=[("2011-03-25", "VIC Long", "raw Short 교정"), ("FY2011", "adjusted EPS $0.99", "guide 상회"), ("FY2012", "adjusted EPS $1.24", "compounding 확인"), ("2013", "unit·SSS growth", "engine 지속"), ("FY2015", "EPS ~$1.89~1.91", "5년 경로 성공"), ("2017-02-21", "RBI $79 deal", "strategic premium"), ("2017-03-27", "거래 종결", "cash payoff"), ("후속", "5.39x 단순 multiple", "IRR 분리")],
    claims=[
        claim("2011 EPS $0.91~0.95", "성공", "guidance 범위 달성.", "SSS·royalty·cost control.", "company guide.", "execution 유지.", "$0.88 미만이면 반증.", "$0.99 adjusted.", "상단 대비 +4.2%.", "adjusted 정의 확인 필요.", "guidance와 동일 정의를 쓴다."),
        claim("FCF ~$1/share", "방향 성공", "asset-light model이 EPS를 현금화.", "low capex·royalty collection.", "franchise mix.", "working capital·tax 안정.", "FCF가 EPS보다 크게 낮으면 반증.", "growth·capital allocation 지속.", "exact annual FCF bridge 제한.", "EPS를 FCF로 대체.", "cash conversion을 별도 표로 둔다."),
        claim("5Y EPS CAGR 13~15%", "성공", "EPS가 중-teens 복리 성장.", "SSS+units+buyback.", "2011 base.", "franchisee economics 유지.", "2015 EPS <$1.60이면 반증.", "2015 ~$1.89~1.91.", "$0.99 base 대비 약 17.6% CAGR.", "start/end 정의 민감.", "reported periods와 adjusted 정의를 고정한다."),
        claim("asset-light unit growth", "성공", "franchise expansion이 낮은 자본으로 성장.", "royalty base 확대.", "97%+ franchise structure.", "unit-level returns 양호.", "net closures면 반증.", "global brand가 strategic buyer 유인.", "질적·정량 방향 적중.", "buyer premium과 운영가치 혼용.", "net openings·franchisee ROI를 추적한다."),
        claim("valuation at $14.65", "강한 성공", "약 14.7x FCF가 growth 대비 싸다.", "earnings compounding이 multiple risk 상쇄.", "~$1 FCF/share.", "growth 두 자릿수.", "EPS stagnation이면 반증.", "EPS 거의 두 배·$79 exit.", "terminal multiple 크게 확대.", "takeout premium 의존 가능.", "no-takeout valuation도 계산한다."),
        claim("$79 strategic exit", "강한 성공", "brand가 장기 전략가치를 만든다.", "global scale buyer synergy.", "Popeyes growth.", "buyer·financing.", "deal break면 반증.", "2017 cash acquisition 종결.", "entry 대비 5.39x.", "T0 명시 catalyst 아님.", "운영 compounding과 terminal event를 분리한다."),
    ],
)


def idea_sources(i):
    return [
        S("VIC source-DB preserved original", i["source"], "Value Investors Club / source SQL", i["date"], "T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL은 source SQL에서 null이다.", "원문"),
        *GROUP_SOURCES[i["group"]],
    ]


def render_index():
    rows = []
    for n, i in enumerate(IDEAS, 1):
        rel = i["filename"].removeprefix("analysis/")
        rows.append(f"| {n} | {i['date']} | {i['ticker']} | {i['raw_direction']} | {i['direction']} | [{i['company']}]({rel}) | {i['verdict']} |")
    return "\n".join([
        "# Batch 067 — AEZS / AF / AFC / AFCE V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. 아이디어 1건 = canonical Markdown 1개다.",
        f"> Research as-of {ASOF}. ticker보다 date+legal entity+security를 우선하고 exact return은 cash ledger가 있을 때만 계산했다.", "",
        "## Canonical idea files", "", "| # | 날짜 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## Entity / direction / security audit", "",
        "- AF 2004·2006은 Astoria Financial, AF 2009·2014는 AlarmForce Industries다.",
        "- AFC 2002는 Allmerica Financial common, AFC 2008은 Allied Capital 6.875% senior unsecured notes due 2047이다.",
        "- raw Short→실제 Long 교정은 Astoria 2004, AlarmForce 2014, Allmerica 2002, AFCE 2007·2011의 5건이다.",
        "- Allied note는 $25 par의 35~36 cents, 즉 약 $8.75~9.00 entry다. common price와 섞지 않는다.", "",
        "## 핵심 비교", "",
        "1. AEZS는 Zoptrex가 실패했지만 Macrilen이 trial headline miss 뒤 FDA 승인·license에 성공했다. clinical·regulatory·commercial outcome을 분리한다.",
        "2. Astoria 2004 Long은 refinancing benefit을 선형 합산해 EPS를 과대평가했고, 2006 Short는 asset/liability repricing mismatch를 정확히 잡았다.",
        "3. AlarmForce 2009는 subscriber growth를 과대평가했지만 recurring franchise는 남았고, 2014는 운영개선보다 BCE의 strategic takeout이 payoff를 만들었다.",
        "4. Allmerica는 negative life stub 제거로 P&C 가치가 드러났고, Allied note는 security priority와 Ares debt assumption이 par recovery를 만들었다.",
        "5. AFCE는 2004 asset sale·special dividend, 2007 지연 turnaround, 2011 장기 compounding·$79 takeout으로 thesis stage가 진화했다.", "",
        "## 구조화 데이터", "",
        "- `data/curated/batch_067_aezs_af_afc_afce_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.",
        "- `data/curated/batch_067_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.",
        "- `analysis/batch_067_aezs_af_afc_afce_10.md`: Streamlit wrapper.", "",
    ])


def main():
    if len(IDEAS) != 10 or len({i["id"] for i in IDEAS}) != 10:
        raise ValueError("Batch 067 requires ten unique ideas")
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
            "**C/제한** — verified corporate action·reported operating data만 사용; exact transaction ledger가 없으면 total return·IRR을 만들지 않음.",
        )
        (ROOT / idea["filename"]).write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_067_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 067 — AEZS / AF / AFC / AFCE V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 067 V9 Index](batch_067_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_067_aezs_af_afc_afce_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 67
    payload["title"] = "AEZS / Astoria / AlarmForce / Allmerica / Allied Notes / AFC Enterprises — Entity, Repricing and Security Payoff V9"
    payload["metadata_audit"] = {
        "direction_corrections": 5,
        "company_mapping_corrections": 4,
        "security_type_corrections": 1,
        "cross_batch_duplicates_removed": 0,
        "performance_rows_rejected": 10,
        "corporate_action_terminal_payoffs": 5,
        "notes": [
            "AF 2004·2006을 Astoria, AF 2009·2014를 AlarmForce로 date-specific 교정.",
            "AFC 2002를 Allmerica common, AFC 2008을 Allied Capital 6.875% senior note로 교정.",
            "raw Short→actual Long 다섯 건을 원문 payoff 기준으로 교정하되 raw flag는 보존.",
            "source SQL 공개 VIC URL은 10건 모두 null이므로 source-DB 원문을 기준으로 보존.",
            "price/coupon/dividend ledger가 없는 건은 exact total return·IRR을 만들지 않고 corporate-action consideration만 표시.",
        ],
    }
    payload["batch_lessons"] = [
        "historical ticker는 legal entity가 아니며 date+entity+security가 canonical key다.",
        "bank EPS는 refinancing 항목의 합이 아니라 asset/liability repricing gap의 결과다.",
        "biotech trial headline, regulatory approval와 commercial license는 서로 다른 claim이다.",
        "subscription franchise quality와 geographic growth forecast를 분리한다.",
        "same ticker common과 senior note는 payoff·data unit가 완전히 다르다.",
        "asset sale은 gross proceeds보다 net distribution으로 판정한다.",
        "turnaround가 맞아도 목표연도보다 늦으면 timing claim은 실패다.",
    ]
    failure_patterns = {
        "aezs": "binary_basket; cash_burn; regulatory_path; dilution",
        "astoria": "repricing_mismatch; additive_eps_bridge; deposit_beta; timing",
        "alarmforce": "geographic_cac_extrapolation; churn; slow_growth; event_dependency",
        "allmerica": "negative_stub; retained_liability; entity_mapping; reserve_tail",
        "allied_note": "security_misclassification; duration; recovery_waterfall; coupon_ledger",
        "afce": "gross_vs_net_proceeds; turnaround_lag; multiple; horizon",
    }
    success_patterns = {
        "aezs": "program_separation; regulatory_salvage; license_monetization",
        "astoria": "repricing_bridge; consensus_gap; reported_nim_validation",
        "alarmforce": "cohort_economics; recurring_revenue; strategic_takeout",
        "allmerica": "implied_stub; liability_transfer; focused_franchise",
        "allied_note": "security_selection; seniority; debt_assumption; par_redemption",
        "afce": "asset_sale; cash_distribution; franchise_compounding; strategic_exit",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failure_patterns[idea["group"]]
        row["success_pattern_ko"] = success_patterns[idea["group"]]
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
