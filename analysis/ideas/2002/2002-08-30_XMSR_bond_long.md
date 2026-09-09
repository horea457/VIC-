# XM Satellite Radio (XMSR) — 2002-08-30 VIC Long

> **Idea unit:** 이 게시일의 증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 사업·valuation·촉매·증권·가격경로를 분리하고 사후정보는 판정에만 사용한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | XM Satellite Radio / XMSR |
| VIC 게시일 / 작성자 | 2002-08-30 / quentin720 |
| 분석 증권 / 실제 방향 | XM 14% senior secured notes / Long |
| 원 SQL 방향 | Short — raw 값 보존, research direction은 별도 교정 |
| 기준 진입가격 | 33 cents; escrow coupon strip 후 약 26 |
| 기대기간 | 약 3.5년 / exchange·call path |
| raw horizon audit | 원문 2005 call 및 3.5년 coupon 분석 |
| 최종 판정 | **강한 성공 — security selection 적중, exact realized IRR은 경로 의존** |

> **결론:** 14% secured notes를 33, escrow된 두 coupon을 빼면 약 26에 매수하는 아이디어였다. 2003 exchange는 $1,000 face당 $1,459 maturity principal의 신규 14% secured discount notes, $70 cash, 85 warrants를 제공했고 $300.2m가 참여했다. 2006 XM은 일부 notes를 premium cash로 repurchase/redeem했다. exact IRR은 tender·warrant 매도경로가 없어 계산하지 않지만 payoff 구조는 강하게 적중했다.

---

## 1. 회사는 정확히 무엇을 하는가

XM Satellite Radio는 위성·지상 중계망으로 전국 유료 오디오를 제공하고 자동차 OEM·딜러를 통해 가입자를 획득한 초기 위성라디오 사업자였다. 이 아이디어의 대상은 common이 아니라 14% senior secured notes다. 가입자 증가가 기업가치를 만들더라도 채권 수익은 escrow coupon, 담보, exchange ratio, 신주·warrant, refinancing 순서로 결정된다.

채권 현금엔진은 `escrow coupon + cash coupon/accretion + exchange consideration + warrant value + recovery - 매입가격 - carry/transaction cost`다. enterprise 성공과 특정 채권의 realized IRR은 별개다.

### 가치사슬과 security payoff

청취자·차량 OEM·광고주 또는 가입자가 만든 gross economics가 station/platform 비용, royalty·content, corporate cost, cash interest, capex, tax를 통과한 뒤 common에 귀속된다. 채권 아이디어는 여기에 담보·seniority·exchange consideration·recovery를 적용한다. 매출 성장, enterprise value 증가, 해당 security 수익을 같은 사건으로 취급하지 않는다.

### 매 분기 볼 핵심 KPI

가입자·SAC·churn·OEM conversion, 월 cash burn, funding need, 담보·seniority, exchange participation, new-money terms, warrant strike, 실제 redemption price

---

## 2. 당시 상황과 시장이 가격에 넣은 것

XM은 가입자 증가 전 막대한 자금이 필요한 위성라디오 startup이었다. $350m 14% senior secured notes와 $125m convert subordinated가 있었고, 원문은 전체 funding need 약 $525m 또는 debt equitization 시 $350m을 추정했다. 두 coupon이 escrow돼 있어 33 price에서 economic at-risk price를 약 26으로 봤다.

### Reverse expectations

기업이 성공해도 common dilution과 추가자금은 불가피했다. 채권 Long의 핵심은 파산회피 그 자체가 아니라 신규자금 제공자가 기존 secured creditor를 어떤 비율로 교환·보호하는지였다. 담보가 약하거나 exchange coercion이 value를 이전하면 26이 싸지 않을 수 있었다.

---

## 3. 원문 투자논지 지도

### C1. stripped cost 약 26은 recovery 대비 싸다 — 성공

**원문 주장**

33 price에서 두 escrow coupon을 빼면 실질 위험자본은 약 26이다.

**경제적 메커니즘**

확정 coupon이 초기 cost basis를 회수한다.

**T0 근거**

coupon escrow 구조.

**숨은 가정**

escrow가 bankruptcy remote하고 제때 지급된다.

**사전 반증조건**

