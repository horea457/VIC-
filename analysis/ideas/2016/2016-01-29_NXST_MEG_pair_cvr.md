# Media General / Nexstar (MEG–NXST) — 2016-01-29 VIC Pair / CVR Trade

> **Idea unit:** 2016-01-29 Media General merger consideration에서 spectrum auction CVR만 최대한 분리해 산 event-driven trade다.  
> 이 아이디어는 Nexstar common equity Long이 아니라 **MEG Long + 계약상 지급되는 0.1249 NXST를 Short hedge하여 CVR/stub를 격리**하는 구조다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 관련 회사 | Media General / Nexstar Broadcasting Group |
| VIC 게시일 | 2016-01-29 |
| Idea ID | `924b250f-5703-4a82-8537-fac2a187abd1` |
| 작성자 | jdr907 |
| Raw SQL flag | Short |
| Research direction | **Pair / Event-driven** |
| Security | Long MEG common + Short 0.1249 NXST per MEG share |
| 거래대가 | $10.55 cash + 0.1249 NXST + spectrum auction CVR |
| 원문 내재 CVR 가치 | 시장 약 $0.85 |
| 원문 기대 CVR | base $2~3, upside 최대 약 $4 |
| 실제 핵심 | spectrum gross proceeds $478.6m; initial CVR payment $258.6m; 2017YE remaining liability $12.4m |
| 최종 판정 | **Trade structure 성공 / CVR 가치 추정 과대** |
| 데이터 검증 기준일 | 2026-09-09 |

---

## 1. 이 거래는 정확히 무엇인가

## 1.1 일반 주식투자와 다른 이유

2016년 Nexstar는 Media General을 인수하기로 했다. MEG 주주가 받는 가치는 세 조각이었다.

1. **현금 $10.55**
2. **Nexstar 주식 0.1249주**
3. **FCC incentive spectrum auction 결과에 연동되는 CVR**

원 아이디어는 Nexstar 사업 자체의 주가 상승에 베팅하는 것이 아니라, MEG 주가 속에 암묵적으로 싸게 거래되는 **CVR의 기대가치**를 사려는 특수상황이었다.

따라서 경제적 payoff는:

**MEG 매수가격  
- 확정 현금 $10.55  
- 0.1249 × NXST 주가노출  
= 시장이 CVR + deal risk에 붙인 가격**

으로 볼 수 있다.

0.1249 NXST를 Short하면 fundamental NXST beta의 상당 부분이 제거된다.

## 1.2 CVR이란 무엇인가

CVR(Contingent Value Right)은 특정 사건 결과에 따라 추가 현금을 받을 권리다. 여기서는 Media General 방송국이 FCC spectrum auction에 참여해 얻는 순수익 일부가 주주에게 돌아오는 구조였다.

중요한 점은 **auction gross proceeds = CVR payout**이 아니라는 것이다.

실제 waterfall은 대략:

**Gross spectrum auction proceeds  
- 세금  
- repacking/channel-sharing 비용  
- transaction/administrative costs  
- 계약상 공제항목  
- 기타 holdback  
= CVR holders에게 분배 가능한 금액**

이다.

## 1.3 거래의 단위경제성

이 아이디어의 단위는 ‘방송국 1개’가 아니라 **MEG 1주가 갖는 CVR claim**이다.

따라서 필요한 계산은:

**Expected CVR/share  
= Σ(auction outcome별 확률 × net distributable proceeds) / eligible shares**

이다.

방송국 가치가 높다는 주장과 CVR holder payout이 높다는 주장은 다르다. 법적 waterfall을 통과해 실제 권리자에게 돈이 와야 한다.

---

## 2. 당시 상황과 시장의 가격

## 2.1 게시 당시 상황

2016-01-27 Nexstar와 Media General은 거래조건에 합의했다. 시장은 cash와 NXST stock consideration은 비교적 쉽게 가격에 넣을 수 있었지만 FCC incentive auction의 결과는 불확실했다.

이 때문에 CVR에는:

- 어떤 station이 auction에 들어가는지
- spectrum clearing price
- 세금·비용
- closing timing
- 거래 실패 가능성

이 한꺼번에 할인돼 있었다.

## 2.2 시장이 암묵적으로 넣은 CVR

원문은 MEG 가격에서 현금과 0.1249 NXST를 빼면 CVR 가치가 약 $0.85 정도밖에 반영되지 않았다고 보았다.

원 저자는 보유 spectrum의 경제적 가치가 더 높아 **$2~3 base, 최대 약 $4**까지 가능하다고 추정했다.

핵심 비대칭은:

**시장 implied CVR 약 $0.85 vs 원문 expected CVR $2~3+**

였다.

---

## 3. 원문 투자논지 지도

