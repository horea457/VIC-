# Anglo-Eastern Plantations Plc / AEP Plantations Plc (AEP) — 2012-06-11 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Anglo-Eastern Plantations Plc / AEP Plantations Plc / AEP |
| VIC 게시일 / 작성자 | 2012-06-11 / Den1200 |
| 분석 증권 / 실제 방향 | LSE:AEP common equity / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 원문 약 $4.2k~5.2k per planted ha |
| 기대기간 | 수령 성숙과 재투자가 진행되는 3~7년 |
| raw horizon audit | 명시적 단기 target보다 ha당 가치·maturation thesis |
| 최종 판정 | **장기 성공 — 생산기반·순현금·순자산 compounding, SQL 성과행은 폐기** |

> **결론:** 낮은 planted-ha 가격과 이미 집행된 immature acreage의 성숙이라는 논지는 생산·순현금·순자산 증가로 장기 검증됐다. 2012 net cash $91.2m에서 2024 $181.9m, 2024 attributable profit $67.5m·shareholder net assets $551.0m으로 커졌다. 다만 SQL 가격은 미국 American Electric Power라 이 아이디어의 수익률로 쓸 수 없다.

---

## 1. 회사는 정확히 무엇을 하는가

당시 Anglo-Eastern Plantations, 현재 AEP Plantations는 인도네시아·말레이시아에서 oil-palm estate와 mill을 운영한다. 토지를 식재한 뒤 약 3년부터 열매를 수확하고 수령이 올라가며 ha당 FFB yield가 성숙한다. CPO·kernel 판매가에서 estate·mill·물류·재식재·세금과 개발 capex를 뺀 현금이 주주에게 귀속된다.

`mature ha × FFB yield/ha × extraction rate × CPO price - estate/mill cost - tax - sustaining/development capex = equity cash flow`.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

mature/immature ha, age profile, FFB yield/ha, oil extraction rate, CPO price, cash cost/t, replanting·development capex, net cash, RSPO/ISPO status

---

## 2. 당시 상황과 시장이 가격에 넣은 것

원문은 mature planted area 약 39.8k ha와 큰 immature acreage를 replacement 약 $8k/ha, private deals $15k~20k/ha보다 낮은 $4.2k~5.2k/ha에 산다고 봤다. CPO 가격을 맞히기보다 높은 oil yield, low-cost estate와 maturation·내부재투자의 시간가치를 강조했다.

### Reverse expectations

할인은 단순 무지가 아니라 commodity price, Indonesia land title·세금·환율, related-party governance, replanting capex와 ESG·deforestation risk를 반영했다. ha당 거래가치는 법적권리·수령·접근성·mill capacity가 다르면 비교가 무너진다.

---

## 3. 원문 투자논지 지도

### C1. planted ha를 replacement 이하에 매수 — 성공 방향

**원문 주장**

$4.2k~5.2k/ha는 replacement $8k와 private $15k~20k보다 싸다.

**경제적 메커니즘**

동일 질의 estate가 더 높은 대체·거래가치를 가지면 NAV discount가 크다.

**T0 근거**

원문 ha와 거래비교.

**숨은 가정**

title·age·mill·country risk가 충분히 유사하다.

**사전 반증조건**

장기 net asset가 식재가치보다 낮아지면 반증.

**실제 결과**

2024 shareholder net assets $551.0m과 순현금이 축적됐다.

**정량 gap**

exact LSE rerating은 미검증.

**분석 오류 또는 제한**

질이 다른 hectare를 한 가격으로 비교했다.

**재사용 교훈**

ha는 legal title·age·yield·mill·access별로 haircut한다.

### C2. immature acreage가 내재성장 — 성공

**원문 주장**

이미 심은 acreage가 성숙하며 생산을 늘린다.

**경제적 메커니즘**

추가 토지구매 없이 tree-age yield curve가 FFB를 증가시킨다.

**T0 근거**

2012 mature 약 39.8k ha와 immature mix.

**숨은 가정**

agronomy·weather·replanting이 정상이다.

**사전 반증조건**

mature 전환에도 own FFB가 늘지 않으면 반증.

**실제 결과**

2012부터 생산기반이 확대되고 2022 age chart에도 young/immature runway가 남았다.

**정량 gap**

연도별 cohort attribution은 제한.

**분석 오류 또는 제한**

면적증가와 yield/ha를 분리하지 않았다.

**재사용 교훈**

age-cohort별 ha와 yield를 연결한다.

### C3. low-cost palm oil economics — 대체로 성공

**원문 주장**

palm oil의 ha당 oil yield와 estate 위치가 낮은 원가를 만든다.

**경제적 메커니즘**

낮은 cash cost가 CPO downturn에서도 양의 margin을 남긴다.

**T0 근거**

원문 $750~1,250/t sensitivity.

