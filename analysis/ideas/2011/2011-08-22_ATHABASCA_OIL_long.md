# Athabasca Oil Sands Corp. — 2011-08-22 — V9

> **Batch 046 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-09.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Athabasca Oil Sands Corp. / ATH |
| Idea ID | `a9e042a6-e212-41eb-b757-77e1c4aaf755` |
| 게시일 / 작성자 | 2011-08-22 / pathbska |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격 | C$12.02 |
| 원 horizon | 2~6년 |
| 최종 판정 | **put 가치 실현, long-duration NAV·equity rerating은 혼합** |

> **결론:** raw Short지만 본문은 명백한 Long이다. C$12.02에서 PetroChina put과 net cash를 합친 hard cash C$7.50대가 하방을 막고, 7.5bn bbl 잔여 oil-sands를 JV 거래의 C$0.80/bbl에 평가하면 C$20~22가 된다고 봤다. 70% upside/30% downside를 섞은 기대값은 C$17.81, 약 +48%였다. 결과적으로 **put 가치 실현, long-duration NAV·equity rerating은 혼합**.

---

## 1. 회사는 정확히 무엇을 하는가

Athabasca Oil은 Alberta의 oil sands와 Duvernay·Montney 같은 light-oil 자산을 개발한다. 당시 현금엔진은 생산현금흐름보다 `보유 현금 + JV/put 수취액 + 위험조정된 매장량 가치 - 남은 개발 capex - 시간·허가·commodity discount - corporate cost`에 가까웠다. 즉 지하자원 NAV는 곧바로 equity value가 아니다. first steam, ramp, steam-oil ratio, well cost, 승인, 원유가격·차등, pipeline, partner funding과 희석을 모두 거쳐야 한다. 장기 프로젝트의 시간은 회계상 부채가 적어도 경제적 레버리지로 작동한다.

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

raw Short지만 본문은 명백한 Long이다. C$12.02에서 PetroChina put과 net cash를 합친 hard cash C$7.50대가 하방을 막고, 7.5bn bbl 잔여 oil-sands를 JV 거래의 C$0.80/bbl에 평가하면 C$20~22가 된다고 봤다. 70% upside/30% downside를 섞은 기대값은 C$17.81, 약 +48%였다.

### Reverse expectations

C$12.02가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. C$7.54 cash floor — 20%

- **원문 주장:** put+net cash가 하방이다.
- **T0 근거:** C$1.1bn net cash·잔여 put
- **숨은 가정:** 계약이 집행되고 cash가 보존된다.
- **사전 반증조건:** 승인 지연·cash burn·재투자면 반증.
- **실제:** put은 실현됐지만 cash는 영구 floor가 아니었다.
- **판정:** **부분 성공**
- **재사용 교훈:** cash floor에는 time-to-cash와 use-of-cash를 붙인다.

### C2. C$20~22 resource value — 18%

- **원문 주장:** JV C$0.80/bbl을 잔여 7.5bn에 적용한다.
- **T0 근거:** PetroChina precedent
- **숨은 가정:** 질·승인·인프라가 유사하다.
- **사전 반증조건:** pilot 실패·capex 상승이면 multiple 제거.
- **실제:** long-duration·technology discount가 지속됐다.
- **판정:** **부분/과대**
- **재사용 교훈:** precedent는 barrel quality와 funding을 맞춘다.

### C3. 70/30 expected value — 18%

- **원문 주장:** EV C$17.81로 +48%다.
- **T0 근거:** C$21.44/C$9.35 시나리오
- **숨은 가정:** 두 상태가 주요 결과를 포괄한다.
- **사전 반증조건:** 중간 희석·oil crash 상태가 크면 반증.
- **실제:** 중간 경로와 macro tail이 컸다.
- **판정:** **불완전**
- **재사용 교훈:** 확률표에는 financing·commodity state를 추가한다.

### C4. PetroChina 지급 — 16%

- **원문 주장:** major가 계약을 이행한다.
- **T0 근거:** 기존 60% 거래
- **숨은 가정:** 정치·규제와 funding barrier가 없다.
- **사전 반증조건:** put 조건 재협상·장기소송이면 반증.
- **실제:** 거래 현금화로 핵심 전제는 맞았다.
- **판정:** **성공**
- **재사용 교훈:** counterparty와 condition precedent를 분리한다.

### C5. light oil이 idle cash를 번다 — 16%

- **원문 주장:** 단기 cycle 자산이 burn을 상쇄한다.
- **T0 근거:** quick-return wells
- **숨은 가정:** well economics가 oil-price 하락에도 견딘다.
- **사전 반증조건:** FCF 음수·capex 확대면 반증.
- **실제:** commodity beta를 없애지 못했다.
- **판정:** **혼합**
- **재사용 교훈:** bridge asset도 full-cycle breakeven으로 본다.

### C6. market turmoil이 원인 — 12%

- **원문 주장:** zero-revenue duration 할인은 일시적이다.
- **T0 근거:** 2011 risk-off
- **숨은 가정:** 할인율만 정상화되고 fundamentals는 유지된다.
- **사전 반증조건:** project delay·oil 하락이면 구조 문제.
- **실제:** 후속 위험은 단순 sentiment 이상이었다.
- **판정:** **부분 실패**
- **재사용 교훈:** macro discount와 project impairment를 분해한다.

