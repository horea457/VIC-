# Genworth MI Canada Inc. (현 Sagen MI Canada Inc.) — 2009-12-29 — V9

> **Batch 051 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Genworth MI Canada Inc. (현 Sagen MI Canada Inc.) / MIC |
| 실제 Security | **Common equity** |
| Idea ID | `3b9202d5-f12b-4285-940b-b2ed2ae59efe` |
| 게시일 / 작성자 | 2009-12-29 / xanadu972 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격 | C$24 부근 |
| 원 horizon | 4~5년 |
| 최종 판정 | **장기 강한 성공 — C$48.86 control transaction** |

> **결론:** raw Short지만 명백한 Long이며 미국 Macquarie가 아니라 TSX Genworth MI Canada다. 미국식 non-recourse 직관을 캐나다에 투영한 housing fear 속에서 recourse·은행 underwriting·시장집중, 높은 premium·낮은 loss ratio와 excess capital이 20%+ book compounding을 만들고 C$24에서 40%+ upside가 있다고 봤다. 결과적으로 **장기 강한 성공 — C$48.86 control transaction**.

---

## 1. 회사는 정확히 무엇을 하는가

Genworth MI Canada(현 Sagen)는 캐나다 주택담보대출기관에 borrower-default 보험을 제공한다. 현금엔진은 `insured mortgage volume×premium rate+투자수익-발생손해-loss adjustment expense-운영비-세금-필요자본 증가`다. 보험료는 upfront, claim은 경기후퇴 뒤 늦게 나오므로 당기 ROE만 보면 tail을 놓친다. recourse·은행 underwriting, LTV·credit score·지역·vintage, cure·foreclosure severity, 정부보증과 OSFI capital이 loss ratio와 배당가능자본을 결정한다.

### Security cash waterfall

영업현금에서 capex·이자·세금·manager/holdco 비용과 선순위 부채를 차감한 뒤 common에 남는 현금만 가치다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw Short지만 명백한 Long이며 미국 Macquarie가 아니라 TSX Genworth MI Canada다. 미국식 non-recourse 직관을 캐나다에 투영한 housing fear 속에서 recourse·은행 underwriting·시장집중, 높은 premium·낮은 loss ratio와 excess capital이 20%+ book compounding을 만들고 C$24에서 40%+ upside가 있다고 봤다.

### Reverse expectations

C$24 부근가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. 캐나다 계약구조 — 20%

- **원문 주장:** recourse·은행심사가 미국식 손실을 막는다.
- **T0 근거:** lender가 insurer 선택·high-ratio 심사
- **숨은 가정:** incentive가 stress에도 작동
- **사전 반증조건:** vintage severity 급등 시 반증
- **실제:** loss economics 견고
- **판정:** **성공**
- **재사용 교훈:** 국가가 아니라 계약·claim waterfall을 비교한다.

### C2. 시장집중·pricing — 18%

- **원문 주장:** 집중시장이 높은 ROE를 지킨다.
- **T0 근거:** 진입규제·lender integration
- **숨은 가정:** 가격경쟁 제한
- **사전 반증조건:** rate·share 동시하락 시 반증
- **실제:** largest private insurer 유지
- **판정:** **성공**
- **재사용 교훈:** price·share·capital로 검증한다.

### C3. 20%+ book 복리 — 18%

- **원문 주장:** 보험이익·float가 book/share를 키운다.
- **T0 근거:** 높은 ROE·낮은 payout
- **숨은 가정:** loss·capital 안정
- **사전 반증조건:** 2년 CAGR<15%면 반증
- **실제:** 장기 가치 상승
- **판정:** **성공**
- **재사용 교훈:** vintage loss와 capital로 bridge한다.

### C4. excess-capital buyback — 16%

- **원문 주장:** 할인매입이 EPS C$7.39를 만든다.
- **T0 근거:** 초과자본·낮은 P/B
- **숨은 가정:** stress 후 여력
- **사전 반증조건:** MICAT·배당제한 시 반증
- **실제:** 환원은 실행·exact EPS 미검증
- **판정:** **부분**
- **재사용 교훈:** stress 뒤 잔여자본만 쓴다.

### C5. 1.5x book — 16%

- **원문 주장:** 15% ROE는 최소 1.5x book이다.
- **T0 근거:** peer·지속 ROE
- **숨은 가정:** cost of equity 안정
- **사전 반증조건:** ROE<12%면 반증
- **실제:** C$48.86 거래
- **판정:** **성공**
- **재사용 교훈:** P/B를 ROE·g·r로 해체한다.

### C6. housing 안정 — 12%

- **원문 주장:** macro 개선이 claim tail을 낮춘다.
- **T0 근거:** 2009 stabilization
- **숨은 가정:** regional shock 없음
- **사전 반증조건:** arrears 재악화 시 반증
- **실제:** systemic loss 없이 회복
- **판정:** **성공**
- **재사용 교훈:** delinquency→claim→severity로 잇는다.

