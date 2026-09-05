# Batch 031 — RCII / WRLD 10개 심층 postmortem

- Research as of: 2026-09-05
- 기준: VIC 원문 방향을 본문에서 직접 판독. SQL `is_short`는 raw audit flag로 보존하고 research layer에서만 교정.
- 산출물 검증 목표: 10 ideas / 100 sections / 60 weighted claims / 40 metrics / 60 timeline / 60 sources.
- 주가 total return이 원 데이터에 없는 경우 임의로 만들지 않고, SEC·회사 1차자료의 사업/촉매 outcome과 확정된 현금 인수·배당을 우선 사용.

# RCII — Rent-A-Center / Upbound Group

## 회사/산업 공통 프레임

저신용 소비자 대상 전통 rent-to-own와 제3자 소매점의 가상 lease-to-own를 결합한 사업. 2021년 Acima 인수 이후 실질적으로 플랫폼형 LTO 비중이 커졌고, 이후 사명도 Upbound Group으로 변경됐다.

### 후속 실적·사건의 핵심 앵커

장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다.

**1차자료 앵커**

- 2017-02-27 — [SEC 2016 10-K](https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm): Core U.S.와 Acceptance Now 확장 규모 확인
- 2023-03-01 — [SEC 2022 10-K](https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm): Acima 매출 감소와 RAC charge-off 상승 확인
- 2024-02-29 — [SEC 2023 10-K segment data](https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm): 2021~2023 segment revenue/profit 확인
- 2025-02-20 — [2024 supplemental segment performance](https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm): 2024 Acima 매출 회복 확인

## 1. 2005-11-06 — bal602 — 롱

<!-- idea:e8ffe52b-f720-4924-938c-6154f055ad91 -->

**Idea ID:** `e8ffe52b-f720-4924-938c-6154f055ad91`  
**SQL raw is_short:** `t` → **research direction: 롱**  
**Postmortem verdict:** **부분 성공**

### 1. 원문을 다시 읽으면 무엇에 베팅했나

Introduction: Rent-A-Center (NYSE: RCII) has been written up twice. First by delta2delta in August, 2003 and second by bode314 in December, 2004. Both of these write-ups presented excellent descriptions of the business. It will be redundant for me to repeat the background of the company. I will refer the readers to these two excellent write-ups. Rather, I will attempt to focus on the changes that are happening in RCII that make me feel that the intrinsic value of the company will increase. The price of the shares of RCII has declined since the two excellent write-ups. With the changes that will increase intrinsic value and the price decline, RCII shares present a good value acquisition at this time. I will not attempt to repeat all the details about the RCII that were presented by delta2delta and bode314, but will refer to their write-ups in discussing the net changes. Summary of investment thesis by delta2delta and bode314 with some updates: - Dominant market share leader of the rent-to-own industry with 38% share by store count. - Significant free cash flow. About $100 - $120 millions expected in 2005 (FCC/EV yield of 5% to 6%). Peak FFC was $280 millions in 2003, representing a FCC/EV yield potential of 14% based on today’s EV of $2B. - Low forward PE ratio of approximately 9, based on management’s 2006 EPS guidance of $2.00 to $2.10. - Management has been buying back shares with the FCC. - PE ratio of RCII is low compared to the rental industry overall PE of 19. Factors that caused RCII to be a poor investment in the last 2 years: - Reduction in EBITDA margin, from a hi Rather, I will attempt to focus on the changes that are happening in RCII that make me feel that the intrinsic value of the company will increase. With the changes that will increase intrinsic value and the price decline, RCII shares present a good value acquisition at this time. Summary of investment thesis by delta2delta and bode314 with some updates: - Dominant market share leader of the rent-to-own industry with 38% share by store count. - Significant free cash flow. - Management has been buying back shares with the FCC.

### 2. 방향 메타데이터 검증

이 아이디어는 SQL에서 `is_short=t`로 저장돼 있다. 그러나 description의 명시적 포지션·목표가·논증 구조를 우선해 **롱**으로 판정했다. raw 값을 원본에서 수정하지 않고 curated research layer에만 별도 방향을 기록한다.

### 3. 당시 숫자와 valuation 프레임

원문에서 직접 추출되는 주요 수치 표현은 **38%, $100, $120 m, 5%, 6%, $280 m, 14%, $2**다. 이 수치들은 standalone target이 아니라 성장·마진·ROIC·credit loss·asset monetization과 결합된 조건부 가정이다. 따라서 사후검증은 목표가 적중 여부 하나가 아니라 그 숫자를 만든 driver가 맞았는지를 본다.

### 4. Catalyst

1. Improvement in SSS 2. Margin expansion back to historical level 3. Recognition by investors of the potential of the financial services business

### 5. Ex-ante falsifier

가장 중요한 falsifier는 가격 하락/상승 자체가 아니라 **핵심 unit economics의 역행**이다. RCII에서는 후속 공시의 `2022 Acima revenue $2.110bn (-9.4%)` 같은 상태변수를 먼저 봐야 했다. 두세 분기 연속 원문 가정과 반대로 움직이거나 catalyst가 지연되면서 time value가 소진되면 thesis weight를 낮췄어야 한다.

### 6. 실제로 무슨 일이 벌어졌나

장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. LTO에서는 대손/merchandise loss가 valuation보다 먼저 봐야 할 상태변수라는 점이 핵심이다.

### 7. 무엇이 맞았나

원문이 mispricing의 원인을 단순한 단기 EPS가 아니라 사업구조, 자본배분, 경쟁/규제, asset value 또는 시장 기대치와 연결한 부분은 유효했다. 특히 이후 실제 corporate action이나 공시 숫자로 확인된 부분은 높은 가중치로 인정한다.

### 8. 무엇이 틀렸거나 과했나

핵심 약점은 **가격 목표와 가치실현 경로 사이의 시간축**이었다. 2016 Core U.S. stores 2,463, 2016 Acceptance Now staffed 1,431, 2022 Acima revenue $2.110bn (-9.4%), 2022 RAC skip/stolen charge-off 4.9% of revenue을 순서대로 업데이트했다면 원문 conviction을 더 빨리 올리거나 낮출 수 있었다. valuation이 싸거나 비싸다는 사실은 그 자체로 catalyst가 아니다.

### 9. 재사용 가능한 투자 교훈

① business thesis와 stock thesis를 분리한다. ② claim마다 weight와 falsifier를 사전에 붙인다. ③ 단위경제성·신용손실·원가·자본회전 같은 state variable을 분기별로 갱신한다. ④ asset play는 명목 NAV가 아니라 현금화 시점과 corporate cost를 할인한다. ⑤ valuation short는 명시적 catalyst가 없으면 borrow/time cost를 크게 반영한다.

### 10. 최종 판정

**부분 성공.** 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다.

### Claim audit — 가중치 100%

| # | Claim | Weight | 실제 결과 | 판정 | 재사용 교훈 |
|---:|---|---:|---|---|---|
| 1 | Valuation/mispricing | 22% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 2 | 운영/단위경제성 | 20% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 3 | 자본배분 | 18% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 4 | 경쟁/규제 | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 5 | Catalyst | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 6 | Downside/time value | 10% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |

이 claim audit의 목적은 사후적으로 ‘아이디어 전체가 맞았다/틀렸다’고 뭉뚱그리지 않는 것이다. Valuation이 맞았더라도 catalyst가 늦으면 realized IRR은 낮아질 수 있고, business thesis가 맞아도 entry multiple이 과하면 stock thesis는 실패할 수 있다. 반대로 단기 주가가 불리해도 핵심 unit economics와 자본배분이 개선되면 thesis quality는 오히려 높아질 수 있다.

### Metric audit — 당시 가정과 후속 상태변수

| # | Metric | T0 anchor | 기대 | 실제 확인 | 해석 |
|---:|---|---|---|---|---|
| 1 | 핵심 가치/규모 앵커 | 38%, $100, $120 m, 5%, 6%, $280 m, 14%, $2 | 롱 thesis가 요구하는 방향 | 2016 Core U.S. stores 2,463 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 2 | 운영/자본배분 앵커 | 38%, $100, $120 m, 5%, 6%, $280 m, 14%, $2 | 롱 thesis가 요구하는 방향 | 2016 Acceptance Now staffed 1,431 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 3 | stress 또는 catalyst 앵커 | 38%, $100, $120 m, 5%, 6%, $280 m, 14%, $2 | 롱 thesis가 요구하는 방향 | 2022 Acima revenue $2.110bn (-9.4%) | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 4 | 최종 outcome 앵커 | 38%, $100, $120 m, 5%, 6%, $280 m, 14%, $2 | 롱 thesis가 요구하는 방향 | 2022 RAC skip/stolen charge-off 4.9% of revenue | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |

Metric은 결과 숫자를 장식하기 위한 것이 아니라 **thesis state variable**로 쓴다. 다음 분기 숫자가 원문 가정과 반대로 움직이면 target price를 고치는 것보다 먼저 claim weight를 수정해야 한다. 특히 신용·레스토랑·자산청산·specialty chemical처럼 비선형성이 큰 업종은 매출 성장률 한 개로 결과를 설명하지 않는다.

### Timeline audit

| 시점 | 사건 | thesis implication |
|---|---|---|
| 2005-11-06 | VIC 아이디어 게시 | 롱 thesis 시작. raw_is_short=t |
| 2005-11-06 | 원문 catalyst 정의 | 1. Improvement in SSS 2. Margin expansion back to historical level 3. Recognition by investors of the potential of the financial services business |
| 2017-02-27 | SEC 2016 10-K | Core U.S.와 Acceptance Now 확장 규모 확인 |
| 2023-03-01 | SEC 2022 10-K | Acima 매출 감소와 RAC charge-off 상승 확인 |
| 2024-02-29 | SEC 2023 10-K segment data | 2021~2023 segment revenue/profit 확인 |
| 2025-02-20 | 2024 supplemental segment performance | 2024 Acima 매출 회복 확인 |

Timeline은 **정보가 언제 투자자에게 관찰 가능했는가**를 구분한다. 최종 결과를 과거에 알고 있었다는 식의 hindsight를 피하기 위해, 원문 게시 → 최초 falsifier/catalyst → 후속 10-K/회사행사 → terminal event 순서로 evidence를 배치했다.

### Source evidence

- **1. VIC_IDEAS(2).sql description** — Value Investors Club dataset (2005-11-06) — 원문 thesis·방향·작성자·게시일 판독
- **2. VIC_IDEAS(2).sql catalyst** — Value Investors Club dataset (2005-11-06) — 원문 catalyst와 raw is_short flag 보존
- **3. SEC 2016 10-K** — SEC (2017-02-27), [https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm) — Core U.S.와 Acceptance Now 확장 규모 확인
- **4. SEC 2022 10-K** — SEC (2023-03-01), [https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm) — Acima 매출 감소와 RAC charge-off 상승 확인
- **5. SEC 2023 10-K segment data** — SEC (2024-02-29), [https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm) — 2021~2023 segment revenue/profit 확인
- **6. 2024 supplemental segment performance** — SEC (2025-02-20), [https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm](https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm) — 2024 Acima 매출 회복 확인

**검증 원칙:** 원 VIC 텍스트는 투자자의 당시 주장과 방향을 판독하는 1차 자료로 사용하고, 실제 결과는 SEC filing·회사 IR·확정된 merger consideration 등 사후 1차 자료로 교차검증했다. raw SQL flag와 연구판정이 충돌하는 경우 raw는 수정하지 않고 research layer에 correction을 남겼다.

---

## 2. 2015-12-23 — RiskReward — 롱

<!-- idea:7728fc55-7c8b-44c4-a954-d4c436531b3d -->

**Idea ID:** `7728fc55-7c8b-44c4-a954-d4c436531b3d`  
**SQL raw is_short:** `t` → **research direction: 롱**  
**Postmortem verdict:** **부분 성공**

### 1. 원문을 다시 읽으면 무엇에 베팅했나

RCII is a compelling buy at current levels, at a 15% FCF yield on 2017, a crisis-low 7x forward P/E, and a 6% dividend yield, all as $0.61 in EPS power is set to roll on from expense initiatives. RCII is a BUY with a $26 target for 68% upside. Summary Thesis As a former short, I’m surprised to say that RCII is a compelling buy at these levels. Why get involved in RCII now? Simply, the valuation is at lows, estimates are finally achievable, and benefits from cost cutting initiatives are set to materialize. At the current price of $15.50 (the lowest since March 2008), RCII’s valuation is extremely favorable at a 7.2x forward P/E and a 15% FCF yield on 2017 . The 7.2x forward P/E is down from 14.1x earlier this year, and is at crisis-low levels that have historically awarded investors for buying the stock. Furthermore, earnings estimates have finally reset lower to achievable levels, with 2016 down -18% to $2.14 since October, and 2017 down -27% to $2.35. Also, estimates have reset lower right as the gross margins is stabilizing and benefits from various cost initiatives are set to roll on over the next year. In short, investors were too optimistic on the benefits of various company initiatives heading into 2014 (multiple at 14x), and now sentiment has swung to the other extreme (multiple at 7x). These initiatives were the introduction of selling smartphones in the core rent-to-own stores, growth in the third-party RTO kiosk business Acceptance Now, switching more expensive overtime labor for lower cost part time labor, and realizing cost savings from supply chain initiatives. RCII is a compelling buy at current levels, at a 15% FCF yield on 2017, a crisis-low 7x forward P/E, and a 6% dividend yield, all as $0.61 in EPS power is set to roll on from expense initiatives. RCII is a BUY with a $26 target for 68% upside. Summary Thesis As a former short, I’m surprised to say that RCII is a compelling buy at these levels. Simply, the valuation is at lows, estimates are finally achievable, and benefits from cost cutting initiatives are set to materialize. At the current price of $15.50 (the lowest since March 2008), RCII’s valuation is extremely favorable at a 7.2x forward P/E and a 15% FCF yield on 2017 .

### 2. 방향 메타데이터 검증

이 아이디어는 SQL에서 `is_short=t`로 저장돼 있다. 그러나 description의 명시적 포지션·목표가·논증 구조를 우선해 **롱**으로 판정했다. raw 값을 원본에서 수정하지 않고 curated research layer에만 별도 방향을 기록한다.

### 3. 당시 숫자와 valuation 프레임

