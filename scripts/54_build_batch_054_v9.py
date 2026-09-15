#!/usr/bin/env python3
"""Build Batch 054 Office Depot / Boca Resorts / Rosetta Stone V9 artifacts."""
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
    "odp": (
        "Office Depot/The ODP Corporation은 시기별로 retail superstore, contract B2B delivery, International/Viking, CompuCom IT services를 묶어 운영했다. "
        "현금엔진은 `customer·store sales×gross margin-store·warehouse·salesforce·delivery opex-inventory/receivable investment-remodel·closure·growth capex-interest·tax`다. "
        "점포·DC·본사 비용을 매출보다 빨리 줄이면 쇠퇴산업에서도 현금이 늘지만, 매출 감소가 고정비 축소를 앞서면 역레버리지가 발생한다. SOTP는 shared cost·lease·working capital·폐점비와 failed-acquisition loss를 각 자산에 완전 배분해야 한다."
    ),
    "boca": (
        "Boca Resorts는 South Florida의 destination resorts, golf clubs, spas, marinas와 private clubs를 보유·운영한 호텔 자산회사였다. "
        "현금엔진은 `available room nights×occupancy×ADR+club·golf·spa·marina revenue-property payroll·F&B·marketing·maintenance capex-interest·tax`다. "
        "trophy location과 management-contract 비구속성은 strategic value를 만들지만 book/replacement value가 common cash가 되려면 property debt·deferred capex·tax와 control structure를 차감하고 실제 매각확률을 붙여야 한다."
    ),
    "rst": (
        "Rosetta Stone은 consumer·Enterprise & Education language learning과 2013년 인수한 K-12 literacy 사업 Lexia를 운영했다. 현금엔진은 "
        "`paid learners/contracts×price·renewal-gross service/content cost-sales & marketing-R&D-G&A-capitalized content·working capital-tax`다. "
        "CD에서 subscription으로 바뀌어도 경제성이 자동 개선되는 것은 아니다. unit growth, AOV, CAC, retention, cohort contribution, deferred-revenue timing을 분리해야 한다. "
        "2018년 이후에는 회사 평균보다 Lexia의 bookings·renewal·growth·standalone value가 더 중요한 SOTP 변수가 됐다."
    ),
})

m.SOURCES.update({
    "odp": [
        m.S("Office Depot SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=800240&owner=exclude", "SEC / Office Depot", "1994-2026", "segment·capital allocation·corporate action 연속성"),
        m.S("Office Depot 2008 operating results", "https://www.sec.gov/Archives/edgar/data/800240/000095014409001557/g17789exv99w1w1.htm", "SEC / Office Depot", "2009-02-24", "Retail·BSD sales와 operating-profit collapse"),
        m.S("2014 synergy progress", "https://www.sec.gov/Archives/edgar/data/800240/000119312514294475/d767739dex991.htm", "SEC / Office Depot", "2014-08-05", "OfficeMax integration, synergy 상향과 store rationalization"),
        m.S("Staples transaction announcement", "https://www.sec.gov/Archives/edgar/data/791519/000110465915006462/a15-3714_1ex99d1.htm", "SEC / Staples", "2015-02-04", "$7.25 cash+0.2188 Staples share·$11 implied value"),
        m.S("FTC Staples/Office Depot case", "https://www.ftc.gov/legal-library/browse/cases-proceedings/1510065-staplesoffice-depot", "U.S. Federal Trade Commission", "2015-2016", "대형 B2B customer market antitrust challenge와 거래 중단"),
        m.S("Office Depot 2018 Form 10-K", "https://www.sec.gov/Archives/edgar/data/800240/000156459019004964/odp-10k_20181229.htm", "SEC / Office Depot", "2019-02-27", "CompuCom goodwill·fair-value cushion과 transformation 위험"),
        m.S("Office Depot 2019 Form 10-K", "https://www.sec.gov/Archives/edgar/data/800240/000156459020006770/odp-10k_20191228.htm", "SEC / Office Depot", "2020-02-26", "CompuCom operating loss와 segment cash"),
        m.S("ODP 1-for-10 reverse split", "https://www.sec.gov/Archives/edgar/data/800240/000156459020030669/odp-ex991_7.htm", "SEC / Office Depot", "2020-06-19", "2020-06-30 reverse split price basis"),
        m.S("Staples $40 proposal / ODP response", "https://www.sec.gov/Archives/edgar/data/800240/000119312521010881/d95194dex991.htm", "SEC / The ODP Corporation", "2021-01-19", "whole-company proposal와 retail/consumer 관심"),
        m.S("ODP B2B separation plan", "https://www.sec.gov/Archives/edgar/data/800240/000119312521150726/d386868dex991.htm", "SEC / The ODP Corporation", "2021-05-05", "B2B Solutions Provider와 consumer 분리 계획"),
        m.S("CompuCom sale", "https://www.sec.gov/Archives/edgar/data/800240/000119312522000224/d221869dex991.htm", "SEC / The ODP Corporation", "2021-12-31", "CompuCom 최대 $305m 매각"),
        m.S("ODP 2022 Form 10-K", "https://www.sec.gov/Archives/edgar/data/800240/000156459023002902/odp-10k_20221231.htm", "SEC / The ODP Corporation", "2023-03-01", "two-company separation 취소와 common ownership 재편"),
    ],
    "boca": [
        m.S("Boca Resorts SEC archive", "https://www.sec.gov/Archives/edgar/data/1020905/", "SEC / Boca Resorts", "1997-2004", "RST ticker, annual reports와 merger filings"),
        m.S("Boca Resorts 10-K search", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001020905&type=10-K", "SEC / Boca Resorts", "1997-2004", "portfolio·debt·cash-flow disclosures"),
        m.S("Boca Resorts merger proxy", "https://www.sec.gov/Archives/edgar/data/1020905/000095014404011165/g91505ddefm14a.htm", "SEC / Boca Resorts", "2004-11-15", "Blackstone affiliate, $24 cash, portfolio와 voting control"),
        m.S("Merger consideration ownership filing", "https://www.sec.gov/Archives/edgar/data/1020905/000129378804000015/xslF345X02/primary_doc.xml", "SEC / Boca Resorts", "2004", "transaction-related security disposition evidence"),
    ],
    "rst": [
        m.S("Rosetta Stone SEC filing archive", "https://www.sec.gov/edgar/browse/?CIK=1351285&owner=exclude", "SEC / Rosetta Stone", "2009-2020", "IPO 이후 unit economics·cash·subscription·transaction filings"),
        m.S("Rosetta Stone 2012 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1351285/000104746913002346/a2213285z10-k.htm", "SEC / Rosetta Stone", "2013-03-15", "2010~12 revenue·operating income·loss와 share-price ranges"),
        m.S("2013 cash-generation materials", "https://www.sec.gov/Archives/edgar/data/1351285/000110465914012931/a14-6648_1ex99d2.htm", "SEC / Rosetta Stone", "2014-02", "2012/13 FCF와 2014 guidance"),
        m.S("Lexia acquisition", "https://www.sec.gov/Archives/edgar/data/1351285/000110465913056496/a13-17097_1ex99d1.htm", "SEC / Rosetta Stone", "2013-07-22", "$22.5m Lexia acquisition"),
        m.S("Rosetta Stone 2020 proxy", "https://www.sec.gov/Archives/edgar/data/1351285/000156459020017251/rst-pre14a_20200611.htm", "SEC / Rosetta Stone", "2020-04-16", "2019 Literacy revenue와 segment evolution"),
        m.S("Cambium acquisition agreement", "https://www.sec.gov/Archives/edgar/data/1351285/000119312520235565/d60457dex991.htm", "SEC / Rosetta Stone", "2020-08-31", "$30/share cash·약 $792m equity value"),
        m.S("Cambium acquisition completion", "https://www.sec.gov/Archives/edgar/data/1351285/000119312520269980/d84157dex991.htm", "SEC / Rosetta Stone", "2020-10-15", "거래 종결과 standalone RST terminal event"),
    ],
})


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**x):
    x["claims"] = [C(*row) for row in x.pop("claimdata")]
    x.setdefault("security", "Common stock")
    x.setdefault(
        "waterfall",
        "Segment operating cash에서 working capital·maintenance/growth capex·lease/closure cost·interest·tax를 차감한다. historical margin과 gross SOTP는 common cash가 아니며, downturn runway와 shared cost를 먼저 뺀다.",
    )
    x.setdefault("contest", False)
    return x


