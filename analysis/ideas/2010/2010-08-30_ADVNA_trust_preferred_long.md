# Advanta Capital Trust I 8.99% Trust Preferreds (ADVNA) — 2010-08-30 VIC Long

> **Security audit:** 이 아이디어는 Advanta common이 아니라 **8.99% Trust Preferreds due 2026**, 즉 파산 waterfall 안의 subordinated claim Long이다.
> **Direction audit:** raw Long과 실제 방향 일치.
> **Research as-of:** 2026-09-11.

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2010-08-30 / samba834 |
| Security | **Advanta Capital Trust I 8.99% Trust Preferreds due 2026** |
| 당시 가격 | 약 **14% of par** |
| 원문 expected recovery | 약 **67% of par** |
| 기대 payoff | 약 **5x** |
| 실제 누적 subordinated-note recovery | 약 **28.5c/$** |
| 실제 gross payoff | 약 **2.0x** vs entry 14 |
| 최종 판정 | **security selection 성공 / recovery valuation 과도** |

> **결론:** 파산회사라도 common equity가 아니라 어느 claim을 사느냐가 핵심인 사례다. 원문은 FDIC settlement 이후 trust preferred를 14에 사서 67 recovery를 기대했다. 실제 plan에서 trust preferred는 취소되고 같은 금액의 subordinated note claim으로 전환됐으며 누적 recovery는 약 28.5c였다. 따라서 방향과 seniority 분석은 맞았지만 asset recovery를 크게 과대평가했다.

---

# 1. Security / Waterfall

Advanta는 bankruptcy/liquidation 단계였다. 따라서 기업가치를 P/E로 볼 이유가 없다.

핵심 구조:
**recoverable assets - administrative/secured/senior claims - general unsecured claims = subordinated recovery pool**

ADVNA holders는 equity보다 앞서지만 senior notes/GUC보다 뒤에 있었다.

Plan effective date에 trust preferred securities 자체는 취소되고 holders는 해당 금액만큼 **Allowed Subordinated Note Claim**을 받았다.

---

# 2. 원문 recovery thesis

원문이 본 recoverable assets:
- tax refunds
- Visa B shares
- Fleet Services stake/cash flows
- credit-card receivables
- insurance/litigation recoveries
- art/other assets
- NOL은 보수적으로 거의 0

주요 claims:
- senior notes 약 $137m
- trust preferred/subordinated 약 $96m including accrued amounts
- GUC 등

FDIC settlement로 매우 큰 litigation uncertainty가 줄었다는 것이 핵심 catalyst였다.

---

# 3. 원문 Scenario

| Scenario | 확률 | Recovery |
|---|---:|---:|
| Worst | 5% | 7% |
| Low | 15% | 28% |
| Base | 50% | 69% |
| Best | 30% | 93% |

Probability-weighted expected recovery:
**약 67%**.

Entry ~14 대비 거의 **5x** payoff.

---

# 4. 실제 결과

Advanta liquidating trust distributions가 진행되며:
- GUC cumulative recovery는 약 **70.9c/$**
- **Subordinated Note Claims cumulative recovery는 약 28.5c/$**

수준까지 지급됐다.

trustee는 이후 material distributions를 크게 기대하지 않는다는 취지로 안내했다.

즉 entry 14 기준 단순 gross recovery:
**28.5 / 14 ≈ 2.0x**.

시간가치와 distribution timing을 포함한 exact IRR은 지급일별 cash-flow 재구성이 필요하므로 여기서는 산출하지 않는다.

---

# 5. Claim Map

### C1. Trust preferred is money-good enough at 14 — **성공**
0이 되지 않았고 약 2x gross recovery.

### C2. FDIC settlement materially de-risks waterfall — **성공 방향**
큰 법률 불확실성이 줄었다.

### C3. Asset recoveries support ~67c subordinated recovery — **실패**
실제 약 28.5c.

### C4. Claim seniority creates downside protection vs equity — **강한 성공**
common과 달리 의미 있는 recovery를 받았다.

### C5. 5x payoff — **실패**, 다만 positive special-situation return.

---

# 6. Process Error

좋은 부분은 **회사 전망이 아니라 claim waterfall을 분석**했다는 것이다.

틀린 부분은 여러 asset recovery assumptions가 동시에 우호적으로 작동해야 subordinated까지 67c가 내려온다는 사실을 충분히 haircut하지 않은 점이다.

특히 distressed에서는 asset value error가 junior claim에서 비선형적으로 증폭된다.

예:
- enterprise recovery 10% miss
- senior claims unchanged
→ subordinated residual은 30~50% 줄 수도 있다.

---

# 7. 재사용 체크리스트

1. distressed security는 ticker보다 **CUSIP/security class/seniority**를 먼저 적는다.
2. asset마다 recovery %와 timing을 분리한다.
3. legal settlement가 claim amount와 asset pool 중 무엇을 바꾸는지 본다.
4. junior claim은 EV sensitivity를 선형으로 처리하지 않는다.
5. 지급일이 여러 해에 걸치면 gross multiple과 IRR을 분리한다.
6. plan conversion(Preferred → claim)을 corporate action으로 기록한다.

### 한 문장 교훈
> **파산에서는 회사를 맞히는 것보다 어느 층의 청구권을 얼마에 사는지가 훨씬 중요하지만, junior recovery는 작은 asset-value 오차에도 크게 흔들린다.**

## 8. Sources

1. VIC original / uploaded SQL, 2010-08-30.
2. Advanta reorganization plan and liquidating-trust distribution notices: https://advantareorg.com/index.php3
3. Advanta SEC trust-preferred disclosures.
