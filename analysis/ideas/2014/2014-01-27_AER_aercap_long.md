# AerCap Holdings N.V. (AER) — 2014-01-27 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AerCap Holdings N.V. / AER |
| VIC 게시일 / 작성자 | 2014-01-27 / jso1123 |
| 분석 증권 / 실제 방향 | NYSE:AER common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 원문 약 $43대 |
| 기대기간 | 약 24개월 |
| raw horizon audit | $60.50 target·2016 EPS $5.50 |
| 최종 판정 | **사업·EPS 성공 / 주가·multiple timing 실패** |

> **결론:** ILFC 인수는 fleet·funding·EPS accretion을 실현했고 2016 diluted EPS $5.52는 원문 $5.50과 거의 완벽히 일치했다. 하지만 uploaded SQL price-only return은 1Y +8.8%, 2Y -18.4%, 5Y +26.3%여서 24개월 $60.50 rerating은 실패했다. 정확한 earnings forecast와 좋은 stock call은 별개의 가설이다.

---

## 1. 회사는 정확히 무엇을 하는가

AerCap은 항공기를 OEM 또는 sale-leaseback으로 취득해 항공사에 장기 임대하는 항공금융회사다. lease rent와 maintenance receipts에서 funding cost·감가상각·관리비·credit loss를 뺀 spread, 그리고 재임대·매각 residual value가 ROE를 결정한다. 이동 가능한 자산이어도 기종·연식·정비상태와 레버리지가 equity tail risk를 만든다.

`lease revenue + maintenance + gain on sale - interest - depreciation - credit loss - opex - tax = equity earnings`; book value를 실제 판매 gain과 손실로 검증한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

lease yield, funding cost, utilization, collections, gain on sale, impairments, debt/equity, secured debt, book/share, ROE, buybacks

---

## 2. 당시 상황과 시장이 가격에 넣은 것

AIG의 forced sale로 AerCap이 ILFC를 취득해 fleet를 327대에서 약 1,300대로 확대하고 3년 lease revenue의 약 80%를 계약했다고 봤다. cost·tax·funding synergy와 leverage 감소로 ROE 15~17%, 2016 EPS $5.50, 약 11x P/E의 $60.50을 24개월 target로 제시했다.

### Reverse expectations

시장은 높은 debt/equity, aircraft residual value, airline credit, integration·refinancing과 lessor 업종의 persistent P/B discount를 반영했다. EPS가 맞아도 book quality와 tail risk가 재평가되지 않으면 multiple은 오르지 않는다.

---

## 3. 원문 투자논지 지도

### C1. ILFC acquisition이 큰 EPS accretion — 강한 성공

**원문 주장**

forced sale price와 scale로 EPS가 크게 늘어난다.

**경제적 메커니즘**

lease revenue·order book·overhead scale이 주당 earnings를 높인다.

**T0 근거**

327→~1,300 aircraft·contracted revenue.

**숨은 가정**

integration·credit·funding이 계획대로다.

**사전 반증조건**

2016 EPS가 $5.50에 크게 미달하면 반증.

**실제 결과**

2016 diluted EPS $5.52.

**정량 gap**

+$0.02/+0.4%.

**분석 오류 또는 제한**

EPS 적중을 stock thesis 적중으로 확장했다.

**재사용 교훈**

earnings와 multiple claim을 독립 score한다.

### C2. cost·tax·funding synergy — 성공

**원문 주장**

ILFC의 funding을 repricing하고 overhead·tax를 낮춘다.

**경제적 메커니즘**

scale·credit access가 interest와 opex를 줄인다.

**T0 근거**

deal financing·revolver·note plan.

**숨은 가정**

capital markets와 rating이 열려 있다.

**사전 반증조건**

funding cost 상승·liquidity shortfall이면 반증.

**실제 결과**

deal close와 후속 earnings가 synergy 실현을 지지했다.

**정량 gap**

각 synergy bucket exact 공개 제한.

**분석 오류 또는 제한**

gross synergy와 balance-sheet risk를 같은 방향으로만 봤다.

**재사용 교훈**

funding synergy는 spread·maturity·secured mix로 검증한다.

### C3. leverage가 낮아짐 — 방향 성공

**원문 주장**

retained earnings·asset sales로 debt/equity를 약 4x 방향으로 낮춘다.

**경제적 메커니즘**

FCF와 sale proceeds가 equity base를 키우고 debt를 줄인다.

**T0 근거**

pro forma high leverage.

**숨은 가정**

residual loss·buyback이 deleveraging을 막지 않는다.

**사전 반증조건**

debt/equity 정체·상승이면 반증.

**실제 결과**

integration 뒤 deleveraging과 refinancing이 진행됐다.

**정량 gap**

later GECAS로 다시 규모·leverage 변화.

**분석 오류 또는 제한**

