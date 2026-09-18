# Affinity Media Inc. (AFMI.OB) — 2008-06-04 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Affinity Media Inc. / AFMI.OB |
| VIC 게시일 / 작성자 | 2008-06-04 / scrooge833 |
| 분석 증권 / 실제 방향 | SPAC IPO common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 $5.85 |
| 기대기간 | 2008 deal vote 또는 liquidation |
| raw horizon audit | Hotels at Home merger 성공 시 effective basis 약 $3.84, 2009 target $7.60; 실패 시 trust $6+ |
| 최종 판정 | **downside thesis 성공 — deal 실패에도 $6 cash + residual** |

> **결론:** Hotels at Home business-combination thesis는 vote 실패로 무너졌다. 그러나 $5.85 common은 liquidation에서 IPO share당 $6 cash와 취소된 7주당 residual common 1주를 받았다. 따라서 operating deal claim은 실패했지만 핵심 trust-floor 비대칭은 작동했다. residual의 최종 현금가치가 완전하지 않아 exact total return·IRR은 계산하지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

Affinity Media는 IPO proceeds를 trust에 보관한 blank-check company였다. merger 승인 전 common의 가치는 trust cash와 redemption/liquidation rights, deal 성공 시 교부될 operating-company equity, sponsor dilution과 청산 뒤 residual shell 가치의 합이다.

trust cash + merger equity value - sponsor/promote dilution - transaction cost + liquidation residual = common payoff; vote·redemption·liquidation date를 실제 ledger로 잇는다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

trust cash/share, redemption terms, vote threshold, sponsor promote, merger exchange ratio, liquidation deadline, residual shares, cash settlement

---

## 2. 당시 상황과 시장이 가격에 넣은 것

$5.85에 SPAC common을 사면 merger 성사 시 Hotels at Home equity를 약 $3.84 effective basis로 얻고 2009년 $7.60을 기대하며, 부결 시 trust cash $6 이상으로 원금이 방어된다는 event-driven thesis였다.

### Reverse expectations

시장은 transaction dilution, Hotels at Home valuation·execution, 낮은 vote certainty와 청산비용 때문에 trust보다 낮은 가격을 붙였다. 핵심은 deal 성공확률보다 실제 redemption 문서가 $5.85 downside를 지키는지였다.

---

## 3. 원문 투자논지 지도

### C1. Hotels at Home merger — 실패

**원문 주장**

vote 뒤 Hotels at Home과 결합한다.

**경제적 메커니즘**

승인·closing이 operating equity를 만든다.

**T0 근거**

signed transaction과 예정 vote.

**숨은 가정**

주주 승인과 financing 충족.

**사전 반증조건**

vote 부결이면 즉시 실패.

**실제 결과**

vote가 실패했다.

**정량 gap**

closing 0%.

**분석 오류 또는 제한**

deal probability를 과신.

**재사용 교훈**

event claim과 trust claim을 분리한다.

### C2. effective basis $3.84 — 미실현

**원문 주장**

merger equity를 $3.84 basis로 취득한다.

**경제적 메커니즘**

trust cash와 exchange ratio가 implied basis를 낮춘다.

**T0 근거**

원문 pro forma 계산.

**숨은 가정**

거래가 동일 조건으로 닫힌다.

**사전 반증조건**

deal break면 계산 무효.

**실제 결과**

거래가 닫히지 않았다.

**정량 gap**

$3.84 basis 적용 불가.

**분석 오류 또는 제한**

conditional valuation을 확정값처럼 봄.

**재사용 교훈**

closing 조건부 수치는 확률가중한다.

### C3. 2009 target $7.60 — 실패

**원문 주장**

운영개선 뒤 $7.60.

**경제적 메커니즘**

merger EBITDA와 multiple이 equity를 높인다.

**T0 근거**

원문 operating case.

**숨은 가정**

closing 뒤 plan 달성.

**사전 반증조건**

deal failure 또는 target miss.

**실제 결과**

underlying equity를 받지 못했다.

**정량 gap**

$7.60 미실현.

**분석 오류 또는 제한**

business와 security event 혼합.

**재사용 교훈**

target는 security tree 각 branch에 둔다.

### C4. trust floor $6+ — 성공

**원문 주장**

부결 시 $6 이상을 회수한다.

**경제적 메커니즘**

IPO cash가 trust에 보관된다.

**T0 근거**

trust/redemption terms.

**숨은 가정**

비용·tax leakage가 제한적.

**사전 반증조건**

$5.85 미만 지급이면 반증.

**실제 결과**

$6 cash가 지급됐다.

**정량 gap**

$0.15/+2.6% cash spread.

**분석 오류 또는 제한**

settlement time 비용 미포함.

**재사용 교훈**

floor는 날짜·비용 포함 IRR로 본다.

### C5. residual upside — 부분 성공

**원문 주장**

청산 뒤 residual shell도 가치가 있다.

**경제적 메커니즘**

취소 주식 7주당 residual 1주.

**T0 근거**

liquidation filing.

**숨은 가정**

residual assets·listing이 가치 보존.

**사전 반증조건**

residual이 무가치면 upside 0.

**실제 결과**

1/7주 교부는 확인, 최종 가치 미복원.

**정량 gap**

수량 확인·가치 미확정.

**분석 오류 또는 제한**

nominal security를 현금으로 간주.

**재사용 교훈**

residual은 실현 ledger가 있을 때만 수익에 넣는다.

### C6. asymmetric downside — 성공

**원문 주장**

$5.85에서 손실은 제한되고 upside가 크다.

**경제적 메커니즘**

trust branch가 downside를 지킨다.

