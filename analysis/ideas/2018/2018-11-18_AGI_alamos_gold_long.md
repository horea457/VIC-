# Alamos Gold Inc. (AGI.) — 2018-11-18 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-19. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Alamos Gold Inc. / AGI. |
| VIC 게시일 / 작성자 | 2018-11-18 / EITR210 |
| 분석 증권 / 실제 방향 | NYSE:AGI common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 US$3.60 |
| 기대기간 | 2~4년 Young-Davidson fix·Island Gold reserve growth |
| raw horizon audit | $1,200 gold에서 $5.15 target; lower-mine infrastructure와 debt-free balance sheet |
| 최종 판정 | **매우 강한 성공 — operational fix·reserve growth·target 초과** |

> **결론:** 2014의 Turkey option이 아니라 가동광산 repair를 샀다. Young-Davidson lower-mine expansion은 2020 완료됐고 Island Gold reserves는 acquisition 이후 2020까지 depletion 순감 후 74% 늘었다. 2025 production 545.4koz·FCF $351.7m, 2026-09 market check $35.72로 $3.60 entry와 $5.15 target를 크게 넘었다. 다만 gold beta를 company alpha와 분리한다.

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

Young-Davidson bottleneck과 acquisition complexity 때문에 shares가 약 $3.60, 0.5x book 이하로 보였다. debt-free balance sheet, Island Gold의 high-grade reserve potential과 lower-mine shaft/crusher/conveyor가 완료되면 $1,200 gold에서도 $5.15가 가능하다는 thesis였다. 2018 production은 505koz였다.

### Reverse expectations

Young-Davidson expansion은 capital·commissioning risk가 있었고 Island Gold reserve additions가 economic ounces로 전환되지 않을 수 있었다. mine valuation은 gold price에 민감하며 low book multiple 일부는 cost·jurisdiction·asset-quality 차이를 반영한다. 장기 return 대부분이 gold 상승일 가능성도 있었다.

---

## 3. 원문 투자논지 지도

### C1. Young-Davidson lower-mine fix — 강한 성공

**원문 주장**

shaft·crusher·conveyor가 bottleneck을 제거한다.

**경제적 메커니즘**

ore-handling reliability와 throughput가 cost/oz와 FCF를 개선한다.

**T0 근거**

defined infrastructure project.

**숨은 가정**

commissioning이 budget·schedule에 가깝다.

**사전 반증조건**

completion delay·throughput miss면 반증.

**실제 결과**

2020-07 lower-mine expansion이 완료됐다.

**정량 gap**

dated catalyst 실현.

**분석 오류 또는 제한**

ramp와 mechanical completion을 같게 볼 위험.

**재사용 교훈**

completion 뒤 sustained throughput를 확인한다.

### C2. ~8,000 tpd sustainable rate — 성공

**원문 주장**

lower mine가 약 8,000 tpd를 지원한다.

**경제적 메커니즘**

higher steady mining rate가 fixed-cost absorption과 ounces를 안정화한다.

**T0 근거**

design/ramp plan.

**숨은 가정**

grade·equipment availability가 유지된다.

**사전 반증조건**

sustained rate 크게 미달하면 실패.

**실제 결과**

후속 reserve framework와 operations가 8,000 tpd path를 지지했다.

**정량 gap**

정확한 매분기 rate는 별도 추적 필요.

**분석 오류 또는 제한**

design을 realized average로 부르지 않는다.

**재사용 교훈**

quarterly tonnes·grade·cost를 같이 본다.

### C3. Island Gold reserve quality — 강한 성공

**원문 주장**

high-grade asset가 acquisition value를 키운다.

**경제적 메커니즘**

reserve additions net depletion이 mine life·NPV를 높인다.

**T0 근거**

exploration potential과 grades.

**숨은 가정**

drilling success가 economic reserve로 전환된다.

**사전 반증조건**

reserve replacement <100%면 약화.

**실제 결과**

2020 reserves는 2017 acquisition 이후 net depletion 기준 +74%.

**정량 gap**

강한 초과달성.

**분석 오류 또는 제한**

resource와 reserve를 섞을 수 있다.

**재사용 교훈**

reserve conversion·grade·cost를 따로 기록한다.

### C4. debt-free balance sheet — 성공

**원문 주장**

cash/no debt가 projects를 self-fund한다.

**경제적 메커니즘**

funding stress 없이 lower mine·exploration을 지속한다.

**T0 근거**

2018 cash $206m·no debt.

**숨은 가정**

capex와 gold downside를 cash flow가 감당한다.

**사전 반증조건**

