# Sirius XM Holdings (SIRI) — 2017-04-25 VIC Short

> **Idea unit:** 이 게시일의 증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 사업·valuation·촉매·증권·가격경로를 분리하고 사후정보는 판정에만 사용한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Sirius XM Holdings / SIRI |
| VIC 게시일 / 작성자 | 2017-04-25 / Flaum |
| 분석 증권 / 실제 방향 | SIRI common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research direction은 별도 교정 |
| 기준 진입가격 | 원문 context 약 $5대; exact 미확정 |
| 기대기간 | 24개월 |
| raw horizon audit | 원문 target $2.50 / 24개월 |
| 최종 판정 | **24개월 실패 — catalyst 일부 적중, 구조적 약화는 늦게 발생** |

> **결론:** CRB royalty 상승과 connected-car 경쟁이라는 방향은 맞았고 2018~2022 royalty rate는 15.5%로 결정됐다. 그러나 2017 EBITDA $2.12bn·FCF $1.56bn, 2018 net adds와 40%+ margin이 단기 earnings를 지지했고 $2.50 target의 24개월 Short는 실패한 것으로 판단한다. self-pay decline은 2024~25에야 뚜렷해졌다.

---

## 1. 회사는 정확히 무엇을 하는가

Sirius XM은 북미 위성라디오 구독, 차량 내 trial·conversion, 광고, streaming·Pandora를 운영한다. OEM이 신차에 수신기를 탑재하고 Sirius XM이 trial 사용자를 self-pay 구독자로 전환한다. 위성·콘텐츠 비용의 상당 부분이 고정이라 가입자와 ARPU 성장은 높은 incremental margin을 만들지만, churn·royalty·OEM subsidy·위성 capex·부채와 자사주매입이 주당 FCF를 크게 바꾼다.

현금엔진은 `self-pay subscribers × ARPU + advertising - revenue share·royalty - content/customer service - satellite capex - cash tax - interest`다. 고정비 leverage와 churn이 반대 방향으로 작동한다.

### 가치사슬과 security payoff

청취자·차량 OEM·광고주 또는 가입자가 만든 gross economics가 station/platform 비용, royalty·content, corporate cost, cash interest, capex, tax를 통과한 뒤 common에 귀속된다. 채권 아이디어는 여기에 담보·seniority·exchange consideration·recovery를 적용한다. 매출 성장, enterprise value 증가, 해당 security 수익을 같은 사건으로 취급하지 않는다.

### 매 분기 볼 핵심 KPI

self-pay net adds, trial conversion, churn, ARPU, SAC·OEM subsidy, royalty rate, adjusted EBITDA margin, satellite capex, FCF, leverage·buyback price

---

## 2. 당시 상황과 시장이 가격에 넣은 것

Sirius XM은 약 $25bn market cap, 3.5% fully taxed FCF yield, 약 15배 EBITDA로 평가됐다. connected car·CarPlay·Android와 월 $10 이하 streaming이 $16~19 list price를 위협하고, royalty 10~11%에서 SoundExchange 요구 23%, trial penetration 75% 하락, 두 위성 capex와 NOL 종료가 겹친다는 Short였다.

### Reverse expectations

높은 valuation은 전국 독점적 차량 distribution, low churn, price power와 70% contribution margin을 반영했다. Short가 맞으려면 royalty 결정이 earnings를 크게 훼손하고 trial/conversion 하락이 net adds를 꺾으며 capex·tax가 FCF를 동시에 낮춰야 했다. structural threat의 방향만으로 24개월 timing은 나오지 않는다.

---

## 3. 원문 투자논지 지도

### C1. connected car가 subscription을 대체 — 실패/지연

**원문 주장**

CarPlay·Android·streaming이 $16~19 satellite plan을 압박한다.

**경제적 메커니즘**

차량 내 선택지 증가가 conversion과 churn을 악화한다.

**T0 근거**

2017 connected-car adoption.

**숨은 가정**

embedded connectivity가 빠르게 보급되고 switching friction이 낮다.

**사전 반증조건**

self-pay adds·ARPU·churn이 24개월 견조하면 timing 반증.

**실제 결과**

2018 Q2 self-pay adds 483k, revenue +6%.

**정량 gap**

24개월 수요붕괴가 나타나지 않음.

**분석 오류 또는 제한**

기술가용성과 소비자전환을 동일시했다.

**재사용 교훈**

adoption funnel을 penetration·usage·cancellation로 나눈다.

### C2. trial penetration 75% 하락이 funnel을 꺾음 — 실패

**원문 주장**

90%대에서 75%로 떨어져 gross trials가 감소한다.

