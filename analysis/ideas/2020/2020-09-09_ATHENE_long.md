# Athene Holding Ltd. — 2020-09-09 — V9

> **Batch 046 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-09.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Athene Holding Ltd. / ATH |
| Idea ID | `2cac07f8-87d1-484e-87b4-ab3523aa44da` |
| 게시일 / 작성자 | 2020-09-09 / Jumpman23 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격 | 약 $34 |
| 원 horizon | 2~5년 |
| 최종 판정 | **Apollo 합병으로 매우 성공한 event-plus-compounder Long** |

> **결론:** raw Short지만 실제는 Long이다. 2018년 $49 추천가보다 거의 30% 낮은 약 $34, 0.7x P/B·5.2x FY19 P/E에서 pandemic credit loss가 과도하게 반영됐다고 봤다. Apollo 거래로 $1bn excess capital, ACRA의 $4bn 목표와 약 $10bn buying power, 높아진 new-money yield와 Jackson reinsurance를 성장엔진으로 제시했다. 결과적으로 **Apollo 합병으로 매우 성공한 event-plus-compounder Long**.

---

## 1. 회사는 정확히 무엇을 하는가

Athene은 retail annuity·institutional reinsurance로 장기 보험부채를 조달하고 fixed income·structured credit·private assets에 투자해 spread를 번다. 현금엔진은 `투자수익률 - 계약자 crediting/hedging cost - DAC amortization - 운영비 - 실현 신용손실 - 세금·자본비용`이다. Apollo는 origination과 자산운용을 제공하지만 약 40bp의 fee와 관련자 거래·governance 문제도 만든다. P/B나 P/E만 볼 수 없고, asset/liability duration, surrender behavior, ratings·RBC, AOCI와 economic credit loss, excess capital, buyback·reinsurance economics를 연결해야 한다.

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

raw Short지만 실제는 Long이다. 2018년 $49 추천가보다 거의 30% 낮은 약 $34, 0.7x P/B·5.2x FY19 P/E에서 pandemic credit loss가 과도하게 반영됐다고 봤다. Apollo 거래로 $1bn excess capital, ACRA의 $4bn 목표와 약 $10bn buying power, 높아진 new-money yield와 Jackson reinsurance를 성장엔진으로 제시했다.

### Reverse expectations

약 $34가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. credit loss 과대반영 — 20%

- **원문 주장:** modeled OTTI $1~2bn 전에도 연 earnings $1bn+다.
- **T0 근거:** Q2 OTTI <2bp
- **숨은 가정:** migration이 realized loss로 급증하지 않는다.
- **사전 반증조건:** 누적 loss가 capital buffer 초과면 반증.
- **실제:** portfolio와 capital이 stress를 견뎠다.
- **판정:** **성공**
- **재사용 교훈:** mark·migration·realized loss를 분리한다.

### C2. 0.7x book rerating — 18%

- **원문 주장:** 1.0x만 가도 +40%다.
- **T0 근거:** low P/B·5.2x P/E
- **숨은 가정:** adjusted book이 경제적이다.
- **사전 반증조건:** capital raise·reserve charge면 book haircut.
- **실제:** Apollo 거래로 discount가 닫혔다.
- **판정:** **성공**
- **재사용 교훈:** book target에 terminal buyer 확률을 따로 둔다.

### C3. $10bn buying power — 18%

- **원문 주장:** Apollo/ACRA 구조가 crisis assets를 산다.
- **T0 근거:** $1bn excess·$4bn ACRA target
- **숨은 가정:** third-party capital과 ratings headroom 가용.
- **사전 반증조건:** 자본이 defensive use로 묶이면 반증.
- **실제:** 대형 reinsurance와 deployment가 이어졌다.
- **판정:** **성공**
- **재사용 교훈:** gross capacity를 equity economics로 환산한다.

### C4. new-money ROA +40bp — 16%

- **원문 주장:** spread widening이 미래 earnings를 높인다.
- **T0 근거:** crisis reinvestment yield
- **숨은 가정:** liability cost는 느리게 상승한다.
- **사전 반증조건:** credit loss가 spread pickup 초과면 반증.
- **실제:** 후속 earnings/strategic value를 지지했다.
- **판정:** **성공**
- **재사용 교훈:** spread pickup은 loss-adjusted로 본다.

### C5. organic franchise — 16%

- **원문 주장:** retail sales +44% QoQ·record $7bn volume다.
- **T0 근거:** industry -4% 대비 share gain
- **숨은 가정:** 27% return estimate가 실제 cash ROE다.
- **사전 반증조건:** commission·pricing 후 IRR 하락이면 반증.
- **실제:** franchise가 거래가치를 만들었다.
- **판정:** **성공**
- **재사용 교훈:** sales growth와 cohort IRR을 같이 본다.

### C6. 몇 년 내 double — 12%

- **원문 주장:** BVPS compound와 multiple 회복으로 +100%다.
- **T0 근거:** 0.7x start·mid-teens ROE
- **숨은 가정:** deal/repurchase가 per-share value를 보존.
- **사전 반증조건:** unfavorable exchange·APO de-rate면 반증.
- **실제:** 합병은 방향을 지지했으나 exact return 미복원.
- **판정:** **방향 성공**
- **재사용 교훈:** corporate action 뒤 successor security까지 잇는다.

