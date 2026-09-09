# Athene Holding Ltd. — 2019-03-31 — V9

> **Batch 046 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-09.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Athene Holding Ltd. / ATH |
| Idea ID | `cea526a6-864b-4eb5-a1f5-3ef84f9d1700` |
| 게시일 / 작성자 | 2019-03-31 / sas7 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격 | 약 $40 |
| 원 horizon | 3~5년 |
| 최종 판정 | **$64 target과 strategic value가 합병 경로에서 실현된 성공** |

> **결론:** raw Short지만 실제는 Long이다. 2019/2020 EPS $7.30/$8.50에 5.5x/4.8x, adjusted BVPS $45.60에서 약 0.8x였다. 4.65% yield에서 crediting 1.70%, DAC 1.35%, opex 0.35%를 빼 after-tax ROA 1.25~1.35%, 11~13x leverage로 15%+ ROE를 만들 수 있다고 봤다. 7.5x 2020 EPS 또는 1.2x book의 $64, +57%가 target이다. 결과적으로 **$64 target과 strategic value가 합병 경로에서 실현된 성공**.

---

## 1. 회사는 정확히 무엇을 하는가

Athene은 retail annuity·institutional reinsurance로 장기 보험부채를 조달하고 fixed income·structured credit·private assets에 투자해 spread를 번다. 현금엔진은 `투자수익률 - 계약자 crediting/hedging cost - DAC amortization - 운영비 - 실현 신용손실 - 세금·자본비용`이다. Apollo는 origination과 자산운용을 제공하지만 약 40bp의 fee와 관련자 거래·governance 문제도 만든다. P/B나 P/E만 볼 수 없고, asset/liability duration, surrender behavior, ratings·RBC, AOCI와 economic credit loss, excess capital, buyback·reinsurance economics를 연결해야 한다.

### Common equity cash waterfall

회계이익에서 운전자본·담보·규제자본·maintenance/growth investment·interest·tax를 차감하고, common보다 선순위인 계약·채권자 청구권을 먼저 배치한다. 자산가치와 계약상 수취액은 현금화 날짜·세금·재투자 의무를 반영한다. 기업가치가 맞아도 security와 duration이 틀리면 투자결과는 실패할 수 있다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw Short지만 실제는 Long이다. 2019/2020 EPS $7.30/$8.50에 5.5x/4.8x, adjusted BVPS $45.60에서 약 0.8x였다. 4.65% yield에서 crediting 1.70%, DAC 1.35%, opex 0.35%를 빼 after-tax ROA 1.25~1.35%, 11~13x leverage로 15%+ ROE를 만들 수 있다고 봤다. 7.5x 2020 EPS 또는 1.2x book의 $64, +57%가 target이다.

### Reverse expectations

약 $40가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. spread ROA 1.25~1.35% — 20%

- **원문 주장:** 4.65-1.70-1.35-0.35% bridge다.
- **T0 근거:** asset/liability cost breakdown
- **숨은 가정:** credit loss·tax가 정상이다.
- **사전 반증조건:** realized loss·hedge cost로 1% 아래면 반증.
- **실제:** pandemic을 통과하고 franchise가 확대됐다.
- **판정:** **성공**
- **재사용 교훈:** 보험 ROA는 모든 자본·credit cost 후로 본다.

### C2. 15%+ ROE — 18%

- **원문 주장:** 11~13x leverage로 mid-teens ROE다.
- **T0 근거:** ROA와 operating leverage
- **숨은 가정:** ratings capital이 leverage를 허용한다.
- **사전 반증조건:** capital raise·RBC 압박이면 반증.
- **실제:** capital survival과 거래가 이를 지지했다.
- **판정:** **성공**
- **재사용 교훈:** accounting leverage보다 statutory constraint다.

### C3. credit fear 과도 — 18%

- **원문 주장:** 94% IG이고 alternatives 위험은 작다.
- **T0 근거:** true PE/HF 약 assets 75bp
- **숨은 가정:** CLO senior·RMBS losses가 제한적.
- **사전 반증조건:** downgrade/OTTI가 recession model 초과.
- **실제:** 2020 modeled loss보다 견조했다.
- **판정:** **성공**
- **재사용 교훈:** label이 아니라 tranche·attachment point를 본다.

### C4. direct origination alpha — 16%

- **원문 주장:** 40bp yield advantage와 33% 목표가 있다.
- **T0 근거:** Apollo sourcing
- **숨은 가정:** 추가 yield가 loss·fee보다 크다.
- **사전 반증조건:** capital-adjusted spread가 peer 아래면 반증.
- **실제:** Apollo 결합이 전략가치를 확인했다.
- **판정:** **성공**
- **재사용 교훈:** origination alpha는 fee 차감 후 검증한다.

### C5. rate downside 제한 — 16%

- **원문 주장:** ±25bp는 $25~30m, zero rate도 -10~15%다.
- **T0 근거:** management sensitivity
- **숨은 가정:** surrender·hedge가 모델 내다.
- **사전 반증조건:** earnings/book 훼손이 sensitivity 초과.
- **실제:** stress에도 terminal value가 유지됐다.
- **판정:** **부분 성공**
- **재사용 교훈:** nonlinear ALM tail을 별도 stress한다.

### C6. $64/20% IRR — 12%

