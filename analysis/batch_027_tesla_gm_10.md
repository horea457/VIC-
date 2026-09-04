# Batch 027 — Tesla · General Motors 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Tesla 7건 · General Motors 3건

## 결론부터

이번 배치는 자동차 투자에서 가장 자주 섞이는 세 질문을 분리한다. **회사가 살아남는가, 생산을 scale할 수 있는가, 그리고 그 성공이 현재 주가에 이미 얼마나 반영돼 있는가.**

Tesla의 2012·2016 Short는 당시 유동성·생산 ramp·자본조달 위험을 실제로 포착했지만 이를 곧바로 파산 확률과 equity zero에 연결했다. 2012년 말 Tesla는 Model S 약 2,650대를 인도했지만 이미 연환산 2만대 생산 run-rate에 도달했고, 2013년에는 22,477대의 Model S를 인도했다. 2016년 Model 3 공개 후 2016-05-15 기준 순예약은 약 373,000건이었다. 결국 2019년 Tesla는 367,656대, 2021년에는 매출 $53.8bn을 기록하면서 생존·대량생산 논쟁은 사실상 끝났다. 반면 2021년 Short는 ‘사업 실패’보다 **valuation duration**을 공격했다는 점에서 앞선 Short들과 구분해야 한다.

GM은 반대 방향의 좋은 교재다. 2009년 Old GM common은 실제 bankruptcy에서 소멸해 Short/short-call 논지가 맞았다. 그러나 2010 IPO 이후의 New GM은 부채와 고정비를 크게 줄인 다른 기업이었다. 2011·2013 Long은 ‘Old GM의 기억 때문에 New GM도 같은 multiple을 받는다’는 orphan-stock 논리를 사용했다. 2013 Long의 1년 성과는 약 +35%, 3년은 약 +19%, 5년은 약 +82%로 사업 정상화는 상당부분 맞았지만 자동차 OEM 특유의 낮은 장기 multiple은 완전히 사라지지 않았다.

> **방향 교정:** 원 SQL은 Tesla 7건과 GM 3건 모두 `is_short=true`다. 본문상 실제 방향은 Tesla 2012 Short, 2016 Short, 2018 Long, 2019-03 Short, 2019-08 Long, 2019-11 시장중립 short-volatility, 2021 Short. GM은 2009 short-call, 2011 Long, 2013 Long이다. raw flag는 보존하고 연구방향만 교정한다.

---

# TESLA INC (TSLA)

## 기업과 비즈니스

Tesla는 전기차를 설계·제조·직접판매하고, 차량 소프트웨어·충전 인프라·에너지저장·태양광을 함께 제공하는 vertically integrated EV/energy company다. 자동차 가치사슬에서 전통 OEM이 dealer network와 Tier-1 suppliers에 많이 의존하는 것과 달리 Tesla는 direct sales, 자체 software stack, OTA update, proprietary charging network와 battery/pack engineering을 묶었다. 이 구조는 높은 초기 CapEx와 execution risk를 요구하지만, scale에 성공하면 software-like 기능 판매와 직접 customer relationship을 통해 전통 OEM보다 높은 gross-profit pool을 만들 수 있다.

Tesla를 분석할 때 핵심 KPI는 단순 ‘EV 수요’가 아니다. **① 차량 생산·인도량, ② automotive gross margin ex-credits, ③ unit당 CapEx와 working capital, ④ cash/FCL과 증자 필요성, ⑤ 공장별 capacity utilization, ⑥ 가격인하 후 demand elasticity, ⑦ FSD/서비스의 실제 monetization**을 봐야 한다. 2012년 말 Model S 생산은 3,100대 이상, 인도는 약 2,650대였고 회사는 12월에 연환산 2만대 run-rate를 달성했다고 공시했다. 2019년 총 인도는 367,656대까지 늘었고, 2021년 매출은 $53.8bn으로 증가했다. 따라서 2012~19의 핵심 쟁점은 ‘전기차가 가능한가’보다 ‘Tesla가 자본을 조달하며 생산 learning curve를 통과할 수 있는가’였다.

## 1. 2012-11-30 — hawkeye901 — Short: “clean-tech bankruptcy analogue”

### 원 논지
Tesla를 A123, Ener1 등 당시 파산한 clean-tech 기업들과 같은 범주로 보고 Model S ramp가 지연되고 현금이 부족해 추가자본을 구하기 어렵다고 주장했다. 고정비가 큰 자동차 제조업에서 생산차질은 즉시 gross margin·cash burn으로 이어지므로 파산 또는 대규모 희석 가능성이 핵심이었다.

