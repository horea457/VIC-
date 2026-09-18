# Atlas Engineered Products Ltd. (AEP.V) — 2022-05-30 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Atlas Engineered Products Ltd. / AEP.V |
| VIC 게시일 / 작성자 | 2022-05-30 / Stelio |
| 분석 증권 / 실제 방향 | TSX-V:AEP common equity / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 C$0.53 |
| 기대기간 | 12~24개월 |
| raw horizon audit | 2022E EBIT C$17m·C$1.50 target @ 6x EV/EBIT |
| 최종 판정 | **지연 성공 — C$1.50 price hit, C$17m EBIT annualization은 실패** |

> **결론:** C$0.53에서 2.4x EV/EBITDA·3.1x EV/EBIT은 싸고 balance sheet·M&A optionality도 유효했다. 그러나 1Q22를 연환산한 C$17m EBIT 대비 실제 2022 operating income은 C$12.53m(-26.3%)였고 2023 C$5.26m으로 급감했다. 주가는 2024 C$1.50대를 기록해 target는 지연 달성했지만 denominator thesis는 틀렸다.

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

원문은 1Q22 revenue C$12.43m·EBIT 약 C$2.3m, LTM normalized EBITDA 약 C$15m·EBIT 약 C$12m, net debt 약 C$3m을 바탕으로 매우 낮은 multiple을 제시했다. Hi-Tec과 recession M&A optionality, 2022E EBIT C$17m·net debt 0·FDSO 67m에 6x를 적용해 C$1.50을 계산했다.

### Reverse expectations

시장은 record quarter의 lumber pricing·housing demand가 정상화되고, 작은 roll-up의 overhead·share dilution·integration이 낮은 headline multiple을 상쇄할 가능성을 반영했다.

---

## 3. 원문 투자논지 지도

### C1. 2022 banner year — 성공

**원문 주장**

Hi-Tec·pricing·backlog로 2022가 record year다.

**경제적 메커니즘**

volume·price·M&A가 매출·이익을 높인다.

**T0 근거**

1Q22 revenue C$12.43m·EBIT 약 C$2.3m.

**숨은 가정**

분기 strength가 연간 지속된다.

**사전 반증조건**

후속분기 매출·margin 급락이면 반증.

**실제 결과**

2022 revenue C$61.90m·operating income C$12.53m으로 record.

**정량 gap**

방향 성공.

**분석 오류 또는 제한**

record year와 normalized year를 혼용했다.

**재사용 교훈**

peak 여부는 다음 cycle trough와 평균으로 판정한다.

### C2. 2022 EBIT C$17m — 실패

**원문 주장**

1Q run-rate와 backlog로 EBIT C$17m을 번다.

**경제적 메커니즘**

record quarter를 연환산한다.

**T0 근거**

원문 model.

**숨은 가정**

seasonality·lumber·housing이 유지된다.

**사전 반증조건**

FY EBIT가 C$14m 아래면 반증.

**실제 결과**

FY operating income C$12.53m.

**정량 gap**

-C$4.47m/-26.3%.

**분석 오류 또는 제한**

한 분기 annualization.

**재사용 교훈**

quarter ×4 대신 trailing·mid-cycle margin을 쓴다.

### C3. 3x EBIT valuation — 부분 성공

**원문 주장**

LTM EBIT C$12m에 3.1x EV/EBIT은 과도하게 싸다.

**경제적 메커니즘**

unchanged EBIT에 normal 6x가 적용된다.

**T0 근거**

C$0.53·net debt C$3m.

**숨은 가정**

EBIT denominator가 지속된다.

**사전 반증조건**

다음해 EBIT 반감이면 low multiple 착시.

**실제 결과**

2023 operating income C$5.26m으로 감소했지만 주가는 rerate했다.

**정량 gap**

2023 기준 multiple은 약 2배 이상 상승.

**분석 오류 또는 제한**

denominator risk를 haircut하지 않았다.

**재사용 교훈**

trough·base·peak EBIT 각각에 multiple을 붙인다.

### C4. balance sheet가 recession을 방어 — 성공 방향

**원문 주장**

낮은 net debt와 현금창출이 downturn survival·M&A를 가능하게 한다.

**경제적 메커니즘**

covenant headroom과 funding access가 duration을 준다.

**T0 근거**

T0 net debt 약 C$3m.

**숨은 가정**

인수 후 leverage와 working capital이 통제된다.

**사전 반증조건**

distress financing·covenant breach면 반증.

**실제 결과**

distress 없이 LCF를 인수하고 equity raise로 자동화 투자.

**정량 gap**

survival 성공·희석 비용 존재.

**분석 오류 또는 제한**

funding cost를 upside model에 덜 반영했다.

**재사용 교훈**

downside는 debt뿐 아니라 dilution도 본다.

### C5. recession이 M&A 기회 — 성공 방향

**원문 주장**

housing 약세가 succession sellers를 늘려 accretive deals를 만든다.

**경제적 메커니즘**

현금·신용으로 약한 competitor를 산다.

**T0 근거**

roll-up playbook과 pipeline.

**숨은 가정**

asset quality·price·financing이 유리하다.

**사전 반증조건**

deal이 없거나 per-share EBITDA가 줄면 반증.

**실제 결과**

2023 LCF를 인수했지만 debt·shares도 늘었다.

**정량 gap**

enterprise scale 증가·per-share 효과 혼합.

**분석 오류 또는 제한**

M&A availability를 accretion과 동일시했다.

**재사용 교훈**

deal별 purchase EV/normalized EBITDA와 FDSO를 기록한다.

### C6. C$1.50 @ 6x EV/EBIT — 지연 성공

**원문 주장**

