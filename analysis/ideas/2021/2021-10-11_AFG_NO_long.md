# AF Gruppen ASA (AFG NO) — 2021-10-11 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AF Gruppen ASA / AFG NO |
| VIC 게시일 / 작성자 | 2021-10-11 / Barong |
| 분석 증권 / 실제 방향 | AF Gruppen Oslo-listed common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 NOK197 |
| 기대기간 | 약 2년; 2024 operating case 교차검증 |
| raw horizon audit | 2024 revenue NOK36.7bn, EBIT margin 6.6%, probability-weighted fair value NOK248 |
| 최종 판정 | **부분 실패 — balance sheet·backlog 성공, 성장·margin 경로 미달** |

> **결론:** quality와 solvency는 유지됐지만 원 operating case는 미달했다. 2024 revenue NOK30.638bn은 NOK36.7bn 대비 16.5% 낮았고 EBT margin 3.5%는 제시 EBIT margin 6.6%와 정의가 다르지만 격차가 컸다. 2025 revenue NOK31.992bn·EBT NOK1.653bn으로 개선됐고 backlog는 NOK44.716bn이었다. exact stock return은 verified ledger 부재로 보류한다.

---

## 1. 회사는 정확히 무엇을 하는가

AF Gruppen은 노르웨이의 construction, civil engineering, energy/environment와 demolition·recycling contractor다. 수주잔고가 매출로 전환될 때 project margin과 loss provision을 통과해야 하므로 backlog 규모보다 mix·execution·cash conversion이 중요하다.

backlog × conversion rate × project gross margin - loss provisions - overhead - tax ± working capital - capex = equity cash flow; EBT margin과 현금전환을 같이 본다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

revenue, order intake, backlog, EBT/EBIT margin, project write-downs, operating cash flow, net interest-bearing debt, ROIC, EPS, dividend

---

## 2. 당시 상황과 시장이 가격에 넣은 것

약 NOK197에서 가족·직원 ownership, decentralization, demolition/environment capability와 강한 balance sheet가 NOK40bn revenue·7% margin의 장기 목표로 수렴할 것이라는 quality compounder thesis였다. 원 base는 2024 revenue NOK36.7bn·EBIT margin 6.6%, p-weighted FV NOK248이었다.

### Reverse expectations

시장은 fixed-price project losses, construction cyclicality, acquisition/integration과 backlog의 낮은-margin mix 때문에 high-quality culture가 target margin으로 빠르게 전환되지 않을 위험을 반영했다.

---

## 3. 원문 투자논지 지도

### C1. 2024 revenue NOK36.7bn — 실패

**원문 주장**

revenue가 NOK36.7bn에 도달한다.

**경제적 메커니즘**

backlog conversion과 market-share growth.

**T0 근거**

T0 order book·long-term NOK40bn ambition.

**숨은 가정**

projects가 지연·취소 없이 전환된다.

**사전 반증조건**

2024 revenue <NOK34bn이면 반증.

**실제 결과**

NOK30.638bn.

**정량 gap**

-NOK6.062bn/-16.5%.

**분석 오류 또는 제한**

backlog를 매출로 선형 변환.

**재사용 교훈**

backlog age·segment·cancellation을 반영한다.

### C2. 2024 EBIT margin 6.6% — 실패

**원문 주장**

margin이 6.6%로 개선된다.

**경제적 메커니즘**

mix·scale·decentralized execution.

**T0 근거**

company 7% ambition.

**숨은 가정**

loss projects가 제한된다.

**사전 반증조건**

reported operating margin <5%면 반증.

**실제 결과**

공식 EBT margin 3.5%; 정의는 다르지만 큰 miss.

**정량 gap**

약 -3.1ppt 대 reference.

**분석 오류 또는 제한**

EBIT와 EBT 비교정의 불완전.

**재사용 교훈**

동일 metric으로 target bridge를 고정한다.

### C3. strong balance sheet — 강한 성공

**원문 주장**

net cash가 cycle downside를 흡수한다.

**경제적 메커니즘**

cash conversion과 낮은 leverage.

**T0 근거**

T0 financial quality.

**숨은 가정**

