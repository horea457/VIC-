# Batch 071 — AGC / AGC1 / AGCO / Argentex / Agrify / AGI V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 070 마지막 **AGA CN 2003-02-28** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **3건(AGC 2016, AGC1 2009, AGI 2000)**. AGC1 2009·2012는 common equity가 아니라 **senior unsecured debt**다. AGI 2000은 SQL상 Alamos Gold로 잘못 매핑돼 있으나 실제 회사는 **Alliance Gaming Corporation**이다. SQL performance row는 AGCO 2015와 Alamos Gold 2014에만 유효하게 존재했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2016-01-17 | AGC | **Short** | **Advent Claymore CEF Common Long** | [AGC](ideas/2016/2016-01-17_AGC_closed_end_fund_long.md) | **강한 성공 — discount narrowing + tender + NAV merger** |
| 2 | 2009-01-22 | AGC1 | **Short** | **American General Finance Senior Unsecured Bonds Long** | [AGF Bonds](ideas/2009/2009-01-22_AGC1_american_general_finance_bonds_long.md) | **강한 성공 — panic credit survived/refinanced** |
| 3 | 2012-11-22 | AGC1 | Long | **Springleaf 6.90% 2017 Notes Long** | [Springleaf Notes](ideas/2012/2012-11-22_AGC1_springleaf_6_90_2017_notes_long.md) | **매우 강한 성공 — exchange/repurchase/par path** |
| 4 | 2015-10-16 | AGCO | Long | **AGCO Common Long** | [AGCO 2015](ideas/2015/2015-10-16_AGCO_long.md) | **강한 주가 성공 / margin bull case 미달** |
| 5 | 2021-11-06 | AGFX | Long | **Argentex Common Long** | [Argentex](ideas/2021/2021-11-06_AGFX_argentex_long.md) | **매우 강한 실패 — 88p→2.49p liquidity collapse** |
| 6 | 2021-05-28 | AGFY | Long | **Agrify Common Long** | [Agrify 2021](ideas/2021/2021-05-28_AGFY_long.md) | **매우 강한 실패 — TTK/VFU economics 붕괴** |
| 7 | 2022-02-21 | AGFY | Long | **Agrify Common Long** | [Agrify 2022](ideas/2022/2022-02-21_AGFY_long.md) | **매우 강한 실패 — lower price did not fix broken model** |
| 8 | 2000-08-29 | AGI | **Short** | **Alliance Gaming Common Long** | [Alliance Gaming](ideas/2000/2000-08-29_AGI_alliance_gaming_long.md) | **장기 매우 강한 성공 — Bally→$83.30 cash** |
| 9 | 2014-03-31 | AGI | Long | **Alamos Gold Common Long** | [Alamos 2014](ideas/2014/2014-03-31_AGI_alamos_gold_long.md) | **실패 — Turkey/timing thesis 미실현** |
| 10 | 2018-11-18 | AGI. | Long | **Alamos Gold Common Long** | [Alamos 2018](ideas/2018/2018-11-18_AGI_alamos_gold_long.md) | **매우 강한 성공 — operating fix + gold beta** |

---

# PART A — AGC: CEF 할인은 underlying asset보다 별도의 return source다

## 2. 2016 Advent Claymore Long

원문:
- NAV discount **~18.95%**
- monthly distribution **$0.047**
- distribution yield 약 **11.4%**
- assets mostly Level 1/2
- leverage substantial
- activist/tender optionality

실제:
- FY2016 market return +6.68% vs NAV -0.65%
- FY2017 market return +21.79% vs NAV +14.03%
- FY2017 말 discount 약 **8%**
- 2017 15% tender offer
- 2018 AVK와 **NAV-for-NAV merger**

### 핵심

CEF total return은:

**NAV return + discount change + distributions - leverage/expense drag**

로 분해해야 한다.

이번에는 underlying NAV 상승뿐 아니라 **discount 자체가 약 19%→8%로 닫힌 것**이 중요했다.

---

# PART B — AGC1 두 번: 2009 panic credit와 2012 normalizing credit

## 3. American General Finance 2009

원문:
- senior unsecured bonds
- 2011~12 maturities
- 가격 **50~60c**
- held-to-maturity IRR **35~45%**
- no large secured layer ahead
- AIG/strategic support 가능성

