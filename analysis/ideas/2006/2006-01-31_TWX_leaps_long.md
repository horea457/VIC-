# Time Warner Jan-2008 $15 calls — 2006-01-31 — V9

> **Batch 046 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **LEAPS Long**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Time Warner Jan-2008 $15 calls / TWX |
| Idea ID | `34b54ac6-6f41-4576-845b-4cfa4bb30646` |
| 게시일 / 작성자 | 2006-01-31 / beech625 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **LEAPS Long** |
| 기준가격 | common $17.50 / option $4.20 |
| 원 horizon | Jan-2008 expiry |
| 최종 판정 | **실패 — corporate 방향은 맞았지만 option clock이 먼저 만료** |

> **결론:** raw Short지만 실제 증권은 Jan-2008 $15 call Long이다. common $17.50, premium $4.20, 만기 breakeven $19.20에서 $12.5bn buyback, TWC value separation, AOL 재편과 Icahn activism을 레버리지했다. common $23.40이면 option 약 2배, $27.60이면 약 3배라는 payoff였다. 결과적으로 **실패 — corporate 방향은 맞았지만 option clock이 먼저 만료**.

---

## 1. 회사는 정확히 무엇을 하는가

Time Warner는 시기별로 TWC·AOL·Time Inc.를 분리하고 최종적으로 Turner, HBO, Warner Bros.의 premium-content 기업이 됐다. 현금엔진은 `Turner affiliate fee·광고 + HBO 구독·라이선스 + Warner Bros. 영화·TV·게임 수익 - 스포츠/제작비·마케팅·corporate cost·이자·세금`이다. OTT는 cable bundle과 linear viewing에는 위협이지만 premium IP에는 신규 buyer·DTC 경로를 늘릴 수 있다. 따라서 가입가구·affiliate fee, 광고, content spend/rights, HBO subs/ARPU, library monetization, FCF·buyback과 strategic control premium을 분리한다.

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

raw Short지만 실제 증권은 Jan-2008 $15 call Long이다. common $17.50, premium $4.20, 만기 breakeven $19.20에서 $12.5bn buyback, TWC value separation, AOL 재편과 Icahn activism을 레버리지했다. common $23.40이면 option 약 2배, $27.60이면 약 3배라는 payoff였다.

### Reverse expectations

common $17.50 / option $4.20가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. TWC hidden value — 20%

- **원문 주장:** cable asset 분리가 discount를 줄인다.
- **T0 근거:** TWC public value·Icahn SOTP
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 2009년에 실제 분리됐다.
- **판정:** **장기 성공/horizon 실패**
- **재사용 교훈:** spin feasibility와 만기를 연결한다.

### C2. buyback accretion — 18%

- **원문 주장:** $12.5bn repurchase가 주당가치를 빠르게 올린다.
- **T0 근거:** 대규모 이사회 승인
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 실행됐지만 option hurdle을 넘기지 못했다.
- **판정:** **부분 성공**
- **재사용 교훈:** 발표보다 평균 매입가·share count를 본다.

### C3. AOL turnaround — 18%

- **원문 주장:** 광고·Google 관계가 access decline을 상쇄한다.
- **T0 근거:** access/advertising 분리 가능성
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** turnaround보다 2009 spin으로 해결됐다.
- **판정:** **부분 실패**
- **재사용 교훈:** 문제자산의 개선과 제거를 구분한다.

### C4. sentiment mean reversion — 16%

- **원문 주장:** traditional media multiple이 정상화한다.
- **T0 근거:** 낮은 주가·activism
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 구조변화와 2007 risk-off가 막았다.
- **판정:** **실패**
- **재사용 교훈:** sentiment catalyst에 기한을 둔다.

### C5. cheap volatility — 16%

- **원문 주장:** 낮은 IV가 LEAPS convexity를 싸게 만든다.
- **T0 근거:** $4.20 premium
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** time decay가 event보다 빨랐다.
- **판정:** **실패**
- **재사용 교훈:** 싼 volatility와 싼 option은 다르다.

### C6. $23.40~27.60 within horizon — 12%

- **원문 주장:** 2년 내 option 2~3배가 된다.
- **T0 근거:** SOTP $26~28
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 2007 high $23.15·year-end $16.51였다.
- **판정:** **실패**
- **재사용 교훈:** 기업 duration과 security duration을 맞춘다.

---

## 4. 당시 Valuation과 Payoff Structure

만기 intrinsic은 `max(TWX-$15,0)`, 손익은 intrinsic-$4.20이다. $19.20 breakeven, $23.40 2배, $27.60 3배다. SOTP가 $26~28이어도 board·tax·financing 절차가 만기 뒤면 옵션은 실패한다. 기업가치 duration과 증권 duration을 같은 확률분포로 연결해야 했다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | LEAPS Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 실패 — corporate 방향은 맞았지만 option clock이 먼저 만료의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Common/option | $17.50/$4.20 | $23.40~27.60 | 2007 high $23.15 | 실패 |
| Expiry breakeven | $19.20 | 초과 | 2007 year-end $16.51 | 실패 |
| Buyback | $12.5bn | per-share accretion | 실행 방향 | 부분 성공 |
| TWC separation | 촉매 | 만기 전 | 2009-03 | horizon 실패 |
| AOL action | 재편 기대 | value unlock | 2009-12 spin | 장기 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2006-01-31 | VIC LEAPS Long | 2년 clock |
| 2006~07 | buyback·activism | 일부 촉매 |
| 2007 | high $23.15 | 2배 threshold 미달 |
| 2007-12-31 | close $16.51 | breakeven 하회 |
| 2008-01 | option expiry | security failure |
| 2009-03 | TWC separation | too late |
| 2009-12 | AOL spin | corporate simplification |

