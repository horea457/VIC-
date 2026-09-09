# Level 3 Communications (LVLT) — 2017-07-29 VIC Long

> **Idea unit:** 이 게시일·증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 원 SQL 방향은 Short로 보존하고 실제 원문 방향·증권은 research layer에서 교정했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Level 3 Communications / LVLT |
| VIC 게시일 / 작성자 | 2017-07-29 / VQRP99 |
| 분석 증권 / 실제 방향 | LVLT common into CTL merger / post-close hold |
| 원 SQL 방향 | Short — raw 값 보존, 실제 원문은 매수 논지 |
| 기준 진입가격 | $58.61 |
| 기대기간 | deal close 후 1~2년; standalone 5년 |
| raw horizon audit | 2017-09-30 예상 close·1~2년 $75~90 |
| 최종 판정 | **혼합 — 거래종결 성공, post-close $75~90·dividend thesis 실패** |

> **결론:** 2017-11-01 계약대로 $26.50 cash+1.4286 CTL shares를 받은 event leg는 성공했다. 그러나 post-close combined EBITDA $10bn, dividend safety와 LVLT-equivalent $75~90 rerating은 이어진 CenturyLink/Lumen의 2019 dividend cut과 2022 dividend elimination으로 반증됐다. arb와 장기 hold를 하나의 성공으로 묶으면 안 된다.

---

## 1. 회사는 정확히 무엇을 하는가

Level 3 Communications는 북미·유럽·중남미의 장거리·도시 광섬유망, IP backbone, enterprise buildings와 data center를 연결해 기업·통신사·콘텐츠 사업자에게 wavelength, transport, IP transit, VPN, voice, colocation을 팔았다. 선행 network cost는 크고 incremental on-net traffic의 비용은 낮다. 따라서 traffic 증가만으로는 충분하지 않고, 단위가격 하락보다 volume·on-net 전환이 빨라야 하며 gross margin과 EBITDA가 cash interest·capex를 넘은 뒤에야 common equity 가치가 생긴다.

Common의 현금엔진은 `Core Network Services 매출 - access/network cost - SG&A - cash interest - capex - tax = equity FCF`다. Bank debt·채권은 enterprise value에서 senior claim, 담보, coupon, 만기, exchange/tender 조건을 적용한 회수액이 payoff다. 같은 회사라도 common, secured bank debt, subordinated convert의 손익은 서로 반대일 수 있다.

### 가치사슬과 security payoff

고객 traffic와 계약매출이 access/network cost, SG&A, cash interest, capex, tax를 통과한 뒤 common에 남는다. Debt 아이디어는 enterprise value보다 담보·선순위·만기·refinancing source가 먼저다. Pair는 long bond와 short common, option hedge의 각 cash flow를 별도로 기록해야 한다.

### 매 분기 볼 핵심 KPI

CNS organic·constant-currency revenue, enterprise buildings·on-net connects, churn, price decline 대비 traffic volume, incremental gross/EBITDA margin, capex/revenue, FCF, cash interest, liquidity, 순레버리지, maturity wall, debt-for-equity dilution

---

## 2. 당시 상황과 시장이 가격에 넣은 것

LVLT는 $58.61, 360m shares, market cap $21bn, net debt $9bn, NOL 약 $9bn이었다. offer는 $26.50 cash+1.4286 CTL shares로 당시 약 $59.80, 2% spread였고 2017-09-30 close를 기대했다. 결합 EBITDA는 CTL $6bn+LVLT $3bn+$1bn synergy=$10bn, strategic mix 65%, mid-single digit EBITDA growth, 7~8배에서 LVLT-equivalent $75~90을 제시했다.

### Reverse expectations

시장 spread는 regulatory·timing risk와 CTL 주가변동을, 낮은 CTL multiple은 legacy consumer decline·integration·capex·leverage·dividend risk를 반영했다. half-cash consideration은 deal-break downside를 낮추지만 post-close CTL exposure를 제거하지 않는다.

---

## 3. 원문 투자논지 지도

### C1. 거래가 2017년 종결 — 성공

**원문 주장**

$26.50+1.4286 CTL을 예정대로 받는다.

**경제적 메커니즘**

승인과 financing 완료로 2% spread가 수렴한다.

**T0 근거**

signed merger·small spread.

**숨은 가정**

regulatory remedies와 CTL price risk가 관리된다.

**사전 반증조건**

deal delay·break면 반증.

**실제 결과**

2017-11-01 계약조건대로 종결.

