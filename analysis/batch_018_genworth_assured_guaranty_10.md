# Batch 018 — Genworth Financial·Assured Guaranty 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Genworth Financial 8건 · Assured Guaranty 2건

## 결론부터

이번 배치는 보험주에서 **낮은 P/B·adjusted book·asset value가 왜 곧바로 equity floor가 아닌지**를 본다.

- **Genworth:** 2009년 $2 crisis Long은 HoldCo liquidity와 asset haircut을 먼저 계산해 매우 성공했다. 그러나 2009년 말 이후 여러 Long은 U.S. mortgage insurance 위험을 반박한 뒤 legacy LTC tail을 충분히 보지 못했다. 2016 Short는 LTC를 잘 봤지만 Oceanwide bid와 MI asset를 놓쳤고, 2017·2019·2020 merger-arb는 financing/duration을 과소평가했다.
- **Assured Guaranty:** 2008~09 위기에서 살아남아 FSA를 인수하고 dominant monoline이 된 franchise 통찰은 맞았다. 그러나 adjusted book와 normalized EPS가 빠르게 주가에 반영될 것이라는 timing은 크게 틀렸다.

> 데이터 경고: 선택한 GNW 8건은 원 SQL상 모두 `is_short=true`지만 실제 본문은 2016 Short를 제외하면 Long 또는 merger-arb Long이다. 원본 flag는 보존하고 research direction만 교정한다.

---

# GENWORTH FINANCIAL INC (GNW) — 기업과 비즈니스

## 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

## 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2004-06-02 | Short | Long | GE spin supply overhang·book value discount Long | 2004~07에는 $20대 후반~$30대로 상승했지만 2008 금융위기에는 $1 아래까지 붕괴. 초기 rerating은 성공했으나 장기 franchise/downside 가정은 실패. | 초기 가격 성공·장기 tail-risk 실패 |
| 2009-01-22 | Short | Long | Adjusted tangible book·liquidity panic Long | $2 부근에서 6개월 약 2.5배, 1년 약 5.1배. crisis panic Long으로 매우 성공. | 전설적 성공 |
| 2009-11-13 | Short | Long | Book-value recovery·diversified insurer Long | 1년 거의 보합, 2년 약 -42%, 3년 약 -52%, 5년 약 -24%. 장기 value trap. | 단기 생존 적중·장기 실패 |
| 2015-04-21 | Short | Long | 0.3x book·LTC rate-action turnaround Long | 1년 약 -63%, 2년 -48%, 3년 -65%, 5년 -57%. 실패. | 치명적 value-trap 실패 |
| 2016-04-14 | Short | Short | LTC reserve hole·HoldCo liquidity Short | 6개월 약 +95%, 1년 +52%, 3년 +46%, 5년 +30% 수준으로 Short 손실. Oceanwide $5.43 bid가 큰 tail event. | LTC 분석 일부 적중·증권 Short 실패 |
| 2017-01-15 | Short | Merger Arb Long GNW | Oceanwide $5.43 merger-arb Long | $3.88에서 $5.43 cash deal을 기대했지만 거래는 수차례 연장 뒤 2021년 종료. 1년 수익률 약 -17%. | 이벤트 실패 |
| 2019-03-15 | Short | Merger Arb Long GNW | Deal fatigue·$5.43 merger-arb Long | $4 부근에서 $5.43을 기대했지만 거래 미종결. 1~3년 수익률은 대체로 부진/보합. | 가격·이벤트 실패 |
| 2020-04-14 | Short | Special Situation Long GNW equity / GNW 2034 bonds | 2034 bonds + Oceanwide equity dual-trade | Merger는 2021 종료되어 $5.43 equity payoff 실패. 장기채는 Enact IPO·debt reduction으로 credit가 개선되는 경로가 더 견조. | Equity 이벤트 실패·credit thesis 부분 성공 |

---

<!-- idea:33aaf41c-e0cd-4fb4-af05-647c8a695cc8 -->
## 1. 2004-06-02 — GE spin supply overhang·book value discount Long

### 결론부터

**종합판정: 초기 가격 성공·장기 tail-risk 실패.** spin supply overhang과 초기 valuation은 잘 봤지만 보험회사의 book value quality를 충분히 분해하지 않았다. 특히 LTC처럼 수십 년 뒤 손실이 나타나는 liability는 당시 book value와 near-term EPS에 거의 드러나지 않는다. 'GE quality stamp'와 diversification이 tail risk를 없애지 못했다.

**주가·증권 결과:** 2004~07에는 $20대 후반~$30대로 상승했지만 2008 금융위기에는 $1 아래까지 붕괴. 초기 rerating은 성공했으나 장기 franchise/downside 가정은 실패.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

### 5. 밸류에이션과 기대수익의 연결

약 10x LTM EPS와 낮은 P/B에서 거래되고 GE의 70% 잔여지분 매각 overhang이 사라지면 ROE 개선·independent capital allocation으로 rerating 가능하다고 봤다. 정확한 단일 target보다 spin discount 정상화가 핵심이었다. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Spin overhang — 적중 · 논지 비중 18%

**당시 주장**

대형 IPO와 GE 잔여지분 매각이 일시적으로 가격을 누른다.

**당시 근거**

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

**이 주장이 성립하려면**

사업가치가 안정되고 supply만 일시적

**사전 반증조건**

fundamental capital deterioration

**실제 결과**

초기 주가 rerating은 실제로 발생했다.

**정량적 괴리**

주가 / 약 $20 / spin discount 해소 / 2006~07 $30대 후 2008 <$1

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Spin overhang 가설은 'fundamental capital deterioration'를 사전 반증조건으로 저장한다.

#### 2. Diversified franchise — 부분 실패 · 논지 비중 18%

**당시 주장**

Protection·Retirement·MI 분산이 earnings 안정성을 높인다.

**당시 근거**

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

**이 주장이 성립하려면**

segment shocks가 상쇄

**사전 반증조건**

동시에 credit/liability shock 발생

**실제 결과**

2008에는 여러 자본압력이 동시 발생했다.

**정량적 괴리**

P/E / 약 10x LTM / rerating / 초기 rerating 후 crisis multiple collapse

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Diversified franchise 가설은 '동시에 credit/liability shock 발생'를 사전 반증조건으로 저장한다.

#### 3. Book-value floor — 실패 · 논지 비중 16%

**당시 주장**

낮은 P/B가 downside를 제한한다.

**당시 근거**

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

**이 주장이 성립하려면**

reserve·asset marks가 보수적

**사전 반증조건**

hidden reserve hole·asset impairment

**실제 결과**

book value quality가 생각보다 약했다.

**정량적 괴리**

Book value / 할인 / capital quality 안정 / mortgage/LTC tail로 quality 훼손

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Book-value floor 가설은 'hidden reserve hole·asset impairment'를 사전 반증조건으로 저장한다.

#### 4. Independent ROE — 부분 · 논지 비중 16%

**당시 주장**

GE 독립 후 capital allocation과 asset yield를 개선한다.

**당시 근거**

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

**이 주장이 성립하려면**

rating·capital 여유

**사전 반증조건**

규제자본·liquidity가 capital return 제한

**실제 결과**

후일 capital preservation이 더 중요해졌다.

**정량적 괴리**

GE overhang / GE 70% 잔여 / 점진 해소 / 해소됨

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Independent ROE 가설은 '규제자본·liquidity가 capital return 제한'를 사전 반증조건으로 저장한다.

#### 5. Buyback optionality — 실패 · 논지 비중 16%

**당시 주장**

GE 지분 정리 후 buyback이 주당가치를 높일 수 있다.

**당시 근거**

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

**이 주장이 성립하려면**

free cash available

**사전 반증조건**

HoldCo cash가 debt/rating support에 필요

**실제 결과**

위기에서 buyback optionality는 사라졌다.

**정량적 괴리**

2004~07에는 $20대 후반~$30대로 상승했지만 2008 금융위기에는 $1 아래까지 붕괴. 초기 rerating은 성공했으나 장기 franchise/downside 가정은 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Buyback optionality 가설은 'HoldCo cash가 debt/rating support에 필요'를 사전 반증조건으로 저장한다.

#### 6. Long-term rerating — 부분 실패 · 논지 비중 16%

**당시 주장**

10x 수준이 정상화되면 좋은 장기 수익이 가능하다.

**당시 근거**

GE가 Genworth를 IPO한 직후 공급물량과 향후 GE 잔여지분 매각이 주가를 눌렀다고 봤다. Protection, Retirement Income/Investments, Mortgage Insurance의 diversified earnings와 book value 대비 할인, 독립경영 후 자본배분 개선 가능성을 강조했다. GE가 잔여지분을 정리한 뒤 buyback이나 higher-yield asset mix로 ROE를 높일 수 있다는 논리였다.

**이 주장이 성립하려면**

보험 liabilities가 안정

**사전 반증조건**

tail liabilities가 valuation을 재정의

**실제 결과**

초기 성공 후 장기적으로 크게 실패했다.

**정량적 괴리**

2004~07에는 $20대 후반~$30대로 상승했지만 2008 금융위기에는 $1 아래까지 붕괴. 초기 rerating은 성공했으나 장기 franchise/downside 가정은 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Long-term rerating 가설은 'tail liabilities가 valuation을 재정의'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

초기에는 spin overhang이 해소되고 주가가 2006~07년 $30대를 기록해 rerating 논지가 작동했다. 그러나 2008 금융위기와 mortgage·investment losses, 이후 장기요양보험 reserve 문제가 드러나며 회사는 극심한 자본·rating 압박을 겪었다. 단순 저P/B 보험주가 아니라 long-tail liabilities와 regulated capital이 핵심이었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2004~07에는 $20대 후반~$30대로 상승했지만 2008 금융위기에는 $1 아래까지 붕괴. 초기 rerating은 성공했으나 장기 franchise/downside 가정은 실패. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

spin supply overhang과 초기 valuation은 잘 봤지만 보험회사의 book value quality를 충분히 분해하지 않았다. 특히 LTC처럼 수십 년 뒤 손실이 나타나는 liability는 당시 book value와 near-term EPS에 거의 드러나지 않는다. 'GE quality stamp'와 diversification이 tail risk를 없애지 못했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-10-01 — 금융위기에서 Genworth 주가·capital confidence가 급격히 붕괴하며 book-value floor와 diversified-insurer downside 가정이 깨졌다. 회피 가능성: 높음. 2007~08 mortgage/investment stress와 rating pressure가 커질 때 book-value discount가 아니라 statutory capital과 liquidity를 재평가했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

초기 가격 성공·장기 tail-risk 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | 약 $20 | spin discount 해소 | 2006~07 $30대 후 2008 <$1 | 초기 성공·장기 실패 |
| P/E | 약 10x LTM | rerating | 초기 rerating 후 crisis multiple collapse | 혼합 |
| Book value | 할인 | capital quality 안정 | mortgage/LTC tail로 quality 훼손 | 실패 |
| GE overhang | GE 70% 잔여 | 점진 해소 | 해소됨 | 촉매 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2004-06-02 | VIC 아이디어 게시 | GE spin supply overhang·book value discount Long |
| 2008-10-01 | 최초 핵심 검증·반증 신호 | 금융위기에서 Genworth 주가·capital confidence가 급격히 붕괴하며 book-value floor와 diversified-insurer downside 가정이 깨졌다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | 2004~07에는 $20대 후반~$30대로 상승했지만 2008 금융위기에는 $1 아래까지 붕괴. 초기 rerating은 성공했으나 장기 franchise/downside 가정은 실패. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2008-10-01 — 금융위기에서 Genworth 주가·capital confidence가 급격히 붕괴하며 book-value floor와 diversified-insurer downside 가정이 깨졌다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 높음. 2007~08 mortgage/investment stress와 rating pressure가 커질 때 book-value discount가 아니라 statutory capital과 liquidity를 재평가했어야 한다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- 1. VIC GNW 2004-06-02 원문 — Value Investors Club, 2004-06-02. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:45e5a6a0-56f9-4b2d-827b-f7bfa3940d3b -->
## 2. 2009-01-22 — Adjusted tangible book·liquidity panic Long

