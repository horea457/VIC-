# Batch 003 — American Express (AXP), 금융위기 전후 3개 롱

평가기준일: 각 글의 명시·암시 보유기간과 최대 5년 성과, 장기사업 확인은 2024-01-31  
분석일: 2026-09-03  
대상 VIC 아이디어: 2007-04-01 Long, 2008-06-12 Long, 2008-12-31 Long

## 결론부터

| VIC 아이디어 | 실제 방향 | 원래 기대 | 실제 가격 경로 | 종합판정 |
|---|---:|---|---|---:|
| 2007-04-01 | Long | EPS 성장·18x 적용, 목표 $68 | 1년 -21.7%, 2년 -75.6%, 5년 +5.2% | 실패 |
| 2008-06-12 | Long | 3년 내 2배 이상 | 6개월 -47.9%, 1년 -43.7%, 3년 +8.4%, 5년 +77.0% | 대체로 실패 |
| 2008-12-31 | Long | $18→$45+, 18~24개월·연 30%+ | 1년 +109.6%, 2년 +122.0%, 5년 +382.8% | 매우 성공 |

SQL에는 세 글 모두 `is_short=true`로 저장돼 있지만 원문은 모두 명백한 롱이다. 기존
가격성과도 숏 방향으로 부호가 붙어 있으므로 분석 레이어에서는 실제 롱 방향으로
교정했다.

세 글 모두 American Express의 동일한 장점을 봤다.

- affluent customer의 높은 지출
- issuer·network·merchant acquirer를 모두 가진 closed loop
- 높은 merchant discount rate
- 전자결제의 장기 성장
- 높은 ROE와 자본환원

그런데 결과는 완전히 달랐다. 핵심 차이는 사업품질을 누가 더 잘 설명했는지가 아니다.

> **2007년과 2008년 6월 글은 좋은 프랜차이즈가 신용손실·도매조달·유동화시장과
> 결합된 자본구조를 과소평가했다. 2008년 12월 글은 손실이 사라졌다고 본 것이 아니라,
> 은행지주회사 전환·정부자본·FDIC 보증·예금조달로 생존확률이 바뀐 뒤 가격이 $18까지
> 떨어졌다는 사실을 샀다.**

이 사례의 가장 중요한 교훈은 `좋은 기업을 사라`가 아니다. **좋은 기업도 자금조달과
신용손실 때문에 equity가 75% 하락할 수 있고, 같은 기업을 좋은 가격에 사는 것만으로도
부족하며 그 가격까지 살아남을 자본구조가 확인돼야 한다**는 것이다.

---

## 1. American Express는 무슨 기업인가

American Express를 Visa·Mastercard와 같은 결제 네트워크로만 보거나 Capital One과
같은 카드대출회사로만 보면 세 글의 오류를 이해할 수 없다. AXP는 두 모델을 한 회사
안에 결합한 `closed-loop spend-and-lend platform`이다.

### ① 카드회원 모집과 발급

AXP는 소비자·중소기업·법인에 직접 카드를 발급한다. 전통적인 charge card는 매월
잔액을 전액 결제하지만, 신용카드와 일부 상품은 잔액을 회전시키며 이자를 낸다.

주요 수익은 다음과 같다.

- 연회비와 각종 카드 수수료
- 카드대출 이자와 수수료
- 여행·서비스 수익

주요 비용은 rewards, 공항라운지·여행보험 등 cardmember services, 마케팅, 신용손실,
카드채권 조달비용이다.

### ② 결제 네트워크

카드가 사용되면 AXP 네트워크가 승인·정산·결제를 처리한다. Visa·Mastercard의 일반적
four-party 구조에서는 발급은행, merchant acquirer, network가 나뉘어 있다. AXP의
proprietary 거래에서는 AXP가 발급사이면서 네트워크이고 대부분의 경우 가맹점 관계도
직접 가진다.

