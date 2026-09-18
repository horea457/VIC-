# Arctic Glacier Income Fund (AGUNF) — 2014-02-06 VIC Liquidation Long

> **Idea unit:** 2014-02-06 Arctic Glacier Income Fund liquidating trust-unit Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 실제는 **liquidation Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Issuer / Ticker | Arctic Glacier Income Fund / AGUNF |
| VIC 게시일 / 작성자 | 2014-02-06 / JetsFan |
| 실제 방향 | Liquidating trust-unit Long |
| 원 SQL 방향 | **Short — 오류** |
| entry | 약 **US$0.1945** |
| expected total distributions | **US$0.23~0.25** |
| expected nominal upside | **20~30%** |
| expected timing | 약 **1년** |
| expected IRR | **35%+** |
| initial actual distribution | **US$0.155570**, 2015-01-22 |
| later distribution | **C$0.042818335**, 2019 |
| later distribution | **C$0.01427278**, 2020 |
| final distribution | **C$0.00549502**, 2022 |
| 최종 판정 | **recovery direction은 맞았지만 timing/IRR thesis 실패** |

> **결론:** 2014 아이디어는 이미 operating assets를 매각한 Arctic Glacier의 남은 cash와 claims를 사는 liquidation trade였다. 첫 distribution은 2015년 **US$0.15557**로 예상 방향에 부합했다. 문제는 잔여 cash였다. 후속 distributions는 2019·2020·2022까지 늘어졌고, USD/CAD가 섞여 있어 exact realized IRR을 단순 합산할 수 없다. entry $0.1945 대비 원금은 대체로 회수 가능한 방향이었지만 **20~30%를 1년 내 얻고 35%+ IRR이라는 thesis는 명백히 실패**했다.

---

## 1. 원문 투자논지

원문은:
- cash roughly US$118m,
- claims roughly $32~38m,
- no operating business risk,
- Plan/claims resolution,
- expected distribution $0.23~0.25/unit

을 바탕으로 purely event-driven recovery를 봤다.

핵심 risk는 asset value가 아니라 **claims amount와 time-to-distribution**이었다.

---

## 2. Claim Map

### C1. large initial distribution — **성공**
2015-01-22 US$0.155570 지급.

### C2. total recovery > entry — **방향상 대체로 성공 가능**
후속 CAD distributions가 추가됐다.

### C3. one-year completion — **강한 실패**
final distribution은 2022년.

### C4. 35%+ IRR — **강한 실패**
잔여 cash가 5~8년 지연됐다.

### C5. cash/no operating risk means low risk — **부분 실패**
administrative, tax, claims, legal, currency and timing risks가 남았다.

---

## 3. Distribution Timeline

| 시점 | Distribution |
|---|---:|
| 2015-01-22 | **US$0.155570** |
| 2019-12 | **C$0.042818335** |
| 2020-09 | **C$0.01427278** |
| 2022-11 | **C$0.00549502 final** |

통화와 지급시점이 달라 exact IRR은 FX date를 복원하지 않고 산출하지 않는다.

---

## 4. 핵심 오류

Liquidation에서 residual cash는 안전해 보여도:
- tax clearance,
- litigation,
- claim reserves,
- monitor/administrative fees,
- court approvals,
- currency

때문에 지급이 오래 지연될 수 있다.

IRR은 **최종 회수액보다 시간에 훨씬 민감**하다.

---

## 5. 재사용 가능한 교훈

1. liquidation은 recovery amount와 payment date를 동시에 underwrite한다.
2. cash shell에도 administrative burn이 있다.
3. multiple currencies는 지급일 FX로 환산한다.
4. 1년 예상 liquidation이 8년 걸리면 nominal gain이 있어도 IRR은 실패다.
5. claims reserve의 release schedule을 catalyst map에 넣는다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Initial recovery | 성공 |
| Principal protection | 대체로 성공 방향 |
| Timing | 강한 실패 |
| IRR | 실패 |
| Thesis score | 5.0/10 |
| Process score | 9.8/10 |
| 종합 | **recovery thesis 부분 성공 / IRR thesis 실패** |

### 한 문장 교훈

> liquidation에서는 **1달러를 받는가보다 그 1달러를 언제 받는가가 수익률을 결정한다.**

---

## 7. Sources / Validation Notes

1. VIC original: https://www.valueinvestorsclub.com/idea/ARCTIC_GLACIER_INCOME_FUND/3321607643
2. Initial US$0.155570 distribution / Monitor report: https://www.alvarezandmarsal.com/sites/default/files/canada/twenty-second_report_of_the_monitor_may_27_2015.pdf
3. 2020 C$0.01427278 distribution: https://webfiles.thecse.com/PressRelease_-_Third_Interim_Distribution.pdf
4. 2022 final C$0.00549502 distribution: https://www.globenewswire.com/news-release/2022/11/07/2550327/0/en/arctic-glacier-income-fund-announces-final-distribution-and-delisting-from-the-cse.html

### 데이터 품질
- T0 thesis: **A**
- distribution history: **A/B**
- exact FX-adjusted IRR: **not reconstructed**
