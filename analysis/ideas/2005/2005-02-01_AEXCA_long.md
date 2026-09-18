# Ampex Corporation (AEXCA) — 2005-02-01 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Ampex Corporation / AEXCA |
| VIC 게시일 / 작성자 | 2005-02-01 / gearl1818 |
| 분석 증권 / 실제 방향 | Ampex Class A common / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 2005 common |
| 기대기간 | 2014 patent cash-flow window |
| raw horizon audit | minimum EPS ~$6.25 through 2014 from royalty+storage |
| 최종 판정 | **강한 실패 — royalty를 common annuity로 오인** |

> **결론:** digital-imaging royalty의 높은 margin은 맞았지만 legacy storage 손실·debt·patent duration이 common 현금을 흡수했다. 2008 Chapter 11 plan에서 existing Class A common은 취소됐고 distribution은 없었다. CPR은 별도 contingent claim이다.

---

## 1. 회사는 정확히 무엇을 하는가

Ampex는 data-storage 장비와 digital-imaging 특허 licensing으로 수익을 냈다. 특허 royalty는 높은 incremental margin을 가질 수 있지만 만기·소송·licensee volume에 따라 흔들리고, legacy storage의 손실과 debt service가 먼저 현금을 흡수한다. common은 모든 고정청구권 뒤의 잔여다.

royalty receipts + storage gross profit - litigation/R&D/SG&A - interest - capex = residual cash; patent expiry와 debt waterfall을 common 가치에 적용한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

royalty revenue, license concentration, patent life, storage gross margin, operating cash burn, interest, liquidity, net debt, restructuring priority

---

## 2. 당시 상황과 시장이 가격에 넣은 것

원문은 licensing stream과 storage turnaround를 합쳐 최소 EPS 약 $6.25가 2014까지 지속될 것으로 봤다. 특허가치를 common per-share annuity처럼 평가했다.

### Reverse expectations

시장은 royalty concentration·patent expiry/litigation, legacy cash burn, leverage와 small-cap governance를 할인했다.

---

## 3. 원문 투자논지 지도

### C1. EPS ~$6.25 — 강한 실패

**원문 주장**

최소 EPS $6.25.

**경제적 메커니즘**

royalty+storage earnings.

**T0 근거**

license economics.

**숨은 가정**

cash royalty 지속·loss 축소.

**사전 반증조건**

EPS/FCF가 크게 미달하면 반증.

**실제 결과**

파산·common 취소.

**정량 gap**

terminal 0.

**분석 오류 또는 제한**

gross royalty를 EPS로 직결.

**재사용 교훈**

cash-to-common bridge가 필요하다.

### C2. royalty annuity through 2014 — 실패

**원문 주장**

특허 cash가 장기간 지속.

**경제적 메커니즘**

licenses·settlements.

**T0 근거**

patent portfolio.

**숨은 가정**

expiry·challenge 제한.

**사전 반증조건**

royalty 하락·소송비 증가면 반증.

**실제 결과**

common까지 지속되지 않음.

**정량 gap**

duration 부족.

**분석 오류 또는 제한**

유한 특허를 perpetuity처럼 봄.

**재사용 교훈**

license별 expiry와 net cash를 본다.

### C3. storage turnaround — 실패

**원문 주장**

legacy storage가 흑자 전환.

**경제적 메커니즘**

cost cuts·product demand.

**T0 근거**

installed base.

**숨은 가정**

매출·margin 회복.

**사전 반증조건**

반복 operating loss면 반증.

**실제 결과**

cash drain 지속.

**정량 gap**

common FCF 악화.

**분석 오류 또는 제한**

optional upside를 base에 포함.

**재사용 교훈**

loss business는 0이 아니라 closure cost를 둔다.

### C4. deleveraging — 실패

**원문 주장**

royalty로 debt를 줄인다.

**경제적 메커니즘**

cash sweep이 interest를 낮춤.

**T0 근거**

high-margin receipts.

**숨은 가정**

burn보다 royalty 큼.

**사전 반증조건**

liquidity stress면 반증.

**실제 결과**

Chapter 11.

**정량 gap**

완전 반대.

**분석 오류 또는 제한**

cash gross와 net 혼동.

**재사용 교훈**

sources/uses waterfall을 분기별로 만든다.

### C5. common retains IP value — 강한 실패

**원문 주장**

특허가 common floor.

**경제적 메커니즘**

sale/reorg 잔여가치.

**T0 근거**

IP asset.

**숨은 가정**

claims보다 value 큼.

**사전 반증조건**

common cancellation이면 반증.

**실제 결과**

취소/no distribution.

**정량 gap**

recovery 0.

**분석 오류 또는 제한**

EV와 equity 혼동.

**재사용 교훈**

senior claims 뒤 recovery를 계산한다.

### C6. CPR as recovery — 분리 필요

**원문 주장**

후속권리가 주주가치 보완.

**경제적 메커니즘**

threshold 이후 contingent payment.

**T0 근거**

plan terms.

**숨은 가정**

threshold 달성·old holder entitlement.

**사전 반증조건**

무조건 common recovery로 보면 오류.

