# Argentex Group Plc (AGFX) — 2021-11-06 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-19. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Argentex Group Plc / AGFX |
| VIC 게시일 / 작성자 | 2021-11-06 / MickyS |
| 분석 증권 / 실제 방향 | AIM:AGFX common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 88p; market cap ~£100m |
| 기대기간 | 3~5년 client growth·margin·platform rerating |
| raw horizon audit | ~£20m free cash, ~7x 2022E EV/EBITDA, ~10% FCF yield, rising-rate·technology optionality |
| 최종 판정 | **매우 강한 실패 — liquidity tail이 -97% terminal loss** |

> **결론:** 88p에서 high-margin·low-capex FX broker를 샀지만 원문 risk section의 client default/collateral risk가 2025 terminal event가 됐다. 급격한 FX 움직임과 margin calls가 liquidity를 훼손해 trading이 정지됐고 IFX가 2.49p cash offer를 제시했다. 단순 price loss는 약 97.2%다.

---

## 1. 회사는 정확히 무엇을 하는가

Argentex는 기업·기관 고객에게 spot FX, forwards, options와 international payments를 제공했다. fixed asset과 capex는 적지만 client collateral 부족, prime broker·bank margin calls와 settlement timing 때문에 급격한 시장변동 시 큰 단기유동성이 필요하다. 정상시 높은 margin과 stress시 liquidity capital을 함께 모델링해야 한다.

`client flow × spread + interest income - staff/tech/compliance cost - credit loss - liquidity buffer cost = equity cash`; stressed collateral need를 excess cash에서 먼저 차감한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

client count/flow, revenue, operating margin, net cash, client collateral, margin-call liquidity, bank facilities, counterparty concentration, stress VaR, suspended balances

---

## 2. 당시 상황과 시장이 가격에 넣은 것

revenue가 2013 £1m 미만에서 2020 약 £29m으로 성장했고 operating profit 약 £12.4m, insider ownership 30%+, free cash 약 £20m이었다. 88p·market cap £100m에서 EV 약 £80m, 2022E 약 7x EV/EBITDA와 10% FCF yield로 보였다. 금리상승과 technology platform은 upside였다.

### Reverse expectations

FX broker는 inventory와 PP&E가 없어도 derivatives collateral과 settlement liquidity가 필요하다. client가 variation margin을 제때 내지 못하면 Argentex가 banks/prime brokers에 먼저 현금을 내야 한다. reported net cash 전부를 배당 가능한 excess로 보면 stress liquidity를 이중계산에서 빠뜨린다.

---

## 3. 원문 투자논지 지도

### C1. capital-light high-margin model — stress에서 실패

**원문 주장**

낮은 capex와 높은 margins가 compounder economics를 만든다.

**경제적 메커니즘**

client flow spread가 fixed cost를 넘어 FCF로 전환된다.

**T0 근거**

historical revenue·operating profit·low capex.

**숨은 가정**

collateral funding이 구조적으로 작다.

**사전 반증조건**

stress liquidity가 annual FCF를 넘으면 반증.

**실제 결과**

2025 margin calls가 business continuity를 위협했다.

**정량 gap**

평시 margin보다 liquidity가 지배.

**분석 오류 또는 제한**

accounting capital intensity만 봤다.

**재사용 교훈**

operational·liquidity capital을 합산한다.

### C2. £20m cash downside floor — 강한 실패

**원문 주장**

market cap £100m 중 £20m cash가 downside를 지지한다.

**경제적 메커니즘**

net cash를 EV에서 빼면 operating business가 싸다.

**T0 근거**

reported free cash.

**숨은 가정**

cash가 unrestricted excess다.

**사전 반증조건**

stress collateral·working capital need가 cash와 비슷하면 실패.

**실제 결과**

£6.5m secured bridge와 추가 즉시지원이 필요했다.

**정량 gap**

floor가 사라짐.

**분석 오류 또는 제한**

cash의 functional purpose를 분류하지 않았다.

**재사용 교훈**

minimum liquidity와 tail margin을 restricted-like로 본다.

### C3. 7x 2022E EV/EBITDA — 실패

**원문 주장**

normalized earnings 대비 multiple이 낮다.

**경제적 메커니즘**

