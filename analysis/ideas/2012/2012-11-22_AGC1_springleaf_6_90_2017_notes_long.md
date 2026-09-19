# Springleaf Finance Corporation (AGC1) — 2012-11-22 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-19. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Springleaf Finance Corporation / AGC1 |
| VIC 게시일 / 작성자 | 2012-11-22 / creditguy |
| 분석 증권 / 실제 방향 | 6.90% Medium-Term Notes Series J due 2017 / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 87; YTM 약 10% |
| 기대기간 | 12개월 spread tightening·2017 pull-to-par |
| raw horizon audit | delinquency normalization, securitization access, Fortress alignment와 maturity management |
| 최종 판정 | **매우 강한 성공 — exchange·repurchase·maturity 해결** |

> **결론:** 6.90% 2017 notes를 약 87에 사 coupon, pull-to-par와 spread tightening을 노렸다. 2013 회사는 $700m principal을 2021/2023 notes로 교환하고 약 $184m 현금매입을 계획했으며, 2017 약 $466m을 추가 repurchase했다. holder 선택별 exact IRR은 다르지만 maturity-wall thesis는 매우 강하게 적중했다.

---

## 1. 회사는 정확히 무엇을 하는가

American General Finance와 후신 Springleaf Finance는 branch 기반 consumer finance lender였다. 높은 수익률의 personal·retail·real-estate receivables에서 credit loss, servicing cost와 funding cost를 차감해 unsecured debt service를 만든다. 채권자는 common upside가 아니라 만기별 coupon·principal과 secured·structural subordination 뒤 recovery를 산다.

`receivable collections - credit losses - opex - secured funding cost = unsecured debt capacity`; maturity별 coupon·exchange·repurchase·principal cash flow를 추적한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

receivable balance, 60+ delinquency, charge-off, reserve coverage, cash, unencumbered assets, secured/unsecured debt, maturity wall, securitization yield, exchange/repurchase price

---

## 2. 당시 상황과 시장이 가격에 넣은 것

60+ delinquency는 non-real-estate loans 2.90%로 5.09% peak보다 낮았고 retail finance 2.71%도 약 6.1% peak에서 개선됐다. 2012 cash 약 $1.5bn과 $500m note receivable, 약 $200m FCF가 약 $15bn debt를 받쳤고 securitization yields는 4.38%→3.59%→2.80%로 하락했다. 원문은 liquidity가 2016까지 확보됐다고 판단했다.

### Reverse expectations

equity FCF가 양수여도 large debt stack의 maturity concentration과 secured funding은 unsecured note를 위협할 수 있었다. delinquency 개선이 loan sales·forbearance 효과일 수 있고 Fortress는 equity sponsor이지 bond guarantee가 아니었다. exchange는 par cash repayment가 아니라 duration 연장일 수 있었다.

---

## 3. 원문 투자논지 지도

### C1. 87 price·10% YTM — 강한 성공

**원문 주장**

2017 note는 normalized credit에 비해 싸다.

**경제적 메커니즘**

coupon+13-point pull-to-par+spread tightening이 return을 만든다.

**T0 근거**

price ~87와 6.90% coupon.

**숨은 가정**

principal impairment가 없다.

**사전 반증조건**

expected recovery 87 미만이면 반증.

**실제 결과**

exchange·repurchase·maturity가 principal을 보존했다.

**정량 gap**

exact holder IRR 미확정.

**분석 오류 또는 제한**

quoted YTM와 realized path를 혼용할 수 있다.

**재사용 교훈**

dirty price와 cash-flow election을 저장한다.

### C2. delinquency normalization — 성공

**원문 주장**

consumer book credit가 2009 peak에서 회복한다.

**경제적 메커니즘**

lower delinquency·charge-off가 cash collection과 funding access를 개선한다.

**T0 근거**

non-RE 2.90% vs 5.09%; retail 2.71% vs ~6.1%.

**숨은 가정**

improvement가 seasoning·sale effect만은 아니다.

**사전 반증조건**

두 분기 재악화면 반증.

**실제 결과**

후속 securitization와 public issuance가 market validation을 제공했다.

**정량 gap**

asset-level loss curve 없음.

**분석 오류 또는 제한**

delinquency 수준만으로 ultimate loss cash를 완전히 설명할 수 없다.

**재사용 교훈**

credit KPI와 capital-market KPI를 연결한다.

### C3. liquidity through 2016 — 부분 성공

**원문 주장**

$1.5bn cash·$500m note·FCF가 runway를 준다.

**경제적 메커니즘**

cash+collections가 near-term maturities를 넘어 refinancing window를 연다.

**T0 근거**

