# Batch 005 — American Express (AXP), 팬데믹과 rewards 경쟁 3건

평가기준일: 2024-01-31, SQL 제공 성과는 최대 가용기간까지 별도 표시  
분석일: 2026-09-02  
대상 VIC 아이디어: 2020-02-16 Long, 2020-10-14 Long, 2022-05-31 Short

## 결론부터

| VIC 아이디어 | 실제 방향 | 핵심 투자 주장 | 실제 가격 경로 | 종합판정 |
|---|---:|---|---|---:|
| 2020-02-16 | Long | 15x의 고품질 복리기업, 이익수익률 7% + 순이익 성장 7% | 1개월 -36.1%, 1년 -1.9%, 2년 +50.2%, 3년 +38.5% | 부분 성공 |
| 2020-10-14 | Long | 생존위험이 사라진 약 $100의 AXP, 극단적으로 느린 회복도 반영 | 6개월 +42.2%, 1년 +66.1%, 2년 +34.2% | 매우 성공 |
| 2022-05-31 | Short | rewards 경쟁이 fee economics를 파괴해 AXP가 대출회사로 전락 | 숏 가격손익 1개월 +16.1%, 3개월 +6.4%, 6개월 +8.3%; 2024-01까지는 손실 전환 | 대체로 실패 |

SQL에는 세 글 모두 `is_short=true`로 저장돼 있다. 그러나 2020년 두 글은 본문,
가격과 보유공시가 모두 명백한 롱이고 2022년 글만 실제 숏이다. 원본 필드는 보존하고
분석 레이어에서 실제 방향을 따로 기록했다.

세 글은 같은 회사를 두고도 **좋은 기업이라는 판단, 좋은 가격, 나쁜 시나리오를 견디는
자본구조, 그리고 투자자가 실제로 버틸 수 있는 가격경로는 서로 다른 질문**임을 보여준다.

> 2020년 2월 롱은 AXP의 장기 사업품질을 대체로 맞혔지만 `robust`라는 표현과 14% 수익
> 알고리즘에 전례 없는 T&E 정지를 넣지 않았다. 2020년 10월 롱은 같은 품질론을 반복한
> 것이 아니라 실제 위기 손실·비용가변성·자본을 확인하고 2019년 실적을 2025년에야
> 회복하는 스트레스 시나리오를 샀다. 2022년 숏은 비용경쟁과 2021년 이익의 낮은 질을
> 정확히 봤지만, rewards를 매출과 고객가치를 만드는 투자에서 분리해 순수 누수로
> 계산하고 회계상 segment 잔여이익을 경제적 독립사업 가치로 오인했다.

재사용 가능한 결론은 다음과 같다.

1. 장기 compounder도 진입 직후 36% 하락할 수 있다. `장기적으로 맞음`과 `위험조정
   진입이 좋음`을 분리해야 한다.
2. 위기 뒤 매수는 단순 저가매수가 아니다. 생존성, 비용의 가변성, 신용손실과 회복기간을
   명시해도 수익이 나는지를 봐야 한다.
3. rewards·partner payment는 비용이면서 동시에 회원획득·유지와 결제액을 만드는
   상품원가다. gross fee에서 떼어내 비용만 독립적으로 외삽하면 양면 플랫폼의 경제성을
   잘못 읽을 수 있다.
4. 단기 주가방향 적중은 사업논지 적중과 다르다. 2022년 숏의 첫 6개월 이익은 금리상승과
   시장 multiple 압축 구간에서 발생했지만, 예측한 구조적 실적붕괴는 일어나지 않았다.

---

## 1. American Express는 무슨 기업인가

American Express는 Visa나 Mastercard처럼 결제망만 제공하는 회사도, Capital One처럼
카드대출을 중심으로 하는 은행도 아니다. 카드회원 모집·발급, 가맹점 계약·정산,
결제 network와 대출을 한 회사 안에 결합한 `closed-loop spend-and-lend platform`이다.

