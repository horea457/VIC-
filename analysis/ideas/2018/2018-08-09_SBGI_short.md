# Sinclair Broadcast Group, Inc. — 2018-08-09 — V9

> **Batch 055 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Short**으로 확정했다. Research as-of 2026-09-15.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Sinclair Broadcast Group, Inc. / SBGI |
| 실제 Security | **Sinclair Class A common stock** |
| Idea ID | `7a3adc85-2f3c-4244-a076-98fc1553101c` |
| 게시일 / 작성자 | 2018-08-09 / JSTC |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Short** |
| 기준가격 | 원문 가격 미복원 |
| 원 horizon | 6~18개월 |
| 최종 판정 | **legal size·timing은 실패, capital-allocation 경고는 후일 적중** |

> **결론:** raw Short와 실제 방향은 일치하지만 Diamond mapping은 틀렸고 대상은 Sinclair common이다. Tribune이 거래를 종료·소송한 당일 legal damages, $1bn buyback의 실질성 부족, regulator credibility와 future M&A franchise 훼손을 근거로 standalone Short 또는 peer hedge를 제안했다. 결과적으로 **legal size·timing은 실패, capital-allocation 경고는 후일 적중**.

---

## 1. 회사는 정확히 무엇을 하는가

Sinclair Broadcast Group은 local television stations, digital assets와 시기별 비핵심 미디어 투자를 보유했다. 방송 현금엔진은 `local/national/political 광고+MVPD/vMVPD 가입자×retrans fee-network reverse compensation-station opex-corporate-maintenance capex-interest-tax`다. retrans와 정치광고가 성장을 만들 수 있지만 cord-cutting, network fees, 규제 ownership cap과 acquisitive capital allocation이 duration을 줄인다. 따라서 levered FCF yield는 영구수익률이 아니라 even/odd 정치주기 평균과 runoff 기간, debt·legal reserve·share count를 거쳐 common에 귀속시켜야 한다.

### Security cash waterfall

사업 현금에서 운전자본·maintenance/growth investment·interest·tax·법적 준비금을 차감하고, debt와 계약상 senior claim을 먼저 지급한 뒤의 per-share 현금만 common payoff로 본다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw Short와 실제 방향은 일치하지만 Diamond mapping은 틀렸고 대상은 Sinclair common이다. Tribune이 거래를 종료·소송한 당일 legal damages, $1bn buyback의 실질성 부족, regulator credibility와 future M&A franchise 훼손을 근거로 standalone Short 또는 peer hedge를 제안했다.

### Reverse expectations

원문 가격 미복원가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. deal is dead — 20%

- **원문 주장:** Tribune 거래는 되살아나지 않는다.
- **T0 근거:** termination filing
- **숨은 가정:** 새 합의가 없다.
- **사전 반증조건:** deal revival이면 반증.
- **실제:** 종료 확정
- **판정:** **성공**
- **재사용 교훈:** 종료 사실과 추가 downside를 분리한다.

### C2. $1bn damages — 18%

- **원문 주장:** 큰 cash damages가 equity를 훼손한다.
- **T0 근거:** Tribune complaint
- **숨은 가정:** claim이 settlement로 실현된다.
- **사전 반증조건:** low-cash settlement면 반증.
- **실제:** $1bn cash 배상 아님
- **판정:** **실패**
- **재사용 교훈:** claim amount에 probability·time을 곱한다.

### C3. buyback empty — 18%

- **원문 주장:** $1bn authorization은 실행하기 어렵다.
- **T0 근거:** leverage·legal overhang
- **숨은 가정:** 현금보존이 우선이다.
- **사전 반증조건:** material repurchase면 반증.
- **실제:** 실제 repurchase
- **판정:** **부분 실패**
- **재사용 교훈:** authorization와 execution을 분기별로 본다.

### C4. M&A franchise lost — 16%

- **원문 주장:** 규제평판이 future deals를 막는다.
- **T0 근거:** FCC candor issue
- **숨은 가정:** seller/lender도 회피한다.
- **사전 반증조건:** 새 대형 deal이면 반증.
- **실제:** 2019 RSN 인수
- **판정:** **단기 실패**
- **재사용 교훈:** option impairment와 완전소멸을 구분한다.

### C5. capital allocation risk — 16%

- **원문 주장:** owner-control이 나쁜 다음 거래를 부를 수 있다.
- **T0 근거:** aggressive Tribune structure
- **숨은 가정:** governance가 바뀌지 않는다.
- **사전 반증조건:** deleveraging·환원 우선이면 반증.
- **실제:** Diamond 파산 경로
- **판정:** **장기 강한 성공**
- **재사용 교훈:** governance는 반복행동으로 검증한다.

