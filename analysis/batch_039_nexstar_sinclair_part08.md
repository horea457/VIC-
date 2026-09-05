<!-- idea:585159f9-193f-40f6-aafa-3454b889e2fa -->
## 8. 2021-09-20 — M&A 종료 이후 buyback machine으로 본 2021 Long
### 1. 결론부터

**종합판정: 강한 성공.** M&A가 끝나면 성장률이 낮아지는 것이 아니라 높은 FCF yield가 share count 감소로 이전될 수 있다는 thesis였다. 주당가치 관점에서 매우 중요하다.

### 2. 원 투자논지

지난 10년간 station M&A와 deleveraging으로 earnings power가 30배 이상 커졌는데 valuation은 여전히 약 5x 수준이라는 논지였다. station M&A runway가 거의 끝나도 buyback, adjacent acquisitions, debt paydown으로 높은 earnings yield를 주당가치 성장에 전환할 수 있다고 봤다.

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

2021년 이사회는 $1.0bn repurchase authorization을 승인했고 상반기만 1.7m shares를 $258.8m에 매입했다. 2022년 7월에는 추가 $1.5bn authorization을 승인했다. 즉 'roll-up의 다음 단계가 buyback'이라는 핵심은 실제 자본배분으로 이어졌다. 다만 장기적으로 broadcast secular risk와 비방송 자산 배분의 질은 별도 평가가 필요하다.

### 6. 주장별 검증

- **방향:** 원문 기준 Long; raw SQL Short flag는 오류 또는 security-level 분류 미흡이다.
- **사업:** 지난 10년간 station M&A와 deleveraging으로 earnings power가 30배 이상 커졌는데 valuation은 여전히 약 5x 수준이라는 논지였다. station M&A runway가 거의 끝나도 buyback, adjacent acquisitions, debt paydown으로 높은 earnings yield를 주당가치 성장에 전환할 수 있다고 봤다.
- **촉매:** 2021년 이사회는 $1.0bn repurchase authorization을 승인했고 상반기만 1.7m shares를 $258.8m에 매입했다. 2022년 7월에는 추가 $1.5bn authorization을 승인했다. 즉 'roll-up의 다음 단계가 buyback'이라는 핵심은 실제 자본배분으로 이어졌다. 다만 장기적으로 broadcast secular risk와 비방송 자산 배분의 질은 별도 평가가 필요하다.
- **밸류에이션/청구권:** M&A가 끝나면 성장률이 낮아지는 것이 아니라 높은 FCF yield가 share count 감소로 이전될 수 있다는 thesis였다. 주당가치 관점에서 매우 중요하다.
- **반증:** FCF yield가 높은 이유가 terminal decline을 반영한 것이고 buyback이 declining intrinsic value보다 비싼 가격에 이뤄지면 EPS accretion은 가치창출이 아니다.
- **사후평가:** 강한 성공

### 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| Jan21 buyback auth | 1.0 | USD bn | Nexstar |
| H1 2021 repurchases | 258.8 | USD m | Nexstar |
| H1 shares repurchased | 1.7 | m shares | Nexstar |
| Jul22 new auth | 1.5 | USD bn | Nexstar |

### 8. 촉매와 타임라인

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2021-01-27 | $1bn buyback authorization | capital allocation shift |
| 2021-06-30 | H1 buyback progress | $258.8m/1.7m shares |
| 2021-09-20 | VIC Long 게시 | earnings yield/buyback thesis |
| 2022-07-28 | $1.5bn new authorization | buyback scale-up |
| 2022-09-30 | 2022 repurchases 확대 | cash return continued |
| 2025-12-31 | buyback capacity 잔존 | program persistence |

### 9. 반증조건과 놓치기 쉬운 변수

**사전 반증조건:** FCF yield가 높은 이유가 terminal decline을 반영한 것이고 buyback이 declining intrinsic value보다 비싼 가격에 이뤄지면 EPS accretion은 가치창출이 아니다.

또한 local TV는 구조적으로 cord-cutting, network fee inflation, audience fragmentation, political cycle, FCC ownership rules, refinancing cost에 노출된다. 과거의 높은 FCF yield가 terminal decline을 반영한 것인지, 아니면 계약수익과 자본배분으로 상쇄 가능한 할인인지 분리해야 한다.

### 10. 재사용 가능한 교훈

**성숙 roll-up은 다음 단계에서 ROIIC 대신 'buyback yield × discount to intrinsic value'가 주당가치 compounding을 결정한다.**

이 아이디어를 다른 기업에 재사용할 때는 단순히 `FCF yield가 높다`는 사실이 아니라, (a) FCF의 반복가능성, (b) debt와 maturity, (c) incremental acquisition/buyback return, (d) 규제 이벤트의 net cash proceeds, (e) 주당가치로 귀속되는 비율을 순서대로 검증해야 한다.

---
