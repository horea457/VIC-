# Level 3 Communications (LVLT) — 2002-04-19 VIC Long

> **Idea unit:** 이 게시일·증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 원 SQL 방향은 Short로 보존하고 실제 원문 방향·증권은 research layer에서 교정했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Level 3 Communications / LVLT |
| VIC 게시일 / 작성자 | 2002-04-19 / nish697 |
| 분석 증권 / 실제 방향 | Level 3 bonds / Long — 원문이 여러 issue를 열거해 단일 CUSIP 미확정 |
| 원 SQL 방향 | Short — raw 값 보존, 실제 원문은 매수 논지 |
| 기준 진입가격 | 원문 YTM 약 25~35% |
| 기대기간 | 6~8년 |
| raw horizon audit | 25%+ annual return for 6~8 years 주장 |
| 최종 판정 | **성공 — bankruptcy 회피·여러 2008/2010 채무 상환, exact issue IRR은 미검증** |

> **결론:** Level 3가 파산하지 않고 2008·2010 만기채무를 실제 상환·상환전 매입했으므로 broad bond Long과 seniority 선택은 성공했다. 다만 원문이 하나의 CUSIP·매입가·coupon path를 고정하지 않아 모든 채권이 25~35% YTM으로 par 상환됐다고 일반화하거나 exact IRR을 만들 수 없다.

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

주가는 고점 대비 97% 하락한 약 $4.50, 채권은 25~35% YTM이었다. 논지는 IP dominance, optics-to-optics, dark fiber lighting에 향후 10년 $500bn 필요, outsourcing, data traffic 고성장의 다섯 전제를 바탕으로 모든 Level 3 bonds가 지급될 것이라 봤다. 2001말 debt는 secured $1.357bn, senior unsecured $3.370bn, subordinated $1.340bn, 합계 $6.067bn. cash $1.5bn+unused revolver $650m으로 $2.1bn liquidity가 있었고 2004 FCF+를 기대했다.

### Reverse expectations

25~35% YTM은 시장이 default, coercive exchange, subordination, duration을 크게 가격에 넣었다는 뜻이다. network cost $10bn은 recovery value가 아니며 dark-fiber replacement spending이 실제 수요로 전환되지 않을 수 있다. bond별 담보·만기·exchange 조건을 구분해야 한다.

---

## 3. 원문 투자논지 지도

### C1. $2.1bn liquidity가 FCF+까지 연결 — 부분 성공

**원문 주장**

cash $1.5bn과 revolver $650m이면 2004까지 버틴다.

**경제적 메커니즘**

liquidity가 burn·interest·maturity를 흡수한다.

**T0 근거**

2001말 liquidity와 burn forecast.

**숨은 가정**

revolver 가용성과 burn forecast가 유지된다.

**사전 반증조건**

liquidity runway가 2004 이전 소진되면 반증.

**실제 결과**

신규자본·discount repurchase를 병행해 bankruptcy를 피했다.

**정량 gap**

단독 liquidity보다 liability management 기여 큼.

**분석 오류 또는 제한**

static cash bridge로 봤다.

**재사용 교훈**

credit runway는 신규자본과 교환확률을 포함한다.

### C2. FCF burn이 -$2.1bn→0으로 축소 — 부분 실패

**원문 주장**

2002 <-$1bn, 2003 <-$500m, 2004 positive다.

**경제적 메커니즘**

망 완공과 매출성장이 자금수요를 줄인다.

**T0 근거**

1999~01 burn history와 원문 forecast.

**숨은 가정**

가격·고객신용·통합비가 안정된다.

**사전 반증조건**

2004에도 큰 burn이면 timing 반증.

**실제 결과**

단순 forecast보다 전환이 늦었고 debt actions가 생존을 보완했다.

**정량 gap**

timing miss, terminal survival hit.

**분석 오류 또는 제한**

operating path를 낙관했다.

**재사용 교훈**

credit는 peak funding need를 stress한다.

### C3. network value가 debt를 덮음 — 부분 성공

**원문 주장**

>$10bn 구축비가 $6.1bn debt에 recovery cushion을 준다.

**경제적 메커니즘**

strategic/reproduction value가 creditor recovery를 지지한다.

**T0 근거**

network cost와 debt stack.

**숨은 가정**

distress sale haircut 뒤에도 EV가 debt 이상이다.

