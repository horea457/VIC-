# Nexstar Media Group (NXST) — 기업과 비즈니스

Nexstar는 미국 지역 TV station을 소유·운영하고 local news와 network programming을 배포한다. 전통적 돈벌이는 지역·전국 광고였지만 2000년대 중반 이후 retransmission consent가 독립적인 수익원으로 커졌다. station이 cable/satellite/vMVPD에 자신의 broadcast signal을 제공하는 대가를 받고, 동시에 ABC/CBS/NBC/Fox 등 network에는 affiliation/programming fee를 지급한다. 따라서 gross distribution revenue와 net distribution contribution을 구분해야 한다.

Nexstar의 장기적 차별점은 단순 station ownership보다 **자본배분 playbook**이었다. 작은 station group을 인수해 corporate overhead를 흡수하고 retrans bargaining scale을 키우고, 규제상 필요한 station은 높은 가격에 divest한 뒤 debt를 줄였다. Media General과 Tribune은 이 playbook의 대형 버전이었다. M&A runway가 줄자 buyback이 다음 주당가치 성장 엔진으로 이동했다.

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제 방향 | 핵심 논지 | 사후판정 |
|---|---|---|---|---|
| 2005-12-20 | Short | Long | retrans 정상화·deleveraging | 성공 |
| 2011-12-14 | Short | Long | 30%대 FCF yield + strategic alternatives | 강한 성공 |
| 2012-08-26 | Short | Long | Newport synergy·roll-up | 강한 성공 |
| 2016-01-29 | Short | Long MEG / Short 0.1249 NXST | spectrum CVR isolation | 성공·가치추정 과대 |
| 2017-08-12 | Short | Long | Media General 후 retrans/FCF | 강한 성공 |
| 2018-04-23 | Short | Long | 규제·정치광고·capital return | 강한 성공·촉매경로 변형 |
| 2020-03-12 | Short | Long | COVID panic 3.5x levered FCF | 매우 강한 성공 |
| 2021-09-20 | Short | Long | M&A 후 buyback compounding | 강한 성공 |

---
<!-- idea:7b8c3ad5-3249-4756-901a-9d267e0a8a4b -->
## 1. 2005-12-20 — retrans 분쟁 정상화·deleveraging에 건 초기 Long
### 1. 결론부터

**종합판정: 성공.** 핵심은 'TV 광고 성장'이 아니라 배급권의 경제적 가치가 케이블 사업자와의 협상에서 현금으로 전환되는지였다. 이 가정은 맞았다. 다만 7x대 leverage의 equity convexity를 과소평가하면 같은 사업 개선도 주주수익으로 이어지기 전 liquidity risk가 커진다.

### 2. 원 투자논지

2005년의 부진을 구조적 붕괴로 보지 않고 retransmission consent 분쟁의 일시적 매출 공백, 2004 정치·올림픽의 어려운 비교, 높은 레버리지 때문에 눌린 주가로 해석했다. 2006년 retrans 계약 정상화와 광고 비교기저 개선, 자산매각·부채감축을 촉매로 봤다.

원문 SQL에는 `is_short=true`가 저장돼 있지만 실제 증권 방향은 **Long**이다. 이 차이는 raw 데이터 자체를 수정하지 않고 research layer의 `research_direction_ko`와 `security_instrument_ko`에 명시했다.

### 3. 사업과 돈의 흐름

Nexstar의 경제성은 local/national advertising, election-cycle political advertising, retransmission/distribution, digital에서 발생한다. station 운영은 fixed-cost 비중이 높아 추가 매출의 incremental margin이 높을 수 있지만, network affiliation fee와 debt service가 이를 흡수할 수 있다. 그래서 `gross retrans 성장 → EBITDA 성장`이라는 단순 연결보다 **net retrans contribution, leverage, cash interest, capex, share count**를 함께 봐야 한다.

### 4. 핵심 가정과 당시 관찰 가능 변수

당시 투자자가 확인할 수 있었던 것은 retrans 계약 갱신과 carriage dispute, station별/시장별 규모, 정치광고 cycle, 인수 multiple과 financing, covenant/leverage, network affiliation fee, station divestiture 필요성, 그리고 FCF 대비 market capitalization이었다. 이 아이디어의 핵심 가정은 다음과 같다.

