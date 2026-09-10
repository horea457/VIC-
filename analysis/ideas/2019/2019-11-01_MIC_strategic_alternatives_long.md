# Macquarie Infrastructure Corporation — 2019-11-01 — V9

> **Batch 051 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Macquarie Infrastructure Corporation / MIC |
| 실제 Security | **Common / asset-sale distribution claim** |
| Idea ID | `ddc3442c-ff16-4b1d-a92d-216ab9c3a0f7` |
| 게시일 / 작성자 | 2019-11-01 / rii136 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격 | 약 $43 |
| 원 horizon | 약 1년 |
| 최종 판정 | **강한 성공 — 전 자산 매각·분배, clock 지연** |

> **결론:** 2017 dividend compounder를 liquidation으로 재분류했다. 약 $43에서 review와 private storage/FBO multiples로 sale value $52~66, 3Q dividend 포함 1년 25~60%를 봤다. manager의 13m주·$550m 지분과 fee 변화가 sale incentive를 강화했다. 결과적으로 **강한 성공 — 전 자산 매각·분배, clock 지연**.

---

## 1. 회사는 정확히 무엇을 하는가

Macquarie Infrastructure는 IMTT 액체저장터미널, Atlantic Aviation FBO, Hawaii Gas·propane을 보유한 외부운용 holding company였다. 초기 현금엔진은 `자회사 EBITDA-capex-이자·세금-covenant cash trap-holdco cost·manager fee`, 2019년 이후에는 `자산별 sale EV-debt-tax-transaction·manager disposition fee-wind-down cost`다. 장기계약도 utilization·renewal·airport lease와 upstream covenant가 나쁘면 holdco dividend가 끊긴다. payout이 깨진 뒤에도 매각·분배가 확정되면 liquidation claim으로 다시 평가할 수 있다.

### Security cash waterfall

sale EV에서 debt·tax·transaction·manager fee·wind-down을 빼고 실제 분배일 common/LLC cash만 payoff다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

2017 dividend compounder를 liquidation으로 재분류했다. 약 $43에서 review와 private storage/FBO multiples로 sale value $52~66, 3Q dividend 포함 1년 25~60%를 봤다. manager의 13m주·$550m 지분과 fee 변화가 sale incentive를 강화했다.

### Reverse expectations

약 $43가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. review 실행 — 20%

- **원문 주장:** board가 매각한다.
- **T0 근거:** 공식 review·incentives
- **숨은 가정:** buyers 존재
- **사전 반증조건:** 6개월 evidence 부재 시 반증
- **실제:** 세 자산 매각
- **판정:** **강한 성공**
- **재사용 교훈:** 첫 sale이 credibility다.

### C2. IMTT private value — 18%

- **원문 주장:** buyer가 높게 산다.
- **T0 근거:** 10~13x deals
- **숨은 가정:** weakness 일시적
- **사전 반증조건:** bid<floor 시 반증
- **실제:** $2.67bn
- **판정:** **성공**
- **재사용 교훈:** buyer EV로 검증한다.

### C3. IMO uplift — 18%

- **원문 주장:** EBITDA +$38~80m다.
- **T0 근거:** segregation·contango
- **숨은 가정:** 수요 지속
- **사전 반증조건:** utilization 미개선 시 반증
- **실제:** sale에는 비핵심
- **판정:** **부분**
- **재사용 교훈:** theme와 sale floor를 나눈다.

### C4. Atlantic multiple — 16%

- **원문 주장:** 10~12x+다.
- **T0 근거:** Signature·Landmark
- **숨은 가정:** traffic·lease 안정
- **사전 반증조건:** bid<10x 시 반증
- **실제:** $4.475bn
- **판정:** **강한 성공**
- **재사용 교훈:** active auction comp가 강하다.

### C5. proceeds 분배 — 16%

- **원문 주장:** sale cash가 주주에게 온다.
- **T0 근거:** ownership·fee termination
- **숨은 가정:** 재투자 안 함
- **사전 반증조건:** 분배 지연 시 반증
- **실제:** $11+$37.386817+residual
- **판정:** **강한 성공**
- **재사용 교훈:** calendar까지 쓴다.

### C6. 1년 25~60% — 12%

- **원문 주장:** 1년에 완료다.
- **T0 근거:** review
- **숨은 가정:** delay 없음
- **사전 반증조건:** 12개월 미close 시 반증
- **실제:** 전체는 지연
- **판정:** **방향 성공/시간 실패**
- **재사용 교훈:** value와 IRR을 나눈다.

---

