# Batch 064 — AEP / Atlas Engineered Products / AEP Industries / Aeroplan / AerCap V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-16.
> **Batch boundary:** Batch 063 마지막 AEOS 2005-12-11 이후 ticker/date ordering을 유지한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **2건**. 동일 ticker 충돌 **2건**을 발견해 company mapping을 교정했다: 2012 `AEP`는 American Electric Power가 아니라 **Anglo-Eastern Plantations**, 2011 `AER`는 AerCap이 아니라 **Groupe Aeroplan/Aimia**다. 두 idea의 SQL performance row는 다른 회사 가격이므로 폐기했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 방향 / Security | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2003-08-27 | AEP | Long | **American Electric Power Common Long** | [AEP 2003](ideas/2003/2003-08-27_AEP_american_electric_power_long.md) | **강한 성공 — cleanup·규제회수·$37 target 달성** |
| 2 | 2012-06-11 | AEP | **Short** | **Anglo-Eastern Plantations Common Long** | [AEP LN 2012](ideas/2012/2012-06-11_AEP_anglo_eastern_plantations_long.md) | **사업/asset thesis 장기 성공·SQL return 폐기** |
| 3 | 2020-01-28 | AEP. | Long | **Atlas Engineered Products Common Long** | [Atlas 2020](ideas/2020/2020-01-28_AEP_atlas_engineered_products_long.md) | **가격 지연 성공 / 2022 C$100m sales 실패** |
| 4 | 2022-05-30 | AEP. | **Short** | **Atlas Engineered Products Common Long** | [Atlas 2022](ideas/2022/2022-05-30_AEP_atlas_engineered_products_long.md) | **C$1.50 지연 성공 / peak earnings extrapolation 과도** |
| 5 | 2008-03-20 | AEPI | Long | **Common Long** | [AEPI 2008](ideas/2008/2008-03-20_AEPI_long.md) | **장기 valuation 성공 / GFC로 near-term timing 혼합** |
| 6 | 2009-10-12 | AEPI | Long | **Common Long** | [AEPI 2009](ideas/2009/2009-10-12_AEPI_long.md) | **distressed M&A mechanism 성공 / 1~2Y target 과도** |
| 7 | 2011-07-12 | AEPI | Long | **Common Long** | [AEPI 2011](ideas/2011/2011-07-12_AEPI_long.md) | **강한 성공 — normalized spread + buyback** |
| 8 | 2014-07-09 | AEPI | Long | **Common Long** | [AEPI 2014](ideas/2014/2014-07-09_AEPI_long.md) | **강한 성공 — trough normalization + $110 exit** |
| 9 | 2011-09-15 | AER | Long | **Groupe Aeroplan/Aimia Common Long** | [Aeroplan 2011](ideas/2011/2011-09-15_AER_groupe_aeroplan_long.md) | **혼합 — FCF 개선, C$24 실패, anchor risk 현실화** |
| 10 | 2014-01-27 | AER | Long | **AerCap Common Long** | [AerCap 2014](ideas/2014/2014-01-27_AER_aercap_long.md) | **EPS 적중 / stock target 실패 — 2Y -18.4%** |

---

# PART A — AEP라는 ticker가 세 회사다

## 2. American Electric Power 2003 — growth가 아니라 risk normalization

@ 약 **$27.50**, dividend **$1.40 / ~5.1% yield**.

원문 base:
- cost reduction ~$200m
- Texas stranded-cost recovery **≥$1.4bn**
- merchant asset sales **≥$1bn**
- 2006 EPS **$2.82**
- target **$37**

실제:
- Texas securitization/recovery 약 **$1.697bn**
- 2005 asset-sale proceeds 약 **$1.606bn**
- 2006 ongoing EPS **$2.77**
- 2005 year-end stock **$37.09**
- 2006 year-end **$42.58**

> **utility turnaround에서 핵심은 성장보다 규제회수와 asset sales가 실제 cash로 들어와 risk premium을 낮추는가다.**

## 3. Anglo-Eastern Plantations 2012 — P/E보다 hectare와 tree age

SQL은 이 회사를 American Electric Power로 잘못 매핑했다. 원문은 명백히 **LSE:AEP Anglo-Eastern Plantations**다.

