# Murphy USA Inc. — 2020-01-02 — V9

> **Batch 049 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Short**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Murphy USA Inc. / MUSA |
| Idea ID | `33322efc-4c79-44a0-bae8-d523401d5294` |
| 게시일 / 작성자 | 2020-01-02 / helopilot |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Short** |
| 기준가격 | $112.19 next-day close |
| 원 horizon | 3~12개월 |
| 최종 판정 | **초기 trade 성공 / 중기 thesis 강한 실패 — 3개월 +27.1%, 3년 -143.2% simple Short** |

> **결론:** raw와 실제 모두 Short다. gasoline과 cigarettes를 dual melting ice cube로 규정하고, 작은 kiosk 중심 MUSA가 Casey's·Couche-Tard와 같은 10~11x EBITDA를 받는 것은 과도하다고 봤다. 8x $420m EBITDA로 $85, 약 -27%를 제시했고 Q4 miss, tobacco/vaping 약세, CEO 이탈과 Speedway spin을 catalyst로 들었다. 결과적으로 **초기 trade 성공 / 중기 thesis 강한 실패 — 3개월 +27.1%, 3년 -143.2% simple Short**.

---

## 1. 회사는 정확히 무엇을 하는가

Murphy USA는 대형 소형매장·kiosk 기반의 연료 및 편의점 체인이다. 당시 핵심 입지는 Walmart 인접 부지였고 Murphy Express, 이후 QuickChek까지 포맷을 넓혔다. 주당가치 엔진은 gallons × total fuel contribution per gallon + merchandise gross profit - store operating cost - SG&A - maintenance/growth capex - interest·tax를 계속 줄어드는 희석주식수로 나눈 값이다. 연료수요 감소가 곧 연료이익 감소는 아니다. 소규모 독립사업자의 breakeven CPG, 공급 최적화·RIN, 경쟁강도와 가격전가 속도가 volume과 반대 방향으로 움직일 수 있기 때문이다.

### Common equity cash waterfall

회계이익에서 운전자본·담보·규제자본·maintenance/growth investment·interest·tax를 차감하고, common보다 선순위인 계약·채권자 청구권을 먼저 배치한다. 자산가치와 계약상 수취액은 현금화 날짜·세금·재투자 의무를 반영한다. 기업가치가 맞아도 security와 duration이 틀리면 투자결과는 실패할 수 있다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw와 실제 모두 Short다. gasoline과 cigarettes를 dual melting ice cube로 규정하고, 작은 kiosk 중심 MUSA가 Casey's·Couche-Tard와 같은 10~11x EBITDA를 받는 것은 과도하다고 봤다. 8x $420m EBITDA로 $85, 약 -27%를 제시했고 Q4 miss, tobacco/vaping 약세, CEO 이탈과 Speedway spin을 catalyst로 들었다.

### Reverse expectations

$112.19 next-day close가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. 10~11x excessive — 20%

- **원문 주장:** 저성장 kiosk에 infrastructure multiple은 부당하다.
- **T0 근거:** 2013~19 EBITDA 정체
- **숨은 가정:** normalized earnings가 $420m 부근에 머문다.
- **사전 반증조건:** CPG·owner earnings/share 상승이면 반증.
- **실제:** earnings power가 크게 재평가됐다.
- **판정:** **중기 실패**
- **재사용 교훈:** multiple Short는 denominator 변화를 먼저 본다.

### C2. gasoline melting ice cube — 18%

- **원문 주장:** EV와 효율이 gallons·EBITDA를 줄인다.
- **T0 근거:** 장기 gasoline demand headwind
- **숨은 가정:** CPG가 volume 감소를 상쇄하지 않는다.
- **사전 반증조건:** volume down·fuel profit up이면 반증.
- **실제:** 2020에 바로 그 divergence가 발생했다.
- **판정:** **실패**
- **재사용 교훈:** 수요량과 unit margin의 산업반응을 함께 모델링한다.

### C3. tobacco weakness — 18%

- **원문 주장:** 연령·vaping 규제가 merchandise를 훼손한다.
- **T0 근거:** 21세 상향·flavored vape 규제
- **숨은 가정:** non-nicotine·food가 대체하지 못한다.
- **사전 반증조건:** merchandise GP/store가 유지되면 반증.
- **실제:** headwind는 있었지만 QuickChek·mix가 보완했다.
- **판정:** **부분 성공**
- **재사용 교훈:** category decline과 store basket을 분리한다.

### C4. capex no return — 16%

