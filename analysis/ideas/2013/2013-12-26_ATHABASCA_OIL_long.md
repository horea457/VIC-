# Athabasca Oil Corp. — 2013-12-26 — V9

> **Batch 046 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Long**으로 확정했다. Research as-of 2026-09-09.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Athabasca Oil Corp. / ATH |
| Idea ID | `147a6251-3aab-4a99-bfee-0685a093135d` |
| 게시일 / 작성자 | 2013-12-26 / hao777 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격 | C$6.25 |
| 원 horizon | 6~24개월 |
| 최종 판정 | **핵심 put catalyst 성공, C$10~15 NAV의 지속성은 oil shock로 실패** |

> **결론:** raw Short지만 C$6.25에서 산 event-driven Long이다. 주가는 YTD 40% 하락했지만 Dover 40% put C$1.32bn은 시가총액의 약 50%였고, Fort McKay First Nation 분쟁·cabinet 지연이 2개 분기 안에 풀릴 것으로 봤다. core/light-oil NAV는 C$17 북쪽, haircut한 적정가는 C$10~15였다. 결과적으로 **핵심 put catalyst 성공, C$10~15 NAV의 지속성은 oil shock로 실패**.

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

raw Short지만 C$6.25에서 산 event-driven Long이다. 주가는 YTD 40% 하락했지만 Dover 40% put C$1.32bn은 시가총액의 약 50%였고, Fort McKay First Nation 분쟁·cabinet 지연이 2개 분기 안에 풀릴 것으로 봤다. core/light-oil NAV는 C$17 북쪽, haircut한 적정가는 C$10~15였다.

### Reverse expectations

C$6.25가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. 2개 분기 내 C$1.32bn — 20%

- **원문 주장:** settlement·cabinet 뒤 put 수취다.
- **T0 근거:** 계약·AER approval·PetroChina 의사
- **숨은 가정:** FMFN 합의와 condition precedent 완료.
- **사전 반증조건:** hearing·appeal 재지연이면 반증.
- **실제:** 후속 거래로 현금화됐다.
- **판정:** **성공**
- **재사용 교훈:** binary event는 법적 gate별 확률을 둔다.

### C2. C$10~15 fair value — 18%

- **원문 주장:** 현금과 자산을 합치면 현 가격 60~100%+다.
- **T0 근거:** gross NAV >C$17
- **숨은 가정:** capex·oil haircut이 충분하다.
- **사전 반증조건:** strip 하락으로 project NPV가 음수면 반증.
- **실제:** oil shock에서 지속되지 않았다.
- **판정:** **장기 실패**
- **재사용 교훈:** resource NAV는 strip·capex sensitivity 표가 필요하다.

### C3. Plan B가 bridge — 18%

- **원문 주장:** C$460m 예산으로 put까지 버틴다.
- **T0 근거:** Kaybob infra 50% 매각 C$145m
- **숨은 가정:** 추가 희석 없이 핵심 project 유지.
- **사전 반증조건:** liquidity buffer가 12개월 아래면 반증.
- **실제:** 회사는 event까지 bridge했다.
- **판정:** **성공**
- **재사용 교훈:** bridge liquidity는 최소 18개월로 본다.

### C4. Hangingstone first steam — 16%

- **원문 주장:** Q4'14부터 12k boe/d가 가치를 연다.
- **T0 근거:** 건설·개발 일정
- **숨은 가정:** cost/SOR/ramp가 plan 근처다.
- **사전 반증조건:** 6개월+ 지연·capex overrun이면 반증.
- **실제:** 운영가치는 macro·ramp에 흔들렸다.
- **판정:** **혼합**
- **재사용 교훈:** first steam과 steady-state cash를 구분한다.

### C5. Duvernay option — 16%

- **원문 주장:** 350k net/200k high-grade acres가 jewel이다.
- **T0 근거:** peer well results
- **숨은 가정:** ATH acreage와 economics가 비교 가능.
- **사전 반증조건:** well NPV·JV bid가 기대 미달이면 반증.
- **실제:** asset option은 남았지만 target을 방어하지 못했다.
- **판정:** **부분**
- **재사용 교훈:** adjacent acreage는 own-well data로 할인한다.

### C6. misguided promises는 신뢰문제일 뿐 — 12%

- **원문 주장:** 2013 사건은 저확률 legal delay다.
- **T0 근거:** management Plan B
- **숨은 가정:** 운영·capital allocation 능력은 훼손되지 않음.
- **사전 반증조건:** 반복 일정 miss면 governance discount 구조화.
- **실제:** event는 풀렸지만 후속 value는 약했다.
- **판정:** **부분**
- **재사용 교훈:** 한 번의 외생지연과 반복 과신을 분리한다.

---

## 4. 당시 Valuation과 Payoff Structure