### 실제 사업·자본구조

대규모 buyback과 사업 단순화 방향은 진행됐고 TWC는 2009년 3월, AOL은 2009년 12월 분리됐다. 그러나 Time Warner 2007 연중 high는 $23.15로 2배 threshold $23.40에도 못 미쳤고 2007년말 $16.51은 breakeven 아래였다. 옳은 corporate event가 옵션 만기 뒤 왔다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

정확한 2008-01 option settlement·중간매도는 미복원이라 IRR은 null이다. 2007 high와 year-end close를 기준으로 원문의 2배/3배 조건은 실패했으며 security-level verdict는 실패다.

이 아이디어는 첨부 SQL과 repository source layer에 검증된 performance row가 없어 1개월~5년 수익률을 만들지 않는다. 사건 성공, target 달성과 투자 total return을 각각 별도 필드로 두며 누락값은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | TWC hidden value | 20% | 장기 성공/horizon 실패 | spin feasibility와 만기를 연결한다. |
| C2 | buyback accretion | 18% | 부분 성공 | 발표보다 평균 매입가·share count를 본다. |
| C3 | AOL turnaround | 18% | 부분 실패 | 문제자산의 개선과 제거를 구분한다. |
| C4 | sentiment mean reversion | 16% | 실패 | sentiment catalyst에 기한을 둔다. |
| C5 | cheap volatility | 16% | 실패 | 싼 volatility와 싼 option은 다르다. |
| C6 | $23.40~27.60 within horizon | 12% | 실패 | 기업 duration과 security duration을 맞춘다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

TWC/AOL 분리는 장기 enterprise value를 드러냈지만 2년 안의 주가·변동성·time decay가 option payoff를 지배했다. 값싼 implied volatility가 catalyst timing risk를 보상하지 못했다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 common $17.50 / option $4.20에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

Icahn SOTP와 planned buyback을 만기 안 catalyst처럼 취급했다. legal separation calendar, 금융위기·sentiment branch와 만기 롤 비용을 확률가중하지 않았다.

### 최초 관찰 가능한 경고/반증

2007년 내내 common이 $23.40을 넘지 못하고 12월말 $16.51로 내려갔을 때 corporate thesis와 무관하게 option thesis를 종료해야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** ticker `TWX`만 보지 말고 Time Warner Jan-2008 $15 calls의 법인·증권·날짜로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 LEAPS Long을 확정한다.
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
| Entity / direction | raw Short → **LEAPS Long**, Time Warner Jan-2008 $15 calls |
| Business thesis | 부분 성공 |
| Valuation thesis | 실패 |
| Catalyst / timing | 실패 — corporate 방향은 맞았지만 option clock이 먼저 만료 |
| Thesis score | 4.0/10 |
| Process score | 7.0/10 |
| Outcome-adjusted score | 5.5/10 |

### 한 문장 교훈

> spin feasibility와 만기를 연결한다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/Time_Warner_LEAPS/5456777628) — VIC_IDEAS(4).sql / VIC, 2006-01-31. idea_id·raw direction·description 0 chars·catalyst 213 chars
2. [Time Warner 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/1105705/000095014408001291/g11419e10vk.htm) — SEC / Time Warner, 2008-02-29. 2007 주가범위·TWC/AOL과 사업구조
3. [TWC separation disclosure](https://www.sec.gov/Archives/edgar/data/1105705/000095014409003643/g18170e10vq.htm) — SEC / Time Warner, 2009-03. $9.253bn cash transfer와 TWC 분리
4. [Time Warner 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1105705/000119312516477965/d280491d10k.htm) — SEC / Time Warner, 2016-02-24. Turner·HBO·Warner Bros. segment economics
5. [Time Warner 2016 Form 10-K](https://www.sec.gov/Archives/edgar/data/1105705/000119312517053483/d300508d10k.htm) — SEC / Time Warner, 2017-02-22. 2016 EPS·OTT·AT&T collar와 year-end 2017 예상
6. [DOJ antitrust challenge](https://www.justice.gov/archives/opa/pr/justice-department-challenges-attdirectv-s-acquisition-time-warner) — U.S. DOJ, 2017-11-20. vertical deal에 대한 소송과 duration risk
7. [AT&T closing Form 8-K](https://www.sec.gov/Archives/edgar/data/732717/000119312518194502/d609728d8k.htm) — SEC / AT&T, 2018-06-15. $53.75 cash+1.437 AT&T shares의 최종 consideration

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL와 repository raw extract로 원문 direction·수치를 수동검증.
- 기업·사건: **A/B** — SEC·회사·규제기관 자료로 terminal event를 교차검증.
- 가격성과: **C** — SQL performance row 부재. 원문 가격은 anchor이며 exact return/IRR은 null.
- 교정: ticker=TWX, entity=Time Warner Jan-2008 $15 calls, raw=Short, research=LEAPS Long.
