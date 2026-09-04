# Batch 027 — Tesla · CarMax 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Tesla 7건 · CarMax 3건

## 결론부터

이번 배치는 자본집약적 성장기업에서 **생존성 → scale → unit economics → valuation**을 분리해 분석한다. Tesla 2012·2016 Short는 진짜 제조·유동성 위험을 봤지만 이를 permanent failure로 과대해석했고, 2018·2019 Long은 Model 3 mass-production이라는 새 evidence를 반영해 prior를 업데이트했다. CarMax 2010 Short는 retail spread와 finance spread를 각각 낮은 질로 봤지만 appraisal·inventory turn·wholesale·CAF·store network가 결합된 시스템 경제성을 놓쳤다.

> 방향 교정: 원 SQL에서 10건 모두 `is_short=true`다. 실제 방향은 본문 기준으로 교정했고 raw flag는 보존했다.

---

# TESLA INC (TSLA)

## 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

## 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

## 3. 경쟁우위·경쟁구도·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2012-11-30 | Short | Short | clean-tech bankruptcy analogue | 장기 Short 치명적 실패 | 치명적 실패 |
| 2016-06-23 | Short | Short | Model 3/SolarCity execution overload | 장기 Short 실패 | 실패 |
| 2018-01-23 | Short | Long | long-duration optionality | 장기 매우 성공 | 매우 성공 |
| 2019-03-17 | Short | Short | demand cliff/cash raise | Short 실패 | 실패 |
| 2019-08-03 | Short | Long | mass-production proof/EV transition | 장기 강한 성공 | 강한 성공 |
| 2019-11-17 | Short | Market-neutral short volatility | expensive-volatility selling | naked short-vol 큰 손실 가능 | 실패 |
| 2021-01-11 | Short | Short | valuation bubble | holding period 혼합 | 부분 적중 |

---

<!-- idea:92e4e60c-04f0-48e4-ab54-fcc476808b4d -->
## 1. 2012-11-30 — clean-tech bankruptcy analogue

### 결론부터

**종합판정: 치명적 실패.** ramp risk를 permanent failure로 과대해석

**증권 결과:** 장기 Short 치명적 실패

**Thesis / Process 점수:** 4.0 / 6.5

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

### 5. 밸류에이션

파산확률을 크게 둔 distressed valuation 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 실패 · 논지 비중 18%

**당시 주장**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**당시 근거**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

**정량적 괴리**

Model S: 132대(9/23) → 2,650대

**분석 오류·핵심**

ramp risk를 permanent failure로 과대해석

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 실패 · 논지 비중 18%

**당시 주장**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**당시 근거**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

**정량적 괴리**

run-rate: 낮음 → 20,000/yr

**분석 오류·핵심**

ramp risk를 permanent failure로 과대해석

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 실패 · 논지 비중 16%

**당시 주장**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**당시 근거**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

**정량적 괴리**

2013 deliveries: 부진 예상 → 22,477

**분석 오류·핵심**

ramp risk를 permanent failure로 과대해석

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 실패 · 논지 비중 16%

**당시 주장**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**당시 근거**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

**정량적 괴리**

liquidity: 파산 → 조달 지속

**분석 오류·핵심**

ramp risk를 permanent failure로 과대해석

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 치명적 실패 · 논지 비중 16%

**당시 주장**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**당시 근거**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

**정량적 괴리**

Model S: 132대(9/23) → 2,650대

**분석 오류·핵심**

ramp risk를 permanent failure로 과대해석

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 치명적 실패 · 논지 비중 16%

**당시 주장**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**당시 근거**

Model S ramp 지연·현금부족이 파산/희석으로 이어질 것

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

**정량적 괴리**

run-rate: 낮음 → 20,000/yr

**분석 오류·핵심**

ramp risk를 permanent failure로 과대해석

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

2012말 2,650대 인도·2만대 run-rate, 2013 22,477대

### 7. 사업과 증권 결과 분리

장기 Short 치명적 실패

### 8. 무엇을 맞고 틀렸나

ramp risk를 permanent failure로 과대해석

### 9. 최초 검증·반증 신호

2012-12-31 — 주당 생산속도 개선

### 10. 최종 교훈

치명적 실패 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Model S | 132대(9/23) | 원 VIC 논지 방향 | 2,650대 | 실패 |
| run-rate | 낮음 | 원 VIC 논지 방향 | 20,000/yr | 실패 |
| 2013 deliveries | 부진 예상 | 원 VIC 논지 방향 | 22,477 | 실패 |
| liquidity | 파산 | 원 VIC 논지 방향 | 조달 지속 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2012-11-30 | VIC 게시 | clean-tech bankruptcy analogue |
| 2012-12-31 | 최초 신호 | 주당 생산속도 개선 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** ramp risk를 permanent failure로 과대해석
- **최초 검증·반증 신호:** 2012-12-31 — 주당 생산속도 개선
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 높음
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2012-11-30 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증

---

<!-- idea:41e61934-04e3-47ad-ab90-86d3e073e184 -->
## 2. 2016-06-23 — Model 3/SolarCity execution overload

### 결론부터

**종합판정: 실패.** execution risk 적중, permanent impairment 실패

**증권 결과:** 장기 Short 실패

**Thesis / Process 점수:** 4.0 / 6.5

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

50만대 계획과 SolarCity가 제조·자본부담 과도

### 5. 밸류에이션

tail-risk valuation 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 실패 · 논지 비중 18%

**당시 주장**

50만대 계획과 SolarCity가 제조·자본부담 과도

**당시 근거**

50만대 계획과 SolarCity가 제조·자본부담 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

production hell은 실제였으나 2018~19 scale 성공

**정량적 괴리**

reservations: 373k → 대규모 유지

**분석 오류·핵심**

execution risk 적중, permanent impairment 실패

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 부분 · 논지 비중 18%

**당시 주장**