Hangingstone·Dover West·Duvernay·Montney를 합친 gross NAV에서 capex·corporate cost를 빼면 C$17+라고 계산했고, 실행 haircut 뒤 C$10~15를 제시했다. 가장 관찰 가능한 bridge는 C$1.32bn put 수취다. 이것이 약 C$3.3/share에 해당하더라도 전액 excess cash가 아니며 2014 C$460m budget과 project funding을 차감해야 한다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 핵심 put catalyst 성공, C$10~15 NAV의 지속성은 oil shock로 실패의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | C$6.25 | C$10~15 | SQL 성과 없음 | 미검증 |
| Dover put | C$1.32bn | 2개 분기 수취 | 후속 수취 | 성공 |
| 2014 budget | C$460m | flexibility 유지 | 현금 재투자 | 혼합 |
| Hangingstone 1 | 12k boe/d | Q4'14 first steam | ramp/cycle risk | 혼합 |
| Core NAV | >C$17 | 60~100%+ upside | oil shock로 훼손 | 실패 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2013-04 | AER hearing | FMFN dispute |
| 2013-08-06 | AER approval | 주가 반응 |
| 2013-10-18 | appeal 수용 | overhang 확대 |
| 2013-12-26 | VIC Long | C$6.25 |
| 2014 | settlement/approval 진행 | event de-risk |
| 2014 | Dover put 현금화 | 핵심 catalyst |
| 2014-2016 | oil collapse | NAV 반증 |

### 실제 사업·자본구조

Dover 관련 승인·합의가 진행되고 Athabasca는 PetroChina put 대금을 받으면서 가장 중요한 binary catalyst는 실현됐다. 그러나 직후의 원유가격 붕괴와 development economics 악화로 gross NAV는 현금만큼 안정적인 가치가 아니었다. event window의 논지는 성공이지만 C$10~15를 장기 intrinsic value로 본 결론은 지속되지 않았다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

SQL performance가 없다. C$6.25 entry와 C$10~15 target의 정확한 달성·보유수익은 null로 남긴다. 사건 발생을 price return으로 대체하지 않는다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | 2개 분기 내 C$1.32bn | 20% | 성공 | binary event는 법적 gate별 확률을 둔다. |
| C2 | C$10~15 fair value | 18% | 장기 실패 | resource NAV는 strip·capex sensitivity 표가 필요하다. |
| C3 | Plan B가 bridge | 18% | 성공 | bridge liquidity는 최소 18개월로 본다. |
| C4 | Hangingstone first steam | 16% | 혼합 | first steam과 steady-state cash를 구분한다. |
| C5 | Duvernay option | 16% | 부분 | adjacent acreage는 own-well data로 할인한다. |
| C6 | misguided promises는 신뢰문제일 뿐 | 12% | 부분 | 한 번의 외생지연과 반복 과신을 분리한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

초기 rerating을 만든 것은 court/cabinet sequence와 지급확률이었다. 이후 common 가치는 받은 현금의 재투자, Hangingstone ramp와 oil price로 이동했다. thesis가 event asset에서 operating E&P로 바뀐 순간 exit rule이 필요했다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 C$6.25에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

C$1.32bn 수령과 C$17 gross NAV를 같은 확실성으로 합쳤고, cash receipt 직후 2014 capex·Hangingstone ramp·commodity hedge를 충분히 stress하지 않았다. 정부·First Nation 사건의 확률도 단일 2-quarter clock에 과도하게 압축했다.

### 최초 관찰 가능한 경고/반증

Dover cash가 들어온 뒤에도 주당 순현금이 budget burn보다 빠르게 줄거나 Hangingstone first steam/cost가 plan을 벗어나면 catalyst 성공과 무관하게 exit해야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `ATH`를 회사로 보지 말고 Athabasca Oil Corp. 법인·exchange·날짜로 고정한다.
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
| Entity / direction | raw Short → **Long**, Athabasca Oil Corp. |
| Business thesis | 장기 실패 |
| Valuation thesis | 미검증 |
| Catalyst / timing | 핵심 put catalyst 성공, C$10~15 NAV의 지속성은 oil shock로 실패 |
| Thesis score | 7.5/10 |
| Process score | 8.0/10 |
| Outcome-adjusted score | 7.8/10 |

### 한 문장 교훈

> binary event는 법적 gate별 확률을 둔다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/ATHABASCA_OIL_CORP/8944407068) — VIC_IDEAS(4).sql / VIC, 2013-12-26. idea_id·raw direction·description 20053 chars·catalyst 0 chars
2. [Athabasca investor reports](https://www.athabascaoil.com/investors/financial-reports/) — Athabasca Oil, 2011-2025. Dover 현금·Hangingstone·light-oil 자본배분의 후속 검증
3. [Athabasca corporate presentation archive](https://www.athabascaoil.com/investors/presentations-events/) — Athabasca Oil, 2011-2025. project 규모·production ramp·자본계획
4. [Alberta Energy Regulator](https://www.aer.ca/) — AER, 2013-2014. Dover 승인과 규제경로의 1차 기관

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=ATH, entity=Athabasca Oil Corp., raw=Short, research=Long.
