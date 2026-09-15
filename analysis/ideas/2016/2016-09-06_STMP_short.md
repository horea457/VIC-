# Stamps.com Inc. — 2016-09-06 — V9

> **Batch 056 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Short**으로 확정했다. Research as-of 2026-09-15.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Stamps.com Inc. / STMP |
| 실제 Security | **Common stock** |
| Idea ID | `d3dcfac9-be86-40f2-b862-24768133c133` |
| 게시일 / 작성자 | 2016-09-06 / avahaz |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Short** |
| 기준가격 | 원문 가격 미복원 |
| 원 horizon | 12~30개월 |
| 최종 판정 | **mechanism은 2019 적중했지만 2016 trade timing은 실패** |

> **결론:** USPS reseller/NSA 보상이 구조적으로 지속 불가능하고 약 $90m EBIT이 위험해 약 80% downside가 있다는 Short다. 실제 USPS monetization reset은 2019 발생했지만 그 전 2년 이상 고객·earnings·주가가 크게 성장했다. mechanism과 investable timing을 분리해야 한다. 결과적으로 **mechanism은 2019 적중했지만 2016 trade timing은 실패**.

---

## 1. 회사는 정확히 무엇을 하는가

Stamps.com은 USPS PC Postage에서 출발해 Endicia·ShipStation·ShipWorks·ShippingEasy·MetaPack을 묶은 shipping-software platform으로 확장했다. 현금엔진은 `유료고객×subscription/transaction ARPU+carrier·insurance·supplies monetization-CAC-support·processing-R&D-G&A-capex-tax`다. 2007년에는 SOHO postage 구독과 마케팅 cohort가 핵심이었지만 2016년 이후에는 e-commerce parcel volume, multi-carrier workflow, high-volume shipper와 partner economics가 더 중요했다. USPS 우편물 감소만으로 TAM을 정의하면 parcel software를 놓치고, 반대로 USPS reseller economics를 영구화하면 platform value를 과대평가한다.

### Security cash waterfall

고객이 지급한 subscription·transaction 현금에서 고객획득·서비스·기술투자·운전자본·이자·세금을 차감하고 debt와 계약상 senior claim을 먼저 지급한 뒤의 per-share 현금만 common payoff로 본다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

USPS reseller/NSA 보상이 구조적으로 지속 불가능하고 약 $90m EBIT이 위험해 약 80% downside가 있다는 Short다. 실제 USPS monetization reset은 2019 발생했지만 그 전 2년 이상 고객·earnings·주가가 크게 성장했다. mechanism과 investable timing을 분리해야 한다.

### Reverse expectations

원문 가격 미복원가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. USPS concentration — 20%

- **원문 주장:** reseller economics가 EBIT의 큰 부분이다.
- **T0 근거:** 약 $90m EBIT 추정
- **숨은 가정:** partner terms가 business 전체로 귀속된다.
- **사전 반증조건:** subscription/software residual이 크면 반증.
- **실제:** 2019 shock는 material
- **판정:** **성공**
- **재사용 교훈:** counterparty exposure를 profit bridge로 만든다.

### C2. terms unsustainable — 18%

- **원문 주장:** USPS가 보상을 낮출 경제적 유인이 있다.
- **T0 근거:** NSA/reseller structure
- **숨은 가정:** USPS가 계약상 실행할 수 있다.
- **사전 반증조건:** renewal 지속·volume benefit이면 반증.
- **실제:** 2019 reset
- **판정:** **성공/지연**
- **재사용 교훈:** 유인과 실행일을 분리한다.

### C3. 80% downside — 18%

- **원문 주장:** 보상 제거 시 equity 대부분이 사라진다.
- **T0 근거:** $90m stress
- **숨은 가정:** 고객과 software value도 훼손된다.
- **사전 반증조건:** migration·대체 monetization이면 반증.
- **실제:** 장기 residual이 큼
- **판정:** **실패**
- **재사용 교훈:** broken earnings와 남는 자산을 분리한다.

