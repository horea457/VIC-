# Batch 069 — AFMI / Alphamin / Ag Growth / AFOP / Aluflexpack / AFR / AfriSam / Affirm / AmTrust V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 068 마지막 **AFI 2021-08-25** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **3건(AFN.UN 2004, AFR 2003, AFRISJ 2010)**. AFRISJ는 common equity가 아니라 **AfriSam senior secured floating-rate notes** Long이다. AFOP 두 vintage는 2010 1-for-5 reverse split과 2013 2-for-1 split을 보정했다. source DB performance row는 10건 모두 없어 corporate action·operating outcome·split-adjusted price를 우선했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2008-06-04 | AFMI.OB | Long | **Affinity Media SPAC Common Long** | [AFMI](ideas/2008/2008-06-04_AFMI_OB_long.md) | **부분 성공 — merger 실패, trust floor 성공** |
| 2 | 2021-01-10 | AFMJF | Long | **Alphamin Common Long** | [Alphamin](ideas/2021/2021-01-10_AFMJF_long.md) | **매우 강한 성공 — de-risking·Mpama South·배당** |
| 3 | 2004-10-12 | AFN.UN | **Short** | **Ag Growth Income Fund Long** | [Ag Growth](ideas/2004/2004-10-12_AFN_UN_long.md) | **강한 성공 — distribution + niche industrial compounding** |
| 4 | 2010-05-26 | AFOP | Long | **AFOP Common Long** | [AFOP 2010](ideas/2010/2010-05-26_AFOP_long.md) | **매우 강한 성공 — split-adjusted ~$3.38→$18.50 + dividends** |
| 5 | 2012-08-07 | AFOP | Long | **AFOP Common Long** | [AFOP 2012](ideas/2012/2012-08-07_AFOP_long.md) | **매우 강한 성공 — split-adjusted ~$4.65→$18.50 + cash distribution** |
| 6 | 2022-05-29 | AFP SW | Long | **Aluflexpack Common Long** | [Aluflexpack](ideas/2022/2022-05-29_AFP_SW_long.md) | **운영 성공 / security outcome 혼합** |
| 7 | 2003-12-11 | AFR | **Short** | **American Financial Realty Trust Long** | [AFR](ideas/2003/2003-12-11_AFR_long.md) | **실패 — asset growth without per-share value creation** |
| 8 | 2010-11-01 | AFRISJ | **Short** | **AfriSam Senior Secured FRN Long** | [AfriSam FRN](ideas/2010/2010-11-01_AFRISJ_secured_frn_long.md) | **구조조정 성공 / exact recovery 미확정** |
| 9 | 2021-02-08 | AFRM | Short | **Affirm Common Short** | [Affirm Short](ideas/2021/2021-02-08_AFRM_short.md) | **매우 강한 성공 — $122→$30 target 이하** |
| 10 | 2010-01-13 | AFSI | Short | **AmTrust Common Short** | [AmTrust Short](ideas/2010/2010-01-13_AFSI_short.md) | **실패 — governance 우려는 후행 적중, short path 치명적** |

---

# PART A — AFMI: upside를 틀려도 구조가 맞으면 돈을 지킬 수 있다

## 2. Affinity Media SPAC 2008

원문:
- entry 약 **$5.85**
- Hotels at Home merger 성공 시 effective cost basis 약 **$3.84**
- end-2009 target **$7.60**
- 실패 시 trust liquidation **$6+**

실제:
- merger vote 실패
- transaction abandoned
- IPO common 1주당 **$6.00 cash + residual common 1/7주**

### 핵심

기업분석은 틀렸지만 **security structure**가 투자결과를 보호했다.

> **SPAC common에서는 target business보다 trust floor가 더 중요한 경우가 있다.**

---

# PART B — Alphamin: 운영 bottleneck 제거가 asset quality를 드러내다

## 3. 2021 Long

