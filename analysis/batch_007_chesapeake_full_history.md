# Batch 007 — Chesapeake Energy (CHK), 셰일 자산·부채·파산 9건

평가기준일: 각 글의 명시 보유기간과 증권별 실제 결과, 장기사업 확인은 2024-01-31  
분석일: 2026-09-03  
대상 VIC 아이디어: 2001-04-05~2021-02-17, 총 9건

## 결론부터

| 게시일 | 실제 증권·방향 | 원래 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|
| 2001-04-05 | 보통주 Long | 낮은 비용·가스부족, 약 $8→$18~20 | 생산·현금흐름과 주가가 크게 상승해 목표권 도달 | 성공 |
| 2006-06-24 | 보통주 Long | 인수·희석보다 reserve 가치가 큼, $45~60 | 2008년 $74까지 상승했으나 이후 급락; 자본배분 평가는 틀림 | 가격 성공·논지 부분 실패 |
| 2008-10-12 | 보통주 Long | $16.52는 강제청산, $22~24 반등·$40 인수 | 반등은 발생했지만 인수는 없었고 CEO 위험은 오히려 현실화 | 부분 성공 |
| 2009-11-15 | 보통주 Short | 셰일 과잉·FCF 적자·부채로 약 $10 | 가스·지배구조 진단은 적중, 2년 목표는 실패; 2020 파산은 너무 늦음 | 논지 부분 성공·타이밍 실패 |
| 2011-02-08 | 보통주 Long | 25/25·liquids 전환·JV·Icahn 규율 | 이사회 개편은 발생했지만 부채·현금부족 지속, 장기 주가 붕괴 | 실패 |
| 2011-10-07 | 보통주 Long | Utica JV와 $52.35bn NAV, 주당 $68.43 | JV는 체결됐지만 NAV가 equity 현금흐름으로 전환되지 않음 | 치명적 실패 |
| 2015-12-11 | 6.5% 2017채 Long | $70 매수·만기보유, YTM 약 44% | 2016년 말 par redemption 발표로 원금·쿠폰 회수 | 매우 성공 |
| 2016-06-13 | 2020채 Long | $0.75·YTM 15%, 주주 희석이 채권 보호 | 2020년 만기 직전 Chapter 11, 무담보채권은 신주·warrant 회수 | 실패 |
| 2021-02-17 | 신 보통주 Long | 파산 후 저부채·저비용, 2022E 3.3x EBITDAX | 1년 +62.0%, 2년 +115.5%; 2022 CFO $4.13bn | 매우 성공 |

SQL의 방향값은 실제 원문과 크게 다르다. 본문·보유공시·추천 증권을 기준으로 교정하면
보통주 롱 6건, 회사채 롱 2건, 보통주 숏 1건이다. 특히 2015·2016년 글을 단순 CHK
보통주 아이디어로 합치면 분석이 망가진다. 같은 기업에서도 만기와 자본구조상 위치가
결과를 정반대로 만들었다.

> **CHK에는 실제로 좋은 셰일 자산이 있었다. 그러나 2006~2011년 롱들은 지하자원 가치와
> 기존 보통주가 가져갈 잔여가치를 혼동했다. 2015년 단기채는 파산보다 만기가 먼저 와서
> 성공했고, 2016년 장기채는 회사가 4년 더 버틸 것이라는 같은 생존논리로 실패했다.
> 2021년 롱은 파산을 거치며 과거 부채와 기존주주가 제거된 뒤 같은 자산을 샀기 때문에
> 성공했다.**

---

## 1. Chesapeake는 무슨 기업인가

Chesapeake는 미국 육상 셰일에서 천연가스·원유·NGL을 탐사하고 생산하는 E&P다.
수익은 생산량에 실현가격을 곱한 판매대금과 hedge 정산에서 나오며, 현금비용은 lease
operating expense, production tax, gathering·transportation, G&A와 이자다. 그러나
경제성을 결정하는 가장 큰 항목은 손익계산서 아래가 아니라 신규 시추·완결 capex다.

### ① 셰일 생산의 decline treadmill

셰일정은 초기 생산량이 높지만 빠르게 감소한다. 생산량을 유지하려면 계속 새 well을
뚫어야 한다. 따라서 EBITDA가 커 보여도 maintenance drilling을 빼면 FCF가 작거나
음수가 될 수 있다. 2006년 CHK는 영업현금 $4.84bn을 만들었지만 투자현금유출은
$8.94bn이었다. 차액 대부분을 부채·주식·preferred 같은 외부자본으로 채웠다.

