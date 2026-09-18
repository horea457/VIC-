# AlarmForce Industries Inc. (AF) — 2009-11-08 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AlarmForce Industries Inc. / AF |
| VIC 게시일 / 작성자 | 2009-11-08 / hb190 |
| 분석 증권 / 실제 방향 | AlarmForce common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 2009 AF common; 약 100k subscribers |
| 기대기간 | 3~5년 |
| raw horizon audit | 200~250k subscribers, 26% new-customer IRR, steady-state EV/EBITDA 3.2x |
| 최종 판정 | **부분 성공 — recurring franchise 성공, growth 과대** |

> **결론:** SAC 약 $662, after-tax 신규고객 IRR 26%, gross margin 78%라는 recurring economics는 가치 있는 franchise를 포착했다. 그러나 subscribers는 2010 113.5k, 2015 144.2k로 200~250k 목표에 크게 못 미쳤다. 2018 BCE C$16 takeout은 strategic value를 검증하지만 원 3~5년 growth forecast를 구제하지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

AlarmForce는 월 모니터링료를 받는 residential security 회사였다. 신규 고객 CAC를 먼저 지출하고 장기간 monthly recurring revenue와 높은 gross margin으로 회수한다. 고객 lifetime, churn, 지역별 설치·광고 CAC와 현금전환이 subscriber growth보다 중요하며, contracted base는 전략적 인수자에게 별도 가치가 있다.

subscriber additions × lifetime gross profit - CAC - service/installation cost - G&A - capex = FCF; 지역별 cohort payback과 churn을 분리한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

subscribers, net adds, churn, ARPU, gross margin, CAC/SAC, payback, cohort IRR, recurring-revenue mix, FCF/share

---

## 2. 당시 상황과 시장이 가격에 넣은 것

약 100k subscribers에서 낮은 churn과 월 $25+ recurring fee, SAC 회수 economics를 미국 확장에 재투자하면 3~5년 200~250k subscribers가 가능하다는 논지였다.

### Reverse expectations

시장은 지역별 브랜드·광고효율, 설치 economics와 incumbent competition 때문에 기존 market의 CAC·churn을 새 지역에 복제하기 어렵다고 봤다.

---

## 3. 원문 투자논지 지도

### C1. SAC ~$662 — 지역별 미검증

**원문 주장**

낮은 SAC로 고객을 확보한다.

**경제적 메커니즘**

upfront CAC를 recurring margin으로 회수.

**T0 근거**

기존 cohort.

**숨은 가정**

새 지역 CAC도 유사.

**사전 반증조건**

CAC 급등이면 반증.

**실제 결과**

성장목표 미달로 복제성 제한.

**정량 gap**

정확한 후속 SAC 없음.

**분석 오류 또는 제한**

평균을 지역에 외삽.

**재사용 교훈**

channel·region cohort를 분리한다.

### C2. new-customer IRR 26% — 부분 성공

**원문 주장**

신규고객 투자수익이 높다.

**경제적 메커니즘**

낮은 churn과 높은 gross margin.

**T0 근거**

SAC·monthly fee.

**숨은 가정**

lifetime/churn 안정.

**사전 반증조건**

payback 연장·net adds 둔화면 약화.

**실제 결과**

franchise는 유지·성장은 둔화.

**정량 gap**

IRR 방향만 지지.

**분석 오류 또는 제한**

terminal churn 가정 민감.

**재사용 교훈**

IRR보다 payback·retention curve를 본다.

### C3. gross margin 78% — 성공

**원문 주장**

recurring monitoring이 고마진이다.

**경제적 메커니즘**

fixed platform에 월 fee가 쌓인다.

**T0 근거**

T0 margin.

**숨은 가정**

service cost 통제.

**사전 반증조건**

margin 급락이면 반증.

**실제 결과**

BCE가 recurring base를 인수.

**정량 gap**

전략가치 확인.

**분석 오류 또는 제한**

gross margin과 FCF 혼동.

**재사용 교훈**

CAC·G&A 뒤 cash를 본다.

### C4. 200~250k subscribers — 실패

**원문 주장**

3~5년 subscriber 두 배.

**경제적 메커니즘**

geographic reinvestment.

**T0 근거**

약 100k base.

**숨은 가정**

net adds 가속.

**사전 반증조건**

2015 <180k면 반증.

**실제 결과**

2015 144.2k.

**정량 gap**

하단 대비 -55.8k/-27.9%.

**분석 오류 또는 제한**

growth extrapolation.

**재사용 교훈**

필요 net adds를 사전 calendar로 둔다.

### C5. steady-state 3.2x EV/EBITDA — 제한적 성공

**원문 주장**

growth spend 정상화 시 매우 싸다.

**경제적 메커니즘**

CAC 지출 감소가 EBITDA로 전환.

**T0 근거**

recurring margin.

**숨은 가정**

subscriber base 유지.

**사전 반증조건**

churn/decline이면 무효.

**실제 결과**

base는 유지되고 takeout 발생.

**정량 gap**

정확 multiple 미복원.

**분석 오류 또는 제한**

성장비용을 선택재로 봄.

**재사용 교훈**

maintenance acquisition spend를 분리한다.

### C6. strategic takeout — 장기 성공

**원문 주장**

customer base가 인수매력이 있다.

**경제적 메커니즘**

telco bundle·cross-sell synergy.

**T0 근거**

contracted revenue.

**숨은 가정**

buyer synergy.

**사전 반증조건**

독립가치만 남으면 미실현.

**실제 결과**

BCE C$16 acquisition.

**정량 gap**

terminal price 확인.

**분석 오류 또는 제한**

원 horizon 밖 event.

