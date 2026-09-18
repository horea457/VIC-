# Astoria Financial Corporation (AF) — 2004-01-09 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Astoria Financial Corporation / AF |
| VIC 게시일 / 작성자 | 2004-01-09 / evan73 |
| 분석 증권 / 실제 방향 | Astoria Financial common equity / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 2004-01 AF common |
| 기대기간 | FY2004 earnings |
| raw horizon audit | LTM EPS $2.59→2004E $3.57; target $43~57 |
| 최종 판정 | **실패 — additive EPS bridge 과대** |

> **결론:** raw Short와 current-company mapping은 모두 틀렸다. 원문은 Astoria Long이지만 2004E EPS $3.57 대비 실제 operating diluted EPS $2.09로 41.5% 미달했고 2005도 $2.26에 그쳤다. refinancing savings를 prepayment·asset-yield 변화와 독립적으로 더한 것이 핵심 오류다.

---

## 1. 회사는 정확히 무엇을 하는가

Astoria Financial은 Long Island·NYC에서 예금과 wholesale funding으로 주택담보대출·multifamily/CRE·MBS를 보유한 thrift였다. earning assets×yield에서 deposits·FHLB·CD funding cost를 뺀 NIM이 핵심이며, mortgage prepayment와 asset/liability repricing 속도가 대손보다 먼저 EPS를 흔들 수 있다.

earning assets × asset yield - interest-bearing liabilities × funding cost - provision - opex - tax = earnings; repricing bucket과 prepayment를 월별로 잇는다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

NIM, asset yield, deposit beta, wholesale funding cost, repricing gaps, prepayment speed, premium amortization, NII, operating EPS, tangible capital

---

## 2. 당시 상황과 시장이 가격에 넣은 것

LTM EPS $2.59, NIM 약 2.40%에서 $7.7bn liabilities의 낮은 금리 refinancing, premium amortization 정상화, loan growth와 buyback이 2004 EPS를 $3.57로 높인다고 봤다.

### Reverse expectations

시장은 저금리 refinancing 이익이 asset yield 하락, mortgage prepayment와 deposit competition으로 상쇄되고 thrift의 convexity가 나빠질 가능성을 가격에 넣었다.

---

## 3. 원문 투자논지 지도

### C1. FHLB refinancing +$0.40 — 부분 성공

**원문 주장**

$5bn refinancing이 EPS $0.40를 더한다.

**경제적 메커니즘**

funding coupon 하락이 NII를 높인다.

**T0 근거**

$5bn maturity opportunity.

**숨은 가정**

asset yield가 유지된다.

**사전 반증조건**

NIM·EPS가 하락하면 과대.

**실제 결과**

EPS는 $2.09로 하락.

**정량 gap**

net +$0.40 미확인.

**분석 오류 또는 제한**

gross saving만 계산.

**재사용 교훈**

asset-side offset을 동시에 넣는다.

### C2. CD refinancing +$0.11 — 부분 성공

**원문 주장**

$2.7bn CDs 재가격으로 EPS $0.11.

**경제적 메커니즘**

deposit cost 하락.

**T0 근거**

high-cost CD book.

**숨은 가정**

deposit mix·balance 유지.

**사전 반증조건**

deposit competition이 saving을 지우면 반증.

**실제 결과**

총 EPS bridge는 실패.

**정량 gap**

+$0.11 분리 검증 불가.

**분석 오류 또는 제한**

funding 항목을 독립시킴.

**재사용 교훈**

deposit beta와 runoff를 모델링한다.

### C3. premium amortization +$0.45 — 실패

**원문 주장**

prepayment 정상화로 EPS $0.45 회복.

**경제적 메커니즘**

premium write-off 감소.

**T0 근거**

refi wave 완화 기대.

**숨은 가정**

mortgage speed가 빠르게 정상화.

**사전 반증조건**

amortization·yield 압박 지속이면 반증.

**실제 결과**

2004 EPS가 출발점보다 낮음.

**정량 gap**

예상 회복 미실현.

**분석 오류 또는 제한**

convexity를 선형화.

**재사용 교훈**

rate scenarios별 CPR과 yield를 잇는다.

### C4. loan growth +$0.32 — 미달

**원문 주장**

loan growth가 EPS $0.32.

**경제적 메커니즘**

earning asset 확대.

**T0 근거**

지역 franchise.

**숨은 가정**

incremental spread가 양수.

**사전 반증조건**

성장해도 NIM 하락이면 반증.

**실제 결과**

$3.57 bridge를 채우지 못함.

**정량 gap**

+$0.32 효과 미실현.

**분석 오류 또는 제한**

volume과 spread 혼동.

**재사용 교훈**

growth는 marginal NIM으로 계산한다.

### C5. buyback +$0.08 — 방향 성공

**원문 주장**

repurchase가 EPS/share를 높인다.

**경제적 메커니즘**

share count 감소.

**T0 근거**

capital availability.

**숨은 가정**

내재가치 이하 매입.

**사전 반증조건**

고가 매입·capital pressure면 반증.

**실제 결과**

2005 6.6m주 repurchase.

**정량 gap**

행동은 실현·총 EPS는 미달.

**분석 오류 또는 제한**

EPS accretion을 영업개선과 혼용.

**재사용 교훈**

share count bridge를 별도 둔다.

### C6. 2004 EPS $3.57·$43~57 — 강한 실패

**원문 주장**

EPS 급증과 rerating.

**경제적 메커니즘**

네 lever 합산×multiple.

**T0 근거**

