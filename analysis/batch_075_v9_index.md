# Batch 075 — Argan / Argosy Gaming / Allergy Therapeutics / Agilysys / Accretive Health V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. VIC 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 074 마지막 **AGX 2000-09-21 Agribrands International** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.
> **핵심 데이터 품질:** raw Short→actual Long **3건(AGX 2019, AGY 2002, AGYS 2013)**. Batch 74의 AGX 2000은 Agribrands였지만 Batch 75의 AGX 2013~2019는 실제 **Argan Inc.**로 ticker reuse 경계를 확인했다. Source SQL performance row는 이번 10건 모두 없다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2013-05-20 | AGX | Long | **Argan Common Long** | [Argan 2013](ideas/2013/2013-05-20_AGX_argan_long.md) | **매우 강한 성공 — Moxie financing/NTP + ~70% 2013 YE** |
| 2 | 2015-05-10 | AGX | Long | **Argan Common Long** | [Argan 2015](ideas/2015/2015-05-10_AGX_argan_long.md) | **운영 강한 성공 / 6M timing 실패 / 18M 대성공** |
| 3 | 2016-04-12 | AGX | Long | **Argan Common Long** | [Argan 2016](ideas/2016/2016-04-12_AGX_argan_long.md) | **매우 강한 성공 — $59 target를 1년 내 초과** |
| 4 | 2019-08-07 | AGX | **Short** | **Argan Common Long** | [Argan 2019](ideas/2019/2019-08-07_AGX_argan_long.md) | **명확한 실패 — backlog/NTP timing 과대평가** |
| 5 | 2002-12-23 | AGY | **Short** | **Argosy Gaming Common Long** | [Argosy](ideas/2002/2002-12-23_AGY_argosy_gaming_long.md) | **강한 성공 — Penn National $47 cash** |
| 6 | 2007-04-03 | AGY.L | Long | **Allergy Therapeutics Common Long** | [Allergy Therapeutics](ideas/2007/2007-04-03_AGY_L_allergy_therapeutics_long.md) | **near-term 실패 — FDA clinical hold** |
| 7 | 2007-10-04 | AGYS | Long | **Agilysys Common Long** | [Agilysys 2007](ideas/2007/2007-10-04_AGYS_long.md) | **강한 실패 — roll-up/capital allocation 붕괴** |
| 8 | 2013-06-03 | AGYS | **Short** | **Agilysys Common Long** | [Agilysys 2013](ideas/2013/2013-06-03_AGYS_long.md) | **SOTP 부분 성공 / sale catalyst 실패** |
| 9 | 2016-02-03 | AGYS | Long | **Agilysys Common Long** | [Agilysys 2016](ideas/2016/2016-02-03_AGYS_long.md) | **event 실패 / 장기 SaaS fundamental 성공** |
| 10 | 2012-06-06 | AH | Long | **Accretive Health Common Long** | [Accretive Health](ideas/2012/2012-06-06_AH_accretive_health_long.md) | **near-term 실패 — accounting/delisting, franchise는 생존** |

---

# PART A — Argan 2013~2019: Backlog는 금액보다 Quality가 중요하다

## 2. 2013 — Financing/NTP가 빠르게 닫힌 Backlog

entry **$16.19**.

원문:
- cash ~$175m / ~$13 per share
- 1.6x LTM EV/EBITDA
- Moxie Liberty + Patriot
- backlog >$900m 가능
- 1.1x forward EV/EBITDA

실제:
- Liberty financing/sale: 2013-08
- Patriot financing/sale: 2013-12
- full notice to proceed
- FY2014 Moxie-related fee/note receipts 약 $37.9m
- 2013 YE stock **~$27.56**

price-only 약 **+70%**.

### 핵심

> 계약이 아니라 **financing + full NTP + cash receipt**까지 연결된 backlog가 좋은 backlog다.

---

## 3. 2015 — Operating thesis는 맞고 Catalyst Clock만 틀렸다

원문:
- new bookings ~$1.4bn
- cumulative EBITDA ~$210m
- normalized EPS ~$3
- target **$50 in ~6 months**

