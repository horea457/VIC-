# American Home Mortgage (AHM) — 2007-03-15 VIC Long

> **Idea unit:** American Home Mortgage common equity Long.  
> **Research as-of:** 2026-09-20. Source SQL `is_short=true`, but original text calls AHM **“the baby thrown out with the subprime bath water”** and argues for ~40% upside; corrected to Long.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | American Home Mortgage Investment Corp. / AHM |
| VIC 게시일 / 작성자 | 2007-03-15 / david101 |
| 실제 방향 | **Long** |
| implied price | 약 **$24** (1.07x BV $22.64) |
| tangible book | 약 **$20** |
| forward dividend | **$1.12/quarter**, stated yield ~18.5% |
| portfolio subprime | **0.3%** |
| Alt-A | **18.2%** |
| weighted FICO / LTV | **710 / 75%** |
| stated upside | **~40% + dividend** |
| terminal event | Chapter 11 **2007-08-06**, less than five months later |
| 최종 판정 | **완전한 실패 — credit quality를 봤지만 funding liquidity를 equity margin-of-safety로 착각** |

> **결론:** 이 아이디어의 가장 큰 오류는 “AHM은 subprime이 아니다”를 “AHM은 안전하다”로 바꾼 것이다. mortgage originator의 terminal risk는 borrower credit loss가 발생하기 전에 **warehouse/repo/commercial-paper funding이 닫혀 inventory를 fund하지 못하는 것**일 수 있다. 원문은 liquidity를 핵심 질문으로 제기했지만, 다양한 credit lines와 AAA MBS를 보고 위험을 과소평가했다. 5개월도 안 돼 AHM은 Chapter 11에 들어갔다.

---

## 1. 원문 투자논지

작성자는 subprime lenders와 AHM을 구분했다.

- subprime loans 0.3%
- Alt-A 18.2%
- weighted FICO 710
- LTV 75%
- book value $22.64 / tangible book ~$20
- forward dividend yield 18.5%
- stock 1.07x book

따라서 시장이 subprime contagion으로 prime/Alt-A lender까지 indiscriminately 팔았다고 봤다.

---

## 2. 원문이 liquidity를 보긴 봤다

흥미롭게도 글은 첫 핵심 질문을 **liquidity**라고 했다.

다양한 funding facilities를 나열했다.
- structured notes commercial paper
- UBS, Bear Stearns facilities
- Bank of America syndicated facility
- JPMorgan, IXIS, CSFB, Barclays, Calyon 등
- reverse repurchase agreements

문제는 “facility가 많다”를 “funding이 diversified and durable하다”로 해석했다는 점이다.

실제로 stress에서는 여러 lender가 서로 독립적이지 않다. 같은 collateral marks, repo haircuts, securitization market, short-term confidence에 노출된다.

---

## 3. 2005 Short와 정반대의 증거 가중치

### 2005 Short가 본 것
- cash earnings 부족
- dividend funding dependence
- model-dependent gains
- wholesale funding fragility

### 2007 Long이 본 것
- 좋은 FICO/LTV
- 낮은 subprime share
- book-value discount
- 높은 dividend yield
- 많은 funding counterparties

2007 long은 **asset quality**를 더 강한 evidence로 두었고, 2005 short는 **liability/funding structure**를 더 강한 evidence로 뒀다.

mortgage lender crisis에서는 후자가 결정적이었다.

---

## 4. 왜 book value와 dividend yield가 margin of safety가 아니었나

금융사의 book value는 assets를 계속 funding할 수 있을 때 의미가 있다.

**Equity survival condition = collateral liquidity + funding rollover capacity > margin calls + cash operating needs**

이 조건이 깨지면:
- asset sale discount 확대
- collateral marks 하락
- 추가 margin call
- forced deleveraging

이라는 feedback loop가 생긴다.

18.5% dividend yield는 upside가 아니라 시장이 funding discontinuity를 가격에 넣기 시작한 signal이었다.

---

## 5. 실제 결과

2007년 여름 mortgage funding market이 급속히 악화됐고 AHM은 영업자금을 확보하지 못했다. 회사 및 계열사는 **2007-08-06 Chapter 11**을 신청했다.

게시일 2007-03-15에서 약 4개월 3주 만이다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Direction metadata | raw Short → **Long correction** |
| Borrower-credit differentiation | 맞음, 그러나 비본질적 |
| Liquidity assessment | 매우 강한 실패 |
| Book-value margin of safety | 실패 |
| Dividend thesis | 실패 |
| Security outcome | **catastrophic failure** |
| Thesis score | **0.5/10** |
| Process score | **10/10** |

### 한 문장 교훈

> **레버리지 금융사에서 asset quality가 좋아도 liability duration과 collateral liquidity가 나쁘면 equity는 0이 될 수 있다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2007-03-15.
2. Bankruptcy filing, 2007-08-06: https://www.sec.gov/Archives/edgar/data/1400122/000114420407041333/v083645_8k.htm
3. Related filing: https://www.sec.gov/Archives/edgar/data/1406223/000114420407041223/v083526_8k.htm

### 데이터 품질
- T0 thesis: **A**
- bankruptcy date/outcome: **A**
- implied entry: **A-**, derived directly from write-up's 1.07x book value $22.64
