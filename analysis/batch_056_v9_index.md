# Batch 056 — Stamps.com / Weight Watchers V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 055 마지막 STMP 2003-12-06 이후, reviewed idea_id를 제외한 다음 10건.
> **핵심 데이터 품질:** raw direction 10건 모두 Short이나 실제는 Long 6 / Short 4. WTW price-performance는 후대 Willis Towers Watson ticker reuse로 오염되어 outcome 판정에 사용하지 않음.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2007-07-03 | STMP | **Short** | **Long** | [STMP 2007](ideas/2007/2007-07-03_STMP_long.md) | stated 2009 horizon 실패 / 장기 business thesis 성공 |
| 2 | 2008-03-07 | STMP | **Short** | **Long** | [STMP 2008](ideas/2008/2008-03-07_STMP_long.md) | 단기 혼합 / 3~4년 성공 |
| 3 | 2016-02-06 | STMP | Short | **Short** | [STMP 2016 Feb](ideas/2016/2016-02-06_STMP_short.md) | **강한 실패** — TAM 정의 오류 |
| 4 | 2016-09-06 | STMP | Short | **Short** | [STMP 2016 Sep](ideas/2016/2016-09-06_STMP_short.md) | **timing 실패 / mechanism 일부 선행** |
| 5 | 2017-04-06 | STMP | **Short** | **Long** | [STMP 2017](ideas/2017/2017-04-06_STMP_long.md) | **강한 성공**, $500 target은 미달 |
| 6 | 2019-06-24 | STMP | **Short** | **Long** | [STMP 2019](ideas/2019/2019-06-24_STMP_long.md) | **매우 강한 성공** — broken earnings를 0으로 둔 SOTP |
| 7 | 2008-05-11 | WTW | Short | **Short** | [WTW 2008](ideas/2008/2008-05-11_WTW_short.md) | **전술적 강한 성공** — recession + leverage |
| 8 | 2013-03-21 | WTW | **Short** | **Long** | [WTW 2013 Mar](ideas/2013/2013-03-21_WTW_long.md) | **강한 실패** — free apps를 temporary로 오판 |
| 9 | 2013-09-30 | WTW | **Short** | **Long** | [WTW 2013 Sep](ideas/2013/2013-09-30_WTW_long.md) | **강한 실패** — category redefinition / debt 해석 오류 |
| 10 | 2014-02-22 | WTW | Short | **Short** | [WTW 2014](ideas/2014/2014-02-22_WTW_short.md) | **fundamental 성공 / borrow economics 위험** |

---

## 2. Direction Audit

raw SQL은 10건 모두 `is_short=true`.

실제 원문:
- **Long 6건:** STMP 2007, STMP 2008, STMP 2017, STMP 2019, WTW 2013-03, WTW 2013-09
- **Short 4건:** STMP 2016-02, STMP 2016-09, WTW 2008, WTW 2014

따라서 **6건 direction correction**.

특히:
- STMP 2017 작성자는 자신을 short-seller라 소개하지만 “STMP is my biggest position… I am long”이라고 명시.
- STMP 2019 원문은 “We recommend purchase of Stamps.com”.
- WTW 2013-03 원문은 “Recommendation: Buy”.
- WTW 2013-09 원문은 “buy at $37 or better”.

---

# PART A — STAMPS.COM: 2007→2019, 같은 회사에서 thesis quality가 어떻게 진화했나

## 3. STMP 2007 Long — 좋은 회사 분석, 나쁜 stated horizon

### 당시 숫자
- price ~$13.78
- cash ~$104m
- NOL DTA ~$103m / PV ~$61m
- adjusted EV ~$137m
- TTM EBIT ~$11m
- pre-tax ROC ~95.7%

원문은 marketing을 expense가 아니라 **customer-acquisition growth capex**로 봤다.

### 2009 scenarios
- Downside $17.47
- Base $23.30
- Upside $28.40