IDEAS = [
I(id="1df346ed-fb64-433c-96a0-f0c0512e6d34", date="2007-12-27", author="gigi404", ticker="ODP", entity="Office Depot, Inc.", group="odp", raw_short=True, direction="Long", entry="약 $13.60", horizon="2~3년", filename="analysis/ideas/2007/2007-12-27_ODP_long.md", link="https://www.valueinvestorsclub.com/idea/Office_Depot_Inc./1072611756", desc=0, cat=142, title="70% drawdown·5% normalized margin Long", verdict="정상매출·margin·buyback 핵심 실패, 정확 수익률 미검증", score=3.2, process=6.4,
summary="2007-03 Long 이후 주가가 고점 $46에서 약 $13.60으로 70% 가까이 하락한 뒤에도 raw Short가 아니라 $23~32를 기대한 Long이다. 2008 하반기 earnings 회복, modest sales growth, 2009/10 operating margin 5.0/5.2%와 연 2% buyback을 가정해 8x 2006 EPS·10x 미만 forward EPS가 과도하다고 봤다.",
valuation="2009 model은 sales $16.5bn×5.0% margin→net income $504m, 260m shares, EPS $1.94, 12~15x=$23.25~29.06이다. 2010은 sales $17.325bn×5.2%→EPS $2.17, 12~15x=$26.03~32.53이다. 문제는 low multiple이 아니라 prior-cycle 5% margin과 modest sales growth를 denominator에 넣은 것이다.",
actual="2008 North American Retail sales는 10% 감소하고 operating profit은 2007 $354.5m에서 -$29.2m으로 붕괴했다. BSD sales는 8% 감소, operating profit은 $220.1m에서 $119.8m으로 줄었다. 2H08 recovery·5% margin·buyback의 세 축이 동시에 실패했고 thesis는 growth/recovery에서 restructuring으로 바뀌었다.",
price="첨부 SQL에는 catalyst 142자만 있고 description·performance COPY는 없다. 기존 초안의 수익률은 사용하지 않는다. $13.60과 $23~32 target만 prior curated T0 anchor이며 exact return/IRR은 null이다.",
drivers="손실은 multiple compression보다 매출 하락×store/warehouse fixed cost의 negative operating leverage가 만들었다. 이미 70% 하락한 가격도 normal EPS가 더 크게 무너지면 안전마진이 아니다. buyback은 downturn cash를 지키지 못하는 capital-use risk였다.",
error="GFC 예측 실패보다 T0부터 보인 comps 둔화와 1H08 earnings decline을 5% normalized margin에 충분히 반영하지 않은 것이 핵심이다. 2006 EPS와 5% margin을 normal로 두고 share count 감소까지 더해 earnings denominator를 세 번 낙관했다.", first_signal="Retail comps≤-3%, gross margin -100bp 또는 store/warehouse expense deleverage가 나타나면 5% margin을 제거하고 recession EBIT·liquidity 기준으로 재평가한다. 2H08 recovery가 한 분기 밀리면 catalyst도 재승인한다.",
metrics=[("Entry/target", "$13.60", "$23~32", "exact return null", "실패"),("2009 sales", "$16.5bnE", "modest growth", "Retail -10% 2008", "실패"),("Operating margin", "5.0%/5.2% E", "정상화", "Retail segment 적자", "대실패"),("Retail profit", "$354.5m 2007", "회복", "-$29.2m 2008", "대실패"),("BSD profit", "$220.1m 2007", "rebound", "$119.8m 2008", "실패")],
timeline=[("2006", "높은 EPS/margin 기준", "valuation anchor"),("2007-03", "선행 ODP Long", "turnaround extrapolation"),("2007-12-27", "VIC Long", "$13.60"),("2008-H1", "earnings 악화", "first break"),("2008-H2", "예상 recovery 미발생", "catalyst 실패"),("2008-FY", "Retail 영업적자", "core 반증"),("2009", "구조조정·점포축소", "thesis 전환")],
claimdata=[("2H08 earnings 회복", "상반기 약세 뒤 earnings가 돌아온다.", "SQL catalyst", "recession이 짧고 comps가 안정된다.", "2H08에도 estimate cut이면 반증.", "GFC 심화·영업적자", "실패", "시간촉매는 분기별 재승인한다."),("5% normalized margin", "2009/10 5.0/5.2%가 정상이다.", "과거 margin·cost plan", "매출 감소에도 fixed cost를 빨리 뺀다.", "sales -5%에서 margin<2%면 반증.", "Retail 적자", "대실패", "normal margin은 recession bridge와 함께 쓴다."),("modest sales growth", "$16.5bn→$17.3bn이면 된다.", "낮아진 기대", "office spending·traffic이 안정된다.", "segment sales -5%면 반증.", "Retail -10%·BSD -8%", "실패", "cyclical sales에는 downside volume을 먼저 둔다."),("buyback accretion", "연 2% share shrink가 EPS를 지지한다.", "과거 repurchase·SQL catalyst", "FCF가 downturn 필요현금보다 크다.", "cash burn에도 buyback이면 반증.", "liquidity 보존이 더 중요", "실패", "buyback은 survival capital 뒤에 둔다."),("low P/E floor", "8x 2006 EPS/10x forward는 싸다.", "$13.60", "E가 정상치와 가깝다.", "EPS -30%면 반증.", "denominator 붕괴", "실패", "주가 drawdown과 valuation margin을 구분한다."),("Long direction", "raw Short가 아니라 $23~32 상승 payoff다.", "target·buyback catalyst", "동일 common 기준이다.", "negative target/borrow가 확인되면 반증.", "Long으로 교정", "성공", "방향은 원문 payoff로 정한다.")]),

I(id="8ae12761-8e65-4342-91da-9585344293c9", date="2014-04-05", author="frankie3", ticker="ODP", entity="Office Depot, Inc.", group="odp", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="12~24개월", filename="analysis/ideas/2014/2014-04-05_ODP_long.md", link="https://www.valueinvestorsclub.com/idea/OFFICE_DEPOT_INC/1913808579", desc=0, cat=235, title="OfficeMax cost-out·capacity shrink·$7.25 Long", verdict="self-help·target 성공, 최종 Staples 거래는 antitrust 실패·정확 수익률 미검증", score=9.0, process=9.2,
summary="raw Short와 달리 2.2x 2016E EBITDA에서 $7.25/share fair value를 제시한 Long이다. secular decline을 부정하지 않고 OfficeMax 중복비용·점포·DC를 수요보다 빨리 줄여 $600m+ synergy와 working-capital benefit을 얻는다고 봤다. ODP 최대 450개와 Staples 225개 폐점이 industry capacity 약 20%를 줄이는 supply-side thesis다.",
valuation="원문은 2016E EBITDA의 약 2.2x인 시장가를 4x로만 재평가해 $7.25를 산출했다. payoff는 self-help cost-out과 strategic consolidation 두 층이다. 2015 Staples 계약은 $7.25 cash+0.2188 Staples share, 당시 약 $11 implied value였지만 antitrust probability·deal break price를 별도 확률가중해야 했다.",
actual="2014 company는 annual run-rate synergy 전망을 $700m+로 높이고 그해 최소 $220m 실현을 예상했으며 168 stores를 닫았다. 2015 Staples가 약 $11 implied value로 계약해 $7.25 target과 strategic value를 확인했다. 그러나 FTC가 대형 B2B customer 시장의 경쟁저하를 문제 삼았고 2016 법원 injunction 뒤 거래가 중단됐다. ODP는 $250m termination fee를 받았다.",
price="첨부 SQL에는 catalyst 235자만 있고 description·performance는 없다. $7.25 target과 $11 transaction value는 event anchors이며 exact total return/IRR은 null이다. target hit와 final merger completion을 같은 성과로 합치지 않는다.",
drivers="단기 가치창출은 revenue growth가 아니라 duplicated store/DC/G&A capacity를 실제로 제거한 데서 나왔다. strategic buyer는 추가 synergy를 가격에 반영했지만 마지막 두-player consolidation은 antitrust gate에 막혔다. target 도달 뒤 투자성격이 self-help Long에서 merger arb로 바뀌었다.",
error="$600m synergy와 store closures는 비교적 검증 가능했지만 industry consolidation을 자연스러운 종착점으로 본 것은 규제시장 정의를 과소평가했다. declining revenue가 cost-out 이후 다시 EBITDA를 잠식하는 terminal case와 closure liability도 더 명시해야 했다.", first_signal="분기 realized synergy가 계획의 75% 미만이거나 closure 뒤 retained-store comps·B2B retention이 악화하면 $7.25 base를 낮춘다. Staples deal 후에는 FTC가 national large-account B2B를 별도시장으로 정의하는 순간 새 merger-arb로 재심사한다.",
metrics=[("Valuation", "2.2x 2016E EBITDA", "4x/$7.25", "event value $11", "성공"),("Synergy", "$600m+", "$700m+ run-rate", "$700m+ 상향", "성공"),("2014 realization", "integration 초기", "$220m+", "$220m+ 예상", "성공"),("Store closures", "최대 450 계획", "capacity shrink", "168개 2014", "성공"),("Staples deal", "strategic option", "$11 implied", "FTC 차단", "value 성공/event 실패")],
timeline=[("2013-11", "OfficeMax merger 완료", "cost-out 시작"),("2014-04-05", "VIC Long", "$7.25"),("2014", "synergy $700m+ 상향", "self-help 성공"),("2014", "168 stores 폐점", "capacity 제거"),("2015-02-04", "Staples 계약", "$11 implied"),("2015-12", "FTC challenge", "regulatory break"),("2016-05", "injunction·deal 중단", "$250m fee")],
claimdata=[("$600m+ synergy", "중복비용 제거가 revenue decline을 앞선다.", "OfficeMax overlap", "execution·retention이 유지된다.", "realized<75% plan이면 반증.", "$700m+ outlook", "성공", "쇠퇴산업은 demand보다 supply/cost 속도를 본다."),("store rationalization", "450 ODP+225 Staples closure가 capacity를 줄인다.", "overlap·store economics", "폐점매출이 retained 채널로 이전된다.", "transfer rate 낮고 closure cost 급증이면 반증.", "168 stores 2014·계획 진행", "성공", "closure gross saving에서 leakage를 뺀다."),("secular<cost-out", "단기 EBITDA는 수요감소보다 빨리 개선된다.", "synergy schedule", "headwind가 완만하다.", "organic decline>synergy면 반증.", "2014~15 value direction", "기간 성공", "영구 turnaround가 아닌 시간제한 trade로 본다."),("net cash runway", "integration을 balance sheet가 버틴다.", "net cash", "working capital·closure cash가 계획 내다.", "cash burn·debt 증가면 반증.", "self-help와 fee 수취", "성공", "synergy에는 cash realization timing을 붙인다."),("$7.25 fair value", "4x 2016E EBITDA가 보수적이다.", "2.2x entry", "EBITDA bridge가 맞다.", "2016E EBITDA -25%면 반증.", "$11 strategic value", "강한 성공", "target hit 후 thesis를 재심사한다."),("최종 consolidation", "Staples 결합이 industry value를 완성한다.", "strategic logic", "FTC가 broad office-supply market을 쓴다.", "large B2B 별도시장 정의면 반증.", "FTC 차단", "실패", "전략가치와 규제가능성을 분리한다.")]),

I(id="d0e31976-8a76-43ec-a94d-c425bbae0cb8", date="2018-08-13", author="TomMurner", ticker="ODP", entity="Office Depot, Inc.", group="odp", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="3~5년", filename="analysis/ideas/2018/2018-08-13_ODP_long.md", link=None, desc=0, cat=47, title="B2B/services transformation·high-teens FCF yield Long", verdict="CompuCom transformation 실패·legacy value 일부 잔존, 정확 수익률 미검증", score=4.5, process=7.2,
summary="raw Short와 달리 conservative case도 30%+ IRR을 제시한 Long이다. Retail·Business Solutions가 각각 약 45%, CompuCom이 약 10%인 회사를 office retailer가 아니라 B2B/services omnichannel platform으로 재평가해야 한다고 봤다. high-teens FCF yield와 3%대 dividend, non-recourse debt 조정을 하방으로 썼다.",
valuation="원문은 dividend, FCF yield, SOTP와 LBO IRR을 병렬 사용했다. 그러나 모든 방법이 2017 약 $1bn에 인수한 CompuCom의 growth·cross-sell·margin 개선이라는 공통 assumption에 종속됐다. CompuCom을 0 또는 impairment/salvage로 두고 legacy B2B·retail FCF만으로 싼지 먼저 봐야 했다.",
actual="2018 Q4 CompuCom fair value는 carrying value보다 약 4% 높은 수준에 불과했고 2019에는 revenue/profitability shortfall과 operating loss가 나타났다. 2021 ODP는 CompuCom을 최대 $305m에 매각했다. 원 purchase price 약 $1bn 대비 transformation engine 가정은 강하게 반증됐다. legacy cash와 B2B asset은 남았지만 company rerating 논리는 실패했다.",
price="현 SQL에는 catalyst 47자만 있고 description·performance가 없다. 기존 return 값은 없으며 high-teens FCF yield·30%+ IRR은 prior curated T0 claim으로만 보존한다. exact return/IRR은 null이다.",
drivers="가치누수는 싸게 보인 legacy FCF를 비싼 growth acquisition에 재투자한 capital allocation에서 나왔다. service revenue mix가 늘어도 incremental ROIC와 organic retention이 낮으면 retailer multiple을 벗어날 수 없다. dividend는 이 손실을 막는 floor가 아니었다.",
error="goodwill과 strategic fit을 moat로 취급했고 recently acquired business의 cohort·cross-sell evidence 없이 LBO/SOTP/FCF 세 방법을 사용했다. 방법 수가 많아도 동일 assumption이면 독립 검증이 아니다. management tenure와 FY18 muted guidance도 더 큰 haircut이 필요했다.", first_signal="CompuCom organic revenue가 감소하고 segment operating margin이 3% 아래거나 fair-value cushion<10%이면 transformation multiple을 제거하고 salvage value만 사용한다. consolidated FCF가 배당+integration spend를 못 덮으면 downside floor도 제거한다.",
metrics=[("Business mix", "Retail/BSD 각 ~45%", "services rerating", "CompuCom underperformance", "실패"),("CompuCom cost", "약 $1bn 2017", "growth engine", "최대 $305m sale", "대실패"),("Fair-value cushion", "확대 기대", "goodwill 보호", "약 4% Q4'18", "첫 반증"),("2019 result", "cross-sell 기대", "profitability", "operating loss", "실패"),("FCF/dividend", "high-teens/~3%대", "하방", "capital loss 상쇄 못함", "부분")],
timeline=[("2017", "CompuCom 약 $1bn 인수", "transformation bet"),("2018-08-13", "VIC Long", "B2B rerating"),("2018-Q4", "fair-value cushion 약 4%", "first break"),("2019-Q1", "revenue/profitability shortfall", "cross-sell 반증"),("2019-FY", "CompuCom operating loss", "core failure"),("2021-12", "최대 $305m sale 발표", "salvage"),("2022", "legacy businesses 재편", "narrative 종료")],
claimdata=[("CompuCom engine", "IT services가 B2B transformation을 만든다.", "$1bn acquisition·cross-sell", "organic growth·margin이 개선된다.", "organic decline·margin<3%면 반증.", "operating loss·$305m sale", "대실패", "transformation M&A는 incremental ROIC로 검증한다."),("Workonomy cross-sell", "one-stop-shop가 wallet share를 높인다.", "B2B customer base", "salesforce가 service를 낮은 CAC로 판다.", "attach rate·retention 부재면 반증.", "경제성 입증 실패", "실패/미검증", "브랜드명보다 cohort attach와 margin을 본다."),("B2B rerating", "retail이 아닌 services multiple을 받는다.", "mix 약 55% non-retail", "quality가 reporting label과 함께 바뀐다.", "service segment loss면 반증.", "multiple unlock 제한", "실패", "mix보다 business quality가 multiple을 결정한다."),("high-teens FCF yield", "legacy cash가 하방을 보호한다.", "FCF valuation", "M&A/working capital이 cash를 소모하지 않는다.", "FCF<배당+integration이면 반증.", "legacy value 일부만 잔존", "부분", "owner earnings에서 capital allocation을 뺀다."),("dividend floor", "3%대 yield가 downside를 제한한다.", "cash dividend", "지급이 유지되고 capital loss가 작다.", "coverage<1x면 반증.", "transformation 손실 방어 못함", "약함", "배당은 valuation floor가 아니다."),("Long direction", "raw Short가 아니라 30%+ IRR Long이다.", "positive payoff", "same common 기준", "short borrow/negative target 확인 시 반증.", "Long으로 교정", "성공", "direction은 기대 payoff로 판정한다.")]),

I(id="dbfb855f-c606-4552-8108-ebbd8801df0d", date="2019-04-22", author="maybeman", ticker="ODP", entity="Office Depot, Inc.", group="odp", raw_short=True, direction="Long", entry="약 $2.40 (2020 reverse split 전)", horizon="2~4년", filename="analysis/ideas/2019/2019-04-22_ODP_long.md", link="https://www.valueinvestorsclub.com/idea/Office_Depot/4422513198", desc=0, cat=116, title="B2B SOTP·23~25% FCFE yield·failed-M&A salvage Long", verdict="asset separation·salvage 방향 성공, full value·정확 수익률 미검증", score=8.8, process=9.4,
summary="raw Short와 달리 약 $2.40 pre-split에서 23~25% FCFE yield와 B2B SOTP를 제시한 Long이다. 2018과 달리 CompuCom을 hero가 아니라 impairment risk로 낮추고, stress EBITDA $500m 대비 EV 3.4x, B2B EBITDA 약 $320m×7x가 EV 대부분을 덮으며 Retail 약 $250m EBITDA는 거의 무료라고 봤다.",
valuation="equity 약 $1.3bn, adjusted EV 최대 $1.685bn, stress EBITDA $500m으로 3.4x다. B2B $320m×7=$2.24bn에서 CompuCom/corporate drag를 빼 약 $1.68bn, $3.10/share로 계산했다. FCFE 약 $300m은 23~25% yield다. 2020 1-for-10 split 때문에 $2.40은 후속 가격과 비교할 때 $24 basis로 조정해야 한다.",
actual="2020 1-for-10 reverse split 뒤 2021 Staples는 $40 cash proposal을 냈다. 이는 pre-split $4 basis로 2019 valuation gap과 buyer interest를 확인하지만 exact return은 아니다. ODP는 2021 B2B separation plan을 발표하고 CompuCom을 최대 $305m에 매각했다. 2022에는 two-company spin을 취소해 full SOTP crystallization은 미완이다.",
price="첨부 SQL에는 catalyst 116자만 있고 description·performance가 없다. $2.40, $3.10 SOTP, 23~25% FCFE와 $40 post-split proposal은 anchor다. split·dividend·실제 보유경로가 포함된 performance row가 없어 exact return/IRR은 null이다.",
drivers="이전보다 강해진 이유는 실패한 CompuCom을 upside에서 downside로 옮기고 B2B·Retail cash를 자산별로 나눈 점이다. buyer proposal·separation plan·CompuCom sale이 asset proof를 제공했다. value는 transformation 성공이 아니라 실패해도 남는 cash asset에서 왔다.",
error="$320m B2B EBITDA×7x에 standalone corporate cost·customer concentration·working capital을 더 엄격히 배분해야 했다. FCFE $300m도 secular revenue decline과 closure capex를 full-cycle로 normalize해야 한다. strategic optionality를 가격에 미리 전액 넣으면 안 된다.", first_signal="B2B organic sales와 margin이 동시에 하락해 EBITDA<$250m, consolidated FCFE<$200m 또는 separation timetable이 12개월 이상 미뤄지면 $3.10 SOTP와 23~25% yield를 낮춘다.",
metrics=[("Entry basis", "$2.40 pre-split", "$3.10+ SOTP", "$24 post-split basis", "방향 성공"),("Adjusted EV", "$1.685bn", "3.4x stress EBITDA", "buyer/asset actions", "가치 방향"),("B2B EBITDA", "$320m", "7x/$2.24bn", "separation plan", "부분 성공"),("FCFE", "$300m", "23~25% yield", "exact cash cohort 없음", "미검증"),("CompuCom", "impairment risk", "salvage", "최대 $305m sale", "성공")],
timeline=[("2018", "CompuCom thesis 약화", "framework change"),("2019-04-22", "VIC Long", "$2.40 pre-split"),("2020-06-30", "1-for-10 reverse split", "basis $24"),("2021-01", "Staples $40 proposal", "buyer evidence"),("2021-05", "B2B separation plan", "SOTP catalyst"),("2021-12", "CompuCom sale", "salvage"),("2022", "two-company spin 취소", "full unlock 미완")],
claimdata=[("B2B quality", "B2B는 retail보다 높은 multiple 자산이다.", "$320m EBITDA·delivery density", "retention·standalone overhead가 안정적이다.", "organic decline+margin 하락이면 반증.", "buyer·separation plan으로 차별화", "성공 방향", "SOTP는 자산별 KPI와 buyer를 찾는다."),("CompuCom downside", "growth hero가 아니라 impairment/salvage다.", "2018 cushion·underperformance", "더 큰 cash drain이 없다.", "추가 대규모 support면 반증.", "$305m sale", "성공", "실패 M&A는 original cost 대신 third-party bid를 쓴다."),("Retail free option", "$250m EBITDA가 current EV에 거의 무료다.", "residual SOTP", "closure/lease가 negative value가 아니다.", "four-wall cash<closure cost면 반증.", "Staples 관심", "부분 성공", "free option에도 lease·working capital을 붙인다."),("23~25% FCFE", "$300m cash yield가 시간을 보상한다.", "stress EBITDA bridge", "maintenance/closure capex가 충분히 반영됐다.", "FCFE<$200m이면 반증.", "exact cohort 미복원", "미검증", "decliner FCFE는 runoff capex를 포함한다."),("corporate action", "M&A·분리가 SOTP를 드러낸다.", "SQL catalyst", "board와 buyer가 실행한다.", "timetable 철회면 반증.", "proposal·계획·sale, spin은 취소", "부분 성공", "event는 단계별 확률을 둔다."),("split normalization", "nominal price를 1:10으로 맞춰야 한다.", "2020 reverse split", "다른 분배·배당이 반영된다.", "unadjusted 비교면 오류.", "$2.40→$24 basis 교정", "성공", "corporate action 전후 price basis를 고정한다.")]),

I(id="33258e7a-c5fc-4c9c-a10b-ba2c96016a06", date="2021-01-19", author="BlueFIN24", ticker="ODP", entity="The ODP Corporation", group="odp", raw_short=True, direction="Long", entry="Staples $40 proposal 이후", horizon="12~36개월", filename="analysis/ideas/2021/2021-01-19_ODP_long.md", link="https://www.valueinvestorsclub.com/idea/ODP_CORP/5150473520", desc=0, cat=124, title="$40 bid 뒤 $80 asset-separation SOTP Long", verdict="CompuCom salvage 정확·asset actions 부분 성공, $80 완전실현 미검증", score=8.4, process=9.2,
summary="raw Short와 달리 Staples/Sycamore의 $40 cash proposal 뒤에도 약 $80 SOTP를 제시한 Long이다. Retail 약 $20, CompuCom 약 $6, B2B 약 $47, cash 약 $7로 나눴다. buyer가 실제 원하는 retail/consumer와 dense next-day B2B logistics network를 분리하면 whole-company bid보다 가치가 크다는 event-driven thesis다.",
valuation="SOTP는 Retail operating profit 약 $250m×5x≈$20/share, CompuCom salvage 약 $300m≈$6, B2B 2021 operating profit 약 $250m×10x≈$47, cash 약 $7로 합계 $80이다. 각 leg에 sale/spin probability, tax·standalone cost·time discount를 곱해야 하며 announced action을 completed payoff로 보면 안 된다.",
actual="ODP board는 Staples가 retail/consumer ecommerce에 관심 있다고 설명했고 2021-05 B2B Solutions Provider 분리계획을 발표했다. 2021-12 CompuCom은 최대 $305m에 팔려 원문 $300m salvage를 매우 가깝게 확인했다. 그러나 2022 company는 businesses를 common ownership 아래 두기로 바꿔 B2B public spin과 full $80 crystallization은 완결되지 않았다.",
price="현재 SQL에는 catalyst 124자만 있고 description·performance가 없다. $40 proposal과 $80 SOTP는 event/value anchors다. 실제 transaction close, distributions와 holding-period performance가 없어 exact return/IRR은 null이다.",
drivers="가장 재사용 가능한 edge는 2017 $1bn purchase price를 버리고 2021 third-party salvage를 $300m로 낮춘 것이다. 실제 sale headline이 최대 $305m였다. 반면 B2B 10x와 public spin은 board decision·standalone costs·execution time에 노출돼 미완으로 남았다.",
error="$80을 산술합으로 제시하면서 four-leg의 correlation과 tax·overhead·time을 충분히 할인하지 않았다. Staples가 retail을 원한다는 사실은 $20 floor evidence지만 B2B 10x를 보장하지 않는다. board가 separation을 철회할 governance option도 base에 들어가야 했다.", first_signal="CompuCom bid가 $250m 아래거나 B2B separation Form 10/timetable이 2개 분기 이상 지연되고 B2B operating profit<$200m이면 $80 SOTP를 $40~50대로 즉시 재산정한다.",
metrics=[("Staples proposal", "$40 cash", "더 높은 SOTP", "whole deal 미완", "value evidence"),("Retail", "약 $20/share", "sale", "buyer 관심", "부분 성공"),("CompuCom", "약 $6/$300m", "salvage", "최대 $305m", "강한 성공"),("B2B", "약 $47/10x", "public separation", "계획 후 취소", "미완"),("Total SOTP", "약 $80", "12~36개월", "full crystallization 없음", "미검증")],
timeline=[("2021-01-11", "Staples $40 proposal", "event 시작"),("2021-01-19", "ODP response·VIC Long", "$80 SOTP"),("2021-03", "추가 asset proposal", "retail interest"),("2021-05", "B2B spin plan", "hard catalyst"),("2021-12", "CompuCom 최대 $305m sale", "salvage 적중"),("2022", "two-company separation 취소", "core delay/실패"),("2023", "OBS·Veyer·Varis 내부 재편", "common ownership")],
claimdata=[("Retail buyer value", "Staples가 원하는 consumer asset은 약 $20/share다.", "$40 whole-company proposal", "deal perimeter·liability가 분리된다.", "asset bid<$15/share면 반증.", "retail 관심은 확인·sale 미완", "부분 성공", "buyer intent와 closed price를 나눈다."),("CompuCom $300m", "failed M&A의 salvage가 약 $6/share다.", "third-party value estimate", "추가 liabilities가 작다.", "bid<$250m이면 반증.", "최대 $305m sale", "강한 성공", "salvage는 sunk cost가 아니라 현 bid다."),("B2B logistics moat", "density·SLA·procurement integration이 10x를 받는다.", "$250m operating profit", "standalone retention·cost가 안정적이다.", "profit<$200m이면 반증.", "분리계획은 있었으나 독립상장 없음", "부분", "moat는 fill-rate·retention·unit cost로 본다."),("cash $7/share", "순현금이 분리비용 뒤 주주에게 남는다.", "balance sheet", "tax·closure·working capital이 제한적이다.", "event cash use>$5/share면 반증.", "정확 분배 미복원", "미검증", "cash는 use-of-cash 후 센다."),("$80 crystallization", "네 leg가 12~36개월에 현실화된다.", "proposal·board review", "events가 순차 완결된다.", "spin 취소면 반증.", "2022 spin 취소", "실패/부분", "SOTP 각 leg에 확률·시간을 곱한다."),("Long direction", "raw Short가 아니라 $80 upside Long이다.", "positive SOTP", "동일 ODP common 기준", "negative payoff 확인 시 반증.", "Long으로 교정", "성공", "bid 이후에도 방향은 incremental payoff로 정한다.")]),

I(id="a18a84e4-1831-42eb-8ae9-b45fc110bac8", date="2002-04-07", author="alli718", ticker="RST", entity="Boca Resorts, Inc.", group="boca", raw_short=False, direction="Long", entry="약 $12.85", horizon="2~4년", filename="analysis/ideas/2002/2002-04-07_RST_boca_resorts_long.md", link="https://www.valueinvestorsclub.com/idea/Boca_Resorts_Inc/7610357754", desc=0, cat=925, security="Boca Resorts Class A common stock", title="trophy-resort scarcity·$20.29 private-value Long", verdict="$24 cash takeout로 asset·sale 논지 강한 성공, exact return은 null", score=9.4, process=9.5,
summary="raw company mapping의 Rosetta Stone이 아니라 2002년 NYSE `RST`였던 Boca Resorts Long이다. 약 $12.85·tangible book $11.67에서 normalized cash flow 약 $110m, maintenance capex 후 약 $95m을 사용해 trophy South Florida resorts의 private value $20.29를 계산했다. travel recovery·repurchase·debt buyback과 strategic sale이 촉매였다.",
valuation="normalized cash flow $110m×9=$990m에서 debt $184.4m을 빼고 39.7m shares로 나누면 $20.29다. maintenance capex 후 $95m FCF는 당시 EV 대비 약 13.6% property cash yield로 제시됐다. book와 normalized cash는 참고치이고 deferred maintenance·tax·property debt·control을 차감한 net sale proceeds가 common payoff다.",
actual="2004-10 Boca Resorts board는 Blackstone affiliate와 합병계약을 승인했고 1주당 $24 cash를 제시했다. proxy는 five destination resorts와 golf·spa·marina assets, H. Wayne Huizenga의 약 98% voting power와 $24 consideration을 확인한다. $24는 원문 $20.29를 상회해 trophy scarcity·control sale 논지를 직접 검증했다.",
price="현 SQL에는 catalyst 925자만 있고 description·performance는 없다. $12.85·$20.29·$24는 T0와 transaction anchors다. 게시일 종가·배당·세금·정확 closing 보유기간을 포함한 performance row가 없으므로 canonical total return/IRR은 null이다.",
drivers="depressed public hotel earnings가 아니라 irreplaceable Florida locations와 unencumbered control이 private buyer에게 높은 strategic value를 준 것이 수익경로였다. travel 완전회복을 기다리기 전에 buyer가 normalized economics를 선반영했다. 강한 controlling owner의 매각 의사도 hard gate였다.",
error="9x cash flow와 13.6% yield가 property별 quality·renovation need를 평균화했고, $110m normalized cash의 cycle range를 충분히 보이지 않았다. Huizenga control은 sale을 빠르게 할 수 있지만 minority가 다른 가격을 강제하기 어렵다는 양면성이 있다.", first_signal="Boca 핵심 property의 occupancy·ADR 회복이 market보다 뒤지고 maintenance capex가 normalized FCF의 20% 이상을 추가로 소모하거나 controlling owner가 sale 대신 levered acquisition을 택하면 $20.29 appraisal을 낮춘다.",
waterfall="Property EBITDA에서 maintenance/renovation capex·property/holdco debt·interest·tax와 transaction leakage를 차감한다. tangible book와 resort appraisal은 매각 전 common cash가 아니며 Class A의 control discount를 반영한다.",
metrics=[("Entry/fair value", "$12.85", "$20.29", "$24 cash agreement", "강한 성공"),("Tangible book", "$11.67/share", "public floor", "$24 buyer value", "방향 성공"),("Normalized cash", "$110m", "9x private value", "transaction이 상단 지지", "성공 방향"),("Maintenance FCF", "$95m", "13.6% EV yield", "exact cohort 없음", "미검증"),("Control", "Huizenga ~98% vote", "sale route", "merger vote 확보", "성공")],
timeline=[("2001-09", "travel shock", "depressed earnings"),("2002-04-07", "VIC Long", "$12.85"),("2002~04", "Florida travel 회복", "normalized cash path"),("2004-10-20", "Blackstone agreement", "$24 cash"),("2004-11-15", "definitive proxy", "terms·assets 공개"),("2004-12-08", "stockholder vote 예정", "control gate"),("2004말", "takeout process", "terminal cash event")],
claimdata=[("trophy scarcity", "South Florida resort locations가 book보다 가치 있다.", "waterfront·club·marina assets", "replacement·entitlement가 어렵다.", "comparable sales/book 이하이면 반증.", "$24 strategic bid", "강한 성공", "scarcity는 third-party bid로 검증한다."),("normalized $110m", "depressed travel 뒤 cash flow가 회복한다.", "portfolio history", "2001 shock가 영구수요 훼손이 아니다.", "2년 normalized EBITDA 미회복이면 반증.", "buyer가 $20.29 상단 지불", "성공 방향", "cycle recovery와 asset sale을 별도 경로로 둔다."),("unencumbered control", "management-contract 제약이 적어 buyer universe가 넓다.", "property structure", "change-of-control 비용이 제한적이다.", "brand/management termination fee가 크면 반증.", "Blackstone affiliate가 whole company 계약", "성공", "호텔 SOTP는 brand encumbrance를 확인한다."),("balance-sheet floor", "$11.67 book와 낮은 debt가 하방이다.", "tangible book·$184.4m debt", "deferred capex가 작다.", "repair capex로 book가 소진되면 반증.", "$24 cash event", "기간 성공", "book floor는 capex·debt 후 net이다."),("sale catalyst", "strategic/PE buyer가 몇 년 안에 control premium을 낸다.", "SQL catalyst·owner actions", "controller가 매각을 선택한다.", "levered expansion 우선이면 반증.", "2004 Blackstone 계약", "강한 성공", "sale thesis에는 control owner의 행동을 둔다."),("entity resolution", "2002 RST는 Rosetta Stone이 아니라 Boca Resorts다.", "date·VIC link·SEC ticker", "security mapping이 정확하다.", "CIK/business 불일치면 반증.", "CIK 1020905 Boca로 확정", "성공", "ticker는 법인이 아니며 날짜별로 resolve한다.")]),

I(id="22ef2bf1-6d9c-4048-bbed-13725baee559", date="2010-01-04", author="rascal997", ticker="RST", entity="Rosetta Stone Inc.", group="rst", raw_short=True, direction="Short", entry="약 $18", horizon="12개월", filename="analysis/ideas/2010/2010-01-04_RST_short.md", link=None, desc=0, cat=105, title="unit saturation·CAC inflation·AOV illusion Short", verdict="profitability 붕괴·$12 downside 방향 강한 성공, exact return은 null", score=9.4, process=9.6,
summary="약 $18에서 $12를 목표로 한 raw·실제 Short다. headline revenue는 bundle과 AOV 상승으로 버티지만 customer-unit growth가 둔화하고 sales & marketing per customer가 4Q08/1Q09 20%+, 2Q09 35%, 3Q09 25% YoY 증가해 US consumer penetration과 CAC가 악화된다고 봤다.",
valuation="2010E EPS 약 $0.90의 estimate cut과 growth multiple compression을 함께 봤다. Short payoff는 revenue collapse가 아니라 `unit growth↓+CAC/unit↑+bundle AOV↑→contribution margin↓→EPS miss`다. $12는 낮아진 earnings와 multiple의 결합이며 international/institutional upside와 squeeze를 위험으로 둬야 한다.",
actual="공식 2012 10-K상 revenue는 2010 $258.9m, 2011 $268.4m, 2012 $273.2m으로 완전히 붕괴하지 않았다. 그러나 operating income은 2010 +$12.9m에서 2011 -$28.4m, 2012 -$6.0m이 되었고 net income은 2010 +$13.3m에서 2011 -$20.0m, 2012 -$35.8m으로 악화했다. 2011 Q4 trading range 저점은 $6.55였다.",
price="첨부 SQL에는 catalyst 105자만 있고 description·performance는 없다. $18·$12·Q4 low $6.55는 thesis/filing anchors이지 posting-to-horizon total return이 아니다. borrow cost와 exact dates가 없어 return/IRR은 null이다.",
drivers="Short alpha는 brand·TAM 반박이 아니라 CAC라는 leading unit metric이 earnings보다 먼저 악화된 데서 나왔다. bundle/AOV가 volume weakness를 가리므로 매출은 늦게 둔화했고 profitability가 먼저 무너졌다. estimate cut과 multiple compression이 같은 방향으로 작동했다.",
error="channel checks와 per-unit marketing cost의 정의·cohort comparability를 더 엄격히 설명할 수 있었다. International·institutional expansion과 high short interest squeeze는 실제 position sizing에 반영해야 했고 $12 cover rule을 사전에 명확히 둘 필요가 있었다.", first_signal="반대로 customer-unit growth가 재가속하고 S&M per new unit가 2개 분기 연속 하락하며 contribution margin이 개선되면 saturation Short를 cover한다. $12 도달 또는 positive cohort evidence 중 먼저 오는 것을 exit gate로 둔다.",
waterfall="Short payoff는 revenue가 아니라 customer unit×AOV에서 CAC·fulfillment/content·R&D·G&A를 차감한 cohort contribution과 cash burn으로 검증한다. gross margin·brand·cash는 CAC가 악화하면 equity floor가 아니다.",
metrics=[("Entry/target", "$18", "$12", "2011 Q4 low $6.55", "방향 성공"),("S&M/customer", "+20~35% YoY", "margin pressure", "2011 operating loss", "성공"),("Revenue", "$258.9m 2010", "둔화", "$268.4m/$273.2m", "collapse 아님"),("Operating income", "+$12.9m 2010", "estimate cut", "-$28.4m 2011", "강한 성공"),("Net income", "+$13.3m 2010", "악화", "-$20m/-$35.8m", "성공")],
timeline=[("2009", "IPO·growth narrative", "high expectations"),("2009-Q1~Q3", "CAC/unit +20~35%", "leading break"),("2010-01-04", "VIC Short", "$18→$12"),("2010", "operating income +$12.9m", "last profit year"),("2011", "operating loss -$28.4m", "core validation"),("2011-Q4", "range low $6.55", "target direction"),("2012", "net loss -$35.8m", "profitability failure 지속")],
claimdata=[("US saturation", "customer unit growth가 포화에 접근한다.", "channel/unit slowdown", "international이 즉시 상쇄하지 않는다.", "unit growth 재가속이면 반증.", "core profitability 악화", "성공 방향", "포화는 unit와 CAC로 측정한다."),("CAC inflation", "S&M/customer +20~35%가 margin을 압박한다.", "분기 per-unit data", "spend가 durable retention을 만들지 않는다.", "CAC payback 개선이면 반증.", "2011 -$28.4m operating loss", "강한 성공", "consumer growth는 incremental CAC가 선행한다."),("AOV illusion", "bundle 가격상승이 unit 약화를 가린다.", "revenue=unit×AOV", "bundle attach가 true demand가 아니다.", "unit·retention 동시개선 시 반증.", "매출은 유지·profit은 붕괴", "성공", "price/mix와 volume을 분리한다."),("estimate cuts", "2010E EPS $0.90가 하향된다.", "CAC·unit trend", "비용을 빨리 줄이지 못한다.", "positive operating leverage면 반증.", "2011/12 losses", "성공", "leading unit metric을 estimate bridge로 연결한다."),("$12 target", "earnings와 multiple이 함께 낮아진다.", "$18 entry", "short squeeze·M&A가 없다.", "positive cohort signal이면 cover.", "filing range가 target 아래", "방향 성공", "target hit와 exact short return은 다르다."),("Short risk", "brand·international·institutional은 thesis를 뒤집을 수 있다.", "optionality·high SI", "core CAC가 더 큰 변수다.", "international contribution이 US loss 상쇄하면 cover.", "상쇄하지 못함", "risk 관리 성공", "Short에는 명시적 cover 조건을 둔다.")]),

I(id="fa33642b-2bb2-4c3c-9791-3c3869f7234c", date="2011-08-23", author="zach721", ticker="RST", entity="Rosetta Stone Inc.", group="rst", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="2~3년", filename="analysis/ideas/2011/2011-08-23_RST_long.md", link="https://www.valueinvestorsclub.com/idea/Rosetta_Stone/5842388987", desc=0, cat=911, title="0.55x EV/Sales·net cash·SaaS transition Long", verdict="SaaS 매출만 성장·consolidated economics와 $40 실패, exact return은 null", score=3.8, process=6.9,
summary="raw Short와 달리 business value의 절반 이하라며 $40 target을 제시한 Long이다. EV 약 $135m·0.55~0.6x sales, $115m net cash가 market cap의 약 45%였고, 80%+ gross margin·International growth·ReFLEX/TOTALe와 subscription mix 15%→27%가 CD에서 sticky SaaS로 바뀌어 2013 revenue $400~420m·15% EBITDA margin을 만든다고 봤다.",
valuation="2013 revenue $400~420m×15% EBITDA margin은 EBITDA/share $3+를 만들고 10x에 cash를 더해 $40 target이라는 구조다. EV/Sales가 낮아도 S&M 약 50%와 R&D 약 15%를 유지해야 매출이 나면 owner margin은 낮다. cash $115m도 operating loss·product transition·acquisition에 쓰이면 floor가 아니라 runway다.",
actual="subscription/service revenue는 2010 $43m에서 2011 $73m, 2012 $92m으로 늘어 transition 방향은 맞았다. 그러나 operating income은 2011 -$28.4m, 2012 -$6.0m, 2013 revenue는 약 $264.6m으로 $400~420m에 크게 못 미쳤다. net cash·brand·gross margin은 weak CAC/contribution economics를 막지 못했다.",
price="현 SQL에는 catalyst 911자만 있고 description·performance는 없다. $40, EV $135m, $115m cash, 0.55x sales는 prior metadata anchors다. 정확 entry와 보유수익률이 없어 return/IRR은 null이다.",
drivers="실패원인은 SaaS transition 자체가 아니라 subscription revenue 성장과 cohort profitability를 동일시한 것이다. high gross margin 아래 customer acquisition과 product/R&D가 과도했고 International은 localization·channel spend를 필요로 했다. cash는 이 전환을 보조했지만 intrinsic floor가 아니었다.",
error="2010 Short가 제시한 CAC·unit saturation을 충분히 반증하지 않고 low EV/Sales·cash·TAM으로 narrative를 뒤집었다. subscription mix를 retention/payback 없이 quality로 봤고 2013 revenue와 15% margin을 동시에 달성하는 operating bridge가 없었다.", first_signal="subscription revenue가 늘어도 S&M/revenue가 45% 아래로 내려오지 않고 annualized FCF가 음수이거나 consumer unit가 감소하면 $400m revenue·15% margin·$40 target을 폐기한다.",
metrics=[("EV/Sales", "0.55~0.6x", "rerating", "profitability 악화", "실패"),("Net cash", "$115m/~45% cap", "downside floor", "loss funding runway", "실패"),("Subscription", "$43m 2010", "mix 27%+", "$73m/$92m", "성공"),("2013 revenue", "$400~420mE", "growth", "약 $264.6m", "강한 실패"),("EBITDA/target", "15%/$40", "$3+/share", "consolidated loss path", "실패")],
timeline=[("2010-01", "VIC Short", "CAC warning"),("2010", "service revenue $43m", "transition base"),("2011-08-23", "VIC Long", "$40 target"),("2011", "operating loss -$28.4m", "first break"),("2012", "service revenue $92m", "mix success"),("2012", "net loss -$35.8m", "economics failure"),("2013", "revenue 약 $264.6m", "forecast miss")],
claimdata=[("SaaS transition", "subscription mix 증가가 sticky revenue를 만든다.", "$43m→$73m trajectory", "renewal·CAC payback이 좋다.", "mix↑에도 loss면 반증.", "$92m까지 증가·loss 지속", "매출 성공/경제성 실패", "SaaS label과 unit economics를 분리한다."),("International TAM", "해외 50% growth가 US saturation을 상쇄한다.", "language demand·ReFLEX", "localization CAC가 낮다.", "growth 둔화·loss 확대면 반증.", "consolidated forecast 미달", "실패", "TAM보다 country contribution을 본다."),("0.55x EV/Sales", "80% gross-margin business에 과도하게 싸다.", "EV $135m", "S&M/R&D가 정상화된다.", "contribution margin 음수면 반증.", "operating loss", "실패", "EV/Sales는 below-gross-margin cost를 포함하지 않는다."),("net cash floor", "$115m cash가 downside를 지지한다.", "45% market cap", "burn·M&A가 제한된다.", "cash burn 가속이면 반증.", "runway로 소모", "실패", "cash에는 use-of-cash를 붙인다."),("2013 15% margin", "$400~420m에서 15% EBITDA가 가능하다.", "scale·subscription", "CAC가 revenue보다 느리게 증가한다.", "S&M ratio 미하락이면 반증.", "revenue $264.6m·loss path", "대실패", "두 가정 동시달성의 bridge를 요구한다."),("Long direction", "raw Short가 아니라 $40 Long이다.", "positive target", "same common 기준", "short payoff가 확인되면 반증.", "Long으로 교정", "성공", "metadata flag를 원문 action으로 감사한다.")]),

I(id="e29782f1-5643-46fd-b849-1c2675cc3f0c", date="2013-03-25", author="zach721", ticker="RST", entity="Rosetta Stone Inc.", group="rst", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="12~24개월", filename="analysis/ideas/2013/2013-03-25_RST_long.md", link="https://www.valueinvestorsclub.com/idea/ROSETTA_STONE_INC/4992259309", desc=0, cat=9, title="$7 cash·16% FCF yield·SaaS reset Long", verdict="2013 FCF forecast 강한 실패·Lexia capital allocation은 별도 성공, exact return은 null", score=5.0, process=7.4,
summary="raw Short와 달리 $23~25 target·$12 downside를 제시한 재도전 Long이다. new management, 약 $7/share net cash, 4Q12 cash generation, subscription services $73m→$92m을 근거로 2013 FCF $35m+, 2014 $45m+, 약 16% FCF yield와 bolt-on education acquisitions를 기대했다.",
valuation="핵심은 2013 $35m+ FCF와 2014 $45m+ FCF에 12x EV/FCF와 cash를 더한 $23~25다. 그러나 4Q12 seasonality·deferred revenue·promotion·working capital을 annual run-rate로 취급했다. downside $12도 $7 cash가 burn과 M&A에 쓰이지 않는다는 가정에 종속됐다.",
actual="공식 자료상 FY2012 FCF는 $22.1m이었지만 FY2013 FCF는 -$0.9m, adjusted FCF도 약 $7.1m으로 원문 $35m+에 크게 못 미쳤다. 2014 adjusted EBITDA guidance는 $18~22m이었다. 반면 2013 $22.5m에 인수한 Lexia는 훗날 핵심 교육자산이 됐다. 이 later success는 당시 core FCF forecast 실패와 분리한다.",
price="현재 SQL에는 `See above` catalyst 9자만 있고 description·performance는 없다. $7 cash, $35m/$45m FCF, $12 downside와 $23~25 target은 prior metadata anchors다. exact return/IRR은 null이다.",
drivers="핵심 실패는 seasonal Q4 cash를 annualize하고 deferred-revenue timing을 economic FCF로 본 것이다. management change와 SaaS mix는 cash conversion을 보장하지 않았다. 다만 작은 bolt-on M&A였던 Lexia는 company-level forecast와 독립적으로 높은 장기 value를 만들었다.",
error="2011 thesis의 CAC·contribution 문제를 해결했다는 증거 없이 management conservatism과 한 분기 FCF에 의존했다. 16% FCF yield의 F가 반복 가능한지 검증하지 않았고, cash를 downside와 M&A funding에 동시에 사용했다.", first_signal="Q1/Q2 2013 cumulative FCF가 $10m 미만이고 subscription growth에도 S&M ratio·deferred revenue-adjusted cash가 개선되지 않으면 $35m forecast와 $23~25 target을 즉시 폐기한다.",
metrics=[("Net cash", "$7/share", "downside $12", "M&A·burn에 사용", "floor 실패"),("FY2012 FCF", "$22.1m", "run-rate", "$22.1m", "base"),("FY2013 FCF", "$35m+ E", "16% yield", "-$0.9m", "대실패"),("Adjusted FCF", "증가 기대", "$35m+", "$7.1m", "실패"),("Lexia", "$10~30m bolt-on", "optionality", "$22.5m acquisition", "장기 성공")],
timeline=[("2011-08", "선행 Long 실패", "reset 필요"),("2012-Q4", "strong cash generation", "annualization anchor"),("2013-03-25", "VIC Long", "$23~25"),("2013-07", "Lexia $22.5m 인수", "capital allocation"),("2013-FY", "FCF -$0.9m", "core 반증"),("2014-02", "FY13 결과·guidance", "forecast miss 확인"),("2018~20", "Lexia 성장·sale value", "별도 장기 성공")],
claimdata=[("2013 FCF $35m+", "4Q12 momentum으로 연간 cash가 증가한다.", "$22.1m FY12·Q4 cash", "seasonality·working capital이 반복된다.", "H1 cumulative<$10m이면 반증.", "-$0.9m", "대실패", "seasonal quarter를 annualize하지 않는다."),("2014 FCF $45m+", "SaaS scale로 추가 개선한다.", "subscription mix", "CAC·R&D가 leverage된다.", "FY13 base miss면 제거.", "2014 guide $18~22m EBITDA", "실패", "다음 해 target은 현재 bridge 성공 조건부다."),("management conservative", "new team이 underpromise한다.", "new CFO/CEO·guidance", "operating execution이 개선된다.", "첫 full-year miss면 반증.", "cash forecast 미달", "실패", "management label은 숫자 이력으로 검증한다."),("cash downside", "$7/share cash가 $12를 지지한다.", "net cash", "burn·M&A가 value-creating이다.", "FCF 음수·acquisition이면 반증.", "cash burn과 Lexia purchase", "부분", "cash floor와 reinvestment option을 중복하지 않는다."),("Lexia optionality", "small education deals가 recurring value를 만든다.", "$10~30m plan", "target economics가 좋다.", "retention·growth 미달이면 반증.", "$22.5m Lexia 장기 성공", "강한 별도 성공", "core thesis와 capital-allocation outcome을 분리한다."),("Long direction", "raw Short가 아니라 $23~25 Long이다.", "positive target", "same security", "negative payoff 확인 시 반증.", "Long으로 교정", "성공", "방향 오류를 먼저 고친다.")]),

I(id="6bda7bdb-498c-401d-95d0-b8321df2802b", date="2018-09-08", author="skimmer610", ticker="RST", entity="Rosetta Stone Inc.", group="rst", raw_short=True, direction="Long", entry="원문 가격 미복원", horizon="2~3년", filename="analysis/ideas/2018/2018-09-08_RST_long.md", link=None, desc=0, cat=161, title="Lexia alone covers EV·$22~35 SOTP Long", verdict="Lexia 성장과 $30 cash sale로 강한 성공, exact return은 null", score=9.6, process=9.6,
summary="raw Short와 달리 50~100%+ upside를 제시한 Long이다. 2011/13처럼 Rosetta Stone brand·cash를 사는 대신, 2013 인수한 K-12 literacy SaaS Lexia의 2018 bookings 약 $60m·25%+ growth와 2020 target $100m에 5~8x를 적용하면 $22~35/share로 whole-company EV를 덮고 language businesses는 무료라고 봤다.",
valuation="Lexia 2020 sales/bookings $100m×5~8x에서 corporate cost·tax·net cash·shares를 조정해 $22~35/share를 제시했다. Enterprise & Education language는 약 1.5x revenue, Consumer는 subscription transition optionality로만 둔다. 핵심은 good asset standalone value가 bad/slow assets와 corporate drag를 빼고도 EV를 커버하는지다.",
actual="2019 Literacy revenue는 $62.6m으로 19% 증가했고 consolidated revenue도 5% 늘어 2014 이전 이후 첫 growth year를 기록했다. 2020 Cambium/Veritas는 Rosetta Stone 전체를 $30/share cash, 약 $792m equity value에 인수했고 2020-10-15 거래가 완료됐다. $30은 원문 Lexia-based $22~35 range 안에 있다.",
price="현 SQL에는 catalyst 161자만 있고 description·performance는 없다. $22~35 SOTP와 $30 cash takeout은 valuation/event anchors다. exact posting price·배당·holding period performance가 없어 total return/IRR은 null이다.",
drivers="2018 thesis가 이전 Long보다 강한 이유는 추상적 TAM·brand 대신 distinct asset의 bookings growth, customer validation과 private-market multiple을 쓴 것이다. Lexia가 whole EV를 덮고 company sale이 standalone value를 현금으로 전환했다. language businesses가 악화해도 base가 서는 구조였다.",
error="$100m 2020 target과 5~8x range는 growth·renewal·margin이 유지돼야 하며 corporate tax/standalone sales cost를 더 명시해야 했다. customer interviews도 learning outcome·renewal cohort와 연결해야 하고 sale probability를 target에 전액 넣지 않아야 한다.", first_signal="Lexia bookings growth<15%, net retention<100%, school renewal 약화 또는 2020 target 철회와 함께 corporate cash burn이 지속되면 5~8x를 3~5x로 낮추고 language businesses를 negative value로 stress한다.",
waterfall="Lexia bookings/revenue에서 sales implementation·content/R&D·G&A·standalone public cost와 tax를 빼고, E&E/Consumer의 현금 또는 wind-down cost와 net cash를 더한다. gross SaaS multiple은 common payoff가 아니다.",
metrics=[("Lexia bookings", "$60m 2018", "$100m 2020", "$62.6m revenue 2019", "성공 방향"),("Growth", "25%+ bookings", "15%+ 유지", "Literacy revenue +19%", "성공"),("Lexia multiple", "5~8x", "$22~35/share", "$30 whole-company deal", "강한 성공"),("Consumer CD", "2016 74%→2Q18 3%", "subscription option", "business included in sale", "부분"),("Terminal event", "sale optionality", "2020 target", "$30 cash completion", "강한 성공")],
timeline=[("2013-07", "Lexia $22.5m 인수", "hidden asset seed"),("2016~18", "Consumer CD 74%→3%", "subscription transition"),("2018-09-08", "VIC Long", "$22~35 SOTP"),("2019", "Literacy revenue $62.6m/+19%", "core validation"),("2020-07", "sale process", "hard catalyst"),("2020-08-31", "Cambium $30 agreement", "range realization"),("2020-10-15", "transaction completion", "cash terminal")],
claimdata=[("Lexia quality", "K-12 literacy bookings가 25%+ 성장한다.", "$60m bookings·customer checks", "renewal·outcomes·sales efficiency가 좋다.", "growth<15%·retention<100%면 반증.", "2019 Literacy +19%", "성공", "교육 SaaS는 bookings·renewal·outcome을 본다."),("Lexia covers EV", "Lexia standalone value가 whole-company EV보다 크다.", "5x run-rate bookings", "corporate drag·tax가 제한적이다.", "3x stress value<EV면 반증.", "$30 whole-company bid", "강한 성공", "good asset>EV는 net standalone value로 검증한다."),("$100m 2020 target", "Lexia가 2020 sales $100m에 접근한다.", "25%+ growth", "school budget·sales capacity가 유지된다.", "target 철회면 반증.", "whole company가 target 시점 전 sale", "부분/terminal", "operating target과 sale event를 분리한다."),("language free option", "E&E·Consumer를 낮게 봐도 downside가 제한된다.", "1.5x E&E·Consumer option", "cash burn이 크지 않다.", "negative FCF가 Lexia 가치 잠식하면 반증.", "buyer가 전체 인수", "부분 성공", "free option에도 wind-down cost를 둔다."),("company sale", "asset proof가 strategic sale을 부른다.", "SQL catalyst·portfolio fit", "buyer financing·board execution이 있다.", "process 중단이면 반증.", "Cambium $30 cash close", "강한 성공", "SOTP는 credible buyer가 있을 때 강해진다."),("Long direction", "raw Short가 아니라 50~100%+ Long이다.", "$22~35 target", "same RST common", "negative target 확인 시 반증.", "Long으로 교정", "성공", "ticker·direction을 원문 payoff로 확정한다.")]),
]