**T0 근거**

entry below trust.

**숨은 가정**

fraud·비용·지연이 없음.

**사전 반증조건**

cash recovery <entry면 실패.

**실제 결과**

cash만 $6.

**정량 gap**

cash spread +2.6%.

**분석 오류 또는 제한**

opportunity cost를 작게 봄.

**재사용 교훈**

event time과 annualized floor yield를 같이 본다.

---

## 4. 당시 Valuation과 Payoff Structure

binary tree로 계산한다. 성공가치는 merger exchange 뒤 fully diluted shares로, 실패가치는 trust 현금·비용·tax·residual rights로 계산한다. $7.60 target와 $6 floor를 한 기대값으로 섞지 않는다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | deal 실패·trust leakage | $5.5 이하 | 미실현 |
| Base | deal 실패·$6 cash | 원금+소폭 | 실현 |
| Bull | deal close·2009 execution | $7.60 | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $5.85 | $6 floor / $7.60 bull | $6 cash+1/7 residual | floor 성공 |
| Deal vote | 승인 가능 | 통과 | 실패 | operating claim 실패 |
| Effective merger basis | $3.84 | Hotels at Home ownership | 거래 미종결 | 미실현 |
| Cash floor | $6+ | >entry | $6 | +$0.15/+2.6% |
| Residual | 추가 upside | 양의 가치 | 1/7 share | 가치 ledger 불완전 |

### 촉매와 시간

판정 horizon은 **2008 deal vote 또는 liquidation**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2008-06-04 | VIC Long | $5.85 event entry |
| 2008-06-10 | proxy supplement | vote mechanics |
| 2008-06-13 | deal vote 실패 | operating thesis break |
| 2008-07 | 청산 준비 | trust payoff 중심 |
| 2008-09 | deadline 경과 | business combination 종료 |
| 2008-10-10 | liquidation terms 공시 | $6+residual |
| 2008-10 | IPO shares 취소 | cash conversion |
| 2026-09-18 | research cutoff | residual exact value 미복원 |

### 실제 사업·자본구조 추이

deal vote가 실패했고 proposed merger는 닫히지 않았다. 2008-10 공시는 IPO common each를 $6 cash와 residual common 1/7주로 전환했다. operating upside는 사라졌지만 $5.85 entry 대비 cash만으로도 nominal downside를 막았다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

$6 cash / $5.85 = 1.0256x, 즉 cash component만 약 +2.6%다. residual 1/7 share의 후속 현금화와 정확 settlement·tax가 빠졌으므로 이는 total return이나 IRR이 아니다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | Hotels at Home merger | 20% | 실패 | closing 0%. |
| C2 | effective basis $3.84 | 18% | 미실현 | $3.84 basis 적용 불가. |
| C3 | 2009 target $7.60 | 18% | 실패 | $7.60 미실현. |
| C4 | trust floor $6+ | 16% | 성공 | $0.15/+2.6% cash spread. |
| C5 | residual upside | 16% | 부분 성공 | 수량 확인·가치 미확정. |
| C6 | asymmetric downside | 12% | 성공 | cash spread +2.6%. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익의 원천은 Hotels at Home execution이 아니라 trust 계약이었다. vote 실패가 business thesis를 제거했지만 liquidation waterfall이 common을 보호했다.

### Counterfactual

trust cash가 $5.50으로 줄거나 liquidation이 18개월 지연되어도 $5.85 entry의 expected value가 충분했는가?

---

## 9. 분석 오류 유형과 최초 경고

merger 성공 뒤 $7.60을 자세히 모델링한 반면 vote mechanics, trust leakage와 residual share liquidation의 기간을 상대적으로 덜 정량화했다.

### 최초로 관찰 가능했던 경고신호

2008-06 deal vote 실패가 operating thesis의 즉시 break였지만 동시에 trust-floor thesis를 실제 payoff 단계로 전환한 신호였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

SPAC common은 deal quality와 trust-floor payoff를 별도 claim으로 쪼갠다.

### Lesson 2

trust cash는 vote·redemption·deadline·tax와 expenses 뒤 주당액으로 계산한다.

### Lesson 3

실패한 merger라도 downside thesis는 성공할 수 있다.

### Lesson 4

residual share 가치가 없으면 exact total return을 만들지 않는다.

### 지금 같은 아이디어를 다시 본다면

- trust cash/share
- vote·redemption
- deal exchange ratio
- sponsor dilution
- deadline
- liquidation ledger

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | deal thesis 실패 |
| Valuation thesis | trust discount 성공 |
| Catalyst thesis | vote 실패·liquidation |
| Security payoff | SPAC common 적절 |
| Timing / path | 짧은 event 성공 |
| Thesis score | 7.5/10 |
| Process score | 8.5/10 |
| 종합 | **downside thesis 성공 — deal 실패에도 $6 cash + residual** |

### 한 문장 교훈

> SPAC common은 deal quality와 trust-floor payoff를 별도 claim으로 쪼갠다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/Affinity_Media/8205028420) — Value Investors Club / source SQL, 2008-06-04. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Affinity proxy supplement before vote](https://www.sec.gov/Archives/edgar/data/1343305/000114420408034845/v116747_defa14a.htm) — SEC / Affinity Media, 2008-06-10. Hotels at Home vote와 trust/redemption context 검증.
3. [Affinity liquidation distribution](https://www.sec.gov/Archives/edgar/data/1343305/000114420408057586/v128968_defa14a.htm) — SEC / Affinity Media, 2008-10-10. IPO common당 $6 cash와 7주당 residual common 1주의 최종 구조 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·corporate-action payoff만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
