# Ahern Rentals (AHERN) — 2012-12-17 VIC Second-Lien Long

> **Idea unit:** Ahern Rentals Senior Secured Second Lien Notes Long @ **65**.  
> **Research as-of:** 2026-09-20. Source SQL has `is_short=true`, but the original thesis explicitly says **“Buy ... Second Lien Notes @ 65”**; direction is corrected to Long.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Ahern Rentals / AHERN |
| VIC 게시일 / 작성자 | 2012-12-17 / eal820 |
| 실제 Security | Senior Secured Second Lien Notes |
| 실제 방향 | **Long** |
| entry | **65 cents on the dollar** |
| thesis type | Distressed credit / fulcrum-security / bankruptcy reorganization |
| 핵심 논지 | second lien이 fulcrum이 될 가능성 + equipment-rental recovery + branch operating leverage |
| bankruptcy filing | 2011-12-22 |
| plan confirmation | 2013-06-05/06 |
| emergence | 2013-06-24 |
| 실제 recovery | **par + pre-petition interest** |
| 최종 판정 | **매우 강한 성공 — fulcrum equity는 아니었지만 65 매수 채권이 par+interest로 현금 회수** |

> **결론:** 원문은 65에 거래되던 second lien이 구조조정의 fulcrum이 되어 equity를 받을 가능성을 봤다. 최종 결과는 오히려 더 단순하고 좋았다. Ahern의 기존 오너들은 지분 100%를 유지했고, second-lien holders는 **허용채권 100%, 즉 par + pre-petition interest**를 받았다. 65 매수 기준 원금 회수만으로 약 **+53.8%**이고 이자가 추가됐다. 투자 논지의 “equity conversion” 경로는 빗나갔지만 **recovery underwriting**은 크게 맞았다.

---

## 1. 원문 투자논지

원문은 Ahern Rentals의 9.25% Senior Secured Second Lien Notes를 65에 매수했다.

핵심은:
- 2012년 revenue 약 $389m, branch network 70개+,
- 장비렌탈 업황 회복,
- 2009년 이후 branch build-out 비용이 먼저 반영되고 revenue ramp가 늦게 나타난 operating leverage,
- debtor exclusivity 종료로 creditor plan 제출 가능,
- Oppenheimer EV estimate 약 $680~790m,
- 약 $240m second-lien claims가 capital structure에서 fulcrum이 될 가능성

이었다.

원문은 reorganized equity를 받는 시나리오에서 큰 upside를 계산했지만, 동시에 illiquidity/value-trap risk도 인지했다.

---

## 2. 실제 bankruptcy outcome

2013년 6월 법원은 Ahern의 amended reorganization plan을 승인했다. 결과는:

- Don Ahern / John Paul Ahern이 reorganized equity **100% 유지**
- second lien holders: **face amount + accrued prepetition interest**
- 기타 creditors: **100% allowed claims**
- 회사는 2013-06-24 Chapter 11에서 공식적으로 exit

즉 second lien은 equity로 전환되지 않았다.

---

## 3. Return 구조

가격 65에 매수해 par 100을 회수하면:

**100 / 65 - 1 = +53.8%**

여기에 pre-petition interest가 추가된다. 게시일에서 emergence까지 약 반년이므로 realized IRR은 매우 높다.

이 아이디어에서 중요한 것은 “fulcrum security라는 명칭을 맞혔는가”보다 **downside waterfall과 enterprise value가 65보다 충분히 높은가**였다.

---

## 4. 왜 성공했나

### ① Asset coverage를 equity story보다 먼저 봤다
원문은 장비 렌탈 industry multiples, fleet value, EBITDA recovery를 여러 방법으로 교차검증했다.

### ② 업황 회복이 bankruptcy 협상력을 바꿨다
회사가 Chapter 11 동안 revenue와 EBITDA를 개선하면서 refinance가 가능해졌다.

### ③ 65라는 entry price가 legal-path error를 흡수했다
작성자가 예상한 equity conversion이 일어나지 않아도 par recovery만으로 큰 return이 가능했다.

---

## 5. 재사용 가능한 Distressed Credit 식

**Expected recovery = Σ(state probability × security recovery in state)**

그리고:

**Credit IRR ≠ reorganized equity upside only**

좋은 distressed credit은 특정 restructuring path를 맞히지 않아도, 여러 가능한 경로에서 매입가보다 recovery가 충분히 높아야 한다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Direction metadata | raw Short → **Long correction** |
| EV / recovery underwriting | 매우 성공 |
| Fulcrum-equity path | 실패 |
| Security recovery | 매우 성공 |
| Timing | 매우 성공 |
| Thesis score | **9.5/10** |
| Process score | **9.9/10** |

### 한 문장 교훈

> **distressed credit에서 가장 좋은 margin of safety는 ‘어떤 plan이 이겨도 매입가보다 recovery가 높다’는 구조다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2012-12-17.
2. Ahern plan confirmation: https://www.rermag.com/news-analysis/headline-news/article/20948068/ahern-reorganization-plan-confirmed-by-bankruptcy-court
3. Ahern emergence: https://www.rermag.com/news-analysis/headline-news/article/20948140/ahern-rentals-emerges-from-chapter-11
4. Bankruptcy case summary: https://www.lopucki.law.ufl.edu/companyinfo.php?name=Ahern+Rentals%2C+Inc.
5. Later strategic value cross-check — United Rentals acquired Ahern in 2022 for about $2.0bn cash.

### 데이터 품질
- T0 thesis: **A**
- bankruptcy outcome: **A-/B+**
- recovery terms: **A-/B+**, multiple independent contemporaneous reports agree