escrow 접근불가 또는 recovery 26 미만이면 반증.

**실제 결과**

exchange에서 cash·new notes·warrants를 수령.

**정량 gap**

회수 package가 stripped cost를 크게 초과한 방향.

**분석 오류 또는 제한**

exact coupon timing IRR은 미복원.

**재사용 교훈**

표면가격과 net-at-risk를 분리한다.

### C2. 14% secured seniority가 협상력을 준다 — 성공

**원문 주장**

new money는 secured creditors를 무시하기 어렵다.

**경제적 메커니즘**

담보·우선순위가 restructuring value allocation을 지킨다.

**T0 근거**

14% senior secured status.

**숨은 가정**

담보가 충분하고 priming이 제한된다.

**사전 반증조건**

무보상 priming이면 반증.

**실제 결과**

$300.2m이 유리한 secured exchange에 참여.

**정량 gap**

우선순위가 consideration으로 전환.

**분석 오류 또는 제한**

담보 coverage exact appraisal는 부족.

**재사용 교훈**

seniority는 문구가 아니라 recovery waterfall로 검증한다.

### C3. 2005 call까지 coupon+107 payoff — 부분 성공

**원문 주장**

49 points coupon과 107 call이 큰 수익을 만든다.

**경제적 메커니즘**

funding 후 contractual cash flow가 price discount를 닫는다.

**T0 근거**

indenture coupon/call terms.

**숨은 가정**

회사에 현금이 생겨 notes를 유지·상환한다.

**사전 반증조건**

exchange가 불리하거나 default recovery가 낮으면 반증.

**실제 결과**

실제 path는 2003 exchange 후 2006 premium redemption.

**정량 gap**

정확한 경로는 달랐지만 premium cash realization.

**분석 오류 또는 제한**

base path와 event path를 혼용했다.

**재사용 교훈**

bond target은 hold·exchange·default 시나리오를 분리한다.

### C4. debt equitization도 upside — 성공

**원문 주장**

신규 $350m이 78%를 가져가도 notes buyer가 equity를 싸게 받는다.

**경제적 메커니즘**

낮은 debt price가 post-money equity claim으로 전환된다.

**T0 근거**

원문 post-money common $1.5bn vs notes $451m.

**숨은 가정**

enterprise value가 funding 후 유지된다.

**사전 반증조건**

과도한 dilution·낮은 warrant value면 반증.

**실제 결과**

실제 exchange는 new secured notes+cash+warrants였다.

**정량 gap**

순수 equity swap보다 더 creditor-friendly.

**분석 오류 또는 제한**

낙관적 enterprise value에 의존했다.

**재사용 교훈**

restructuring security mix를 option별로 가격화한다.

### C5. $225m+ funding이 runway를 만든다 — 성공

**원문 주장**

필요자금 유치로 liquidation을 피한다.

**경제적 메커니즘**

new money와 GM concession이 cash burn을 견딜 시간을 산다.

**T0 근거**

$525m gross need/$350m restructured need 추정.

**숨은 가정**

OEM support와 capital market access가 유지된다.

**사전 반증조건**

필요자금 부족으로 즉시 filing이면 반증.

**실제 결과**

$225m gross new money와 $250m GM obligations restructuring.

**정량 gap**

두 축의 funding gap 완화.

**분석 오류 또는 제한**

funding need 추정범위가 넓었다.

**재사용 교훈**

cash runway는 new money와 liability concession을 함께 본다.

### C6. 20m 시장·XM 50%가 terminal value를 지지 — 부분 성공

**원문 주장**

XM EBIT $301m·10배=$3bn을 제시했다.

**경제적 메커니즘**

subscriber scale이 고정 위성비를 흡수한다.

**T0 근거**

SAC $100·70% variable margin·1.5% churn model.

**숨은 가정**

OEM conversion과 churn이 forecast를 따른다.

**사전 반증조건**

가입자 economics 악화·추가자본이 value를 소진하면 약화.

**실제 결과**

XM은 생존해 2008 Sirius와 합병했지만 exact forecast 검증은 별개다.

**정량 gap**

방향 성공·수치 미검증.

**분석 오류 또는 제한**

enterprise bull case를 bond safety와 섞었다.

**재사용 교훈**

