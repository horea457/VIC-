# Atlas Engineered Products Ltd. (AEP.V) — 2020-01-28 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Atlas Engineered Products Ltd. / AEP.V |
| VIC 게시일 / 작성자 | 2020-01-28 / hack731 |
| 분석 증권 / 실제 방향 | TSX-V:AEP common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 C$0.39 |
| 기대기간 | 2022 operating target |
| raw horizon audit | 2022 C$100m sales·15% EBITDA·C$1.00 target |
| 최종 판정 | **지연 성공 — C$1 target는 달성, 2022 C$100m revenue는 38% 미달** |

> **결론:** 지역 운송·설계 moat와 succession-driven roll-up은 살아남았고 주가는 2023~24 C$1을 넘어 2024 약 C$1.57까지 관찰됐다. 그러나 2022 revenue C$61.90m은 C$100m 목표보다 C$38.10m/-38.1% 미달했다. 좋은 unit economics와 M&A runway를 맞혔지만 acquisition cadence를 확정변수로 둔 timing error다.

---

## 1. 회사는 정확히 무엇을 하는가

Atlas Engineered Products는 캐나다의 지역 truss·wall panel·engineered wood 제조사를 인수·통합한다. 제품이 부피가 크고 설계·permit·납기가 지역별이라 장거리 운송이 비경제적이다. 매출은 lumber 가격 pass-through의 영향을 받으므로 revenue growth보다 volume, gross margin, acquisition multiple, debt와 주당 EBITDA가 중요하다.

`regional volume × selling price - lumber/labour - plant overhead - integration cost - interest - capex = equity FCF`; M&A는 dilution까지 주당으로 계산한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

organic volume, lumber pass-through, gross margin, normalized EBITDA, acquisition multiple, integration cost, net debt, fully diluted shares, housing starts

---

## 2. 당시 상황과 시장이 가격에 넣은 것

원문은 2019 run-rate sales C$33~35m에서 지역 truss 회사를 2~3개 인수하고 organic growth를 더해 2022 C$100m sales, 30% gross margin, 15% EBITDA margin을 제시했다. 6.5x EV/EBITDA로 C$1.00/share, 당시 C$0.39 대비 약 2.6배를 기대했다.

### Reverse expectations

시장은 작은 issuer의 key-person·financing·integration risk와 Canadian housing cycle, lumber pass-through 때문에 3년 내 규모 3배를 할인했다. M&A pipeline은 계약된 revenue가 아니었다.

---

## 3. 원문 투자논지 지도

### C1. 지역 운송·permit moat — 성공

**원문 주장**

truss는 bulky하고 설계·permit이 지역별이라 local density가 방어력이다.

**경제적 메커니즘**

짧은 운송반경과 고객관계가 가격·납기를 지킨다.

**T0 근거**

Nanaimo model plant와 지역 operators.

**숨은 가정**

지역 수요·경쟁이 gross margin을 지지한다.

**사전 반증조건**

organic gross margin이 peer 수준 아래로 떨어지면 반증.

**실제 결과**

여러 지역 company가 존속하고 group gross margin은 2022 32%를 기록했다.

**정량 gap**

2024 gross margin 24%로 cycle sensitivity 확인.

**분석 오류 또는 제한**

구조적 moat와 cycle margin을 혼용했다.

**재사용 교훈**

moat는 multi-cycle gross margin과 share로 검증한다.

### C2. fragmented succession M&A runway — 성공 방향

**원문 주장**

고령 owner가 많은 산업에서 싸게 회사를 연속 인수한다.

**경제적 메커니즘**

seller succession과 shared systems가 acquisition supply·synergy를 만든다.

**T0 근거**

수백개 target과 C$3~15m revenue 범위.

**숨은 가정**

valuation·financing·integration capacity가 유지된다.

**사전 반증조건**

signed deals와 per-share EBITDA가 늘지 않으면 반증.

**실제 결과**

2022 Hi-Tec, 2023 LCF 등 인수가 이어졌다.

**정량 gap**

2022까지 C$100m scale에는 못 미침.

**분석 오류 또는 제한**

opportunity set을 executable cadence로 봤다.

**재사용 교훈**

pipeline을 LOI·financed·closed·integrated로 나눈다.

### C3. 2022 revenue C$100m — 실패

**원문 주장**

run-rate C$33~35m을 3년 내 약 3배로 키운다.

**경제적 메커니즘**

2~3개 인수와 organic growth가 합쳐진다.

**T0 근거**

원문 2022 model.

**숨은 가정**

deals가 제때 종결되고 housing demand가 유지된다.

**사전 반증조건**

2022 revenue가 C$80m 아래면 반증.

**실제 결과**

2022 revenue C$61.90m.

**정량 gap**

-C$38.10m/-38.1%.

**분석 오류 또는 제한**

M&A timing과 organic growth를 단일 point forecast로 묶었다.

**재사용 교훈**

