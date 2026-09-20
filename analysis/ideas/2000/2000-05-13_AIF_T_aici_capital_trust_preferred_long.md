# AICI Capital Trust 9% Preferred (AIF-T) — 2000-05-13 VIC Long

> **Idea unit:** 2000-05-13 AICI Capital Trust trust-originated preferred Long.
> **Research as-of:** 2026-09-20. 원 SQL은 Short지만 원문은 명백한 **trust preferred Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer | AICI Capital Trust / Acceptance Insurance Companies |
| VIC 게시일 / 작성자 | 2000-05-13 / rich116 |
| 실제 방향 | Trust preferred Long |
| 원 SQL 방향 | **Short — 오류** |
| security | **9% trust-originated preferred** |
| par | **$25** |
| maturity | ~30 years |
| callable | after **2002-09-30** |
| dividend deferral | issuer could defer up to **5 years** |
| thesis | restructuring + crop insurance profitability + continued dividend + capital gain |
| parent bankruptcy | **Chapter 11, 2005-01-07** |
| later outcome | company sought Chapter 7 conversion in 2010 |
| company recovery assessment | preferred holders expected **no material distributions** |
| 최종 판정 | **catastrophic failure — trust preferred credit risk dominated yield** |

> **결론:** 이 아이디어는 Acceptance Insurance common이 아니라 **AICI Capital Trust 9% trust preferred**였다. 당시 management가 dividend deferral 계획이 없다고 말했고, crop-insurance business와 investment portfolio가 restructuring 이후 preferred를 지지할 것으로 기대했다. 그러나 parent는 2005 Chapter 11을 신청했고 2010에는 Chapter 7 conversion을 추진하면서 회사가 직접 trust-preferred holders에게 **material distribution이 없을 것**이라고 밝혔다. coupon carry가 있었더라도 terminal principal recovery가 사실상 사라진 실패다.

---

## 1. Security Mechanics

- $25 par
- 9% coupon
- callable after 9/30/2002
- trust structure
- dividend deferral up to five years

핵심은 “preferred”라는 이름보다 **parent insurer의 subordinated credit claim**이라는 점이다.

---

## 2. Claim Map

### C1. dividend continues — **초기에는 가능**
하지만 terminal credit risk가 더 중요했다.

### C2. insurance restructuring succeeds — **실패**
parent eventually filed bankruptcy.

### C3. crop-insurance value supports claim — **불충분**
asset/business value가 senior creditors 아래서 preferred recovery로 남지 않았다.

### C4. par/call optionality — **실패**
call value는 solvency가 있을 때만 존재한다.

---

## 3. 실제 경로

| 시점 | 사건 |
|---|---|
| 2000-05 | VIC preferred Long |
| 2000~04 | restructuring / dividends over part of period |
| 2005-01-07 | Acceptance Insurance Chapter 11 |
| 2010 | proposed conversion to Chapter 7 |
| 2010 | company says AICI preferred holders not expected material distributions |

---

## 4. 재사용 가능한 교훈

1. trust preferred는 equity-like income이 아니라 subordinated credit다.
2. deferrable coupon은 true default protection이 아니다.
3. insurer book value는 holding-company creditor recovery와 다르다.
4. callable-at-par optionality에 solvency probability를 곱한다.
5. 높은 yield의 핵심은 coupon보다 terminal principal recovery다.

---

## 5. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Income thesis | 초기 carry 가능 |
| Restructuring | 실패 |
| Principal recovery | 사실상 없음 |
| Thesis score | 0.5/10 |
| Process score | 9.9/10 |
| 종합 | **catastrophic failure — subordinated preferred recovery 소멸** |

### 한 문장 교훈

> **trust preferred의 9% coupon보다 parent company bankruptcy waterfall이 훨씬 중요하다.**

---

## 6. Sources / Validation Notes

1. VIC original: https://www.valueinvestorsclub.com/idea/AICI_Capital_Trust/4248830994
2. Acceptance Insurance 2010 8-K — 2005 Chapter 11, Chapter 7 conversion intent, no material distributions expected for AICI Capital Trust preferred holders: https://www.sec.gov/Archives/edgar/data/74783/000119312510184703/d8k.htm

### 데이터 품질
- T0 security/thesis: **A**
- bankruptcy/recovery: **A**
- exact dividend-adjusted IRR: **not reconstructed**
