# Diamond Sports Group, LLC — 2020-02-05 — V9

> **Batch 055 canonical report.** Raw SQL `Short`를 원문 action/payoff로 감사해 **Short**으로 확정했다. Research as-of 2026-09-15.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 원 ticker | Diamond Sports Group, LLC / SBGI |
| 실제 Security | **6.625% senior unsecured notes due 2027** |
| Idea ID | `82eaec90-3559-4161-a7d7-7f12b8506646` |
| 게시일 / 작성자 | 2020-02-05 / burlap |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Short** |
| 기준가격 | 약 95 cents |
| 원 horizon | 12~36개월 |
| 최종 판정 | **2023 Chapter 11·대규모 debt elimination으로 credit thesis 강한 성공** |

> **결론:** raw ticker는 SBGI지만 실제 security는 Diamond Sports 6.625% unsecured notes due 2027 Short @ 약 95다. Base 80, short에 불리한 case 104, severe case insolvency를 두고 acquisition LTV가 80%에서 100%+로 악화됐으며 FCF/debt<5%, DISH blackout·subscriber churn과 rights-cost escalator가 unsecured par을 위협한다고 봤다. 결과적으로 **2023 Chapter 11·대규모 debt elimination으로 credit thesis 강한 성공**.

---

## 1. 회사는 정확히 무엇을 하는가

Diamond Sports Group은 지역 스포츠 네트워크에서 `MVPD/vMVPD 가입자×affiliate fee+광고-sports rights escalator-production-distribution-corporate cost-interest`를 번다. 가입자와 carriage가 줄어도 다년간 rights payment는 빠르게 내려가지 않아 operating leverage가 역방향으로 작동한다. credit 분석에서는 positive EBITDA나 FCF보다 secured/unsecured priority, current asset value 대비 LTV, cash interest, rights commitments, distribution renewal과 liability-management transaction을 먼저 본다. Sinclair parent에 non-recourse라는 문구는 Diamond 채권자에게 protection이 아니라 parent support가 제한될 수 있다는 뜻이다.

### Security cash waterfall

Affiliate-fee·광고 현금에서 rights payment·production·opex·cash interest·필수 capex를 빼고, first-lien/secured debt와 DIP·administrative claim을 먼저 지급한다. 남는 enterprise recovery를 unsecured face에 배분하며 Sinclair parent support는 계약상 보장되지 않는다.

### 분기/사건별 KPI

- 원문 핵심 unit economics와 실제 현금전환
- funding·regulatory capital·unencumbered liquidity
- per-share book/EPS와 share count
- catalyst gate, 예상일·실제일·실패조건
- target multiple과 successor security를 포함한 terminal payoff

---

## 2. 당시 상황과 시장이 가격에 넣은 것

raw ticker는 SBGI지만 실제 security는 Diamond Sports 6.625% unsecured notes due 2027 Short @ 약 95다. Base 80, short에 불리한 case 104, severe case insolvency를 두고 acquisition LTV가 80%에서 100%+로 악화됐으며 FCF/debt<5%, DISH blackout·subscriber churn과 rights-cost escalator가 unsecured par을 위협한다고 봤다.

### Reverse expectations

약 95 cents가 정당화하려면 시장이 어느 매출·margin·loss·funding·capital·event 확률을 넣었는지 역산한다. 원문의 낙관/비관 시나리오와 가격의 암묵적 시나리오를 같은 단위로 맞춰야 한다. 단순히 싸다거나 비싸다는 설명은 claim이 아니다.

---

## 3. 원문 투자논지 지도

### C1. top-tick LTV — 20%

- **원문 주장:** purchase 뒤 LTV가 100%를 넘는다.
- **T0 근거:** carriage loss·lower asset value
- **숨은 가정:** rights value가 회복되지 않는다.
- **사전 반증조건:** LTV<80% 회복이면 반증.
- **실제:** Chapter 11·debt elimination
- **판정:** **강한 성공**
- **재사용 교훈:** credit LTV는 current value로 갱신한다.

### C2. FCF is insufficient — 18%

- **원문 주장:** positive FCF라도 debt의 5% 미만이면 안전하지 않다.
- **T0 근거:** FCF/debt<5%
- **숨은 가정:** rights·interest가 경직적이다.
- **사전 반증조건:** sustained deleveraging이면 반증.
- **실제:** restructuring
- **판정:** **성공**
- **재사용 교훈:** positive FCF와 debt service capacity를 구분한다.

### C3. distribution erosion — 18%

- **원문 주장:** DISH drop과 renewals가 structural하다.
- **T0 근거:** blackout·cord-cutting
- **숨은 가정:** 다른 MVPD도 강경해진다.
- **사전 반증조건:** subscriber 안정·renewal 개선이면 반증.
- **실제:** carriage pressure 지속
- **판정:** **성공**
- **재사용 교훈:** revenue contract duration을 본다.

### C4. rights escalator — 16%