그래서 거래 한 건에서 더 많은 정보를 확보하고 더 넓은 경제성을 가져간다. 반대로
신용손실, 사기, 결제대금 선지급과 조달, 가맹점 확대 비용도 직접 부담한다.

### ③ 가맹점 매입과 discount revenue

AXP는 가맹점으로부터 결제액의 일정 비율을 merchant discount로 받는다. 2006년 평균
discount rate는 약 2.55%였다. Visa·Mastercard 계열 카드보다 비싼 수수료를 받을 수
있었던 이유는 AXP 고객이 평균적으로 소득과 지출이 높아 가맹점에 가치 있는 고객이라는
주장이었다.

### ④ spend-centric flywheel

세 롱이 공통으로 본 선순환은 다음과 같다.

> 고소득·고지출 고객 모집
> → 카드당 지출 증가
> → 가맹점이 높은 discount rate를 감수
> → AXP가 rewards·서비스에 재투자
> → 고객 유지와 신규회원 확대
> → 더 많은 가맹점이 카드를 수용

이 선순환은 실제 경쟁우위였다. 다만 rewards와 partner payments가 수수료를 대부분
먹어버리지 않는지, 가맹점이 높은 수수료를 계속 받아들이는지는 별도 검증해야 한다.

### ⑤ Global Network Services(GNS)

AXP는 제3자 은행이 Amex 브랜드 카드를 발급하도록 네트워크를 개방했다. 이 경우 AXP는
직접 모든 신용위험을 지지 않고 network·processing 수수료를 얻는다. 2008년 6월 롱은
이 부분의 자본수익률이 90% 이상이며 순이익 비중이 2008년 1분기 26%에서 2011년 33%로
커질 것이라고 봤다.

다만 GNS billed business는 AXP가 merchant discount 전부를 가져가는 proprietary
거래보다 단위 매출이 낮다. 거래액이 늘어도 discount revenue 증가율이 더 낮을 수 있다.

### ⑥ 대출·receivable과 자금조달

AXP는 가맹점에 먼저 돈을 지급하고 카드회원에게 나중에 받는다. charge receivable은
짧은 기간의 reverse float이고, revolving balance는 실제 카드대출이다. 이를 장기·단기
부채, commercial paper, 카드채권 유동화와 예금으로 조달한다.

따라서 AXP에는 두 개의 엔진과 두 개의 위험이 동시에 있다.

| 엔진 | 좋은 시기 | 나쁜 시기 |
|---|---|---|
| Spend·network | 거래액·연회비·discount revenue 증가 | 소비둔화·여행감소·reward 부담 |
| Lending·funding | 이자수익과 높은 ROE | 연체·상각·충당금·조달경색 |

폐쇄형 네트워크는 강점이지만 네트워크와 대출을 법적으로 분리해 주지 않는다. 심한
불황에서는 카드사용 감소, 신용손실 증가와 조달경색이 동시에 발생한다.

---

# Part A. 2007년 4월 Long

## 2. 원래 투자 논지

2007년 글은 Ameriprise 분사 이후 AXP가 약 10% 조정받은 시점을 단기 진입기회로 봤다.
2006년 EPS $3.00 이상, 2007년 예상 $3.40, 2008년 예상 $3.80을 근거로 약 16.6x 당해,
15x 미만 다음 해 이익에 거래된다고 계산했다.

### 논지 ① 35% ROE와 두 자릿수 EPS 성장에 15~17x는 싸다

2006년 실제 ROE는 34.7%였고 2007년에는 37.3%까지 올라갔다. 당시까지의 회계실적은
원문을 강하게 지지했다. 2008년 예상 EPS $3.80에 18x를 적용한 목표가는 약 $68이었다.

### 논지 ② closed loop는 더 높은 가격과 더 많은 정보를 준다

