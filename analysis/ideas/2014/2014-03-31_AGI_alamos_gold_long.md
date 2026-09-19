# Alamos Gold Inc. (AGI) — 2014-03-31 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-19. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Alamos Gold Inc. / AGI |
| VIC 게시일 / 작성자 | 2014-03-31 / andrew152 |
| 분석 증권 / 실제 방향 | TSX/NYSE:AGI common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 원문 약 C$10; source DB next-session close 8.47491 |
| 기대기간 | 2016 Turkey start·production >400koz |
| raw horizon audit | 0.9x NAV→1.5x, target ~C$18; Kirazli/Agi Dagi permits와 debt-free cash |
| 최종 판정 | **실패 — permit·production·horizon 미실현** |

> **결론:** debt-free balance sheet는 회사를 지켰지만 투자 thesis의 clock은 Turkey였다. Kirazli/Agi Dagi가 2016 생산을 만들지 못했고 2015 AuRico merger로 perimeter가 바뀌었다. source DB price-only return은 1Y -34.8%, 2Y -41.4%, 3Y -9.8%로 원 horizon에서 실패했다.

---

## 1. 회사는 정확히 무엇을 하는가

Alamos Gold는 금광을 개발·운영한다. 생산량×realized gold price에서 mining·processing cost, royalties, sustaining·growth capex와 세금을 뺀 현금이 가치의 핵심이다. 개발자산 NAV에는 permit·financing·construction·start-date probability를, 가동광산에는 grade·throughput·reserve replacement와 bottleneck removal을 적용한다.

`ounces × realized gold price - cash cost - sustaining capex - growth capex - tax = equity cash`; project NPV, operating FCF와 gold beta를 별도 claim으로 관리한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

production ounces, grade, recovery, throughput, cash cost/AISC, sustaining/growth capex, mine-site FCF, reserves/resources, net cash/debt, permit and commissioning dates

---

## 2. 당시 상황과 시장이 가격에 넣은 것

Alamos는 cash 약 $475m, no debt와 Mulatos cash flow를 가졌고 Turkey projects·Esperanza를 포함한 NAV 약 C$1.678bn 대비 약 0.9x에 거래된다고 봤다. permits와 construction이 진행되면 2016 production 400koz+, 1.5x NAV와 약 C$18 target가 가능하다는 논지였다.

### Reverse expectations

development NAV는 permit, local opposition, litigation, financing, construction와 start-up timing을 모두 통과해야 한다. 현금은 delay survival을 주지만 NPV timing loss와 gold-price beta를 제거하지 않는다. 1.5x NAV는 execution뿐 아니라 sector multiple rerating도 필요했다.

---

## 3. 원문 투자논지 지도

### C1. debt-free cash downside — 부분 성공

**원문 주장**

~$475m cash·no debt가 downside를 제한한다.

**경제적 메커니즘**

cash가 project delay와 gold downturn을 self-fund한다.

**T0 근거**

strong balance sheet.

**숨은 가정**

cash가 capex·G&A에 과도하게 소모되지 않는다.

**사전 반증조건**

large drawdown에도 floor 부재면 valuation claim 약화.

**실제 결과**

company survived·merged했지만 2Y price -41.4%.

**정량 gap**

survival 성공/price floor 실패.

**분석 오류 또는 제한**

balance sheet와 equity volatility를 혼동했다.

**재사용 교훈**

cash는 per-share commitments 차감 후 본다.

### C2. Turkey permits·2016 start — 강한 실패

**원문 주장**

Kirazli/Agi Dagi가 permit을 받아 2016 생산한다.

**경제적 메커니즘**

low-cost new ounces가 NAV와 cash flow를 현실화한다.

**T0 근거**

project studies·EIA progress.

**숨은 가정**

legal·social license가 schedule 내 해결된다.

**사전 반증조건**

permit delay 12개월+면 반증.

**실제 결과**

Turkey는 2016 production asset가 되지 못했다.

**정량 gap**

start date 수년 miss.

**분석 오류 또는 제한**

binary approval만 보고 local/legal duration을 축소했다.

**재사용 교훈**

permit tree에 dates와 probabilities를 둔다.

### C3. 2016 production >400koz — 실패

**원문 주장**

Turkey+Mulatos growth로 >400koz다.

**경제적 메커니즘**

new mine ramp가 ounces를 늘린다.

**T0 근거**

project schedule와 base operations.

**숨은 가정**

construction·ramp가 계획대로다.

**사전 반증조건**

organic production <360koz면 실패.

**실제 결과**

AuRico merger 후 combined production도 약 392koz.

