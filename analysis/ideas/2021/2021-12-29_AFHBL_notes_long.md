# Atlas Financial Holdings 6.625% Notes (AFHBL) — 2021-12-29 VIC Long

> **Idea unit:** 2021-12-29 Atlas Financial Holdings exchange-traded senior unsecured note Long.
> **Research as-of:** 2026-09-18. 분석 증권은 common이 아니라 **6.625% Senior Unsecured Notes due 2022 (AFHBL)**다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer | Atlas Financial Holdings |
| Security / Ticker | 6.625% Senior Unsecured Notes due 2022 / AFHBL |
| VIC 게시일 / 작성자 | 2021-12-29 / mrsox977 |
| 실제 방향 | Debt Long |
| 원 SQL 방향 | Long |
| 당시 가격 | 약 **$10 per $25 par** (~40c on dollar) |
| 당시 상태 | payment default / restructuring |
| 핵심 catalyst | scheme of arrangement → new 2027 notes |
| 실제 exchange | 2022-04-14 completed |
| new security | **6.625% cash / 7.25% PIK Senior Unsecured Notes due 2027** |
| exchange principal | old $25 + accrued unpaid interest |
| 2027 maturity | **2027-04-27 — 아직 미래** |
| 최종 판정 | **restructuring catalyst 성공 / 최종 credit recovery는 미확정·위험 확대** |

> **결론:** 원문은 $25 par note를 약 $10에 사서 restructuring 후 새 paper가 high-teens 이상으로 거래될 수 있다고 봤다. 실제 2022년 4월 old notes는 취소되고 **$25 + accrued unpaid interest** 상당의 new 2027 notes로 교환됐다. 하지만 이것은 par recovery가 아니라 **principal claim의 재표시**다. 2024 회사는 핵심 subsidiaries를 secured lender에게 넘겨 약 $12.7m debt를 소멸시켜야 했고, 따라서 2027 만기 전 최종 회수율은 아직 확정할 수 없다.

---

## 1. 증권 구조

원 note:
- $25 par
- 6.625% coupon
- senior unsecured
- 2022 maturity

restructuring 후:
- initial aggregate principal 약 **$26.64m**
- 6.625% cash / 7.25% PIK
- maturity **2027-04-27**
- unsecured

---

## 2. 원문 투자논지 지도

### C1. restructuring은 실제로 완료될 것 — **성공**
2022-02 scheme vote에서 voting notes의 약 **99.34%**가 찬성했고 2022-04-14 effective.

### C2. old $25 principal이 new note에서 보존 — **성공**
각 old note는 $25 + accrued unpaid interest 상당의 new principal로 교환됐다.

### C3. post-exchange note가 high-teens로 rerate — **미확정**
공개 시장가격의 일관된 series가 없어 확정하지 않는다.

### C4. MGA recovery가 최종 par을 지지 — **위험 확대**
2024 core subsidiaries가 secured lender에게 이전된 것은 credit deterioration의 강한 경고다.

### C5. $10 entry는 충분한 margin of safety — **최종 미확정**
2027 maturity 전이라 realized recovery 판정 불가.

---

## 3. 실제 경로

| 날짜 | 사건 |
|---|---|
| 2021-12 | VIC Debt Long @ ~$10 |
| 2022-02-25 | Cayman Court scheme 승인 |
| 2022-04-14 | old notes cancelled / new 2027 notes issued |
| 2022 | 6.625% cash / 7.25% PIK toggle 구조 |
| 2024-01 | core subsidiaries transferred to secured lender for ~$12.7m debt satisfaction |
| 2027-04-27 | contractual maturity — future |

---

## 4. 왜 exchange principal을 recovery로 보면 안 되는가

$25 old principal이 $25+ accrued interest new principal로 바뀌어도 **market value가 $25가 된 것은 아니다**.

distressed exchange에서는:
`recovery = market value of new security + cash received`
로 봐야 한다.

---

## 5. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| restructuring completion | 25% | 성공 |
| face principal preservation | 20% | 성공 |
| post-deal rerating | 15% | 미확정 |
| operating/MGA recovery | 20% | 악화 |
| ultimate recovery | 20% | 미확정 |

---

## 6. 재사용 가능한 교훈

1. distressed exchange의 face principal을 realized recovery로 착각하지 않는다.
2. maturity extension은 default 해결이 아니라 duration 연장일 수 있다.
3. PIK toggle은 liquidity를 돕지만 creditor compounding이 실제 현금회수를 보장하지 않는다.
4. secured lender가 operating subsidiaries를 가져가면 unsecured recovery가 급격히 나빠질 수 있다.
5. 아직 만기가 오지 않은 debt는 final verdict를 유보한다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Restructuring catalyst | 성공 |
| Security conversion | 성공 |
| Operating credit | 악화 |
| Ultimate recovery | 미확정 |
| Thesis score | 6.0/10 provisional |
| Process score | 9.7/10 |
| 종합 | **중간 판정 — exchange 성공, 2027 최종 회수 미확정** |

### 한 문장 교훈

> distressed bond에서 **par-for-par exchange는 돈을 번 것이 아니라 청구권의 만기를 뒤로 민 것**일 수 있다.

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2021-12-29.
2. Scheme approval: https://www.sec.gov/Archives/edgar/data/1539894/000153989422000005/afhifpressrelease030122.htm
3. Exchange effective: https://www.sec.gov/Archives/edgar/data/1539894/000153989422000015/afh-20220414.htm
4. New note terms: https://www.sec.gov/Archives/edgar/data/1539894/000153989422000015/formofnoterepresenting6625.htm
5. 2024 subsidiary transfer: https://www.sec.gov/Archives/edgar/data/1539894/000110465924008805/tm244617d1_8k.htm

### 데이터 품질
- T0 security: **A**
- restructuring terms: **A**
- final recovery: **미확정 — maturity 2027**
