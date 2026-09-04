# Batch 025 — Interactive Brokers·Discover Financial 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Interactive Brokers 7건 · Discover Financial Services 3건

## 결론부터

이번 배치는 금융주에서 **P/E가 아니라 balance-sheet plumbing을 보는 법**을 다룬다.

- **IBKR:** 2008~18 Long은 automation·low-cost producer·계좌성장이라는 같은 본질을 반복해서 포착했다. 흥미로운 점은 market making은 결국 2017년 철수했는데 오히려 brokerage thesis는 더 강해졌다는 것이다. 2018·2022 글은 고객현금과 margin balances에 금리를 곱해 NII를 추정했고 2023 NII $2.79bn(+68%)로 강하게 확인됐다.
- **Discover:** 2007 spin Long은 franchise는 맞았지만 GFC credit/funding downside를 놓쳐 1년 -43.5%를 맞았다. 2012 Long은 legacy CD의 3.30% funding cost가 ~1.33% marginal funding으로 재가격되는 schedule을 잡아 1년 +62.7%, 5년 +221.7%로 성공했다. 2020 Long은 COVID reserves가 실제손실보다 과도하다는 probability call로 1년 주가가 두 배가 됐다.

> 방향 교정: DFS 2020은 원 SQL `is_short=true`지만 본문은 명백한 Long이다. 나머지 9건은 raw direction과 실제 Long이 일치한다.

---

# INTERACTIVE BROKERS GROUP INC (IBKR) — 기업과 비즈니스

## 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

## 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

## 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2008-11-18 | Long | Long | 8x earnings·automation moat crisis Long | 금융위기 이후 IBKR는 생존했고 brokerage 계좌·client equity가 장기적으로 크게 성장했다. Market-making은 후일 철수했지만 주식은 장기 compounder가 됐다. | 장기 매우 성공·사업 mix는 변형 |
| 2012-12-03 | Long | Long | 1.1x TBV·11x earnings·brokerage hidden by market maker Long | 시장조성 이익의 변동성 때문에 가려졌던 brokerage가 장기 핵심이 됐고 주가는 이후 여러 배 상승. | 전설적 성공 |
| 2014-09-02 | Long | Long | Implied brokerage 10~12x·$48/$60 Long | 이후 수년 내 $48 이상에 도달하고 장기적으로 크게 상승. Strategic buyer는 필요하지 않았다. | 매우 성공 |
| 2016-01-11 | Long | Long | GEICO-like automated brokerage quality Long | 2016 이후 client accounts와 earnings가 구조적으로 성장해 장기 성공. | 장기 매우 성공 |
| 2017-09-09 | Long | Long | 17% account CAGR·$57 intrinsic value Long | $57 intrinsic value는 이후 달성했고 장기적으로 더 상승. | 매우 성공 |
| 2018-10-13 | Long | Long | 5x cheaper all-in·60%+ margin·NIM optionality Long | 2020 zero-rate 구간 변동성은 있었지만 2022~24 금리상승으로 NII가 폭증해 장기 thesis 강하게 성공. | 장기 매우 성공 |
| 2022-03-16 | Long | Long | 2021 $1.64bn income·zero debt·rate-hike Long | 2022-03 약 $65.91 → 2024-01 raw 약 $88.75, 약 +35%. Earnings catalyst는 더 강하게 적중. | 매우 성공 |

---

<!-- idea:ef1eaa5d-f0f6-4aef-bc8b-0a734a611e11 -->
## 1. 2008-11-18 — 8x earnings·automation moat crisis Long

### 결론부터

**종합판정: 장기 매우 성공·사업 mix는 변형.** 기업의 durable edge를 '특정 사업라인'보다 automation/risk engine이라는 capability로 본 점이 강했다. 그래서 market making이 사라져도 더 중요한 brokerage moat가 남았다.

**주가·증권 결과:** 금융위기 이후 IBKR는 생존했고 brokerage 계좌·client equity가 장기적으로 크게 성장했다. Market-making은 후일 철수했지만 주식은 장기 compounder가 됐다.

**Thesis / Process 점수:** 9 / 8.2

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

### 5. 밸류에이션과 기대수익의 연결

당시 약 8x EPS 수준의 crisis valuation. Market making과 electronic brokerage를 합한 현재 earnings에 low-cost technology moat를 적용하면 정상화 valuation이 훨씬 높다고 봤다. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Automation moat — 강한 적중 · 논지 비중 18%

**당시 주장**

자동화가 구조적 cost advantage를 만든다.

**당시 근거**

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

**이 주장이 성립하려면**

technology scale 유지

**사전 반증조건**

service cost가 경쟁사 수준으로 상승

**실제 결과**

장기 brokerage margin으로 확인.

**정량적 괴리**

Valuation / ~8x EPS / normalization / 장기 rerating

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Automation moat 가설은 'service cost가 경쟁사 수준으로 상승'를 반증조건으로 저장한다.

#### 2. Risk management — 적중 · 논지 비중 18%

**당시 주장**

실시간 risk system이 crisis survivability를 높인다.

**당시 근거**

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

**이 주장이 성립하려면**

counterparty/market losses 통제

**사전 반증조건**

대형 trading loss

**실제 결과**

2008 이후 생존·성장.

**정량적 괴리**

Business mix / market making+brokerage / 둘 다 가치 / market making 2017 철수

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Risk management 가설은 '대형 trading loss'를 반증조건으로 저장한다.

#### 3. Market making — 실패 · 논지 비중 16%

**당시 주장**

market making이 장기 핵심 earnings engine이다.

**당시 근거**

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

**이 주장이 성립하려면**

competitive spreads 유지

**사전 반증조건**

HFT 경쟁으로 economics 훼손

**실제 결과**

2017 사실상 철수.

**정량적 괴리**

2023 NII / 미성숙 / brokerage economics 확대 / $2.79bn

**분석 오류·핵심**

현재 earnings를 funding·credit·segment transition 없이 선형적으로 자본화했다.

**재사용할 교훈**

Market making 가설은 'HFT 경쟁으로 economics 훼손'를 반증조건으로 저장한다.

#### 4. Brokerage growth — 강한 적중 · 논지 비중 16%

**당시 주장**

electronic brokerage가 share를 늘린다.

**당시 근거**

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

**이 주장이 성립하려면**

low pricing attracts clients

**사전 반증조건**

price war removes economics

**실제 결과**

장기 핵심 franchise로 성장.

**정량적 괴리**

2023 pretax / 초기 소규모 / scale / $3.07bn

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Brokerage growth 가설은 'price war removes economics'를 반증조건으로 저장한다.

#### 5. Peterffy alignment — 적중 · 논지 비중 16%

**당시 주장**

founder ownership이 장기 capital discipline을 준다.

**당시 근거**

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

**이 주장이 성립하려면**

governance aligned

**사전 반증조건**

related-party/value leakage

**실제 결과**

장기 platform investment 지속.

**정량적 괴리**

금융위기 이후 IBKR는 생존했고 brokerage 계좌·client equity가 장기적으로 크게 성장했다. Market-making은 후일 철수했지만 주식은 장기 compounder가 됐다.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Peterffy alignment 가설은 'related-party/value leakage'를 반증조건으로 저장한다.

#### 6. 8x mispricing — 적중 · 논지 비중 16%

**당시 주장**

crisis P/E가 franchise quality를 과소평가한다.

**당시 근거**

IBKR는 기술·자동화·risk management 때문에 사람이 많은 전통 broker보다 훨씬 낮은 비용으로 거래를 처리하고, 2008 crisis volatility에서도 오히려 market-making/brokerage opportunity가 커질 수 있다고 봤다. Peterffy가 약 80% 경제적 지분을 보유하고 public float가 작다는 alignment도 강조했다.

**이 주장이 성립하려면**

earnings survive

**사전 반증조건**

financial failure

**실제 결과**

장기 강한 rerating.

**정량적 괴리**

금융위기 이후 IBKR는 생존했고 brokerage 계좌·client equity가 장기적으로 크게 성장했다. Market-making은 후일 철수했지만 주식은 장기 compounder가 됐다.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

8x mispricing 가설은 'financial failure'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

IBKR는 위기를 통과하고 brokerage business를 크게 확장했다. 다만 2017년 옵션 market-making을 철수해 '두 사업 모두 장기 성장'이라는 형태는 틀렸고, 오히려 brokerage가 핵심 franchise로 집중됐다. 2023 pretax income $3.07bn, NII $2.79bn, commissions $1.36bn으로 recurring brokerage economics가 훨씬 커졌다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 금융위기 이후 IBKR는 생존했고 brokerage 계좌·client equity가 장기적으로 크게 성장했다. Market-making은 후일 철수했지만 주식은 장기 compounder가 됐다. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

기업의 durable edge를 '특정 사업라인'보다 automation/risk engine이라는 capability로 본 점이 강했다. 그래서 market making이 사라져도 더 중요한 brokerage moat가 남았다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-12-31 — brokerage가 전체 earnings의 절반 이상으로 성장하고 accounts/client equity가 증가하면서 crisis-survivor 이상의 platform thesis가 확인됐다. 회피 가능성: 해당 없음. 다만 market-making 경쟁력 약화는 2017년에 별도 claim으로 종료했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

