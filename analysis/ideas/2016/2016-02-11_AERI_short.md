# Aerie Pharmaceuticals (AERI) — 2016-02-11 VIC Short

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Aerie Pharmaceuticals / AERI |
| VIC 게시일 / 작성자 | 2016-02-11 / Napoleon |
| 분석 증권 / 실제 방향 | AERI common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 $14.16 |
| 기대기간 | 승인·상업화 및 terminal outcome |
| raw horizon audit | Rhopressa TAM ~$100m vs bull ~$350m |
| 최종 판정 | **fundamental 일부 적중 / terminal Short 실패** |

> **결론:** Rhopressa+Rocklatan 2021 제품매출 $112.1m과 순손실 $74.8m은 작은 TAM·cash burn 논지를 지지했다. 그러나 두 제품이 승인됐고 Alcon이 $15.25 cash에 인수해 $14.16 short는 borrow 전에도 terminal loss였다.

---

## 1. 회사는 정확히 무엇을 하는가

Aerie Pharmaceuticals는 녹내장·고안압 치료제 Rhopressa와 복합제 Rocklatan을 개발·상업화한 안과 전문 바이오텍이었다. 가치는 승인확률×시장침투×순가격에서 임상·영업조직·R&D·자금조달비용을 뺀 현금흐름과 후속 파이프라인·전략적 인수가치로 구성된다. 따라서 작은 상업 TAM을 맞혀도 FDA binary와 buyer option value가 short payoff를 뒤집을 수 있다.

net product revenue × gross margin - commercial SG&A - R&D - interest = cash burn/FCF; approval확률·희석·borrow·M&A consideration을 common short payoff에 적용한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

FDA/label, prescription growth, net price, product revenue, gross margin, commercial SG&A, cash burn, cash runway, diluted shares, borrow cost, strategic interest

---

## 2. 당시 상황과 시장이 가격에 넣은 것

bull은 Rhopressa를 $350m급 franchise로 평가했다. 원문은 efficacy·side effects·physician adoption과 약 100명 salesforce 비용을 반영하면 약 $100m 사업에 가깝고 dilution이 필요하다고 봤다.

### Reverse expectations

가격은 approval·commercial platform·Rocklatan option과 strategic buyer value를 반영했다. short는 TAM뿐 아니라 FDA binary와 M&A premium을 이겨야 했다.

---

## 3. 원문 투자논지 지도

### C1. Rhopressa TAM 과대 — 대체로 성공

**원문 주장**

$350m bull TAM은 과도.

**경제적 메커니즘**

효능·adoption이 penetration 제한.

**T0 근거**

bear ~$100m.

**숨은 가정**

combined revenue 비교 가능.

**사전 반증조건**

revenue $250m+면 반증.

**실제 결과**

2021 combined $112.1m.

**정량 gap**

bear와 근접.

**분석 오류 또는 제한**

combination 포함 비교.

**재사용 교훈**

제품별 매출을 분리.

### C2. 차별성 제한 — 부분 성공

**원문 주장**

임상차별성이 adoption을 제한.

**경제적 메커니즘**

의사 처방·side effect.

**T0 근거**

원문 clinical view.

**숨은 가정**

승인·label은 가능.

**사전 반증조건**

빠른 broad adoption이면 반증.

**실제 결과**

승인됐지만 ramp 제한.

**정량 gap**

약은 성공, blockbuster 아님.

**분석 오류 또는 제한**

approval와 commercial success 혼동.

**재사용 교훈**

label·persistence 추적.

### C3. commercial cash burn — 성공

**원문 주장**

salesforce가 owner earnings를 압박.

**경제적 메커니즘**

SG&A fixed cost.

**T0 근거**

독립 commercialization.

**숨은 가정**

gross margin이 opex 못 덮음.

**사전 반증조건**

FCF breakeven이면 반증.

**실제 결과**

2021 net loss $74.8m.

**정량 gap**

손실 지속.

**분석 오류 또는 제한**

손실의 R&D/launch 분해 제한.

**재사용 교훈**

매출 대비 SG&A·R&D bridge.

### C4. dilution/financing — 부분 성공

**원문 주장**

장기 손실로 자금조달 필요.

**경제적 메커니즘**

cash burn→shares/convert.

**T0 근거**

임상단계 balance sheet.

**숨은 가정**

capital access.

**사전 반증조건**

self-funded 전환이면 반증.

**실제 결과**

손실 지속, 그러나 sale로 종결.

**정량 gap**

collapse 미발생.

**분석 오류 또는 제한**

financing을 terminal로 과신.

**재사용 교훈**

runway와 buyer option 병행.

### C5. FDA downside — 실패

**원문 주장**

regulatory/clinical risk가 value 훼손.

**경제적 메커니즘**

approval binary.

**T0 근거**

개발자산.

**숨은 가정**

FDA 승인 실패 가능.

**사전 반증조건**

두 제품 승인 시 반증.

**실제 결과**

Rhopressa·Rocklatan 승인.

**정량 gap**

핵심 binary 반대.

**분석 오류 또는 제한**

확률 calibration 부족.

**재사용 교훈**

base rate와 label 확률.

### C6. common short payoff — 실패

**원문 주장**

fundamental miss가 주가하락으로 전환.

**경제적 메커니즘**

cash burn·dilution.

**T0 근거**

$14.16 entry.

**숨은 가정**

M&A premium 제한.

**사전 반증조건**

takeout above entry면 실패.

**실제 결과**

$15.25 cash.

**정량 gap**

+7.7% underlying, borrow 전.

**분석 오류 또는 제한**

M&A tail 누락.

**재사용 교훈**

strategic value를 확률가중.

---

## 4. 당시 Valuation과 Payoff Structure

