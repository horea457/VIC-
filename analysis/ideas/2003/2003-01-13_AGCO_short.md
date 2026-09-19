# AGCO Corporation (AG) — 2003-01-13 VIC Short

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AGCO Corporation / AG |
| VIC 게시일 / 작성자 | 2003-01-13 / chris815 |
| 분석 증권 / 실제 방향 | NYSE:AGCO common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | $21.74 |
| 기대기간 | 2003~2005 integration·cycle |
| raw horizon audit | 90x TTM GAAP earnings, leverage·working capital·pension·Challenger integration |
| 최종 판정 | **중기 부분 성공 / 장기 thesis 실패** |

> **결론:** $21.74 short는 2005말 약 $16.6에서 약 24% favorable price move를 보였다. 그러나 AGCO sales는 2003 $3.495bn에서 2004 $5.273bn, 2005 $5.450bn으로 커졌고 2007말 주가는 약 $68까지 상승했다. valuation·balance-sheet concern은 중기 trade에 일부 맞았지만 enduring business failure thesis는 틀렸다.

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

90x TTM GAAP earnings, 높은 debt와 finance JV·working capital, underfunded pension, Caterpillar Challenger integration cost 때문에 acquisitions가 earnings quality와 liquidity를 악화시킨다는 short였다. agricultural equipment weakness가 deleveraging을 막는다고 봤다.

### Reverse expectations

시장은 Challenger·Valtra 등 product portfolio와 dealer network가 sales·scale·parts economics를 키우고 cycle 회복이 fixed cost와 debt를 빠르게 흡수한다고 봤다. trailing GAAP P/E는 restructuring·integration trough 때문에 과장될 수 있었다.

---

## 3. 원문 투자논지 지도

### C1. 90x TTM GAAP P/E — 중기 성공·분모 오류

**원문 주장**

valuation이 극단적으로 높다.

**경제적 메커니즘**

earnings normalization이나 multiple compression이 price를 낮춘다.

**T0 근거**

T0 trailing GAAP earnings.

**숨은 가정**

earnings가 trough가 아니다.

**사전 반증조건**

normalized EPS 급증이면 반증.

**실제 결과**

2005까지 주가는 약 24% 하락했지만 이후 earnings/cycle로 크게 상승했다.

**정량 gap**

중기 hit·장기 miss.

**분석 오류 또는 제한**

trough denominator를 정상 earnings로 봤다.

**재사용 교훈**

reported·normalized·cycle EPS를 나눈다.

### C2. debt·finance JV risk — 실패

**원문 주장**

차입과 off-balance-sheet financing이 equity를 압박한다.

**경제적 메커니즘**

판매둔화가 receivable·funding loss로 번진다.

**T0 근거**

debt와 Rabobank JVs.

**숨은 가정**

credit access가 악화된다.

**사전 반증조건**

sales·funding이 확대되면 반증.

**실제 결과**

회사는 sales를 확대하고 distress 없이 cycle을 통과했다.

**정량 gap**

default catalyst 미실현.

**분석 오류 또는 제한**

gross exposure를 expected loss로 오인했다.

**재사용 교훈**

JV receivables·loss-sharing·liquidity를 모델링한다.

### C3. working-capital squeeze — 부분

**원문 주장**

inventory·receivables가 cash를 흡수한다.

**경제적 메커니즘**

dealer demand 약화가 cash conversion을 나쁘게 한다.

**T0 근거**

cyclical equipment balance sheet.

**숨은 가정**

inventory turns가 악화한다.

**사전 반증조건**

growth와 funding이 cash need를 흡수하면 약화.

**실제 결과**

scale-up 과정의 cash need는 있었지만 terminal stress는 없었다.

**정량 gap**

정확한 short catalyst 부족.

**분석 오류 또는 제한**

seasonal WC를 structural insolvency와 혼동했다.

**재사용 교훈**

quarterly turns와 committed liquidity를 본다.

### C4. pension 부담 — 부분

**원문 주장**

underfunded pension이 equity cash를 소모한다.

**경제적 메커니즘**

contributions가 deleveraging·EPS를 제한한다.

**T0 근거**

T0 benefit obligations.

**숨은 가정**

funding gap·rates가 악화한다.

**사전 반증조건**

contribution이 cash flow 대비 작으면 약화.

**실제 결과**

pension은 drag였지만 cycle upside를 막지 못했다.

**정량 gap**

price driver로는 2차적.

**분석 오류 또는 제한**

liability 존재와 catalyst를 혼동했다.

**재사용 교훈**

5년 cash contribution schedule로 본다.

### C5. Challenger integration 실패 — 실패

**원문 주장**

인수 통합비용·dealer conflict가 value를 훼손한다.

**경제적 메커니즘**

중복비용과 channel disruption이 margin을 누른다.

**T0 근거**

Caterpillar deal transition.

**숨은 가정**

sales synergy가 제한된다.

**사전 반증조건**

sales·portfolio가 크게 확대되면 반증.

**실제 결과**

2004~05 sales가 $5.3~5.45bn으로 확대됐다.

**정량 gap**

2003 대비 +56% in 2005.

**분석 오류 또는 제한**

cost만 보고 acquired revenue를 덜 봤다.

**재사용 교훈**

cost·revenue·working capital synergy를 함께 본다.

### C6. ag equipment weakness 지속 — 실패

**원문 주장**

industry weakness가 earnings를 계속 누른다.

**경제적 메커니즘**

farmer income·replacement delay가 unit demand를 낮춘다.

**T0 근거**