원문 liquidity bridge.

**숨은 가정**

cash가 restricted가 아니고 burn이 관리된다.

**사전 반증조건**

2015 이전 funding gap이면 실패.

**실제 결과**

2013 exchange로 2017 wall 일부가 장기화됐다.

**정량 gap**

2017까지 자동 보장된 것은 아님.

**분석 오류 또는 제한**

runway 끝과 maturity date를 혼동했다.

**재사용 교훈**

월별 sources/uses를 maturity까지 연장한다.

### C4. securitization funding 회복 — 강한 성공

**원문 주장**

yield 4.38%→2.80%는 시장 접근 개선이다.

**경제적 메커니즘**

lower asset funding cost가 equity cash와 unsecured refinance capacity를 높인다.

**T0 근거**

2012 sequential transaction yields.

**숨은 가정**

collateral performance와 advance rates가 유지된다.

**사전 반증조건**

deal 취소·haircut 급증이면 반증.

**실제 결과**

2013 unsecured 2021/23 notes까지 발행했다.

**정량 gap**

public funding으로 확장.

**분석 오류 또는 제한**

headline yield만 보고 structural subordination을 작게 봤다.

**재사용 교훈**

advance rate·tranche와 recourse를 함께 본다.

### C5. Fortress alignment·platform value — 성공

**원문 주장**

sponsor가 franchise를 유지하고 capital markets를 연다.

**경제적 메커니즘**

equity sponsor의 option value와 IPO/scale plan이 default avoidance를 지지한다.

**T0 근거**

Fortress control과 operating franchise.

**숨은 가정**

sponsor가 추가 capital·refinancing을 선택한다.

**사전 반증조건**

asset strip·bankruptcy면 실패.

**실제 결과**

Springleaf/OneMain platform이 확대되고 debt market 접근이 회복됐다.

**정량 gap**

support 방향 적중.

**분석 오류 또는 제한**

sponsor alignment를 guarantee처럼 볼 위험.

**재사용 교훈**

sponsor incentives와 legal claims를 분리한다.

### C6. 2017 maturity management — 강한 성공

**원문 주장**

회사는 2017 notes를 exchange·repurchase·pay할 수 있다.

**경제적 메커니즘**

new long-term notes와 cash tender가 wall을 줄인다.

**T0 근거**

improving liquidity·funding market.

**숨은 가정**

new debt terms가 지속 가능하다.

**사전 반증조건**

2017 payment default면 실패.

**실제 결과**

2013 $700m exchange, ~$184m cash plan, 2017 ~$466m repurchase.

**정량 gap**

wall 대부분 구체적으로 해결.

**분석 오류 또는 제한**

gross issuance만 보고 net debt를 놓칠 수 있다.

**재사용 교훈**

maturity별 beginning-to-ending principal roll-forward를 만든다.

---

## 4. 당시 Valuation과 Payoff Structure

87 price의 bond return은 coupon 6.90%, pull-to-par 13 points와 spread duration이다. base는 2017 par, bull은 12개월 spread tightening, bear는 exchange coercion·recovery haircut이다. exchange holder는 2021/2023 notes를 받으므로 original 2017-note IRR과 successor cash flows를 연결해야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | credit 재악화·funding shut | 60~80 recovery | 미실현 |
| Base | carry+2017 par | low-mid teens 1Y 후 par | principal path 실현 |
| Bull | rapid spread tightening | 90s/100 조기 | refinancing이 지지 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Bond price/YTM | ~87/~10% | low-mid teens 1Y | principal impairment 없음 | 강한 성공 |
| Non-RE 60+ delinquency | 2.90% vs 5.09% peak | 계속 개선 | funding 회복 | 성공 |
| Securitization yield | 4.38→3.59→2.80% | access 개선 | public notes 발행 | 강한 성공 |
| 2013 exchange | $700m | wall 완화 | 2021/23로 교환 | 성공 |
| 2017 repurchase | maturity risk | 상환 | ~$466m | 강한 성공 |

### 촉매와 시간

판정 horizon은 **12개월 spread tightening·2017 pull-to-par**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2012-11-22 | VIC bond Long | ~87·~10% YTM |
| 2012-12 | credit metrics 개선 | delinquency down |
| 2013-09-24 | new notes issued | $650m 2021+$300m 2023 |
| 2013-09-25 | $700m exchange | 2017 wall 분산 |
| 2013 | ~$184m cash repurchase plan | principal reduction |
| 2015 | OneMain transaction era | platform scale |
| 2017-05 | ~$466m repurchase | tail 제거 |
| 2017 maturity | remaining notes 해결 | credit thesis 완료 |

### 실제 사업·자본구조 추이