실제:
- 2008말 ~$9.8
- 2009말 ~$9.0

즉 **원문의 모든 2009 price scenario가 빗나갔다.**

하지만:
- 2010 ~$13.3
- 2011 ~$26.1

로 장기 platform economics는 결국 드러났다.

### 교훈
**LTV/CAC가 좋다는 사실과 2년 내 multiple rerating은 별개다.**

---

## 4. STMP 2008 Long — 첫 thesis가 깨진 뒤 더 싸게 재심사

2007 actual:
- revenue ~$85m vs prior ~$95m expectation
- marketing ~$27m → ~$33m
- marketing/revenue 33% → 39%

2008 writeup은 이 failure를 숨기지 않고:
- TTM FCF ~$8.7m
- EV ~$91.5m
- EV/FCF ~10.5x
- NOL
- insider buying
- repurchases

로 다시 봤다.

### 결과
1~2년은 flat/down이었지만 2010~11 strong recovery.

### 교훈
**같은 회사라도 expectation reset + lower entry price가 생기면 새로운 투자다.**

---

## 5. STMP 2016-02 Short — 가장 큰 오류는 “무슨 시장인가”였다

Short 논리:
- postal volume decline
- churn
- acquisition-masked organic weakness
- Endicia >3x revenue
- ~32x EV/FCF

하지만 실제 성장시장은:
**letter mail이 아니라 e-commerce parcel shipping + shipping software**.

2016:
- paid customers +13%
- ARPU +50%
- mailing/shipping revenue +70%
- churn 3.3% → 3.0%

2017:
- paid customers +12%
- ARPU +15%
- mailing/shipping revenue +28%

### 실패식
**declining legacy category ≠ declining company TAM**

---

## 6. STMP 2016-09 Short — mechanism은 선행했지만 trade는 실패

원문:
- USPS reseller/NSA economics가 유지 불가능
- ~$90m EBIT at risk
- 약 80% downside

실제:
- 2017~18 earnings/stock 급등
- STMP $80~90대 → 2018 $270+ 구간

2019에는 실제로 USPS monetization reset이 발생했다.

그러나 이를 이유로 2016 Short를 성공이라 하면 안 된다.

### 핵심
**Structural mechanism ≠ investable timing.**

2.5년 동안 주가가 수배 상승하면 borrow/capital constraint로 Short는 이미 실패할 수 있다.

---

## 7. STMP 2017 Long — 산업을 다시 정의해서 Short thesis를 뒤집다

Writer는 dedicated short-seller였지만 STMP는 biggest Long.

### 재정의
Stamps.com이 아니라:
- Endicia
- ShipStation
- ShipWorks
- ShippingEasy

를 포함한 **shipping software ecosystem**.

### 당시 price
약 $110.

### 5Y thesis
- EPS ~$25
- 20x
- target **$500**

실제:
- 2018 $270+ 구간
- 2019 USPS shock으로 crash
- 2020 recovery
- 2021 **$330 cash takeout**

### 판정
Long은 강한 성공.
하지만 $500 target과 USPS risk map은 과도/불완전.

---

## 8. STMP 2019 Long — BATCH 56 최고의 equity Long

2019 두 번의 USPS shock 이후:
- 2018 EBITDA ~$258m
- 2019 guide ~$130m
- Street 2020 ~$100m
- market cap ~$750m

원문은 **old earnings 회복을 가정하지 않았다.**

### Zero monetization SOTP
- cash / HQ
- 575k SOHO subscribers
- 160k e-commerce shippers
- MetaPack
- other assets

합계:
**$37~47/share**, midpoint ~$42.

Alternative carrier monetization까지:
**midpoint ~$72**.

실제:
- 2020 revenue ~$758m, +33%
- >1m paid customers
- multi-carrier strategy 진전
- 2021 **$330 cash takeout**

