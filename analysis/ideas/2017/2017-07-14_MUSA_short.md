# Murphy USA Inc. — 2017-07-14 — V9

> **Batch 049 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Short**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Murphy USA Inc. / MUSA |
| Idea ID | `c03d8a90-48ef-40a1-9806-53f7c66b55a1` |
| 게시일 / 작성자 | 2017-07-14 / jbur |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Short** |
| 기준가격 | $71.99 next-day close |
| 원 horizon | 12~24개월 |
| 최종 판정 | **실패 — 1개월 +6.0% 후 1년 -9.2%, 5년 -265.9% simple short P&L** |

> **결론:** raw와 실제 모두 Short다. 동일점 gallons 감소, RIN 정상화, 새점포·R&R capex의 낮은 incremental return과 buyback 부담을 묶어 EBITDA·multiple 압축을 기대했다. 문제는 gallons 감소를 total fuel contribution 감소로 직결하고, 경쟁자의 pump-pricing behavior와 MUSA의 low-cost supply advantage를 충분히 모델링하지 않은 점이다. 결과적으로 **실패 — 1개월 +6.0% 후 1년 -9.2%, 5년 -265.9% simple short P&L**.

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

raw와 실제 모두 Short다. 동일점 gallons 감소, RIN 정상화, 새점포·R&R capex의 낮은 incremental return과 buyback 부담을 묶어 EBITDA·multiple 압축을 기대했다. 문제는 gallons 감소를 total fuel contribution 감소로 직결하고, 경쟁자의 pump-pricing behavior와 MUSA의 low-cost supply advantage를 충분히 모델링하지 않은 점이다.

### Reverse expectations

$71.99 next-day close가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. same-store gallons decline — 20%

- **원문 주장:** traffic와 fuel volume이 구조적으로 감소한다.
- **T0 근거:** 2017 APSM 약세와 Walmart 관계 변화
- **숨은 가정:** volume 감소가 contribution dollars 감소로 이어진다.
- **사전 반증조건:** CPG 상승이 volume decline을 상쇄하면 economic claim 반증.
- **실제:** 2017 volume은 약 -5.3%였다.
- **판정:** **수치 성공**
- **재사용 교훈:** 수요량과 profit pool을 분리한다.

### C2. volume to EBITDA — 18%

- **원문 주장:** gallons 감소가 EBITDA를 압박한다.
- **T0 근거:** fuel이 핵심 profit source
- **숨은 가정:** industry pricing이 고정돼 있다.
- **사전 반증조건:** total fuel contribution dollars가 증가하면 반증.
- **실제:** 16.4 cpg로 단가가 상승했다.
- **판정:** **실패**
- **재사용 교훈:** volume×unit margin bridge 없이는 earnings claim이 아니다.

### C3. RIN normalization — 18%

- **원문 주장:** RIN 가격 하락이 PS&W profit을 줄인다.
- **T0 근거:** renewable credit volatility
- **숨은 가정:** retail margin이 동시에 보완하지 않는다.
- **사전 반증조건:** retail CPG가 올라 total contribution을 지키면 반증.
- **실제:** 전체 fuel contribution은 견고했다.
- **판정:** **부분 실패**
- **재사용 교훈:** RIN과 retail CPG를 별도 factor로 stress한다.

### C4. capex burden — 16%

- **원문 주장:** R&R·신점은 EBITDA를 만들지 못하는 maintenance다.
- **T0 근거:** 높은 연간 capex와 kiosk 노후화
- **숨은 가정:** cohort ROIC가 자본비용 아래다.
- **사전 반증조건:** 신점/R&R contribution과 store count가 증가하면 반증.
- **실제:** 점포·merchandise 플랫폼이 확대됐다.
- **판정:** **실패**
- **재사용 교훈:** capex는 vintage별 maintenance/growth로 나눈다.

### C5. buyback constraint — 16%

- **원문 주장:** leverage 때문에 repurchase가 멈춘다.
- **T0 근거:** capex와 debt service competing uses
- **숨은 가정:** FCF가 부족하고 board가 보수화한다.
- **사전 반증조건:** share count가 계속 줄면 반증.
- **실제:** Q4와 이후 repurchase가 지속됐다.
- **판정:** **실패**
- **재사용 교훈:** Short는 buyback capacity와 평균가격을 추적한다.

### C6. multiple compression — 12%

- **원문 주장:** CASY 대비 열위가 de-rate를 만든다.
- **T0 근거:** 작은 format·tobacco mix
- **숨은 가정:** earning power가 정체된다.
- **사전 반증조건:** owner earnings/share 증가면 반증.
- **실제:** 주가는 5년 3.66x가 됐다.
- **판정:** **강한 실패**
- **재사용 교훈:** quality discount가 per-share compounding을 이기나 본다.

---

## 4. 당시 Valuation과 Payoff Structure