2013-09 Springleaf는 $500m 7.75% 2021 notes와 $200m 8.25% 2023 notes를 $700m 2017 notes와 교환했고 약 $184m 2017 notes cash repurchase를 계획했다. 2017에는 약 $466m principal을 추가 repurchase하기 위한 financing을 조달했다. remaining maturity가 해결되며 principal impairment thesis는 발생하지 않았다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

원문 low-to-mid teens 12개월 return은 spread/coupon 방향상 타당했지만 trade·exchange election 자료가 없어 exact realized total return을 확정하지 않는다. 87에서 principal impairment 없이 exchange·cash repurchase·maturity path를 통과한 점은 payoff의 핵심을 입증한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 87 price·10% YTM | 20% | 강한 성공 | exact holder IRR 미확정. |
| C2 | delinquency normalization | 18% | 성공 | asset-level loss curve 없음. |
| C3 | liquidity through 2016 | 18% | 부분 성공 | 2017까지 자동 보장된 것은 아님. |
| C4 | securitization funding 회복 | 16% | 강한 성공 | public funding으로 확장. |
| C5 | Fortress alignment·platform value | 16% | 성공 | support 방향 적중. |
| C6 | 2017 maturity management | 12% | 강한 성공 | wall 대부분 구체적으로 해결. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

delinquency 개선이 funding access 회복으로 이어졌고 securitization yield 하락이 public unsecured refinancing을 가능하게 했다. 2013 exchange는 maturity wall을 분산했고 2017 cash repurchase가 잔여 tail을 줄였다.

### Counterfactual

securitization yield가 다시 6%로 오르고 delinquency가 peak의 80%까지 반등해도 2017 principal을 현금·자산매각 없이 상환할 수 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

liquidity through 2016을 2017 maturity solution과 거의 같은 것으로 봤다. exchange는 default avoidance에는 긍정적이지만 holder에게 duration·coupon·liquidity risk를 바꾸므로 par repayment와 동일하지 않다.

### 최초로 관찰 가능했던 경고신호

2013 exchange pricing이 punitive하거나 participation이 사실상 강제였다면 return thesis를 다시 계산해야 했다. 실제 exchange와 cash repurchase는 긍정적 de-risking 신호였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

normalizing credit는 delinquency가 funding cost로 이어지는 bridge를 본다.

### Lesson 2

bond pull-to-par와 spread tightening을 분리한다.

### Lesson 3

exchange는 default 해결과 holder return을 별도로 판정한다.

### Lesson 4

maturity wall은 amount·date·committed liquidity로 추적한다.

### 지금 같은 아이디어를 다시 본다면

- CUSIP
- dirty price·accrued
- 60+ delinquency
- charge-off
- securitization yield
- unencumbered assets
- maturity ladder
- exchange consideration

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 성공 |
| Valuation thesis | 강한 성공 |
| Catalyst thesis | 강한 성공 |
| Security payoff | 2017 note 적절 |
| Timing / path | 강한 성공 |
| Thesis score | 9.5/10 |
| Process score | 9.0/10 |
| 종합 | **매우 강한 성공 — exchange·repurchase·maturity 해결** |

### 한 문장 교훈

> normalizing credit는 delinquency가 funding cost로 이어지는 bridge를 본다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/SPRINGLEAF_FINANCE_CORP/6086881565) — Value Investors Club / source SQL, 2012-11-22. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [AIG/Fortress AGF transaction announcement](https://www.sec.gov/Archives/edgar/data/25598/000134100410001987/ex99-1.htm) — SEC / AIG, 2010-08-11. Fortress affiliate의 AGF 80% acquisition agreement 검증.
3. [Springleaf Finance 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/25600/000002560011000014/inc1210.htm) — SEC / Springleaf, 2011-03-31. 2010-11-30 Fortress 80% closing, company lineage, cash·receivables·debt와 going-concern context 검증.
4. [2013 Springleaf exchange and notes](https://www.sec.gov/Archives/edgar/data/25598/000110465913072173/a13-20760_58k.htm) — SEC / Springleaf, 2013-09-25. $700m 2017 notes exchange, 2021/2023 notes와 약 $184m cash repurchase 계획 검증.
5. [2017 Springleaf note repurchase](https://www.sec.gov/Archives/edgar/data/25598/000104746917003674/a2232287z424b5.htm) — SEC / OneMain, 2017-05-25. 약 $466m 6.90% 2017 notes repurchase와 refinancing 조건 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B/C** — AGCO 2015·Alamos 2014는 source SQL price-only ratios, 그 외는 verified corporate action·official operating actual·제한적 market cross-check만 사용. complete dated ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
