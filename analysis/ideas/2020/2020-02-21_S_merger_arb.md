# Sprint / T-Mobile — 2020-02-21 VIC Merger Arb

## 0. Snapshot
| 항목 | 내용 |
|---|---|
| Security | Long Sprint / Short TMUS |
| Thesis | T-Mobile merger 마지막 45~60일 spread Long |
| 실제 결과 | 거래는 작성자 예상 4월 6일보다 빠른 2020-04-01 종결. non-SoftBank Sprint 주주는 1주당 0.10256 TMUS를 받아 spread trade가 성공. |
| 판정 | **깔끔한 성공** |

# 1. 이건 Sprint 사업투자가 아니다

2020 아이디어는 Sprint standalone value를 사는 거래가 아니었다.

핵심 payoff는:

**받게 될 TMUS 주식가치  
- Sprint 매입가  
- hedge / borrow / financing cost  
= merger spread**

였다.

non-SoftBank Sprint 주주는 1주당 **0.10256 TMUS**를 받는 구조였다.

# 2. Arb에서 봐야 할 것

Merger arb는:
- 법원판결
- DOJ/FCC 조건
- Dish remedy
- exchange ratio
- closing date
- break risk
를 본다.

즉 operating KPI보다 **계약과 법률조건**이 더 중요하다.

# 3. 원문 논지
DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

핵심 insight: 무선통신에서는 spectrum의 장부·auction 가치보다 실제 network/customer economics와 strategic monetization 경로를 구분해야 한다.

# 4. Expected value framework

**Closing probability × deal consideration  
+ break probability × standalone Sprint value  
- hedge / carry cost**

로 계산해야 한다.

2020년 2월 시점에는 주요 법률 불확실성이 크게 줄어 있었고 남은 기간이 짧았다.

# 5. Claim-by-Claim
## C1. Regulatory completion
- 주장: 필수 규제승인은 사실상 끝났다.
- 근거: DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.
- 숨은 가정: FCC/DOJ/법원 이슈 재발 없음
- 반증조건: 새 injunction·regulatory reopening
- 실제: 거래는 정상 종결됐다.
- 판정: 적중
- 교훈: Regulatory completion 가설은 '새 injunction·regulatory reopening'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

## C2. Amended terms
- 주장: SoftBank 재협상 후 일반 Sprint 주주는 0.10256을 유지한다.
- 근거: DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.
- 숨은 가정: amendment가 변경되지 않음
- 반증조건: 일반주주 exchange ratio 재하향
- 실제: 그 비율 그대로 적용됐다.
- 판정: 적중
- 교훈: Amended terms 가설은 '일반주주 exchange ratio 재하향'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

## C3. Financing
- 주장: financing이 더 이상 closing condition이 아니다.
- 근거: DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.
- 숨은 가정: commitment와 closing mechanics 안정
- 반증조건: financing failure
- 실제: 종결에 문제 없었다.
- 판정: 적중
- 교훈: Financing 가설은 'financing failure'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

## C4. Closing timing
- 주장: 45~60일 내, 4월 6일 정도 종결한다.
- 근거: DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.
- 숨은 가정: administrative steps만 남음
- 반증조건: 장기 지연
- 실제: 4월 1일 조기 종결.
- 판정: 강한 적중
- 교훈: Closing timing 가설은 '장기 지연'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

## C5. Hedge
- 주장: TMUS short로 시장·acquirer beta를 제거한다.
- 근거: DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.
- 숨은 가정: hedge ratio 정확
- 반증조건: borrow/ratio mismatch
- 실제: 계약비율 기반 spread가 수렴했다.
- 판정: 적중
- 교훈: Hedge 가설은 'borrow/ratio mismatch'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

## C6. 7.5% spread
- 주장: 잔여 deal-break risk 대비 gross spread가 매력적이다.
- 근거: DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.
- 숨은 가정: break probability 매우 낮음
- 반증조건: 거래 무산
- 실제: 거래 성공으로 spread 수익 실현.
- 판정: 성공
- 교훈: 7.5% spread 가설은 '거래 무산'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