C$17m EBIT·net debt 0·67m shares면 C$1.50다.

**경제적 메커니즘**

earnings 유지와 multiple rerating.

**T0 근거**

원문 valuation bridge.

**숨은 가정**

2022 earnings와 12~24개월 rerating이 모두 맞는다.

**사전 반증조건**

2024 이전 target 미달이면 timing 실패.

**실제 결과**

2024 C$1.50~1.57 관찰.

**정량 gap**

약 2년 지연·earnings bridge 불일치.

**분석 오류 또는 제한**

terminal target hit으로 original path를 정당화했다.

**재사용 교훈**

target은 earnings·debt·multiple 기여로 attribution한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 C$17m EBIT × 6배 - net debt 0을 67m FDSO로 나누면 약 C$1.52다. 실제 2022 operating income C$12.53m을 같은 방식으로 쓰면 약 C$1.12이고, 2023 C$5.26m이면 약 C$0.47 before net debt다. denominator가 valuation의 대부분이었다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | housing slowdown·24% GM | C$0.5 안팎 | 2023~24 earnings |
| Base | 2022 EBIT C$17m·6x | C$1.50 | price만 지연 실현 |
| Bull | recession M&A+margin 유지 | C$2+ | denominator 미달 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2022 EBIT | C$17m | C$17m | C$12.53m | -26.3% |
| 2022 adjusted EBITDA | LTM ~C$15m | 유지 | C$15.73m | 성공 |
| 2023 operating income | 정상화 유지 | C$17m path | C$5.26m | peak 반증 |
| 2024 normalized EBITDA | 성장 | C$15m+ | C$8.52m | 미달 |
| Price target | C$0.53→C$1.50 | 12~24개월 | 2024 hit | 지연 성공 |

### 촉매와 시간

판정 horizon은 **12~24개월**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2022-05-30 | VIC Long 게시 | 3x EBIT·C$1.50 |
| 2022-12-31 | revenue C$61.90m | banner year |
| 2022-12-31 | operating income C$12.53m | C$17m miss |
| 2023-08-23 | LCF 인수 | M&A option 실행 |
| 2023-12-31 | operating income C$5.26m | peak denominator 반증 |
| 2024 | 주가 C$1.50대 | target 지연 hit |
| 2024-06-26 | C$14.56m equity raise | growth capital·dilution |
| 2024-12-31 | normalized EBITDA C$8.52m | mid-cycle reset |

### 실제 사업·자본구조 추이

2022 revenue C$61.90m, operating income C$12.53m, adjusted EBITDA C$15.73m이었다. 2023 revenue C$49.41m, operating income C$5.26m, normalized EBITDA C$9.93m으로 후퇴했다. 2024 revenue는 C$55.83m으로 회복했지만 normalized EBITDA C$8.52m이었다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

독립 월간 cross-check에서 2024 C$1.50~1.57을 관찰해 target hit만 인정한다. exact entry execution·corporate action·total-return series가 없어 정확한 IRR은 만들지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 2022 banner year | 20% | 성공 | 방향 성공. |
| C2 | 2022 EBIT C$17m | 18% | 실패 | -C$4.47m/-26.3%. |
| C3 | 3x EBIT valuation | 18% | 부분 성공 | 2023 기준 multiple은 약 2배 이상 상승. |
| C4 | balance sheet가 recession을 방어 | 16% | 성공 방향 | survival 성공·희석 비용 존재. |
| C5 | recession이 M&A 기회 | 16% | 성공 방향 | enterprise scale 증가·per-share 효과 혼합. |
| C6 | C$1.50 @ 6x EV/EBIT | 12% | 지연 성공 | 약 2년 지연·earnings bridge 불일치. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

very low entry multiple과 balance-sheet survival, 추가 LCF 인수와 platform optionality가 rerating을 만들었다. 반면 lumber pass-through와 housing strength를 structural EBIT으로 annualize한 것이 forecast miss를 만들었다.

### Counterfactual

2022 gross margin이 32%가 아니라 2024의 24%, normalized EBITDA가 C$8.5m이면 C$0.53에서 진짜 EV/EBITDA와 downside는 얼마인가?

---

## 9. 분석 오류 유형과 최초 경고

좋은 분기 ×4를 정상 earnings로 쓰고 price target의 성공을 operating forecast 성공과 혼동할 위험이 있었다.

### 최초로 관찰 가능했던 경고신호

2022 operating income C$12.53m이 C$17m을 26.3% 미달했고 2023 gross margin 27%·operating income C$5.26m이 peak denominator를 확정 반증했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

낮은 multiple을 보기 전에 denominator가 peak-quarter annualization인지 본다.

### Lesson 2

lumber pass-through로 움직인 revenue와 organic volume을 분리한다.

### Lesson 3

가격목표 적중이 earnings model의 정확성을 증명하지 않는다.

### 지금 같은 아이디어를 다시 본다면

- quarter seasonality
- gross margin normalization
- lumber price vs volume
- housing starts
- net debt
- FDSO
- deal funding
- 3년 평균 EBITDA

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 성공 |
| Valuation thesis | 성공 |
| Earnings thesis | 실패 |
| Timing / path | 약 2년 지연 |
| Security selection | common 적절 |
| Thesis score | 8.1/10 |
| Process score | 9.5/10 |
| 종합 | **지연 성공 — C$1.50 price hit, C$17m EBIT annualization은 실패** |

### 한 문장 교훈

> 낮은 multiple을 보기 전에 denominator가 peak-quarter annualization인지 본다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/ATLAS_ENGINEERED_PRODCTS_LTD/5737776840) — Value Investors Club / source SQL, 2022-05-30. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
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
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
