# Batch 067 — AEZS / AF / AFC / AFCE V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> **Research as-of:** 2026-09-18.
> **Batch boundary:** Batch 066 마지막 **AEYE 2020-08-17** 이후 SQL의 `ticker/date/id` 정렬을 직접 파싱해 확정한 다음 10건.
> **핵심 데이터 품질:** historical ticker reuse 때문에 SQL `companies` table이 과거 entity를 덮어쓴 구간이다. **AF 2004·2006은 Astoria Financial, AF 2009·2014는 AlarmForce Industries; AFC 2002는 Allmerica Financial, AFC 2008은 Allied Capital 6.875% senior note**다. raw Short→actual Long **5건**, security-type correction **1건**이다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | SQL/raw | 실제 Entity / Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2016-07-25 | AEZS | Long | **Aeterna Zentaris Common Long** | [AEZS](ideas/2016/2016-07-25_AEZS_long.md) | **혼합 — Zoptrex 실패, Macrilen 최종 승인·license** |
| 2 | 2004-01-09 | AF | **Short** | **Astoria Financial Common Long** | [Astoria 2004](ideas/2004/2004-01-09_AF_astoria_long.md) | **실패 — $3.57 EPS bridge 과대** |
| 3 | 2006-09-18 | AF | Short | **Astoria Financial Common Short** | [Astoria 2006](ideas/2006/2006-09-18_AF_astoria_short.md) | **성공 — NIM/earnings compression 적중** |
| 4 | 2009-11-08 | AF | Long | **AlarmForce Industries Common Long** | [AlarmForce 2009](ideas/2009/2009-11-08_AF_alarmforce_long.md) | **부분 성공 — growth 과대, recurring franchise·takeout 성공** |
| 5 | 2014-03-10 | AF | **Short** | **AlarmForce Industries Common Long** | [AlarmForce 2014](ideas/2014/2014-03-10_AF_alarmforce_long.md) | **성공 — C$10.70→C$16 takeout** |
| 6 | 2002-10-04 | AFC | **Short** | **Allmerica Financial Common Long** | [Allmerica](ideas/2002/2002-10-04_AFC_allmerica_long.md) | **매우 강한 성공 — negative life stub 해소** |
| 7 | 2008-12-29 | AFC | Long | **Allied Capital 6.875% 2047 Senior Notes Long** | [Allied AFC Notes](ideas/2008/2008-12-29_AFC_allied_capital_2047_notes_long.md) | **매우 강한 성공 — ~35c→par + coupons** |
| 8 | 2004-06-24 | AFCE | Long | **AFC Enterprises Common Long** | [AFCE 2004](ideas/2004/2004-06-24_AFCE_long.md) | **강한 성공 — divestitures + $12 special dividend** |
| 9 | 2007-12-05 | AFCE | **Short** | **AFC Enterprises Common Long** | [AFCE 2007](ideas/2007/2007-12-05_AFCE_long.md) | **지연 성공 — 2009 EPS target를 2011에 달성** |
| 10 | 2011-03-25 | AFCE | **Short** | **AFC Enterprises Common Long** | [AFCE 2011](ideas/2011/2011-03-25_AFCE_long.md) | **매우 강한 성공 — $14.65→$79 cash takeout** |

---

# PART A — 이번 배치의 가장 중요한 데이터 문제: ticker는 entity가 아니다

## 2. AF와 AFC의 ticker reuse

### AF

SQL의 current `companies` mapping만 보면 AF는 AlarmForce로 보이지만 원문을 읽으면:

- **2004-01-09 AF = Astoria Financial**
- **2006-09-18 AF = Astoria Financial**
- **2009-11-08 AF = AlarmForce Industries**
- **2014-03-10 AF = AlarmForce Industries**

다.

### AFC

마찬가지로:

- **2002-10-04 AFC = Allmerica Financial common equity**
- **2008-12-29 AFC = Allied Capital 6.875% senior unsecured note due 2047**

다.

따라서 historical investment DB의 primary key는 ticker만으로는 부족하다.

> **권장 canonical key: `idea_id + date + legal entity + security type`.**

---

# PART B — AEZS: 두 번의 trial headline failure 중 하나가 규제적으로 살아남다

## 3. AEZS 2016 — option basket

원문은 약 **$33m market cap, EV≈0**에서:

- Macrilen Phase III
- Zoptrex Phase III

두 개의 독립 binary options를 산다는 구조였다.

실제:

