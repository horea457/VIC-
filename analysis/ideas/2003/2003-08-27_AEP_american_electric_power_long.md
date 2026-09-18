# American Electric Power Company (AEP) — 2003-08-27 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | American Electric Power Company / AEP |
| VIC 게시일 / 작성자 | 2003-08-27 / sameplot850 |
| 분석 증권 / 실제 방향 | AEP common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 원문 약 $27.50 |
| 기대기간 | 2005~2006 earnings normalization |
| raw horizon audit | Jan-2006 $37 target와 2006 EPS bridge |
| 최종 판정 | **강한 성공 — regulatory cash·asset sales·EPS와 목표가격이 대체로 실현** |

> **결론:** Enron 이후 merchant risk와 높은 debt를 할인한 entry에서 Texas stranded-cost recovery, 비핵심 매각, 비용절감과 regulated earnings 정상화가 순서대로 나타났다. 2006 ongoing EPS는 $2.71로 원문 $2.82에 4% 미달했지만 $37 목표는 2005년 말 종가 $37.09로 사실상 달성했다.

---

## 1. 회사는 정확히 무엇을 하는가

American Electric Power는 여러 주의 regulated electric utility와 당시 merchant generation·trading 자산을 보유했다. 규제 utility는 승인 rate base에 허용 ROE를 곱해 수익을 얻지만 fuel·stranded cost 회수의 시점은 주 규제기관·법원·securitization 구조에 달려 있다. merchant 사업은 전력가격과 spark spread에 노출된다.

`rate base × allowed ROE + merchant margin - interest - capex - tax = equity earnings/FCF`; regulatory recovery와 debt reduction을 별도 추적한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

regulated EPS, allowed ROE, rate-base growth, stranded-cost recovery cash, merchant exposure, asset-sale net proceeds, debt/capital, dividend coverage

---

## 2. 당시 상황과 시장이 가격에 넣은 것

AEP는 merchant trading 실패, 신용등급 압박, Texas restructuring 회수 불확실성과 과다부채 때문에 전형적인 utility보다 낮은 배수를 받았다. 원문은 $200m 비용절감, 최소 $1.4bn Texas 현금, 최소 $1bn merchant 자산매각, 2006 EPS $2.82와 배당을 연결해 Jan-2006 $37을 제시했다.

### Reverse expectations

시장은 stranded-cost true-up이 삭감·지연되고 merchant asset이 장부가 이하에 팔리며, 신용등급을 지키기 위한 equity 발행 또는 배당삭감이 common upside를 흡수할 가능성을 반영했다. 목표가가 되려면 규제·매각·비용절감·금리와 utility multiple이 동시에 크게 어긋나지 않아야 했다.

---

## 3. 원문 투자논지 지도

### C1. $200m cost reduction이 core earnings를 높인다 — 대체로 성공

**원문 주장**

$200m 구조적 비용절감이 EPS를 끌어올린다.

**경제적 메커니즘**

fixed O&M 감소가 regulated earnings와 credit metric을 개선한다.

**T0 근거**

원문 $200m program.

**숨은 가정**

절감액이 일회성·merchant 손실에 흡수되지 않는다.

**사전 반증조건**

ongoing O&M 또는 EPS가 개선되지 않으면 반증.

**실제 결과**

2006 ongoing EPS가 $2.71까지 정상화했다.

**정량 gap**

$2.82 target 대비 -$0.11/-3.9%.

**분석 오류 또는 제한**

gross saving을 after-tax EPS로 직접 환산했다.

**재사용 교훈**

cost program은 gross·net·one-time cost를 분리한다.

### C2. Texas true-up에서 최소 $1.4bn 현금 — 강한 성공

**원문 주장**

regulatory stranded cost를 securitize해 cash를 회수한다.

**경제적 메커니즘**

확정 regulatory claim을 저금리 채권으로 바꿔 debt를 낮춘다.

**T0 근거**

원문 최소 $1.4bn 회수.

**숨은 가정**

PUCT·법원결정과 financing market이 허용한다.

**사전 반증조건**

승인액이 크게 삭감되거나 securitization이 지연되면 반증.

**실제 결과**

2006 공시에 Texas securitization과 관련 현금화가 반영됐다.

**정량 gap**

방향·규모가 thesis를 지지.

**분석 오류 또는 제한**

legal entitlement와 현금입금 사이 기간위험을 단순화했다.

**재사용 교훈**

규제자산은 order·appeal·bond close·cash의 네 단계로 본다.

### C3. merchant asset sale로 최소 $1bn — 성공

**원문 주장**

비핵심 발전·trading 자산을 매각해 balance sheet를 정리한다.

**경제적 메커니즘**

volatile EBITDA를 없애고 net proceeds로 leverage를 낮춘다.

**T0 근거**

원문 최소 $1bn proceeds.

**숨은 가정**