### C6. Short direction/entity — 12%

- **원문 주장:** 실제 Sinclair common Short다.
- **T0 근거:** standalone short 문구
- **숨은 가정:** borrow와 hedge가 가능하다.
- **사전 반증조건:** positive target이면 반증.
- **실제:** raw direction 일치·entity 교정
- **판정:** **성공**
- **재사용 교훈:** security resolve 후 성과를 본다.

---

## 4. 당시 Valuation과 Payoff Structure

Short payoff는 claim amount가 아니라 expected settlement×지급시기, buyback 실행 cash, standalone broadcast FCF와 reputation이 future deal multiple에 주는 영향을 합쳐야 한다. 소송이 길어져도 현금손실이 작거나 주가에 선반영되면 carry·squeeze가 커진다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Short 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | legal size·timing은 실패, capital-allocation 경고는 후일 적중의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Legal damages | 최대 약 $1bn 우려 | equity hit | $1bn cash 배상 아님 | 실패 |
| Buyback | $1bn authorization | 실행 제약 | 후속 repurchase 실행 | 부분 실패 |
| M&A franchise | 훼손 | future deals 감소 | 2019 $10.6bn RSN deal | 단기 실패 |
| Governance | 공격적 배분 | discount 확대 | Diamond value destruction | 장기 성공 |
| Short timing | deal-break 당일 | 6~18개월 | 2019 반등 구간 | 혼합 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2018-07 | FCC HDO | deal risk 현실화 |
| 2018-08-09 | Tribune termination·lawsuit | Short 시작 |
| 2018-08 | $1bn buyback authorization | squeeze/credibility 변수 |
| 2019-05 | $10.6bn RSN deal | M&A franchise 지속 |
| 2020-01 | Tribune litigation settlement | cash-damage thesis 약화 |
| 2020~22 | Diamond restructuring | governance 우려 현실화 |
| 2023-03 | Diamond Chapter 11 | 다른 경로의 장기 적중 |

### 실제 사업·자본구조

litigation은 2020까지 이어졌지만 $1bn 현금배상으로 끝나지 않았다. Sinclair는 후속 repurchase를 실제 수행했고 2019에는 $10.6bn 가치의 RSN 인수를 발표해 M&A capacity가 완전히 사라지지 않았다. 다만 바로 그 aggressive capital allocation이 Diamond 파산과 parent settlement로 이어져 governance 우려는 다른 경로로 적중했다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

첨부 SQL에는 95자 catalyst만 있고 description·performance는 없다. intraday 반응·후속 2019 반등을 exact short return으로 계산하지 않는다. borrow, cover date와 distribution이 없어 return/IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | deal is dead | 20% | 성공 | 종료 사실과 추가 downside를 분리한다. |
| C2 | $1bn damages | 18% | 실패 | claim amount에 probability·time을 곱한다. |
| C3 | buyback empty | 18% | 부분 실패 | authorization와 execution을 분기별로 본다. |
| C4 | M&A franchise lost | 16% | 단기 실패 | option impairment와 완전소멸을 구분한다. |
| C5 | capital allocation risk | 16% | 장기 강한 성공 | governance는 반복행동으로 검증한다. |
| C6 | Short direction/entity | 12% | 성공 | security resolve 후 성과를 본다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

단기 Short의 직접 catalyst였던 cash damages는 과대평가됐고 buyback·새 deal이 squeeze를 만들 수 있었다. 장기 손실은 Tribune lawsuit보다 management가 core 방송 현금을 고레버리지 RSN에 재투자한 데서 발생했다. 후일의 다른 실패로 원 Short timing을 사후 정당화하면 안 된다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 원문 가격 미복원에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

complaint claim과 expected cash settlement를 혼동하고, event break 당일 이미 반영된 damage와 앞으로 새로 발생할 damage를 분리하지 않았다. buyback ability와 대체 M&A, borrow/carry·relative hedge 실행을 수치화하지 않았다.

### 최초 관찰 가능한 경고/반증

