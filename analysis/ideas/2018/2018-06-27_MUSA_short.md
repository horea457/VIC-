# Murphy USA Inc. — 2018-06-27 — V9

> **Batch 049 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Short**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Murphy USA Inc. / MUSA |
| Idea ID | `1f5e5ed8-0ff8-46eb-a46e-b11f7a3aacd4` |
| 게시일 / 작성자 | 2018-06-27 / cable888 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Short** |
| 기준가격 | $74.22 next-day close |
| 원 horizon | 6~18개월 |
| 최종 판정 | **실패 — 6개월 +6.5% 후 1년 -11.6%, 3년 -77.4% simple short P&L** |

> **결론:** raw와 실제 모두 Short다. 2017 Short를 갱신해 약 $560m 누적 capex에도 EBITDA가 늘지 않았고, kiosk format·same-store gallons 약세·높아진 leverage로 guidance cut과 buyback 중단을 기대했다. 정상 fuel contribution을 15 cpg 이하, 2018 EBITDA를 $350m, multiple을 grocery loser 수준 6x로 두어 $40 target을 제시했다. 결과적으로 **실패 — 6개월 +6.5% 후 1년 -11.6%, 3년 -77.4% simple short P&L**.

---

## 1. 회사는 정확히 무엇을 하는가

Murphy USA는 대형 소형매장·kiosk 기반의 연료 및 편의점 체인이다. 당시 핵심 입지는 Walmart 인접 부지였고 Murphy Express, 이후 QuickChek까지 포맷을 넓혔다. 주당가치 엔진은 gallons × total fuel contribution per gallon + merchandise gross profit - store operating cost - SG&A - maintenance/growth capex - interest·tax를 계속 줄어드는 희석주식수로 나눈 값이다. 연료수요 감소가 곧 연료이익 감소는 아니다. 소규모 독립사업자의 breakeven CPG, 공급 최적화·RIN, 경쟁강도와 가격전가 속도가 volume과 반대 방향으로 움직일 수 있기 때문이다.

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

raw와 실제 모두 Short다. 2017 Short를 갱신해 약 $560m 누적 capex에도 EBITDA가 늘지 않았고, kiosk format·same-store gallons 약세·높아진 leverage로 guidance cut과 buyback 중단을 기대했다. 정상 fuel contribution을 15 cpg 이하, 2018 EBITDA를 $350m, multiple을 grocery loser 수준 6x로 두어 $40 target을 제시했다.

### Reverse expectations

$74.22 next-day close가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. SSS weakness — 20%

- **원문 주장:** same-store gallons가 계속 감소한다.
- **T0 근거:** 2018 Q1 약세·누적 capex
- **숨은 가정:** traffic loss가 지속적이다.
- **사전 반증조건:** 두 분기 회복과 chain volume 개선이면 반증.
- **실제:** FY -0.6%지만 Q4 +2.1%였다.
- **판정:** **부분 성공**
- **재사용 교훈:** 같은 해 평균과 exit-rate를 함께 본다.

### C2. 15 cpg ceiling — 18%

- **원문 주장:** 정상 fuel contribution은 15 cpg 이하다.
- **T0 근거:** 과거 평균과 RIN 하락
- **숨은 가정:** industry cost curve가 변하지 않는다.
- **사전 반증조건:** 16 cpg 이상이 반복되면 반증.
- **실제:** 2018 16.2 cpg였다.
- **판정:** **실패**
- **재사용 교훈:** mean reversion 전 구조적 breakeven 변화를 확인한다.

### C3. $350m EBITDA — 18%

- **원문 주장:** volume·CPG 압박으로 EBITDA가 $350m 이하다.
- **T0 근거:** 2013~18 EBITDA 정체
- **숨은 가정:** merchandise와 cost가 상쇄하지 못한다.
- **사전 반증조건:** $400m 이상이면 target bridge 반증.
- **실제:** 실제 $412m였다.
- **판정:** **실패**
- **재사용 교훈:** target earnings에는 명확한 cover threshold를 둔다.

### C4. buyback stop — 16%

