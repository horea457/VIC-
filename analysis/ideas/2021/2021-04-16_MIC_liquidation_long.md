# Macquarie Infrastructure Corporation / MIC LLC — 2021-04-16 — V9

> **Batch 051 canonical report.** Raw SQL `Long`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Macquarie Infrastructure Corporation / MIC LLC / MIC |
| 실제 Security | **Common→LLC units / liquidation distributions** |
| Idea ID | `770d0a70-f908-4b5d-a0fd-4ad0b2eb76a6` |
| 게시일 / 작성자 | 2021-04-16 / althea |
| 원 SQL 방향 | Long |
| 원문 검증 방향 | **Long** |
| 기준가격 | 약 $3.7bn EV |
| 원 horizon | Atlantic 6개월·Hawaii 12개월+ |
| 최종 판정 | **매우 성공 — 52일 내 $4.475bn deal·$37.386817 분배** |

> **결론:** IMTT sale 뒤 Atlantic·Hawaii만 남았다. Signature $5.58bn auction을 active comp로 Atlantic 14.5x 2019 EBITDA, Hawaii $540m/9x로 평가했고 LLC 전환이 Atlantic-first tax-efficient sale을 가능하게 해 6개월 catalyst를 예상했다. 결과적으로 **매우 성공 — 52일 내 $4.475bn deal·$37.386817 분배**.

---

## 1. 회사는 정확히 무엇을 하는가

Macquarie Infrastructure는 IMTT 액체저장터미널, Atlantic Aviation FBO, Hawaii Gas·propane을 보유한 외부운용 holding company였다. 초기 현금엔진은 `자회사 EBITDA-capex-이자·세금-covenant cash trap-holdco cost·manager fee`, 2019년 이후에는 `자산별 sale EV-debt-tax-transaction·manager disposition fee-wind-down cost`다. 장기계약도 utilization·renewal·airport lease와 upstream covenant가 나쁘면 holdco dividend가 끊긴다. payout이 깨진 뒤에도 매각·분배가 확정되면 liquidation claim으로 다시 평가할 수 있다.

### Security cash waterfall

sale EV에서 debt·tax·1% cost·manager fee·$10m wind-down을 빼고 분배일별 unit cash를 기록한다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

IMTT sale 뒤 Atlantic·Hawaii만 남았다. Signature $5.58bn auction을 active comp로 Atlantic 14.5x 2019 EBITDA, Hawaii $540m/9x로 평가했고 LLC 전환이 Atlantic-first tax-efficient sale을 가능하게 해 6개월 catalyst를 예상했다.

### Reverse expectations

약 $3.7bn EV가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. 6개월 sale — 20%

- **원문 주장:** agreement가 6개월 내다.
- **T0 근거:** 첫 sale·LLC·auction
- **숨은 가정:** diligence 준비
- **사전 반증조건:** 2021-10 미발표 시 반증
- **실제:** 52일
- **판정:** **매우 성공**
- **재사용 교훈:** deadline을 둔다.

### C2. 14.5x value — 18%

- **원문 주장:** Signature보다 소폭 할인이다.
- **T0 근거:** 14.6x/15.9x comp
- **숨은 가정:** scale discount 상쇄
- **사전 반증조건:** bid<12.5x 시 반증
- **실제:** $4.475bn
- **판정:** **성공**
- **재사용 교훈:** metric을 맞춘다.

### C3. durable FBO — 18%

- **원문 주장:** long lease·hangar·low capex다.
- **T0 근거:** 2007~20 positive FCF
- **숨은 가정:** traffic 회복
- **사전 반증조건:** GP·tenure 급락 시 반증
- **실제:** buyer가 인정
- **판정:** **성공**
- **재사용 교훈:** gallons보다 GP·lease다.

### C4. LLC tax — 16%

- **원문 주장:** Atlantic-first tax를 낮춘다.
- **T0 근거:** reorganization
- **숨은 가정:** vote·opinion 통과
- **사전 반증조건:** 큰 leakage 시 반증
- **실제:** 실행
- **판정:** **성공**
- **재사용 교훈:** tax도 core claim이다.

### C5. Hawaii — 16%

- **원문 주장:** 9x/$540m다.
- **T0 근거:** utility·propane
- **숨은 가정:** tourism·PUC
- **사전 반증조건:** 6x 이하 시 반증
- **실제:** 후속 sale
- **판정:** **성공**
- **재사용 교훈:** residual duration을 나눈다.

### C6. downside — 12%

- **원문 주장:** no-sale $26다.
- **T0 근거:** 10.5x/6x implied
- **숨은 가정:** FCF 유지
- **사전 반증조건:** 구조하락 시 반증
- **실제:** sale로 미시험
- **판정:** **미발생**
- **재사용 교훈:** failed-sale gap도 둔다.

---

## 4. 당시 Valuation과 Payoff Structure

