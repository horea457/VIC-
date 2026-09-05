<!-- idea:f91c8f1f-4a84-4eab-ab51-03068d3b0b2b -->
## 7. 2020-03-12 — COVID panic에서 3.5x levered FCF를 산 2020 Long
### 1. 결론부터

**종합판정: 매우 강한 성공.** crisis long의 핵심은 '광고가 회복될 것'이 아니라 distribution revenue와 balance sheet가 일시적 ad shock을 버틸 수 있는지였다. Tribune integration으로 FCF base가 커진 직후 panic valuation이 발생해 convexity가 컸다.

### 2. 원 투자논지

주가 급락으로 약 3.5x levered FCF, 약 8.5x TEV/unlevered FCF까지 내려왔고, 3년간 주당 FCF 20% 안팎 성장 가능성을 net retrans와 capital deployment에서 찾았다. 2020 FCF가 시총의 31%, 2021 FCF가 추가 24%라는 매우 높은 cash yield를 강조했다.

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

COVID는 2Q core advertising을 강하게 때렸지만 회사는 흑자와 유동성을 유지했다. 2020 FCF before one-time transaction expenses는 약 $1.305bn, reported FCF는 약 $1.280bn이었다. 2020년 political ad revenue도 큰 폭으로 늘었고, 회사는 leverage reduction과 buyback을 병행했다. 2020년 9월에는 buyback capacity를 약 $384m으로 확대했다.

### 6. 주장별 검증

- **방향:** 원문 기준 Long; raw SQL Short flag는 오류 또는 security-level 분류 미흡이다.
- **사업:** 주가 급락으로 약 3.5x levered FCF, 약 8.5x TEV/unlevered FCF까지 내려왔고, 3년간 주당 FCF 20% 안팎 성장 가능성을 net retrans와 capital deployment에서 찾았다. 2020 FCF가 시총의 31%, 2021 FCF가 추가 24%라는 매우 높은 cash yield를 강조했다.
- **촉매:** COVID는 2Q core advertising을 강하게 때렸지만 회사는 흑자와 유동성을 유지했다. 2020 FCF before one-time transaction expenses는 약 $1.305bn, reported FCF는 약 $1.280bn이었다. 2020년 political ad revenue도 큰 폭으로 늘었고, 회사는 leverage reduction과 buyback을 병행했다. 2020년 9월에는 buyback capacity를 약 $384m으로 확대했다.
- **밸류에이션/청구권:** crisis long의 핵심은 '광고가 회복될 것'이 아니라 distribution revenue와 balance sheet가 일시적 ad shock을 버틸 수 있는지였다. Tribune integration으로 FCF base가 커진 직후 panic valuation이 발생해 convexity가 컸다.
- **반증:** distribution customers가 cord-cutting/contract dispute로 동시에 빠지고 advertising shock이 장기화돼 covenant headroom과 liquidity가 소진되면 low multiple은 trap이다.
- **사후평가:** 매우 강한 성공

### 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| 2020 FCF before one-time | 1304.6 | USD m | Nexstar |
| 2020 reported FCF | 1280.1 | USD m | Nexstar |
| 2Q20 FCF | 194.9 | USD m | Nexstar |
| Sep20 repurchase capacity | 384.2 | USD m | Nexstar |

### 8. 촉매와 타임라인

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2020-03-12 | VIC Long 게시 | COVID panic valuation |
| 2020-05-06 | 1Q20 results | FCF $423m |
| 2020-08-05 | 2Q20 results | FCF $194.9m despite ad shock |
| 2020-09-02 | buyback expansion | capacity ~$384.2m |
| 2020-11-05 | 3Q20 results | FCF $219m |
| 2021-02-23 | FY20 results | FCF before one-time $1.305bn |

### 9. 반증조건과 놓치기 쉬운 변수

**사전 반증조건:** distribution customers가 cord-cutting/contract dispute로 동시에 빠지고 advertising shock이 장기화돼 covenant headroom과 liquidity가 소진되면 low multiple은 trap이다.

또한 local TV는 구조적으로 cord-cutting, network fee inflation, audience fragmentation, political cycle, FCC ownership rules, refinancing cost에 노출된다. 과거의 높은 FCF yield가 terminal decline을 반영한 것인지, 아니면 계약수익과 자본배분으로 상쇄 가능한 할인인지 분리해야 한다.

### 10. 재사용 가능한 교훈

**panic valuation에서는 cyclic ad revenue와 contractual distribution revenue를 분리하고 debt maturity/liquidity를 먼저 스트레스테스트해야 한다.**

이 아이디어를 다른 기업에 재사용할 때는 단순히 `FCF yield가 높다`는 사실이 아니라, (a) FCF의 반복가능성, (b) debt와 maturity, (c) incremental acquisition/buyback return, (d) 규제 이벤트의 net cash proceeds, (e) 주당가치로 귀속되는 비율을 순서대로 검증해야 한다.

---
