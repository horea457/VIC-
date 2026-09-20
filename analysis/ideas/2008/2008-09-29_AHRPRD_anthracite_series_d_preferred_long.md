# Anthracite Capital Series D Preferred (AHRPRD) — 2008-09-29 VIC Long

> **Idea unit:** 2008-09-29 Anthracite Capital Series D cumulative preferred Long.
> **Research as-of:** 2026-09-20. 원 SQL은 Short지만 원문은 명백한 **preferred Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer | Anthracite Capital |
| Security | **Series D cumulative preferred** |
| VIC 게시일 / 작성자 | 2008-09-29 / bowd57 |
| 실제 방향 | Preferred Long |
| 원 SQL 방향 | **Short — 오류** |
| entry | 약 **38% of $25 par ≈ $9.50** |
| coupon | **8.25%** |
| current yield | **20%+** |
| author upside | could **double** if credit markets normalize |
| thesis | CRE fundamentals better than market prices; interest/dividend coverage adequate |
| terminal event | **2010 Chapter 7** |
| 최종 판정 | **catastrophic failure — apparent 20% yield was compensation for terminal funding risk** |

> **결론:** 2008 vintage는 2007보다 더 싸졌다. Series D는 par의 약 38%에서 거래됐고 current yield는 20%를 넘었다. 작성자는 CMBS가 지나치게 싸고 AHR의 interest/preferred-dividend coverage가 아직 충분하다고 봤다. 하지만 “싸진 가격”은 risk가 제거됐다는 뜻이 아니었다. 2009 말 securities는 suspended/delisted됐고 2010 Chapter 7에 들어갔다. **2007 thesis의 averaging-down 버전이었지만 terminal outcome은 동일했다.**

---

## 1. 원문 투자논지

원문은:
- super-senior CMBS spread가 과도
- CRE delinquency 아직 낮음
- adjusted NII로 debt interest coverage 약 2.14x
- preferred/TRuPS 포함 coverage 약 1.67x
- long-term CDO cash flows가 preferred claim을 지지

한다고 봤다.

---

## 2. 무엇이 잘못됐나

Coverage ratio는 **static income statement**였다.

위기에서 문제는:
- collateral marks
- financing withdrawal
- repo haircuts
- trapped CDO cash
- asset-sale liquidity
- counterparty behavior

였다.

즉:

**current interest coverage ≠ liquidity survival probability**

다.

---

## 3. 실제 경로

| 시점 | 사건 |
|---|---|
| 2008-09-29 | Long @ ~38% par |
| 2008 Q4~2009 | CMBS liquidity/funding stress intensifies |
| 2009-12 | NYSE suspension/delisting |
| 2010-03 | Chapter 7 |

---

## 4. 2007 vs 2008 Vintage

| 구분 | 2007 | 2008 |
|---|---:|---:|
| entry | $13.67 | ~$9.50 |
| yield | ~15% | >20% |
| stated margin of safety | equity cushion | income/asset cash-flow coverage |
| terminal outcome | Chapter 7 | Chapter 7 |

낮은 가격이 recovery waterfall 자체를 바꾸지 못했다.

---

## 5. 재사용 가능한 교훈

1. distressed preferred의 yield는 expected return이 아니라 distress signal일 수 있다.
2. static coverage ratio에 liquidity haircut을 적용한다.
3. CDO cash flow가 structurally trapped되는지 확인한다.
4. averaging down은 thesis error가 아닌 price error일 때만 유효하다.
5. terminal recovery가 0이면 coupon carry는 장기 결과를 구하지 못한다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Cheapness | 매우 싸 보였음 |
| Coverage analysis | 불충분 |
| Liquidity thesis | 실패 |
| Terminal recovery | 사실상 전손 |
| Thesis score | 0.3/10 |
| Process score | 9.9/10 |
| 종합 | **catastrophic failure — 20%+ yield trap** |

### 한 문장 교훈

> **20% yield가 좋은 수익률인지, 시장이 bankruptcy probability를 가격에 넣은 것인지 먼저 구분해야 한다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2008-09-29.
2. Anthracite 2009 NYSE suspension/no-value assessment: https://www.sec.gov/Archives/edgar/data/1050112/000134100409002401/anthracite_8k.htm
3. Chapter 7: https://www.sec.gov/Archives/edgar/data/1050112/000134100410000503/form_8k.htm

### 데이터 품질
- T0 thesis: **A**
- terminal outcome: **A**