### ② acreage와 Held By Production

초기 CHK의 경쟁력은 유망 basin의 lease를 빠르게 모으고 지질정보·수평시추·fracturing으로
core acreage를 선점하는 능력이었다. 그러나 lease는 일정 기간 내 시추하지 않으면
소멸할 수 있다. 수십 년치 inventory가 있어도 HBP를 위해 낮은 가스가격에서 시추하면
현재가치는 줄어든다. ‘acre당 최근 거래가 × 전체 면적’은 시간·개발비·품질차이를
생략한다.

### ③ reserve와 PV-10

proved reserve와 SEC PV-10은 중요한 자산지표지만 곧바로 equity value가 아니다.
가격 deck, decline curve, 미래개발비와 세금에 민감하고 그 아래에 순부채, preferred,
운송 최소물량계약, VPP와 corporate cost가 있다. 특히 undeveloped acreage는 구매자가
당장 같은 단가로 전부 살 수 있다는 보장이 없다.

### ④ hedge는 다리이지 영구가치가 아니다

CHK는 swap·collar뿐 아니라 knockout과 three-way 구조, 미래 call 매도로 당기 hedge
가격을 높였다. hedge는 단기 현금흐름을 안정시키지만 미래 upside를 팔거나 가격이
일정 수준 아래로 가면 보호가 사라질 수 있다. 2012년 상반기 실제 가스가격은 전년
$5.25/mcf에서 $2.11로 떨어졌고 영업현금은 2011년 $5.90bn에서 2012년 $2.84bn으로
반감했다.

### ⑤ JV·VPP·asset sale

CHK는 BP, Statoil, Total, CNOOC 등에 일부 working interest를 팔고 현금과 drilling carry를
받았다. 이는 acreage의 외부검증이자 자금조달이었지만 반복될수록 좋은 자산과 미래생산도
넘긴다. VPP도 현금을 선취하는 대신 특정 생산량의 미래매출을 이전한다. 거래 발표가
높은 acre valuation을 보여줘도 연결기업의 부채상환 후 주당가치 증가 여부는 별도다.

### ⑥ 같은 회사, 다른 증권

보통주는 모든 채무·계약을 지급한 뒤 남는 잔여청구권이다. 반면 2017·2020 senior note는
만기 전에 회사가 지불 가능한지가 핵심이다. 2020년 파산에서 기존 보통주·preferred는
무회수로 소각됐고, 무담보채권자는 재편회사 신주 12% pool과 warrant 일부를 배분받았다.
따라서 ‘기업이 살아남았다’는 말은 기존 주주, 단기채, 장기채에 전혀 다른 뜻이다.

---

## 2. 장기 자본순환

| 시점 | 핵심 수치·사건 | 해석 |
|---|---|---|
| 2000 | 생산 134 Bcfe, CFO 약 $305m | 높은 가스가격으로 2001 롱의 출발점 형성 |
| 2006 | CFO $4.84bn, 투자유출 $8.94bn, 금융유입 $4.04bn | 성장했지만 self-funded business가 아니었음 |
| 2008 | 주가 $74→$12, CEO 31m주 margin-call 매도 | 기업·CEO leverage가 같은 충격에 노출 |
| 2009 | 외부투입자본 누계 추정 $23.2bn, 순부채·preferred 약 $13.5bn | reserve 성장보다 debt-adjusted per-share가 중요 |
| 2011 | CFO $5.90bn | JV·hedge가 현금을 지지했으나 capex·의무도 큼 |
| 2012 | CFO $2.84bn, 상반기 가스 실현가 $2.11/mcf | 가격하락이 liquidity bridge를 약화 |
| 2015 | 약 $11.8bn senior debt, $4bn secured facility | 단기채와 장기채의 생존확률이 갈린 시점 |
| 2017 | 6.5% 2017 note par redemption 완료 | 만기가 파산보다 앞선 단기채 성공 |
| 2020-06-28 | Chapter 11 신청 | 기존 보통주·preferred 가치 0 |
| 2021-02-09 | 파산 탈출, 구 equity 취소·신주 발행 | 자산은 살아남고 청구권 소유자가 교체됨 |
| 2022 | successor CFO $4.13bn, 순이익 $4.94bn | 저부채 구조와 높은 commodity price 결합 |
| 2023 | CFO $2.38bn | 가격 정상화로 E&P의 cyclicality 재확인 |

