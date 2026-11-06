# Aimia Inc. (AIM) — 2013-11-26 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-11-06. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Aimia Inc. / AIM |
| VIC 게시일 / 작성자 | 2013-11-26 / Ragnar0307 |
| 분석 증권 / 실제 방향 | TSX:AIM common / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | C$18.75 (2013-11-26 종가). 원문 가격 미기재, 3.6% 배당으로 일관 |
| 기대기간 | 12~18개월 +40~50%, 강세 +70~80% |
| raw horizon audit | 9~10배 FCF → 15배 |
| 최종 판정 | **치명적 실패 — 앵커 파트너 이탈, -86%** |

> **결론:** 카드사 재계약과 Aeroplan 개편은 실제로 일어났지만 FCF 두 자릿수 성장은 오지 않았고 주가는 Air Canada 발표 직전까지 이미 -52%였다. 2017-05-11 Air Canada가 2020 이후 계약 비갱신을 알리자 하루 -63%였다. 원문은 2020 계약을 위험으로 적었으나 '2020까지 문제없다'로 끝냈다.

---

## 1. 회사는 정확히 무엇을 하는가

Aimia는 Aeroplan을 운영하는 로열티 사업자다. TD·CIBC·Amex 같은 카드사와 제휴사에 마일을 먼저 팔아 Gross Billings를 받고, 회원이 마일을 쓸 때 Air Canada 좌석 등 보상을 구매한다. 수익의 핵심은 판매단가와 보상원가의 차이이며, 2013년 EBITDA의 약 80%가 캐나다에서 나왔다. Air Canada 좌석 구매 계약이 이 차이의 기반이었다.

`FCF = Gross Billings − 보상원가(burn × 마일당 원가) − 운영비 − 세금 ± 파트너 일회성 현금`. Air Canada 좌석 원가와 카드사 단가가 스프레드를 정한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

Gross Billings 증가율, burn/earn 비율, 마일당 원가, 배당 전 FCF(일회성 제외), TD·CIBC 전환율, Air Canada 계약 협상 상태, 순부채, 배당 커버리지

---

## 2. 당시 상황과 시장이 가격에 넣은 것

작성자는 CIBC 대비 15% 이상 높은 TD 조건, TD의 C$100m 지원, CIBC에 지급한 C$150m, Amex 재계약을 근거로 들었다. 마일 차감을 20~50% 낮춰 회원에게 돌려주는 대신 매출을 mid~high single digit로 재가속한다는 논지다. 9~10배 선행 FCF 대비 ADS 20배, AXP 16배, Smiles 24배를 동종으로 봤다.

### Reverse expectations

C$18.75에 3.6% 배당과 9~10배 FCF면 시장은 캐나다 사업의 정체와 파트너 위험을 할인했다. 더 올라가려면 스프레드 유지와 파트너 유지가 모두 필요했다.

---

## 3. 원문 투자논지 지도

### C1. Air Canada 관계가 지속 경쟁우위 — 치명적 실패

**원문 주장**

2020까지 좌석 8% 할인 구매 계약이 지속적 우위다.

**경제적 메커니즘**

싼 좌석이 스프레드와 회원 유인을 만든다.

**T0 근거**

계약 2020까지, 8% 좌석.

**숨은 가정**

Air Canada가 2020 이후 갱신한다.

**사전 반증조건**

2020 3년 전까지 갱신 합의가 없으면 반증.

**실제 결과**

2017-05-11 비갱신 발표, 주가 하루 -63%.

**정량 gap**

주가 C$8.93 → C$3.33

**분석 오류 또는 제한**

계약 만기가 논지 기간 내 영향을 주지 않는다고 봤다.

**재사용 교훈**

앵커 파트너의 관점에서 계약 만기 후 대안의 경제성을 계산한다.

### C2. FCF 두 자릿수 재가속 — 실패

**원문 주장**

2015부터 두 자릿수 성장이다.

**경제적 메커니즘**

높아진 단가와 물량 증가.

**T0 근거**

경영진 FCF >C$250m 가이던스.

**숨은 가정**

회원 혜택 비용이 물량으로 상쇄된다.

