# Allergan / AbbVie Merger Arbitrage (AGN) — 2019-10-16 VIC Long Spread

> **Idea unit:** 2019-10-16 Allergan merger-arbitrage spread Long against AbbVie consideration.
> **Research as-of:** 2026-09-18. 원 SQL Long과 실제 방향이 일치한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Target | Allergan plc |
| Acquirer | AbbVie Inc. |
| VIC 게시일 / 작성자 | 2019-10-16 / honeycreek |
| 실제 방향 | **Long merger spread** |
| consideration | **$120.30 cash + 0.8660 ABBV share** |
| 당시 spread | 약 **7.9%** |
| author expected IRR | 약 **17%** after fees/borrow/dividends |
| expected close | early 2020 |
| actual close | **2020-05-08** |
| 최종 판정 | **강한 성공 — deal closed at stated terms; timing slightly later than expected** |

> **결론:** 2019 아이디어는 Allergan standalone valuation이 아니라 AbbVie signed deal의 spread를 사는 merger arb였다. 각 AGN share는 $120.30 cash + 0.8660 ABBV share를 받는 구조였고, 당시 spread는 약 7.9%였다. 거래는 2020년 5월 8일 정확한 terms로 완료됐다. 원문의 “early 2020”보다 다소 늦었지만 break가 발생하지 않았으므로 **arb thesis는 강한 성공**이다. 정확 realized IRR은 ABBV hedge, dividends, borrow/fees를 복원하지 않아 단정하지 않는다.

---

## 1. Deal Structure

각 AGN share:
- cash **$120.30**
- stock **0.8660 ABBV**

따라서 hedged trade는 대략:

**Long 1 AGN / Short 0.8660 ABBV**

이다.

---

## 2. 원문 투자논지

원문은:
- definitive agreement,
- financing certainty,
- antitrust divestiture feasibility,
- shareholder approval,
- AbbVie incentive to close

를 근거로 약 90% close probability를 제시했다.

---

## 3. Claim Map

### C1. deal closes — **강한 성공**
2020-05-08 완료.

### C2. stated terms preserved — **성공**
$120.30 + 0.8660 ABBV.

### C3. early-2020 close — **조금 지연**
May 2020로 넘어갔다.

### C4. 7.9% spread capture — **성공 방향**
gross economics는 실현됐지만 exact hedge P&L은 별도다.

### C5. 17% IRR — **정확 검증 유보**
actual hedge execution과 close delay 때문에 exact realized IRR은 산출하지 않는다.

---

## 4. 실제 경로

| 날짜 | 사건 |
|---|---|
| 2019-10-16 | VIC arb post |
| 2020 Q1 | regulatory process 지속 |
| 2020-05-08 | AbbVie completes Allergan acquisition |
| final terms | $120.30 cash + 0.8660 ABBV |

---

## 5. Merger-Arb Return Formula

**Arb P&L = cash + stock consideration - target cost - hedge cost ± dividends - fees/borrow**

따라서 target chart만으로 merger-arb return을 계산하면 안 된다.

---

## 6. 재사용 가능한 교훈

1. mixed consideration은 acquirer hedge ratio를 정확히 맞춘다.
2. close probability와 timing을 별도 변수로 둔다.
3. regulatory delay는 deal success와 return timing을 모두 바꾼다.
4. target stock 상승률과 arb return을 혼동하지 않는다.
5. exact IRR은 실제 hedge fills 없이는 확정하지 않는다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Deal completion | 강한 성공 |
| Terms | 성공 |
| Timing | 약간 지연 |
| Spread thesis | 성공 |
| Thesis score | 9.5/10 |
| Process score | 9.8/10 |
| 종합 | **강한 성공 — stated consideration으로 deal 완료** |

### 한 문장 교훈

> merger arb에서는 **좋은 회사가 아니라 signed contract와 break mechanics를 산다.**

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2019-10-16.
2. AbbVie acquisition closing, 2020-05-08.
3. Final consideration: $120.30 cash + 0.8660 ABBV share per Allergan share.

### 데이터 품질
- T0 arb thesis: **A**
- closing terms/date: **A**
- exact realized IRR: **not reconstructed**
