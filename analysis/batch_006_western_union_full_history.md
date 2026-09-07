# Batch 006 — Western Union (WU), Agent Moat와 디지털 전환 완전 재분석 v2

대상: 2007~2017 VIC 아이디어 9건

## 0. 한눈에 보는 결과

| 게시일 | 방향 | 실제 가격경로 | 판정 |
|---|---|---|---|
| 2007-07-12 | Long | 1Y +16.4%, 3Y -23.1%, 5Y -16.8% | 실패 |
| 2011-09-15 | Long | 1Y +18.5%, 3Y +11.6%, 5Y +44.3% | 부분 성공 |
| 2012-11-13 | Short | 1Y -42.8%, 3Y -60.7%, 5Y -80.9% 숏손익 | 치명적 실패 |
| 2013-06-06 | Short | 1Y -0.5%, 3Y -29.0%, 5Y -45.4% | 실패 |
| 2013-08-29 | Short | 6M +6.7%, 1Y -2.6%, 5Y -26.2% | 실패 |
| 2014-02-25 | Long | 1Y +23.1%, 3Y +35.2%, 5Y +27.8% | 부분 성공 |
| 2015-04-13 | Long | 1Y -0.5%, 3Y +1.9%, 5Y +15.3% | 실패 |
| 2016-03-18 | Short | 1Y -9.3%, 3Y -6.1%, 5Y -56.5% | 실패 |
| 2017-09-10 | Long | 1Y +5.1%, 3Y +34.5%, 5Y -3.2% | 부분 성공 |

raw SQL은 9건 모두 Short지만 실제는 Long 5 / Short 4다.

## 1. Western Union은 무슨 기업인가

WU는 국제송금 원금 자체를 매출로 잡는 회사가 아니다. 고객이 보내는 돈을 전달하고 **transaction fee + FX spread**를 번다. 현금 고객은 우체국·은행·편의점 등 agent에 돈을 내고 상대국 agent에서 현금으로 찾을 수 있다.

Agent는 WU 직원/점포가 아니라 제3자다. 그래서 WU는 거대한 물리망을 적은 직접 capex로 운영하지만 transaction fee 일부를 agent에 지급한다. 보내는 곳과 받는 곳이 많을수록 고객이 늘고 고객이 많을수록 agent가 가입하는 양면 network다.

디지털은 이 moat를 없애는 동시에 WU가 재사용할 수 있는 자산이기도 하다. 고객이 앱에서 송금을 시작해도 수취인이 현금을 원하면 WU payout network가 필요하다. 반대로 account-to-account가 보편화되면 물리망 가치가 줄어든다.

## 2. 돈의 흐름과 용어

`송금건수 × (평균 fee + FX spread) - agent commission - compliance/fraud - technology/marketing = operating profit`.

- Corridor: 미국→멕시코처럼 특정 송금국가 쌍.
- Revenue per transaction: 건당 fee와 FX economics. volume이 늘어도 이 값이 더 빨리 하락하면 매출은 감소한다.
- Compliance scale: AML/KYC/sanctions 시스템은 큰 고정비지만 규모가 큰 WU에는 진입장벽이기도 하다.
- Self-cannibalization: WU.com이 기존 고마진 retail 고객을 더 싼 digital channel로 이동시키는 현상.

2023년에도 Consumer Money Transfer는 WU consolidated revenue의 92%였고, 회사는 200개 이상 국가/지역에 network를 유지했다. 즉 digital disruption은 network를 즉시 0으로 만들지 않았다.

## 3. 장기적으로 실제 무슨 일이 있었나

2007~2017 C2C transaction은 크게 증가했지만 2012~17 C2C revenue와 operating income은 오히려 감소했다. **숏이 예측한 가격/마진 압박은 실제였다.** 그러나 WU는 현금흐름을 계속 만들고 자사주와 배당을 지급했다. **롱이 본 cash moat도 실제였다.**

따라서 핵심은 disruption 여부가 아니라 `disruption 속도 vs 시작 valuation + capital return`이었다.

# 4. 2007-07-12 Long

약 $20.75에서 agent network, 이민/송금 성장, asset-light FCF와 $32 DCF를 봤다. 모바일 송금은 unbanked 고객에게 먼 미래라고 판단했다. 사업은 사라지지 않았지만 margin은 이미 하락 중이었다. volume growth를 profit growth로 연결한 것이 오류였다.

1Y +16.4% 후 3Y -23.1%, 5Y -16.8%. **맞춘 것:** network durability. **틀린 것:** margin trajectory와 목표가. **경고신호:** transaction 성장보다 operating income 성장률이 낮아지는 현상. 최종 실패.

# 5. 2011-09-15 Long

약 10배 unlevered FCF와 거대한 agent network를 샀다. 스마트폰 경쟁이 와도 compliance, brand와 cash payout이 쉽게 복제되지 않는다는 논리였다. 이 판단은 상당히 맞았다. 다만 moat는 가격결정력을 완전히 보호하지 못했다.

