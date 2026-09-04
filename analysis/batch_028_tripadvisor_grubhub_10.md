# Batch 028 — TripAdvisor · Grubhub 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

## 결론부터

이번 배치는 같은 산업 안에서 **규모 성장과 경제성, 그리고 가격 결과를 분리**해 postmortem한다. 원 SQL raw flag는 보존하고 본문 기준 실제 방향을 research layer에 기록했다.

---

# TRIPADVISOR INC (TRIP)

## 기업과 비즈니스

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

## 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

## 경쟁우위·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

| 게시일 | 실제방향 | 논지 | 결과 |
|---|---|---|---|
| 2012-05-02 | Short | decelerating growth premium-multiple Short | 실패 |
| 2012-07-10 | Long | click-based growth Long | 강한 성공 |
| 2016-08-30 | Long | Instant Booking reinvestment Long | 실패 |
| 2018-02-01 | Long | investor fatigue/non-hotel optionality Long | 부분 적중 |
| 2018-08-04 | Long | Experiences/Restaurants unit-economics Long | 성공 |
| 2021-02-22 | Long | subscription transformation Long | 실패 |

---

<!-- idea:3fe23c06-d9eb-4c69-9da2-207a274f4cab -->
## 1. 2012-05-02 — decelerating growth premium-multiple Short

### 결론부터

**실패.** growth deceleration을 franchise decay로 너무 빨리 연결

**증권 결과:** 초기 Short 구조적 실패

### 1. 무슨 기업인가

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

### 2. 산업 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

### 4. 당시 VIC 원문과 핵심 논지

Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

### 5. 밸류에이션과 기대수익의 연결

premium growth multiple compression growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 실패 · 18%

**원 주장:** Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

**정량 괴리:** Growth: 30%→teens 우려 → 사업규모 확대

**오류/핵심:** growth deceleration을 franchise decay로 너무 빨리 연결

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 부분 · 18%

**원 주장:** Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

**정량 괴리:** Competition: 증가 → 장기 현실화

**오류/핵심:** growth deceleration을 franchise decay로 너무 빨리 연결

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 부분 · 16%

**원 주장:** Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

**정량 괴리:** Pricing: 약화 우려 → metasearch monetization 유지

**오류/핵심:** growth deceleration을 franchise decay로 너무 빨리 연결

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 실패 · 16%

**원 주장:** Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

**정량 괴리:** Moat: 약화 → UGC scale 지속

**오류/핵심:** growth deceleration을 franchise decay로 너무 빨리 연결

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 실패 · 16%

**원 주장:** Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

**정량 괴리:** Growth: 30%→teens 우려 → 사업규모 확대

**오류/핵심:** growth deceleration을 franchise decay로 너무 빨리 연결

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 실패 · 16%

**원 주장:** Q4 30% 성장에서 mid/high-teens 가이던스로 급감하고 경쟁·pricing pressure가 premium multiple을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

**정량 괴리:** Competition: 증가 → 장기 현실화

**오류/핵심:** growth deceleration을 franchise decay로 너무 빨리 연결

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

TripAdvisor traffic과 metasearch는 이후 수년 더 성장했고 2012~14 business scale이 확대됨

### 7. 사업 결과와 가격 결과 분리

초기 Short 구조적 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

growth deceleration을 franchise decay로 너무 빨리 연결

### 9. 최초 검증·반증 신호와 회피 가능성

2013-12-31 — traffic/revenue가 계속 성장 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

