# Batch 029 — U-Haul · United Rentals 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

## 결론부터

이번 배치는 같은 산업 안에서 **규모 성장과 경제성, 그리고 가격 결과를 분리**해 postmortem한다. 원 SQL raw flag는 보존하고 본문 기준 실제 방향을 research layer에 기록했다.

---

# U-HAUL HOLDING CO (UHAL)

## 기업과 비즈니스

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

## 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

## 경쟁우위·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

| 게시일 | 실제방향 | 논지 | 결과 |
|---|---|---|---|
| 2003-07-24 | Long preferred/notes | bankruptcy debt/preferred recovery | 강한 성공 |
| 2004-10-11 | Long | post-bankruptcy common hidden value | 강한 성공 |
| 2012-11-08 | Long | hub-and-spoke moat + cheap FCF Long | 강한 성공 |
| 2016-09-26 | Long | 9.5% steady-state FCF + 25m sqft storage Long | 강한 성공 |
| 2017-07-21 | Long | misunderstood moving economics Long | 강한 성공 |
| 2019-09-07 | Long | storage alone near market cap Long | 강한 성공 |
| 2020-08-20 | Short | old-world moving + storage oversupply Short | 실패 |
| 2022-08-28 | Long | 50m+ sqft storage + dominant moving Long | 성공 |

---

<!-- idea:f50e56a0-87b2-46b4-9fe8-76714d623744 -->
## 1. 2003-07-24 — bankruptcy debt/preferred recovery

### 결론부터

**강한 성공.** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**증권 결과:** 강한 성공

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

### 5. 밸류에이션과 기대수익의 연결

recovery value vs claim price growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

**정량 괴리:** Preferred: $17 이하 → recovery

**오류/핵심:** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

**정량 괴리:** Notes: 85 이하 → recovery

**오류/핵심:** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

**정량 괴리:** U-Haul: going concern → 생존

**오류/핵심:** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

**정량 괴리:** Bankruptcy: value destruction → 재조직

**오류/핵심:** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

**정량 괴리:** Preferred: $17 이하 → recovery

**오류/핵심:** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** AMERCO Chapter 11에서 $25 face preferred를 $17 이하, senior notes를 85 이하에 사면 U-Haul·real estate·insurance asset value가 recovery를 지지

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

**정량 괴리:** Notes: 85 이하 → recovery

**오류/핵심:** distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

AMERCO는 2004 bankruptcy에서 재조직되고 U-Haul franchise를 유지하며 후속 common value가 크게 성장

### 7. 사업 결과와 가격 결과 분리

강한 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석

### 9. 최초 검증·반증 신호와 회피 가능성

2004-03-31 — reorganization plan과 operating franchise 생존 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Preferred | $17 이하 | recovery | 적중 |
| Notes | 85 이하 | recovery | 적중 |
| U-Haul | going concern | 생존 | 적중 |
| Bankruptcy | value destruction | 재조직 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2003-07-24 | VIC 게시 | bankruptcy debt/preferred recovery |
| 2004-03-31 | 최초 검증·반증 신호 | reorganization plan과 operating franchise 생존 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: distress에서 operating franchise와 legal waterfall을 분리한 좋은 분석
- 최초 signal: 2004-03-31 — reorganization plan과 operating franchise 생존
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2003-07-24 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:a2145f41-ecf6-4eb4-a8e2-1e50d0f5ed91 -->
## 2. 2004-10-11 — post-bankruptcy common hidden value

### 결론부터

**강한 성공.** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**증권 결과:** 장기 전설적 성공

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

### 5. 밸류에이션과 기대수익의 연결

SOTP moving+storage+insurance growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** 초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

**정량 괴리:** Network: 압도적 → 유지/확대

**오류/핵심:** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** 초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

**정량 괴리:** Storage: hidden asset → 대규모 성장

**오류/핵심:** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** 초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

**정량 괴리:** Debt: reorg burden → 정상화

**오류/핵심:** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** 초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

**정량 괴리:** Equity: 추가 double → 장기 크게 초과

**오류/핵심:** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** 초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

**정량 괴리:** Network: 압도적 → 유지/확대