**실제 결과**

약 $83.8m threshold의 별도 CPR.

**정량 gap**

즉시 common 분배 0.

**분석 오류 또는 제한**

다른 security를 합산.

**재사용 교훈**

CPR을 독립 option으로 평가한다.

---

## 4. 당시 Valuation과 Payoff Structure

$6.25 minimum EPS×multiple 접근은 royalty의 유한수명과 debt priority, storage losses를 충분히 haircut하지 않았다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | royalty decline+storage burn | restructuring/common 0 | 현실화 |
| Base | EPS $6.25 지속 | 큰 upside | 실패 |
| Bull | new licenses+debt paydown | 2014 annuity | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Minimum EPS | ~$6.25 | through 2014 | 지속되지 않음 | 강한 실패 |
| Royalty duration | 2014 | 현금 annuity | patent/litigation risk | 과대 |
| Legacy storage | turnaround | 흑자 | cash drain | 실패 |
| Chapter 11 | 배제 | 없음 | 2008 | terminal 반증 |
| Old common | 가치 보존 | distribution | 취소/no distribution | 0 |

### 촉매와 시간

판정 horizon은 **2014 patent cash-flow window**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2005-02-01 | VIC Long | IP annuity thesis |
| 2005 | royalty receipts | headline strength |
| 2006 | legacy losses | cash conversion 약화 |
| 2007 | liquidity pressure | first break |
| 2008-03-30 | Chapter 11 | capital structure 실패 |
| 2008-08-06 | plan disclosure | old common treatment |
| 2008 | common cancellation | terminal 0 |
| 후속 | CPR 별도 | common recovery 아님 |

### 실제 사업·자본구조 추이

영업·자본구조 압력이 이어져 2008 Chapter 11. SEC 공시상 old common, options와 restricted shares는 취소되고 분배가 없었다. CPR은 약 $83.8m threshold 이후 조건부로 설계돼 common 보존과 다르다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

old Class A common terminal payoff는 0이다. CPR을 common recovery로 합산하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | EPS ~$6.25 | 20% | 강한 실패 | terminal 0. |
| C2 | royalty annuity through 2014 | 18% | 실패 | duration 부족. |
| C3 | storage turnaround | 18% | 실패 | common FCF 악화. |
| C4 | deleveraging | 16% | 실패 | 완전 반대. |
| C5 | common retains IP value | 16% | 강한 실패 | recovery 0. |
| C6 | CPR as recovery | 12% | 분리 필요 | 즉시 common 분배 0. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

loss는 특허자산 자체보다 그 cash flow가 debt·legacy burn·restructuring priority 뒤 common까지 도달하지 않은 데서 났다.

### Counterfactual

royalty가 50% 감소하고 storage가 계속 손실이어도 debt service 뒤 common FCF가 양수였는가?

---

## 9. 분석 오류 유형과 최초 경고

gross royalty를 durable per-share earnings로 자본화하고 claim priority와 patent duration을 누락했다.

### 최초로 관찰 가능했던 경고신호

cash burn과 debt pressure가 royalty cash를 상쇄한 시점이 첫 경고였고 2008 filing이 terminal break였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

특허 royalty는 만기·소송·licensee volume을 반영한 declining asset로 본다.

### Lesson 2

높은-margin revenue와 common FCF를 혼동하지 않는다.

### Lesson 3

CPR은 old common 보존과 별도 청구권이다.

### Lesson 4

legacy business와 debt가 royalty cash를 먼저 흡수하는지 본다.

### 지금 같은 아이디어를 다시 본다면

- patent expiry
- license concentration
- cash royalty
- legacy burn
- interest
- liquidity
- priority waterfall

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 실패 |
| Valuation thesis | 강한 실패 |
| Catalyst thesis | deleveraging 실패 |
| Security payoff | common 0 |
| Timing / path | 2008 terminal |
| Thesis score | 2.2/10 |
| Process score | 2.5/10 |
| 종합 | **강한 실패 — royalty를 common annuity로 오인** |

### 한 문장 교훈

> 특허 royalty는 만기·소송·licensee volume을 반영한 declining asset로 본다.

---

## 12. Sources / Validation Notes

1. [VIC source-DB preserved original](https://www.valueinvestorsclub.com/idea/Ampex_Corporation/6253988944) — Value Investors Club / source SQL, 2005-02-01. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [Ampex 2008 Form 10-Q](https://www.sec.gov/Archives/edgar/data/887433/000119312508178320/d10q.htm) — SEC / Ampex, 2008-08-18. Chapter 11 plan, old common cancellation, contingent payment rights의 별도 취급 검증.
3. [Ampex Chapter 11 8-K](https://www.sec.gov/Archives/edgar/data/887433/000119312508168066/d8k.htm) — SEC / Ampex, 2008-08-06. restructuring 절차와 capital-structure outcome 검증.
4. [Ampex SEC issuer archive](https://www.sec.gov/edgar/browse/?CIK=887433&owner=exclude) — SEC, 2005-2008. royalty·storage·debt 공시 교차검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported high/period-end price만 사용; exact total-return ledger가 없으면 IRR·MFE를 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
