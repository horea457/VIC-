# Batch 070 — AFSI / AFT / Carl Zeiss Meditec / Afya / AGCO / Arctic Glacier / AUTO1 / Algoma Steel V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 069 마지막 **AFSI 2010-01-13** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **2건(AFT-U 2004, AG1 2021)**. AFT-U와 AG-U는 ordinary common이 아니라 **Canadian income-trust units**다. source DB performance row는 10건 모두 없어 SEC/company filings, corporate actions, insolvency distributions, historical price series를 우선했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2013-08-19 | AFSI | Short | **AmTrust Common Short** | [AFSI 2013](ideas/2013/2013-08-19_AFSI_short.md) | **fundamental 후행 적중 / trade 혼합·실패** |
| 2 | 2004-11-18 | AFT-U | **Short** | **Advanced Fiber Technologies Income Trust Long** | [AFT](ideas/2004/2004-11-18_AFT_UN_long.md) | **실패 — C$5.50→C$3 takeout** |
| 3 | 2022-03-12 | AFX.GY | Long | **Carl Zeiss Meditec Common Long** | [CZM](ideas/2022/2022-03-12_AFX_GY_long.md) | **강한 실패 — product moat 유지, earnings/multiple 붕괴** |
| 4 | 2022-01-13 | AFYA | Long | **Afya Common Long** | [Afya](ideas/2022/2022-01-13_AFYA_long.md) | **운영 성공 / 주식 실패** |
| 5 | 2003-01-13 | AG | Short | **AGCO Common Short** | [AGCO 2003](ideas/2003/2003-01-13_AGCO_short.md) | **2~3Y 가격 부분 성공 / 장기 fundamental 실패** |
| 6 | 2005-10-18 | AG | Short | **AGCO Common Short** | [AGCO 2005](ideas/2005/2005-10-18_AGCO_short.md) | **강한 실패 — ~$16→2007 ~$68** |
| 7 | 2009-08-27 | AG-U | Long | **Arctic Glacier Income Trust Long** | [Arctic Glacier](ideas/2009/2009-08-27_AG_UN_long.md) | **강한 실패 — 2012 CCAA / 저회수** |
| 8 | 2021-09-30 | AG1 | **Short** | **AUTO1 Group Common Long** | [AUTO1 2021](ideas/2021/2021-09-30_AG1_long.md) | **사업 성공 / 주식 실패 — ~€31.6→~€20** |
| 9 | 2022-03-04 | AG1-ETR | Long | **AUTO1 Group Common Long** | [AUTO1 2022](ideas/2022/2022-03-04_AG1_ETR_long.md) | **부분 성공·진행 중 — ~€11→~€20, 2027 target 미달** |
| 10 | 2003-02-28 | AGA CN | Long | **Legacy Algoma Steel Common Long** | [Algoma](ideas/2003/2003-02-28_AGA_CN_algoma_long.md) | **초대형 성공 — C$3.30→C$56 cash, ~17x** |

---

# PART A — AmTrust 2013: 회계 문제를 맞혀도 Short는 실패할 수 있다

## 2. 2013 Short

원문은 AFSI를 단순 고평가 보험사가 아니라 **reported earnings와 tangible-book accumulation이 맞지 않는 회사**로 분석했다.

핵심:
- life-settlement Level 3 valuation,
- under-reserving,
- M&A accounting,
- captive/related-party reinsurance,
- NPW / tangible equity **~150% → ~336%**.

실제:
- 2014·2015 및 2016 일부 분기 restatement,
- service/fee revenue recognition 오류,
- 2014 net income -7.2%, 2015 -11.2% restatement,
- 2018 take-private **$14.75**.

하지만 주가는 short entry 약 $18에서 2015 약 $36까지 먼저 상승했다.

### 핵심

> **Short에서 fundamental truth와 investable timing은 별개다.**

회계 분석은 높은 점수를 주되 security outcome은 clean success로 분류하면 안 된다.

---

# PART B — AFT: M&A catalyst가 일어나도 실패할 수 있다

## 3. Advanced Fiber Technologies 2004

entry:
- **C$5.50**
- EV 약 C$118m
- 2004E EBITDA 약 C$16.2m
- distribution **C$0.60/unit**
- 11% yield

원문은:
- 85~90% replacement demand,
- global screen-cylinder share 약 30%,
- historical EBITDA margin high-20s/low-30s,
- cost savings,
- distribution recovery,
- M&A

를 기대했다.