def idea_sources(idea):
    raw = m.S(
        "첨부 SQL catalyst / prior curated metadata",
        idea["link"],
        "VIC_IDEAS(4).sql / VIC / repository prior overlay",
        idea["date"],
        f"idea_id·catalyst {idea['cat']} chars·description absent; date·author·raw flag·원문 anchor는 prior overlay 대조",
        "원문/metadata",
    )
    return [raw, *m.SOURCES[idea["group"]]]


def report(idea):
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        text = m.report(idea)
    finally:
        m.idea_sources = old
    generic = (
        "회계이익에서 운전자본·담보·규제자본·maintenance/growth investment·interest·tax를 차감하고, common보다 선순위인 계약·채권자 청구권을 먼저 배치한다. "
        "자산가치와 계약상 수취액은 현금화 날짜·세금·재투자 의무를 반영한다. 기업가치가 맞아도 security와 duration이 틀리면 투자결과는 실패할 수 있다."
    )
    text = text.replace("Batch 046 canonical report.", "Batch 054 canonical report.")
    text = text.replace("### Common equity cash waterfall", "### Security cash waterfall")
    text = text.replace(generic, idea["waterfall"])
    text = text.replace(
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |",
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |\n| 실제 Security | **{idea['security']}** |",
    )
    text = text.replace(
        f"`ATH`를 회사로 보지 말고 {idea['entity']} 법인·exchange·날짜로 고정한다.",
        f"`{idea['ticker']}`를 단일 회사로 보지 말고 {idea['entity']} 법인·날짜·실제 security로 고정한다.",
    )
    text = text.replace(
        "원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.",
        "원문·metadata: **C** — 첨부 SQL에는 catalyst만 있고 Batch 054 description은 0건이다. date·author·raw flag·원문 수치는 prior curated overlay를 별도 provenance로 대조했다.",
    )
    text = text.replace(
        "기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.",
        "기업·사건: **A/B** — SEC·FTC·회사 filing으로 segment 결과·corporate action·terminal event를 검증했다.",
    )
    text = text.replace(
        "가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
        "가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. corporate event·filing price range를 exact return으로 바꾸지 않고 return/IRR을 null로 유지했다.",
    )
    return text


