# Boca Resorts, Inc. — 2002-04-07 — V9

> **Batch 054 canonical report.** Raw SQL `Long`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Boca Resorts, Inc. / RST |
| 실제 Security | **Boca Resorts Class A common stock** |
| Idea ID | `a18a84e4-1831-42eb-8ae9-b45fc110bac8` |
| 게시일 / 작성자 | 2002-04-07 / alli718 |
| 원 SQL 방향 | Long |
| 원문 검증 방향 | **Long** |
| 기준가격 | 약 $12.85 |
| 원 horizon | 2~4년 |
| 최종 판정 | **$24 cash takeout로 asset·sale 논지 강한 성공, exact return은 null** |

> **결론:** raw company mapping의 Rosetta Stone이 아니라 2002년 NYSE `RST`였던 Boca Resorts Long이다. 약 $12.85·tangible book $11.67에서 normalized cash flow 약 $110m, maintenance capex 후 약 $95m을 사용해 trophy South Florida resorts의 private value $20.29를 계산했다. travel recovery·repurchase·debt buyback과 strategic sale이 촉매였다. 결과적으로 **$24 cash takeout로 asset·sale 논지 강한 성공, exact return은 null**.

---

## 1. 회사는 정확히 무엇을 하는가

Boca Resorts는 South Florida의 destination resorts, golf clubs, spas, marinas와 private clubs를 보유·운영한 호텔 자산회사였다. 현금엔진은 `available room nights×occupancy×ADR+club·golf·spa·marina revenue-property payroll·F&B·marketing·maintenance capex-interest·tax`다. trophy location과 management-contract 비구속성은 strategic value를 만들지만 book/replacement value가 common cash가 되려면 property debt·deferred capex·tax와 control structure를 차감하고 실제 매각확률을 붙여야 한다.

### Security cash waterfall

Property EBITDA에서 maintenance/renovation capex·property/holdco debt·interest·tax와 transaction leakage를 차감한다. tangible book와 resort appraisal은 매각 전 common cash가 아니며 Class A의 control discount를 반영한다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw company mapping의 Rosetta Stone이 아니라 2002년 NYSE `RST`였던 Boca Resorts Long이다. 약 $12.85·tangible book $11.67에서 normalized cash flow 약 $110m, maintenance capex 후 약 $95m을 사용해 trophy South Florida resorts의 private value $20.29를 계산했다. travel recovery·repurchase·debt buyback과 strategic sale이 촉매였다.

### Reverse expectations

약 $12.85가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. trophy scarcity — 20%

- **원문 주장:** South Florida resort locations가 book보다 가치 있다.
- **T0 근거:** waterfront·club·marina assets
- **숨은 가정:** replacement·entitlement가 어렵다.
- **사전 반증조건:** comparable sales/book 이하이면 반증.
- **실제:** $24 strategic bid
- **판정:** **강한 성공**
- **재사용 교훈:** scarcity는 third-party bid로 검증한다.

### C2. normalized $110m — 18%

- **원문 주장:** depressed travel 뒤 cash flow가 회복한다.
- **T0 근거:** portfolio history
- **숨은 가정:** 2001 shock가 영구수요 훼손이 아니다.
- **사전 반증조건:** 2년 normalized EBITDA 미회복이면 반증.
- **실제:** buyer가 $20.29 상단 지불
- **판정:** **성공 방향**
- **재사용 교훈:** cycle recovery와 asset sale을 별도 경로로 둔다.

### C3. unencumbered control — 18%

- **원문 주장:** management-contract 제약이 적어 buyer universe가 넓다.
- **T0 근거:** property structure
- **숨은 가정:** change-of-control 비용이 제한적이다.
- **사전 반증조건:** brand/management termination fee가 크면 반증.
- **실제:** Blackstone affiliate가 whole company 계약
- **판정:** **성공**
- **재사용 교훈:** 호텔 SOTP는 brand encumbrance를 확인한다.

### C4. balance-sheet floor — 16%

- **원문 주장:** $11.67 book와 낮은 debt가 하방이다.
- **T0 근거:** tangible book·$184.4m debt
- **숨은 가정:** deferred capex가 작다.
- **사전 반증조건:** repair capex로 book가 소진되면 반증.
- **실제:** $24 cash event
- **판정:** **기간 성공**
- **재사용 교훈:** book floor는 capex·debt 후 net이다.

### C5. sale catalyst — 16%

- **원문 주장:** strategic/PE buyer가 몇 년 안에 control premium을 낸다.
- **T0 근거:** SQL catalyst·owner actions
- **숨은 가정:** controller가 매각을 선택한다.
- **사전 반증조건:** levered expansion 우선이면 반증.
- **실제:** 2004 Blackstone 계약
- **판정:** **강한 성공**
- **재사용 교훈:** sale thesis에는 control owner의 행동을 둔다.

### C6. entity resolution — 12%

- **원문 주장:** 2002 RST는 Rosetta Stone이 아니라 Boca Resorts다.
- **T0 근거:** date·VIC link·SEC ticker
- **숨은 가정:** security mapping이 정확하다.
- **사전 반증조건:** CIK/business 불일치면 반증.
- **실제:** CIK 1020905 Boca로 확정
- **판정:** **성공**
- **재사용 교훈:** ticker는 법인이 아니며 날짜별로 resolve한다.

---

## 4. 당시 Valuation과 Payoff Structure

