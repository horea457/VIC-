# Astoria Financial Corporation (AF) — 2006-09-18 VIC Short

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Astoria Financial Corporation / AF |
| VIC 게시일 / 작성자 | 2006-09-18 / skyhawk887 |
| 분석 증권 / 실제 방향 | Astoria Financial common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 2006-09 AF short |
| 기대기간 | FY2007 |
| raw horizon audit | Street 2007 EPS ~$1.94 vs own ~$1.35; target 2005 low ~$24.43 |
| 최종 판정 | **성공 — NIM·NII·EPS 압박 적중** |

> **결론:** 회사 mapping만 교정하면 raw Short는 맞다. 2007 operating EPS $1.50은 자체 $1.35보다 11.1% 높았지만 Street $1.94보다 22.7% 낮았고, NIM은 1.87%에서 1.62%, NII는 $390.4m에서 $333.5m로 감소했다. short의 핵심 spread mechanism이 실현됐다.

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

inverted curve에서 wholesale·deposit liabilities가 asset보다 빠르게 재가격되며 Street 2007 EPS 약 $1.94가 과대이고 자체 추정 $1.35가 현실적이라는 논지였다.

### Reverse expectations

시장은 curve 정상화, deposit repricing relief와 asset growth가 spread를 회복시키거나 낮은 valuation이 downside를 제한할 가능성을 반영했다.

---

## 3. 원문 투자논지 지도

### C1. Street EPS ~$1.94 과대 — 성공

**원문 주장**

2007 consensus가 높다.

**경제적 메커니즘**

NIM compression이 earnings를 낮춘다.

**T0 근거**

repricing mismatch.

**숨은 가정**

curve inversion 지속.

**사전 반증조건**

EPS가 $1.85 이상이면 반증.

**실제 결과**

operating EPS $1.50.

**정량 gap**

Street 대비 -22.7%.

**분석 오류 또는 제한**

none material.

**재사용 교훈**

consensus gap을 NIM bridge로 설명한다.

### C2. own EPS ~$1.35 — 근접

**원문 주장**

2007 EPS가 약 $1.35.

**경제적 메커니즘**

spread 압박의 bottom-up estimate.

**T0 근거**

funding mix.

**숨은 가정**

credit·opex 안정.

**사전 반증조건**

$1.70 이상이면 과도한 bearish.

**실제 결과**

operating $1.50, GAAP $1.36.

**정량 gap**

operating +11.1%; GAAP 근접.

**분석 오류 또는 제한**

EPS 정의 혼용 위험.

**재사용 교훈**

operating/GAAP를 사전 고정한다.

### C3. NIM compression — 강한 성공

**원문 주장**

NIM이 의미 있게 하락.

**경제적 메커니즘**

liabilities가 assets보다 빨리 재가격.

**T0 근거**

inverted curve.

**숨은 가정**

deposit beta가 높다.

**사전 반증조건**

NIM 안정/상승이면 반증.

**실제 결과**

1.87%→1.62%.

**정량 gap**

-25bp/-13.4%.

**분석 오류 또는 제한**

none material.

**재사용 교훈**

repricing table이 short의 중심이다.

### C4. NII decline — 강한 성공

**원문 주장**

balance growth로도 NII 감소를 못 막는다.

**경제적 메커니즘**

spread loss가 volume을 압도.

**T0 근거**

low NIM.

**숨은 가정**

asset growth 제한.

**사전 반증조건**

NII 증가면 반증.

**실제 결과**

$390.4m→$333.5m.

**정량 gap**

-$56.9m/-14.6%.

**분석 오류 또는 제한**

none material.

**재사용 교훈**

NIM과 dollars NII를 함께 본다.

### C5. 2005 low retest — 미검증

**원문 주장**

주가가 약 $24.43으로 하락.

**경제적 메커니즘**

earnings revision과 de-rating.

**T0 근거**

historical support.

**숨은 가정**

multiple이 유지된다.

**사전 반증조건**

earnings miss에도 price 견조면 실패.

**실제 결과**

verified price ledger 없음.

**정량 gap**

정확한 hit 불명.

**분석 오류 또는 제한**

fundamental과 price claim 혼용.

**재사용 교훈**

가격은 별도 source로 검증한다.

### C6. short payoff — fundamental 성공

**원문 주장**

common short가 수익을 낸다.

**경제적 메커니즘**

EPS miss가 price에 반영.

**T0 근거**

Street gap.

**숨은 가정**

borrow·dividend·timing 감당.

**사전 반증조건**

borrow recall/price rally면 손실.

**실제 결과**

business mechanism 적중.

**정량 gap**

exact net return 없음.

