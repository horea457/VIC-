# Adecoagro (AGRO) — 2019-06-27 VIC Long

> **Idea unit:** 2019-06-27 Adecoagro common equity Long.
> **Research as-of:** 2026-09-18. 원 SQL Long과 실제 방향이 일치한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Adecoagro / AGRO |
| VIC 게시일 / 작성자 | 2019-06-27 / aquicap |
| 실제 방향 | Common equity Long |
| 당시 가격 | **$6.90** |
| 2019 EV/EBITDA | 약 **5x** |
| 2021 EV/EBITDA | 원문 기준 **<4x** |
| 2021 EBITDA plan | **$454m** |
| valuation target | **$12.66 (+83%)** |
| actual 2021 adj. EBITDA | **$437.1m** |
| actual 2021 adjusted FCF from ops | **$152.1m** |
| distribution policy | **2022부터 최소 40% AFCF** |
| SQL 1Y | **-39.5%** |
| SQL 2Y | **+41.2%** |
| SQL 3Y | **+24.0%** |
| 최종 판정 | **운영 thesis 강한 성공 / target-multiple은 미달** |

> **결론:** 2019 thesis는 2015와 달리 정치변화보다 이미 집행 중인 5개년 capex plan의 completion과 capital return을 샀다. 원문은 2021 EBITDA $454m을 예상했는데 실제는 **$437.1m**으로 매우 근접했다. 회사는 2022부터 전년도 adjusted FCF의 최소 40%를 배당·buyback으로 환원하는 정책도 도입했다. 다만 COVID 때문에 1년 return은 -39.5%였고, 2년 +41.2%, 3년 +24.0%로 회복했지만 원문 $12.66 target에는 충분히 도달하지 못했다.

---

## 1. 원문 투자논지

2017~21 five-year plan:
- expansion capex **$355m**
- EBITDA **$288m→$454m**
- unlevered IRR **20~25%**
- 2019 말까지 대부분 capex 투입
- 2020~21 earnings acceleration
- share repurchase / dividend formalization

이었다.

---

## 2. Claim Map

### C1. EBITDA ~$454m by 2021 — **매우 근접**
actual $437.1m.

### C2. expansion-capex payoff — **성공**
Sugar/Ethanol/Energy와 Farming 모두 EBITDA growth.

### C3. capital return policy — **강한 성공**
2022부터 최소 40% adjusted FCF distribution policy.

### C4. buybacks — **성공**
2019 이후 매년 buyback 지속, 2021에는 약 6.3% shares repurchased.

### C5. $12.66 target — **미달**
3Y source return +24%.

---

## 3. Source SQL Performance

| Horizon | Return |
|---|---:|
| 1W | -1.8% |
| 1M | -3.8% |
| 3M | -17.4% |
| 6M | +19.5% |
| 1Y | **-39.5%** |
| 2Y | **+41.2%** |
| 3Y | **+24.0%** |

---

## 4. 2015 vs 2019

| 항목 | 2015 | 2019 |
|---|---|---|
| 핵심 catalyst | Argentina policy | committed capex plan |
| EBITDA forecast | 맞음 | 맞음 |
| FCF forecast | 크게 틀림 | 개선 |
| capital return | 기대 | 실제 정책화 |
| security result | 약함 | 2~3Y positive |

> 같은 회사라도 **정책 옵션보다 이미 집행된 project economics가 더 검증 가능**했다.

---

## 5. 재사용 가능한 교훈

1. capex plan은 deployed capital과 EBITDA ramp를 연도별 추적한다.
2. operational target이 가까울수록 forecast error가 줄어든다.
3. capital-return policy는 cash generation을 equity value로 연결하는 bridge다.
4. COVID 같은 macro shock은 1Y result와 thesis quality를 분리해서 본다.
5. multiple target은 operating delivery와 별도 hypothesis다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| 5Y plan execution | 강한 성공 |
| EBITDA forecast | 매우 강한 성공 |
| Capital return | 강한 성공 |
| Price target | 미달 |
| Thesis score | 8.8/10 |
| Process score | 9.9/10 |
| 종합 | **운영 강한 성공 / valuation upside 부분 성공** |

### 한 문장 교훈

> 같은 macro-exposed 회사라도 **정치변화보다 이미 투입된 capex의 수익률을 사는 thesis가 더 반복 가능**하다.

---

## 7. Sources / Validation Notes

1. VIC original: https://www.valueinvestorsclub.com/idea/ADECOAGRO_SA/5021005401
2. Source SQL performance row.
3. 2021 results: https://sustainability.adecoagro.com/wp-content/uploads/2023/02/2021-Integrated-Report-Adecoagro.pdf
4. Distribution policy: https://www.sec.gov/Archives/edgar/data/1499505/000162828021022796/a6ker09302021.htm
5. Current distribution history: https://ir.adecoagro.com/shareholder-distribution/

### 데이터 품질
- T0 thesis: **A**
- operating/capital-return actuals: **A**
- source return: **A within DB**
