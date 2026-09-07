# Batch 010 v2 Deep — 항공·렌터카·자동차와 자본구조

## 목적
이 배치는 좋은 운영자산과 좋은 보통주가 같지 않다는 점을 가장 강하게 보여준다. 항공기·렌터카 fleet·자동차공장처럼 실물자산이 커도 높은 레버리지와 중고자산 가격, 계약·규제·유동성 경로를 함께 보지 않으면 equity 하방을 잘못 계산한다. 기존 30개 아이디어의 사업설명은 유지하면서 청구권·만기·담보·거래구조 관점으로 더 구체화한다.

---

# 1. Aimia/AerCap — entity부터 정확히 확인

먼저 가장 중요한 데이터 오류부터 분리한다. 캐나다 Groupe Aeroplan/Aimia와 NYSE ticker AER인 AerCap은 전혀 다른 회사다. ticker 충돌 때문에 잘못된 가격성과를 붙이면 투자 postmortem 전체가 무효가 된다.

## Aimia 돈의 흐름
카드사·항공사·소매업체가 포인트를 미리 구매 → Aimia가 현금을 먼저 받음 → 고객이 나중에 포인트를 항공권·상품으로 사용 → redemption 비용 발생. 미사용 포인트인 breakage와 포인트 판매가격-보상원가 spread가 이익원이다.

핵심 위험은 포인트 회계가 아니라 anchor partner다. Air Canada나 주요 카드사가 떠나면 적립량과 사용가치가 동시에 떨어진다. 따라서 `포인트 float = 영구 저비용자금`이 아니다.

## AerCap 돈의 흐름
항공기 매입 → 항공사에 장기 임대 → lease rent 수취 → 이자·감가상각·관리비·신용손실 차감 → lease 종료 후 재임대 또는 매각. book value보다 실제 resale value와 funding cost가 중요하다.

### 왜 leverage가 중요한가
자산 $100, 부채 $70, equity $30인 회사에서 항공기 가치가 10% 하락해 $90이 되면 equity는 $20으로 33% 줄어든다. asset haircut이 equity에 확대되는 이유다.

### AerCap 아이디어 RECAP
- 2014 ILFC Long: forced-sale acquisition과 scale economics는 맞았지만 명시기간 수익은 기대에 못 미쳤다.
- 2017/2018 Long: book discount를 안전마진으로 봤지만 COVID 같은 correlated tail에서 asset value와 funding spread가 동시에 악화될 수 있음을 과소평가했다.
- 2020 COVID Long: 이미 극단적 stress 가격에서 liquidity runway와 movable collateral을 산 것이 핵심 성공요인.
- 2022 GECAS Long: accretion과 buyback은 맞았지만 러시아 항공기 압류라는 새로운 tail shock가 발생했다.

**재사용 원칙:** `P/B가 낮다`가 아니라 `stress asset value - net debt - required liquidity reserve`를 계산한다.

---

# 2. Hertz — 산업생존과 issuer 생존은 다르다

렌터카 회사는 차량을 대량 매입하거나 ABS·fleet debt로 조달해 단기간 임대하고, 중고차로 매각한다. 경제성은 단순 대여료가 아니다.

`Rental revenue - fleet depreciation - vehicle interest - operating expense`가 핵심이다. 여기서 fleet depreciation은 회계숫자이면서 실제 중고차 가격과 매우 밀접하다.

## 핵심 용어
- **Fleet debt/ABS:** 차량을 담보로 조달하는 부채. 회사 일반채무와 상환순위·담보가 다를 수 있다.
- **Residual value:** 차량을 팔 때 받을 중고차 가치.
- **Corporate debt vs vehicle debt:** 차량담보부채가 있다고 해서 보통주가 안전한 것은 아니다. corporate level 고정비·이자·유동성 부족이 equity를 먼저 압박할 수 있다.

## 아이디어별 핵심
- 2018 equity Long: 중고차 가격과 turnaround를 봤지만 높은 leverage와 cyclical travel demand의 동시충격을 충분히 넣지 않았다.
- 2019 debt Short: capital structure 취약성과 fleet economics 악화를 공격한 것이 더 직접적인 security selection이었다.
- 2020 bankruptcy는 렌터카 수요가 언젠가 회복하느냐와 별개로, 기존 issuer가 그때까지 버틸 수 있느냐가 핵심임을 보여줬다.
- 2022 equity Long: post-reorg Hertz는 과거와 다른 자본구조였지만, 중고차 가격 정상화와 EV fleet 전략의 economics를 과도하게 낙관하면 다시 같은 오류가 생긴다.