growth와 durable margins가 multiple normalization을 만든다.

**T0 근거**

EV ~£80m와 forecast EBITDA.

**숨은 가정**

EBITDA가 distributable cash에 가깝다.

**사전 반증조건**

cash conversion·liquidity cost 붕괴면 반증.

**실제 결과**

terminal equity value 약 £3m.

**정량 gap**

multiple thesis 소멸.

**분석 오류 또는 제한**

tail capital cost를 EBITDA에 반영하지 않았다.

**재사용 교훈**

stress-adjusted FCF로 value한다.

### C4. rising rates tailwind — 부차적

**원문 주장**

client balances의 interest income이 증가한다.

**경제적 메커니즘**

higher rates가 float yield를 높인다.

**T0 근거**

rate sensitivity와 cash balances.

**숨은 가정**

FX volatility·hedging losses가 통제된다.

**사전 반증조건**

liquidity shock이 interest benefit을 압도하면 반증.

**실제 결과**

2025 FX move와 margin calls가 모든 rate benefit을 압도했다.

**정량 gap**

driver ranking 오류.

**분석 오류 또는 제한**

positive carry가 tail liquidity loss를 상쇄한다고 암묵적으로 가정했다.

**재사용 교훈**

작은 recurring tailwind보다 low-frequency ruin risk를 우선한다.

### C5. technology/platform optionality — 미실현

**원문 주장**

platform 투자로 client acquisition과 operating leverage가 커진다.

**경제적 메커니즘**

automation이 sales capacity와 margin을 높인다.

**T0 근거**

growth plans와 international footprint.

**숨은 가정**

funding runway가 충분하다.

**사전 반증조건**

core liquidity event가 platform payoff 전 도착하면 실패.

**실제 결과**

terminal rescue가 platform optionality보다 먼저 발생했다.

**정량 gap**

option value 사실상 0.

**분석 오류 또는 제한**

funded-to-inflection을 검증하지 않았다.

**재사용 교훈**

optionality에는 cost·date·survival probability를 붙인다.

### C6. insider ownership alignment — 보호 실패

**원문 주장**

30%+ insiders가 prudent risk management를 유도한다.

**경제적 메커니즘**

owner-operators가 dilution·tail risk를 피한다.

**T0 근거**

high insider holdings.

**숨은 가정**

risk limits와 liquidity governance가 강하다.

**사전 반증조건**

emergency financing·near-zero sale이면 반증.

**실제 결과**

board가 insolvency 대안으로 2.49p offer를 권고했다.

**정량 gap**

alignment가 downside 못 막음.

**분석 오류 또는 제한**

ownership을 competence·controls로 대체했다.

**재사용 교훈**

risk governance와 exposure limits를 직접 확인한다.

---

## 4. 당시 Valuation과 Payoff Structure

normalized EBITDA/FCF multiple에 앞서 stressed liquidity reserve를 enterprise value에서 차감해야 한다. `free cash - peak variation margin - counterparty default loss - regulatory buffer`가 진짜 excess cash다. terminal offer 2.49p는 평시 earnings multiple이 아니라 insolvency alternative 아래 rescue value였다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | client default·£20m+ margin calls | near-zero/rescue | 2.49p·약 £3m |
| Base | client growth·stable volatility | 7x EBITDA rerating | terminal 전에 붕괴 |
| Bull | rates+platform | double-digit compounding | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry/offer | 88p | 상승 | 2.49p | -97.2% |
| Free cash | ~£20m | downside floor | stress collateral에 소진 | 강한 실패 |
| Bridge | 불필요 가정 | self-funded | £6.5m secured | 반증 |
| Equity value | ~£100m | compound | ~£3m offer | 강한 실패 |
| Liquidity event | tail risk | 관리 가능 | suspension·urgent funding | 강한 실패 |

### 촉매와 시간

판정 horizon은 **3~5년 client growth·margin·platform rerating**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2021-11-06 | VIC Long | 88p compounder thesis |
| 2022 | international/platform expansion | growth investment |
| 2024 | financial year ends | cash·risk baseline |
| 2025-04-02 | FY24 results | roadshow 뒤 volatility |
| 2025-04-22 | liquidity warning·suspension | thesis break |
| 2025-04-23 | further deterioration | immediate finance 필요 |
| 2025-04-24 | IFX £6.5m bridge | secured rescue |
| 2025-04-25 | 2.49p recommended offer | terminal common value |

