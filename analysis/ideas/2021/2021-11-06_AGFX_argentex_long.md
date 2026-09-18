# Argentex Group (AGFX) — 2021-11-06 VIC Long

> **Idea unit:** 2021-11-06 Argentex Group common equity Long.
> **Research as-of:** 2026-09-18. 원 SQL Long과 실제 방향이 일치한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Argentex Group / AGFX LN |
| VIC 게시일 / 작성자 | 2021-11-06 / MickyS |
| 실제 방향 | Common equity Long |
| 당시 가격 | 약 **88p** |
| market cap / free cash | 약 **£100m / £20m** |
| 당시 EV | 약 **£80m** |
| historical revenue / op profit | 약 **£30m / £10m** |
| headline valuation | 2022E 약 **7x EV/EBITDA**, ~10% FCF yield |
| 핵심 논지 | capital-light FX brokerage + high margins + insider ownership + platform option |
| 원문 주요 risk | client default 시 collateral / margin-call liquidity |
| 2025 liquidity crisis | rapid FX volatility로 **£20m+ margin calls** |
| rescue takeout | **2.49p/share**, equity value ~£3m |
| 최종 판정 | **매우 강한 실패 — 88p→2.49p, liquidity risk가 business model을 압도** |

> **결론:** 원문은 Argentex를 높은 margin, 낮은 capex, 순현금의 capital-light FX broker로 봤고, rising rates와 technology platform을 upside로 뒀다. 그러나 원문 risk section에 이미 적혀 있던 **client collateral / margin-call liquidity risk**가 2025 실제 terminal event가 됐다. 급격한 FX volatility와 USD 약세로 £20m를 넘는 margin calls가 발생했고 trading이 중단됐다. IFX가 bridge funding을 제공한 뒤 최종 2.49p cash offer를 제시했다. 88p 대비 약 **-97.2%**다.

---

## 1. 사업 구조

Argentex는 corporate clients를 대상으로:
- spot FX,
- forwards,
- options,
- treasury/hedging

을 제공했다.

표면적으로는:
- inventory 없음,
- capex 낮음,
- high gross margin,
- recurring client flow

라 capital-light로 보인다.

하지만 derivatives/forward business는 **market moves와 counterparty settlement timing 때문에 큰 intraday/short-term liquidity requirement**가 생길 수 있다.

---

## 2. 원문 투자논지

원문:
- price 88p,
- ~£20m free cash,
- EV ~£80m,
- revenue <£1m in 2013 → ~£29m in 2020,
- operating profit ~£12.4m,
- insider ownership >30%,
- rising rates tailwind,
- tech platform optionality.

그리고 중요한 risk:
> client가 계약을 이행하지 못하면 collateral/margin calls가 회사 현금을 크게 묶을 수 있다.

이 위험이 실제로 thesis를 파괴했다.

---

## 3. Claim Map

### C1. capital-light high-margin broker — **평상시 성공 / stress에서 실패**
normal environment에서는 맞지만 liquidity tail risk를 business model 밖으로 볼 수 없었다.

### C2. cash balance가 downside를 지지 — **강한 실패**
stress margin calls가 free cash를 빠르게 소진했다.

### C3. rising rates가 earnings를 돕는다 — **부차적**
2025 FX volatility/liquidity shock가 금리 수혜를 압도했다.

### C4. technology platform growth — **미실현**
terminal liquidity event가 먼저 도착했다.

### C5. management alignment — **보호 못함**
insider ownership도 tail-risk controls 실패를 막지 못했다.

---

## 4. 실제 경로

| 시점 | 사건 |
|---|---|
| 2021-11 | VIC Long @ ~88p |
| 2022~24 | growth / market volatility |
| 2025-04 | rapid FX moves → £20m+ margin calls |
| 2025-04-22 | shares suspended |
| 2025 | IFX emergency funding / bridge loans |
| 2025 | recommended cash offer **2.49p/share** |

---

## 5. Payoff

**2.49 / 88 - 1 ≈ -97.2%**

정확한 dividend-adjusted return은 별도 계산하지 않지만 terminal capital loss가 지배한다.

---

## 6. 분석 오류

가장 큰 오류는 “capital-light”라는 용어였다.

FX broker는 fixed assets가 적어도:
- settlement liquidity,
- collateral posting,
- counterparty default,
- stress VaR

때문에 **liquidity-capital intensive**일 수 있다.

---

## 7. 재사용 가능한 교훈

1. low-capex와 low-capital-risk를 혼동하지 않는다.
2. derivatives broker는 P&L보다 collateral liquidity stress test가 먼저다.
3. free cash를 모두 excess cash로 보지 않는다.
4. counterparty default와 margin call을 scenario-based liquidity requirement로 모델링한다.
5. risk section에 적힌 tail risk가 실제로 발생했을 때 즉시 thesis를 재평가한다.

---

## 8. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Normalized business thesis | 일부 타당 |
| Liquidity-risk underwriting | 강한 실패 |
| Downside protection | 실패 |
| Terminal outcome | -97% 수준 |
| Thesis score | 1.0/10 |
| Process score | 9.9/10 |
| 종합 | **매우 강한 실패 — capital-light로 보인 broker가 liquidity shock에서 붕괴** |

### 한 문장 교훈

> derivatives broker에서 **capex가 적다는 사실은 stress liquidity가 적다는 뜻이 아니다.**

---

## 9. Sources / Validation Notes

1. VIC original / uploaded SQL, 2021-11-06.
2. UK NSM/FCA-hosted recommended IFX acquisition — 2.49p/share, ~£3m equity value: https://data.fca.org.uk/artefacts/NSM/RNS/5630285.html
3. 2025 company announcements on liquidity and bridge financing.
4. Reuters reporting on £20m+ margin calls and collapse in share price.

### 데이터 품질
- T0 thesis: **A**
- terminal transaction: **A**
- liquidity event size: **A/B**