**숨은 가정**

fertilizer·labour·FX·levy가 cost advantage를 없애지 않는다.

**사전 반증조건**

낮은 CPO에서 operating cash가 반복 적자면 반증.

**실제 결과**

2012 가격하락에도 생산·net cash를 유지했고 2024 높은 profit을 냈다.

**정량 gap**

cycle별 unit cost series는 미완전.

**분석 오류 또는 제한**

industry yield advantage를 company cost curve로 동일시했다.

**재사용 교훈**

cash cost/t와 yield/ha를 공시로 검증한다.

### C4. 20%+ planted-asset ROIC — 방향 성공·정밀 제한

**원문 주장**

개발원가 대비 성숙 earnings가 높은 ROIC를 만든다.

**경제적 메커니즘**

저가 개발capex가 mature EBITDA/NAV로 전환된다.

**T0 근거**

원문 development cost와 mature value 비교.

**숨은 가정**

유지·재식재·인프라 capex가 완전히 포함된다.

**사전 반증조건**

full-cycle after-tax ROIC가 자본비용 이하이면 반증.

**실제 결과**

장기 profit·net cash 축적은 높은 경제성을 지지한다.

**정량 gap**

cohort별 invested capital 부재로 20% exact test 불가.

**분석 오류 또는 제한**

spot margin을 full-cycle ROIC로 확장했다.

**재사용 교훈**

개발·유지·replanting capex를 cohort basis로 합산한다.

### C5. 내부재투자 runway — 성공

**원문 주장**

현금흐름을 신규식재·mill에 재투자해 per-share NAV를 키운다.

**경제적 메커니즘**

net cash와 저부채가 commodity cycle을 견디며 개발을 self-fund한다.

**T0 근거**

큰 undeveloped/immature base.

**숨은 가정**

capital allocation과 land access가 건전하다.

**사전 반증조건**

순현금 감소와 저수익 개발이 반복되면 반증.

**실제 결과**

2024까지 생산자산·순현금·순자산이 증가했다.

**정량 gap**

주당가치와 share count bridge는 추가 검증 필요.

**분석 오류 또는 제한**

회사 규모 증가를 자동으로 per-share compounding으로 봤다.

**재사용 교훈**

재투자는 incremental ROIC와 주당 NAV로 판정한다.

### C6. SQL 가격성과로 Long 성공 판정 — 무효

**원문 주장**

database price row가 아이디어 성과를 보여준다는 암묵 가정.

**경제적 메커니즘**

ticker-date price를 entry와 비교한다.

**T0 근거**

SQL AEP price $27대.

**숨은 가정**

ticker가 같은 법인·거래소·통화다.

**사전 반증조건**

회사·거래소가 다르면 즉시 폐기.

**실제 결과**

row는 NYSE American Electric Power로 판명됐다.

**정량 gap**

전체 horizon return 무효.

**분석 오류 또는 제한**

ticker 문자열만으로 entity를 매칭했다.

**재사용 교훈**

ISIN·exchange·currency·company name을 먼저 맞춘다.

---

## 4. 당시 Valuation과 Payoff Structure

원문의 핵심은 EV/ha를 replacement와 private transaction에 비교하고, immature ha의 mature yield를 별도로 더하는 SOTP였다. 정교한 모델은 hectare를 immature·young·prime·old로 나누고 각 yield curve, CPO margin, tax, development/replanting capex와 country haircut을 적용해야 한다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | CPO $750·yield 저하·개발중단 | 자산할인 지속 | 순현금으로 방어 |
| Base | immature maturation·보수적 CPO | 생산·NAV compounding | 장기 실현 |
| Bull | private $15k+/ha·높은 CPO | 큰 SOTP rerating | exact price 검증 안 함 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Planted value | $4.2k~5.2k/ha | replacement 이하 | 2024 NAV 축적 | 성공 방향 |
| 2012 FFB | 783.4k mt | maturation growth | +11% | 성공 |
| 2012 CPO | 260.5k mt | 증가 | +5% | 성공 |
| Net cash | $91.2m | 유지·증가 | 2024 $181.9m | 강한 성공 |
| SQL return | AEP $27대 | LSE 성과 | NYSE 타사 | 폐기 |

### 촉매와 시간

판정 horizon은 **수령 성숙과 재투자가 진행되는 3~7년**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2012-06-11 | VIC Long 게시 | low EV/ha·maturation |
| 2012-12-31 | FFB +11%·CPO +5% | 첫 운영 확인 |
| 2012-12-31 | net cash $91.2m | downside buffer |
| 2022-12-31 | age-profile chart | young/immature runway 확인 |
| 2024-12-31 | profit $67.5m·net cash $181.9m | 장기 compounding |
| 2025-11-24 | AEP Plantations로 사명 변경 | 법인은 연속·ticker 유지 |
| 2026-02-04 | 공식 name-change notice | entity mapping 갱신 |