**경제적 메커니즘**

신차 trial 수가 줄면 conversion pool이 작아진다.

**T0 근거**

T0 OEM penetration trend.

**숨은 가정**

used-car reactivation이 gap을 메우지 못한다.

**사전 반증조건**

self-pay net adds가 계속 양수면 반증.

**실제 결과**

2018 Q2 483k self-pay net adds.

**정량 gap**

funnel은 단기 유지.

**분석 오류 또는 제한**

trial penetration 하나로 total gross adds를 설명했다.

**재사용 교훈**

new·used·win-back funnel을 합산한다.

### C3. royalty가 15~23%로 상승 — 부분 성공

**원문 주장**

10~11%에서 크게 올라 earnings를 최대 두 자릿수 훼손한다.

**경제적 메커니즘**

revenue-based royalty가 높은 contribution margin을 직접 깎는다.

**T0 근거**

SoundExchange 23% request·CRB calendar.

**숨은 가정**

회사가 가격·비용으로 상쇄하지 못한다.

**사전 반증조건**

최종 rate가 낮거나 EBITDA 성장으로 흡수되면 payoff 약화.

**실제 결과**

최종 15.5%; 2017 EBITDA +13%, 2018 margin 40%+.

**정량 gap**

방향 적중·극단치 미달·흡수 성공.

**분석 오류 또는 제한**

청구액을 expected value로 사용했다.

**재사용 교훈**

규제 outcome은 확률가중하고 mitigation을 모델링한다.

### C4. satellite capex·NOL 종료가 FCF를 압박 — 실패/지연

**원문 주장**

두 위성 지출과 cash tax가 3.5% FCF yield를 약화한다.

**경제적 메커니즘**

temporary cash holiday 종료가 owner earnings를 낮춘다.

**T0 근거**

T0 satellite schedule·NOL estimate.

**숨은 가정**

EBITDA growth가 현금부담보다 작다.

**사전 반증조건**

FCF가 24개월 성장하면 반증.

**실제 결과**

2017 FCF $1.56bn, 2018 Q2 FCF +17%.

**정량 gap**

초기 FCF 압박 미현실화.

**분석 오류 또는 제한**

capex timing과 cash payment schedule을 거칠게 처리했다.

**재사용 교훈**

FCF catalyst는 분기별 cash schedule로 만든다.

### C5. 15배 EBITDA·3.5% FCF yield는 과대 — 실패

**원문 주장**

5% revenue·7.5% EBITDA growth에 valuation이 높다.

**경제적 메커니즘**

성장 둔화와 비용상승이 multiple compression을 만든다.

**T0 근거**

T0 market cap 약 $25bn·consensus.

**숨은 가정**

earnings beat와 buyback이 valuation을 지지하지 못한다.

**사전 반증조건**

EBITDA·FCF가 두 자릿수 성장하면 short를 재검토.

**실제 결과**

2017 EBITDA +13%, 2018 Q2 FCF +17%.

**정량 gap**

핵심 near-term falsifier 충족.

**분석 오류 또는 제한**

valuation mean reversion보다 earnings momentum이 강했다.

**재사용 교훈**

multiple short는 estimate-revision path를 우선한다.

### C6. 24개월 $2.50 target — 실패

**원문 주장**

royalty·competition·capex가 결합해 큰 downside를 만든다.

**경제적 메커니즘**

earnings miss와 multiple compression이 동시에 발생한다.

**T0 근거**

원문 target·event calendar.

**숨은 가정**

여섯 촉매가 8분기 안에 정렬된다.

**사전 반증조건**

영업 KPI가 개선되고 defensive M&A가 실행되면 실패.

**실제 결과**

2017~2018 KPI 강세, 2019-02 Pandora completion.

**정량 gap**

target 경로를 지지하지 않음; exact return 미복원.

**분석 오류 또는 제한**

지연 가능한 structural factors를 동시조건으로 묶었다.

**재사용 교훈**

short target은 촉매별 날짜·확률·cover rule을 둔다.

---

## 4. 당시 Valuation과 Payoff Structure

