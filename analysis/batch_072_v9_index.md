# Batch 072 — Alamos / Aegis / Aggreko / Angelica / Autogrill / Farmer Mac / Allergan V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 071 마지막 **AGI 2018-11-18** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long/Long-spread **3건(AGK 2014, AGM 2009, AGN.PA 2016)**. AGN.PA 2016은 단순 equity short가 아니라 **Pfizer/Allergan merger-arb basket leg**다. Source SQL performance row는 Farmer Mac 2009에만 유효하게 존재한다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 전략 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2022-06-24 | AGI. | Long | **Alamos Gold Common Long** | [Alamos 2022](ideas/2022/2022-06-24_AGI_alamos_gold_long.md) | **주가 매우 강한 성공 / 일정·AISC forecast 미달** |
| 2 | 2019-12-30 | AGIS IN | Long | **Aegis Logistics Common Long** | [Aegis](ideas/2019/2019-12-30_AGIS_IN_aegis_logistics_long.md) | **매우 강한 성공 — LPG terminal compounder** |
| 3 | 2014-02-07 | AGK | **Short** | **Aggreko Common Long** | [Aggreko](ideas/2014/2014-02-07_AGK_aggreko_long.md) | **실패 — 1,527p→880p takeout** |
| 4 | 2003-12-31 | AGL | Long | **Angelica Common Long** | [Angelica](ideas/2003/2003-12-31_AGL_angelica_long.md) | **성공·혼합 — divestiture 미달, $22 strategic exit** |
| 5 | 2013-10-02 | AGL IM | Long | **Autogrill Common Long** | [Autogrill](ideas/2013/2013-10-02_AGL_IM_autogrill_long.md) | **운영 부분 성공 / timing·payoff 실패** |
| 6 | 2009-08-10 | AGM | **Short** | **Farmer Mac Common Long** | [Farmer Mac](ideas/2009/2009-08-10_AGM_farmer_mac_long.md) | **매우 강한 성공 — 5Y +295.4%** |
| 7 | 2015-01-16 | AGN | Long | **Allergan/Actavis Merger-Arb Long Spread** | [Actavis Arb](ideas/2015/2015-01-16_AGN_actavis_merger_arb_long.md) | **강한 성공 — 약 2개월 내 close** |
| 8 | 2018-01-17 | AGN | Long | **Allergan Common Long** | [Allergan 2018](ideas/2018/2018-01-17_AGN_allergan_long.md) | **부분 성공 — strategic takeout, $240~270 target 미달** |
| 9 | 2019-10-16 | AGN | Long | **Allergan/AbbVie Merger-Arb Long Spread** | [AbbVie Arb](ideas/2019/2019-10-16_AGN_abbvie_merger_arb_long.md) | **강한 성공 — exact terms로 close** |
| 10 | 2016-02-19 | AGN.PA | **Short** | **Pfizer/Allergan Merger-Arb Long Spread / Pair Leg** | [Pfizer Arb](ideas/2016/2016-02-19_AGN_PA_pfizer_allergan_merger_arb.md) | **실패 — Treasury tax-rule change로 deal break** |

---

# PART A — Alamos 2022: 주가 성공과 운영 Forecast 정확도를 분리해야 한다

## 2. 2022 Long

원문:
- current production 약 465k oz
- 2027 production **700k oz+**
- 2025 AISC 약 **$800/oz**
- Island Gold Phase III
- Mulatos PDA
- Lynn Lake 2027
- strong balance sheet
- possible buyout

실제:
- 2024 Magino acquisition으로 company perimeter 확대
- 2027 current guide **650~730k oz**
- 2028 **755~835k oz**
- 2026 AISC **$1,500~1,600**
- Lynn Lake first production **H1 2029**
- Island Gold District 장기 scale는 오히려 더 커짐

주가는 high-$6s에서 2026 mid-$30s 수준으로 multi-bagger가 됐다.

### 핵심

> **좋은 광산을 맞힌 것과 그 광산이 정확히 언제 얼마의 원가로 생산할지를 맞힌 것은 별개의 skill이다.**

---

# PART B — Aegis Logistics: throughput compounder

## 3. 2019 Long

