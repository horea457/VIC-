# Batch 004 — American Express (AXP), Costco 이탈과 반독점 소송 3건

평가기준일: 각 글의 명시·암시 보유기간과 최대 5년 성과, 사업 확인은 2024-01-31  
분석일: 2026-09-03  
대상 VIC 아이디어: 2015-05-11 Long, 2016-07-05 Long, 2018-06-14 Short

## 결론부터

| VIC 아이디어 | 실제 방향 | 원래 기대 | 실제 가격 경로 | 종합판정 |
|---|---:|---|---|---:|
| 2015-05-11 | Long | Costco 충격 뒤 2017 성장 재개·multiple expansion | 1년 -16.6%, 2년 +3.0%, 3년 +34.8%, 5년 +17.0% | 부분 성공 |
| 2016-07-05 | Long | $59.15→$78~84, 중기 연 13%+ 총수익 | 6개월 +27.3%, 1년 +45.2%, 3년 +120.8%, 5년 +207.8% | 매우 성공 |
| 2018-06-14 | Short | 2개월 10% alpha·연말 20%, 기업가치 20~40% 훼손 | 3개월 -9.9%, 1년 -25.7%, 3년 -74.1%의 숏 가격손익 | 치명적 실패 |

SQL에는 세 글 모두 `is_short=true`로 저장돼 있다. 그러나 2015년과 2016년 글은 본문,
목표가와 보유공시가 모두 명백한 롱이다. 2018년 글만 실제 숏이다. 따라서 원본 방향은
보존하고 분석 레이어에서 앞의 두 건만 롱으로 교정했다.

세 글을 함께 보면 같은 회사의 좋은 사업을 알아보는 것보다 **언제, 어떤 확률구조로
매수·매도했는지**가 수익을 더 크게 결정했다.

> 2015년 롱은 Costco 손실 규모와 이익 reset이 완전히 드러나기 전에 14배를 싸다고
> 봤다. 2016년 롱은 실제 포트폴리오 매각과 고객전환이 끝난 뒤 같은 franchise를
> 10.6배에 샀다. 2018년 숏은 좋은 기업을 비싸게 판 것이 아니라 대법원 판결을 90%
> 확률로 예측했고, 그 단일 전제가 반대로 나오면서 후속 수수료 하락·손해배상 논리도
> 한꺼번에 0이 됐다.

이 배치의 재사용 가능한 결론은 세 가지다.

1. `좋은 기업 + 시장의 과잉반응`만으로는 진입시점을 정할 수 없다. 손익계산서에서
   사건의 기저효과가 끝나고 잔존사업 성장률이 확인되는 시점을 따로 봐야 한다.
2. 같은 논지라도 14배와 10.6배, 사건 전과 사건 후는 다른 투자다.
3. 법률 전문가의 권위, certiorari 통계와 구두변론 인상은 판결확률을 90%로 만드는
   충분조건이 아니다. 이진 촉매는 틀릴 때 후속 가치사슬 전체가 사라지는지부터 본다.

---

## 1. American Express는 무슨 기업인가

American Express는 카드 브랜드 하나가 아니라 카드발급, 대출, 결제 네트워크와 가맹점
매입을 한 회사에 결합한 `closed-loop payments and lending platform`이다. 이 구조가
Costco 제휴의 가치와 반독점 소송의 경제적 중요성을 동시에 설명한다.

### ① 카드 발급과 고객관계

AXP는 소비자·중소기업·대기업에 직접 charge card와 revolving credit card를 발급한다.
수익은 연회비, 카드대출 이자, 각종 수수료에서 나오고 비용은 rewards, 여행·라운지 등
서비스, 마케팅, 조달비와 신용손실이다.

전통 charge card는 매월 전액 결제하므로 대출잔액보다 결제액이 중요하다. 하지만 회사
전체에는 상당한 revolving loans도 있어 AXP를 순수 network로 보면 안 된다.

### ② closed-loop network와 가맹점 수익

