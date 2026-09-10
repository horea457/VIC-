# Batch 057 — Weight Watchers / Asbury Automotive / Advanced Emissions Solutions V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 056 마지막 WTW 2014-02-22 이후, reviewed idea_id를 제외한 다음 10건.
> **핵심 데이터 품질:** raw direction 교정 7건 + capital-structure pair security 교정 1건 + WTW ticker-performance contamination 지속.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2015-05-05 | WTW | Short | **Common Short + B-1 1st-lien loan Long** | [WTW Pair](ideas/2015/2015-05-05_WTW_capital_structure_pair.md) | **Credit 성공 / Equity 실패 / Pair 전체 혼합~실패** |
| 2 | 2015-11-10 | WTW | **Short** | Common **Long** | [WTW 2015 Long](ideas/2015/2015-11-10_WTW_long.md) | **stated 2016 horizon 실패 / 2~3년 성공** |
| 3 | 2018-12-11 | WTW | **Short** | Common **Long** | [WTW 2018 Long](ideas/2018/2018-12-11_WTW_long.md) | **10개월 horizon 강한 실패 / digital thesis 일부 성공** |
| 4 | 2008-04-24 | ABG | **Short** | Common **Long** | [ABG 2008](ideas/2008/2008-04-24_ABG_long.md) | **6M -78%, timing 강한 실패 / 5Y +133%** |
| 5 | 2010-03-12 | ABG | **Short** | Common **Long** | [ABG 2010](ideas/2010/2010-03-12_ABG_long.md) | **매우 강한 성공 — 5Y +460%** |
| 6 | 2020-02-18 | ABG | **Short** | Common **Long** | [ABG 2020 Feb](ideas/2020/2020-02-18_ABG_long.md) | **1M -50.5% 후 3Y +144.2%** |
| 7 | 2020-09-10 | ABG | **Short** | Common **Long** | [ABG 2020 Sep](ideas/2020/2020-09-10_ABG_long.md) | **강한 성공 — 1Y +63.5%** |
| 8 | 2021-09-16 | ABG | **Short** | Common **Long** | [ABG 2021](ideas/2021/2021-09-16_ABG_long.md) | **사업확장 부분 성공 / $360 rerating 실패** |
| 9 | 2022-09-26 | ABG | Long | Common **Long** | [ABG 2022](ideas/2022/2022-09-26_ABG_long.md) | **부분 성공 / 5~10Y horizon 진행 중** |
| 10 | 2012-07-15 | ADES | Long | Common **Long** | [ADES 2012](ideas/2012/2012-07-15_ADES_long.md) | **cash-flow thesis 성공 / governance-security path 혼합** |

---

# PART A — Metadata / Security Audit

## 2. Direction corrections

### 실제 Long인데 raw Short인 7건
- WTW 2015-11
- WTW 2018-12
- ABG 2008
- ABG 2010
- ABG 2020-02
- ABG 2020-09
- ABG 2021

### Raw Long과 실제 Long 일치
- ABG 2022
- ADES 2012

### 단순 direction으로 표현하면 안 되는 1건
WTW 2015-05:
- **Short common equity**
- **Long Tranche B-1 first-lien term loan**

즉 한 row 안에 상반된 두 security leg가 있다.

## 3. WTW price-series contamination

BATCH 56에서 확인한 문제를 그대로 유지한다. Weight Watchers의 과거 ticker **WTW**는 후대 **Willis Towers Watson**에도 사용됐다.

따라서 DB raw performance는:
- 원본 보존
- audit trail 유지
- **Weight Watchers outcome 판정에는 사용하지 않음**

실제 historical price / SEC filing / event data를 별도로 사용한다.

---

# PART B — WEIGHT WATCHERS: 같은 기업에서 Credit과 Equity가 갈린다

## 4. WTW 2015-05 — Common Short + B-1 Loan Long

### Common Short 논리
- meetings decline
- online disruption
- high leverage
- B-2 distressed
- bankruptcy / refinancing risk

### B-1 Long 논리
- price 약 **89**
- principal 약 **$292.3m**
- maturity **2016-04-02**
- senior first-lien
- cash/revolver로 상환 가능

원문 Base:
- equity short contribution 약 +35%
- B-1 contribution 약 +16.4%
- total 약 **+52%**

## 5. 실제 결과는 security별로 완전히 다름