AXP는 고객, 카드발급, 가맹점과 network를 모두 만지므로 거래정보와 관계를 통합하고
Visa·Mastercard보다 평균 1%p 이상 높은 merchant economics를 얻을 수 있다고 봤다.
2006년 discount rate 2.55%가 전년과 같다는 사실도 가격결정력의 증거로 사용했다.

### 논지 ③ 핵심 운영지표가 모두 좋다

2006년 billed business는 13% 증가했고 미국 cards-in-force는 43m에서 48.1m,
해외는 28m에서 29.9m으로 증가했다. 전자결제의 성장과 카드회원 확대가 두 자릿수
이익성장을 지속시킨다는 논리였다.

### 논지 ④ AXP는 전통 대출회사가 아니며 오히려 underlevered다

원문은 약 $50bn 대출과 $67bn 시가총액을 비교해 카드대출회사의 위험으로 볼 필요가
없다고 했다. 약 $11bn equity, $58bn 장·단기 부채를 적으면서도 자사주 매입을 위해
부채를 더 늘릴 수 있다고 평가했다.

이 부분이 가장 치명적인 오류였다. **loan book를 market cap과 비교하는 것은
손실흡수력을 측정하지 않는다.** 신용손실은 장부자기자본과 당기이익이 흡수하고,
단기부채와 유동화 만기는 조달접근성이 결정한다. 시가총액이 크다고 대출손실이 작아지는
것은 아니다.

## 3. 실제 결과

### 2007년 숫자는 좋았지만 이미 신용위험의 변화율이 악화됐다

2007년 EPS는 $3.40, ROE는 37.3%로 원문의 당해 예상과 거의 일치했다. 하지만 2007년
3분기까지 managed lending balance가 21% 증가한 가운데 provisions는 65% 증가했다.
강한 billed business와 EPS라는 수준값 아래에서 연체·상각과 충당금의 변화율이 더
빠르게 악화되고 있었다.

### 2008~2009년에는 spend와 lend가 동시에 꺾였다

2008년 순이익은 $2.7bn, EPS $2.33, ROE 22.3%로 하락했다. 2009년에는 순이익
$2.13bn, EPS $1.54, ROE 14.6%까지 낮아졌다. 2009년 worldwide billed business는
$619.8bn으로 9% 감소했고, managed card loans는 $61.8bn으로 14% 줄었으며 net
write-off rate는 8.4%까지 상승했다.

좋은 고객과 높은 수수료가 손실을 줄였지만, 회사 전체를 macro-neutral network로
만들지는 못했다.

### 가격결과는 단기 목표와 위험관리 모두 실패했다

원 가격계열상 1개월에는 9.2%, 6개월에는 6.3% 올랐지만 1년 -21.7%, 2년 -75.6%로
붕괴했다. 3년에도 -26.1%였고 5년에야 +5.2%로 원금 근처를 회복했다. 배당을 포함해도
목표 $68와 두 자릿수 연복리에는 크게 못 미친다.

### 2007년 최종 판정

**사업의 장기 경쟁우위는 맞았지만 투자로는 실패**다. 고ROE를 사업의 영구적 특성으로
보고 그 ROE를 만들던 대출성장·유동화·단기조달의 조건을 분리하지 않았다. 가장 위험한
시점에 “underlevered이므로 더 빌려 자사주를 사도 된다”고 판단한 것은 process 실패다.

---

# Part B. 2008년 6월 Long

## 4. 원래 투자 논지

이 글은 AXP가 현재가의 두 배 이상 가치가 있고 3년 내 주가가 두 배가 될 수 있다고
주장했다. 2008년 consensus EPS의 13.3x, 자체 2011년 추정치의 9.8x이며 적정 배수는
18~21x라고 봤다.

### 논지 ① spend-centric closed loop는 불황 뒤에도 살아남는다

고지출 고객이 가맹점에 높은 매출을 주고, 높은 merchant discount가 rewards와 서비스를
재원으로 제공한다. 발급·가맹점·network 데이터를 모두 보므로 가격·위험관리·마케팅을
정교하게 할 수 있다는 주장이다.

