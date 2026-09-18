# AfriSam Investment Holdings (AFRISJ) — 2010-11-01 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AfriSam Investment Holdings / AFRISJ |
| VIC 게시일 / 작성자 | 2010-11-01 / lvampa1070 |
| 분석 증권 / 실제 방향 | senior secured floating-rate notes / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 75~80 cents on par |
| 기대기간 | 2011~2013 restructuring |
| raw horizon audit | issuer leverage 약 7x, market-price leverage 약 3.5x EBITDA; base return 14~15% annual |
| 최종 판정 | **구조조정 성공 / holder-level IRR 미확정** |

> **결론:** raw Short를 실제 Long으로, security를 senior secured floating-rate notes로 교정했다. PIC와 80% 초과 noteholders가 합의했고 R15bn 초과 debt reduction·대규모 debt-to-equity conversion으로 capital structure가 정상화됐다. 다만 각 holder가 받은 cash/new notes/equity와 coupon ledger가 없어 14~15% IRR을 확정하지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

AfriSam은 남아공 cement producer였지만 이 아이디어의 증권은 common이 아니라 senior secured floating-rate notes였다. enterprise value에서 secured claims와 구조조정 비용을 차감한 recovery, coupon·swap·maturity와 debt-to-equity 교환조건이 수익을 결정한다.

restructuring enterprise value - super-priority/secured claims - costs = noteholder recovery; cash/PIK coupon·principal·equity conversion을 날짜별로 합산한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

exact note class, quoted price/par, collateral, senior debt, EBITDA, leverage, swap cost, coupon, maturity, recovery and equity conversion

---

## 2. 당시 상황과 시장이 가격에 넣은 것

AfriSam issuer leverage는 약 7x였지만 notes를 75~80c에 매입하면 market-price debt/EBITDA가 약 3.5x로 내려가고, collateral·restructuring에서 par보다 높은 recovery와 14~15% annual return을 기대한다는 distressed-credit thesis였다.

### Reverse expectations

시장은 cement cycle, LBO overleverage, swap·interest burden, cross-border documentation, PIC의 policy objectives와 recovery timing을 할인했다. secured라는 표지만으로 collateral control과 priority가 보장되지 않는다.

---

## 3. 원문 투자논지 지도

### C1. raw Short — metadata 실패

**원문 주장**

source SQL은 Short다.

**경제적 메커니즘**

방향 오류는 creditor payoff를 반전시킨다.

**T0 근거**

원문은 discount notes를 매수했다.

**숨은 가정**

본문 security가 실제 방향을 정한다.

**사전 반증조건**

default 이익을 노리면 Short다.

**실제 결과**

실제 secured-note Long.

**정량 gap**

완전 반대.

**분석 오류 또는 제한**

raw flag 의존.

**재사용 교훈**

증권·방향을 원문으로 교정한다.

### C2. senior secured status — 대체로 성공

**원문 주장**

notes가 collateral 우선권을 갖는다.

**경제적 메커니즘**

secured priority가 EV recovery를 보호한다.

**T0 근거**

indenture/원문 구조.

**숨은 가정**

lien perfection·priority 유지.

**사전 반증조건**

priming·collateral shortfall이면 실패.

**실제 결과**

restructuring에서 senior group이 핵심 협상자였다.

**정량 gap**

claim influence 확인; exact recovery 제한.

**분석 오류 또는 제한**

secured를 full coverage로 오인.

**재사용 교훈**

collateral별 waterfall을 만든다.

### C3. 75~80c recovery asymmetry — 방향 성공

**원문 주장**

discount가 loss를 흡수하고 upside를 준다.

**경제적 메커니즘**

purchase discount와 coupon이 recovery cushion.

**T0 근거**

quoted price와 EBITDA.

**숨은 가정**

EV가 senior claims를 커버.

**사전 반증조건**

recovery<75c면 실패.

**실제 결과**

claims가 new structure로 보존·전환됐다.

**정량 gap**

cash equivalent 미확정.

**분석 오류 또는 제한**

new paper를 par로 표시.

**재사용 교훈**

market value와 realized cash를 구분한다.

### C4. deleveraging — 강한 성공

**원문 주장**

구조조정이 debt를 크게 줄인다.

**경제적 메커니즘**

debt-to-equity와 terms reset.

**T0 근거**

PIC·noteholder incentives.

**숨은 가정**

supermajority·court/consents 확보.

**사전 반증조건**

deal collapse면 실패.

**실제 결과**

R15bn 초과 debt reduction.

**정량 gap**

규모·방향 강한 적중.

**분석 오류 또는 제한**

equity dilution은 creditor별 상이.

**재사용 교훈**

issuer와 holder 성과를 분리한다.

### C5. swap·interest relief — 성공 방향

**원문 주장**

Euribor swap 종료와 interest 감소.

**경제적 메커니즘**

cash coupon burden 축소가 going concern을 높인다.

**T0 근거**

원문 catalyst.

**숨은 가정**

termination cost manageable.

**사전 반증조건**

swap claim이 recovery를 잠식하면 실패.

**실제 결과**

new structure가 historic burden을 낮췄다.

**정량 gap**

exact swap settlement 미공개.

**분석 오류 또는 제한**

gross debt reduction과 cash interest 혼용.

**재사용 교훈**

coupon·swap cash dates를 별도 둔다.

### C6. 14~15% annual return — 미확정

**원문 주장**

restructuring으로 mid-teens annual 수익.

**경제적 메커니즘**

discount accretion+coupon+equity option.

**T0 근거**

