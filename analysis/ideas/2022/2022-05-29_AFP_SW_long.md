# Aluflexpack AG (AFP SW) — 2022-05-29 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Aluflexpack AG / AFP SW |
| VIC 게시일 / 작성자 | 2022-05-29 / MrTwister |
| 분석 증권 / 실제 방향 | Aluflexpack registered shares / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 2022 depressed Swiss-listed valuation; exact entry ledger unavailable |
| 기대기간 | 2022~2025 capacity ramp·margin normalization |
| raw horizon audit | 2025 revenue €425m, EBITDA margin 14%, EBITDA 약 €59.5m |
| 최종 판정 | **운영 성공 / security outcome 혼합 — 2025 CHF16 takeout** |

> **결론:** 2023 revenue €380.3m와 EBITDA 약 €51m은 2025 목표 €425m·€59.5m에 상당히 접근해 operating thesis를 지지했다. 그러나 Constantia의 최종 CHF16/share acquisition·delisting이 각 투자자의 충분한 return이었는지는 T0 entry와 배당 ledger 없이는 단정할 수 없다. 사업 예측 성공과 security payoff를 분리한다.

---

## 1. 회사는 정확히 무엇을 하는가

Aluflexpack은 식품·pet food·pharma용 aluminum·flexible packaging을 생산했다. volume·price/mix에서 aluminum·energy·labour와 conversion cost를 빼고, 신규 capacity ramp와 working capital·capex를 반영한 현금이 equity에 귀속된다.

volume × price/mix - aluminum·energy·labour - plant overhead - SG&A - tax - capex ± working capital = equity FCF; ramp utilization과 acquisition consideration을 분리한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

volume, price/mix, aluminum pass-through, EBITDA margin, utilization, expansion capex, working capital, leverage, bid price

---

## 2. 당시 상황과 시장이 가격에 넣은 것

aluminum·energy inflation과 expansion capex가 earnings를 눌러 valuation이 낮았지만, defensive end markets, pass-through와 new capacity ramp로 2025 revenue €425m·14% EBITDA margin·약 €59.5m EBITDA를 달성한다는 논지였다.

### Reverse expectations

시장은 raw-material pass-through lag, capex overrun, utilization ramp, working-capital funding과 controlling-shareholder/low-liquidity discount를 반영했다. 성장 capex가 revenue는 늘려도 FCF/share를 만들지 못할 수 있었다.

---

## 3. 원문 투자논지 지도

### C1. revenue €425m — 대체로 성공

**원문 주장**

2025 revenue €425m.

**경제적 메커니즘**

capacity·volume·price/mix가 sales를 늘린다.

**T0 근거**

expansion plan과 defensive demand.

**숨은 가정**

ramp·pass-through가 작동.

**사전 반증조건**

€350m 아래면 실패.

**실제 결과**

2023 €380.3m.

**정량 gap**

목표의 89.5%를 2년 전 달성.

**분석 오류 또는 제한**

price inflation과 real volume 혼용.

**재사용 교훈**

volume·price·FX bridge를 만든다.

### C2. EBITDA margin 14% — 대체로 성공

**원문 주장**

scale·pass-through로 14% margin.

**경제적 메커니즘**

utilization과 price recovery가 input cost를 상쇄.

**T0 근거**

historical margin·contracts.

**숨은 가정**

원재료 lag와 ramp cost 축소.

**사전 반증조건**

12% 미만 지속이면 실패.

**실제 결과**

2023 약 13.4%.

**정량 gap**

-0.6ppt.

**분석 오류 또는 제한**

adjusted EBITDA definition risk.

**재사용 교훈**

reported·adjusted bridge를 고정한다.

### C3. EBITDA €59.5m — 대체로 성공

**원문 주장**

2025 약 €59.5m.

**경제적 메커니즘**

€425m×14%.

**T0 근거**

explicit target.

**숨은 가정**

revenue·margin 동시 달성.

**사전 반증조건**

€45m 미만이면 실패.

**실제 결과**

2023 약 €51m.

**정량 gap**

-€8.5m/-14.3% two years early.

**분석 오류 또는 제한**

point target 과신.

**재사용 교훈**

range와 date를 같이 판정한다.

### C4. capacity expansion — 성공

**원문 주장**

new capacity가 demand를 수용한다.

**경제적 메커니즘**

installed lines가 volume·mix를 높인다.

**T0 근거**

announced capex.

**숨은 가정**

customer qualification·utilization 확보.

**사전 반증조건**

low utilization·cash burn이면 실패.

**실제 결과**

revenue·EBITDA scale-up 확인.

**정량 gap**

방향 성공.

**분석 오류 또는 제한**

capex return를 EBITDA로만 평가.

**재사용 교훈**

incremental ROIC·cash payback을 본다.

### C5. inflation reversal — 부분 성공

**원문 주장**

commodity inflation 완화가 margin을 회복한다.

**경제적 메커니즘**

aluminum·energy cost와 pass-through lag가 줄어든다.

**T0 근거**

2022 inflation spike.

**숨은 가정**

selling price stickiness 유지.

**사전 반증조건**

cost 재상승·price reset이면 실패.

**실제 결과**

margin이 13%대로 회복.

**정량 gap**

결과 지지·driver attribution 제한.

**분석 오류 또는 제한**

macro timing 의존.

**재사용 교훈**

contract별 pass-through lag를 추적한다.

### C6. equity rerating — 혼합

**원문 주장**

operating delivery가 depressed stock을 재평가한다.

**경제적 메커니즘**

