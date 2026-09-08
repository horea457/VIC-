# Batch 016 — Cigna / UnitedHealth V9 Index

> 기존 `analysis/batch_016_cigna_unitedhealth_10.md`와 `analysis/batch_016_cigna_unitedhealth_v2_deep.md`는 archive/reference로 유지한다.  
> V9에서는 **10개 VIC 아이디어를 각각 독립 canonical report**로 관리한다.  
> 이번 버전은 기존 V7보다 더 구체적으로 **사업구조 → 당시 시장기대 → causal chain → 6개 claim → 숫자 검증 → chronology → 최초 thesis break → knowability → security selection → counterfactual** 순으로 보강했다.

---

# 1. Canonical idea files

## Cigna (CI) — 8건

| 날짜 | 파일 | 실제 결과 | 핵심 판정 |
|---|---|---|---|
| 2000-09-21 | [CI Watchlist Long](ideas/2000/2000-09-21_CI_long.md) | 실제 체결이 불명확한 $70 이하 진입대기형 | 구조적 통찰 일부 적중·투자논지 미완성 |
| 2003-12-30 | [CI Turnaround Long](ideas/2003/2003-12-30_CI_long.md) | 약 $57.5 → $81.57, 약 +42% | 매우 성공 |
| 2009-07-13 | [CI Event Long](ideas/2009/2009-07-13_CI_long.md) | 약 $24.4 → $35.27, 약 +45% | 가격 성공·PBM 매각 촉매 실패 |
| 2012-09-23 | [CI ACA Long](ideas/2012/2012-09-23_CI_long.md) | 약 $47.4 → $87.48, 약 +85% | 매우 성공 |
| 2017-02-20 | [CI Standalone Long](ideas/2017/2017-02-20_CI_long.md) | 약 $143~144 → $203, 약 +40% | 매우 성공 |
| 2019-03-28 | [CI Express Scripts Long](ideas/2019/2019-03-28_CI_long.md) | $160 → 2021말 약 $230, +44%; $350 target 미달 | 사업논지 적중·multiple thesis 실패 |
| 2021-06-03 | [CI Evernorth Long](ideas/2021/2021-06-03_CI_long.md) | 2021말 약 -10%; 2022말 $331.34 | 운영예측 정확·timing 오류 |
| 2022-09-25 | [CI Compounder Long](ideas/2022/2022-09-25_CI_long.md) | 약 $279 → 2023말 $299.45, 약 +7% | 사업·buyback 부분 적중·SOTP/multiple 실패 |

## UnitedHealth Group (UNH) — 2건

| 날짜 | 파일 | 실제 결과 | 핵심 판정 |
|---|---|---|---|
| 2006-12-30 | [UNH Platform Long](ideas/2006/2006-12-30_UNH_long.md) | $53.73 → 2008말 약 $26.6, 약 -50% | 중기 투자 실패·장기 Optum 통찰 탁월 |
| 2007-12-20 | [UNH LEAPS Long](ideas/2007/2007-12-20_UNH_long.md) | $58.11 → 2008말 $26.6; Jan-2010 $50 strike LEAPS 실패 | 명백한 security-selection 실패 |

---

# 2. Managed Care를 보험업 하나로 보면 안 되는 이유

Managed care 기업은 적어도 네 가지 경제성을 나눠 봐야 한다.

## 2-1. ASO — fee-like earnings

ASO(Administrative Services Only)는 고용주가 실제 claims를 부담한다.

보험사는:
- provider network
- claims processing
- plan design
- utilization management

을 제공하고 fee를 받는다.

따라서:

**ASO membership × admin fee - service cost = ASO earnings**

에 가깝다.

보험회사가 의료비를 직접 부담하지 않으므로 risk-bearing book보다 capital intensity와 underwriting volatility가 낮다.

---

## 2-2. Risk-bearing insurance — medical trend와 pricing의 싸움

보험사가 claims를 직접 부담하는 경우:

**Premium  
- medical claims  
- SG&A  
= underwriting earnings**

이다.

가장 중요한 지표는 MLR(Medical Loss Ratio).

핵심은 단순 의료비 상승률이 아니다.

> **Pricing trend - Medical cost trend**

가 중요하다.

예를 들어:
- premium +5%
- medical cost +8%

이면 시간이 갈수록 margin이 줄어든다.

따라서 “의료비가 오른다”를 투자논지로 쓰려면 반드시:

**medical trend  
→ pricing gap  
→ MLR  
→ segment earnings  
→ consolidated EPS/FCF**

까지 연결해야 한다.

---

# 3. PBM / Evernorth / Optum — 보험 외 이익은 왜 다른가

## Cigna — Evernorth

