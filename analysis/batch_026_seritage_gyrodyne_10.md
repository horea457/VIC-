# Batch 026 — Seritage Growth Properties·Gyrodyne 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Seritage 8건 · Gyrodyne 2건

## 결론부터

이번 배치는 **NAV가 실제 주주현금이 되기까지의 마찰**을 분석한다.

- **Seritage:** 좋은 Sears 부동산과 낮은 in-place rent는 실제 option value였다. 그러나 Bull 글들은 대부분 stabilized NAV에서 remaining CapEx·vacancy carry·interest·Sears rent cliff와 time을 충분히 차감하지 않았다. 2016 Short는 이 J-curve를 정확히 봤다. 2018 fraudulent-conveyance Short는 주가 방향은 맞았지만 핵심 법률손실 규모는 틀렸고, 2022 Short는 debt stress를 맞혔지만 자산매각을 통한 orderly liquidation 경로를 낮게 봐 equity-zero까지는 실패했다.
- **Gyrodyne:** 반대로 법원 award principal + 연 9% statutory interest + remaining property floor를 probability-weighted liquidation value로 계산했다. 상급심 승소, 2012 약 $167.53m 현금수령, 2013 $66.56 특별배당으로 value가 실제 cash로 crystallize됐다.

> 방향 교정: SRG 8건은 raw SQL이 모두 `is_short=true`다. 실제로 2016-08·2018-10·2022-03 세 건만 Short이고 나머지 5건은 Long이다. Gyrodyne 2건은 raw/actual 모두 Long이다.

---

# SERITAGE GROWTH PROPERTIES (SRG) — 기업과 비즈니스

## 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

## 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2015-08-05 | Short | Long | Sears rights spin·low-rent redevelopment Long | 2015 $39.60 부근에서 시작해 2018 한때 $50대에 갔지만 2022 $10대, 2024-01 약 $9.15. 장기 compounder thesis 실패. | 자산가치 일부 적중·장기 equity thesis 실패 |
| 2016-02-09 | Short | Long | $4.30→$18.80 rent redevelopment economics Long | 2016-02 ~$41 → 2024-01 ~$9.15. 부동산 redevelopment math는 일부 맞았지만 equity는 실패. | 프로젝트 경제성 적중·포트폴리오 자금조달 실패 |
| 2016-08-25 | Short | Short | Sears Chapter 7·rent cliff/liquidity Short | 2016-08 ~$44.5 → 2024-01 ~$9.15. 장기 가격방향 강한 적중, Sears bankruptcy timing은 약 2년 늦음. | 장기 Short 성공·타이밍 지연 |
| 2017-02-03 | Short | Long | Short rebuttal·JV/asset-value redevelopment Long | 2017 ~$46.5 → 2024 ~$9.15. 장기 실패. | 자산질 통찰은 있었으나 liquidity thesis 실패 |
| 2018-05-23 | Short | Long | Property-level SOTP·$50 base/$60~70 long-term Long | 2018-08 한때 약 $51.48로 $50 base를 달성했지만 2024-01 $9.15. 단기 목표 성공·구조적 실패. | 단기 가격 성공·장기 thesis 실패 |
| 2018-10-17 | Short | Short | Fraudulent-conveyance $500m~1.5bn existential Short | 2018-10 ~$38 → 2024-01 ~$9.15로 가격은 강하게 하락. 그러나 핵심 fraudulent-transfer 손실 추정은 크게 과대. | 가격 성공·핵심 인과 실패 |
| 2018-11-01 | Short | Long | Fraudulent-conveyance rebuttal·asset-value Long | 2018-11 ~$37.94 → 2024-01 ~$9.15. 법률 rebuttal은 맞았지만 Long은 실패. | 법률판단 적중·증권 Long 실패 |
| 2022-03-10 | Short | Short | $1.44bn Berkshire loan·liquidity/equity-zero Short | 2022 중 $5대까지 하락해 tactical Short 성공, 2024-01 $9.15. Equity-zero는 cutoff까지 실패. | 전술적 가격 성공·zero thesis 실패 |

---

<!-- idea:b3cf317f-c393-4f1e-8595-50e68a65599c -->
## 1. 2015-08-05 — Sears rights spin·low-rent redevelopment Long

### 결론부터

**종합판정: 자산가치 일부 적중·장기 equity thesis 실패.** 토지와 embedded rent spread는 실제였지만 NAV에서 시간축과 funding requirement가 빠졌다. 낮은 in-place rent는 upside인 동시에 tenant가 갑자기 사라질 경우 near-term cash-flow liability였다.

**주가·증권 결과:** 2015 $39.60 부근에서 시작해 2018 한때 $50대에 갔지만 2022 $10대, 2024-01 약 $9.15. 장기 compounder thesis 실패.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

### 5. 밸류에이션과 기대수익의 연결

Rights offering $29.58, 당시 price $39.60. 53.3m shares, market cap ~$2.1bn, debt ~$1.2bn, EV ~$3.3bn. Sears의 비정상적으로 낮은 rent를 market rent로 바꾸는 NOI uplift를 NAV 핵심으로 봤다. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Rent spread — 적중 · 논지 비중 18%

**당시 주장**

Sears의 낮은 rent를 market rent로 올릴 수 있다.

**당시 근거**

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

**이 주장이 성립하려면**

tenant demand

**사전 반증조건**

retail demand/lease-up 약화

**실제 결과**

일부 redevelopments에서 rent uplift 현실화.

**정량적 괴리**

주가 / $39.60 / NAV rerating / 2024-01 ~$9.15

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Rent spread 가설은 'retail demand/lease-up 약화'를 사전 반증조건으로 저장한다.

#### 2. Location quality — 부분 · 논지 비중 18%

**당시 주장**

prime locations가 asset floor를 만든다.

**당시 근거**

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

**이 주장이 성립하려면**

liquid buyer demand

**사전 반증조건**

sale discounts

**실제 결과**

자산 매각가치는 있었지만 equity floor는 약했다.

**정량적 괴리**

EV / ~$3.3bn / asset value > EV / 장기 debt/capex 압박

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Location quality 가설은 'sale discounts'를 사전 반증조건으로 저장한다.

#### 3. Recapture optionality — 실패 · 논지 비중 16%

**당시 주장**

Sears space를 선택적으로 회수한다.

**당시 근거**

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

**이 주장이 성립하려면**

Sears survives long enough

**사전 반증조건**

tenant bankruptcy causes mass vacancy

**실제 결과**

2018 bankruptcy로 강제화.

**정량적 괴리**

Sears rent / 매우 낮음 / market-rent uplift / Sears bankruptcy로 먼저 소멸

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Recapture optionality 가설은 'tenant bankruptcy causes mass vacancy'를 사전 반증조건으로 저장한다.

#### 4. Funding — 실패 · 논지 비중 16%

**당시 주장**

debt와 cash flow로 redevelopment를 감당한다.

**당시 근거**

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

**이 주장이 성립하려면**

capex pacing

**사전 반증조건**

rent loss>new NOI

**실제 결과**

liquidity가 핵심문제.

**정량적 괴리**

구조 / growth REIT / redevelopment compound / 2022 Plan of Sale

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Funding 가설은 'rent loss>new NOI'를 사전 반증조건으로 저장한다.

#### 5. Sponsor quality — 부분 · 논지 비중 16%

**당시 주장**

strong sponsors가 capital allocation을 돕는다.

**당시 근거**

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

**이 주장이 성립하려면**

aligned financing

**사전 반증조건**

leverage/time dominates

**실제 결과**

완전한 보호막 아니었음.

**정량적 괴리**

2015 $39.60 부근에서 시작해 2018 한때 $50대에 갔지만 2022 $10대, 2024-01 약 $9.15. 장기 compounder thesis 실패.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Sponsor quality 가설은 'leverage/time dominates'를 사전 반증조건으로 저장한다.

#### 6. NAV rerating — 실패 · 논지 비중 16%

**당시 주장**

redevelopment가 EV보다 높은 NAV를 현실화한다.

**당시 근거**

Sears에서 분리된 portfolio가 prime mall/outparcel locations를 매우 낮은 rent로 임대하고 있어 공간을 recapture·redevelop하면 평방피트당 rent와 property value가 크게 상승한다고 봤다. Berkshire/ESL 등 강한 sponsors와 Sears lease termination rights를 catalyst로 봤다.

**이 주장이 성립하려면**

completion/sale

**사전 반증조건**

time/cost leakage

**실제 결과**

장기 실패.

**정량적 괴리**

2015 $39.60 부근에서 시작해 2018 한때 $50대에 갔지만 2022 $10대, 2024-01 약 $9.15. 장기 compounder thesis 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

NAV rerating 가설은 'time/cost leakage'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

여러 redevelopment는 실제 higher rents와 mixed-use optionality를 만들었지만 Sears decline/bankruptcy가 너무 빨라 old rent가 사라지는 속도가 new rent opening보다 빨랐다. CapEx·interest·construction duration이 equity를 압박했고 결국 회사는 2022 Plan of Sale로 전환했다. 2024-01 주가는 약 $9.15.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2015 $39.60 부근에서 시작해 2018 한때 $50대에 갔지만 2022 $10대, 2024-01 약 $9.15. 장기 compounder thesis 실패. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

토지와 embedded rent spread는 실제였지만 NAV에서 시간축과 funding requirement가 빠졌다. 낮은 in-place rent는 upside인 동시에 tenant가 갑자기 사라질 경우 near-term cash-flow liability였다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-10-15 — Sears bankruptcy로 대규모 recapture가 선택적 catalyst가 아니라 강제적 cash-flow shock으로 바뀌었다. 회피 가능성: 매우 높음. Sears rent loss와 redevelopment completion을 연도별 cash waterfall로 모델링했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