normalized cash flow $110m×9=$990m에서 debt $184.4m을 빼고 39.7m shares로 나누면 $20.29다. maintenance capex 후 $95m FCF는 당시 EV 대비 약 13.6% property cash yield로 제시됐다. book와 normalized cash는 참고치이고 deferred maintenance·tax·property debt·control을 차감한 net sale proceeds가 common payoff다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | $24 cash takeout로 asset·sale 논지 강한 성공, exact return은 null의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry/fair value | $12.85 | $20.29 | $24 cash agreement | 강한 성공 |
| Tangible book | $11.67/share | public floor | $24 buyer value | 방향 성공 |
| Normalized cash | $110m | 9x private value | transaction이 상단 지지 | 성공 방향 |
| Maintenance FCF | $95m | 13.6% EV yield | exact cohort 없음 | 미검증 |
| Control | Huizenga ~98% vote | sale route | merger vote 확보 | 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2001-09 | travel shock | depressed earnings |
| 2002-04-07 | VIC Long | $12.85 |
| 2002~04 | Florida travel 회복 | normalized cash path |
| 2004-10-20 | Blackstone agreement | $24 cash |
| 2004-11-15 | definitive proxy | terms·assets 공개 |
| 2004-12-08 | stockholder vote 예정 | control gate |
| 2004말 | takeout process | terminal cash event |

### 실제 사업·자본구조

2004-10 Boca Resorts board는 Blackstone affiliate와 합병계약을 승인했고 1주당 $24 cash를 제시했다. proxy는 five destination resorts와 golf·spa·marina assets, H. Wayne Huizenga의 약 98% voting power와 $24 consideration을 확인한다. $24는 원문 $20.29를 상회해 trophy scarcity·control sale 논지를 직접 검증했다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

현 SQL에는 catalyst 925자만 있고 description·performance는 없다. $12.85·$20.29·$24는 T0와 transaction anchors다. 게시일 종가·배당·세금·정확 closing 보유기간을 포함한 performance row가 없으므로 canonical total return/IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | trophy scarcity | 20% | 강한 성공 | scarcity는 third-party bid로 검증한다. |
| C2 | normalized $110m | 18% | 성공 방향 | cycle recovery와 asset sale을 별도 경로로 둔다. |
| C3 | unencumbered control | 18% | 성공 | 호텔 SOTP는 brand encumbrance를 확인한다. |
| C4 | balance-sheet floor | 16% | 기간 성공 | book floor는 capex·debt 후 net이다. |
| C5 | sale catalyst | 16% | 강한 성공 | sale thesis에는 control owner의 행동을 둔다. |
| C6 | entity resolution | 12% | 성공 | ticker는 법인이 아니며 날짜별로 resolve한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

depressed public hotel earnings가 아니라 irreplaceable Florida locations와 unencumbered control이 private buyer에게 높은 strategic value를 준 것이 수익경로였다. travel 완전회복을 기다리기 전에 buyer가 normalized economics를 선반영했다. 강한 controlling owner의 매각 의사도 hard gate였다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 약 $12.85에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

9x cash flow와 13.6% yield가 property별 quality·renovation need를 평균화했고, $110m normalized cash의 cycle range를 충분히 보이지 않았다. Huizenga control은 sale을 빠르게 할 수 있지만 minority가 다른 가격을 강제하기 어렵다는 양면성이 있다.

### 최초 관찰 가능한 경고/반증

Boca 핵심 property의 occupancy·ADR 회복이 market보다 뒤지고 maintenance capex가 normalized FCF의 20% 이상을 추가로 소모하거나 controlling owner가 sale 대신 levered acquisition을 택하면 $20.29 appraisal을 낮춘다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `RST`를 단일 회사로 보지 말고 Boca Resorts, Inc. 법인·날짜·실제 security로 고정한다.
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
| Entity / direction | raw Long → **Long**, Boca Resorts, Inc. |
| Business thesis | 성공 방향 |
| Valuation thesis | 강한 성공 |
| Catalyst / timing | $24 cash takeout로 asset·sale 논지 강한 성공, exact return은 null |
| Thesis score | 9.4/10 |
| Process score | 9.5/10 |
| Outcome-adjusted score | 9.4/10 |

### 한 문장 교훈

> scarcity는 third-party bid로 검증한다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL catalyst / prior curated metadata](https://www.valueinvestorsclub.com/idea/Boca_Resorts_Inc/7610357754) — VIC_IDEAS(4).sql / VIC / repository prior overlay, 2002-04-07. idea_id·catalyst 925 chars·description absent; date·author·raw flag·원문 anchor는 prior overlay 대조
2. [Boca Resorts SEC archive](https://www.sec.gov/Archives/edgar/data/1020905/) — SEC / Boca Resorts, 1997-2004. RST ticker, annual reports와 merger filings
3. [Boca Resorts 10-K search](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001020905&type=10-K) — SEC / Boca Resorts, 1997-2004. portfolio·debt·cash-flow disclosures
4. [Boca Resorts merger proxy](https://www.sec.gov/Archives/edgar/data/1020905/000095014404011165/g91505ddefm14a.htm) — SEC / Boca Resorts, 2004-11-15. Blackstone affiliate, $24 cash, portfolio와 voting control
5. [Merger consideration ownership filing](https://www.sec.gov/Archives/edgar/data/1020905/000129378804000015/xslF345X02/primary_doc.xml) — SEC / Boca Resorts, 2004. transaction-related security disposition evidence

### 데이터 품질

- 원문·metadata: **C** — 첨부 SQL에는 catalyst만 있고 Batch 054 description은 0건이다. date·author·raw flag·원문 수치는 prior curated overlay를 별도 provenance로 대조했다.
- 기업·사건: **A/B** — SEC·FTC·회사 filing으로 segment 결과·corporate action·terminal event를 검증했다.
- 가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. corporate event·filing price range를 exact return으로 바꾸지 않고 return/IRR을 null로 유지했다.
- 교정: ticker=RST, entity=Boca Resorts, Inc., raw=Long, research=Long.
