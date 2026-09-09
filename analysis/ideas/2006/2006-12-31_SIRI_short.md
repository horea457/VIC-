# Sirius Satellite Radio (SIRI) — 2006-12-31 VIC Short

> **Idea unit:** 이 게시일의 증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-09. 사업·valuation·촉매·증권·가격경로를 분리하고 사후정보는 판정에만 사용한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Sirius Satellite Radio / SIRI |
| VIC 게시일 / 작성자 | 2006-12-31 / bode314 |
| 분석 증권 / 실제 방향 | SIRI common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존, research direction은 별도 교정 |
| 기준 진입가격 | 원문 공개 URL·정확한 가격 미복원 |
| 기대기간 | 2007년 guidance·financing |
| raw horizon audit | 촉매는 2007년 |
| 최종 판정 | **혼합/실패 — 재무위험 적중, short payoff 미검증·merger가 경로 변경** |

> **결론:** 가입자 guidance 하향, 월 churn 1.4~1.8%, 연 $600m+ operating loss와 $6bn EV의 긴장을 지적한 것은 타당했다. 그러나 2007 subscriber revenue는 49% 성장했고 2007-02 XM 합병 발표가 standalone insolvency path를 바꿨다. 2009 Liberty rescue는 funding risk를 확인했지만 exact short return은 없어 승리로 소급하지 않는다.

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

Sirius는 2006 subscriber guidance를 6.3m에서 5.9~6.1m으로 낮췄고 net adds가 둔화됐다. Q3 revenue $167.1m, gross profit $102.3m, operating expense $204.1m, EBIT -$101.8m이었다. 원문은 EV 약 $6bn·subscriber당 약 $1,000, 10m subs에서도 $670/sub를 문제 삼았다.

### Reverse expectations

시장은 현재 손실이 아니라 높은 fixed-cost platform의 미래 scale과 XM 결합 가능성을 살 수 있었다. Short가 성공하려면 2007 CFFO break-even 실패와 추가 financing이 dilution 또는 distress로 직결되고, merger/strategic capital이 그 tail을 막지 않아야 했다.

---

## 3. 원문 투자논지 지도

### C1. subscriber growth는 둔화 — 실패

**원문 주장**

guidance 6.3m→5.9~6.1m과 net adds 둔화가 수요약화를 보인다.

**경제적 메커니즘**

가입자 부족이 fixed cost absorption을 늦춘다.

**T0 근거**

2006 revised guidance·1.4~1.8% monthly churn.

**숨은 가정**

guidance miss가 2007에도 이어진다.

**사전 반증조건**

subscriber·revenue growth가 재가속하면 반증.

**실제 결과**

2007 subscriber +38%, subscriber revenue +49%.

**정량 gap**

방향이 반대로 전개.

**분석 오류 또는 제한**

한 차례 guidance cut을 trend로 고정했다.

**재사용 교훈**

subscriber thesis는 cohort·churn·gross adds로 갱신한다.

### C2. Howard Stern economics는 부정적 — 미검증/부분 실패

**원문 주장**

약 1.5m subs/$200m revenue 대비 $500m/5년 contract가 과도하다.

**경제적 메커니즘**

content cost가 contribution을 흡수한다.

**T0 근거**

원문 subscriber attribution 추정.

**숨은 가정**

incremental retention·brand spillover가 작다.

**사전 반증조건**

subscriber/revenue growth가 content spend를 정당화하면 약화.

**실제 결과**

2007 높은 subscriber/revenue 성장과 merger scale이 나타났다.

**정량 gap**

계약의 완전한 unit economics는 미복원.

**분석 오류 또는 제한**

direct subs만 세고 churn·brand option을 누락했다.

**재사용 교훈**

content ROI는 acquisition+retention+ad revenue로 본다.

### C3. 연 $600m+ loss는 financing을 강제 — 부분 성공

**원문 주장**

Q3 EBIT -$101.8m과 높은 cash burn이 추가자금을 요구한다.

**경제적 메커니즘**

현금소진이 dilution·high-cost debt·distress를 만든다.

**T0 근거**

Q3 2006 P&L과 원문 annualization.

**숨은 가정**

operating leverage가 funding 전에 충분히 개선되지 않는다.

**사전 반증조건**

strategic capital·merger가 runway를 연장하면 timing 반증.

**실제 결과**

2009 Liberty rescue가 필요했지만 merger가 2007 발표됐다.

**정량 gap**

risk 적중·short timing 지연.

