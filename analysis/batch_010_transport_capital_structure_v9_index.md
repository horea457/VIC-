# Batch 010 — Transport / Capital Structure V9 Index

> 기존 `analysis/batch_010_transport_capital_structure_30.md`와 `analysis/batch_010_transport_capital_structure_v2_deep.md`는 archive/reference로 유지한다.  
> V9에서는 **30개 VIC 아이디어를 각각 독립 canonical report**로 관리한다.

---

# 1. Canonical idea files

## Aimia / AerCap — 8건

| 날짜 | Ticker | 파일 | 핵심 판정 |
|---|---|---|---|
| 2011-09-15 | AIMIA | [Aimia Long](ideas/2011/2011-09-15_AIMIA_long.md) | 단기 성공·장기 논지 훼손; 기존 DB AerCap 가격 혼입 오류 |
| 2014-01-27 | AER | [AerCap Long](ideas/2014/2014-01-27_AER_long.md) | ILFC 사업시너지는 맞았지만 24개월 기간 미달 |
| 2015-12-28 | AER | [AerCap Long](ideas/2015/2015-12-28_AER_long.md) | book growth 논지 일부 적중, 주가 실패 |
| 2017-07-14 | AER | [AerCap Long](ideas/2017/2017-07-14_AER_long.md) | 실패 — 평시 aircraft sale premium을 stress value로 사용 |
| 2018-06-21 | AER | [AerCap Long](ideas/2018/2018-06-21_AER_long.md) | 명시기간 실패·3년 회복 |
| 2019-02-06 | AER | [AerCap Long](ideas/2019/2019-02-06_AER_long.md) | 성공·큰 path risk |
| 2020-08-17 | AER | [AerCap COVID Long](ideas/2020/2020-08-17_AER_long.md) | 매우 성공 — stress value + liquidity runway |
| 2022-02-05 | AER | [AerCap GECAS Long](ideas/2022/2022-02-05_AER_long.md) | 부분 성공·러시아 압류 tail |

## Hertz — 8건

| 날짜 | 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2013-01-08 | Long | [HTZ Long](ideas/2013/2013-01-08_HTZ_long.md) | 단기 synergy 성공·장기 실패 |
| 2014-01-20 | Long | [HTZ Long](ideas/2014/2014-01-20_HTZ_long.md) | 실패 |
| 2017-05-31 | Long | [HTZ Long](ideas/2017/2017-05-31_HTZ_long.md) | 부분 성공 후 실패 |
| 2017-08-31 | Short | [HTZ Short](ideas/2017/2017-08-31_HTZ_short.md) | 매우 성공·회수율 과신 |
| 2018-09-04 | Long | [HTZ Long](ideas/2018/2018-09-04_HTZ_long.md) | 치명적 실패 |
| 2019-05-14 | Short | [HTZ Short](ideas/2019/2019-05-14_HTZ_short.md) | 매우 성공 |
| 2020-06-08 | Short | [HTZ Bankruptcy Equity Short](ideas/2020/2020-06-08_HTZ_short.md) | 논지 실패·옵션 성과 판정 불가 |
| 2022-02-18 | Long | [Post-Reorg HTZ Long](ideas/2022/2022-02-18_HTZ_long.md) | 실패 |

## Spirit Airlines — 7건

| 날짜 | 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2012-03-12 | Long | [SAVE Long](ideas/2012/2012-03-12_SAVE_long.md) | 성공 |
| 2013-01-23 | Long | [SAVE Long](ideas/2013/2013-01-23_SAVE_long.md) | 매우 성공 |
| 2015-10-28 | Long | [SAVE Long](ideas/2015/2015-10-28_SAVE_long.md) | 실패 |
| 2017-05-09 | Long | [SAVE Long](ideas/2017/2017-05-09_SAVE_long.md) | 치명적 실패 |
| 2018-04-17 | Long | [SAVE Long](ideas/2018/2018-04-17_SAVE_long.md) | 실패 |
| 2020-06-18 | Long | [SAVE EETC Long](ideas/2020/2020-06-18_SAVE_long.md) | 성공 |
| 2022-05-05 | Long | [SAVE Merger Arb](ideas/2022/2022-05-05_SAVE_long.md) | 실패 — 법원 차단 |

## General Motors — 7건