Visa·Mastercard의 일반적 거래에서는 발급은행, network, merchant acquirer가 나뉜다.
AXP proprietary 거래에서는 AXP가 카드회원과 가맹점 모두와 직접 관계를 맺고 승인,
정산과 결제를 처리한다. 가맹점에는 결제액의 일정 비율인 merchant discount를 부과한다.

2016년 10-K는 closed loop가 거래 양쪽의 데이터를 제공해 underwriting, fraud control,
targeted marketing에 쓰인다고 설명했다. spend-centric 모델의 선순환은 다음과 같다.

> 고소득·고지출 회원 → 가맹점 매출가치 증가 → 높은 merchant discount 수취
> → rewards·서비스 재투자 → 회원 충성도와 지출 증가

하지만 이 선순환은 무료가 아니다. 더 높은 rewards, 공동브랜드 partner payment와
마케팅이 gross discount revenue를 소비한다. 따라서 billed business 성장만 보지 말고
discount revenue, contra-revenue와 고객획득비를 함께 봐야 한다.

### ③ 공동브랜드 카드가 만드는 집중위험

Costco, Delta, Starwood 같은 partner는 고객획득 채널이자 반복사용을 만드는 anchor다.
AXP는 카드발급과 network 수익을 동시에 얻지만 partner는 계약갱신 때 더 높은 보상과
더 낮은 economics를 요구할 수 있다. 네트워크 효과가 강해도 대형 partner가 입찰을 통해
그 지대를 가져갈 수 있다는 뜻이다.

Costco 관계는 약 16년 지속됐다. 2016년 VIC 글 기준 7m accounts, $76bn billings,
$12bn loans와 $3.1bn revenue로 각각 전체의 약 6%, 7%, 16%, 10%였다. 단순 고객 한 곳의
매출손실이 아니라 회원, 결제액과 loan book이 함께 이동하는 사건이었다.

### ④ Global Network Services와 OptBlue

GNS에서는 제3자 금융회사가 Amex 카드를 발급하고 신용위험과 운영비 일부를 부담한다.
AXP는 낮은 자본으로 network volume을 늘릴 수 있지만 proprietary 거래보다 단위매출이
낮다. OptBlue는 제3자 acquirer가 중소가맹점과 계약해 Amex acceptance gap을 줄이는
방식이다. acceptance가 늘면 카드가 더 유용해지지만 평균 discount rate에는 하방압력이
생길 수 있다.

### ⑤ 수익과 위험을 읽는 핵심 지표

| 지표 | 의미 | 잘못 읽기 쉬운 부분 |
|---|---|---|
| Billed business | 카드 네트워크를 통과한 지출 | GNS·mix가 늘면 매출이 같은 속도로 늘지 않음 |
| Discount revenue·rate | 가맹점 측 수익과 가격 | rewards·rebate 등 contra-revenue 차감 필요 |
| Cards-in-force·fee revenue | 고객기반과 구독성 수익 | 신규카드 bonus와 서비스비용이 먼저 발생 |
| Loans·NII | revolving lending 규모·수익 | provision·funding cost와 함께 봐야 함 |
| Partner concentration | 제휴 유지와 유입 채널 | 계약갱신 때 economics가 partner로 이동 가능 |
| Share count | 자본환원의 EPS 기여 | 영업이익 정체를 buyback이 가릴 수 있음 |

---

# Part A. 2015년 5월 Long

## 2. 원래 투자 논지

원문은 주가 $79.50, 약 14x P/E에서 AXP를 시장 21x보다 싼 고품질 회사로 봤다.
Costco·JetBlue 공동브랜드 이탈과 가맹점 steering을 허용한 1심 패소 때문에 주가가
52주 저점 부근으로 떨어졌지만 시장이 성장둔화에 과민반응했다고 주장했다.

### 논지 ① closed-loop와 affluent customer는 넓은 moat다

AXP 회원의 평균지출이 일반 카드회원의 3배 이상이므로 가맹점은 더 높은 수수료를
받아들인다. 높은 수수료를 더 좋은 rewards에 재투자하면 우량고객이 다시 유입되는
선순환이 유지된다는 논리다.

