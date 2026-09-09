# Level 3 Communications (LVLT) — 2003-03-17 VIC Long

> **Idea unit:** 이 게시일·증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 원 SQL 방향은 Short로 보존하고 실제 원문 방향·증권은 research layer에서 교정했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Level 3 Communications / LVLT |
| VIC 게시일 / 작성자 | 2003-03-17 / jon64 |
| 분석 증권 / 실제 방향 | $1.125bn senior secured purchase-money bank debt / Long |
| 원 SQL 방향 | Short — raw 값 보존, 실제 원문은 매수 논지 |
| 기준 진입가격 | 약 83; L+325~450 |
| 기대기간 | 3.5~4.5년 maturity |
| raw horizon audit | 원문 12% unlevered·20%+ 2:1 levered |
| 최종 판정 | **강한 성공 — 2003년 facility 전액상환** |

> **결론:** 83에 매입한 $1.125bn senior secured facility는 회사가 2003년에 현금·restricted cash와 신규 10.75% notes proceeds로 전액상환했다. 원문의 3.5~4.5년보다 빨리 credit event가 해소돼 security selection은 강하게 성공했다. 정확한 settlement date·coupon carry가 없어 12%/levered IRR은 재계산하지 않는다.

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

원문은 $1.125bn outstanding, 최대 $1.275bn의 purchase-money senior secured bank debt를 83에 매수해 L+325~450, 약 12% unlevered yield를 제시했다. minimum cash covenant $400~500m이 약 31c coverage, noncore software resale 사업 $60m EBITDA를 $350~450m으로 평가해 약 30c, core post-Genuity EBITDA $550~650m을 더해 3~4x coverage를 주장했다. Genuity는 $130m+약 $50m burn으로 샀고 $660m run-rate revenue의 margin을 30%→64%→80%로 높일 것으로 봤다.

### Reverse expectations

가격 83은 secured claim인데도 refinancing·cash-burn·담보가치 불확실성을 반영했다. 3~4x coverage는 software resale valuation과 예상 EBITDA를 합친 going-concern 수치라 liquidation coverage가 아니다. leverage를 얹으면 recovery는 같아도 margin-call과 funding risk가 추가된다.

---

## 3. 원문 투자논지 지도

### C1. secured debt가 3~4x covered — 성공

**원문 주장**

cash·resale·core value가 claim을 여러 번 덮는다.

**경제적 메커니즘**

담보와 seniority가 downside recovery를 높인다.

**T0 근거**

$400~500m cash covenant, resale $350~450m, core EBITDA.

**숨은 가정**

going-concern values가 stress에서도 유지된다.

**사전 반증조건**

coverage가 1x 아래면 반증.

**실제 결과**

facility는 2003년 par 전액상환됐다.

**정량 gap**

recovery 100% 직접 확인.

**분석 오류 또는 제한**

coverage 구성요소 중복 가능성.

**재사용 교훈**

recovery bridge는 중복 없는 자산·현금으로 만든다.

### C2. Genuity 인수가 EBITDA를 만든다 — 미검증/비핵심

**원문 주장**

$180m 이하 투입으로 $200~300m EBITDA를 얻는다.

**경제적 메커니즘**

망 통합과 access-cost 절감이 margin을 30→64→80%로 높인다.

**T0 근거**

$660m run-rate revenue와 synergy estimate.

**숨은 가정**

customer churn과 integration cost가 낮다.

**사전 반증조건**

margin·revenue가 계획보다 크게 낮으면 반증.

**실제 결과**

상환은 Genuity 완전 정상화 전에 refinancing으로 이뤄졌다.

**정량 gap**

credit 성공의 필요조건이 아니었음.

**분석 오류 또는 제한**

extreme margin을 base에 넣었다.

**재사용 교훈**

security payoff의 필수·보조 claim을 구분한다.

### C3. cash covenant가 31c floor — 성공

**원문 주장**

$400~500m minimum cash가 principal 일부를 보호한다.

**경제적 메커니즘**

covenant breach 전 lender가 통제권·remedy를 얻는다.

