# Batch 017 v2 Deep — Sprint·AT&T Telecom

> 목적: 기존 Batch 017의 개별 아이디어와 가격경로를 유지하면서, 통신주에서 `좋은 스펙트럼/좋은 FCF/좋은 증권`이 왜 서로 다를 수 있는지 더 명확하게 정리한다.

## 1. 이 배치의 핵심 프레임

통신사는 가입자 기반의 반복매출 사업처럼 보이지만 실제 주주경제성은 `가입자 × ARPU → 서비스매출 → 네트워크·고객획득·단말기 비용 → EBITDA → 네트워크 CapEx·단말기 현금유출·이자 → FCF → 부채·M&A·자사주 → 주당가치`로 내려가야 한다. 특히 Sprint 사례에서는 2.5GHz spectrum의 전략가치는 실제였지만 이를 고객경험과 FCF로 바꾸는 운영능력, 그리고 그때까지 버틸 balance sheet가 부족했다. 따라서 spectrum SOTP는 현금과 동일한 하방이 아니라 ‘누가, 언제, 어떤 조건으로 사줄 수 있는가’라는 duration과 buyer probability를 붙여야 한다.

AT&T는 반대로 가입자 기반과 FCF는 훨씬 안정적이었지만, DirecTV·Time Warner/WarnerMedia 같은 대형 자본배분이 기업가치를 바꿨다. 즉 Sprint는 `좋은 자산이 약한 운영회사 안에 갇힌 문제`, AT&T는 `좋은 현금흐름을 어디에 재배분하느냐의 문제`로 구분하는 것이 맞다.

## 2. 용어와 메커니즘

### Spectrum

이동통신 사업자가 사용할 수 있는 주파수 사용권이다. 면허 희소성 때문에 큰 자산가치를 가질 수 있지만, 고객이 실제로 쓰려면 기지국·backhaul·단말기 ecosystem·망 최적화가 필요하다. 즉 spectrum 자체는 현금이 아니라 ‘네트워크를 구축하면 현금흐름을 만들 수 있는 생산요소’다.

### Churn

기존 가입자가 서비스를 해지하는 비율이다. 통신은 고정비가 큰 사업이므로 churn 상승은 단순히 고객 한 명을 잃는 문제가 아니다. 동일 네트워크 비용을 더 적은 가입자에게 배분하게 되고, 잃은 고객을 채우기 위해 마케팅·프로모션·단말기 보조금도 늘어난다. 그래서 `churn 상승 → CAC 상승 → EBITDA 압박 → FCF 압박`이 비선형적으로 이어질 수 있다.

### Handset lease

회사가 단말기를 고객에게 임대하는 구조다. 단말기 현금은 먼저 지출되지만 회계상 일부가 자산화되어 EBITDA가 좋아 보일 수 있다. 따라서 Sprint 2016 Short처럼 EBITDA와 실제 현금흐름을 분리한 것은 중요한 분석이었다. 문제는 회계왜곡을 발견한 것과 equity가 0이 되는 것은 다른 명제라는 점이다.

## 3. Sprint 아이디어를 다시 읽는 법

| 시점 | 핵심 실수/강점 | v2 판단 |
|---|---|---|
| 2005 Long | Nextel 합병 후 낮은 leverage를 buyback capacity로 봄 | 통합 실패 시 leverage capacity는 buyback 재원이 아니라 생존 buffer가 됨 |
| 2008 Long | QChat·spectrum·breakup value에 하방을 둠 | asset-value trap. 가입자·망 품질 악화가 liquidation option보다 빠르게 equity를 훼손 |
| 2010 Short | standalone economics와 FCF 약화를 정확히 포착 | SoftBank라는 외부 자본공급자와 strategic rescue probability 누락 |
| 2014 Long | 2.5GHz + SoftBank + Claure 개선을 봄 | 사업 방향은 맞았으나 standalone rerating 속도와 2~3배 목표는 과함 |
| 2016 Short | handset lease 회계와 cash burn을 정확히 비판 | 회계/FCF 분석은 좋았지만 T-Mobile strategic value를 0에 가깝게 둔 것이 치명적 |
| 2020 merger arb | 기업가치보다 계약·법률·spread payoff 분석 | 가장 깔끔한 성공. 보통주 방향성이 아니라 증권 payoff를 분석했기 때문 |

