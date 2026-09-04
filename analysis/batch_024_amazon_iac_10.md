# Batch 024 — Amazon·IAC Platform & Capital Allocation 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Amazon 6건 · IAC 4건

## 결론부터

이번 배치는 **현재 이익이 아니라 미래의 business mix와 capital allocation을 분석해야 하는 경우**를 모았다.

- **Amazon:** 2010 Short는 media digitization이라는 한 현상은 맞혔지만 Amazon의 customer relationship이 retail→marketplace→cloud→advertising으로 확장되는 것을 놓쳤다. 2011·2016 Long은 reinvestment가 moat를 키운다는 점을 정확히 봤다. 2020 COVID Long도 크게 성공했다. 반면 2021·2022 Long은 사업 mix 분석은 좋았지만 starting valuation과 overcapacity 때문에 주가수익률은 훨씬 약했다.
- **IAC:** 2016~20 글들은 public stake를 빼면 residual stub이 0 또는 음수라는 점과 Barry Diller식 build-and-spin process를 이용했다. Match 2020 separation, Vimeo 2021 spin으로 핵심 catalyst가 실제 crystallize됐다.

> 데이터 경고: Amazon 6건과 선택한 IAC 4건은 원 SQL에서 모두 `is_short=true`다. 실제로 Amazon 2010만 Short이고 나머지는 Long 또는 hedged stub Long이다. raw flag는 보존하고 research direction을 교정한다.

---

# AMAZON.COM INC (AMZN) — 기업과 비즈니스

## 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

## 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2010-06-15 | Short | Short | Media digitization·Kindle/iPad·sales-tax Short | 2010-06 약 $5.46 → 2024-01 $155.20, 약 28배. 구조적 Short는 치명적으로 실패. | 치명적 실패 |
| 2011-12-17 | Short | Long | 5+ year reinvestment·growing moat Long | 2011-12 $8.66 → 2024-01 $155.20, 약 17.9배. 장기 thesis가 전설적으로 성공. | 전설적 성공 |
| 2016-08-04 | Short | Long | Inversion valuation·AWS/retail optionality Long | 2016-08 $38.46 → 2024-01 $155.20, 약 4.0배. | 매우 성공 |
| 2020-03-13 | Short | Long | COVID adoption acceleration·$1.53tn SOTP Long | 2020-03 $97.49 → 2021말 $166.72, +71%; 2024-01 $155.20, +59%. | 매우 성공 |
| 2021-03-31 | Short | Long | Retail $1.3tn + cheap AWS·ads/marketplace Long | 2021-03 $154.70 → 2024-01 $155.20, 가격은 사실상 보합. 2022에는 $84까지 큰 drawdown. | 사업논지 적중·증권수익률 미달 |
| 2022-01-11 | Short | Long | Investment-cycle normalization·~20% IRR Long | 2022-01 $149.57 → 2022말 $84(-44%), 2024-01 $155.20(+4%). 원문 ~20% annualized 목표 미달. | 사업회복 적중·IRR 실패 |

---

<!-- idea:562234b7-86f8-46a7-ae30-8928265b8c06 -->
## 1. 2010-06-15 — Media digitization·Kindle/iPad·sales-tax Short

### 결론부터

**종합판정: 치명적 실패.** 가장 큰 오류는 기존 상품 category의 쇠퇴를 customer relationship과 platform 전체의 쇠퇴로 등치한 것이다. Sales tax나 배송비 같은 단위 headwind도 selection·Prime·logistics density가 만드는 flywheel을 깨지 못했다.

**주가·증권 결과:** 2010-06 약 $5.46 → 2024-01 $155.20, 약 28배. 구조적 Short는 치명적으로 실패.

**Thesis / Process 점수:** 3.5 / 3.8

### 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

### 5. 밸류에이션과 기대수익의 연결

Media에 낮은 multiple, FX·shipping·sales-tax headwind와 Kindle slowdown을 반영하면 당시 growth valuation이 지속 불가하다고 봤다. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Media decline — 회사 수준 실패 · 논지 비중 18%

**당시 주장**

책·DVD·CD digitization이 Amazon 성장률을 훼손한다.

**당시 근거**

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

**이 주장이 성립하려면**

media mix가 계속 핵심

**사전 반증조건**

non-media/서비스 mix 급성장

**실제 결과**

media 중요도는 낮아지고 회사는 더 커졌다.

**정량적 괴리**

주가 / $5.46 / 하락 / 2024-01 $155.20

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

Media decline 가설은 'non-media/서비스 mix 급성장'를 반증조건으로 저장한다.

#### 2. Kindle disruption — 실패 · 논지 비중 18%

**당시 주장**

iPad가 Kindle과 Amazon digital 전략을 약화한다.

**당시 근거**

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

**이 주장이 성립하려면**

device 경쟁이 customer relationship을 지배

**사전 반증조건**

content/ecosystem이 device보다 중요

**실제 결과**

Kindle 경쟁은 있었지만 Amazon 전체에는 미미.

**정량적 괴리**

Media / 매출 절반+ / 구조적 drag / 회사 mix 급변

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

Kindle disruption 가설은 'content/ecosystem이 device보다 중요'를 반증조건으로 저장한다.

#### 3. Sales tax — 실패 · 논지 비중 16%

**당시 주장**

세금 advantage 소멸이 가격경쟁력을 훼손한다.

**당시 근거**

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

**이 주장이 성립하려면**

tax가 구매결정 핵심

**사전 반증조건**

selection/convenience가 세금효과 상쇄

**실제 결과**

사업 성장 지속.

**정량적 괴리**

AWS / 작은 사업 / 가치 미반영 / 2023 sales $90.8bn

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

Sales tax 가설은 'selection/convenience가 세금효과 상쇄'를 반증조건으로 저장한다.

#### 4. Shipping inflation — 실패 · 논지 비중 16%

**당시 주장**

배송비 상승이 구조적으로 margin을 압박한다.

**당시 근거**

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

**이 주장이 성립하려면**

density improvement 제한

**사전 반증조건**

network scale이 unit cost 개선

**실제 결과**

장기적으로 logistics가 moat가 됐다.

**정량적 괴리**

Ads/3P / 미성숙 / 낮은 중요도 / 2023 $46.9bn/$140.1bn

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

Shipping inflation 가설은 'network scale이 unit cost 개선'를 반증조건으로 저장한다.

#### 5. International FX — 부분 · 논지 비중 16%

**당시 주장**

유럽 FX가 earnings를 악화시킨다.

**당시 근거**

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

**이 주장이 성립하려면**

currency headwind 지속

**사전 반증조건**

local growth가 상쇄

**실제 결과**

단기 변수였을 뿐.

**정량적 괴리**

2010-06 약 $5.46 → 2024-01 $155.20, 약 28배. 구조적 Short는 치명적으로 실패.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

International FX 가설은 'local growth가 상쇄'를 반증조건으로 저장한다.

#### 6. Valuation collapse — 치명적 실패 · 논지 비중 16%

**당시 주장**

낮은 earnings multiple로 de-rate된다.

**당시 근거**

매출의 절반 이상이 books/DVD/CD 같은 media에서 나오는데 digitization이 이를 잠식하고, iPad가 Kindle을 약화시키며, 유럽 FX·배송비·인터넷 sales tax가 margin과 growth를 압박한다고 주장했다. Amazon을 당시 product mix의 온라인 소매업체로 보고 고성장 multiple이 과도하다는 Short였다.

**이 주장이 성립하려면**

business mix 고정

**사전 반증조건**

new high-margin pools

**실제 결과**

주가 28배.

**정량적 괴리**

2010-06 약 $5.46 → 2024-01 $155.20, 약 28배. 구조적 Short는 치명적으로 실패.

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

Valuation collapse 가설은 'new high-margin pools'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Media digitization 자체는 맞았지만 Amazon은 general merchandise, Prime, 3P marketplace, AWS와 advertising으로 이익 pool을 이동시켰다. 2023년 AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn으로 2010년에 작았거나 거의 보이지 않던 고마진 사업이 거대해졌다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2010-06 약 $5.46 → 2024-01 $155.20, 약 28배. 구조적 Short는 치명적으로 실패. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가장 큰 오류는 기존 상품 category의 쇠퇴를 customer relationship과 platform 전체의 쇠퇴로 등치한 것이다. Sales tax나 배송비 같은 단위 headwind도 selection·Prime·logistics density가 만드는 flywheel을 깨지 못했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-01-01 — AWS·3P·Prime이 media decline을 상쇄하며 Amazon의 경제적 실체가 '온라인 서점'에서 platform으로 이동하는 것이 명확해졌다. 회피 가능성: 매우 높음. non-media mix, 3P mix, Prime adoption과 AWS를 별도 segment처럼 추적했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

치명적 실패. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $5.46 | 하락 | 2024-01 $155.20 | 치명적 실패 |
| Media | 매출 절반+ | 구조적 drag | 회사 mix 급변 | claim만 부분 적중 |
| AWS | 작은 사업 | 가치 미반영 | 2023 sales $90.8bn | 치명적 누락 |
| Ads/3P | 미성숙 | 낮은 중요도 | 2023 $46.9bn/$140.1bn | 치명적 누락 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2010-06-15 | VIC 아이디어 게시 | Media digitization·Kindle/iPad·sales-tax Short |
| 2012-01-01 | 최초 검증·반증 신호 | AWS·3P·Prime이 media decline을 상쇄하며 Amazon의 경제적 실체가 '온라인 서점'에서 platform으로 이동하는 것이 명확해졌다. |
| 2015-12-31 | AWS economics 가시화 | retail 외 high-margin value pool이 독립적으로 중요해짐 |
| 2020-03-31 | COVID digital acceleration | e-commerce/cloud adoption 급가속 |
| 2023-12-31 | 효율회복 | 2023 OI $36.9bn, AWS OI $24.6bn |
| 2024-01-31 | 고정 평가기준일 | 2010-06 약 $5.46 → 2024-01 $155.20, 약 28배. 구조적 Short는 치명적으로 실패. |

### Failure / Success Anatomy