**사전 반증조건**

2015 FCF가 C$250m 미달이면 반증.

**실제 결과**

2014 C$287.0m(TD C$100m 포함, 제외 시 C$187m), 2015 C$202.3m, 2016 가이던스 C$190~220m.

**정량 gap**

약 C$200m 정체

**분석 오류 또는 제한**

단가 상승을 회원에게 넘긴 뒤의 FCF를 낙관했다.

**재사용 교훈**

일회성 파트너 현금을 빼고 FCF를 추적한다.

### C3. 15배 FCF로 재평가 — 실패

**원문 주장**

15배로 +40~50%다.

**경제적 메커니즘**

성장과 부담 해소.

**T0 근거**

ADS·AXP·Smiles 비교.

**숨은 가정**

파트너 집중을 동종과 같게 할인.

**사전 반증조건**

FCF 정체 시 15배 근거 소멸.

**실제 결과**

최고 C$19.73, 1년 -22.2%, 2년 -48.4%.

**정량 gap**

+40~50% 대 -48%

**분석 오류 또는 제한**

파트너 집중을 반영하지 않았다.

**재사용 교훈**

동종 배수는 집중 위험을 반영해 쓴다.

### C4. 부담 해소 — 부분 적중

**원문 주장**

CIBC·Amex·경쟁심판·마일 만료 이슈가 끝난다.

**경제적 메커니즘**

할인 요인 제거.

**T0 근거**

2013 내 대부분 해소.

**숨은 가정**

더 큰 부담이 없다.

**사전 반증조건**

새 파트너 부담이 나오면 반증.

**실제 결과**

기존 부담은 해소, Air Canada 위험은 남음.

**정량 gap**

4개 해소, 최대 부담 미해소

**분석 오류 또는 제한**

가장 큰 부담이 목록에 없었다.

**재사용 교훈**

부담 목록을 현금 기여도 순서로 정렬한다.

### C5. 배당·자사주 — 부분 적중

**원문 주장**

3.6% 배당과 10% 자사주 가능하다.

**경제적 메커니즘**

주주 환원이 하방을 막는다.

**T0 근거**

배당 실적, NCIB.

**숨은 가정**

자본 잠식이 없다.

**사전 반증조건**

자본손상 테스트 위험 시 반증.

**실제 결과**

배당 평균 C$137m(2014~16), 자사주 누적 C$275m, 2017-06-14 배당 중단.

**정량 gap**

환원 후 중단

**분석 오류 또는 제한**

환원이 파트너 위험을 해결하지 못했다.

**재사용 교훈**

배당은 자본잠식 조건을 함께 본다.

### C6. redemption은 일시 상승 후 정상화 — 부분 적중

**원문 주장**

1Q 100% 초과 후 2H 정상화한다.

**경제적 메커니즘**

회원 사용이 일시 급증한다.

**T0 근거**

경영진 설명.

**숨은 가정**

높은 보상 비용이 일시적이다.

**사전 반증조건**

2015 비용 재상승이면 반증.

**실제 결과**

FY2014 발표가 Aeroplan 마일당 보상 원가 상승을 FCF 압박 요인으로 언급. 정상화 2015 FCF C$206.8m에는 세금 환급 C$41.1m가 포함.

**정량 gap**

구조적 원가 상승 신호

**분석 오류 또는 제한**

개편 후 보상 원가 수준의 영구 상승을 작게 봤다.

**재사용 교훈**

일시와 구조적 비용 변화를 나누어 본다.

---

## 4. 당시 Valuation과 Payoff Structure

15배 선행 FCF 기준 Base +40~50%(C$26.25~28.13), Bull +70~80%(C$31.88~33.75). 표 원문은 이미지라 보존되지 않아 FCF 입력값은 원문 수치로 확인하지 못했다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bull | 높은 FCF + 15배 | C$32~34 | 미실현 |
| Base | 15배 | C$26~28 | 미실현, 최대 C$19.73 |
| Bear(원문 없음) | Air Canada 이탈 | 90% 하락 | 2017-07-31 C$1.45(-92%) |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | C$18.75 | C$26~28 | 1년 C$14.58, 2026-10-23 C$2.57 | 치명적 실패 |
| 배당 전 FCF | 9~10배 수준 | >C$250m | 2015 C$202.3m | 실패 |
| Gross Billings | 정체 | mid~high single | 2014 고정환율 +9.3%, 2016 가이던스 안정 | 단기 적중 |
| Air Canada 계약 | 2020까지 | 유지 | 2017-05-11 비갱신 | 치명적 실패 |
| 배당 | 3.6% | 성장 | 2017-06-14 중단 | 실패 |