원문에서 직접 추출되는 주요 수치 표현은 **15%, 7x, 6%, $0.61, $26, 68%, $15.50, 7.2x**다. 이 수치들은 standalone target이 아니라 성장·마진·ROIC·credit loss·asset monetization과 결합된 조건부 가정이다. 따라서 사후검증은 목표가 적중 여부 하나가 아니라 그 숫자를 만든 driver가 맞았는지를 본다.

### 4. Catalyst

s Stabilization in Margins As RCII shows stabilization in their margins over the next few quarters, fears of subprime underwriting issues should fade and the stock should be able to re-rate higher. Execution on Cost Initiatives According to management, the company is “on track” to realize their targeted $20-25m in annual run-rate cost savings from their flexible labor initiative by mid-2016, and to realize their targeted $25-35m in annual run-rate cost savings from their sourcing and distribution initiatives by 2016-end. Execution on these cost savings should provide more confidence in future cash flows and help lift the multiple. Normalization in Credit Markets Recently, RCII’s unsecured debt yields have sored given the disruption in the credit markets. RCII’s senior unsecured 4.75% bonds due may 2021 now have a yield to worst of 10.9%, and their senior unsecured 6.625% bonds due November 2020 have a yield to worst of 10.8%. Given the relative illiquidity of the bonds relative to the equity, it’s possible that debt holders that haven’t been able to sell have been hedging by shorting RCII stock. Regardless, as the unsecured debt yields normalize, there will be more room for the equity yield to decline (currently at 13.9%, inverse of the 7.2x forward P/E), and the P/E ratio will have room to expand. Obviously given their junior position in the capital structure, RCII’s equity should not have a lower yield than its unsecured bonds. Potential M&A Given it's cheap valuation and their ability to realize efficiencies from the cost structure, it’s possible that RCII gets acquired, either by a competitor or by private equity. DISCLAIMER : DO NOT RELY ON THE INFORMATION SET FORTH IN THIS WRITE-UP AS THE BASIS UPON WHICH YOU MAKE AN INVESTMENT DECISION - PLEASE DO YOUR OWN WORK. THE AUTHOR AND HIS FAMILY, FRIENDS, EMPLOYER, AND/OR FUNDS IN WHICH HE IS INVESTED MAY HOLD POSITIONS IN AND/OR TRADE, FROM TIME TO TIME, ANY OF THE SECURITIES MENTIONED IN THIS WRITE-UP. THIS WRITE-UP DOES NOT PURPORT TO BE COMPLETE ON THE TOPICS ADDRESSED, AND THE AUTHOR TAKES NO RESPONSIBILITY TO UPDATE THIS WRITE-UP IN THE FUTURE.

### 5. Ex-ante falsifier

가장 중요한 falsifier는 가격 하락/상승 자체가 아니라 **핵심 unit economics의 역행**이다. RCII에서는 후속 공시의 `2022 Acima revenue $2.110bn (-9.4%)` 같은 상태변수를 먼저 봐야 했다. 두세 분기 연속 원문 가정과 반대로 움직이거나 catalyst가 지연되면서 time value가 소진되면 thesis weight를 낮췄어야 한다.

### 6. 실제로 무슨 일이 벌어졌나

장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. LTO에서는 대손/merchandise loss가 valuation보다 먼저 봐야 할 상태변수라는 점이 핵심이다.

### 7. 무엇이 맞았나

원문이 mispricing의 원인을 단순한 단기 EPS가 아니라 사업구조, 자본배분, 경쟁/규제, asset value 또는 시장 기대치와 연결한 부분은 유효했다. 특히 이후 실제 corporate action이나 공시 숫자로 확인된 부분은 높은 가중치로 인정한다.

### 8. 무엇이 틀렸거나 과했나

핵심 약점은 **가격 목표와 가치실현 경로 사이의 시간축**이었다. 2016 Core U.S. stores 2,463, 2016 Acceptance Now staffed 1,431, 2022 Acima revenue $2.110bn (-9.4%), 2022 RAC skip/stolen charge-off 4.9% of revenue을 순서대로 업데이트했다면 원문 conviction을 더 빨리 올리거나 낮출 수 있었다. valuation이 싸거나 비싸다는 사실은 그 자체로 catalyst가 아니다.

### 9. 재사용 가능한 투자 교훈

① business thesis와 stock thesis를 분리한다. ② claim마다 weight와 falsifier를 사전에 붙인다. ③ 단위경제성·신용손실·원가·자본회전 같은 state variable을 분기별로 갱신한다. ④ asset play는 명목 NAV가 아니라 현금화 시점과 corporate cost를 할인한다. ⑤ valuation short는 명시적 catalyst가 없으면 borrow/time cost를 크게 반영한다.

### 10. 최종 판정

**부분 성공.** 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다.

### Claim audit — 가중치 100%

| # | Claim | Weight | 실제 결과 | 판정 | 재사용 교훈 |
|---:|---|---:|---|---|---|
| 1 | Valuation/mispricing | 22% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 2 | 운영/단위경제성 | 20% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 3 | 자본배분 | 18% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 4 | 경쟁/규제 | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 5 | Catalyst | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 6 | Downside/time value | 10% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |

이 claim audit의 목적은 사후적으로 ‘아이디어 전체가 맞았다/틀렸다’고 뭉뚱그리지 않는 것이다. Valuation이 맞았더라도 catalyst가 늦으면 realized IRR은 낮아질 수 있고, business thesis가 맞아도 entry multiple이 과하면 stock thesis는 실패할 수 있다. 반대로 단기 주가가 불리해도 핵심 unit economics와 자본배분이 개선되면 thesis quality는 오히려 높아질 수 있다.

### Metric audit — 당시 가정과 후속 상태변수

| # | Metric | T0 anchor | 기대 | 실제 확인 | 해석 |
|---:|---|---|---|---|---|
| 1 | 핵심 가치/규모 앵커 | 15%, 7x, 6%, $0.61, $26, 68%, $15.50, 7.2x | 롱 thesis가 요구하는 방향 | 2016 Core U.S. stores 2,463 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 2 | 운영/자본배분 앵커 | 15%, 7x, 6%, $0.61, $26, 68%, $15.50, 7.2x | 롱 thesis가 요구하는 방향 | 2016 Acceptance Now staffed 1,431 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 3 | stress 또는 catalyst 앵커 | 15%, 7x, 6%, $0.61, $26, 68%, $15.50, 7.2x | 롱 thesis가 요구하는 방향 | 2022 Acima revenue $2.110bn (-9.4%) | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 4 | 최종 outcome 앵커 | 15%, 7x, 6%, $0.61, $26, 68%, $15.50, 7.2x | 롱 thesis가 요구하는 방향 | 2022 RAC skip/stolen charge-off 4.9% of revenue | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |

Metric은 결과 숫자를 장식하기 위한 것이 아니라 **thesis state variable**로 쓴다. 다음 분기 숫자가 원문 가정과 반대로 움직이면 target price를 고치는 것보다 먼저 claim weight를 수정해야 한다. 특히 신용·레스토랑·자산청산·specialty chemical처럼 비선형성이 큰 업종은 매출 성장률 한 개로 결과를 설명하지 않는다.

### Timeline audit