working-capital reversal·M&A가 cash를 소진하지 않는다.

**사전 반증조건**

net debt 급증이면 반증.

**실제 결과**

2024 net interest-bearing receivable NOK99m.

**정량 gap**

순현금 방향 유지.

**분석 오류 또는 제한**

현금을 margin 안전과 동일시할 수 있다.

**재사용 교훈**

liquidity와 project profitability를 분리한다.

### C4. cash conversion — 강한 성공

**원문 주장**

reported profit가 현금으로 전환된다.

**경제적 메커니즘**

milestone billing과 working-capital discipline.

**T0 근거**

contractor operating model.

**숨은 가정**

receivables·WIP가 cash를 흡수하지 않는다.

**사전 반증조건**

OCF가 EBT를 장기간 하회하면 약화.

**실제 결과**

2024 OCF NOK2.217bn 대 EBT NOK1.085bn.

**정량 gap**

OCF/EBT 약 2.0x.

**분석 오류 또는 제한**

단년 working-capital benefit 가능.

**재사용 교훈**

다년 cash conversion을 본다.

### C5. NOK248 fair value — 미검증·시간 실패

**원문 주장**

약 2년 p-weighted FV NOK248.

**경제적 메커니즘**

earnings growth와 quality multiple.

**T0 근거**

NOK197 대비 25.9% upside.

**숨은 가정**

operating case가 제때 실현된다.

**사전 반증조건**

목표연도 operating miss면 valuation premise 약화.

**실제 결과**

2024 operating denominator 미달; price ledger 보류.

**정량 gap**

FV의 earnings input 불성립.

**분석 오류 또는 제한**

spot price 추정으로 빈칸을 채울 위험.

**재사용 교훈**

verified total-return ledger가 없으면 운영 판정만 한다.

### C6. NOK40bn·7% 장기목표 — 미달·진행중

**원문 주장**

company ambition에 수렴한다.

**경제적 메커니즘**

scale·portfolio quality가 margin을 높인다.

**T0 근거**

공식 long-term goals.

**숨은 가정**

profitable backlog와 capacity.

**사전 반증조건**

2025에도 revenue <NOK35bn·margin <6%면 지연.

**실제 결과**

2025 revenue NOK31.992bn, EBT 5.17%.

**정량 gap**

매출 -NOK8.008bn, margin -1.83ppt 대 ambition.

**분석 오류 또는 제한**

aspiration을 forecast로 사용.

**재사용 교훈**

목표는 외부 base rate와 capacity로 haircut한다.

---

## 4. 당시 Valuation과 Payoff Structure

NOK248은 약 NOK197 대비 25.9% upside다. operating case는 revenue×margin에서 시작하되 EBIT/EBT definitions, net cash, minority와 shares를 잇고, quality premium은 project loss tail 뒤에 적용해야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | project losses·3% margin | earnings·multiple 하락 | 2024에 근접 |
| Base | NOK36.7bn·6.6% | NOK248 | 2024 미달 |
| Recovery | backlog conversion·5%+ EBT | earnings 회복 | 2025 일부 실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2024 revenue | NOK36.7bn 목표 | NOK36.7bn | NOK30.638bn | -16.5% |
| 2024 margin | EBIT 6.6% | 6.6% | EBT 3.5% | 정의 차이에도 큰 미달 |
| 2024 backlog | quality order book | 성장 지지 | NOK40.351bn | 성공 |
| 2024 OCF | cash quality | positive | NOK2.217bn | 강한 성공 |
| 2025 EBT | 장기 회복 | target 접근 | NOK1.653bn; 5.17% | 회복·여전히 7% 미달 |

### 촉매와 시간

판정 horizon은 **약 2년; 2024 operating case 교차검증**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2021-10-11 | VIC Long | NOK197 entry |
| 2022 | construction cost inflation | margin pressure |
| 2023 | backlog 유지 | quality 지지 |
| 2024-12 | revenue NOK30.638bn | target 미달 |
| 2024-12 | EBT margin 3.5% | margin miss |
| 2025-02-13 | FY2024 발표 | horizon failure 확정 |
| 2025-12 | EBT margin 약 5.17% | 회복 |
| 2026 | backlog NOK44.716bn 보고 | forward support |