장기 매우 성공·사업 mix는 변형. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Valuation | ~8x EPS | normalization | 장기 rerating | 적중 |
| Business mix | market making+brokerage | 둘 다 가치 | market making 2017 철수 | 부분 |
| 2023 NII | 미성숙 | brokerage economics 확대 | $2.79bn | 강한 적중 |
| 2023 pretax | 초기 소규모 | scale | $3.07bn | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2008-11-18 | VIC 아이디어 게시 | 8x earnings·automation moat crisis Long |
| 2012-12-31 | 최초 핵심 검증·반증 신호 | brokerage가 전체 earnings의 절반 이상으로 성장하고 accounts/client equity가 증가하면서 crisis-survivor 이상의 platform thesis가 확인됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | 금융위기 이후 IBKR는 생존했고 brokerage 계좌·client equity가 장기적으로 크게 성장했다. Market-making은 후일 철수했지만 주식은 장기 compounder가 됐다. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2012-12-31 — brokerage가 전체 earnings의 절반 이상으로 성장하고 accounts/client equity가 증가하면서 crisis-survivor 이상의 platform thesis가 확인됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음. 다만 market-making 경쟁력 약화는 2017년에 별도 claim으로 종료했어야 한다.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IBKR 2008-11-18 원문](https://www.valueinvestorsclub.com/idea/Interactive_Brokers/6192906655) — Value Investors Club / user SQL, 2008-11-18. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---

<!-- idea:8b3dfadd-9e87-4046-b3ac-6747004feeb7 -->
## 2. 2012-12-03 — 1.1x TBV·11x earnings·brokerage hidden by market maker Long

### 결론부터

**종합판정: 전설적 성공.** 좋은 포인트는 흔들리는 segment가 consolidated numbers를 왜곡할 때 더 좋은 segment를 분리해 valuation한 것이다. TBV는 단순 하방지표였고 실제 upside는 brokerage franchise에서 나왔다.

**주가·증권 결과:** 시장조성 이익의 변동성 때문에 가려졌던 brokerage가 장기 핵심이 됐고 주가는 이후 여러 배 상승.

**Thesis / Process 점수:** 9.6 / 9.3

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

$14.98, 약 1.1x tangible book, 11x earnings, 2.7% dividend. Brokerage가 earnings의 50% 이상을 만들지만 market-making volatility가 consolidated multiple을 눌렀다고 판단. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Hidden brokerage — 강한 적중 · 논지 비중 18%

**당시 주장**

market-making noise가 좋은 brokerage를 가린다.

**당시 근거**

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

**이 주장이 성립하려면**

brokerage margins/growth 지속

**사전 반증조건**

client assets 정체

**실제 결과**

후일 회사 핵심으로 드러남.

**정량적 괴리**

주가 / $14.98 / rerating / 장기 multi-bagger

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Hidden brokerage 가설은 'client assets 정체'를 반증조건으로 저장한다.

#### 2. TBV floor — 적중 · 논지 비중 18%

**당시 주장**

1.1x TBV가 downside를 제한한다.

**당시 근거**

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

**이 주장이 성립하려면**

capital quality

**사전 반증조건**

trading losses

**실제 결과**

balance sheet 안정.

**정량적 괴리**

P/TBV / 1.1x / floor / book보다 franchise 가치 중요

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

TBV floor 가설은 'trading losses'를 반증조건으로 저장한다.

#### 3. Account growth — 적중 · 논지 비중 16%

**당시 주장**

계좌·client equity가 구조적으로 증가한다.

**당시 근거**

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

**이 주장이 성립하려면**

price/service advantage

**사전 반증조건**

customer churn

**실제 결과**

장기 고성장.

**정량적 괴리**

P/E / 11x / quality rerating / 장기 상승

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Account growth 가설은 'customer churn'를 반증조건으로 저장한다.

#### 4. Excess capital — 적중 · 논지 비중 16%

**당시 주장**

필요자본 이상이 optionality다.

**당시 근거**

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

**이 주장이 성립하려면**

regulatory capital 여유

**사전 반증조건**

capital trapped

**실제 결과**

growth funding에 충분.

**정량적 괴리**

Brokerage share / >50% earnings / 핵심화 / market making exit 후 거의 전부

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Excess capital 가설은 'capital trapped'를 반증조건으로 저장한다.

#### 5. Market-maker drag — 강한 적중 · 논지 비중 16%

**당시 주장**

낮은-quality segment가 multiple을 누른다.

**당시 근거**

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

**이 주장이 성립하려면**

segment contraction

**사전 반증조건**

drag worsens

**실제 결과**

2017 철수.

**정량적 괴리**

시장조성 이익의 변동성 때문에 가려졌던 brokerage가 장기 핵심이 됐고 주가는 이후 여러 배 상승.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Market-maker drag 가설은 'drag worsens'를 반증조건으로 저장한다.

#### 6. 11x earnings — 강한 적중 · 논지 비중 16%

**당시 주장**

brokerage quality 대비 11x가 낮다.

**당시 근거**

시장조성 사업은 불안정하지만 brokerage는 고객자산·계좌가 성장하는 high-quality franchise이고 excess capital도 크다고 봤다. TBV 부근에서 brokerage growth를 사는 구조라 downside가 낮다고 주장했다.

**이 주장이 성립하려면**

earnings durable

**사전 반증조건**

brokerage commoditizes

**실제 결과**

장기 rerating.

**정량적 괴리**

시장조성 이익의 변동성 때문에 가려졌던 brokerage가 장기 핵심이 됐고 주가는 이후 여러 배 상승.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

11x earnings 가설은 'brokerage commoditizes'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2017 market making 철수로 원문의 '가려진 brokerage'가 회사 전체가 됐다. 이후 zero commissions 경쟁 속에서도 low margin rates/global access로 client assets가 늘었다. 2023에는 NII와 commissions가 대부분 earnings를 만들었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 시장조성 이익의 변동성 때문에 가려졌던 brokerage가 장기 핵심이 됐고 주가는 이후 여러 배 상승. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

좋은 포인트는 흔들리는 segment가 consolidated numbers를 왜곡할 때 더 좋은 segment를 분리해 valuation한 것이다. TBV는 단순 하방지표였고 실제 upside는 brokerage franchise에서 나왔다.

### 9. 최초 검증·반증 신호와 회피 가능성

2017-03-08 — 회사가 options market-making 철수를 발표하면서 brokerage hidden-value thesis가 기업구조 변화로 직접 확인됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $14.98 | rerating | 장기 multi-bagger | 강한 적중 |
| P/TBV | 1.1x | floor | book보다 franchise 가치 중요 | 적중 |
| P/E | 11x | quality rerating | 장기 상승 | 적중 |
| Brokerage share | >50% earnings | 핵심화 | market making exit 후 거의 전부 | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2012-12-03 | VIC 아이디어 게시 | 1.1x TBV·11x earnings·brokerage hidden by market maker Long |
| 2017-03-08 | 최초 핵심 검증·반증 신호 | 회사가 options market-making 철수를 발표하면서 brokerage hidden-value thesis가 기업구조 변화로 직접 확인됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | 시장조성 이익의 변동성 때문에 가려졌던 brokerage가 장기 핵심이 됐고 주가는 이후 여러 배 상승. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2017-03-08 — 회사가 options market-making 철수를 발표하면서 brokerage hidden-value thesis가 기업구조 변화로 직접 확인됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IBKR 2012-12-03 원문](https://www.valueinvestorsclub.com/idea/INTERACTIVE_BROKERS_GROUP/3617274595) — Value Investors Club / user SQL, 2012-12-03. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---

<!-- idea:0baa5883-7c34-4350-9910-a1415f2b167a -->
## 3. 2014-09-02 — Implied brokerage 10~12x·$48/$60 Long

### 결론부터

**종합판정: 매우 성공.** SOTP와 segment-quality 분석이 맞았다. 다만 strategic sale을 upside로 넣을 필요 없이 organic compounding만으로 thesis가 성립했다는 점이 오히려 강점이다.

**주가·증권 결과:** 이후 수년 내 $48 이상에 도달하고 장기적으로 크게 상승. Strategic buyer는 필요하지 않았다.

**Thesis / Process 점수:** 9 / 8.2

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

### 5. 밸류에이션과 기대수익의 연결

Market maker와 excess capital을 분리하면 brokerage implied P/E가 10~12x. Standalone value 약 $48, 2016 mid-$50s, strategic buyer라면 $60+ 가능하다고 계산. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Low-cost producer — 적중 · 논지 비중 18%

**당시 주장**

자동화가 commission·margin pricing 우위를 만든다.

**당시 근거**

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

**이 주장이 성립하려면**

cost lead 유지

**사전 반증조건**

competitors match cost

**실제 결과**

우위 지속.

**정량적 괴리**

Broker P/E / 10~12x implied / rerating / pure broker로 재평가

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Low-cost producer 가설은 'competitors match cost'를 반증조건으로 저장한다.

#### 2. Global platform — 적중 · 논지 비중 18%

**당시 주장**

다시장/다자산 접근성이 switching value를 높인다.

**당시 근거**

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

**이 주장이 성립하려면**

regulatory connectivity

**사전 반증조건**

local brokers replicate

**실제 결과**

차별화 유지.

**정량적 괴리**

Target / $48 / 달성 / 수년 내 상회

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Global platform 가설은 'local brokers replicate'를 반증조건으로 저장한다.

#### 3. Brokerage multiple — 강한 적중 · 논지 비중 16%

**당시 주장**

10~12x는 quality 대비 너무 낮다.

**당시 근거**

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

**이 주장이 성립하려면**

growth/margins

**사전 반증조건**

growth stalls

**실제 결과**

rerating.

**정량적 괴리**

Strategic / $60+ / buyer option / 독립기업으로 달성

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Brokerage multiple 가설은 'growth stalls'를 반증조건으로 저장한다.

#### 4. Market maker value — 적중 · 논지 비중 16%

**당시 주장**

market maker를 별도 낮은 multiple로 봐도 투자성립.

**당시 근거**

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

**이 주장이 성립하려면**

losses 제한

**사전 반증조건**

large losses

**실제 결과**

후일 철수해 논지 단순화.

**정량적 괴리**

Margins / 업계 최고권 / scale leverage / 2023 pretax margin 매우 높음

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Market maker value 가설은 'large losses'를 반증조건으로 저장한다.

#### 5. Strategic option — 비필수 · 논지 비중 16%

**당시 주장**

buyer라면 $60+ 가치가 있다.

**당시 근거**

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

**이 주장이 성립하려면**

acquirer synergies

**사전 반증조건**

no buyer

**실제 결과**

buyer 없이 value 달성.

**정량적 괴리**

이후 수년 내 $48 이상에 도달하고 장기적으로 크게 상승. Strategic buyer는 필요하지 않았다.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Strategic option 가설은 'no buyer'를 반증조건으로 저장한다.

#### 6. $48 value — 강한 적중 · 논지 비중 16%

**당시 주장**

standalone compounding으로 큰 upside다.

**당시 근거**

IBKR brokerage는 세계적으로 가장 낮은 commission/margin rates와 높은 automation으로 경쟁사보다 높은 profitability를 내는데, market maker 때문에 낮은 multiple을 받는다고 봤다. Scale과 global multi-asset access가 진입장벽.

**이 주장이 성립하려면**

account growth

**사전 반증조건**

price war

**실제 결과**

달성.

**정량적 괴리**

이후 수년 내 $48 이상에 도달하고 장기적으로 크게 상승. Strategic buyer는 필요하지 않았다.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

$48 value 가설은 'price war'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Brokerage는 성장했고 2017 market-making exit 뒤 pure brokerage economics가 더 선명해졌다. $48/$60 수준은 후일 달성됐고 buyer 없이 독립 compounder로 가치가 커졌다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 이후 수년 내 $48 이상에 도달하고 장기적으로 크게 상승. Strategic buyer는 필요하지 않았다. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

SOTP와 segment-quality 분석이 맞았다. 다만 strategic sale을 upside로 넣을 필요 없이 organic compounding만으로 thesis가 성립했다는 점이 오히려 강점이다.

### 9. 최초 검증·반증 신호와 회피 가능성

2017-03-08 — market-making exit 발표로 sum-of-parts discount의 핵심 원인이 제거됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Broker P/E | 10~12x implied | rerating | pure broker로 재평가 | 적중 |
| Target | $48 | 달성 | 수년 내 상회 | 적중 |
| Strategic | $60+ | buyer option | 독립기업으로 달성 | option 불필요 |
| Margins | 업계 최고권 | scale leverage | 2023 pretax margin 매우 높음 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2014-09-02 | VIC 아이디어 게시 | Implied brokerage 10~12x·$48/$60 Long |
| 2017-03-08 | 최초 핵심 검증·반증 신호 | market-making exit 발표로 sum-of-parts discount의 핵심 원인이 제거됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | 이후 수년 내 $48 이상에 도달하고 장기적으로 크게 상승. Strategic buyer는 필요하지 않았다. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2017-03-08 — market-making exit 발표로 sum-of-parts discount의 핵심 원인이 제거됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- 1. VIC IBKR 2014-09-02 원문 — Value Investors Club / user SQL, 2014-09-02. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---

<!-- idea:12404fc3-7ee8-41de-96dc-47f20ba38571 -->
## 4. 2016-01-11 — GEICO-like automated brokerage quality Long

### 결론부터

**종합판정: 장기 매우 성공.** 제품가격이 싸다는 사실이 아니라 '왜 경쟁사보다 싸게 팔면서 더 높은 margin을 낼 수 있는가'를 cost architecture로 설명했다는 점이 좋다.

**주가·증권 결과:** 2016 이후 client accounts와 earnings가 구조적으로 성장해 장기 성공.

**Thesis / Process 점수:** 9 / 8.2

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

### 5. 밸류에이션과 기대수익의 연결

약 20% 주가 pullback을 business deterioration보다 valuation opportunity로 해석. GEICO처럼 structural low-cost producer에 장기 compounding multiple을 부여. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. GEICO analogy — 적중 · 논지 비중 18%

**당시 주장**

구조적 cost lead가 share gain을 만든다.

**당시 근거**

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

**이 주장이 성립하려면**

cost gap persists

**사전 반증조건**

competitor automation catches up

**실제 결과**

IBKR pricing 우위 지속.

**정량적 괴리**

Pullback / ~20% / entry opportunity / 장기 회복/상승

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

GEICO analogy 가설은 'competitor automation catches up'를 반증조건으로 저장한다.

#### 2. Automation scale — 적중 · 논지 비중 18%

**당시 주장**

volume growth가 unit cost를 낮춘다.

**당시 근거**

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

**이 주장이 성립하려면**

fixed tech platform

**사전 반증조건**

service headcount scales linearly

**실제 결과**

높은 operating leverage.

**정량적 괴리**

Cost model / automation / scale leverage / 높은 pretax profitability

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Automation scale 가설은 'service headcount scales linearly'를 반증조건으로 저장한다.

#### 3. Price as marketing — 적중 · 논지 비중 16%

**당시 주장**

낮은 fees/margin rates가 organic acquisition을 만든다.

**당시 근거**

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

**이 주장이 성립하려면**

customers price sensitive

**사전 반증조건**

brand/service dominates

**실제 결과**

계좌 성장.

**정량적 괴리**

Commission / 낮음 / customer acquisition / 업계 zero-commission화

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Price as marketing 가설은 'brand/service dominates'를 반증조건으로 저장한다.

#### 4. Competitive response — 적중 · 논지 비중 16%

**당시 주장**

zero commissions가 moat를 파괴하지 않는다.

**당시 근거**

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

**이 주장이 성립하려면**

other economics differentiate

**사전 반증조건**

all-in cost equalizes

**실제 결과**

margin rates/global access로 차별화.

**정량적 괴리**

NII / 낮은 금리로 제한 / future option / 2023 $2.79bn

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Competitive response 가설은 'all-in cost equalizes'를 반증조건으로 저장한다.

#### 5. Rate option — 적중 · 논지 비중 16%

**당시 주장**

금리상승 시 customer cash가 earnings option이다.

**당시 근거**

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

**이 주장이 성립하려면**

balances stable

**사전 반증조건**

cash outflows

**실제 결과**

후일 매우 큰 NII.

**정량적 괴리**

2016 이후 client accounts와 earnings가 구조적으로 성장해 장기 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Rate option 가설은 'cash outflows'를 반증조건으로 저장한다.

#### 6. Quality compounder — 적중 · 논지 비중 16%

**당시 주장**

20% pullback은 long-duration entry다.

**당시 근거**

보험에서 GEICO가 direct model로 cost curve를 낮췄듯 IBKR도 automation으로 broker cost curve를 낮춘다고 봤다. 낮은 가격 자체가 고객획득수단이며 더 많은 volume이 scale advantage를 강화하는 positive feedback을 강조했다.

**이 주장이 성립하려면**

moat intact

**사전 반증조건**

technology failure

**실제 결과**

장기 성공.

**정량적 괴리**

2016 이후 client accounts와 earnings가 구조적으로 성장해 장기 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Quality compounder 가설은 'technology failure'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Zero-commission era가 와도 IBKR는 commission 자체보다 margin rates, international access와 interest economics로 차별화했다. Market making exit 후 brokerage focus가 강해졌고 2023 NII가 급증했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2016 이후 client accounts와 earnings가 구조적으로 성장해 장기 성공. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

제품가격이 싸다는 사실이 아니라 '왜 경쟁사보다 싸게 팔면서 더 높은 margin을 낼 수 있는가'를 cost architecture로 설명했다는 점이 좋다.

### 9. 최초 검증·반증 신호와 회피 가능성

2017-12-31 — market-making 철수 뒤에도 brokerage revenue/accounts가 성장해 low-cost automation thesis가 독립적으로 확인됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

장기 매우 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Pullback | ~20% | entry opportunity | 장기 회복/상승 | 적중 |
| Cost model | automation | scale leverage | 높은 pretax profitability | 적중 |
| Commission | 낮음 | customer acquisition | 업계 zero-commission화 | 차별화 축 이동 |
| NII | 낮은 금리로 제한 | future option | 2023 $2.79bn | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-01-11 | VIC 아이디어 게시 | GEICO-like automated brokerage quality Long |
| 2017-12-31 | 최초 핵심 검증·반증 신호 | market-making 철수 뒤에도 brokerage revenue/accounts가 성장해 low-cost automation thesis가 독립적으로 확인됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | 2016 이후 client accounts와 earnings가 구조적으로 성장해 장기 성공. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2017-12-31 — market-making 철수 뒤에도 brokerage revenue/accounts가 성장해 low-cost automation thesis가 독립적으로 확인됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- 1. VIC IBKR 2016-01-11 원문 — Value Investors Club / user SQL, 2016-01-11. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---

<!-- idea:8d62d278-d3db-45fa-b25a-16b08e3febac -->
## 5. 2017-09-09 — 17% account CAGR·$57 intrinsic value Long

### 결론부터

**종합판정: 매우 성공.** 장기 KPI를 account CAGR로 잡고 이를 revenue/margin로 연결한 점이 좋았다. 단기 trading volume보다 client relationship growth를 봤다.

**주가·증권 결과:** $57 intrinsic value는 이후 달성했고 장기적으로 더 상승.

**Thesis / Process 점수:** 9 / 8.2

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

### 5. 밸류에이션과 기대수익의 연결

Intrinsic value $57, 당시 가격 대비 약 28% upside. 2007 이후 accounts CAGR 약 17%, low-cost producer와 operating leverage를 반영. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Account CAGR — 적중 · 논지 비중 18%

**당시 주장**

17% account growth가 지속가능하다.

**당시 근거**

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

**이 주장이 성립하려면**

cost/market reach

**사전 반증조건**

acquisition slows

**실제 결과**

장기 계좌성장.

**정량적 괴리**

Accounts CAGR / ~17% since 2007 / 지속 / 장기 double-digit 성장

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Account CAGR 가설은 'acquisition slows'를 반증조건으로 저장한다.

#### 2. Client equity — 적중 · 논지 비중 18%

**당시 주장**

고객자산이 계좌와 함께 성장한다.

**당시 근거**

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

**이 주장이 성립하려면**

retention

**사전 반증조건**

large outflows

**실제 결과**

장기 확대.

**정량적 괴리**

Intrinsic / $57 / +28% / 후일 상회

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Client equity 가설은 'large outflows'를 반증조건으로 저장한다.

#### 3. Low-cost moat — 적중 · 논지 비중 16%

**당시 주장**

가격우위가 organic growth를 만든다.

**당시 근거**

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

**이 주장이 성립하려면**

automation

**사전 반증조건**

competitor parity

**실제 결과**

지속.

**정량적 괴리**

Business mix / market maker 축소 / broker focus / 2017 exit

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Low-cost moat 가설은 'competitor parity'를 반증조건으로 저장한다.

#### 4. Operating leverage — 적중 · 논지 비중 16%

**당시 주장**

incremental accounts가 high margin이다.

**당시 근거**

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

**이 주장이 성립하려면**

fixed platform

**사전 반증조건**

service costs rise

**실제 결과**

높은 profitability.

**정량적 괴리**

Margins / operating leverage / 확대 / 2023 pretax $3.07bn

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Operating leverage 가설은 'service costs rise'를 반증조건으로 저장한다.

#### 5. Founder alignment — 적중 · 논지 비중 16%

**당시 주장**

Peterffy ownership이 장기투자를 지지한다.

**당시 근거**

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

**이 주장이 성립하려면**

capital discipline

**사전 반증조건**

governance discount

**실제 결과**

platform investment 지속.

**정량적 괴리**

$57 intrinsic value는 이후 달성했고 장기적으로 더 상승.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Founder alignment 가설은 'governance discount'를 반증조건으로 저장한다.

#### 6. $57 value — 적중 · 논지 비중 16%

**당시 주장**

business growth가 28% upside를 만든다.

**당시 근거**

IBKR는 고객계좌·client equity가 장기간 double-digit 성장하고, 자동화 때문에 낮은 commission에도 operating leverage가 큰데 market making 과거가 valuation을 누른다고 봤다. Peterffy의 owner orientation도 강조.

**이 주장이 성립하려면**

growth/multiple

**사전 반증조건**

market downturn

**실제 결과**

달성.

**정량적 괴리**

$57 intrinsic value는 이후 달성했고 장기적으로 더 상승.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

$57 value 가설은 'market downturn'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2017 market-making exit가 거의 완료돼 business가 brokerage에 집중됐다. 이후 accounts/client equity 성장과 금리상승이 함께 earnings를 키웠다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 $57 intrinsic value는 이후 달성했고 장기적으로 더 상승. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

장기 KPI를 account CAGR로 잡고 이를 revenue/margin로 연결한 점이 좋았다. 단기 trading volume보다 client relationship growth를 봤다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-12-31 — market-making exit 후에도 계좌·client equity가 계속 늘어 brokerage-only thesis가 검증됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Accounts CAGR | ~17% since 2007 | 지속 | 장기 double-digit 성장 | 적중 |
| Intrinsic | $57 | +28% | 후일 상회 | 적중 |
| Business mix | market maker 축소 | broker focus | 2017 exit | 강한 적중 |
| Margins | operating leverage | 확대 | 2023 pretax $3.07bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-09-09 | VIC 아이디어 게시 | 17% account CAGR·$57 intrinsic value Long |
| 2018-12-31 | 최초 핵심 검증·반증 신호 | market-making exit 후에도 계좌·client equity가 계속 늘어 brokerage-only thesis가 검증됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | $57 intrinsic value는 이후 달성했고 장기적으로 더 상승. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2018-12-31 — market-making exit 후에도 계좌·client equity가 계속 늘어 brokerage-only thesis가 검증됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IBKR 2017-09-09 원문](https://www.valueinvestorsclub.com/idea/INTERACTIVE_BROKERS_GROUP/4525170392) — Value Investors Club / user SQL, 2017-09-09. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---

<!-- idea:5534e963-4cf0-49d3-aec3-a3555a49d1b4 -->
## 6. 2018-10-13 — 5x cheaper all-in·60%+ margin·NIM optionality Long

### 결론부터

**종합판정: 장기 매우 성공.** 수익식을 customer equity × cash/margin balances × spread로 분해해 금리상승을 단순 macro bet가 아니라 platform scale과 결합했다는 점이 강했다.

**주가·증권 결과:** 2020 zero-rate 구간 변동성은 있었지만 2022~24 금리상승으로 NII가 폭증해 장기 thesis 강하게 성공.

**Thesis / Process 점수:** 9 / 8.2

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

### 5. 밸류에이션과 기대수익의 연결

Brokerage를 고성장·60%+ operating margin platform으로 보고, 당시 profit의 약 70%가 NIM에서 나오며 client equity와 금리가 normalizing될 때 earnings power가 더 커질 수 있다고 평가. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. 5x cost edge — 적중 · 논지 비중 18%

**당시 주장**

all-in cost가 경쟁사보다 크게 낮다.

**당시 근거**

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

**이 주장이 성립하려면**

automation advantage

**사전 반증조건**

competitor matching

**실제 결과**

차별화 지속.

**정량적 괴리**

All-in cost / ~5x cheaper / share gain / low-cost positioning 유지

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

5x cost edge 가설은 'competitor matching'를 반증조건으로 저장한다.

#### 2. 60%+ margin — 적중 · 논지 비중 18%

**당시 주장**

low cost가 높은 brokerage margin을 만든다.

**당시 근거**

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

**이 주장이 성립하려면**

scale

**사전 반증조건**

pricing pressure

**실제 결과**

높은 margin 유지.

**정량적 괴리**

Operating margin / 60%+ / scale / 높은 pretax margin

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

60%+ margin 가설은 'pricing pressure'를 반증조건으로 저장한다.

#### 3. Hidden growth — 적중 · 논지 비중 16%

**당시 주장**

market-maker decline이 brokerage growth를 가린다.

**당시 근거**

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

**이 주장이 성립하려면**

brokerage standalone growth

**사전 반증조건**

client growth stalls

**실제 결과**

exit 후 명확해짐.

**정량적 괴리**

2023 NII / rate option / 대폭 증가 / $2.79bn +68%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Hidden growth 가설은 'client growth stalls'를 반증조건으로 저장한다.

#### 4. NIM engine — 강한 적중 · 논지 비중 16%

**당시 주장**

client cash/margin × rates가 큰 profit driver다.

**당시 근거**

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

**이 주장이 성립하려면**

balances sticky

**사전 반증조건**

cash sweep outflows

**실제 결과**

2023 NII 폭증.

**정량적 괴리**

2023 NIM / 낮은 과거 base / normalize / 2.36%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

NIM engine 가설은 'cash sweep outflows'를 반증조건으로 저장한다.

#### 5. Rate sensitivity — 강한 적중 · 논지 비중 16%

**당시 주장**

금리정상화가 earnings를 비선형적으로 높인다.

**당시 근거**

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

**이 주장이 성립하려면**

Fed rates rise

**사전 반증조건**

rates stay zero

**실제 결과**

2022~23 현실화.

**정량적 괴리**

2020 zero-rate 구간 변동성은 있었지만 2022~24 금리상승으로 NII가 폭증해 장기 thesis 강하게 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Rate sensitivity 가설은 'rates stay zero'를 반증조건으로 저장한다.

#### 6. Long-term value — 적중 · 논지 비중 16%

**당시 주장**

brokerage+NIM이 per-share earnings를 compound한다.

**당시 근거**

IBKR all-in transaction cost가 경쟁사보다 약 5배 저렴하고, automation으로 60%+ margin이 가능하다고 봤다. Market-maker decline이 headline growth를 가렸지만 brokerage만 보면 고성장이며, 고객현금/마진대출과 금리의 곱이 추가 earnings engine.

**이 주장이 성립하려면**

accounts growth

**사전 반증조건**

regulatory cap

**실제 결과**

장기 성공.

**정량적 괴리**

2020 zero-rate 구간 변동성은 있었지만 2022~24 금리상승으로 NII가 폭증해 장기 thesis 강하게 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Long-term value 가설은 'regulatory cap'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2020~21 저금리에는 NIM option이 잠시 숨었지만 2023 NII가 $2.79bn으로 68% 증가하고 NIM 2.36%로 상승했다. Commissions도 $1.36bn으로 증가해 rate-only story가 아니었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2020 zero-rate 구간 변동성은 있었지만 2022~24 금리상승으로 NII가 폭증해 장기 thesis 강하게 성공. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

수익식을 customer equity × cash/margin balances × spread로 분해해 금리상승을 단순 macro bet가 아니라 platform scale과 결합했다는 점이 강했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-06-30 — Fed hiking과 함께 net interest income가 빠르게 증가하기 시작해 long-dormant rate optionality가 현실화됐다. 회피 가능성: 해당 없음. zero-rate 시기에는 NII sensitivity를 normalized basis로 유지해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

장기 매우 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| All-in cost | ~5x cheaper | share gain | low-cost positioning 유지 | 적중 |
| Operating margin | 60%+ | scale | 높은 pretax margin | 적중 |
| 2023 NII | rate option | 대폭 증가 | $2.79bn +68% | 강한 적중 |
| 2023 NIM | 낮은 과거 base | normalize | 2.36% | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-10-13 | VIC 아이디어 게시 | 5x cheaper all-in·60%+ margin·NIM optionality Long |
| 2022-06-30 | 최초 핵심 검증·반증 신호 | Fed hiking과 함께 net interest income가 빠르게 증가하기 시작해 long-dormant rate optionality가 현실화됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | 2020 zero-rate 구간 변동성은 있었지만 2022~24 금리상승으로 NII가 폭증해 장기 thesis 강하게 성공. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2022-06-30 — Fed hiking과 함께 net interest income가 빠르게 증가하기 시작해 long-dormant rate optionality가 현실화됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음. zero-rate 시기에는 NII sensitivity를 normalized basis로 유지해야 했다.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IBKR 2018-10-13 원문](https://www.valueinvestorsclub.com/idea/INTERACTIVE_BROKERS_GROUP/4701018140) — Value Investors Club / user SQL, 2018-10-13. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---

<!-- idea:24215b1b-e546-4a37-9d19-6e3df718cc05 -->
## 7. 2022-03-16 — 2021 $1.64bn income·zero debt·rate-hike Long

### 결론부터

**종합판정: 매우 성공.** 금리상승을 단순 은행식 NIM bet가 아니라 이미 성장하는 client-assets platform에 붙은 convexity로 본 점이 좋았다. 가격성과보다 earnings mechanism이 더 명확하게 적중했다.

**주가·증권 결과:** 2022-03 약 $65.91 → 2024-01 raw 약 $88.75, 약 +35%. Earnings catalyst는 더 강하게 적중.

**Thesis / Process 점수:** 9 / 8.2

### 1. 무슨 기업인가

Interactive Brokers는 개인투자자, 전문 트레이더, 자산운용사, 헤지펀드, introducing broker와 금융자문업자에게 전 세계 주식·옵션·선물·FX·채권 등 여러 자산을 하나의 전자 플랫폼에서 거래하게 해주는 글로벌 브로커다. 핵심은 사람 중심의 고비용 영업조직이 아니라 주문 라우팅·리스크관리·결제·마진대출·FX conversion을 소프트웨어로 자동화한 구조다. 그래서 고객당 서비스 비용이 낮고 낮은 commission·margin rate를 제공하면서도 높은 operating margin을 만들 수 있다. 수익은 commissions, 고객 현금의 운용수익과 margin loans에서 발생하는 net interest income, securities lending, market-data·account fees 등에서 나온다. 역사적으로는 electronic market making과 brokerage를 함께 했으나 2017년 옵션 market-making 사업을 사실상 철수하면서 business quality가 더 선명해졌다. 2023년 net revenue는 약 $4.34bn, pretax income $3.07bn, net interest income $2.79bn(+68%), commissions $1.36bn(+3%), net interest margin 약 2.36%, diluted EPS $5.67이었다. 핵심 KPI는 customer accounts, client equity, DARTs/trading volume, commission per trade, margin loans, customer credit balances, NIM/NII, pretax margin, compensation/technology cost, capital excess와 share count다.

### 2. 산업 가치사슬과 돈의 흐름

IBKR의 돈 흐름은 두 개의 엔진으로 이해하면 된다. 첫째 brokerage에서는 고객계좌와 거래량이 늘수록 commissions와 data/other fees가 증가한다. 거래 인프라가 대부분 자동화돼 있어 신규계좌의 incremental servicing cost가 낮아 operating leverage가 크다. 둘째 balance-sheet business에서는 고객이 맡긴 현금을 안전자산에 운용하고 margin loans에 이자를 받아 net interest spread를 번다. 금리가 0에 가까울 때는 이 earning power가 가려지지만 금리가 오르면 customer cash와 margin balances가 커질수록 NII가 비선형적으로 늘 수 있다. 반대로 고객 cash에 지급하는 금리, 경쟁사 pricing, market volatility와 regulatory capital이 spread를 제한한다. 과거 market making은 trading profits를 만들었지만 기술경쟁이 심해지며 2017년 철수했고, 이익이 brokerage 중심으로 이동하면서 recurring franchise의 질이 오히려 높아졌다.

### 3. 경쟁우위·경쟁구도·핵심 지표

IBKR의 경쟁우위는 low-cost automation, 전 세계 시장·상품 접근성, low margin rates, sophisticated risk engine, high client-equity retention과 founder-controlled 장기투자 문화다. Fidelity/Schwab 같은 retail brokers는 서비스·distribution이 강하고, prime brokers는 institutional relationship이 강하지만 IBKR는 가격·상품범위·자동화에서 차별화된다. 중요한 리스크는 commission price war, zero-rate environment, regulatory/capital requirements, 시스템 장애와 customer concentration이 아니라 market-activity sensitivity다. 그러나 market making 철수 사례처럼 특정 수익원이 사라져도 brokerage platform의 unit economics가 좋아질 수 있어 segment mix를 지속적으로 재평가해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

2021 net income 약 $1.636bn vs market cap 약 $25.8bn. Strong balance sheet, low-cost automated platform와 rising-rate earnings sensitivity를 감안하면 mid-teens earnings multiple이 낮다고 판단. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Technology moat — 적중 · 논지 비중 18%

**당시 주장**

automated global broker가 durable edge다.

**당시 근거**

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

**이 주장이 성립하려면**

platform reliability

**사전 반증조건**

tech parity/outage

**실제 결과**

장기 성장.

**정량적 괴리**

주가 / $65.91 / upside / 2024-01 ~$88.75

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Technology moat 가설은 'tech parity/outage'를 반증조건으로 저장한다.

#### 2. Low costs — 적중 · 논지 비중 18%

**당시 주장**

industry-low fees/margin rates가 share를 늘린다.

**당시 근거**

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

**이 주장이 성립하려면**

cost advantage

**사전 반증조건**

price parity

**실제 결과**

계좌 증가.

**정량적 괴리**

2021 NI / $1.636bn / earnings compound / 2023 pretax $3.069bn

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Low costs 가설은 'price parity'를 반증조건으로 저장한다.

#### 3. Client balances — 적중 · 논지 비중 16%

**당시 주장**

client equity/cash가 earnings base를 키운다.

**당시 근거**

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

**이 주장이 성립하려면**

retention

**사전 반증조건**

large outflows

**실제 결과**

NII base 확대.

**정량적 괴리**

2023 NII / 상승 기대 / rate leverage / $2.794bn +68%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Client balances 가설은 'large outflows'를 반증조건으로 저장한다.

#### 4. Rate hikes — 강한 적중 · 논지 비중 16%

**당시 주장**

Fed hikes가 NII를 크게 높인다.

**당시 근거**

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

**이 주장이 성립하려면**

cash beta<asset yield increase

**사전 반증조건**

deposit repricing fully offsets

**실제 결과**

2023 +68%.

**정량적 괴리**

Balance sheet / zero/low corporate debt / resilience / strong capital

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Rate hikes 가설은 'deposit repricing fully offsets'를 반증조건으로 저장한다.

#### 5. Balance sheet — 적중 · 논지 비중 16%

**당시 주장**

낮은 debt가 downturn risk를 낮춘다.

**당시 근거**

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

**이 주장이 성립하려면**

capital discipline

**사전 반증조건**

regulatory loss

**실제 결과**

안정.

**정량적 괴리**

2022-03 약 $65.91 → 2024-01 raw 약 $88.75, 약 +35%. Earnings catalyst는 더 강하게 적중.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Balance sheet 가설은 'regulatory loss'를 반증조건으로 저장한다.

#### 6. Valuation — 적중 · 논지 비중 16%

**당시 주장**

$25.8bn mcap 대비 earnings power가 저평가다.

**당시 근거**

IBKR는 brokerage technology moat, industry-low all-in costs, high margins, 거의 없는 corporate debt와 growing client balances를 보유하고 있다. 2022 rate hikes는 고객 cash와 margin balances에서 발생하는 NII를 크게 증가시킬 촉매라고 봤다.

**이 주장이 성립하려면**

earnings delivery

**사전 반증조건**

multiple compression

**실제 결과**

주가 +35%, earnings 더 강함.

**정량적 괴리**

2022-03 약 $65.91 → 2024-01 raw 약 $88.75, 약 +35%. Earnings catalyst는 더 강하게 적중.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Valuation 가설은 'multiple compression'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2023 NII는 $2.794bn으로 68% 증가했고 total net revenues $4.340bn, pretax income $3.069bn, diluted EPS $5.67을 기록했다. 주가도 cutoff까지 약 35% 상승했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2022-03 약 $65.91 → 2024-01 raw 약 $88.75, 약 +35%. Earnings catalyst는 더 강하게 적중. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

금리상승을 단순 은행식 NIM bet가 아니라 이미 성장하는 client-assets platform에 붙은 convexity로 본 점이 좋았다. 가격성과보다 earnings mechanism이 더 명확하게 적중했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-12-31 — 연속 금리인상과 함께 NII가 큰 폭으로 증가해 핵심 catalyst가 직접 확인됐다. 회피 가능성: 해당 없음. 이후에는 client cash beta와 rate cuts sensitivity를 반대 방향 falsifier로 저장해야 한다.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $65.91 | upside | 2024-01 ~$88.75 | 성공 |
| 2021 NI | $1.636bn | earnings compound | 2023 pretax $3.069bn | 적중 |
| 2023 NII | 상승 기대 | rate leverage | $2.794bn +68% | 강한 적중 |
| Balance sheet | zero/low corporate debt | resilience | strong capital | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2022-03-16 | VIC 아이디어 게시 | 2021 $1.64bn income·zero debt·rate-hike Long |
| 2022-12-31 | 최초 핵심 검증·반증 신호 | 연속 금리인상과 함께 NII가 큰 폭으로 증가해 핵심 catalyst가 직접 확인됐다. |
| 2017-03-08 | Market-making wind-down 발표 | brokerage franchise가 더 선명해짐 |
| 2017-12-31 | 대부분 market making exit | segment simplification 완료 |
| 2023-12-31 | Rate-cycle 결과 | NII $2.79bn, pretax $3.07bn |
| 2024-01-31 | 고정 평가기준일 | 2022-03 약 $65.91 → 2024-01 raw 약 $88.75, 약 +35%. Earnings catalyst는 더 강하게 적중. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2022-12-31 — 연속 금리인상과 함께 NII가 큰 폭으로 증가해 핵심 catalyst가 직접 확인됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음. 이후에는 client cash beta와 rate cuts sensitivity를 반대 방향 falsifier로 저장해야 한다.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC IBKR 2022-03-16 원문](https://www.valueinvestorsclub.com/idea/INTERACTIVE_BROKERS_GROUP/9002721703) — Value Investors Club / user SQL, 2022-03-16. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Interactive Brokers 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119724000083/ibkr-20231231x10k.htm) — SEC, 2024-02-29. 2023 net revenue, pretax, NII, commissions, NIM 확인
- [3. Interactive Brokers 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1381197/000138119720000006/ibkr-20191231x10k.htm) — SEC, 2020-02-28. market-making exit와 brokerage structure 확인
- [4. Interactive Brokers 2017 Annual Report](https://investors.interactivebrokers.com/download/2017_IBG_AR.pdf) — Interactive Brokers, 2018-02-28. 2017 market-making wind-down·business transition 확인
- [5. Interactive Brokers historical prices](https://www.digrin.com/stocks/detail/IBKR/price) — Digrin, 2024-01-31. 역사적 가격경로 교차검증
- [6. Interactive Brokers Investor Relations](https://investors.interactivebrokers.com/) — Interactive Brokers, 2024-01-31. accounts/client equity·financial releases

---
# DISCOVER FINANCIAL SERVICES (DFS) — 기업과 비즈니스

## 1. 무슨 기업인가

Discover Financial Services는 신용카드 대출을 직접 보유하는 issuer이면서 Discover Network, PULSE debit network, Diners Club network를 운영하는 결제회사다. 2007년 Morgan Stanley에서 분사됐다. 카드사업의 핵심 수익은 카드대출 잔액에서 받는 interest yield와 interchange/fees이며, deposits·securitization·wholesale debt로 자금을 조달한다. 따라서 수익성은 card receivables 성장, net interest margin, funding cost, rewards expense, delinquency와 net charge-off에 좌우된다. 네트워크 사업은 거래액이 늘수록 fee revenue를 얻지만 Visa/Mastercard보다 규모가 작아 closed-loop의 customer data와 merchant economics가 중요하다. 2023년 loans는 약 $128.4bn, 이 중 card loans $102.3bn, consumer deposits $84.0bn, network volume $589bn이었다. 2023 net charge-off rate는 3.42%로 2022 1.82%에서 상승했고, net income은 약 $2.94bn, EPS $11.26, ROE 21%였다. 핵심 KPI는 card loan growth, NIM, funding mix/deposit cost, delinquency/charge-off, reserve coverage, payment volume, rewards rate, CET1/capital return과 regulatory/compliance costs다.

## 2. 산업 가치사슬과 돈의 흐름

Discover의 cash engine은 카드대출 yield − deposit/wholesale funding cost − credit losses − rewards/operating expense다. 좋은 시기에는 높은 revolving yield와 낮은 charge-offs 때문에 ROE가 매우 높아지지만 recession에서는 charge-offs가 급증해 earnings가 빠르게 훼손될 수 있다. 2012 VIC 논지는 3%대 고비용 CD가 1%대 신규 funding으로 교체될 때 funding cost만으로 NIM과 EPS가 개선되는 구조를 포착했다. 반대로 2020에는 COVID reserve build가 미래손실을 지나치게 선반영했는지가 핵심이었다. Payment network는 카드대출과 달리 capital-light fee business라 혼합 valuation이 필요하다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Discover의 장점은 issuer와 network를 동시에 가진 closed-loop data, 높은 direct-deposit funding, strong card franchise와 PULSE/Diners network다. 그러나 credit card는 Chase, Amex, Citi, Capital One 등과 경쟁하며 rewards·marketing cost가 높다. Visa/Mastercard에 비해 network acceptance/scale도 약하다. 따라서 낮은 P/E가 항상 싸다는 뜻이 아니고, credit normalization과 funding cost를 cycle-adjusted 해야 한다. 특히 분사 직후나 crisis에는 capital adequacy와 deposit access가 valuation floor를 결정한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2007-10-22 | Long | Long | Morgan Stanley spin·card/network value Long | SQL: 1년 -43.5%, 2년 -23.4%, 3년 -9.6%, 5년 +110%. 초기 하방은 크게 틀렸지만 franchise 생존 후 장기 회복. | 장기 사업성공·GFC 하방 치명적 과소평가 |
| 2012-01-04 | Long | Long | Funding-cost refi·low-$30s fair value Long | SQL: 1년 +62.7%, 2년 +130.1%, 3년 +171.3%, 5년 +221.7%. 전설적 성공. | 전설적 성공 |
| 2020-10-08 | Short | Long | COVID reserve overreaction·$88 Long | SQL: 1개월 +17.4%, 6개월 +54.0%, 1년 +101.4%, 2년 +47.0%. 강한 성공. | 전설적 성공 |

---

<!-- idea:a9bd5585-9390-451a-b292-d832c95c674e -->
## 1. 2007-10-22 — Morgan Stanley spin·card/network value Long

### 결론부터

**종합판정: 장기 사업성공·GFC 하방 치명적 과소평가.** Spin dislocation은 맞아도 financial company는 balance-sheet/credit cycle이 asset value를 압도할 수 있다. 'forced selling'보다 receivable credit quality와 funding access를 먼저 stress했어야 한다.

**주가·증권 결과:** SQL: 1년 -43.5%, 2년 -23.4%, 3년 -9.6%, 5년 +110%. 초기 하방은 크게 틀렸지만 franchise 생존 후 장기 회복.

**Thesis / Process 점수:** 4 / 4.5

### 1. 무슨 기업인가

Discover Financial Services는 신용카드 대출을 직접 보유하는 issuer이면서 Discover Network, PULSE debit network, Diners Club network를 운영하는 결제회사다. 2007년 Morgan Stanley에서 분사됐다. 카드사업의 핵심 수익은 카드대출 잔액에서 받는 interest yield와 interchange/fees이며, deposits·securitization·wholesale debt로 자금을 조달한다. 따라서 수익성은 card receivables 성장, net interest margin, funding cost, rewards expense, delinquency와 net charge-off에 좌우된다. 네트워크 사업은 거래액이 늘수록 fee revenue를 얻지만 Visa/Mastercard보다 규모가 작아 closed-loop의 customer data와 merchant economics가 중요하다. 2023년 loans는 약 $128.4bn, 이 중 card loans $102.3bn, consumer deposits $84.0bn, network volume $589bn이었다. 2023 net charge-off rate는 3.42%로 2022 1.82%에서 상승했고, net income은 약 $2.94bn, EPS $11.26, ROE 21%였다. 핵심 KPI는 card loan growth, NIM, funding mix/deposit cost, delinquency/charge-off, reserve coverage, payment volume, rewards rate, CET1/capital return과 regulatory/compliance costs다.

### 2. 산업 가치사슬과 돈의 흐름

Discover의 cash engine은 카드대출 yield − deposit/wholesale funding cost − credit losses − rewards/operating expense다. 좋은 시기에는 높은 revolving yield와 낮은 charge-offs 때문에 ROE가 매우 높아지지만 recession에서는 charge-offs가 급증해 earnings가 빠르게 훼손될 수 있다. 2012 VIC 논지는 3%대 고비용 CD가 1%대 신규 funding으로 교체될 때 funding cost만으로 NIM과 EPS가 개선되는 구조를 포착했다. 반대로 2020에는 COVID reserve build가 미래손실을 지나치게 선반영했는지가 핵심이었다. Payment network는 카드대출과 달리 capital-light fee business라 혼합 valuation이 필요하다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Discover의 장점은 issuer와 network를 동시에 가진 closed-loop data, 높은 direct-deposit funding, strong card franchise와 PULSE/Diners network다. 그러나 credit card는 Chase, Amex, Citi, Capital One 등과 경쟁하며 rewards·marketing cost가 높다. Visa/Mastercard에 비해 network acceptance/scale도 약하다. 따라서 낮은 P/E가 항상 싸다는 뜻이 아니고, credit normalization과 funding cost를 cycle-adjusted 해야 한다. 특히 분사 직후나 crisis에는 capital adequacy와 deposit access가 valuation floor를 결정한다.

### 4. 당시 VIC 원문과 핵심 숫자

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

최근 Morgan Stanley spin으로 forced selling과 standalone uncertainty가 discount를 만들고, card issuer earnings와 Discover/PULSE/Diners network를 분리하면 intrinsic value가 시장가보다 높다고 판단. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Spin dislocation — 부분 · 논지 비중 18%

**당시 주장**

Morgan Stanley 분리가 forced selling을 만든다.

**당시 근거**

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

**이 주장이 성립하려면**

business stable

**사전 반증조건**

credit shock

**실제 결과**

dislocation은 있었으나 credit cycle이 더 큼.

**정량적 괴리**

Entry / ~$16 / rerating / 1년 -43.5%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Spin dislocation 가설은 'credit shock'를 반증조건으로 저장한다.

#### 2. Card franchise — 부분 적중 · 논지 비중 18%

**당시 주장**

Discover 카드 고객/receivables가 durable하다.

**당시 근거**

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

**이 주장이 성립하려면**

credit losses manageable

**사전 반증조건**

charge-offs surge

**실제 결과**

생존했지만 큰 cycle loss.

**정량적 괴리**

2년 / - / recovery / -23.4%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Card franchise 가설은 'charge-offs surge'를 반증조건으로 저장한다.

#### 3. Network value — 적중 · 논지 비중 16%

**당시 주장**

Discover/PULSE/Diners가 독립 fee value를 갖는다.

**당시 근거**

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

**이 주장이 성립하려면**

volume/acceptance

**사전 반증조건**

network erosion

**실제 결과**

장기 유지.

**정량적 괴리**

5년 / - / franchise value / +110%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Network value 가설은 'network erosion'를 반증조건으로 저장한다.

#### 4. Funding — 실패 · 논지 비중 16%

**당시 주장**

standalone funding이 안정적이다.

**당시 근거**

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

**이 주장이 성립하려면**

deposit/securitization access

**사전 반증조건**

wholesale freeze

**실제 결과**

GFC에서 큰 위험.

**정량적 괴리**

Network / hidden asset / 가치 유지 / Discover/PULSE 지속

**분석 오류·핵심**

현재 earnings를 funding·credit·segment transition 없이 선형적으로 자본화했다.

**재사용할 교훈**

Funding 가설은 'wholesale freeze'를 반증조건으로 저장한다.

#### 5. Credit normalization — 실패 · 논지 비중 16%

**당시 주장**

손실률이 정상범위에 머문다.

**당시 근거**

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

**이 주장이 성립하려면**

unemployment benign

**사전 반증조건**

severe recession

**실제 결과**

2008~09 악화.

**정량적 괴리**

SQL: 1년 -43.5%, 2년 -23.4%, 3년 -9.6%, 5년 +110%. 초기 하방은 크게 틀렸지만 franchise 생존 후 장기 회복.

**분석 오류·핵심**

현재 earnings를 funding·credit·segment transition 없이 선형적으로 자본화했다.

**재사용할 교훈**

Credit normalization 가설은 'severe recession'를 반증조건으로 저장한다.

#### 6. Long-term value — 장기 적중·경로 실패 · 논지 비중 16%

**당시 주장**

spin discount 해소로 좋은 수익.

**당시 근거**

Discover는 미국 주요 credit-card issuer이면서 자체 payments network를 가진 독특한 franchise고, Morgan Stanley에서 2007-06-30 분리되며 자연 주주층이 정리되지 않아 싸다고 봤다. PULSE debit network와 Diners global network가 hidden value를 제공한다고 주장했다.

**이 주장이 성립하려면**

survival

**사전 반증조건**

capital impairment

**실제 결과**

5년 +110%지만 큰 drawdown.

**정량적 괴리**

SQL: 1년 -43.5%, 2년 -23.4%, 3년 -9.6%, 5년 +110%. 초기 하방은 크게 틀렸지만 franchise 생존 후 장기 회복.

**분석 오류·핵심**

현재 earnings를 funding·credit·segment transition 없이 선형적으로 자본화했다.

**재사용할 교훈**

Long-term value 가설은 'capital impairment'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

프랜차이즈는 생존했지만 2008 credit cycle이 card losses와 funding concern을 크게 악화시켜 1년 주가가 43.5% 하락했다. 5년에는 약 +110%로 회복해 network/card value는 남았지만 entry risk가 컸다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 SQL: 1년 -43.5%, 2년 -23.4%, 3년 -9.6%, 5년 +110%. 초기 하방은 크게 틀렸지만 franchise 생존 후 장기 회복. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

Spin dislocation은 맞아도 financial company는 balance-sheet/credit cycle이 asset value를 압도할 수 있다. 'forced selling'보다 receivable credit quality와 funding access를 먼저 stress했어야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-09-30 — delinquencies·charge-offs와 wholesale funding stress가 확대되며 단순 spin discount thesis가 credit-risk thesis로 바뀌었다. 회피 가능성: 매우 높음. unemployment/charge-off stress와 deposit funding transition을 별도 downside case로 넣었어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

장기 사업성공·GFC 하방 치명적 과소평가. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | ~$16 | rerating | 1년 -43.5% | 치명적 단기 실패 |
| 2년 | - | recovery | -23.4% | 미달 |
| 5년 | - | franchise value | +110% | 장기 성공 |
| Network | hidden asset | 가치 유지 | Discover/PULSE 지속 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2007-10-22 | VIC 아이디어 게시 | Morgan Stanley spin·card/network value Long |
| 2008-09-30 | 최초 핵심 검증·반증 신호 | delinquencies·charge-offs와 wholesale funding stress가 확대되며 단순 spin discount thesis가 credit-risk thesis로 바뀌었다. |
| 2007-06-30 | Morgan Stanley 분리 | standalone Discover 시작 |
| 2020-12-31 | COVID credit outcome | reserve tail probability 재평가 |
| 2023-12-31 | 정상 credit cycle 복귀 | NCO 3.42%, EPS $11.26 |
| 2024-01-31 | 고정 평가기준일 | SQL: 1년 -43.5%, 2년 -23.4%, 3년 -9.6%, 5년 +110%. 초기 하방은 크게 틀렸지만 franchise 생존 후 장기 회복. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2008-09-30 — delinquencies·charge-offs와 wholesale funding stress가 확대되며 단순 spin discount thesis가 credit-risk thesis로 바뀌었다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 매우 높음. unemployment/charge-off stress와 deposit funding transition을 별도 downside case로 넣었어야 한다.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC DFS 2007-10-22 원문](https://www.valueinvestorsclub.com/idea/Discover_Financial_Services/7725498133) — Value Investors Club / user SQL, 2007-10-22. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Discover spin-off 8-K](https://www.sec.gov/Archives/edgar/data/1393612/000119312507150060/d8k.htm) — SEC, 2007-07-02. Morgan Stanley separation 완료 확인
- [3. Discover 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393612/000119312508039547/d10k.htm) — SEC, 2008-02-29. 분사 직후 card/network/funding 구조 확인
- [4. Discover 2023 Annual Report](https://www.sec.gov/Archives/edgar/data/1393612/000139361224000023/dfs12312023ars.pdf) — SEC / Discover, 2024-02-23. 2023 loans, deposits, network volume, NCO, EPS/ROE 확인
- [5. Discover Jan-2024 card statistics](https://www.sec.gov/Archives/edgar/data/1393612/000139361224000006/exhibit99101-31x24.htm) — SEC / Discover, 2024-02-15. card ending loans·delinquency/chargeoff follow-up
- [6. Discover Investor Relations](https://investorrelations.discover.com/) — Discover, 2024-01-31. historical results·capital disclosures

---

<!-- idea:cd78eefd-abeb-42f3-917d-7e8fa7c91636 -->
## 2. 2012-01-04 — Funding-cost refi·low-$30s fair value Long

### 결론부터

**종합판정: 전설적 성공.** 좋은 금융주 분석의 예다. 거시적으로 '금리가 낮다'가 아니라 liability stack의 재가격 schedule을 보고 정확한 EPS bridge를 만들었다.

**주가·증권 결과:** SQL: 1년 +62.7%, 2년 +130.1%, 3년 +171.3%, 5년 +221.7%. 전설적 성공.

**Thesis / Process 점수:** 9.6 / 9.3

### 1. 무슨 기업인가

Discover Financial Services는 신용카드 대출을 직접 보유하는 issuer이면서 Discover Network, PULSE debit network, Diners Club network를 운영하는 결제회사다. 2007년 Morgan Stanley에서 분사됐다. 카드사업의 핵심 수익은 카드대출 잔액에서 받는 interest yield와 interchange/fees이며, deposits·securitization·wholesale debt로 자금을 조달한다. 따라서 수익성은 card receivables 성장, net interest margin, funding cost, rewards expense, delinquency와 net charge-off에 좌우된다. 네트워크 사업은 거래액이 늘수록 fee revenue를 얻지만 Visa/Mastercard보다 규모가 작아 closed-loop의 customer data와 merchant economics가 중요하다. 2023년 loans는 약 $128.4bn, 이 중 card loans $102.3bn, consumer deposits $84.0bn, network volume $589bn이었다. 2023 net charge-off rate는 3.42%로 2022 1.82%에서 상승했고, net income은 약 $2.94bn, EPS $11.26, ROE 21%였다. 핵심 KPI는 card loan growth, NIM, funding mix/deposit cost, delinquency/charge-off, reserve coverage, payment volume, rewards rate, CET1/capital return과 regulatory/compliance costs다.

### 2. 산업 가치사슬과 돈의 흐름

Discover의 cash engine은 카드대출 yield − deposit/wholesale funding cost − credit losses − rewards/operating expense다. 좋은 시기에는 높은 revolving yield와 낮은 charge-offs 때문에 ROE가 매우 높아지지만 recession에서는 charge-offs가 급증해 earnings가 빠르게 훼손될 수 있다. 2012 VIC 논지는 3%대 고비용 CD가 1%대 신규 funding으로 교체될 때 funding cost만으로 NIM과 EPS가 개선되는 구조를 포착했다. 반대로 2020에는 COVID reserve build가 미래손실을 지나치게 선반영했는지가 핵심이었다. Payment network는 카드대출과 달리 capital-light fee business라 혼합 valuation이 필요하다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Discover의 장점은 issuer와 network를 동시에 가진 closed-loop data, 높은 direct-deposit funding, strong card franchise와 PULSE/Diners network다. 그러나 credit card는 Chase, Amex, Citi, Capital One 등과 경쟁하며 rewards·marketing cost가 높다. Visa/Mastercard에 비해 network acceptance/scale도 약하다. 따라서 낮은 P/E가 항상 싸다는 뜻이 아니고, credit normalization과 funding cost를 cycle-adjusted 해야 한다. 특히 분사 직후나 crisis에는 capital adequacy와 deposit access가 valuation floor를 결정한다.

### 4. 당시 VIC 원문과 핵심 숫자

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

### 5. 밸류에이션과 기대수익의 연결

Fair value low-$30s. 기존 CD funding 약 3.30%를 신규 marginal funding 약 1.33%로 교체하면 funding cost가 약 60bp 개선되고 EPS 약 $0.40 증가 가능. Earnings revisions가 상방. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Funding refi — 강한 적중 · 논지 비중 18%

**당시 주장**

고금리 CD가 낮은 금리로 교체된다.

**당시 근거**

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

**이 주장이 성립하려면**

maturities/refi access

**사전 반증조건**

deposit cost rises

**실제 결과**

기계적 tailwind 현실화.

**정량적 괴리**

Entry / $19.50 / low-$30s / 1년 +62.7%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Funding refi 가설은 'deposit cost rises'를 반증조건으로 저장한다.

#### 2. 60bp benefit — 적중 · 논지 비중 18%

**당시 주장**

funding cost가 약 60bp 개선된다.

**당시 근거**

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

**이 주장이 성립하려면**

mix shift

**사전 반증조건**

asset yield falls faster

**실제 결과**

earnings 개선.

**정량적 괴리**

Legacy CD / 3.30% / refi / ~1.33% marginal funding

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

60bp benefit 가설은 'asset yield falls faster'를 반증조건으로 저장한다.

#### 3. Credit normalize — 적중 · 논지 비중 16%

**당시 주장**

GFC charge-offs가 정상화된다.

**당시 근거**

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

**이 주장이 성립하려면**

labor/consumer recovery

**사전 반증조건**

double dip

**실제 결과**

정상화.

**정량적 괴리**

Funding benefit / ~60bp / EPS +$0.40 / earnings tailwind

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Credit normalize 가설은 'double dip'를 반증조건으로 저장한다.

#### 4. Capital strength — 적중 · 논지 비중 16%

**당시 주장**

강한 capital이 buyback/dividend를 허용한다.

**당시 근거**

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

**이 주장이 성립하려면**

regulatory approval

**사전 반증조건**

capital shortfall

**실제 결과**

주주환원 확대.

**정량적 괴리**

5년 / - / compound / +221.7%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Capital strength 가설은 'capital shortfall'를 반증조건으로 저장한다.

#### 5. EPS revisions — 적중 · 논지 비중 16%

**당시 주장**

consensus가 상향된다.

**당시 근거**

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

**이 주장이 성립하려면**

funding+credit

**사전 반증조건**

revenue miss

**실제 결과**

실적 개선.

**정량적 괴리**

SQL: 1년 +62.7%, 2년 +130.1%, 3년 +171.3%, 5년 +221.7%. 전설적 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

EPS revisions 가설은 'revenue miss'를 반증조건으로 저장한다.

#### 6. Low-$30s — 강한 적중 · 논지 비중 16%

**당시 주장**

fair value가 low-$30s 이상이다.

**당시 근거**

GFC 후 credit losses가 정상화되고 capital이 강한데 시장은 여전히 crisis multiple을 적용한다고 봤다. 특히 고금리 legacy CD가 만기돼 저금리 deposit/wholesale funding으로 바뀌는 mechanical earnings tailwind를 정량화했다.

**이 주장이 성립하려면**

normal multiple

**사전 반증조건**

new crisis

**실제 결과**

1년 내 초과 방향.

**정량적 괴리**

SQL: 1년 +62.7%, 2년 +130.1%, 3년 +171.3%, 5년 +221.7%. 전설적 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Low-$30s 가설은 'new crisis'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2012 이후 credit normalization과 낮은 funding costs, capital return이 earnings와 valuation을 동시에 끌어올렸다. 1년 +63%, 5년 +222%로 크게 성공했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 SQL: 1년 +62.7%, 2년 +130.1%, 3년 +171.3%, 5년 +221.7%. 전설적 성공. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

좋은 금융주 분석의 예다. 거시적으로 '금리가 낮다'가 아니라 liability stack의 재가격 schedule을 보고 정확한 EPS bridge를 만들었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-12-31 — funding-cost decline과 credit normalization이 실제 earnings revisions에 반영되며 주가가 1년 +60% 이상 상승했다. 회피 가능성: 해당 없음. 이후에는 credit costs 재상승을 cycle falsifier로 봐야 했다.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $19.50 | low-$30s | 1년 +62.7% | 강한 적중 |
| Legacy CD | 3.30% | refi | ~1.33% marginal funding | 적중 |
| Funding benefit | ~60bp | EPS +$0.40 | earnings tailwind | 적중 |
| 5년 | - | compound | +221.7% | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2012-01-04 | VIC 아이디어 게시 | Funding-cost refi·low-$30s fair value Long |
| 2012-12-31 | 최초 핵심 검증·반증 신호 | funding-cost decline과 credit normalization이 실제 earnings revisions에 반영되며 주가가 1년 +60% 이상 상승했다. |
| 2007-06-30 | Morgan Stanley 분리 | standalone Discover 시작 |
| 2020-12-31 | COVID credit outcome | reserve tail probability 재평가 |
| 2023-12-31 | 정상 credit cycle 복귀 | NCO 3.42%, EPS $11.26 |
| 2024-01-31 | 고정 평가기준일 | SQL: 1년 +62.7%, 2년 +130.1%, 3년 +171.3%, 5년 +221.7%. 전설적 성공. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2012-12-31 — funding-cost decline과 credit normalization이 실제 earnings revisions에 반영되며 주가가 1년 +60% 이상 상승했다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음. 이후에는 credit costs 재상승을 cycle falsifier로 봐야 했다.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC DFS 2012-01-04 원문](https://www.valueinvestorsclub.com/idea/DISCOVER_FINANCIAL_SVCS_INC/0712036079) — Value Investors Club / user SQL, 2012-01-04. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Discover spin-off 8-K](https://www.sec.gov/Archives/edgar/data/1393612/000119312507150060/d8k.htm) — SEC, 2007-07-02. Morgan Stanley separation 완료 확인
- [3. Discover 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393612/000119312508039547/d10k.htm) — SEC, 2008-02-29. 분사 직후 card/network/funding 구조 확인
- [4. Discover 2023 Annual Report](https://www.sec.gov/Archives/edgar/data/1393612/000139361224000023/dfs12312023ars.pdf) — SEC / Discover, 2024-02-23. 2023 loans, deposits, network volume, NCO, EPS/ROE 확인
- [5. Discover Jan-2024 card statistics](https://www.sec.gov/Archives/edgar/data/1393612/000139361224000006/exhibit99101-31x24.htm) — SEC / Discover, 2024-02-15. card ending loans·delinquency/chargeoff follow-up
- [6. Discover Investor Relations](https://investorrelations.discover.com/) — Discover, 2024-01-31. historical results·capital disclosures

---

<!-- idea:e7fc8ac3-4305-4316-9e0f-f492cd745ef9 -->
## 3. 2020-10-08 — COVID reserve overreaction·$88 Long

### 결론부터

**종합판정: 전설적 성공.** '신용이 영구적으로 좋아졌다'가 아니라 reserves와 market price가 특정 tail scenario를 너무 높은 확률로 반영한다고 본 probability trade였다. 그래서 후일 charge-offs 상승과 모순되지 않는다.

**주가·증권 결과:** SQL: 1개월 +17.4%, 6개월 +54.0%, 1년 +101.4%, 2년 +47.0%. 강한 성공.

**Thesis / Process 점수:** 9.6 / 9.3

### 1. 무슨 기업인가

Discover Financial Services는 신용카드 대출을 직접 보유하는 issuer이면서 Discover Network, PULSE debit network, Diners Club network를 운영하는 결제회사다. 2007년 Morgan Stanley에서 분사됐다. 카드사업의 핵심 수익은 카드대출 잔액에서 받는 interest yield와 interchange/fees이며, deposits·securitization·wholesale debt로 자금을 조달한다. 따라서 수익성은 card receivables 성장, net interest margin, funding cost, rewards expense, delinquency와 net charge-off에 좌우된다. 네트워크 사업은 거래액이 늘수록 fee revenue를 얻지만 Visa/Mastercard보다 규모가 작아 closed-loop의 customer data와 merchant economics가 중요하다. 2023년 loans는 약 $128.4bn, 이 중 card loans $102.3bn, consumer deposits $84.0bn, network volume $589bn이었다. 2023 net charge-off rate는 3.42%로 2022 1.82%에서 상승했고, net income은 약 $2.94bn, EPS $11.26, ROE 21%였다. 핵심 KPI는 card loan growth, NIM, funding mix/deposit cost, delinquency/charge-off, reserve coverage, payment volume, rewards rate, CET1/capital return과 regulatory/compliance costs다.

### 2. 산업 가치사슬과 돈의 흐름

Discover의 cash engine은 카드대출 yield − deposit/wholesale funding cost − credit losses − rewards/operating expense다. 좋은 시기에는 높은 revolving yield와 낮은 charge-offs 때문에 ROE가 매우 높아지지만 recession에서는 charge-offs가 급증해 earnings가 빠르게 훼손될 수 있다. 2012 VIC 논지는 3%대 고비용 CD가 1%대 신규 funding으로 교체될 때 funding cost만으로 NIM과 EPS가 개선되는 구조를 포착했다. 반대로 2020에는 COVID reserve build가 미래손실을 지나치게 선반영했는지가 핵심이었다. Payment network는 카드대출과 달리 capital-light fee business라 혼합 valuation이 필요하다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Discover의 장점은 issuer와 network를 동시에 가진 closed-loop data, 높은 direct-deposit funding, strong card franchise와 PULSE/Diners network다. 그러나 credit card는 Chase, Amex, Citi, Capital One 등과 경쟁하며 rewards·marketing cost가 높다. Visa/Mastercard에 비해 network acceptance/scale도 약하다. 따라서 낮은 P/E가 항상 싸다는 뜻이 아니고, credit normalization과 funding cost를 cycle-adjusted 해야 한다. 특히 분사 직후나 crisis에는 capital adequacy와 deposit access가 valuation floor를 결정한다.

### 4. 당시 VIC 원문과 핵심 숫자

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

### 5. 밸류에이션과 기대수익의 연결

2022 consensus EPS 약 $8.80에 10x = $88 by end-2021, 약 +38%; dividend $1.76 추가. COVID credit concern이 normalized earnings보다 과도하게 가격에 반영됐다고 봄. 사후에는 customer accounts/loans → balances → commission/NIM → credit/funding cost → capital → per-share earnings 순으로 재검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Reserve overreaction — 강한 적중 · 논지 비중 18%

**당시 주장**

COVID reserves가 실제손실보다 보수적이다.

**당시 근거**

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

**이 주장이 성립하려면**

stimulus/borrower liquidity

**사전 반증조건**

defaults surge

**실제 결과**

손실 feared case 미달.

**정량적 괴리**

Entry / $63.40 / $88 / 1년 +101.4%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Reserve overreaction 가설은 'defaults surge'를 반증조건으로 저장한다.

#### 2. Capital strength — 적중 · 논지 비중 18%

**당시 주장**

충분한 capital이 downside를 제한한다.

**당시 근거**

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

**이 주장이 성립하려면**

CET1/liquidity

**사전 반증조건**

capital raise

**실제 결과**

회복.

**정량적 괴리**

2022E EPS / $8.80 / 10x / 실적 정상화

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Capital strength 가설은 'capital raise'를 반증조건으로 저장한다.

#### 3. Loan demand — 적중 · 논지 비중 16%

**당시 주장**

카드 사용·대출이 정상화된다.

**당시 근거**

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

**이 주장이 성립하려면**

reopening

**사전 반증조건**

persistent contraction

**실제 결과**

회복.

**정량적 괴리**

Dividend / $1.76 / 추가 return / capital return 유지

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Loan demand 가설은 'persistent contraction'를 반증조건으로 저장한다.

#### 4. 10x normalized — 적중 · 논지 비중 16%

**당시 주장**

10x 2022 EPS가 보수적이다.

**당시 근거**

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

**이 주장이 성립하려면**

EPS $8.8 근접

**사전 반증조건**

credit remains impaired

**실제 결과**

주가 크게 rerating.

**정량적 괴리**

2023 NCO / pandemic panic / normal cycle / 3.42% vs 1.82%

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

10x normalized 가설은 'credit remains impaired'를 반증조건으로 저장한다.

#### 5. $88 target — 강한 적중 · 논지 비중 16%

**당시 주장**

+38% + dividend가 가능.

**당시 근거**

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

**이 주장이 성립하려면**

credit normalization

**사전 반증조건**

new lockdown

**실제 결과**

1년 +101%.

**정량적 괴리**

SQL: 1개월 +17.4%, 6개월 +54.0%, 1년 +101.4%, 2년 +47.0%. 강한 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

$88 target 가설은 'new lockdown'를 반증조건으로 저장한다.

#### 6. Temporary not permanent — 적중 · 논지 비중 16%

**당시 주장**

COVID shock는 one-off credit event다.

**당시 근거**

시장과 loss reserves가 unemployment/COVID charge-offs를 매우 보수적으로 반영했지만 stimulus, payment behavior와 strong capital 때문에 실제 credit losses가 feared case보다 낮을 가능성이 높다고 봤다. 정상화 EPS에 10x만 적용해도 $88.

**이 주장이 성립하려면**

policy support

**사전 반증조건**

structural borrower damage

**실제 결과**

당시 맞았지만 2023 normal credit cycle 재등장.

**정량적 괴리**

SQL: 1개월 +17.4%, 6개월 +54.0%, 1년 +101.4%, 2년 +47.0%. 강한 성공.

**분석 오류·핵심**

핵심 causal chain이 실제 balance-sheet/earnings data에서 확인됐다.

**재사용할 교훈**

Temporary not permanent 가설은 'structural borrower damage'를 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Credit losses는 예상보다 빠르게 안정됐고 주가는 1년 두 배가 됐다. 이후 2023 net charge-off rate가 3.42%로 2022 1.82%에서 상승해 credit cycle이 사라진 것은 아니었지만, 2020 reserve panic이 과도했다는 논지는 정확했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 SQL: 1개월 +17.4%, 6개월 +54.0%, 1년 +101.4%, 2년 +47.0%. 강한 성공. business mechanism과 cycle/path를 분리해 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

'신용이 영구적으로 좋아졌다'가 아니라 reserves와 market price가 특정 tail scenario를 너무 높은 확률로 반영한다고 본 probability trade였다. 그래서 후일 charge-offs 상승과 모순되지 않는다.

### 9. 최초 검증·반증 신호와 회피 가능성

2021-04-30 — 실제 charge-off/delinquency가 feared COVID path보다 훨씬 양호하고 reserve releases가 나타나면서 thesis가 빠르게 검증됐다. 회피 가능성: 해당 없음. 2022~23에는 정상 credit cycle로 새로 모델링해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. 금융주는 earnings multiple보다 고객 balance와 funding/credit의 재가격 schedule을 먼저 본다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $63.40 | $88 | 1년 +101.4% | 강한 적중 |
| 2022E EPS | $8.80 | 10x | 실적 정상화 | 적중 |
| Dividend | $1.76 | 추가 return | capital return 유지 | 적중 |
| 2023 NCO | pandemic panic | normal cycle | 3.42% vs 1.82% | 후속 cycle |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-10-08 | VIC 아이디어 게시 | COVID reserve overreaction·$88 Long |
| 2021-04-30 | 최초 핵심 검증·반증 신호 | 실제 charge-off/delinquency가 feared COVID path보다 훨씬 양호하고 reserve releases가 나타나면서 thesis가 빠르게 검증됐다. |
| 2007-06-30 | Morgan Stanley 분리 | standalone Discover 시작 |
| 2020-12-31 | COVID credit outcome | reserve tail probability 재평가 |
| 2023-12-31 | 정상 credit cycle 복귀 | NCO 3.42%, EPS $11.26 |
| 2024-01-31 | 고정 평가기준일 | SQL: 1개월 +17.4%, 6개월 +54.0%, 1년 +101.4%, 2년 +47.0%. 강한 성공. |

### Failure / Success Anatomy

- **근본 오류:** 수익식을 accounts/balances/spread 또는 funding stack/credit cost로 분해
- **최초 검증·반증 신호:** 2021-04-30 — 실제 charge-off/delinquency가 feared COVID path보다 훨씬 양호하고 reserve releases가 나타나면서 thesis가 빠르게 검증됐다.
- **당시 알 수 있었나:** accounts, client equity, commissions, margin balances, NII/NIM, card loans, deposit cost, delinquency/charge-off와 capital은 공시로 지속 확인 가능했다.
- **피할 수 있었나:** 해당 없음. 2022~23에는 정상 credit cycle로 새로 모델링해야 했다.
- **반사실 질문:** 거래량이나 대출성장 없이도 고객자산·funding mix·금리·credit cost가 바뀌면 normalized EPS와 equity value는 어떻게 달라지는가?

### 주요 근거자료

- [1. VIC DFS 2020-10-08 원문](https://www.valueinvestorsclub.com/idea/DISCOVER_FINANCIAL_SVCS/9055413728) — Value Investors Club / user SQL, 2020-10-08. 원 업로드 SQL에서 thesis·valuation·risk·방향 복원
- [2. Discover spin-off 8-K](https://www.sec.gov/Archives/edgar/data/1393612/000119312507150060/d8k.htm) — SEC, 2007-07-02. Morgan Stanley separation 완료 확인
- [3. Discover 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393612/000119312508039547/d10k.htm) — SEC, 2008-02-29. 분사 직후 card/network/funding 구조 확인
- [4. Discover 2023 Annual Report](https://www.sec.gov/Archives/edgar/data/1393612/000139361224000023/dfs12312023ars.pdf) — SEC / Discover, 2024-02-23. 2023 loans, deposits, network volume, NCO, EPS/ROE 확인
- [5. Discover Jan-2024 card statistics](https://www.sec.gov/Archives/edgar/data/1393612/000139361224000006/exhibit99101-31x24.htm) — SEC / Discover, 2024-02-15. card ending loans·delinquency/chargeoff follow-up
- [6. Discover Investor Relations](https://investorrelations.discover.com/) — Discover, 2024-01-31. historical results·capital disclosures

---

# 배치 공통 학습

1. **Broker의 진짜 scale moat는 branch count보다 automation과 risk engine일 수 있다.**
2. **낮은 commission만 보면 moat가 약해 보이지만 all-in cost·margin loan·market access까지 봐야 한다.**
3. **Segment가 사라져도 capability moat는 남을 수 있다.** IBKR market making exit가 대표적이다.
4. **NII는 금리 하나가 아니라 client cash/margin balances × asset yield − client cash beta의 함수다.**
5. **Credit card valuation은 P/E보다 funding cost와 net charge-off를 먼저 normalize한다.**
6. **Spin dislocation은 financial balance-sheet stress보다 약한 요인일 수 있다.**
7. **Liability repricing schedule을 추적하면 funding-cost catalyst를 정량화할 수 있다.**
8. **Reserve release thesis는 '신용이 영구적으로 좋다'는 주장이 아니라 tail probability mispricing일 수 있다.**
