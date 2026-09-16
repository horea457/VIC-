# Batch 066 — Aetna / Applied Extrusion / Aether / Ampex / ADDvantage / AudioEye V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-17.
> **Batch boundary:** Batch 065 마지막 AES 2020-09-18 이후 ticker/date ordering을 유지한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **3건(AET 2000, AET 2009, AETC 2001)**. AETH 2001은 common이 아니라 **Aether Systems 6% convertible subordinated notes due 2005**로 security type을 교정했다. 이번 10건은 SQL performance row가 없어 transaction consideration, redemption, bankruptcy treatment, SEC stock-range와 운영실적을 사용했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 방향 / Security | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2000-06-02 | AET | **Short** | **Aetna Common Long** | [AET 2000](ideas/2000/2000-06-02_AET_long.md) | **breakup catalyst 성공 / $134 bull SOTP 미실현** |
| 2 | 2006-12-22 | AET | Long | **Aetna Common Long** | [AET 2006](ideas/2006/2006-12-22_AET_long.md) | **EPS forecast 성공 / $65 multiple thesis 실패** |
| 3 | 2009-01-16 | AET | **Short** | **Aetna Common Long** | [AET 2009](ideas/2009/2009-01-16_AET_long.md) | **2009 earnings 실패 / $44 target 2년 뒤 지연 달성** |
| 4 | 2001-06-12 | AETC | **Short** | **Common Long** | [AETC](ideas/2001/2001-06-12_AETC_long.md) | **강한 실패 — refinance 성공 뒤 common wipeout** |
| 5 | 2001-04-29 | AETH Corp | Long | **6% Convertible Notes Long** | [Aether Convert](ideas/2001/2001-04-29_AETH_convert_long.md) | **강한 성공 — 59 entry, 101.2 redemption + coupons** |
| 6 | 2005-02-01 | AEXCA | Long | **Ampex Common Long** | [Ampex](ideas/2005/2005-02-01_AEXCA_long.md) | **강한 실패 — IP royalty thesis 뒤 common cancellation** |
| 7 | 2010-09-02 | AEY | Long | **ADDvantage Common Long** | [AEY 2010](ideas/2010/2010-09-02_AEY_long.md) | **근거리 부분 성공 / 장기 terminal 실패** |
| 8 | 2013-01-18 | AEY | Long | **ADDvantage Common Long** | [AEY 2013](ideas/2013/2013-01-18_AEY_long.md) | **partial rerating / $4~5 실패 / NCAV floor 실패** |
| 9 | 2018-03-21 | AEY | Long | **ADDvantage Common Long** | [AEY 2018](ideas/2018/2018-03-21_AEY_long.md) | **tactical 부분 성공 / liquidation-value thesis 실패** |
| 10 | 2020-08-17 | AEYE | Long | **AudioEye Common Long** | [AudioEye](ideas/2020/2020-08-17_AEYE_long.md) | **가격 조기 성공 / 3~4Y growth duration 과대** |

---

# PART A — Aetna 세 번: EPS를 맞혀도 주가는 틀릴 수 있다

## 2. 2000 Aetna — SOTP는 transaction으로 검증

원문은 Aetna를 하나의 보험사가 아니라 **Financial Services + Health Care**로 분해했다.

- 당시 market cap 약 **$9.8bn**
- Financial Services 기대가치 약 **$9bn**
- low case 약 **$68/share**
- bull case 약 **$134/share**

실제 ING transaction:
- gross deal value 약 **$7.7bn**
- 주주 cash 약 **$35.33/share**
- + new Aetna health company 1 share

### 판정
breakup catalyst는 매우 강하게 적중했다. 그러나 remaining health stub가 원문 bull valuation만큼 즉시 높게 거래되지는 않았다.

> **SOTP의 한 leg가 현금화돼도 다른 leg의 높은 multiple까지 자동 검증되는 것은 아니다.**

---

## 3. 2006 Aetna — EPS는 거의 정확, 주가목표는 실패

원문:
- 2008E EPS **$3.83**
- FCF/share **$3.60**
- target multiple **17x**
- implied value **$65**

실제:
- 2008 operating EPS **$3.93**
- 2008 high 약 **$59.19**
- 2008 year-end **$28.50**