### 당시 숫자와 반증조건
2012년 9월 Tesla는 Model S 인도가 목표보다 4~5주 늦다고 인정했고 9월 23일까지 고객 인도는 132대에 불과했다. Short가 성립하려면 생산량이 계속 낮고 reservation이 취소되며 외부자금 조달이 막혀야 했다. 반증은 반대로 **주당 생산량이 빠르게 올라 2013년 2만대 수준을 감당하고 gross margin이 개선되는 것**이었다.

### 실제
연말 3,100대 이상 생산·2,650대 인도, 12월 3주 연속 주당 400대 이상 생산으로 2만대 run-rate를 달성했다. 2013년 인도는 22,477대로 올라갔다. 파산 thesis는 매우 빠르게 반증됐다.

### 판정
**치명적 실패.** liquidity risk는 실재했지만 ‘어려운 ramp’와 ‘ramp 불가능’을 구분하지 못했다. 제조업 Short에서는 생산속도의 1차미분이 개선되는지 봐야 한다.

## 2. 2016-06-23 — fogle42 — Short: Model 3/SolarCity execution overload

Model X ramp가 어렵고 Model 3의 2018년 50만대 build plan이 지나치게 공격적이며 SolarCity 인수가 또 하나의 자본부담을 더한다고 봤다. 당시 Model 3 순예약은 약 373,000건이었고 회사는 2018년 50만대 계획을 앞당긴 상태였다. Short의 핵심은 ‘수요가 없다’가 아니라 **수요를 감당할 제조·재무 capacity가 없다**였다.

실제로 Model 3 ‘production hell’과 2017~18 현금압박은 컸다. 그러나 2018년 Tesla는 Model 3 volume ramp를 통과했고 2019년 36.8만대 인도까지 올라갔다. SolarCity는 기대했던 성장자산이 되지 못했으나 자동차 business의 생존을 막지도 못했다.

**판정: 부분적으로 좋은 process, 증권방향은 실패.** execution risk를 정확히 잡았지만 그 위험을 permanent failure로 자본화했다.

## 3. 2018-01-23 — YCOMBINATOR — Long: optionality와 capital-market reflexivity

원 SQL은 Short지만 본문은 명백한 Long이다. 작성자는 Tesla가 비싸고 현금을 태우는 점을 인정하면서도 Model 3가 대중시장 EV category를 만들고 brand·battery·software·Supercharger·자본시장 접근성이 기존 OEM보다 훨씬 큰 option value를 준다고 봤다. 중요한 통찰은 Tesla가 ‘현재 EBITDA를 사는 종목’이 아니라 **미래 생산량과 신규 사업에 대한 장기 call option 묶음**이라는 점이었다.

실제로 2018년 Model 3 생산이 scale됐고 2019년 367,656대 인도, 2021년 $53.8bn 매출로 기업가치는 크게 증가했다. 다만 이 분석은 높은 valuation이 언제든 큰 drawdown을 만들 수 있다는 점을 충분히 분리하지 못했다.

**판정: 사업논지 매우 성공.** 장기적으로 브랜드와 scale을 잘 봤지만 security return은 entry multiple에 민감했다.

## 4. 2019-03-17 — jcoviedo — Short: demand cliff·cash raise·service weakness

Model 3 tax-credit phaseout, 가격인하, store closure 혼선, service 문제와 Shanghai/Model Y에 필요한 CapEx를 근거로 2019년 수요·현금흐름이 크게 악화될 것이라고 봤다. 작성자는 증자 가능성이 크고 narrative가 깨지면 valuation이 급격히 내려갈 것으로 예상했다.

Tesla는 실제로 2019년 초 demand/price 우려와 증자를 겪었지만 연간 인도는 사상 최대 367,656대가 됐다. Shanghai factory가 예상보다 빠르게 가동되면서 오히려 다음 성장단계가 열렸다.

**판정: 단기 지표 포착·구조적 Short 실패.** 가격인하를 무조건 demand weakness로 읽기보다 capacity expansion과 market-penetration 전략을 함께 봐야 했다.

## 5. 2019-08-03 — veki282 — Long: 2018 mass-production proof와 EV transition

작성자는 과거 Tesla skeptics였지만 2018년 Model 3 mass-production 성공을 보고 입장을 바꿨다. 장기 EV penetration, Tesla brand, vertically integrated software와 autonomous optionality를 핵심으로 제시했다. Robotaxi는 valuation에 넣지 않으면서도 추가 option으로 봤다.

