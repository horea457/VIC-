# Groupe Aeroplan Inc. / Aimia Inc. (AER CN) — 2011-09-15 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Groupe Aeroplan Inc. / Aimia Inc. / AER CN |
| VIC 게시일 / 작성자 | 2011-09-15 / castor13 |
| 분석 증권 / 실제 방향 | Canadian AER/AIM common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 원문 약 C$12대 |
| 기대기간 | 2013 |
| raw horizon audit | C$1.60 FCF/share·C$24 target by 2013 |
| 최종 판정 | **혼합 — 현금엔진은 유효, C$24 실패·anchor-partner tail 현실화** |

> **결론:** 포인트 선판매·breakage·redemption spread의 capital-light economics와 단기 FCF 회복은 유효했다. 그러나 C$24 target는 실패했고 coalition diversification이 Air Canada anchor risk를 제거하지 못했다. 2017 non-renewal이 topology risk를 드러냈고 Aeroplan은 약 C$450m headline, 최종 조정 후 약 C$516m cash로 매각됐다. SQL 미국 AER 성과는 AerCap이라 폐기한다.

---

## 1. 회사는 정확히 무엇을 하는가

Groupe Aeroplan은 뒤에 Aimia로 사명을 바꾸고 coalition loyalty program을 운영했다. 은행·항공사·소매업체에 포인트를 선판매해 현금을 먼저 받고 redemption 때 비용을 인식한다. spread·breakage·float는 매력적이지만 anchor airline과 카드 파트너가 이탈하면 미래 billings와 보상의 효용이 동시에 약해진다.

`gross billings + ancillary revenue - redemption cost - opex - tax ± reserve/working-capital change = equity FCF`; float와 경제적 부채를 함께 본다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

gross billings, active members, miles issued/redeemed, cost per mile, breakage, redemption reserve, FCF, partner concentration, contract expiry

---

## 2. 당시 상황과 시장이 가격에 넣은 것

원문은 normalized FCF C$205m·C$1.25/share, 약 10% FCF yield와 2013 C$1.60/share를 제시했다. 21% breakage와 C$300m redemption reserve, Nectar·Carlson·analytics·신규 coalition을 근거로 Aeroplan Canada 의존도가 낮아지고 C$24가 가능하다고 봤다.

### Reverse expectations

시장은 accounting breakage·reserve의 추정오차보다 Air Canada와 카드사의 계약갱신·member utility가 단일 실패점임을 할인했다. coalition은 member 수가 많아도 핵심 airline reward와 accumulation partner가 빠지면 network value가 비선형으로 떨어진다.

---

## 3. 원문 투자논지 지도

### C1. loyalty model은 capital-light/high-FCF — 성공

**원문 주장**

포인트 선판매와 breakage가 낮은 capex로 FCF를 만든다.

**경제적 메커니즘**

cash-in이 redemption cash-out보다 앞서 float와 spread가 생긴다.

**T0 근거**

C$205m normalized FCF·C$300m reserve.

**숨은 가정**

partner contracts와 redemption economics가 안정적이다.

**사전 반증조건**

billings·FCF가 구조적으로 감소하면 반증.

**실제 결과**

초기 수년 현금창출과 Aeroplan의 매각가치가 franchise를 확인했다.

**정량 gap**

경제적 부채 조정 후 FCF는 headline보다 낮을 수 있음.

**분석 오류 또는 제한**

working-capital float를 영구 earnings로 볼 위험.

**재사용 교훈**

issuance·redemption cohort와 liability를 함께 본다.

### C2. 2013 FCF C$1.60/share — 부분 성공

**원문 주장**

integration·growth로 per-share FCF가 C$1.60이 된다.

**경제적 메커니즘**

core Canada와 Nectar·analytics가 비용을 흡수하고 성장한다.

**T0 근거**

T0 C$1.25 normalized base.

**숨은 가정**

Carlson integration·partner economics가 개선된다.

**사전 반증조건**

2013 owner FCF가 target에 크게 미달하면 반증.

**실제 결과**

현금흐름은 개선됐으나 exact owner-FCF comparability가 회계변경으로 제한됐다.

**정량 gap**

point estimate 완전 검증 제한.

**분석 오류 또는 제한**

reported FCF와 economic FCF bridge가 부족했다.

**재사용 교훈**

reserve·billings growth·one-offs를 조정한다.

### C3. C$24 by 2013 — 실패

**원문 주장**

C$1.60 FCF에 15x를 받아 두 배가 된다.

**경제적 메커니즘**

earnings growth와 quality rerating이 결합한다.

**T0 근거**

원문 explicit target.

**숨은 가정**

multiple이 partner concentration을 낮게 평가한다.

**사전 반증조건**

2013까지 target 미달이면 실패.

**실제 결과**

공개 역사 cross-check에서 C$24 미달.

