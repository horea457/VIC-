# Batch 073 — AGNC / AGNT / AGO / AGP V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 072 마지막 **AGN.PA 2016-02-19** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **3건(AGNC 2020, AGO 2011, AGO 2021)**. AGO 2014는 단순 Long이 아니라 **Long AGO / Short MBI pair trade**로 strategy type을 교정했다. Source SQL performance row는 AGO 2005/2008/2009/2011/2014/2021 총 6건에 존재하지만, **AGO 2014 row는 long leg만 측정하므로 pair return으로 사용하지 않는다.**

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 전략 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2020-04-17 | AGNC | **Short** | **AGNC Common Long** | [AGNC 2020](ideas/2020/2020-04-17_AGNC_long.md) | **강한 성공 — Fed backstop + TBV 회복 + dividend** |
| 2 | 2022-06-15 | AGNC US | Short | **AGNC Common Short** | [AGNC 2022](ideas/2022/2022-06-15_AGNC_US_short.md) | **강한 성공 — spread widening / TBV destruction 적중** |
| 3 | 2005-05-09 | AGNT | Long | **Argonaut Technologies Liquidation Long** | [AGNT](ideas/2005/2005-05-09_AGNT_argonaut_technologies_liquidation_long.md) | **부분/강한 성공 — $0.70 first distribution 실현, final recovery 미확정** |
| 4 | 2005-04-20 | AGO | Long | **Assured Guaranty Common Long** | [AGO 2005](ideas/2005/2005-04-20_AGO_long.md) | **중기 강한 성공 — 2Y +49.6%** |
| 5 | 2008-01-18 | AGO | Long | **Assured Guaranty Common Long** | [AGO 2008](ideas/2008/2008-01-18_AGO_long.md) | **fundamental survival 적중 / entry timing 실패** |
| 6 | 2009-11-16 | AGO | Long | **Assured Guaranty Common Long** | [AGO 2009](ideas/2009/2009-11-16_AGO_long.md) | **실패 — FSA는 맞고 normalized EPS가 과대** |
| 7 | 2011-04-15 | AGO | **Short** | **Assured Guaranty Common Long** | [AGO 2011](ideas/2011/2011-04-15_AGO_long.md) | **장기 성공 — R&W settlement / 5Y +59.7%** |
| 8 | 2014-12-10 | AGO | Long | **Long AGO / Short MBI Pair Trade** | [AGO/MBI Pair](ideas/2014/2014-12-10_AGO_MBI_pair_long_short.md) | **강한 성공 — rough 1Y gross pair +33~34%** |
| 9 | 2021-12-27 | AGO | **Short** | **Assured Guaranty Common Long** | [AGO 2021](ideas/2021/2021-12-27_AGO_long.md) | **fundamental 성공 / P/B rerating 실패** |
| 10 | 2008-12-29 | AGP | Long | **Amerigroup Common Long** | [Amerigroup](ideas/2008/2008-12-29_AGP_amerigroup_long.md) | **매우 강한 성공 — ~$29.5→$92 cash, ~3.1x** |

---

# PART A — AGNC 2020 vs 2022: 같은 Agency mREIT, 반대 Regime에서 둘 다 맞다

## 2. 2020 Long

2020-04 entry:
- stock ~**$12.15**
- 3/31 TBVPS **$13.62**
- monthly dividend **$0.12**
- Fed agency-MBS buying
- post-forced-deleveraging balance sheet

실제:
- 12/31/20 TBVPS **$16.71**
- 2021-04 price ~**$17.34**
- 약 12개월 dividends **$1.44**

대략:

**price-only +42.7%**

**price + simple dividends ≈ +54.6%**

## 3. 2022 Short

2022-06:
- stock ~$10~11
- ~0.8x book
- leverage ~7.5x
- QT / hikes / MBS-spread widening

실제 FY2022:
- TBVPS **$15.75→$9.84 (-37.5%)**
- economic return on TCE **-28.4%**
- total stock return **-21.7%**
- Oct stock $7~8 area

### 두 vintage 비교

| 구분 | 2020 | 2022 |
|---|---|---|
| Fed regime | MBS buyer / backstop | tightening / QT |
| trade | Long | Short |
| core variable | liquidation finished / TBV recovery | spread widening / TBV loss |
| result | 강한 성공 | 강한 성공 |

