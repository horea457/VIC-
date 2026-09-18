# Advent Claymore Convertible Securities and Income Fund II (AGC) — 2016-01-17 VIC Long

> **Idea unit:** 2016-01-17 AGC closed-end fund common-share Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 원문은 명백한 **Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Fund / Ticker | Advent Claymore Convertible Securities and Income Fund II / AGC |
| VIC 게시일 / 작성자 | 2016-01-17 / jcoviedo |
| 실제 방향 | Closed-end fund common-share Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 NAV discount | 약 **18.95%** |
| 당시 distribution | 월 **$0.047**, 연환산 yield 약 **11.4%** |
| leverage | investments 약 **174.5% of net assets** |
| key thesis | liquid marked assets + extreme discount + distribution + activist/tender optionality |
| FY2016 market/NAV return | **+6.68% / -0.65%** |
| FY2017 market/NAV return | **+21.79% / +14.03%** |
| FY2017 ending discount | 약 **8.0%** |
| 2017 catalyst | 15% tender offer |
| 2018 terminal event | AVK에 NAV-for-NAV merger |
| 최종 판정 | **강한 성공 — discount narrowing + distributions + tender/merger** |

> **결론:** 원문은 AGC의 underlying assets가 대부분 Level 1/2 liquid securities인데 closed-end fund market price만 NAV 대비 약 19% 할인된 점을 샀다. 실제 FY2017 말 discount는 약 8%까지 좁혀졌고, 2017년 15% tender offer, 2018년 AVK와의 NAV-for-NAV merger가 이어졌다. 높은 leverage와 return-of-capital distribution이라는 위험은 있었지만 **discount-closure thesis는 분명히 적중**했다.

---

## 1. 무엇을 샀는가

AGC는 convertibles와 high-yield securities를 보유한 leveraged closed-end fund였다.

핵심식:

**CEF common value = NAV × (1 - market discount) + distributions - leverage drag**

원문에서 중요한 점은 underlying holdings가 opaque private assets가 아니라 mostly marked liquid securities였다는 것이다.

---

## 2. 원문 투자논지 지도

### C1. ~19% discount는 과도 — **강한 성공**
FY2017 말 NAV $6.73, market $6.19로 discount가 약 8%까지 축소됐다.

### C2. 11%대 distribution이 carry 제공 — **성공, 단 quality 주의**
2015 distribution의 약 36%가 return of capital이었다. 따라서 headline yield 전부를 economic income으로 볼 수는 없다.

### C3. credit stabilization이 NAV와 discount를 동시에 돕는다 — **성공**
FY2017 NAV return +14.03%, market return +21.79%로 discount narrowing이 추가 알파를 만들었다.

### C4. activist/tender optionality — **강한 성공**
2017 fund는 common shares의 최대 15% tender를 실시했고 oversubscribed됐다.

### C5. liquidation/merger optionality — **강한 성공**
2018-08-27 AGC는 AVK에 합병됐고 AGC holders는 보유 NAV와 동일한 aggregate NAV의 AVK shares를 받았다.

---

## 3. 실제 경로

| 시점 | 결과 |
|---|---|
| 2016-01 | VIC Long, discount ~18.95% |
| FY2016 | market +6.68%, NAV -0.65% |
| 2017-09 | 15% tender offer, oversubscribed |
| FY2017 | market +21.79%, NAV +14.03%, discount ~8% |
| 2018-08-27 | AGC merged into AVK at NAV-equivalent exchange |

---

## 4. 왜 distribution yield만 보면 안 되는가

CEF에서 distribution은:
- investment income,
- realized gains,
- return of capital

이 섞일 수 있다.

따라서 **distribution yield ≠ portfolio earning yield**다.

AGC 2015 distribution 중 상당 부분이 ROC였으므로 원문 thesis의 핵심은 yield 자체가 아니라 **liquid NAV discount**였다.

---

## 5. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| discount cheapness | 30% | 강한 성공 |
| liquid NAV reliability | 20% | 성공 |
| distribution carry | 15% | 성공/quality 낮음 |
| tender/activism | 20% | 강한 성공 |
| merger/liquidation optionality | 15% | 강한 성공 |

---

## 6. 재사용 가능한 교훈

1. CEF는 price보다 **discount-to-NAV**를 먼저 본다.
2. NAV quality는 Level 1/2/3 composition으로 검증한다.
3. distribution yield에서 return of capital을 분리한다.
4. leverage는 NAV volatility를 증폭한다.
5. tender와 NAV-for-NAV merger는 discount thesis의 강한 catalyst다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| NAV thesis | 성공 |
| Discount thesis | 강한 성공 |
| Catalyst | 강한 성공 |
| Distribution quality | 혼합 |
| Thesis score | 9.2/10 |
| Process score | 9.8/10 |
| 종합 | **강한 성공 — ~19% discount가 ~8%로 축소되고 tender·NAV merger까지 발생** |

### 한 문장 교훈

> CEF deep value는 **싼 자산이 아니라 같은 자산을 NAV보다 얼마나 싸게 살 수 있고 그 discount를 무엇이 닫아주는가**의 문제다.

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2016-01-17.
2. AGC 2017 tender result: https://www.sec.gov/Archives/edgar/data/1391461/000139146117000002/avkagctenderfinalresultspr.htm
3. 2018 AGC/LCM-to-AVK merger proxy: https://www.sec.gov/Archives/edgar/data/1219120/000089180418000253/gug74131-497.htm
4. AVK 2019 report confirming 2018-08-27 merger and NAV-equivalent share exchange: https://www.sec.gov/Archives/edgar/data/1219120/000089180419000224/gug76254-ncsr.htm

### 데이터 품질
- T0 thesis: **A**
- tender/merger: **A**
- fund returns: **A**
