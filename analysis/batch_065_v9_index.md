# Batch 065 — AerCap / Aerie Pharmaceuticals / Aeroméxico / AES V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-16.
> **Batch boundary:** Batch 064 마지막 AerCap 2014-01-27 이후 ticker/date ordering을 유지한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **1건(AES 2020)**. AerCap 2015~2022 **6개 구판 canonical을 V9 정본으로 승격**했다. AERI는 실제 Short로 raw 방향이 맞다. AERI·Aeroméxico는 SQL performance row가 없어 각각 cash takeout·bankruptcy treatment를 terminal payoff anchor로 사용했다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 방향 / Security | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2015-12-28 | AER | Long | **AerCap Common Long** | [AER 2015](ideas/2015/2015-12-28_AER_long.md) | **BV/EPS thesis 성공 / rerating 실패** |
| 2 | 2017-07-14 | AER | Long | **AerCap Common Long** | [AER 2017](ideas/2017/2017-07-14_AER_long.md) | **buyback·BVPS 성공 / valuation·COVID path 혼합** |
| 3 | 2018-06-21 | AER | Long | **AerCap Common Long** | [AER 2018](ideas/2018/2018-06-21_AER_long.md) | **2020 horizon 실패 — BV target 미달·2Y -41.6%** |
| 4 | 2019-02-06 | AER | Long | **AerCap Common Long** | [AER 2019](ideas/2019/2019-02-06_AER_long.md) | **liquidity/process 강한 성공 / volatile return** |
| 5 | 2020-08-17 | AER | Long | **AerCap Common Long** | [AER 2020](ideas/2020/2020-08-17_AER_long.md) | **매우 강한 성공 — 0.4x book crisis mispricing, 1Y +76.7%** |
| 6 | 2022-02-05 | AER | Long | **AerCap Common Long** | [AER 2022](ideas/2022/2022-02-05_AER_long.md) | **1Y 실패 / Russia loss 후 book·buyback 지연 회복** |
| 7 | 2016-02-11 | AERI | **Short** | **Aerie Pharmaceuticals Common Short** | [AERI 2016](ideas/2016/2016-02-11_AERI_short.md) | **TAM skepticism 일부 성공 / $15.25 takeout으로 terminal Short 실패** |
| 8 | 2017-11-01 | Aeromex | Long | **Grupo Aeroméxico Common Long** | [Aeroméxico 2017](ideas/2017/2017-11-01_Aeromex_long.md) | **강한 실패 — Chapter 11, old equity <0.01%** |
| 9 | 2009-10-15 | AES | Long | **Common Long** | [AES 2009](ideas/2009/2009-10-15_AES_long.md) | **실패 — EPS bridge 미달, 2Y -30.7%** |
| 10 | 2020-09-18 | AES | **Short** | **Common Long** | [AES 2020](ideas/2020/2020-09-18_AES_long.md) | **강한 성공 — EPS·IG·coal exit·Fluence catalysts 적중** |

---

# PART A — AerCap 6번: 같은 회사라도 entry price와 tail risk가 outcome을 바꾼다

## 2. Six-vintage comparison

| Vintage | 핵심 entry logic | 가장 중요한 예상 | 실제 결과 | 판정 |
|---|---|---|---|---|
| 2015 | ~1x book, ILFC integration | 2018 BVPS ~$60 / EPS $7~8 | BVPS $62.95 / EPS $6.83, 3Y -11% | 숫자 성공·multiple 실패 |
| 2017 | 0.9x book + below-book buyback | ROE + buyback → BVPS growth | 2019 BVPS $72.08, 3Y -38% | mechanism 성공·path 혼합 |
| 2018 | 0.8x book, contracted rents | 2020 BVPS $80~85 | $69.34, 2Y -41.6% | horizon 실패 |
| 2019 | 0.77x book, liquidity fear | funding runway 충분 | COVID에도 solvency 유지, 3Y +36.4% | process 강한 성공 |
| 2020 | ~0.4x book crisis entry | implied impairment 과도 | BVPS only -4%, 1Y +76.7% | 매우 강한 성공 |
| 2022 | GECAS accretion | ~$84 economic BV + buyback | Russia $2.7bn charge, 1Y -2.6%, 2023 BVPS $83.81 | 지연 성공 / 1Y 실패 |

### 가장 중요한 비교: 2015 vs 2020

2015는 **좋은 company at roughly book**이었다. BVPS forecast를 거의 정확히 맞혀도 P/B가 붙지 않아 주가가 실패했다.

2020은 **같은 company at ~0.4x book**이었다. 정상 earnings를 정밀하게 맞힐 필요가 없었다. 실제 book이 40~50% 파괴되지 않기만 해도 큰 upside가 생겼다.

> **같은 자산과 같은 management라도 price가 요구하는 impairment가 다르면 투자 난이도가 완전히 달라진다.**

---

## 3. AerCap에서 반복해서 확인된 분석식

### 평시

`opening BVPS + retained earnings + below-book buyback accretion + sale gains - impairments = ending BVPS`

### stress

`unrestricted liquidity + operating cash + financing capacity - maturities - purchase commitments - rent shortfalls = survival runway`

### equity return

`BVPS growth × exit P/B`가 아니라 정확히는:

`(ending BVPS × ending P/B + distributions) / entry price - 1`

따라서 BV forecast와 terminal multiple은 별도 claim이다.

---

