#!/usr/bin/env python3
"""Build Batch 052 Madison Square Garden / New England Realty V9 artifacts."""
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
    "msg_pre": (
        "2012~2014 The Madison Square Garden Company는 MSG·MSG+ regional sports networks(RSN), Knicks·Rangers 등 팀, "
        "Madison Square Garden·Radio City·Forum 같은 venue를 한 common에 담았다. 현금엔진은 `subscriber×affiliate fee+광고+ticket·suite·sponsorship+event revenue-rights fee-team payroll-show cost-corporate cost-renovation capex-tax`다. "
        "Media가 recurring cash의 대부분을 만들고 sports·venue가 희소자산 가치를 제공했다. 2015 분할 뒤 원 common은 MSG Networks와 sports/entertainment MSG 두 증권이 됐으므로 원 투자단위의 성과는 두 증권과 후속 2020·2023 분배까지 연결해야 한다."
    ),
    "msg_post": (
        "2015년 9월 분할 뒤 새 MSG는 RSN이 빠진 sports+entertainment 회사였다. Sports의 현금은 `ticket+suite+sponsorship+local·league media distributions-team payroll·revenue sharing`, Entertainment는 `advance ticket cash+venue rent·food+production revenue-show·talent·venue opex-growth capex`에서 나온다. "
        "advance sales는 negative working capital을 만들지만 환불·공연취소 때 역전된다. 팀 가치는 희소하지만 control discount와 media-rights 계약을 빼야 하고, venue 가치는 maintenance/growth capex 특히 Sphere를 차감해야 한다. 2020년 1:1 MSGE 분배로 MSGS와 MSGE가 갈라졌고 2023년 Sphere와 전통 live entertainment가 다시 나뉘었다."
    ),
    "nen": (
        "New England Realty Associates(NERA/NEN)는 Greater Boston의 아파트와 일부 상업용 부동산을 보유·운영하는 limited partnership이다. 현금엔진은 `occupied units×rent-property operating cost-recurring capex-property mortgage interest·principal-G&A+NEN 지분만큼의 JV cash`다. "
        "Gross property NAV가 receipt holder 가치가 되려면 자산별 mortgage, unconsolidated JV debt, GP·related-party 비용과 세금을 빼야 한다. NEN은 REIT처럼 대부분의 소득을 즉시 배당할 의무가 없어 인수·개선·buyback에 재투자할 수 있다. 2012년 3-for-1 forward split 전 receipt는 Class A Unit의 1/10, 이후에는 1/30이므로 장기 가격은 분할조정이 필수다."
    ),
})

m.SOURCES.update({
    "msg_pre": [
        m.S("MSG pre-2015 SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1469372&owner=exclude", "SEC / MSG", "2009-2015", "통합 Media·Sports·Entertainment와 renovation·현금·분할 filings"),
        m.S("2015 separation Form 10", "https://investor.msgsports.com/press-releases/news-details/2015/The-Madison-Square-Garden-Company-Announces-Filing-of-Form-10-Registration-Statement-for-Separation-of-Sports-and-Entertainment-Businesses-From-Media-Business/default.aspx", "MSG", "2015-03-30", "Media와 sports/entertainment의 독립 재무·분할경로"),
        m.S("2015 separation completion", "https://investor.msgsports.com/press-releases/news-details/2015/The-Madison-Square-Garden-Company-Becomes-New-Public-Sports-and-Entertainment-Company/default.aspx", "MSG", "2015-10-01", "구 MSG 3주당 신 MSG 1주, MSGN 잔존"),
        m.S("2020 entertainment separation", "https://investor.msgsports.com/press-releases/news-details/2020/Madison-Square-Garden-Sports-Corp-Completes-Spin-Off-of-Entertainment-Businesses/default.aspx", "MSG Sports", "2020-04-20", "MSG 1주당 MSGE 1주와 MSGS 잔존"),
        m.S("MSG Sports corporate overview", "https://investor.msgsports.com/", "MSG Sports", "2026", "Knicks·Rangers와 후속 security의 현재 법인 연속성"),
    ],
    "msg_post": [
        m.S("MSG post-2015 SEC archive", "https://www.sec.gov/edgar/browse/?CIK=1636519&owner=exclude", "SEC / MSG", "2015-2020", "standalone 비용·DTA·Sports·Entertainment·분할 filings"),
        m.S("MSG 2019 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1636519/000163651919000019/tmsgc06302019-10k.htm", "SEC / MSG", "2019-08-23", "2018 sports spin 계획·Sphere·segment와 위험"),
        m.S("2020 entertainment separation", "https://investor.msgsports.com/press-releases/news-details/2020/Madison-Square-Garden-Sports-Corp-Completes-Spin-Off-of-Entertainment-Businesses/default.aspx", "MSG Sports", "2020-04-20", "MSGS와 MSGE의 1:1 분리"),
        m.S("2023 Sphere separation information", "https://investor.msgentertainment.com/Information-on-the-2023-Spin-Off-from-Sphere-Entertainment-Co/", "MSG Entertainment", "2023-04", "Sphere와 전통 live entertainment 후속 분리"),
        m.S("MSG Entertainment overview", "https://investor.msgentertainment.com/overview/default.aspx", "MSG Entertainment", "2026", "Garden·Radio City·Beacon·Chicago Theatre의 현재 포트폴리오"),
    ],
    "nen": [
        m.S("NERA investor relations", "https://www.thehamiltoncompany.com/Investor-Relations.aspx", "New England Realty Associates / Hamilton", "2026", "2,943 apartments·130k sf commercial·1/30 receipt·ownership philosophy·37년 배당"),
        m.S("NERA 2025 Form 10-K — company host", "https://www.thehamiltoncompany.us/nera/nen-20251231x10k.htm", "NERA", "2026-03", "receipt split·portfolio·mortgages·JV·repurchase와 related parties"),
        m.S("NERA 2025 Form 10-K — SEC", "https://www.sec.gov/Archives/edgar/data/746514/000110465926027586/nen-20251231x10k.htm", "SEC / NERA", "2026-03", "감사 재무제표와 2012 3-for-1 receipt split"),
        m.S("Hamilton management", "https://www.thehamiltoncompany.com/About-us/Management", "The Hamilton Company", "2026", "Harold Brown 1925~2019와 Jameson Brown succession·운영조직"),
        m.S("Hamilton operating platform", "https://www.thehamiltoncompany.com/About-us/About-us.aspx", "The Hamilton Company", "2026", "Greater Boston 5,600+ residential units·1.5m sf 관리 플랫폼"),
    ],
})


def C(title, original, evidence, assumption, falsifier, actual, verdict, lesson):
    return m.C(title, original, evidence, assumption, falsifier, actual, verdict, lesson)


def I(**x):
    x["claims"] = [C(*row) for row in x.pop("claimdata")]
    x.setdefault("security", "Class A common stock")
    x.setdefault("waterfall", "영업현금에서 rights·payroll·venue opex·maintenance/growth capex·interest·tax를 차감하고 실제 분배된 successor shares를 더한다. SOTP appraisal은 분배나 매각 전까지 현금이 아니다.")
    x.setdefault("contest", False)
    return x