**정량 gap**

예상 9월말 대비 약 한 달 지연.

**분석 오류 또는 제한**

close date를 과도하게 정확히 잡았다.

**재사용 교훈**

arb는 calendar buffer와 share hedge를 둔다.

### C2. LVLT deal-break downside가 낮음 — 미검증

**원문 주장**

half cash와 standalone quality가 downside를 줄인다.

**경제적 메커니즘**

LVLT FCF·replacement value가 break price를 지지한다.

**T0 근거**

2016 FCF $1.009bn, NOL·network.

**숨은 가정**

standalone operating trend가 유지된다.

**사전 반증조건**

CNS/FCF 급락이면 floor 약화.

**실제 결과**

deal이 완료돼 직접 시험되지 않았다.

**정량 gap**

counterfactual 미검증.

**분석 오류 또는 제한**

unobserved downside를 성공으로 볼 수 없다.

**재사용 교훈**

deal-break value는 독립 standalone model로 보관한다.

### C3. combined EBITDA $10bn — 부분 실패

**원문 주장**

$6bn+$3bn+$1bn synergy가 실현된다.

**경제적 메커니즘**

망·SG&A 중복 제거로 strategic mix와 margin이 오른다.

**T0 근거**

원문 pro-forma bridge.

**숨은 가정**

legacy decline·integration cost가 synergy보다 작다.

**사전 반증조건**

EBITDA·FCF가 계획을 못 따르면 반증.

**실제 결과**

2019 FCF guide는 강했지만 자본정책은 방어적으로 바뀌었다.

**정량 gap**

headline FCF만으로 equity rerating 부재.

**분석 오류 또는 제한**

synergy와 quality를 같은 것으로 봤다.

**재사용 교훈**

결합 EBITDA는 organic mix와 cost synergy를 분리한다.

### C4. FCF $2.80→$3/share — 부분 실패

**원문 주장**

$10bn EBITDA에서 capex·interest·tax 후 충분한 현금이 남는다.

**경제적 메커니즘**

FCF가 deleveraging·dividend·equity value를 동시에 지지한다.

**T0 근거**

원문 $10-$4-$2.2-$0.65bn bridge.

**숨은 가정**

working capital·restructuring·integration cash가 작다.

**사전 반증조건**

배당 cut 또는 leverage 악화면 반증.

**실제 결과**

2019 FCF guide $3.1~3.4bn에도 dividend를 낮췄다.

**정량 gap**

gross FCF와 distributable FCF 괴리.

**분석 오류 또는 제한**

현금의 경쟁용도를 과소평가했다.

**재사용 교훈**

FCF allocation waterfall을 별도 모델링한다.

### C5. dividend는 안전 — 강한 실패

**원문 주장**

FCF coverage가 높아 CTL payout이 유지된다.

**경제적 메커니즘**

배당수익이 rerating 대기기간을 보상한다.

**T0 근거**

원문 FCF bridge와 payout.

**숨은 가정**

board가 debt·capex보다 dividend를 우선한다.

**사전 반증조건**

dividend cut이면 즉시 반증.

**실제 결과**

2019 annual dividend $1로 cut, 2022 완전 elimination.

**정량 gap**

명시적 반증.

**분석 오류 또는 제한**

배당을 discretionary equity distribution이 아닌 coupon처럼 봤다.

**재사용 교훈**

배당안전에는 board priority와 leverage covenant를 포함한다.

### C6. 7~8x에서 LVLT $75~90 — 실패

**원문 주장**

strategic mix 65%와 mid-single digit EBITDA growth가 rerating을 만든다.

**경제적 메커니즘**

질 높은 enterprise mix가 legacy telco discount를 줄인다.

**T0 근거**

원문 multiple sensitivity.

**숨은 가정**

시장과 경영진이 mix 개선을 신뢰한다.

**사전 반증조건**

dividend cut·multiple compression이면 실패.

**실제 결과**

post-close capital allocation stress로 rerating thesis가 훼손됐다.

**정량 gap**

$75~90 실현 근거 없음.

**분석 오류 또는 제한**

acquirer legacy exposure를 과소평가했다.

**재사용 교훈**

