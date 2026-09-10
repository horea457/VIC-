# Time Warner / AT&T merger claim — 2017-02-22 — V9

> **Batch 046 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Merger Arb Long**으로 확정했다. Research as-of 2026-09-10.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Time Warner / AT&T merger claim / TWX |
| Idea ID | `a32500d7-d85f-41a7-a66b-cba1ec17747e` |
| 게시일 / 작성자 | 2017-02-22 / rhianik |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Merger Arb Long** |
| 기준가격 | implied consideration 약 $107.80 |
| 원 horizon | 2017-12-31 close 가정 |
| 최종 판정 | **성공 — deal close, regulatory simplicity·duration은 실패** |

> **결론:** raw Short지만 실제는 AT&T/Time Warner merger-arbitrage Long이다. $53.75 cash와 AT&T stock collar를 합친 당시 implied consideration 약 $107.80 대비 absolute spread 약 12%, year-end 2017 close 가정 annualized 약 14%와 TWX 배당 1.8%를 기대했다. vertical deal·FCC license 이슈 제한으로 closing probability가 높다고 봤다. 결과적으로 **성공 — deal close, regulatory simplicity·duration은 실패**.

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

raw Short지만 실제는 AT&T/Time Warner merger-arbitrage Long이다. $53.75 cash와 AT&T stock collar를 합친 당시 implied consideration 약 $107.80 대비 absolute spread 약 12%, year-end 2017 close 가정 annualized 약 14%와 TWX 배당 1.8%를 기대했다. vertical deal·FCC license 이슈 제한으로 closing probability가 높다고 봤다.

### Reverse expectations

implied consideration 약 $107.80가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. high close probability — 20%

- **원문 주장:** vertical integration이라 거래가 닫힌다.
- **T0 근거:** shareholder approval·asset quality
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 최종 close했다.
- **판정:** **성공**
- **재사용 교훈:** probability와 path를 분리한다.

### C2. regulatory simplicity — 18%

- **원문 주장:** FCC transfer·horizontal overlap가 제한적이다.
- **T0 근거:** vertical-deal precedent
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** DOJ가 실제 소송을 제기했다.
- **판정:** **실패**
- **재사용 교훈:** 기관 jurisdiction보다 remedy theory를 본다.

### C3. year-end 2017 close — 18%

- **원문 주장:** review가 10개월 안에 끝난다.
- **T0 근거:** 회사 guidance·거래구조
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 2018-06까지 지연됐다.
- **판정:** **실패**
- **재사용 교훈:** 3/6/12개월 delay IRR을 만든다.

### C4. limited break downside — 16%

- **원문 주장:** fail해도 TWX standalone valuation은 견고하다.
- **T0 근거:** premium content·peer multiple
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** deal이 닫혀 관찰되지 않았다.
- **판정:** **미검증**
- **재사용 교훈:** unaffected price와 peer beta를 stress한다.

### C5. collar hedge — 16%

- **원문 주장:** AT&T stock leg를 비율대로 hedge할 수 있다.
- **T0 근거:** 1.3~1.437 share collar
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 최종 1.437주가 지급됐다.
- **판정:** **성공**
- **재사용 교훈:** VWAP window에 맞춰 delta를 조정한다.

### C6. dividend carry — 12%

- **원문 주장:** TWX 배당이 기다림을 보완한다.
- **T0 근거:** 분기 $0.405 예상
- **숨은 가정:** 핵심 수치·capital·catalyst가 원 horizon 안에 유지된다.
- **사전 반증조건:** 핵심 KPI가 두 분기 연속 역행하거나 event gate가 실패하면 반증한다.
- **실제:** 배당은 받았지만 T short carry도 있었다.
- **판정:** **부분 성공**
- **재사용 교훈:** 양쪽 배당·borrow를 netting한다.

---

## 4. 당시 Valuation과 Payoff Structure