| 날짜 | 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2009-04-27 | Short | [Old GM Call Short](ideas/2009/2009-04-27_GM_short.md) | 매우 성공 |
| 2011-02-17 | Long | [New GM Long](ideas/2011/2011-02-17_GM_long.md) | 실패 |
| 2012-01-06 | Long | [GM NOL / Cash Stub Long](ideas/2012/2012-01-06_GM_long.md) | 매우 성공 |
| 2013-02-25 | Long | [GM Treasury Exit Long](ideas/2013/2013-02-25_GM_long.md) | 성공·목표 미달 |
| 2013-03-20 | Long | [GM Warrant Long](ideas/2013/2013-03-20_GM_long.md) | 성공 |
| 2017-11-19 | Long | [GM Core + Cruise Long](ideas/2017/2017-11-19_GM_long.md) | 실패 |
| 2018-05-19 | Long | [GM Truck Profit Pool Long](ideas/2018/2018-05-19_GM_long.md) | 성공·큰 경로위험 |

---

# 2. Batch 010의 핵심 질문

이 배치의 공통 질문은 매우 단순하다.

> **좋은 실물자산이 실제로 common equity를 보호하는가?**

답은 자주 **아니다**였다.

실물자산의 가치가 아무리 커도 그 위에:

- secured debt
- fleet debt / ABS
- lease obligations
- pension
- corporate debt
- liquidity reserve
- bankruptcy costs

가 있으면 보통주의 residual claim은 훨씬 작다.

따라서 기본식은:

**Stress asset value  
- secured claims  
- other debt  
- fixed obligations  
- required liquidity  
= residual equity value**

다.

---

# 3. Aimia / AerCap — entity와 residual value부터 확인

## Aimia
Aimia는 loyalty program 회사다.

핵심 위험은 포인트 회계가 아니라:
- anchor airline
- major credit-card partner

가 떠날 때 program value가 동시에 훼손되는 것이다.

특히 기존 DB에서 **Aimia와 AerCap의 ticker/entity가 충돌해 잘못된 가격성과가 붙은 오류**가 있었다.

이건 단순 데이터 정정이 아니라 중요한 원칙이다.

> **Security identity가 틀리면 모든 사후분석도 틀린다.**

## AerCap
AerCap은 aircraft leasing company다.

좋은 항공기와 낮은 P/B만으로는 부족하다.

예를 들어:

- aircraft value -10%
- debt는 그대로

이면 equity는 훨씬 더 크게 하락할 수 있다.

### 2020 COVID Long이 좋았던 이유

평시 book value를 믿은 게 아니라 이미 stress가 가격에 크게 반영된 상태에서:

- liquidity runway
- movable collateral
- funding access
- stress aircraft value

를 같이 봤다.

실제 1년 **+76.68%**.

즉 낮은 P/B가 아니라:

> **stress value 대비 낮은 가격 + survival**

이 핵심이었다.

---

# 4. Hertz — 산업생존과 issuer 생존은 다르다

Hertz는 자동차를 빌려주는 사업이지만 실제 equity economics는:

**Rental revenue  
- fleet depreciation  
- vehicle interest  
- corporate opex  
- fixed charges**

다.

특히 used-car residual value가 중요하다.

## 2018 Long의 대표 오류

“렌터카 산업은 ride-sharing 때문에 사라지지 않는다.”

이 자체는 틀리지 않았다.

하지만 이걸:

> **따라서 당시 높은 leverage의 Hertz equity는 안전하다**

로 바꿨다.

2020 Chapter 11이 보여준 건:

> **산업이 살아남는 것과 특정 issuer의 equity가 살아남는 것은 다르다.**

## 2019 Short가 더 좋았던 이유

취약한 financing structure와 FCF, refinancing wall을 직접 공격했다.

즉 business direction보다 **capital structure를 security selection에 반영**했다.

---

# 5. Spirit — Common, EETC, Merger Arb는 완전히 다른 투자

Spirit의 ULCC economics는:
- low CASM
- ancillary revenue
- high utilization

이 핵심이다.

하지만 증권은 세 가지로 분리해야 한다.

## Common equity
항공수요·유가·임금·capacity competition에 직접 노출.

## EETC
항공기를 담보로 한 구조화 채권.

2020 EETC Long이 성공한 이유는 Spirit equity를 산 게 아니라:

> **aircraft collateral + priority**