원문:
- India LPG demand 7~8% CAGR
- company gas volumes 20%+ CAGR
- LPG terminal capacity 5m mtpa → 9.2m mtpa
- high terminal margins
- incremental ROIC 50%+
- current earnings multiple ~25x

실제 FY2026:
- group revenue **₹8,333 crore**
- normalized EBITDA **₹1,599 crore**
- PAT **₹1,107 crore**
- LPG terminal throughput **5.15m tonnes**
- Vopak JV와 다지역 terminal expansion

2026 price 약 ₹1,354, early-2020 reference 약 ₹131.

### 핵심

> **25x P/E가 비싸 보여도 terminal capacity와 incremental ROIC가 오래 복리성장하면 denominator가 valuation을 따라잡을 수 있다.**

---

# PART C — Aggreko: historical ROCE를 영구 moat로 보면 안 된다

## 4. 2014 Long

entry **1,527p**.

원문:
- world #1 temporary power
- historical sales CAGR ~20%
- EPS CAGR ~30%
- ROCE 25~35%
- 12x EV/EBIT / 15x P/E
- passage of time itself is catalyst

실제:
- long-run economics weakened
- 2021 I Squared/TDR take-private
- cash consideration **880p**

**880 / 1,527 - 1 ≈ -42.4%** before dividends.

### 핵심

> **Capital-intensive compounder는 브랜드보다 cycle-adjusted incremental ROCE가 계속 높은지를 확인해야 한다.**

---

# PART D — Angelica와 Autogrill: corporate action이 있어도 IRR은 전혀 다를 수 있다

## 5. Angelica 2003

원문:
- Life Uniform sale
- healthcare textile pure-play
- tangible assets / owned real estate
- consolidation
- eventual strategic sale

실제:
- 2004 Life Uniform sale: **$16.24m**, 원문 $20m+ 기대 미달
- 2008 company sold for **$22 cash/share**

구조적 thesis는 대체로 성공했지만 exact entry가 없어 IRR은 산출하지 않는다.

## 6. Autogrill 2013

entry **€6.02**.

원문:
- WDF demerger
- bad Italian motorway concessions expiry
- 24~30개월 내 FCF uplift
- possible SSP merger

실제:
- operating cash generation 개선
- SSP merger는 없음
- 2023 Dufry combination
- mandatory offer **0.1583 Dufry share or €6.33 cash**

cash 기준 nominal gain은 약 **+5.1%**에 불과하다.

### 비교

| 구분 | Angelica | Autogrill |
|---|---|---|
| 핵심 catalyst | non-core sale + eventual sale | bad concession expiry |
| corporate action | $22 cash takeout | Dufry combination |
| timing | 수년 | 약 10년 |
| payoff | 성공 방향 | 낮은 IRR |
| lesson | simplification can crystallize | delayed catalyst can destroy IRR |

---

# PART E — Farmer Mac: crisis loss book과 core franchise를 분리하면

## 7. 2009 Long

원문은 2008 위기의:
- Fannie/Freddie preferreds
- Lehman exposure
- ethanol lending
- capital impairment

을 core agricultural finance business와 분리했다.

원문 core earnings:
- annual **$15~20m**
- equity value **$150m+**

실제:
- 2009 core earnings **$16.1m**
- 2010 **$25.4m**
- 2011 **$42.9m**

Source SQL:
- 1Y **+64.0%**
- 2Y **+116.1%**
- 3Y **+211.7%**
- 5Y **+295.4%**

> **crisis equity에서 old losses가 이미 recognition된 뒤 core engine이 살아 있다면 earnings normalization이 매우 큰 convexity를 만든다.**

---

# PART F — Allergan 4개: ticker는 같지만 투자 메커니즘은 네 번 다르다

## 8. 2015 — Actavis Merger Arb

- AGN $216.40
- ACT $265.13
- consideration **$129.22 + 0.3683 ACT**
- implied value $226.87
- spread **4.8%**
- expected close 6~8 weeks

실제:
- **2015-03-17 close**
- exact stated terms

**강한 성공.**

## 9. 2016 — Pfizer Merger Arb

이 record는 단순 Short가 아니라 merger-arb basket의 AGN/PFE leg다.

원문은 deal-specific/antitrust risk를 관리 가능한 Tier-2로 봤다.