2019~21 차량판매와 이익은 급증해 ‘Tesla도 자동차를 대량생산할 수 있다’는 핵심은 정확했다. 반면 autonomous/robotaxi timeline은 지나치게 빠른 기대가 반복됐다.

**판정: 핵심 사업논지 강한 성공, autonomy timing 과대.**

## 6. 2019-11-17 — carbone959 — Market-neutral: expensive-volatility 판매

이 아이디어는 방향성 Long/Short가 아니다. 작성자는 bull과 bear 모두 강한 신념을 갖고 있어 TSLA option implied volatility가 구조적으로 비싸다고 보고, 적절한 strike/expiry의 puts와 calls를 opportunistically 매도하는 전략을 제안했다. 핵심 assumption은 주가가 장기간 일정 범위에서 머물며 realized volatility가 implied보다 낮다는 것이었다.

2020~21 Tesla는 역사적인 방향성 rally와 극단적 realized volatility를 보였다. naked short-vol 전략이라면 tail loss가 매우 컸을 수 있다. ‘논쟁이 심해서 option이 비싸다’는 관찰만으로 variance risk premium이 충분하다고 결론내리는 것은 위험하다.

**판정: 구조적 실패 가능성이 큰 전략.** volatility selling은 회사분석보다 position sizing·convexity·gap risk가 핵심이다.

## 7. 2021-01-11 — bowd57 — Short: bubble/market-share-of-equity valuation

Tesla가 미국 주식시장 시가총액의 약 1.7%까지 커진 상태에서 1% 규모의 소형 Short와 매우 넓은 stop을 제안했다. 앞선 Short와 달리 회사가 파산한다는 주장이 아니라 **성공을 너무 많이 선반영한 valuation bubble**이라는 논리였다.

이후 Tesla는 사업적으로 더 성장했고 2021 매출 $53.8bn을 기록했다. 주가는 2022년에 큰 폭 하락했으나 2023에 다시 회복했다. 따라서 valuation Short의 timing/holding period에 따라 결과가 달라진다.

**판정: 사업 Short는 실패, valuation 경고는 부분 적중.** 좋은 기업도 duration이 길면 할인율과 기대치 변화에 매우 민감하다.

### Tesla 공통 학습

- ‘현금이 부족하다’는 사실만으로 파산을 주장하지 않는다. **향후 12~24개월 외부자본 접근성과 생산 learning curve**를 함께 본다.
- 생산계획 미달은 수준보다 변화율이 중요하다. 132대 인도라는 정적 숫자보다 주당 생산량이 100→200→400대로 상승하는지가 더 중요했다.
- 가격인하는 demand failure일 수도 있고 scale/penetration 전략일 수도 있다. gross margin·order backlog·capacity를 함께 본다.
- optionality는 0으로 둘 수 있지만, 반대로 무한한 premium을 주어서도 안 된다.
- valuation Short는 business Short와 다른 thesis다. 반증조건도 다르게 저장해야 한다.

---

# GENERAL MOTORS (GM)

## 기업과 비즈니스

GM은 Chevrolet, GMC, Cadillac, Buick 등을 통해 차량을 설계·제조·판매하고 GM Financial로 자동차금융을 제공한다. 자동차 OEM의 수익은 단순 판매대수보다 mix, incentive, warranty, labor/fixed-cost absorption과 금융손익에 좌우된다. 특히 pickup·large SUV는 passenger car보다 훨씬 높은 unit profit을 만드는 경향이 있어 북미 truck franchise가 GM의 핵심 cash engine이었다.

Old GM과 New GM은 반드시 구분해야 한다. 2009 bankruptcy에서 기존 common equity는 사실상 소멸했고 많은 부채·노동비용이 재구조화됐다. 2010년 IPO한 New GM은 더 낮은 leverage와 고정비 구조를 가졌다. 2023년 GM은 매출 $171.8bn, stockholder net income $10.1bn, adjusted EBIT $12.4bn, automotive operating cash flow $20.8bn을 기록했다.

## 8. 2009-04-27 — nha855 — Short Jan-2011 $2.50 calls

작성자는 당시 $2.04의 Old GM common이 debt-for-equity swap 후 신설회사의 약 1%만 받는다고 가정했다. $2.50에서는 pro-forma equity value가 비현실적으로 커지므로 Jan-2011 $2.50 call을 $0.55에 매도하자는 아이디어였다.

