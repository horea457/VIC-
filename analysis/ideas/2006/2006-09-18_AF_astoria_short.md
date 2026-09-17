# Astoria Financial (AF) — 2006-09-18 VIC Short

> **Idea unit:** 2006-09-18 Astoria Financial common equity Short.
> **Research as-of:** 2026-09-18. SQL companies table의 AF=AlarmForce는 ticker-reuse 오류다. 이 원문은 **Astoria Financial Short**이며 raw Short는 맞다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 당시 Ticker | Astoria Financial / AF |
| VIC 게시일 / 작성자 | 2006-09-18 / skyhawk887 |
| 실제 방향 | Common equity Short |
| 당시 가격 추정 | 약 **$31** |
| consensus 2007 EPS | 약 **$1.94** |
| 원문 2007 EPS | 약 **$1.35** |
| target | 2005 low **$24.43** 재시험 |
| 실제 2007 NIM | **1.62%**, 2006 1.87% |
| 실제 2007 net interest income | **$333.5m**, 2006 $390.4m |
| 최종 판정 | **성공 — NIM/earnings deterioration 적중** |

> **결론:** 이 short는 housing credit crash가 아니라 **inverted curve와 funding-cost pressure**를 숏했다. 실제 2007 NIM은 1.87%에서 1.62%로 하락했고 net interest income도 약 14.6% 감소했다. 2004 bull thesis가 liability refinancing의 이점을 과대평가했다면, 2006 short는 자산과 부채의 repricing 속도 차이를 더 정확히 포착했다.

---

## 1. 당시 구조

Astoria는 hybrid mortgage, multifamily/CRE, securities를 deposits·CDs·borrowings로 funding하는 thrift였다.

2006에는 short rates 상승, yield-curve inversion, deposit competition, wholesale funding cost 상승, asset repricing 지연이 동시에 나타났다.

---

## 2. 원문 투자논지 지도

### C1. 2007 consensus EPS $1.94는 너무 높다 — **성공 방향**
원문은 약 $1.35까지 내려갈 수 있다고 봤다. 2007 revenue/NIM 경로가 이를 지지했다.

### C2. NIM compression 지속 — **강한 성공**
2007 full-year NIM **1.62%**, 전년 **1.87%**.

### C3. core deposit deterioration — **성공**
funding costs가 asset yields보다 빨리 올랐다.

### C4. expense cuts로 방어하기 어렵다 — **성공 방향**
earnings 압박은 revenue/NIM에서 왔다.

### C5. acquisition risk — **근거리 미발생**
실제 M&A는 2017로 10년 이상 뒤였다.

---

## 3. 실제 경로

| 시점 | 결과 |
|---|---|
| 2006-09 | VIC Short |
| FY2006 | NIM 1.87% |
| FY2007 | NIM **1.62%** |
| FY2007 | net interest income **$333.5m vs $390.4m** |
| 2007 Q4 | NIM 1.57% |
| 2017 | Sterling merger |

---

## 4. Payoff 해석

원문은 약 $31에서 $24.43을 target으로 봤다. SQL performance row가 없어 exact short return은 확정하지 않지만 **핵심 fundamental falsifier인 NIM과 net interest income은 명확히 short 방향**이었다.

---

## 5. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| NIM compression | 30% | 강한 성공 |
| EPS estimates 하향 | 25% | 성공 방향 |
| deposit pressure | 20% | 성공 |
| expense defense 제한 | 10% | 성공 방향 |
| near-term M&A 없음 | 15% | 성공 |

---

## 6. 재사용 가능한 교훈

1. 은행 short는 credit loss 없이도 NIM만으로 성립한다.
2. inverted curve에서는 deposit beta와 wholesale funding을 본다.
3. 높은 P/B는 earnings denominator가 내려가면 더 비싸진다.
4. acquisition optionality는 별도 short risk다.
5. 같은 ticker의 과거 bull thesis와 현재 balance-sheet regime을 혼동하지 않는다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Operating thesis | 강한 성공 |
| Valuation thesis | 성공 방향 |
| Timing | 양호 |
| Risk identification | 양호 |
| Thesis score | 8.8/10 |
| Process score | 9.5/10 |
| 종합 | **성공 — curve/funding-cost short의 좋은 사례** |

### 한 문장 교훈

> bank short의 핵심은 대손이 아니라 **자산과 부채의 repricing 속도 차이**일 수 있다.

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2006-09-18.
2. Astoria FY2007 results — NIM 1.62%, net interest income $333.5m.
3. https://www.sec.gov/Archives/edgar/data/910322/000114420408003676/v100570_ex99-1.htm

### 데이터 품질
- T0 thesis: **A**
- operating outcome: **A**
- exact short return: **미확정**