---

# Part A. 2001년 보통주 Long

## 3. 원 논지

당시 CHK는 천연가스 중심 4,700개 well을 보유했고 Gothic Energy 인수로 proved reserve가
30% 늘어 1.656 Tcfe가 된다고 봤다. 2000년 생산은 6.6% 증가했고 gas 판매가는 $3.50/mcf,
총비용은 $2.05였다. 2001년 NYMEX $5.61을 가정해 cash flow $625m·주당 $3.70,
EPS $1.63을 예상했다. 약 5x P/E·2x cash flow에서 산업 5~6x cash flow를 적용해
$18~20을 목표로 했다.

## 4. 결과

가스가격·인수·생산성장이 결합해 2000년대 중반 CHK의 현금흐름과 주가는 크게 상승했고
목표가격권을 넘어섰다. **가격과 산업사이클 판정은 성공**이다.

다만 이 성공을 영구경쟁력으로 해석하면 안 된다. 높은 가격이 CFO를 늘리자 회사는 그보다
더 많은 돈을 acreage·인수에 썼고, 2006년 투자유출은 CFO의 1.85배였다. 초기 싸이클 롱은
맞았지만 이후 자본배분 위험의 씨앗도 같은 성장기에 생겼다.

---

# Part B. 2006년 보통주 Long

## 5. 원 논지

8.3 Tcfe proved·11.6 Tcfe unproved reserve, 저비용 onshore gas, 장기 hedge와 빠른 M&A를
강점으로 봤다. convertible 발행의 희석보다 매입 reserve 가치가 더 크며, 최근 거래의
$/mcfe를 적용한 takeout value와 DCF로 주당 $45~60을 제시했다. $6 gas에서 $40,
$7에서 $53.5, $8에서 $84라는 민감도였다.

## 6. 결과

2008년 7월 주가가 $74까지 올라 목표는 달성됐다. **정해진 가격목표 기준 성공**이다.
그러나 성공 원인은 저평가 해소뿐 아니라 gas가 $14 부근까지 급등한 commodity beta였다.
곧 주가는 $12까지 급락했다.

핵심 오판은 ‘좋은 가격에 산 acreage’와 ‘좋은 주당 자본배분’을 동일시한 것이다.
2006년 CFO $4.84bn에 투자유출 $8.94bn, 금융유입 $4.04bn이었다. reserve 거래가격은
asset value를 입증했지만 끊임없는 external funding과 미래 의무를 제거하지 못했다.
따라서 **가격 성공·과정 및 장기 논지 부분 실패**다.

---

# Part C. 2008년 보통주 Long

## 7. 원 논지

주가는 7월 $74에서 10월 $16.52로 떨어졌다. CEO Aubrey McClendon의 margin call로
31m주가 강제매도된 일시적 수급이라고 보고 $22~24 반등을 기대했다. majors는 현금이
많고 shale 노출이 부족하므로 내부지분이 사라진 CHK를 약 $40에 인수할 수 있다는 논리였다.

## 8. 결과

강제청산 뒤 반등이라는 전술 논리는 맞았고 이후 주가는 $20대 이상을 회복했다. 그러나
인수는 없었으며 McClendon의 레버리지·Founder Well Participation·hedge 구조는 일시적
noise가 아니라 governance와 risk appetite의 증거였다.

**부분 성공.** entry dislocation은 맞았지만 takeover를 주주규율의 대체재로 삼았다.
지배구조가 약한 회사는 ‘싼 가격 때문에 누군가 사준다’보다 현금고갈 전에 이사회가
행동할 확률을 모델링해야 한다.

---

# Part D. 2009년 보통주 Short

## 9. 원 논지

이 배치의 유일한 실제 숏이다. 40개 생산자의 계획을 모아 대형사가 2010년 생산을 약 5%
늘리므로 shale 공급이 예상만큼 줄지 않고 gas가 $3 이하로 간다고 봤다. CHK는 2010년
hedge가 22%에 불과하고 knockout·three-way 때문에 하락보호도 약했다.

기업 차원에서는 2000년대 common·preferred $10.4bn, 순부채 $12.3bn을 조달하고 주식수가
150m→625m으로 늘었는데 환원은 $0.6bn뿐이라고 지적했다. HBP drilling, VPP의 경제적
부채성, capitalized interest, $13.5bn 조정부채와 FCF -$1bn을 근거로 fair value 약
$10을 제시했다.