50만대 계획과 SolarCity가 제조·자본부담 과도

**당시 근거**

50만대 계획과 SolarCity가 제조·자본부담 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

production hell은 실제였으나 2018~19 scale 성공

**정량적 괴리**

2018 plan: 500k → ramp 통과

**분석 오류·핵심**

execution risk 적중, permanent impairment 실패

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 부분 · 논지 비중 16%

**당시 주장**

50만대 계획과 SolarCity가 제조·자본부담 과도

**당시 근거**

50만대 계획과 SolarCity가 제조·자본부담 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

production hell은 실제였으나 2018~19 scale 성공

**정량적 괴리**

SolarCity: 부담 → auto 생존 막지 못함

**분석 오류·핵심**

execution risk 적중, permanent impairment 실패

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 실패 · 논지 비중 16%

**당시 주장**

50만대 계획과 SolarCity가 제조·자본부담 과도

**당시 근거**

50만대 계획과 SolarCity가 제조·자본부담 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

production hell은 실제였으나 2018~19 scale 성공

**정량적 괴리**

2019 deliveries: - → 367,656

**분석 오류·핵심**

execution risk 적중, permanent impairment 실패

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 실패 · 논지 비중 16%

**당시 주장**

50만대 계획과 SolarCity가 제조·자본부담 과도

**당시 근거**

50만대 계획과 SolarCity가 제조·자본부담 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

production hell은 실제였으나 2018~19 scale 성공

**정량적 괴리**

reservations: 373k → 대규모 유지

**분석 오류·핵심**

execution risk 적중, permanent impairment 실패

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 실패 · 논지 비중 16%

**당시 주장**

50만대 계획과 SolarCity가 제조·자본부담 과도

**당시 근거**

50만대 계획과 SolarCity가 제조·자본부담 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

production hell은 실제였으나 2018~19 scale 성공

**정량적 괴리**

2018 plan: 500k → ramp 통과

**분석 오류·핵심**

execution risk 적중, permanent impairment 실패

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

production hell은 실제였으나 2018~19 scale 성공

### 7. 사업과 증권 결과 분리

장기 Short 실패

### 8. 무엇을 맞고 틀렸나

execution risk 적중, permanent impairment 실패

### 9. 최초 검증·반증 신호

2018-06-30 — Model 3 weekly output 급상승

### 10. 최종 교훈

실패 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| reservations | 373k | 원 VIC 논지 방향 | 대규모 유지 | 실패 |
| 2018 plan | 500k | 원 VIC 논지 방향 | ramp 통과 | 부분 |
| SolarCity | 부담 | 원 VIC 논지 방향 | auto 생존 막지 못함 | 부분 |
| 2019 deliveries | - | 원 VIC 논지 방향 | 367,656 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-06-23 | VIC 게시 | Model 3/SolarCity execution overload |
| 2018-06-30 | 최초 신호 | Model 3 weekly output 급상승 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** execution risk 적중, permanent impairment 실패
- **최초 검증·반증 신호:** 2018-06-30 — Model 3 weekly output 급상승
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 높음
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2016-06-23 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증

---

<!-- idea:4ebc7587-ed23-43f2-bb93-282befc92ac5 -->
## 3. 2018-01-23 — long-duration optionality

### 결론부터

**종합판정: 매우 성공.** 현재 P&L보다 scalable capability를 봄

**증권 결과:** 장기 매우 성공

**Thesis / Process 점수:** 9.2 / 8.8

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

현재 손실보다 Model3·brand·battery·software optionality가 큼

### 5. 밸류에이션

장기 optionality valuation 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 적중 · 논지 비중 18%

**당시 주장**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**당시 근거**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

**정량적 괴리**

Model3: production hell → mass production

**분석 오류·핵심**

현재 P&L보다 scalable capability를 봄

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 적중 · 논지 비중 18%

**당시 주장**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**당시 근거**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

**정량적 괴리**

brand: 강함 → EV leader

**분석 오류·핵심**

현재 P&L보다 scalable capability를 봄

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 적중 · 논지 비중 16%

**당시 주장**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**당시 근거**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

**정량적 괴리**

revenue: 초기 → $53.8bn 2021

**분석 오류·핵심**

현재 P&L보다 scalable capability를 봄

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 적중 · 논지 비중 16%

**당시 주장**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**당시 근거**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

**정량적 괴리**

funding: 의존 → 접근 지속

**분석 오류·핵심**

현재 P&L보다 scalable capability를 봄

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 매우 성공 · 논지 비중 16%

**당시 주장**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**당시 근거**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

**정량적 괴리**

Model3: production hell → mass production

**분석 오류·핵심**

현재 P&L보다 scalable capability를 봄

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 매우 성공 · 논지 비중 16%

**당시 주장**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**당시 근거**

현재 손실보다 Model3·brand·battery·software optionality가 큼

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

**정량적 괴리**

brand: 강함 → EV leader

**분석 오류·핵심**

현재 P&L보다 scalable capability를 봄

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

2018 mass-production, 2019 36.8만대, 2021 revenue $53.8bn

### 7. 사업과 증권 결과 분리

장기 매우 성공

### 8. 무엇을 맞고 틀렸나

현재 P&L보다 scalable capability를 봄

### 9. 최초 검증·반증 신호

2018-06-30 — Model 3 ramp 성공

### 10. 최종 교훈

매우 성공 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Model3 | production hell | 원 VIC 논지 방향 | mass production | 적중 |
| brand | 강함 | 원 VIC 논지 방향 | EV leader | 적중 |
| revenue | 초기 | 원 VIC 논지 방향 | $53.8bn 2021 | 적중 |
| funding | 의존 | 원 VIC 논지 방향 | 접근 지속 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-01-23 | VIC 게시 | long-duration optionality |
| 2018-06-30 | 최초 신호 | Model 3 ramp 성공 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** 현재 P&L보다 scalable capability를 봄
- **최초 검증·반증 신호:** 2018-06-30 — Model 3 ramp 성공
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 중간
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2018-01-23 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증