**분석 오류 또는 제한**

implementation cost 누락.

**재사용 교훈**

short는 borrow와 cover rule까지 기록한다.

---

## 4. 당시 Valuation과 Payoff Structure

earnings miss와 2005 저점 약 $24.43 재방문을 연결했다. short valuation은 price target보다 NIM·NII·EPS의 동시 하향으로 검증하는 편이 안전하다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for short | curve 정상화·deposit relief | EPS ~$1.94 | 미발생 |
| Base | NIM 압박 | EPS ~$1.50 | 실현 |
| Bull for short | severe compression | EPS ~$1.35/$24.43 | EPS 근접 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Operating EPS | Street ~$1.94 | own ~$1.35 | $1.50 | short 성공 |
| GAAP EPS | Street ~$1.94 | 하향 | $1.36 | 강한 miss |
| NIM | 1.87% prior | 압축 | 1.62% | -25bp |
| NII | $390.4m prior | 감소 | $333.5m | -14.6% |
| Price target | ~$24.43 | 2005 low retest | ledger 없음 | 미검증 |

### 촉매와 시간

판정 horizon은 **FY2007**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2006-09-18 | VIC Short | funding spread thesis |
| 2006-H2 | curve inversion 지속 | liability pressure |
| 2007-Q1 | NIM 하락 | 초기 확인 |
| 2007-Q2 | NIM·NII 동반감소 | first signal |
| 2007-H2 | earnings revisions | Street gap 축소 |
| FY2007 | operating EPS $1.50 | short 성공 |
| FY2007 | GAAP EPS $1.36 | own estimate 근접 |
| 2008-01-24 | 연간결과 공시 | 검증 완료 |

### 실제 사업·자본구조 추이

FY2007 NIM 1.62% 대 1.87%, NII $333.5m 대 $390.4m, operating EPS $1.50, GAAP EPS $1.36이었다. own EPS는 다소 보수적이었지만 Street miss 방향과 메커니즘은 맞았다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

검증된 entry·borrow·cover ledger가 없어 exact short return은 보류한다. fundamental short outcome은 2007 공시수치로 판정한다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | Street EPS ~$1.94 과대 | 20% | 성공 | Street 대비 -22.7%. |
| C2 | own EPS ~$1.35 | 18% | 근접 | operating +11.1%; GAAP 근접. |
| C3 | NIM compression | 18% | 강한 성공 | -25bp/-13.4%. |
| C4 | NII decline | 16% | 강한 성공 | -$56.9m/-14.6%. |
| C5 | 2005 low retest | 16% | 미검증 | 정확한 hit 불명. |
| C6 | short payoff | 12% | fundamental 성공 | exact net return 없음. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

asset/liability duration mismatch가 funding cost를 더 빨리 올려 NIM과 NII를 눌렀고 Street denominator가 하향됐다.

### Counterfactual

curve가 6개월 안에 정상화되고 deposits가 즉시 낮은 금리로 재가격돼도 EPS $1.94가 가능한가?

---

## 9. 분석 오류 유형과 최초 경고

방향은 맞았으나 $1.35 EPS와 특정 price target를 정밀값처럼 둔 점, short squeeze·borrow·dividend cost를 덜 모델링했다.

### 최초로 관찰 가능했던 경고신호

2007 중간결과에서 NIM과 NII가 동시에 전년 대비 하락한 것이 조기 확인 신호였다.

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
| Business thesis | spread 압박 |
| Valuation thesis | earnings miss 성공 |
| Catalyst thesis | curve catalyst 성공 |
| Security payoff | short costs 미복원 |
| Timing / path | FY2007 성공 |
| Thesis score | 8.2/10 |
| Process score | 8.5/10 |
| 종합 | **성공 — NIM·NII·EPS 압박 적중** |

### 한 문장 교훈

> thrift는 liability saving보다 asset/liability repricing gap을 먼저 모델링한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2006-09-18. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL은 source SQL에서 null이다.
2. [Astoria 2005 results](https://www.sec.gov/Archives/edgar/data/910322/000127528706001133/af4938ex991.htm) — SEC / Astoria Financial, 2006-01. 2004 operating EPS $2.09, 2005 diluted EPS $2.26와 repurchase 검증.
3. [Astoria FY2007 results](https://www.sec.gov/Archives/edgar/data/910322/000114420408003676/v100570_ex99-1.htm) — SEC / Astoria Financial, 2008-01-24. 2007 operating EPS $1.50, GAAP $1.36, NIM과 NII 감소 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — verified corporate action·reported operating data만 사용; exact transaction ledger가 없으면 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Short**다. raw 값은 덮어쓰지 않았다.