**오류/핵심:** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** 초기 진입 후 8배 오른 주식도 bankruptcy cleanup 뒤 DIY moving·storage·insurance의 normalized value 대비 여전히 싸서 추가 double 가능

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

**정량 괴리:** Storage: hidden asset → 대규모 성장

**오류/핵심:** 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

U-Haul은 이후 장기간 moving network와 storage를 확대하며 기업가치가 크게 증가

### 7. 사업 결과와 가격 결과 분리

장기 전설적 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음

### 9. 최초 검증·반증 신호와 회피 가능성

2006-03-31 — 재조직 후 operating cash flow와 deleveraging 지속 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Network | 압도적 | 유지/확대 | 적중 |
| Storage | hidden asset | 대규모 성장 | 적중 |
| Debt | reorg burden | 정상화 | 적중 |
| Equity | 추가 double | 장기 크게 초과 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2004-10-11 | VIC 게시 | post-bankruptcy common hidden value |
| 2006-03-31 | 최초 검증·반증 신호 | 재조직 후 operating cash flow와 deleveraging 지속 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 과거 가격상승률보다 post-reorg earning power와 assets를 재산정한 점이 좋았음
- 최초 signal: 2006-03-31 — 재조직 후 operating cash flow와 deleveraging 지속
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2004-10-11 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:75e37670-1d1d-4d30-a9e1-46e9d3c70184 -->
## 3. 2012-11-08 — hub-and-spoke moat + cheap FCF Long

### 결론부터

**강한 성공.** network density와 owner-operated capital allocation을 잘 봄

**증권 결과:** 장기 강한 성공

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

### 5. 밸류에이션과 기대수익의 연결

high FCF yield + low multiples growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

**정량 괴리:** Moving rev: 성장 → 2019 $2.653bn

**오류/핵심:** network density와 owner-operated capital allocation을 잘 봄

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

**정량 괴리:** Storage: 확대 → 지속 확대

**오류/핵심:** network density와 owner-operated capital allocation을 잘 봄

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

**정량 괴리:** Competition: 약함 → network 유지

**오류/핵심:** network density와 owner-operated capital allocation을 잘 봄

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

**정량 괴리:** Capital allocation: owner focus → 장기 reinvestment

**오류/핵심:** network density와 owner-operated capital allocation을 잘 봄

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

**정량 괴리:** Moving rev: 성장 → 2019 $2.653bn

**오류/핵심:** network density와 owner-operated capital allocation을 잘 봄

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** DIY moving의 hub-and-spoke network가 경쟁사보다 압도적이고 FCF yield/P-E/EV-EBITDA가 낮으며 owner-management가 자본배분에 집중

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

**정량 괴리:** Storage: 확대 → 지속 확대

**오류/핵심:** network density와 owner-operated capital allocation을 잘 봄

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2019 self-moving rental revenue $2.653bn, self-storage $367m으로 성장하고 이후 storage footprint도 크게 확대

### 7. 사업 결과와 가격 결과 분리

장기 강한 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

network density와 owner-operated capital allocation을 잘 봄

### 9. 최초 검증·반증 신호와 회피 가능성

2015-03-31 — moving revenue·storage sqft·special distributions 증가 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Moving rev | 성장 | 2019 $2.653bn | 적중 |
| Storage | 확대 | 지속 확대 | 적중 |
| Competition | 약함 | network 유지 | 적중 |
| Capital allocation | owner focus | 장기 reinvestment | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2012-11-08 | VIC 게시 | hub-and-spoke moat + cheap FCF Long |
| 2015-03-31 | 최초 검증·반증 신호 | moving revenue·storage sqft·special distributions 증가 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: network density와 owner-operated capital allocation을 잘 봄
- 최초 signal: 2015-03-31 — moving revenue·storage sqft·special distributions 증가
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2012-11-08 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:7e1b9b94-8944-4cac-8238-02b9c5f3b8ee -->
## 4. 2016-09-26 — 9.5% steady-state FCF + 25m sqft storage Long

### 결론부터

**강한 성공.** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**증권 결과:** 장기 강한 성공

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

### 5. 밸류에이션과 기대수익의 연결

steady-state FCF + hidden NAV growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

**정량 괴리:** Storage sqft: 25m → 56.4m 2023