Express Scripts 이후 Cigna는:
- PBM
- specialty pharmacy
- care services
- health-data services

비중이 커졌다.

PBM의 핵심은 prescription volume 하나가 아니다.

봐야 할 것은:
- client retention
- rebate economics
- formulary power
- specialty mix
- client repricing
- regulatory pressure

다.

## UNH — Optum

Optum은:
- Optum Health
- Optum Insight
- Optum Rx

를 통해 보험 외 fee/service earnings를 만든다.

핵심 flywheel은:

**insurance membership  
→ claims / clinical data  
→ analytics / care management  
→ lower cost / better outcomes  
→ stronger employer/provider proposition  
→ more membership / service revenue**

다.

이 구조는 매우 강하지만:

> **좋은 서비스사업 = 자동으로 높은 multiple**

은 아니다.

Organic growth, client retention, acquisition ROIC, capital intensity를 확인해야 한다.

---

# 4. Cigna 2000 — 큰 산업위험보다 가까운 운영리스크

2000 아이디어는 ASO economics를 premium accounting과 분리한 점은 좋았다.

하지만 주된 관심이 health-reform risk에 쏠렸다.

실제 더 가까운 위험은:
- claims-processing 문제
- customer service
- reserve visibility
- retention

이었다.

결국 2002년 Cigna는 운영문제로 크게 흔들렸다.

### 재사용 교훈

> **큰 거시·규제 리스크가 눈에 띄어도, 당장 earnings를 깨뜨릴 기업고유 operational bottleneck을 먼저 본다.**

또 이 글은 실제 체결이 확인되지 않는 watchlist형이라:

> **아이디어 성과와 실제 투자성과를 분리**

했다.

---

# 5. Cigna 2003 — Turnaround 분석의 좋은 형태

2003 Long은 단순 “싸다”가 아니었다.

구체적 chain은:

**claims-system 정상화  
→ claims 처리 정확도/속도 개선  
→ reserve visibility 개선  
→ MLR 정상화  
→ customer retention 개선  
→ EPS/FCF 회복  
→ valuation 정상화**

였다.

실제 약:

**$57.5 → $81.57, 약 +42%**

로 12개월 $80 목표를 거의 정확히 달성했다.

### 좋은 turnaround의 조건

1. 병목이 무엇인지 안다.
2. 병목이 어떤 KPI를 움직여야 하는지 안다.
3. KPI가 earnings로 어떻게 연결되는지 안다.
4. 매 분기 thesis confirmation이 가능하다.

이 구조가 있어야 단순 mean reversion과 구분된다.

---

# 6. Cigna 2009 — 가격 성공과 catalyst 성공은 다르다

원문 핵심 촉매는 PBM 매각이었다.

주가는:
- 약 $24.4
- 2009말 약 $35.27
- 약 +45%

로 목표범위를 달성했다.

하지만 **PBM 매각은 발생하지 않았다.**

따라서:

**가격 성공  
≠ Catalyst 성공**

이다.

실제 주가상승은:
- operating earnings 회복
- 시장 risk-on
- managed-care multiple 정상화

가 더 중요했다.

### DB 원칙

사후에 가격이 올랐다는 이유로 원래 catalyst가 맞았다고 재작성하지 않는다.

---

# 7. Cigna 2012 — 정책 headline을 실제 profit pool로 변환

ACA가 managed care 전체에 악재라는 식으로 보면 분석이 너무 거칠다.

2012 Long은:

- ASO
- risk-bearing
- HealthSpring / Medicare

를 나눴다.

즉:

**Policy change  
→ 어느 membership에 적용되는가  
→ 누가 claims risk를 부담하는가  
→ MLR/fee earnings에 얼마나 영향  
→ EPS/FCF 영향**

으로 봤다.

실제:
**$47.4 → $87.48, 약 +85%**

### 재사용 원칙

> 규제 headline을 revenue에 곱하지 말고 **실제 위험을 부담하는 profit pool**에 적용한다.

---

# 8. Cigna 2017 — Deal Break 이후 standalone value

Anthem deal이 깨질 가능성이 커졌을 때 중요한 건:

“거래가 깨질까?” 하나가 아니었다.

봐야 하는 식은:

**Standalone earnings value  
+ capital return option  
- breakup/litigation cost**

였다.

실제 약:
**$143~144 → $203**

으로 약 +40%.

핵심은 event가 바뀌어도 standalone business가 싸다는 구조였다.

### 강한 event-driven Long

> **Catalyst 실패에도 standalone value가 충분한 구조**

가 강하다.

---

# 9. Cigna 2019 — Express Scripts M&A를 어떻게 봐야 하나

Express Scripts 인수 후 단순 EPS accretion은 충분하지 않다.

