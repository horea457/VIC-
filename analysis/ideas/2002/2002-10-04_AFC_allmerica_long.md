# Allmerica Financial (AFC) — 2002-10-04 VIC Long

> **Idea unit:** 2002-10-04 Allmerica Financial common equity Long.
> **Research as-of:** 2026-09-18. SQL companies table은 AFC를 Allied Capital Bonds로 덮어썼지만 이 2002 원문은 **Allmerica Financial Corporation**이다. raw Short도 오류이며 실제 방향은 Long이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 당시 Ticker | Allmerica Financial / AFC |
| VIC 게시일 / 작성자 | 2002-10-04 / pomfret626 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 가격 | 약 **$10** |
| P&C value estimate | 약 **$20/share** |
| life downside value | 약 **$3/share** |
| 원문 target | **$23/share** |
| 실제 2004-02 stock | **$37.16** |
| 후속 구조조정 | life/annuity run-off 매각 → P&C 집중 |
| 사명 변경 | 2005 The Hanover Insurance Group |
| 최종 판정 | **매우 강한 성공 — negative life stub pricing이 해소** |

> **결론:** 원문은 시장이 P&C franchise를 약 $20/share로 평가해도 life business를 **마이너스 $10/share**로 가격에 넣고 있다고 봤다. 실제 회사는 2002~05 life/annuity exposure를 단계적으로 매각·run-off하고 P&C에 집중했으며, 2004-02 주가는 이미 $37.16이었다. 원문 $23 target를 크게 넘어선 매우 강한 성공이다.

---

## 1. 당시 구조

Allmerica는:
- P&C: Hanover/Citizens
- life/variable annuity
- corporate debt

를 가진 복합보험사였다.

2000~02 equity-market decline과 GMDB exposure 때문에 life capital 우려가 커지며 holding-company value가 무너졌다.

---

## 2. 원문 투자논지 지도

### C1. P&C만으로 $20/share — **성공**
P&C business는 유지됐고 이후 회사 전체의 core가 됐다.

### C2. life business value가 -$10/share일 수 없다 — **강한 성공**
회사는 2002 fixed universal life를 coinsurance로 넘기고, 2005 Goldman Sachs에 대부분의 variable life/annuity business를 매각했다.

### C3. life runoff에서 최소 $3/share residual — **성공 방향**
life business는 0 이하가 아니라 capital release source가 됐다.

### C4. strategic alternatives가 value를 unlock — **강한 성공**
2003~05 business simplification이 실제로 진행됐다.

### C5. $23 target — **강한 성공**
2004-02 stock은 $37.16.

---

## 3. 실제 경로

| 시점 | 사건 |
|---|---|
| 2002-10 | VIC Long @ ~$10 |
| 2002-12 | fixed universal life business coinsurance |
| 2003 | strategic review → P&C 집중 |
| 2004-02 | stock **$37.16** |
| 2005-08 | Goldman Sachs에 variable life/annuity sale 계약 |
| 2005-12 | The Hanover Insurance Group로 사명 변경 |
| 2009 | remaining run-off life business sale 완료 |

---

## 4. Valuation hindsight

원문 SOTP:

`P&C $20 + life $3 = $23 target`

시장은 당시 life를 사실상 **-$10/share**로 가격화했다. 실제 restructuring은 life liability가 parent equity를 영구 소멸시키는 시나리오가 아님을 증명했다.

---

## 5. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| P&C $20 value | 25% | 성공 |
| life negative value 과도 | 30% | 강한 성공 |
| strategic alternatives | 20% | 성공 |
| capital release | 10% | 성공 |
| $23 target | 15% | 강한 성공 |

---

## 6. 무엇이 실제 수익을 만들었는가

multiple expansion보다 **liability uncertainty의 제거**였다. 복합금융사에서는 hated/run-off segment가 없어질 때 core franchise multiple이 되살아난다.

---

## 7. 재사용 가능한 교훈

1. insurance SOTP는 statutory capital을 legal entity별로 본다.
2. run-off book은 headline losses보다 capital release path를 계산한다.
3. 시장이 문제사업에 negative value를 주는 경우가 최고의 setup일 수 있다.
4. strategic alternatives는 말이 아니라 실제 reinsurance/sale로 검증한다.
5. simplification은 holding-company discount를 크게 줄일 수 있다.

---

## 8. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| SOTP thesis | 매우 강한 성공 |
| Catalyst | 성공 |
| Timing | 빠름 |
| Downside framing | 좋음 |
| Thesis score | 9.8/10 |
| Process score | 9.7/10 |
| 종합 | **매우 강한 성공 — $10→$23 target 초과, 2004 $37+** |

### 한 문장 교훈

> 복합보험사에서 문제사업이 **negative value로 가격화됐는데 실제로는 capital을 풀어줄 수 있다면** 큰 비대칭이 생긴다.

---

## 9. Sources / Validation Notes

1. VIC original / uploaded SQL, 2002-10-04.
2. Allmerica 2003 Annual Report — life sales cessation, universal-life coinsurance, P&C focus.
3. 2004-02 common stock price $37.16 from 2003 10-K.
4. Goldman Sachs / Allmerica 2005 variable-life transaction.
5. https://www.sec.gov/Archives/edgar/data/944695/000119312504037515/d10k.htm
6. https://www.goldmansachs.com/pressroom/press-releases/2005/2005-08-22
7. https://www.sec.gov/Archives/edgar/data/944695/000119312506056711/d10k.htm

### 데이터 품질
- T0 thesis: **A**
- restructuring/price outcome: **A**