**정량 gap**

acquired 포함 target 미달.

**분석 오류 또는 제한**

organic/acquired denominator를 섞었다.

**재사용 교훈**

mine별 ounce bridge를 유지한다.

### C4. 0.9x NAV는 cheap — 실패

**원문 주장**

stated NAV 대비 10% 할인이다.

**경제적 메커니즘**

de-risking이 1.0~1.5x multiple을 만든다.

**T0 근거**

NAV ~$1.678bn.

**숨은 가정**

project NAV가 timely realizable하다.

**사전 반증조건**

risked NAV가 market value 이하이면 반증.

**실제 결과**

delay와 gold weakness로 1~2Y price가 크게 하락했다.

**정량 gap**

2Y -41.4%.

**분석 오류 또는 제한**

unrisked NAV를 denominator로 썼다.

**재사용 교훈**

project마다 probability·time haircut를 적용한다.

### C5. 1.5x NAV·C$18 target — 강한 실패

**원문 주장**

permit·production 뒤 premium rerating이 온다.

**경제적 메커니즘**

growth scarcity와 balance sheet가 premium을 지지한다.

**T0 근거**

peer multiple와 asset pipeline.

**숨은 가정**

sector multiple과 gold price가 유지된다.

**사전 반증조건**

discount 지속·price target miss면 실패.

**실제 결과**

source horizons 모두 target 미달, 2Y 큰 손실.

**정량 gap**

target 미실현.

**분석 오류 또는 제한**

execution success와 sector rerating을 동시에 요구했다.

**재사용 교훈**

EPS/FCF와 NAV multiple catalysts를 분리한다.

### C6. M&A optionality — 현실화·원논지 구제 아님

**원문 주장**

cash와 management가 consolidation option을 가진다.

**경제적 메커니즘**

merger가 operating assets와 scale을 추가한다.

**T0 근거**

strong balance sheet.

**숨은 가정**

deal terms가 value accretive하다.

**사전 반증조건**

dilutive perimeter change면 재인수.

**실제 결과**

2015 AuRico merger가 발생했다.

**정량 gap**

option 현실화, original Turkey path 대체.

**분석 오류 또는 제한**

event를 자동 success로 볼 위험.

**재사용 교훈**

deal 후 thesis를 new idea unit로 다시 쓴다.

---

## 4. 당시 Valuation과 Payoff Structure

project NAV에는 `permit probability × build probability × start-date discount`를 적용하고 cash는 corporate G&A·care-and-maintenance·future capex를 차감한다. acquired production은 original organic forecast와 분리한다. source DB returns는 price-only이며 original C$ quote와 통화·listing basis가 다를 수 있다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | Turkey multi-year delay·gold weakness | NAV discount 확대 | 1Y -34.8%, 2Y -41.4% |
| Base | permits·2016 >400koz | ~C$18 | 미실현 |
| Bull | 1.5x NAV·projects on time | C$18+ | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 1Y price-only | Long | 상승 | -34.8% | 실패 |
| 2Y price-only | Long | target 접근 | -41.4% | 강한 실패 |
| 3Y price-only | Long | rerating | -9.8% | 실패 |
| 2016 production | >400koz organic framing | >400koz | ~392koz combined | 실패 |
| Turkey start | 2016 | production | 미실현 | 강한 실패 |

### 촉매와 시간

판정 horizon은 **2016 Turkey start·production >400koz**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2014-03-31 | VIC Long | ~0.9x NAV |
| 2014-09 | gold weakness | NAV beta |
| 2015-03-31 | 1Y -34.8% | timing break |
| 2015 | AuRico merger | perimeter change |
| 2016-03-31 | 2Y -41.4% | security failure |
| 2016 | combined production ~392koz | >400koz miss |
| 2017-03-31 | 3Y -9.8% | 미회복 |
| 2020 | Turkey still non-producing | original clock failure |

### 실제 사업·자본구조 추이

Turkey는 원래 2016 production schedule를 달성하지 못했다. 2015 AuRico merger로 Young-Davidson 등 새 assets가 들어오며 original company perimeter가 변경됐고 combined 2016 production도 약 392koz였다. 이후 Alamos 성공을 이 2014 Turkey thesis의 horizon 성공으로 소급하지 않는다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