**T0 근거**

원문 covenant와 principal.

**숨은 가정**

cash가 unrestricted이며 lender가 선순위 접근 가능하다.

**사전 반증조건**

waiver·restricted cash면 haircut.

**실제 결과**

cash·restricted cash가 실제 takeout 재원에 포함됐다.

**정량 gap**

floor mechanism 확인.

**분석 오류 또는 제한**

covenant cash와 recovery cash를 동일시할 위험.

**재사용 교훈**

현금의 법적 가용성과 pledge를 확인한다.

### C4. resale 사업이 약 30c coverage — 미검증

**원문 주장**

$60m EBITDA 사업이 $350~450m 가치다.

**경제적 메커니즘**

비핵심 매각이 secured debt를 줄일 수 있다.

**T0 근거**

원문 EBITDA·multiple.

**숨은 가정**

분리가능하고 buyer·tax leakage가 작다.

**사전 반증조건**

매각불가·multiple 압축이면 반증.

**실제 결과**

직접 매각회수보다 refinancing이 facility를 갚았다.

**정량 gap**

30c valuation은 직접 검증되지 않음.

**분석 오류 또는 제한**

예상 asset sale을 현금처럼 합산했다.

**재사용 교훈**

coverage는 realizability·tax·timing haircut을 둔다.

### C5. 83 매입은 12% unlevered — 성공·수치 제한

**원문 주장**

coupon과 par accretion으로 연 12%를 번다.

**경제적 메커니즘**

floating coupon과 17-point pull-to-par가 수익을 만든다.

**T0 근거**

83 price, L+325~450, 3.5~4.5년.

**숨은 가정**

par repayment와 coupon 전액지급.

**사전 반증조건**

haircut·payment block이면 반증.

**실제 결과**

par 전액상환 확인.

**정량 gap**

exact carry/date 없어 IRR 미확인.

**분석 오류 또는 제한**

headline yield만 남길 위험.

**재사용 교훈**

bond return은 cash-flow 날짜로 검산한다.

### C6. 2:1 leverage로 20%+ — 미검증

**원문 주장**

은행채권을 차입해 equity IRR을 높인다.

**경제적 메커니즘**

asset yield와 funding spread 차이가 equity return을 증폭한다.

**T0 근거**

원문 leverage illustration.

**숨은 가정**

financing이 maturity까지 유지되고 margin call이 없다.

**사전 반증조건**

haircut·repo rate 상승이면 thesis 훼손.

**실제 결과**

asset은 par 상환됐지만 financing record가 없다.

**정량 gap**

levered realized IRR 미검증.

**분석 오류 또는 제한**

회수성공을 레버리지 성공으로 일반화할 수 없다.

**재사용 교훈**

financing terms 없는 levered IRR은 확정하지 않는다.

---

## 4. 당시 Valuation과 Payoff Structure

unlevered payoff는 par accretion 17포인트+floating coupon이다. maturity까지 약 4년이면 단순 price accretion만 연 4.8% 수준이고 coupon을 더해 약 12% 주장에 접근한다. 다만 실제 조기상환일·LIBOR fixing·accrued interest가 없어 exact IRR을 만들지 않는다. 2:1 leverage의 20%+는 repo rate·haircut·margin call을 차감해야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | refinancing 실패·담보가치 하락 | 83 아래 recovery | 미발생 |
| Base | new notes·cash로 takeout | coupon+17pt accretion | 2003 전액상환 |
| Bull | 빠른 상환+2:1 leverage | 20%+ 주장 | exact IRR 미확인 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 매입가/상환 | 약 83 | par | 2003 전액상환 | 성공 |
| Principal | $1.125bn | covered | 전액상환 | 성공 |
| Coupon | L+325~450 | 지급 | exact cash dates 없음 | 제한 |
| Unlevered return | 약 12% 주장 | 실현 | 방향 성공·IRR 미확인 | 제한 |
| Genuity EBITDA | $200~300m 예상 | margin 80% | payoff에 불필요 | 미검증 |

### 촉매와 시간

