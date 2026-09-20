# Anthracite Capital Series D Preferred (AHRPRD) — 2007-08-06 VIC Long

> **Idea unit:** 2007-08-06 Anthracite Capital 8.25% Series D cumulative preferred Long.
> **Research as-of:** 2026-09-20. 원 SQL은 Short지만 원문은 명백한 **preferred Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer | Anthracite Capital, Inc. |
| Security | **Series D cumulative preferred** |
| VIC 게시일 / 작성자 | 2007-08-06 / bowd57 |
| 실제 방향 | Preferred Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 가격 | **$13.67** |
| liquidation preference | **$25** |
| annual dividend | **$2.0625 / 8.25% of par** |
| current yield | 약 **15%** |
| callable | 2012 |
| thesis | recourse leverage modest + common-equity cushion + CRE losses manageable |
| terminal event | **2010 Chapter 7** |
| 2009 NYSE action | common + preferred C/D suspended/delisted |
| recovery | company said shareholders would receive **no value** in reorganization/liquidation scenario |
| 최종 판정 | **catastrophic failure — preferred cushion did not survive funding/liquidity collapse** |

> **결론:** 원문은 $25 par Series D를 $13.67에 사면서 15% current yield와 common-equity cushion을 샀다. 작성자는 reported D/E가 securitization accounting 때문에 과장됐고 recourse debt/equity는 약 1.7x라 liquidity risk가 낮다고 봤다. 그러나 2008~09 CRE/CMBS funding shock은 자산손실뿐 아니라 financing 구조 자체를 무너뜨렸다. Anthracite는 2009 말 securities가 NYSE에서 suspended/delisted됐고 2010-03-15 Chapter 7을 신청했다. **우선주 seniority는 enterprise funding collapse를 막지 못했다.**

---

## 1. Security를 정확히 본다

이 아이디어는 AHR common이 아니다.

Series D:
- $25 liquidation preference
- 8.25% cumulative coupon
- pari passu with Series C
- dividends six quarters 이상 arrears면 directors 선임권
- perpetual, callable 2012

였다.

따라서 payoff는:

**preferred recovery = available residual assets after debt / preferred claims**

이다.

---

## 2. 원문 투자논지

### C1. recourse leverage가 낮아 liquidity risk 제한 — **강한 실패**
repo/credit facilities와 mark-to-market funding risk가 crisis에서 핵심이 됐다.

### C2. common equity가 preferred를 보호 — **강한 실패**
common-equity book cushion은 stressed liquidation value가 아니었다.

### C3. CRE defaults만 합리적이면 preferred가 par 쪽으로 복귀 — **실패**
credit losses 이전에 capital-markets/funding 구조가 무너졌다.

### C4. BlackRock manager relationship optionality — **보호 못함**
external-manager affiliation은 rescue guarantee가 아니었다.

---

## 3. 실제 경로

| 시점 | 사건 |
|---|---|
| 2007-08 | VIC Long @ $13.67 |
| 2008~09 | CMBS/CRE marks + liquidity stress 급증 |
| 2009-12 | NYSE suspends common and Series C/D |
| 2009-12 | management says shareholders likely no value in reorg/liquidation |
| 2010-03-15 | voluntary Chapter 7 filing |

---

## 4. 분석 오류

가장 큰 오류는 **recourse leverage**만으로 liquidity risk를 낮게 본 것이다.

Mortgage REIT의 실제 stress equation:

**survival = collateral value + haircuts + repo availability + margin calls + unencumbered liquidity**

다.

GAAP book과 stated recourse D/E만으로는 funding run을 설명하지 못한다.

---

## 5. 재사용 가능한 교훈

1. preferred seniority는 debt/funding claims 뒤의 residual seniority다.
2. mortgage REIT는 book equity보다 daily liquidity를 stress-test한다.
3. repo haircut과 margin-call sensitivity를 별도 모델링한다.
4. external manager의 reputation은 explicit support contract가 아니다.
5. $25 par는 recovery floor가 아니다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Security identification | preferred Long |
| Yield thesis | 초기 carry only |
| Liquidity underwriting | 강한 실패 |
| Recovery | 사실상 전손 |
| Thesis score | 0.5/10 |
| Process score | 9.9/10 |
| 종합 | **catastrophic failure — $13.67 preferred가 Chapter 7로 가치 소멸** |

### 한 문장 교훈

> **우선주는 부채보다 후순위이고, funding run이 시작되면 높은 coupon과 par value는 아무런 방어막이 아닐 수 있다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2007-08-06.
2. Anthracite 2009 NYSE suspension and management no-value assessment: https://www.sec.gov/Archives/edgar/data/1050112/000134100409002401/anthracite_8k.htm
3. Chapter 7 filing, 2010-03-15: https://www.sec.gov/Archives/edgar/data/1050112/000134100410000503/form_8k.htm

### 데이터 품질
- T0 security/thesis: **A**
- bankruptcy outcome: **A**
- exact dividend-adjusted loss: **not reconstructed**