stock leg는 T 15-day VWAP가 $37.411 아래면 1.437주, $41.349 위면 1.3주, 중간이면 $53.75/VWAP다. expected IRR은 `확률가중 consideration/entry-1`을 expected duration으로 연율화하고 T short dividend·borrow·financing cost와 break loss를 차감해야 한다. 2017-12-31이라는 단일 날짜가 가장 큰 sensitivity였다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Merger Arb Long 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 성공 — deal close, regulatory simplicity·duration은 실패의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Implied consideration | ~$107.80 | 12% absolute | $53.75+1.437 T shares | 성공 |
| Annualized spread | ~14% | 2017-12-31 close | 2018-06-14 close | 하향 |
| TWX dividends | 3~4×$0.405 | ~1.8% 보완 | closing 전 지급 | 성공 |
| Regulatory path | vertical/simple | 소송 없음 | DOJ litigation | 실패 |
| Break downside | peer-like valuation | 제한적 | deal closed | 미검증 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2016-10-22 | merger agreement | cash-stock collar |
| 2017-02-15 | shareholder approval | closing gate |
| 2017-02-22 | VIC arb Long | 14% annualized |
| 2017-11-20 | DOJ lawsuit | litigated arb |
| 2018-03~06 | antitrust trial | duration |
| 2018-06-12 | 법원 challenge 기각 | close 가능 |
| 2018-06-14 | acquisition 완료 | deal success |

### 실제 사업·자본구조

DOJ는 2017-11-20 거래 저지 소송을 제기했고 법원 판단을 거쳐 2018-06-14에야 closing했다. 최종 TWX 1주당 $53.75 cash+1.437 AT&T shares가 지급됐다. deal direction은 맞았지만 routine vertical review라는 규제경로와 duration 가정은 틀렸다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

hedge ratio, T short entry·배당, TWX 배당, financing cost가 없어 exact arb IRR은 null이다. absolute deal leg는 성공했으나 closing이 약 5.5개월 늦어져 annualized return은 원문 14%보다 낮아졌다.

이 아이디어는 첨부 SQL과 repository source layer에 검증된 performance row가 없어 1개월~5년 수익률을 만들지 않는다. 사건 성공, target 달성과 투자 total return을 각각 별도 필드로 두며 누락값은 null이다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | high close probability | 20% | 성공 | probability와 path를 분리한다. |
| C2 | regulatory simplicity | 18% | 실패 | 기관 jurisdiction보다 remedy theory를 본다. |
| C3 | year-end 2017 close | 18% | 실패 | 3/6/12개월 delay IRR을 만든다. |
| C4 | limited break downside | 16% | 미검증 | unaffected price와 peer beta를 stress한다. |
| C5 | collar hedge | 16% | 성공 | VWAP window에 맞춰 delta를 조정한다. |
| C6 | dividend carry | 12% | 부분 성공 | 양쪽 배당·borrow를 netting한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

spread 수렴은 법원 승소와 closing이 만들었다. 반대로 DOJ litigation은 duration·mark-to-market·financing cost를 늘렸다. probability와 duration을 독립 변수가 아니라 litigated path의 결합분포로 봐야 했다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 implied consideration 약 $107.80에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

정치발언은 할인하면서 실제 DOJ 소송 branch를 거의 두지 않았다. vertical precedent만으로 regulatory simplicity를 결론내리고 stock collar와 long/short dividend carry의 경로를 충분히 모델링하지 않았다.

### 최초 관찰 가능한 경고/반증

2017-11-20 DOJ complaint가 제출된 순간 routine arb가 litigated arb로 바뀌었다. position size·break price·6/12개월 delay IRR을 완전히 다시 계산해야 했다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** ticker `TWX`만 보지 말고 Time Warner / AT&T merger claim의 법인·증권·날짜로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Merger Arb Long을 확정한다.
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
| Entity / direction | raw Short → **Merger Arb Long**, Time Warner / AT&T merger claim |
| Business thesis | 실패 |
| Valuation thesis | 성공 |
| Catalyst / timing | 성공 — deal close, regulatory simplicity·duration은 실패 |
| Thesis score | 8.0/10 |
| Process score | 8.0/10 |
| Outcome-adjusted score | 8.0/10 |

### 한 문장 교훈

> probability와 path를 분리한다.

---

## 12. Sources / Validation Notes

1. [첨부 SQL 원문/metadata](https://www.valueinvestorsclub.com/idea/TIME_WARNER_INC/2622171445) — VIC_IDEAS(4).sql / VIC, 2017-02-22. idea_id·raw direction·description 0 chars·catalyst 84 chars
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
- 교정: ticker=TWX, entity=Time Warner / AT&T merger claim, raw=Short, research=Merger Arb Long.