- **원문 주장:** 7.5x EPS·1.2x book 또는 unchanged multiple compounding.
- **T0 근거:** 낮은 starting multiple
- **숨은 가정:** book growth가 share count 후 유지.
- **사전 반증조건:** BVPS 정체·merger dilution이면 반증.
- **실제:** 합병 경로가 target을 지지했다.
- **판정:** **성공**
- **재사용 교훈:** target과 exact total return을 구분한다.

---

## 4. 당시 Valuation과 Payoff Structure

2019 EPS $7.30, 2020 $8.50과 약 $40 가격은 5.5x/4.8x다. YE18 adjusted BVPS $45.60, 2019-06 약 $49, statutory book 약 $56였다. Base $64는 7.5x 2020 EPS 또는 1.2x YE19 book. multiple이 그대로 5.5x여도 15% book/earnings compound로 약 20% IRR을 기대했다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | $64 target과 strategic value가 합병 경로에서 실현된 성공의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2020 EPS | $8.50E | 7.5x | $64 target bridge | 성공 |
| Adjusted BVPS | $45.60→$49 | 15% compound | 합병 strategic value | 성공 |
| P/B | 약 0.8x | 1.2x | terminal rerating | 성공 |
| After-tax ROA | 1.25~1.35% | 유지 | stress survival | 성공 |
| Target | $64 | +57% | 합병 경로 지지 | 성공/정확수익 미검증 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2018-12 | BVPS $45.60 | book anchor |
| 2019-03-31 | VIC Long | <5x 2020 EPS |
| 2019-06 | BVPS 약 $49 | compounding |
| 2020-03 | COVID credit shock | stress test |
| 2020-09 | 후속 Long | 0.7x book |
| 2021-03 | Apollo 거래 발표 | $11bn strategic event |
| 2022-01-03 | 합병 종결 | target 경로 실현 |

### 실제 사업·자본구조

2020 pandemic은 credit·ALM·capital의 실제 stress test였지만 Athene은 생존했고 ACRA·reinsurance와 Apollo 연계를 확대했다. 2021 전액주식 결합 발표와 2022 종결로 standalone ATH는 APO 1.149주 교환 구조로 끝났다. 합병 경로의 implied value는 원문의 $64 target을 지지했으나 exact total return은 SQL 부재로 산출하지 않았다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

SQL performance row가 없다. 원문 배수로 역산한 약 $40은 근사치이며 공식 entry price가 아니다. $64 target 달성 판정은 merger exchange economics와 후속 price anchor를 사용한 사건 판정이고 exact return은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | spread ROA 1.25~1.35% | 20% | 성공 | 보험 ROA는 모든 자본·credit cost 후로 본다. |
| C2 | 15%+ ROE | 18% | 성공 | accounting leverage보다 statutory constraint다. |
| C3 | credit fear 과도 | 18% | 성공 | label이 아니라 tranche·attachment point를 본다. |
| C4 | direct origination alpha | 16% | 성공 | origination alpha는 fee 차감 후 검증한다. |
| C5 | rate downside 제한 | 16% | 부분 성공 | nonlinear ALM tail을 별도 stress한다. |
| C6 | $64/20% IRR | 12% | 성공 | target과 exact total return을 구분한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

높은 starting earnings yield, book compounding과 capital survival이 time arbitrage를 만들었다. 94% investment-grade, 제한된 true PE/HF exposure와 dry powder가 시장의 'shadow banking' 공포를 완화했고, Apollo가 최종 strategic buyer가 됐다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 약 $40에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

zero-rate earnings impact 10~15%와 recession loss를 단년으로 단순화했고, fee conflict·structured-credit tail과 AOCI liquidity를 더 깊게 stress할 수 있었다. 반대로 market은 headline alternatives/CLO exposure를 실제 equity-at-risk보다 크게 봤다.

### 최초 관찰 가능한 경고/반증

statutory capital이 modeled recession 뒤에도 유지되고 OTTI/realized loss가 원문 120bp cumulative stress 아래라면 Long 유지; 반대로 ratings downgrade·capital raise면 즉시 thesis break다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `ATH`를 회사로 보지 말고 Athene Holding Ltd. 법인·exchange·날짜로 고정한다.
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
| Entity / direction | raw Short → **Long**, Athene Holding Ltd. |
| Business thesis | 성공 |
| Valuation thesis | 성공 |
| Catalyst / timing | $64 target과 strategic value가 합병 경로에서 실현된 성공 |
| Thesis score | 9.0/10 |
| Process score | 9.0/10 |
| Outcome-adjusted score | 9.0/10 |

### 한 문장 교훈

> 보험 ROA는 모든 자본·credit cost 후로 본다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/ATHENE_HOLDING_LTD/2008198635) — VIC_IDEAS(4).sql / VIC, 2019-03-31. idea_id·raw direction·description 20556 chars·catalyst 617 chars
2. [Athene SEC filing archive](https://www.sec.gov/edgar/browse/?CIK=1527469&owner=exclude) — SEC / Athene, 2016-2022. book value·spread·capital·related-party disclosure
3. [Athene 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1527469/000152746921000018/ath-20201231.htm) — SEC / Athene, 2021-02-26. 2020 stress, portfolio, capital과 earnings bridge
4. [Apollo and Athene transaction close](https://ir.apollo.com/news-events/press-releases/detail/28/apollo-and-athene-announce-transaction-close) — Apollo, 2022-01-03. 전액주식 합병 종결과 standalone ATH의 terminal event

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=ATH, entity=Athene Holding Ltd., raw=Short, research=Long.
