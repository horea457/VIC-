#!/usr/bin/env python3
"""Build Batch 042 radio / satellite-audio canonical V9 research artifacts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-09"
WEIGHTS = [20, 18, 18, 16, 16, 12]


def C(title, original, mechanism, evidence, assumption, falsifier, actual, gap, verdict, error, lesson):
    return dict(
        title=title,
        original=original,
        mechanism=mechanism,
        evidence=evidence,
        assumption=assumption,
        falsifier=falsifier,
        actual=actual,
        gap=gap,
        verdict=verdict,
        error=error,
        lesson=lesson,
    )


def S(title, url, publisher, date, evidence, source_type="1차자료"):
    return dict(title=title, url=url, publisher=publisher, date=date, evidence=evidence, type=source_type)


BUSINESS = {
    "CMLS": (
        "Cumulus Media는 미국 지역 라디오 방송국과 Westwood One 전국 네트워크를 통해 spot 광고, network 광고, "
        "syndicated content, digital audio·podcast를 판매한다. 지역 방송국은 청취자와 지역 광고주 관계를 만들고, "
        "네트워크는 콘텐츠와 전국 광고 inventory를 여러 affiliate에 배포한다. 주파수 면허와 지역 브랜드는 희소하지만 "
        "광고예산과 청취시간은 search·social·streaming으로 이동할 수 있다."
    ),
    "SGA": (
        "Saga Communications는 중소도시 중심의 지역 라디오 방송사다. 지역 뉴스·스포츠·진행자와 영업조직으로 청취자와 "
        "지역 광고주를 연결하고, 최근에는 digital advertising과 non-traditional revenue를 붙인다. 전국 광고보다 local "
        "매출 비중이 높아 대형 네트워크와 다른 경기·경쟁 노출을 갖는다. 무차입·순현금 구조와 실제 배당정책이 common "
        "equity 가치의 핵심 완충재다."
    ),
    "SALM": (
        "Salem Media는 기독교·보수 성향의 라디오, block programming, digital media, 출판 사업을 운영했다. 일반 spot 광고뿐 "
        "아니라 프로그램 제작자가 airtime을 사는 block programming이 큰 비중을 차지해 광고경기 민감도를 낮출 수 있다. "
        "반면 청취층 집중, AM/FM 자산의 구조적 감소, 높은 고정비와 부채 때문에 EBITDA보다 현금이자·자산매각·만기구조가 "
        "common equity의 존속을 좌우한다."
    ),
    "XMSR": (
        "XM Satellite Radio는 위성·지상 중계망으로 전국 유료 오디오를 제공하고 자동차 OEM·딜러를 통해 가입자를 획득한 "
        "초기 위성라디오 사업자였다. 이 아이디어의 대상은 common이 아니라 14% senior secured notes다. 가입자 증가가 "
        "기업가치를 만들더라도 채권 수익은 escrow coupon, 담보, exchange ratio, 신주·warrant, refinancing 순서로 결정된다."
    ),
    "SIRI": (
        "Sirius XM은 북미 위성라디오 구독, 차량 내 trial·conversion, 광고, streaming·Pandora를 운영한다. OEM이 신차에 "
        "수신기를 탑재하고 Sirius XM이 trial 사용자를 self-pay 구독자로 전환한다. 위성·콘텐츠 비용의 상당 부분이 고정이라 "
        "가입자와 ARPU 성장은 높은 incremental margin을 만들지만, churn·royalty·OEM subsidy·위성 capex·부채와 자사주매입이 "
        "주당 FCF를 크게 바꾼다."
    ),
}

ENGINE = {
    "CMLS": "현금엔진은 `local spot + national/network + digital - station/content/sales cost - corporate cost - cash interest - capex - tax`다. 7배 안팎 레버리지에서는 소폭의 organic EBITDA 감소도 common value를 크게 훼손한다.",
    "SGA": "현금엔진은 `local advertising + national advertising + digital/NTR - station programming·sales cost - corporate cost - capex - tax`다. 순현금은 이자비용을 없애고 downturn 생존과 배당·인수 선택권을 만든다.",
    "SALM": "현금엔진은 `block programming + spot advertising + digital/publishing - content·station·sales cost - corporate cost - cash interest - capex - tax`다. 높은 표면 FCF yield가 보여도 이자와 만기, 자산매각 후 earning-base 축소를 함께 봐야 한다.",
    "XMSR": "채권 현금엔진은 `escrow coupon + cash coupon/accretion + exchange consideration + warrant value + recovery - 매입가격 - carry/transaction cost`다. enterprise 성공과 특정 채권의 realized IRR은 별개다.",
    "SIRI": "현금엔진은 `self-pay subscribers × ARPU + advertising - revenue share·royalty - content/customer service - satellite capex - cash tax - interest`다. 고정비 leverage와 churn이 반대 방향으로 작동한다.",
}

KPI = {
    "CMLS": "same-station revenue, local/national mix, Westwood One EBITDA·synergy, cash interest, capex, 순부채/2년 평균 EBITDA, maturity wall, 실제 debt paydown",
    "SGA": "same-station revenue ex-political, local 매출비중, digital gross·segment contribution, station margin, FCF, 순현금, 배당·특별배당, share count",
    "SALM": "block-programming renewal·가격, same-station revenue, digital contribution, cash interest coverage, maintenance capex, 순부채/EBITDA, asset-sale proceeds와 잔존 EBITDA",
    "XMSR": "가입자·SAC·churn·OEM conversion, 월 cash burn, funding need, 담보·seniority, exchange participation, new-money terms, warrant strike, 실제 redemption price",
    "SIRI": "self-pay net adds, trial conversion, churn, ARPU, SAC·OEM subsidy, royalty rate, adjusted EBITDA margin, satellite capex, FCF, leverage·buyback price",
}


CMLS_SOURCES = [
    S("Cumulus to acquire Dial Global", "https://www.crestview.com/news/cumulus-to-acquire-dial-global/", "Crestview / Cumulus", "2013-08-30", "거래가격·station swap·시너지 기대 검증."),
    S("2017 restructuring announcement", "https://www.cumulusmedia.com/wp-content/uploads/2017/11/Press_Release_11.29.17_F.pdf", "Cumulus Media", "2017-11-29", "첫 Chapter 11과 debt-reduction 계획 검증."),
    S("Q2 2018 results and emergence", "https://www.cumulusmedia.com/2018/08/20/cumulus-reports-operating-results-for-second-quarter-2018/", "Cumulus Media", "2018-08-20", "2018 emergence와 약 $1bn debt reduction 검증."),
    S("FY2019 results", "https://www.cumulusmedia.com/2020/02/21/cumulus-media-reports-operating-results-for-2019-2/", "Cumulus Media", "2020-02-21", "2019 debt paydown과 leverage 검증."),
    S("FY2022 results", "https://www.cumulusmedia.com/2023/02/23/cumulus-media-reports-operating-results-for-2022/", "Cumulus Media", "2023-02-23", "2022 leverage 검증."),
    S("FY2024 results", "https://www.cumulusmedia.com/wp-content/uploads/2025/02/CMLS-12.31.2024-Earnings-Release-FINAL-we98JNz75.pdf", "Cumulus Media", "2025-02", "2024 EBITDA와 debt 검증."),
    S("2026 balance-sheet restructuring", "https://www.cumulusmedia.com/2026/03/05/cumulus-media-announces-agreement-to-eliminate-substantially-all-remaining-debt-and-significantly-strengthen-financial-position/", "Cumulus Media", "2026-03-05", "두 번째 Chapter 11과 약 $600m debt elimination 검증."),
    S("2026 plan confirmation", "https://www.cumulusmedia.com/2026/04/15/cumulus-media-secures-court-approval-of-reorganization-plan/", "Cumulus Media", "2026-04-15", "plan confirmation 검증."),
    S("Q2 2026 restructuring status", "https://www.cumulusmedia.com/2026/08/14/cumulus-media-reports-operating-results-for-the-second-quarter-2026/", "Cumulus Media", "2026-08-14", "FCC 승인 대기 상태 검증."),
]

SGA_SOURCES = [
    S("Saga Q1 2019 filing", "https://ir.sagacom.com/node/6621/html", "Saga Communications", "2019", "station 수·현금·영업구조 교차검증."),
    S("Saga FY2020 results", "https://ir.sagacom.com/static-files/09ea0d3f-3d7a-4429-8647-e4f18bcf285a", "Saga Communications", "2021", "pandemic 매출·FCF와 생존력 검증."),
    S("Saga 2021 Form 10-K", "https://ir.sagacom.com/static-files/32c200aa-2655-40ec-8cef-57b0d720c86e", "Saga Communications", "2022", "2021 digital growth와 2022 T0 자본구조 검증."),
    S("Saga 2022 annual report", "https://ir.sagacom.com/static-files/dce247dd-4ee6-4f41-8c9c-614d310490dd", "Saga Communications", "2023", "2022 revenue·FCF·dividend 검증."),
    S("Saga 2023 annual report", "https://ir.sagacom.com/static-files/05b35d9d-5c6c-464f-b333-87c82e4cc6b4", "Saga Communications", "2024", "특별배당과 누적 자본환원 검증."),
    S("Saga 2025 annual report", "https://ir.sagacom.com/static-files/f44e6fad-250e-4ab5-b1a3-12429e0b8341", "Saga Communications", "2026", "2025 revenue·CFO·digital mix 검증."),
]

SALM_SOURCES = [
    S("Salem 2021 Form 10-K", "https://investor.salemmedia.com/sec-filings/content/0001193125-22-066029/d301480d10k.htm", "SEC / Salem", "2022-03", "사업구조·station portfolio·부채 검증."),
    S("Quarterly dividend suspension", "https://investor.salemmedia.com/news-events/press-releases/detail/663/salem-media-group-inc-announces-temporary-suspension-of-quarterly-dividend", "Salem Media", "2020-05-11", "배당 중단이라는 초기 반증사건 검증."),
    S("Voluntary Nasdaq delisting", "https://investor.salemmedia.com/news-events/press-releases/detail/833/inserting-and-replacing-salem-media-group-announces-voluntary-delisting-from-the-nasdaq-global-market", "Salem Media", "2024", "OTC 전환·유동성 훼손 검증."),
    S("Station-sale plan", "https://investor.salemmedia.com/news-events/press-releases/detail/838/salem-media-group-announces-plan-to-sell-its-contemporary-christian-music-stations-in-nashville-and-honolulu", "Salem Media", "2024-03", "asset sale을 통한 유동성 조달 검증."),
    S("2024 debt restructuring", "https://investor.salemmedia.com/news-events/press-releases/detail/866/salem-media-group-substantially-strengthens-its-balance-sheet-by-repaying-all-159-4-million-of-its-long-term-debt-and-brings-in-new-strategic-investor", "Salem Media", "2024-12-23", "2028 notes repurchase와 신규 preferred·asset-sale 자금 검증."),
    S("WaterStone acquisition announcement", "https://investor.salemmedia.com/news-events/press-releases/detail/924/salem-media-to-be-acquired-by-waterstone-in-major-growth-deal", "Salem Media", "2026", "$1 per share take-private 조건 검증."),
    S("WaterStone acquisition completion", "https://investor.salemmedia.com/news-events/press-releases/detail/939/salem-media-completes-acquisition-by-waterstone-begins-new-chapter-as-private-company", "Salem Media", "2026", "상장 common의 종결 검증."),
]

XM_SOURCES = [
    S("XM exchange offer", "https://www.sec.gov/Archives/edgar/data/1091530/000095010902006334/dex991.htm", "SEC / XM", "2002", "교환조건과 신규자금 구조 검증."),
    S("XM 2004 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1091530/000119312505042835/d10k.htm", "SEC / XM", "2005", "2003 exchange 참여액·GM restructuring·new money 검증."),
    S("XM 2006 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1091530/000119312507044379/d10k.htm", "SEC / XM", "2007", "14% notes repurchase·redemption 금액 검증."),
    S("XM/Sirius merger announcement", "https://investor.siriusxm.com/sec-filings/sirius-xm-holdings-inc/content/0000950123-07-003042/0000950123-07-003042.pdf", "SEC / Sirius XM", "2007-02-19", "합병 발표 검증."),
    S("FCC XM/Sirius merger docket", "https://www.fcc.gov/proceedings-actions/mergers-transactions/xm-and-sirius", "FCC", "2008", "규제심사와 합병 승인 검증."),
    S("XM/Sirius merger completion", "https://www.sec.gov/Archives/edgar/data/908937/000095012308009301/y65279exv99w1.htm", "SEC / Sirius XM", "2008-07-29", "거래 종결 검증."),
]

SIRI_SOURCES = [
    S("Sirius 2007 Form 10-K", "https://www.sec.gov/Archives/edgar/data/908937/000095012308002331/y50289e10vk.htm", "SEC / Sirius", "2008", "2007 subscriber·revenue 성장 검증."),
    S("XM/Sirius merger announcement", "https://investor.siriusxm.com/sec-filings/sirius-xm-holdings-inc/content/0000950123-07-003042/0000950123-07-003042.pdf", "SEC / Sirius XM", "2007-02-19", "합병 선택권과 조건 검증."),
    S("Sirius XM 2016 filing/results", "https://investor.siriusxm.com/sec-filings/sirius-xm-holdings-inc/content/0000908937-17-000007/0000908937-17-000007.pdf", "SEC / Sirius XM", "2017", "2016 revenue·EBITDA·FCF 검증."),
    S("Sirius XM FY2017 results", "https://investor.siriusxm.com/news-events/press-releases/detail/1204/siriusxm-reports-fourth-quarter-and-full-year-2017-results", "Sirius XM", "2018", "2017 EBITDA·FCF 검증."),
    S("Q2 2018 results", "https://investor.siriusxm.com/news-events/press-releases/detail/1141/siriusxm-reports-second-quarter-2018-results", "Sirius XM", "2018", "net adds·revenue·FCF momentum 검증."),
    S("Q3 2018 results", "https://investor.siriusxm.com/news-events/press-releases/detail/1114/siriusxm-reports-third-quarter-2018-results", "Sirius XM", "2018", "40% 초과 EBITDA margin 검증."),
    S("CRB SDARS III rates", "https://www.crb.gov/rate/16-CRB-0001-SR-PSSR-SDARSIII/appendix-a-rates-and-terms.pdf", "Copyright Royalty Board", "2017", "2018~2022 15.5% royalty rate 검증."),
    S("Pandora acquisition completion", "https://investor.siriusxm.com/news-events/press-releases/detail/1084/siriusxm-completes-acquisition-of-pandora", "Sirius XM", "2019-02-01", "Pandora 인수와 대가 검증."),
    S("Sirius XM FY2021 results", "https://www.sec.gov/Archives/edgar/data/908937/000090893722000004/siriq42021earningsrelease.htm", "SEC / Sirius XM", "2022", "subscriber·buyback authorization 검증."),
    S("2024 Liberty simplification", "https://investor.siriusxm.com/news-events/press-releases/detail/2105/siriusxm-kicks-off-new-phase-as-an-independent-public", "Sirius XM", "2024", "거래·reverse split·추가 debt 검증."),
    S("Sirius XM 2025 Form 10-K", "https://www.sec.gov/Archives/edgar/data/908937/000090893726000006/siri-20251231.htm", "SEC / Sirius XM", "2026", "2025 subscriber·FCF·사업구조 검증."),
]


def idea_sources(idea):
    raw = S(
        "VIC original idea" if idea["source"] else "VIC source-DB preserved original",
        idea["source"],
        "Value Investors Club / source SQL",
        idea["date"],
        "T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준. SGA 2010은 본문이 누락되어 가격 series와 2019 동일 작성자 회고만 사용.",
        "원문",
    )
    return [raw, *idea["sources"]]


IDEAS = [
    dict(
        id="cdd1ef14-3122-41eb-8f8d-da184b6b6add", date="2013-09-12", author="pcm983", ticker="CMLS", company="Cumulus Media",
        filename="analysis/ideas/2013/2013-09-12_CMLS_long.md", source="https://www.valueinvestorsclub.com/idea/CUMULUS_MEDIA_INC/2033948422",
        raw_short=True, direction="Long", security="CMLS common equity / Long", entry="원문 implied 약 $5.35; target $7.50", horizon="12~18개월", raw_horizon="명시적 12~18개월",
        title="Dial Global 시너지와 자발적 deleveraging을 산 고레버리지 common Long", verdict="강한 실패 — common equity가 두 차례 구조조정으로 훼손", score=2.0, process=3.5,
        conclusion="Talk-heavy radio의 방어력과 Westwood One 전략가치는 일부 남았지만, 7.5배 레버리지 common이 $700m을 자발적으로 갚아 equity value를 복리화한다는 핵심은 실패했다. 2017년 첫 Chapter 11에서 약 $1bn, 2026년 두 번째 절차에서 약 $600m의 부채를 법원절차로 줄였다.",
        t0="Cumulus는 467개 station과 전국 광고 inventory를 가진 대형 terrestrial radio 사업자였다. 원문은 local/national 광고 75/25, talk 중심 포맷, Dial Global 인수로 추가되는 약 $150m revenue·$30m EBITDA와 약 $40m cost synergy를 근거로 2014E EV/EBITDA 8.5배, 12~18개월 $7.50 target을 제시했다. 당시 leverage는 약 7.5배였다.",
        reverse="시장이 싼 배수를 준 이유는 radio 광고의 구조적 감소가 높은 고정비와 cash interest를 통과하며 common을 압착할 수 있기 때문이다. $7.50이 되려면 synergy가 현금으로 실현되고, asset swaps가 현금화되며, EBITDA 감소 없이 3년간 $700m을 갚아야 했다. 단순 multiple discount가 아니라 여러 동시조건의 refinancing option이었다.",
        valuation="원문은 2013E EBITDA 대비 약 10배, 2014E 약 8.5배를 제시했고 2017E EBITDA 약 $525m, 8배 terminal multiple, 12.5% WACC, debt $2bn·3.5배 leverage로 $6.50 DCF floor를 주장했다. 하지만 2017E UFCF 약 $505m 표기는 EBITDA와 거의 같아 tax·interest·capex bridge 또는 단위가 내부적으로 맞지 않는다. V9에서는 이 수치를 확정 FCF로 쓰지 않는다.",
        scenarios=[("Bear", "광고 감소·synergy 미달·7배 leverage", "refinancing/Chapter 11", "2017과 2026 두 차례 현실화"), ("Base", "$40m synergy·완만한 안정", "debt paydown 후 $6.50~$7.50", "자발적 paydown보다 법원절차"), ("Bull", "EBITDA $525m·3.5배 leverage", "큰 equity convexity", "미달")],
        actual="Cumulus는 2017-11-29 첫 Chapter 11을 신청했고 2018-06-04 약 $1bn 적은 debt로 나왔다. 2019년에는 $220m, emergence 이후 누적 $275m 이상을 갚아 4.7배 leverage를 보고했다. 2022년 3.7배까지 낮아졌지만 2023년 상반기 revenue -11.3%, EBITDA -46.5%로 영업축이 다시 약해졌다. 2024 adjusted EBITDA는 $82.7m, debt는 $671.6m이었고 2026-03 두 번째 Chapter 11에서 약 $600m 제거 계획을 발표했다.",
        price="원 DB에 event-date 가격 series가 없어 12~18개월 total return, MFE·MAE, exact IRR은 계산하지 않는다. 다만 첫 Chapter 11과 두 번째 restructuring은 기존 common의 장기 terminal outcome이 실패했음을 직접 보여준다. 이후 사업자산의 존속은 2013 common security의 성공과 다르다.",
        drivers="단기적으로 Dial Global/Westwood One 결합과 비용절감은 네트워크 자산의 생존력을 높였고 2018 이후 실제 debt paydown도 있었다. 그러나 손실을 만든 핵심은 높은 시작 leverage, secular ad decline, EBITDA 변동성이다. $40m synergy의 현금가치보다 debt claim의 규모와 refinancing 반복이 컸다.",
        counterfactual="Dial Global 시너지가 전액 실현됐더라도 core radio EBITDA가 매년 중한 자릿수 감소했다면 7.5배 common에 충분한 safety margin이 있었는가?",
        error="Synergy·asset swap·deleveraging을 하나의 확정 bridge로 연결했고, downside를 낮은 terminal growth로만 처리했다. 7.5배 leverage에서는 EBITDA stress와 maturity/refinancing을 먼저 모델링했어야 한다.",
        warning="2017-11 Chapter 11이 최종 반증이다. 그 전에는 광고·EBITDA가 $700m 자발적 paydown schedule을 따라가지 못하고 refinancing 의존도가 유지된 시점이 첫 경고였다.", first_signal_date="2017-11-29",
        lessons=["고레버리지 미디어의 synergy는 debt paydown 이후 common 귀속액으로 계산한다.", "DCF의 UFCF가 EBITDA와 비슷하면 세금·capex·운전자본 bridge부터 감사한다.", "사업자산 생존과 기존 common security 생존을 분리한다."],
        checklist=["same-station revenue", "synergy 현금실현", "cash interest", "2년 평균 EBITDA leverage", "maturity wall", "asset-sale net cash", "자발적 debt paydown"],
        scorecard=[("Business thesis", "자산 생존·방어력 일부"), ("Valuation thesis", "실패"), ("Catalyst thesis", "synergy 일부·deleveraging 방식 실패"), ("Timing / path", "실패"), ("Security selection", "common 부적절")],
        claims=[
            C("terrestrial radio는 안정 또는 성장", "지역 radio cash flow가 안정적이고 talk는 음악보다 대체위험이 낮다.", "지역성·실시간 talk가 청취와 광고 inventory를 지킨다.", "467개 station, local/national 75/25, talk-heavy mix.", "디지털 대체가 pricing과 청취시간을 크게 훼손하지 않는다.", "same-station revenue·EBITDA가 반복 감소하면 반증.", "2023 1H revenue -11.3%, EBITDA -46.5%; 2024 EBITDA $82.7m.", "방어력보다 고정비 leverage가 컸다.", "실패", "콘텐츠 차별화를 매체 economics 지속성으로 확장했다.", "format moat는 organic revenue와 margin으로 검증한다."),
            C("Dial Global은 $40m cost synergy", "인수로 $150m revenue·$30m EBITDA와 약 $40m 비용시너지를 얻는다.", "중복 network·판매·corporate 비용을 제거한다.", "$260m 거래와 management synergy 제시.", "통합비용과 core decline이 synergy를 상쇄하지 않는다.", "pro forma EBITDA가 synergy 전 대비 개선되지 않으면 반증.", "Westwood One은 존속했지만 두 차례 restructuring을 막지 못했다.", "synergy의 equity 귀속이 확인되지 않았다.", "부분 성공/경제적 실패", "gross synergy와 after-interest common FCF를 혼동했다.", "시너지는 integration cost와 base erosion을 차감한다."),
            C("station 거래가 deleveraging 재원을 만든다", "53개 매각·15개 swap으로 debt를 낮춘다.", "비핵심 자산 현금화가 leverage를 즉시 줄인다.", "거래 발표의 station package.", "headline asset value가 net cash로 전환된다.", "net proceeds가 debt 대비 미미하면 반증.", "원문 자체도 net cash를 약 $22m으로 계산했다.", "$22m은 수십억 debt 대비 1% 미만.", "실패", "자산 수와 현금 proceeds 규모를 혼동했다.", "asset sale은 net cash/debt 비율로 본다."),
            C("3년 $700m 자발적 debt paydown", "FCF와 거래효과로 leverage를 7.5배에서 3.5배 부근으로 낮춘다.", "cash sweep이 equity option의 strike를 내린다.", "원문 3년 paydown schedule과 2017E debt $2bn.", "core EBITDA와 refinancing access가 유지된다.", "법원절차가 필요하거나 schedule이 크게 늦으면 반증.", "2017 Chapter 11에서 약 $1bn 제거; 이후 paydown 뒤 2026 다시 약 $600m 법원절차.", "자발적 deleveraging이 아니라 두 차례 restructuring.", "실패", "debt 감소의 방식과 기존 주주 귀속을 구분하지 않았다.", "deleveraging은 voluntary와 coercive를 분리한다."),
            C("8.5배 2014E valuation은 싸다", "거래 후 EBITDA 기준 낮은 배수가 $7.50 target을 지지한다.", "안정 EBITDA에 peer multiple이 적용되면 equity convexity가 크다.", "EV 약 $3.6bn과 2013E 10배·2014E 8.5배.", "forward EBITDA가 실현되고 debt가 감소한다.", "EBITDA miss로 실제 multiple이 올라가면 반증.", "영업침체와 restructuring으로 common target은 장기 유지되지 못했다.", "낮은 forward multiple이 denominator risk를 숨겼다.", "실패", "forecast EBITDA의 cyclicality를 충분히 hair-cut하지 않았다.", "levered equity는 stressed EBITDA 배수부터 계산한다."),
            C("$6.50 DCF floor와 $7.50 target", "12.5% WACC·8배 terminal로 downside가 제한된다.", "미래 UFCF와 낮은 terminal growth가 debt 차감 후 common value를 남긴다.", "2017E EBITDA $525m·UFCF 약 $505m 표기.", "UFCF bridge와 terminal debt가 경제적으로 일관된다.", "UFCF가 EBITDA에 비정상적으로 근접하면 모델을 기각.", "공시 outcome은 두 번의 debt restructuring이었다.", "핵심 FCF 표기의 내부 불일치와 terminal failure.", "실패", "모델 내부검증 없이 point target을 사용했다.", "DCF floor는 accounting bridge와 capital structure stress를 통과해야 한다."),
        ],
        metrics=[("시작 leverage", "약 7.5x", "3년 내 약 3.5x", "2018 법원절차; 2022 3.7x 후 재악화", "실패"), ("Dial Global cost synergy", "$40m", "현금화", "독립 common payoff 미확인", "미검증"), ("3년 debt paydown", "$700m", "자발적 상환", "2017 약 $1bn 법원감축", "실패"), ("2024 adjusted EBITDA", "2017E $525m", "안정 성장", "$82.7m", "대폭 미달"), ("2024 debt", "2017E $2bn·3.5x", "지속 하락", "$671.6m 후 2026 재구조화", "방식 실패")],
        timeline=[("2013-09-12", "VIC Long", "$7.50 target·Dial Global synergy"), ("2017-11-29", "첫 Chapter 11", "기존 common thesis 직접 반증"), ("2018-06-04", "emergence", "약 $1bn debt 제거"), ("2019-12-31", "$220m debt paydown", "신자본구조에서 개선"), ("2022-12-31", "leverage 3.7x", "일시적 정상화"), ("2024-12-31", "EBITDA $82.7m·debt $671.6m", "재구조화 위험"), ("2026-03-05", "두 번째 Chapter 11", "약 $600m 제거 계획"), ("2026-08-14", "FCC 승인 대기", "절차 미종결")], sources=CMLS_SOURCES,
    ),
    dict(
        id="23194b96-65fc-46b4-9b03-7fb4033d4e37", date="2010-12-20", author="andreas947", ticker="SGA", company="Saga Communications",
        filename="analysis/ideas/2010/2010-12-20_SGA_long.md", source="https://www.valueinvestorsclub.com/idea/Saga_CommunicationsSGA/4972998580",
        raw_short=True, direction="Long", security="SGA Class A common equity / Long", entry="$12.6072 next-day open; 원문 본문 누락", horizon="3년·5년 가격 series 병기", raw_horizon="원문 본문 누락으로 명시 horizon 복원 불가",
        title="본문 누락이지만 후속 회고와 가격 series로 검증되는 무차입 전환 Long", verdict="가격 기준 강한 성공 — claim reconstruction 신뢰도 제한", score=8.5, process=5.0,
        conclusion="원 SQL에 본문과 catalyst가 없어 원래의 target·세부 claim을 발명하지 않는다. 다만 동일 작성자의 2019 회고는 2010 아이디어가 80% 이상 상승했다고 기록하고, DB 가격 series는 1년 +41.6%, 3년 +162.9%, 5년 +130.4%를 보여준다. 배당 제외 연환산은 각각 3년 38.01%, 5년 18.16%다.",
        t0="2010 원문 body가 source SQL에서 누락됐다. 따라서 이 문서는 2019년 동일 작성자가 설명한 SGA의 안정적 same-station revenue, 2008~2010 debt 감소와 후속 DB 가격 series로만 제한적으로 재구성한다. 정확한 진입 thesis, target, catalyst, horizon은 미복원이다.",
        reverse="결과를 알고 과거 논지를 아름답게 재구성하면 hindsight bias가 생긴다. 여기서 검증 가능한 최소 명제는 높은 FCF와 debt 감소가 equity value로 전환됐는지, 그리고 가격 series가 그 방향과 일치하는지뿐이다. 2019 원문의 숫자는 2010 원문을 대체하지 않는다.",
        valuation="동일 작성자의 후속 회고에 따르면 cash from operations는 2007~2009 $27m·$25m·$26m, 2008~2009 FCF는 $17~18m였고 net debt는 2008 초 약 $130m에서 2010 말 약 $90m로 줄었다. 당시 정확한 share count·target multiple이 없어 original upside bridge는 복원하지 않는다. realized price CAGR만 별도로 제시한다.",
        scenarios=[("Bear", "본문 부재·FCF 감소", "판정 보류", "가격 series와 불일치"), ("Base", "안정 매출·debt 감소", "equity rerating", "3년 +162.9%"), ("Bull", "순현금 전환·자본환원", "장기 compound", "2019 순현금 약 $30m")],
        actual="후속 2019 원문은 net debt가 2008 초 약 $130m, 2010 말 약 $90m에서 2019-06 순현금 약 $30m으로 전환됐다고 회고했다. DB는 next-day open $12.6072, close $12.9501와 장기 가격비율을 보존한다. 정확한 배당 reinvestment는 포함되지 않았다.",
        price="가격비율은 1개월 0.972x, 3개월 1.285x, 6개월 1.344x, 1년 1.416x, 2년 1.877x, 3년 2.629x, 5년 2.304x다. 즉 price-only 수익률은 -2.8%, +28.5%, +34.4%, +41.6%, +87.7%, +162.9%, +130.4%다. 3년·5년 연환산은 38.01%, 18.16%이며 배당 포함 IRR은 더 높을 수 있으나 계산하지 않는다.",
        drivers="가격 성공을 만든 관찰 가능한 driver는 경기침체에도 유지된 현금창출, debt 감소, 이후 순현금 전환이다. 단, 원문 claim이 없기 때문에 이 인과를 저자의 정확한 ex-ante thesis였다고 확정할 수 없다. 성과 판정과 프로세스 판정을 분리한다.",
        counterfactual="같은 가격 성과가 나왔더라도 원래 논지가 전혀 다른 catalyst였다면 이를 thesis success라고 부를 수 있는가?",
        error="가장 큰 제한은 source completeness다. 후속 회고를 원문처럼 취급하거나 realized winner에서 claim을 역추론하면 안 된다.", warning="본문 누락 자체가 즉시 데이터 품질 경고다. 따라서 가격·debt facts 외의 claim confidence를 낮췄다.", first_signal_date="2010-12-20",
        lessons=["원문이 없으면 target과 catalyst를 만들지 말고 복원 범위를 명시한다.", "가격 성공과 분석과정 성공은 별도 점수로 둔다.", "장기 price ratio는 배당·세금·거래비용과 분리한다."],
        checklist=["원문 archive 복구", "same-station revenue", "CFO·capex", "net debt", "배당 포함 total return", "share count", "후속 회고와 원문 분리"],
        scorecard=[("Business thesis", "후속자료상 성공"), ("Valuation thesis", "원문 누락"), ("Catalyst thesis", "원문 누락"), ("Timing / path", "강한 성공"), ("Security selection", "common Long 적중")],
        claims=[
            C("현금창출은 recession에도 유지", "후속 회고 기준 2007~2009 CFO가 $25~27m 수준이었다.", "지역 radio의 반복 광고·낮은 capex가 debt service 여력을 만든다.", "2019 동일 작성자의 역사 수치.", "후속 회고가 당시 공시를 정확히 요약한다.", "CFO가 급감하거나 capex가 FCF를 소진하면 반증.", "2008~2009 FCF $17~18m으로 회고됐다.", "방향상 유지; 원문 claim 여부 미확인.", "부분 검증", "후속 자료를 T0 evidence로 소급할 위험.", "reconstructed claim에는 별도 confidence를 붙인다."),
            C("net debt가 감소", "2008 초 약 $130m에서 2010 말 약 $90m으로 줄었다.", "FCF가 creditor claim을 줄여 common residual을 확대한다.", "동일 작성자 2019 회고.", "현금이 M&A보다 debt reduction에 우선 사용된다.", "net debt가 다시 늘면 반증.", "2019-06 순현금 약 $30m으로 전환.", "약 $120m 개선.", "성공", "정확한 원문 목표 속도는 미복원.", "deleveraging은 시작·종료 debt와 기간으로 측정한다."),
            C("same-station revenue는 상대적으로 안정", "지역 매출 기반이 secular decline을 완만하게 만든다.", "중소시장 관계형 영업이 national volatility를 줄인다.", "2019 retrospective business description.", "local advertiser retention이 유지된다.", "여러 해 organic decline이 FCF를 훼손하면 반증.", "장기 생존과 순현금 전환은 최소한 cash engine의 방어력을 지지한다.", "정확한 2010~2013 organic series 미복원.", "부분 성공", "survivorship로 매출안정을 역추론했다.", "business evidence와 price outcome을 분리한다."),
            C("낮은 capex가 FCF를 만든다", "CFO 대부분이 debt paydown 가능한 cash로 남는다.", "방송 주파수·studio의 maintenance intensity가 낮다.", "2008~2009 FCF $17~18m 회고.", "license·digital 투자의 숨은 capex가 작다.", "CFO와 FCF gap이 커지면 반증.", "debt 감소와 순현금 전환이 실제 cash conversion을 지지한다.", "정확한 capex bridge는 미복원.", "부분 성공", "회고 수치에 의존.", "FCF는 CFO-capex와 자산매각을 분리한다."),
            C("deleveraging이 multiple rerating을 만든다", "부채 감소가 equity 위험과 이자비용을 낮춘다.", "enterprise value가 같아도 debt 1달러 감소는 common에 귀속된다.", "2008~2010 debt 감소.", "EV가 secular decline보다 덜 감소한다.", "debt 감소에도 주가가 장기 하락하면 반증.", "3년 price ratio 2.629x, 5년 2.304x.", "3년 +162.9%, 5년 +130.4%.", "성공", "배당 제외 series임을 명시해야 함.", "capital structure thesis는 price CAGR과 함께 본다."),
            C("Long의 realized return은 강하다", "동일 작성자는 80%+ gain을 회고했다.", "사업 안정·debt 감소·rerating이 누적수익을 만든다.", "DB next-day price series.", "series 정의가 동일하고 corporate action 왜곡이 없다.", "3년·5년 ratio가 1배 이하면 반증.", "3년 2.629x, 5년 2.304x.", "연환산 38.01%, 18.16% price-only.", "성공", "total return과 price-only를 혼동할 수 있다.", "성과 숫자에는 series 정의와 포함항목을 붙인다."),
        ],
        metrics=[("Next-day open", "미복원", "entry proxy", "$12.6072", "DB 관찰치"), ("1년 price return", "미복원", "Long", "+41.62%", "성공"), ("3년 price return", "미복원", "Long", "+162.88% / 연 38.01%", "강한 성공"), ("5년 price return", "미복원", "Long", "+130.37% / 연 18.16%", "성공"), ("Net debt", "2010 말 약 $90m", "감소", "2019-06 순현금 약 $30m", "성공")],
        timeline=[("2010-12-20", "VIC Long", "본문 누락"), ("2011-01", "1개월 ratio 0.972x", "초기 약세"), ("2011-03", "3개월 ratio 1.285x", "rerating 시작"), ("2011-12", "1년 ratio 1.416x", "Long 적중"), ("2013-12", "3년 ratio 2.629x", "연 38.01%"), ("2015-12", "5년 ratio 2.304x", "연 18.16%"), ("2019-06", "순현금 약 $30m 회고", "deleveraging 장기완료")], sources=SGA_SOURCES,
    ),
    dict(
        id="e40ec74c-12db-460c-bab8-c7c4435c1d90", date="2019-08-24", author="andreas947", ticker="SGA", company="Saga Communications",
        filename="analysis/ideas/2019/2019-08-24_SGA_long.md", source="https://www.valueinvestorsclub.com/idea/SAGA_COMMUNICATIONS__-CL_A/2363353097",
        raw_short=False, direction="Long", security="SGA Class A common equity / Long", entry="$29 원문", horizon="약 3년 관찰", raw_horizon="명시 horizon 없음; DB 3년 series 사용",
        title="순현금·13% unlevered FCF yield의 안전은 맞았지만 $50 rerating은 실패한 Long", verdict="혼합 — business 방어 성공, target·timing 실패", score=5.5, process=7.0,
        conclusion="$29에서 약 $30m net cash, $30m LTM EBITDA, $20m sustainable FCF를 근거로 $50을 제시했다. pandemic에도 회사는 버텼지만 DB price-only 경로는 1년 -18.2%, 2년 -10.8%, 3년 +9.6%, 연 3.10%로 target과 거리가 컸다. 순현금의 downside 보호는 맞았고 FCF durability와 multiple rerating은 과대평가했다.",
        t0="SGA는 79 FM·34 AM과 77개 metro signal을 운영했고 매출 약 87%가 local이었다. 6m shares, market cap $174m, net cash 약 $30m, EV $145m, LTM EBITDA 약 $30m으로 adjusted 5배, sustainable FCF 약 $20m으로 13%+ unlevered yield라는 논지였다.",
        reverse="시장은 순현금을 인정하면서도 radio terminal decline, 지배구조, 낮은 유동성, capital-return 불확실성을 가격에 넣었다. $50이 되려면 2020E EBITDA $32m, net cash $50m, 8배 EV/EBITDA가 동시에 필요했다. FCF만 유지되고 multiple이 그대로면 target은 나오지 않는다.",
        valuation="원문 target은 `8 × $32m EBITDA + $50m net cash = 약 $300m equity`, 6m shares 기준 $50이었다. EBITDA 5배의 저평가와 13%+ unlevered FCF yield는 분명했지만, radio의 감소 duration과 control/liquidity discount를 반영한 terminal multiple 감도가 컸다.",
        scenarios=[("Bear", "pandemic/organic decline·배수 4~5x", "현금이 downside 완충", "1년 -18.2%"), ("Base", "$20m FCF·현금누적", "점진적 rerating", "3년 +9.6%"), ("Bull", "$32m EBITDA·$50m cash·8x", "$50 / +72%", "미달")],
        actual="2020 revenue는 pandemic으로 $95.8m까지 감소했지만 FCF는 $18.1m으로 2019 $19.5m에 근접했다. 2022 revenue는 $114.9m으로 회복했으나 FCF는 $10.5m이었다. 2025 revenue는 $107.112m, 전년 대비 -5.1%, CFO는 $5.464m으로 2024 $13.772m에서 감소했다. digital gross revenue mix는 2024 12%에서 2025 15%로 늘었고 local 비중은 91%였다.",
        price="DB price ratio는 1개월 1.065x, 3개월 1.065x, 6개월 1.086x, 1년 0.818x, 2년 0.892x, 3년 1.096x다. 3년 price-only 연환산은 3.10%다. 배당은 포함되지 않았으므로 total return은 이보다 높을 수 있지만 $50 target 달성 근거는 없다.",
        drivers="순현금과 local 광고 mix는 pandemic 충격에서 파산·희석을 막아줬다. 그러나 8배 rerating에 필요한 EBITDA/FCF 성장과 명확한 capital return이 늦었고, 2022 FCF는 원문 $20m sustainable 수준의 절반가량이었다. safety와 upside catalyst를 같은 것으로 취급한 점이 핵심이다.",
        counterfactual="$20m FCF가 유지됐지만 시장이 terminal decline 때문에 계속 5배를 적용했다면 $50 target은 무엇으로 실현됐을까?",
        error="순현금·낮은 배수라는 downside 근거는 강했지만 8배 rerating의 catalyst와 governance discount 해소를 별도로 입증하지 않았다.", warning="1년 price ratio 0.818x와 2022 FCF $10.5m이 각각 시장·fundamental 경고였다.", first_signal_date="2020-08-24",
        lessons=["순현금은 downside buffer이지 자동 rerating catalyst가 아니다.", "sustainable FCF는 recession year와 recovery year를 함께 stress한다.", "price-only와 dividend total return을 분리한다."],
        checklist=["same-station ex-political", "FCF 3년 평균", "순현금", "배당·특별배당", "digital contribution", "control discount", "average daily liquidity"],
        scorecard=[("Business thesis", "성공"), ("Valuation thesis", "싼 가격은 맞음·target 실패"), ("Catalyst thesis", "지연"), ("Timing / path", "실패"), ("Security selection", "안전하지만 낮은 IRR")],
        claims=[
            C("local radio 매출은 상대적으로 안정", "87% local mix가 national volatility와 플랫폼 대체를 완충한다.", "지역 관계형 영업과 커뮤니티 콘텐츠가 retention을 높인다.", "79 FM·34 AM, 77 metro signals, local 87%.", "local 광고주가 경기충격 뒤 돌아온다.", "same-station revenue가 장기 감소하면 반증.", "2020 큰 하락 후 2022 revenue는 회복했지만 2025 다시 -5.1%.", "cycle 방어는 확인, 장기성장은 미확인.", "부분 성공", "안정을 영구 duration으로 확장했다.", "local mix는 drawdown과 추세를 따로 본다."),
            C("$20m FCF는 sustainable", "낮은 capex와 무이자 구조로 연 $20m FCF가 지속된다.", "EBITDA가 cash interest 없이 common cash로 전환된다.", "2019 FCF $19.5m 부근과 순현금.", "pandemic 이후 margin이 복원된다.", "2년 평균 FCF가 $14m 아래면 반증.", "2020 $18.1m이었으나 2022 $10.5m, 2025 CFO $5.5m.", "2022 FCF는 $20m 대비 -47.5%.", "부분 실패", "한 해 run-rate를 terminal cash flow로 사용했다.", "FCF는 cycle-average와 maintenance needs로 정상화한다."),
            C("5배 adjusted EBITDA는 과도하게 싸다", "EV $145m/LTM EBITDA 약 $30m은 5배다.", "무차입 사업의 낮은 enterprise multiple이 margin of safety다.", "market cap $174m·net cash $30m.", "EBITDA가 감소하지 않고 market multiple이 정상화된다.", "EBITDA 하락으로 forward multiple이 높아지면 반증.", "사업은 생존했지만 3년 price return은 +9.6%에 그쳤다.", "valuation gap이 price gap으로 전환되지 않았다.", "부분 성공", "cheapness와 catalyst를 혼동했다.", "낮은 배수에는 realization mechanism을 붙인다."),
            C("순현금이 downside를 보호", "debt가 없고 약 $30m cash가 recession 선택권을 준다.", "이자·maturity 없이 downturn을 통과하고 인수·배당을 선택한다.", "T0 balance sheet.", "현금이 operating loss로 빠르게 소진되지 않는다.", "희석·고금리 차입·distress가 오면 반증.", "pandemic을 distress 없이 통과했다.", "1년 주가는 -18.2%였지만 solvency 훼손 없음.", "성공", "가격 downside와 solvency downside는 다르다.", "net cash thesis는 survival과 return을 분리한다."),
            C("8배·$50 target", "$32m 2020E EBITDA와 $50m net cash로 $50/share를 제시했다.", "earnings growth·cash accumulation·multiple expansion이 결합한다.", "원문 valuation bridge.", "세 조건이 같은 horizon에 실현된다.", "3년 price ratio가 1.5x 미만이면 target thesis 실패.", "3년 ratio 1.096x, 연 3.10%.", "$29→$50 +72% 기대 대비 price-only +9.6%.", "실패", "세 개의 bull condition을 base처럼 사용했다.", "target은 성장·cash·multiple 기여도를 분해한다."),
            C("capital allocation이 value를 실현", "cash를 배당·특별배당·accretive deal에 쓴다.", "순현금이 discount를 주주현금으로 전환한다.", "부채 없는 구조와 이후 배당 여력.", "controller가 현금을 장기간 쌓아두지 않는다.", "3년 내 의미 있는 환원이 없으면 재평가.", "큰 자본환원은 주로 2022 이후 나타나 2019 target timing과 어긋났다.", "방향은 맞고 시간은 늦었다.", "부분 성공", "촉매 날짜와 정책 commitment가 약했다.", "cash-rich value는 payout calendar를 요구한다."),
        ],
        metrics=[("Entry / target", "$29 / $50", "+72%", "3년 price-only +9.58%", "실패"), ("LTM EBITDA", "약 $30m", "2020E $32m", "후속 FCF 약화", "미달"), ("Sustainable FCF", "$20m", "유지", "2022 $10.5m", "-47.5%"), ("1년 price return", "Long", "상승", "-18.24%", "실패"), ("3년 price return", "Long", "target 접근", "+9.58% / 연 3.10%", "미달")],
        timeline=[("2019-08-24", "VIC Long", "$29→$50"), ("2020-08", "1년 ratio 0.818x", "초기 thesis break"), ("2020-12-31", "revenue $95.8m·FCF $18.1m", "pandemic 방어"), ("2021-08", "2년 ratio 0.892x", "rerating 부재"), ("2022-08", "3년 ratio 1.096x", "연 3.10%"), ("2022-12-31", "revenue $114.9m·FCF $10.5m", "FCF miss"), ("2025-12-31", "revenue -5.1%·CFO $5.5m", "장기 earning 약화")], sources=SGA_SOURCES,
    ),
    dict(
        id="8f8b9173-3403-4002-abd0-203cc4c71935", date="2022-07-14", author="militiaman", ticker="SGA", company="Saga Communications",
        filename="analysis/ideas/2022/2022-07-14_SGA_long.md", source="https://www.valueinvestorsclub.com/idea/SAGA_COMMUNICATIONS_INC/2889162014",
        raw_short=False, direction="Long", security="SGA Class A common equity / Long", entry="next-day open $21.5556; 원문 target $32", horizon="6~12개월", raw_horizon="원문 약 1년 catalyst framing; DB 6개월까지",
        title="순현금·부동산·특별배당의 value realization은 맞았지만 FCF forecast는 빗나간 Long", verdict="근접기간 부분 성공 — 배당 강함, 영업모델 미달", score=7.0, process=7.0,
        conclusion="원문은 EV 약 $81m, net cash $55m, $15~20m FCF와 owned real estate를 근거로 $32 target을 제시했다. 2022 actual revenue $114.9m은 $118m forecast보다 2.6%, FCF $10.5m은 $15m 하단보다 30% 낮았다. 그러나 게시 후 약 6개월 안에 $4.50의 특별·정기 배당이 선언됐고 DB price ratio도 1.107x여서 capital-return catalyst는 강하게 적중했다.",
        t0="SGA는 79 FM·35 AM, 27 markets, local ad 89%, no debt와 net cash 약 $55m을 보유했다. owned land/buildings/towers의 gross book value는 $78.1m, EV는 약 $81m이었다. 원문은 2022 revenue $118m, operating profit $19m, FCF $15m, EV $135m+cash $55m으로 $32/share를 제시했다.",
        reverse="싼 EV는 radio terminal decline, 지배주주 succession, 낮은 liquidity와 현금의 미실현을 반영했을 수 있다. $32가 되려면 FCF $15~20m, 배당 또는 sale, digital 성장, 89% local 매출의 방어가 같은 기간에 필요했다. 자산 book value는 liquidation proceeds와 다르다.",
        valuation="T0 market cap 약 $136m·net cash $55m·EV 약 $81m이었다. $15~20m FCF이면 unlevered yield는 약 19~25%다. 원문 base target은 EV $135m+cash $55m=$190m equity, 약 $32/share였다. actual 2022 FCF $10.5m을 쓰면 T0 EV/FCF는 약 7.7배로 여전히 낮지만 원문 yield보다 상당히 약하다.",
        scenarios=[("Bear", "revenue/FCF miss·현금유보", "20달러 초반 정체", "영업은 이쪽"), ("Base", "$15m FCF·배당", "$32 접근", "배당은 적중·가격 미달"), ("Bull", "$20m FCF·digital 10%+·sale", "40%+", "미실현")],
        actual="2022 revenue는 $114.9m, FCF는 $10.5m이었다. 회사는 2022-10 $2 특별배당+$0.25 정기배당, 2023-01 다시 $2 특별배당+$0.25 정기배당을 지급해 게시 후 약 6개월에 총 $4.50을 선언했다. 2024에도 variable $0.60과 정기배당을 지급했고 2012 이후 누적 배당은 $133m을 넘었다. 반면 2025 revenue와 CFO는 약해졌다.",
        price="DB price ratio는 1주 1.009x, 2주 0.993x, 1개월 1.030x, 3개월 1.062x, 6개월 1.107x다. 이 series의 배당조정 여부가 확인되지 않아 $4.50을 더해 total return을 만들지 않는다. 관찰 가능한 price-only 6개월 수익률은 +10.74%다.",
        drivers="근접기간 수익은 사업 성장보다 excess cash의 특별배당 전환이 만들었다. 영업 forecast는 revenue -2.6%, FCF -30% miss였지만, balance-sheet margin of safety와 payout catalyst가 이를 상쇄했다. 장기적으로는 revenue·CFO 감소가 terminal multiple을 제한한다.",
        counterfactual="특별배당이 없고 2022 FCF $10.5m만 확인됐다면 $32 target을 유지할 근거가 남았는가?",
        error="owned real estate의 gross book value를 realizable floor처럼 읽고, digital gross revenue 성장을 segment contribution으로 연결했다. 반대로 payout 가능성은 실제보다 보수적으로 평가했다.", warning="2022 FCF $10.5m이 첫 영업 반증이지만 2022-10 $2.25 dividend가 catalyst 성공을 동시에 확인했다.", first_signal_date="2022-10-01",
        lessons=["cash-rich value trap은 영업 thesis와 payout thesis를 분리하면 판정이 선명해진다.", "부동산 book value는 tax·sale probability·사업필수성을 차감한다.", "배당조정 여부가 불명확한 price series에 현금배당을 중복가산하지 않는다."],
        checklist=["FCF vs forecast", "net cash", "board payout policy", "special dividend record date", "digital contribution", "owned real estate saleability", "local ex-political revenue"],
        scorecard=[("Business thesis", "부분 실패"), ("Valuation thesis", "낮은 EV는 맞음"), ("Catalyst thesis", "강한 성공"), ("Timing / path", "6개월 성공"), ("Security selection", "common Long 적절")],
        claims=[
            C("local 89%가 매출을 방어", "중소시장 local 광고가 national decline보다 안정적이다.", "지역관계·낮은 플랫폼 대체가 station cash flow를 지킨다.", "79 FM·35 AM, local 89%.", "경기둔화에도 same-station 매출이 유지된다.", "2022 revenue가 $118m 대비 5% 이상 미달하면 약화.", "2022 $114.9m으로 forecast 대비 -2.6%.", "허용범위 내 소폭 미달.", "부분 성공", "local share를 성장률로 읽을 위험.", "local mix와 organic growth를 분리한다."),
            C("연 FCF $15~20m", "낮은 capex와 무이자 구조로 $15~20m이 반복된다.", "EBITDA가 cash interest 없이 주주현금으로 전환된다.", "T0 model과 balance sheet.", "revenue와 margin이 유지된다.", "actual FCF가 $12m 아래면 반증.", "2022 FCF $10.5m.", "$15m 하단 대비 -$4.5m/-30%.", "실패", "정상화 margin을 높게 잡았다.", "FCF forecast는 revenue·margin·capex bridge로 감사한다."),
            C("EV $81m은 자산과 현금흐름 대비 싸다", "owned real estate $78.1m gross book과 FCF가 EV를 지지한다.", "tangible assets와 cash flow가 downside floor를 만든다.", "market cap $136m-net cash $55m.", "자산이 매각 가능하고 영업에 필수적이지 않다.", "sale discount·tax 후 proceeds가 작으면 반증.", "대규모 부동산 realization은 확인되지 않았지만 distress도 없었다.", "book value floor는 미검증.", "미검증", "gross book을 liquidation value로 암묵 사용.", "asset floor는 net realizable value로만 쓴다."),
            C("digital은 10%+ 매출로 성장", "2021 +86%, 2022 Q1 +75% 성장해 6%에서 10%+가 된다.", "existing local salesforce가 digital wallet share를 늘린다.", "T0 growth rates와 6% mix.", "높은 성장률이 큰 base에서도 지속되고 contribution이 양수다.", "mix가 정체하거나 gross growth가 profit으로 안 이어지면 약화.", "2025 digital gross revenue mix는 15%로 상승.", "mix target 초과; contribution economics는 제한적.", "부분 성공", "gross revenue와 net profit을 혼동했다.", "digital은 gross·net·segment profit을 함께 본다."),
            C("특별배당이 excess cash를 실현", "정기 $0.20 외 추가 환원이 가능하다.", "no debt와 excess cash가 shareholder distribution으로 전환된다.", "T0 $55m net cash·배당 이력.", "board가 현금을 유보하지 않는다.", "12개월 내 추가환원이 없으면 catalyst 약화.", "약 6개월 내 특별 $4+정기 $0.50 선언.", "$4.50/share 현금 이벤트.", "강한 성공", "확률은 맞았지만 정확한 규모는 더 컸다.", "cash-rich thesis는 payout calendar로 검증한다."),
            C("$32 target·40% upside", "EV $135m+cash $55m으로 equity $190m을 제시했다.", "FCF yield 정상화와 배당이 valuation gap을 닫는다.", "원문 bridge.", "$15m+ FCF와 multiple rerating이 동시 발생한다.", "6~12개월 price와 배당 합계가 target에 크게 못 미치면 실패.", "6개월 price-only +10.7%, 큰 배당은 있었지만 $32 가격은 미확인.", "target 미달·현금수익 보완.", "부분 성공", "target price와 total payout을 혼합했다.", "price target과 cash distribution return을 따로 측정한다."),
        ],
        metrics=[("2022 revenue", "$118m", "forecast", "$114.9m", "-2.6%"), ("2022 FCF", "$15m", "하단 달성", "$10.5m", "-30.0%"), ("Net cash", "$55m", "downside buffer", "no-debt 유지·배당", "성공"), ("6개월 price return", "Long", "상승", "+10.74%", "성공"), ("6개월 내 declared dividends", "추가환원", "미정", "$4.50/share", "강한 성공")],
        timeline=[("2022-07-14", "VIC Long", "$32 target"), ("2022-10", "$2 special+$0.25 regular", "catalyst 실현"), ("2023-01", "$2 special+$0.25 regular", "6개월 누적 $4.50"), ("2023-01", "6개월 ratio 1.107x", "price-only +10.7%"), ("2022-12-31", "revenue $114.9m·FCF $10.5m", "forecast miss"), ("2024", "variable·regular dividends", "환원 지속"), ("2025-12-31", "revenue·CFO 감소", "장기 earning 경고")], sources=SGA_SOURCES,
    ),
    dict(
        id="4e88007a-5df8-4dbb-be00-cb635445aae3", date="2012-01-05", author="jordash111", ticker="SALM", company="Salem Communications",
        filename="analysis/ideas/2012/2012-01-05_SALM_long.md", source="https://www.valueinvestorsclub.com/idea/SALEM_COMMUNICATIONS_CORP/2030950212",
        raw_short=False, direction="Long", security="SALM Class A common equity / Long", entry="$2.50", horizon="장기 value realization", raw_horizon="명시 horizon 없음",
        title="35% FCF yield와 block programming 방어력을 샀지만 debt duration을 과소평가한 Long", verdict="장기 실패 — 배당 일부 실현 후 $1 take-private", score=3.0, process=6.0,
        conclusion="$2.50에서 LTM FCF $21.6m/$0.87, 35% yield와 $7~$9 가치가 제시됐다. block programming 방어력과 후속 정기배당은 일부 맞았지만 2020 배당 중단, 2024 자산매각·preferred 자금에 의존한 debt exchange와 Nasdaq 자진상장폐지, 2026 $1 take-private는 common의 장기 thesis를 부정했다.",
        t0="Salem은 95개 station을 가진 최대 기독교 중심 방송사였다. broadcast ad revenue는 2006 $108m에서 2009 $74m로 하락 후 LTM 2011 $77m, block programming은 revenue 35% 이상·renewal 90% 이상이었다. LTM EBITDA $52.4m, interest $25.2m, OCF $29.6m, capex $8m, FCF $21.6m이었다.",
        reverse="35% FCF yield는 시장이 현 FCF의 짧은 duration과 debt refinancing 위험을 가격에 넣었다는 뜻일 수 있다. 9.625% secured notes와 2016 maturity가 존재했고 interest는 EBITDA의 거의 절반이었다. $7~$9가 되려면 FCF가 유지되고 debt가 현금으로 줄며 배당이 지속돼야 했다.",
        valuation="원문은 $0.87 FCF/share에 peer value 약 $9, dividend capitalization 약 $7을 제시했다. 하지만 interest $25.2m은 EBITDA $52.4m의 48%였고, enterprise cash flow의 작은 변화가 common FCF를 크게 흔든다. V9 base는 radio EBITDA를 stress하고 debt maturity별 refinancing cost를 차감한다.",
        scenarios=[("Bear", "secular decline·refinancing·배당중단", "$1 안팎 exit", "2026 현실화"), ("Base", "block 안정·debt 감소", "$7 dividend value", "일부 배당 후 실패"), ("Bull", "광고회복·peer multiple", "$9", "미실현")],
        actual="회사는 정기배당을 시작했지만 2020-05-11 이를 중단했다. 2024 자진 Nasdaq delisting을 했고, 2024-12 $159.4m 2028 notes를 $104m cash+$24m subordinated notes로 repurchase해 $37.1m discount를 얻었다. 그러나 자금은 $40m WaterStone preferred와 약 $90m station sale/marketing transaction에 의존했다. 2026 WaterStone이 $1/share에 인수해 비공개화했다.",
        price="원 DB에 게시일 이후 표준 가격 series가 없어 original horizon IRR·MFE·MAE를 계산하지 않는다. 확정 가능한 terminal comparison은 $2.50 entry 대비 2026 $1 cash take-private로, 배당을 제외한 가격 기준 -60%다. 중간 배당을 더한 exact total return은 배당 series 부재로 계산하지 않는다.",
        drivers="block programming과 낮은 maintenance capex는 한동안 cash flow와 배당을 만들었다. 그러나 cash interest, debt maturity, AM/FM asset erosion이 그 cash를 creditor·refinancing 쪽으로 돌렸다. 2024 discount exchange는 부채감소 성공처럼 보이나 asset sale과 preferred capital을 동반해 기존 common의 경제적 승리와 다르다.",
        counterfactual="2012 FCF $21.6m이 3년 유지됐어도 이를 debt 대신 배당하고 이후 cash engine이 감소했다면 $7~$9 intrinsic value가 지속 가능했는가?",
        error="높은 trailing FCF yield를 durable annuity로 해석했고 debt maturity를 단일 날짜로만 봤다. asset-sale-funded deleveraging이 남은 earning base와 common seniority를 훼손할 가능성을 모델링하지 않았다.", warning="2020-05 배당 중단이 첫 명확한 common-level 반증이었다. 그 전에는 interest/EBITDA 약 48%와 2016 maturity가 T0 경고였다.", first_signal_date="2020-05-11",
        lessons=["35% FCF yield는 upside보다 cash-flow duration 질문부터 요구한다.", "debt discount repurchase는 자금원과 잔존 EBITDA를 함께 본다.", "배당 개시는 thesis 성공이 아니라 지속성 검증의 시작이다."],
        checklist=["block renewal·pricing", "same-station revenue", "cash interest/EBITDA", "maturity wall", "asset-sale EBITDA loss", "preferred seniority", "dividend coverage"],
        scorecard=[("Business thesis", "일시적 방어"), ("Valuation thesis", "실패"), ("Catalyst thesis", "배당 일부"), ("Timing / path", "장기 실패"), ("Security selection", "common 부적절")],
        claims=[
            C("block programming은 방어적", "35%+ revenue와 90%+ renewal이 spot 광고보다 안정적이다.", "programmer가 airtime을 구매해 audience-risk 일부를 부담한다.", "T0 revenue mix·renewal data.", "가격인상 3~6%와 renewal이 청취 감소를 상쇄한다.", "renewal·pricing이 하락하거나 station sale이 필요하면 반증.", "한동안 배당을 지지했지만 결국 station sale과 take-private로 이어졌다.", "단기 방어·장기 duration 실패.", "부분 성공", "계약 갱신을 terminal demand로 확장했다.", "renewal rate와 revenue per block을 함께 본다."),
            C("recession EBITDA는 견조", "2009 EBITDA는 peers 약 -30% 대비 약 -2% 감소했다.", "block revenue와 비용절감이 광고충격을 흡수한다.", "원문 2007~2009 comparison.", "비용절감 후에도 자산경쟁력이 유지된다.", "회복기 매출이 돌아오지 않고 비용만 고착되면 약화.", "후속 secular decline과 asset sales가 나타났다.", "cycle proof가 secular proof는 아니었다.", "부분 실패", "한 번의 recession resilience를 영구 moat로 해석했다.", "cycle과 secular stress를 별도로 둔다."),
            C("$21.6m FCF·35% yield", "LTM FCF $0.87/share가 지속돼 entry를 빠르게 회수한다.", "낮은 capex가 EBITDA를 common cash로 전환한다.", "CFO $29.6m-capex $8m.", "cash interest와 tax가 안정적이고 capex가 충분하다.", "배당중단 또는 debt-funded liquidity면 반증.", "2020 배당 중단; 2024 preferred·asset sale로 debt 해결.", "durable common FCF thesis 실패.", "실패", "trailing FCF의 maintenance/debt burden을 과소평가했다.", "FCF yield에는 debt-paydown years를 붙인다."),
            C("9.625% notes를 현금으로 상환", "2016 전 FCF로 notes를 줄이고 refinancing risk를 낮춘다.", "cash sweep이 interest를 줄여 FCF 선순환을 만든다.", "2009 이후 $47.5m redemption.", "영업 FCF가 배당과 debt reduction을 모두 감당한다.", "새 senior/preferred capital 또는 asset sale 의존 시 반증.", "2024 notes 해결은 $40m preferred와 약 $90m asset deal에 의존.", "방향은 맞았으나 방식·기간이 크게 달랐다.", "실패", "debt 감소의 funding source를 무시했다.", "organic deleveraging과 liability management를 분리한다."),
            C("배당이 $7 가치를 드러냄", "FCF 일부 배당으로 높은 yield와 rerating을 만든다.", "현금지급이 accounting FCF를 주주수익으로 확정한다.", "원문 dividend scenario.", "배당 coverage와 debt covenant가 유지된다.", "배당 suspension이면 직접 반증.", "정기배당 후 2020-05 suspension.", "촉매는 잠시 실현됐지만 지속성 실패.", "부분 성공", "개시확률과 지속확률을 혼합했다.", "payout thesis는 coverage와 stop condition을 둔다."),
            C("peer multiple로 $9", "radio peers 수준 valuation이면 3배 이상 upside다.", "business normalization과 debt 감소가 discount를 닫는다.", "원문 peer comparison.", "peer EBITDA duration이 Salem에도 적용된다.", "asset sale·delisting·private exit이면 반증.", "2024 delisting, 2026 $1 take-private.", "$2.50 대비 terminal price -60%, 배당 제외.", "실패", "peer quality·leverage 차이를 무시했다.", "peer multiple은 business mix와 capital structure를 맞춘다."),
        ],
        metrics=[("Entry / terminal deal", "$2.50", "$7~$9", "$1 take-private", "가격 -60%"), ("LTM FCF", "$21.6m/$0.87", "지속", "후속 배당중단·restructuring", "실패"), ("Cash interest/EBITDA", "$25.2m/$52.4m", "감소", "높은 debt burden 지속", "실패"), ("Block programming", ">35% revenue", "90%+ renewal", "단기 방어·장기 미흡", "부분"), ("2024 notes", "$159.4m face", "organic paydown", "$104m cash+$24m sub notes·$37.1m discount", "방식 변경")],
        timeline=[("2012-01-05", "VIC Long", "$2.50→$7~$9"), ("2012 이후", "정기배당", "초기 catalyst 실현"), ("2020-05-11", "배당 중단", "첫 명확한 반증"), ("2024", "Nasdaq 자진상장폐지", "liquidity·governance 악화"), ("2024-12-23", "notes restructuring", "asset sale·preferred 자금"), ("2026", "$1 WaterStone acquisition", "상장 common 종결")], sources=SALM_SOURCES,
    ),
    dict(
        id="a9f7338b-17a2-4aa2-99dc-1419d2b4d652", date="2019-08-06", author="Helm56", ticker="SALM", company="Salem Media Group",
        filename="analysis/ideas/2019/2019-08-06_SALM_long.md", source="https://www.valueinvestorsclub.com/idea/SALEM_MEDIA_GROUP_INC/5321637821",
        raw_short=True, direction="Long", security="SALM Class A common equity / Long", entry="약 $2.12; target $3.18", horizon="12~36개월", raw_horizon="원문 2020·2022·2023 valuation path",
        title="12.5% dividend yield와 30%+ cash-flow yield를 샀지만 leverage tail이 지배한 Long", verdict="강한 실패 — 배당 중단·delisting·$1 take-private", score=2.5, process=6.5,
        conclusion="원문은 zero 가능성을 명시하면서도 12.5% dividend yield, 30%+ cash-flow yield와 5배 2020 cash flow 기준 $3.18을 제시했다. 2020-05 배당 중단이 즉시 핵심 thesis를 깼고, 2024 OTC·asset-sale-funded debt transaction, 2026 $1 take-private로 이어졌다. deleveraging 방향은 맞았지만 시간·방식·common payoff가 틀렸다.",
        t0="Salem은 116 stations·39 markets, top-25 markets에 73개 station을 보유했다. Q1 2019 normalized broadcast decline은 약 2.2%, average station -1.6%, consolidated adjusted -1%로 주장됐고 Q2 ex-political +1~3% guide가 있었다. entry 약 $2.12, dividend yield 12.5%, cash-flow yield 30%+, target $3.18이었다.",
        reverse="30%+ yield는 distress probability와 cash-flow duration을 반영할 수 있다. 회사는 block programming의 안정성에도 높은 leverage를 지녔고, 1% revenue growth·무현금세금·저가 bond repurchase가 모두 필요했다. 원문이 인정한 zero case의 확률을 target IRR에 명시적으로 반영했어야 한다.",
        valuation="원문은 5배 2020 cash flow에서 $3.18(+50%), 5배 2022에서 +90%, 2023 leverage 4.75배를 제시했다. 하지만 high coupon debt, dividend, capex, bond repurchase를 동시에 수행해야 했다. common value는 EBITDA multiple보다 `FCF after interest - mandatory debt actions`에 민감했다.",
        scenarios=[("Bear", "배당중단·asset sale·distress", "$0~$1", "거의 현실화"), ("Base", "1% 성장·bond discount buyback", "$3.18", "미달"), ("Bull", "digital 성장·4.75x leverage", "+90%", "미실현")],
        actual="2020-05-11 quarterly dividend가 중단돼 12.5% carry thesis가 9개월 만에 무너졌다. 2024 회사는 Nasdaq에서 자진상장폐지했고, 연말 $159.4m notes를 $104m cash+$24m subordinated notes로 교환하며 $37.1m discount를 기록했다. 자금은 $40m preferred와 station transaction에 의존했다. 2026 $1/share WaterStone take-private가 완료됐다.",
        price="표준 DB 가격 series가 없어 exact 1·3년 IRR, MFE·MAE는 계산하지 않는다. 약 $2.12 entry와 2026 $1 deal만 단순 비교하면 배당 제외 -52.8%다. 2019~2020 실제 배당수취와 중간가격을 더한 total return은 자료가 없어 만들지 않는다.",
        drivers="초기에는 block programming, aggressive cost flex와 bond discount purchases가 시간을 벌었다. 그러나 배당은 deleveraging과 경쟁했고 secular decline 속에서 interest coverage가 약해졌다. 최종 debt reduction은 organic FCF가 아니라 asset sale·preferred capital·discount exchange로 이루어져 old common의 upside를 만들지 못했다.",
        counterfactual="배당을 2019부터 전액 중단해 debt를 더 빨리 갚았다면 common terminal value가 $1보다 높아졌을까, 아니면 business decline이 여전히 압도했을까?",
        error="30% cash-flow yield를 zero-risk와 확률가중하지 않았고, 배당·debt repurchase·성장투자를 같은 현금으로 동시에 달성하는 모델을 사용했다.", warning="2020-05-11 배당 suspension이 9개월 내 발생한 직접 반증이다.", first_signal_date="2020-05-11",
        lessons=["고배당 distressed equity는 배당이 아니라 debt covenant와 liquidity waterfall을 먼저 본다.", "zero 가능성을 문장으로만 쓰지 말고 확률가중 IRR에 넣는다.", "할인채 매입은 earning-base 매각과 신규 senior capital을 차감한다."],
        checklist=["dividend coverage", "cash interest", "bond price·maturity", "same-station ex-political", "block renewal", "asset-sale proceeds/EBITDA loss", "preferred terms"],
        scorecard=[("Business thesis", "방어력 일시적"), ("Valuation thesis", "실패"), ("Catalyst thesis", "배당 역전"), ("Timing / path", "실패"), ("Security selection", "common 부적절")],
        claims=[
            C("12.5% dividend yield는 지속", "현금흐름이 quarterly dividend를 충분히 덮는다.", "현금배당이 기다리는 동안 carry를 제공한다.", "T0 payout와 management policy.", "FCF가 interest·capex·dividend를 모두 덮는다.", "배당중단은 직접 반증.", "2020-05-11 dividend suspension.", "게시 약 9개월 후 실패.", "실패", "payout을 residual이 아니라 고정수익처럼 취급했다.", "배당은 debt waterfall 뒤에 둔다."),
            C("cash-flow yield 30%+", "정상화 cash flow 대비 equity가 지나치게 싸다.", "반복 FCF가 debt를 줄이고 주주에게 귀속된다.", "T0 normalization과 no-cash-tax assumption.", "현금세금·interest·capex가 안정적이다.", "FCF가 배당을 중단하거나 asset sale이 필요하면 반증.", "후속 debt 해결은 asset sale·preferred에 의존.", "organic common FCF durability 실패.", "실패", "cash flow 정의와 creditor 우선순위를 흐렸다.", "yield의 분자와 사용처를 명확히 한다."),
            C("block programming은 recession hedge", "40%+ broadcast revenue가 높은 renewal로 안정적이다.", "airtime purchaser가 spot-ad risk를 부담한다.", "원문 revenue mix와 2007~09 cost response.", "renewal과 pricing이 audience erosion을 상쇄한다.", "station disposals·consolidated FCF 약화면 반증.", "일부 방어에도 회사는 stations를 팔아 debt를 해결했다.", "business survival은 했으나 common value 방어 실패.", "부분 실패", "segment 방어를 consolidated solvency로 확장했다.", "stable revenue와 leveraged equity를 분리한다."),
            C("1% revenue growth와 digital이 EBITDA를 안정", "Salem Surround와 Q2 guide가 저성장 회복을 만든다.", "digital cross-sell과 cost discipline이 radio decline을 상쇄한다.", "Q1 normalized decline·Q2 +1~3% guide.", "digital contribution이 legacy decline보다 크다.", "consolidated revenue·EBITDA가 반복 감소하면 반증.", "long-run restructuring과 take-private가 안정가설을 부정했다.", "구조적 offset 불충분.", "실패", "quarterly guide를 multi-year base로 사용했다.", "단기 guide와 secular trend를 분리한다."),
            C("bond buyback이 4.75x leverage로 연결", "low-90s debt 매입과 FCF로 2023 leverage를 낮춘다.", "할인매입이 face debt와 interest를 줄인다.", "T0 bond price와 model.", "영업 FCF가 asset sale 없이 매입재원을 제공한다.", "preferred·asset sale·exchange가 필요하면 실패.", "2024 discount는 컸지만 preferred와 asset transaction으로 실행.", "방향 적중·메커니즘 실패.", "부분 실패", "liability-management source를 낙관했다.", "debt reduction은 organic·asset-funded·court-driven으로 구분한다."),
            C("5배 2020 cash flow로 $3.18", "entry 약 $2.12에서 +50% rerating을 기대한다.", "earnings 안정과 carry가 multiple gap을 닫는다.", "원문 2020 target bridge.", "배당과 FCF가 12개월 유지된다.", "배당중단·가격 target 미달이면 반증.", "2020 배당중단, 2026 $1 exit.", "terminal 단순가격 -52.8%, exact horizon 미복원.", "실패", "tail probability가 target에 반영되지 않았다.", "distressed target은 확률가중 recovery로 계산한다."),
        ],
        metrics=[("Entry / target", "약 $2.12 / $3.18", "+50%", "2026 $1", "장기 -52.8% 배당 제외"), ("Dividend yield", "12.5%", "지속", "2020-05 suspension", "실패"), ("Cash-flow yield", ">30%", "debt+dividend", "asset/preferred-funded restructuring", "실패"), ("2023 leverage", "4.75x", "organic deleveraging", "직접 비교 미복원", "미검증"), ("2024 note discount", "low-90s 매입 기대", "점진적", "$37.1m discount", "방향 적중·방식 다름")],
        timeline=[("2019-08-06", "VIC Long", "$3.18 target"), ("2020-05-11", "dividend suspension", "핵심 carry 반증"), ("2024", "Nasdaq delisting", "liquidity 악화"), ("2024-03", "station-sale plan", "asset-funded deleveraging"), ("2024-12-23", "notes transaction", "$37.1m discount"), ("2026", "$1 take-private", "common terminal failure")], sources=SALM_SOURCES,
    ),
    dict(
        id="58bac334-bf2b-49db-bca8-3a0a981c29f8", date="2002-08-30", author="quentin720", ticker="XMSR", company="XM Satellite Radio",
        filename="analysis/ideas/2002/2002-08-30_XMSR_bond_long.md", source="https://www.valueinvestorsclub.com/idea/XM_Satellite_Radio/1329667940",
        raw_short=True, direction="Long", security="XM 14% senior secured notes / Long", entry="33 cents; escrow coupon strip 후 약 26", horizon="약 3.5년 / exchange·call path", raw_horizon="원문 2005 call 및 3.5년 coupon 분석",
        title="common보다 senior secured notes를 선택해 funding event를 수익원으로 바꾼 distressed Long", verdict="강한 성공 — security selection 적중, exact realized IRR은 경로 의존", score=8.5, process=8.5,
        conclusion="14% secured notes를 33, escrow된 두 coupon을 빼면 약 26에 매수하는 아이디어였다. 2003 exchange는 $1,000 face당 $1,459 maturity principal의 신규 14% secured discount notes, $70 cash, 85 warrants를 제공했고 $300.2m가 참여했다. 2006 XM은 일부 notes를 premium cash로 repurchase/redeem했다. exact IRR은 tender·warrant 매도경로가 없어 계산하지 않지만 payoff 구조는 강하게 적중했다.",
        t0="XM은 가입자 증가 전 막대한 자금이 필요한 위성라디오 startup이었다. $350m 14% senior secured notes와 $125m convert subordinated가 있었고, 원문은 전체 funding need 약 $525m 또는 debt equitization 시 $350m을 추정했다. 두 coupon이 escrow돼 있어 33 price에서 economic at-risk price를 약 26으로 봤다.",
        reverse="기업이 성공해도 common dilution과 추가자금은 불가피했다. 채권 Long의 핵심은 파산회피 그 자체가 아니라 신규자금 제공자가 기존 secured creditor를 어떤 비율로 교환·보호하는지였다. 담보가 약하거나 exchange coercion이 value를 이전하면 26이 싸지 않을 수 있었다.",
        valuation="원문 coupon path는 약 3.5년 동안 49 points와 2005-03 call 107이었다. 더 가능성 높은 debt-to-equity에서 새 $350m이 최대 78%를 가져가도 notes buyer가 implied equity를 싸게 받는다고 봤다. 20m satellite-radio subs의 50%와 XM EBIT $301m·10배=$3bn은 enterprise upside를 설명했지만 bond margin of safety는 seniority와 exchange terms에서 나왔다.",
        scenarios=[("Bear", "funding 실패·low recovery", "26 principal loss", "회피"), ("Base", "secured exchange+new money", "cash·new notes·warrants", "2003 현실화"), ("Bull", "coupon+107 call", "매우 높은 IRR", "일부 premium redemption")],
        actual="2003-01-28 financing에서 $325m old notes 중 $300.2m이 exchange됐다. $1,000 face당 $1,459 maturity principal의 신규 14% secured discount notes(2003-03-15 accreted value $1,000), $70 cash, 85 warrants($3.18 strike)를 받았다. GM obligations $250m도 재구조화했고 $225m gross new money를 조달했다. 2006에는 $148.7m carrying/$186.5m maturity value notes를 $209.6m(이자 포함)에 repurchase/redeem했다.",
        price="표준 채권가격·coupon receipt·warrant sale series가 없어 realized IRR을 단일 숫자로 만들지 않는다. 33 매입, escrow strip 후 26 exposure, 2003 exchange consideration과 2006 premium redemption은 큰 positive payoff를 지지한다. 참여 여부와 warrant 처분일에 따라 투자자별 IRR은 달라진다.",
        drivers="수익의 원천은 위성라디오 subscriber forecast의 정확성보다 secured position과 new-money negotiation이었다. GM restructuring과 $225m 자금조달이 liquidation을 피하게 했고, coercive exchange가 오히려 principal accretion·cash·warrant를 제공했다. common 대신 debt를 산 security selection이 핵심이다.",
        counterfactual="XM common의 dilution이 훨씬 컸더라도 secured-note exchange consideration이 동일했다면 bond thesis는 여전히 성공인가? 그렇다. 두 증권의 payoff를 분리해야 한다.",
        error="20m subs·$301m EBIT·10배 valuation은 매우 낙관적이었고 exact bond IRR을 이를 통해 정당화할 필요가 없었다. 더 강한 논지는 담보·escrow·exchange bargaining만으로 구성할 수 있었다.", warning="반증경보는 new-money가 secured notes보다 선순위로 들어오거나 exchange recovery가 stripped cost 26 아래로 제시되는 것이었다. 실제로는 반대였다.", first_signal_date="2003-01-28",
        lessons=["distress에서는 좋은 회사보다 좋은 security를 찾는다.", "escrow coupon은 purchase price에서 분리해 true capital-at-risk를 계산한다.", "exchange IRR은 각 consideration의 수령일·market value로 계산하고 임의 합산하지 않는다."],
        checklist=["담보범위", "escrow coupon", "new-money seniority", "exchange participation", "warrant strike", "maturity principal/accretion", "call/redemption price"],
        scorecard=[("Business thesis", "생존·합병"), ("Valuation thesis", "채권 payoff 성공"), ("Catalyst thesis", "2003 exchange 성공"), ("Timing / path", "성공"), ("Security selection", "탁월")],
        claims=[
            C("stripped cost 약 26은 recovery 대비 싸다", "33 price에서 두 escrow coupon을 빼면 실질 위험자본은 약 26이다.", "확정 coupon이 초기 cost basis를 회수한다.", "coupon escrow 구조.", "escrow가 bankruptcy remote하고 제때 지급된다.", "escrow 접근불가 또는 recovery 26 미만이면 반증.", "exchange에서 cash·new notes·warrants를 수령.", "회수 package가 stripped cost를 크게 초과한 방향.", "성공", "exact coupon timing IRR은 미복원.", "표면가격과 net-at-risk를 분리한다."),
            C("14% secured seniority가 협상력을 준다", "new money는 secured creditors를 무시하기 어렵다.", "담보·우선순위가 restructuring value allocation을 지킨다.", "14% senior secured status.", "담보가 충분하고 priming이 제한된다.", "무보상 priming이면 반증.", "$300.2m이 유리한 secured exchange에 참여.", "우선순위가 consideration으로 전환.", "성공", "담보 coverage exact appraisal는 부족.", "seniority는 문구가 아니라 recovery waterfall로 검증한다."),
            C("2005 call까지 coupon+107 payoff", "49 points coupon과 107 call이 큰 수익을 만든다.", "funding 후 contractual cash flow가 price discount를 닫는다.", "indenture coupon/call terms.", "회사에 현금이 생겨 notes를 유지·상환한다.", "exchange가 불리하거나 default recovery가 낮으면 반증.", "실제 path는 2003 exchange 후 2006 premium redemption.", "정확한 경로는 달랐지만 premium cash realization.", "부분 성공", "base path와 event path를 혼용했다.", "bond target은 hold·exchange·default 시나리오를 분리한다."),
            C("debt equitization도 upside", "신규 $350m이 78%를 가져가도 notes buyer가 equity를 싸게 받는다.", "낮은 debt price가 post-money equity claim으로 전환된다.", "원문 post-money common $1.5bn vs notes $451m.", "enterprise value가 funding 후 유지된다.", "과도한 dilution·낮은 warrant value면 반증.", "실제 exchange는 new secured notes+cash+warrants였다.", "순수 equity swap보다 더 creditor-friendly.", "성공", "낙관적 enterprise value에 의존했다.", "restructuring security mix를 option별로 가격화한다."),
            C("$225m+ funding이 runway를 만든다", "필요자금 유치로 liquidation을 피한다.", "new money와 GM concession이 cash burn을 견딜 시간을 산다.", "$525m gross need/$350m restructured need 추정.", "OEM support와 capital market access가 유지된다.", "필요자금 부족으로 즉시 filing이면 반증.", "$225m gross new money와 $250m GM obligations restructuring.", "두 축의 funding gap 완화.", "성공", "funding need 추정범위가 넓었다.", "cash runway는 new money와 liability concession을 함께 본다."),
            C("20m 시장·XM 50%가 terminal value를 지지", "XM EBIT $301m·10배=$3bn을 제시했다.", "subscriber scale이 고정 위성비를 흡수한다.", "SAC $100·70% variable margin·1.5% churn model.", "OEM conversion과 churn이 forecast를 따른다.", "가입자 economics 악화·추가자본이 value를 소진하면 약화.", "XM은 생존해 2008 Sirius와 합병했지만 exact forecast 검증은 별개다.", "방향 성공·수치 미검증.", "부분 성공", "enterprise bull case를 bond safety와 섞었다.", "채권 thesis는 terminal equity forecast 없이도 성립해야 한다."),
        ],
        metrics=[("Note price", "33 / stripped 약 26", "recovery 상회", "유리한 exchange·redemption", "성공"), ("Old notes exchanged", "$325m 대상", "높은 참여", "$300.2m", "92.4%"), ("Exchange per $1,000", "equity 가능", "value 보호", "$1,459 maturity principal+$70+85 warrants", "성공"), ("New money", "$225m 필요축", "funding", "$225m gross", "성공"), ("2006 redemption", "107 call 경로", "premium realization", "$186.5m maturity value에 $209.6m incl interest", "성공")],
        timeline=[("2002-08-30", "VIC bond Long", "33·stripped 26"), ("2003-01-28", "financing/exchange", "$300.2m 참여"), ("2003-03-15", "new-note accretion 기준", "$1,000 value"), ("2004~2005", "일부 exchanges", "liability management 지속"), ("2006", "repurchase/redemption", "$209.6m incl interest"), ("2007-02-19", "Sirius merger 발표", "enterprise 생존"), ("2008-07-28", "merger 완료", "산업구조 통합")], sources=XM_SOURCES,
    ),
    dict(
        id="295e4ed3-e95f-44b0-996d-5836165c44ea", date="2006-12-31", author="bode314", ticker="SIRI", company="Sirius Satellite Radio",
        filename="analysis/ideas/2006/2006-12-31_SIRI_short.md", source="", raw_short=True, direction="Short", security="SIRI common equity / Short",
        entry="원문 공개 URL·정확한 가격 미복원", horizon="2007년 guidance·financing", raw_horizon="촉매는 2007년",
        title="가입자 둔화·현금소진을 봤지만 XM merger option을 놓친 common Short", verdict="혼합/실패 — 재무위험 적중, short payoff 미검증·merger가 경로 변경", score=5.0, process=7.0,
        conclusion="가입자 guidance 하향, 월 churn 1.4~1.8%, 연 $600m+ operating loss와 $6bn EV의 긴장을 지적한 것은 타당했다. 그러나 2007 subscriber revenue는 49% 성장했고 2007-02 XM 합병 발표가 standalone insolvency path를 바꿨다. 2009 Liberty rescue는 funding risk를 확인했지만 exact short return은 없어 승리로 소급하지 않는다.",
        t0="Sirius는 2006 subscriber guidance를 6.3m에서 5.9~6.1m으로 낮췄고 net adds가 둔화됐다. Q3 revenue $167.1m, gross profit $102.3m, operating expense $204.1m, EBIT -$101.8m이었다. 원문은 EV 약 $6bn·subscriber당 약 $1,000, 10m subs에서도 $670/sub를 문제 삼았다.",
        reverse="시장은 현재 손실이 아니라 높은 fixed-cost platform의 미래 scale과 XM 결합 가능성을 살 수 있었다. Short가 성공하려면 2007 CFFO break-even 실패와 추가 financing이 dilution 또는 distress로 직결되고, merger/strategic capital이 그 tail을 막지 않아야 했다.",
        valuation="원문은 10m subs에서도 EV/sub $670이며 10배 valuation을 지지하려면 subscriber당 EBITDA $67이 필요하다고 계산했다. 이는 유용한 reverse DCF지만, fixed satellite/content cost와 merger synergies가 subscriber당 economics를 크게 바꿀 수 있었다. Howard Stern 계약 $500m/5년을 단순 비용으로만 보지 않고 acquisition value와 retention을 함께 봐야 했다.",
        scenarios=[("Bear for short", "XM merger·subscriber scale", "short squeeze/손실", "2007 발표"), ("Base", "guidance miss·financing", "valuation 압축", "risk는 적중"), ("Bull for short", "현금고갈·독자 distress", "큰 하락", "2009 rescue까지 지연")],
        actual="2007 subscriber revenue는 subscriber 38% 증가에 힘입어 49% 늘었다. Sirius와 XM은 2007-02-19 합병을 발표했고 2008-07-28 완료했다. 2009에는 Liberty로부터 최대 $530m을 빌려 near-term liquidity를 확보했고 같은 해 이를 상환했다. 독자기업 funding risk는 실제였지만 merger·strategic capital이 terminal outcome을 바꿨다.",
        price="게시일 공개 URL과 표준 가격 series가 없어 short entry·cover·borrow cost·MFE·MAE·IRR을 계산하지 않는다. 2009 rescue가 있었다는 사실을 2007 short profit으로 간주하지 않는다. short 판정은 2007 subscriber growth와 merger announcement 때문에 혼합/실패 쪽으로 둔다.",
        drivers="맞은 것은 standalone cash burn과 추가자금 필요였다. 틀린 것은 Howard Stern·content spending의 subscriber acquisition 효과와 XM merger option을 충분히 가격화하지 않은 점이다. Short security는 timing과 strategic event에 취약했고, eventual funding stress가 즉시 수익을 보장하지 않았다.",
        counterfactual="XM merger가 발표되지 않고 2007 subscriber revenue가 49% 성장했다면 cash burn alone이 언제 short payoff로 전환됐을까?",
        error="standalone EV/subscriber와 손실 run-rate를 정적 사용했고 merger synergy·strategic financing이라는 path dependency를 작게 뒀다.", warning="2007-02-19 XM merger 발표가 thesis를 즉시 재평가해야 할 첫 사건이었다.", first_signal_date="2007-02-19",
        lessons=["플랫폼 short는 cash burn뿐 아니라 strategic buyer·merger option을 명시적으로 가격화한다.", "EV/subscriber는 incremental margin과 fixed-cost absorption을 함께 본다.", "eventual distress는 entry-to-cover short IRR을 대체하지 않는다."],
        checklist=["net adds·churn", "trial conversion", "SAC", "monthly cash burn", "liquidity runway", "merger probability", "borrow cost·cover rule"],
        scorecard=[("Business thesis", "standalone risk 적중"), ("Valuation thesis", "비싸다는 지적 부분"), ("Catalyst thesis", "merger로 경로 변경"), ("Timing / path", "실패/미검증"), ("Security selection", "common Short 취약")],
        claims=[
            C("subscriber growth는 둔화", "guidance 6.3m→5.9~6.1m과 net adds 둔화가 수요약화를 보인다.", "가입자 부족이 fixed cost absorption을 늦춘다.", "2006 revised guidance·1.4~1.8% monthly churn.", "guidance miss가 2007에도 이어진다.", "subscriber·revenue growth가 재가속하면 반증.", "2007 subscriber +38%, subscriber revenue +49%.", "방향이 반대로 전개.", "실패", "한 차례 guidance cut을 trend로 고정했다.", "subscriber thesis는 cohort·churn·gross adds로 갱신한다."),
            C("Howard Stern economics는 부정적", "약 1.5m subs/$200m revenue 대비 $500m/5년 contract가 과도하다.", "content cost가 contribution을 흡수한다.", "원문 subscriber attribution 추정.", "incremental retention·brand spillover가 작다.", "subscriber/revenue growth가 content spend를 정당화하면 약화.", "2007 높은 subscriber/revenue 성장과 merger scale이 나타났다.", "계약의 완전한 unit economics는 미복원.", "미검증/부분 실패", "direct subs만 세고 churn·brand option을 누락했다.", "content ROI는 acquisition+retention+ad revenue로 본다."),
            C("연 $600m+ loss는 financing을 강제", "Q3 EBIT -$101.8m과 높은 cash burn이 추가자금을 요구한다.", "현금소진이 dilution·high-cost debt·distress를 만든다.", "Q3 2006 P&L과 원문 annualization.", "operating leverage가 funding 전에 충분히 개선되지 않는다.", "strategic capital·merger가 runway를 연장하면 timing 반증.", "2009 Liberty rescue가 필요했지만 merger가 2007 발표됐다.", "risk 적중·short timing 지연.", "부분 성공", "필요자금과 주가촉매 날짜를 동일시했다.", "cash runway에는 strategic funding scenario를 둔다."),
            C("EV $6bn/$1,000 per sub는 과대", "10m subs에서도 $670/sub로 높은 기대를 반영한다.", "필요 EBITDA/sub가 현실 unit economics를 넘으면 multiple이 압축된다.", "원문 EV/sub reverse valuation.", "incremental margin이 충분히 높지 않다.", "합병 synergy와 scale로 EBITDA margin이 크게 오르면 반증.", "2017~2018 합병회사의 EBITDA/FCF scale은 강해졌다.", "장기 operating leverage가 valuation critique를 약화.", "부분 실패", "static unit metric에 fixed-cost leverage를 누락했다.", "subscriber multiple은 mature contribution으로 환산한다."),
            C("iPod·WiMAX가 차량 moat를 침식", "portable·in-car internet가 paid satellite value를 낮춘다.", "대체재가 listening time과 willingness-to-pay를 가져간다.", "2006 device/technology landscape.", "차량 connectivity가 빠르게 보급된다.", "OEM funnel과 exclusive content가 subs를 계속 늘리면 timing 실패.", "단기에는 subscriber 성장·합병이 우세했고 장기 경쟁은 늦게 나타났다.", "방향은 맞고 horizon이 길었다.", "지연된 성공", "technology adoption curve를 촉매로 과속했다.", "secular short에는 adoption milestone을 둔다."),
            C("2007 financing/guidance가 short catalyst", "CFFO break-even 실패와 H2 financing이 valuation을 깬다.", "현금필요가 equity dilution 우려로 가격에 반영된다.", "원문 2007 catalyst list.", "XM deal이 standalone financing event를 대체하지 않는다.", "merger 발표·revenue growth면 catalyst 무효.", "2007-02 merger 발표, 2007 subscriber revenue +49%.", "촉매가 반대 전략이벤트에 덮였다.", "실패", "event tree를 단일 downside path로 봤다.", "catalyst calendar에는 positive optionality도 넣는다."),
        ],
        metrics=[("2006 subscriber guide", "6.3m→5.9~6.1m", "추가 하향", "2007 subscriber +38%", "실패"), ("Monthly churn", "1.4~1.8%", "악화", "정확한 후속 비교 미복원", "미검증"), ("Q3 EBIT", "-$101.8m", "cash burn", "2009 strategic rescue", "위험 적중"), ("EV/sub", "약 $1,000", "압축", "장기 scale economics 개선", "부분 실패"), ("Merger", "미반영", "없음", "2007-02 발표·2008-07 완료", "short 반증")],
        timeline=[("2006-12-31", "VIC Short", "guidance·cash burn"), ("2007-02-19", "XM merger 발표", "첫 반증"), ("2007-12-31", "subscriber revenue +49%", "영업방향 반대"), ("2008-07-28", "merger 완료", "scale·synergy option"), ("2009-02", "Liberty financing", "standalone risk 확인"), ("2009", "Liberty loan 상환", "즉시 insolvency 회피")], sources=SIRI_SOURCES,
    ),
    dict(
        id="54fa011e-c658-4352-87fa-c1eb711a6eeb", date="2013-02-25", author="jon64", ticker="SIRI", company="Sirius XM Radio",
        filename="analysis/ideas/2013/2013-02-25_SIRI_long.md", source="https://www.valueinvestorsclub.com/idea/SIRIUS_XM_RADIO_INC/2030431118",
        raw_short=True, direction="Long", security="SIRI common equity / Long", entry="원문 정확한 가격 미복원; 25x 2013 normalized FCF", horizon="2013~2016", raw_horizon="원문 4년 cash/buyback model",
        title="차량 funnel·고정비 leverage·대형 buyback을 정확히 본 satellite-radio Long", verdict="중기 사업·capital allocation 성공 — exact equity IRR 미검증", score=8.0, process=8.0,
        conclusion="23.9m subs, 45% trial conversion, 약 2% churn, used-car funnel과 35% fixed-cost leverage를 근거로 큰 FCF·buyback을 예상했다. 2016 revenue $5.0bn, EBITDA $1.88bn, FCF $1.51bn과 2017 FCF $1.56bn, 2021 $18bn buyback authorization은 방향을 강하게 확인한다. 다만 10% subscriber CAGR은 과대였고 exact 주가 IRR은 없다.",
        t0="Sirius XM은 합병 후 23.9m subscribers와 사실상 전국 위성라디오 단일 플랫폼을 보유했고 Liberty가 majority holder였다. new-car trials의 약 45% conversion, churn 약 2%, 가격 5% 인상 뒤 유지된 demand, 2012 used-car 1m 신규 subs와 확대되는 dealer network가 핵심이었다.",
        reverse="25배 2013 normalized FCF는 이미 상당한 성장과 capital return을 가격에 넣었다. Long이 맞으려면 10% subscriber growth 또는 그에 준하는 ARPU·margin expansion, no-cash-tax와 낮은 satellite capex, 수십억 buyback의 적정가격 집행이 필요했다. 한 축의 miss를 다른 축이 보완할 수는 있었다.",
        valuation="원문은 2016까지 약 $6.7bn cash generation, 초기 $2bn buyback과 3.5배 re-levering을 통해 4년간 $10bn+ repurchase 가능성을 제시했다. 25배 normalized FCF는 싸지 않았으므로 return은 FCF/share 성장에 의존했다. buyback은 authorization이 아니라 실제 share count와 평균가격·debt 증가로 평가해야 한다.",
        scenarios=[("Bear", "conversion 하락·capex·multiple 압축", "높은 시작배수 손실", "단기 미현실화"), ("Base", "중한 자릿수 subs·margin expansion", "FCF/share 성장", "대체로 적중"), ("Bull", "10% subs CAGR·$10bn+ buyback", "큰 rerating", "가입자 성장 미달·buyback 방향 적중")],
        actual="2016 revenue $5.0bn, adjusted EBITDA $1.88bn, FCF $1.51bn; 2017 EBITDA $2.12bn, FCF $1.56bn이었다. 2018 Q3 adjusted EBITDA margin은 40%를 넘었다. Buyback authorization은 2021까지 $18bn으로 확대됐다. 2019 Pandora를 인수했다. subscribers는 2021 약 34m에 이르렀지만 2025 32.9m, 2024 self-pay -296k, 2025 -301k로 뒤늦게 감소했다. 2025 FCF는 $1.256bn이었다.",
        price="원 DB에 이 아이디어의 event-date price series가 없어 2013~2016 total return·MFE·MAE·IRR은 계산하지 않는다. 사업 KPI와 capital return은 중기 논지를 강하게 지지하지만, 이를 특정 equity return 숫자로 치환하지 않는다. Liberty 구조와 later corporate actions도 단순 가격비교를 어렵게 한다.",
        drivers="중기 value creation은 OEM-installed base, used-car reactivation, low churn과 높은 fixed-cost absorption이 만들었다. NOL과 satellite capex holiday가 FCF를 키웠고 buyback이 share-level exposure를 높였다. 다만 10% subscriber growth와 무제한 duration은 과했고 Pandora 인수는 pure buyback thesis의 일부 현금을 전환했다.",
        counterfactual="가입자가 2016 이후 정체했어도 ARPU·margin과 buyback만으로 25배 시작 valuation을 정당화할 수 있었는가?",
        error="subscriber CAGR을 너무 높게 잡고, re-levered buyback의 평균매입가격과 debt downside를 충분히 stress하지 않았다. Pandora 같은 재투자 option도 초기 capital allocation map에 없었다.", warning="10% subscriber CAGR보다 실제 성장률이 낮아지는 시점이 첫 모델 경고였고, 2024 self-pay 감소가 장기 duration 반증을 명확히 했다.", first_signal_date="2016-12-31",
        lessons=["높은 시작배수 Long은 subscriber·ARPU·margin·buyback의 FCF/share bridge로 판정한다.", "buyback authorization과 realized accretion을 분리한다.", "중기 thesis 성공과 장기 secular decline은 동시에 참일 수 있다."],
        checklist=["self-pay net adds", "trial conversion", "churn", "ARPU", "EBITDA margin", "satellite capex", "buyback average price·net leverage"],
        scorecard=[("Business thesis", "중기 성공"), ("Valuation thesis", "높은 배수 감당"), ("Catalyst thesis", "buyback 성공"), ("Timing / path", "성공"), ("Security selection", "Long 적절")],
        claims=[
            C("subscriber 10% 성장", "new·used car funnel로 5년간 약 10% 성장한다.", "OEM trial과 used-car reactivation이 gross adds를 만든다.", "23.9m subs·45% conversion·dealer 확대.", "churn 2% 부근과 conversion이 유지된다.", "성장률이 중한 자릿수 아래로 내려가면 target 수정.", "2021 약 34m으로 증가했으나 10% CAGR에는 미달; 2025 32.9m.", "방향 적중·속도 과대.", "부분 성공", "used-car funnel의 포화와 cohort 차이를 작게 봤다.", "가입자 bridge를 installed base·conversion·churn으로 나눈다."),
            C("used-car subscriber는 고마진", "OEM subsidy 없는 used-car conversion이 margin을 높인다.", "이미 설치된 receiver를 재활성화해 SAC를 낮춘다.", "2012 used-car 1m adds·dealer network 확대.", "used-car conversion과 retention이 new-car보다 충분히 좋다.", "SAC·churn 악화로 contribution이 낮으면 반증.", "중기 subscriber·margin expansion이 관찰됐다.", "segment별 exact unit economics는 미복원.", "부분 성공", "공시되지 않은 cohort margin을 확정했다.", "used-car LTV/CAC를 별도 추적한다."),
            C("35% fixed-cost leverage가 margin 확대", "subscriber growth가 revenue보다 EBITDA를 빠르게 늘린다.", "위성·content fixed cost가 더 큰 base에 분산된다.", "T0 fixed-cost share 약 35%.", "royalty·content variable cost가 leverage를 상쇄하지 않는다.", "EBITDA margin이 정체하면 반증.", "2016 EBITDA $1.88bn, 2017 $2.12bn; 2018 Q3 margin 40%+.", "강한 margin expansion.", "성공", "장기 royalty·content 재가격 위험은 남았다.", "fixed-cost thesis는 incremental margin으로 검증한다."),
            C("NOL·capex holiday가 FCF를 키움", "$7.6bn NOL과 2017 전 낮은 satellite capex가 cash conversion을 높인다.", "cash tax·growth capex 지연이 EBITDA를 FCF로 바꾼다.", "T0 NOL·satellite schedule.", "세법·launch schedule이 유지된다.", "cash tax·satellite capex가 조기 급증하면 반증.", "2016 FCF $1.51bn, 2017 $1.56bn.", "FCF scale 확인.", "성공", "일시적 tax/capex benefit을 terminal로 볼 위험.", "temporary cash benefits에는 expiry를 붙인다."),
            C("$10bn+ buyback이 주당가치를 높임", "2016까지 cash generation과 3.5x leverage로 대규모 repurchase가 가능하다.", "intrinsic value 아래 share retirement가 FCF/share를 높인다.", "초기 $2bn authorization·Liberty control.", "매입가격과 추가 debt가 합리적이다.", "비싼 매입·leverage 상승·M&A 전환이면 accretion 약화.", "authorization은 2021 $18bn으로 확대; 2019 Pandora 인수도 실행.", "규모 방향 초과·quality는 가격/주식수 bridge 필요.", "성공/부분", "authorization을 곧 realized IRR로 봤다.", "buyback은 가격·shares retired·net debt로 평가한다."),
            C("25x normalized FCF를 성장으로 소화", "높은 multiple에도 FCF/share 복리가 valuation을 정당화한다.", "margin·tax·capex·buyback이 분모를 빠르게 키운다.", "원문 normalized FCF valuation.", "사업·capital allocation이 동시에 작동한다.", "FCF 정체와 subscriber decline이면 multiple risk.", "중기 FCF $1.5bn+로 성공; 2024~25 self-pay 감소·2025 FCF $1.256bn.", "중기 적중·장기 duration 약화.", "부분 성공", "terminal duration을 과대평가했다.", "높은 배수는 명시적 fade curve로 검증한다."),
        ],
        metrics=[("Subscribers", "23.9m", "5년 10% 성장", "2021 약 34m·2025 32.9m", "속도 미달"), ("2016 revenue", "성장", "미래 scale", "$5.0bn", "성공"), ("2016 FCF", "$6.7bn 누적모델", "강한 cash", "$1.51bn", "성공"), ("2017 EBITDA/FCF", "margin leverage", "상승", "$2.12bn/$1.56bn", "성공"), ("Buyback authorization", "$2bn 시작", "$10bn+ 가능", "2021 $18bn", "방향 강한 성공")],
        timeline=[("2013-02-25", "VIC Long", "25x FCF·used-car·buyback"), ("2016-12-31", "revenue $5.0bn·FCF $1.51bn", "cash engine 확인"), ("2017-12-31", "EBITDA $2.12bn·FCF $1.56bn", "margin thesis 성공"), ("2018-Q3", "EBITDA margin 40%+", "fixed-cost leverage"), ("2019-02-01", "Pandora 인수 완료", "capital allocation 확장"), ("2021", "subs 약 34m·buyback authorization $18bn", "중기 성공"), ("2024~2025", "self-pay 순감소", "장기 duration 경고"), ("2025", "FCF $1.256bn", "성숙기 cash 유지")], sources=SIRI_SOURCES,
    ),
    dict(
        id="9013631b-6397-4414-9f1b-3e88ce11771f", date="2017-04-25", author="Flaum", ticker="SIRI", company="Sirius XM Holdings",
        filename="analysis/ideas/2017/2017-04-25_SIRI_short.md", source="https://www.valueinvestorsclub.com/idea/SIRIUS_XM_HOLDINGS_INC/7836075076",
        raw_short=True, direction="Short", security="SIRI common equity / Short", entry="원문 context 약 $5대; exact 미확정", horizon="24개월", raw_horizon="원문 target $2.50 / 24개월",
        title="royalty와 connected-car 위협은 맞았지만 24개월 operating leverage를 이기지 못한 Short", verdict="24개월 실패 — catalyst 일부 적중, 구조적 약화는 늦게 발생", score=4.5, process=8.0,
        conclusion="CRB royalty 상승과 connected-car 경쟁이라는 방향은 맞았고 2018~2022 royalty rate는 15.5%로 결정됐다. 그러나 2017 EBITDA $2.12bn·FCF $1.56bn, 2018 net adds와 40%+ margin이 단기 earnings를 지지했고 $2.50 target의 24개월 Short는 실패한 것으로 판단한다. self-pay decline은 2024~25에야 뚜렷해졌다.",
        t0="Sirius XM은 약 $25bn market cap, 3.5% fully taxed FCF yield, 약 15배 EBITDA로 평가됐다. connected car·CarPlay·Android와 월 $10 이하 streaming이 $16~19 list price를 위협하고, royalty 10~11%에서 SoundExchange 요구 23%, trial penetration 75% 하락, 두 위성 capex와 NOL 종료가 겹친다는 Short였다.",
        reverse="높은 valuation은 전국 독점적 차량 distribution, low churn, price power와 70% contribution margin을 반영했다. Short가 맞으려면 royalty 결정이 earnings를 크게 훼손하고 trial/conversion 하락이 net adds를 꺾으며 capex·tax가 FCF를 동시에 낮춰야 했다. structural threat의 방향만으로 24개월 timing은 나오지 않는다.",
        valuation="원문은 consensus revenue/EBITDA CAGR 5%/7.5% to 2020에 비해 3.5% FCF yield·15배 EBITDA가 과도하다고 봤고 24개월 $2.50 target을 제시했다. 하지만 70% contribution margin과 buyback은 소폭 revenue growth도 FCF/share growth로 만들 수 있다. Short valuation은 terminal multiple뿐 아니라 8개 분기 earnings path를 필요로 했다.",
        scenarios=[("Bear for short", "15.5% royalty·margin/FCF 성장", "short 손실", "2017~2018 현실화"), ("Base", "net adds 둔화·valuation 압축", "완만한 하락", "24개월 미실현"), ("Bull for short", "23% royalty·connected-car churn", "$2.50", "미실현")],
        actual="CRB는 2018~2022 SDARS royalty를 15.5%로 정해 방향은 맞았지만 23% extreme보다 낮았다. 2017 EBITDA는 $2.12bn(+13%), FCF $1.56bn이었다. 2018 Q2 self-pay net adds 483k, revenue +6%, net income +45%, FCF +17%; Q3 EBITDA margin은 40%를 넘었다. 2019 Pandora를 인수했고 self-pay 감소는 2024 -296k, 2025 -301k로 늦게 나타났다.",
        price="원 DB에 정확한 short entry·24개월 price series·borrow cost가 없어 IRR·MFE·MAE를 계산하지 않는다. 다만 24개월 안의 영업 KPI와 Pandora 인수는 $2.50 downside path보다 강했다. 구조적 경쟁이 7~8년 뒤 확인된 사실은 원래 24개월 short 성공을 소급해 만들지 않는다.",
        drivers="Short 손실을 만든 것은 강한 installed base, contribution margin, price power와 buyback이었다. royalty 상승은 earnings를 일부 낮췄지만 극단치보다 낮았고, connected-car 경쟁은 churn을 즉시 폭발시키지 않았다. Pandora 인수는 defensive response였지만 동시에 short catalyst를 뒤로 밀었다.",
        counterfactual="royalty가 15.5%로 오르더라도 EBITDA가 두 자릿수 성장하고 self-pay adds가 양수라면 valuation short는 어떤 분기 KPI에서 cover했어야 하는가?",
        error="정확한 secular direction을 short horizon과 혼동했다. 23% request를 base-case outcome처럼 사용했고 high incremental margin의 단기 earnings cushion을 과소평가했다.", warning="2017 full-year EBITDA +13%와 2018 Q2 FCF +17%가 24개월 thesis를 재평가할 첫 직접 경고였다.", first_signal_date="2018-01-31",
        lessons=["secular short에는 방향뿐 아니라 8개 분기 내 earnings inflection이 필요하다.", "규제청구액과 최종결정 확률분포를 분리한다.", "늦게 맞은 산업통찰은 원래 short IRR을 구제하지 않는다."],
        checklist=["self-pay adds", "trial penetration·conversion", "churn", "royalty rate", "incremental margin", "satellite capex·cash tax", "borrow cost·cover rule"],
        scorecard=[("Business thesis", "장기 방향 일부"), ("Valuation thesis", "24개월 실패"), ("Catalyst thesis", "royalty 일부 적중"), ("Timing / path", "실패"), ("Security selection", "Short 부적절")],
        claims=[
            C("connected car가 subscription을 대체", "CarPlay·Android·streaming이 $16~19 satellite plan을 압박한다.", "차량 내 선택지 증가가 conversion과 churn을 악화한다.", "2017 connected-car adoption.", "embedded connectivity가 빠르게 보급되고 switching friction이 낮다.", "self-pay adds·ARPU·churn이 24개월 견조하면 timing 반증.", "2018 Q2 self-pay adds 483k, revenue +6%.", "24개월 수요붕괴가 나타나지 않음.", "실패/지연", "기술가용성과 소비자전환을 동일시했다.", "adoption funnel을 penetration·usage·cancellation로 나눈다."),
            C("trial penetration 75% 하락이 funnel을 꺾음", "90%대에서 75%로 떨어져 gross trials가 감소한다.", "신차 trial 수가 줄면 conversion pool이 작아진다.", "T0 OEM penetration trend.", "used-car reactivation이 gap을 메우지 못한다.", "self-pay net adds가 계속 양수면 반증.", "2018 Q2 483k self-pay net adds.", "funnel은 단기 유지.", "실패", "trial penetration 하나로 total gross adds를 설명했다.", "new·used·win-back funnel을 합산한다."),
            C("royalty가 15~23%로 상승", "10~11%에서 크게 올라 earnings를 최대 두 자릿수 훼손한다.", "revenue-based royalty가 높은 contribution margin을 직접 깎는다.", "SoundExchange 23% request·CRB calendar.", "회사가 가격·비용으로 상쇄하지 못한다.", "최종 rate가 낮거나 EBITDA 성장으로 흡수되면 payoff 약화.", "최종 15.5%; 2017 EBITDA +13%, 2018 margin 40%+.", "방향 적중·극단치 미달·흡수 성공.", "부분 성공", "청구액을 expected value로 사용했다.", "규제 outcome은 확률가중하고 mitigation을 모델링한다."),
            C("satellite capex·NOL 종료가 FCF를 압박", "두 위성 지출과 cash tax가 3.5% FCF yield를 약화한다.", "temporary cash holiday 종료가 owner earnings를 낮춘다.", "T0 satellite schedule·NOL estimate.", "EBITDA growth가 현금부담보다 작다.", "FCF가 24개월 성장하면 반증.", "2017 FCF $1.56bn, 2018 Q2 FCF +17%.", "초기 FCF 압박 미현실화.", "실패/지연", "capex timing과 cash payment schedule을 거칠게 처리했다.", "FCF catalyst는 분기별 cash schedule로 만든다."),
            C("15배 EBITDA·3.5% FCF yield는 과대", "5% revenue·7.5% EBITDA growth에 valuation이 높다.", "성장 둔화와 비용상승이 multiple compression을 만든다.", "T0 market cap 약 $25bn·consensus.", "earnings beat와 buyback이 valuation을 지지하지 못한다.", "EBITDA·FCF가 두 자릿수 성장하면 short를 재검토.", "2017 EBITDA +13%, 2018 Q2 FCF +17%.", "핵심 near-term falsifier 충족.", "실패", "valuation mean reversion보다 earnings momentum이 강했다.", "multiple short는 estimate-revision path를 우선한다."),
            C("24개월 $2.50 target", "royalty·competition·capex가 결합해 큰 downside를 만든다.", "earnings miss와 multiple compression이 동시에 발생한다.", "원문 target·event calendar.", "여섯 촉매가 8분기 안에 정렬된다.", "영업 KPI가 개선되고 defensive M&A가 실행되면 실패.", "2017~2018 KPI 강세, 2019-02 Pandora completion.", "target 경로를 지지하지 않음; exact return 미복원.", "실패", "지연 가능한 structural factors를 동시조건으로 묶었다.", "short target은 촉매별 날짜·확률·cover rule을 둔다."),
        ],
        metrics=[("CRB royalty", "10~11%; request 23%", "15~23%", "15.5%", "방향 적중"), ("2017 EBITDA", "둔화 기대", "pressure", "$2.12bn / +13%", "실패"), ("2017 FCF", "3.5% yield pressure", "감소", "$1.56bn", "실패"), ("2018 Q2 self-pay adds", "funnel 약화", "감소", "483k", "실패"), ("2018 Q2 FCF", "압박", "감소", "+17% YoY", "실패")],
        timeline=[("2017-04-25", "VIC Short", "$2.50/24개월"), ("2017-12", "CRB 15.5% 결정", "촉매 일부 적중"), ("2017-12-31", "EBITDA $2.12bn·FCF $1.56bn", "영업 반증"), ("2018-Q2", "483k self-pay adds·FCF +17%", "short path 실패"), ("2018-Q3", "EBITDA margin 40%+", "operating leverage"), ("2019-02-01", "Pandora 인수 완료", "defensive expansion"), ("2024", "self-pay -296k", "지연된 구조약화"), ("2025", "self-pay -301k", "장기 방향 확인")], sources=SIRI_SOURCES,
    ),
]


RAW_META = {
    "cdd1ef14-3122-41eb-8f8d-da184b6b6add": (14682, 314, None),
    "23194b96-65fc-46b4-9b03-7fb4033d4e37": (0, 0, {"open": 12.6072, "close": 12.9501, "1m": 0.9723168160863622, "3m": 1.2848472212569786, "6m": 1.344020509494135, "1y": 1.4161821144238267, "2y": 1.8774217959706874, "3y": 2.628798233218276, "5y": 2.3037042185002434}),
    "e40ec74c-12db-460c-bab8-c7c4435c1d90": (38678, 9, {"open": 23.5867, "close": 23.989, "1m": 1.065413314435783, "3m": 1.0647630163825086, "6m": 1.0857684772187253, "1y": 0.8175663845929384, "2y": 0.892275626328734, "3y": 1.0958064112718329, "5y": None}),
    "8f8b9173-3403-4002-abd0-203cc4c71935": (15145, 84, {"open": 21.5556, "close": 21.5187, "1m": 1.0295742772565257, "3m": 1.0618671202256642, "6m": 1.1074089048130231, "1y": None, "2y": None, "3y": None, "5y": None}),
    "4e88007a-5df8-4dbb-be00-cb635445aae3": (5467, 108, None),
    "a9f7338b-17a2-4aa2-99dc-1419d2b4d652": (10846, 606, None),
    "58bac334-bf2b-49db-bca8-3a0a981c29f8": (9235, 191, None),
    "295e4ed3-e95f-44b0-996d-5836165c44ea": (9596, 270, None),
    "54fa011e-c658-4352-87fa-c1eb711a6eeb": (9705, 0, None),
    "9013631b-6397-4414-9f1b-3e88ce11771f": (16369, 803, None),
}


def render_report(i):
    raw_direction = "Short" if i["raw_short"] else "Long"
    lines = [
        f"# {i['company']} ({i['ticker']}) — {i['date']} VIC {i['direction']}", "",
        "> **Idea unit:** 이 게시일의 증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.",
        f"> **Research as-of:** {ASOF}. 사업·valuation·촉매·증권·가격경로를 분리하고 사후정보는 판정에만 사용한다.",
        "", "---", "", "## 0. Idea Snapshot", "", "| 항목 | 내용 |", "|---|---|",
        f"| 회사 / Ticker | {i['company']} / {i['ticker']} |",
        f"| VIC 게시일 / 작성자 | {i['date']} / {i['author']} |",
        f"| 분석 증권 / 실제 방향 | {i['security']} |",
        f"| 원 SQL 방향 | {raw_direction} — raw 값 보존, research direction은 별도 교정 |",
        f"| 기준 진입가격 | {i['entry']} |", f"| 기대기간 | {i['horizon']} |",
        f"| raw horizon audit | {i['raw_horizon']} |", f"| 최종 판정 | **{i['verdict']}** |", "",
        f"> **결론:** {i['conclusion']}", "", "---", "", "## 1. 회사는 정확히 무엇을 하는가", "",
        BUSINESS[i["ticker"]], "", ENGINE[i["ticker"]], "", "### 가치사슬과 security payoff", "",
        "청취자·차량 OEM·광고주 또는 가입자가 만든 gross economics가 station/platform 비용, royalty·content, corporate cost, cash interest, capex, tax를 통과한 뒤 common에 귀속된다. 채권 아이디어는 여기에 담보·seniority·exchange consideration·recovery를 적용한다. 매출 성장, enterprise value 증가, 해당 security 수익을 같은 사건으로 취급하지 않는다.",
        "", "### 매 분기 볼 핵심 KPI", "", KPI[i["ticker"]], "", "---", "",
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
    lines += ["---", "", "## 4. 당시 Valuation과 Payoff Structure", "", i["valuation"], "", "### 시나리오 분석", "", "| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |", "|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scenarios"]]
    lines += ["", "### 핵심 수치", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["metrics"]]
    lines += [
        "", "### 촉매와 시간", "", f"판정 horizon은 **{i['horizon']}**다. 이후 사건은 장기 사업가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.",
        "", "---", "", "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "", "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|",
    ]
    lines += ["| " + " | ".join(row) + " |" for row in i["timeline"]]
    lines += [
        "", "### 실제 사업·자본구조 추이", "", i["actual"], "", "---", "",
        "## 6. 실제 투자결과 — 가격 경로와 실현 가능성", "", i["price"], "",
        "가격 series는 배당·세금·거래비용을 포함한 total return과 분리한다. 데이터가 없으면 수익률·MFE·MAE를 추정하지 않는다. Short는 entry·cover·borrow, bond는 coupon·exchange·warrant 수령일이 있어야 exact IRR을 계산한다.",
        "", "---", "", "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 핵심 gap |", "|---|---|---:|---|---|",
    ]
    for n, (c, weight) in enumerate(zip(i["claims"], WEIGHTS), 1):
        lines.append(f"| C{n} | {c['title']} | {weight}% | {c['verdict']} | {c['gap']} |")
    lines += [
        "", "---", "", "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", i["drivers"], "",
        "### What was right / What was wrong", "", f"**맞았던 것:** {i['scorecard'][0][1]}와 관련된 관찰은 유효했다. **틀렸던 것:** {i['error']}", "",
        "### Counterfactual", "", i["counterfactual"], "", "---", "", "## 9. 분석 오류 유형과 최초 경고", "", i["error"], "",
        "### 최초로 관찰 가능했던 경고신호", "", i["warning"], "", "---", "", "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", "",
    ]
    for n, lesson in enumerate(i["lessons"], 1):
        lines += [f"### Lesson {n}", "", lesson, ""]
    lines += ["### 지금 같은 아이디어를 다시 본다면", ""] + [f"- {x}" for x in i["checklist"]]
    lines += ["", "---", "", "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|"]
    lines += ["| " + " | ".join(row) + " |" for row in i["scorecard"]]
    lines += [f"| Thesis score | {i['score']:.1f}/10 |", f"| Process score | {i['process']:.1f}/10 |", f"| 종합 | **{i['verdict']}** |", "", "### 한 문장 교훈", "", f"> {i['lessons'][0]}", "", "---", "", "## 12. Sources / Validation Notes", ""]
    for n, source in enumerate(idea_sources(i), 1):
        if source["url"]:
            lines.append(f"{n}. [{source['title']}]({source['url']}) — {source['publisher']}, {source['date']}. {source['evidence']}")
        else:
            lines.append(f"{n}. {source['title']} — {source['publisher']}, {source['date']}. {source['evidence']}")
    lines += [
        "", "### 데이터 품질", "",
        "- T0 원문·metadata: **A/B** — source SQL과 공개 VIC URL을 기준으로 했다. SGA 2010은 body가 없어 claim reconstruction을 명시적으로 낮은 신뢰도로 처리했다.",
        "- 사업·거래·자본구조: **A** — SEC·회사·CRB·FCC 1차자료를 우선했다.",
        "- 가격경로: **B/C 또는 미검증** — 원 DB가 보존한 SGA ratio만 수치화했다. 배당 포함 여부가 불명확해 현금배당을 중복 가산하지 않았다.",
        f"- raw SQL direction은 **{raw_direction}**, 본문 실제 research direction은 **{i['direction']}**다. 둘을 덮어쓰지 않고 나란히 보존했다.", "",
    ]
    return "\n".join(lines)


def make_payload(ideas):
    out = {
        "schema_version": "vic-deep-research-v9", "batch": 42,
        "title": "Radio / Satellite Audio — Cumulus, Saga, Salem, XM, Sirius V9", "research_asof": ASOF,
        **{key: [] for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")},
    }
    for i in ideas:
        desc_chars, catalyst_chars, perf = RAW_META[i["id"]]
        perf = perf or {}
        out["ideas_master"].append({
            "idea_id": i["id"], "date": i["date"], "year": int(i["date"][:4]), "ticker": i["ticker"], "company_name": i["company"], "author": i["author"],
            "is_short": int(i["raw_short"]), "direction_ko": "숏" if i["raw_short"] else "롱", "idea_type_ko": "기업가치/증권분석",
            "source_link": i["source"] or None, "description_chars": desc_chars, "catalyst_chars": catalyst_chars, "contest_winner": 0,
            "auto_tag_status_ko": "raw 방향 보존·본문 증권/방향 수동검증 완료", "narrative_tags_ko": "radio; satellite audio; leverage; capital allocation; security selection",
            "horizon_raw": i["raw_horizon"], "horizon_months": None, "performance_available": int(bool(perf)),
            "perf_1m": perf.get("1m"), "perf_3m": perf.get("3m"), "perf_6m": perf.get("6m"), "perf_1y": perf.get("1y"), "perf_2y": perf.get("2y"), "perf_3y": perf.get("3y"), "perf_5y": perf.get("5y"),
            "idea_return_1y": None, "idea_return_3y": None, "idea_return_5y": None,
        })
        out["postmortems"].append({
            "idea_id": i["id"], "ticker": i["ticker"], "research_direction_ko": i["direction"], "company_description_ko": BUSINESS[i["ticker"]],
            "original_thesis_ko": i["t0"], "actual_development_ko": i["actual"], "thesis_verdict_ko": i["conclusion"],
            "business_verdict_ko": i["scorecard"][0][1], "catalyst_verdict_ko": i["scorecard"][2][1], "valuation_verdict_ko": i["scorecard"][1][1],
            "stock_verdict_ko": i["price"], "current_verdict_ko": i["verdict"], "overall_verdict_ko": i["verdict"], "why_ko": i["drivers"],
            "success_pattern_ko": "claim_mapping; security_mapping; capital_structure; primary_source_validation", "failure_pattern_ko": "duration; leverage; timing; catalyst; gross_net_confusion",
            "root_error_ko": i["error"], "first_signal_ko": i["warning"], "first_signal_date": i["first_signal_date"],
            "knowable_at_t0_ko": i["claims"][0]["evidence"] + " " + i["claims"][0]["falsifier"], "avoidability_ko": "중간 이상. T0 공시로 증권·현금엔진·부채·촉매·반증조건을 분리할 수 있었다.",
            "counterfactual_question_ko": i["counterfactual"], "analyst_note_ko": f"raw SQL {'Short' if i['raw_short'] else 'Long'} 보존; 실제 방향 {i['direction']}. {i['raw_horizon']}",
            "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None,
            "confidence": 0.78 if i["id"].startswith("23194") else (0.89 if not i["source"] else 0.95), "research_asof": ASOF, "research_status_ko": "1차자료 검증 완료·가격성과 제한 명시",
        })
        out["meta"].append({
            "idea_id": i["id"], "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·가격·event calendar·first break·security payoff 장문분석",
            "report_version": "V9-canonical", "thesis_type_ko": i["title"], "one_line_verdict_ko": i["conclusion"], "thesis_score": i["score"], "process_score": i["process"],
            "return_summary_ko": i["price"], "core_error_ko": i["error"], "core_insight_ko": i["lessons"][0], "research_asof": ASOF,
        })
        sections = [
            ("회사·가치사슬·현금엔진", f"{BUSINESS[i['ticker']]}\n\n{ENGINE[i['ticker']]}\n\n핵심 KPI: {KPI[i['ticker']]}."),
            ("T0 시장기대·reverse expectations", f"{i['t0']}\n\n{i['reverse']}"),
            ("Valuation·payoff·실제경로", f"{i['valuation']}\n\n실제: {i['actual']}\n\n가격: {i['price']}"),
            ("사후인과·오류·교훈", f"{i['drivers']}\n\n오류: {i['error']}\n\nCounterfactual: {i['counterfactual']}"),
        ]
        for n, (title, body) in enumerate(sections, 1):
            out["sections"].append({"idea_id": i["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, (c, weight) in enumerate(zip(i["claims"], WEIGHTS), 1):
            out["claims"].append({"idea_id": i["id"], "claim_order": n, "claim_title_ko": c["title"], "thesis_weight_pct": weight, "original_claim_ko": c["original"], "t0_evidence_ko": c["evidence"], "key_assumption_ko": c["assumption"], "ex_ante_falsifier_ko": c["falsifier"], "actual_result_ko": c["actual"], "quantitative_gap_ko": c["gap"], "verdict_ko": c["verdict"], "analytical_error_ko": c["error"], "reusable_lesson_ko": c["lesson"]})
        for n, row in enumerate(i["metrics"], 1):
            out["metrics"].append({"idea_id": i["id"], "metric_order": n, "metric_name_ko": row[0], "t0_value_ko": row[1], "thesis_expectation_ko": row[2], "actual_value_ko": row[3], "verdict_ko": row[4], "interpretation_ko": f"{row[0]}의 T0 기대와 실제를 동일 단위가 가능한 범위에서 비교했다."})
        for n, row in enumerate(i["timeline"], 1):
            out["timeline"].append({"idea_id": i["id"], "event_order": n, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for n, source in enumerate(idea_sources(i), 1):
            out["sources"].append({"idea_id": i["id"], "source_order": n, "source_type_ko": source["type"], "publisher": source["publisher"], "title_ko": source["title"], "source_date": source["date"], "url": source["url"], "evidence_ko": source["evidence"]})
    return out


def render_index(ideas):
    lines = [
        "# Batch 042 — Radio / Satellite Audio V9 Index", "",
        "> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.",
        f"> Research as-of {ASOF}. 원문 방향과 실제 security direction을 분리하고 SEC·회사·CRB·FCC 1차자료로 검증했다.", "",
        "## Canonical idea files", "", "| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |", "|---:|---|---|---|---|---|---|",
    ]
    for n, i in enumerate(ideas, 1):
        raw = "Short" if i["raw_short"] else "Long"
        rel = i["filename"].removeprefix("analysis/")
        lines.append(f"| {n} | {i['date']} | {i['ticker']} | {raw} | {i['direction']} | [{i['date']} {i['ticker']}]({rel}) | {i['verdict']} |")
    lines += [
        "", "## Direction / security audit", "",
        "Raw SQL은 CMLS 2013, SGA 2010, SALM 2019, XMSR 2002, SIRI 2006·2013·2017을 Short로 저장했다. 실제 원문은 CMLS·SGA 2010·SALM 2019·SIRI 2013이 common Long이며 XMSR 2002는 14% senior secured notes Long이다. SGA 2019·2022와 SALM 2012는 raw와 실제가 Long, SIRI 2006·2017만 실제 Short다.",
        "", "## 핵심 판정", "",
        "1. **CMLS 2013 Long:** Westwood One 자산은 생존했지만 common은 2017·2026 두 차례 Chapter 11을 거쳐 강한 실패다.",
        "2. **SGA 2010 Long:** 원문 body는 누락됐지만 price-only 3년 +162.9%(연 38.01%), 5년 +130.4%(연 18.16%)로 성과는 강하다.",
        "3. **SGA 2019 Long:** 순현금·pandemic 방어는 맞았으나 3년 +9.6%(연 3.10%)로 $50 target은 실패했다.",
        "4. **SGA 2022 Long:** 2022 FCF는 forecast보다 30% 낮았지만 약 6개월 내 $4.50 dividend와 price-only +10.7%로 catalyst가 적중했다.",
        "5. **SALM 2012·2019 Long:** block programming과 배당은 일시적이었고 2020 배당 중단, 2024 delisting/debt transaction, 2026 $1 take-private로 장기 실패했다.",
        "6. **XMSR 2002 bond Long:** 2003 secured exchange와 2006 premium redemption으로 security selection이 강하게 적중했다. exact IRR은 tender·warrant 경로 부재로 만들지 않았다.",
        "7. **SIRI 2006 Short:** standalone funding risk는 맞았지만 subscriber growth와 XM merger가 2007 path를 바꿨다.",
        "8. **SIRI 2013 Long:** 2016~2018 EBITDA·FCF·margin과 대규모 buyback은 중기 논지를 확인했다. 10% subscriber CAGR은 과대였다.",
        "9. **SIRI 2017 Short:** 15.5% royalty는 방향상 적중했지만 24개월 earnings path와 $2.50 target은 실패했다. subscriber decline은 2024~25에야 뚜렷했다.",
        "", "## 공통 분석식", "",
        "`subscriber/local-ad/block revenue - content·royalty·station cost - corporate cost - cash interest - capex - tax = common equity FCF`",
        "", "채권은 `escrow coupon + exchange consideration + warrant/recovery - stripped purchase cost`로 따로 계산한다. Debt 감소는 organic paydown, asset-sale-funded exchange, court-driven equitization을 구분한다.",
        "", "## 상위 교훈", "",
        "1. radio license scarcity는 advertiser attention의 moat가 아니다.",
        "2. 높은 FCF yield는 짧은 duration과 refinancing tail의 가격일 수 있다.",
        "3. 순현금은 downside buffer지만 자동 rerating catalyst가 아니다.",
        "4. 배당·debt paydown·성장투자는 같은 현금을 두 번 쓸 수 없다.",
        "5. distress에서는 enterprise thesis보다 security waterfall이 더 중요하다.",
        "6. secular short는 방향뿐 아니라 horizon 안의 earnings inflection이 필요하다.",
        "", "## 앱/DB 반영", "",
        "- `analysis/batch_042_radio_satellite_audio_10.md`는 10개 canonical 파일을 불러오는 wrapper다.",
        "- `data/curated/batch_042_radio_satellite_audio_deep_v7.json`은 V9 상세 overlay다.", "",
    ]
    return "\n".join(lines)


def main():
    if len(IDEAS) != 10 or len({i["id"] for i in IDEAS}) != 10:
        raise ValueError("Batch 042 must contain exactly ten unique ideas")
    for i in IDEAS:
        if len(i["claims"]) != 6 or sum(WEIGHTS) != 100:
            raise ValueError(f"{i['id']}: six weighted claims required")
        path = ROOT / i["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_report(i), encoding="utf-8")
    (ROOT / "analysis" / "batch_042_radio_satellite_audio_v9_index.md").write_text(render_index(IDEAS), encoding="utf-8")
    parts = "|".join(i["filename"].removeprefix("analysis/") for i in IDEAS)
    wrapper = "# Batch 042 — Radio / Satellite Audio V9\n\n" + f"<!-- batch_parts: {parts} -->\n\n" + "> Streamlit 호환 wrapper다. canonical index: [Batch 042 V9 Index](batch_042_radio_satellite_audio_v9_index.md).\n"
    (ROOT / "analysis" / "batch_042_radio_satellite_audio_10.md").write_text(wrapper, encoding="utf-8")
    payload = make_payload(IDEAS)
    output = ROOT / "data" / "curated" / "batch_042_radio_satellite_audio_deep_v7.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reports={len(IDEAS)} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
