# Allied Capital Corporation (AFC) — 2008-12-29 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Allied Capital Corporation / AFC |
| VIC 게시일 / 작성자 | 2008-12-29 / doggy835 |
| 분석 증권 / 실제 방향 | 6.875% senior unsecured notes due 2047 / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 35~36 cents on par; $25 par 기준 약 $8.75~9.00 |
| 기대기간 | credit normalization·change of control |
| raw horizon audit | credit-crunch easing, issuer buyback/equity raise; par recovery |
| 최종 판정 | **매우 강한 성공 — Ares assumption 후 par redemption** |

> **결론:** common이 아닌 6.875% senior unsecured notes due 2047이다. 약 $8.75~9.00에 산 $25 par claim은 2010 Ares가 인수하며 assumption됐고 2021 $25 par+accrued interest로 상환됐다. principal-only 단순 gain은 약 +178%이며 coupons와 exact IRR은 ledger 없이 만들지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

Allied Capital은 중소기업 대출·지분을 보유한 BDC였다. 이 아이디어의 대상은 common이 아니라 거래소 상장 6.875% senior unsecured notes due 2047이다. asset coverage, seniority, coupon, change of control와 call 조건이 payoff를 만들며 common NAV 회복은 필요한 조건이 아니었다.

realizable portfolio value - senior/secured claims - burn = unsecured-note coverage; coupon과 par redemption을 실제 cash dates로 계산한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

portfolio fair value, nonaccruals, secured claims, unsecured coverage, liquidity, coupon, quoted price/par, call price, accrued interest

---

## 2. 당시 상황과 시장이 가격에 넣은 것

GFC 중 Allied portfolio와 liquidity 불신으로 장기 senior note가 par의 35~36%에 거래됐다. 원문은 asset coverage와 credit-market 정상화, issuer action이 default보다 높은 recovery를 만든다고 봤다.

### Reverse expectations

NAV write-down, nonaccrual, leverage와 refinancing failure가 unsecured claim의 recovery를 par 아래로 낮출 수 있었다. 2047 maturity는 catalyst가 없으면 duration risk가 매우 컸다.

---

## 3. 원문 투자논지 지도

### C1. 35~36c mispricing — 강한 성공

**원문 주장**

note가 recovery보다 싸다.

**경제적 메커니즘**

asset coverage가 market panic을 이긴다.

**T0 근거**

quoted discount.

**숨은 가정**

unsecured recovery >36.

**사전 반증조건**

coverage 붕괴면 반증.

**실제 결과**

par redemption.

**정량 gap**

+64~65 points.

**분석 오류 또는 제한**

quoted cents/par 단위 주의.

**재사용 교훈**

$25 par dollars로 변환한다.

### C2. senior-note identity — 강한 성공

**원문 주장**

common보다 선순위 fixed claim을 산다.

**경제적 메커니즘**

contractual coupon·principal과 priority.

**T0 근거**

indenture terms.

**숨은 가정**

security 정확히 식별.

**사전 반증조건**

common으로 분류되면 분석 무효.

**실제 결과**

6.875% senior unsecured due 2047.

**정량 gap**

security 교정.

**분석 오류 또는 제한**

ticker-only mapping.

**재사용 교훈**

CUSIP·par·maturity를 저장한다.

### C3. asset coverage — 성공

**원문 주장**

haircut 후에도 note principal을 지지.

**경제적 메커니즘**

portfolio recoveries가 unsecured claims를 덮는다.

**T0 근거**

BDC assets.

**숨은 가정**

marks realizable.

**사전 반증조건**

nonaccrual·secured claims가 coverage <1x면 반증.

**실제 결과**

Ares assumption과 par repayment.

**정량 gap**

최종 100 recovery.

**분석 오류 또는 제한**

중간 coverage 수치 제한.

**재사용 교훈**

waterfall을 분기별 갱신한다.

### C4. credit-market easing — 성공

**원문 주장**

liquidity 정상화가 default risk를 낮춘다.

**경제적 메커니즘**

funding access·asset sales.

**T0 근거**

GFC panic entry.

**숨은 가정**

markets reopen.

**사전 반증조건**

refinancing failure면 반증.

**실제 결과**

2010 M&A 종결.

**정량 gap**

liquidity exit.

**분석 오류 또는 제한**

macro catalyst 광범위.

**재사용 교훈**

issuer-specific liquidity를 본다.

### C5. Ares assumption — 강한 성공

**원문 주장**

change of control이 credit를 보존한다.

**경제적 메커니즘**

stronger acquirer가 obligations를 assume.

**T0 근거**

deal structure.

**숨은 가정**

indenture 존속.

**사전 반증조건**

notes haircut/cancel이면 반증.

**실제 결과**

2010 notes assumed.

**정량 gap**

duration risk 감소.

**분석 오류 또는 제한**

T0 exact catalyst는 아님.

**재사용 교훈**

deal debt treatment를 직접 읽는다.

### C6. par+coupon payoff — 강한 성공

**원문 주장**

coupon을 받고 par 회수.

**경제적 메커니즘**

contractual redemption.

**T0 근거**

6.875% note.

**숨은 가정**

no default.

**사전 반증조건**

below-par exchange면 반증.