### ① 카드회원: 연회비와 반복사용

AXP는 소비자, 중소기업과 대기업에 charge card와 revolving credit card를 직접 발급한다.
Platinum·Gold 같은 상품은 연회비를 받고 라운지, 여행혜택, 포인트와 서비스를 제공한다.
연회비는 구독성에 가깝지만 무료이익은 아니다. 라운지 계약, 포인트, 보험·여행서비스와
가입보너스가 함께 증가한다. 중요한 것은 연회비 한 줄이 아니라 회원유지율, 회원당 지출,
서비스원가와 신규회원 생애가치의 조합이다.

### ② 가맹점·결제망: discount revenue

AXP proprietary 카드 사용액이 가맹점을 통과할 때 AXP는 merchant discount를 받는다.
일반적인 4-party 카드 구조와 달리 발급사와 network가 분리되지 않아 거래 양쪽의 데이터와
경제성을 더 많이 보유한다. 고지출 회원을 모으면 가맹점에 더 높은 구매력을 제공하고,
가맹점 수익을 rewards와 서비스에 재투자해 다시 회원과 지출을 늘리는 선순환이 가능하다.

평균 discount rate가 내려가도 결제액이 더 빨리 늘면 discount revenue는 증가할 수 있다.
반대로 결제액만 늘어도 rewards·partner rebates와 marketing이 더 빨리 증가하면 순이익은
늘지 않는다. 따라서 `billed business × take rate`만으로 가치를 계산하면 부족하다.

### ③ 대출과 예금: 높은 ROE의 다른 절반

charge card는 매월 결제하지만 AXP는 상당한 consumer·small-business revolving loans도
보유한다. 이자수익에서 예금·채권 조달비와 신용손실을 차감한 결과가 lending economics다.
2008년 이후 자체 예금기반을 키워 조달을 안정화했지만, 경기침체에서는 provision과
charge-off가 이익을 크게 흔든다. AXP를 순수 결제 network 배수로만 평가할 수 없는 이유다.

### ④ Customer engagement 비용은 비용이자 제품이다

2019년 원문은 rewards, card-member services, marketing과 business development를 합친
customer engagement 지출이 약 $20bn이라고 강조했다. 일부는 결제액에 연동하는 변동비이고,
일부는 partner 계약·라운지 같은 고정 또는 준고정비다. 경쟁이 심해지면 단위비용이 올라
margin을 압박한다. 그러나 이 지출은 동시에 fee-paying 신규회원, retention과 더 높은
spend를 산다. 2022년 숏처럼 이를 전부 `merchant fee의 누수`로 보면 고객획득 투자와
상품원가의 경제적 대가를 놓친다.

### ⑤ 팬데믹이 드러낸 민감도

AXP는 2019년까지 T&E 의존도를 낮췄지만 여행·외식과 corporate spend는 여전히 고수익
결제액의 중요한 부분이었다. 팬데믹은 세 경로를 동시에 타격했다.

- travel·entertainment 결제액과 높은 discount revenue 감소
- 항공·호텔 cobrand와 premium card의 즉시 효용 감소
- 실업·기업부실 우려에 따른 CECL provision 급증

반면 rewards 적립, 마케팅과 일부 운영비는 결제액과 함께 감소했고, 정부지원으로 실제
write-off는 초기 예상보다 낮았다. 2020년 10월 글은 바로 이 `매출 충격-비용 완충-신용손실-
자본생존`의 다리까지 분석했다.

### ⑥ 분석할 핵심 지표

| 지표 | 무엇을 보여주는가 | 반드시 함께 볼 것 |
|---|---|---|
| Billed business·T&E mix | network 사용량과 경기민감도 | discount rate, 지역·고객 mix |
| Discount revenue | 가맹점에서 얻는 gross economics | rewards·rebates·partner payments |
| Card fees·신규카드 | 구독성 수익과 franchise 성장 | acquisition cost, retention, engagement |
| Loans·NII | lending 성장과 spread | funding cost, provision, charge-off |
| Customer engagement expense | 경쟁강도와 고객투자 | 회원당 지출·수수료·생애가치 |
| CET1·capital return | 생존성과 주당가치 증가 | stress loss, 규제상 buyback 제한 |