- **2017-01 Macrilen confirmatory trial:** objective miss
- **2017-05 Zoptrex:** Phase III 실패, 개발 중단
- **2017-12 Macrilen:** FDA 승인
- **2018:** Strongbridge license, upfront + royalty economics

### 핵심

단순히 “1승 1패”가 아니다. Macrilen은 **clinical headline miss → regulatory reassessment → approval**의 경로였다.

> **Biotech에서는 trial outcome, regulatory outcome, financing outcome을 한 개의 binary variable로 묶으면 안 된다.**

---

# PART C — Astoria Financial 2004 vs 2006: 같은 은행의 bull과 short가 정반대로 갈린 이유

## 4. 2004 Long — refinancing benefit을 너무 선형적으로 더했다

원문:

- LTM EPS $2.59
- 2004E EPS **$3.57**
- NIM **2.40%**
- $7.7bn liabilities refinancing
- target $43~57

실제:

- 2004 operating diluted EPS **$2.09**
- 2005 diluted EPS **$2.26**

즉 refinancing, prepayment normalization, loan growth, buyback을 독립 항목처럼 더한 EPS bridge가 과대였다.

## 5. 2006 Short — asset/liability repricing mismatch를 정확히 봤다

원문:

- Street 2007 EPS ~$1.94
- own estimate ~$1.35
- inverted curve + funding pressure
- target 2005 low ~$24.43

실제 2007:

- NIM **1.87% → 1.62%**
- net interest income **$390.4m → $333.5m**

### 두 아이디어의 비교

| 구분 | 2004 Long | 2006 Short |
|---|---|---|
| 주된 변수 | liability refinancing savings | funding cost > asset repricing |
| 모델링 | additive EPS bridge | spread mechanism |
| 실제 결과 | earnings 예상 미달 | NIM compression 적중 |
| 교훈 | 항목별 절감액을 선형 합산하지 말 것 | balance-sheet repricing 속도를 볼 것 |

> **은행은 좋은 자산을 보유했는지가 아니라 자산과 부채가 어떤 속도로 재가격되는지가 earnings path를 결정한다.**

---

# PART D — AlarmForce: 훌륭한 recurring economics와 과도한 growth extrapolation

## 6. 2009 Long

원문은 약 100k subscribers에서:
- SAC ~$662
- customer IRR ~26%
- gross margin ~78%
- steady-state EV/EBITDA ~3.2x
- 3~5년 subscribers **200~250k**

를 기대했다.

실제:
- 2010 **113.5k**
- 2015 **144.2k**
- 2018 BCE **C$16/share** 인수

### 판정

사업의 recurring-revenue quality는 맞았지만 **새 지역 CAC가 기존 market과 같을 것이라는 성장 extrapolation은 틀렸다.**

## 7. 2014 Long

entry **C$10.70**에서:
- founder removal
- failed sale process
- net cash
- 91% contracted recurring revenue
- downside FCF C$0.58 / upside C$1.07

을 봤다.

실제 subscriber growth는 정체했지만 BCE가 **C$16/share**에 인수했다.

`C$16 / C$10.70 - 1 ≈ +49.5%`

> **운영 턴어라운드가 완벽하지 않아도 recurring customer base에 전략적 가치가 남아 있으면 event payoff가 생길 수 있다.**

---

# PART E — AFC 두 건: ticker는 같지만 common과 distressed bond는 완전히 다른 투자

## 8. Allmerica Financial 2002 — hated life stub에 negative value

원문 SOTP:

- P&C 약 **$20/share**
- life conservative value **$3/share**
- target **$23**
- stock 약 **$10**

시장은 사실상 life book을 큰 negative value로 가격화했다.

실제:
- life blocks coinsurance/sale
- P&C focus
- 2004-02 stock **$37.16**
- 2005 The Hanover로 사명 변경

**매우 강한 성공.**

## 9. Allied Capital AFC Notes 2008 — common narrative가 아니라 claim coverage

증권:
- 6.875% senior unsecured
- $25 par
- 2047 maturity
- 약 **35~36c of par** entry

실제:
- 2010 Ares Capital이 Allied 인수하며 debt assumption
- 2021 잔여 notes를 **$25 par + accrued interest**에 전액 redemption

단순 principal 기준 약 $9→$25, 즉 **+178%**에 coupon이 추가된다.

> **같은 ticker “AFC”라도 하나는 insurance common, 하나는 exchange-traded senior debt다. security type을 잃는 순간 분석이 무너진다.**

---

# PART F — AFC Enterprises 3번: asset-sale → turnaround → compounder

