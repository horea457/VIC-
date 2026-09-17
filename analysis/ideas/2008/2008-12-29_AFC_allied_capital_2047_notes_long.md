# Allied Capital 6.875% Notes due 2047 (AFC) — 2008-12-29 VIC Long

> **Idea unit:** 2008-12-29 exchange-traded senior unsecured note Long.
> **Research as-of:** 2026-09-18. 분석 증권은 Allied Capital common이 아니라 **6.875% senior unsecured notes due 2047, NYSE:AFC**다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer | Allied Capital Corporation |
| Security / Ticker | 6.875% Senior Notes due 2047 / AFC |
| VIC 게시일 / 작성자 | 2008-12-29 / doggy835 |
| 실제 방향 | Senior unsecured note Long |
| 당시 가격 | 약 **35~36% of par** |
| par | **$25/security** |
| current yield | 약 **19~20%** |
| 핵심 protection | BDC 1:1 debt/equity asset-coverage constraint |
| 2010 event | Ares Capital acquired Allied and **assumed AFC debt** |
| 2021 event | Ares redeemed all remaining 2047 notes at **$25 par + accrued interest** |
| 최종 판정 | **매우 강한 성공 — distressed credit security selection 적중** |

> **결론:** 원문은 Allied Capital의 accounting과 asset quality를 신뢰한 게 아니라, **80%+ asset haircut을 해도 35c debt가 covered되는지**를 봤다. 2010 Ares Capital이 Allied를 인수하며 AFC를 포함한 unsecured debt를 승계했고, 2021 남은 2047 notes를 par $25 + accrued interest에 전액 상환했다. 2008 entry가 약 $9 per $25 par 수준이었다는 점을 감안하면 매우 강한 security-level 성공이다.

---

## 1. 증권 구조

AFC는:
- 6.875% coupon
- $25 par
- 2047 maturity
- senior unsecured
- Allied Capital의 다른 unsecured notes와 pari passu

였다.

중요한 것은 common equity story가 아니라 **asset coverage와 debt seniority**였다.

---

## 2. 원문 투자논지 지도

### C1. 35c price는 극단적 asset impairment를 반영 — **성공**
회사가 독립적으로 끝까지 생존할 필요조차 없었다. credit claim이 다른 stronger issuer로 이전될 수 있었다.

### C2. BDC leverage rule이 creditor를 보호 — **성공**
asset coverage requirement는 debt reduction pressure를 만들었다.

### C3. nearer-maturity debt가 먼저 상환돼도 AFC residual coverage 충분 — **성공**
AFC는 가장 긴 maturity였지만 2010 Ares assumption으로 credit quality가 크게 개선됐다.

### C4. equity raise/debt reduction catalyst — **경로 변경**
실제 decisive catalyst는 Ares acquisition이었다.

### C5. par recovery — **최종 강한 성공**
2021 Ares가 잔여 notes를 $25 par + accrued interest에 redeem했다.

---

## 3. 실제 경로

| 시점 | 사건 |
|---|---|
| 2008-12 | AFC ~35~36c of par |
| 2009 | Allied liquidity/asset concerns 지속 |
| 2010-04 | Ares Capital acquires Allied; ~$745.5m unsecured notes assumed |
| 2011 | shorter-dated Allied notes redeemed |
| 2012 이후 | 2047 AFC redeemable at par |
| 2021-03 | remaining ~$230m AFC notes **par redemption** |

---

## 4. Payoff Structure

단순 principal comparison만 보면:

`$25 / ~$9 - 1 ≈ +178%`

여기에 장기간 6.875% coupon이 추가된다. 다만 exact purchase price·coupon dates·매도시점이 없으므로 realized IRR은 계산하지 않는다.

---

## 5. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| severe haircut에도 coverage | 30% | 성공 |
| BDC leverage protection | 20% | 성공 |
| seniority 가치 | 20% | 성공 |
| catalyst | 10% | M&A로 경로 변경 |
| par recovery | 20% | 강한 성공 |

---

## 6. 무엇이 실제 수익을 만들었는가

Allied의 business quality가 좋아진 것이 아니라 **claim이 Ares Capital balance sheet로 이동**했다. distressed credit에서는 회사 narrative보다 legal security가 우선이라는 사례다.

---

## 7. 재사용 가능한 교훈

1. exchange-traded debt를 common ticker처럼 처리하지 않는다.
2. BDC는 statutory asset-coverage constraint를 creditor analysis에 반영한다.
3. liquidation value는 asset haircut 후 debt waterfall로 본다.
4. long-dated note도 change-of-control/merger가 duration을 사실상 줄일 수 있다.
5. common이 위험해도 senior debt가 좋은 투자일 수 있다.

---

## 8. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Credit underwriting | 강한 성공 |
| Security selection | 매우 강한 성공 |
| Catalyst | M&A |
| Ultimate recovery | par + coupons |
| Thesis score | 9.8/10 |
| Process score | 9.8/10 |
| 종합 | **매우 강한 성공 — 35c distressed debt가 결국 par 회수** |

### 한 문장 교훈

> distressed credit의 질문은 “회사가 좋은가?”가 아니라 **내 채권 앞에 얼마의 손실흡수 자본이 있는가?**다.

---

## 9. Sources / Validation Notes

1. VIC original / uploaded SQL, 2008-12-29.
2. Ares Capital 2010 merger filing — Allied unsecured notes assumed.
3. Ares 2021 redemption notice — all 6.875% 2047 notes redeemed at $25 + accrued interest.
4. https://www.sec.gov/Archives/edgar/data/1287750/000104746910003449/a2197910z8-k.htm
5. https://www.sec.gov/Archives/edgar/data/1287750/000128775021000014/arcc-2047seniornotesredemp.htm

### 데이터 품질
- T0 security/price: **A**
- assumption/redemption: **A**
- exact IRR: **미확정**
