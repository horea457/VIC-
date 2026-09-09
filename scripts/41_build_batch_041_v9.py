#!/usr/bin/env python3
"""Build Batch 041 canonical V9 reports and the detailed dashboard overlay."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-09"
WEIGHTS = [20, 18, 18, 16, 16, 12]


def C(title, original, mechanism, evidence, assumption, falsifier, actual, gap, verdict, error, lesson):
    return {
        "title": title,
        "original": original,
        "mechanism": mechanism,
        "evidence": evidence,
        "assumption": assumption,
        "falsifier": falsifier,
        "actual": actual,
        "gap": gap,
        "verdict": verdict,
        "error": error,
        "lesson": lesson,
    }


def S(title, url, publisher, date, evidence, source_type="1차자료"):
    return {
        "title": title,
        "url": url,
        "publisher": publisher,
        "date": date,
        "evidence": evidence,
        "type": source_type,
    }


TSQ_BUSINESS = (
    "Townsquare Media는 미국 상위 50위 밖의 중소도시를 중심으로 지역 라디오, 지역 웹·앱, "
    "programmatic digital advertising인 Townsquare Ignite, SMB 구독형 마케팅 서비스인 Townsquare "
    "Interactive를 운영한다. 라디오는 지역 영업조직·브랜드·퍼스트파티 audience data를 만들고, 디지털 "
    "사업은 그 고객접점과 자체 ad-tech를 이용해 더 넓은 광고예산을 가져오는 구조다. 따라서 회사의 정체성은 "
    "라디오 청취율 하나가 아니라 지역 고객획득 엔진을 여러 매체에 재사용할 수 있는지로 판단해야 한다."
)

TSQ_ENGINE = (
    "경제 엔진은 `Digital Advertising revenue + subscription revenue + broadcast advertising + events - "
    "direct sales/platform/content cost - corporate cost - cash interest - capex - cash tax`다. 디지털 매출비중이 "
    "올라도 subscription churn, digital segment profit, cash interest가 나빠지면 common equity FCF는 늘지 않는다. "
    "높은 부채 때문에 digital absolute growth와 debt reduction이 동시에 나타나야 valuation rerating이 지속된다."
)

ETM_BUSINESS = (
    "Entercom은 2017년 CBS Radio를 결합해 대형 지역 라디오 네트워크가 됐고 이후 Audacy로 사명을 바꿨다. "
    "광고주는 지역·전국 청취자에게 도달하기 위해 spot 광고, digital audio, podcast, sports·news content와 events에 "
    "돈을 지불한다. 방송 주파수와 지역 브랜드는 희소하지만 청취시간과 광고예산은 streaming·search·social로 이동할 "
    "수 있다. 고정적인 programming·talent·sales 비용 때문에 유기적 매출 감소는 EBITDA보다 FCF에 더 크게 전달된다."
)

ETM_ENGINE = (
    "경제 엔진은 `broadcast spot + network/digital/podcast/event revenue - station/programming/talent/sales cost - "
    "corporate cost - cash interest - capex - tax`다. CBS Radio 거래 이후에는 headline revenue나 synergy보다 "
    "`organic revenue decline + cash interest`와 비교한 stressed-normalized FCF가 중요했다. 2024년 구조조정은 "
    "약 $1.9bn debt를 약 $350m로 줄여야 equity 청구권이 생길 수 있었음을 보여준다."
)

EMMS_BUSINESS = (
    "Emmis Communications는 New York·Los Angeles·Indianapolis 등 주요 시장의 radio station, 과거 TV·publishing, "
    "digital·emerging technology 자산을 보유했던 지배주주형 소형 미디어 회사다. Station 가치는 주파수 license, "
    "지역 브랜드, audience, 광고관계를 묶은 현금흐름과 전략적 희소성에서 나오지만, minority common은 자산 자체가 "
    "아니라 debt·preferred·tax·transaction cost·지배주주의 처분 결정을 모두 지난 뒤의 residual claim이다."
)

EMMS_ENGINE = (
    "경제 엔진은 `station-level BCF + publishing/events/other - corporate overhead - cash interest - capex - tax`이고, "
    "asset play의 common value는 `매각가능가치 × 실현확률 × 세후·시간할인 - debt - preferred/legal claims`다. "
    "자산을 제값에 팔아도 새 인수에 재투자하거나 현금화가 수년 늦으면 nominal NAV와 주주 IRR은 크게 달라진다."
)

BUSINESS = {"TSQ": TSQ_BUSINESS, "ETM": ETM_BUSINESS, "EMMS": EMMS_BUSINESS}
ENGINE = {"TSQ": TSQ_ENGINE, "ETM": ETM_ENGINE, "EMMS": EMMS_ENGINE}
KPI = {
    "TSQ": "Digital Advertising·Interactive의 유기적 매출, subscription churn·고객수, segment profit, broadcast ex-political revenue, cash interest, 순부채/2년평균 EBITDA, FCF, 실제 주식수·평균 자사주 매입가",
    "ETM": "same-station/core spot revenue, digital revenue와 contribution, station EBITDA, 현금이자, maturity wall, liquidity, 순부채/stressed EBITDA, FCF, covenant·refinancing 가격",
    "EMMS": "station BCF, corporate overhead, cash interest, 순부채·preferred 청구액, covenant, 자산별 after-tax sale value, 매각대금 사용처, 완전희석 주식수, 지배주주와 minority holder의 경제적 일치",
}


ETM_SOURCES = [
    S("CBS/Entercom merger announcement", "https://www.sec.gov/Archives/edgar/data/813828/000119312517028280/d513089dex991.htm", "SEC / CBS", "2017-02-02", "CBS Radio 결합 구조와 예상 규모 검증."),
    S("CBS Radio combination completion", "https://www.sec.gov/Archives/edgar/data/813828/000119312517350719/d471182d8k.htm", "SEC / CBS", "2017-11-17", "CBS Radio 결합 종결일 검증."),
    S("Entercom 2018 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1067837/000119312519054296/d712409d10k.htm", "SEC / Entercom", "2019-03-01", "2018 net revenue $1.462567bn과 합병 후 사업·부채 검증."),
    S("Audacy Chapter 11 / restructuring announcement", "https://audacyinc.com/press/audacy-reaches-agreement-with-a-supermajority-of-its-debtholders-on-balance-sheet-deleveraging-transaction-that-will-equitize-over-80-of-the-companys-debt-and-establish-a-robust-capital-struc/", "Audacy", "2024-01-07", "약 $1.6bn equitization과 debt $1.9bn→$350m 계획 검증."),
    S("Audacy restructuring completion", "https://audacyinc.com/press/audacy-successfully-completes-financial-restructuring-emerges-as-a-growing-scaled-multi-platform-audio-leader-with-the-industrys-strongest-balance-sheet/", "Audacy", "2024-09-30", "80% debt reduction과 약 2.7x post-emergence leverage 검증."),
]

TSQ_SOURCES = [
    S("Townsquare FY2022 results", "https://www.sec.gov/Archives/edgar/data/1499832/000149983223000027/a123122pressrelease.htm", "SEC / Townsquare", "2023-03-09", "Digital 50%·+16%와 net leverage 4.29x 검증."),
    S("Townsquare FY2024 results", "https://www.sec.gov/Archives/edgar/data/1499832/000149983225000038/a123124pressrelease.htm", "SEC / Townsquare", "2025-03-17", "Digital $233.958m·segment profit $62.112m·refinancing·repurchases 검증."),
    S("Townsquare FY2025 results", "https://www.sec.gov/Archives/edgar/data/1499832/000149983226000019/a123125pressrelease.htm", "SEC / Townsquare", "2026-03-16", "2025 Digital 매출 55%, segment profit 56% 검증."),
    S("Townsquare Q2 2026 results", "https://www.sec.gov/Archives/edgar/data/1499832/000149983226000044/a63026pressrelease.htm", "SEC / Townsquare", "2026-08-06", "1H26 Digital 매출 57%, segment profit 59% 검증."),
]

EMMS_SOURCES = {
    "tender": S("Emmis FY2006 Q1 Form 10-Q", "https://www.sec.gov/Archives/edgar/data/783005/000095013705008542/c96603e10vq.htm", "SEC / Emmis", "2005-07-11", "$19.50·20.25m주·$394.9m tender와 debt financing 검증."),
    "tv": S("Emmis 2009 Form 10-K", "https://www.sec.gov/Archives/edgar/data/783005/000095012309008795/c51249e10vk.htm", "SEC / Emmis", "2009-05-14", "2008-07 최종 WVUE $41m 매각과 TV division exit 완료 검증."),
    "deal": S("Emmis 2011 Form 10-K", "https://www.sec.gov/Archives/edgar/data/783005/000095012311047715/c16797e10vk.htm", "SEC / Emmis", "2011-05-10", "$2.40 tender, preferred amendment 실패, 거래 종료 검증."),
    "termination": S("Emmis merger termination Form 8-K", "https://www.sec.gov/Archives/edgar/data/783005/000095014210001475/form8k_092710.htm", "SEC / Emmis", "2010-09-29", "9월 24일 drop-dead 이후 merger termination 검증."),
    "kxos": S("KXOS discontinued-operation disclosure", "https://www.sec.gov/Archives/edgar/data/783005/000078300513000007/R9.htm", "SEC / Emmis", "2013", "$85.5m 현금 매각과 약 $32.8m gain 검증."),
    "wbls": S("WBLS/WLIB acquisition announcement", "https://www.sec.gov/Archives/edgar/data/783005/000078300514000018/exhibit991.htm", "SEC / Emmis", "2014-02-11", "$131m cash 거래와 station operating income 기대 검증."),
    "litigation": S("Emmis financing and preferred litigation disclosure", "https://www.sec.gov/Archives/edgar/data/783005/000119312514144950/d713183dex991.htm", "SEC / Emmis", "2014-04", "2014 district-court 승소·appeal 및 financing 검증."),
    "q2015": S("Emmis FY2016 Q2 Form 10-Q", "https://www.sec.gov/Archives/edgar/data/783005/000078300515000046/emms2016q210-q.htm", "SEC / Emmis", "2015-10", "2014 Credit Agreement $191.6m과 2015 appellate affirmation 검증."),
    "k2016": S("Emmis 2016 Form 10-K", "https://www.sec.gov/Archives/edgar/data/783005/000078300516000072/emms10k-2016.htm", "SEC / Emmis", "2016-05", "preferred litigation의 2015 affirmation·settlement 검증."),
    "mediaco": S("Emmis 2020 Form 10-K", "https://www.sec.gov/Archives/edgar/data/783005/000156459020025335/emms-10k_20200229.htm", "SEC / Emmis", "2020-05", "MediaCo $91.5m cash+$5m note+23.72% stake 및 delisting 검증."),
    "separation": S("MediaCo separation filing", "https://www.sec.gov/Archives/edgar/data/1784254/000104746919006201/a2240029zex-99_1.htm", "SEC / MediaCo", "2019-11-25", "WQHT/WBLS separation 조건의 교차검증."),
    "delist": S("Emmis voluntary delisting Form 8-K", "https://www.sec.gov/Archives/edgar/data/783005/000156459020018540/emms-8k_20200421.htm", "SEC / Emmis", "2020-04-21", "Nasdaq 자진상장폐지 결정 검증."),
}


IDEAS = []


IDEAS.extend([
    {
        "id": "2eec41d0-f8d6-47ba-822f-c361725a37ee",
        "date": "2022-03-14", "author": "JohnnyFinance", "ticker": "TSQ", "company": "Townsquare Media",
        "filename": "analysis/ideas/2022/2022-03-14_TSQ_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/TOWNSQUARE_MEDIA_INC/5454442109",
        "direction": "Long", "security": "TSQ common equity / Long", "entry": "원문 가격 미복원; forward FCF yield 약 24%",
        "horizon": "2024년 말(약 34개월)", "raw_horizon": "DB의 명시 horizon 없음; 원문 2024년 말 target 사용",
        "title": "digital mix 전환은 맞았지만 절대이익과 rerating 속도를 과대평가한 Long",
        "verdict": "사업구조 성공·수익경로 실패/미검증", "score": 5.5, "process": 6.0,
        "conclusion": (
            "‘라디오 안의 디지털 회사’라는 분류는 맞았다. Digital은 2022년 매출·adjusted operating income의 "
            "50%가 됐고 2025년 매출 55%, 1H26 57%까지 높아졌다. 그러나 2024 Digital revenue는 $233.958m으로 "
            "원문 $275m 목표를 14.9% 밑돌았고, segment profit은 전년 대비 10.2% 감소했다. mix 확대를 절대이익 "
            "성장으로 간주한 것이 핵심 오류다. 원 SQL 6개월 가격비율도 0.751x여서 초기 가격경로는 Long과 반대였다."
        ),
        "t0": (
            "Townsquare는 radio broadcaster라는 분류 때문에 낮은 배수를 받았고 2017~2020년 FCC license impairment로 "
            "회계이익도 흐려졌다. 원문은 Ignite와 Interactive가 곧 매출·현금흐름의 과반이 되는 capital-light growth "
            "platform인데 시장 screen이 이를 놓친다고 봤다. 약 24% forward FCF yield, 2022년 말 net leverage 3.8x, "
            "2023 refinancing, $50m buyback을 연결해 2024년 말 2.9배·46% IRR을 제시했다."
        ),
        "reverse": (
            "싼 가격이 정당하려면 digital mix가 올라가도 Interactive churn·sales cost 때문에 absolute digital profit이 "
            "정체되고, radio decline과 cash interest가 FCF를 흡수하면 된다. 반대로 2.9배가 되려면 $275m digital "
            "revenue뿐 아니라 segment profit 성장, 4x 아래 leverage, refinancing 비용 하락, 저가 buyback이 동시에 "
            "필요했다. 이는 한 개의 transformation claim이 아니라 네 개의 동시조건이었다."
        ),
        "valuation": (
            "24% FCF yield를 단순 역수인 4.2배로 읽으면 싸 보이지만, equity FCF의 지속기간이 핵심이다. V9 base는 "
            "Digital Advertising와 Interactive를 별도 성장률·margin으로 두고, Broadcast를 감소 annuity로 평가한 뒤 "
            "순부채를 차감한다. 2024 실제로 Digital Advertising은 +5.5%였지만 Interactive는 -8.4%였고 합산 Digital은 "
            "+0.6%에 그쳤다. 같은 해 Digital segment profit은 -10.2%였으므로 revenue mix만으로 higher multiple을 "
            "부여할 수 없었다."
        ),
        "scenarios": [
            ("Bear", "Interactive 감소·broadcast ex-political 약세·고금리", "FCF yield는 value trap", "2024 profit 경로가 일부 근접"),
            ("Base", "Digital 절대성장·안정 margin·완만한 deleveraging", "FCF/주 증가", "mix는 성공, profit은 미달"),
            ("Bull", "$275m Digital·3.8x 이하 leverage·buyback", "2024 말 2.9배", "동시조건 미충족"),
        ],
        "actual": (
            "2022 Digital revenue는 약 $231m, 전년 대비 16% 늘어 매출과 adjusted operating income의 50%가 됐고 "
            "net leverage는 4.29x였다. 2024 합산 Digital revenue는 $233.958m으로 전년 대비 0.6%, 원문 목표 $275m보다 "
            "$41.0m 낮았다. Digital segment profit은 $62.112m으로 10.2% 줄었다. 회사는 2024년 $36.2m의 2026 notes를 "
            "상환하고 2.3m주를 평균 $10.31에 매입했으며 만기를 2030년으로 연장했다. 2025~1H26에는 digital mix가 "
            "55%→57%로 더 높아져 구조전환 자체는 이어졌다."
        ),
        "price": (
            "원 SQL의 price ratio는 1개월 1.061x, 3개월 0.780x, 6개월 0.751x다. 즉 +6.1% 뒤 -22.0%, -24.9%로 "
            "초기 drawdown이 컸다. 원문 진입가와 2024-12 배당포함 종가 series가 복원되지 않아 exact horizon IRR, "
            "MFE·MAE는 계산하지 않았다. 2.9배·46% IRR을 달성했다고 볼 검증자료는 없고, 영업 bridge는 그 bull "
            "case를 지지하지 않는다."
        ),
        "drivers": (
            "맞은 것은 local salesforce를 digital 상품에 재사용하는 distribution advantage였다. 틀린 것은 digital "
            "비중 상승을 digital absolute profit 성장으로 번역한 부분과 leverage 개선 속도다. 2024 buyback과 note "
            "repurchase는 실제였지만, Interactive 감소와 segment profit 하락이 multiple expansion의 현금근거를 약화했다."
        ),
        "counterfactual": "2024 Digital revenue가 $275m에 도달했어도 segment profit이 $62m에 머물렀다면 24% FCF yield의 재평가는 정당했을까?",
        "error": "mix shift, absolute growth, incremental margin을 하나로 묶었다. 2023 refinancing을 금리·수수료·maturity별 bridge 없이 확정 catalyst처럼 취급했다.",
        "warning": "2022년 말 leverage가 원문 기대 3.8x가 아니라 4.29x였던 것이 첫 계량 경고였다. 2024 Interactive -8.4%와 Digital profit -10.2%가 business-model 경고를 확정했다.",
        "first_signal_date": "2022-12-31",
        "lessons": [
            "숨은 성장사업은 매출비중이 아니라 절대매출·segment profit·FCF contribution으로 검증한다.",
            "고레버리지 transformation은 영업 KPI와 refinancing KPI를 같은 분기 bridge에 둔다.",
            "buyback은 authorization이 아니라 평균매입가·실제 주식수 감소·부채기회비용으로 평가한다.",
        ],
        "checklist": ["Ignite와 Interactive 성장률 분리", "Interactive churn·customer count", "Digital segment profit margin", "broadcast ex-political decline", "cash interest와 maturity", "순부채/2년평균 EBITDA", "actual diluted shares"],
        "scorecard": [("Business thesis", "구조 성공·절대이익 부분"), ("Valuation thesis", "미흡"), ("Catalyst thesis", "부분 성공"), ("Timing / path", "실패"), ("Security selection", "Long 방향은 혼합")],
        "claims": [
            C("Digital이 회사의 과반이 된다", "Ignite·Interactive가 곧 매출과 cash flow의 과반이 된다.", "기존 local salesforce·first-party data를 digital 상품에 재사용한다.", "사업부 분리공시와 T0 growth.", "digital 성장이 radio 감소보다 빠르고 margin이 유지된다.", "Digital 매출·profit 비중이 50% 아래에 머물면 반증.", "2022 50%, 2025 매출 55%, 1H26 57%로 상승했다.", "mix 기준 강한 적중.", "성공", "비중과 절대이익을 혼동하면 안 됨.", "mix claim과 earnings claim을 별도 저장한다."),
            C("2024 Digital revenue는 $275m이다", "두 digital 사업의 성장으로 2024 $275m에 도달한다.", "광고주 cross-sell·programmatic scale·subscription retention이 매출을 복리시킨다.", "T0 segment forecast.", "Interactive 감소를 Ignite가 충분히 상쇄한다.", "2024 actual이 $247.5m 미만이면 목표의 10% 이상 미달.", "2024 actual $233.958m.", "$41.042m, 14.9% 미달.", "실패", "서로 다른 unit economics를 한 growth rate로 묶음.", "segment별 revenue bridge를 만든다."),
            C("Interactive의 반복매출은 안정적이다", "best-in-class churn이 subscription revenue의 예측성을 높인다.", "낮은 churn이 CAC 회수기간과 lifetime value를 개선한다.", "원문이 인용한 2021 management commentary.", "공시되지 않은 churn 설명이 실제 customer economics를 대표한다.", "revenue·profit이 함께 감소하면 반복매출 quality를 재평가.", "2024 Interactive revenue -8.4%, segment profit -7.9%.", "반복성은 있었지만 growth·profit 방어 실패.", "부분 실패", "비공시 churn을 hard KPI처럼 사용.", "retention 주장은 cohort revenue와 contribution으로 검증한다."),
            C("deleveraging과 refinancing이 equity duration을 늘린다", "2022 말 3.8x, 2023 저비용 refinancing으로 risk가 낮아진다.", "이자·만기 위험 감소가 FCF와 equity multiple을 높인다.", "T0 cash-generation 기대와 2026 notes.", "EBITDA growth와 capital-market access가 동시에 유지된다.", "4x대 leverage 지속·higher coupon refinance면 thesis 약화.", "2022 4.29x로 기대 미달; 2024 notes $36.2m repurchase와 2030 maturity refinance는 실행.", "속도 실패·maturity 성공.", "부분 성공", "refinancing의 가격과 기간을 분리하지 않음.", "maturity extension과 interest saving을 별도 평가한다."),
            C("$50m buyback이 주당가치를 높인다", "저평가 주식을 사서 FCF/share를 높인다.", "intrinsic value 아래 매입이 share count를 줄인다.", "3년 authorization.", "부채상환보다 buyback IRR이 높고 주식보상이 상쇄하지 않는다.", "순부채와 주식수가 동시에 악화하면 반증.", "2024 2.3m주를 평균 $10.31에 매입하고 options도 retire했다.", "실행 확인; intrinsic accretion은 별도 미검증.", "부분 성공", "authorization을 realized return으로 간주.", "debt repurchase와 buyback의 risk-adjusted yield를 비교한다."),
            C("24% FCF yield가 2.9배·46% IRR을 만든다", "cheap cash yield와 catalyst가 2024 말 큰 rerating을 만든다.", "FCF 성장·debt 감소·multiple expansion이 복합적으로 작동한다.", "원문 valuation bridge.", "FCF가 durable하고 terminal decline haircut이 작다.", "6개월 -25% 또는 Digital profit 미달 시 sizing·target 재검토.", "6개월 ratio 0.751x, 2024 영업 bull case 미달; exact horizon return 미복원.", "목표 수익 검증불가·핵심 driver 미달.", "실패/미검증", "bull 동시조건에 높은 확률을 부여.", "IRR은 성장·debt·multiple 기여도를 분해한다."),
        ],
        "metrics": [
            ("Forward FCF yield", "약 24%", "지속 가능한 FCF", "exact normalized FCF 미복원", "미검증"),
            ("2022 net leverage", "3.8x 기대", "빠른 하락", "4.29x", "미달"),
            ("2024 Digital revenue", "$275m", "목표 달성", "$233.958m", "-14.9%"),
            ("2024 Digital segment profit", "성장 기대", "성장", "$62.112m, -10.2%", "실패"),
            ("6개월 price ratio", "상승 경로", "1.0x 초과", "0.751x", "실패"),
        ],
        "timeline": [("2022-03-14", "VIC Long", "24% FCF yield·2024 2.9배"), ("2022-12-31", "Digital 50%·leverage 4.29x", "mix 성공·debt 속도 미달"), ("2024", "notes·equity repurchase", "$36.2m debt·2.3m shares"), ("2024-12-31", "Digital $233.958m", "$275m target 미달"), ("2025-12-31", "Digital revenue 55%", "구조전환 지속"), ("2026-06-30", "Digital revenue 57%", "mix 추가 상승")],
        "sources": TSQ_SOURCES,
    },
    {
        "id": "9bc25044-5526-4075-8977-165259b54e0f",
        "date": "2005-11-28", "author": "leob710", "ticker": "ETM", "company": "Entercom Communications",
        "filename": "analysis/ideas/2005/2005-11-28_ETM_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/Entercom/9301817401",
        "direction": "Long", "security": "ETM common equity / Long", "entry": "정확한 원문 가격 미복원; 12.4x 2006E after-tax FCF",
        "horizon": "12~18개월", "raw_horizon": "12-18 months",
        "title": "희소 주파수와 높은 FCF의 duration을 과대평가한 전통 라디오 Long",
        "verdict": "목표기간 가격 미검증·장기 사업논지 실패", "score": 3.5, "process": 4.5,
        "conclusion": (
            "12~18개월의 정확한 배당포함 수익률은 데이터가 없어 판정하지 않는다. 다만 장기 사업 가설은 실패했다. "
            "Entercom은 2017년 CBS Radio를 결합해 2018 매출을 $1.463bn까지 키웠지만 2024년 약 $1.6bn debt "
            "equitization이 필요했다. 2005년의 양호한 margin·FCF는 디지털 대체가 만드는 현금흐름 duration risk를 "
            "막지 못했다."
        ),
        "t0": (
            "iPod·satellite radio·internet audio와 광고둔화 우려로 radio multiple이 낮아진 시기였다. 원문은 제한된 "
            "주파수와 지역시장 지위, 업계 상위 margin, 강한 FCF, 당시 보수적 balance sheet를 근거로 구조적 붕괴가 "
            "아니라 cyclical·sentiment discount라고 봤다. 2006E after-tax FCF 12.4배에 12~18개월 30~40% upside를 "
            "예상했고 광고 회복·accretive acquisition·capital-structure action을 촉매로 제시했다."
        ),
        "reverse": (
            "시장 가격은 새 오디오 기술이 즉시 radio를 없앤다는 것보다, 광고예산과 청취시간이 서서히 이동해 높은 "
            "현재 FCF의 잔존기간이 짧아질 위험을 반영했을 수 있다. Long이 맞으려면 same-station revenue와 pricing이 "
            "유지되고, 낮은 capex가 진짜 owner earnings로 남으며, M&A가 decline을 숨기는 것이 아니라 FCF/share를 "
            "높여야 했다."
        ),
        "valuation": (
            "12.4배 FCF는 안정적 자산에는 합리적일 수 있지만 declining annuity에는 비쌀 수 있다. 적정식은 "
            "`현재 FCF × 존속기간/감소율 - 순부채`다. 30~40% rerating은 광고 uptick만으로 부족하고 시장이 FCF "
            "duration을 다시 길게 봐야 했다. 후일 CBS Radio scale은 revenue를 키웠으나 debt claim도 커져, 현재 FCF "
            "multiple만으로 downside를 정의한 약점이 드러났다."
        ),
        "scenarios": [("Bear", "radio ad·audience의 구조적 감소", "FCF duration 축소", "장기적으로 실현"), ("Base", "광고 정상화·margin 유지", "30~40% rerating", "목표기간 가격 미검증"), ("Bull", "accretive M&A·private value", "높은 FCF/주", "scale은 실현, equity economics 실패")],
        "actual": (
            "2017-11 CBS Radio 결합이 완료돼 전국 규모가 크게 늘었고 2018 net revenue는 $1.462567bn이었다. 그러나 "
            "유기적 radio-ad pressure와 높은 fixed cost, 인수후 leverage가 FCF를 압박했다. Audacy는 2024-01 "
            "Chapter 11에서 약 $1.9bn debt 중 $1.6bn을 equitize하고 2024-09 약 $350m debt, 2.7x net leverage로 "
            "나왔다. 이는 장기 common equity duration 가정이 틀렸음을 보여준다."
        ),
        "price": (
            "원 DB에는 1개월~5년 성과가 없다. 따라서 12~18개월 30~40% 목표가 달성됐는지, MFE·MAE가 얼마였는지 "
            "수치를 만들지 않는다. 2024 restructuring은 장기 terminal result이지 원문의 짧은 horizon 수익률 대체값이 "
            "아니다. 판정은 ‘기간성과 미검증’과 ‘장기 business/equity thesis 실패’를 의도적으로 분리한다."
        ),
        "drivers": "초기 수익이 있었다면 광고 cycle·multiple mean reversion이었을 가능성이 크고, 장기 손실은 청취시간·광고예산 이동과 후속 leveraged M&A가 만들었다. Spectrum scarcity는 공급을 제한했지만 대체매체에 대한 고객수요를 고정하지 못했다.",
        "counterfactual": "2006 광고가 반등해 18개월 수익이 났더라도 long-run FCF duration이 계속 짧아졌다면 이 논지는 성공인가, 단기 multiple trade인가?",
        "error": "희소 license를 고객수요의 moat로 해석하고 현재 높은 FCF margin을 장기 duration으로 외삽했다.",
        "warning": "원문 horizon 안의 first contradictory quarter는 미복원이다. 구조적 경고는 radio organic growth보다 acquisition scale에 의존하는 비중이 커질 때 확인됐고 2017 CBS deal에서 크게 확대됐다.",
        "first_signal_date": "미복원",
        "lessons": ["전통 미디어 FCF는 크기보다 감소율과 존속기간을 먼저 추정한다.", "희소한 물리자산과 희소한 고객 attention을 구분한다.", "M&A revenue growth는 same-station growth와 debt-adjusted FCF/share로 해체한다."],
        "checklist": ["same-station ad revenue", "청취시간·광고 share", "cash conversion", "maintenance capex", "organic FCF 감소율", "M&A 제외 leverage", "maturity/refinancing"],
        "scorecard": [("Business thesis", "장기 실패"), ("Valuation thesis", "기간성과 미검증"), ("Catalyst thesis", "미검증"), ("Timing / path", "미검증"), ("Security selection", "장기 common 부적절")],
        "claims": [
            C("기술파괴 우려는 과도하다", "새 오디오 기술이 radio를 빠르게 훼손하지 못한다.", "local reach·habit·license scarcity가 청취자와 광고주를 지킨다.", "당시 audience와 strong franchise.", "대체재가 attention과 ad budget을 의미 있게 빼앗지 않는다.", "same-station revenue·audience가 경기회복 뒤에도 하락하면 반증.", "장기적으로 digital audio와 광고이동이 지속됐다.", "정확한 T0 horizon gap은 미복원, 장기 방향 실패.", "장기 실패", "license scarcity와 demand durability 혼동.", "moat는 공급제약이 아니라 고객예산 점유율로 측정한다."),
            C("광고둔화는 cyclical이다", "광고 uptick이 12~18개월 내 실적을 정상화한다.", "높은 fixed cost 때문에 소폭 매출 회복이 FCF를 크게 늘린다.", "경기민감 업종의 평균회귀.", "점유율 침식이 cyclical rebound보다 작다.", "경기회복기에도 organic revenue가 회복하지 않으면 반증.", "기간별 organic series 미복원.", "정량 판정 불가.", "미검증", "cycle과 secular trend를 분해하지 않음.", "광고회복은 industry와 company share로 나눈다."),
            C("업계 상위 margin·FCF는 지속된다", "운영효율과 낮은 capex가 owner earnings를 방어한다.", "고정비 규모와 local franchise가 높은 cash conversion을 만든다.", "T0 historical margin·FCF.", "revenue decline과 content cost가 margin을 압도하지 않는다.", "stressed FCF가 debt service를 못 덮으면 반증.", "2024에는 $1.6bn debt equitization이 필요했다.", "terminal equity cash flow 방어 실패.", "실패", "peak/current FCF에 terminal haircut 부족.", "declining annuity는 duration-adjusted multiple을 쓴다."),
            C("보수적 balance sheet가 하방을 제한한다", "낮은 leverage가 downturn과 기술변화를 견딘다.", "재무여력이 acquisition·buyback과 생존옵션을 제공한다.", "T0 balance-sheet 평가.", "후속 capital allocation이 보수성을 유지한다.", "debt-funded deal로 stressed leverage가 급증하면 반증.", "CBS Radio 결합 뒤 높은 debt가 equity를 지배했다.", "T0 상태는 가능했으나 정책의 지속성 실패.", "부분→실패", "현재 balance sheet를 영구 management policy로 봄.", "재무건전성 thesis에는 acquisition guardrail을 붙인다."),
            C("accretive M&A·buyback이 FCF/주를 높인다", "저평가 자본환원과 거래가 주당가치를 만든다.", "낮은 purchase multiple과 share shrink가 per-share cash를 늘린다.", "원문 catalyst.", "organic decline과 financing cost를 넘는 incremental return.", "revenue만 늘고 debt/FCF가 악화하면 반증.", "2017 대형 M&A는 revenue를 키웠지만 최종 deleveraging을 막지 못했다.", "scale 성공·per-share durability 실패.", "실패", "accretion을 첫해 회계수치로 볼 위험.", "M&A는 stressed FCF/주와 5년 debt paydown으로 판정한다."),
            C("12.4x FCF에서 30~40% upside다", "limited downside와 12~18개월 rerating을 기대한다.", "광고회복·capital action이 multiple discount를 닫는다.", "원문 target.", "시장 discount가 duration risk가 아니라 sentiment다.", "18개월 total return이 목표범위에 못 미치면 실패.", "event-date price series가 없어 판정하지 않았다.", "exact return 미검증.", "미검증", "terminal thesis와 horizon return을 사후 혼합하면 안 됨.", "가격성과는 원문 horizon으로 별도 저장한다."),
        ],
        "metrics": [("2006E after-tax FCF multiple", "12.4x", "30~40% rerating", "horizon return 미복원", "미검증"), ("Expected upside", "30~40%", "12~18개월", "미복원", "미검증"), ("2018 net revenue", "T0 미해당", "scale optionality", "$1.462567bn", "scale 성공"), ("2024 funded debt", "보수적 BS 기대", "관리 가능", "$1.9bn→$350m", "장기 실패")],
        "timeline": [("2005-11-28", "VIC Long", "12.4x FCF·12~18개월"), ("2007-05", "원 horizon 종료", "exact price 미복원"), ("2017-02-02", "CBS Radio deal", "balance-sheet policy 변화"), ("2017-11-17", "거래 종결", "scale 확대"), ("2018-12-31", "매출 $1.463bn", "revenue scale 확인"), ("2024-01~09", "Chapter 11·emergence", "장기 equity thesis 실패")],
        "sources": ETM_SOURCES,
    },
    {
        "id": "68bfa6f3-94ca-4ba9-903c-9d00eadca05d",
        "date": "2017-08-08", "author": "greenshoes93", "ticker": "ETM", "company": "Entercom Communications",
        "filename": "analysis/ideas/2017/2017-08-08_ETM_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/ENTERCOM_COMMUNICATIONS_CORP/4501708346",
        "direction": "Long", "security": "ETM common equity / Long", "entry": "약 $10.04 역산($16.66 target / 1.66)",
        "horizon": "약 1년", "raw_horizon": "DB parser 12~18개월; 원문 excerpt는 next year",
        "title": "CBS Radio synergy를 secular decline과 debt hurdle보다 크게 본 Long",
        "verdict": "명시기간 실패·장기 common 실패", "score": 2.0, "process": 3.0,
        "conclusion": (
            "거래 종결과 revenue scale은 맞았지만 보통주 payoff는 실패했다. 원문은 2018 FCF/share $2.37의 7배인 "
            "$16.66을 1년 target으로 제시했고 2019 FCF/share $2.90에는 100%+ upside를 봤다. 그러나 2018-07 후속 "
            "Short가 $8.15에 등장해 target 기간 안에 가격이 이미 역방향이었고, 2024 Chapter 11은 synergy가 secular "
            "revenue decline과 interest hurdle을 넘지 못했음을 확정했다."
        ),
        "t0": (
            "CBS Radio는 실적이 약했지만 Entercom의 운영진이 station turnaround와 비용·매출 synergy를 만들 수 있다는 "
            "기대가 컸다. 합병 후 portfolio와 광고 reach가 확대되고 management quality가 재평가되면 2018 FCF/share "
            "$2.37, 2019 $2.90이 가능하다는 논리였다. 시장가격은 target $16.66과 66% upside에서 역산해 약 $10.04다."
        ),
        "reverse": (
            "약 3~4배 forward FCF가 맞으려면 시장은 CBS assets의 decline, revenue synergy 불확실성, integration, 높은 "
            "leverage로 FCF가 common에 귀속되지 않을 위험을 가격에 넣은 것이다. Long 성공에는 cost synergy만이 아니라 "
            "organic station revenue 안정화와 빠른 debt paydown이 필요했다. 둘 중 하나가 빠지면 low multiple은 함정이다."
        ),
        "valuation": (
            "$16.66 target은 2018 FCF/share $2.37의 7배이고, 66% upside에서 역산한 당시 가격은 약 $10.04다. "
            "2019 $2.90은 더 높은 upside를 만들지만 이 FCF가 synergy 전인지 후인지, cash restructuring cost와 interest를 "
            "완전히 반영했는지가 핵심이다. V9에서는 `organic EBITDA + realized cash synergy - cash interest - capex - tax`를 "
            "주식수로 나눈 뒤 debt paydown 전후를 비교한다."
        ),
        "scenarios": [("Bear", "CBS decline 지속·synergy 지연·6x대 leverage", "equity impairment", "실현"), ("Base", "cost synergy·revenue 안정·debt paydown", "$16.66", "실패"), ("Bull", "$2.90 FCF/share·multiple 정상화", "100%+", "실패")],
        "actual": (
            "2017-11-17 거래는 종결됐고 2018 net revenue는 $1.462567bn으로 확대됐다. 그러나 2018-07 별도 VIC Short는 "
            "$8.15, leverage 6.3x, 2018 EBITDA 10.5배를 제시했다. 즉 원 Long의 약 1년 horizon이 끝나기 전 시장가격과 "
            "capital structure가 모두 반증신호를 냈다. 이후 Audacy는 2024년 $1.6bn debt를 equitize해 총 debt를 약 "
            "$1.9bn에서 $350m으로 낮췄다."
        ),
        "price": (
            "원문 target/upside로 진입가를 역산하면 약 $10.04다. 2018-07-23 후속 Short의 $8.15는 약 -18.8%이고 "
            "$16.66 target보다 51.1% 낮다. 동일 timestamp 종가·배당을 이용한 정확한 total return은 아니므로 보조치다. "
            "그러나 1년 안에 +66%라는 방향이 틀렸다는 판단에는 충분하다."
        ),
        "drivers": "Revenue 규모와 일부 cost synergy는 생겼을 수 있으나, acquired stations의 organic decline과 cash interest가 common FCF를 압도했다. 수익모델의 핵심 오류는 synergy dollar를 gross로 더하고 shrinking revenue pool과 debt duration을 독립 stress하지 않은 것이다.",
        "counterfactual": "cost synergy가 계획대로 전부 실현돼도 legacy와 CBS organic revenue가 매년 4~5% 줄었다면 $2.90 FCF/share는 유지될 수 있었나?",
        "error": "좋은 운영진과 합병 synergy를 산업 감소율보다 상위 변수로 놓고, pro forma leverage를 equity survival의 독립조건으로 다루지 않았다.",
        "warning": "2018-07-23 $8.15와 6.3x leverage가 목표기간 안의 명확한 경고였다.",
        "first_signal_date": "2018-07-23",
        "lessons": ["쇠퇴산업 M&A는 synergy보다 revenue-decline plus interest hurdle을 먼저 계산한다.", "pro forma FCF/share는 integration cash cost와 정상화 capex를 포함한다.", "management quality는 narrative가 아니라 cohort별 organic revenue·debt paydown으로 측정한다."],
        "checklist": ["legacy/CBS same-station revenue", "cash synergy timing", "integration cash cost", "cash interest", "net leverage/stressed EBITDA", "FCF/share bridge", "maturity wall"],
        "scorecard": [("Business thesis", "실패"), ("Valuation thesis", "실패"), ("Catalyst thesis", "거래종결만 성공"), ("Timing / path", "실패"), ("Security selection", "levered common 부적절")],
        "claims": [
            C("CBS Radio를 turnaround할 수 있다", "Entercom management가 acquired station 실적을 안정화한다.", "운영규율·현지 영업·programming 개선이 organic revenue와 margin을 회복시킨다.", "Entercom의 과거 operating reputation.", "CBS decline이 일시적이고 management playbook이 이전 가능하다.", "합병 4개 분기 뒤 acquired organic revenue가 안정되지 않으면 반증.", "Scale은 늘었지만 장기 cash economics는 구조조정으로 귀결됐다.", "turnaround cash bridge 미달.", "실패", "management skill의 transferability 과신.", "acquired cohort KPI를 별도 추적한다."),
            C("cost·revenue synergy가 margin을 높인다", "결합자산이 비용절감과 cross-sell을 만든다.", "중복 overhead 제거와 넓어진 reach가 EBITDA를 높인다.", "deal synergy plan.", "organic decline이 synergy dollar보다 작다.", "synergy 후에도 stressed EBITDA가 debt를 5x 이상 남기면 반증.", "2018 revenue는 커졌지만 6.3x leverage와 후일 Chapter 11.", "gross scale 성공·net equity 실패.", "부분 실패", "synergy를 revenue decline과 netting하지 않음.", "net synergy = realized synergy - lost organic EBITDA로 본다."),
            C("2019 FCF/share는 $2.90이다", "full synergy와 turnaround가 두 번째 해 FCF를 더 높인다.", "integration 완료와 debt paydown이 interest를 낮춘다.", "원문 forecast.", "revenue stabilization이 선행된다.", "$2.90의 20% 이상 미달 또는 leverage 정체면 반증.", "후속 capital structure는 forecast와 양립하지 않았다.", "terminal outcome 명확한 실패.", "실패", "base와 bull의 동시조건 중복.", "연도별 FCF bridge에 organic·synergy·interest를 분리한다."),
            C("부채는 manageable하다", "운영실적과 discipline으로 합병 debt를 줄일 수 있다.", "FCF가 mandatory amortization과 refinancing risk를 낮춘다.", "management capital-allocation 평가.", "stressed EBITDA에도 liquidity와 covenant cushion이 충분하다.", "net leverage가 4x 아래로 빠르게 못 내려오면 반증.", "2018 6.3x 추정, 2024 $1.6bn equitization.", "debt-bearing capacity 실패.", "실패", "base EBITDA로만 leverage 계산.", "stressed-normalized leverage를 main case로 둔다."),
            C("1년 내 $16.66이다", "$2.37의 7배와 management rerating으로 66% upside다.", "실적공시가 정보격차를 닫고 multiple을 정상화한다.", "원문 target과 next-year horizon.", "통합 지연 없이 FCF가 가시화된다.", "12개월 전후 가격이 target과 크게 반대면 실패.", "2018-07 $8.15는 역산 진입가보다 약 18.8% 낮았다.", "target 대비 약 -51.1%.", "실패", "timing에 integration lag를 충분히 반영하지 않음.", "target은 operational milestones와 연결한다."),
            C("common equity가 올바른 청구권이다", "높은 equity upside가 integration risk를 보상한다.", "debt 이후 잔여 FCF가 common에 convex하게 귀속된다.", "낮은 forward P/FCF.", "debt 만기가 FCF realization보다 늦다.", "debt가 equity option의 만기를 앞당기면 반증.", "2024 debt equitization이 기존 common보다 앞섰다.", "security waterfall 실패.", "실패", "cheap common multiple에 capital-structure seniority 미반영.", "levered M&A는 debt와 common을 함께 비교한다."),
        ],
        "metrics": [("Implied VIC price", "약 $10.04", "$16.66", "$8.15 2018-07 reference", "역방향"), ("2018 FCF/share", "$2.37", "7x", "exact reconciliation 미복원", "미검증"), ("2019 FCF/share", "$2.90", "100%+ upside", "terminal debt restructuring", "실패"), ("2018 net revenue", "PF scale", "성장", "$1.462567bn", "scale 성공"), ("2024 funded debt", "manageable", "deleveraging", "$1.9bn→$350m", "실패")],
        "timeline": [("2017-08-08", "VIC Long", "$16.66 target"), ("2017-11-17", "CBS Radio close", "transaction catalyst 성공"), ("2018-07-23", "후속 VIC Short $8.15", "기간 내 반증"), ("2018-12-31", "매출 $1.463bn", "scale 확대"), ("2024-01-07", "Chapter 11", "equity waterfall 실패"), ("2024-09-30", "emergence", "debt 약 $350m")],
        "sources": ETM_SOURCES,
    },
])


ORDER = [
    "2eec41d0-f8d6-47ba-822f-c361725a37ee",
    "9bc25044-5526-4075-8977-165259b54e0f",
    "68bfa6f3-94ca-4ba9-903c-9d00eadca05d",
    "3027530a-b943-4fe7-8fb5-ea719a6f9c0b",
    "eaf5eea7-6a56-4f6e-8bc4-44ec3439b962",
    "56eb0e52-b78e-4a38-94c6-20d3fb879b14",
    "0105017c-3cc2-416f-a517-639654c5f8c6",
    "18528fe4-250e-403f-a410-5a34e8688c0b",
    "2698dc16-9bce-40ee-94a2-0ba05ad801f3",
    "75a33add-6ad5-4d30-a3e1-b55d451b3fca",
]

RAW_META = {
    "2eec41d0-f8d6-47ba-822f-c361725a37ee": (22129, 558, None, None, '["자사주", "재무구조", "반복매출", "규제", "자본배분", "SOTP·자산가치", "시장규모·TAM", "이벤트 드리븐"]', "공개매수·자본환원"),
    "9bc25044-5526-4075-8977-165259b54e0f": (5997, 99, "12-18 months", 15, '["자사주", "턴어라운드", "자본배분", "M&A", "이벤트 드리븐"]', "인수합병·매각"),
    "68bfa6f3-94ca-4ba9-903c-9d00eadca05d": (13523, 80, "12-18 months", 15, '["턴어라운드", "영업레버리지", "경영진", "자본배분", "규제"]', "일반 투자논지"),
    "3027530a-b943-4fe7-8fb5-ea719a6f9c0b": (8956, 56, None, None, '["턴어라운드", "경기·사이클", "공매도·과대평가"]', "실적·가이던스"),
    "eaf5eea7-6a56-4f6e-8bc4-44ec3439b962": (10529, 240, "5 years", 60, "[]", "일반 투자논지"),
    "56eb0e52-b78e-4a38-94c6-20d3fb879b14": (8001, 171, None, None, '["자본배분", "자사주", "규제", "이벤트 드리븐"]', "공개매수·자본환원"),
    "0105017c-3cc2-416f-a517-639654c5f8c6": (8269, 107, "3 years", 36, '["청산·자산매각", "M&A", "재무구조", "이벤트 드리븐"]', "인수합병·매각"),
    "18528fe4-250e-403f-a410-5a34e8688c0b": (23968, 179, "24 month", 24, '["청산·자산매각", "재무구조", "규제", "자사주", "SOTP·자산가치", "자본배분", "이벤트 드리븐"]', "공개매수·자본환원"),
    "2698dc16-9bce-40ee-94a2-0ba05ad801f3": (7853, 77, "11 years", 132, '["재무구조", "자본배분", "SOTP·자산가치", "자사주"]', "일반 투자논지"),
    "75a33add-6ad5-4d30-a3e1-b55d451b3fca": (10439, 79, "3-4 months", 4, '["SOTP·자산가치", "자본배분", "회계·포렌식", "이벤트 드리븐"]', "소송·법원"),
}


def ordered_ideas():
    position = {idea_id: n for n, idea_id in enumerate(ORDER)}
    return sorted(IDEAS, key=lambda idea: position[idea["id"]])


def idea_sources(idea):
    if idea["source"]:
        original = S("VIC original idea", idea["source"], "Value Investors Club", idea["date"], "T0 방향·원문 주장·수치·촉매 복원.", "원문")
    else:
        original = S("VIC original text retained in source SQL", "", "Value Investors Club / source SQL", idea["date"], "공개 URL이 저장되지 않은 원문 description·catalyst 복원.", "원문·저장자료")
    return [original, *idea["sources"]]


def render_report(i):
    lines = [
        f"# {i['company']} ({i['ticker']}) — {i['date']} VIC {i['direction']}",
        "",
        "> **Idea unit:** 이 게시일의 증권 한 건만 분석한다. 같은 ticker의 다른 VIC 게시물은 별도 파일이다.",
        f"> **Research as-of:** {ASOF}. 사업·valuation·촉매·증권·가격경로를 분리해 판정한다.",
        "",
        "---",
        "",
        "## 0. Idea Snapshot",
        "",
        "| 항목 | 내용 |",
        "|---|---|",
        f"| 회사 / Ticker | {i['company']} / {i['ticker']} |",
        f"| VIC 게시일 / 작성자 | {i['date']} / {i['author']} |",
        f"| Security / 실제 방향 | {i['security']} |",
        "| 원 SQL 방향 | Short — raw 값 보존; 본문 research direction은 별도 교정 |",
        f"| 기준 진입가격 | {i['entry']} |",
        f"| 기대기간 | {i['horizon']} |",
        f"| raw horizon audit | {i['raw_horizon']} |",
        f"| 최종 판정 | **{i['verdict']}** |",
        "",
        f"> **결론:** {i['conclusion']}",
        "",
        "---",
        "",
        "## 1. 회사는 정확히 무엇을 하는가",
        "",
        BUSINESS[i["ticker"]],
        "",
        ENGINE[i["ticker"]],
        "",
        "### 가치사슬과 common equity 청구권",
        "",
        "광고주가 지불하는 gross revenue가 곧 주주현금은 아니다. Audience와 advertiser demand에서 station·platform 운영비, talent·sales 비용, corporate overhead, cash interest, capex, tax가 차례로 빠진다. Asset sale 아이디어는 여기에 preferred·transaction cost·control decision까지 통과해야 한다. 이 보고서는 매출 증가, EBITDA 증가, common value 증가를 같은 사건으로 취급하지 않는다.",
        "",
        "### 매 분기 볼 핵심 KPI",
        "",
        KPI[i["ticker"]],
        "",
        "---",
        "",
        "## 2. 당시 상황과 시장이 가격에 넣은 것",
        "",
        i["t0"],
        "",
        "### Reverse expectations",
        "",
        i["reverse"],
        "",
        "---",
        "",
        "## 3. 원문 투자논지 지도",
        "",
    ]
    for n, c in enumerate(i["claims"], 1):
        lines.extend([
            f"### C{n}. {c['title']} — {c['verdict']}", "",
            "**원문 주장**", "", c["original"], "",
            "**경제적 메커니즘**", "", c["mechanism"], "",
            "**T0 근거**", "", c["evidence"], "",
            "**숨은 가정**", "", c["assumption"], "",
            "**사전 반증조건**", "", c["falsifier"], "",
            "**실제 결과**", "", c["actual"], "",
            "**정량 gap**", "", c["gap"], "",
            "**분석 오류 또는 제한**", "", c["error"], "",
            "**재사용 교훈**", "", c["lesson"], "",
        ])
    lines.extend([
        "---", "", "## 4. 당시 Valuation과 Payoff Structure", "", i["valuation"], "",
        "### 시나리오 분석", "", "| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |", "|---|---|---|---|",
    ])
    for row in i["scenarios"]:
        lines.append("| " + " | ".join(row) + " |")
    lines.extend(["", "### 핵심 수치", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"])
    for row in i["metrics"]:
        lines.append("| " + " | ".join(row) + " |")
    lines.extend([
        "", "### 촉매와 시간", "", f"원문 기대기간은 **{i['horizon']}**다. 판정에서는 이 기간을 고정한다. 그 뒤의 corporate event는 장기 사업가설 검증에는 쓰되 원 horizon 수익률을 대체하지 않는다.",
        "", "---", "", "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "",
        "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|",
    ])
    for row in i["timeline"]:
        lines.append("| " + " | ".join(row) + " |")
    lines.extend([
        "", "### 실제 사업·자본구조 추이", "", i["actual"],
        "", "---", "", "## 6. 실제 투자결과 — 가격 경로와 실현 가능성", "", i["price"],
        "", "가격 데이터는 배당·세금·거래비용을 포함한 total return과 분리한다. 원 DB에 event-date series가 없으면 수익률·MFE·MAE를 추정해 채우지 않는다. Short는 borrow와 cover rule, event trade는 계약상 payout과 duration이 있어야 exact IRR을 계산한다.",
        "", "---", "", "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 핵심 gap |", "|---|---|---:|---|---|",
    ])
    for n, (c, weight) in enumerate(zip(i["claims"], WEIGHTS), 1):
        lines.append(f"| C{n} | {c['title']} | {weight}% | {c['verdict']} | {c['gap']} |")
    lines.extend([
        "", "---", "", "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", i["drivers"],
        "", "### Counterfactual", "", i["counterfactual"],
        "", "---", "", "## 9. 분석 오류 유형과 최초 경고", "", i["error"],
        "", "### 최초로 관찰 가능했던 경고신호", "", i["warning"],
        "", "---", "", "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", "",
    ])
    for n, lesson in enumerate(i["lessons"], 1):
        lines.extend([f"### Lesson {n}", "", lesson, ""])
    lines.extend(["### 지금 같은 아이디어를 다시 본다면", ""])
    for item in i["checklist"]:
        lines.append(f"- {item}")
    lines.extend(["", "---", "", "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|"])
    for row in i["scorecard"]:
        lines.append("| " + " | ".join(row) + " |")
    lines.extend([
        f"| Thesis score | {i['score']:.1f}/10 |",
        f"| Process score | {i['process']:.1f}/10 |",
        f"| 종합 | **{i['verdict']}** |",
        "", "### 한 문장 교훈", "", f"> {i['lessons'][0]}",
        "", "---", "", "## 12. Sources / Validation Notes", "",
    ])
    for n, source in enumerate(idea_sources(i), 1):
        if source["url"]:
            lines.append(f"{n}. [{source['title']}]({source['url']}) — {source['publisher']}, {source['date']}. {source['evidence']}")
        else:
            lines.append(f"{n}. {source['title']} — {source['publisher']}, {source['date']}. {source['evidence']}")
    lines.extend([
        "", "### 데이터 품질", "",
        "- 원문 방향·작성자·기간·excerpt: **A/B** — 원 source DB와 공개 VIC URL을 대조했다. 공개 URL이 없는 3건은 저장된 SQL 원문을 사용했다.",
        "- 사업·거래·법원·자본구조: **A** — SEC와 회사 1차자료를 우선했다.",
        "- 가격경로: **C 또는 미검증** — 원 DB에 있는 TSQ 단기 ratio와 원문에 명시된 가격만 사용했다. 그 밖의 exact total return·MFE·MAE는 만들지 않았다.",
        "- 원 SQL `is_short=true`는 모든 아이디어에서 감사추적용으로 보존했다. 실제 Long/Short와 multi-leg hedge는 research layer에서 별도로 기록했다.",
        "",
    ])
    return "\n".join(lines)


def make_payload(ideas):
    out = {
        "schema_version": "vic-deep-research-v9",
        "batch": 41,
        "title": "Local Radio / Digital Audio — TSQ, Entercom/Audacy, Emmis V9",
        "research_asof": ASOF,
        **{key: [] for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")},
    }
    for i in ideas:
        desc_chars, catalyst_chars, horizon_raw, horizon_months, raw_tags, raw_type = RAW_META[i["id"]]
        out["ideas_master"].append({
            "idea_id": i["id"], "date": i["date"], "year": int(i["date"][:4]), "ticker": i["ticker"],
            "company_name": i["company"], "author": i["author"], "is_short": 1,
            "direction_ko": "숏", "idea_type_ko": raw_type,
            "source_link": i["source"] or None, "description_chars": desc_chars, "catalyst_chars": catalyst_chars,
            "contest_winner": 0, "auto_tag_status_ko": "raw 방향 보존·본문 방향 수동검증 완료",
            "narrative_tags_ko": raw_tags, "horizon_raw": horizon_raw, "horizon_months": horizon_months,
            "performance_available": 1 if i["ticker"] == "TSQ" else 0,
            "perf_1m": 1.061278863232682 if i["ticker"] == "TSQ" else None,
            "perf_3m": 0.7797513321492007 if i["ticker"] == "TSQ" else None,
            "perf_6m": 0.7513321492007106 if i["ticker"] == "TSQ" else None,
            "perf_1y": None, "perf_2y": None, "perf_3y": None, "perf_5y": None,
            "idea_return_1y": None, "idea_return_3y": None, "idea_return_5y": None,
        })
        out["postmortems"].append({
            "idea_id": i["id"], "ticker": i["ticker"], "research_direction_ko": i["direction"],
            "company_description_ko": BUSINESS[i["ticker"]], "original_thesis_ko": i["t0"],
            "actual_development_ko": i["actual"], "thesis_verdict_ko": i["conclusion"],
            "business_verdict_ko": i["scorecard"][0][1], "catalyst_verdict_ko": i["scorecard"][2][1],
            "valuation_verdict_ko": i["scorecard"][1][1], "stock_verdict_ko": i["price"],
            "current_verdict_ko": i["verdict"], "overall_verdict_ko": i["verdict"], "why_ko": i["drivers"],
            "success_pattern_ko": "claim_mapping; security_mapping; event_calendar; primary_source_validation",
            "failure_pattern_ko": "secular_duration; leverage_path; gross_net_confusion; governance; timing; raw_direction_error",
            "root_error_ko": i["error"], "first_signal_ko": i["warning"], "first_signal_date": i["first_signal_date"],
            "knowable_at_t0_ko": i["claims"][0]["evidence"] + " " + i["claims"][0]["falsifier"],
            "avoidability_ko": "중간 이상. 원문과 T0 filing으로 organic growth, debt, preferred, event dependency, realization timing을 분리할 수 있었다.",
            "counterfactual_question_ko": i["counterfactual"],
            "analyst_note_ko": f"raw SQL Short 보존; 본문 실제 방향은 {i['direction']}. {i['raw_horizon']}",
            "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None,
            "confidence": 0.94 if i["source"] else 0.88, "research_asof": ASOF, "research_status_ko": "1차자료 검증 완료·가격성과 제한 명시",
        })
        out["meta"].append({
            "idea_id": i["id"], "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·가격·event calendar·first break·security payoff 장문분석",
            "report_version": "V9-canonical", "thesis_type_ko": i["title"], "one_line_verdict_ko": i["conclusion"],
            "thesis_score": i["score"], "process_score": i["process"], "return_summary_ko": i["price"],
            "core_error_ko": i["error"], "core_insight_ko": i["lessons"][0], "research_asof": ASOF,
        })
        section_rows = [
            ("회사·가치사슬·현금엔진", f"{BUSINESS[i['ticker']]}\n\n{ENGINE[i['ticker']]}\n\n핵심 KPI: {KPI[i['ticker']]}."),
            ("T0 시장기대·reverse expectations", f"{i['t0']}\n\n{i['reverse']}"),
            ("Valuation·payoff·실제경로", f"{i['valuation']}\n\n실제: {i['actual']}\n\n가격: {i['price']}"),
            ("사후인과·오류·교훈", f"{i['drivers']}\n\n오류: {i['error']}\n\nCounterfactual: {i['counterfactual']}"),
        ]
        for n, (title, body) in enumerate(section_rows, 1):
            out["sections"].append({"idea_id": i["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, (c, weight) in enumerate(zip(i["claims"], WEIGHTS), 1):
            out["claims"].append({
                "idea_id": i["id"], "claim_order": n, "claim_title_ko": c["title"], "thesis_weight_pct": weight,
                "original_claim_ko": c["original"], "t0_evidence_ko": c["evidence"], "key_assumption_ko": c["assumption"],
                "ex_ante_falsifier_ko": c["falsifier"], "actual_result_ko": c["actual"], "quantitative_gap_ko": c["gap"],
                "verdict_ko": c["verdict"], "analytical_error_ko": c["error"], "reusable_lesson_ko": c["lesson"],
            })
        for n, row in enumerate(i["metrics"], 1):
            out["metrics"].append({
                "idea_id": i["id"], "metric_order": n, "metric_name_ko": row[0], "t0_value_ko": row[1],
                "thesis_expectation_ko": row[2], "actual_value_ko": row[3], "verdict_ko": row[4],
                "interpretation_ko": f"{row[0]}의 T0 기대와 실제를 동일 단위가 가능한 범위에서 비교했다.",
            })
        for n, row in enumerate(i["timeline"], 1):
            out["timeline"].append({"idea_id": i["id"], "event_order": n, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for n, source in enumerate(idea_sources(i), 1):
            out["sources"].append({
                "idea_id": i["id"], "source_order": n, "source_type_ko": source["type"], "publisher": source["publisher"],
                "title_ko": source["title"], "source_date": source["date"], "url": source["url"], "evidence_ko": source["evidence"],
            })
    return out


def render_index(ideas):
    lines = [
        "# Batch 041 — Local Radio / Digital Audio V9 Index", "",
        "> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. 원문 방향·기간·증권을 복원하고 SEC/회사 1차자료와 사후 사건을 교차검증했다.", "",
        "## Canonical idea files", "",
        "| 순서 | VIC 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |", "|---:|---|---|---|---|---|---|",
    ]
    for n, i in enumerate(ideas, 1):
        rel = i["filename"].removeprefix("analysis/")
        lines.append(f"| {n} | {i['date']} | {i['ticker']} | Short | {i['direction']} | [{i['date']} {i['ticker']}]({rel}) | {i['verdict']} |")
    lines.extend([
        "", "## Direction / horizon audit", "",
        "10건 모두 raw SQL `is_short=true`다. 실제 원문은 Long 8건, Short 2건이다. ETM 2020은 common Long이 primary recommendation이고 unsecured-bond Short는 optional hedge다. Raw 값은 삭제하지 않고 V9 research layer에서만 방향과 security leg를 교정했다.",
        "",
        "EMMS 2010의 raw 3년은 9월 drop-dead event와 모순되고, EMMS 2013의 raw 11년은 98.7FM lease-return 기간을 horizon으로 잘못 읽었을 가능성이 높다. 이 두 값은 판정에서 제외하고 계약상 event date 또는 ‘명시 없음’을 사용했다.",
        "", "## 핵심 판정 교정", "",
        "1. **TSQ 2022:** digital mix는 성공했지만 2024 Digital revenue는 $233.958m으로 $275m target 대비 14.9% 미달했고 Digital segment profit은 10.2% 감소했다.",
        "2. **ETM 2005:** 12~18개월 가격성과는 미검증이다. 2024 Chapter 11은 짧은 horizon 수익률 대체값이 아니라 장기 FCF-duration thesis의 실패근거로만 썼다.",
        "3. **ETM 2017:** $16.66·1년 target과 달리 2018-07 후속 Short의 $8.15가 기간 내 반증이었다.",
        "4. **ETM 2018:** 구조적 Short는 적중했지만 Chapter 11까지 약 5.5년이므로 borrow-adjusted IRR은 별도 미검증이다.",
        "5. **ETM 2020:** 단기 liquidity survival은 성공했어도 5년 common survival은 게시 후 약 46개월의 Chapter 11로 실패했다.",
        "6. **EMMS 2005:** $394.9m tender는 $100m revolver+$300m notes로 조달한 levered recap이었다. 단순 share-count accretion으로 보지 않았다.",
        "7. **EMMS 2010:** 2/3 preferred consent와 drop-dead date를 이용한 merger-break Short는 event 기준 강한 성공이다.",
        "8. **EMMS 2012~2014:** 자산·법률가치는 존재했지만 $131m WBLS/WLIB acquisition과 $191.6m Credit Agreement, controller/time discount가 common payoff를 약화했다.",
        "", "## Batch 041의 공통 분석식", "",
        "`organic ad/digital contribution - fixed operating cost - corporate overhead - cash interest - maintenance capex - tax = common equity FCF`",
        "",
        "Asset play는 여기에 `sale probability × after-tax proceeds × time discount - debt - preferred - control discount`를 적용한다. M&A는 headline revenue와 EBITDA multiple 대신 acquired/legacy organic trend, post-synergy after-interest FCF, debt paydown years를 본다.",
        "", "## 상위 교훈", "",
        "1. Digital mix 상승은 absolute revenue·segment profit 성장과 다르다.",
        "2. Radio license scarcity는 advertiser attention의 moat가 아니다.",
        "3. 높은 FCF yield는 declining annuity의 짧은 duration을 반영할 수 있다.",
        "4. 위기 Long은 liquidity runway와 solvency runway를 분리한다.",
        "5. Levered recap의 buyback accretion은 pro forma interest 뒤 FCF/share로 검증한다.",
        "6. SOTP에는 corporate overhead·tax·realization probability·time·controller discount를 넣는다.",
        "7. Merger-break Short는 closing threshold와 blocker의 경제적 유인을 수학으로 본다.",
        "", "## 앱/DB 반영", "",
        "- `analysis/batch_041_local_radio_audio_10.md`는 위 10개 canonical 파일을 불러오는 wrapper다.",
        "- `data/curated/batch_041_local_radio_audio_deep_v7.json`은 V9 상세 overlay schema로 재작성했다.",
        "- 기존 idea01~idea10 Markdown은 감사추적용 legacy 파일로 보존했다.", "",
    ])
    return "\n".join(lines)


def main():
    ideas = ordered_ideas()
    if len(ideas) != 10 or {idea["id"] for idea in ideas} != set(ORDER):
        raise ValueError("Batch 041 must contain exactly the ten ordered ideas")
    for idea in ideas:
        if len(idea["claims"]) != 6:
            raise ValueError(f"{idea['id']}: expected six claims")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_report(idea), encoding="utf-8")
    index_path = ROOT / "analysis" / "batch_041_local_radio_audio_v9_index.md"
    index_path.write_text(render_index(ideas), encoding="utf-8")
    parts = "|".join(idea["filename"].removeprefix("analysis/") for idea in ideas)
    wrapper = (
        "# Batch 041 — Local Radio / Digital Audio V9\n\n"
        f"<!-- batch_parts: {parts} -->\n\n"
        "> 이 파일은 Streamlit 호환 wrapper다. canonical index: "
        "[Batch 041 V9 Index](batch_041_local_radio_audio_v9_index.md).\n"
    )
    (ROOT / "analysis" / "batch_041_local_radio_audio_10.md").write_text(wrapper, encoding="utf-8")
    payload = make_payload(ideas)
    payload_path = ROOT / "data" / "curated" / "batch_041_local_radio_audio_deep_v7.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(ideas)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} sources={len(payload['sources'])}")


IDEAS.extend([
    {
        "id": "18528fe4-250e-403f-a410-5a34e8688c0b",
        "date": "2012-10-08", "author": "specialk992", "ticker": "EMMS", "company": "Emmis Communications",
        "filename": "analysis/ideas/2012/2012-10-08_EMMS_long.md",
        "source": "", "direction": "Long", "security": "EMMS Class A common equity / Long", "entry": "정확한 원문 가격 미복원",
        "horizon": "24개월", "raw_horizon": "24 month",
        "title": "liability engineering과 refinancing 촉매를 산 distressed-equity Long",
        "verdict": "이벤트 부분 성공·common payoff 미검증/혼합", "score": 6.0, "process": 6.5,
        "conclusion": (
            "KXOS $85.5m 매각은 게시 전에 이미 완료됐고 pro forma debt가 $90m 아래라는 출발점을 만들었다. 이후 "
            "preferred 구조 관련 2014 district-court 승소는 24개월 안에 발생해 legal catalyst는 맞았다. 그러나 2015 "
            "appellate affirmation은 기간 밖이었고, WBLS/WLIB $131m 인수 뒤 2014 Credit Agreement debt가 $191.6m으로 "
            "다시 커졌다. Mid $5·low $2.77·high $6.74의 정확한 주가성과는 미복원이라 ‘부분 성공’으로 제한한다."
        ),
        "t0": (
            "2010 take-private 실패 뒤 Emmis는 preferred voting·swap·retention-plan 구조를 재편했고 assets를 팔아 senior "
            "debt를 낮췄다. 2012-08 KXOS-FM을 $85.5m에 매각했고 publishing sale $8.7m 등을 반영한 원문 pro forma "
            "debt는 $90m 미만이었다. 시장이 복잡한 capital structure를 잘못 계산한다고 보고 imminent refinancing, "
            "insider buying, 향후 dividends/buybacks를 촉매로 Long을 제시했다."
        ),
        "reverse": (
            "가격이 싼 이유는 preferred restructuring이 법원에서 뒤집힐 가능성, controller discount, radio duration, "
            "asset sale cash가 새 M&A로 다시 레버리지될 가능성이었다. Low case $2.77이 진짜 floor가 되려면 legal claim과 "
            "tax를 충분히 차감하고, refinancing 뒤 management가 debt를 다시 늘리지 않아야 했다."
        ),
        "valuation": (
            "원문 SOTP는 low $2.77, mid $5.00, high $6.74였다. V9에서는 station value에 sale probability·tax·time "
            "discount를 곱하고 enforceable debt와 preferred claims를 뺀다. KXOS sale은 valuation 입력이 아니라 이미 "
            "현금화된 T0 balance-sheet 항목이다. 향후 refinancing과 legal outcome만 catalyst probability로 둬야 double "
            "counting을 피할 수 있다."
        ),
        "scenarios": [("Bear", "preferred 구조 무효·refi 실패·재레버리지", "$2.77 이하", "재레버리지 위험 현실화"), ("Base", "district win·refi·안정 station value", "$5.00", "법률 성공·가격 미검증"), ("Bull", "claim 제거·buyback·asset rerating", "$6.74", "정확한 payoff 미검증")],
        "actual": (
            "KXOS sale은 2012-08-23 $85.5m cash, 약 $32.8m gain으로 게시 전 완료됐다. Preferred plaintiffs의 injunction은 "
            "기각됐고 2014-02-28 district court가 Emmis에 유리하게 판결했다. 2015-07 Seventh Circuit도 만장일치로 "
            "affirm했다. 반면 회사는 2014 WBLS/WLIB를 $131m에 인수했고 2015-08 Credit Agreement carrying amount는 "
            "$191.6m이었다. Legal liability 감소가 곧 permanent deleveraging을 의미하지는 않았다."
        ),
        "price": (
            "원 DB에 event-date prices가 없어 $2.77/$5/$6.74 band 도달 여부와 24개월 total return을 확정하지 않는다. "
            "2014 district win이 기간 내 발생한 것은 catalyst 성공이고, 2015 affirmation과 2019 monetization은 original "
            "horizon 밖의 장기 관찰치다."
        ),
        "drivers": "가치증가는 asset sale과 preferred legal risk 감소에서 나왔다. 할인 지속은 controller/governance, radio duration, 재인수로 인한 leverage 증가가 만들었다. Liability engineering이 맞아도 이후 capital allocation이 그 가치를 다시 소모할 수 있다.",
        "counterfactual": "Preferred claim이 줄어든 직후 $131m acquisition으로 debt가 재증가한다면 T0 NAV improvement는 실제 common 가치창출인가, 단순 balance-sheet round trip인가?",
        "error": "KXOS처럼 이미 발생한 event를 미래 catalyst와 섞고, liability reduction 후 management가 debt를 다시 늘릴 policy risk를 low case에 충분히 반영하지 않았다.",
        "warning": "2014-02 $131m WBLS/WLIB 인수는 asset-sale/deleveraging thesis가 acquisition/releveraging thesis로 바뀌는 첫 경고였다.",
        "first_signal_date": "2014-02-11",
        "lessons": ["Distressed equity에서는 liability engineering과 이후 capital allocation을 연속된 하나의 bridge로 본다.", "이미 완료된 asset sale은 catalyst가 아니라 T0 balance sheet다.", "법적 승소 뒤에도 governance·releveraging discount를 0으로 두지 않는다."],
        "checklist": ["T0 pro forma debt", "preferred/legal claim probability", "refi coupon·maturity", "asset-sale proceeds use", "new M&A guardrail", "after-tax NAV", "controller discount"],
        "scorecard": [("Business thesis", "혼합"), ("Valuation thesis", "미검증"), ("Catalyst thesis", "legal 성공"), ("Timing / path", "district win 기간 내"), ("Security selection", "common은 governance 노출")],
        "claims": [
            C("asset sales로 debt가 $90m 아래다", "KXOS·publishing sale 뒤 재무위험이 크게 낮아졌다.", "현금매각과 mandatory repayment가 interest·refi risk를 낮춘다.", "KXOS $85.5m, publishing $8.7m, 원문 sources/uses.", "pro forma debt 계산에 모든 claim·fee가 포함된다.", "12개월 내 debt가 다시 크게 늘면 thesis 약화.", "KXOS는 cash를 만들었으나 2015 Credit Agreement $191.6m.", "초기 사실 적중·지속성 실패.", "부분 성공", "point-in-time deleveraging을 policy로 외삽.", "순부채 변화는 후속 M&A까지 연결한다."),
            C("preferred liability engineering이 유지된다", "swap·vote·retention 구조가 common의 senior claim을 줄인다.", "법적으로 유효하면 residual NAV가 커진다.", "2012 구조와 injunction denial.", "법원이 fiduciary·securities claims를 기각한다.", "injunction·judgment로 구조가 무효면 반증.", "2014 district win, 2015 appellate affirmation.", "법적 방향 적중.", "성공", "최종기간은 24개월을 넘음.", "법률 outcome과 timing을 분리한다."),
            C("imminent refinancing이 촉매다", "낮아진 debt가 더 나은 terms로 refinance된다.", "coupon·maturity 개선이 common FCF와 survival을 높인다.", "원문 catalyst.", "시장 access와 radio cash flow가 안정적이다.", "refi가 비싸거나 새 acquisition debt로 대체되면 약화.", "새 credit agreement는 확보됐으나 acquisition 후 $191.6m로 확대.", "access 성공·deleveraging 실패.", "부분 성공", "refi 존재와 경제성을 혼동.", "coupon·maturity·net debt 세 축으로 판정한다."),
            C("insider buying이 downside를 제한한다", "controller와 insiders의 매수가 value signal이다.", "ownership alignment가 underpricing과 capital return을 시사한다.", "원문 insider activity.", "controller의 utility가 minority IRR과 일치한다.", "related-party action·delisting·재레버리지가 나타나면 반증.", "장기적으로 governance discount와 voluntary delisting.", "downside floor로 불충분.", "실패", "ownership과 alignment 혼동.", "controller incentive를 cash distribution으로 검증한다."),
            C("common value는 $2.77~$6.74다", "updated SOTP가 시장가격보다 높다.", "radio value에서 debt·preferred를 차감한 residual이다.", "원문 low/mid/high cases.", "overhead·tax·time·control discount가 충분히 반영된다.", "실제 monetization net proceeds가 SOTP를 크게 밑돌면 반증.", "가격 series 미복원; 자산가치는 후일 일부 현금화.", "exact valuation 판정 불가.", "미검증", "nominal NAV를 liquid floor로 볼 위험.", "probability/time-adjusted NAV를 쓴다."),
            C("24개월이면 가치가 드러난다", "refi·법원·capital return이 two-year horizon에 발생한다.", "법률과 financing milestones가 discount를 닫는다.", "원 DB 24 month.", "appeal·governance delay가 제한적이다.", "24개월 뒤에도 핵심 uncertainty가 남으면 timing 실패.", "district win은 17개월 내, appellate affirmation은 33개월 후.", "첫 법률단계 성공·완결 지연.", "부분 성공", "sequential legal duration 과소평가.", "court milestones별 확률과 시간을 둔다."),
        ],
        "metrics": [("Value range", "$2.77 / $5.00 / $6.74", "24개월 rerating", "price 미복원", "미검증"), ("KXOS sale", "$85.5m", "deleveraging", "게시 전 완료·$32.8m gain", "T0 사실"), ("Pro forma debt", "<$90m", "refi 후 안정", "$191.6m Credit Agreement 2015-08", "지속성 실패"), ("District decision", "pending", "승소", "2014-02-28 승소", "성공"), ("Appeal", "미정", "affirm", "2015-07-02 affirm", "기간 지연")],
        "timeline": [("2012-08-23", "KXOS sale", "$85.5m·게시 전"), ("2012-10-08", "VIC Long", "24개월"), ("2014-02-11", "WBLS/WLIB deal", "$131m·재레버리지"), ("2014-02-28", "district win", "기간 내 catalyst"), ("2015-07-02", "appeal affirmed", "기간 밖 완결"), ("2020-05", "delisting", "governance/liquidity")],
        "sources": [EMMS_SOURCES["kxos"], EMMS_SOURCES["litigation"], EMMS_SOURCES["wbls"], EMMS_SOURCES["q2015"], EMMS_SOURCES["k2016"], EMMS_SOURCES["mediaco"], EMMS_SOURCES["delist"]],
    },
    {
        "id": "2698dc16-9bce-40ee-94a2-0ba05ad801f3",
        "date": "2013-07-18", "author": "bowd57", "ticker": "EMMS", "company": "Emmis Communications",
        "filename": "analysis/ideas/2013/2013-07-18_EMMS_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/EMMIS_COMMUNICATIONS_CP-CL_A/9284550843",
        "direction": "Long", "security": "EMMS Class A common equity / Long", "entry": "약 $2.75",
        "horizon": "명시 없음", "raw_horizon": "DB parser 11년은 98.7FM 반환기간 오인 가능성이 높아 판정 제외",
        "title": "station SOTP는 맞았지만 realization·overhead·control discount가 부족한 Long",
        "verdict": "자산가치 부분 성공·common realization 지연/미흡", "score": 5.5, "process": 6.0,
        "conclusion": (
            "원문은 radio fair value $220.8m에서 debt 약 $66m을 빼 NAV $154.8m, 주당 $3.44를 계산했다. 2019 "
            "WQHT/WBLS가 $91.5m cash+$5m note+MediaCo 23.72% stake로 현금화돼 major-market asset value는 확인됐다. "
            "그러나 원문이 SOTP에서 corporate overhead를 제외한다고 명시한 점, 지배주주 capital allocation을 스스로 "
            "경계한 점, 2014 $131m acquisition으로 debt가 다시 늘어난 점 때문에 nominal NAV는 즉시 common floor가 아니었다."
        ),
        "t0": (
            "시장가격 약 $2.75에서 WQHT·KPWR와 Austin/St. Louis/Indianapolis clusters를 자산별 평가하고 debt를 빼면 "
            "$3.44가 나왔다. 여기에 Disney에 leased된 98.7FM의 장기 반환, NextRadio, Hungary claim, magazine을 option으로 "
            "더했다. 원문은 과거 station sales가 carrying value를 웃돌았다는 점을 근거로 appraisal을 지지했지만, "
            "corporate overhead는 SOTP에서 무시하고 있었다."
        ),
        "reverse": (
            "약 25% NAV discount는 station appraisal 오류만이 아니라 tax, sale timing, overhead, debt covenant, illiquidity, "
            "controller decision을 반영했을 수 있다. 특히 debt가 adjusted EBITDA 2.5x 아래여야 dividend·repurchase가 "
            "가능하다는 제약은 자산가치가 있어도 common에 전달되는 경로가 막혀 있음을 뜻했다."
        ),
        "valuation": (
            "원문 nominal 식은 $220.818m radio FV - 약 $66m debt = 약 $154.8m NAV, $3.44/share다. V9 식은 "
            "`Σ(asset value×sale probability×after-tax factor×time discount) - debt - preferred - PV(overhead)`다. "
            "Corporate overhead를 영구자본화하고 hidden options는 추가투자와 성공확률을 차감해야 한다. $3.44는 target이라기보다 "
            "unadjusted gross NAV에 가깝다."
        ),
        "scenarios": [("Bear", "overhead·controller·releveraging", "NAV discount 영구화", "상당 부분 실현"), ("Base", "station value 유지·부분 monetization", "$3.44 근처", "자산가치 확인·가격 미검증"), ("Bull", "98.7FM·NextRadio·Hungary option", "NAV 추가 상승", "핵심 engine으로 미실현")],
        "actual": (
            "2014 Emmis는 WBLS/WLIB를 $131m에 사며 NYC cluster를 키웠고 debt를 다시 늘렸다. 2019에는 WQHT와 WBLS를 "
            "MediaCo에 넘겨 $91.5m cash, $5m convertible note, MediaCo Class A 1,666,667주를 받았다. 이 지분은 closing "
            "직후 23.72% 경제지분이지만 3.02% voting interest였다. Asset value는 실재했지만 control과 realization "
            "waterfall은 nominal appraisal보다 불리했고 2020 Emmis는 Nasdaq에서 자진 delist했다."
        ),
        "price": (
            "$2.75 entry와 $3.44 NAV는 복원했으나 명시 horizon과 가격 series가 없다. 2019 monetization까지 약 6.4년이 "
            "걸렸고 cash 외에 note·minority equity가 섞였다. 이 corporate consideration을 common 주가수익으로 대체하지 "
            "않으며 exact IRR·MFE·MAE는 미검증이다."
        ),
        "drivers": "Asset scarcity는 맞았지만 수익은 gross appraisal이 아니라 controller가 언제 어떤 구조로 파는지에 달렸다. 2019 deal의 cash·note·non-control stake는 value existence와 value delivery의 차이를 잘 보여준다.",
        "counterfactual": "$220.8m station appraisal이 정확해도 overhead의 영구가치, 6년 지연, tax, 재레버리지를 넣으면 $3.44 common NAV가 얼마나 남는가?",
        "error": "Corporate overhead를 무시했고 hidden options를 비용·확률 없이 더했다. 낮은 NAV discount를 catalyst로 보면서 controller가 이를 해소할 유인은 약하게 다뤘다.",
        "warning": "2014-02 $131m WBLS/WLIB 인수는 자산매각 대신 재투자·재레버리지를 선택한다는 첫 observable warning이었다.",
        "first_signal_date": "2014-02-11",
        "lessons": ["SOTP에는 realization probability, after-tax proceeds, timing, PV(overhead)를 넣는다.", "경제지분과 voting interest를 분리해 control discount를 계산한다.", "장기 lease 반환·legal claim·technology option은 자본투입 후 확률가중 가치만 더한다."],
        "checklist": ["asset별 sale comps", "tax basis", "PV corporate overhead", "debt/preferred", "covenant distribution gate", "controller incentive", "timing discount", "voting vs economic stake"],
        "scorecard": [("Business thesis", "asset value 성공"), ("Valuation thesis", "부분"), ("Catalyst thesis", "지연"), ("Timing / path", "미흡"), ("Security selection", "minority common discount")],
        "claims": [
            C("Radio fair value는 $220.8m이다", "major-market station appraisal 합계가 carrying value를 웃돈다.", "희소 spectrum·브랜드·audience가 strategic value를 만든다.", "과거 station sale evidence와 자산별 estimate.", "comps·tax·market trend가 유효하다.", "실제 sale value가 appraisal보다 크게 낮으면 반증.", "2019 NY assets가 상당한 현금·note·equity consideration을 만들었다.", "전체 portfolio exact compare는 불가.", "부분 성공", "자산 cohort와 T0 appraisal 단위 불일치.", "appraisal은 asset별 after-tax comp로 검증한다."),
            C("Debt 차감 NAV는 $3.44/share다", "$220.8m-$66m=$154.8m, 주당 $3.44다.", "gross assets에서 financial claims를 뺀 common residual이다.", "원문 debt·share count.", "overhead·preferred·tax·dilution이 충분히 반영된다.", "new debt 또는 overhead PV가 discount를 소진하면 반증.", "2014 acquisition과 2015 $191.6m Credit Agreement로 debt 재증가.", "point-in-time NAV의 지속성 실패.", "부분 실패", "dynamic capital allocation 누락.", "NAV는 pro forma transactions까지 roll-forward한다."),
            C("과거 매각이 fair value를 검증한다", "station sales가 carrying/FV 이상이므로 appraisal 신뢰가 높다.", "realized transactions가 private-market mark를 제공한다.", "원문 과거 sale observations.", "매각 cohort·시점·세금이 보유자산과 비교 가능하다.", "후속 sale의 net multiple이 낮으면 반증.", "2019 monetization은 value 존재를 확인했지만 구조가 복잡했다.", "gross value 확인·common 전달 미완전.", "부분 성공", "selection bias·gross/net 혼동.", "sale comp는 net proceeds와 cohort quality를 맞춘다."),
            C("98.7FM·NextRadio·Hungary는 무료 option이다", "base NAV 밖 hidden assets가 추가 upside를 만든다.", "장기 반환·기술채택·법률회수가 비선형 payoff를 준다.", "원문 option list.", "추가 cash burn이 제한되고 권리가 common에 귀속된다.", "option 유지비가 커지거나 commercialization이 없으면 0.", "핵심 value realization engine으로 확인되지 않았다.", "구체 cash contribution 미복원.", "실패/미검증", "free option의 carrying cost 누락.", "옵션은 cash burn과 만료를 함께 평가한다."),
            C("NAV discount는 시간이 해결한다", "business momentum과 조용한 운영이 가격을 NAV로 이끈다.", "실적·매각이 정보격차와 stigma를 줄인다.", "원문 catalyst.", "controller가 realization을 선택한다.", "추가 M&A·distribution gate·delisting이면 반증.", "2019까지 monetization 지연, 2020 voluntary delisting.", "realization 기간·liquidity 미흡.", "실패", "명시된 강제 catalyst 부재.", "SOTP에는 self-help 또는 liquidation mechanism이 필요하다."),
            C("Corporate overhead 무시는 보수적이다", "자산가치 비교에서 corporate cost를 제외해도 upside가 남는다.", "순수 asset appraisal이 operating noise를 제거한다.", "원문이 overhead 제외를 명시.", "buyer가 overhead를 흡수하거나 곧 청산한다.", "standalone overhead가 지속되면 직접 차감.", "회사는 수년 지속됐고 자산별 거래 뒤에도 corporate 구조가 남았다.", "PV overhead 누락.", "실패", "holding company cost를 0으로 둠.", "지속 overhead는 영구가치로 차감한다."),
        ],
        "metrics": [("VIC price", "약 $2.75", "NAV convergence", "exact return 미복원", "미검증"), ("Radio FV", "$220.818m", "현금화", "부분 monetization", "부분"), ("Debt", "약 $66m", "유지/감소", "$191.6m Credit Agreement 2015", "실패"), ("NAV/share", "$3.44", "약 25% upside", "가격 미복원", "미검증"), ("MediaCo consideration", "미포함", "option", "$91.5m+$5m note+23.72% stake", "value 확인")],
        "timeline": [("2013-07-18", "VIC Long", "$2.75 vs $3.44 NAV"), ("2014-02-11", "WBLS/WLIB acquisition", "$131m·재레버리지"), ("2015-08", "Credit Agreement $191.6m", "NAV debt 상승"), ("2019-11-25", "MediaCo closing", "NY assets monetized"), ("2020-04-21", "delist 결정", "liquidity discount"), ("2020-05", "Nasdaq exit", "public catalyst 종료")],
        "sources": [EMMS_SOURCES["wbls"], EMMS_SOURCES["q2015"], EMMS_SOURCES["mediaco"], EMMS_SOURCES["separation"], EMMS_SOURCES["delist"]],
    },
    {
        "id": "75a33add-6ad5-4d30-a3e1-b55d451b3fca",
        "date": "2014-10-30", "author": "WKB319", "ticker": "EMMS", "company": "Emmis Communications",
        "filename": "analysis/ideas/2014/2014-10-30_EMMS_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/EMMIS_COMMUNICATIONS_CP-CL_A/4256590307",
        "direction": "Long", "security": "EMMS Class A common equity / Long", "entry": "약 $1.90",
        "horizon": "3~4개월", "raw_horizon": "3-4 months",
        "title": "WBLS synergy·appeal·hidden assets의 빠른 rerating을 기대한 Long",
        "verdict": "asset/legal claim 성공·3~4개월 equity payoff 실패/미검증", "score": 5.0, "process": 5.5,
        "conclusion": (
            "WBLS/WLIB $131m acquisition의 strategic value와 preferred appeal은 결국 회사에 유리하게 전개됐다. Seventh "
            "Circuit은 2015-07 district ruling을 만장일치로 affirm했고 2019 NY stations는 MediaCo 거래에서 현금·note·지분 "
            "가치를 만들었다. 그러나 appeal은 원문의 3~4개월보다 늦었고 2015-08 Credit Agreement debt는 $191.6m이었다. "
            "숨은자산이 존재한다는 것과 약 $1.90 common이 수개월 안에 100%+ 오르는 것은 다른 주장이다."
        ),
        "t0": (
            "Emmis는 2014 WBLS/WLIB를 $131m에 사 HOT97과 NYC cluster를 만들었다. 원문은 약 $3m cost savings와 "
            "revenue synergy를 반영하면 약 7.1x BCF이고 station operating income을 거의 두 배로 만들 수 있다고 봤다. "
            "2014-02 district-court 승소 후 appeal, transaction close, eventual sale을 촉매로 두고 NOL·98.7FM·기타 hidden "
            "assets를 합치면 약 $1.90에서 100%+ upside라고 주장했다."
        ),
        "reverse": (
            "시장 discount는 appeal duration, $131m debt-funded acquisition, corporate overhead, controller history, radio "
            "decline을 반영했다. 100%+가 되려면 7.1x가 headline이 아니라 after-interest cash multiple이어야 하고, appeal "
            "승소와 asset realization이 3~4개월 내 common price에 전달돼야 했다."
        ),
        "valuation": (
            "7.1x after-synergy BCF는 acquisition asset-level multiple이지 equity multiple이 아니다. Common valuation은 "
            "증분 BCF에서 cash interest·integration cost·maintenance capex·tax를 뺀 뒤 acquisition debt를 차감해야 한다. "
            "Hidden assets도 NOL 사용가능성, sale tax, time discount를 적용한다. 원문 100%+ target은 여러 옵션의 동시 "
            "실현과 prompt rerating을 요구했다."
        ),
        "scenarios": [("Bear", "synergy 미달·appeal reversal·debt", "common impairment", "debt risk 현실화"), ("Base", "appeal affirm·cluster cash flow", "NAV 일부 반영", "법률 성공·지연"), ("Bull", "hidden assets sale·100%+ rerating", "2배 이상", "2019 value realization·기간 실패")],
        "actual": (
            "District court 승소는 게시 전인 2014-02에 이미 발생했다. Appeal oral argument는 2014-12였고 Seventh Circuit은 "
            "2015-07-02 만장일치로 판결을 affirm했다. 2015-08 Credit Agreement carrying value는 $191.6m이고 98.7FM 등 "
            "non-recourse debt도 별도였다. 2019 WQHT/WBLS MediaCo transaction은 $91.5m cash, $5m note, 23.72% economic "
            "stake를 만들었지만 posting 후 약 5년이 걸렸다."
        ),
        "price": (
            "약 $1.90 entry, 100%+ expected upside, 3~4개월 horizon은 복원했다. 하지만 2015-01~02 exact price와 배당·"
            "liquidity를 복원하지 못해 target miss의 숫자는 만들지 않는다. 확인 가능한 appeal resolution은 8개월 뒤, "
            "asset monetization은 5년 뒤였으므로 event timing은 명시 horizon을 넘었다."
        ),
        "drivers": "장기 자산가치는 major-market station과 favorable litigation에서 나왔지만, common IRR은 acquisition debt, overhead, controller discount, event delay가 결정했다. Asset-level accretion을 equity-level rerating으로 바로 번역한 것이 문제였다.",
        "counterfactual": "$131m acquisition이 7.1x BCF여도 전액 debt 조달과 radio decline을 반영한 incremental equity IRR이 자본비용을 넘었는가?",
        "error": "게시 전 district win을 미래 catalyst처럼 겹쳐 보고, appeal·sale의 순차적 기간과 debt waterfall을 100%+ target에 충분히 haircut하지 않았다.",
        "warning": "3~4개월 horizon이 끝날 때까지 appeal 결정이 없었다면 timing thesis는 깨진 것이다. 2015-08 $191.6m Credit Agreement는 valuation risk를 추가 확인했다.",
        "first_signal_date": "2015-02-28",
        "lessons": ["Acquisition BCF multiple과 equity IRR을 구분한다.", "이미 발생한 법원승소는 T0 fact이고 appeal만 미래 catalyst다.", "Hidden asset은 after-tax waterfall과 realization date를 통과한 common cash로 평가한다."],
        "checklist": ["purchase price·funding", "synergy dollar·timing", "incremental cash interest", "appeal calendar", "NOL usability", "after-tax sale proceeds", "controller distribution", "horizon exit"],
        "scorecard": [("Business thesis", "asset 부분 성공"), ("Valuation thesis", "혼합"), ("Catalyst thesis", "성공·지연"), ("Timing / path", "실패"), ("Security selection", "common realization 위험")],
        "claims": [
            C("WBLS/WLIB는 7.1x after-synergy BCF다", "$131m deal이 cost·revenue synergy 후 싸다.", "cluster density가 sales·programming·overhead를 공유한다.", "회사 발표와 원문 synergy estimate.", "$3m cost saving과 revenue synergy가 cash로 실현된다.", "증분 BCF가 interest·integration을 못 덮으면 반증.", "NY asset은 2019 monetization 가치가 있었으나 standalone synergy bridge 미복원.", "strategic value 확인·7.1x exact 미검증.", "부분 성공", "asset multiple과 equity return 혼동.", "증분 after-interest FCF로 인수 IRR을 계산한다."),
            C("station operating income이 거의 두 배다", "NY cluster가 consolidated station profit을 크게 높인다.", "고정비 sharing과 audience scale이 contribution을 키운다.", "회사 transaction announcement.", "기존 station decline이 synergy를 상쇄하지 않는다.", "organic station income이 계획보다 낮으면 반증.", "회사는 규모를 늘렸으나 debt도 크게 늘었다.", "consolidated cohort exact gap 미복원.", "미검증", "company pro forma claim을 그대로 사용.", "acquired cohort actual을 별도 공시로 맞춘다."),
            C("preferred appeal은 승소한다", "district win이 appeal에서도 유지된다.", "senior claim·legal uncertainty 감소가 common NAV를 높인다.", "게시 전 district decision과 legal record.", "Seventh Circuit이 reversal하지 않는다.", "reversal·remand면 반증.", "2015-07-02 unanimous affirmation.", "방향 성공·3~4개월보다 늦음.", "성공·지연", "법률 duration 낙관.", "appeal outcome과 decision timing을 따로 확률화한다."),
            C("NOL·98.7FM 등 hidden assets가 100%+ upside다", "base operation 밖 자산이 equity value를 두 배 이상으로 만든다.", "세금절감·lease 반환·asset sale이 cash option을 제공한다.", "원문 hidden-asset list.", "권리가 common에 귀속되고 cash burn·세금이 작다.", "사용제한·지연·추가투자로 PV가 작으면 반증.", "2019 NY asset은 value를 만들었지만 기타 option의 핵심 cash contribution은 미확인.", "일부 value·전체 100% bridge 미검증.", "부분", "여러 option의 동시실현을 base에 포함.", "option별 probability·expiry·cash burn을 둔다."),
            C("Debt waterfall은 감당 가능하다", "synergy와 refinancing이 acquisition debt를 흡수한다.", "증분 cash가 interest 후 leverage를 낮춘다.", "7.1x purchase multiple.", "cash interest와 legacy decline이 낮다.", "Credit Agreement와 other debt가 NAV를 크게 차감하면 반증.", "2015-08 Credit Agreement $191.6m, additional non-recourse debt 존재.", "gross asset와 common 사이 gap 확대.", "실패", "debt를 headline multiple 뒤로 숨김.", "asset deal은 pro forma capitalization부터 본다."),
            C("3~4개월 내 100%+ rerating이다", "appeal·close가 시장 discount를 빠르게 해소한다.", "binary catalyst가 NAV를 price에 전달한다.", "원문 horizon·upside.", "events가 기간 내 끝나고 liquidity가 충분하다.", "4개월 내 appeal 미결·price 미반응이면 timing 실패.", "appeal은 약 8개월, major monetization은 약 5년 뒤.", "event duration 명확히 초과.", "실패", "sequential catalysts를 병렬로 취급.", "event tree에 각 단계의 calendar를 더한다."),
        ],
        "metrics": [("VIC price", "약 $1.90", "100%+ upside", "exact horizon price 미복원", "미검증"), ("WBLS/WLIB price", "$131m", "7.1x after synergy", "asset value 확인·exact IRR 미복원", "부분"), ("Appeal", "pending", "3~4개월 win", "2015-07 affirmation", "지연"), ("Credit Agreement", "인수 전제", "manageable", "$191.6m 2015-08", "위험"), ("MediaCo consideration", "hidden", "eventual sale", "$91.5m+$5m+23.72%", "장기 실현")],
        "timeline": [("2014-02-11", "WBLS/WLIB announcement", "$131m"), ("2014-02-28", "district win", "게시 전 T0 fact"), ("2014-10-30", "VIC Long", "$1.90·3~4개월"), ("2015-02", "horizon 종료", "appeal 미결"), ("2015-07-02", "appeal affirmed", "방향 성공·지연"), ("2019-11-25", "MediaCo close", "asset value 장기 실현")],
        "sources": [EMMS_SOURCES["wbls"], EMMS_SOURCES["litigation"], EMMS_SOURCES["q2015"], EMMS_SOURCES["k2016"], EMMS_SOURCES["mediaco"], EMMS_SOURCES["separation"], EMMS_SOURCES["delist"]],
    },
])


IDEAS.extend([
    {
        "id": "56eb0e52-b78e-4a38-94c6-20d3fb879b14",
        "date": "2005-12-30", "author": "pman908", "ticker": "EMMS", "company": "Emmis Communications",
        "filename": "analysis/ideas/2005/2005-12-30_EMMS_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/Emmis_Communications/7932687054",
        "direction": "Long", "security": "EMMS Class A common equity / Long", "entry": "정확한 원문 가격 미복원",
        "horizon": "명시 없음", "raw_horizon": "원 DB horizon 없음",
        "title": "TV 매각 후 radio stub의 FCF/주 복리를 기대한 Long",
        "verdict": "asset-sale 이벤트 성공·residual compounding 실패", "score": 5.0, "process": 5.5,
        "conclusion": (
            "TV division 매각과 대규모 tender라는 corporate action은 실재했다. 그러나 2005-06 tender는 $394.9m 중 "
            "약 $400m을 revolver와 floating-rate notes로 조달해, 즉시 deleveraging이 아니라 levered recap이었다. 이후 "
            "TV exit가 완료됐어도 radio FCF/share가 연 5~10% 복리로 늘어난다는 residual thesis는 장기적으로 실패했고 "
            "Emmis는 2020년 자진상장폐지했다. 이벤트 수익과 남은 사업의 복리수익을 분리해야 한다."
        ),
        "t0": (
            "Emmis는 radio·TV·magazine을 가진 media conglomerate였고 TV 자산을 순차 매각 중이었다. 2005-06에는 "
            "20.25m주를 $19.50에 tender해 share count를 크게 줄였다. 게시시점 논지는 남은 TV proceeds로 debt를 줄이고, "
            "radio FCF를 debt paydown·추가 repurchase에 쓰면 FCF/share가 연 5~10% 늘어난다는 것이었다. Washington "
            "Nationals 계약 무산, 광고 category 확대, CEO LBO도 optional catalyst였다."
        ),
        "reverse": (
            "Per-share accretion은 share count 감소만 보면 커 보이지만 tender financing으로 debt와 interest가 동시에 "
            "늘었다. 가격이 싸려면 TV proceeds가 gross headline에 가깝게 현금화되고 세금·fee 뒤 debt를 실제 상환하며, "
            "남은 radio FCF decline이 작아야 했다. 시장 discount는 이 capital-allocation circularity와 지배주주 옵션을 "
            "반영했을 수 있다."
        ),
        "valuation": (
            "원문은 post-sale radio를 약 12x pro forma FCF, Chicago를 제외하면 8~9x로 봤다. 그러나 올바른 denominator는 "
            "tender 전 FCF가 아니라 새 notes 이자와 매각 후 corporate overhead를 뺀 residual FCF다. TV proceeds도 gross "
            "value가 아니라 세금·거래비용·mandatory debt repayment 후 common에 남는 cash로 계산해야 한다."
        ),
        "scenarios": [("Bear", "매각 지연·radio 감소·interest 부담", "levered stub value trap", "장기 실현"), ("Base", "TV sale·debt paydown·안정 FCF", "5~10% FCF/주", "event만 부분 실현"), ("Bull", "추가 buyback·LBO·광고 optionality", "높은 rerating", "지속적 실현 미확인")],
        "actual": (
            "2005-06 Emmis는 20.25m주를 $19.50, 총 $394.9m에 tender했다. filing은 $100m revolver와 $300m "
            "floating-rate notes로 tender와 fee를 조달했다고 밝힌다. 회사는 TV division 매각을 계속해 2008-07 마지막 "
            "WVUE를 $41m에 팔며 exit를 완료했다. Corporate events는 진행됐지만 residual radio의 구조적 압력과 반복된 "
            "capital-structure/governance 이슈로 장기 compounder가 되지 못했고 2020 Nasdaq에서 자진 delist했다."
        ),
        "price": (
            "원문 entry와 명시 horizon, DB performance가 없어 exact stock IRR·MFE·MAE는 산출하지 않는다. Tender는 "
            "게시 전에 완료됐으므로 게시 후 catalyst 수익으로 세면 안 된다. 판정은 TV-sale execution 성공과 그 뒤 "
            "radio stub의 장기 common value 실패를 분리한 것이다."
        ),
        "drivers": "맞은 부분은 방송자산이 거래 가능한 현금가치를 가졌다는 점이다. 실패한 부분은 leveraged tender의 이자비용, stranded overhead, radio decline, 지배주주 재투자를 충분히 haircut하지 않고 share count 감소를 곧바로 per-share compounding으로 본 것이다.",
        "counterfactual": "20.25m주를 없애도 $400m의 새 debt가 생겼다면, TV 세후 proceeds와 radio FCF가 몇 년 안에 그 debt를 상환해야 실제 FCF/share가 늘었을까?",
        "error": "Tender를 순수 주주환원으로 보고 financing source를 valuation bridge에 충분히 넣지 않았다. 이벤트 완료와 residual business quality도 한 thesis로 묶었다.",
        "warning": "2005 filing에서 tender가 $100m revolver와 $300m notes로 거의 전액 debt-financed였다는 사실이 T0에 알 수 있었던 핵심 경고다.",
        "first_signal_date": "2005-07-11 filing에서 T0 확인 가능",
        "lessons": ["asset-sale event와 post-event stub return을 별도 underwrite한다.", "대규모 tender는 source-of-funds와 pro forma interest까지 봐야 accretion을 말할 수 있다.", "gross proceeds가 아니라 after-tax debt waterfall로 common value를 계산한다."],
        "checklist": ["asset별 gross/net proceeds", "tender source-of-funds", "pro forma cash interest", "stranded overhead", "radio FCF decline", "debt paydown schedule", "minority-holder distribution"],
        "scorecard": [("Business thesis", "residual 실패"), ("Valuation thesis", "혼합"), ("Catalyst thesis", "TV sale 성공"), ("Timing / path", "가격 미검증"), ("Security selection", "levered common 위험")],
        "claims": [
            C("TV 자산은 현금화된다", "비핵심 TV station을 팔아 balance sheet를 재편한다.", "전략적 buyer에게 매각해 hidden value를 cash로 바꾼다.", "이미 진행 중인 station sales와 FCC approvals.", "매각가·세금·closing이 기대범위다.", "할인매각·승인지연·세후 proceeds 미달이면 반증.", "2008 마지막 WVUE $41m 매각으로 TV exit 완료.", "event 실행 적중; aggregate net proceeds 별도 미복원.", "성공", "gross와 net 혼동 가능.", "매각 cohort별 net proceeds를 추적한다."),
            C("tender가 FCF/share를 높인다", "20.25m주 소각이 남은 주주의 ownership을 높인다.", "share denominator 감소가 per-share cash를 키운다.", "$19.50 tender 실행.", "financing cost가 denominator benefit보다 작다.", "pro forma interest로 FCF/share가 줄면 반증.", "$394.9m tender가 $100m revolver+$300m notes로 조달됐다.", "주식수 감소와 debt 증가가 동시 발생.", "부분/위험", "source-of-funds 누락.", "buyback accretion은 debt-adjusted FCF/share로 본다."),
            C("radio FCF/share는 연 5~10% 성장한다", "성장·debt paydown·repurchase로 per-share cash가 복리화한다.", "안정 station cash flow와 capital allocation이 서로 강화된다.", "원문 장기 기대.", "radio revenue duration이 길고 interest가 감소한다.", "FCF/주 감소·asset sale 의존 반복이면 반증.", "잔여 radio는 장기 compounder가 되지 못했다.", "정확한 연도별 series 미복원·terminal failure.", "실패", "구조적 감소와 governance discount 부족.", "mature media growth는 cohort FCF와 distribution으로 확인한다."),
            C("TV proceeds가 debt를 줄인다", "매각현금이 tender financing과 기존 debt를 상환한다.", "interest saving이 common FCF를 높인다.", "진행 중 매각계획.", "proceeds가 새 M&A보다 mandatory debt reduction에 쓰인다.", "순부채가 매각 뒤 감소하지 않으면 반증.", "매각은 완료됐으나 장기적으로 debt·capital structure 문제가 반복됐다.", "초기 bridge는 부분, 지속성 실패.", "부분 성공", "capital allocation policy를 고정값으로 봄.", "매각대금 사용처를 closing별 추적한다."),
            C("광고·계약 optionality가 upside다", "alcohol/gaming 광고, Nationals deal 무산 등이 revenue를 높인다.", "규제·계약 변화가 station inventory economics를 개선한다.", "원문 optional catalysts.", "one-off 이익이 base FCF에 중복되지 않는다.", "option이 cash contribution을 못 만들면 0으로 처리.", "독립적인 realized cash contribution을 복원하지 못했다.", "미검증.", "미검증", "soft catalyst를 base value에 더할 위험.", "옵션은 확률가중 별도항으로 둔다."),
            C("CEO LBO·추가 repurchase가 value를 드러낸다", "지배주주 action이 discount를 해소한다.", "control transaction이 public-market gap을 닫는다.", "원문 catalyst list.", "가격·공정성·minority treatment가 우호적이다.", "거래 지연·불공정 terms·delisting이면 반증.", "지속적 value realization 대신 2020 voluntary delisting.", "minority liquidity 악화.", "실패", "controller incentive와 minority payoff를 동일시.", "controller option에는 governance haircut을 둔다."),
        ],
        "metrics": [("Tender shares", "20.25m", "share count 감소", "실행", "성공"), ("Tender price/cash", "$19.50 / $394.9m", "accretive", "약 $400m debt financing", "혼합"), ("Tender financing", "미강조", "debt paydown", "$100m revolver+$300m notes", "위험"), ("Final TV station sale", "진행 중", "TV exit", "WVUE $41m·2008 완료", "성공"), ("FCF/share growth", "5~10%/년", "복리", "장기 실현 근거 없음", "실패")],
        "timeline": [("2005-06-20", "Dutch tender", "$394.9m·debt-financed"), ("2005-12-30", "VIC Long", "post-sale radio stub"), ("2008-07-18", "마지막 TV sale", "WVUE $41m·exit 완료"), ("2010", "take-private 실패", "governance/capital structure"), ("2019-11", "MediaCo transaction", "추가 asset monetization"), ("2020-05", "Nasdaq delisting", "minority liquidity 훼손")],
        "sources": [EMMS_SOURCES["tender"], EMMS_SOURCES["tv"], EMMS_SOURCES["deal"], EMMS_SOURCES["mediaco"], EMMS_SOURCES["delist"]],
    },
    {
        "id": "0105017c-3cc2-416f-a517-639654c5f8c6",
        "date": "2010-07-19", "author": "pfq783", "ticker": "EMMS", "company": "Emmis Communications",
        "filename": "analysis/ideas/2010/2010-07-19_EMMS_short.md",
        "source": "", "direction": "Short", "security": "EMMS Class A common equity / Short", "entry": "$2.15",
        "horizon": "2010-09-24 drop-dead까지 약 2개월", "raw_horizon": "DB parser 3년은 note maturity 문구 오인 가능성이 높아 판정 제외",
        "title": "preferred 2/3 consent의 closing math를 산 merger-break Short",
        "verdict": "강한 이벤트 성공·exact trade return 미검증", "score": 9.0, "process": 9.0,
        "conclusion": (
            "$2.40 take-private는 common tender와 preferred amendment/exchange가 연결돼 있었고 required preferred vote를 "
            "얻지 못하면 닫힐 수 없었다. 2010-09-09 회사는 proposed amendments가 requisite vote를 얻지 못했고 exchange와 "
            "tender가 종료됐다고 밝혔다. 9월 29일 merger도 공식 종료됐다. $2.15 Short의 핵심 catalyst는 정확히 실현됐지만 "
            "break-day 가격과 borrow를 복원하지 않아 exact profit은 만들지 않는다."
        ),
        "t0": (
            "Capital structure는 약 $345m secured credit와 $141m preferred liquidation preference(2.81m주×$50)로 "
            "복잡했다. JS Acquisition은 common을 $2.40에 tender하는 동시에 6.25% cumulative preferred를 12% PIK "
            "subordinated notes로 교환하고 preferred terms를 고치려 했다. 원문은 반대 bloc 때문에 약 2/3 consent가 "
            "어렵고, $2.15에서 close 손실은 약 11.6%인 반면 break gain은 25~50%라고 봤다."
        ),
        "reverse": (
            "시장 spread는 closing probability를 높게 봤다. 그러나 payoff는 운영가치보다 계약 dependency에 달렸다. "
            "조건변경 없이 2/3 vote를 얻을 확률, blocker가 이탈할 확률, buyer가 terms를 sweeten할 확률을 합쳐도 market "
            "implied close probability보다 낮다면 Short가 성립한다. 핵심은 opinion이 아니라 cap-table math였다."
        ),
        "valuation": (
            "Close loss는 ($2.40-$2.15)/$2.15 ≈ 11.6%다. Break gain 25~50%라면 break price는 약 $1.61~$1.08에 "
            "해당한다. Borrow와 시간가치를 빼기 전 기대값은 `P(break)×break gain - P(close)×11.6%`다. 25% gain 기준 "
            "손익분기 break probability는 약 31.7%, 50% 기준 약 18.8%다. 계약상 blocker가 이 확률보다 강하면 비대칭이다."
        ),
        "scenarios": [("Bear for Short", "2/3 consent·terms sweetening", "약 -11.6% before carry", "발생하지 않음"), ("Base", "vote fail·tender 종료", "+25% 가정", "event 실현·가격 미복원"), ("Bull for Short", "급한 deal break", "+50% 가정", "가격 미복원")],
        "actual": (
            "2010-09-09 proposed preferred amendments가 required vote를 얻지 못했고, 그 조건에 묶인 exchange offer와 "
            "common tender도 종료됐다. 9월 24일 drop-dead date가 지났고 9월 29일 JS Parent가 merger agreement를 "
            "종료했다. Holders는 기존 Emmis shareholders로 남았다. 운영사업의 장기 결과와 무관하게 원 이벤트 thesis는 "
            "이 시점에 판정 가능했다."
        ),
        "price": (
            "$2.15 entry와 $2.40 close cap은 복원됐지만 종료 직후 주가·borrow fee·실제 cover date는 없다. 따라서 원문이 "
            "말한 25~50% gain을 actual return으로 쓰지 않는다. 확정 가능한 것은 close condition 실패와 merger termination이다."
        ),
        "drivers": "수익기회는 radio 가치평가가 아니라 common tender가 preferred vote에 종속된 계약구조에서 나왔다. 제한된 close loss와 더 큰 break payoff, 두 달 남짓한 event calendar가 결합된 점이 좋았다.",
        "counterfactual": "Buyer가 preferred에 얼마를 더 제공하면 blocker가 2/3 threshold를 넘기고 Short 기대값이 음수가 되는가?",
        "error": "성과판정에서 25~50% 기대 gain을 actual gain으로 바꾸면 안 된다. 3년 raw horizon도 event calendar와 모순되므로 제외했다.",
        "warning": "반증은 preferred holders의 2/3 지지 또는 terms sweetening이다. 실제로는 2010-09-09 vote failure가 catalyst를 확정했다.",
        "first_signal_date": "2010-09-09",
        "lessons": ["Merger-break Short는 valuation opinion보다 closing threshold와 blocking stake를 먼저 본다.", "close loss·break gain·확률 손익분기점을 같은 표에 둔다.", "원문 horizon parser보다 계약상 drop-dead date를 우선한다."],
        "checklist": ["필요 vote threshold", "blocker ownership", "조건간 dependency", "sweetener capacity", "close loss", "break price", "borrow·drop-dead date"],
        "scorecard": [("Business thesis", "해당 없음"), ("Valuation thesis", "비대칭 성공"), ("Catalyst thesis", "강한 성공"), ("Timing / path", "event 적중"), ("Security selection", "common Short 적절")],
        "claims": [
            C("preferred 2/3 consent가 필수다", "common tender는 preferred amendment 통과에 종속된다.", "연결조건 하나의 실패가 전체 transaction을 막는다.", "offer·merger 조건과 preferred cap table.", "waiver 없이 requisite vote가 유지된다.", "buyer가 condition을 포기하거나 threshold를 확보하면 반증.", "requisite vote 미달로 amendment·exchange·tender 종료.", "직접 적중.", "성공", "중대한 오류 없음.", "모든 closing condition의 dependency graph를 만든다."),
            C("반대 bloc이 거래를 막는다", "경제적으로 불리한 exchange에 preferred holders가 반대한다.", "$50 liquidation·arrears를 낮은 조건의 PIK notes로 바꾸는 손실이 vote를 막는다.", "preferred economics와 ownership.", "blocker가 충분히 결집한다.", "lock-up 이탈·sweetener로 2/3 확보 시 반증.", "vote가 실제 통과하지 못했다.", "blocking thesis 확인.", "성공", "exact holder votes는 별도 미복원.", "blocker는 법적 권리와 경제적 유인을 함께 본다."),
            C("close downside는 약 11.6%다", "$2.15 Short가 $2.40 close 시 제한손실이다.", "fixed deal price가 adverse payoff를 cap한다.", "명시 offer price.", "price increase·borrow squeeze가 없다.", "deal sweetening 또는 borrow cost 급등이면 cap 무효.", "deal이 종료돼 close loss는 발생하지 않았다.", "구조적 downside 미발생.", "성공", "borrow와 sweetener tail은 남음.", "deal cap은 financing·borrow tail을 포함한다."),
            C("break upside는 25~50%다", "거래 무산 시 pre-deal value로 하락한다.", "deal premium 제거와 weak capital structure가 가격을 낮춘다.", "원문 downside appraisal.", "standalone value와 market liquidity가 유지된다.", "break 후 가격이 $1.61 위에 머물면 low case 미달.", "break-day price를 복원하지 못했다.", "event 방향만 확인.", "미검증", "expected와 actual return 혼동 금지.", "break price는 별도 시장데이터로 검증한다."),
            C("9월 drop-dead가 빠른 촉매다", "vote failure 뒤 거래가 9월 말 종료된다.", "짧은 calendar가 carry를 제한한다.", "8월 meeting·9월 24일 date.", "연장·소송이 없다.", "deal 연장 시 IRR 하락.", "9월 29일 merger termination.", "약 10주 내 실현.", "성공", "며칠의 procedural lag만 존재.", "event IRR은 legal milestones로 계산한다."),
            C("운영사업 전망은 secondary다", "Short 성공은 radio EBITDA가 아니라 closing failure에 달렸다.", "contractual binary가 market beta를 압도한다.", "구조화된 tender/exchange.", "event window 안에 business shock가 payoff를 바꾸지 않는다.", "재무개선으로 standalone price가 급등하면 반증.", "거래조건 실패가 결과를 결정했다.", "driver attribution 적중.", "성공", "중대한 오류 없음.", "event trade는 핵심 risk factor만 남긴다."),
        ],
        "metrics": [("Short entry", "$2.15", "break downside", "exact cover 미복원", "event 성공"), ("Deal price", "$2.40", "close loss", "약 11.6%", "정의됨"), ("Preferred threshold", "약 66.7%", "미달", "requisite vote 미달", "성공"), ("Break-even probability", "31.7% / 18.8%", "25% / 50% gain case", "deal break", "비대칭"), ("Drop-dead", "2010-09-24", "빠른 종료", "9월 29일 종료", "성공")],
        "timeline": [("2010-05-25", "Going-private agreement", "$2.40 tender"), ("2010-07-19", "VIC Short", "$2.15"), ("2010-08", "preferred vote process", "핵심 condition"), ("2010-09-09", "vote 미달", "offer 종료"), ("2010-09-24", "drop-dead", "termination right"), ("2010-09-29", "merger 종료", "thesis 실현")],
        "sources": [EMMS_SOURCES["deal"], EMMS_SOURCES["termination"], EMMS_SOURCES["k2016"]],
    },
])


IDEAS.extend([
    {
        "id": "3027530a-b943-4fe7-8fb5-ea719a6f9c0b",
        "date": "2018-07-23", "author": "JSTC", "ticker": "ETM", "company": "Entercom Communications",
        "filename": "analysis/ideas/2018/2018-07-23_ETM_short.md",
        "source": "", "direction": "Short", "security": "ETM common equity / Short", "entry": "$8.15",
        "horizon": "명시 없음; 2Q miss·estimate cuts 촉매", "raw_horizon": "원 DB horizon 없음",
        "title": "CBS Radio의 headline scale보다 debt-bearing capacity를 본 Short",
        "verdict": "구조적으로 강한 성공·정확한 실행 IRR 미검증", "score": 9.0, "process": 8.5,
        "conclusion": (
            "6.3x leverage, 10.5x 2018E EBITDA에서 legacy와 acquired station의 광고 headwind가 겹친다는 핵심은 "
            "정확했다. 원문은 TV broadcasters의 7~8배보다 낮은 7배 미만이 맞다며 $8.15에서 50%+ downside를 봤다. "
            "2024 Audacy가 $1.6bn debt를 equitize해 총 debt를 약 $1.9bn에서 $350m으로 줄인 결과는 equity downside의 "
            "구조적 방향을 강하게 확인한다. 다만 borrow·cover date·배당을 반영한 exact Short IRR은 미검증이다."
        ),
        "t0": (
            "CBS Radio 결합으로 reported revenue와 EBITDA는 급증했지만, acquired stations의 turnaround가 아직 확인되지 "
            "않은 상태에서 equity는 6.3x leverage에 노출됐다. 원문은 TV station peer가 7~8배인데 성장성이 더 약하고 "
            "leverage가 높은 ETM이 10.5배를 받을 이유가 없다고 봤다. 2Q earnings miss와 Street estimate cuts가 "
            "valuation gap을 드러낼 촉매였다."
        ),
        "reverse": (
            "$8.15가 유지되려면 CBS Radio organic revenue가 빠르게 안정되고 cost/revenue synergy가 debt service를 "
            "넘어 net leverage를 낮춰야 했다. 7배 미만 재평가가 맞으려면 반대로 stressed EBITDA가 base estimate보다 "
            "낮고 interest burden이 equity FCF를 잠식하면 충분했다. 이 숏은 ‘radio가 망한다’보다 denominator인 "
            "stressed-normalized EBITDA가 낮다는 주장이다."
        ),
        "valuation": (
            "원문의 10.5배 2018E EBITDA에 7배를 적용하면 EV가 약 3분의 1 줄어든다. 6.3x debt/EBITDA에서는 이 EV "
            "감소가 equity에 비선형으로 전달돼 50%+ downside가 가능하다. 다만 TV peer는 retrans·political cash flow가 "
            "달라 완전한 비교군이 아니다. 더 강한 검증은 ETM 자체의 `debt / stressed EBITDA`, cash interest coverage, "
            "organic revenue decline을 이용하는 것이다."
        ),
        "scenarios": [("Bear for Short", "CBS 안정·synergy·4x 이하 leverage", "short squeeze", "발생하지 않음"), ("Base", "organic 약세·완만한 synergy", "7배 이하·50% downside", "방향 실현"), ("Bull for Short", "광고악화·refinancing 차단", "equity restructuring", "2024 실현")],
        "actual": (
            "2018 net revenue는 $1.462567bn으로 합병규모를 보여줬지만 scale은 solvency를 보장하지 못했다. 2024-01 "
            "Audacy는 prepackaged Chapter 11을 시작하며 약 $1.9bn total debt를 약 $350m으로 줄이고 $1.6bn funded "
            "debt를 equitize하겠다고 발표했다. 2024-09 emergence 때 debt reduction 80%, net leverage 약 2.7x가 확인됐다. "
            "즉 기존 자본구조가 감당할 수 없었다는 원 숏의 핵심이 맞았다."
        ),
        "price": (
            "진입가 $8.15와 50%+ downside는 공개 원문 excerpt로 복원했다. 그러나 원 DB의 1개월~5년 performance가 "
            "비어 있고 exact cover rule도 없다. Chapter 11까지 약 5년 6개월이 걸렸으므로 nominal thesis success와 "
            "annualized short return은 다르다. borrow fee, recall, interim squeeze를 반영하지 않은 IRR은 제시하지 않는다."
        ),
        "drivers": "손실을 만든 것은 합병 회계매출이 아니라 organic ad weakness가 높은 fixed cost와 interest를 통과하며 debt capacity를 훼손한 과정이다. 상대가치 7배보다 6.3x leverage와 EBITDA downside convexity가 더 강한 근거였다.",
        "counterfactual": "ETM이 TV peers처럼 7배로 하락해도 CBS organic revenue가 안정되고 24개월 내 leverage 4x가 됐다면 숏은 계속 유효했을까?",
        "error": "결과는 맞았지만 TV broadcaster peer multiple은 retrans와 정치광고가 없는 radio에 불완전한 비교다. catalyst timing과 short carry도 원문 정보만으로는 약하다.",
        "warning": "합병 후 leverage 6.3x 자체가 T0의 선행위험이었다. 명시된 첫 촉매인 2Q miss의 실제 발표값은 현재 자료에서 별도 복원하지 못했다.",
        "first_signal_date": "2018-07-23",
        "lessons": ["쇠퇴산업 M&A는 EV/EBITDA보다 debt/stressed-normalized EBITDA를 먼저 본다.", "Short target과 별도로 borrow·squeeze·cover calendar를 저장한다.", "상대가치는 business-model 차이를 조정한 뒤 보조근거로만 쓴다."],
        "checklist": ["organic revenue by legacy/acquired cohort", "stressed EBITDA", "cash interest coverage", "net leverage", "maturity/refinancing", "borrow fee·utilization", "cover trigger"],
        "scorecard": [("Business thesis", "강한 성공"), ("Valuation thesis", "성공"), ("Catalyst thesis", "단기 미검증·장기 성공"), ("Timing / path", "미검증"), ("Security selection", "Short 적절")],
        "claims": [
            C("6.3x leverage는 과도하다", "CBS 결합 후 부채가 작은 EBITDA miss에도 equity를 훼손한다.", "고정비와 interest가 revenue decline을 equity 손실로 증폭한다.", "원문 pro forma leverage.", "stressed EBITDA가 base와 비슷하고 refinance access가 있다면 위험 완화.", "24개월 내 net leverage 4x 이하이면 숏 반증.", "2024 $1.6bn equitization이 필요했다.", "debt capacity 명확한 실패.", "성공", "큰 오류 없음.", "leverage는 stressed EBITDA로 계산한다."),
            C("10.5x EBITDA valuation은 높다", "성장성이 낮은 radio가 더 좋은 peer보다 premium을 받는다.", "multiple compression이 높은 debt 뒤 equity를 크게 줄인다.", "원문 2018E multiple.", "EBITDA estimate와 enterprise value 계산이 일관된다.", "organic 회복으로 multiple이 7배 아래여도 equity가 상승하면 반증.", "terminal restructuring이 premium의 지속불가능성을 확인했다.", "exact rerating timing 미검증.", "성공", "TV peer comparability 제한.", "자체 historical/stressed multiple을 병행한다."),
            C("legacy와 CBS stations 모두 광고 headwind다", "두 portfolio가 동시에 약하면 diversification이 없다.", "same-industry scale은 공통 demand shock를 상쇄하지 못한다.", "원문 station trend 분석.", "revenue synergy가 common decline을 역전하지 못한다.", "acquired cohort가 4분기 내 유기적 성장하면 반증.", "Scale 후에도 long-run cash generation이 debt를 지키지 못했다.", "cohort exact series 미복원·방향 적중.", "성공", "공시 segment 부족.", "합병은 acquired/legacy cohort를 분리 추적한다."),
            C("ETM은 TV peers보다 7배 미만이 맞다", "낮은 growth와 높은 leverage에 discount를 적용한다.", "retrans·political cash flow가 없는 만큼 duration이 짧다.", "TV peers 7~8x vs ETM 10.5x.", "peer accounting과 leverage 정의가 비교 가능하다.", "radio의 digital optionality가 더 높은 growth를 만들면 반증.", "ETM capital structure가 먼저 깨졌다.", "relative direction 적중.", "성공", "cross-sector comp는 보조근거.", "peer gap은 cash-flow mix 차이로 조정한다."),
            C("2Q miss와 estimate cuts가 촉매다", "근기 실적 miss가 시장의 PF EBITDA를 낮춘다.", "denominator 하향이 6.3x leverage와 valuation을 동시에 악화한다.", "원문 catalyst.", "Street가 organic weakness를 아직 반영하지 않았다.", "2Q beat·guidance 유지면 단기 catalyst 반증.", "해당 분기 exact consensus gap은 미복원.", "단기 판정 불가.", "미검증", "event evidence 부족.", "earnings catalyst는 consensus table을 보존한다."),
            C("$8.15에서 50%+ downside다", "7배 미만 적용 시 common이 절반 이하가 된다.", "EV change가 debt 뒤 residual equity에 증폭된다.", "원문 target math.", "short를 구조조정까지 유지할 실행 가능성이 있다.", "cover price·borrow cost 포함 수익이 하방을 지우면 실패.", "2024 debt equitization은 손실 severity를 확인했다.", "nominal 방향 성공·exact IRR 미검증.", "강한 성공", "duration·borrow 비용 미반영.", "Short payoff는 price target과 carry-adjusted IRR을 분리한다."),
        ],
        "metrics": [("Short entry", "$8.15", "50%+ downside", "exact cover price 미복원", "구조 성공"), ("Leverage", "6.3x", "악화/재평가", "2024 restructuring", "성공"), ("2018E EBITDA multiple", "10.5x", "<7x", "capital structure failure", "성공"), ("2018 net revenue", "PF growth", "scale", "$1.462567bn", "매출만 성공"), ("Debt restructuring", "없음", "위험", "$1.9bn→$350m", "강한 성공")],
        "timeline": [("2018-07-23", "VIC Short", "$8.15·6.3x"), ("2018-Q2", "miss/cuts catalyst", "actual gap 미복원"), ("2018-12-31", "매출 $1.463bn", "headline scale"), ("2021-03", "Audacy rebrand", "digital 확장 시도"), ("2024-01-07", "Chapter 11", "$1.6bn equitization"), ("2024-09-30", "emergence", "debt 80% 감소")],
        "sources": ETM_SOURCES,
    },
    {
        "id": "eaf5eea7-6a56-4f6e-8bc4-44ec3439b962",
        "date": "2020-03-15", "author": "TRUTH_SEEKER", "ticker": "ETM", "company": "Entercom Communications",
        "filename": "analysis/ideas/2020/2020-03-15_ETM_long.md",
        "source": "https://www.valueinvestorsclub.com/idea/ENTERCOM_COMMUNICATIONS_CORP/8113869966",
        "direction": "Long", "security": "ETM common equity Long; unsecured-bond Short는 선택적 hedge", "entry": "정확한 가격 미복원; 직전 1개월 약 50% 급락",
        "horizon": "5년", "raw_horizon": "5 years",
        "title": "COVID liquidity shock를 구조적 solvency 문제와 혼동한 common Long",
        "verdict": "즉시 생존 성공·5년 common thesis 실패", "score": 3.0, "process": 4.0,
        "conclusion": (
            "회사는 2020년에 즉시 파산하지 않았으므로 liquidity call은 맞았지만, 5년 common-equity survival call은 "
            "실패했다. 광고는 재개될 수 있어도 shock 이전의 ‘normal’ 자체가 radio secular decline과 CBS debt 때문에 "
            "불안정했다. Audacy는 게시 후 3년 10개월 만에 Chapter 11에 들어가 $1.6bn debt를 equitize했다. 원문에서 "
            "무담보채 숏은 hedge였고 primary recommendation은 common Long이므로 raw SQL Short를 그대로 쓰면 안 된다."
        ),
        "t0": (
            "COVID 초기에 local advertising이 급정지하며 ETM 주가는 한 달 약 50% 하락했다. 원문은 당장 만기벽이 "
            "가깝지 않고 cash flow와 liquidity가 lockdown을 견딜 수 있어 bankruptcy 우려가 과도하다고 봤다. 주가가 "
            "Russell 2000 beta의 약 두 배로 움직이다 신규 확진 감소 시 반등한다는 tactical Long이었고, tail risk를 "
            "줄이기 위해 unsecured bond short를 선택적 hedge로 제시했다."
        ),
        "reverse": (
            "가격은 COVID 매출절벽뿐 아니라 이미 존재하던 secular radio decline과 merger debt를 함께 반영했을 수 있다. "
            "Long이 지속되려면 단기 liquidity로 2020을 넘긴 뒤 normalized EBITDA가 shock 이전 수준으로 회복되고, 그 "
            "FCF가 debt를 계속 줄여 5년 내 refinance risk를 제거해야 했다. 단순 재개방은 필요조건일 뿐 충분조건이 아니었다."
        ),
        "valuation": (
            "위기 Long의 가치는 `survival probability × post-normal equity value - dilution/restructuring loss`다. Base "
            "case는 월별 cash burn과 liquidity runway, post-COVID EBITDA, 현금이자, maturity를 연결해야 한다. 원문은 "
            "단기 만기 부재를 강조했지만 five-year horizon에서는 secular EBITDA decline이 option expiry를 앞당긴다. "
            "Bond short hedge도 recovery와 notional을 정하지 않으면 common downside를 완전히 막지 못한다."
        ),
        "scenarios": [("Bear", "COVID 장기화 또는 post-normal 약화", "restructuring·common impairment", "2024 실현"), ("Base", "광고 회복·liquidity 유지·완만한 debt paydown", "common 반등", "즉시 생존만 실현"), ("Bull", "빠른 reopening·digital growth·deleveraging", "큰 equity convexity", "지속되지 않음")],
        "actual": (
            "ETM은 2020 당장 청산되지 않았고 Audacy로 전환하며 digital audio 확장을 시도했다. 그러나 normalized cash "
            "generation은 기존 debt를 충분히 줄이지 못했다. 2024-01 prepackaged Chapter 11에서 약 $1.9bn total debt를 "
            "$350m으로 낮추고 $1.6bn을 equitize하는 계획을 발표했고, 2024-09 80% debt reduction과 약 2.7x net "
            "leverage로 emergence했다. 이는 old common의 five-year payoff가 실패했음을 의미한다."
        ),
        "price": (
            "원문 정확한 진입가와 short-term performance series는 복원되지 않았다. 따라서 COVID 저점 반등이 얼마였는지 "
            "또는 hedge 포함 IRR을 만들지 않는다. 확정 가능한 것은 5년 horizon 안인 2024-01에 balance-sheet "
            "restructuring이 발생했고 기존 common thesis가 유지될 수 없었다는 점이다."
        ),
        "drivers": "단기 반등은 신규확진·광고 재개 기대가 만들 수 있었지만 장기 손실은 shock 이전부터 존재한 industry decline과 debt service가 만들었다. liquidity runway를 solvency margin으로 해석한 것이 핵심 transmission error다.",
        "counterfactual": "2021 광고가 2019 수준으로 한 번 회복했어도 이후 매년 organic EBITDA가 줄고 debt가 유지됐다면 2020 저점 common은 투자였나, 만기 있는 call option이었나?",
        "error": "COVID-only framing으로 pre-existing secular decline을 정상상태로 놓았다. primary Long과 optional bond hedge의 notional·recovery를 분리하지 않았다.",
        "warning": "경제재개 뒤에도 반복 FCF로 net leverage가 지속 하락하지 않는 첫 4개 분기가 경고였어야 한다. 정확한 최초 분기 bridge는 현재 자료에서 미복원이다.",
        "first_signal_date": "2021-12-31 이전 재검증 필요",
        "lessons": ["위기 Long은 liquidity runway와 solvency runway를 별도 모델링한다.", "shock 이전 normal이 구조적으로 지속 가능한지 먼저 재검증한다.", "주식 Long·채권 Short hedge는 각 leg의 notional, carry, recovery를 명시한다."],
        "checklist": ["월별 cash burn·liquidity", "maturity wall", "post-shock organic revenue", "stressed EBITDA", "cash interest coverage", "net leverage trend", "hedge notional·bond recovery"],
        "scorecard": [("Business thesis", "장기 실패"), ("Valuation thesis", "실패"), ("Catalyst thesis", "단기 부분 성공 가능·미검증"), ("Timing / path", "5년 내 실패"), ("Security selection", "common Long 부적절")],
        "claims": [
            C("한 달 50% 급락은 COVID 과잉반응이다", "market beta 약 2배의 panic selloff를 산다.", "확진 감소·reopening이 광고와 risk appetite를 되돌린다.", "원문 price observation.", "회사가 lockdown 기간 liquidity를 유지한다.", "현금부족·covenant breach가 reopening 전에 오면 반증.", "즉시 파산은 피했지만 exact 반등수익은 미복원.", "liquidity 방향 일부 적중.", "부분 성공", "가격 beta와 내재가치 gap을 동일시.", "panic trade는 event exit를 사전에 정한다."),
            C("가까운 만기 부재로 2020을 버틴다", "maturity runway와 cash flow가 acute shock를 통과시킨다.", "시간을 벌면 광고가 회복돼 refinancing option이 살아난다.", "T0 debt maturity와 liquidity.", "cash burn이 available liquidity보다 작다.", "12개월 내 restructuring이면 즉시 실패.", "2020 immediate bankruptcy는 피했다.", "acute horizon 성공.", "성공", "단기 생존을 장기 가치로 확장.", "liquidity claim에는 만료일을 붙인다."),
            C("post-COVID EBITDA가 정상화된다", "광고가 reopening과 함께 shock 전 수준으로 회복한다.", "높은 fixed cost가 revenue rebound를 EBITDA로 증폭한다.", "광고의 경기민감성.", "2019가 지속 가능한 정상상태다.", "reopening 후 organic EBITDA가 debt service를 못 덮으면 반증.", "2024 debt equitization이 필요했다.", "durable normalization 실패.", "실패", "pre-shock secular trend 누락.", "normal은 shock 전 1년이 아니라 3~5년 추세로 정한다."),
            C("FCF가 debt를 줄인다", "광고회복 뒤 반복현금으로 leverage를 낮춘다.", "deleveraging이 refinancing probability와 equity value를 높인다.", "원문 bankruptcy-avoidance logic.", "회복 FCF가 interest와 capex 후 양수다.", "2년 뒤 net leverage가 줄지 않으면 반증.", "2024 $1.6bn을 equity로 전환해야 했다.", "자발적 debt paydown 실패.", "실패", "cash flow amount와 debt scale 불일치.", "debt paydown years를 명시 계산한다."),
            C("bond Short가 tail을 hedge한다", "무담보채 숏을 더해 bankruptcy tail을 줄일 수 있다.", "common rebound와 unsecured recovery 하락의 상대가치 포지션이다.", "원문 optional hedge.", "borrow·carry와 recovery sensitivity가 관리된다.", "bond rally·short carry가 common gain을 지우면 hedge 실패.", "restructuring은 bond risk를 확인했지만 exact hedge payoff 미복원.", "방향 적중·수익 미검증.", "미검증", "notional과 instrument price 누락.", "hedge는 security-level payoff table을 만든다."),
            C("5년 common equity는 살아남는다", "cycle 회복 뒤 bankruptcy를 피하고 equity가 재평가된다.", "시간과 FCF가 debt option 만기를 연장한다.", "DB horizon 5년.", "secular decline이 debt paydown보다 느리다.", "horizon 내 Chapter 11이면 직접 반증.", "게시 후 약 46개월에 Chapter 11.", "5년보다 약 14개월 빠른 실패.", "실패", "liquidity와 solvency 시간축 혼동.", "위기 equity는 milestone별 생존확률을 곱한다."),
        ],
        "metrics": [("One-month selloff", "약 50%", "mean reversion", "exact return 미복원", "미검증"), ("Horizon", "5년", "equity survival", "약 46개월 후 Chapter 11", "실패"), ("Pre-restructuring debt", "maturity runway", "deleveraging", "약 $1.9bn", "실패"), ("Debt equitized", "없음 기대", "bankruptcy 회피", "약 $1.6bn", "실패"), ("Post debt", "자발적 감소", "낮은 leverage", "$350m·약 2.7x", "법원절차로 실현")],
        "timeline": [("2020-03-15", "VIC common Long", "COVID oversold"), ("2020", "acute liquidity 구간", "즉시 파산 회피"), ("2021-03", "Audacy 전환", "multi-platform 시도"), ("2023", "solvency pressure", "deleveraging 실패 가시화"), ("2024-01-07", "Chapter 11", "5년 thesis 반증"), ("2024-09-30", "emergence", "old capital structure 교체")],
        "sources": ETM_SOURCES,
    },
])


if __name__ == "__main__":
    main()
