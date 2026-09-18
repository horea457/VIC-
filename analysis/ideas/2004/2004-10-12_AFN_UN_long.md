# Ag Growth Income Fund (AFN UN) — 2004-10-12 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Ag Growth Income Fund / AFN UN |
| VIC 게시일 / 작성자 | 2004-10-12 / dylex849 |
| 분석 증권 / 실제 방향 | income trust units / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 11.5% indicated cash distribution yield |
| 기대기간 | 2005~2007 operating growth·distributions |
| raw horizon audit | double-digit FCF yield, 30%+ EBITDA margin, replacement demand와 bolt-on M&A |
| 최종 판정 | **강한 성공 — margin·distribution·bolt-ons 실현** |

> **결론:** raw Short를 실제 Long으로 교정했다. 2005 H1 revenue C$40.4m·EBITDA C$12.0m, 2007 revenue C$130.7m·EBITDA C$32.4m과 distribution 증가는 high-margin niche thesis를 확인했다. Edwards와 후속 bolt-ons가 규모를 늘렸지만 완전한 distribution·unit-price ledger가 없어 exact total return은 계산하지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

Ag Growth Income Fund는 grain handling·storage·conditioning 장비를 만드는 niche manufacturer였다. replacement demand와 dealer network가 매출을 지지하고, 높은 market share·margin에서 maintenance capex와 cash distribution을 뺀 unit-holder cash가 가치의 핵심이었다.

units sold × price - steel·labour·factory overhead - SG&A - tax - maintenance capex ± working capital = distributable cash; acquisition은 incremental FCF/unit로 본다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

organic volume, market share, gross/EBITDA margin, maintenance capex, working capital, FCF/unit, payout ratio, leverage, acquisition multiple

---

## 2. 당시 상황과 시장이 가격에 넣은 것

약 35% market share, 다음 경쟁자의 약 3배 규모와 replacement-driven grain equipment를 가진 사업을 11.5% distribution yield·double-digit FCF yield에 산다는 논지였다. EBITDA margin 30%+와 EBITDA-capex margin 29%+가 payout을 지지했다.

### Reverse expectations

시장은 작은 Canadian income trust의 seasonality, steel·ag cycle, key-person risk와 acquisition deployment를 할인했다. 높은 yield가 maintenance capex·working capital 또는 temporary peak margin을 놓친 것일 수 있었다.

---

## 3. 원문 투자논지 지도

### C1. raw Short — metadata 실패

**원문 주장**

source SQL은 Short다.

**경제적 메커니즘**

방향 오류는 yield payoff를 반전시킨다.

**T0 근거**

원문은 upside·distribution을 샀다.

**숨은 가정**

본문이 실제 payoff를 확정한다.

**사전 반증조건**

하락으로 수익이면 Short다.

**실제 결과**

실제 income-trust Long.

**정량 gap**

완전 반대.

**분석 오류 또는 제한**

raw flag 의존.

**재사용 교훈**

원문 cash-flow 방향으로 교정한다.

### C2. 30%+ EBITDA margin — 성공

**원문 주장**

niche 지위가 30%+ margin을 지킨다.

**경제적 메커니즘**

scale·dealer network가 price/cost spread를 보호한다.

**T0 근거**

T0 margin history.

**숨은 가정**

cycle·steel pass-through 관리.

**사전 반증조건**

25% 이하 지속이면 실패.

**실제 결과**

2005 H1 29.7%, 2007 약 24.8%.

**정량 gap**

초기 적중·scale 뒤 완화.

**분석 오류 또는 제한**

peak margin 영구화 위험.

**재사용 교훈**

organic margin과 acquired mix를 분리한다.

### C3. 11.5% distribution — 성공

**원문 주장**

double-digit cash yield가 covered된다.

**경제적 메커니즘**

FCF가 unit cash distribution을 지불한다.

**T0 근거**

EBITDA-capex spread.

**숨은 가정**

working capital·tax·interest가 작다.

**사전 반증조건**

cut 또는 coverage<1x면 실패.

**실제 결과**

2005 distribution 8%+ 인상.

**정량 gap**

cut 대신 인상.

**분석 오류 또는 제한**

complete coverage bridge 부재.

**재사용 교훈**

DCF보다 cash coverage 표를 먼저 만든다.

### C4. 35% share/moat — 대체로 성공

**원문 주장**

다음 경쟁자 3배 규모가 방어력이다.

**경제적 메커니즘**

distribution·installed base가 replacement sales를 만든다.

**T0 근거**

T0 share estimates.

**숨은 가정**

customers가 switching하지 않는다.

**사전 반증조건**

share·margin 급락이면 실패.

**실제 결과**

매출·제품군이 확대됐다.

**정량 gap**

share exact follow-up 제한.

**분석 오류 또는 제한**

규모를 moat로 바로 등치.

**재사용 교훈**

dealer retention·price realization을 추적한다.

### C5. bolt-on M&A — 강한 성공

**원문 주장**

adjacent acquisitions가 accretive growth를 만든다.

**경제적 메커니즘**

shared channel·manufacturing이 FCF/unit를 늘린다.

**T0 근거**

Edwards pipeline.

**숨은 가정**

multiple·integration·debt 통제.

**사전 반증조건**

unit당 cash 희석이면 실패.

**실제 결과**

Edwards, Hi Roller, Twister, Union Iron 실행.

**정량 gap**

다수 거래 실현.

**분석 오류 또는 제한**

deal quantity를 accretion으로 대체.

**재사용 교훈**

deal별 pro forma FCF/unit를 기록한다.

### C6. management alignment — 부분 검증

**원문 주장**

CEO 순자산 90%가 units에 묶여 있다.

**경제적 메커니즘**

ownership이 payout·capital allocation을 정렬한다.