### 논지 ② merchant discount 하락은 미미하고 거래량이 상쇄한다

평균 discount rate는 약 2.5%에서 안정됐으며 Visa·Mastercard의 interchange도 오르고
있으므로 추가 하락은 작고 billed business 증가가 이를 상쇄한다고 봤다.

### 논지 ③ network·processing의 가치가 시장에 가려져 있다

GNS와 merchant acquiring이 90%+ return on capital을 내고 순이익 비중이 Q1 2008
26%에서 2011년 33%로 커진다고 예상했다. 이 부분에 25~30x, 나머지 lending에 낮은
배수를 적용해도 전체 적정 P/E가 18x 이상이라는 SOTP였다.

### 논지 ④ 신용·조달위험은 크지만 valuation이 충분히 보상한다

원문은 2007년 글보다 위험을 훨씬 명확히 적었다. 약 $80bn의 charge·credit card
loans, 향후 수년간 EPS $1~6의 신용손실 가능성, 유동화시장·무담보 조달 spread와
LIBOR-Fed Funds basis, $16bn 투자포트폴리오와 장기침체를 위험으로 열거했다.

문제는 위험을 발견하지 못한 것이 아니라 **동시에 발생할 때의 equity와 유동성 경로를
계산하지 않은 것**이다. credit loss $1~6라는 넓은 범위를 valuation에 확률가중하지
않고 정상 2011 EPS와 18~21x를 중심값으로 사용했다.

## 5. 실제 결과

### 2008년 예상이익이 먼저 무너졌다

실제 2008년 EPS는 $2.33이었다. 2007년 $3.40보다 31% 감소했고 ROE는 37.3%에서
22.3%로 내려갔다. 2008년 worldwide net write-off rate는 5.5%였고 순상각액은
$2.6bn으로 2007년 $1.6bn보다 크게 늘었다.

따라서 `13.3x 2008 consensus`는 확정된 싼 배수가 아니었다. 분모인 forward EPS가
하향되자 실제 지급배수와 안전마진이 달라졌다.

### network와 lending은 위기 때 분리되지 않았다

2009년 billed business가 9% 감소하고 카드대출 상각률이 8%대로 오르면서 discount
revenue·대출이익·조달이 동시에 압박받았다. GNS와 전자결제의 장기성장은 살아 있었지만
그 가치가 단기에 lending 손실과 유동성 discount를 상쇄하지 못했다.

### 3년 목표는 실패했지만 5년 사업복원은 성공했다

주가는 6개월 -47.9%, 1년 -43.7%였다. 2년에도 -10.7%였고, 명시한 3년 시점 가격수익은
+8.4%에 불과해 `3년 2배` 목표와 큰 차이가 났다. 그러나 5년에는 +77.0%까지 회복했다.

2010년 EPS는 $3.35, ROE 27.5%, billed business 증가율 15%로 정상화했고 2011년
EPS는 $4.09, billed business도 15% 늘었다. 프랜차이즈와 전자결제 성장 논지는 맞았지만
회복시점과 위기경로, 18~21x rerating을 지나치게 낙관했다.

### 2008년 6월 최종 판정

**사업논지는 대체로 성공, 투자결론은 대체로 실패**다. 5년을 견딘 투자자는 상당한
수익을 얻었지만 원문의 3년 2배와 drawdown 가정은 실패했다. 48% 손실을 견뎌야 하는
투자를 “현재가치의 절반 이하”라고만 표현하면 실제 자본관리와 다르다.

---

# Part C. 2008년 12월 Long

## 6. 원래 투자 논지

2008년 6월 글 이후 주가가 약 60% 하락한 $18에서 다시 제시된 롱이다. 이번 글은
사업품질보다 세 가지 불확실성의 가격과 생존확률을 중심으로 구성됐다.

1. 카드대출의 최종 신용손실
2. 부채·유동화의 차환과 조달비용
3. 소비지출 감소에 따른 단기 이익하락