**사전 반증조건**

asset sale bid가 senior claims 아래면 반증.

**실제 결과**

파산 없이 debt를 관리했고 장기 strategic sale이 성사됐다.

**정량 gap**

기업수준 방향 확인·당시 liquidation value 미확인.

**분석 오류 또는 제한**

cost와 sale value를 동일시했다.

**재사용 교훈**

recovery는 cash EBITDA와 comparable sale value를 함께 쓴다.

### C4. debt retirement가 accretive — 성공

**원문 주장**

회사가 할인채를 사면 face debt와 interest가 줄어든다.

**경제적 메커니즘**

cash 1달러로 1달러 이상 claim을 제거한다.

**T0 근거**

6개월간 face $2.1bn retirement 주장.

**숨은 가정**

현금소진보다 discount capture가 크다.

**사전 반증조건**

repurchase 뒤 liquidity가 위험수준이면 반증.

**실제 결과**

2004 83~89 매입, 이후 상환·교환이 이어졌다.

**정량 gap**

실제 liability management 확인.

**분석 오류 또는 제한**

issue별 우선순위 차이를 덜 봤다.

**재사용 교훈**

discount repurchase는 runway와 함께 평가한다.

### C5. 모든 bonds가 전액지급 — 부분 성공

**원문 주장**

25~35% YTM 채권은 모두 par로 갚힌다.

**경제적 메커니즘**

기업생존과 maturity extension이 principal을 보존한다.

**T0 근거**

원문 debt list와 liquidity.

**숨은 가정**

모든 issue가 coercive exchange 없이 동일 회수한다.

**사전 반증조건**

어느 issue라도 haircut이면 표현 반증.

**실제 결과**

여러 2008/2010 채무는 상환됐지만 일부는 교환·할인매입됐다.

**정량 gap**

broad survival 성공, all-issue literal claim 미확인.

**분석 오류 또는 제한**

security specificity 부족.

**재사용 교훈**

채권 thesis는 issue matrix가 필수다.

### C6. 25%+ annual return 6~8년 — 성과 방향 성공·수치 미검증

**원문 주장**

매입 YTM이 realized return으로 이어진다.

**경제적 메커니즘**

coupon 재투자와 par repayment가 복리수익을 만든다.

**T0 근거**

원문 quoted YTM.

**숨은 가정**

매입가·coupon·exit와 tender가 명확하다.

**사전 반증조건**

교환·조기상환·가격차이로 realized cash flow가 바뀌면 재계산.

**실제 결과**

principal survival은 확인됐으나 거래 cash-flow가 없다.

**정량 gap**

exact IRR 계산불가.

**분석 오류 또는 제한**

quoted YTM을 realized IRR로 취급할 위험.

**재사용 교훈**

수익률에는 cash-flow 날짜와 security ID를 남긴다.

---

## 4. 당시 Valuation과 Payoff Structure

1998~2001 revenue는 $392m→$515m→$1.2bn→$1.5bn으로 늘었지만 FCF는 1999 -$2.9bn, 2000 -$4.4bn, 2001 -$2.1bn이었다. 원문은 2002 burn <$1bn, 2003 <$500m, 2004 positive를 예상했다. 핵심 coverage는 $2.1bn liquidity가 inflection까지 burn·interest·maturity를 덮는지였다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | FCF 지연·exchange haircut | sub debt 손실 | issue별 일부 교환 |
| Base | liquidity bridge·할인매입 | 높은 carry+par 회수 | 여러 2008/2010 채무 상환 |
| Bull | 2004 FCF+·rerating | 25~35% YTM 온전 실현 | exact issue 미확인 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Debt stack | $6.067bn | 전액 service | bank debt·2008/2010 notes 상환/관리 | 성공 |
| Liquidity | $2.1bn | 2004까지 bridge | 신규자본·교환 병행 | 부분 |
| FCF | 2001 -$2.1bn | 2004 positive | 전환 지연 | 미달 |
| Quoted YTM | 25~35% | realized | exact issue IRR 없음 | 미검증 |
| 2008/2010 maturities | distressed | par recovery | 여러 issue 실제 지급 | 성공 |

### 촉매와 시간