실패 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Growth | 30%→teens 우려 | 사업규모 확대 | 실패 |
| Competition | 증가 | 장기 현실화 | 부분 |
| Pricing | 약화 우려 | metasearch monetization 유지 | 부분 |
| Moat | 약화 | UGC scale 지속 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2012-05-02 | VIC 게시 | decelerating growth premium-multiple Short |
| 2013-12-31 | 최초 검증·반증 신호 | traffic/revenue가 계속 성장 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: growth deceleration을 franchise decay로 너무 빨리 연결
- 최초 signal: 2013-12-31 — traffic/revenue가 계속 성장
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC TRIP 2012-05-02 — Value Investors Club / user SQL
- [2. TripAdvisor 2016 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000156459017003118/trip-10k_20161231.htm) — SEC
- [3. TripAdvisor 2021 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652022000011/trip-20211231.htm) — SEC
- [4. TripAdvisor 2023 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652024000008/trip-20231231.htm) — SEC
- [5. TripAdvisor IR](https://ir.tripadvisor.com/) — Tripadvisor
- [6. Tripadvisor company](https://www.tripadvisor.com/) — Tripadvisor

---

<!-- idea:9e0e1746-8cb0-4fa9-8503-84472dcd5185 -->
## 2. 2012-07-10 — click-based growth Long

### 결론부터

**강한 성공.** 초기 traffic/monetization flywheel을 잘 봄

**증권 결과:** 초기 강한 성공

### 1. 무슨 기업인가

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

### 2. 산업 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

### 4. 당시 VIC 원문과 핵심 논지

2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

### 5. 밸류에이션과 기대수익의 연결

고성장 earnings multiple growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** 2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

**정량 괴리:** 2012E rev: $817m → 장기 $1bn+

**오류/핵심:** 초기 traffic/monetization flywheel을 잘 봄

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** 2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

**정량 괴리:** 2014E rev: $1.30bn → 규모 확대

**오류/핵심:** 초기 traffic/monetization flywheel을 잘 봄

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** 2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

**정량 괴리:** Traffic: 성장 → 지속

**오류/핵심:** 초기 traffic/monetization flywheel을 잘 봄

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** 2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

**정량 괴리:** Moat: UGC/SEO → 유지

**오류/핵심:** 초기 traffic/monetization flywheel을 잘 봄

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** 2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

**정량 괴리:** 2012E rev: $817m → 장기 $1bn+

**오류/핵심:** 초기 traffic/monetization flywheel을 잘 봄

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** 2012E revenue $817m, 2013E $1.052bn, 2014E $1.300bn과 높은 incremental margin을 기대

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

**정량 괴리:** 2014E rev: $1.30bn → 규모 확대

**오류/핵심:** 초기 traffic/monetization flywheel을 잘 봄

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

TripAdvisor는 2014~15까지 빠르게 성장하고 글로벌 travel-review leader 지위 유지

### 7. 사업 결과와 가격 결과 분리

초기 강한 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

초기 traffic/monetization flywheel을 잘 봄

### 9. 최초 검증·반증 신호와 회피 가능성

2014-12-31 — revenue와 hotel shoppers 성장 지속 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| 2012E rev | $817m | 장기 $1bn+ | 적중 |
| 2014E rev | $1.30bn | 규모 확대 | 적중 |
| Traffic | 성장 | 지속 | 적중 |
| Moat | UGC/SEO | 유지 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2012-07-10 | VIC 게시 | click-based growth Long |
| 2014-12-31 | 최초 검증·반증 신호 | revenue와 hotel shoppers 성장 지속 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 초기 traffic/monetization flywheel을 잘 봄
- 최초 signal: 2014-12-31 — revenue와 hotel shoppers 성장 지속
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC TRIP 2012-07-10 — Value Investors Club / user SQL
- [2. TripAdvisor 2016 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000156459017003118/trip-10k_20161231.htm) — SEC
- [3. TripAdvisor 2021 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652022000011/trip-20211231.htm) — SEC
- [4. TripAdvisor 2023 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652024000008/trip-20231231.htm) — SEC
- [5. TripAdvisor IR](https://ir.tripadvisor.com/) — Tripadvisor
- [6. Tripadvisor company](https://www.tripadvisor.com/) — Tripadvisor

---

<!-- idea:82849da2-f8c0-485e-a518-90f35502fcdd -->
## 3. 2016-08-30 — Instant Booking reinvestment Long

### 결론부터

**실패.** temporary reinvestment와 business-model monetization impairment를 혼동

**증권 결과:** Long 실패

### 1. 무슨 기업인가

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

### 2. 산업 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

### 4. 당시 VIC 원문과 핵심 논지

$62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

### 5. 밸류에이션과 기대수익의 연결

normalized hotel monetization growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 실패 · 18%

**원 주장:** $62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

**정량 괴리:** Hotel rev: 회복 기대 → 2016 -6%

**오류/핵심:** temporary reinvestment와 business-model monetization impairment를 혼동

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 부분 · 18%

**원 주장:** $62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

**정량 괴리:** Shopper growth: +6% → traffic 유지

**오류/핵심:** temporary reinvestment와 business-model monetization impairment를 혼동

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 실패 · 16%

**원 주장:** $62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

**정량 괴리:** Rev/shopper: 회복 기대 → -15%

**오류/핵심:** temporary reinvestment와 business-model monetization impairment를 혼동

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 실패 · 16%

**원 주장:** $62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

**정량 괴리:** IB: 장기 개선 → 기대 미달

**오류/핵심:** temporary reinvestment와 business-model monetization impairment를 혼동

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 실패 · 16%

**원 주장:** $62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

**정량 괴리:** Hotel rev: 회복 기대 → 2016 -6%

**오류/핵심:** temporary reinvestment와 business-model monetization impairment를 혼동

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 실패 · 16%

**원 주장:** $62에서 Instant Booking rollout이 현재 monetization을 일시적으로 눌렀을 뿐 장기 conversion·economics를 높인다고 봄

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

**정량 괴리:** Shopper growth: +6% → traffic 유지

**오류/핵심:** temporary reinvestment와 business-model monetization impairment를 혼동

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2016 Hotel revenue -6%, hotel shoppers +6%인데 revenue/shopper -15%; Instant Booking economics가 기대만큼 회복되지 않음

### 7. 사업 결과와 가격 결과 분리

Long 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

temporary reinvestment와 business-model monetization impairment를 혼동

### 9. 최초 검증·반증 신호와 회피 가능성

2017-12-31 — Instant Booking이 기대한 monetization 회복을 만들지 못함 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

실패 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Hotel rev | 회복 기대 | 2016 -6% | 실패 |
| Shopper growth | +6% | traffic 유지 | 부분 |
| Rev/shopper | 회복 기대 | -15% | 실패 |
| IB | 장기 개선 | 기대 미달 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2016-08-30 | VIC 게시 | Instant Booking reinvestment Long |
| 2017-12-31 | 최초 검증·반증 신호 | Instant Booking이 기대한 monetization 회복을 만들지 못함 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: temporary reinvestment와 business-model monetization impairment를 혼동
- 최초 signal: 2017-12-31 — Instant Booking이 기대한 monetization 회복을 만들지 못함
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC TRIP 2016-08-30 — Value Investors Club / user SQL
- [2. TripAdvisor 2016 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000156459017003118/trip-10k_20161231.htm) — SEC
- [3. TripAdvisor 2021 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652022000011/trip-20211231.htm) — SEC
- [4. TripAdvisor 2023 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652024000008/trip-20231231.htm) — SEC
- [5. TripAdvisor IR](https://ir.tripadvisor.com/) — Tripadvisor
- [6. Tripadvisor company](https://www.tripadvisor.com/) — Tripadvisor

---

<!-- idea:b5883b54-4a4a-46b9-b7d1-8a929bc9c9a5 -->
## 4. 2018-02-01 — investor fatigue/non-hotel optionality Long

### 결론부터

**부분 적중.** non-hotel option은 맞고 core turnaround durability는 과대

**증권 결과:** 부분 성공

### 1. 무슨 기업인가

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

### 2. 산업 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

### 4. 당시 VIC 원문과 핵심 논지

3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

### 5. 밸류에이션과 기대수익의 연결

SOTP hotel + non-hotel growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** 3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

**정량 괴리:** Non-hotel: hidden value → Viator/TheFork 성장

**오류/핵심:** non-hotel option은 맞고 core turnaround durability는 과대

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 부분 실패 · 18%

**원 주장:** 3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

**정량 괴리:** Hotel: 회복 → 장기 압박

**오류/핵심:** non-hotel option은 맞고 core turnaround durability는 과대

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** 3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

**정량 괴리:** Expectations: 낮음 → 단기 rerating

**오류/핵심:** non-hotel option은 맞고 core turnaround durability는 과대

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 부분 · 16%

**원 주장:** 3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

**정량 괴리:** Horizon: 3-5y → mixed

**오류/핵심:** non-hotel option은 맞고 core turnaround durability는 과대

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 부분 적중 · 16%

**원 주장:** 3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

**정량 괴리:** Non-hotel: hidden value → Viator/TheFork 성장

**오류/핵심:** non-hotel option은 맞고 core turnaround durability는 과대

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 부분 적중 · 16%

**원 주장:** 3~5년 horizon에서 낮은 기대와 Non-Hotel 가치가 core Hotel misexecution을 상쇄할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

**정량 괴리:** Hotel: 회복 → 장기 압박

**오류/핵심:** non-hotel option은 맞고 core turnaround durability는 과대

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2018 중 주가/사업이 회복했지만 Brand Tripadvisor는 장기 압박, Viator/TheFork가 가치원천으로 커짐

### 7. 사업 결과와 가격 결과 분리

부분 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

non-hotel option은 맞고 core turnaround durability는 과대

### 9. 최초 검증·반증 신호와 회피 가능성

2018-08-31 — Experiences/Dining 성장과 단기 rerating 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

부분 적중 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Non-hotel | hidden value | Viator/TheFork 성장 | 적중 |
| Hotel | 회복 | 장기 압박 | 부분 실패 |
| Expectations | 낮음 | 단기 rerating | 적중 |
| Horizon | 3-5y | mixed | 부분 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2018-02-01 | VIC 게시 | investor fatigue/non-hotel optionality Long |
| 2018-08-31 | 최초 검증·반증 신호 | Experiences/Dining 성장과 단기 rerating |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: non-hotel option은 맞고 core turnaround durability는 과대
- 최초 signal: 2018-08-31 — Experiences/Dining 성장과 단기 rerating
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC TRIP 2018-02-01 — Value Investors Club / user SQL
- [2. TripAdvisor 2016 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000156459017003118/trip-10k_20161231.htm) — SEC
- [3. TripAdvisor 2021 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652022000011/trip-20211231.htm) — SEC
- [4. TripAdvisor 2023 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652024000008/trip-20231231.htm) — SEC
- [5. TripAdvisor IR](https://ir.tripadvisor.com/) — Tripadvisor
- [6. Tripadvisor company](https://www.tripadvisor.com/) — Tripadvisor

---

<!-- idea:2662bb35-e5d8-434d-8db6-dffcbdf108fa -->
## 5. 2018-08-04 — Experiences/Restaurants unit-economics Long

### 결론부터

**성공.** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**증권 결과:** 사업논지 성공·주가경로 혼합

### 1. 무슨 기업인가

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

### 2. 산업 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

### 4. 당시 VIC 원문과 핵심 논지

Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

### 5. 밸류에이션과 기대수익의 연결

SOTP with growing non-hotel growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 부분 · 18%

**원 주장:** Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

**정량 괴리:** Hotel shoppers: -2.6% → core mixed

**오류/핵심:** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

**정량 괴리:** Viator: 고성장 → $737m 2023

**오류/핵심:** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

**정량 괴리:** TheFork: 고성장 → $154m 2023

**오류/핵심:** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

**정량 괴리:** SOTP: non-hotel value → 현실화

**오류/핵심:** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 성공 · 16%

**원 주장:** Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

**정량 괴리:** Hotel shoppers: -2.6% → core mixed

**오류/핵심:** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 성공 · 16%

**원 주장:** Hotel shoppers -2.6% 반응이 과도하며 Viator/Restaurants의 unit economics와 runway가 큰 가치

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

**정량 괴리:** Viator: 고성장 → $737m 2023

**오류/핵심:** 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2023 Viator revenue $737m, TheFork $154m으로 Non-Hotel thesis가 실제 큰 segment로 성장; Brand revenue $1.031bn

### 7. 사업 결과와 가격 결과 분리

사업논지 성공·주가경로 혼합 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

기업 전체보다 segment별 profit pool을 분리한 점이 좋았음

### 9. 최초 검증·반증 신호와 회피 가능성

2023-12-31 — Viator/TheFork가 독립적으로 큰 revenue pools가 됨 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Hotel shoppers | -2.6% | core mixed | 부분 |
| Viator | 고성장 | $737m 2023 | 적중 |
| TheFork | 고성장 | $154m 2023 | 적중 |
| SOTP | non-hotel value | 현실화 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2018-08-04 | VIC 게시 | Experiences/Restaurants unit-economics Long |
| 2023-12-31 | 최초 검증·반증 신호 | Viator/TheFork가 독립적으로 큰 revenue pools가 됨 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 기업 전체보다 segment별 profit pool을 분리한 점이 좋았음
- 최초 signal: 2023-12-31 — Viator/TheFork가 독립적으로 큰 revenue pools가 됨
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC TRIP 2018-08-04 — Value Investors Club / user SQL
- [2. TripAdvisor 2016 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000156459017003118/trip-10k_20161231.htm) — SEC
- [3. TripAdvisor 2021 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652022000011/trip-20211231.htm) — SEC
- [4. TripAdvisor 2023 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652024000008/trip-20231231.htm) — SEC
- [5. TripAdvisor IR](https://ir.tripadvisor.com/) — Tripadvisor
- [6. Tripadvisor company](https://www.tripadvisor.com/) — Tripadvisor

---

<!-- idea:15f4534e-2738-4f55-8662-5db3fde58aee -->
## 6. 2021-02-22 — subscription transformation Long

### 결론부터

**실패.** recovery와 subscription-model success를 함께 묶어 과대평가

**증권 결과:** Long 실패

### 1. 무슨 기업인가

TripAdvisor는 여행자 리뷰·평점·사진을 축적해 대규모 여행 traffic을 만들고 호텔·OTA에 metasearch click/booking lead를 판매한다. Viator Experiences와 TheFork Dining도 운영한다. 핵심 KPI는 hotel shoppers, revenue per shopper, CPC/CPA monetization, direct traffic, marketing efficiency, Viator gross bookings/revenue, TheFork bookings와 segment EBITDA다.

### 2. 산업 가치사슬과 돈의 흐름

UGC/SEO/brand가 여행자를 모으고 hotel shoppers의 click·booking을 OTA/호텔에 monetization한다. Instant Booking은 click-out 대신 TripAdvisor 안에서 booking을 완결해 conversion을 높이려 했지만 monetization 전환비용이 컸다. Viator/TheFork는 booking volume×take rate에서 CAC/merchant acquisition costs를 뺀다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

리뷰 corpus·브랜드·direct traffic이 장점이나 Google travel surfaces와 Booking/Expedia의 direct relationship이 위협이다. 핵심은 traffic 자체보다 revenue per shopper와 paid-marketing 의존도다.

### 4. 당시 VIC 원문과 핵심 논지

B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

### 5. 밸류에이션과 기대수익의 연결

$585-590m EBITDA recovery thesis growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 실패 · 18%

**원 주장:** B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

**정량 괴리:** Subscription: 핵심전환 → 미정착

**오류/핵심:** recovery와 subscription-model success를 함께 묶어 과대평가

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 부분 · 18%

**원 주장:** B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

**정량 괴리:** Revenue: 2019 초과 → 2023 $1.788bn

**오류/핵심:** recovery와 subscription-model success를 함께 묶어 과대평가

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 실패 · 16%

**원 주장:** B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

**정량 괴리:** EBITDA: $585m+ → 기대 미달

**오류/핵심:** recovery와 subscription-model success를 함께 묶어 과대평가

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 논지변경 · 16%

**원 주장:** B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

**정량 괴리:** Viator: 보조 → 주요 성장원

**오류/핵심:** recovery와 subscription-model success를 함께 묶어 과대평가

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 실패 · 16%

**원 주장:** B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

**정량 괴리:** Subscription: 핵심전환 → 미정착

**오류/핵심:** recovery와 subscription-model success를 함께 묶어 과대평가

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 실패 · 16%

**원 주장:** B2B metasearch에서 consumer subscription 중심으로 바뀌며 2019 peak EBITDA를 크게 초과할 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

**정량 괴리:** Revenue: 2019 초과 → 2023 $1.788bn

**오류/핵심:** recovery와 subscription-model success를 함께 묶어 과대평가

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

Tripadvisor Plus 유료 subscription thesis는 중심 business model이 되지 못했고 2023 성장은 Viator/experiences가 주도

### 7. 사업 결과와 가격 결과 분리

Long 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

recovery와 subscription-model success를 함께 묶어 과대평가

### 9. 최초 검증·반증 신호와 회피 가능성

2022-12-31 — paid subscription이 핵심 monetization engine으로 자리잡지 못함 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

실패 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Subscription | 핵심전환 | 미정착 | 실패 |
| Revenue | 2019 초과 | 2023 $1.788bn | 부분 |
| EBITDA | $585m+ | 기대 미달 | 실패 |
| Viator | 보조 | 주요 성장원 | 논지변경 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2021-02-22 | VIC 게시 | subscription transformation Long |
| 2022-12-31 | 최초 검증·반증 신호 | paid subscription이 핵심 monetization engine으로 자리잡지 못함 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: recovery와 subscription-model success를 함께 묶어 과대평가
- 최초 signal: 2022-12-31 — paid subscription이 핵심 monetization engine으로 자리잡지 못함
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC TRIP 2021-02-22 — Value Investors Club / user SQL
- [2. TripAdvisor 2016 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000156459017003118/trip-10k_20161231.htm) — SEC
- [3. TripAdvisor 2021 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652022000011/trip-20211231.htm) — SEC
- [4. TripAdvisor 2023 10-K](https://www.sec.gov/Archives/edgar/data/1526520/000152652024000008/trip-20231231.htm) — SEC
- [5. TripAdvisor IR](https://ir.tripadvisor.com/) — Tripadvisor
- [6. Tripadvisor company](https://www.tripadvisor.com/) — Tripadvisor
---

# GRUBHUB INC (GRUB)

## 기업과 비즈니스

Grubhub는 식당과 소비자를 연결하는 online food-ordering marketplace였다. 초기에는 restaurant delivery를 중개하는 asset-light model이었지만 자체 delivery 비중이 늘면서 logistics economics가 중요해졌다. 핵심 KPI는 active diners, Daily Average Grubs, Gross Food Sales, revenue/capture rate, restaurant count, own-delivery mix와 contribution margin이다.

## 가치사슬과 돈의 흐름

active diners와 restaurants가 주문을 만들고 GFS×commission이 revenue가 된다. own-delivery는 take rate를 높일 수 있지만 courier pay·insurance·support가 추가돼 gross revenue와 economic profit이 다르게 움직일 수 있다.

## 경쟁우위·핵심 KPI

초기 local density와 restaurant selection이 강점이었지만 diner/restaurant 모두 multi-homing이 쉽고 DoorDash/Uber 등 subsidized entrants가 network effect를 약화시켰다.

| 게시일 | 실제방향 | 논지 | 결과 |
|---|---|---|---|
| 2015-02-02 | Long | dominant two-sided network Long | 부분 성공 |
| 2015-03-31 | Short | 20% growth/re-rating Short | 혼합 |
| 2015-12-09 | Long | 35k restaurants/6.4m diners network Long | 성공 |
| 2016-04-14 | Short | no-network-effect/delivery war Short | 부분 적중 |

---

<!-- idea:297e22cb-efd5-4177-9a68-f8d859f3bc8d -->
## 1. 2015-02-02 — dominant two-sided network Long

### 결론부터

**부분 성공.** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**증권 결과:** 중기 성공·장기 moat 과대

### 1. 무슨 기업인가

Grubhub는 식당과 소비자를 연결하는 online food-ordering marketplace였다. 초기에는 restaurant delivery를 중개하는 asset-light model이었지만 자체 delivery 비중이 늘면서 logistics economics가 중요해졌다. 핵심 KPI는 active diners, Daily Average Grubs, Gross Food Sales, revenue/capture rate, restaurant count, own-delivery mix와 contribution margin이다.

### 2. 산업 가치사슬과 돈의 흐름

active diners와 restaurants가 주문을 만들고 GFS×commission이 revenue가 된다. own-delivery는 take rate를 높일 수 있지만 courier pay·insurance·support가 추가돼 gross revenue와 economic profit이 다르게 움직일 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

초기 local density와 restaurant selection이 강점이었지만 diner/restaurant 모두 multi-homing이 쉽고 DoorDash/Uber 등 subsidized entrants가 network effect를 약화시켰다.

### 4. 당시 VIC 원문과 핵심 논지

Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

### 5. 밸류에이션과 기대수익의 연결

platform growth multiple growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

**정량 괴리:** Diners: 고성장 → 31.4m 2020

**오류/핵심:** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

**정량 괴리:** GFS: 확대 → $8.7bn

**오류/핵심:** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 부분 실패 · 16%

**원 주장:** Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

**정량 괴리:** Share: dominant → 경쟁심화

**오류/핵심:** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 부분 실패 · 16%

**원 주장:** Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

**정량 괴리:** Moat: network effect → multi-homing 약화

**오류/핵심:** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 부분 성공 · 16%

**원 주장:** Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

**정량 괴리:** Diners: 고성장 → 31.4m 2020

**오류/핵심:** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 부분 성공 · 16%

**원 주장:** Grubhub/Seamless 합병 후 약 65% share와 restaurant/diner network effect가 장기 compounder를 만든다

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

**정량 괴리:** GFS: 확대 → $8.7bn

**오류/핵심:** 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2015 active diners 6.746m·DAG 227.1k·GFS $2.354bn, 2020 diners 31.4m·GFS $8.7bn; 그러나 delivery 경쟁으로 moat/margins 약화 후 2021 JET에 인수

### 7. 사업 결과와 가격 결과 분리

중기 성공·장기 moat 과대 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가

### 9. 최초 검증·반증 신호와 회피 가능성

2018-12-31 — 규모는 급성장했으나 own-delivery 경쟁이 economics를 변화 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

부분 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Diners | 고성장 | 31.4m 2020 | 적중 |
| GFS | 확대 | $8.7bn | 적중 |
| Share | dominant | 경쟁심화 | 부분 실패 |
| Moat | network effect | multi-homing 약화 | 부분 실패 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2015-02-02 | VIC 게시 | dominant two-sided network Long |
| 2018-12-31 | 최초 검증·반증 신호 | 규모는 급성장했으나 own-delivery 경쟁이 economics를 변화 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 초기 network growth는 적중했지만 multi-homing과 logistics competition을 과소평가
- 최초 signal: 2018-12-31 — 규모는 급성장했으나 own-delivery 경쟁이 economics를 변화
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC GRUB 2015-02-02 — Value Investors Club / user SQL
- [2. Grubhub 2015 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459016013426/grub-10k_20151231.htm) — SEC
- [3. Grubhub 2016 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459017002838/grub-10k_20161231.htm) — SEC
- [4. Grubhub 2020 proxy metrics](https://www.sec.gov/Archives/edgar/data/1594109/000156459021021335/grub-def14a_20210618.htm) — SEC
- [5. JET Grubhub acquisition](https://www.justeattakeaway.com/newsroom/en-WW/202220-just-eat-takeaway-com-completes-acquisition-of-grubhub/) — Just Eat Takeaway
- [6. Grubhub product](https://www.grubhub.com/) — Grubhub

---

<!-- idea:fb426fb2-511f-4688-b53e-c6662aed360b -->
## 2. 2015-03-31 — 20% growth/re-rating Short

### 결론부터

**혼합.** 가격방향과 핵심 fundamental forecast를 분리해야 함

**증권 결과:** 가격 성공·인과 실패

### 1. 무슨 기업인가

Grubhub는 식당과 소비자를 연결하는 online food-ordering marketplace였다. 초기에는 restaurant delivery를 중개하는 asset-light model이었지만 자체 delivery 비중이 늘면서 logistics economics가 중요해졌다. 핵심 KPI는 active diners, Daily Average Grubs, Gross Food Sales, revenue/capture rate, restaurant count, own-delivery mix와 contribution margin이다.

### 2. 산업 가치사슬과 돈의 흐름

active diners와 restaurants가 주문을 만들고 GFS×commission이 revenue가 된다. own-delivery는 take rate를 높일 수 있지만 courier pay·insurance·support가 추가돼 gross revenue와 economic profit이 다르게 움직일 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

초기 local density와 restaurant selection이 강점이었지만 diner/restaurant 모두 multi-homing이 쉽고 DoorDash/Uber 등 subsidized entrants가 network effect를 약화시켰다.

### 4. 당시 VIC 원문과 핵심 논지

NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

### 5. 밸류에이션과 기대수익의 연결

3x EV/Sales, $14 target growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 실패 · 18%

**원 주장:** NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

**정량 괴리:** Revenue growth: 20% → +43%

**오류/핵심:** 가격방향과 핵심 fundamental forecast를 분리해야 함

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 부분 · 18%

**원 주장:** NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

**정량 괴리:** EV/Sales: 8.5x→3x → multiple 압축

**오류/핵심:** 가격방향과 핵심 fundamental forecast를 분리해야 함

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 실패 · 16%

**원 주장:** NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

**정량 괴리:** Diners: 둔화 → +34%

**오류/핵심:** 가격방향과 핵심 fundamental forecast를 분리해야 함

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

**정량 괴리:** Price: 하락 기대 → 하락

**오류/핵심:** 가격방향과 핵심 fundamental forecast를 분리해야 함

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 혼합 · 16%

**원 주장:** NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

**정량 괴리:** Revenue growth: 20% → +43%

**오류/핵심:** 가격방향과 핵심 fundamental forecast를 분리해야 함

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 혼합 · 16%

**원 주장:** NY 확장한계·경쟁·AG ruling·weather comp로 2015 revenue growth 약 20%, EV/Sales 8.5x→3x와 $14 target

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

**정량 괴리:** EV/Sales: 8.5x→3x → multiple 압축

**오류/핵심:** 가격방향과 핵심 fundamental forecast를 분리해야 함

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

실제 2015 revenue는 약 $361.8m로 +43%, diners +34%, GFS +32%; 그럼에도 주가는 경쟁우려로 하락

### 7. 사업 결과와 가격 결과 분리

가격 성공·인과 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가격방향과 핵심 fundamental forecast를 분리해야 함

### 9. 최초 검증·반증 신호와 회피 가능성

2015-12-31 — 실제 revenue growth가 +43%로 20% 가정 반증 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

혼합 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Revenue growth | 20% | +43% | 실패 |
| EV/Sales | 8.5x→3x | multiple 압축 | 부분 |
| Diners | 둔화 | +34% | 실패 |
| Price | 하락 기대 | 하락 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2015-03-31 | VIC 게시 | 20% growth/re-rating Short |
| 2015-12-31 | 최초 검증·반증 신호 | 실제 revenue growth가 +43%로 20% 가정 반증 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 가격방향과 핵심 fundamental forecast를 분리해야 함
- 최초 signal: 2015-12-31 — 실제 revenue growth가 +43%로 20% 가정 반증
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC GRUB 2015-03-31 — Value Investors Club / user SQL
- [2. Grubhub 2015 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459016013426/grub-10k_20151231.htm) — SEC
- [3. Grubhub 2016 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459017002838/grub-10k_20161231.htm) — SEC
- [4. Grubhub 2020 proxy metrics](https://www.sec.gov/Archives/edgar/data/1594109/000156459021021335/grub-def14a_20210618.htm) — SEC
- [5. JET Grubhub acquisition](https://www.justeattakeaway.com/newsroom/en-WW/202220-just-eat-takeaway-com-completes-acquisition-of-grubhub/) — Just Eat Takeaway
- [6. Grubhub product](https://www.grubhub.com/) — Grubhub

---

<!-- idea:354670a9-fe9c-4b48-b730-b5ae1ca1f2cc -->
## 3. 2015-12-09 — 35k restaurants/6.4m diners network Long

### 결론부터

**성공.** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**증권 결과:** 중기 강한 성공

### 1. 무슨 기업인가

Grubhub는 식당과 소비자를 연결하는 online food-ordering marketplace였다. 초기에는 restaurant delivery를 중개하는 asset-light model이었지만 자체 delivery 비중이 늘면서 logistics economics가 중요해졌다. 핵심 KPI는 active diners, Daily Average Grubs, Gross Food Sales, revenue/capture rate, restaurant count, own-delivery mix와 contribution margin이다.

### 2. 산업 가치사슬과 돈의 흐름

active diners와 restaurants가 주문을 만들고 GFS×commission이 revenue가 된다. own-delivery는 take rate를 높일 수 있지만 courier pay·insurance·support가 추가돼 gross revenue와 economic profit이 다르게 움직일 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

초기 local density와 restaurant selection이 강점이었지만 diner/restaurant 모두 multi-homing이 쉽고 DoorDash/Uber 등 subsidized entrants가 network effect를 약화시켰다.

### 4. 당시 VIC 원문과 핵심 논지

6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

### 5. 밸류에이션과 기대수익의 연결

growth platform valuation growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** 6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

**정량 괴리:** Diners: 6.4m → 31.4m 2020

**오류/핵심:** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** 6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

**정량 괴리:** Restaurants: 35k+ → 265k+ partners

**오류/핵심:** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** 6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

**정량 괴리:** GFS: $2.2bn → $8.7bn

**오류/핵심:** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 부분 · 16%

**원 주장:** 6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

**정량 괴리:** Margin: 26% → delivery 투자로 압박

**오류/핵심:** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 성공 · 16%

**원 주장:** 6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

**정량 괴리:** Diners: 6.4m → 31.4m 2020

**오류/핵심:** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 성공 · 16%

**원 주장:** 6.4m active diners·35k+ restaurants·15.5% take rate·26% Adj EBITDA margin의 two-sided platform이 성장

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

**정량 괴리:** Restaurants: 35k+ → 265k+ partners

**오류/핵심:** 초기 scale economics와 volume runway는 정확, durable monopoly는 과대

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2016 diners 8.174m·GFS $2.998bn, 이후 2020 diners 31.4m·GFS $8.7bn까지 성장; 장기 경쟁으로 margins 압박

### 7. 사업 결과와 가격 결과 분리

중기 강한 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

초기 scale economics와 volume runway는 정확, durable monopoly는 과대

### 9. 최초 검증·반증 신호와 회피 가능성

2018-09-30 — orders/diners 성장과 주가 rerating 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Diners | 6.4m | 31.4m 2020 | 적중 |
| Restaurants | 35k+ | 265k+ partners | 적중 |
| GFS | $2.2bn | $8.7bn | 적중 |
| Margin | 26% | delivery 투자로 압박 | 부분 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2015-12-09 | VIC 게시 | 35k restaurants/6.4m diners network Long |
| 2018-09-30 | 최초 검증·반증 신호 | orders/diners 성장과 주가 rerating |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 초기 scale economics와 volume runway는 정확, durable monopoly는 과대
- 최초 signal: 2018-09-30 — orders/diners 성장과 주가 rerating
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC GRUB 2015-12-09 — Value Investors Club / user SQL
- [2. Grubhub 2015 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459016013426/grub-10k_20151231.htm) — SEC
- [3. Grubhub 2016 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459017002838/grub-10k_20161231.htm) — SEC
- [4. Grubhub 2020 proxy metrics](https://www.sec.gov/Archives/edgar/data/1594109/000156459021021335/grub-def14a_20210618.htm) — SEC
- [5. JET Grubhub acquisition](https://www.justeattakeaway.com/newsroom/en-WW/202220-just-eat-takeaway-com-completes-acquisition-of-grubhub/) — Just Eat Takeaway
- [6. Grubhub product](https://www.grubhub.com/) — Grubhub

---

<!-- idea:8bc3c491-7a2f-4037-8fc8-27153119b2c1 -->
## 4. 2016-04-14 — no-network-effect/delivery war Short

### 결론부터

**부분 적중.** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**증권 결과:** 장기 인과 적중·증권 timing 실패

### 1. 무슨 기업인가

Grubhub는 식당과 소비자를 연결하는 online food-ordering marketplace였다. 초기에는 restaurant delivery를 중개하는 asset-light model이었지만 자체 delivery 비중이 늘면서 logistics economics가 중요해졌다. 핵심 KPI는 active diners, Daily Average Grubs, Gross Food Sales, revenue/capture rate, restaurant count, own-delivery mix와 contribution margin이다.

### 2. 산업 가치사슬과 돈의 흐름

active diners와 restaurants가 주문을 만들고 GFS×commission이 revenue가 된다. own-delivery는 take rate를 높일 수 있지만 courier pay·insurance·support가 추가돼 gross revenue와 economic profit이 다르게 움직일 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

초기 local density와 restaurant selection이 강점이었지만 diner/restaurant 모두 multi-homing이 쉽고 DoorDash/Uber 등 subsidized entrants가 network effect를 약화시켰다.

### 4. 당시 VIC 원문과 핵심 논지

switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

### 5. 밸류에이션과 기대수익의 연결

structural competition Short growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

**정량 괴리:** Multi-home: 높음 → 지속

**오류/핵심:** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 실패 · 18%

**원 주장:** switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

**정량 괴리:** 2016 GFS: 둔화 예상 → +27%

**오류/핵심:** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

**정량 괴리:** Competition: 심화 → 현실화

**오류/핵심:** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 실패 · 16%

**원 주장:** switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

**정량 괴리:** Security: downside → 2018 대폭 상승

**오류/핵심:** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 부분 적중 · 16%

**원 주장:** switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

**정량 괴리:** Multi-home: 높음 → 지속

**오류/핵심:** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 부분 적중 · 16%

**원 주장:** switching cost가 0이고 restaurants가 multi-home하며 Uber/Amazon 진입으로 gory death match가 올 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

**정량 괴리:** 2016 GFS: 둔화 예상 → +27%

**오류/핵심:** 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2016 diners +21%, DAG +21%, GFS +27%로 즉시 성장 지속하고 2018 주가 급등; 장기적으로 DoorDash/Uber 경쟁과 delivery investment가 economics를 압박하고 2021 매각

### 7. 사업 결과와 가격 결과 분리

장기 인과 적중·증권 timing 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험

### 9. 최초 검증·반증 신호와 회피 가능성

2019-10-28 — 시장점유·수익성 우려가 본격화 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

부분 적중 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Multi-home | 높음 | 지속 | 적중 |
| 2016 GFS | 둔화 예상 | +27% | 실패 |
| Competition | 심화 | 현실화 | 적중 |
| Security | downside | 2018 대폭 상승 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2016-04-14 | VIC 게시 | no-network-effect/delivery war Short |
| 2019-10-28 | 최초 검증·반증 신호 | 시장점유·수익성 우려가 본격화 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 산업구조는 장기 적중했지만 timing이 매우 빨라 Short security는 위험
- 최초 signal: 2019-10-28 — 시장점유·수익성 우려가 본격화
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC GRUB 2016-04-14 — Value Investors Club / user SQL
- [2. Grubhub 2015 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459016013426/grub-10k_20151231.htm) — SEC
- [3. Grubhub 2016 10-K](https://www.sec.gov/Archives/edgar/data/1594109/000156459017002838/grub-10k_20161231.htm) — SEC
- [4. Grubhub 2020 proxy metrics](https://www.sec.gov/Archives/edgar/data/1594109/000156459021021335/grub-def14a_20210618.htm) — SEC
- [5. JET Grubhub acquisition](https://www.justeattakeaway.com/newsroom/en-WW/202220-just-eat-takeaway-com-completes-acquisition-of-grubhub/) — Just Eat Takeaway
- [6. Grubhub product](https://www.grubhub.com/) — Grubhub

---
# 배치 공통 학습

1. traffic·volume 성장과 monetization 개선을 동일시하지 않는다.
2. network effect는 multi-homing과 subsidy 이후에도 유지되는지 본다.
3. 자산집약 사업은 maintenance와 growth capex를 분리한다.
4. cycle thesis에는 만료조건을 붙인다.
5. 가격이 맞고 causal forecast가 틀릴 수 있으므로 둘을 분리 판정한다.