원문:
- Mpama North, 세계 최고품위 수준 tin mine
- post-tax NPV8 대비 **48% discount**
- FTR plant
- 2021 debt-free 목표
- Mpama South optionality
- 20%+ forward dividend yield 가능성

실제:
- debt reduction
- dividend 시작
- Mpama South resource → development → 2024 commissioning
- 2025 tin production **18,576t**
- 2025 dividends **C$0.11/share**
- 2026 guidance 약 **20kt**

DRC security risk도 2025 실제 운영중단으로 나타났지만 장기 expansion thesis를 무너뜨리지는 않았다.

> **좋은 광산은 grade만으로 돈을 버는 것이 아니라 recovery·logistics·management가 정상화될 때 가치가 폭발한다.**

---

# PART C — Ag Growth: “농기계”라는 라벨이 숨긴 replacement compounder

## 4. AFN.UN 2004

원문:
- cash distribution **11.5%**
- double-digit FCF yield
- EBITDA margin **30%+**
- EBITDA-capex margin **29%+**
- market share **35%**, next competitor의 약 3배
- CEO net worth 90% invested

실제:
- 2005 Edwards acquisition
- 2005 H1 revenue **C$40.4m**, EBITDA **C$12m**
- distribution >8% 추가 인상
- 2007 revenue **C$130.7m**, EBITDA **C$32.4m**
- Hi Roller, Twister, Union Iron 등 bolt-on M&A 지속

### 핵심

농산물 가격보다 grain throughput과 교체주기에 노출된 high-margin niche equipment business였다.

---

# PART D — AFOP 두 번: 현금이 downside, secular growth와 M&A가 upside

## 5. 2010 Long

entry:
- **$1.35** pre 1-for-5 reverse split
- cash $0.97/share
- EV ~$16m

corporate actions:
- 2010 **1-for-5 reverse split**
- 2013 **2-for-1 split**
- 2016 Corning **$18.50 cash/share**

2016 share basis entry:

**$1.35 × 5 / 2 = $3.375**

takeout multiple:

**$18.50 / $3.375 ≈ 5.48x**

## 6. 2012 Long

entry:
- $9.29 pre-2013 split
- net cash $5.70/share
- tangible book $7.20/share
- TEV/EBIT ~5x

실제:
- 2012 **$1.25/share cash distribution**
- 2013 2-for-1 split
- 2016 $18.50 cash takeout

2016 share basis entry:

**$9.29 / 2 = $4.645**

takeout multiple:

**$18.50 / $4.645 ≈ 3.98x**

> **split과 special dividend를 보정하지 않은 historical return은 의미가 없다.**

---

# PART E — Aluflexpack: operating forecast가 맞아도 주식은 별개다

## 7. 2022 Long

원문 2025:
- revenue **€425m**
- EBITDA margin **14%**
- EBITDA **~€59.5m**

실제 2023:
- revenue **€380.3m**
- EBITDA 약 **€51m**

운영적으로 상당히 빠른 성장이었다.

그러나 Constantia의 최종 takeover는 **CHF16/share**였다. 원문 당시 public valuation과 비교하면 shareholder outcome은 운영성과만큼 좋지 않았다.

> **좋은 forecast와 좋은 IRR은 같은 문장이 아니다.**

---

# PART F — AFR: 자산을 늘려도 주당가치는 줄 수 있다

## 8. American Financial Realty Trust 2003

entry:
- price **~$16**
- dividend $1
- AFFO target $1.30~1.40
- target **$19~20**

원문은 금융기관 sale-leaseback을 통해 빠른 balance-sheet growth를 기대했다.

실제 2007 Gramercy merger:
- **$5.50 cash**
- **0.12096 GKK share**
- announcement-day implied value 약 **$8.43**
- closing 때 $0.2419 special-dividend adjustment 추가

규모성장은 있었지만 per-share value creation은 실패했다.

> **REIT에서 asset growth는 KPI가 아니라 input이다. 핵심은 NAV/share와 AFFO/share다.**

---

# PART G — AfriSam: 나쁜 회사에서 좋은 채권을 살 수 있다