blended company는 segment별 duration multiple을 쓴다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 FCF bridge는 $10bn EBITDA-$4bn capex-$2.2bn interest-$650m pension/tax로 약 $3.15bn, 주당 약 $2.80에서 $3를 기대했다. 7~8배 EBITDA rerating과 $1bn synergy가 $75~90을 만들었다. standalone은 replacement value $95, FCF 20~25% CAGR으로 5년 $120~150을 주장했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Deal break | LVLT standalone | 원문 downside 제한 | 미발생 |
| Arb | 계약대로 close | 2% spread | 2017-11-01 성공 |
| Post-close bull | $10bn EBITDA·7~8x | $75~90 | dividend cut·rerating 실패 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / implied deal | $58.61 / 약 $59.80 | 2% spread | 계약조건 종결 | 성공 |
| Consideration | $26.50+1.4286 CTL | 수령 | 2017-11-01 수령 | 성공 |
| Combined EBITDA | $10bn 예상 | $1bn synergy | rerating 미실현 | 부분 |
| FCF | 약 $2.80/share | $3 | 2019 $3.1~3.4bn guide | headline 일부 |
| Dividend | 안전 주장 | 유지 | 2019 cut·2022 제거 | 실패 |

### 촉매와 시간

판정 horizon은 **deal close 후 1~2년; standalone 5년**다. 이후 사건은 장기 가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2017-07-29 | VIC merger/post-close Long | $58.61 |
| 2017-11-01 | 거래 종결 | $26.50+1.4286 CTL |
| 2017-12-31 | former LVLT holders 약 49% | CTL exposure 현실화 |
| 2019-02 | 2019 FCF $3.1~3.4bn guide | 현금력 일부 |
| 2019-02 | annual dividend $1로 cut | 첫 hold 반증 |
| 2022-11-02 | dividend elimination | 장기 thesis 실패 |

### 실제 사업·자본구조 추이

거래는 예상보다 약 한 달 늦은 2017-11-01 종결됐고 former LVLT holders가 combined company 약 49%를 보유했다. CenturyLink는 2019 FCF $3.1~3.4bn을 안내했지만 연 dividend를 $1.00으로 낮추는 capital-allocation reset을 발표했다. Lumen은 2022-11-02 common dividend를 완전히 없앴다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

contractual consideration은 직접 확인된다. 그러나 $75~90 LVLT-equivalent의 exact 1~2년 total return은 CTL share-price·배당·mark date가 필요해 여기서는 임의 계산하지 않는다. dividend cut·elimination은 long-hold thesis의 명확한 fundamental failure signal이다.

가격 series가 없으면 수익률·MFE·MAE를 추정하지 않는다. Bond·pair는 exact issue, coupon, exchange, short borrow와 cash-flow date가 있어야 IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 거래가 2017년 종결 | 20% | 성공 | 예상 9월말 대비 약 한 달 지연. |
| C2 | LVLT deal-break downside가 낮음 | 18% | 미검증 | counterfactual 미검증. |
| C3 | combined EBITDA $10bn | 18% | 부분 실패 | headline FCF만으로 equity rerating 부재. |
| C4 | FCF $2.80→$3/share | 16% | 부분 실패 | gross FCF와 distributable FCF 괴리. |
| C5 | dividend는 안전 | 16% | 강한 실패 | 명시적 반증. |
| C6 | 7~8x에서 LVLT $75~90 | 12% | 실패 | $75~90 실현 근거 없음. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

event 수익은 small merger spread와 확정 consideration이 만들었다. 장기 손실은 legacy CTL decline, integration/capital intensity, leverage와 dividend-capital allocation이 $1bn synergy·FCF보다 크게 작용한 데서 나왔다.

### Counterfactual

2% arb spread만 원했다면 close 즉시 CTL shares를 매도했어야 하는가, 아니면 $75~90 long을 정당화할 별도 downside·dividend test가 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

낮은 deal-break downside와 post-close operating upside를 하나의 포지션으로 묶고, dividend를 FCF output이 아니라 사실상 고정 claim처럼 취급했다.

### 최초로 관찰 가능했던 경고신호

2019년 annual dividend를 $1.00으로 낮춘 결정이 combined-company hold 논지의 첫 명확한 반증이다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

merger arb와 post-close fundamental Long은 entry·exit·반증조건을 분리한다.

### Lesson 2

배당안전은 headline FCF보다 leverage·capex·management priority로 검증한다.

### Lesson 3

주식대가 거래는 target 가격이 아니라 acquirer exposure를 산다.

### 지금 같은 아이디어를 다시 본다면

