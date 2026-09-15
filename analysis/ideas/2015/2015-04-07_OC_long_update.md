# Owens Corning — 2015-04-07 — V9

> **Batch 053 canonical report.** Raw SQL `Long`를 원문 action/payoff로 감사해 **Long Update**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Owens Corning / OC |
| 실제 Security | **Common stock** |
| Idea ID | `8a1f7ef6-2064-40ff-95d9-aeaec1336894` |
| 게시일 / 작성자 | 2015-04-07 / booM() |
| 원 SQL 방향 | Long |
| 원문 검증 방향 | **Long Update** |
| 기준가격 | 2015-01-06 이후 약 +17% (선행 metadata) |
| 원 horizon | 6~18개월 |
| 최종 판정 | **channel 방향·earnings 성공, realized-price 가정 부분 실패·정확 수익률 미검증** |

> **결론:** 1월 6일 Long을 업데이트한 별도 idea unit이다. 일부 지역 roofing flux가 약 30% 하락했고, OC의 asphalt 구매가 이미 진행됐으며, winter discount/rebate가 거의 없고 distributor inventory가 낮아 May price increase가 가능하다고 봤다. price letter보다 cost·inventory·survey라는 near-term evidence를 추가했다. 결과적으로 **channel 방향·earnings 성공, realized-price 가정 부분 실패·정확 수익률 미검증**.

---

## 1. 회사는 정확히 무엇을 하는가

Owens Corning은 당시 Roofing, Insulation, Composites 세 축의 건자재 제조사였다. 현금엔진은 `출하량×실현가격-asphalt·glass·energy·freight-plant fixed cost-SG&A-운전자본-capex-interest·tax`다. Roofing은 replacement/storm demand와 asphalt spread, Insulation은 housing starts·capacity utilization·price/cost, Composites는 산업생산·utilization·mix가 수익을 좌우한다. 높은 고정비 때문에 trough multiple보다 segment별 정상 출하·margin과 다음 downturn의 현금전환을 함께 봐야 한다. 2006 재편 뒤 asbestos 청구는 trust로 이전됐지만 영업 cycle은 그대로 common에 남았다.

### Security cash waterfall

Segment operating cash에서 운전자본·maintenance/growth capex·interest·tax를 차감한다. normalized EBITDA와 historical margin은 현금이 아니며, cycle trough까지 필요한 자본과 구조조정비를 먼저 뺀다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

1월 6일 Long을 업데이트한 별도 idea unit이다. 일부 지역 roofing flux가 약 30% 하락했고, OC의 asphalt 구매가 이미 진행됐으며, winter discount/rebate가 거의 없고 distributor inventory가 낮아 May price increase가 가능하다고 봤다. price letter보다 cost·inventory·survey라는 near-term evidence를 추가했다.

### Reverse expectations

2015-01-06 이후 약 +17% (선행 metadata)가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. flux 하락 — 20%

- **원문 주장:** roofing asphalt input가 약 30%까지 하락한다.
- **T0 근거:** 지역 supplier quote
- **숨은 가정:** blended OC purchase cost에 반영된다.
- **사전 반증조건:** FY saving<$35m이면 반증.
- **실제:** $68m benefit
- **판정:** **성공**
- **재사용 교훈:** quote를 weighted realized cost로 변환한다.

### C2. inventory shortage — 18%

- **원문 주장:** 낮은 distributor 재고가 가격을 지지한다.
- **T0 근거:** channel survey
- **숨은 가정:** sell-through가 유지된다.
- **사전 반증조건:** inventory build·rebate 재개면 반증.
- **실제:** price는 실제 하락
- **판정:** **부분 실패**
- **재사용 교훈:** 재고와 invoice price를 함께 본다.

### C3. winter discipline — 18%

- **원문 주장:** rebate 부재가 industry behavior 변화를 뜻한다.
- **T0 근거:** manufacturer/distributor checks
- **숨은 가정:** 경쟁사가 share를 위해 이탈하지 않는다.
- **사전 반증조건:** discount 재도입이면 반증.
- **실제:** cost 우위는 남았지만 price 고정 실패
- **판정:** **부분**
- **재사용 교훈:** 일시 행동과 구조 discipline을 구분한다.