## 4. 당시 Valuation과 Payoff Structure

asset EBITDA×transaction multiple에서 debt·tax·1% cost·disposition fee를 뺀다. no-sale mid-$40s, Atlantic 10~12x+, storage 10~13x, IMTT 2020 uplift $38~80m였다. 9.5% dividend는 sale 전 carry다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 강한 성공 — 전 자산 매각·분배, clock 지연의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry/sale | $43 | $52~66 | asset sales | 강한 성공 |
| Yield | 9.5% | 3Q carry | liquidation 전환 | 부분 |
| IMTT sale | public discount | private | $2.67bn | 성공 |
| IMTT distribution | 없음 | cash | $11 | 성공 |
| Atlantic distribution | SOTP | private | $37.386817 | 강한 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2018-02 | cut | compounder 붕괴 |
| 2019-10 | review | event |
| 2019-11-01 | VIC Long | $43 |
| 2020-11 | IMTT deal | $2.67bn |
| 2020-12 | close | cash |
| 2021-01 | $11 | 분배 |
| 2021-06 | Atlantic deal | $4.475bn |
| 2021-09 | $37.386817 | payoff |
| 2022 | Hawaii | 종결 |

### 실제 사업·자본구조

IMTT를 약 $2.67bn에 팔아 $11/share를 지급했고 Atlantic을 $4.475bn에 팔아 $37.386817/unit을 분배했다. Hawaii도 후속 매각됐지만 전체 clock은 1년보다 길었다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

$11+$37.386817만 $48.386817이지만 ex-date price·일반배당·LLC·tax series가 없어 exact IRR은 null이다.

첨부·repository에 정확한 performance row가 없다. 기업·사건 결과와 security total return을 분리하며 배당·청산분배·successor shares를 날짜별로 복원하기 전 return과 IRR은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | review 실행 | 20% | 강한 성공 | 첫 sale이 credibility다. |
| C2 | IMTT private value | 18% | 성공 | buyer EV로 검증한다. |
| C3 | IMO uplift | 18% | 부분 | theme와 sale floor를 나눈다. |
| C4 | Atlantic multiple | 16% | 강한 성공 | active auction comp가 강하다. |
| C5 | proceeds 분배 | 16% | 강한 성공 | calendar까지 쓴다. |
| C6 | 1년 25~60% | 12% | 방향 성공/시간 실패 | value와 IRR을 나눈다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

buyer universe와 board/manager incentive, asset별 sale이 public discount를 현금으로 바꿨다. IMO uplift가 완전히 맞을 필요도 없었다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 약 $43에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

모든 sale을 1년에 압축했고 IMO uplift·regular dividend를 낙관했다. tax basis·fee sensitivity가 더 필요했다.

### 최초 관찰 가능한 경고/반증

6개월 내 banker·buyer evidence 부재 또는 after-tax floor<$44·dividend cut이면 1년 IRR을 철회한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `MIC`와 날짜를 Macquarie Infrastructure Corporation의 실제 법인·security에 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Long을 확정한다.
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
| Entity / direction | raw Short → **Long**, Macquarie Infrastructure Corporation |
| Business thesis | 성공 |
| Valuation thesis | 강한 성공 |
| Catalyst / timing | 강한 성공 — 전 자산 매각·분배, clock 지연 |
| Thesis score | 9.0/10 |
| Process score | 9.1/10 |
| Outcome-adjusted score | 9.1/10 |

### 한 문장 교훈

> 첫 sale이 credibility다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL 원문·metadata — VIC_IDEAS(4).sql / VIC, 2019-11-01. idea_id·raw direction·description 19676 chars·catalyst 175 chars
2. [MIC SEC archive](https://www.sec.gov/edgar/browse/?CIK=1289790&owner=exclude) — SEC / MIC, 2004-2021. segment FCF·covenant·distribution·asset sale
3. [IMTT sale / $11 dividend](https://www.sec.gov/Archives/edgar/data/1289790/000115752320001625/a52353418ex99_1.htm) — SEC / MIC, 2020-12-23. $2.67bn close와 $11/share
4. [Atlantic close / distribution](https://www.sec.gov/Archives/edgar/data/1845290/000110465921118596/tm2128286d1_ex99-1.htm) — SEC / MIC LLC, 2021-09-23. $4.475bn close와 $37.386817/unit
5. [IMTT operations](https://imtt.com/) — IMTT, 2026. 40m barrels 북미 bulk-liquid storage

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=MIC, entity=Macquarie Infrastructure Corporation, raw=Short, research=Long.