---

<!-- idea:12820812-3234-4172-b020-6f2df296925a -->
## 4. 2019-03-17 — demand cliff/cash raise

### 결론부터

**종합판정: 실패.** 가격인하를 demand failure로 단선 해석

**증권 결과:** Short 실패

**Thesis / Process 점수:** 4.0 / 6.5

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

가격인하·service 문제·CapEx가 demand/cash 훼손

### 5. 밸류에이션

multiple compression 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 실패 · 논지 비중 18%

**당시 주장**

가격인하·service 문제·CapEx가 demand/cash 훼손

**당시 근거**

가격인하·service 문제·CapEx가 demand/cash 훼손

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

**정량적 괴리**

price cuts: 약세신호 → volume 증가

**분석 오류·핵심**

가격인하를 demand failure로 단선 해석

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 부분 · 논지 비중 18%

**당시 주장**

가격인하·service 문제·CapEx가 demand/cash 훼손

**당시 근거**

가격인하·service 문제·CapEx가 demand/cash 훼손

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

**정량적 괴리**

cash: 압박 → 조달 성공

**분석 오류·핵심**

가격인하를 demand failure로 단선 해석

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 실패 · 논지 비중 16%

**당시 주장**

가격인하·service 문제·CapEx가 demand/cash 훼손

**당시 근거**

가격인하·service 문제·CapEx가 demand/cash 훼손

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

**정량적 괴리**

Shanghai: 부담 → 빠른 가동

**분석 오류·핵심**

가격인하를 demand failure로 단선 해석

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 실패 · 논지 비중 16%

**당시 주장**

가격인하·service 문제·CapEx가 demand/cash 훼손

**당시 근거**

가격인하·service 문제·CapEx가 demand/cash 훼손

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

**정량적 괴리**

deliveries: - → 367,656

**분석 오류·핵심**

가격인하를 demand failure로 단선 해석

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 실패 · 논지 비중 16%

**당시 주장**

가격인하·service 문제·CapEx가 demand/cash 훼손

**당시 근거**

가격인하·service 문제·CapEx가 demand/cash 훼손

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

**정량적 괴리**

price cuts: 약세신호 → volume 증가

**분석 오류·핵심**

가격인하를 demand failure로 단선 해석

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 실패 · 논지 비중 16%

**당시 주장**

가격인하·service 문제·CapEx가 demand/cash 훼손

**당시 근거**

가격인하·service 문제·CapEx가 demand/cash 훼손

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

**정량적 괴리**

cash: 압박 → 조달 성공

**분석 오류·핵심**

가격인하를 demand failure로 단선 해석

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

단기압박·증자는 있었으나 2019 인도 record와 Shanghai 가동

### 7. 사업과 증권 결과 분리

Short 실패

### 8. 무엇을 맞고 틀렸나

가격인하를 demand failure로 단선 해석

### 9. 최초 검증·반증 신호

2019-12-31 — 2019 deliveries 367,656

### 10. 최종 교훈

실패 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| price cuts | 약세신호 | 원 VIC 논지 방향 | volume 증가 | 실패 |
| cash | 압박 | 원 VIC 논지 방향 | 조달 성공 | 부분 |
| Shanghai | 부담 | 원 VIC 논지 방향 | 빠른 가동 | 실패 |
| deliveries | - | 원 VIC 논지 방향 | 367,656 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-03-17 | VIC 게시 | demand cliff/cash raise |
| 2019-12-31 | 최초 신호 | 2019 deliveries 367,656 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** 가격인하를 demand failure로 단선 해석
- **최초 검증·반증 신호:** 2019-12-31 — 2019 deliveries 367,656
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 높음
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2019-03-17 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증

---

<!-- idea:7265c2cd-17d0-466c-b027-4cb4827d6ed9 -->
## 5. 2019-08-03 — mass-production proof/EV transition

### 결론부터

**종합판정: 강한 성공.** core auto 적중, robotaxi timing 과대

**증권 결과:** 장기 강한 성공

**Thesis / Process 점수:** 9.2 / 8.8

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

2018 mass-production proof와 EV·brand·software moat

### 5. 밸류에이션

autonomy를 큰 본가치에 넣지 않은 valuation 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 적중 · 논지 비중 18%

**당시 주장**

2018 mass-production proof와 EV·brand·software moat

**당시 근거**

2018 mass-production proof와 EV·brand·software moat

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2019~21 판매·매출 급증, autonomy는 지연

**정량적 괴리**

EV scale: 검증 → 대량생산

**분석 오류·핵심**

core auto 적중, robotaxi timing 과대

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 적중 · 논지 비중 18%

**당시 주장**

2018 mass-production proof와 EV·brand·software moat

**당시 근거**

2018 mass-production proof와 EV·brand·software moat

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2019~21 판매·매출 급증, autonomy는 지연

**정량적 괴리**

brand: 강화 → 유지

**분석 오류·핵심**

core auto 적중, robotaxi timing 과대

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 과대 · 논지 비중 16%

**당시 주장**

2018 mass-production proof와 EV·brand·software moat

**당시 근거**

2018 mass-production proof와 EV·brand·software moat

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2019~21 판매·매출 급증, autonomy는 지연

**정량적 괴리**

autonomy: option → 지연

**분석 오류·핵심**

core auto 적중, robotaxi timing 과대

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 적중 · 논지 비중 16%

**당시 주장**

2018 mass-production proof와 EV·brand·software moat

**당시 근거**

2018 mass-production proof와 EV·brand·software moat

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2019~21 판매·매출 급증, autonomy는 지연

**정량적 괴리**

revenue: 성장 → $53.8bn

**분석 오류·핵심**

core auto 적중, robotaxi timing 과대

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 강한 성공 · 논지 비중 16%

**당시 주장**

