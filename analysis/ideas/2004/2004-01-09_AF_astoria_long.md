# Astoria Financial (AF) — 2004-01-09 VIC Long

> **Idea unit:** 2004-01-09 Astoria Financial common equity Long.
> **Research as-of:** 2026-09-18. SQL companies table은 AF를 AlarmForce로 덮어썼지만 원문은 **Astoria Financial**이다. raw Short도 오류이며 실제 방향은 Long이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 당시 Ticker | Astoria Financial / AF |
| VIC 게시일 / 작성자 | 2004-01-09 / evan73 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 LTM EPS | $2.59 |
| 원문 2004E EPS / NIM | **$3.57 / 2.40%** |
| valuation target | **$43~57**, 중심 high-$40s/low-$50s |
| 실제 2004 operating diluted EPS | **$2.09** |
| 실제 2005 diluted EPS | **$2.26** |
| 장기 corporate action | 2017 Sterling merger, announced value 약 $21.92/share |
| 최종 판정 | **핵심 earnings bridge 실패 — M&A optionality는 13년 뒤 실현** |

> **결론:** 원문은 $7.7bn liability refinancing, premium amortization 정상화, loan growth, buyback이 겹치며 EPS가 $2.59에서 $3.57로 50% 넘게 뛸 것으로 봤다. 실제 2004 operating EPS는 $2.09, 2005 diluted EPS도 $2.26에 그쳐 핵심 earnings bridge가 성립하지 않았다. Astoria의 deposit franchise와 credit quality는 실제였지만 **asset repricing보다 funding cost·mortgage prepayment dynamics가 더 복잡했다.**

---

## 1. 회사는 정확히 무엇을 하는가

Astoria는 Long Island·NYC 지역의 대형 thrift였다. 주된 자산은 1~4 family mortgage, multifamily/CRE, MBS였고 자금조달은 deposits, CDs, FHLB borrowings였다.

핵심 수익식은:

`NIM × earning assets - credit costs - operating expenses = pretax earnings`

2004 아이디어는 credit가 아니라 **duration mismatch와 liability repricing**을 사는 구조였다.

---

## 2. 당시 상황과 시장이 가격에 넣은 것

2003 저금리 환경에서 mortgage refinancing이 폭증하면서 premium MBS/loan prepayment, premium amortization 급증, lower-yield asset 재투자, NIM 압박이 동시에 발생했다.

원문은 rates가 안정되거나 오르면 prepayment가 줄고, 고금리 CDs/FHLB borrowings가 낮은 금리로 refinance되며, balance-sheet growth가 재개될 것으로 봤다.

---

## 3. 원문 투자논지 지도

### C1. $5bn FHLB refinancing이 EPS +$0.40 / NIM +22bp — **과대**
refinancing 자체는 우호적이었지만 전체 NIM·EPS는 예상만큼 회복하지 않았다.

### C2. $2.7bn CD refinancing이 EPS +$0.11 — **부분 성공**
liability cost는 낮아졌지만 asset yield와 prepayment가 동시에 움직였다.

### C3. premium amortization 정상화가 EPS +$0.45 — **과대**
mortgage thrift의 convexity를 너무 선형적으로 모델링했다.

### C4. loan growth가 EPS +$0.32 — **미달**
portfolio growth가 있어도 $3.57 EPS bridge를 채우지 못했다.

### C5. buyback — **성공 방향**
2005에 6.6m주를 repurchase했고 2006 새 authorization을 열었다.

### C6. M&A takeout $44~54 — **horizon 실패**
Astoria는 2017 Sterling과 합병했지만 announced value는 약 $21.92/share였다.

---

## 4. Valuation과 실제 숫자

| 지표 | 원문 | 실제 |
|---|---:|---:|
| 2004 EPS | **$3.57** | operating diluted **$2.09** |
| 2005 EPS | — | **$2.26** |
| target | $43~57 | denominator 미달 |
| M&A | near-term optionality | 2017 |

원문의 핵심 오류는 multiple보다 **$3.57 earnings denominator**였다.

---

## 5. 실제 경로

| 시점 | 사건 | 의미 |
|---|---|---|
| 2004-01 | VIC Long | refinancing/NIM thesis |
| FY2004 | operating EPS $2.09 | forecast 크게 미달 |
| FY2005 | EPS $2.26 | 50% growth thesis 미실현 |
| 2005~06 | buybacks 지속 | capital return 적중 |
| 2006~07 | curve/NIM 압박 | duration risk 재확인 |
| 2017 | Sterling merger | M&A optionality 매우 후행 |

---

## 6. 투자결과 해석

SQL performance row가 없어 exact return은 만들지 않는다. 이 아이디어는 **예상 EPS가 실제 earning power였는가**로 검증하는 편이 더 정확하며, 그 기준에서는 실패다.

---

## 7. Claim별 판정

| Claim | Weight | 판정 |
|---|---:|---|
| liability refinancing | 20% | 부분 성공 |
| premium amortization normalization | 20% | 과대 |
| loan growth | 15% | 미달 |
| buyback | 15% | 성공 |
| 2004 EPS $3.57 | 20% | 실패 |
| near-term M&A | 10% | 실패 |

---

## 8. 무엇이 실제 손익을 만들었는가

funding-rate 하락만 보는 것으로는 부족했다. **asset yield, prepayment, deposit beta, curve shape**가 동시에 움직였다.

---

## 9. 분석 오류와 최초 경고

2004 actual EPS가 $3.57 bridge와 크게 벌어진 순간이 최초 falsifier였다.

---

## 10. 재사용 가능한 교훈

1. bank/thrift EPS bridge는 각 항목을 독립적으로 더하지 않는다.
2. mortgage book은 prepayment convexity와 funding beta를 같이 본다.
3. buyback은 earnings miss를 완전히 상쇄하지 못한다.
4. M&A optionality는 base valuation과 분리한다.
5. target multiple보다 target earnings의 질을 먼저 검증한다.

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business understanding | 좋음 |
| Earnings forecast | 실패 |
| Valuation thesis | 실패 |
| Capital allocation | 성공 |
| M&A catalyst | 매우 지연 |
| Thesis score | 4.8/10 |
| Process score | 9.5/10 |
| 종합 | **실패 — refinancing savings를 EPS로 과도하게 선형 전환** |

### 한 문장 교훈

> thrift에서는 “부채금리 하락”이 곧 EPS 상승이 아니다; **asset repricing과 prepayment convexity가 같은 순간에 반대로 움직일 수 있다.**

---

## 12. Sources / Validation Notes

1. VIC original / uploaded `VIC_IDEAS(5).sql`, 2004-01-09.
2. Astoria 2005 results / SEC exhibit — 2004 operating EPS $2.09, 2005 EPS $2.26, repurchases.
3. Sterling/Astoria merger filing — 2017 announced value approximately $21.92/share.
4. https://www.sec.gov/Archives/edgar/data/910322/000127528706001133/af4938ex991.htm
5. https://www.sec.gov/Archives/edgar/data/1070154/000157104917002052/t1700647_ex99-2.htm

### 데이터 품질

- T0 thesis: **A**
- operating/M&A outcome: **A**
- exact realized return: **미확정**