1Y +18.5%, 5Y +44.3%로 5년 CAGR은 약 7.6%다. 낮은 valuation과 capital return이 구조적 둔화를 흡수했다. **부분 성공.**

# 6. 2012-11-13 Short

온라인 가격비교와 digital transfer가 WU의 높은 fee를 투명하게 만들어 50% 이상 하락할 것이라고 봤다. 사업방향은 정확했다. 실제로 WU는 가격 reset을 하고 margin이 하락했다.

그러나 진입가격은 이미 이 문제를 상당부분 반영했다. transaction volume이 증가했고 cash network는 즉시 사라지지 않았으며 buyback도 계속됐다. 1Y 숏 -42.8%, 5Y -80.9%. **사업을 맞히고 주식을 틀린 대표 사례.**

RECAP: disruption thesis 적중 / speed 과대평가 / valuation 실패 / catalyst 부재 / 치명적 투자실패.

# 7. 2013-06-06 Short

스마트폰을 Kodak moment로 봤다. 문제는 사진필름과 송금의 switching mechanism이 다르다는 점이다. 송금은 send-side UI만 디지털화한다고 끝나지 않는다. 수취인의 bank account penetration, cash preference, AML/KYC, payout infrastructure가 함께 변해야 한다.

1Y 거의 보합, 3Y -29%, 5Y -45.4% 숏손실. **기술방향을 adoption curve와 혼동한 실패.**

# 8. 2013-08-29 Short

ROIC 하락, 가격압박과 $11~14 목표를 제시했다. 가격압박은 맞았지만 이미 2012 price reset 뒤 volume response가 나타나고 있었다. 가격을 내렸을 때 transaction elasticity가 충분하면 profit decline은 예상보다 느릴 수 있다.

6M +6.7%의 작은 이익 후 5Y -26.2%. **단기 trade 가능 / 구조적 short 실패.**

# 9. 2014-02-25 Long

Mexico pricing과 compliance 비용을 일시적 reset으로 보고 낮은 FCF multiple과 buyback을 샀다. 핵심은 성장기업으로의 복귀가 아니라 **느린 decline보다 더 낮은 가격**이었다.

1Y +23.1%, 3Y +35.2%, 5Y +27.8%. 5년 CAGR 약 5%로 원래 기대한 20% IRR에는 크게 못 미쳤다. 따라서 성공이라기보다 부분 성공이다.

# 10. 2015-04-13 Long

기술파괴 가능성이 낮고 12배 FCF가 싸다는 논리였다. network survival은 맞았지만 terminal growth와 capital return만으로 충분한 복리가 나오지 않았다. 5Y +15.3%, CAGR 약 2.9%. **기업생존을 투자성공과 혼동한 사례.**

# 11. 2016-03-18 Short

경쟁, margin 하락과 공격적 비용자본화를 공격했다. 회계품질 점검은 유용했지만 cash generation과 valuation을 이길 만큼 빠른 deterioration이 없었다. 5Y 숏 -56.5%. **회계 red flag가 catalyst가 되지 못한 실패.**

# 12. 2017-09-10 Long

WU.com이 2020년까지 커지며 EPS를 10~13% 성장시키고 $19→$33이 가능하다고 봤다. 이 아이디어는 digital을 위협이 아니라 WU가 기존 brand/compliance/payout을 재사용하는 채널로 본 점이 좋았다.

그러나 digital 사업이 성장해도 기존 retail의 가격/volume을 잠식한다. 성장사업의 규모가 legacy decline을 상쇄하는지 반드시 `digital incremental profit - retail cannibalization`으로 계산해야 한다.

1Y +5.1%, 3Y +34.5%, 5Y -3.2%. **digital asset 발견은 맞았지만 consolidated rerating thesis는 실패.**

# 13. 통합 RECAP

### 숏이 맞춘 것

가격투명성, digital migration, revenue/transaction 압력, 장기 margin erosion.

### 숏이 틀린 것

파괴속도, cash payout network의 잔존가치, compliance scale, 낮은 valuation과 buyback의 방어력.

### 롱이 맞춘 것

network가 하루아침에 사라지지 않는다는 점, 높은 FCF conversion, capital return.

### 롱이 틀린 것

transaction volume을 pricing power로 착각하고 digital growth가 legacy decline을 자동 상쇄한다고 본 것.

### 다음 투자에서 바꿀 것

Legacy disruption은 `기술이 더 좋은가?`가 아니라 다음 다섯 변수를 시간축으로 모델링한다.

1. 신규채널 adoption 속도
2. 기존채널 가격하락
3. 고객/agent switching friction
4. incumbent의 자기잠식 대응
5. 시작 FCF yield + capital return

**최종 교훈: 나빠지는 사업을 short하는 것과 나쁜 주식을 short하는 것은 다르다.** WU는 실제로 구조적으로 둔화됐지만 여러 숏의 진입가격은 그보다 더 빠른 붕괴를 요구했다.