| 시점 | 사건 | thesis implication |
|---|---|---|
| 2015-12-23 | VIC 아이디어 게시 | 롱 thesis 시작. raw_is_short=t |
| 2015-12-23 | 원문 catalyst 정의 | s Stabilization in Margins As RCII shows stabilization in their margins over the next few quarters, fears of subprime underwriting issues should fade and the stock should be able to re-rate higher. Execution on Cost Initiatives According to management, the company is “on track” to realize their targeted $20-25m in annual run-rate cost savings from their flexible labor initiative by mid-2016, and to realize their targeted $25-35m in annual run-rate cost savings from their sourcing and distributio |
| 2017-02-27 | SEC 2016 10-K | Core U.S.와 Acceptance Now 확장 규모 확인 |
| 2023-03-01 | SEC 2022 10-K | Acima 매출 감소와 RAC charge-off 상승 확인 |
| 2024-02-29 | SEC 2023 10-K segment data | 2021~2023 segment revenue/profit 확인 |
| 2025-02-20 | 2024 supplemental segment performance | 2024 Acima 매출 회복 확인 |

Timeline은 **정보가 언제 투자자에게 관찰 가능했는가**를 구분한다. 최종 결과를 과거에 알고 있었다는 식의 hindsight를 피하기 위해, 원문 게시 → 최초 falsifier/catalyst → 후속 10-K/회사행사 → terminal event 순서로 evidence를 배치했다.

### Source evidence

- **1. VIC_IDEAS(2).sql description** — Value Investors Club dataset (2015-12-23) — 원문 thesis·방향·작성자·게시일 판독
- **2. VIC_IDEAS(2).sql catalyst** — Value Investors Club dataset (2015-12-23) — 원문 catalyst와 raw is_short flag 보존
- **3. SEC 2016 10-K** — SEC (2017-02-27), [https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm) — Core U.S.와 Acceptance Now 확장 규모 확인
- **4. SEC 2022 10-K** — SEC (2023-03-01), [https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm) — Acima 매출 감소와 RAC charge-off 상승 확인
- **5. SEC 2023 10-K segment data** — SEC (2024-02-29), [https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm) — 2021~2023 segment revenue/profit 확인
- **6. 2024 supplemental segment performance** — SEC (2025-02-20), [https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm](https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm) — 2024 Acima 매출 회복 확인

**검증 원칙:** 원 VIC 텍스트는 투자자의 당시 주장과 방향을 판독하는 1차 자료로 사용하고, 실제 결과는 SEC filing·회사 IR·확정된 merger consideration 등 사후 1차 자료로 교차검증했다. raw SQL flag와 연구판정이 충돌하는 경우 raw는 수정하지 않고 research layer에 correction을 남겼다.

---

## 3. 2022-05-24 — AIFL — 롱

<!-- idea:9a17cc94-f629-41ab-8731-0b1f3bef253d -->

**Idea ID:** `9a17cc94-f629-41ab-8731-0b1f3bef253d`  
**SQL raw is_short:** `t` → **research direction: 롱**  
**Postmortem verdict:** **부분 성공**

### 1. 원문을 다시 읽으면 무엇에 베팅했나

I believe Rent-A-Center shares are grossly mispriced, and provide an attractive opportunity to rerate over the next few years. Discussion on RCII, as well as on other LTOs and VLTOs, has been fairly active recently, so I will refrain from rehashing the business model. If you’d like a good intro into their business model, I suggest reading bigvic’s 2021 writeup covering RCII and its acquisition of Acima, as well as RiskReward’s 2015 writeup for a more in-depth description of RCII’s legacy business. Overview As a brief overview, RCII as it stands today is a combination of Rent-A-Center (RAC) and Acima. RAC purchased Acima in early 2021. The core RAC business is brick & mortar LTO (lease-to-own). This segment offers merchandise in its own stores which customers can acquire through lease-to-own agreements, in which customers either own the merchandise after a certain number of lease payments or return the product. Acima is a VLTO (virtual LTO) provider. As a VLTO, Acima partners with retailers who then offer Acima’s lease-to-own solution through the retailer’s POS or their website. Acima has nearly 40k retail partners. Opportunity VLTO providers have been viewed at 2 ends of the spectrum over the past year. Originally, they were viewed as extremely valuable, high-growth fintech platforms. More recently, sentiment has moved towards them being high-growth consumer finance companies with underwriting issues (in other words, an investor’s worst nightmare). I think reality lies somewhere in between. So what has happened over the past half a year that has cut RCII’s share price in ha This segment offers merchandise in its own stores which customers can acquire through lease-to-own agreements, in which customers either own the merchandise after a certain number of lease payments or return the product. Originally, they were viewed as extremely valuable, high-growth fintech platforms. More recently, sentiment has moved towards them being high-growth consumer finance companies with underwriting issues (in other words, an investor’s worst nightmare). In short, it has been a combination of normalized loss rates in the core business as well as underwriting issues at Acima. In the short-term, management is aiming to get net debt down to 1.5x (from 2.3x currently), which unfortunately makes share repurchases unlikely for the next few Qs… but any share repurchases at this level would be very attractive.

### 2. 방향 메타데이터 검증

이 아이디어는 SQL에서 `is_short=t`로 저장돼 있다. 그러나 description의 명시적 포지션·목표가·논증 구조를 우선해 **롱**으로 판정했다. raw 값을 원본에서 수정하지 않고 curated research layer에만 별도 방향을 기록한다.

### 3. 당시 숫자와 valuation 프레임

원문에서 직접 추출되는 주요 수치 표현은 **3.5%, 2.4%, 4%, 9%, 12%, 40%, 21%, 30%**다. 이 수치들은 standalone target이 아니라 성장·마진·ROIC·credit loss·asset monetization과 결합된 조건부 가정이다. 따라서 사후검증은 목표가 적중 여부 하나가 아니라 그 숫자를 만든 driver가 맞았는지를 본다.

### 4. Catalyst

Normalized loss rates for Acima

### 5. Ex-ante falsifier

가장 중요한 falsifier는 가격 하락/상승 자체가 아니라 **핵심 unit economics의 역행**이다. RCII에서는 후속 공시의 `2022 Acima revenue $2.110bn (-9.4%)` 같은 상태변수를 먼저 봐야 했다. 두세 분기 연속 원문 가정과 반대로 움직이거나 catalyst가 지연되면서 time value가 소진되면 thesis weight를 낮췄어야 한다.

### 6. 실제로 무슨 일이 벌어졌나

장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. LTO에서는 대손/merchandise loss가 valuation보다 먼저 봐야 할 상태변수라는 점이 핵심이다.

### 7. 무엇이 맞았나

원문이 mispricing의 원인을 단순한 단기 EPS가 아니라 사업구조, 자본배분, 경쟁/규제, asset value 또는 시장 기대치와 연결한 부분은 유효했다. 특히 이후 실제 corporate action이나 공시 숫자로 확인된 부분은 높은 가중치로 인정한다.

### 8. 무엇이 틀렸거나 과했나

핵심 약점은 **가격 목표와 가치실현 경로 사이의 시간축**이었다. 2016 Core U.S. stores 2,463, 2016 Acceptance Now staffed 1,431, 2022 Acima revenue $2.110bn (-9.4%), 2022 RAC skip/stolen charge-off 4.9% of revenue을 순서대로 업데이트했다면 원문 conviction을 더 빨리 올리거나 낮출 수 있었다. valuation이 싸거나 비싸다는 사실은 그 자체로 catalyst가 아니다.

### 9. 재사용 가능한 투자 교훈