---

# Part A. 2020년 2월 Long — 품질은 맞고 경로는 틀렸다

## 2. 원래 투자 논지

글은 AXP를 장기 포트폴리오의 `foundational brick`으로 제시했다. 주가 약 $135,
2020년 예상이익의 15배에서 AXP가 매출과 순이익을 중고단일 자릿수로 성장시키면서
증분자본이 적고 이익의 80% 이상을 주주에게 돌릴 수 있다고 봤다.

### 논지 ① 7% earnings yield + 7% 순이익 성장 = 14% 수익

핵심 valuation은 단순했다. 15배는 약 7% 이익수익률이고, 장기 순이익이 연 7% 성장하면
multiple 변화 없이도 중장기 기대수익이 약 14%라는 주장이다. Visa의 3% 미만 이익수익률과
11~12% 성장을 합친 결과와 비슷하지만, AXP는 현재현금흐름 비중이 높아 더 견고하고
20배로 rerating될 선택권도 있다고 봤다.

### 논지 ② 80% fee·20% lending의 우수한 혼합

AXP를 Mastercard/Visa와 premium Capital One의 혼합으로 설명했다. 수익의 약 80%가
swipe·membership fee, 20%가 lending에서 나온다고 보고 순수은행보다 높은 30%+ ROE와
더 낮은 자본집약도를 강조했다.

### 논지 ③ closed-loop·고지출 고객의 flywheel

2019년 proprietary AXP 고객의 연간 지출을 약 $20,000, 일반 Visa/Mastercard 고객을
약 $5,500로 비교했다. $1.2tn billed business, 미국 카드가맹점의 약 99% acceptance,
연 11.5m 신규카드 중 약 70% fee-based라는 수치를 근거로 고지출 고객-가맹점 가치-
rewards 재투자의 flywheel이 경쟁을 방어한다고 봤다.

### 논지 ④ 국제·SMB·lending의 장기 runway

국제 acceptance와 발급, 미국 SMB, 기존 우량회원의 대출점유율 확대가 장기 성장축이었다.
대출은 prime·super-prime 중심이고 예금이 조달의 절반 이상이며 Fed stress test에서도
강하므로 경기위험이 관리 가능하다고 판단했다.

### 논지 ⑤ 높은 자본환원

약 $1.6bn 배당과 $5.5bn buyback, 합계 $7bn 이상을 예로 들어 최소 이익의 80%를 계속
환원할 수 있다고 예상했다. 명시적 촉매는 없었고, `honey badger`처럼 시간이 복리를
만들어준다는 아이디어였다.

## 3. 실제 결과

### 게시 직후 전제가 동시에 깨졌다

글이 게시된 2020년 2월 중순은 코로나가 글로벌 여행·외식과 기업활동을 정지시키기
직전이었다. 주가는 1개월 -36.1%, 3개월 -34.4%, 6개월 -25.2%였다. 이는 단순 multiple
변동이 아니라 AXP의 고수익 T&E 지출, cobrand 가치와 신용비용이 동시에 악화되는
사업충격이었다.

2020년 full-year revenue net of interest expense는 $36.1bn으로 17% 감소하고 diluted
EPS는 $3.77로 2019년 $7.99의 절반 이하가 됐다. provision은 $4.7bn이었다. `T&E에서
충분히 다변화돼 robust하다`는 표현은 방향은 맞아도 tail sensitivity를 과소평가했다.

### 사업은 살아남았고 예상보다 빠르게 회복했다

