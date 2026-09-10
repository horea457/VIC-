# Batch 058 — Advanced Emissions Solutions / Adient V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 057 마지막 ADES 2012-07-15 이후, reviewed idea_id를 제외한 다음 10건.
> **핵심 데이터 품질:** raw direction 교정 7건. ADES 2013 source body는 외부 Dropbox PDF 소실로 제한적 reconstruction.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2013-05-10 | ADES | **Short** | **Long** | [ADES 2013](ideas/2013/2013-05-10_ADES_long.md) | **경제 thesis 성공 / security path 변동적** |
| 2 | 2015-07-03 | ADES | Long | Long | [ADES 2015](ideas/2015/2015-07-03_ADES_long.md) | **operating/catalyst 부분 성공, valuation target 실패** |
| 3 | 2016-09-30 | ADES | **Short** | **Long** | [ADES 2016](ideas/2016/2016-09-30_ADES_long.md) | **cash-return thesis 성공 / upside targets 과도** |
| 4 | 2017-12-13 | ADES | Long | Long | [ADES 2017](ideas/2017/2017-12-13_ADES_long.md) | **base runoff validated / large upside 실패** |
| 5 | 2021-05-19 | ADES | **Short** | **Long** | [ADES 2021](ideas/2021/2021-05-19_ADES_long.md) | **APT operating thesis 성공 / sale-catalyst 실패** |
| 6 | 2016-11-08 | ADNT | **Short** | **Long** | [ADNT 2016](ideas/2016/2016-11-08_ADNT_long.md) | **초기 성공 / 장기 operating thesis 붕괴** |
| 7 | 2017-05-31 | ADNT | **Short** | **Long** | [ADNT 2017](ideas/2017/2017-05-31_ADNT_long.md) | **강한 실패** |
| 8 | 2018-05-22 | ADNT | **Short** | **Long** | [ADNT 2018](ideas/2018/2018-05-22_ADNT_long.md) | **매우 강한 실패** |
| 9 | 2019-05-09 | ADNT | Short | Short | [ADNT 2019 Short](ideas/2019/2019-05-09_ADNT_short.md) | **전술적 성공 / $5 target 미달** |
| 10 | 2020-08-17 | ADNT | **Short** | **Long** | [ADNT 2020](ideas/2020/2020-08-17_ADNT_long.md) | **중간구간 성공 / 5Y target 실패** |

---

# PART A — Direction / Source Audit

## 2. Direction corrections

### 실제 Long인데 raw Short
- ADES 2013
- ADES 2016
- ADES 2021
- ADNT 2016
- ADNT 2017
- ADNT 2018
- ADNT 2020

총 **7건**.

### Raw와 실제 일치
- ADES 2015 Long
- ADES 2017 Long
- ADNT 2019 Short

---

## 3. ADES 2013 source-body limitation

2013 idea의 SQL body에는:
- “interesting value proposition”
- material investment disclosure
- Dropbox PDF URL

만 남아 있다.

외부 PDF 원문이 현재 dataset에 없으므로:
- exact target
- detailed original DCF
- original claim wording

을 **추정해 채우지 않았다**.

대신 2012/2015 후속 VIC 글과 공식 cash-flow history를 이용해 핵심 thesis만 보수적으로 reconstruction.

---

# PART B — ADES: Cash Flow를 맞혀도 Value Realization은 별개

## 4. 2013→2017 공통 asset: Refined Coal

핵심 구조:

**Section 45 tax credits  
→ tax-equity investors  
→ Tinuum / CCS facility payments  
→ ADES 42.5% economic interest  
→ cash distributions**

실제 cash distributions:
- 2015: ~$8.65m
- 2016: **$41.65m**
- 2017: **$48.88m**

따라서 refined-coal cash-flow mechanism은 반복해서 검증됐다.

---

## 5. ADES 2015 Long — “BadCo=0” 접근은 좋았지만 DCF가 높았다

