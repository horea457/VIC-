# Level 3 Communications (LVLT) — 2004-12-30 VIC Pair Long

> **Idea unit:** 이 게시일·증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 원 SQL 방향은 Short로 보존하고 실제 원문 방향·증권은 research layer에서 교정했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Level 3 Communications / LVLT |
| VIC 게시일 / 작성자 | 2004-12-30 / doggy835 |
| 분석 증권 / 실제 방향 | Long 6% subordinated convertible notes / Short 100 LVLT common per bond / optional Jan-2006 $7.50 calls |
| 원 SQL 방향 | Short — raw 값 보존, 실제 원문은 매수 논지 |
| 기준 진입가격 | bond just below 60; common 약 $3.45; call 약 $0.05 |
| 기대기간 | 2009~2010 bond maturity |
| raw horizon audit | maturity 또는 restructuring까지 |
| 최종 판정 | **성공 가능성 높음 — principal survival·dilution은 적중, exact pair IRR은 미검증** |

> **결론:** 회사는 bankruptcy를 피했고 6% converts를 2008~09 매입·교환한 뒤 2010 잔액 약 $111m을 만기에 갚았다. 따라서 bond survival과 equity dilution을 함께 산 구조는 논리적으로 성공 가능성이 높다. 다만 어느 6% tranche를 몇 주 short했고 tender/exchange에 어떻게 응했는지 없어 exact pair IRR은 확정하지 않는다.

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

capital structure는 secured $875m, senior unsecured $3.4bn, 6% subordinated converts $875m, debt $5.15bn, cash $850m, net debt $4.3bn, common market cap $2.35bn, TEV $6.65bn이었다. bond는 60 아래로 10%+ current yield, bond당 common 100주를 short하고 $7.50 Jan-2006 calls를 $0.05에 사 tail risk를 제한하자는 구조였다. fully diluted shares는 5년 전 360m에서 700m 이상으로 늘어 dilution을 핵심으로 봤다.

### Reverse expectations

pair는 방향중립처럼 보여도 완전 hedge가 아니다. convert delta, borrow availability·fee, coupon blockage, exchange ratio, call expiry, tender 선택이 수익을 바꾼다. bankruptcy에서 subordinated recovery가 0이고 common도 0이면 coupon과 short gain이 bond loss를 얼마나 상쇄하는지가 핵심이다.

---

## 3. 원문 투자논지 지도

### C1. 6% converts below 60은 싸다 — 성공

**원문 주장**

10%+ current yield와 par upside가 있다.

**경제적 메커니즘**

coupon·pull-to-par가 common보다 먼저 지급된다.

**T0 근거**

bond price·coupon·capital stack.

**숨은 가정**

회사 생존·coupon 지급·maturity refinancing.

**사전 반증조건**

coupon block·haircut exchange면 반증.

**실제 결과**

다수 notes가 매입·교환되고 잔액은 2010 par 상환됐다.

**정량 gap**

principal survival 확인.

**분석 오류 또는 제한**

tranche별 path를 뭉쳤다.

**재사용 교훈**

각 note를 별도 cash-flow ledger로 관리한다.

### C2. common short가 bankruptcy loss를 상쇄 — 방향 성공·수치 미검증

**원문 주장**

100주 short gain이 zero sub recovery를 메운다.

**경제적 메커니즘**

같은 EV 하락에서 residual common이 먼저 소멸한다.

**T0 근거**

원문 stress payoff -585+240+345=0.

**숨은 가정**

common entry·cover와 short 유지가 가능하다.

**사전 반증조건**

borrow recall·common squeeze면 반증.

**실제 결과**

회사 bankruptcy는 없었고 common dilution이 계속됐다.

**정량 gap**

정확한 short gain 미복원.

**분석 오류 또는 제한**

borrow friction을 제외했다.

**재사용 교훈**

short leg는 locate·fee·recall을 손익에 넣는다.

### C3. cheap call이 upside tail을 막음 — 미검증

**원문 주장**

$0.05 Jan06 $7.50 calls가 common 급등을 제한한다.

