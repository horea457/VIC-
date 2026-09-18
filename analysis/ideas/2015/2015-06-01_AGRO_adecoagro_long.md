# Adecoagro (AGRO) — 2015-06-01 VIC Long

> **Idea unit:** 2015-06-01 Adecoagro common equity Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 원문은 명백한 **Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Adecoagro / AGRO |
| VIC 게시일 / 작성자 | 2015-06-01 / thrive25 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 가격 | **$9.66** |
| target | **$27 (+179%)** |
| 원문 2017 FCF | 약 **$163m** |
| 2016 EBITDA forecast | **$300~340m** |
| 실제 2016 adj. EBITDA | **$298m** |
| 실제 2017 AFCF before expansion capex | **$78.0m** |
| 실제 2017 adjusted FCF | **$7.2m** |
| SQL 1Y | **+15.0%** |
| SQL 2Y | **+11.1%** |
| SQL 3Y | **-17.9%** |
| 최종 판정 | **정책·EBITDA thesis 적중 / FCF·valuation target 실패** |

> **결론:** 원문은 Kirchner 이후 Argentina 정상화를 핵심 catalyst로 봤고 이 부분은 매우 정확했다. Macri 정부는 실제로 대부분의 FX controls를 완화하고 corn/wheat export duties를 없애거나 줄였으며 peso는 크게 절하됐다. Adecoagro의 2016 adjusted EBITDA도 $298m으로 원문 $300~340m forecast 하단에 거의 도달했다. 그러나 2017 adjusted FCF는 **$7.2m**으로 원문 $163m과 크게 달랐다. 정책은 맞았지만 maintenance/expansion capex와 cash conversion bridge가 과도했다.

---

## 1. 원문 투자논지

원문은 세 축을 샀다.

1. Argentina regime change
2. Brazil sugar/ethanol capex cycle 종료
3. farmland NAV discount

정책효과 가정:
- export-tax reduction → +$50m FCF
- 20% peso devaluation → +$40~60m FCF
- Brazil normalized FCF → ~$63m

합계 2017 pro forma FCF 약 **$163m**.

---

## 2. 실제 정책 변화

Macri 정부 취임 후:
- corn/wheat export taxes/quotas 제거
- soybean tax 35%→30%
- FX restrictions 대폭 완화
- peso nominal devaluation >50%

Adecoagro는 이 조치로 Argentine farmland profitability가 크게 개선됐다고 직접 밝혔다.

---

## 3. Claim Map

### C1. political regime reform — **강한 성공**

### C2. 2016 EBITDA ~$300m+ — **강한 성공**
actual **$298m**.

### C3. farmland economics improve — **성공**
2015 farm sales도 independent appraisal 대비 48~57% premium을 기록했다.

### C4. 2017 FCF ~$163m — **강한 실패**
AFCF before expansion capex $78m, after expansion capex adjusted FCF $7.2m.

### C5. $27 target — **실패**
SQL 1Y +15%, 2Y +11%, 3Y -18%.

---

## 4. Source SQL Performance

| Horizon | Return |
|---|---:|
| 1W | +1.3% |
| 1M | -7.1% |
| 3M | -19.5% |
| 6M | +13.6% |
| 1Y | **+15.0%** |
| 2Y | **+11.1%** |
| 3Y | **-17.9%** |

---

## 5. 핵심 오류

원문은 policy change를 EBITDA뿐 아니라 **FCF에 거의 1:1로 연결**했다.

하지만 실제:
- maintenance capex
- expansion capex
- working capital
- weather
- commodity mix

가 cash conversion을 크게 낮췄다.

---

## 6. 재사용 가능한 교훈

1. policy reform과 FCF conversion을 별도 hypothesis로 둔다.
2. EBITDA forecast가 맞아도 FCF target은 틀릴 수 있다.
3. agricultural capex는 maintenance와 expansion을 분리한다.
4. land appraisal premium을 recurring operating FCF로 합산하지 않는다.
5. macro catalyst가 맞아도 starting valuation target이 자동 실현되지는 않는다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Political thesis | 매우 강한 성공 |
| EBITDA forecast | 성공 |
| FCF forecast | 강한 실패 |
| Price target | 실패 |
| Thesis score | 6.5/10 |
| Process score | 9.9/10 |
| 종합 | **정책은 맞고 cash-flow bridge는 틀린 사례** |

### 한 문장 교훈

> **정책이 맞았다는 것과 그 정책효과가 주주 FCF로 그대로 떨어진다는 것은 전혀 다른 주장**이다.

---

## 8. Sources / Validation Notes

1. VIC original: https://www.valueinvestorsclub.com/idea/ADECOAGRO_SA/9203855446
2. Source SQL performance row.
3. 2016 EBITDA $298m: https://www.sec.gov/Archives/edgar/data/1499505/000167276417000012/t1700674_x1-6k.htm
4. Macri reforms / farm economics: https://www.sec.gov/Archives/edgar/data/1499505/000114036116058290/form6k.htm
5. 2017 adjusted FCF $7.2m: https://ir.adecoagro.com/wp-content/uploads/2024/12/4Q17-Earnings-Release.pdf

### 데이터 품질
- T0 thesis: **A**
- policy/EBITDA/FCF actuals: **A**
- source returns: **A within DB**