## 10. 2004 — event-driven SOTP

원문:
- stock ~$21
- 6x FY04E EBITDA
- Church's/Cinnabon 매각
- Popeyes pure-play
- target ~$28

실제:
- Cinnabon: ~$21m cash
- Church's: ~$379m cash + $7m note
- 2005: **$12/share special dividend**

### 판정

가격차트가 아니라 **asset-sale cash + special dividend**로 봐야 하는 강한 성공이다.

## 11. 2007 — turnaround 방향은 맞고 timing은 틀림

원문:
- Cheryl Bachelder turnaround
- 2009 EPS ~$1
- $14 target in 18~24m

실제:
- 2008 adj EPS $0.76, SSS negative
- 2010 global SSS +2.6%
- 2011 adj EPS **$0.99**

즉 숫자는 맞았지만 약 **2년 늦었다**.

## 12. 2011 — recovery에서 compounding으로

entry:
- ~$14.65
- 2011 EPS guide $0.91~0.95
- FCF ~$1/share
- 5Y EPS CAGR guide 13~15%

실제:
- 2011 adj EPS **$0.99**
- 2012 **$1.24**
- 2015 **$1.89~1.91**
- 2017 RBI **$79 cash/share**

`$79 / $14.65 ≈ 5.39x`

### 세 vintage 비교

| Vintage | 무엇을 샀나 | 핵심 catalyst | 결과 |
|---|---|---|---|
| 2004 | 복잡한 holding company discount | 자산매각 + 현금환원 | 강한 성공 |
| 2007 | broken brand turnaround | CEO/SSS/unit growth | 지연 성공 |
| 2011 | 검증되기 시작한 franchisor compounding | EPS/SSS/unit growth + buyback | 매우 강한 성공 |

> **같은 기업도 “cheap assets → turnaround → compounder”로 lifecycle이 이동하면 underwriting 방식도 바뀌어야 한다.**

---

# PART G — Batch 067 공통 분석식

### Bank / Thrift

`NIM = asset yield - funding cost`

그리고:
`ΔEPS ≠ 단순 refinancing saving 합계`

asset repricing, deposit beta, prepayment, curve shape를 함께 연결한다.

### Subscription business

`Cohort LTV = monthly recurring revenue × gross margin × expected life - fully-loaded CAC`

새 지역의 CAC/retention을 기존 지역에서 그대로 외삽하지 않는다.

### Distressed credit

`Recovery value = stressed asset value - claims senior to me`

common equity narrative보다 legal claim을 먼저 본다.

### Franchisor

`Corporate FCF ≈ system sales × royalty rate + franchise fees - brand SG&A`

핵심 선행지표는 SSS, franchisee returns, net new units다.

### Biotech

`Equity option value = cash + Σ[P(asset outcome) × retained asset economics] - burn - dilution`

clinical, regulatory, financing probability를 분리한다.

---

# PART H — Batch 067 재사용 체크리스트

1. ticker를 company ID로 쓰지 않는다.
2. historical ticker reuse를 legal entity/date로 교정한다.
3. common과 exchange-traded debt를 같은 ticker로 합치지 않는다.
4. raw Long/Short flag보다 원문 recommendation/disclosure를 우선한다.
5. bank EPS bridge는 balance-sheet feedback을 반영한다.
6. subscription business는 market별 CAC와 churn을 분리한다.
7. negative-value stub는 실제 capital-release path를 검증한다.
8. distressed debt는 stressed asset coverage와 seniority를 먼저 본다.
9. special dividend가 있으면 raw price return을 사용하지 않는다.
10. turnaround에서는 direction과 time-to-repair를 별도 평가한다.
11. compounder 단계에서는 EPS denominator 성장과 multiple을 분리한다.
12. corporate action은 가장 강한 realized-value anchor가 될 수 있다.

---

## 13. Batch 067 핵심 한 줄

> **이번 배치의 핵심은 ticker가 아니라 “그 날짜에 어떤 법인·어떤 증권을 샀는가”다. AF와 AFC의 ticker reuse를 교정하고 나면, 은행 common·subscription common·보험 SOTP·distressed bond가 완전히 다른 투자라는 것이 선명해진다.**

## 14. 앱 / DB 반영

- Wrapper: `analysis/batch_067_aezs_af_afc_afce_10.md`
- Staging catalog (DB 미반영): `data/staging/batch_067_aezs_af_afc_afce_catalog_v9.json`
- Canonical source of truth: 위 10개 Markdown.
