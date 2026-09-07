# Batch 005 — American Express Pandemic / Rewards V9 Index

> 기존 `analysis/batch_005_american_express_pandemic_rewards.md`는 archive/reference로 유지한다.  
> V9에서는 **평시 quality Long / 위기 후 stress-tested Long / 구조적 rewards Short**를 별도 투자 아이디어로 관리한다.

## Canonical idea files

| VIC 게시일 | 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2020-02-16 | Long | [2020 Feb AXP Long](ideas/2020/2020-02-16_AXP_long.md) | franchise는 맞았지만 tail-state와 path risk를 놓친 부분 성공 |
| 2020-10-14 | Long | [2020 Oct AXP Long](ideas/2020/2020-10-14_AXP_long.md) | 실제 stress를 확인한 뒤 2025년 회복이어도 싸게 산 매우 성공한 Long |
| 2022-05-31 | Short | [2022 AXP Rewards Short](ideas/2022/2022-05-31_AXP_short.md) | rewards를 leakage로만 보고 cohort LTV와 통합 economics를 끊어 구조적 thesis 실패 |

## Batch 005의 핵심 비교

### 2020-02 Long — 정상상태 compounder
원문은:
- 약 15x
- earnings yield 약 7%
- 순이익 성장 약 7%
- 합계 약 14% 장기수익

이라는 간결한 algorithm을 사용했다.

문제는:
- T&E
- corporate spend
- credit reserve
- capital return

이 동시에 흔들리는 state가 모델 밖이었다는 점이다.

실제 1개월 -36.1%, 2020 EPS -52.8%.

다만 franchise는 회복했고 3년 가격수익은 +38.5%.

### 2020-10 Long — stress를 본 뒤 다시 산 compounder
같은 회사지만 정보집합이 달랐다.

이미:
- revenue collapse
- reserve build
- cost flexibility
- capital survival

을 실제로 확인할 수 있었다.

그리고 원문은 2019 수준 회복을 2025년까지 늦춰도 싸다고 봤다.

실제 회복은 2021부터 거의 완료돼 1년 +66.1%.

이 아이디어의 우수성은 V자 회복을 맞힌 것이 아니라 **나쁜 회복경로에도 수익이 남았다는 점**이다.

### 2022 Short — rewards 경쟁을 구조적 붕괴로 본 오류
원문은 rewards·services·marketing·partner payments 증가를 차감해 비이자 이익이 약 90% 사라졌다고 재구성했다.

하지만 이 비용들은 동시에:
- 신규회원
- retention
- annual fee
- spend

를 만드는 상품원가다.

따라서 rewards가 없더라도 같은 revenue가 남는 것처럼 계산하면 안 된다.

실제로:
- 2022 revenue +25%
- 2022 EPS $9.85
- 2023 revenue +14%
- 2023 EPS $11.21

로 구조적 fee-engine 붕괴는 확인되지 않았다.

## Batch 005에서 추출되는 재사용 가능한 교훈

1. **Compounder return algorithm에도 severe recession / tail state를 넣어야 한다.**
2. **회계상 revenue diversification보다 공통 risk factor를 본다.**
3. **Moat는 장기 회복력을 높이지 단기 drawdown을 제거하지 않는다.**
4. **금융회사의 자사주는 규제·자본상태에 조건부다.**
5. **위기 후 Long은 회복속도보다 bear case에서도 남는 기대수익이 중요하다.**
6. **Rewards는 순수 비용이 아니라 customer acquisition / retention / spend의 상품원가일 수 있다.**
7. **일회성 이익을 제거한 뒤 organic earnings bridge를 반드시 다시 계산한다.**
8. **Shared platform의 segment SOTP에는 고객·공유비용·자본의 실제 분리가능성을 검증한다.**
9. **단기 주가방향을 company thesis의 인과적 적중으로 착각하지 않는다.**
10. **강한 확률표현에는 사전 falsifier와 exit rule을 붙인다.**

## 추가 보강 항목

- 세 아이디어의 일별 MFE / MAE
- dividend-adjusted total return
- 2020 Feb severe recession EPS / valuation 재구성
- 2020 Oct 당시 CET1·liquidity·reserve stress table
- 2022 rewards cohort LTV proxy
- organic EPS growth와 buyback 기여 분해