metric definition과 target date가 모호했다.

**재사용 교훈**

gross debt, net debt, debt/equity를 날짜별로 고정한다.

### C4. 15~17% ROE가 11x P/E를 지지 — 부분 실패

**원문 주장**

quality ROE가 normal financial multiple을 받는다.

**경제적 메커니즘**

지속 ROE와 book compounding이 risk discount를 줄인다.

**T0 근거**

pro forma ROE·book value.

**숨은 가정**

시장에 residual·tail·funding discount가 사라진다.

**사전 반증조건**

EPS hit에도 P/E·P/B가 낮으면 반증.

**실제 결과**

EPS는 맞았지만 2Y stock -18.4%로 rerating이 오지 않았다.

**정량 gap**

multiple component 실패.

**분석 오류 또는 제한**

accounting ROE를 low-risk ROE로 봤다.

**재사용 교훈**

ROE를 leverage·gain on sale·impairment로 분해한다.

### C5. $60.50 within ~2 years — 실패

**원문 주장**

$5.50 EPS × 11x로 target를 달성한다.

**경제적 메커니즘**

earnings와 multiple이 동시에 실현된다.

**T0 근거**

explicit target.

**숨은 가정**

deal close 뒤 risk discount가 빠르게 축소된다.

**사전 반증조건**

2Y return이 음수면 실패.

**실제 결과**

2Y price-only -18.4%.

**정량 gap**

target 방향과 반대.

**분석 오류 또는 제한**

time arbitrage의 시간이 너무 짧았다.

**재사용 교훈**

catalyst가 earnings인지 market perception인지 구분한다.

### C6. discounted book buybacks가 accretive — 성공

**원문 주장**

book 이하 자사주 매입이 per-share book·EPS를 높인다.

**경제적 메커니즘**

자산 기대수익보다 높은 yield로 own shares를 산다.

**T0 근거**

deal 뒤 large share base·AIG stake.

**숨은 가정**

book가 보수적이고 liquidity가 충분하다.

**사전 반증조건**

impairments 또는 funding stress가 buyback accretion을 상쇄하면 반증.

**실제 결과**

2015~16 buybacks와 per-share earnings가 확대됐다.

**정량 gap**

tail risk는 후일 COVID·러시아에서 확인.

**분석 오류 또는 제한**

book quality stress보다 arithmetic accretion을 앞세웠다.

**재사용 교훈**

buyback은 stressed book와 liquidity buffer 뒤 계산한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문은 pro forma book 약 1.2x, ROE 15~17%, 2016 EPS $5.50에 11x를 적용했다. 이를 earnings claim과 multiple claim으로 분리하면 EPS는 적중했지만 11x rerating은 실패했다. lessor valuation은 P/E뿐 아니라 P/B, gain on sale, funding spread, stress asset haircut과 debt/equity를 함께 봐야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | integration·funding stress·0.8x book | $30대 | 2Y -18.4% |
| Base | $5.50 EPS·11x | $60.50 | EPS만 적중 |
| Long bull | buyback·scale·deleveraging | 장기 appreciation | 5Y +26.3% |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2016 diluted EPS | $5.50 | $5.50 | $5.52 | +0.4%/성공 |
| Fleet | 327+ILFC ~1,002 | ~1,300 | deal close ~1,300 | 성공 |
| Deal consideration | modeled | close | $3.0bn cash+97.56m shares | 성공 |
| 2Y price-only | 상승/$60.50 | ~+40% | -18.4% | 실패 |
| 5Y price-only | 장기 upside | 상승 | +26.3% | 부분 |

### 촉매와 시간

판정 horizon은 **약 24개월**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2014-01-27 | VIC Long 게시 | $60.50·$5.50 EPS |
| 2014-02-13 | shareholder approval | closing risk 감소 |
| 2014-05-14 | ILFC close | $3.0bn+97.56m shares |
| 2014-07-11 | Q2 122 aircraft transactions | integration activity |
| 2015~16 | buybacks·deleveraging | per-share accretion |
| 2016-01-27 | 2Y return -18.4% | target failure |
| 2016-12-31 | diluted EPS $5.52 | earnings thesis hit |
| 2021-11-01 | GECAS close | platform scale 재확대 |
| 2022 | 러시아 asset claims | tail-risk stress |
| 2023 | insurance settlements·travel recovery | long-duration resilience |

### 실제 사업·자본구조 추이

2014-05-14 거래가 종결됐고 AerCap은 AIG에 $3.0bn cash와 97,560,976 shares를 지급했다. 약 $45bn assets·1,300 aircraft platform이 됐고 financing facilities도 확대됐다. 2016 diluted EPS는 $5.52였다. 이후 buyback과 deleveraging을 했지만 업종 multiple은 낮았고, 장기에는 COVID·GECAS·러시아 asset seizure 같은 tail을 견뎠다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

