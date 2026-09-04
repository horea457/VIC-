# Batch 016 — Cigna·UnitedHealth Managed Care 10건

평가기준일: 2024-01-31

분석일: 2026-09-04

대상: Cigna 8건 · UnitedHealth 2건

## 결론부터

이번 배치는 managed care를 **보험업 하나로 뭉개지 않고 ASO fee, risk-bearing insurance, PBM/health services, data/technology platform, 자본배분과 증권경로로 분해**한다.

- **Cigna:** 2003 claims-system turnaround와 2012 ASO/ACA 분석은 사업의 구체적인 operating mechanism을 맞힌 좋은 사례다. 반면 2009는 PBM sale이 실패했는데도 주가 목표가 맞은 '가격 성공·촉매 실패', 2019와 2021은 EPS가 거의 정확했는데 P/E와 timing이 틀린 '사업 성공·valuation 경로 실패'의 전형이다.
- **UnitedHealth:** 2006년 '보험사가 아니라 healthcare technology/data company'라는 통찰은 훗날 Optum 성장으로 매우 강하게 검증됐다. 그러나 $45~60이라는 downside floor와 2007년 2010 LEAPS는 2008 drawdown에서 무너졌다. **장기 기업 통찰과 단기 증권 payoff는 별개**다.

> 데이터 경고: Cigna의 2000-09-21, 2009-07-13, 2017-02-20, 2021-06-03, 2022-09-25 아이디어는 원 SQL `is_short=true`지만 본문은 Long 또는 Long 진입대기 논지다. 원본 flag는 감사추적용으로 보존하고 research 방향을 Long으로 교정한다. 2000년 글은 명확한 체결가 없이 $70 이하를 기다리는 watchlist형 Long이라 방향·성과 신뢰도를 한 단계 낮게 둔다.

---

# THE CIGNA GROUP (CI) — 기업과 비즈니스

## 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

## 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2000-09-21 | Short | Long | ASO mix·health-reform overreaction·$70 이하 진입대기 Long | 깔끔한 체결가격이 없는 watchlist형 Long. 주가는 2000년 말 약 $132까지 올랐지만 2002년 Cigna 운영문제로 약 $41 수준까지 급락했다. | 구조적 통찰 일부 적중·투자논지 미완성 |
| 2003-12-30 | Long | Long | Claims-system turnaround·MLR 정상화·$80 target Long | 약 $57.5→2004년 말 약 $81.57, 약 +42%. 12개월 $80 목표를 거의 정확히 달성. | 매우 성공 |
| 2009-07-13 | Short | Long | PBM 매각 value-unlock·20~40% event-driven Long | 약 $24.4→2009년 말 약 $35.27, 약 +45%. 목표범위 $29~34는 빠르게 달성됐지만 PBM 매각은 발생하지 않음. | 가격 성공·핵심 촉매 실패 |
| 2012-09-23 | Long | Long | ASO·ACA downside 제한·HealthSpring·$61 base Long | 약 $47.4→2013년 말 약 $87.48, 약 +85%. Base $61을 크게 초과. | 매우 성공 |
| 2017-02-20 | Short | Long | Anthem deal break·$7bn buyback·$167 standalone Long | 약 $143~144→2017년 말 약 $203, +40% 안팎. 작성자는 약 1년 뒤 +32%로 청산했다고 후속 글에서 언급. | 매우 성공 |
| 2019-03-28 | Long | Long | Express Scripts integration·15% EPS CAGR·$350 2021 Long | $160→2019말 약 $204(+28%), 2021말 약 $230(+44%). 2021 target $350은 크게 미달. | 사업논지 강한 적중·multiple thesis 실패 |
| 2021-06-03 | Short | Long | Evernorth 54% earnings·$8bn FCF/buyback·$300 year-end Long | 2021말 약 $229.63로 단기 -10% 안팎, $300 target 실패. 2022말 약 $331.34로 target은 약 1년 늦게 달성. | 운영예측 매우 정확·timing/multiple 오류 |
| 2022-09-25 | Short | Long | 10~13% EPS compounder·Evernorth/Cigna SOTP·$382 Long | 약 $279→2023말 약 $299.45, +7% 안팎. 1년 $382 target에는 크게 미달. | 사업·buyback 부분 적중·SOTP/multiple 실패 |

---

<!-- idea:48fc7da8-6910-4689-b430-f6779c5b9798 -->
## 1. 2000-09-21 — ASO mix·health-reform overreaction·$70 이하 진입대기 Long

### 결론부터

**종합판정: 구조적 통찰 일부 적중·투자논지 미완성.** 이 글은 premium accounting 때문에 작아 보이는 ASO fee를 premium equivalent로 환산해 경제적 위험노출을 다시 본 점이 훌륭했다. 그러나 '건강개혁 위험이 작다'는 한 가지 반론에 집중해 claims operations·service quality·medical-cost visibility·runoff reinsurance 같은 훨씬 가까운 리스크를 거의 모델링하지 않았다. 또한 실제 매수가가 정해지지 않아 투자성과 판정도 애매하다.

**주가·증권 결과:** 깔끔한 체결가격이 없는 watchlist형 Long. 주가는 2000년 말 약 $132까지 올랐지만 2002년 Cigna 운영문제로 약 $41 수준까지 급락했다.

**Thesis / Process 점수:** 7.4 / 7.5

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

### 5. 밸류에이션과 기대수익의 연결

2001E EPS $7.45 × 12x = $89.40 fair value. 단 작성자는 당시 가격 매수를 권하지 않고 healthcare-reform 공포가 $70 이하 진입점을 만들기를 기다렸다. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. ASO risk mix — 적중 · 논지 비중 18%

**당시 주장**

premium-equivalent로 보면 Cigna 의료사업의 큰 부분이 employer-funded ASO라 직접 claims risk가 낮다.

**당시 근거**

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

**이 주장이 성립하려면**

고용주가 claims를 계속 부담하고 fee economics가 안정

**사전 반증조건**

ASO 고객 이탈·admin cost 급증

**실제 결과**

ASO가 risk-bearing 보험보다 underwriting 위험이 낮다는 구조는 맞았다.

**정량적 괴리**

ASO 경제적 비중 / premium-equivalent 기준 GLDH 약 60% / 개혁·underwriting 위험 완충 / ASO 자체는 fee-based 구조 유지

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

ASO risk mix 가설은 'ASO 고객 이탈·admin cost 급증'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Healthcare reform exposure — 적중 · 논지 비중 18%

**당시 주장**

전체 continuing income 중 개혁으로 직접 위험한 부분은 25% 미만이다.

**당시 근거**

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

**이 주장이 성립하려면**

개혁이 risk premium·HMO 영역에 집중

**사전 반증조건**

정책이 ASO fee·employer coverage까지 구조적으로 훼손

**실제 결과**

정책 자체는 이후 Cigna 붕괴의 직접원인이 아니었다.

**정량적 괴리**

2001E EPS / $7.45 / 12% 성장 / 2002 전후 운영문제로 earnings path 훼손

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Healthcare reform exposure 가설은 '정책이 ASO fee·employer coverage까지 구조적으로 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Earnings quality — 실패 · 논지 비중 16%

**당시 주장**

$6.66→$7.45 EPS 성장과 강한 cash/balance sheet가 하방을 지지한다.

**당시 근거**

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

**이 주장이 성립하려면**

claims operations와 reserve quality가 안정

**사전 반증조건**

medical cost read·claims system이 훼손

**실제 결과**

2001~02 운영문제가 earnings를 크게 훼손했다.

**정량적 괴리**

진입가격 / $70 이하 대기 / 공포 진입 / 명확한 체결가격 없음

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Earnings quality 가설은 'medical cost read·claims system이 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Claims operations — 실패 · 논지 비중 16%

**당시 주장**

운영시스템은 thesis의 주요 위험이 아니라고 암묵적으로 가정했다.

**당시 근거**

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

**이 주장이 성립하려면**

claims adjudication·provider relations 안정

**사전 반증조건**

system conversion으로 service와 pricing data 훼손

**실제 결과**

실제로 claims-system 문제가 핵심 실패기제가 됐다.

**정량적 괴리**

중기 주가 / 글 당시 약 $90 추정 / 하방 제한 기대 / 2002 약 $41까지 급락

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Claims operations 가설은 'system conversion으로 service와 pricing data 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. Buyback·balance sheet — 부분 실패 · 논지 비중 16%

**당시 주장**

cash와 buyback은 undervaluation에서 주당가치를 보호한다.

**당시 근거**

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

**이 주장이 성립하려면**

현금이 operating losses·charges에 소모되지 않음

**사전 반증조건**

capital이 remediation·charges에 흡수

**실제 결과**

buyback만으로 운영악화를 상쇄하지 못했다.

**정량적 괴리**

깔끔한 체결가격이 없는 watchlist형 Long. 주가는 2000년 말 약 $132까지 올랐지만 2002년 Cigna 운영문제로 약 $41 수준까지 급락했다.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Buyback·balance sheet 가설은 'capital이 remediation·charges에 흡수'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. Entry discipline — 부분 적중 · 논지 비중 16%

**당시 주장**

$89 fair value보다 충분히 싼 $70 이하에서만 사면 손익비가 좋아진다.

**당시 근거**

Cigna를 단순 HMO로 보면 안 되며 GLDH의 premium-equivalent 기준으로 ASO가 약 60%를 차지하고, 전체 continuing income 중 healthcare reform에 직접 underwriting risk를 지는 부분은 25% 미만이라고 주장했다. 2000E EPS $6.66, 2001E $7.45(+12%), cash $2.2bn, long-term debt $1.3bn, 1Q00 $521m buyback과 $448m CFO를 근거로 재무여력도 강조했다. Gore의 healthcare 공약과 HMO 소송 공포가 추가 하락을 만들면 $70 이하에서 사겠다는 구조였다.

**이 주장이 성립하려면**

실제 공포가격이 operating impairment가 아닌 sentiment 때문

**사전 반증조건**

가격하락이 fundamentals 훼손을 반영

**실제 결과**

진입 대기는 좋은 규율이었지만 $70 하락이 오면 원인을 재검증해야 했다.

**정량적 괴리**

깔끔한 체결가격이 없는 watchlist형 Long. 주가는 2000년 말 약 $132까지 올랐지만 2002년 Cigna 운영문제로 약 $41 수준까지 급락했다.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Entry discipline 가설은 '가격하락이 fundamentals 훼손을 반영'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

정책위험보다 훨씬 중요한 operational risk가 뒤늦게 현실화됐다. 2001~02 claims-system transformation이 provider relationship과 customer satisfaction을 훼손했고 medical cost를 제대로 읽지 못하게 하면서 membership loss와 MLR 악화로 이어졌다. 2002년 10월 회사는 의료비·비용문제로 실적경고를 내며 하루 38% 급락했다. ASO가 underwriting risk를 줄인다는 원리는 맞았지만 회사 전체 이익을 보호하는 충분조건은 아니었다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 깔끔한 체결가격이 없는 watchlist형 Long. 주가는 2000년 말 약 $132까지 올랐지만 2002년 Cigna 운영문제로 약 $41 수준까지 급락했다. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 premium accounting 때문에 작아 보이는 ASO fee를 premium equivalent로 환산해 경제적 위험노출을 다시 본 점이 훌륭했다. 그러나 '건강개혁 위험이 작다'는 한 가지 반론에 집중해 claims operations·service quality·medical-cost visibility·runoff reinsurance 같은 훨씬 가까운 리스크를 거의 모델링하지 않았다. 또한 실제 매수가가 정해지지 않아 투자성과 판정도 애매하다.

### 9. 최초 검증·반증 신호와 회피 가능성

2002-10-25 — Cigna가 비용과 higher medical claims로 earnings target을 크게 낮추고 주가가 하루 약 38% 급락. 정책보다 운영·의료비 관리가 핵심 리스크였음이 드러났다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 높음. 2001~02 claims conversion과 customer dissatisfaction이 공개되면서 healthcare-reform exposure만으로 하방을 설명하는 논지를 재작성할 수 있었다.

### 10. 최종 판정·반사실·재사용 교훈