## 10. 결과

**사업 분석은 9건 중 가장 정확했다.** shale 공급과 낮은 gas price, debt-adjusted
per-share 가치파괴, McClendon 지배구조, 반복 asset sale과 외부자본 의존은 모두
후속 역사에서 확인됐다. 2012년 이사회가 재편되고 2013년 McClendon이 떠났으며 회사는
2020년 결국 파산했다.

그러나 2년 내 $10이라는 숏은 실패했다. 2010~11 JV·hedge·자산가치가 liquidity를
연장했고 주가는 즉시 붕괴하지 않았다. 파산은 10년 7개월 뒤 발생했다. **논지 부분
성공·타이밍 실패**다. 장기 인과가 맞아도 배당·대차·commodity squeeze를 10년 버틸 수
없으면 실행가능한 숏이 아니다.

---

# Part E. 2011년 2월 보통주 Long

## 11. 원 논지

시장은 CHK를 gas company로만 보지만 2012년 drilling capital의 70%가 liquids로 이동하고,
JV가 cash와 drilling carry를 주면서 25/25 plan—부채 25% 축소·생산 25% 성장—을
달성한다고 봤다. CNOOC JV가 토지 원가를 회수하고 잔여 acreage 가치를 만들었으며
Icahn이 McClendon을 통제하고 장기적으로 gas·oil 회사를 분할할 수 있다고 기대했다.

## 12. 결과

JV·liquids 전환과 2012년 이사회 재편은 실제였다. 그러나 2012 CFO는 $2.84bn으로
2011년의 절반 이하가 됐고 capex·transport·VPP·부채의 복합의무가 남았다. asset
monetization은 부채축소와 동시에 미래 생산·좋은 자산을 팔아야 하는 treadmill이었다.

**실패.** 촉매 일부가 발생했는데도 equity가치가 늘지 않았다. ‘활동이 일어남’과
‘그 활동 뒤 순부채를 차감한 주당가치가 증가함’을 분리하지 않았다.

---

# Part F. 2011년 10월 보통주 Long

## 13. 원 논지

Utica JV가 underfunded capex를 해결하고 McClendon의 acreage 정보우위가 지속된다고 봤다.
Barnett $5.2bn, Eagle Ford $9bn, drilling carry $2.6bn, legacy PV-10 $13bn, Marcellus
$12bn, Utica $12.5bn 등을 합산해 부채·negative working capital $12bn 차감 후 equity
$52.35bn, 희석주당 $68.43을 계산했다. Utica는 $15~20bn 잠재가치였다.

## 14. 결과

2012년 Total과의 Utica JV는 실제 체결됐다. 하지만 이것이 thesis를 살리지 못했다.
acreage comparator는 소수지분 거래·drilling carry·개발시점·transport commitment와
대량매각 할인 없이 전체 면적에 적용됐다. ‘내일 각 자산을 제시가격에 팔 수 있다’는
가정과 회사를 계속 운영하는 가정도 동시에 사용했다.

2012년 gas shock, governance 위기와 asset sales 뒤에도 부채문제는 계속됐고 보통주는
2021년 파산계획에서 무회수 소각됐다. **치명적 실패.** 자산가치는 있었지만 waterfall
상단 채권자와 계속된 자금소요가 그 가치를 흡수했다.

---

# Part G. 2015년 6.5% 2017채 Long

## 15. 원 논지

$70에 거래되는 6.5% senior note를 2017-08-15 만기까지 보유해 약 44% YTM을 얻고,
8% second-lien 2022채 교환에는 응하지 말라고 했다. 회사 전체 장기생존을 맞힐 필요 없이
‘구조조정이 2018년 이후’이기만 하면 됐다. $4bn secured facility, 단기채 우선교환,
현금·asset sale과 covenant 여유가 시간 다리였다.

## 16. 결과

회사는 2016년 equity issuance·asset sale·tender로 단기만기를 줄였고 2016년 12월 남은
6.5% 2017채를 par에 상환한다고 발표했다. 원금과 coupon이 파산 3년 전에 회수됐다.

**매우 성공.** 가장 좋은 점은 기업가치 전체를 맞히려 하지 않고 필요한 생존기간을
20개월로 제한한 것이다. 2020년 회사가 파산했다는 사실은 이 단기채 논지를 반증하지
않는다.

---

# Part H. 2016년 2020채 Long

## 17. 원 논지