source DB next-session base 8.47491에서 1Y ratio 0.651929(-34.8%), 2Y 0.585638(-41.4%), 3Y 0.901842(-9.8%)다. dividend·tax 제외이며 5Y row는 없다. 원문 약 C$10 quote와 DB price의 단위 차이 때문에 exact original-position IRR이 아니라 horizon 판정에만 쓴다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | debt-free cash downside | 20% | 부분 성공 | survival 성공/price floor 실패. |
| C2 | Turkey permits·2016 start | 18% | 강한 실패 | start date 수년 miss. |
| C3 | 2016 production >400koz | 18% | 실패 | acquired 포함 target 미달. |
| C4 | 0.9x NAV는 cheap | 16% | 실패 | 2Y -41.4%. |
| C5 | 1.5x NAV·C$18 target | 16% | 강한 실패 | target 미실현. |
| C6 | M&A optionality | 12% | 현실화·원논지 구제 아님 | option 현실화, original Turkey path 대체. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

손실은 gold weakness와 project timing discount 확대가 만들었다. cash/no debt는 insolvency를 막았지만 permit delay로 NPV가 멀어졌고, merger는 assets를 바꿔 original Turkey catalyst의 direct payoff를 희석했다.

### Counterfactual

Turkey가 3년 늦어지고 금값이 15% 낮아져도 0.9x stated NAV가 실제 risk-adjusted NAV 대비 할인인가, 오히려 premium인가?

---

## 9. 분석 오류 유형과 최초 경고

unrisked project NAV를 높은 weight로 쓰고 permit/legal clock을 binary catalyst처럼 봤다. no-debt를 share-price floor로, M&A production을 organic thesis validation으로 볼 위험도 있었다.

### 최초로 관찰 가능했던 경고신호

2014~15 Turkey schedule가 미끄러지고 주가가 1Y -34.8%가 된 시점에 timing thesis는 반증됐다. 2015 merger는 original idea를 새 security/perimeter로 재인수할 사건이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

development-mine NAV에는 permit·build·time probability를 곱한다.

### Lesson 2

debt-free cash는 survival asset이지 share-price floor가 아니다.

### Lesson 3

M&A 뒤 acquired ounces로 original organic forecast를 구제하지 않는다.

### Lesson 4

commodity beta와 company execution을 각각 score한다.

### 지금 같은 아이디어를 다시 본다면

- permit/legal milestones
- local opposition
- capex funding
- construction critical path
- organic vs acquired ounces
- gold sensitivity
- risked NAV
- cash after commitments

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | survival 성공 |
| Valuation thesis | 실패 |
| Catalyst thesis | 강한 실패 |
| Security payoff | common 손실 |
| Timing / path | 실패 |
| Thesis score | 3.5/10 |
| Process score | 6.5/10 |
| 종합 | **실패 — permit·production·horizon 미실현** |

### 한 문장 교훈

> development-mine NAV에는 permit·build·time probability를 곱한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/ALAMOS_GOLD_INC/0481433134) — Value Investors Club / source SQL, 2014-03-31. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Alamos FY2018 results](https://www.alamosgold.com/news-and-events/news/news-details/2019/Alamos-Reports-Fourth-Quarter-and-Year-End-2018-Results/default.aspx) — Alamos Gold, 2019-02-20. 2018 production 505koz, debt-free balance sheet, cash $206m과 operating context 검증.
3. [Young-Davidson lower-mine completion](https://www.alamosgold.com/news-and-events/news/news-details/2020/Alamos-Gold-Announces-Completion-of-Lower-Mine-Expansion-at-Young-Davidson-Mine/default.aspx) — Alamos Gold, 2020-07. Northgate shaft·crusher/conveyor commissioning과 약 8,000 tpd design path 검증.
4. [Alamos 2020 reserves and resources](https://www.alamosgold.com/news-and-events/news/news-details/2021/Alamos-Gold-Reports-Mineral-Reserves-and-Resources-for-the-Year-Ended-2020/default.aspx) — Alamos Gold, 2021. Island Gold reserves가 2017 acquisition 이후 depletion 순감 후 74% 증가했음을 검증.
5. [Alamos FY2025 results](https://www.alamosgold.com/news-and-events/news/news-details/2026/Alamos-Gold-Reports-Fourth-Quarter-and-Year-End-2025-Results/) — Alamos Gold, 2026-02. 2025 production 545.4koz, free cash flow $351.7m과 mine별 cash generation 검증.
6. [Alamos Q1 2026 results](https://www.alamosgold.com/news-and-events/news/news-details/2026/Alamos-Gold-Reports-First-Quarter-2026-Results/default.aspx) — Alamos Gold, 2026-04-29. Q1 FCF $101.7m, net cash·liquidity와 operating follow-through 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B/C** — AGCO 2015·Alamos 2014는 source SQL price-only ratios, 그 외는 verified corporate action·official operating actual·제한적 market cross-check만 사용. complete dated ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