**오류/핵심:** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

**정량 괴리:** FCF yield: 9.5%+ → 사업확대

**오류/핵심:** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

**정량 괴리:** Moving: stable moat → revenue 성장

**오류/핵심:** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

**정량 괴리:** Hidden assets: 부동산 → 규모 확대

**오류/핵심:** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

**정량 괴리:** Storage sqft: 25m → 56.4m 2023

**오류/핵심:** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** moving+25m sqft storage를 가진 property-backed business가 expansion capex를 제외하면 9.5%+ steady-state equity FCF yield이고 hidden assets도 존재

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

**정량 괴리:** FCF yield: 9.5%+ → 사업확대

**오류/핵심:** maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2019 moving/storage revenue 성장, 2023 owned storage rentable sqft 약 56.4m으로 두 배 이상 확대

### 7. 사업 결과와 가격 결과 분리

장기 강한 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음

### 9. 최초 검증·반증 신호와 회피 가능성

2019-03-31 — self-storage sqft와 moving cash engine 동시 확대 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Storage sqft | 25m | 56.4m 2023 | 적중 |
| FCF yield | 9.5%+ | 사업확대 | 적중 |
| Moving | stable moat | revenue 성장 | 적중 |
| Hidden assets | 부동산 | 규모 확대 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2016-09-26 | VIC 게시 | 9.5% steady-state FCF + 25m sqft storage Long |
| 2019-03-31 | 최초 검증·반증 신호 | self-storage sqft와 moving cash engine 동시 확대 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: maintenance와 growth capex를 분리하고 storage real estate를 별도 가치원천으로 본 점이 좋음
- 최초 signal: 2019-03-31 — self-storage sqft와 moving cash engine 동시 확대
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2016-09-26 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:39e93681-f4f4-478e-901c-91d56ef534a4 -->
## 5. 2017-07-21 — misunderstood moving economics Long

### 결론부터

**강한 성공.** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**증권 결과:** 장기 성공

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

### 5. 밸류에이션과 기대수익의 연결

normalized FCF/SOTP growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** 약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

**정량 괴리:** Trucks: 150k → 대규모 network 유지

**오류/핵심:** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** 약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

**정량 괴리:** Locations: 20k → network 확대

**오류/핵심:** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** 약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

**정량 괴리:** Storage sqft: 27m+ → 56.4m

**오류/핵심:** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** 약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

**정량 괴리:** Occupancy: 성숙화 → 83.4% 2023

**오류/핵심:** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** 약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

**정량 괴리:** Trucks: 150k → 대규모 network 유지

**오류/핵심:** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** 약 150k trucks/20k locations와 27m+ owned storage sqft를 가진 사업인데 회계 감가·fleet capex 때문에 core economics가 과소평가됨

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

**정량 괴리:** Locations: 20k → network 확대

**오류/핵심:** 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

U-Haul network와 self-storage는 계속 확장됐고 2023 owned storage 56.4m sqft, occupancy 83.4%

### 7. 사업 결과와 가격 결과 분리

장기 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심

### 9. 최초 검증·반증 신호와 회피 가능성

2019-03-31 — moving revenue와 storage economics 개선 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Trucks | 150k | 대규모 network 유지 | 적중 |
| Locations | 20k | network 확대 | 적중 |
| Storage sqft | 27m+ | 56.4m | 적중 |
| Occupancy | 성숙화 | 83.4% 2023 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2017-07-21 | VIC 게시 | misunderstood moving economics Long |
| 2019-03-31 | 최초 검증·반증 신호 | moving revenue와 storage economics 개선 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 회계 depreciation과 경제적 maintenance capex를 구분한 것이 핵심
- 최초 signal: 2019-03-31 — moving revenue와 storage economics 개선
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2017-07-21 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:22996430-fd82-4b11-b94a-00d4365a75f6 -->
## 6. 2019-09-07 — storage alone near market cap Long

### 결론부터

**강한 성공.** SOTP downside floor와 margin mean reversion을 잘 봄

**증권 결과:** 강한 성공

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

### 5. 밸류에이션과 기대수익의 연결

storage NAV + moving option growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

**정량 괴리:** Storage: near mcap value → 규모/수익 증가