> **Agency guarantee는 mortgage principal을 보호하지 mREIT common의 book value를 보호하지 않는다.**

---

# PART B — AGNT 2005: liquidation은 “추정 가치”보다 실제 분배 시점이 중요하다

## 4. Argonaut Technologies

원문:
- implied purchase price 약 **$0.91**
- liquidation range **$0.98~1.10**
- first distribution **$0.70**
- expected return **8~20%**

실제:
- 2005-06-01 Biotage asset sale approved
- 2005-07 **$0.70/share** first distribution
- company estimated another **$0.28~0.32**
- 2005-07-08 Nasdaq delisting

첫 catalyst는 정확히 실현됐다. 다만 deregistration 이후 **최종 모든 분배 cash flow를 공개자료로 완전히 복원할 수 없어 exact IRR은 유보**했다.

> **Liquidation thesis에서 management estimate를 realized cash로 바꾸어 쓰면 안 된다.**

---

# PART C — AGO 2005~2021: 같은 franchise가 여섯 개의 다른 투자였다

## 5. 2005 Long — book growth / rerating 성공

원문:
- **0.88x book**
- **8.9x 2005E EPS**
- primary-insurance expansion
- rating upside

실제:
- BVPS 2005 **$22.22** → 2006 **$24.44**
- ABVPS **$30.39→$36.57**
- SQL 1Y **+35.5%**
- 2Y **+49.6%**
- 5Y **+24.2%**

중기 thesis는 강하게 성공했지만 2008 crisis가 장기 return을 일부 지웠다.

---

## 6. 2008 Long — 회사 선택은 맞고 시점은 틀렸다

원문:
- AGO는 ABK/MBI보다 RMBS/CDO exposure가 작음
- rating survival
- new-business share gain
- EPS $5+
- target $50~60

실제:
- AGO는 실제로 industry survivor가 됐고 2009 FSA를 인수
- 그러나 SQL 1Y **-54.5%**
- 2Y **+35.9%**
- 5Y **-12.2%**

### 교훈

**relative winner ≠ good absolute Long at any price/date**

---

## 7. 2009 Long — FSA는 맞았고 $7.22 EPS는 틀렸다

원문:
- FSA acquisition
- “no-loss” quarterly run-rate annualization
- normalized op EPS **~$7.22**
- target **$50**

실제 operating EPS:
- 2009 **$2.15**
- 2010 **$3.46**
- 2011 **$3.24**

SQL:
- 1Y **-32.3%**
- 2Y **-57.3%**
- 3Y **-46.6%**
- 5Y **+7.7%**

### 핵심

> **좋은 M&A thesis를 잘못된 normalized denominator가 망칠 수 있다.**

---

## 8. 2011 Long — R&W recovery가 실제 현금이 되다

raw SQL은 Short지만 original은 명백한 Long.

원문:
- ~4.8x earnings
- 0.82x book
- 0.34x adjusted book
- mortgage R&W recovery optionality

실제 Bank of America settlement:
- cash **~$1.1bn**
- expected-value loss-sharing reinsurance **~$470m**
- 29 RMBS transactions

SQL:
- 1Y **-13.6%**
- 2Y **+16.6%**
- 3Y **+44.7%**
- 5Y **+59.7%**

fundamental catalyst는 강하게 맞았지만 rerating은 느렸다.

---

## 9. 2014 Pair — SQL standalone return으로 평가하면 틀린다

실제 전략:

**Long AGO / Short MBI**

대략 Dec-2014→Dec-2015:
- AGO **$25.99→$26.43**, +1.7%
- MBI **$9.54→$6.48**, short gain +32.1%

equal-dollar gross pair 약 **+33~34%**.

SQL AGO-only row 1Y -3.9%는 **pair-return 측정치가 아니다.**

### 핵심

> **Pair trade에서는 ticker 하나의 성과가 아니라 두 leg의 spread를 본다.**

---

## 10. 2021 Long — 분자는 맞고 P/B가 틀렸다

raw SQL은 Short지만 original:
**“AGO – Long Thesis $48”**

원문 2023:
- GAAP BVPS **$108**
- ABVPS **$150**
- target **$96 @0.9x GAAP**
- bull **$135 @0.9x ABV**

실제 2023:
- GAAP equity/share **$101.63**
- ABV/share **$155.92**
- YE stock **~$71.89**

즉 **book-value denominator forecast는 거의 완벽**했다.