| Claim | 원문 주장 | 작동 메커니즘 | 숨은 가정 | 사전 반증조건 |
|---|---|---|---|---|
| C1 | MEG에 CVR이 싸게 내재돼 있다 | cash/stock을 hedge하면 contingent claim만 남음 | hedge basis가 계약과 잘 맞음 | deal spread/CVR implied value 급상승 |
| C2 | spectrum gross value가 높다 | scarce broadcast spectrum → auction bids | auction clearing price 충분 | auction demand/price 하락 |
| C3 | CVR holder가 gross value 상당 부분을 받는다 | auction proceeds → contract waterfall → payout | 세금/비용/holdback 낮음 | net/gross conversion 급락 |
| C4 | NXST hedge로 business beta를 제거할 수 있다 | 0.1249 ratio short | ratio/borrow/closing terms 안정 | borrow squeeze 또는 terms 변경 |
| C5 | 거래가 예정대로 닫힌다 | regulatory approval → CVR 발행 | FCC/DOJ 승인 가능 | closing probability 급락 |
| C6 | duration이 감당 가능하다 | event calendar가 가치실현 시점 제한 | auction/settlement 지연 제한 | 수년 지연 + carry 증가 |

## C1. 시장이 CVR을 지나치게 싸게 평가한다

**원문 주장**  
MEG 주가에서 확정 cash와 NXST stock value를 제거하면 CVR이 약 $0.85에 거래되고 있는데 내재 spectrum value를 감안하면 너무 낮다는 주장이다.

**경제적 메커니즘**  
합병 consideration의 다른 조각을 hedge하면 남는 payoff가 CVR에 가까워진다. 실제 payout이 implied price보다 크면 event return이 발생한다.

**숨은 가정**  
MEG의 잔여 deal risk와 NXST hedge basis가 작아야 한다.

**실제**  
CVR은 실제로 양(+)의 payout을 냈다.

**판정: 적중**

## C2. Spectrum auction proceeds는 충분히 크다

Nexstar는 Media General 관련 spectrum auction gross proceeds를 약 $479m으로 추정했고 실제 2017년 gross proceeds는 $478.6m이었다.

**판정: 매우 적중**

## C3. Gross proceeds가 CVR holders에게 거의 그대로 전달된다

여기가 가장 중요한 오류였다. 실제 initial CVR payment는 $258.6m이고 2017년 말 remaining liability는 $12.4m이었다. Gross $478.6m과 상당한 차이가 난다.

즉 원문은 **asset value**는 잘 맞혔지만 **claim value**를 과대평가했다.

**판정: 실패 / 핵심 valuation error**

## C4. 0.1249 NXST Short로 beta를 제거한다

거래조건에 명시된 stock ratio만큼 hedge하는 방식은 특수상황의 핵심 장점이었다. NXST가 크게 움직여도 CVR thesis의 상대적 순도가 높아진다.

다만 borrow fee, dividend, hedge rebalance, closing timing은 실제 realized return에서 차감해야 한다.

**판정: 적중**

## C5. 거래는 닫힌다

거래는 2017-01-17 종결됐다.

**판정: 적중**

## C6. 이벤트 시간이 가치를 잠그지 않는다

거래종결 → spectrum proceeds 수령 → initial CVR payout이 2017년에 이어졌다. duration은 존재했지만 무한정 늘어지지 않았다.

**판정: 대체로 적중**

---

## 4. Valuation과 Legal Waterfall

## 4.1 원문 방식

원문은 대략:

**MEG price - $10.55 cash - 0.1249×NXST = implied CVR**

을 통해 약 $0.85를 도출했다.

그리고 spectrum 가치를 station별로 추정해 $2~3 base case를 제시했다.

## 4.2 더 나은 방식

이 거래는 반드시 두 단계를 분리해야 한다.

### Step 1 — Asset value
**각 station spectrum × auction clearing value = gross proceeds**

### Step 2 — Security claim value
**Gross proceeds  
- taxes  
- repack/channel-sharing  
- transaction/admin  
- contractual deductions/holdbacks  
= distributable CVR pool  
÷ eligible CVRs  
= CVR per share**

원문은 Step 1은 매우 잘 맞혔고 Step 2를 너무 낙관적으로 봤다.

## 4.3 시나리오

| Case | Auction | Net/gross conversion | 결과 |
|---|---|---|---|
| Adverse | 낮은 clearing price | 낮음 | implied $0.85 이하 가능 |
| Base | gross ~$400~500m | 중간 | positive payout, 원문 base보다 낮을 수 있음 |
| Bull | 높은 spectrum price | 높음 | $2~3+ 가능 |

실제는 **gross proceeds는 Bull에 가까웠지만 net-to-holder conversion은 Base/Adverse에 가까웠다.**

## 4.4 Deal risk와 carry

Event trade의 실제 IRR은 단순 payout spread가 아니라:

**CVR payout + cash consideration + hedge P&L - entry cost - borrow - dividends - financing cost**

를 투자기간으로 연환산해야 한다.

현재 curated DB에는 정확한 MEG T0 price, NXST hedge execution price, borrow/dividend carry가 고정돼 있지 않아 정확 realized IRR은 미기재한다.

---