정확한 bridge:

**인수가격  
→ financing cost  
→ synergy  
→ client retention  
→ incremental operating earnings  
→ incremental FCF  
→ debt reduction  
→ acquisition ROIC**

다.

원문은 약 15% EPS CAGR과 2021년 $350을 기대했다.

실제:
- $160
- 2019말 약 $204
- 2021말 약 $230

사업논지는 강하게 맞았지만 $350에는 크게 미달.

### 핵심 오류

> **EPS 성장 성공을 multiple rerating 성공으로 자동 연결**

했다.

시장은:
- PBM regulatory risk
- conglomerate discount
- capital intensity

를 계속 낮은 multiple로 반영할 수 있었다.

---

# 10. Cigna 2021 — 숫자를 맞히고도 horizon을 틀릴 수 있다

2021 Long은:
- Evernorth earnings
- 약 $8bn FCF
- buyback

을 매우 잘 봤다.

하지만 year-end $300 목표는 실패.

2021말 약 $229.63.

그런데 2022말:
**$331.34**

로 목표를 약 1년 늦게 달성했다.

### 여기서 분리할 것

**Business forecast accuracy  
≠ Timing accuracy  
≠ IRR accuracy**

목표가격이 결국 도달했더라도 원래 horizon보다 늦으면 실제 IRR은 달라진다.

---

# 11. Cigna 2022 — Compounder와 SOTP의 함정

2022 아이디어는 10~13% EPS compounder 논지였다.

좋은 부분:

**Organic segment growth  
+ buyback accretion  
→ EPS growth**

나쁜 부분:

**EPS growth  
→ 높은 SOTP multiple**

을 너무 쉽게 붙였다.

실제:
- 약 $279
- 2023말 $299.45
- 약 +7%

1년 $382 목표는 크게 미달.

### 앞으로 분해

**Organic EPS growth  
+ buyback contribution  
+ dividend  
+ multiple change  
= shareholder return**

네 변수를 따로 본다.

---

# 12. UNH 2006 — 탁월한 기업통찰과 실패한 초기 투자

원문의 “보험사가 아니라 healthcare technology/data platform”이라는 시각은 매우 뛰어났다.

나중의 Optum이 이를 강하게 검증했다.

하지만 실제 초기 투자경로:

**$53.73 → 2008말 약 $26.6**

약 -50%.

### 중요한 교훈

> **장기 franchise quality가 단기 valuation floor를 보장하지 않는다.**

2008년에는:
- earnings uncertainty
- multiple compression
- liquidity stress
- policy risk

가 동시에 발생했다.

즉 downside에서:

**Earnings ↓ + Multiple ↓**

가 같이 일어나는 joint-tail을 봐야 한다.

---

# 13. UNH 2007 LEAPS — 같은 회사, 완전히 다른 증권

2007 아이디어는 common이 아니라:

- Jan-2010
- $50 strike
- breakeven 약 $65.70

인 LEAPS가 핵심이었다.

Option payoff는:

**Max(Expiry price - Strike, 0) - Premium**

이다.

장기적으로 UNH가 훌륭한 회사였다는 것은 중요하지 않다.

Expiry 전에 $65.70 이상이어야 했다.

실제 2008말 주가 약 $26.6.

### 결론

> **Long-term business thesis correct ≠ Option trade correct**

Option은 세 가지를 모두 맞혀야 한다.

1. 방향
2. 크기
3. 시간

---

# 14. Managed Care에서 가장 중요한 KPI Tree

## Insurance

**Membership  
→ premium pricing  
→ medical utilization / cost trend  
→ MLR  
→ underwriting earnings**

## ASO

**ASO members  
× admin fee  
→ fee revenue  
- servicing cost  
→ fee earnings**

## PBM / Services

**Clients / scripts / specialty mix  
→ revenue  
→ gross profit / fee earnings  
→ operating earnings**

## Consolidated

**Segment earnings  
- interest / corporate / tax  
→ operating cash flow  
→ FCF  
→ debt / buyback / M&A  
→ diluted shares  
→ FCF/share**

---

# 15. Medical Cost Trend 분석에서 흔한 오류

### 오류 1
“의료비가 8% 오른다.”

이건 투자논지가 아니다.

### 올바른 질문

1. 회사 pricing은 몇 %인가?
2. 어느 book이 risk-bearing인가?
3. ASO에서는 누가 claims를 부담하는가?
4. utilization과 unit cost 중 무엇이 오르는가?
5. reserve development가 어떤가?
6. MLR이 몇 bp 변하는가?
7. EPS sensitivity가 얼마인가?

즉:

> **Medical trend는 EPS sensitivity로 번역해야 투자변수가 된다.**

