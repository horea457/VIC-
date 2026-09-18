# Assured Guaranty vs MBIA — 2014-12-10 VIC Pair Trade

> **Idea unit:** 2014-12-10 **Long AGO / Short MBI** relative-value pair trade.
> **Research as-of:** 2026-09-18. 원 SQL은 AGO Long으로만 저장돼 있지만 실제 전략은 **pairs trade**다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Long leg | Assured Guaranty / AGO |
| Short leg | MBIA / MBI |
| VIC 게시일 / 작성자 | 2014-12-10 / socratesplus |
| 실제 전략 | **Long AGO / Short MBI** |
| 핵심 논지 | AGO superior capital/ABV compounding vs MBI weaker exposure/capital |
| major catalyst | Puerto Rico / PREPA restructuring differentiation |
| AGO Dec-2014 price ref | 약 **$25.99** |
| AGO Dec-2015 price ref | 약 **$26.43** |
| MBI Dec-2014 price ref | 약 **$9.54** |
| MBI Dec-2015 price ref | 약 **$6.48** |
| rough equal-dollar 1Y pair return | 약 **+33~34% gross** |
| SQL AGO-only 1Y | **-3.9%** — pair return으로 사용 불가 |
| 최종 판정 | **강한 성공 — short leg가 대부분의 alpha를 만든 relative-value trade** |

> **결론:** 원문은 AGO를 단독 Long으로 추천한 것이 아니라 **AGO를 사고 MBI를 숏**했다. AGO는 adjusted book와 capital adequacy가 더 강하고 buybacks로 per-share value를 늘릴 수 있는 반면, MBI는 Puerto Rico/PREPA 등 상대적으로 취약한 exposure를 갖고 있다고 봤다. 2015년 AGO는 거의 보합이었지만 MBI는 약 32% 하락해 equal-dollar pair는 gross 기준 약 **+33~34%**로 추정된다. source SQL의 AGO standalone 1Y -3.9%는 이 전략의 성과를 측정하지 못한다.

---

## 1. 왜 Pair Trade였나

보험보증 업종 전체에는:
- municipal-credit risk,
- Puerto Rico,
- interest-rate / spread environment,
- regulatory capital

이라는 공통 beta가 있었다.

원문은 업종 방향을 맞히기보다:

**relative return = AGO quality/capital advantage - MBI weakness**

를 샀다.

---

## 2. 원문 투자논지

### AGO Long
- stronger claims-paying resources
- better adjusted book
- accretive buybacks
- more diversified public-finance franchise

### MBI Short
- weaker capital flexibility
- more concentrated problematic exposures
- Puerto Rico/PREPA sensitivity
- lower expected per-share value compounding

---

## 3. 실제 Rough Pair Outcome

월말 가격 approximation:

| Leg | Dec-2014 | Dec-2015 | Approx return |
|---|---:|---:|---:|
| AGO Long | $25.99 | $26.43 | **+1.7%** |
| MBI Short | $9.54 | $6.48 | **+32.1% short gain** |

equal-dollar gross pair:
**~+33.8%**

배당, borrow cost, exact trade date, rebalance는 제외한다.

---

## 4. SQL Performance Row를 왜 쓰면 안 되는가

source DB의 AGO row:
- 1Y **-3.9%**
- 2Y +49.3%
- 3Y +41.7%
- 5Y +104.3%

이는 **AGO long leg만** 추적한 값이다.

pair trade 성과는:
**AGO return - MBI return - borrow/dividend/financing adjustments**
로 계산해야 한다.

---

## 5. Claim Map

### C1. AGO relative capital strength — **성공**
AGO는 계속 buybacks와 ABV compounding을 수행했다.

### C2. MBI relative weakness — **강한 성공**
2015 주가가 큰 폭 하락했다.

### C3. PREPA/Puerto Rico differentiation — **성공 방향**
시장 stress가 양사에 비대칭적으로 반영됐다.

### C4. pair reduces industry beta — **성공**
AGO가 거의 보합이어도 MBI short에서 큰 alpha가 났다.

---

## 6. 재사용 가능한 교훈

1. pair trade는 long-leg chart만으로 평가하지 않는다.
2. equal-dollar, beta-neutral, notional-neutral 중 어떤 sizing인지 기록한다.
3. short-leg borrow/dividend 비용을 gross pair return과 분리한다.
4. industry beta를 제거하면 security-quality 차이가 더 잘 드러날 수 있다.
5. SQL schema가 단일 ticker만 보존하면 strategy type을 별도 필드로 복원한다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Relative-value thesis | 강한 성공 |
| Long leg | 대체로 보합 |
| Short leg | 강한 성공 |
| Strategy reconstruction | 필수 |
| Thesis score | 9.0/10 |
| Process score | 9.9/10 |
| 종합 | **강한 성공 — pair economics는 SQL standalone return보다 훨씬 좋았음** |

### 한 문장 교훈

> pair trade에서는 **“롱이 올랐나”가 아니라 내가 산 spread가 좁혀졌나**를 봐야 한다.

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2014-12-10.
2. Source SQL AGO performance row — long leg only, not pair result.
3. Historical AGO monthly prices — FinanceCharts.
4. Historical MBI monthly prices — Digrin / market history.
5. Assured capital-return and Puerto Rico disclosures.

### 데이터 품질
- strategy identity: **A**
- exact pair IRR: **B** — month-end approximations and no borrow-cost reconstruction