2018 mass-production proof와 EV·brand·software moat

**당시 근거**

2018 mass-production proof와 EV·brand·software moat

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2019~21 판매·매출 급증, autonomy는 지연

**정량적 괴리**

EV scale: 검증 → 대량생산

**분석 오류·핵심**

core auto 적중, robotaxi timing 과대

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 강한 성공 · 논지 비중 16%

**당시 주장**

2018 mass-production proof와 EV·brand·software moat

**당시 근거**

2018 mass-production proof와 EV·brand·software moat

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2019~21 판매·매출 급증, autonomy는 지연

**정량적 괴리**

brand: 강화 → 유지

**분석 오류·핵심**

core auto 적중, robotaxi timing 과대

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

2019~21 판매·매출 급증, autonomy는 지연

### 7. 사업과 증권 결과 분리

장기 강한 성공

### 8. 무엇을 맞고 틀렸나

core auto 적중, robotaxi timing 과대

### 9. 최초 검증·반증 신호

2019-12-31 — deliveries record

### 10. 최종 교훈

강한 성공 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| EV scale | 검증 | 원 VIC 논지 방향 | 대량생산 | 적중 |
| brand | 강화 | 원 VIC 논지 방향 | 유지 | 적중 |
| autonomy | option | 원 VIC 논지 방향 | 지연 | 과대 |
| revenue | 성장 | 원 VIC 논지 방향 | $53.8bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-08-03 | VIC 게시 | mass-production proof/EV transition |
| 2019-12-31 | 최초 신호 | deliveries record |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** core auto 적중, robotaxi timing 과대
- **최초 검증·반증 신호:** 2019-12-31 — deliveries record
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 중간
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2019-08-03 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증

---

<!-- idea:b3d1bb1a-33d9-4d10-9e92-843ea240a2f0 -->
## 6. 2019-11-17 — expensive-volatility selling

### 결론부터

**종합판정: 실패.** convexity/tail risk 과소평가

**증권 결과:** naked short-vol 큰 손실 가능

**Thesis / Process 점수:** 4.0 / 6.5

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

bull/bear 확신 때문에 option IV 과도

### 5. 밸류에이션

IV-vs-RV trade 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 실패 · 논지 비중 18%

**당시 주장**

bull/bear 확신 때문에 option IV 과도

**당시 근거**

bull/bear 확신 때문에 option IV 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2020~21 realized vol·directional rally 극단적

**정량적 괴리**

IV: 높음 → RV 폭증

**분석 오류·핵심**

convexity/tail risk 과소평가

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 실패 · 논지 비중 18%

**당시 주장**

bull/bear 확신 때문에 option IV 과도

**당시 근거**

bull/bear 확신 때문에 option IV 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2020~21 realized vol·directional rally 극단적

**정량적 괴리**

range: 유지 예상 → 상방돌파

**분석 오류·핵심**

convexity/tail risk 과소평가

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 실패 · 논지 비중 16%

**당시 주장**

bull/bear 확신 때문에 option IV 과도

**당시 근거**

bull/bear 확신 때문에 option IV 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2020~21 realized vol·directional rally 극단적

**정량적 괴리**

tail: 낮음 → 극단적

**분석 오류·핵심**

convexity/tail risk 과소평가

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 실패 · 논지 비중 16%

**당시 주장**

bull/bear 확신 때문에 option IV 과도

**당시 근거**

bull/bear 확신 때문에 option IV 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2020~21 realized vol·directional rally 극단적

**정량적 괴리**

theta: 수취 → convexity 손실

**분석 오류·핵심**

convexity/tail risk 과소평가

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 실패 · 논지 비중 16%

**당시 주장**

bull/bear 확신 때문에 option IV 과도

**당시 근거**

bull/bear 확신 때문에 option IV 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2020~21 realized vol·directional rally 극단적

**정량적 괴리**

IV: 높음 → RV 폭증

**분석 오류·핵심**

convexity/tail risk 과소평가

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 실패 · 논지 비중 16%

**당시 주장**

bull/bear 확신 때문에 option IV 과도

**당시 근거**

bull/bear 확신 때문에 option IV 과도

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2020~21 realized vol·directional rally 극단적

**정량적 괴리**

range: 유지 예상 → 상방돌파

**분석 오류·핵심**

convexity/tail risk 과소평가

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

2020~21 realized vol·directional rally 극단적

### 7. 사업과 증권 결과 분리

naked short-vol 큰 손실 가능

### 8. 무엇을 맞고 틀렸나

convexity/tail risk 과소평가

### 9. 최초 검증·반증 신호

2020-03-31 — realized volatility 급등

### 10. 최종 교훈

실패 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| IV | 높음 | 원 VIC 논지 방향 | RV 폭증 | 실패 |
| range | 유지 예상 | 원 VIC 논지 방향 | 상방돌파 | 실패 |
| tail | 낮음 | 원 VIC 논지 방향 | 극단적 | 실패 |
| theta | 수취 | 원 VIC 논지 방향 | convexity 손실 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-11-17 | VIC 게시 | expensive-volatility selling |
| 2020-03-31 | 최초 신호 | realized volatility 급등 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** convexity/tail risk 과소평가
- **최초 검증·반증 신호:** 2020-03-31 — realized volatility 급등
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 높음
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2019-11-17 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증

---

<!-- idea:be717dc4-96df-42cb-b7c1-687c49db4033 -->
## 7. 2021-01-11 — valuation bubble

### 결론부터

**종합판정: 부분 적중.** business Short보다 duration warning 부분 적중

**증권 결과:** holding period 혼합

**Thesis / Process 점수:** 6.5 / 6.5

### 1. 무슨 기업인가

Tesla는 전기차를 설계·제조·직접판매하고 차량 소프트웨어·충전망·에너지저장을 수직통합한다. 핵심 KPI는 생산·인도량, automotive gross margin, unit cost, cash/FCF, 공장 utilization, ASP와 가격인하 후 volume elasticity다.