### 결론부터

**종합판정: 전설적 성공.** 이 글은 정상화 EPS보다 먼저 liquidation/liquidity survival을 계산했다. 미국 MI를 0으로 놓고 asset marks를 추가 haircut한 뒤에도 equity cushion이 남는지를 확인한 것이 핵심이었다. 위기투자에서는 '얼마 벌까'보다 '12개월 안에 죽는가'를 먼저 묻는 좋은 사례다.

**주가·증권 결과:** $2 부근에서 6개월 약 2.5배, 1년 약 5.1배. crisis panic Long으로 매우 성공.

**Thesis / Process 점수:** 9.5 / 9.3

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

### 5. 밸류에이션과 기대수익의 연결

투자자산 fair value를 약 8% 추가 haircut하고 미국 MI는 0, goodwill/intangibles 제거, tax benefit을 반영해 adjusted tangible book 약 $5.77/share를 계산. 목표는 대략 $6 수준. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Asset haircut — 적중 · 논지 비중 18%

**당시 주장**

투자자산을 추가 8% haircut해도 equity value가 남는다.

**당시 근거**

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

**이 주장이 성립하려면**

marks가 stress loss보다 보수적

**사전 반증조건**

credit losses가 haircut 초과

**실제 결과**

systemic tail 완화 후 value 회복.

**정량적 괴리**

주가 / $2.00 / 약 $6 / 1년 약 5.1배

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Asset haircut 가설은 'credit losses가 haircut 초과'를 사전 반증조건으로 저장한다.

#### 2. U.S. MI zero value — 적중 · 논지 비중 18%

**당시 주장**

미국 MI를 0으로 둬도 $5.77 tangible value다.

**당시 근거**

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

**이 주장이 성립하려면**

다른 자산이 debt를 충분히 커버

**사전 반증조건**

다른 segment까지 capital trap

**실제 결과**

survival case가 성립했다.

**정량적 괴리**

Adj tangible BV / $5.77 / 가격 대비 큰 cushion / survival 후 rerating

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

U.S. MI zero value 가설은 '다른 segment까지 capital trap'를 사전 반증조건으로 저장한다.

#### 3. HoldCo liquidity — 적중 · 논지 비중 16%

**당시 주장**

$1.3bn cash+revolver가 2009 만기를 감당한다.

**당시 근거**

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

**이 주장이 성립하려면**

cash 접근 가능

**사전 반증조건**

subsidiary capital이 trapped되고 HoldCo cash 부족

**실제 결과**

만기 상환이 실제 이뤄졌다.

**정량적 괴리**

2009 debt maturity / 약 $1.1bn / cash/revolver로 대응 / Canada MI IPO proceeds 포함 상환

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

HoldCo liquidity 가설은 'subsidiary capital이 trapped되고 HoldCo cash 부족'를 사전 반증조건으로 저장한다.

#### 4. Asset monetization — 강한 적중 · 논지 비중 16%

**당시 주장**

Canada MI 등 자산을 현금화할 수 있다.

**당시 근거**

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

**이 주장이 성립하려면**

시장 접근·regulatory approval

**사전 반증조건**

IPO market 폐쇄

**실제 결과**

Canada MI IPO 성공.

**정량적 괴리**

Canada MI IPO / 잠재 유동성 / 자본조달 / 약 $705m proceeds

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Asset monetization 가설은 'IPO market 폐쇄'를 사전 반증조건으로 저장한다.

#### 5. Positive FCF — 적중 · 논지 비중 16%

**당시 주장**

핵심 사업 cash generation이 liquidity를 보완한다.

**당시 근거**

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

**이 주장이 성립하려면**

claim losses 통제

**사전 반증조건**

cash burn 확대

**실제 결과**

단기 survival을 지지했다.

**정량적 괴리**

$2 부근에서 6개월 약 2.5배, 1년 약 5.1배. crisis panic Long으로 매우 성공.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Positive FCF 가설은 'cash burn 확대'를 사전 반증조건으로 저장한다.

#### 6. $6 recovery — 강한 적중 · 논지 비중 16%

**당시 주장**

insolvency discount가 줄면 수배 상승 가능하다.

**당시 근거**

시장가격 $2는 insolvency를 전제로 하지만 asset portfolio를 추가로 크게 깎고 미국 MI를 0으로 둬도 tangible value가 $5.77이라고 주장했다. 2009 debt maturities 약 $1.1bn은 HoldCo cash $1.3bn과 revolver로 대응 가능하고 operating businesses도 positive FCF라 단기 liquidity panic이 과도하다고 봤다.

**이 주장이 성립하려면**

systemic panic 완화

**사전 반증조건**

capital raise로 심한 희석

**실제 결과**

주가가 1년 내 약 5배.

**정량적 괴리**

$2 부근에서 6개월 약 2.5배, 1년 약 5.1배. crisis panic Long으로 매우 성공.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

$6 recovery 가설은 'capital raise로 심한 희석'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2009년 캐나다 MI IPO로 약 $705m을 조달했고 회사는 2009 장기채 만기를 상환해 다음 큰 만기를 2011년까지 미뤘다. 금융시장 정상화와 capital actions로 insolvency tail이 급격히 줄며 주가가 몇 배 상승했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 $2 부근에서 6개월 약 2.5배, 1년 약 5.1배. crisis panic Long으로 매우 성공. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 정상화 EPS보다 먼저 liquidation/liquidity survival을 계산했다. 미국 MI를 0으로 놓고 asset marks를 추가 haircut한 뒤에도 equity cushion이 남는지를 확인한 것이 핵심이었다. 위기투자에서는 '얼마 벌까'보다 '12개월 안에 죽는가'를 먼저 묻는 좋은 사례다.

### 9. 최초 검증·반증 신호와 회피 가능성

2009-07-08 — 캐나다 MI IPO와 debt repayment 계획이 구체화되며 2009 liquidity wall이 해소될 가능성이 확인됐다. 회피 가능성: 해당 없음. 다만 위기보험주는 holding-company cash와 regulated subsidiary capital을 절대 합산하지 않는 discipline이 필요하다.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $2.00 | 약 $6 | 1년 약 5.1배 | 강한 적중 |
| Adj tangible BV | $5.77 | 가격 대비 큰 cushion | survival 후 rerating | 적중 |
| 2009 debt maturity | 약 $1.1bn | cash/revolver로 대응 | Canada MI IPO proceeds 포함 상환 | 적중 |
| Canada MI IPO | 잠재 유동성 | 자본조달 | 약 $705m proceeds | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2009-01-22 | VIC 아이디어 게시 | Adjusted tangible book·liquidity panic Long |
| 2009-07-08 | 최초 핵심 검증·반증 신호 | 캐나다 MI IPO와 debt repayment 계획이 구체화되며 2009 liquidity wall이 해소될 가능성이 확인됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | $2 부근에서 6개월 약 2.5배, 1년 약 5.1배. crisis panic Long으로 매우 성공. |

### Failure / Success Anatomy