LTM $2.59.

**숨은 가정**

상쇄가 작다.

**사전 반증조건**

EPS <$2.7이면 반증.

**실제 결과**

operating EPS $2.09.

**정량 gap**

-$1.48/-41.5%.

**분석 오류 또는 제한**

상관·denominator 오류.

**재사용 교훈**

target보다 earnings bridge를 먼저 stress한다.

---

## 4. 당시 Valuation과 Payoff Structure

원문은 refinancing +$0.51, premium amortization +$0.45, loan growth +$0.32, buyback +$0.08을 더해 EPS를 만들고 $43~57 target를 제시했다. 상호의존 변수를 단순 합산한 bridge였다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | asset yield 하락·prepayment 지속 | EPS ~$2 | 현실화 |
| Base | 네 lever 일부 상쇄 | EPS $2.5~3 | 상단 미달 |
| Bull | 모든 lever 합산 | EPS $3.57/$43~57 | 실패 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| LTM EPS | $2.59 | 상승 출발점 | FY2004 $2.09 | 하락 |
| 2004 EPS | $3.57E | $3.57 | $2.09 operating | -41.5% |
| 2005 EPS | 회복 지속 | >$3 | $2.26 | 미달 |
| Liabilities | $7.7bn | refinancing benefit | 부분 상쇄 | 과대 |
| Target | $43~57 | FY2004 rerating | return ledger 없음 | 미검증 |

### 촉매와 시간

판정 horizon은 **FY2004 earnings**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2004-01-09 | VIC Long | raw Short 교정 |
| 2004-H1 | liability refinancing | funding benefit |
| 2004-H2 | asset yield pressure | 상쇄효과 |
| FY2004 | operating EPS $2.09 | 핵심 실패 |
| FY2005 | EPS $2.26 | 회복 미달 |
| 2005 | 6.6m shares repurchased | buyback claim 성공 |
| 2006-07 | 추가 authorization | capital return 지속 |
| 2017 | Sterling merger | 원 horizon 밖 |

### 실제 사업·자본구조 추이

2004 operating diluted EPS는 $2.09, 2005 diluted EPS는 $2.26이었다. repurchase는 진행됐지만 NIM·asset yield와 mortgage dynamics가 refinancing benefit을 흡수했다. 2017 Sterling merger는 원 horizon과 13년 떨어진 별도 사건이다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

performance row가 없어 exact return이나 target hit를 만들지 않는다. 2004 earnings denominator와 공시 결과로 판정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | FHLB refinancing +$0.40 | 20% | 부분 성공 | net +$0.40 미확인. |
| C2 | CD refinancing +$0.11 | 18% | 부분 성공 | +$0.11 분리 검증 불가. |
| C3 | premium amortization +$0.45 | 18% | 실패 | 예상 회복 미실현. |
| C4 | loan growth +$0.32 | 16% | 미달 | +$0.32 효과 미실현. |
| C5 | buyback +$0.08 | 16% | 방향 성공 | 행동은 실현·총 EPS는 미달. |
| C6 | 2004 EPS $3.57·$43~57 | 12% | 강한 실패 | -$1.48/-41.5%. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

earnings miss는 funding cost 한 항목이 아니라 asset yield·prepayment·deposit beta가 같은 방향으로 움직이지 않은 데서 왔다.

### Counterfactual

refinancing 절감액을 절반만 반영하고 asset yield -25bp·prepayment stress를 넣어도 $3.57 EPS가 가능한가?

---

## 9. 분석 오류 유형과 최초 경고

서로 상관된 네 EPS lever를 선형 합산하고 balance-sheet repricing을 총액이 아닌 속도 문제로 보지 않았다.

### 최초로 관찰 가능했던 경고신호

FY2004 operating EPS $2.09가 예상 $3.57에 크게 미달한 시점이 명확한 first break였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

thrift는 liability saving보다 asset/liability repricing gap을 먼저 모델링한다.

### Lesson 2

premium amortization·loan growth·buyback을 독립 EPS 항목처럼 단순 합산하지 않는다.

### Lesson 3

Street EPS 차이는 NIM bridge로 설명한다.

### Lesson 4

M&A optionality는 원 horizon earnings thesis와 분리한다.

### 지금 같은 아이디어를 다시 본다면

- asset repricing buckets
- deposit beta
- wholesale funding
- prepayment speed
- premium amortization
- NIM/NII
- operating EPS

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | franchise 생존 |
| Valuation thesis | denominator 실패 |
| Catalyst thesis | refi 일부 |
| Security payoff | common 방향 교정 |
| Timing / path | FY2004 실패 |
| Thesis score | 3.8/10 |
| Process score | 5.5/10 |
| 종합 | **실패 — additive EPS bridge 과대** |

### 한 문장 교훈

> thrift는 liability saving보다 asset/liability repricing gap을 먼저 모델링한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2004-01-09. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL은 source SQL에서 null이다.
2. [Astoria 2005 results](https://www.sec.gov/Archives/edgar/data/910322/000127528706001133/af4938ex991.htm) — SEC / Astoria Financial, 2006-01. 2004 operating EPS $2.09, 2005 diluted EPS $2.26와 repurchase 검증.
3. [Astoria FY2007 results](https://www.sec.gov/Archives/edgar/data/910322/000114420408003676/v100570_ex99-1.htm) — SEC / Astoria Financial, 2008-01-24. 2007 operating EPS $1.50, GAAP $1.36, NIM과 NII 감소 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported operating data만 사용; exact transaction ledger가 없으면 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
