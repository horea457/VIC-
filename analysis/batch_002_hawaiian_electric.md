# Batch 002 — Hawaiian Electric Industries (HEI) 완전 재분석 v2

대상 VIC 아이디어: 2008-12-03 Short / 2010-05-09 Short / 2020-06-05 Long

> 원칙: 회사·산업·돈의 흐름은 한 번 충분히 설명하고, 각 아이디어는 당시 시장가격에 들어 있던 기대, 실제 현금흐름, 촉매, 가격경로와 투자결과를 별도로 판정한다.

## 0. 결론

| 아이디어 | 방향 | 기존 DB 가격결과 | 사업논지 | 투자판정 |
|---|---|---|---|---|
| 2008-12-03 | Short | 3개월 약 +43.5%, 1년 +12.2% | 경기·은행·유틸리티 현금흐름 취약성 적중, 배당삭감/SOTP 과도 | 단기 성공, 장기 thesis 과장 |
| 2010-05-09 | Short | 1년 -13.1%, 3년 -33.6%, 5년 -61.8% | 과거 문제를 미래에 직선 외삽 | 실패 |
| 2020-06-05 | Long | 1년 +10.8%, 2년 +15.0%, 2024-01 기준 약 -65% | 정상상태 utility+bank 논리는 상당부분 진행, catastrophe liability 누락 | 최종 실패 |

SQL의 세 건은 모두 Short로 저장돼 있으나 2020년 글은 $38.90 보통주 Long이다. raw flag는 보존하고 curated direction만 교정한다.

## 1. HEI는 무슨 기업인가

HEI는 단일 전력회사가 아니라 **규제 전력유틸리티 Hawaiian Electric + 지역은행 American Savings Bank(ASB)**를 지주회사 아래 둔 구조였다. 두 자회사의 이익 원천과 tail risk가 전혀 다르므로 단순 consolidated P/E로 보면 안 된다.

### 전력 유틸리티

Oahu·Maui·Hawaii Island 등 고립된 섬 전력망에서 발전·송전·배전을 한다. 전력망이 미국 본토와 연결되지 않아 섬별 예비력과 발전설비가 필요하다. 유틸리티는 설비에 자본을 넣고 규제기관이 인정한 rate base에 허용수익률을 적용해 요금으로 회수한다. 따라서 `capex → rate base → 허용매출 → 현금회수` 사이의 규제시차가 중요하다.

**Rate base**는 규제기관이 고객요금으로 수익을 벌어도 된다고 인정한 투자자본이다. **Allowed ROE**는 그 자본 중 자기자본 부분에 허용된 수익률이다. 실제 ROE가 낮다고 곧바로 나쁜 기업인 것은 아니다. 다음 rate case와 decoupling 같은 제도변화로 회수구조가 바뀔 수 있기 때문이다.

### American Savings Bank

ASB는 Hawaii 예금을 받아 주택담보·HELOC·상업용부동산·소비자/기업대출에 투자한다. `대출수익률 - 예금/조달비용 = NIM`에서 운영비와 신용손실을 빼면 이익이 남는다. 따라서 부동산가격, LTV, 연체율, 충당금, 예금비용과 규제자본을 함께 봐야 한다.

### 지주회사 돈의 흐름

HEI 보통주 배당과 지주회사 이자는 자회사에서 올라오는 현금에 의존한다. 유틸리티가 대규모 capex 때문에 현금을 보유해야 하거나 ASB가 신용손실 때문에 자본을 쌓아야 하면 회계상 이익이 있어도 지주회사 배당가능현금은 줄 수 있다.

따라서 핵심 공식은 `Utility dividend capacity + Bank dividend capacity - HoldCo interest/overhead = HEI equity cash capacity`다.

## 2. 핵심 KPI

- Utility rate-base growth와 승인 capex
- allowed ROE와 realized ROE
- regulatory lag / decoupling
- utility FFO와 debt/capital
- ASB NIM, charge-off, NPL, allowance
- ASB CET1/규제자본과 dividend capacity
- HoldCo debt와 만기
- HEI dividend payout
- 산불·허리케인 등 catastrophe exposure와 보험
- liability 발생 시 utility ring-fencing 여부

# Part A — 2008-12-03 Short

## 3. 시장이 무엇을 잘못 가격한다고 봤나

당시 reference price는 약 $26 수준이었다. 숏은 HEI가 안정적인 고배당 utility처럼 거래되지만 실제로는 utility의 낮은 현금회수와 ASB의 Hawaii 부동산 신용위험이 동시에 악화될 수 있다고 봤다. 핵심은 단순 경기침체가 아니라 **두 자회사가 같은 지역경제에 노출되어 분산효과가 약하다**는 것이었다.

