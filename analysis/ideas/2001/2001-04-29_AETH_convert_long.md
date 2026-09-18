# Aether Systems (AETH Corp) — 2001-04-29 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Aether Systems / AETH Corp |
| VIC 게시일 / 작성자 | 2001-04-29 / gumpster335 |
| 분석 증권 / 실제 방향 | 6% convertible subordinated notes due 2005 / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 59 cents on par |
| 기대기간 | 2005 maturity |
| raw horizon audit | 6% coupon, conversion $243.95, cash-covered par recovery |
| 최종 판정 | **강한 성공 — security selection과 par redemption** |

> **결론:** common 약 $13.89에서 $243.95 conversion은 사실상 out-of-the-money였지만 note는 약 59에 샀고 6% coupon을 받았다. 회사는 2004-10-04에 101.2% par+accrued interest로 조기상환했다. 정확한 IRR은 coupon settlement ledger 없이 과장하지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

Aether Systems는 무선 데이터 소프트웨어·서비스와 여러 지분투자를 가진 닷컴시대 회사였다. 이 아이디어의 대상은 common이 아니라 6% convertible subordinated notes due 2005다. 전환가치, 현금·투자자산으로 뒷받침되는 상환가치와 senior claims를 함께 봐야 하며, 높은 주가 upside 없이도 par redemption이 수익의 주된 원천이었다.

unrestricted cash + realizable investments + operating value - senior claims - note principal = coverage; coupon·call price·accrued interest를 채권 payoff로 계산한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

unrestricted cash, realizable investments, cash burn, senior claims, note coverage, coupon, call price, maturity, conversion value

---

## 2. 당시 상황과 시장이 가격에 넣은 것

닷컴 붕괴로 common은 크게 하락했지만 issuer의 cash·investments가 note principal을 상당히 덮는다는 논지였다. upside는 전환보다 credit recovery였다.

### Reverse expectations

시장은 cash burn, 투자자산 가치하락, subordination과 2005 전 유동성 소진을 할인했다.

---

## 3. 원문 투자논지 지도

### C1. cash covers note — 성공

**원문 주장**

cash·investments가 principal을 덮는다.

**경제적 메커니즘**

hard assets가 credit floor.

**T0 근거**

balance sheet.

**숨은 가정**

burn 제한·assets realizable.

**사전 반증조건**

coverage <1x면 반증.

**실제 결과**

101.2 redemption 가능.

**정량 gap**

principal 전액+premium.

**분석 오류 또는 제한**

restricted/senior 차감 부족.

**재사용 교훈**

net hard coverage를 쓴다.

### C2. 6% coupon — 성공

**원문 주장**

보유 중 6% coupon.

**경제적 메커니즘**

contractual cash payment.

**T0 근거**

indenture.

**숨은 가정**

default 없음.

**사전 반증조건**

coupon 중단이면 반증.

**실제 결과**

상환 전 지급.

**정량 gap**

current yield ~10.2%.

**분석 오류 또는 제한**

settlement dates 미복원.

**재사용 교훈**

exact IRR은 ledger 후 계산한다.

### C3. par recovery — 강한 성공

**원문 주장**

59→100.

**경제적 메커니즘**

maturity/redemption.

**T0 근거**

discounted note.

**숨은 가정**

issuer solvent.

**사전 반증조건**

recovery <80이면 반증.

**실제 결과**

101.2+accrued.

**정량 gap**

+42.2 points before coupon.

**분석 오류 또는 제한**

none material.

**재사용 교훈**

fixed claim의 terminal term을 기준으로 판정한다.

### C4. conversion upside — 불필요·미실현

**원문 주장**

$243.95 conversion option.

**경제적 메커니즘**

common rally 때 upside.

**T0 근거**

convert feature.

**숨은 가정**

common 17x+ 상승.

**사전 반증조건**

far OTM 지속이면 0 가치.

**실제 결과**

T0 common ~$13.89; credit payoff로 종료.

**정량 gap**

option 거의 0.

**분석 오류 또는 제한**

convert 명칭이 upside를 과장.

**재사용 교훈**

straight bond로도 매력적인지 본다.

### C5. cash burn manageable — 성공

**원문 주장**

운영 burn이 coverage를 소진하지 않는다.

**경제적 메커니즘**

cost cuts·asset monetization.

**T0 근거**

large cash base.

**숨은 가정**

분기 burn 감소.

**사전 반증조건**

redemption 전 liquidity crisis면 반증.

**실제 결과**

조기상환.

**정량 gap**

위기 없음.

**분석 오류 또는 제한**

burn path 단순화.

**재사용 교훈**

quarterly sources/uses를 갱신한다.

### C6. security beats common — 강한 성공

**원문 주장**

common 대신 note가 downside를 제한.

**경제적 메커니즘**

priority와 contractual maturity.

**T0 근거**

subordinated라도 common보다 선순위.

**숨은 가정**

senior claims 과도하지 않음.

**사전 반증조건**

common 상승 없고 note도 haircut이면 반증.