자산가치 일부 적중·장기 equity thesis 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $39.60 | NAV rerating | 2024-01 ~$9.15 | 실패 |
| EV | ~$3.3bn | asset value > EV | 장기 debt/capex 압박 | 부분 |
| Sears rent | 매우 낮음 | market-rent uplift | Sears bankruptcy로 먼저 소멸 | 양면 |
| 구조 | growth REIT | redevelopment compound | 2022 Plan of Sale | 전제변경 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2015-08-05 | VIC 아이디어 게시 | Sears rights spin·low-rent redevelopment Long |
| 2018-10-15 | 최초 핵심 검증·반증 신호 | Sears bankruptcy로 대규모 recapture가 선택적 catalyst가 아니라 강제적 cash-flow shock으로 바뀌었다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2015 $39.60 부근에서 시작해 2018 한때 $50대에 갔지만 2022 $10대, 2024-01 약 $9.15. 장기 compounder thesis 실패. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2018-10-15 — Sears bankruptcy로 대규모 recapture가 선택적 catalyst가 아니라 강제적 cash-flow shock으로 바뀌었다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 매우 높음. Sears rent loss와 redevelopment completion을 연도별 cash waterfall로 모델링했어야 한다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- [1. VIC SRG 2015-08-05 원문](https://www.valueinvestorsclub.com/idea/SERITAGE_GROWTH_PROPERTIES/1909382595) — Value Investors Club / user SQL, 2015-08-05. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:d073cdf4-233c-443b-a201-fc94904651c1 -->
## 2. 2016-02-09 — $4.30→$18.80 rent redevelopment economics Long

### 결론부터

**종합판정: 프로젝트 경제성 적중·포트폴리오 자금조달 실패.** 좋은 프로젝트 underwriting과 좋은 security underwriting을 혼동한 사례다. 한 건의 10~13% yield-on-cost가 맞아도 전체 pipeline의 CapEx peak, debt interest와 completion sequence를 합산해야 한다.

**주가·증권 결과:** 2016-02 ~$41 → 2024-01 ~$9.15. 부동산 redevelopment math는 일부 맞았지만 equity는 실패.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Old rent 약 $4.30/sqft. Higher-quality sites에 $100/sqft capex로 13% return을 내려면 new rent 약 $18.80, lower-quality $60/sqft capex/10% return이면 약 $9.00 rent가 필요하다고 계산. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Yield-on-cost — 부분 적중 · 논지 비중 18%

**당시 주장**

13%/10% redevelopment returns가 가능하다.

**당시 근거**

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

**이 주장이 성립하려면**

market rents exceed hurdle

**사전 반증조건**

construction/rent miss

**실제 결과**

일부 프로젝트에서 가능.

**정량적 괴리**

Old rent / $4.30/sqft / 재임대 / 대규모 recapture

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Yield-on-cost 가설은 'construction/rent miss'를 사전 반증조건으로 저장한다.

#### 2. Rent hurdle — 부분 · 논지 비중 18%

**당시 주장**

$18.80/$9가 충분히 보수적이다.

**당시 근거**

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

**이 주장이 성립하려면**

tenant demand

**사전 반증조건**

retail disruption

**실제 결과**

상위 site는 가능, 전체 portfolio는 불균일.

**정량적 괴리**

High-quality / $100 capex /13% / $18.80 rent / 일부 market rent 가능

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Rent hurdle 가설은 'retail disruption'를 사전 반증조건으로 저장한다.

#### 3. Repeatability — 실패 · 논지 비중 16%

**당시 주장**

개별 project economics를 portfolio 전체에 반복한다.

**당시 근거**

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

**이 주장이 성립하려면**

capital availability

**사전 반증조건**

too many simultaneous projects

**실제 결과**

funding bottleneck.

**정량적 괴리**

Lower-quality / $60 /10% / $9 rent / 일부 가능

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Repeatability 가설은 'too many simultaneous projects'를 사전 반증조건으로 저장한다.

#### 4. Time to rent — 실패 · 논지 비중 16%

**당시 주장**

redevelopment 후 rent가 빠르게 열린다.

**당시 근거**

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

**이 주장이 성립하려면**

permits/tenants timely

**사전 반증조건**

multi-year delays

**실제 결과**

negative carry 확대.

**정량적 괴리**

주가 / ~$41.36 / NAV growth / 2024 ~$9.15

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Time to rent 가설은 'multi-year delays'를 사전 반증조건으로 저장한다.

#### 5. Debt capacity — 실패 · 논지 비중 16%

**당시 주장**

company가 pipeline을 자금조달할 수 있다.

**당시 근거**

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

**이 주장이 성립하려면**

NOI grows with capex

**사전 반증조건**

old rent disappears first

**실제 결과**

liquidity stress.

**정량적 괴리**

2016-02 ~$41 → 2024-01 ~$9.15. 부동산 redevelopment math는 일부 맞았지만 equity는 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Debt capacity 가설은 'old rent disappears first'를 사전 반증조건으로 저장한다.

#### 6. Equity compounding — 실패 · 논지 비중 16%

**당시 주장**

project IRR가 주당 NAV 상승으로 연결된다.

**당시 근거**

개별 redevelopment에서 필요한 new rent hurdle이 시장 rent보다 낮아 프로젝트-level returns가 매우 매력적이라고 봤다. Portfolio 전체에서 이런 spread를 반복하면 NAV와 FFO가 크게 상승한다고 주장했다.

**이 주장이 성립하려면**

capital structure stable

**사전 반증조건**

debt/time absorbs returns

**실제 결과**

주가 급락.

**정량적 괴리**

2016-02 ~$41 → 2024-01 ~$9.15. 부동산 redevelopment math는 일부 맞았지만 equity는 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Equity compounding 가설은 'debt/time absorbs returns'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

일부 프로젝트의 tenant rents는 hurdle을 충족했지만 문제는 동시에 너무 많은 Sears 공간이 비고 portfolio-level funding gap이 발생한 것이다. Project IRR이 좋아도 전체 회사가 construction 기간의 negative carry를 감당하지 못하면 equity compounding으로 연결되지 않는다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2016-02 ~$41 → 2024-01 ~$9.15. 부동산 redevelopment math는 일부 맞았지만 equity는 실패. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

좋은 프로젝트 underwriting과 좋은 security underwriting을 혼동한 사례다. 한 건의 10~13% yield-on-cost가 맞아도 전체 pipeline의 CapEx peak, debt interest와 completion sequence를 합산해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-10-15 — Sears bankruptcy로 portfolio-level vacancy와 redevelopment funding requirement가 동시에 급증했다. 회피 가능성: 매우 높음. site별 project IRR 외에 annual corporate cash burn/loan covenant를 모델링했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

프로젝트 경제성 적중·포트폴리오 자금조달 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Old rent | $4.30/sqft | 재임대 | 대규모 recapture | 기회+리스크 |
| High-quality | $100 capex /13% | $18.80 rent | 일부 market rent 가능 | project 적중 |
| Lower-quality | $60 /10% | $9 rent | 일부 가능 | project 적중 |
| 주가 | ~$41.36 | NAV growth | 2024 ~$9.15 | security 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-02-09 | VIC 아이디어 게시 | $4.30→$18.80 rent redevelopment economics Long |
| 2018-10-15 | 최초 핵심 검증·반증 신호 | Sears bankruptcy로 portfolio-level vacancy와 redevelopment funding requirement가 동시에 급증했다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2016-02 ~$41 → 2024-01 ~$9.15. 부동산 redevelopment math는 일부 맞았지만 equity는 실패. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2018-10-15 — Sears bankruptcy로 portfolio-level vacancy와 redevelopment funding requirement가 동시에 급증했다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 매우 높음. site별 project IRR 외에 annual corporate cash burn/loan covenant를 모델링했어야 한다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- 1. VIC SRG 2016-02-09 원문 — Value Investors Club / user SQL, 2016-02-09. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:cdcae60e-79b5-4f9f-be7b-8a67c42b637f -->
## 3. 2016-08-25 — Sears Chapter 7·rent cliff/liquidity Short

### 결론부터

**종합판정: 장기 Short 성공·타이밍 지연.** 동일한 낮은 rent를 '향후 upside'가 아니라 '현재 negative-carry subsidy'로 재해석한 것이 핵심 edge였다. 실패는 정확한 bankruptcy timing을 너무 당긴 것.

**주가·증권 결과:** 2016-08 ~$44.5 → 2024-01 ~$9.15. 장기 가격방향 강한 적중, Sears bankruptcy timing은 약 2년 늦음.

**Thesis / Process 점수:** 9 / 8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

SHLD leased GLA 약 35.105m sqft, annual base rent $150.937m, third-party rent $38.779m. 추가 triple-net reimbursements 약 $70.2m로 추정. Sears Chapter 7 시 rent/reimbursement가 급감해 funding need가 폭증한다고 봄. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Sears failure — 방향 적중·timing 지연 · 논지 비중 18%

**당시 주장**

Sears가 예상보다 빨리 파산한다.

**당시 근거**

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

**이 주장이 성립하려면**

liquidity deteriorates

**사전 반증조건**

turnaround

**실제 결과**

2018 Chapter 11.

**정량적 괴리**

Sears GLA / 35.105m sqft / large exposure / bankruptcy/closures

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Sears failure 가설은 'turnaround'를 사전 반증조건으로 저장한다.

#### 2. Rent cliff — 적중 · 논지 비중 18%

**당시 주장**

Sears base rent가 사라진다.

**당시 근거**

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

**이 주장이 성립하려면**

leases terminate

**사전 반증조건**

continued payments

**실제 결과**

closures로 현실화.

**정량적 괴리**

Base rent / $150.937m / 소멸 위험 / 대규모 감소

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Rent cliff 가설은 'continued payments'를 사전 반증조건으로 저장한다.

#### 3. Expense transfer — 적중 · 논지 비중 16%

**당시 주장**

tax/maintenance reimbursements가 SRG 부담이 된다.

**당시 근거**

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

**이 주장이 성립하려면**

vacancy

**사전 반증조건**

new tenants immediately replace

**실제 결과**

negative carry 증가.

**정량적 괴리**

NNN reimburse / ~$70.2m / SRG expense로 전환 / carrying cost 부담

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Expense transfer 가설은 'new tenants immediately replace'를 사전 반증조건으로 저장한다.

#### 4. Redevelopment funding — 적중 · 논지 비중 16%

**당시 주장**

동시 recapture가 capital need를 폭증시킨다.

**당시 근거**

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

**이 주장이 성립하려면**

capex intensive

**사전 반증조건**

asset sales fund smoothly

**실제 결과**

term-loan/asset sales 의존.

**정량적 괴리**

주가 / $44.50 / large downside / 2024 ~$9.15

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Redevelopment funding 가설은 'asset sales fund smoothly'를 사전 반증조건으로 저장한다.

#### 5. NAV illusion — 강한 적중 · 논지 비중 16%

**당시 주장**

stabilized NAV가 interim liquidity를 무시한다.

**당시 근거**

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

**이 주장이 성립하려면**

long duration

**사전 반증조건**

fast execution

**실제 결과**

time/debt가 equity 훼손.

**정량적 괴리**

2016-08 ~$44.5 → 2024-01 ~$9.15. 장기 가격방향 강한 적중, Sears bankruptcy timing은 약 2년 늦음.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

NAV illusion 가설은 'fast execution'를 사전 반증조건으로 저장한다.

#### 6. Short payoff — 강한 적중 · 논지 비중 16%

**당시 주장**

liquidity stress가 equity를 크게 낮춘다.

**당시 근거**

Bull은 낮은 Sears rent를 upside로 보지만 실제로는 Sears가 redevelopment 기간의 carrying cost를 대신 내주는 financing source라고 반박했다. Sears가 Chapter 7으로 빠르게 사라지면 $150m base rent와 ~$70m reimbursements가 사라지고 SRG가 taxes/maintenance까지 떠안아 liquidity가 악화된다고 주장했다.

**이 주장이 성립하려면**

no rescue

**사전 반증조건**

cheap financing

**실제 결과**

장기 주가 -80% 수준.

**정량적 괴리**

2016-08 ~$44.5 → 2024-01 ~$9.15. 장기 가격방향 강한 적중, Sears bankruptcy timing은 약 2년 늦음.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Short payoff 가설은 'cheap financing'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Sears는 즉시 Chapter 7은 아니었지만 2018 Chapter 11을 신청했고 대규모 store closures가 발생했다. 그 뒤 SRG는 redevelopment cash burn과 term loan 의존도가 커졌고 장기 주가는 크게 하락했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2016-08 ~$44.5 → 2024-01 ~$9.15. 장기 가격방향 강한 적중, Sears bankruptcy timing은 약 2년 늦음. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

동일한 낮은 rent를 '향후 upside'가 아니라 '현재 negative-carry subsidy'로 재해석한 것이 핵심 edge였다. 실패는 정확한 bankruptcy timing을 너무 당긴 것.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-10-15 — Sears Chapter 11 filing으로 tenant-support/rent-cliff mechanism이 현실화됐다. 회피 가능성: Short 유지 가능. 다만 2016~18 squeeze/borrow cost를 버틸 position sizing이 필요했다.

### 10. 최종 판정·반사실·재사용 교훈

장기 Short 성공·타이밍 지연. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Sears GLA | 35.105m sqft | large exposure | bankruptcy/closures | 적중 |
| Base rent | $150.937m | 소멸 위험 | 대규모 감소 | 적중 |
| NNN reimburse | ~$70.2m | SRG expense로 전환 | carrying cost 부담 | 적중 |
| 주가 | $44.50 | large downside | 2024 ~$9.15 | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-08-25 | VIC 아이디어 게시 | Sears Chapter 7·rent cliff/liquidity Short |
| 2018-10-15 | 최초 핵심 검증·반증 신호 | Sears Chapter 11 filing으로 tenant-support/rent-cliff mechanism이 현실화됐다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2016-08 ~$44.5 → 2024-01 ~$9.15. 장기 가격방향 강한 적중, Sears bankruptcy timing은 약 2년 늦음. |

### Failure / Success Anatomy

- **근본 오류:** event payoff를 probability×cash waterfall로 분해
- **최초 검증·반증 신호:** 2018-10-15 — Sears Chapter 11 filing으로 tenant-support/rent-cliff mechanism이 현실화됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** Short 유지 가능. 다만 2016~18 squeeze/borrow cost를 버틸 position sizing이 필요했다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- 1. VIC SRG 2016-08-25 원문 — Value Investors Club / user SQL, 2016-08-25. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:579151a3-e1ec-4e8c-8d31-df091e33a77b -->
## 4. 2017-02-03 — Short rebuttal·JV/asset-value redevelopment Long

### 결론부터

**종합판정: 자산질 통찰은 있었으나 liquidity thesis 실패.** 자산가치와 financing timing의 싸움에서 자산가치만 더 정확히 계산해도 충분하지 않았다. 좋은 real estate가 bad balance sheet를 자동으로 고치지 않는다.

**주가·증권 결과:** 2017 ~$46.5 → 2024 ~$9.15. 장기 실패.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

### 5. 밸류에이션과 기대수익의 연결

개별 site/JV와 redevelopment yield를 stratified하게 평가해 단일 portfolio cap rate보다 훨씬 높은 NAV를 주장. Sears failure를 asset recapture catalyst로 해석. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Asset quality — 적중 · 논지 비중 18%

**당시 주장**

상위 site의 land/location value가 높다.

**당시 근거**

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

**이 주장이 성립하려면**

buyer/tenant demand

**사전 반증조건**

retail real-estate decline

**실제 결과**

일부 sales/JV로 확인.

**정량적 괴리**

주가 / $46.48 / NAV upside / 2024 ~$9.15

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Asset quality 가설은 'retail real-estate decline'를 사전 반증조건으로 저장한다.

#### 2. JV funding — 부분 · 논지 비중 18%

**당시 주장**

JV가 development capital burden을 낮춘다.

**당시 근거**

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

**이 주장이 성립하려면**

partners fund

**사전 반증조건**

JV pipeline insufficient

**실제 결과**

도움됐지만 전체 문제 해결 못함.

**정량적 괴리**

JV / funding source / capital-light redevelopment / 일부 실제 활용

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

JV funding 가설은 'JV pipeline insufficient'를 사전 반증조건으로 저장한다.

#### 3. Sears exit upside — 실패 · 논지 비중 16%

**당시 주장**

Sears 퇴거가 value unlock을 가속한다.

**당시 근거**

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

**이 주장이 성립하려면**

replacement tenants ready

**사전 반증조건**

mass vacancy

**실제 결과**

liquidity shock이 더 큼.

**정량적 괴리**

Asset sales / liquidity / redeploy / 후일 생존용 funding으로 전환

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Sears exit upside 가설은 'mass vacancy'를 사전 반증조건으로 저장한다.

#### 4. Asset sales — 부분 실패 · 논지 비중 16%

**당시 주장**

비핵심 매각으로 self-funding 가능하다.

**당시 근거**

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

**이 주장이 성립하려면**

sale prices/NAV

**사전 반증조건**

forced sale discount

**실제 결과**

후일 대량매각 필요.

**정량적 괴리**

Sears exit / catalyst / faster unlock / negative carry 급증

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Asset sales 가설은 'forced sale discount'를 사전 반증조건으로 저장한다.

#### 5. NAV — 실패 · 논지 비중 16%

**당시 주장**

stratified property values가 주가보다 높다.

**당시 근거**

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

**이 주장이 성립하려면**

time/cost modest

**사전 반증조건**

debt/carry eats NAV

**실제 결과**

equity 미실현.

**정량적 괴리**

2017 ~$46.5 → 2024 ~$9.15. 장기 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

NAV 가설은 'debt/carry eats NAV'를 사전 반증조건으로 저장한다.

#### 6. Long payoff — 실패 · 논지 비중 16%

**당시 주장**

Sears distress에도 주주가치가 커진다.

**당시 근거**

2016 Short가 Sears rent loss를 과장했고, 좋은 sites는 JVs·asset sales·new tenant rents로 충분히 자금을 조달할 수 있다고 반박했다. Sears가 빠지면 오히려 undervalued land를 더 빨리 monetize할 수 있다는 논리.

**이 주장이 성립하려면**

funding survives

**사전 반증조건**

cash burn

**실제 결과**

장기 실패.

**정량적 괴리**

2017 ~$46.5 → 2024 ~$9.15. 장기 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Long payoff 가설은 'cash burn'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Sears exit는 recapture를 가속했지만 동시에 rent loss·expense burden·CapEx need를 앞당겼다. Asset sales/JVs는 실제 funding source였으나 전체 development plan을 self-fund하기엔 부족해 Berkshire term loan과 후일 liquidation이 필요했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2017 ~$46.5 → 2024 ~$9.15. 장기 실패. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

자산가치와 financing timing의 싸움에서 자산가치만 더 정확히 계산해도 충분하지 않았다. 좋은 real estate가 bad balance sheet를 자동으로 고치지 않는다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-10-15 — Sears bankruptcy 직후 recapture가 선택권보다 liquidity burden으로 작동하기 시작했다. 회피 가능성: 매우 높음. Short rebuttal은 Sears failure 시 24개월 cash budget으로 검증했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

자산질 통찰은 있었으나 liquidity thesis 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $46.48 | NAV upside | 2024 ~$9.15 | 실패 |
| JV | funding source | capital-light redevelopment | 일부 실제 활용 | 부분 적중 |
| Asset sales | liquidity | redeploy | 후일 생존용 funding으로 전환 | 혼합 |
| Sears exit | catalyst | faster unlock | negative carry 급증 | 역효과 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-02-03 | VIC 아이디어 게시 | Short rebuttal·JV/asset-value redevelopment Long |
| 2018-10-15 | 최초 핵심 검증·반증 신호 | Sears bankruptcy 직후 recapture가 선택권보다 liquidity burden으로 작동하기 시작했다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2017 ~$46.5 → 2024 ~$9.15. 장기 실패. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2018-10-15 — Sears bankruptcy 직후 recapture가 선택권보다 liquidity burden으로 작동하기 시작했다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 매우 높음. Short rebuttal은 Sears failure 시 24개월 cash budget으로 검증했어야 한다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- 1. VIC SRG 2017-02-03 원문 — Value Investors Club / user SQL, 2017-02-03. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:8e876722-fd92-41bd-9cf0-8a653c2455e8 -->
## 5. 2018-05-23 — Property-level SOTP·$50 base/$60~70 long-term Long

### 결론부터

**종합판정: 단기 가격 성공·장기 thesis 실패.** 목표가에 도달했을 때 expected return을 다시 계산하지 않고 long-term NAV story로 연장하면 같은 분석이 성공에서 실패로 바뀐다. Property SOTP도 debt/time을 지속 업데이트해야 한다.

**주가·증권 결과:** 2018-08 한때 약 $51.48로 $50 base를 달성했지만 2024-01 $9.15. 단기 목표 성공·구조적 실패.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

### 5. 밸류에이션과 기대수익의 연결

Conservative property-level SOTP 약 $50, longer-term $60~70. 향후 6개월 내 1~3개 residential/mixed-use announcements를 기대. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Property SOTP — 부분 적중 · 논지 비중 18%

**당시 주장**

보수적 site별 NAV가 $50 이상이다.

**당시 근거**

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

**이 주장이 성립하려면**

sale/cap rate

**사전 반증조건**

capex/time leakage

**실제 결과**

단기 가격은 도달.

**정량적 괴리**

Entry / $41.66 / $50 / 2018-08 ~$51.48

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Property SOTP 가설은 'capex/time leakage'를 사전 반증조건으로 저장한다.

#### 2. Mixed-use option — 부분 · 논지 비중 18%

**당시 주장**

residential/office entitlement가 upside다.

**당시 근거**

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

**이 주장이 성립하려면**

zoning/partners

**사전 반증조건**

delays

**실제 결과**

일부 가치 있으나 전체 equity 못 살림.

**정량적 괴리**

Long-term / $60~70 / redevelopment / 2024 $9.15

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Mixed-use option 가설은 'delays'를 사전 반증조건으로 저장한다.

#### 3. Berkshire bridge — 부분 실패 · 논지 비중 16%

**당시 주장**

term financing이 redevelopment 시간을 준다.

**당시 근거**

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

**이 주장이 성립하려면**

loan runway

**사전 반증조건**

cash burn/maturity

**실제 결과**

후일 debt가 liquidation waterfall 핵심.

**정량적 괴리**

Mixed-use / 1~3 announcements / optionality / 일부 projects

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Berkshire bridge 가설은 'cash burn/maturity'를 사전 반증조건으로 저장한다.

#### 4. Sears transition — 실패 · 논지 비중 16%

**당시 주장**

tenant decline을 관리하며 redevelop한다.

**당시 근거**

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

**이 주장이 성립하려면**

staged closures

**사전 반증조건**

bankruptcy

**실제 결과**

2018 shock.

**정량적 괴리**

구조 / redevelopment REIT / compound / 2022 sale plan

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Sears transition 가설은 'bankruptcy'를 사전 반증조건으로 저장한다.

#### 5. $50 target — 강한 적중 · 논지 비중 16%

**당시 주장**

near-term rerating 가능.

**당시 근거**

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

**이 주장이 성립하려면**

market recognizes NAV

**사전 반증조건**

new shock

**실제 결과**

3개월 내 달성.

**정량적 괴리**

2018-08 한때 약 $51.48로 $50 base를 달성했지만 2024-01 $9.15. 단기 목표 성공·구조적 실패.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

$50 target 가설은 'new shock'를 사전 반증조건으로 저장한다.

#### 6. $60~70 — 실패 · 논지 비중 16%

**당시 주장**

장기 execution으로 더 상승.

**당시 근거**

Property를 quality별로 나눠 stabilized rent와 land/mixed-use optionality를 평가하면 $50 이상이고, residential entitlements가 장기 NAV를 더 높인다고 봤다. Berkshire financing도 liquidity bridge로 인식했다.

**이 주장이 성립하려면**

capital/funding

**사전 반증조건**

liquidation

**실제 결과**

실패.

**정량적 괴리**

2018-08 한때 약 $51.48로 $50 base를 달성했지만 2024-01 $9.15. 단기 목표 성공·구조적 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

$60~70 가설은 'liquidation'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

주가는 3개월 내 $50을 넘어 tactical target은 맞았다. 그러나 Sears bankruptcy와 cash burn 이후 장기 $60~70은 무너졌다. 2022 Plan of Sale로 redevelopment platform thesis가 종료됐다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2018-08 한때 약 $51.48로 $50 base를 달성했지만 2024-01 $9.15. 단기 목표 성공·구조적 실패. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

목표가에 도달했을 때 expected return을 다시 계산하지 않고 long-term NAV story로 연장하면 같은 분석이 성공에서 실패로 바뀐다. Property SOTP도 debt/time을 지속 업데이트해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-08-31 — 주가가 약 $51.5로 base target을 달성해 원 투자논지의 단기 margin of safety가 소진됐다. 회피 가능성: 매우 높음. $50 도달 시 resize/exit하고 long-term redevelopment는 새 thesis로 분리했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

단기 가격 성공·장기 thesis 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $41.66 | $50 | 2018-08 ~$51.48 | 단기 성공 |
| Long-term | $60~70 | redevelopment | 2024 $9.15 | 실패 |
| Mixed-use | 1~3 announcements | optionality | 일부 projects | 부분 |
| 구조 | redevelopment REIT | compound | 2022 sale plan | 전제변경 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-05-23 | VIC 아이디어 게시 | Property-level SOTP·$50 base/$60~70 long-term Long |
| 2018-08-31 | 최초 핵심 검증·반증 신호 | 주가가 약 $51.5로 base target을 달성해 원 투자논지의 단기 margin of safety가 소진됐다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2018-08 한때 약 $51.48로 $50 base를 달성했지만 2024-01 $9.15. 단기 목표 성공·구조적 실패. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2018-08-31 — 주가가 약 $51.5로 base target을 달성해 원 투자논지의 단기 margin of safety가 소진됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 매우 높음. $50 도달 시 resize/exit하고 long-term redevelopment는 새 thesis로 분리했어야 한다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- [1. VIC SRG 2018-05-23 원문](https://www.valueinvestorsclub.com/idea/SERITAGE_GROWTH_PROPERTIES/7892421607) — Value Investors Club / user SQL, 2018-05-23. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:05057479-11f0-4876-975c-f400ba470a3e -->
## 6. 2018-10-17 — Fraudulent-conveyance $500m~1.5bn existential Short

### 결론부터

**종합판정: 가격 성공·핵심 인과 실패.** 투자결과와 분석정확도를 분리해야 하는 대표 사례다. Short의 방향은 맞았지만 가장 강조한 causal mechanism의 magnitude가 틀렸다. '주가가 내렸다=논지가 맞았다'가 아니다.

**주가·증권 결과:** 2018-10 ~$38 → 2024-01 ~$9.15로 가격은 강하게 하락. 그러나 핵심 fraudulent-transfer 손실 추정은 크게 과대.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

Sears bankruptcy estate가 2015 SRG transaction을 fraudulent conveyance로 공격하면 $500m~$1.5bn 또는 그 이상 liability가 생겨 equity가 크게 훼손될 수 있다고 봄. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Fraudulent transfer — 실패 · 논지 비중 18%

**당시 주장**

2015 transaction이 avoidable transfer다.

**당시 근거**

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

**이 주장이 성립하려면**

estate proves insolvency/value gap

**사전 반증조건**

claims settle modestly

**실제 결과**

대형 clawback 없이 settlement.

**정량적 괴리**

Entry / $38.02 / large downside / 2024 $9.15

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Fraudulent transfer 가설은 'claims settle modestly'를 사전 반증조건으로 저장한다.

#### 2. Damage magnitude — 치명적 실패 · 논지 비중 18%

**당시 주장**

SRG liability $500m~1.5bn 가능.

**당시 근거**

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

**이 주장이 성립하려면**

joint/several exposure

**사전 반증조건**

limited contribution

**실제 결과**

약 $35m 수준.

**정량적 괴리**

Liability / $500m~1.5bn / existential / SRG defendants ~$35m contribution

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Damage magnitude 가설은 'limited contribution'를 사전 반증조건으로 저장한다.

#### 3. Liquidity — 부분 실패 · 논지 비중 16%

**당시 주장**

litigation이 financing을 막는다.

**당시 근거**

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

**이 주장이 성립하려면**

lenders fear claim

**사전 반증조건**

other funding/sales

**실제 결과**

더 큰 문제는 operating cash burn.

**정량적 괴리**

Sears / bankruptcy / litigation tail / settlement/release

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Liquidity 가설은 'other funding/sales'를 사전 반증조건으로 저장한다.

#### 4. Sears bankruptcy — 적중 · 논지 비중 16%

**당시 주장**

bankruptcy가 SRG 위험을 크게 높인다.

**당시 근거**

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

**이 주장이 성립하려면**

claims filed

**사전 반증조건**

estate benign

**실제 결과**

실제 event 발생.

**정량적 괴리**

실제 driver / litigation / equity impairment / debt/cash burn/liquidation

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Sears bankruptcy 가설은 'estate benign'를 사전 반증조건으로 저장한다.

#### 5. Short direction — 적중 · 논지 비중 16%

**당시 주장**

equity는 크게 하락한다.

**당시 근거**

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

**이 주장이 성립하려면**

multiple stresses

**사전 반증조건**

asset values rescue

**실제 결과**

가격은 크게 하락.

**정량적 괴리**

2018-10 ~$38 → 2024-01 ~$9.15로 가격은 강하게 하락. 그러나 핵심 fraudulent-transfer 손실 추정은 크게 과대.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Short direction 가설은 'asset values rescue'를 사전 반증조건으로 저장한다.

#### 6. Causal attribution — 실패 · 논지 비중 16%

**당시 주장**

하락의 핵심은 litigation이다.

**당시 근거**

Sears가 insolvency 상태에서 valuable real estate를 SRG에 낮은 가격으로 넘겼다면 creditors가 transfer를 되돌리거나 대형 damages를 청구할 수 있다고 주장했다. 이미 높은 redevelopment funding need에 litigation tail까지 붙으면 existential risk라고 봤다.

**이 주장이 성립하려면**

damages materialize

**사전 반증조건**

debt/capex dominates

**실제 결과**

틀림.

**정량적 괴리**

2018-10 ~$38 → 2024-01 ~$9.15로 가격은 강하게 하락. 그러나 핵심 fraudulent-transfer 손실 추정은 크게 과대.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Causal attribution 가설은 'debt/capex dominates'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Sears-related litigation은 실제 존재했지만 2022 settlement에서 관련 Seritage defendants의 contribution은 약 $35m 수준이었고 claims가 release됐다. 주가는 크게 하락했지만 원인은 redevelopment cash burn, debt, asset-sale/liquidation dynamics가 더 중요했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2018-10 ~$38 → 2024-01 ~$9.15로 가격은 강하게 하락. 그러나 핵심 fraudulent-transfer 손실 추정은 크게 과대. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

투자결과와 분석정확도를 분리해야 하는 대표 사례다. Short의 방향은 맞았지만 가장 강조한 causal mechanism의 magnitude가 틀렸다. '주가가 내렸다=논지가 맞았다'가 아니다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-08-17 — Sears litigation settlement 규모와 Seritage 측 contribution이 약 $35m으로 구체화돼 $500m~1.5bn existential-liability 가정이 반증됐다. 회피 가능성: 매우 높음. 법률 claim은 damages probability×recoverability를 따로 모델링하고 가격하락의 실제 driver와 구분해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

가격 성공·핵심 인과 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $38.02 | large downside | 2024 $9.15 | 가격 적중 |
| Liability | $500m~1.5bn | existential | SRG defendants ~$35m contribution | 인과 실패 |
| Sears | bankruptcy | litigation tail | settlement/release | event 종료 |
| 실제 driver | litigation | equity impairment | debt/cash burn/liquidation | 오판 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-10-17 | VIC 아이디어 게시 | Fraudulent-conveyance $500m~1.5bn existential Short |
| 2022-08-17 | 최초 핵심 검증·반증 신호 | Sears litigation settlement 규모와 Seritage 측 contribution이 약 $35m으로 구체화돼 $500m~1.5bn existential-liability 가정이 반증됐다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2018-10 ~$38 → 2024-01 ~$9.15로 가격은 강하게 하락. 그러나 핵심 fraudulent-transfer 손실 추정은 크게 과대. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2022-08-17 — Sears litigation settlement 규모와 Seritage 측 contribution이 약 $35m으로 구체화돼 $500m~1.5bn existential-liability 가정이 반증됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 매우 높음. 법률 claim은 damages probability×recoverability를 따로 모델링하고 가격하락의 실제 driver와 구분해야 했다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- [1. VIC SRG 2018-10-17 원문](https://www.valueinvestorsclub.com/idea/SERITAGE_GROWTH_PROPERTIES/8318662187) — Value Investors Club / user SQL, 2018-10-17. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:1a3f1210-7f54-4821-8f39-ac1f50e32d0d -->
## 7. 2018-11-01 — Fraudulent-conveyance rebuttal·asset-value Long

### 결론부터

**종합판정: 법률판단 적중·증권 Long 실패.** 반대편 Short의 가장 약한 논점을 정확히 반박해도 Long 전체가 성립하는 것은 아니다. 'A라는 bear case가 틀렸다'와 '주식이 싸다' 사이에는 다른 downside mechanisms가 남는다.

**주가·증권 결과:** 2018-11 ~$37.94 → 2024-01 ~$9.15. 법률 rebuttal은 맞았지만 Long은 실패.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

Fraudulent-conveyance claim이 intrinsic value를 크게 훼손하지 않는다고 보고 기존 property-level NAV와 redevelopment optionality를 유지. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Legal rebuttal — 적중 · 논지 비중 18%

**당시 주장**

fraudulent-conveyance tail이 과장됐다.

**당시 근거**

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

**이 주장이 성립하려면**

transaction defenses

**사전 반증조건**

large judgment

**실제 결과**

modest settlement.

**정량적 괴리**

Entry / $37.94 / NAV recovery / 2024 $9.15

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Legal rebuttal 가설은 'large judgment'를 사전 반증조건으로 저장한다.

#### 2. Asset quality — 적중 · 논지 비중 18%

**당시 주장**

부동산 자체가 valuable하다.

**당시 근거**

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

**이 주장이 성립하려면**

buyers

**사전 반증조건**

market weakness

**실제 결과**

매각 proceeds 실재.

**정량적 괴리**

Litigation / 대형 liability 낮음 / manageable / 2022 ~$35m contribution

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Asset quality 가설은 'market weakness'를 사전 반증조건으로 저장한다.

#### 3. Legal=equity floor — 실패 · 논지 비중 16%

**당시 주장**

법률 tail 제거가 주가하방을 막는다.

**당시 근거**

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

**이 주장이 성립하려면**

other risks modest

**사전 반증조건**

debt/cash burn

**실제 결과**

주가 급락.

**정량적 괴리**

NAV / 높은 asset value / equity floor / debt/time leakage

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Legal=equity floor 가설은 'debt/cash burn'를 사전 반증조건으로 저장한다.

#### 4. Funding — 부분 실패 · 논지 비중 16%

**당시 주장**

Berkshire loan/asset sales가 runway를 준다.

**당시 근거**

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

**이 주장이 성립하려면**

sales timely

**사전 반증조건**

cash burn

**실제 결과**

eventually liquidation.

**정량적 괴리**

구조 / redevelopment / normalization / liquidation

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Funding 가설은 'cash burn'를 사전 반증조건으로 저장한다.

#### 5. Redevelopment — 실패 · 논지 비중 16%

**당시 주장**

bankruptcy 후에도 project yields가 가치창출.

**당시 근거**

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

**이 주장이 성립하려면**

capital available

**사전 반증조건**

forced sale

**실제 결과**

scale-down.

**정량적 괴리**

2018-11 ~$37.94 → 2024-01 ~$9.15. 법률 rebuttal은 맞았지만 Long은 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Redevelopment 가설은 'forced sale'를 사전 반증조건으로 저장한다.

#### 6. Long payoff — 실패 · 논지 비중 16%

**당시 주장**

bear legal thesis가 틀리면 주가 회복.

**당시 근거**

Sears transaction은 independent board/rights offering와 valuation process를 거쳤고 fraudulent conveyance로 거액을 토해낼 가능성이 낮다고 반박했다. 따라서 bankruptcy 이후 주가하락은 좋은 real-estate assets를 과도하게 할인한 기회라고 봤다.

**이 주장이 성립하려면**

legal risk dominant

**사전 반증조건**

other mechanisms dominate

**실제 결과**

실패.

**정량적 괴리**

2018-11 ~$37.94 → 2024-01 ~$9.15. 법률 rebuttal은 맞았지만 Long은 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Long payoff 가설은 'other mechanisms dominate'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2022 settlement 규모가 약 $35m contribution으로 끝나 법률 rebuttal 방향은 맞았다. 하지만 그 사실이 equity를 구하지 못했다. 재개발 funding·interest·asset-sale discounts와 liquidation으로 주가는 크게 하락했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2018-11 ~$37.94 → 2024-01 ~$9.15. 법률 rebuttal은 맞았지만 Long은 실패. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

반대편 Short의 가장 약한 논점을 정확히 반박해도 Long 전체가 성립하는 것은 아니다. 'A라는 bear case가 틀렸다'와 '주식이 싸다' 사이에는 다른 downside mechanisms가 남는다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-12-31 — litigation이 existential 수준으로 확대되지 않아 법률 claim은 맞는 방향이었지만 ongoing cash burn과 debt가 Long의 새로운 핵심 falsifier가 됐다. 회피 가능성: 매우 높음. legal rebuttal 뒤 corporate cash-flow thesis를 독립적으로 다시 썼어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

법률판단 적중·증권 Long 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $37.94 | NAV recovery | 2024 $9.15 | 주식 실패 |
| Litigation | 대형 liability 낮음 | manageable | 2022 ~$35m contribution | 법률 적중 |
| NAV | 높은 asset value | equity floor | debt/time leakage | 실패 |
| 구조 | redevelopment | normalization | liquidation | 전제변경 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-11-01 | VIC 아이디어 게시 | Fraudulent-conveyance rebuttal·asset-value Long |
| 2020-12-31 | 최초 핵심 검증·반증 신호 | litigation이 existential 수준으로 확대되지 않아 법률 claim은 맞는 방향이었지만 ongoing cash burn과 debt가 Long의 새로운 핵심 falsifier가 됐다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2018-11 ~$37.94 → 2024-01 ~$9.15. 법률 rebuttal은 맞았지만 Long은 실패. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2020-12-31 — litigation이 existential 수준으로 확대되지 않아 법률 claim은 맞는 방향이었지만 ongoing cash burn과 debt가 Long의 새로운 핵심 falsifier가 됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 매우 높음. legal rebuttal 뒤 corporate cash-flow thesis를 독립적으로 다시 썼어야 한다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- [1. VIC SRG 2018-11-01 원문](https://www.valueinvestorsclub.com/idea/SERITAGE_GROWTH_PROPERTIES/5144211202) — Value Investors Club / user SQL, 2018-11-01. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---

<!-- idea:aa0781bf-6327-4085-9bed-8e5ca6c9e484 -->
## 8. 2022-03-10 — $1.44bn Berkshire loan·liquidity/equity-zero Short

### 결론부터

**종합판정: 전술적 가격 성공·zero thesis 실패.** Debt waterfall과 cash burn을 본 것은 정확했지만 gross asset-sale proceeds와 liquidation optionality를 너무 낮게 봤다. Distressed real-estate Short에서는 refinance만이 아니라 asset sale로 debt를 갚는 경로도 모델링해야 한다.

**주가·증권 결과:** 2022 중 $5대까지 하락해 tactical Short 성공, 2024-01 $9.15. Equity-zero는 cutoff까지 실패.

**Thesis / Process 점수:** 4.5 / 4.8

### 1. 무슨 기업인가

Seritage Growth Properties는 2015년 Sears Holdings가 보유·임차하던 미국 쇼핑몰·독립형 부동산을 분리해 만든 REIT다. 초기 자산의 핵심 특징은 좋은 상권·넓은 토지를 갖고 있지만 Sears/Kmart가 매우 낮은 임대료를 내고 있다는 점이었다. 투자논지는 Sears 공간을 recapture한 뒤 철거·재개발하고 Whole Foods, Nordstrom Rack, restaurants, offices, residential 등 더 생산적인 용도로 전환하면 평방피트당 임대료와 토지가치가 크게 오른다는 것이었다. 문제는 이 가치차익이 즉시 현금화되지 않는다는 데 있다. Sears가 빠져나가면 기존 rent가 먼저 사라지고, entitlement·tenant improvement·construction에 수년과 거액의 CapEx가 든 뒤에야 새 rent가 열린다. 그래서 재개발 속도보다 Sears 퇴거가 빠르면 EBITDA와 liquidity가 먼저 악화되는 J-curve가 생긴다. 2018년 Sears bankruptcy 이후 이 문제가 심해졌고, Berkshire Hathaway term loan과 지속적인 자산매각에 의존했다. 2022년 주주들은 Plan of Sale을 승인해 성장형 REIT가 아니라 자산을 매각하고 부채를 상환한 뒤 잔여가치를 분배하는 liquidation vehicle로 사실상 전환했다. 핵심 KPI는 wholly-owned/JV property 수, leased·occupied GLA, signed-not-open rent, redevelopment pipeline·cost/yield, annual asset-sale proceeds, cash burn, term-loan balance·maturity와 net distributable liquidation value다.

### 2. 산업 가치사슬과 돈의 흐름

Seritage의 원 경제모델은 '저임대 Sears 공간 recapture → entitlement/design → redevelopment CapEx → 더 높은 third-party rent → 낮은 cap rate로 재평가'다. 예를 들어 기존 Sears rent가 $4~5/sqft이고 새 tenant rent가 $15~30라면 잠재 NOI uplift는 매우 커 보인다. 그러나 새 rent에는 landlord construction, tenant allowance, leasing commissions, carrying cost와 몇 년의 공실기간이 선행된다. 따라서 단순히 stabilized NOI/cap rate를 적용한 NAV에서 아직 써야 할 CapEx, interest, corporate overhead, taxes와 execution time을 차감해야 한다. 2022 이후에는 가치사슬이 바뀌어 'property sale gross proceeds → transaction costs/taxes → Berkshire term-loan repayment → wind-down costs → shareholder distributions'가 핵심이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Seritage에는 전통적인 브랜드 moat가 없다. 강점은 개별 site의 location, acreage, zoning/entitlement potential과 mall owner/JV partners와의 redevelopment optionality다. 하지만 real estate는 location이 좋아도 capital structure가 나쁘면 equity가 시간과 이자에 의해 희석될 수 있다. 또 appraised/stabilized value는 거래가치가 아니며, 대규모 portfolio를 기한 내 팔면 buyer pool과 financing conditions에 따라 discount가 커질 수 있다. 따라서 NAV 투자에서 '좋은 땅'이라는 질적 판단을 debt maturity·remaining CapEx·cash burn·sale velocity와 동시에 본다.

### 4. 당시 VIC 원문과 핵심 숫자

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Berkshire term loan 약 $1.44bn, July-2023 maturity; principal을 $800m까지 낮추면 July-2025 extension 가능. Equity market cap 약 $685m. Mostly vacant/redevelopment portfolio와 cash burn 때문에 restructure 시 common recovery가 매우 낮다고 봄. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Maturity wall — 실패 · 논지 비중 18%

**당시 주장**

July-2023 loan이 existential이다.

**당시 근거**

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

**이 주장이 성립하려면**

no sales/refi

**사전 반증조건**

asset-sale proceeds

**실제 결과**

대규모 paydown으로 완화.

**정량적 괴리**

Entry / $12.66 / equity≈0 / 2024 $9.15

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Maturity wall 가설은 'asset-sale proceeds'를 사전 반증조건으로 저장한다.

#### 2. Cash burn — 적중 · 논지 비중 18%

**당시 주장**

vacancy/redevelopment가 cash를 소모한다.

**당시 근거**

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

**이 주장이 성립하려면**

NOI weak

**사전 반증조건**

cost cuts/sales

**실제 결과**

실제 부담 지속.

**정량적 괴리**

Term loan / ~$1.44bn / maturity stress / 2023 $670m paydown

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Cash burn 가설은 'cost cuts/sales'를 사전 반증조건으로 저장한다.

#### 3. Asset-sale insufficiency — 실패 · 논지 비중 16%

**당시 주장**

매각만으로 debt를 못 갚는다.

**당시 근거**

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

**이 주장이 성립하려면**

buyers discount assets

**사전 반증조건**

large proceeds

**실제 결과**

2022~23 $1.35bn+ gross sales.

**정량적 괴리**

2022 sales / 불확실 / insufficient / 65 props/$650.3m

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Asset-sale insufficiency 가설은 'large proceeds'를 사전 반증조건으로 저장한다.

#### 4. Debt priority — 적중 · 논지 비중 16%

**당시 주장**

Berkshire가 equity보다 먼저 회수한다.

**당시 근거**

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

**이 주장이 성립하려면**

waterfall

**사전 반증조건**

asset value far exceeds debt

**실제 결과**

우선순위는 맞고 paydown 진행.

**정량적 괴리**

2023 sales / 불확실 / distress / 60 props/$702m

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Debt priority 가설은 'asset value far exceeds debt'를 사전 반증조건으로 저장한다.

#### 5. Tactical downside — 적중 · 논지 비중 16%

**당시 주장**

주가는 추가 급락한다.

**당시 근거**

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

**이 주장이 성립하려면**

liquidity fear

**사전 반증조건**

sale catalyst

**실제 결과**

2022 $5대까지 하락.

**정량적 괴리**

2022 중 $5대까지 하락해 tactical Short 성공, 2024-01 $9.15. Equity-zero는 cutoff까지 실패.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Tactical downside 가설은 'sale catalyst'를 사전 반증조건으로 저장한다.

#### 6. Equity zero — 실패 · 논지 비중 16%

**당시 주장**

restructure로 common recovery 거의 0.

**당시 근거**

SRG는 operating cash flow보다 redevelopment/interest cash burn이 크고 loan maturity가 equity를 압박한다. 자산매각이 충분히 빠르지 않으면 Berkshire debt가 common보다 우선해 restructuring/equity-zero가 가능하다고 주장했다.

**이 주장이 성립하려면**

asset sales fail

**사전 반증조건**

orderly liquidation

**실제 결과**

cutoff까지 미실현.

**정량적 괴리**

2022 중 $5대까지 하락해 tactical Short 성공, 2024-01 $9.15. Equity-zero는 cutoff까지 실패.

**분석 오류·핵심**

gross NAV/event value와 common equity 사이의 funding·time·probability를 과소반영했다.

**재사용할 교훈**

Equity zero 가설은 'orderly liquidation'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2022 Plan of Sale이 승인됐고 회사는 대규모 자산매각을 통해 debt를 줄였다. 2022 65 properties를 $650.3m, 2023 60 properties를 $702m에 팔고 2023 term loan을 $670m 상환했다. Equity는 크게 약해졌지만 2024-01에도 약 $9.15로 남아 zero/restructure는 실현되지 않았다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2022 중 $5대까지 하락해 tactical Short 성공, 2024-01 $9.15. Equity-zero는 cutoff까지 실패. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

Debt waterfall과 cash burn을 본 것은 정확했지만 gross asset-sale proceeds와 liquidation optionality를 너무 낮게 봤다. Distressed real-estate Short에서는 refinance만이 아니라 asset sale로 debt를 갚는 경로도 모델링해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-10-24 — 주주가 Plan of Sale을 승인하면서 '재구조화로 common wipeout' 대신 orderly asset liquidation이라는 대체경로가 공식화됐다. 회피 가능성: 높음. Plan approval와 실제 sale proceeds가 NAV보다 나쁘지 않은지 확인하며 zero probability를 낮췄어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

전술적 가격 성공·zero thesis 실패. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $12.66 | equity≈0 | 2024 $9.15 | zero 실패 |
| Term loan | ~$1.44bn | maturity stress | 2023 $670m paydown | 위험 완화 |
| 2022 sales | 불확실 | insufficient | 65 props/$650.3m | 반증 |
| 2023 sales | 불확실 | distress | 60 props/$702m | 반증 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2022-03-10 | VIC 아이디어 게시 | $1.44bn Berkshire loan·liquidity/equity-zero Short |
| 2022-10-24 | 최초 핵심 검증·반증 신호 | 주주가 Plan of Sale을 승인하면서 '재구조화로 common wipeout' 대신 orderly asset liquidation이라는 대체경로가 공식화됐다. |
| 2018-10-15 | Sears Chapter 11 | low-rent upside가 rent-cliff/capex shock으로 전환 |
| 2022-10-24 | Plan of Sale 승인 | growth REIT→liquidation vehicle로 regime change |
| 2023-12-31 | 대규모 자산매각 | 2023 60 properties/$702m, term loan $670m paydown |
| 2024-01-31 | 고정 평가기준일 | 2022 중 $5대까지 하락해 tactical Short 성공, 2024-01 $9.15. Equity-zero는 cutoff까지 실패. |

### Failure / Success Anatomy

- **근본 오류:** gross real-estate/legal value를 CapEx·time·debt·probability·distribution leakage 없이 common equity value로 직접 연결
- **최초 검증·반증 신호:** 2022-10-24 — 주주가 Plan of Sale을 승인하면서 '재구조화로 common wipeout' 대신 orderly asset liquidation이라는 대체경로가 공식화됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 높음. Plan approval와 실제 sale proceeds가 NAV보다 나쁘지 않은지 확인하며 zero probability를 낮췄어야 한다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- [1. VIC SRG 2022-03-10 원문](https://www.valueinvestorsclub.com/idea/SERITAGE_GROWTH_PROPERTIES/1598112691) — Value Investors Club / user SQL, 2022-03-10. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Seritage 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1628063/000095017024039550/srg-20231231.htm) — SEC, 2024-04-04. 2023 asset sales, impairments, term-loan paydown·liquidation status 확인
- [3. Seritage Plan of Sale preliminary proxy](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Files-Preliminary-Proxy-Materials/default.aspx) — Seritage, 2022-07-07. 전 자산 매각·분배·dissolution 계획 확인
- [4. Seritage Q3 2022 results](https://ir.seritage.com/news/news-details/2022/Seritage-Growth-Properties-Reports-Third-Quarter-2022-Operating-Results/default.aspx) — Seritage, 2022-11-08. Plan approval·asset-sale/debt progress와 Sears litigation settlement 확인
- [5. Seritage historical prices](https://www.digrin.com/stocks/detail/SRG/price) — Digrin, 2024-01-31. 2015~2024 가격경로 확인
- [6. Seritage Investor Relations](https://ir.seritage.com/) — Seritage, 2024-01-31. historical filings·asset-sale updates

---
# GYRODYNE COMPANY OF AMERICA / GYRODYNE LLC (GYRO) — 기업과 비즈니스

## 1. 무슨 기업인가

Gyrodyne은 과거 헬리콥터 제조기업이었지만 투자시점에는 Long Island 부동산과 뉴욕주의 수용(eminent domain) 소송 결과가 사실상 기업가치의 대부분을 결정하는 초소형 자산주였다. 뉴욕주는 2005년 Stony Brook 인근 Flowerfield 부지 약 245.5 acres를 수용했고 Gyrodyne은 보상액이 현저히 낮다며 소송했다. 2010년 Court of Claims가 회사에 총 $125m 수준의 가치를 인정해 기존 지급액을 제외한 약 $98.685m 추가보상과 2005년부터 연 9% statutory interest를 판결했다. 뉴욕주가 항소하면서 주가는 '승소확률 × 최종 cash award + 남은 부동산 NAV − 세금·비용'의 이벤트드리븐 증권이 됐다. 상급심에서 회사가 승소한 뒤 2012년 약 $167.5m을 실제 수령했고, 2013년 이사회는 liquidation을 승인해 특별배당과 잔여 부동산 청산으로 전환했다. 핵심 KPI는 각 법원단계, award principal, statutory interest accrual, tax treatment, cash receipt, special distributions, remaining property NAV와 liquidation costs다.

## 2. 산업 가치사슬과 돈의 흐름

Gyrodyne의 valuation은 operating earnings가 아니라 확률가중 expected value다. 소송 승소 시 받을 principal과 매일 쌓이는 9% interest를 계산하고, 패소/감액 시나리오와 remaining real-estate value를 더한다. 실제 현금 수령 후에는 세금·법률비·분배정책을 차감한다. 중요한 점은 법원 판결가가 주주가치가 되는 순간은 판결일이 아니라 appeal이 끝나고 정부에서 cash가 들어와 board가 배당·liquidation을 결정할 때라는 것이다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Gyrodyne의 edge는 사업경쟁력이 아니라 정보구조에 있었다. 법원 판결문·감정가·법정 statutory interest·remaining land를 제대로 읽으면 equity expected value를 시장보다 정밀하게 계산할 수 있었다. 반면 microcap liquidity, tax, appeal duration과 management liquidation intent가 큰 위험이었다. 이런 litigation asset은 '법적으로 이길 것 같다'가 아니라 base asset floor, appeal probability, time value와 실제 distribution waterfall까지 모델링해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2010-07-01 | Long | Long | Court-award liquidation $129 low/$195 upside Long | 2012 뉴욕주로부터 약 $167.5m 현금 수령, 2013 $66.56 특별배당과 추가 cash/property interests로 value crystallization. 강한 성공. | 전설적 성공 |
| 2011-10-25 | Long | Long | 90% appeal win·$145 EV Long | 2012 cash award 수령과 2013 liquidation 결정으로 expected-value thesis가 크게 성공. | 전설적 성공 |

---

<!-- idea:6a79fc21-73dd-4c36-a58a-c909c700ef1d -->
## 1. 2010-07-01 — Court-award liquidation $129 low/$195 upside Long

### 결론부터

**종합판정: 전설적 성공.** 법원 판결·statutory interest·remaining NAV를 하나의 expected-value waterfall로 만든 좋은 event-driven 분석이다. Appeal time이 비용이면서도 9% interest 때문에 부분적으로 보상된다는 비대칭이 강했다.

**주가·증권 결과:** 2012 뉴욕주로부터 약 $167.5m 현금 수령, 2013 $66.56 특별배당과 추가 cash/property interests로 value crystallization. 강한 성공.

**Thesis / Process 점수:** 9.7 / 9.4

### 1. 무슨 기업인가

Gyrodyne은 과거 헬리콥터 제조기업이었지만 투자시점에는 Long Island 부동산과 뉴욕주의 수용(eminent domain) 소송 결과가 사실상 기업가치의 대부분을 결정하는 초소형 자산주였다. 뉴욕주는 2005년 Stony Brook 인근 Flowerfield 부지 약 245.5 acres를 수용했고 Gyrodyne은 보상액이 현저히 낮다며 소송했다. 2010년 Court of Claims가 회사에 총 $125m 수준의 가치를 인정해 기존 지급액을 제외한 약 $98.685m 추가보상과 2005년부터 연 9% statutory interest를 판결했다. 뉴욕주가 항소하면서 주가는 '승소확률 × 최종 cash award + 남은 부동산 NAV − 세금·비용'의 이벤트드리븐 증권이 됐다. 상급심에서 회사가 승소한 뒤 2012년 약 $167.5m을 실제 수령했고, 2013년 이사회는 liquidation을 승인해 특별배당과 잔여 부동산 청산으로 전환했다. 핵심 KPI는 각 법원단계, award principal, statutory interest accrual, tax treatment, cash receipt, special distributions, remaining property NAV와 liquidation costs다.

### 2. 산업 가치사슬과 돈의 흐름

Gyrodyne의 valuation은 operating earnings가 아니라 확률가중 expected value다. 소송 승소 시 받을 principal과 매일 쌓이는 9% interest를 계산하고, 패소/감액 시나리오와 remaining real-estate value를 더한다. 실제 현금 수령 후에는 세금·법률비·분배정책을 차감한다. 중요한 점은 법원 판결가가 주주가치가 되는 순간은 판결일이 아니라 appeal이 끝나고 정부에서 cash가 들어와 board가 배당·liquidation을 결정할 때라는 것이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Gyrodyne의 edge는 사업경쟁력이 아니라 정보구조에 있었다. 법원 판결문·감정가·법정 statutory interest·remaining land를 제대로 읽으면 equity expected value를 시장보다 정밀하게 계산할 수 있었다. 반면 microcap liquidity, tax, appeal duration과 management liquidation intent가 큰 위험이었다. 이런 litigation asset은 '법적으로 이길 것 같다'가 아니라 base asset floor, appeal probability, time value와 실제 distribution waterfall까지 모델링해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Price $75. Trial win을 반영한 low-case liquidation 약 $129, upside 약 $195. Court award: $98.685m additional damages + 당시 약 $40.4m accrued interest, 연 9% simple interest가 appeal 중 계속 누적. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. Trial award — 강한 적중 · 논지 비중 18%

**당시 주장**

$98.685m additional award가 유지된다.

**당시 근거**

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

**이 주장이 성립하려면**

appeal affirm

**사전 반증조건**

reversal

**실제 결과**

상급심 유지.

**정량적 괴리**

Entry / $75 / low $129 / upside $195 / large cash/distributions

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Trial award 가설은 'reversal'를 사전 반증조건으로 저장한다.

#### 2. 9% interest — 적중 · 논지 비중 18%

**당시 주장**

appeal 중 statutory interest가 가치 누적.

**당시 근거**

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

**이 주장이 성립하려면**

법정금리 적용

**사전 반증조건**

interest tolled

**실제 결과**

실제 큰 추가수령.

**정량적 괴리**

Damages / $98.685m / 유지 / 수령

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

9% interest 가설은 'interest tolled'를 사전 반증조건으로 저장한다.

#### 3. Base assets — 적중 · 논지 비중 16%

**당시 주장**

remaining real estate가 downside floor다.

**당시 근거**

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

**이 주장이 성립하려면**

property NAV

**사전 반증조건**

liabilities/tax

**실제 결과**

추가 liquidation interests로 남음.

**정량적 괴리**

Interest / ~$40.4m +9% / 계속 누적 / 총 수령액 $167.53m

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Base assets 가설은 'liabilities/tax'를 사전 반증조건으로 저장한다.

#### 4. Appeal probability — 적중 · 논지 비중 16%

**당시 주장**

state appeal에도 승소확률이 높다.

**당시 근거**

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

**이 주장이 성립하려면**

record/law

**사전 반증조건**

reversal

**실제 결과**

승소 유지.

**정량적 괴리**

Special dividend / 미정 / liquidation / $66.56/share

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Appeal probability 가설은 'reversal'를 사전 반증조건으로 저장한다.

#### 5. Distribution — 강한 적중 · 논지 비중 16%

**당시 주장**

board가 cash를 주주에게 돌린다.

**당시 근거**

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

**이 주장이 성립하려면**

liquidation orientation

**사전 반증조건**

empire building

**실제 결과**

2013 liquidation/special dividend.

**정량적 괴리**

2012 뉴욕주로부터 약 $167.5m 현금 수령, 2013 $66.56 특별배당과 추가 cash/property interests로 value crystallization. 강한 성공.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Distribution 가설은 'empire building'를 사전 반증조건으로 저장한다.

#### 6. $129/$195 — 적중 · 논지 비중 16%

**당시 주장**

expected liquidation value가 $75보다 훨씬 높다.

**당시 근거**

뉴욕주가 Flowerfield 부지를 수용한 보상액에 대한 소송에서 Gyrodyne가 1심에서 크게 승소했고 statutory interest 때문에 appeal duration 자체도 가치가 증가한다고 봤다. Remaining properties가 downside floor를 제공하고 경영진이 최종 cash를 분배할 가능성이 높다고 주장했다.

**이 주장이 성립하려면**

cash receipt/tax

**사전 반증조건**

large leakage

**실제 결과**

가치 crystallization 성공.

**정량적 괴리**

2012 뉴욕주로부터 약 $167.5m 현금 수령, 2013 $66.56 특별배당과 추가 cash/property interests로 value crystallization. 강한 성공.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

$129/$195 가설은 'large leakage'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

상급심에서 회사 승소가 유지됐고 2012년 뉴욕주로부터 총 약 $167.53m을 수령했다. 2013 board가 liquidation을 승인하고 $98.685m, 주당 $66.56 특별배당을 지급했으며 추가 cash 약 $45.86/share와 property interests를 분배하는 구조로 전환했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2012 뉴욕주로부터 약 $167.5m 현금 수령, 2013 $66.56 특별배당과 추가 cash/property interests로 value crystallization. 강한 성공. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

법원 판결·statutory interest·remaining NAV를 하나의 expected-value waterfall로 만든 좋은 event-driven 분석이다. Appeal time이 비용이면서도 9% interest 때문에 부분적으로 보상된다는 비대칭이 강했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-07-05 — 뉴욕주로부터 약 $167.53m 실제 cash를 수령하며 legal expected value가 balance-sheet cash로 전환됐다. 회피 가능성: 해당 없음. 수령 후에는 tax와 distribution timing을 새 모델로 바꿔야 했다.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $75 | low $129 / upside $195 | large cash/distributions | 강한 적중 |
| Damages | $98.685m | 유지 | 수령 | 적중 |
| Interest | ~$40.4m +9% | 계속 누적 | 총 수령액 $167.53m | 강한 적중 |
| Special dividend | 미정 | liquidation | $66.56/share | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2010-07-01 | VIC 아이디어 게시 | Court-award liquidation $129 low/$195 upside Long |
| 2012-07-05 | 핵심 법률 검증 | appeal/cash-receipt thesis 업데이트 |
| 2012-07-05 | 뉴욕주 현금수령 | 총 약 $167.53m award/interest가 현금화 |
| 2013-09-12 | Liquidation 승인 | 법률가치가 distribution thesis로 전환 |
| 2013-12-30 | Special dividend | $66.56/share 대규모 현금분배 |
| 2024-01-31 | 사후평가 | 법률 expected value→현금분배 성공 판정 |

### Failure / Success Anatomy

- **근본 오류:** event payoff를 probability×cash waterfall로 분해
- **최초 검증·반증 신호:** 2012-07-05 — 뉴욕주로부터 약 $167.53m 실제 cash를 수령하며 legal expected value가 balance-sheet cash로 전환됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 해당 없음. 수령 후에는 tax와 distribution timing을 새 모델로 바꿔야 했다.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- [1. VIC GYRO 2010-07-01 원문](https://www.valueinvestorsclub.com/idea/GYRODYNE_CO_OF_AMERICA_INC/8115113073) — Value Investors Club / user SQL, 2010-07-01. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Gyrodyne 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/44689/000143774915006464/gyro20141231_10k.htm) — SEC, 2015-03-31. Court award, $167.53m receipt, 2013 liquidation/special dividend 확인
- [3. Gyrodyne 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1589061/000143774916028641/gyrllc20151231_10k.htm) — SEC, 2016-03-31. liquidation structure·remaining property interests 확인
- [4. Gyrodyne appeal update 8-K](https://www.sec.gov/Archives/edgar/data/44689/000143774912002806/gyrodyne_8k-032712.htm) — SEC, 2012-03-27. appeal judgment·award and statutory interest 확인
- [5. Gyrodyne SEC filings](https://www.sec.gov/edgar/browse/?CIK=44689) — SEC, 2024-01-31. litigation·distribution historical filings
- [6. Gyrodyne liquidation history](https://www.sec.gov/Archives/edgar/data/44689/000143774915006464/gyro20141231_10k.htm) — SEC, 2015-03-31. $66.56 special dividend와 후속 distribution 구조 확인

---

<!-- idea:acb10951-9704-4f4d-8b7d-52ef2b342f0f -->
## 2. 2011-10-25 — 90% appeal win·$145 EV Long

### 결론부터

**종합판정: 전설적 성공.** binary event의 확률뿐 아니라 패소 시 base NAV와 승소 시 time-accreting interest를 함께 계산한 것이 좋았다. Expected value뿐 아니라 path-dependent carry가 투자자 편이었다.

**주가·증권 결과:** 2012 cash award 수령과 2013 liquidation 결정으로 expected-value thesis가 크게 성공.

**Thesis / Process 점수:** 9.7 / 9.4

### 1. 무슨 기업인가

Gyrodyne은 과거 헬리콥터 제조기업이었지만 투자시점에는 Long Island 부동산과 뉴욕주의 수용(eminent domain) 소송 결과가 사실상 기업가치의 대부분을 결정하는 초소형 자산주였다. 뉴욕주는 2005년 Stony Brook 인근 Flowerfield 부지 약 245.5 acres를 수용했고 Gyrodyne은 보상액이 현저히 낮다며 소송했다. 2010년 Court of Claims가 회사에 총 $125m 수준의 가치를 인정해 기존 지급액을 제외한 약 $98.685m 추가보상과 2005년부터 연 9% statutory interest를 판결했다. 뉴욕주가 항소하면서 주가는 '승소확률 × 최종 cash award + 남은 부동산 NAV − 세금·비용'의 이벤트드리븐 증권이 됐다. 상급심에서 회사가 승소한 뒤 2012년 약 $167.5m을 실제 수령했고, 2013년 이사회는 liquidation을 승인해 특별배당과 잔여 부동산 청산으로 전환했다. 핵심 KPI는 각 법원단계, award principal, statutory interest accrual, tax treatment, cash receipt, special distributions, remaining property NAV와 liquidation costs다.

### 2. 산업 가치사슬과 돈의 흐름

Gyrodyne의 valuation은 operating earnings가 아니라 확률가중 expected value다. 소송 승소 시 받을 principal과 매일 쌓이는 9% interest를 계산하고, 패소/감액 시나리오와 remaining real-estate value를 더한다. 실제 현금 수령 후에는 세금·법률비·분배정책을 차감한다. 중요한 점은 법원 판결가가 주주가치가 되는 순간은 판결일이 아니라 appeal이 끝나고 정부에서 cash가 들어와 board가 배당·liquidation을 결정할 때라는 것이다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Gyrodyne의 edge는 사업경쟁력이 아니라 정보구조에 있었다. 법원 판결문·감정가·법정 statutory interest·remaining land를 제대로 읽으면 equity expected value를 시장보다 정밀하게 계산할 수 있었다. 반면 microcap liquidity, tax, appeal duration과 management liquidation intent가 큰 위험이었다. 이런 litigation asset은 '법적으로 이길 것 같다'가 아니라 base asset floor, appeal probability, time value와 실제 distribution waterfall까지 모델링해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

약 90% 확률로 $153m 또는 ~$103/share cash award 수령, underlying business/property base ~$42/share. Win value ~$145/share, current $65 대비 약 123% upside. 사후에는 gross asset/legal value → remaining capex/tax/cost → debt waterfall → time/probability → distributable equity cash 순으로 재구성했다.

### 투자논지를 구성한 핵심 주장

#### 1. 90% win — 적중 · 논지 비중 18%

**당시 주장**

appeal 승소확률이 매우 높다.

**당시 근거**

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

**이 주장이 성립하려면**

case record

**사전 반증조건**

reversal

**실제 결과**

승소 유지.

**정량적 괴리**

Entry / $65 / ~$145 win value / cash/distribution 실현

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

90% win 가설은 'reversal'를 사전 반증조건으로 저장한다.

#### 2. Cash award — 강한 적중 · 논지 비중 18%

**당시 주장**

~$153m 수령한다.

**당시 근거**

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

**이 주장이 성립하려면**

state pays after appeal

**사전 반증조건**

further stay

**실제 결과**

$167.53m 수령.

**정량적 괴리**

Win probability / ~90% / award affirm / affirmed

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Cash award 가설은 'further stay'를 사전 반증조건으로 저장한다.

#### 3. Interest carry — 적중 · 논지 비중 16%

**당시 주장**

9%가 duration cost를 상쇄한다.

**당시 근거**

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

**이 주장이 성립하려면**

interest accrues

**사전 반증조건**

legal change

**실제 결과**

실제 수령 증가.

**정량적 괴리**

Award cash / ~$153m/$103 per share / 수령 / 총 $167.53m

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Interest carry 가설은 'legal change'를 사전 반증조건으로 저장한다.

#### 4. Base NAV — 적중 · 논지 비중 16%

**당시 주장**

패소해도 ~$42/share property value다.

**당시 근거**

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

**이 주장이 성립하려면**

property values

**사전 반증조건**

hidden liabilities

**실제 결과**

잔여 real estate 존재.

**정량적 괴리**

Base property / ~$42/share / downside floor / 잔여 interests 분배

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Base NAV 가설은 'hidden liabilities'를 사전 반증조건으로 저장한다.

#### 5. Management — 강한 적중 · 논지 비중 16%

**당시 주장**

현금수령 후 liquidation/distribution한다.

**당시 근거**

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

**이 주장이 성립하려면**

shareholder orientation

**사전 반증조건**

reinvestment

**실제 결과**

2013 liquidation.

**정량적 괴리**

2012 cash award 수령과 2013 liquidation 결정으로 expected-value thesis가 크게 성공.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

Management 가설은 'reinvestment'를 사전 반증조건으로 저장한다.

#### 6. $145 value — 강한 적중 · 논지 비중 16%

**당시 주장**

$65 대비 123% upside.

**당시 근거**

1심 승소 후 appeal record를 읽으면 New York이 판결을 뒤집을 가능성이 낮고, 9% interest가 계속 붙어 time decay가 오히려 투자자에게 유리하다고 봤다. Litigation value를 0으로 둬도 remaining property 약 $42/share가 하방을 제공한다고 주장했다.

**이 주장이 성립하려면**

award+base

**사전 반증조건**

tax/cost

**실제 결과**

큰 value crystallization.

**정량적 괴리**

2012 cash award 수령과 2013 liquidation 결정으로 expected-value thesis가 크게 성공.

**분석 오류·핵심**

원 claim의 asset/event mechanism이 실제 거래·법원·현금분배로 확인됐다.

**재사용할 교훈**

$145 value 가설은 'tax/cost'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Court award는 상급심에서 유지됐고 2012 총 $167.53m이 들어왔다. 2013 liquidation 승인으로 cash가 주주에게 직접 이전되기 시작했다. 실제 outcome은 원문의 90% win probability를 지지했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2012 cash award 수령과 2013 liquidation 결정으로 expected-value thesis가 크게 성공. asset/legal thesis와 실제 common-equity payoff의 인과를 분리한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

binary event의 확률뿐 아니라 패소 시 base NAV와 승소 시 time-accreting interest를 함께 계산한 것이 좋았다. Expected value뿐 아니라 path-dependent carry가 투자자 편이었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-03-27 — 상급심 판결이 회사에 유리하게 유지되면서 90% win assumption이 더 강하게 확인됐다. 회피 가능성: 해당 없음.

### 10. 최종 판정·반사실·재사용 교훈

전설적 성공. NAV와 litigation value는 현금화 waterfall과 duration을 통과시킨 뒤에만 equity value로 쓴다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | $65 | ~$145 win value | cash/distribution 실현 | 강한 적중 |
| Win probability | ~90% | award affirm | affirmed | 적중 |
| Award cash | ~$153m/$103 per share | 수령 | 총 $167.53m | 초과 방향 |
| Base property | ~$42/share | downside floor | 잔여 interests 분배 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2011-10-25 | VIC 아이디어 게시 | 90% appeal win·$145 EV Long |
| 2012-03-27 | 핵심 법률 검증 | appeal/cash-receipt thesis 업데이트 |
| 2012-07-05 | 뉴욕주 현금수령 | 총 약 $167.53m award/interest가 현금화 |
| 2013-09-12 | Liquidation 승인 | 법률가치가 distribution thesis로 전환 |
| 2013-12-30 | Special dividend | $66.56/share 대규모 현금분배 |
| 2024-01-31 | 사후평가 | 법률 expected value→현금분배 성공 판정 |

### Failure / Success Anatomy

- **근본 오류:** event payoff를 probability×cash waterfall로 분해
- **최초 검증·반증 신호:** 2012-03-27 — 상급심 판결이 회사에 유리하게 유지되면서 90% win assumption이 더 강하게 확인됐다.
- **당시 알 수 있었나:** lease exposure, redevelopment budget, property sales, loan maturities, litigation docket/award, statutory interest와 distributions는 공개자료로 지속 추적 가능했다.
- **피할 수 있었나:** 해당 없음.
- **반사실 질문:** 표면 NAV 또는 법원 award에서 아직 필요한 CapEx·interest·tax·debt repayment·time을 모두 차감하면 실제 주주에게 언제 얼마가 현금으로 돌아오는가?

### 주요 근거자료

- 1. VIC GYRO 2011-10-25 원문 — Value Investors Club / user SQL, 2011-10-25. 원 업로드 SQL에서 thesis·valuation·risk·실제 방향 복원
- [2. Gyrodyne 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/44689/000143774915006464/gyro20141231_10k.htm) — SEC, 2015-03-31. Court award, $167.53m receipt, 2013 liquidation/special dividend 확인
- [3. Gyrodyne 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1589061/000143774916028641/gyrllc20151231_10k.htm) — SEC, 2016-03-31. liquidation structure·remaining property interests 확인
- [4. Gyrodyne appeal update 8-K](https://www.sec.gov/Archives/edgar/data/44689/000143774912002806/gyrodyne_8k-032712.htm) — SEC, 2012-03-27. appeal judgment·award and statutory interest 확인
- [5. Gyrodyne SEC filings](https://www.sec.gov/edgar/browse/?CIK=44689) — SEC, 2024-01-31. litigation·distribution historical filings
- [6. Gyrodyne liquidation history](https://www.sec.gov/Archives/edgar/data/44689/000143774915006464/gyro20141231_10k.htm) — SEC, 2015-03-31. $66.56 special dividend와 후속 distribution 구조 확인

---

# 배치 공통 학습

1. **좋은 부동산과 좋은 equity는 다르다.**
2. **Stabilized NOI/cap-rate NAV에서 아직 쓸 CapEx와 공실기간을 반드시 차감한다.**
3. **낮은 기존 rent는 upside인 동시에 tenant failure 시 carrying-cost subsidy의 소멸이다.**
4. **Project-level IRR이 높아도 portfolio-level cash peak를 못 버티면 주식은 실패한다.**
5. **Bear case 하나를 반박했다고 Long이 되는 것은 아니다.** SRG 2018 legal rebuttal이 대표적이다.
6. **주가방향과 causal accuracy를 분리한다.** Fraudulent-conveyance Short는 가격은 맞고 핵심 인과는 틀렸다.
7. **Distressed real estate에서는 refinancing뿐 아니라 asset-sale/debt-paydown 경로를 모델링한다.**
8. **Litigation investment는 판결금액이 아니라 승소확률×award+interest+base NAV−tax/cost의 waterfall이다.**
9. **법정이자가 높으면 event duration이 항상 불리한 것은 아니다.**
10. **최종 가치는 배당·청산으로 실제 현금이 주주에게 넘어오는 순간 확인된다.**
