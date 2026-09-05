# Batch 031 — Rent-A-Center & World Acceptance: RTO·소액대출의 성장, 신용, 레버리지

> **범위:** 10개 VIC 아이디어(RCII 8, WRLD 2). raw SQL/VIC 방향은 보존하고 research layer에서 방향을 별도 기록했다. 오래된 아이디어 중 VIC 전체 본문이 재수집되지 않은 경우 thesis 문장은 직접인용이 아니라 raw metadata + 당시 SEC filing에 기반한 구조적 재구성이다.

## 배치 검증 요약

- Ideas: **10**
- Sections: **100**
- Weighted claims: **60** (각 idea 100%)
- Metrics: **40**
- Timeline items: **60**
- Sources: **60**

## 공통 투자 프레임

RTO와 소액대출은 저성장처럼 보여도 고객의 유동성 제약 때문에 높은 nominal yield를 만들 수 있다. 그러나 높은 yield 자체가 moat는 아니다. 경제적 이익은 **신규 고객/계약 → 반복 지불·renewal → loss/charge-off → SG&A → funding cost → FCF**의 전체 사슬에서 결정된다. 특히 성장률이 높은 시기에는 손실이 뒤늦게 인식되고, M&A로 balance sheet가 바뀌면 작은 EBITDA miss가 equity에 비선형적으로 전이된다.

이 배치에서 재사용할 핵심 질문은 세 가지다. ① 성장의 얼마가 mature cohort에서도 남는가, ② loss-adjusted contribution이 개선되는가, ③ 인수·buyback 이후 debt service를 제하고도 FCF가 남는가. 규제는 별도 binary event가 아니라 고객획득·가격·renewal·compliance cost에 미치는 손익 변수로 모델링한다.

# WORLD ACCEPTANCE (WRLD)

## 1. 2002-03-31 — WRLD Short — hbomb5

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. 원문 링크가 raw dataset에 비어 있어 방향은 원본 추출 metadata를 기준으로 보존했다.

### 1. 무슨 기업인가
World Acceptance는 미국 남부·중서부와 과거 멕시코에서 소액 installment loan을 지점망을 통해 취급한 소비자금융사다. 수익은 대출 이자·수수료와 관련 보험상품에서 발생하며, 반복 고객의 renewal/refinancing 비중과 신규 고객 획득, charge-off·provision, 지점 생산성, 자금조달비용, 소비자보호 규제가 ROE를 좌우한다. 성장률만 볼 것이 아니라 대출 vintage별 손실과 renewals가 경제성을 얼마나 지탱하는지 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름
World Acceptance는 미국 남부·중서부와 과거 멕시코에서 소액 installment loan을 지점망을 통해 취급한 소비자금융사다. 수익은 대출 이자·수수료와 관련 보험상품에서 발생하며, 반복 고객의 renewal/refinancing 비중과 신규 고객 획득, charge-off·provision, 지점 생산성, 자금조달비용, 소비자보호 규제가 ROE를 좌우한다. 성장률만 볼 것이 아니라 대출 vintage별 손실과 renewals가 경제성을 얼마나 지탱하는지 봐야 한다. 지점은 고객 획득·collection과 renewal의 현장 unit이며 funding과 credit cost가 branch contribution을 결정한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2002년 Short는 빠른 지점·대출 성장이 곧 경제적 가치 증가라는 시장 해석을 의심하고, 반복 refinancing/renewal과 신용손실 인식이 보고 성장률과 ROE를 과대하게 보이게 할 수 있다는 구조적 회의론으로 재구성된다. 원문 방향은 Short로 확인되지만 전체 VIC 본문은 현재 연구환경에서 재수집되지 않아 숫자 문장은 contemporaneous filing과 raw metadata를 바탕으로 재구성했다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
회사는 이후 오랜 기간 생존·확장했고 2014년에도 14개 주와 멕시코에서 영업할 정도로 branch franchise를 유지했다. 즉 2002년에 즉시 구조 붕괴를 기대했다면 timing은 실패했다. 다만 2014년 CFPB CID로 renewals·마케팅·신용공여 관행이 조사 대상이 되면서 원래의 규제·상품구조 위험 자체는 훨씬 뒤에 현실화했다.