### 촉매와 시간

판정 horizon은 **12~18개월 +40~50%, 강세 +70~80%**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2013-11-26 | VIC Long, C$18.75 | 재계약 인플렉션 |
| 2014-01-22 | C$19.73 | MFE +5% |
| 2015-02 | 2014 FCF C$287.0m(TD C$100m 포함) | 일회성 제외 C$187m |
| 2016-02 | 2015 FCF C$202.3m | 두 자릿수 성장 실패 |
| 2017-05-11 | Air Canada 비갱신 발표, C$8.93 → C$3.33 | -63% |
| 2017-06-14 | 배당 중단(자본 손상 테스트) | 소득 논지 종료 |
| 2017-07-31 | C$1.45 | MAE -92% |
| 2019-01-10 | Aeroplan 매각 종결, 현금 C$450m + 약 C$1.9bn 부채 인수 | 핵심 사업 종료 |

### 실제 사업·자본구조 추이

2014 FCF는 TD 일회성을 제외하면 약 C$187m, 2015 C$202.3m, 2016 가이던스 C$190~220m였다. 2015 수치에는 세금 환급이 포함돼 기초 현금창출력은 더 낮았다. Air Canada는 자체 프로그램이 C$2~2.5bn의 가치를 만든다고 추정했다. 2018-02 Nectar를 약 C$105m(순 C$34m)에 매각했고, 2019-01 Aeroplan을 현금 C$450m에 넘겼다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

1개월 +3.8%, 1년 -22.2%, 2년 -48.4%, 3년 -57.7%, 2017-05-10 C$8.93(-52%), 5년 -79.6%(배당 포함 -71.6%), 2026-10-23 C$2.57 -86.3%(배당 포함 -80.9%). MFE +5%, MAE -92%. SQL 성과행은 없다. 모든 수치는 C$ 기준이다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | Air Canada 관계가 지속 경쟁우위 | 20% | 치명적 실패 | 주가 C$8.93 → C$3.33 |
| C2 | FCF 두 자릿수 재가속 | 18% | 실패 | 약 C$200m 정체 |
| C3 | 15배 FCF로 재평가 | 18% | 실패 | +40~50% 대 -48% |
| C4 | 부담 해소 | 16% | 부분 적중 | 4개 해소, 최대 부담 미해소 |
| C5 | 배당·자사주 | 16% | 부분 적중 | 환원 후 중단 |
| C6 | redemption은 일시 상승 후 정상화 | 12% | 부분 적중 | 구조적 원가 상승 신호 |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

두 단계 손실이다. 2014~2017-05 FCF 정체로 약 -52%, 그 뒤 앵커 파트너 이탈로 C$8.93에서 C$3.33까지. 뒤의 사건이 더 극적이지만 앞의 사건이 이미 절반을 가져갔다.

### Counterfactual

Air Canada가 재계약했더라도 FCF가 C$200m 근처라면 15배 재평가는 어려웠다. 다만 -86%는 아니었을 것이다.

---

## 9. 분석 오류 유형과 최초 경고

계약 만기를 기한 밖 위험으로 처리했다. 파트너 입장에서 자체 프로그램의 경제성을 계산하지 않았다.

### 최초로 관찰 가능했던 경고신호

2015-02 FY2014에서 일회성 제외 FCF가 약 C$187m로 >C$250m 가이던스 경로에 못 미쳤다. 2017-05 전 C$10 미만으로 시장이 이미 경고했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

앵커 파트너의 계약 만기는 파트너 입장에서 대안 경제성으로 계산한다.

### Lesson 2

