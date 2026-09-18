# Arctic Glacier Income Fund (AGUNF) — 2019-11-18 VIC Residual Cash Long

> **Idea unit:** 2019-11-18 Arctic Glacier Income Fund residual-liquidation trust-unit Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 실제는 **residual cash Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer / Ticker | Arctic Glacier Income Fund / AGUNF |
| VIC 게시일 / 작성자 | 2019-11-18 / value_31 |
| 실제 방향 | Residual liquidation Long |
| 원 SQL 방향 | **Short — 오류** |
| entry | 약 **US$0.0165** |
| critical ex-date | **2019-11-14** |
| 2019 C$0.042818335 distribution | idea date에는 **권리 없음** |
| post-distribution cash estimate | 약 **C$9.4m / ~US$0.02 per unit** |
| expected gross upside | **20%+** |
| actual future 2020 distribution | **C$0.01427278** |
| actual final 2022 distribution | **C$0.00549502** |
| future CAD distributions total | **C$0.01976780** |
| 최종 판정 | **실패 — nominal cash estimate는 근접했지만 FX·cost·3년 delay로 투자수익 미흡** |

> **결론:** 원문은 2019년 11월 이미 대부분 청산된 fund를 $0.0165에 사고, ex-distribution 이후 남아 있는 cash가 약 $0.02/unit이라 20% 이상을 짧은 기간에 받을 수 있다고 봤다. 중요한 점은 2019년 C$0.042818335 distribution의 ex-date가 11월 14일이라 **11월 18일 매수자는 그 분배를 받을 수 없었다**는 것이다. 이후 실제로 받은 것은 2020 C$0.01427278과 2022 C$0.00549502, 합계 C$0.0197678이다. 당시 환율로 USD 환산하면 대략 $0.015 안팎으로 entry $0.0165에 못 미치거나 비슷한 수준이고, 지급도 3년 걸렸다. short-duration 20%+ thesis는 실패다.

---

## 1. 원문 투자논지

원문은:
- operating liabilities 사실상 없음,
- post-Nov-2019 distribution cash 약 C$9.4m,
- remaining expenses 작음,
- final update imminent,
- market cap below residual cash

라고 봤다.

따라서 business analysis가 아니라 **cash minus wind-down expenses** 문제였다.

---

## 2. Ex-Date가 중요한 이유

2019 interim distribution:
- C$0.042818335/unit
- ex-date **2019-11-14**
- record date 2019-11-15
- payable 2019-12-06

VIC idea는 **2019-11-18**이므로 이 distribution은 post-entry cash flow가 아니다.

이를 포함하면 수익률을 크게 과대평가한다.

---

## 3. 실제 Post-Entry Distributions

| 시점 | Distribution |
|---|---:|
| 2020-09 | **C$0.01427278** |
| 2022-11 | **C$0.00549502 final** |
| 합계 | **C$0.01976780** |

USD 환산 exact return은 각 지급일 FX를 복원하지 않고 계산하지 않는다.

다만 typical CAD/USD 수준에서는 US$0.0165 entry에 대해 20%+ short-term return과 거리가 멀다.

---

## 4. Claim Map

### C1. residual cash exists — **성공**
후속 distributions가 실제 발생했다.

### C2. expenses/liabilities negligible — **과도**
수년간 wind-down이 지속됐다.

### C3. final distribution imminent — **강한 실패**
2022까지 지연.

### C4. >20% gross return — **실패**
미래 CAD distributions만 보면 entry 대비 매력적이지 않았다.

---

## 5. 재사용 가능한 교훈

1. liquidation event는 ex-date entitlement를 정확히 본다.
2. 이미 ex된 distribution을 투자 payoff에 포함하지 않는다.
3. no-liabilities에도 legal/admin/tax expenses가 남는다.
4. residual-cash trade는 duration이 길어지면 tiny spread가 사라진다.
5. cross-currency liquidation은 각 지급일 FX가 필요하다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Cash-existence thesis | 성공 |
| Expense/timing estimate | 실패 |
| 20%+ return thesis | 실패 |
| Final security outcome | 낮은/음의 IRR 가능 |
| Thesis score | 3.0/10 |
| Process score | 9.9/10 |
| 종합 | **실패 — cash는 있었지만 시간과 비용이 spread를 소진** |

### 한 문장 교훈

> residual cash trade에서 **몇 센트의 숨은 가치보다 ex-date와 지급기간이 훨씬 중요하다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2019-11-18.
2. 2019 distribution / ex-date: https://www.marketscreener.com/quote/stock/ARCTIC-GLACIER-INCOME-FUN-119074302/news/Arctic-Glacier-Income-Fund-Announces-Interim-Distribution-Payable-on-December-6-2019-34093203/
3. 2020 C$0.01427278 distribution: https://webfiles.thecse.com/PressRelease_-_Third_Interim_Distribution.pdf
4. 2022 final C$0.00549502 distribution: https://www.globenewswire.com/news-release/2022/11/07/2550327/0/en/arctic-glacier-income-fund-announces-final-distribution-and-delisting-from-the-cse.html

### 데이터 품질
- T0 thesis: **A**
- distribution/ex-date data: **A**
- exact USD IRR: **not reconstructed**
