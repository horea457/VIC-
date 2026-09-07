# Batch 009 v2 Deep — Netflix·ADT·Activision Blizzard·Alibaba

## 목적
기존 30개 아이디어의 기본 사실관계와 장기결과를 유지하면서, 처음 읽는 사람이 이해할 수 있도록 각 기업의 **돈 버는 구조, 실제 주주현금흐름, 청구권, 핵심 숨은 가정, 실제 투자결과와 RECAP**을 더 명시적으로 정리한다.

---

# 1. Netflix — 현재 margin과 terminal economics를 혼동하지 않기

Netflix는 구독료를 먼저 받고 콘텐츠를 장기간 소비시키는 모델이다. 단순 매출식은 `가입자 × ARPU`지만 가치평가 핵심은 콘텐츠 현금지출과 상각의 시차다. 콘텐츠 제작비는 현금이 먼저 나가고 비용은 여러 해에 걸쳐 상각되므로 GAAP 영업이익이 좋아져도 FCF가 뒤처질 수 있다.

## 핵심 용어
- **ARPU**: 가입자당 평균매출.
- **Churn**: 유료회원 이탈률.
- **Content amortization**: 이미 지출한 콘텐츠 제작비를 여러 기간에 나눠 비용처리하는 것.
- **Content cash spend**: 실제로 해당 기간 현금이 나간 금액. 장기 경제성에서는 상각보다 이 값이 중요할 수 있다.

## 아이디어들을 다시 읽는 법
- **2003 Short:** churn과 LTV 회계의 허점을 잘 지적했지만, 현재 DVD cohort economics를 회사 전체 terminal value로 고정했다. 사업모델이 DVD→streaming으로 진화할 옵션을 거의 0으로 봤다는 것이 치명적 오류다.
- **2007 Long:** 당시 DVD economics와 낮은 valuation은 맞았다. 더 중요한 점은 스트리밍 성공이 없어도 싸다고 본 하방규율이다. 이후 실제 초과수익은 오히려 스트리밍 전환에서 왔다.
- **2010 Long:** 글로벌 streaming operating leverage는 맞았지만 2011 Qwikster 충격처럼 전환과정의 가격·제품 실수 위험을 과소평가했다.
- **2012 Long:** $64 부근에서 국내 streaming franchise 가치만으로 하방을 만들고 해외를 옵션으로 둔 구조가 매우 좋았다.
- **2013/2016 Shorts:** DVD 이익소멸, cash burn, 경쟁은 상당 부분 맞았다. 하지만 `사업이 더 자본집약적이다`와 `주가가 하락한다`를 동일시했다. 가입자 성장과 TAM 확대가 valuation denominator를 계속 키웠다.
- **2016/2019 Longs:** 가장 중요한 변수는 margin 자체보다 **회원당 장기 콘텐츠비용이 규모로 얼마나 낮아질 수 있느냐**였다. 이후 광고요금제·paid sharing까지 monetization 옵션이 추가됐다.

## Netflix RECAP
맞춘 롱: 글로벌 규모와 distribution flywheel. 맞춘 숏: 콘텐츠 cash burn과 경쟁심화. 숏의 큰 오류: terminal economics가 아직 형성되지 않은 플랫폼을 현재 margin으로 고정. 다음 투자에서는 `current margin`, `mature cohort contribution`, `long-run content spend/member`, `pricing power`를 분리한다.

---

# 2. ADT — RMR만 보면 왜 위험한가

ADT는 월정액 보안서비스를 제공해 반복매출(RMR)을 만든다. 문제는 고객 1명을 설치하기 위해 장비·영업·설치비를 먼저 쓰고, 해지될 때까지 오랜 기간 그 비용을 회수한다는 점이다.

## 핵심 용어
- **RMR(Recurring Monthly Revenue)**: 매달 반복적으로 받는 서비스 수익.
- **SAC(Subscriber Acquisition Cost)**: 신규고객 설치·영업에 들어간 선행비용.
- **Attrition**: 고객 이탈률. churn과 유사하지만 보안업계에서는 attrition 용어를 많이 쓴다.

## 아이디어별 핵심
- 저가 Long들은 `RMR multiple`이 싸다는 점을 봤지만, 진짜 검증식은 `고객 LTV - 유지·획득 SAC - 부채비용`이다.
- 2015 Short는 레버리지와 subscriber economics를 공격했지만, 안정적인 RMR이 refinancing runway를 늘리는 점을 과소평가했다.
- 2018/2020 Long의 핵심 오류는 Google partnership 등 전략적 뉴스가 높은 leverage와 유지 SAC 문제를 자동으로 해결한다고 본 것이다.
- 2022 odd-lot/tender 아이디어는 사업분석보다 거래구조를 산 것이므로 별도 이벤트 수익으로 봐야 한다.

