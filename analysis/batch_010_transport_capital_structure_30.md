# Batch 010 — 항공·렌터카·자동차와 자본구조 30건

평가기준일: 2024-01-31  
분석일: 2026-09-03  
대상: Aimia/AerCap 8건·Hertz 8건·Spirit 7건·GM 7건

## 결론부터

이번 배치의 공통점은 **좋은 운영자산과 보통주 가치가 다르고, 같은 기업 안에서도 보통주·채권·워런트·옵션·합병차익거래의 결과가 다르다**는 점이다. 항공기·차량처럼 담보가 보여도 높은 레버리지와 중고자산 가격, 계약·규제·유동성 경로를 함께 보지 않으면 하방을 잘못 계산한다.

| 기업 | 건수 | 가장 강한 성공 | 가장 큰 실패 | 핵심 학습 |
|---|---:|---|---|---|
| Aimia/AerCap | 8 | AER 2020 COVID Long | AER 2017·2018 Long | book discount와 stress asset value를 분리 |
| Hertz | 8 | 2019 debt Short | 2018·2022 equity Long | 산업생존과 levered issuer 생존은 다름 |
| Spirit | 7 | 2012·2013 Long, 2020 EETC | 2017 Long·2022 arb | common·담보채권·deal spread 분리 |
| GM | 7 | 2009 call Short, 2012 Long | 2011·2017 Long | 구주/New GM·warrant·tech option 분리 |

> 데이터 경고: SQL의 첫 AER은 AerCap이 아니라 캐나다 Groupe Aeroplan/Aimia다. 미국 AER 가격으로 계산된 성과는 무효 처리했다. 또한 SQL short flag와 실제 본문 방향이 다른 글은 원본을 보존하고 research_direction을 교정했다.

---

# Groupe Aeroplan/Aimia (AER(legacy Canada)) — 기업과 비즈니스

Groupe Aeroplan은 Air Canada의 상용고객 프로그램에서 분리돼 캐나다 Aeroplan과 영국 Nectar 같은 coalition loyalty program을 운영했고 뒤에 Aimia로 사명을 바꿨다. 은행·항공사·소매업체에 포인트를 선판매해 현금을 먼저 받고 고객이 항공권·상품으로 교환할 때 비용이 발생한다. 수익은 포인트 판매가격과 redemption 원가의 spread, 미사용 포인트 breakage, 데이터·마케팅 서비스에서 나온다. 따라서 당기 EBITDA보다 gross billings, redemption reserve, breakage 추정, 핵심 accumulation partner 계약의 갱신과 고객이 실제로 쓸 수 있는 보상좌석이 중요하다. 포인트 float는 저비용자금처럼 보이지만 발행 파트너나 anchor airline이 떠나면 미래 billings와 프로그램 매력이 동시에 훼손된다. 이 회사는 미국 ticker AER인 AerCap과 전혀 다른 캐나다 기업이므로 ticker 기반 성과매칭은 entity 오류를 만든다.

## 돈을 버는 구조

- 포인트 선판매→float 운용→redemption 비용의 시차
- 핵심 moat는 카드사·항공사·회원의 다면 network와 데이터
- breakage 상향은 현금이 아니라 미래부채 추정변경일 수 있음
- anchor airline 계약 종료는 적립과 사용가치를 동시에 훼손

## 아이디어 전체 판정

| 게시일 | 실제 방향 | 추천 증권 | 투자논지 | 결과 | 판정 |
|---|---|---|---|---|---|
| 2011-09-15 | Long | 보통주 | loyalty float 저평가 | DB의 1~5년 성과는 다른 기업 AerCap 가격이라 전부 사용 불가 | 단기 성공·장기 논지 훼손 |

## 1. 2011-09-15 — loyalty float 저평가

**추천 증권·방향:** 보통주 Long

### 원 투자논지

정상화 FCF C$205m·주당 C$1.25, 약 10% yield와 2013년까지 연 10% 성장을 제시했다. 캐나다 coalition의 포인트 spread·21% breakage·C$300m redemption reserve를 안정적 cash cow로 보고 Carlson 통합비·회계변경에 가린 Nectar·analytics·신규 coalition을 공짜 option으로 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 정상화 FCF C$205m·주당 C$1.25, 약 10% yield와 2013년까지 연 10% 성장을 제시했다. 캐나다 coalition의 포인트 spread·21% breakage·C$300m redemption reserve를 안정적 cash cow로 보고 Carlson 통합비·회계변경에 가린 Nectar·analytics·신규 coalition을 공짜 option으로 봤다. | 초기 현금창출은 지속됐지만 핵심위험은 redemption 변동이 아니라 Air Canada·카드사 계약 집중이었다. Air Canada의 2020 계약종료와 새 loyalty 계획 뒤 Aeroplan은 2018년 C$450m+liability assumption에 매각됐다. 더구나 SQL의 미국 AER 가격은 AerCap으로 entity가 틀렸다. |
| 밸류에이션·청구권 | FCF yield 10%·10% 성장 | DB의 1~5년 성과는 다른 기업 AerCap 가격이라 전부 사용 불가 |
| 촉매·시간 | I&C·Aeromexico·India JV | Air Canada가 2020년 이후 독자 loyalty program 계획 발표 |
| 사전 반증조건 | Air Canada와 핵심카드사가 동시에 이탈해도 reserve 차감 후 equity가 보존되는가? | 핵심 오류: ticker/entity collision과 anchor-partner tail 누락 |

### 실제 전개와 투자 결론

초기 현금창출은 지속됐지만 핵심위험은 redemption 변동이 아니라 Air Canada·카드사 계약 집중이었다. Air Canada의 2020 계약종료와 새 loyalty 계획 뒤 Aeroplan은 2018년 C$450m+liability assumption에 매각됐다. 더구나 SQL의 미국 AER 가격은 AerCap으로 entity가 틀렸다.

**종합판정: 단기 성공·장기 논지 훼손.** 핵심 오류·교훈: ticker/entity collision과 anchor-partner tail 누락

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 정상 FCF | C$205m/C$1.25 | 연 10% 성장 | 초기 cash 유지 | 부분 |
| breakage | 21% | 안정 spread | 계약위험이 더 큼 | 프레임 부족 |
| Aeroplan 매각 | 미가정 | compound | 2018 C$450m+부채인수 | 논지변경 |
| 가격데이터 | AER ticker | 성과측정 | AerCap 잘못 매칭 | 무효 |

재사용 질문: **Air Canada와 핵심카드사가 동시에 이탈해도 reserve 차감 후 equity가 보존되는가?**

## 2024-01-31 기준 기업 결론

Air Canada는 기존 계약의 2020년 종료를 앞두고 새 프로그램을 추진했고 2018년 컨소시엄이 Aeroplan 사업을 C$450m 현금과 약 C$1.9bn 포인트부채 인수조건으로 사기로 했다. 원래 Aimia 주주는 cash-generative loyalty compounder가 아니라 핵심자산 매각 뒤 investment holding company를 보유하게 됐다.

## 주요 근거