- **원문 주장:** sports-rights cost가 revenue보다 느리게 내려간다.
- **T0 근거:** long-term contracts
- **숨은 가정:** termination/renegotiation이 어렵다.
- **사전 반증조건:** cost reset이 revenue decline을 앞서면 반증.
- **실제:** Chapter 11에서 계약조정
- **판정:** **성공**
- **재사용 교훈:** fixed cost duration을 debt처럼 본다.

### C5. unsecured mispricing — 16%

- **원문 주장:** 95의 unsecured는 priority risk를 반영하지 못한다.
- **T0 근거:** secured debt ahead·exchange capacity
- **숨은 가정:** priming이 가능하다.
- **사전 반증조건:** asset coverage 충분 시 반증.
- **실제:** secured exchanges·principal impairment
- **판정:** **강한 성공**
- **재사용 교훈:** liability management 전 priority를 그린다.

### C6. Short security — 12%

- **원문 주장:** SBGI common이 아니라 Diamond 2027 bond Short다.
- **T0 근거:** coupon/maturity/payoff
- **숨은 가정:** 동일 instrument를 추적한다.
- **사전 반증조건:** common thesis면 반증.
- **실제:** security 교정
- **판정:** **성공**
- **재사용 교훈:** issuer·security·seniority를 분리한다.

---

## 4. 당시 Valuation과 Payoff Structure

95에서 80은 15-point gross downside지만 coupon carry·borrow·cover date가 필요하다. 핵심은 maturity yield가 아니라 current enterprise value가 secured+unsecured debt와 fixed rights commitments를 덮는지다. >100% LTV이면 시간이 많아도 unsecured recovery는 rights renegotiation·carriage·priority에 민감하다.

### 시나리오 구조

| 시나리오 | 필요한 조건 | common payoff |
|---|---|---|
| Bear | 첫 반증조건 발생·funding/capital 악화 | Short 손실, duration 확대 또는 recovery 훼손 |
| Base | 핵심 KPI 절반 이상과 catalyst 일부 실현 | valuation gap 일부 축소 |
| Bull | operating claim·capital·catalyst가 동시에 실현 | 2023 Chapter 11·대규모 debt elimination으로 credit thesis 강한 성공의 상단, 단 exact return은 별도 검증 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Bond | 6.625% 2027 @95 | Base 80 | Chapter 11 | 강한 성공 |
| LTV | >100% | coverage 악화 | 대규모 debt elimination | 강한 성공 |
| FCF/debt | <5% | deleveraging 불충분 | restructuring 지속 | 성공 |
| Distribution | DISH blackout | 추가 renewal risk | carriage pressure 지속 | 성공 |
| Priority | unsecured | priming 위험 | secured exchanges | 강한 성공 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2019-08 | RSN acquisition close | 약 $10.6bn top-tick |
| 2020-02-05 | bond Short | 95→80 |
| 2020-06 | 12.75% secured exchange | priority deterioration |
| 2021~22 | subscriber·renewal 압력 | cash duration 감소 |
| 2022 | 추가 debt exchange | distress 심화 |
| 2023-03-14 | Chapter 11 | insolvency 현실화 |
| 2024~25 | plan·emergence | debt 대폭 제거 |

### 실제 사업·자본구조

2020 2027 unsecured를 12.75% secured debt로 바꾸는 exchange가 시작됐고 2022 추가 liability management가 이어졌다. Diamond는 2023-03-14 Chapter 11을 신청해 약 $8bn debt elimination을 추진했고 2025 emergence 때 debt는 대폭 축소됐다. par-credit가 principal impairment asset으로 바뀌었다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

첨부 SQL에는 catalyst 287자만 있고 description·performance는 없다. 95/80/104와 Chapter 11·debt elimination은 thesis/event anchors다. coupon, trade price, borrow/cover를 복원하지 못해 exact short return/IRR은 null이다.

이번 10건은 첨부 SQL에 performance row가 없으므로 1개월~5년 수익률을 만들지 않는다. 사건 성공, 기업 생존, target 도달과 투자 total return을 각각 별도 필드로 둔다. corporate action이 있으면 successor security까지 연결돼야 정확한 IRR을 계산할 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | top-tick LTV | 20% | 강한 성공 | credit LTV는 current value로 갱신한다. |
| C2 | FCF is insufficient | 18% | 성공 | positive FCF와 debt service capacity를 구분한다. |
| C3 | distribution erosion | 18% | 성공 | revenue contract duration을 본다. |
| C4 | rights escalator | 16% | 성공 | fixed cost duration을 debt처럼 본다. |
| C5 | unsecured mispricing | 16% | 강한 성공 | liability management 전 priority를 그린다. |
| C6 | Short security | 12% | 성공 | issuer·security·seniority를 분리한다. |