## 5. 실제 Timeline

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2016-01-27 | 거래조건 합의 | $10.55 + 0.1249 NXST + CVR |
| 2016-01-29 | VIC pair 게시 | implied CVR discount |
| 2017-01-17 | Media General close | CVR 발행/거래구조 확정 |
| 2017-07-21 | spectrum proceeds 수령 | gross $478.6m |
| 2017-08-28 | initial CVR payment | $258.6m pool |
| 2017-12-31 | remaining CVR liability | $12.4m |

---

## 6. 실제 투자결과

**방향성:** 성공. 시장이 CVR을 0으로 보던 것은 아니었지만, 실제로 추가 지급가치가 존재했다.

**정량 추정:** 원문이 기대한 $2~3 base case보다 실제 holder payout은 낮았다. 따라서 “CVR이 undervalued”는 맞았지만 “얼마나 undervalued인가”는 과장됐다.

정확 realized IRR은 MEG entry, NXST hedge execution, borrow, dividend, final CVR distributions를 한 세트로 맞춘 뒤 계산해야 한다.

---

## 7. Claim별 사후 판정

### 맞춘 것
- CVR이 유의미한 경제적 가치를 가짐
- spectrum gross proceeds 수준
- merger closing
- hedge 구조 자체

### 틀린 것
- gross spectrum proceeds → CVR payout conversion
- 세금·비용·contractual deductions의 크기

### 가장 중요한 숨은 가정
**자산가치가 곧 증권가치로 거의 그대로 이전된다.**

### 최초 경고신호
CVR agreement의 정의상 deductible/expense/tax 항목을 세부적으로 읽었을 때 gross proceeds와 distributable pool 사이 gap이 클 수 있다는 점.

---

## 8. 무엇이 실제 수익과 오차를 만들었는가

수익의 핵심은 방송주 방향성이 아니라 **고정 현금·주식대가를 헤지하고 별도 CVR claim만 남긴 계약 구조**였다. 거래 종결과 spectrum proceeds 발생은 이 구조를 실제 현금가치로 전환했다. 오차는 auction asset의 headline gross value에서 세금·repacking·관리비·holdback을 뺀 **실제 distributable pool**로 내려오는 구간에서 발생했다.

### Counterfactual

Opening bid에 50% haircut, gross proceeds에서 CVR pool로의 conversion에 추가 40% haircut, 18개월 지급지연과 short borrow·배당 carry를 적용해도 내재가 $0.85 대비 충분한 연환산 수익률이 남았는가?

---

## 9. 분석 오류 유형과 최초 경고

핵심 오류는 **FCC opening bid → gross auction proceeds → issuer net proceeds → CVR distributable proceeds**를 하나의 가치로 취급한 것이다. 또한 “CVR이 0이어도 downside가 거의 0”이라는 표현은 시간가치, deal break, borrow fee, 배당 mismatch와 hedge execution을 제외했다.

### 최초로 관찰 가능했던 경고신호

CVR agreement의 세금·비용·공제·holdback 정의가 T0의 최초 경고였다. 사후에는 2017년 gross proceeds 약 $478.6m 대비 초기 CVR 지급액 약 $258.6m이 공개되며 gross-to-net haircut이 핵심 변수였음이 확인됐다.

---

## 10. 재사용 가능한 교훈과 체크리스트

1. CVR은 underlying asset이 아니라 계약서의 **net distributable claim**으로 가치평가한다.
2. Exchange ratio hedge는 비율만이 아니라 borrow, 배당, rebalance, closing date를 현금흐름에 넣는다.
3. Event outcome과 event duration을 분리해 지급지연까지 IRR에 반영한다.

### 지금 같은 아이디어를 다시 본다면

- exchange ratio와 hedge rebalancing
- deal break·regulatory conditions
- gross-to-net CVR waterfall
- 세금·거래비용·escrow·holdback
- CVR outstanding 수와 지급순위
- short borrow·배당·지급지연
- exact execution price와 hedge-adjusted IRR

---

## 11. 최종 Scorecard

| 항목 | 판정 |
|---|---|
| Asset thesis | **강한 적중** |
| Legal/waterfall thesis | **실패** |
| Valuation thesis | **부분 적중** |
| Deal-closing thesis | **적중** |
| Hedge/security selection | **강한 적중** |
| Timing | **대체로 적중** |
| 최종 투자결과 | **성공, 기대수익 과대** |

### 한 문장 교훈

> **CVR·stub 투자에서는 underlying asset value보다 그 가치가 어떤 법적 waterfall을 거쳐 내 증권에 몇 달러 귀속되는지를 먼저 모델링해야 한다.**

---

## 12. Sources / Validation Notes

1. Value Investors Club — 2016-01-29 Media General/Nexstar CVR pair idea.
2. Nexstar transaction announcement — $10.55 cash + 0.1249 NXST + CVR.
3. Nexstar 2017 annual report — $478.6m gross spectrum proceeds, $258.6m initial CVR payment, $12.4m remaining liability.
4. Existing curated postmortem: `analysis/batch_039_nexstar_sinclair_part04.md`.

## 추가 정밀화 필요
- 2016-01-29 MEG와 NXST exact execution price
- exact final CVR per-share distributions
- NXST borrow fee/dividend carry
- hedge-adjusted realized IRR와 max adverse excursion
