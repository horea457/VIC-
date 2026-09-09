# Anthem, Inc. — 2002-01-18 — V9

> **Batch 046 canonical report.** Raw SQL `Long`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-09.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Anthem, Inc. / ATH |
| Idea ID | `4510e63f-516d-422c-ad0f-976c01c76690` |
| 게시일 / 작성자 | 2002-01-18 / abra399 |
| 원 SQL 방향 | Long |
| 원문 검증 방향 | **Long** |
| 기준가격 | $51 |
| 원 horizon | 12~24개월 |
| 최종 판정 | **사업·전략 종착점 성공, SQL 가격성과는 미검증** |

> **결론:** 2001년 10월 demutualization IPO 뒤 $36에서 $51로 올랐지만, 8개 주 800만 가입자의 Anthem은 여전히 2002 EPS 14배로 Trigon 15배·WellPoint 18배보다 쌌다. 상호회사 시절 4% 미만이던 margin을 peer 5%로 끌어올리면 EPS $4.50+, 16배 적용 시 $70+라는 Long이다. raw와 실제 방향은 모두 Long이다. 결과적으로 **사업·전략 종착점 성공, SQL 가격성과는 미검증**.

---

## 1. 회사는 정확히 무엇을 하는가

Anthem은 지역 Blue Cross Blue Shield 면허 아래 고용주·개인·정부 가입자에게 건강보험을 제공한다. 경제엔진은 `가입자 수 × 보험료 - 의료비 - 판매·관리비 - 세금·필요자본비용`이다. 가장 중요한 수치는 매출보다 medical loss ratio(MLR), 보험료 갱신률, 가입자 mix, SG&A ratio, 준비금 적정성과 인수 통합비다. 보험료는 매년 다시 가격을 붙일 수 있지만 의료비 추세를 뒤늦게 따라가면 한 해의 손해가 먼저 발생한다. 따라서 margin expansion은 단순 비용절감이 아니라 pricing lag, 의료이용량, network discount와 규제 승인을 함께 통과해야 common equity로 귀속된다.

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

2001년 10월 demutualization IPO 뒤 $36에서 $51로 올랐지만, 8개 주 800만 가입자의 Anthem은 여전히 2002 EPS 14배로 Trigon 15배·WellPoint 18배보다 쌌다. 상호회사 시절 4% 미만이던 margin을 peer 5%로 끌어올리면 EPS $4.50+, 16배 적용 시 $70+라는 Long이다. raw와 실제 방향은 모두 Long이다.

### Reverse expectations

$51가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. peer multiple discount — 20%

- **원문 주장:** 14x를 16x로 정상화하면 $58다.
- **T0 근거:** TGH 15x·WLP 18x
- **숨은 가정:** growth·reserve quality가 유사하다.
- **사전 반증조건:** MLR/성장 열위가 지속되면 discount 정당화.
- **실제:** 전국 scale과 merger option이 실현됐다.
- **판정:** **성공/수익 미검증**
- **재사용 교훈:** peer multiple은 margin·reserve 차이를 조정한다.

### C2. 100bp margin expansion — 18%

- **원문 주장:** <4%에서 5%면 EPS $4.50+다.
- **T0 근거:** mutual 시절 낮은 효율
- **숨은 가정:** pricing과 SG&A가 동시에 개선된다.
- **사전 반증조건:** 두 갱신주기 뒤 4% 미만이면 반증.
- **실제:** 장기 사업 확장은 방향을 지지했다.
- **판정:** **방향 성공**
- **재사용 교훈:** 보험 margin은 MLR와 SG&A로 나눈다.

### C3. 보험료 12% 인상 — 18%

- **원문 주장:** medical trend를 가격으로 상쇄한다.
- **T0 근거:** Q3 managed-care pricing +12%
- **숨은 가정:** 가입자 이탈 없이 갱신된다.
- **사전 반증조건:** MLR 상승·membership 감소 동시 발생.
- **실제:** scale franchise는 생존·확대했다.
- **판정:** **부분 검증**
- **재사용 교훈:** price와 retention을 함께 본다.

### C4. IPO 물량압력 해소 — 16%

- **원문 주장:** policyholder/flipper 매도가 일시적이다.
- **T0 근거:** $36→$51 뒤 변동성
- **숨은 가정:** 매도 종료 후 fundamental buyer가 유입된다.
- **사전 반증조건:** volume 소화 뒤에도 discount 지속.
- **실제:** 장기 rerating은 있었으나 timing 미복원.
- **판정:** **미검증**
- **재사용 교훈:** technical catalyst에는 날짜·거래량 조건을 둔다.

### C5. Kansas·과거 M&A 통합 — 16%

- **원문 주장:** 통합이 margin 개선을 돕는다.
- **T0 근거:** 1993~2002 다수 인수
- **숨은 가정:** systems·reserve 통합비가 제한적이다.
- **사전 반증조건:** 통합비와 reserve strengthening이 EPS 훼손.
- **실제:** WellPoint 대형 결합까지 진전했다.
- **판정:** **성공**
- **재사용 교훈:** serial M&A는 organic cohort와 분리한다.

### C6. national Blue option — 12%

- **원문 주장:** Anthem/WellPoint 경쟁이 전략가치를 높인다.
- **T0 근거:** 전국망 구축 경쟁
- **숨은 가정:** 과지불 없이 scale을 얻는다.
- **사전 반증조건:** 20x+ 인수·희석이면 반증.
- **실제:** 2004 두 회사가 결합했다.
- **판정:** **강한 성공**
- **재사용 교훈:** terminal event와 투자수익은 별도 기록한다.