2020년 만기채를 $0.75, YTM 15%에 매수했다. 2016년 3~6월 네 차례 주식발행으로 약
$549m 부채를 갚았고, 주가도 $1.60에서 $5로 올라 주주가 희석을 받아들인다는 점을
채권자 보호로 봤다. $2.1bn의 3년 만기벽은 개선된 commodity price, asset sale과
$4bn ABL로 넘을 수 있다고 판단했다.

## 18. 결과

이 글은 2015년 단기채 성공을 더 긴 만기에 외삽했다. equity issuance는 채권친화적이었지만
유한했고, 2019년에도 장기부채는 약 $9bn대였다. 2020년 commodity shock 직후 회사는
채권 만기 전에 Chapter 11을 신청했다. 무담보채권자는 현금을 par로 받은 것이 아니라
재편회사 신주 12% pool과 warrant 일부를 pro rata로 받았다.

**실패.** ‘management가 주주를 희석할 의향이 있다’와 ‘2020년까지 희석 가능한 equity
market cap·자산매각 여력이 충분하다’ 사이에 수치화된 runway가 없었다. 성공한
short-dated bond play의 표면패턴을 만기위험이 다른 증권에 복제했다.

---

# Part I. 2021년 파산 후 신 보통주 Long

## 19. 원 논지

파산 직후 신주를 약 $40에 추천했다. market cap $4.2bn, debt $1.25bn, TEV $5.46bn에서
2021E EBITDAX $1.125bn은 4.9x, 2022E $1.66bn은 3.3x였다. 현금 operating cost/boe가
2019년 $15.81에서 $9.75로 39% 낮아지고 총 operating cost는 약 50% 감소했다고 봤다.
2021년 hedge가 upside를 막지만 2022년 hedge가 적어 높은 gas price가 이익에 반영된다는
논리였다.

## 20. 결과

가격은 1년 +61.95%, 2년 +115.46%였다. 2021 successor CFO $1.81bn, 2022 $4.13bn,
2022 순이익 $4.94bn으로 실제 현금흐름은 보수적 추정을 크게 웃돌았다. debt가 제거된
상태에서 commodity upcycle이 equity로 전달됐다.

**매우 성공.** 과거 CHK 롱과 달리 ‘좋은 acreage’가 아니라 파산으로 제거된 청구권,
새 debt와 current cash cost를 출발점으로 삼았다. 다만 2022 성과에는 높은 gas price가
크게 기여했으므로 이를 영구 정상마진으로 외삽하면 안 된다.

---

## 21. 9건을 관통하는 성공·실패 유형

### 유형 ① Asset value와 equity value 혼동

지하자원은 가치가 있었고 파산 뒤에도 생산됐다. 하지만 기존주주는 0을 받았다.
NAV는 순부채뿐 아니라 future development capex, transport·VPP·preferred와 corporate
burn을 모두 차감한 뒤 잔여가치를 확률가중해야 한다.

### 유형 ② CFO를 FCF로 착각

2006년 CFO $4.84bn만 보면 현금창출기업이지만 투자유출 $8.94bn을 함께 보면 외부자본
의존기업이다. E&P에서는 maintenance capex 정의가 투자논지의 중심이어야 한다.

### 유형 ③ 거래가치를 전체 acreage에 외삽

JV는 일부 core acreage와 carry 조건의 가격이다. 이를 전체 미개발 면적에 곱하고 즉시
현금화 가능하다고 가정하면 시간가치·quality dispersion·대량매각 할인이 사라진다.

### 유형 ④ Commodity call과 기업분석의 귀속

2001·2006 롱의 가격 성공에는 gas 상승이 컸고, 2009 숏의 가스 논지가 맞아도 JV·hedge가
equity timing을 늦췄다. return을 commodity beta, hedge, production, cost, capital
structure와 multiple로 분해해야 한다.

### 유형 ⑤ 만기가 thesis다

2017채와 2020채는 같은 issuer·비슷한 가격에도 결과가 반대였다. bond thesis의 핵심은
ultimate solvency보다 maturity 이전 누적 liquidity와 선순위 담보 증가 위험이다.

### 유형 ⑥ 파산은 사업의 종말이 아니라 소유권 이전

2020년 old equity는 소각됐지만 2021년 신 equity는 성공했다. ‘회사가 살아남았다’로
구주주 투자를 정당화할 수 없다. 법인·자산의 생존과 특정 security의 회수율을 분리한다.

---

## 22. 학습 태그