### 논지 ② Costco 포기는 자본배분 규율의 증거다

회사는 자본비용을 벌지 못하는 조건을 거절했고, 저수익 매출을 지키려고 경제성을
훼손하지 않았다는 해석이다. 원문은 Costco 손실로 2년가량 성장이 어렵다는 점을
인정하면서도 그 정체가 이미 14x에 반영됐다고 봤다.

### 논지 ③ steering의 실제 영향은 작다

가맹점이 더 싼 카드를 권할 수 있게 돼도 결제금액 차이는 최대 약 2%이고, 가장 많이
쓰는 고객을 불편하게 할 위험 때문에 실제 steering은 드물 것이라고 봤다.

### 논지 ④ 자본환원이 정체기를 메운다

직전 3년 현금흐름의 약 75%를 배당과 자사주로 돌렸고, 경영진도 의미 있는 주식을
보유했다. 2014년 $5.58에서 LTM $5.84로 EPS가 유지되고 발행주식수는 계속 감소해
매출정체 중에도 주당가치가 늘 수 있다는 주장이다.

### 촉매

명시적 촉매는 `2017년 성장이 다시 시작되고 multiple이 확대되는 것`이었다.

## 3. 실제 결과와 판정

### Costco의 회계·영업 충격은 생각보다 오래 숫자를 흐렸다

Costco 카드와 대출 포트폴리오는 2016년 중반 Citi로 이전됐다. 2016년 worldwide billed
business는 전년과 같았고 미국 billed business는 3% 감소했다. discount revenue는
Costco 관련 감소로 3% 줄었다. 2016년 diluted EPS $5.65에는 Costco loan·receivable
매각의 세전 $1.1bn 이익이 포함됐으므로 headline EPS만으로 잔존사업 성장을 확인하기
어려웠다.

이것이 2015년 글의 핵심 약점이다. Costco를 거절한 의사결정이 장기적으로 옳을 수 있어도
`언제 기존 회원·대출·merchant revenue를 대체하는가`는 별도 문제였다. 14x는 시장보다
낮았지만 earnings bridge가 불명확한 사건 전 multiple이었다.

### 2017년 성장 재개라는 촉매는 실제로 맞았다

2017년 full-year revenue net of interest expense는 $33.5bn으로 4% 늘었고, 전년 Costco
수익과 환율을 제외하면 8% 증가했다. Tax Act 일회성 영향을 제외한 EPS는 $5.87로 회사의
초기 $5.60~5.80 guidance를 웃돌았다. 4분기 cardmember spending은 11% 늘었다.

즉 `Costco 기저효과가 끝나면 franchise가 다시 성장한다`는 사업논지는 맞았다.
Costco 한 건이 network 전체를 파괴하지 않았고 새 카드·merchant·partner 투자가 성장을
되살렸다.

### 하지만 매수시점의 기회비용이 컸다

가격은 6개월 -6.5%, 1년 -16.6%였고 2년에도 +3.0%에 불과했다. 3년 +34.8%로 성장재개와
rerating을 반영했지만 5년 수익은 +17.0%였다. 5년 말이 코로나 충격 구간이라는 외생변수도
있으나, 원문이 강조한 장기 복리와 비교하면 진입시점의 안전마진은 충분하지 않았다.

### 2015년 최종 판정

**사업·촉매는 성공했고 가격경로는 부분 성공**이다. 2017 성장재개를 정확히 봤고 3년
수익도 양호했다. 그러나 Costco 경제성이 완전히 빠지기 전 14x를 시장 21x와 비교해
싸다고 한 것은 부족했다. 같은 논지를 14개월 뒤 10.6x에서 실행할 수 있었고 그 차이가
수익률을 크게 갈랐다.

---

# Part B. 2016년 7월 Long

## 4. 원래 투자 논지