roll-up base case에는 확정 deal만 넣는다.

### C4. 15% EBITDA margin — 부분 성공

**원문 주장**

scale·procurement·IT로 15% EBITDA margin을 달성한다.

**경제적 메커니즘**

local gross margin에 shared overhead leverage가 붙는다.

**T0 근거**

원문 30% gross/15% EBITDA.

**숨은 가정**

lumber·labour·integration cost가 통제된다.

**사전 반증조건**

normalized EBITDA margin이 반복 12% 이하이면 반증.

**실제 결과**

2022 adjusted margin 25%였으나 2023 20%, 2024 15%로 내려왔다.

**정량 gap**

peak를 넘었지만 지속성은 혼합.

**분석 오류 또는 제한**

한 해 peak margin을 mature margin으로 읽을 위험.

**재사용 교훈**

3년 평균 normalized margin을 쓴다.

### C5. C$1 target @ 6.5x — 지연 성공

**원문 주장**

2022 C$15m EBITDA를 6.5배 평가해 C$1을 만든다.

**경제적 메커니즘**

earnings scale-up과 multiple이 주당가치를 높인다.

**T0 근거**

C$0.39 entry·C$1 target.

**숨은 가정**

share dilution·net debt가 제한되고 2022 실행된다.

**사전 반증조건**

2022까지 C$1 미도달 또는 FDSO 급증이면 timing 실패.

**실제 결과**

C$1은 2023~24에 지연 통과했다.

**정량 gap**

약 1~2년 지연.

**분석 오류 또는 제한**

target price와 target date를 분리하지 않았다.

**재사용 교훈**

IRR에는 달성날짜가 필수다.

### C6. leverage·dilution manageable — 부분 성공

**원문 주장**

cash flow와 financing이 roll-up을 무리 없이 지탱한다.

**경제적 메커니즘**

적정 debt/equity mix가 distress 없이 규모를 키운다.

**T0 근거**

T0 작은 balance sheet와 acquisition model.

**숨은 가정**

downcycle에도 covenant와 per-share value가 유지된다.

**사전 반증조건**

net debt spike 또는 저가 증자면 반증.

**실제 결과**

distress는 없었지만 2024 C$14.56m equity raise와 share count 증가가 있었다.

**정량 gap**

survival 성공·per-share dilution 존재.

**분석 오류 또는 제한**

enterprise growth를 per-share growth로 자동 전환했다.

**재사용 교훈**

모든 deal을 fully diluted per-share로 재계산한다.

---

## 4. 당시 Valuation과 Payoff Structure

2022E C$15m EBITDA × 6.5배에서 net debt·dilution을 차감해 C$1을 산출했다. 실제 2022 adjusted EBITDA C$15.73m은 근접했지만 revenue mix·cycle peak와 이후 margin reset이 multiple durability를 약화했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | M&A 중단·housing slowdown | C$0.3~0.5 | 2023 earnings reset |
| Base | C$100m·15% margin | C$1.00 | price만 지연 달성 |
| Bull | 빠른 national roll-up | C$1+ 조기 | cadence 미달 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2022 revenue | C$100m target | C$100m | C$61.90m | -38.1% |
| 2022 adjusted EBITDA | C$15m | 15% margin | C$15.73m/25% | 수치 성공·mix 다름 |
| 2023 revenue | 성장 지속 | C$100m path | C$49.41m | cycle reset |
| 2024 normalized EBITDA | mature 15%+ | 확대 | C$8.52m/15% | 부분 |
| Price target | C$0.39→C$1 | 2022 | 2023~24 통과 | 지연 성공 |

### 촉매와 시간

판정 horizon은 **2022 operating target**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2020-01-28 | VIC Long 게시 | C$100m/C$1 thesis |
| 2021-12-31 | revenue C$55.00m | scale-up |
| 2022-02-28 | Hi-Tec 인수 | C$5.8m shares+C$3.25m real estate |
| 2022-12-31 | revenue C$61.90m | C$100m target 실패 |
| 2023-08-23 | LCF 인수 | 동부 확장·debt/equity financing |
| 2023-12-31 | revenue C$49.41m | 금리·lumber reset |
| 2024 | 주가 C$1.50대 관찰 | target 지연 달성 |
| 2024-06-26 | C$14.56m equity raise | automation·M&A·dilution |
| 2024-12-31 | normalized EBITDA C$8.52m | mature denominator 재평가 |

### 실제 사업·자본구조 추이

2022 revenue C$61.90m, operating income C$12.53m, adjusted EBITDA C$15.73m이었다. 2023 금리·lumber normalization으로 revenue C$49.41m, normalized EBITDA C$9.93m으로 후퇴했다. LCF 인수 뒤 2024 revenue C$55.83m, normalized EBITDA C$8.52m이었다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