실제:
- FY2016 revenue $413.3m / EBITDA $62.9m
- FY2017 revenue $675.0m / EPS **$4.50**
- 2015 YE stock ~$32.40
- 2016 YE **$70.55**

즉 6개월 target은 실패했지만 operating denominator는 오히려 초과 달성했다.

---

## 4. 2016 — 가장 좋은 Backlog Vintage

원문:
- backlog ~$1.5bn
- 5 major projects
- ~$120m FCF / ~$8 per share over 9 quarters
- target **$59**
- expected IRR 38% / 2 years

실제:
- FY2017 EPS **$4.50**
- 2016 high ~$75.35
- 2016 YE **$70.55**

**target를 1년 안에 초과.**

---

## 5. 2019 — Headline Backlog를 Revenue로 너무 빨리 환산

원문:
- price ~$40
- net cash ~$19/share
- backlog $1.4bn → expected $2.5bn
- revenue ~$200m → **>$1bn**
- EPS FY21 $5.60 / FY22 $7.50 / FY23 $7.10
- target $70~80

실제:
- FY2020 EPS **-$2.73**
- FY2021 **$1.51**
- FY2022 **$2.40**
- FY2022 revenue **$509.4m**
- 2022 YE stock mid-$30s

### 네 vintage 비교

| Vintage | Backlog Quality | Forecast | 결과 |
|---|---|---|---|
| 2013 | financing/NTP imminent | 보수적 | 매우 성공 |
| 2015 | execution visibility 높음 | timing 공격적 | 운영 성공 |
| 2016 | project-by-project visibility 높음 | cash bridge 구체적 | 매우 성공 |
| 2019 | headline awards 큼, start-date 불확실 | revenue/EPS 급증 | 실패 |

### 공통식

**Probability-adjusted backlog = contract value × financing probability × NTP probability × schedule factor**

---

# PART B — Argosy Gaming: Regulatory Fear + Strategic Value

## 6. 2002 Long

raw SQL은 Short지만 original은 명백한 Long.

원문:
- 7.25x earnings
- 5.6x EBITDA
- <7x FCF ex growth capex
- gaming-tax fear
- buyback / deleveraging
- acquisition candidate

실제:
- 2004 Penn National acquisition
- **$47 cash/share**
- enterprise value 약 $2.2bn including debt

2002 Q4 trading range가 $16.49~24.29였으므로 terminal strategic value는 entry 대비 매우 큰 premium이었다.

---

# PART C — Allergy Therapeutics: Base Business가 Pipeline Burn을 떠안는다

## 7. 2007 Long

원문:
- implied price ~£1.04
- core European business ~70p
- pipeline optionality ~34p
- Pollinex Quattro 4-shot vaccine
- U.S. Phase III
- partnership / FDA approval

실제:
- 2007-07 FDA clinical hold
- FY2007 R&D **£25.3m**
- operating loss **£26.8m**
- hold는 **2012**에야 해제

### 핵심

원문은:

**equity floor = core business value**

처럼 봤지만 실제는:

**equity floor = core business value - pipeline burn - financing/dilution cost**

였다.

---

# PART D — Agilysys 2007~2016: 같은 회사, 세 번 다른 Thesis

## 8. 2007 — Cash-rich Roll-up 실패

원문:
- KSG sale $485m
- ~$170m net cash
- 20% self-tender
- revenue $1bn→$1.5bn
- 6% EBITDA / 15% ROIC
- SOTP $27 / 3~5Y mid-$50s

실제:
- 2008 YE stock **~$4.27**
- 2011 TSG, FY2011 revenue의 약 70%, **$64m cash**에 매각
- 전략을 hospitality software로 다시 전환

### 교훈

> **Cash value는 capital allocation quality를 곱한 값이다.**

---

## 9. 2013 — Divestiture SOTP는 맞고 Sale Catalyst는 틀림

원문:
- price < $12
- RSG sale net proceeds ~$36m
- post-sale cash ~$4.90/share
- no debt
- SOTP **$13.60~17.95**
- MAK Capital ~31% → company sale 기대

실제:
- RSG sale 2013-07-01 완료
- 2013 YE stock **$13.92**
- 2014 high **$15.25**
- company sale은 없음