uploaded SQL price-only ratios는 1Y 1.0879, 2Y 0.8162, 3Y 1.1925, 5Y 1.2631이다. 즉 1Y +8.8%, 2Y -18.4%, 3Y +19.2%, 5Y +26.3%이며 dividend·buyback benefit은 별도다. 24개월 target call은 명백히 실패했다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | ILFC acquisition이 큰 EPS accretion | 20% | 강한 성공 | +$0.02/+0.4%. |
| C2 | cost·tax·funding synergy | 18% | 성공 | 각 synergy bucket exact 공개 제한. |
| C3 | leverage가 낮아짐 | 18% | 방향 성공 | later GECAS로 다시 규모·leverage 변화. |
| C4 | 15~17% ROE가 11x P/E를 지지 | 16% | 부분 실패 | multiple component 실패. |
| C5 | $60.50 within ~2 years | 16% | 실패 | target 방향과 반대. |
| C6 | discounted book buybacks가 accretive | 12% | 성공 | tail risk는 후일 COVID·러시아에서 확인. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

사업가치는 ILFC의 규모·order book·funding synergy와 buyback이 만들었다. 24개월 주가부진은 레버리지·residual-value tail과 업종 P/B discount가 earnings accretion을 상쇄한 결과다.

### Counterfactual

2016 EPS가 정확히 $5.50이어도 P/E 7x·P/B 0.8x이면 24개월 downside와 target IRR은 얼마인가?

---

## 9. 분석 오류 유형과 최초 경고

deal EPS accretion을 valuation-regime change와 직결하고, aircraft asset haircut·funding spread가 multiple에 남길 영구 discount를 작게 봤다.

### 최초로 관찰 가능했던 경고신호

2016-01-27 2년 price-only -18.4%가 target horizon 실패를 확정했으며 EPS miss가 아니라 multiple miss였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

M&A earnings accretion과 valuation multiple rerating을 별도 claim으로 둔다.

### Lesson 2

levered asset financier는 P/E보다 asset haircut 뒤 P/B·funding liquidity를 먼저 본다.

### Lesson 3

EPS가 정확해도 security return이 실패할 수 있다.

### 지금 같은 아이디어를 다시 본다면

- lease yield-funding cost
- utilization·collections
- gain on sale
- impairment
- debt/equity
- unsecured liquidity
- book/share
- buyback below book
- P/E·P/B separate

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 강한 성공 |
| EPS thesis | 강한 성공 |
| Valuation thesis | 실패 |
| Timing / path | 2년 실패 |
| Security selection | common duration 과소평가 |
| Thesis score | 7.4/10 |
| Process score | 9.8/10 |
| 종합 | **사업·EPS 성공 / 주가·multiple timing 실패** |

### 한 문장 교훈

> M&A earnings accretion과 valuation multiple rerating을 별도 claim으로 둔다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/AERCAP_HOLDINGS_NV/4527154442) — Value Investors Club / source SQL, 2014-01-27. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [AerCap shareholders approve ILFC acquisition](https://www.aercap.com/news-media/press-releases/detail/300/aercap-holdings-n-v-shareholders-approve-acquisition-of) — AerCap, 2014-02-13. deal 승인과 closing condition 검증.
3. [AerCap completes ILFC acquisition](https://www.aercap.com/news-media/press-releases/detail/309/aercap-completes-acquisition-of-ilfc-from-aig-and-closes) — AerCap, 2014-05-14. $3.0bn cash·97,560,976 shares·46% AIG stake·financing 검증.
4. [AerCap Q2 2014 aircraft transactions](https://www.aercap.com/news-media/press-releases/detail/310/aercap-holdings-n-v-completed-122-aircraft-transactions) — AerCap, 2014-07-11. ILFC 통합 직후 fleet activity 검증.
5. [AerCap 2016 Form 20-F](https://www.sec.gov/Archives/edgar/data/1378789/000137878917000009/aer-20161231x20f.htm) — SEC / AerCap, 2017-03-06. 2016 diluted EPS $5.52, fleet·funding·book value 검증.
6. [AerCap 2022 Form 20-F](https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-23-000006/aer-20221231.htm) — AerCap, 2023-03-02. COVID·GECAS·러시아 자산손실 이후 재무구조 검증.
7. [AerCap Q1 2022 results](https://www.aercap.com/news-media/press-releases/detail/415/aercap-holdings-n-v-reports-financial-results-for-the) — AerCap, 2022-05-17. 러시아 자산 관련 약 $3.5bn 보험청구 검증.
8. [AerCap 2023 Form 20-F](https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-24-000010/aer-20231231.htm) — AerCap, 2024-02-23. fleet·부채·러시아 보험합의·book recovery 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B** — source SQL price-only ratios; dividends·tax 제외.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