**재사용 교훈**

later takeout으로 growth miss를 지우지 않는다.

---

## 4. 당시 Valuation과 Payoff Structure

원문은 steady-state EV/EBITDA 약 3.2x와 customer IRR 26%를 저평가 근거로 삼았다. growth capex를 비용처리하더라도 cohort economics가 재현돼야 multiple이 싸다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | CAC 상승·churn 악화 | 성장정체 | 부분 현실화 |
| Base | 지속 net adds | 200k 접근 | 144.2k에 그침 |
| Bull | 미국 확장 | 250k+·rerating | 실패 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Subscribers T0 | 약 100k | 200~250k | 2015 144.2k | 42~58% 미달 |
| FY2010 subscribers | 약 100k | 고성장 | 113.5k | 초기 미달 |
| SAC | ~$662 | stable | 지역별 불확실 | 복제 미확인 |
| Gross margin | ~78% | 유지 | recurring model 지속 | 방향 성공 |
| Terminal | 성장 rerating | 전략가치 | BCE C$16 | 장기 성공 |

### 촉매와 시간

판정 horizon은 **3~5년**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2009-11-08 | VIC Long | unit economics thesis |
| 2010 | 113.5k subscribers | 성장속도 경고 |
| 2011 | 미국확장 | CAC test |
| 2013 | subscriber growth 둔화 | target risk |
| 2015 | 144.2k subscribers | 200k 미달 |
| 2017-11-06 | BCE deal 발표 | strategic value |
| 2018-01-05 | C$16 deal 종결 | terminal payoff |
| 후속 | growth와 takeout 분리 | 혼합 판정 |

### 실제 사업·자본구조 추이

FY2010 subscribers는 113.5k, FY2015는 144.2k였다. recurring customer base는 남았지만 200~250k expansion은 미달했다. BCE는 2018-01 C$16/share 현금으로 인수를 완료했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

T0 share price와 배당 ledger가 완전하지 않아 exact return은 보류한다. subscriber forecast와 terminal C$16 takeout을 별도 판정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | SAC ~$662 | 20% | 지역별 미검증 | 정확한 후속 SAC 없음. |
| C2 | new-customer IRR 26% | 18% | 부분 성공 | IRR 방향만 지지. |
| C3 | gross margin 78% | 18% | 성공 | 전략가치 확인. |
| C4 | 200~250k subscribers | 16% | 실패 | 하단 대비 -55.8k/-27.9%. |
| C5 | steady-state 3.2x EV/EBITDA | 16% | 제한적 성공 | 정확 multiple 미복원. |
| C6 | strategic takeout | 12% | 장기 성공 | terminal price 확인. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

운영 가치는 sticky monthly revenue가 만들었지만 성장속도는 geographic CAC의 불리한 재현성 때문에 낮아졌다. 최종 payoff는 strategic buyer가 customer base와 bundling synergy를 평가해 만들었다.

### Counterfactual

새 지역 SAC가 50% 높고 churn이 2ppt 높아도 신규고객 IRR이 hurdle을 넘고 200k subscribers에 도달하는가?

---

## 9. 분석 오류 유형과 최초 경고

기존 cohort economics를 다른 지역에 일정하게 적용하고 subscriber count가 두 배가 될 때 필요한 CAC·설치자본을 과소평가했다.

### 최초로 관찰 가능했던 경고신호

2010 113.5k의 성장속도가 200~250k 목표에 필요한 run-rate에 못 미친 것이 첫 경고였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

subscriber economics는 지역·channel별 CAC와 churn cohort로 검증한다.

### Lesson 2

좋은 recurring franchise와 공격적 subscriber forecast를 분리한다.

### Lesson 3

founder removal은 운영개선의 보증이 아니라 governance catalyst다.

### Lesson 4

전략적 takeout은 customer base 가치의 별도 실현경로다.

### 지금 같은 아이디어를 다시 본다면

- regional net adds
- CAC
- churn
- ARPU
- cohort payback
- FCF/share
- strategic-buyer synergies

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | franchise 성공 |
| Valuation thesis | growth denominator 과대 |
| Catalyst thesis | takeout 장기 성공 |
| Security payoff | common 적절 |
| Timing / path | 3~5년 미달 |
| Thesis score | 6.5/10 |
| Process score | 7.2/10 |
| 종합 | **부분 성공 — recurring franchise 성공, growth 과대** |

### 한 문장 교훈

> subscriber economics는 지역·channel별 CAC와 churn cohort로 검증한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2009-11-08. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL은 source SQL에서 null이다.
2. [AlarmForce FY2010 results](https://www.newswire.ca/news-releases/alarmforce-closes-2010-fiscal-year-with-over-113500-subscribers-547257212.html) — AlarmForce / CNW, 2011. FY2010 subscriber 113,500명 검증.
3. [AlarmForce FY2015 results](https://www.globenewswire.com/news-release/2016/01/21/1279609/0/en/AlarmForce-Reports-Q4-2015-Financial-Results.html) — AlarmForce, 2016-01-21. FY2015 subscriber 144,200명과 운영성과 검증.
4. [BCE acquisition announcement](https://www.globenewswire.com/news-release/2017/11/06/1324295/0/en/alarmforce-to-be-acquired-by-bce.html) — BCE / AlarmForce, 2017-11-06. C$16 현금 거래조건 검증.
5. [BCE completes AlarmForce acquisition](https://www.globenewswire.com/news-release/2018/01/05/1324311/0/en/bce-completes-acquisition-of-alarmforce.html) — BCE, 2018-01-05. 인수 종결과 terminal payoff 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported operating data만 사용; exact transaction ledger가 없으면 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