# PART B — AERI: Fundamental Short가 맞아도 security Short는 질 수 있다

## 4. Aerie Pharmaceuticals 2016 Short

원문:
- entry 약 $14.16
- Rhopressa market이 bull의 ~$350m보다 **~$100m**에 가깝다고 판단
- commercialization salesforce/SG&A로 cash burn 증가
- dilution/convert risk

실제:
- Rhopressa FDA approval 2017
- Rocklatan approval 2019
- 2021 product revenue **$112.1m**
- 2021 net loss 약 $74.8m
- 2022 Alcon **$15.25/share cash acquisition**

즉 TAM size와 cash-burn skepticism은 상당히 맞았지만 **regulatory success + strategic takeout**이 common Short의 terminal payoff를 뒤집었다.

> **Short는 ‘내 fundamental forecast가 맞는가’뿐 아니라 누가 더 높은 strategic value를 지불할 수 있는가를 봐야 한다.**

---

# PART C — Aeroméxico: Strategic shareholder는 common floor가 아니다

## 5. Aeroméxico 2017 Long

원문:
- price MXN 32.7
- Delta가 약 MXN49 수준에 strategic stake
- Mexico aviation penetration growth
- Delta JV synergies ~$200m by 2021
- margin doubling / deleveraging
- 2019 fair value **MXN71.4**

실제:
- 2019에도 consolidated net loss
- 2020 revenue **-58.5%**
- Chapter 11
- 2022 emergence 시 기존 equity는 reorganized equity의 **0.01% 미만**

Delta는 post-reorg에도 partner로 남았지만 기존 common을 보호하지 않았다.

### 교훈

**Strategic value belongs first to the enterprise.** 높은 debt/lease claim이 있으면 그 value가 old common에 남는다는 보장은 없다.

---

# PART D — AES 2009 vs 2020: “프로젝트 성장”과 “측정 가능한 transformation”

## 6. AES 2009 Long — project MW를 EPS로 너무 빨리 번역

원문:
- 3,500MW construction program
- 96% contracted
- 2011 adjusted EPS **$1.20~1.30**
- target **$19~20**

실제:
- 2010 adjusted EPS **$0.94**
- 2011 adjusted EPS **$1.04**
- SQL 2Y **-30.7%**

non-recourse debt와 contracted projects는 solvency risk를 낮췄지만 parent EPS growth를 보장하지 않았다.

## 7. AES 2020 Long — milestone stack가 실제로 움직였다

원문:
- ~6GW renewables backlog
- adjusted EPS CAGR **7~9%** through 2022
- second investment-grade rating
- coal exposure <30%
- Fluence IPO/private mark
- target $32

실제:
- 2020-11 S&P **BBB-**
- year-end backlog **6.9GW**
- pro-forma coal exposure **25%**
- adjusted EPS $1.44 → $1.67, **~7.7% CAGR**
- Fluence 2021 IPO @ **$28**
- SQL 2Y **+52.8%**

### 핵심 차이

2009는 `MW under construction → future EPS`라는 긴 causal chain이었다.

2020은 `signed backlog + credit upgrade + coal mix + external Fluence mark`처럼 **각 단계가 관찰 가능한 catalyst**였다.

---

# PART E — Batch 065 재사용 체크리스트

1. 같은 company의 vintage를 합치지 말고 entry price·P/B·tail risk를 별도 기록한다.
2. book-value forecast와 exit multiple forecast를 분리한다.
3. aircraft lessor는 NTM maturities + purchase commitments vs liquidity를 계산한다.
4. contracted rent와 실제 collection certainty는 다르다.
5. crisis에서는 normal EPS보다 current price implied impairment를 계산한다.
6. jurisdiction risk는 legal ownership과 physical recoverability를 분리한다.
7. biotech Short는 FDA binary·borrow·M&A premium을 반드시 넣는다.
8. strategic investor의 과거 purchase price를 equity floor로 쓰지 않는다.
9. project-level contracted MW와 parent EPS 사이의 leakage를 계산한다.
10. transformation Long은 observable milestone sequence로 만든다.
11. original horizon failure와 delayed recovery를 섞지 않는다.
12. raw SQL direction은 original text와 audit해 교정한다.

---

## 8. Batch 065 핵심 한 줄

> **정확한 기업 예측보다 더 중요한 것은 어떤 claim을 어느 가격에 샀는가다. AerCap 2015는 BVPS를 거의 정확히 맞혀도 주가가 실패했지만, 2020의 0.4x book entry는 실제 book이 크게 파괴되지 않는 것만으로도 큰 수익이 났다.**

## 9. 중복·정본 처리

- AerCap 2015·2017·2018·2019·2020·2022는 기존 짧은 canonical을 같은 경로에서 **V9 정본으로 승격**했다.
- Batch 064의 AerCap 2014와 합치지 않는다. 2014~22 각 entry의 valuation regime과 risk state가 다르기 때문이다.
- AERI는 raw Short가 실제 Short이므로 방향을 교정하지 않았다.
- AES 2020만 raw Short를 original-text Long으로 교정했다.

## 10. 앱 / DB 반영

- Wrapper: `analysis/batch_065_aer_aeri_aeromex_aes_10.md`
- Staging catalog (DB 미반영): `data/staging/batch_065_aer_aeri_aeromex_aes_catalog_v9.json`
- Canonical source of truth: 위 10개 Markdown.