2021년 revenue는 $42.38bn으로 17% 증가하고 EPS는 $10.02로 반등했다. 다만 provision이
$1.42bn benefit이었고 reserve release가 $2.5bn 포함돼 headline EPS의 질은 낮았다.
2022년 revenue는 25% 증가하고 EPS는 $9.85였다. reserve release가 사라진 뒤에도
사업이 유지됐다는 점은 closed-loop franchise와 회원투자 논리가 실재했음을 보여준다.

가격은 1년 -1.9%로 거의 원점, 2년 +50.2%, 3년 +38.5%였다. 3년 연환산 가격수익률은
약 11.5%로 원문의 14% algorithm보다 낮지만 장기 롱 방향은 맞았다. 그러나 중간 36%
하락과 1년 기회비용을 무시하면 사후편향이다.

## 4. 최종 판정

**사업품질은 성공, 투자경로는 실패, 장기 가격결과는 부분 성공**이다. 팬데믹 자체는 T0에
합리적으로 예측하기 어려운 외생충격이었다. 하지만 `robust`, fee 80%와 다변화를 강조하면서
T&E·cobrand·provision이 동시에 흔들릴 때의 earnings-at-risk를 수치화하지 않은 것은
분석과정의 약점이다. 15배가 절대적으로 싸다는 주장도 순이익이 절반이 되는 tail에서는
안전마진이 아니었다.

첫 반증신호는 2020년 3월 여행중단과 카드지출 급락이었다. 이때부터 2020E EPS와 14%
algorithm을 폐기하고 자본·유동성·신용손실 기반으로 재평가해야 했다. 결과적으로 계속
보유한 투자자는 수익을 냈지만, 그 성공은 원래의 매끄러운 복리경로가 아니라 생존 후
회복에 의존했다.

---

# Part B. 2020년 10월 Long — 같은 기업, 더 나은 가격과 명시적 스트레스

## 5. 원래 투자 논지

이 글은 2월 글을 직접 계승하면서도 약 $100에서 `생존이 확인된 뒤의 회복 옵션`을 샀다.
핵심은 2019년 실적이 곧 돌아온다는 낙관이 아니었다. 2020년 billed business -20%,
2021년에도 2019년보다 10% 낮고 2019년 수준을 2025년에야 회복한다고 가정해도 가격이
내재가치보다 싸다는 스트레스 논리였다.

### 논지 ① closed-loop의 장기 ROE는 훼손되지 않았다

15년 평균 ROE 약 27%, 2005~2019 billed business 약 $620bn에서 $1.24tn, cards-in-force
약 49m에서 114m라는 장기 기록을 근거로 코로나가 network의 구조적 경쟁력을 없애지는
않았다고 봤다. rewards·서비스비 비중 상승도 고객가치 투자로 해석했고 고정비 비중은
장기적으로 낮아졌다고 봤다.

### 논지 ② bear case 자체를 valuation에 넣었다

T&E가 proprietary spend의 약 29%, corporate·SMB와 airline/hotel cobrand 노출이 크다는
약점을 인정했다. 2019 실적 회복을 2025년까지 미루고 2022년 이후에야 추세성장을 넣었다.
기대회복이 느린데도 약 $100이 싸다면 투자논지는 특정 백신일정이나 V자 회복에 덜
의존한다.

### 논지 ③ 대손 스트레스와 자본생존

원문은 charge-off와 provision을 금융위기보다 더 나쁜 수준으로 스트레스했다. 당시 실제
write-off가 정부지원 때문에 거의 증가하지 않았다는 점, 우량고객 mix와 자본을 들어
존속위험이 낮아졌다고 판단했다. 2월 글의 품질 주장을 `얼마나 손실을 견딜 수 있는가`로
바꾼 것이 중요하다.

### 논지 ④ 비용은 매출보다 가변적이다

rewards 적립·사용, 마케팅과 partner payment가 결제액과 함께 줄고 회사가 약 $1bn의
operating expense 절감을 추진해 매출감소가 동일 비율의 영구이익 감소로 연결되지 않는다고
봤다. 여행 rewards의 미사용·이연도 단기 완충이었다.