---

## 4. 당시 Valuation과 Payoff Structure

약 15% ROE franchise에 최소 1.5x forward book을 적용했다. excess capital buyback 시 2014 EPS C$7.39, 2010 PV C$5.05와 4~5% dividend를 제시했다. 안전한 bridge는 `opening book+retained earnings-stress loss-capital return`이며 MICAT buffer를 매년 갱신한다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 장기 강한 성공 — C$48.86 control transaction의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry/transaction | C$24 | +40% | C$48.86 control | 성공 |
| ROE | 약 15%+ | 20%+ book compound | franchise ROE 지속 | 성공 |
| P/B | discount | ≥1.5x forward | control value | 성공 |
| 2014 EPS | C$7.39 case | C$5.05 PV | 미복원 | 미검증 |
| Capital return | 4~5%+buyback | excess 환원 | 배당·거래 | 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2009-07 | IPO | TSX MIC |
| 2009-12-29 | VIC Long | C$24 |
| 2010 | OSFI 규정 | 구조 확인 |
| 2010s | book·dividend 성장 | 복리 |
| 2019-08-13 | Brookfield 발표 | C$48.86 |
| 2019-12 | 57% close | control |
| 2020 | Sagen 개명 | 연속성 |
| 2021-04 | 100% 보유 | terminal |

### 실제 사업·자본구조

book·dividend는 성장했다. 2019 Genworth는 48,944,645주 약 57%를 Brookfield에 C$48.86/share, 약 C$2.4bn에 매각했고 이후 Sagen으로 개명해 2021 common이 비상장화됐다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

C$24는 원문 제안가, C$48.86은 2019 control 거래가다. 배당·배분시점·체결가가 없어 exact return/IRR은 null이다.

첨부·repository에 정확한 performance row가 없다. 기업·사건 결과와 security total return을 분리하며 배당·청산분배·successor shares를 날짜별로 복원하기 전 return과 IRR은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | 캐나다 계약구조 | 20% | 성공 | 국가가 아니라 계약·claim waterfall을 비교한다. |
| C2 | 시장집중·pricing | 18% | 성공 | price·share·capital로 검증한다. |
| C3 | 20%+ book 복리 | 18% | 성공 | vintage loss와 capital로 bridge한다. |
| C4 | excess-capital buyback | 16% | 부분 | stress 뒤 잔여자본만 쓴다. |
| C5 | 1.5x book | 16% | 성공 | P/B를 ROE·g·r로 해체한다. |
| C6 | housing 안정 | 12% | 성공 | delinquency→claim→severity로 잇는다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

recourse와 은행 underwriting, upfront premium·float·시장집중이 높은 ROE를 만들고 retained earnings·capital return·strategic buyer가 가치를 실현했다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 C$24 부근에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

C$7.39 EPS는 buyback·높은 ROE·낮은 loss의 동시지속이 필요했다. unemployment·regional HPI·90+ day delinquency별 stress loss가 부족했다.

### 최초 관찰 가능한 경고/반증

loss ratio가 두 분기 정상범위를 넘고 신규보험·capital return이 줄거나 MICAT buffer가 급락하면 1.5x book을 폐기한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `MIC`와 날짜를 Genworth MI Canada Inc. (현 Sagen MI Canada Inc.)의 실제 법인·security에 고정한다.
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
| Entity / direction | raw Short → **Long**, Genworth MI Canada Inc. (현 Sagen MI Canada Inc.) |
| Business thesis | 성공 |
| Valuation thesis | 성공 |
| Catalyst / timing | 장기 강한 성공 — C$48.86 control transaction |
| Thesis score | 9.0/10 |
| Process score | 8.1/10 |
| Outcome-adjusted score | 8.6/10 |

### 한 문장 교훈

> 국가가 아니라 계약·claim waterfall을 비교한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL 원문·metadata — VIC_IDEAS(4).sql / VIC, 2009-12-29. idea_id·raw direction·description 5042 chars·catalyst 117 chars
2. [Sagen corporate overview](https://investor.sagen.ca/English/home/default.aspx) — Sagen MI Canada, 2026. 2009~2021 TSX MIC 법인과 Brookfield 100% 보유
3. [OSFI Mortgage Insurance](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/mortgage-insurance) — OSFI, 2010-06-30. 80% LTV 초과 대출의 보험요건과 lender-insurer 구조
4. [Genworth SEC archive](https://www.sec.gov/edgar/browse/?CIK=1276520&owner=exclude) — SEC / Genworth, 2009-2020. IPO·majority stake·Brookfield 거래
5. [Genworth sale completion](https://investor.genworth.com/news-events/press-releases) — Genworth Financial, 2019-12-12. C$48.86/share Brookfield 거래 종결

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=MIC, entity=Genworth MI Canada Inc. (현 Sagen MI Canada Inc.), raw=Short, research=Long.
