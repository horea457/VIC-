# Batch 068 — AFCE / AFFY / AF Gruppen / Atlas Financial / AFH Financial / Armstrong Flooring V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 067 마지막 **AFCE 2011-03-25** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **3건(AFCE 2012, AFFY 2016, AFHIF 2021)**. AFHBL 2021은 common이 아니라 **Atlas Financial Holdings 6.625% Senior Unsecured Notes due 2022** Long이며, 2022년 새 2027 PIK-toggle notes로 교환됐다. SQL performance row는 10건 모두 없어 operating data, corporate actions, reverse split, bankruptcy treatment를 우선했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Entity / Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2012-04-20 | AFCE | **Short** | **AFC Enterprises Common Long** | [AFCE 2012](ideas/2012/2012-04-20_AFCE_long.md) | **매우 강한 성공 — $16.50→$79 cash** |
| 2 | 2016-08-30 | AFFY | **Short** | **Affymax Shell Common Long** | [AFFY](ideas/2016/2016-08-30_AFFY_long.md) | **실패 — NOL monetization catalyst 장기 미실현** |
| 3 | 2021-10-11 | AFG NO | Long | **AF Gruppen Common Long** | [AF Gruppen](ideas/2021/2021-10-11_AFG_NO_long.md) | **부분 실패 — quality는 유지, growth/margin/target 미달** |
| 4 | 2012-06-05 | AFH | Long | **Atlas Financial Common Long** | [Atlas 2012](ideas/2012/2012-06-05_AFH_long.md) | **강한 성공 — premium/book/price rerating** |
| 5 | 2013-09-22 | AFH | Long | **Atlas Financial Common Long** | [Atlas 2013](ideas/2013/2013-09-22_AFH_long.md) | **강한/부분 성공 — 2Y double, EPS target 과대** |
| 6 | 2021-12-29 | AFHBL | Long | **6.625% Senior Notes Long** | [Atlas Notes](ideas/2021/2021-12-29_AFHBL_notes_long.md) | **exchange 성공 / 2027 ultimate recovery 미확정** |
| 7 | 2021-04-12 | AFHIF | **Short** | **Atlas Financial Common Long** | [Atlas 2021 Common](ideas/2021/2021-04-12_AFHIF_long.md) | **강한 실패 — secured debt가 common residual 압도** |
| 8 | 2020-12-13 | AFHP LN | Long | **AFH Financial Group Common Long** | [AFH Financial](ideas/2020/2020-12-13_AFHP_LN_long.md) | **강한 성공 — 330p→480p cash** |
| 9 | 2016-09-21 | AFI | Long | **Armstrong Flooring Common Long** | [AFI 2016](ideas/2016/2016-09-21_AFI_long.md) | **강한 실패 — 2022 Chapter 11** |
| 10 | 2021-08-25 | AFI | Long | **Armstrong Flooring Common Long** | [AFI 2021](ideas/2021/2021-08-25_AFI_long.md) | **매우 강한 실패 — 8.5개월 내 Chapter 11** |

---

# PART A — AFCE 2012: turnaround가 compounder가 된 뒤에도 충분히 싸면

## 2. Popeyes 2012

2012 entry:
- price **$16.50**
- market cap ~$400m
- 2012E EBITDA ~$50m
- fair value **$22.50~28.15**

실제:
- FY2012 adjusted EPS **$1.24, +25%**
- global SSS **+6.9%**
- 141 openings / 66 net openings
- FY2013 adjusted EPS **~$1.43**
- 2017 RBI cash acquisition **$79/share**

단순 price multiple은 약 **4.79x**다.

### 핵심

2004 AFCE는 asset-sale special situation, 2007은 turnaround, 2011·2012는 **이미 회복된 asset-light franchisor의 compounding**이었다.

> **같은 회사라도 lifecycle stage가 바뀌면 싸다는 이유가 asset discount → turnaround → earnings compounding으로 이동한다.**

---

# PART B — AFFY: NOL face value는 기업가치가 아니다

## 3. Affymax 2016

원문:
- market cap 약 **$2.2m**
- federal NOL **~$481m**
- state NOL **~$491m**
- Jonathan Couchman이 profitable business를 reverse-merge할 가능성
- NOL의 일부만 monetization해도 큰 upside

실제:
- 수년이 지나도 meaningful value-unlocking transaction이 확인되지 않음
- 2020·2024 외부 SEC filings에서도 Couchman은 Affymax CEO로 계속 기재
- 2017 corporate tax-rate 하락으로 tax shield nominal economics도 낮아짐

### 핵심

NOL은 cash가 아니다.

**NOL value = usable taxable income × tax rate × Section 382 feasibility × timing discount**

> **microcap shell에서 “아무 일도 일어나지 않는 것”은 결과가 아니라 핵심 리스크다.**

---

# PART C — AF Gruppen: 좋은 회사와 좋은 주식의 차이

## 4. 2021 Long

원문 base:
- 2024 revenue **NOK36.7bn**
- EBIT margin **6.6%**
- p-weighted FV **NOK248**
- ~2년 15%대 CAGR

실제:
- 2024 revenue **NOK30.64bn**
- EBT **NOK1.085bn**, margin 3.5%
- 2025 revenue **NOK31.99bn**
- EBT **NOK1.653bn**
- backlog **NOK44.72bn**
- 2026-09 price 약 **NOK189**, 2021 entry 월간 가격 약 NOK197

quality, backlog, cash generation은 유지됐지만 original growth/margin path는 미달했다.

> **좋은 contractor는 장기 생존할 수 있어도, backlog가 예상한 margin으로 전환되지 않으면 starting valuation을 정당화하지 못한다.**

---

# PART D — Atlas Financial 네 개: 같은 기업, 완전히 다른 security outcomes