### 논지 ⑤ 촉매가 아니라 비대칭성

명시적 촉매는 없었다. existential downside가 크게 줄어든 뒤 시장은 정상화에 오랜 시간이
걸리는 것으로 가격을 매겼고, 실제 회복이 조금만 빨라도 upside가 크다는 구조였다.

## 6. 실제 결과와 판정

회복은 원문의 보수적 가정보다 훨씬 빨랐다. 2021년 revenue $42.38bn은 이미 2019년
$43.55bn에 근접했고 EPS $10.02는 reserve release의 도움을 받았지만 2019년을 넘었다.
2022년 revenue +25%, EPS $9.85로 credit benefit 정상화 뒤에도 earnings power가
유지됐다.

주가는 1개월 +10.1%, 3개월 +16.9%, 6개월 +42.2%, 1년 +66.1%였다. 2년 +34.2%로 일부
반납했지만 원문이 요구한 중기 기대수익은 빠르게 달성됐다. 이 성공은 단순히 팬데믹 종식을
맞힌 것이 아니다. 원문은 2025년 회복이라는 느린 경로에서도 가치가 남도록 가격과 손실을
설계했고 실제 결과가 그보다 좋아졌다.

**논지·valuation·생존성·가격결과가 모두 맞은 매우 성공적인 롱**이다. 가장 좋은 부분은
`AXP는 좋은 회사`가 아니라 다음 네 항목을 분리한 점이다.

1. 매출·T&E가 얼마나 감소하는가
2. rewards와 운영비가 얼마나 함께 줄어드는가
3. 대손과 자본이 어느 정도까지 견디는가
4. 2019 실적회복을 2025년으로 늦춰도 현재가가 싼가

다만 2021 EPS $10.02의 $2.5bn reserve release를 정상 이익으로 그대로 사용하면 안 된다.
성공한 투자에서도 회복속도와 회계상 이익의 질은 분리해야 한다.

---

# Part C. 2022년 5월 Short — 비용압박은 맞았지만 사업의 연결고리를 끊어 계산했다

## 7. 원래 투자 논지

이 글은 AXP의 2021년 비이자수익에서 rewards, services, marketing과 partner payment를
차감한 자체 재구성 이익이 2007년 약 $6.4bn에서 2021년 $645m로 90% 줄었다고 주장했다.
따라서 spend-centric franchise는 이미 사라졌고, 사실상 낮은 대손률에 의존한 lending
business를 20배 넘게 주고 사는 셈이라고 봤다.

### 논지 ① rewards 경쟁이 fee economics를 0으로 만든다

Chase, Citi, Wells Fargo와 Capital One이 2% cash back, 큰 가입보너스와 cobrand 입찰에
공격적으로 나서 AXP도 경제성을 포기해야 한다고 주장했다. discount rate는 2005년 2.58%
에서 약 2.3%로 내려갔고 세 주요 변동비가 2011~2021년 revenue 대비 약 1,700bp 상승해
63%에 이르렀다는 분석이었다. rewards가 추가 5% 늘면 비이자 경제성이 적자로 전환한다고
봤다.

### 논지 ② AXP는 대출이익에만 의존한다

2021년 약 $5.3bn interest income과 기록적으로 낮은 write-off가 사실상 이익 전부를
만들었다고 봤다. 정상화 loss ratio와 높은 funding 필요를 반영하면 spread가 줄고,
super-prime 고객은 revolving balance를 덜 보유해 loan growth에도 한계가 있다는 주장이다.

### 논지 ③ 2022·2023·장기 목표는 달성 불가능하다

2022년 EPS 약 $9.5와 장기 revenue 10%+, EPS mid-teens 성장을 `NO chance`라고 표현했다.
2023 목표를 맞추려면 대출이 20~30%, 경우에 따라 40% 가까이 늘어야 한다고 계산했고,
실적미달과 기대치 reset을 촉매로 뒀다.