### C4. May price hike — 16%

- **원문 주장:** announced 인상이 실현된다.
- **T0 근거:** letters·survey
- **숨은 가정:** customer가 수용한다.
- **사전 반증조건:** realized price negative면 반증.
- **실제:** FY price -$114m
- **판정:** **실패**
- **재사용 교훈:** price letter는 catalyst가 아니라 가설이다.

### C5. earnings update — 16%

- **원문 주장:** 추가 증거가 consensus beat를 높인다.
- **T0 근거:** cost·inventory chain
- **숨은 가정:** 타 segment가 상쇄하지 않는다.
- **사전 반증조건:** EPS<$2.30이면 반증.
- **실제:** $2.57
- **판정:** **성공**
- **재사용 교훈:** update는 새 evidence의 incremental value를 기록한다.

### C6. payoff compression — 12%

- **원문 주장:** 17% 상승 뒤에도 충분한 upside가 남는다.
- **T0 근거:** $50 기존 target
- **숨은 가정:** target multiple이 유지된다.
- **사전 반증조건:** remaining upside<15%면 반증.
- **실제:** 정확 entry/path 없음
- **판정:** **미검증**
- **재사용 교훈:** 후속 글은 가격상승 뒤 EV를 다시 계산한다.

---

## 4. 당시 Valuation과 Payoff Structure

이 update는 새 terminal multiple보다 기존 `$2.30 consensus+$0.50 asphalt benefit→$2.80 EPS×18=$50`의 확률을 높였다. 1월 이후 약 +17%는 선행 metadata이며 정확 가격은 복원하지 않는다. update 시점에서는 이미 오른 가격 때문에 upside가 줄었으므로 expected value는 realized selling price가 flat인지에 더 민감해졌다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long Update 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | channel 방향·earnings 성공, realized-price 가정 부분 실패·정확 수익률 미검증의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Idea status | 1월 Long update | 확률 상향 | Long으로 일관 | 성공 |
| Asphalt flux | 일부 지역 -30% | cost benefit | FY15 +$68m | 성공 |
| Distributor inventory | 낮음 | flat/up price | selling price -$114m | 부분 실패 |
| Roofing EBIT | 개선 기대 | +$34m | +$34m | 성공 |
| FCF | $50m prior year | 현금전환 | $341m | 강한 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2015-01-06 | 원 Long | $50 framework |
| 2015-Q1 | flux·inventory channel check | evidence 강화 |
| 2015-04-07 | VIC update | 약 +17% 뒤 |
| 2015-05 | price increase letters | announced catalyst |
| 2015 | selling price 감소 | channel claim 반증 |
| 2015 | asphalt benefit·FCF 개선 | earnings 성공 |
| 2016-02 | FY15 공시 | realized bridge |

### 실제 사업·자본구조

2015 공식 결과에서 asphalt cost deflation $68m과 FCF $341m은 Long을 지지했다. 그러나 selling price는 $114m 감소해 survey와 price-increase letter가 실제 invoice price를 완전히 예측하지 못했다. Roofing EBIT +$34m·adjusted EPS $2.57로 방향은 성공했지만 pricing claim은 부분 실패다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

첨부 SQL에서 이 idea는 catalyst가 `.` 한 글자이고 description·performance도 없다. 기존 초안의 수익률은 전부 폐기한다. 후속 원문 성격과 약 +17% 진행은 prior curated metadata 등급으로만 남기며 exact return/IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | flux 하락 | 20% | 성공 | quote를 weighted realized cost로 변환한다. |
| C2 | inventory shortage | 18% | 부분 실패 | 재고와 invoice price를 함께 본다. |
| C3 | winter discipline | 18% | 부분 | 일시 행동과 구조 discipline을 구분한다. |
| C4 | May price hike | 16% | 실패 | price letter는 catalyst가 아니라 가설이다. |
| C5 | earnings update | 16% | 성공 | update는 새 evidence의 incremental value를 기록한다. |
| C6 | payoff compression | 12% | 미검증 | 후속 글은 가격상승 뒤 EV를 다시 계산한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

