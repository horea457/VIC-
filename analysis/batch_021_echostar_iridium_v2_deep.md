# Batch 021 v2 Deep — EchoStar·Iridium

> 목적: 기존 Batch 021의 10개 아이디어를 `위성 자산가치·capacity economics·replacement CapEx·launch risk·LEO 경쟁·financing`으로 다시 읽는다.

## 1. 위성회사는 SOTP보다 시간축이 중요하다

위성통신 회사는 장부상 위성·주파수·현금·지분투자가 커서 SOTP가 매력적으로 보이기 쉽다. 하지만 자산가치가 실제 주주가치가 되려면 위성을 제작·발사하고, capacity를 채우고, 고객이 계약을 유지하며, 다음 replacement cycle을 위한 CapEx까지 감당해야 한다. 따라서 `asset value`와 `network economics`를 분리해야 한다.

EchoStar의 GEO broadband는 특히 duration이 길다. 위성 제작과 발사에 수년이 걸리고 CapEx는 먼저 발생하며, launch 뒤에야 가입자를 받아 utilization을 올린다. 한 위성이 capacity ceiling에 도달하면 신규가입 성장이 멈추고 다음 위성까지 공백이 생길 수 있다. 이 때문에 EBITDA가 견조해도 FCF와 주가가 긴 시간 정체될 수 있다.

## 2. GEO broadband의 돈의 흐름

핵심 흐름은 다음과 같다.

`위성 제작·발사 CapEx → orbital capacity 확보 → 가입자 증가 × ARPU → 서비스매출 → ground/network·SG&A → EBITDA → maintenance/replacement satellite CapEx → FCF`

중요한 점은 위성이 감가상각되는 회계자산인 동시에 실제로 다시 교체해야 하는 생산자산이라는 것이다. 따라서 단순 EBITDA multiple에 replacement CapEx를 무시하면 economics를 과대평가한다.

## 3. EchoStar Long들이 반복적으로 틀린 지점

2008~2018 Long들은 cash, STB, satellite, spectrum, Hughes를 더한 SOTP에서 큰 upside를 찾았다. 개별 자산가치는 상당 부분 실제였지만 다음 세 가지가 반복적으로 과소평가됐다.

1. **Monetization duration:** 자산이 팔리거나 spin될 때까지 몇 년이 걸릴지 불확실했다.
2. **Capital leakage:** 위성 제작·launch·replacement CapEx가 계속 필요했다.
3. **Competitive regime change:** rural broadband에서 GEO가 사실상 독점적 대안이라는 가정이 Starlink·FWA로 무너졌다.

따라서 `$1의 현금 + $1의 spectrum + $1의 satellite`를 모두 같은 $1로 더하면 안 된다. 현금은 즉시 가치, spectrum은 규제·buyer path, 위성은 utilization·수명·replacement liability를 반영해야 한다.

## 4. 2019 Long이 특히 중요한 이유

2019 Long의 큰 오류는 LEO 위협이 5~20년 뒤라는 가정이었다. Starlink는 예상보다 훨씬 빠르게 rural broadband의 성능·latency·capacity 기준을 바꿨다. 이것은 단순 경쟁사 등장보다 더 중요하다. GEO의 긴 투자주기 때문에 경쟁환경이 바뀌어도 기존 architecture를 빠르게 바꾸기 어렵기 때문이다.

위성산업에서는 기술위험을 ‘현재 시장점유율’로만 보면 안 된다. 다음 replacement cycle이 끝나는 시점에 고객이 어떤 성능을 기대할지를 봐야 한다. 긴 asset duration이 기술 변화에 대한 취약성을 키운다.

## 5. Iridium 2009 Long vs Short

같은 시점에 Long과 Short가 충돌한 것이 이 배치의 가장 좋은 학습자료다.

### Long의 관점

- 전 세계 coverage라는 희소성
- recurring service revenue
- government·maritime·aviation·M2M 같은 niche demand
- NEXT constellation financing이 해결되면 큰 overhang 제거

### Short의 관점

- 위성교체에 $2.7bn+ 필요
- handset 경쟁과 기술노후
- 현재 EBITDA가 replacement economics를 과장

둘 다 중요한 점을 봤다. 결국 승패를 가른 것은 replacement cost 자체가 아니라 **financing access와 서비스의 지불의사**였다. Coface-backed financing 등으로 NEXT 자금조달이 가능해지면서 기존 network가 끊기기 전에 새 constellation으로 넘어갈 수 있었고, global coverage가 필요한 niche 고객이 가격을 지불했다.

즉 capital-intensive infrastructure에서 ‘CapEx가 크다’는 Short 논지만으로 부족하다. `CapEx를 누가 어떤 금리와 보증조건으로 조달할 수 있는가`, 그리고 `그 이후 cash yield가 자본비용을 넘는가`가 핵심이다.

## 6. 아이디어별 v2 판정

| 구간 | 핵심 판단 | v2 교훈 |
|---|---|---|
| SATS 2008 Long | spin SOTP·cash floor | 현금 외 자산에 duration/leakage haircut 부족 |
| SATS 2010 Long | orphan discount·NAV | 성공했지만 3년 duration 필요 |
| SATS 2012 Long | Hughes/JUPITER capacity | operating catalyst가 있어 더 강한 Long |
| SATS 2013~18 Long | EBITDA/SOTP 반복 | replacement CapEx·monetization timing 과소평가 |
| SATS 2019/21 Long | GEO moat·JUPITER3 | LEO/FWA regime change와 launch delay가 압도 |
| IRDM 2009 Long | coverage + recurring + financing | 장기 결과가 강하게 지지 |
| IRDM 2009 Short | replacement cost | financing probability를 너무 낮게 봄 |

## 7. 사전 반증조건

- 신규 위성 launch가 2개 분기 이상 지연되면 subscriber/FCF bridge를 즉시 다시 계산한다.
- capacity가 차는데 다음 satellite가 준비되지 않으면 성장률에 자동 haircut을 적용한다.
- 경쟁자가 latency·speed·installation economics를 한 단계 바꾸면 과거 rural TAM을 그대로 쓰지 않는다.
- spectrum·strategic asset은 구체적 buyer·regulatory path가 없으면 현금가치의 일부만 인정한다.
- replacement CapEx 조달조건이 악화되면 equity SOTP보다 credit survival을 먼저 본다.

## 8. 통합 Postmortem

이 배치의 핵심은 **위성 자산의 replacement cost가 크다는 사실과 가치가 없다는 사실은 다르고, 자산가치가 크다는 사실과 주식이 싸다는 사실도 다르다**는 것이다. EchoStar는 실제 자산을 보유했지만 그 가치를 monetization하는 시간이 길었고 기술경쟁이 그 사이 바뀌었다. Iridium은 큰 replacement burden이 있었지만 niche network value와 financing이 그것을 넘었다.

- **Business thesis:** Hughes GEO와 Iridium global network 모두 실제 고객가치가 있었으나 경쟁구조는 크게 달랐다.
- **Valuation thesis:** SOTP에는 duration, replacement CapEx, tax/leakage, 경쟁 haircut이 필요하다.
- **Catalyst/timing:** JUPITER launch처럼 operating catalyst가 있는 Long이 단순 asset discount Long보다 우수했다.
- **Security selection:** capital-intensive network는 common equity보다 debt/financing 구조까지 함께 분석해야 한다.
- **재사용 질문:** `이 위성의 가치가 얼마인가?`보다 `다음 교체주기까지 이 자산이 얼마의 FCF를 만들고 어떤 비용으로 다시 교체되는가?`