**오류/핵심:** SOTP downside floor와 margin mean reversion을 잘 봄

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

**정량 괴리:** Moving margin: 압박 → 회복

**오류/핵심:** SOTP downside floor와 margin mean reversion을 잘 봄

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

**정량 괴리:** Revenue: stable → 성장

**오류/핵심:** SOTP downside floor와 margin mean reversion을 잘 봄

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

**정량 괴리:** Downside: 강함 → 실제 상방

**오류/핵심:** SOTP downside floor와 margin mean reversion을 잘 봄

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 강한 성공 · 16%

**원 주장:** self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

**정량 괴리:** Storage: near mcap value → 규모/수익 증가

**오류/핵심:** SOTP downside floor와 margin mean reversion을 잘 봄

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 강한 성공 · 16%

**원 주장:** self-storage 가치만으로 현 주가 대부분을 설명하고 moving rental margin pressure가 안정화되면 massive upside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

**정량 괴리:** Moving margin: 압박 → 회복

**오류/핵심:** SOTP downside floor와 margin mean reversion을 잘 봄

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

FY2019 moving revenue $2.653bn/storage $367m 이후 FY2020 storage +14% 수준 성장, pandemic migration/storage 수요가 강한 tailwind

### 7. 사업 결과와 가격 결과 분리

강한 성공 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

SOTP downside floor와 margin mean reversion을 잘 봄

### 9. 최초 검증·반증 신호와 회피 가능성

2021-03-31 — pandemic 이후 moving/storage earnings 급증 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

강한 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Storage | near mcap value | 규모/수익 증가 | 적중 |
| Moving margin | 압박 | 회복 | 적중 |
| Revenue | stable | 성장 | 적중 |
| Downside | 강함 | 실제 상방 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2019-09-07 | VIC 게시 | storage alone near market cap Long |
| 2021-03-31 | 최초 검증·반증 신호 | pandemic 이후 moving/storage earnings 급증 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: SOTP downside floor와 margin mean reversion을 잘 봄
- 최초 signal: 2021-03-31 — pandemic 이후 moving/storage earnings 급증
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2019-09-07 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:f1c1855d-4f90-4f05-b439-02cf819e8ea5 -->
## 7. 2020-08-20 — old-world moving + storage oversupply Short

### 결론부터

**실패.** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**증권 결과:** Short 실패

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

### 5. 밸류에이션과 기대수익의 연결

40x earnings Short growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 실패 · 18%

**원 주장:** 약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

**정량 괴리:** Valuation: 40x → earnings 급증

**오류/핵심:** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 실패 · 18%

**원 주장:** 약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

**정량 괴리:** Moving: 경쟁압박 → 강한 수요

**오류/핵심:** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 실패 · 16%

**원 주장:** 약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

**정량 괴리:** Storage: oversupply → occupancy 개선

**오류/핵심:** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 실패 · 16%

**원 주장:** 약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

**정량 괴리:** Network: old world → 강점 유지

**오류/핵심:** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 실패 · 16%

**원 주장:** 약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

**정량 괴리:** Valuation: 40x → earnings 급증

**오류/핵심:** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 실패 · 16%

**원 주장:** 약 $350, 2022E 40x earnings에서 truck rental 경쟁심화와 self-storage oversupply가 valuation을 깨뜨릴 것

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

**정량 괴리:** Moving: 경쟁압박 → 강한 수요

**오류/핵심:** 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

pandemic 이후 DIY moving·migration·storage 수요가 오히려 강해지고 storage footprint·occupancy가 개선되며 earnings가 확대

### 7. 사업 결과와 가격 결과 분리

Short 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가

### 9. 최초 검증·반증 신호와 회피 가능성

2021-03-31 — moving/storage revenue와 occupancy가 예상보다 강하게 개선 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

실패 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Valuation | 40x | earnings 급증 | 실패 |
| Moving | 경쟁압박 | 강한 수요 | 실패 |
| Storage | oversupply | occupancy 개선 | 실패 |
| Network | old world | 강점 유지 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2020-08-20 | VIC 게시 | old-world moving + storage oversupply Short |
| 2021-03-31 | 최초 검증·반증 신호 | moving/storage revenue와 occupancy가 예상보다 강하게 개선 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 경쟁·공급 증가를 봤지만 network density와 migration shock, 신규 storage lease-up을 과소평가
- 최초 signal: 2021-03-31 — moving/storage revenue와 occupancy가 예상보다 강하게 개선
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2020-08-20 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror

---

<!-- idea:0c03fd4d-4275-4854-baee-a741519ee795 -->
## 8. 2022-08-28 — 50m+ sqft storage + dominant moving Long

### 결론부터

**성공.** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**증권 결과:** 장기 thesis 유지

### 1. 무슨 기업인가

U-Haul은 DIY moving truck/trailer rental, self-storage, moving supplies와 보험을 묶은 북미 네트워크다. 핵심 KPI는 truck/trailer fleet, locations, transaction volume, equipment utilization, rental revenue, fleet CapEx/used-equipment disposals, storage rentable sqft·occupancy·rent/sqft와 insurance results다.

### 2. 산업 가치사슬과 돈의 흐름

fleet을 대량구매해 반복 대여하고 one-way network로 inventory를 재배치한다. self-storage는 moving customer funnel과 real estate를 공유한다. 회계 감가와 경제적 maintenance capex를 분리하면 moving FCF를 더 정확히 볼 수 있고 storage는 NOI/cap-rate NAV로 별도 평가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

브랜드·location density·one-way inventory balancing·real estate footprint가 경쟁우위다. fleet 과잉, storage 공급과 owner-family governance가 주요 위험이다.

### 4. 당시 VIC 원문과 핵심 논지

dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

### 5. 밸류에이션과 기대수익의 연결

SOTP with storage NAV growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

**정량 괴리:** Storage sqft: 50m+ → 56.4m

**오류/핵심:** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 적중 · 18%

**원 주장:** dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

**정량 괴리:** Occupancy: 강함 → 83.4%

**오류/핵심:** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 적중 · 16%

**원 주장:** dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

**정량 괴리:** Moving moat: dominant → 유지

**오류/핵심:** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

**정량 괴리:** Downside: strong → franchise 유지

**오류/핵심:** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 성공 · 16%

**원 주장:** dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

**정량 괴리:** Storage sqft: 50m+ → 56.4m

**오류/핵심:** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 성공 · 16%

**원 주장:** dominant truck-rental brand와 50m+ sqft storage, strong downside protection와 large upside·near-term catalyst

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

**정량 괴리:** Occupancy: 강함 → 83.4%

**오류/핵심:** mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2023 owned storage sqft 약 56.4m, avg occupancy 83.4%; moving/storage franchise 유지

### 7. 사업 결과와 가격 결과 분리

장기 thesis 유지 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음

### 9. 최초 검증·반증 신호와 회피 가능성