75~80c entry.

**숨은 가정**

1~3년 내 liquid recovery.

**사전 반증조건**

지연·illiquid paper면 미달.

**실제 결과**

package 완료, holder ledger 없음.

**정량 gap**

IRR 산출 불가.

**분석 오류 또는 제한**

par exchange를 실현으로 볼 위험.

**재사용 교훈**

cash·PIK·equity를 날짜별로 추적한다.

---

## 4. 당시 Valuation과 Payoff Structure

enterprise value waterfall에서 super-priority·working-capital facilities, secured notes, swap termination, restructuring fees와 equity conversion을 순서대로 반영한다. quoted 75~80c와 par exchange를 cash recovery로 혼동하지 않는다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | EBITDA -25%·liquidation | recovery<75c | 미실현 |
| Base | debt-to-equity·new notes | claim 보존 | 실현 |
| Bull | operating recovery·equity upside | 14~15%+ | ledger 불완전 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Purchase | 75~80c | par-near recovery | package 완료 | cash recovery 미확정 |
| Issuer leverage | 약 7x | 대폭 감소 | R15bn+ debt reduction | 강한 성공 |
| Market-price leverage | 약 3.5x | coverage | EV ledger 제한 | 방향 성공 |
| Support | 협상 필요 | >75% | >80% noteholders | 성공 |
| Base return | 14~15% annual | 1~3년 | holder ledger 없음 | 미확정 |

### 촉매와 시간

판정 horizon은 **2011~2013 restructuring**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2010-11-01 | VIC note Long | raw Short 교정 |
| 2011-H1 | restructuring talks | coordination |
| 2011-12-09 | PIC agreement | >80% support |
| 2012 | terms implementation | debt conversion |
| 2012 | swap/interest reset | cash burden 감소 |
| 2013-04-02 | completion 발표 | R15bn+ reduction |
| 2013 | new debt/equity | claim rollover |
| 2026-09-18 | research cutoff | exact holder IRR 미복원 |

### 실제 사업·자본구조 추이

2011 PIC와 80% 초과 senior noteholders가 restructuring을 지지했다. 2013 완료된 package는 debt를 R15bn 이상 줄이고 상당액을 equity로 전환했으며 remaining senior debt를 새로운 notes로 재편했다. Lazard가 noteholders를 자문했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

restructuring headline은 claim preservation을 지지하지만 exact purchase price, accrued coupon, new-note principal/price, equity realization과 dates가 없다. 따라서 14~15% annual return이나 exact recovery percentage를 재구성하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | raw Short | 20% | metadata 실패 | 완전 반대. |
| C2 | senior secured status | 18% | 대체로 성공 | claim influence 확인; exact recovery 제한. |
| C3 | 75~80c recovery asymmetry | 18% | 방향 성공 | cash equivalent 미확정. |
| C4 | deleveraging | 16% | 강한 성공 | 규모·방향 강한 적중. |
| C5 | swap·interest relief | 16% | 성공 방향 | exact swap settlement 미공개. |
| C6 | 14~15% annual return | 12% | 미확정 | IRR 산출 불가. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

secured creditor coordination과 PIC의 going-concern incentive가 liquidation 대신 deleveraging을 만들었다. swap·interest burden 축소와 debt-to-equity conversion이 enterprise continuity를 보존했다.

### Counterfactual

cement EBITDA -25%, collateral value -30%, two-year delay와 super-priority funding을 반영해도 75c purchase가 principal·coupon을 충분히 회수했는가?

---

## 9. 분석 오류 유형과 최초 경고

market-price leverage 3.5x를 recovery coverage처럼 사용했고 collateral perfection·swap priority·new-money priming과 equity exit liquidity를 더 명시적으로 다뤄야 했다.

### 최초로 관찰 가능했던 경고신호

2011 majority support agreement는 촉매 확인이었지만 cash realization이 아니라 restructuring path의 확정일 뿐이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

distressed credit은 회사의 질보다 collateral·priority·recovery를 먼저 본다.

### Lesson 2

par-for-new-paper는 현금 회수가 아니다.

### Lesson 3

swap 제거와 coupon reduction을 restructuring economics에 포함한다.

### Lesson 4

holder별 cash·PIK·equity ledger 없이는 exact IRR을 만들지 않는다.

### 지금 같은 아이디어를 다시 본다면

- CUSIP/note class
- collateral
- senior claims
- coupon/swap
- maturity
- restructuring vote
- cash/equity recovery

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | issuer 정상화 |
| Valuation thesis | 75~80c coverage 지지 |
| Catalyst thesis | restructuring 성공 |
| Security payoff | secured notes 정확 |
| Timing / path | 실현수익 미확정 |
| Thesis score | 8.0/10 |
| Process score | 8.2/10 |
| 종합 | **구조조정 성공 / holder-level IRR 미확정** |

### 한 문장 교훈

> distressed credit은 회사의 질보다 collateral·priority·recovery를 먼저 본다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2010-11-01. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [PIC agreement with AfriSam noteholders](https://cisp.cachefly.net/assets/articles/attachments/36845_public_investment_corporation.pdf) — Public Investment Corporation, 2011-12-09. 80% 초과 noteholder 지지와 R15bn 초과 debt reduction 검증.
3. [AfriSam restructuring completion](https://businessreport.co.za/companies/2013-04-02-afrisam-cuts-debt-by-r15bn/) — AfriSam statement / Business Report, 2013-04-02. R15bn 초과 deleveraging 완료와 ownership change 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·corporate-action payoff만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