를 샀기 때문이다.

## Merger Arb
2022 JetBlue 거래에서는 Spirit의 좋은/나쁜 사업보다:

**DOJ / 법원 승인확률  
× deal spread  
+ break value**

가 핵심이었다.

결국 2024-01-16 법원이 거래를 차단했다.

따라서 merger arb에서:

> **규제위험을 business quality로 상쇄할 수 없다.**

---

# 6. GM — 같은 이름, 다른 증권

GM 사례는 capital structure lesson이 가장 선명하다.

## Old GM 2009
기존 common의 residual value가 거의 사라진 상황에서 call option을 매도.

구주 option은 무가치가 되어 성공.

## New GM 2011
파산 후 새 capital structure.

구 GM과 같은 ticker history로 보면 안 된다.

낮은 valuation은 매력적이었지만:
- Europe
- pension
- auto cycle

을 과소평가해 실패.

## 2012 Long
더 낮은 가격, NOL, excess cash라는 더 좋은 setup.

실제:
- 1Y +29.84%
- 3Y +55.60%
- 5Y +83.76%

## 2013 Warrant
Common과 달리 strike·maturity가 있는 별도 payoff.

성과도 보통주와 같은 방식으로 계산하면 안 된다.

## 2017 Cruise SOTP
Cruise option에 가치를 넣은 건 합리적이지만:

**기술 option value  
× 성공확률  
× 현금화확률  
- funding requirement**

를 해야 했다.

미실현 option을 액면가로 더한 것이 오류였다.

---

# 7. Batch 010의 대표 성공/실패 유형

## 성공 유형 1 — Stress asset value + survival

대표:
- AerCap 2020

## 성공 유형 2 — Security seniority / collateral 선택

대표:
- SAVE EETC 2020

## 성공 유형 3 — 파산 전 residual claim을 정확히 공격

대표:
- Old GM Call Short 2009

## 성공 유형 4 — post-reorg 낮은 가격에서 새 capital structure를 재평가

대표:
- GM 2012

## 실패 유형 1 — Asset value를 equity floor로 오해

대표:
- AER 2017/2018
- HTZ Longs

## 실패 유형 2 — 산업생존을 issuer 생존으로 오해

대표:
- HTZ 2018

## 실패 유형 3 — 단일 cost advantage를 영구화

대표:
- SAVE 2017/2018

## 실패 유형 4 — 기술 option을 확정가치로 합산

대표:
- GM Cruise 2017

## 실패 유형 5 — Merger approval probability 과대평가

대표:
- SAVE 2022

---

# 8. Batch 010의 V9 원칙

### 원칙 1
**Asset value ≠ Equity value**

항상 liability waterfall을 만든다.

### 원칙 2
**Industry survival ≠ Issuer survival**

회복까지 버틸 liquidity가 먼저다.

### 원칙 3
**Book value는 stress liquidation value가 아니다**

특히 leveraged lessor에서는 그렇다.

### 원칙 4
**Collateralized debt는 common과 다른 투자다**

EETC, ABS, fleet debt는 담보와 priority를 본다.

### 원칙 5
**Post-reorg equity는 새 회사처럼 underwriting**

구주 history를 그대로 이어 붙이지 않는다.

### 원칙 6
**Option value는 probability-adjusted**

Cruise·AV 같은 미래사업은 확정가치가 아니다.

### 원칙 7
**Merger-arb는 standalone business thesis와 분리**

법원·규제·outside date가 핵심이다.

### 원칙 8
**같은 issuer라도 증권별로 결과가 다르다**

Common, debt, warrant, option, EETC, merger arb를 하나의 return series로 섞지 않는다.

---

# 9. 향후 정밀 가격 / Security Pass

Batch 010은 security 종류가 많아 추가 보강 가치가 크다.

향후:

1. exact entry close
2. MFE / MAE
3. Long total return
4. Short borrow/dividend carry
5. bond clean price + accrued interest
6. coupon cash-flow IRR
7. EETC recovery / collateral value
8. warrant strike·expiry·dividend adjustment
9. option premium·strike·expiry
10. merger spread actual annualized IRR
11. bankruptcy recovery waterfall
12. entity/ticker validation

을 일괄 보강한다.

**확인되지 않은 옵션·채권 IRR은 임의로 생성하지 않는다.**