## 9. 2010 Senior Secured FRN

원문:
- notes **75~80c**
- issuer leverage 약 **7x**
- market-price leverage 약 **3.5x EBITDA**
- base return **14~15% annual**
- restructuring catalyst

실제:
- PIC + 80%+ noteholders restructuring support
- debt >R15bn 감축
- large debt-to-equity conversion
- remaining senior debt 약 **€392m** new notes로 roll

정확한 final holder IRR은 공개자료로 완전히 복원되지 않지만 **bankruptcy avoidance와 senior claim preservation**은 적중했다.

---

# PART H — Affirm vs AmTrust: Short에서 “맞음”보다 timing이 중요하다

## 10. Affirm 2021 Short

entry:
- **$122**
- target **$30**
- 33x 2022 sales
- Peloton concentration
- subprime/credit
- BNPL competition
- stimulus normalization

실제:
- Peloton revenue share FY2021 ~20% → FY2022 ~8%
- 2022 low close 약 **$8.91**
- 이후 business survives and stock rebounds

original short horizon에서는 매우 강한 성공.

## 11. AmTrust 2010 Short

entry price 수준 약 **$12**.

원문:
- related-party Maiden economics
- family control
- abnormal ROE
- governance/accounting catalyst

실제:
- 2011 ~$19
- 2012 ~$27
- 2017 restatement/internal-control issues
- 2018 take-private **$14.75**

### 비교

| 구분 | Affirm | AmTrust |
|---|---|---|
| thesis issue | valuation + concentration + macro | governance/accounting |
| catalyst speed | 빠름 | 매우 느림 |
| initial path | 큰 하락 | 2배 이상 상승 |
| long-run concern | 일부 완화/사업 생존 | 일부 현실화 |
| 투자결과 | 강한 성공 | 실패 |

> **Short는 종착점보다 경로 의존성이 훨씬 크다.**

---

# PART I — Batch 069 공통 분석식

### SPAC

**Common value = trust cash + residual shell value + transaction optionality**

### Mining

**FCF = commodity price × recovered tonnes - mining/processing/logistics costs - capex - tax**

### Niche Industrial

**FCF quality = replacement demand × market share × margin - maintenance capex**

### Cash-rich Tech

**EV = market cap - excess cash**

그리고 split/dividends를 반드시 보정한다.

### REIT

**Per-share value creation = ΔAFFO/share + ΔNAV/share + dividends**

asset growth alone ≠ shareholder growth.

### Distressed Credit

**Recovery = stressed enterprise/collateral value - senior/equal claims**

### Short

**Expected payoff = fundamental downside × catalyst probability - path/borrow/squeeze risk**

---

# PART J — Batch 069 재사용 체크리스트

1. SPAC common과 warrant를 분리한다.
2. trust liquidation value를 downside case에 직접 넣는다.
3. mining은 grade와 recovery를 분리한다.
4. jurisdiction risk는 실제 operating shutdown scenario로 모델링한다.
5. distribution yield는 maintenance capex 차감 후 검증한다.
6. reverse/forward split을 전부 보정한다.
7. special dividend는 raw price return과 분리한다.
8. operating forecast와 shareholder IRR을 따로 판정한다.
9. REIT는 asset growth 대신 AFFO/share와 NAV/share를 본다.
10. distressed credit은 issuer story보다 security waterfall을 우선한다.
11. short thesis에는 catalyst time과 maximum adverse excursion을 포함한다.
12. 장기적으로 우려가 맞아도 short path가 먼저 치명적이면 실패다.

---

## 12. Batch 069 핵심 한 줄

> **같은 “논지가 맞았다”라도 security 구조와 시간축이 다르면 수익은 정반대다. AFMI는 기업 이벤트가 틀려도 trust floor가 지켰고, Affirm은 빠른 repricing으로 성공했지만 AmTrust는 훗날 governance 우려가 현실화돼도 short가 먼저 두 배 역행했다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_10.md`
- Overlay: `data/curated/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