### 2. 산업 가치사슬과 돈의 흐름

차량 ASP×인도량에서 제조·보증·물류비를 빼고 software/service 이익을 더한다. ramp 초기에는 fixed-cost absorption이 낮아 cash burn이 커지지만 throughput과 yield가 개선되면 손익이 비선형적으로 좋아질 수 있다.

### 3. 경쟁우위·핵심 KPI

EV brand·전용 software architecture·OTA·충전망이 강점이다. 경쟁 OEM scale-up, 가격경쟁, CapEx와 autonomy monetization 지연이 위험이다.

### 4. 당시 VIC 원문

시총 비중 1.7% 수준이 성공 과도 선반영

### 5. 밸류에이션

valuation-duration Short 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 부분 · 논지 비중 18%

**당시 주장**

시총 비중 1.7% 수준이 성공 과도 선반영

**당시 근거**

시총 비중 1.7% 수준이 성공 과도 선반영

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2021 사업성장, 2022 drawdown, 2023 회복

**정량적 괴리**

market share: 1.7% → 2022 de-rate

**분석 오류·핵심**

business Short보다 duration warning 부분 적중

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 실패 · 논지 비중 18%

**당시 주장**

시총 비중 1.7% 수준이 성공 과도 선반영

**당시 근거**

시총 비중 1.7% 수준이 성공 과도 선반영

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2021 사업성장, 2022 drawdown, 2023 회복

**정량적 괴리**

revenue: 실망 예상 → 성장 지속

**분석 오류·핵심**

business Short보다 duration warning 부분 적중

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 적중 · 논지 비중 16%

**당시 주장**

시총 비중 1.7% 수준이 성공 과도 선반영

**당시 근거**

시총 비중 1.7% 수준이 성공 과도 선반영

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2021 사업성장, 2022 drawdown, 2023 회복

**정량적 괴리**

multiple: 극단 → 압축

**분석 오류·핵심**

business Short보다 duration warning 부분 적중

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 중립 · 논지 비중 16%

**당시 주장**

시총 비중 1.7% 수준이 성공 과도 선반영

**당시 근거**

시총 비중 1.7% 수준이 성공 과도 선반영

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2021 사업성장, 2022 drawdown, 2023 회복

**정량적 괴리**

business: 둔화 → 성장

**분석 오류·핵심**

business Short보다 duration warning 부분 적중

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 부분 적중 · 논지 비중 16%

**당시 주장**

시총 비중 1.7% 수준이 성공 과도 선반영

**당시 근거**

시총 비중 1.7% 수준이 성공 과도 선반영

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2021 사업성장, 2022 drawdown, 2023 회복

**정량적 괴리**

market share: 1.7% → 2022 de-rate

**분석 오류·핵심**

business Short보다 duration warning 부분 적중

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 부분 적중 · 논지 비중 16%

**당시 주장**

시총 비중 1.7% 수준이 성공 과도 선반영

**당시 근거**

시총 비중 1.7% 수준이 성공 과도 선반영

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

2021 사업성장, 2022 drawdown, 2023 회복

**정량적 괴리**

revenue: 실망 예상 → 성장 지속

**분석 오류·핵심**

business Short보다 duration warning 부분 적중

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

2021 사업성장, 2022 drawdown, 2023 회복

### 7. 사업과 증권 결과 분리

holding period 혼합

### 8. 무엇을 맞고 틀렸나

business Short보다 duration warning 부분 적중

### 9. 최초 검증·반증 신호

2022-06-30 — multiple compression

### 10. 최종 교훈