### 논지 ④ 회계·segment 표시는 악화를 가린다

rewards를 gross revenue 아래 비용으로 표시하는 방식, segment 사이의 revenue·corporate
expense 재배분, venture gain과 reserve release를 expense에 상계한 표시를 문제 삼았다.
2021 reported EPS가 reserve release와 약 $750m venture gains로 부풀었다는 지적은
중요했다. 그러나 여기서 경영진이 business story를 오도한다는 강한 결론으로 나아갔다.

### 논지 ⑤ 정상가치는 $90bn, 약 30% downside

fee business EBIT $1.8bn에 15배, lending EBIT $6.3bn에 10배를 적용해 약 $90bn,
30% downside를 제시했다. secular bear case는 $30bn까지 낮췄다.

## 8. 실제 결과

### 단기 가격방향은 맞았다

주가는 글 이후 1개월 16.1%, 3개월 6.4%, 6개월 8.3% 하락해 단순 숏 가격손익은 각각
플러스였다. 금리상승, 인플레이션과 경기침체 우려로 성장주·금융주 multiple이 압축된
구간과 겹쳤다. 전술적 숏으로 6개월 안에 청산했다면 수익이다.

그러나 SQL에는 1년 이후 성과가 없다. 보조 가격자료의 월말 기준으로 2022년 5월 약
$168.82에서 2024년 1월 약 $200.74로 18.9% 상승했다. 평가기준일까지 계속 보유했다면
배당과 대차비용 전에도 숏 손실로 전환된다. 이 수치는 일별 VIC 진입가와 정확히 일치하지
않으므로 중기 방향 확인용으로만 사용했다.

### 실적붕괴 촉매는 반대로 갔다

2022년 revenue는 25% 증가했고 EPS는 $9.85로 초기 $9.25~9.65 guidance를 상회했다.
2023년 revenue는 $60.5bn으로 reported 14%, FX-adjusted 15% 증가했고 EPS는 $11.21로
13.8% 늘었다. `10%+ revenue와 mid-teens EPS 성장에는 가능성이 없다`는 단정과 반대다.

평가기준일 뒤의 확인자료지만 2024년에도 revenue는 $65.95bn으로 9%, FX-adjusted 10%
증가하고 EPS는 $14.01로 25%, 일회성 항목을 조정하면 $13.35로 19% 늘었다. 2021년
reserve release를 제거한 뒤에도 fee·spend engine과 lending이 함께 성장했다.

### 맞은 부분: 경쟁과 2021 이익의 질

rewards·가입보너스·cobrand partner payment가 올라가는 구조적 경쟁은 실제 위험이다.
2021 EPS $10.02에는 $2.5bn reserve release가 포함됐으므로 그 숫자를 정상 earnings로
쓰면 과대평가된다. gross revenue 증가만 보고 고객유지비를 무시해서도 안 된다. 숏은
롱 투자자들이 확인해야 할 중요한 비용과 회계 bridge를 잘 지적했다.

### 틀린 부분: 독립될 수 없는 경제성을 인위적으로 분리했다

가장 큰 오류는 rewards·marketing·partner payment를 spend business 밖의 순수 누수로
본 것이다. 이 비용은 fee-based card 가입, 유지, 사용빈도와 billed business를 만드는
상품원가이기도 하다. 비용이 늘었다는 사실만으로 `그 비용이 없었어도 같은 고객·결제액과
fee revenue가 남는다`고 가정할 수 없다.

또 segment별 비이자수익에서 배분된 비용을 차감해 만든 `fee EBIT`는 독립적으로 매각하거나
15배를 적용할 수 있는 사업이 아니다. closed loop의 고객획득, network, merchant와 lending은
공유 데이터·브랜드·운영비와 자본을 사용한다. segment 재분류가 분석을 어렵게 한다는
지적과 회계조작에 가까운 경제적 소멸을 입증하는 것은 다르다.