### 실제 사업·자본구조 추이

2025-04 rapid FX volatility, 특히 USD 약세가 forward·options book의 margin calls를 불렀다. 회사는 4월 22일 suspension을 요청했고 다음 날 liquidity가 더 악화됐다고 밝혔다. IFX는 £6.5m secured bridge와 추가 지원 논의를 제공했고 4월 25일 2.49p/share, 약 £3m equity value의 recommended offer를 발표했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

2.49p / 88p - 1 = 약 -97.2%다. 중간 dividends를 포함하지 않아도 terminal capital loss가 결과를 지배한다. offer가 insolvency 시 very limited or nil return의 대안이었다는 공식 설명은 net cash downside-floor 가정이 왜 틀렸는지 보여준다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | capital-light high-margin model | 20% | stress에서 실패 | 평시 margin보다 liquidity가 지배. |
| C2 | £20m cash downside floor | 18% | 강한 실패 | floor가 사라짐. |
| C3 | 7x 2022E EV/EBITDA | 18% | 실패 | multiple thesis 소멸. |
| C4 | rising rates tailwind | 16% | 부차적 | driver ranking 오류. |
| C5 | technology/platform optionality | 16% | 미실현 | option value 사실상 0. |
| C6 | insider ownership alignment | 12% | 보호 실패 | alignment가 downside 못 막음. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

loss의 원인은 spread margin 악화가 아니라 path-dependent collateral liquidity였다. 고객 collateral 수취와 bank margin 지급의 timing mismatch가 평시 cash를 며칠 만에 필요자본으로 바꿨다. emergency secured financing 뒤 common은 residual rescue value만 받았다.

### Counterfactual

상위 stress week에서 clients가 variation margin의 절반만 제때 내고 banks는 전액을 당일 요구할 때 필요한 cash가 £20m free cash보다 작았는가?

---

## 9. 분석 오류 유형과 최초 경고

low capex를 low capital intensity로, cash balance를 excess cash로 간주했다. 이미 원문에 식별한 risk를 정량 liquidity waterfall·limit·position sizing으로 연결하지 않아 tail risk를 footnote로 남겼다.

### 최초로 관찰 가능했던 경고신호

첫 명확한 공개 break는 2025-04-22 margin-call liquidity pressure와 trading suspension이었다. 하지만 사전에는 gross derivatives exposure·client collateral gap이 net cash에 근접하는 순간이 경고였어야 했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

low-capex broker도 collateral 때문에 liquidity-capital intensive일 수 있다.

### Lesson 2

free cash에서 stressed margin requirement를 먼저 차감한다.

### Lesson 3

risk disclosure를 probability×cash need×time-to-fund로 계량한다.

### Lesson 4

trading suspension과 secured rescue는 common thesis의 즉시 재인수점이다.

### 지금 같은 아이디어를 다시 본다면

- gross/net derivatives
- client collateral timing
- variation-margin stress
- top counterparties
- bank facilities
- liquidity headroom
- regulatory buffer
- suspension/secured-finance triggers

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 평시 일부 타당 |
| Valuation thesis | 강한 실패 |
| Catalyst thesis | 실패 |
| Security payoff | common 취약 |
| Timing / path | 매우 강한 실패 |
| Thesis score | 1.0/10 |
| Process score | 5.8/10 |
| 종합 | **매우 강한 실패 — liquidity tail이 -97% terminal loss** |

### 한 문장 교훈

> low-capex broker도 collateral 때문에 liquidity-capital intensive일 수 있다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2021-11-06. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [IFX recommended acquisition of Argentex](https://data.fca.org.uk/artefacts/NSM/RNS/5630285.html) — UK National Storage Mechanism / IFX·Argentex, 2025-04-25. 2.49p cash offer, 약 £3m equity value, £6.5m bridge, margin-call liquidity deterioration와 suspension 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B/C** — AGCO 2015·Alamos 2014는 source SQL price-only ratios, 그 외는 verified corporate action·official operating actual·제한적 market cross-check만 사용. complete dated ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