2015-10 Oprah Winfrey strategic investment:
- 약 6.36m shares
- 약 $43m
- 약 10% stake
- options
- board / collaboration

2016-04:
**B-1 잔액 $144.3m 전액 cash par repayment.**

| Leg | Thesis | 실제 |
|---|---|---|
| Common Short | bankruptcy / decline | **실패** |
| B-1 Long | near-term money-good | **강한 성공** |
| Combined pair | +52% 기대 | **정확한 sizing 없이는 IRR 미산출, 대체로 실패/혼합** |

> **기업 전망을 맞히는 것과 security payoff를 맞히는 것은 다르다.**

## 6. WTW 2015-11 Long — Oprah를 operating leverage로 번역

주가 약 $24.

원문:
- upside $87
- downside $16
- probability-weighted $50
- target date YE2016
- 1.5~2.0m incremental subscribers

핵심:
**subscriber additions × high fixed-cost platform = 큰 EBITDA leverage**

실제:
- YE2016 $50 target: 실패
- 2017~18 turnaround 가속
- 2018 subscriber base 약 4.6m
- 주가 2018 고점에서 $80~100 수준

### 판정
**시간은 틀리고 구조는 맞았다.**

## 7. WTW 2018 Long — digital thesis가 맞아도 주식은 실패할 수 있다

2018-12 약 $48.

원문:
- retention 개선
- average customer life 8 → 10개월
- net adds 둔화 과대반영
- ~$72.85 target
- 약 1.45x MOIC
- 대략 10개월 horizon

실제 2019:
- revenue -6.7%
- gross profit -9.2%
- recruiting weakness
- marketing execution 문제

그러나:
- YE2019 subscribers +8% to ~4.2m
- Digital subscribers ~3.0m
- early 2020 total members >5m

### 판정
**digital product thesis 일부 성공 / stock expectations·customer acquisition thesis 실패.**

## 8. WTW 시계열

| 시점 | 방향 | 가장 중요한 변수 | 결과 |
|---|---|---|---|
| 2014 Short | free apps / leverage | structural disruption | fundamental 성공 |
| 2015-05 pair | capital structure | senior maturity vs equity optionality | credit만 성공 |
| 2015-11 Long | Oprah / subscriber adds | customer-acquisition catalyst | 중기 성공 |
| 2018 Long | retention / digital | gross adds 둔화 | 단기 실패 |

Subscription consumer equity는 **retention**과 **gross additions**를 동시에 본다. LTV 개선만으로 신규 customer funnel 악화를 상쇄할 수 있다고 가정하지 않는다.

---

# PART C — ASBURY AUTOMOTIVE: 같은 회사, 다른 cycle entry

## 9. ABG 2008 Long — “14m SAAR가 바닥”이라는 오류

당시:
- price ~$14
- dividend yield ~6.4%
- consensus P/E ~7.5x
- recession EPS ~$1.47 at 14m SAAR
- normalized $2.50 × 15x = $37.50

좋은 insight:
- P&S + F&I 약 60% gross profit
- import/luxury mix
- dealer model이 headline unit sales보다 resilient

나쁜 assumption:
**14m SAAR가 deep recession floor.**

실제 2009 U.S. sales는 약 **10.3m**.

SQL:
- 6M **-78.0%**
- 1Y -48.9%
- 5Y +133.1%

## 10. ABG 2010 Long — 바닥을 예측하지 않고 바닥에서 살아남은 economics를 샀다

2009 EPS **$0.82**.

normalized bridge:
- +$0.95 unit recovery
- +$0.06 truck loss elimination
- +$0.20 SG&A efficiency

= **$2.03**

9~10x:
**$18~20**

### 결정적 차이
2008: “수요가 여기보다 더 안 내려갈 것이다.”

2010: “실제로 수요가 최악까지 내려갔는데 이 회사가 cost를 줄이고 다시 흑자가 났다.”

SQL:
- 1Y +32.1%
- 2Y +100.2%
- 3Y +171.8%
- **5Y +460.0%**

## 11. ABG 2008 vs 2010 — 이번 batch 최고의 비교

| 항목 | 2008 Long | 2010 Long |
|---|---|---|
| SAAR | forecast floor 14m | actual trough ~10m observed |
| earnings | modeled | stress-tested actual |
| cost structure | assumed | reset verified |
| downside | historical extrapolation | observed survival |
| 6M | -78% | -3.2% |
| 5Y | +133% | **+460%** |