핵심 T0:
- 약 **$4.2k~5.2k per planted ha**
- replacement value 약 **$8k/ha**
- private deals **$15k~20k/ha**
- immature acreage가 maturity로 가며 embedded production growth

실제:
- 2012 FFB **783.4k mt**, +11%
- CPO **260.5k mt**, +5%
- 2012 net cash **$91.2m**
- 2024 attributable profit **$67.5m**
- 2024 net cash **$181.9m**

SQL price series는 NYSE:AEP 가격이므로 전부 폐기했다.

> **plantation은 commodity price보다 EV/ha, tree age, yield/ha, extraction rate를 먼저 본다.**

---

# PART B — Atlas: 좋은 roll-up도 시간은 마음대로 못 줄인다

## 4. 2020 Long

@ **C$0.39**.

원문 2022 목표:
- revenue **C$100m**
- EBITDA margin **15%**
- target **C$1.00**

실제:
- 2022 revenue **C$61.9m**
- operating profit 약 **C$12.5m**
- 2024 price roughly **C$1.5+**
- 2025 revenue **C$62.6m**, normalized EBITDA **C$7.38m**

즉 operating scale-up timing은 실패했지만 stock target는 약 3~4년 늦게 달성했다.

## 5. 2022 Long

@ 약 **C$0.53**.

원문은 record 1Q22를 바탕으로:
- LTM normalized EBITDA ~C$15m
- 2022 EBIT **C$17m**
- 6x EV/EBIT
- target **C$1.50**

을 제시했다.

실제 2022 operating profit은 약 **C$12.5m**, 2023에는 약 **C$5.3m**으로 크게 내려갔다. 그러나 2024 stock은 C$1.50 이상을 기록했다.

> **3x EBIT은 싸 보여도, 분모가 record-quarter annualization이면 multiple보다 denominator를 먼저 의심한다.**

---

# PART C — AEPI 네 번: spread business + capital allocation

## 6. 공통 economic engine

AEPI의 매출은 resin price 때문에 noise가 크다. 핵심은:

`pounds sold × gross spread/lb - conversion/SG&A - interest - capex = equity FCF`

네 아이디어를 관통하는 것은:
1. resin price pass-through lag
2. downturn에서 distressed acquisitions
3. capacity rationalization
4. aggressive buybacks
5. normalized spread recovery

이다.

## 7. Four-vintage comparison

| 아이디어 | 핵심 entry logic | 핵심 claim | 사후 판정 |
|---|---|---|---|
| 2008 | 4.9x LTM EBITDA / 6x FCF | recession-resistant + buyback | GFC timing 혼합, long-run value 성공 |
| 2009 | Atlantis 실질 purchase price 매우 낮음 | ≥$125m normalized EBITDA | M&A thesis 성공, target timing 과도 |
| 2011 | depressed EBIT/lb + 36% share-count reduction | $80m+ EBITDA, >$50 value | 강한 성공 |
| 2014 | LTM $44m EBITDA vs normalized $135m | ~$9.40 EPS / consolidation | exact EPS 미검증, $110 exit로 value 검증 |

### 최종 external anchor

Berry는 2017-01-20 AEPI 인수를 완료했다. 각 AEPI share는 **$110 cash 또는 2.5011 Berry shares**를 받을 권리로 전환됐고 aggregate consideration은 50/50 cash/stock proration이었다.

### 핵심

> AEPI에서 알파는 resin 가격을 맞힌 것이 아니라 **cycle-low에 assets와 자기주식을 싸게 사서 normalized spread가 돌아왔을 때 per-share earnings power를 크게 만든 것**이었다.

---

# PART D — 같은 AER ticker, 완전히 다른 두 기업

## 8. Groupe Aeroplan 2011 — network effect보다 network topology

SQL company mapping은 AerCap으로 잘못돼 있지만 원문은 Canadian loyalty company **Groupe Aeroplan**, later Aimia다.

원문:
- normalized FCF/share 약 **C$1.20~1.25**
- 2013 FCF/share **~C$1.60**
- 15x FCF → **C$24 target**

