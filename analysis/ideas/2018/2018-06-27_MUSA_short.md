# Murphy USA (MUSA) — 2018-06-27 VIC Short

> **Idea unit:** 이 게시일의 투자 아이디어를 독립 분석한다.
> **Research as-of:** 2026-09-09. raw SQL metadata와 실제 security/direction을 분리한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2018-06-27 / cable888 |
| 실제 방향 | **Short** |
| 원 SQL 방향 | Short — 일치 |
| 기준가격 | SQL next-day close $74.22 |
| 원문 target | $40, 약 -45% |
| 핵심 가정 | 2018 EBITDA $350m × 6x |
| SQL price path | 1M +4.8%, 3M +14.4%, 6M -6.5%, 1Y +11.6%, 3Y +77.4% |
| 최종 판정 | **실패 — 6개월 trade는 일부 성공, earnings/multiple thesis는 실패** |

> **결론:** Short가 기대한 단기 volume weakness는 일부 있었지만 normalized EBITDA와 multiple이 모두 너무 낮았다.

---

## 1. 회사는 정확히 무엇을 하는가

이 아이디어는 2017 short를 업데이트해 **더 높은 leverage, buyback 의존, kiosk format의 구조적 열위**를 강조했다. 회사가 2016년 이후 약 $560m capex를 썼지만 EBITDA가 늘지 않았고, SSS fuel volume도 약하다는 점이 핵심이었다.

### 핵심 KPI
- SSS gallons
- retail fuel margin / cpg
- total fuel contribution
- adjusted EBITDA
- net leverage
- buyback pace
- merchandise contribution

---

## 2. 당시 상황과 시장이 가격에 넣고 있던 것

2018 1Q miss 뒤 주가가 회복했지만 RIN 가격은 낮고 WTI는 상승 중이었다. 원문은 sell-side estimate cut과 guidance 하향, covenant 때문에 buyback 중단까지 기대했다.

---

## 3. 원문 투자논지 지도

### C1. 2018 SSS fuel volume 약세가 지속된다 — 부분 성공
Full-year SSS volume은 -0.6%였지만 Q4에는 +2.1%로 회복했다.

### C2. 정상 fuel contribution은 15 cpg 이하 — 실패/과소
2018 total fuel contribution은 16.2 cpg였고 Q4 retail fuel margin은 22.8 cpg였다.

### C3. EBITDA $350m 이하 — 실패
2018 adjusted EBITDA는 $412m.

### C4. buyback이 멈춘다 — 실패
1Q18에만 약 929k shares, $71.7m을 repurchase했고 이후 프로그램이 계속됐다.

### C5. 6x grocery-loser multiple이 맞다 — 실패
fuel retail의 economics가 grocery와 달랐고 share count compounding도 반영되지 않았다.

### C6. $40 target — 실패
SQL 기준 1Y 주가는 +11.6%, 3Y +77.4%.

---

## 4. Valuation / Payoff Structure

원문은 $350m × 6x로 $40을 제시했다. 그러나 actual 2018 adjusted EBITDA $412m과 fuel contribution resilience가 base assumption을 깨뜨렸다.

---

## 5. 실제로 무슨 일이 일어났는가

| 날짜 | 사건 |
|---|---|
| 2018-06-27 | VIC Short |
| 2018 FY | adjusted EBITDA $412m |
| 2018 Q4 | SSS gallons +2.1%, retail fuel margin 22.8 cpg |
| 2020 | record fuel economics, 대규모 repurchase |
| 2021 | QuickChek 인수 |

---

## 6. 실제 투자결과

6개월 price-only로는 주가 -6.5%라 short가 일부 이익이었지만 1년 이후 반전. 3년 주가 +77.4%로 전략적 short는 실패.

---

## 7. Claim별 사후 판정

| Claim | 판정 |
|---|---|
| SSS weakness | 부분 성공 |
| ≤15 cpg | 실패 |
| $350m EBITDA | 실패 |
| buyback stop | 실패 |
| 6x multiple | 실패 |
| $40 target | 실패 |

---

## 8. 무엇이 실제 수익을 만들거나 파괴했는가

fuel margin mean level을 너무 낮게 잡았고, buyback의 per-share 효과와 merchandise mix를 과소평가했다.

---

## 9. 분석 오류와 최초 경고

CASY 대신 grocery losers를 proxy로 둔 relative valuation이 사업경제 차이를 너무 많이 남겼다.

---

## 10. 재사용 가능한 투자 교훈

1. VIC original body preserved in uploaded SQL.
2. 2018 results: https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2019/Murphy-USA-Inc-Reports-Preliminary-Fourth-Quarter-2018-Results/
3. Q1 2018 results: https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2018/Murphy-USA-Inc-Reports-First-Quarter-2018-Results/default.aspx

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Fundamental timing | 5/10 |
| Normalized earnings | 3/10 |
| Valuation | 3/10 |
| Risk management | 5/10 |
| 종합 | **실패** |

### 한 문장 교훈
> peer가 없을 때 억지 proxy multiple을 가져오면 작은 operating-model 차이가 valuation 오류를 크게 만든다.

---

## 12. Sources / Validation Notes

undefined

### 데이터 품질
SQL price series B / 2018 results A.