SOTP는 상당 부분 실현됐지만 value-realization path는 sale이 아니라 독립 성장으로 바뀌었다.

---

## 10. 2016 — 12~18M Sale 실패, SaaS는 장기 성공

원문:
- stock ~$10
- sale ~$15 / 50%+ premium
- 12~18개월
- cash ~$60m
- NOL ~$175m
- recurring revenue growth
- valuation 1.3x EV/Sales vs sale 2x

실제:
- FY2016 recurring revenue $60.1m / 50%
- subscription Q4 +33%
- 2016 YE $10.36
- 2017 YE $12.28
- sale 없음
- 이후 hospitality SaaS가 장기간 크게 성장

### 세 vintage 비교

| Vintage | 핵심 thesis | 결과 |
|---|---|---|
| 2007 | cash + distribution roll-up | 실패 |
| 2013 | divestiture + SOTP + sale | SOTP 성공 / sale 실패 |
| 2016 | SaaS quality + near-term sale | event 실패 / business 성공 |

> **좋은 사업이라는 가설과 곧 팔릴 것이라는 가설은 분리해야 한다.**

---

# PART E — Accretive Health: Headline Legal Risk가 진짜 Tail Risk가 아니었다

## 11. 2012 Long

entry **$11.48**.

원문:
- Minnesota AG/Fairview controversy overdone
- revenue ~$1bn
- adjusted EBITDA run-rate ~$100m
- net cash >$200m
- mature contracts 15~18% EBITDA margin
- revenue ~$2bn / EBITDA ~$300m potential

실제:
- Fairview revenue impact ~$62~68m
- Minnesota settlement ~$2.49m
- legal issue 자체는 existential하지 않았음
- 그러나 2009~12 financial statements restatement
- filing delays
- **2014 NYSE suspension/delisting**

이후:
- 2015 Ascension 10-year exclusive partnership
- >$8bn new NPR opportunity
- Ascension/TowerBrook ~$200m strategic investment

### 핵심

> 원문이 집중한 **legal headline은 생각보다 작았고, accounting credibility가 더 큰 tail risk**였다.

Core franchise는 장기적으로 살아남았지만 original public-equity path는 실패했다.

---

# PART F — Batch 075 공통 분석식

### EPC Contractor

**Expected backlog value = contract value × financing probability × NTP probability × schedule factor**

### Regulatory Biotech

**Equity floor = core-business value - pipeline burn - financing/dilution cost + risk-adjusted pipeline NPV**

### Cash-Rich Roll-up

**Per-share value = current assets + acquisition NPV × capital-allocation skill**

### Strategic-Sale Thesis

**Expected value = standalone value + sale probability × strategic premium**

### Controversy Long

**Expected loss = headline-event loss + second-order governance/accounting/control loss**

---

# PART G — Batch 075 재사용 체크리스트

1. historical ticker identity를 날짜별 legal entity로 재확인한다.
2. raw Short/Long을 원문으로 감사한다.
3. EPC backlog를 financing/NTP-adjusted backlog로 바꾼다.
4. backlog 금액과 revenue timing을 별도 변수로 둔다.
5. catalyst timing을 operating forecast와 분리한다.
6. regulatory pipeline SOTP에서 future burn을 차감한다.
7. cash-rich company는 management capital-allocation record를 본다.
8. activist ownership을 sale probability 100%로 두지 않는다.
9. strategic value와 near-term sale event를 분리한다.
10. controversy investment에서는 headline issue 밖의 accounting/governance risk를 찾는다.
11. later franchise validation을 original security success로 소급하지 않는다.
12. exact performance row가 없으면 corporate actions와 dated operating facts로 판정한다.

---

## 12. Batch 075 핵심 한 줄

> **이번 배치는 “가치가 있느냐”보다 “그 가치가 어떤 경로와 시점으로 주주에게 도달하느냐”가 중요하다는 사례다. Argan은 NTP가 경로였고, Agilysys는 예상한 매각 대신 SaaS 성장이 경로였으며, Accretive Health는 franchise value가 살아 있어도 accounting path가 equity를 훼손했다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_075_agx_agy_agys_ah_10.md`
- Overlay: `data/curated/batch_075_agx_agy_agys_ah_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
