# AlarmForce Industries Inc. (AF) — 2014-03-10 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AlarmForce Industries Inc. / AF |
| VIC 게시일 / 작성자 | 2014-03-10 / thistle933 |
| 분석 증권 / 실제 방향 | AlarmForce common equity / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | C$10.70 |
| 기대기간 | 2~3년 운영개선·전략대안 |
| raw horizon audit | 142.4k customers, downside FCF/share C$0.58, upside C$1.07 |
| 최종 판정 | **성공 — C$10.70→C$16 takeout** |

> **결론:** raw Short는 실제 Long으로 교정했다. 142.4k customers, 91% recurring revenue와 net cash가 downside를 지지했고 운영성장은 강하지 않았지만 BCE가 C$16 cash로 인수했다. 단순 price comparison은 약 +49.5%이며 배당·세금·정확 IRR은 별도다.

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

founder 제거와 실패한 sale process 뒤 C$10.70에 거래됐다. 142.4k customers, 14% churn, CAC $746, 91% recurring revenue와 net cash를 바탕으로 professionalization과 재매각 optionality를 샀다.

### Reverse expectations

시장은 높은 churn·CAC, 정체된 subscriber base, governance disruption과 이전 sale 실패가 intrinsic FCF와 strategic value를 훼손할 가능성을 반영했다.

---

## 3. 원문 투자논지 지도

### C1. raw Short — metadata 실패

**원문 주장**

SQL은 Short다.

**경제적 메커니즘**

방향 오류는 payoff를 반전시킨다.

**T0 근거**

원문 upside·FCF 논리.

**숨은 가정**

원문 읽기.

**사전 반증조건**

하락 베팅이면 Short.

**실제 결과**

실제는 Long.

**정량 gap**

완전 반대.

**분석 오류 또는 제한**

metadata 의존.

**재사용 교훈**

원문 payoff를 우선한다.

### C2. downside FCF $0.58 — 방향 성공

**원문 주장**

보수적 FCF가 valuation floor다.

**경제적 메커니즘**

recurring fees가 cash를 만든다.

**T0 근거**

91% recurring revenue.

**숨은 가정**

churn·CAC 안정.

**사전 반증조건**

FCF 붕괴면 반증.

**실제 결과**

base 유지 후 takeout.

**정량 gap**

정확 FCF bridge 제한.

**분석 오류 또는 제한**

reported metric 정의 부족.

**재사용 교훈**

maintenance CAC 뒤 FCF를 쓴다.

### C3. upside FCF $1.07 — 운영 미달

**원문 주장**

전문화로 FCF/share가 크게 상승.

**경제적 메커니즘**

CAC·opex 효율화.

**T0 근거**

founder removal.

**숨은 가정**

subscriber growth 재개.

**사전 반증조건**

성장정체면 미달.

**실제 결과**

growth는 강하게 회복하지 않음.

**정량 gap**

upside denominator 미확인.

**분석 오류 또는 제한**

governance catalyst 과대.

**재사용 교훈**

KPI milestones를 사전 둔다.

### C4. 142.4k customer base — 성공

**원문 주장**

sticky customers가 downside를 지지.

**경제적 메커니즘**

월 반복청구·낮은 service cost.

**T0 근거**

contracted base.

**숨은 가정**

churn 폭증 없음.

**사전 반증조건**

base 급감이면 반증.

**실제 결과**

BCE가 base를 인수.

**정량 gap**

전략가치 확인.

**분석 오류 또는 제한**

고객 수와 quality 혼용 위험.

**재사용 교훈**

cohort churn·ARPU를 추적한다.

### C5. professionalization — 부분 성공

**원문 주장**

founder 제거 뒤 운영개선.

**경제적 메커니즘**

governance·capital allocation 개선.

**T0 근거**

board change.

**숨은 가정**

management execution.

**사전 반증조건**

CAC/churn 악화면 반증.

**실제 결과**

운영 개선은 혼합.

**정량 gap**

성장 bull 미실현.

**분석 오류 또는 제한**

사람 교체를 결과로 봄.

**재사용 교훈**

운영 KPI가 확인될 때만 credit한다.

### C6. sale optionality — 강한 성공

**원문 주장**

전략적 buyer가 premium을 지불.

**경제적 메커니즘**

telco synergy+recurring base.

**T0 근거**

이전 sale interest.

**숨은 가정**

asset remains attractive.

**사전 반증조건**

장기 독립·저가 거래면 실패.

**실제 결과**

BCE C$16 cash.

**정량 gap**

entry 대비 +49.5% 단순.

**분석 오류 또는 제한**

매각을 base에 넣을 위험.

**재사용 교훈**

standalone downside와 option을 분리한다.

---

## 4. 당시 Valuation과 Payoff Structure