공식 daily total-return ledger는 만들지 않았다. 독립 월간 cross-check에서 2023~24 C$1을 통과하고 2024 약 C$1.57을 관찰했다. target hit은 확인하되 정확한 IRR·배당조정 수익률은 주장하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 지역 운송·permit moat | 20% | 성공 | 2024 gross margin 24%로 cycle sensitivity 확인. |
| C2 | fragmented succession M&A runway | 18% | 성공 방향 | 2022까지 C$100m scale에는 못 미침. |
| C3 | 2022 revenue C$100m | 18% | 실패 | -C$38.10m/-38.1%. |
| C4 | 15% EBITDA margin | 16% | 부분 성공 | peak를 넘었지만 지속성은 혼합. |
| C5 | C$1 target @ 6.5x | 16% | 지연 성공 | 약 1~2년 지연. |
| C6 | leverage·dilution manageable | 12% | 부분 성공 | survival 성공·per-share dilution 존재. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

장기 수익은 지역 franchise, 낮은 entry valuation과 추가 인수 optionality가 만들었다. 미달은 acquisition availability·financing·integration·housing cycle가 3년 안에 동시에 맞지 않은 데서 나왔다.

### Counterfactual

인수를 한 건도 못 하고 housing starts가 20% 감소해도 기존 공장 FCF만으로 C$0.39의 downside와 debt service가 가능한가?

---

## 9. 분석 오류 유형과 최초 경고

M&A pipeline과 record plant margin을 2022 forecast에 높은 확률로 넣고, acquisition financing·dilution과 cycle stress를 충분히 확률가중하지 않았다.

### 최초로 관찰 가능했던 경고신호

2022 revenue가 C$61.90m으로 C$100m target에 38.1% 미달한 시점에 operating target가 깨졌고, 2023 margin reset이 normalization 문제를 확인했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

roll-up pipeline은 signed deal과 funded capacity만 forecast에 넣는다.

### Lesson 2

regional moat와 national synergy를 별도 claim으로 검증한다.

### Lesson 3

목표가격 달성과 operating forecast 달성을 분리한다.

### 지금 같은 아이디어를 다시 본다면

- organic volume vs price
- deal pipeline stage
- purchase multiple
- post-deal margin
- net debt
- share dilution
- housing starts
- 주당 normalized EBITDA

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Industry thesis | 성공 |
| Valuation thesis | 지연 성공 |
| Catalyst thesis | M&A cadence 미달 |
| Timing / path | 크게 지연 |
| Security selection | common 적절 |
| Thesis score | 7.6/10 |
| Process score | 9.5/10 |
| 종합 | **지연 성공 — C$1 target는 달성, 2022 C$100m revenue는 38% 미달** |

### 한 문장 교훈

> roll-up pipeline은 signed deal과 funded capacity만 forecast에 넣는다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/ATLAS_ENGINEERED_PRODCTS_LTD/9941570662) — Value Investors Club / source SQL, 2020-01-28. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [Atlas corporate and operating-company overview](https://www.atlasengineeredproducts.com/) — Atlas Engineered Products, 2026. 10개 인수, 지역별 회사, 제품·succession roll-up 논리 검증.
3. [Atlas FY2019 MD&A](https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2019-MDA-FINAL.pdf) — Atlas Engineered Products, 2020-04-30. 2020 아이디어의 당시 규모·M&A·margin 출발점 검증.
4. [Atlas FY2021 MD&A](https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2021-MDA-final.pdf) — Atlas Engineered Products, 2022-04. 2021 record year와 2022 진입 전 run-rate 검증.
5. [Atlas FY2022 MD&A](https://www.atlasengineeredproducts.com/dist/assets/images/hero/AEP-F2022-MDA-Final.pdf) — Atlas Engineered Products, 2023-04. 매출 C$61.90m, operating income C$12.53m, adjusted EBITDA C$15.73m, Hi-Tec 조건 검증.
6. [Atlas FY2022 financial statements](https://www.atlasengineeredproducts.com/dist/assets/images/hero/Atlas-Engineered-Products-Ltd-Dec-2022-FS.pdf) — Atlas Engineered Products, 2023-04. 감사 재무제표·부채·share count 검증.
7. [Atlas FY2023 MD&A](https://www.atlasengineeredproducts.com/dist/assets/images/hero/AEP-F2023-MDA-final.pdf) — Atlas Engineered Products, 2024-04. 매출 C$49.41m, margin 27%, LCF acquisition과 금리민감도 검증.
8. [Atlas FY2024 MD&A](https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2024-MDA-final.pdf) — Atlas Engineered Products, 2025-04. 매출 C$55.83m, normalized EBITDA C$8.52m, share issue·robotics 검증.
9. [Atlas FY2025 MD&A](https://www.atlasengineeredproducts.com/dist/assets/images/misc/AEP-F2025-MDA-final-Compressed.pdf) — Atlas Engineered Products, 2026-04. 2025 매출·normalized EBITDA와 최신 cycle outcome 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — exact total-return ledger가 없어 target hit와 corporate-action value만 제한적으로 판정했다.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