Atlantic base 14.5x EBITDA/15.4x EBITDA-maintenance capex, bear 12.5x/13.3x. Hawaii $540m/9x에서 1% cost+$10m wind-down+manager fee를 차감했다. no-sale $26은 Atlantic 10.5x·Hawaii 6x다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 매우 성공 — 52일 내 $4.475bn deal·$37.386817 분배의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Catalyst | 6개월 | sale | 52일 | 매우 성공 |
| Multiple | 14.5x | Signature 할인 | $4.475bn | 성공 |
| Distribution | 미정 | 대규모 | $37.386817 | 강한 성공 |
| Hawaii | $540m/9x | 12개월+ | 후속 sale | 성공 |
| Costs | 1%+$10m+fee | 차감 | proceeds 반영 | 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2020-11 | IMTT deal | credibility |
| 2021-01 | $11 | payout |
| 2021-02 | Signature $5.58bn | comp |
| 2021-04-16 | VIC Long | clock |
| 2021-06-07 | $4.475bn | 52일 |
| 2021-09-23 | close | cash |
| 2021-10 | $37.386817 | payoff |
| 2022 | Hawaii | residual |

### 실제 사업·자본구조

게시 52일 뒤 2021-06-07 KKR $4.475bn sale이 발표되고 9월 close 뒤 $37.386817/unit이 분배됐다. Hawaii는 더 오래 걸렸다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

공식 분배는 확인되지만 entry·IMTT basis·Hawaii final cash가 연결되지 않아 exact IRR은 null이다.

첨부·repository에 정확한 performance row가 없다. 기업·사건 결과와 security total return을 분리하며 배당·청산분배·successor shares를 날짜별로 복원하기 전 return과 IRR은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | 6개월 sale | 20% | 매우 성공 | deadline을 둔다. |
| C2 | 14.5x value | 18% | 성공 | metric을 맞춘다. |
| C3 | durable FBO | 18% | 성공 | gallons보다 GP·lease다. |
| C4 | LLC tax | 16% | 성공 | tax도 core claim이다. |
| C5 | Hawaii | 16% | 성공 | residual duration을 나눈다. |
| C6 | downside | 12% | 미발생 | failed-sale gap도 둔다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

첫 sale·분배라는 revealed preference, Signature bidding war, LLC tax 구조와 Atlantic의 69개 base·long leases·hangar·low capex가 edge였다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 약 $3.7bn EV에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

Hawaii regulatory/tax와 Atlantic 14.5x downside probability를 더 넓게 봐야 했다.

### 최초 관찰 가능한 경고/반증

2021-10 무agreement·LLC tax 지연·bid<12.5x면 핵심 IRR을 폐기한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `MIC`와 날짜를 Macquarie Infrastructure Corporation / MIC LLC의 실제 법인·security에 고정한다.
2. **Direction audit:** raw Long가 아니라 원문 payoff를 읽어 Long을 확정한다.
3. **Bridge:** target을 EPS/book/NAV와 cash waterfall로 연결한다.
4. **Falsifier:** 최초 경고에 날짜와 수치를 둔다.
5. **Path:** 원 horizon과 terminal event를 섞지 않는다.
6. **Missing data:** SQL performance가 없으면 null을 유지한다.

### 다시 분석한다면

- legal/capital/funding gate를 확률·날짜별로 나눈다.
- gross asset value와 common에 귀속되는 순가치를 분리한다.
- base/bull target뿐 아니라 survival/recovery case를 수치화한다.
- corporate action 이후 교환비율·배당·successor price를 연결해 total return을 복원한다.
- event가 맞아도 price target이 실패할 수 있도록 exit/cover rule을 미리 쓴다.

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Entity / direction | raw Long → **Long**, Macquarie Infrastructure Corporation / MIC LLC |
| Business thesis | 성공 |
| Valuation thesis | 매우 성공 |
| Catalyst / timing | 매우 성공 — 52일 내 $4.475bn deal·$37.386817 분배 |
| Thesis score | 9.7/10 |
| Process score | 9.5/10 |
| Outcome-adjusted score | 9.6/10 |

### 한 문장 교훈

> deadline을 둔다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문·metadata](https://www.valueinvestorsclub.com/idea/MACQUARIE_INFRASTRUCTURE_CP/9439712255) — VIC_IDEAS(4).sql / VIC, 2021-04-16. idea_id·raw direction·description 20001 chars·catalyst 59 chars
2. [MIC SEC archive](https://www.sec.gov/edgar/browse/?CIK=1289790&owner=exclude) — SEC / MIC, 2004-2021. segment FCF·covenant·distribution·asset sale
3. [IMTT sale / $11 dividend](https://www.sec.gov/Archives/edgar/data/1289790/000115752320001625/a52353418ex99_1.htm) — SEC / MIC, 2020-12-23. $2.67bn close와 $11/share
4. [Atlantic close / distribution](https://www.sec.gov/Archives/edgar/data/1845290/000110465921118596/tm2128286d1_ex99-1.htm) — SEC / MIC LLC, 2021-09-23. $4.475bn close와 $37.386817/unit
5. [IMTT operations](https://imtt.com/) — IMTT, 2026. 40m barrels 북미 bulk-liquid storage

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=MIC, entity=Macquarie Infrastructure Corporation / MIC LLC, raw=Long, research=Long.