이 글은 Costco 전환 직후 주가 $59.15, 회사가 제시한 2017 EPS $5.60 이상 기준 10.6x에서
AXP를 샀다. 적정가치는 2017 EPS의 14~15x인 $78~84, 현재가 대비 32~42% 높다고 봤다.

### 논지 ① Costco 손실은 forward estimate보다 더 반영됐다

Costco가 전체 revenue 10%, loans 16%로 컸다는 사실을 숨기지 않았다. 대신 고객과
대출의 실제 이전이 끝난 뒤 clean 2017 EPS 기준으로 가격을 잡았다. 2015년 글과 가장
다른 점은 `충격이 작다`가 아니라 `큰 충격을 반영한 새 분모가 나왔다`는 것이다.

### 논지 ② SYF 신용경고를 AXP에 그대로 적용하면 안 된다

Synchrony가 향후 charge-off 20~30bp 상승을 경고한 뒤 issuer 주가가 동반하락했다.
원문은 AXP가 lending만 하는 회사가 아니고 고객의 연체율도 더 낮다고 지적했다.
25bp 손실상승을 AXP의 $72.3bn loans·receivables에 적용해도 LTM pretax profit의 약
2.3%인데 주가는 3주간 7% 하락했다고 계산했다.

### 논지 ③ FX·유가를 제거하면 장기 결제성장은 살아 있다

당시 reported billed business 성장은 약 2%였지만 constant currency는 약 6%, 낮은
유가의 결제액 영향은 약 1%라고 봤다. 10년 worldwide billed business CAGR 7.9%,
constant-FX 8.3%를 근거로 전자결제의 구조적 성장이 지속된다고 주장했다.

### 논지 ④ 중기 EPS + 배당 13.1% algorithm

clean 2017 EPS $5.60을 출발점으로 card growth, pricing·mix, credit cost, 비용절감과
연 4.6% 정도의 buyback을 결합해 steady-state EPS growth 11.1%, dividend yield 2.0%,
총 13.1% 수익 알고리즘을 제시했다. $1bn 비용절감과 CCAR이 허용한 약 6% buyback은
추가 upside였다.

### 논지 ⑤ near-record bearishness가 해소된다

Costco, FX, 유가, SYF 신용우려가 모두 알려진 반면 sell-side 평가는 금융위기 이후 가장
약세에 가까워, 실제 잔존사업 성장률이 드러나면 upgrade cycle이 촉매가 된다고 봤다.

## 5. 실제 결과와 판정

### 목표가는 1년 안에 경제적으로 달성됐다

가격수익은 6개월 +27.3%, 1년 +45.2%였다. 원문의 $78~84 목표가가 요구한 32~42%
upside를 1년 수익률이 넘어섰다. 2년 +71.0%, 3년 +120.8%, 5년 +207.8%로 중기 결과도
강했다.

### 잔존사업 성장과 비용·자본환원 논리가 확인됐다

2016년 AXP는 $4.4bn의 자사주를 평균 $63.11에 매입했고 배당을 합쳐 그 해 생성자본의
약 99%를 주주에게 돌렸다. 2017년 Costco·FX 조정 revenue는 8% 증가하고 adjusted EPS는
$5.87이었다. 2018년 U.S. billed business는 10% 늘었고 diluted EPS는 $7.91,
Tax Act 관련 항목을 제외한 adjusted EPS는 $7.33으로 2017년 $5.89 대비 24% 증가했다.

즉 이익성장의 전부가 multiple expansion이나 buyback은 아니었다. 카드사용, loans,
fees와 잔존사업 revenue가 실제로 성장했다.

### 성공했지만 일부 표현은 과도했다

`AXP가 lending peer보다 덜 cyclical`이라는 비교는 합리적이었지만, 2020년 여행·오프라인
spend 붕괴에서 AXP 이익과 주가가 크게 흔들린 점을 보면 절대적 방어주라는 뜻은 아니다.
또 cobrand 경쟁은 Costco 한 번으로 끝나지 않는 구조적 협상위험이다. 성공한 투자에서도
이 표현을 영구 면제로 바꾸면 안 된다.

### 2016년 최종 판정

