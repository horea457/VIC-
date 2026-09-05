# Sinclair Broadcast Group (SBGI) — 기업과 비즈니스

Sinclair는 미국 지역방송 station group으로 local/national advertising, political advertising, retransmission/distribution, digital에서 수익을 얻는다. 2010년대 초에는 station consolidation과 retrans fee 상승으로 높은 FCF conversion을 보였고, 낮은 maintenance capex가 acquisition capacity를 만들었다. 그러나 Sinclair의 역사는 core station economics와 이후의 비핵심 자본배분을 분리해야 함을 보여준다.

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제 방향 | 핵심 논지 | 사후판정 |
|---|---|---|---|---|
| 2013-01-14 | Short | Long | 21% normalized FCF yield + retrans/M&A | 강한 성공 |
| 2015-08-16 | Short | Long | 16~18% FCF yield + $2bn spectrum option | 혼합: core 성공 / spectrum 실패 |

---
<!-- idea:2035e135-0601-4545-9f0c-0f1562365ac0 -->
## 9. 2013-01-14 — 21% normalized FCF yield와 retrans/M&A를 산 2013 Long
### 1. 결론부터

**종합판정: 강한 성공·장기 자본배분 주의.** 저성장 광고기업으로 보이던 broadcaster의 hidden growth가 retrans와 consolidation에서 나왔다는 통찰이 좋았다. 현금흐름 자산의 가치가 단순 revenue growth보다 capital allocation에 달려 있었다.

### 2. 원 투자논지

지역 TV의 약 70%가 local advertising으로 sticky하고, retransmission과 digital이 아직 저평가돼 있으며, maintenance capex가 낮아 BCF가 현금으로 잘 전환된다고 봤다. 당시 약 21% normalized FCF yield와 accretive acquisitions를 핵심으로 $23 안팎 목표를 제시했다.

원문 SQL에는 `is_short=true`가 저장돼 있지만 실제 증권 방향은 **Long**이다. 이 차이는 raw 데이터 자체를 수정하지 않고 research layer의 `research_direction_ko`와 `security_instrument_ko`에 명시했다.

### 3. 사업과 돈의 흐름

Sinclair의 경제성은 local/national advertising, election-cycle political advertising, retransmission/distribution, digital에서 발생한다. station 운영은 fixed-cost 비중이 높아 추가 매출의 incremental margin이 높을 수 있지만, network affiliation fee와 debt service가 이를 흡수할 수 있다. 그래서 `gross retrans 성장 → EBITDA 성장`이라는 단순 연결보다 **net retrans contribution, leverage, cash interest, capex, share count**를 함께 봐야 한다.

### 4. 핵심 가정과 당시 관찰 가능 변수

당시 투자자가 확인할 수 있었던 것은 retrans 계약 갱신과 carriage dispute, station별/시장별 규모, 정치광고 cycle, 인수 multiple과 financing, covenant/leverage, network affiliation fee, station divestiture 필요성, 그리고 FCF 대비 market capitalization이었다. 이 아이디어의 핵심 가정은 다음과 같다.

1. contractual distribution economics가 advertising cycle보다 안정적일 것.
2. acquisition synergies가 headline multiple을 실제 cash yield로 낮출 것.
3. debt가 equity optionality를 파괴하기 전에 FCF로 빠르게 줄어들 것.
4. 정치광고를 정상화해도 valuation이 충분히 낮을 것.
5. 규제·ownership cap 때문에 생기는 divestiture가 deal economics를 훼손하지 않을 것.

### 5. 실제 전개

Sinclair는 2013년 대규모 station acquisitions를 진행했고 이후 retrans 확대와 선거주기 수혜로 규모를 키웠다. 2015년 revenue는 $2.219bn, 2016년 $2.737bn으로 늘었고 2016 operating income은 $602.9m이었다. core 방송 consolidation/retrans thesis는 실제로 작동했다. 다만 훗날 sports/RSN 등 비핵심 capital allocation은 이 초기 core thesis와 분리해야 한다.

### 6. 주장별 검증

- **방향:** 원문 기준 Long; raw SQL Short flag는 오류 또는 security-level 분류 미흡이다.
- **사업:** 지역 TV의 약 70%가 local advertising으로 sticky하고, retransmission과 digital이 아직 저평가돼 있으며, maintenance capex가 낮아 BCF가 현금으로 잘 전환된다고 봤다. 당시 약 21% normalized FCF yield와 accretive acquisitions를 핵심으로 $23 안팎 목표를 제시했다.
- **촉매:** Sinclair는 2013년 대규모 station acquisitions를 진행했고 이후 retrans 확대와 선거주기 수혜로 규모를 키웠다. 2015년 revenue는 $2.219bn, 2016년 $2.737bn으로 늘었고 2016 operating income은 $602.9m이었다. core 방송 consolidation/retrans thesis는 실제로 작동했다. 다만 훗날 sports/RSN 등 비핵심 capital allocation은 이 초기 core thesis와 분리해야 한다.
- **밸류에이션/청구권:** 저성장 광고기업으로 보이던 broadcaster의 hidden growth가 retrans와 consolidation에서 나왔다는 통찰이 좋았다. 현금흐름 자산의 가치가 단순 revenue growth보다 capital allocation에 달려 있었다.
- **반증:** acquisition multiple이 retrans synergy를 앞서거나 reverse compensation/network fees가 retrans growth를 흡수하면 roll-up economics가 나빠진다.
- **사후평가:** 강한 성공·장기 자본배분 주의

### 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| normalized FCF yield | 21 | % | VIC |
| 2015 revenue | 2.219 | USD bn | Sinclair |
| 2016 revenue | 2.737 | USD bn | Sinclair |
| 2016 operating income | 602.9 | USD m | Sinclair |

### 8. 촉매와 타임라인

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2013-01-14 | VIC Long 게시 | retrans/M&A thesis |
| 2013-12-31 | station acquisition year | 대규모 portfolio 확장 |
| 2015-12-31 | FY15 revenue | $2.219bn |
| 2016-11-08 | US election cycle | political revenue peak |
| 2017-02-09 | spectrum auction result | $313m gross |
| 2017-12-31 | post-election results | core economics 지속 |

### 9. 반증조건과 놓치기 쉬운 변수

**사전 반증조건:** acquisition multiple이 retrans synergy를 앞서거나 reverse compensation/network fees가 retrans growth를 흡수하면 roll-up economics가 나빠진다.

또한 local TV는 구조적으로 cord-cutting, network fee inflation, audience fragmentation, political cycle, FCC ownership rules, refinancing cost에 노출된다. 과거의 높은 FCF yield가 terminal decline을 반영한 것인지, 아니면 계약수익과 자본배분으로 상쇄 가능한 할인인지 분리해야 한다.

### 10. 재사용 가능한 교훈

**방송 roll-up의 장점은 low maintenance capex지만, 그 현금이 어떤 다음 자산에 재투자되는지가 장기 quality를 결정한다.**

이 아이디어를 다른 기업에 재사용할 때는 단순히 `FCF yield가 높다`는 사실이 아니라, (a) FCF의 반복가능성, (b) debt와 maturity, (c) incremental acquisition/buyback return, (d) 규제 이벤트의 net cash proceeds, (e) 주당가치로 귀속되는 비율을 순서대로 검증해야 한다.

---