일회성 파트너 현금을 빼지 않으면 FCF 인플렉션은 착시다.

### Lesson 3

부담 목록은 현금 기여도 순으로 쓴다. 가장 큰 부담이 빠지면 나머지 해소는 의미가 없다.

### 지금 같은 아이디어를 다시 본다면

- 파트너 내재화 시 NPV 계산
- 좌석 원가 대비 시장가 차이
- 일회성 제외 FCF
- 계약 만기 3년 전 갱신 진행도
- 유사 항공사의 로열티 재매입 사례

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 카드 재계약 적중, 파트너 판단 치명적 |
| Valuation thesis | 15배 실패 |
| Catalyst thesis | 카드 촉매 적중, 최대 촉매 놓침 |
| Security selection | 보통주 잔여 위험 그대로 |
| Timing / path survivability | 2년 -48%, 이탈 전 이미 -52% |
| Thesis score | 2.0/10 |
| Process score | 4.0/10 |
| 종합 | **치명적 실패 — 앵커 파트너 이탈, -86%** |

### 한 문장 교훈

> 앵커 파트너의 계약 만기는 파트너 입장에서 대안 경제성으로 계산한다.

---

## 12. Sources / Validation Notes

1. VIC source-DB preserved original — Value Investors Club / source SQL, 2013-11-26. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 source SQL 본문을 사용했다.
2. [Aimia reports 4Q and FY2014 results](https://newswire.ca/news-releases/aimia-reports-fourth-quarter-and-full-year-2014-results-516976411.html) — Aimia / Newswire, 2015-02. 2014 배당 전 FCF C$287.0m(TD 기여 C$100m 포함), Gross Billings 고정환율 +9.3%.
3. [Aimia reports 4Q and FY2015 results](https://www.aimia.com/aimia-reports-fourth-quarter-and-full-year-2015-results/) — Aimia, 2016-02. 2015 배당 전 FCF C$202.3m.
4. [Aimia reports 1Q 2016 results](https://aimia.com/aimia-reports-first-quarter-2016-results) — Aimia, 2016-05-12. 2016 FCF 가이던스 C$190~220m, Gross Billings 안정, 정상화 2015 FCF C$206.8m(세금 환급 C$41.1m 포함), 자사주 누적 C$275m.
5. [Why Air Canada is abandoning Aeroplan](https://theglobeandmail.com/business/rob-magazine/article-why-air-canada-is-abandoning-aeroplanand-what-that-means-for-your) — The Globe and Mail, 2018-05-11. 좌석 원가 시장가 대비 20~30% 할인, Air Canada의 $2~2.5bn 가치 추정, 하루 -63%, 배당 평균 C$137m, Nectar 순매각 C$34m.
6. [Aimia provides update on dividends](https://www.aimia.com/aimia-provides-update-on-dividends/) — Aimia, 2017-06-14. 보통주·우선주 배당 중단, 자본손상 테스트가 사유.
7. [Aimia sells Nectar business to Sainsbury's](https://aimia.com/aimia-sells-nectar-business-to-sainsburys) — Aimia, 2018-02-01. 총 대가 약 C$105m(£60m).
8. [Air Canada completes acquisition of Aeroplan](https://stockhouse.com/news/press-releases/2019/01/10/air-canada-completes-acquisition-of-aeroplan-loyalty-business) — Air Canada, 2019-01-10. 2019-01-10 종결, 현금 C$450m과 약 C$1.9bn 마일 부채 인수. 본문 직접 접근 불가, 검색 발췌 확인(등급 B).
9. [Aimia daily close / adjusted close (AIM.TO)](https://finance.yahoo.com/quote/AIM.TO/history/) — Yahoo Finance chart data, 2026-10-23. C$ 기준 종가·배당 조정 종가로 경로와 2017-05-11 하루 낙폭을 계산했다.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A/B** — SEC·회사 1차자료 우선. 일부는 2차자료와 검색 발췌로 확인했고 각 출처에 표시했다.
- 가격·수익률: **C/D** — source SQL 성과행 없음. Yahoo 종가와 원문 기록가만 사용. 워런트 일별 시가 미확보.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