**논지, 촉매, valuation과 가격결과가 모두 맞은 매우 성공적인 롱**이다. 특히 알려진
악재를 단순히 무시하지 않고 실제 포트폴리오 이전 뒤의 clean EPS와 훨씬 낮은 가격으로
재설정한 것이 2015년 글보다 우수했다.

---

# Part C. 2018년 6월 Short

## 6. 원래 투자 논지

이 글은 `Ohio v. American Express` 대법원 판결을 2주 이내 촉매로 둔 special-situation
short다. 2개월 안에 시장대비 약 10%, 연말까지 20% 수익을 기대했고, 대법원이 90%
확률로 AXP에 불리하게 제2순회항소법원을 뒤집을 것이라고 봤다.

### 논지 ① anti-steering 조항은 경쟁을 막는다

AXP의 Non-Discrimination Provisions는 가맹점이 결제 시점에 고객에게 더 싼 카드를
권하거나 Amex 사용에 불리한 조건을 붙이는 행위를 제한했다. 원문은 이 조항이 높은
merchant discount를 보호하므로 제거되면 가맹점 수수료가 크게 낮아진다고 봤다.

### 논지 ② 대법원 reversal 확률은 90%다

근거는 1심의 상세한 사실인정, DOJ와 17개 주정부의 주장, Hovenkamp를 포함한 반독점
학자들의 amicus briefs, circuit split 없이 certiorari가 허가된 사건의 높은 reversal
비율, 구두변론에서 일부 대법관의 질문이었다. 가장 가능성 높은 표결을 정부 측 8대1로
예상했다.

### 논지 ③ 수수료 하락만으로 기업가치가 10~20% 줄어든다

2017 discount revenue $22.9bn 중 미국 몫을 약 $15bn으로 추정하고 rate가 10~40%
하락할 수 있다고 봤다. 20% 하락이면 revenue $3bn, 이론상 pretax profit 약 40% 감소로
계산했다. 카드수수료·혜택조정으로 일부를 회수해도 가치손실이 $10bn 이상이라는 논리다.

### 논지 ④ merchant 손해배상이 추가 10~20% 가치를 없앤다

정부가 최종 승소하면 merchant 소송에서 liability가 사실상 확정되고 12년 overcharge에
treble damages가 붙는다고 봤다. 이론상 $86.4bn에서 실제 청구 merchant 비중 50%,
settlement 50%, 시간가치를 차감해 약 $16bn의 현재가치 손실을 추정했다.

따라서 fee decline과 litigation liability를 합쳐 enterprise value가 20~40% 훼손된다는
구조였다.

## 7. 실제 결과와 판정

### 첫 촉매가 정확히 반대로 나왔다

2018년 6월 25일 대법원은 5대4로 제2순회항소법원을 **affirm**하고 AXP의 anti-steering
조항이 연방 반독점법을 위반하지 않는다고 판결했다. 다수의견은 신용카드를 강한 간접
네트워크효과가 있는 양면 transaction platform으로 보고 merchant 측만이 아니라 양쪽을
함께 평가해야 한다고 판단했다. 원고가 전체 거래가격 상승이나 거래량·품질 저하 같은
반경쟁 효과를 입증하지 못했다고 봤다.

Breyer 등 4명의 반대의견이 있었으므로 원 소송우려 자체가 터무니없었던 것은 아니다.
그러나 `가장 가능성 높은 8대1 패소`와 실제 `5대4 승소` 사이의 calibration gap은 매우
크다.

### 후속 손실 두 축이 동시에 사라졌다

판결 때문에 조항을 제거할 의무가 생기지 않았고, 정부 승소를 전제로 한 collateral
estoppel과 대규모 merchant damages 계산도 성립하지 않았다. 수수료 하락과 배상금은
독립된 두 위험이 아니라 **같은 법률판결에 조건부인 하나의 위험을 두 번 가치합산한 것**에
가까웠다.

### 사업 모멘텀은 숏의 시간을 더 불리하게 만들었다