buyer liquidity와 자산가치가 유지된다.

**사전 반증조건**

매각손실·지연 또는 proceeds가 debt 감소로 이어지지 않으면 반증.

**실제 결과**

2004~05 매각과 사업축소가 진행됐다.

**정량 gap**

정확한 동일자산 합계보다 방향이 확인됨.

**분석 오류 또는 제한**

headline value와 after-tax net cash를 혼용할 위험.

**재사용 교훈**

asset sale은 net cash/debt 비율로 검증한다.

### C4. deleveraging이 utility multiple을 회복 — 성공

**원문 주장**

회수·매각 현금이 rating risk를 낮춘다.

**경제적 메커니즘**

credit spread와 equity risk premium이 내려가면 P/E가 정상화된다.

**T0 근거**

높은 debt와 rating pressure가 할인 원인.

**숨은 가정**

회수현금이 capex·배당에 소비되지 않는다.

**사전 반증조건**

debt/capital과 rating이 개선되지 않으면 반증.

**실제 결과**

risk profile이 regulated utility 중심으로 이동하고 목표배수가 실현됐다.

**정량 gap**

$37 target를 2005말 달성.

**분석 오류 또는 제한**

multiple 회복을 금리·sector rerating과 완전히 분리하지 못했다.

**재사용 교훈**

deleveraging과 market beta 기여를 따로 기록한다.

### C5. 2006 EPS $2.82 — 거의 성공

**원문 주장**

비용절감·이자감소·regulated earnings로 $2.82를 번다.

**경제적 메커니즘**

operating improvement와 lower debt가 주당이익에 결합한다.

**T0 근거**

원문 2006 model.

**숨은 가정**

share count와 정상화 조정이 안정적이다.

**사전 반증조건**

ongoing EPS가 10% 이상 미달하면 반증.

**실제 결과**

2006 ongoing EPS $2.71.

**정량 gap**

-$0.11/-3.9%.

**분석 오류 또는 제한**

point estimate의 오차범위를 제시하지 않았다.

**재사용 교훈**

EPS target는 ±10% band와 bridge로 판정한다.

### C6. Jan-2006 $37 target — 성공

**원문 주장**

$27.50에서 $37과 배당을 기대한다.

**경제적 메커니즘**

EPS 정상화와 P/E rerating이 price를 만든다.

**T0 근거**

2006E EPS × 약 13배.

**숨은 가정**

촉매가 horizon 내 실현된다.

**사전 반증조건**

2005~06 가격이 $37에 도달하지 못하면 실패.

**실제 결과**

2005말 공시 종가 $37.09.

**정량 gap**

price target 사실상 일치.

**분석 오류 또는 제한**

배당포함 IRR과 point-in-time target hit을 구분해야 한다.

**재사용 교훈**

target hit·holding-period return·total return을 각각 기록한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 bridge는 2006 EPS $2.82에 약 13배를 적용해 $37을 산출했다. 이 접근은 EPS를 regulated core, merchant, asset-sale gain으로 분리하고, 회수 현금이 순부채를 낮추는 만큼만 multiple을 정상화해야 한다. 2006 ongoing EPS $2.71과 2005말 $37.09는 earnings·multiple 두 축이 모두 대체로 맞았음을 보여준다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | Texas 회수 삭감·매각지연·rating pressure | $20대·배당위험 | 현실화하지 않음 |
| Base | $200m 절감·$2bn+ 현금화·EPS 정상화 | $37 | 2005말 $37.09 |
| Bull | merchant 가격·utility multiple 동시개선 | $40+와 배당 | 배당 포함 upside 존재 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / target | $27.50 / $37 | +34.5%+배당 | 2005말 $37.09 | 성공 |
| 2006 ongoing EPS | T0 $2.82 | $2.82 | $2.71 | -3.9% |
| Texas cash | ≥$1.4bn | securitization | 공시상 실행 | 성공 |
| Merchant proceeds | ≥$1bn | debt reduction | 다년 매각 실행 | 성공 |
| 2Y price-only | Long | 상승 | +29.9% | 성공 |

### 촉매와 시간

판정 horizon은 **2005~2006 earnings normalization**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2003-08-27 | VIC Long 게시 | $27.50→$37 cleanup thesis |
| 2004 | 비핵심·merchant 매각 지속 | risk reduction |
| 2005-12-31 | 주가 $37.09 | target 달성 |
| 2006-01 | Texas true-up 관련 결정·financing | 규제 cash crystallization |
| 2006-08-04 | Q2 10-Q securitization 공시 | cash/debt bridge 확인 |
| 2006-12-31 | ongoing EPS $2.71 | $2.82에 근접 |
| 2007-01-25 | FY2006 results | thesis 수치 확정 |

### 실제 사업·자본구조 추이

