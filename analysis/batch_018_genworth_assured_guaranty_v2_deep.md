# Batch 018 v2 Deep — Genworth Financial·Assured Guaranty

> 목적: 기존 Batch 018의 10개 아이디어를 `book value·reserve quality·trapped capital·HoldCo liquidity·event duration`으로 다시 읽는다.

## 1. 보험주에서 P/B가 위험한 이유

보험회사의 book value는 자산에서 회계상 부채를 뺀 값이지만, 부채의 정확도가 핵심이다. 장기요양보험(LTC)처럼 수십 년 뒤 보험금이 지급되는 상품은 morbidity, lapse, claim duration, rate increase, 투자수익률 가정이 조금만 틀려도 경제적 부채가 크게 달라진다. 따라서 `0.3x book`이 싸다는 결론을 내리기 전에 book의 분모인 reserve가 충분한지부터 검증해야 한다.

Genworth에서는 이 문제가 특히 컸다. 미국 MI 사업과 Enact 지분은 실제 가치가 있었지만 legacy LTC가 장기간 자본을 묶고 HoldCo의 현금흐름을 제한했다. 즉 좋은 자산 하나가 있다고 해서 지주회사 보통주가 그 가치 전부를 즉시 가져갈 수 있는 것은 아니다.

## 2. 현금의 위치가 가치보다 중요할 때

보험지주는 자회사 현금을 마음대로 가져올 수 없다. 각 보험자회사는 statutory capital과 RBC를 충족해야 하고, 감독당국·rating agency 기준을 만족한 뒤에야 배당을 올릴 수 있다. 그래서 아래 순서를 따라야 한다.

`segment earnings → statutory capital 필요액 → 자회사 dividend capacity → HoldCo cash → interest·debt maturity → 보통주 잔여가치`

2009년 $2 위기 Long이 강했던 이유는 단순 P/B가 아니라 HoldCo liquidity와 asset haircut을 먼저 봤기 때문이다. 반대로 이후 Long들은 ‘MI가 생각보다 괜찮다’는 반론을 LTC reserve 위험과 합쳐서 보지 못했다.

## 3. Genworth 아이디어 재평가

| 시점 | 핵심 인사이트 | 놓친 것 | v2 판정 |
|---|---|---|---|
| 2004 Long | GE spin overhang·낮은 valuation | LTC tail과 보험부채의 질 | 초기 성공, 장기 실패 |
| 2009.01 Long | liquidity panic과 asset haircut | 큰 오류 적음 | 가장 우수한 crisis Long |
| 2009.11 Long | 생존 후 book recovery | LTC가 장기 value trap을 만들 가능성 | 실패 |
| 2015 Long | 0.3x book·rate action turnaround | reserve adequacy와 trapped capital | 치명적 실패 |
| 2016 Short | LTC reserve hole 정확히 인식 | Oceanwide bid·MI asset·buyer optionality | 사업 일부 적중, 증권 실패 |
| 2017/2019 merger arb | $5.43 cash deal spread | 중국 financing·규제·시간가치 | 이벤트 실패 |
| 2020 special situation | bond와 equity payoff 분리 시도 | equity는 merger 의존, bond는 asset/liquidity 개선 수혜 | credit가 더 우수 |

### 2009년 Long과 2015년 Long의 차이

둘 다 낮은 valuation을 샀지만 2009년에는 시장이 당장 파산을 가격에 넣고 있었고 회사는 단기 liquidity를 확보할 수 있었다. 반면 2015년에는 단기 파산보다 장기 reserve deterioration이 핵심이었다. 첫 번째는 ‘생존 확률 mispricing’, 두 번째는 ‘부채 추정 자체가 틀릴 수 있는 value trap’이다. 같은 P/B 프레임을 적용하면 안 된다.

## 4. Merger arb의 핵심은 upside가 아니라 duration

Oceanwide $5.43 거래는 headline spread만 보면 매력적이었다. 하지만 중국 자본통제, 미국 규제, financing 확정성, 반복된 deadline extension이 모두 closing probability를 깎았다. merger arb 기대수익은 단순히 `(deal price/current price)-1`이 아니라 다음처럼 봐야 한다.

`기대가치 = closing probability × deal value + break probability × standalone value − time/duration cost`

거래가 계속 연장될수록 연환산 IRR은 급격히 낮아지고, standalone downside가 큰 경우 작은 확률오차가 전체 기대수익을 뒤집는다.

## 5. Assured Guaranty에서 배울 점

Assured Guaranty는 monoline 보험사이므로 핵심은 premium growth보다 insured portfolio의 loss severity와 claim-paying resources다. 금융위기 이후 FSA 인수와 경쟁자 퇴출은 franchise를 강화했지만 adjusted book가 빠르게 market value로 수렴할 것이라는 가정은 너무 단순했다. 보험사의 discount는 reserve uncertainty, runoff duration, 신규보험 성장률과 capital return 속도 때문에 오래 지속될 수 있다.

따라서 AGO 같은 회사에서는 `adjusted book per share`와 함께 `insured exposure runoff`, `economic loss development`, `excess capital`, `buyback discount`를 동시에 봐야 한다.

## 6. 사전 반증조건

- LTC claim incidence·duration이 예상보다 나빠지는데 rate increase만으로 해결 가능하다고 가정하면 안 된다.
- statutory capital이 늘어 자회사 배당가능액이 줄면 HoldCo SOTP를 즉시 낮춰야 한다.
- merger deadline이 두 번 이상 연장되고 financing 조건이 완결되지 않으면 확률을 기계적으로 하향해야 한다.
- adjusted book가 유지돼도 실제 capital return이 없다면 duration discount를 높여야 한다.

## 7. 통합 Postmortem

이 배치의 핵심은 **보험주의 ‘싼 장부가’는 자산 문제가 아니라 부채와 현금이동 문제일 수 있다**는 것이다. Genworth의 MI/Enact는 실제 가치가 있었지만 LTC와 HoldCo 구조가 그 가치의 즉시 귀속을 막았다. Assured Guaranty 역시 book value 자체보다 손실의 최종 확정과 자본환원 속도가 중요했다.

- **Business thesis:** segment별로 크게 달랐으며 MI는 좋은 자산, LTC는 장기 tail liability였다.
- **Valuation thesis:** P/B는 reserve quality와 trapped capital을 조정해야 의미가 있다.
- **Catalyst/timing:** 2009 crisis Long은 좋았고 Oceanwide arb는 duration을 과소평가했다.
- **Security selection:** 2020의 bond가 equity보다 더 견조했던 이유는 payoff가 merger보다 asset coverage와 debt reduction에 더 연결됐기 때문이다.
- **재사용 질문:** `이 book value 중 실제로 3년 안에 HoldCo 보통주에게 현금으로 올라올 수 있는 금액은 얼마인가?`