### C4. near-term catalyst — 16%

- **원문 주장:** 계약 변화가 investable horizon 안에 온다.
- **T0 근거:** 정책 risk
- **숨은 가정:** 12~30개월 내 formal action
- **사전 반증조건:** 공식 gate 부재면 반증.
- **실제:** 약 2.5년 뒤 발생
- **판정:** **실패**
- **재사용 교훈:** Short mechanism에는 expiry date가 필요하다.

### C5. growth masks risk — 16%

- **원문 주장:** reported growth가 low-quality partner economics다.
- **T0 근거:** 높은 ARPU와 acquired volume
- **숨은 가정:** 고객 retention과 alternatives가 약하다.
- **사전 반증조건:** customer·carrier diversification이면 반증.
- **실제:** 2016~18 성장 후 2020 회복
- **판정:** **혼합**
- **재사용 교훈:** quality risk도 KPI가 좋아지면 sizing을 줄인다.

### C6. Short payoff — 12%

- **원문 주장:** downside가 borrow·squeeze를 보상한다.
- **T0 근거:** 80% headline downside
- **숨은 가정:** carry 기간이 짧다.
- **사전 반증조건:** 주가·earnings 상승 지속이면 반증.
- **실제:** trade timing 실패
- **판정:** **실패**
- **재사용 교훈:** 나중에 맞은 사건으로 과거 Short를 성공 처리하지 않는다.

---

## 4. 당시 Valuation과 Payoff Structure

약 $90m EBIT을 제거하는 stress는 reseller economics가 갑자기 사라지고 고객·volume·subscription value도 보전되지 않는 경우다. 80% downside에는 P(change), effective date, migration retention, 대체 carrier monetization과 남는 software value를 곱해야 한다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Short 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | mechanism은 2019 적중했지만 2016 trade timing은 실패의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| EBIT at risk | 약 $90m | 소멸 | 2019 일부 reset | mechanism 성공 |
| Downside | 약 80% | 계약 변화 | software residual 큼 | 과대 |
| Timing | 12~30개월 | USPS reset | 2019 발생 | 지연/실패 |
| Customer/ARPU | 성장 위험 | 둔화 | 2016~18 성장 | 반증 |
| Residual platform | 낮게 평가 | 제한적 | multi-carrier 가치 확대 | 실패 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2015 | Endicia 인수 | USPS exposure 확대 |
| 2016-09-06 | VIC Short | $90m EBIT risk |
| 2017 | 고객·ARPU 증가 | 첫 trade 반증 |
| 2018 | earnings·shipping 성장 | Short duration 악화 |
| 2019-02 | USPS strategy reset | mechanism 현실화 |
| 2019 | guidance shock | 주가 충격 |
| 2020-2021 | multi-carrier 회복·sale | residual value 확인 |

### 실제 사업·자본구조

2016~18 회사는 shipping growth와 인수 platform을 통해 earnings를 확대했다. 2019 USPS 관계 reset과 guidance shock가 발생해 구조적 의존성은 뒤늦게 드러났다. 그러나 Short는 그 전 duration·squeeze·borrow 비용을 버텨야 했으므로 원 horizon의 trade는 실패다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

현재 SQL에는 catalyst 57자만 있고 description·performance COPY는 없다. $90m EBIT risk와 80% downside는 scenario anchor이며 exact Short return·borrow cost·IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | USPS concentration | 20% | 성공 | counterparty exposure를 profit bridge로 만든다. |
| C2 | terms unsustainable | 18% | 성공/지연 | 유인과 실행일을 분리한다. |
| C3 | 80% downside | 18% | 실패 | broken earnings와 남는 자산을 분리한다. |
| C4 | near-term catalyst | 16% | 실패 | Short mechanism에는 expiry date가 필요하다. |
| C5 | growth masks risk | 16% | 혼합 | quality risk도 KPI가 좋아지면 sizing을 줄인다. |
| C6 | Short payoff | 12% | 실패 | 나중에 맞은 사건으로 과거 Short를 성공 처리하지 않는다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

