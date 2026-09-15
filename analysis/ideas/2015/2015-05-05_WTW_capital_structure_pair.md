# Weight Watchers International, Inc. — 2015-05-05 — V9

> **Batch 057 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Pair**으로 확정했다. Research as-of 2026-09-15.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Weight Watchers International, Inc. / WTW |
| 실제 Security | **Short common + Long Tranche B-1 first-lien term loan** |
| Idea ID | `be3754ee-1951-434d-a1cd-1bf7f106f800` |
| 게시일 / 작성자 | 2015-05-05 / pistolpete |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Pair** |
| 기준가격 | common 약 $8.46 / B-1 약 89 |
| 원 horizon | 12~18개월 |
| 최종 판정 | **B-1 성공·common Short 실패·pair 혼합/실패·exact return 미검증** |

> **결론:** raw 단순 Short가 아니라 common을 Short하고 89에 거래된 2016년 만기 B-1 first-lien loan을 Long한 자본구조 pair다. cash $301m·undrawn revolver $50m과 B-1의 짧은 만기는 credit leg을 지지했지만, 2015년 10월 Oprah의 10% 투자와 board/brand 참여가 common bankruptcy narrative를 뒤집었다. 결과적으로 **B-1 성공·common Short 실패·pair 혼합/실패·exact return 미검증**.

---

## 1. 회사는 정확히 무엇을 하는가

당시 WTW는 Willis Towers Watson이 아니라 Weight Watchers International common과 그 차입금이다. 회사는 대면 meetings, digital 체중관리 구독, 제품·라이선싱을 판매했다. 현금엔진은 `meeting attendance×fee+digital subscribers×ARPU+products/licensing-leader·rent·marketing·technology-interest-tax`다. 고정비가 큰 만큼 subscriber gross additions와 retention이 동시에 좋아질 때 operating leverage가 크지만, free apps·wearables·낮은 category relevance는 gross additions를 빠르게 훼손한다. 2012 debt-funded tender 뒤에는 enterprise value가 맞아도 common, 2016년 만기 B-1, 2020년 만기 B-2의 payoff가 달랐으므로 security별 waterfall이 분석의 출발점이다.

### Security cash waterfall

동일 enterprise cash에서 2016-04-02 만기 B-1 first-lien 약 $292.3m이 common보다 먼저 지급된다. B-2 약 $2.1bn과 common은 그 뒤의 residual claim이다. 따라서 포지션은 회사 전망 하나가 아니라 `B-1 repayment probability·carry/pull-to-par`와 `common downside·borrow/squeeze` 두 payoff를 sizing 후 합쳐야 한다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw 단순 Short가 아니라 common을 Short하고 89에 거래된 2016년 만기 B-1 first-lien loan을 Long한 자본구조 pair다. cash $301m·undrawn revolver $50m과 B-1의 짧은 만기는 credit leg을 지지했지만, 2015년 10월 Oprah의 10% 투자와 board/brand 참여가 common bankruptcy narrative를 뒤집었다.

### Reverse expectations

common 약 $8.46 / B-1 약 89가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. attendance·product decline — 20%

- **원문 주장:** meetings와 제품의 구조적 쇠퇴가 EBITDA를 낮춘다.
- **T0 근거:** attendance 약 62.0%→48.3%, products $442.7m→$298.0m
- **숨은 가정:** digital/brand rescue가 gross adds를 못 되돌린다.
- **사전 반증조건:** gross additions·attendance의 지속 반등이면 반증.
- **실제:** Oprah 이후 subscriber narrative가 반전했다.
- **판정:** **부분→실패**
- **재사용 교훈:** 구조적 decline에도 rescue option을 가격화한다.

### C2. B-1 money-good — 18%

- **원문 주장:** 89의 B-1은 cash와 짧은 만기로 par 상환된다.
- **T0 근거:** $301m cash+$50m revolver 대 $292.3m principal
- **숨은 가정:** cash가 common보다 senior maturity에 배정된다.
- **사전 반증조건:** liquidity burn·교차가속·refinancing 실패면 반증.
- **실제:** 2016-04-01 잔액 $144.3m cash 상환.
- **판정:** **성공**
- **재사용 교훈:** enterprise distress 속에서도 maturity별 claim을 산다.

### C3. B-2가 common 압박 — 18%

