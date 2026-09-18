# Pfizer / Allergan Merger Arbitrage Leg (AGN.PA) — 2016-02-19 VIC Arb Long Spread

> **Idea unit:** 2016-02-19 Pfizer/Allergan leg within a broader merger-arbitrage basket.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 이는 pair/basket 표현으로 보이며, 실제 경제적 방향은 **Long AGN deal spread / hedged PFE exposure**다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Deal | Pfizer / Allergan |
| VIC 게시일 / 작성자 | 2016-02-19 / mojoris |
| 실제 전략 | **Long merger spread, hedged/pair trade** |
| 원 SQL 방향 | **Short — 단순 방향값으로 부적절** |
| deal type | tax-inversion merger |
| original basket rank | Tier 2 / sizing opportunity |
| key perceived risk | antitrust / deal complexity |
| actual break catalyst | **U.S. Treasury tax-regulation change** |
| termination date | **2016-04-06** |
| expense reimbursement | Pfizer → Allergan **$150m** |
| 최종 판정 | **명확한 실패 — policy regime change가 merger agreement의 tax-law termination right를 작동** |

> **결론:** 이 record는 단순 Allergan Short가 아니라 여러 merger-arb를 묶은 basket 안의 Pfizer/Allergan spread leg다. 원문은 antitrust 등 deal-specific risk를 감수할 수 있는 Tier-2 기회로 봤다. 하지만 실제 deal-break 원인은 경쟁법이 아니라 2016년 4월 미국 Treasury의 tax-inversion 규정 변경이었다. merger agreement상 Adverse Tax Law Change가 발생하면서 양사는 4월 6일 거래를 종료했고 Pfizer는 Allergan에 $150m 비용을 상환했다. **정책 regime change를 충분히 반영하지 못한 arb 실패**다.

---

## 1. Security / Strategy Identity

이 아이디어를 “AGN short”로 읽으면 안 된다.

Merger arb의 경제적 포지션은:
- target / deal consideration Long,
- 필요시 acquirer 또는 basket hedge,
- spread convergence 기대

였다.

따라서 raw Short flag는 hedge leg 또는 데이터 ingestion artifact로 보는 것이 합리적이다.

---

## 2. 원문 투자논지

원문은 portfolio approach로:
- Tier 1: very high confidence
- Tier 2: 일부 antitrust/complexity risk가 있지만 attractive spread
- Tier 3: lower confidence

를 구분했다.

Pfizer/Allergan은 size를 늘릴 수 있는 Tier-2 deal로 취급됐다.

---

## 3. Claim Map

### C1. deal risk는 주로 antitrust/ordinary execution — **실패**
actual fatal risk는 U.S. tax-policy change였다.

### C2. signed agreement가 downside를 제한 — **실패**
agreement 자체에 adverse tax-law change termination mechanism이 있었다.

### C3. spread converges to close — **실패**
deal terminated.

### C4. basket diversification이 risk를 줄인다 — **portfolio 수준에서는 가능**
하지만 이 canonical은 AGN/PFE leg 하나만 평가한다.

---

## 4. 실제 경로

| 날짜 | 사건 |
|---|---|
| 2016-02-19 | VIC merger-arb basket post |
| 2016-04-04 | U.S. Treasury announces anti-inversion tax rules |
| 2016-04-06 | Pfizer / Allergan mutually terminate merger |
| 2016-04-08 | Pfizer pays Allergan $150m expense reimbursement |

---

## 5. 왜 이 Risk를 놓쳤는가

Cross-border tax inversion deal의 핵심 변수는:
- antitrust,
- shareholder approval,
- financing

뿐 아니라 **tax-law continuity itself**였다.

정책변화가 transaction economics를 제거하면 signed agreement도 보호막이 되지 않는다.

---

## 6. 재사용 가능한 교훈

1. merger agreement의 tax-law / MAE / regulatory termination clauses를 직접 읽는다.
2. tax inversion deal은 policy-regime probability를 별도 모델링한다.
3. basket arb의 개별 leg 성과와 portfolio 성과를 분리한다.
4. raw Long/Short field로 pair trade의 경제적 방향을 판단하지 않는다.
5. break fee나 expense reimbursement가 target spread 손실을 자동 보전하지 않는다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Deal-risk identification | 실패 |
| Policy-risk underwriting | 강한 실패 |
| Closing thesis | 실패 |
| Strategy classification | raw direction correction 필요 |
| Thesis score | 2.0/10 |
| Process score | 9.8/10 |
| 종합 | **명확한 실패 — Treasury rule change로 deal break** |

### 한 문장 교훈

> tax-driven merger arb에서는 **계약서보다 세법이 먼저 바뀌면 계약 자체가 사라질 수 있다.**

---

## 8. Sources / Validation Notes

1. VIC original: https://www.valueinvestorsclub.com/idea/ALLERGAN_PLC/2853252264
2. Pfizer/Allergan merger termination announcement, 2016-04-06.
3. Treasury anti-inversion rules announced 2016-04-04.
4. Pfizer $150m expense reimbursement to Allergan.

### 데이터 품질
- T0 basket thesis: **A**
- break event: **A**
- exact leg P&L: **not reconstructed**