채권 thesis는 terminal equity forecast 없이도 성립해야 한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 coupon path는 약 3.5년 동안 49 points와 2005-03 call 107이었다. 더 가능성 높은 debt-to-equity에서 새 $350m이 최대 78%를 가져가도 notes buyer가 implied equity를 싸게 받는다고 봤다. 20m satellite-radio subs의 50%와 XM EBIT $301m·10배=$3bn은 enterprise upside를 설명했지만 bond margin of safety는 seniority와 exchange terms에서 나왔다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | funding 실패·low recovery | 26 principal loss | 회피 |
| Base | secured exchange+new money | cash·new notes·warrants | 2003 현실화 |
| Bull | coupon+107 call | 매우 높은 IRR | 일부 premium redemption |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Note price | 33 / stripped 약 26 | recovery 상회 | 유리한 exchange·redemption | 성공 |
| Old notes exchanged | $325m 대상 | 높은 참여 | $300.2m | 92.4% |
| Exchange per $1,000 | equity 가능 | value 보호 | $1,459 maturity principal+$70+85 warrants | 성공 |
| New money | $225m 필요축 | funding | $225m gross | 성공 |
| 2006 redemption | 107 call 경로 | premium realization | $186.5m maturity value에 $209.6m incl interest | 성공 |

### 촉매와 시간

판정 horizon은 **약 3.5년 / exchange·call path**다. 이후 사건은 장기 사업가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2002-08-30 | VIC bond Long | 33·stripped 26 |
| 2003-01-28 | financing/exchange | $300.2m 참여 |
| 2003-03-15 | new-note accretion 기준 | $1,000 value |
| 2004~2005 | 일부 exchanges | liability management 지속 |
| 2006 | repurchase/redemption | $209.6m incl interest |
| 2007-02-19 | Sirius merger 발표 | enterprise 생존 |
| 2008-07-28 | merger 완료 | 산업구조 통합 |

### 실제 사업·자본구조 추이

2003-01-28 financing에서 $325m old notes 중 $300.2m이 exchange됐다. $1,000 face당 $1,459 maturity principal의 신규 14% secured discount notes(2003-03-15 accreted value $1,000), $70 cash, 85 warrants($3.18 strike)를 받았다. GM obligations $250m도 재구조화했고 $225m gross new money를 조달했다. 2006에는 $148.7m carrying/$186.5m maturity value notes를 $209.6m(이자 포함)에 repurchase/redeem했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

표준 채권가격·coupon receipt·warrant sale series가 없어 realized IRR을 단일 숫자로 만들지 않는다. 33 매입, escrow strip 후 26 exposure, 2003 exchange consideration과 2006 premium redemption은 큰 positive payoff를 지지한다. 참여 여부와 warrant 처분일에 따라 투자자별 IRR은 달라진다.

가격 series는 배당·세금·거래비용을 포함한 total return과 분리한다. 데이터가 없으면 수익률·MFE·MAE를 추정하지 않는다. Short는 entry·cover·borrow, bond는 coupon·exchange·warrant 수령일이 있어야 exact IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | stripped cost 약 26은 recovery 대비 싸다 | 20% | 성공 | 회수 package가 stripped cost를 크게 초과한 방향. |
| C2 | 14% secured seniority가 협상력을 준다 | 18% | 성공 | 우선순위가 consideration으로 전환. |
| C3 | 2005 call까지 coupon+107 payoff | 18% | 부분 성공 | 정확한 경로는 달랐지만 premium cash realization. |
| C4 | debt equitization도 upside | 16% | 성공 | 순수 equity swap보다 더 creditor-friendly. |
| C5 | $225m+ funding이 runway를 만든다 | 16% | 성공 | 두 축의 funding gap 완화. |
| C6 | 20m 시장·XM 50%가 terminal value를 지지 | 12% | 부분 성공 | 방향 성공·수치 미검증. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익의 원천은 위성라디오 subscriber forecast의 정확성보다 secured position과 new-money negotiation이었다. GM restructuring과 $225m 자금조달이 liquidation을 피하게 했고, coercive exchange가 오히려 principal accretion·cash·warrant를 제공했다. common 대신 debt를 산 security selection이 핵심이다.

### What was right / What was wrong

