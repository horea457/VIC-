# Batch 053 — New England Realty / Owens Corning / Office Depot V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 052 마지막 NEN 2011-06-30 이후 reviewed idea_id를 제외한 다음 10건.

## Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 방향 | Canonical | 핵심 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2019-01-15 | NEN | Long | Long | [NEN 2019](ideas/2019/2019-01-15_NEN_long.md) | 3Y +46.8%, 장기 200% thesis는 미검증 |
| 2 | 2007-01-31 | OC | Long | Long | [OC 2007 Jan](ideas/2007/2007-01-31_OC_long.md) | 2Y -53.5%, post-reorg timing 실패 |
| 3 | 2007-12-26 | OC | Long | Long | [OC 2007 Dec](ideas/2007/2007-12-26_OC_long.md) | 5Y +84.4%, 낮아진 가격에서 성공 |
| 4 | 2013-03-14 | OC | Long | Long | [OC 2013](ideas/2013/2013-03-14_OC_long.md) | business thesis 적중, 5Y +118.5% |
| 5 | 2015-01-06 | OC | **Short** | **Long** | [OC 2015 Jan](ideas/2015/2015-01-06_OC_long.md) | 3Y +164.9%, raw direction 오류 |
| 6 | 2015-04-07 | OC | Long | Long Update | [OC 2015 Apr](ideas/2015/2015-04-07_OC_long_update.md) | 3Y +98.9%, channel-check update 성공 |
| 7 | 2017-05-12 | OC | Long | Long | [OC 2017](ideas/2017/2017-05-12_OC_long.md) | 6M +30.8% 후 3Y -30.3% |
| 8 | 2018-12-12 | OC | Long | Long | [OC 2018](ideas/2018/2018-12-12_OC_long.md) | 1Y +52.9%, 3Y +118.3% |
| 9 | 2000-07-28 | ODP | **Short** | **Long** | [ODP 2000](ideas/2000/2000-07-28_ODP_long.md) | SOTP tactical success 방향 |
| 10 | 2007-03-22 | ODP | **Short** | **Long** | [ODP 2007](ideas/2007/2007-03-22_ODP_long.md) | 2008 operating collapse, 강한 실패 |

## Direction Audit

이번 batch도 raw SQL 방향 오류가 3건이다.

1. **OC 2015-01-06:** raw Short → 실제 Long
   - 2015-04-07 후속 글이 직접 “my Long thesis posted on 1/6/2015”라고 명시.
2. **ODP 2000-07-28:** raw Short → 실제 Long
   - 원문이 “recommending the purchase of this stock”이라고 명시.
3. **ODP 2007-03-22:** raw Short → 실제 Long
   - 원문이 +25% upside와 $40s target을 제시.

따라서 BATCH 53의 **10건 모두 실제 Long**이다.

## NEN 2019 — 장기 compounder framing

2019 writeup은 이전 NEN 아이디어보다 더 장기적이다.

- replacement cost 대비 55%+ 할인
- NAV 대비 67% 할인
- 10~11% FCF yield
- under-market rents
- Boston Class-B supply constraint
- Brown family buyback / capital allocation
- 10년 15%+ compound 목표

SQL:
- 1Y +10.7%
- 2Y -9.7%
- 3Y +46.8%

2020 COVID drawdown을 거친 뒤 회복했지만 200%/10년 thesis는 아직 별도 장기 total-return 복원이 필요하다.

## Owens Corning — 같은 산업구조, 완전히 다른 entry point

### 2007-01: Post-reorg Long
$28.50, 6.1x trailing EBITDA.

논리:
- asbestos 제거
- fresh balance sheet
- distressed investor cost basis
- normalized housing earnings

결과:
- 1Y -24.3%
- 2Y -53.5%
- 5Y +17.9%

**재무구조는 clean했지만 earnings cycle은 clean하지 않았다.**

### 2007-12: 같은 회사, $20.60
EV/normalized EBITDA 약 3.7x.

결과:
- 1Y -13.9%
- 2Y +30.6%
- 3Y +57.5%
- 5Y +84.4%

11개월의 가격하락과 더 보수적인 normalized-margin 분석이 risk/reward를 바꿨다.

## OC 2013 — Business thesis와 stock timing 분리