### 핵심
**깨진 earnings를 정상화한 것이 아니라, 깨진 earnings를 0으로 두고 남는 자산을 샀다.**

---

## 9. STMP 전체 시계열

| 시점 | 방향 | 핵심 프레임 | 판정 |
|---|---|---|---|
| 2003 | Long | product + LTV/CAC | 초장기 대성공 |
| 2007 | Long | marketing = growth capex | horizon 실패 |
| 2008 | Long | reset valuation / FCF | 중기 성공 |
| 2016-02 | Short | declining mail / M&A masking | 강한 실패 |
| 2016-09 | Short | USPS contract risk | timing 실패 |
| 2017 | Long | shipping ecosystem | 강한 성공 |
| 2019 | Long | zero-USPS SOTP | 매우 강한 성공 |

### 분석의 질이 높아진 방향
**headline revenue → unit economics → platform definition → downside SOTP**

---

# PART B — WEIGHT WATCHERS: cycle Short에서 structural disruption으로

## 10. Critical Data Audit — WTW ticker contamination

SQLite의 WTW performance ratios는 Weight Watchers가 아닌 **Willis Towers Watson** ticker history와 섞인 흔적이 명확하다.

예를 들어 raw SQL의 2013 WTW performance는 Weight Watchers 당시 actual price path와 양립하지 않는다.

따라서:
- raw performance fields는 **원본 보존**
- canonical/outcome verdict에서는 **사용 금지**
- independently validated Weight Watchers price history와 SEC/company filings 사용

으로 처리한다.

이 batch는 단순 direction correction보다 이 문제가 더 중요하다.

---

## 11. WTW 2008 Short — tactical cycle Short 성공

원문:
- meeting attendance Q1 already declining
- debt-funded $1.025bn tender
- debt ~$830m → ~$1.8bn
- fixed-cost meeting model
- target ~$31 / 30% downside

실제 Weight Watchers stock:
**2008 annual 약 -33.6%**.

하지만 online:
- revenue +22.6%
- subscribers +16.3%

였으므로 company 전체의 secular collapse thesis는 아니었다.

### 교훈
**cycle Short로는 맞고 permanent Short로는 틀릴 수 있다.**

---

## 12. WTW 2013-03 Long — free apps를 “일시적 recruiting issue”로 봄

원문:
- price $41.73
- target $53
- upside $65
- downside $37
- 2012 FCF yield 11.2%
- 2014 recovery

writer는 January weakness를:
- payroll tax
- Jessica Simpson pregnancy
- poor campaign

등 temporary factors로 봤다.

하지만 actual disruption:
- MyFitnessPal
- free calorie apps
- activity monitors

가 paid category의 willingness-to-pay를 바꾸고 있었다.

2014 stock은 mid-$20s까지 약화.

### 실패식
**low historical FCF multiple × shrinking FCF duration**

---

## 13. WTW 2013-09 Long — market share moat의 함정

원문:
- US share ~43%
- online = crown jewel
- buy <= $37
- fair value $48~60
- debt를 loose covenants / low amortization 때문에 quasi-asset처럼 해석

실제:
2013-10 earnings shock:
- revenue -8.5%
- net income -10.5%
- EPS -11.2%
- dividend suspended

2014-02:
- revenue ~-11%
- attendance ~-14%
- stock ~$22.70

### 가장 큰 오류
**43% share가 있어도 relevant market 자체가 paid diet program에서 free digital self-service로 재정의되면 share moat가 무의미해진다.**

---

## 14. WTW 2014 Short — fundamental thesis는 좋았지만 borrow economics가 문제

원문:
- ~6x earnings인데도 Short
- meetings 70% revenue
- online 30%
- online ~$19/month vs free apps
- internet revenue -5.3%
- debt ~$2.2bn
- meetings -5%, internet -50% stress 시 interest coverage 위험
- borrow **50~60%**