> **사이클 바닥을 예측하는 것보다 바닥에서 실제로 살아남은 economics를 관찰하는 것이 훨씬 강한 정보다.**

## 12. ABG 2020-02 — COVID 직전 좋은 thesis, 극단적 path risk

원문:
- market cap ~$2bn
- EV ~$4bn
- PF revenue ~$9.4bn
- EBITDA ~$455m
- FCF ~$223m
- <10x EPS
- double-digit FCF yield
- Park Place accretion

게시 직후:
**1M -50.5%**

그 뒤:
- 6M +10.1%
- 1Y +62.4%
- 3Y +144.2%

회복 메커니즘:
- P&S resilience
- variable SG&A
- inventory scarcity → GPU 상승
- Park Place deal repricing
- franchise scarcity

## 13. ABG 2020-09 — 실제 stress test를 보고도 싸게 살 수 있었다

2020-02:
**resilience = hypothesis**

2020-09:
**resilience = observed fact**

원문:
- 2021E EPS ~$13
- Park Place ~$2.50/share
- ~8.5x P/E
- luxury mix 확대

SQL:
- 1Y **+63.5%**
- 2Y +66.5%

### 교훈
최저가를 맞히지 않아도, **불확실성이 줄었는데 multiple이 여전히 낮으면 더 좋은 risk-adjusted entry**가 될 수 있다.

---

# PART D — ABG Roll-up: 2021 vs 2022

## 14. ABG 2021 Long — 규모 성장과 주당가치 성장은 다르다

원문:
- 2025 revenue ~$20bn
- normalized EPS ~$33
- margins 유지 시 ~$43
- 11x → **$360**
- owned real estate net value ~$430m
- Clicklane
- M&A runway

LHM/TCA:
- ~$3.48bn transaction
- 54 new dealerships
- 7 used
- 11 collision
- ~$5.7bn annualized revenue

실제:
2022:
- revenue ~$15.4bn
- adjusted EPS ~$37.66

2025:
- revenue ~$18.0bn
- adjusted EPS ~$28.10

판정:
- scale execution: 성공
- 2025 revenue target: 미달
- $360 rerating: 실패
- 2022 peak EPS 지속: 실패

## 15. ABG 2022 Long — overearning과 EV terminal fear를 직접 다룸

시장 공포:
1. peak vehicle GPU normalizes
2. EV direct-to-consumer가 dealer를 없앤다

writer:
- P&S / F&I / used / financing / trade-in 기능은 지속
- normalized FCF **$30~50/share**
- stock 약 3~5x
- conservative 2025 revenue ~$20bn
- 5~10Y horizon

실제 2025:
- revenue ~$18bn
- adjusted EPS ~$28.10
- adjusted operating cash flow ~$651m

판정:
- dealership terminal value collapse: 아직 발생 안 함
- business durability: 확인
- revenue target: 미달
- 5~10Y thesis: **진행 중**

## 16. ABG 전체 시계열

| 시점 | Thesis style | 결과 |
|---|---|---|
| 2008 | SAAR bottom forecast | path failure |
| 2010 | observed trough economics | 매우 성공 |
| 2020-02 | quality / P&S / M&A | 큰 drawdown 후 성공 |
| 2020-09 | post-stress evidence | 강한 성공 |
| 2021 | roll-up / growth target | business partial, rerating miss |
| 2022 | normalized FCF / terminal-risk rebuttal | partial / ongoing |

분석의 질이 좋아진 방향:
**macro forecast → segment economics → observed stress → normalized per-share FCF**

---

# PART E — ADES 2012: Cash Flow는 맞았는데 Security Path는 왜 복잡했나

## 17. ADES의 두 가치엔진

### Emission Control
MATS 규제:
- ACI
- DSI
- mercury / acid-gas controls

### Refined Coal
Section 45:
- 약 $6.47/ton tax credit in 2012
- qualified facilities
- monetizer
- JV
- ADA distributions

원문은 ADA economic share를 약 **$1.50~1.70/ton**으로 추정.

## 18. 원문 Refined Coal model

- facilities ramp
- cash ~$1.50/ton
- run-rate:
  - 2012 ~$30m
  - 2013 ~$80m
  - 2014 onward ~$94m
- 15% DCF NPV ~$404m

Emission Control 포함 SOTP:
**$60~85+ pre-split basis**

## 19. 실제 cash distributions — thesis의 핵심은 맞았다