2009 bankruptcy에서 old GM equity는 소멸했고 ‘현재 common이 new GM의 경제적 지분을 그대로 보유한다’는 시장착시는 실제로 깨졌다. 다만 옵션 매도는 bankruptcy 처리와 contract adjustment를 정확히 이해해야 하는 event-driven trade였다.

**판정: 강한 성공.** capital structure가 바뀌는 distress에서는 EV보다 **어떤 법인이 어떤 security를 발행하는지**가 우선이다.

## 9. 2011-02-17 — Ragnar0307 — Long New GM

New GM이 bankruptcy를 통해 부채·고정비를 줄였고 net-cash에 가까운 balance sheet, 북미 break-even 개선, BRIC/중국 exposure를 갖췄는데도 투자자들이 Old GM의 기억 때문에 낮은 multiple을 준다고 봤다.

SQL 성과는 1년 약 -25%, 2년 -24%, 3년 거의 보합, 5년 약 -16% 수준이다. 회사는 생존하고 현금흐름을 냈지만 유럽 손실, cycle, pension/legacy concerns와 낮은 OEM multiple 때문에 rerating이 늦었다.

**판정: 기업재무 개선은 적중, 증권수익률은 실패.** ‘파산으로 부채가 줄었다’와 ‘높은 ROIC compounder가 됐다’는 같은 말이 아니다.

## 10. 2013-02-25 — Dogstar — Long at $26.71, 6-up/1-down

New GM이 trough에서도 FCF를 만들고, union/fixed-cost restructuring, product launch, GM Financial 확대, emerging-market 성장과 Treasury overhang 해소로 2~3년 내 2~3배 가능하다고 봤다. 당시 미국정부의 지분매각/회사의 Treasury share repurchase는 forced-seller overhang을 줄이는 catalyst였다.

SQL 성과는 1년 +34.6%, 2년 +46.1%, 3년 +18.6%, 5년 +82.4%로 장기적으로 유의미한 성공이었다. 다만 GM은 이후에도 cyclical OEM multiple을 벗어나지 못했고 EV 전환에 다시 막대한 CapEx가 필요했다.

**판정: 성공.** restructuring 이후 투자에서는 ‘예전보다 좋아졌다’보다 **새 break-even volume, normalized FCF와 자본환원**을 숫자로 연결한 점이 좋았다.

### GM 공통 학습

1. Distress 전후의 동일 ticker는 동일 기업이 아닐 수 있다.
2. bankruptcy로 debt가 사라진 뒤에도 산업 ROIC와 cyclicality는 남는다.
3. 정부/대주주 overhang 해소는 catalyst지만 그 자체가 장기 moat를 만들지는 않는다.
4. 자동차 OEM은 EV/EBITDA보다 pension, finance arm, captive cash와 working capital을 함께 본다.
5. pickup/SUV mix처럼 사업 내부 profit pool을 분리하면 consolidated multiple보다 더 정확한 valuation이 가능하다.

---

# Batch 027 재사용 프레임워크

**생존성**: 현금 + committed liquidity + 향후 24개월 FCF - mandatory CapEx - debt maturities.

**생산 scale**: 월별/분기별 생산량, yield, unit cost, fixed-cost absorption, supplier bottleneck을 별도 claim으로 저장한다.

**수요**: reservation/order가 실제 delivery로 전환되는 비율과 가격인하 후 gross margin을 같이 본다.

**valuation**: 성공 확률과 성공 시 terminal economics를 곱하되, 성공 자체가 이미 price에 반영됐는지 분리한다.

**Short process**: business failure, valuation compression, volatility-selling은 서로 다른 거래다. 동일한 ticker라는 이유로 한 thesis처럼 섞지 않는다.

## 주요 1차자료

- Tesla 2012 Form 10-K: https://www.sec.gov/Archives/edgar/data/1318605/000119312513096241/d452995d10k.htm
- Tesla 2016 Model 3 reservation disclosure: https://www.sec.gov/Archives/edgar/data/1318605/000119312516596657/d185970d424b5.htm
- Tesla 2019 Form 10-K: https://www.sec.gov/Archives/edgar/data/1318605/000156459020004475/tsla-10k_20191231.htm
- Tesla 2021 Form 10-K: https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm
- GM 2023 full-year release: https://www.sec.gov/Archives/edgar/data/1467858/000146785824000029/a2023q4pressreleaseandfina.htm
- 각 VIC 원문은 user-supplied `VIC_IDEAS(2).sql`의 description/catalyst를 기준으로 복원했다.