- **원문 주장:** $1bn+ capex에도 EBITDA 성장이 없다.
- **T0 근거:** 작은 format 비중·과거 EBITDA
- **숨은 가정:** R&R/new store cohort가 낮은 ROIC다.
- **사전 반증조건:** cohort contribution과 store count가 증가하면 반증.
- **실제:** 성장 플랫폼과 1,800 stores로 이어졌다.
- **판정:** **실패**
- **재사용 교훈:** aggregate EBITDA 대신 cohort IRR을 본다.

### C5. catalyst basket — 16%

- **원문 주장:** Q4 miss·CEO·Speedway가 de-rate를 촉발한다.
- **T0 근거:** event speculation과 weak season
- **숨은 가정:** 발생확률·영향이 충분하다.
- **사전 반증조건:** 핵심 catalyst가 비발생하고 earnings가 beat하면 반증.
- **실제:** COVID 외생충격이 실제 초기 catalyst였다.
- **판정:** **논지 미스**
- **재사용 교훈:** 관찰 가능한 catalyst만 probability-weight한다.

### C6. $85 sustained value — 12%

- **원문 주장:** 8x $420m이 지속 fair value다.
- **T0 근거:** 역사적 7~8x range
- **숨은 가정:** target hit 뒤에도 fundamentals가 악화한다.
- **사전 반증조건:** target hit가 외생 shock이고 KPI가 개선되면 cover.
- **실제:** 3개월 성공 뒤 1~3년 큰 손실이었다.
- **판정:** **path 실패**
- **재사용 교훈:** target hit와 thesis validation을 별도 gate로 둔다.

---

## 4. 당시 Valuation과 Payoff Structure

$420m EBITDA × 8x와 순부채로 $85를 만들었다. 이 모델은 EBITDA가 2013~2019 정체한다는 출발은 합리적이었지만 gallons decline 때 cpg가 어떻게 반응하는지 빠졌다. secular terminal decline과 12개월 cash earnings를 같은 multiple로 압축했고, intrinsic value 아래의 buyback이 share count를 줄이는 효과도 충분히 반영하지 않았다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Short 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 초기 trade 성공 / 중기 thesis 강한 실패 — 3개월 +27.1%, 3년 -143.2% simple Short의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / fair value | $112.19 | $85 | 3M Short +27.1% | 단기 성공 |
| Normalized EBITDA | $420m | 정체/하락 | 2020~21 record economics | 실패 |
| Valuation | 10~11x | 8x | earnings power 재평가 | 실패 |
| 2020 buyback | 부담/정체 | 감소 기대 | $399.6m·3.3m shares | 실패 |
| 3Y payoff | 지속 de-rate | 양의 Short 수익 | -143.2% simple Short | 강한 실패 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2020-01-02 | VIC Short | $85 target |
| 2020-03 | COVID crash | 3개월 +27.1% Short MFE |
| 2020-FY | gallons 감소·fuel economics 강화 | core thesis 반증 |
| 2020-FY | $399.6m·3.3m shares repurchase | per-share engine |
| 2021-01-29 | $645m QuickChek close | merchandise expansion |
| 2021-FY | record earnings·$355m repurchase | Short break 확정 |
| 2023-01 | 3년 multiplier 2.432x | simple Short -143.2% |

### 실제 사업·자본구조

COVID는 2020 Q1 주가와 gallons를 급락시켜 초기 Short에 큰 이익을 줬다. 그러나 독립사업자들이 생존 margin을 높이고 MUSA의 supply scale이 작동하면서 fuel contribution과 earnings가 오히려 강해졌다. 회사는 2020에 3.3m shares를 $399.6m에 매입하고 2021-01-29 QuickChek을 $645m에 인수했다. 2021에도 record earnings와 $355m repurchase가 이어졌다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

실제 Short 기준 1M +9.2%, 3M +27.1%, 6M +1.0%, 1Y -12.9%, 2Y -75.3%, 3Y -143.2%다. 초기 $85 근처까지의 하락은 훌륭한 trade였지만 외생 COVID shock이 원인이었다. target hit 뒤 cover하지 않고 secular thesis로 연장하면 simple Short 손실이 -100%를 넘었다.

이 아이디어는 repository에 보존된 price multiplier를 실제 Short 방향으로 교정했다. Long은 multiplier-1, Short는 1-multiplier인 price-only 수익이며 배당·borrow·거래비용은 포함하지 않는다. 누락 horizon은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | 10~11x excessive | 20% | 중기 실패 | multiple Short는 denominator 변화를 먼저 본다. |
| C2 | gasoline melting ice cube | 18% | 실패 | 수요량과 unit margin의 산업반응을 함께 모델링한다. |
| C3 | tobacco weakness | 18% | 부분 성공 | category decline과 store basket을 분리한다. |
| C4 | capex no return | 16% | 실패 | aggregate EBITDA 대신 cohort IRR을 본다. |
| C5 | catalyst basket | 16% | 논지 미스 | 관찰 가능한 catalyst만 probability-weight한다. |
| C6 | $85 sustained value | 12% | path 실패 | target hit와 thesis validation을 별도 gate로 둔다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

