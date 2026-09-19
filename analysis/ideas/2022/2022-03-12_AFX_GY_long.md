# Carl Zeiss Meditec AG (AFX.GY) — 2022-03-12 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Carl Zeiss Meditec AG / AFX.GY |
| VIC 게시일 / 작성자 | 2022-03-12 / taiidea |
| 분석 증권 / 실제 방향 | Xetra:AFX common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 €151 |
| 기대기간 | 2025 earnings realization |
| raw horizon audit | base €263 / bull €514; VisuMax installed base, consumables와 premium IOL compounding |
| 최종 판정 | **강한 실패 — product moat 생존, earnings duration·multiple 붕괴** |

> **결론:** SMILE·VisuMax franchise와 recurring revenue 논리는 살아 있지만 원문의 earnings·margin·multiple 경로는 실패했다. FY2024/25 revenue €2.228bn에도 EBITA margin은 11.6%, EPS €1.61이었고 H1 FY2025/26 adjusted margin은 6.1%, EPS €0.17로 악화됐다. €151 entry에서 high-€20s 가격은 operating moat가 entry valuation을 구제하지 못했음을 보여준다.

---

## 1. 회사는 정확히 무엇을 하는가

Carl Zeiss Meditec는 ophthalmology와 microsurgery 장비·소모품을 판매한다. VisuMax 설치장비는 SMILE 시술용 patient interface와 service를, IOL 사업은 수술 건수와 premium mix를 recurring revenue로 바꾼다. 장비 출하·소모품 mix·R&D와 규제 품질비용이 EBITA를 좌우한다.

device volume×ASP + installed base×procedure/consumable revenue - manufacturing·R&D·SG&A·quality cost - tax - capex = equity FCF; recurring mix와 acquisition amortization을 분리한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

VisuMax installed base, SMILE procedures, recurring revenue mix, IOL volume/mix, order intake, gross margin, EBITA margin, R&D ratio, FCF, EPS

---

## 2. 당시 상황과 시장이 가격에 넣은 것

약 1,500대 VisuMax installed base와 SMILE procedure consumables, 신형 VisuMax 800 replacement cycle, premium IOL mix가 장기간 두 자릿수 성장과 높은 incremental margin을 만든다는 논지였다. sell-side가 order intake와 APAC adoption을 과소평가해 base €263, bull €514 rerating을 기대했다.

### Reverse expectations

시장은 elective procedure·China/APAC 규제와 procurement, device order volatility, IOL product quality·mix, R&D 부담과 이미 높은 duration multiple을 할인했다. installed base가 커도 시술 utilization·consumable price와 device cycle이 동시에 둔화될 수 있다.

---

## 3. 원문 투자논지 지도

### C1. SMILE razor-and-blade — 부분 성공

**원문 주장**

VisuMax 설치가 procedure consumables를 누적한다.

**경제적 메커니즘**

installed base×utilization이 recurring revenue와 high margin을 만든다.

**T0 근거**

약 1,500대 installed base와 procedure model.

**숨은 가정**

utilization·pricing·clinical adoption이 계속 오른다.

**사전 반증조건**

recurring mix·procedure growth가 정체되면 반증.

**실제 결과**

H1 FY25/26 recurring revenue는 49.9%였으나 total earnings가 약화됐다.

**정량 gap**

recurring mix 존재·profit 보호 실패.

**분석 오류 또는 제한**

recurring을 recession-proof로 봤다.

**재사용 교훈**

installed base와 utilization을 따로 추적한다.

### C2. VisuMax 800 replacement cycle — 부분 성공

**원문 주장**

빠른 신형 장비가 installed base 교체·확장을 촉진한다.

**경제적 메커니즘**

throughput 개선이 surgeon ROI와 placements를 높인다.

**T0 근거**

제품 출시·order intake.

**숨은 가정**

capital budgets와 approvals가 원활하다.

**사전 반증조건**

device shipments·orders 약세면 반증.

**실제 결과**

제품은 출시됐지만 2025/26 diagnostic device shipments가 계획보다 낮았다.

**정량 gap**

product success≠forecast success.

**분석 오류 또는 제한**

출시를 매출로 즉시 환산했다.

**재사용 교훈**

orders·shipment·installation·utilization을 구분한다.

### C3. premium IOL compounding — 실패

**원문 주장**