edge는 upstream asphalt quote, manufacturer buying, distributor inventory와 rebate를 한 chain으로 연결한 점이다. 손익은 price 고정보다 cost decline이 price decline을 얼마나 앞섰는지에서 나왔다. update는 conviction을 높였지만 valuation margin은 초기 글보다 좁아졌다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 2015-01-06 이후 약 +17% (선행 metadata)에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

channel 응답과 announced price increase를 realized price로 취급했다. 지역별 flux -30%가 OC blended cost에 그대로 들어오지 않고 inventory layer·contract lag가 있다. 이미 +17% 오른 뒤에도 payoff를 같은 $50로 둬 upside compression을 명시적으로 다시 계산하지 않았다.

### 최초 관찰 가능한 경고/반증

Q2/Q3 price-volume bridge에서 selling-price decline이 asphalt saving보다 크거나, distributor 재고일수가 정상 이상으로 오르면 price-increase letter와 무관하게 Long update를 철회한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `OC`를 단일 회사로 보지 말고 Owens Corning 법인·날짜·실제 security로 고정한다.
2. **Direction audit:** raw Long가 아니라 원문 payoff를 읽어 Long Update을 확정한다.
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
| Entity / direction | raw Long → **Long Update**, Owens Corning |
| Business thesis | 부분 실패 |
| Valuation thesis | 성공 |
| Catalyst / timing | channel 방향·earnings 성공, realized-price 가정 부분 실패·정확 수익률 미검증 |
| Thesis score | 8.0/10 |
| Process score | 9.3/10 |
| Outcome-adjusted score | 8.7/10 |

### 한 문장 교훈

> quote를 weighted realized cost로 변환한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL catalyst / prior curated metadata — VIC_IDEAS(4).sql / VIC / repository prior overlay, 2015-04-07. idea_id·catalyst 1 chars·description absent; date·author·raw flag·원문 anchor는 prior overlay 대조
2. [Owens Corning SEC filing archive](https://www.sec.gov/edgar/browse/?CIK=1370946&owner=exclude) — SEC / Owens Corning, 2006-2026. 재편 뒤 10-K·8-K와 segment·capital allocation 연속성
3. [Owens Corning 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/1370946/000119312508040193/d10k.htm) — SEC / Owens Corning, 2008-02-27. housing downturn·Saint-Gobain composites 인수·segment economics
4. [Owens Corning 2013 results](https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2014/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2013-Results/default.aspx) — Owens Corning, 2014-02-12. adjusted EBIT·EPS·Roofing·Insulation와 dividend
5. [Owens Corning 2015 results](https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2016/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2015-Results/default.aspx) — Owens Corning, 2016-02-10. asphalt cost·selling price·volume/mix와 FCF bridge
6. [Owens Corning 2017 results](https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2018/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2017-Results/default.aspx) — Owens Corning, 2018-02-21. 세 segment EBIT·operating cash·FCF
7. [Owens Corning 2018 results](https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2019/Owens-Corning-Reports-Fourth-Quarter-and-Full-Year-2018-Results/default.aspx) — Owens Corning, 2019-02-20. 2018 input-cost/storm 환경과 segment 결과
8. [Owens Corning 2019 results](https://investor.owenscorning.com/investors/stock-performance-and-earnings/press-releases/press-release-details/2020/Owens-Corning-Reports-Full-Year-and-Fourth-Quarter-2019-Results/default.aspx) — Owens Corning, 2020-02-19. 2019 Roofing EBIT·operating cash·FCF

### 데이터 품질

- 원문·metadata: **B/C** — 첨부 SQL에는 catalyst 10건과 description 1건만 있다. 누락된 date·author·raw flag·원문 수치는 prior curated overlay를 별도 provenance로 대조했다.
- 기업·사건: **A/B** — SEC·회사 IR·감사보고서로 segment 결과와 후속 사건을 검증했다.
- 가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. 기존 overlay 성과값을 폐기하고 exact return/IRR을 모두 null로 재설정했다.
- 교정: ticker=OC, entity=Owens Corning, raw=Long, research=Long Update.