---

## 4. 당시 Valuation과 Payoff Structure

Hard cash C$7.54, 보수적 downside C$9.35, upside C$21.44를 사용했다. 원문의 probability-weighted value는 `70%×21.44 + 30%×9.35 = C$17.81`이다. 하지만 put의 세금·closing 조건, 개발 burn과 2014/2017 production duration을 분리하지 않으면 cash floor가 시간에 따라 줄어든다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | put 가치 실현, long-duration NAV·equity rerating은 혼합의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | C$12.02 | EV C$17.81 | SQL 성과 없음 | 미검증 |
| Hard cash | C$7.54 | 하방 floor | put 수취 후 재투자 | 부분 성공 |
| Upside | C$21.44 | 70% 확률 | 정확 가격경로 없음 | 미검증 |
| 잔여 resource | 7.5bn bbl | C$0.80/bbl | 기술·capex 할인 지속 | 과대 가능 |
| 생산 timing | 2014/2017 | ramp | 긴 duration 현실화 | 혼합 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2009-08 | PetroChina JV | 60%에 C$1.9bn |
| 2010-04 | C$1.35bn IPO | 자본확보 |
| 2011-08-22 | VIC Long | C$12.02 |
| 2014 | first oil 목표 | duration 시작 |
| 2014 | Dover put 진행 | cash catalyst 현실화 |
| 2014-2016 | oil-price 충격 | NAV discount 확대 |
| 2017+ | serious production 가정 | 원 horizon 장기화 |

### 실제 사업·자본구조

PetroChina 관련 put 거래는 후속 규제·settlement를 거쳐 결국 현금화되어 핵심 asset-monetization 논리는 맞았다. 반면 zero-revenue land bank의 장기 생산·commodity duration은 원문이 인정한 것보다 훨씬 큰 변동성을 만들었고 이후 oil-price 하락은 NAV rerating을 훼손했다. event 성공과 C$20~22 equity 성공은 같은 판정이 아니다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

SQL performance row가 없어 exact return은 null이다. 원문 C$12.02, downside C$9.35, EV C$17.81, upside C$21.44만 T0 anchor로 사용한다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | C$7.54 cash floor | 20% | 부분 성공 | cash floor에는 time-to-cash와 use-of-cash를 붙인다. |
| C2 | C$20~22 resource value | 18% | 부분/과대 | precedent는 barrel quality와 funding을 맞춘다. |
| C3 | 70/30 expected value | 18% | 불완전 | 확률표에는 financing·commodity state를 추가한다. |
| C4 | PetroChina 지급 | 16% | 성공 | counterparty와 condition precedent를 분리한다. |
| C5 | light oil이 idle cash를 번다 | 16% | 혼합 | bridge asset도 full-cycle breakeven으로 본다. |
| C6 | market turmoil이 원인 | 12% | 부분 실패 | macro discount와 project impairment를 분해한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

가치의 첫 driver는 원유가격이 아니라 계약상 put과 대형 파트너의 지급능력이었다. 이후 equity는 capex burn·승인·기술·oil beta에 다시 노출됐다. 즉 cash floor는 closing 전 event claim이고, closing 뒤에는 capital-allocation claim으로 변한다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 C$12.02에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

현금을 'hard downside'로 부르면서 수령시점·세금·잔여 capex·경영진 재투자를 충분히 haircut하지 않았다. carbonate 2.9bn bbl의 상업성 검증 전 resource multiple을 적용한 것도 큰 model risk다.

### 최초 관찰 가능한 경고/반증

put 승인 지연으로 수령시점이 한 해 이상 밀리거나 annual cash burn이 C$7.54 floor의 15~20%를 소진하면 downside와 확률을 즉시 재산정해야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `ATH`를 회사로 보지 말고 Athabasca Oil Sands Corp. 법인·exchange·날짜로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Long을 확정한다.
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
| Entity / direction | raw Short → **Long**, Athabasca Oil Sands Corp. |
| Business thesis | 부분/과대 |
| Valuation thesis | 미검증 |
| Catalyst / timing | put 가치 실현, long-duration NAV·equity rerating은 혼합 |
| Thesis score | 7.0/10 |
| Process score | 7.5/10 |
| Outcome-adjusted score | 7.2/10 |

### 한 문장 교훈

> cash floor에는 time-to-cash와 use-of-cash를 붙인다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/ATHABASCA_OIL_SANDS_CORP/7591076608) — VIC_IDEAS(4).sql / VIC, 2011-08-22. idea_id·raw direction·description 7142 chars·catalyst 72 chars
2. [Athabasca investor reports](https://www.athabascaoil.com/investors/financial-reports/) — Athabasca Oil, 2011-2025. Dover 현금·Hangingstone·light-oil 자본배분의 후속 검증
3. [Athabasca corporate presentation archive](https://www.athabascaoil.com/investors/presentations-events/) — Athabasca Oil, 2011-2025. project 규모·production ramp·자본계획
4. [Alberta Energy Regulator](https://www.aer.ca/) — AER, 2013-2014. Dover 승인과 규제경로의 1차 기관

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=ATH, entity=Athabasca Oil Sands Corp., raw=Short, research=Long.
