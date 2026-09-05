<!-- idea:924b250f-5703-4a82-8537-fac2a187abd1 -->
## 4. 2016-01-29 — Media General spectrum CVR을 분리한 2016 pair trade
### 1. 결론부터

**종합판정: 성공·가치 추정은 과대.** 증권구조를 분리해 fundamental NXST beta를 제거한 점이 좋았다. 하지만 auction gross proceeds에서 세금·repack·fees·계약공제 후 CVR holder에게 귀속되는 waterfall을 과대평가했다.

### 2. 원 투자논지

거래조건 $10.55 cash + 0.1249 NXST + spectrum auction CVR에서 NXST 주가노출을 short로 제거하고 CVR만 싸게 사는 구조였다. 시장 내재 CVR을 약 $0.85로 보고 $2~3, 최대 $4 가능성을 제시했다.

원문 SQL에는 `is_short=true`가 저장돼 있지만 실제 증권 방향은 **Pair/Event**이다. 이 차이는 raw 데이터 자체를 수정하지 않고 research layer의 `research_direction_ko`와 `security_instrument_ko`에 명시했다.

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

거래는 2017-01-17 종결됐다. Nexstar는 Media General의 spectrum auction gross proceeds를 약 $479m으로 추정했고, 2017년 실제 gross proceeds $478.6m을 받았다. 2017년 8월 CVR holders에 $258.6m initial payment, 연말 remaining liability $12.4m이 기록됐다. 총 payout은 positive였지만 원문의 $2~3 base case보다 낮은 수준이었다.

### 6. 주장별 검증

- **방향:** 원문 기준 Pair/Event; raw SQL Short flag는 오류 또는 security-level 분류 미흡이다.
- **사업:** 거래조건 $10.55 cash + 0.1249 NXST + spectrum auction CVR에서 NXST 주가노출을 short로 제거하고 CVR만 싸게 사는 구조였다. 시장 내재 CVR을 약 $0.85로 보고 $2~3, 최대 $4 가능성을 제시했다.
- **촉매:** 거래는 2017-01-17 종결됐다. Nexstar는 Media General의 spectrum auction gross proceeds를 약 $479m으로 추정했고, 2017년 실제 gross proceeds $478.6m을 받았다. 2017년 8월 CVR holders에 $258.6m initial payment, 연말 remaining liability $12.4m이 기록됐다. 총 payout은 positive였지만 원문의 $2~3 base case보다 낮은 수준이었다.
- **밸류에이션/청구권:** 증권구조를 분리해 fundamental NXST beta를 제거한 점이 좋았다. 하지만 auction gross proceeds에서 세금·repack·fees·계약공제 후 CVR holder에게 귀속되는 waterfall을 과대평가했다.
- **반증:** CVR contract의 deductible, tax, channel-sharing/repack 비용이 예상보다 크거나 auction proceeds가 낮으면 implied discount는 사라진다.
- **사후평가:** 성공·가치 추정은 과대

### 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| cash consideration | 10.55 | USD/share | Nexstar |
| NXST ratio | 0.1249 | share/share | Nexstar |
| gross spectrum proceeds | 478.6 | USD m | Nexstar 2017 annual report |
| initial CVR payment | 258.6 | USD m | Nexstar 2017 annual report |

### 8. 촉매와 타임라인

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2016-01-27 | 거래조건 합의 | $10.55 + 0.1249 NXST + CVR |
| 2016-01-29 | VIC pair 게시 | CVR isolation |
| 2017-01-17 | Media General close | CVR 발행 |
| 2017-07-21 | spectrum proceeds 수령 | gross $478.6m |
| 2017-08-28 | initial CVR payment | $258.6m |
| 2017-12-31 | remaining CVR liability | $12.4m |

### 9. 반증조건과 놓치기 쉬운 변수

**사전 반증조건:** CVR contract의 deductible, tax, channel-sharing/repack 비용이 예상보다 크거나 auction proceeds가 낮으면 implied discount는 사라진다.

또한 local TV는 구조적으로 cord-cutting, network fee inflation, audience fragmentation, political cycle, FCC ownership rules, refinancing cost에 노출된다. 과거의 높은 FCF yield가 terminal decline을 반영한 것인지, 아니면 계약수익과 자본배분으로 상쇄 가능한 할인인지 분리해야 한다.

### 10. 재사용 가능한 교훈

**CVR·stub trade는 자산가치보다 계약 waterfall을 먼저 모델링하고 hedge ratio를 계약단위로 고정해야 한다.**

이 아이디어를 다른 기업에 재사용할 때는 단순히 `FCF yield가 높다`는 사실이 아니라, (a) FCF의 반복가능성, (b) debt와 maturity, (c) incremental acquisition/buyback return, (d) 규제 이벤트의 net cash proceeds, (e) 주당가치로 귀속되는 비율을 순서대로 검증해야 한다.

---