SOTP도 공유비용·transfer pricing·필요자본을 일관되게 배분하지 않은 채 fee 잔여이익에는
15배, lending에는 10배를 적용했다. 두 이익이 서로의 고객과 transaction을 만드는
상호의존성을 끊어 계산해 정밀해 보이지만 재현 가능한 독립가치가 아니었다.

## 9. 최종 판정

**단기 가격은 성공했지만 핵심 사업논지와 중기 투자결론은 대체로 실패**다. 2021년
이익의 질과 rewards 경쟁은 맞았고 6개월 내 short P/L도 플러스였다. 그러나 촉매로 제시한
목표미달은 발생하지 않았고 2022~2024 revenue와 EPS는 오히려 강하게 성장했다.

첫 반증신호는 2022년 4분기까지 full-year revenue +25%, EPS $9.85가 확인되며 회사가
2023 revenue +15~17%, EPS $11.00~11.40을 제시한 시점이다. 이때 `no chance` 가설을
폐기하거나 최소한 fee economics 재구성 방식이 실제 consolidated 결과와 왜 어긋나는지
재검증해야 했다.

---

## 10. 세 아이디어 비교: 무엇이 성패를 갈랐나

| 분석축 | 2020-02 Long | 2020-10 Long | 2022-05 Short |
|---|---|---|---|
| 출발가격·상태 | 약 $135, 평시 15x | 약 $100, 충격 뒤 | $160대, 성장기대 논쟁 |
| 사업관 | 장기 quality compounder | quality + 위기생존 | fee engine 구조적 붕괴 |
| downside 모델 | 사실상 없음 | GFC 이상 신용손실·2025 회복 | secular bear $30bn |
| 비용 해석 | engagement가 moat 투자 | 매출과 함께 일부 가변 | rewards가 fee를 잠식하는 누수 |
| 가장 좋은 통찰 | closed-loop·자본환원 | 보수적 회복에서도 저평가 | 2021 EPS 질·경쟁비용 |
| 핵심 오류 | tail·경로 누락 | reserve release 정상화 주의 | 상호의존 사업을 인위적으로 분리 |
| 결과 | 장기 회복, 큰 초기 손실 | 빠른 rerating·매우 성공 | 단기 가격 성공, thesis 실패 |

가장 중요한 대조는 2월과 10월 롱이다. 두 글 모두 같은 기업을 좋아했지만 10월 글은
`좋은 회사라 언젠가 오른다`를 `2019 회복이 2025년이어도 싼가`로 바꿨다. 좋은 분석의
진전은 새로운 스토리를 만드는 것이 아니라, 기존 스토리가 실패할 수 있는 경로를 가격과
재무제표에 넣는 데서 나왔다.

2022년 숏은 반대로 숫자가 많지만 연결구조가 약했다. 비용·segment·대출을 세밀하게
나눴으나, 그 조각들이 서로 고객과 수익을 만드는 closed-loop라는 경제적 인과를 끊었다.
세분화는 언제나 정확성을 높이지 않는다. 분리할 수 없는 경제를 분리하면 더 정교한
오류가 된다.

---

## 11. 학습 태그

### 2020-02 Long

- `quality_compounder`
- `exogenous_shock`
- `timing_path`
- `tail_risk_omission`
- `business_right_entry_early`
- `long_term_recovery`

### 2020-10 Long

- `post_crisis_entry`
- `stress_tested_valuation`
- `balance_sheet_survival`
- `cost_flexibility`
- `faster_than_expected_recovery`
- `margin_of_safety`

### 2022-05 Short

- `reward_cost_pressure`
- `earnings_quality`
- `segment_allocation_error`
- `gross_to_net_economics`
- `price_right_thesis_wrong`
- `overconfident_no_chance`
- `catalyst_failure`

---

## 12. 향후 같은 유형을 분석할 체크리스트