**경제적 메커니즘**

out-of-the-money option이 short convexity를 보완한다.

**T0 근거**

원문 call 가격·strike.

**숨은 가정**

급등이 option expiry 전 발생한다.

**사전 반증조건**

expiry 뒤 급등하거나 volatility repricing이면 실패.

**실제 결과**

position path와 option exercise 기록이 없다.

**정량 gap**

hedge effectiveness 미검증.

**분석 오류 또는 제한**

만기 mismatch를 작게 봤다.

**재사용 교훈**

tail hedge는 exposure horizon과 만기를 맞춘다.

### C4. dilution이 common upside를 제한 — 성공

**원문 주장**

share count 360m→700m+가 per-share value를 희석한다.

**경제적 메커니즘**

debt-for-equity가 creditor를 보호하고 common claim을 넓힌다.

**T0 근거**

원문 fully diluted share comparison.

**숨은 가정**

operating value growth가 dilution보다 작다.

**사전 반증조건**

FCF 급증이 share growth를 압도하면 반증.

**실제 결과**

이후 debt-for-equity와 convert issuance가 계속됐다.

**정량 gap**

메커니즘 확인.

**분석 오류 또는 제한**

gross shares와 economic dilution을 혼용 가능.

**재사용 교훈**

per-share EV·FCF로 dilution을 추적한다.

### C5. Chapter 11 downside도 breakeven — 미검증

**원문 주장**

zero bond recovery에서도 coupon+short가 원금을 메운다.

**경제적 메커니즘**

cross-capital-structure hedge가 tail loss를 상쇄한다.

**T0 근거**

원문 payoff table.

**숨은 가정**

coupon 4년 수령·short 100주 유지가 동시에 가능하다.

**사전 반증조건**

조기 default·coupon stop이면 반증.

**실제 결과**

Chapter 11은 발생하지 않아 stress case 자체는 시험되지 않았다.

**정량 gap**

모델 robustness 미검증.

**분석 오류 또는 제한**

default timing을 YE08로 고정했다.

**재사용 교훈**

distress payoff는 default date별로 만든다.

### C6. maturity면 큰 absolute profit — 부분 성공

**원문 주장**

common flat이면 bond+coupon에서 +715다.

**경제적 메커니즘**

bond discount와 carry가 pair 수익의 주축이다.

**T0 근거**

원문 base payoff.

**숨은 가정**

full coupon·par payment·low borrow cost.

**사전 반증조건**

discount tender·비싼 borrow면 수익 감소.

**실제 결과**

notes survival은 확인되나 tender/exchange path가 달랐다.

**정량 gap**

exact +715 미확인.

**분석 오류 또는 제한**

corporate actions를 단순 maturity로 처리했다.

**재사용 교훈**

tender consideration을 실제 cash flow로 대체한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 stress case는 YE2008 Chapter 11에서 bond -585, coupon +240, common short +345로 breakeven이다. maturity·common flat이면 +715, maturity·common 급등은 cheap call로 cap을 씌워 +310에서 call cost 25~50을 뺀다고 했다. 이는 borrow fee·margin·tax·conversion adjustment 전 payoff다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | YE08 Ch11·sub recovery 0 | 원문 거의 breakeven | bankruptcy 미발생 |
| Base | bond maturity·common flat/약세 | +715 전 비용 | principal survival·dilution |
| Bull risk | common 급등 | call hedge 후 +310 전 비용 | 경로자료 없음 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Convert price | <60 | par+coupon | 매입·교환·잔액 par 상환 | 성공 |
| Current yield | 10%+ | 지속 | coupon path issue별 상이 | 부분 |
| Common hedge | 100 shares/bond | downside 상쇄 | exact cover 없음 | 미검증 |
| Diluted shares | 700m+ vs 360m | common 압박 | debt-for-equity 지속 | 성공 |
| 2010 잔액 | 6% notes | 지급 | 약 $111m 만기상환 | 성공 |

### 촉매와 시간