def payload():
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(IDEAS)
    finally:
        m.idea_sources = old
    out["batch"] = 54
    out["title"] = "Office Depot / Boca Resorts / Rosetta Stone — Forecasting, Unit Economics and Asset Proof V9"
    null_keys = (
        "perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y",
        "idea_return_1y", "idea_return_3y", "idea_return_5y",
    )
    for idea, master, post in zip(IDEAS, out["ideas_master"], out["postmortems"]):
        master["security_ko"] = idea["security"]
        master["performance_available"] = 0
        master["contest_winner"] = int(idea["contest"])
        master["auto_tag_status_ko"] = "current SQL catalyst 감사·entity/direction 수동교정·성과 null"
        for key in null_keys:
            master[key] = None
        post["research_direction_ko"] = f"{idea['direction']} / {idea['security']}"
        post["research_status_ko"] = "SQL catalyst·prior metadata·공식 filings 검증; description/performance COPY 부재로 exact return null"
        post["confidence"] = 0.91 if idea["link"] else 0.84
    return out


def make_index():
    rows = []
    for n, idea in enumerate(IDEAS, 1):
        raw = "Short" if idea["raw_short"] else "Long"
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['ticker']} | {idea['entity']} | {raw}→**{idea['direction']}** | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 054 — Office Depot / Boca Resorts / Rosetta Stone — V9 Index", "",
        f"> Research as-of {ASOF}. Batch 053 다음 10건이다. **10 idea = 10 canonical reports**이며 현재 첨부 SQL에 없는 description·성과값을 만들지 않았다.", "",
        "## 0. 배치 결론", "",
        "ODP 5건은 같은 declining retailer에서 `prior-margin forecasting→merger cost-out→services transformation→remaining-assets SOTP→bid 뒤 asset separation`으로 논지의 질이 어떻게 바뀌는지 보여준다. 2002 `RST`는 Rosetta Stone이 아니라 Boca Resorts이며 trophy asset sale로 성공했다. Rosetta Stone 4건은 CAC Short의 성공, cash/EV-Sales Long의 실패, 잘못된 FCF annualization, 그리고 Lexia라는 distinct asset proof의 성공을 비교한다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | Raw ticker | 실제 회사 | raw→연구 방향 | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|---|", *rows, "",
        "## 2. SQL / Entity / Direction Audit", "",
        "첨부 `VIC_IDEAS(4).sql`에는 `catalyst·companies·descriptions` COPY만 있고 `ideas·performance` data COPY는 없다. Batch 054의 catalyst는 10건 모두 확인됐지만 description은 **0건**이다. date·author·raw flag·원문 수치는 prior curated metadata로 낮은 provenance를 명시하고, 실제 결과는 SEC·FTC filings로 검증했다. exact return/IRR은 모두 null이다.", "",
        "raw direction 오류는 8건이다. ODP 5건은 모두 상승 target/payoff의 Long이고, RST 2011·2013·2018도 Long이다. Rosetta Stone 2010만 raw Short=실제 Short다. 2002 ticker RST는 CIK·business·VIC link상 **Boca Resorts, Inc.**이며 Rosetta Stone mapping을 교정했다.", "",
        "## 3. Office Depot — forecasting에서 asset proof로", "",
        "| 시점 | 논지 | 핵심 검증 | 판정 |", "|---|---|---|---|",
        "| 2007-12 | 5% normalized margin | 2008 Retail $354.5m→-$29.2m | 실패 |",
        "| 2014 | OfficeMax cost-out·capacity shrink | synergy $700m+·Staples $11 value | self-help 성공/FTC 실패 |",
        "| 2018 | CompuCom services transformation | $1bn acquisition→최대 $305m sale | 실패 |",
        "| 2019 | B2B SOTP·failed-M&A salvage | $40 proposal·B2B plan·CompuCom sale | 방향 성공 |",
        "| 2021 | $40 bid 뒤 $80 four-leg SOTP | $300m salvage 정확·spin 취소 | 부분 성공 |", "",
        "가장 중요한 진화는 `회사의 미래 margin 예측`에서 `실패해도 남는 자산과 실제 buyer price`로 이동한 것이다. decline company의 강한 thesis는 transformation이 아니라 downside asset proof에서 나왔다.", "",
        "## 4. Boca Resorts — ticker 충돌과 private value", "",
        "2002 RST는 Rosetta Stone이 아니다. Boca Resorts는 약 $12.85에서 tangible book $11.67, normalized cash $110m, $20.29 private value였고 2004 Blackstone affiliate가 $24 cash 계약을 제시했다. trophy location·control owner·unencumbered sale route가 depressed hotel earnings보다 중요했다. 다만 event anchor를 exact total return으로 바꾸지 않았다.", "",
        "## 5. Rosetta Stone — unit economics가 narrative를 이긴다", "",
        "| 시점 | 무엇을 봤나 | 결과 |", "|---|---|---|",
        "| 2010 Short | unit saturation·CAC +20~35%·AOV illusion | profitability collapse 적중 |",
        "| 2011 Long | 0.55x sales·$115m cash·SaaS/TAM | revenue/margin forecast 실패 |",
        "| 2013 Long | 4Q cash annualization·$35m FCF | actual -$0.9m, 실패 |",
        "| 2018 Long | Lexia $60m bookings·good asset>EV | $30 Cambium sale, 성공 |", "",
        "CAC·cohort economics를 본 2010 Short가 brand·cash·EV/Sales를 본 2011 Long보다 강했다. 2018에는 Lexia가 standalone buyer value를 가진 distinct asset이 되어 이전의 추상적 SaaS narrative와 달라졌다.", "",
        "## 6. 공통 투자 교훈", "",
        "1. ticker는 날짜별 entity·CIK로 resolve한다.\n2. 주가 drawdown과 valuation safety margin은 다르다.\n3. declining industry에서는 demand보다 cost/capacity 감소속도를 비교한다.\n4. merger synergy와 antitrust completion probability를 분리한다.\n5. transformation M&A는 revenue mix가 아니라 incremental ROIC로 본다.\n6. failed acquisition은 sunk cost가 아니라 현재 third-party salvage로 평가한다.\n7. EV/Sales·gross margin·cash는 나쁜 CAC를 막는 floor가 아니다.\n8. seasonal Q4 FCF를 annualize하지 않는다.\n9. good asset>EV는 corporate drag·tax·sale probability 후 검증한다.\n10. corporate event와 filing price는 performance row가 아니므로 exact return은 null이다.", "",
        "## 7. 산출물", "",
        "- Payload: `data/curated/batch_054_odp_rst_deep_v7.json`\n- Wrapper: `analysis/batch_054_odp_rst_10.md`\n- Source packet: `data/curated/batch_054_source_packet.json`\n- Builder: `scripts/54_build_batch_054_v9.py`", "",
    ])


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 054 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or len(idea_sources(idea)) < 5:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(idea["filename"]).relative_to("analysis").as_posix() for idea in IDEAS]
    wrapper = "# Batch 054 — Office Depot / Boca Resorts / Rosetta Stone V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit wrapper. [Batch 054 V9 Index](batch_054_v9_index.md).\n"
    (ROOT / "analysis/batch_054_odp_rst_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_054_v9_index.md").write_text(make_index(), encoding="utf-8")
    out = payload()
    (ROOT / "data/curated/batch_054_odp_rst_deep_v7.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {
        "batch": "054", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + prior curated metadata + official filings",
        "record_count": 10, "raw_descriptions_present": 0, "raw_catalysts_verified": 10,
        "current_attachment_performance_rows_found": 0, "legacy_overlay_performance_values_discarded": 0,
        "direction_corrections": 8, "entity_corrections": 1, "security_normalizations": 10,
        "performance_rule": "No performance COPY in current attachment; corporate events are not exact returns",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"],
            "raw_direction": "Short" if i["raw_short"] else "Long", "research_direction": i["direction"], "security": i["security"],
            "description_chars": 0, "catalyst_chars": i["cat"], "performance_available": False,
            "canonical_report": i["filename"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_054_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10,
        "copy_tables_present": ["catalyst", "companies", "descriptions"], "idea_rows_in_attachment": 0,
        "raw_descriptions_present": 0, "raw_descriptions_absent": 10, "raw_catalysts_verified": 10,
        "description_chars_by_idea": {i["id"]: 0 for i in IDEAS},
        "catalyst_chars_by_idea": {i["id"]: i["cat"] for i in IDEAS},
        "performance_copy_present": False, "performance_rows_found": 0, "legacy_overlay_rows_nullified": 0,
        "note": "Current attachment controls. Original descriptions are absent; prior curated metadata is lower provenance. Official filings control actual outcomes; events are not exact returns.",
    }
    (ROOT / "data/curated/batch_054_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(out[key]) for key in ("ideas_master", "postmortems", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