유틸리티는 판매량 감소와 큰 capex 때문에 허용 ROE를 실제로 벌지 못했고, 은행은 토지·건설·주택 관련 신용손실이 올라갈 가능성이 있었다. 두 자회사가 동시에 현금을 지주회사에 보내지 못하면 $1.24 배당을 유지하기 어렵고 증자 또는 배당삭감이 촉매가 될 것이라는 논리였다.

원문의 SOTP는 ASB $6.49~9.74, utility $10.30~15.45에서 비은행 순부채 약 $16.56를 차감해 주당 $0.23~8.63을 제시했다. 여기서 중요한 오류는 **정상 영업가치에서 지주회사 부채를 차감하는 과정 자체가 아니라, 위기 시점의 낮은 수익성을 영구 정상상태로 취급했다는 것**이다.

## 4. 실제 결과와 IRR 관점

기존 DB의 실제 가격계열 기준 숏 가격수익은 3개월 약 +43.5%, 6개월 +21.0%, 1년 +12.2%였다. 즉 명시한 6~12개월 이벤트 기간 초반에는 상당한 수익기회가 있었다. 숏 수익은 long CAGR 공식이 아니라 `진입가격-청산가격 / 진입가격`의 unlevered price-return으로 표시하며 대차료·배당·margin financing은 데이터가 없으면 제외한다.

하지만 2년 시점에는 이익이 약 +2.2%로 거의 사라졌고 이후 방향이 역전됐다. 따라서 2008 숏을 “HEI equity가 구조적으로 거의 0”이라는 장기 thesis의 성공으로 기록하면 안 된다. **금융위기라는 촉매를 이용한 단기 숏은 성공했지만 terminal valuation은 틀렸다.**

### RECAP

- 맞춘 것: Hawaii 경기민감도, ASB 신용악화, utility cash conversion 취약성, 두 자회사의 상관위험.
- 틀린 것: 배당삭감이 임박했다는 판단, 극단적 SOTP, 규제회복 가능성 과소평가.
- 숨은 가정: 낮은 realized ROE와 은행손실이 장기간 지속되고 자회사 배당능력이 회복되지 않는다.
- 사전 경고신호: 규제기관의 cost recovery 개선, 은행 자본비율 안정, 실제 배당 유지가 thesis를 약화시키는 신호였다.
- Business verdict: 부분 적중.
- Valuation verdict: 지나치게 bearish.
- Catalyst/timing: 매우 좋음.
- Security selection: common short는 맞았으나 장기 보유는 위험.
- 최종: **단기 이벤트 숏 성공 / 장기 구조적 숏 실패.**

# Part B — 2010-05-09 Short

## 5. 왜 같은 숏이 이번에는 실패했나

2010년 글도 낮은 utility ROE, ASB 부실, 배당부담과 지주회사 구조를 공격했다. 그러나 2008년과 결정적으로 다른 것은 가격과 변화율이었다. 금융위기의 급격한 악화가 이미 지나간 뒤였고, 시장은 정상화 가능성을 보기 시작했다.

특히 utility에서는 판매량과 허용매출을 분리하는 **decoupling**이 중요했다. 이는 전력판매량이 줄어도 규제상 목표매출과 실제매출 차이를 추후 요금으로 조정해주는 구조다. 에너지효율이나 태양광 때문에 kWh 판매가 줄어드는 것을 utility 주주가 그대로 부담하는 구조가 완화된다.

따라서 2010 숏은 “과거에 실제 ROE가 낮았다”는 사실을 맞혔지만 `왜 낮았고 어떤 제도변화가 이를 바꿀 수 있는가`를 충분히 모델링하지 않았다. 규제기업에서 trailing ROE는 원인이 아니라 결과다.

## 6. 실제 결과

기존 DB 가격결과상 숏은 1년 -13.1%, 3년 -33.6%, 5년 -61.8%였다. 배당까지 고려하면 실제 short economics는 더 나빴을 가능성이 높다. 즉 구조적 약점에 대한 분석이 일부 맞아도 투자결과는 명확한 실패다.

### RECAP

- 맞춘 것: utility의 자본집약성, 은행과 utility를 함께 봐야 한다는 관점.
- 틀린 것: 악화된 수준을 변화율과 혼동, 규제제도 개선, 은행 정상화, 배당지속성.
- 숨은 가정: 위기 때의 수익성이 새로운 정상상태다.
- 경고신호: NPL/charge-off의 peak-out, decoupling 진전, dividend 유지.
- 가장 큰 오류: **좋은 2008 short thesis를 2010 가격에 재사용한 것.**
- Business verdict: 약한 부분 적중.
- Valuation: 실패.
- Timing: 실패.
- 최종: **매우 실패.**

# Part C — 2020-06-05 Long

## 7. 이 Long은 무엇을 샀나