premium mix와 APAC 수요가 성장·margin을 높인다.

**경제적 메커니즘**

higher ASP lenses가 recurring surgical revenue를 키운다.

**T0 근거**

portfolio와 demographic demand.

**숨은 가정**

tender·quality·channel risk가 낮다.

**사전 반증조건**

recall·tender exclusion·mix 악화면 반증.

**실제 결과**

2025/26 bifocal IOL tender exclusion·channel recall과 unfavorable mix가 earnings를 눌렀다.

**정량 gap**

H1 adj margin 6.1%.

**분석 오류 또는 제한**

product/regulatory downside를 과소평가했다.

**재사용 교훈**

IOL는 country·tender·SKU별로 stress한다.

### C4. multi-quarter earnings upgrades — 실패

**원문 주장**

order intake가 consensus 상향을 부른다.

**경제적 메커니즘**

backlog가 shipment와 EPS로 전환된다.

**T0 근거**

당시 order book +24% vs revenue +11%.

**숨은 가정**

cancellations·mix·cost가 안정적이다.

**사전 반증조건**

EPS·margin 하락이면 반증.

**실제 결과**

FY24/25 EPS €1.61, H1 FY25/26 EPS €0.17로 악화됐다.

**정량 gap**

upgrade가 아닌 downgrade path.

**분석 오류 또는 제한**

orders를 margin-adjusted revenue로 연결하지 않았다.

**재사용 교훈**

backlog conversion과 gross margin을 함께 본다.

### C5. APAC가 절반 이상 성장엔진 — 실패 구간

**원문 주장**

Asia adoption이 company growth를 가속한다.

**경제적 메커니즘**

SMILE·IOL penetration이 western maturity를 상쇄한다.

**T0 근거**

APAC exposure와 underpenetration.

**숨은 가정**

China procurement·FX·regulation이 우호적이다.

**사전 반증조건**

APAC decline이면 반증.

**실제 결과**

H1 FY25/26 APAC revenue는 -10.0%(-8.6% FX-adjusted)였다.

**정량 gap**

명확한 반증.

**분석 오류 또는 제한**

TAM을 realized demand로 봤다.

**재사용 교훈**

country별 volume·price·policy를 분리한다.

### C6. €263 base / €514 bull — 강한 실패

**원문 주장**

earnings growth와 premium multiple로 큰 upside가 난다.

**경제적 메커니즘**

higher EPS×quality multiple이 target를 만든다.

**T0 근거**

원문 valuation cases.

**숨은 가정**

margin이 확대되고 multiple이 유지된다.

**사전 반증조건**

EPS·margin·price가 동시 하락하면 실패.

**실제 결과**

주가는 high-€20s, margin·EPS도 미달했다.

**정량 gap**

base 대비 약 -90% 수준.

**분석 오류 또는 제한**

downside multiple과 duration을 과소평가했다.

**재사용 교훈**

target를 earnings와 multiple bridge로 분해한다.

---

## 4. 당시 Valuation과 Payoff Structure

installed devices×procedures/device×consumable contribution과 equipment replacement, IOL units·mix를 각각 모델링하고 R&D·SG&A·tax·capex를 빼 EPS·FCF로 연결해야 한다. €263/€514 target는 earnings와 multiple 기여를 분리하고 15~20% margin 하방에서 stress했어야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | China·IOL·device weakness, margin<10% | €30~60 | high-€20s |
| Base | SMILE·IOL compounding | €263 | 미실현 |
| Bull | VisuMax800·premium mix | €514 | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / base target | €151 / €263 | +74% | high-€20s | 강한 실패 |
| FY24/25 revenue | 고성장 | target path | €2,227.6m | scale 성장 |
| FY24/25 EBITA margin | high-teens 기대 | 확대 | 11.6% | 미달 |
| FY24/25 EPS | earnings compounding | 상승 | €1.61 | 미달 |
| H1 FY25/26 adj margin | 회복 | mid/high teens | 6.1% | 반증 |

### 촉매와 시간

판정 horizon은 **2025 earnings realization**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2022-03-12 | VIC Long | ~€151 |
| 2022 | VisuMax 800 rollout | product catalyst |
| 2023 | China·device normalization | duration pressure |
| 2024 | IOL/portfolio challenges | mix risk |
| 2025-09-30 | FY2024/25 close | margin 11.6% |
| 2025-12-11 | annual report | EPS €1.61 |
| 2026-05-12 | H1 results·restructuring | adj margin 6.1% |
| 2026-08 | 9M statement | adj margin 8.0% |