당시:
- auditor resignation
- OTC delisting
- accounting review
- emissions-control deterioration

writer는:
**Emissions Control = zero**

로 놓고 Refined Coal만 DCF.

Valuation:
- 15% discount rate → **$24.50**
- 8% → **$30**
- 일부 facilities only → ~$17.85
- deep downside → ~$10.75

실제:
- 2016 Nasdaq 재상장
- Tinuum cash flow 증가
- financials current

즉 catalysts는 발생.

하지만 $25~30 price realization은 실패.

### 왜?
- facility ramp timing
- holdco G&A
- finite-life duration
- accounting discount
- capital-allocation uncertainty

---

## 6. ADES 2016 Long — “현금 반환” 자체는 정확히 맞힘

price:
**$7.50**

writer:
- runoff ~$12
- 12M catalyst $20+
- patent tail $50+

실제 2017:
- Tinuum distribution **$48.875m**
- dividends paid **$15.7m**
- Dutch tender **$9.40**
- 추가 buyback authorization

즉:
**cash harvesting starts**
라는 claim은 강한 성공.

하지만:
- $20+
- $50 patent tail

은 현실화되지 않음.

### 교훈
**Capital return amount를 맞히는 것과 market multiple을 맞히는 것은 별개.**

---

## 7. ADES 2017 Long — Tax reform scare는 지나갔지만 double은 안 나옴

VIC page:
- price $10
- market cap $210m
- net cash $25m

writer:
- runoff DCF **$11.50**
- organic upside high teens
- legislative option +100%

Tax reform:
- corporate AMT
- BEAT

리스크를 다룸.

결과:
- core tax-credit economics 생존
- Tinuum cash flow 지속
- large rerating은 실패

### 핵심
**risk-removal ≠ upside-magnitude guarantee**

---

## 8. ADES 2021 Long — Cash-rich cigar butt의 가장 중요한 리스크

VIC page:
- price **$5.35**
- market cap **$98m**
- net cash **$27m**

remaining RC cash:
**$50~60m**

expected YE21 net cash:
**~$82m**

따라서 APT implied value:
**~$16m**

APT:
- Red River 150m lbs capacity
- Cabot long-term supply agreements
- 10~15% price increase
- end-FY21 target $15~20m EBITDA

### 실제 operating result
2022:
- revenue ~$103m
- consumables sales +20%
- company-described best year for activated-carbon assets since 2018 acquisition

즉 APT turnaround는 맞았다.

### 하지만 strategic review 결과
writer 기대:
- sale
- liquidation
- capital return

실제:
- **Arq acquisition**
- growth capex / new strategy

### 핵심
> **Net cash is a floor only if management distributes it.**

---

## 9. ADES 시계열

| 시점 | 핵심 가치 | 무엇이 맞았나 | 무엇이 틀렸나 |
|---|---|---|---|
| 2013 | Refined Coal | cash mechanism | governance path |
| 2015 | RC DCF | relisting/cash | valuation magnitude |
| 2016 | runoff + return | dividends/tender | tail targets |
| 2017 | tax scare | credit survives | high-teens rerating |
| 2021 | APT + cash | APT turnaround | sale/liquidation catalyst |

### 분석 변화
**asset economics는 반복적으로 맞았지만, public-company capital allocation이 계속 value-realization 변수가 됨.**

---

# PART C — ADIENT: Spin-Off Long에서 구조적 Short까지

## 10. ADNT 2016 Long — Spin-off mispricing은 맞았다

원문:
- global seating share ~34%
- China share ~45%
- FY17 EBITDA ~$1.575bn
- baseline $47~56
- FY18 EPS ~$10.15
- FCF-yield value ~$62

실제:
- 2017 high **$84.05**
- 2017 close ~$76.98

초기 rerating은 강하게 성공.

그러나:
- 2018 close **$15.06**
- annual decline ~80%