하지만 0.9x multiple rerating은 오지 않았다.

SQL 1Y return은 **+28.7%**로 투자 자체는 나쁘지 않았지만 목표가에는 크게 미달했다.

> **분자를 맞혀도 배수를 틀리면 목표주가는 틀린다.**

---

# PART D — AGO vintages를 한 표로 보면

| Vintage | 핵심 thesis | 무엇이 맞았나 | 무엇이 틀렸나 | 결과 |
|---|---|---|---|---|
| 2005 | book / primary growth | BV·ABV 성장 | tail durability | 중기 성공 |
| 2008 | relative survivor | AGO 생존 / FSA | entry timing | 혼합·실패 |
| 2009 | FSA + normalized EPS | FSA | $7.22 EPS / rerating | 실패 |
| 2011 | R&W recovery | BofA $1.1bn+ | speed | 장기 성공 |
| 2014 | AGO>MBI pair | relative quality | — | 강한 성공 |
| 2021 | BV compounding + 0.9x | BV/ABV 거의 적중 | P/B normalization | fundamental 성공 / target 실패 |

### 공통 인사이트

AGO는 장기간:
- adjusted book compounding,
- legacy loss resolution,
- accretive buybacks,
- public-finance franchise

가 실제로 작동했다.

하지만 **언제 어떤 multiple로 시장이 인정하느냐는 별개의 문제**였다.

---

# PART E — Amerigroup 2008: 경기침체 자체가 수요와 Outsourcing을 동시에 늘리다

## 11. 2008 Long

entry reference:
- 12/31/08 close **$29.52**

원문:
- recession → Medicaid eligibles 증가
- state fiscal stress → managed-care outsourcing 필요 증가
- federal matching support
- SCHIP expansion
- high-cost populations의 managed-care penetration upside

실제 2009:
- membership **~1.8m, +13.2%**
- EPS **~$2.85**
- guidance raised during year

2012:
- WellPoint **$92 cash/share** acquisition
- completed 2012-12-24

price multiple:

**$92 / $29.52 ≈ 3.12x**

### 핵심

이건 단순 defensive healthcare가 아니라:

**unemployment ↑ → eligibility ↑**

그리고

**state tax revenue ↓ → outsourcing incentive ↑**

가 동시에 작동하는 countercyclical feedback loop였다.

---

# PART F — Batch 073 공통 분석식

### mREIT

**Common equity sensitivity ≈ asset spread/duration shock × leverage + funding effects - hedges**

### Liquidation

**Realized return = Σ actual cash distributions / purchase price - 1**

### Financial Guarantor

**Per-share value = GAAP/adjusted book growth + capital return ± legacy claim development**

### Pair Trade

**Pair return = Long return - Short return - borrow/dividend/financing effects**

### Medicaid MCO

**Earnings growth = membership growth × premium yield × normalized medical margin + scale effects**

---

# PART G — Batch 073 재사용 체크리스트

1. mREIT에서 agency guarantee와 common-book protection을 혼동하지 않는다.
2. Fed reaction function이 달라지면 같은 company의 Long/Short가 바뀔 수 있다.
3. liquidation estimate와 actual distributions를 분리한다.
4. final distribution이 불완전하면 exact IRR을 만들지 않는다.
5. insurer normalized EPS는 한 분기를 annualize하지 않는다.
6. crisis survivor thesis와 entry timing을 별도로 score한다.
7. R&W recoveries는 gross loss에서 별도 asset으로 본다.
8. pair trade는 standalone ticker return으로 평가하지 않는다.
9. denominator forecast와 valuation multiple hypothesis를 분리한다.
10. deep-P/B buyback은 per-share book compounding을 직접 계산한다.
11. policy-driven healthcare는 enrollment과 state/federal incentives를 동시에 본다.
12. corporate cash takeout은 가장 강한 terminal payoff anchor다.

---

## 12. Batch 073 핵심 한 줄

> **이번 배치는 동일 자산도 regime·claim·valuation layer가 달라지면 정반대 투자로 바뀐다는 사례다. AGNC는 2020 Long·2022 Short가 모두 맞았고, AGO는 book value를 맞혀도 timing·normalized EPS·P/B 가정에 따라 여섯 번의 결과가 갈렸다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_073_agnc_agnt_ago_agp_10.md`
- Overlay: `data/curated/batch_073_agnc_agnt_ago_agp_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