## ADT RECAP
RMR은 좋은 출발점이지만 `RMR / EV`만으로는 부족하다. recurring revenue가 있어도 subscriber acquisition을 계속 자본화하고 부채가 높다면 equity는 매우 민감하다. 실제 투자판정은 business quality와 capital structure를 따로 해야 한다.

---

# 3. Activision Blizzard — IP portfolio와 governance를 분리

게임회사의 자산은 공장보다 IP, 개발인력, 커뮤니티다. Call of Duty, Warcraft, Diablo, Candy Crush 같은 프랜차이즈는 매년 새 콘텐츠를 붙여 높은 ROIC를 만들 수 있지만, 작품 실패와 조직문화·인재유출이 동시에 발생하면 가치가 빠르게 훼손될 수 있다.

## 돈의 흐름
게임 판매·DLC·microtransaction·subscription·mobile IAP → platform fee와 개발·마케팅 차감 → IP별 현금흐름. 강한 IP는 반복 수익이 가능하지만 hit-driven risk는 남는다.

## 주요 아이디어 해석
- 초기 Long들은 단일 타이틀이 아니라 portfolio IP의 재사용성을 본 것이 강점이었다.
- 2019 Long은 Blizzard 우려가 극단적으로 반영됐을 때 Call of Duty·King까지 함께 싸게 산 구조였다.
- 2019 Short는 engagement 약화와 개발조직 문제를 봤지만, 포트폴리오 전체의 현금창출과 balance sheet를 충분히 할인하지 않았다.
- 2021 고가 Long은 IP quality를 맞혔어도 governance·문화 리스크가 valuation multiple을 훼손할 수 있음을 과소평가했다.
- 2022 Microsoft merger arb는 ATVI 사업가치가 아니라 `거래종결확률 × deal spread - break risk` 문제다. 장기 IP thesis와 합치면 안 된다.

## ATVI RECAP
좋은 IP portfolio는 강한 moat지만 governance가 discount rate를 올릴 수 있다. 이벤트 투자에서는 standalone value와 deal probability를 완전히 분리해야 한다.

---

# 4. Alibaba — SOTP와 실제 주주청구권의 차이

Alibaba는 중국 전자상거래, 클라우드, 물류, 국제커머스, 로컬서비스, 지분투자를 가진 복합 플랫폼이다. SOTP는 각 사업가치를 더하는 방식이지만, 중국 ADR 투자자는 해당 영업자산을 직접 소유하지 않고 VIE 계약구조를 통해 경제적 이익을 받는다는 점이 중요하다.

## 핵심 용어
- **VIE**: 외국인 투자 제한 산업에서 offshore 상장회사가 중국 운영회사와 계약을 맺어 경제적 이익을 연결하는 구조. 법적 직접지분과 경제적 노출이 다르다.
- **SOTP**: 각 사업부/지분자산 가치를 따로 평가한 뒤 순부채 등을 조정해 합산하는 방식.

## 아이디어별 반복 오류
- 2021 Long들은 core commerce와 cloud, Ant, Cainiao 등을 더해 큰 할인율을 계산했다. 사업가치 자체는 상당했지만 규제·정책·VIE·capital allocation 때문에 **그 가치가 ADR 주주에게 언제 어떤 형태로 귀속될지**를 충분히 할인하지 않았다.
- buyback과 사업분할 계획은 분명 catalyst였지만, 정책환경 변화가 multiple과 실현확률을 동시에 낮췄다.
- 2022-10 tactical Long은 가격이 훨씬 낮고 pessimism이 극단적이어서 risk/reward가 좋아졌다. 같은 회사라도 valuation과 policy path가 달라진 다른 투자다.

## Alibaba RECAP
SOTP discount가 크다는 것만으로 싸다고 단정하지 않는다. `사업가치 × 주주귀속확률 × 실현시점 할인`이 필요하다. 중국 플랫폼은 operating thesis와 policy/legal claim thesis를 별도 모듈로 본다.

---

# 5. 통합 Postmortem

1. **Netflix:** 현재의 낮은 FCF를 terminal economics로 고정하면 혁신 옵션을 놓칠 수 있다.
2. **ADT:** 반복매출도 CAC와 레버리지를 빼면 전혀 다른 equity가 된다.
3. **ATVI:** 좋은 IP와 좋은 governance는 별개다.
4. **Alibaba:** SOTP와 실제 주주청구권은 별개다.
5. **모든 아이디어 공통:** 가격이 맞아도 실제 성공 원인이 원 논지와 다르면 `인과 부분실패`로 기록한다.

각 아이디어 최종판정은 `Business / Valuation / Catalyst / Timing / Capital structure or claim / Security selection / 실제 투자결과` 7개 축으로 남긴다.