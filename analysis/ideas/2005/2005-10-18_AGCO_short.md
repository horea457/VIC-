# AGCO Corporation (AG) — 2005-10-18 VIC Short

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AGCO Corporation / AG |
| VIC 게시일 / 작성자 | 2005-10-18 / chris815 |
| 분석 증권 / 실제 방향 | NYSE:AGCO common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 $16 |
| 기대기간 | 12~24개월 rate·farm-cost pressure |
| raw horizon audit | EV $2.6bn vs adjusted EV 약 $5bn; 86% variable-rate debt, higher LIBOR·energy·fertilizer |
| 최종 판정 | **강한 실패 — ag upcycle이 leverage·rate headwind를 압도** |

> **결론:** 약 $16 short 뒤 2006말 약 $31, 2007말 약 $68로 올랐다. 86% variable-rate debt, higher LIBOR·energy·fertilizer는 실제 위험이었지만 farm income·commodity cycle, product mix와 operating leverage를 압도하지 못했다. 약 325% adverse price move는 명확한 trade failure다.

---

## 1. 회사는 정확히 무엇을 하는가

AGCO는 Massey Ferguson·Fendt·Valtra·Challenger 등의 농기계와 부품을 전 세계 dealer망을 통해 판다. farmer income·crop price·금리와 dealer inventory가 장비수요를, volume·mix·공장가동률·working capital과 finance JV가 equity cash flow를 결정한다.

units×price/mix + parts - material·labour·warranty - SG&A/R&D - interest - tax - capex ± working capital = equity cash; finance-JV exposure와 pension을 함께 stress한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

retail units, dealer inventory, crop/farmer income, price/mix, gross margin, working capital, finance receivables, pension, net debt, EPS

---

## 2. 당시 상황과 시장이 가격에 넣은 것

headline EV 약 $2.6bn에 finance-company exposure와 pension·dealer financing 등을 더하면 adjusted EV가 약 $5bn이고, debt의 86%가 variable rate라 LIBOR 상승이 earnings를 훼손한다는 논지였다. energy·fertilizer 상승도 farmer 구매력을 낮춘다고 봤다.

### Reverse expectations

시장은 높은 crop prices·farm income과 replacement demand가 장비 가격·volume을 끌어올리고 Fendt·Massey·Valtra franchise가 fixed-cost leverage를 만든다고 봤다. financing은 risk이면서 동시에 dealer/customer sales를 지탱하는 distribution asset이었다.

---

## 3. 원문 투자논지 지도

### C1. adjusted EV 약 $5bn — 실패

**원문 주장**

finance·pension 등을 더하면 headline $2.6bn보다 훨씬 비싸다.

**경제적 메커니즘**

hidden claims가 equity의 enterprise cushion을 줄인다.

**T0 근거**

원문 balance-sheet adjustments.

**숨은 가정**

claims가 recourse이고 상쇄 assets·income이 적다.

**사전 반증조건**

finance book이 self-funding·profitable이면 약화.

**실제 결과**

distress 없이 cycle을 통과하고 equity가 급등했다.

**정량 gap**

terminal value 반증.

**분석 오류 또는 제한**

gross liabilities를 EV에 중복 합산했다.

**재사용 교훈**

recourse·assets·earnings을 net으로 분류한다.

### C2. 86% variable-rate debt — mechanism 적중·trade 실패

**원문 주장**

LIBOR 상승이 interest expense를 크게 높인다.

**경제적 메커니즘**

floating debt×rate change가 pretax earnings를 낮춘다.

**T0 근거**

원문 86% exposure.

**숨은 가정**

hedges·debt paydown·operating profit이 상쇄 못한다.

**사전 반증조건**

EBIT growth가 interest를 압도하면 반증.

**실제 결과**

rate headwind에도 stock은 $16→$68였다.

**정량 gap**

price thesis 완전 반대.

**분석 오류 또는 제한**

sensitivity를 total EPS bridge 없이 사용했다.

**재사용 교훈**

EBIT·interest 동시 sensitivity를 만든다.