**분석 오류 또는 제한**

필요자금과 주가촉매 날짜를 동일시했다.

**재사용 교훈**

cash runway에는 strategic funding scenario를 둔다.

### C4. EV $6bn/$1,000 per sub는 과대 — 부분 실패

**원문 주장**

10m subs에서도 $670/sub로 높은 기대를 반영한다.

**경제적 메커니즘**

필요 EBITDA/sub가 현실 unit economics를 넘으면 multiple이 압축된다.

**T0 근거**

원문 EV/sub reverse valuation.

**숨은 가정**

incremental margin이 충분히 높지 않다.

**사전 반증조건**

합병 synergy와 scale로 EBITDA margin이 크게 오르면 반증.

**실제 결과**

2017~2018 합병회사의 EBITDA/FCF scale은 강해졌다.

**정량 gap**

장기 operating leverage가 valuation critique를 약화.

**분석 오류 또는 제한**

static unit metric에 fixed-cost leverage를 누락했다.

**재사용 교훈**

subscriber multiple은 mature contribution으로 환산한다.

### C5. iPod·WiMAX가 차량 moat를 침식 — 지연된 성공

**원문 주장**

portable·in-car internet가 paid satellite value를 낮춘다.

**경제적 메커니즘**

대체재가 listening time과 willingness-to-pay를 가져간다.

**T0 근거**

2006 device/technology landscape.

**숨은 가정**

차량 connectivity가 빠르게 보급된다.

**사전 반증조건**

OEM funnel과 exclusive content가 subs를 계속 늘리면 timing 실패.

**실제 결과**

단기에는 subscriber 성장·합병이 우세했고 장기 경쟁은 늦게 나타났다.

**정량 gap**

방향은 맞고 horizon이 길었다.

**분석 오류 또는 제한**

technology adoption curve를 촉매로 과속했다.

**재사용 교훈**

secular short에는 adoption milestone을 둔다.

### C6. 2007 financing/guidance가 short catalyst — 실패

**원문 주장**

CFFO break-even 실패와 H2 financing이 valuation을 깬다.

**경제적 메커니즘**

현금필요가 equity dilution 우려로 가격에 반영된다.

**T0 근거**

원문 2007 catalyst list.

**숨은 가정**

XM deal이 standalone financing event를 대체하지 않는다.

**사전 반증조건**

merger 발표·revenue growth면 catalyst 무효.

**실제 결과**

2007-02 merger 발표, 2007 subscriber revenue +49%.

**정량 gap**

촉매가 반대 전략이벤트에 덮였다.

**분석 오류 또는 제한**

event tree를 단일 downside path로 봤다.

**재사용 교훈**

catalyst calendar에는 positive optionality도 넣는다.

---

## 4. 당시 Valuation과 Payoff Structure

원문은 10m subs에서도 EV/sub $670이며 10배 valuation을 지지하려면 subscriber당 EBITDA $67이 필요하다고 계산했다. 이는 유용한 reverse DCF지만, fixed satellite/content cost와 merger synergies가 subscriber당 economics를 크게 바꿀 수 있었다. Howard Stern 계약 $500m/5년을 단순 비용으로만 보지 않고 acquisition value와 retention을 함께 봐야 했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for short | XM merger·subscriber scale | short squeeze/손실 | 2007 발표 |
| Base | guidance miss·financing | valuation 압축 | risk는 적중 |
| Bull for short | 현금고갈·독자 distress | 큰 하락 | 2009 rescue까지 지연 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2006 subscriber guide | 6.3m→5.9~6.1m | 추가 하향 | 2007 subscriber +38% | 실패 |
| Monthly churn | 1.4~1.8% | 악화 | 정확한 후속 비교 미복원 | 미검증 |
| Q3 EBIT | -$101.8m | cash burn | 2009 strategic rescue | 위험 적중 |
| EV/sub | 약 $1,000 | 압축 | 장기 scale economics 개선 | 부분 실패 |
| Merger | 미반영 | 없음 | 2007-02 발표·2008-07 완료 | short 반증 |

### 촉매와 시간

판정 horizon은 **2007년 guidance·financing**다. 이후 사건은 장기 사업가설 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2006-12-31 | VIC Short | guidance·cash burn |
| 2007-02-19 | XM merger 발표 | 첫 반증 |
| 2007-12-31 | subscriber revenue +49% | 영업방향 반대 |
| 2008-07-28 | merger 완료 | scale·synergy option |
| 2009-02 | Liberty financing | standalone risk 확인 |
| 2009 | Liberty loan 상환 | 즉시 insolvency 회피 |