2023-03-31 — storage square footage/occupancy가 높은 수준 유지 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| Storage sqft | 50m+ | 56.4m | 적중 |
| Occupancy | 강함 | 83.4% | 적중 |
| Moving moat | dominant | 유지 | 적중 |
| Downside | strong | franchise 유지 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2022-08-28 | VIC 게시 | 50m+ sqft storage + dominant moving Long |
| 2023-03-31 | 최초 검증·반증 신호 | storage square footage/occupancy가 높은 수준 유지 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: mature moving cash flow와 real-estate growth를 별도 가치원천으로 본 점이 좋음
- 최초 signal: 2023-03-31 — storage square footage/occupancy가 높은 수준 유지
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC UHAL 2022-08-28 — Value Investors Club / user SQL
- [2. AMERCO FY2012 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445712000023/amerco-20120331x10k.htm) — SEC
- [3. AMERCO FY2019 10-K](https://www.sec.gov/Archives/edgar/data/4457/000000445719000024/march201910k.htm) — SEC
- [4. U-Haul SEC filings](https://www.sec.gov/edgar/browse/?CIK=4457) — SEC
- [5. U-Haul Investor Relations](https://www.uhaul.com/Investors/) — U-Haul
- [6. U-Haul FY2024 storage data](https://cdn.yahoofinance.com/prod/sec-filings/0000004457/000095017024066077/uhal-ex99_1.htm) — SEC/Yahoo mirror
---

# UNITED RENTALS INC (URI)

## 기업과 비즈니스

United Rentals는 건설·산업 고객에게 장비를 임대하는 북미 최대급 rental 업체다. 핵심 KPI는 fleet OEC, time utilization, rental rate, fleet productivity, used-equipment proceeds, maintenance/growth CapEx, leverage와 FCF다.

## 가치사슬과 돈의 흐름

장비를 구매해 반복 대여하므로 utilization×rental rate가 fleet yield를 결정한다. scale은 장비 구매조건·branch density·national accounts·specialty cross-sell에 유리하지만 산업 전체 fleet supply가 demand보다 빠르면 rates와 utilization이 함께 압박받는다.

## 경쟁우위·핵심 KPI

scale·national accounts·specialty mix가 강점이다. 가장 큰 위험은 cyclical demand보다 공급 discipline 붕괴이며, cycle Short는 기간을 명확히 해야 한다.

| 게시일 | 실제방향 | 논지 | 결과 |
|---|---|---|---|
| 2014-07-16 | Long | 8.5x maintenance FCF cyclical Long | 부분 적중 |
| 2014-12-10 | Short | fleet supply > demand Short | 부분 성공 |

---

<!-- idea:85f84ae9-a52b-4bfb-8a69-96eb23e732b9 -->
## 1. 2014-07-16 — 8.5x maintenance FCF cyclical Long

### 결론부터

**부분 적중.** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**증권 결과:** 장기 부분 성공·초기 실패

### 1. 무슨 기업인가

United Rentals는 건설·산업 고객에게 장비를 임대하는 북미 최대급 rental 업체다. 핵심 KPI는 fleet OEC, time utilization, rental rate, fleet productivity, used-equipment proceeds, maintenance/growth CapEx, leverage와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

장비를 구매해 반복 대여하므로 utilization×rental rate가 fleet yield를 결정한다. scale은 장비 구매조건·branch density·national accounts·specialty cross-sell에 유리하지만 산업 전체 fleet supply가 demand보다 빠르면 rates와 utilization이 함께 압박받는다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

scale·national accounts·specialty mix가 강점이다. 가장 큰 위험은 cyclical demand보다 공급 discipline 붕괴이며, cycle Short는 기간을 명확히 해야 한다.

### 4. 당시 VIC 원문과 핵심 논지

GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

### 5. 밸류에이션과 기대수익의 연결

8.5x maintenance FCF growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 실패 · 18%

**원 주장:** GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** 2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

**정량 괴리:** 1y return: upside → -25.7%

**오류/핵심:** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 실패 · 18%

**원 주장:** GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** 2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

**정량 괴리:** 2y return: upside → -36.3%

**오류/핵심:** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 부분 · 16%

**원 주장:** GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** 2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

**정량 괴리:** 5y return: compound → +22.4%

**오류/핵심:** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 적중 · 16%

**원 주장:** GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** 2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

**정량 괴리:** 2023 rev: 장기 scale → $14.332bn

**오류/핵심:** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 부분 적중 · 16%

**원 주장:** GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** 2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

**정량 괴리:** 1y return: upside → -25.7%

**오류/핵심:** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 부분 적중 · 16%

**원 주장:** GAAP보다 경제성이 좋고 8.5x maintenance FCF, commercial construction 정상화 +20%와 rent-over-own secular tailwind

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** 2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

**정량 괴리:** 2y return: upside → -36.3%

**오류/핵심:** 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

2014 revenue $5.7bn/fleet OEC $8.4bn. SQL 1년 -25.7%, 2년 -36.3%, 3년 +7.0%, 5년 +22.4%; 장기 2023 revenue $14.332bn

### 7. 사업 결과와 가격 결과 분리

장기 부분 성공·초기 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음

### 9. 최초 검증·반증 신호와 회피 가능성

2015-12-31 — rental rate/fleet cycle 약화로 1~2년 drawdown 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

부분 적중 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| 1y return | upside | -25.7% | 실패 |
| 2y return | upside | -36.3% | 실패 |
| 5y return | compound | +22.4% | 부분 |
| 2023 rev | 장기 scale | $14.332bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2014-07-16 | VIC 게시 | 8.5x maintenance FCF cyclical Long |
| 2015-12-31 | 최초 검증·반증 신호 | rental rate/fleet cycle 약화로 1~2년 drawdown |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: 장기 secular/scale thesis는 맞았지만 fleet cycle과 entry timing이 나빴음
- 최초 signal: 2015-12-31 — rental rate/fleet cycle 약화로 1~2년 drawdown
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC URI 2014-07-16 — Value Investors Club / user SQL
- [2. United Rentals 2014 10-K](https://www.sec.gov/Archives/edgar/data/1067701/000106770115000006/uri-2014123110k.htm) — SEC
- [3. United Rentals SEC filings](https://www.sec.gov/edgar/browse/?CIK=1067701) — SEC
- [4. United Rentals 2023 results](https://investors.unitedrentals.com/files/doc_financials/2023/q4/United-Rentals-Announces-Record-Fourth-Quarter-and-Full-Year-2023-Results-Introduces-2024-Outlook.pdf) — United Rentals
- [5. United Rentals IR](https://investor-relations.unitedrentals.com/) — United Rentals
- [6. United Rentals business](https://www.unitedrentals.com/) — United Rentals

---

<!-- idea:45d636cf-bfda-42b8-9804-9e2de0ac1152 -->
## 2. 2014-12-10 — fleet supply > demand Short

### 결론부터

**부분 성공.** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**증권 결과:** 전술적 성공·구조적 실패

### 1. 무슨 기업인가

United Rentals는 건설·산업 고객에게 장비를 임대하는 북미 최대급 rental 업체다. 핵심 KPI는 fleet OEC, time utilization, rental rate, fleet productivity, used-equipment proceeds, maintenance/growth CapEx, leverage와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

장비를 구매해 반복 대여하므로 utilization×rental rate가 fleet yield를 결정한다. scale은 장비 구매조건·branch density·national accounts·specialty cross-sell에 유리하지만 산업 전체 fleet supply가 demand보다 빠르면 rates와 utilization이 함께 압박받는다.

### 3. 경쟁우위·경쟁구도·핵심 KPI

scale·national accounts·specialty mix가 강점이다. 가장 큰 위험은 cyclical demand보다 공급 discipline 붕괴이며, cycle Short는 기간을 명확히 해야 한다.

### 4. 당시 VIC 원문과 핵심 논지

EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

### 5. 밸류에이션과 기대수익의 연결

30-50% cyclical downside growth/traffic 또는 NAV를 바로 주가로 연결하지 않고 unit economics·capital needs·multiple을 거친다.

### 투자논지를 구성한 6개 핵심 주장

#### 1. 수요·traffic/volume — 적중 · 18%

**원 주장:** EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 2~3개 분기 핵심 traffic/volume가 기대와 반대로 움직인다.

**실제:** SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

**정량 괴리:** 1y return: down 30-50% → -33.3%

**오류/핵심:** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**재사용 교훈:** 수요·traffic/volume는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 2. monetization·unit economics — 소진 · 18%

**원 주장:** EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** volume이 늘어도 revenue/unit 또는 contribution margin이 악화된다.

**실제:** SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

**정량 괴리:** 2y return: down → +1.4%

**오류/핵심:** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**재사용 교훈:** monetization·unit economics는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 3. network·경쟁구도 — 실패 · 16%

**원 주장:** EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 경쟁사 multi-homing·subsidy로 share/retention이 구조적으로 약화된다.

**실제:** SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

**정량 괴리:** 3y return: down → +53.8%

**오류/핵심:** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**재사용 교훈:** network·경쟁구도는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 4. capital intensity·balance sheet — 실패 · 16%

**원 주장:** EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 성장을 유지하는 데 필요한 CapEx·working capital·debt가 예상보다 커진다.

**실제:** SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

**정량 괴리:** 5y return: down → +46.3%

**오류/핵심:** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**재사용 교훈:** capital intensity·balance sheet는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 5. management·capital allocation — 부분 성공 · 16%

**원 주장:** EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 자본배분이 낮은 ROI expansion 또는 과도한 acquisition으로 이동한다.

**실제:** SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

**정량 괴리:** 1y return: down 30-50% → -33.3%

**오류/핵심:** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**재사용 교훈:** management·capital allocation는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

#### 6. valuation·catalyst — 부분 성공 · 16%

**원 주장:** EV/EBITDA가 flawed high이고 rental equipment supply growth가 demand보다 빨라 rates가 둔화하므로 30-50% downside

**성립 가정:** 핵심 KPI가 원 논지의 causal chain을 지지한다.

**사전 반증조건:** 사업이 맞아도 multiple compression 후 목표 IRR이 사라진다.

**실제:** SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

**정량 괴리:** 2y return: down → +1.4%

**오류/핵심:** cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

**재사용 교훈:** valuation·catalyst는 사전 반증조건을 수치로 저장하고 signal 발생 시 즉시 재평가한다.

### 6. 실제 사업의 시간순 전개

SQL 1년 -33.3%로 정확했으나 2년 +1.4%, 3년 +53.8%, 5년 +46.3%; 2023 revenue $14.332bn과 FCF $2.314bn

### 7. 사업 결과와 가격 결과 분리

전술적 성공·구조적 실패 가격방향이 맞아도 핵심 causal forecast가 틀릴 수 있다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패

### 9. 최초 검증·반증 신호와 회피 가능성

2015-12-31 — rate/fleet productivity 약화와 주가 하락 이 시점부터 thesis 확률과 holding period를 재설정한다.

### 10. 최종 판정·재사용 교훈

부분 성공 operating KPI와 security-return KPI를 분리 저장한다.

### 핵심 수치

| 지표 | 당시 | 실제 | 판정 |
|---|---|---|---|
| 1y return | down 30-50% | -33.3% | 적중 |
| 2y return | down | +1.4% | 소진 |
| 3y return | down | +53.8% | 실패 |
| 5y return | down | +46.3% | 실패 |

### 사건 타임라인

| 시점 | 사건 | 의미 |
|---|---|---|
| 2014-12-10 | VIC 게시 | fleet supply > demand Short |
| 2015-12-31 | 최초 검증·반증 신호 | rate/fleet productivity 약화와 주가 하락 |
| 2016-12-31 | 산업/KPI 구조 점검 | traffic·volume과 monetization/cycle을 분리 |
| 2019-12-31 | 경쟁·자본배분 변화 | business model의 실제 진화를 원문과 비교 |
| 2021-12-31 | 후속 결과 | 사업 성공과 증권 결과를 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- 근본 오류/핵심: cycle inflection은 정확했지만 이를 permanent economics deterioration으로 연장하면 실패
- 최초 signal: 2015-12-31 — rate/fleet productivity 약화와 주가 하락
- 당시 알 수 있었나: traffic/orders/volume, unit economics, segment revenue, fleet/store/storage data와 capital structure를 공개자료로 추적 가능했다.
- 반사실: 핵심 operating KPI가 맞더라도 경쟁비용·CapEx·multiple을 반영한 per-share 기대수익이 남는가?

### 주요 근거자료

- 1. VIC URI 2014-12-10 — Value Investors Club / user SQL
- [2. United Rentals 2014 10-K](https://www.sec.gov/Archives/edgar/data/1067701/000106770115000006/uri-2014123110k.htm) — SEC
- [3. United Rentals SEC filings](https://www.sec.gov/edgar/browse/?CIK=1067701) — SEC
- [4. United Rentals 2023 results](https://investors.unitedrentals.com/files/doc_financials/2023/q4/United-Rentals-Announces-Record-Fourth-Quarter-and-Full-Year-2023-Results-Introduces-2024-Outlook.pdf) — United Rentals
- [5. United Rentals IR](https://investor-relations.unitedrentals.com/) — United Rentals
- [6. United Rentals business](https://www.unitedrentals.com/) — United Rentals

---
# 배치 공통 학습

1. traffic·volume 성장과 monetization 개선을 동일시하지 않는다.
2. network effect는 multi-homing과 subsidy 이후에도 유지되는지 본다.
3. 자산집약 사업은 maintenance와 growth capex를 분리한다.
4. cycle thesis에는 만료조건을 붙인다.
5. 가격이 맞고 causal forecast가 틀릴 수 있으므로 둘을 분리 판정한다.