**T0 근거**

원문 ownership.

**숨은 가정**

control benefit·risk-taking이 과하지 않다.

**사전 반증조건**

과대 M&A·희석이면 반증.

**실제 결과**

distribution과 bolt-ons가 가치를 늘렸다.

**정량 gap**

결과 지지·인과 단정 불가.

**분석 오류 또는 제한**

ownership을 governance quality로 동일시.

**재사용 교훈**

related-party·compensation을 별도 본다.

---

## 4. 당시 Valuation과 Payoff Structure

distribution yield만 보지 않고 EBITDA에서 cash tax·maintenance capex·working capital·interest를 빼 unit당 distributable cash를 계산한다. acquisitions는 debt·issued units 뒤 증분 cash/unit가 양수일 때만 가치창출이다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | ag downcycle·margin 20% | distribution cut | 미실현 |
| Base | replacement·30% EBITDA | yield+성장 | 2005 실현 |
| Bull | bolt-on accretion | 매출·EBITDA scale | 2007 실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Distribution yield | 11.5% | covered·증가 | 2005 8%+ 인상 | 성공 |
| EBITDA margin | 30%+ | 약 30% | 2005 H1 29.7% | 근접 |
| Market share | 35% | 지위 유지 | product expansion | 방향 성공 |
| 2005 H1 | 성장 | strong results | revenue C$40.4m/EBITDA C$12m | 성공 |
| 2007 | bolt-on 성장 | scale | revenue C$130.7m/EBITDA C$32.4m | 강한 성공 |

### 촉매와 시간

판정 horizon은 **2005~2007 operating growth·distributions**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2004-10-12 | VIC Long | raw Short 교정 |
| 2005 | Edwards acquisition | product breadth |
| 2005-H1 | C$40.4m revenue | growth |
| 2005-H1 | C$12.0m EBITDA | 29.7% margin |
| 2005 | distribution 8%+ 인상 | coverage 확인 |
| 2006 | Hi Roller·Twister | bolt-ons |
| 2007 | Union Iron | platform 확대 |
| 2007-FY | C$130.7m/C$32.4m | scale success |

### 실제 사업·자본구조 추이

2005 Edwards acquisition이 product breadth를 넓혔다. 2005 H1 revenue C$40.4m, EBITDA C$12.0m으로 약 29.7% margin을 기록했고 distribution은 8% 이상 인상됐다. 2007 revenue C$130.7m, EBITDA C$32.4m이었으며 Hi Roller, Twister와 Union Iron 등 bolt-ons가 이어졌다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

distribution record dates, unit prices와 세금처리가 완전하지 않아 exact total return·IRR을 만들지 않는다. operating margin·distribution increase·scale growth로 thesis를 판정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | raw Short | 20% | metadata 실패 | 완전 반대. |
| C2 | 30%+ EBITDA margin | 18% | 성공 | 초기 적중·scale 뒤 완화. |
| C3 | 11.5% distribution | 18% | 성공 | cut 대신 인상. |
| C4 | 35% share/moat | 16% | 대체로 성공 | share exact follow-up 제한. |
| C5 | bolt-on M&A | 16% | 강한 성공 | 다수 거래 실현. |
| C6 | management alignment | 12% | 부분 검증 | 결과 지지·인과 단정 불가. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

replacement demand, dominant dealer position과 높은 factory margin이 현금을 만들었고, management가 그 현금을 distributions와 adjacent acquisitions에 배분했다.

### Counterfactual

steel +20%, farm capex -20%, working-capital build와 acquisition debt를 반영해도 11.5% distribution이 1.2x 이상 covered였는가?

---

## 9. 분석 오류 유형과 최초 경고

높은 역사적 margin과 CEO alignment를 구조적 moat의 충분조건으로 보고 cycle·integration·payout coverage sensitivity를 덜 계량화했다.

### 최초로 관찰 가능했던 경고신호

thesis break는 없었다. 사전 핵심 경고는 EBITDA margin 25% 이하 또는 distribution coverage 1.0x 미만이었지만 초기 결과는 반대로 강했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

income trust의 높은 yield는 maintenance capex와 working capital 뒤 coverage로 검증한다.

### Lesson 2

시장점유율은 pricing power보다 replacement demand·dealer economics와 함께 본다.

### Lesson 3

M&A는 headline EBITDA가 아니라 unit당 distributable cash accretion으로 본다.

### Lesson 4

배당을 포함한 ledger 없이 exact return을 주장하지 않는다.

### 지금 같은 아이디어를 다시 본다면

- organic volume
- EBITDA margin
- maintenance capex
- working capital
- FCF/unit
- payout
- leverage
- M&A multiple

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 강한 성공 |
| Valuation thesis | 11.5% yield 지지 |
| Catalyst thesis | results·M&A 실현 |
| Security payoff | trust units 적절 |
| Timing / path | 2005~07 성공 |
| Thesis score | 9.0/10 |
| Process score | 8.4/10 |
| 종합 | **강한 성공 — margin·distribution·bolt-ons 실현** |

### 한 문장 교훈

> income trust의 높은 yield는 maintenance capex와 working capital 뒤 coverage로 검증한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/Ag_Growth/7929689393) — Value Investors Club / source SQL, 2004-10-12. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Ag Growth 2005 annual report](https://www.annualreports.com/HostedData/AnnualReportArchive/a/TSX_AFN_2005.pdf) — Ag Growth, 2006. 2005 Edwards acquisition, 매출·EBITDA·distribution 검증.
3. [AGI corporate history / AIF](https://www.aggrowth.com/globalassets/investors-section/shareholder-information-pdfs/agi-aif-2018.pdf) — Ag Growth International, 2018. bolt-on acquisition과 장기 사업확장 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·corporate-action payoff만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