---

# 16. PBM 규제도 같은 방식으로 본다

“PBM 규제가 강화된다” 역시 너무 넓다.

정확히는:

**Regulation  
→ rebate economics / spread / admin fee  
→ client repricing  
→ specialty / formulary economics  
→ Evernorth / Optum Rx earnings  
→ consolidated EPS/FCF**

로 연결한다.

정책 headline과 실제 profit pool을 분리해야 한다.

---

# 17. EPS Growth를 해부하는 법

Managed care 기업은 buyback이 크기 때문에 EPS만 보면 착시가 생길 수 있다.

예:

**Operating earnings +6%  
Share count -5%  
→ EPS 약 +12%**

라면 headline EPS 12% 중 절반은 capital allocation에서 온다.

따라서:

1. Organic operating earnings growth
2. Interest/tax effect
3. Share-count effect
4. M&A effect

를 분리한다.

---

# 18. Buyback을 평가하는 법

Buyback은 금액 자체가 좋은 것이 아니다.

필요한 조건:

**FCF 지속 가능  
+ leverage 관리 가능  
+ intrinsic value 이하 가격  
+ better reinvestment opportunity 부재**

이다.

추적할 KPI:
- repurchase dollars
- average purchase price
- diluted share count
- debt
- FCF/share

---

# 19. M&A 분석

Express Scripts 같은 deal은:

**EPS accretion**

만 보면 안 된다.

필수 분석:

1. purchase price
2. debt/equity financing
3. synergy
4. customer retention
5. integration expense
6. incremental capex
7. incremental FCF
8. ROIC
9. regulatory risk

### 핵심

> **EPS accretion ≠ Value accretion**

낮은 금리·낮은 target multiple로 EPS는 쉽게 올릴 수 있다.

---

# 20. Batch 016 대표 성공/실패 유형

## 성공 유형 1 — 운영병목을 KPI로 추적

대표:
- CI 2003

## 성공 유형 2 — 규제 headline을 실제 risk pool로 분해

대표:
- CI 2012

## 성공 유형 3 — catalyst 실패에도 standalone이 싼 구조

대표:
- CI 2017

## 부분 성공 유형 — Business 맞음 / multiple 틀림

대표:
- CI 2019
- CI 2021
- CI 2022

## 실패 유형 1 — 장기 quality를 단기 floor로 사용

대표:
- UNH 2006

## 실패 유형 2 — 장기 thesis와 만기 있는 security를 동일시

대표:
- UNH 2007 LEAPS

---

# 21. Batch 016에서 추출되는 V9 원칙

### 원칙 1
**ASO와 risk-bearing insurance를 분리한다.**

### 원칙 2
**Medical trend보다 pricing gap을 본다.**

### 원칙 3
**MLR은 결과변수이므로 원인을 utilization/unit cost/pricing으로 분해한다.**

### 원칙 4
**Regulation을 전체 revenue가 아니라 실제 profit pool에 적용한다.**

### 원칙 5
**EPS growth와 multiple rerating을 분리한다.**

### 원칙 6
**Organic EPS와 buyback EPS를 분리한다.**

### 원칙 7
**M&A accretion은 incremental FCF/ROIC로 검증한다.**

### 원칙 8
**가격 성공과 catalyst 성공을 별도 판정한다.**

### 원칙 9
**Common과 option/LEAPS는 다른 투자다.**

### 원칙 10
**좋은 장기 franchise가 short-term downside floor는 아니다.**

### 원칙 11
**첫 thesis break는 MLR·reserve·retention·cash conversion에서 찾는다.**

### 원칙 12
**당시 알 수 있었던 것과 사후에만 알 수 있는 것을 구분한다.**

---

# 22. 향후 정밀화

추가 보강 가치가 높은 항목:

1. 게시일 exact close
2. 1M / 3M / 6M / 1Y / 3Y / 5Y
3. 목표가 최초 도달일
4. MFE / MAE
5. dividend-adjusted total return
6. 실제 holding IRR
7. CI/UNH MLR quarter series
8. pricing trend vs medical-cost trend
9. ASO/risk membership mix
10. PBM client wins/losses
11. Optum/Evernorth segment margins
12. operating cash flow / adjusted EPS conversion
13. net debt / leverage
14. buyback average price
15. diluted share count
16. organic EPS vs buyback contribution
17. M&A incremental ROIC
18. UNH 2007 LEAPS exact premium / IV / expiry payoff

**이번 Batch부터는 “EPS가 얼마나 성장했는가”보다, 누가 medical risk를 부담하고 그 earnings가 FCF/share와 실제 security payoff로 어떻게 전달됐는지를 우선 기록한다.**