higher EBITDA와 strategic interest가 equity value를 높인다.

**T0 근거**

low valuation.

**숨은 가정**

debt·control discount가 제한하지 않는다.

**사전 반증조건**

offer가 intrinsic value 아래면 미달.

**실제 결과**

CHF16 cash exit.

**정량 gap**

entry 미복원으로 payoff 판정 제한.

**분석 오류 또는 제한**

business success=stock success 등치.

**재사용 교훈**

entry·FX·dividend·offer를 별도 ledger화한다.

---

## 4. 당시 Valuation과 Payoff Structure

2025 €59.5m EBITDA target에는 net debt·minority·maintenance capex를 연결해야 한다. terminal CHF16 cash offer는 operating forecast 검증과 별개이며, entry price·FX·dividends가 없으면 realized return을 계산하지 않는다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | inflation·ramp miss | margin<10%·debt | 미실현 |
| Base | €425m·14% | €59.5m EBITDA | 근접 |
| Bull | strategic premium | cash exit | CHF16 실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2025 revenue | €425m | €425m | 2023 €380.3m | 목표의 89.5% two years early |
| EBITDA margin | 14% | 14% | 2023 약 13.4% | 근접 |
| EBITDA | €59.5m | €59.5m | 2023 약 €51m | 85.7% |
| Capacity | expansion | ramp | operating scale 증가 | 성공 |
| Terminal price | upside | rerating | CHF16 cash | entry 없어 혼합 |

### 촉매와 시간

판정 horizon은 **2022~2025 capacity ramp·margin normalization**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2022-05-29 | VIC Long | 2025 targets |
| 2022-H2 | inflation/pass-through | margin test |
| 2023 | revenue €380.3m | trajectory 확인 |
| 2023 | EBITDA ~€51m | margin 근접 |
| 2024 | Constantia transaction | control event |
| 2025-03-04 | join-forces announcement | completion |
| 2025 | final CHF16 offer | terminal cash |
| 2025 | delisting | public-equity 종료 |

### 실제 사업·자본구조 추이

FY2023 revenue는 €380.3m, EBITDA는 약 €51m으로 target trajectory에 접근했다. Constantia Flexibles가 지배권을 취득하고 최종 offer CHF16/share로 2025 거래·delisting이 진행됐다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

terminal cash consideration CHF16/share는 검증했다. 그러나 source catalog에 exact entry·purchase date·dividend·FX ledger가 없으므로 price gain·total return·IRR은 제시하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | revenue €425m | 20% | 대체로 성공 | 목표의 89.5%를 2년 전 달성. |
| C2 | EBITDA margin 14% | 18% | 대체로 성공 | -0.6ppt. |
| C3 | EBITDA €59.5m | 18% | 대체로 성공 | -€8.5m/-14.3% two years early. |
| C4 | capacity expansion | 16% | 성공 | 방향 성공. |
| C5 | inflation reversal | 16% | 부분 성공 | 결과 지지·driver attribution 제한. |
| C6 | equity rerating | 12% | 혼합 | entry 미복원으로 payoff 판정 제한. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

volume·pricing과 capacity ramp가 EBITDA를 키웠고 strategic buyer가 platform value를 인정했다. 다만 control transaction price가 minority investor의 원래 upside를 얼마나 실현했는지는 entry별로 다르다.

### Counterfactual

volume ramp 2년 지연, aluminum pass-through 6개월 lag와 working-capital peak를 넣어도 equity가 추가 debt 없이 2025까지 버틸 수 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

EBITDA target를 equity payoff와 가깝게 봤고 expansion capex·working capital·control shareholder가 terminal multiple을 제한할 가능성을 덜 반영했다.

### 최초로 관찰 가능했던 경고신호

takeover terms가 CHF16으로 정해진 시점은 운영 thesis의 상단과 minority payoff가 달라질 수 있음을 보여준 최초의 security-level 신호였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

operating target 적중과 주식 payoff 적중을 분리한다.

### Lesson 2

capacity expansion은 utilization·working capital·leverage를 함께 본다.

### Lesson 3

원재료 pass-through의 시차가 EBITDA와 cash를 다르게 움직인다.

### Lesson 4

cash offer는 entry price와 interim dividends가 있어야 total return이 된다.

### 지금 같은 아이디어를 다시 본다면

- volume
- pass-through
- EBITDA margin
- utilization
- capex
- working capital
- leverage
- offer terms

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 운영 성공 |
| Valuation thesis | entry 없어 혼합 |
| Catalyst thesis | capacity·takeout 실현 |
| Security payoff | common 적절·control risk |
| Timing / path | 2025 종료 |
| Thesis score | 6.8/10 |
| Process score | 7.8/10 |
| 종합 | **운영 성공 / security outcome 혼합 — 2025 CHF16 takeout** |

### 한 문장 교훈

> operating target 적중과 주식 payoff 적중을 분리한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/Aluflexpack/3093562527) — Value Investors Club / source SQL, 2022-05-29. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Aluflexpack 2023 annual report](https://www.aluflexpack.com/investors/reports-presentations/) — Aluflexpack, 2024. 2023 revenue €380.3m와 EBITDA 약 €51m 검증.
3. [Constantia and Aluflexpack join forces](https://www.cflex.com/) — Constantia Flexibles, 2025-03-04. 거래 completion·지배권 이전의 공식 발표 검증.
4. [EU merger case archive](https://competition-cases.ec.europa.eu/) — European Commission, 2025. Constantia/Aluflexpack 기업결합 절차 교차검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·corporate-action payoff만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