**정량 gap**

target 실패; SQL price는 사용 불가.

**분석 오류 또는 제한**

earnings·multiple 두 가정을 하나로 묶었다.

**재사용 교훈**

target 기여도를 FCF와 multiple로 나눈다.

### C4. diversification이 Air Canada 의존도를 낮춤 — 실패

**원문 주장**

Nectar·Carlson·new coalitions가 Canada concentration을 상쇄한다.

**경제적 메커니즘**

지역·partner를 늘려 single-node risk를 줄인다.

**T0 근거**

국제 assets와 JV pipeline.

**숨은 가정**

새 프로그램이 독립적으로 cash·member utility를 만든다.

**사전 반증조건**

Air Canada 이탈이 group value를 크게 훼손하면 반증.

**실제 결과**

2017 non-renewal이 equity와 전략을 재편했다.

**정량 gap**

anchor loss가 diversification을 압도.

**분석 오류 또는 제한**

revenue share와 network criticality를 혼동했다.

**재사용 교훈**

partner concentration은 매출뿐 아니라 network removal test로 잰다.

### C5. partner contract risk manageable — 부분 실패

**원문 주장**

contract terms·reserve가 renewal risk를 감당한다.

**경제적 메커니즘**

장기 계약과 switching cost가 bargaining을 제한한다.

**T0 근거**

Air Canada 관계·카드 partners.

**숨은 가정**

anchor airline이 자체 program을 만들 유인이 낮다.

**사전 반증조건**

non-renewal 또는 economics 급격 재협상이면 반증.

**실제 결과**

Air Canada가 2020 이후 non-renewal·독자 program을 발표했다.

**정량 gap**

가장 중요한 tail이 현실화.

**분석 오류 또는 제한**

expiry date를 tail event로만 처리했다.

**재사용 교훈**

모든 critical contract에 expiry·renewal owner·outside option을 기록한다.

### C6. residual Aeroplan franchise value — 성공

**원문 주장**

worst case에도 member base·data·brand가 strategic value를 가진다.

**경제적 메커니즘**

airline·bank가 continuity를 위해 franchise를 산다.

**T0 근거**

large active member network.

**숨은 가정**

redemption liability보다 buyer value가 높다.

**사전 반증조건**

fire-sale 또는 negative equity면 반증.

**실제 결과**

consortium이 C$450m headline cash와 liabilities를 인수; 최종 cash 약 C$516m.

**정량 gap**

asset value는 존재하지만 original C$24 equity와 다름.

**분석 오류 또는 제한**

asset value와 whole-company value를 섞었다.

**재사용 교훈**

asset sale proceeds에서 liabilities·tax·holdco costs를 차감한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 C$1.60 FCF/share에 15배를 적용하면 C$24다. 하지만 FCF는 points issued와 redeemed의 timing, reserve release와 growth billings를 구분해야 한다. 경제적 부채를 차감한 owner earnings와 partner-renewal stress case에 서로 다른 multiple을 적용해야 했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | Air Canada·card partner 이탈 | network break·asset sale | 2017~19 현실화 |
| Base | C$1.60 FCF·15x | C$24 by 2013 | 실패 |
| Bull | Nectar·analytics·new coalitions | diversified compounder | 부분·anchor 미상쇄 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Normalized FCF | C$205m/C$1.25 | 2013 C$1.60 | 초기 cash 유지·exact 제한 | 부분 |
| Breakage | 21% | stable spread | anchor contract가 더 중요 | 프레임 부족 |
| Target | C$24 by 2013 | ~2x | 미달 | 실패 |
| Air Canada contract | 2020 expiry | renew/manage | 2017 non-renewal | 실패 |
| Aeroplan sale | 미가정 | residual value | C$450m headline/~C$516m final cash | asset value 성공 |

### 촉매와 시간

판정 horizon은 **2013**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2011-09-15 | VIC Long 게시 | C$1.60 FCF·C$24 |
| 2011-10 | Aimia brand 전환 | international diversification |
| 2013-12-31 | target horizon 종료 | C$24 미달 |
| 2016-03 | Air Canada 자료가 2020 expiry 명시 | renewal clock |
| 2017-05-11 | Air Canada non-renewal | decisive thesis break |
| 2018-07-25 | consortium proposal | strategic residual value |
| 2018-11-26 | definitive agreement | C$450m headline |
| 2019-01-10 | sale completion | asset monetized·holdco 전환 |

### 실제 사업·자본구조 추이

초기 cash generation과 diversification은 일부 진전됐으나 2017-05-11 Air Canada가 2020 뒤 독자 loyalty plan을 발표했다. anchor risk가 현실화되자 Air Canada·TD·CIBC·Visa consortium이 Aeroplan을 다시 인수했고 2019 거래가 끝났다. Aimia는 핵심 loyalty asset을 판 뒤 investment holding company로 변했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