### 7. 무엇이 맞았나
핵심 구조적 위험은 있었지만 조기 Short의 시간축이 너무 짧았다. 높은 renewal 의존을 곧바로 파산/earnings collapse로 번역하기보다 vintage loss, branch maturity, funding과 규제의 임계점을 따로 추적했어야 한다.

### 8. 무엇이 틀렸나/놓쳤나
구조적 위험의 존재와 그 위험이 투자기간 안에 손익·주가로 전이되는 시점을 충분히 분리하지 못했다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2014-03-12 CFPB CID.

### 10. 재사용 가능한 교훈
소액대출은 reported loan growth보다 신규대출/renewal을 분리하고 vintage charge-off, provision, branch maturity, funding과 규제비용을 같이 추적해야 한다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | loan growth·branch productivity | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 부분적중 |
| 2 | renewal/refinance·credit quality | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 부분적중 |
| 3 | charge-off·provision economics | 17% | mature-unit contribution margin 하락 | 부분적중 |
| 4 | funding·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 부분적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 부분적중 |
| 6 | regulation·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 부분적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | branch/loan growth | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | renewal mix | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | charge-off/provision | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | regulatory status | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2002-03-31 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2002-03-31 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2014-03-12 | 2014-03-12 CFPB CID | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 회사는 이후 오랜 기간 생존·확장했고 2014년에도 14개 주와 멕시코에서 영업할 정도로 branch franchise를 유지했다. 즉 2002년에 즉시 구조 붕괴를 기대했다면 timing은 실패했다. 다만 2014년 CFPB CID로 renewals·마케팅·신용공여 관행이 조사 대상이 되면서 원래의 규제·상품구조 위험  | 사후 판정 |

### Primary / source audit