실제 Aikawa가 2006 회사를 인수했지만 가격은 **C$3.00/unit**.

**C$3 / C$5.5 - 1 ≈ -45.5%** before distributions.

### 핵심

> **M&A는 catalyst의 발생 여부가 아니라 takeout consideration이 결과다.**

---

# PART C — Carl Zeiss vs Afya: 좋은 사업이 좋은 주식이 아닌 두 방식

## 4. Carl Zeiss Meditec 2022

entry 약 **€151**.

원문:
- SMILE / VisuMax moat,
- recurring procedure consumables,
- VisuMax 800 upgrade,
- premium IOL,
- base target €263 / bull €514.

실제:
- FY2024/25 revenue €2.228bn
- EBITA margin **11.6%**
- EPS **€1.61**
- H1 FY2025/26 adjusted EBITA margin **6.1%**
- 9M margin **8.0%**
- 2026 대규모 구조조정
- share price high-€20s

### 판정

제품 moat가 사라진 것이 아니라 **earnings duration과 starting multiple이 무너졌다.**

## 5. Afya 2022

entry 약 **$14.5**, core-only target **$28**.

실제 2025:
- revenue **R$3.697bn**
- adjusted EBITDA **R$1.680bn**
- EBITDA margin **45.4%**
- FCF **R$1.056bn**

2026-09 stock은 약 **$13.5~13.7**.

### 판정

Afya는 Carl Zeiss와 달리 earnings가 실제로 강하게 성장했다. 그런데도 multiple/country-risk가 rerate되지 않아 stock은 실패했다.

| 비교 | Carl Zeiss | Afya |
|---|---|---|
| 사업 moat | 유지 | 유지/강화 |
| earnings forecast | 크게 미달 | 대체로 성공 |
| optionality | IOL 기대 미달 | digital 기대 미달 |
| valuation | 강한 de-rating | persistent discount |
| 주가 | 큰 손실 | 대체로 flat/down |

> **주가 실패는 earnings가 틀려서도, earnings는 맞지만 multiple이 안 붙어서도 발생한다.**

---

# PART D — AGCO Short 두 번: balance-sheet analysis가 cycle call을 이기지 못하다

## 6. 2003 Short

entry **$21.74**.

원문:
- 90x TTM GAAP earnings,
- high debt / finance JV exposure,
- working-capital deterioration,
- pension issues,
- Challenger integration.

실제:
- 2003 sales **$3.495bn**
- 2004 **$5.273bn**
- 2005 **$5.450bn**
- 2005 year-end stock ~**$16.6**
- 2007 year-end ~**$68**

2005까지는 short에 약 24% favorable move가 있었지만 business thesis는 예상보다 훨씬 강했다.

## 7. 2005 Short

entry 약 **$16**.

원문:
- EV $2.6bn,
- off-BS financing까지 adj EV 약 $5bn,
- 86% variable-rate debt,
- higher LIBOR,
- fertilizer/energy pressure.

실제:
- 2006 year-end ~$31
- 2007 year-end ~$68

maximum adverse move는 약 **+325% against short**.

### 핵심

> **cyclical short에서 balance-sheet 취약성보다 cycle inflection timing이 더 중요할 수 있다.**

---

# PART E — Arctic Glacier: 안정적인 사업과 안전한 equity는 다르다

## 8. 2009 Long

entry **C$1.72**, expected value **C$5.40**.

원문:
- P/E 3.7x,
- TEV/EBITDA 5.3x,
- normalized EBITDA ~$60m,
- ~50% equity FCF yield,
- DOJ/lawsuits manageable,
- refinancing 해결 가능.

실제:
- **2012-02-22 CCAA**
- operating assets sale
- 2015 US$0.155570/unit distribution
- 2019 C$0.042818335
- 2020 C$0.01427278
- 2022 final C$0.00549502

총 recovery는 original C$1.72에 크게 미달했다.

> **stable EBITDA가 있어도 debt maturity 전에 refinancing이 실패하면 equity는 residual이 아니다.**

---

# PART F — AUTO1 두 번: 같은 회사, entry price가 thesis를 바꾸다

## 9. 2021 Long

2021-09 month-end 약 **€31.57**.

원문:
- European used-car fragmentation,
- consumer sourcing network,
- proprietary data,
- logistics density,
- 1.3x forward sales,
- 5%+ long-run net margin.

실제 FY2025:
- revenue **€8.173bn**
- units **842,271**
- gross profit **€990.6m**
- adjusted EBITDA **€197.5m**

