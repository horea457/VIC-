#!/usr/bin/env python3
"""Build Batch 046 Anthem / Athabasca / Athene / CIT canonical V9 artifacts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-09"
WEIGHTS = [20, 18, 18, 16, 16, 12]


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return dict(title=title, original=original, evidence=evidence, assumption=assumption,
                falsifier=falsifier, actual=actual, verdict=verdict, lesson=lesson)


def S(title, url, publisher, date, evidence, kind="1차자료"):
    return dict(title=title, url=url, publisher=publisher, date=date, evidence=evidence, kind=kind)


BUSINESS = {
    "anthem": (
        "Anthem은 지역 Blue Cross Blue Shield 면허 아래 고용주·개인·정부 가입자에게 건강보험을 제공한다. 경제엔진은 "
        "`가입자 수 × 보험료 - 의료비 - 판매·관리비 - 세금·필요자본비용`이다. 가장 중요한 수치는 매출보다 medical loss ratio(MLR), "
        "보험료 갱신률, 가입자 mix, SG&A ratio, 준비금 적정성과 인수 통합비다. 보험료는 매년 다시 가격을 붙일 수 있지만 의료비 추세를 뒤늦게 "
        "따라가면 한 해의 손해가 먼저 발생한다. 따라서 margin expansion은 단순 비용절감이 아니라 pricing lag, 의료이용량, network discount와 "
        "규제 승인을 함께 통과해야 common equity로 귀속된다."
    ),
    "athabasca": (
        "Athabasca Oil은 Alberta의 oil sands와 Duvernay·Montney 같은 light-oil 자산을 개발한다. 당시 현금엔진은 생산현금흐름보다 "
        "`보유 현금 + JV/put 수취액 + 위험조정된 매장량 가치 - 남은 개발 capex - 시간·허가·commodity discount - corporate cost`에 가까웠다. "
        "즉 지하자원 NAV는 곧바로 equity value가 아니다. first steam, ramp, steam-oil ratio, well cost, 승인, 원유가격·차등, pipeline, partner funding과 "
        "희석을 모두 거쳐야 한다. 장기 프로젝트의 시간은 회계상 부채가 적어도 경제적 레버리지로 작동한다."
    ),
    "athene": (
        "Athene은 retail annuity·institutional reinsurance로 장기 보험부채를 조달하고 fixed income·structured credit·private assets에 투자해 spread를 번다. "
        "현금엔진은 `투자수익률 - 계약자 crediting/hedging cost - DAC amortization - 운영비 - 실현 신용손실 - 세금·자본비용`이다. "
        "Apollo는 origination과 자산운용을 제공하지만 약 40bp의 fee와 관련자 거래·governance 문제도 만든다. P/B나 P/E만 볼 수 없고, "
        "asset/liability duration, surrender behavior, ratings·RBC, AOCI와 economic credit loss, excess capital, buyback·reinsurance economics를 연결해야 한다."
    ),
    "cit": (
        "CIT는 중견기업 대출·리스·factoring·vendor finance·항공기·철도차량 금융을 하는 비은행 금융사였다. 수익은 "
        "`earning assets × net finance margin + fee - credit loss - funding cost - operating cost - 자본비용`이다. 예금기반이 약하고 unsecured debt·CP·ABS에 "
        "의존하면 장부가치가 높아도 시장이 닫히는 순간 equity duration이 급격히 짧아진다. 따라서 P/TBV와 정상 EPS보다 만기 ladder, 담보·haircut, "
        "CP rollover, bank line 가용성, ratings trigger, asset-sale realizability와 common 앞의 구조적 청구권이 먼저다."
    ),
}


SOURCES = {
    "anthem": [
        S("Anthem 2001 VIC 원문", "https://www.valueinvestorsclub.com/idea/Anthem/3720878904", "VIC", "2002-01-18", "8m 가입자·14x 2002 EPS·MLR와 $58/$70 valuation"),
        S("Anthem SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=1156039&owner=exclude", "SEC / Anthem", "2001-2022", "demutualization 이후 filings와 법인 연속성"),
        S("Anthem–WellPoint merger announcement", "https://www.sec.gov/Archives/edgar/data/1156039/000119312504011119/d425.htm", "SEC / Anthem", "2003-10-27", "WellPoint 결합 조건과 전략적 종착점"),
    ],
    "athabasca": [
        S("Athabasca investor reports", "https://www.athabascaoil.com/investors/financial-reports/", "Athabasca Oil", "2011-2025", "Dover 현금·Hangingstone·light-oil 자본배분의 후속 검증"),
        S("Athabasca corporate presentation archive", "https://www.athabascaoil.com/investors/presentations-events/", "Athabasca Oil", "2011-2025", "project 규모·production ramp·자본계획"),
        S("Alberta Energy Regulator", "https://www.aer.ca/", "AER", "2013-2014", "Dover 승인과 규제경로의 1차 기관"),
    ],
    "athene": [
        S("Athene SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=1527469&owner=exclude", "SEC / Athene", "2016-2022", "book value·spread·capital·related-party disclosure"),
        S("Athene 2020 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1527469/000152746921000018/ath-20201231.htm", "SEC / Athene", "2021-02-26", "2020 stress, portfolio, capital과 earnings bridge"),
        S("Apollo and Athene transaction close", "https://ir.apollo.com/news-events/press-releases/detail/28/apollo-and-athene-announce-transaction-close", "Apollo", "2022-01-03", "전액주식 합병 종결과 standalone ATH의 terminal event"),
    ],
    "cit": [
        S("CIT 2009 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1171825/000089109210001036/e38085_10k.htm", "SEC / CIT", "2010-03-01", "Chapter 11, old common cancellation과 재편 balance sheet"),
        S("CIT SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=1171825&owner=exclude", "SEC / CIT", "2002-2022", "funding·asset sales·bank holding company·reorganization 검증"),
        S("CIT restructuring filing", "https://www.sec.gov/Archives/edgar/data/1171825/000095012309051067/y79463exv99wt3ew1.htm", "SEC / CIT", "2009-11-01", "prepackaged Chapter 11과 security waterfall"),
    ],
}


IDEAS = [
    dict(id="4510e63f-516d-422c-ad0f-976c01c76690", date="2002-01-18", author="abra399", ticker="ATH", entity="Anthem, Inc.", group="anthem", raw_short=False, direction="Long", entry="$51", horizon="12~24개월", filename="analysis/ideas/2002/2002-01-18_ANTHEM_long.md", link="https://www.valueinvestorsclub.com/idea/Anthem/3720878904", desc=3322, cat=69,
         title="demutualization 이후 margin·multiple 동시 정상화 Long", verdict="사업·전략 종착점 성공, SQL 가격성과는 미검증", score=8.5, process=8.0,
         summary="2001년 10월 demutualization IPO 뒤 $36에서 $51로 올랐지만, 8개 주 800만 가입자의 Anthem은 여전히 2002 EPS 14배로 Trigon 15배·WellPoint 18배보다 쌌다. 상호회사 시절 4% 미만이던 margin을 peer 5%로 끌어올리면 EPS $4.50+, 16배 적용 시 $70+라는 Long이다. raw와 실제 방향은 모두 Long이다.",
         valuation="Base는 2002 EPS $3.65×16=$58로 약 14% upside이고, 원문 표현상 당시 가격 대비 20% 이상을 기대했다. Bull은 margin 5%×EPS $4.50+×16=$70+다. 핵심은 2~3 multiple point discount와 약 100bp margin gap이 중복된 가치가 아니라 earnings와 multiple의 두 단계 bridge라는 점이다.",
         actual="Anthem은 상장 보험사로서 가입자·수익기반을 키웠고 2004년 WellPoint Health Networks와 약 $16.5bn 규모 결합을 완료했다. 이는 전국 Blue 네트워크와 scale 논지를 확인하는 전략적 종착점이다. 다만 합병 사실만으로 2002년 $51 entry의 1/3/5년 total return을 역산하지 않았다.",
         price="첨부 SQL에 performance row가 없다. $51은 원문 서술가격이며, corporate action·배당·WellPoint 교환비율을 반영한 시계열을 복원하지 못해 1/3/5년 return과 IRR은 null이다.",
         drivers="demutualization 이후 비용규율, 보험료 재가격과 peer scale이 business quality를 높였다. 최종 결합은 네트워크 경쟁의 option value를 실현했다. 수익의 원인은 단순 multiple expansion보다 MLR·SG&A 개선과 기업결합 기대의 조합이었다.",
         error="$58 base를 '20% 이상'으로 표현한 숫자 불일치, margin 100bp 개선을 세전/세후 EPS로 세밀하게 연결하지 않은 점, Kansas와 후속 인수의 통합비·reserve risk를 낮게 둔 점이 약점이다.", first_signal="MLR가 85%에서 peer 81~82%로 좁혀지지 않거나 두 번의 annual repricing 뒤에도 margin이 4% 아래면 $70 bull case를 제거해야 했다.",
         metrics=[("가입자", "8m/8개 주", "Kansas+scale", "WellPoint 결합으로 확대", "성공"),("2002 EPS", "$3.65E", "16x=$58", "SQL 성과 없음", "미검증"),("Operating margin", "<4%", "5%", "장기 scale 개선", "방향 성공"),("MLR", "85%", "peer 81~82% 접근", "정확한 horizon 미복원", "미검증"),("Strategic event", "standalone", "national Blue network", "2004 WellPoint 결합", "성공")],
         timeline=[("2001-10","demutualization IPO","$36 출발"),("2002-01-18","VIC Long","$51·$58/$70+"),("2002 여름","Kansas BCBS closing 예상","scale catalyst"),("2003-10","WellPoint 결합 발표","전략 옵션 현실화"),("2004-11","규제 승인","closing gate"),("2004-12-01","합병 완료","사업 종착점 성공")],
         claims=[C("peer multiple discount", "14x를 16x로 정상화하면 $58다.", "TGH 15x·WLP 18x", "growth·reserve quality가 유사하다.", "MLR/성장 열위가 지속되면 discount 정당화.", "전국 scale과 merger option이 실현됐다.", "성공/수익 미검증", "peer multiple은 margin·reserve 차이를 조정한다."), C("100bp margin expansion", "<4%에서 5%면 EPS $4.50+다.", "mutual 시절 낮은 효율", "pricing과 SG&A가 동시에 개선된다.", "두 갱신주기 뒤 4% 미만이면 반증.", "장기 사업 확장은 방향을 지지했다.", "방향 성공", "보험 margin은 MLR와 SG&A로 나눈다."), C("보험료 12% 인상", "medical trend를 가격으로 상쇄한다.", "Q3 managed-care pricing +12%", "가입자 이탈 없이 갱신된다.", "MLR 상승·membership 감소 동시 발생.", "scale franchise는 생존·확대했다.", "부분 검증", "price와 retention을 함께 본다."), C("IPO 물량압력 해소", "policyholder/flipper 매도가 일시적이다.", "$36→$51 뒤 변동성", "매도 종료 후 fundamental buyer가 유입된다.", "volume 소화 뒤에도 discount 지속.", "장기 rerating은 있었으나 timing 미복원.", "미검증", "technical catalyst에는 날짜·거래량 조건을 둔다."), C("Kansas·과거 M&A 통합", "통합이 margin 개선을 돕는다.", "1993~2002 다수 인수", "systems·reserve 통합비가 제한적이다.", "통합비와 reserve strengthening이 EPS 훼손.", "WellPoint 대형 결합까지 진전했다.", "성공", "serial M&A는 organic cohort와 분리한다."), C("national Blue option", "Anthem/WellPoint 경쟁이 전략가치를 높인다.", "전국망 구축 경쟁", "과지불 없이 scale을 얻는다.", "20x+ 인수·희석이면 반증.", "2004 두 회사가 결합했다.", "강한 성공", "terminal event와 투자수익은 별도 기록한다.")]),

    dict(id="a9e042a6-e212-41eb-b757-77e1c4aaf755", date="2011-08-22", author="pathbska", ticker="ATH", entity="Athabasca Oil Sands Corp.", group="athabasca", raw_short=True, direction="Long", entry="C$12.02", horizon="2~6년", filename="analysis/ideas/2011/2011-08-22_ATHABASCA_OIL_long.md", link="https://www.valueinvestorsclub.com/idea/ATHABASCA_OIL_SANDS_CORP/7591076608", desc=7142, cat=72,
         title="PetroChina put과 world-scale acreage의 비대칭 Long", verdict="put 가치 실현, long-duration NAV·equity rerating은 혼합", score=7.0, process=7.5,
         summary="raw Short지만 본문은 명백한 Long이다. C$12.02에서 PetroChina put과 net cash를 합친 hard cash C$7.50대가 하방을 막고, 7.5bn bbl 잔여 oil-sands를 JV 거래의 C$0.80/bbl에 평가하면 C$20~22가 된다고 봤다. 70% upside/30% downside를 섞은 기대값은 C$17.81, 약 +48%였다.",
         valuation="Hard cash C$7.54, 보수적 downside C$9.35, upside C$21.44를 사용했다. 원문의 probability-weighted value는 `70%×21.44 + 30%×9.35 = C$17.81`이다. 하지만 put의 세금·closing 조건, 개발 burn과 2014/2017 production duration을 분리하지 않으면 cash floor가 시간에 따라 줄어든다.",
         actual="PetroChina 관련 put 거래는 후속 규제·settlement를 거쳐 결국 현금화되어 핵심 asset-monetization 논리는 맞았다. 반면 zero-revenue land bank의 장기 생산·commodity duration은 원문이 인정한 것보다 훨씬 큰 변동성을 만들었고 이후 oil-price 하락은 NAV rerating을 훼손했다. event 성공과 C$20~22 equity 성공은 같은 판정이 아니다.",
         price="SQL performance row가 없어 exact return은 null이다. 원문 C$12.02, downside C$9.35, EV C$17.81, upside C$21.44만 T0 anchor로 사용한다.",
         drivers="가치의 첫 driver는 원유가격이 아니라 계약상 put과 대형 파트너의 지급능력이었다. 이후 equity는 capex burn·승인·기술·oil beta에 다시 노출됐다. 즉 cash floor는 closing 전 event claim이고, closing 뒤에는 capital-allocation claim으로 변한다.",
         error="현금을 'hard downside'로 부르면서 수령시점·세금·잔여 capex·경영진 재투자를 충분히 haircut하지 않았다. carbonate 2.9bn bbl의 상업성 검증 전 resource multiple을 적용한 것도 큰 model risk다.", first_signal="put 승인 지연으로 수령시점이 한 해 이상 밀리거나 annual cash burn이 C$7.54 floor의 15~20%를 소진하면 downside와 확률을 즉시 재산정해야 했다.",
         metrics=[("Entry", "C$12.02", "EV C$17.81", "SQL 성과 없음", "미검증"),("Hard cash", "C$7.54", "하방 floor", "put 수취 후 재투자", "부분 성공"),("Upside", "C$21.44", "70% 확률", "정확 가격경로 없음", "미검증"),("잔여 resource", "7.5bn bbl", "C$0.80/bbl", "기술·capex 할인 지속", "과대 가능"),("생산 timing", "2014/2017", "ramp", "긴 duration 현실화", "혼합")],
         timeline=[("2009-08","PetroChina JV","60%에 C$1.9bn"),("2010-04","C$1.35bn IPO","자본확보"),("2011-08-22","VIC Long","C$12.02"),("2014","first oil 목표","duration 시작"),("2014","Dover put 진행","cash catalyst 현실화"),("2014-2016","oil-price 충격","NAV discount 확대"),("2017+","serious production 가정","원 horizon 장기화")],
         claims=[C("C$7.54 cash floor", "put+net cash가 하방이다.", "C$1.1bn net cash·잔여 put", "계약이 집행되고 cash가 보존된다.", "승인 지연·cash burn·재투자면 반증.", "put은 실현됐지만 cash는 영구 floor가 아니었다.", "부분 성공", "cash floor에는 time-to-cash와 use-of-cash를 붙인다."), C("C$20~22 resource value", "JV C$0.80/bbl을 잔여 7.5bn에 적용한다.", "PetroChina precedent", "질·승인·인프라가 유사하다.", "pilot 실패·capex 상승이면 multiple 제거.", "long-duration·technology discount가 지속됐다.", "부분/과대", "precedent는 barrel quality와 funding을 맞춘다."), C("70/30 expected value", "EV C$17.81로 +48%다.", "C$21.44/C$9.35 시나리오", "두 상태가 주요 결과를 포괄한다.", "중간 희석·oil crash 상태가 크면 반증.", "중간 경로와 macro tail이 컸다.", "불완전", "확률표에는 financing·commodity state를 추가한다."), C("PetroChina 지급", "major가 계약을 이행한다.", "기존 60% 거래", "정치·규제와 funding barrier가 없다.", "put 조건 재협상·장기소송이면 반증.", "거래 현금화로 핵심 전제는 맞았다.", "성공", "counterparty와 condition precedent를 분리한다."), C("light oil이 idle cash를 번다", "단기 cycle 자산이 burn을 상쇄한다.", "quick-return wells", "well economics가 oil-price 하락에도 견딘다.", "FCF 음수·capex 확대면 반증.", "commodity beta를 없애지 못했다.", "혼합", "bridge asset도 full-cycle breakeven으로 본다."), C("market turmoil이 원인", "zero-revenue duration 할인은 일시적이다.", "2011 risk-off", "할인율만 정상화되고 fundamentals는 유지된다.", "project delay·oil 하락이면 구조 문제.", "후속 위험은 단순 sentiment 이상이었다.", "부분 실패", "macro discount와 project impairment를 분해한다.")]),

    dict(id="147a6251-3aab-4a99-bfee-0685a093135d", date="2013-12-26", author="hao777", ticker="ATH", entity="Athabasca Oil Corp.", group="athabasca", raw_short=True, direction="Long", entry="C$6.25", horizon="6~24개월", filename="analysis/ideas/2013/2013-12-26_ATHABASCA_OIL_long.md", link="https://www.valueinvestorsclub.com/idea/ATHABASCA_OIL_CORP/8944407068", desc=20053, cat=0,
         title="C$1.32bn Dover put의 binary overhang 해소 Long", verdict="핵심 put catalyst 성공, C$10~15 NAV의 지속성은 oil shock로 실패", score=7.5, process=8.0,
         summary="raw Short지만 C$6.25에서 산 event-driven Long이다. 주가는 YTD 40% 하락했지만 Dover 40% put C$1.32bn은 시가총액의 약 50%였고, Fort McKay First Nation 분쟁·cabinet 지연이 2개 분기 안에 풀릴 것으로 봤다. core/light-oil NAV는 C$17 북쪽, haircut한 적정가는 C$10~15였다.",
         valuation="Hangingstone·Dover West·Duvernay·Montney를 합친 gross NAV에서 capex·corporate cost를 빼면 C$17+라고 계산했고, 실행 haircut 뒤 C$10~15를 제시했다. 가장 관찰 가능한 bridge는 C$1.32bn put 수취다. 이것이 약 C$3.3/share에 해당하더라도 전액 excess cash가 아니며 2014 C$460m budget과 project funding을 차감해야 한다.",
         actual="Dover 관련 승인·합의가 진행되고 Athabasca는 PetroChina put 대금을 받으면서 가장 중요한 binary catalyst는 실현됐다. 그러나 직후의 원유가격 붕괴와 development economics 악화로 gross NAV는 현금만큼 안정적인 가치가 아니었다. event window의 논지는 성공이지만 C$10~15를 장기 intrinsic value로 본 결론은 지속되지 않았다.",
         price="SQL performance가 없다. C$6.25 entry와 C$10~15 target의 정확한 달성·보유수익은 null로 남긴다. 사건 발생을 price return으로 대체하지 않는다.",
         drivers="초기 rerating을 만든 것은 court/cabinet sequence와 지급확률이었다. 이후 common 가치는 받은 현금의 재투자, Hangingstone ramp와 oil price로 이동했다. thesis가 event asset에서 operating E&P로 바뀐 순간 exit rule이 필요했다.",
         error="C$1.32bn 수령과 C$17 gross NAV를 같은 확실성으로 합쳤고, cash receipt 직후 2014 capex·Hangingstone ramp·commodity hedge를 충분히 stress하지 않았다. 정부·First Nation 사건의 확률도 단일 2-quarter clock에 과도하게 압축했다.", first_signal="Dover cash가 들어온 뒤에도 주당 순현금이 budget burn보다 빠르게 줄거나 Hangingstone first steam/cost가 plan을 벗어나면 catalyst 성공과 무관하게 exit해야 했다.",
         metrics=[("Entry", "C$6.25", "C$10~15", "SQL 성과 없음", "미검증"),("Dover put", "C$1.32bn", "2개 분기 수취", "후속 수취", "성공"),("2014 budget", "C$460m", "flexibility 유지", "현금 재투자", "혼합"),("Hangingstone 1", "12k boe/d", "Q4'14 first steam", "ramp/cycle risk", "혼합"),("Core NAV", ">C$17", "60~100%+ upside", "oil shock로 훼손", "실패")],
         timeline=[("2013-04","AER hearing","FMFN dispute"),("2013-08-06","AER approval","주가 반응"),("2013-10-18","appeal 수용","overhang 확대"),("2013-12-26","VIC Long","C$6.25"),("2014","settlement/approval 진행","event de-risk"),("2014","Dover put 현금화","핵심 catalyst"),("2014-2016","oil collapse","NAV 반증")],
         claims=[C("2개 분기 내 C$1.32bn", "settlement·cabinet 뒤 put 수취다.", "계약·AER approval·PetroChina 의사", "FMFN 합의와 condition precedent 완료.", "hearing·appeal 재지연이면 반증.", "후속 거래로 현금화됐다.", "성공", "binary event는 법적 gate별 확률을 둔다."), C("C$10~15 fair value", "현금과 자산을 합치면 현 가격 60~100%+다.", "gross NAV >C$17", "capex·oil haircut이 충분하다.", "strip 하락으로 project NPV가 음수면 반증.", "oil shock에서 지속되지 않았다.", "장기 실패", "resource NAV는 strip·capex sensitivity 표가 필요하다."), C("Plan B가 bridge", "C$460m 예산으로 put까지 버틴다.", "Kaybob infra 50% 매각 C$145m", "추가 희석 없이 핵심 project 유지.", "liquidity buffer가 12개월 아래면 반증.", "회사는 event까지 bridge했다.", "성공", "bridge liquidity는 최소 18개월로 본다."), C("Hangingstone first steam", "Q4'14부터 12k boe/d가 가치를 연다.", "건설·개발 일정", "cost/SOR/ramp가 plan 근처다.", "6개월+ 지연·capex overrun이면 반증.", "운영가치는 macro·ramp에 흔들렸다.", "혼합", "first steam과 steady-state cash를 구분한다."), C("Duvernay option", "350k net/200k high-grade acres가 jewel이다.", "peer well results", "ATH acreage와 economics가 비교 가능.", "well NPV·JV bid가 기대 미달이면 반증.", "asset option은 남았지만 target을 방어하지 못했다.", "부분", "adjacent acreage는 own-well data로 할인한다."), C("misguided promises는 신뢰문제일 뿐", "2013 사건은 저확률 legal delay다.", "management Plan B", "운영·capital allocation 능력은 훼손되지 않음.", "반복 일정 miss면 governance discount 구조화.", "event는 풀렸지만 후속 value는 약했다.", "부분", "한 번의 외생지연과 반복 과신을 분리한다.")]),

    dict(id="1dacae0f-2738-4d5b-a79c-0623c39908e3", date="2017-05-02", author="pcm983", ticker="ATH", entity="Athene Holding Ltd.", group="athene", raw_short=True, direction="Short", entry="약 $55", horizon="12~24개월", filename="analysis/ideas/2017/2017-05-02_ATHENE_short.md", link=None, desc=25898, cat=2362,
         title="1.6x book에 성장·Apollo 구조위험을 판 Athene Short", verdict="$33 target은 미달; 일부 de-rating 뒤 Long counter-pitch가 반증", score=5.5, process=7.0,
         summary="raw와 실제 모두 Short다. 약 1.6x P/B ex-AOCI, 13x 2017 P/E가 peer 대비 과도하고, 5~10% commission을 써서 비선호 annuity를 공격적으로 가격하며 성장한다고 봤다. Aviva 등 block acquisition, Bermuda 재보험·낮은 세율, Apollo fee·conflict, 4년 4명 CFO를 위험으로 묶어 $33, 약 40% downside를 제시했다.",
         valuation="Target은 ex-AOCI book 약 $33에 1.0x를 적용했다. Short payoff는 1.6x→1.0x multiple compression에 ROE 하락까지 겹친 구조다. 그러나 성장 둔화가 book destruction을 뜻하지 않고, 15% 안팎 ROE로 book이 복리하면 시간은 Short의 적이다. borrow·dividend·takeout option도 target bridge에 포함해야 한다.",
         actual="2018년 9월 후속 반대 Long은 주가 약 $49, 1.1x P/B·7x forward P/E라고 기록했다. 즉 multiple은 크게 압축됐지만 $33 target과 thesis-level impairment는 나타나지 않았다. 2020 stress를 견딘 뒤 2021 Apollo 결합이 발표되고 2022 종결돼 standalone short에는 terminal M&A risk가 현실화됐다.",
         price="SQL performance row가 없다. 약 $55 T0와 2018년 원문 anchor $49만 비교 가능하며 정확한 adjusted return은 null이다. 2020 COVID 저점은 원래의 구조적 short가 맞았다는 단독 증거로 쓰지 않는다.",
         drivers="초기 de-rating은 IPO premium, governance·credit 우려와 낮은 life-insurer multiple의 평균회귀가 만들었다. 그러나 earnings/book compound와 excess capital이 $33까지의 손실가정을 상쇄했고, Apollo 거래는 conflict risk가 동시에 strategic value임을 보여줬다.",
         error="판매 commission을 고객가치 부재와 등치했고, acquisition growth와 organic liability franchise를 충분히 분리하지 않았다. 관련자 구조의 downside는 상세했지만 Apollo가 제공하는 origination·takeout option의 convexity와 book compounding을 underwrite하지 않았다.", first_signal="2018년 1.1x book·7x P/E까지 de-rate했는데도 ROE·capital이 유지되면 valuation claim은 달성된 것이므로 cover하고 $33 target을 고집하지 말아야 했다.",
         metrics=[("T0 P/B ex-AOCI", "1.6x", "1.0x", "2018 약 1.1x", "대부분 성공"),("T0 P/E", "13x", "peer 수준", "2018 약 7x", "성공"),("ROE", "24→15.6→12.5%", "계속 하락", "후속 15%대 회복", "반증"),("Target", "$33", "-40%", "후속 $49 anchor", "미달"),("Terminal event", "standalone", "규제/실망", "2022 Apollo 합병", "Short 위험")],
         timeline=[("2016-12","Athene IPO","public price discovery"),("2017-05-02","VIC Short","$33 target"),("2017-2018","multiple compression","일부 성공"),("2018-09-09","counter Long","$49·1.1x book"),("2020-03","market stress","credit/ALM test"),("2021-03","Apollo merger 발표","terminal risk"),("2022-01-03","거래 종결","standalone 종료")],
         claims=[C("1.6x book 과대평가", "peer와 risk 대비 premium이 크다.", "1.6x ex-AOCI·13x P/E", "book quality와 growth가 peer와 유사하다.", "ROE 15%+·book compound면 반증.", "1.1x까지 de-rate했으나 book 훼손은 제한적이었다.", "valuation 성공/target 실패", "Short는 multiple target에서 cover한다."), C("organic decline", "aggressive pricing 없이는 liabilities가 runoff다.", "5~8년 duration·acquisition history", "retail franchise가 economics 없이 성장한다.", "attractive return의 organic volume이면 반증.", "후속 organic/reinsurance 성장이 나타났다.", "실패", "volume을 new-business IRR과 함께 본다."), C("commission이 value 부재", "5~10% 수수료가 수요를 인위적으로 만든다.", "annuity distribution economics", "customer retention이 commission 없이는 약하다.", "persistency·spread가 견고하면 반증.", "liabilities는 stress를 견뎠다.", "과도", "distribution cost는 lifetime spread와 비교한다."), C("Bermuda tax/capital unwind", "낮은 세율·80% 재보험은 규제위험이다.", "2015/16 낮은 tax rate", "규제 변경이 capital/earnings를 훼손한다.", "구조가 승인·유지되면 timing 반증.", "원 horizon에 치명적 변경은 없었다.", "실패", "규제 short에는 법안·날짜·노출액을 둔다."), C("Apollo conflict", "40bp fee와 control이 minority에 불리하다.", "related-party structure", "fee가 origination alpha보다 크다.", "net yield/ROE가 유지되면 반증.", "합병으로 conflict는 사라졌지만 전략가치는 확인됐다.", "혼합", "related party는 gross fee보다 net economics다."), C("governance fragility", "4년 4명 CFO가 통제위험이다.", "management turnover", "보고·자본통제 문제로 번진다.", "filing·capital 문제 없이 안정되면 반증.", "파국적 통제 실패는 없었다.", "실패", "red flag와 손익 catalyst를 연결한다.")]),

    dict(id="f87c02f1-769f-4e03-be72-e8e00574c7a5", date="2018-09-09", author="Jumpman23", ticker="ATH", entity="Athene Holding Ltd.", group="athene", raw_short=True, direction="Long", entry="$49", horizon="2~5년", filename="analysis/ideas/2018/2018-09-09_ATHENE_long.md", link=None, desc=13658, cat=40,
         title="1.1x book·7x earnings에서 2017 Short를 뒤집은 Long", verdict="1~2년 price path 실패, 합병까지 보유하면 business/terminal thesis 회복", score=7.0, process=8.0,
         summary="raw Short지만 원문은 2017 Short를 정면 반박한 Long이다. 그때 1.6x book이던 주식이 $49, 약 1.1x P/B와 7x 2019 P/E로 낮아졌고, 15% 안팎 ROE·book compounding·Apollo sourcing을 이 가격에 사는 편이 유리하다고 봤다. 같은 회사도 entry valuation이 바뀌면 방향이 바뀐다.",
         valuation="P/B 1.1x, forward P/E 약 7x에서 핵심 payoff는 ① 15% ROE가 book을 늘리고 ② multiple이 최소 1.0~1.2x를 유지하는 것이다. 2017 Short의 1.6x premium은 사라졌다. 단, AOCI 제외 book·statutory capital·economic credit marks를 같은 denominator로 맞춰야 한다.",
         actual="2020년 9월 같은 작성자의 후속 Long은 2018 $49 대비 주가가 거의 30% 낮다고 명시했다. 따라서 1~2년 주식 결과는 실패다. 그러나 2020 credit stress를 견디고 Apollo 합병이 2022년 종결되면서 book·strategic franchise의 terminal value는 확인됐다. 정확한 APO 교환 후 total return은 복원하지 않았다.",
         price="SQL performance가 없다. $49 T0와 2020년 약 30% 하락이라는 원문 자기평가를 기록한다. merger-close 뒤 APO share까지 포함한 exact return은 null이다.",
         drivers="초기 손실은 lower-for-longer rates, credit fear와 life-insurer de-rating이 multiple을 더 눌렀기 때문이다. 회복 driver는 capital survival, new-money spread, third-party capital과 Apollo 결합이었다. cheap P/E는 path risk를 없애지 않았다.",
         error="7x P/E가 stress를 충분히 반영했다고 봤지만, insurer earnings의 credit/mark convexity와 liquidity-driven multiple floor를 과소평가했다. 장기 terminal thesis와 12~24개월 mark-to-market budget을 분리하지 않았다.", first_signal="P/B가 1.0x 아래로 내려갈 때 share repurchase·capital release가 discount를 줄이지 못하고 credit spread가 더 악화되면 long duration을 줄여야 했다.",
         metrics=[("Entry", "$49", "book compound", "2020 약 -30% anchor", "초기 실패"),("P/B", "1.1x", "1.0~1.2x+", "stress 때 0.7x", "실패 후 회복"),("Forward P/E", "약 7x", "rerating", "2020 FY19 5.2x", "초기 실패"),("ROE", "약 15%", "지속", "capital survival", "방향 성공"),("Terminal", "standalone", "value recognition", "Apollo 합병", "성공")],
         timeline=[("2017-05","선행 Short","1.6x book"),("2018-09-09","VIC Long","$49·1.1x"),("2019","credit/rate 우려","discount 지속"),("2020-03","COVID stress","P/B 급락"),("2020-09","후속 Long","약 30% 낮은 가격"),("2021-03","Apollo merger 발표","terminal catalyst"),("2022-01-03","종결","standalone ATH 종료")],
         claims=[C("valuation flip", "1.1x book·7x P/E면 Long이 우월하다.", "2017 1.6x 대비 압축", "book/earnings quality가 유지된다.", "credit loss로 adjusted book 훼손이면 반증.", "초기 가격은 더 하락했지만 capital은 생존했다.", "기간 혼합", "같은 기업도 가격이 direction을 바꾼다."), C("15% ROE compounding", "book이 mid-teens로 증가한다.", "spread·leverage economics", "loss·capital charge가 정상 범위다.", "ROE 한 자릿수 지속이면 반증.", "franchise는 stress와 합병을 통과했다.", "사업 성공", "ROE는 realized loss 후로 계산한다."), C("2017 short risk priced", "commission·Bermuda·Apollo 우려가 multiple에 반영됐다.", "1.6x→1.1x", "새 tail risk가 없다.", "0.8x 아래로 재평가되면 반증.", "2020에 0.7x까지 내려갔다.", "초기 실패", "싸다는 판단에도 stress multiple을 둔다."), C("Apollo sourcing advantage", "fee보다 asset alpha가 크다.", "direct origination·structured credit", "net yield가 peer보다 높고 losses는 유사.", "추가 yield가 loss/capital로 상쇄되면 반증.", "합병으로 전략적 결합이 강화됐다.", "방향 성공", "gross yield가 아닌 capital-adjusted spread다."), C("capital allocation", "discount에서 buyback·deal이 accretive다.", "excess capital", "ratings constraint 없이 실행된다.", "capital이 방어에 묶이면 반증.", "ACRA/합병 등 capital 구조가 확대됐다.", "부분 성공", "excess capital은 holdco·opco 위치를 구분한다."), C("long horizon이 volatility를 흡수", "book compound가 multiple 변동을 이긴다.", "낮은 entry multiple", "강제매도 없이 3~5년 보유.", "terminal dilution·merger unfairness면 반증.", "2년 손실 뒤 합병으로 회복 경로가 열렸다.", "경로 의존", "horizon은 risk budget이 아니라 검증기한이다.")]),

    dict(id="cea526a6-864b-4eb5-a1f5-3ef84f9d1700", date="2019-03-31", author="sas7", ticker="ATH", entity="Athene Holding Ltd.", group="athene", raw_short=True, direction="Long", entry="약 $40", horizon="3~5년", filename="analysis/ideas/2019/2019-03-31_ATHENE_long.md", link="https://www.valueinvestorsclub.com/idea/ATHENE_HOLDING_LTD/2008198635", desc=20556, cat=617,
         title="5x earnings·0.8x book에서 20% IRR을 산 Long", verdict="$64 target과 strategic value가 합병 경로에서 실현된 성공", score=9.0, process=9.0,
         summary="raw Short지만 실제는 Long이다. 2019/2020 EPS $7.30/$8.50에 5.5x/4.8x, adjusted BVPS $45.60에서 약 0.8x였다. 4.65% yield에서 crediting 1.70%, DAC 1.35%, opex 0.35%를 빼 after-tax ROA 1.25~1.35%, 11~13x leverage로 15%+ ROE를 만들 수 있다고 봤다. 7.5x 2020 EPS 또는 1.2x book의 $64, +57%가 target이다.",
         valuation="2019 EPS $7.30, 2020 $8.50과 약 $40 가격은 5.5x/4.8x다. YE18 adjusted BVPS $45.60, 2019-06 약 $49, statutory book 약 $56였다. Base $64는 7.5x 2020 EPS 또는 1.2x YE19 book. multiple이 그대로 5.5x여도 15% book/earnings compound로 약 20% IRR을 기대했다.",
         actual="2020 pandemic은 credit·ALM·capital의 실제 stress test였지만 Athene은 생존했고 ACRA·reinsurance와 Apollo 연계를 확대했다. 2021 전액주식 결합 발표와 2022 종결로 standalone ATH는 APO 1.149주 교환 구조로 끝났다. 합병 경로의 implied value는 원문의 $64 target을 지지했으나 exact total return은 SQL 부재로 산출하지 않았다.",
         price="SQL performance row가 없다. 원문 배수로 역산한 약 $40은 근사치이며 공식 entry price가 아니다. $64 target 달성 판정은 merger exchange economics와 후속 price anchor를 사용한 사건 판정이고 exact return은 null이다.",
         drivers="높은 starting earnings yield, book compounding과 capital survival이 time arbitrage를 만들었다. 94% investment-grade, 제한된 true PE/HF exposure와 dry powder가 시장의 'shadow banking' 공포를 완화했고, Apollo가 최종 strategic buyer가 됐다.",
         error="zero-rate earnings impact 10~15%와 recession loss를 단년으로 단순화했고, fee conflict·structured-credit tail과 AOCI liquidity를 더 깊게 stress할 수 있었다. 반대로 market은 headline alternatives/CLO exposure를 실제 equity-at-risk보다 크게 봤다.", first_signal="statutory capital이 modeled recession 뒤에도 유지되고 OTTI/realized loss가 원문 120bp cumulative stress 아래라면 Long 유지; 반대로 ratings downgrade·capital raise면 즉시 thesis break다.",
         metrics=[("2020 EPS", "$8.50E", "7.5x", "$64 target bridge", "성공"),("Adjusted BVPS", "$45.60→$49", "15% compound", "합병 strategic value", "성공"),("P/B", "약 0.8x", "1.2x", "terminal rerating", "성공"),("After-tax ROA", "1.25~1.35%", "유지", "stress survival", "성공"),("Target", "$64", "+57%", "합병 경로 지지", "성공/정확수익 미검증")],
         timeline=[("2018-12","BVPS $45.60","book anchor"),("2019-03-31","VIC Long","<5x 2020 EPS"),("2019-06","BVPS 약 $49","compounding"),("2020-03","COVID credit shock","stress test"),("2020-09","후속 Long","0.7x book"),("2021-03","Apollo 거래 발표","$11bn strategic event"),("2022-01-03","합병 종결","target 경로 실현")],
         claims=[C("spread ROA 1.25~1.35%", "4.65-1.70-1.35-0.35% bridge다.", "asset/liability cost breakdown", "credit loss·tax가 정상이다.", "realized loss·hedge cost로 1% 아래면 반증.", "pandemic을 통과하고 franchise가 확대됐다.", "성공", "보험 ROA는 모든 자본·credit cost 후로 본다."), C("15%+ ROE", "11~13x leverage로 mid-teens ROE다.", "ROA와 operating leverage", "ratings capital이 leverage를 허용한다.", "capital raise·RBC 압박이면 반증.", "capital survival과 거래가 이를 지지했다.", "성공", "accounting leverage보다 statutory constraint다."), C("credit fear 과도", "94% IG이고 alternatives 위험은 작다.", "true PE/HF 약 assets 75bp", "CLO senior·RMBS losses가 제한적.", "downgrade/OTTI가 recession model 초과.", "2020 modeled loss보다 견조했다.", "성공", "label이 아니라 tranche·attachment point를 본다."), C("direct origination alpha", "40bp yield advantage와 33% 목표가 있다.", "Apollo sourcing", "추가 yield가 loss·fee보다 크다.", "capital-adjusted spread가 peer 아래면 반증.", "Apollo 결합이 전략가치를 확인했다.", "성공", "origination alpha는 fee 차감 후 검증한다."), C("rate downside 제한", "±25bp는 $25~30m, zero rate도 -10~15%다.", "management sensitivity", "surrender·hedge가 모델 내다.", "earnings/book 훼손이 sensitivity 초과.", "stress에도 terminal value가 유지됐다.", "부분 성공", "nonlinear ALM tail을 별도 stress한다."), C("$64/20% IRR", "7.5x EPS·1.2x book 또는 unchanged multiple compounding.", "낮은 starting multiple", "book growth가 share count 후 유지.", "BVPS 정체·merger dilution이면 반증.", "합병 경로가 target을 지지했다.", "성공", "target과 exact total return을 구분한다.")]),

    dict(id="2cac07f8-87d1-484e-87b4-ab3523aa44da", date="2020-09-09", author="Jumpman23", ticker="ATH", entity="Athene Holding Ltd.", group="athene", raw_short=True, direction="Long", entry="약 $34", horizon="2~5년", filename="analysis/ideas/2020/2020-09-09_ATHENE_long.md", link=None, desc=14757, cat=34,
         title="0.7x book·5.2x earnings와 crisis deployment Long", verdict="Apollo 합병으로 매우 성공한 event-plus-compounder Long", score=9.2, process=9.0,
         summary="raw Short지만 실제는 Long이다. 2018년 $49 추천가보다 거의 30% 낮은 약 $34, 0.7x P/B·5.2x FY19 P/E에서 pandemic credit loss가 과도하게 반영됐다고 봤다. Apollo 거래로 $1bn excess capital, ACRA의 $4bn 목표와 약 $10bn buying power, 높아진 new-money yield와 Jackson reinsurance를 성장엔진으로 제시했다.",
         valuation="0.7x book에서 1.0x만 받아도 약 40% upside다. FY19 P/E 5.2x라 credit shock 한 해를 흡수해도 earnings yield가 높다. 원문은 몇 년 내 +100% 가능성도 제시했지만, 이는 BVPS compound·capital deployment·multiple 회복이 모두 필요하다. ACRA third-party capital은 gross liabilities가 아니라 Athene equity와 fee/share 귀속으로 환산해야 한다.",
         actual="Athene은 portfolio stress를 견뎠고 2021년 Apollo와 전액주식 합병에 합의했다. Athene 주주는 1주당 APO 1.149주를 받는 구조였고 2022-01-03 거래가 종결됐다. 0.7x book에서 산 standalone discount와 Apollo strategic value가 짧은 기간에 함께 실현돼 방향·catalyst 모두 성공이다.",
         price="SQL performance row가 없다. 2018 $49 대비 거의 30% 낮다는 원문에서 약 $34를 anchor로만 사용한다. 교환비율 이후 APO 가격·배당을 포함한 exact return은 산출하지 않아 null이다.",
         drivers="credit loss가 feared level보다 낮고 자본이 보존된 상태에서 higher new-money spread·organic volume·reinsurance deployment가 book growth를 재가동했다. Apollo가 minority discount를 거래로 닫으면서 valuation catalyst까지 발생했다.",
         error="COVID 이후 spread widening과 capital deployment를 강하게 봤지만 downgrade migration·liquidity·policyholder behavior의 nonlinear tail은 얕았다. Jackson 등 대형 block의 reserve/hedge assumption과 third-party share도 별도 haircut해야 했다.", first_signal="quarterly OTTI가 원문 <2bp 수준을 벗어나 누적 $2bn stress를 초과하거나 excess capital $1bn이 ratings 방어에 묶이면 40% rerating thesis를 낮춰야 했다.",
         metrics=[("P/B", "0.7x", "1.0x", "합병으로 discount 해소", "성공"),("FY19 P/E", "5.2x", "정상화", "terminal strategic value", "성공"),("Excess capital", "$1bn+", "deployment", "ACRA/Jackson 확대", "성공"),("New investment ROA", "+40bp", "earnings 개선", "crisis deployment", "방향 성공"),("Retail organic volume", "약 $7bn·27% return", "성장", "franchise 견조", "성공")],
         timeline=[("2018-09","선행 Long $49","valuation anchor"),("2020-03","COVID shock","credit fear"),("2020-Q2","OTTI <2bp","loss test"),("2020-09-09","VIC Long","약 $34·0.7x book"),("2020","Jackson $27bn reinsurance","deployment"),("2021-03","Apollo merger 발표","exchange 1.149 APO"),("2022-01-03","거래 종결","standalone ATH 종료")],
         claims=[C("credit loss 과대반영", "modeled OTTI $1~2bn 전에도 연 earnings $1bn+다.", "Q2 OTTI <2bp", "migration이 realized loss로 급증하지 않는다.", "누적 loss가 capital buffer 초과면 반증.", "portfolio와 capital이 stress를 견뎠다.", "성공", "mark·migration·realized loss를 분리한다."), C("0.7x book rerating", "1.0x만 가도 +40%다.", "low P/B·5.2x P/E", "adjusted book이 경제적이다.", "capital raise·reserve charge면 book haircut.", "Apollo 거래로 discount가 닫혔다.", "성공", "book target에 terminal buyer 확률을 따로 둔다."), C("$10bn buying power", "Apollo/ACRA 구조가 crisis assets를 산다.", "$1bn excess·$4bn ACRA target", "third-party capital과 ratings headroom 가용.", "자본이 defensive use로 묶이면 반증.", "대형 reinsurance와 deployment가 이어졌다.", "성공", "gross capacity를 equity economics로 환산한다."), C("new-money ROA +40bp", "spread widening이 미래 earnings를 높인다.", "crisis reinvestment yield", "liability cost는 느리게 상승한다.", "credit loss가 spread pickup 초과면 반증.", "후속 earnings/strategic value를 지지했다.", "성공", "spread pickup은 loss-adjusted로 본다."), C("organic franchise", "retail sales +44% QoQ·record $7bn volume다.", "industry -4% 대비 share gain", "27% return estimate가 실제 cash ROE다.", "commission·pricing 후 IRR 하락이면 반증.", "franchise가 거래가치를 만들었다.", "성공", "sales growth와 cohort IRR을 같이 본다."), C("몇 년 내 double", "BVPS compound와 multiple 회복으로 +100%다.", "0.7x start·mid-teens ROE", "deal/repurchase가 per-share value를 보존.", "unfavorable exchange·APO de-rate면 반증.", "합병은 방향을 지지했으나 exact return 미복원.", "방향 성공", "corporate action 뒤 successor security까지 잇는다.")]),

    dict(id="797e8f52-79b4-42f8-87c1-94123103ce3d", date="2001-01-16", author="rich44", ticker="CIT", entity="CIT Group Inc.", group="cit", raw_short=True, direction="Long", entry="$20+", horizon="12~24개월", filename="analysis/ideas/2001/2001-01-16_CIT_long.md", link=None, desc=7809, cat=0,
         title="5.7x normal EPS와 takeout asymmetry Long", verdict="두 달 내 Tyco takeout으로 강한 성공", score=9.0, process=8.5,
         summary="raw Short지만 실제는 Long이다. $20 조금 넘는 가격에서 TBV $14.80, normalized EPS $3.55로 5.7x였고, recession downside $15~16 대비 upside $40+를 제시했다. telecom exposure는 $350m, 50% loss여도 $0.44/share로 제한적이며 Citigroup 같은 buyer가 $30을 지불해도 accretive하다고 봤다.",
         valuation="Downside EPS $1.60과 TBV가 $15~16 floor, normalized $3.55에 10~12x가 $35~43 upside다. M&A case는 $30에서도 buyer EPS accretive, synergy 포함 더 높은 가격 가능. 이 아이디어는 accounting cheapness보다 strategic buyer가 wholesale funding franchise를 더 높은 multiple로 재평가하는 event convexity가 핵심이다.",
         actual="게시 약 두 달 뒤인 2001년 3월 Tyco가 CIT를 약 $9.2bn 주식거래로 인수하기로 했다. 거래가치는 대략 주당 $35 수준으로 원문의 $30+ takeout과 $40 intrinsic range 사이에 들어왔다. horizon·catalyst·방향이 모두 맞은 강한 성공이다. 이후 Tyco가 CIT를 재상장한 사실은 최초 trade의 성공을 소급 취소하지 않는다.",
         price="SQL performance row는 없다. $20+ entry와 약 $35 transaction value를 비교하면 방향상 큰 이익이지만, 정확한 posting close·Tyco exchange ratio·closing까지의 배당을 복원하지 않아 공식 return/IRR은 null이다.",
         drivers="낮은 standalone multiple이 buyer에게 EPS accretion을 제공했고, factoring·equipment finance franchise와 scale synergy가 strategic value를 만들었다. 가장 빠른 catalyst가 business normalization보다 M&A였다는 점이 중요하다.",
         error="normalized EPS $3.55와 downside $1.60 사이의 credit-cycle bridge, Newcourt integration과 wholesale funding risk를 더 세밀하게 만들 수 있었다. takeout이 없을 때의 holding period와 stop rule도 부족했다.", first_signal="credit loss보다 funding spread가 먼저 악화하고 tangible equity return이 1991 저점 12.4% 아래로 내려가면 takeout 없는 standalone case를 낮춰야 했다.",
         metrics=[("Entry", "$20+", "$40+", "약 $35 deal value", "성공"),("TBV", "$14.80", "$15~16 downside", "takeout로 floor 상회", "성공"),("Normalized EPS", "$3.55", "10~12x", "strategic multiple", "성공"),("Telecom exposure", "$350m", "$0.44/share stress", "deal 전 치명손실 없음", "성공"),("Catalyst", "potential takeout", "$30+", "2001-03 Tyco", "강한 성공")],
         timeline=[("1999","Newcourt merger","discount 시작"),("2000-11","Citigroup/Associates precedent","M&A comp"),("2001-01-16","VIC Long","$20+"),("2001-03-13","Tyco deal 발표","약 $9.2bn"),("2001","거래 종결","takeout 실현"),("2002","Tyco가 CIT 재상장","후속 corporate event")],
         claims=[C("5.7x normalized earnings", "$3.55 EPS 대비 극저평가다.", "$20+ price", "normal earnings가 cycle에서 유지.", "loss·funding cost로 EPS $1.60 이하 지속.", "takeout이 discount를 빠르게 닫았다.", "성공", "financial multiple은 funding-normalized EPS로 본다."), C("TBV downside", "$14.80 book이 $15~16을 지지한다.", "historical 12.4% return", "assets와 funding이 orderly다.", "forced sale·liquidity run이면 반증.", "M&A가 floor 위에서 실현됐다.", "성공", "book floor는 going-concern funding 조건부다."), C("telecom fear 과도", "$350m exposure의 50% loss는 $0.44/share다.", "$56bn managed assets 대비 소액", "hidden vendor exposure가 없다.", "off-balance recourse 발견이면 반증.", "deal 전 핵심 impairment가 되지 않았다.", "성공", "headline exposure를 equity loss로 번역한다."), C("credit cycle 관리", "spread widening이 losses를 상쇄한다.", "1990s return history", "pricing power가 funding cost보다 빠르다.", "net margin·charge-off 동시 악화면 반증.", "짧은 event window에는 치명적 악화가 없었다.", "기간 성공", "asset spread와 liability spread를 분리한다."), C("buyer accretion", "Citigroup가 $30에도 EPS accretive다.", "Associates precedent", "규제·capital·integration이 허용된다.", "buyer multiple 하락·deal market 폐쇄면 반증.", "Tyco가 더 높은 가치로 제안했다.", "강한 성공", "M&A target은 buyer currency로 계산한다."), C("$40+ upside", "10~12x normal EPS가 가능하다.", "$3.55 earnings power", "standalone 또는 synergy가 materialize.", "takeout이 $30 아래면 target 미달.", "약 $35로 full target보다 낮지만 큰 수익.", "부분~성공", "intrinsic target과 deal-clearing price를 나눈다.")]),

    dict(id="671b2431-63fc-4542-98c7-62bbcd9189a3", date="2007-08-23", author="sag301", ticker="CIT", entity="CIT Group Inc.", group="cit", raw_short=True, direction="Long", entry="$35", horizon="12~24개월", filename="analysis/ideas/2007/2007-08-23_CIT_long.md", link="https://www.valueinvestorsclub.com/idea/CIT_Group/7407339140", desc=10950, cat=48,
         title="1x book·6.5x earnings와 liquidity buffer Long", verdict="wholesale funding collapse와 2009 bankruptcy로 대실패", score=3.5, process=6.0,
         summary="raw Short지만 실제는 Long이다. $35에서 약 1x book·1.2x tangible book, annualized H2 earnings 6.5x였고 normalized EPS $5.20~5.50에 10~12x를 기대했다. CP $6.2bn에 bank lines $7.5bn, ABS facilities $5.5bn, cash $5.2bn을 대응시켜 liquidity가 충분하다고 봤다.",
         valuation="Base $52~66는 normalized EPS $5.2~5.5×10~12x다. downside는 book/tangible book이 지지한다는 전제였다. 그러나 lender equity의 value는 earnings multiple보다 funding survival probability에 먼저 곱해져야 한다. `going-concern value × 생존확률 + restructuring recovery × 실패확률`로 바꾸면 CP·unsecured market closure가 valuation을 지배한다.",
         actual="신용위기 동안 wholesale funding access가 붕괴했고 asset sales·equity·TARP·bank holding company 전환도 common을 지키지 못했다. CIT는 2009-11-01 prepackaged Chapter 11을 신청했고 기존 common은 reorganization에서 취소됐다. 장기보유 common Long은 원금 전액 손실에 가까운 대실패다.",
         price="SQL performance row는 없지만 old common cancellation은 terminal payoff를 명확히 한다. exact 1/3/5년 return은 null로 두고 terminal common outcome은 약 -100%로 질적 판정한다.",
         drivers="손실을 만든 것은 예상보다 약한 normalized EPS가 아니라 liability-side run이었다. committed line의 covenant·draw 조건, collateral haircut과 ratings가 악화되면서 asset value가 있어도 시간을 살 수 없었다. liquidity buffer의 gross 합계가 fungible cash가 아니었다.",
         error="CP $6.2bn과 lines/ABS/cash를 단순 상계해 법적·운영상 가용성, 담보 중복, maturity clustering, ratings trigger를 빠뜨렸다. book value에 forced-sale haircut과 dilution waterfall도 부족했다.", first_signal="CP outstanding 감소가 business shrink가 아니라 시장 접근상실로 나타나고 secured funding 비중·haircut이 상승하는 순간 P/E thesis를 중단했어야 했다.",
         metrics=[("Entry", "$35", "$52~66", "old common cancelled", "대실패"),("Normalized EPS", "$5.2~5.5", "10~12x", "funding collapse", "무의미화"),("CP", "$6.2bn", "roll 가능", "시장 접근 악화", "실패"),("Bank lines", "$7.5bn", "liquidity cover", "제약·질 저하", "실패"),("Terminal", "going concern", "book recovery", "2009 Chapter 11", "대실패")],
         timeline=[("2007-07-17","home lending exit","$765m pretax mark"),("2007-08-23","VIC Long","$35"),("2008-03","secured funding 의존 상승","liability stress"),("2008-12","bank holding/TARP","emergency bridge"),("2009-07","FDIC guarantee 불발","first fatal signal"),("2009-11-01","Chapter 11 filing","common impairment"),("2009-12","재편 출구","old common 취소")],
         claims=[C("1x book 하방", "book가 equity를 지지한다.", "1.2x tangible", "assets가 orderly realization된다.", "forced-sale discount·funding run이면 반증.", "common은 취소됐다.", "대실패", "lender book은 liability duration과 함께 본다."), C("6.5x earnings cheap", "H2 earnings에 낮은 배수다.", "$5.2~5.5 normalized EPS", "funding cost가 정상화된다.", "spread보다 funding cost가 더 상승하면 반증.", "earnings claim은 liquidity에 종속됐다.", "실패", "survival probability가 P/E 앞에 온다."), C("lines가 CP를 덮는다", "$7.5bn lines>$6.2bn CP다.", "cash·ABS도 추가", "undrawn·unencumbered·조건 없는 가용성.", "covenant·collateral 중복이면 반증.", "gross liquidity가 common을 구하지 못했다.", "실패", "liquidity는 source-by-use matrix로 만든다."), C("diversification", "산업·asset·지역 분산이 losses를 제한한다.", "5개 segment", "상관이 stress에서도 낮다.", "funding shock가 전 segment를 묶으면 반증.", "liability shock가 diversification을 압도했다.", "실패", "asset diversification은 funding concentration을 상쇄 못한다."), C("home lending mark 충분", "$765m loss로 문제를 정리했다.", "held-for-sale transfer", "추가 discount·reps가 제한적.", "sale discount·other credit migration이면 반증.", "crisis는 더 넓고 길었다.", "실패", "one-time mark를 terminal loss로 착각하지 않는다."), C("10~12x rerating", "정상화하면 $52~66다.", "historical franchise multiple", "common 희석 없이 생존.", "emergency capital·restructuring이면 반증.", "기존 common이 소멸했다.", "대실패", "target 전에 capital waterfall을 확률가중한다.")]),

    dict(id="8530cf07-e131-4623-b20c-4b8cbcdd661a", date="2008-05-02", author="jna341", ticker="CIT", entity="CIT Group Inc.", group="cit", raw_short=True, direction="Long", entry="$11.79", horizon="3~6개월", filename="analysis/ideas/2008/2008-05-02_CIT_long.md", link=None, desc=21502, cat=255,
         title="0.58x adjusted TBV와 $15~18 sale catalyst Long", verdict="단기 liquidity 판단·sale catalyst 실패, bankruptcy로 terminal 대실패", score=3.0, process=6.5,
         summary="raw Short지만 실제는 Long이다. $11.79에서 Q1 tangible book의 0.45x, $1.5bn 희석증자 후 adjusted TBV의 0.58x였고 시장이 Bear Stearns식 bankruptcy를 과대평가한다고 봤다. 2009년까지 liquidity가 있고 rail portfolio 매각·회사 sale로 3~6개월 안에 $15~18을 기대했다.",
         valuation="Adjusted TBV의 0.58x에서 $15~18은 약 0.74~0.89x book recovery다. 그러나 $1.5bn equity raise가 runway를 늘리는 동시에 per-share claim을 희석했고, rail asset-sale gain도 unencumbered holdco cash인지 확인해야 했다. liquidation value는 face book이 아니라 stressed bid·funding unwind·senior claims 후 common recovery다.",
         actual="일부 자산매각과 bank holding company 전환, TARP $2.33bn에도 funding model은 회복되지 않았다. 2009년 FDIC guarantee 불발 뒤 CIT는 prepackaged Chapter 11에 들어갔고 old common은 취소됐다. '2009년까지 버틸 수 있다'는 timing과 3~6개월 sale catalyst 모두 실패했다.",
         price="SQL performance는 없다. old common cancellation을 terminal outcome으로 삼아 qualitative -100%에 가까운 실패로 판정하되, 중간 rebound와 정확한 holding-period return은 만들지 않는다.",
         drivers="자산 quality보다 confidence·funding cost·maturity가 먼저 common을 압박했다. equity raise와 asset sale은 gross liquidity를 제공했지만 secured creditors와 collateral needs 앞에서 충분한 permanent funding이 아니었다. buyer도 같은 financing tail을 인수해야 했기 때문에 $15~18 sale thesis가 약했다.",
         error="'Bear Stearns와 달리 시간이 있다'를 만기별 daily liquidity로 증명하지 못했고, committed facilities의 조건과 asset encumbrance를 과소평가했다. strategic sale 가격도 buyer funding cost·capital requirement를 반영하지 않았다.", first_signal="FDIC 지원 이전에도 secured funding 비중과 borrowing cost가 계속 오르고 unsecured maturities를 asset shrink로만 갚는다면 3~6개월 catalyst 실패로 즉시 손절해야 했다.",
         metrics=[("Entry", "$11.79", "$15~18", "old common cancelled", "대실패"),("P/adjusted TBV", "0.58x", "0.74~0.89x", "book recovery 없음", "실패"),("Equity raise", "$1.5bn", "2009 runway", "추가 구조조정 필요", "실패"),("Rail sale", "$4bn portfolio", "gain/liquidity", "common 보호 불충분", "부분"),("Catalyst", "company sale", "3~6개월", "Chapter 11", "실패")],
         timeline=[("2008-Q1","funding shock","TBV discount"),("2008-04","$1.5bn equity raise","희석·runway"),("2008-05-02","VIC Long","$11.79"),("2008-12","BHC·TARP $2.33bn","public bridge"),("2009-07","FDIC guarantee 불발","thesis break"),("2009-11-01","Chapter 11","terminal failure"),("2009-12","old common 취소","equity recovery 0")],
         claims=[C("0.58x TBV 과도", "bankruptcy/fire sale이 과대반영됐다.", "adjusted tangible book", "assets가 book 근처에 팔린다.", "haircut·encumbrance로 common recovery 0이면 반증.", "old common은 취소됐다.", "대실패", "stressed lender TBV는 recovery waterfall이다."), C("asset quality 양호", "누적 losses가 discount보다 작다.", "portfolio underwriting", "credit loss가 주요 위험이다.", "funding loss·forced sale이 credit를 앞서면 반증.", "liability crisis가 thesis를 압도했다.", "논점 미스", "자산이 좋아도 funding mismatch가 죽인다."), C("2009까지 liquidity", "추가 dilutive raise 없이 버틴다.", "$1.5bn equity·facilities", "maturity·collateral needs가 buffer 이내.", "unsecured market 폐쇄·haircut 상승이면 반증.", "TARP 뒤에도 Chapter 11로 갔다.", "실패", "runway는 월별 sources/uses로 계산한다."), C("rail sale catalyst", "$4bn portfolio가 gain과 cash를 낸다.", "salable hard assets", "proceeds가 holdco common에 가용.", "debt release·discount가 proceeds 흡수.", "sale만으로 common을 지키지 못했다.", "부분/실패", "asset sale gross와 net liquidity를 구분한다."), C("strategic sale $15~18", "well-capitalized buyer가 book discount를 산다.", "franchise·survival time", "buyer가 funding·capital tail을 감수.", "deal market 폐쇄면 반증.", "sale 대신 restructuring이었다.", "실패", "buyer universe와 financing certainty를 검증한다."), C("not Bear Stearns", "CIT에는 시간이 있다.", "longer-dated assets/liabilities", "time이 market reopening으로 이어진다.", "time 동안 cash burn·maturity가 누적되면 반증.", "시간은 equity가 아니라 creditors에 귀속됐다.", "실패", "runway는 value가 아닌 option expiry다.")]),
]


def add_remaining_athene():
    """Insert the 2019/2020 ideas already declared and return chronological order."""
    return sorted(IDEAS, key=lambda x: (x["date"], x["id"]))


def idea_sources(idea):
    raw = S("첨부 SQL 원문/metadata", idea["link"], "VIC_IDEAS(4).sql / VIC", idea["date"],
            f"idea_id·raw direction·description {idea['desc']} chars·catalyst {idea['cat']} chars", "원문")
    return [raw, *SOURCES[idea["group"]]]


def report(idea):
    raw = "Short" if idea["raw_short"] else "Long"
    actual = idea["direction"]
    claim_blocks = []
    claim_rows = []
    for n, (c, weight) in enumerate(zip(idea["claims"], WEIGHTS), 1):
        claim_blocks.extend([
            f"### C{n}. {c['title']} — {weight}%", "",
            f"- **원문 주장:** {c['original']}", f"- **T0 근거:** {c['evidence']}",
            f"- **숨은 가정:** {c['assumption']}", f"- **사전 반증조건:** {c['falsifier']}",
            f"- **실제:** {c['actual']}", f"- **판정:** **{c['verdict']}**", f"- **재사용 교훈:** {c['lesson']}", "",
        ])
        claim_rows.append(f"| C{n} | {c['title']} | {weight}% | {c['verdict']} | {c['lesson']} |")

    score = (idea["score"] + idea["process"]) / 2
    lines = [
        f"# {idea['entity']} — {idea['date']} — V9", "",
        f"> **Batch 046 canonical report.** Raw SQL `{raw}`를 원문 action/payoff로 감사해 **{actual}**으로 확정했다. Research as-of {ASOF}.", "", "---", "",
        "## 0. Idea Snapshot", "", "| 항목 | 내용 |", "|---|---|",
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |", f"| Idea ID | `{idea['id']}` |",
        f"| 게시일 / 작성자 | {idea['date']} / {idea['author']} |", f"| 원 SQL 방향 | {raw} |",
        f"| 원문 검증 방향 | **{actual}** |", f"| 기준가격 | {idea['entry']} |", f"| 원 horizon | {idea['horizon']} |",
        f"| 최종 판정 | **{idea['verdict']}** |", "",
        f"> **결론:** {idea['summary']} 결과적으로 **{idea['verdict']}**.", "", "---", "",
        "## 1. 회사는 정확히 무엇을 하는가", "", BUSINESS[idea["group"]], "",
        "### Common equity cash waterfall", "",
        "회계이익에서 운전자본·담보·규제자본·maintenance/growth investment·interest·tax를 차감하고, common보다 선순위인 계약·채권자 청구권을 먼저 배치한다. "
        "자산가치와 계약상 수취액은 현금화 날짜·세금·재투자 의무를 반영한다. 기업가치가 맞아도 security와 duration이 틀리면 투자결과는 실패할 수 있다.", "",
        "### 분기/사건별 KPI", "",
        "- 원문 핵심 unit economics와 실제 현금전환\n- funding·regulatory capital·unencumbered liquidity\n- per-share book/EPS와 share count\n- catalyst gate, 예상일·실제일·실패조건\n- target multiple과 successor security를 포함한 terminal payoff", "", "---", "",
        "## 2. 당시 상황과 시장이 가격에 넣은 것", "", idea["summary"], "",
        "### Reverse expectations", "",
        f"{idea['entry']}가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.", "", "---", "",
        "## 3. 원문 투자논지 지도", "", *claim_blocks, "---", "",
        "## 4. 당시 Valuation과 Payoff Structure", "", idea["valuation"], "",
        "### 시나리오 구조", "", "| 시나리오 | 필요한 조건 | common payoff |", "|---|---|---|",
        f"| Bear | 첫 반증조건 발생·funding/capital 악화 | {actual} 손실, duration 확대 또는 recovery 훼손 |",
        "| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |",
        f"| Bull | operating claim·capital·catalyst가 동시에 실현 | {idea['verdict']}의 상단, 단 exact return은 별도 검증 |", "",
        "### 핵심 수치 감사", "", "| 지표 | T0 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|",
        *["| " + " | ".join(row) + " |" for row in idea["metrics"]], "", "---", "",
        "## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인", "", "| 날짜 | 사건 | 논지에 미친 의미 |", "|---|---|---|",
        *["| " + " | ".join(row) + " |" for row in idea["timeline"]], "", "### 실제 사업·자본구조", "", idea["actual"], "", "---", "",
        "## 6. 실제 투자결과 — 방향 교정과 가격 경로", "", idea["price"], "",
        "이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.", "", "---", "",
        "## 7. Claim별 사후 판정", "", "| Claim | 내용 | Weight | 판정 | 재사용 교훈 |", "|---|---|---:|---|---|", *claim_rows, "",
        f"가중치 합계는 {sum(WEIGHTS)}%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.", "", "---", "",
        "## 8. 무엇이 실제 수익 또는 손실을 만들었는가", "", idea["drivers"], "",
        "### 인과 분해", "",
        "1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.\n2. 이후 새로 발생한 macro·regulation·management event를 분리한다.\n3. 기업 결과와 common security payoff를 구분한다.\n4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.", "",
        "### Counterfactual", "", f"핵심 catalyst가 없었어도 {idea['entry']}에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.", "", "---", "",
        "## 9. 분석 오류 유형과 최초 경고", "", idea["error"], "", "### 최초 관찰 가능한 경고/반증", "", idea["first_signal"], "",
        "### 사후편향 방지", "", "최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.", "", "---", "",
        "## 10. 재사용 가능한 교훈과 다음 분석 체크리스트", "",
        f"1. **Entity audit:** `ATH`를 회사로 보지 말고 {idea['entity']} 법인·exchange·날짜로 고정한다.\n2. **Direction audit:** raw {raw}가 아니라 원문 payoff를 읽어 {actual}을 확정한다.\n3. **Bridge:** target을 EPS/book/NAV와 cash waterfall로 연결한다.\n4. **Falsifier:** 최초 경고에 날짜와 수치를 둔다.\n5. **Path:** 원 horizon과 terminal event를 섞지 않는다.\n6. **Missing data:** SQL performance가 없으면 null을 유지한다.", "",
        "### 다시 분석한다면", "", "- legal/capital/funding gate를 확률·날짜별로 나눈다.\n- gross asset value와 common에 귀속되는 순가치를 분리한다.\n- base/bull target뿐 아니라 survival/recovery case를 수치화한다.\n- corporate action 이후 교환비율·배당·successor price를 연결해 total return을 복원한다.\n- event가 맞아도 price target이 실패할 수 있도록 exit/cover rule을 미리 쓴다.", "", "---", "",
        "## 11. 최종 Scorecard", "", "| 평가축 | 판정 |", "|---|---|", f"| Entity / direction | raw {raw} → **{actual}**, {idea['entity']} |",
        f"| Business thesis | {idea['claims'][1]['verdict']} |", f"| Valuation thesis | {idea['metrics'][0][4]} |", f"| Catalyst / timing | {idea['verdict']} |",
        f"| Thesis score | {idea['score']:.1f}/10 |", f"| Process score | {idea['process']:.1f}/10 |", f"| Outcome-adjusted score | {score:.1f}/10 |", "",
        "### 한 문장 교훈", "", f"> {idea['claims'][0]['lesson']}", "", "---", "", "## 12. Sources / Validation Notes", "",
    ]
    for n, src in enumerate(idea_sources(idea), 1):
        label = f"[{src['title']}]({src['url']})" if src["url"] else src["title"]
        lines.append(f"{n}. {label} — {src['publisher']}, {src['date']}. {src['evidence']}")
    lines.extend(["", "### 데이터 품질", "",
                  "- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.",
                  "- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.",
                  "- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
                  f"- 교정: ticker={idea['ticker']}, entity={idea['entity']}, raw={raw}, research={actual}.", ""])
    return "\n".join(lines)


def make_payload(ideas):
    keys = ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")
    out = {"schema_version": "vic-deep-research-v9", "batch": 46,
           "title": "Anthem / Athabasca Oil / Athene / CIT — Entity, Direction, Capital and Event V9",
           "research_asof": ASOF, **{key: [] for key in keys}}
    for idea in ideas:
        raw_ko = "숏" if idea["raw_short"] else "롱"
        out["ideas_master"].append({
            "idea_id": idea["id"], "date": idea["date"], "year": int(idea["date"][:4]), "ticker": idea["ticker"],
            "company_name": idea["entity"], "author": idea["author"], "direction_ko": raw_ko,
            "is_short": int(idea["raw_short"]), "contest_winner": 0, "source_link": idea["link"],
            "description_chars": idea["desc"], "catalyst_chars": idea["cat"],
            "narrative_tags_ko": "entity_collision; direction_audit; capital_structure; valuation; catalyst; path_dependency",
            "idea_type_ko": "기업가치/특수상황", "horizon_raw": idea["horizon"], "horizon_months": None,
            "performance_available": 0, "idea_return_1y": None, "idea_return_3y": None, "idea_return_5y": None,
            "auto_tag_status_ko": "raw metadata 보존·원문 entity/direction 수동검증 완료",
            "perf_1m": None, "perf_3m": None, "perf_6m": None, "perf_1y": None, "perf_2y": None, "perf_3y": None, "perf_5y": None})
        out["postmortems"].append({
            "idea_id": idea["id"], "ticker": idea["ticker"], "research_direction_ko": idea["direction"],
            "company_description_ko": BUSINESS[idea["group"]], "original_thesis_ko": idea["summary"], "actual_development_ko": idea["actual"],
            "thesis_verdict_ko": idea["verdict"], "business_verdict_ko": idea["claims"][1]["verdict"],
            "catalyst_verdict_ko": idea["verdict"], "valuation_verdict_ko": idea["metrics"][0][4], "stock_verdict_ko": idea["price"],
            "current_verdict_ko": idea["verdict"], "overall_verdict_ko": idea["verdict"], "why_ko": idea["drivers"],
            "success_pattern_ko": "direction_correction; expectation_gap; contract_event; book_compounding; strategic_value",
            "failure_pattern_ko": "ticker_collision; funding_run; gross_nav; duration; capital_waterfall; path_dependency",
            "root_error_ko": idea["error"], "first_signal_ko": idea["first_signal"], "first_signal_date": idea["timeline"][2][0],
            "knowable_at_t0_ko": idea["claims"][0]["evidence"] + "; " + idea["claims"][0]["falsifier"],
            "avoidability_ko": "중간 이상. 원문 direction·entity·현금/자본 waterfall과 사전 반증조건으로 상당 부분 방지 가능.",
            "counterfactual_question_ko": f"핵심 catalyst 없이도 {idea['entry']}에서 충분한 expected return이 남았는가?",
            "analyst_note_ko": f"raw {'Short' if idea['raw_short'] else 'Long'} 보존; 실제 {idea['direction']}; entity={idea['entity']}",
            "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None, "confidence": 0.90,
            "research_asof": ASOF, "research_status_ko": "SQL 원문·공식 사건 검증 완료; performance row 부재로 exact return 미산출"})
        out["meta"].append({"idea_id": idea["id"], "analysis_depth_ko": "기업·현금엔진·T0 기대·6개 weighted claim·valuation·timeline·성과·first break·counterfactual 장문분석",
                            "report_version": "V9-canonical", "thesis_type_ko": idea["title"], "one_line_verdict_ko": idea["summary"],
                            "thesis_score": idea["score"], "process_score": idea["process"], "return_summary_ko": idea["price"],
                            "core_error_ko": idea["error"], "core_insight_ko": idea["claims"][0]["lesson"], "research_asof": ASOF})
        for n, (title, body) in enumerate([
            ("회사·가치사슬·현금엔진", BUSINESS[idea["group"]]), ("T0 기대·reverse expectations", idea["summary"]),
            ("Valuation·payoff·실제경로", idea["valuation"] + "\n\n" + idea["price"]),
            ("사후인과·오류·교훈", idea["drivers"] + "\n\n" + idea["error"])], 1):
            out["sections"].append({"idea_id": idea["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, (c, weight) in enumerate(zip(idea["claims"], WEIGHTS), 1):
            out["claims"].append({"idea_id": idea["id"], "claim_order": n, "claim_title_ko": c["title"], "thesis_weight_pct": weight,
                                  "original_claim_ko": c["original"], "t0_evidence_ko": c["evidence"], "key_assumption_ko": c["assumption"],
                                  "ex_ante_falsifier_ko": c["falsifier"], "actual_result_ko": c["actual"], "quantitative_gap_ko": c["actual"],
                                  "verdict_ko": c["verdict"], "analytical_error_ko": idea["error"], "reusable_lesson_ko": c["lesson"]})
        for n, row in enumerate(idea["metrics"], 1):
            out["metrics"].append({"idea_id": idea["id"], "metric_order": n, "metric_name_ko": row[0], "t0_value_ko": row[1],
                                   "thesis_expectation_ko": row[2], "actual_value_ko": row[3], "verdict_ko": row[4],
                                   "interpretation_ko": "T0와 actual을 같은 단위로 비교하고 불가능한 수익률은 null로 유지."})
        for n, row in enumerate(idea["timeline"], 1):
            out["timeline"].append({"idea_id": idea["id"], "event_order": n, "event_date_ko": row[0], "event_ko": row[1], "thesis_implication_ko": row[2]})
        for n, src in enumerate(idea_sources(idea), 1):
            out["sources"].append({"idea_id": idea["id"], "source_order": n, "source_type_ko": src["kind"], "publisher": src["publisher"],
                                   "title_ko": src["title"], "source_date": src["date"], "url": src["url"], "evidence_ko": src["evidence"]})
    return out


def make_index(ideas):
    rows = []
    for n, idea in enumerate(ideas, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['entity']} | {raw}→**{idea['direction']}** | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 046 — Anthem / Athabasca Oil / Athene / CIT — V9 Index", "",
        f"> **Research as-of:** {ASOF}. 첨부 `VIC_IDEAS(4).sql`의 원문을 기준으로 entity와 direction을 수동 교정했다. SQL performance row가 없는 10건의 수익률은 만들지 않았다.", "",
        "## 0. 배치 결론", "",
        "이번 배치는 데이터 정규화가 투자분석보다 먼저라는 대표 사례다. 원 ticker `ATH`는 2002 Anthem, 2011/2013 Athabasca Oil, 2017~2020 Athene Holding의 세 법인을 뜻한다. raw Short 9건 중 실제 Short는 2017 Athene 한 건뿐이며, 나머지는 원문 payoff가 모두 Long이다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | 실제 회사 | raw→연구 방향 | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|", *rows, "",
        "## 2. 기업별 투자논지", "", "### Anthem — margin과 network scale", "",
        "2002 Long은 14x EPS와 4% 미만 margin에서 peer 수준 16x·5%로의 이중 정상화를 샀다. MLR·pricing·통합위험이 있었지만 2004 WellPoint 결합으로 전국 Blue 네트워크의 전략가치는 확인됐다.", "",
        "### Athabasca — 계약상 cash와 개발 NAV를 분리", "",
        "2011·2013 두 Long 모두 PetroChina put이 hard catalyst였다. put 현금화는 성공했지만 gross resource NAV는 capex·기술·승인·oil price·시간을 거쳐야 했다. 계약상 현금 성공을 C$20~22 또는 C$10~15의 지속적 equity value 성공으로 바꾸면 안 된다.", "",
        "### Athene — 가격에 따라 Short에서 Long으로", "",
        "2017 Short는 1.6x book premium의 압축을 맞혔으나 $33·40% downside는 실패했다. 2018 Long은 1~2년 path에서 손실, 2019·2020 Long은 5x earnings·0.8/0.7x book에서 capital survival과 Apollo 합병을 포착해 성공했다. 같은 business risk도 entry multiple과 capital buffer가 direction을 바꾼다.", "",
        "### CIT — 자산가치보다 liability clock", "",
        "2001 Long은 $20+에서 takeout accretion을 계산했고 두 달 뒤 Tyco 거래로 성공했다. 2007·2008 Long은 book·normalized EPS와 gross liquidity를 믿었지만 wholesale funding run을 놓쳐 2009 bankruptcy와 old common cancellation로 실패했다.", "",
        "## 3. 배치 공통 교훈", "",
        "1. **Ticker는 entity가 아니다.** 법인·exchange·날짜·business description으로 먼저 resolve한다.\n2. **Direction은 raw flag가 아니라 payoff다.** target 상승·현금수취·rerating이면 Long이다.\n3. **Cash/NAV/book는 common floor가 아니다.** timing, capex, funding, senior claims와 use-of-cash를 차감한다.\n4. **Event 성공과 투자 성공을 분리한다.** put·합병·인수가 일어나도 exact return은 별도다.\n5. **Funding은 lender P/E보다 앞선다.** gross lines가 아니라 가용성·담보·만기별 sources/uses를 본다.\n6. **성과값이 없으면 null이다.** terminal event를 임의의 1/3/5년 수익률로 바꾸지 않는다.", "",
        "## 4. 데이터·앱 산출물", "",
        "- DB payload: `data/curated/batch_046_anthem_athabasca_athene_cit_deep_v7.json`\n- Streamlit wrapper: `analysis/batch_046_anthem_athabasca_athene_cit_10.md`\n- SQL source packet: `data/curated/batch_046_source_packet.json`\n- Builder: `scripts/46_build_batch_046_v9.py`", "",
        "## 5. 검증 기준", "",
        "10개 보고서 모두 0~12절, 6개 claim/100% weight, 5개 metric, 최소 6개 event와 원문+공식자료 source를 포함한다. Payload·문서·앱 popup의 entity, direction, verdict를 동일하게 유지한다.", "",
    ])


def main():
    ideas = add_remaining_athene()
    if len(ideas) != 10 or len({i["id"] for i in ideas}) != 10:
        raise ValueError("Batch 046 requires ten unique idea units")
    for idea in ideas:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or sum(WEIGHTS) != 100:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(i["filename"]).relative_to("analysis").as_posix() for i in ideas]
    wrapper = "# Batch 046 — Anthem / Athabasca Oil / Athene / CIT V9\n\n" + \
              f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + \
              "> Streamlit 호환 wrapper다. canonical index: [Batch 046 V9 Index](batch_046_v9_index.md).\n"
    (ROOT / "analysis/batch_046_anthem_athabasca_athene_cit_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_046_v9_index.md").write_text(make_index(ideas), encoding="utf-8")
    payload = make_payload(ideas)
    (ROOT / "data/curated/batch_046_anthem_athabasca_athene_cit_deep_v7.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {"batch": "046", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql", "record_count": 10,
              "direction_audit": "complete", "performance_rule": "no performance row; exact returns remain null",
              "candidates": [{"idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"],
                              "author": i["author"], "raw_direction": "Short" if i["raw_short"] else "Long",
                              "research_direction": i["direction"], "performance_available": False,
                              "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None,
                              "canonical_report": i["filename"]} for i in ideas]}
    (ROOT / "data/curated/batch_046_source_packet.json").write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql",
        "attachment_bytes_checked": 122499072,
        "records_selected": 10,
        "raw_descriptions_verified": 10,
        "performance_rows_found": 0,
        "note": "첨부 SQL와 선행 raw extract를 함께 감사했다. exact return은 performance row 부재로 null 유지.",
    }
    (ROOT / "data/curated/batch_046_sql_inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ideas={len(payload['ideas_master'])} postmortems={len(payload['postmortems'])} sections={len(payload['sections'])} "
          f"claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
