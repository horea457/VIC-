# Batch 074 — Agere / Adecoagro / BrasilAgro / PlayAGS / AGTC / Agrium / Arctic Glacier / Agribrands V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. VIC 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 073 마지막 AGP 2008-12-29 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **7건**(Adecoagro 2015, BrasilAgro 2007, PlayAGS 2019, Agrium 2002, Arctic Glacier 2014/2019, Agribrands 2000). AGX 2000은 SQL company table의 **Argan Inc.가 아니라 Agribrands International**로 mapping 교정했다. Source SQL performance row는 Adecoagro 2015·2019 두 건만 유효하다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2002-11-01 | AGR/A | Long | **Agere Systems Common Long** | [Agere](ideas/2002/2002-11-01_AGR_A_agere_systems_long.md) | **강한 성공 — split-adjusted strategic merger** |
| 2 | 2015-06-01 | AGRO | **Short** | **Adecoagro Common Long** | [Adecoagro 2015](ideas/2015/2015-06-01_AGRO_adecoagro_long.md) | **정책·EBITDA 성공 / FCF·target 실패** |
| 3 | 2019-06-27 | AGRO | Long | **Adecoagro Common Long** | [Adecoagro 2019](ideas/2019/2019-06-27_AGRO_adecoagro_long.md) | **운영 강한 성공 / valuation 부분 성공** |
| 4 | 2007-12-31 | AGRO3 BZ | **Short** | **BrasilAgro Common Long** | [BrasilAgro](ideas/2007/2007-12-31_AGRO3_BZ_brasilagro_long.md) | **asset thesis 성공 / 1Y timing 혼합** |
| 5 | 2019-05-29 | AGS | **Short** | **PlayAGS Common Long** | [PlayAGS](ideas/2019/2019-05-29_AGS_playags_long.md) | **실패 — takeout $12.50, entry 이하** |
| 6 | 2021-07-20 | AGTC | Long | **Applied Genetic Technologies Common Long** | [AGTC](ideas/2021/2021-07-20_AGTC_long.md) | **매우 강한 실패 — cash runway / funding collapse** |
| 7 | 2002-03-09 | AGU | **Short** | **Agrium Common Long** | [Agrium](ideas/2002/2002-03-09_AGU_agrium_long.md) | **운영·장기 강한 성공 / target timing 지연** |
| 8 | 2014-02-06 | AGUNF | **Short** | **Arctic Glacier Liquidating Trust Long** | [Arctic 2014](ideas/2014/2014-02-06_AGUNF_liquidation_long.md) | **recovery 부분 성공 / IRR 실패** |
| 9 | 2019-11-18 | AGUNF | **Short** | **Arctic Glacier Residual Cash Long** | [Arctic 2019](ideas/2019/2019-11-18_AGUNF_final_distribution_long.md) | **실패 — timing·expenses가 spread 소진** |
| 10 | 2000-09-21 | AGX | **Short** | **Agribrands International Common Long** | [Agribrands](ideas/2000/2000-09-21_AGX_agribrands_long.md) | **강한 성공 — Cargill $54.50 cash superior bid** |

---

# PART A — Agere 2002: profitable segment + shrinking loss pool

## 2. Agere Systems

entry:
- **$0.96 pre-split**
- cash/share $0.55
- debt/share $0.41
- target **$2.50**

실제:
- 2005 **1-for-10 reverse split**
- split-adjusted entry **$9.60**
- 2006 LSI merger agreement
- consideration **2.16 LSI shares per Agere share**
- announcement implied value 약 **$22.81**

단순 announcement-value multiple:

**$22.81 / $9.60 ≈ 2.38x**

원문 target $2.50은 split-adjusted $25이므로 strategic value가 target에 근접했다.

### 핵심

> turnaround에서 전체 손익보다 **이미 흑자인 segment와 빠르게 줄어드는 적자 segment를 분리**하는 것이 유용하다.

---

# PART B — Adecoagro 2015 vs 2019: 정책 옵션보다 집행된 CapEx가 더 예측 가능했다

## 3. 2015 Long

entry **$9.66**, target **$27**.

원문:
- Macri reform
- export tax removal
- peso depreciation
- 2016 EBITDA **$300~340m**
- 2017 FCF **~$163m**