### 실제 사업·자본구조 추이

2012 FFB는 783.4k mt(+11%), CPO는 260.5k mt(+5%)였고 CPO 평균가격이 하락해도 net cash $91.2m을 유지했다. 2024 revenue $372.3m, operating profit $81.7m, attributable profit $67.5m, net cash $181.9m, shareholder net assets $551.0m이었다. 회사는 2025-11-24 AEP Plantations로 사명을 바꿨지만 LSE ticker는 유지했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

SQL의 $27대 price series는 NYSE American Electric Power에 해당해 전부 rejected다. LSE corporate actions·GBP dividends를 복원한 별도 series 없이 exact return·MFE·MAE를 만들지 않는다. 사업·자산가치 판정과 주가성과 판정을 분리한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | planted ha를 replacement 이하에 매수 | 20% | 성공 방향 | exact LSE rerating은 미검증. |
| C2 | immature acreage가 내재성장 | 18% | 성공 | 연도별 cohort attribution은 제한. |
| C3 | low-cost palm oil economics | 18% | 대체로 성공 | cycle별 unit cost series는 미완전. |
| C4 | 20%+ planted-asset ROIC | 16% | 방향 성공·정밀 제한 | cohort별 invested capital 부재로 20% exact test 불가. |
| C5 | 내부재투자 runway | 16% | 성공 | 주당가치와 share count bridge는 추가 검증 필요. |
| C6 | SQL 가격성과로 Long 성공 판정 | 12% | 무효 | 전체 horizon return 무효. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

가치는 CPO spot multiple보다 이미 심은 나무의 생물학적 성숙, yield 증가, low-cost mill integration과 내부현금 재투자·net cash 축적에서 나왔다.

### Counterfactual

CPO가 $750/t로 5년 머물고 replanting·ESG capex가 두 배여도 mature ha와 net cash를 보수적으로 평가한 downside가 현재 EV를 지지하는가?

---

## 9. 분석 오류 유형과 최초 경고

per-ha private deal 비교에서 land title·age·mill·minority·country risk를 충분히 층화하지 않았고 exact shareholder return data를 확보하지 못했다.

### 최초로 관찰 가능했던 경고신호

commodity 가격하락은 관찰됐지만 balance sheet와 생산량이 버텼다. 사전 핵심경고는 yield/ha 하락과 net cash 소진이었으나 장기적으로 현실화하지 않았다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

plantation은 P/E보다 EV/ha를 tree-age·yield/ha·mill capacity와 함께 본다.

### Lesson 2

immature acreage는 성장설비지만 이미 쓴 capex와 앞으로 필요한 upkeep을 함께 반영한다.

### Lesson 3

ticker/entity가 틀리면 가격성과 전체를 폐기한다.

### 지금 같은 아이디어를 다시 본다면

- mature/immature ha
- FFB yield/ha
- extraction rate
- CPO unit margin
- replanting·development capex
- land title·certification
- net cash
- GBP total-return series

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 강한 성공 |
| Valuation thesis | 방향 성공 |
| Catalyst thesis | maturation 장기 실현 |
| Timing / path | commodity 혼합 |
| Data quality | SQL return 무효 |
| Thesis score | 8.8/10 |
| Process score | 9.7/10 |
| 종합 | **장기 성공 — 생산기반·순현금·순자산 compounding, SQL 성과행은 폐기** |

### 한 문장 교훈

> plantation은 P/E보다 EV/ha를 tree-age·yield/ha·mill capacity와 함께 본다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2012-06-11. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [AEP reports and presentations archive](https://aepplantations.com/investors/reports-and-presentations/) — AEP Plantations, 2026. 2012·2024·2025 annual report 공식 보관 위치.
3. [Anglo-Eastern Plantations 2024 annual report](https://www.angloeastern.co.uk/~/media/Files/A/Anglo-Eastern/reports-and-documents/AEP%20AR2024_Final.pdf) — Anglo-Eastern Plantations, 2025-04. 2024 생산·손익·net cash·순자산 검증.
4. [AEP Plantations official business overview](https://aepplantations.com/) — AEP Plantations, 2026. 현재 사업지역·상장·estate/mill 구조 검증.
5. [AEP official name-change notice](https://aepplantations.com/aep-plantations-plc-announces-official-name-change/) — AEP Plantations, 2026-02-04. 2025-11-24 사명변경과 ticker 유지 검증.
6. [AEP palm age and production charts](https://www.angloeastern.co.uk/~/media/Files/A/Anglo-Eastern/documents/Charts%202022.pdf) — Anglo-Eastern Plantations, 2022-12-31. immature·young·prime·old age mix와 생산 추이 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **REJECTED** — ticker collision으로 wrong-company 가격행을 폐기했다.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