### 실제 사업·자본구조 추이

2024 revenue NOK30.638bn, EBT NOK1.085bn(3.5%), backlog NOK40.351bn, operating cash flow NOK2.217bn, net interest-bearing receivable NOK99m, EPS NOK6.52와 dividend NOK5였다. 2025 revenue NOK31.992bn, EBT NOK1.653bn(약 5.17%)과 backlog NOK44.716bn으로 회복했지만 2024 target timing은 놓쳤다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

2021 entry 약 NOK197은 원문 기준이다. 동일 거래소·배당·split을 반영한 검증 가격 ledger가 없어 2026 spot 또는 exact CAGR을 쓰지 않는다. 운영목표와 명시 valuation range를 기준으로 판정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 2024 revenue NOK36.7bn | 20% | 실패 | -NOK6.062bn/-16.5%. |
| C2 | 2024 EBIT margin 6.6% | 18% | 실패 | 약 -3.1ppt 대 reference. |
| C3 | strong balance sheet | 18% | 강한 성공 | 순현금 방향 유지. |
| C4 | cash conversion | 16% | 강한 성공 | OCF/EBT 약 2.0x. |
| C5 | NOK248 fair value | 16% | 미검증·시간 실패 | FV의 earnings input 불성립. |
| C6 | NOK40bn·7% 장기목표 | 12% | 미달·진행중 | 매출 -NOK8.008bn, margin -1.83ppt 대 ambition. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

order intake, cash generation과 net-cash balance sheet는 downside를 제한했지만 backlog mix와 project execution이 revenue·margin convergence를 늦췄다. 2025 EBT 회복은 quality를 확인하되 2024 timing miss를 지우지 않는다.

### Counterfactual

revenue NOK31bn, EBT margin 3.5%, 12x earnings와 NOK5 dividend만으로 NOK197 entry가 정당화됐는가?

---

## 9. 분석 오류 유형과 최초 경고

문화·분산운영·backlog의 질을 target margin 도달확률로 너무 곧게 연결하고 project-level downside와 EBIT/EBT 정의 차이를 충분히 stress하지 않았다.

### 최초로 관찰 가능했던 경고신호

2024 revenue·EBT 발표에서 target-year 매출과 margin이 동시에 미달해 timing claim이 명확히 깨졌다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

backlog는 매출도 이익도 아니며 conversion과 project margin을 거쳐야 한다.

### Lesson 2

좋은 balance sheet와 좋은 entry valuation을 분리한다.

### Lesson 3

EBT와 EBIT 정의를 섞지 않는다.

### Lesson 4

목표연도 miss를 후속 개선으로 소급해 지우지 않는다.

### 지금 같은 아이디어를 다시 본다면

- backlog mix
- order intake
- conversion
- project provisions
- EBT margin
- OCF
- net debt
- ROIC·dividend

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | quality 유지 |
| Valuation thesis | NOK248 미검증·operating miss |
| Catalyst thesis | 시간만으로 해결 안 됨 |
| Security payoff | common 적절 |
| Timing / path | 2024 실패·2025 회복 |
| Thesis score | 5.5/10 |
| Process score | 7.0/10 |
| 종합 | **부분 실패 — balance sheet·backlog 성공, 성장·margin 경로 미달** |

### 한 문장 교훈

> backlog는 매출도 이익도 아니며 conversion과 project margin을 거쳐야 한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/AF_Gruppen/2488905589) — Value Investors Club / source SQL, 2021-10-11. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [AF Gruppen FY2024 results](https://www.afgruppen.com/news/2025/02/af-gruppen-ended-the-year-with-solid-results-and-a-strong-order-intake/) — AF Gruppen, 2025-02-13. 2024 revenue NOK30.638bn, EBT NOK1.085bn, backlog NOK40.351bn, OCF NOK2.217bn 검증.
3. [AF Gruppen Annual Report 2025](https://www.afgruppen.com/kampanje/annual-report-af-gruppen/) — AF Gruppen, 2026. 2025 revenue NOK31.992bn, EBT NOK1.653bn와 backlog NOK44.716bn 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·bankruptcy waterfall만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