dilutive equity·distress debt면 실패.

**실제 결과**

growth investment 뒤 record 2025 FCF와 positive net liquidity를 확보했다.

**정량 gap**

resilience 확인.

**분석 오류 또는 제한**

후속 portfolio 변화 영향 존재.

**재사용 교훈**

project-level sources/uses로 본다.

### C5. $5.15 at $1,200 gold — 강한 성공

**원문 주장**

operating repair만으로 43% upside다.

**경제적 메커니즘**

risk discount 축소와 mine FCF 정상화가 target를 만든다.

**T0 근거**

mine NAV·low entry.

**숨은 가정**

gold가 base 근처이고 fix가 성공한다.

**사전 반증조건**

fix 뒤 target 미달이면 실패.

**실제 결과**

장기 market check $35.72로 target 초과.

**정량 gap**

초과분 상당 부분 gold beta.

**분석 오류 또는 제한**

target hit와 attribution을 혼용할 수 있다.

**재사용 교훈**

base-gold and actual-gold value를 분리한다.

### C6. long-run FCF compounding — 강한 성공

**원문 주장**

quality assets가 capital investment 뒤 cash를 낸다.

**경제적 메커니즘**

reserve growth·throughput·price가 mine-site FCF로 전환된다.

**T0 근거**

asset quality와 low leverage.

**숨은 가정**

capex가 끝나고 cash conversion이 나타난다.

**사전 반증조건**

persistent negative FCF면 실패.

**실제 결과**

2025 company FCF $351.7m, Q1 2026 $101.7m.

**정량 gap**

cash outcome 확인.

**분석 오류 또는 제한**

high gold price 도움 큼.

**재사용 교훈**

volume·margin·price bridge로 attribution한다.

---

## 4. 당시 Valuation과 Payoff Structure

mine별 risked NAV와 through-cycle FCF를 사용한다. $5.15 target는 $1,200 gold base에서 operating fix의 value를 테스트하고, 실제 장기 price는 realized gold price·new acquisitions·share count를 별도 attribution한다. 2026 market price는 시점 cross-check이며 total return·IRR이 아니다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | lower-mine delay·$1,100 gold | $2.5~3.5 | 미실현 |
| Base | fix·$1,200 gold | $5.15 | target 초과 |
| Bull | Island growth·gold upside | multi-bagger | $35.72 point check |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry/target | $3.60/$5.15 | +43% | $35.72 point check | 매우 강한 성공 |
| 2018 production | 505koz | stable/grow | 505koz | 기반 확인 |
| YD lower mine | under construction | completion | 2020-07 완료 | 강한 성공 |
| Island reserves | growth thesis | replace depletion | +74% since 2017 by 2020 | 강한 성공 |
| 2025 production/FCF | long-run quality | cash generation | 545.4koz/$351.7m | 성공 |

### 촉매와 시간

판정 horizon은 **2~4년 Young-Davidson fix·Island Gold reserve growth**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2018-11-18 | VIC Long | $3.60→$5.15 |
| 2018-12-31 | 505koz production | base established |
| 2019 | lower-mine construction | execution period |
| 2020-07 | lower mine completed | bottleneck catalyst |
| 2020-12-31 | Island reserves +74% | asset quality |
| 2021 | 8,000 tpd framework | throughput validation |
| 2025-12-31 | 545.4koz·$351.7m FCF | cash realization |
| 2026-09-18 | $35.72 market check | target far exceeded |

### 실제 사업·자본구조 추이

2018 production은 505koz, year-end cash $206m·debt 없음이었다. Young-Davidson lower-mine expansion은 2020-07 완료돼 roughly 8,000 tpd design path를 열었다. Island Gold reserves는 2017 acquisition 이후 2020까지 74% 증가했다. 2025 production 545.4koz와 record FCF $351.7m, Q1 2026 FCF $101.7m을 기록했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

2026-09-18 market cross-check $35.72는 $3.60의 약 9.9x이고 $5.15 target를 크게 초과한다. 이는 price-only point comparison이며 배당·세금·holding ledger가 없어 IRR로 쓰지 않는다. 또한 2018 $1,200 assumption보다 높은 gold prices와 후속 portfolio changes가 장기 payoff에 크게 기여했다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | Young-Davidson lower-mine fix | 20% | 강한 성공 | dated catalyst 실현. |
| C2 | ~8,000 tpd sustainable rate | 18% | 성공 | 정확한 매분기 rate는 별도 추적 필요. |
| C3 | Island Gold reserve quality | 18% | 강한 성공 | 강한 초과달성. |
| C4 | debt-free balance sheet | 16% | 성공 | resilience 확인. |
| C5 | $5.15 at $1,200 gold | 16% | 강한 성공 | 초과분 상당 부분 gold beta. |
| C6 | long-run FCF compounding | 12% | 강한 성공 | cash outcome 확인. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