1. 회사가 말하는 gross revenue와 투자자가 받을 net economics 사이의 모든 변동비를
   bridge로 작성했는가?
2. 그 비용은 순수 누수인가, 아니면 고객·매출을 만드는 상품원가 또는 획득비인가?
3. segment 이익을 독립기업처럼 평가할 수 있는가? 공유 고객·data·brand·capital과 본사비를
   일관되게 배분했는가?
4. 평시 EPS가 50% 감소하는 tail에서도 부채·규제자본과 유동성이 버티는가?
5. `장기 품질` 판단과 `현재 multiple` 판단, 그리고 `첫 12개월 경로`를 분리했는가?
6. 회사 목표를 불가능하다고 할 때 필요한 수치를 역산했을 뿐 아니라 대체 성장축과
   비용가변성도 넣었는가?
7. 단기 가격수익이 시장 beta·금리·multiple 때문인지, 예측한 사업지표 악화 때문인지
   인과를 구분했는가?
8. 첫 반증 공시가 나오면 `no chance` 같은 절대표현을 즉시 업데이트할 규칙이 있는가?

---

## 주요 근거

- [VIC 2020년 2월 AXP Long](https://www.valueinvestorsclub.com/idea/AMERICAN_EXPRESS_CO/6164368987)
- [VIC 2020년 10월 AXP Long](https://www.valueinvestorsclub.com/idea/American_Express_Company/5827292954)
- VIC 2022년 5월 AXP Short: SQL 원문, 공개 source link 미수록
- [American Express 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/4962/000000496220000030/axp-20191231.htm)
- [American Express 2020 results](https://ir.americanexpress.com/news/investor-relations-news/investor-relations-news-details/2021/American-Express-Reports-Fourth-Quarter-Revenue-of-9.4-Billion-and-Earnings-Per-Share-Of-1.76/default.aspx)
- [American Express 2021 results](https://ir.americanexpress.com/news/investor-relations-news/investor-relations-news-details/2022/American-Express-Fourth-Quarter-Revenue-Increases-30-to-12.1-Billion-Driven-By-Record-Card-Member-Spending/default.aspx)
- [American Express 2022 results, SEC exhibit](https://www.sec.gov/Archives/edgar/data/4962/000000496223000004/q422exhibit991.htm)
- [American Express 2023 results](https://ir.americanexpress.com/news/investor-relations-news/investor-relations-news-details/2024/American-Express-Announces-Record-Full-Year-2023-Revenue-of-60.5-Billion-Up-14-on-a-Reported-Basis-and-15-on-an-FX-Adjusted-Basis/default.aspx)
- [American Express 2024 results](https://ir.americanexpress.com/news/investor-relations-news/investor-relations-news-details/2025/American-Express-Announces-Record-FY-2024-Revenue-Up-9-or-10-on-an-FX-Adjusted-Basis/default.aspx)
- [American Express annual-report archive](https://ir.americanexpress.com/financials/annual-reports-and-proxy-statements/default.aspx)
- 가격수익률: VIC SQL의 horizon ratio를 실제 롱·숏 방향으로 교정. 2022년 숏의
  2024-01 중기 방향은 [Digrin 월별 조정·실제가 자료](https://www.digrin.com/stocks/detail/AXP/price)를
  보조자료로 사용했으며 정확한 VIC 일별 진입가 수익으로 간주하지 않았다.

## 데이터 해석 주의

- SQL 성과값은 `수익률`이 아니라 가격비율이다. 롱은 `ratio - 1`, 숏은 단순 가격손익을
  `1 - ratio`로 표시했다. 배당, 대차비용, benchmark alpha는 포함하지 않는다.
- 2020년 두 글은 SQL 방향 오류를 교정했다.
- 2024년 결과는 2022년 숏의 평가기준일 이후 사업논지 확인에만 사용했으며,
  2024-01-31 현재 알려진 투자판정을 사후적으로 바꾸는 단독 근거로 사용하지 않았다.