실제:
- Argentina policy reform 강하게 현실화
- 2016 adjusted EBITDA **$298m**
- 2017 AFCF before expansion capex **$78.0m**
- 2017 adjusted FCF **$7.2m**

SQL:
- 1Y **+15.0%**
- 2Y **+11.1%**
- 3Y **-17.9%**

정책과 EBITDA는 맞았지만 **EBITDA→FCF bridge가 무너졌다.**

## 4. 2019 Long

entry **$6.90**.

원문 2021:
- EBITDA **$454m**
- 5개년 expansion capex $355m
- target **$12.66**

실제:
- 2021 adjusted EBITDA **$437.1m**
- adjusted FCF from operations **$152.1m**
- 2022부터 prior-year AFCF의 최소 40% 주주환원 정책

SQL:
- 1Y **-39.5%**
- 2Y **+41.2%**
- 3Y **+24.0%**

### 두 vintage 비교

| 항목 | 2015 | 2019 |
|---|---|---|
| 핵심 catalyst | 정책 변화 | 이미 진행 중인 capex |
| EBITDA | 거의 적중 | 거의 적중 |
| FCF | 크게 미달 | 개선·환원 연결 |
| 주가 | 장기 약함 | 2~3Y 회복 |
| 핵심 lesson | macro→cash bridge 위험 | physical capex KPI가 더 검증 가능 |

> **정책이 맞는 것보다 투입된 자본이 실제 EBITDA와 FCF로 바뀌는 과정을 추적하는 편이 반복 가능성이 높다.**

---

# PART C — BrasilAgro: 자산 IRR과 주식 IRR은 다르다

## 5. 2007 Long

entry **R$10**.

원문:
- base R$13.50
- upside R$17
- cash-rich farmland development
- acquire → improve → sell

실제:
- Engenho: **R$10.1m cost → R$22m sale**
- São Pedro: **R$10.3m → R$26m**
- 2008-06 stock ~R$13
- 2008-12 stock ~R$6.9

farm-level capital allocation은 강하게 성공했지만 GFC 때문에 1Y equity result는 나빴다.

### 핵심

> **좋은 자산이 실제 좋은 가격에 팔렸다는 사실과 그 해 주식시장이 NAV를 인정하는 것은 별개다.**

---

# PART D — PlayAGS: M&A optionality가 있어도 entry 아래에서 팔릴 수 있다

## 6. 2019 Long

원문 implied entry 약 **$18.6**, 5Y target 약 **$50**.

thesis:
- recurring leased slots
- product/share gains
- table games
- shuffler optionality
- international expansion
- acquisition target

실제:
- 2020 casino shutdown shock
- business recovery
- 2025 Brightstar acquisition
- **$12.50 cash/share**

대략:

**$12.50 / $18.6 - 1 ≈ -33%**

### 핵심

> strategic buyer가 나타났다는 사실만으로 original valuation thesis가 성공한 것은 아니다.

---

# PART E — AGTC: Biotech Cash는 Floor가 아니라 Runway

## 7. 2021 Long

entry 약 **$3.60+**.

원문:
- cash/share ~**$2.36**
- risk-adjusted value ~**$10.5**
- XLRP / ACHM programs
- cash-adjusted EV cheapness

실제:
- 2022 standalone funding difficulty
- Syncona acquisition
- upfront **$0.34/share**
- CVR 최대 **$0.73**
- theoretical maximum **$1.07**

upfront loss 약 **-90.6%**.

CVR을 모두 받는 비현실적 최대치로도 entry 대비 약 **-70%**.

### 핵심

> **Clinical biotech의 cash는 liquidation asset이 아니라 임상 데이터를 얻기 위해 소진될 committed capital이다.**

---

# PART F — Agrium: Earnings Peak는 맞고 Price Peak 시점은 늦었다

## 8. 2002 Long

raw SQL은 Short지만 original은 명확한 Long.

entry 약 **$9**.

원문:
- North American nitrogen supply shrinkage
- natural-gas cost curve
- peak EPS **~$4**
- target **$35~40 by 2004/05**

실제 2005:
- net earnings **$542.9m**
- diluted EPS **$4.89**

EPS call은 오히려 초과 적중했다.

하지만 2005 YE stock은 약 $22로 target에 못 미쳤고, 2007에는 $60+까지 상승했다.

2018:
- PotashCorp와 Nutrien formation
- AGU 1주당 **2.23 NTR shares**

### 핵심