**맞았던 것:** 생존·합병와 관련된 관찰은 유효했다. **틀렸던 것:** 20m subs·$301m EBIT·10배 valuation은 매우 낙관적이었고 exact bond IRR을 이를 통해 정당화할 필요가 없었다. 더 강한 논지는 담보·escrow·exchange bargaining만으로 구성할 수 있었다.

### Counterfactual

XM common의 dilution이 훨씬 컸더라도 secured-note exchange consideration이 동일했다면 bond thesis는 여전히 성공인가? 그렇다. 두 증권의 payoff를 분리해야 한다.

---

## 9. 분석 오류 유형과 최초 경고

20m subs·$301m EBIT·10배 valuation은 매우 낙관적이었고 exact bond IRR을 이를 통해 정당화할 필요가 없었다. 더 강한 논지는 담보·escrow·exchange bargaining만으로 구성할 수 있었다.

### 최초로 관찰 가능했던 경고신호

반증경보는 new-money가 secured notes보다 선순위로 들어오거나 exchange recovery가 stripped cost 26 아래로 제시되는 것이었다. 실제로는 반대였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

distress에서는 좋은 회사보다 좋은 security를 찾는다.

### Lesson 2

escrow coupon은 purchase price에서 분리해 true capital-at-risk를 계산한다.

### Lesson 3

exchange IRR은 각 consideration의 수령일·market value로 계산하고 임의 합산하지 않는다.

### 지금 같은 아이디어를 다시 본다면

- 담보범위
- escrow coupon
- new-money seniority
- exchange participation
- warrant strike
- maturity principal/accretion
- call/redemption price

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 생존·합병 |
| Valuation thesis | 채권 payoff 성공 |
| Catalyst thesis | 2003 exchange 성공 |
| Timing / path | 성공 |
| Security selection | 탁월 |
| Thesis score | 8.5/10 |
| Process score | 8.5/10 |
| 종합 | **강한 성공 — security selection 적중, exact realized IRR은 경로 의존** |

### 한 문장 교훈

> distress에서는 좋은 회사보다 좋은 security를 찾는다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/XM_Satellite_Radio/1329667940) — Value Investors Club / source SQL, 2002-08-30. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준. SGA 2010은 본문이 누락되어 가격 series와 2019 동일 작성자 회고만 사용.
2. [XM exchange offer](https://www.sec.gov/Archives/edgar/data/1091530/000095010902006334/dex991.htm) — SEC / XM, 2002. 교환조건과 신규자금 구조 검증.
3. [XM 2004 Form 10-K](https://www.sec.gov/Archives/edgar/data/1091530/000119312505042835/d10k.htm) — SEC / XM, 2005. 2003 exchange 참여액·GM restructuring·new money 검증.
4. [XM 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/1091530/000119312507044379/d10k.htm) — SEC / XM, 2007. 14% notes repurchase·redemption 금액 검증.
5. [XM/Sirius merger announcement](https://investor.siriusxm.com/sec-filings/sirius-xm-holdings-inc/content/0000950123-07-003042/0000950123-07-003042.pdf) — SEC / Sirius XM, 2007-02-19. 합병 발표 검증.
6. [FCC XM/Sirius merger docket](https://www.fcc.gov/proceedings-actions/mergers-transactions/xm-and-sirius) — FCC, 2008. 규제심사와 합병 승인 검증.
7. [XM/Sirius merger completion](https://www.sec.gov/Archives/edgar/data/908937/000095012308009301/y65279exv99w1.htm) — SEC / Sirius XM, 2008-07-29. 거래 종결 검증.

### 데이터 품질

- T0 원문·metadata: **A/B** — source SQL과 공개 VIC URL을 기준으로 했다. SGA 2010은 body가 없어 claim reconstruction을 명시적으로 낮은 신뢰도로 처리했다.
- 사업·거래·자본구조: **A** — SEC·회사·CRB·FCC 1차자료를 우선했다.
- 가격경로: **B/C 또는 미검증** — 원 DB가 보존한 SGA ratio만 수치화했다. 배당 포함 여부가 불명확해 현금배당을 중복 가산하지 않았다.
- raw SQL direction은 **Short**, 본문 실제 research direction은 **Long**다. 둘을 덮어쓰지 않고 나란히 보존했다.
