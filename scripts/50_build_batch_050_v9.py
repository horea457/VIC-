#!/usr/bin/env python3
"""Build Batch 050 McDermott / Mohawk Industries canonical V9 artifacts."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-10"
spec = importlib.util.spec_from_file_location("batch46", ROOT / "scripts/46_build_batch_046_v9.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.ASOF = ASOF


m.BUSINESS.update({
    "mdr50": (
        "McDermott는 해양·육상 에너지 인프라를 설계·조달·제작·설치하는 EPCI contractor다. 경제엔진은 "
        "`계약가격 + 승인 change order - 최신 estimate-at-completion - 지체상금 - 남은 운전자본 - SG&A·이자·세금`이다. "
        "percentage-of-completion 회계에서는 원가추정이 나빠지면 남은 예상손실을 즉시 인식하므로 backlog 금액은 자산이 아니라 "
        "미확정 margin exposure다. Common에는 project cash burn·letter of credit·담보부채를 모두 통과한 잔여가치만 귀속되고, "
        "무담보채에는 reorganized EV에서 DIP·담보·우선청구권을 뺀 recovery가 귀속된다."
    ),
    "mhk50": (
        "Mohawk Industries는 carpet, ceramic tile, laminate·wood·luxury vinyl tile을 제조·유통하는 글로벌 flooring 업체다. "
        "현금엔진은 `주택신축·기존주택거래·remodel·commercial 물량 × price/mix - 원재료·freight·labor - 미가동 고정비 - "
        "SG&A - maintenance/growth capex ± 운전자본`이다. 전국 유통망, 수직계열화, Dal-Tile·Unilin·Marazzi와 기술·브랜드는 "
        "moat지만, 큰 고정비 때문에 utilization과 가격-원가 시차가 margin을 크게 흔든다. 좋은 franchise와 좋은 cycle entry는 "
        "별개의 claim이며 starts·turnover·remodel은 서로 다른 lag로 flooring 수요에 들어온다."
    ),
})


m.SOURCES.update({
    "mdr50": [
        m.S("McDermott FY2013 Form 10-K", "https://www.sec.gov/Archives/edgar/data/708819/000119312514062722/d638164d10k.htm", "SEC / McDermott", "2014-02", "2013 매출 약 $2.7bn, backlog 약 $4.8bn, project charges와 손실계약"),
        m.S("McDermott historical investor materials", "https://www.sec.gov/Archives/edgar/data/708819/000119312518091352/d520888dex991.htm", "SEC / McDermott", "2018-03", "2013년말 9개 loss-making projects와 turnaround bridge"),
        m.S("McDermott 2018 Form 10-K filing archive", "https://www.sec.gov/edgar/browse/?CIK=708819&owner=exclude", "SEC / McDermott", "2018-2019", "CB&I 결합, project EAC, 부채·유동성과 10.625% notes"),
        m.S("McDermott prepackaged restructuring", "https://www.mcdermott.com/press-release-detail/122728/mcdermott-international-inc-announces-comprehensive-prepackaged-restructuring-transaction-to-de-lever-balance-sheet-and-immediately-position-company-for-long-term-growth", "McDermott", "2020-01-21", "Chapter 11, 약 $4.6bn debt 제거와 funded debt equitization"),
        m.S("McDermott restructuring completion", "https://www.mcdermott.com/press-release-detail/122716/mcdermott-successfully-completes-comprehensive-restructuring-process", "McDermott", "2020-06-30", "기존 capital structure의 terminal event와 재편 완료"),
    ],
    "mhk50": [
        m.S("Mohawk SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=851968&owner=exclude", "SEC / Mohawk Industries", "1993-2026", "2007·2009·2013을 포함한 공시, segment·housing exposure·인수·재무제표 검증"),
        m.S("Mohawk annual-report archive", "https://ir.mohawkind.com/financial-information/annual-reports", "Mohawk Industries", "2016-2025", "공식 연차보고서와 segment·margin·capex·현금흐름 검증"),
        m.S("Mohawk 2018 Annual Report", "https://ir.mohawkind.com/static-files/250e3467-50b7-4c7c-8397-67d515deb533", "Mohawk Industries", "2019", "2018 input inflation, 신규 capacity, segment performance와 현금흐름"),
        m.S("Mohawk 2020 Annual Report", "https://ir.mohawkind.com/static-files/2b4eadfe-e050-4730-8b81-9bee20337b1e", "Mohawk Industries", "2021", "COVID 수요·housing recovery, LVT·segment와 cash conversion"),
        m.S("Mohawk 2021 Annual Report", "https://ir.mohawkind.com/static-files/b52bf971-5f8d-4827-819b-159436d035d6", "Mohawk Industries", "2022", "2021 price-cost·margin·capacity와 2022 출발점"),
        m.S("Mohawk 2024 Annual Report", "https://ir.mohawkind.com/static-files/47e34730-dfeb-446f-aa1f-9d7f2c345bbb", "Mohawk Industries", "2025", "$9.70 adjusted EPS, $680m FCF, $10.8bn sales와 2022~24 수요수축"),
    ],
})


PERF = {
    "57ac591e-b624-407a-be54-18ea0ef94ae0": {"1m": .8775613458133062, "3m": .8431570958765494, "6m": .903870478117885, "1y": .4549709081710093, "2y": .5618517581583607, "3y": .7318492284341006, "5y": 1.0383253225398432},
    "02425766-dadd-41c8-84e5-1574f17fd988": {"1m": .8048037889039242, "3m": 1.3487821380243572, "6m": 1.527063599458728, "1y": 1.5761163734776726, "2y": 2.006089309878214, "3y": 2.2374830852503385, "5y": 4.896143437077131},
    "9677bae5-283c-498f-b8e1-c0f32c865ddb": {"1m": 1.0756390690576114, "3m": 1.1222815719191148, "6m": 1.2058374666157954, "1y": 1.3833460511255247, "2y": 1.5821251430751622, "3y": 1.4477298740938573, "5y": 2.5530331934376194},
    "23387e45-c762-4f66-9eb0-cb1fdf4e38e2": {"1m": 1.043114451850801, "3m": 1.0177279818465466, "6m": .962345766557935, "1y": 1.117571975606297, "2y": 1.3489575946674228, "3y": 1.4272443625017728, "5y": .8508013047794639},
    "b39c46a3-43b6-4dd1-a244-5c355b80e618": {"1m": 1.0167352831096614, "3m": .7042185745602311, "6m": .6725658985189542, "1y": .6321980430946906, "2y": .4247981607228787, "3y": 1.040474790140619},
    "4bc970f8-09ad-43c8-847c-baf292216a29": {"1m": 1.1955339805825242, "3m": 1.464757281553398, "6m": 1.9816504854368933, "1y": 1.8037864077669903, "2y": .9344660194174758},
    "20752c4b-0a92-4e7b-8379-f2d2384b6f06": {"1m": .9096271691197526, "3m": .7795086192085219, "6m": .6897084932134471, "1y": .561021705515148},
}


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**idea):
    idea["claims"] = [C(*row) for row in idea.pop("claimdata")]
    idea.setdefault("security", "Common equity")
    idea.setdefault("waterfall", "Common 가치는 영업현금에서 운전자본·capex·이자·세금과 선순위 청구권을 뺀 잔여다. 자산·backlog·book value를 그대로 주당 floor로 쓰지 않는다.")
    return idea


IDEAS = [
    I(id="01aae406-cb89-4ef2-9972-a2cdf7c7d53c", date="2013-10-14", author="fiftycent501", ticker="MDR", entity="McDermott International, Inc.", group="mdr50", raw_short=False, direction="Long", security="Common equity", entry="원문 약 $6~7대", horizon="2~3년", filename="analysis/ideas/2013/2013-10-14_MDR_long.md", link="https://www.valueinvestorsclub.com/idea/MCDERMOTT_INTL_INC/5025002655", desc=0, cat=126,
      title="문제계약 burn-off·asset floor·$600m EBITDA 정상화 Long", verdict="실패 — 반복 EAC 손실과 offshore downturn이 asset floor·정상화 clock을 깨뜨림", score=3.8, process=7.3,
      summary="2012 Long의 재도전이다. 연속 project charge로 주가가 약 40% 하락한 $6~7대에서 나쁜 backlog가 12~15개월 안에 소진되고 Atlantic 구조조정·새 수주 discipline·신규 vessel이 2014~15 margin을 회복시킨다고 봤다. fleet·yard·net cash로 $8.50~11.15, 정상 EBITDA 약 $675m에 7x를 주면 약 $21이라는 Long이었다.",
      valuation="원문은 physical fleet·yard와 net cash를 합쳐 $8.50~11.15/share, 약 $4bn revenue와 정상 margin에서 EBITDA 약 $675m, 7x를 적용해 약 $21을 계산했다. 그러나 EPCI SOTP는 remaining project loss, unapproved change order, vessel idle cost, working-capital deficit와 LC 필요액을 먼저 차감해야 한다. 12~15개월 burn-off와 oil-cycle 회복을 동시에 놓은 것이 가장 큰 중복 낙관이었다.",
      actual="FY2013 매출은 약 $2.7bn, 연말 backlog는 약 $4.8bn이었지만 net loss는 약 $509m였고 후속 자료는 2013년말 9개 loss-making project를 제시했다. CEO 교체와 구조조정 뒤 일부 회복은 있었으나 oil capex 붕괴까지 겹쳐 원 horizon의 clean normalization은 나오지 않았다. 2015년 주가가 $2대로 하락해 자산 floor도 반증됐다.",
      price="이 idea에는 repository performance row가 없다. 원문 서술가격·2015년 $2대 저점은 thesis 경로 검증에만 사용하며 1/3/5년 exact return과 IRR은 null이다.",
      drivers="손실의 첫 원인은 유가가 아니라 fixed-price 입찰·EAC 통제였다. loss project가 하나씩 끝나도 새 charge가 생겼고, 이후 offshore capex 하락이 vessel utilization과 신규 backlog margin을 추가로 압박했다. 유형자산은 distress에서 즉시 현금화 가능한 common floor가 아니었다.",
      error="개별 bad project를 finite inventory로 보고 반복되는 bidding·execution process failure를 구조문제로 다루지 않았다. asset value에서 project liabilities·idle cost·LC를 빼지 않았고, 2014~15 operational fix와 industry upcycle을 같은 base case에 쌓았다.",
      first_signal="quarterly EAC revision과 loss-making project 수가 2개 분기 연속 줄지 않거나, 새 backlog award margin이 공개되지 않은 채 working-capital cash burn이 지속되는 순간 $8.50 floor와 $675m EBITDA를 폐기했어야 했다.",
      metrics=[("Entry / asset value", "$6~7대", "$8.50~11.15", "2015 $2대 저점", "실패"), ("Revenue", "약 $4bn 정상화 가정", "margin 회복", "FY2013 약 $2.7bn", "미달"), ("EBITDA", "약 $675m 정상", "2014~15", "2013 adjusted EBITDA 큰 음수", "실패"), ("Loss projects", "12~15개월 burn-off", "지속 감소", "2013년말 9개", "실패"), ("Backlog", "quality 개선", "profitable conversion", "FY2013 약 $4.8bn이나 손실", "금액 무의미")],
      timeline=[("2012-01", "선행 VIC MDR Long", "동일 burn-off 논지"), ("2013-10-14", "재도전 VIC Long", "$6~7대·$21 bull"), ("2013-12", "David Dickson CEO 선임", "management reset"), ("2013-12", "9개 loss-making projects", "finite-project 가정 반증"), ("2014", "Atlantic 구조조정", "비용조치"), ("2014~2015", "offshore capex 급락", "cycle 역풍"), ("2015", "주가 $2대", "asset floor 파괴"), ("2018", "CB&I 결합", "새 liability 확대")],
      claimdata=[("12~15개월 burn-off", "기존 문제계약이 끝나면 earnings가 정상화된다.", "특정 프로젝트의 예정 완공일", "새 수주·EAC process는 이미 개선됐다.", "loss-project 수·charge가 두 분기 연속 안 줄면 반증.", "2013년말에도 9개 loss project였다.", "실패", "반복 사고면 자산이 아니라 process를 조사한다."), ("backlog quality 개선", "신규 수주는 과거보다 좋은 margin이다.", "경영진의 bidding discipline", "공시되지 않은 award margin이 충분하다.", "신규 project charge 발생 시 반증.", "후속 EAC 손실이 계속됐다.", "실패", "backlog dollar를 margin backlog로 바꾼다."), ("Atlantic 구조조정", "고질적 지역손실을 제거한다.", "Morgan City 축소와 조직개편", "절감액이 idle·실행손실보다 크다.", "segment breakeven 미달 지속 시 반증.", "비용조치는 있었으나 전사손실을 못 막았다.", "부분", "cost-out과 risk-process fix를 구분한다."), ("fleet asset floor", "fleet·yard·cash가 $8.50~11.15를 지지한다.", "replacement/SOTP", "orderly sale·높은 utilization이 가능하다.", "주가가 floor 아래에서 오래 거래되면 반증.", "2015 $2대까지 하락했다.", "실패", "특수자산은 utilization·liability 후 순가치다."), ("$675m 정상 EBITDA", "$4bn revenue와 정상 margin으로 가능하다.", "과거 수익성", "시장·입찰·실행이 동시에 정상화된다.", "2014~15 margin bridge 미달이면 반증.", "원 horizon에 실현되지 않았다.", "실패", "cycle과 self-help를 독립 sensitivity로 둔다."), ("M&A option", "strategic buyer가 가치를 실현한다.", "fleet·regional position", "buyer가 project tail을 감수한다.", "liability 때문에 buyer가 없으면 반증.", "near-term takeout은 없었다.", "미실현", "M&A는 buyer의 liability-adjusted EV로 계산한다.")]),

    I(id="5f965311-0ef7-42b1-ba47-39d191d66ddc", date="2018-01-04", author="sidhardt1105", ticker="MDR", entity="McDermott International, Inc. / CB&I combination", group="mdr50", raw_short=False, direction="Long", security="Common equity", entry="합병 발표 후 MDR 약 한 자릿수", horizon="1~3년", filename="analysis/ideas/2018/2018-01-04_MDR_CBI_merger_long.md", link=None, desc=11428, cat=310,
      title="CB&I scrubbed liabilities·$250m+ synergy·turnaround playbook Long", verdict="강한 실패 — acquired project liabilities와 leverage가 synergy를 압도, 20개월 뒤 Chapter 11", score=1.5, process=6.6,
      summary="MDR을 되살린 David Dickson이 distressed CB&I도 되살릴 수 있다는 merger Long이다. CB&I가 Q3 charge와 MDR due diligence로 두 번 derisk됐고, 약 6.25x 2018 EBITDA·Technology business $2.5bn bid를 반영하면 RemainCo는 3.5x 미만, $250m synergy도 50~100% 상회할 수 있다고 봤다. Base $10~11 1년, $20+ 2~3년이었다.",
      valuation="원문은 pro forma LTM adjusted EBITDA $1bn+, net income $534m, closing funded debt 약 $3.3bn(2.6x gross/2.2x net)을 사용했다. $250m synergy를 더하면 약 5.6x EV/EBITDA라고 봤다. 하지만 acquired EPC의 경제적 순부채는 funded debt뿐 아니라 loss contract의 남은 cash-to-complete, negative working capital, LC와 restructuring cash cost를 포함한다.",
      actual="2018-05 combination이 종결됐지만 같은 해 하반기 Cameron·Freeport LNG 등 cost estimate가 다시 크게 늘었다. synergy guidance 증가는 일부 실현됐어도 cash project loss와 차입비용을 못 이겼다. 2019 superpriority financing과 forbearance를 거쳐 2020-01-21 prepackaged Chapter 11을 신청했고 약 $4.6bn debt를 제거하는 과정에서 기존 common은 보존되지 않았다.",
      price="MDR common의 exact SQL performance row가 없어 1/3/5년 수익률은 null이다. 다만 1년 $10~11·2~3년 $20+ 목표와 달리 2020 restructuring에서 기존 common의 경제적 가치가 소멸한 terminal outcome은 강한 실패로 별도 기록한다.",
      drivers="손실은 synergy 미달 하나가 아니라 inherited contract liability의 크기와 timing에서 왔다. CB&I의 과거 charge를 final loss estimate로 봤고, MDR의 standalone turnaround를 더 크고 다른 onshore LNG portfolio에 외삽했다. leverage가 높아진 상태에서 작은 EAC revision도 liquidity spiral을 만들었다.",
      error="management quality를 계약별 downside underwriting의 대체물로 사용했다. Technology business auction value와 RemainCo EBITDA를 합치면서 sale tax·separation cost·loss contracts를 충분히 차감하지 않았고, 2.2x net debt에 off-balance project cash need를 넣지 않았다.",
      first_signal="합병 후 첫 두 분기 안에 acquired project EAC·contract liability·negative working capital이 due-diligence base보다 악화하거나 asset sale이 deleveraging이 아니라 liquidity funding에 쓰이면 $20+ case를 폐기했어야 했다.",
      metrics=[("Entry / targets", "한 자릿수", "$10~11 1Y / $20+", "2020 old common impaired", "강한 실패"), ("Pro forma EBITDA", "$1bn+", "synergy 포함 확대", "project charges가 압도", "실패"), ("Cost synergy", "$250m", "50~100% upside", "guide 증액에도 liquidity 악화", "논점 미스"), ("Closing debt", "$3.3bn", "2.2x net", "superpriority financing 필요", "과소측정"), ("CB&I price", "6.25x 2018E EBITDA", "<3.5x ex-Tech", "liability-adjusted multiple 무의미", "실패")],
      timeline=[("2017-10", "CB&I Q3 charges", "첫 derisk 주장"), ("2017-12", "all-stock combination 발표", "MDR -10%+"), ("2018-01-04", "VIC Long", "$10~11/$20+"), ("2018-05-10", "combination 완료", "contract·debt 승계"), ("2018-10", "LNG project estimate 급증", "핵심 반증"), ("2019", "asset sale·superpriority financing", "liquidity spiral"), ("2020-01-21", "Chapter 11 신청", "old common terminal failure"), ("2020-06-30", "restructuring 완료", "약 $4.6bn debt 제거")],
      claimdata=[("CB&I 두 번 derisk", "Q3 charge와 MDR DD가 loss tail을 scrub했다.", "새 CEO charge·deal diligence", "EAC 정보가 완전하고 인센티브가 보수적이다.", "closing 후 EAC 재증가 시 반증.", "2018 하반기 비용추정이 다시 급증했다.", "치명적 실패", "seller charge와 buyer DD는 독립 증거가 아닐 수 있다."), ("turnaround playbook", "Dickson이 MDR처럼 CB&I를 고친다.", "MDR 개선 track record", "규모·사업·계약질 차이가 작다.", "초기 milestone·cash conversion 미달 시 반증.", "더 큰 inherited loss가 관리역량을 압도했다.", "실패", "management는 underwriting을 대체하지 못한다."), ("$250m+ synergy", "3% cost cut이므로 쉽게 초과한다.", "$8.5bn combined cost base", "COGS가 실제 controllable cost다.", "cash cost·project loss가 saving 초과 시 반증.", "synergy가 있어도 equity는 실패했다.", "부분/논점 미스", "gross cost base가 아닌 addressable cost를 쓴다."), ("diversification", "on/offshore scale이 blow-up risk를 줄인다.", "geography·end-market 확대", "project loss 상관이 낮다.", "같은 fixed-price process가 손실을 전파하면 반증.", "portfolio와 liability가 함께 커졌다.", "실패", "분산은 공통 underwriting process를 못 분산한다."), ("manageable leverage", "$3.3bn debt·2.2x net은 감당 가능하다.", "pro forma EBITDA·WC normalize", "loss cash flow가 EBITDA에 이미 반영됐다.", "secured rescue finance 필요 시 반증.", "2019 superpriority financing이 필요했다.", "실패", "EPC leverage에는 project cash-to-complete를 더한다."), ("$20+ value", "synergy·debt paydown이면 2~3년 $20+다.", "5.6x pro forma multiple", "equity dilution·restructuring이 없다.", "liquidity runway 12개월 미만이면 반증.", "20개월 뒤 Chapter 11이었다.", "강한 실패", "target 앞에 survival probability를 곱한다.")]),

    I(id="1f37a6ff-a0bd-4600-a3ef-be23fe9fe6ca", date="2018-11-11", author="sidhardt1105", ticker="MDR", entity="McDermott International, Inc.", group="mdr50", raw_short=False, direction="Long", security="10.625% senior unsecured notes due 2024", entry="채권 약 87", horizon="call 2021 / maturity 2024", filename="analysis/ideas/2018/2018-11-11_MDR_2024_notes_long.md", link="https://www.valueinvestorsclub.com/idea/MCDERMOTT_INTL_INC/9249108601", desc=21839, cat=186,
      title="87 가격·14% YTM의 2024 무담보채 money-good Long", verdict="강한 실패 — liquidity·priority spiral로 par maturity 경로 소멸", score=2.3, process=7.4,
      summary="보통주가 아니라 $1.3bn 규모 10.625% senior unsecured notes due 2024를 87에 사는 credit idea다. 14% YTM·2021 call 기준 19% yield를 받고, Chiyoda 불이행의 최대 after-tax 부담 $392m($2.10/share), 2019 이후만 보면 $204m($1.09/share)라서 Goldman preferred $300m과 Tank & Pipe sale로 흡수할 수 있다고 봤다.",
      valuation="bond에는 common SOTP가 아니라 recovery waterfall이 필요하다. 원문 SOTP는 net working capital -$1.915bn, secured term loan $2.249bn, unsecured notes $1.3bn, preferred $360m를 포함하면서도 RemainCo EBITDA $1.275bn×7x와 Tank & Pipe $1.0~1.6bn으로 common $25~30을 냈다. 하지만 distress에서는 DIP·superpriority·secured·administrative claim이 unsecured보다 먼저다.",
      actual="Chiyoda만의 contingent loss보다 CB&I legacy project cash drain과 전사 liquidity가 더 컸다. 2019년 회사는 고비용 superpriority financing과 noteholder forbearance에 의존했고 2020-01-21 Chapter 11을 신청했다. restructuring은 거의 모든 funded debt를 equity로 전환하고 약 $4.6bn debt를 제거했으므로 87에서 par 상환을 받는 money-good 경로는 깨졌다.",
      price="채권의 정확한 coupon cash flow·restructuring distribution·신규 equity value를 연결하지 못했으므로 holding-period IRR과 recovery %는 null이다. Chapter 11 및 funded-debt equitization은 business outcome이 아니라 security thesis의 명백한 실패지만 임의로 -100%라 쓰지 않는다.",
      drivers="손실은 Chiyoda 단일 counterparty가 아니라 total liquidity와 priority migration이 만들었다. Goldman preferred는 bond 뒤의 equity cushion이 아니라 비싼 rescue capital이었고, 후속 superpriority debt는 unsecured 위에 새 claim을 쌓았다. pre-filing common market cap은 법적 recovery cushion이 아니었다.",
      error="joint-and-several liability를 세밀하게 계산했지만 질문 범위를 너무 좁혔다. 13-week cash flow, project별 remaining cash burn, LC draw와 secured refinancing need를 먼저 계산하지 않았고 common SOTP로 bond safety를 보강해 capital-structure 범주 오류를 냈다.",
      first_signal="Tank & Pipe proceeds가 debt paydown이 아니라 운영유동성에 쓰이거나, unsecured 위의 superpriority tranche가 추가되고 notes가 forbearance에 들어가는 순간 money-good base를 철회하고 recovery case로 전환했어야 했다.",
      waterfall="2024 notes의 payoff는 reorganized enterprise value에서 DIP·superpriority·담보부채·행정/우선청구권을 차감한 뒤 무담보 pool에 배분되는 recovery와 interim coupon의 합이다. common 시가총액과 preferred 액면은 법적으로 선순위인 bond cushion이 아니다.",
      metrics=[("Bond price", "87", "par + coupon", "par maturity 경로 소멸", "실패"), ("Yield", "14% YTM / 19% YTC", "money good", "2020 Chapter 11", "실패"), ("Chiyoda stress", "$392m after-tax max", "$204m 2019+", "전사 cash need가 더 큼", "범위 오류"), ("Unsecured notes", "$1.3bn", "equity/preferred cushion", "funded debt equitized", "recovery 미복원"), ("Asset sale", ">$1bn 목표", "deleveraging", "liquidity 문제 미해결", "실패")],
      timeline=[("2018-10-31", "project charge·MDR 급락", "credit stress"), ("2018-11-06", "insider common 매수", "원문 보조신호"), ("2018-11-09", "Chiyoda going-concern 경고", "JV tail 확대"), ("2018-11-11", "VIC notes Long", "87·14% YTM"), ("2019", "Tank & Pipe monetization 추진", "현금조달"), ("2019", "superpriority financing·forbearance", "waterfall 악화"), ("2020-01-21", "prepack Chapter 11", "money-good 반증"), ("2020-06-30", "funded debt equitization", "par claim 종결")],
      claimdata=[("Chiyoda loss 제한", "추가 after-tax 부담은 $392m 이하, 현실적 $204m다.", "JV cash-flow schedule", "공개 estimate가 완전하고 다른 손실이 없다.", "전사 project cash need가 이를 넘으면 반증.", "더 넓은 liquidity loss가 발생했다.", "부분/범위 실패", "단일 tail 계산 뒤 total liquidity를 다시 본다."), ("rescue preferred", "$300m Goldman 자금이 WC를 안정시킨다.", "$289m 순유입", "고비용 PIK가 runway를 충분히 연장한다.", "추가 선순위 자금 필요 시 반증.", "superpriority financing이 뒤따랐다.", "실패", "rescue capital은 안전증거보다 distress 가격신호다."), ("asset-sale deleveraging", "Tank & Pipe가 $1bn+을 낸다.", "$200m EBITDA·7~8x", "net proceeds가 note protection에 쓰인다.", "운영 cash burn이 proceeds를 흡수하면 반증.", "매각만으로 runway를 못 고쳤다.", "실패", "gross proceeds와 debt-paydown cash를 나눈다."), ("equity cushion", "$1.6bn common·preferred가 notes를 보호한다.", "pre-filing capitalization", "시장가치가 법적 우선순위와 같다.", "superpriority claim·EV 하락이면 반증.", "funded debt가 equity로 전환됐다.", "실패", "market cap은 unsecured recovery cushion이 아니다."), ("87 money good", "coupon과 par가 지급된다.", "14% YTM", "2024까지 refinancing 가능하다.", "forbearance·DIP 필요 시 반증.", "2020 Chapter 11로 maturity path가 깨졌다.", "강한 실패", "yield보다 runway와 maturity wall을 먼저 본다."), ("$25~30 common SOTP", "높은 equity value가 bond downside를 지지한다.", "7x EBITDA·asset values", "distress haircut과 priority dilution이 작다.", "SOTP asset가 forced-sale value로 하락하면 반증.", "restructuring이 common SOTP를 지웠다.", "실패", "credit는 enterprise SOTP를 waterfall로 번역한다.")]),

    I(id="57ac591e-b624-407a-be54-18ea0ef94ae0", date="2007-12-10", author="tdylan409", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Long", entry="$79.06 next-day close", horizon="3~5년", filename="analysis/ideas/2007/2007-12-10_MHK_long.md", link=None, desc=36072, cat=580,
      title="duopoly·distribution·hard-surface mix와 10~11x FCF Long", verdict="실패 — quality는 맞았지만 cycle floor를 너무 일찍 선언; 1Y -54.5%, 5Y +3.8%", score=4.4, process=8.1,
      summary="raw Short지만 실제는 buy-and-hold Long이다. 약 25% 미국 점유율, duopoly, 자체 유통, pricing power, 수직계열화와 Dal-Tile·Unilin의 hard-surface mix를 믿고 11.1x 2007E P/E, 7.5x EBITDA, 10~11x FCF가 housing downturn을 충분히 반영했다고 봤다. 3~5년 high-teens~20% CAGR을 기대했다.",
      valuation="낮은 2007E multiple을 quality discount로 봤지만 당시 earnings·FCF 분모는 housing·remodel peak의 잔향을 포함했다. 19% new residential, 55% remodel, 26% commercial exposure를 각각 starts·turnover·employment lag에 연결하고 volume -10/-20/-30%, gross margin과 inventory stress를 교차했어야 한다. 저평가는 trough earnings가 아닌 peak-normalized earnings로 판정해야 한다.",
      actual="GFC housing collapse는 원문이 예상한 12~24개월 unit recovery보다 깊고 길었다. scale·distribution과 hard-surface 전략은 살아남았지만 volume·plant absorption·raw material의 조합이 near-term FCF floor를 무너뜨렸다. SQL price multiplier는 1Y 0.455배, 5Y 1.038배다.",
      price="실제 Long 기준 price-only return은 1M -12.2%, 3M -15.7%, 6M -9.6%, 1Y -54.5%, 2Y -43.8%, 3Y -26.8%, 5Y +3.8%다. 배당·세금·거래비용은 제외한다.",
      drivers="초기 손실은 moat 훼손보다 housing volume·utilization 붕괴가 만들었다. 규모와 유통망은 survival advantage였지만 cyclic downside를 즉시 막는 floor는 아니었다. 5년 동안 회복했어도 목표 CAGR과 큰 중간 drawdown을 고려하면 원 trade는 실패다.",
      error="franchise quality와 entry timing을 합쳤고, 2007E FCF를 normalized owner earnings로 사용했다. new construction·remodel·commercial을 한 housing 변수로 묶고 fixed-cost absorption과 inventory markdown을 stress하지 않았다.",
      first_signal="residential volume과 plant utilization이 동시에 두 분기 악화하고 price increase가 raw-material·freight를 못 따라가며 inventory turns까지 내려가면 10x FCF floor를 버렸어야 했다.",
      metrics=[("Entry / 1Y", "$79.06", "capital-loss 최소", "-54.5%", "실패"), ("5Y return", "high-teens~20% CAGR", "+100~149% 필요", "+3.8%", "강한 미달"), ("P/E", "11.1x 2007E", "quality rerating", "earnings denominator 붕괴", "실패"), ("EV/EBITDA", "7.5x", "downside support", "cycle drawdown", "실패"), ("Market share", "약 25% US", "moat 유지", "장기 leader 유지", "성공")],
      timeline=[("2007-12-10", "VIC Long", "quality-at-discount"), ("2008-H1", "housing·consumer 악화", "volume pressure"), ("2008-H2", "GFC 심화", "utilization 붕괴"), ("2009-02", "별도 MHK Short 등장", "cycle stress 극대화"), ("2009-12", "2Y -43.8%", "capital recovery 지연"), ("2010-12", "3Y -26.8%", "thesis clock 미달"), ("2012-12", "5Y +3.8%", "CAGR 목표 실패")],
      claimdata=[("downturn priced", "현재 가격이 housing 악화를 넘게 반영했다.", "11.1x P/E·10x 2008E FCF", "earnings가 정상 수준이다.", "volume·FCF가 예상보다 더 하락하면 반증.", "1Y -54.5%였다.", "실패", "cyclical multiple은 peak-normalized 분모로 본다."), ("duopoly moat", "25% share와 scale이 방어력을 준다.", "상위 업체 집중", "share가 cash margin으로 전환된다.", "share 유지에도 margin 붕괴 시 한계.", "franchise는 생존했다.", "성공", "moat는 drawdown 방지가 아니라 cycle survival일 수 있다."), ("distribution advantage", "자체망·retailer 관계가 share를 높인다.", "broad product/service", "fixed cost가 downturn에서 감당된다.", "network absorption 급락 시 반증.", "장기 자산은 남았지만 단기 부담이었다.", "부분", "network moat의 operating leverage를 함께 잰다."), ("pricing power", "scale이 원가상승을 전가한다.", "수직계열화·brand", "수요가 가격인상을 흡수한다.", "price/mix가 cost lag에 뒤지면 반증.", "deep downturn에서 volume이 우선했다.", "부분 실패", "pricing power는 수요 탄력성과 같이 본다."), ("hard-surface tailwind", "tile·laminate mix가 구조성장을 만든다.", "Dal-Tile·Unilin", "cycle보다 secular mix가 강하다.", "category growth가 total volume loss를 못 메우면 반증.", "장기 방향은 맞았다.", "성공", "secular mix는 cycle clock과 분리한다."), ("3~5Y high-teens CAGR", "cheapness+growth로 높은 복리수익이다.", "low-teens EPS growth", "multiple·earnings 모두 유지된다.", "5Y 누적 100% 미만이면 반증.", "5Y +3.8%였다.", "강한 실패", "CAGR 목표는 path drawdown과 함께 평가한다.")]),

    I(id="02425766-dadd-41c8-84e5-1574f17fd988", date="2009-02-18", author="todd1123", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Short", security="Common short + long CDS protection", entry="$29.56 next-day close; CDS 약 350bp", horizon="1~3개월", filename="analysis/ideas/2009/2009-02-18_MHK_short.md", link="https://www.valueinvestorsclub.com/idea/Mohawk_Industries/5308391281", desc=13509, cat=1020,
      title="earnings miss·junk downgrade·trade-down의 equity Short + CDS Long", verdict="기간 실패 — 1M short +19.5% 뒤 3M부터 급반전; CDS 성과 null", score=4.8, process=8.0,
      summary="MHK equity $31~32를 short하고 약 350bp CDS protection을 사는 paired bearish idea다. 1~3개월 equity $18, CDS 500bp+로 30~50%를 기대했다. housing·commercial·Europe가 동시에 악화하고 power-box 소비자가 private label로 trade down하며 goodwill write-down·junk downgrade가 debt covenant를 압박한다는 논지였다.",
      valuation="equity $18은 약 42% downside이고 CDS 350→500bp는 spread duration과 default probability 상승 trade다. 그러나 둘은 같은 payoff가 아니다. equity short는 borrow·rebate·squeeze를, CDS는 running coupon·upfront·maturity·recovery를 각각 모델링해야 한다. 1~3개월 catalyst 직후 주가 second derivative가 반전하면 macro level이 나빠도 trade가 실패한다.",
      actual="2009-02 말까지 하락해 1개월 short는 유리했지만 3월 시장저점 이후 주가는 빠르게 반등했다. stock multiplier는 1M 0.805배 뒤 3M 1.349배, 1Y 1.576배, 5Y 4.896배가 됐다. downturn·earnings 약화 자체는 맞았어도 policy·liquidity·expectations inflection을 놓쳤다. CDS의 실제 spread/P&L은 복원되지 않았다.",
      price="stock leg의 단순 short price return은 1M +19.5%, 3M -34.9%, 6M -52.7%, 1Y -57.6%, 2Y -100.6%, 3Y -123.7%, 5Y -389.6%다. 이는 `1-price multiplier`이며 borrow·배당·margin·cover timing을 제외한다. CDS leg의 exact return은 null이다.",
      drivers="1개월 수익은 recession news와 실적·downgrade 우려가 만들었지만, 이후 손실은 2009년 3월의 market/credit inflection과 기대치 바닥이 만들었다. earnings level이 계속 약해도 더 나빠지는 속도가 둔화하면 high-beta cyclical short는 먼저 오른다.",
      error="fundamental stress를 정확히 봤지만 1~3개월 trade에 필요한 catalyst-to-price transmission과 cover rule을 약하게 뒀다. downgrade·goodwill write-down이 cash default와 같지 않았고 CDS spread widening과 equity downside를 중복 payoff처럼 더했다.",
      first_signal="실적 하향 뒤에도 주가가 새 저점을 만들지 않고 credit spread·homebuilder equities가 2~4주 개선되거나 3M stock multiplier가 1을 넘는 순간 equity short를 cover했어야 했다.",
      waterfall="Equity short와 CDS는 별도 증권이다. stock leg는 가격·배당·borrow·margin으로, CDS leg는 spread move·carry·default recovery로 계산한다. 기업악화가 맞아도 각 leg의 진입·청산시점이 다르면 합산수익은 알 수 없다.",
      metrics=[("Equity entry", "$29.56", "$18", "1M short +19.5%; 3M -34.9%", "기간 실패"), ("CDS", "약 350bp", ">500bp", "시계열 미복원", "null"), ("1Y stock", "bearish", "downside 지속", "+57.6% stock", "실패"), ("Rating", "BBB-", "junk downgrade", "cash default와 불일치", "촉매 과대"), ("5Y stock", "bear thesis", "낮은 earning power", "+389.6% stock", "강한 실패")],
      timeline=[("2009-02-18", "VIC short+CDS", "$18·500bp+"), ("2009-02-23", "earnings/outlook catalyst", "near-term test"), ("2009-03", "market low·policy inflection", "cover signal"), ("2009-03-18", "1M stock -19.5%", "단기 성공"), ("2009-05", "3M stock +34.9%", "thesis timing break"), ("2009-08", "6M stock +52.7%", "short squeeze 확대"), ("2010-02", "1Y stock +57.6%", "bear payoff 실패"), ("2014-02", "5Y stock +389.6%", "terminal 강한 실패")],
      claimdata=[("earnings downside", "Street estimates가 housing stress를 못 담았다.", "residential·commercial·Europe 동시 약화", "miss가 아직 가격에 안 들어갔다.", "miss 뒤에도 주가가 오르면 반증.", "1M 하락 뒤 급반등했다.", "기간만 성공", "level보다 expectations second derivative를 본다."), ("trade-down", "소비자가 lower-price/private label로 이동한다.", "power-box channel checks", "mix 하락이 cost savings보다 크다.", "volume/mix 안정 시 반증.", "macro stress는 맞았지만 stock target 실패.", "부분", "channel data를 segment gross margin으로 연결한다."), ("commercial·Europe mask", "비핵심 강세가 사라져 legacy weakness가 드러난다.", "segment mix", "모든 지역이 동시 악화한다.", "region divergence·FX 개선이면 반증.", "earnings 약화는 나타났다.", "성공 방향", "multi-region short는 상관과 FX를 stress한다."), ("junk downgrade", "rating 하락이 refinancing cost를 높인다.", "BBB-와 leverage", "downgrade가 liquidity event다.", "ample liquidity·maturity면 반증.", "equity terminal loss로 이어지지 않았다.", "촉매 과대", "rating event와 default event를 분리한다."), ("goodwill/covenant", "write-down이 debt covenant를 촉발한다.", "large acquisition goodwill", "covenant가 GAAP equity 기반이다.", "add-back·waiver 가능 시 반증.", "주가 경로를 지속 압박하지 못했다.", "실패", "covenant 정의를 계약 원문으로 확인한다."), ("$18·500bp", "두 leg가 1~3개월에 30~50% 낸다.", "equity/CDS asymmetry", "catalyst가 동시에 작동한다.", "stock·spread 반전 시 cover.", "1M 이후 stock leg가 큰 손실이었다.", "실패", "paired trade는 leg별 stop·P&L을 둔다.")]),

    I(id="9677bae5-283c-498f-b8e1-c0f32c865ddb", date="2013-02-08", author="lys615", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Short", entry="$104.84 next-day close", horizon="1~5년", filename="analysis/ideas/2013/2013-02-08_MHK_short.md", link="https://www.valueinvestorsclub.com/idea/MOHAWK_INDUSTRIES_INC/0173364108", desc=0, cat=4,
      title="low ROIC·peak tile margin·Marazzi overpayment의 MHK Short", verdict="강한 실패 — housing·hard-surface·M&A leverage를 과소평가; 5Y stock +155.3%", score=2.4, process=8.0,
      summary="원문은 MHK가 quality compounder가 아니라 low-ROE roll-up이며 ceramic peak margin과 goodwill-heavy acquisitions가 intrinsic value를 과장한다고 봤다. Marazzi 인수를 overpriced로 보고 book value 근처·약 $60대가 적정하다는 Short였다. raw와 실제 방향은 Short로 일치한다.",
      valuation="asset/segment ROIC와 book value를 중심으로 $60대 intrinsic value를 제시했지만 platform의 distribution synergy, hard-surface mix와 depressed-cycle earnings의 operating leverage를 낮게 뒀다. acquisition EV만 보지 말고 incremental EBITDA·working capital·cross-sell·tax·capex를 합친 cohort ROIC로 Marazzi를 평가해야 했다.",
      actual="미국 housing·remodel 회복, hard-surface mix와 Marazzi를 포함한 글로벌 ceramic scale이 earnings를 끌어올렸다. stock multiplier는 1Y 1.383배, 2Y 1.582배, 5Y 2.553배다. 일부 ROIC·goodwill 우려가 맞아도 entry와 earnings direction을 이기지 못했다.",
      price="단순 short price return은 1M -7.6%, 3M -12.2%, 6M -20.6%, 1Y -38.3%, 2Y -58.2%, 3Y -44.8%, 5Y -155.3%다. borrow·배당·short margin을 제외해 실제 손실은 다를 수 있다.",
      drivers="손실은 multiple expansion만이 아니라 depressed base에서의 volume·utilization·mix와 acquisition synergy가 만들었다. book multiple은 브랜드·distribution·technology platform의 incremental return을 충분히 담지 못했다.",
      error="과거 평균 ROIC를 forward acquisition economics에 그대로 적용했고 housing trough에서 cycle recovery를 충분히 확률가중하지 않았다. ceramic margin mean reversion을 주장하면서 distribution synergy·fixed-cost leverage를 독립 변수로 두지 않았다.",
      first_signal="Marazzi 통합 뒤 ceramic sales·margin과 consolidated EPS estimate가 두 분기 연속 상향되고 주가가 target 반대 방향으로 20% 이상 가면 valuation Short를 닫았어야 했다.",
      metrics=[("Entry", "$104.84", "$60대", "1Y stock +38.3%", "실패"), ("5Y stock", "downside", "book rerating 하락", "+155.3%", "강한 실패"), ("Marazzi", "overpriced", "value destructive", "global ceramic scale 확대", "실패"), ("ROE/ROIC", "낮음", "near-book multiple", "platform premium 지속", "실패"), ("Housing", "recovery priced", "limited upside", "multi-year operating leverage", "실패")],
      timeline=[("2013-02-08", "VIC Short", "$60대 value"), ("2013", "Marazzi acquisition", "핵심 short claim"), ("2013-H2", "housing/remodel 회복", "volume leverage"), ("2014-02", "1Y stock +38.3%", "반증"), ("2015-02", "2Y +58.2%", "손실 확대"), ("2016-02", "3Y +44.8%", "short 미회복"), ("2018-02", "5Y +155.3%", "terminal 실패")],
      claimdata=[("quality 과대평가", "MHK는 low-return roll-up이다.", "historical ROE·goodwill", "incremental economics도 과거와 같다.", "incremental margin·FCF 개선 시 반증.", "earnings와 stock이 상승했다.", "실패", "average ROIC와 incremental ROIC를 나눈다."), ("tile peak margin", "bubble-era ceramic margin으로 못 돌아간다.", "housing peak comparison", "mix·scale 개선이 없다.", "ceramic margin 상승 지속 시 반증.", "hard-surface와 scale이 개선을 만들었다.", "부분 실패", "mean reversion에는 구조적 mix shift를 반영한다."), ("Marazzi 과지불", "인수가 goodwill만 늘리고 ROIC를 낮춘다.", "deal valuation", "distribution synergy가 작다.", "sales·margin cross-sell가 나타나면 반증.", "global ceramic platform에 기여했다.", "실패", "M&A는 cohort cash ROIC로 추적한다."), ("book-value anchor", "낮은 ROE라 book 근처가 적정하다.", "tangible capital return", "intangibles·distribution 가치가 작다.", "FCF multiple이 유지되면 반증.", "book보다 높은 platform value를 받았다.", "실패", "book는 브랜드·network를 누락할 수 있다."), ("$60대 intrinsic", "valuation downside가 크다.", "sum of segment returns", "cycle recovery가 제한된다.", "EPS revision·price +20%면 반증.", "1Y +38.3%였다.", "강한 실패", "short target에는 cycle-up state를 넣는다."), ("housing priced", "주택회복 기대는 이미 주가에 있다.", "2012 rally", "실제 flooring lag가 짧다.", "orders·utilization이 계속 상향되면 반증.", "multi-year recovery가 이어졌다.", "실패", "starts와 flooring installation lag를 잰다.")]),

    I(id="23387e45-c762-4f66-9eb0-cb1fdf4e38e2", date="2013-12-09", author="ci230", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Long", entry="$141.02 next-day close", horizon="12개월", filename="analysis/ideas/2013/2013-12-09_MHK_long.md", link="https://www.valueinvestorsclub.com/idea/MOHAWK_INDUSTRIES_INC/6179320214", desc=0, cat=133,
      title="flooring lag·Marazzi synergy·hard-surface mix의 12M Long", verdict="부분 성공 — 1Y +11.8%로 +28% target 미달, 2~3Y 지연 달성", score=7.3, process=8.2,
      summary="raw Short지만 실제 Long이다. housing starts·home sales 뒤 flooring 설치가 늦게 따라오고, GFC 뒤 leaner cost base·Marazzi Russia distribution·hard-surface mix와 deleveraging이 operating leverage를 만든다고 봤다. 12개월 약 +28%가 목표였다.",
      valuation="2014~15 EBITDA/EPS 성장과 quality multiple을 결합했다. 핵심은 terminal multiple보다 earnings-revision timing이다. flooring demand lag가 6개월인지 18개월인지에 따라 같은 intrinsic value도 12개월 수익은 달라진다. Marazzi synergy는 Russia volume, plant utilization, distribution cross-sell와 integration cash cost로 분해해야 한다.",
      actual="housing/remodel recovery, hard-surface mix와 acquisition platform 방향은 맞았다. 그러나 1년 stock return은 +11.8%로 +28% 목표에 못 미쳤다. 2년 +34.9%, 3년 +42.7%로 target이 지연 달성됐고 5년에는 -14.9%로 다시 entry 아래가 됐다.",
      price="실제 Long price-only return은 1M +4.3%, 3M +1.8%, 6M -3.8%, 1Y +11.8%, 2Y +34.9%, 3Y +42.7%, 5Y -14.9%다. 목표기간과 장기 terminal 결과를 분리한다.",
      drivers="2~3년 수익은 flooring cycle의 늦은 회복과 capacity utilization, hard-surface·Marazzi 효과가 만들었다. 12개월 miss는 논지 방향보다 timing error였고, 5년 반락은 cyclical rerating을 영구 compounder로 바꾸면 안 된다는 점을 보여준다.",
      error="housing→flooring의 lag를 thesis edge로 제시했지만 catalyst date와 quarterly order proxy를 충분히 고정하지 않았다. synergy·cycle·multiple을 한 target에 쌓고 target 도달 후 재-underwrite 규칙이 없었다.",
      first_signal="12개월 안에 residential segment volume과 margin이 예상대로 가속하지 않으면 horizon failure로 기록하되, earnings estimate가 계속 상향되면 2년차 thesis로 명시적으로 재승인했어야 했다.",
      metrics=[("Entry / 1Y", "$141.02", "+28%", "+11.8%", "미달"), ("2Y", "same thesis", "target", "+34.9%", "지연 성공"), ("3Y", "operating leverage", "상승", "+42.7%", "성공"), ("5Y", "compounder 가능", "가치 유지", "-14.9%", "실패"), ("Marazzi", "synergy", "distribution 확대", "global ceramic 기여", "성공 방향")],
      timeline=[("2013-02", "선행 MHK Short", "반대 시각"), ("2013-12-09", "VIC Long", "+28% 12M"), ("2014-H1", "flooring 회복 지연", "6M -3.8%"), ("2014-12", "1Y +11.8%", "horizon miss"), ("2015-12", "2Y +34.9%", "target 지연 달성"), ("2016-12", "3Y +42.7%", "cycle payoff"), ("2018-12", "5Y -14.9%", "rerating 반납")],
      claimdata=[("delayed flooring rebound", "housing 뒤 flooring 매출이 강하게 회복한다.", "historical negative-growth rebounds", "lag가 원 horizon 안이다.", "12M volume 가속 부재 시 timing 반증.", "2~3년에 주가 target을 넘겼다.", "지연 성공", "산업 lag에는 날짜·leading indicator를 붙인다."), ("lean cost base", "GFC 구조조정 뒤 volume이 margin으로 크게 전환된다.", "lower fixed-cost base", "재증설·inflation이 leverage를 상쇄하지 않는다.", "incremental margin 미달 시 반증.", "회복기 earnings를 도왔다.", "성공 방향", "operating leverage를 incremental margin으로 추적한다."), ("Marazzi synergy", "Russia·distribution이 cross-sell을 만든다.", "2013 acquisition footprint", "integration·FX tail이 제한적이다.", "segment sales/margin 미달 시 반증.", "global ceramic scale에 기여했다.", "성공 방향", "M&A thesis는 지역별 synergy bridge가 필요하다."), ("hard-surface mix", "soft→hard 전환이 growth와 margin을 높인다.", "tile·laminate secular share", "LVT competition이 economics를 훼손하지 않는다.", "mix 상승에도 margin 하락 시 반증.", "장기 portfolio 전환은 지속됐다.", "성공", "mix share와 category profitability를 따로 본다."), ("deleveraging/M&A", "cash flow로 부채를 낮추고 추가 deal을 한다.", "recovery cash generation", "capital allocation이 disciplined하다.", "net leverage 상승·ROIC 하락 시 반증.", "roll-up platform이 이어졌다.", "성공 방향", "deal capacity보다 per-share ROIC를 본다."), ("12M +28%", "earnings/guidance가 1년에 rerate를 만든다.", "recovery estimate", "시장 recognition lag가 짧다.", "1Y return +28% 미달이면 반증.", "1Y +11.8%, 2Y +34.9%였다.", "실패/지연", "business truth와 horizon truth를 분리한다.")]),

    I(id="b39c46a3-43b6-4dd1-a244-5c355b80e618", date="2018-08-03", author="dsteiner84", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Long", entry="$187.03 next-day close", horizon="1~2년", filename="analysis/ideas/2018/2018-08-03_MHK_long.md", link="https://www.valueinvestorsclub.com/idea/MOHAWK_INDUSTRIES_INC/5932791795", desc=0, cat=9,
      title="2Q miss 과잉반응·capex roll-off·LVT ramp의 expectation-reset Long", verdict="실패 — transitory miss가 multi-year margin reset으로 이어져 2Y -57.5%", score=3.4, process=8.0,
      summary="raw Short지만 실제 Long이다. 2Q18 miss와 guidance cut 뒤 약 $185에서 owner-operator·distribution moat·insider buying을 믿고, multi-year capacity capex가 끝나며 FCF가 늘고 미국 LVT startup·freight/raw-material 문제가 일시적이라고 봤다. 낮아진 기대가 충분한 margin of safety라는 논지였다.",
      valuation="capex peak-out은 `EBITDA - maintenance capex` 개선의 필요조건이지만 신규 capacity가 목표 utilization·yield를 내야 충분조건이 된다. price/mix가 input·freight·incremental depreciation을 따라가는지, Flooring NA margin이 몇 분기에 회복하는지를 target multiple보다 먼저 모델링해야 했다.",
      actual="2018 하반기부터 input·freight inflation, Flooring NA execution/LVT startup, housing·remodel 둔화가 지속됐다. franchise는 살아남았지만 earnings miss는 일회성이 아니었다. stock은 3M -29.6%, 1Y -36.8%, 2Y -57.5%였고 3년에는 +4.0%로 장기간 후에야 entry를 회복했다.",
      price="실제 Long price-only return은 1M +1.7%, 3M -29.6%, 6M -32.7%, 1Y -36.8%, 2Y -57.5%, 3Y +4.0%다. 배당·거래비용은 제외한다.",
      drivers="손실은 multiple panic보다 margin estimate reset이 만들었다. 신규 capacity의 depreciation·startup inefficiency, price-cost lag와 낮은 utilization이 동시에 FCF 기대를 낮췄고, insider buying은 이를 상쇄하지 못했다.",
      error="'capex가 끝난다'를 '높은 ROIC의 현금흐름이 시작된다'로 건너뛰었다. miss 원인을 transitory 항목으로 묶고 4-quarter price-cost·yield·utilization bridge와 사전 손절수준을 두지 않았다.",
      first_signal="다음 두 분기에도 Flooring NA margin이 회복하지 않고 price/mix가 raw material·freight·depreciation을 못 덮거나 3M 주가가 -20%를 넘으면 expectation reset이 불충분하다고 인정했어야 했다.",
      metrics=[("Entry", "$187.03", "sell-off floor", "3M -29.6%", "실패"), ("2Y return", "FCF inflection", "positive", "-57.5%", "강한 실패"), ("Capex", "peak-out", "FCF ramp", "earnings decline이 상쇄", "부분"), ("Flooring NA", "temporary pressure", "margin recovery", "multi-quarter reset", "실패"), ("3Y return", "franchise value", "recovery", "+4.0%", "지연 회복")],
      timeline=[("2018-Q2", "earnings miss·guidance cut", "entry setup"), ("2018-08-03", "VIC Long", "약 $185"), ("2018-Q3", "inflation·execution 지속", "transitory 반증"), ("2018-11", "3M -29.6%", "첫 stop signal"), ("2019-08", "1Y -36.8%", "horizon failure"), ("2020-03", "COVID trough", "drawdown 확대"), ("2020-08", "2Y -57.5%", "강한 실패"), ("2021-08", "3Y +4.0%", "뒤늦은 회복")],
      claimdata=[("miss transitory", "freight·inflation은 몇 분기 안에 끝난다.", "2Q guide reset", "pricing lag와 execution 문제가 짧다.", "두 분기 margin 미회복 시 반증.", "pressure가 오래 지속됐다.", "실패", "transitory에는 종료조건과 날짜를 둔다."), ("capex roll-off", "투자완료로 FCF가 크게 늘어난다.", "multi-year capacity spend", "신규 자산 ROIC가 높다.", "utilization·yield 미달 시 반증.", "earnings decline이 capex 감소를 상쇄했다.", "부분 실패", "capex 종료와 cash ROIC를 분리한다."), ("LVT startup", "미국 LVT 문제는 일시적이다.", "신규 plant ramp", "quality·competition이 통제된다.", "scrap·yield·share 미개선 시 반증.", "startup/competition이 예상보다 길었다.", "실패", "ramp는 yield·unit cost·share로 검증한다."), ("insider signal", "owner buying이 undervaluation을 확인한다.", "CEO/insider purchases", "insider가 cycle 정보를 정확히 안다.", "fundamental KPI 악화 시 signal 무효.", "주가 하락을 막지 못했다.", "실패", "insider 매수는 thesis가 아닌 보조증거다."), ("distribution moat", "scale·network가 장기 franchise를 지킨다.", "national footprint", "moat가 near-term margin floor다.", "share 유지에도 cash margin 하락 시 구분.", "franchise는 생존했다.", "성공/기간 무관", "business survival과 stock timing을 나눈다."), ("sell-off 과잉", "기대치가 충분히 낮아졌다.", "2Q 주가 급락", "추가 estimate cuts가 작다.", "3M -20%·추가 guide cut이면 반증.", "3M -29.6%, 2Y -57.5%였다.", "강한 실패", "price fall이 아닌 earnings floor를 확인한다.")]),

    I(id="4bc970f8-09ad-43c8-847c-baf292216a29", date="2020-10-14", author="Value1929", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Long", entry="$103.00 next-day close", horizon="18개월 미만", filename="analysis/ideas/2020/2020-10-14_MHK_long.md", link=None, desc=36263, cat=87,
      title="housing catch-up·LVT share recapture·FX·legal discount의 tactical Long", verdict="강한 tactical 성공 — 6M +98.2%, 1Y +80.4%; 2Y에는 상승분 반납", score=9.0, process=8.6,
      summary="raw Short지만 실제 Long이다. COVID 뒤 low rates·housing boom이 먼저 나타났지만 flooring은 installer·order lag 때문에 아직 실적에 덜 반영됐고, LVT tariff/local capacity·약달러·legal/channel-stuffing overhang 해소가 추가 upside라고 봤다. 약 7.15x NTM EV/EBITDA에서 18개월 50~75%+를 기대한 catch-up trade였다.",
      valuation="NTM EV/EBITDA 약 7.15x에서 earnings recovery와 11~13x rerating을 함께 봤다. upside를 `(EBITDA revision) × (multiple rerating) - net debt/share change`로 분해하면 legal discount 해소 없이도 housing volume·price-cost만으로 어느 정도 수익이 나는지 확인할 수 있다. 목표가 6개월에 초과되면 새 multiple에서 재-underwrite해야 한다.",
      actual="housing·remodel demand와 flooring lag, LVT/local production, FX tailwind가 earnings expectations를 끌어올렸다. stock은 6개월 +98.2%, 1년 +80.4%로 목표를 조기 초과했다. 그러나 2년에는 -6.6%로 entry 아래가 되어 2021 peak 이후 rate·housing cycle을 계속 보유하면 수익을 반납했다.",
      price="실제 Long price-only return은 1M +19.6%, 3M +46.5%, 6M +98.2%, 1Y +80.4%, 2Y -6.6%다. 원문 작성자는 약 한 달 뒤 $130 부근에서 청산했다고 후속 2021 글이 언급하지만 DB 공식성과는 보존 multiplier만 사용한다.",
      drivers="수익은 housing data 자체보다 flooring estimate의 지연 catch-up과 depressed multiple의 동시 회복이 만들었다. 낮은 entry expectation과 명확한 18개월 clock이 edge였고, 조기 target 도달 뒤 exit하지 않으면 macro beta가 다시 지배했다.",
      error="legal·tariff·FX·housing을 모두 upside로 쌓아 각 기여도를 분리하지 않았고 target 초과 뒤 trailing thesis를 새로 정의하지 않았다. installer bottleneck이 demand destruction으로 바뀌는 조건도 더 명확했어야 했다.",
      first_signal="6~12개월 안에 11~13x rerating 또는 +50~75% target에 도달하면 자동 매도/재승인하고, housing turnover·orders·price-cost가 두 분기 둔화하면 catch-up thesis를 종료했어야 했다.",
      metrics=[("Entry", "$103.00", "+50~75%", "6M +98.2%", "강한 성공"), ("1Y return", "18M target", "+50~75%", "+80.4%", "성공"), ("2Y return", "compound 가능", "value 유지", "-6.6%", "반납"), ("EV/EBITDA", "약 7.15x NTM", "11~13x", "급격한 rerating", "성공"), ("Catalysts", "LVT·FX·housing", "estimate catch-up", "동시 개선", "성공 방향")],
      timeline=[("2020-03", "COVID·housing shock", "trough setup"), ("2020-H2", "rates·housing boom", "leading indicator"), ("2020-10-14", "VIC Long", "$100대·50~75%"), ("2020-11", "1M +19.6%", "early confirmation"), ("2021-01", "3M +46.5%", "target 접근"), ("2021-04", "6M +98.2%", "target 초과·exit signal"), ("2021-10", "1Y +80.4%", "강한 성공"), ("2022-10", "2Y -6.6%", "cycle 반납")],
      claimdata=[("flooring demand lag", "housing boom이 12~18개월 뒤 flooring에 온다.", "orders·installer bottleneck", "lagged demand가 취소되지 않는다.", "backlog 취소·turnover 둔화면 반증.", "estimate와 stock이 빠르게 상승했다.", "성공", "leading data를 installation lag로 번역한다."), ("legal discount 과도", "channel-stuffing scrutiny가 enterprise-threatening하지 않다.", "valuation discount", "cash penalty·restatement tail이 제한적이다.", "material restatement·covenant 영향 시 반증.", "discount가 빠르게 닫혔다.", "성공 방향", "legal risk를 cash·timing·reputation으로 나눈다."), ("LVT recapture", "tariff와 domestic capacity가 share를 회복한다.", "import economics·plant capacity", "yield·design이 경쟁사와 동등하다.", "share·utilization 미개선 시 반증.", "recovery 기대에 기여했다.", "성공 방향", "policy catalyst를 unit economics로 연결한다."), ("FX tailwind", "약달러가 Europe translation을 개선한다.", "currency reversal", "local margin이 유지된다.", "constant-currency miss면 반증.", "reported expectation에 도움을 줬다.", "성공", "FX와 organic growth를 분리한다."), ("7.15x trough multiple", "normal 11~13x로 rerate한다.", "historical range", "EBITDA도 회복한다.", "multiple만 오르고 EBITDA 하향이면 반증.", "6M stock이 거의 2배였다.", "강한 성공", "multiple·earnings 기여를 따로 attribution한다."), ("18M +50~75%", "catalyst 묶음이 빠른 catch-up을 만든다.", "low expectations", "target 도달 뒤 discipline이 있다.", "6~12M target 초과 시 재승인.", "6M +98.2%, 2Y -6.6%였다.", "기간 강한 성공", "cyclical target 달성은 exit event다.")]),

    I(id="20752c4b-0a92-4e7b-8379-f2d2384b6f06", date="2021-12-23", author="Glory_Warriors", ticker="MHK", entity="Mohawk Industries, Inc.", group="mhk50", raw_short=True, direction="Long", entry="$174.61 next-day close", horizon="1~3년", filename="analysis/ideas/2021/2021-12-23_MHK_long.md", link=None, desc=32836, cat=129,
      title="15% EBIT margin·$26 EPS·LVT share의 $390 Long", verdict="강한 실패 — peak margin을 정상으로 보고 rate·housing regime 전환을 누락", score=2.0, process=7.6,
      summary="raw Short지만 실제 Long이다. 2020 trough 8%에서 2021 약 12%로 오른 EBIT margin이 2016~17의 15%로 복귀하고, housing growth·pricing·LVT share·buyback으로 2024 EPS $26을 낸다고 봤다. Base $26×15x=$390, 1Y 약 $320, Bull $28×18x=$500, Bear $13×12x≈$170이었다.",
      valuation="scenario가 모두 같은 저금리·housing regime 안에서 움직였다. 15% margin을 volume·price-cost·mix·productivity로 bridge하고 2022~24 mortgage-rate shock, existing-home turnover freeze, utilization downside를 별도 state로 넣었어야 한다. 실제 2024 adjusted EPS $9.70은 원문 Bear $13보다도 낮았다.",
      actual="2022부터 금리상승과 affordability 악화로 기존주택 거래·remodel이 약해지고 volume·utilization·price competition이 margin을 압박했다. 2024 매출은 약 $10.8bn, adjusted EPS $9.70, FCF $680m이었다. 회사는 재무건전성과 FCF를 유지했지만 원문의 15% margin·$26 EPS·$390 target은 실현되지 않았다.",
      price="실제 Long price-only return은 1M -9.0%, 3M -22.0%, 6M -31.0%, 1Y -43.9%다. 2024-12-31 주가 약 $119는 $390 target의 약 31%이며 exact 3Y total return은 repository row가 없어 null이다.",
      drivers="손실은 moat 붕괴보다 regime 전환과 denominator error에서 왔다. 2021 pricing·stimulus·high utilization이 만든 margin을 정상으로 보고 mortgage rate와 turnover shock를 scenario 밖에 뒀다. buyback과 낮은 leverage는 생존을 도왔지만 earnings multiple의 분모 붕괴를 막지 못했다.",
      error="2016~17의 15% margin을 mean으로 선택하면서 당시와 2021의 mix·capacity·input·competition을 비교하지 않았다. Bear EPS $13도 severe housing state를 포함하지 않아 false floor였고, valuation target이 EPS와 multiple의 동시 낙관에 의존했다.",
      first_signal="mortgage rate 상승과 existing-home sales 둔화가 주문에 반영되고 adjusted margin이 12%에서 두 분기 연속 하락하거나 2022 EPS consensus가 10% 상향 대신 하향되면 $390 framework를 즉시 폐기했어야 했다.",
      metrics=[("Entry / 1Y", "$174.61", "$320", "-43.9%", "강한 실패"), ("2024 target", "$390", "$26×15x", "YE 약 $119", "강한 실패"), ("2024 EPS", "$26E", "base", "$9.70 adjusted", "강한 실패"), ("EBIT margin", "약 12%", "15%", "2024 segment 합산 약 8%대", "실패"), ("2024 FCF", "balance-sheet support", "buyback floor", "$680m", "사업 성공/주가 미방어")],
      timeline=[("2020", "COVID trough·8% margin", "mean-reversion base"), ("2021", "약 12% margin·housing 강세", "peak setup"), ("2021-12-23", "VIC Long", "$320/$390"), ("2022-H1", "mortgage rate 급등", "regime break"), ("2022-06", "6M -31.0%", "첫 강한 반증"), ("2022-12", "1Y -43.9%", "horizon failure"), ("2022~2024", "industry contraction", "volume·utilization 압박"), ("2024-12", "$9.70 adjusted EPS·약 $119", "target 붕괴")],
      claimdata=[("15% margin 복귀", "2016~17 수준으로 mean revert한다.", "8%→12% recovery", "2021 margin이 peak가 아니다.", "두 분기 연속 margin 하락 시 반증.", "2024 수익성은 목표에 크게 미달했다.", "실패", "mean은 regime·mix·capacity를 맞춰 고른다."), ("2024 EPS $26", "volume·price·margin·buyback으로 달성한다.", "operating leverage model", "housing·price-cost가 우호적이다.", "consensus 하향·EPS <$13이면 반증.", "2024 adjusted EPS $9.70이었다.", "강한 실패", "EPS target을 driver bridge로 만든다."), ("LVT share", "domestic capacity·innovation이 Flooring NA를 견인한다.", "category growth", "category gain이 total flooring weakness를 넘는다.", "share gain에도 segment EBIT 하락 시 반증.", "전략은 유효했지만 earnings gap을 못 메웠다.", "부분", "category winner와 company earnings를 구분한다."), ("housing 지속", "strong starts·home sales가 flooring 수요를 지지한다.", "2021 housing data", "금리·affordability regime이 유지된다.", "mortgage/turnover 급변 시 반증.", "2022 rate shock가 수요를 눌렀다.", "실패", "starts·turnover·remodel을 분리한다."), ("buyback floor", "낮은 leverage와 repurchase가 downside를 막는다.", "balance-sheet capacity", "earnings yield가 stable하다.", "EPS 하락이 share reduction보다 크면 반증.", "FCF·buyback에도 주가가 크게 하락했다.", "실패한 floor", "buyback은 intrinsic value가 안정적일 때만 floor다."), ("$320/$390", "$26×15x로 large upside다.", "base/bull/bear table", "EPS와 multiple이 동시에 유지된다.", "Bear $170 하향 돌파 시 model 폐기.", "1Y -43.9%, 2024 약 $119였다.", "강한 실패", "scenario에는 regime-break state를 넣는다.")]),
]


def idea_sources(idea):
    raw = m.S("첨부 SQL 원문·metadata", idea["link"], "VIC_IDEAS(4).sql / VIC", idea["date"], f"idea_id·raw direction·description {idea['desc']} chars·catalyst {idea['cat']} chars", "원문")
    return [raw, *m.SOURCES[idea["group"]]]


def performance_note(idea):
    if idea["id"] not in PERF:
        return "첨부·repository에 이 idea의 정확한 performance row가 없어 1개월~5년 수익률을 만들지 않는다. 사건·기업 생존·target 도달과 투자 total return을 별도 필드로 둔다."
    if idea["id"] == "02425766-dadd-41c8-84e5-1574f17fd988":
        return "보존 주가 multiplier는 equity short 방향으로 교정했으며 CDS leg는 spread·carry·recovery 시계열이 없어 null이다. 단순 short price return은 실제 short P&L과 다르다."
    return "보존 주가 multiplier를 원문에서 확인한 실제 방향으로 교정했다. price-only이며 배당·borrow·세금·거래비용과 corporate action 조정은 포함하지 않는다."


def report(idea):
    old_sources = m.idea_sources
    m.idea_sources = idea_sources
    try:
        text = m.report(idea)
    finally:
        m.idea_sources = old_sources
    raw = "Short" if idea["raw_short"] else "Long"
    quality = "B — 보존 multiplier를 실제 방향으로 교정; price-only." if idea["id"] in PERF else "C — performance row 부재; exact return/IRR null."
    text = text.replace("Batch 046 canonical report.", "Batch 050 canonical report.")
    text = text.replace("### Common equity cash waterfall", "### Security cash waterfall")
    generic = ("회계이익에서 운전자본·담보·규제자본·maintenance/growth investment·interest·tax를 차감하고, common보다 선순위인 계약·채권자 청구권을 먼저 배치한다. "
               "자산가치와 계약상 수취액은 현금화 날짜·세금·재투자 의무를 반영한다. 기업가치가 맞아도 security와 duration이 틀리면 투자결과는 실패할 수 있다.")
    text = text.replace(generic, idea["waterfall"])
    text = text.replace("이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.", performance_note(idea))
    text = text.replace(f"`ATH`를 회사로 보지 말고 {idea['entity']} 법인·exchange·날짜로 고정한다.", f"`{idea['ticker']}`와 날짜를 {idea['entity']}의 실제 법인·security에 고정한다.")
    text = text.replace("SQL performance가 없으면 null을 유지한다.", "성과는 원문 방향으로 교정하고, 없는 security leg·기간은 null로 유지한다.")
    text = text.replace("- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.", f"- 가격성과: **{quality}**")
    text = text.replace(f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |", f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |\n| 실제 Security | **{idea['security']}** |")
    text = text.replace(f"raw {raw} 보존; 실제 {idea['direction']}; entity={idea['entity']}", f"raw {raw} 보존; 실제 {idea['direction']} / {idea['security']}; entity={idea['entity']}")
    return text


def make_payload(ideas):
    old_sources = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(ideas)
    finally:
        m.idea_sources = old_sources
    out["batch"] = 50
    out["title"] = "McDermott / Mohawk Industries — Project Liability, Cycle and Security V9"
    for idea, master, post in zip(ideas, out["ideas_master"], out["postmortems"]):
        perf = PERF.get(idea["id"])
        master["security_ko"] = idea["security"]
        master["performance_available"] = int(perf is not None)
        master["next_day_close"] = float(idea["entry"].split("$")[1].split()[0]) if "next-day close" in idea["entry"] else None
        for period in ("1m", "3m", "6m", "1y", "2y", "3y", "5y"):
            master[f"perf_{period}"] = perf.get(period) if perf else None
        if perf:
            sign = -1 if idea["direction"] == "Short" else 1
            for period in ("1y", "3y", "5y"):
                mult = perf.get(period)
                value = None if mult is None else sign * (mult - 1)
                master[f"idea_return_{period}"] = value
                post[f"corrected_return_{period}"] = value
        post["research_direction_ko"] = f"{idea['direction']} / {idea['security']}"
        post["research_status_ko"] = performance_note(idea)
        post["confidence"] = .92 if idea["desc"] else .86
    return out


def make_index(ideas):
    rows = []
    for n, idea in enumerate(ideas, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['ticker']} | {raw}→**{idea['direction']} / {idea['security']}** | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 050 — McDermott / Mohawk Industries — V9 Index", "",
        f"> **Research as-of:** {ASOF}. 첨부 `VIC_IDEAS(4).sql`의 원문 action/payoff와 repository 성과를 감사했다. **10 idea = 10 canonical reports**다.", "",
        "## 0. 배치 결론", "",
        "MDR은 동일한 오류가 security를 바꾸며 깊어졌다. 2013 common은 문제계약을 finite inventory로 오판했고, 2018 merger common은 그 turnaround 역량을 CB&I의 더 큰 계약부채에 외삽했다. 2018 notes는 security seniority를 높였지만 전사 liquidity와 recovery waterfall 대신 Chiyoda 단일 tail·common SOTP에 기대어 실패했다. MHK는 durable franchise가 맞아도 cycle entry·horizon·normalized margin이 틀리면 50%+ drawdown이 난다는 연속 실험이다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | Ticker | raw→실제 방향 / Security | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|", *rows, "",
        "## 2. Direction / Security Audit", "",
        "- MDR 3건의 raw Long은 맞다. 단, 2018-11-11은 common이 아니라 **10.625% senior unsecured notes due 2024**다.",
        "- MHK raw Short 7건 중 실제 Long은 2007-12, 2013-12, 2018-08, 2020-10, 2021-12의 5건이다.",
        "- 실제 Short는 2009-02의 common Short + CDS Long과 2013-02 common Short 두 건뿐이다.", "",
        "## 3. 투자논지의 누적 교정", "",
        "### McDermott — backlog에서 recovery waterfall까지", "",
        "1. Backlog 금액을 가치로 보지 말고 계약별 expected margin과 remaining cash-to-complete로 바꾼다.\n2. 반복 charge는 개별 project가 아니라 bidding·EAC·execution process 문제일 수 있다.\n3. 인수기업의 EBITDA보다 inherited fixed-price liability·negative working capital·LC를 먼저 산다.\n4. Distress bond는 common 시가총액이 아니라 DIP→secured→priority→unsecured waterfall로 평가한다.", "",
        "### Mohawk — franchise와 cycle을 분리", "",
        "2007 Long은 moat는 맞고 cycle floor가 틀렸다. 2009 Short는 recession은 맞고 시장저점 timing이 틀렸다. 2013 Short는 hard-surface·M&A·operating leverage를 과소평가했고, 같은 해 Long은 방향은 맞지만 12개월 clock이 짧았다. 2018 Long은 capex roll-off를 ROIC inflection으로 오인했고, 2020 Long은 낮은 기대와 housing lag를 정확히 잡았다. 2021 Long은 peak margin을 정상 margin으로 썼다.", "",
        "## 4. 배치 공통 교훈", "",
        "1. **Backlog는 margin exposure다.** 계약가격에서 remaining cost·cash need를 뺀다.\n2. **Management quality는 liability underwriting의 대체물이 아니다.**\n3. **Good cyclical과 good entry는 다르다.** moat는 drawdown을 막지 않을 수 있다.\n4. **Crisis short는 second derivative가 핵심이다.** bad news가 계속돼도 덜 나빠지면 먼저 오른다.\n5. **Capex roll-off와 FCF inflection은 다르다.** utilization·yield·ROIC를 확인한다.\n6. **Peak margin을 mean으로 쓰지 않는다.** rate·turnover·utilization의 regime-break state를 둔다.\n7. **Target 조기 달성은 재-underwrite event다.** 2020 Long의 6M +98.2%와 2Y -6.6%가 이를 보여준다.\n8. **성과는 security별이다.** CDS·bond recovery가 없으면 common price로 대체하지 않는다.", "",
        "## 5. 데이터·앱 산출물", "",
        "- DB payload: `data/curated/batch_050_mdr_mhk_deep_v7.json`\n- Streamlit wrapper: `analysis/batch_050_mdr_mhk_10.md`\n- SQL source packet: `data/curated/batch_050_source_packet.json`\n- Builder: `scripts/50_build_batch_050_v9.py`", "",
        "## 6. 검증 기준", "",
        "10개 보고서 모두 0~12절, 6개 claim/100% weight, 5개 metric, 최소 6개 event와 원문+공식자료 source를 포함한다. Payload·문서·앱 popup의 entity, direction, security, verdict를 동일하게 유지한다.", "",
    ])


def main():
    if len(IDEAS) != 10 or len({i["id"] for i in IDEAS}) != 10:
        raise ValueError("Batch 050 requires ten unique idea units")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or sum(m.WEIGHTS) != 100:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(i["filename"]).relative_to("analysis").as_posix() for i in IDEAS]
    wrapper = "# Batch 050 — McDermott / Mohawk Industries V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit 호환 wrapper다. canonical index: [Batch 050 V9 Index](batch_050_v9_index.md).\n"
    (ROOT / "analysis/batch_050_mdr_mhk_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_050_v9_index.md").write_text(make_index(IDEAS), encoding="utf-8")
    payload = make_payload(IDEAS)
    (ROOT / "data/curated/batch_050_mdr_mhk_deep_v7.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {"batch": "050", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + official filings + repository performance multipliers", "record_count": 10, "direction_audit": "complete", "direction_corrections": 5, "security_corrections": 2, "performance_rows_preserved": 7, "performance_rule": "actual direction price-only; CDS and bond return remain null", "candidates": [{"idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"], "raw_direction": "Short" if i["raw_short"] else "Long", "research_direction": i["direction"], "security": i["security"], "description_chars": i["desc"], "catalyst_chars": i["cat"], "performance_available": i["id"] in PERF, "canonical_report": i["filename"]} for i in IDEAS]}
    (ROOT / "data/curated/batch_050_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {"source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10, "raw_descriptions_present_in_attachment": 6, "raw_catalysts_verified": 10, "repository_performance_rows_preserved": 7, "direction_corrections": 5, "security_corrections": 2, "note": "첨부 SQL의 10개 catalyst와 6개 description을 확인했다. MHK multiplier는 실제 Long/Short 방향으로 교정했고 CDS·MDR notes 정확성과는 null이다."}
    (ROOT / "data/curated/batch_050_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ideas={len(payload['ideas_master'])} postmortems={len(payload['postmortems'])} sections={len(payload['sections'])} claims={len(payload['claims'])} metrics={len(payload['metrics'])} timeline={len(payload['timeline'])} sources={len(payload['sources'])}")


if __name__ == "__main__":
    main()