가중치 합계는 100%다. Direction·business·valuation·catalyst·timing·security selection을 한 점수로 섞지 않았다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익 방향을 만든 것은 EBITDA가 아직 positive인지가 아니라 subscriber revenue duration보다 rights cost와 debt가 길고 고정돼 있었다는 점이다. non-recourse는 parent를 보호하지만 Diamond unsecured에는 support 부재를 뜻했고, liability management가 priority를 더 악화시켰다.

### 인과 분해

1. T0에 이미 관찰 가능했던 가격·계약·balance-sheet edge를 먼저 둔다.
2. 이후 새로 발생한 macro·regulation·management event를 분리한다.
3. 기업 결과와 common security payoff를 구분한다.
4. hindsight terminal fact가 원래 horizon에 관찰 가능했는지 표시한다.

### Counterfactual

핵심 catalyst가 없었어도 약 95 cents에서 같은 방향의 기대수익이 충분했는가? 그렇지 않다면 이 아이디어는 cheap compounder가 아니라 event timing trade이며, catalyst clock을 넘기면 재승인이 필요하다.

---

## 9. 분석 오류 유형과 최초 경고

Base 80은 강한 credit deterioration에 비해 보수적이었으나 timing은 exchange·liquidity runway에 따라 길어질 수 있었다. team별 rights termination value, secured priming capacity와 restructuring recovery waterfall을 더 세밀히 모델링해야 했다.

### 최초 관찰 가능한 경고/반증

DISH blackout 지속, 다른 주요 MVPD renewal 악화, FCF/debt<5% 유지와 secured exchange 제안 중 하나가 발생하면 insolvency weight를 높인다. 반대로 subscriber stabilization·rights reset·LTV<80%가 확인되면 cover한다.

### 사후편향 방지

최종 인수·파산·합병을 알고 T0 논지를 다시 쓰지 않는다. 다만 원문이 무엇을 잘못 측정했는지 확인하기 위해 당시 확인 가능했던 covenant, spread, MLR, book, capex와 법적 gate를 사용한다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity audit:** `SBGI`를 단일 회사로 보지 말고 Diamond Sports Group, LLC 법인·날짜·실제 security로 고정한다.
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
| Entity / direction | raw Short → **Short**, Diamond Sports Group, LLC |
| Business thesis | 성공 |
| Valuation thesis | 강한 성공 |
| Catalyst / timing | 2023 Chapter 11·대규모 debt elimination으로 credit thesis 강한 성공 |
| Thesis score | 9.8/10 |
| Process score | 9.8/10 |
| Outcome-adjusted score | 9.8/10 |

### 한 문장 교훈

> credit LTV는 current value로 갱신한다.

---

## 12. Sources / Validation Notes

1. 첨부 SQL catalyst / prior curated metadata — VIC_IDEAS(4).sql / VIC / repository prior overlay, 2020-02-05. idea_id·catalyst 287 chars·description absent; date·author·raw flag·원문 anchor는 prior overlay 대조
2. [Sinclair RSN acquisition](https://sbgi.net/sinclair-broadcast-group-to-acquire-21-regional-sports-networks-from-disney-at-a-valuation-of-10-6-billion/) — Sinclair, 2019-05-03. $10.6bn purchase value와 financing context
3. [2020 Diamond exchange completion](https://www.sec.gov/Archives/edgar/data/912752/000091275220000054/exhibit991-pressreleas.htm) — SEC / Sinclair, 2020-06. 2027 unsecured와 secured exchange
4. [2022 Diamond exchange](https://www.sec.gov/Archives/edgar/data/912752/000091275222000014/dsgexchangeofferandconsent.htm) — SEC / Sinclair, 2022. 추가 liability management
5. [Diamond Chapter 11 case](https://cases.ra.kroll.com/DSG/) — Kroll Restructuring Administration, 2023-2025. Chapter 11 docket·plan·final decree
6. [Diamond Chapter 11 announcement](https://www.businesswire.com/news/home/20230314006050/en/Diamond-Sports-Group-Commences-Voluntary-Chapter-11-Proceedings-to-Strengthen-Balance-Sheet-and-Continue-Broadcasting-Local-Sports-Nationwide) — Diamond Sports Group, 2023-03-14. 약 $8bn debt elimination 계획
7. [Sinclair-Diamond settlement](https://www.sec.gov/Archives/edgar/data/912752/000197121324000003/pressreleasedated11724.htm) — SEC / Sinclair, 2024-01-17. intercompany litigation과 cash settlement

### 데이터 품질

- 원문·metadata: **C** — 첨부 SQL에는 Batch 055 catalyst만 있고 description은 0건이다. date·author·raw flag·원문 수치는 prior curated overlay로 provenance를 분리했다.
- 기업·사건: **A/B** — SEC·FCC·회사·법원/구조조정 자료로 segment 결과와 terminal event를 검증했다.
- 가격성과: **C** — 현 첨부 SQL에는 performance COPY가 없다. 거래가·채권 사건을 exact return으로 바꾸지 않고 return/IRR을 null로 유지했다.
- 교정: ticker=SBGI, entity=Diamond Sports Group, LLC, raw=Short, research=Short.