### 실제 사업·자본구조 추이

FY2024/25 revenue €2,227.6m, EBITA €257.7m, margin 11.6%, EPS €1.61, FCF €203.7m이었다. H1 FY2025/26 revenue €991.0m, adjusted EBITA €60.5m, margin 6.1%, EPS €0.17로 약해졌고 회사는 최대 1,000개 positions와 net savings >€160m p.a.를 포함한 구조조정을 제시했다. 9M adjusted margin은 8.0%였다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

약 €151에서 2026 high-€20s는 대략 80%+ price decline이다. exact trade date·dividends·tax ledger가 없으므로 total return·IRR은 계산하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | SMILE razor-and-blade | 20% | 부분 성공 | recurring mix 존재·profit 보호 실패. |
| C2 | VisuMax 800 replacement cycle | 18% | 부분 성공 | product success≠forecast success. |
| C3 | premium IOL compounding | 18% | 실패 | H1 adj margin 6.1%. |
| C4 | multi-quarter earnings upgrades | 16% | 실패 | upgrade가 아닌 downgrade path. |
| C5 | APAC가 절반 이상 성장엔진 | 16% | 실패 구간 | 명확한 반증. |
| C6 | €263 base / €514 bull | 12% | 강한 실패 | base 대비 약 -90% 수준. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

product innovation보다 earnings duration과 entry multiple이 payoff를 지배했다. China·IOL mix·장비 투자둔화와 cost base가 recurring growth를 상쇄했고, market은 long-duration quality multiple을 재평가했다.

### Counterfactual

revenue가 늘어도 EBITA margin이 8~12%, EPS가 €1.5 안팎이면 €151 entry에서 어떤 terminal multiple이 손실을 막을 수 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

installed base와 clinical moat를 predictable earnings duration으로 곧바로 번역했고 downside valuation, product-quality/regulatory shock와 fixed-cost deleverage를 작게 봤다.

### 최초로 관찰 가능했던 경고신호

FY2024/25 EPS가 €1.61에 그치고 EBITA margin이 11.6%로 내려간 시점이 base-case earnings path의 명확한 break였으며 H1 FY2025/26가 이를 확정했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

product moat와 entry-price moat는 별개다.

### Lesson 2

installed base는 procedures/device·consumable contribution으로 풀어야 한다.

### Lesson 3

high-duration medical devices에는 margin·multiple 동시 stress가 필요하다.

### Lesson 4

company restructuring은 과거 earnings-quality 가정의 반증일 수 있다.

### 지금 같은 아이디어를 다시 본다면

- VisuMax installed base
- procedures/device
- recurring mix
- IOL volume·recall
- China/APAC revenue
- gross·EBITA margin
- R&D ratio
- downside P/E·FCF

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | product moat 부분 성공 |
| Valuation thesis | entry 실패 |
| Catalyst thesis | upgrade cycle 실패 |
| Security payoff | common 적절 |
| Timing / path | 강한 실패 |
| Thesis score | 3.0/10 |
| Process score | 6.8/10 |
| 종합 | **강한 실패 — product moat 생존, earnings duration·multiple 붕괴** |

### 한 문장 교훈

> product moat와 entry-price moat는 별개다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2022-03-12. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Carl Zeiss Meditec FY2024/25 annual report](https://reports.zeiss.com/meditec-ag/2425/en/) — Carl Zeiss Meditec, 2025-12-11. Revenue €2,227.6m, EBITA €257.7m, EPS €1.61, FCF €203.7m 검증.
3. [H1 FY2025/26 results](https://www.zeiss.com/meditec-ag/en/media-news/press-releases/2026/half-year-financial-communication-2025-26.html) — Carl Zeiss Meditec, 2026-05-12. Revenue €991.0m, adjusted EBITA margin 6.1%, EPS €0.17와 restructuring 검증.
4. [9M FY2025/26 statement](https://www.zeiss.com/meditec-ag/en/media-news/press-releases/2026/statement-q3-fy-2025-26.html) — Carl Zeiss Meditec, 2026-08. 9개월 adjusted EBITA margin 8.0%와 outlook 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·제한적 price comparison만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