---

## 4. 당시 Valuation과 Payoff Structure

Base는 2002 EPS $3.65×16=$58로 약 14% upside이고, 원문 표현상 당시 가격 대비 20% 이상을 기대했다. Bull은 margin 5%×EPS $4.50+×16=$70+다. 핵심은 2~3 multiple point discount와 약 100bp margin gap이 중복된 가치가 아니라 earnings와 multiple의 두 단계 bridge라는 점이다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 사업·전략 종착점 성공, SQL 가격성과는 미검증의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가입자 | 8m/8개 주 | Kansas+scale | WellPoint 결합으로 확대 | 성공 |
| 2002 EPS | $3.65E | 16x=$58 | SQL 성과 없음 | 미검증 |
| Operating margin | <4% | 5% | 장기 scale 개선 | 방향 성공 |
| MLR | 85% | peer 81~82% 접근 | 정확한 horizon 미복원 | 미검증 |
| Strategic event | standalone | national Blue network | 2004 WellPoint 결합 | 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2001-10 | demutualization IPO | $36 출발 |
| 2002-01-18 | VIC Long | $51·$58/$70+ |
| 2002 여름 | Kansas BCBS closing 예상 | scale catalyst |
| 2003-10 | WellPoint 결합 발표 | 전략 옵션 현실화 |
| 2004-11 | 규제 승인 | closing gate |
| 2004-12-01 | 합병 완료 | 사업 종착점 성공 |

### 실제 사업·자본구조

Anthem은 상장 보험사로서 가입자·수익기반을 키웠고 2004년 WellPoint Health Networks와 약 $16.5bn 규모 결합을 완료했다. 이는 전국 Blue 네트워크와 scale 논지를 확인하는 전략적 종착점이다. 다만 합병 사실만으로 2002년 $51 entry의 1/3/5년 total return을 역산하지 않았다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

첨부 SQL에 performance row가 없다. $51은 원문 서술가격이며, corporate action·배당·WellPoint 교환비율을 반영한 시계열을 복원하지 못해 1/3/5년 return과 IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | peer multiple discount | 20% | 성공/수익 미검증 | peer multiple은 margin·reserve 차이를 조정한다. |
| C2 | 100bp margin expansion | 18% | 방향 성공 | 보험 margin은 MLR와 SG&A로 나눈다. |
| C3 | 보험료 12% 인상 | 18% | 부분 검증 | price와 retention을 함께 본다. |
| C4 | IPO 물량압력 해소 | 16% | 미검증 | technical catalyst에는 날짜·거래량 조건을 둔다. |
| C5 | Kansas·과거 M&A 통합 | 16% | 성공 | serial M&A는 organic cohort와 분리한다. |
| C6 | national Blue option | 12% | 강한 성공 | terminal event와 투자수익은 별도 기록한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

demutualization 이후 비용규율, 보험료 재가격과 peer scale이 business quality를 높였다. 최종 결합은 네트워크 경쟁의 option value를 실현했다. 수익의 원인은 단순 multiple expansion보다 MLR·SG&A 개선과 기업결합 기대의 조합이었다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 $51에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

$58 base를 '20% 이상'으로 표현한 숫자 불일치, margin 100bp 개선을 세전/세후 EPS로 세밀하게 연결하지 않은 점, Kansas와 후속 인수의 통합비·reserve risk를 낮게 둔 점이 약점이다.

### 최초 관찰 가능한 경고/반증

MLR가 85%에서 peer 81~82%로 좁혀지지 않거나 두 번의 annual repricing 뒤에도 margin이 4% 아래면 $70 bull case를 제거해야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `ATH`를 회사로 보지 말고 Anthem, Inc. 법인·exchange·날짜로 고정한다.
2. **Direction audit:** raw Long가 아니라 원문 payoff를 읽어 Long을 확정한다.
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
| Entity / direction | raw Long → **Long**, Anthem, Inc. |
| Business thesis | 방향 성공 |
| Valuation thesis | 성공 |
| Catalyst / timing | 사업·전략 종착점 성공, SQL 가격성과는 미검증 |
| Thesis score | 8.5/10 |
| Process score | 8.0/10 |
| Outcome-adjusted score | 8.2/10 |

### 한 문장 교훈

> peer multiple은 margin·reserve 차이를 조정한다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/Anthem/3720878904) — VIC_IDEAS(4).sql / VIC, 2002-01-18. idea_id·raw direction·description 3322 chars·catalyst 69 chars
2. [Anthem 2001 VIC 원문](https://www.valueinvestorsclub.com/idea/Anthem/3720878904) — VIC, 2002-01-18. 8m 가입자·14x 2002 EPS·MLR와 $58/$70 valuation
3. [Anthem SEC filing archive](https://www.sec.gov/edgar/browse/?CIK=1156039&owner=exclude) — SEC / Anthem, 2001-2022. demutualization 이후 filings와 법인 연속성
4. [Anthem–WellPoint merger announcement](https://www.sec.gov/Archives/edgar/data/1156039/000119312504011119/d425.htm) — SEC / Anthem, 2003-10-27. WellPoint 결합 조건과 전략적 종착점

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=ATH, entity=Anthem, Inc., raw=Long, research=Long.