**RECAP:** 좋은 recovery asset도 높은 leverage에서는 timing이 틀리면 equity가 0이 될 수 있다.

---

# 3. Spirit Airlines — common, EETC, merger arb는 완전히 다른 투자

Spirit의 운영모델은 초저가 운임에 ancillary fee를 붙이는 ULCC다. 항공기 utilization을 높이고 좌석밀도를 높여 CASM을 낮추는 것이 핵심이다. 하지만 fuel·labor·airport fee·aircraft lease가 크게 오르면 저운임 장점이 약해진다.

## EETC란
**Enhanced Equipment Trust Certificate**는 항공기를 담보로 발행되는 구조화 채권이다. 항공사 보통주와 달리 특정 항공기·lease payment에 대한 담보와 priority가 있다. 항공사가 어려워져도 항공기 회수·재임대 가치가 채권 회수율을 지지할 수 있다.

## Merger arbitrage란
예를 들어 거래가격이 $30인데 주가가 $24라면 $6 spread가 있다. 수익률은 단순 25%가 아니라 `거래종결확률 × $30 + 실패시 standalone value × 실패확률`로 계산해야 한다. 규제소송, financing, outside date가 핵심이다.

## 아이디어별 RECAP
- 2012/2013 equity Long: 구조적으로 낮은 unit cost와 ancillary revenue를 잘 봤다.
- 2017 Long: 비용우위가 영구적이고 경쟁사가 쉽게 모방하지 못한다는 가정이 약했다.
- 2020 EETC Long: 보통주가 아니라 담보청구권을 산 것이 성공확률을 높였다.
- 2022 JetBlue arb: Spirit business quality가 아니라 DOJ 승인확률과 break price를 샀다. 법률·정책 tail을 0에 가깝게 두면 안 된다.

---

# 4. General Motors — 구 GM, New GM, warrant, tech option 분리

GM 사례는 같은 이름의 기업이라도 파산 전 common과 파산 후 New GM common이 다른 security라는 점을 보여준다.

## 핵심 구조
자동차 사업은 차량 판매 gross profit뿐 아니라 captive finance, pension, warranty, dealer incentives, working capital, capex, union obligation이 함께 움직인다. EV/AV option은 별도로 가치가 있지만 core ICE cash flow와 무관하게 무한한 가치를 주면 안 된다.

## 주요 아이디어
- 2009 call Short: 구 GM common의 residual claim이 거의 사라진 상황에서 option price가 과도하다는 구조적 trade였다.
- 2011 Long: New GM의 낮은 valuation과 현금은 매력적이었지만 auto cycle과 pension/Europe risk를 과소평가했다.
- 2012 Long: 더 낮은 valuation에서 balance sheet와 buyback optionality를 산 것이 상대적으로 우월했다.
- 2017 Long: Cruise/AV 같은 기술 option을 core valuation에 더했지만 option 가치가 곧 현금으로 실현되는 것은 아니다.

**RECAP:** 자동차에서는 `normalized EBIT`만 볼 게 아니라 cycle trough liquidity와 pension·finance subsidiary·capex까지 cash waterfall로 연결한다.

---

# 5. 통합 Postmortem

1. **Asset value와 equity value를 분리한다.** 항공기·차량·공장 가치가 있어도 그 위에 debt가 있다.
2. **같은 회사도 증권별 payoff가 다르다.** common, senior debt, EETC, warrant, merger arb는 전혀 다른 투자다.
3. **만기와 liquidity가 valuation보다 먼저다.** 회사가 장기적으로 회복해도 만기 전 현금이 없으면 기존 equity는 소멸할 수 있다.
4. **중고자산 가격은 핵심 변수다.** aircraft residual, used-car prices가 leverage를 통해 equity에 확대된다.
5. **이벤트 투자에서 사업분석과 deal probability를 섞지 않는다.**

각 아이디어 최종판정은 `Business / Asset value / Liability waterfall / Liquidity / Catalyst / Timing / Security selection / 실제 투자결과`로 기록한다.