# 6. 숫자 검증
| 지표 | 당시/기대 | 실제 | 의미 |
|---|---|---|---|
| Gross spread | 약 7.5% / 45~60일 수익 | 2020-04-01 종결 | 당시 약 7.5%에서 45~60일 수익를 기대했다. 실제는 2020-04-01 종결로 확인되어 적중로 판정했다. |
| 교환비율 | 0.10256 TMUS/S / 일반 S 주주 유지 | 0.10256 적용 | 당시 0.10256 TMUS/S에서 일반 S 주주 유지를 기대했다. 실제는 0.10256 적용로 확인되어 적중로 판정했다. |
| 예상 종결 | 2020-04-06 / 약 45일 | 2020-04-01 | 당시 2020-04-06에서 약 45일를 기대했다. 실제는 2020-04-01로 확인되어 조기 적중로 판정했다. |
| 방향 | SQL Short / Long S / Short TMUS | spread trade | 당시 SQL Short에서 Long S / Short TMUS를 기대했다. 실제는 spread trade로 확인되어 메타데이터 교정로 판정했다. |


# 7. Chronology
| 날짜 | 사건 | 의미 |
|---|---|---|
| 2020-02-21 | VIC 아이디어 게시 | T-Mobile merger 마지막 45~60일 spread Long |
| 2020-04-01 | 최초 핵심 검증·반증 신호 | T-Mobile/Sprint merger가 공식 종결되고 교환비율 0.10256이 적용되어 thesis가 완전히 실현됐다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |


# 8. 실제 성과

T-Mobile과 Sprint는 2020년 4월 1일 합병을 완료했다. non-SoftBank Sprint 주주는 Sprint 1주당 0.10256 T-Mobile 주식을 받았다. 작성자가 가정한 4월 6일보다 빨리 종결되어 duration도 더 짧았다.

거래는 예상 4월 6일보다 빠른 **2020-04-01** 종결. spread trade는 성공했다.

# 9. 왜 이전 Sprint 아이디어보다 분석이 깔끔했나

2008/2014 Long은:
- spectrum value
- turnaround
- buyer probability
- FCF
를 동시에 맞혀야 했다.

2020 arb는:
- 계약조건
- 승인상태
- exchange ratio
- closing timing
으로 변수가 크게 줄었다.

즉 **같은 회사라도 payoff가 명확한 security를 선택하자 분석오차가 줄었다.**

# 10. 최초 반증조건

- court/DOJ/FCC remedy 변경
- financing/closing condition 훼손
- exchange ratio 변경
- outside date 지연
- hedge basis 급변

중 하나가 발생하면 재평가했어야 한다.

# 11. 재사용 규칙

1. Merger arb는 standalone business thesis와 분리한다.
2. Spread는 확정수익이 아니라 확률가중 payoff다.
3. Break value를 항상 넣는다.
4. Exchange-ratio deal은 상대주가 hedge를 명확히 한다.
5. 예상 종결일이 늦어지면 annualized IRR을 다시 계산한다.
6. 같은 issuer라도 common long/short와 arb를 한 성과로 섞지 않는다.

# 12. Sources
1. Value Investors Club — VIC S 2020-02-21 원문 (2020-02-21) — https://www.valueinvestorsclub.com/idea/SPRINT_CORP/9908147447
2. SEC — Sprint 2006 Form 10-K (2007-02-28) — https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm
3. SEC — Sprint Nextel 2007 Form 10-K (2008-02-29) — https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm
4. Sprint/SEC — Sprint FY2008 Results (2009-02-19) — https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm
5. SEC — Sprint 2010 Form 10-K (2011-02-24) — https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm
6. SEC — Sprint 2014 Form 10-K (2015-05-26) — https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm
7. Sprint — Sprint FY2015 Results (2016-05-03) — https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm
8. Sprint/SoftBank — Sprint FY2016 Results (2017-05-03) — https://group.softbank/en/news/press/20170503
9. Sprint — Sprint FY2017 Results (2018-05-02) — https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm
10. T-Mobile — T-Mobile and Sprint amend merger terms (2020-02-20) — https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement
11. T-Mobile — T-Mobile completes merger with Sprint (2020-04-01) — https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company
12. Macrotrends/market history — Sprint historical price context (2020-04-01)