실제:
- 2016-04-04 Treasury anti-inversion rules
- 2016-04-06 merger terminated
- Pfizer → Allergan $150m expense reimbursement

**정책 regime risk를 놓친 명확한 실패.**

## 10. 2018 — Fundamental Allergan Long

원문:
- 2018 EPS ≥$15
- 2022 EPS **$22~25**
- target **$240~270**
- Botox + growth pharma franchise

실제:
- standalone thesis가 끝까지 검증되기 전에 AbbVie 인수
- 2019 announcement implied value 약 **$188.24**
- 2020 close: **$120.30 cash + 0.8660 ABBV**

takeout은 depressed price보다 높았지만 원문 target보다 낮았다.

**부분 성공.**

## 11. 2019 — AbbVie Merger Arb

- consideration **$120.30 cash + 0.8660 ABBV**
- spread **7.9%**
- author expected IRR ~17%
- expected early-2020

실제:
- **2020-05-08 close**
- exact stated terms

**강한 성공**, 다만 exact realized IRR은 hedge execution 없이 산출하지 않는다.

---

# PART G — 같은 Allergan에서 배울 수 있는 것

| Vintage | 투자 유형 | 핵심 변수 | 실제 결과 |
|---|---|---|---|
| 2015 | merger arb | close probability / timing | 성공 |
| 2016 | tax-inversion arb | policy regime | 실패 |
| 2018 | fundamental Long | EPS / multiple / franchise | 부분 성공 |
| 2019 | merger arb | close probability / hedge | 성공 |

### 핵심

> **ticker를 연구하는 것이 아니라 특정 시점의 특정 claim을 연구해야 한다.**

같은 Allergan이라도:
- fundamental equity,
- target merger spread,
- tax-inversion spread,
- stock-for-stock hedge

는 완전히 다른 투자다.

---

# PART H — Batch 072 공통 분석식

### Mining

**Equity return = project execution + reserve growth + commodity beta + valuation change**

### Throughput Infrastructure

**EBITDA = capacity × utilization × tariff - fixed operating cost**

### Capital-Intensive Rental

**Value creation = incremental invested capital × sustainable incremental ROCE**

### Service Divestiture

**Equity value = core business value + net divestiture proceeds - stranded overhead**

### Crisis Financial

**Normalized equity value = core earnings / required yield - remaining loss book**

### Merger Arbitrage

**Expected return = close probability × spread - break probability × break loss - time/borrow/hedge costs**

---

# PART I — Batch 072 재사용 체크리스트

1. mining production growth와 AISC forecast를 별도 검증한다.
2. acquisition으로 perimeter가 바뀌면 original denominator를 재작성한다.
3. terminal infrastructure는 capacity보다 actual throughput과 utilization을 본다.
4. historical ROCE를 영구적인 moat로 자동 extrapolate하지 않는다.
5. asset sale은 expected proceeds와 actual net proceeds를 비교한다.
6. catalyst가 10년 늦게 오면 original event thesis 성공으로 처리하지 않는다.
7. crisis 금융사는 core earnings와 toxic-assets loss book을 분리한다.
8. merger arb는 target fundamental value와 별도 security다.
9. stock consideration deal은 hedge ratio를 정확히 보존한다.
10. tax-driven deal은 tax-law change clause를 반드시 읽는다.
11. takeout premium이 original fair-value target보다 낮으면 partial success로 분리한다.
12. 같은 ticker라도 vintage별 payoff mechanism을 다시 정의한다.

---

## 12. Batch 072 핵심 한 줄

> **이번 배치의 핵심은 같은 기업명이나 좋은 사업보다 “내가 실제로 산 claim이 무엇인가”다. Alamos는 좋은 자산과 나쁜 일정이 공존했고, Aggreko는 좋은 franchise가 나쁜 주식이었으며, Allergan은 같은 ticker 안에서도 fundamental Long과 세 종류의 merger-arb가 전혀 다른 결과를 냈다.**

## 13. 앱 / DB 반영

- Wrapper: analysis/batch_072_agi_agis_agk_agl_agm_agn_10.md
- Overlay: data/curated/batch_072_agi_agis_agk_agl_agm_agn_deep_v7.json
- Canonical source of truth: 위 10개 Markdown.