구조적 통찰 일부 적중·투자논지 미완성. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| ASO 경제적 비중 | premium-equivalent 기준 GLDH 약 60% | 개혁·underwriting 위험 완충 | ASO 자체는 fee-based 구조 유지 | 구조 적중 |
| 2001E EPS | $7.45 | 12% 성장 | 2002 전후 운영문제로 earnings path 훼손 | 실패 |
| 진입가격 | $70 이하 대기 | 공포 진입 | 명확한 체결가격 없음 | 미판정 |
| 중기 주가 | 글 당시 약 $90 추정 | 하방 제한 기대 | 2002 약 $41까지 급락 | 하방 분석 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2000-09-21 | VIC 아이디어 게시 | ASO mix·health-reform overreaction·$70 이하 진입대기 Long |
| 2002-10-25 | 최초 핵심 검증·반증 신호 | Cigna가 비용과 higher medical claims로 earnings target을 크게 낮추고 주가가 하루 약 38% 급락. 정책보다 운영·의료비 관리가 핵심 리스크였음이 드러났다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 깔끔한 체결가격이 없는 watchlist형 Long. 주가는 2000년 말 약 $132까지 올랐지만 2002년 Cigna 운영문제로 약 $41 수준까지 급락했다. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating causal chain은 대체로 맞았으나 price target의 multiple·timing은 별도 관리 필요
- **최초 검증·반증 신호:** 2002-10-25 — Cigna가 비용과 higher medical claims로 earnings target을 크게 낮추고 주가가 하루 약 38% 급락. 정책보다 운영·의료비 관리가 핵심 리스크였음이 드러났다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 높음. 2001~02 claims conversion과 customer dissatisfaction이 공개되면서 healthcare-reform exposure만으로 하방을 설명하는 논지를 재작성할 수 있었다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- [1. VIC CI 2000-09-21 원문](https://www.valueinvestorsclub.com/idea/CIGNA_Corporation/1617026210) — Value Investors Club, 2000-09-21. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:446e42f4-4029-4919-9976-0e9b0057609d -->
## 2. 2003-12-30 — Claims-system turnaround·MLR 정상화·$80 target Long

### 결론부터

**종합판정: 매우 성공.** 이 글은 실패 원인을 'managed care가 나쁜 산업'이라고 뭉개지 않고 claims-system → provider/customer dissatisfaction → medical-cost blindness → mispricing → MLR 상승으로 구체적 causal chain을 만들었다. 또한 membership을 여전히 크게 감소시킨 상태에서도 margin 회복만으로 valuation을 만들었다. 가장 좋은 turnaround 분석에 가깝다.

**주가·증권 결과:** 약 $57.5→2004년 말 약 $81.57, 약 +42%. 12개월 $80 목표를 거의 정확히 달성.

**Thesis / Process 점수:** 9.2 / 9

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

### 5. 밸류에이션과 기대수익의 연결

2003 EPS 약 $5.50, 2004 약 $5.60, 2005 약 $7.00. 2005 EPS × 12x = 약 $80. SOTP도 약 $80대 중반을 지지. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Claims-system repair — 적중 · 논지 비중 18%

**당시 주장**

새 claims systems가 안정되며 auto-adjudication과 medical-cost visibility가 회복된다.

**당시 근거**

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

**이 주장이 성립하려면**

migration·system uptime·provider payment 정상

**사전 반증조건**

claims backlog·provider complaints 재악화

**실제 결과**

운영정상화와 주가회복이 동행했다.

**정량적 괴리**

Membership / 2002→03 약 -11% / 2004 -10%, 2005 -4% / 감소를 감수하고도 turnaround 진행

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Claims-system repair 가설은 'claims backlog·provider complaints 재악화'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. MLR normalization — 적중 · 논지 비중 18%

**당시 주장**

claims data와 pricing 회복으로 MLR이 2004 200bp, 2005 추가 100bp 개선된다.

**당시 근거**

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

**이 주장이 성립하려면**

medical trend보다 pricing·care management가 개선

**사전 반증조건**

MLR 90%대 고착

**실제 결과**

수익성이 회복되며 turnaround가 현실화됐다.

**정량적 괴리**

MLR / 2Q03 90.4% / 2004 -200bp, 2005 -100bp / 운영정상화로 수익성 회복

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

MLR normalization 가설은 'MLR 90%대 고착'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Membership lag — 적중 · 논지 비중 16%

**당시 주장**

서비스 평판 회복은 느려 2004에도 membership이 10% 줄어도 thesis는 성립한다.

**당시 근거**

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

**이 주장이 성립하려면**

margin 개선이 volume 감소를 상쇄

**사전 반증조건**

membership loss가 예상보다 크고 지속

**실제 결과**

보수적 membership 가정 덕분에 thesis가 volume 반등에 의존하지 않았다.

**정량적 괴리**

2005E EPS / 약 $7 / 12x 적용 / earnings recovery 진행

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Membership lag 가설은 'membership loss가 예상보다 크고 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Runoff reinsurance — 적중 · 논지 비중 16%

**당시 주장**

2002 $1.1bn·2003 $230m charge 뒤 큰 추가 charge 가능성은 낮다.

**당시 근거**

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

**이 주장이 성립하려면**

hedging·runoff 관리 안정

**사전 반증조건**

추가 대규모 reserve charge

**실제 결과**

핵심 thesis를 깨는 대형 추가 charge는 나타나지 않았다.

**정량적 괴리**

주가 / 약 $57.5 / 12개월 $80 / 2004말 $81.57

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Runoff reinsurance 가설은 '추가 대규모 reserve charge'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. EPS leverage — 적중 · 논지 비중 16%

**당시 주장**

MLR 100bp 개선당 약 $0.80 EPS sensitivity가 turnaround를 증폭한다.

**당시 근거**

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

**이 주장이 성립하려면**

membership·SG&A가 동시에 악화되지 않음

**사전 반증조건**

MLR 개선에도 EPS 정체

**실제 결과**

earnings와 valuation이 회복했다.

**정량적 괴리**

약 $57.5→2004년 말 약 $81.57, 약 +42%. 12개월 $80 목표를 거의 정확히 달성.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

EPS leverage 가설은 'MLR 개선에도 EPS 정체'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $80 valuation — 강한 적중 · 논지 비중 16%

**당시 주장**

2005 약 $7 EPS에 12x면 $80이 가능하다.

**당시 근거**

2001년 시작된 claims-system 통합 실패가 provider relationship·customer satisfaction·medical-cost visibility를 훼손해 2002→03 membership이 약 11% 줄고 2Q03 MLR이 90.4%까지 올랐지만, 두 새 시스템에 12m 중 약 7m members가 이미 올라갔고 auto-adjudication도 60~70%로 old systems의 <40%보다 좋아졌다고 봤다. 2004 membership -10%, 2005 -4%라는 보수적 가정에도 MLR 200bp+100bp 개선이면 2005 EPS 약 $7, 12x에서 $80이라고 계산했다.

**이 주장이 성립하려면**

industry-normal multiple 회복

**사전 반증조건**

turnaround discount 지속

**실제 결과**

약 12개월 만에 $80선을 달성했다.

**정량적 괴리**

약 $57.5→2004년 말 약 $81.57, 약 +42%. 12개월 $80 목표를 거의 정확히 달성.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

$80 valuation 가설은 'turnaround discount 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

turnaround가 실제로 진행되면서 주가는 2004년 말 약 $81.57까지 올라 12개월 목표를 달성했고 2005년 말에는 $100을 크게 웃돌았다. 핵심은 membership recovery 자체보다 claims operations 정상화와 medical-cost pricing visibility 회복이었다. 원문이 두려워한 추가 대규모 runoff reinsurance charge도 thesis를 깨는 규모로 재발하지 않았다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 약 $57.5→2004년 말 약 $81.57, 약 +42%. 12개월 $80 목표를 거의 정확히 달성. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 실패 원인을 'managed care가 나쁜 산업'이라고 뭉개지 않고 claims-system → provider/customer dissatisfaction → medical-cost blindness → mispricing → MLR 상승으로 구체적 causal chain을 만들었다. 또한 membership을 여전히 크게 감소시킨 상태에서도 margin 회복만으로 valuation을 만들었다. 가장 좋은 turnaround 분석에 가깝다.

### 9. 최초 검증·반증 신호와 회피 가능성

2004-12-31 — 2004년 실적과 주가가 개선되며 claims system·MLR 정상화 논지가 확인되고 $80 목표가 12개월 안에 실현됐다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 해당 없음에 가깝다. 실제 결과가 논지와 일치했다. 다만 MLR 100bp당 EPS $0.80이라는 sensitivity는 향후에도 membership·mix 변화와 함께 재계산해야 한다.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Membership | 2002→03 약 -11% | 2004 -10%, 2005 -4% | 감소를 감수하고도 turnaround 진행 | 보수적 |
| MLR | 2Q03 90.4% | 2004 -200bp, 2005 -100bp | 운영정상화로 수익성 회복 | 적중 |
| 2005E EPS | 약 $7 | 12x 적용 | earnings recovery 진행 | 방향 적중 |
| 주가 | 약 $57.5 | 12개월 $80 | 2004말 $81.57 | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2003-12-30 | VIC 아이디어 게시 | Claims-system turnaround·MLR 정상화·$80 target Long |
| 2004-12-31 | 최초 핵심 검증·반증 신호 | 2004년 실적과 주가가 개선되며 claims system·MLR 정상화 논지가 확인되고 $80 목표가 12개월 안에 실현됐다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 약 $57.5→2004년 말 약 $81.57, 약 +42%. 12개월 $80 목표를 거의 정확히 달성. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating causal chain은 대체로 맞았으나 price target의 multiple·timing은 별도 관리 필요
- **최초 검증·반증 신호:** 2004-12-31 — 2004년 실적과 주가가 개선되며 claims system·MLR 정상화 논지가 확인되고 $80 목표가 12개월 안에 실현됐다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 해당 없음에 가깝다. 실제 결과가 논지와 일치했다. 다만 MLR 100bp당 EPS $0.80이라는 sensitivity는 향후에도 membership·mix 변화와 함께 재계산해야 한다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- [1. VIC CI 2003-12-30 원문](https://www.valueinvestorsclub.com/idea/Cigna/8013464207) — Value Investors Club, 2003-12-30. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:3f7e9121-7113-4612-aef7-7c2379ef08e3 -->
## 3. 2009-07-13 — PBM 매각 value-unlock·20~40% event-driven Long

### 결론부터

**종합판정: 가격 성공·핵심 촉매 실패.** 이 사례는 사후분석에서 매우 중요하다. 목표가를 맞혔지만 원인귀속은 틀렸다. PBM valuation gap과 balance-sheet overhang을 잘 봤지만 '회사가 매각할 것'이라는 catalyst probability를 과대평가했다. 투자성과와 thesis accuracy를 분리하지 않으면 false learning을 만들 수 있다.

**주가·증권 결과:** 약 $24.4→2009년 말 약 $35.27, 약 +45%. 목표범위 $29~34는 빠르게 달성됐지만 PBM 매각은 발생하지 않음.

**Thesis / Process 점수:** 7.4 / 7.5

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

PBM 매각 후 ex-PBM EPS 약 $3.40. Peer 8.6x 적용 시 $29.24(+20%), historical 10x 적용 시 $34(+40%). PBM sale proceeds는 balance-sheet overhang 완화에 사용될 것으로 예상. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. PBM sale — 실패 · 논지 비중 18%

**당시 주장**

Cigna가 PBM을 매각해 hidden value를 실현한다.

**당시 근거**

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

**이 주장이 성립하려면**

실제 buyer·process·management 의지 존재

**사전 반증조건**

PBM을 계속 운영

**실제 결과**

PBM은 매각되지 않았다.

**정량적 괴리**

주가 / 약 $24.4 / $29.24~$34 / 2009말 $35.27

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

PBM sale 가설은 'PBM을 계속 운영'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. PBM valuation gap — 부분 적중 · 논지 비중 18%

**당시 주장**

독립 PBM의 높은 multiple이 Cigna PBM value를 보여준다.

**당시 근거**

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

**이 주장이 성립하려면**

사업 quality·growth가 public PBM과 유사

**사전 반증조건**

PBM economics가 구조적으로 열위

**실제 결과**

valuation gap은 존재했지만 transaction으로 crystallize되진 않았다.

**정량적 괴리**

PBM sale / 검토 중 / $1.3~1.5bn 매각 / 매각하지 않음

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

PBM valuation gap 가설은 'PBM economics가 구조적으로 열위'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Balance-sheet repair — 결과 적중·경로 실패 · 논지 비중 16%

**당시 주장**

매각대금이 VA·pension·CRE overhang을 줄여 equity issuance 위험을 낮춘다.

**당시 근거**

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

**이 주장이 성립하려면**

proceeds가 실제 debt/capital에 사용

**사전 반증조건**

매각 무산·capital shortfall 확대

**실제 결과**

매각 없이도 금융환경과 earnings 회복으로 우려가 완화됐다.

**정량적 괴리**

Ex-PBM EPS / 약 $3.40 / 8.6~10x / 기업실적 회복으로 rerating

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Balance-sheet repair 가설은 '매각 무산·capital shortfall 확대'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Reform exposure — 적중 · 논지 비중 16%

**당시 주장**

ASO 중심 Cigna는 Obama reform downside가 peers보다 작다.

**당시 근거**

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

**이 주장이 성립하려면**

employer-sponsored ASO 유지

**사전 반증조건**

정책이 ASO economics까지 훼손

**실제 결과**

reform이 단기 catastrophic loss를 만들지는 않았다.

**정량적 괴리**

Balance-sheet overhang / VA·pension·CRE 우려 / sale proceeds로 완화 / 매각 없이도 우려 완화

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Reform exposure 가설은 '정책이 ASO economics까지 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. $29~34 valuation — 가격 적중 · 논지 비중 16%

**당시 주장**

ex-PBM $3.40 EPS에 8.6~10x면 20~40% upside다.

**당시 근거**

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

**이 주장이 성립하려면**

earnings 유지와 multiple 회복

**사전 반증조건**

EPS 하향

**실제 결과**

주가가 2009말 $35를 넘어섰다.

**정량적 괴리**

약 $24.4→2009년 말 약 $35.27, 약 +45%. 목표범위 $29~34는 빠르게 달성됐지만 PBM 매각은 발생하지 않음.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

$29~34 valuation 가설은 'EPS 하향'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. Catalyst attribution — 실패·핵심 교훈 · 논지 비중 16%

**당시 주장**

목표가 달성은 PBM value-unlock이 원인일 것이라는 암묵적 전제.

**당시 근거**

Cigna가 PBM을 매각 검토 중이고 독립 PBM은 평균 17.6x 2009E EPS인데 Cigna 전체는 6.5x라 매각이 hidden value를 드러낼 것으로 봤다. 약 $1.3~1.5bn proceeds로 variable annuity, underfunded pension, CRE와 equity issuance 우려를 줄일 수 있고, ex-PBM earnings에 peer/historical multiple을 붙이면 $29~34가 가능하다고 계산했다. Obama healthcare reform에도 ASO 중심이라 영향이 제한적이라고 주장했다.

**이 주장이 성립하려면**

PBM sale이 실제 주가 재평가를 촉발

**사전 반증조건**

sale 없이 주가 상승

**실제 결과**

실제로 sale 없이 목표가를 달성했다.

**정량적 괴리**

약 $24.4→2009년 말 약 $35.27, 약 +45%. 목표범위 $29~34는 빠르게 달성됐지만 PBM 매각은 발생하지 않음.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Catalyst attribution 가설은 'sale 없이 주가 상승'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

주가는 2009년 말 약 $35로 목표를 초과했지만 Cigna는 PBM을 매각하지 않았다. 2010 10-K에서도 Cigna Pharmacy Management를 계속 운영했다. 즉 '가격 목표 달성=촉매 성공'이 아니다. 금융시장 정상화, capital concerns 완화, earnings 회복 등 다른 요인이 더 중요했다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 약 $24.4→2009년 말 약 $35.27, 약 +45%. 목표범위 $29~34는 빠르게 달성됐지만 PBM 매각은 발생하지 않음. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 사례는 사후분석에서 매우 중요하다. 목표가를 맞혔지만 원인귀속은 틀렸다. PBM valuation gap과 balance-sheet overhang을 잘 봤지만 '회사가 매각할 것'이라는 catalyst probability를 과대평가했다. 투자성과와 thesis accuracy를 분리하지 않으면 false learning을 만들 수 있다.

### 9. 최초 검증·반증 신호와 회피 가능성

2010-02-25 — 2010 10-K에서 Cigna Pharmacy Management를 계속 영위하는 것이 확인되며 PBM sale catalyst가 실현되지 않았음이 명확해졌다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 중간. 가격은 성공했지만 catalyst가 발생하지 않는 시점부터 포지션을 'PBM event-driven'이 아니라 earnings/balance-sheet recovery 투자로 재분류했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

가격 성공·핵심 촉매 실패. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | 약 $24.4 | $29.24~$34 | 2009말 $35.27 | 가격 성공 |
| PBM sale | 검토 중 | $1.3~1.5bn 매각 | 매각하지 않음 | 촉매 실패 |
| Ex-PBM EPS | 약 $3.40 | 8.6~10x | 기업실적 회복으로 rerating | 방향 부분 |
| Balance-sheet overhang | VA·pension·CRE 우려 | sale proceeds로 완화 | 매각 없이도 우려 완화 | 원인 오판 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2009-07-13 | VIC 아이디어 게시 | PBM 매각 value-unlock·20~40% event-driven Long |
| 2010-02-25 | 최초 핵심 검증·반증 신호 | 2010 10-K에서 Cigna Pharmacy Management를 계속 영위하는 것이 확인되며 PBM sale catalyst가 실현되지 않았음이 명확해졌다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 약 $24.4→2009년 말 약 $35.27, 약 +45%. 목표범위 $29~34는 빠르게 달성됐지만 PBM 매각은 발생하지 않음. |

### Failure / Success Anatomy

- **근본 오류:** operating earnings와 catalyst·multiple의 독립성을 충분히 분리하지 않음
- **최초 검증·반증 신호:** 2010-02-25 — 2010 10-K에서 Cigna Pharmacy Management를 계속 영위하는 것이 확인되며 PBM sale catalyst가 실현되지 않았음이 명확해졌다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 중간. 가격은 성공했지만 catalyst가 발생하지 않는 시점부터 포지션을 'PBM event-driven'이 아니라 earnings/balance-sheet recovery 투자로 재분류했어야 한다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- 1. VIC CI 2009-07-13 원문 — Value Investors Club, 2009-07-13. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:86779ba9-ab75-4499-9215-04f04dcfbaf3 -->
## 4. 2012-09-23 — ASO·ACA downside 제한·HealthSpring·$61 base Long

### 결론부터

**종합판정: 매우 성공.** ACA를 'insurer에 좋다/나쁘다'가 아니라 ASO fee business, risk commercial, MA, insurer tax로 분해한 것이 핵심이었다. 대선 결과는 틀렸지만 downside가 제한적이었던 이유는 구조적 business mix였다. 정치 catalyst보다 segment economics가 더 재사용 가능한 insight다.

**주가·증권 결과:** 약 $47.4→2013년 말 약 $87.48, 약 +85%. Base $61을 크게 초과.

**Thesis / Process 점수:** 9.2 / 9

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

### 5. 밸류에이션과 기대수익의 연결

2013 consensus EPS $6.16에 당시 약 7.7x. Bear $44, base 10x≈$62, bull $76. 세 시나리오 equal-weight value 약 $61. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. ASO protection — 적중 · 논지 비중 18%

**당시 주장**

80%+ ASO customer mix가 insurer tax·claims risk를 완충한다.

**당시 근거**

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

**이 주장이 성립하려면**

employer self-funding 유지

**사전 반증조건**

ASO migration reversal·fee pressure

**실제 결과**

Cigna earnings가 ACA transition에서 상대적으로 견고했다.

**정량적 괴리**

2013E EPS / $6.16 / 유지/성장 / earnings franchise 유지

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

ASO protection 가설은 'ASO migration reversal·fee pressure'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Commercial risk exposure — 적중 · 논지 비중 18%

**당시 주장**

실제 risk-bearing commercial earnings가 약 25% EBIT에 불과하다.

**당시 근거**

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

**이 주장이 성립하려면**

segment mix가 안정

**사전 반증조건**

risk book loss가 그룹 전체를 훼손

**실제 결과**

그룹 downside가 bear case보다 작았다.

**정량적 괴리**

Valuation / 7.7x 2013E / base 10x≈$62 / 2013말 $87.48

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Commercial risk exposure 가설은 'risk book loss가 그룹 전체를 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. HealthSpring — 적중 · 논지 비중 16%

**당시 주장**

HealthSpring 인수가 Medicare Advantage 성장축을 추가한다.

**당시 근거**

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

**이 주장이 성립하려면**

MA reimbursement와 integration 양호

**사전 반증조건**

MA cuts·integration 실패

**실제 결과**

HealthSpring은 Cigna 정부사업 기반을 확대했다.

**정량적 괴리**

ASO 비중 / U.S. medical 80%+ / ACA downside 완충 / 사업 안정성 유지

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

HealthSpring 가설은 'MA cuts·integration 실패'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. ACA tax/regulation — 적중 · 논지 비중 16%

**당시 주장**

ACA 비용은 peers보다 Cigna에 덜 불리하다.

**당시 근거**

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

**이 주장이 성립하려면**

ASO exemption·pricing pass-through

**사전 반증조건**

세금/benefit rule이 margin을 크게 훼손

**실제 결과**

catastrophic margin hit는 나타나지 않았다.

**정량적 괴리**

정치 catalyst / Romney 가능성 / 규제 완화 upside / Obama 재선

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

ACA tax/regulation 가설은 '세금/benefit rule이 margin을 크게 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. Political catalyst — 실패 · 논지 비중 16%

**당시 주장**

대선 결과가 sector multiple을 개선할 수 있다.

**당시 근거**

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

**이 주장이 성립하려면**

Romney 승리 또는 규제완화

**사전 반증조건**

Obama 재선

**실제 결과**

Obama 재선으로 catalyst는 실패했다.

**정량적 괴리**

약 $47.4→2013년 말 약 $87.48, 약 +85%. Base $61을 크게 초과.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Political catalyst 가설은 'Obama 재선'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $61 valuation — 강한 적중 · 논지 비중 16%

**당시 주장**

7.7x에서 10x 정상화만으로 $61 부근 가치가 있다.

**당시 근거**

ACA implementation과 대선 불확실성 때문에 managed-care multiple이 눌렸지만 Cigna는 commercial health customers의 80%+가 ASO이고 commercial risk earnings는 전체 EBIT의 약 25%로 peers보다 직접 underwriting exposure가 낮다고 봤다. Insurer tax도 ASO에는 직접 적용되지 않는다고 보았고, 2012 인수한 HealthSpring의 Medicare Advantage 성장과 runoff divestiture/PBM monetization을 추가 upside로 제시했다.

**이 주장이 성립하려면**

EPS 유지·multiple 정상화

**사전 반증조건**

EPS decline

**실제 결과**

2013말 $87로 목표를 크게 초과했다.

**정량적 괴리**

약 $47.4→2013년 말 약 $87.48, 약 +85%. Base $61을 크게 초과.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

$61 valuation 가설은 'EPS decline'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

Obama가 재선되어 원문의 정치적 bull catalyst는 실패했지만 Cigna earnings와 MA/ASO franchise는 견고했다. HealthSpring은 2012년 약 $3.8bn에 인수되어 정부사업 footprint를 키웠고, 주가는 2013년 말 약 $87로 base와 bull case를 모두 넘어섰다. 즉 정책경로를 맞힌 것이 아니라 business mix의 방어력을 맞혔다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 약 $47.4→2013년 말 약 $87.48, 약 +85%. Base $61을 크게 초과. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

ACA를 'insurer에 좋다/나쁘다'가 아니라 ASO fee business, risk commercial, MA, insurer tax로 분해한 것이 핵심이었다. 대선 결과는 틀렸지만 downside가 제한적이었던 이유는 구조적 business mix였다. 정치 catalyst보다 segment economics가 더 재사용 가능한 insight다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-11-06 — Obama 재선으로 Romney 기반 정책 bull case는 즉시 사라졌지만 Cigna의 ASO 중심 사업논지는 유지됐다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 해당 없음. 정치 catalyst 실패 후에도 ASO·earnings와 valuation이 살아 있어 Long thesis를 유지할 근거가 있었다.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2013E EPS | $6.16 | 유지/성장 | earnings franchise 유지 | 적중 |
| Valuation | 7.7x 2013E | base 10x≈$62 | 2013말 $87.48 | 강한 rerating |
| ASO 비중 | U.S. medical 80%+ | ACA downside 완충 | 사업 안정성 유지 | 적중 |
| 정치 catalyst | Romney 가능성 | 규제 완화 upside | Obama 재선 | 실패·비핵심 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2012-09-23 | VIC 아이디어 게시 | ASO·ACA downside 제한·HealthSpring·$61 base Long |
| 2012-11-06 | 최초 핵심 검증·반증 신호 | Obama 재선으로 Romney 기반 정책 bull case는 즉시 사라졌지만 Cigna의 ASO 중심 사업논지는 유지됐다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 약 $47.4→2013년 말 약 $87.48, 약 +85%. Base $61을 크게 초과. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating causal chain은 대체로 맞았으나 price target의 multiple·timing은 별도 관리 필요
- **최초 검증·반증 신호:** 2012-11-06 — Obama 재선으로 Romney 기반 정책 bull case는 즉시 사라졌지만 Cigna의 ASO 중심 사업논지는 유지됐다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 해당 없음. 정치 catalyst 실패 후에도 ASO·earnings와 valuation이 살아 있어 Long thesis를 유지할 근거가 있었다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- 1. VIC CI 2012-09-23 원문 — Value Investors Club, 2012-09-23. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:3c6961b2-d8d4-4215-af42-6a9f1fd9507e -->
## 5. 2017-02-20 — Anthem deal break·$7bn buyback·$167 standalone Long

### 결론부터

**종합판정: 매우 성공.** 이 글은 merger arbitrage를 'deal이 될까'에만 걸지 않고 deal/no-deal 두 상태에서 모두 equity value를 계산한 점이 좋았다. 특히 blocked deal 후 idle capital이 buyback으로 바뀌는 capital-allocation path를 핵심으로 봤다. Breakup fee에 대한 기대는 지나치게 단순했지만 thesis의 필요조건이 아니었다.

**주가·증권 결과:** 약 $143~144→2017년 말 약 $203, +40% 안팎. 작성자는 약 1년 뒤 +32%로 청산했다고 후속 글에서 언급.

**Thesis / Process 점수:** 9.2 / 9

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

### 5. 밸류에이션과 기대수익의 연결

Deal close 5% 확률: $185.96(+29.5%). 95% stand-alone: $7bn buyback, 2018 EPS $11.92 × 14x = $167(+16%). Breakup fee·M&A는 추가 upside. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Anthem block — 적중 · 논지 비중 18%

**당시 주장**

Anthem-Cigna 거래는 사실상 무산된다.

**당시 근거**

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

**이 주장이 성립하려면**

항소가 구조적 antitrust 문제를 뒤집지 못함

**사전 반증조건**

항소승소·deal close

**실제 결과**

거래는 종료됐다.

**정량적 괴리**

Deal probability / 5% / 대부분 blocked / 2017-05 종료

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Anthem block 가설은 '항소승소·deal close'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Standalone buyback — 적중 · 논지 비중 18%

**당시 주장**

deal 무산 시 약 $7bn capital return이 share count를 크게 줄인다.

**당시 근거**

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

**이 주장이 성립하려면**

balance sheet와 board 의지

**사전 반증조건**

capital을 다른 M&A에 즉시 전용

**실제 결과**

자사주 매입이 강화됐다.

**정량적 괴리**

Buyback / 약 $7bn 예상 / 18.8% 시총 규모 / 자본환원 대폭 강화

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Standalone buyback 가설은 'capital을 다른 M&A에 즉시 전용'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Group D&L recovery — 방향 적중 · 논지 비중 16%

**당시 주장**

2016 약했던 disability/life earnings가 회복된다.

**당시 근거**

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

**이 주장이 성립하려면**

claims experience 정상화

**사전 반증조건**

loss ratio 악화 지속

**실제 결과**

standalone earnings 회복에 기여했다.

**정량적 괴리**

Standalone target / 2018 EPS $11.92×14x / $167 / 2017말 $203

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Group D&L recovery 가설은 'loss ratio 악화 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Breakup fee — 부분 실패 · 논지 비중 16%

**당시 주장**

Cigna가 breakup fee를 받을 가능성이 높다.

**당시 근거**

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

**이 주장이 성립하려면**

계약·litigation 우위

**사전 반증조건**

법원이 fee 지급을 막음

**실제 결과**

즉시 확정촉매가 아니었고 소송이 장기화됐다.

**정량적 괴리**

Breakup fee / $1.85bn+ 기대 / 추가 upside / 장기 소송·즉시 실현 아님

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Breakup fee 가설은 '법원이 fee 지급을 막음'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. 2018 EPS — 적중 · 논지 비중 16%

**당시 주장**

buyback 포함 $11.92 EPS가 가능하다.

**당시 근거**

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

**이 주장이 성립하려면**

operating earnings 안정·share reduction

**사전 반증조건**

earnings miss

**실제 결과**

주가가 target을 크게 상회할 정도로 standalone 가치가 인정됐다.

**정량적 괴리**

약 $143~144→2017년 말 약 $203, +40% 안팎. 작성자는 약 1년 뒤 +32%로 청산했다고 후속 글에서 언급.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

2018 EPS 가설은 'earnings miss'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $167 valuation — 강한 적중 · 논지 비중 16%

**당시 주장**

14x standalone EPS로 16% upside, deal이면 29.5% upside다.

**당시 근거**

연방법원이 Anthem의 Cigna 인수를 막은 뒤 deal completion 가능성을 5%로 낮게 봤다. Deal이 무산되면 Cigna가 약 $7bn을 자사주 매입해 시총의 약 18.8%를 줄이고, 2018 EPS $11.92에 14x를 적용하면 $167이 가능하다고 계산했다. 2016 약했던 Group Disability & Life earnings 회복과 breakup fee, 새로운 M&A도 upside로 봤다.

**이 주장이 성립하려면**

no-deal downside가 제한

**사전 반증조건**

business deterioration

**실제 결과**

2017말 $203으로 target 초과.

**정량적 괴리**

약 $143~144→2017년 말 약 $203, +40% 안팎. 작성자는 약 1년 뒤 +32%로 청산했다고 후속 글에서 언급.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

$167 valuation 가설은 'business deterioration'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

Anthem 거래는 2017년 5월 종료됐고 Cigna는 즉시 자본환원 계획을 강화했다. Breakup-fee 소송은 간단한 즉시 현금화 촉매가 아니었지만 standalone business와 buyback이 주가를 끌어올렸다. 2017년 말 주가는 약 $203으로 $167 standalone target을 크게 넘어섰고, 2018년에는 Express Scripts 인수를 발표했다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 약 $143~144→2017년 말 약 $203, +40% 안팎. 작성자는 약 1년 뒤 +32%로 청산했다고 후속 글에서 언급. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 merger arbitrage를 'deal이 될까'에만 걸지 않고 deal/no-deal 두 상태에서 모두 equity value를 계산한 점이 좋았다. 특히 blocked deal 후 idle capital이 buyback으로 바뀌는 capital-allocation path를 핵심으로 봤다. Breakup fee에 대한 기대는 지나치게 단순했지만 thesis의 필요조건이 아니었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2017-05-12 — Cigna가 Anthem merger agreement 종료와 대규모 자사주 매입을 발표. No-deal standalone case가 실제 실행경로로 전환됐다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 낮음. 핵심 standalone thesis가 맞았다. 단 breakup fee를 확정 현금처럼 보지 않고 litigation-adjusted probability를 별도 관리했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Deal probability | 5% | 대부분 blocked | 2017-05 종료 | 적중 |
| Buyback | 약 $7bn 예상 | 18.8% 시총 규모 | 자본환원 대폭 강화 | 적중 |
| Standalone target | 2018 EPS $11.92×14x | $167 | 2017말 $203 | 초과 |
| Breakup fee | $1.85bn+ 기대 | 추가 upside | 장기 소송·즉시 실현 아님 | 부분 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-02-20 | VIC 아이디어 게시 | Anthem deal break·$7bn buyback·$167 standalone Long |
| 2017-05-12 | 최초 핵심 검증·반증 신호 | Cigna가 Anthem merger agreement 종료와 대규모 자사주 매입을 발표. No-deal standalone case가 실제 실행경로로 전환됐다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 약 $143~144→2017년 말 약 $203, +40% 안팎. 작성자는 약 1년 뒤 +32%로 청산했다고 후속 글에서 언급. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating causal chain은 대체로 맞았으나 price target의 multiple·timing은 별도 관리 필요
- **최초 검증·반증 신호:** 2017-05-12 — Cigna가 Anthem merger agreement 종료와 대규모 자사주 매입을 발표. No-deal standalone case가 실제 실행경로로 전환됐다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 낮음. 핵심 standalone thesis가 맞았다. 단 breakup fee를 확정 현금처럼 보지 않고 litigation-adjusted probability를 별도 관리했어야 한다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- 1. VIC CI 2017-02-20 원문 — Value Investors Club, 2017-02-20. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:f41d7535-909b-4d27-80c4-35fdb55eacbd -->
## 6. 2019-03-28 — Express Scripts integration·15% EPS CAGR·$350 2021 Long

### 결론부터

**종합판정: 사업논지 강한 적중·multiple thesis 실패.** 이번 배치에서 가장 교육적인 사례 중 하나다. operating model은 거의 정확했지만 valuation multiple을 독립된 가정으로 충분히 stress하지 않았다. 10x가 싸다는 판단과 17x로 돌아가야 한다는 판단은 완전히 다른 주장이다. 사업 성공과 rerating 성공을 분리해야 한다.

**주가·증권 결과:** $160→2019말 약 $204(+28%), 2021말 약 $230(+44%). 2021 target $350은 크게 미달.

**Thesis / Process 점수:** 7.4 / 7.5

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

2018~21 EPS CAGR 약 15%, 2021 EPS $20~21. 17x를 적용해 약 $350 in 2021. Year-end 2019 fair value를 약 $290로 제시. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. EPS compounding — 강한 적중 · 논지 비중 18%

**당시 주장**

ESRX 통합 후에도 2018~21 EPS가 약 15% CAGR 가능하다.

**당시 근거**

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

**이 주장이 성립하려면**

synergy·organic growth·buyback이 offset

**사전 반증조건**

PBM slowdown·integration failure

**실제 결과**

2021 adjusted EPS $20.47로 목표범위 정확히 달성.

**정량적 괴리**

2021 adj EPS / $20~21 / 15% CAGR / $20.47

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

EPS compounding 가설은 'PBM slowdown·integration failure'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. PBM durability — 적중 · 논지 비중 18%

**당시 주장**

Express Scripts는 정치 headline보다 안정적 cash/fee business다.

**당시 근거**

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

**이 주장이 성립하려면**

client retention·script growth 유지

**사전 반증조건**

rebate reform으로 economics 급감

**실제 결과**

사업은 earnings를 지지하며 Evernorth 기반이 됐다.

**정량적 괴리**

Forward P/E / 약 10x / 17x 정상화 / 2021말 target 대비 낮은 multiple

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

PBM durability 가설은 'rebate reform으로 economics 급감'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Deleveraging — 적중 · 논지 비중 16%

**당시 주장**

인수 후 약 4x leverage가 빠르게 내려간다.

**당시 근거**

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

**이 주장이 성립하려면**

FCF를 debt reduction에 우선 배분

**사전 반증조건**

earnings miss·추가 M&A

**실제 결과**

인수 직후보다 balance sheet가 개선됐다.

**정량적 괴리**

Debt / 약 4x debt/EBITDA / mid-2x 방향 / deleveraging 진행

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Deleveraging 가설은 'earnings miss·추가 M&A'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Political risk — 적중 · 논지 비중 16%

**당시 주장**

Medicare-for-All·rebate 공포가 현실 fundamentals보다 과도하다.

**당시 근거**

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

**이 주장이 성립하려면**

정책이 급진적 구조변화로 이어지지 않음

**사전 반증조건**

PBM/보험 economics 직접 훼손

**실제 결과**

단기 catastrophic policy shock은 없었다.

**정량적 괴리**

주가 / $160 / 2021 $350 / 2021말 약 $230

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Political risk 가설은 'PBM/보험 economics 직접 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. 17x rerating — 실패 · 논지 비중 16%

**당시 주장**

사업정상화 후 S&P에 가까운 17x multiple이 가능하다.

**당시 근거**

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

**이 주장이 성립하려면**

merger/PBM discount 소멸

**사전 반증조건**

구조적 discount 지속

**실제 결과**

2021에도 target P/E가 형성되지 않았다.

**정량적 괴리**

$160→2019말 약 $204(+28%), 2021말 약 $230(+44%). 2021 target $350은 크게 미달.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

17x rerating 가설은 '구조적 discount 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $350 target — 실패 · 논지 비중 16%

**당시 주장**

$20~21 EPS×17x로 2021 $350 가능하다.

**당시 근거**

Express Scripts 인수 직후 Cigna가 약 10x forward earnings로 S&P 17x 대비 40% discount인데 2009~18 EPS CAGR 15%를 이어갈 수 있다고 봤다. PBM rebate 규제, Medicare for All, 약 4x debt/EBITDA가 과도한 우려이며 integration·deleveraging 후 mid-2x leverage와 2021 EPS $20~21, 17x multiple로 $350이 가능하다고 주장했다.

**이 주장이 성립하려면**

EPS와 multiple이 동시에 맞음

**사전 반증조건**

둘 중 하나 미달

**실제 결과**

EPS는 맞았지만 multiple이 틀려 $350 미달.

**정량적 괴리**

$160→2019말 약 $204(+28%), 2021말 약 $230(+44%). 2021 target $350은 크게 미달.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

$350 target 가설은 '둘 중 하나 미달'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

운영예측은 놀랍도록 정확했다. Cigna의 2021 adjusted EPS는 $20.47로 원문 $20~21 범위에 정확히 들어왔고, debt ratio도 인수 직후보다 낮아졌다. 그러나 2021년 말 주가는 약 $230으로 $350 target에 크게 못 미쳤다. 즉 'EPS를 맞혔다=주식 목표가를 맞혔다'가 아니었다. PBM 정치위험·복합사업 할인·capital allocation을 반영한 P/E는 원문이 기대한 17x까지 가지 않았다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 $160→2019말 약 $204(+28%), 2021말 약 $230(+44%). 2021 target $350은 크게 미달. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이번 배치에서 가장 교육적인 사례 중 하나다. operating model은 거의 정확했지만 valuation multiple을 독립된 가정으로 충분히 stress하지 않았다. 10x가 싸다는 판단과 17x로 돌아가야 한다는 판단은 완전히 다른 주장이다. 사업 성공과 rerating 성공을 분리해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-02-03 — 2021 adjusted EPS $20.47가 발표돼 operating thesis는 사실상 완전 검증됐지만 주가는 $350과 크게 괴리되어 multiple thesis 실패가 확정적으로 드러났다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 높음. 2020~21 EPS가 예상대로 가는 동안에도 stock multiple이 낮게 유지된 이유를 PBM·politics·conglomerate/merger discount 관점에서 다시 평가했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

사업논지 강한 적중·multiple thesis 실패. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2021 adj EPS | $20~21 | 15% CAGR | $20.47 | 거의 정확 |
| Forward P/E | 약 10x | 17x 정상화 | 2021말 target 대비 낮은 multiple | 실패 |
| Debt | 약 4x debt/EBITDA | mid-2x 방향 | deleveraging 진행 | 적중 |
| 주가 | $160 | 2021 $350 | 2021말 약 $230 | 목표 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-03-28 | VIC 아이디어 게시 | Express Scripts integration·15% EPS CAGR·$350 2021 Long |
| 2022-02-03 | 최초 핵심 검증·반증 신호 | 2021 adjusted EPS $20.47가 발표돼 operating thesis는 사실상 완전 검증됐지만 주가는 $350과 크게 괴리되어 multiple thesis 실패가 확정적으로 드러났다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | $160→2019말 약 $204(+28%), 2021말 약 $230(+44%). 2021 target $350은 크게 미달. |

### Failure / Success Anatomy

- **근본 오류:** operating earnings와 catalyst·multiple의 독립성을 충분히 분리하지 않음
- **최초 검증·반증 신호:** 2022-02-03 — 2021 adjusted EPS $20.47가 발표돼 operating thesis는 사실상 완전 검증됐지만 주가는 $350과 크게 괴리되어 multiple thesis 실패가 확정적으로 드러났다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 높음. 2020~21 EPS가 예상대로 가는 동안에도 stock multiple이 낮게 유지된 이유를 PBM·politics·conglomerate/merger discount 관점에서 다시 평가했어야 한다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- [1. VIC CI 2019-03-28 원문](https://www.valueinvestorsclub.com/idea/CIGNA_CORP/2769380286) — Value Investors Club, 2019-03-28. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:924328d7-6fb7-4375-a708-b55c5ddb4f0b -->
## 7. 2021-06-03 — Evernorth 54% earnings·$8bn FCF/buyback·$300 year-end Long

### 결론부터

**종합판정: 운영예측 매우 정확·timing/multiple 오류.** 2019 글과 마찬가지로 'EPS 정확도'와 '주가 timing'을 분리해야 하는 사례다. Evernorth economics와 capital return을 잘 봤지만 13x multiple이 6개월 안에 형성된다는 event-time 가정이 약했다. 목표가에 만기를 붙이면 multiple path도 thesis가 된다.

**주가·증권 결과:** 2021말 약 $229.63로 단기 -10% 안팎, $300 target 실패. 2022말 약 $331.34로 target은 약 1년 늦게 달성.

**Thesis / Process 점수:** 7.4 / 7.5

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

2021 EPS 약 $20.50, 2022 약 $23.00. 13x 2022 EPS≈$300, 약 6개월 +17% 목표. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Evernorth quality — 적중 · 논지 비중 18%

**당시 주장**

Evernorth가 earnings 54%를 차지하는 scaled asset-light PBM/services platform이다.

**당시 근거**

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

**이 주장이 성립하려면**

높은 retention·script/specialty growth

**사전 반증조건**

대형 client loss·regulation

**실제 결과**

2021 Evernorth가 strong earnings를 이끌었다.

**정량적 괴리**

2021 adj EPS / 약 $20.50 / 달성 / $20.47

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Evernorth quality 가설은 '대형 client loss·regulation'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Cigna Healthcare — 적중 · 논지 비중 18%

**당시 주장**

U.S. Medical 37% earnings와 ASO mix가 안정적이다.

**당시 근거**

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

**이 주장이 성립하려면**

medical cost/pricing 관리

**사전 반증조건**

MLR shock

**실제 결과**

2021 medical customers도 성장했다.

**정량적 괴리**

2022 adj EPS / 약 $23.00 / 달성 / $23.27

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Cigna Healthcare 가설은 'MLR shock'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Political risk — 적중 · 논지 비중 16%

**당시 주장**

2021 정치환경에서 급진적 PBM/insurance risk가 낮다.

**당시 근거**

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

**이 주장이 성립하려면**

정책변화 제한

**사전 반증조건**

reimbursement/rebate 구조 붕괴

**실제 결과**

단기 catastrophic shock 없음.

**정량적 괴리**

2021 buyback / ~$8bn FCF 활용 / 대규모 repurchase / 35.2m/$7.7bn

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Political risk 가설은 'reimbursement/rebate 구조 붕괴'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Balance sheet reload — 강한 적중 · 논지 비중 16%

**당시 주장**

Disability/Life sale proceeds와 FCF가 buyback·dividend 여력을 만든다.

**당시 근거**

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

**이 주장이 성립하려면**

sale close·debt 관리

**사전 반증조건**

proceeds가 debt stress에만 흡수

**실제 결과**

2021 $7.7bn buyback과 dividend 시작.

**정량적 괴리**

주가 / 약 $256 / 2021말 $300 / 2021말 $229.63; 2022말 $331.34

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Balance sheet reload 가설은 'proceeds가 debt stress에만 흡수'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. EPS targets — 강한 적중 · 논지 비중 16%

**당시 주장**

2021 $20.50, 2022 $23 EPS가 가능하다.

**당시 근거**

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

**이 주장이 성립하려면**

Evernorth·Healthcare earnings 유지

**사전 반증조건**

EPS miss

**실제 결과**

$20.47/$23.27로 거의 정확.

**정량적 괴리**

2021말 약 $229.63로 단기 -10% 안팎, $300 target 실패. 2022말 약 $331.34로 target은 약 1년 늦게 달성.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

EPS targets 가설은 'EPS miss'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $300 timing — timing 실패 · 논지 비중 16%

**당시 주장**

13x 2022 EPS로 2021말 $300 가능하다.

**당시 근거**

Cigna가 11x 2022E earnings에 거래되고 Evernorth가 2021E earnings의 약 54%, U.S. Medical 37%를 차지한다고 분해했다. Evernorth는 3대 scaled PBM 중 하나로 98% 수준 retention·specialty/mail-order·formulary scale을 가진 asset-light toll taker라고 봤다. Group Disability & Life 매각으로 balance sheet가 재장전되고 약 $8bn FCF, 새 배당, buyback을 통해 장기 10~13% EPS growth가 가능하다고 주장했다.

**이 주장이 성립하려면**

multiple이 6개월 내 정상화

**사전 반증조건**

P/E discount 지속

**실제 결과**

2021말 실패, 2022말 지연 달성.

**정량적 괴리**

2021말 약 $229.63로 단기 -10% 안팎, $300 target 실패. 2022말 약 $331.34로 target은 약 1년 늦게 달성.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

$300 timing 가설은 'P/E discount 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

2021 adjusted EPS $20.47, 2022 adjusted EPS $23.27로 operating forecast가 거의 완벽하게 맞았다. 2021에 35.2m shares/$7.7bn을 repurchase했고 dividend도 시작했다. 하지만 2021말 주가는 약 $230으로 $300 target을 못 맞췄다. 2022말에는 약 $331로 target을 넘었다. 즉 business forecast는 맞고 valuation/timing이 1년 틀렸다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 2021말 약 $229.63로 단기 -10% 안팎, $300 target 실패. 2022말 약 $331.34로 target은 약 1년 늦게 달성. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

2019 글과 마찬가지로 'EPS 정확도'와 '주가 timing'을 분리해야 하는 사례다. Evernorth economics와 capital return을 잘 봤지만 13x multiple이 6개월 안에 형성된다는 event-time 가정이 약했다. 목표가에 만기를 붙이면 multiple path도 thesis가 된다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-02-03 — 2021 EPS $20.47와 $7.7bn buyback이 발표돼 operating/capital-return thesis는 검증됐지만 연말 $300 target은 이미 실패. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 높음. 2021 하반기 EPS와 buyback이 맞는데 multiple만 안 움직였으므로 보유논지를 '6개월 rerating'에서 'EPS/share compounding'으로 명시적으로 바꿀 수 있었다.

### 10. 최종 판정·반사실·재사용 교훈

운영예측 매우 정확·timing/multiple 오류. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2021 adj EPS | 약 $20.50 | 달성 | $20.47 | 거의 정확 |
| 2022 adj EPS | 약 $23.00 | 달성 | $23.27 | 초과 |
| 2021 buyback | ~$8bn FCF 활용 | 대규모 repurchase | 35.2m/$7.7bn | 적중 |
| 주가 | 약 $256 | 2021말 $300 | 2021말 $229.63; 2022말 $331.34 | 1년 지연 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-06-03 | VIC 아이디어 게시 | Evernorth 54% earnings·$8bn FCF/buyback·$300 year-end Long |
| 2022-02-03 | 최초 핵심 검증·반증 신호 | 2021 EPS $20.47와 $7.7bn buyback이 발표돼 operating/capital-return thesis는 검증됐지만 연말 $300 target은 이미 실패. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 2021말 약 $229.63로 단기 -10% 안팎, $300 target 실패. 2022말 약 $331.34로 target은 약 1년 늦게 달성. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating causal chain은 대체로 맞았으나 price target의 multiple·timing은 별도 관리 필요
- **최초 검증·반증 신호:** 2022-02-03 — 2021 EPS $20.47와 $7.7bn buyback이 발표돼 operating/capital-return thesis는 검증됐지만 연말 $300 target은 이미 실패.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 높음. 2021 하반기 EPS와 buyback이 맞는데 multiple만 안 움직였으므로 보유논지를 '6개월 rerating'에서 'EPS/share compounding'으로 명시적으로 바꿀 수 있었다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- [1. VIC CI 2021-06-03 원문](https://www.valueinvestorsclub.com/idea/CIGNA_CORP/2652481205) — Value Investors Club, 2021-06-03. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

<!-- idea:5c62749c-7f75-4c8f-8336-ba8b40b8ffc6 -->
## 8. 2022-09-25 — 10~13% EPS compounder·Evernorth/Cigna SOTP·$382 Long

### 결론부터

**종합판정: 사업·buyback 부분 적중·SOTP/multiple 실패.** business quality와 buyback capacity를 잘 봤지만 segment multiple을 더한 SOTP가 실제 public-market multiple로 즉시 crystallize될 이유가 부족했다. Evernorth와 Healthcare가 한 회사 안에 있는 구조 자체가 diversification premium이 아니라 conglomerate/PBM discount를 받을 수도 있다. 'intrinsic 382'와 '1년 안에 382'는 별도 주장이다.

**주가·증권 결과:** 약 $279→2023말 약 $299.45, +7% 안팎. 1년 $382 target에는 크게 미달.

**Thesis / Process 점수:** 7.4 / 7.5

### 1. 무슨 기업인가

The Cigna Group는 고용주·개인·정부 고객에게 건강보험과 건강서비스를 제공하는 미국의 대형 health-services 기업이다. 2018년 Express Scripts 인수 전에는 상업 건강보험, Administrative Services Only(ASO), International, Group Disability & Life 등이 중심이었고, 인수 이후에는 크게 Evernorth Health Services와 Cigna Healthcare로 나뉜다. Cigna Healthcare의 ASO에서는 고용주가 실제 의료비 위험을 부담하고 Cigna는 네트워크·청구처리·plan design 등 관리서비스 수수료를 받는다. 반면 guaranteed cost·Medicare 등 risk-bearing 보험에서는 premium에서 medical claims와 SG&A를 차감한 underwriting margin이 핵심이다. Evernorth는 Express Scripts를 기반으로 PBM, specialty pharmacy, care delivery, benefits management 등을 제공한다. 따라서 Cigna를 볼 때 단순 가입자수보다 ASO/risk mix, medical loss ratio·medical cost trend, 고객 유지율, 약국·PBM 고객수와 script volume, specialty pharmacy, SG&A, reserve accuracy, debt, FCF, 자사주 매입가격을 함께 봐야 한다. 이 회사의 투자역사에서 특히 중요한 것은 운영이 좋아도 P/E가 원하는 만큼 rerating되지 않을 수 있고, 반대로 이벤트 촉매가 실패해도 사업 실적 때문에 주가가 오를 수 있다는 점이다.

### 2. 산업 가치사슬과 돈의 흐름

Managed care의 돈 흐름은 fee와 risk를 분리해서 봐야 한다. ASO에서는 employer가 claims를 실질적으로 부담하고 Cigna는 관리수수료를 받아 보험위험이 낮고 자본집약도도 낮다. Risk product에서는 premium − medical claims = gross underwriting margin이고, 여기서 SG&A와 기타비용을 빼야 한다. 따라서 pricing이 medical trend를 얼마나 앞서가는지와 claims system이 의료비를 정확하게 읽는지가 결정적이다. PBM에서는 대규모 script volume과 pharmacy network를 이용해 plan sponsor와 제약사·약국 사이에서 formulary, rebate, mail order, specialty, administrative fee 등으로 수익을 얻지만 규제와 client retention이 핵심 리스크다. 최종 equity value는 각 사업의 operating earnings가 cash로 전환된 뒤 debt reduction·M&A·dividend·buyback으로 어떻게 배분되는지까지 내려가야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Cigna의 경쟁우위는 전국 단위 employer network, 높은 ASO 비중, 의료비 관리·provider contracting 능력, Express Scripts 이후 PBM 규모와 specialty capabilities, 장기 client relationships에 있다. 하지만 managed care는 짧은 tail의 보험이라고 해서 low-risk가 아니다. claims processing 오류, medical trend 오판, pricing lag, reserve error, employer churn이 1~2년 안에 수익성을 크게 흔들 수 있다. PBM은 규모가 moat이지만 rebate·spread economics에 대한 정치적 압력과 client repricing도 존재한다. 따라서 핵심 질문은 '좋은 managed-care franchise인가'가 아니라 '현재 EPS 성장의 원천이 영업인지, buyback인지, multiple 가정인지'까지 분해하는 것이다.

### 4. 당시 VIC 원문과 핵심 숫자

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

2022E 12x, 2023E 11x. Evernorth 12x EBITDA, Cigna Healthcare 14x EBITDA SOTP로 1년 intrinsic $382(+37%). Best case 18x 2023E EPS≈$455(+64%). 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. EPS compounder — 부분 · 논지 비중 18%

**당시 주장**

10~13% LT EPS growth와 과거 15% track record가 지속된다.

**당시 근거**

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

**이 주장이 성립하려면**

organic growth+buyback

**사전 반증조건**

medical/PBM headwind로 EPS 저성장

**실제 결과**

2023 EPS는 성장했지만 약 7.8%로 단기 range 미달.

**정량적 괴리**

Adjusted EPS / 2022E 기준 / 10~13% LT growth / 2022 $23.27→2023 $25.09(+7.8%)

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

EPS compounder 가설은 'medical/PBM headwind로 EPS 저성장'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Evernorth SOTP — 사업 적중·valuation 실패 · 논지 비중 18%

**당시 주장**

Evernorth는 12x EBITDA를 받을 quality services/PBM이다.

**당시 근거**

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

**이 주장이 성립하려면**

client retention·specialty growth·정책안정

**사전 반증조건**

PBM multiple 구조적 할인

**실제 결과**

사업규모는 성장했지만 SOTP multiple은 시장에서 즉시 인정되지 않았다.

**정량적 괴리**

Buyback / 2022 약 10% shares / 공격적 지속 / 2022 27.4m/$7.6bn; 2023 7.8m/$2.3bn

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Evernorth SOTP 가설은 'PBM multiple 구조적 할인'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Healthcare SOTP — 부분 · 논지 비중 16%

**당시 주장**

Cigna Healthcare는 14x EBITDA quality insurance/ASO franchise다.

**당시 근거**

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

**이 주장이 성립하려면**

medical trend·ASO retention 안정

**사전 반증조건**

MLR·membership shock

**실제 결과**

사업은 안정적이었지만 14x crystallization은 부재.

**정량적 괴리**

SOTP value / $382 1년 / 37% upside / 2023말 $299.45

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Healthcare SOTP 가설은 'MLR·membership shock'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Buyback — 강한 적중 · 논지 비중 16%

**당시 주장**

divestiture proceeds와 FCF로 2022 약 10% shares를 repurchase한다.

**당시 근거**

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

**이 주장이 성립하려면**

balance sheet 여력

**사전 반증조건**

capital diversion

**실제 결과**

2022 27.4m shares/$7.6bn 매입.

**정량적 괴리**

Evernorth scale / 핵심 compounder / 성장 / 2023 adjusted revenue $153.5bn

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Buyback 가설은 'capital diversion'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. Macro/political defense — 대체로 적중 · 논지 비중 16%

**당시 주장**

recession/inflation 영향이 낮고 higher rates가 일부 긍정적이다.

**당시 근거**

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

**이 주장이 성립하려면**

pricing과 fee revenue 방어

**사전 반증조건**

medical inflation이 premium repricing보다 빠름

**실제 결과**

단기 macro가 thesis를 깨는 shock은 없었다.

**정량적 괴리**

약 $279→2023말 약 $299.45, +7% 안팎. 1년 $382 target에는 크게 미달.

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Macro/political defense 가설은 'medical inflation이 premium repricing보다 빠름'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $382/$455 target — 실패 · 논지 비중 16%

**당시 주장**

SOTP·18x scenario로 1년 37~64% upside가 있다.

**당시 근거**

Cigna는 장기 EPS growth 10~13%를 가이드하지만 과거 11년 15%를 달성했고, 2022 약 12x·2023 약 11x에 거래된다고 봤다. 2022년에 divestiture proceeds까지 이용해 약 10% share count를 repurchase하고, Evernorth와 Cigna Healthcare를 각각 별도 quality multiple로 평가하면 $382, 최고 $455가 가능하다고 주장했다. Inflation/recession 영향이 작고 higher rates도 일부 이익이라고 봤다.

**이 주장이 성립하려면**

market multiple expansion

**사전 반증조건**

discount 지속

**실제 결과**

2023말 약 $299로 target 크게 미달.

**정량적 괴리**

약 $279→2023말 약 $299.45, +7% 안팎. 1년 $382 target에는 크게 미달.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

$382/$455 target 가설은 'discount 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

2022 adjusted EPS $23.27, 2023 $25.09로 earnings는 계속 늘었지만 2023 growth는 약 7.8%로 10~13% 장기 range보다 낮았다. 2022에는 27.4m shares/$7.6bn을 repurchase했고 2023에도 7.8m/$2.3bn을 매입했다. 2023 Evernorth adjusted revenue는 $153.5bn, Cigna Healthcare $51.2bn이었다. 그러나 2023말 주가는 약 $299로 $382 one-year SOTP에 크게 못 미쳤다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 약 $279→2023말 약 $299.45, +7% 안팎. 1년 $382 target에는 크게 미달. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

business quality와 buyback capacity를 잘 봤지만 segment multiple을 더한 SOTP가 실제 public-market multiple로 즉시 crystallize될 이유가 부족했다. Evernorth와 Healthcare가 한 회사 안에 있는 구조 자체가 diversification premium이 아니라 conglomerate/PBM discount를 받을 수도 있다. 'intrinsic 382'와 '1년 안에 382'는 별도 주장이다.

### 9. 최초 검증·반증 신호와 회피 가능성

2023-12-29 — 2023말 주가가 약 $299에 머문 반면 1년 $382 target horizon이 종료되어 SOTP/multiple thesis가 실패. 동시에 earnings와 buyback은 계속되어 business thesis와 price thesis가 분리됐다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 높음. 2023 실적이 나쁘지 않은데 multiple만 낮다면 segment SOTP가 market-clearing valuation인지 재검증할 수 있었다.

### 10. 최종 판정·반사실·재사용 교훈

사업·buyback 부분 적중·SOTP/multiple 실패. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Adjusted EPS | 2022E 기준 | 10~13% LT growth | 2022 $23.27→2023 $25.09(+7.8%) | 성장·range 미달 |
| Buyback | 2022 약 10% shares | 공격적 지속 | 2022 27.4m/$7.6bn; 2023 7.8m/$2.3bn | 적중 |
| SOTP value | $382 1년 | 37% upside | 2023말 $299.45 | 실패 |
| Evernorth scale | 핵심 compounder | 성장 | 2023 adjusted revenue $153.5bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2022-09-25 | VIC 아이디어 게시 | 10~13% EPS compounder·Evernorth/Cigna SOTP·$382 Long |
| 2023-12-29 | 최초 핵심 검증·반증 신호 | 2023말 주가가 약 $299에 머문 반면 1년 $382 target horizon이 종료되어 SOTP/multiple thesis가 실패. 동시에 earnings와 buyback은 계속되어 business thesis와 price thesis가 분리됐다. |
| 2012-12-31 | managed-care 구조 중간점검 | ASO/risk mix·health reform·capital allocation을 재검증 |
| 2018-12-20 | Express Scripts 시대 전환 | Cigna가 Express Scripts를 인수하며 Evernorth/PBM economics가 그룹 가치의 핵심으로 확대 |
| 2023-12-31 | 장기 사업상태 점검 | 2023 adjusted EPS $25.09, Evernorth adjusted revenue $153.5bn, 지속 자사주 매입 |
| 2024-01-31 | 고정 평가기준일 | 약 $279→2023말 약 $299.45, +7% 안팎. 1년 $382 target에는 크게 미달. |

### Failure / Success Anatomy

- **근본 오류:** operating earnings와 catalyst·multiple의 독립성을 충분히 분리하지 않음
- **최초 검증·반증 신호:** 2023-12-29 — 2023말 주가가 약 $299에 머문 반면 1년 $382 target horizon이 종료되어 SOTP/multiple thesis가 실패. 동시에 earnings와 buyback은 계속되어 business thesis와 price thesis가 분리됐다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 높음. 2023 실적이 나쁘지 않은데 multiple만 낮다면 segment SOTP가 market-clearing valuation인지 재검증할 수 있었다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** aso_fee_model; claims_turnaround; segment_economics; pbm_scale; eps_compounding; buyback
- **실패·주의 패턴:** catalyst_attribution; multiple_rerating; claims_system_operational_risk; political_timing; sotp_crystallization

### 주요 근거자료

- [1. VIC CI 2022-09-25 원문](https://www.valueinvestorsclub.com/idea/CIGNA_CORP/4948540181) — Value Investors Club, 2022-09-25. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Cigna 2002 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015903000165/cigna10k.htm) — SEC, 2003-03-06. 2001~02 claims-system·사업구조·재무상태 사후검증
- [3. Cigna says it won't meet earnings target](https://www.businessinsurance.com/cigna-says-it-wont-meet-earnings-target/) — Business Insurance, 2002-10-25. 2002 earnings warning과 하루 38%대 주가 급락 확인
- [4. Cigna 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000095015905000256/cigna10k.htm) — SEC, 2005-03-03. 2003 turnaround 이후 사업·실적 확인
- [5. Cigna 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000130817911000024/lcig2010f10k.htm) — SEC, 2011-02-24. Cigna Pharmacy Management를 계속 영위해 2009 PBM sale 미발생 확인
- [6. Cigna 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/701221/000104746913001925/a2213028z10-k.htm) — SEC, 2013-02-28. HealthSpring 약 $3.8bn 인수·사업 mix 확인
- [7. Cigna terminates Anthem merger and outlines capital deployment](https://www.sec.gov/Archives/edgar/data/701221/000095015917000134/ex99-1.htm) — Cigna/SEC, 2017-05-12. Anthem 거래 종료·자본환원 확인
- [8. Cigna to acquire Express Scripts](https://www.sec.gov/Archives/edgar/data/701221/000095015918000059/ex99-1.htm) — Cigna/SEC, 2018-03-08. Express Scripts 거래 구조·전략 확인
- [9. Cigna 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994020000006/ci-20191231.htm) — SEC, 2020-02-27. Express Scripts 통합·deleveraging 진행 확인
- [10. Cigna FY2021 results](https://www.sec.gov/Archives/edgar/data/1739940/000095015922000018/ex99-1.htm) — Cigna/SEC, 2022-02-03. 2021 adjusted EPS $20.47, repurchase 35.2m/$7.7bn 확인
- [11. Cigna 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994023000008/ci-20221231.htm) — SEC, 2023-02-23. 2022 27.4m shares/$7.6bn repurchase와 사업실적 확인
- [12. Cigna 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1739940/000173994024000005/ci-20231231.htm) — SEC, 2024-02-23. 2023 Evernorth $153.5bn adjusted revenue, buyback·segment economics 확인
- [13. Cigna historical prices](https://www.digrin.com/stocks/detail/CI/price) — Digrin, 2024-01-31. 역사적 월말 가격 교차검증


---

# UNITEDHEALTH GROUP (UNH) — 기업과 비즈니스

## 1. 무슨 기업인가

UnitedHealth Group는 UnitedHealthcare와 Optum을 결합한 미국 최대급 통합 health-care 기업이다. UnitedHealthcare는 commercial, Medicare, Medicaid 등 risk-bearing 보험과 fee-based employer 서비스를 제공하고, Optum은 Optum Health, Optum Insight, Optum Rx를 통해 care delivery, data/analytics, technology, pharmacy benefit 서비스를 제공한다. 이 구조는 보험의 underwriting cash flow와 fee-based·service earnings를 결합한다. 보험에서는 medical care ratio(MCR), pricing, member mix, reserves가 핵심이고 Optum에서는 고객수·revenue·operating margin·care delivery scale이 중요하다. 2006 VIC 작성자가 UNH를 단순 보험사가 아니라 'healthcare technology/data company'라고 본 통찰은 훗날 Optum의 성장으로 강하게 검증됐다. 다만 business quality가 높더라도 옵션 백데이팅, 의료비 trend, 정치·규제, recession, multiple compression과 파생상품의 만기 같은 경로위험이 주식성과를 크게 바꿀 수 있다.

## 2. 산업 가치사슬과 돈의 흐름

UnitedHealthcare는 premium·fee revenue에서 medical costs와 operating costs를 차감해 수익을 낸다. Optum은 PBM script economics, data/technology fees, care delivery·value-based care 등 여러 서비스 수익원을 제공한다. 규모가 커질수록 provider network 협상력, data density, SG&A leverage와 cross-selling이 강화될 수 있다. 그러나 정부사업 비중이 크기 때문에 Medicare/Medicaid reimbursement와 medical cost trend가 빠르게 바뀔 수 있다. 투자자는 revenue growth보다 MCR, operating cost ratio, Optum earnings, cash flow from operations, share count, repurchase price와 규제환경을 함께 봐야 한다.

## 3. 경쟁우위·경쟁구도·핵심 지표

UNH의 핵심 우위는 규모·provider network·data·technology·brand·distribution·Optum 서비스의 통합이다. 이 결합은 보험만 하는 경쟁사보다 고객 접점과 수익원이 넓고, data를 pricing·care management·fraud detection·provider performance에 재사용할 수 있게 한다. 그러나 이러한 장기 moat가 단기 valuation floor를 보장하지는 않는다. 2007~08 사례처럼 earnings가 완전히 무너지지 않아도 MCR 우려·정치리스크·금융시장 shock과 multiple compression으로 equity와 LEAPS가 크게 손실날 수 있다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2006-12-30 | Long | Long | Healthcare technology/data platform·$85 intrinsic Long | 약 $53.73→2007말 $58대였지만 2008말 약 $26.6으로 약 -50%. 장기적으로는 Optum 성장과 함께 사업가치가 크게 확대됐으나 원래 몇 년 투자경로는 실패. | 중기 투자 실패·장기 사업모델 통찰은 탁월 |
| 2007-12-20 | Long | Long | 12~15% FCF/share·$85~100 2010·LEAPS Long | $58.11→2008말 약 $26.6(-54%). Jan-2010 $50 strike LEAPS의 breakeven $65.70을 크게 밑돌아 파생상품 thesis는 심각한 실패. | 명백한 실패 |

---

<!-- idea:3e9ff049-86a7-42c1-a813-feff637208e8 -->
## 1. 2006-12-30 — Healthcare technology/data platform·$85 intrinsic Long

### 결론부터

**종합판정: 중기 투자 실패·장기 사업모델 통찰은 탁월.** 기업의 본질에 대한 통찰과 주식의 downside distribution을 분리해야 하는 사례다. 'technology/data platform'이라는 추상화는 15년 후 Optum으로 강하게 검증됐지만, options scandal이 non-operational이므로 downside가 작다는 결론은 과도했다. managed-care cycle, MCR, politics, recession과 multiple compression이 동시에 오는 joint tail을 모델링하지 않았다.

**주가·증권 결과:** 약 $53.73→2007말 $58대였지만 2008말 약 $26.6으로 약 -50%. 장기적으로는 Optum 성장과 함께 사업가치가 크게 확대됐으나 원래 몇 년 투자경로는 실패.

**Thesis / Process 점수:** 8.8 / 7.5

### 1. 무슨 기업인가

UnitedHealth Group는 UnitedHealthcare와 Optum을 결합한 미국 최대급 통합 health-care 기업이다. UnitedHealthcare는 commercial, Medicare, Medicaid 등 risk-bearing 보험과 fee-based employer 서비스를 제공하고, Optum은 Optum Health, Optum Insight, Optum Rx를 통해 care delivery, data/analytics, technology, pharmacy benefit 서비스를 제공한다. 이 구조는 보험의 underwriting cash flow와 fee-based·service earnings를 결합한다. 보험에서는 medical care ratio(MCR), pricing, member mix, reserves가 핵심이고 Optum에서는 고객수·revenue·operating margin·care delivery scale이 중요하다. 2006 VIC 작성자가 UNH를 단순 보험사가 아니라 'healthcare technology/data company'라고 본 통찰은 훗날 Optum의 성장으로 강하게 검증됐다. 다만 business quality가 높더라도 옵션 백데이팅, 의료비 trend, 정치·규제, recession, multiple compression과 파생상품의 만기 같은 경로위험이 주식성과를 크게 바꿀 수 있다.

### 2. 산업 가치사슬과 돈의 흐름

UnitedHealthcare는 premium·fee revenue에서 medical costs와 operating costs를 차감해 수익을 낸다. Optum은 PBM script economics, data/technology fees, care delivery·value-based care 등 여러 서비스 수익원을 제공한다. 규모가 커질수록 provider network 협상력, data density, SG&A leverage와 cross-selling이 강화될 수 있다. 그러나 정부사업 비중이 크기 때문에 Medicare/Medicaid reimbursement와 medical cost trend가 빠르게 바뀔 수 있다. 투자자는 revenue growth보다 MCR, operating cost ratio, Optum earnings, cash flow from operations, share count, repurchase price와 규제환경을 함께 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

UNH의 핵심 우위는 규모·provider network·data·technology·brand·distribution·Optum 서비스의 통합이다. 이 결합은 보험만 하는 경쟁사보다 고객 접점과 수익원이 넓고, data를 pricing·care management·fraud detection·provider performance에 재사용할 수 있게 한다. 그러나 이러한 장기 moat가 단기 valuation floor를 보장하지는 않는다. 2007~08 사례처럼 earnings가 완전히 무너지지 않아도 MCR 우려·정치리스크·금융시장 shock과 multiple compression으로 equity와 LEAPS가 크게 손실날 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

### 5. 밸류에이션과 기대수익의 연결

확률가중 intrinsic 약 $85, 합리적 range $80~95. Management guidance 기반 $95~110. Meltdown scenario를 $45~60으로 봐 downside가 제한적이라고 평가. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Technology/data edge — 장기 강한 적중 · 논지 비중 18%

**당시 주장**

UNH는 단순 insurer가 아니라 data와 technology를 monetization하는 platform이다.

**당시 근거**

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

**이 주장이 성립하려면**

data scale·analytics가 pricing/care/services로 재사용

**사전 반증조건**

technology edge가 commodity화

**실제 결과**

Optum의 거대한 services/data platform 성장으로 강하게 검증.

**정량적 괴리**

주가 / $53.73 / intrinsic $85 / 2008말 약 $26.6

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Technology/data edge 가설은 'technology edge가 commodity화'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Scale/network moat — 적중 · 논지 비중 18%

**당시 주장**

최대 national network와 low SG&A가 superior economics를 만든다.

**당시 근거**

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

**이 주장이 성립하려면**

network breadth·cost leverage 유지

**사전 반증조건**

scale diseconomy·provider backlash

**실제 결과**

UNH는 장기적으로 업계 최대급 수익성을 유지했다.

**정량적 괴리**

Meltdown floor / $45~60 / 하방 제한 / 실제 $30 아래

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Scale/network moat 가설은 'scale diseconomy·provider backlash'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. Risk+fee diversification — 장기 적중 · 논지 비중 16%

**당시 주장**

risk insurance와 fee-based operations 결합이 earnings quality를 높인다.

**당시 근거**

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

**이 주장이 성립하려면**

fee services growth

**사전 반증조건**

보험 shock이 그룹 전체를 지배

**실제 결과**

Optum 비중 확대가 diversification을 강화했다.

**정량적 괴리**

Business model / insurance+data/technology / services 확대 / 2023 Optum revenue $226.6bn

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Risk+fee diversification 가설은 '보험 shock이 그룹 전체를 지배'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. Options scandal — 부분 실패 · 논지 비중 16%

**당시 주장**

backdating 문제는 largely non-operational이고 가격에 충분히 반영됐다.

**당시 근거**

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

**이 주장이 성립하려면**

fines·governance 비용이 제한

**사전 반증조건**

governance shock이 multiple·management confidence를 크게 훼손

**실제 결과**

scandal 자체와 broader uncertainty가 valuation 부담을 오래 만들었다.

**정량적 괴리**

2023 Group scale / 장기 성장 기대 / platform compounding / Revenue $371.6bn, CFO $29.1bn

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

Options scandal 가설은 'governance shock이 multiple·management confidence를 크게 훼손'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. $85 intrinsic — 실패 · 논지 비중 16%

**당시 주장**

보수적 stress 후에도 $80~95 가치가 있다.

**당시 근거**

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

**이 주장이 성립하려면**

earnings growth와 normal multiple

**사전 반증조건**

multiple compression·MCR shock

**실제 결과**

원 horizon에서 $85에 도달하지 못하고 2008 급락.

**정량적 괴리**

약 $53.73→2007말 $58대였지만 2008말 약 $26.6으로 약 -50%. 장기적으로는 Optum 성장과 함께 사업가치가 크게 확대됐으나 원래 몇 년 투자경로는 실패.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

$85 intrinsic 가설은 'multiple compression·MCR shock'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. $45 meltdown floor — 치명적 실패 · 논지 비중 16%

**당시 주장**

최악에도 $45~60 정도라 손익비가 좋다.

**당시 근거**

UNH는 보험사가 아니라 superior technology로 healthcare data를 수집·정리·활용하는 health-tech company이며, 이를 risk insurance와 fee-based operations에 monetization한다고 주장했다. 규모·network·low SG&A·data advantage가 high ROIC와 FCF를 만들고 options backdating scandal은 비운영적·일회성 이슈라고 봤다. 약 $1bn fines/taxes와 연 $200m additional SG&A까지 stress하고도 $80~95 가치, meltdown $45~60이라고 계산했다.

**이 주장이 성립하려면**

earnings·market multiple이 floor 유지

**사전 반증조건**

macro+sector+valuation tail 동시발생

**실제 결과**

실제 $30 아래로 내려가 floor가 크게 깨졌다.

**정량적 괴리**

약 $53.73→2007말 $58대였지만 2008말 약 $26.6으로 약 -50%. 장기적으로는 Optum 성장과 함께 사업가치가 크게 확대됐으나 원래 몇 년 투자경로는 실패.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

$45 meltdown floor 가설은 'macro+sector+valuation tail 동시발생'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

장기 business-model insight는 매우 훌륭했다. 훗날 Optum은 health, insight, Rx를 아우르는 거대한 services/data platform으로 성장했고 2023 Optum revenue는 약 $226.6bn이었다. 그러나 투자경로는 심각하게 틀렸다. 2007~08 options scandal, medical-cost/political concerns와 금융위기 속에서 UNH 주가는 2008말 약 $26.6까지 떨어져 원문 meltdown floor $45를 크게 하회했다. 2008 revenue는 $81bn+로 성장하고 cash flow도 유지됐지만 multiple/path가 훨씬 나빴다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 약 $53.73→2007말 $58대였지만 2008말 약 $26.6으로 약 -50%. 장기적으로는 Optum 성장과 함께 사업가치가 크게 확대됐으나 원래 몇 년 투자경로는 실패. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

기업의 본질에 대한 통찰과 주식의 downside distribution을 분리해야 하는 사례다. 'technology/data platform'이라는 추상화는 15년 후 Optum으로 강하게 검증됐지만, options scandal이 non-operational이므로 downside가 작다는 결론은 과도했다. managed-care cycle, MCR, politics, recession과 multiple compression이 동시에 오는 joint tail을 모델링하지 않았다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-01-23 — 2008년 들어 managed-care 의료비·정책·시장 우려와 valuation compression이 본격화되며 주가가 원문 meltdown range로 빠르게 접근. 이후 금융위기에서 $45 floor도 붕괴했다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 높음. 장기 business thesis를 유지하더라도 $45~60 downside floor가 깨지는 순간 valuation distribution과 position size를 다시 설정했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

중기 투자 실패·장기 사업모델 통찰은 탁월. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $53.73 | intrinsic $85 | 2008말 약 $26.6 | 중기 실패 |
| Meltdown floor | $45~60 | 하방 제한 | 실제 $30 아래 | 하방 분석 실패 |
| Business model | insurance+data/technology | services 확대 | 2023 Optum revenue $226.6bn | 장기 강한 적중 |
| 2023 Group scale | 장기 성장 기대 | platform compounding | Revenue $371.6bn, CFO $29.1bn | 장기 검증 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2006-12-30 | VIC 아이디어 게시 | Healthcare technology/data platform·$85 intrinsic Long |
| 2008-01-23 | 최초 핵심 검증·반증 신호 | 2008년 들어 managed-care 의료비·정책·시장 우려와 valuation compression이 본격화되며 주가가 원문 meltdown range로 빠르게 접근. 이후 금융위기에서 $45 floor도 붕괴했다. |
| 2008-12-31 | 금융위기·managed-care repricing | 주가가 2006~07 VIC의 downside range를 크게 하회 |
| 2010-12-31 | 사업 회복 점검 | underlying franchise는 살아 있었지만 원 security horizon과 path는 실패 |
| 2023-12-31 | Optum 장기검증 | 2023 Group revenue $371.6bn, Optum scale 확대, CFO $29.1bn |
| 2024-01-31 | 고정 평가기준일 | 약 $53.73→2007말 $58대였지만 2008말 약 $26.6으로 약 -50%. 장기적으로는 Optum 성장과 함께 사업가치가 크게 확대됐으나 원래 몇 년 투자경로는 실패. |

### Failure / Success Anatomy

- **근본 오류:** 장기 franchise quality에서 단기 valuation floor·path risk로 넘어갈 때 joint-tail을 과소평가
- **최초 검증·반증 신호:** 2008-01-23 — 2008년 들어 managed-care 의료비·정책·시장 우려와 valuation compression이 본격화되며 주가가 원문 meltdown range로 빠르게 접근. 이후 금융위기에서 $45 floor도 붕괴했다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 높음. 장기 business thesis를 유지하더라도 $45~60 downside floor가 깨지는 순간 valuation distribution과 position size를 다시 설정했어야 한다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** data_network_effect; scale_advantage; fee_risk_diversification; optum_platform; cash_compounding
- **실패·주의 패턴:** downside_distribution; medical_cost_cycle; multiple_compression; derivative_path_risk; governance_shock

### 주요 근거자료

- [1. VIC UNH 2006-12-30 원문](https://www.valueinvestorsclub.com/idea/UnitedHealth_Group/4016278495) — Value Investors Club, 2006-12-30. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. UnitedHealth board review of stock option practices](https://www.sec.gov/Archives/edgar/data/731766/000119312506207894/dex991.htm) — UnitedHealth/SEC, 2006-10-15. options backdating review와 restatement 배경 확인
- [3. UnitedHealth 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000119312507046861/d10k.htm) — SEC, 2007-03-01. 2006 사업구조·options restatement·재무 확인
- [4. SEC settlement with former UnitedHealth CEO William McGuire](https://www.sec.gov/news/press/2007/2007-255.htm) — SEC, 2007-12-06. options scandal settlement·$468m 관련 확인
- [5. UnitedHealth FY2008 results](https://www.sec.gov/Archives/edgar/data/731766/000119312509009268/dex991.htm) — UnitedHealth/SEC, 2009-01-21. 2008 revenue·adjusted EPS·cash flow 확인
- [6. UnitedHealth 2009 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000119312510027229/d10k.htm) — SEC, 2010-02-11. 2009 buyback·사업상태 확인
- [7. UnitedHealth 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176624000081/unh-20231231.htm) — SEC, 2024-02-28. 2023 UHC·Optum segment scale, MCR, cash flow 장기검증
- [8. UnitedHealth FY2023 results](https://www.sec.gov/Archives/edgar/data/731766/000073176624000023/a2023q4exhibit991.htm) — UnitedHealth/SEC, 2024-01-12. 2023 revenue $371.6bn, operating earnings $32.4bn, CFO $29.1bn 확인
- [9. UnitedHealth historical prices](https://www.digrin.com/stocks/detail/UNH/price) — Digrin, 2024-01-31. 역사적 가격 교차검증


---

<!-- idea:df94c27f-7d04-4bd2-91e1-aec334afc9a1 -->
## 2. 2007-12-20 — 12~15% FCF/share·$85~100 2010·LEAPS Long

### 결론부터

**종합판정: 명백한 실패.** 좋은 compounder를 맞혀도 옵션의 strike와 만기가 틀리면 투자성과는 실패한다. 이 글은 FCF/share와 buyback math는 합리적이었지만 2년 내 rerating이 필요하다는 path dependency를 과소평가했다. LEAPS는 장기 질적 확신을 단기 timing risk로 바꾸는 레버리지였다.

**주가·증권 결과:** $58.11→2008말 약 $26.6(-54%). Jan-2010 $50 strike LEAPS의 breakeven $65.70을 크게 밑돌아 파생상품 thesis는 심각한 실패.

**Thesis / Process 점수:** 5.7 / 5.8

### 1. 무슨 기업인가

UnitedHealth Group는 UnitedHealthcare와 Optum을 결합한 미국 최대급 통합 health-care 기업이다. UnitedHealthcare는 commercial, Medicare, Medicaid 등 risk-bearing 보험과 fee-based employer 서비스를 제공하고, Optum은 Optum Health, Optum Insight, Optum Rx를 통해 care delivery, data/analytics, technology, pharmacy benefit 서비스를 제공한다. 이 구조는 보험의 underwriting cash flow와 fee-based·service earnings를 결합한다. 보험에서는 medical care ratio(MCR), pricing, member mix, reserves가 핵심이고 Optum에서는 고객수·revenue·operating margin·care delivery scale이 중요하다. 2006 VIC 작성자가 UNH를 단순 보험사가 아니라 'healthcare technology/data company'라고 본 통찰은 훗날 Optum의 성장으로 강하게 검증됐다. 다만 business quality가 높더라도 옵션 백데이팅, 의료비 trend, 정치·규제, recession, multiple compression과 파생상품의 만기 같은 경로위험이 주식성과를 크게 바꿀 수 있다.

### 2. 산업 가치사슬과 돈의 흐름

UnitedHealthcare는 premium·fee revenue에서 medical costs와 operating costs를 차감해 수익을 낸다. Optum은 PBM script economics, data/technology fees, care delivery·value-based care 등 여러 서비스 수익원을 제공한다. 규모가 커질수록 provider network 협상력, data density, SG&A leverage와 cross-selling이 강화될 수 있다. 그러나 정부사업 비중이 크기 때문에 Medicare/Medicaid reimbursement와 medical cost trend가 빠르게 바뀔 수 있다. 투자자는 revenue growth보다 MCR, operating cost ratio, Optum earnings, cash flow from operations, share count, repurchase price와 규제환경을 함께 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

UNH의 핵심 우위는 규모·provider network·data·technology·brand·distribution·Optum 서비스의 통합이다. 이 결합은 보험만 하는 경쟁사보다 고객 접점과 수익원이 넓고, data를 pricing·care management·fraud detection·provider performance에 재사용할 수 있게 한다. 그러나 이러한 장기 moat가 단기 valuation floor를 보장하지는 않는다. 2007~08 사례처럼 earnings가 완전히 무너지지 않아도 MCR 우려·정치리스크·금융시장 shock과 multiple compression으로 equity와 LEAPS가 크게 손실날 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

### 5. 밸류에이션과 기대수익의 연결

2008 FCF $4.92/share, EPS $4.00; 2009 FCF $5.41, EPS $4.50; 2010 EPS >$5. 15~18x + 약 $10 cash로 $85~100. Jan-2010 $50 strike LEAPS $15.70 추천, breakeven $65.70. 사후검증에서는 membership/ASO·risk mix 또는 Optum scale → MLR/MCR·operating margin → EPS/FCF → debt·buyback → 적용 multiple과 horizon 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. FCF/share compounding — 부분 · 논지 비중 18%

**당시 주장**

organic growth·cost savings·M&A로 FCF/share가 12~15% 성장한다.

**당시 근거**

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

**이 주장이 성립하려면**

medical margin과 operating cost 안정

**사전 반증조건**

MCR·earnings miss

**실제 결과**

2008 business는 현금창출을 유지했지만 예상 per-share trajectory에 못 미쳤다.

**정량적 괴리**

2008 revenue / $83bn / +9~10% / 약 $81bn+

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

FCF/share compounding 가설은 'MCR·earnings miss'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 2. Buyback — 부분 적중 · 논지 비중 18%

**당시 주장**

대규모 repurchase가 share count를 빠르게 줄여 EPS/FCF를 증폭한다.

**당시 근거**

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

**이 주장이 성립하려면**

낮은 가격과 충분한 FCF

**사전 반증조건**

capital constraints·earnings miss

**실제 결과**

buyback은 이어졌지만 주가붕괴를 막지 못했다.

**정량적 괴리**

2008 EPS/FCF / $4.00 / $4.92 / 성장 / adjusted EPS 약 $2.95, CFO 약 $4.8bn

**분석 오류·핵심**

해당 causal chain은 실제 사업수치에서 확인됐지만 valuation과 security path는 독립적으로 계속 재검증해야 한다.

**재사용할 교훈**

Buyback 가설은 'capital constraints·earnings miss'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 3. 2008/09 forecasts — 부분 실패 · 논지 비중 16%

**당시 주장**

2008 revenue $83bn, EPS $4 / 2009 EPS $4.50이 가능하다.

**당시 근거**

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

**이 주장이 성립하려면**

medical trend와 membership 양호

**사전 반증조건**

pricing lag·MCR 악화

**실제 결과**

revenue는 근접했지만 earnings 기대는 미달했다.

**정량적 괴리**

2010 target / $85~100 / 15~18x / 2010초 훨씬 미달

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

2008/09 forecasts 가설은 'pricing lag·MCR 악화'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 4. MLR/political risk — 확률 오판 · 논지 비중 16%

**당시 주장**

MLR 상승·Medicare cut·single payer를 risk로 알지만 base probability는 낮다.

**당시 근거**

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

**이 주장이 성립하려면**

pricing·policy 안정

**사전 반증조건**

risk가 동시에 확대

**실제 결과**

managed-care sentiment와 medical-cost 우려가 실제 valuation을 압박했다.

**정량적 괴리**

LEAPS / $50 strike @ $15.70 / breakeven $65.70 / 만기 전 breakeven 미회복

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

MLR/political risk 가설은 'risk가 동시에 확대'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 5. $85~100 valuation — 실패 · 논지 비중 16%

**당시 주장**

2010 EPS>$5와 15~18x로 $85~100이 가능하다.

**당시 근거**

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

**이 주장이 성립하려면**

multiple normalization

**사전 반증조건**

multiple compression 지속

**실제 결과**

2010 horizon 내 목표 미달.

**정량적 괴리**

$58.11→2008말 약 $26.6(-54%). Jan-2010 $50 strike LEAPS의 breakeven $65.70을 크게 밑돌아 파생상품 thesis는 심각한 실패.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

$85~100 valuation 가설은 'multiple compression 지속'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

#### 6. LEAPS path — 치명적 실패 · 논지 비중 16%

**당시 주장**

Jan-2010 $50 LEAPS는 13% stock 상승만 필요해 매력적이다.

**당시 근거**

UNH가 14x 2008 FCF, ROE 25%+인데 organic growth·tuck-in M&A·cost savings·buyback으로 earnings/FCF per share가 연 12~15% 성장한다고 봤다. 2006 이후 $8.7bn buyback으로 15%+ market cap을 환원했고 shares가 1.4bn→1.3bn→2008 <1.2bn으로 줄 것이라 예상했다. 2008 revenue 9~10% 증가해 $83bn, EPS $4.00/FCF $4.92, 2010 EPS>$5와 15~18x multiple로 $85~100을 계산하고 LEAPS까지 추천했다.

**이 주장이 성립하려면**

2년 내 주가가 $65.70 이상

**사전 반증조건**

drawdown·rerating 지연

**실제 결과**

2008 crash로 breakeven을 크게 하회, path dependency가 치명적이었다.

**정량적 괴리**

$58.11→2008말 약 $26.6(-54%). Jan-2010 $50 strike LEAPS의 breakeven $65.70을 크게 밑돌아 파생상품 thesis는 심각한 실패.

**분석 오류·핵심**

평균적인 operating path를 증권가격·catalyst·multiple 경로에 직접 연결하거나, joint-tail을 충분히 stress하지 않았다.

**재사용할 교훈**

LEAPS path 가설은 'drawdown·rerating 지연'를 사전 반증조건으로 저장하고, 가격 목표 달성과 실제 원인 발생을 별도로 판정한다.

### 6. 실제 사업의 시간순 전개

2008 revenue는 약 $81bn으로 여전히 성장했고 회사는 profitable·cash generative했지만 주식과 derivative 경로는 완전히 실패했다. 주가는 2008말 약 $26.6으로 반토막 이하가 됐고, Jan-2010까지 $65.70 breakeven을 회복하지 못했다. Earnings quality가 완전히 사라진 것은 아니지만 MCR·political·economic uncertainty와 multiple compression이 buyback/FCF thesis를 압도했다.

### 7. 사업 결과와 가격 결과 분리

가격·증권 결과는 $58.11→2008말 약 $26.6(-54%). Jan-2010 $50 strike LEAPS의 breakeven $65.70을 크게 밑돌아 파생상품 thesis는 심각한 실패. 사업논지, 촉매논지, valuation multiple, 보유경로를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

좋은 compounder를 맞혀도 옵션의 strike와 만기가 틀리면 투자성과는 실패한다. 이 글은 FCF/share와 buyback math는 합리적이었지만 2년 내 rerating이 필요하다는 path dependency를 과소평가했다. LEAPS는 장기 질적 확신을 단기 timing risk로 바꾸는 레버리지였다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-04-22 — 2008년 실적 가이던스·medical cost와 managed-care sector valuation 우려가 커지며 주가가 급락, LEAPS breakeven 경로가 빠르게 훼손됐다. 이 시점에 medical cost/claims operations·EPS·capital allocation·multiple을 다시 계산하면 thesis의 어느 층이 맞고 틀렸는지 구분할 수 있었다. 회피 가능성: 매우 높음. 보통주 Long과 2010 LEAPS를 별도 thesis로 관리했다면 underlying 장기 quality를 믿더라도 옵션 position은 조기에 축소할 수 있었다.

### 10. 최종 판정·반사실·재사용 교훈

명백한 실패. Managed care에서는 ASO와 risk-bearing economics를 분리하고, operating forecast가 맞아도 catalyst·multiple·security horizon이 틀릴 수 있음을 항상 별도 stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2008 revenue | $83bn | +9~10% | 약 $81bn+ | 근접 |
| 2008 EPS/FCF | $4.00 / $4.92 | 성장 | adjusted EPS 약 $2.95, CFO 약 $4.8bn | EPS 미달 |
| 2010 target | $85~100 | 15~18x | 2010초 훨씬 미달 | 실패 |
| LEAPS | $50 strike @ $15.70 | breakeven $65.70 | 만기 전 breakeven 미회복 | 치명적 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2007-12-20 | VIC 아이디어 게시 | 12~15% FCF/share·$85~100 2010·LEAPS Long |
| 2008-04-22 | 최초 핵심 검증·반증 신호 | 2008년 실적 가이던스·medical cost와 managed-care sector valuation 우려가 커지며 주가가 급락, LEAPS breakeven 경로가 빠르게 훼손됐다. |
| 2008-12-31 | 금융위기·managed-care repricing | 주가가 2006~07 VIC의 downside range를 크게 하회 |
| 2010-12-31 | 사업 회복 점검 | underlying franchise는 살아 있었지만 원 security horizon과 path는 실패 |
| 2023-12-31 | Optum 장기검증 | 2023 Group revenue $371.6bn, Optum scale 확대, CFO $29.1bn |
| 2024-01-31 | 고정 평가기준일 | $58.11→2008말 약 $26.6(-54%). Jan-2010 $50 strike LEAPS의 breakeven $65.70을 크게 밑돌아 파생상품 thesis는 심각한 실패. |

### Failure / Success Anatomy

- **근본 오류:** 장기 franchise quality에서 단기 valuation floor·path risk로 넘어갈 때 joint-tail을 과소평가
- **최초 검증·반증 신호:** 2008-04-22 — 2008년 실적 가이던스·medical cost와 managed-care sector valuation 우려가 커지며 주가가 급락, LEAPS breakeven 경로가 빠르게 훼손됐다.
- **당시 알 수 있었나:** MLR/MCR, ASO/risk mix, customer/membership, claims operations, adjusted EPS, debt, cash flow, buyback, PBM client retention과 정책 이벤트는 공시·earnings에서 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. 보통주 Long과 2010 LEAPS를 별도 thesis로 관리했다면 underlying 장기 quality를 믿더라도 옵션 position은 조기에 축소할 수 있었다.
- **반사실 질문:** 사업 operating thesis가 맞더라도 촉매가 실패하거나 P/E가 rerating되지 않거나 만기 전 drawdown이 발생하면 이 증권의 기대수익은 여전히 충분한가?
- **성공 패턴:** data_network_effect; scale_advantage; fee_risk_diversification; optum_platform; cash_compounding
- **실패·주의 패턴:** downside_distribution; medical_cost_cycle; multiple_compression; derivative_path_risk; governance_shock

### 주요 근거자료

- [1. VIC UNH 2007-12-20 원문](https://www.valueinvestorsclub.com/idea/UnitedHealth_Group_Inc./6097830450) — Value Investors Club, 2007-12-20. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. UnitedHealth board review of stock option practices](https://www.sec.gov/Archives/edgar/data/731766/000119312506207894/dex991.htm) — UnitedHealth/SEC, 2006-10-15. options backdating review와 restatement 배경 확인
- [3. UnitedHealth 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000119312507046861/d10k.htm) — SEC, 2007-03-01. 2006 사업구조·options restatement·재무 확인
- [4. SEC settlement with former UnitedHealth CEO William McGuire](https://www.sec.gov/news/press/2007/2007-255.htm) — SEC, 2007-12-06. options scandal settlement·$468m 관련 확인
- [5. UnitedHealth FY2008 results](https://www.sec.gov/Archives/edgar/data/731766/000119312509009268/dex991.htm) — UnitedHealth/SEC, 2009-01-21. 2008 revenue·adjusted EPS·cash flow 확인
- [6. UnitedHealth 2009 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000119312510027229/d10k.htm) — SEC, 2010-02-11. 2009 buyback·사업상태 확인
- [7. UnitedHealth 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176624000081/unh-20231231.htm) — SEC, 2024-02-28. 2023 UHC·Optum segment scale, MCR, cash flow 장기검증
- [8. UnitedHealth FY2023 results](https://www.sec.gov/Archives/edgar/data/731766/000073176624000023/a2023q4exhibit991.htm) — UnitedHealth/SEC, 2024-01-12. 2023 revenue $371.6bn, operating earnings $32.4bn, CFO $29.1bn 확인
- [9. UnitedHealth historical prices](https://www.digrin.com/stocks/detail/UNH/price) — Digrin, 2024-01-31. 역사적 가격 교차검증


---

# 배치 공통 학습

1. **Managed care는 short-tail이라고 low-risk가 아니다.** Cigna 2001~02처럼 claims system이 medical-cost visibility를 망가뜨리면 다음 pricing cycle 전에 membership·MLR·customer satisfaction이 동시에 훼손될 수 있다.
2. **ASO와 risk-bearing 보험을 반드시 분리한다.** ASO는 employer가 claims를 부담하므로 규제·medical trend downside가 다르지만, 운영서비스 품질과 고객유지 위험은 남는다.
3. **가격 성공과 촉매 성공을 분리한다.** 2009 Cigna는 PBM 매각이 없었는데도 목표가를 달성했다. 이 사례를 'PBM sale 분석 성공'으로 저장하면 잘못 학습한다.
4. **EPS를 맞히는 것과 주가를 맞히는 것은 별개다.** 2019 Cigna의 2021 EPS $20~21 전망은 실제 $20.47로 거의 완벽했지만 $350 target은 실패했다.
5. **목표가에 날짜가 붙으면 multiple path도 thesis다.** 2021 Cigna는 2021/22 EPS를 거의 정확히 맞혔지만 $300은 약 1년 늦게 왔다.
6. **SOTP는 crystallization mechanism이 필요하다.** 2022 Cigna에서 Evernorth·Healthcare에 peer multiple을 붙였다고 시장이 1년 안에 같은 multiple을 줄 이유는 없었다.
7. **장기 기업 통찰과 증권 payoff를 분리한다.** 2006 UNH의 technology/data platform 통찰은 Optum으로 놀랍게 적중했지만 2008 주가는 meltdown floor보다 훨씬 아래로 내려갔다.
8. **LEAPS는 장기 질적 확신을 단기 timing risk로 바꾼다.** 2007 UNH 사례처럼 좋은 기업도 만기 전 multiple compression이면 파생상품 성과는 실패한다.
