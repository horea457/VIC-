#!/usr/bin/env python3
"""Build Batch 068 canonical V9 reports and production overlay."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-18"
CATALOG = ROOT / "data/curated/batch_068_source_catalog.json"
OUTPUT = ROOT / "data/curated/batch_068_afce_affy_afg_afh_afhp_afi_deep_v7.json"

spec = importlib.util.spec_from_file_location("batch64_base", ROOT / "scripts/64_build_batch_064_v9.py")
base = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(base)
C, S = base.C, base.S


BUSINESS = {
    "afce": "AFC Enterprises는 Popeyes 중심의 asset-light restaurant franchisor였다. 가맹점 매출에서 royalty와 advertising fee를 받고 일부 company stores를 운영했다. system sales, SSS, 순점포 증가와 franchisee unit economics가 royalty FCF와 장기 브랜드 가치를 결정한다.",
    "affy": "Affymax는 OMONTYS 회수 뒤 실질 영업이 거의 없는 public shell이었다. common의 가치는 현금사업보다 NOL을 합법적으로 사용할 수 있는 수익사업의 유입 확률, Section 382 제한, 거래비용과 기다리는 시간의 현재가치에 달렸다.",
    "afg": "AF Gruppen은 노르웨이의 construction, civil engineering, energy/environment와 demolition·recycling contractor다. 수주잔고가 매출로 전환될 때 project margin과 loss provision을 통과해야 하므로 backlog 규모보다 mix·execution·cash conversion이 중요하다.",
    "atlas_common": "Atlas Financial은 taxi·limousine·paratransit 등 niche commercial-auto 보험사였다. premium growth가 loss ratio와 reserve adequacy를 훼손하지 않을 때만 combined ratio, book value와 common 가치가 복리화한다. 훗날 legacy 보험을 줄이고 MGA로 전환했지만 holding-company debt는 남았다.",
    "atlas_note": "AFHBL은 Atlas common이 아니라 $25 par의 6.625% senior unsecured notes due 2022였다. 2022 scheme 뒤 현금 6.625% 또는 PIK 7.25%의 new notes due 2027로 바뀌었다. 명목원금, 지급형태, 선순위 담보채권, 유동성과 실제 현금 회수를 따로 봐야 한다.",
    "afhp": "AFH Financial Group은 영국 independent financial adviser 네트워크와 wealth platform을 운영했다. adviser recruitment·acquisition, recurring fee assets와 integration 뒤 cash conversion이 가치의 핵심이며 2021년 private-equity buyer가 현금으로 인수했다.",
    "afi": "Armstrong Flooring은 resilient flooring과 LVT를 제조·유통했다. volume·mix와 selling price에서 원재료·운송·공장고정비를 뺀 EBITDA, 그리고 working capital·capex·interest 뒤의 liquidity runway가 common payoff를 결정했다.",
}

ENGINE = {
    "afce": "franchised units × unit sales × royalty rate + company-store profit - G&A - tax - capex = FCF; net openings와 buyback을 fully diluted share 기준으로 연결한다.",
    "affy": "NOL × 적용세율 × 법적 사용가능비율 × 거래성공확률 × 시간할인 - shell burn·희석 = common option value; NOL face value는 cash가 아니다.",
    "afg": "backlog × conversion rate × project gross margin - loss provisions - overhead - tax ± working capital - capex = equity cash flow; EBT margin과 현금전환을 같이 본다.",
    "atlas_common": "earned premium × (1 - loss ratio - expense ratio) + investment income - tax = book-value growth; reserve development·debt·희석을 common에 반영한다.",
    "atlas_note": "realizable asset value - secured claims - operating burn = unsecured-note coverage; cash coupon과 PIK, maturity와 recovery waterfall을 실제 날짜별로 잇는다.",
    "afhp": "advisers × client assets × recurring fee rate - adviser payout - platform·central cost - acquisition/integration cash = FCF; cash consideration이 terminal payoff다.",
    "afi": "volume × price/mix - material·freight - conversion cost - SG&A - cash interest - capex - working capital = liquidity change; time-to-repair와 cash runway를 비교한다.",
}

KPI = {
    "afce": "global SSS, system sales, gross/net openings, franchise mix, royalty revenue, restaurant margin, G&A, adjusted EPS, FCF/share, leverage",
    "affy": "federal/state NOL, ownership changes, Section 382 annual limit, shell cash burn, tax rate, transaction probability, profitable taxable income, diluted shares",
    "afg": "revenue, order intake, backlog, EBT/EBIT margin, project write-downs, operating cash flow, net interest-bearing debt, ROIC, EPS, dividend",
    "atlas_common": "gross/earned premium, loss ratio, expense ratio, combined ratio, reserve development, statutory capital, book/share, EPS, debt and liquidity",
    "atlas_note": "exact indenture, par, quoted price/par, cash/PIK coupon, accrued interest, maturity, liquidity covenant, secured claims, subsidiary collateral, recovery",
    "afhp": "advisers, assets under management, recurring revenue, fee margin, acquisition price, integration cost, operating cash conversion, EPS, bidder consideration",
    "afi": "volume, price/mix, LVT mix, utilization, gross margin, adjusted EBITDA, working capital, capex, cash burn, liquidity, covenant headroom",
}


SOURCES = {
    "afce": [
        S("Popeyes FY2012 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1041379/000119312513080439/d444568d10k.htm", "SEC / AFC Enterprises", "2013-02-27", "2012 adjusted EPS $1.24, global SSS +6.9%, 141 openings·66 net, 2,104 restaurants와 franchise economics 검증."),
        S("Popeyes preliminary FY2013 results", "https://www.sec.gov/Archives/edgar/data/1041379/000119312514008863/d658964dex991.htm", "SEC / AFC Enterprises", "2014-01-10", "2013 adjusted EPS $1.42~1.43와 194 openings·126 net 검증."),
        S("RBI acquisition announcement", "https://www.sec.gov/Archives/edgar/data/1041379/000119312517050863/d332271dex991.htm", "SEC / RBI", "2017-02-21", "$79 cash/share와 약 $1.8bn 거래 검증."),
        S("RBI acquisition completion", "https://www.sec.gov/Archives/edgar/data/1041379/000119312517097222/d269346d8k.htm", "SEC / AFC Enterprises", "2017-03-27", "합병 종결과 terminal cash payoff 검증."),
    ],
    "affy": [
        S("Couchman Schedule 13D", "https://www.sec.gov/Archives/edgar/data/1158223/000092189514001932/sc13d09073012_08192014.htm", "SEC", "2014-08-19", "Couchman 투자·control context와 shell catalyst의 T0 전제 검증."),
        S("2020 SEC filing naming Affymax role", "https://www.sec.gov/Archives/edgar/data/727510/000092189520002102/sc13da105735004_08052020.htm", "SEC", "2020-08-05", "Jonathan Couchman이 Affymax CEO로 계속 기재된 후속 상태 교차검증."),
        S("2024 Enzo filing naming Affymax role", "https://www.sec.gov/Archives/edgar/data/316253/000121390024102169/ea0222393-8k_enzobio.htm", "SEC", "2024-11", "2024년에도 Affymax CEO 경력이 현재형으로 기재된 점과 장기 미실현 교차검증."),
    ],
    "afg": [
        S("AF Gruppen FY2024 results", "https://www.afgruppen.com/news/2025/02/af-gruppen-ended-the-year-with-solid-results-and-a-strong-order-intake/", "AF Gruppen", "2025-02-13", "2024 revenue NOK30.638bn, EBT NOK1.085bn, backlog NOK40.351bn, OCF NOK2.217bn 검증."),
        S("AF Gruppen Annual Report 2025", "https://www.afgruppen.com/kampanje/annual-report-af-gruppen/", "AF Gruppen", "2026", "2025 revenue NOK31.992bn, EBT NOK1.653bn와 backlog NOK44.716bn 검증."),
    ],
    "atlas_common": [
        S("Atlas 1-for-3 reverse split", "https://www.sec.gov/Archives/edgar/data/1539894/000153989413000033/exhibit991pressreleasedate.htm", "SEC / Atlas Financial", "2013-01-29", "1-for-3 reverse split과 2012 entry의 post-split 환산 검증."),
        S("Atlas FY2015 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1539894/000153989416000050/atlas2015form10k.htm", "SEC / Atlas Financial", "2016-03", "2013~15 premium, combined ratio, EPS와 book/share 검증."),
        S("Atlas FY2016 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1539894/000153989417000009/atlas2016form10k.htm", "SEC / Atlas Financial", "2017-03", "2016 reserve strengthening $32.6m, combined ratio 102.9%, EPS $0.19 검증."),
        S("Atlas 2024 subsidiary transfer", "https://www.sec.gov/Archives/edgar/data/1539894/000110465924008805/tm244617d1_8k.htm", "SEC / Atlas Financial", "2024-01-25", "핵심 subsidiaries의 secured lender 이전과 약 $12.7m debt satisfaction 검증."),
    ],
    "atlas_note": [
        S("Atlas scheme sanction announcement", "https://www.sec.gov/Archives/edgar/data/1539894/000153989422000005/afhifpressrelease030122.htm", "SEC / Atlas Financial", "2022-03-01", "99.34% 찬성, Cayman sanction과 new-note 구조 검증."),
        S("Atlas exchange effective", "https://www.sec.gov/Archives/edgar/data/1539894/000153989422000015/afh-20220414.htm", "SEC / Atlas Financial", "2022-04-14", "old notes cancellation과 new notes 발행일 검증."),
        S("2027 PIK-toggle note form", "https://www.sec.gov/Archives/edgar/data/1539894/000153989422000015/formofnoterepresenting6625.htm", "SEC / Atlas Financial", "2022-04-14", "$26.640m initial principal, 6.625% cash/7.25% PIK, 2027-04-27 maturity 검증."),
        S("Atlas 2024 subsidiary transfer", "https://www.sec.gov/Archives/edgar/data/1539894/000110465924008805/tm244617d1_8k.htm", "SEC / Atlas Financial", "2024-01-25", "minimum-liquidity default와 secured lender로의 asset transfer 검증."),
    ],
    "afhp": [
        S("Increased recommended cash offer", "https://shareprices.com/rns/increased-recommended-cash-offer-ddqvemypxlitszi/", "AFH / RNS mirror", "2021-03-02", "현금 offer가 463p에서 480p로 상향된 조건 검증.", "공시 미러"),
        S("Court sanction and scheme timetable", "https://www.lse.co.uk/rns/court-sanction-of-scheme-expected-scheme-timetable-z5daxunvun7f22r.html", "AFH / RNS mirror", "2021-06", "court sanction과 scheme effective timetable 검증.", "공시 미러"),
    ],
    "afi": [
        S("Armstrong Flooring Chapter 11 and asset sales", "https://www.sec.gov/Archives/edgar/data/1655075/000119312522232961/d305146d8k.htm", "SEC / Armstrong Flooring", "2022-08-26", "2022-05-08 Chapter 11, $107m/$31m/$59m asset sales와 equity likely no recovery 검증."),
        S("Armstrong Flooring SEC issuer archive", "https://www.sec.gov/edgar/browse/?CIK=1655075&owner=exclude", "SEC", "2016-2022", "spin-off 뒤 실적·유동성·구조조정 공시 교차검증."),
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
    "afce": ["같은 기업도 lifecycle stage가 바뀌면 asset discount·turnaround·compounding의 근거를 다시 써야 한다.", "franchisor는 gross openings보다 net openings와 franchisee returns를 본다.", "EPS 성장과 terminal strategic premium을 분리한다.", "cash ledger 없이는 장기 exact IRR을 만들지 않는다."],
    "affy": ["NOL face value를 cash로 보지 말고 사용가능성·세율·거래확률·시간을 곱한다.", "shell에서 무사건은 기다림이 아니라 핵심 bear case다.", "Section 382와 ownership change를 사전에 모델링한다.", "촉매 보유자의 명성보다 실행 가능한 거래 pipeline을 요구한다."],
    "afg": ["backlog는 매출도 이익도 아니며 conversion과 project margin을 거쳐야 한다.", "좋은 balance sheet와 좋은 entry valuation을 분리한다.", "EBT와 EBIT 정의를 섞지 않는다.", "목표연도 miss를 후속 개선으로 소급해 지우지 않는다."],
    "atlas_common": ["보험 growth는 reserve-adjusted combined ratio와 함께 봐야 한다.", "reverse split을 반영해 가격과 book/share 단위를 맞춘다.", "짧은 horizon 성공과 장기 reserve tail을 분리한다.", "MGA가 asset-light여도 holding-company debt 뒤 common residual은 별개다."],
    "atlas_note": ["distressed exchange의 par-for-par는 realized par recovery가 아니다.", "cash coupon과 PIK를 실제 지급일별로 분리한다.", "unsecured note는 secured lender의 asset sweep 뒤 잔여가치만 가진다.", "만기 전에는 최종 recovery를 확정하지 않는다."],
    "afhp": ["외부 cash bid는 intrinsic value의 강한 검증이지만 원 target와 consideration을 구분한다.", "bid 발표 전 standalone downside가 견딜 수 있어야 한다.", "가격수익과 배당·세금 포함 total return을 혼동하지 않는다.", "scheme calendar와 break conditions를 추적한다."],
    "afi": ["turnaround에서는 time-to-repair보다 liquidity runway가 길어야 한다.", "capacity와 과거 peak margin을 정상화 이익으로 바로 쓰지 않는다.", "working-capital release를 반복가능한 FCF로 보지 않는다.", "Chapter 11의 common은 asset sale headline보다 priority waterfall을 먼저 본다."],
}

CHECKLIST = {
    "afce": ["global/domestic SSS", "net openings", "franchisee payback", "royalty revenue", "G&A", "adjusted EPS", "FCF/share", "leverage·buyback"],
    "affy": ["NOL tax-year schedule", "Section 382 limit", "ownership changes", "cash burn", "transaction pipeline", "taxable-income capacity", "diluted shares"],
    "afg": ["backlog mix", "order intake", "conversion", "project provisions", "EBT margin", "OCF", "net debt", "ROIC·dividend"],
    "atlas_common": ["GPW/earned premium", "loss ratio", "expense ratio", "reserve development", "statutory capital", "BVPS", "debt", "liquidity"],
    "atlas_note": ["exact security", "secured claims", "liquidity covenant", "cash/PIK election", "accrued interest", "asset coverage", "maturity recovery"],
    "afhp": ["advisers/AUM", "recurring fee mix", "integration cost", "cash conversion", "offer conditions", "scheme vote", "cash settlement"],
    "afi": ["cash runway", "quarterly burn", "working capital", "gross margin", "EBITDA bridge", "capex", "covenant headroom", "priority waterfall"],
}


add(
    id="74afc0f3-c1cc-42f0-8759-65d207b26fb1", date="2012-04-20", author="oogum858", ticker="AFCE", company="AFC Enterprises Inc.", filename="analysis/ideas/2012/2012-04-20_AFCE_long.md", source="https://www.valueinvestorsclub.com/idea/AFC_ENTERPRISES_INC/1348883397", group="afce", direction="Long", raw_direction="Short", security="AFC Enterprises common equity / Long", entry="$16.50; market cap 약 $400m", horizon="2~3년 compounding; 장기 terminal event 별도", raw_horizon="2012E EBITDA 약 $50m; fair value $22.50~28.15; domestic growth·SSS·buyout",
    title="asset-light Popeyes compounding Long", verdict="매우 강한 성공 — 운영 추정 상회·2017 $79 cash", score=9.4, process=8.8,
    conclusion="raw Short를 실제 Long으로 교정했다. FY2012 adjusted EPS $1.24(+25%), global SSS +6.9%, 141 openings·66 net과 FY2013 adjusted EPS $1.42~1.43가 compounding을 확인했다. RBI는 2017년 $79 cash로 인수했다. $79/$16.50=4.79x는 단순 가격배수이며 배당·세금을 포함한 exact IRR은 아니다.",
    t0="$16.50, 약 $400m market cap와 2012E EBITDA 약 $50m에서 이미 개선된 Popeyes가 domestic whitespace, positive SSS와 franchise-funded openings로 EPS를 복리화할 수 있다는 논지였다. 제시 fair value는 $22.50~28.15였다.", reverse="시장은 turnaround의 쉬운 구간이 끝났고 franchisee economics, commodity inflation과 execution이 unit growth·SSS를 둔화시키며 약 8x EBITDA가 정당할 수 있다고 봤다.",
    valuation="약 $400m equity value를 2012E EBITDA 약 $50m와 비교한 headline 8x는 net debt·cash bridge가 필요하다. 단기 fair value $22.50~28.15와 장기 compounding을 분리하며, 2017 strategic premium은 T0 base case가 아니라 후속 terminal event다.",
    actual="FY2012에는 adjusted EPS $1.24, global SSS +6.9%, system sales +13.5%, 141 openings·75 closures로 66 net additions가 나왔다. 연말 2,104개 매장 중 2,059개가 franchised였다. FY2013 adjusted EPS는 $1.42~1.43, openings 194·net 126이었다. 2017-03-27 RBI가 $79 cash deal을 종결했다.",
    price="$79/$16.50=4.79x, 단순 가격상승은 약 +378.8%다. 약 5년간 배당·정확 settlement date·세금 ledger가 없으므로 이 수치를 total return 또는 exact IRR로 부르지 않는다.",
    drivers="franchisee-funded unit additions, positive SSS와 royalty/G&A leverage가 EPS를 늘렸고 global quick-service platform을 원하는 전략적 인수자가 terminal multiple을 높였다.", counterfactual="SSS 0%, net openings 30개, EPS growth 8%, exit 14x이며 takeout이 없어도 $16.50에서 충분한 downside protection이 있었는가?", error="turnaround 성공을 근거로 향후 SSS·net openings를 선형 연장할 위험과 strategic takeout을 intrinsic compounding 성과에 모두 귀속할 위험이 있었다.", warning="FY2012 실적은 오히려 초기 확인 신호였다. 사전 break는 global SSS 음전환, net closures 또는 franchisee return 악화였으며 관찰되지 않았다.", first_signal_date="2013-02-27", lessons=LESSONS["afce"], checklist=CHECKLIST["afce"], scorecard=sc("강한 성공", "단기 target·장기 가치 모두 지지", "unit growth·takeout 성공", "common 적절", "단기·장기 성공"),
    scenarios=[("Bear", "SSS 0%·net openings 30", "낮은 EPS growth·multiple 압박", "미실현"), ("Base", "SSS와 franchise openings 지속", "$22.50~28.15", "운영 상회"), ("Bull", "global brand·strategic premium", "$79 cash", "2017 실현")],
    metrics=[("Entry", "$16.50", "$22.50~28.15", "$79 cash", "4.79x 단순"), ("FY2012 adjusted EPS", "성장 기대", "약 $1.20대", "$1.24; +25%", "성공"), ("Global SSS", "positive", "성장", "+6.9%", "강한 성공"), ("2012 net openings", "domestic/global growth", "positive", "66 net", "성공"), ("FY2013 adjusted EPS", "compounding", "두 자릿수 성장", "$1.42~1.43; 약 +15%", "성공")],
    timeline=[("2012-04-20", "VIC Long", "raw Short 교정"), ("2012-12", "141 openings·66 net", "unit engine 확인"), ("2012-12", "global SSS +6.9%", "demand 확인"), ("2013-02-27", "FY2012 EPS $1.24", "초기 thesis 확인"), ("2013-12", "194 openings·126 net", "가속"), ("2014-01-10", "FY2013 EPS $1.42~1.43", "compounding"), ("2017-02-21", "RBI $79 deal 발표", "strategic premium"), ("2017-03-27", "거래 종결", "cash payoff")],
    claims=[
        claim("raw Short", "metadata 실패", "source SQL은 Short다.", "방향 오류는 payoff 해석을 반전시킨다.", "원문은 상승 valuation·성장·buyout을 제시했다.", "본문 payoff가 방향을 확정한다.", "하락으로 수익을 내는 구조면 Short다.", "실제는 common Long이었다.", "완전 반대.", "raw flag를 본문보다 우선할 위험.", "원문 payoff로 방향을 교정하고 raw는 보존한다."),
        claim("global SSS 성장", "강한 성공", "Popeyes SSS가 성장한다.", "점포매출 증가가 royalty와 restaurant profit을 높인다.", "turnaround 뒤 menu·brand momentum.", "traffic·ticket 개선이 지속된다.", "FY2012 global SSS가 0% 이하이면 반증.", "FY2012 +6.9%.", "반증선 대비 +6.9ppt.", "한 해의 강한 SSS를 영구성장으로 외삽할 수 있다.", "SSS를 traffic·ticket·promotion으로 분해한다."),
        claim("franchise unit growth", "강한 성공", "domestic whitespace를 낮은 corporate capital로 연다.", "net units가 royalty base를 확대한다.", "franchise model과 development pipeline.", "franchisee unit returns가 충분하다.", "gross openings에도 net closures면 반증.", "2012 66 net, 2013 126 net additions.", "net additions가 2배 가까이 가속.", "gross openings만 볼 위험.", "openings와 closures를 항상 함께 적는다."),
        claim("2012 earnings", "성공", "약 $50m EBITDA와 EPS growth가 현실화한다.", "SSS·units·G&A leverage.", "T0 operating estimates.", "commodity와 SG&A가 leverage를 상쇄하지 않는다.", "adjusted EPS 정체면 반증.", "adjusted EPS $1.24, +25%; operating EBITDA $55.9m.", "EBITDA가 약 $5.9m 상회.", "adjusted 정의와 leverage bridge 제한.", "EBITDA에서 FCF·EPS로 bridge한다."),
        claim("$22.50~28.15 fair value", "성공", "2~3년 내 valuation range로 rerating한다.", "EPS growth와 franchise multiple.", "$16.50 대비 36~71% upside.", "multiple compression이 없다.", "운영성공에도 가격이 entry 아래면 실패.", "후일 $79 cash terminal value가 range를 넘었다.", "장기 event라 단기 hit date는 미복원.", "나중 takeout으로 단기 target를 소급할 수 있다.", "target horizon과 terminal event를 따로 판정한다."),
        claim("strategic buyout", "강한 장기 성공", "Popeyes가 인수대상이 될 수 있다.", "global brand와 franchise platform이 buyer synergy를 만든다.", "asset-light global system.", "전략적 buyer가 premium을 지불한다.", "독립회사로 남으면 option 미실현.", "RBI가 $79 cash로 인수·종결.", "$16.50 대비 4.79x 단순.", "T0 base와 event optionality 혼용 위험.", "operating value와 buyer premium을 분리한다."),
    ],
)


add(
    id="da44c9d8-3ef2-48d8-b4e9-0f004b755947", date="2021-10-11", author="Barong", ticker="AFG NO", company="AF Gruppen ASA", filename="analysis/ideas/2021/2021-10-11_AFG_NO_long.md", source="https://www.valueinvestorsclub.com/idea/AF_Gruppen/2488905589", group="afg", direction="Long", raw_direction="Long", security="AF Gruppen Oslo-listed common equity / Long", entry="약 NOK197", horizon="약 2년; 2024 operating case 교차검증", raw_horizon="2024 revenue NOK36.7bn, EBIT margin 6.6%, probability-weighted fair value NOK248",
    title="Nordic quality-contractor Long", verdict="부분 실패 — balance sheet·backlog 성공, 성장·margin 경로 미달", score=5.5, process=7.0,
    conclusion="quality와 solvency는 유지됐지만 원 operating case는 미달했다. 2024 revenue NOK30.638bn은 NOK36.7bn 대비 16.5% 낮았고 EBT margin 3.5%는 제시 EBIT margin 6.6%와 정의가 다르지만 격차가 컸다. 2025 revenue NOK31.992bn·EBT NOK1.653bn으로 개선됐고 backlog는 NOK44.716bn이었다. exact stock return은 verified ledger 부재로 보류한다.",
    t0="약 NOK197에서 가족·직원 ownership, decentralization, demolition/environment capability와 강한 balance sheet가 NOK40bn revenue·7% margin의 장기 목표로 수렴할 것이라는 quality compounder thesis였다. 원 base는 2024 revenue NOK36.7bn·EBIT margin 6.6%, p-weighted FV NOK248이었다.", reverse="시장은 fixed-price project losses, construction cyclicality, acquisition/integration과 backlog의 낮은-margin mix 때문에 high-quality culture가 target margin으로 빠르게 전환되지 않을 위험을 반영했다.",
    valuation="NOK248은 약 NOK197 대비 25.9% upside다. operating case는 revenue×margin에서 시작하되 EBIT/EBT definitions, net cash, minority와 shares를 잇고, quality premium은 project loss tail 뒤에 적용해야 한다.",
    actual="2024 revenue NOK30.638bn, EBT NOK1.085bn(3.5%), backlog NOK40.351bn, operating cash flow NOK2.217bn, net interest-bearing receivable NOK99m, EPS NOK6.52와 dividend NOK5였다. 2025 revenue NOK31.992bn, EBT NOK1.653bn(약 5.17%)과 backlog NOK44.716bn으로 회복했지만 2024 target timing은 놓쳤다.",
    price="2021 entry 약 NOK197은 원문 기준이다. 동일 거래소·배당·split을 반영한 검증 가격 ledger가 없어 2026 spot 또는 exact CAGR을 쓰지 않는다. 운영목표와 명시 valuation range를 기준으로 판정한다.",
    drivers="order intake, cash generation과 net-cash balance sheet는 downside를 제한했지만 backlog mix와 project execution이 revenue·margin convergence를 늦췄다. 2025 EBT 회복은 quality를 확인하되 2024 timing miss를 지우지 않는다.", counterfactual="revenue NOK31bn, EBT margin 3.5%, 12x earnings와 NOK5 dividend만으로 NOK197 entry가 정당화됐는가?", error="문화·분산운영·backlog의 질을 target margin 도달확률로 너무 곧게 연결하고 project-level downside와 EBIT/EBT 정의 차이를 충분히 stress하지 않았다.", warning="2024 revenue·EBT 발표에서 target-year 매출과 margin이 동시에 미달해 timing claim이 명확히 깨졌다.", first_signal_date="2025-02-13", lessons=LESSONS["afg"], checklist=CHECKLIST["afg"], scorecard=sc("quality 유지", "NOK248 미검증·operating miss", "시간만으로 해결 안 됨", "common 적절", "2024 실패·2025 회복"),
    scenarios=[("Bear", "project losses·3% margin", "earnings·multiple 하락", "2024에 근접"), ("Base", "NOK36.7bn·6.6%", "NOK248", "2024 미달"), ("Recovery", "backlog conversion·5%+ EBT", "earnings 회복", "2025 일부 실현")],
    metrics=[("2024 revenue", "NOK36.7bn 목표", "NOK36.7bn", "NOK30.638bn", "-16.5%"), ("2024 margin", "EBIT 6.6%", "6.6%", "EBT 3.5%", "정의 차이에도 큰 미달"), ("2024 backlog", "quality order book", "성장 지지", "NOK40.351bn", "성공"), ("2024 OCF", "cash quality", "positive", "NOK2.217bn", "강한 성공"), ("2025 EBT", "장기 회복", "target 접근", "NOK1.653bn; 5.17%", "회복·여전히 7% 미달")],
    timeline=[("2021-10-11", "VIC Long", "NOK197 entry"), ("2022", "construction cost inflation", "margin pressure"), ("2023", "backlog 유지", "quality 지지"), ("2024-12", "revenue NOK30.638bn", "target 미달"), ("2024-12", "EBT margin 3.5%", "margin miss"), ("2025-02-13", "FY2024 발표", "horizon failure 확정"), ("2025-12", "EBT margin 약 5.17%", "회복"), ("2026", "backlog NOK44.716bn 보고", "forward support")],
    claims=[
        claim("2024 revenue NOK36.7bn", "실패", "revenue가 NOK36.7bn에 도달한다.", "backlog conversion과 market-share growth.", "T0 order book·long-term NOK40bn ambition.", "projects가 지연·취소 없이 전환된다.", "2024 revenue <NOK34bn이면 반증.", "NOK30.638bn.", "-NOK6.062bn/-16.5%.", "backlog를 매출로 선형 변환.", "backlog age·segment·cancellation을 반영한다."),
        claim("2024 EBIT margin 6.6%", "실패", "margin이 6.6%로 개선된다.", "mix·scale·decentralized execution.", "company 7% ambition.", "loss projects가 제한된다.", "reported operating margin <5%면 반증.", "공식 EBT margin 3.5%; 정의는 다르지만 큰 miss.", "약 -3.1ppt 대 reference.", "EBIT와 EBT 비교정의 불완전.", "동일 metric으로 target bridge를 고정한다."),
        claim("strong balance sheet", "강한 성공", "net cash가 cycle downside를 흡수한다.", "cash conversion과 낮은 leverage.", "T0 financial quality.", "working-capital reversal·M&A가 cash를 소진하지 않는다.", "net debt 급증이면 반증.", "2024 net interest-bearing receivable NOK99m.", "순현금 방향 유지.", "현금을 margin 안전과 동일시할 수 있다.", "liquidity와 project profitability를 분리한다."),
        claim("cash conversion", "강한 성공", "reported profit가 현금으로 전환된다.", "milestone billing과 working-capital discipline.", "contractor operating model.", "receivables·WIP가 cash를 흡수하지 않는다.", "OCF가 EBT를 장기간 하회하면 약화.", "2024 OCF NOK2.217bn 대 EBT NOK1.085bn.", "OCF/EBT 약 2.0x.", "단년 working-capital benefit 가능.", "다년 cash conversion을 본다."),
        claim("NOK248 fair value", "미검증·시간 실패", "약 2년 p-weighted FV NOK248.", "earnings growth와 quality multiple.", "NOK197 대비 25.9% upside.", "operating case가 제때 실현된다.", "목표연도 operating miss면 valuation premise 약화.", "2024 operating denominator 미달; price ledger 보류.", "FV의 earnings input 불성립.", "spot price 추정으로 빈칸을 채울 위험.", "verified total-return ledger가 없으면 운영 판정만 한다."),
        claim("NOK40bn·7% 장기목표", "미달·진행중", "company ambition에 수렴한다.", "scale·portfolio quality가 margin을 높인다.", "공식 long-term goals.", "profitable backlog와 capacity.", "2025에도 revenue <NOK35bn·margin <6%면 지연.", "2025 revenue NOK31.992bn, EBT 5.17%.", "매출 -NOK8.008bn, margin -1.83ppt 대 ambition.", "aspiration을 forecast로 사용.", "목표는 외부 base rate와 capacity로 haircut한다."),
    ],
)


add(
    id="b831bcd3-82aa-4fe6-97b7-582bc636de44", date="2016-08-30", author="clancy836", ticker="AFFY", company="Affymax Inc.", filename="analysis/ideas/2016/2016-08-30_AFFY_long.md", source="", group="affy", direction="Long", raw_direction="Short", security="Affymax public-shell common equity / Long", entry="market cap 약 $2.2m", horizon="1~3년 reverse merger / NOL monetization", raw_horizon="federal NOL 약 $481m; state NOL 약 $491m; Couchman-led transaction option",
    title="NOL-shell reverse-merger Long", verdict="실패 — value-unlocking transaction 장기 미실현", score=2.5, process=4.5,
    conclusion="raw Short를 실제 Long으로 교정했다. 약 $481m federal·$491m state NOL의 face value에 비해 $2.2m market cap은 작았지만, NOL을 사용할 profitable business와 실행 가능한 거래가 확인되지 않았다. 2020·2024 SEC cross-references에서도 Couchman은 Affymax CEO로 기재됐고 2017 세율 인하는 nominal shield도 낮췄다.",
    t0="운영자산이 거의 없는 $2.2m public shell에 거대한 NOL이 남아 있고 Jonathan Couchman이 profitable business를 reverse-merge하면 NOL 일부만 써도 common upside가 크다는 event-driven thesis였다.", reverse="시장은 Section 382, ownership-change limits, 거래상대 부재, shell burn·희석, 장기간 무사건과 NOL 만료를 반영해 face value를 거의 0으로 평가했다.",
    valuation="$481m federal NOL×35%는 약 $168m gross shield처럼 보이지만 이는 상한이 아니다. 2017 뒤 21% 세율이면 약 $101m before limits이며, Section 382 사용률·taxable income·거래확률·시기 할인과 비용을 적용해야 한다.",
    actual="T0 뒤 의미 있는 NOL monetization 또는 reverse merger를 확인하지 못했다. Couchman의 Affymax CEO 직함은 2020과 2024 외부 SEC filing에 계속 등장했다. 2017 Tax Cuts and Jobs Act의 21% corporate rate는 동일 NOL의 nominal federal shield를 낮췄다.",
    price="검증 가능한 진입·exit·distribution ledger와 value-unlocking corporate action이 없어 exact return은 계산하지 않는다. 핵심 event가 수년간 발생하지 않은 점을 opportunity-cost와 time-value 기준 실패로 판정한다.",
    drivers="NOL 자체가 아니라 미래 taxable income과 법적 사용가능성이 필요한데, 이를 공급할 거래가 오지 않았다. 촉매 부재와 시간할인이 작은 market cap만으로는 해결되지 않았다.", counterfactual="5년간 거래확률 10%/년, 21% 세율, Section 382로 shield의 20%만 사용 가능하고 연 $0.3m shell burn이면 $2.2m common의 기대가치는 얼마인가?", error="gross NOL을 realizable asset에 가깝게 취급하고 deal sourcing, tax opinion, ownership-change capacity와 explicit catalyst deadline을 요구하지 않았다.", warning="2017년 말까지 거래가 없고 세율이 35%에서 21%로 내려간 시점에 valuation premise와 timing이 동시에 약화됐다.", first_signal_date="2017-12-22", lessons=LESSONS["affy"], checklist=CHECKLIST["affy"], scorecard=sc("영업 thesis 없음", "face-value 과대", "reverse merger 미실현", "common option 소멸", "deadline 없는 실패"),
    scenarios=[("Bear", "거래 없음·burn·만료", "common option 소멸", "장기 경로"), ("Base", "제한된 NOL 사용 거래", "작은 monetization", "확인 안 됨"), ("Bull", "대규모 profitable business 유입", "multi-bagger", "미실현")],
    metrics=[("Market cap", "약 $2.2m", "small option premium", "거래 미확인", "싼 가격만 불충분"), ("Federal NOL", "약 $481m", "일부 monetization", "실현액 미확인", "실패"), ("State NOL", "약 $491m", "추가 tax shield", "실현액 미확인", "실패"), ("Federal tax rate", "35%", "gross shield 약 $168m", "2018부터 21%; 약 $101m before limits", "약 40% 감소"), ("Catalyst", "Couchman transaction", "1~3년", "2024까지 meaningful deal 미확인", "시간 실패")],
    timeline=[("2016-08-30", "VIC Long", "raw Short 교정"), ("2017", "reverse merger 대기", "무사건 risk"), ("2017-12-22", "TCJA enactment", "세율 35%→21%"), ("2018", "낮은 세율 적용", "gross shield 감소"), ("2020-08", "SEC filing에 Affymax CEO 직함", "shell 지속"), ("2021", "5년 horizon 경과", "time failure"), ("2024-11", "다시 Affymax CEO 직함", "거래 미실현"), ("2026-09-18", "research cutoff", "확정 value event 없음")],
    claims=[
        claim("raw Short", "metadata 실패", "source SQL은 Short다.", "방향은 payoff를 결정한다.", "원문은 NOL monetization upside를 샀다.", "본문을 기준으로 한다.", "하락 베팅이면 Short다.", "실제는 shell common Long.", "완전 반대.", "raw metadata 의존.", "방향을 원문 thesis로 확정한다."),
        claim("$481m federal NOL", "존재하나 가치 과대", "거대한 federal NOL이 common을 지지한다.", "미래 세금을 줄인다.", "T0 tax attributes.", "충분한 taxable income과 법적 사용가능성.", "사용 거래가 없거나 Section 382가 제한하면 약화.", "현금 monetization 확인 안 됨.", "face $481m 대 realized $0 확인.", "face와 PV 혼동.", "NOL을 세율·사용률·확률·시간으로 할인한다."),
        claim("$491m state NOL", "미실현", "state NOL도 추가 upside다.", "state taxable income의 세금을 줄인다.", "T0 disclosed balance.", "사업의 주별 income footprint가 맞는다.", "주별 만료·apportionment 불일치면 실패.", "사용 증거 없음.", "realized value 미확인.", "주별 법률 차이를 묶음.", "jurisdiction별 만료·세율·income을 매칭한다."),
        claim("Couchman transaction", "실패", "capital allocator가 profitable business를 유입한다.", "reverse merger가 NOL usage와 public listing을 결합한다.", "Couchman involvement.", "seller·financing·tax opinion이 확보된다.", "3년 내 signed deal이 없으면 timing 실패.", "2020·2024에도 Affymax CEO 직함만 확인, value event 없음.", "3년 deadline 초과.", "사람의 명성을 transaction pipeline으로 대체.", "counterparty·term sheet·deadline을 요구한다."),
        claim("35% tax-rate economics", "구조적 악화", "높은 법인세율이 NOL 가치를 키운다.", "NOL당 절감세액=적용세율.", "2016 federal rate 35%.", "세율이 유지된다.", "세율 인하 시 valuation haircut.", "TCJA로 21%.", "gross shield 약 40% 감소.", "정책변수 sensitivity 부족.", "세율 bear case를 항상 둔다."),
        claim("$2.2m margin of safety", "실패", "작은 market cap이 downside를 제한한다.", "option premium이 작아 NOL의 일부만 필요하다.", "tiny market cap.", "annual burn·dilution·opportunity cost가 작다.", "무사건 3년이면 thesis 손상.", "장기 무사건.", "가격이 작아도 시간가치 손실 큼.", "nominal cheapness를 downside floor로 봄.", "cash burn과 catalyst clock을 가격에 넣는다."),
    ],
)


add(
    id="cc7be7f0-3b67-44c5-baba-eaeb3ada5a33", date="2012-06-05", author="mrsox977", ticker="AFH", company="Atlas Financial Holdings Inc.", filename="analysis/ideas/2012/2012-06-05_AFH_long.md", source="", group="atlas_common", direction="Long", raw_direction="Long", security="Atlas Financial common equity / Long", entry="$1.77 pre-split; $5.31 post-split equivalent", horizon="약 2년 operating rerating", raw_horizon="GPW 약 $80m, combined ratio 95%, BVPS $2.03 pre-split and book rerating",
    title="specialty commercial-auto insurer rerating Long", verdict="강한 단기 성공 — premium·underwriting·book growth", score=8.7, process=8.0,
    conclusion="2013-01의 1-for-3 reverse split을 반영하면 $1.77 entry는 약 $5.31이다. 2013 GPW $93.1m은 2년 목표 $80m을 이미 넘었고 combined ratio 94.2%, BVPS $6.54 post-split였다. 2014 BVPS $9.08, 2015 $10.15와 역사적 high 약 $20.97로 단기 thesis는 강하게 성공했다. 2016 reserve 강화는 장기 tail을 드러냈다.",
    t0="specialty commercial-auto hard market에서 약 $80m GPW, 95% combined ratio와 book-value growth가 가능하며 $1.77 pre-split price가 $2.03 pre-split BVPS 부근에서 rerating할 수 있다는 thesis였다.", reverse="시장은 작은 insurer의 reserve uncertainty, taxi concentration, statutory capital과 corporate reorganization·낮은 liquidity를 할인했다.",
    valuation="pre-split $1.77와 BVPS $2.03은 약 0.87x book이다. 1-for-3 split 뒤 모든 per-share 수치를 3배 해야 하므로 entry $5.31, T0 BVPS 약 $6.09가 비교단위다. underwriting profit와 book growth가 없으면 낮은 P/B는 trap이다.",
    actual="2013 GPW $93.1m, combined ratio 94.2%, BVPS $6.54 post-split였다. 2014 GPW $122.4m·EPS $1.56·BVPS $9.08, 2015 GPW $209.3m·EPS $1.13·BVPS $10.15가 됐다. 2015 historical high는 약 $20.97였다. 2016에는 $32.6m reserve strengthening, combined ratio 102.9%, EPS $0.19로 tail risk가 현실화했다.",
    price="post-split entry $5.31 대비 reported 2015 high $20.97는 상단 기준 3.95x다. 이는 매도 가능한 종가·배당·세금 ledger가 아니라 historical high comparison이므로 exact realized return이나 IRR로 사용하지 않는다.",
    drivers="hard-market premium growth, sub-100% combined ratio와 book compounding이 P/B rerating을 만들었다. 이후 reserve development는 빠른 growth의 latent underwriting cost가 늦게 나타날 수 있음을 보여줬다.", counterfactual="combined ratio 102%, premium growth 10%, 0.8x stressed book를 적용해도 split-adjusted $5.31 entry가 안전했는가?", error="초기 2년 성공은 분명하지만 reported combined ratio와 book를 reserve-tail stress 없이 영구화하면 장기 quality를 과대평가하게 된다.", warning="2016 reserve strengthening $32.6m과 combined ratio 102.9%가 short-horizon 성공 뒤 최초의 명확한 장기 break였다.", first_signal_date="2017-03-16", lessons=LESSONS["atlas_common"], checklist=CHECKLIST["atlas_common"], scorecard=sc("2년 강한 성공", "0.87x book rerating", "premium·book catalyst 성공", "common 적절", "단기 성공·장기 tail"),
    scenarios=[("Bear", "reserve miss·102% CR", "book erosion", "2016 뒤 현실화"), ("Base", "$80m GPW·95% CR", "book compounding", "2013 상회"), ("Bull", "hard-market growth·rerating", "$20대", "2015 high에서 실현")],
    metrics=[("Entry", "$1.77 pre / $5.31 post", "book rerating", "2015 high ~$20.97", "3.95x high comparison"), ("GPW", "$80m 2Y 목표", "$80m", "2013 $93.1m", "+16.4%"), ("Combined ratio", "95%", "≤95%", "2013 94.2%", "+0.8ppt better"), ("BVPS", "$2.03 pre / $6.09 post", "growth", "2013 $6.54; 2015 $10.15", "성공"), ("2016 reserve strengthening", "낮은 tail", "제한적", "$32.6m", "장기 경고")],
    timeline=[("2012-06-05", "VIC Long", "$1.77 pre-split"), ("2013-01-29", "1-for-3 reverse split", "$5.31 equivalent"), ("2013-12", "GPW $93.1m", "target 상회"), ("2013-12", "combined ratio 94.2%", "underwriting 성공"), ("2014-12", "BVPS $9.08", "book compounding"), ("2015", "high 약 $20.97", "rerating"), ("2015-12", "GPW $209.3m·BVPS $10.15", "growth peak"), ("2016-12", "$32.6m reserve strengthening", "tail break")],
    claims=[
        claim("1-for-3 split adjustment", "검증 성공", "$1.77 entry를 현재 단위로 비교한다.", "split은 경제가치를 바꾸지 않고 주당 단위를 3배한다.", "2013 company release.", "동일 share class다.", "corporate-action mismatch면 비교 무효.", "$5.31 post-split equivalent.", "$1.77×3=$5.31.", "raw prices를 직접 잇는 오류.", "모든 price·BVPS·EPS를 같은 split basis로 맞춘다."),
        claim("GPW $80m", "강한 성공", "약 2년 GPW가 $80m.", "hard-market share gain이 earned premium으로 전환.", "niche underwriting opportunity.", "capital과 distribution이 성장 지원.", "$70m 미만이면 반증.", "2013 $93.1m.", "+$13.1m/+16.4%.", "written premium을 earnings로 동일시 위험.", "earned premium과 reserve adequacy를 함께 본다."),
        claim("combined ratio 95%", "성공", "underwriting이 약 95% CR.", "pricing·claims discipline.", "specialty expertise.", "reserve estimate가 충분하다.", ">100%면 반증.", "2013 94.2%.", "0.8ppt better.", "후기 reserve development 미반영.", "accident-year와 calendar-year를 분리한다."),
        claim("book-value compounding", "강한 성공", "underwriting profit가 BVPS를 늘린다.", "retained earnings가 equity를 축적.", "$2.03 pre-split BVPS.", "reserve·dilution이 통제된다.", "post-split BVPS <$6이면 실패.", "2013 $6.54, 2015 $10.15.", "2013 +7.4% 대 adjusted T0; 2015 +66.7%.", "reported book quality stress 부족.", "stressed reserves 뒤 tangible book를 본다."),
        claim("P/B rerating", "강한 단기 성공", "0.87x book가 정상화된다.", "growth·profitability가 discount를 축소.", "split-adjusted entry와 BVPS.", "underwriting 신뢰가 유지된다.", "price가 book 아래 머물면 실패.", "2015 high $20.97, BVPS $10.15.", "high에서 약 2.07x book.", "high를 realized exit로 오인.", "종가·거래가능성 없이 MFE만 제한 사용한다."),
        claim("reserve tail", "장기 실패", "성장 중 reserves가 충분하다.", "adequate case reserves가 future development를 막는다.", "sub-100% reported CR.", "frequency·severity 추정이 안정적이다.", "material adverse development면 반증.", "2016 strengthening $32.6m·CR 102.9%.", "명확한 tail loss.", "짧은 실적 창에 과신.", "reserve triangles와 claim duration을 stress한다."),
    ],
)


add(
    id="97762eda-4350-4f09-bad7-ca22a7255d61", date="2013-09-22", author="fiverocks19", ticker="AFH", company="Atlas Financial Holdings Inc.", filename="analysis/ideas/2013/2013-09-22_AFH_long.md", source="https://www.valueinvestorsclub.com/idea/ATLAS_FINANCIAL_HOLDINGS_INC/4764855798", group="atlas_common", direction="Long", raw_direction="Long", security="Atlas Financial common equity / Long", entry="$9.85", horizon="2015 earnings·book value", raw_horizon="2014 EPS $1.25~1.50; 2015 EPS ~$2; YE2015 BVPS $11~12; fair value $25~30",
    title="specialty-insurer premium/book growth Long", verdict="부분 성공 — 가격·premium 강함, 2015 EPS/BV target 과대", score=7.5, process=7.5,
    conclusion="$9.85에서 2015 high 약 $20.97로 가격은 상단 기준 2.13x였고 premium growth도 강했다. 2014 EPS $1.56은 range를 넘었지만 2015 EPS $1.13과 BVPS $10.15는 각각 약 $2, $11~12 목표를 놓쳤다. $25~30 fair value는 확인된 high 기준 미달했다.",
    t0="Q2 book 약 $6.07에서 $9.85에 거래되지만 hard-market premium growth, NOL allowance 해제, AM Best 개선과 operating leverage로 2014 EPS $1.25~1.50, 2015 약 $2, YE2015 BVPS $11~12와 $25~30 가치가 가능하다는 thesis였다.", reverse="시장은 빠른 premium growth가 capital과 reserve risk를 키우고 taxi severity·expense ratio가 earnings conversion을 방해할 가능성을 가격에 넣었다.",
    valuation="2015 EPS 약 $2에 12.5~15x를 적용한 $25~30 target와 BVPS $11~12의 약 2.1~2.7x P/B다. earnings quality가 reserve release가 아닌 accident-year underwriting에서 나와야 했다.",
    actual="2014 GPW $122.4m, diluted EPS $1.56, BVPS $9.08로 초기 earnings가 상회했다. 2015 GPW $209.3m으로 성장했지만 EPS $1.13, BVPS $10.15에 그쳤다. 2015 high 약 $20.97 뒤 2016 reserve strengthening $32.6m과 combined ratio 102.9%가 나타났다.",
    price="$20.97/$9.85=2.13x의 historical-high comparison, 약 +112.9%다. 이 수치는 종가·배당·매도 ledger가 아니므로 realized return으로 부르지 않는다. target $25~30 대비 high는 16.1~30.1% 낮았다.",
    drivers="premium과 2014 earnings surprise가 rerating을 만들었지만 reserve-adjusted profitability가 성장률을 따라가지 못해 2015 EPS·book와 target multiple이 미달했다.", counterfactual="2015 EPS $1.10, 1.5x stressed BVPS $10과 reserve charge를 적용하면 $9.85 entry의 기대수익은 충분했는가?", error="written-premium growth와 reported early EPS를 normalized earning power로 빠르게 자본화하고 reserve development의 lag를 약하게 stress했다.", warning="2015 EPS $1.13이 약 $2 목표를 43.5% 밑돈 시점에 earnings conversion thesis가 깨졌다.", first_signal_date="2016-03-16", lessons=LESSONS["atlas_common"], checklist=CHECKLIST["atlas_common"], scorecard=sc("premium 성공·reserve 혼합", "target $25~30 미달", "earnings surprise 후 둔화", "common 적절", "2014 성공·2015 미달"),
    scenarios=[("Bear", "reserve deterioration", "book·multiple 하락", "2016부터 현실화"), ("Base", "2015 EPS ~$2·BV $11~12", "$25~30", "미달"), ("Observed", "EPS $1.13·BV $10.15", "high ~$20.97", "부분 성공")],
    metrics=[("Entry/high", "$9.85", "$25~30", "high ~$20.97", "2.13x high; target 미달"), ("2014 EPS", "$1.25~1.50", "range", "$1.56", "상단 +4%"), ("2015 EPS", "약 $2.00", "$2.00", "$1.13", "-43.5%"), ("2015 BVPS", "$11~12", "$11~12", "$10.15", "-7.7%~-15.4%"), ("2015 GPW", "강한 성장", "premium scale", "$209.3m", "성공")],
    timeline=[("2013-09-22", "VIC Long", "$9.85"), ("2013-12", "GPW $93.1m", "growth base"), ("2014-12", "EPS $1.56", "range 상회"), ("2014-12", "BVPS $9.08", "book growth"), ("2015", "high 약 $20.97", "price rerating"), ("2015-12", "GPW $209.3m", "premium 급증"), ("2015-12", "EPS $1.13·BVPS $10.15", "targets 미달"), ("2016-12", "reserve strengthening $32.6m", "tail 확인")],
    claims=[
        claim("2014 EPS $1.25~1.50", "성공", "2014 diluted EPS가 range에 든다.", "premium growth와 operating leverage.", "earned premium pipeline.", "loss ratio와 expense ratio 개선.", "$1.10 미만이면 실패.", "$1.56.", "상단 +$0.06/+4%.", "단년 EPS를 정상화로 봄.", "accident-year underwriting으로 질을 확인한다."),
        claim("2015 EPS ~$2", "실패", "2015 EPS가 약 $2다.", "premium conversion과 fixed-cost leverage.", "hard-market growth.", "reserves가 충분하다.", "$1.50 미만이면 반증.", "$1.13.", "-$0.87/-43.5%.", "GPW와 EPS를 선형 연결.", "loss ratio·reserve development를 bridge한다."),
        claim("YE2015 BVPS $11~12", "미달", "retained earnings로 book가 $11~12.", "underwriting profit 누적.", "Q2 book 약 $6.07.", "dilution·reserve loss 제한.", "$10.50 미만이면 미달.", "$10.15.", "하단 -$0.85/-7.7%.", "reported EPS가 book로 그대로 남는다고 봄.", "OCI·capital·reserve movement를 잇는다."),
        claim("premium hard-cycle", "강한 성공", "competitor issues와 pricing으로 volume을 늘린다.", "niche capacity가 시장점유율을 얻는다.", "earned premium pipeline.", "underwriting standard 유지.", "growth 정체면 실패.", "GPW 2014 $122.4m→2015 $209.3m.", "+71.0%.", "growth와 profitability를 한 claim으로 묶을 위험.", "volume과 accident-year margin을 따로 score한다."),
        claim("$25~30 fair value", "미달", "earnings와 book rerating으로 $25~30.", "~$2 EPS와 12.5~15x.", "explicit valuation.", "earnings target 적중.", "2015 high <$25면 실패.", "high 약 $20.97.", "하단 대비 -16.1%.", "peak price를 정확히 검증하기 어려움.", "daily ledger 없으면 high comparison으로 제한한다."),
        claim("reserve adequacy", "실패", "성장에도 reserves가 충분하다.", "pricing과 claims expertise가 later charges를 막는다.", "sub-100% early CR.", "severity trend가 추정 내다.", "material charge면 반증.", "2016 $32.6m strengthening.", "material adverse development.", "short-tail 가정 과신.", "growth vintage별 loss triangles를 추적한다."),
    ],
)


add(
    id="0497fdbb-2e37-454f-9cb0-ab260fab5507", date="2021-12-29", author="mrsox977", ticker="AFHBL", company="Atlas Financial Holdings Inc.", filename="analysis/ideas/2021/2021-12-29_AFHBL_notes_long.md", source="", group="atlas_note", direction="Long", raw_direction="Long", security="6.625% Senior Unsecured Notes due 2022 / Long", entry="약 $10 per $25 par; 약 40 cents on par", horizon="2022 restructuring; ultimate recovery through 2027 maturity", raw_horizon="$25 par note at about $10; scheme/exchange catalyst and improved MGA liquidity",
    title="distressed senior-unsecured-note exchange Long", verdict="교환 성공·최종 recovery 미확정 — 2024 credit deterioration", score=5.5, process=7.5,
    conclusion="common이 아닌 AFHBL senior unsecured notes다. 99.34%가 scheme에 찬성했고 2022-04-14 old $25 plus accrued interest가 new 2027 notes principal로 교환됐다. 그러나 par-for-par principal은 cash recovery가 아니다. new notes는 6.625% cash/7.25% PIK이며 첫 이자는 PIK였다. 2024 core subsidiaries가 secured lender에 이전됐고 2027-04-27 maturity가 아직 미래라 최종 판정은 provisional이다.",
    t0="$25 par가 약 $10에 거래될 때 2022 maturity wall을 court scheme으로 넘기고, MGA cash flow가 회복되면 coupon과 principal recovery가 큰 upside를 만들 수 있다는 distressed-credit thesis였다.", reverse="시장은 unsecured priority, insufficient liquidity, restructuring coercion, PIK accumulation과 operating subsidiary assets가 secured creditors에게 빠질 위험을 반영했다.",
    valuation="$10 price는 $25 par의 40%다. 단순 par upside 2.5x는 recovery가 cash로 지급될 때만 성립한다. new principal, cash/PIK coupons, maturity extension과 senior claims를 날짜별 discounted cash flow로 계산해야 한다.",
    actual="scheme vote 99.34% 찬성 뒤 Cayman court가 2022-02-25 sanction했고 2022-04-14 exchange가 effective됐다. new notes initial principal은 $26,639,856, coupon은 cash 6.625% 또는 PIK 7.25%, maturity는 2027-04-27였다. 첫 interest payment는 PIK였다. 2024-01 core subsidiaries를 약 $12.7m secured debt satisfaction으로 넘겼다.",
    price="old note 약 $10와 $25 nominal new claim을 비교해 +150% realized gain으로 처리하지 않는다. coupon election·secondary price·principal payment가 완전히 확인되지 않았고 maturity는 research cutoff 뒤다. cash recovery ledger 완성 전 exact IRR은 금지한다.",
    drivers="court scheme은 near-term default를 피했지만 value creation보다 maturity extension이었다. PIK와 2024 secured-lender asset transfer가 unsecured coverage를 약화시켰다.", counterfactual="secured claims 뒤 realizable assets가 $12m, new-note principal이 $26.64m이고 3년간 PIK가 쌓이면 $10 purchase의 recovery multiple은 얼마인가?", error="legal completion을 economic recovery와 가깝게 취급하고 operating turnaround가 unsecured coverage로 전환되는 경로를 충분히 haircut하지 않았다.", warning="첫 interest가 PIK로 지급된 시점은 cash-generation 부족의 초기 경고였고, 2024-01 subsidiary transfer가 material credit break였다.", first_signal_date="2022-07-27", lessons=LESSONS["atlas_note"], checklist=CHECKLIST["atlas_note"], scorecard=sc("MGA 회복 미확정", "40c 가격은 optionality", "scheme 성공", "unsecured note 정확", "2027까지 provisional"),
    scenarios=[("Bear", "secured assets 이탈·low recovery", "<40c recovery", "2024 risk 증가"), ("Base", "maturity extension·부분 현금", "40~100c", "미확정"), ("Bull", "cash coupon·par payment", "2.5x principal+coupon", "아직 미실현")],
    metrics=[("Entry/par", "$10 / $25", "40c purchase", "new nominal principal", "realized recovery 아님"), ("Scheme vote", "pending", "approval", "99.34% 찬성", "성공"), ("New principal", "old par+accrual", "claim preserved", "$26.640m aggregate", "명목 성공"), ("Coupon", "old 6.625%", "cash servicing", "6.625% cash / 7.25% PIK; first PIK", "credit 경고"), ("Maturity", "2022", "extension", "2027-04-27", "연장·최종 미정")],
    timeline=[("2021-12-29", "VIC note Long", "약 $10/$25 par"), ("2022-02", "scheme vote 99.34%", "approval"), ("2022-02-25", "Cayman sanction", "legal condition"), ("2022-04-14", "exchange effective", "old notes cancelled"), ("2022-04-27", "new notes issued", "2027 maturity"), ("2022-07", "first interest PIK", "cash weakness"), ("2024-01-25", "core subsidiaries transferred", "coverage 악화"), ("2027-04-27", "contractual maturity", "research cutoff 뒤")],
    claims=[
        claim("security classification", "교정 성공", "AFHBL을 distressed debt로 산다.", "note priority·coupon·par가 common과 다른 payoff를 만든다.", "$25 par·6.625% note terms.", "exact indenture를 확인한다.", "common이면 thesis 단위 오류.", "senior unsecured note로 확인.", "security 정확.", "ticker만으로 common 취급 위험.", "CUSIP·indenture·par를 먼저 고정한다."),
        claim("scheme approval", "강한 성공", "court scheme이 maturity wall을 넘긴다.", "supermajority vote와 sanction이 default를 연기.", "negotiated restructuring.", "creditor vote·court approval.", "vote 실패면 terminal default risk.", "99.34% 찬성·court sanction.", "legal catalyst 완결.", "legal success와 value success 혼동.", "event와 recovery를 다른 claim으로 둔다."),
        claim("par-for-par exchange", "명목 성공", "old $25+accrual이 new principal로 보존된다.", "claim amount가 취소 대신 재발행.", "exchange terms.", "issuer가 2027에 지급 가능.", "deep discount/PIK/default면 economic failure.", "$26.640m aggregate new principal.", "face preserved, cash $0 at exchange.", "principal notation을 recovery로 오인.", "cash receipt 전 par 회수로 쓰지 않는다."),
        claim("cash coupon", "약화", "MGA cash flow가 6.625% coupon을 낸다.", "operating cash가 holding-company debt service.", "cash/PIK option.", "subsidiary cash upstream 가능.", "PIK election이면 경고.", "first payment 7.25% PIK.", "cash servicing 미실현.", "toggle 구조의 issuer option을 과소평가.", "PIK는 principal 증가와 liquidity 부족을 동시에 기록한다."),
        claim("asset coverage", "실패 위험 확대", "operating subsidiaries가 unsecured note를 지지한다.", "residual enterprise value가 senior claims 뒤 note에 귀속.", "MGA platform.", "secured lender가 assets를 가져가지 않는다.", "core asset transfer면 coverage 급락.", "2024 core subsidiaries를 ~$12.7m secured debt와 교환.", "unsecured collateral pool 축소.", "holding/sub structure를 단순화.", "entity별 assets와 guarantees를 매핑한다."),
        claim("ultimate par recovery", "미확정", "$10 purchase가 $25 principal로 회수된다.", "2027 maturity payment.", "2.5x nominal upside.", "2027 liquidity와 solvency.", "maturity nonpayment면 실패.", "research cutoff 2026-09-18 현재 미래.", "판정 불가.", "완료 전 승리 선언 위험.", "maturity cash ledger까지 provisional로 둔다."),
    ],
)


add(
    id="262f4617-ca50-4aa0-81a2-574eb9e94281", date="2021-04-12", author="casper719", ticker="AFHIF", company="Atlas Financial Holdings Inc.", filename="analysis/ideas/2021/2021-04-12_AFHIF_long.md", source="", group="atlas_common", direction="Long", raw_direction="Short", security="Atlas Financial OTC common equity / Long", entry="distressed OTC common; exact verified price ledger 없음", horizon="2~4년 MGA pivot", raw_horizon="legacy insurance runoff, capital-light MGA recovery and 10x+ common option",
    title="insurer-to-MGA common-option Long", verdict="강한 실패 — secured debt가 common residual을 압도", score=1.5, process=3.0,
    conclusion="raw Short를 실제 Long으로 교정했다. capital-light MGA business와 National Interstate/Buckle partnerships는 사업가치 가능성을 만들었지만, holding-company debt와 liquidity가 common 앞에 있었다. 2022 note exchange로 시간을 벌었으나 2024 core Anchor/UBI subsidiaries를 secured lender에 넘겼고 common residual thesis가 사실상 붕괴했다.",
    t0="과거 GPW $300m+ 규모의 specialty insurance distribution을 legacy carrier risk 없이 MGA로 재구축하면 fee economics와 10x+ common optionality가 가능하다는 논지였다. National Interstate와 Buckle capacity relationships가 재출발의 기반이었다.", reverse="시장은 legacy liabilities, overdue filings, debt overhang, thin cash와 insurer에서 MGA로 옮기는 동안의 revenue gap 때문에 business quality보다 security insolvency를 가격에 넣었다.",
    valuation="common option은 MGA enterprise value - secured debt - unsecured notes - holding costs - dilution이다. 과거 premium base나 revenue multiple을 common에 바로 적용하면 안 되며, subsidiary cash upstream과 debt waterfall이 먼저다.",
    actual="2021 preliminary operating indicators는 applications·policies 증가를 시사했지만 former paratransit를 뺀 2021 GWP는 약 $9.3m로 과거 $285m+와 거리가 컸다. 2022 notes restructuring으로 maturity가 연장됐고 2024-01 minimum-liquidity default 뒤 core operating subsidiaries가 secured lender로 이전됐다.",
    price="OTC price series, reverse-split·deregistration·distribution ledger가 완전하지 않아 exact return을 만들지 않는다. 핵심 operating assets가 senior creditor에게 이전돼 common의 residual claim이 훼손된 capital-structure outcome으로 판정한다.",
    drivers="MGA의 gross economics가 아니라 holding-company liabilities와 liquidity runway가 결과를 결정했다. 사업 recovery가 충분히 빠르지 않아 secured lender가 core assets를 가져갔다.", counterfactual="MGA가 $20m revenue·20% EBITDA margin에 도달해도 secured/unsecured claims와 holding costs를 뺀 common equity가 양수였는가?", error="asset-light operating model을 asset-light security로 착각하고 past GPW를 recoverable distribution capacity로 사용했으며 creditor priority와 reporting/default clock을 부차화했다.", warning="2021 GWP 약 $9.3m이 과거 scale 대비 극히 작고 note restructuring이 필요해진 시점에 10x common thesis의 time-to-scale가 liquidity runway를 넘었다.", first_signal_date="2022-03-01", lessons=LESSONS["atlas_common"], checklist=CHECKLIST["atlas_common"], scorecard=sc("MGA scale 미달", "common waterfall 음수", "restructuring은 연장뿐", "common 부적절", "runway failure"),
    scenarios=[("Bear", "scale 미달·secured enforcement", "common residual 0", "2024 현실화"), ("Base", "작은 MGA·debt extension", "limited option", "2022만 실현"), ("Bull", "old scale 회복", "10x+ common", "실패")],
    metrics=[("Historical GPW", ">$285m / peak $300m+", "일부 회복", "2021 ex-paratransit GWP ~$9.3m", "약 97% 낮음"), ("Business model", "carrier→MGA", "capital-light", "partnerships 존재", "운영만 부분"), ("Debt maturity", "overhang", "refinance", "2022 exchange→2027", "시간 연장"), ("Liquidity", "tight", "MGA self-funding", "minimum-liquidity default", "실패"), ("Core assets", "common value 기반", "보존", "2024 secured lender 이전", "terminal common break")],
    timeline=[("2021-04-12", "VIC Long", "raw Short 교정"), ("2021", "MGA partnerships", "operating option"), ("2021-12", "GWP 약 $9.3m", "scale gap"), ("2022-02", "note scheme 승인", "runway extension"), ("2022-04-14", "note exchange", "debt remains"), ("2023", "reporting/liquidity pressure", "common risk"), ("2024-01", "minimum-liquidity default", "creditor control"), ("2024-01-25", "core subsidiaries transfer", "common thesis break")],
    claims=[
        claim("raw Short", "metadata 실패", "source SQL은 Short다.", "방향이 payoff 해석을 바꾼다.", "원문은 10x+ common upside를 제시.", "본문이 기준이다.", "downside bet이면 Short.", "실제는 common Long.", "완전 반대.", "raw flag 의존.", "원문 payoff로 교정한다."),
        claim("capital-light MGA pivot", "부분 성공", "carrier risk를 버리고 MGA fee model로 전환한다.", "보험위험 대신 commission income을 얻는다.", "capacity partnerships.", "carrier capacity와 distribution 유지.", "partner 이탈·premium scale 부재면 실패.", "National Interstate/Buckle 관계는 있었으나 scale 작음.", "구조는 성립, 규모 미달.", "모델 전환을 economics 확보로 간주.", "partner별 premium·commission·retention을 본다."),
        claim("premium-base recovery", "강한 실패", "과거 $300m+ premium distribution의 일부를 회복한다.", "agents·niche expertise가 volume을 되찾는다.", "historical franchise.", "licenses·partners·customers가 남아 있다.", "2년 내 <$50m이면 실패.", "2021 GWP 약 $9.3m ex former paratransit.", "과거 $285m 대비 약 -96.7%.", "과거 peak를 available demand로 봄.", "현재 funnel과 capacity로만 forecast한다."),
        claim("note restructuring", "법적 성공·경제 제한", "debt wall을 넘겨 common runway를 만든다.", "maturity extension이 operating ramp 시간을 준다.", "scheme proposal.", "PIK와 senior debt가 common을 잠식하지 않는다.", "restructuring 뒤에도 liquidity default면 실패.", "2022 exchange 성공, 2024 default.", "약 21개월 뒤 break.", "extension을 deleveraging으로 해석.", "principal·PIK·security를 pro forma로 갱신한다."),
        claim("10x+ common option", "실패", "작은 common이 MGA EV에 levered upside를 가진다.", "enterprise value가 debt stack을 크게 넘는다.", "past scale와 asset-light multiple.", "빠른 EBITDA ramp·낮은 dilution.", "core asset loss면 terminal failure.", "2024 core subsidiaries 이전.", "residual engine 상실.", "EV에서 claims 차감 불충분.", "waterfall 뒤 common만 평가한다."),
        claim("liquidity runway", "실패", "runway가 MGA 회복까지 충분하다.", "cash·refinancing이 burn을 견딘다.", "restructuring path.", "time-to-scale < runway.", "minimum-liquidity default면 반증.", "2024 default와 asset transfer.", "명시적 반증 발생.", "사업 turnaround clock을 debt clock보다 앞세움.", "monthly liquidity와 covenant calendar를 둔다."),
    ],
)


add(
    id="85df04ed-ab7e-4059-b9f2-d4313dabcd78", date="2020-12-13", author="Hvitserk", ticker="AFHP LN", company="AFH Financial Group Plc", filename="analysis/ideas/2020/2020-12-13_AFHP_LN_long.md", source="https://www.valueinvestorsclub.com/idea/AFH_Financial_Group/6482598516", group="afhp", direction="Long", raw_direction="Long", security="AFH Financial Group AIM-listed common equity / Long", entry="약 330p", horizon="2~5년 earnings; takeout는 6개월 내", raw_horizon="약 10x P/E; cash-flow normalization; fair value 500~600p",
    title="UK IFA consolidator value Long", verdict="강한 성공 — 330p→480p cash scheme", score=9.0, process=8.5,
    conclusion="약 330p와 10x P/E에서 500~600p fair value를 제시한 뒤, 2021-01 recommended bid 463p가 나왔고 2021-03 480p로 상향됐다. scheme은 2021-06 effective가 됐다. 480/330-1=45.5% 단순 price gain이며 배당·세금·정확 settlement를 포함한 IRR은 아니다.",
    t0="IFA roll-up의 acquisition accounting과 cash-flow timing 때문에 earnings quality가 과소평가됐고 약 10x P/E, 330p에서 recurring advice economics와 500~600p value를 살 수 있다는 thesis였다.", reverse="시장은 adviser retention, acquisition integration, regulatory liabilities, contingent consideration과 accounting profit의 낮은 cash conversion을 할인했다.",
    valuation="500~600p는 entry 대비 51.5~81.8% upside였다. standalone earnings normalization이 base이고 takeout은 별도 option이어야 했다. 실제 480p bid는 원 target 하단보다 4% 낮지만 매우 짧은 시간에 현금화됐다.",
    actual="Cortina Bidco/Flexpoint Ford는 2021-01 463p recommended cash offer를 제시했고 2021-03 consideration을 480p로 높였다. court sanction 뒤 2021-06 scheme이 effective가 되어 common은 cash consideration으로 종결됐다.",
    price="480p/330p-1=45.5% 단순 gain이다. 약 6개월의 정확 purchase/settlement date, dividends와 tax가 없으므로 exact annualized IRR은 계산하지 않는다.",
    drivers="standalone recurring-fee franchise와 낮은 public valuation이 financial buyer의 integration·private ownership synergies와 결합해 빠른 cash catalyst를 만들었다.", counterfactual="bid가 없고 EPS가 10%만 성장하며 10x multiple이 유지돼도 330p에서 downside-adjusted return이 만족스러웠는가?", error="결과는 좋았지만 bidder premium을 T0 earnings thesis의 정확한 적중으로 전부 돌리면 안 된다. standalone value와 control value를 분리해야 한다.", warning="bid가 나온 뒤 핵심 risk는 운영이 아니라 scheme vote·court·financing 조건이었다. 480p 상향과 sanction으로 break risk가 줄었다.", first_signal_date="2021-01-25", lessons=LESSONS["afhp"], checklist=CHECKLIST["afhp"], scorecard=sc("buyer가 franchise 확인", "target 하단 근접", "cash bid 성공", "common 적절", "6개월 내 성공"),
    scenarios=[("Bear", "bid 없음·cash conversion 약화", "10x earnings 정체", "미발생"), ("Base", "standalone normalization", "500p 부근", "takeout로 선반영"), ("Event", "recommended cash bid", "480p cash", "실현")],
    metrics=[("Entry", "330p", "500~600p", "480p cash", "+45.5% 단순"), ("P/E", "약 10x", "rerating", "control bid", "성공"), ("Initial bid", "없음", "optional", "463p", "+40.3% vs entry"), ("Revised bid", "463p", "상향", "480p", "+3.7% vs initial"), ("Target gap", "500~600p", "하단 500p", "480p", "하단 -4.0%")],
    timeline=[("2020-12-13", "VIC Long", "약 330p"), ("2021-01-25", "463p recommended bid", "catalyst"), ("2021-03-02", "bid 480p로 상향", "value 개선"), ("2021-04", "scheme documents", "조건 구체화"), ("2021-05", "shareholder process", "event risk 감소"), ("2021-06", "court sanction", "마지막 조건"), ("2021-06", "scheme effective", "cash payoff"), ("후속", "listing 종료", "terminal event")],
    claims=[
        claim("~10x P/E cheapness", "성공", "quality IFA가 약 10x P/E로 싸다.", "recurring fees와 cash normalization이 higher multiple을 지지.", "T0 valuation.", "earnings·cash conversion 유지.", "profit collapse면 반증.", "buyer가 480p control value를 지급.", "entry 대비 +45.5%.", "bid price가 standalone multiple을 직접 증명하진 않음.", "standalone과 control value를 분리한다."),
        claim("cash-flow normalization", "간접 성공", "accounting timing 뒤 cash가 드러난다.", "integration·deferred consideration 소멸.", "recurring client revenue.", "adviser/client retention.", "cash conversion 악화면 실패.", "6개월 내 buyer diligence를 통과.", "독립 장기 ledger 전에 takeout.", "buyer 결정을 operating proof로 과대해석.", "transaction outcome은 간접 검증으로 표기한다."),
        claim("500~600p fair value", "근접·하단 미달", "standalone value가 500~600p.", "earnings normalization과 rerating.", "explicit range.", "공개시장 또는 bidder가 value 인정.", "cash bid <450p면 약화.", "480p.", "하단 -20p/-4%; 상단 -120p/-20%.", "range가 control premium 포함 여부 모호.", "standalone·control targets를 나눈다."),
        claim("initial 463p bid", "강한 성공", "external catalyst가 value를 닫을 수 있다.", "buyer가 public discount를 현금화.", "consolidation appeal.", "financing·board support.", "deal 없음이면 option 0.", "463p recommended offer.", "entry 대비 +40.3%.", "takeout을 base에 넣을 위험.", "probability-weighted option으로 둔다."),
        claim("480p increased offer", "강한 성공", "competitive/process pressure가 consideration을 높인다.", "shareholder support 확보.", "initial bid와 company value.", "bidder가 terms 개선.", "463p 고정이면 추가 upside 없음.", "480p로 17p 상향.", "+3.7% vs initial.", "작은 상향을 운영 alpha로 오인.", "event return을 별도 ledger로 둔다."),
        claim("scheme completion", "강한 성공", "cash offer가 실제 종결된다.", "vote·court·effective date 통과.", "recommended scheme.", "conditions 충족.", "vote/court failure면 반증.", "2021-06 effective.", "terminal cash payoff.", "announcement price를 realized로 조기 간주.", "effective date까지 completion risk를 추적한다."),
    ],
)


add(
    id="7fe82576-de93-4f60-9527-8d401c74e246", date="2016-09-21", author="rjm59", ticker="AFI", company="Armstrong Flooring Inc.", filename="analysis/ideas/2016/2016-09-21_AFI_long.md", source="https://www.valueinvestorsclub.com/idea/Armstrong_Flooring_Inc._/3222811552", group="afi", direction="Long", raw_direction="Long", security="Armstrong Flooring common equity / Long", entry="약 $18.90", horizon="2017~2018 EBITDA normalization", raw_horizon="spin-off focus; EBITDA $80m→$100m→$120m; long-term revenue growth 5.5% and EBITDA margin 10%",
    title="flooring spin-off manufacturing-turnaround Long", verdict="강한 실패 — EBITDA normalization 붕괴·2022 Chapter 11", score=1.5, process=3.5,
    conclusion="spin-off focus, LVT growth와 utilization/cost improvement는 잠깐의 2017 price strength를 만들었지만 $100m 2017·$120m 2018 EBITDA path는 지속되지 않았다. Armstrong Flooring은 2022-05-08 Chapter 11을 신청했고 세 지역 자산을 매각한 뒤 SEC filing에서 existing equity가 likely no recovery라고 밝혔다.",
    t0="약 $18.90에서 parent 분리 뒤 management focus, LVT mix, 공장 utilization과 cost takeout으로 EBITDA를 2016 약 $80m에서 2017 $100m, 2018 $120m으로 높이고 long-term 10% margin을 달성한다는 thesis였다.", reverse="시장은 secular product mix change, legacy plant footprint, raw-material/freight volatility와 housing/commercial cyclicality가 spin-off focus보다 강해 cash를 소진할 위험을 반영했다.",
    valuation="normalized EBITDA에 peer multiple을 적용하는 thesis지만 maintenance capex·working capital·debt를 빼야 common 가치다. $120m EBITDA가 나오기 전 liquidity와 downside EBITDA를 함께 모델링했어야 한다.",
    actual="주가는 2017년 약 $21까지 잠시 상승했지만 운영은 악화했고 2022-05-08 Chapter 11을 신청했다. North America assets $107m, Australia $31m, Asia $59m에 매각됐으며 2022-08-23까지 substantially all asset sales가 완료됐다. 회사는 common holders가 likely no recovery라고 공시했다.",
    price="약 $18.90 entry와 잠깐의 2017 ~$21 high는 thesis 성공이 아니다. bankruptcy waterfall에서 existing equity likely no recovery가 terminal outcome이다. exact realized loss는 매도시점 ledger가 없으므로 계산하지 않는다.",
    drivers="LVT 성장과 cost initiatives보다 legacy footprint, weak profitability, working-capital·capex와 leverage가 컸다. 정상화가 오기 전에 liquidity가 소진돼 senior claims가 asset-sale proceeds를 흡수했다.", counterfactual="EBITDA가 $60m에 머물고 maintenance capex·working capital·interest 뒤 FCF가 0이면 $18.90 common의 downside와 covenant runway는 얼마인가?", error="activist/management EBITDA targets를 capacity-based upside로 받아들이고 cash conversion, covenant headroom과 secular product/customer changes를 약하게 검증했다.", warning="2017 EBITDA가 $100m path를 확인하지 못하고 price bounce 뒤 operating deterioration가 이어진 시점이 첫 break였다.", first_signal_date="2018-03-06", lessons=LESSONS["afi"], checklist=CHECKLIST["afi"], scorecard=sc("사업 deteriorated", "normalized EBITDA 과대", "cost/LVT catalyst 실패", "common 최하위", "장기 terminal failure"),
    scenarios=[("Bear", "EBITDA <$60m·cash burn", "distress", "현실화"), ("Base", "$100m→$120m EBITDA", "rerating", "실패"), ("Terminal", "Chapter 11·asset sales", "common likely 0", "2022 현실화")],
    metrics=[("Entry", "약 $18.90", "rerating", "2017 ~$21 뒤 collapse", "일시 +11% high"), ("2017 EBITDA", "$100m", "$100m", "지속 normalization 미확인", "실패"), ("2018 EBITDA", "$120m", "$120m", "미달", "실패"), ("Long-term margin", "10%", "10%", "distress", "실패"), ("Asset-sale proceeds", "going-concern upside", "equity value", "$107m+$31m+$59m", "senior waterfall; equity likely 0")],
    timeline=[("2016-09-21", "VIC Long", "약 $18.90"), ("2017", "price 약 $21", "short bounce"), ("2018-03", "normalization 지연", "first break"), ("2019", "loss·cash pressure", "thesis 악화"), ("2020", "pandemic disruption", "liquidity 부담"), ("2021", "strategic alternatives", "distress"), ("2022-05-08", "Chapter 11", "common terminal break"), ("2022-08-23", "asset sales 완료", "equity likely no recovery")],
    claims=[
        claim("spin-off focus", "실패", "독립경영이 execution을 개선한다.", "capital allocation·accountability가 빨라진다.", "fresh separation.", "legacy dis-synergies가 작다.", "2년 내 margin 개선 없으면 실패.", "operating deterioration·bankruptcy.", "지속 개선 없음.", "focus를 economics로 동일시.", "standalone costs와 systems를 먼저 차감한다."),
        claim("LVT growth", "부분·불충분", "LVT가 company growth를 이끈다.", "고성장 product mix가 volume·margin을 높인다.", "market category growth.", "AFI가 share와 economics를 확보.", "category 성장에도 company EBITDA 미달이면 약화.", "turnaround 전체를 구하지 못함.", "category tailwind≠company return.", "category growth를 company economics로 외삽.", "시장 성장과 company share·gross margin을 분리한다."),
        claim("2017 EBITDA $100m", "실패", "cost·utilization으로 EBITDA $100m.", "volume·fixed-cost leverage.", "2016 약 $80m bridge.", "price/mix와 cost savings 실현.", "$85m 미만이면 실패.", "지속 가능한 $100m path 미확인.", "target miss.", "add-backs와 savings 중복 가능.", "reported-to-adjusted bridge를 검증한다."),
        claim("2018 EBITDA $120m", "강한 실패", "2018 EBITDA $120m.", "LVT·commercial recovery·cost takeout 누적.", "activist forecast.", "liquidity가 ramp를 지원.", "2018 FCF 음수면 반증.", "사업은 장기 distress 방향.", "normalization 미실현.", "peak margin anchoring.", "base rate와 downside EBITDA를 우선한다."),
        claim("10% long-term margin", "실패", "매출성장 5.5%·margin 10%.", "scale와 mix.", "company aspirations.", "competitive pricing·plant utilization 양호.", "gross margin·FCF 악화면 실패.", "bankruptcy 전 profitability 붕괴.", "목표와 terminal outcome 반대.", "장기 target에 deadline 없음.", "milestone calendar와 cash runway를 둔다."),
        claim("common recovery", "terminal 실패", "enterprise recovery가 common에 귀속된다.", "EV가 debt·claims를 넘는다.", "normalized EBITDA valuation.", "liquidity와 debt service 충분.", "Chapter 11·equity no recovery면 반증.", "2022 filing이 likely no recovery 명시.", "residual 거의 0.", "EV upside만 보고 priority 무시.", "distress에서는 waterfall을 먼저 계산한다."),
    ],
)


add(
    id="3c3375d2-550b-42e0-98d1-25a1c4e0d716", date="2021-08-25", author="uncleM", ticker="AFI", company="Armstrong Flooring Inc.", filename="analysis/ideas/2021/2021-08-25_AFI_long.md", source="", group="afi", direction="Long", raw_direction="Long", security="Armstrong Flooring common equity / Long", entry="약 $3.50", horizon="FY2023 normalization", raw_horizon="FY2023 revenue ~$744m, EBITDA ~$52m/7% margin, target $12+",
    title="distressed flooring-turnaround Long", verdict="매우 강한 실패 — 약 8.5개월 내 Chapter 11", score=0.8, process=2.5,
    conclusion="new CEO, sales reps, products와 commercial recovery로 FY2023 revenue 약 $744m·EBITDA $52m을 기대했지만, 회사는 게시 약 8.5개월 뒤인 2022-05-08 Chapter 11을 신청했다. substantially all assets가 매각됐고 existing equity는 likely no recovery였다. 핵심 오류는 time-to-repair가 liquidity runway보다 길었던 것이다.",
    t0="약 $3.50에서 turnaround가 성공하면 FY2023 revenue 약 $744m, EBITDA 약 $52m·7% margin과 $12+ target가 가능하다는 levered-equity thesis였다. new CEO, expanded sales force, new products와 commercial end-market recovery가 촉매였다.", reverse="시장은 지속 cash burn, raw material·freight inflation, customer loss, weak balance sheet와 refinancing 의존 때문에 정상화 전에 liquidity가 끝날 가능성을 가격에 넣었다.",
    valuation="$12 target는 entry 대비 3.43x였지만 $52m EBITDA에 multiple을 적용한 뒤 net debt, restructuring needs와 dilution을 차감해야 했다. 특히 quarterly cash burn으로 runway를 계산하고 FY2023까지 살아남는지 먼저 검증해야 했다.",
    actual="turnaround milestone에 도달하기 전 2022-05-08 Chapter 11을 신청했다. North America assets는 $107m, Australia $31m, Asia $59m에 매각됐고 2022-08-23 substantially all sales가 완료됐다. SEC filing은 existing equity holders가 likely no recovery라고 밝혔다.",
    price="$3.50에서 $12+ 목표는 실현되지 않았다. bankruptcy 뒤 common likely no recovery가 terminal security outcome이다. interim trading path가 완전히 복원되지 않아 exact holding-period loss나 IRR은 계산하지 않는다.",
    drivers="매출·margin 정상화 속도보다 현금소진·공급망·원가·debt clock이 빨랐다. 사업계획이 맞을 가능성이 일부 있어도 common은 그 결과를 기다릴 기간을 보유하지 못했다.", counterfactual="quarterly cash burn이 유지되고 EBITDA 개선이 2개 분기 지연될 때 cash+revolver가 FY2023까지 버티는가?", error="management actions와 terminal EBITDA를 상세히 모델링하면서도 monthly liquidity, covenant·vendor terms와 restructuring probability를 최우선 gate로 두지 않았다.", warning="2021 하반기에도 cash burn과 liquidity pressure가 개선되지 않은 순간, FY2023 normalization보다 financing event가 앞설 것이 관찰 가능했다.", first_signal_date="2021-11-04", lessons=LESSONS["afi"], checklist=CHECKLIST["afi"], scorecard=sc("turnaround 이전 파산", "$52m denominator 무효", "CEO/products 시간 부족", "common 최하위", "8.5개월 terminal failure"),
    scenarios=[("Bear", "runway <12개월", "Chapter 11·equity 0", "현실화"), ("Base", "FY2023 EBITDA $52m", "$12+", "도달 전 파산"), ("Bull", "7%+ margin·rerating", "multi-bagger", "미실현")],
    metrics=[("Entry/target", "$3.50", "$12+", "common likely no recovery", "target 실패"), ("FY2023 revenue", "약 $744m", "$744m", "파산 전 도달 못함", "실패"), ("FY2023 EBITDA", "약 $52m", "$52m", "파산 전 도달 못함", "실패"), ("EBITDA margin", "7%", "7%", "distress", "실패"), ("Runway", "FY2023까지 필요", ">~28개월", "Chapter 11까지 ~8.5개월", "약 19개월+ 부족")],
    timeline=[("2021-08-25", "VIC Long", "약 $3.50"), ("2021-Q3", "inflation·supply pressure", "cash risk"), ("2021-11-04", "liquidity warning", "first break"), ("2021-Q4", "turnaround 지연", "runway 축소"), ("2022-Q1", "strategic financing 필요", "distress"), ("2022-05-08", "Chapter 11", "약 8.5개월"), ("2022-08", "regional asset sales", "senior recovery"), ("2022-08-23", "substantially all sales complete", "equity likely 0")],
    claims=[
        claim("FY2023 revenue $744m", "실패", "salesforce·products·market recovery가 revenue를 $744m로 높인다.", "volume과 commercial channel 회복.", "management initiatives.", "customers와 capacity가 현금부족 전에 반응.", "financing event가 FY2023보다 먼저면 실패.", "2022-05 Chapter 11.", "target date 약 19개월+ 전에 terminal event.", "revenue plan 앞에 solvency gate 부재.", "runway 통과 후에만 revenue target를 평가한다."),
        claim("FY2023 EBITDA $52m", "강한 실패", "7% margin으로 EBITDA 약 $52m.", "price/mix·cost absorption.", "$744m×7%≈$52m.", "inflation pass-through·utilization 회복.", "cash EBITDA가 계속 음수면 반증.", "normalization 전에 파산.", "$52m denominator 미실현.", "terminal margin anchoring.", "분기별 gross-to-cash EBITDA bridge를 둔다."),
        claim("new CEO execution", "불충분", "새 CEO가 조직과 비용을 빠르게 고친다.", "accountability·portfolio actions.", "leadership change.", "권한보다 liquidity 시간이 충분.", "12개월 내 restructuring이면 timing 실패.", "약 8.5개월 내 Chapter 11.", "실행기간 없음.", "사람을 balance-sheet solution으로 봄.", "CEO catalyst와 financing catalyst를 분리한다."),
        claim("sales reps·new products", "불충분", "상업투자가 demand와 mix를 회복한다.", "coverage와 innovation이 orders를 늘린다.", "go-to-market plan.", "CAC·inventory가 단기 cash를 악화시키지 않는다.", "working-capital burn이 가속하면 실패.", "결과를 기다리기 전 liquidity 소진.", "operating evidence 미실현.", "성장투자의 upfront cash를 과소평가.", "cohort payback과 inventory cycle을 본다."),
        claim("$12+ target", "실패", "EBITDA recovery가 common을 3.4x 올린다.", "EV/EBITDA leverage.", "$3.50 entry와 $52m target.", "net debt·dilution·bankruptcy risk 통제.", "Chapter 11이면 terminal failure.", "equity likely no recovery.", "목표와 거의 전액 손실 방향.", "enterprise upside를 equity에 바로 적용.", "stressed waterfall 뒤 target를 계산한다."),
        claim("liquidity runway", "강한 실패", "회사는 FY2023 turnaround까지 생존한다.", "cash·revolver·vendor credit가 burn을 자금조달.", "ongoing turnaround plan.", "runway가 time-to-repair보다 길다.", "12개월 내 filing이면 반증.", "8.5개월 내 filing.", "사전 반증선보다 빠름.", "runway를 부차 KPI로 둠.", "distressed turnaround의 첫 gate는 monthly liquidity다."),
    ],
)


ORDER = [
    "74afc0f3-c1cc-42f0-8759-65d207b26fb1",
    "b831bcd3-82aa-4fe6-97b7-582bc636de44",
    "da44c9d8-3ef2-48d8-b4e9-0f004b755947",
    "cc7be7f0-3b67-44c5-baba-eaeb3ada5a33",
    "97762eda-4350-4f09-bad7-ca22a7255d61",
    "0497fdbb-2e37-454f-9cb0-ab260fab5507",
    "262f4617-ca50-4aa0-81a2-574eb9e94281",
    "85df04ed-ab7e-4059-b9f2-d4313dabcd78",
    "7fe82576-de93-4f60-9527-8d401c74e246",
    "3c3375d2-550b-42e0-98d1-25a1c4e0d716",
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
        "# Batch 068 — AFCE / AFFY / AF Gruppen / Atlas Financial / AFH Financial / Armstrong Flooring V9 Index", "",
        "> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. raw direction, legal entity, exact security와 payoff를 먼저 고정하고 1차자료로 actual을 검증했다.", "",
        "## Canonical idea files", "", "| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## Direction / security / return audit", "",
        "- AFCE 2012, AFFY 2016, AFHIF 2021의 raw Short를 원문 payoff 기준 실제 Long으로 교정했다.",
        "- AFHBL은 common이 아니라 $25 par의 6.625% senior unsecured notes due 2022다. 2022 exchange 뒤 6.625% cash/7.25% PIK notes due 2027이 됐다.",
        "- Atlas 2012 entry $1.77는 2013 1-for-3 reverse split 뒤 $5.31 equivalent다.",
        "- source SQL performance row가 10건 모두 없으므로 exact return을 생성하지 않았다. cash consideration, reported high, operating actual과 bankruptcy waterfall만 제한적으로 사용했다.", "",
        "## 핵심 판정", "",
        "1. AFCE는 FY2012 EPS·SSS·net openings가 모두 적중했고 2017 $79 cash deal로 장기 brand value도 실현됐다.",
        "2. AFFY는 큰 NOL face value에도 profitable taxable income과 거래가 없으면 가치가 없다는 negative case다.",
        "3. AF Gruppen은 backlog·cash·balance sheet는 강했지만 2024 revenue·margin path를 놓쳤다. quality와 valuation success를 분리했다.",
        "4. Atlas 2012·2013 common은 초기 premium·book rerating이 성공했으나 2016 reserve strengthening이 growth의 tail을 드러냈다.",
        "5. Atlas 2021 common과 AFHBL notes는 같은 issuer라도 payoff가 다르다. common은 2024 core-asset transfer로 실패했고 note recovery는 2027까지 미확정이다.",
        "6. AFH Financial은 480p cash scheme으로 빠르게 성공했다. Armstrong 두 Long은 liquidity runway가 operating repair보다 짧아 Chapter 11로 끝났다.", "",
        "## 구조화 데이터", "",
        "- `data/curated/batch_068_afce_affy_afg_afh_afhp_afi_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.",
        "- `data/curated/batch_068_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.",
        "- `analysis/batch_068_afce_affy_afg_afh_afhp_afi_10.md`: Streamlit wrapper.", "",
    ])


def main():
    IDEAS.sort(key=lambda i: ORDER.index(i["id"]))
    if [i["id"] for i in IDEAS] != ORDER:
        raise ValueError("Batch 068 idea order or IDs do not match catalog boundary")
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
            "**C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·bankruptcy waterfall만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.",
        )
        report_path.write_text(report, encoding="utf-8")

    (ROOT / "analysis/batch_068_v9_index.md").write_text(render_index(), encoding="utf-8")
    parts = [i["filename"].removeprefix("analysis/") for i in IDEAS]
    wrapper = (
        "# Batch 068 — AFCE / AFFY / AF Gruppen / Atlas Financial / AFH Financial / Armstrong Flooring V9\n\n"
        f"<!-- batch_parts: {'|'.join(parts)} -->\n\n"
        "> Streamlit 호환 wrapper다. canonical index: [Batch 068 V9 Index](batch_068_v9_index.md).\n"
    )
    (ROOT / "analysis/batch_068_afce_affy_afg_afh_afhp_afi_10.md").write_text(wrapper, encoding="utf-8")

    payload = base.make_payload()
    payload["batch"] = 68
    payload["title"] = "AFCE / AFFY / AF Gruppen / Atlas Financial / AFH Financial / Armstrong Flooring — Security, Reserve, Catalyst and Runway V9"
    payload["metadata_audit"] = {
        "direction_corrections": 3,
        "company_mapping_corrections": 0,
        "security_type_corrections": 1,
        "cross_batch_duplicates_removed": 0,
        "performance_rows_rejected": 10,
        "corporate_action_terminal_payoffs": 4,
        "notes": [
            "AFCE 2012, AFFY 2016, AFHIF 2021 raw Short를 실제 Long으로 교정하되 raw flag를 보존했다.",
            "AFHBL을 common이 아니라 6.625% senior unsecured notes due 2022로 교정했고 2027 PIK-toggle new notes까지 연결했다.",
            "Atlas common 2012 entry와 per-share figures는 1-for-3 reverse split basis로 통일했다.",
            "source SQL performance row 10건은 모두 부재하므로 exact total return·IRR을 생성하지 않았다.",
            "AFHBL par-for-par exchange는 cash recovery로 간주하지 않았고 2027 maturity 전 최종 판정을 보류했다.",
            "Armstrong asset-sale proceeds는 common recovery가 아니라 priority waterfall의 enterprise proceeds로 처리했다.",
        ],
    }
    payload["batch_lessons"] = [
        "NOL face value는 cash가 아니며 taxable income·세율·Section 382·거래확률·시간을 곱해야 한다.",
        "backlog는 revenue가 아니고 revenue는 profit가 아니며 project margin과 cash conversion까지 이어야 한다.",
        "보험 growth는 reserve-development lag를 통과한 뒤에만 book compounding으로 인정한다.",
        "같은 issuer common과 unsecured note는 별도 waterfall과 catalyst를 가진다.",
        "distressed exchange의 nominal par preservation은 realized recovery가 아니다.",
        "turnaround는 time-to-repair가 liquidity runway보다 짧을 때만 equity thesis가 된다.",
        "verified ledger가 없으면 historical high나 cash consideration을 exact IRR로 바꾸지 않는다.",
    ]
    failure_patterns = {
        "afce": "franchisee_economics; sss_reversal; gross_vs_net_openings; terminal_multiple",
        "affy": "nol_face_value; section_382; no_event; time_decay",
        "afg": "backlog_conversion; project_margin; target_timing; metric_definition",
        "atlas_common": "reserve_lag; premium_growth; capital_stack; liquidity",
        "atlas_note": "nominal_par; pik_coupon; secured_priority; maturity_extension",
        "afhp": "event_dependency; cash_conversion; scheme_completion; control_premium",
        "afi": "normalization_anchor; cash_burn; covenant_clock; bankruptcy_waterfall",
    }
    success_patterns = {
        "afce": "asset_light_royalty; net_unit_growth; eps_compounding; strategic_exit",
        "affy": "explicit_event_clock; tax_attribute_haircut; ownership_audit",
        "afg": "cash_conversion; balance_sheet; backlog_quality; target_audit",
        "atlas_common": "split_adjustment; underwriting_kpi; book_growth; reserve_audit",
        "atlas_note": "exact_security; scheme_calendar; coupon_ledger; recovery_waterfall",
        "afhp": "standalone_value; cash_bid; scheme_calendar; terminal_payoff",
        "afi": "monthly_runway; cash_ebitda; priority_waterfall; terminal_event",
    }
    for row in payload["postmortems"]:
        idea = next(i for i in IDEAS if i["id"] == row["idea_id"])
        row["failure_pattern_ko"] = failure_patterns[idea["group"]]
        row["success_pattern_ko"] = success_patterns[idea["group"]]
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