원문은 이 불확실성이 사라졌다고 하지 않았다. 정부와 회사의 조치로 **going concern을
훼손할 최악의 시나리오 확률이 크게 낮아졌는데 시가총액은 약 $21bn으로 18개월 전의
3분의 1**이라고 봤다.

### 논지 ① $800m 비용절감과 가격인상이 손실을 일부 상쇄한다

인력 약 10% 감축과 투자축소로 2009년 $800m 이상 비용을 줄이고, fees·interest rate를
올려 신용손실과 조달비용을 일부 고객에게 전가한다는 논리였다.

### 논지 ② 정부자본이 신용손실 흡수력을 높인다

원문은 Treasury preferred 약 $3.39bn과 5% 배당, warrant를 반영했다. 실제 2009년
1월 거래는 $3.39bn Series A preferred와 주당 $20.95에 24.264m주를 살 수 있는
10년 warrant였다. 원문의 28.25m주 추정보다 실제 희석권리는 작았다.

### 논지 ③ 은행지주회사 전환이 조달 선택지를 넓힌다

AXP는 2008년 11월 14일 bank holding company가 돼 Federal Reserve 감독과 정부
프로그램 접근, 예금확대 가능성을 얻었다. FDIC 보증부 채권, Fed 유동성과 예금은
commercial paper·유동화시장 의존을 줄일 수 있었다.

실제 평균 customer deposits는 2008년 $13.6bn에서 2009년 $20.4bn으로 늘고,
연말 총예금은 약 $26.3bn에 도달했다. 자금조달 경로가 실제로 다변화됐다.

### 논지 ④ fee engine이 큰 손실도 흡수한다

2008년 첫 9개월 discount revenue 약 $11.5bn과 card fee $1.7bn을 강조했다. Q3에
$958m을 provision하고도 $815m 순이익을 냈기 때문에, 대출손실이 매우 커도 fee engine과
비용절감이 회사를 생존시킬 수 있다고 봤다.

### 논지 ⑤ 2011년 최소 EPS $3에 15x면 $45 이상이다

2009~2010년 이익은 낮아도 18~24개월 뒤 투자자는 정상화를 보기 시작하고, 2011년 최소
EPS $3 × 15x = $45 이상이라는 계산이었다. $18에서 연 30% 이상의 IRR을 예상했다.

## 7. 실제 결과와 인과 판정

### 신용손실은 예상대로 더 악화됐지만 회사는 생존했다

2009년 managed net write-off rate는 8.4~8.7%, owned basis는 8.5%로 올라갔다.
세계 billed business도 9% 감소했다. 즉 주가가 싸졌다고 영업충격이 끝난 것은 아니었다.

그럼에도 순이익 $2.13bn, EPS $1.54를 기록했고 자본과 유동성을 유지했다. 핵심은
손실 예측의 정밀성보다 손실을 흡수할 fee earnings·자본·조달선이 확보됐다는 것이었다.

### 생존안전판은 실제였고 예상보다 빨리 철회할 수 있었다

AXP는 2009년 1월 Treasury 자본을 수령한 뒤 같은 해 6월 preferred 전액을 상환하고
7월 warrant도 재매입했다. 2009년 4분기에는 billed business 성장률이 2008년 3분기
이후 처음으로 전년 대비 플러스로 돌아섰다.

정부지원은 영구적인 수익원이 아니라 시장이 재개될 때까지의 bridge였다. 투자자는
그 bridge를 통해 생존한 equity의 정상화 convexity를 샀다.

### 정상 EPS는 원문보다 높아졌다

2010년 EPS $3.35, ROE 27.5%, 2011년 EPS $4.09로 원문의 2011년 최소 $3를 웃돌았다.
2011년 worldwide billed business도 15% 증가했다. 회복의 이익방향과 franchise
지속성은 정확했다.

### 가격은 압도적으로 성공했다