| 아이디어 | 태그 |
|---|---|
| 2001 Long | `commodity_cycle`, `low_multiple`, `target_success`, `future_capital_intensity` |
| 2006 Long | `reserve_nav`, `commodity_beta`, `price_right_process_wrong`, `external_funding` |
| 2008 Long | `forced_seller`, `governance`, `takeover_catalyst_failure`, `partial_success` |
| 2009 Short | `shale_oversupply`, `capital_allocation`, `thesis_right_timing_wrong`, `short_duration` |
| 2011-02 Long | `asset_monetization`, `liquids_pivot`, `activist`, `cash_bridge_failure` |
| 2011-10 Long | `sum_of_parts`, `acreage_extrapolation`, `waterfall_error`, `equity_zero` |
| 2015 Bond Long | `security_selection`, `maturity_wall`, `runway`, `very_successful` |
| 2016 Bond Long | `pattern_copy_error`, `refinancing_risk`, `unsecured_recovery`, `failure` |
| 2021 Long | `post_reorg_equity`, `deleveraging`, `cost_reset`, `commodity_upcycle` |

---

## 23. 재사용 체크리스트

1. CFO에서 sustaining drilling과 lease 유지 capex를 빼면 실제 FCF는 얼마인가?
2. reserve·acreage value에서 debt 외의 preferred·transport·VPP·future development를 뺐는가?
3. 비교거래가 core 일부인지 전체 면적에 적용 가능한지 확인했는가?
4. hedge의 당기 현금이 미래 call 매도나 knockout 대가인지 분해했는가?
5. asset sale 뒤 순부채뿐 아니라 미래생산과 증분 FCF도 줄어드는가?
6. 보통주·secured debt·unsecured debt·preferred를 각각 별도 idea로 기록했는가?
7. bond 만기까지 분기별 liquidity sources와 uses를 만들었는가?
8. 담보제공으로 내 채권의 recovery waterfall이 후순위화되는가?
9. commodity price가 30~50% 하락해도 covenant와 borrowing base가 유지되는가?
10. 파산 후 신주 성과를 파산 전 구주주의 회복으로 잘못 연결하지 않았는가?

---

## 24. 주요 근거

- VIC 원문: 2001년 글은 제공 SQL 원문; [2006 Long](https://www.valueinvestorsclub.com/idea/Chesapeake_Energy/0972844482),
  [2008 Long](https://www.valueinvestorsclub.com/idea/Chesapeake_Energy/5799977098),
  2009·2011 두 글은 제공 SQL 원문,
  [2015 6.5% 2017채](https://www.valueinvestorsclub.com/idea/Chesapeake_Energy_Corp_6.5%25_Senior_Notes_Due_2017/1854027054),
  [2016 2020채](https://www.valueinvestorsclub.com/idea/Chesapeake_2020_Debt/8290091537),
  [2021 post-BK Long](https://www.valueinvestorsclub.com/idea/Cheasapeak_Energy/3120958886).
- [Chesapeake 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000119312507043979/d10k.htm)
- [Chesapeake 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000089512613000076/chk-2012123110k.htm)
- [Chesapeake 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000089512616000395/chk-20151231_10k.htm)
- [Chesapeake 2016 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000089512617000068/chk-20161231_10k.htm)
- [Chapter 11 Restructuring Support Agreement](https://www.sec.gov/Archives/edgar/data/895126/000110465920077745/tm2023599d1_ex10-1.htm)
- [Chesapeake 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000089512621000078/chk-20201231.htm)
- [Chesapeake 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000089512622000029/chk-20211231.htm)
- [Chesapeake 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/895126/000089512624000013/chk-20231231.htm)
- [2017채 par redemption 발표](https://www.prnewswire.com/news-releases/chesapeake-energy-corporation-announces-redemption-of-65-senior-notes-due-2017-300383198.html)

### 데이터 해석 주의

- 초기 8건의 SQL performance series는 비어 있어 허위 정밀수익률을 만들지 않았다.
  원문 가격·목표, SEC 사건과 당시 공개가격 범위로 판정했다.
- 2021년 신주는 SQL 가격비율을 실제 롱으로 교정해 1년 +61.95%, 2년 +115.46%다.
- 2020년 reverse split과 파산 전·후 CHK는 경제적으로 다른 증권이다.
- 회사채 판정은 보통주 가격이 아니라 coupon·par 상환 또는 Chapter 11 recovery로 했다.