### 실제 사업·자본구조 추이

2007 subscriber revenue는 subscriber 38% 증가에 힘입어 49% 늘었다. Sirius와 XM은 2007-02-19 합병을 발표했고 2008-07-28 완료했다. 2009에는 Liberty로부터 최대 $530m을 빌려 near-term liquidity를 확보했고 같은 해 이를 상환했다. 독자기업 funding risk는 실제였지만 merger·strategic capital이 terminal outcome을 바꿨다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

게시일 공개 URL과 표준 가격 series가 없어 short entry·cover·borrow cost·MFE·MAE·IRR을 계산하지 않는다. 2009 rescue가 있었다는 사실을 2007 short profit으로 간주하지 않는다. short 판정은 2007 subscriber growth와 merger announcement 때문에 혼합/실패 쪽으로 둔다.

가격 series는 배당·세금·거래비용을 포함한 total return과 분리한다. 데이터가 없으면 수익률·MFE·MAE를 추정하지 않는다. Short는 entry·cover·borrow, bond는 coupon·exchange·warrant 수령일이 있어야 exact IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | subscriber growth는 둔화 | 20% | 실패 | 방향이 반대로 전개. |
| C2 | Howard Stern economics는 부정적 | 18% | 미검증/부분 실패 | 계약의 완전한 unit economics는 미복원. |
| C3 | 연 $600m+ loss는 financing을 강제 | 18% | 부분 성공 | risk 적중·short timing 지연. |
| C4 | EV $6bn/$1,000 per sub는 과대 | 16% | 부분 실패 | 장기 operating leverage가 valuation critique를 약화. |
| C5 | iPod·WiMAX가 차량 moat를 침식 | 16% | 지연된 성공 | 방향은 맞고 horizon이 길었다. |
| C6 | 2007 financing/guidance가 short catalyst | 12% | 실패 | 촉매가 반대 전략이벤트에 덮였다. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

맞은 것은 standalone cash burn과 추가자금 필요였다. 틀린 것은 Howard Stern·content spending의 subscriber acquisition 효과와 XM merger option을 충분히 가격화하지 않은 점이다. Short security는 timing과 strategic event에 취약했고, eventual funding stress가 즉시 수익을 보장하지 않았다.

### What was right / What was wrong

**맞았던 것:** standalone risk 적중와 관련된 관찰은 유효했다. **틀렸던 것:** standalone EV/subscriber와 손실 run-rate를 정적 사용했고 merger synergy·strategic financing이라는 path dependency를 작게 뒀다.

### Counterfactual

XM merger가 발표되지 않고 2007 subscriber revenue가 49% 성장했다면 cash burn alone이 언제 short payoff로 전환됐을까?

---

## 9. 분석 오류 유형과 최초 경고

standalone EV/subscriber와 손실 run-rate를 정적 사용했고 merger synergy·strategic financing이라는 path dependency를 작게 뒀다.

### 최초로 관찰 가능했던 경고신호

2007-02-19 XM merger 발표가 thesis를 즉시 재평가해야 할 첫 사건이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

플랫폼 short는 cash burn뿐 아니라 strategic buyer·merger option을 명시적으로 가격화한다.

### Lesson 2

EV/subscriber는 incremental margin과 fixed-cost absorption을 함께 본다.

### Lesson 3

eventual distress는 entry-to-cover short IRR을 대체하지 않는다.

### 지금 같은 아이디어를 다시 본다면

- net adds·churn
- trial conversion
- SAC
- monthly cash burn
- liquidity runway
- merger probability
- borrow cost·cover rule

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | standalone risk 적중 |
| Valuation thesis | 비싸다는 지적 부분 |
| Catalyst thesis | merger로 경로 변경 |
| Timing / path | 실패/미검증 |
| Security selection | common Short 취약 |
| Thesis score | 5.0/10 |
| Process score | 7.0/10 |
| 종합 | **혼합/실패 — 재무위험 적중, short payoff 미검증·merger가 경로 변경** |

### 한 문장 교훈

> 플랫폼 short는 cash burn뿐 아니라 strategic buyer·merger option을 명시적으로 가격화한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2006-12-31. T0 원문, 작성자, raw 방향, valuation·catalyst 수치의 기준. SGA 2010은 본문이 누락되어 가격 series와 2019 동일 작성자 회고만 사용.
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