실제:
- 2014 추가 약세
- 2015 pre-Oprah low ~$3.78
- 2015 Oprah partnership 후 폭발적 반등

### 판정
**Fundamental thesis: 강한 성공**
**Trade economics: 매우 위험**

50% borrow면 stock이 50% 하락해도 1년 holding의 gross gain이 거의 사라질 수 있다.

---

## 15. WTW 2008→2014 비교

| 시점 | 방향 | 무엇을 봤나 | 판정 |
|---|---|---|---|
| 2008 | Short | recession + attendance + leverage | 성공 |
| 2013-03 | Long | cheap FCF + temporary issue | 실패 |
| 2013-09 | Long | market share + online jewel | 실패 |
| 2014 | Short | meetings + online 동시 disruption | fundamental 성공 |

### 핵심 변화
2008 문제는 **cycle**.
2013~14 문제는 **category structure**.

이 둘을 구분해야 한다.

---

# PART C — Cross-Case Lessons

## 16. STMP와 WTW는 digital disruption을 반대로 보여준다

### STMP
old category:
mail/postage

새 category:
e-commerce shipping software

→ incumbent가 **digital transition의 수혜자**.

### WTW
old category:
paid meetings / paid online diet program

새 category:
free apps / digital self-service

→ incumbent가 **digital transition의 피해자**.

따라서 “digital disruption”이라는 말만으로 Long/Short가 결정되지 않는다.

질문은:
**새 value chain에서 이 회사가 customer relationship을 더 강하게 가지는가, 아니면 customer가 회사를 우회하는가?**

---

## 17. 가장 중요한 비교

### STMP 2016 Short
무료/저가 경쟁과 postal decline을 봤지만
회사가 adjacent shipping value chain을 장악.

### WTW 2013 Long
brand와 market share를 봤지만
consumer가 free tools로 기존 value chain을 우회.

### 차이
STMP는 digital transition이 **distribution/software attach를 강화**.
WTW는 digital transition이 **intermediation을 제거**.

---

## 18. BATCH 56 재사용 체크리스트 20개

1. raw direction은 원문으로 확인한다.
2. ticker reuse는 가격성과 DB를 오염시킬 수 있다.
3. performance series의 entity continuity를 검증한다.
4. LTV/CAC와 customer growth를 분리한다.
5. marketing growth capex는 cohort payback으로 검증한다.
6. NOL은 value이지 price floor가 아니다.
7. 같은 회사 재매수는 expectations reset 여부를 본다.
8. declining legacy category와 company TAM을 구분한다.
9. M&A masking과 strategic category consolidation을 구분한다.
10. contract-risk Short는 exact renewal catalyst가 필요하다.
11. eventual event로 early Short를 성공 처리하지 않는다.
12. platform moat와 supplier dependency를 동시에 본다.
13. guidance shock 뒤에는 broken earnings를 0으로 둔 SOTP를 만든다.
14. subscription asset은 ARR/churn/ARPU로 standalone valuation한다.
15. debt-funded buyback 뒤 downturn을 stress한다.
16. market share는 relevant market definition이 유지되는지 본다.
17. $0 substitute는 historical FCF duration을 줄일 수 있다.
18. brand moat와 acquisition moat를 구분한다.
19. Short IRR은 borrow cost를 차감한다.
20. fundamental correctness와 tradeability를 별도 score로 저장한다.

---

## 19. Batch 056 핵심 문장

> **디지털 전환의 승패는 ‘온라인이 커지는가’가 아니라 고객이 기존 회사를 더 많이 통과하게 되는지, 아예 우회하게 되는지에 달려 있다. Stamps.com은 shipping workflow를 장악했고, Weight Watchers는 무료 앱에 customer relationship 일부를 빼앗겼다.**

---

## 20. 앱 / DB 반영

- Wrapper: `analysis/batch_056_stmp_wtw_10.md`
- Overlay: `data/curated/batch_056_stmp_wtw_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
