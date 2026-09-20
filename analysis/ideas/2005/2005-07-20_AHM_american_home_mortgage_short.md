# American Home Mortgage (AHM) — 2005-07-20 VIC Short

> **Idea unit:** American Home Mortgage common equity Short.  
> **Research as-of:** 2026-09-20. Source SQL `is_short=true`; actual direction is Short.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | American Home Mortgage Investment Corp. / AHM |
| VIC 게시일 / 작성자 | 2005-07-20 / dkepesh935 |
| 실제 방향 | **Short** |
| stated valuation | **1.9x** Q2 stated BV $20.21; dividend yield **8.7%** |
| core thesis | reported gain-on-sale / REIT taxable income ≠ distributable cash; dividends depend on external capital and wholesale funding |
| critical accounting issue | self-sponsored securitization economics and convexity/prepayment assumptions |
| terminal event | Chapter 11 filed **2007-08-06** |
| 최종 판정 | **매우 강한 성공 — cash-flow/accounting critique identified the exact fragility that later became fatal** |

> **결론:** 2005 AHM short의 가장 강한 부분은 “housing will crash”가 아니다. **회계상 earnings와 실제 cash generation을 분리하고, 현금배당을 내부적으로 만들지 못하는 originating mortgage REIT가 wholesale funding과 equity issuance에 의존한다**는 구조를 봤다. 2년 뒤 liquidity window가 닫히자 AHM은 Chapter 11에 들어갔다. 결과뿐 아니라 causal mechanism까지 맞은 rare short다.

---

## 1. 원문 핵심 논지

작성자는 당시 시장이 earnings, dividend yield, book value만 보며 cash flow를 무시한다고 주장했다.

핵심 질문은:

> **“이 회사는 배당금을 실제 현금으로 벌고 있는가?”**

였다.

AHM은 REIT taxable income의 90% 이상을 배당해야 하지만, 원문은 internal cash generation이 부족하고 equity capital raising이 dividend funding에 기여한다고 봤다.

---

## 2. 회계 메커니즘

AHM은 loans를 securitize하고, sponsored QSPE가 만든 securities 일부를 다시 보유하면서 gain-on-sale을 인식했다.

작성자는 이 과정에서:
- cash가 실제로 유입되는가,
- IO strip / mortgage security의 prepayment convexity를 적절히 amortize하는가,
- origination cost와 servicing/credit enhancement cost가 충분히 반영되는가

를 문제 삼았다.

즉 **income statement profit → cash dividend capacity** 연결고리가 약하다는 지적이다.

---

## 3. 왜 2007에 이 구조가 폭발했나

originating mortgage REIT는:

**short-duration wholesale liabilities → mortgage inventory / MBS assets**

라는 구조를 가진다.

평소에는 repo, warehouse, commercial paper가 rollover되지만, lenders가 haircuts를 높이거나 collateral value를 낮추면 equity가 충분해도 즉시 cash shortage가 날 수 있다.

AHM은 2007년 여름 funding crisis 후 영업을 중단했고 **2007-08-06 Chapter 11**을 신청했다.

---

## 4. Short thesis에서 특히 좋았던 점

### ① Valuation short가 아니라 funding-model short
8x earnings / 8.7% dividend yield만 보면 싸 보였다. 원문은 “earnings가 현금인가”를 먼저 물었다.

### ② terminal liquidity risk를 balance-sheet identity로 설명
이건 housing-price forecast 없이도 성립하는 thesis였다.

### ③ dividend를 evidence가 아니라 liability로 봄
현금이 부족한 REIT의 높은 dividend는 안전신호가 아니라 **외부자금 의존도를 높이는 constraint**일 수 있다.

---

## 5. 재사용 가능한 Financial Short 식

**Cash dividend coverage = recurring cash earnings / cash dividends paid**

**Funding fragility = short-term wholesale funding / immediately monetizable unencumbered assets**

**Reported ROE quality = cash ROE - gains dependent on model assumptions / securitization marks**

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Direction | Short, metadata correct |
| Cash-flow thesis | 매우 성공 |
| Accounting-quality thesis | 매우 성공 |
| Funding-risk thesis | 매우 성공 |
| Terminal security outcome | 매우 강한 성공 |
| Thesis score | **10/10** |
| Process score | **10/10** |

### 한 문장 교훈

> **금융사의 높은 배당과 낮은 P/E는 현금창출이 아니라 funding window가 열려 있어서 유지되는 것일 수 있다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2005-07-20.
2. American Home Mortgage bankruptcy filing confirmation / SEC-related filing: https://www.sec.gov/Archives/edgar/data/1400122/000114420407041333/v083645_8k.htm
3. Additional bankruptcy confirmation: https://www.sec.gov/Archives/edgar/data/1406223/000114420407041223/v083526_8k.htm

### 데이터 품질
- T0 thesis: **A**
- bankruptcy event/date: **A**
- causal linkage: **A-/B+**, consistent with funding-collapse chronology and original balance-sheet mechanism