### 가장 중요한 비교: 2016 Short vs 2020 Arb

2016 Short는 ‘Sprint 독립기업은 경제성이 나쁘다’는 주장을 했고 상당 부분 맞았다. 그러나 숏의 실제 payoff는 `독립기업 가치`가 아니라 `인수될 확률 × 인수가격 + 독립가치 × 미인수 확률`이었다. T-Mobile에게 Sprint의 2.5GHz가 매우 전략적이었기 때문에 운영부진이 오히려 매각 필요성을 높이는 역설도 있었다.

2020 merger arb에서는 이 불확실성이 대부분 제거됐다. 법원판결, DOJ/FCC 조건, Dish remedy, exchange ratio가 이미 구체화됐고 남은 문제는 closing probability와 시간이었다. 같은 기업이라도 security selection을 바꾸자 분석해야 할 변수가 완전히 달라진다.

## 4. AT&T 아이디어를 다시 읽는 법

AT&T 2018 Long의 강점은 Time Warner 인수 직후 단순한 ‘미디어 성장’이 아니라 FCF와 deleveraging을 중심으로 본 것이다. 이 시기에는 operating thesis보다 `부채가 실제로 줄어드는가`, `배당 후 잔여 FCF가 있는가`, `WarnerMedia가 현금창출에 기여하는가`가 핵심이었다.

반면 2021 Long들은 HBO Max와 fiber의 성장 자체는 일부 맞혔지만, 기업구조가 WarnerMedia 분리로 바뀌면서 기존 SOTP의 귀속이 달라졌다. 분할 전 AT&T 주주가 보유하던 성장자산의 일부가 별도 거래구조로 이동하면 ‘사업이 잘된다’와 ‘현재 T 주식이 그 가치를 계속 보유한다’는 같은 문장이 아니다.

## 5. 사전에 반드시 봤어야 할 반증조건

1. Sprint Long에서는 postpaid churn이 개선되지 않는데도 spectrum SOTP만 상승한다면 thesis를 축소했어야 한다.
2. Sprint Short에서는 strategic buyer가 asset value를 인정할 가능성과 SoftBank의 자금지원 능력을 별도 확률변수로 넣었어야 한다.
3. AT&T Long에서는 자산매각·spin·배당정책 변경으로 주주가 받는 청구권이 바뀔 가능성을 valuation bridge에 포함했어야 한다.
4. 모든 통신주에서 EBITDA보다 `EBITDA − network CapEx − handset cash − interest`를 우선 확인해야 한다.

## 6. 통합 Postmortem

가장 큰 교훈은 **좋은 통신자산의 가치가 보통주에 자동으로 귀속되지 않는다는 것**이다. Sprint의 spectrum은 훗날 T-Mobile에서 막대한 전략가치를 증명했지만 기존 Sprint 독립기업은 그 가치를 충분히 수익화하지 못했다. 반대로 AT&T는 안정적인 FCF를 보유했지만 대형 M&A와 분할이 주주가 실제로 보유하는 자산구성을 계속 바꿨다.

따라서 다음 통신 투자에서는 `자산가치 → 운영 monetization → FCF → 자본구조 → 주주 청구권 → 촉매/시간`의 6단계를 분리한다. 특히 merger arb, bond, common equity를 같은 회사라는 이유로 하나의 thesis로 합치지 않는다.

## 7. 최종 판정 프레임

- **Business thesis:** Sprint 독립사업은 약했고 spectrum은 강했다. AT&T 핵심 connectivity FCF는 강했으나 미디어 자본배분은 혼합.
- **Valuation thesis:** spectrum·SOTP는 monetization haircut과 duration이 없으면 과대평가되기 쉽다.
- **Catalyst/timing:** 2020 Sprint merger arb가 가장 우수. 2005/08 turnaround와 2021 AT&T는 촉매를 과대평가.
- **Security selection:** common equity보다 merger spread처럼 payoff가 명확할 때 분석 신뢰도가 크게 높아졌다.
- **재사용 질문:** `이 자산이 좋은가?`가 아니라 `이 자산의 가치가 언제, 어떤 경로로, 지금 내가 가진 증권에 귀속되는가?`