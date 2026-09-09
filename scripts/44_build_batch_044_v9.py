#!/usr/bin/env python3
"""Build Batch 044 Nexstar / ePlus canonical V9 research artifacts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-09"
WEIGHTS = [20, 18, 18, 16, 16, 12]
NXST_IDS = [
    "71436938-3f4b-4d1d-9825-afe818a2f4d7",
    "924b250f-5703-4a82-8537-fac2a187abd1",
    "1b8faf06-08ca-4b27-b723-641fee88d15f",
    "dd7f83ea-6590-4028-9742-84d0cdffda86",
    "f91c8f1f-4a84-4eab-ab51-03068d3b0b2b",
    "585159f9-193f-40f6-aafa-3454b889e2fa",
]


def C(title, original, mechanism, evidence, assumption, falsifier, actual, gap, verdict, error, lesson):
    return dict(title=title, original=original, mechanism=mechanism, evidence=evidence,
                assumption=assumption, falsifier=falsifier, actual=actual, gap=gap,
                verdict=verdict, error=error, lesson=lesson)


def S(title, url, publisher, date, evidence, source_type="1차자료"):
    return dict(title=title, url=url, publisher=publisher, date=date,
                evidence=evidence, type=source_type)


BUSINESS = (
    "ePlus inc.는 미국 기업·공공기관에 서버, 네트워크, 보안, 데이터센터, 클라우드 장비를 조달하고 설계·구축·관리하는 "
    "value-added reseller/IT services 사업과 장비 금융·리스를 결합했다. Technology 사업은 큰 product billings에서 낮은 "
    "product gross margin과 더 높은 service gross profit을 남기고, financing 사업은 lease spread·transaction gain·residual "
    "recovery에서 돈을 번다. 성장기에 매출채권·재고·lease assets가 현금을 흡수하므로 매출이나 EBITDA만으로 owner earnings를 "
    "판단하면 안 된다. 2025년 국내 financing 사업 매각 뒤에는 technology·services 중심으로 경제엔진이 이동했다."
)

ENGINE = (
    "현금엔진은 `product gross profit + professional/managed-service gross profit + financing contribution - sales/engineering/G&A "
    "- cash tax - working-capital investment - corporate capex = equity FCF`다. Financing asset을 뒷받침하는 non-recourse debt와 "
    "일반 corporate recourse debt를 구분하고, tangible book에서는 lease credit loss·residual haircut·법률충당금을 차감해야 한다."
)

KPI = (
    "gross billings와 net sales의 차이, product/service gross profit, service attach와 gross margin, receivable·inventory days, "
    "lease investment·spread·credit loss·residual gain, recourse/non-recourse debt, cash conversion, share count, SEC filing·audit status"
)


EPLUS_SOURCES = [
    S("ePlus FY2007 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1022408/000102240808000003/form10k.htm", "SEC / ePlus", "2008-02-08", "옵션 조사·restatement, 2007-07-20 delisting, Pink Sheets와 법률·상장위험 검증."),
    S("ePlus FY2009 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm", "SEC / ePlus", "2009-06-16", "2008-05-05 공시 정상화, 2008-09-03 NASDAQ relisting, 분기 가격범위·cash 검증."),
    S("ePlus FY2010 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm", "SEC / ePlus", "2010-06", "technology/financing segment, capital structure와 후속 영업 검증."),
    S("ePlus fiscal 2011 Q1 results", "https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm", "SEC / ePlus", "2010-08", "2010-06 cash $79.3m·equity $190.4m과 non-recourse notes 검증."),
    S("ePlus FY2025 results", "https://www.eplus.com/who-we-are/investor-relations/press-releases/2025/05/eplus-reports-fourth-quarter-and-fiscal-year-2025-financial-results", "ePlus", "2025-05-22", "FY2025 product·services·financing mix와 gross profit 검증."),
    S("ePlus FY2026 results", "https://www.eplus.com/who-we-are/investor-relations/press-releases/2026/05/eplus-reports-fourth-quarter-and-fiscal-year-2026-financial-results", "ePlus", "2026-05-28", "FY2026 $2.443bn sales·$616m gross profit·$205m adjusted EBITDA·$411m cash와 financing sale 검증."),
]


IDEAS = [
    dict(
        id="16577e38-4933-4db0-892e-fa5b9fdd7d79", date="2002-06-04", author="adanah312", raw_short=False,
        filename="analysis/ideas/2002/2002-06-04_PLUS_long.md", source="https://www.valueinvestorsclub.com/idea/ePlus_Inc/1076596755",
        direction="Long", security="ePlus common equity / Long", entry="약 $9.10", horizon="18개월 및 IT spending 정상화", raw_horizon="원문 much greater volumes over next 18 months",
        title="닷컴 붕괴 뒤 생존·book/cash·volume recovery를 산 common Long",
        verdict="사업·장부가치 논지 성공, 18개월 가격성과 미검증·촉매 지연", score=7.0, process=6.5,
        conclusion="ePlus가 닷컴 붕괴에도 흑자를 유지하고 장기적으로 대형 IT solutions/services 사업으로 성장했다는 생존자 선별은 성공했다. 다만 $9.10→18개월 수익률 자료가 없고, 2007년 옵션회계로 실제 delisting까지 겪었으므로 book $9.45와 cash $2.50을 깨끗한 즉시 floor로 본 프로세스에는 큰 누락이 있었다.",
        t0="주가는 2년 전 $74에서 약 $9.10으로 하락했다. 1996년 상장 뒤 계속 흑자를 냈고 book value는 $2.71에서 $9.45, sales는 $56m에서 $306m으로 늘었으며 shares는 약 10m으로 두 배만 증가했다. EPS는 1999 $0.98, 2000 $0.91, 2001 $0.80, 단기 $0.80 수준을 예상했다. 고객은 약 1,500개, cash $2.50/share, 750k-share buyback authorization과 은행 finance subsidiaries와의 제휴가 근거였다.",
        reverse="시장은 IT spending 침체뿐 아니라 작은 reseller의 customer/vendor concentration, 낮은 product margin, working-capital·lease asset risk와 공시품질을 할인했을 수 있다. book와 cash는 receivable·lease impairment, growth working capital, contingent claims를 차감하기 전 숫자다.",
        valuation="표면상 price/book은 `9.10/9.45=0.96x`, P/E는 `9.10/0.80=11.4x`, cash를 차감한 price는 $6.60이다. 하지만 book가 liquidation floor가 되려면 receivables·lease residual이 회수되고 non-recourse/recourse obligations와 법률비용이 정확히 분류돼야 한다. 원문은 명시 target보다 survival+normalization rerating을 제시했다.",
        actual="2007년 option-grant investigation과 지연공시로 NASDAQ에서 상장폐지됐지만 2008-05-05 모든 required reports를 제출하고 2008-09-03 재상장했다. FY2009 cash는 $107.8m으로 FY2008 $58.4m에서 늘었다. FY2026에는 net sales $2.443bn, services revenue $462.9m, gross profit $616.1m, adjusted EBITDA $204.8m, cash $410.8m이었다. 장기 business survival·scale은 강하게 확인됐다.",
        price="원 DB에 performance row가 없고 2002~08 corporate-action-adjusted 일별 series도 복원하지 않았다. 따라서 18개월·1/3/5년 return, MFE·MAE, IRR은 계산하지 않는다. 사업의 장기성공과 실제 투자수익은 별도 판정한다.",
        drivers="장기 가치창출은 단순 B2B software가 아니라 vendor/customer 관계, product gross profit, services attach, working-capital 실행과 규모확대가 만들었다. Cash는 downside floor보다 accounting/listing shock을 버티는 duration insurance로 더 중요했다.",
        counterfactual="18개월 IT spending 회복이 없어도 $2.50 cash와 lease-adjusted book만으로 상장·공시 tail을 버틸 충분한 expected return이 있었는가?",
        error="book·cash의 질과 contingent governance risk를 충분히 감사하지 않았고, 18개월 volume catalyst를 gross profit·FCF bridge 없이 제시했다.",
        warning="2006년 지연공시와 option-grant review가 장부가치의 신뢰성과 liquidity discount를 동시에 훼손한 첫 사후 경고였다.", first_signal_date="2006-06-28",
        scenarios=[("Bear", "IT 침체·asset impairment·공시 shock", "book discount 지속/illiquidity", "2007 delisting 현실화"), ("Base", "생존·volume 정상화", "book 이상 rerating", "장기 사업확대"), ("Bull", "services scale·buyback", "quality rerating", "FY2026 규모로 장기 확인")],
        lessons=["small-cap book value는 audit·asset quality·상장 접근성을 포함해야 한다.", "cash는 excess value보다 adverse-event runway일 수 있다.", "매출 volume catalyst는 gross profit·working capital·FCF로 번역한다."],
        checklist=["gross profit dollars", "receivable/inventory days", "lease credit·residual", "recourse debt", "filing timeliness", "buyback execution", "price series·liquidity"],
        scorecard=[("Business thesis", "강한 성공"), ("Valuation thesis", "장기 지지·가격성과 미검증"), ("Catalyst thesis", "18개월 미검증"), ("Timing / path", "공시 shock 누락"), ("Security selection", "common 생존·illiquidity 위험")],
        claims=[
            C("닷컴 붕괴에도 흑자 생존", "상장 이후 계속 흑자여서 B2B wreckage와 다르다.", "현금창출·고객기반이 downturn을 견딜 runway를 만든다.", "EPS 1999 $0.98, 2000 $0.91, 2001 $0.80.", "보고이익의 질과 lease credit가 양호하다.", "지속손실·cash burn·covenant stress면 반증.", "회사는 delisting shock도 통과하고 FY2026까지 대규모 흑자를 냈다.", "terminal survival 강하게 확인.", "성공", "당시 회계·governance audit가 약했다.", "생존자는 회계품질과 cash conversion까지 본다."),
            C("book $9.45가 $9.10 downside를 지지", "price가 reported book 아래다.", "회수가능 자산이 enterprise가치 하방을 만든다.", "book $9.45/share vs price $9.10.", "receivable·lease·residual 가치가 장부에 가깝다.", "impairment·contingent liability가 discount를 소진하면 반증.", "장기 equity는 확대됐지만 2007 상장폐지로 liquidity discount가 발생했다.", "asset survival 성공·즉시 price floor 미검증.", "부분 성공", "reported book를 claim-adjusted book로 바꾸지 않았다.", "book에는 asset haircut과 market-access discount를 적용한다."),
            C("cash $2.50/share는 excess value", "현금이 가격의 27%를 차지한다.", "cash가 buyback·acquisition 또는 downturn buffer가 된다.", "T0 cash $2.50/share.", "working capital·lease funding·법률비용에 묶이지 않는다.", "cash가 영업자금으로 소진되면 excess 주장은 약화.", "현금은 2007~08 event를 견디는 buffer가 됐고 FY2009 $107.8m이었다.", "방어가치 확인·즉시 배분은 미확인.", "성공/재해석", "cash를 전액 excess로 보기 쉽다.", "성장 VAR cash는 operating minimum을 차감한다."),
            C("18개월 volume 증가가 효율을 만든다", "promotion cost 뒤 큰 volume이 operating efficiency를 연다.", "고정 sales/IT infrastructure를 더 큰 gross profit에 분산한다.", "원문 18개월 volume catalyst.", "volume의 incremental gross margin이 양수이고 WC 소요가 낮다.", "sales 증가에도 gross profit·CFO가 정체하면 반증.", "장기 scale은 크게 커졌으나 18개월 bridge는 복원되지 않았다.", "장기 방향 성공·horizon 미검증.", "미검증", "sales와 gross profit을 같은 성장으로 봤다.", "volume thesis는 incremental gross profit과 cash conversion으로 판정한다."),
            C("IT spending 회복이 rerating", "IT cycle 정상화가 EPS를 $0.80 이상으로 회복시킨다.", "고객 project 재개가 product·service demand를 늘린다.", "닷컴후 IT spending 침체.", "vendor competition이 회복분을 가격으로 넘기지 않는다.", "IT 회복에도 EPS·gross profit이 정체하면 반증.", "장기 technology/services 사업은 대폭 성장했다.", "원 18개월 timing은 미확인.", "장기 성공", "cycle timing을 구체 KPI 없이 제시했다.", "IT cycle은 backlog·billings·gross profit로 추적한다."),
            C("750k buyback이 per-share value 증가", "싼 가격에서 약 7% shares를 살 수 있다.", "share count 감소가 book·EPS/share를 올린다.", "750k authorization vs 약 10m shares.", "실제 매입이 book 이하에서 집행된다.", "authorization만 있고 execution이 없으면 촉매 실패.", "이후 회사는 여러 해 buyback을 활용했지만 이 authorization의 18개월 집행은 미복원이다.", "정책 방향 확인·T0 execution 미검증.", "부분 성공", "authorization를 completed repurchase처럼 읽을 위험.", "buyback은 수량·평균가·기간으로 검증한다."),
        ],
        metrics=[("Price / book", "$9.10 / $9.45", "book 이상 정상화", "장기 equity 확대·단기 return 없음", "부분"), ("Cash/share", "$2.50", "downside/excess", "FY2009 cash $107.8m", "buffer 성공"), ("EPS", "$0.80 run-rate", "IT 회복", "FY2026 diluted continuing EPS $4.71", "장기 성공"), ("Sales", "$56m→$306m", "volume 증가", "FY2026 $2.443bn", "장기 성공"), ("18개월 return", "$9.10 entry", "상승", "performance row 없음", "미검증")],
        timeline=[("2002-06-04", "VIC Long", "$9.10·book $9.45"), ("2006-06-28", "late filing/restatement 발표", "공시 risk"), ("2007-07-20", "NASDAQ delisting", "unmodeled liquidity shock"), ("2008-05-05", "모든 required reports 제출", "정상화 gate"), ("2008-09-03", "NASDAQ relisting", "market access 회복"), ("2009-03-31", "cash $107.8m", "survival buffer"), ("2025-06-30", "국내 financing 사업 매각", "business mix 전환"), ("2026-03-31", "sales $2.443bn·EBITDA $204.8m", "장기 scale 성공")],
    ),
    dict(
        id="09cb4b70-533d-435e-8566-be6203f98c1b", date="2004-12-23", author="hack731", raw_short=False,
        filename="analysis/ideas/2004/2004-12-23_PLUS_long.md", source="https://www.valueinvestorsclub.com/idea/ePlus/7455315813",
        direction="Long", security="ePlus common equity / Long", entry="약 $10.92", horizon="약 12개월", raw_horizon="Ariba trial·Manchester synergy·buyback·IT recovery",
        title="6.3x normalized earnings·1.1x TBV와 사건정상화를 산 common Long",
        verdict="사업·정상화 가치 성공, Cyberco·회계/listing duration 과소평가·가격성과 미검증", score=6.5, process=7.0,
        conclusion="$1.40 normalized EPS와 1.1x tangible book이 보여준 core earning power는 장기적으로 맞았지만, Cyberco가 경제적으로 비소구라는 가정과 법률·회계 문제가 빠르게 사라진다는 전제는 틀렸다. 실제 cash payment와 옵션 restatement, 2007 delisting까지 이어졌으므로 event-risk haircut이 부족했다. 정확한 투자수익은 데이터 부재로 확정하지 않는다.",
        t0="FY2004 sales $330m은 product/equipment 81%, lease 15.5%, fee/other 3.4%였다. TBV $9.80/share, cash $14.1m, FY04 EPS $1.02에서 option expense -$0.25, Ariba legal cost +$0.24, Manchester benefit +$0.19, buyback +$0.10, end-market growth +$0.10으로 normalized EPS $1.40을 만들었다. 약 7.7x, cash 90%를 excess로 보면 6.3x라고 주장했다. 최근 고객사기 $14m은 non-recourse 계약이라 회사 책임이 없다는 판단이었다.",
        reverse="시장은 정상화 EPS가 아니라 Cyberco representation/warranty breach, lender access, option accounting, legal cost duration과 thin-margin reseller의 working capital을 할인했다. $1.40 bridge는 five-year steady EPS 위에 여러 add-back·synergy·buyback·cycle 회복을 동시에 더했다.",
        valuation="원문 bridge `1.02-0.25+0.24+0.19+0.10+0.10=1.40`은 산술상 맞지만 buyback과 end-market 10%를 각각 $0.10로 단순화했다. cash 90% excess 가정도 lease/working-capital need를 작게 본다. Cyberco liability와 audit/legal fees를 probability-weighted claim으로 차감한 adjusted value가 필요했다.",
        actual="Cyberco 관련해 ePlus Group은 GMAC에 $6m을 지급했고 BoA 관련 이전 소송에서 $4.3m을 지급했다. 옵션부여일 조사로 2004·05 statements를 restate했고 FY2006 10-K는 2007-08-16에야 제출됐다. 2007-07-20 delisting 후 2008-05-05 filings current, 2008-09-03 relisting했다. FY2026 operating scale은 장기 core thesis를 확인했다.",
        price="원 DB performance row가 없다. 약 $10.92 entry와 SEC의 2007~09 분기 high/low는 있으나 중간 corporate action·OTC liquidity를 통일하지 못해 1/3/5년 total return과 IRR을 계산하지 않는다.",
        drivers="Core business·asset value는 견조했지만 투자경로는 legal/accounting duration과 exchange access가 지배했다. 사건비용이 normalized earnings에서 사라지는 속도보다 공시·상장 discount의 duration이 길었다.",
        counterfactual="Cyberco cash loss·audit fee·3년의 liquidity discount를 먼저 차감해도 $10.92에서 충분한 annualized return이 남았는가?",
        error="one-off를 너무 빨리 add-back하고 cash 90%를 excess로 보며, Cyberco의 non-recourse 예외조항과 market-access tail을 작게 평가했다.",
        warning="2006-06 late filing·option review가 normalization horizon을 넘어섰고, 2007-07 delisting은 최종 path 반증이었다.", first_signal_date="2006-06-28",
        scenarios=[("Bear", "Cyberco liability·restatement·delisting", "TBV discount 확대", "실제 중간경로"), ("Base", "$1.40 EPS·event cost 종료", "6~8x→rerating", "장기 core 성공"), ("Bull", "Manchester+buyback+IT recovery", "높은 per-share growth", "timing 지연")],
        lessons=["normalized EPS add-back은 제거 날짜와 재발확률을 붙인다.", "non-recourse에는 representation/warranty recourse exception이 숨어 있다.", "법률사건은 cash loss뿐 아니라 lender·audit·listing access를 훼손한다."],
        checklist=["legal cash paid", "representation warranty", "filing calendar", "audit fees", "working-capital minimum cash", "actual buyback", "TBV asset quality"],
        scorecard=[("Business thesis", "장기 성공"), ("Valuation thesis", "core cheapness 적중"), ("Catalyst thesis", "지연·경로 악화"), ("Timing / path", "실패/혼합"), ("Security selection", "common 생존·liquidity tail")],
        claims=[
            C("1.1x TBV는 downside", "$9.80 TBV 부근이라 하방이 낮다.", "회수가능 자산과 lease residual이 equity floor를 만든다.", "TBV $9.80/share.", "book asset·receivable·lease가 깨끗하다.", "법률claim·impairment가 TBV를 소진하면 반증.", "기업은 생존했지만 delisting과 litigation이 liquidity discount를 만들었다.", "asset survival은 성공·price floor 미검증.", "부분 성공", "claim-adjusted TBV가 아니었다.", "TBV에서 contingent claims와 liquidity haircut을 뺀다."),
            C("normalized EPS $1.40", "one-off 비용·synergy·buyback·cycle을 반영하면 $1.40이다.", "일시비용 제거와 scale이 reported EPS를 정상화한다.", "원문 $1.02에서 5단계 bridge.", "모든 조정이 같은 12개월에 실현된다.", "법률·audit 비용이 반복되면 반증.", "option/Cyberco/audit 비용이 수년 이어졌지만 장기 earnings power는 성장했다.", "magnitude 장기 지지·timing 실패.", "지연 성공", "여러 독립 bull 조정을 모두 base에 넣었다.", "normalized bridge는 확률·날짜·중복을 감사한다."),
            C("cash 90%가 excess", "$14.1m cash의 90%를 valuation에서 차감한다.", "현금이 buyback으로 per-share 가치를 만든다.", "T0 cash와 $7.5m authorization.", "working capital·lease funding에 cash가 거의 필요 없다.", "receivable/lease growth로 cash가 묶이면 반증.", "현금은 event shock을 흡수했고 장기 크게 증가했지만 즉시 excess payout은 아니었다.", "buffer 성공·excess 90% 미검증.", "부분 성공", "operating cash floor를 과소평가했다.", "VAR cash는 stress working capital을 먼저 차감한다."),
            C("Manchester synergy $0.19", "중복비용 제거가 diluted EPS $0.19를 더한다.", "인수 고객·매출을 낮은 incremental overhead로 통합한다.", "회사 pro forma FY04 estimate.", "exit·integration cost와 revenue loss가 작다.", "actual incremental profit이 안 보이면 약화.", "사업은 장기 확대됐으나 단일 deal contribution은 분리되지 않았다.", "claim attribution 미검증.", "미검증", "pro forma를 realized cash로 봤다.", "deal synergy는 standalone cohort로 검증한다."),
            C("Cyberco는 non-recourse라 무해", "$14m fraud exposure에 회사 책임이 없다고 봤다.", "lender가 financed asset/customer risk를 부담한다.", "회사 설명·약 40 financing sources.", "ePlus가 reps/warranties를 위반하지 않는다.", "cash settlement·lender restriction이면 반증.", "GMAC $6m, BoA $4.3m 지급과 추가 litigation이 있었다.", "최소 $10.3m cash outflow 확인.", "실패", "non-recourse 예외조건을 base에서 제외했다.", "계약 risk는 carve-out별 expected loss로 계산한다."),
            C("buyback·IT recovery가 catalyst", "$7.5m 매입과 IT 회복이 EPS/share를 높인다.", "싼 가격의 share reduction과 gross profit growth가 rerating을 만든다.", "FY02~04 repurchase와 board authorization.", "회사가 filings current이고 현금을 쓸 수 있다.", "공시지연으로 buyback이 막히면 반증.", "공시·delisting 경로가 buyback ability와 timing을 훼손했다.", "촉매가 event cleanup 뒤로 지연.", "부분 실패", "상장·SEC status를 촉매의 선행조건으로 놓지 않았다.", "capital return은 legal eligibility부터 확인한다."),
        ],
        metrics=[("Price / TBV", "$10.92 / $9.80", "1.1x floor", "장기 생존·중간 delisting", "부분"), ("Normalized EPS", "$1.40", "실현", "수년간 event cost 지속", "지연"), ("Cash", "$14.1m", "90% excess", "event runway로 사용", "재해석"), ("Cyberco cash loss", "0에 가까운 가정", "non-recourse", "최소 $10.3m 지급", "실패"), ("Price return", "$10.92 entry", "rerating", "performance row 없음", "미검증")],
        timeline=[("2004-12-23", "VIC Long", "$10.92·TBV $9.80"), ("2006-06-28", "late filing/restatement", "duration 반증"), ("2006-07", "option-grant review", "audit scope 확대"), ("2007-07-20", "NASDAQ delisting", "liquidity tail"), ("2008-05-05", "filings current", "event 정상화"), ("2008-09-03", "NASDAQ relisting", "discount source 제거"), ("2009-03-31", "cash $107.8m", "survival"), ("2026-03-31", "adjusted EBITDA $204.8m", "장기 core value")],
    ),
    dict(
        id="98c3017f-e2f5-4a57-8e98-ee0ebac34d63", date="2007-05-09", author="ele2996", raw_short=True,
        filename="analysis/ideas/2007/2007-05-09_PLUS_long.md", source="",
        direction="Long", security="ePlus common equity / Long", entry="약 $9.55", horizon="restatement 공개·potential business combination", raw_horizon="정확한 종료일 없음; timely enough to be a buy",
        title="hard book $12.90와 accounting-overhang 해소를 산 special-situation Long",
        verdict="방향교정·eventual 성공, 두 달 뒤 delisting과 duration 과소평가·exact IRR 미검증", score=7.0, process=7.5,
        conclusion="raw Short가 아니라 명시적 Long이다. Hard book $12.90, manageable option charge, SAP recovery와 insider/Hovde ownership은 survival을 지지했고 최종 restatement·relisting도 성공했다. 그러나 2007-07-20 delisting과 $6.75 분기 low는 'timely' 가정을 반증했으며 exact OTC execution이 없어 realized IRR은 만들지 않는다.",
        t0="원문은 과거 2002 $9.10·2004 $10.92 Long을 업데이트하며 약 $9.55에서 매수를 제안했다. 2005-12 equity $131m에서 goodwill 등 $30m을 빼 hard book $12.90/share로 계산했다. SAP $17.5m receipt가 GMAC $6m, BoA $4m, option charge 약 $3m+investigation $5m을 거의 상쇄한다고 봤다. Hovde 15.5%, insiders 38.7% excluding Hovde와 potential business combination이 catalyst였다.",
        reverse="시장은 charge amount보다 filings가 얼마나 늦고 audit scope가 확대돼 listing·buyback·employee retention·institutional ownership이 훼손되는지 할인했다. 특허 settlement와 legal losses를 netting해도 timing·liquidity loss는 상쇄되지 않는다.",
        valuation="entry $9.55는 hard book $12.90의 약 74%였다. 그러나 hard book에서 litigation reserve, audit/professional fees, OTC liquidity discount와 working-capital lockup을 차감해야 한다. SAP receipt와 Cyberco/option cash cost는 세금·시점·재발 가능성이 달라 단순 netting하면 안 된다.",
        actual="게시 약 두 달 뒤 2007-07-20 NASDAQ에서 delist됐다. SEC FY2009 10-K의 분기 range는 2007-09 quarter low $6.75로 $9.55 대비 약 -29.3% observed drawdown을 보여준다. FY2006 10-K는 2007-08-16, FY2007 10-K는 2008-02-08, 최종 late 10-Q는 2008-05-05 제출됐고 2008-09-03 NASDAQ에 재상장했다.",
        price="T0 약 $9.55 대비 SEC-reported 2007-09 quarter low $6.75는 약 -29.3%다. 이 low가 투자자가 실제 체결한 MAE는 아니다. Relisting을 포함한 2008-09 quarter range는 $10.82~$13.85였지만 exact exit·dividend·OTC spread가 없어 realized return/IRR은 계산하지 않는다.",
        drivers="성과는 core 사업·cash·hard book가 audit duration을 버티고 filings current→relisting이라는 discount source가 실제 제거되면서 만들어졌다. 중간 손실은 accounting charge가 아니라 exchange access·liquidity 악화가 만들었다.",
        counterfactual="restatement 결과가 $8m charge로 끝나도 15개월 OTC capital lock-up과 29% drawdown을 감수할 expected annualized return이 있었는가?",
        error="restatement charge와 legal settlement를 잘 분석했지만 delisting probability·filing dependency·OTC liquidity를 payoff에 충분히 넣지 않았다.",
        warning="2007-07-20 delisting은 게시 72일 뒤 발생한 명확한 adverse event였다.", first_signal_date="2007-07-20",
        scenarios=[("Bear", "delisting·filing 지연", "$6.75 observed low", "실제 발생"), ("Base", "charges manageable·filings current", "hard book rerating", "2008-05 실현"), ("Bull", "business combination", "빠른 value realization", "미실현")],
        lessons=["event direction과 event duration은 별도 claim이다.", "상장폐지 risk는 price drawdown·spread·capital lock-up으로 비용화한다.", "settlement proceeds와 legal/audit loss는 세금·시점·확률을 맞춘 뒤 net한다."],
        checklist=["late filings remaining", "auditor sign-off", "NASDAQ deadlines", "OTC volume/spread", "legal cash payments", "adjusted hard book", "relisting application"],
        scorecard=[("Business thesis", "성공"), ("Valuation thesis", "asset support 적중"), ("Catalyst thesis", "restatement/relisting 성공"), ("Timing / path", "실패·delisting"), ("Security selection", "common 성공·illiquidity tail")],
        claims=[
            C("raw Short가 아니라 Long", "cheap enough and timely enough to be a buy라고 결론냈다.", "metadata 교정이 payoff 부호를 바로잡는다.", "원문 명시적 buy 문구.", "원문 entity가 미국 ePlus다.", "실제 short payoff면 방향 재검토.", "원문 valuation·ownership·catalyst가 모두 상승을 전제로 한다.", "raw flag 반대.", "교정 성공", "SQL 방향을 믿으면 결과가 뒤집힌다.", "direction은 원문 action verb로 검증한다."),
            C("hard book $12.90가 downside", "$9.55는 hard book의 약 74%다.", "회수가능 net assets가 downside를 완충한다.", "$131m equity-$30m goodwill/other.", "법률·audit·working capital haircut이 제한적이다.", "adjusted book가 price 아래면 반증.", "core balance sheet는 생존했으나 주가는 분기 low $6.75까지 갔다.", "price floor는 실패·asset survival은 성공.", "부분 실패", "liquidity discount를 book에 반영하지 않았다.", "special-situation book에는 duration haircut을 붙인다."),
            C("SAP가 Cyberco·option cost를 상쇄", "$17.5m receipt가 약 $6m+$4m+$3m+$5m cost를 거의 덮는다.", "one-off inflow가 event cash loss를 중화한다.", "원문 settlement/cost estimate.", "세금·시점·추가 fees가 작다.", "추가 claim·audit fee가 늘면 반증.", "Cyberco·audit/legal duration은 계속돼 단순 cash netting보다 컸다.", "명목액 유사·duration cost 누락.", "부분 실패", "gross proceeds와 all-in event cost를 비교했다.", "event waterfall에 tax·professional fee·time을 포함한다."),
            C("option restatement charge는 manageable", "약 $3m earnings charge+$5m investigation이면 해결된다.", "noncash/limited charge 공개 뒤 valuation discount가 닫힌다.", "Audit Committee preliminary estimate.", "scope가 확대되지 않고 auditor가 빨리 sign-off한다.", "filing 지연·delisting이면 timing 반증.", "회계 charge보다 late filings가 2007 delisting을 초래했다.", "금액보다 second-order effect가 큼.", "방향 성공·경로 실패", "charge size에 집중했다.", "회계사건은 filing/listing consequences를 먼저 본다."),
            C("Hovde·insider가 value realization", "Hovde 15.5%, insiders 38.7%가 sale/buyback을 압박한다.", "집중 ownership과 board seats가 capital allocation을 바꾼다.", "Hovde cost 약 $10.15·two board seats.", "지배주주와 outsider incentives가 정렬된다.", "장기 현금유보·deal 부재면 catalyst 약화.", "사업은 생존했으나 near-term business combination은 없었다.", "ownership support·specific catalyst 실패.", "부분 성공", "activist presence를 transaction으로 직결했다.", "ownership은 제안·투표·actual allocation으로 검증한다."),
            C("restated filings/business combination 촉매", "공시 공개 또는 결합이 discount를 제거한다.", "정보·liquidity 접근 회복이 buyer universe를 넓힌다.", "원문 catalyst.", "회사가 NASDAQ access를 잃기 전에 current가 된다.", "delisting 또는 12개월 초과면 timing 실패.", "2008-05 filings current, 2008-09 relisting; deal은 없음.", "eventual success·15개월 duration.", "지연 성공", "delisting intermediate state를 누락했다.", "event tree에 adverse intermediate nodes를 포함한다."),
        ],
        metrics=[("Entry / hard book", "$9.55 / $12.90", "discount close", "asset survival·price low $6.75", "혼합"), ("Observed low", "$9.55", "downside limited", "$6.75", "약 -29.3%"), ("Option/event cost", "약 $8m", "manageable", "filing/listing effect 큼", "경로 실패"), ("Filing status", "late", "restated release", "2008-05-05 current", "지연 성공"), ("Relisting", "미정", "value realization", "2008-09-03", "성공")],
        timeline=[("2007-05-09", "VIC Long", "$9.55·hard book $12.90"), ("2007-07-20", "NASDAQ delisting", "72일 뒤 adverse path"), ("2007-Q3", "quarter low $6.75", "약 -29.3% observed"), ("2007-08-16", "FY2006 10-K", "filing catch-up"), ("2008-02-08", "FY2007 10-K", "audit progress"), ("2008-05-05", "all required reports current", "핵심 catalyst"), ("2008-09-03", "NASDAQ relisting", "liquidity 회복"), ("2009-03-31", "cash $107.8m", "survival 확인")],
    ),
    dict(
        id="f04f83bb-ff87-4e97-981c-05be168e60c6", date="2007-11-14", author="zach721", raw_short=True,
        filename="analysis/ideas/2007/2007-11-14_PLUS_long.md", source="",
        direction="Long", security="ePlus common equity on Pink Sheets / Long", entry="$10.00", horizon="12개월; filings 60~90일·early-2008 relisting", raw_horizon="more than double over next year",
        title="65% TBV·3.5x normalized EBTDA와 relisting을 산 Pink Sheets Long",
        verdict="방향교정·filing/relisting 성공, $20+ 12개월 target 실패·exact return 미검증", score=7.5, process=8.5,
        conclusion="이미 delisted된 $10 common을 사서 filings current와 NASDAQ relisting을 기다린 구조는 2008-05·09에 실제 성공했다. 다만 60~90일보다 오래 걸렸고 SEC 분기 high는 12개월 안에 $13.85에 그쳐 $20+ target은 실패했다. Business·asset thesis와 catalyst는 성공, target/timing은 혼합이다.",
        t0="주가 $10, 3Q06A TBV $13.75, FY08E TBV $15+, forecast book의 65%, normalized FY08 EBTDA $24.8m/$2.88 per share, 3.5x EV/EBTDA-capex였다. revenue는 FY05 $575m, FY06 $650m, FY07 $798m, FY08E $900m+; 8.6m shares에 sales $105+/share였다. 2001~06 shares 2.979m/20%를 $11.04 평균에 매입했고 filing 정상화 후 buyback 재개를 기대했다. Downside $9, upside $20+였다.",
        reverse="시장은 20개월째인 option restatement, Pink Sheets 15k average volume, thin 2.5% EBTDA margin, high working capital과 schedule uncertainty를 가격에 넣었다. TBV는 liquid해 보여도 매출성장이 A/R·inventory를 흡수하면 주주에게 즉시 배분할 수 없다.",
        valuation="원문 normalized EBTDA는 FY08E reported $20.8m에 excess professional fee $4m을 더해 $24.8m이었다. $20 target은 <8x normalized EBTDA, 1.3x TBV, 약 10x EPS라고 했다. 그러나 normalization 비용의 재발, working-capital cash, OTC discount와 catalyst delay를 반영하면 target duration이 늘어난다.",
        actual="회사는 2008-02-08 FY2007 10-K, 2008-03-31 2007-Q1 10-Q, 2008-05-05 마지막 required reports를 제출했다. 2008-09-03 NASDAQ에 재상장했다. SEC-reported price range는 2007-12 quarter $8.78~$10.55, 2008-06 $9.50~$13.80, 2008-09 $10.82~$13.85, 2008-12 $8.01~$10.99였다. 금융위기까지 겹쳐 $20 target은 관찰되지 않았다.",
        price="$10 entry 대비 2008-09 quarter high $13.85는 최대 관찰 가능한 +38.5%지만 investor MFE나 realized return이 아니다. 같은 12개월 창의 SEC-reported high가 $13.85라 $20+ target은 실패했다. exact OTC spread·daily exit·dividend가 없어 IRR은 계산하지 않는다.",
        drivers="수익 driver는 cheap multiple 자체보다 late filing count가 줄고 NASDAQ relisting으로 정보·유동성 discount가 제거된 것이었다. 반대로 $20 미달은 timing delay, thin margin·working capital과 2008 market shock이 multiple rerating을 제한한 결과다.",
        counterfactual="relisting이 성공해도 macro shock으로 multiple이 오르지 않을 수 있는데, $20 target 중 얼마가 earnings·book growth이고 얼마가 liquidity rerating이었는가?",
        error="adverse event가 이미 발생한 뒤라 구조는 좋아졌지만 60~90일 schedule과 buyback·multiple expansion을 지나치게 빠르게 묶었다.",
        warning="2008년 초까지 remaining filings가 남아 60~90일 예상이 미뤄진 시점이 timing 경고였다. Fundamental failure는 아니었다.", first_signal_date="2008-02-14",
        scenarios=[("Bear", "filings 지연·OTC·macro shock", "$8~9", "2008-Q4 low $8.01"), ("Base", "current→relisting", "$13~16", "high $13.85·relisting"), ("Bull", "$24.8m EBTDA·buyback·8x", "$20+", "12개월 실패")],
        lessons=["event special situation은 이미 발생한 adverse state에서 사면 확률분포가 개선될 수 있다.", "catalyst 성공과 target price 성공을 분리한다.", "TBV·EBTDA 할인은 working-capital과 liquidity duration을 차감한다."],
        checklist=["remaining filing count", "auditor date", "relisting requirements", "OTC volume/spread", "normalized fee run-rate", "cash conversion", "actual buyback restart"],
        scorecard=[("Business thesis", "성공"), ("Valuation thesis", "cheapness 적중·$20 실패"), ("Catalyst thesis", "강한 성공"), ("Timing / path", "약 10개월·예상보다 지연"), ("Security selection", "Pink Sheets common 적절·liquidity risk")],
        claims=[
            C("raw Short가 아니라 Pink Sheets Long", "보유주식이 1년 내 두 배 가능하다고 했다.", "direction 교정이 payoff와 success sign을 바로잡는다.", "원문 own shares·$9 downside/$20+ upside.", "entity가 미국 ePlus다.", "실제 원문이 decline을 목표하면 반증.", "모든 valuation·catalyst가 Long이다.", "raw flag 반대.", "교정 성공", "ticker/flag만 쓰면 반대로 판정된다.", "원문 action·payoff로 direction을 확정한다."),
            C("65% FY08E TBV가 downside", "$10은 forecast TBV $15+의 65%다.", "liquid tangible assets가 $9 downside를 지지한다.", "3Q06A $13.75, last 3Qs +$2.26.", "book growth가 filings 후 확인되고 asset haircut이 낮다.", "restated TBV가 크게 낮아지면 반증.", "filings는 완료되고 balance sheet는 생존했다.", "asset thesis 성공·price floor는 2008 low $8.01 근접.", "성공", "forecast book에 liquidity haircut이 없었다.", "book discount는 actual audited book 기준으로 갱신한다."),
            C("normalized EBTDA $24.8m", "excess professional fees 종료 후 $2.88/share earning power다.", "one-off remediation cost 소멸이 margin을 정상화한다.", "FY08E reported $20.8m+$4m add-back.", "legal/audit run-rate가 historic 1% revenue로 돌아간다.", "fees·margin pressure가 반복되면 반증.", "filing 정상화 후 business는 성장했고 FY2026 EBITDA $204.8m이었다.", "장기 earning power 강하게 확인.", "장기 성공", "EBTDA와 cash conversion을 혼용했다.", "normalized earning에는 working-capital cash를 연결한다."),
            C("60~90일 내 filings current", "5개 late filings 중 3개를 7주에 냈으니 곧 끝난다.", "정보정상화가 OTC discount를 제거한다.", "recent filing velocity.", "remaining audit work가 같은 속도로 진행된다.", "90일 초과면 timing 반증.", "all required filings는 2008-05-05 완료됐다.", "게시 후 약 173일로 90일보다 약 83일 지연.", "방향 성공·timing 실패", "linear throughput extrapolation.", "event schedule은 remaining item complexity로 산정한다."),
            C("NASDAQ relisting이 rerating", "early 2008 재상장으로 buyer universe가 회복된다.", "liquidity·institutional eligibility가 multiple을 높인다.", "delisting 원인이 late filings로 명확.", "다른 listing deficiency가 없고 market이 안정적이다.", "relisting 거부·장기지연이면 반증.", "2008-09-03 NASDAQ relisting.", "날짜는 늦었지만 사건 직접 적중.", "강한 성공", "macro multiple risk를 별도 처리하지 않았다.", "listing catalyst와 market beta를 분리한다."),
            C("buyback 재개·$20+", "회사는 filing current 뒤 TBV 110%까지 매입한다.", "저평가 share reduction이 EPS/TBV per share를 높인다.", "과거 2.979m shares at $11.04.", "cash가 working capital보다 buyback에 쓰인다.", "buyback 부재 또는 12개월 high <$20이면 target 실패.", "12개월 SEC range high $13.85로 $20 미달.", "$20 대비 최소 -30.8%.", "실패", "historical policy를 automatic future execution으로 봤다.", "capital allocation은 authorization·eligibility·execution으로 나눈다."),
        ],
        metrics=[("Entry / target", "$10 / $20+", "100%+ 1년", "12개월 high $13.85", "target 실패"), ("TBV", "$13.75 actual / $15+ forecast", "discount close", "balance sheet 생존", "성공"), ("Normalized EBTDA", "$24.8m", "fee normalization", "FY2026 $204.8m", "장기 성공"), ("Filing completion", "60~90일", "early 2008", "2008-05-05", "약 83일 이상 지연"), ("NASDAQ relisting", "early 2008", "multiple catalyst", "2008-09-03", "성공·지연")],
        timeline=[("2007-07-20", "NASDAQ delisting", "T0 이전 adverse state"), ("2007-11-14", "VIC Long", "$10→$20+"), ("2007-12-31", "close $9.67", "초기 정체"), ("2008-02-08", "FY2007 10-K", "catch-up"), ("2008-05-05", "all reports current", "핵심 catalyst"), ("2008-Q2/Q3", "range high $13.85", "$20 미달"), ("2008-09-03", "NASDAQ relisting", "liquidity 회복"), ("2008-Q4", "low $8.01", "macro/path risk"), ("2026-03-31", "sales $2.443bn·EBITDA $204.8m", "장기 quality 확인")],
    ),
]


RAW_META = {
    "16577e38-4933-4db0-892e-fa5b9fdd7d79": (2415, 185),
    "09cb4b70-533d-435e-8566-be6203f98c1b": (5229, 336),
    "98c3017f-e2f5-4a57-8e98-ee0ebac34d63": (5068, 68),
    "f04f83bb-ff87-4e97-981c-05be168e60c6": (10224, 1215),
}


def idea_sources(i):
    raw = S("VIC original idea" if i["source"] else "VIC source-DB preserved original", i["source"],
            "Value Investors Club / source SQL", i["date"],
            "T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준.", "원문")
    return [raw, *EPLUS_SOURCES]


def render_report(i):
    raw_direction = "Short" if i["raw_short"] else "Long"
    lines = [
        f"# ePlus inc. (PLUS) — {i['date']} VIC {i['direction']}", "",
        "> **Idea unit:** 이 게시일의 ePlus common 한 건만 분석한다. `PLUS` ticker의 Plus500 아이디어와 분리한다.",
        f"> **Research as-of:** {ASOF}. 원 SQL 방향과 실제 security direction, business outcome과 투자수익을 분리했다.",
        "", "---", "", "## 0. Idea Snapshot", "", "| 항목 | 내용 |", "|---|---|",
        "| 회사 / Ticker | ePlus inc. / PLUS — 미국 ePlus, Plus500 아님 |",
        f"| VIC 게시일 / 작성자 | {i['date']} / {i['author']} |", f"| 분석 증권 / 실제 방향 | {i['security']} |",
        f"| 원 SQL 방향 | {raw_direction} — raw 값 보존, research direction은 별도 검증 |",
        f"| 기준 진입가격 | {i['entry']} |", f"| 기대기간 | {i['horizon']} |", f"| raw horizon audit | {i['raw_horizon']} |",
        f"| 최종 판정 | **{i['verdict']}** |", "", f"> **결론:** {i['conclusion']}", "", "---", "",
        "## 1. 회사는 정확히 무엇을 하는가", "", BUSINESS, "", ENGINE, "", "### 가치사슬과 security payoff", "",
        "Vendor의 hardware/software를 고객 solution으로 설계·조달하고 services와 financing을 붙인다. 매출총액은 gross/net presentation에 따라 바뀔 수 있어 gross profit dollars와 cash conversion이 더 중요하다. Book value는 receivable·lease·residual·재고의 회수와 recourse 분류 뒤에만 common floor가 된다.",
        "", "### 매 분기 볼 핵심 KPI", "", KPI, "", "---", "", "## 2. 당시 상황과 시장이 가격에 넣은 것", "", i["t0"], "", "### Reverse expectations", "", i["reverse"], "", "---", "", "## 3. 원문 투자논지 지도", "",
    ]
    for n, c in enumerate(i["claims"], 1):
        lines += [f"### C{n}. {c['title']} — {c['verdict']}", "", "**원문 주장**", "", c["original"], "",
                  "**경제적 메커니즘**", "", c["mechanism"], "", "**T0 근거**", "", c["evidence"], "",
                  "**숨은 가정**", "", c["assumption"], "", "**사전 반증조건**", "", c["falsifier"], "",
                  "**실제 결과**", "", c["actual"], "", "**정량 gap**", "", c["gap"], "",
                  "**분석 오류 또는 제한**", "", c["error"], "", "**재사용 교훈**", "", c["lesson"], ""]
    lines += ["---", "", "## 4. 당시 Valuation과 Payoff Structure", "", i["valuation"], "", "### 시나리오 분석", "",
              "| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |", "|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scenarios"]]
    lines += ["", "### 핵심 수치", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["metrics"]]
    lines += ["", "### 촉매와 시간", "", f"판정 horizon은 **{i['horizon']}**다. 장기 기업성공은 원 horizon의 투자수익을 대체하지 않는다.",
              "", "---", "", "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "", "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["timeline"]]
    lines += ["", "### 실제 사업·자본구조 추이", "", i["actual"], "", "---", "", "## 6. 실제 투자결과 — 가격 경로와 실현 가능성", "", i["price"], "",
              "SEC의 분기 high/low는 가능한 관찰범위이지 특정 투자자의 execution·MFE·MAE가 아니다. 일별 split/dividend-adjusted series와 OTC spread가 없으면 exact IRR을 만들지 않는다.",
              "", "---", "", "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 핵심 gap |", "|---|---|---:|---|---|"]
    for n, (c, w) in enumerate(zip(i["claims"], WEIGHTS), 1):
        lines.append(f"| C{n} | {c['title']} | {w}% | {c['verdict']} | {c['gap']} |")
    lines += ["", "---", "", "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", i["drivers"], "",
              "### Counterfactual", "", i["counterfactual"], "", "---", "", "## 9. 분석 오류 유형과 최초 경고", "", i["error"], "",
              "### 최초로 관찰 가능했던 경고신호", "", i["warning"], "", "---", "", "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", ""]
    for n, lesson in enumerate(i["lessons"], 1):
        lines += [f"### Lesson {n}", "", lesson, ""]
    lines += ["### 지금 같은 아이디어를 다시 본다면", ""] + [f"- {x}" for x in i["checklist"]]
    lines += ["", "---", "", "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scorecard"]]
    lines += [f"| Thesis score | {i['score']:.1f}/10 |", f"| Process score | {i['process']:.1f}/10 |", f"| 종합 | **{i['verdict']}** |",
              "", "### 한 문장 교훈", "", f"> {i['lessons'][0]}", "", "---", "", "## 12. Sources / Validation Notes", ""]
    for n, source in enumerate(idea_sources(i), 1):
        if source["url"]:
            lines.append(f"{n}. [{source['title']}]({source['url']}) — {source['publisher']}, {source['date']}. {source['evidence']}")
        else:
            lines.append(f"{n}. {source['title']} — {source['publisher']}, {source['date']}. {source['evidence']}")
    lines += ["", "### 데이터 품질", "",
              "- T0 원문·metadata: **A/B** — source SQL의 원문을 기준으로 했다. 공개 URL이 없는 2007년 글도 raw body가 보존돼 있다.",
              "- 공시·상장·자본구조: **A** — SEC filing과 회사 결과를 우선했다.",
              "- 가격경로: **C/미검증** — performance row가 없어 SEC 분기 range만 제한적으로 썼다. exact total return·IRR은 계산하지 않았다.",
              f"- raw SQL direction은 **{raw_direction}**, 실제 research direction은 **{i['direction']}**다. ticker entity도 Plus500과 분리했다.", ""]
    return "\n".join(lines)


def make_payload(ideas):
    out = {"schema_version": "vic-deep-research-v9", "batch": 44,
           "title": "Nexstar / ePlus — Value Engines, Event Duration and Security V9", "research_asof": ASOF,
           **{k: [] for k in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")}}

    nxst = json.loads((ROOT / "data/curated/batch_039_nexstar_sinclair_deep_v7.json").read_text(encoding="utf-8"))
    for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources"):
        for iid in NXST_IDS:
            out[key].extend(row.copy() for row in nxst[key] if row["idea_id"] == iid)
    for row in out["ideas_master"]:
        row["is_short"] = 1
        row["direction_ko"] = "숏"
        row["auto_tag_status_ko"] = "raw 방향 보존·본문 실제 Long/Pair 수동검증 완료"

    for i in ideas:
        desc_chars, catalyst_chars = RAW_META[i["id"]]
        raw_ko = "숏" if i["raw_short"] else "롱"
        out["ideas_master"].append({
            "idea_id": i["id"], "date": i["date"], "year": int(i["date"][:4]), "ticker": "PLUS", "company_name": "ePlus inc.",
            "author": i["author"], "direction_ko": raw_ko, "is_short": int(i["raw_short"]), "contest_winner": 0,
            "source_link": i["source"] or None, "description_chars": desc_chars, "catalyst_chars": catalyst_chars,
            "narrative_tags_ko": "entity-resolution; IT VAR; tangible book; accounting; delisting; relisting; working capital",
            "idea_type_ko": "기업가치/특수상황", "horizon_raw": i["raw_horizon"], "horizon_months": None,
            "performance_available": 0, "idea_return_1y": None, "idea_return_3y": None, "idea_return_5y": None,
            "auto_tag_status_ko": "raw 방향·ticker entity 보존·본문 실제 방향 수동검증 완료",
            "perf_1m": None, "perf_3m": None, "perf_6m": None, "perf_1y": None, "perf_2y": None, "perf_3y": None, "perf_5y": None})
        out["postmortems"].append({
            "idea_id": i["id"], "ticker": "PLUS", "research_direction_ko": i["direction"], "company_description_ko": BUSINESS,
            "original_thesis_ko": i["t0"], "actual_development_ko": i["actual"], "thesis_verdict_ko": i["conclusion"],
            "business_verdict_ko": i["scorecard"][0][1], "catalyst_verdict_ko": i["scorecard"][2][1], "valuation_verdict_ko": i["scorecard"][1][1],
            "stock_verdict_ko": i["price"], "current_verdict_ko": i["verdict"], "overall_verdict_ko": i["verdict"], "why_ko": i["drivers"],
            "success_pattern_ko": "entity_resolution; asset_support; filing_catalyst; business_survival",
            "failure_pattern_ko": "duration; liquidity; accounting; gross_net; normalization; working_capital",
            "root_error_ko": i["error"], "first_signal_ko": i["warning"], "first_signal_date": i["first_signal_date"],
            "knowable_at_t0_ko": i["claims"][0]["evidence"] + " " + i["claims"][0]["falsifier"],
            "avoidability_ko": "중간 이상. 원문·SEC event tree와 claim-adjusted book로 사전에 더 보수적으로 모델링 가능했다.",
            "counterfactual_question_ko": i["counterfactual"],
            "analyst_note_ko": f"raw SQL {'Short' if i['raw_short'] else 'Long'} 보존; 실제 방향 {i['direction']}; entity=ePlus inc.",
            "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None,
            "confidence": 0.95, "research_asof": ASOF, "research_status_ko": "원문·SEC 1차자료 검증 완료·가격성과 제한 명시"})
        out["meta"].append({
            "idea_id": i["id"], "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·event calendar·price range·first break·entity audit 장문분석",
            "report_version": "V9-canonical", "thesis_type_ko": i["title"], "one_line_verdict_ko": i["conclusion"],
            "thesis_score": i["score"], "process_score": i["process"], "return_summary_ko": i["price"],
            "core_error_ko": i["error"], "core_insight_ko": i["lessons"][0], "research_asof": ASOF})
        sections = [
            ("회사·가치사슬·현금엔진", f"{BUSINESS}\n\n{ENGINE}\n\n핵심 KPI: {KPI}."),
            ("T0 시장기대·reverse expectations", f"{i['t0']}\n\n{i['reverse']}"),
            ("Valuation·payoff·실제경로", f"{i['valuation']}\n\n실제: {i['actual']}\n\n가격: {i['price']}"),
            ("사후인과·오류·교훈", f"{i['drivers']}\n\n오류: {i['error']}\n\nCounterfactual: {i['counterfactual']}"),
        ]
        for n, (title, body) in enumerate(sections, 1):
            out["sections"].append({"idea_id": i["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, (c, w) in enumerate(zip(i["claims"], WEIGHTS), 1):
            out["claims"].append({"idea_id": i["id"], "claim_order": n, "claim_title_ko": c["title"], "thesis_weight_pct": w,
                                  "original_claim_ko": c["original"], "t0_evidence_ko": c["evidence"], "key_assumption_ko": c["assumption"],
                                  "ex_ante_falsifier_ko": c["falsifier"], "actual_result_ko": c["actual"], "quantitative_gap_ko": c["gap"],
                                  "verdict_ko": c["verdict"], "analytical_error_ko": c["error"], "reusable_lesson_ko": c["lesson"]})
        for n, row in enumerate(i["metrics"], 1):
            out["metrics"].append({"idea_id": i["id"], "metric_order": n, "metric_name_ko": row[0], "t0_value_ko": row[1],
                                   "thesis_expectation_ko": row[2], "actual_value_ko": row[3], "verdict_ko": row[4],
                                   "interpretation_ko": f"{row[0]}의 T0 기대와 실제를 동일 단위가 가능한 범위에서 비교했다."})
        for n, row in enumerate(i["timeline"], 1):
            out["timeline"].append({"idea_id": i["id"], "event_order": n, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for n, source in enumerate(idea_sources(i), 1):
            out["sources"].append({"idea_id": i["id"], "source_order": n, "source_type_ko": source["type"], "publisher": source["publisher"],
                                   "title_ko": source["title"], "source_date": source["date"], "url": source["url"], "evidence_ko": source["evidence"]})
    return out


def main():
    if len(IDEAS) != 4 or len({i["id"] for i in IDEAS}) != 4:
        raise ValueError("Batch 044 must contain four ePlus ideas plus six reused NXST ideas")
    for i in IDEAS:
        if len(i["claims"]) != 6 or sum(WEIGHTS) != 100:
            raise ValueError(f"{i['id']}: six weighted claims required")
        path = ROOT / i["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_report(i), encoding="utf-8")
    parts = [
        "ideas/2012/2012-08-26_NXST_long.md", "ideas/2016/2016-01-29_NXST_MEG_pair_cvr.md",
        "ideas/2017/2017-08-12_NXST_long.md", "ideas/2018/2018-04-23_NXST_long.md",
        "ideas/2020/2020-03-12_NXST_long.md", "ideas/2021/2021-09-20_NXST_long.md",
        *[i["filename"].removeprefix("analysis/") for i in IDEAS],
    ]
    wrapper = "# Batch 044 — Nexstar / ePlus V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + \
              "> Streamlit 호환 wrapper다. canonical index: [Batch 044 V9 Index](batch_044_v9_index.md).\n"
    (ROOT / "analysis/batch_044_nexstar_eplus_10.md").write_text(wrapper, encoding="utf-8")
    payload = make_payload(IDEAS)
    output = ROOT / "data/curated/batch_044_nexstar_eplus_deep_v7.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports=10 claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