---

## 4. 당시 Valuation과 Payoff Structure

0.7x book에서 1.0x만 받아도 약 40% upside다. FY19 P/E 5.2x라 credit shock 한 해를 흡수해도 earnings yield가 높다. 원문은 몇 년 내 +100% 가능성도 제시했지만, 이는 BVPS compound·capital deployment·multiple 회복이 모두 필요하다. ACRA third-party capital은 gross liabilities가 아니라 Athene equity와 fee/share 귀속으로 환산해야 한다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | Apollo 합병으로 매우 성공한 event-plus-compounder Long의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| P/B | 0.7x | 1.0x | 합병으로 discount 해소 | 성공 |
| FY19 P/E | 5.2x | 정상화 | terminal strategic value | 성공 |
| Excess capital | $1bn+ | deployment | ACRA/Jackson 확대 | 성공 |
| New investment ROA | +40bp | earnings 개선 | crisis deployment | 방향 성공 |
| Retail organic volume | 약 $7bn·27% return | 성장 | franchise 견조 | 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2018-09 | 선행 Long $49 | valuation anchor |
| 2020-03 | COVID shock | credit fear |
| 2020-Q2 | OTTI <2bp | loss test |
| 2020-09-09 | VIC Long | 약 $34·0.7x book |
| 2020 | Jackson $27bn reinsurance | deployment |
| 2021-03 | Apollo merger 발표 | exchange 1.149 APO |
| 2022-01-03 | 거래 종결 | standalone ATH 종료 |

### 실제 사업·자본구조

Athene은 portfolio stress를 견뎠고 2021년 Apollo와 전액주식 합병에 합의했다. Athene 주주는 1주당 APO 1.149주를 받는 구조였고 2022-01-03 거래가 종결됐다. 0.7x book에서 산 standalone discount와 Apollo strategic value가 짧은 기간에 함께 실현돼 방향·catalyst 모두 성공이다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

SQL performance row가 없다. 2018 $49 대비 거의 30% 낮다는 원문에서 약 $34를 anchor로만 사용한다. 교환비율 이후 APO 가격·배당을 포함한 exact return은 산출하지 않아 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | credit loss 과대반영 | 20% | 성공 | mark·migration·realized loss를 분리한다. |
| C2 | 0.7x book rerating | 18% | 성공 | book target에 terminal buyer 확률을 따로 둔다. |
| C3 | $10bn buying power | 18% | 성공 | gross capacity를 equity economics로 환산한다. |
| C4 | new-money ROA +40bp | 16% | 성공 | spread pickup은 loss-adjusted로 본다. |
| C5 | organic franchise | 16% | 성공 | sales growth와 cohort IRR을 같이 본다. |
| C6 | 몇 년 내 double | 12% | 방향 성공 | corporate action 뒤 successor security까지 잇는다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

credit loss가 feared level보다 낮고 자본이 보존된 상태에서 higher new-money spread·organic volume·reinsurance deployment가 book growth를 재가동했다. Apollo가 minority discount를 거래로 닫으면서 valuation catalyst까지 발생했다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 약 $34에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

COVID 이후 spread widening과 capital deployment를 강하게 봤지만 downgrade migration·liquidity·policyholder behavior의 nonlinear tail은 얕았다. Jackson 등 대형 block의 reserve/hedge assumption과 third-party share도 별도 haircut해야 했다.

### 최초 관찰 가능한 경고/반증

quarterly OTTI가 원문 <2bp 수준을 벗어나 누적 $2bn stress를 초과하거나 excess capital $1bn이 ratings 방어에 묶이면 40% rerating thesis를 낮춰야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `ATH`를 회사로 보지 말고 Athene Holding Ltd. 법인·exchange·날짜로 고정한다.
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
| Entity / direction | raw Short → **Long**, Athene Holding Ltd. |
| Business thesis | 성공 |
| Valuation thesis | 성공 |
| Catalyst / timing | Apollo 합병으로 매우 성공한 event-plus-compounder Long |
| Thesis score | 9.2/10 |
| Process score | 9.0/10 |
| Outcome-adjusted score | 9.1/10 |

### 한 문장 교훈

> mark·migration·realized loss를 분리한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL 원문/metadata — VIC_IDEAS(4).sql / VIC, 2020-09-09. idea_id·raw direction·description 14757 chars·catalyst 34 chars
2. [Athene SEC filing archive](https://www.sec.gov/edgar/browse/?CIK=1527469&owner=exclude) — SEC / Athene, 2016-2022. book value·spread·capital·related-party disclosure
3. [Athene 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1527469/000152746921000018/ath-20201231.htm) — SEC / Athene, 2021-02-26. 2020 stress, portfolio, capital과 earnings bridge
4. [Apollo and Athene transaction close](https://ir.apollo.com/news-events/press-releases/detail/28/apollo-and-athene-announce-transaction-close) — Apollo, 2022-01-03. 전액주식 합병 종결과 standalone ATH의 terminal event

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=ATH, entity=Athene Holding Ltd., raw=Short, research=Long.