판정 horizon은 **3.5~4.5년 maturity**다. 이후 사건은 장기 가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2003-03-17 | VIC bank debt Long | 83·12% unlevered |
| 2003 | 10.75% senior notes 조달 | secured takeout 재원 |
| 2003 | $1.125bn facility 전액상환 | security payoff 성공 |
| 2004 | 다른 2008 notes 할인매입 | credit 개선 지속 |
| 2006 | 2008 notes redemption | maturity 관리 |
| 2011 | Global Crossing 결합 | enterprise 생존 |

### 실제 사업·자본구조 추이

Level 3는 2003년에 cash·restricted cash와 신규 10.75% senior notes proceeds를 사용해 $1.125bn purchase-money Senior Secured Credit Facility를 전액상환했다. 이는 enterprise turnaround를 기다리지 않고 해당 senior claim이 현금으로 회수된 직접적 security outcome이다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

83 매입, par repayment라는 방향은 확인된다. 그러나 exact purchase settlement, floating coupon cash dates, repayment date와 leverage financing cost가 없어 unlevered 12% 및 levered 20%+ IRR은 수치 확정하지 않는다.

가격 series가 없으면 수익률·MFE·MAE를 추정하지 않는다. Bond·pair는 exact issue, coupon, exchange, short borrow와 cash-flow date가 있어야 IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | secured debt가 3~4x covered | 20% | 성공 | recovery 100% 직접 확인. |
| C2 | Genuity 인수가 EBITDA를 만든다 | 18% | 미검증/비핵심 | credit 성공의 필요조건이 아니었음. |
| C3 | cash covenant가 31c floor | 18% | 성공 | floor mechanism 확인. |
| C4 | resale 사업이 약 30c coverage | 16% | 미검증 | 30c valuation은 직접 검증되지 않음. |
| C5 | 83 매입은 12% unlevered | 16% | 성공·수치 제한 | exact carry/date 없어 IRR 미확인. |
| C6 | 2:1 leverage로 20%+ | 12% | 미검증 | levered realized IRR 미검증. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익의 직접 driver는 높은 담보순위, par까지 17포인트 discount, 회사의 refinancing 능력과 신규 unsecured capital이었다. Genuity margin 80%나 2004 FCF+가 완전히 실현돼야만 회수되는 구조가 아니었다.

### Counterfactual

Genuity synergy가 실패해도 신규 unsecured 자본으로 secured facility를 par 상환할 수 있다면 가장 중요한 thesis는 enterprise turnaround인가 seniority/refinancing인가?

---

## 9. 분석 오류 유형과 최초 경고

원문은 좋은 security를 골랐지만 going-concern asset values를 단순 합산했고 2:1 leverage의 financing·margin-call risk를 작게 다뤘다.

### 최초로 관찰 가능했던 경고신호

minimum cash covenant 하회 또는 10.75% notes 발행 실패가 즉시 반증이었으나, 실제로 refinancing이 먼저 성사됐다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

distress에서 좋은 회사보다 먼저 갚히는 증권을 찾는다.

### Lesson 2

senior claim은 equity FCF가 아니라 refinancing capacity로도 상환된다.

### Lesson 3

levered bond IRR은 asset yield와 funding·margin-call risk를 분리한다.

### 지금 같은 아이디어를 다시 본다면

- facility principal
- collateral·guarantee
- cash covenant
- new-money issuance
- restricted cash
- coupon fixing
- exact repayment date

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 일부 불필요·방향 적중 |
| Valuation thesis | 83→par 적중 |
| Catalyst thesis | refinancing 조기 성공 |
| Timing / path | 예상보다 빠른 성공 |
| Security selection | 탁월 |
| Thesis score | 9.0/10 |
| Process score | 8.5/10 |
| 종합 | **강한 성공 — 2003년 facility 전액상환** |

### 한 문장 교훈

> distress에서 좋은 회사보다 먼저 갚히는 증권을 찾는다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/Level_3_Bank_Debt/9040413468) — Value Investors Club / source SQL, 2003-03-17. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준.
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