Tinuum/CCS related distributions:

| 연도 | 대략 현금 |
|---|---:|
| 2013 | **$13.8m** |
| 2014 | **$43.6m** |
| 2018 | **$52.7m** |
| 2019 | **$65.2m** |
| 2020 | **$53.3m** |
| 2021 | **$65.2m + services $8.8m** |

Section 45 operations:
**2021-12-31 종료.**

즉 “tax-credit facilities가 monetized되면 수천만 달러 cash distributions가 발생한다”는 핵심 economic thesis는 강하게 맞았다.

## 20. Accounting / Governance가 별도 failure domain이었다

회사에는 이후:
- 2011~13 financial restatements
- material weaknesses
- internal-control failures
- 장기 SEC filing delay
- SEC enforcement

가 발생.

이는 refined-coal cash economics와 별개다.

> **Economics correct ≠ Financial reporting reliable ≠ Security rerating guaranteed**

세 축을 따로 본다.

## 21. ADES exact return을 보류한 이유

2014:
**2-for-1 stock split**.

또 후속:
- cash distributions
- capital returns
- business changes

가 있어 2012 nominal price와 later nominal price를 직접 비교하지 않는다.

따라서:
- operating thesis: 성공
- governance: 실패
- exact shareholder IRR: **corporate-action reconstruction 전 보류**

---

# PART F — Batch 057 Cross-Case Lessons

## 22. 이번 batch의 공통점: “어떤 Claim을 보유하고 있나?”

### WTW pair
기업을 Short한 것이 아니라:
- equity claim Short
- senior claim Long

### ABG
자동차 판매량을 산 것이 아니라:
- franchise claim
- P&S cash flow
- F&I
- real estate
- M&A capital allocation

### ADES
세액공제를 산 것이 아니라:
- JV distribution right
- tax monetizer execution
- reporting/control structure

즉 security는 **기업 이름이 아니라 현금흐름에 대한 법적/경제적 청구권**이다.

## 23. 정보의 질

낮은 순:
1. “경기가 곧 바닥”
2. management target
3. headline revenue
4. P/E
5. segment gross profit
6. normalized FCF
7. observed trough earnings
8. contractual seniority / maturity
9. actual cash distributions
10. actual third-party/repayment outcome

이번 batch에서도 아래쪽 evidence를 쓴 아이디어가 더 강했다.

## 24. Batch 057 재사용 체크리스트 20개

1. 한 VIC row에 여러 security가 있는지 확인한다.
2. pair trade는 leg별 P&L을 따로 저장한다.
3. senior maturity와 common optionality를 분리한다.
4. distressed equity에 strategic sponsor optionality를 둔다.
5. target price와 target date를 별도 판정한다.
6. cyclical floor는 역사평균보다 liquidity stress를 먼저 본다.
7. 실제 trough에서 cost structure가 어떻게 바뀌었는지 확인한다.
8. dealer는 SAAR보다 gross-profit mix를 본다.
9. P&S/F&I/new/used를 분리한다.
10. floorplan debt와 corporate debt를 분리한다.
11. post-crisis evidence가 생겼는데 multiple이 낮으면 재평가한다.
12. roll-up은 revenue growth보다 incremental ROIC를 본다.
13. peak EPS와 normalized EPS를 분리한다.
14. owned real estate를 double-count하지 않는다.
15. EV disruption은 기능별 disintermediation을 분석한다.
16. 5~10Y thesis는 중간 성과로 최종판정하지 않는다.
17. tax-credit DCF는 statutory expiry를 명시한다.
18. JV cash flow는 legal distribution right를 확인한다.
19. economic thesis와 accounting/governance quality를 별도 점수화한다.
20. stock split/distribution이 있으면 raw nominal return을 금지한다.

## 25. Batch 057 핵심 한 줄

> **투자는 ‘회사’에 하는 것이 아니라 특정 현금흐름과 특정 청구권에 하는 것이다. 같은 Weight Watchers에서도 senior loan은 맞고 equity Short는 틀렸고, 같은 Asbury에서도 바닥을 예측한 2008 Long보다 실제 바닥 economics를 확인한 2010 Long이 훨씬 강했다.**

## 26. 앱 / DB 반영

- Wrapper: analysis/batch_057_wtw_abg_ades_10.md
- Overlay: data/curated/batch_057_wtw_abg_ades_deep_v7.json
- Canonical source of truth: 위 10개 Markdown.