**실제 결과**

2021 $25+accrued.

**정량 gap**

principal 약 +178% before coupons.

**분석 오류 또는 제한**

exact IRR ledger 없음.

**재사용 교훈**

principal·coupon·reinvestment를 분리한다.

---

## 4. 당시 Valuation과 Payoff Structure

$25 par claim을 약 $8.75~9.00에 매입했다. payoff는 coupon+principal이고, common upside가 아니라 senior/secured claims 뒤 realizable asset coverage와 issuer liquidity가 결정한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | asset haircut·default | $10 미만 recovery | 미발생 |
| Base | credit normalize | $20~25+coupon | 실현 |
| Bull | M&A assumption·call | $25+accrued | 실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | 35~36c/par | par convergence | $25 redemption | 강한 성공 |
| Dollar price | $8.75~9/$25 par | $25 | $25+accrued | +~178% principal |
| Coupon | 6.875% | 지속 지급 | redemption 전 contractual | ledger 제한 |
| Assumption | 불확실 | credit catalyst | 2010 Ares assumption | 성공 |
| Maturity | 2047 | duration 단축 | 2021 redemption | 26년 단축 |

### 촉매와 시간

판정 horizon은 **credit normalization·change of control**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2008-12-29 | VIC note Long | 35~36c entry |
| 2009 | credit stress 완화 | coverage 개선 |
| 2010-04-01 | Ares acquisition | debt assumption |
| 2010 | coupon continuity | default tail 감소 |
| 2012-04-15 | par call window | contractual option |
| 2020 | notes outstanding | duration 지속 |
| 2021-02-23 | redemption notice | $25+accrued |
| 2021-03-25 | expected redemption | terminal payoff |

### 실제 사업·자본구조 추이

Ares Capital은 2010-04-01 Allied acquisition을 완료하며 notes를 assumed했다. 2021-03 잔여 약 $229.56m를 $25 par와 accrued interest에 redeem했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

$9 기준 $25/$9-1≈+177.8% principal-only 단순 gain이다. 2009~2021 coupon 지급일·세금·reinvestment가 완전하지 않아 total return과 annualized IRR은 보류한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 35~36c mispricing | 20% | 강한 성공 | +64~65 points. |
| C2 | senior-note identity | 18% | 강한 성공 | security 교정. |
| C3 | asset coverage | 18% | 성공 | 최종 100 recovery. |
| C4 | credit-market easing | 16% | 성공 | liquidity exit. |
| C5 | Ares assumption | 16% | 강한 성공 | duration risk 감소. |
| C6 | par+coupon payoff | 12% | 강한 성공 | principal 약 +178% before coupons. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

deep discount, seniority와 change-of-control assumption이 default tail과 매우 긴 maturity를 줄였고 최종 call이 par를 현금화했다.

### Counterfactual

portfolio를 40% haircut하고 secured debt·fees를 먼저 빼도 unsecured notes가 최소 80 cents recovery를 얻는가?

---

## 9. 분석 오류 유형과 최초 경고

원문 catalyst 중 issuer buyback·equity raise보다 실제 핵심은 Ares assumption이었다. 2047 duration과 coupon settlement를 더 명시적으로 시나리오화할 필요가 있었다.

### 최초로 관찰 가능했던 경고신호

Ares가 notes를 assume하지 않거나 coverage가 1x 아래로 내려가면 thesis break였지만 2010 assumption이 반대로 위험을 낮췄다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

distressed debt는 issuer 이름보다 exact security·seniority·par를 먼저 고정한다.

### Lesson 2

35 cents와 $8.75를 혼용하지 말고 $25 par 단위를 명시한다.

### Lesson 3

principal gain과 coupons를 분리하고 ledger 없이 IRR을 만들지 않는다.

### Lesson 4

M&A debt assumption은 duration risk를 바꾸는 핵심 event다.

### 지금 같은 아이디어를 다시 본다면

- CUSIP/security terms
- asset coverage
- nonaccruals
- senior claims
- liquidity
- coupon ledger
- call/redemption price

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | issuer 정상화 |
| Valuation thesis | deep discount 성공 |
| Catalyst thesis | M&A assumption 성공 |
| Security payoff | note 선택 우수 |
| Timing / path | 장기 hold·2021 종결 |
| Thesis score | 9.5/10 |
| Process score | 9.2/10 |
| 종합 | **매우 강한 성공 — Ares assumption 후 par redemption** |

### 한 문장 교훈

> distressed debt는 issuer 이름보다 exact security·seniority·par를 먼저 고정한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2008-12-29. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL은 source SQL에서 null이다.
2. [Ares assumes Allied notes](https://www.sec.gov/Archives/edgar/data/1287750/000104746910003449/a2197910z8-k.htm) — SEC / Ares Capital, 2010-04-01. Allied 인수와 2047 notes assumption, coupon·call 조건 검증.
3. [2047 notes redemption](https://www.sec.gov/Archives/edgar/data/1287750/000128775021000014/arcc-2047seniornotesredemp.htm) — SEC / Ares Capital, 2021-02-23. $229.56m 잔액을 $25 par+accrued interest로 상환한 조건 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported operating data만 사용; exact transaction ledger가 없으면 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