초기에는 1개월 -13.5%, 3개월 -29.5% 추가 하락했다. 바닥을 정확히 맞힌 아이디어는
아니다. 그러나 6개월 +24.2%, 1년 +109.6%, 2년 +122.0%, 5년 +382.8%였다.

정확한 $45 도달이 18~24개월 안에 확실히 완료된 것은 아니지만, 실제 IRR은 원문이
요구한 연 30%를 크게 웃돌았다. 이 사례에서는 목표가 몇 달의 차이보다 자본생존과
비대칭 수익구조를 정확히 본 것이 더 중요하다.

### 2008년 12월 최종 판정

**매우 성공**이다. 좋은 기업을 싸게 샀다는 상투적 설명으로는 부족하다. 이전 두 글과
달리 이 글은 자산·부채·손익의 세 위험을 분리하고, 정부자본·FDIC 보증·은행지주 전환과
예금이 자본생존을 어떻게 바꾸는지 확인했다. 초기 30% 추가하락을 감수해야 했지만
확률가중 upside는 압도적이었다.

---

## 8. 세 아이디어의 주장별 비교

| 분석축 | 2007.04 Long | 2008.06 Long | 2008.12 Long |
|---|---|---|---|
| 사업품질 | 정확 | 정확 | 정확 |
| 신용위험 | 사실상 누락 | 명시했으나 범위만 제시 | 손실흡수력과 함께 분석 |
| 조달위험 | 부채를 더 늘릴 수 있다고 판단 | 유동화·spread 위험 인식 | BHC·TARP·FDIC·예금으로 bridge 확인 |
| forward EPS | $3.80 낙관 | 2008·2011 정상치 낙관 | 2009 악화 인정, 2011 $3 보수적 |
| valuation | 18x 단일 정상배수 | 18~21x·3년 2배 | $18에서 생존 후 15x |
| 최대 하락 | -75.6% | -47.9% | 진입 뒤 -29.5% |
| 5년 가격수익 | +5.2% | +77.0% | +382.8% |

## 9. 최초 반증 신호와 대응

### 2007 Long

2007년 3분기 managed lending balance가 21% 늘 때 provision이 65% 증가했다. EPS와
ROE가 좋아도 신용비용 변화율이 더 빨라진 첫 명확한 반증이었다. 자사주용 추가부채
논리를 폐기하고 대출 빈티지·write-off·유동화 만기를 다시 계산했어야 한다.

### 2008년 6월 Long

2008년 1분기 provision이 전년 대비 61% 증가했고 이후 조달시장이 더 경색됐다.
원문에 위험을 적어놓는 것만으로 충분하지 않다. EPS $1~6 손실범위를 확률가중하고,
funding closure와 동시 발생하는 stress equity value를 포지션 크기에 반영했어야 한다.

### 2008년 12월 Long

2009년 3월까지 주가가 약 30% 더 떨어지고 write-off가 계속 상승했지만, TARP 수령,
예금확대와 순이익 유지라는 핵심 생존조건은 훼손되지 않았다. 이 경우 가격하락은 원논지
반증이 아니라 예상한 스트레스 범위였다. 반증조건은 정부·예금 접근 상실, 자본비율 급락,
fee earnings가 provision을 흡수하지 못하는 상태였어야 한다.

## 10. 성공·실패 유형 태그

### 2007 Long

- `quality_at_wrong_price`
- `balance_sheet_blindness`
- `market_cap_vs_credit_error`
- `buyback_leverage_error`
- `level_vs_change_rate`

### 2008년 6월 Long

- `thesis_right_timing_wrong`
- `risk_list_without_quantification`
- `forward_eps_denominator_error`
- `network_lending_entanglement`
- `drawdown_underestimated`

### 2008년 12월 Long

- `distressed_quality`
- `capital_survival_verified`
- `policy_backstop`
- `funding_diversification`
- `normalization_convexity`
- `price_over_precision`