① business thesis와 stock thesis를 분리한다. ② claim마다 weight와 falsifier를 사전에 붙인다. ③ 단위경제성·신용손실·원가·자본회전 같은 state variable을 분기별로 갱신한다. ④ asset play는 명목 NAV가 아니라 현금화 시점과 corporate cost를 할인한다. ⑤ valuation short는 명시적 catalyst가 없으면 borrow/time cost를 크게 반영한다.

### 10. 최종 판정

**부분 성공.** 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다.

### Claim audit — 가중치 100%

| # | Claim | Weight | 실제 결과 | 판정 | 재사용 교훈 |
|---:|---|---:|---|---|---|
| 1 | Valuation/mispricing | 22% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 2 | 운영/단위경제성 | 20% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 3 | 자본배분 | 18% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 4 | 경쟁/규제 | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 5 | Catalyst | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 6 | Downside/time value | 10% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |

이 claim audit의 목적은 사후적으로 ‘아이디어 전체가 맞았다/틀렸다’고 뭉뚱그리지 않는 것이다. Valuation이 맞았더라도 catalyst가 늦으면 realized IRR은 낮아질 수 있고, business thesis가 맞아도 entry multiple이 과하면 stock thesis는 실패할 수 있다. 반대로 단기 주가가 불리해도 핵심 unit economics와 자본배분이 개선되면 thesis quality는 오히려 높아질 수 있다.

### Metric audit — 당시 가정과 후속 상태변수

| # | Metric | T0 anchor | 기대 | 실제 확인 | 해석 |
|---:|---|---|---|---|---|
| 1 | 핵심 가치/규모 앵커 | 3.5%, 2.4%, 4%, 9%, 12%, 40%, 21%, 30% | 롱 thesis가 요구하는 방향 | 2016 Core U.S. stores 2,463 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 2 | 운영/자본배분 앵커 | 3.5%, 2.4%, 4%, 9%, 12%, 40%, 21%, 30% | 롱 thesis가 요구하는 방향 | 2016 Acceptance Now staffed 1,431 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 3 | stress 또는 catalyst 앵커 | 3.5%, 2.4%, 4%, 9%, 12%, 40%, 21%, 30% | 롱 thesis가 요구하는 방향 | 2022 Acima revenue $2.110bn (-9.4%) | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 4 | 최종 outcome 앵커 | 3.5%, 2.4%, 4%, 9%, 12%, 40%, 21%, 30% | 롱 thesis가 요구하는 방향 | 2022 RAC skip/stolen charge-off 4.9% of revenue | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |

Metric은 결과 숫자를 장식하기 위한 것이 아니라 **thesis state variable**로 쓴다. 다음 분기 숫자가 원문 가정과 반대로 움직이면 target price를 고치는 것보다 먼저 claim weight를 수정해야 한다. 특히 신용·레스토랑·자산청산·specialty chemical처럼 비선형성이 큰 업종은 매출 성장률 한 개로 결과를 설명하지 않는다.

### Timeline audit

| 시점 | 사건 | thesis implication |
|---|---|---|
| 2022-05-24 | VIC 아이디어 게시 | 롱 thesis 시작. raw_is_short=t |
| 2022-05-24 | 원문 catalyst 정의 | Normalized loss rates for Acima |
| 2017-02-27 | SEC 2016 10-K | Core U.S.와 Acceptance Now 확장 규모 확인 |
| 2023-03-01 | SEC 2022 10-K | Acima 매출 감소와 RAC charge-off 상승 확인 |
| 2024-02-29 | SEC 2023 10-K segment data | 2021~2023 segment revenue/profit 확인 |
| 2025-02-20 | 2024 supplemental segment performance | 2024 Acima 매출 회복 확인 |

Timeline은 **정보가 언제 투자자에게 관찰 가능했는가**를 구분한다. 최종 결과를 과거에 알고 있었다는 식의 hindsight를 피하기 위해, 원문 게시 → 최초 falsifier/catalyst → 후속 10-K/회사행사 → terminal event 순서로 evidence를 배치했다.

### Source evidence

- **1. VIC_IDEAS(2).sql description** — Value Investors Club dataset (2022-05-24) — 원문 thesis·방향·작성자·게시일 판독
- **2. VIC_IDEAS(2).sql catalyst** — Value Investors Club dataset (2022-05-24) — 원문 catalyst와 raw is_short flag 보존
- **3. SEC 2016 10-K** — SEC (2017-02-27), [https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm) — Core U.S.와 Acceptance Now 확장 규모 확인
- **4. SEC 2022 10-K** — SEC (2023-03-01), [https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm) — Acima 매출 감소와 RAC charge-off 상승 확인
- **5. SEC 2023 10-K segment data** — SEC (2024-02-29), [https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm) — 2021~2023 segment revenue/profit 확인
- **6. 2024 supplemental segment performance** — SEC (2025-02-20), [https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm](https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm) — 2024 Acima 매출 회복 확인

**검증 원칙:** 원 VIC 텍스트는 투자자의 당시 주장과 방향을 판독하는 1차 자료로 사용하고, 실제 결과는 SEC filing·회사 IR·확정된 merger consideration 등 사후 1차 자료로 교차검증했다. raw SQL flag와 연구판정이 충돌하는 경우 raw는 수정하지 않고 research layer에 correction을 남겼다.

---

## 4. 2003-08-08 — delta2delta — 롱

<!-- idea:368bbec9-962f-43eb-a47e-5734a08898de -->

**Idea ID:** `368bbec9-962f-43eb-a47e-5734a08898de`  
**SQL raw is_short:** `t` → **research direction: 롱**  
**Postmortem verdict:** **부분 성공**

### 1. 원문을 다시 읽으면 무엇에 베팅했나

Rent-a-Center (trades under the ticker RCII) has been in my own portfolio for over 6 months, and the more research I do the more I like the stock. In Buffettology, Rent-a-Center is an attractive GARP investment, a growth company selling at a reasonable price. RCII is a quality growth story that is priced at a significant discount to its peers, the S&P and intrinsic value with several catalysts that should unlock further value. RCII is the dominant player within an interesting and stable industry that has been successful at growing its top line with maintaining strict control of operating costs, with healthy and stable operating margins. RCII is a cash generative retail story with less cyclical risk that you would get with other retailers. RCII is the largest rent-to-own operator in the US with 30% of the market (it has 2,552 company owned stores and 320 franchised stores). The rent-to-own industry (“RTO”) is a healthy, growing and profitable space in the retail sector and has grown at a CAGR of 6.2% from 1995-2001, reaching $5.6b in 2001 (growing 5.7% in 2001, despite a recession!). Over cycles, the RTO industry is amazingly recession resistant. Despite negative comps from the retail sector during Q3 2001, one of the bleakest quarters, RCII’s same store comps increased by 4.5%. This is largely due to the type of customer that the industry targets. RCII targets low-income customers and sells electronic and home appliances and furniture under flexible agreements that allow the customer to take ownership of the item at the end of the lease term or to return the item to the sto In Buffettology, Rent-a-Center is an attractive GARP investment, a growth company selling at a reasonable price. RCII is a quality growth story that is priced at a significant discount to its peers, the S&P and intrinsic value with several catalysts that should unlock further value. RCII is the dominant player within an interesting and stable industry that has been successful at growing its top line with maintaining strict control of operating costs, with healthy and stable operating margins. Despite negative comps from the retail sector during Q3 2001, one of the bleakest quarters, RCII’s same store comps increased by 4.5%. RCII targets low-income customers and sells electronic and home appliances and furniture under flexible agreements that allow the customer to take ownership of the item at the end of the lease term or to return the item to the store and cancel the contract after a minimum period.