당시 weak conditions.

**숨은 가정**

commodity/farm cycle이 회복하지 않는다.

**사전 반증조건**

farm income·stock 급등이면 반증.

**실제 결과**

2006~07 ag upcycle과 stock ~$68가 반증했다.

**정량 gap**

entry 대비 +213% adverse.

**분석 오류 또는 제한**

cycle mean reversion을 배제했다.

**재사용 교훈**

short에는 crop-price·farm-income bull case를 둔다.

---

## 4. 당시 Valuation과 Payoff Structure

TTM GAAP P/E보다 normalized EBIT by region/product, finance-JV exposure, pension cash, working capital과 net debt를 써야 한다. short payoff는 2005 target뿐 아니라 2007 cycle upside와 stop/cover rule을 포함해야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for short | integration·cycle 성공 | $40~70 | 2007 ~$68 |
| Base | earnings pressure | $15~20 | 2005 ~$16.6 |
| Bull for short | liquidity/pension stress | $10 이하 | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / 2005 | $21.74 | 하락 | ~$16.6 | short +23.6% price-only |
| 2003 sales | $3.495bn | weak | $3.495bn | base |
| 2004 sales | integration risk | 압박 | $5.273bn | thesis 반대 |
| 2005 sales | cycle 약세 | 감소 | $5.450bn | thesis 반대 |
| 2007 price | downside 지속 | entry 이하 | ~$68 | 장기 실패 |

### 촉매와 시간

판정 horizon은 **2003~2005 integration·cycle**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2003-01-13 | VIC Short | $21.74 |
| 2003-12-31 | sales $3.495bn | base year |
| 2004 | Challenger·Valtra scale | integration 진행 |
| 2004-12-31 | sales $5.273bn | business break |
| 2005-12-31 | sales $5.450bn | scale 유지 |
| 2005-12-31 | stock ~$16.6 | 중기 short 이익 |
| 2006 | ag cycle 강화 | cover signal |
| 2007-12-31 | stock ~$68 | 장기 thesis 실패 |

### 실제 사업·자본구조 추이

AGCO net sales는 2003 $3.495bn, 2004 $5.273bn, 2005 $5.450bn으로 증가했다. 2005말 주가는 약 $16.6로 entry 아래였으나 agriculture upcycle과 integration 뒤 2007말 약 $68로 올랐다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

$21.74→$16.6은 short에 price-only 약 +23.6% favorable다. 계속 보유해 $68을 맞으면 약 212.8% adverse move다. borrow·cover ledger가 없어 realized return은 특정하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 90x TTM GAAP P/E | 20% | 중기 성공·분모 오류 | 중기 hit·장기 miss. |
| C2 | debt·finance JV risk | 18% | 실패 | default catalyst 미실현. |
| C3 | working-capital squeeze | 18% | 부분 | 정확한 short catalyst 부족. |
| C4 | pension 부담 | 16% | 부분 | price driver로는 2차적. |
| C5 | Challenger integration 실패 | 16% | 실패 | 2003 대비 +56% in 2005. |
| C6 | ag equipment weakness 지속 | 12% | 실패 | entry 대비 +213% adverse. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

중기에는 integration·earnings noise와 valuation compression이 작동했지만 장기에는 sales scale, product breadth와 farm-cycle operating leverage가 압도했다.

### Counterfactual

trailing earnings가 trough이고 sales가 50% 늘어날 때도 90x P/E가 유효한 short valuation 지표인가?

---

## 9. 분석 오류 유형과 최초 경고

trailing GAAP denominator와 balance-sheet static view에 의존했고 acquisition 뒤 revenue·margin synergy와 cycle-up operating leverage를 충분히 확률가중하지 않았다.

### 최초로 관찰 가능했던 경고신호

2004 sales가 $5.273bn으로 50% 이상 늘고 integration이 매출기반을 확대했다는 공시는 terminal-failure thesis의 최초 반증이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

trailing GAAP P/E가 높은 이유가 trough charges인지 먼저 분해한다.

### Lesson 2

acquisition leverage와 acquired earning power를 같은 pro forma에 넣는다.

### Lesson 3

중기 price win과 장기 business thesis를 분리한다.

### Lesson 4

cyclical short는 cover rule과 upside cycle scenario가 필수다.

### 지금 같은 아이디어를 다시 본다면

- organic vs acquired sales
- dealer inventory
- normalized EBIT
- working capital
- finance JV exposure
- pension cash
- net debt
- cover·MAE

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 장기 실패 |
| Valuation thesis | 중기 일부 적중 |
| Catalyst thesis | distress 미실현 |
| Security payoff | short path 취약 |
| Timing / path | 부분 성공 후 실패 |
| Thesis score | 5.5/10 |
| Process score | 6.5/10 |
| 종합 | **중기 부분 성공 / 장기 thesis 실패** |

### 한 문장 교훈

> trailing GAAP P/E가 높은 이유가 trough charges인지 먼저 분해한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2003-01-13. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [AGCO FY2005 Form 10-K](https://www.sec.gov/Archives/edgar/data/880266/000095014406002147/g99944e10vk.htm) — SEC / AGCO, 2006-03. 2003~05 sales, dealer/finance network, debt와 historical stock range 검증.
3. [AGCO SEC issuer archive](https://www.sec.gov/edgar/browse/?CIK=880266&owner=exclude) — SEC / AGCO, 2003-2008. 연도별 영업·재무·주가 공시 교차검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·제한적 price comparison만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Short**다. raw 값은 덮어쓰지 않았다.