- **원문 주장:** $2.1bn B-2와 6.5x leverage가 equity를 훼손한다.
- **T0 근거:** B-2 약 56·2020 maturity
- **숨은 가정:** 운영회복 전 refinancing이 불가능하다.
- **사전 반증조건:** sponsor/전략투자·EBITDA 반등이면 반증.
- **실제:** 외부 투자와 후속 회복으로 option value 유지.
- **판정:** **실패**
- **재사용 교훈:** distressed debt는 common zero의 충분조건이 아니다.

### C4. pair convexity — 16%

- **원문 주장:** credit carry와 equity downside가 함께 발생한다.
- **T0 근거:** 원문 base +35%와 +16.4%
- **숨은 가정:** B-1 보호 요인이 common에는 도움이 되지 않는다.
- **사전 반증조건:** 동일 rescue catalyst가 두 security를 올리면 반증.
- **실제:** Oprah가 정확히 이 상관을 깨뜨렸다.
- **판정:** **실패**
- **재사용 교훈:** pair는 각 leg보다 cross-catalyst를 먼저 stress한다.

### C5. common downside — 16%

- **원문 주장:** 2015 guide와 category decline으로 common이 더 내려간다.
- **T0 근거:** Q4 guide shock와 $8.46 price
- **숨은 가정:** borrow와 squeeze cost가 제한적이다.
- **사전 반증조건:** strategic capital·subscriber inflection이면 cover.
- **실제:** Oprah 발표 뒤 squeeze.
- **판정:** **실패**
- **재사용 교훈:** Short payoff에는 borrow와 rescue 확률을 넣는다.

### C6. security selection — 12%

- **원문 주장:** common보다 B-1이 훨씬 좋은 risk/reward다.
- **T0 근거:** first-lien·짧은 maturity·현금 cover
- **숨은 가정:** claim priority가 실제 지급으로 이어진다.
- **사전 반증조건:** B-1 default/restructuring이면 반증.
- **실제:** B-1은 par 상환, common은 생존.
- **판정:** **강한 성공**
- **재사용 교훈:** 회사보다 cash-flow claim을 선택한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 base는 common Short 약 +35%, B-1 YTM/pull-to-par 약 +16.4%, 두 leg의 단순 합 약 +52%였다. 그러나 이는 notional·duration·borrow fee·short squeeze·loan accrued interest를 조정한 pair IRR이 아니다. B-1은 89에서 par 상환 여지가 있었지만 common은 option-like residual이라 촉매 전 무한대 손실 꼬리를 갖는다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Pair 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | B-1 성공·common Short 실패·pair 혼합/실패·exact return 미검증의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Common/B-1 entry | $8.46 / 89 | Short 하락 / par 수렴 | common squeeze / B-1 par 상환 | leg 분리 |
| B-1 principal/maturity | $292.3m / 2016-04-02 | 11개월 내 지급 | $144.3m 잔액 cash 상환 | 성공 |
| Liquidity | $301m cash+$50m revolver | B-1 cover | 상환자금 제공 | 성공 |
| B-2/leverage | $2.1bn·약 56 / 6.5x | common 압박 | refinancing option 유지 | 혼합 |
| 원문 base payoff | +35%/+16.4%/합 +52% | 12~18개월 | sizing·borrow 미복원 | 미검증 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2012 | $1.5bn debt-funded tender | common leverage 상승 |
| 2014 | adjusted EBITDA $361.7m·제품매출 하락 | denominator 약화 |
| 2015-05-05 | VIC pair 게시 | common Short/B-1 Long |
| 2015-10-19 | Oprah 10% 투자 | equity 핵심 반증 |
| 2015-Q4 | brand/refinancing narrative 반전 | Short squeeze |
| 2016-04-01 | B-1 $144.3m par 상환 | credit leg 성공 |
| 2017-2018 | subscriber·주가 회복 | common Short 최종 실패 |

### 실제 사업·자본구조

2015-10-19 Oprah는 약 $43.2m에 6,362,103주, 약 10%를 취득하고 options·board role·협업을 받았다. common은 강하게 반등해 Short leg을 훼손했다. 반면 회사는 2016-04-01 B-1 잔액 약 $144.3m을 cash로 par 상환해 senior credit 판단을 확인했다. 기업 분석은 양쪽 leg에서 달랐고 pair 전체는 sizing/borrow 자료 없이 exact 성과를 낼 수 없다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