IDEAS = [
I(id="f09b9d47-cf2a-43d2-b07b-c03cb2a30909", date="2012-12-17", author="sandman898", ticker="MSG", entity="The Madison Square Garden Company (pre-2015)", group="msg_pre", raw_short=False, direction="Long", entry="약 $46", horizon="18개월", filename="analysis/ideas/2012/2012-12-17_MSG_long.md", link=None, desc=13274, cat=83, title="Garden capex cliff·FCF inflection·recap Long", verdict="사업·분할경로 성공, $60/18개월 exact return 미검증", score=8.8, process=9.0,
summary="약 $1bn Garden transformation, NHL lockout, Fuse 손실과 Sandy가 reported cash를 눌렀지만 6개월 안에 대부분 끝나 FY2015 normalized FCF가 드러난다는 Long이다. Media가 cash flow의 90%+를 만들고, renovation 종료 뒤 recap/buyback을 붙여 약 $46에서 $60, 18개월 +30%를 기대했다.",
valuation="FY2015E EBITDA 약 $400m·income $200m에 D&A 대비 낮아질 capex $50m와 non-cash 항목을 조정해 FCF $275m+/$3.50+를 계산했다. $1bn을 5%에 빌려 22m주를 사면 78m→56m주, FCF/share 약 $4.40이라는 bull이다. $60은 약 11x EBITDA 또는 7%대 FCF yield다.",
actual="Garden transformation은 2013년 마무리돼 capex cliff와 suite·sponsorship economics가 드러났다. 2015년 통합 MSG는 Media(MSGN)와 sports/entertainment(MSG)로 분리됐고, 2020에는 MSGS와 MSGE가 다시 1:1로 분리됐다. recap 형태는 원문 가정과 달랐지만 hidden assets를 별도 security로 만드는 더 강한 경로가 실행됐다.",
price="첨부 SQL에 performance table/data가 없다. 약 $46·$60은 원문 anchor이며 2015년 3:1 신 MSG 분배, 잔존 MSGN, 2020년 1:1 MSGE를 합친 adjusted series가 없어 return/IRR은 null이다.",
drivers="확인 가능한 edge는 80% 완료된 renovation과 마지막 단계의 낮은 위험, 8m RSN subs·약 50% margin, contract escalator였다. 수익 메커니즘은 capex 감소→FCF 증가→capital action·분할이었다. NHL lockout 해소는 보조 촉매였다.",
error="$1bn debt-funded buyback을 거의 기계적 accretion으로 봤지만 Dolan control 아래 실제 capital allocation은 분할·growth investment였다. Fuse, rights cost와 corporate overhead를 normalized FCF에 더 보수적으로 넣고 recap을 optional로 낮춰야 했다.", first_signal="2013년 renovation 종료 후 annual capex가 $50m 안팎으로 내려오지 않거나 FY2015 FCF가 $275m에 접근하지 못하고 Media affiliate growth까지 둔화하면 $60 base를 철회한다.",
metrics=[("Entry/target", "약 $46", "$60/+30%", "exact series 없음", "방향 성공·수익 미검증"),("Renovation", "$980m~$1bn·80% 완료", "FY2014 완료", "2013 완료", "성공"),("FY2015 FCF", "$275m+/$3.50+", "capex cliff", "경제성 가시화", "방향 성공"),("Recap", "$1bn debt/22m주", "$4.40 FCF/share", "분할로 대체", "부분"),("Media", "8m subs·~50% margin", "cash anchor", "MSGN 분리", "성공")],
timeline=[("2010-02", "Cablevision에서 MSG 분리", "standalone price discovery"),("2012-12-17", "VIC Long", "약 $46→$60/18개월"),("2013", "Garden transformation 완료", "capex cliff"),("2015-03", "Form 10 제출", "hard catalyst"),("2015-09-30", "신 MSG 3:1 분배", "sports/entitlement 발생"),("2015-10-01", "MSGN·MSG 별도 거래", "SOTP 현실화"),("2020-04-17", "MSGE 1:1 분배", "후속 security tree")],
claimdata=[("renovation capex cliff", "마지막 공사 뒤 capex가 약 90% 감소한다.", "80% 완료·마지막 단계 저위험", "추가 overrun·closure가 없다.", "완료 뒤 capex>$100m가 지속되면 반증.", "transformation 완료와 FCF 가시화", "성공", "완료율·잔여 spend·steady capex를 분리한다."),("RSN cash anchor", "Media가 기업 cash flow의 90%+다.", "8m subs·~50% margin·escalator", "rights cost보다 affiliate growth가 빠르다.", "margin<40%·renewal 정체면 반증.", "2015 MSGN 독립회사로 분리", "성공", "SOTP downside는 반복 cash가 맡아야 한다."),("일회성 악재 해소", "lockout·Sandy·Fuse가 6개월 내 정상화된다.", "사건성 손실", "core 수요가 훼손되지 않는다.", "해소 뒤 earnings miss 지속 시 반증.", "lockout 종료·Fuse 후속 매각", "성공", "일회성과 구조비용을 item별로 추적한다."),("renovated Garden ROI", "suite·sponsor·summer dates가 투자수익을 낸다.", "price hikes·장기 sponsorship", "incremental cash가 $1bn cost를 보상한다.", "venue cash yield가 cost of capital 미달이면 반증.", "arena는 후속 MSGE 핵심자산", "방향 성공", "trophy asset도 증분 ROIC로 본다."),("recapitalization", "완료 뒤 debt·buyback이 tax shield와 accretion을 만든다.", "zero debt·경영진 발언", "5% funding·$1bn capacity가 있다.", "buyback 부재·growth spend 우선이면 반증.", "가정 그대로는 미실행, 분할 실행", "부분", "owner action은 base가 아니라 확률가중 option이다."),("$60 payoff", "$3.50~4.40 FCF/share에 $60이 가능하다.", "11x EBITDA·7% FCF yield", "normalized FCF bridge가 맞다.", "18개월 내 FCF <$3.50이면 반증.", "사업·분할 direction 적중", "방향 성공", "target date와 terminal event를 나눈다.")]),

I(id="b1aaa11a-950a-47ab-9831-10b1c91b8595", date="2014-08-04", author="Azalea", ticker="MSG", entity="The Madison Square Garden Company (pre-2015)", group="msg_pre", raw_short=False, direction="Long", entry="약 $60", horizon="2~3년", filename="analysis/ideas/2014/2014-08-04_MSG_long.md", link="https://www.valueinvestorsclub.com/idea/MADISON_SQUARE_GARDEN_CO/6958821775", desc=28467, cat=1465, title="RSN FCF+teams·air-rights SOTP Long", verdict="강한 사업·분할 성공, exact total return 미검증", score=9.5, process=9.5, contest=True,
summary="spin 이후 178% 올랐어도 intrinsic value보다 약 30% 싸다고 본 contest winner다. renovation capex가 연 $316m에서 $50m 이하로 내려가 FY2015 FCF $300m, 2~3년 $400m에 접근하고, RSN 할인값만으로 시가총액을 설명한 뒤 teams·venue·air rights 약 $27/share를 공짜로 얻는 구조다.",
valuation="MSG/MSG+ 8m subs에 $300/$275 per-sub를 적용해 RSN $4.6bn, 약 13x EBITDA를 산출했다. Knicks·Rangers $750m/$9.59, Entertainment $279m/$3.57, real estate·air rights $850m/$10.87, 기타 $99m/$1.26, cash·Fuse proceeds $246m/$3.15, corporate cost -$86m/-$1.10로 other assets 약 $27/share다.",
actual="2014년 Fuse를 $226m에 매각했고 renovation 종료 뒤 cash generation이 선명해졌다. 2015년 9월 구 MSG 3주당 sports/entertainment 신 MSG 1주를 분배하고 구 회사는 MSG Networks로 남아 원문의 Media와 other-assets bucket을 실제 증권으로 분리했다. 2020·2023 추가분할도 trophy assets의 독립가격 경로를 확대했다.",
price="현재 첨부 SQL에는 performance row가 없다. 약 $60 entry와 $27/share hidden value는 T0 anchor이고 2015 3:1·2020 1:1·2023 분배를 이어야 하므로 exact return/IRR은 null이다.",
drivers="$316m→$50m capex cliff, 약 40% subscriber-base affiliate 재계약, 51.6% Media margin, Fuse 매각과 깨끗한 balance sheet가 현금가치를 만들었다. 2015 분할이 valuation bucket을 securities로 전환했다.",
error="RSN subscriber attrition·rights inflation과 Dolan의 growth capex를 충분히 stress하지 않았다. $900m air-right 잠재가치는 rezoning·transfer·세금·time discount 전 gross option이고, Phil Jackson·going-private는 핵심이 아니었다.", first_signal="FY2015 FCF<$250m, affiliate repricing uplift<10%, Media margin<45% 또는 순현금이 buyback보다 저ROIC growth deal로 빠지면 $27/share upside를 haircut한다.",
metrics=[("FCF", "FY15 $300m/~7%", "2~3년 $400m/~9%", "cash profile 개선", "성공"),("Capex", "2년 평균 $316m", "$50m 이하", "renovation 종료", "성공"),("Media margin", "35.3%→51.6%", "재계약 추가", "MSGN 분리", "성공"),("RSN value", "$4.6bn/13x", "시총 anchor", "별도 security", "성공"),("Other assets", "$27/share", "45% upside", "분할로 표면화", "강한 성공")],
timeline=[("2010", "Cablevision spin", "초기 standalone"),("2014-07", "Fuse $226m 매각", "손실·현금 개선"),("2014-08-04", "VIC Long", "약 $60·30% discount"),("2015-03", "Form 10", "분할 공식화"),("2015-09-30", "신 MSG 3:1 분배", "SOTP crystallization"),("2015-10-01", "MSGN·MSG 별도 거래", "Media/other 분리"),("2020-04", "MSGS·MSGE 1:1", "teams/venue 재분리"),("2023-04", "Sphere·MSGE 분리", "growth capex 분리")],
claimdata=[("FCF acceleration", "renovation 종료로 FY15 $300m, 이후 $400m다.", "$316m capex→$50m 이하", "contract revenue·margin이 유지된다.", "FY15 FCF<$250m이면 반증.", "capex cliff와 현금가시성", "성공", "capex cycle은 EBITDA와 따로 모델링한다."),("affiliate repricing", "40% subs 계약이 10~15% 높은 rate로 갱신된다.", "Cablevision/TWC 선행계약", "consolidation이 pricing을 꺾지 않는다.", "renewal uplift<5%면 반증.", "RSN 가치가 독립화", "방향 성공", "rate·subs·rights cost를 동시에 본다."),("sports scarcity", "teams는 media rights 없이도 $750m 이상이다.", "Forbes·transactions", "control discount 후도 가치가 남는다.", "team sale comps가 Forbes 이하이면 반증.", "2020 MSGS로 독립", "성공", "trophy value에서 rights·debt·control을 뺀다."),("air-right option", "1m sf rights가 $250m+다.", "Penn Station·$250/sf", "transfer·rezoning이 가능하다.", "법적 사용·transfer 불가면 반증.", "옵션은 존속, 즉시 현금화는 없음", "부분", "hidden real estate는 legal gate·duration을 붙인다."),("Dolan capital action", "cash·FCF가 환원 또는 분할로 간다.", "$250m pro-forma cash·zero debt", "저ROIC 투자가 제한된다.", "대형 growth spend 우선이면 반증.", "2015·2020 분할, 성장투자도 병존", "부분 성공", "owner의 실제 행동 이력을 확률로 쓴다."),("SOTP unlock", "RSN을 사고 나머지 $27/share를 얻는다.", "bucket별 appraisal", "분리비·세금이 제한적이다.", "분할 취소·net value<$60이면 반증.", "2015 두 증권으로 분리", "강한 성공", "최강 SOTP 촉매는 실제 separate security다.")]),

I(id="4708ee21-4e17-4f34-9874-adcb9f4f2512", date="2016-07-20", author="RogerDorn24", ticker="MSG", entity="The Madison Square Garden Company (post-2015)", group="msg_post", raw_short=False, direction="Long", entry="약 $179", horizon="3~12개월", filename="analysis/ideas/2016/2016-07-20_MSG_long.md", link=None, desc=22381, cat=79, title="post-spin accounting normalization·$209 Long", verdict="사업 정상화·후속분할 성공 방향, exact return 미검증", score=8.6, process=9.0,
summary="2015 spin 뒤 Media가 빠진 새 MSG의 historical carve-out은 FY2014 operating loss -$114m를 보였지만 waiver·termination, reserve, accelerated depreciation와 transition SG&A를 조정하면 약 -$34m였다. 독립 disclosure가 쌓이면 ongoing value 약 $209, 당시 약 $179 대비 17%와 최소 20% rerating이 가능하다는 Long이다.",
valuation="Sports 2016 revenue에 5x를 적용해 $3.6bn, Entertainment는 normalized EPV $325m 또는 10x EBITDA=$300m로 평가했다. Cash $1.4bn, DTA $160m를 더하고 tax-effected corporate cost $455m를 빼 ongoing equity 약 $209/share를 얻었다. PMV $7bn은 cross-check일 뿐 base가 아니다.",
actual="standalone history가 쌓이며 FY2014 carve-out loss의 일회성·현금시점 차이는 일부 해소됐다. 2018 board가 sports separation 검토를 승인했고 2020년 MSGS와 MSGE를 1:1로 분리했다. 반면 Las Vegas Sphere는 단순 upside가 아니라 대규모 capex·duration risk가 되었고 2023년 다시 traditional entertainment와 분리됐다.",
price="첨부 SQL에는 performance가 없다. 약 $179·$209·최소 20%는 원문 숫자이며 2020 1:1 MSGE와 2023 후속분배를 합치지 못해 exact return은 null이다.",
drivers="알파는 trophy appraisal보다 carve-out accounting 재구성이었다. $54.2m termination cost를 cash timing으로, $30m luxury-tax reserve와 $13m transition cost를 반복성으로 분해했고, FY2015 segment operating income $93m·FY2016 9M $124m가 core 개선을 보였다.",
error="one-time add-back을 과도하게 하면 해고·실패한 productions 같은 반복적 비반복 비용을 지울 수 있다. DTA $160m를 할인하지 않고 100% 더했고, $1.4bn cash의 Sphere·M&A 사용 가능성과 $70m corporate-cost 정상화 불확실성을 작게 봤다.", first_signal="10-K에서 unallocated expense가 $70m를 크게 상회한 채 반복되고, entertainment direct cost가 mid-70%로 내려오지 않거나 cash가 repurchase 대신 저ROIC growth capex로 이동하면 $209를 낮춘다.",
metrics=[("FY2014 op loss", "reported -$114m", "adjusted -$34m", "일회성 혼재 확인", "방향 성공"),("Termination", "$54.2m", "economic cash ~$18m", "lumpy 지속", "부분"),("DTA", "$160m", "$4~6/share reversal", "core보다 부차적", "부분"),("Operating value", "$3.9bn", "$209/share", "분할경로 진전", "방향 성공"),("Cash/buyback", "$1.4bn/$500m earmarked", "per-share accretion", "growth capex 병존", "혼합")],
timeline=[("2015-09-30", "신 MSG 3:1 분배", "분석대상 탄생"),("2016-07-20", "VIC Long", "약 $179→$209"),("2018-06-27", "sports spin 검토 승인", "catalyst 출현"),("2019-11", "분할구조 변경", "entertainment를 분배"),("2020-04-17", "MSGE 1:1 분배", "MSGS 잔존"),("2020", "COVID live-event 중단", "entertainment tail"),("2023-04", "Sphere·전통 MSGE 분리", "growth capex risk 분리")],
claimdata=[("carve-out loss 과대", "FY14 -$114m는 경제손실을 과대표시한다.", "$80m add-back bridge", "add-back이 현금·비반복이다.", "3년 반복되면 반증.", "standalone margin 가시화", "성공 방향", "one-time은 반복빈도·cash timing으로 검증한다."),("sports earning power", "teams는 FY15 $75m op income을 냈다.", "sellout·rights tailwind", "payroll이 revenue를 잠식하지 않는다.", "3년 segment loss면 반증.", "MSGS 독립가치 유지", "성공", "경기성적보다 계약수익과 payroll을 본다."),("entertainment leverage", "advance sales·venue network가 margin을 높인다.", "negative working capital·mid/high single digit margin", "실패 show cost가 정상화된다.", "direct cost>85% 지속 시 반증.", "COVID 전 개선, 이후 충격", "부분 성공", "advance cash는 refund liability와 함께 본다."),("DTA recognition", "$160m DTA가 $4~6/share를 만든다.", "valuation allowance", "taxable income이 충분하다.", "profit 미달·세율하락이면 반증.", "부차적 accounting unlock", "부분", "DTA는 사용시점까지 할인한다."),("cash·asset value", "$1.4bn cash와 $7bn PMV가 downside다.", "zero debt·scarce assets", "cash가 보존·환원된다.", "저ROIC capex면 반증.", "Sphere capex로 leakage risk 현실화", "혼합", "cash에는 use-of-cash discount를 붙인다."),("$209/20%", "독립 disclosure로 최소 20% 오른다.", "SOTP·EPV triangulation", "3~12개월 내 clarity가 온다.", "10-K 뒤 gap 지속 시 반증.", "후속분할까지 방향 적중", "방향 성공", "가격촉매와 장기 corporate action을 나눈다.")]),

I(id="c47641e6-ec3d-4ceb-b2b8-56290e6660f2", date="2018-11-20", author="tyler939", ticker="MSG", entity="The Madison Square Garden Company (post-2015)", group="msg_post", raw_short=False, direction="Long", entry="high-$260s~low-$270s", horizon="2020년 분할까지", filename="analysis/ideas/2018/2018-11-20_MSG_long.md", link=None, desc=8466, cat=123, title="announced sports spin·$373 SOTP Long", verdict="분할 성공, entertainment payoff·timing 혼합, exact return 미검증", score=8.4, process=8.8,
summary="2018년 6월 sports spin 검토 발표 후 $327까지 23% 오른 주가가 high-$260s로 되돌아오자 두 번째 기회로 봤다. 다음 Forbes 값에 15% 성장, 거래 premium 25%, standalone discount 20%를 적용한 Sports $240/share와 Entertainment $133를 합쳐 $373, 35%+ upside를 제시했다.",
valuation="Sports는 Knicks $3.6bn·Rangers $1.5bn의 Forbes 값에 15% mark-up과 25% transaction premium, 기타 teams $30m, 20% public NAV discount, cash $200m를 반영해 $240/share다. Entertainment는 Garden $1.1bn, air rights $500m, Sphere $700m cost, Forum·Radio City 등 $300m, TAO/Boston $200m, cash $500m-debt/liability $150m로 $133/share다.",
actual="2019년 구조가 바뀌어 entertainment를 분배하고 sports가 잔존하는 방식이 됐고, 2020-04-17 MSG 1주당 MSGE 1주가 분배됐다. 분할 claim은 성공했다. 그러나 COVID가 live events를 중단시켰고 Sphere는 $700m cost option이 아니라 훨씬 큰 capital commitment가 되어 2023년 Sphere와 traditional MSGE가 다시 분리됐다.",
price="첨부 SQL에 performance가 없다. $327 peak, high-$260s entry range와 $373 target은 원문 anchor이나 MSGS+MSGE, 2023 successor를 연결한 total-return series가 없어 exact return은 null이다.",
drivers="분할 announcement라는 hard catalyst, New York teams의 scarcity와 national rights economics가 Sports 가치를 지지했다. 반대로 Entertainment의 payoff는 live-event shutdown과 Sphere capex라는 원문 밖 path가 지배했다.",
error="Sports의 15% Forbes 상향과 25% control premium을 public minority value에 동시에 쌓아 double counting 위험이 있었다. Sphere를 2019까지의 $700m cost로만 더하고 completion cost·execution tail을 option liability로 stress하지 않았다.", first_signal="spin 일정이 2020을 넘거나 Entertainment net cash가 Sphere spend로 $350m 이상 감소하고 project cost가 $700m를 크게 넘으면 $133 piece를 즉시 재산정한다.",
metrics=[("Entry/target", "$260s~270s", "$373/35%+", "exact series 없음", "사건 성공·수익 미검증"),("Sports", "$240/share", "scarcity unlock", "MSGS 독립", "성공 방향"),("Entertainment", "$133/share", "venue+Sphere", "COVID·capex 충격", "혼합"),("Sphere", "$700m cost", "cost value", "대규모 초과·duration", "실패"),("Distribution", "possible spin", "2020", "2020-04 1:1", "성공")],
timeline=[("2018-06-27", "sports spin 검토 승인", "주가 +23%"),("2018-10", "Form 10 제출", "실행 진전"),("2018-11-20", "VIC Long", "$373 SOTP"),("2019-11", "구조 변경", "entertainment 분배 방식"),("2020-04-17", "MSGE 1:1 분배", "hard catalyst 성공"),("2020-04-20", "MSGS·MSGE 거래", "separate prices"),("2020", "COVID shutdown", "Entertainment downside"),("2023-04", "Sphere·MSG Entertainment 분리", "capex/venue 재분리")],
claimdata=[("sports separation", "Knicks·Rangers가 2020까지 분리된다.", "board 승인·Form 10", "tax·league approvals 통과", "2020 무분할이면 반증.", "2020 1:1 분리", "성공", "announced spin도 구조·교환비율을 추적한다."),("team scarcity premium", "Forbes보다 25% 높은 거래가치다.", "NBA/NHL 24건 평균 premium", "control comp가 minority에 전이된다.", "거래 premium<10%면 반증.", "MSGS 독립가치 유지", "방향 성공", "control premium과 public discount를 섞지 않는다."),("sports betting", "합법화가 sponsorship·data를 monetization한다.", "2018 대법원 판결·DraftKings", "team economics에 직접 귀속된다.", "NY 지연·league가 가치 흡수하면 반증.", "tailwind이나 즉시 monetization 제한", "부분", "산업 TAM보다 security 귀속을 본다."),("Garden·air rights", "arena $1.1bn+rights $500m다.", "1.4m sf·$360/sf", "이전·개발 legal gate 가능", "rights 비이전이면 반증.", "venue는 MSGE에 귀속, 권리는 장기 option", "부분 성공", "gross option에 duration·세금을 붙인다."),("Sphere cost value", "$700m spend를 그대로 가치로 더한다.", "당시 capex projection", "cost≈NPV다.", "budget 초과·ROIC 미달이면 반증.", "cost·duration 크게 확대", "실패", "growth capex는 asset이 아니라 미완성 claim이다."),("$373 payoff", "$240+$133로 35%+다.", "two-piece SOTP", "분할 뒤 discounts가 좁혀진다.", "합산 net value<$300이면 반증.", "분할 적중·경로 혼합", "부분 성공", "catalyst success와 combined return을 분리한다.")]),

I(id="ae00174e-1333-4bee-b573-ef147bfa24db", date="2001-12-28", author="mal228", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="$29.50 (pre-split receipt)", horizon="3~5년", filename="analysis/ideas/2001/2001-12-28_NEN_long.md", link="https://www.valueinvestorsclub.com/idea/New_England_Realty/7664756422", desc=0, cat=67, security="Depositary Receipt = 1/10 Class A Unit (당시)", title="13.4% cap·5.8x FCF owner-operator Long", verdict="사업·가치 방향 강한 성공, exact return 미검증", score=9.0, process=8.5,
summary="첨부 SQL에는 catalyst만 있고 description은 없다. 선행 canonical에 보존된 T0 수치는 $29.50, 2000 FCF $8.9m/$5.10 per receipt, 5.8x FCF, NOI $15.4m와 13.4% implied cap, 99% occupancy다. 높은 current asset yield와 Brown의 acquisition·renovation 역량을 함께 산 Long이다.",
valuation="`EV/NOI 7.5x=13.4% cap`이 핵심 안전마진이다. 1996~2000 NOI CAGR 15.9%, FCF CAGR 23.8%를 외삽하기보다 no-growth에서도 $5.10 FCF/$29.50=17.3% cash-earning yield가 debt·maintenance capex 후 유지되는지 봐야 한다. 당시 receipt는 Class A Unit의 1/10이다.",
actual="NERA는 독립 LP로 생존해 현재 2,943 apartments와 약 130k sf commercial을 보유하고 37년 연속·증가 배당을 공식 표기한다. Hamilton 운영플랫폼도 5,600+ residential units로 확대됐다. 2012 receipt는 3-for-1 split돼 1/30 Unit이 되었고 Harold Brown 사후 Jameson Brown 세대로 승계됐다.",
price="현 첨부 SQL에는 performance data가 없고 description도 없다. 선행 canonical의 $29.50과 2005 후속 가격 약 $80은 방향 참고일 뿐, 분배금·2012 split을 검증한 시계열이 없어 exact return/IRR은 null이다.",
drivers="13%대 absolute cap rate, 99% occupancy, 낮은 acquisition basis와 내부 운영·공사 capability가 시간을 통해 NAV를 키웠다. illiquidity discount가 닫히지 않아도 높은 asset yield와 재투자가 intrinsic value를 늘리는 구조였다.",
error="23.8% FCF CAGR은 작은 base·acquisition·leverage가 섞였는데 지속가능 organic growth처럼 읽힐 수 있다. maintenance capex, GP/related-party fee, debt maturity와 receipt liquidity가 원문 요약에서 충분히 분리되지 않았다.", first_signal="occupancy<95%, same-store NOI 감소, recurring capex 후 FCF/share <$4 또는 acquisition cap rate가 mortgage cost 아래로 내려가면 13.4% 안전마진이 소멸하는 것으로 본다.",
waterfall="Gross rent에서 vacancy·property opex·recurring capex·property mortgage service·G&A를 빼고 NEN 지분의 JV cash만 더한다. LP distribution·buyback 이후 receipt 1/10 claim을 계산한다.",
metrics=[("Entry/FCF", "$29.50/$5.10", "5.8x", "장기 운영 지속", "방향 성공"),("NOI", "$15.4m", "성장 지속", "portfolio 확대", "성공"),("Implied cap", "13.4%", "discount 축소", "후속 낮은 cap regime", "강한 성공"),("Occupancy", "약 99%", "cash 방어", "주거 portfolio 지속", "성공"),("Growth", "NOI 15.9%/FCF 23.8% CAGR", "재투자", "장기 플랫폼 확대", "방향 성공")],
timeline=[("1996~2000", "NOI·FCF 고성장", "T0 track record"),("2001-12-28", "VIC Long", "$29.50·13.4% cap"),("2002", "AMEX 이전·후속 Long", "liquidity/recognition"),("2005", "후속 VIC 약 $80 anchor", "방향 확인"),("2007", "repurchase program 시작", "per-share allocation"),("2012-01-03", "receipt 3-for-1 split", "1/10→1/30"),("2019", "Harold Brown 사망", "succession test"),("2026", "2,943 apartments·37년 배당", "사업 지속")],
claimdata=[("13.4% cap", "Boston apartments를 13%+ cap에 산다.", "NOI $15.4m·EV/NOI 7.5x", "NOI와 debt가 안정적이다.", "cap spread<200bp·NOI 하락이면 반증.", "장기 자산가치·사업 지속", "강한 성공", "부동산은 P/E보다 entry cap spread를 먼저 본다."),("5.8x FCF", "$5.10 FCF에 $29.50은 과도하게 싸다.", "2000 FCF $8.9m", "maintenance capex가 충분히 반영됐다.", "recurring capex 후 FCF<$4면 반증.", "현금엔진 지속", "성공 방향", "AFFO 정의와 capex를 고정한다."),("99% occupancy", "Boston demand가 downside를 지지한다.", "2001 occupancy 약 99%", "student·local 수요가 유지된다.", "occupancy<95%면 반증.", "주거운영 지속", "성공", "occupancy와 rent를 함께 본다."),("Brown reinvestment", "저평가 매입·개선이 NAV를 compound한다.", "1996~2000 NOI/FCF CAGR", "acquisition yield>funding cost다.", "저수익 acquisition이면 반증.", "platform 확대·buyback", "성공", "operator quality는 거래별 spread로 검증한다."),("낮은 leverage", "부채가 high cap asset을 훼손하지 않는다.", "선행 canonical balance-sheet", "maturity가 분산된다.", "refi DSCR<1.5x면 반증.", "장기 생존", "성공", "property debt를 만기별로 본다."),("operating catalyst", "강한 실적이 가격을 움직인다.", "SQL catalyst", "hard catalyst 없이 가치가 성장한다.", "2년 NOI/share 정체면 반증.", "장기 compound", "성공 방향", "no-event thesis는 per-share 성장률이 catalyst다.")]),

I(id="57c53563-8f25-4dd8-a2c8-eda06b38ef77", date="2002-12-28", author="mal228", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="$40 (pre-split receipt)", horizon="3~5년", filename="analysis/ideas/2002/2002-12-28_NEN_long.md", link=None, desc=1803, cat=121, security="Depositary Receipt = 1/10 Class A Unit (당시)", title="12.5~13% cap·6.6x AFFO Long", verdict="사업·private-value 방향 강한 성공, exact return 미검증", score=9.0, process=8.8,
summary="$40에서 trailing AFFO 6.6x, annualized Q3 7.2x, implied cap 12.5~13%로 apartment REIT 약 8%와 큰 격차였다. 2,211 units·vacancy 3.2%, net debt가 real-estate value의 약 1/3이고 $2.56 distribution/6.4% yield여서 Boston rent softness에도 private value $80~85를 제시했다.",
valuation="Private market $80~85는 8% 안팎 cap과 peer AFFO multiple을 적용한 약 2배 NAV다. 안전한 base는 sale이 아니라 $2.56 cash distribution과 12.5~13% property yield가 유지되는 경우다. sale은 Harold Brown retirement에 달린 낮은 확률 option으로 분리한다.",
actual="NERA는 매각되지 않고 독립으로 장기 compound했다. 현재 공식 IR 기준 2,943 apartments와 37년 연속·증가 dividend를 기록한다. 2012 receipt split과 세대승계 뒤에도 운영은 지속됐다. private-value gap의 정확한 가격수익은 현 첨부자료만으로 계산할 수 없다.",
price="현 SQL에는 performance가 없다. $40·$80~85와 6.4% yield만 보존하며 배당·split-adjusted series가 없어 exact return은 null이다.",
drivers="12%+ cap과 6.4% current distribution이 timing 의존도를 낮췄고, 3.2% vacancy·1/3 net-debt ratio가 rent softness를 흡수했다. 매각 없이도 local platform의 재투자와 rent recovery가 가치를 키웠다.",
error="private $80~85가 어떤 NOI·cap·transaction cost를 썼는지 bridge가 짧았다. 42% student rent exposure, AMEX liquidity, GP control과 distribution tax를 더 크게 haircut해야 했다.", first_signal="vacancy>6%, AFFO/share 두 해 연속 감소, distribution coverage<1x 또는 debt/property value>50%가 되면 $80~85 sale value보다 income survival을 우선한다.",
waterfall="Rent에서 3.2% vacancy·property expense·recurring capex·mortgage service와 GP 비용을 빼고 receipt 1/10에 귀속되는 AFFO·$2.56 distribution을 계산한다.",
metrics=[("Entry/AFFO", "$40", "6.6x trailing", "사업 지속", "방향 성공"),("Implied cap", "12.5~13%", "private 8%", "gap 축소 방향", "성공"),("Private value", "$80~85", "약 2x", "exact price 미검증", "방향 성공"),("Distribution", "$2.56", "6.4% yield", "장기 배당 지속", "성공"),("Portfolio", "2,211 units/3.2% vacancy", "안정", "2,943 units 현재", "성공")],
timeline=[("2001-12", "선행 VIC Long", "$29.50"),("2002-11", "2,211 units·3.2% vacancy", "T0 operating base"),("2002-12-28", "VIC Long", "$40·$80~85"),("2005", "후속 NEN 재평가", "cap regime 변화"),("2007", "repurchase program", "capital allocation"),("2012-01-03", "3-for-1 receipt split", "security basis 변경"),("2019", "founder succession", "governance test"),("2026", "2,943 apartments", "long-term survival")],
claimdata=[("12.5~13% cap", "시장 apartment yield보다 과도하게 높다.", "NEN vs REIT 8%", "portfolio quality가 비교가능하다.", "NOI 급락·cap gap 지속이면 반증.", "장기 value direction", "성공", "relative cap과 absolute spread를 함께 본다."),("6.6x AFFO", "trailing cash earnings가 싸다.", "$40/6.6x", "AFFO가 recurring capex를 포함한다.", "AFFO -20%면 반증.", "cash engine 존속", "성공 방향", "AFFO 정의를 재구성한다."),("vacancy downside", "3.2% vacancy가 rent softness를 흡수한다.", "2,211 units", "student demand가 견조하다.", "vacancy>6%면 반증.", "Boston portfolio 지속", "성공", "rent와 occupancy의 trade-off를 본다."),("low leverage", "net debt가 property value의 1/3이다.", "T0 balance sheet", "property values·DSCR 유지", "LTV>50%면 반증.", "장기 생존", "성공", "LTV와 maturity를 함께 본다."),("Brown redevelopment", "낡은 property 매입·개선이 성장한다.", "1996 이후 track record", "incremental ROIC가 높다.", "acquisition spread 음수면 반증.", "platform 확대", "성공", "operator는 cohort NOI로 측정한다."),("sale option", "Harold Brown 은퇴 시 $80~85 매각이다.", "77세·private gap", "GP가 매각을 원한다.", "독립 유지면 미실현.", "매각 없이 지속", "미실현", "owner-dependent sale은 base가 아니다.")]),

I(id="0e8dfe6c-4fa5-4b84-b087-7c4a26b60f4e", date="2005-12-09", author="nassau799", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="약 $80 (선행 canonical anchor)", horizon="3~5년", filename="analysis/ideas/2005/2005-12-09_NEN_long.md", link="https://www.valueinvestorsclub.com/idea/New_England_Realty_Associates/0584658068", desc=0, cat=231, security="Depositary Receipt = 1/10 Class A Unit (당시)", title="7.7% implied cap·$113 NAV Long", verdict="운영논지 부분 성공, 6% cap·cycle framing 실패", score=5.0, process=7.4,
summary="첨부 SQL에는 catalyst만 있고 description은 없다. 선행 canonical은 LTM NOI $16.6m, implied cap 약 7.7%, 6% cap NAV $113, property-level non-cross-collateralized debt와 Brown insider buying을 보존한다. 2001/02의 13% cap보다 안전마진이 크게 줄었는데 private transactions 5~6%를 보수적 anchor로 사용했다.",
valuation="`property value=NOI/cap rate`, `equity=property value-net debt+JV equity`다. $16.6m NOI를 6%로 자본화하면 $276.7m gross property value지만 8%면 $207.5m로 $69m 줄어든다. debt가 고정이면 이 감소가 receipt equity에 레버리지되어 $113 NAV를 크게 훼손한다.",
actual="Boston operating platform과 property-level financing은 생존했고 JV value creation도 일부 이어졌다. 그러나 2006~08 easy-credit peak와 GFC에서 cap rates·funding spreads가 반전돼 6%를 보수적이라고 본 핵심 valuation premise는 깨졌다. 현재 첨부자료에 price series가 없어 손실률은 재기재하지 않는다.",
price="기존 초안의 1/3/5년 수익률은 현 첨부 SQL에 performance COPY가 없어 검증할 수 없다. 모두 null로 재설정한다. 약 $80·$113만 prior canonical T0 anchor다.",
drivers="business quality는 유지됐지만 equity outcome을 지배한 것은 NOI보다 discount rate와 leverage였다. relative NAV discount보다 7.7% absolute entry cap, mortgage cost·maturity와 8~9% stress cap의 equity residual이 중요했다.",
error="거래시장 5~6% cap을 normal로 두어 full-cycle regime을 sensitivity 밖에 뒀다. insider alignment·non-cross-collateralization이 개별 property 손실전염은 줄여도 public receipt의 mark-to-market duration을 없애지 못한다.", first_signal="Boston apartment transactions이 5%대로 더 압축되고 debt growth가 NOI를 앞서거나 10Y/loan spread 상승으로 7%+ cap이 합리화되는 순간 $113 NAV를 8~9% cap으로 재산정한다.",
waterfall="NOI에서 property-level mortgage service·recurring capex·JV debt·GP 비용을 빼고 receipt 지분을 계산한다. non-cross-collateralized는 손실격리이지 NAV floor가 아니다.",
metrics=[("NOI", "$16.6m LTM", "rent·margin growth", "사업 지속", "성공 방향"),("Implied cap", "7.7%", "5~6%로 축소", "GFC expansion", "실패"),("NAV", "$113@6%", "discount 축소", "stress cap에 민감", "실패"),("Debt", "property-level", "contagion 제한", "구조 생존", "성공"),("Catalyst", "buying·JV·intrinsic growth", "hard sale 불필요", "장기 platform", "부분 성공")],
timeline=[("2001/02", "13% cap Longs", "넓은 safety margin"),("2005-12-09", "VIC Long", "7.7%→6% framing"),("2006", "occupancy·pricing 강세", "단기 확인"),("2007", "cap rates 5% 안팎", "cycle peak signal"),("2007", "repurchase program 시작", "alignment"),("2008~09", "credit crisis", "6% anchor 반증"),("2012", "receipt split", "price basis 변경"),("2026", "독립 LP 지속", "business survival")],
claimdata=[("property debt 격리", "non-cross-collateralized mortgage가 downside를 제한한다.", "asset별 financing", "default가 holdco 전체로 전염되지 않는다.", "guarantee·shared liquidity면 반증.", "structure 생존", "성공", "ring-fence와 equity volatility는 다르다."),("Brown alignment", "insider buying·local skill이 가치가 된다.", "owner-operator history", "매입 yield가 높다.", "related-party leakage면 반증.", "platform 지속", "성공", "alignment는 거래가격·fee로 확인한다."),("JV optionality", "50/50 JV·condo conversion이 NAV를 높인다.", "property-level projects", "sales proceeds가 NEN에 귀속된다.", "JV debt·tax가 흡수하면 반증.", "일부 value creation", "부분", "JV는 gross value가 아닌 equity interest다."),("6% cap 보수성", "quality apartments는 6% 이하가 맞다.", "2005 private transactions", "easy credit가 정상이다.", "full-cycle cap>7%면 반증.", "GFC로 반증", "실패", "peak comps를 normal로 쓰지 않는다."),("NOI offsets cap", "rent·margin이 discount-rate 상승을 상쇄한다.", "occupancy 개선", "NOI growth가 충분히 빠르다.", "cap +200bp면 반증.", "leverage로 NAV 훼손", "실패", "NOI와 cap sensitivity를 동시 shock한다."),("$113 NAV floor", "큰 NAV discount가 주가를 지지한다.", "$16.6m/6%", "private bid가 유동적이다.", "transactions freeze면 반증.", "hard floor 아님", "실패", "NAV는 실행가능한 net proceeds일 때만 floor다.")]),

I(id="41361162-0766-4c8f-8479-39b0ad418956", date="2007-02-27", author="pirate681", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="원문 가격 미복원", horizon="2~5년", filename="analysis/ideas/2007/2007-02-27_NEN_long.md", link="https://www.valueinvestorsclub.com/idea/New_England_Realty_Associates/8458157585", desc=4273, cat=174, security="Depositary Receipt = 1/10 Class A Unit (당시)", title="5% cap·margin expansion·activist Long", verdict="운영 단기 적중, cap-rate·activist 핵심 실패", score=3.8, process=6.8,
summary="98.4% occupancy, LTM NOI $17.4m(+3%), operating margin 55.2%(+80bp)를 근거로 2005 이후 cap rate가 100bp 더 압축됐다고 봤다. 5.0% cap에서 NAV $131, margin +50bp면 $154였고 Mercury Real Estate Advisors의 value-unlock 압력까지 붙인 Long이다.",
valuation="원문 sensitivity는 cap 6.31~4.0%와 margin -50~+100bp를 교차했다. 5.0%/0bp=$131, 5.0%/+50bp=$154다. 그러나 credit crisis에서는 표의 상단인 6.31%보다 높은 cap, frozen transaction volume과 higher mortgage spread가 가능했다. 표가 정교해도 regime 밖이면 false precision이다.",
actual="당시 occupancy·NOI·margin은 좋아 단기 operating claim은 맞았지만 easy-credit peak 뒤 GFC가 왔다. financing condition과 required return이 급변해 cap-compression·$131/$154 valuation premise가 붕괴했고 activist는 hard sale로 이어지지 않았다. NERA는 생존했지만 이는 T0 price payoff 성공과 다르다.",
price="첨부 SQL에는 performance data가 없다. 기존 초안의 1/2/3/5년 숫자는 현 파일로 검증되지 않아 제거했고 exact return은 null이다. business survival만으로 Long 성공을 선언하지 않는다.",
drivers="손실 메커니즘은 occupancy가 아니라 `cap rate 상승×고정 debt`의 equity convexity였다. EQR 5%, AVB 4%, Archstone 4.5%는 모두 같은 easy-money regime에 노출된 상대 comp였고 activist ownership은 transaction certainty가 아니었다.",
error="historical full-cycle cap와 debt refinancing spread를 sensitivity에 넣지 않았다. margin +50bp를 bull로 더하면서 cap 5%를 base로 둬 operating/multiple 두 낙관을 중첩했고, activist의 board seat·tender funding·deadline도 없었다.", first_signal="2007 transaction cap가 4~5%로 내려가고 credit spread·Treasury가 오르거나 apartment REIT NAV discounts가 확대되는 순간 sensitivity를 7~9%까지 넓혀야 했다.",
waterfall="$17.4m NOI를 gross value로 바꾸기 전 full-cycle cap를 적용하고 property debt·JV debt·recurring capex·GP 비용을 뺀다. activist는 signed transaction 전까지 현금이 아니다.",
metrics=[("NOI", "$17.4m/+3%", "성장", "단기 운영 견조", "성공"),("Occupancy", "98.4%", "pricing power", "단기 확인", "성공"),("Margin", "55.2%/+80bp", "+50bp", "discount shock가 압도", "부분"),("Cap/NAV", "5.0%/$131", "compression", "GFC regime 반전", "실패"),("Bull NAV", "+50bp=$154", "unlock", "hard catalyst 없음", "실패")],
timeline=[("2005-12", "6% cap Long", "late-cycle 시작"),("2006-09", "98.4% occupancy", "T0 strength"),("2007-02-27", "VIC Long", "5%/$131·$154"),("2007", "credit cycle peak", "first regime warning"),("2008", "transaction·funding shock", "cap thesis 반증"),("2008~09", "GFC", "equity NAV compression"),("2012", "receipt split", "후속 price basis"),("2026", "LP 생존", "business≠return")],
claimdata=[("operating environment", "98.4% occupancy가 rent power를 만든다.", "fully occupied portfolio", "demand가 macro보다 견조하다.", "occupancy<95%면 반증.", "단기 strength", "성공", "property KPI와 valuation rate를 분리한다."),("margin expansion", "55.2%에서 +50bp가 가능하다.", "+80bp trailing", "expense inflation이 낮다.", "margin 하락이면 반증.", "일부 운영개선", "부분", "margin bull을 cap bull과 중복하지 않는다."),("cap compression", "2005 대비 100bp 낮은 5%가 base다.", "REIT 4~5% comps", "easy credit가 지속된다.", "funding spread 확대면 반증.", "GFC로 붕괴", "실패", "full-cycle rate를 표에 넣는다."),("peer anchor", "EQR·AVB·ASN이 NEN NAV를 지지한다.", "5%·4%·4.5% cap", "quality·liquidity 차이가 작다.", "peer 모두 rerate면 반증.", "systemic repricing", "실패", "동일 factor comp는 독립 안전마진이 아니다."),("activist unlock", "Mercury가 value를 현실화한다.", "activist ownership", "board influence·buyer·funding이 있다.", "deadline·tender 부재면 반증.", "hard transaction 미실현", "실패", "촉매는 권한·돈·날짜로 검증한다."),("$131/$154", "NOI와 margin을 자본화하면 큰 upside다.", "sensitivity table", "range가 tail을 포함한다.", "cap>6.31%면 반증.", "range 밖 regime 발생", "실패", "sensitivity 범위 선택이 모델의 핵심이다.")]),

I(id="2f580789-fcdc-4c31-931a-6835a6aba060", date="2009-08-29", author="clancy836", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="약 $55 (선행 canonical anchor)", horizon="3~5년", filename="analysis/ideas/2009/2009-08-29_NEN_long.md", link="https://www.valueinvestorsclub.com/idea/NEW_ENGLAND_REALTY_ASSC__-LP/5338998526", desc=0, cat=94, security="Depositary Receipt = 1/10 Class A Unit (당시)", title="post-GFC 8.1% cap·buyback Long", verdict="cycle·capital-allocation 강한 성공 방향, exact return 미검증", score=9.2, process=9.2,
summary="첨부 SQL에는 catalyst만 있고 description은 없다. 선행 canonical은 약 $55, FY2008 NOI $16.1m, market cap $72.6m, EV $198.6m와 8.1% implied cap을 보존한다. 7% cap NAV도 $79로 약 44% upside였고 2007 이후 share count 20%+ 감소, 2008 장기 mortgage refinancing이 GFC 하방을 지지했다.",
valuation="5.4% cap NAV $131, 6% $108, 7% $79를 비교했다. entry가 8.1% implied cap라서 2007의 5% 가정과 달리 cap expansion 일부가 이미 가격에 있었다. base는 7%/$79, upside는 credit normalization과 buyback이며 sale/liquidation은 필요하지 않았다.",
actual="NERA의 residential NOI와 long-term property financing은 위기를 통과했고 repurchase program·배당·portfolio 운영이 지속됐다. 현재 2,943 apartments·37년 dividend 기록으로 business durability는 확인된다. 다만 기존 초안의 장기 주가수익률은 현 첨부 SQL에서 검증되지 않아 제거한다.",
price="현 SQL에 performance COPY가 없다. 약 $55와 $79/$108/$131 valuation anchors만 보존하고 exact return은 null이다. 2012 split과 distributions를 반영한 별도 series가 필요하다.",
drivers="GFC 뒤 8.1% absolute entry cap, 2013 이후로 미뤄진 주요 maturity와 장기 고정 financing이 survival을 만들었다. NAV discount가 큰 상태의 buyback은 같은 현금으로 property보다 더 높은 implied yield를 사는 capital allocation이었다.",
error="7% cap를 bear가 아니라 base로 둔 것이 훌륭했지만 recession rent decline·student concentration과 JV guarantee를 더 수치화할 수 있었다. liquidation/sale은 GP 의사와 tax 때문에 probability가 낮았다.", first_signal="NOI가 $16.1m에서 15% 이상 하락하거나 DSCR<1.5x, major maturity 이전 LTV>65%, buyback 중단과 equity issuance가 동시에 나타나면 post-GFC safety margin을 재검토한다.",
waterfall="$16.1m NOI에 stress cap를 적용한 뒤 $126m 안팎 순부채 implied bridge, JV 지분·debt와 recurring capex를 반영한다. buyback은 receipt당 NAV accretion으로 비교한다.",
metrics=[("Entry", "약 $55", "$79@7%", "사업·cycle 회복", "방향 성공"),("NOI", "$16.1m", "recession 안정", "portfolio 지속", "성공"),("Implied cap", "8.1%", "7% normalization", "high-yield entry", "강한 성공 방향"),("Buyback", "2007 이후 >20%", "per-share accretion", "장기 program", "성공"),("Maturity", "2008 refinancing", "주요 2013+", "downturn 통과", "성공")],
timeline=[("2007", "5% cap peak Long", "비교 실패"),("2007~09", "20%+ buyback", "share shrinkage"),("2008", "long-term refinancing", "survival buffer"),("2009-08-29", "VIC Long", "8.1% cap"),("2012-01-03", "3-for-1 receipt split", "basis change"),("2013+", "주요 maturities", "refi test"),("2019", "succession", "operator continuity"),("2026", "2,943 apartments·37년 배당", "business outcome")],
claimdata=[("recession NOI", "residential NOI가 위기에도 안정적이다.", "$16.1m FY2008", "Boston demand·occupancy가 견조하다.", "NOI -15%면 반증.", "portfolio survival", "성공", "cycle bottom은 NOI downside부터 본다."),("8.1% entry cap", "market stress가 좋은 absolute yield를 준다.", "$198.6m EV/$16.1m NOI", "cap가 9%+로 영구 상승하지 않는다.", "normalized cap>8%면 반증.", "business/value direction", "강한 성공", "같은 회사도 entry cap가 투자를 바꾼다."),("7% NAV $79", "stress cap에서도 44% upside다.", "5.4/6/7% table", "net debt·JV가 정확하다.", "NOI·debt로 NAV<$55면 반증.", "downside bridge 유효", "성공 방향", "bull보다 conservative cap의 residual을 본다."),("accretive buyback", "NAV 할인 receipt를 계속 산다.", "share count >20% 감소", "liquidity·debt보다 높은 return이다.", "LTV 상승·고가 매입이면 반증.", "장기 repurchase program", "성공", "buyback yield와 property yield를 비교한다."),("refinancing survival", "2008 장기 debt로 maturity wall을 피한다.", "major maturities 2013+", "fixed-rate DSCR가 충분하다.", "near-term covenant breach면 반증.", "위기 통과", "성공", "cycle bottom에서는 거래보다 runway다."),("sale optionality", "dividend·buyback·eventual sale이 촉매다.", "SQL catalyst", "GP가 가치실현을 택한다.", "독립 지속이면 sale 제외.", "buyback·dividend만 실현", "부분", "필요 없는 catalyst는 base에서 뺀다.")]),

I(id="ff823bb1-262b-42e6-a648-9c7755df43f0", date="2011-06-30", author="nassau799", ticker="NEN", entity="New England Realty Associates Limited Partnership", group="nen", raw_short=False, direction="Long", entry="약 $69 (FCF yield 역산)", horizon="3~5년", filename="analysis/ideas/2011/2011-06-30_NEN_long.md", link=None, desc=5503, cat=46, security="Depositary Receipt = 1/10 Class A Unit (당시)", title="8.6% core cap·JV·buyback compounder Long", verdict="사업·per-share compound 방향 강한 성공, exact return 미검증", score=9.3, process=9.5,
summary="hard catalyst가 없음을 인정하고 intrinsic value 50~60% discount와 그 자체의 성장을 샀다. 2011E NOI $17m을 6%로 자본화한 consolidated equity $107/share에 7 JV 지분 $27를 더해 $134, JV 제외 core implied cap 8.6%, FCF $5.32와 cash-on-cash 7.7%를 계산했다.",
valuation="$17m/6%=$283m EV에서 debt $142m을 빼 $141m/$107 per receipt, JV equity $35m/$27를 더해 $134다. 2,288 wholly owned units+JV proportional 358 units을 enterprise value로 나누면 $88k/unit였고, 열위자산 실제 매각 $96k~133k/unit보다 낮았다. 약 $69 entry는 $5.32/7.7%에서 역산한 값이므로 quoted price가 아니다.",
actual="Boston rent는 2010말부터 firming했고 Dexter Park 등 JV와 consolidated portfolio가 운영됐다. 2007~10 약 30% receipt buyback이라는 행동증거와 장기 property management가 이어졌다. 2012 3-for-1 split, 2019 founder succession 뒤에도 현재 2,943 apartments와 37년 dividend record가 지속된다.",
price="첨부 SQL에 performance가 없다. 기존 초안의 1년·3년 수익률은 provenance가 없어 제거했다. $134 appraisal과 역산 $69는 T0 valuation anchor이며 exact return/IRR은 null이다.",
drivers="8.6% core cap와 12.7% JV-adjusted cash-on-cash, 30% share shrinkage, supply-constrained Boston rental recovery가 함께 작동했다. hard catalyst 대신 NAV growth와 discount buyback이 per-share value를 스스로 높였다.",
error="6% cap을 conservative라 부르려면 2007 실패 후 full-cycle 7~9% case를 병렬로 보여야 했다. $35m JV equity는 Dexter Park value·JV mortgage·40% interest를 property별로 bridge하고 86세 Harold Brown succession을 더 크게 할인해야 했다.", first_signal="Boston vacancy·concessions 상승으로 NOI<$15.5m, 2013~14 refi cost가 FCF yield를 잠식하거나 successor capital allocation이 buyback 대신 low-spread acquisition으로 바뀌면 $134 appraisal을 내린다.",
waterfall="Consolidated NOI에서 $142m mortgage·recurring capex·G&A를 빼고, 7 JV는 40~50% ownership의 property value에서 각 JV debt를 차감한 equity share만 더한다. receipt 1/10 기준을 유지한다.",
metrics=[("NOI", "$17mE", "6%=$283m EV", "Boston operation 지속", "성공"),("Equity NAV", "$107+$27 JV", "$134", "business value 성장", "방향 성공"),("Core cap", "8.6%", "discount 축소", "high-yield entry", "강한 성공 방향"),("FCF", "$5.32/share", "7.7%/JV adj 12.7%", "cash engine 지속", "성공"),("Buyback", "2007~10 약 30%", "평균 <$74", "장기 program", "성공")],
timeline=[("2007~10", "약 30% repurchase", "capital-allocation evidence"),("2009", "Dexter Park $129.5m JV", "hidden value"),("2010말", "Boston rental firming", "operating turn"),("2011-06-30", "VIC Long", "$134 appraisal"),("2012-01-03", "receipt 3-for-1 split", "1/10→1/30"),("2013~14", "refinancing window", "rate risk test"),("2019", "Harold→Jameson generation", "succession"),("2026", "portfolio·dividend 지속", "long-term outcome")],
claimdata=[("Boston supply", "land·permit 제약과 student/healthcare가 rent를 지지한다.", "2010말 market firming", "new supply·demand shock가 제한된다.", "vacancy>6%면 반증.", "운영 platform 지속", "성공", "local moat은 supply·tenant mix로 검증한다."),("8.6% core cap", "JV를 빼도 과도한 yield다.", "consolidated implied cap", "NOI·debt가 정확하다.", "stress cap로 NAV<price면 반증.", "business/value direction", "강한 성공", "hidden value 없이도 base가 서야 한다."),("JV $27/share", "7 JVs가 accounting 밖 equity다.", "Dexter Park 409 units·40%", "JV debt·ownership이 반영됐다.", "net JV equity<$15면 반증.", "assets 지속", "성공 방향", "JV는 proportional net equity로 계산한다."),("$88k/unit", "enterprise basis가 실제 sales보다 낮다.", "$96k~133k/unit sales", "quality·location이 비교가능하다.", "needed capex로 gap 소멸 시 반증.", "low basis thesis 유지", "성공", "unit comp를 NOI·capex로 조정한다."),("FCF yield", "$5.32는 7.7%, JV 제외 후 12.7%다.", "interest·2011 capex 차감", "maintenance capex가 충분하다.", "coverage<1x면 반증.", "cash generation 지속", "성공", "property FCF에서 recurring capex를 분리한다."),("no-catalyst buyback", "30% buyback·운영성장이 catalyst를 대신한다.", "2007~10 평균 <$74", "successor도 rational하다.", "고가매입·희석이면 반증.", "long-running program", "성공", "시간은 per-share NAV가 자랄 때만 catalyst다.")]),
]