그러나 2026-09 share price 약 **€20.2**, entry 대비 약 -36%.

## 10. 2022 Long

원문 가격 약 **€11**, 2022-03 monthly close €10.34.

SOTP:
- merchant business alone ≈ current price,
- net cash ~€3.70/share,
- Autohero effectively negative value.

2027 forecast:
- Autohero 750k+ units,
- GPU €2,500+,
- ~8% operating margin,
- EPS €3.74,
- target €36.

실제 2025:
- Autohero units **101,539**
- GPU **€2,605**
- Group adjusted EBITDA **€197.5m**
- 2026 share ~€20.2

### 두 vintage 비교

| 항목 | 2021 | 2022 |
|---|---:|---:|
| Entry | ~€31.6 | ~€10~11 |
| Business thesis | scale-up | core + free Autohero option |
| 2026 price | ~€20.2 | ~€20.2 |
| Price return | ~-36% | roughly +84~95% |
| Core lesson | valuation too high | lower price changed asymmetry |

> **좋은 회사를 더 싸게 산 정도가 아니라, 가격 하락으로 투자논지 자체가 TAM Long에서 SOTP/options Long으로 바뀌었다.**

---

# PART G — Algoma Steel: post-reorg equity의 convexity

## 11. 2003 Long

entry:
- **C$3.30**
- book value **C$11.47**
- P/B ~0.29x
- bankruptcy emergence Feb-2002
- debt/equity ~C$529m/C$345m
- furnace reline ~$120m.

원문 upside:
- steel price recovery,
- debt paydown,
- takeover.

실제:
- Essar Global 2007 acquisition **C$56 cash/share**
- equity value C$1.85bn.

**C$56 / C$3.30 ≈ 16.97x**

### 핵심

post-reorg equity의 가장 강한 setup:

1. old liabilities가 reset되고,
2. operating leverage는 남고,
3. market은 old bankruptcy fear를 계속 가격화하며,
4. strategic buyer가 replacement value를 인정한다.

---

# PART H — Batch 070 공통 분석식

### Insurer Short

**Economic book growth = cumulative earnings - distributions - dilution ± true reserve/asset marks**

### Income Trust

**Equity yield floor = sustainable distributable cash / purchase price**, not stated distribution alone.

### High-multiple Moat

**Shareholder return = earnings growth × multiple change + distributions**

moat는 multiple compression을 막아주지 않는다.

### Cyclical Short

**Short payoff = cycle downside × catalyst speed - adverse-cycle convexity**

### Distressed Equity

**Equity survival = enterprise cash generation - mandatory debt/legal cash outflows before refinance date**

### Platform Growth

**Intrinsic progress = units × GPU - operating cost structure**

하지만 investment return에는 starting EV까지 들어간다.

### Post-Reorg Cyclical

**Equity convexity = operating leverage × cycle recovery / reduced fixed claims**

---

# PART I — Batch 070 재사용 체크리스트

1. accounting short는 cumulative earnings와 tangible book을 reconcile한다.
2. short에는 catalyst clock과 maximum adverse excursion을 기록한다.
3. income-trust yield를 downside floor로 자동 간주하지 않는다.
4. M&A 가능성이 아니라 takeout price를 검증한다.
5. medical-device moat는 installed base와 procedure utilization을 분리한다.
6. 좋은 earnings와 좋은 stock return을 별도 score로 둔다.
7. emerging-market growth는 country-risk multiple을 별도 변수로 둔다.
8. cyclical short는 commodity/customer-income cycle을 함께 본다.
9. 안정적 business cash flow와 refinancing 가능성을 혼동하지 않는다.
10. 동일 기업의 다른 entry price는 완전히 다른 thesis가 될 수 있다.
11. 미래 terminal target은 현재 checkpoint와 별도 표시한다.
12. post-reorg equity는 debt reset과 cycle sensitivity를 함께 본다.

---

## 12. Batch 070 핵심 한 줄

> **이번 배치의 공통점은 “기업을 맞히는 것”과 “증권을 맞히는 것”의 차이다. Carl Zeiss와 Afya는 좋은 사업이지만 Long이 실패했고, AUTO1은 같은 회사도 €31.6과 €11에서 결과가 갈렸으며, Algoma는 파산 뒤 자본구조 reset이 약 17배 equity convexity를 만들었다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_070_afsi_aft_afx_afya_ag_ag1_aga_10.md`
- Overlay: `data/curated/batch_070_afsi_aft_afx_afya_ag_ag1_aga_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