부분 적중 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| market share | 1.7% | 원 VIC 논지 방향 | 2022 de-rate | 부분 |
| revenue | 실망 예상 | 원 VIC 논지 방향 | 성장 지속 | 실패 |
| multiple | 극단 | 원 VIC 논지 방향 | 압축 | 적중 |
| business | 둔화 | 원 VIC 논지 방향 | 성장 | 중립 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-01-11 | VIC 게시 | valuation bubble |
| 2022-06-30 | 최초 신호 | multiple compression |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** business Short보다 duration warning 부분 적중
- **최초 검증·반증 신호:** 2022-06-30 — multiple compression
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 중간
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC TSLA 2021-01-11 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. Tesla 2012 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm) — SEC. 사업·KPI·event 사후검증
- [3. Tesla Model 3 disclosure](https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm) — SEC. 사업·KPI·event 사후검증
- [4. Tesla 2019 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm) — SEC. 사업·KPI·event 사후검증
- [5. Tesla 2021 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm) — SEC. 사업·KPI·event 사후검증
- [6. Tesla IR](https://ir.tesla.com/) — Tesla. 사업·KPI·event 사후검증
---

# CARMAX INC (KMX)

## 1. 무슨 기업인가

CarMax는 미국 최대급 used-car retailer로 no-haggle pricing, 대규모 재고, appraisal/trade-in sourcing, wholesale auctions와 CarMax Auto Finance(CAF)를 결합한다. 핵심 KPI는 retail/wholesale units, comparable-store units, gross profit/unit, inventory turn, store count, omnichannel conversion, CAF penetration·spread·credit losses다.

## 2. 산업 가치사슬과 돈의 흐름

고객에게 차량을 매입해 reconditioning 후 retail로 판매하고 retail 기준에 맞지 않는 차량은 wholesale auction으로 처분한다. retail spread가 크지 않아도 inventory turn과 scale이 수익을 만들고 CAF가 별도의 finance spread를 제공한다. store는 appraisal·reconditioning·test-drive·fulfillment node 역할을 한다.

## 3. 경쟁우위·경쟁구도·핵심 KPI

No-haggle brand, 전국 inventory pool, appraisal 데이터, wholesale auction, CAF와 store density가 결합된 경쟁우위다. Carvana 등 digital 경쟁, used-car 가격과 금리·신용손실이 주요 위험이다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2010-04-09 | Short | Short | two spread businesses disguised as retailer | SQL 1년 +30.8%, 3년 +74.2%, 5년 +204.4% | 치명적 실패 |
| 2015-12-22 | Short | Long | scale + store growth + operating leverage | SQL 1년 +23.1%, 5년 +87.4% | 성공 |
| 2019-08-07 | Short | Long | omnichannel margin-neutral transition | SQL 1년 +19.8%, 2년 +59.5%, 3년 +18.7% | 성공 |

---

<!-- idea:98927e4d-02c3-423d-aa8b-8e5eac4d96a4 -->
## 1. 2010-04-09 — two spread businesses disguised as retailer

### 결론부터

**종합판정: 치명적 실패.** scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**증권 결과:** SQL 1년 +30.8%, 3년 +74.2%, 5년 +204.4%

**Thesis / Process 점수:** 4.0 / 6.5

### 1. 무슨 기업인가

CarMax는 미국 최대급 used-car retailer로 no-haggle pricing, 대규모 재고, appraisal/trade-in sourcing, wholesale auctions와 CarMax Auto Finance(CAF)를 결합한다. 핵심 KPI는 retail/wholesale units, comparable-store units, gross profit/unit, inventory turn, store count, omnichannel conversion, CAF penetration·spread·credit losses다.

### 2. 산업 가치사슬과 돈의 흐름

고객에게 차량을 매입해 reconditioning 후 retail로 판매하고 retail 기준에 맞지 않는 차량은 wholesale auction으로 처분한다. retail spread가 크지 않아도 inventory turn과 scale이 수익을 만들고 CAF가 별도의 finance spread를 제공한다. store는 appraisal·reconditioning·test-drive·fulfillment node 역할을 한다.

### 3. 경쟁우위·핵심 KPI

No-haggle brand, 전국 inventory pool, appraisal 데이터, wholesale auction, CAF와 store density가 결합된 경쟁우위다. Carvana 등 digital 경쟁, used-car 가격과 금리·신용손실이 주요 위험이다.

### 4. 당시 VIC 원문

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

### 5. 밸류에이션

retail/CAF에 낮은 multiple 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 실패 · 논지 비중 18%

**당시 주장**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**당시 근거**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

**정량적 괴리**

Entry: $24.60 → 1y +30.8%

**분석 오류·핵심**

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 실패 · 논지 비중 18%

**당시 주장**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**당시 근거**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

**정량적 괴리**

Retail units: FY2010 357,129 → FY2015 582,282

**분석 오류·핵심**

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 실패 · 논지 비중 16%

**당시 주장**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**당시 근거**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

**정량적 괴리**

Stores: 약 100 → FY2015 144

**분석 오류·핵심**

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 치명적 실패 · 논지 비중 16%

**당시 주장**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**당시 근거**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

**정량적 괴리**

5y return: 하락 기대 → +204.4%

**분석 오류·핵심**

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 치명적 실패 · 논지 비중 16%

**당시 주장**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**당시 근거**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

**정량적 괴리**

Entry: $24.60 → 1y +30.8%

**분석 오류·핵심**

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 치명적 실패 · 논지 비중 16%

**당시 주장**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**당시 근거**

used-car merchandising spread와 auto-finance spread라는 두 mediocre businesses라 $24.60이 과대평가

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

**정량적 괴리**

Retail units: FY2010 357,129 → FY2015 582,282

**분석 오류·핵심**

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

FY2010 retail 357,129대에서 FY2015 582,282대, FY2019 748,961대로 성장; SQL 5년 +204.4%

### 7. 사업과 증권 결과 분리

SQL 1년 +30.8%, 3년 +74.2%, 5년 +204.4%

### 8. 무엇을 맞고 틀렸나

scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가

### 9. 최초 검증·반증 신호

2012-02-29 — store/units 성장과 CAF profit pool 확인

### 10. 최종 교훈

치명적 실패 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $24.60 | 원 VIC 논지 방향 | 1y +30.8% | 실패 |
| Retail units | FY2010 357,129 | 원 VIC 논지 방향 | FY2015 582,282 | 실패 |
| Stores | 약 100 | 원 VIC 논지 방향 | FY2015 144 | 실패 |
| 5y return | 하락 기대 | 원 VIC 논지 방향 | +204.4% | 치명적 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2010-04-09 | VIC 게시 | two spread businesses disguised as retailer |
| 2012-02-29 | 최초 신호 | store/units 성장과 CAF profit pool 확인 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** scale의 inventory turn·appraisal·wholesale·CAF flywheel을 과소평가
- **최초 검증·반증 신호:** 2012-02-29 — store/units 성장과 CAF profit pool 확인
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 높음
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC KMX 2010-04-09 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. CarMax FY2010 filing](https://www.sec.gov/Archives/edgar/data/1170010/000117001010000044/tenq.htm) — SEC. 사업·KPI·event 사후검증
- [3. CarMax FY2015 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001015000008/kmx-20150228x10k.htm) — SEC. 사업·KPI·event 사후검증
- [4. CarMax FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001019000040/kmx0228201910-k.htm) — SEC. 사업·KPI·event 사후검증
- [5. CarMax FY2019 results](https://www.sec.gov/Archives/edgar/data/1170010/000117001019000016/q4fy19earningsrelease.htm) — SEC. 사업·KPI·event 사후검증
- [6. CarMax FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001023000010/kmx-20230228.htm) — SEC. 사업·KPI·event 사후검증

---

<!-- idea:482da55b-99d9-41b8-91a0-0dcee69dcaa7 -->
## 2. 2015-12-22 — scale + store growth + operating leverage

### 결론부터

**종합판정: 성공.** fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**증권 결과:** SQL 1년 +23.1%, 5년 +87.4%

**Thesis / Process 점수:** 9.2 / 8.8

### 1. 무슨 기업인가

CarMax는 미국 최대급 used-car retailer로 no-haggle pricing, 대규모 재고, appraisal/trade-in sourcing, wholesale auctions와 CarMax Auto Finance(CAF)를 결합한다. 핵심 KPI는 retail/wholesale units, comparable-store units, gross profit/unit, inventory turn, store count, omnichannel conversion, CAF penetration·spread·credit losses다.

### 2. 산업 가치사슬과 돈의 흐름

고객에게 차량을 매입해 reconditioning 후 retail로 판매하고 retail 기준에 맞지 않는 차량은 wholesale auction으로 처분한다. retail spread가 크지 않아도 inventory turn과 scale이 수익을 만들고 CAF가 별도의 finance spread를 제공한다. store는 appraisal·reconditioning·test-drive·fulfillment node 역할을 한다.

### 3. 경쟁우위·핵심 KPI

No-haggle brand, 전국 inventory pool, appraisal 데이터, wholesale auction, CAF와 store density가 결합된 경쟁우위다. Carvana 등 digital 경쟁, used-car 가격과 금리·신용손실이 주요 위험이다.

### 4. 당시 VIC 원문

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

### 5. 밸류에이션

17x forward earnings와 EPS compounding 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 적중 · 논지 비중 18%

**당시 주장**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**당시 근거**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

**정량적 괴리**

Entry: $52.12 → 1y +23.1%

**분석 오류·핵심**

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 적중 · 논지 비중 18%

**당시 주장**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**당시 근거**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

**정량적 괴리**

Retail units: 582,282 → 748,961

**분석 오류·핵심**

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 적중 · 논지 비중 16%

**당시 주장**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**당시 근거**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

**정량적 괴리**

Stores: 144 → 203

**분석 오류·핵심**

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 적중 · 논지 비중 16%

**당시 주장**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**당시 근거**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

**정량적 괴리**

5y return: 장기 compounding → +87.4%

**분석 오류·핵심**

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 성공 · 논지 비중 16%

**당시 주장**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**당시 근거**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

**정량적 괴리**

Entry: $52.12 → 1y +23.1%

**분석 오류·핵심**

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 성공 · 논지 비중 16%

**당시 주장**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**당시 근거**

약 17x earnings에 industry largest player·customer orientation·2년 12%+ store growth와 operating leverage

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

**정량적 괴리**

Retail units: 582,282 → 748,961

**분석 오류·핵심**

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

FY2015 582,282대/144 stores에서 FY2019 748,961대/203 stores; SQL 5년 +87.4%

### 7. 사업과 증권 결과 분리

SQL 1년 +23.1%, 5년 +87.4%

### 8. 무엇을 맞고 틀렸나

fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄

### 9. 최초 검증·반증 신호

2017-02-28 — store count와 used-unit growth 지속

### 10. 최종 교훈

성공 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $52.12 | 원 VIC 논지 방향 | 1y +23.1% | 적중 |
| Retail units | 582,282 | 원 VIC 논지 방향 | 748,961 | 적중 |
| Stores | 144 | 원 VIC 논지 방향 | 203 | 적중 |
| 5y return | 장기 compounding | 원 VIC 논지 방향 | +87.4% | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2015-12-22 | VIC 게시 | scale + store growth + operating leverage |
| 2017-02-28 | 최초 신호 | store count와 used-unit growth 지속 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** fragmented market에서 scale·brand·financing·store density mechanism을 잘 봄
- **최초 검증·반증 신호:** 2017-02-28 — store count와 used-unit growth 지속
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 중간
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC KMX 2015-12-22 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. CarMax FY2010 filing](https://www.sec.gov/Archives/edgar/data/1170010/000117001010000044/tenq.htm) — SEC. 사업·KPI·event 사후검증
- [3. CarMax FY2015 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001015000008/kmx-20150228x10k.htm) — SEC. 사업·KPI·event 사후검증
- [4. CarMax FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001019000040/kmx0228201910-k.htm) — SEC. 사업·KPI·event 사후검증
- [5. CarMax FY2019 results](https://www.sec.gov/Archives/edgar/data/1170010/000117001019000016/q4fy19earningsrelease.htm) — SEC. 사업·KPI·event 사후검증
- [6. CarMax FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001023000010/kmx-20230228.htm) — SEC. 사업·KPI·event 사후검증

---

<!-- idea:d4298930-0f02-4c0b-90d7-3e521d05a5f4 -->
## 3. 2019-08-07 — omnichannel margin-neutral transition

### 결론부터

**종합판정: 성공.** 오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**증권 결과:** SQL 1년 +19.8%, 2년 +59.5%, 3년 +18.7%

**Thesis / Process 점수:** 9.2 / 8.8

### 1. 무슨 기업인가

CarMax는 미국 최대급 used-car retailer로 no-haggle pricing, 대규모 재고, appraisal/trade-in sourcing, wholesale auctions와 CarMax Auto Finance(CAF)를 결합한다. 핵심 KPI는 retail/wholesale units, comparable-store units, gross profit/unit, inventory turn, store count, omnichannel conversion, CAF penetration·spread·credit losses다.

### 2. 산업 가치사슬과 돈의 흐름

고객에게 차량을 매입해 reconditioning 후 retail로 판매하고 retail 기준에 맞지 않는 차량은 wholesale auction으로 처분한다. retail spread가 크지 않아도 inventory turn과 scale이 수익을 만들고 CAF가 별도의 finance spread를 제공한다. store는 appraisal·reconditioning·test-drive·fulfillment node 역할을 한다.

### 3. 경쟁우위·핵심 KPI

No-haggle brand, 전국 inventory pool, appraisal 데이터, wholesale auction, CAF와 store density가 결합된 경쟁우위다. Carvana 등 digital 경쟁, used-car 가격과 금리·신용손실이 주요 위험이다.

### 4. 당시 VIC 원문

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

### 5. 밸류에이션

낮은 nationwide share와 omnichannel 회복을 반영한 장기 EPS compound 사업가정과 starting price를 분리한다.

### 투자논지를 구성한 핵심 주장

#### 1. 생존·유동성 — 적중 · 논지 비중 18%

**당시 주장**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**당시 근거**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

**정량적 괴리**

Stores: 203 → 전국 omnichannel 확대

**분석 오류·핵심**

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**재사용할 교훈**

생존·유동성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 2. 수요·volume — 적중 · 논지 비중 18%

**당시 주장**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**당시 근거**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

**정량적 괴리**

Retail units: 748,961 → FY2023 807,823

**분석 오류·핵심**

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**재사용할 교훈**

수요·volume는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 3. 단위경제성 — 적중 · 논지 비중 16%

**당시 주장**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**당시 근거**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

**정량적 괴리**

CAF income: $438.7m → finance profit pool 유지

**분석 오류·핵심**

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**재사용할 교훈**

단위경제성는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 4. 자본배분·capacity — 부분 적중 · 논지 비중 16%

**당시 주장**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**당시 근거**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

**정량적 괴리**

3y return: 상승 기대 → +18.7%

**분석 오류·핵심**

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**재사용할 교훈**

자본배분·capacity는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 5. 경쟁우위·시장구조 — 성공 · 논지 비중 16%

**당시 주장**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**당시 근거**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

**정량적 괴리**

Stores: 203 → 전국 omnichannel 확대

**분석 오류·핵심**

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**재사용할 교훈**

경쟁우위·시장구조는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

#### 6. valuation·촉매 — 성공 · 논지 비중 16%

**당시 주장**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**당시 근거**

온라인 대응은 늦었지만 store·inventory·CAF를 이용해 true omnichannel을 margin-neutral하게 구현 가능

**이 주장이 성립하려면**

핵심 KPI와 자금조달 환경이 causal chain을 지지한다.

**사전 반증조건**

2~3개 분기 KPI가 반대 방향이거나 capital needs/competition이 기대수익을 소진한다.

**실제 결과**

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

**정량적 괴리**

Retail units: 748,961 → FY2023 807,823

**분석 오류·핵심**

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

**재사용할 교훈**

valuation·촉매는 사전 KPI와 반증조건으로 저장하고 반대 signal에서 확률을 갱신한다.

### 6. 실제 전개

FY2019 203 stores/748,961 units/$18.17bn revenue; FY2023 retail 807,823대·managed receivables $16.77bn; SQL 1년 +19.8%

### 7. 사업과 증권 결과 분리

SQL 1년 +19.8%, 2년 +59.5%, 3년 +18.7%

### 8. 무엇을 맞고 틀렸나

오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석

### 9. 최초 검증·반증 신호

2020-02-29 — omnichannel rollout 확대

### 10. 최종 교훈

성공 정적 headline보다 KPI 변화율과 cash runway를 함께 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Stores | 203 | 원 VIC 논지 방향 | 전국 omnichannel 확대 | 적중 |
| Retail units | 748,961 | 원 VIC 논지 방향 | FY2023 807,823 | 적중 |
| CAF income | $438.7m | 원 VIC 논지 방향 | finance profit pool 유지 | 적중 |
| 3y return | 상승 기대 | 원 VIC 논지 방향 | +18.7% | 부분 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-08-07 | VIC 게시 | omnichannel margin-neutral transition |
| 2020-02-29 | 최초 신호 | omnichannel rollout 확대 |
| 2018-12-31 | 운영 KPI 중간점검 | 초기 narrative보다 scale과 unit economics 재평가 |
| 2019-12-31 | 산업구조 변화 | 실제 operating path 비교 |
| 2021-12-31 | 후속 결과 | 사업과 valuation 분리 |
| 2024-01-31 | 고정 평가일 | 최종 postmortem |

### Failure / Success Anatomy

- **근본 오류/핵심:** 오프라인 store를 online의 적이 아니라 sourcing·reconditioning·fulfillment node로 재해석
- **최초 검증·반증 신호:** 2020-02-29 — omnichannel rollout 확대
- **당시 알 수 있었나:** 생산·인도·점포·판매량·gross profit·CAF·현금·자금조달 공시로 검증 가능했다.
- **피할 수 있었나:** 중간
- **반사실 질문:** 핵심 KPI가 예상대로 움직여도 starting valuation과 balance-sheet runway를 반영하면 목표수익률이 남는가?

### 주요 근거자료

- 1. VIC KMX 2019-08-07 — Value Investors Club / user SQL. 원 thesis와 실제 방향 복원
- [2. CarMax FY2010 filing](https://www.sec.gov/Archives/edgar/data/1170010/000117001010000044/tenq.htm) — SEC. 사업·KPI·event 사후검증
- [3. CarMax FY2015 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001015000008/kmx-20150228x10k.htm) — SEC. 사업·KPI·event 사후검증
- [4. CarMax FY2019 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001019000040/kmx0228201910-k.htm) — SEC. 사업·KPI·event 사후검증
- [5. CarMax FY2019 results](https://www.sec.gov/Archives/edgar/data/1170010/000117001019000016/q4fy19earningsrelease.htm) — SEC. 사업·KPI·event 사후검증
- [6. CarMax FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1170010/000117001023000010/kmx-20230228.htm) — SEC. 사업·KPI·event 사후검증

---
# 배치 공통 학습

1. 생존·성장·주가를 한 문장에 넣지 않는다.
2. 자본집약 사업에서는 KPI 수준보다 변화율이 중요하다.
3. 가격인하는 수요부진과 penetration 전략을 volume·gross margin과 함께 구분한다.
4. scale economy는 단위 margin만으로 보이지 않는다.
5. 오프라인 자산은 디지털 전환에서 fulfillment node가 될 수 있다.
6. business Short, valuation Short, short-volatility는 서로 다른 거래다.