## 5. 2012 Common — specialty insurer rerating

원문 entry **$1.77 pre-split**.

2013 1-for-3 reverse split을 반영하면 약 **$5.31** equivalent다.

실제:
- 2013 gross premium written **$93.1m** vs original 2Y target ~$80m
- combined ratio 약 **94%대**
- BVPS 2013 **$6.54**
- BVPS 2014 **$9.08**
- BVPS 2015 **$10.15**
- 2015 high 약 **$20.97**

original horizon에서는 강한 성공.

## 6. 2013 Common — 가격은 맞고 earnings는 과대

entry **$9.85**.

원문:
- 2015 BVPS $11~12
- 2015 EPS ~$2
- FV $25~30

실제:
- 2015 BVPS **$10.15**
- EPS **$1.13**
- stock high **$20.97**

price는 약 **+113%**였지만 earnings denominator는 미달했다.

## 7. 2021 Common — insurer에서 MGA로 바뀌어도 debt는 남는다

원문:
- legacy insurance runoff 종료
- capital-light MGA pivot
- old premium base 일부 회복
- **10x+ common upside**

실제:
- 2022 unsecured notes maturity extension
- 2024 약 **$12.7m secured debt** 소멸을 위해 핵심 operating subsidiaries를 secured lender에 이전
- common residual economics 사실상 붕괴

### 핵심

**asset-light business ≠ asset-light security.**

holding-company debt stack을 빼고 난 뒤 common이 남아야 한다.

## 8. 2021 AFHBL Bond — restructuring completion과 recovery는 다르다

entry:
- $25 par
- market price 약 **$10**

실제:
- 2022 scheme approved
- old note cancelled
- each old $25 + accrued unpaid interest를 new 2027 notes principal로 exchange
- new coupon **6.625% cash / 7.25% PIK**
- maturity **2027-04-27**

2024 operating subsidiaries transfer는 credit deterioration의 경고다.

> **par-for-par distressed exchange는 par recovery가 아니라 claim maturity를 뒤로 미룬 것일 수 있다.**

---

# PART E — AFH Financial Group: external buyer가 6개월 안에 intrinsic value를 닫다

## 9. 2020 Long

entry:
- **330p**
- 약 10x P/E
- original fair value **500~600p**

실제:
- 2021-01 initial recommended bid **463p**
- 2021-03 increased bid **480p**
- 2021-06 scheme effective

단순 gain:

**480 / 330 - 1 ≈ +45.5%**

원문 target보다 약간 낮았지만 매우 짧은 기간에 현금화됐다.

---

# PART F — Armstrong Flooring: turnaround에서 가장 중요한 숫자는 runway

## 10. 2016 Long

원문:
- spin-off management focus
- LVT growth
- cost reductions
- 2017 EBITDA ~$100m / 2018 ~$120m 기대
- long-term ~10% EBITDA margin

실제:
- 2017 short bounce 이후 장기 deterioration
- 2022-05 Chapter 11
- North America **$107m**, Australia **$31m**, Asia **$59m** asset sales
- SEC: existing equity **likely no recovery**

강한 실패.

## 11. 2021 Long

entry 약 **$3.5**.

원문:
- FY2023 revenue ~$744m
- EBITDA ~$52m / 7% margin
- target **$12+**
- new CEO / sales reps / products / commercial recovery

실제:
- 약 **8.5개월 후 Chapter 11**
- normalized EBITDA에 도달하기 전에 liquidity가 끝남

### 핵심 식

turnaround에서 반드시 비교:

**cash runway / quarterly burn**  
vs  
**time-to-normalized EBITDA**

이번 경우:

**time-to-repair > liquidity runway**

---

# PART G — Batch 068 공통 분석식

### Franchisor

**Corporate FCF ≈ system sales × royalty rate + franchise fees - brand SG&A**

### NOL shell

**NOL value = usable taxable income × tax rate × legal usability × probability of transaction × timing discount**

### Contractor

**Expected profit = backlog × conversion rate × project margin - loss-making project tails**

### Specialty Insurance

**ROE = premium growth × underwriting margin + investment income - reserve development**

### Distressed Credit

**Recovery = market value of replacement securities + cash received**, not face principal.

### Manufacturing Turnaround

**Equity survives only if liquidity runway > time-to-operating normalization**

---

# PART H — Batch 068 재사용 체크리스트

1. reverse split을 historical returns에 반드시 반영한다.
2. insurer book value는 reserve assumptions가 맞을 때만 floor다.
3. rapid premium growth와 reserve tail risk를 동시에 본다.
4. distressed exchange에서 new face value를 recovery로 쓰지 않는다.
5. common과 bond를 security-level로 분리한다.
6. NOL face value를 현금처럼 할인하지 않는다.
7. event shell은 time-to-catalyst를 명시한다.
8. contractor backlog는 margin conversion까지 봐야 한다.
9. spin-off 자체를 catalyst로 취급하지 않는다.
10. turnaround 목표 EBITDA와 liquidity runway를 같은 timeline에 놓는다.
11. bankruptcy asset sales는 common recovery와 다르다.
12. corporate cash takeout은 external value validation으로 우선한다.

---

## 12. Batch 068 핵심 한 줄

> **이번 배치는 “좋은 사업 아이디어”보다 security와 시간축이 수익을 결정한다는 점이 선명하다. Atlas의 MGA pivot도 common은 실패했고 bond는 아직 미확정이며, Armstrong은 EBITDA 목표가 오기 전에 liquidity가 먼저 끝났다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_068_afce_affy_afg_afh_afhp_afi_10.md`
- Overlay: `data/curated/batch_068_afce_affy_afg_afh_afhp_afi_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