uploaded SQL의 AER 1~5년 price rows는 NYSE AerCap과 ticker collision이므로 전부 rejected다. Canadian AER/AIM의 corporate action·dividend series를 독립 복원하지 않아 exact return을 주장하지 않는다. 공개 역사 cross-check상 C$24 target는 달성하지 못한 것으로 판정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | loyalty model은 capital-light/high-FCF | 20% | 성공 | 경제적 부채 조정 후 FCF는 headline보다 낮을 수 있음. |
| C2 | 2013 FCF C$1.60/share | 18% | 부분 성공 | point estimate 완전 검증 제한. |
| C3 | C$24 by 2013 | 18% | 실패 | target 실패; SQL price는 사용 불가. |
| C4 | diversification이 Air Canada 의존도를 낮춤 | 16% | 실패 | anchor loss가 diversification을 압도. |
| C5 | partner contract risk manageable | 16% | 부분 실패 | 가장 중요한 tail이 현실화. |
| C6 | residual Aeroplan franchise value | 12% | 성공 | asset value는 존재하지만 original C$24 equity와 다름. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

초기 가치는 float와 redemption economics가 만들었지만 장기 손실·discount는 Air Canada라는 anchor node의 계약권력, card-partner bargaining과 asset sale 이후 holdco discount가 만들었다.

### Counterfactual

Air Canada와 top card issuer가 동시에 이탈해 gross billings가 40% 감소해도 redemption liability·reserve 차감 후 common에 얼마가 남는가?

---

## 9. 분석 오류 유형과 최초 경고

gross billings diversification과 network resiliency를 혼동하고, 계약 expiry·anchor topology를 breakage·reserve보다 낮은 우선순위로 뒀다.

### 최초로 관찰 가능했던 경고신호

2017-05-11 Air Canada non-renewal 발표가 가장 명확한 thesis break였지만 계약 종료시점은 2020으로 T0에도 갱신 risk를 stress할 수 있었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

network business는 member 수보다 제거했을 때 network가 무너지는 anchor node를 찾는다.

### Lesson 2

loyalty FCF는 points liability·reserve·billings growth를 조정해 owner earnings로 본다.

### Lesson 3

ticker가 같아도 exchange·법인·통화를 확인하기 전 성과를 붙이지 않는다.

### 지금 같은 아이디어를 다시 본다면

- gross billings by partner
- contract expiry·renewal right
- active members
- issuance/redemption ratio
- cost per mile
- breakage sensitivity
- reserve adequacy
- entity·exchange audit

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business economics | 단기 성공 |
| Valuation thesis | 실패 |
| Diversification | 실패 |
| Timing / path | C$24 미달 |
| Data quality | SQL return 무효 |
| Thesis score | 6.7/10 |
| Process score | 9.7/10 |
| 종합 | **혼합 — 현금엔진은 유효, C$24 실패·anchor-partner tail 현실화** |

### 한 문장 교훈

> network business는 member 수보다 제거했을 때 network가 무너지는 anchor node를 찾는다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/GROUPE_AEROPLAN_INC/2133679371) — Value Investors Club / source SQL, 2011-09-15. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [Air Canada 2013 financial statements](https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/en/quarterly-result/2013/2013_FSN_q4.pdf) — Air Canada, 2014-02. Aeroplan points purchase·redemption 관계 검증.
3. [Air Canada investor presentation](https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/speeches-presentations/en/Desjardins-Industrials-Telecom-Consumer-Conference-Montreal-en.pdf) — Air Canada, 2016-03. Aeroplan 계약의 2020 종료시점이 T0부터 계약문서에 존재했음을 검증.
4. [Aimia definitive Aeroplan sale agreement](https://www.aimia.com/aimia-and-air-canada-enter-into-definitive-agreement-for-purchase-of-aeroplan-loyalty-business/) — Aimia, 2018-11-26. C$450m headline cash와 거래구조 검증.
5. [Air Canada Q3 2018 financial statements](https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/en/quarterly-result/2018/2018_FSN_q3.pdf) — Air Canada, 2018-10-31. C$450m 현금·약 C$1.9bn points liability 인수조건 검증.
6. [Air Canada acquisition proposal](https://www.td.com/ca/en/about-td/for-investors/investor-relations/news-and-events/news/2018/proposal-by-air-canada-td-cibc-and-visa-to-acquire-aeroplan) — TD / Air Canada consortium, 2018-07-25. anchor partners가 Aeroplan을 공동 인수하려 한 구조 검증.
7. [SEC entity check: NYSE AER](https://www.sec.gov/edgar/browse/?CIK=1378789&owner=exclude) — SEC, 2026. 미국 AER은 AerCap이며 Canadian AER/AIM과 가격 혼용 금지.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **REJECTED** — ticker collision으로 wrong-company 가격행을 폐기했다.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