### C3. energy·fertilizer가 farmer demand를 훼손 — 실패

**원문 주장**

input inflation이 equipment affordability를 낮춘다.

**경제적 메커니즘**

farm margin 감소가 capex를 지연한다.

**T0 근거**

당시 energy·fertilizer 상승.

**숨은 가정**

crop revenue가 cost 상승을 못 따라간다.

**사전 반증조건**

crop prices·farm income 상승이면 반증.

**실제 결과**

commodity boom이 equipment demand를 강화했다.

**정량 gap**

direction 반대.

**분석 오류 또는 제한**

cost만 보고 output price를 빠뜨렸다.

**재사용 교훈**

farm gross margin을 통합 변수로 본다.

### C4. sales·margin pressure — 실패

**원문 주장**

macro·integration이 operating earnings를 낮춘다.

**경제적 메커니즘**

lower units가 fixed-cost deleverage를 만든다.

**T0 근거**

2005 cycle concern.

**숨은 가정**

dealer inventory가 높고 retail 약세다.

**사전 반증조건**

sales·pricing·mix 개선이면 반증.

**실제 결과**

2005 sales가 유지되고 이후 upcycle이 operating leverage를 만들었다.

**정량 gap**

예상과 반대.

**분석 오류 또는 제한**

cycle bottom을 연장했다.

**재사용 교훈**

retail/wholesale와 inventory를 분리한다.

### C5. valuation compression — 강한 실패

**원문 주장**

높은 adjusted EV가 equity multiple을 낮춘다.

**경제적 메커니즘**

earnings miss와 risk premium이 price를 누른다.

**T0 근거**

$16 entry.

**숨은 가정**

cycle earnings가 늘지 않는다.

**사전 반증조건**

$25 이상이면 반증.

**실제 결과**

2006 ~$31, 2007 ~$68.

**정량 gap**

+94%, +325% adverse.

**분석 오류 또는 제한**

upside scenario가 없었다.

**재사용 교훈**

short target과 max-loss를 함께 둔다.

### C6. 12~24개월 catalyst — 실패

**원문 주장**

rates·input costs가 빠르게 실적에 반영된다.

**경제적 메커니즘**

quarterly EPS misses가 rerating을 촉발한다.

**T0 근거**

macro conditions.

**숨은 가정**

farm boom이 상쇄하지 않는다.

**사전 반증조건**

2006 earnings·price 강세면 실패.

**실제 결과**

2006말 주가가 거의 두 배였다.

**정량 gap**

horizon 내 반증.

**분석 오류 또는 제한**

macro exposure를 dated company catalyst로 봤다.

**재사용 교훈**

catalyst에는 company-specific milestone이 필요하다.

---

## 4. 당시 Valuation과 Payoff Structure

reported EV와 finance receivables·nonrecourse debt·JV guarantees를 무조건 합산하지 않고 exposure별 expected loss와 earnings contribution을 분리해야 한다. rate sensitivity와 farm-income upside를 EPS bridge에 함께 넣고 short의 stop/MAE를 정해야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for short | farm boom·pricing | $30~70 | 2006~07 실현 |
| Base | rates offset demand | $14~20 | 미실현 |
| Bull for short | farmer squeeze·credit stress | $8~12 | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / 2006 | $16 | 하락 | ~$31 | 93.8% adverse |
| 2007 price | entry 이하 | short profit | ~$68 | 325% adverse |
| 2005 sales | $5.45bn | pressure | $5.450bn | 안정 |
| Variable-rate debt | 86% | interest shock | cycle이 상쇄 | driver miss |
| Adjusted EV | ~$5bn | equity 압박 | distress 없음 | 분류 오류 |

### 촉매와 시간

판정 horizon은 **12~24개월 rate·farm-cost pressure**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2005-10-18 | VIC Short | ~$16 |
| 2005-12-31 | sales $5.450bn | 수요 안정 |
| 2006-H1 | rates·inputs 상승 | 예상 headwind |
| 2006-H2 | farm-income 개선 | cycle offset |
| 2006-12-31 | stock ~$31 | cover signal |
| 2007-H1 | commodity boom | equipment demand |
| 2007-H2 | operating leverage | earnings rerating |
| 2007-12-31 | stock ~$68 | 강한 실패 |