논지의 좋은 부분은 hidden counterparty concentration을 EBIT로 번역한 점이다. 실패는 contract change의 날짜와 전환경로를 제시하지 못하고 2016 growth를 무시한 것이다. 2019 shock는 mechanism 확인이지 2016 Short의 자동 성공이 아니다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 원문 가격 미복원에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

USPS가 경제성을 바꿀 유인은 봤지만 company와 customers의 migration option, carrier diversification과 software franchise residual을 거의 0으로 뒀다. Short에는 6~12개월짜리 observable contract gate가 필요했다.

### 최초 관찰 가능한 경고/반증

USPS 공지·계약 renewal·회사 disclosure에서 보상조건 변경일이 12개월 내 특정되지 않고, paid customers·ARPU가 두 분기 연속 성장하면 Short를 닫는다. 반대로 partner revenue concentration이 커지며 formal notice가 나오면 재진입한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `STMP`를 단일 회사명으로 보지 말고 Stamps.com Inc. 법인·날짜·security로 고정한다.
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
| Entity / direction | raw Short → **Short**, Stamps.com Inc. |
| Business thesis | 성공/지연 |
| Valuation thesis | mechanism 성공 |
| Catalyst / timing | mechanism은 2019 적중했지만 2016 trade timing은 실패 |
| Thesis score | 5.2/10 |
| Process score | 8.0/10 |
| Outcome-adjusted score | 6.6/10 |

### 한 문장 교훈

> counterparty exposure를 profit bridge로 만든다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata와 prior curated overlay](https://www.valueinvestorsclub.com/idea/STAMPS.COM_INC/1523234195) — VIC_IDEAS(4).sql / VIC / repository prior overlay, 2016-09-06. idea_id·raw Short·catalyst 57 chars·description absent; 현재 SQL에 없는 원문 anchor는 lower-provenance overlay로 분리
2. [Stamps.com SEC archive](https://www.sec.gov/edgar/browse/?CIK=1082923&owner=exclude) — SEC / Stamps.com, 1999-2021. 사업모델·고객·인수·USPS 관계·자본배분 연속성
3. [Stamps.com 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/1082923/000114420405007345/stampscom10k.htm) — SEC / Stamps.com, 2005-03. 초기 PC postage·NetStamps·고객획득 economics
4. [Stamps.com 2016 Form 10-K](https://www.sec.gov/Archives/edgar/data/1082923/000114036117010000/form10k.htm) — SEC / Stamps.com, 2017-03. Endicia 포함 고객·ARPU·shipping revenue와 비용
5. [Stamps.com 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1082923/000108292321000033/stmp-20201231.htm) — SEC / Stamps.com, 2021-03. 2020 revenue·paid customers·multi-carrier segment 검증
6. [Thoma Bravo acquisition release](https://www.sec.gov/Archives/edgar/data/1082923/000114036121023931/brhc10026739_ex99-1.htm) — SEC / Stamps.com, 2021-07-09. $330/share·약 $6.6bn terminal event
7. [USPS PC Postage](https://postalpro.usps.com/operations/pc-postage) — U.S. Postal Service, 2000s-2026. PC Postage 승인·운영 framework

### 데이터 품질

- 원문·metadata: **C** — 첨부 SQL에는 catalyst만 있고 description은 없다. date·author·raw flag와 원문 수치는 prior curated overlay로 provenance를 분리했다.
- 기업·사건: **A/B** — SEC·회사·USPS 자료로 operating KPI와 terminal event를 교차검증했다.
- 가격성과: **C** — 현재 SQL에 performance COPY가 없다. WTW legacy 값 4건은 ticker contamination으로 폐기했고 corporate event를 exact return으로 바꾸지 않았다.
- 교정: ticker=STMP, entity=Stamps.com Inc., raw=Short, research=Short.