원문은 consensus revenue/EBITDA CAGR 5%/7.5% to 2020에 비해 3.5% FCF yield·15배 EBITDA가 과도하다고 봤고 24개월 $2.50 target을 제시했다. 하지만 70% contribution margin과 buyback은 소폭 revenue growth도 FCF/share growth로 만들 수 있다. Short valuation은 terminal multiple뿐 아니라 8개 분기 earnings path를 필요로 했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for short | 15.5% royalty·margin/FCF 성장 | short 손실 | 2017~2018 현실화 |
| Base | net adds 둔화·valuation 압축 | 완만한 하락 | 24개월 미실현 |
| Bull for short | 23% royalty·connected-car churn | $2.50 | 미실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| CRB royalty | 10~11%; request 23% | 15~23% | 15.5% | 방향 적중 |
| 2017 EBITDA | 둔화 기대 | pressure | $2.12bn / +13% | 실패 |
| 2017 FCF | 3.5% yield pressure | 감소 | $1.56bn | 실패 |
| 2018 Q2 self-pay adds | funnel 약화 | 감소 | 483k | 실패 |
| 2018 Q2 FCF | 압박 | 감소 | +17% YoY | 실패 |

### 촉매와 시간

판정 horizon은 **24개월**다. 이후 사건은 장기 사업가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2017-04-25 | VIC Short | $2.50/24개월 |
| 2017-12 | CRB 15.5% 결정 | 촉매 일부 적중 |
| 2017-12-31 | EBITDA $2.12bn·FCF $1.56bn | 영업 반증 |
| 2018-Q2 | 483k self-pay adds·FCF +17% | short path 실패 |
| 2018-Q3 | EBITDA margin 40%+ | operating leverage |
| 2019-02-01 | Pandora 인수 완료 | defensive expansion |
| 2024 | self-pay -296k | 지연된 구조약화 |
| 2025 | self-pay -301k | 장기 방향 확인 |

### 실제 사업·자본구조 추이

CRB는 2018~2022 SDARS royalty를 15.5%로 정해 방향은 맞았지만 23% extreme보다 낮았다. 2017 EBITDA는 $2.12bn(+13%), FCF $1.56bn이었다. 2018 Q2 self-pay net adds 483k, revenue +6%, net income +45%, FCF +17%; Q3 EBITDA margin은 40%를 넘었다. 2019 Pandora를 인수했고 self-pay 감소는 2024 -296k, 2025 -301k로 늦게 나타났다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

원 DB에 정확한 short entry·24개월 price series·borrow cost가 없어 IRR·MFE·MAE를 계산하지 않는다. 다만 24개월 안의 영업 KPI와 Pandora 인수는 $2.50 downside path보다 강했다. 구조적 경쟁이 7~8년 뒤 확인된 사실은 원래 24개월 short 성공을 소급해 만들지 않는다.

가격 series는 배당·세금·거래비용을 포함한 total return과 분리한다. 데이터가 없으면 수익률·MFE·MAE를 추정하지 않는다. Short는 entry·cover·borrow, bond는 coupon·exchange·warrant 수령일이 있어야 exact IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | connected car가 subscription을 대체 | 20% | 실패/지연 | 24개월 수요붕괴가 나타나지 않음. |
| C2 | trial penetration 75% 하락이 funnel을 꺾음 | 18% | 실패 | funnel은 단기 유지. |
| C3 | royalty가 15~23%로 상승 | 18% | 부분 성공 | 방향 적중·극단치 미달·흡수 성공. |
| C4 | satellite capex·NOL 종료가 FCF를 압박 | 16% | 실패/지연 | 초기 FCF 압박 미현실화. |
| C5 | 15배 EBITDA·3.5% FCF yield는 과대 | 16% | 실패 | 핵심 near-term falsifier 충족. |
| C6 | 24개월 $2.50 target | 12% | 실패 | target 경로를 지지하지 않음; exact return 미복원. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

Short 손실을 만든 것은 강한 installed base, contribution margin, price power와 buyback이었다. royalty 상승은 earnings를 일부 낮췄지만 극단치보다 낮았고, connected-car 경쟁은 churn을 즉시 폭발시키지 않았다. Pandora 인수는 defensive response였지만 동시에 short catalyst를 뒤로 밀었다.

### What was right / What was wrong

**맞았던 것:** 장기 방향 일부와 관련된 관찰은 유효했다. **틀렸던 것:** 정확한 secular direction을 short horizon과 혼동했다. 23% request를 base-case outcome처럼 사용했고 high incremental margin의 단기 earnings cushion을 과소평가했다.

### Counterfactual

royalty가 15.5%로 오르더라도 EBITDA가 두 자릿수 성장하고 self-pay adds가 양수라면 valuation short는 어떤 분기 KPI에서 cover했어야 하는가?

---

## 9. 분석 오류 유형과 최초 경고

정확한 secular direction을 short horizon과 혼동했다. 23% request를 base-case outcome처럼 사용했고 high incremental margin의 단기 earnings cushion을 과소평가했다.

### 최초로 관찰 가능했던 경고신호

2017 full-year EBITDA +13%와 2018 Q2 FCF +17%가 24개월 thesis를 재평가할 첫 직접 경고였다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