### 실제 사업·자본구조 추이

2005 sales는 $5.450bn으로 2004 $5.273bn 수준을 유지했다. 이후 agriculture upcycle, farm economics와 product demand가 강해지며 stock은 2006말 약 $31, 2007말 약 $68로 상승했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

$16→$31은 약 93.8% adverse, $16→$68은 약 325% adverse price move다. short borrow·cover가 없으므로 exact realized P&L은 제시하지 않지만 thesis 실패 여부는 명확하다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | adjusted EV 약 $5bn | 20% | 실패 | terminal value 반증. |
| C2 | 86% variable-rate debt | 18% | mechanism 적중·trade 실패 | price thesis 완전 반대. |
| C3 | energy·fertilizer가 farmer demand를 훼손 | 18% | 실패 | direction 반대. |
| C4 | sales·margin pressure | 16% | 실패 | 예상과 반대. |
| C5 | valuation compression | 16% | 강한 실패 | +94%, +325% adverse. |
| C6 | 12~24개월 catalyst | 12% | 실패 | horizon 내 반증. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

rate와 input-cost headwind보다 crop/farm cash-flow tailwind가 훨씬 컸다. adjusted EV 논리는 liabilities를 포착했지만 cyclic earnings power와 finance assets의 상쇄를 빠뜨렸다.

### Counterfactual

corn·soy prices와 farm income이 급등할 때 LIBOR +200bp가 장비 수요·pricing·margin에 주는 순효과는 정말 음수인가?

---

## 9. 분석 오류 유형과 최초 경고

rate·fertilizer·leverage를 각각 독립된 negative로 더하고 모두 farmer demand와 company EPS를 같은 방향으로 움직인다고 가정했다. cycle bull case와 cover discipline이 없었다.

### 최초로 관찰 가능했던 경고신호

2006 stock이 약 $31로 entry 대비 거의 두 배가 되고 sales·demand가 유지된 시점이 명확한 반증이자 cover 신호였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

cyclical short는 cost headwind보다 customer cash-flow cycle을 먼저 본다.

### Lesson 2

finance-company debt는 related assets·income·recourse를 함께 분류한다.

### Lesson 3

여러 macro negatives를 더하기 전에 상관관계와 상쇄효과를 모델링한다.

### Lesson 4

주가가 두 배가 되는 short에는 사전 cover rule이 있어야 한다.

### 지금 같은 아이디어를 다시 본다면

- crop prices·farm income
- retail units·dealer inventory
- price/mix
- finance assets vs debt
- rate sensitivity
- gross margin
- working capital
- MAE·cover

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 실패 |
| Valuation thesis | adjusted EV 과장 |
| Catalyst thesis | rate catalyst 무효 |
| Security payoff | short 부적합 |
| Timing / path | 강한 실패 |
| Thesis score | 1.8/10 |
| Process score | 4.8/10 |
| 종합 | **강한 실패 — ag upcycle이 leverage·rate headwind를 압도** |

### 한 문장 교훈

> cyclical short는 cost headwind보다 customer cash-flow cycle을 먼저 본다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/AGCO_Corp/8174480323) — Value Investors Club / source SQL, 2005-10-18. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [AGCO FY2005 Form 10-K](https://www.sec.gov/Archives/edgar/data/880266/000095014406002147/g99944e10vk.htm) — SEC / AGCO, 2006-03. 2003~05 sales, dealer/finance network, debt와 historical stock range 검증.
3. [AGCO SEC issuer archive](https://www.sec.gov/edgar/browse/?CIK=880266&owner=exclude) — SEC / AGCO, 2003-2008. 연도별 영업·재무·주가 공시 교차검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·제한적 price comparison만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Short**다. raw 값은 덮어쓰지 않았다.