- regulatory approvals
- deal consideration mark
- CTL hedge ratio
- realized synergy
- legacy revenue decline
- capex/EBITDA
- dividend coverage·priority

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | LVLT cash engine 성공·결합 실패 |
| Valuation thesis | arb 성공·rerating 실패 |
| Catalyst thesis | deal close 성공 |
| Timing / path | 1~2년 hold 실패 |
| Security selection | arb 적절·unhedged CTL 부적절 |
| Thesis score | 5.5/10 |
| Process score | 7.5/10 |
| 종합 | **혼합 — 거래종결 성공, post-close $75~90·dividend thesis 실패** |

### 한 문장 교훈

> merger arb와 post-close fundamental Long은 entry·exit·반증조건을 분리한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/LEVEL_3_COMMUNICATIONS_INC/3863570505) — Value Investors Club / source SQL, 2017-07-29. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준.
2. [Level 3 2002 Form 10-K/A](https://www.sec.gov/Archives/edgar/data/794323/000104746903013081/a2108070z10-ka.htm) — SEC / Level 3, 2003-04. 2001~02 liquidity, debt repurchase와 junior convert financing 검증.
3. [Level 3 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/794323/000104746905006668/a2153221z10-k.htm) — SEC / Level 3, 2005-03. $1.125bn secured facility 전액상환과 2008 notes 할인매입 검증.
4. [Level 3 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/794323/000104746908002075/a2182924z10-k.htm) — SEC / Level 3, 2008-02. 인수통합, debt/equity financing, 2008 cash consumption 전망 검증.
5. [Level 3 2011 Form 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432312000003/lvlt-123111_10k.htm) — SEC / Level 3, 2012-02. Global Crossing 종결, $958m adjusted EBITDA, $716m interest, 1-for-15 reverse split 검증.
6. [Global Crossing acquisition announcement](https://www.sec.gov/Archives/edgar/data/794323/000119312511093638/dex991.htm) — SEC / Level 3, 2011-04-11. pro-forma revenue·EBITDA와 synergy 기대 검증.
7. [Level 3 2014 proxy](https://www.sec.gov/Archives/edgar/data/794323/000104746915003240/a2223988zdef14a.htm) — SEC / Level 3, 2015-04. 2014 sustainable FCF $325m과 2013 대비 $372m 개선 검증.
8. [Level 3 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432316000025/lvlt-123115_10k.htm) — SEC / Level 3, 2016-02. 2015 FCF $626m과 성숙기 cash conversion 검증.
9. [Level 3 2016 Form 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432317000002/lvlt-123116_10k.htm) — SEC / Level 3, 2017-02. 2016 FCF $1.009bn과 merger 전 재무상태 검증.
10. [CenturyLink / Level 3 merger proxy](https://www.sec.gov/Archives/edgar/data/794323/000119312517040682/d282157ddefm14a.htm) — SEC, 2017-02. $26.50 cash + 1.4286 CTL shares의 계약조건 검증.
11. [Level 3 merger completion 8-K](https://www.sec.gov/Archives/edgar/data/794323/000119312517329395/d459582d8k.htm) — SEC / Level 3, 2017-11-01. 거래 종결과 실제 consideration 검증.
12. [CenturyLink 2017 Form 10-K](https://www.sec.gov/Archives/edgar/data/18926/000001892618000012/ctl2017123110k.htm) — SEC / CenturyLink, 2018-02. former LVLT ownership 약 49%와 acquisition accounting 검증.
13. [CenturyLink FY2018 results and 2019 outlook](https://www.sec.gov/Archives/edgar/data/18926/000001892619000003/ctl4q20188-kexhibit991.htm) — SEC / CenturyLink, 2019-02. 2019 FCF guidance와 dividend reset 검증.
14. [Lumen Q3 2022 results](https://ir.lumen.com/news/news-details/2022/Lumen-Technologies-reports-third-quarter-2022-results/default.aspx) — Lumen Technologies, 2022-11-02. common dividend elimination과 capital-allocation 전환 검증.

### 데이터 품질

- T0 원문·metadata: **A/B** — source SQL과 공개 VIC URL을 기준으로 했다. 공개 URL이 없는 글도 source DB 본문은 보존돼 있다.
- 사업·거래·자본구조: **A** — SEC·회사 1차자료를 우선했다.
- 가격·수익률: **C 또는 미검증** — 원 DB에 performance row가 없어 원문 회고·공시가격만 제한적으로 썼다.
- raw SQL direction은 **Short**, 실제 research direction은 위 snapshot의 매수·pair 방향이다. raw 값을 덮어쓰지 않았다.