def idea_sources(idea):
    raw = m.S(
        "첨부 SQL 원문·catalyst / repository metadata",
        idea["link"],
        "VIC_IDEAS(4).sql / VIC / prior curated overlay",
        idea["date"],
        f"idea_id·date·author·raw Long; description {idea['desc']} chars·catalyst {idea['cat']} chars",
        "원문",
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
    text = text.replace("Batch 046 canonical report.", "Batch 052 canonical report.")
    text = text.replace("### Common equity cash waterfall", "### Security cash waterfall")
    text = text.replace(generic, idea["waterfall"])
    text = text.replace(
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |",
        f"| 회사 / 원 ticker | {idea['entity']} / {idea['ticker']} |\n| 실제 Security | **{idea['security']}** |",
    )
    text = text.replace(
        f"`ATH`를 회사로 보지 말고 {idea['entity']} 법인·exchange·날짜로 고정한다.",
        f"`{idea['ticker']}`를 단일 회사로 보지 말고 {idea['entity']} 법인·날짜·분배증권으로 고정한다.",
    )
    text = text.replace(
        "원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.",
        "원문·metadata: **A/B** — 첨부 SQL에는 catalyst 10건·description 7건만 있다. date·author·link는 repository prior overlay와 대조했다.",
    )
    text = text.replace(
        "가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.",
        "가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. 기존 overlay 수익률을 폐기하고 exact return/IRR을 null로 재설정했다.",
    )
    return text


def payload():
    old = m.idea_sources
    m.idea_sources = idea_sources
    try:
        out = m.make_payload(IDEAS)
    finally:
        m.idea_sources = old
    out["batch"] = 52
    out["title"] = "Madison Square Garden / New England Realty — Separation, Accounting and Cap-Rate Cycle V9"
    null_keys = (
        "perf_1m", "perf_3m", "perf_6m", "perf_1y", "perf_2y", "perf_3y", "perf_5y",
        "idea_return_1y", "idea_return_3y", "idea_return_5y",
    )
    for idea, master, post in zip(IDEAS, out["ideas_master"], out["postmortems"]):
        master["security_ko"] = idea["security"]
        master["performance_available"] = 0
        master["contest_winner"] = int(idea["contest"])
        master["auto_tag_status_ko"] = "raw Long 일치·법인/분배증권 수동감사·성과 null"
        for key in null_keys:
            master[key] = None
        post["research_direction_ko"] = f"Long / {idea['security']}"
        post["research_status_ko"] = "SQL catalyst·available description·공식 사건 검증; performance COPY 부재로 exact return null"
        post["confidence"] = 0.93 if idea["desc"] else 0.84
    return out


def make_index():
    rows = []
    for n, idea in enumerate(IDEAS, 1):
        link = Path(idea["filename"]).relative_to("analysis").as_posix()
        rows.append(f"| {n} | {idea['date']} | {idea['entity']} | Long | {idea['verdict']} | [{idea['title']}]({link}) |")
    return "\n".join([
        "# Batch 052 — Madison Square Garden / New England Realty Associates — V9 Index", "",
        f"> Research as-of {ASOF}. Batch 051 다음 10건이다. **10 idea = 10 canonical reports**이며 현 첨부 SQL로 확인되지 않는 성과값은 모두 null 처리했다.", "",
        "## 0. 배치 결론", "",
        "MSG 4건은 같은 SOTP가 `renovation capex cliff→2015 Media 분할→2020 Sports/Entertainment 분할→2023 Sphere 분할`로 실제 securities가 되는 과정이다. NEN 6건은 같은 operator·자산이어도 13% cap의 2001/02, 5~7% late-cycle 2005/07, 8%+ post-GFC 2009/11의 결과가 왜 달라지는지를 보여준다.", "",
        "## 1. Idea Units", "", "| # | 날짜 | 실제 회사 | 방향 | 사후 판정 | Canonical report |", "|---:|---|---|---|---|---|", *rows, "",
        "## 2. SQL / Entity / Security Audit", "",
        "첨부 `VIC_IDEAS(4).sql`에는 `catalyst·companies·descriptions` COPY만 있고 `ideas·performance` data COPY가 없다. 10건 모두 catalyst는 있으나 description은 7건만 존재한다. date·author·link는 기존 curated overlay와 대조했고, 기존 초안의 NEN 성과비율 4건은 provenance가 없어 폐기했다. 방향은 10건 모두 raw Long=실제 Long이다.", "",
        "MSG 2012/14는 pre-2015 common으로 MSGN 잔존주식과 3:1 신 MSG를 함께 받아야 한다. MSG 2016/18은 post-2015 common으로 2020 1:1 MSGE를 더해야 한다. NEN은 2012 전 1/10 Unit receipt, 이후 1/30 Unit receipt다.", "",
        "## 3. MSG — 투자논지의 진화", "",
        "- **2012:** $1bn renovation이 끝나는 capex cliff와 $275m+ FCF를 샀다. $1bn debt buyback은 optional이었고 실제 unlock은 분할이었다.\n- **2014:** RSN $4.6bn이 price를 지지하고 teams·venue·air rights $27/share가 upside였다. 2015 분할이 bucket을 직접 증권화했다.\n- **2016:** carve-out -$114m loss에서 termination·reserve·DTA·transition cost를 조정해 ongoing $209를 만들었다. 핵심은 one-time 비용의 반복성 감사다.\n- **2018:** announced spin은 맞았지만 Sphere를 $700m cost로 더한 가정은 틀렸다. 2020 COVID와 초과 capex 때문에 catalyst success와 payoff가 갈렸다.", "",
        "## 4. NEN — 같은 회사, 다른 entry cap", "",
        "| 시기 | T0 absolute yield | 핵심 risk/reward | 판정 |", "|---|---|---|---|", "| 2001/02 | 12.5~13.4% cap, 5.8~6.6x cash earnings | 낮은 leverage·운영복리 | 강한 성공 방향 |", "| 2005 | 7.7% implied vs 5~6% private | relative cheap, absolute buffer 축소 | valuation 실패 |", "| 2007 | 5% cap+margin expansion+activist | easy-credit peak 낙관 중첩 | 핵심 실패 |", "| 2009/11 | 8.1~8.6% cap+buyback | refinancing survival·per-share compounding | 강한 성공 방향 |", "",
        "## 5. 공통 투자 교훈", "",
        "1. SOTP는 분배증권·교환비율·세금을 연결해야 투자수익이 된다.\n2. capex cliff는 EBITDA보다 FCF를 더 빠르게 바꾼다.\n3. carve-out add-back은 `비현금`이 아니라 `비반복`인지 3년으로 검사한다.\n4. cost는 asset value가 아니다. 미완성 growth capex에는 completion·ROIC haircut이 필요하다.\n5. 부동산 NAV discount와 absolute cap-rate safety margin을 분리한다.\n6. peer cap가 동시에 낮으면 relative cheapness는 독립 안전마진이 아니다.\n7. activist는 권한·자금·날짜가 있어야 catalyst다.\n8. hard catalyst가 없어도 할인 buyback과 NAV/share 성장은 시간을 catalyst로 만든다.\n9. business survival과 common return은 별도 판정한다.\n10. 성과 테이블이 없으면 exact return은 null이다.", "",
        "## 6. 산출물", "",
        "- Payload: `data/curated/batch_052_msg_nen_deep_v7.json`\n- Wrapper: `analysis/batch_052_msg_nen_10.md`\n- Source packet: `data/curated/batch_052_source_packet.json`\n- Builder: `scripts/52_build_batch_052_v9.py`", "",
    ])


def main():
    if len(IDEAS) != 10 or len({idea["id"] for idea in IDEAS}) != 10:
        raise ValueError("Batch 052 requires ten unique ideas")
    for idea in IDEAS:
        if len(idea["claims"]) != 6 or len(idea["metrics"]) != 5 or len(idea["timeline"]) < 6 or len(idea_sources(idea)) < 5:
            raise ValueError(f"Invalid V9 structure: {idea['id']}")
        path = ROOT / idea["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report(idea), encoding="utf-8")
    parts = [Path(idea["filename"]).relative_to("analysis").as_posix() for idea in IDEAS]
    wrapper = "# Batch 052 — Madison Square Garden / New England Realty Associates V9\n\n" + f"<!-- batch_parts: {'|'.join(parts)} -->\n\n" + "> Streamlit wrapper. [Batch 052 V9 Index](batch_052_v9_index.md).\n"
    (ROOT / "analysis/batch_052_msg_nen_10.md").write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_052_v9_index.md").write_text(make_index(), encoding="utf-8")
    out = payload()
    (ROOT / "data/curated/batch_052_msg_nen_deep_v7.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet = {
        "batch": "052", "format": "V9-per-idea", "source": "VIC_IDEAS(4).sql + prior curated metadata + official filings",
        "record_count": 10, "raw_descriptions_present": 7, "raw_catalysts_verified": 10,
        "current_attachment_performance_rows_found": 0, "legacy_overlay_performance_values_discarded": 4,
        "direction_corrections": 0, "security_normalizations": 10,
        "performance_rule": "No performance COPY in current attachment; all exact returns remain null",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["entity"], "author": i["author"],
            "raw_direction": "Long", "research_direction": "Long", "security": i["security"], "description_chars": i["desc"],
            "catalyst_chars": i["cat"], "performance_available": False, "canonical_report": i["filename"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_052_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = {
        "source_filename": "VIC_IDEAS(4).sql", "attachment_bytes_checked": 122499072, "records_selected": 10,
        "copy_tables_present": ["catalyst", "companies", "descriptions"], "idea_rows_in_attachment": 0,
        "raw_descriptions_present": 7, "raw_descriptions_absent": 3, "raw_catalysts_verified": 10,
        "performance_copy_present": False, "performance_rows_found": 0, "legacy_overlay_rows_nullified": 4,
        "note": "Current attachment controls. Corporate events and prior unproven ratios are not exact returns.",
    }
    (ROOT / "data/curated/batch_052_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(out[key]) for key in ("ideas_master", "postmortems", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