- [2016 Air Canada investor presentation](https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/speeches-presentations/en/Desjardins-Industrials-Telecom-Consumer-Conference-Montreal-en.pdf) — Aeroplan 계약이 2020년 종료 예정임을 명시.
- [Agreement to acquire Aeroplan loyalty business](https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/en/quarterly-result/2018/2018_FSN_q3.pdf) — C$450m 현금과 약 C$1.9bn 포인트부채 인수조건.
- [Air Canada 2013 financial statements](https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/en/quarterly-result/2013/2013_FSN_q4.pdf) — Aeroplan과의 포인트 매입·항공권 redemption 구조.
- [NYSE AER ticker entity check](https://www.sec.gov/edgar/browse/?CIK=1378789&owner=exclude) — 미국 AER은 AerCap이므로 Aimia 가격성과와 혼용 금지.

---

# AerCap Holdings (AER) — 기업과 비즈니스

AerCap은 Boeing·Airbus에서 항공기를 대량 할인 구매하거나 sale-leaseback으로 취득해 전 세계 항공사에 장기 임대하는 항공금융회사다. 임대료와 정비보상금에서 이자·감가상각·관리비·신용손실을 뺀 spread가 이익이며, lease 종료 뒤 재임대·매각한 residual value가 장기 ROE를 결정한다. 항공기는 이동 가능한 담보지만 기종·연식·엔진·정비상태와 전 세계 공급에 따라 유동성이 다르다. book value는 원가와 감가상각정책의 산물이라 실제 매각가·gain on sale·appraiser value로 검증해야 한다. 반대로 2.5~3배 debt/equity에서 작은 asset haircut도 equity에 크게 확대된다. 핵심 경쟁력은 싼 OEM order book, 저비용·분산조달, airline credit underwriting, repossession·remarketing, 자산매매와 할인된 자사주 사이의 자본배분이다. ILFC와 GECAS 인수는 규모·조달우위를 키웠지만 COVID와 러시아 압류처럼 상관된 tail risk도 커졌다.

## 돈을 버는 구조

- lease yield−funding cost−depreciation/credit loss의 levered spread
- book discount는 기회지만 asset haircut이 leverage로 증폭
- 젊고 범용적인 narrowbody·신기술 기종일수록 remarketing 용이
- 항공기 매각 premium과 할인 자사주가 주당 book 복리의 핵심

## 아이디어 전체 판정

| 게시일 | 실제 방향 | 추천 증권 | 투자논지 | 결과 | 판정 |
|---|---|---|---|---|---|
| 2014-01-27 | Long | 보통주 | ILFC time-arbitrage | 1년 +8.79%, 2년 -18.38%, 5년 +26.31% | 사업 성공·기간 미달 |
| 2015-12-28 | Long | 보통주 | understated book 복리 | 1년 -2.67%, 3년 -10.96%, 5년 +1.77% | 논지 일부 적중·주가 실패 |
| 2017-07-14 | Long | 보통주 | deleveraging·buyback 롱 | 1년 +14.21%, 3년 -37.99%, 5년 -17.37% | 실패 |
| 2018-06-21 | Long | 보통주 | 0.8x book quality finance | 1년 -7.47%, 2년 -41.65%, 3년 +1.88% | 명시기간 실패·3년 회복 |
| 2019-02-06 | Long | 보통주 | liquidity 공포·자본배분 | 1년 +26.93%, 2년 -5.43%, 3년 +36.42% | 성공·큰 경로위험 |
| 2020-08-17 | Long | 보통주 | COVID cyclical trough | 1년 +76.68%, 2년 +60.26% | 매우 성공 |
| 2022-02-05 | Long | 보통주 | GECAS accretion·buyback | 1년 -2.60%; 2024-01-31에는 진입가 상회 | 부분 성공·tail shock |

## 1. 2014-01-27 — ILFC time-arbitrage

**추천 증권·방향:** 보통주 Long

### 원 투자논지

AIG의 forced sale로 ILFC를 싸게 인수해 fleet가 327대에서 약 1,300대로 커지고 3년 lease revenue 80%가 계약된다고 봤다. pro forma book 약 1.2x, ROE 15~17%, 2016 EPS $5.50과 cost·tax·funding synergy가 24개월 rerating을 만든다는 논지였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | AIG의 forced sale로 ILFC를 싸게 인수해 fleet가 327대에서 약 1,300대로 커지고 3년 lease revenue 80%가 계약된다고 봤다. pro forma book 약 1.2x, ROE 15~17%, 2016 EPS $5.50과 cost·tax·funding synergy가 24개월 rerating을 만든다는 논지였다. | ILFC 거래는 종결·통합됐고 scale·funding·EPS가 개선됐다. 그러나 2년 가격은 -18.38%였고 5년 +26.31%로 time-arbitrage가 예상보다 길었다. 좋은 M&A도 업종 multiple과 macro를 즉시 바꾸지는 못했다. |
| 밸류에이션·청구권 | 1.2x PF book·2016 EPS $5.50 | 1년 +8.79%, 2년 -18.38%, 5년 +26.31% |
| 촉매·시간 | deal close·synergy·debt repricing | 2년 -18.38%로 명시기간 수익 실패 |
| 사전 반증조건 | EPS가 맞아도 P/B가 0.8x로 내려가면 목표 IRR은? | 핵심 오류: 통합가치를 24개월 multiple expansion으로 직결 |

### 실제 전개와 투자 결론

ILFC 거래는 종결·통합됐고 scale·funding·EPS가 개선됐다. 그러나 2년 가격은 -18.38%였고 5년 +26.31%로 time-arbitrage가 예상보다 길었다. 좋은 M&A도 업종 multiple과 macro를 즉시 바꾸지는 못했다.

**종합판정: 사업 성공·기간 미달.** 핵심 오류·교훈: 통합가치를 24개월 multiple expansion으로 직결

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| fleet | 327+ILFC 1,002 | 세계 2위 | 통합 완료 | 적중 |
| ROE | 15~17% | 유지 | double digit | 적중 |
| 2년수익 | 상승 | time-arb | -18.38% | 실패 |
| 5년수익 | 상승 | 장기회수 | +26.31% | 부분 |

재사용 질문: **EPS가 맞아도 P/B가 0.8x로 내려가면 목표 IRR은?**

## 2. 2015-12-28 — understated book 복리

**추천 증권·방향:** 보통주 Long

### 원 투자논지

book $40.80에 외부 appraisal가 fleet를 $3.3bn/$16주당 높게 평가했고, 매각이익이 과도한 감가를 증명한다고 봤다. 2018년 book 50% 증가·EPS $7~8, 1.2x book이면 약 18% IRR을 기대했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | book $40.80에 외부 appraisal가 fleet를 $3.3bn/$16주당 높게 평가했고, 매각이익이 과도한 감가를 증명한다고 봤다. 2018년 book 50% 증가·EPS $7~8, 1.2x book이면 약 18% IRR을 기대했다. | book·earnings는 성장했으나 주가는 1년 -2.67%, 3년 -10.96%, 5년 +1.77%에 그쳤다. book가 늘어도 aircraft cycle·funding 우려가 P/B를 계속 눌렀고 COVID가 5년 종착점을 훼손했다. |
| 밸류에이션·청구권 | appraised book premium·1.2x 목표 | 1년 -2.67%, 3년 -10.96%, 5년 +1.77% |
| 촉매·시간 | IG rating·시장 이해 | COVID로 airline rent·asset value 동시 충격 |
| 사전 반증조건 | P/B 0.5x와 asset haircut 15%가 동시에 와도 equity IRR이 양수인가? | 핵심 오류: book growth와 multiple 정상화를 중복 upside로 가정 |

### 실제 전개와 투자 결론

book·earnings는 성장했으나 주가는 1년 -2.67%, 3년 -10.96%, 5년 +1.77%에 그쳤다. book가 늘어도 aircraft cycle·funding 우려가 P/B를 계속 눌렀고 COVID가 5년 종착점을 훼손했다.

**종합판정: 논지 일부 적중·주가 실패.** 핵심 오류·교훈: book growth와 multiple 정상화를 중복 upside로 가정

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| book | 주당 $40.80 | 2018 +50% | 성장 | 적중 |
| EPS | $7~8 | 2018 | 증가 | 부분 |
| 3년수익 | 상승 | ~18% IRR | -10.96% | 실패 |
| 5년수익 | 복리 | 상승 | +1.77% | 실패 |

재사용 질문: **P/B 0.5x와 asset haircut 15%가 동시에 와도 equity IRR이 양수인가?**

## 3. 2017-07-14 — deleveraging·buyback 롱

**추천 증권·방향:** 보통주 Long

### 원 투자논지

ILFC 통합 뒤 debt/equity 3.7x→2.7x, share count 215m→176m, book/share $35.28→$51.20인데 주가는 mid-$40에 그대로라고 봤다. appraised book $68·0.7x와 aircraft premium 매각 후 할인 자사주를 핵심 복리로 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | ILFC 통합 뒤 debt/equity 3.7x→2.7x, share count 215m→176m, book/share $35.28→$51.20인데 주가는 mid-$40에 그대로라고 봤다. appraised book $68·0.7x와 aircraft premium 매각 후 할인 자사주를 핵심 복리로 제시했다. | 자사주와 book growth는 맞았지만 3년 -37.99%, 5년 -17.37%였다. 2020 COVID가 항공사 신용·fleet value·조달을 함께 때려 ‘매각 가능한 book’ 하방이 위기 중 작동하지 않았다. |
| 밸류에이션·청구권 | 0.9x book/0.7x appraised book | 1년 +14.21%, 3년 -37.99%, 5년 -17.37% |
| 촉매·시간 | 자산매각·buyback·잠재 M&A | COVID로 lease deferral·impairment 우려 급증 |
| 사전 반증조건 | 전 세계 항공사가 동시에 현금을 보존할 때 appraised value로 누가 사는가? | 핵심 오류: 평시 매각 premium을 stress liquidation value로 사용 |

### 실제 전개와 투자 결론

자사주와 book growth는 맞았지만 3년 -37.99%, 5년 -17.37%였다. 2020 COVID가 항공사 신용·fleet value·조달을 함께 때려 ‘매각 가능한 book’ 하방이 위기 중 작동하지 않았다.

**종합판정: 실패.** 핵심 오류·교훈: 평시 매각 premium을 stress liquidation value로 사용

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| D/E | 2.7x | 계속 감소 | 후일 GECAS로 재증가 | 부분 |
| share count | 215m→176m | buyback | 감소 | 적중 |
| 3년수익 | 상승 | book 회수 | -37.99% | 실패 |
| 5년수익 | 상승 | 장기복리 | -17.37% | 실패 |

재사용 질문: **전 세계 항공사가 동시에 현금을 보존할 때 appraised value로 누가 사는가?**

## 4. 2018-06-21 — 0.8x book quality finance

**추천 증권·방향:** 보통주 Long

### 원 투자논지

10년 book CAGR 17%, 평균 gain on sale 7%, 평균 fleet age 7년·lease term 6.6년을 근거로 $54가 2018 year-end book의 0.8x라고 봤다. 2020 book $80~85, 1.0x면 17~19%, 1.2x면 26~29% CAGR을 기대했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 10년 book CAGR 17%, 평균 gain on sale 7%, 평균 fleet age 7년·lease term 6.6년을 근거로 $54가 2018 year-end book의 0.8x라고 봤다. 2020 book $80~85, 1.0x면 17~19%, 1.2x면 26~29% CAGR을 기대했다. | 운영·book는 위기 전까지 견조했으나 2년 -41.65%로 COVID를 맞았고 3년 +1.88%로 회복했다. leverage 사업의 과거 무손실 기록은 전 세계 운항중단이라는 미관측 tail을 배제하지 못한다. |
| 밸류에이션·청구권 | 0.8x 2018E book·2020 $80~85 | 1년 -7.47%, 2년 -41.65%, 3년 +1.88% |
| 촉매·시간 | buyback·M&A·book discount 축소 | 2년 시점 COVID drawdown |
| 사전 반증조건 | 동시에 25% rent deferral·15% asset haircut이면 tangible book는? | 핵심 오류: 과거 금융위기 생존을 모든 항공수요 shock에 일반화 |

### 실제 전개와 투자 결론

운영·book는 위기 전까지 견조했으나 2년 -41.65%로 COVID를 맞았고 3년 +1.88%로 회복했다. leverage 사업의 과거 무손실 기록은 전 세계 운항중단이라는 미관측 tail을 배제하지 못한다.

**종합판정: 명시기간 실패·3년 회복.** 핵심 오류·교훈: 과거 금융위기 생존을 모든 항공수요 shock에 일반화

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| fleet age | 7년 | liquidity | 젊은 fleet 방어 | 부분 |
| gain on sale | 평균 7% | book 보수성 | 평시 확인 | 적중 |
| 2년수익 | 상승 | 17~29% CAGR | -41.65% | 실패 |
| 3년수익 | 회복 | 복리 | +1.88% | 미달 |

재사용 질문: **동시에 25% rent deferral·15% asset haircut이면 tangible book는?**

## 5. 2019-02-06 — liquidity 공포·자본배분

**추천 증권·방향:** 보통주 Long

### 원 투자논지

952 owned+105 managed aircraft, 평균 age 6.6년·lease 7.1년, 지속 low-double-digit ROE인데 6.9x EPS·0.77x book라고 봤다. 2.7x D/E라도 committed liquidity와 장기 lease·asset sale이 purchase commitments를 감당하고, 시간이 지나면 할인 자사주가 가치를 만든다는 논지였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 952 owned+105 managed aircraft, 평균 age 6.6년·lease 7.1년, 지속 low-double-digit ROE인데 6.9x EPS·0.77x book라고 봤다. 2.7x D/E라도 committed liquidity와 장기 lease·asset sale이 purchase commitments를 감당하고, 시간이 지나면 할인 자사주가 가치를 만든다는 논지였다. | 1년 +26.93%였으나 2년 -5.43%, 3년 +36.42%로 큰 COVID 경로를 겪었다. liquidity 준비와 fleet quality가 생존·회복을 만들었다는 핵심은 맞았지만 안정적 경로는 아니었다. |
| 밸류에이션·청구권 | 6.9x EPS·0.77x book | 1년 +26.93%, 2년 -5.43%, 3년 +36.42% |
| 촉매·시간 | time·capital allocation | 전 세계 운항중단으로 thesis stress |
| 사전 반증조건 | 12개월 자본시장 폐쇄와 rent 30% 미수에도 commitments를 자체 현금으로 지키는가? | 핵심 오류: liquidity tail 규모를 과소평가했으나 실제 buffer 충분 |

### 실제 전개와 투자 결론

1년 +26.93%였으나 2년 -5.43%, 3년 +36.42%로 큰 COVID 경로를 겪었다. liquidity 준비와 fleet quality가 생존·회복을 만들었다는 핵심은 맞았지만 안정적 경로는 아니었다.

**종합판정: 성공·큰 경로위험.** 핵심 오류·교훈: liquidity tail 규모를 과소평가했으나 실제 buffer 충분

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| fleet | 952 owned | 분산 | 생존 | 적중 |
| D/E | 2.7x | 관리 가능 | liquidity 유지 | 적중 |
| 1년수익 | 상승 | rerating | +26.93% | 적중 |
| 3년수익 | 상승 | 복리 | +36.42% | 성공 |

재사용 질문: **12개월 자본시장 폐쇄와 rent 30% 미수에도 commitments를 자체 현금으로 지키는가?**

## 6. 2020-08-17 — COVID cyclical trough

**추천 증권·방향:** 보통주 Long

### 원 투자논지

$30·0.4x book에서 900+ aircraft, age 6.2년, lease term 7년+, contracted revenue $40bn을 샀다. 정부의 airline 지원, vaccine·여행회복, 구형기 퇴역으로 AER lease demand가 회복돼 24개월 두 배가 가능하다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $30·0.4x book에서 900+ aircraft, age 6.2년, lease term 7년+, contracted revenue $40bn을 샀다. 정부의 airline 지원, vaccine·여행회복, 구형기 퇴역으로 AER lease demand가 회복돼 24개월 두 배가 가능하다고 봤다. | COVID 손상과 rent relief를 견디고 여행이 회복돼 1년 +76.68%, 2년 +60.26%였다. 정확히 두 배에는 못 미쳤지만 stress 가격·liquidity·범용 fleet 조합이 매우 성공했다. |
| 밸류에이션·청구권 | 0.4x book·24개월 2배 | 1년 +76.68%, 2년 +60.26% |
| 촉매·시간 | vaccine·정부지원·운항회복 | 정부지원·백신 진전과 자본시장 접근 유지 |
| 사전 반증조건 | book 25% 손상 뒤에도 0.4x 진입가 대비 upside가 남는가? | 핵심 오류: book impairment를 인정하고도 충분한 discount 확보 |

### 실제 전개와 투자 결론

COVID 손상과 rent relief를 견디고 여행이 회복돼 1년 +76.68%, 2년 +60.26%였다. 정확히 두 배에는 못 미쳤지만 stress 가격·liquidity·범용 fleet 조합이 매우 성공했다.

**종합판정: 매우 성공.** 핵심 오류·교훈: book impairment를 인정하고도 충분한 discount 확보

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| P/B | 0.4x | 정상화 | 상승 | 적중 |
| 계약매출 | $40bn | 가시성 | cash bridge | 적중 |
| 1년수익 | 상승 | 회복 | +76.68% | 성공 |
| 2년수익 | 2배 | +100% | +60.26% | 목표 미달 |

재사용 질문: **book 25% 손상 뒤에도 0.4x 진입가 대비 upside가 남는가?**

## 7. 2022-02-05 — GECAS accretion·buyback

**추천 증권·방향:** 보통주 Long

### 원 투자논지

$63에서 normalized EPS 8x 미만·book 25% 할인, GECAS를 자산 $34bn 대비 cash $24bn+equity $6.6bn에 사 levered 35% 할인이라고 봤다. pro forma economic book $84, low-double-digit ROE와 연 10% buyback으로 2년 rerating을 기대했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $63에서 normalized EPS 8x 미만·book 25% 할인, GECAS를 자산 $34bn 대비 cash $24bn+equity $6.6bn에 사 levered 35% 할인이라고 봤다. pro forma economic book $84, low-double-digit ROE와 연 10% buyback으로 2년 rerating을 기대했다. | 19일 뒤 러시아 침공으로 잔류 항공기·엔진에 약 $3.5bn 보험청구가 생겼고 1년 -2.60%였다. 큰 tail에도 생존해 2023 보험합의·여행회복으로 2024-01-31에는 진입가를 웃돌았다. 장기 사업은 성공했지만 2년 경로는 러시아 risk가 지배했다. |
| 밸류에이션·청구권 | ~8x EPS·0.75x book | 1년 -2.60%; 2024-01-31에는 진입가 상회 |
| 촉매·시간 | GECAS synergy·연 10% buyback | 러시아 침공·항공기 회수 불능 |
| 사전 반증조건 | 한 국가 fleet가 압류되고 보험이 3년 지연돼도 covenant·buyback이 유지되는가? | 핵심 오류: 국가압류라는 correlated asset/legal tail 미모델링 |

### 실제 전개와 투자 결론

19일 뒤 러시아 침공으로 잔류 항공기·엔진에 약 $3.5bn 보험청구가 생겼고 1년 -2.60%였다. 큰 tail에도 생존해 2023 보험합의·여행회복으로 2024-01-31에는 진입가를 웃돌았다. 장기 사업은 성공했지만 2년 경로는 러시아 risk가 지배했다.

**종합판정: 부분 성공·tail shock.** 핵심 오류·교훈: 국가압류라는 correlated asset/legal tail 미모델링

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $63 | book 회수 | 2024초 상회 | 부분 |
| economic book | $84 | 성장 | 러시아 손상 후 회복 | 부분 |
| 러시아 claim | 미가정 | 없음 | ~$3.5bn | tail |
| 1년수익 | 상승 | rerating | -2.60% | 실패 |

재사용 질문: **한 국가 fleet가 압류되고 보험이 3년 지연돼도 covenant·buyback이 유지되는가?**

## 2024-01-31 기준 기업 결론

AerCap은 2021년 GECAS를 인수해 세계 최대 lessor가 됐다. 2022년 러시아 잔류 항공기·엔진에 약 $3.5bn 보험청구를 제출했으며 큰 손실에도 생존했고 2023년 일부 러시아 보험합의와 여행회복으로 주가·book가 회복됐다.

## 주요 근거

- [AerCap 2023 Form 20-F](https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-24-000010/aer-20231231.htm) — fleet·부채·book·러시아 손실과 보험청구.
- [GECAS transaction completion](https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-22-000022/aer-09302022x6k.htm) — GE에 111.5m주·약 $23bn 현금·$1bn notes 지급.
- [AerCap Q1 2022 results](https://www.aercap.com/news-media/press-releases/detail/415/aercap-holdings-n-v-reports-financial-results-for-the) — 러시아 자산 약 $3.5bn 보험청구.
- [AerCap 2022 Form 20-F](https://www.aercap.com/investors/shareholder-services/sec-filings/content/0001378789-23-000006/aer-20221231.htm) — COVID·GECAS·러시아 뒤 연결재무 검증.

---

# Hertz Global Holdings (HTZ) — 기업과 비즈니스

Hertz는 공항·도심에서 차량을 단기대여하고 보유기간이 지난 fleet를 중고차로 매각한다. 매출은 rental days×revenue per day와 부가상품에서 나오지만 진짜 spread는 임대료에서 차량감가·이자·공항수수료·운영비를 뺀 금액이다. 차량은 대개 ABS·asset-backed facility로 조달되어 corporate debt와 법적으로 분리되더라도, 수요급락·중고차가격 하락·borrowing-base 축소가 동시에 오면 현금이 급격히 사라진다. fleet는 12~24개월 안에 조절할 수 있지만 고정 공항시설·IT·인력과 one-way imbalance가 operating leverage를 만든다. 업계 3사 과점은 pricing을 돕지만 각사가 시장점유율을 좇으면 과잉 fleet가 된다. 2013 Dollar Thrifty 통합·회계문제, Icahn 지배, 2016 HERC 분사, 2020 COVID Chapter 11, 2021 재상장은 경제적으로 다른 증권을 만들었다.

## 돈을 버는 구조

- rental rate·utilization−월 차량감가−fleet financing spread
- 중고차가격 상승은 감가를 낮추지만 되돌릴 수 있는 cycle 이익
- vehicle ABS와 corporate debt·liquidity를 분리 분석
- 파산 전 HTZGQ와 재편 후 HTZ는 서로 다른 equity

## 아이디어 전체 판정

| 게시일 | 실제 방향 | 추천 증권 | 투자논지 | 결과 | 판정 |
|---|---|---|---|---|---|
| 2013-01-08 | Long | 보통주 | Dollar Thrifty synergy | 정밀 SQL 성과 없음; 단기 목표권 도달 후 2020 파산 | 단기 성공·장기 실패 |
| 2014-01-20 | Long | 보통주 | activist·HERC SOTP | 정밀 SQL 성과 없음; $45~49/12개월 미달 | 실패 |
| 2017-05-31 | Long | 보통주 | kitchen-sink turnaround | 정밀 SQL 성과 없음; 반등 후 2020 구주 훼손 | 부분 성공 후 실패 |
| 2017-08-31 | Short | 보통주·자본구조 | rideshare·leverage 숏 | 정밀 SQL 성과 없음; 2020 Ch.11 적중 | 매우 성공·회수율 과신 |
| 2018-09-04 | Long | 보통주 | rideshare 과장 반론 | 정밀 SQL 성과 없음; 2020 Ch.11 | 치명적 실패 |
| 2019-05-14 | Short | 2022 debt | FCF·refinancing 숏 | Chapter 11 적중; 정확 bond total return은 가격자료 부족 | 매우 성공 |
| 2020-06-08 | Short | 콜옵션 매도 | 파산 equity 0 옵션매도 | strike·expiry·premium 불명확; 없는 옵션성과를 생성하지 않음 | 논지 실패·거래판정 불가 |
| 2022-02-18 | Long | 재편 보통주 | post-reorg golden period | 1년 +4.96%; 2024-01-31 기준 2년 목표 크게 미달 | 실패 |

## 1. 2013-01-08 — Dollar Thrifty synergy

**추천 증권·방향:** 보통주 Long

### 원 투자논지

$87.50 현금으로 Dollar Thrifty를 인수한 뒤 2013 EPS $2, cost synergy $0.28, utilization low-80s→high-80s와 10~12x P/E 복귀로 연말 $22를 기대했다. HERC 분사도 추가가치였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $87.50 현금으로 Dollar Thrifty를 인수한 뒤 2013 EPS $2, cost synergy $0.28, utilization low-80s→high-80s와 10~12x P/E 복귀로 연말 $22를 기대했다. HERC 분사도 추가가치였다. | 통합과 HERC 분사는 실행됐지만 회계오류·과잉 fleet·경영문제로 장기 shareholder compounding은 실패했고 구 equity는 2020 Chapter 11을 맞았다. 단기 $22 목표는 도달했어도 장기 사업질 판단은 약했다. |
| 밸류에이션·청구권 | 2013 EPS $2×10~12x | 정밀 SQL 성과 없음; 단기 목표권 도달 후 2020 파산 |
| 촉매·시간 | $0.28 synergy·pricing·HERC | 실적지연·회계조사로 재무 신뢰 훼손 |
| 사전 반증조건 | synergy 전액이 없어도 fleet debt와 corporate debt를 상환하는가? | 핵심 오류: M&A synergy를 integration/회계·fleet risk 없이 자본화 |

### 실제 전개와 투자 결론

통합과 HERC 분사는 실행됐지만 회계오류·과잉 fleet·경영문제로 장기 shareholder compounding은 실패했고 구 equity는 2020 Chapter 11을 맞았다. 단기 $22 목표는 도달했어도 장기 사업질 판단은 약했다.

**종합판정: 단기 성공·장기 실패.** 핵심 오류·교훈: M&A synergy를 integration/회계·fleet risk 없이 자본화

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 목표 | $22 | 연말 | 단기 도달 | 적중 |
| synergy | $0.28 EPS | 실현 | 통합문제 상쇄 | 부분 |
| HERC | 분사 option | 가치실현 | 2016 분사 | 적중 |
| 장기 equity | 복리 | 성장 | 2020 파산 | 실패 |

재사용 질문: **synergy 전액이 없어도 fleet debt와 corporate debt를 상환하는가?**

## 2. 2014-01-20 — activist·HERC SOTP

**추천 증권·방향:** 보통주 Long

### 원 투자논지

Third Point·Corvex·Icahn 참여 뒤 2015 EPS $2.70+에 Avis 14.5x를 적용해 $40, leverage $5/주와 HERC spin $4/주를 더해 12개월 $45~49를 제시했다. 업계 3사가 90%를 장악해 pricing할 것이라 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Third Point·Corvex·Icahn 참여 뒤 2015 EPS $2.70+에 Avis 14.5x를 적용해 $40, leverage $5/주와 HERC spin $4/주를 더해 12개월 $45~49를 제시했다. 업계 3사가 90%를 장악해 pricing할 것이라 봤다. | HERC는 2016년에야 분사됐고 회계 restatement·경영진 교체·fleet 비용으로 12개월 목표는 실패했다. leverage와 buyback은 upside가 아니라 회복탄력성을 낮췄고 2020 파산으로 이어졌다. |
| 밸류에이션·청구권 | 2015 EPS $2.70×14.5x+SOTP | 정밀 SQL 성과 없음; $45~49/12개월 미달 |
| 촉매·시간 | activist·HERC·buyback | 회계오류와 실적가이던스 철회 |
| 사전 반증조건 | HERC 지연·EPS 30% 미달 때 corporate liquidity는? | 핵심 오류: 레버리지를 가치창출로 더하고 risk는 빼지 않음 |

### 실제 전개와 투자 결론

HERC는 2016년에야 분사됐고 회계 restatement·경영진 교체·fleet 비용으로 12개월 목표는 실패했다. leverage와 buyback은 upside가 아니라 회복탄력성을 낮췄고 2020 파산으로 이어졌다.

**종합판정: 실패.** 핵심 오류·교훈: 레버리지를 가치창출로 더하고 risk는 빼지 않음

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 목표 | $45~49 | 12개월 | 미달 | 실패 |
| EPS | $2.70+ | 2015 | 하향 | 실패 |
| HERC | $4/주 | near term | 2016 분사 | 지연 |
| leverage | $5/주 upside | accretion | 파산취약성 | 오류 |

재사용 질문: **HERC 지연·EPS 30% 미달 때 corporate liquidity는?**

## 3. 2017-05-31 — kitchen-sink turnaround

**추천 증권·방향:** 보통주 Long

### 원 투자논지

약 $10에서 정상 EPS $3.25×10=$32를 제시했다. 2017 EBITDA margin 3.5% 대 2006~16 평균 10.5%의 괴리는 self-inflicted overfleet이고 새 CEO의 defleet, 중고차가격 회복·pricing, 46% short interest가 반전을 증폭한다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 약 $10에서 정상 EPS $3.25×10=$32를 제시했다. 2017 EBITDA margin 3.5% 대 2006~16 평균 10.5%의 괴리는 self-inflicted overfleet이고 새 CEO의 defleet, 중고차가격 회복·pricing, 46% short interest가 반전을 증폭한다고 봤다. | 주가는 저점에서 반등했지만 $32와 정상 margin을 지속적으로 달성하지 못했고 2020 파산했다. Uber 위협 과장은 맞았으나 commodity spread와 balance sheet가 더 큰 원인이었다. |
| 밸류에이션·청구권 | 3x normalized earnings·목표 $32 | 정밀 SQL 성과 없음; 반등 후 2020 구주 훼손 |
| 촉매·시간 | defleet·residual·pricing·short squeeze | margin 회복이 목표보다 약하고 debt 지속 |
| 사전 반증조건 | normalized margin이 6%에 불과해도 debt service 후 equity가 남는가? | 핵심 오류: 과거 평균 margin을 자동 정상값으로 사용 |

### 실제 전개와 투자 결론

주가는 저점에서 반등했지만 $32와 정상 margin을 지속적으로 달성하지 못했고 2020 파산했다. Uber 위협 과장은 맞았으나 commodity spread와 balance sheet가 더 큰 원인이었다.

**종합판정: 부분 성공 후 실패.** 핵심 오류·교훈: 과거 평균 margin을 자동 정상값으로 사용

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | ~$10 | 목표 $32 | 반등/미달 | 부분 |
| margin | 3.5% | 10.5% 정상화 | 미달 | 실패 |
| short interest | 46% | squeeze | 반등 | 적중 |
| 최종 | turnaround | 생존 | 2020 Ch.11 | 실패 |

재사용 질문: **normalized margin이 6%에 불과해도 debt service 후 equity가 남는가?**

## 4. 2017-08-31 — rideshare·leverage 숏

**추천 증권·방향:** 보통주·자본구조 Short

### 원 투자논지

공항 고정비·세금, Uber가 빼앗는 고마진 business trip, massive vehicle/corporate leverage와 작은 revenue 하락의 EBITDA 증폭을 근거로 equity와 자본구조 전체가 결국 0에 가깝다고 봤다. covenant 위반·cash burn·defensive Ch.11을 촉매로 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 공항 고정비·세금, Uber가 빼앗는 고마진 business trip, massive vehicle/corporate leverage와 작은 revenue 하락의 EBITDA 증폭을 근거로 equity와 자본구조 전체가 결국 0에 가깝다고 봤다. covenant 위반·cash burn·defensive Ch.11을 촉매로 제시했다. | Hertz는 2020년 Chapter 11을 신청해 핵심 solvency 논지가 맞았다. 다만 2017~18 큰 squeeze와 파산경쟁입찰로 구주주도 이례적 회수를 받아 ‘완전한 0’은 틀렸다. debt tranche별 결과도 달라 자본구조 전체 short는 과도했다. |
| 밸류에이션·청구권 | equity/convertible/debt 과대평가 | 정밀 SQL 성과 없음; 2020 Ch.11 적중 |
| 촉매·시간 | covenant·cash burn·Ch.11 | Chapter 11 신청 |
| 사전 반증조건 | 파산해도 used-car 급등과 sponsor bidding이 recovery를 높이면 각 tranche 손익은? | 핵심 오류: 방향은 맞았으나 모든 청구권 0으로 일반화 |

### 실제 전개와 투자 결론

Hertz는 2020년 Chapter 11을 신청해 핵심 solvency 논지가 맞았다. 다만 2017~18 큰 squeeze와 파산경쟁입찰로 구주주도 이례적 회수를 받아 ‘완전한 0’은 틀렸다. debt tranche별 결과도 달라 자본구조 전체 short는 과도했다.

**종합판정: 매우 성공·회수율 과신.** 핵심 오류·교훈: 방향은 맞았으나 모든 청구권 0으로 일반화

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 파산 | 예상 | 촉매 | 2020-05-22 | 적중 |
| rideshare | 핵심 원인 | 수요훼손 | COVID가 직접촉매 | 부분 |
| equity | 0 기대 | 소멸 | 이례적 회수 | 과신 |
| 자본구조 | 전부 short | 손실 | tranche별 상이 | 오류 |

재사용 질문: **파산해도 used-car 급등과 sponsor bidding이 recovery를 높이면 각 tranche 손익은?**

## 5. 2018-09-04 — rideshare 과장 반론

**추천 증권·방향:** 보통주 Long

### 원 투자논지

미국 rental 매출이 2012~17년 GDP와 비슷한 3.9% CAGR이므로 Uber가 산업을 파괴한다는 47% short-interest 서사는 과장됐다고 봤다. price·volume·utilization 개선과 IT rebuild·AV partnership이 turnaround를 만든다는 롱이었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 미국 rental 매출이 2012~17년 GDP와 비슷한 3.9% CAGR이므로 Uber가 산업을 파괴한다는 47% short-interest 서사는 과장됐다고 봤다. price·volume·utilization 개선과 IT rebuild·AV partnership이 turnaround를 만든다는 롱이었다. | 산업매출이 유지된다는 반론은 맞았지만 Hertz equity는 2020 파산했다. 산업수요와 개별회사의 cost·debt·fleet discipline을 혼동한 사례다. |
| 밸류에이션·청구권 | 높은 upside/short squeeze | 정밀 SQL 성과 없음; 2020 Ch.11 |
| 촉매·시간 | 산업성장·IT·운영개선 | 호황에도 FCF 부족·7.9x corporate leverage 지적 |
| 사전 반증조건 | 산업매출이 GDP만큼 늘어도 회사가 FCF를 못 만들면 왜 equity가 사는가? | 핵심 오류: 산업생존을 levered issuer 생존으로 대체 |

### 실제 전개와 투자 결론

산업매출이 유지된다는 반론은 맞았지만 Hertz equity는 2020 파산했다. 산업수요와 개별회사의 cost·debt·fleet discipline을 혼동한 사례다.

**종합판정: 치명적 실패.** 핵심 오류·교훈: 산업생존을 levered issuer 생존으로 대체

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 산업매출 | 2012~17 3.9% CAGR | 지속 | 산업 생존 | 적중 |
| short interest | 47% | squeeze | 경로 변동 | 부분 |
| issuer FCF | 회복 기대 | 양수 | 호황에도 약함 | 실패 |
| 최종 | turnaround | 생존 | Ch.11 | 실패 |

재사용 질문: **산업매출이 GDP만큼 늘어도 회사가 FCF를 못 만들면 왜 equity가 사는가?**

## 6. 2019-05-14 — FCF·refinancing 숏

**추천 증권·방향:** 2022 debt Short

### 원 투자논지

2018년 utilization·used-car·pricing 호황에도 adjusted FCF $99m뿐이고 debt/total capital 94%, net corporate debt/EBITDA 7.9x, 2015년 이후 EBIT가 이자를 못 덮는다고 봤다. 2022 2nd lien/unsecured notes를 팔아 2020/21 refinancing 실패에 베팅했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 2018년 utilization·used-car·pricing 호황에도 adjusted FCF $99m뿐이고 debt/total capital 94%, net corporate debt/EBITDA 7.9x, 2015년 이후 EBIT가 이자를 못 덮는다고 봤다. 2022 2nd lien/unsecured notes를 팔아 2020/21 refinancing 실패에 베팅했다. | 2020 Chapter 11로 solvency·refinancing 촉매가 1년 만에 현실화됐다. COVID는 예상 밖 직접촉매였지만 호황에도 현금이 없다는 사전취약성 분석이 정확했다. 구체 채권 회수는 tranche·가격에 따라 달라진다. |
| 밸류에이션·청구권 | 7.9x net debt/EBITDA·FCF $99m | Chapter 11 적중; 정확 bond total return은 가격자료 부족 |
| 촉매·시간 | residual 하락·debt market close·Icahn 매도 | Chapter 11 신청 |
| 사전 반증조건 | COVID 없이도 2021 만기까지 cash burn으로 covenant가 깨지는가? | 핵심 오류: tail 촉매는 달랐지만 취약성 인과 적중 |

### 실제 전개와 투자 결론

2020 Chapter 11로 solvency·refinancing 촉매가 1년 만에 현실화됐다. COVID는 예상 밖 직접촉매였지만 호황에도 현금이 없다는 사전취약성 분석이 정확했다. 구체 채권 회수는 tranche·가격에 따라 달라진다.

**종합판정: 매우 성공.** 핵심 오류·교훈: tail 촉매는 달랐지만 취약성 인과 적중

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| FCF | 2018 $99m | 악화 | liquidity 붕괴 | 적중 |
| leverage | 7.9x | refi 실패 | Ch.11 | 적중 |
| interest cover | 2015후 <1x | 지속 | default | 적중 |
| 촉매 | used-car/refi | 2020~21 | COVID | 다른 직접원인 |

재사용 질문: **COVID 없이도 2021 만기까지 cash burn으로 covenant가 깨지는가?**

## 7. 2020-06-08 — 파산 equity 0 옵션매도

**추천 증권·방향:** 콜옵션 매도 Short

### 원 투자논지

이미 Chapter 11인데 자산 $25.8bn·장부 equity $1.49bn에서 비용을 빼면 보통주가 0이라 보고 borrow 대신 높은 implied vol의 call을 매도했다. 임직원 $1 부근 매도와 meme short squeeze 종료를 촉매로 삼았다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 이미 Chapter 11인데 자산 $25.8bn·장부 equity $1.49bn에서 비용을 빼면 보통주가 0이라 보고 borrow 대신 높은 implied vol의 call을 매도했다. 임직원 $1 부근 매도와 meme short squeeze 종료를 촉매로 삼았다. | 파산은 맞았지만 used-car 급등과 sponsor bidding war로 구주주가 cash·신주·warrant를 받은 이례적 사례가 됐다. strike·expiry가 원문에 명확하지 않아 옵션 trade 수익은 판정할 수 없고 ‘equity recovery 0’ 논지는 실패했다. |
| 밸류에이션·청구권 | 파산장부 equity 소멸 | strike·expiry·premium 불명확; 없는 옵션성과를 생성하지 않음 |
| 촉매·시간 | IV collapse·squeeze 종료 | 재편 sponsor 경쟁으로 equity recovery 발생 |
| 사전 반증조건 | asset price와 plan bidding이 급등해 equity에 option value가 생길 확률은? | 핵심 오류: 파산=보통주 무조건 0이라는 회수율 오류 |

### 실제 전개와 투자 결론

파산은 맞았지만 used-car 급등과 sponsor bidding war로 구주주가 cash·신주·warrant를 받은 이례적 사례가 됐다. strike·expiry가 원문에 명확하지 않아 옵션 trade 수익은 판정할 수 없고 ‘equity recovery 0’ 논지는 실패했다.

**종합판정: 논지 실패·거래판정 불가.** 핵심 오류·교훈: 파산=보통주 무조건 0이라는 회수율 오류

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Chapter 11 | 이미 신청 | 지속 | 맞음 | 사실 |
| equity recovery | 0 | 없음 | cash+신주+warrant | 실패 |
| 옵션조건 | 미기재 | 수익 | 판정불가 | 데이터부족 |
| IV | 매우 높음 | collapse | 경로 불명 | 미확정 |

재사용 질문: **asset price와 plan bidding이 급등해 equity에 option value가 생길 확률은?**

## 8. 2022-02-18 — post-reorg golden period

**추천 증권·방향:** 재편 보통주 Long

### 원 투자논지

$18.35에서 debt-free에 가까운 재편회사, 차량공급 부족·중고차가격 +70%·높은 rental rate로 2022 EBITDA $2.9bn을 예상했다. base $26, high $34, bull $40이며 2년간 float 90% 상당 buyback과 Tesla/Uber/Carvana partnership을 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $18.35에서 debt-free에 가까운 재편회사, 차량공급 부족·중고차가격 +70%·높은 rental rate로 2022 EBITDA $2.9bn을 예상했다. base $26, high $34, bull $40이며 2년간 float 90% 상당 buyback과 Tesla/Uber/Carvana partnership을 제시했다. | 1년은 +4.96%였지만 차량공급·중고차 호황이 정상화되고 EV 감가가 커져 2024-01-31 주가는 진입가보다 크게 낮았다. peak depreciation benefit을 normalized EBITDA로 사용한 것이 핵심 오류다. |
| 밸류에이션·청구권 | base $26·bull $40 | 1년 +4.96%; 2024-01-31 기준 2년 목표 크게 미달 |
| 촉매·시간 | 2022 EBITDA·buyback·index | fleet depreciation·Tesla 가격인하 부담 확대 |
| 사전 반증조건 | used-car 가격이 pre-COVID로 정상화돼도 $1.6bn EBITDA와 buyback이 가능한가? | 핵심 오류: cycle windfall을 구조적 oligopoly margin으로 정상화 |

### 실제 전개와 투자 결론

1년은 +4.96%였지만 차량공급·중고차 호황이 정상화되고 EV 감가가 커져 2024-01-31 주가는 진입가보다 크게 낮았다. peak depreciation benefit을 normalized EBITDA로 사용한 것이 핵심 오류다.

**종합판정: 실패.** 핵심 오류·교훈: cycle windfall을 구조적 oligopoly margin으로 정상화

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $18.35 | base $26 | 2024초 크게 하회 | 실패 |
| 2022 EBITDA | $2.9bn | 호황 | 높았으나 비지속 | 부분 |
| buyback | float 90%/2년 | 실행 | 과도 | 실패 |
| 1년수익 | 상승 | rerating | +4.96% | 미달 |

재사용 질문: **used-car 가격이 pre-COVID로 정상화돼도 $1.6bn EBITDA와 buyback이 가능한가?**

## 2024-01-31 기준 기업 결론

Hertz는 2020년 5월 Chapter 11을 신청했고 bidding competition 덕분에 구주주도 이례적으로 cash·신주·warrant를 받았다. 2021년 6월 재편에서 나온 새 equity는 저부채였지만 2022년의 차량부족·중고차 호황이 정상화되고 대규모 EV fleet의 감가가 커지면서 2024년 초 주가가 크게 낮아졌다.

## 주요 근거

- [Hertz Chapter 11 filing 8-K](https://www.sec.gov/Archives/edgar/data/1657853/000110465920065674/tm2020858d1_8k.htm) — 2020-05-22 파산과 fleet debt automatic stay.
- [Hertz 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/47129/000165785322000012/htz-20211231.htm) — 재편·rights offering·새 자본구조.
- [Hertz post-reorg registration](https://www.sec.gov/Archives/edgar/data/1657853/000110465921126784/tm2128732-1_s1.htm) — Chapter 11 plan과 sponsor 자본투입.
- [Hertz SEC filings](https://ir.hertz.com/financials/sec-filings/default.aspx) — 연도별 fleet·감가·부채·실적 검증.

---

# Spirit Airlines (SAVE) — 기업과 비즈니스

Spirit은 Airbus 단일기종에 좌석을 촘촘히 배치하고 기본운임을 낮춘 뒤 수하물·좌석지정·기내판매 등 ancillary fee를 받는 미국 ultra-low-cost carrier다. 단위경제는 passenger flight segment당 total revenue에서 fuel·labor·airport·maintenance·aircraft ownership을 뺀 값이며 CASM ex-fuel, TRASM, load factor, aircraft utilization과 ancillary per passenger가 핵심이다. 낮은 CASM은 가격우위를 만들지만 항공기는 장기주문·lease로 고정되고 pilot·airport·정비는 단기에 줄이기 어려워 과잉 capacity와 가격경쟁이 margin을 빠르게 없앤다. 저유가 때 legacy carrier가 basic economy로 가격을 낮추면 비용격차가 운임격차로 연결되지 않을 수 있다. EETC 채권자는 특정 항공기 담보와 waterfall을 갖지만 보통주는 모든 연료·노무·규제·유동성 위험 뒤의 잔여청구권이다. 2022년 Frontier와 JetBlue 경쟁입찰 뒤에는 영업주가 아니라 antitrust merger-arb가 됐다.

## 돈을 버는 구조

- 낮은 CASM·고밀도 좌석·높은 utilization이 기본 moat
- ancillary revenue가 낮은 base fare를 보조
- fleet 성장률보다 mature route RASM과 증분 ROIC가 중요
- EETC 담보가치와 common equity·merger spread를 분리

## 아이디어 전체 판정

| 게시일 | 실제 방향 | 추천 증권 | 투자논지 | 결과 | 판정 |
|---|---|---|---|---|---|
| 2012-03-12 | Long | 보통주 | 초기 ULCC 성장 롱 | 초기 수년 큰 주가상승; 장기에는 cycle 반전 | 성공 |
| 2013-01-23 | Long | 보통주 | 비용우위·장기 runway 롱 | 2013~14 큰 상승; 이후 고점 대비 급락 | 매우 성공 |
| 2015-10-28 | Long | 보통주 | 가격전쟁 과잉반응 롱 | 5년 보유경로에서 큰 손실·COVID 충격 | 실패 |
| 2017-05-09 | Long | 보통주 | 유가상승 수혜형 ULCC 롱 | 진입 $55.50에서 장기 대폭 하락 | 치명적 실패 |
| 2018-04-17 | Long | 보통주 | fleet 성장·earnings double 롱 | 1~5년 경로에서 목표 EPS·기업가치 미달 | 실패 |
| 2020-06-18 | Long | 2015/2017 EETC 채권 | 항공기 담보채권 롱 | 2024-01-31까지 default 없이 coupon·가격회복 | 성공 |
| 2022-05-05 | Long | 합병차익 보통주 | Frontier hedge·JetBlue optionality | 2024-01-16 법원 차단; merger spread 손실 | 실패 |

## 1. 2012-03-12 — 초기 ULCC 성장 롱

**추천 증권·방향:** 보통주 Long

### 원 투자논지

37대의 Airbus 단일 fleet와 178석 고밀도 A320, point-to-point 노선, 낮은 기본운임과 수하물·좌석 등 ancillary fee를 결합한 ULCC였다. 2012년 fleet 19%, 2013년 16% 성장과 6.5x EV/EBITDAR를 근거로 34% base·60% bull upside를 기대했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 37대의 Airbus 단일 fleet와 178석 고밀도 A320, point-to-point 노선, 낮은 기본운임과 수하물·좌석 등 ancillary fee를 결합한 ULCC였다. 2012년 fleet 19%, 2013년 16% 성장과 6.5x EV/EBITDAR를 근거로 34% base·60% bull upside를 기대했다. | Spirit은 2014년까지 좌석·노선·이익을 빠르게 늘려 초기 산업공백과 저비용 논지가 적중했다. 다만 같은 fleet 성장모델은 뒤에 legacy basic economy와 ULCC 공급경쟁, 고정 lease 부담을 키웠다. 원 보유기간 기준 성공이지만 영구적 moat로 해석하면 안 된다. |
| 밸류에이션·청구권 | 6.5x EV/EBITDAR·34~60% upside | 초기 수년 큰 주가상승; 장기에는 cycle 반전 |
| 촉매·시간 | fleet 성장·신규노선·ancillary | fleet·매출·이익 성장과 주가상승으로 초기 논지 확인 |
| 사전 반증조건 | 신규 노선의 3년차 RASM이 기존 노선과 같고 fuel·labor가 정상화돼도 증분 ROIC가 높은가? | 핵심 오류: 초기 white-space 성장률을 성숙기 economics로 외삽 |

### 실제 전개와 투자 결론

Spirit은 2014년까지 좌석·노선·이익을 빠르게 늘려 초기 산업공백과 저비용 논지가 적중했다. 다만 같은 fleet 성장모델은 뒤에 legacy basic economy와 ULCC 공급경쟁, 고정 lease 부담을 키웠다. 원 보유기간 기준 성공이지만 영구적 moat로 해석하면 안 된다.

**종합판정: 성공.** 핵심 오류·교훈: 초기 white-space 성장률을 성숙기 economics로 외삽

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| fleet | 37대 | 2012 +19%/2013 +16% | 빠른 확대 | 적중 |
| A320 seats | 178 | 저 CASM | 고밀도 유지 | 적중 |
| multiple | 6.5x EV/EBITDAR | rerating | 초기 상승 | 적중 |
| 장기 moat | ULCC cost | 지속 | 경쟁으로 약화 | 부분 |

재사용 질문: **신규 노선의 3년차 RASM이 기존 노선과 같고 fuel·labor가 정상화돼도 증분 ROIC가 높은가?**

## 2. 2013-01-23 — 비용우위·장기 runway 롱

**추천 증권·방향:** 보통주 Long

### 원 투자논지

forward EPS 약 10x, 순현금 차감 7x에 40%+ after-tax ROIC를 내는 성장주로 봤다. CASM은 JetBlue보다 19%, Southwest보다 8% 낮고 break-even fare는 $58 대 $133/$103이라 경기와 fare war에도 유리하며, 미국 ULCC 침투 여지가 크다는 논지였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | forward EPS 약 10x, 순현금 차감 7x에 40%+ after-tax ROIC를 내는 성장주로 봤다. CASM은 JetBlue보다 19%, Southwest보다 8% 낮고 break-even fare는 $58 대 $133/$103이라 경기와 fare war에도 유리하며, 미국 ULCC 침투 여지가 크다는 논지였다. | 저비용과 ancillary 모델은 2013~14 매우 강한 성장을 만들었다. 그러나 높은 reported ROIC는 aircraft lease를 자본화하면 high-teens로 낮아지고, 경쟁사가 basic economy 가격을 맞추자 비용격차가 수익격차로 그대로 남지 않았다. 진입·보유기간은 성공, 장기 품질 평가는 과도했다. |
| 밸류에이션·청구권 | 10x forward EPS·7x ex-cash | 2013~14 큰 상승; 이후 고점 대비 급락 |
| 촉매·시간 | fleet·시장점유율·ancillary | 고성장·고마진이 실적으로 확인 |
| 사전 반증조건 | 모든 aircraft lease를 debt로 보고 mature route fare가 10% 낮아져도 ROIC가 자본비용을 넘는가? | 핵심 오류: 운용리스와 mature-route 경쟁을 정상화하지 않음 |

### 실제 전개와 투자 결론

저비용과 ancillary 모델은 2013~14 매우 강한 성장을 만들었다. 그러나 높은 reported ROIC는 aircraft lease를 자본화하면 high-teens로 낮아지고, 경쟁사가 basic economy 가격을 맞추자 비용격차가 수익격차로 그대로 남지 않았다. 진입·보유기간은 성공, 장기 품질 평가는 과도했다.

**종합판정: 매우 성공.** 핵심 오류·교훈: 운용리스와 mature-route 경쟁을 정상화하지 않음

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| CASM 격차 | JBLU -19%/LUV -8% | 유지 | 비용우위 유지 | 적중 |
| break-even fare | $58 | fare war 방어 | 초기 방어 | 적중 |
| ROIC | 40%+ | 높은 복리 | lease 조정 high-teens | 과장 |
| valuation | 7x ex-cash | rerating | 큰 상승 | 적중 |

재사용 질문: **모든 aircraft lease를 debt로 보고 mature route fare가 10% 낮아져도 ROIC가 자본비용을 넘는가?**

## 3. 2015-10-28 — 가격전쟁 과잉반응 롱

**추천 증권·방향:** 보통주 Long

### 원 투자논지

유가급락으로 legacy carrier가 운임을 내리자 주가가 고점에서 크게 빠진 상황에서, 구조적 저비용·성장·ROIC와 미국 ULCC 침투율 약 5% 대 유럽 20%를 샀다. 5.9x EV/EBIT, $35 부근 하방과 가격정상화 upside를 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 유가급락으로 legacy carrier가 운임을 내리자 주가가 고점에서 크게 빠진 상황에서, 구조적 저비용·성장·ROIC와 미국 ULCC 침투율 약 5% 대 유럽 20%를 샀다. 5.9x EV/EBIT, $35 부근 하방과 가격정상화 upside를 제시했다. | 낮은 비용과 시장성장은 남았지만 경쟁운임·capacity와 labor 비용이 margin을 눌렀고 5년 내 COVID가 항공수요를 붕괴시켰다. 싸 보인 peak-cycle EBIT는 하방이 아니었다. 장기 보유결과는 실패다. |
| 밸류에이션·청구권 | 5.9x EV/EBIT·약 $35 floor | 5년 보유경로에서 큰 손실·COVID 충격 |
| 촉매·시간 | 운임정상화·ULCC 침투 | COVID로 운항·수요 급감과 자금조달 필요 |
| 사전 반증조건 | EBIT가 50% 줄고 fleet lease는 그대로여도 $35가 liquidation floor인가? | 핵심 오류: 낮은 유가가 경쟁사 가격행동을 바꾸는 2차효과 누락 |

### 실제 전개와 투자 결론

낮은 비용과 시장성장은 남았지만 경쟁운임·capacity와 labor 비용이 margin을 눌렀고 5년 내 COVID가 항공수요를 붕괴시켰다. 싸 보인 peak-cycle EBIT는 하방이 아니었다. 장기 보유결과는 실패다.

**종합판정: 실패.** 핵심 오류·교훈: 낮은 유가가 경쟁사 가격행동을 바꾸는 2차효과 누락

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| EV/EBIT | 5.9x | 저평가 | peak 이익 기준 | 오류 |
| 미국 ULCC | ~5% | 유럽 20%로 확대 | 성장 | 부분 |
| 하방 | ~$35 | floor | 하회 | 실패 |
| 5년결과 | 상승 | 정상화 | COVID 손실 | 실패 |

재사용 질문: **EBIT가 50% 줄고 fleet lease는 그대로여도 $35가 liquidation floor인가?**

## 4. 2017-05-09 — 유가상승 수혜형 ULCC 롱

**추천 증권·방향:** 보통주 Long

### 원 투자논지

420편/일·61개 목적지, 11.5% margin과 약 $65 ex-fuel segment cost를 가진 Spirit은 ancillary가 그중 대부분을 충당해 base-fare break-even이 약 $11이라고 봤다. 유가가 오르면 legacy의 높은 비용 때문에 운임격차가 다시 넓어지고 fleet 성장이 이익을 키워 $55.50 진입가를 정당화한다고 주장했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 420편/일·61개 목적지, 11.5% margin과 약 $65 ex-fuel segment cost를 가진 Spirit은 ancillary가 그중 대부분을 충당해 base-fare break-even이 약 $11이라고 봤다. 유가가 오르면 legacy의 높은 비용 때문에 운임격차가 다시 넓어지고 fleet 성장이 이익을 키워 $55.50 진입가를 정당화한다고 주장했다. | 유가만으로 industry pricing이 회복되지 않았고 pilot 계약·운항차질·capacity 경쟁이 비용우위를 상쇄했다. 주가는 크게 하락했고 2020에는 COVID를 맞았다. 방향·촉매·하방 모두 실패했다. |
| 밸류에이션·청구권 | 11.5% margin·낮은 break-even fare | 진입 $55.50에서 장기 대폭 하락 |
| 촉매·시간 | 유가상승·fare spread·fleet 성장 | 운항차질·노무비·가격경쟁으로 margin 악화 |
| 사전 반증조건 | 유가가 오르면서 동시에 pilot cost와 신규 capacity가 늘면 fare spread가 실제 확대되는가? | 핵심 오류: 단일 원가변수로 경쟁사의 가격·capacity 행동을 설명 |

### 실제 전개와 투자 결론

유가만으로 industry pricing이 회복되지 않았고 pilot 계약·운항차질·capacity 경쟁이 비용우위를 상쇄했다. 주가는 크게 하락했고 2020에는 COVID를 맞았다. 방향·촉매·하방 모두 실패했다.

**종합판정: 치명적 실패.** 핵심 오류·교훈: 단일 원가변수로 경쟁사의 가격·capacity 행동을 설명

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $55.50 | 상승 | 대폭 하락 | 실패 |
| margin | 11.5% | 확대 | 축소 | 실패 |
| segment cost | ~$65 ex-fuel | 우위 | 우위는 유지 | 부분 |
| 유가촉매 | 상승 | fare spread 확대 | 불충분 | 실패 |

재사용 질문: **유가가 오르면서 동시에 pilot cost와 신규 capacity가 늘면 fare spread가 실제 확대되는가?**

## 5. 2018-04-17 — fleet 성장·earnings double 롱

**추천 증권·방향:** 보통주 Long

### 원 투자논지

14% ASM CAGR과 mature economics를 근거로 operating income/ASM 1.5센트, 2022 EPS $8~9를 기대했다. pilot 계약은 임금 43% 인상에도 work-rule 개선으로 상쇄되고 ancillary per passenger가 $55로 올라가며 Frontier 결합도 선택지라고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 14% ASM CAGR과 mature economics를 근거로 operating income/ASM 1.5센트, 2022 EPS $8~9를 기대했다. pilot 계약은 임금 43% 인상에도 work-rule 개선으로 상쇄되고 ancillary per passenger가 $55로 올라가며 Frontier 결합도 선택지라고 봤다. | 용량은 늘었지만 단위수익과 비용이 기대만큼 따라오지 않았고 COVID 뒤 부채와 고정비가 커졌다. 2022년에는 Frontier 거래가 발표됐으나 독립 EPS $8~9 복리는 실현되지 않았다. 원 SQL short flag와 달리 본문은 명백한 Long이다. |
| 밸류에이션·청구권 | 2022 EPS $8~9·14% ASM CAGR | 1~5년 경로에서 목표 EPS·기업가치 미달 |
| 촉매·시간 | ancillary·pilot productivity·Frontier | COVID로 계획된 fleet 성장과 독립 earnings 경로 붕괴 |
| 사전 반증조건 | RASM이 10% 낮고 pilot cost가 전액 반영돼도 1.5센트/ASM이 가능한가? | 핵심 오류: capacity 성장과 per-ASM 이익을 동시에 고정 |

### 실제 전개와 투자 결론

용량은 늘었지만 단위수익과 비용이 기대만큼 따라오지 않았고 COVID 뒤 부채와 고정비가 커졌다. 2022년에는 Frontier 거래가 발표됐으나 독립 EPS $8~9 복리는 실현되지 않았다. 원 SQL short flag와 달리 본문은 명백한 Long이다.

**종합판정: 실패.** 핵심 오류·교훈: capacity 성장과 per-ASM 이익을 동시에 고정

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| ASM | 연 14% | 성장 | 성장 후 충격 | 부분 |
| OI/ASM | 1.5¢ | 유지 | 미달 | 실패 |
| 2022 EPS | $8~9 | 두 배 | 미실현 | 실패 |
| ancillary | $55 | 상승 | 상승 | 적중 |

재사용 질문: **RASM이 10% 낮고 pilot cost가 전액 반영돼도 1.5센트/ASM이 가능한가?**

## 6. 2020-06-18 — 항공기 담보채권 롱

**추천 증권·방향:** 2015/2017 EETC 채권 Long

### 원 투자논지

보통주가 아니라 2015·2017 EETC first lien을 $90 이하, second lien을 $80 이하에서 매수했다. 3~7년 된 A320/A321 담보와 약 70% 이하 LTV, first-lien waterfall을 분석해 파산을 피하거나 Chapter 11에서도 담보회수가 가능하고 first lien은 $85에서 $95로 정상화될 수 있다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 보통주가 아니라 2015·2017 EETC first lien을 $90 이하, second lien을 $80 이하에서 매수했다. 3~7년 된 A320/A321 담보와 약 70% 이하 LTV, first-lien waterfall을 분석해 파산을 피하거나 Chapter 11에서도 담보회수가 가능하고 first lien은 $85에서 $95로 정상화될 수 있다고 봤다. | 2024-01-31까지 Spirit은 Chapter 11을 신청하지 않았고 담보·coupon과 항공회복이 채권을 방어했다. 이후 사건을 평가기준에 소급하지 않는다. common의 취약성과 달리 특정 aircraft collateral·seniority를 산 아이디어는 성공했다. |
| 밸류에이션·청구권 | LTV 약 70% 이하·first $85→$95 | 2024-01-31까지 default 없이 coupon·가격회복 |
| 촉매·시간 | 운항회복·담보가치·유동성 | 여행회복과 liquidity로 단기 파산회피 확인 |
| 사전 반증조건 | 담보가 25% haircut되고 24개월 회수가 지연돼도 accrued interest 포함 IRR이 양수인가? | 핵심 오류: 항공기 처분비·lease rejection을 더 보수적으로 볼 여지 |

### 실제 전개와 투자 결론

2024-01-31까지 Spirit은 Chapter 11을 신청하지 않았고 담보·coupon과 항공회복이 채권을 방어했다. 이후 사건을 평가기준에 소급하지 않는다. common의 취약성과 달리 특정 aircraft collateral·seniority를 산 아이디어는 성공했다.

**종합판정: 성공.** 핵심 오류·교훈: 항공기 처분비·lease rejection을 더 보수적으로 볼 여지

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 담보 | A320/A321 3~7년 | 유동성 | 항공회복으로 방어 | 적중 |
| LTV | ~70% 이하 | 회수 | 충분 | 적중 |
| first price | $85→$95 | 정상화 | 회복 | 적중 |
| default | 회피 예상 | 없음 | 기준일까지 없음 | 적중 |

재사용 질문: **담보가 25% haircut되고 24개월 회수가 지연돼도 accrued interest 포함 IRR이 양수인가?**

## 7. 2022-05-05 — Frontier hedge·JetBlue optionality

**추천 증권·방향:** 합병차익 보통주 Long

### 원 투자논지

unaffected $21.78 아래에서 Frontier의 주식·현금 대가 implied 약 $25.83을 사고 Frontier 또는 JETS를 hedge했다. JetBlue의 $33 cash 제안이 upside option이며, slot·gate divestiture로 DOJ와 Northeast Alliance 우려를 해결할 수 있다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | unaffected $21.78 아래에서 Frontier의 주식·현금 대가 implied 약 $25.83을 사고 Frontier 또는 JETS를 hedge했다. JetBlue의 $33 cash 제안이 upside option이며, slot·gate divestiture로 DOJ와 Northeast Alliance 우려를 해결할 수 있다고 봤다. | Spirit은 Frontier를 버리고 최종 $33.50 이상 JetBlue 계약을 택했지만 DOJ가 제소했고 2024-01-16 법원이 거래를 차단했다. 선급금과 hedge가 손실을 줄였어도 deal-close라는 핵심 논지는 평가기준 전에 실패했다. |
| 밸류에이션·청구권 | Frontier ~$25.83/JBLU $33+ | 2024-01-16 법원 차단; merger spread 손실 |
| 촉매·시간 | 경쟁입찰·주주승인·규제승인 | 연방법원이 JetBlue 인수를 차단 |
| 사전 반증조건 | DOJ 시장정의를 그대로 적용해 deal이 깨질 때 prepayment 차감 standalone value는? | 핵심 오류: ULCC 소멸의 소비자피해를 divestiture로 해결 가능하다고 과신 |

### 실제 전개와 투자 결론

Spirit은 Frontier를 버리고 최종 $33.50 이상 JetBlue 계약을 택했지만 DOJ가 제소했고 2024-01-16 법원이 거래를 차단했다. 선급금과 hedge가 손실을 줄였어도 deal-close라는 핵심 논지는 평가기준 전에 실패했다.

**종합판정: 실패.** 핵심 오류·교훈: ULCC 소멸의 소비자피해를 divestiture로 해결 가능하다고 과신

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| unaffected | $21.78 | 하방 | standalone 악화 | 실패 |
| Frontier implied | ~$25.83 | 회수 | 계약 종료 | 실패 |
| JetBlue | $33~33.50+ | 현금회수 | 법원 차단 | 실패 |
| hedge/prepay | 손실완충 | IRR 방어 | 일부 완충 | 부분 |

재사용 질문: **DOJ 시장정의를 그대로 적용해 deal이 깨질 때 prepayment 차감 standalone value는?**

## 2024-01-31 기준 기업 결론

Spirit은 2022년 Frontier 계약을 버리고 JetBlue의 주당 $33.50 이상 현금제안을 택했지만 DOJ가 제소했고 2024년 1월 16일 법원이 $3.8bn 거래를 차단했다. 2024-01-31 기준 merger thesis는 깨졌고 standalone 회사는 Pratt engine grounding·비용·부채 압박을 안게 됐다.

## 주요 근거

- [Spirit 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1498710/000149871016000205/save-20151231x10k.htm) — ULCC economics·fleet·경쟁위험.
- [Spirit 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1498710/000149871022000088/save-20211231.htm) — COVID 뒤 재무와 Frontier merger.
- [JetBlue offer terms](https://www.sec.gov/Archives/edgar/data/1498710/000119312522204192/d368049dex992.htm) — $33.50~$34.15 cash와 prepayment/ticking fee.
- [Court blocks JetBlue acquisition of Spirit](https://www.justice.gov/archives/opa/pr/justice-department-statements-district-court-decision-block-jetblues-acquisition-spirit) — 법원이 $3.8bn 인수를 차단.

---

# General Motors (GM) — 기업과 비즈니스

GM은 Chevrolet·GMC·Cadillac·Buick 차량을 설계·제조·판매하고 GM Financial로 딜러·소비자 금융을 제공한다. 북미 pickup·large SUV가 높은 가격·mix·margin과 대부분의 현금을 만들고, 승용차·중국 JV·남미·EV·Cruise가 cycle과 투자부담을 더한다. 자동차 제조의 경제성은 SAAR, 점유율, incentive-adjusted price, mix, 공장가동률, warranty·recall, UAW labor와 원재료에 좌우된다. GM Financial은 판매를 지지하지만 credit loss·used-car residual·조달리스크를 추가한다. 2009년 파산은 구 GM 보통주를 소멸시키고 부채·노무·retiree liability를 재편한 ‘New GM’을 만들었으므로 전후 주식은 다른 증권이다. 낮은 P/E는 peak truck profit, pension·warranty·cycle capex·EV 전환비용을 정상화해야 의미가 있다. Cruise·EV 같은 option은 분리실현 가능성과 계속 필요한 투자금을 함께 빼야 한다.

## 돈을 버는 구조

- 북미 truck/SUV price·mix가 제조이익의 핵심
- 높은 고정비 때문에 SAAR·utilization 변화가 이익을 증폭
- GM Financial은 판매·이익과 credit/funding 위험을 함께 추가
- 구 GM 옵션 short와 New GM common/warrant는 별도 증권

## 아이디어 전체 판정

| 게시일 | 실제 방향 | 추천 증권 | 투자논지 | 결과 | 판정 |
|---|---|---|---|---|---|
| 2009-04-27 | Short | 구 GM 2011 $2.50 call 매도 | 구주 소멸 옵션매도 | 수취 premium $0.55 보존; 구주 call 무가치 | 매우 성공 |
| 2011-02-17 | Long | New GM 보통주 | 파산후 저평가 롱 | 1년 -25.13%, 3년 -0.56%, 5년 -15.56% | 실패 |
| 2012-01-06 | Long | New GM 보통주 | NOL·cash stub 롱 | 1년 +29.84%, 3년 +55.60%, 5년 +83.76% | 매우 성공 |
| 2013-02-25 | Long | New GM 보통주 | Treasury exit·truck cycle 롱 | 1년 +34.56%, 3년 +18.63%, 5년 +82.45% | 성공·목표 미달 |
| 2013-03-20 | Long | Series B warrant | 장기 워런트 레버리지 롱 | 만기 내재가치 대략 $20.7, 약 +72% 추정 | 성공 |
| 2017-11-19 | Long | New GM 보통주 | core+Cruise SOTP 롱 | 1년 -17.36%, 3년 +5.46%, 5년 -1.60% | 실패 |
| 2018-05-19 | Long | New GM 보통주 | truck profit pool 롱 | 1년 +1.01%, 2년 -29.21%, 3년 +59.48% | 성공·경로위험 |

## 1. 2009-04-27 — 구주 소멸 옵션매도

**추천 증권·방향:** 구 GM 2011 $2.50 call 매도 Short

### 원 투자논지

구 GM의 debt exchange나 법원 구조조정에서 보통주 몫은 0~$0.25에 가깝다고 보고, 주가급락 뒤에도 남은 변동성 프리미엄을 이용해 2011년 $2.50 call을 $0.55에 매도했다. 무차입 equity short가 아니라 strike 위 회수가능성에 베팅한 증권선택이었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 구 GM의 debt exchange나 법원 구조조정에서 보통주 몫은 0~$0.25에 가깝다고 보고, 주가급락 뒤에도 남은 변동성 프리미엄을 이용해 2011년 $2.50 call을 $0.55에 매도했다. 무차입 equity short가 아니라 strike 위 회수가능성에 베팅한 증권선택이었다. | GM은 2009-06-01 Chapter 11을 신청했고 구 보통주는 취소됐다. New GM IPO와 이후 티커 GM은 다른 증권이므로 구주 콜은 무가치해졌다. 방향·청구권·촉매가 모두 맞았다. |
| 밸류에이션·청구권 | 구주 equity $0~0.25·strike $2.50 | 수취 premium $0.55 보존; 구주 call 무가치 |
| 촉매·시간 | debt exchange/Chapter 11 | Chapter 11과 구주 청구권 소멸 |
| 사전 반증조건 | 정부가 구주주에게 예외적 recovery를 주고 주가가 strike를 넘을 최대손실은? | 핵심 오류: 무제한 call매도 squeeze 위험은 있었으나 구조조정 기한 명확 |

### 실제 전개와 투자 결론

GM은 2009-06-01 Chapter 11을 신청했고 구 보통주는 취소됐다. New GM IPO와 이후 티커 GM은 다른 증권이므로 구주 콜은 무가치해졌다. 방향·청구권·촉매가 모두 맞았다.

**종합판정: 매우 성공.** 핵심 오류·교훈: 무제한 call매도 squeeze 위험은 있었으나 구조조정 기한 명확

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| call | $2.50 strike | 무가치 | $0 | 적중 |
| premium | $0.55 | 전액수익 | 보존 | 성공 |
| 구주가치 | $0~0.25 | 소멸 | 취소 | 적중 |
| 촉매 | 구조조정 | 근시일 | 2009-06-01 | 적중 |

재사용 질문: **정부가 구주주에게 예외적 recovery를 주고 주가가 strike를 넘을 최대손실은?**

## 2. 2011-02-17 — 파산후 저평가 롱

**추천 증권·방향:** New GM 보통주 Long

### 원 투자논지

구조조정으로 legacy debt·labor 부담을 낮춘 New GM을 $36.50에서 2012 EBIT 4.5x, EBITDA 2.7x, earnings 5.9x로 샀다. 미국 SAAR 회복, BRIC 성장, product quality와 break-even 개선이 normalized multiple을 만들 것으로 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 구조조정으로 legacy debt·labor 부담을 낮춘 New GM을 $36.50에서 2012 EBIT 4.5x, EBITDA 2.7x, earnings 5.9x로 샀다. 미국 SAAR 회복, BRIC 성장, product quality와 break-even 개선이 normalized multiple을 만들 것으로 봤다. | 제조·판매는 회복했지만 유럽손실·연금·cycle·정부 overhang과 낮은 quality multiple이 지속됐다. 주가는 1년 -25.13%, 3년 -0.56%, 5년 -15.56%였다. 싼 숫자가 catalyst 없는 가치함정이 됐다. |
| 밸류에이션·청구권 | 4.5x EBIT·2.7x EBITDA·5.9x EPS | 1년 -25.13%, 3년 -0.56%, 5년 -15.56% |
| 촉매·시간 | SAAR·BRIC·정부지분 매각 | 1년 -25.13%로 rerating 실패 |
| 사전 반증조건 | SAAR이 회복해도 유럽·연금·incentive를 정상화한 FCF yield가 충분한가? | 핵심 오류: 파산비용 절감을 곧바로 높은 through-cycle ROIC로 해석 |

### 실제 전개와 투자 결론

제조·판매는 회복했지만 유럽손실·연금·cycle·정부 overhang과 낮은 quality multiple이 지속됐다. 주가는 1년 -25.13%, 3년 -0.56%, 5년 -15.56%였다. 싼 숫자가 catalyst 없는 가치함정이 됐다.

**종합판정: 실패.** 핵심 오류·교훈: 파산비용 절감을 곧바로 높은 through-cycle ROIC로 해석

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $36.50 | rerating | 5년 하회 | 실패 |
| 2012 EBIT | 4.5x | 정상화 | multiple 유지 | 실패 |
| SAAR | 회복 | volume leverage | 회복 | 적중 |
| 5년수익 | 상승 | 복리 | -15.56% | 실패 |

재사용 질문: **SAAR이 회복해도 유럽·연금·incentive를 정상화한 FCF yield가 충분한가?**

## 3. 2012-01-06 — NOL·cash stub 롱

**추천 증권·방향:** New GM 보통주 Long

### 원 투자논지

$22 중 주당 약 $6 NOL과 $1 excess cash를 빼면 자동차 stub가 $15, 2013 EPS $4.70의 약 3x라고 봤다. 미국 회복·유럽 구조조정·정부지분 매각으로 두 배가 가능하고 downside는 25%라고 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $22 중 주당 약 $6 NOL과 $1 excess cash를 빼면 자동차 stub가 $15, 2013 EPS $4.70의 약 3x라고 봤다. 미국 회복·유럽 구조조정·정부지분 매각으로 두 배가 가능하고 downside는 25%라고 제시했다. | SAAR 회복과 정부 exit가 현실화됐고 주가는 1년 +29.84%, 3년 +55.60%, 5년 +83.76%였다. 낮은 진입가격이 유럽·cycle 오차를 흡수했다. NOL 전액가치는 할인해야 하지만 결과는 강한 성공이다. |
| 밸류에이션·청구권 | stub 약 3x 2013 EPS·두 배 | 1년 +29.84%, 3년 +55.60%, 5년 +83.76% |
| 촉매·시간 | SAAR·유럽·Treasury exit | 미 재무부가 GM 지분을 완전매각 |
| 사전 반증조건 | NOL을 50% 할인하고 유럽손실 3년을 넣어도 stub multiple이 싼가? | 핵심 오류: NOL과 excess cash의 실현시기·의무 차감이 단순화 |

### 실제 전개와 투자 결론

SAAR 회복과 정부 exit가 현실화됐고 주가는 1년 +29.84%, 3년 +55.60%, 5년 +83.76%였다. 낮은 진입가격이 유럽·cycle 오차를 흡수했다. NOL 전액가치는 할인해야 하지만 결과는 강한 성공이다.

**종합판정: 매우 성공.** 핵심 오류·교훈: NOL과 excess cash의 실현시기·의무 차감이 단순화

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $22 | 두 배 | $40대 접근 | 성공 |
| stub | $15 | ~3x EPS | rerating | 적중 |
| Treasury | overhang | exit | 2013 완전매각 | 적중 |
| 5년수익 | 상승 | 복리 | +83.76% | 성공 |

재사용 질문: **NOL을 50% 할인하고 유럽손실 3년을 넣어도 stub multiple이 싼가?**

## 4. 2013-02-25 — Treasury exit·truck cycle 롱

**추천 증권·방향:** New GM 보통주 Long

### 원 투자논지

$26.71에서 2~3년 +160%/-27%를 제시했다. 약 $5bn의 cash tax·pension benefit, Treasury exit와 S&P 편입, pickup 교체주기, GM Financial 확대가 earnings·multiple을 동시에 올린다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $26.71에서 2~3년 +160%/-27%를 제시했다. 약 $5bn의 cash tax·pension benefit, Treasury exit와 S&P 편입, pickup 교체주기, GM Financial 확대가 earnings·multiple을 동시에 올린다고 봤다. | 정부는 2013년 지분을 모두 팔았고 미국 truck·SAAR 회복과 금융확대가 이익을 도왔다. 주가는 1년 +34.56%, 3년 +18.63%, 5년 +82.45%로 상승했지만 +160%에는 못 미쳤다. 성공이되 upside magnitude는 과장됐다. |
| 밸류에이션·청구권 | 2~3년 +160%/-27% | 1년 +34.56%, 3년 +18.63%, 5년 +82.45% |
| 촉매·시간 | $5bn benefit·Treasury·S&P·truck | Treasury exit로 핵심 수급촉매 현실화 |
| 사전 반증조건 | exit multiple이 그대로여도 truck FCF와 현금혜택만으로 기대 IRR이 충분한가? | 핵심 오류: multiple·earnings·현금효과를 모두 더해 목표 중복 |

### 실제 전개와 투자 결론

정부는 2013년 지분을 모두 팔았고 미국 truck·SAAR 회복과 금융확대가 이익을 도왔다. 주가는 1년 +34.56%, 3년 +18.63%, 5년 +82.45%로 상승했지만 +160%에는 못 미쳤다. 성공이되 upside magnitude는 과장됐다.

**종합판정: 성공·목표 미달.** 핵심 오류·교훈: multiple·earnings·현금효과를 모두 더해 목표 중복

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $26.71 | +160% | 5년 +82.45% | 목표미달 |
| Treasury | 매각 | 완전 exit | 2013 완료 | 적중 |
| 현금혜택 | ~$5bn | 주주가치 | 부분 실현 | 부분 |
| 3년수익 | 상승 | 큰 rerating | +18.63% | 미달 |

재사용 질문: **exit multiple이 그대로여도 truck FCF와 현금혜택만으로 기대 IRR이 충분한가?**

## 5. 2013-03-20 — 장기 워런트 레버리지 롱

**추천 증권·방향:** Series B warrant Long

### 원 투자논지

2019-07-10 만기 Series B warrant를 $12.03에 사고 strike $18.33을 더한 break-even GM $30.36에 베팅했다. GM $41이면 warrant 약 +90% 대 common +45%, GM $26이면 약 -40%로 장기 convexity를 샀다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 2019-07-10 만기 Series B warrant를 $12.03에 사고 strike $18.33을 더한 break-even GM $30.36에 베팅했다. GM $41이면 warrant 약 +90% 대 common +45%, GM $26이면 약 -40%로 장기 convexity를 샀다. | 만기 무렵 GM common은 약 $39 부근이어서 내재가치는 약 $20.7, $12.03 대비 대략 +72%였다. 정확 종가·배당조정 검증에는 제한이 있으나 warrant는 성공했다. SQL common 수익률을 이 증권에 붙이면 안 된다. |
| 밸류에이션·청구권 | 가격 $12.03·strike $18.33·BE $30.36 | 만기 내재가치 대략 $20.7, 약 +72% 추정 |
| 촉매·시간 | 시간·SAAR·정부 exit | 만기시 common이 break-even을 상회 |
| 사전 반증조건 | GM이 $30 아래 머물러 time value가 0이 되어도 손실상한을 감내하는가? | 핵심 오류: 배당·strike 조정과 path/만기집중 위험 |

### 실제 전개와 투자 결론

만기 무렵 GM common은 약 $39 부근이어서 내재가치는 약 $20.7, $12.03 대비 대략 +72%였다. 정확 종가·배당조정 검증에는 제한이 있으나 warrant는 성공했다. SQL common 수익률을 이 증권에 붙이면 안 된다.

**종합판정: 성공.** 핵심 오류·교훈: 배당·strike 조정과 path/만기집중 위험

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| warrant 가격 | $12.03 | 상승 | ~$20.7 내재가치 | 성공 |
| strike | $18.33 | ITM | ITM | 적중 |
| break-even | $30.36 | common 상회 | ~$39 | 적중 |
| 수익 | GM $41시 +90% | 레버리지 | 대략 +72% | 부분 |

재사용 질문: **GM이 $30 아래 머물러 time value가 0이 되어도 손실상한을 감내하는가?**

## 6. 2017-11-19 — core+Cruise SOTP 롱

**추천 증권·방향:** New GM 보통주 Long

### 원 투자논지

24개월 $80 목표를 core 2019 EPS $7×10=$70과 Cruise·Maven 등 emerging tech $10으로 나눴다. SAAR rollover 우려가 과도하고 truck launch, buyback, Cruise monetization이 rerating을 만든다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 24개월 $80 목표를 core 2019 EPS $7×10=$70과 Cruise·Maven 등 emerging tech $10으로 나눴다. SAAR rollover 우려가 과도하고 truck launch, buyback, Cruise monetization이 rerating을 만든다고 봤다. | core truck earnings는 견조했지만 Cruise 가치가 현금화되지 않았고 autonomous 개발비·규제위험이 커졌다. 주가는 1년 -17.36%, 2년 -12.21%, 3년 +5.46%, 5년 -1.60%로 24개월 목표에 크게 실패했다. |
| 밸류에이션·청구권 | core $70+tech $10=$80 | 1년 -17.36%, 3년 +5.46%, 5년 -1.60% |
| 촉매·시간 | truck·buyback·Cruise | 2년 -12.21%로 목표기한 실패 |
| 사전 반증조건 | Cruise 가치를 0으로 두고 투자비를 비용처리해도 core만으로 충분한 upside인가? | 핵심 오류: 미실현 option에 양수가치를 더하면서 funding·확률을 차감하지 않음 |

### 실제 전개와 투자 결론

core truck earnings는 견조했지만 Cruise 가치가 현금화되지 않았고 autonomous 개발비·규제위험이 커졌다. 주가는 1년 -17.36%, 2년 -12.21%, 3년 +5.46%, 5년 -1.60%로 24개월 목표에 크게 실패했다.

**종합판정: 실패.** 핵심 오류·교훈: 미실현 option에 양수가치를 더하면서 funding·확률을 차감하지 않음

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 목표 | $80/24개월 | 상승 | 2년 -12.21% | 실패 |
| core EPS | $7×10 | ~$70 | multiple 미달 | 실패 |
| tech option | $10 | monetize | 현금소모·지연 | 실패 |
| 5년수익 | 상승 | 복리 | -1.60% | 실패 |

재사용 질문: **Cruise 가치를 0으로 두고 투자비를 비용처리해도 core만으로 충분한 upside인가?**

## 7. 2018-05-19 — truck profit pool 롱

**추천 증권·방향:** New GM 보통주 Long

### 원 투자논지

GM은 car가 아니라 pickup/SUV profit pool이라고 재정의했다. 2020 EPS $8.50+ 중 truck 기여 $5.40, 15% segment margin, chicken tax·brand loyalty·dealer network를 moat로 보고 EV/AV는 무료 option으로 뒀다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | GM은 car가 아니라 pickup/SUV profit pool이라고 재정의했다. 2020 EPS $8.50+ 중 truck 기여 $5.40, 15% segment margin, chicken tax·brand loyalty·dealer network를 moat로 보고 EV/AV는 무료 option으로 뒀다. | truck/SUV 수익력은 정확했고 3년 +59.48%로 회복했다. 그러나 2년 -29.21%의 COVID drawdown과 cycle·EV 투자경로가 컸다. 2020 EPS 목표는 충격으로 미달했으나 핵심 profit-pool 인과는 맞았다. |
| 밸류에이션·청구권 | 2020 EPS $8.50+·truck $5.40 | 1년 +1.01%, 2년 -29.21%, 3년 +59.48% |
| 촉매·시간 | 신형 truck·mix·buyback | COVID 공장중단·수요충격으로 2년 drawdown |
| 사전 반증조건 | SAAR 12m·공장중단 8주에도 liquidity와 truck franchise가 회복을 버티는가? | 핵심 오류: truck moat는 맞지만 cycle/공장가동 tail 미모델링 |

### 실제 전개와 투자 결론

truck/SUV 수익력은 정확했고 3년 +59.48%로 회복했다. 그러나 2년 -29.21%의 COVID drawdown과 cycle·EV 투자경로가 컸다. 2020 EPS 목표는 충격으로 미달했으나 핵심 profit-pool 인과는 맞았다.

**종합판정: 성공·경로위험.** 핵심 오류·교훈: truck moat는 맞지만 cycle/공장가동 tail 미모델링

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2020 EPS | $8.50+ | 성장 | COVID로 미달 | 실패 |
| truck EPS | $5.40 | 핵심 pool | 높은 수익 지속 | 적중 |
| 2년수익 | 상승 | rerating | -29.21% | 실패 |
| 3년수익 | 회복 | 장기 | +59.48% | 성공 |

재사용 질문: **SAAR 12m·공장중단 8주에도 liquidity와 truck franchise가 회복을 버티는가?**

## 2024-01-31 기준 기업 결론

2023년 GM은 높은 북미 truck 수익과 대규모 자사주를 유지했지만 UAW 파업, EV ramp 지연과 Cruise 운행중단·투자위험이 함께 나타났다. 2009년 구조조정은 생존을 만들었으나 New GM이 지속적으로 낮은 multiple을 받는 cycle·capital-intensity 문제까지 없애지는 못했다.

## 주요 근거

- [Auto Industry Program Overview](https://home.treasury.gov/data/troubled-assets-relief-program/automotive-programs/overview) — 2009 구조조정·2010 IPO·2013 정부지분 완전매각.
- [Treasury exits GM](https://home.treasury.gov/news/press-releases/jl2236) — 정부의 GM 보통주 최종 매각.
- [GM 2023 Annual Report](https://investor.gm.com/static-files/1fff6f59-551f-4fe0-bca9-74bfc9a56aeb) — segment·truck·GM Financial·Cruise·EV·UAW.
- [GM 2021 Annual Report](https://investor.gm.com/static-files/8f1001fb-1fba-4e71-bb42-4a48066820a0) — EV·Cruise 투자와 제조·금융 구조.

---

# 배치 공통 성공·실패 유형

| 유형 | 성공조건 | 실패조건 | 대표사례 |
|---|---|---|---|
| 담보·book value | stress haircut·회수기간 뒤에도 equity/채권 가치 유지 | 평시 appraisal·매각 premium을 하방으로 사용 | AER 2017 실패, SAVE EETC 성공 |
| cycle 정상화 | peak/trough와 고정비·부채를 함께 stress | peak residual·fare·truck margin을 정상값으로 사용 | HTZ 2022 실패, GM 2018 회복 |
| 자본구조 | security별 담보·만기·waterfall·손실상한 분리 | 기업 결과를 모든 청구권에 동일 적용 | GM call·warrant, HTZ debt/equity |
| 계약·규제 | signing·closing·break value·hedge 분리 | 계약 발표를 확정 현금으로 봄 | SAVE 2022 arb 실패 |
| ticker/entity | 법인·상장시장·증권식별자를 우선 확인 | ticker 문자열만으로 가격 결합 | Aimia/AerCap 오류 |

## 데이터 품질 메모

- AER 2011 가격성과는 entity mismatch로 무효 처리했다.
- 원 SQL 방향값과 본문 추론 방향을 분리했다.
- 워런트·옵션·EETC·merger arb에는 common 성과를 대입하지 않았다.
- 평가기준일 뒤 사건은 이 배치 판정에 사용하지 않았다.