- **원문 주장:** leverage/covenant가 repurchase를 막는다.
- **T0 근거:** capex·debt 부담
- **숨은 가정:** board가 balance sheet를 우선한다.
- **사전 반증조건:** 분기 repurchase 지속이면 반증.
- **실제:** Q1 $71.7m 등 매입이 이어졌다.
- **판정:** **실패**
- **재사용 교훈:** covenant headroom을 실제 정의로 계산한다.

### C5. 6x proxy — 16%

- **원문 주장:** grocery loser multiple이 적절하다.
- **T0 근거:** kiosk·tobacco·낮은 merchandise mix
- **숨은 가정:** fuel economics의 변동성과 quality가 유사하다.
- **사전 반증조건:** CPG·FCF conversion이 peer보다 높으면 반증.
- **실제:** 시장은 장기 더 높은 가치를 부여했다.
- **판정:** **실패**
- **재사용 교훈:** peer가 없으면 unit economics로 DCF를 먼저 만든다.

### C6. $40 payoff — 12%

- **원문 주장:** earnings miss와 de-rate가 약 -45%를 만든다.
- **T0 근거:** $350m×6x
- **숨은 가정:** 두 가정이 동시에 실현된다.
- **사전 반증조건:** 한 가정만 실패해도 target을 재산정한다.
- **실제:** 6개월만 일부 이익, 3년 큰 손실이었다.
- **판정:** **실패**
- **재사용 교훈:** Short target은 earnings와 multiple의 독립 확률을 곱한다.

---

## 4. 당시 Valuation과 Payoff Structure

$350m EBITDA × 6x에서 순부채를 빼 $40을 만든 구조다. 2018 실제 adjusted EBITDA $412m만 넣어도 EV가 18% 커지고, cpg·merchandise·share count 차이가 equity target을 더 크게 바꾼다. 6x proxy는 grocery format의 inventory, margin, working-capital과 fuel-retail의 high-throughput economics가 같다는 가정이라 peer mismatch가 컸다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Short 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 실패 — 6개월 +6.5% 후 1년 -11.6%, 3년 -77.4% simple short P&L의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / target | $74.22 | $40 | 3Y stock +77.4% | 실패 |
| 2018 adjusted EBITDA | $350m 이하 | miss/guide cut | $412m | 실패 |
| Fuel contribution | 15 cpg 이하 | normalization | 16.2 cpg | 실패 |
| SSS gallons | 지속 감소 | negative | FY -0.6%·Q4 +2.1% | 부분 성공 |
| Buyback | 중단 | covenant 제약 | Q1 $71.7m·이후 지속 | 실패 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2018-06-27 | VIC Short | $40 target |
| 2018-Q2 | estimate/guidance catalyst window | 단기 약세 기대 |
| 2018-FY | $412m adjusted EBITDA·16.2 cpg | 핵심 반증 |
| 2018-Q4 | same-store gallons +2.1% | volume 회복 |
| 2020 | COVID에서 fuel margin 구조 강화 | Short economics 악화 |
| 2021-01 | QuickChek acquisition | format diversification |
| 2021-06 | 3년 multiplier 1.774x | simple Short -77.4% |

### 실제 사업·자본구조

2018 full-year same-store volume은 약 -0.6%였지만 Q4 +2.1%로 돌아섰다. total fuel contribution은 16.2 cpg, adjusted EBITDA는 $412m로 Short의 15 cpg/$350m을 모두 웃돌았다. 회사는 2018 Q1에도 약 929k shares를 $71.7m에 매입했고 프로그램을 이어갔다. 이후 2020 fuel economics와 2021 QuickChek이 사업범위를 강화했다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

실제 Short 기준 simple price P&L은 1M -4.8%, 3M -14.4%, 6M +6.5%, 1Y -11.6%, 2Y -47.1%, 3Y -77.4%다. 6개월에는 cover 가능한 이익이 있었지만 thesis horizon을 늘리면 손실이 급증했다. borrow, 배당과 transaction cost를 제외한 1-multiplier 계산이다.