판정 horizon은 **2009~2010 bond maturity**다. 이후 사건은 장기 가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2004-12-30 | VIC convert/common pair | bond <60·common short |
| 2008 | 6% converts 일부 매입 | discount exit 가능 |
| 2009 | 추가 매입 | principal 축소 |
| 2009 | 일부 새 7% convert로 교환 | cash-flow path 변경 |
| 2010 | 잔여 약 $111m 만기상환 | bond survival |
| 2011 | reverse split | 누적 dilution/가격 흔적 |

### 실제 사업·자본구조 추이

2008년 6% converts due 2009 약 $39m과 due 2010 약 $32m을 매입했고, 2009년에는 각각 약 $126m·$55m을 더 매입했다. 2010 issue 약 $142m 등은 새 7% converts $200m와 cash $78m으로 교환됐고, 2010년 남은 6% converts 약 $111m은 만기에 상환됐다. 회사는 지속적으로 debt-for-equity를 사용해 common dilution thesis도 확인했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

bond coupon·principal survival과 희석 방향은 확인된다. 하지만 정확한 issue, short entry·cover, borrow fee, call 수량·만기, tender 선택, exchange consideration이 없어 pair의 realized IRR·MFE·MAE는 계산하지 않는다.

가격 series가 없으면 수익률·MFE·MAE를 추정하지 않는다. Bond·pair는 exact issue, coupon, exchange, short borrow와 cash-flow date가 있어야 IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 6% converts below 60은 싸다 | 20% | 성공 | principal survival 확인. |
| C2 | common short가 bankruptcy loss를 상쇄 | 18% | 방향 성공·수치 미검증 | 정확한 short gain 미복원. |
| C3 | cheap call이 upside tail을 막음 | 18% | 미검증 | hedge effectiveness 미검증. |
| C4 | dilution이 common upside를 제한 | 16% | 성공 | 메커니즘 확인. |
| C5 | Chapter 11 downside도 breakeven | 16% | 미검증 | 모델 robustness 미검증. |
| C6 | maturity면 큰 absolute profit | 12% | 부분 성공 | exact +715 미확인. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익은 60 아래 bond의 coupon·pull-to-par, company survival, refinancing과 common dilution/약세에서 나왔을 가능성이 크다. 핵심은 enterprise direction을 맞히는 것이 아니라 같은 enterprise 안에서 더 싼 claim을 사고 비싼 residual을 판 것이다.

### Counterfactual

common이 급등하고 bond가 강제교환되며 short borrow가 회수됐다면 5센트 call만으로 실제 hedge를 유지할 수 있었는가?

---

## 9. 분석 오류 유형과 최초 경고

payoff table은 훌륭하지만 dynamic delta·borrow·tender path와 subordinated recovery timing을 정적으로 처리했다.

### 최초로 관찰 가능했던 경고신호

short borrow recall, conversion ratio 조정, coupon blockage 중 하나라도 발생하면 정적 arbitrage가 깨진다. 실제 liability management가 시작된 2008년부터 position-level 재계산이 필요했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

capital-structure pair는 두 다리의 cash flow와 path dependency를 함께 기록한다.

### Lesson 2

convert hedge는 고정 주식수보다 delta·borrow·corporate action이 중요하다.

### Lesson 3

정확한 issue와 tender 선택이 없으면 realized arbitrage IRR을 만들지 않는다.

### 지금 같은 아이디어를 다시 본다면

- exact note tranche
- conversion ratio
- short borrow·fee
- coupon dates
- call expiry·strike
- tender/exchange election
- margin requirements

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 생존 성공 |
| Valuation thesis | bond/common 상대가치 적중 |
| Catalyst thesis | liability management |
| Timing / path | 경로 복잡·대체로 성공 |
| Security selection | 우수 |
| Thesis score | 8.0/10 |
| Process score | 8.5/10 |
| 종합 | **성공 가능성 높음 — principal survival·dilution은 적중, exact pair IRR은 미검증** |

### 한 문장 교훈

> capital-structure pair는 두 다리의 cash flow와 path dependency를 함께 기록한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/Level_3/2370352061) — Value Investors Club / source SQL, 2004-12-30. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준.
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