**실제 결과**

common recovery 불필요, note 101.2.

**정량 gap**

구조적 payoff 적중.

**분석 오류 또는 제한**

issuer thesis보다 security thesis가 핵심.

**재사용 교훈**

capital structure 전체에서 최적 claim을 고른다.

---

## 4. 당시 Valuation과 Payoff Structure

59 purchase price에서 6 coupon의 current yield는 약 10.2%. par 또는 101.2 call이면 가격 recovery가 크지만 conversion value는 거의 0으로 두는 것이 보수적이다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | cash burn·asset haircut | par 미달 recovery | 미발생 |
| Base | maturity par | coupon+41pt gain | 조기 초과실현 |
| Bull | conversion | $243.95+ common | 불필요 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Purchase price | 59 | par recovery | 101.2 redemption | 강한 성공 |
| Coupon | 6% | 지급 | redemption 전 지급 | 성공 |
| Current yield | ~10.2% | 유지 | coupon/59 | 성공 |
| Conversion price | $243.95 | optionality | common ~$13.89 at T0 | 무가치 option |
| Maturity | 2005 | 상환 | 2004-10-04 조기상환 | 조기 성공 |

### 촉매와 시간

판정 horizon은 **2005 maturity**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2001-04-29 | VIC note Long | 59 purchase |
| 2001 | common ~$13.89 | conversion far OTM |
| 2002 | cash coverage 추적 | credit thesis |
| 2003 | burn·asset monetization | coverage 유지 |
| 2004-H1 | redemption 여력 | catalyst 접근 |
| 2004-10-04 | 101.2 call | principal recovery |
| 2004-10-04 | accrued interest 지급 | coupon settlement |
| 2005 | 원 maturity | 그 전에 종료 |

### 실제 사업·자본구조 추이

6% convertible subordinated notes는 2004-10-04에 101.2% of par plus accrued interest로 redeemed됐다. common이 전환가를 회복할 필요가 없었다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

확정 terminal consideration은 101.2+accrued interest다. 개별 coupon dates와 reinvestment가 없어 exact annualized return은 보류한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | cash covers note | 20% | 성공 | principal 전액+premium. |
| C2 | 6% coupon | 18% | 성공 | current yield ~10.2%. |
| C3 | par recovery | 18% | 강한 성공 | +42.2 points before coupon. |
| C4 | conversion upside | 16% | 불필요·미실현 | option 거의 0. |
| C5 | cash burn manageable | 16% | 성공 | 위기 없음. |
| C6 | security beats common | 12% | 강한 성공 | 구조적 payoff 적중. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익은 사업 turnaround가 아니라 discounted fixed claim과 cash coverage, issuer의 조기 redemption에서 나왔다.

### Counterfactual

분기 burn이 두 배이고 투자자산을 50% haircut해도 senior claims 뒤 note principal이 덮였는가?

---

## 9. 분석 오류 유형과 최초 경고

결론은 맞았지만 headline cash에서 operating burn과 senior/restricted claims를 더 명시적으로 차감했어야 한다.

### 최초로 관찰 가능했던 경고신호

note coverage가 1x 아래로 떨어지거나 분기 burn이 가속되면 첫 경고였으나 redemption이 먼저 일어났다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

같은 issuer라도 common과 cash-covered convert의 payoff는 전혀 다르다.

### Lesson 2

distressed bond는 conversion upside보다 hard coverage와 redemption terms를 먼저 본다.

### Lesson 3

headline cash에서 burn·senior claims·restricted cash를 차감한다.

### Lesson 4

정확한 IRR은 coupon settlement ledger가 있을 때만 계산한다.

### 지금 같은 아이디어를 다시 본다면

- unrestricted cash
- quarterly burn
- senior claims
- note coverage
- call price
- accrued coupon
- conversion value

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | common 불필요 |
| Valuation thesis | 강한 성공 |
| Catalyst thesis | redemption 성공 |
| Security payoff | convert 적절 |
| Timing / path | 만기 전 성공 |
| Thesis score | 9.0/10 |
| Process score | 9.2/10 |
| 종합 | **강한 성공 — security selection과 par redemption** |

### 한 문장 교훈

> 같은 issuer라도 common과 cash-covered convert의 payoff는 전혀 다르다.

---

## 12. Sources / Validation Notes

1. [VIC source-DB preserved original](https://www.valueinvestorsclub.com/idea/Aether_Systems_6_percen_05_Co/6957633241) — Value Investors Club / source SQL, 2001-04-29. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [Aether Systems SEC issuer archive](https://www.sec.gov/edgar/browse/?CIK=1086844&owner=exclude) — SEC, 2001-2004. 6% notes, cash/investment coverage와 2004 redemption 검증.
3. [Aether corporate reorganization no-action letter](https://www.sec.gov/divisions/corpfin/cf-noaction/aether042605.htm) — SEC, 2005-04-26. 후속 법인 재편과 security identity 교차검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported high/period-end price만 사용; exact total-return ledger가 없으면 IRR·MFE를 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