2018년 U.S. billed business는 10% 증가했고 EPS는 $7.91이었다. 판결이 빗나간 뒤에도
강한 spend, loans, fee growth와 자본환원이 주가를 밀었다. 원 가격계열에서 주가는
1개월 +2.6%, 3개월 +9.9%, 6개월 +7.8%, 1년 +25.7%, 3년 +74.1%였다. 이를 단순
숏 가격손익으로 뒤집으면 각각 -2.6%, -9.9%, -7.8%, -25.7%, -74.1%이며 배당·대차비용을
반영하면 더 나쁘다.

### 왜 90%가 잘못됐나

1. **조건부 base rate 오류:** circuit split 없는 certiorari 사건의 reversal 빈도는 이
   사건의 법리, 대법관 성향과 양면시장 쟁점을 대체하지 않는다.
2. **권위의 투표화:** 유력 학자와 훌륭한 brief는 증거지만 각 대법관의 표가 아니다.
3. **구두변론 과해석:** 질문 강도와 판결방향을 일대일로 연결했고 중립적 질문을 유리하게
   읽었다.
4. **상관된 손실의 중복:** fee 하락과 damages는 첫 판결이 맞아야 함께 발생한다. 독립된
   downside처럼 더하면 기대손실을 부풀린다.
5. **반대 시나리오 부재:** AXP 승소 시 binary catalyst가 즉시 사라지고 강한 본업만 남는
   상황의 손실한도, 포지션 크기와 철수규칙이 부족했다.

### 2018년 최종 판정

**치명적 실패**다. 이 글은 merchant fee 의존성과 litigation tail을 구체적으로 계량한
점은 좋았지만, 가장 중요한 확률변수의 calibration이 틀렸다. 첫 노드가 실패하면 $3bn
수익감소와 $16bn 배상손실이라는 나머지 분석은 정교함과 무관하게 전부 비활성화된다.

---

## 8. 같은 기업에서 왜 결과가 달라졌나

| 비교축 | 2015 Long | 2016 Long | 2018 Short |
|---|---|---|---|
| 사건 단계 | Costco 이전 전·손익 불확실 | 실제 이전 직후·clean EPS 제시 | 대법원 판결 11일 전 |
| 가격·valuation | $79.50, 약 14x | $59.15, 2017E 10.6x | 좋은 본업 위 binary legal short |
| 핵심 확률 | 2017 성장재개 | 악재 반영·정상화 | AXP 패소 90% |
| 틀렸을 때 | 시간·기회비용 | valuation cushion 존재 | 촉매와 손실논리 전체 소멸 |
| 실제 결과 | 3년 성공·초기 부진 | 목표가 조기달성 | 판결 반대·주가 상승 |

2015년과 2016년은 thesis wording보다 **정보집합과 가격**이 달랐다. 2015년에는 Costco
매출·대출이 빠지는 방식과 대체투자비가 추정이었고, 2016년에는 매각이익, 잔존 balance와
2017 guidance가 있었다. 가격도 약 26% 낮아졌다.

2018년은 반대로 valuation이 부차적이었다. 판결을 맞히면 수익성 구조가 변하고 틀리면
본업 성장에 노출되는 촉매거래였다. 이런 거래는 기업가치 분석의 페이지 수보다 첫 분기점의
확률, payoff asymmetry와 포지션 크기가 중요하다.

## 9. 최초 반증·확인 신호

| 아이디어 | 사전에 볼 수 있던 신호 | 의미 |
|---|---|---|
| 2015 Long | Costco가 billed business 8%·loans 20% 안팎이라는 공시 | 14x가 단순 저평가인지 earnings reset인지 먼저 계산해야 함 |
| 2015 Long | 2016 billed business flat·discount revenue -3% | 대체성장이 아직 headline에 나타나지 않음 |
| 2016 Long | 2017 ex-Costco·FX revenue +8%, adjusted EPS $5.87 | clean EPS와 성장재개 확인, 논지 강화 |
| 2018 Short | 제2순회항소법원 승소와 양면시장 법리 | 90% 패소 확률에 큰 반대증거였음 |
| 2018 Short | 2018-06-25 5대4 affirm | 즉시 cover해야 하는 완전한 thesis break |