실제:
- 2010 Fortress가 AGF 80% 인수
- company renamed Springleaf
- near-term senior unsecured claims survived/refinanced

정확 CUSIP가 원문에 완전 보존되지 않아 exact IRR은 만들지 않는다.

## 4. Springleaf 2012

추천 security:
- **6.90% Medium-Term Notes due 2017**
- price ~**87**
- YTM ~**10%**

실제:
- 2013 $700m principal exchange into 2021/2023 notes
- 약 $184m cash repurchase 계획
- 2017 약 $466m additional repurchase
- remaining 2017 notes maturity repayment

### 두 아이디어의 차이

| 항목 | 2009 | 2012 |
|---|---|---|
| 상태 | panic / survival | normalization |
| 가격 | 50~60c | ~87 |
| alpha | recovery probability | spread tightening + pull-to-par |
| catalyst | strategic buyer | refinancing/capital markets |
| 결과 | 강한 성공 | 매우 강한 성공 |

> **Credit에서는 같은 issuer라도 survival 단계와 normalization 단계의 expected return source가 다르다.**

---

# PART C — AGCO 2015: peak earnings를 틀려도 trough를 맞히면 돈을 벌 수 있다

## 5. 2015 Long

entry:
- price ~$44
- EV ~$4.85bn
- multi-year ag-equipment downturn

원문 bull:
- 2018/19 sales **$10bn**
- op margin **10%**
- EPS **$7.25**

실제:
- 2018 sales **$9.352bn**
- 2019 sales **$9.041bn**
- 2018 operating income **$489m**, margin 약 5.2%

즉 margin forecast는 크게 과대였다.

그런데 SQL security performance:
- 1Y **+18.4%**
- 2Y **+66.7%**
- 5Y **+92.3%**

### 핵심

> **Cyclical Long은 peak earnings의 높이를 정확히 맞히지 않아도, 현재 earnings가 trough라는 방향을 맞히면 강한 수익이 가능하다.**

---

# PART D — Argentex: capital-light와 liquidity-light는 다르다

## 6. 2021 Long

entry:
- **88p**
- market cap ~£100m
- free cash ~£20m
- EV ~£80m
- 2022E ~7x EV/EBITDA
- FCF yield ~10%

원문은:
- high-margin FX broker
- low capex
- insider ownership >30%
- rising-rate benefit
- tech platform option

을 봤다.

그러나 risk section에는 이미 **client default / collateral margin call**이 있었다.

실제 2025:
- rapid FX moves
- £20m+ margin calls
- shares suspended
- emergency bridge financing
- IFX recommended cash acquisition **2.49p/share**

**2.49 / 88 - 1 ≈ -97.2%**

### 핵심

> **고정자산이 적다고 필요한 자본이 적은 것은 아니다. derivatives broker는 stress liquidity가 진짜 capital requirement다.**

---

# PART E — Agrify: “현금이 많고 싸다”는 broken unit economics를 못 고친다

## 7. 2021 Long

entry:
- $9.26
- market cap ~$213m
- cash ~$138m
- EV ~$76m

원문:
- VFU hardware
- TTK customer financing
- software
- 10-year fee stream

실제:
- 2021 revenue **$59.9m**
- 2022 revenue **$58.3m**
- 2022 gross loss **-$31.8m**
- operating loss **-$193.3m**
- impairment **$69.9m**

## 8. 2022 Long

entry ~$6, net cash ~$4/share.

원문 2024 bridge:
- TTK EBITDA **$56m**
- software EBITDA **$27m**
- total base **$83m**
- target **$55/share**

실제는 위와 같이 business economics가 즉시 악화됐다.

### 누적 capital destruction signals

- 2022 reverse split **1:10**
- 2023 **1:20**
- 2024 **1:15**
- cumulative **1:3,000**
- 2024 Green Thumb secured convertible financing
- legacy cultivation business sale

### 핵심

> **Net cash는 future burn과 customer financing commitments를 빼기 전에는 downside floor가 아니다.**

---

# PART F — AGI mapping: 같은 ticker에 완전히 다른 두 회사

## 9. AGI 2000 = Alliance Gaming, not Alamos

