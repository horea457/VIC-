# Adyen N.V. (ADYYF US / ADYEN NA) — 2019-08-26 VIC Long

> **Direction audit:** raw Long과 실제 방향 일치.
> **Entity note:** ADYYF는 미국 OTC 표기지만 경제적 underlying은 네덜란드 상장 Adyen N.V.와 동일하다. 2019-03 아이디어와 별도 thesis로 유지.
> **Research as-of:** 2026-09-11.

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2019-08-26 / StaminaVIC |
| 실제 방향 | **Long** |
| 당시 ADYEN 가격 | 약 **€639** |
| 원문 fair value | **€1,181** |
| 기대 upside | 약 **85%** |
| horizon | 약 **2년** |
| 핵심 | enterprise wallet-share + negligible volumetric churn + mid-market mix + operating leverage |
| 실제 | 2020-08 management share transaction **€1,365** |
| 최종 판정 | **매우 강한 성공** |

> **결론:** 2019-03 Long보다 이 글은 ‘왜 growth duration이 긴가’를 더 세밀하게 설명했다. 신규 merchant TAM이 아니라 기존 enterprise 고객의 wallet-share 확대, full-stack migration, unified commerce, mid-market take-rate가 성장의 층을 만들었다. €1,181 target은 약 1년 만에 초과됐고 2021 EBITDA margin 63%는 원문의 operating-leverage 가정을 직접 검증했다.

---

# 1. 당시 business mix

원문 기준:
- volume의 약 **97%가 large enterprise**
- volumetric churn **<1%**
- average take rate 약 **22bps**
- POS 약 10% 수준
- top customers 자체 매출/volume도 빠르게 성장

Adyen의 가장 중요한 특징은 merchant를 한번 따낸 뒤:
**국가 + payment method + channel + acquiring share**
를 계속 늘릴 수 있다는 점이었다.

즉 CAC를 매년 반복하지 않고 existing cohort가 스스로 커진다.

---

# 2. 원문의 differentiated thesis

### A. Wallet-share gain
2018 top customers organic growth가 약 35%였고 Adyen의 top-10 revenue growth 중 상당 부분이 wallet-share expansion에서 나왔다고 봤다.

### B. Mid-market has higher take rate
Magento, Salesforce, NetSuite 같은 ecosystem을 통해 들어오는 mid-market 고객은 largest enterprise보다 take rate가 대략 2배 높을 수 있어 mix가 revenue yield를 높인다.

### C. Unified commerce
online + physical POS를 한 stack으로 처리할수록 data/risk/authorization value가 커진다.

### D. Street deceleration assumptions too harsh
원문은 sell-side가 2018 약 60% 성장에서 2021 10%대까지 너무 빠른 deceleration을 가정한다고 봤다.

writer는 적어도 **500bp 이상 더 빠른 growth**를 기대.

### E. Margin >63% possible
consensus long-term ~59%보다 높게 보고, IFRS16 이후 **63%+**도 가능하다고 판단.

---

# 3. Valuation

원문 base:
- revenue growth 약 40% CAGR for 3 years
- EBITDA margin ~60%
- discount rate 8%
- terminal growth 3%

→ fair value **€1,181/share**.

당시 €639 대비 약 **+85%**.

이 valuation의 가장 민감한 변수는 단기 take rate보다:
1. growth duration
2. incremental margin
3. terminal competitive advantage

였다.

---

# 4. 실제 검증

2020-08 company-related share transaction:
**€1,365/share**.

즉 target €1,181은 약 1년 내 달성.

2021:
- processed volume €516bn, +70%
- net revenue 약 €1.0bn, +46%
- EBITDA 약 €630m, +57%
- EBITDA margin **63%**

원문이 가장 공격적으로 본 margin scenario까지 실제 숫자로 관찰됐다.

하지만 2023~24 회사가 다시 대규모 hiring/reinvestment를 하면서 margin은 50% 부근으로 내려왔다.

따라서:
**scalability는 맞지만 peak margin이 항상 유지된다는 뜻은 아니다.**

---

# 5. Claim Map

### C1. Enterprise churn is structurally low — **성공**
### C2. Existing customers create long growth runway — **강한 성공**
### C3. Mid-market/unified commerce adds second growth vector — **성공**
### C4. Street growth deceleration is too severe — **강한 성공**
### C5. EBITDA margin can exceed 60% — **성공, peak 기준**
### C6. €1,181 within ~2Y — **강한 성공, 약 1Y 내 달성**

---

# 6. 재사용 교훈

1. payment company는 TPV growth와 revenue growth를 분리한다.
2. take rate 하락이 나빠 보여도 mix/volume/incremental margin을 같이 본다.
3. churn이 낮은 enterprise software-like payment model은 cohort growth가 핵심.
4. 높은 multiple은 **duration error**가 있으면 오히려 싸다.
5. peak operating margin을 terminal margin과 동일시하지 않는다.

### 한 문장 교훈
> **좋은 플랫폼의 가치평가에서 가장 큰 오차는 다음 분기 성장률보다 ‘기존 고객이 몇 년 동안 얼마나 더 커질 수 있는가’를 잘못 보는 데서 나온다.**

## 7. Sources

1. VIC original / uploaded SQL, 2019-08-26.
2. Adyen 2020 share transaction at €1,365.
3. Adyen 2021 results.
4. Adyen subsequent annual/H1 results through 2026.