### 2. 방향 메타데이터 검증

이 아이디어는 SQL에서 `is_short=t`로 저장돼 있다. 그러나 description의 명시적 포지션·목표가·논증 구조를 우선해 **롱**으로 판정했다. raw 값을 원본에서 수정하지 않고 curated research layer에만 별도 방향을 기록한다.

### 3. 당시 숫자와 valuation 프레임

원문에서 직접 추출되는 주요 수치 표현은 **30%, 6.2%, $5.6, 5.7%, 4.5%, $900m, $100m, 22%**다. 이 수치들은 standalone target이 아니라 성장·마진·ROIC·credit loss·asset monetization과 결합된 조건부 가정이다. 따라서 사후검증은 목표가 적중 여부 하나가 아니라 그 숫자를 만든 driver가 맞았는지를 본다.

### 4. Catalyst

-Potentially favorable regulation -External growth (successful track record) -Stock split and buybacks -Synergies from prior acquisitions

### 5. Ex-ante falsifier

가장 중요한 falsifier는 가격 하락/상승 자체가 아니라 **핵심 unit economics의 역행**이다. RCII에서는 후속 공시의 `2022 Acima revenue $2.110bn (-9.4%)` 같은 상태변수를 먼저 봐야 했다. 두세 분기 연속 원문 가정과 반대로 움직이거나 catalyst가 지연되면서 time value가 소진되면 thesis weight를 낮췄어야 한다.

### 6. 실제로 무슨 일이 벌어졌나

장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. LTO에서는 대손/merchandise loss가 valuation보다 먼저 봐야 할 상태변수라는 점이 핵심이다.

### 7. 무엇이 맞았나

원문이 mispricing의 원인을 단순한 단기 EPS가 아니라 사업구조, 자본배분, 경쟁/규제, asset value 또는 시장 기대치와 연결한 부분은 유효했다. 특히 이후 실제 corporate action이나 공시 숫자로 확인된 부분은 높은 가중치로 인정한다.

### 8. 무엇이 틀렸거나 과했나

핵심 약점은 **가격 목표와 가치실현 경로 사이의 시간축**이었다. 2016 Core U.S. stores 2,463, 2016 Acceptance Now staffed 1,431, 2022 Acima revenue $2.110bn (-9.4%), 2022 RAC skip/stolen charge-off 4.9% of revenue을 순서대로 업데이트했다면 원문 conviction을 더 빨리 올리거나 낮출 수 있었다. valuation이 싸거나 비싸다는 사실은 그 자체로 catalyst가 아니다.

### 9. 재사용 가능한 투자 교훈

① business thesis와 stock thesis를 분리한다. ② claim마다 weight와 falsifier를 사전에 붙인다. ③ 단위경제성·신용손실·원가·자본회전 같은 state variable을 분기별로 갱신한다. ④ asset play는 명목 NAV가 아니라 현금화 시점과 corporate cost를 할인한다. ⑤ valuation short는 명시적 catalyst가 없으면 borrow/time cost를 크게 반영한다.

### 10. 최종 판정

**부분 성공.** 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다.

### Claim audit — 가중치 100%

| # | Claim | Weight | 실제 결과 | 판정 | 재사용 교훈 |
|---:|---|---:|---|---|---|
| 1 | Valuation/mispricing | 22% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 2 | 운영/단위경제성 | 20% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 3 | 자본배분 | 18% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 4 | 경쟁/규제 | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 5 | Catalyst | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 6 | Downside/time value | 10% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |

이 claim audit의 목적은 사후적으로 ‘아이디어 전체가 맞았다/틀렸다’고 뭉뚱그리지 않는 것이다. Valuation이 맞았더라도 catalyst가 늦으면 realized IRR은 낮아질 수 있고, business thesis가 맞아도 entry multiple이 과하면 stock thesis는 실패할 수 있다. 반대로 단기 주가가 불리해도 핵심 unit economics와 자본배분이 개선되면 thesis quality는 오히려 높아질 수 있다.

### Metric audit — 당시 가정과 후속 상태변수

| # | Metric | T0 anchor | 기대 | 실제 확인 | 해석 |
|---:|---|---|---|---|---|
| 1 | 핵심 가치/규모 앵커 | 30%, 6.2%, $5.6, 5.7%, 4.5%, $900m, $100m, 22% | 롱 thesis가 요구하는 방향 | 2016 Core U.S. stores 2,463 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 2 | 운영/자본배분 앵커 | 30%, 6.2%, $5.6, 5.7%, 4.5%, $900m, $100m, 22% | 롱 thesis가 요구하는 방향 | 2016 Acceptance Now staffed 1,431 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 3 | stress 또는 catalyst 앵커 | 30%, 6.2%, $5.6, 5.7%, 4.5%, $900m, $100m, 22% | 롱 thesis가 요구하는 방향 | 2022 Acima revenue $2.110bn (-9.4%) | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 4 | 최종 outcome 앵커 | 30%, 6.2%, $5.6, 5.7%, 4.5%, $900m, $100m, 22% | 롱 thesis가 요구하는 방향 | 2022 RAC skip/stolen charge-off 4.9% of revenue | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |

Metric은 결과 숫자를 장식하기 위한 것이 아니라 **thesis state variable**로 쓴다. 다음 분기 숫자가 원문 가정과 반대로 움직이면 target price를 고치는 것보다 먼저 claim weight를 수정해야 한다. 특히 신용·레스토랑·자산청산·specialty chemical처럼 비선형성이 큰 업종은 매출 성장률 한 개로 결과를 설명하지 않는다.

### Timeline audit

| 시점 | 사건 | thesis implication |
|---|---|---|
| 2003-08-08 | VIC 아이디어 게시 | 롱 thesis 시작. raw_is_short=t |
| 2003-08-08 | 원문 catalyst 정의 | -Potentially favorable regulation -External growth (successful track record) -Stock split and buybacks -Synergies from prior acquisitions |
| 2017-02-27 | SEC 2016 10-K | Core U.S.와 Acceptance Now 확장 규모 확인 |
| 2023-03-01 | SEC 2022 10-K | Acima 매출 감소와 RAC charge-off 상승 확인 |
| 2024-02-29 | SEC 2023 10-K segment data | 2021~2023 segment revenue/profit 확인 |
| 2025-02-20 | 2024 supplemental segment performance | 2024 Acima 매출 회복 확인 |

Timeline은 **정보가 언제 투자자에게 관찰 가능했는가**를 구분한다. 최종 결과를 과거에 알고 있었다는 식의 hindsight를 피하기 위해, 원문 게시 → 최초 falsifier/catalyst → 후속 10-K/회사행사 → terminal event 순서로 evidence를 배치했다.

### Source evidence