> commodity cycle에서 **peak earnings를 맞히는 것과 market euphoria가 도착하는 연도를 맞히는 것은 별개의 문제**다.

---

# PART G — Arctic Glacier 2014 vs 2019: 현금이 있어도 시간이 Spread를 먹는다

## 9. 2014 Liquidation Long

entry **US$0.1945**.

원문:
- distributions **$0.23~0.25**
- 1년 내 20~30%
- IRR **35%+**

실제:
- 2015 **US$0.155570**
- 2019 **C$0.042818335**
- 2020 **C$0.01427278**
- 2022 **C$0.00549502 final**

nominal recovery 방향은 대체로 맞았지만 잔여 현금이 8년 가까이 묶였다.

**IRR thesis는 실패.**

## 10. 2019 Residual Cash Long

entry **US$0.0165**.

주의:
- C$0.042818335 distribution의 ex-date는 **2019-11-14**
- VIC post는 **2019-11-18**

따라서 이 distribution은 매수자가 받을 수 없다.

실제 post-entry distributions:
- 2020 C$0.01427278
- 2022 C$0.00549502
- 합계 **C$0.01976780**

USD 환산 시 entry 대비 매력적인 20%+ short-term payoff가 아니었고 3년이 걸렸다.

### 핵심

> liquidation에서 **ex-date 하나를 잘못 잡으면 존재하지 않는 수익을 계산하게 된다.**

---

# PART H — Agribrands: Ticker Mapping 교정이 수익률 분석의 출발점

## 11. 2000 Long

SQL:
- ticker AGX
- company **Argan Inc.**
- raw Short

원문 실제:
- **Agribrands International**
- animal feed / Purina brands
- **Long**

원문:
- market cap ~$425m
- book ~$382m
- net cash >$150m
- EBITDA ~$95m
- TEV/EBITDA **2.9x**
- private value **$59.50**
- implied entry ~$41
- low Ralcorp consideration이 깨질 가능성

실제:
- Cargill이 2000-12 superior bid
- **$54.50 cash/share**
- 약 **$580m**
- Ralcorp transaction 종료

approx payoff:

**$54.50 / ~$41 - 1 ≈ +33%**

약 2~3개월 만의 강한 event-driven 성공.

---

# PART I — Batch 074 공통 분석식

### Commodity Agriculture

**FCF = EBITDA - maintenance capex - expansion capex - working capital - tax/interest**

### Farmland

**Asset IRR = sale proceeds + operating cash flow - land purchase - development capex**

### Clinical Biotech

**Equity value = cash - future burn + probability-adjusted pipeline value - future dilution cost**

### Liquidation

**IRR = dated distributions / purchase price**, not nominal total recovery alone.

### Strategic M&A

**Event payoff = final consideration - purchase price - time/hedge/break costs**

---

# PART J — Batch 074 재사용 체크리스트

1. raw Long/Short field를 original disclosure로 확인한다.
2. historical ticker는 legal entity를 재검증한다.
3. reverse split을 corporate-action return에 반영한다.
4. EBITDA와 FCF forecast를 별도 hypothesis로 둔다.
5. agricultural expansion capex와 maintenance capex를 분리한다.
6. farm-level realized sale IRR와 listed-equity return을 분리한다.
7. acquisition optionality는 실제 takeout price로 검증한다.
8. biotech cash에서 clinical runway를 차감한다.
9. CVR maximum을 realized cash로 간주하지 않는다.
10. liquidation은 ex-date와 entitlement를 확인한다.
11. cross-currency distributions는 지급일 FX가 필요하다.
12. commodity earnings peak와 stock multiple peak의 timing을 분리한다.

---

## 12. Batch 074 핵심 한 줄

> **이번 배치의 공통점은 “보이는 자산가치”를 그대로 주주가치로 쓰면 안 된다는 것이다. Adecoagro의 EBITDA는 FCF와 달랐고, AGTC cash는 burn runway였으며, Arctic cash는 지급이 늦었고, Agribrands의 net cash는 반대로 실제 superior bid를 지지했다.**

## 13. 앱 / DB 반영

- Wrapper: analysis/batch_074_agr_agro_ags_agtc_agu_agunf_agx_10.md
- Overlay: data/curated/batch_074_agr_agro_ags_agtc_agu_agunf_agx_deep_v7.json
- Canonical source of truth: 위 10개 Markdown.