company-specific value는 lower-mine bottleneck removal, Island Gold reserve growth와 debt-free funding capacity에서 왔다. macro value는 gold-price 상승에서 왔다. 좋은 entry는 execution과 commodity beta 모두에 option value를 줬지만 두 기여를 전부 management alpha로 귀속하면 안 된다.

### Counterfactual

gold가 계속 $1,200이고 lower-mine ramp가 12개월 늦어졌어도 mine-level FCF와 risked NAV만으로 $5.15 target가 성립했는가?

---

## 9. 분석 오류 유형과 최초 경고

핵심 mechanism은 좋았지만 long-run outcome에서 gold beta와 later acquisitions를 원 thesis alpha로 과대귀속할 수 있다. book value discount 역시 mine-quality와 future capex를 충분히 반영해야 한다.

### 최초로 관찰 가능했던 경고신호

명확한 thesis break는 없었다. 사전 경고는 lower-mine commissioning 지연, sustained throughput 8,000 tpd 미달과 Island Gold reserve replacement 실패였는데 핵심 milestone은 반대로 달성됐다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

가동광산 bottleneck fix는 distant permit optionality보다 검증 가능하다.

### Lesson 2

reserve growth는 acquisition quality를 depletion 순감 후 평가한다.

### Lesson 3

debt-free balance sheet는 growth-capex 동안 option value를 준다.

### Lesson 4

commodity beta와 company execution return을 분리한다.

### 지금 같은 아이디어를 다시 본다면

- mine throughput
- grade/recovery
- commissioning date
- reserve additions net depletion
- mine-site FCF
- growth capex
- net cash
- gold-price attribution

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 강한 성공 |
| Valuation thesis | 강한 성공 |
| Catalyst thesis | 강한 성공 |
| Security payoff | common 적절 |
| Timing / path | 강한 성공 |
| Thesis score | 9.6/10 |
| Process score | 8.8/10 |
| 종합 | **매우 강한 성공 — operational fix·reserve growth·target 초과** |

### 한 문장 교훈

> 가동광산 bottleneck fix는 distant permit optionality보다 검증 가능하다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/ALAMOS_GOLD_INC/4349354391) — Value Investors Club / source SQL, 2018-11-18. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Alamos FY2018 results](https://www.alamosgold.com/news-and-events/news/news-details/2019/Alamos-Reports-Fourth-Quarter-and-Year-End-2018-Results/default.aspx) — Alamos Gold, 2019-02-20. 2018 production 505koz, debt-free balance sheet, cash $206m과 operating context 검증.
3. [Young-Davidson lower-mine completion](https://www.alamosgold.com/news-and-events/news/news-details/2020/Alamos-Gold-Announces-Completion-of-Lower-Mine-Expansion-at-Young-Davidson-Mine/default.aspx) — Alamos Gold, 2020-07. Northgate shaft·crusher/conveyor commissioning과 약 8,000 tpd design path 검증.
4. [Alamos 2020 reserves and resources](https://www.alamosgold.com/news-and-events/news/news-details/2021/Alamos-Gold-Reports-Mineral-Reserves-and-Resources-for-the-Year-Ended-2020/default.aspx) — Alamos Gold, 2021. Island Gold reserves가 2017 acquisition 이후 depletion 순감 후 74% 증가했음을 검증.
5. [Alamos FY2025 results](https://www.alamosgold.com/news-and-events/news/news-details/2026/Alamos-Gold-Reports-Fourth-Quarter-and-Year-End-2025-Results/) — Alamos Gold, 2026-02. 2025 production 545.4koz, free cash flow $351.7m과 mine별 cash generation 검증.
6. [Alamos Q1 2026 results](https://www.alamosgold.com/news-and-events/news/news-details/2026/Alamos-Gold-Reports-First-Quarter-2026-Results/default.aspx) — Alamos Gold, 2026-04-29. Q1 FCF $101.7m, net cash·liquidity와 operating follow-through 검증.
7. AGI market-price cross-check — market data, 2026-09-18. $35.72 point-in-time price; total return·IRR이 아닌 target comparison에만 사용.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B/C** — AGCO 2015·Alamos 2014는 source SQL price-only ratios, 그 외는 verified corporate action·official operating actual·제한적 market cross-check만 사용. complete dated ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