Short payoff는 volume 하락 × cpg 정상화로 EBITDA가 낮아지고, 동시에 multiple도 압축되는 구조였다. 이중 하락을 쓰려면 gallons, retail margin, PS&W/RIN을 분리해 total fuel contribution dollars를 만들어야 한다. buyback은 leverage를 높이는 위험인 동시에 낮은 가격에서는 per-share value를 높여 short의 float와 earnings denominator를 줄인다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Short 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 실패 — 1개월 +6.0% 후 1년 -9.2%, 5년 -265.9% simple short P&L의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / payoff | $71.99 | 지속 하락 | 1M +6.0%·5Y -265.9% Short | 실패 |
| APSM gallons | 감소 예상 | 구조적 하락 | 2017 약 -5.3% | 성공 |
| Total fuel contribution | 15.4 cpg 2016 | 압축 | 16.4 cpg 2017 | 실패 |
| Buyback | 현금·leverage 부담 | 중단/감소 | Q4 약 $54m·이후 지속 | 실패 |
| Long-term CPG | mean reversion | 낮은 teens | 2025 30.7 cpg | 강한 실패 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2017-07-14 | VIC Short | volume·RIN·capex thesis |
| 2017-Q4 | 약 $54m repurchase | float shrink 지속 |
| 2017-FY | APSM gallons 약 -5.3%, total fuel contribution 16.4 cpg | 핵심 divergence |
| 2018-FY | fuel contribution 16.2 cpg·merchandise 개선 | EBITDA resilience |
| 2020 | COVID gallons 급락·CPG 급등 | volume-to-profit 반증 |
| 2021-01 | QuickChek 인수 | merchandise capability |
| 2022-07 | 5년 multiplier 약 3.66x | simple Short -265.9% |
| 2025 | 30.7 cpg·1,800 stores | terminal lesson |

### 실제 사업·자본구조

2017 APSM fuel volume은 약 -5.3%로 volume call은 맞았지만 total fuel contribution은 16.4 cpg로 2016 15.4 cpg를 웃돌았다. 2018 full-year fuel contribution도 16.2 cpg였고 merchandise contribution은 늘었다. 회사는 2017 Q4에도 약 $54m을 평균 약 $76에 매입했고 이후 R&R·신점·QuickChek와 buyback을 지속했다. 2025 total fuel contribution은 30.7 cpg였다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

실제 Short로 교정한 simple price P&L은 1M +6.0%, 3M +0.6%, 6M -17.7%, 1Y -9.2%, 2Y -16.5%, 3Y -54.6%, 5Y -265.9%다. 1-multiplier 방식이라 borrow·배당·margin call을 제외하며 손실이 -100% 아래로 갈 수 있다. 첫 달의 이익을 장기 thesis 성공으로 오인하면 안 된다.

이 아이디어는 repository에 보존된 price multiplier를 실제 Short 방향으로 교정했다. Long은 multiplier-1, Short는 1-multiplier인 price-only 수익이며 배당·borrow·거래비용은 포함하지 않는다. 누락 horizon은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | same-store gallons decline | 20% | 수치 성공 | 수요량과 profit pool을 분리한다. |
| C2 | volume to EBITDA | 18% | 실패 | volume×unit margin bridge 없이는 earnings claim이 아니다. |
| C3 | RIN normalization | 18% | 부분 실패 | RIN과 retail CPG를 별도 factor로 stress한다. |
| C4 | capex burden | 16% | 실패 | capex는 vintage별 maintenance/growth로 나눈다. |
| C5 | buyback constraint | 16% | 실패 | Short는 buyback capacity와 평균가격을 추적한다. |
| C6 | multiple compression | 12% | 강한 실패 | quality discount가 per-share compounding을 이기나 본다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

초기 이익은 weak gallons와 sentiment에서 나왔지만 장기 손실은 CPG 상승, 상품 mix, low-cost network, buyback의 share shrink가 만들었다. volume call이 맞아도 profit pool의 단가와 자본배분이 반대로 움직이면 equity Short는 실패한다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 $71.99 next-day close에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

gallons와 EBITDA 사이에 CPG response function을 두지 않았고 RIN과 retail margin을 같은 mean-reversion bucket으로 묶었다. capex를 전액 maintenance처럼 봤으며 repurchase를 단순 현금유출로 처리해 분모 감소를 누락했다. 사업 악화와 overvaluation을 분리한 cover rule도 부족했다.

### 최초 관찰 가능한 경고/반증

2017 실적에서 gallons가 줄었는데 total fuel contribution이 16.4 cpg로 상승한 것이 최초 핵심 반증이다. 그 시점부터 volume-only Short를 중단하고 fuel contribution dollars와 owner earnings/share를 재산정했어야 했다.

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
| Valuation thesis | 실패 |
| Catalyst / timing | 실패 — 1개월 +6.0% 후 1년 -9.2%, 5년 -265.9% simple short P&L |
| Thesis score | 4.0/10 |
| Process score | 7.0/10 |
| Outcome-adjusted score | 5.5/10 |

### 한 문장 교훈

> 수요량과 profit pool을 분리한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL 원문/metadata — VIC_IDEAS(4).sql / VIC, 2017-07-14. idea_id·raw direction·description 14729 chars·catalyst 93 chars
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