이 아이디어는 repository에 보존된 price multiplier를 실제 Short 방향으로 교정했다. Long은 multiplier-1, Short는 1-multiplier인 price-only 수익이며 배당·borrow·거래비용은 포함하지 않는다. 누락 horizon은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | SSS weakness | 20% | 부분 성공 | 같은 해 평균과 exit-rate를 함께 본다. |
| C2 | 15 cpg ceiling | 18% | 실패 | mean reversion 전 구조적 breakeven 변화를 확인한다. |
| C3 | $350m EBITDA | 18% | 실패 | target earnings에는 명확한 cover threshold를 둔다. |
| C4 | buyback stop | 16% | 실패 | covenant headroom을 실제 정의로 계산한다. |
| C5 | 6x proxy | 16% | 실패 | peer가 없으면 unit economics로 DCF를 먼저 만든다. |
| C6 | $40 payoff | 12% | 실패 | Short target은 earnings와 multiple의 독립 확률을 곱한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

6개월 수익은 volume·sentiment weakness가 만들었고, 손실은 예상보다 높은 fuel contribution과 EBITDA, 계속된 buyback, merchandise/format 개선이 만들었다. 가장 큰 오류는 6x와 $350m이라는 두 개의 낮은 가정을 곱해 target downside를 과장한 것이다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 $74.22 next-day close에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

CASY가 아니라 grocery losers를 relative multiple proxy로 사용했고, fuel contribution의 distribution과 industry breakeven behavior를 모델링하지 않았다. covenant를 buyback 중단과 바로 연결했으며 capex 후 cohort economics를 확인하지 않았다. 한 분기 miss와 terminal multiple을 혼합했다.

### 최초 관찰 가능한 경고/반증

2018 실적에서 adjusted EBITDA $412m, total fuel contribution 16.2 cpg가 확인된 순간 $350m/15 cpg base는 폐기해야 했다. Q4 same-store gallons +2.1%와 buyback 지속은 추가 cover signal이었다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** ticker MUSA만 보지 말고 Murphy USA Inc.의 법인·security·날짜로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Short을 확정한다.
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
| Entity / direction | raw Short → **Short**, Murphy USA Inc. |
| Business thesis | 실패 |
| Valuation thesis | 실패 |
| Catalyst / timing | 실패 — 6개월 +6.5% 후 1년 -11.6%, 3년 -77.4% simple short P&L |
| Thesis score | 3.8/10 |
| Process score | 7.2/10 |
| Outcome-adjusted score | 5.5/10 |

### 한 문장 교훈

> 같은 해 평균과 exit-rate를 함께 본다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL 원문/metadata — VIC_IDEAS(4).sql / VIC, 2018-06-27. idea_id·raw direction·description 11418 chars·catalyst 511 chars
2. [Murphy USA spin-off completion 8-K](https://www.sec.gov/Archives/edgar/data/1573516/000157351613000008/musa-20130905x8k.htm) — SEC / Murphy USA, 2013-08-30. Murphy Oil에서 1:4 배분으로 독립한 법인·security 경계
3. [Murphy USA 2017 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2018/Murphy-USA-Inc-Reports-Preliminary-Fourth-Quarter-2017-Results/default.aspx) — Murphy USA, 2018-02. 2017 gallons, fuel contribution, merchandise와 repurchase
4. [Murphy USA 2018 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2019/Murphy-USA-Inc-Reports-Preliminary-Fourth-Quarter-2018-Results/) — Murphy USA, 2019-02. 2018 adjusted EBITDA $412m, CPG와 same-store volume
5. [Murphy USA 2020 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2021/Murphy-USA-Inc.-Reports-Fourth-Quarter-2020-Results/default.aspx) — Murphy USA, 2021-02. COVID volume 충격, fuel economics와 $399.6m repurchase
6. [Murphy USA 2021 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2022/Murphy-USA-Inc.-Reports-Fourth-Quarter-2021-Results/default.aspx) — Murphy USA, 2022-02. QuickChek 첫해, record EBITDA와 $355m repurchase
7. [Murphy USA 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1573516/000157351626000090/musa-20251231.htm) — SEC / Murphy USA, 2026-02. 1,800 stores, 30.7 cpg, adjusted EBITDA $1,019.4m와 누적 $4.1bn repurchase

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **B** — repository multiplier를 실제 Short 방향으로 교정. price-only이며 누락 horizon은 null.
- 교정: ticker=MUSA, entity=Murphy USA Inc., raw=Short, research=Short.