원문:
- Bear $29
- Base $60
- Bull $96
- current $40.61

실제 2013:
- adjusted EBIT $293m → $416m
- Roofing margin 약 20%
- Insulation -$38m → +$40m
- dividend 신규 도입

사업논지는 빠르게 맞았지만 주가는 1Y +6.1%에 그쳤다.
5Y는 +118.5%.

**Correct fundamentals do not guarantee immediate rerating.**

## OC 2015 — 결과가 맞아도 causal claim을 다시 본다

2015-01 Long:
- crude/asphalt cost deflation
- stable shingle pricing
- winter pre-buy discipline
- $2.30 consensus EPS + 약 $0.50 asphalt benefit
- PT 약 $50

실제 2015:
- selling price **-$114m**
- asphalt cost deflation **+$68m**
- Roofing EBIT +$34m
- adjusted EPS +46%
- FCF $50m → $341m

즉 Long 결과는 성공했지만:

**원문:** flat price + lower asphalt  
**실제:** lower price + lower asphalt + volume/mix

였다.

이 구분이 postmortem에서 중요하다.

## OC 2017 vs 2018 — 가장 중요한 비교

| 항목 | 2017 Long | 2018-12 Long |
|---|---|---|
| 핵심 | all 3 segments normalize | 2018 악재 과반영 |
| valuation | 약 10% FCF yield | 8.5x normalized EPS |
| 기대 | 높아지는 중 | 크게 reset |
| 6M | +30.8% | +23.8% |
| 1Y | +5.5% | +52.9% |
| 2Y | -20.7% | +75.5% |
| 3Y | -30.3% | +118.3% |

2017 business thesis는 실제로 맞았다:
- Roofing EBIT $535m
- Insulation +40%
- Composites 5년 연속 개선
- FCF $679m

그런데 stock은 중기 실패했다.

2018 말에는 같은 회사가:
- storm normalization
- freight/asphalt inflation
- housing worries

로 48% 가까이 하락한 뒤였다.

**좋은 기업인지보다 starting expectation이 더 중요했다.**

## Office Depot 2000 vs 2007

### 2000 Long
주가 약 $6.

원문 SOTP:
- BSG 약 $1.0bn
- International 약 $1.3bn
- Retail 약 $1.0bn
- whole market cap 약 $1.9bn

BSG + International만으로 equity value를 설명하고 Retail을 free option으로 봤다.

2001 International:
- sales +6% reported
- FX 제외 +11%
- Viking local-currency comps +11%

단기 SOTP/recovery thesis는 성공 방향.

### 2007 Long
Odland turnaround를 다시 샀다.

원문:
- 13x 2008E
- mid-high teens EPS growth
- +30bp annual margin expansion
- 150 new stores
- $200~250m buybacks
- +25% / 6~12M

실제 2008:
- Retail sales -10%
- Retail operating profit $354.5m → **-$29.2m**
- BSD sales -8%
- BSD profit $220.1m → $119.8m

비용절감 turnaround에서 **incremental investment turnaround**로 넘어가는 순간 실패했다.

## Batch 053 상위 투자 교훈

1. post-reorg balance sheet clean-up과 earnings-cycle bottom을 분리한다.
2. distressed investor cost basis는 downside floor가 아니다.
3. 같은 cyclical도 entry multiple과 normalized-margin assumptions가 달라지면 전혀 다른 투자다.
4. business thesis success와 stock rerating timing을 별도 판정한다.
5. 결과가 좋았어도 earnings bridge의 각 causal claim을 재검증한다.
6. channel checks는 realized price/cost로 사후 확인한다.
7. 모든 segment가 동시에 좋아질 때는 peak-risk도 체크한다.
8. normalized EPS multiple은 기대가 reset된 뒤 가장 강하게 작동할 수 있다.
9. turnaround 2단계는 cost cutting보다 incremental ROIC가 중요하다.
10. SOTP tactical value와 long-term structural decline thesis는 동시에 참일 수 있다.

## 앱 / DB 반영

- Wrapper: analysis/batch_053_nen_oc_odp_10.md
- Overlay: data/curated/batch_053_nen_oc_odp_deep_v7.json
- Canonical source of truth: 위 10개 idea Markdown.