초기 수익의 원인은 catalyst list보다 COVID liquidity shock이었다. 이후 손실은 volume 감소가 industry CPG를 높이는 역설, low-cost operator의 share gain, 상품/food 확장과 공격적 repurchase였다. 맞는 매크로 방향을 틀린 unit-economics sign으로 연결했다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 $112.19 next-day close에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

gasoline demand와 retail fuel profit을 같은 방향으로 두었고 EV penetration의 속도·고객 mix를 horizon에 맞추지 않았다. catalyst 네 개는 독립 확률과 expected impact가 없었고, CEO 이탈 추측은 falsifiable evidence가 약했다. target 도달 시 cover rule 부재가 가장 큰 security-level 오류다.

### 최초 관찰 가능한 경고/반증

2020 demand crash 중 gallons가 무너졌는데 fuel CPG와 EBITDA가 상승하는 것이 thesis break였다. 3개월 +27.1% 수익 구간에서 외생 shock과 원래 논지를 분리하고 전량 또는 대부분 cover했어야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** ticker MUSA만 보지 말고 Murphy USA Inc.의 법인·security·날짜로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Short을 확정한다.
3. **Bridge:** target을 EPS/book/NAV와 cash waterfall로 연결한다.
4. **Falsifier:** 최초 경고에 날짜와 수치를 둔다.
5. **Path:** 원 horizon과 terminal event를 섞지 않는다.
6. **Missing data:** SQL performance가 없으면 null을 유지한다.

### 다시 분석한다면

- legal/capital/funding gate를 확률·날짜별로 나눈다.
- gross asset value와 common에 귀속되는 순가치를 분리한다.
- base/bull target뿐 아니라 survival/recovery case를 수치화한다.
- corporate action 이후 교환비율·배당·successor price를 연결해 total return을 복원한다.
- event가 맞아도 price target이 실패할 수 있도록 exit/cover rule을 미리 쓴다.

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Entity / direction | raw Short → **Short**, Murphy USA Inc. |
| Business thesis | 실패 |
| Valuation thesis | 단기 성공 |
| Catalyst / timing | 초기 trade 성공 / 중기 thesis 강한 실패 — 3개월 +27.1%, 3년 -143.2% simple Short |
| Thesis score | 5.0/10 |
| Process score | 7.0/10 |
| Outcome-adjusted score | 6.0/10 |

### 한 문장 교훈

> multiple Short는 denominator 변화를 먼저 본다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/MURPHY_USA_INC/0938974983) — VIC_IDEAS(4).sql / VIC, 2020-01-02. idea_id·raw direction·description 6021 chars·catalyst 102 chars
2. [Murphy USA spin-off completion 8-K](https://www.sec.gov/Archives/edgar/data/1573516/000157351613000008/musa-20130905x8k.htm) — SEC / Murphy USA, 2013-08-30. Murphy Oil에서 1:4 배분으로 독립한 법인·security 경계
3. [Murphy USA 2017 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2018/Murphy-USA-Inc-Reports-Preliminary-Fourth-Quarter-2017-Results/default.aspx) — Murphy USA, 2018-02. 2017 gallons, fuel contribution, merchandise와 repurchase
4. [Murphy USA 2018 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2019/Murphy-USA-Inc-Reports-Preliminary-Fourth-Quarter-2018-Results/) — Murphy USA, 2019-02. 2018 adjusted EBITDA $412m, CPG와 same-store volume
5. [Murphy USA 2020 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2021/Murphy-USA-Inc.-Reports-Fourth-Quarter-2020-Results/default.aspx) — Murphy USA, 2021-02. COVID volume 충격, fuel economics와 $399.6m repurchase
6. [Murphy USA 2021 results](https://ir.corporate.murphyusa.com/investor-relations/news-releases/press-release-details/2022/Murphy-USA-Inc.-Reports-Fourth-Quarter-2021-Results/default.aspx) — Murphy USA, 2022-02. QuickChek 첫해, record EBITDA와 $355m repurchase
7. [Murphy USA 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1573516/000157351626000090/musa-20251231.htm) — SEC / Murphy USA, 2026-02. 1,800 stores, 30.7 cpg, adjusted EBITDA $1,019.4m와 누적 $4.1bn repurchase

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **B** — repository multiplier를 실제 Short 방향으로 교정. price-only이며 누락 horizon은 null.
- 교정: ticker=MUSA, entity=Murphy USA Inc., raw=Short, research=Short.