소송에서 현금 damages probability가 낮아지거나 분기 buyback이 authorization의 10% 이상 실행되고 새 accretive deal financing이 열리면 cover한다. governance thesis는 별도 장기 관찰로 넘긴다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `SBGI`를 단일 회사로 보지 말고 Sinclair Broadcast Group, Inc. 법인·날짜·실제 security로 고정한다.
2. **Direction audit:** raw Short가 아니라 원문 payoff를 읽어 Short을 확정한다.
3. **Bridge:** target을 EPS/book/NAV와 cash waterfall로 연결한다.
4. **Falsifier:** 최초 경고에 날짜와 수치를 둔다.
5. **Path:** 원 horizon과 terminal event를 섞지 않는다.
6. **Missing data:** SQL performance가 없으면 null을 유지한다.

### 다시 분석한다면

- legal/capital/funding gate를 확률·날짜별로 나눈다.
- gross asset value와 common에 귀속되는 순가치를 분리한다.
- base/bull target뿐 아니라 survival/recovery case를 수치화한다.
- corporate action 이후 교환비율·배당·successor price를 연결해 total return을 복원한다.
- event가 맞아도 price target이 실패할 수 있도록 exit/cover rule을 미리 쓴다.

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Entity / direction | raw Short → **Short**, Sinclair Broadcast Group, Inc. |
| Business thesis | 실패 |
| Valuation thesis | 실패 |
| Catalyst / timing | legal size·timing은 실패, capital-allocation 경고는 후일 적중 |
| Thesis score | 5.3/10 |
| Process score | 7.2/10 |
| Outcome-adjusted score | 6.2/10 |

### 한 문장 교훈

> 종료 사실과 추가 downside를 분리한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL catalyst / prior curated metadata — VIC_IDEAS(4).sql / VIC / repository prior overlay, 2018-08-09. idea_id·catalyst 95 chars·description absent; date·author·raw flag·원문 anchor는 prior overlay 대조
2. [Sinclair SEC archive](https://www.sec.gov/edgar/browse/?CIK=912752&owner=exclude) — SEC / Sinclair, 1995-2025. 방송·부채·M&A·Diamond 연속성
3. [Sinclair 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/912752/000091275216000020/sbgi-20151231x10k.htm) — SEC / Sinclair, 2016-02. broadcast·retrans·leverage와 지배구조
4. [Sinclair FY2016 results](https://sbgi.net/sinclair-reports-fourth-quarter-2016-financial-results/) — Sinclair, 2017-03. 2016 매출·영업이익·정치광고
5. [Sinclair 2017 Form 10-K](https://www.sec.gov/Archives/edgar/data/912752/000091275218000006/sbgi-20171231x10k.htm) — SEC / Sinclair, 2018-03. spectrum $310.8m·사업·자본배분
6. [Tribune merger termination](https://www.sec.gov/Archives/edgar/data/726513/000119312518248520/d560189d8k.htm) — SEC / Tribune Media, 2018-08-09. Sinclair 거래 종료와 소송
7. [RSN acquisition announcement](https://sbgi.net/sinclair-broadcast-group-to-acquire-21-regional-sports-networks-from-disney-at-a-valuation-of-10-6-billion/) — Sinclair, 2019-05-03. 21 RSN·$10.6bn enterprise value
8. [2021 Diamond A/R facility](https://www.sec.gov/Archives/edgar/data/912752/000091275221000078/arfacilitypressrelease11521.htm) — SEC / Sinclair, 2021-11-05. Sinclair의 약 $184.4m lender-obligation 인수
9. [2022 Diamond exchange](https://www.sec.gov/Archives/edgar/data/912752/000091275222000014/dsgexchangeofferandconsent.htm) — SEC / Sinclair, 2022. Diamond debt exchange와 restructuring
10. [2024 Sinclair-Diamond settlement](https://www.sec.gov/Archives/edgar/data/912752/000197121324000003/pressreleasedated11724.htm) — SEC / Sinclair, 2024-01-17. $495m cash settlement·litigation resolution
11. [Sinclair 2024 annual report](https://www.sec.gov/Archives/edgar/data/1971213/000197121325000031/finalannualreport2024.pdf) — SEC / Sinclair, 2025. Diamond emergence·parent exposure 후속검증

### 데이터 품질

- 원문·metadata: **C** — 첨부 SQL에는 Batch 055 catalyst만 있고 description은 0건이다. date·author·raw flag·원문 수치는 prior curated overlay로 provenance를 분리했다.
- 기업·사건: **A/B** — SEC·FCC·회사·법원/구조조정 자료로 segment 결과와 terminal event를 검증했다.
- 가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. 거래가·채권 사건을 exact return으로 바꾸지 않고 return/IRR을 null로 유지했다.
- 교정: ticker=SBGI, entity=Sinclair Broadcast Group, Inc., raw=Short, research=Short.