## 10. 학습 태그

### 2015 Long

- `quality_at_wrong_time`
- `partner_concentration`
- `earnings_reset`
- `relative_multiple_trap`
- `thesis_right_entry_early`

### 2016 Long

- `post_event_entry`
- `expectations_reset`
- `clean_eps_bridge`
- `capital_return`
- `known_bad_news_overdiscounted`

### 2018 Short

- `binary_catalyst`
- `probability_miscalibration`
- `base_rate_misuse`
- `expert_authority_bias`
- `conditional_loss_double_count`
- `catalyst_failure`
- `short_asymmetry`

## 11. 재사용 가능한 체크리스트

### 대형 partner 이탈 롱

1. accounts, billings, loans, revenue, profit 중 무엇이 얼마나 이동하는가?
2. portfolio sale gain을 제외한 clean EPS는 얼마인가?
3. 이탈 뒤 4~6개 분기의 기저효과와 대체 고객획득비를 반영했는가?
4. 계약거절이 정말 ROIC 규율인지, 경쟁력이 약해져 가격을 못 맞춘 것인지 구분했는가?
5. 시장 multiple이 아니라 reset EPS와 stress multiple로 가격을 비교했는가?

### 법률 이진촉매 숏

1. 각 판결 시나리오의 독립확률과 payoff는 무엇인가?
2. certiorari·전문가·구두변론 같은 proxy를 실제 vote count로 과대변환하지 않았는가?
3. 1차 판결이 틀리면 후속 손실항목들이 동시에 사라지는가?
4. 승소·지연 시 본업 성장과 시장상승이 숏에 주는 손실은 얼마인가?
5. 판결 당일 cover rule, 최대손실과 포지션 크기가 사전에 정해졌는가?

---

## 주요 근거

- [VIC 2015 AXP 원문](https://www.valueinvestorsclub.com/idea/American_Express_/9390945749) — 실제 롱, $79.50·14x, Costco·steering·자본환원 논지
- [VIC 2016 AXP 원문](https://www.valueinvestorsclub.com/idea/AMERICAN_EXPRESS_CO/5672439448) — 실제 롱, $59.15·2017E 10.6x, $78~84 목표와 EPS algorithm
- [VIC 2018 AXP 원문](https://www.valueinvestorsclub.com/idea/AMERICAN_EXPRESS_CO/2379749386) — 실제 숏, 대법원 패소 90%와 가치손실 산식
- [American Express 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/4962/000119312516469798/d131774d10k.htm) — Costco 집중도, 2015 실적과 사업구조
- [American Express 2016 Form 10-K](https://www.sec.gov/Archives/edgar/data/4962/000119312517047588/d321397d10k.htm) — closed loop, Costco 매각, billed business·discount revenue·EPS·자사주
- [American Express 2017 실적발표](https://ir.americanexpress.com/news/investor-relations-news/investor-relations-news-details/2018/American-Express-Reports-Quarterly-Revenues-Up-10-Percent-with-Record-Card-Member-Spending/default.aspx) — ex-Costco 성장과 adjusted EPS
- [American Express 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/4962/000000496219000018/axp201810k.htm) — 2018 billed business, EPS와 소송결과
- [Ohio v. American Express 대법원 판결](https://www.supremecourt.gov/Opinions/17pdf/16-1454_5h26.Pdf) — 5대4 affirm, 양면시장과 anti-steering 판단
- [American Express 연차보고서 아카이브](https://ir.americanexpress.com/financials/annual-reports-and-proxy-statements/default.aspx) — 연도별 교차검증
- VIC SQL `source_performance` — 각 아이디어 게시시점 이후 가격비율. 본 보고서는 본문에서 추론한 실제 방향으로 부호를 교정한 단순 가격수익률이며 배당·대차비용·benchmark alpha는 별도다.

