# AmTrust Financial Services Inc. (AFSI) — 2013-08-19 VIC Short

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AmTrust Financial Services Inc. / AFSI |
| VIC 게시일 / 작성자 | 2013-08-19 / Francisco432 |
| 분석 증권 / 실제 방향 | AmTrust common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 $18 |
| 기대기간 | 1~3년 capital·reserve catalyst |
| raw horizon audit | tangible-book depletion, reserve development, captive scrutiny와 rating/covenant catalyst |
| 최종 판정 | **fundamental concern 부분 적중 / trade 실패에 가까움** |

> **결론:** tangible book·reserve·internal-control 우려는 2017 restatement로 일부 검증됐고 2018 take-private는 $14.75였다. 그러나 약 $18 short 뒤 주가가 약 $36까지 올라 약 100% adverse excursion을 만들었다. 후행 accounting validation은 catalyst clock과 생존경로가 틀린 short를 소급해 성공으로 만들지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

AmTrust는 small-commercial P&C, warranty와 specialty risk를 인수하던 보험사였다. earned premium과 investment income에서 losses·expenses·reinsurance cost를 빼며, reserve adequacy와 statutory capital이 common의 실질 book-value growth를 결정한다.

earned premium × (1-loss ratio-expense ratio) + investment income - tax = book growth; reserve development·ceded recoverables·related parties·statutory capital을 common payoff에 연결한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

gross/earned premium, accident-year loss ratio, prior-year development, combined ratio, ceded recoverables, statutory surplus, tangible book/share, NPW/tangible equity, related-party balances

---

## 2. 당시 상황과 시장이 가격에 넣은 것

reported earnings가 tangible book으로 축적되지 않고, life-settlement contract의 Level 3 valuation, aggressive reserving·acquisition accounting, related-party reinsurance와 balance-sheet leverage가 premium growth를 떠받친다는 논지였다. NPW/tangible equity가 mid-2010 약 150%에서 2Q13 약 336%로 상승한 점을 catalyst 압력으로 봤다.

### Reverse expectations

시장은 niche premium growth, acquisitions, reinsurance access와 reported ROE가 capital을 계속 보충한다고 봤다. 보험 short에서는 accounting quality가 낮아도 statutory intervention·rating action·reserve charge의 날짜가 없으면 book growth와 multiple expansion이 수년간 short를 압도할 수 있다.

---

## 3. 원문 투자논지 지도

### C1. earnings와 tangible book 불일치 — 부분 성공

**원문 주장**

reported earnings가 tangible book을 만들지 못한다.

**경제적 메커니즘**

low-quality gains·intangibles·capital leakage가 common cushion을 약화한다.

**T0 근거**

earnings와 tangible book divergence.

**숨은 가정**

차이가 경제적 손실을 선행한다.

**사전 반증조건**

tangible book가 지속 성장하면 약화.

**실제 결과**

2017 restatement가 일부 earnings quality 우려를 확인했다.

**정량 gap**

방향 적중·4년 지연.

**분석 오류 또는 제한**

회계 divergence를 즉시 가격 catalyst로 봤다.

**재사용 교훈**

quality claim과 timing claim을 분리한다.

### C2. life-settlement Level 3 가치 — 미확정

**원문 주장**

life-settlement contracts가 과대평가됐다.

**경제적 메커니즘**

unobservable mortality·discount assumptions이 asset와 income을 부풀린다.

**T0 근거**

복잡한 Level 3 disclosures.

**숨은 가정**

mark haircut이 capital에 material하다.

**사전 반증조건**

cash realization이 carrying value를 지지하면 반증.

**실제 결과**

공개 자료만으로 동일 portfolio의 full cash realization을 복원하지 못했다.

**정량 gap**

정량 gap 미확정.

**분석 오류 또는 제한**

불투명성을 손실액으로 등치했다.

**재사용 교훈**

asset별 cash-vs-mark roll-forward를 요구한다.

### C3. reserve underestimation — 부분 성공

**원문 주장**

초기 loss picks가 낮아 adverse development가 온다.

**경제적 메커니즘**

성장기에 낮은 picks가 earnings·surplus를 앞당긴다.

**T0 근거**

peer 대비 빠른 성장과 reserve mechanics.

**숨은 가정**

claims maturation이 unfavorable하다.

