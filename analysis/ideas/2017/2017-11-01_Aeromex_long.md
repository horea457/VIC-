# Grupo Aeroméxico (Aeromex) — 2017-11-01 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Grupo Aeroméxico / Aeromex |
| VIC 게시일 / 작성자 | 2017-11-01 / flubber926 |
| 분석 증권 / 실제 방향 | Aeroméxico legacy common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 MXN32.7 |
| 기대기간 | 2019 |
| raw horizon audit | 2019 fair value MXN71.4, Delta JV synergy ~$200m |
| 최종 판정 | **강한 실패 — Chapter 11 old equity near-wipeout** |

> **결론:** Mexico demand와 Delta partnership는 franchise를 살렸지만 margin·deleveraging은 미달했고 COVID 뒤 Chapter 11에서 old equity는 reorganized equity의 0.01% 미만을 받았다. Delta의 MXN49 과거 매입가는 common floor가 아니었다.

---

## 1. 회사는 정확히 무엇을 하는가

Grupo Aeroméxico는 Mexico City hub를 중심으로 국내선과 미주·유럽·아시아 노선을 운영한 full-service airline이다. Delta와 JV 및 지분관계를 맺었지만 common의 가치는 RASM×capacity에서 fuel·CASK·aircraft rent·interest를 차감한 잔여현금이다. 높은 operating·financial leverage 때문에 수요가 사라지면 brand·slot·partner의 enterprise value가 있어도 old common은 DIP·secured debt·lease claim 뒤에서 소멸할 수 있다.

RASM × ASK - fuel - non-fuel CASK - aircraft rent - interest - tax = common cash flow; stress에서는 liquidity와 claim waterfall을 먼저 계산한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

ASK/RPK, load factor, yield/RASM, CASK ex-fuel, EBITDAR margin, net debt/EBITDAR, fleet commitments, MXN/USD, unrestricted cash, JV contribution

---

## 2. 당시 상황과 시장이 가격에 넣은 것

MXN32.7, 2017E EV/EBITDAR 약 4.6x. Delta가 약 MXN49에 strategic stake를 취득했고, low penetration·slot hub·fleet simplification·2021까지 $200m JV synergy로 margin doubling과 MXN71.4를 기대했다.

### Reverse expectations

시장은 fuel·FX·labor·airport constraints와 leverage를 할인했다. 원문은 strategic sponsor price와 enterprise franchise value가 common downside를 보호한다고 보았다.

---

## 3. 원문 투자논지 지도

### C1. Mexico aviation growth — 장기 방향만 성공

**원문 주장**

낮은 penetration이 traffic 성장.

**경제적 메커니즘**

소득·노선 확대.

**T0 근거**

시장 구조.

**숨은 가정**

yield·capacity discipline.

**사전 반증조건**

traffic가 margin으로 안 이어지면 제한.

**실제 결과**

franchise는 생존.

**정량 gap**

equity 구제 못함.

**분석 오류 또는 제한**

TAM을 profit으로 직결.

**재사용 교훈**

RASM-CASK conversion.

### C2. Delta JV synergy ~$200m — 실패·불충분

**원문 주장**

revenue $160m+cost $40m synergy.

**경제적 메커니즘**

network·sales·cost.

**T0 근거**

JV plan.

**숨은 가정**

규제·execution.

**사전 반증조건**

2019 margin/net income 미달이면 반증.

**실제 결과**

2019 net loss.

**정량 gap**

synergy가 equity 부족.

**분석 오류 또는 제한**

gross synergy 강조.

**재사용 교훈**

standalone counterfactual 필요.

### C3. margin doubling — 실패

**원문 주장**

CASK 개선과 mix로 margin 확대.

**경제적 메커니즘**

operating leverage.

**T0 근거**

fleet simplification.

**숨은 가정**

fuel·FX 안정.

**사전 반증조건**

2019 margin/earnings 미달.

**실제 결과**

net loss 지속.

**정량 gap**

target 미달.

**분석 오류 또는 제한**

EBITDAR와 net income 혼동.

**재사용 교훈**

lease·interest까지 bridge.

### C4. Delta MXN49 floor — 강한 실패

**원문 주장**

strategic purchase price가 downside anchor.

**경제적 메커니즘**

partner incentive.

**T0 근거**

49% stake.

**숨은 가정**

partner가 old equity 보호.

**사전 반증조건**

restructuring dilution이면 반증.

**실제 결과**

old equity <0.01%.

**정량 gap**

floor 소멸.

**분석 오류 또는 제한**

enterprise와 security 혼동.

**재사용 교훈**

waterfall을 먼저 본다.

### C5. deleveraging·MXN71.4 — 실패

**원문 주장**

growth가 debt burden을 낮춰 fair value 실현.

**경제적 메커니즘**

EBITDAR growth.

**T0 근거**

4.6x entry.

**숨은 가정**

shock 없음.

**사전 반증조건**

leverage 상승·target 미달이면 반증.

**실제 결과**

Chapter 11.

**정량 gap**

terminal near-zero.

**분석 오류 또는 제한**

path risk 과소평가.

**재사용 교훈**

liquidity calendar.

### C6. brand/slots protect common — 실패

**원문 주장**

quality assets가 downside 방어.

**경제적 메커니즘**

franchise sale/reorg value.

**T0 근거**

hub·partner.

**숨은 가정**

claims보다 잔여가치 큼.

**사전 반증조건**

company survives but old equity wiped면 반증.

**실제 결과**

정확히 발생.

**정량 gap**