AEP는 2003~05 비핵심·merchant 자산을 처분하고 비용구조를 낮췄다. Texas Central Company는 stranded-cost securitization으로 현금을 회수했으며 2006 10-Q에 관련 구조가 구체화됐다. FY2006 GAAP EPS $2.29, ongoing EPS $2.71을 기록했고 regulated utility 중심의 risk profile로 복귀했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

uploaded SQL price-only ratio는 1Y 1.1383, 2Y 1.2990, 3Y 1.2785, 5Y 1.3611이다. 즉 배당 제외로도 2년 약 +29.9%, 5년 약 +36.1%이며, 2005말 공시 종가 $37.09는 원문 $37 목표와 일치한다. 정확한 total return은 배당을 포함하지 않아 별도로 주장하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | $200m cost reduction이 core earnings를 높인다 | 20% | 대체로 성공 | $2.82 target 대비 -$0.11/-3.9%. |
| C2 | Texas true-up에서 최소 $1.4bn 현금 | 18% | 강한 성공 | 방향·규모가 thesis를 지지. |
| C3 | merchant asset sale로 최소 $1bn | 18% | 성공 | 정확한 동일자산 합계보다 방향이 확인됨. |
| C4 | deleveraging이 utility multiple을 회복 | 16% | 성공 | $37 target를 2005말 달성. |
| C5 | 2006 EPS $2.82 | 16% | 거의 성공 | -$0.11/-3.9%. |
| C6 | Jan-2006 $37 target | 12% | 성공 | price target 사실상 일치. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익은 고성장이 아니라 불확실성 제거에서 나왔다. regulatory receivable이 현금이 되고, merchant tail이 매각되며, credit risk가 낮아져 같은 regulated EPS에 더 정상적인 배수가 적용됐다.

### Counterfactual

Texas 회수가 절반으로 줄고 merchant 매각이 2년 늦어져도 배당·등급을 지키며 $37에 도달할 수 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

핵심 방향은 맞았지만 서로 독립적이지 않은 규제회수·매각·deleveraging을 base case에 함께 놓아 execution correlation을 작게 봤다.

### 최초로 관찰 가능했던 경고신호

명확한 thesis break는 없었다. 사전 핵심경고는 true-up 승인액 삭감 또는 securitization 지연이었으나 실제 현금화가 진행됐다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

regulated utility turnaround는 매출성장보다 regulatory receivable이 실제 현금과 debt reduction으로 바뀌는지를 본다.

### Lesson 2

asset-sale headline보다 net proceeds와 debt/capital 개선을 추적한다.

### Lesson 3

EPS target와 multiple target를 분리하면 어느 축이 수익을 만들었는지 보인다.

### 지금 같은 아이디어를 다시 본다면

- 규제명령의 승인액·appeal
- securitization closing
- asset-sale net cash
- ongoing vs GAAP EPS
- debt/capital·rating
- 배당 coverage

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 성공 |
| Valuation thesis | 성공 |
| Catalyst thesis | 강한 성공 |
| Timing / path | 성공 |
| Security selection | common 적절 |
| Thesis score | 9.5/10 |
| Process score | 9.6/10 |
| 종합 | **강한 성공 — regulatory cash·asset sales·EPS와 목표가격이 대체로 실현** |

### 한 문장 교훈

> regulated utility turnaround는 매출성장보다 regulatory receivable이 실제 현금과 debt reduction으로 바뀌는지를 본다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2003-08-27. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [AEP 2003 Form 10-K](https://www.sec.gov/Archives/edgar/data/4904/000000490404000055/form10k.txt) — SEC / American Electric Power, 2004-03-11. T0 직후 segment·debt·regulatory·asset-sale risk 검증.
3. [AEP 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/4904/000101540205001007/aep10k04.htm) — SEC / American Electric Power, 2005-03-01. cost reduction, merchant exit와 재무구조 진행 검증.
4. [AEP 2005 Form 10-K](https://www.sec.gov/Archives/edgar/data/4904/000000490406000034/ye05aep10k.htm) — SEC / American Electric Power, 2006-03-01. asset-sale proceeds·debt·EPS bridge 검증.
5. [AEP Q2 2006 Form 10-Q](https://www.sec.gov/Archives/edgar/data/4904/000000490406000148/q206aep10q.htm) — SEC / American Electric Power, 2006-08-04. Texas stranded-cost securitization과 현금회수 검증.
6. [AEP 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/4904/000000490407000041/ye06aep10k.htm) — SEC / American Electric Power, 2007-02-28. 2006 EPS·year-end 주가·사업구성 검증.
7. [AEP FY2006 earnings](https://www.aep.com/news/stories/view/892/AEP-reports-2006-fourthquarter-fullyear-earnings/) — American Electric Power, 2007-01-25. 2006 GAAP·ongoing EPS와 guidance 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B** — source SQL price-only ratios; dividends·tax 제외.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