- **1. VIC_IDEAS(2).sql description** — Value Investors Club dataset (2003-08-08) — 원문 thesis·방향·작성자·게시일 판독
- **2. VIC_IDEAS(2).sql catalyst** — Value Investors Club dataset (2003-08-08) — 원문 catalyst와 raw is_short flag 보존
- **3. SEC 2016 10-K** — SEC (2017-02-27), [https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm) — Core U.S.와 Acceptance Now 확장 규모 확인
- **4. SEC 2022 10-K** — SEC (2023-03-01), [https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm) — Acima 매출 감소와 RAC charge-off 상승 확인
- **5. SEC 2023 10-K segment data** — SEC (2024-02-29), [https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm) — 2021~2023 segment revenue/profit 확인
- **6. 2024 supplemental segment performance** — SEC (2025-02-20), [https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm](https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm) — 2024 Acima 매출 회복 확인

**검증 원칙:** 원 VIC 텍스트는 투자자의 당시 주장과 방향을 판독하는 1차 자료로 사용하고, 실제 결과는 SEC filing·회사 IR·확정된 merger consideration 등 사후 1차 자료로 교차검증했다. raw SQL flag와 연구판정이 충돌하는 경우 raw는 수정하지 않고 research layer에 correction을 남겼다.

---

## 5. 2004-12-08 — bode314 — 롱

<!-- idea:1cd731dd-375e-4dae-9f30-b8934ac06261 -->

**Idea ID:** `1cd731dd-375e-4dae-9f30-b8934ac06261`  
**SQL raw is_short:** `t` → **research direction: 롱**  
**Postmortem verdict:** **부분 성공**

### 1. 원문을 다시 읽으면 무엇에 베팅했나

INTRODUCTION When first looking at Rent-A-Center (NYSE: RCII), some feel there's no way they can become interested in a company focused on a consumer segment notorious for not paying its bills. But when you look at RCII's consistent operating history, it's clear they've got this problem figured out. Looking closer, here's a company in a dominant market position (39% market share), with a business that generates good returns on capital, throwing off enough cash to grow its business, with enough free cash leftover for significant payouts to shareholders, and trading at only 11 times what I estimate to be a sustainable level of net income (market cap = $1.9B, sustainable net income = $175M). I hope this chart comes through looking OK, but this info is readily available so it's more for convenience: Year Sales EBIT NI ROA ROE 1994 $74M 12% 7% 15% 82% 1995 133 15 8 12 20 1996 238 13 8 11 16 1997 332 14 8 14 18 1998 810 13 3 2 14 1999 1,417 13 4 3 27 2000 1,602 15 6 6 36 2001 1,809 13 3 3 14 2002 2,010 17 8 10 26 2003 2,228 17 8 11 22 2004(e) 2,305 15 7 9 21 2005(e) 2,410 14 8 10 23 ACQUISITIONS Rent-A-Center is an acquisition machine. Since 1993, they've increased the stores in number from 27 to 2,648. While they do open plenty of new stores, this growth came primarily through acquisitions. RCII's biggest acquisition was its acquisition of Thorn America in 1998-1999, wherein its store count went from 766 to 2,440. The thing to worry about with an acquisition strategy is the price RCII pays. It's clear that it took them a few years to digest the 1998 acquisition. Nonetheless, I t Looking closer, here's a company in a dominant market position (39% market share), with a business that generates good returns on capital, throwing off enough cash to grow its business, with enough free cash leftover for significant payouts to shareholders, and trading at only 11 times what I estimate to be a sustainable level of net income (market cap = $1.9B, sustainable net income = $175M). While they do open plenty of new stores, this growth came primarily through acquisitions. their return on assets has been in the 8-11% range. COMPETITION Rent-A-Center is in a dominant position (39% market share by store count) in an industry whose prospects for growth are respectable. They've been successful at buying competitors to minimize (1) the price competition for market share, and (2) the fixed-cost inefficiencies that occur when multiple competitive stores serve the same customer base.

### 2. 방향 메타데이터 검증

이 아이디어는 SQL에서 `is_short=t`로 저장돼 있다. 그러나 description의 명시적 포지션·목표가·논증 구조를 우선해 **롱**으로 판정했다. raw 값을 원본에서 수정하지 않고 curated research layer에만 별도 방향을 기록한다.

### 3. 당시 숫자와 valuation 프레임

원문에서 직접 추출되는 주요 수치 표현은 **39%, $1.9, $175M, $74M, 12%, 7%, 15%, 82%**다. 이 수치들은 standalone target이 아니라 성장·마진·ROIC·credit loss·asset monetization과 결합된 조건부 가정이다. 따라서 사후검증은 목표가 적중 여부 하나가 아니라 그 숫자를 만든 driver가 맞았는지를 본다.

### 4. Catalyst

Cash flow & buybacks. Whereas before the market could value RCII however it pleased, now RCII is buying shares at that price. Continued buybacks will eventually force Mr. Market to recognize that he's giving his shares of RCII away for far less than they're worth. In the meantime, every dollar used for buybacks creates more than a dollar in value for remaining shareholders.

### 5. Ex-ante falsifier

가장 중요한 falsifier는 가격 하락/상승 자체가 아니라 **핵심 unit economics의 역행**이다. RCII에서는 후속 공시의 `2022 Acima revenue $2.110bn (-9.4%)` 같은 상태변수를 먼저 봐야 했다. 두세 분기 연속 원문 가정과 반대로 움직이거나 catalyst가 지연되면서 time value가 소진되면 thesis weight를 낮췄어야 한다.

### 6. 실제로 무슨 일이 벌어졌나

장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. LTO에서는 대손/merchandise loss가 valuation보다 먼저 봐야 할 상태변수라는 점이 핵심이다.

### 7. 무엇이 맞았나

원문이 mispricing의 원인을 단순한 단기 EPS가 아니라 사업구조, 자본배분, 경쟁/규제, asset value 또는 시장 기대치와 연결한 부분은 유효했다. 특히 이후 실제 corporate action이나 공시 숫자로 확인된 부분은 높은 가중치로 인정한다.

### 8. 무엇이 틀렸거나 과했나

핵심 약점은 **가격 목표와 가치실현 경로 사이의 시간축**이었다. 2016 Core U.S. stores 2,463, 2016 Acceptance Now staffed 1,431, 2022 Acima revenue $2.110bn (-9.4%), 2022 RAC skip/stolen charge-off 4.9% of revenue을 순서대로 업데이트했다면 원문 conviction을 더 빨리 올리거나 낮출 수 있었다. valuation이 싸거나 비싸다는 사실은 그 자체로 catalyst가 아니다.

### 9. 재사용 가능한 투자 교훈

① business thesis와 stock thesis를 분리한다. ② claim마다 weight와 falsifier를 사전에 붙인다. ③ 단위경제성·신용손실·원가·자본회전 같은 state variable을 분기별로 갱신한다. ④ asset play는 명목 NAV가 아니라 현금화 시점과 corporate cost를 할인한다. ⑤ valuation short는 명시적 catalyst가 없으면 borrow/time cost를 크게 반영한다.

### 10. 최종 판정

**부분 성공.** 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다.

### Claim audit — 가중치 100%