business 생존/common 실패.

**분석 오류 또는 제한**

security selection 오류.

**재사용 교훈**

enterprise survival과 common recovery 분리.

---

## 4. 당시 Valuation과 Payoff Structure

traffic·margin expansion·deleveraging을 통해 lower exit EV/EBITDAR에도 equity가 두 배 이상 되는 구조였다. levered common이라 EBITDA miss가 residual에 비선형으로 작용했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | margin 미달·FX/fuel | equity 압박 | 2019 이미 진행 |
| Base | JV+deleveraging | MXN71.4 | 미실현 |
| Tail | zero demand/Chapter 11 | old equity 소멸 | 현실화 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry price | MXN32.7 | MXN71.4 | old equity near-zero | 강한 실패 |
| Delta anchor | ~MXN49 | floor | floor 아님 | 강한 실패 |
| 2017E EV/EBITDAR | ~4.6x | rerating | earnings 붕괴 | 실패 |
| 2020 revenue | 성장 | 증가 | -58.5% | 강한 실패 |
| Old equity | 보존 | 큰 upside | <0.01% new equity | near-wipeout |

### 촉매와 시간

판정 horizon은 **2019**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2017-11-01 | VIC Long | Delta/JV thesis |
| 2018 | JV 운영 | strategic value 유지 |
| 2019 | net loss MXN2.4bn | margin 반증 |
| 2020-06-30 | Chapter 11 filing | waterfall 현실화 |
| 2020 | revenue -58.5% | zero-demand shock |
| 2020 | EBITDAR -MXN6.8bn | fixed-cost 폭발 |
| 2022-03-17 | Chapter 11 emergence | franchise 생존 |
| 2022 | old equity <0.01% | legacy common 실패 |

### 실제 사업·자본구조 추이

2019 revenue MXN68.8bn·EBITDAR MXN14.9bn에도 net loss MXN2.4bn. 2020 revenue MXN28.5bn(-58.5%), EBITDAR -MXN6.8bn, Chapter 11. 2022 emergence에서 old equity <0.01%.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

SQL performance row가 없어 exact interim return을 만들지 않는다. reorganization treatment가 terminal payoff를 사실상 0으로 고정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | Mexico aviation growth | 20% | 장기 방향만 성공 | equity 구제 못함. |
| C2 | Delta JV synergy ~$200m | 18% | 실패·불충분 | synergy가 equity 부족. |
| C3 | margin doubling | 18% | 실패 | target 미달. |
| C4 | Delta MXN49 floor | 16% | 강한 실패 | floor 소멸. |
| C5 | deleveraging·MXN71.4 | 16% | 실패 | terminal near-zero. |
| C6 | brand/slots protect common | 12% | 실패 | business 생존/common 실패. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

zero-demand shock가 operating leverage와 lease/debt claims를 폭발시켰고 enterprise value는 DIP·creditors·new money에 귀속됐다.

### Counterfactual

12개월 zero-revenue stress에서 unrestricted cash와 DIP 없이 old common에 잔여가치가 남는가?

---

## 9. 분석 오류 유형과 최초 경고

strategic partner의 past purchase price와 network value를 legacy common의 floor로 오해했다.

### 최초로 관찰 가능했던 경고신호

2019에도 consolidated net loss가 지속된 것이 COVID 이전 첫 경고였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

좋은 network와 strategic partner는 회사를 살려도 기존 common을 살린다는 뜻은 아니다.

### Lesson 2

airline은 EV/EBITDAR보다 liquidity와 fixed-claim waterfall을 먼저 본다.

### Lesson 3

과거 strategic 매입가는 bankruptcy recovery floor가 아니다.

### Lesson 4

JV synergy는 실제 margin·parent cash로 검증한다.

### Lesson 5

zero-revenue stress와 FX·lease claim을 반드시 넣는다.

### 지금 같은 아이디어를 다시 본다면

- unrestricted cash runway
- lease-adjusted leverage
- zero-revenue stress
- DIP waterfall
- partner incentives

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | franchise 생존 |
| Valuation thesis | 실패 |
| Catalyst thesis | JV 불충분 |
| Security payoff | near-wipeout |
| Timing / path | 2019부터 실패 |
| Thesis score | 1.8/10 |
| Process score | 3.2/10 |
| 종합 | **강한 실패 — Chapter 11 old equity near-wipeout** |

### 한 문장 교훈

> 좋은 network와 strategic partner는 회사를 살려도 기존 common을 살린다는 뜻은 아니다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2017-11-01. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [Aeroméxico FY2020 results](https://ir.aeromexico.com/static-files/ddb2e746-8f9f-4f60-b526-77fdd381515c) — Grupo Aeroméxico, 2021-02. 2019 비교치, 2020 revenue -58.5%, EBITDAR -MXN6.8bn, Chapter 11 검증.
3. [Delta Q1 2022 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27904/000002790422000006/dal-20220331.htm) — SEC / Delta Air Lines, 2022-04. Aeroméxico reorganization과 Delta post-emergence interest 검증.
4. [Delta 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/27904/000002790423000010/dal-20221231.htm) — SEC / Delta Air Lines, 2023-02. 재편 후 strategic relationship·ownership context 검증.
5. [Aeroméxico restructuring emergence](https://aeromexico.com/en-us/information-about-aeromexico/restructuring) — Grupo Aeroméxico, 2022-03. Chapter 11 emergence와 재편 절차 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **미사용** — reliable interim price ledger가 없어 terminal corporate-action payoff만 사용.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