SQL company table은 AGI를 Alamos Gold로 연결하지만 2000 original은:
- gaming machines,
- Native American casino expansion,
- participation games,
- leveraged capital structure

를 다루는 **Alliance Gaming**이다.

실제:
- 2006 Bally Technologies로 name change
- 2014 Scientific Games가 **$83.30 cash/share**에 인수

장기적으로 매우 강한 성공.

exact 2000→2014 multiple은 split history를 완전히 복원하지 않아 산출하지 않는다.

---

# PART G — Alamos 2014 vs 2018: 개발허가보다 operating bottleneck이 더 검증 가능했다

## 10. 2014 Long — 실패

entry ~C$10.

원문:
- 0.9x NAV
- Turkey Kirazli/Agi Dagi
- debt-free cash
- 2016 production >400k oz
- target ~C$18

SQL:
- 1Y **-34.8%**
- 2Y **-41.4%**
- 3Y **-9.8%**

2015 AuRico merger로 company perimeter가 바뀌었고 Turkey project는 original timing에 생산하지 못했다.

## 11. 2018 Long — 매우 강한 성공

entry **~US$3.60**, target **US$5.15**.

이번 thesis는:
- Young-Davidson lower-mine infrastructure
- Island Gold reserve quality
- debt-free balance sheet

였다.

실제:
- YD lower mine completed **2020-07**
- expected mining rate ~**8,000 tpd**
- Island Gold reserves acquisition 이후 2020까지 **+74%**
- 2025 production **545.4k oz**
- 2025 FCF **$351.7m**
- 2026 share price mid-$30s 수준

### 두 vintage 비교

| 구분 | 2014 | 2018 |
|---|---|---|
| 핵심 asset | Turkey development | operating mines |
| 주요 risk | permits/timing | execution/bottleneck |
| balance sheet | 좋음 | 좋음 |
| outcome | 실패 | 매우 강한 성공 |
| lesson | NPV realization timing | existing asset repair |

> **Development NAV는 허가 시점을 맞혀야 하지만 operating bottleneck fix는 매 분기 물리적 진척을 검증할 수 있다.**

---

# PART H — Batch 071 공통 분석식

### Closed-End Fund

**Return = NAV return + discount compression + distribution - leverage/expense drag**

### Distressed Credit

**Expected return = coupon + pull-to-par + spread change × survival probability**

### Broker Liquidity

**Required capital = normal operating cash + stressed collateral calls + counterparty settlement gap**

### Vendor-Financed Platform

**Economic equity = cash - committed financing - future burn + proven unit economics**

### Mining Development

**Project value = headline NPV × permit probability × funding probability × timing discount**

### Operating Mine Repair

**Value uplift = throughput/cost improvement × reserve life × commodity margin**

---

# PART I — Batch 071 재사용 체크리스트

1. CEF yield에서 ROC를 분리한다.
2. NAV discount와 NAV return을 별도 attribution한다.
3. credit idea는 exact security/maturity를 반드시 보존한다.
4. panic credit와 normalization credit를 구분한다.
5. cyclical Long에서 bull margin과 cycle direction을 분리한다.
6. low-capex broker도 collateral stress test를 한다.
7. cash에서 customer financing commitment를 차감한다.
8. negative gross margin은 성장 thesis의 즉각적 falsifier다.
9. historical ticker는 legal entity/date로 검증한다.
10. 장기 M&A return은 split history가 없으면 정밀화하지 않는다.
11. mining development NAV에는 timing probability를 넣는다.
12. operating bottleneck thesis는 physical KPI로 검증한다.

---

## 12. Batch 071 핵심 한 줄

> **이번 배치는 “표면적 자산”보다 실제 cash-flow claim을 보는 훈련이다. CEF는 NAV discount, credit는 maturity, broker는 collateral liquidity, Agrify는 committed cash burn, 광산은 permit timing과 operating bottleneck을 각각 분리해야 한다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_071_agc_agc1_agco_agfx_agfy_agi_10.md`
- Staging catalog (DB 미반영): `data/staging/batch_071_agc_agc1_agco_agfx_agfy_agi_catalog_v9.json`
- Canonical source of truth: 위 10개 Markdown.