즉 earnings forecast는 매우 정확했지만 GFC와 underwriting/investment risk premium으로 multiple이 붕괴했다.

> **분모 예측 성공 ≠ valuation regime 예측 성공.**

---

## 4. 2009 Aetna — 낮은 P/E의 E가 먼저 무너졌다

원문:
- price ~$25
- 2009 Street EPS **$4.03**
- target **$44 @ 11x**
- membership growth + buyback 기대

실제 2009:
- operating EPS **$2.75**
- commercial MBR **80.3% → 84.5%**
- membership 약 **+1.2m**
- repurchase 약 **$773m**

2011에는 operating EPS **$5.17**, stock high 약 **$46**으로 결국 $44 target를 넘었다.

### 핵심
**membership/share gain이 있어도 underwriting margin이 무너지면 EPS는 줄 수 있다.** 가격목표 지연 달성을 near-term thesis 성공으로 바꾸지 않는다.

---

# PART B — AETC vs Aether: refinancing과 security selection

## 5. Applied Extrusion 2001 — refinancing 성공, equity 실패

@ 약 **$6.10**.

원문:
- 0.9x tangible book
- 0.28x sales
- FY02 EPS **$1.50** 기대
- $150m maturity/refinancing risk

실제:
- **$275m 10.75% senior notes due 2011** 발행 → refinancing 성공
- FY2002 EPS **-$2.55**
- 2004 Chapter 11
- 2005 기존 common **100% cancellation**

> **만기를 연장하는 것은 earning power를 만드는 것이 아니다.**

---

## 6. Aether 6% Convert 2001 — 같은 distress라도 좋은 security는 살아남았다

Security:
**6% convertible subordinated notes due 2005**.

Entry:
- bond price 약 **59**
- conversion price **$243.95** vs common ~$13.89 → option 사실상 무가치
- current yield 약 **10.2%**

실제:
- 2004-10-04 outstanding notes를 **101.2% of par + accrued interest**로 redemption

원문의 20%+ annual-return expectation과 방향상 정합적이다.

### 핵심 비교

| 항목 | AETC Common | Aether Convert |
|---|---|---|
| Catalyst | refinancing | cash survival/redemption |
| Catalyst 결과 | 성공 | 성공 |
| Operating business | 실패 | 혼합/비핵심 |
| Security payoff | **wipeout** | **101.2 + coupons** |
| 교훈 | refinance ≠ solvency | security selection이 company quality보다 중요 |

---

# PART C — Ampex: 높은 IP margin이 common floor는 아니다

## 7. AEXCA 2005

원문은:
- digital-imaging licensing
- specialty storage/DoD recorder
- licensing cash로 debt paydown
- minimum EPS 약 **$6.25**

을 제시했다.

실제:
- patent/royalty duration과 debt 부담이 common을 압박
- 2008 Chapter 11
- existing Class A common cancellation

### 핵심

`royalty cash PV - litigation/tax - debt claims = residual equity`

로 봐야 한다. high-margin licensing EPS를 perpetual annuity처럼 multiple화하면 안 된다.

---

# PART D — ADDvantage 세 번: NCAV가 왜 녹는가

## 8. Three-vintage comparison

| Vintage | Entry thesis | 후속 price behavior | 장기 결과 | 판정 |
|---|---|---|---|---|
| 2010 | ~$2.94, cycle recovery / low P/E | 2011 high ~$3.90 | 2024 Chapter 7 | tactical 부분 성공 |
| 2013 | $2.17, 61% TBV / 79% NCAV | 2014 high ~$3.55 | 2024 Chapter 7 | partial rerating, target 실패 |
| 2018 | $1.32, NCAV $1.89 / TBV $2.59 | 2018~19 high ~$2.20 | 2024 Chapter 7 | tactical 부분 성공, floor 실패 |

### 왜 asset floor가 사라졌나

NCAV는 정적 숫자가 아니다.

`cash + collectible receivables + realizable inventory - liabilities - wind-down costs`

로 다시 계산해야 한다.

- cable equipment inventory는 obsolete될 수 있다.
- receivable quality가 바뀐다.
- operating losses가 cash를 태운다.
- acquisitions/사업전환이 asset mix를 바꾼다.