현재 SQL은 description 32,273자와 catalyst 2,073자를 포함하지만 performance COPY는 없다. common $8.46·B-1 89·원문 +35%/+16.4%/+52%는 T0 payoff model이며, 실제 borrow·notional·cover/repayment cash flow가 없어 pair return과 IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | attendance·product decline | 20% | 부분→실패 | 구조적 decline에도 rescue option을 가격화한다. |
| C2 | B-1 money-good | 18% | 성공 | enterprise distress 속에서도 maturity별 claim을 산다. |
| C3 | B-2가 common 압박 | 18% | 실패 | distressed debt는 common zero의 충분조건이 아니다. |
| C4 | pair convexity | 16% | 실패 | pair는 각 leg보다 cross-catalyst를 먼저 stress한다. |
| C5 | common downside | 16% | 실패 | Short payoff에는 borrow와 rescue 확률을 넣는다. |
| C6 | security selection | 12% | 강한 성공 | 회사보다 cash-flow claim을 선택한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

credit leg은 짧은 maturity, first-lien priority와 당시 cash/revolver가 만들었다. equity leg 실패는 손익의 완만한 개선보다 외부 전략투자자가 refinancing probability와 brand relevance를 한 번에 바꾼 데서 왔다. 같은 enterprise에서 senior debt와 common의 duration·convexity가 반대였다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 common 약 $8.46 / B-1 약 89에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

B-1 repayment와 common bankruptcy를 함께 놓고 상관이 낮다고 본 것이 오류다. B-1을 지키는 liquidity·refinancing catalyst가 common option value도 급등시킬 수 있었다. 또한 leg별 notional, borrow availability/fee, stop-loss와 Oprah 같은 rescue catalyst의 확률을 base payoff에 반영하지 않았다.

### 최초 관찰 가능한 경고/반증

전략투자·brand partnership가 발표되거나 common의 borrow cost/short interest가 급등하는 동시에 B-1 price가 par 쪽으로 움직이면 pair의 두 leg가 동시에 이기는 전제가 깨진 것으로 보고 common Short를 우선 재승인한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `WTW`를 단일 회사명으로 보지 말고 Weight Watchers International, Inc. 법인·날짜·security로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Pair을 확정한다.
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
| Entity / direction | raw Short → **Pair**, Weight Watchers International, Inc. |
| Business thesis | 성공 |
| Valuation thesis | leg 분리 |
| Catalyst / timing | B-1 성공·common Short 실패·pair 혼합/실패·exact return 미검증 |
| Thesis score | 6.0/10 |
| Process score | 9.2/10 |
| Outcome-adjusted score | 7.6/10 |

### 한 문장 교훈

> 구조적 decline에도 rescue option을 가격화한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL 원문/metadata — VIC_IDEAS(4).sql / VIC, 2015-05-05. idea_id·raw Short·catalyst 2073 chars·description 32273 chars; 현재 SQL에 없는 원문 수치는 lower-provenance overlay로 분리
2. [WeightWatchers SEC archive](https://www.sec.gov/edgar/browse/?CIK=105319&owner=exclude) — SEC / Weight Watchers, 2001-2019. annual filings·debt·attendance·digital subscriber 연속성
3. [WeightWatchers annual reports](https://corporate.ww.com/financials/annual-reports-and-proxy/default.aspx) — WW International, 2008-2025. 2012 tender·2014 실적·2016 B-1·2018~19 subscriber 검증
4. [WeightWatchers SEC filings](https://corporate.ww.com/financials/sec-filings/default.aspx) — WW International, 2001-2025. 공식 10-K·10-Q·8-K archive
5. [Weight Watchers 2017 proxy](https://www.sec.gov/Archives/edgar/data/105319/000119312517107775/d264156ddef14a.htm) — SEC / Weight Watchers, 2017-04. meetings·online 정의와 Oprah 주식·option 계약
6. [Oprah partnership release](https://corporate.ww.com/news/news-details/2015/Oprah-Winfrey-And-Weight-Watchers-Join-Forces-In-Groundbreaking-Partnership/default.aspx) — Weight Watchers, 2015-10-19. 10% 지분·option·board·협업 catalyst

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL description 32,273자와 catalyst 2,073자를 직접 확인했다.
- 기업·사건: **A/B** — SEC·회사·정부기관 자료로 operating·capital·regulatory event를 교차검증했다.
- 가격성과: **C** — 현재 SQL에 performance COPY가 없다. legacy ABG 수치와 WTW ticker 오염값을 폐기했고 corporate event를 exact return으로 바꾸지 않았다.
- 교정: ticker=WTW, entity=Weight Watchers International, Inc., raw=Short, research=Pair.