판정 horizon은 **6~8년**다. 이후 사건은 장기 가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2002-04-19 | VIC bond Long | 25~35% YTM |
| 2002 | junior convert financing·discount retirements | liquidity 연장 |
| 2003 | $1.125bn secured facility 상환 | senior credit 개선 |
| 2004 | 2008 notes 83~89에 매입 | liability management |
| 2006 | 2008 notes 약 $460m 상환 | principal recovery |
| 2008 | 잔여 2008 notes 지급 | maturity 통과 |
| 2009 | 6% converts 일부 교환 | 경로 분기 |
| 2010 | 잔여 6% converts 약 $111m 만기상환 | 생존 확인 |

### 실제 사업·자본구조 추이

회사는 2002~04 할인매입과 신규자본으로 maturity를 관리했다. 2004년에는 일부 2008 notes를 83~89에 매입했고, 2006년 남은 9.125% 2008 notes 약 $398m과 10.5% 2008 notes 약 $62m을 상환했다. 2008년 남은 11% 2008 notes 약 $20m과 euro notes를 지급했다. 6% converts는 2008~09 매입·교환 후 2010년 잔액 약 $111m을 만기에 상환했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

원문이 특정 CUSIP, clean price, accrued interest, trade/exit date를 고정하지 않았다. 따라서 observed outcome은 'broad bond basket의 principal survival 성공'으로 판정하되 25~35% realized YTM, MFE·MAE는 계산하지 않는다.

가격 series가 없으면 수익률·MFE·MAE를 추정하지 않는다. Bond·pair는 exact issue, coupon, exchange, short borrow와 cash-flow date가 있어야 IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | $2.1bn liquidity가 FCF+까지 연결 | 20% | 부분 성공 | 단독 liquidity보다 liability management 기여 큼. |
| C2 | FCF burn이 -$2.1bn→0으로 축소 | 18% | 부분 실패 | timing miss, terminal survival hit. |
| C3 | network value가 debt를 덮음 | 18% | 부분 성공 | 기업수준 방향 확인·당시 liquidation value 미확인. |
| C4 | debt retirement가 accretive | 16% | 성공 | 실제 liability management 확인. |
| C5 | 모든 bonds가 전액지급 | 16% | 부분 성공 | broad survival 성공, all-issue literal claim 미확인. |
| C6 | 25%+ annual return 6~8년 | 12% | 성과 방향 성공·수치 미검증 | exact IRR 계산불가. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

성공은 network TAM보다 liquidity 확보, 할인 debt retirement, maturity extension, 신규 junior capital과 점진적 operating improvement가 만들었다. common dilution은 bondholder survival에 오히려 긍정적일 수 있었다.

### Counterfactual

같은 enterprise가 생존해도 특정 subordinated issue가 강제교환·할인 tender를 겪었다면 '모든 채권 25~35% 수익' 주장은 유지되는가?

---

## 9. 분석 오류 유형과 최초 경고

회사 생존 분석은 강했지만 여러 채권을 하나의 수익률로 묶고 Buffett association과 management ethics를 credit protection처럼 사용했다.

### 최초로 관찰 가능했던 경고신호

2004 FCF 전환이 지연되거나 $2.1bn liquidity가 예상 burn보다 빨리 줄면 핵심 반증이었다. 실제로 회사는 단순 cash burn 종료 대신 적극적 liability management를 택했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

distressed debt는 회사가 아니라 CUSIP·seniority·문서 단위로 분석한다.

### Lesson 2

equity dilution은 채권 회수율을 높일 수 있다.

### Lesson 3

replacement cost는 recovery waterfall에서 담보가능성과 매각비용을 반영한다.

### 지금 같은 아이디어를 다시 본다면

- CUSIP·매입 clean price
- seniority·guarantee
- restricted cash·revolver
- 분기 burn
- mandatory maturities
- exchange/tender terms
- coupon·exit cash-flow dates

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 장기 생존 성공 |
| Valuation thesis | 높은 YTM 보상 적중 |
| Catalyst thesis | liability management로 변경 |
| Timing / path | 대체로 성공 |
| Security selection | 채권 Long 우수·issue 모호 |
| Thesis score | 8.0/10 |
| Process score | 7.5/10 |
| 종합 | **성공 — bankruptcy 회피·여러 2008/2010 채무 상환, exact issue IRR은 미검증** |

### 한 문장 교훈

> distressed debt는 회사가 아니라 CUSIP·seniority·문서 단위로 분석한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2002-04-19. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준.
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