- [wrld03](https://www.sec.gov/Archives/edgar/data/108385/000010838503000006/form10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld14](https://www.sec.gov/Archives/edgar/data/108385/000010838514000021/wrld-3312014x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld15](https://www.sec.gov/Archives/edgar/data/108385/000010838515000018/wrld-3312015x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld17](https://www.sec.gov/Archives/edgar/data/108385/000010838517000020/wrld-3312017x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld18close](https://www.sec.gov/Archives/edgar/data/108385/000010838518000002/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [vic2021](https://www.valueinvestorsclub.com/ideas/a-z/2021) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 6. 2010-12-18 — WRLD Short — casper719

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. 원문 링크가 raw dataset에 비어 있어 방향은 원본 추출 metadata를 기준으로 보존했다.

### 1. 무슨 기업인가
World Acceptance는 미국 남부·중서부와 과거 멕시코에서 소액 installment loan을 지점망을 통해 취급한 소비자금융사다. 수익은 대출 이자·수수료와 관련 보험상품에서 발생하며, 반복 고객의 renewal/refinancing 비중과 신규 고객 획득, charge-off·provision, 지점 생산성, 자금조달비용, 소비자보호 규제가 ROE를 좌우한다. 성장률만 볼 것이 아니라 대출 vintage별 손실과 renewals가 경제성을 얼마나 지탱하는지 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름
World Acceptance는 미국 남부·중서부와 과거 멕시코에서 소액 installment loan을 지점망을 통해 취급한 소비자금융사다. 수익은 대출 이자·수수료와 관련 보험상품에서 발생하며, 반복 고객의 renewal/refinancing 비중과 신규 고객 획득, charge-off·provision, 지점 생산성, 자금조달비용, 소비자보호 규제가 ROE를 좌우한다. 성장률만 볼 것이 아니라 대출 vintage별 손실과 renewals가 경제성을 얼마나 지탱하는지 봐야 한다. 지점은 고객 획득·collection과 renewal의 현장 unit이며 funding과 credit cost가 branch contribution을 결정한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2010년 WRLD Short는 높은 ROE와 성장률이 반복 renewals/refinancing, 높은 effective pricing과 benign credit에 의존할 수 있고, 소비자보호 규제가 강화되면 branch economics와 valuation이 동시에 훼손될 수 있다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
규제 위험은 실제로 커졌다. 회사는 2014년 3월 CFPB로부터 CID를 받았고 2015년 10-K에 광범위한 마케팅·신용공여 관행 조사가 공시됐다. 그러나 2018년 CFPB 조사는 enforcement action 없이 종료됐다. 따라서 규제 tail risk는 정확했지만 파국적 outcome을 전제했다면 과도했다.

### 7. 무엇이 맞았나
규제 thesis는 binary 사건 예측보다 규제로 고객 acquisition, renewals, pricing, compliance cost가 얼마나 달라지는지를 손익 bridge로 만들어야 한다.

### 8. 무엇이 틀렸나/놓쳤나
구조적 위험의 존재와 그 위험이 투자기간 안에 손익·주가로 전이되는 시점을 충분히 분리하지 못했다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: CFPB CID.

### 10. 재사용 가능한 교훈
소액대출은 reported loan growth보다 신규대출/renewal을 분리하고 vintage charge-off, provision, branch maturity, funding과 규제비용을 같이 추적해야 한다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | loan growth·branch productivity | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 부분적중 |
| 2 | renewal/refinance·credit quality | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 부분적중 |
| 3 | charge-off·provision economics | 17% | mature-unit contribution margin 하락 | 부분적중 |
| 4 | funding·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 부분적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 부분적중 |
| 6 | regulation·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 부분적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | loan growth | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | renewal/refinance | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | charge-offs | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | regulatory status | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2010-12-18 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2010-12-18 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2014-03-12 | CFPB CID | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 규제 위험은 실제로 커졌다. 회사는 2014년 3월 CFPB로부터 CID를 받았고 2015년 10-K에 광범위한 마케팅·신용공여 관행 조사가 공시됐다. 그러나 2018년 CFPB 조사는 enforcement action 없이 종료됐다. 따라서 규제 tail risk는 정확했지만 파국적 outcome을 전제했다면 과도했다. | 사후 판정 |

### Primary / source audit

- [wrld03](https://www.sec.gov/Archives/edgar/data/108385/000010838503000006/form10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld14](https://www.sec.gov/Archives/edgar/data/108385/000010838514000021/wrld-3312014x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld15](https://www.sec.gov/Archives/edgar/data/108385/000010838515000018/wrld-3312015x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld17](https://www.sec.gov/Archives/edgar/data/108385/000010838517000020/wrld-3312017x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [wrld18close](https://www.sec.gov/Archives/edgar/data/108385/000010838518000002/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [vic2021](https://www.valueinvestorsclub.com/ideas/a-z/2021) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

# RENT-A-CENTER (RCII)

## 2. 2003-08-08 — RCII Short — delta2delta

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. 원문 링크가 raw dataset에 비어 있어 방향은 원본 추출 metadata를 기준으로 보존했다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2003년 Short는 핵심 rent-to-own 매장의 성숙·포화와 공격적인 unit growth가 same-store economics를 약화시키고, 높은 고정비 때문에 작은 revenue miss가 EBIT에 크게 전이될 수 있다는 논지로 재구성된다. 단순 저소득 소비자 노출보다 store cohort productivity와 loss/expense leverage가 핵심이다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
Rent-A-Center는 단기적으로 무너지지 않았고 이후 Rent-Way 등 인수를 통해 규모를 확대했다. 그러나 사업은 반복적으로 매장 구조조정과 비용절감이 필요했고 경기 하강기에 영업레버리지가 크게 드러났다. 따라서 포화 논리는 방향성은 있었지만 2003년의 즉시 catalyst로는 약했다.

### 7. 무엇이 맞았나
좋은 산업구조 질문이었지만 신규점/기존점 cohort를 분리하지 않으면 saturation thesis는 너무 일찍 short를 만들 수 있다.

### 8. 무엇이 틀렸나/놓쳤나
구조적 위험의 존재와 그 위험이 투자기간 안에 손익·주가로 전이되는 시점을 충분히 분리하지 못했다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2006~08 통합·경기하강 압력 확대.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 부분적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 부분적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 부분적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 부분적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 부분적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 부분적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | same-store sales | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | store count | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | rental merchandise loss | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | operating margin | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2003-08-08 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2003-08-08 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2008-12-31 | 2006~08 통합·경기하강 압력 확대 | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | Rent-A-Center는 단기적으로 무너지지 않았고 이후 Rent-Way 등 인수를 통해 규모를 확대했다. 그러나 사업은 반복적으로 매장 구조조정과 비용절감이 필요했고 경기 하강기에 영업레버리지가 크게 드러났다. 따라서 포화 논리는 방향성은 있었지만 2003년의 즉시 catalyst로는 약했다. | 사후 판정 |

### Primary / source audit

- [rcii03](https://www.sec.gov/Archives/edgar/data/933036/000119312504038444/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii06](https://www.sec.gov/Archives/edgar/data/933036/000095013407004710/d44558e10vk.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii08](https://www.sec.gov/Archives/edgar/data/933036/000119312509040807/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii10](https://www.sec.gov/Archives/edgar/data/933036/000119312511050980/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii12](https://www.sec.gov/Archives/edgar/data/933036/000119312513075350/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [vic2021](https://www.valueinvestorsclub.com/ideas/a-z/2021) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 3. 2004-12-08 — RCII Short — bode314

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. VIC 원문 링크가 raw dataset에 보존되어 있다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2004년 Short는 성숙한 core RTO에 대해 높은 headline EPS/FCF가 영구 성장으로 자본화되는 것을 경계하고, 상품손실·매장비용·자사주/부채를 포함한 per-share economics가 valuation을 지지하는지 묻는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
회사는 이후 여러 해 영업을 지속하고 규모도 커져 즉시 multiple collapse는 없었다. 그러나 장기적으로 매장 생산성·통합·자본배분 문제는 되풀이됐고, 2018년에는 전략적 매각 과정까지 갔다. 당시 Short는 구조 문제를 봤지만 catalyst와 horizon이 길었다.

### 7. 무엇이 맞았나
질 낮은 성장과 자본배분을 묶어 본 점은 유효하지만, 높은 FCF가 실제로 debt/buyback을 통해 per-share value를 만들 수 있는 반대경로도 확률에 넣어야 했다.

### 8. 무엇이 틀렸나/놓쳤나
구조적 위험의 존재와 그 위험이 투자기간 안에 손익·주가로 전이되는 시점을 충분히 분리하지 못했다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 후속 구조조정·전략대안 반복.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 부분적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 부분적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 부분적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 부분적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 부분적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 부분적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | core revenue | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | store productivity | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | FCF | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | net debt/share | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2004-12-08 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2004-12-08 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2016-12-31 | 후속 구조조정·전략대안 반복 | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 회사는 이후 여러 해 영업을 지속하고 규모도 커져 즉시 multiple collapse는 없었다. 그러나 장기적으로 매장 생산성·통합·자본배분 문제는 되풀이됐고, 2018년에는 전략적 매각 과정까지 갔다. 당시 Short는 구조 문제를 봤지만 catalyst와 horizon이 길었다. | 사후 판정 |

### Primary / source audit

- [rcii03](https://www.sec.gov/Archives/edgar/data/933036/000119312504038444/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii06](https://www.sec.gov/Archives/edgar/data/933036/000095013407004710/d44558e10vk.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii10](https://www.sec.gov/Archives/edgar/data/933036/000119312511050980/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii16](https://www.sec.gov/Archives/edgar/data/933036/000093303617000010/rcii-20161231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_vintage](https://www.sec.gov/Archives/edgar/data/933036/000093303618000041/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 4. 2005-11-06 — RCII Short — bal602

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. 원문 링크가 raw dataset에 비어 있어 방향은 원본 추출 metadata를 기준으로 보존했다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2005년 Short는 same-store deceleration과 비용 구조 때문에 영업레버리지가 역으로 작동할 위험, 그리고 추가 M&A가 headline growth는 만들지만 integration risk와 balance-sheet 부담을 높일 수 있다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
곧이어 Rent-Way 인수로 외형은 커졌지만 통합과 경기 하강이 겹치며 운영 난도가 상승했다. 2008년 10-K에서 경기·고객 신용여건과 손실관리 중요성이 더 커졌다. Short의 핵심인 operating leverage는 맞았지만 정확한 손익 경로는 M&A와 거시 충격에 좌우됐다.

### 7. 무엇이 맞았나
매출 성장률보다 acquired stores의 mature margin과 loss rate를 별도 cohort로 추적했어야 더 강한 논지가 됐다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 causal chain은 맞았으나 각 변수의 독립적 기여와 timing을 더 정량화할 여지는 남는다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: Rent-Way 통합 후 경기하강.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 부분적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 부분적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 부분적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 부분적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 부분적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 부분적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | same-store sales | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | acquired-store margin | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | skip/stolen loss | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | net debt | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2005-11-06 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2005-11-06 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2008-12-31 | Rent-Way 통합 후 경기하강 | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 곧이어 Rent-Way 인수로 외형은 커졌지만 통합과 경기 하강이 겹치며 운영 난도가 상승했다. 2008년 10-K에서 경기·고객 신용여건과 손실관리 중요성이 더 커졌다. Short의 핵심인 operating leverage는 맞았지만 정확한 손익 경로는 M&A와 거시 충격에 좌우됐다. | 사후 판정 |

### Primary / source audit

- [rcii06](https://www.sec.gov/Archives/edgar/data/933036/000095013407004710/d44558e10vk.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii08](https://www.sec.gov/Archives/edgar/data/933036/000119312509040807/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii10](https://www.sec.gov/Archives/edgar/data/933036/000119312511050980/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii12](https://www.sec.gov/Archives/edgar/data/933036/000119312513075350/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii16](https://www.sec.gov/Archives/edgar/data/933036/000093303617000010/rcii-20161231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 5. 2007-10-04 — RCII Short — jim211

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. VIC 원문 링크가 raw dataset에 보존되어 있다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2007년 Short는 Rent-Way 통합 직후의 높은 실행부담에 저소득 소비자 스트레스가 겹칠 경우 same-store sales, collection/loss, SG&A와 leverage가 동시에 악화될 수 있다는 경기민감 downside thesis로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
2008년 금융위기는 저소득층 현금흐름과 retail demand를 압박했고 회사는 비용·매장구조 관리가 중요해졌다. 이 아이디어는 다른 RCII shorts보다 catalyst가 가까웠고 downside 변수들이 같은 방향으로 움직이는 시점에 제시됐다.

### 7. 무엇이 맞았나
사이클 short의 질은 거시전망 자체보다 이미 높아진 operating leverage와 integration risk가 있는지를 보는 데서 나왔다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 causal chain은 맞았으나 각 변수의 독립적 기여와 timing을 더 정량화할 여지는 남는다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2008 recession stress.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | same-store sales | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | customer loss rates | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | SG&A/store | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | leverage | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2007-10-04 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2007-10-04 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2008-12-31 | 2008 recession stress | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 2008년 금융위기는 저소득층 현금흐름과 retail demand를 압박했고 회사는 비용·매장구조 관리가 중요해졌다. 이 아이디어는 다른 RCII shorts보다 catalyst가 가까웠고 downside 변수들이 같은 방향으로 움직이는 시점에 제시됐다. | 사후 판정 |

### Primary / source audit

- [rcii06](https://www.sec.gov/Archives/edgar/data/933036/000095013407004710/d44558e10vk.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii08](https://www.sec.gov/Archives/edgar/data/933036/000119312509040807/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii10](https://www.sec.gov/Archives/edgar/data/933036/000119312511050980/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii12](https://www.sec.gov/Archives/edgar/data/933036/000119312513075350/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii16](https://www.sec.gov/Archives/edgar/data/933036/000093303617000010/rcii-20161231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 7. 2012-08-24 — RCII Short — Rightlanedriver

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. VIC 원문 링크가 raw dataset에 보존되어 있다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2012년 Short는 Acceptance Now 같은 kiosk/partner channel이 빠른 originations를 만들더라도 core store maturity를 상쇄할 만큼 좋은 unit economics인지, 손실·SG&A·working capital을 반영한 incremental ROIC가 진짜 높은지 의심하는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
신규 채널은 회사 성장축이 되었지만 이후 core business 약화와 운영문제가 누적되어 2016~17 실적 압박과 전략 재검토로 이어졌다. 단순 매장수보다 channel별 loss-adjusted contribution을 봐야 한다는 문제제기는 유효했다.

### 7. 무엇이 맞았나
신규 포맷 성장률을 외삽하지 않고 mature cohort contribution과 cannibalization을 봤다는 점이 핵심 교훈이다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 causal chain은 맞았으나 각 변수의 독립적 기여와 timing을 더 정량화할 여지는 남는다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2016 core deterioration.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 부분적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 부분적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 부분적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 부분적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 부분적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 부분적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | Acceptance Now locations | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | core same-store sales | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | loss-adjusted margin | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | FCF/net debt | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2012-08-24 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2012-08-24 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2016-12-31 | 2016 core deterioration | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 신규 채널은 회사 성장축이 되었지만 이후 core business 약화와 운영문제가 누적되어 2016~17 실적 압박과 전략 재검토로 이어졌다. 단순 매장수보다 channel별 loss-adjusted contribution을 봐야 한다는 문제제기는 유효했다. | 사후 판정 |

### Primary / source audit

- [rcii12](https://www.sec.gov/Archives/edgar/data/933036/000119312513075350/d10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii16](https://www.sec.gov/Archives/edgar/data/933036/000093303617000010/rcii-20161231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii19](https://www.sec.gov/Archives/edgar/data/933036/000093303620000006/rcii-20191231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_vintage](https://www.sec.gov/Archives/edgar/data/933036/000093303618000041/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_settle](https://www.sec.gov/Archives/edgar/data/933036/000093303619000019/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 8. 2015-12-23 — RCII Short — RiskReward

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. 원문 링크가 raw dataset에 비어 있어 방향은 원본 추출 metadata를 기준으로 보존했다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2015년 Short는 Acceptance Now의 높은 headline growth가 core store의 약화, loss/collection pressure와 SG&A deleverage를 가릴 수 있으며, 성장채널의 economics가 둔화되면 전체 enterprise가 구조조정 모드로 들어갈 수 있다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
2016~17에 운영악화와 경영진 변화가 나타났고 회사는 결국 전략적 대안을 검토했다. 2018년 Vintage와 $15/share 매각계약까지 갔지만 거래는 깨졌고 회사는 $126.5m reverse fee를 요구한 뒤 2019년 $92.5m 현금 합의금을 받았다. Short가 본 사업 스트레스는 현실화했지만 event-driven path는 복잡했다.

### 7. 무엇이 맞았나
성장채널이 core weakness를 상쇄하는지 판단할 때 revenue mix가 아니라 incremental contribution, loss rate, cash conversion을 봐야 한다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 causal chain은 맞았으나 각 변수의 독립적 기여와 timing을 더 정량화할 여지는 남는다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2016~17 운영악화·전략대안.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | core same-store sales | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 2 | Acceptance Now growth | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 3 | loss rate | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |
| 4 | operating margin | 당시 filing/VIC에서 추적 | 후속 공시로 추적 |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2015-12-23 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2015-12-23 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2016-12-31 | 2016~17 운영악화·전략대안 | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 2016~17에 운영악화와 경영진 변화가 나타났고 회사는 결국 전략적 대안을 검토했다. 2018년 Vintage와 $15/share 매각계약까지 갔지만 거래는 깨졌고 회사는 $126.5m reverse fee를 요구한 뒤 2019년 $92.5m 현금 합의금을 받았다. Short가 본 사업 스트레스는 현실화했지만 event | 사후 판정 |

### Primary / source audit

- [rcii16](https://www.sec.gov/Archives/edgar/data/933036/000093303617000010/rcii-20161231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_vintage](https://www.sec.gov/Archives/edgar/data/933036/000093303618000041/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_settle](https://www.sec.gov/Archives/edgar/data/933036/000093303619000019/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii19](https://www.sec.gov/Archives/edgar/data/933036/000093303620000006/rcii-20191231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [vic2021](https://www.valueinvestorsclub.com/ideas/a-z/2021) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 9. 2021-08-18 — RCII Long — bigvic

**VIC 방향 검증:** raw `is_short=false` → research direction **Long**. VIC 원문 링크가 raw dataset에 보존되어 있다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2021년 Long은 Acima 인수로 RCII가 매장형 RTO에서 merchant-integrated virtual lease-to-own 플랫폼으로 확장되고, 더 큰 TAM·merchant network·디지털 underwriting이 높은 성장과 FCF를 만들며 시너지가 acquisition leverage를 빠르게 낮춘다는 논지였다. 이 건은 VIC 2021 A-Z에서도 Short 표식이 없는 Long으로 확인된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
2020말 RCII는 net debt/adjusted EBITDA 약 0.1x였지만 Acima 거래는 약 $1.3bn cash와 주식대가를 수반했고 $875m term loan과 $450m 6.375% notes 등으로 자금조달됐다. 2021 매출은 $4.6bn으로 커졌지만 2022 Acima revenue -9.4%, GMV -17.2%, segment operating profit -14.3%; 회사 전체 adjusted EBITDA는 $453.5m로 28.2% 감소했고 net debt/adjusted EBITDA는 2.8x가 됐다. 성장 플랫폼보다 post-stimulus normalization, underwriting/loss와 leverage가 먼저 지배했다.

### 7. 무엇이 맞았나
TAM과 merchant count를 성장률로 외삽하고 acquisition leverage의 비선형 downside를 작게 본 실패다. deal 전 낮은 leverage는 안전마진이 아니라 큰 인수를 가능하게 한 capacity였고, 인수 후에는 downside convexity가 커졌다.

### 8. 무엇이 틀렸나/놓쳤나
TAM·성장률을 외삽하고 acquisition leverage와 credit normalization의 비선형 downside를 과소평가했다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2022 Acima GMV·EBITDA 급감.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 오판 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 오판 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 오판 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 오판 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 오판 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 오판 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | Acima GMV | 당시 filing/VIC에서 추적 | 2022 -17.2% |
| 2 | Acima revenue | 당시 filing/VIC에서 추적 | 2022 -9.4% |
| 3 | adjusted EBITDA | 당시 filing/VIC에서 추적 | 2022 $453.5m, -28.2% |
| 4 | net debt/EBITDA | 당시 filing/VIC에서 추적 | 2022 2.8x |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2021-08-18 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2021-08-18 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2022-12-31 | 2022 Acima GMV·EBITDA 급감 | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 2020말 RCII는 net debt/adjusted EBITDA 약 0.1x였지만 Acima 거래는 약 $1.3bn cash와 주식대가를 수반했고 $875m term loan과 $450m 6.375% notes 등으로 자금조달됐다. 2021 매출은 $4.6bn으로 커졌지만 2022 Acima revenue -9.4%,  | 사후 판정 |

### Primary / source audit

- [rcii21](https://www.sec.gov/Archives/edgar/data/933036/000093303622000008/rcii-20211231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii22](https://www.sec.gov/Archives/edgar/data/933036/000093303623000007/rcii-20221231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii19](https://www.sec.gov/Archives/edgar/data/933036/000093303620000006/rcii-20191231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_vintage](https://www.sec.gov/Archives/edgar/data/933036/000093303618000041/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [vic2021](https://www.valueinvestorsclub.com/ideas/a-z/2021) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

## 10. 2022-05-24 — RCII Short — AIFL

**VIC 방향 검증:** raw `is_short=true` → research direction **Short**. 원문 링크가 raw dataset에 비어 있어 방향은 원본 추출 metadata를 기준으로 보존했다.

### 1. 무슨 기업인가
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다.

### 2. 산업 가치사슬과 돈의 흐름
Rent-A-Center는 미국의 rent-to-own 사업자다. 전통 매장은 가전·가구·전자제품을 주·월 단위 rental-purchase 계약으로 제공하고, 고객은 계약을 끝까지 이행하면 소유권을 취득한다. 2021년 Acima 인수 후에는 제휴 소매점 POS에서 가상 lease-to-own를 제공하는 디지털 채널이 커졌다. 경제성의 핵심은 신규 계약/GMV, 반복 지불률, 상품 원가와 depreciation, skip/stolen losses, 매장·merchant 생산성, CAC·underwriting, SG&A와 차입비용이다. 고객이 매장/merchant에서 상품을 선택하면 계약자산과 collection risk를 회사가 부담한다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심 경쟁력은 자금 접근성·distribution·underwriting/collection 데이터와 density지만 고객층의 취약성과 규제가 동시에 moat의 한계를 만든다.

### 4. 당시 VIC 원문과 핵심 숫자
2022년 Short는 stimulus 종료와 소비 정상화로 Acima/RAC originations가 둔화되는 동시에 loss rate가 올라가고, 2021 Acima 인수로 높아진 debt가 EBITDA 감소를 equity에 증폭시킨다는 post-acquisition deleveraging 실패 thesis로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
당시 valuation은 headline EPS나 TAM보다 loss-adjusted FCF, mature-unit margin과 debt sensitivity를 중심으로 재구성하는 것이 적절하다.

### 6. 실제 전개
2022년 결과는 논지를 강하게 지지했다. Acima revenue는 $2.328bn에서 $2.110bn으로 9.4% 감소했고 GMV는 17.2% 감소했다. Acima gross profit -13.3%, operating profit -14.3%; RAC segment skip/stolen losses는 revenue의 4.9%로 2021년 3.1%보다 상승했다. 전체 adjusted EBITDA는 28.2% 감소하고 year-end net leverage는 2.8x였다.

### 7. 무엇이 맞았나
이 Short는 성장둔화 하나가 아니라 volume, credit/loss, margin과 leverage가 같은 방향으로 움직이는 causal chain을 잡았다. 인수 후 기업의 가장 중요한 지표는 pro forma growth가 아니라 debt service 전 loss-adjusted FCF다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 causal chain은 맞았으나 각 변수의 독립적 기여와 timing을 더 정량화할 여지는 남는다.

### 9. 사전 반증조건과 첫 신호
사전 반증조건은 volume/origination, loss/charge-off, margin/FCF, leverage 중 2개 이상이 2개 분기 연속 악화하는 경우다. 첫 신호: 2022 GMV·loss·EBITDA 동시 악화.

### 10. 재사용 가능한 교훈
RTO는 revenue 성장보다 loss-adjusted contribution과 cohort/store/merchant maturity를 추적해야 한다. 성장채널 인수 뒤에는 pro forma EBITDA가 아니라 debt service 전 FCF, loss rate와 leverage를 같이 본다.

### 핵심 주장 6개와 사후 판정

| # | 주장 축 | Weight | 사전 반증조건 | 사후 판정 |
|---:|---|---:|---|---|
| 1 | 수요·originations / same-store | 20% | volume/origination 또는 same-store/loan growth가 2개 분기 연속 악화 | 적중 |
| 2 | loss rate·underwriting | 18% | loss/charge-off가 가격·yield 개선보다 빠르게 악화 | 적중 |
| 3 | unit economics·operating leverage | 17% | mature-unit contribution margin 하락 | 적중 |
| 4 | FCF·balance sheet | 16% | FCF 적자 또는 leverage 상승 | 적중 |
| 5 | valuation·capital allocation | 15% | loss-adjusted normalized FCF 기준 기대수익률 소멸 | 적중 |
| 6 | 규제·catalyst·반증규칙 | 14% | 규제·catalyst가 반대로 전개되거나 핵심 KPI 반증에도 thesis 유지 | 적중 |

### 추적 Metric

| # | Metric | T0 | 사후 |
|---:|---|---|---|
| 1 | Acima GMV | 당시 filing/VIC에서 추적 | 2022 -17.2% |
| 2 | RAC skip/stolen loss | 당시 filing/VIC에서 추적 | 2022 4.9% vs 3.1% |
| 3 | adjusted EBITDA | 당시 filing/VIC에서 추적 | 2022 $453.5m, -28.2% |
| 4 | net leverage | 당시 filing/VIC에서 추적 | 2022 2.8x |

### Timeline

| 날짜 | 사건 | 해석 |
|---|---|---|
| 2022-05-24 | VIC idea 게시 | 원 논지와 방향의 기준점 |
| 2022-05-24 | 당시 SEC filing / 사업구조 확인 | T0 base-rate와 balance sheet |
| 2022-12-31 | 2022 GMV·loss·EBITDA 동시 악화 | 첫 핵심 신호 |
| 2018-12-31 | 규제·전략·산업구조의 후속 변화 점검 | 중간 posterior update |
| 2021-12-31 | pandemic/Acima 등 후속 regime 점검 | 경로의 비선형성 확인 |
| 2022-12-31 | 2022년 결과는 논지를 강하게 지지했다. Acima revenue는 $2.328bn에서 $2.110bn으로 9.4% 감소했고 GMV는 17.2% 감소했다. Acima gross profit -13.3%, operating profit -14.3%; RAC segment skip/stolen losses는 revenue의 | 사후 판정 |

### Primary / source audit

- [rcii21](https://www.sec.gov/Archives/edgar/data/933036/000093303622000008/rcii-20211231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii22](https://www.sec.gov/Archives/edgar/data/933036/000093303623000007/rcii-20221231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii19](https://www.sec.gov/Archives/edgar/data/933036/000093303620000006/rcii-20191231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii18](https://www.sec.gov/Archives/edgar/data/933036/000093303619000010/rcii-20181231x10k.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [rcii_vintage](https://www.sec.gov/Archives/edgar/data/933036/000093303618000041/ex991pressrelease.htm) — 원 방향/당시 사업·재무·규제/후속 outcome 검증
- [vic2021](https://www.valueinvestorsclub.com/ideas/a-z/2021) — 원 방향/당시 사업·재무·규제/후속 outcome 검증