**사전 반증조건**

다년 favorable development면 반증.

**실제 결과**

후속 accounting·control 문제는 질 우려를 지지했지만 reserve collapse 단독증거는 제한적이다.

**정량 gap**

claim-specific 증거 부족.

**분석 오류 또는 제한**

회계 문제를 전부 reserve 문제로 묶었다.

**재사용 교훈**

accident year·line별 triangle로 검증한다.

### C4. acquisition accounting — 부분 성공

**원문 주장**

인수회계가 organic profitability를 과장한다.

**경제적 메커니즘**

purchase accounting·bargain gains가 recurring earnings처럼 보인다.

**T0 근거**

연속 acquisitions와 높은 reported ROE.

**숨은 가정**

organic cohorts가 인수 후에도 profitable하다.

**사전 반증조건**

organic combined ratio가 안정되면 약화.

**실제 결과**

restatement는 quality 우려를 지지했지만 acquisition별 economics는 혼합이다.

**정량 gap**

정확한 deal ROIC 미복원.

**분석 오류 또는 제한**

복잡성을 자동으로 value destruction으로 봤다.

**재사용 교훈**

deal별 cash price·reserve·earn-out·organic result를 잇는다.

### C5. related-party reinsurance·capital — 부분 검증

**원문 주장**

affiliate 구조가 risk와 capital을 가린다.

**경제적 메커니즘**

ceding·recoverables·collateral이 earnings와 statutory capital을 이동시킨다.

**T0 근거**

Maiden 등 related-party links.

**숨은 가정**

terms가 arm's length가 아니다.

**사전 반증조건**

collateral·cash settlement가 충분하면 약화.

**실제 결과**

governance scrutiny는 커졌지만 즉시 capital failure는 없었다.

**정량 gap**

red flag와 loss 사이 gap.

**분석 오류 또는 제한**

관계 자체를 손실로 간주했다.

**재사용 교훈**

terms·collateral·counterparty credit을 계량한다.

### C6. NPW/tangible equity 150%→336% — timing 실패

**원문 주장**

leverage가 성장의 끝과 rating/covenant catalyst를 부른다.

**경제적 메커니즘**

premium risk가 capital cushion보다 빠르게 커진다.

**T0 근거**

mid-2010 ~150%, 2Q13 ~336%.

**숨은 가정**

외부 capital과 reinsurance가 닫힌다.

**사전 반증조건**

growth·rating이 3년 지속되면 timing 반증.

**실제 결과**

즉시 collapse 없이 stock이 약 2배 오른 뒤 2017 event가 왔다.

**정량 gap**

1~3년 horizon miss.

**분석 오류 또는 제한**

stress indicator를 dated catalyst로 오인했다.

**재사용 교훈**

ratio threshold에 실제 rating/covenant 문구를 붙인다.

---

## 4. 당시 Valuation과 Payoff Structure

reported P/E가 아니라 tangible book, statutory surplus와 normalized accident-year loss ratio로 equity를 다시 계산해야 한다. Level 3 assets·ceded recoverables를 haircut하고 adverse reserve development를 surplus에서 차감하되, downside target와 catalyst timing·borrow·MAE를 하나의 position rule로 묶는다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for short | growth·capital access 지속 | $30~40 | 약 $36 실현 |
| Base | reserve·capital 정상화 | $14~18 | 2018 $14.75 |
| Bull for short | rating/covenant 조기 촉발 | $8~12 | 기간 내 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry / peak | ~$18 short | 하락 | ~$36 | ~100% adverse |
| NPW/tangible equity | ~150%→336% | capital constraint | 즉시 collapse 없음 | timing 실패 |
| Restatement | 회계 우려 | 1~3년 catalyst | 2017 | 약 4년 지연 |
| 2014/15 income | 질 낮음 | 하향수정 | restated lower | 부분 적중 |
| Terminal | entry 아래 | short payoff | $14.75 | price-only -18.1% |

### 촉매와 시간

판정 horizon은 **1~3년 capital·reserve catalyst**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2013-08-19 | VIC Short | ~$18 entry |
| 2014 | premium·book growth 지속 | catalyst 지연 |
| 2015 | stock $30대 | MAE 확대 |
| 2016 | stock 약 $36 | trade-level failure |
| 2017-04-10 | restatement notice | accounting concern 확인 |
| 2017-04-11 | revised results | 정량 조정 |
| 2018-06-07 | $14.75 amended deal | terminal price |
| 2018 | take-private | public short 종료 |