- **근본 오류:** 사업구조 또는 valuation state를 고정해 future mix/capital allocation/duration을 충분히 반영하지 않음
- **최초 검증·반증 신호:** 2012-01-01 — AWS·3P·Prime이 media decline을 상쇄하며 Amazon의 경제적 실체가 '온라인 서점'에서 platform으로 이동하는 것이 명확해졌다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 매우 높음. non-media mix, 3P mix, Prime adoption과 AWS를 별도 segment처럼 추적했어야 한다.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC AMZN 2010-06-15 원문](https://www.valueinvestorsclub.com/idea/AMAZON.COM_INC/4331713271) — Value Investors Club / user SQL, 2010-06-15. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Amazon 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) — SEC, 2024-02-02. 2023 매출·segment OI·3P/ads/AWS 수치
- [3. Amazon FY2023 results](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/amzn-20231231xex991.htm) — Amazon / SEC, 2024-02-01. 2023 sales와 profitability recovery 확인
- [4. Amazon historical prices](https://www.digrin.com/stocks/detail/AMZN/price) — Digrin, 2024-01-31. split-adjusted historical price path
- [5. Amazon Investor Relations](https://ir.aboutamazon.com/) — Amazon, 2024-01-31. annual reports·shareholder materials
- [6. Amazon segment tables FY2023](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R32.htm) — SEC, 2024-02-02. North America/International/AWS segment earnings

---

<!-- idea:28df417b-85fd-487f-b76c-610ed654ff0a -->
## 2. 2011-12-17 — 5+ year reinvestment·growing moat Long

### 결론부터

**종합판정: 전설적 성공.** 단기 margin보다 reinvestment의 목적과 결과를 봤고, customer-value flywheel을 회사의 확장 가능한 핵심으로 정의했다. 특정 상품이나 1년 EPS가 아니라 '어떤 capability에 돈을 쓰는가'를 본 점이 강했다.

**주가·증권 결과:** 2011-12 $8.66 → 2024-01 $155.20, 약 17.9배. 장기 thesis가 전설적으로 성공.

**Thesis / Process 점수:** 9.6 / 9.4

### 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

당기 EPS보다 5년+ free-cash-flow power와 moat 확대를 우선했다. 당시 약 $49bn sales와 global online-retail migration을 장기 value driver로 봤다. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Reinvestment — 강한 적중 · 논지 비중 18%

**당시 주장**

낮은 당기이익은 moat 확대를 위한 선택이다.

**당시 근거**

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

**이 주장이 성립하려면**

investment cohorts high ROI

**사전 반증조건**

매출 없이 CapEx만 누적

**실제 결과**

장기 scale·earnings 확대.

**정량적 괴리**

주가 / $8.66 / 5년+ compound / 2024-01 $155.20

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Reinvestment 가설은 '매출 없이 CapEx만 누적'를 반증조건으로 저장한다.

#### 2. E-commerce migration — 적중 · 논지 비중 18%

**당시 주장**

retail sales가 온라인으로 이동한다.

**당시 근거**

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

**이 주장이 성립하려면**

secular penetration 상승

**사전 반증조건**

offline resilience

**실제 결과**

장기 강한 tailwind.

**정량적 괴리**

Sales / ~$49bn / 세계 최대급 retailer / 2023 $574.8bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

E-commerce migration 가설은 'offline resilience'를 반증조건으로 저장한다.

#### 3. Prime flywheel — 적중 · 논지 비중 16%

**당시 주장**

Prime이 loyalty·frequency를 높인다.

**당시 근거**

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

**이 주장이 성립하려면**

member engagement

**사전 반증조건**

churn/low usage

**실제 결과**

핵심 ecosystem으로 성장.

**정량적 괴리**

AWS / 초기 / 큰 optionality / 2023 $90.8bn sales

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Prime flywheel 가설은 'churn/low usage'를 반증조건으로 저장한다.

#### 4. AWS optionality — 강한 적중 · 논지 비중 16%

**당시 주장**

cloud가 큰 독립 value pool이 된다.

**당시 근거**

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

**이 주장이 성립하려면**

developer adoption

**사전 반증조건**

commodity hosting

**실제 결과**

Amazon 최대 이익원으로 성장.

**정량적 괴리**

Operating income / 재투자로 낮음 / 장기 확대 / 2023 $36.9bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

AWS optionality 가설은 'commodity hosting'를 반증조건으로 저장한다.

#### 5. Global scale — 부분 적중 · 논지 비중 16%

**당시 주장**

국제확장이 selection·cost advantage를 키운다.

**당시 근거**

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

**이 주장이 성립하려면**

local execution

**사전 반증조건**

persistent losses

**실제 결과**

International 수익성은 느렸지만 규모 확대.

**정량적 괴리**

2011-12 $8.66 → 2024-01 $155.20, 약 17.9배. 장기 thesis가 전설적으로 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Global scale 가설은 'persistent losses'를 반증조건으로 저장한다.

#### 6. 5+ year compounder — 강한 적중 · 논지 비중 16%

**당시 주장**

moat가 넓어지며 장기 주가도 따라간다.

**당시 근거**

Bezos가 near-term earnings를 희생해 fulfillment, technology, selection과 customer experience에 재투자하고 있으며 시장이 이 비용을 영구적 저수익성으로 오해한다고 봤다. Prime, AWS, global e-commerce migration과 customer obsession이 moat를 더 넓힐 것이라고 주장했다.

**이 주장이 성립하려면**

FCF power 상승

**사전 반증조건**

capital returns decay

**실제 결과**

약 18배.

**정량적 괴리**

2011-12 $8.66 → 2024-01 $155.20, 약 17.9배. 장기 thesis가 전설적으로 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

5+ year compounder 가설은 'capital returns decay'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Amazon은 세계 최대급 retailer와 cloud provider로 성장했고 marketplace·ads가 추가됐다. 2023 sales $574.8bn, AWS operating income $24.6bn, consolidated operating income $36.9bn이었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2011-12 $8.66 → 2024-01 $155.20, 약 17.9배. 장기 thesis가 전설적으로 성공. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

단기 margin보다 reinvestment의 목적과 결과를 봤고, customer-value flywheel을 회사의 확장 가능한 핵심으로 정의했다. 특정 상품이나 1년 EPS가 아니라 '어떤 capability에 돈을 쓰는가'를 본 점이 강했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2013-12-31 — 매출·Prime·AWS 성장과 fulfillment scale이 동시에 확대되며 재투자가 단순 비용이 아니라 moat-building이라는 증거가 누적됐다. 회피 가능성: 해당 없음. 다만 장기보유 중 reinvestment ROI가 낮아지는지 계속 검증해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $8.66 | 5년+ compound | 2024-01 $155.20 | 강한 적중 |
| Sales | ~$49bn | 세계 최대급 retailer | 2023 $574.8bn | 강한 적중 |
| AWS | 초기 | 큰 optionality | 2023 $90.8bn sales | 강한 적중 |
| Operating income | 재투자로 낮음 | 장기 확대 | 2023 $36.9bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2011-12-17 | VIC 아이디어 게시 | 5+ year reinvestment·growing moat Long |
| 2013-12-31 | 최초 검증·반증 신호 | 매출·Prime·AWS 성장과 fulfillment scale이 동시에 확대되며 재투자가 단순 비용이 아니라 moat-building이라는 증거가 누적됐다. |
| 2015-12-31 | AWS economics 가시화 | retail 외 high-margin value pool이 독립적으로 중요해짐 |
| 2020-03-31 | COVID digital acceleration | e-commerce/cloud adoption 급가속 |
| 2023-12-31 | 효율회복 | 2023 OI $36.9bn, AWS OI $24.6bn |
| 2024-01-31 | 고정 평가기준일 | 2011-12 $8.66 → 2024-01 $155.20, 약 17.9배. 장기 thesis가 전설적으로 성공. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2013-12-31 — 매출·Prime·AWS 성장과 fulfillment scale이 동시에 확대되며 재투자가 단순 비용이 아니라 moat-building이라는 증거가 누적됐다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음. 다만 장기보유 중 reinvestment ROI가 낮아지는지 계속 검증해야 했다.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- 1. VIC AMZN 2011-12-17 원문 — Value Investors Club / user SQL, 2011-12-17. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Amazon 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) — SEC, 2024-02-02. 2023 매출·segment OI·3P/ads/AWS 수치
- [3. Amazon FY2023 results](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/amzn-20231231xex991.htm) — Amazon / SEC, 2024-02-01. 2023 sales와 profitability recovery 확인
- [4. Amazon historical prices](https://www.digrin.com/stocks/detail/AMZN/price) — Digrin, 2024-01-31. split-adjusted historical price path
- [5. Amazon Investor Relations](https://ir.aboutamazon.com/) — Amazon, 2024-01-31. annual reports·shareholder materials
- [6. Amazon segment tables FY2023](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R32.htm) — SEC, 2024-02-02. North America/International/AWS segment earnings

---

<!-- idea:24cb41f4-0650-48f5-b408-cca70bd66196 -->
## 3. 2016-08-04 — Inversion valuation·AWS/retail optionality Long

### 결론부터

**종합판정: 매우 성공.** 높은 headline multiple을 피하지 않고 earnings의 질과 재투자 후 normalized margin을 분해했다. 다만 2021 이후처럼 starting valuation이 너무 높아지면 같은 business thesis라도 security return이 낮아질 수 있다는 후속 교훈이 있다.

**주가·증권 결과:** 2016-08 $38.46 → 2024-01 $155.20, 약 4.0배.

**Thesis / Process 점수:** 9 / 8.1

### 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Cumulative GAAP income가 작다는 표면적 약점을 뒤집어 retail/AWS의 normalized economics와 장기 runway를 분리해 valuation했다. 핵심은 현재 P/E보다 hidden earnings power. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. GAAP inversion — 적중 · 논지 비중 18%

**당시 주장**

낮은 cumulative net income가 낮은 quality를 의미하지 않는다.

**당시 근거**

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

**이 주장이 성립하려면**

reinvestment earns returns

**사전 반증조건**

persistent low returns

**실제 결과**

후일 earnings power 확대.

**정량적 괴리**

주가 / $38.46 / 장기 실질수익 / 2024-01 $155.20

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

GAAP inversion 가설은 'persistent low returns'를 반증조건으로 저장한다.

#### 2. Retail scale — 적중 · 논지 비중 18%

**당시 주장**

selection/logistics scale이 durable moat다.

**당시 근거**

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

**이 주장이 성립하려면**

density/Prime 성장

**사전 반증조건**

competition erodes

**실제 결과**

장기 유지.

**정량적 괴리**

AWS / 고성장 / major value pool / 2023 OI $24.6bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Retail scale 가설은 'competition erodes'를 반증조건으로 저장한다.

#### 3. AWS value — 강한 적중 · 논지 비중 16%

**당시 주장**

AWS가 retail과 별도 고가치 platform이다.

**당시 근거**

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

**이 주장이 성립하려면**

cloud leadership

**사전 반증조건**

price commoditization

**실제 결과**

높은 이익원.

**정량적 괴리**

Ads / 초기 / option / 2023 sales $46.9bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

AWS value 가설은 'price commoditization'를 반증조건으로 저장한다.

#### 4. Optionality — 적중 · 논지 비중 16%

**당시 주장**

새 business line이 반복적으로 생긴다.

**당시 근거**

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

**이 주장이 성립하려면**

culture/capital allocation

**사전 반증조건**

innovation slows

**실제 결과**

ads 등 새 pool 출현.

**정량적 괴리**

3P services / 성장 / mix improvement / 2023 $140.1bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Optionality 가설은 'innovation slows'를 반증조건으로 저장한다.

#### 5. Capital allocation — 부분 적중 · 논지 비중 16%

**당시 주장**

재투자가 장기 FCF를 높인다.

**당시 근거**

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

**이 주장이 성립하려면**

Jassy/Bezos discipline

**사전 반증조건**

low-ROI expansion

**실제 결과**

2022 효율문제 있었지만 2023 회복.

**정량적 괴리**

2016-08 $38.46 → 2024-01 $155.20, 약 4.0배.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Capital allocation 가설은 'low-ROI expansion'를 반증조건으로 저장한다.

#### 6. Security return — 적중 · 논지 비중 16%

**당시 주장**

비싸 보여도 장기 return이 좋다.

**당시 근거**

시장도 Amazon을 좋아하기 시작했지만 여전히 GAAP net income만으로 평가하면 재투자 때문에 business quality를 놓친다고 봤다. Retail scale, Prime, AWS와 long-duration optionality가 inflation 이상의 실질수익을 제공하는 core holding이라고 주장했다.

**이 주장이 성립하려면**

growth exceeds multiple decay

**사전 반증조건**

valuation collapse

**실제 결과**

2024까지 약 4배.

**정량적 괴리**

2016-08 $38.46 → 2024-01 $155.20, 약 4.0배.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Security return 가설은 'valuation collapse'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2016 이후 AWS와 advertising이 빠르게 커졌고 retail fulfillment network도 확대됐다. 2023 AWS operating income $24.6bn, advertising sales $46.9bn, 3P seller services $140.1bn으로 earnings mix가 더 좋아졌다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2016-08 $38.46 → 2024-01 $155.20, 약 4.0배. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

높은 headline multiple을 피하지 않고 earnings의 질과 재투자 후 normalized margin을 분해했다. 다만 2021 이후처럼 starting valuation이 너무 높아지면 같은 business thesis라도 security return이 낮아질 수 있다는 후속 교훈이 있다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-12-31 — AWS와 3P/Prime economics가 consolidated earnings에서 더 선명해지며 'GAAP EPS가 business economics를 과소표현한다'는 주장 확인. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $38.46 | 장기 실질수익 | 2024-01 $155.20 | 강한 적중 |
| AWS | 고성장 | major value pool | 2023 OI $24.6bn | 강한 적중 |
| Ads | 초기 | option | 2023 sales $46.9bn | 강한 적중 |
| 3P services | 성장 | mix improvement | 2023 $140.1bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-08-04 | VIC 아이디어 게시 | Inversion valuation·AWS/retail optionality Long |
| 2018-12-31 | 최초 검증·반증 신호 | AWS와 3P/Prime economics가 consolidated earnings에서 더 선명해지며 'GAAP EPS가 business economics를 과소표현한다'는 주장 확인. |
| 2015-12-31 | AWS economics 가시화 | retail 외 high-margin value pool이 독립적으로 중요해짐 |
| 2020-03-31 | COVID digital acceleration | e-commerce/cloud adoption 급가속 |
| 2023-12-31 | 효율회복 | 2023 OI $36.9bn, AWS OI $24.6bn |
| 2024-01-31 | 고정 평가기준일 | 2016-08 $38.46 → 2024-01 $155.20, 약 4.0배. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2018-12-31 — AWS와 3P/Prime economics가 consolidated earnings에서 더 선명해지며 'GAAP EPS가 business economics를 과소표현한다'는 주장 확인.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC AMZN 2016-08-04 원문](https://www.valueinvestorsclub.com/idea/AMAZON.COM_INC/0950248237) — Value Investors Club / user SQL, 2016-08-04. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Amazon 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) — SEC, 2024-02-02. 2023 매출·segment OI·3P/ads/AWS 수치
- [3. Amazon FY2023 results](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/amzn-20231231xex991.htm) — Amazon / SEC, 2024-02-01. 2023 sales와 profitability recovery 확인
- [4. Amazon historical prices](https://www.digrin.com/stocks/detail/AMZN/price) — Digrin, 2024-01-31. split-adjusted historical price path
- [5. Amazon Investor Relations](https://ir.aboutamazon.com/) — Amazon, 2024-01-31. annual reports·shareholder materials
- [6. Amazon segment tables FY2023](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R32.htm) — SEC, 2024-02-02. North America/International/AWS segment earnings

---

<!-- idea:8375e33e-e8d3-4bec-b1d4-6e2f13fec089 -->
## 4. 2020-03-13 — COVID adoption acceleration·$1.53tn SOTP Long

### 결론부터

**종합판정: 매우 성공.** 행동변화와 digital adoption의 방향은 잘 맞혔고 SOTP로 high-margin segments를 분리했다. 다만 crisis tailwind를 영구 trend로 완전히 자본화하지 않고 subsequent capacity normalization을 별도 추적해야 했다.

**주가·증권 결과:** 2020-03 $97.49 → 2021말 $166.72, +71%; 2024-01 $155.20, +59%.

**Thesis / Process 점수:** 9 / 8.1

### 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

### 5. 밸류에이션과 기대수익의 연결

2019 기반 1P 6% net margin/30x, 3P 20%/35x, Ads 25%/35x, AWS 22%/50x로 SOTP 약 $1.53tn, 당시 약 $0.9tn 대비 70% upside. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. COVID e-commerce — 적중 · 논지 비중 18%

**당시 주장**

lockdown이 온라인 구매 adoption을 앞당긴다.

**당시 근거**

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

**이 주장이 성립하려면**

behavior persists

**사전 반증조건**

full reversal

**실제 결과**

강하게 현실화.

**정량적 괴리**

SOTP / $1.53tn / ~70% upside / 시장가치 빠른 상승

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

COVID e-commerce 가설은 'full reversal'를 반증조건으로 저장한다.

#### 2. AWS acceleration — 적중 · 논지 비중 18%

**당시 주장**

remote/digital workload가 cloud를 가속한다.

**당시 근거**

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

**이 주장이 성립하려면**

enterprise migration

**사전 반증조건**

IT cuts

**실제 결과**

장기 AWS 성장.

**정량적 괴리**

주가 / $97.49 / +70% 방향 / 2021말 $166.72

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

AWS acceleration 가설은 'IT cuts'를 반증조건으로 저장한다.

#### 3. 1P margin — 부분 · 논지 비중 16%

**당시 주장**

normalized 1P net margin 6%가 가능하다.

**당시 근거**

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

**이 주장이 성립하려면**

density/scale

**사전 반증조건**

labor/logistics inflation

**실제 결과**

2022 압박 후 2023 개선.

**정량적 괴리**

AWS / 2020 +35% 가정 / 가속 / 장기 고성장 지속

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

1P margin 가설은 'labor/logistics inflation'를 반증조건으로 저장한다.

#### 4. 3P/Ads margin — 적중 · 논지 비중 16%

**당시 주장**

fee/ads가 retail보다 높은 margin이다.

**당시 근거**

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

**이 주장이 성립하려면**

mix 상승

**사전 반증조건**

seller backlash

**실제 결과**

고마진 mix 확대.

**정량적 괴리**

Pandemic / digital adoption 가속 / stickiness / 일부 pull-forward

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

3P/Ads margin 가설은 'seller backlash'를 반증조건으로 저장한다.

#### 5. $1.53tn SOTP — 적중 · 논지 비중 16%

**당시 주장**

분리 valuation이 당시 $0.9tn보다 높다.

**당시 근거**

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

**이 주장이 성립하려면**

growth/multiples

**사전 반증조건**

normalization/multiple compression

**실제 결과**

단기 가치 실현.

**정량적 괴리**

2020-03 $97.49 → 2021말 $166.72, +71%; 2024-01 $155.20, +59%.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

$1.53tn SOTP 가설은 'normalization/multiple compression'를 반증조건으로 저장한다.

#### 6. Behavior stickiness — 부분 적중 · 논지 비중 16%

**당시 주장**

새 고객행동이 상당부분 남는다.

**당시 근거**

COVID가 e-commerce·cloud adoption을 가속하고 시장 급락이 Amazon을 좋은 entry로 만들었다고 봤다. 중국 SARS/lockdown 사례를 analog로 사용했고 1P, 3P, Ads, AWS를 분리해 normalized profit을 계산했다.

**이 주장이 성립하려면**

repeat usage

**사전 반증조건**

post-COVID normalization

**실제 결과**

완전 reversal은 아니나 일부 pull-forward.

**정량적 괴리**

2020-03 $97.49 → 2021말 $166.72, +71%; 2024-01 $155.20, +59%.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Behavior stickiness 가설은 'post-COVID normalization'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

팬데믹 기간 Amazon demand와 AWS usage가 급증했고 주가는 빠르게 상승했다. 다만 과잉 fulfillment investment가 2022 margin/FCF를 압박하면서 pandemic acceleration의 일부가 pull-forward였음도 드러났다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2020-03 $97.49 → 2021말 $166.72, +71%; 2024-01 $155.20, +59%. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

행동변화와 digital adoption의 방향은 잘 맞혔고 SOTP로 high-margin segments를 분리했다. 다만 crisis tailwind를 영구 trend로 완전히 자본화하지 않고 subsequent capacity normalization을 별도 추적해야 했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-06-30 — e-commerce와 AWS 수요 급증, Amazon hiring/fulfillment expansion으로 COVID acceleration thesis가 즉시 확인됐다. 회피 가능성: 해당 없음. 2021부터 fulfillment capacity와 demand normalization을 새 claim으로 추가해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| SOTP | $1.53tn | ~70% upside | 시장가치 빠른 상승 | 적중 |
| 주가 | $97.49 | +70% 방향 | 2021말 $166.72 | 적중 |
| AWS | 2020 +35% 가정 | 가속 | 장기 고성장 지속 | 적중 |
| Pandemic | digital adoption 가속 | stickiness | 일부 pull-forward | 부분 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-03-13 | VIC 아이디어 게시 | COVID adoption acceleration·$1.53tn SOTP Long |
| 2020-06-30 | 최초 검증·반증 신호 | e-commerce와 AWS 수요 급증, Amazon hiring/fulfillment expansion으로 COVID acceleration thesis가 즉시 확인됐다. |
| 2015-12-31 | AWS economics 가시화 | retail 외 high-margin value pool이 독립적으로 중요해짐 |
| 2020-03-31 | COVID digital acceleration | e-commerce/cloud adoption 급가속 |
| 2023-12-31 | 효율회복 | 2023 OI $36.9bn, AWS OI $24.6bn |
| 2024-01-31 | 고정 평가기준일 | 2020-03 $97.49 → 2021말 $166.72, +71%; 2024-01 $155.20, +59%. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2020-06-30 — e-commerce와 AWS 수요 급증, Amazon hiring/fulfillment expansion으로 COVID acceleration thesis가 즉시 확인됐다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음. 2021부터 fulfillment capacity와 demand normalization을 새 claim으로 추가해야 했다.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC AMZN 2020-03-13 원문](https://www.valueinvestorsclub.com/idea/AMAZON.COM_INC/5615632233) — Value Investors Club / user SQL, 2020-03-13. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Amazon 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) — SEC, 2024-02-02. 2023 매출·segment OI·3P/ads/AWS 수치
- [3. Amazon FY2023 results](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/amzn-20231231xex991.htm) — Amazon / SEC, 2024-02-01. 2023 sales와 profitability recovery 확인
- [4. Amazon historical prices](https://www.digrin.com/stocks/detail/AMZN/price) — Digrin, 2024-01-31. split-adjusted historical price path
- [5. Amazon Investor Relations](https://ir.aboutamazon.com/) — Amazon, 2024-01-31. annual reports·shareholder materials
- [6. Amazon segment tables FY2023](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R32.htm) — SEC, 2024-02-02. North America/International/AWS segment earnings

---

<!-- idea:ead61fcd-6231-401c-ac08-3a421bea511f -->
## 5. 2021-03-31 — Retail $1.3tn + cheap AWS·ads/marketplace Long

### 결론부터

**종합판정: 사업논지 적중·증권수익률 미달.** 사업의 mix shift는 놀랄 만큼 정확했지만 security analysis에서는 '좋은 자산을 싸게 산다'는 AWS residual valuation이 retail의 높은 standalone multiple에 의존했다. Business success와 stock return을 분리해야 한다.

**주가·증권 결과:** 2021-03 $154.70 → 2024-01 $155.20, 가격은 사실상 보합. 2022에는 $84까지 큰 drawdown.

**Thesis / Process 점수:** 7.5 / 8.1

### 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Retail을 장기 $2tn, 10% discount해 약 $1.3tn; 당시 전체 $1.5tn에서 AWS를 사실상 $200bn/4x sales에 산다고 봄. downside SOTP $1.7tn, 2024 marketplace+ads $200bn revenue×35% EBIT=$70bn, 20x=$1.4tn 가능. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Retail moat — 부분 · 논지 비중 18%

**당시 주장**

retail alone가 $1.3tn discounted value를 지지한다.

**당시 근거**

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

**이 주장이 성립하려면**

long-run margin/scale

**사전 반증조건**

capital intensity rises

**실제 결과**

business scale 유지, value estimate는 공격적.

**정량적 괴리**

주가 / $154.70 / upside / 2024-01 $155.20

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Retail moat 가설은 'capital intensity rises'를 반증조건으로 저장한다.

#### 2. AWS cheap residual — 부분 적중 · 논지 비중 18%

**당시 주장**

전체 valuation에서 AWS를 낮은 implied price에 산다.

**당시 근거**

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

**이 주장이 성립하려면**

retail value estimate valid

**사전 반증조건**

retail multiple compression

**실제 결과**

AWS 사업은 맞았으나 residual math 민감.

**정량적 괴리**

3P+Ads / 2024 $200bn 예상 / $70bn EBIT potential / 2023 revenue $187.0bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

AWS cheap residual 가설은 'retail multiple compression'를 반증조건으로 저장한다.

#### 3. Marketplace — 적중 · 논지 비중 16%

**당시 주장**

3P revenue가 크게 성장한다.

**당시 근거**

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

**이 주장이 성립하려면**

seller ecosystem

**사전 반증조건**

regulation/seller churn

**실제 결과**

2023 $140bn.

**정량적 괴리**

AWS / ~$55bn 2021E / high value / 2023 $90.8bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Marketplace 가설은 'regulation/seller churn'를 반증조건으로 저장한다.

#### 4. Advertising — 강한 적중 · 논지 비중 16%

**당시 주장**

ads가 고마진 $50bn+ business가 된다.

**당시 근거**

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

**이 주장이 성립하려면**

commercial intent

**사전 반증조건**

ad load constraint

**실제 결과**

2023 $46.9bn.

**정량적 괴리**

Consolidated OI / 높은 장기 power / 확대 / 2022 $12.2bn→2023 $36.9bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Advertising 가설은 'ad load constraint'를 반증조건으로 저장한다.

#### 5. $70bn EBIT potential — 미완전 · 논지 비중 16%

**당시 주장**

3P+ads 35% blended margin 가능.

**당시 근거**

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

**이 주장이 성립하려면**

mix/margin

**사전 반증조건**

cost allocation higher

**실제 결과**

방향은 좋지만 직접 segment EBIT 미공시.

**정량적 괴리**

2021-03 $154.70 → 2024-01 $155.20, 가격은 사실상 보합. 2022에는 $84까지 큰 drawdown.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

$70bn EBIT potential 가설은 'cost allocation higher'를 반증조건으로 저장한다.

#### 6. Stock upside — 실패 · 논지 비중 16%

**당시 주장**

사업성장이 valuation을 이긴다.

**당시 근거**

Amazon retail 자체가 강한 moat를 갖고 있고 AWS는 전체 valuation에 비해 싸며 Marketplace와 Advertising이 30~40% operating margin의 추가 earnings engine이 될 수 있다고 주장했다.

**이 주장이 성립하려면**

starting multiple sustainable

**사전 반증조건**

2022 de-rate

**실제 결과**

cutoff 보합.

**정량적 괴리**

2021-03 $154.70 → 2024-01 $155.20, 가격은 사실상 보합. 2022에는 $84까지 큰 drawdown.

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

Stock upside 가설은 '2022 de-rate'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2023 3P seller services $140.1bn, advertising $46.9bn으로 합계 $187bn에 도달해 $200bn revenue 가정에 근접했다. AWS도 $90.8bn sales/$24.6bn operating income으로 성장했다. 그러나 2021 starting valuation과 2022 cost reset 때문에 주가는 cutoff까지 보합이었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2021-03 $154.70 → 2024-01 $155.20, 가격은 사실상 보합. 2022에는 $84까지 큰 drawdown. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

사업의 mix shift는 놀랄 만큼 정확했지만 security analysis에서는 '좋은 자산을 싸게 산다'는 AWS residual valuation이 retail의 높은 standalone multiple에 의존했다. Business success와 stock return을 분리해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-04-28 — North America/International profitability와 excess capacity 문제가 드러나며 높은 retail standalone value에 대한 discount rate를 높여야 했다. 회피 가능성: 높음. 2022 fulfillment overcapacity와 FCF deterioration에서 valuation claim을 재설정했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

사업논지 적중·증권수익률 미달. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $154.70 | upside | 2024-01 $155.20 | 가격 실패 |
| 3P+Ads | 2024 $200bn 예상 | $70bn EBIT potential | 2023 revenue $187.0bn | 매출 적중 |
| AWS | ~$55bn 2021E | high value | 2023 $90.8bn | 적중 |
| Consolidated OI | 높은 장기 power | 확대 | 2022 $12.2bn→2023 $36.9bn | 회복 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-03-31 | VIC 아이디어 게시 | Retail $1.3tn + cheap AWS·ads/marketplace Long |
| 2022-04-28 | 최초 검증·반증 신호 | North America/International profitability와 excess capacity 문제가 드러나며 높은 retail standalone value에 대한 discount rate를 높여야 했다. |
| 2015-12-31 | AWS economics 가시화 | retail 외 high-margin value pool이 독립적으로 중요해짐 |
| 2020-03-31 | COVID digital acceleration | e-commerce/cloud adoption 급가속 |
| 2023-12-31 | 효율회복 | 2023 OI $36.9bn, AWS OI $24.6bn |
| 2024-01-31 | 고정 평가기준일 | 2021-03 $154.70 → 2024-01 $155.20, 가격은 사실상 보합. 2022에는 $84까지 큰 drawdown. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2022-04-28 — North America/International profitability와 excess capacity 문제가 드러나며 높은 retail standalone value에 대한 discount rate를 높여야 했다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 높음. 2022 fulfillment overcapacity와 FCF deterioration에서 valuation claim을 재설정했어야 한다.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC AMZN 2021-03-31 원문](https://www.valueinvestorsclub.com/idea/AMAZON.COM_INC/0888750890) — Value Investors Club / user SQL, 2021-03-31. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Amazon 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) — SEC, 2024-02-02. 2023 매출·segment OI·3P/ads/AWS 수치
- [3. Amazon FY2023 results](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/amzn-20231231xex991.htm) — Amazon / SEC, 2024-02-01. 2023 sales와 profitability recovery 확인
- [4. Amazon historical prices](https://www.digrin.com/stocks/detail/AMZN/price) — Digrin, 2024-01-31. split-adjusted historical price path
- [5. Amazon Investor Relations](https://ir.aboutamazon.com/) — Amazon, 2024-01-31. annual reports·shareholder materials
- [6. Amazon segment tables FY2023](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R32.htm) — SEC, 2024-02-02. North America/International/AWS segment earnings

---

<!-- idea:f7079491-42a7-4fa7-b376-75a816a976a0 -->
## 6. 2022-01-11 — Investment-cycle normalization·~20% IRR Long

### 결론부터

**종합판정: 사업회복 적중·IRR 실패.** Business-cycle diagnosis는 좋았지만 cycle trough의 깊이와 valuation compression을 과소평가했다. 재투자 cycle은 언제 끝나는지만 아니라 peak capacity가 수요보다 얼마나 과잉인지가 중요하다.

**주가·증권 결과:** 2022-01 $149.57 → 2022말 $84(-44%), 2024-01 $155.20(+4%). 원문 ~20% annualized 목표 미달.

**Thesis / Process 점수:** 7.5 / 8.1

### 1. 무슨 기업인가

Amazon은 단순 온라인 소매업체가 아니라 네 개의 서로 다른 경제성을 한 플랫폼에 결합한 기업이다. 첫째 1P retail은 Amazon이 재고를 직접 사서 소비자에게 판매하는 낮은 마진·높은 회전율 사업이다. 둘째 3P marketplace는 외부 판매자가 Amazon 트래픽·결제·Fulfillment by Amazon을 이용하고 Amazon이 commission·fulfillment fee를 받는 자본효율 높은 사업이다. 셋째 광고는 구매의도가 이미 높은 검색·상품 페이지에 광고를 판매해 높은 incremental margin을 만든다. 넷째 AWS는 기업·개발자에게 compute, storage, database 등 cloud infrastructure를 사용량 기반으로 판매한다. Prime은 별도 구독수익이면서 동시에 구매빈도와 ecosystem lock-in을 높이는 flywheel의 연결고리다. 2023년 매출은 $574.8bn, AWS $90.8bn, 3P seller services $140.1bn, advertising $46.9bn이었고 영업이익은 $36.9bn, 이 중 AWS가 $24.6bn을 담당했다. 핵심 KPI는 GMV/online store sales, 3P mix와 seller-service revenue, Prime engagement, advertising growth, AWS growth·margin, fulfillment/technology CapEx, operating cash flow와 FCF다.

### 2. 산업 가치사슬과 돈의 흐름

Amazon의 돈 흐름은 retail traffic이 더 많은 sellers와 selection을 부르고, selection과 낮은 가격·빠른 배송이 다시 traffic을 늘리는 flywheel이다. 1P retail 자체 마진은 낮아도 규모가 fulfillment density와 vendor terms를 개선한다. Marketplace와 advertising은 동일한 traffic 위에서 높은 fee/margin을 만들고, Prime은 구매빈도와 loyalty를 높인다. AWS는 retail과는 별도의 cloud scale economy를 갖지만 Amazon 전체의 기술·capital allocation culture를 공유한다. 따라서 consolidated P/E만 보면 재투자로 낮아진 retail earnings와 고마진 AWS/ads를 같은 multiple로 평가하는 오류가 생긴다. 반대로 '재투자라서 현재 FCF가 낮아도 무조건 가치창출'이라고 보는 것도 위험하다. fulfillment·data-center 투자 cohort가 실제 revenue, margin, working-capital efficiency로 회수되는지를 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Amazon의 핵심 경쟁우위는 selection·price·convenience, Prime member base, logistics density, seller ecosystem, 구매의도 데이터와 AWS의 규모·서비스 breadth다. 2010 Short가 지적한 physical media digitization은 실제였지만 Amazon은 media seller가 아니라 general merchandise, marketplace, cloud, advertising platform으로 business mix를 바꿨다. 중요한 lesson은 기존 revenue category가 죽는 것과 회사의 customer relationship이 죽는 것을 구분하는 것이다. 반대로 2021~22의 높은 valuation에서는 moat가 맞더라도 reinvestment returns와 starting multiple이 낮은 주가수익률을 만들 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

### 5. 밸류에이션과 기대수익의 연결

Normalized trailing earnings 기준 약 30x로 최근 5년 최저 수준이라 보고, 각 사업 성장률과 margin 정상화를 적용해 multiple expansion 없이도 약 20% annualized return을 예상. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Investment cycle — 적중·지연 · 논지 비중 18%

**당시 주장**

낮은 FCF는 일시적 capacity investment다.

**당시 근거**

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

**이 주장이 성립하려면**

demand catches capacity

**사전 반증조건**

persistent overbuild

**실제 결과**

2023 효율회복.

**정량적 괴리**

주가 / $149.57 / ~20% CAGR / 2024-01 $155.20

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Investment cycle 가설은 'persistent overbuild'를 반증조건으로 저장한다.

#### 2. 3P/Ads margins — 적중 · 논지 비중 18%

**당시 주장**

고마진 mix가 earnings를 높인다.

**당시 근거**

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

**이 주장이 성립하려면**

revenue mix 확대

**사전 반증조건**

regulatory pressure

**실제 결과**

매출 mix 확대.

**정량적 괴리**

2022 OI / 정상화 기대 / 회복 / $12.2bn로 저점

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

3P/Ads margins 가설은 'regulatory pressure'를 반증조건으로 저장한다.

#### 3. AWS growth — 부분 적중 · 논지 비중 16%

**당시 주장**

AWS가 long runway를 유지한다.

**당시 근거**

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

**이 주장이 성립하려면**

cloud migration

**사전 반증조건**

growth deceleration

**실제 결과**

2023 성장 13%로 둔화했지만 확대.

**정량적 괴리**

2023 OI / cycle recovery / 상승 / $36.9bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

AWS growth 가설은 'growth deceleration'를 반증조건으로 저장한다.

#### 4. Jassy allocation — 적중 · 논지 비중 16%

**당시 주장**

새 CEO가 과잉투자를 교정한다.

**당시 근거**

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

**이 주장이 성립하려면**

cost discipline

**사전 반증조건**

continued overbuild

**실제 결과**

2023 cost reset 확인.

**정량적 괴리**

NA OI / investment drag / normalize / -$2.85bn→+$14.88bn

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Jassy allocation 가설은 'continued overbuild'를 반증조건으로 저장한다.

#### 5. 30x normalized — 실패 · 논지 비중 16%

**당시 주장**

valuation이 과거 대비 낮아 안전마진이다.

**당시 근거**

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

**이 주장이 성립하려면**

normalized E 빠른 회복

**사전 반증조건**

E와 multiple 동시 하락

**실제 결과**

2022 큰 drawdown.

**정량적 괴리**

2022-01 $149.57 → 2022말 $84(-44%), 2024-01 $155.20(+4%). 원문 ~20% annualized 목표 미달.

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

30x normalized 가설은 'E와 multiple 동시 하락'를 반증조건으로 저장한다.

#### 6. 20% IRR — 실패 · 논지 비중 16%

**당시 주장**

multiple expansion 없이 20% CAGR.

**당시 근거**

Amazon이 다시 fulfillment/technology investment cycle에 들어가 FCF가 일시적으로 눌렸고 시장이 과거처럼 이를 구조적 수익성 악화로 오해한다고 봤다. Advertising과 3P의 높은 margin, AWS 성장과 Jassy의 capital allocation을 핵심으로 봤다.

**이 주장이 성립하려면**

earnings compounding

**사전 반증조건**

recovery delay

**실제 결과**

cutoff 약 +4%.

**정량적 괴리**

2022-01 $149.57 → 2022말 $84(-44%), 2024-01 $155.20(+4%). 원문 ~20% annualized 목표 미달.

**분석 오류·핵심**

현재 mix·multiple을 장기 고정하거나 catalyst probability를 과대평가했다.

**재사용할 교훈**

20% IRR 가설은 'recovery delay'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2022에는 overcapacity, inflation, Rivian mark 등으로 주가와 earnings가 더 악화됐다. 하지만 2023 North America OI가 -$2.8bn에서 +$14.9bn으로 개선되고 consolidated OI가 $12.2bn→$36.9bn으로 회복해 '투자사이클 후 효율회복'은 상당부분 맞았다. 주가는 cutoff까지 원가 수준이라 20% IRR은 실패.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2022-01 $149.57 → 2022말 $84(-44%), 2024-01 $155.20(+4%). 원문 ~20% annualized 목표 미달. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

Business-cycle diagnosis는 좋았지만 cycle trough의 깊이와 valuation compression을 과소평가했다. 재투자 cycle은 언제 끝나는지만 아니라 peak capacity가 수요보다 얼마나 과잉인지가 중요하다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-07-28 — 회사가 fulfillment network productivity와 cost reduction을 강조할 정도로 overcapacity가 커져 원문의 빠른 normalized earnings 경로가 지연됐다. 회피 가능성: 중간. 2022년 capacity utilization·North America margin을 중심 KPI로 재설정했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

사업회복 적중·IRR 실패. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $149.57 | ~20% CAGR | 2024-01 $155.20 | IRR 실패 |
| 2022 OI | 정상화 기대 | 회복 | $12.2bn로 저점 | 초기 실패 |
| 2023 OI | cycle recovery | 상승 | $36.9bn | 사업 적중 |
| NA OI | investment drag | normalize | -$2.85bn→+$14.88bn | 강한 회복 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2022-01-11 | VIC 아이디어 게시 | Investment-cycle normalization·~20% IRR Long |
| 2022-07-28 | 최초 검증·반증 신호 | 회사가 fulfillment network productivity와 cost reduction을 강조할 정도로 overcapacity가 커져 원문의 빠른 normalized earnings 경로가 지연됐다. |
| 2015-12-31 | AWS economics 가시화 | retail 외 high-margin value pool이 독립적으로 중요해짐 |
| 2020-03-31 | COVID digital acceleration | e-commerce/cloud adoption 급가속 |
| 2023-12-31 | 효율회복 | 2023 OI $36.9bn, AWS OI $24.6bn |
| 2024-01-31 | 고정 평가기준일 | 2022-01 $149.57 → 2022말 $84(-44%), 2024-01 $155.20(+4%). 원문 ~20% annualized 목표 미달. |

### Failure / Success Anatomy

- **근본 오류:** 사업구조 또는 valuation state를 고정해 future mix/capital allocation/duration을 충분히 반영하지 않음
- **최초 검증·반증 신호:** 2022-07-28 — 회사가 fulfillment network productivity와 cost reduction을 강조할 정도로 overcapacity가 커져 원문의 빠른 normalized earnings 경로가 지연됐다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 중간. 2022년 capacity utilization·North America margin을 중심 KPI로 재설정했어야 한다.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- 1. VIC AMZN 2022-01-11 원문 — Value Investors Club / user SQL, 2022-01-11. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Amazon 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) — SEC, 2024-02-02. 2023 매출·segment OI·3P/ads/AWS 수치
- [3. Amazon FY2023 results](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/amzn-20231231xex991.htm) — Amazon / SEC, 2024-02-01. 2023 sales와 profitability recovery 확인
- [4. Amazon historical prices](https://www.digrin.com/stocks/detail/AMZN/price) — Digrin, 2024-01-31. split-adjusted historical price path
- [5. Amazon Investor Relations](https://ir.aboutamazon.com/) — Amazon, 2024-01-31. annual reports·shareholder materials
- [6. Amazon segment tables FY2023](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/R32.htm) — SEC, 2024-02-02. North America/International/AWS segment earnings

---
# IAC INC (IAC) — 기업과 비즈니스

## 1. 무슨 기업인가

IAC는 전형적인 operating conglomerate가 아니라 인터넷 사업을 만들고 키운 뒤 독립 상장시키는 capital-allocation platform이다. Barry Diller 체제에서 Expedia, Ticketmaster, Match, TripAdvisor, LendingTree, Vimeo 등 수많은 사업을 acquire/build/spin했고, 특정 시점의 IAC 주주는 상장된 자회사 지분과 비상장 stub을 동시에 보유하는 구조가 반복됐다. 2016~20 VIC 논지의 핵심은 Match Group, ANGI/HomeAdvisor, Vimeo, Dotdash/Publishing, Applications와 현금을 분리해 보면 public stakes를 제외한 stub이 0 또는 음의 가치로 거래된다는 점이었다. 2020년 Match가 분리됐고 2021년 Vimeo도 spin-off됐다. 2023년 기준 IAC의 주요 사업은 Dotdash Meredith, Angi, Care.com, Search/Emerging였으며 MGM Resorts 등 전략지분도 보유했다. 핵심 KPI는 각 operating subsidiary revenue/EBITDA, public stake market value, HoldCo net cash, corporate overhead, share count, spin/tax 구조와 새로운 capital deployment다.

## 2. 산업 가치사슬과 돈의 흐름

IAC의 가치사슬은 일반 기업과 다르다. operating asset을 낮은 규모에서 acquire/build → management·capital·cross-company know-how를 투입 → 규모가 커지면 public company로 분리 → 분리 뒤 HoldCo는 현금과 남은 사업으로 다시 cycle을 반복한다. 따라서 valuation은 consolidated EPS보다 public stakes의 market value + private businesses의 standalone value + net cash − HoldCo costs/tax leakage로 계산하는 SOTP가 적합하다. 2017·2019 VIC의 hedged stub trade는 IAC를 Long하고 MTCH/ANGI를 해당 지분비율만큼 Short해 공개지분의 가격변동을 제거한 뒤 residual stub만 사는 구조였다.

## 3. 경쟁우위·경쟁구도·핵심 지표

IAC의 moat는 개별 product보다는 capital allocation, entrepreneurial management, tax-efficient separation 경험과 인터넷 자산을 초기 단계에서 키우는 반복능력에 가깝다. 하지만 이 'meta-moat'는 founder/management judgment에 의존하고 새 사업의 success rate가 떨어질 수 있다. SOTP discount는 단순히 싸다는 이유로 닫히지 않으며 spin·sale·buyback 같은 crystallization mechanism이 필요하다. 또 public stakes를 hedge한 stub trade는 borrow cost, hedge ratio 변화와 corporate action timing을 별도 관리해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2016-05-02 | Short | Long | Match/HomeAdvisor/Vimeo SOTP·Diller capital allocation Long | Match 분리(2020)와 Vimeo spin(2021)까지 이어지며 distributed-value 기준 큰 성공. | 전설적 capital-allocation 성공 |
| 2017-08-08 | Short | Long IAC / Short MTCH & ANGI stub | Negative-$1.60 stub·$21+ hedged value | Stub가 음의 가치에서 양의 가치로 재평가되고 Match/Vimeo spin까지 이어져 구조적 성공. | 매우 성공 |
| 2019-04-29 | Short | Long IAC / Short MTCH & ANGI stub | Negative-$33 stub·$283 SOTP Long | 2020 Match separation과 2021 Vimeo spin으로 핵심 catalyst가 실현. 강한 성공. | 전설적 성공 |
| 2020-02-22 | Short | Long | Post-Match-spin next-chapter Long | Match 분리 후 IAC standalone와 배포 MTCH 가치가 분리됐고 2021 Vimeo spin까지 추가 value realization. Event thesis 성공. | 이벤트 성공·후속 portfolio 혼합 |

---

<!-- idea:f683f4a3-a162-49e1-aced-efb245f50cde -->
## 1. 2016-05-02 — Match/HomeAdvisor/Vimeo SOTP·Diller capital allocation Long

### 결론부터

**종합판정: 전설적 capital-allocation 성공.** SOTP와 catalyst가 management의 장기 operating pattern에 연결됐다. 단순 HoldCo discount가 아니라 어떤 자산이 언제 독립기업이 될 수 있는지를 봤다는 점이 강했다.

**주가·증권 결과:** Match 분리(2020)와 Vimeo spin(2021)까지 이어지며 distributed-value 기준 큰 성공.

**Thesis / Process 점수:** 9.6 / 9.4

### 1. 무슨 기업인가

IAC는 전형적인 operating conglomerate가 아니라 인터넷 사업을 만들고 키운 뒤 독립 상장시키는 capital-allocation platform이다. Barry Diller 체제에서 Expedia, Ticketmaster, Match, TripAdvisor, LendingTree, Vimeo 등 수많은 사업을 acquire/build/spin했고, 특정 시점의 IAC 주주는 상장된 자회사 지분과 비상장 stub을 동시에 보유하는 구조가 반복됐다. 2016~20 VIC 논지의 핵심은 Match Group, ANGI/HomeAdvisor, Vimeo, Dotdash/Publishing, Applications와 현금을 분리해 보면 public stakes를 제외한 stub이 0 또는 음의 가치로 거래된다는 점이었다. 2020년 Match가 분리됐고 2021년 Vimeo도 spin-off됐다. 2023년 기준 IAC의 주요 사업은 Dotdash Meredith, Angi, Care.com, Search/Emerging였으며 MGM Resorts 등 전략지분도 보유했다. 핵심 KPI는 각 operating subsidiary revenue/EBITDA, public stake market value, HoldCo net cash, corporate overhead, share count, spin/tax 구조와 새로운 capital deployment다.

### 2. 산업 가치사슬과 돈의 흐름

IAC의 가치사슬은 일반 기업과 다르다. operating asset을 낮은 규모에서 acquire/build → management·capital·cross-company know-how를 투입 → 규모가 커지면 public company로 분리 → 분리 뒤 HoldCo는 현금과 남은 사업으로 다시 cycle을 반복한다. 따라서 valuation은 consolidated EPS보다 public stakes의 market value + private businesses의 standalone value + net cash − HoldCo costs/tax leakage로 계산하는 SOTP가 적합하다. 2017·2019 VIC의 hedged stub trade는 IAC를 Long하고 MTCH/ANGI를 해당 지분비율만큼 Short해 공개지분의 가격변동을 제거한 뒤 residual stub만 사는 구조였다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IAC의 moat는 개별 product보다는 capital allocation, entrepreneurial management, tax-efficient separation 경험과 인터넷 자산을 초기 단계에서 키우는 반복능력에 가깝다. 하지만 이 'meta-moat'는 founder/management judgment에 의존하고 새 사업의 success rate가 떨어질 수 있다. SOTP discount는 단순히 싸다는 이유로 닫히지 않으며 spin·sale·buyback 같은 crystallization mechanism이 필요하다. 또 public stakes를 hedge한 stub trade는 borrow cost, hedge ratio 변화와 corporate action timing을 별도 관리해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

84% Match 지분, HomeAdvisor, Vimeo, Publishing/Applications, VC assets와 cash를 분리한 conservative SOTP가 market price보다 크게 높다고 주장. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Match value — 적중 · 논지 비중 18%

**당시 주장**

Match 지분이 IAC 핵심 공개가치다.

**당시 근거**

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

**이 주장이 성립하려면**

dating network growth

**사전 반증조건**

Match de-rate

**실제 결과**

성장·분리.

**정량적 괴리**

Match stake / 84% / spin/value realization / 2020 완전 분리

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Match value 가설은 'Match de-rate'를 반증조건으로 저장한다.

#### 2. HomeAdvisor — 부분 적중 · 논지 비중 18%

**당시 주장**

home-services marketplace가 큰 asset이 된다.

**당시 근거**

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

**이 주장이 성립하려면**

service requests growth

**사전 반증조건**

CAC/quality issues

**실제 결과**

ANGI 규모 확대, 장기 quality는 혼합.

**정량적 괴리**

Vimeo / 650k+ paid subs / optionality / 2021 spin

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

HomeAdvisor 가설은 'CAC/quality issues'를 반증조건으로 저장한다.

#### 3. Vimeo — 강한 적중 · 논지 비중 16%

**당시 주장**

paid-video platform이 hidden value다.

**당시 근거**

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

**이 주장이 성립하려면**

subscription growth

**사전 반증조건**

YouTube competition

**실제 결과**

2021 public spin.

**정량적 괴리**

HomeAdvisor / 고성장 / scale / ANGI로 확대

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Vimeo 가설은 'YouTube competition'를 반증조건으로 저장한다.

#### 4. Mature cash flow — 부분 · 논지 비중 16%

**당시 주장**

Publishing/Apps가 growth bets를 fund한다.

**당시 근거**

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

**이 주장이 성립하려면**

FCF 유지

**사전 반증조건**

search erosion

**실제 결과**

portfolio 재배치 가능.

**정량적 괴리**

Capital allocation / 반복 spin / 지속 / Match/Vimeo 분리

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Mature cash flow 가설은 'search erosion'를 반증조건으로 저장한다.

#### 5. Diller allocator — 강한 적중 · 논지 비중 16%

**당시 주장**

acquire/build/spin 반복능력이 지속된다.

**당시 근거**

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

**이 주장이 성립하려면**

governance continuity

**사전 반증조건**

bad acquisition

**실제 결과**

Match/Vimeo로 재확인.

**정량적 괴리**

Match 분리(2020)와 Vimeo spin(2021)까지 이어지며 distributed-value 기준 큰 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Diller allocator 가설은 'bad acquisition'를 반증조건으로 저장한다.

#### 6. SOTP discount — 적중 · 논지 비중 16%

**당시 주장**

spin이 discount를 닫는다.

**당시 근거**

IAC는 공개 Match 지분만이 아니라 HomeAdvisor, Vimeo, Publishing와 hidden VC investments를 갖고 있으며 Diller의 acquire-build-spin track record가 이 discount를 반복적으로 해소할 것이라고 봤다.

**이 주장이 성립하려면**

tax-efficient actions

**사전 반증조건**

permanent HoldCo discount

**실제 결과**

실제 separation.

**정량적 괴리**

Match 분리(2020)와 Vimeo spin(2021)까지 이어지며 distributed-value 기준 큰 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

SOTP discount 가설은 'permanent HoldCo discount'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

IAC는 2020 Match를 완전 분리했고 2021 Vimeo도 spin-off했다. 후일 Dotdash-Meredith, Care.com 등으로 portfolio를 재구성했다. 원 thesis의 핵심인 'operating asset를 키워 독립시키는 capital-allocation machine'이 재현됐다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: Match 분리(2020)와 Vimeo spin(2021)까지 이어지며 distributed-value 기준 큰 성공. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

SOTP와 catalyst가 management의 장기 operating pattern에 연결됐다. 단순 HoldCo discount가 아니라 어떤 자산이 언제 독립기업이 될 수 있는지를 봤다는 점이 강했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-06-30 — Match separation 완료로 가장 큰 public stake가 실제로 IAC 주주에게 분리되어 SOTP discount가 현물로 crystallize됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

전설적 capital-allocation 성공. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Match stake | 84% | spin/value realization | 2020 완전 분리 | 강한 적중 |
| Vimeo | 650k+ paid subs | optionality | 2021 spin | 강한 적중 |
| HomeAdvisor | 고성장 | scale | ANGI로 확대 | 적중 |
| Capital allocation | 반복 spin | 지속 | Match/Vimeo 분리 | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-05-02 | VIC 아이디어 게시 | Match/HomeAdvisor/Vimeo SOTP·Diller capital allocation Long |
| 2020-06-30 | 핵심 corporate-action 신호 | Match separation 완료로 가장 큰 public stake가 실제로 IAC 주주에게 분리되어 SOTP discount가 현물로 crystallize됐다. |
| 2020-06-30 | Match separation 완료 | public stake가 IAC에서 완전 분리 |
| 2021-05-25 | Vimeo spin 완료 | 두 번째 hidden asset crystallization |
| 2023-12-31 | 새 portfolio 점검 | Dotdash Meredith·Angi·Care.com 중심으로 재구성 |
| 2024-01-31 | 고정 평가기준일 | Match 분리(2020)와 Vimeo spin(2021)까지 이어지며 distributed-value 기준 큰 성공. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2020-06-30 — Match separation 완료로 가장 큰 public stake가 실제로 IAC 주주에게 분리되어 SOTP discount가 현물로 crystallize됐다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IAC 2016-05-02 원문](https://www.valueinvestorsclub.com/idea/IACINTERACTIVECORP/5841024207) — Value Investors Club / user SQL, 2016-05-02. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. IAC 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. IAC history, Match 2020/Vimeo 2021 separation, current portfolio
- [3. IAC Investor Relations](https://ir.iac.com/) — IAC, 2024-01-31. shareholder letters·corporate actions
- [4. IAC historical prices](https://www.digrin.com/stocks/detail/IAC/price) — Digrin, 2024-01-31. raw-price path; spin adjustments 필요
- [5. IAC corporate history and segment disclosures](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. Dotdash Meredith·Angi·Care.com 구조
- [6. IAC company overview](https://www.iac.com/) — IAC, 2024-01-31. build/acquire/spin business model

---

<!-- idea:e28de04c-adfd-4764-824e-443f5016c2e0 -->
## 2. 2017-08-08 — Negative-$1.60 stub·$21+ hedged value

### 결론부터

**종합판정: 매우 성공.** SOTP를 실제 trade construction으로 변환한 좋은 사례다. 공개지분 valuation debate를 hedge로 제거해 'stub이 정말 음수인가'에 집중했다.

**주가·증권 결과:** Stub가 음의 가치에서 양의 가치로 재평가되고 Match/Vimeo spin까지 이어져 구조적 성공.

**Thesis / Process 점수:** 9 / 8.1

### 1. 무슨 기업인가

IAC는 전형적인 operating conglomerate가 아니라 인터넷 사업을 만들고 키운 뒤 독립 상장시키는 capital-allocation platform이다. Barry Diller 체제에서 Expedia, Ticketmaster, Match, TripAdvisor, LendingTree, Vimeo 등 수많은 사업을 acquire/build/spin했고, 특정 시점의 IAC 주주는 상장된 자회사 지분과 비상장 stub을 동시에 보유하는 구조가 반복됐다. 2016~20 VIC 논지의 핵심은 Match Group, ANGI/HomeAdvisor, Vimeo, Dotdash/Publishing, Applications와 현금을 분리해 보면 public stakes를 제외한 stub이 0 또는 음의 가치로 거래된다는 점이었다. 2020년 Match가 분리됐고 2021년 Vimeo도 spin-off됐다. 2023년 기준 IAC의 주요 사업은 Dotdash Meredith, Angi, Care.com, Search/Emerging였으며 MGM Resorts 등 전략지분도 보유했다. 핵심 KPI는 각 operating subsidiary revenue/EBITDA, public stake market value, HoldCo net cash, corporate overhead, share count, spin/tax 구조와 새로운 capital deployment다.

### 2. 산업 가치사슬과 돈의 흐름

IAC의 가치사슬은 일반 기업과 다르다. operating asset을 낮은 규모에서 acquire/build → management·capital·cross-company know-how를 투입 → 규모가 커지면 public company로 분리 → 분리 뒤 HoldCo는 현금과 남은 사업으로 다시 cycle을 반복한다. 따라서 valuation은 consolidated EPS보다 public stakes의 market value + private businesses의 standalone value + net cash − HoldCo costs/tax leakage로 계산하는 SOTP가 적합하다. 2017·2019 VIC의 hedged stub trade는 IAC를 Long하고 MTCH/ANGI를 해당 지분비율만큼 Short해 공개지분의 가격변동을 제거한 뒤 residual stub만 사는 구조였다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IAC의 moat는 개별 product보다는 capital allocation, entrepreneurial management, tax-efficient separation 경험과 인터넷 자산을 초기 단계에서 키우는 반복능력에 가깝다. 하지만 이 'meta-moat'는 founder/management judgment에 의존하고 새 사업의 success rate가 떨어질 수 있다. SOTP discount는 단순히 싸다는 이유로 닫히지 않으며 spin·sale·buyback 같은 crystallization mechanism이 필요하다. 또 public stakes를 hedge한 stub trade는 borrow cost, hedge ratio 변화와 corporate action timing을 별도 관리해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

### 5. 밸류에이션과 기대수익의 연결

IAC Long 1x, MTCH Short 2.5559x, ANGI Short 4.958x. StubCo implied -$1.60 vs $7.80 cash + $3.08 real-estate/VC + operations 약 $9 = $20+ value, 약 $21 upside. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Negative stub — 적중 · 논지 비중 18%

**당시 주장**

hedged residual이 음의 가치라 비정상이다.

**당시 근거**

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

**이 주장이 성립하려면**

asset marks correct

**사전 반증조건**

hidden liabilities

**실제 결과**

residual assets 실제 가치 보유.

**정량적 괴리**

Stub price / -$1.60 / $20+ value / 독립자산 가치 확인

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Negative stub 가설은 'hidden liabilities'를 반증조건으로 저장한다.

#### 2. Cash/assets — 적중 · 논지 비중 18%

**당시 주장**

$10.88/share non-op value가 있다.

**당시 근거**

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

**이 주장이 성립하려면**

cash not consumed

**사전 반증조건**

capital loss

**실제 결과**

value cushion 제공.

**정량적 괴리**

Non-op assets / $10.88/share / floor / 현금/투자자산 실재

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Cash/assets 가설은 'capital loss'를 반증조건으로 저장한다.

#### 3. Operating value — 적중 · 논지 비중 16%

**당시 주장**

Vimeo/Publishing/Apps가 positive FCF다.

**당시 근거**

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

**이 주장이 성립하려면**

growth/margins

**사전 반증조건**

cash burn

**실제 결과**

Vimeo spin 등으로 확인.

**정량적 괴리**

Operations / ~$60m EBITDA / ~$9/share / Vimeo/Publishing 가치 성장

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Operating value 가설은 'cash burn'를 반증조건으로 저장한다.

#### 4. Hedge purity — 적중 · 논지 비중 16%

**당시 주장**

MTCH/ANGI shorts로 public-value risk 제거.

**당시 근거**

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

**이 주장이 성립하려면**

ratios stable

**사전 반증조건**

corporate action/borrow costs

**실제 결과**

관리 필요했지만 concept 유효.

**정량적 괴리**

Catalyst / MTCH monetization / spin / 2020 separation

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Hedge purity 가설은 'corporate action/borrow costs'를 반증조건으로 저장한다.

#### 5. Catalyst — 강한 적중 · 논지 비중 16%

**당시 주장**

MTCH tax-efficient monetization이 온다.

**당시 근거**

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

**이 주장이 성립하려면**

board action

**사전 반증조건**

no spin

**실제 결과**

2020 완료.

**정량적 괴리**

Stub가 음의 가치에서 양의 가치로 재평가되고 Match/Vimeo spin까지 이어져 구조적 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Catalyst 가설은 'no spin'를 반증조건으로 저장한다.

#### 6. $21 upside — 적중 · 논지 비중 16%

**당시 주장**

stub가 최소 0~positive로 재평가된다.

**당시 근거**

공개 MTCH·ANGI 지분을 hedge하면 시장이 나머지 IAC를 음의 가치로 평가하지만 실제로는 $10.88 non-operating assets와 ~$60m EBITDA/positive FCF businesses를 보유한다고 주장했다. ANGI close와 MTCH monetization announcement가 catalyst.

**이 주장이 성립하려면**

crystallization

**사전 반증조건**

HoldCo discount persists

**실제 결과**

구조적 성공.

**정량적 괴리**

Stub가 음의 가치에서 양의 가치로 재평가되고 Match/Vimeo spin까지 이어져 구조적 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

$21 upside 가설은 'HoldCo discount persists'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

ANGI 구조가 정착됐고 Match는 2020에 분리됐다. Vimeo·Publishing 등 residual businesses도 무가치가 아니었고 Vimeo는 2021 spin됐다. 다만 hedge trade는 borrow/ratio와 corporate-action timing을 별도 관리해야 했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: Stub가 음의 가치에서 양의 가치로 재평가되고 Match/Vimeo spin까지 이어져 구조적 성공. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

SOTP를 실제 trade construction으로 변환한 좋은 사례다. 공개지분 valuation debate를 hedge로 제거해 'stub이 정말 음수인가'에 집중했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-06-30 — Match separation으로 hedge 대상 중 가장 큰 public stake가 제거되며 residual IAC가 독립 price discovery를 받았다. 회피 가능성: 해당 없음. carry/borrow를 엄격히 관리.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Stub price | -$1.60 | $20+ value | 독립자산 가치 확인 | 적중 |
| Non-op assets | $10.88/share | floor | 현금/투자자산 실재 | 적중 |
| Operations | ~$60m EBITDA | ~$9/share | Vimeo/Publishing 가치 성장 | 적중 |
| Catalyst | MTCH monetization | spin | 2020 separation | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-08-08 | VIC 아이디어 게시 | Negative-$1.60 stub·$21+ hedged value |
| 2020-06-30 | 핵심 corporate-action 신호 | Match separation으로 hedge 대상 중 가장 큰 public stake가 제거되며 residual IAC가 독립 price discovery를 받았다. |
| 2020-06-30 | Match separation 완료 | public stake가 IAC에서 완전 분리 |
| 2021-05-25 | Vimeo spin 완료 | 두 번째 hidden asset crystallization |
| 2023-12-31 | 새 portfolio 점검 | Dotdash Meredith·Angi·Care.com 중심으로 재구성 |
| 2024-01-31 | 고정 평가기준일 | Stub가 음의 가치에서 양의 가치로 재평가되고 Match/Vimeo spin까지 이어져 구조적 성공. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2020-06-30 — Match separation으로 hedge 대상 중 가장 큰 public stake가 제거되며 residual IAC가 독립 price discovery를 받았다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음. carry/borrow를 엄격히 관리.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IAC 2017-08-08 원문](https://www.valueinvestorsclub.com/idea/IACInteractive_Corp/3669283792) — Value Investors Club / user SQL, 2017-08-08. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. IAC 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. IAC history, Match 2020/Vimeo 2021 separation, current portfolio
- [3. IAC Investor Relations](https://ir.iac.com/) — IAC, 2024-01-31. shareholder letters·corporate actions
- [4. IAC historical prices](https://www.digrin.com/stocks/detail/IAC/price) — Digrin, 2024-01-31. raw-price path; spin adjustments 필요
- [5. IAC corporate history and segment disclosures](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. Dotdash Meredith·Angi·Care.com 구조
- [6. IAC company overview](https://www.iac.com/) — IAC, 2024-01-31. build/acquire/spin business model

---

<!-- idea:a6bfb87f-48c3-45ec-98b3-39aa2e5cbddb -->
## 3. 2019-04-29 — Negative-$33 stub·$283 SOTP Long

### 결론부터

**종합판정: 전설적 성공.** 가치평가와 crystallization이 모두 맞았다. 특히 public stakes를 빼고 residual의 cash flow를 직접 산출해 conglomerate discount를 정량화했다.

**주가·증권 결과:** 2020 Match separation과 2021 Vimeo spin으로 핵심 catalyst가 실현. 강한 성공.

**Thesis / Process 점수:** 9.6 / 9.4

### 1. 무슨 기업인가

IAC는 전형적인 operating conglomerate가 아니라 인터넷 사업을 만들고 키운 뒤 독립 상장시키는 capital-allocation platform이다. Barry Diller 체제에서 Expedia, Ticketmaster, Match, TripAdvisor, LendingTree, Vimeo 등 수많은 사업을 acquire/build/spin했고, 특정 시점의 IAC 주주는 상장된 자회사 지분과 비상장 stub을 동시에 보유하는 구조가 반복됐다. 2016~20 VIC 논지의 핵심은 Match Group, ANGI/HomeAdvisor, Vimeo, Dotdash/Publishing, Applications와 현금을 분리해 보면 public stakes를 제외한 stub이 0 또는 음의 가치로 거래된다는 점이었다. 2020년 Match가 분리됐고 2021년 Vimeo도 spin-off됐다. 2023년 기준 IAC의 주요 사업은 Dotdash Meredith, Angi, Care.com, Search/Emerging였으며 MGM Resorts 등 전략지분도 보유했다. 핵심 KPI는 각 operating subsidiary revenue/EBITDA, public stake market value, HoldCo net cash, corporate overhead, share count, spin/tax 구조와 새로운 capital deployment다.

### 2. 산업 가치사슬과 돈의 흐름

IAC의 가치사슬은 일반 기업과 다르다. operating asset을 낮은 규모에서 acquire/build → management·capital·cross-company know-how를 투입 → 규모가 커지면 public company로 분리 → 분리 뒤 HoldCo는 현금과 남은 사업으로 다시 cycle을 반복한다. 따라서 valuation은 consolidated EPS보다 public stakes의 market value + private businesses의 standalone value + net cash − HoldCo costs/tax leakage로 계산하는 SOTP가 적합하다. 2017·2019 VIC의 hedged stub trade는 IAC를 Long하고 MTCH/ANGI를 해당 지분비율만큼 Short해 공개지분의 가격변동을 제거한 뒤 residual stub만 사는 구조였다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IAC의 moat는 개별 product보다는 capital allocation, entrepreneurial management, tax-efficient separation 경험과 인터넷 자산을 초기 단계에서 키우는 반복능력에 가깝다. 하지만 이 'meta-moat'는 founder/management judgment에 의존하고 새 사업의 success rate가 떨어질 수 있다. SOTP discount는 단순히 싸다는 이유로 닫히지 않으며 spin·sale·buyback 같은 crystallization mechanism이 필요하다. 또 public stakes를 hedge한 stub trade는 borrow cost, hedge ratio 변화와 corporate action timing을 별도 관리해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

### 5. 밸류에이션과 기대수익의 연결

Public MTCH+ANGI stakes만으로 IAC 약 $260/share vs stock ~$227 → stub -$33. Stub underlying SOTP +$26, total IAC 약 $283, 약 25% upside. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Stub mispricing — 적중 · 논지 비중 18%

**당시 주장**

-$3bn residual valuation이 비정상이다.

**당시 근거**

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

**이 주장이 성립하려면**

asset/FCF values positive

**사전 반증조건**

corporate burn

**실제 결과**

spin으로 반증.

**정량적 괴리**

IAC / ~$227 / $283 / spin value realization

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Stub mispricing 가설은 'corporate burn'를 반증조건으로 저장한다.

#### 2. Publishing cash flow — 부분 적중 · 논지 비중 18%

**당시 주장**

Publishing/Apps가 $120m EBITDA 수준이다.

**당시 근거**

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

**이 주장이 성립하려면**

search/publishing durability

**사전 반증조건**

traffic collapse

**실제 결과**

Dotdash로 사업진화.

**정량적 괴리**

Stub / -$33/share / +$26/share / public separations로 양수 확인

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Publishing cash flow 가설은 'traffic collapse'를 반증조건으로 저장한다.

#### 3. Vimeo value — 강한 적중 · 논지 비중 16%

**당시 주장**

Vimeo recurring revenue가 큰 option이다.

**당시 근거**

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

**이 주장이 성립하려면**

subscriber growth

**사전 반증조건**

competition

**실제 결과**

public spin.

**정량적 괴리**

Publishing/Apps / ~$120m 2020E EBITDA / cash generator / Dotdash 중심 가치 성장

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Vimeo value 가설은 'competition'를 반증조건으로 저장한다.

#### 4. Match spin — 강한 적중 · 논지 비중 16%

**당시 주장**

Match가 독립한다.

**당시 근거**

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

**이 주장이 성립하려면**

tax/corporate approval

**사전 반증조건**

delay

**실제 결과**

2020 완료.

**정량적 괴리**

Vimeo / ~$225m 2020E recurring rev / hidden asset / 2021 spin

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Match spin 가설은 'delay'를 반증조건으로 저장한다.

#### 5. Allocator optionality — 적중 · 논지 비중 16%

**당시 주장**

새 winners를 반복적으로 만든다.

**당시 근거**

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

**이 주장이 성립하려면**

management discipline

**사전 반증조건**

capital allocation miss

**실제 결과**

portfolio 재구성 지속.

**정량적 괴리**

2020 Match separation과 2021 Vimeo spin으로 핵심 catalyst가 실현. 강한 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Allocator optionality 가설은 'capital allocation miss'를 반증조건으로 저장한다.

#### 6. $283 SOTP — 적중 · 논지 비중 16%

**당시 주장**

25%+ upside.

**당시 근거**

Publishing/Applications가 2020 약 $120m EBITDA, Vimeo recurring subscription revenue 약 $225m으로 성장하는데 market은 이를 negative $3bn에 평가한다고 봤다. Match/ANGI spin과 future capital allocation이 catalyst.

**이 주장이 성립하려면**

spin/asset values

**사전 반증조건**

market discount

**실제 결과**

value realization 방향 성공.

**정량적 괴리**

2020 Match separation과 2021 Vimeo spin으로 핵심 catalyst가 실현. 강한 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

$283 SOTP 가설은 'market discount'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Match가 2020 분리되고 Vimeo가 2021 독립상장돼 residual assets가 음수가 아니라는 것이 직접 확인됐다. 2023 IAC는 다시 Dotdash Meredith·Angi·Care.com 등 새로운 portfolio로 재구성됐다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: 2020 Match separation과 2021 Vimeo spin으로 핵심 catalyst가 실현. 강한 성공. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가치평가와 crystallization이 모두 맞았다. 특히 public stakes를 빼고 residual의 cash flow를 직접 산출해 conglomerate discount를 정량화했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2019-12-19 — IAC와 Match가 full separation agreement를 발표하면서 가장 중요한 catalyst가 구체화됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| IAC | ~$227 | $283 | spin value realization | 적중 |
| Stub | -$33/share | +$26/share | public separations로 양수 확인 | 강한 적중 |
| Publishing/Apps | ~$120m 2020E EBITDA | cash generator | Dotdash 중심 가치 성장 | 적중 |
| Vimeo | ~$225m 2020E recurring rev | hidden asset | 2021 spin | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-04-29 | VIC 아이디어 게시 | Negative-$33 stub·$283 SOTP Long |
| 2019-12-19 | 핵심 corporate-action 신호 | IAC와 Match가 full separation agreement를 발표하면서 가장 중요한 catalyst가 구체화됐다. |
| 2020-06-30 | Match separation 완료 | public stake가 IAC에서 완전 분리 |
| 2021-05-25 | Vimeo spin 완료 | 두 번째 hidden asset crystallization |
| 2023-12-31 | 새 portfolio 점검 | Dotdash Meredith·Angi·Care.com 중심으로 재구성 |
| 2024-01-31 | 고정 평가기준일 | 2020 Match separation과 2021 Vimeo spin으로 핵심 catalyst가 실현. 강한 성공. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2019-12-19 — IAC와 Match가 full separation agreement를 발표하면서 가장 중요한 catalyst가 구체화됐다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IAC 2019-04-29 원문](https://www.valueinvestorsclub.com/idea/Interactive_Corp_the_stub/3983598398) — Value Investors Club / user SQL, 2019-04-29. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. IAC 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. IAC history, Match 2020/Vimeo 2021 separation, current portfolio
- [3. IAC Investor Relations](https://ir.iac.com/) — IAC, 2024-01-31. shareholder letters·corporate actions
- [4. IAC historical prices](https://www.digrin.com/stocks/detail/IAC/price) — Digrin, 2024-01-31. raw-price path; spin adjustments 필요
- [5. IAC corporate history and segment disclosures](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. Dotdash Meredith·Angi·Care.com 구조
- [6. IAC company overview](https://www.iac.com/) — IAC, 2024-01-31. build/acquire/spin business model

---

<!-- idea:7cec141f-dee2-4000-8599-b4a5e01c923b -->
## 4. 2020-02-22 — Post-Match-spin next-chapter Long

### 결론부터

**종합판정: 이벤트 성공·후속 portfolio 혼합.** Event와 capital-allocation process를 잘 봤지만 allocator premium을 영구 multiple로 주기보다는 각 새 investment cohort를 별도 검증해야 한다.

**주가·증권 결과:** Match 분리 후 IAC standalone와 배포 MTCH 가치가 분리됐고 2021 Vimeo spin까지 추가 value realization. Event thesis 성공.

**Thesis / Process 점수:** 7.5 / 8.1

### 1. 무슨 기업인가

IAC는 전형적인 operating conglomerate가 아니라 인터넷 사업을 만들고 키운 뒤 독립 상장시키는 capital-allocation platform이다. Barry Diller 체제에서 Expedia, Ticketmaster, Match, TripAdvisor, LendingTree, Vimeo 등 수많은 사업을 acquire/build/spin했고, 특정 시점의 IAC 주주는 상장된 자회사 지분과 비상장 stub을 동시에 보유하는 구조가 반복됐다. 2016~20 VIC 논지의 핵심은 Match Group, ANGI/HomeAdvisor, Vimeo, Dotdash/Publishing, Applications와 현금을 분리해 보면 public stakes를 제외한 stub이 0 또는 음의 가치로 거래된다는 점이었다. 2020년 Match가 분리됐고 2021년 Vimeo도 spin-off됐다. 2023년 기준 IAC의 주요 사업은 Dotdash Meredith, Angi, Care.com, Search/Emerging였으며 MGM Resorts 등 전략지분도 보유했다. 핵심 KPI는 각 operating subsidiary revenue/EBITDA, public stake market value, HoldCo net cash, corporate overhead, share count, spin/tax 구조와 새로운 capital deployment다.

### 2. 산업 가치사슬과 돈의 흐름

IAC의 가치사슬은 일반 기업과 다르다. operating asset을 낮은 규모에서 acquire/build → management·capital·cross-company know-how를 투입 → 규모가 커지면 public company로 분리 → 분리 뒤 HoldCo는 현금과 남은 사업으로 다시 cycle을 반복한다. 따라서 valuation은 consolidated EPS보다 public stakes의 market value + private businesses의 standalone value + net cash − HoldCo costs/tax leakage로 계산하는 SOTP가 적합하다. 2017·2019 VIC의 hedged stub trade는 IAC를 Long하고 MTCH/ANGI를 해당 지분비율만큼 Short해 공개지분의 가격변동을 제거한 뒤 residual stub만 사는 구조였다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IAC의 moat는 개별 product보다는 capital allocation, entrepreneurial management, tax-efficient separation 경험과 인터넷 자산을 초기 단계에서 키우는 반복능력에 가깝다. 하지만 이 'meta-moat'는 founder/management judgment에 의존하고 새 사업의 success rate가 떨어질 수 있다. SOTP discount는 단순히 싸다는 이유로 닫히지 않으며 spin·sale·buyback 같은 crystallization mechanism이 필요하다. 또 public stakes를 hedge한 stub trade는 borrow cost, hedge ratio 변화와 corporate action timing을 별도 관리해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

### 5. 밸류에이션과 기대수익의 연결

25년간 약 14% CAGR의 capital-allocation record와 Match spin 후 약 $2.4bn net cash를 기반으로 residual IAC를 새 cycle의 시작으로 평가. 단순 multiple이 아니라 business mix/공개지분/normalized economics를 주당가치로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Match separation — 강한 적중 · 논지 비중 18%

**당시 주장**

planned spin이 완료된다.

**당시 근거**

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

**이 주장이 성립하려면**

regulatory/tax execution

**사전 반증조건**

delay

**실제 결과**

완료.

**정량적 괴리**

Match spin / 예정 / 완료 / 2020-06 완료

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Match separation 가설은 'delay'를 반증조건으로 저장한다.

#### 2. Post-spin cash — 부분 적중 · 논지 비중 18%

**당시 주장**

$2.4bn net cash가 optionality다.

**당시 근거**

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

**이 주장이 성립하려면**

discipline

**사전 반증조건**

overpay

**실제 결과**

새 investments에 사용.

**정량적 괴리**

Net cash / ~$2.4bn 기대 / new cycle funding / 재투자 자원

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Post-spin cash 가설은 'overpay'를 반증조건으로 저장한다.

#### 3. Vimeo — 강한 적중 · 논지 비중 16%

**당시 주장**

Vimeo가 다음 major value realization 후보다.

**당시 근거**

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

**이 주장이 성립하려면**

subscriber growth

**사전 반증조건**

growth stall

**실제 결과**

2021 spin.

**정량적 괴리**

Vimeo / hidden growth / value realization / 2021 spin

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Vimeo 가설은 'growth stall'를 반증조건으로 저장한다.

#### 4. Repeatable process — 적중 · 논지 비중 16%

**당시 주장**

IAC의 build-spin model이 반복된다.

**당시 근거**

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

**이 주장이 성립하려면**

management culture

**사전 반증조건**

key-person/process decay

**실제 결과**

분리 engine 유지.

**정량적 괴리**

2023 portfolio / 새 assets / repeat success / Dotdash/Angi volatility

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Repeatable process 가설은 'key-person/process decay'를 반증조건으로 저장한다.

#### 5. Capital discipline — 부분 · 논지 비중 16%

**당시 주장**

비싼 private assets를 무리하게 사지 않는다.

**당시 근거**

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

**이 주장이 성립하려면**

valuation discipline

**사전 반증조건**

overpay

**실제 결과**

Meredith 등 성과는 혼합.

**정량적 괴리**

Match 분리 후 IAC standalone와 배포 MTCH 가치가 분리됐고 2021 Vimeo spin까지 추가 value realization. Event thesis 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Capital discipline 가설은 'overpay'를 반증조건으로 저장한다.

#### 6. Total shareholder value — 적중 · 논지 비중 16%

**당시 주장**

spin distributions 포함 value가 증가한다.

**당시 근거**

Match separation이 IAC의 세 번째 대형 separation이고, spin 뒤 남는 cash와 Vimeo/HomeAdvisor/Dotdash 등에서 다시 build-and-spin cycle을 시작할 수 있다고 봤다. Private-market valuation이 비싸 IAC가 서두르지 않을 것이라는 discipline도 강조했다.

**이 주장이 성립하려면**

assets compound

**사전 반증조건**

stub destroys value

**실제 결과**

event horizon 성공.

**정량적 괴리**

Match 분리 후 IAC standalone와 배포 MTCH 가치가 분리됐고 2021 Vimeo spin까지 추가 value realization. Event thesis 성공.

**분석 오류·핵심**

핵심 causal chain이 segment/corporate-action outcome으로 확인됐다.

**재사용할 교훈**

Total shareholder value 가설은 'stub destroys value'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2020 Match, 2021 Vimeo가 분리됐다. 이후 IAC는 MGM stake, Care.com, Meredith acquisition 등을 통해 새 portfolio를 만들었다. 2022~23 Dotdash Meredith/Angi의 operating volatility로 '항상 바로 성공하는 allocator'는 아니지만 separation engine은 실제로 작동했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과: Match 분리 후 IAC standalone와 배포 MTCH 가치가 분리됐고 2021 Vimeo spin까지 추가 value realization. Event thesis 성공. 사업의 성공과 starting valuation·spin distribution을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

Event와 capital-allocation process를 잘 봤지만 allocator premium을 영구 multiple로 주기보다는 각 새 investment cohort를 별도 검증해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-06-30 — Match separation이 실제 완료돼 원문의 핵심 event가 예정대로 실행됐다. 회피 가능성: 해당 없음. spin 후에는 pre-spin IAC 가격과 단순 비교하지 말고 distributed MTCH를 포함한 total value로 봐야 한다.

### 10. 최종 판정·반사실·재사용 교훈

이벤트 성공·후속 portfolio 혼합. 재투자/플랫폼에서는 mix 변화, HoldCo에서는 crystallization을 사전 claim으로 저장한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Match spin | 예정 | 완료 | 2020-06 완료 | 강한 적중 |
| Net cash | ~$2.4bn 기대 | new cycle funding | 재투자 자원 | 적중 |
| Vimeo | hidden growth | value realization | 2021 spin | 강한 적중 |
| 2023 portfolio | 새 assets | repeat success | Dotdash/Angi volatility | 혼합 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-02-22 | VIC 아이디어 게시 | Post-Match-spin next-chapter Long |
| 2020-06-30 | 핵심 corporate-action 신호 | Match separation이 실제 완료돼 원문의 핵심 event가 예정대로 실행됐다. |
| 2020-06-30 | Match separation 완료 | public stake가 IAC에서 완전 분리 |
| 2021-05-25 | Vimeo spin 완료 | 두 번째 hidden asset crystallization |
| 2023-12-31 | 새 portfolio 점검 | Dotdash Meredith·Angi·Care.com 중심으로 재구성 |
| 2024-01-31 | 고정 평가기준일 | Match 분리 후 IAC standalone와 배포 MTCH 가치가 분리됐고 2021 Vimeo spin까지 추가 value realization. Event thesis 성공. |

### Failure / Success Anatomy

- **근본 오류:** 운영 mechanism과 장기 capital-allocation catalyst를 연결
- **최초 검증·반증 신호:** 2020-06-30 — Match separation이 실제 완료돼 원문의 핵심 event가 예정대로 실행됐다.
- **당시 알 수 있었나:** segment sales/margins, reinvestment, 3P/ads/AWS mix, public stake values, spin announcements와 HoldCo cash는 공개자료로 지속 검증 가능했다.
- **피할 수 있었나:** 해당 없음. spin 후에는 pre-spin IAC 가격과 단순 비교하지 말고 distributed MTCH를 포함한 total value로 봐야 한다.
- **반사실 질문:** 현재 이익 또는 SOTP가 맞더라도 사업 mix와 자본배분이 바뀌면 주주에게 귀속되는 장기 per-share value는 어떻게 달라지는가?

### 주요 근거자료

- 1. VIC IAC 2020-02-22 원문 — Value Investors Club / user SQL, 2020-02-22. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. IAC 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. IAC history, Match 2020/Vimeo 2021 separation, current portfolio
- [3. IAC Investor Relations](https://ir.iac.com/) — IAC, 2024-01-31. shareholder letters·corporate actions
- [4. IAC historical prices](https://www.digrin.com/stocks/detail/IAC/price) — Digrin, 2024-01-31. raw-price path; spin adjustments 필요
- [5. IAC corporate history and segment disclosures](https://www.sec.gov/Archives/edgar/data/1800227/000180022724000011/iaci-20231231.htm) — SEC, 2024-02-29. Dotdash Meredith·Angi·Care.com 구조
- [6. IAC company overview](https://www.iac.com/) — IAC, 2024-01-31. build/acquire/spin business model

---

# 배치 공통 학습

1. **현재 revenue mix를 회사의 영구정체성으로 착각하지 않는다.**
2. **재투자는 비용이 아니라 미래 capability를 사는 것일 수 있지만, cohort별 ROI를 확인해야 한다.**
3. **좋은 사업과 좋은 주식은 다르다.** Amazon 2021은 business call과 security return이 분리된 대표 사례다.
4. **Marketplace·advertising 같은 high-margin mix shift는 consolidated P/E보다 먼저 본다.**
5. **HoldCo SOTP는 spin/sale/buyback이라는 crystallization mechanism이 있을 때 강하다.**
6. **Stub trade는 공개지분 valuation debate를 hedge로 제거할 수 있다.**
7. **Capital allocator의 과거 record는 새 투자 cohort의 수익성을 보장하지 않는다.**