실제:
- 2013 year-end price 약 **C$17.6** → target 실패
- 2017 Air Canada가 2020 이후 Aeroplan 계약 non-renewal 통보
- Aeroplan business는 결국 Air Canada-led consortium에 매각
- post-close adjustment 후 final cash purchase price 약 **C$516m**

원문은 coalition network와 diversification을 moat로 봤지만 Air Canada는 단순 partner가 아니라 redemption utility의 **critical node**였다.

> **network size보다 가장 중요한 node가 빠졌을 때 utility가 남는지 봐야 한다.**

## 9. AerCap 2014 — 분자를 정확히 맞혔는데 주가는 틀렸다

@ 약 **$35**.

원문 ILFC 모델:
- pro forma book 약 1.2x
- ROE **15~17%**
- 2016 EPS **~$5.50**
- target **$60.50 @ 11x**

실제:
- ILFC close 2014-05-14
- 2016 reported diluted EPS **$5.52**
- adjusted diluted EPS **$6.85**
- end-2016 BVPS **$49.33**
- SQL 2Y price return **-18.4%**
- SQL 5Y price return **+26.3%**

EPS forecast가 거의 완벽히 맞았지만 11x multiple이 오지 않았다.

> **분자를 맞혀도 valuation regime을 틀리면 stock return은 실패한다.**

---

# PART E — Batch 064 공통 분석식

### Utility

`rate base × allowed ROE + nonregulated earnings - interest/capex funding gap = equity earnings`

### Plantation

`mature ha × yield/ha × extraction rate × CPO price - estate/mill cost = plantation cash earnings`

### Building-products roll-up

`regional volume × price - material/labour/plant cost + acquisition synergy = EBITDA`

### Flexible-film converter

`pounds sold × gross spread/lb - conversion/SG&A - interest/capex = FCF`

### Loyalty

`gross billings - redemption cash cost - opex - capex/tax ± float timing = FCF`

### Aircraft leasing

`lease yield + asset-sale economics - depreciation - funding cost = earnings`, but stock value is additionally **sustainable ROE × book-value multiple**의 함수다.

---

# PART F — Batch 064 재사용 체크리스트

1. ticker만 보고 company identity를 확정하지 않는다.
2. company mapping이 틀리면 performance row도 같이 audit한다.
3. raw Short/Long과 실제 원문 방향을 분리한다.
4. utility turnaround는 regulatory cash recovery를 직접 확인한다.
5. plantation은 EV/ha와 age profile을 본다.
6. roll-up pipeline을 확정매출처럼 연환산하지 않는다.
7. record quarter를 annualize하기 전에 cycle/seasonality를 정상화한다.
8. spread business는 revenue보다 unit spread를 본다.
9. buyback은 dollar amount보다 share-count reduction으로 본다.
10. network effect는 critical-node removal stress test를 한다.
11. earnings forecast와 multiple forecast를 별도 claim으로 저장한다.
12. strategic takeout이 value를 검증해도 이전 horizon의 target-price 실패를 성공으로 소급하지 않는다.

---

## 10. Batch 064 핵심 한 줄

> **좋은 분석은 ‘얼마를 벌 것인가’와 ‘시장이 그 이익에 얼마를 지불할 것인가’를 분리한다. AerCap은 2016 EPS $5.50 예상이 실제 $5.52로 거의 정확했지만 2년 주가는 -18.4%였다.**

## 11. 데이터 정합성 / 중복 처리

- `AEP 2003` = American Electric Power.
- `AEP 2012` = Anglo-Eastern Plantations; SQL company/performance contamination 교정.
- `AEP. 2020/2022` = Atlas Engineered Products.
- `AER 2011` = Groupe Aeroplan/Aimia; SQL AerCap mapping/performance contamination 교정.
- `AER 2014` = 실제 AerCap Holdings.
- AEPI 네 아이디어는 같은 company지만 각각 다른 cycle/entry/horizon이므로 canonical을 별도로 유지한다.

## 12. 앱 / DB 반영

- Wrapper: `analysis/batch_064_aep_atlas_aepi_aer_10.md`
- Overlay: `data/curated/batch_064_aep_atlas_aepi_aer_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