### 교훈
**Spin technical success ≠ durable operating thesis.**

---

## 11. ADNT 2017 Long — Peer margin gap을 opportunity로 본 오류

원문:
- current ~$67
- FY20 EPS **$14.75**
- 10x
- target **$150**
- +125% / 2.5Y

Margin bridge:
1. SG&A ~150bp
2. metals/SS&M ~100~200bp
3. China JV
4. aircraft seating optionality

### 실제
SG&A savings:
**부분 성공**

SS&M:
**대규모 실패**

원인:
- launch issues
- outsourced stamping
- premium freight
- specialty alloy shortages
- line stoppage damages

### 핵심
> **Peer margin gap can be a cost opportunity — or evidence that your business is structurally harder.**

---

## 12. ADNT 2018 Long — Known bad news라고 safe하지 않았다

price:
**~$56**

normalized EPS:
**$8.62**

P/E:
**6.5x**

DCF:
**$92**

writer는 SS&M을:
**temporary operational problem**
으로 판단.

실제 2018:
- gross margin **9% → 5%**
- stock close **$15.06**

### 핵심
Known issue의 위험은:
- 알려져 있느냐
가 아니라
- **duration과 cash cost를 시장이 정확히 알고 있느냐**
다.

---

# PART D — 2019 Short가 Long보다 더 잘 본 것

## 13. ADNT 2019 Short

writer 핵심:
**adjusted earnings ≠ cash economics**

원문:
- FY15 이후 adjusted NI ~$3.5bn
- 같은 기간 FCF **-$1.4bn**
- FY17 이후 adjusted NI ~$1.46bn
- FCF ~$100m

target:
**$5**

### 구조적 분석
SS&M:
- safety critical
- long validation
- 10년+ contract duration
- high fixed costs
- geographically fragmented metal plants
- underpriced programs

따라서 turnaround가 수분기 안에 끝날 수 없다고 봄.

### 결과
2020 Long writer retrospective:
**2019-05-09 → 2020-03-11 Short 약 +23%**

target $5는 실패.

---

## 14. 왜 2019 Short가 이전 Long보다 정보의 질이 높았나

이전 Long:
**margin gap → opportunity**

2019 Short:
**margin gap → contract/plant structure의 결과**

Long:
**mid-single-digit SS&M margin 가능**

Short:
**loss contracts가 expire/reprice 되기까지 시간이 물리적으로 오래 걸림**

즉:
**management intention보다 contract duration을 봄.**

---

# PART E — ADNT 2020 Long: Short가 맞았는데 왜 다시 Long인가

## 15. 2020 Long의 핵심은 “문제가 없어졌다”가 아니다

writer는 2019 Short가 맞았다고 인정.

그 뒤 새 evidence:

### Launch
- launch costs 감소
- containment costs 감소
- premium freight **-85%**

### Commercial
- 5+ customers renegotiated
- **$700m+ negative-return business** 교체

### COVID
- volume -20%대에도 survival
- June -25% sales에서 near-flat EBITDA
- liquidity >$1.2bn

### Portfolio
- YFAI stake sale
- fabrics sale
- debt reduction

즉:
**same problems, better evidence of resolution.**

---

## 16. 2020 Long valuation

assumptions:
- revenue ~$16.5bn
- core EBITDA margin 8.5%
- EBITDA ~$1.4bn
- China equity income ~$280m
- normalized EPS low-$8
- 9x discounted multiple

fair value:
**$75**

entry implied:
~$18~19.

---

## 17. 실제 outcome

Macrotrends:
- 2020 close **$34.77**
- 2021 high **$52.93**
- 2021 close **$47.88**
- 2024 close **$17.23**
- 2025 close **$19.17**

### 판정
- tactical 12~18M Long: **강한 성공**
- 5Y $75 target: **실패**
- 5Y endpoint: **거의 flat**