1. contractual distribution economics가 advertising cycle보다 안정적일 것.
2. acquisition synergies가 headline multiple을 실제 cash yield로 낮출 것.
3. debt가 equity optionality를 파괴하기 전에 FCF로 빠르게 줄어들 것.
4. 정치광고를 정상화해도 valuation이 충분히 낮을 것.
5. 규제·ownership cap 때문에 생기는 divestiture가 deal economics를 훼손하지 않을 것.

### 5. 실제 전개

2006년 초 Nexstar는 약 150개 케이블 사업자, 약 400만 가입자를 포괄하는 다년 retrans 계약을 발표했고 회사는 약 $48m의 retrans revenue 기여를 기대했다. 반면 2005년 총부채는 약 $646.5m로 높아 원문이 지적한 balance-sheet risk도 실제였다. 이후 Nexstar가 retrans를 핵심 수익원으로 키운 점은 사업 방향을 확인해준다.

### 6. 주장별 검증

- **방향:** 원문 기준 Long; raw SQL Short flag는 오류 또는 security-level 분류 미흡이다.
- **사업:** 2005년의 부진을 구조적 붕괴로 보지 않고 retransmission consent 분쟁의 일시적 매출 공백, 2004 정치·올림픽의 어려운 비교, 높은 레버리지 때문에 눌린 주가로 해석했다. 2006년 retrans 계약 정상화와 광고 비교기저 개선, 자산매각·부채감축을 촉매로 봤다.
- **촉매:** 2006년 초 Nexstar는 약 150개 케이블 사업자, 약 400만 가입자를 포괄하는 다년 retrans 계약을 발표했고 회사는 약 $48m의 retrans revenue 기여를 기대했다. 반면 2005년 총부채는 약 $646.5m로 높아 원문이 지적한 balance-sheet risk도 실제였다. 이후 Nexstar가 retrans를 핵심 수익원으로 키운 점은 사업 방향을 확인해준다.
- **밸류에이션/청구권:** 핵심은 'TV 광고 성장'이 아니라 배급권의 경제적 가치가 케이블 사업자와의 협상에서 현금으로 전환되는지였다. 이 가정은 맞았다. 다만 7x대 leverage의 equity convexity를 과소평가하면 같은 사업 개선도 주주수익으로 이어지기 전 liquidity risk가 커진다.
- **반증:** retrans 분쟁이 일시적이 아니라 구조적 carriage loss로 고착되거나, leverage covenant가 사업 정상화 이전에 equity를 강제희석시키면 thesis는 깨진다.
- **사후평가:** 성공

### 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| 2005 total debt | 646.5 | USD m | SEC 2005 10-K |
| 2006 retrans operators | 150 | operators | company/SEC |
| covered subscribers | 4.0 | m | company/SEC |
| expected retrans revenue | 48 | USD m | company/SEC |

### 8. 촉매와 타임라인

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2005-12-20 | VIC Long 게시 | retrans 분쟁과 레버리지로 눌린 방송주 |
| 2006-02-01 | 다년 retrans 계약 발표 | 약 150 operators/4m subscribers |
| 2006-03-01 | 2005 10-K | 총부채 약 $646.5m 확인 |
| 2012-07-19 | Newport 인수 발표 | M&A/scale 전략 확장 |
| 2017-01-17 | Media General 인수 종결 | 전국 2위 규모로 확대 |
| 2019-09-19 | Tribune 인수 종결 | 미국 최대 local broadcaster로 확대 |

### 9. 반증조건과 놓치기 쉬운 변수

**사전 반증조건:** retrans 분쟁이 일시적이 아니라 구조적 carriage loss로 고착되거나, leverage covenant가 사업 정상화 이전에 equity를 강제희석시키면 thesis는 깨진다.

또한 local TV는 구조적으로 cord-cutting, network fee inflation, audience fragmentation, political cycle, FCC ownership rules, refinancing cost에 노출된다. 과거의 높은 FCF yield가 terminal decline을 반영한 것인지, 아니면 계약수익과 자본배분으로 상쇄 가능한 할인인지 분리해야 한다.

### 10. 재사용 가능한 교훈

**고정비가 큰 지역방송은 광고매출보다 '순 retrans 수익/가입자'와 leverage headroom을 함께 봐야 한다.**

이 아이디어를 다른 기업에 재사용할 때는 단순히 `FCF yield가 높다`는 사실이 아니라, (a) FCF의 반복가능성, (b) debt와 maturity, (c) incremental acquisition/buyback return, (d) 규제 이벤트의 net cash proceeds, (e) 주당가치로 귀속되는 비율을 순서대로 검증해야 한다.

---