> **liquidation catalyst가 없는 NCAV는 시간이 지나며 녹을 수 있다.**

---

# PART E — AudioEye: growth rate보다 duration

## 9. 2020 AEYE Long

당시:
- market cap 약 **$145m**
- LTM revenue 약 **$15.9m**
- MRR 약 **$1.6m**
- run-rate sales multiple 약 **7.5x**
- 3~4Y revenue expectation 약 **$50m**
- GM target 약 **75%**

실제:
- FY2020 revenue **$20.5m, +90%**
- YE2020 MRR 약 **$1.9m**, customers 약 **32k**
- Q4 GM **73%**
- 2021-02 stock high **$44.37**
- FY2024 revenue **$35.2m**, GM 약 **79%**
- FY2025 revenue **$40.3m**

### 판정

partner distribution과 gross-margin thesis는 강하게 맞았고 주가는 매우 빠르게 rerate됐다. 그러나 $50m revenue를 3~4년에 달성한다는 **growth-duration assumption**은 실패했다.

> **고성장 SaaS valuation에서 가장 민감한 변수는 TAM보다 성장률이 몇 년 지속되는가다.**

---

# PART F — Batch 066 공통 분석식

### Managed Care

`members × premium/member - medical claims - SG&A + investment income - tax = earnings`

membership growth와 MLR/MBR을 반드시 분리한다.

### Leveraged Industrial

`volume × unit spread - fixed costs - cash interest - maintenance capex = equity FCF`

refinancing 성공만으로 common floor를 만들지 않는다.

### Distressed Convert

`coupon + pull-to-par + redemption/conversion value - default haircut`

company quality보다 exact claim payoff가 먼저다.

### NCAV

`cash + haircut AR + haircut inventory - all liabilities - liquidation cost`

### SaaS

`customers × ARPU × gross margin - CAC/R&D/G&A = FCF`

현재 growth rate와 **duration**을 별도 가정한다.

---

# PART G — Batch 066 재사용 체크리스트

1. SOTP는 각 leg가 실제 주주에게 얼마로 현금화되는지 본다.
2. earnings forecast와 valuation-multiple forecast를 별도 점수화한다.
3. managed-care membership growth와 medical-cost margin을 분리한다.
4. refinancing은 liquidity를 개선하지만 solvency/earning power를 만들지 않는다.
5. distress에서는 common보다 더 나은 security가 있는지 먼저 본다.
6. patent royalty는 만기·license renewal·litigation을 계약별로 모델링한다.
7. NCAV inventory와 AR에는 asset-specific haircut을 둔다.
8. liquidation catalyst 없는 asset play는 시간가치를 차감한다.
9. 한 분기 turnaround earnings를 연율화하지 않는다.
10. SaaS는 growth rate와 growth duration을 분리한다.
11. target-price hit가 늦으면 원래 mechanism과 timing을 다시 판정한다.
12. terminal bankruptcy/corporate action이 있으면 stock chart보다 security treatment를 우선한다.

---

## 10. Batch 066 핵심 한 줄

> **좋은 숫자를 찾는 것보다 그 숫자가 어느 security에, 얼마나 오래, 어떤 multiple로 귀속되는지를 맞히는 것이 더 중요하다. Aetna는 EPS를 맞혀도 multiple이 틀렸고, AETC는 refinancing을 맞혀도 common이 0이 됐으며, Aether는 회사 turnaround를 못 맞혀도 discounted bond는 par 이상으로 회수됐다.**

## 11. 중복·정본 처리

- AET 2000/2006/2009는 같은 franchise지만 breakup, quality compounder, crisis value라는 서로 다른 thesis이므로 별도 canonical로 유지한다.
- AEY 2010/2013/2018은 동일 company지만 cycle-value, NCAV, liquidation-value entry가 달라 각각 보존한다.
- AETH는 ticker가 아닌 **6% convertible note security**가 실제 분석 단위다.

## 12. 앱 / DB 반영

- Wrapper: `analysis/batch_066_aetna_aetc_aether_ampex_aey_aeye_10.md`
- Overlay: `data/curated/batch_066_aetna_aetc_aether_ampex_aey_aeye_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