2020년 글은 약 $38.90에서 HEI를 단순 고배당 utility가 아니라 `재생에너지 전환으로 rate base가 성장하는 utility + 담보여력이 높은 지역은행`의 조합으로 봤다. Hawaii의 100% renewable 목표를 달성하려면 태양광·풍력·저장장치·DER를 연결하는 송배전망 투자가 필요하고, 승인된 투자액이 rate base에 들어가면 규제이익도 성장할 수 있다는 논리였다.

ASB는 2018~19년 약 13.5% ROE와 3.84% NIM, 낮은 주택 LTV 등을 근거로 이전 금융위기와 다른 저위험 은행으로 평가됐다. 즉 2008년 숏이 공격했던 두 축이 2020년에는 각각 `regulated growth`와 `conservative bank`로 바뀌었다.

여기까지의 정상상태 논리는 상당히 합리적이었다. 실제로 2022년까지 배당은 분기 $0.36까지 올라갔다. 문제는 정상 EPS가 아니라 **단일 재난이 utility liability → HoldCo liquidity → dividend → equity financing으로 전염되는 tail**이었다.

## 8. Maui 산불이 무엇을 바꿨나

2023-08-08 Maui 산불 이후 시장은 정상적인 P/E가 아니라 잠재 손해배상 규모와 생존자본을 가격에 넣기 시작했다. utility의 물리적 자산이 계속 운영돼도 기존 보통주가 그 장기가치를 모두 가져간다는 보장은 없다. 소송·합의·보험한도·차입비용·배당중단·증자 가능성이 equity waterfall 앞에 들어오기 때문이다.

이후 Hawaiian Electric과 HEI를 포함한 피고들은 Maui 산불 tort claims를 해결하기 위한 40억 달러 초과의 글로벌 합의 틀에 들어갔다. 따라서 2020 Long의 실패를 단순히 “예측 불가능한 사고”로 제외하면 안 된다. 발생시점은 예측하기 어렵지만, 산불노출 지역 utility에 대해 `catastrophe liability × insurance gap × equity dilution` 시나리오를 valuation에 넣는 것은 가능했다.

## 9. 실제 결과와 RECAP

기존 DB 가격계열상 1년 +10.8%, 2년 +15.0%로 초기 thesis는 수익을 냈다. 그러나 2024-01 기준 게시가격 대비 약 -65%까지 무너졌다. 따라서 장기보유를 전제로 한 투자판정은 실패다. 산불 이후 장기 소송을 거쳐 2026년에는 settlement payment의 최종 조건이 충족됐다는 공시까지 나왔으므로 이 사건은 일시적 headline이 아니라 실제 자본구조 사건이었다.

- 맞춘 것: 재생에너지 전환의 rate-base 기회, ASB의 정상 수익성, 초기 배당/이익경로.
- 틀린 것: utility를 사실상 low-tail-risk bond proxy처럼 취급한 것.
- 숨은 가정: catastrophe liability가 보험/규제/법적 구조 안에서 흡수된다.
- 경고신호: wildfire mitigation capex, vegetation management, insurance coverage, utility liability precedent, HoldCo liquidity를 별도 KPI로 봤어야 했다.
- Business verdict: 정상상태 논리는 상당부분 적중.
- Valuation verdict: tail-adjusted valuation 실패.
- Catalyst: 정상 성장 촉매는 작동.
- Timing: 초기 성공, 장기 실패.
- Security selection: catastrophe claim보다 후순위인 common equity가 가장 취약.
- 최종: **좋은 정상상태 분석이 나쁜 tail-risk 분석을 상쇄하지 못한 장기 실패.**

# 10. 통합 Postmortem

HEI 세 아이디어의 가장 큰 교훈은 같은 기업의 약점을 발견하는 것보다 **그 약점이 지금 악화 중인지, 회복 중인지, 그리고 어떤 청구권이 equity보다 앞서는지**가 중요하다는 것이다.

2008년에는 신용과 경기의 변화율이 악화되고 있어 숏의 촉매가 있었다. 2010년에는 같은 약점이 이미 알려졌고 규제와 신용이 정상화되는 방향이었다. 2020년에는 정상사업 분석은 좋아졌지만 catastrophe liability라는 다른 상태공간을 누락했다.

따라서 regulated utility + bank 지주회사는 앞으로 다음처럼 분석한다.

`정상 EPS 가치 + rate-base 성장 옵션 + bank franchise 가치 - HoldCo debt - expected catastrophe loss - tail dilution value`.

여기서 expected catastrophe loss는 단순 평균손실만이 아니라 낮은 확률의 대형 손실이 common equity를 얼마나 희석시키는지를 포함해야 한다.

## 출처 메모

기존 VIC/SQL 원문 및 HEI 공시를 기본으로 하고, Maui settlement 관련 후속 사실은 Hawaiian Electric/HEI 공식 공시로 재검증한다. 가격수익률은 기존 DB 가격계열을 유지하며, 정확한 일별 reference price가 없는 경우 임의 가격을 만들어 IRR을 계산하지 않는다.