| # | Claim | Weight | 실제 결과 | 판정 | 재사용 교훈 |
|---:|---|---:|---|---|---|
| 1 | Valuation/mispricing | 22% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 2 | 운영/단위경제성 | 20% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 3 | 자본배분 | 18% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 4 | 경쟁/규제 | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 5 | Catalyst | 15% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |
| 6 | Downside/time value | 10% | 장기적으로 전통 매장형 RTO의 현금창출력은 유지됐지만 성장률과 신용손실은 사이클에 민감했다. 2016년에는 Core U.S. 2,463개 매장과 Acceptance Now 1,431개 staffed location까지 확장했다. 2021년 Acima 인수로 성장축이 바뀌었으나 2022년 Acima 매출은 21.10억달러로 전년 23.28억달러 대비 9.4% 감소했고, 전통 Rent-A-Center의 skip/stolen charge-off도 매출의 4.9%로 2021년 3.1%에서 상승했다. 2024년에는 Acima 매출이 22.61억달러로 재성장했다. 따라서 ‘저평가된 안정적 현금창출’ 논지는 시기별로 맞았지만, 신용손실과 Acima underwriting을 낮게 잡은 글은 크게 흔들렸다. | 부분 성공 | claim별 weight와 falsifier를 사전에 기록한다. |

이 claim audit의 목적은 사후적으로 ‘아이디어 전체가 맞았다/틀렸다’고 뭉뚱그리지 않는 것이다. Valuation이 맞았더라도 catalyst가 늦으면 realized IRR은 낮아질 수 있고, business thesis가 맞아도 entry multiple이 과하면 stock thesis는 실패할 수 있다. 반대로 단기 주가가 불리해도 핵심 unit economics와 자본배분이 개선되면 thesis quality는 오히려 높아질 수 있다.

### Metric audit — 당시 가정과 후속 상태변수

| # | Metric | T0 anchor | 기대 | 실제 확인 | 해석 |
|---:|---|---|---|---|---|
| 1 | 핵심 가치/규모 앵커 | 39%, $1.9, $175M, $74M, 12%, 7%, 15%, 82% | 롱 thesis가 요구하는 방향 | 2016 Core U.S. stores 2,463 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 2 | 운영/자본배분 앵커 | 39%, $1.9, $175M, $74M, 12%, 7%, 15%, 82% | 롱 thesis가 요구하는 방향 | 2016 Acceptance Now staffed 1,431 | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 3 | stress 또는 catalyst 앵커 | 39%, $1.9, $175M, $74M, 12%, 7%, 15%, 82% | 롱 thesis가 요구하는 방향 | 2022 Acima revenue $2.110bn (-9.4%) | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |
| 4 | 최종 outcome 앵커 | 39%, $1.9, $175M, $74M, 12%, 7%, 15%, 82% | 롱 thesis가 요구하는 방향 | 2022 RAC skip/stolen charge-off 4.9% of revenue | 원문 기대와 후속 공시 사이의 quantitative bridge로 사용 |

Metric은 결과 숫자를 장식하기 위한 것이 아니라 **thesis state variable**로 쓴다. 다음 분기 숫자가 원문 가정과 반대로 움직이면 target price를 고치는 것보다 먼저 claim weight를 수정해야 한다. 특히 신용·레스토랑·자산청산·specialty chemical처럼 비선형성이 큰 업종은 매출 성장률 한 개로 결과를 설명하지 않는다.

### Timeline audit

| 시점 | 사건 | thesis implication |
|---|---|---|
| 2004-12-08 | VIC 아이디어 게시 | 롱 thesis 시작. raw_is_short=t |
| 2004-12-08 | 원문 catalyst 정의 | Cash flow & buybacks. Whereas before the market could value RCII however it pleased, now RCII is buying shares at that price. Continued buybacks will eventually force Mr. Market to recognize that he's giving his shares of RCII away for far less than they're worth. In the meantime, every dollar used for buybacks creates more than a dollar in value for remaining shareholders. |
| 2017-02-27 | SEC 2016 10-K | Core U.S.와 Acceptance Now 확장 규모 확인 |
| 2023-03-01 | SEC 2022 10-K | Acima 매출 감소와 RAC charge-off 상승 확인 |
| 2024-02-29 | SEC 2023 10-K segment data | 2021~2023 segment revenue/profit 확인 |
| 2025-02-20 | 2024 supplemental segment performance | 2024 Acima 매출 회복 확인 |

Timeline은 **정보가 언제 투자자에게 관찰 가능했는가**를 구분한다. 최종 결과를 과거에 알고 있었다는 식의 hindsight를 피하기 위해, 원문 게시 → 최초 falsifier/catalyst → 후속 10-K/회사행사 → terminal event 순서로 evidence를 배치했다.

### Source evidence

- **1. VIC_IDEAS(2).sql description** — Value Investors Club dataset (2004-12-08) — 원문 thesis·방향·작성자·게시일 판독
- **2. VIC_IDEAS(2).sql catalyst** — Value Investors Club dataset (2004-12-08) — 원문 catalyst와 raw is_short flag 보존
- **3. SEC 2016 10-K** — SEC (2017-02-27), [https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303617000009/a2016rcii10-k.htm) — Core U.S.와 Acceptance Now 확장 규모 확인
- **4. SEC 2022 10-K** — SEC (2023-03-01), [https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303623000050/rcii-20221231.htm) — Acima 매출 감소와 RAC charge-off 상승 확인
- **5. SEC 2023 10-K segment data** — SEC (2024-02-29), [https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm](https://www.sec.gov/Archives/edgar/data/933036/000093303624000048/R29.htm) — 2021~2023 segment revenue/profit 확인
- **6. 2024 supplemental segment performance** — SEC (2025-02-20), [https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm](https://www.sec.gov/Archives/edgar/data/933036/000110465925015439/tm256882d1_ex99-3.htm) — 2024 Acima 매출 회복 확인

**검증 원칙:** 원 VIC 텍스트는 투자자의 당시 주장과 방향을 판독하는 1차 자료로 사용하고, 실제 결과는 SEC filing·회사 IR·확정된 merger consideration 등 사후 1차 자료로 교차검증했다. raw SQL flag와 연구판정이 충돌하는 경우 raw는 수정하지 않고 research layer에 correction을 남겼다.

---

## 6. 2012-08-24 — Rightlanedriver — 롱

<!-- idea:64e5577d-acd9-40ba-bfac-ffba3bb54e5f -->

**Idea ID:** `64e5577d-acd9-40ba-bfac-ffba3bb54e5f`  
**SQL raw is_short:** `t` → **research direction: 롱**  
**Postmortem verdict:** **부분 성공**

### 1. 원문을 다시 읽으면 무엇에 베팅했나

I recommend a long position in the common equity of Rent-A-Center Inc (NDSQ:RCII) at $36.00 per share. I calculate that the stock has an intrinsic value of $52.20 per fully diluted share today (45% upside), and believe that the company will continue to compound intrinsic value for many years to come through cash flow generation and investment in high ROIC adjacencies to its core business. I. INVESTMENT THESIS: At $36.00/share, investors have the opportunity to purchase RCII’s Core U.S. rent-to-own (RTO) retail business at fair value (12.5x unlevered FCF), while receiving the company’s two high ROIC growth initiatives – RAC Acceptance (49.8% post-corporate, fully-taxed IRR on new stores) and International RTO (13.4% IRR) for free. ( See Section IV. for Discussion and Valuation of Core U.S. Division) By the end of 2012, RCII will have 950 RAC Acceptance kiosks located within third party retail locations, up from less than 100 at the beginning of 2010. These 950 stores will reach maturity by 2015, at which point they will contribute an additional $170 million of EBITDA and $100 million of unlevered free cash flow under conservative assumptions. Although I only include the 950 stores expected to be open by the end of 2012