낙관적 $350m revenue에서도 commercial opex를 차감한 EPS 약 $1.58, 약 9x라는 역산이었다. 하지만 strategic buyer는 standalone EPS가 아니라 portfolio·pipeline value를 지불했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear/short | approval·TAM 부진 | 큰 하락 | TAM만 부분 적중 |
| Base | ~$100m business | 제한 가치 | $112.1m |
| Strategic | buyer premium | short loss | $15.25 takeout |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Short entry | $14.16 | 하락 | $15.25 terminal | 실패 |
| Bull TAM | ~$350m | 과대 | combined $112.1m | bearish view 지지 |
| Bear TAM | ~$100m | ~$100m | $112.1m | 근접 |
| 2021 net loss | cash burn | 지속 손실 | $74.8m | 성공 |
| Takeout premium | 미모델링 | 없음 | 37% to prior close | tail 실패 |

### 촉매와 시간

판정 horizon은 **승인·상업화 및 terminal outcome**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2016-02-11 | VIC Short | TAM·burn thesis |
| 2017-12-18 | Rhopressa FDA approval | binary 반증 |
| 2018-04 | commercial launch | revenue 시작 |
| 2019-03 | Rocklatan approval | option value 확대 |
| 2020 | 제품매출 $83.1m | 상업화 진행 |
| 2021 | 매출 $112.1m | TAM 근접 |
| 2021 | 순손실 $74.8m | burn 지속 |
| 2022-11 | Alcon $15.25 close | terminal short 실패 |

### 실제 사업·자본구조 추이

Rhopressa 2017, Rocklatan 2019 승인. 2021 combined product revenue $112.1m, net loss $74.8m. 2022 Alcon이 $15.25 cash, 약 $770m equity value로 인수했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

중간 SQL performance row는 없어 exact borrow-adjusted IRR을 만들지 않는다. terminal $15.25는 entry $14.16보다 7.7% 높아 borrow 전 short 손실이다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | Rhopressa TAM 과대 | 20% | 대체로 성공 | bear와 근접. |
| C2 | 차별성 제한 | 18% | 부분 성공 | 약은 성공, blockbuster 아님. |
| C3 | commercial cash burn | 18% | 성공 | 손실 지속. |
| C4 | dilution/financing | 16% | 부분 성공 | collapse 미발생. |
| C5 | FDA downside | 16% | 실패 | 핵심 binary 반대. |
| C6 | common short payoff | 12% | 실패 | +7.7% underlying, borrow 전. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

commercial forecast의 edge보다 regulatory success와 strategic option value가 security payoff를 지배했다.

### Counterfactual

$100m revenue와 지속 손실을 정확히 맞혀도 buyer가 $15.25를 낼 확률을 반영한 expected short return은 양수였는가?

---

## 9. 분석 오류 유형과 최초 경고

business-size forecast를 stock short payoff로 직결하고 M&A/approval convexity를 충분히 가격화하지 않았다.

### 최초로 관찰 가능했던 경고신호

2017-12 Rhopressa FDA approval이 core binary short thesis의 첫 명확한 반증이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

작은 TAM을 맞혀도 전략적 buyer가 option value에 premium을 지불하면 biotech short는 실패할 수 있다.

### Lesson 2

FDA binary, borrow cost와 M&A tail을 별도 payoff로 모델링한다.

### Lesson 3

매출과 owner earnings 사이의 commercial fixed cost를 명시한다.

### Lesson 4

제품 실패 확률과 회사가치 하락 확률을 동일시하지 않는다.

### Lesson 5

terminal cash consideration이 있으면 정확한 short ledger의 기준점으로 사용한다.

### 지금 같은 아이디어를 다시 본다면

- approval probability
- label/efficacy
- gross-to-net
- cash runway/dilution
- borrow+M&A premium

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 부분 성공 |
| Valuation thesis | 부분 성공 |
| Catalyst thesis | approval 실패 |
| Security payoff | terminal 실패 |
| Timing / path | 장기 보유 불리 |
| Thesis score | 5.7/10 |
| Process score | 5.8/10 |
| 종합 | **fundamental 일부 적중 / terminal Short 실패** |

### 한 문장 교훈

> 작은 TAM을 맞혀도 전략적 buyer가 option value에 premium을 지불하면 biotech short는 실패할 수 있다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2016-02-11. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준.
2. [Rhopressa FDA approval announcement](https://www.sec.gov/Archives/edgar/data/1337553/000119312517372035/d705067dex991.htm) — SEC / Aerie Pharmaceuticals, 2017-12-18. Rhopressa approval로 core binary short catalyst 반증.
3. [Rocklatan FDA approval package](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2019/208259Orig1s000Approv.pdf) — U.S. FDA, 2019-03. fixed-dose combination approval 검증.
4. [Aerie 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1337553/000133755322000013/aeri-20211231.htm) — SEC / Aerie Pharmaceuticals, 2022-02. 제품매출 $112.1m, 순손실 $74.8m, commercial economics 검증.
5. [Alcon acquisition announcement](https://www.alcon.com/media-release/alcon-acquire-aerie-pharmaceuticals-inc-enhancing-its-ophthalmic-pharmaceutical/) — Alcon, 2022-08-22. $15.25 cash, 37% premium, equity value 약 $770m 검증.
6. [Alcon completes Aerie acquisition](https://www.alcon.com/media-release/alcon-completes-acquisition-aerie-pharmaceuticals-inc/) — Alcon, 2022-11-22. 현금 인수 종결과 terminal payoff 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **미사용** — reliable interim price ledger가 없어 terminal corporate-action payoff만 사용.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Short**다. raw 값은 덮어쓰지 않았다.