downside FCF/share C$0.58와 upside C$1.07을 두고 cash-flow multiple을 적용했다. sale은 base가 아니라 option이어야 하며 C$10.70이 downside FCF에도 감당 가능한지 봐야 했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | churn↑·CAC↑·sale 없음 | FCF $0.58×저배수 | 미발생 |
| Base | 안정 customer base | 운영가치 유지 | 대체로 실현 |
| Bull | professionalization·takeout | C$16+ | 실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | C$10.70 | downside 보호 | C$16 consideration | +49.5% 단순 |
| Customers | 142.4k | 재성장 | 대체로 정체 | 미달 |
| Churn | 14% | 개선 | 구조적 부담 지속 | 혼합 |
| CAC | $746 | 효율개선 | 성장제약 | 미달 |
| Recurring revenue | 91% | 가치보존 | buyer가 인수 | 성공 |

### 촉매와 시간

판정 horizon은 **2~3년 운영개선·전략대안**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2014-03-10 | VIC Long | raw Short 교정 |
| 2014 | founder 이후 governance | professionalization |
| 2015 | growth 정체 | 운영 bull 경고 |
| 2016 | recurring base 유지 | downside 지지 |
| 2017-H1 | 전략대안 | takeout option |
| 2017-11-06 | BCE C$16 발표 | 가치 실현 |
| 2018-01-05 | 거래 종결 | terminal payoff |
| 후속 | +49.5% 단순 비교 | IRR 과장 방지 |

### 실제 사업·자본구조 추이

subscriber growth는 크게 가속되지 않았지만 contracted customer base와 recurring revenue가 유지됐다. BCE는 2017-11 C$16 cash acquisition을 발표했고 2018-01-05 종결했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

C$16/C$10.70-1≈+49.5%의 단순 corporate-action comparison이다. 보유기간 배당·세금·정확 settlement dates를 넣은 total return/IRR은 주장하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | raw Short | 20% | metadata 실패 | 완전 반대. |
| C2 | downside FCF $0.58 | 18% | 방향 성공 | 정확 FCF bridge 제한. |
| C3 | upside FCF $1.07 | 18% | 운영 미달 | upside denominator 미확인. |
| C4 | 142.4k customer base | 16% | 성공 | 전략가치 확인. |
| C5 | professionalization | 16% | 부분 성공 | 성장 bull 미실현. |
| C6 | sale optionality | 12% | 강한 성공 | entry 대비 +49.5% 단순. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

완벽한 operating turnaround보다 recurring cash flow의 보존과 telco buyer의 bundle synergy가 terminal value를 만들었다.

### Counterfactual

sale을 0으로 두고 churn 16%, CAC C$850, FCF/share C$0.58만 적용해도 C$10.70에 충분한 downside protection이 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

운영개선과 재매각 가능성을 함께 base에 넣을 위험이 있었고 customer additions보다 churn·CAC sensitivity를 더 강하게 봤어야 했다.

### 최초로 관찰 가능했던 경고신호

subscriber growth 정체가 운영 bull case의 첫 경고였지만 recurring base·cash flow가 무너지지 않아 전체 thesis break는 아니었다.

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
| Business thesis | recurring base 유지 |
| Valuation thesis | downside 지지 |
| Catalyst thesis | takeout 성공 |
| Security payoff | common 적절 |
| Timing / path | 운영 지연·event 성공 |
| Thesis score | 8.5/10 |
| Process score | 8.2/10 |
| 종합 | **성공 — C$10.70→C$16 takeout** |

### 한 문장 교훈

> subscriber economics는 지역·channel별 CAC와 churn cohort로 검증한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2014-03-10. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL은 source SQL에서 null이다.
2. [AlarmForce FY2010 results](https://www.newswire.ca/news-releases/alarmforce-closes-2010-fiscal-year-with-over-113500-subscribers-547257212.html) — AlarmForce / CNW, 2011. FY2010 subscriber 113,500명 검증.
3. [AlarmForce FY2015 results](https://www.globenewswire.com/news-release/2016/01/21/1279609/0/en/AlarmForce-Reports-Q4-2015-Financial-Results.html) — AlarmForce, 2016-01-21. FY2015 subscriber 144,200명과 운영성과 검증.
4. [BCE acquisition announcement](https://www.globenewswire.com/news-release/2017/11/06/1324295/0/en/alarmforce-to-be-acquired-by-bce.html) — BCE / AlarmForce, 2017-11-06. C$16 현금 거래조건 검증.
5. [BCE completes AlarmForce acquisition](https://www.globenewswire.com/news-release/2018/01/05/1324311/0/en/bce-completes-acquisition-of-alarmforce.html) — BCE, 2018-01-05. 인수 종결과 terminal payoff 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported operating data만 사용; exact transaction ledger가 없으면 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