### 실제 사업·자본구조 추이

주가는 먼저 약 $36까지 올랐다. 2017 회사는 2014·2015와 2016 interim financials를 restate했고 internal controls 문제를 공시했다. 2018 amended take-private price는 $14.75 cash였다. diagnosis의 일부는 맞았지만 원 horizon보다 훨씬 늦었고 path가 치명적이었다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

$18→$36은 short에 약 100% adverse price move다. $14.75 terminal은 entry보다 약 18.1% 낮지만 exact borrow·cover·dividend ledger가 없어 realized return이나 IRR은 제시하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | earnings와 tangible book 불일치 | 20% | 부분 성공 | 방향 적중·4년 지연. |
| C2 | life-settlement Level 3 가치 | 18% | 미확정 | 정량 gap 미확정. |
| C3 | reserve underestimation | 18% | 부분 성공 | claim-specific 증거 부족. |
| C4 | acquisition accounting | 16% | 부분 성공 | 정확한 deal ROIC 미복원. |
| C5 | related-party reinsurance·capital | 16% | 부분 검증 | red flag와 loss 사이 gap. |
| C6 | NPW/tangible equity 150%→336% | 12% | timing 실패 | 1~3년 horizon miss. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

fundamental red flags보다 premium growth, book accretion과 catalyst latency가 먼저 작동했다. 최종 가격만 보면 하락이지만 실제 short는 두 배 adverse path·carry·margin risk를 견뎌야 했다.

### Counterfactual

회계 문제가 4년 뒤에야 드러나고 그 전에 주가가 2배가 되어도 이 position size와 borrow terms에서 expected value가 양수였는가?

---

## 9. 분석 오류 유형과 최초 경고

여러 quality concern을 하나의 임박한 collapse로 묶었고 statutory capital·rating·reserve review 각각의 독립된 catalyst clock과 MAE/cover rule을 두지 않았다.

### 최초로 관찰 가능했던 경고신호

주가와 premium/book growth가 2014~15에도 계속 올라 $30대를 통과한 시점이 trade-level timing thesis의 명확한 반증이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

보험 short는 red flag의 수보다 statutory·rating·reserve catalyst의 날짜가 중요하다.

### Lesson 2

eventual restatement와 investable short payoff를 분리한다.

### Lesson 3

reserve·Level 3·related-party claim을 각각 별도 falsifier로 관리한다.

### Lesson 4

100% adverse excursion을 허용하는 thesis에는 position-size와 cover rule이 필수다.

### 지금 같은 아이디어를 다시 본다면

- accident-year loss ratio
- prior-year reserve development
- statutory surplus
- NPW/surplus와 tangible equity
- ceded recoverable collateral
- Level 3 marks
- rating triggers
- borrow·MAE·cover

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 우려 일부 적중 |
| Valuation thesis | terminal 일부 적중 |
| Catalyst thesis | 촉매 지연 |
| Security payoff | short path 취약 |
| Timing / path | 실패에 가까움 |
| Thesis score | 5.5/10 |
| Process score | 6.5/10 |
| 종합 | **fundamental concern 부분 적중 / trade 실패에 가까움** |

### 한 문장 교훈

> 보험 short는 red flag의 수보다 statutory·rating·reserve catalyst의 날짜가 중요하다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2013-08-19. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [AmTrust restatement notice](https://www.sec.gov/Archives/edgar/data/1365555/000136555517000051/amtrustform8-kedgarcopy.htm) — SEC / AmTrust, 2017-04-10. 2014·2015와 2016 interim statements 재작성 및 controls issue 검증.
3. [AmTrust restatement results](https://www.sec.gov/Archives/edgar/data/1365555/000136555517000061/ex991pressrelease.htm) — SEC / AmTrust, 2017-04-11. 2014·2015 net income 감소와 오류 성격 검증.
4. [Amended take-private agreement](https://www.sec.gov/Archives/edgar/data/1365555/000119312518186313/d556924d8k.htm) — SEC / AmTrust, 2018-06-07. $14.75/share cash terminal consideration 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·제한적 price comparison만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Short**다. raw 값은 덮어쓰지 않았다.