- **근본 오류:** survival/liquidity와 operating value를 분리해 분석한 점이 강점
- **최초 검증·반증 신호:** 2009-07-08 — 캐나다 MI IPO와 debt repayment 계획이 구체화되며 2009 liquidity wall이 해소될 가능성이 확인됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 해당 없음. 다만 위기보험주는 holding-company cash와 regulated subsidiary capital을 절대 합산하지 않는 discipline이 필요하다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- [1. VIC GNW 2009-01-22 원문](https://www.valueinvestorsclub.com/idea/GENWORTH_FINANCIAL_INC/9911649073) — Value Investors Club, 2009-01-22. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:7d2e2d27-e25b-4489-ae7b-24a2eb8af797 -->
## 3. 2009-11-13 — Book-value recovery·diversified insurer Long

### 결론부터

**종합판정: 단기 생존 적중·장기 실패.** 가장 큰 오류는 '시장 우려의 중심인 U.S. MI가 작다'는 반론을 성공적으로 입증한 뒤 다른 tail liability가 없다고 암묵적으로 간주한 것이다. 위험원 하나를 반박했다고 전체 balance sheet가 안전해지는 것은 아니다. LTC in-force block의 assumption sensitivity를 독립적으로 검증했어야 했다.

**주가·증권 결과:** 1년 거의 보합, 2년 약 -42%, 3년 약 -52%, 5년 약 -24%. 장기 value trap.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Q1 book value 약 $19에서 Q3 $25+로 회복한 점과 U.S. MI가 매출의 약 10%에 불과하다는 diversification을 근거로 book-value discount 축소를 기대. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Diversification — 부분 실패 · 논지 비중 18%

**당시 주장**

U.S. MI가 작은 비중이라 시장의 단일-factor pricing이 과도하다.

**당시 근거**

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

**이 주장이 성립하려면**

life/LTC/international segments 안정

**사전 반증조건**

다른 segment에서 대형 손실

**실제 결과**

LTC가 새 핵심 위험으로 부상.

**정량적 괴리**

주가 / $11.47 / book-value rerating / 5년 약 -24%

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Diversification 가설은 '다른 segment에서 대형 손실'를 사전 반증조건으로 저장한다.

#### 2. Book recovery — 실패 · 논지 비중 18%

**당시 주장**

Q1 $19→Q3 $25+ book 회복이 franchise normalization을 의미한다.

**당시 근거**

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

**이 주장이 성립하려면**

book quality 안정

**사전 반증조건**

reserve strengthening

**실제 결과**

LTC reserve로 book quality 훼손.

**정량적 괴리**

Book value / Q3 $25+ / discount 축소 / LTC charge로 quality 훼손

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Book recovery 가설은 'reserve strengthening'를 사전 반증조건으로 저장한다.

#### 3. Canada/Australia MI — 적중 · 논지 비중 16%

**당시 주장**

국제 MI는 profitable하고 가치가 높다.

**당시 근거**

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

**이 주장이 성립하려면**

housing cycle 양호

**사전 반증조건**

housing losses 급증

**실제 결과**

이 자산들은 실제로 가치가 있었다.

**정량적 괴리**

U.S. MI revenue / 약 10% / 위기 risk 제한 / MI는 전체 파국 원인이 아님

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Canada/Australia MI 가설은 'housing losses 급증'를 사전 반증조건으로 저장한다.

#### 4. U.S. MI containment — 적중 · 논지 비중 16%

**당시 주장**

미국 MI 손실이 그룹 전체를 파괴하지 않는다.

**당시 근거**

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

**이 주장이 성립하려면**

capital ring-fencing

**사전 반증조건**

HoldCo 지원 확대

**실제 결과**

파국의 핵심은 후일 LTC였다.

**정량적 괴리**

2014 LTC reserve / 미반영 / 안정 가정 / +$531m reserve

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

U.S. MI containment 가설은 'HoldCo 지원 확대'를 사전 반증조건으로 저장한다.

#### 5. LTC adequacy — 실패 · 논지 비중 16%

**당시 주장**

legacy LTC가 book-value thesis를 훼손하지 않는다.

**당시 근거**

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

**이 주장이 성립하려면**

morbidity/lapse assumptions 적정

**사전 반증조건**

대규모 reserve increase

**실제 결과**

2014 대형 reserve charge.

**정량적 괴리**

1년 거의 보합, 2년 약 -42%, 3년 약 -52%, 5년 약 -24%. 장기 value trap.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

LTC adequacy 가설은 '대규모 reserve increase'를 사전 반증조건으로 저장한다.

#### 6. Long-term rerating — 실패 · 논지 비중 16%

**당시 주장**

diversified earnings와 book 회복으로 valuation이 정상화된다.

**당시 근거**

위기 직후 시장이 Genworth를 U.S. mortgage insurer처럼 취급하지만 실제로는 life/retirement/international MI가 큰 diversified insurer라고 봤다. book value가 이미 회복되고 Canada/Australia MI가 profitable하며 U.S. MI는 작은 비중이라 normalized valuation이 크게 높다고 주장했다.

**이 주장이 성립하려면**

tail liabilities 안정

**사전 반증조건**

새 liability overhang

**실제 결과**

5년 성과 부진.

**정량적 괴리**

1년 거의 보합, 2년 약 -42%, 3년 약 -52%, 5년 약 -24%. 장기 value trap.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Long-term rerating 가설은 '새 liability overhang'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2009 crisis survival은 맞았지만 이후 legacy LTC가 더 큰 문제로 부상했다. 2014년 회사는 LTC claim reserves를 $531m 늘리고 after-tax charge $345m, goodwill impairment $517m을 인식했다. 주가는 장기적으로 회복하지 못했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 1년 거의 보합, 2년 약 -42%, 3년 약 -52%, 5년 약 -24%. 장기 value trap. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가장 큰 오류는 '시장 우려의 중심인 U.S. MI가 작다'는 반론을 성공적으로 입증한 뒤 다른 tail liability가 없다고 암묵적으로 간주한 것이다. 위험원 하나를 반박했다고 전체 balance sheet가 안전해지는 것은 아니다. LTC in-force block의 assumption sensitivity를 독립적으로 검증했어야 했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2014-11-05 — LTC reserve $531m 증가와 대규모 after-tax charge가 발표되며 장기 book-value quality가 훼손됐음이 확인됐다. 회피 가능성: 중간~높음. 2010~13 LTC industry assumption changes와 rate-action dependence가 커질 때 thesis를 mortgage-insurance 중심에서 liability-duration 중심으로 재작성할 수 있었다.

### 10. 최종 판정·반사실·재사용 교훈

단기 생존 적중·장기 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $11.47 | book-value rerating | 5년 약 -24% | 실패 |
| Book value | Q3 $25+ | discount 축소 | LTC charge로 quality 훼손 | 실패 |
| U.S. MI revenue | 약 10% | 위기 risk 제한 | MI는 전체 파국 원인이 아님 | 적중 |
| 2014 LTC reserve | 미반영 | 안정 가정 | +$531m reserve | 치명적 반증 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2009-11-13 | VIC 아이디어 게시 | Book-value recovery·diversified insurer Long |
| 2014-11-05 | 최초 핵심 검증·반증 신호 | LTC reserve $531m 증가와 대규모 after-tax charge가 발표되며 장기 book-value quality가 훼손됐음이 확인됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | 1년 거의 보합, 2년 약 -42%, 3년 약 -52%, 5년 약 -24%. 장기 value trap. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2014-11-05 — LTC reserve $531m 증가와 대규모 after-tax charge가 발표되며 장기 book-value quality가 훼손됐음이 확인됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 중간~높음. 2010~13 LTC industry assumption changes와 rate-action dependence가 커질 때 thesis를 mortgage-insurance 중심에서 liability-duration 중심으로 재작성할 수 있었다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- [1. VIC GNW 2009-11-13 원문](https://www.valueinvestorsclub.com/idea/GENWORTH_FINANCIAL_INC/0175268604) — Value Investors Club, 2009-11-13. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:2e43e984-b905-4599-aa71-49c096e23ab6 -->
## 4. 2015-04-21 — 0.3x book·LTC rate-action turnaround Long

### 결론부터

**종합판정: 치명적 value-trap 실패.** 0.3x book는 싸 보였지만 book의 질이 LTC assumption에 따라 움직였다. public MI stake를 asset floor로 더한 것도 HoldCo debt·regulatory capital·tax·시간을 충분히 차감하지 않았다. long-tail insurance에서는 낮은 P/B보다 reserve uncertainty의 분포가 먼저다.

**주가·증권 결과:** 1년 약 -63%, 2년 -48%, 3년 -65%, 5년 -57%. 실패.

**Thesis / Process 점수:** 4.2 / 4.6

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

약 5x normalized EPS, 0.3x book. Canada/Australia MI public stakes 약 $2.5bn으로 시총의 약 2/3를 설명하고, LTC rate increases·business separation·asset sales로 gap 축소를 기대. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. LTC rate increases — 부분 · 논지 비중 18%

**당시 주장**

premium rate actions가 legacy economics를 크게 개선한다.

**당시 근거**

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

**이 주장이 성립하려면**

규제승인·persistency 적정

**사전 반증조건**

승인 부족·claims 악화

**실제 결과**

일부 개선은 있었지만 overhang 제거 못함.

**정량적 괴리**

주가 / $7.84 / 큰 rerating / 1년 -63%

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

LTC rate increases 가설은 '승인 부족·claims 악화'를 사전 반증조건으로 저장한다.

#### 2. Reserve stabilization — 실패 · 논지 비중 18%

**당시 주장**

과거 assumption error가 대부분 인식됐다.

**당시 근거**

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

**이 주장이 성립하려면**

추가 strengthening 제한

**사전 반증조건**

추가 reserve/capital stress

**실제 결과**

불확실성 지속.

**정량적 괴리**

Valuation / 0.3x book / discount 축소 / book-quality discount 지속

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Reserve stabilization 가설은 '추가 reserve/capital stress'를 사전 반증조건으로 저장한다.

#### 3. MI asset floor — 부분 · 논지 비중 16%

**당시 주장**

Canada/Australia MI 지분이 equity 하방을 지지한다.

**당시 근거**

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

**이 주장이 성립하려면**

현금화 가능·proceeds 귀속

**사전 반증조건**

HoldCo liabilities가 가치 흡수

**실제 결과**

자산가치는 있었으나 주가 floor는 약했다.

**정량적 괴리**

MI stakes / 약 $2.5bn / asset floor / 실제 가치 존재

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

MI asset floor 가설은 'HoldCo liabilities가 가치 흡수'를 사전 반증조건으로 저장한다.

#### 4. Separation catalyst — 실패 · 논지 비중 16%

**당시 주장**

life/annuity sale 또는 LTC separation이 가치를 해방한다.

**당시 근거**

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

**이 주장이 성립하려면**

regulatory approval·buyer

**사전 반증조건**

구조개편 지연

**실제 결과**

가치 crystallization이 오래 걸렸다.

**정량적 괴리**

LTC / remedial actions / reserve 안정 / 불확실성 장기 지속

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Separation catalyst 가설은 '구조개편 지연'를 사전 반증조건으로 저장한다.

#### 5. Normalized EPS — 실패 · 논지 비중 16%

**당시 주장**

약 5x earnings는 과도한 할인이다.

**당시 근거**

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

**이 주장이 성립하려면**

earnings quality 안정

**사전 반증조건**

reserve-driven volatility

**실제 결과**

normalized EPS 정의 자체가 불안정했다.

**정량적 괴리**

1년 약 -63%, 2년 -48%, 3년 -65%, 5년 -57%. 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Normalized EPS 가설은 'reserve-driven volatility'를 사전 반증조건으로 저장한다.

#### 6. 0.3x book rerating — 실패 · 논지 비중 16%

**당시 주장**

book discount가 정상화된다.

**당시 근거**

LTC industry가 morbidity·mortality·interest·lapse assumptions를 과거에 크게 잘못 잡았지만 Genworth는 이미 reserve strengthening과 premium rate increases를 진행 중이며 시장이 영구손실을 과대평가한다고 봤다. MI stakes가 강한 asset floor를 제공하고 life/annuity sale 또는 LTC 분리도 catalyst가 될 수 있다고 주장했다.

**이 주장이 성립하려면**

book value가 economic value에 근접

**사전 반증조건**

tail liability가 book을 왜곡

**실제 결과**

장기 부진.

**정량적 괴리**

1년 약 -63%, 2년 -48%, 3년 -65%, 5년 -57%. 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

0.3x book rerating 가설은 'tail liability가 book을 왜곡'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

rate increases는 진행됐지만 legacy LTC uncertainty는 사라지지 않았고 HoldCo capital flexibility도 제한됐다. 이후 Oceanwide merger가 2016년 새로운 catalyst가 됐지만 수년간 지연 후 2021년 무산됐다. '더 이상의 큰 bad news가 없다'는 핵심 확률판단이 틀렸다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 1년 약 -63%, 2년 -48%, 3년 -65%, 5년 -57%. 실패. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

0.3x book는 싸 보였지만 book의 질이 LTC assumption에 따라 움직였다. public MI stake를 asset floor로 더한 것도 HoldCo debt·regulatory capital·tax·시간을 충분히 차감하지 않았다. long-tail insurance에서는 낮은 P/B보다 reserve uncertainty의 분포가 먼저다.

### 9. 최초 검증·반증 신호와 회피 가능성

2016-02-04 — 지속적인 LTC·life capital uncertainty와 restructuring 필요성이 이어지며 'bad news is largely behind us' 가정이 약해졌다. 회피 가능성: 높음. rate-action approval과 reserve adequacy를 base-case 숫자가 아니라 range로 모델링했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

치명적 value-trap 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $7.84 | 큰 rerating | 1년 -63% | 실패 |
| Valuation | 0.3x book | discount 축소 | book-quality discount 지속 | 실패 |
| MI stakes | 약 $2.5bn | asset floor | 실제 가치 존재 | 부분 적중 |
| LTC | remedial actions | reserve 안정 | 불확실성 장기 지속 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2015-04-21 | VIC 아이디어 게시 | 0.3x book·LTC rate-action turnaround Long |
| 2016-02-04 | 최초 핵심 검증·반증 신호 | 지속적인 LTC·life capital uncertainty와 restructuring 필요성이 이어지며 'bad news is largely behind us' 가정이 약해졌다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | 1년 약 -63%, 2년 -48%, 3년 -65%, 5년 -57%. 실패. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2016-02-04 — 지속적인 LTC·life capital uncertainty와 restructuring 필요성이 이어지며 'bad news is largely behind us' 가정이 약해졌다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 높음. rate-action approval과 reserve adequacy를 base-case 숫자가 아니라 range로 모델링했어야 한다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- 1. VIC GNW 2015-04-21 원문 — Value Investors Club, 2015-04-21. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:535923b3-064a-40f3-9560-a0e4ea1ea1ad -->
## 5. 2016-04-14 — LTC reserve hole·HoldCo liquidity Short

### 결론부터

**종합판정: LTC 분석 일부 적중·증권 Short 실패.** liability analysis는 날카로웠지만 equity를 zero로 만드는 경로에서 strategic buyer와 separable MI value를 너무 낮게 봤다. distressed holding-company short는 operating loss뿐 아니라 third-party capital injection과 asset monetization의 convexity를 고려해야 한다.

**주가·증권 결과:** 6개월 약 +95%, 1년 +52%, 3년 +46%, 5년 +30% 수준으로 Short 손실. Oceanwide $5.43 bid가 큰 tail event.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

### 5. 밸류에이션과 기대수익의 연결

추가 LTC reserve 필요액을 $2bn+로 추정해 equity를 사실상 0에 가깝게 봤다. HoldCo cash 약 $1.05bn, revolver $300m, debt 약 $4.27bn과 2018 maturities를 stress. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. LTC reserve hole — 방향 적중 · 논지 비중 18%

**당시 주장**

추가 $2bn+ reserve가 필요하다.

**당시 근거**

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

**이 주장이 성립하려면**

assumptions 계속 낙관

**사전 반증조건**

rate actions/claim experience 개선

**실제 결과**

LTC overhang은 장기 지속.

**정량적 괴리**

주가 / $2.64 / equity≈0 / 1년 +52%

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

LTC reserve hole 가설은 'rate actions/claim experience 개선'를 사전 반증조건으로 저장한다.

#### 2. HoldCo liquidity — 부분 실패 · 논지 비중 18%

**당시 주장**

2018 maturities가 심각한 stress다.

**당시 근거**

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

**이 주장이 성립하려면**

subsidiary dividend 부족

**사전 반증조건**

asset monetization/외부자본

**실제 결과**

생존경로가 열렸다.

**정량적 괴리**

LTC reserve / $2bn+ 추가 추정 / 대형 charge / tail uncertainty 지속

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

HoldCo liquidity 가설은 'asset monetization/외부자본'를 사전 반증조건으로 저장한다.

#### 3. Regulatory trap — 적중 · 논지 비중 16%

**당시 주장**

자본이 regulated subs에 갇혀 equity 가치가 낮다.

**당시 근거**

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

**이 주장이 성립하려면**

regulators dividend 제한

**사전 반증조건**

capital release

**실제 결과**

실제 제약은 존재.

**정량적 괴리**

HoldCo cash / $1.05bn / liquidity stress / asset/bid로 생존

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Regulatory trap 가설은 'capital release'를 사전 반증조건으로 저장한다.

#### 4. MI insufficient — 실패 · 논지 비중 16%

**당시 주장**

MI asset가 LTC/HoldCo hole을 상쇄하지 못한다.

**당시 근거**

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

**이 주장이 성립하려면**

MI valuation 약화

**사전 반증조건**

MI strategic/public value 유지

**실제 결과**

후일 Enact로 큰 가치 확인.

**정량적 괴리**

Oceanwide / 미반영 / 없음 / $5.43 bid

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

MI insufficient 가설은 'MI strategic/public value 유지'를 사전 반증조건으로 저장한다.

#### 5. No strategic rescue — 치명적 실패 · 논지 비중 16%

**당시 주장**

buyer/외부자본이 나타날 가능성이 낮다.

**당시 근거**

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

**이 주장이 성립하려면**

LTC 때문에 buyer 회피

**사전 반증조건**

strategic buyer 등장

**실제 결과**

Oceanwide bid 발생.

**정량적 괴리**

6개월 약 +95%, 1년 +52%, 3년 +46%, 5년 +30% 수준으로 Short 손실. Oceanwide $5.43 bid가 큰 tail event.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

No strategic rescue 가설은 'strategic buyer 등장'를 사전 반증조건으로 저장한다.

#### 6. Equity zero — 실패 · 논지 비중 16%

**당시 주장**

reserve+debt로 equity가 0에 수렴한다.

**당시 근거**

Genworth LTC book이 여전히 비현실적 morbidity/lapse assumptions를 사용하고 있어 $2bn 이상 reserve strengthening이 필요하며, 자회사 dividend capacity가 약해 HoldCo가 2018 debt를 감당하기 어렵다고 주장했다. 규제당국이 LTC 분리/재편을 막거나 capital을 더 요구할 수 있다는 short였다.

**이 주장이 성립하려면**

모든 downside 동시발생

**사전 반증조건**

asset floor·bid·restructuring

**실제 결과**

주가가 오히려 상승.

**정량적 괴리**

6개월 약 +95%, 1년 +52%, 3년 +46%, 5년 +30% 수준으로 Short 손실. Oceanwide $5.43 bid가 큰 tail event.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Equity zero 가설은 'asset floor·bid·restructuring'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

LTC tail risk 자체는 사라지지 않았지만 equity는 0으로 가지 않았다. 2016년 10월 China Oceanwide가 $5.43/share 현금 인수를 발표해 주가가 급등했다. 이후 거래는 실패했으나 MI franchise와 자산가치, 자본조치가 생존가치를 제공했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 6개월 약 +95%, 1년 +52%, 3년 +46%, 5년 +30% 수준으로 Short 손실. Oceanwide $5.43 bid가 큰 tail event. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

liability analysis는 날카로웠지만 equity를 zero로 만드는 경로에서 strategic buyer와 separable MI value를 너무 낮게 봤다. distressed holding-company short는 operating loss뿐 아니라 third-party capital injection과 asset monetization의 convexity를 고려해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2016-10-23 — Oceanwide가 $5.43/share 인수를 발표하며 near-zero equity thesis가 즉시 반증됐다. 회피 가능성: 매우 높음. bid 발표 즉시 Short를 재평가해야 했고, 사전에 MI franchise의 standalone strategic value를 tail scenario로 포함했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

LTC 분석 일부 적중·증권 Short 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $2.64 | equity≈0 | 1년 +52% | 실패 |
| LTC reserve | $2bn+ 추가 추정 | 대형 charge | tail uncertainty 지속 | 부분 적중 |
| HoldCo cash | $1.05bn | liquidity stress | asset/bid로 생존 | 과도 |
| Oceanwide | 미반영 | 없음 | $5.43 bid | 치명적 누락 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-04-14 | VIC 아이디어 게시 | LTC reserve hole·HoldCo liquidity Short |
| 2016-10-23 | 최초 핵심 검증·반증 신호 | Oceanwide가 $5.43/share 인수를 발표하며 near-zero equity thesis가 즉시 반증됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | 6개월 약 +95%, 1년 +52%, 3년 +46%, 5년 +30% 수준으로 Short 손실. Oceanwide $5.43 bid가 큰 tail event. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2016-10-23 — Oceanwide가 $5.43/share 인수를 발표하며 near-zero equity thesis가 즉시 반증됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. bid 발표 즉시 Short를 재평가해야 했고, 사전에 MI franchise의 standalone strategic value를 tail scenario로 포함했어야 한다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- 1. VIC GNW 2016-04-14 원문 — Value Investors Club, 2016-04-14. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:a41fef5f-3a42-4817-b2f1-d9cfe6eca7db -->
## 6. 2017-01-15 — Oceanwide $5.43 merger-arb Long

### 결론부터

**종합판정: 이벤트 실패.** deal/no-deal SOTP를 만든 점은 좋았지만 regulatory/financing path의 duration을 심각하게 과소평가했다. 중국 buyer·보험규제·미국 national-security·financing을 동시에 통과해야 하는 거래는 각 조건의 상관관계를 고려해야 한다.

**주가·증권 결과:** $3.88에서 $5.43 cash deal을 기대했지만 거래는 수차례 연장 뒤 2021년 종료. 1년 수익률 약 -17%.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

### 5. 밸류에이션과 기대수익의 연결

Deal close시 $5.43, 약 +39.9%. Standalone SOTP $5.36~7.32, severe downside floor $3.39로 추정해 6~9개월 높은 expected value를 주장. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Regulatory approval — 부분 실패 · 논지 비중 18%

**당시 주장**

복수 규제승인을 통과할 확률이 높다.

**당시 근거**

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

**이 주장이 성립하려면**

CFIUS·state approvals 관리 가능

**사전 반증조건**

승인/조건 장기화

**실제 결과**

여러 조건과 financing이 계속 지연.

**정량적 괴리**

주가 / $3.88 / $5.43 cash / 1년 약 -17%

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Regulatory approval 가설은 '승인/조건 장기화'를 사전 반증조건으로 저장한다.

#### 2. Oceanwide financing — 실패 · 논지 비중 18%

**당시 주장**

buyer가 자금을 확실히 조달한다.

**당시 근거**

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

**이 주장이 성립하려면**

strategic commitment·funding access

**사전 반증조건**

중국 자본통제·funding shortfall

**실제 결과**

2021 financing 불확실성 핵심.

**정량적 괴리**

Deal probability / 75%+ / 6~9개월 close / 2021 종료

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Oceanwide financing 가설은 '중국 자본통제·funding shortfall'를 사전 반증조건으로 저장한다.

#### 3. 6~9m closing — 실패 · 논지 비중 16%

**당시 주장**

빠른 종결로 높은 annualized IRR이 가능하다.

**당시 근거**

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

**이 주장이 성립하려면**

remaining steps 제한

**사전 반증조건**

반복 연장

**실제 결과**

수년 지연.

**정량적 괴리**

Standalone SOTP / $5.36~7.32 / floor 제공 / 주가 변동성 지속

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

6~9m closing 가설은 '반복 연장'를 사전 반증조건으로 저장한다.

#### 4. Standalone value — 부분 적중 · 논지 비중 16%

**당시 주장**

deal break에도 MI assets가 $5+ 가치를 지지한다.

**당시 근거**

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

**이 주장이 성립하려면**

MI franchise 안정

**사전 반증조건**

LTC/HoldCo liabilities 흡수

**실제 결과**

후일 Enact가 가치 확인했지만 당시 discount 지속.

**정량적 괴리**

Downside floor / $3.39 / deal break 방어 / 거래 지연 중 $3 아래 구간 경험

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Standalone value 가설은 'LTC/HoldCo liabilities 흡수'를 사전 반증조건으로 저장한다.

#### 5. Downside floor — 부분 실패 · 논지 비중 16%

**당시 주장**

U.S. Life/LTC를 0으로 둬도 $3.39다.

**당시 근거**

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

**이 주장이 성립하려면**

other assets monetizable

**사전 반증조건**

time/liquidity discount

**실제 결과**

floor는 완벽하지 않았다.

**정량적 괴리**

$3.88에서 $5.43 cash deal을 기대했지만 거래는 수차례 연장 뒤 2021년 종료. 1년 수익률 약 -17%.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Downside floor 가설은 'time/liquidity discount'를 사전 반증조건으로 저장한다.

#### 6. $5.43 payoff — 실패 · 논지 비중 16%

**당시 주장**

75%+ close probability로 expected value가 높다.

**당시 근거**

CFIUS·보험규제·중국 자본통제에도 deal completion probability를 75%+로 봤고, Oceanwide의 strategic commitment와 standalone MI value가 downside를 제한한다고 주장했다. 거래가 깨져도 U.S. Life/LTC를 0으로 둔 SOTP가 $3대 중반을 지지한다고 계산했다.

**이 주장이 성립하려면**

financing close

**사전 반증조건**

deal termination

**실제 결과**

event thesis 실패.

**정량적 괴리**

$3.88에서 $5.43 cash deal을 기대했지만 거래는 수차례 연장 뒤 2021년 종료. 1년 수익률 약 -17%.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

$5.43 payoff 가설은 'deal termination'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

거래는 예상기간을 훨씬 넘어 수년간 지연됐다. 2021년 1월 회사는 financing 불확실성 때문에 merger end date를 더 연장하지 않았고, 4월 6일 계약을 공식 종료했다. event-time probability가 핵심적으로 틀렸다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 $3.88에서 $5.43 cash deal을 기대했지만 거래는 수차례 연장 뒤 2021년 종료. 1년 수익률 약 -17%. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

deal/no-deal SOTP를 만든 점은 좋았지만 regulatory/financing path의 duration을 심각하게 과소평가했다. 중국 buyer·보험규제·미국 national-security·financing을 동시에 통과해야 하는 거래는 각 조건의 상관관계를 고려해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-06-01 — 거래가 반복 연장되고 financing/regulatory closing이 지연되면서 6~9개월 event thesis가 이미 무너졌다. 회피 가능성: 높음. time-to-close가 base horizon을 넘긴 순간 annualized IRR을 다시 계산하고 probability를 낮췄어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

이벤트 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $3.88 | $5.43 cash | 1년 약 -17% | 실패 |
| Deal probability | 75%+ | 6~9개월 close | 2021 종료 | 실패 |
| Standalone SOTP | $5.36~7.32 | floor 제공 | 주가 변동성 지속 | 부분 |
| Downside floor | $3.39 | deal break 방어 | 거래 지연 중 $3 아래 구간 경험 | 과도 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-01-15 | VIC 아이디어 게시 | Oceanwide $5.43 merger-arb Long |
| 2018-06-01 | 최초 핵심 검증·반증 신호 | 거래가 반복 연장되고 financing/regulatory closing이 지연되면서 6~9개월 event thesis가 이미 무너졌다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | $3.88에서 $5.43 cash deal을 기대했지만 거래는 수차례 연장 뒤 2021년 종료. 1년 수익률 약 -17%. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2018-06-01 — 거래가 반복 연장되고 financing/regulatory closing이 지연되면서 6~9개월 event thesis가 이미 무너졌다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 높음. time-to-close가 base horizon을 넘긴 순간 annualized IRR을 다시 계산하고 probability를 낮췄어야 한다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- 1. VIC GNW 2017-01-15 원문 — Value Investors Club, 2017-01-15. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:56a66ac6-3181-4ccf-8c34-c863afcdbe5c -->
## 7. 2019-03-15 — Deal fatigue·$5.43 merger-arb Long

### 결론부터

**종합판정: 가격·이벤트 실패.** event-driven에서 discount가 크다는 사실은 edge가 아니다. 반복 연장은 시장이 이미 포착한 closing-friction의 증거일 수 있다. standalone SOTP가 있더라도 holding-company liquidity와 LTC uncertainty 때문에 즉시 실현 가능한 cash floor가 아니었다.

**주가·증권 결과:** $4 부근에서 $5.43을 기대했지만 거래 미종결. 1~3년 수익률은 대체로 부진/보합.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

### 5. 밸류에이션과 기대수익의 연결

$5.43 deal price 대비 약 35% spread. Standalone SOTP도 LTC를 0으로 두고 약 $5로 보아 downside가 제한적이라고 주장. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Deal fatigue mispricing — 실패 · 논지 비중 18%

**당시 주장**

긴 지연 때문에 market이 과도하게 비관한다.

**당시 근거**

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

**이 주장이 성립하려면**

remaining approvals manageable

**사전 반증조건**

지연이 실제 structural friction

**실제 결과**

지연은 실제 위험 신호였다.

**정량적 괴리**

주가 / 약 $4 / $5.43 / 1~3년 부진

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Deal fatigue mispricing 가설은 '지연이 실제 structural friction'를 사전 반증조건으로 저장한다.

#### 2. Financing — 실패 · 논지 비중 18%

**당시 주장**

Oceanwide financing이 곧 완료된다.

**당시 근거**

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

**이 주장이 성립하려면**

funding sources 확정

**사전 반증조건**

중국 자본/financing 제약

**실제 결과**

끝내 해결되지 못함.

**정량적 괴리**

Spread / 약 35% / 단기 수렴 / 수년 미수렴

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Financing 가설은 '중국 자본/financing 제약'를 사전 반증조건으로 저장한다.

#### 3. Regulatory path — 부분 실패 · 논지 비중 16%

**당시 주장**

remaining approvals가 closing을 막지 않는다.

**당시 근거**

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

**이 주장이 성립하려면**

조건 충족

**사전 반증조건**

추가 review/conditions

**실제 결과**

종결 지연 지속.

**정량적 괴리**

Standalone / 약 $5 / floor / discount 지속

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Regulatory path 가설은 '추가 review/conditions'를 사전 반증조건으로 저장한다.

#### 4. Standalone floor — 부분 · 논지 비중 16%

**당시 주장**

MI value가 deal break downside를 제한한다.

**당시 근거**

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

**이 주장이 성립하려면**

asset monetization

**사전 반증조건**

LTC/HoldCo discount

**실제 결과**

장기적으로 일부 맞았지만 즉시 floor는 약함.

**정량적 괴리**

Close timing / 2019 H1 / 종결 / 2021 termination

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Standalone floor 가설은 'LTC/HoldCo discount'를 사전 반증조건으로 저장한다.

#### 5. 2019 close — 실패 · 논지 비중 16%

**당시 주장**

상반기 종결 가능성이 높다.

**당시 근거**

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

**이 주장이 성립하려면**

financing/approval 마무리

**사전 반증조건**

window miss

**실제 결과**

미종결.

**정량적 괴리**

$4 부근에서 $5.43을 기대했지만 거래 미종결. 1~3년 수익률은 대체로 부진/보합.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

2019 close 가설은 'window miss'를 사전 반증조건으로 저장한다.

#### 6. 35% spread — 실패 · 논지 비중 16%

**당시 주장**

짧은 duration 대비 attractive IRR.

**당시 근거**

시장은 deal fatigue와 Chinese-buyer skepticism 때문에 closing probability를 지나치게 낮게 보고 있다고 판단했다. 남은 규제승인과 financing이 해결되면 2019년 상반기 close가 가능하고, deal break에도 MI asset가 현재가를 지지한다고 봤다.

**이 주장이 성립하려면**

short duration

**사전 반증조건**

수년 delay

**실제 결과**

annualized IRR 붕괴.

**정량적 괴리**

$4 부근에서 $5.43을 기대했지만 거래 미종결. 1~3년 수익률은 대체로 부진/보합.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

35% spread 가설은 '수년 delay'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

거래는 2019년에도 종결되지 않았고 계속 연장됐다. 결국 2021년 financing 문제와 장기 지연 끝에 termination. spread가 시간이 지나며 carry cost와 opportunity cost를 누적했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 $4 부근에서 $5.43을 기대했지만 거래 미종결. 1~3년 수익률은 대체로 부진/보합. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

event-driven에서 discount가 크다는 사실은 edge가 아니다. 반복 연장은 시장이 이미 포착한 closing-friction의 증거일 수 있다. standalone SOTP가 있더라도 holding-company liquidity와 LTC uncertainty 때문에 즉시 실현 가능한 cash floor가 아니었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2019-06-30 — 작성자가 기대한 상반기 closing window가 지나도 거래가 종결되지 않아 event-time thesis가 반증됐다. 회피 가능성: 매우 높음. 각 extension마다 annualized expected return과 conditional probability를 업데이트했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

가격·이벤트 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | 약 $4 | $5.43 | 1~3년 부진 | 실패 |
| Spread | 약 35% | 단기 수렴 | 수년 미수렴 | 실패 |
| Standalone | 약 $5 | floor | discount 지속 | 부분 |
| Close timing | 2019 H1 | 종결 | 2021 termination | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-03-15 | VIC 아이디어 게시 | Deal fatigue·$5.43 merger-arb Long |
| 2019-06-30 | 최초 핵심 검증·반증 신호 | 작성자가 기대한 상반기 closing window가 지나도 거래가 종결되지 않아 event-time thesis가 반증됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | $4 부근에서 $5.43을 기대했지만 거래 미종결. 1~3년 수익률은 대체로 부진/보합. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2019-06-30 — 작성자가 기대한 상반기 closing window가 지나도 거래가 종결되지 않아 event-time thesis가 반증됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. 각 extension마다 annualized expected return과 conditional probability를 업데이트했어야 한다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- [1. VIC GNW 2019-03-15 원문](https://www.valueinvestorsclub.com/idea/GENWORTH_FINANCIAL_INC/4583805448) — Value Investors Club, 2019-03-15. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:8180fc98-1e4d-42ac-a27d-7289900d9d3d -->
## 8. 2020-04-14 — 2034 bonds + Oceanwide equity dual-trade

### 결론부터

**종합판정: Equity 이벤트 실패·credit thesis 부분 성공.** 같은 회사의 equity와 bond가 같은 thesis가 아님을 보여준다. Equity는 $5.43 close라는 binary event에 민감했고 bond는 asset coverage·maturity runway에 더 민감했다. 두 증권을 하나의 'deal will close' 논지로 묶지 않은 점은 좋았지만 close timing은 다시 틀렸다.

**주가·증권 결과:** Merger는 2021 종료되어 $5.43 equity payoff 실패. 장기채는 Enact IPO·debt reduction으로 credit가 개선되는 경로가 더 견조.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Genworth Financial은 2004년 GE에서 분사된 보험지주회사로, 역사적으로 미국 생명보험·장기요양보험(LTC), 고정연금, 미국·캐나다·호주 모기지보험을 함께 보유했다. 이 회사에서 가장 중요한 점은 보험계약의 회계이익보다 현금과 규제자본의 위치다. 특히 LTC는 보험료를 수십 년 먼저 받고 훗날 장기간 보험금을 지급하는 상품이므로 mortality, morbidity, lapse/persistency, claim duration, benefit utilization, rate increase 승인, 투자수익률 같은 작은 가정 변화가 장기 reserve 필요액을 크게 바꾼다. 또한 HoldCo가 보험 자회사 자본을 자유롭게 끌어올 수 없기 때문에 statutory capital, RBC, rating, 자회사 dividend capacity와 HoldCo debt maturity를 별도로 봐야 한다. 반면 mortgage insurance는 주택가격·실업률·default cycle에 민감하지만 oligopoly·규제자본 구조와 underwriting discipline이 좋아지면 큰 franchise value를 가질 수 있다. 2021년 Enact IPO 이후에는 미국 MI 자산가치가 더 투명해졌고, legacy LTC는 여전히 장기 tail liability로 남았다. 핵심 KPI는 LTC reserve development·rate-action approvals·claim incidence/termination, statutory RBC, HoldCo cash/debt maturities, MI new insurance written·loss ratio·PMIERs capital, Enact 지분가치와 자회사 배당이다.

### 2. 산업 가치사슬과 돈의 흐름

보험지주의 가치사슬은 segment마다 다르다. LTC에서는 장기간 보험료와 투자수익을 쌓아 future claims와 expenses를 지급하므로 reserve assumption이 경제성을 지배한다. Mortgage insurance에서는 mortgage origination에 붙은 premium에서 future default claim을 지급하며 housing/credit cycle과 underwriting vintage가 핵심이다. HoldCo equity로 내려오려면 각 regulated subsidiary가 충분한 statutory capital을 유지한 뒤 dividend를 올릴 수 있어야 하고, 그 cash가 HoldCo interest·debt maturities·corporate expense를 커버한 뒤에야 주주가치가 된다. 따라서 GAAP book value나 segment earnings를 단순 합산하는 SOTP는 자회사 capital trap과 long-tail reserve를 반드시 차감해야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Genworth의 장점은 오래된 보험 distribution, 대규모 in-force LTC block, mortgage-insurance underwriting platform과 후일 Enact로 분리된 MI franchise였다. 그러나 LTC에서는 오래된 book 자체가 moat가 아니라 위험이 될 수 있다. 잘못된 lapse·morbidity 가정을 수십 년간 보유한 계약은 신규 경쟁자가 없더라도 큰 reserve hole을 만든다. MI에서는 underwriting data·lender relationships·규제자본·scale이 장점이지만 housing cycle에서 손실이 비선형적으로 커진다. 따라서 'book value discount'보다 reserve adequacy, trapped capital, rating, debt maturity와 각 segment의 실제 dividend capacity를 먼저 봐야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

2034 notes 88, YTM 약 7.9%, 1년 target 101로 19.4%. Equity $3.60→deal $5.43 +51%. No-deal equity mid-case $2.50, bond는 MI asset coverage로 par에 가깝다고 판단. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. NY approval — 실패 · 논지 비중 18%

**당시 주장**

마지막 주요 규제 step이 곧 해결된다.

**당시 근거**

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

**이 주장이 성립하려면**

remaining conditions 제한

**사전 반증조건**

financing/regulatory linkage

**실제 결과**

deal 미종결.

**정량적 괴리**

Equity / $3.60 / $5.43 / +51% 기대 미실현

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

NY approval 가설은 'financing/regulatory linkage'를 사전 반증조건으로 저장한다.

#### 2. Oceanwide financing — 실패 · 논지 비중 18%

**당시 주장**

COVID 이후에도 자금조달 가능하다.

**당시 근거**

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

**이 주장이 성립하려면**

funding commitment

**사전 반증조건**

financing uncertainty

**실제 결과**

2021 핵심 실패요인.

**정량적 괴리**

2034 bond / 88 / 101 / asset monetization으로 credit 개선

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Oceanwide financing 가설은 'financing uncertainty'를 사전 반증조건으로 저장한다.

#### 3. Equity $5.43 — 실패 · 논지 비중 16%

**당시 주장**

단기 closing으로 +51%다.

**당시 근거**

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

**이 주장이 성립하려면**

deal close

**사전 반증조건**

termination

**실제 결과**

미실현.

**정량적 괴리**

Close date / 2020-06-30 / 종결 / 2021 termination

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Equity $5.43 가설은 'termination'를 사전 반증조건으로 저장한다.

#### 4. No-deal equity — 부분 · 논지 비중 16%

**당시 주장**

$2.50 정도 downside로 제한된다.

**당시 근거**

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

**이 주장이 성립하려면**

MI value

**사전 반증조건**

LTC/HoldCo stress

**실제 결과**

가격변동성 컸음.

**정량적 괴리**

Enact IPO / 잠재 asset / credit support / 2021-09 완료

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

No-deal equity 가설은 'LTC/HoldCo stress'를 사전 반증조건으로 저장한다.

#### 5. Bond asset coverage — 적중 · 논지 비중 16%

**당시 주장**

MI assets가 장기채 par recovery를 지지한다.

**당시 근거**

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

**이 주장이 성립하려면**

asset monetization 가능

**사전 반증조건**

MI value collapse

**실제 결과**

Enact IPO로 강하게 지지.

**정량적 괴리**

Merger는 2021 종료되어 $5.43 equity payoff 실패. 장기채는 Enact IPO·debt reduction으로 credit가 개선되는 경로가 더 견조.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Bond asset coverage 가설은 'MI value collapse'를 사전 반증조건으로 저장한다.

#### 6. Security separation — 강한 적중 · 논지 비중 16%

**당시 주장**

equity event risk와 bond recovery는 다르다.

**당시 근거**

COVID로 financing이 흔들렸지만 Oceanwide deal의 마지막 큰 step은 New York regulator라고 봤고 2020-06-30 close를 예상했다. 동시에 bonds는 merger가 깨져도 MI assets와 future asset monetization으로 충분히 covered라고 주장했다.

**이 주장이 성립하려면**

maturity/priority 차이

**사전 반증조건**

동일 factor collapse

**실제 결과**

실제 결과가 달라졌다.

**정량적 괴리**

Merger는 2021 종료되어 $5.43 equity payoff 실패. 장기채는 Enact IPO·debt reduction으로 credit가 개선되는 경로가 더 견조.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Security separation 가설은 '동일 factor collapse'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

equity merger arb는 실패했다. 2021년 1월 financing uncertainty가 공개됐고 4월 deal termination. 그러나 2021년 9월 Enact IPO가 완료되며 MI asset를 monetization했고 Genworth는 proceeds와 이후 distributions를 debt reduction에 활용했다. 그래서 equity event와 credit recovery의 결과가 분리됐다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 Merger는 2021 종료되어 $5.43 equity payoff 실패. 장기채는 Enact IPO·debt reduction으로 credit가 개선되는 경로가 더 견조. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

같은 회사의 equity와 bond가 같은 thesis가 아님을 보여준다. Equity는 $5.43 close라는 binary event에 민감했고 bond는 asset coverage·maturity runway에 더 민감했다. 두 증권을 하나의 'deal will close' 논지로 묶지 않은 점은 좋았지만 close timing은 다시 틀렸다.

### 9. 최초 검증·반증 신호와 회피 가능성

2021-01-04 — 회사와 Oceanwide가 financing 불확실성 때문에 merger end date를 더 연장하지 않는다고 발표해 equity event thesis가 크게 훼손됐다. 회피 가능성: 높음. equity는 Jan 2021에 재평가해야 했지만 credit는 별도 recovery analysis로 유지할 수 있었다.

### 10. 최종 판정·반사실·재사용 교훈

Equity 이벤트 실패·credit thesis 부분 성공. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Equity | $3.60 | $5.43 | +51% 기대 미실현 | 실패 |
| 2034 bond | 88 | 101 | asset monetization으로 credit 개선 | 부분 성공 |
| Close date | 2020-06-30 | 종결 | 2021 termination | 실패 |
| Enact IPO | 잠재 asset | credit support | 2021-09 완료 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-04-14 | VIC 아이디어 게시 | 2034 bonds + Oceanwide equity dual-trade |
| 2021-01-04 | 최초 핵심 검증·반증 신호 | 회사와 Oceanwide가 financing 불확실성 때문에 merger end date를 더 연장하지 않는다고 발표해 equity event thesis가 크게 훼손됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | Merger는 2021 종료되어 $5.43 equity payoff 실패. 장기채는 Enact IPO·debt reduction으로 credit가 개선되는 경로가 더 견조. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2021-01-04 — 회사와 Oceanwide가 financing 불확실성 때문에 merger end date를 더 연장하지 않는다고 발표해 equity event thesis가 크게 훼손됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 높음. equity는 Jan 2021에 재평가해야 했지만 credit는 별도 recovery analysis로 유지할 수 있었다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- [1. VIC GNW 2020-04-14 원문](https://www.valueinvestorsclub.com/idea/GENWORTH_FINANCIAL_INC/6595209000) — Value Investors Club, 2020-04-14. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Genworth 2009 liquidity and Canada MI IPO update](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-09-159677/dex991.htm) — Genworth / SEC, 2009-07-29. Canada MI IPO proceeds와 2009 debt repayment 확인
- [3. Genworth Q3 2014 LTC review](https://investor.genworth.com/sec-filings/all-sec-filings/content/0001193125-14-398801/d810251dex991.htm) — Genworth / SEC, 2014-11-05. LTC claim reserve $531m 증가 및 after-tax charge 확인
- [4. Genworth and Oceanwide transaction update](https://investor.genworth.com/news-events/press-releases/detail/92/genworth-and-oceanwide-provide-transaction-update-genworth) — Genworth, 2021-01-04. merger end date 미연장·financing uncertainty 확인
- [5. Genworth terminates Oceanwide merger](https://investor.genworth.com/news-events/press-releases/detail/85/genworth-announces-termination-of-merger-agreement-with) — Genworth, 2021-04-06. Oceanwide merger 종료 확인
- [6. Enact IPO completion](https://investor.genworth.com/news-events/press-releases/detail/73/genworth-financial-announces-completion-of-the-ipo-of-enact) — Genworth, 2021-09-20. Enact IPO와 MI monetization 확인
- [7. Enact 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1823529/000182352922000038/act-20211231.htm) — SEC, 2022-02-25. MI franchise economics·capital 확인
- [8. Genworth historical prices](https://www.digrin.com/stocks/detail/GNW/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증

---
# ASSURED GUARANTY LTD (AGO) — 기업과 비즈니스

## 1. 무슨 기업인가

Assured Guaranty는 지방채·공공인프라·일부 structured finance 채권의 원리금 지급을 보증하는 financial guaranty, 즉 monoline insurer다. 고객은 bond issuer나 투자자이고, Assured는 보증 premium을 upfront 또는 장기간에 걸쳐 받아 장기 credit loss를 떠안는다. 손실발생이 평상시에는 매우 낮아 ROE와 earnings가 안정적으로 보이지만, 한 번의 신용사이클·구조화상품 손실·지방정부 위기가 수년치 premium을 훼손할 수 있다. 2008 금융위기 당시 많은 monoline 경쟁사가 붕괴했지만 Assured는 살아남았고 2009년 FSA를 인수해 규모와 시장지위를 확대했다. 핵심 KPI는 insured par, new business production, premium written/earned, expected loss·loss reserves, rating-agency capital, leverage, adjusted book value, Puerto Rico 등 집중 exposure, 그리고 자사주 매입이다.

## 2. 산업 가치사슬과 돈의 흐름

Financial guaranty의 돈 흐름은 보증계약 체결 → premium 수취 → 장기간 unearned premium recognition → 극히 낮은 평시 claim → 위기 때 대규모 claim 지급의 구조다. 단기 EPS보다 신규보증의 risk-adjusted pricing, reserve adequacy와 rating capital이 더 중요하다. 시장이 약할 때 경쟁사가 퇴출되면 신규사업 pricing은 좋아질 수 있지만 기존 legacy book의 tail loss가 동시에 커질 수 있다. Equity value는 GAAP book, adjusted book, unearned premium의 미래이익, 예상손실, capital required와 capital return을 함께 봐야 한다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Assured의 경쟁우위는 AAA/AA급 claims-paying capacity, underwriting history, municipal issuer/investor network와 2009년 FSA 인수 이후의 규모다. 위기 때 경쟁사가 퇴출되면 surviving insurer가 pricing power를 얻을 수 있다. 그러나 rating agency가 capital requirement를 높이거나 structured/municipal tail loss가 예상보다 커지면 신규사업 기회가 있어도 equity 가치가 훼손된다. 따라서 adjusted book value와 normalized EPS에만 multiple을 붙이지 말고 실제 loss emergence와 rating capital을 함께 추적해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2008-01-18 | Long | Long | AAA survivor·monoline dislocation Long | 금융위기 중 1년 약 -55%로 큰 drawdown. 이후 FSA 인수와 survivor status로 회복했으나 초기 $50~60 target/timing은 실패. | 프랜차이즈 통찰 적중·타이밍/하방 실패 |
| 2009-11-16 | Long | Long | FSA accretion·adjusted book $50 Long | 1년 약 -32%, 2년 -57%, 3년 -47%; 5년 뒤에야 대체로 원가 회복. $50 단기 target 실패. | 사업 지위 적중·valuation crystallization 실패 |

---

<!-- idea:00efc056-201e-47e2-8502-57e786322b1e -->
## 1. 2008-01-18 — AAA survivor·monoline dislocation Long

### 결론부터

**종합판정: 프랜차이즈 통찰 적중·타이밍/하방 실패.** 위기 후 market structure를 잘 봤지만 'survivor'와 '주가가 지금 바닥'을 동일시했다. tail-credit insurer는 실제 loss가 작아도 rating agency capital과 market confidence가 equity를 먼저 압박할 수 있다.

**주가·증권 결과:** 금융위기 중 1년 약 -55%로 큰 drawdown. 이후 FSA 인수와 survivor status로 회복했으나 초기 $50~60 target/timing은 실패.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Assured Guaranty는 지방채·공공인프라·일부 structured finance 채권의 원리금 지급을 보증하는 financial guaranty, 즉 monoline insurer다. 고객은 bond issuer나 투자자이고, Assured는 보증 premium을 upfront 또는 장기간에 걸쳐 받아 장기 credit loss를 떠안는다. 손실발생이 평상시에는 매우 낮아 ROE와 earnings가 안정적으로 보이지만, 한 번의 신용사이클·구조화상품 손실·지방정부 위기가 수년치 premium을 훼손할 수 있다. 2008 금융위기 당시 많은 monoline 경쟁사가 붕괴했지만 Assured는 살아남았고 2009년 FSA를 인수해 규모와 시장지위를 확대했다. 핵심 KPI는 insured par, new business production, premium written/earned, expected loss·loss reserves, rating-agency capital, leverage, adjusted book value, Puerto Rico 등 집중 exposure, 그리고 자사주 매입이다.

### 2. 산업 가치사슬과 돈의 흐름

Financial guaranty의 돈 흐름은 보증계약 체결 → premium 수취 → 장기간 unearned premium recognition → 극히 낮은 평시 claim → 위기 때 대규모 claim 지급의 구조다. 단기 EPS보다 신규보증의 risk-adjusted pricing, reserve adequacy와 rating capital이 더 중요하다. 시장이 약할 때 경쟁사가 퇴출되면 신규사업 pricing은 좋아질 수 있지만 기존 legacy book의 tail loss가 동시에 커질 수 있다. Equity value는 GAAP book, adjusted book, unearned premium의 미래이익, 예상손실, capital required와 capital return을 함께 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Assured의 경쟁우위는 AAA/AA급 claims-paying capacity, underwriting history, municipal issuer/investor network와 2009년 FSA 인수 이후의 규모다. 위기 때 경쟁사가 퇴출되면 surviving insurer가 pricing power를 얻을 수 있다. 그러나 rating agency가 capital requirement를 높이거나 structured/municipal tail loss가 예상보다 커지면 신규사업 기회가 있어도 equity 가치가 훼손된다. 따라서 adjusted book value와 normalized EPS에만 multiple을 붙이지 말고 실제 loss emergence와 rating capital을 함께 추적해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

2008 earnings 약 6x, 2009 약 3.5x. 2009 EPS $5+와 1.7~2.0x book을 적용해 $50~60 target, 180~240% upside. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Low subprime exposure — 적중 · 논지 비중 18%

**당시 주장**

peer 대비 risky CDO/subprime exposure가 낮다.

**당시 근거**

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

**이 주장이 성립하려면**

underwriting data 정확

**사전 반증조건**

hidden correlated losses

**실제 결과**

Assured는 peers보다 잘 생존.

**정량적 괴리**

주가 / 약 $13.9 / $50~60 / 1년 약 -55%

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Low subprime exposure 가설은 'hidden correlated losses'를 사전 반증조건으로 저장한다.

#### 2. AAA capital — 부분 적중 · 논지 비중 18%

**당시 주장**

stress loss를 감당할 cushion이 충분하다.

**당시 근거**

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

**이 주장이 성립하려면**

rating capital 유지

**사전 반증조건**

agency capital demand 급증

**실제 결과**

생존했지만 equity volatility 컸다.

**정량적 괴리**

2009 EPS / $5+ 기대 / 저평가 / crisis로 earnings quality 변동

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

AAA capital 가설은 'agency capital demand 급증'를 사전 반증조건으로 저장한다.

#### 3. Competitor exit — 부분 · 논지 비중 16%

**당시 주장**

peer failures가 신규사업 pricing을 높인다.

**당시 근거**

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

**이 주장이 성립하려면**

시장 수요 유지

**사전 반증조건**

monoline demand 자체 붕괴

**실제 결과**

시장규모는 줄었지만 dominant position 확보.

**정량적 괴리**

AAA capital / 충분 / rating 유지 / survived

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Competitor exit 가설은 'monoline demand 자체 붕괴'를 사전 반증조건으로 저장한다.

#### 4. 20%+ ROE — 부분 · 논지 비중 16%

**당시 주장**

새 business pricing으로 높은 returns가 가능하다.

**당시 근거**

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

**이 주장이 성립하려면**

capital-efficient production

**사전 반증조건**

capital requirement 상승

**실제 결과**

장기 economics는 개선됐지만 timing 지연.

**정량적 괴리**

FSA / 미반영/기회 / 업계 consolidation / 2009 인수

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

20%+ ROE 가설은 'capital requirement 상승'를 사전 반증조건으로 저장한다.

#### 5. $50~60 target — 실패 · 논지 비중 16%

**당시 주장**

1.7~2x book rerating 가능.

**당시 근거**

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

**이 주장이 성립하려면**

book quality·market confidence 회복

**사전 반증조건**

crisis multiple collapse

**실제 결과**

초기 horizon 실패.

**정량적 괴리**

금융위기 중 1년 약 -55%로 큰 drawdown. 이후 FSA 인수와 survivor status로 회복했으나 초기 $50~60 target/timing은 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

$50~60 target 가설은 'crisis multiple collapse'를 사전 반증조건으로 저장한다.

#### 6. Downside limited — 실패 · 논지 비중 16%

**당시 주장**

underwriting quality가 주가 floor를 만든다.

**당시 근거**

다른 monoline과 달리 post-2004 CDO를 거의 보증하지 않았고 subprime exposure가 제한적이며 AAA capital cushion이 충분하다고 주장했다. 경쟁사 붕괴 후 신규 municipal/structured pricing이 좋아져 20%+ ROE를 낼 survivor라고 봤다.

**이 주장이 성립하려면**

loss estimates 안정

**사전 반증조건**

liquidity/rating panic

**실제 결과**

1년 큰 drawdown.

**정량적 괴리**

금융위기 중 1년 약 -55%로 큰 drawdown. 이후 FSA 인수와 survivor status로 회복했으나 초기 $50~60 target/timing은 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Downside limited 가설은 'liquidity/rating panic'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Assured는 실제로 생존했고 2009년 FSA를 인수해 업계 지위를 강화했다. 그러나 2008 crisis 중 rating/capital fear와 mark-to-market, legacy structured exposure로 주가는 크게 하락했다. 장기 franchise direction은 맞았지만 downside distribution과 시간은 크게 틀렸다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 금융위기 중 1년 약 -55%로 큰 drawdown. 이후 FSA 인수와 survivor status로 회복했으나 초기 $50~60 target/timing은 실패. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

위기 후 market structure를 잘 봤지만 'survivor'와 '주가가 지금 바닥'을 동일시했다. tail-credit insurer는 실제 loss가 작아도 rating agency capital과 market confidence가 equity를 먼저 압박할 수 있다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-09-15 — 금융위기 심화와 monoline sector confidence collapse로 주가가 target 반대방향으로 급락하며 capital/rating path risk가 현실화됐다. 회피 가능성: 중간. 장기 franchise는 유지하되 position size와 entry timing을 rating-capital stress에 맞춰야 했다.

### 10. 최종 판정·반사실·재사용 교훈

프랜차이즈 통찰 적중·타이밍/하방 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | 약 $13.9 | $50~60 | 1년 약 -55% | 단기 실패 |
| 2009 EPS | $5+ 기대 | 저평가 | crisis로 earnings quality 변동 | 부분 |
| AAA capital | 충분 | rating 유지 | survived | 적중 |
| FSA | 미반영/기회 | 업계 consolidation | 2009 인수 | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2008-01-18 | VIC 아이디어 게시 | AAA survivor·monoline dislocation Long |
| 2008-09-15 | 최초 핵심 검증·반증 신호 | 금융위기 심화와 monoline sector confidence collapse로 주가가 target 반대방향으로 급락하며 capital/rating path risk가 현실화됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | 금융위기 중 1년 약 -55%로 큰 drawdown. 이후 FSA 인수와 survivor status로 회복했으나 초기 $50~60 target/timing은 실패. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2008-09-15 — 금융위기 심화와 monoline sector confidence collapse로 주가가 target 반대방향으로 급락하며 capital/rating path risk가 현실화됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 중간. 장기 franchise는 유지하되 position size와 entry timing을 rating-capital stress에 맞춰야 했다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- [1. VIC AGO 2008-01-18 원문](https://www.valueinvestorsclub.com/idea/Assured_Guaranty_Ltd/7060974311) — Value Investors Club, 2008-01-18. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Assured Guaranty history](https://assuredguaranty.com/about-us/history) — Assured Guaranty, 2024-01-31. FSA 인수 및 회사 역사 확인
- [3. Assured/FSA transaction filing](https://www.sec.gov/Archives/edgar/data/913357/000110465909042440/a09-17606_18k.htm) — SEC, 2009-07-01. FSA acquisition closing 관련 확인
- [4. Assured Guaranty annual reports](https://assuredguaranty.com/investor-information/by-company/assured-guaranty-ltd/sec-filings) — Assured Guaranty, 2010-12-31. insured portfolio·loss reserves·capital 자료
- [5. Assured Guaranty financial information](https://assuredguaranty.com/investor-information) — Assured Guaranty, 2024-01-31. adjusted book·capital return 장기검증
- 6. Assured Guaranty historical prices — Macrotrends / market history, 2024-01-31. 역사적 가격경로 교차검증

---

<!-- idea:0db67587-f040-44d4-8e43-868e6fa0cd63 -->
## 2. 2009-11-16 — FSA accretion·adjusted book $50 Long

### 결론부터

**종합판정: 사업 지위 적중·valuation crystallization 실패.** 가장 큰 오류는 adjusted book와 normalized EPS를 '현재 시장이 곧 인정해야 하는 가치'로 본 것이다. long-tail guaranty는 unearned premium을 value로 더하는 동시에 future capital requirement와 tail loss distribution도 함께 차감해야 한다.

**주가·증권 결과:** 1년 약 -32%, 2년 -57%, 3년 -47%; 5년 뒤에야 대체로 원가 회복. $50 단기 target 실패.

**Thesis / Process 점수:** 5.8 / 7.5

### 1. 무슨 기업인가

Assured Guaranty는 지방채·공공인프라·일부 structured finance 채권의 원리금 지급을 보증하는 financial guaranty, 즉 monoline insurer다. 고객은 bond issuer나 투자자이고, Assured는 보증 premium을 upfront 또는 장기간에 걸쳐 받아 장기 credit loss를 떠안는다. 손실발생이 평상시에는 매우 낮아 ROE와 earnings가 안정적으로 보이지만, 한 번의 신용사이클·구조화상품 손실·지방정부 위기가 수년치 premium을 훼손할 수 있다. 2008 금융위기 당시 많은 monoline 경쟁사가 붕괴했지만 Assured는 살아남았고 2009년 FSA를 인수해 규모와 시장지위를 확대했다. 핵심 KPI는 insured par, new business production, premium written/earned, expected loss·loss reserves, rating-agency capital, leverage, adjusted book value, Puerto Rico 등 집중 exposure, 그리고 자사주 매입이다.

### 2. 산업 가치사슬과 돈의 흐름

Financial guaranty의 돈 흐름은 보증계약 체결 → premium 수취 → 장기간 unearned premium recognition → 극히 낮은 평시 claim → 위기 때 대규모 claim 지급의 구조다. 단기 EPS보다 신규보증의 risk-adjusted pricing, reserve adequacy와 rating capital이 더 중요하다. 시장이 약할 때 경쟁사가 퇴출되면 신규사업 pricing은 좋아질 수 있지만 기존 legacy book의 tail loss가 동시에 커질 수 있다. Equity value는 GAAP book, adjusted book, unearned premium의 미래이익, 예상손실, capital required와 capital return을 함께 봐야 한다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Assured의 경쟁우위는 AAA/AA급 claims-paying capacity, underwriting history, municipal issuer/investor network와 2009년 FSA 인수 이후의 규모다. 위기 때 경쟁사가 퇴출되면 surviving insurer가 pricing power를 얻을 수 있다. 그러나 rating agency가 capital requirement를 높이거나 structured/municipal tail loss가 예상보다 커지면 신규사업 기회가 있어도 equity 가치가 훼손된다. 따라서 adjusted book value와 normalized EPS에만 multiple을 붙이지 말고 실제 loss emergence와 rating capital을 함께 추적해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

FY+1 consensus EPS $3.70, FY+2 $4.41이나 normalized no-loss run-rate operating EPS 약 $7.20로 추정. GAAP BVPS $17.52, tangible $16.88, BV ex MTM/full reserve $21.27, adjusted BV에 unearned premium economics를 더해 $50.69. Target $50. 사후에는 segment assets → reserve/capital → subsidiary dividend capacity → HoldCo debt → event probability/duration → 기존 보통주·채권 payoff 순서로 다시 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. FSA accretion — 적중 · 논지 비중 18%

**당시 주장**

FSA 인수로 scale·earnings·market share가 크게 좋아진다.

**당시 근거**

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

**이 주장이 성립하려면**

integration 성공

**사전 반증조건**

legacy loss 증가

**실제 결과**

dominant franchise가 됐다.

**정량적 괴리**

주가 / $21.66 / $50 / 3년 약 -47%

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

FSA accretion 가설은 'legacy loss 증가'를 사전 반증조건으로 저장한다.

#### 2. Moody's risk — 적중 · 논지 비중 18%

**당시 주장**

rating downgrade tail이 대부분 제거됐다.

**당시 근거**

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

**이 주장이 성립하려면**

capital adequate

**사전 반증조건**

agency stress 재확대

**실제 결과**

생존/rating 유지.

**정량적 괴리**

Normalized EPS / $7.20 / rerating / reported/adjusted earnings 변동

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Moody's risk 가설은 'agency stress 재확대'를 사전 반증조건으로 저장한다.

#### 3. Normalized losses — 부분 실패 · 논지 비중 16%

**당시 주장**

crisis loss가 정상화되면 $7.20 operating EPS다.

**당시 근거**

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

**이 주장이 성립하려면**

legacy claims 제한

**사전 반증조건**

tail losses 지속

**실제 결과**

normalization이 느리고 변동적이었다.

**정량적 괴리**

Adj book / $50.69 / 가격 수렴 / 장기 discount 지속

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

Normalized losses 가설은 'tail losses 지속'를 사전 반증조건으로 저장한다.

#### 4. Adjusted book — 부분 · 논지 비중 16%

**당시 주장**

unearned premium economics 포함 $50.69 가치다.

**당시 근거**

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

**이 주장이 성립하려면**

future premiums 실현

**사전 반증조건**

capital/loss drag

**실제 결과**

장기 discount 지속.

**정량적 괴리**

FSA / accretive / dominant franchise / 2009 인수 후 leading position

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Adjusted book 가설은 'capital/loss drag'를 사전 반증조건으로 저장한다.

#### 5. Municipal dominance — 적중 · 논지 비중 16%

**당시 주장**

primary muni insurer로 pricing power가 생긴다.

**당시 근거**

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

**이 주장이 성립하려면**

insured demand 유지

**사전 반증조건**

monoline penetration 축소

**실제 결과**

시장지위는 강해졌다.

**정량적 괴리**

1년 약 -32%, 2년 -57%, 3년 -47%; 5년 뒤에야 대체로 원가 회복. $50 단기 target 실패.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐지만 security payoff와 timing은 별도 검증해야 한다.

**재사용할 교훈**

Municipal dominance 가설은 'monoline penetration 축소'를 사전 반증조건으로 저장한다.

#### 6. $50 target — 실패 · 논지 비중 16%

**당시 주장**

사업지위+adj book가 주가에 빠르게 반영된다.

**당시 근거**

Moody's downgrade tail이 줄고 FSA acquisition이 크게 accretive하며 Assured가 사실상 primary municipal guarantor로 남았다고 봤다. normalized loss level로 돌아가면 $7+ operating EPS와 $50 adjusted book이 드러날 것이라고 주장했다.

**이 주장이 성립하려면**

catalyst 존재

**사전 반증조건**

crystallization 부재

**실제 결과**

초기 horizon 실패.

**정량적 괴리**

1년 약 -32%, 2년 -57%, 3년 -47%; 5년 뒤에야 대체로 원가 회복. $50 단기 target 실패.

**분석 오류·핵심**

asset/book/normalized earnings를 economic equity value로 옮길 때 tail liability·capital trap·duration을 충분히 stress하지 않았다.

**재사용할 교훈**

$50 target 가설은 'crystallization 부재'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

FSA 인수로 Assured가 업계 dominant survivor가 된 것은 맞았다. 그러나 legacy structured losses, municipal/Puerto Rico uncertainty와 monoline demand 축소가 multiple을 오랫동안 억눌렀다. adjusted book가 즉시 주가로 crystallize되지 않았다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 1년 약 -32%, 2년 -57%, 3년 -47%; 5년 뒤에야 대체로 원가 회복. $50 단기 target 실패. 보험사업 생존, reserve quality, event, valuation과 가격을 별도 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가장 큰 오류는 adjusted book와 normalized EPS를 '현재 시장이 곧 인정해야 하는 가치'로 본 것이다. long-tail guaranty는 unearned premium을 value로 더하는 동시에 future capital requirement와 tail loss distribution도 함께 차감해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2010-12-31 — FSA integration에도 주가가 지속 부진해 $50 adjusted-book crystallization이 단기간에 일어나지 않는다는 점이 확인됐다. 회피 가능성: 높음. adjusted book discount의 catalyst를 구체화하고, 없다면 duration을 길게 잡아야 했다.

### 10. 최종 판정·반사실·재사용 교훈

사업 지위 적중·valuation crystallization 실패. 보험에서는 낮은 P/B·adjusted book가 아니라 economic reserve와 capital fungibility가 먼저다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $21.66 | $50 | 3년 약 -47% | 실패 |
| Normalized EPS | $7.20 | rerating | reported/adjusted earnings 변동 | 부분 |
| Adj book | $50.69 | 가격 수렴 | 장기 discount 지속 | 실패 |
| FSA | accretive | dominant franchise | 2009 인수 후 leading position | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2009-11-16 | VIC 아이디어 게시 | FSA accretion·adjusted book $50 Long |
| 2010-12-31 | 최초 핵심 검증·반증 신호 | FSA integration에도 주가가 지속 부진해 $50 adjusted-book crystallization이 단기간에 일어나지 않는다는 점이 확인됐다. |
| 2009-12-31 | 금융위기 후 capital 재평가 | MI·liquidity·rating 자본을 재검증 |
| 2014-11-05 | LTC liability 재평가 | Genworth 장기 reserve risk가 시장 핵심변수로 전환 |
| 2021-09-20 | 구조적 자산가치 확인 | Enact IPO로 Genworth MI asset가 공개시장 가치로 crystallize |
| 2024-01-31 | 고정 평가기준일 | 1년 약 -32%, 2년 -57%, 3년 -47%; 5년 뒤에야 대체로 원가 회복. $50 단기 target 실패. |

### Failure / Success Anatomy

- **근본 오류:** 보험 book/asset value를 reserve·regulatory capital·duration을 충분히 차감하지 않고 equity payoff에 직접 연결
- **최초 검증·반증 신호:** 2010-12-31 — FSA integration에도 주가가 지속 부진해 $50 adjusted-book crystallization이 단기간에 일어나지 않는다는 점이 확인됐다.
- **당시 알 수 있었나:** reserve development, statutory capital, HoldCo cash/debt, subsidiary dividends, MI losses, rating capital과 merger conditions는 공개자료로 재검증 가능했다.
- **피할 수 있었나:** 높음. adjusted book discount의 catalyst를 구체화하고, 없다면 duration을 길게 잡아야 했다.
- **반사실 질문:** book/asset value가 높더라도 reserve tail, trapped capital, debt maturity 또는 event duration을 반영하면 기존 보통주의 실현가치는 얼마인가?

### 주요 근거자료

- [1. VIC AGO 2009-11-16 원문](https://www.valueinvestorsclub.com/idea/ASSURED_GUARANTY_LTD/1111773402) — Value Investors Club, 2009-11-16. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Assured Guaranty history](https://assuredguaranty.com/about-us/history) — Assured Guaranty, 2024-01-31. FSA 인수 및 회사 역사 확인
- [3. Assured/FSA transaction filing](https://www.sec.gov/Archives/edgar/data/913357/000110465909042440/a09-17606_18k.htm) — SEC, 2009-07-01. FSA acquisition closing 관련 확인
- [4. Assured Guaranty annual reports](https://assuredguaranty.com/investor-information/by-company/assured-guaranty-ltd/sec-filings) — Assured Guaranty, 2010-12-31. insured portfolio·loss reserves·capital 자료
- [5. Assured Guaranty financial information](https://assuredguaranty.com/investor-information) — Assured Guaranty, 2024-01-31. adjusted book·capital return 장기검증
- 6. Assured Guaranty historical prices — Macrotrends / market history, 2024-01-31. 역사적 가격경로 교차검증

---

# 배치 공통 학습

1. **보험주의 P/B는 liability quality를 모르고는 의미가 없다.**
2. **HoldCo cash와 regulated subsidiary capital을 합산하지 않는다.**
3. **Long-tail reserve는 평균치가 아니라 assumption distribution으로 본다.**
4. **Asset floor는 매각가능성·세금·capital requirement·debt waterfall을 차감한다.**
5. **Merger spread는 spread 크기보다 conditional probability와 duration이 핵심이다.**
6. **같은 회사의 equity와 bond는 서로 다른 thesis일 수 있다.**
7. **가격 성공과 촉매 성공을 분리한다.**