## 11. 재사용 가능한 투자 교훈

1. **고ROE를 경쟁우위와 레버리지로 분해한다.** AXP의 closed loop는 진짜 moat였지만
   대출·조달 leverage도 ROE에 기여했다.
2. **시가총액과 대출원금을 비교해 안전성을 판단하지 않는다.** 예상손실은 pre-provision
   earnings와 tangible common equity가 흡수하고 만기는 liquidity가 막는다.
3. **위험목록은 스트레스테스트가 아니다.** 2008년 6월 글은 모든 위험을 적었지만
   상관된 동시발생과 확률가중 equity value를 계산하지 않았다.
4. **forward P/E의 분모를 먼저 공격한다.** 경기민감 금융주의 낮은 P/E는 정상화 EPS가
   아니라 peak·stale estimate일 수 있다.
5. **네트워크와 대출의 경제성은 위기 때 분리되지 않는다.** proprietary closed loop의
   높은 수익은 신용·조달·가맹점 비용을 함께 부담한 대가다.
6. **distressed long은 바닥가격보다 생존 bridge가 먼저다.** 정부자본, 보증, 예금,
   만기와 비용절감이 시간이 필요한 정상화까지 회사를 연결하는지 확인한다.
7. **최대하락은 사후 부록이 아니라 논지의 일부다.** 2008년 12월의 성공도 진입 뒤
   약 30% 추가하락을 견딜 포지션 크기가 있어야 실현 가능했다.

---

## 12. 주요 근거

- [American Express 2006 Form 10-K — 카드수·billed business·사업구조](https://www.sec.gov/Archives/edgar/data/4962/000095012307003020/y30921e10vk.htm)
- [American Express 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/4962/000119312508042043/d10k.htm)
- [2007 Q3 Form 10-Q — lending balance와 provision 증가](https://www.sec.gov/Archives/edgar/data/4962/000110465907081852/a07-28534_110q.htm)
- [2008 Q1 Form 10-Q — provision 61% 증가](https://www.sec.gov/Archives/edgar/data/4962/000110465908029464/a08-11759_110q.htm)
- [American Express 2008 Form 10-K — 이익·ROE·BHC·TARP·write-off](https://www.sec.gov/Archives/edgar/data/4962/000119312509041008/d10k.htm)
- [American Express 2009 Form 10-K — 예금·TARP 상환·회복지표](https://www.sec.gov/Archives/edgar/data/4962/000119312510041232/d10k.htm)
- [American Express 2010 Form 10-K — EPS·ROE·신용정상화](https://www.sec.gov/Archives/edgar/data/4962/000095012311019072/y87970e10vk.htm)
- [American Express 2011 Earnings Release — EPS $4.09·billed business +15%](https://www.sec.gov/Archives/edgar/data/4962/000114036112003072/ex99_3.htm)
- [American Express 연차보고서 아카이브](https://ir.americanexpress.com/financials/annual-reports-and-proxy-statements/default.aspx)

### 데이터 해석 주의

- 원 SQL은 세 아이디어를 모두 숏으로 잘못 저장했다. 본문, 목표가와 촉매를 근거로 실제
  방향을 롱으로 교정했다.
- 가격수익률은 원 SQL의 조정가격 비율을 실제 롱 방향으로 읽은 값이며 배당은 별도다.
- 2007 글의 정확한 기준가는 원문에 없으므로 예상 EPS × P/E상 약 $56~57로 추정한다.
- 2008년 6월 글은 2008 consensus P/E 13.3x를 제시하지만 정확한 기준가는 원문에 없다.
  판정은 가격비율로 하므로 기준가 몇십 센트의 차이에 영향을 받지 않는다.
- 장기적으로 AXP 사업이 회복했다는 사실과 원문이 제시한 기간·수익목표 달성 여부를
  분리했다. 좋은 사업의 사후 생존이 위기 직전 진입을 자동으로 성공으로 바꾸지 않는다.