secular short에는 방향뿐 아니라 8개 분기 내 earnings inflection이 필요하다.

### Lesson 2

규제청구액과 최종결정 확률분포를 분리한다.

### Lesson 3

늦게 맞은 산업통찰은 원래 short IRR을 구제하지 않는다.

### 지금 같은 아이디어를 다시 본다면

- self-pay adds
- trial penetration·conversion
- churn
- royalty rate
- incremental margin
- satellite capex·cash tax
- borrow cost·cover rule

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 장기 방향 일부 |
| Valuation thesis | 24개월 실패 |
| Catalyst thesis | royalty 일부 적중 |
| Timing / path | 실패 |
| Security selection | Short 부적절 |
| Thesis score | 4.5/10 |
| Process score | 8.0/10 |
| 종합 | **24개월 실패 — catalyst 일부 적중, 구조적 약화는 늦게 발생** |

### 한 문장 교훈

> secular short에는 방향뿐 아니라 8개 분기 내 earnings inflection이 필요하다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/SIRIUS_XM_HOLDINGS_INC/7836075076) — Value Investors Club / source SQL, 2017-04-25. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준. SGA 2010은 본문이 누락되어 가격 series와 2019 동일 작성자 회고만 사용.
2. [Sirius 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/908937/000095012308002331/y50289e10vk.htm) — SEC / Sirius, 2008. 2007 subscriber·revenue 성장 검증.
3. [XM/Sirius merger announcement](https://investor.siriusxm.com/sec-filings/sirius-xm-holdings-inc/content/0000950123-07-003042/0000950123-07-003042.pdf) — SEC / Sirius XM, 2007-02-19. 합병 선택권과 조건 검증.
4. [Sirius XM 2016 filing/results](https://investor.siriusxm.com/sec-filings/sirius-xm-holdings-inc/content/0000908937-17-000007/0000908937-17-000007.pdf) — SEC / Sirius XM, 2017. 2016 revenue·EBITDA·FCF 검증.
5. [Sirius XM FY2017 results](https://investor.siriusxm.com/news-events/press-releases/detail/1204/siriusxm-reports-fourth-quarter-and-full-year-2017-results) — Sirius XM, 2018. 2017 EBITDA·FCF 검증.
6. [Q2 2018 results](https://investor.siriusxm.com/news-events/press-releases/detail/1141/siriusxm-reports-second-quarter-2018-results) — Sirius XM, 2018. net adds·revenue·FCF momentum 검증.
7. [Q3 2018 results](https://investor.siriusxm.com/news-events/press-releases/detail/1114/siriusxm-reports-third-quarter-2018-results) — Sirius XM, 2018. 40% 초과 EBITDA margin 검증.
8. [CRB SDARS III rates](https://www.crb.gov/rate/16-CRB-0001-SR-PSSR-SDARSIII/appendix-a-rates-and-terms.pdf) — Copyright Royalty Board, 2017. 2018~2022 15.5% royalty rate 검증.
9. [Pandora acquisition completion](https://investor.siriusxm.com/news-events/press-releases/detail/1084/siriusxm-completes-acquisition-of-pandora) — Sirius XM, 2019-02-01. Pandora 인수와 대가 검증.
10. [Sirius XM FY2021 results](https://www.sec.gov/Archives/edgar/data/908937/000090893722000004/siriq42021earningsrelease.htm) — SEC / Sirius XM, 2022. subscriber·buyback authorization 검증.
11. [2024 Liberty simplification](https://investor.siriusxm.com/news-events/press-releases/detail/2105/siriusxm-kicks-off-new-phase-as-an-independent-public) — Sirius XM, 2024. 거래·reverse split·추가 debt 검증.
12. [Sirius XM 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/908937/000090893726000006/siri-20251231.htm) — SEC / Sirius XM, 2026. 2025 subscriber·FCF·사업구조 검증.

### 데이터 품질

- T0 원문·metadata: **A/B** — source SQL과 공개 VIC URL을 기준으로 했다. SGA 2010은 body가 없어 claim reconstruction을 명시적으로 낮은 신뢰도로 처리했다.
- 사업·거래·자본구조: **A** — SEC·회사·CRB·FCC 1차자료를 우선했다.
- 가격경로: **B/C 또는 미검증** — 원 DB가 보존한 SGA ratio만 수치화했다. 배당 포함 여부가 불명확해 현금배당을 중복 가산하지 않았다.
- raw SQL direction은 **Short**, 본문 실제 research direction은 **Short**다. 둘을 덮어쓰지 않고 나란히 보존했다.
