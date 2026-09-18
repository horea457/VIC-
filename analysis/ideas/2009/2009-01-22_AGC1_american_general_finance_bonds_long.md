# American General Finance Senior Unsecured Bonds (AGC1) — 2009-01-22 VIC Long

> **Idea unit:** 2009-01-22 American General Finance senior unsecured debt Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 원문은 **bond Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer | American General Finance Corp. |
| VIC 게시일 / 작성자 | 2009-01-22 / madmax989 |
| 실제 방향 | **Senior unsecured debt Long** |
| 원 SQL 방향 | **Short — 오류** |
| 추천 maturity | 주로 **2011~2012 senior bonds** |
| 당시 가격 | 대략 **50~60 cents on par** |
| 원문 expected YTM/IRR | **35~45%** held-to-maturity |
| 핵심 논지 | no secured debt ahead + consumer-loan cash flow + AIG/Fortress strategic support |
| 2010 corporate event | Fortress가 AGF 80% 지분 인수 |
| 후속 사명 | Springleaf Finance |
| 최종 판정 | **강한 성공 — near-term unsecured claims survived and refinanced; exact CUSIP IRR 미확정** |

> **결론:** 원문은 AIG crisis 당시 AGF senior unsecured bonds가 50~60c까지 떨어졌지만, consumer-loan asset cash flow와 seniority를 고려하면 near-term maturities의 recovery가 크게 과소평가됐다고 봤다. 실제 AIG는 2010 Fortress에 AGF 80%를 매각했고 회사는 Springleaf로 재편됐다. 원문이 특정 CUSIP를 완전히 보존하지 않아 bond-by-bond IRR을 만들지는 않지만, **issuer가 청산되지 않고 near-term senior unsecured debt가 정상적으로 servicing/refinancing된 점에서 security thesis는 강하게 적중**했다.

---

## 1. 증권을 먼저 본다

이 아이디어는 AGF common equity가 아니다.

핵심 질문은:

**stressed loan value - operating/administrative claims - secured claims = unsecured bond recovery**

였다.

원문은 당시 AGF capital structure에서 senior unsecured noteholders 앞에 큰 secured debt layer가 없다는 점을 중요하게 봤다.

---

## 2. 원문 투자논지 지도

### C1. 50~60c 가격은 과도한 default/recovery haircut — **성공**
issuer는 going concern으로 유지됐다.

### C2. near-term maturity bonds가 가장 매력적 — **성공**
duration이 짧아 uncertainty를 줄이고 maturity/refinancing catalyst를 앞당겼다.

### C3. consumer-loan cash flows가 debt service를 지지 — **성공 방향**
Fortress가 business를 인수해 continuation value를 인정했다.

### C4. AIG 또는 buyer가 franchise를 보존 — **강한 성공**
Fortress-managed funds가 2010-11-30 80% economic interest를 인수했다.

### C5. 35~45% IRR — **정확 검증 유보**
정확한 CUSIP·coupon·purchase date별 cash flow가 없어 숫자를 재현하지 않는다.

---

## 3. 실제 경로

| 시점 | 사건 |
|---|---|
| 2009-01 | senior unsecured bonds ~50~60c |
| 2010-08 | AIG/Fortress sale agreement |
| 2010-11-30 | Fortress 80% acquisition completed |
| 2011 이후 | company renamed Springleaf; capital markets refinancing 지속 |
| 이후 | near-term unsecured notes serviced/refinanced |

---

## 4. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| distressed price too low | 30% | 강한 성공 |
| unsecured seniority value | 20% | 성공 |
| near-term maturity selection | 20% | 성공 |
| strategic transaction | 20% | 강한 성공 |
| exact IRR | 10% | 미확정 |

---

## 5. 재사용 가능한 교훈

1. financial distressed credit는 common-equity solvency narrative와 분리한다.
2. 동일 issuer에서도 maturity 선택이 recovery duration을 크게 바꾼다.
3. secured claims가 적은 unsecured bond는 생각보다 강한 position일 수 있다.
4. strategic buyer가 franchise value를 인정하면 credit claim이 먼저 회복될 수 있다.
5. CUSIP가 없으면 exact IRR을 만들지 않는다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Credit underwriting | 강한 성공 |
| Security selection | 강한 성공 |
| Catalyst | 성공 |
| Exact IRR | 미확정 |
| Thesis score | 9.2/10 |
| Process score | 9.8/10 |
| 종합 | **강한 성공 — distressed senior bonds의 survival/refinancing thesis 적중** |

### 한 문장 교훈

> 금융사 위기에서는 “회사 망하나?”보다 **내 채권 만기까지 어떤 현금흐름과 선순위 청구권이 버텨주는가**가 더 중요하다.

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2009-01-22.
2. Fortress/AIG acquisition completion: https://www.sec.gov/Archives/edgar/data/25598/000134100410001987/ex99-1.htm
3. Springleaf 2010 annual filing, company lineage and 80% Fortress transaction: https://www.sec.gov/Archives/edgar/data/25600/000002560011000014/inc1210.htm

### 데이터 품질
- T0 bond thesis: **A**
- corporate outcome: **A**
- exact bond-level IRR: **미확정**