### 핵심
**Turnaround success ≠ business quality transformation**

회사는 살아났지만 auto supplier multiple/FCF quality는 Lear-like rerating을 충분히 얻지 못했다.

---

# PART F — ADNT 2016→2020 전체 시계열

| 시점 | 방향 | 핵심 thesis | 결과 |
|---|---|---|---|
| 2016 | Long | spin discount / China / FCF | 초기 성공 |
| 2017 | Long | margin gap closure | 강한 실패 |
| 2018 | Long | SS&M temporary | 매우 강한 실패 |
| 2019 | Short | FCF mismatch / long bad contracts | tactical 성공 |
| 2020 | Long | turnaround evidence / survival | intermediate 성공, 5Y 실패 |

### 분석의 질 변화
**valuation gap  
→ margin target  
→ operational detail  
→ contract-level failure mechanics  
→ observed turnaround evidence**

---

# PART G — Cross-Case Lessons

## 18. ADES와 ADNT의 공통점

둘 다 한동안 **“수학상 매우 싸다”**는 아이디어였다.

### ADES
cash distributions 계산은 맞음.
문제:
**누가 그 현금을 어떻게 배분하는가**

### ADNT
normalized margin 계산은 매력적.
문제:
**그 margin을 만드는 operational path가 현실적인가**

즉 valuation formula보다 더 중요한 것은:
**value realization mechanism**.

---

## 19. 이번 batch의 가장 중요한 구분

### Asset value
“이 자산은 얼마인가?”

### Realization path
“누가, 언제, 어떤 방식으로 그 가치를 주주에게 넘기는가?”

### Operational bridge
“현재 실적에서 정상 실적까지 구체적으로 무엇이 바뀌어야 하는가?”

ADES는 첫 번째를 잘 맞히고 두 번째가 계속 문제였다.

ADNT는 첫 번째 valuation보다 세 번째 operational bridge가 문제였다.

---

## 20. Batch 058 재사용 체크리스트 20개

1. raw direction을 원문으로 감사한다.
2. 외부 source body가 사라졌으면 reconstruction이라고 표시한다.
3. refined-coal/tax-credit는 finite-life DCF로 본다.
4. cash distribution과 public holdco burn을 분리한다.
5. net cash는 distributable cash인지 확인한다.
6. strategic review가 반드시 sale로 끝난다고 가정하지 않는다.
7. optional patents/IP는 base case에서 뺀다.
8. capital return의 실행가격을 기록한다.
9. risk-event removal과 rerating magnitude를 분리한다.
10. spin technical discount와 business-quality discount를 분리한다.
11. peer margin gap의 원인을 구조적으로 설명한다.
12. SG&A savings와 manufacturing turnaround를 별도 phase로 본다.
13. launch-heavy 사업은 premium freight / scrap / line stoppage를 본다.
14. known problem도 duration risk를 별도 계산한다.
15. normalized EPS는 loss-contract runoff schedule을 포함한다.
16. adjusted earnings와 cumulative FCF를 비교한다.
17. safety-critical component contract는 redesign speed가 느리다.
18. turnaround success를 survival / margin recovery / peer convergence로 나눈다.
19. 5년 target은 5년 endpoint로 판정한다.
20. asset sales/deleveraging은 ongoing earnings power와 분리한다.

---

## 21. Batch 058 핵심 한 줄

> **싸다는 계산보다 중요한 것은 ‘왜 지금의 낮은 실적이 정상화될 수 있는가’와 ‘정상화된 가치가 어떤 경로로 주주에게 도달하는가’다. ADES는 현금흐름을 맞히고도 자본배분이 변수였고, Adient는 margin target보다 손실계약과 생산복잡성이 훨씬 오래 지속됐다.**

---

## 22. 앱 / DB 반영

- Wrapper: `analysis/batch_058_ades_adnt_10.md`
- Overlay: `data/curated/batch_058_ades_adnt_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
