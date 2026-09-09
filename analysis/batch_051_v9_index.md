# Batch 051 — Genworth MI Canada / Macquarie Infrastructure / Madison Square Garden V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-09.
> **Batch boundary:** Batch 050 마지막 MHK 2021-12-23 이후 SQL-derived queue 10건.

## Canonical Idea Units

| # | 날짜 | Raw ticker | 실제 entity | Raw 방향 | 실제 방향 / Security | Canonical | 판정 |
|---:|---|---|---|---|---|---|---|
| 1 | 2009-12-29 | MIC | **Genworth MI Canada** | Short | **Long** | [Genworth MI Canada](ideas/2009/2009-12-29_MIC_genworth_canada_long.md) | 장기 강한 성공 |
| 2 | 2010-06-03 | MIC | Macquarie Infrastructure | Short | **Long** | [MIC 2010](ideas/2010/2010-06-03_MIC_long.md) | crisis recovery 강한 성공 |
| 3 | 2012-03-28 | MIC | Macquarie Infrastructure | Short | **Long** | [MIC 2012](ideas/2012/2012-03-28_MIC_long.md) | cash unlock / FCF 성공 |
| 4 | 2014-01-13 | MIC | Macquarie Infrastructure | Short | **Long** | [MIC 2014](ideas/2014/2014-01-13_MIC_long.md) | dividend rerating 성공 |
| 5 | 2017-10-04 | MIC | Macquarie Infrastructure | Short | **Long** | [MIC 2017](ideas/2017/2017-10-04_MIC_long.md) | dividend cut로 강한 실패 |
| 6 | 2019-11-01 | MIC | Macquarie Infrastructure | Short | **Strategic Alternatives Long** | [MIC 2019](ideas/2019/2019-11-01_MIC_strategic_alternatives_long.md) | asset-sale thesis 강한 성공 |
| 7 | 2021-04-16 | MIC | Macquarie Infrastructure | Long | **Liquidation Long** | [MIC 2021](ideas/2021/2021-04-16_MIC_liquidation_long.md) | catalyst timing까지 매우 성공 |
| 8 | 2010-03-11 | MSG | Madison Square Garden | Long | Long | [MSG 2010 Mar](ideas/2010/2010-03-11_MSG_long.md) | SOTP / spin 강한 성공 방향 |
| 9 | 2010-06-22 | MSG | Madison Square Garden | Long | Long | [MSG 2010 Jun](ideas/2010/2010-06-22_MSG_long.md) | RSN hidden value 성공 |
| 10 | 2010-12-22 | MSG | Madison Square Garden | Short | **Long** | [MSG 2010 Dec](ideas/2010/2010-12-22_MSG_long.md) | FCF + SOTP 성공 방향 |

## Direction / Entity Audit

이번 batch는 raw metadata 오류가 특히 크다.

- **10건 모두 실제 Long**
- raw SQL이 Short로 잘못 표시한 건: 7건
- 첫 번째 MIC는 Macquarie가 아니라 **Genworth MI Canada**
- 따라서 ticker와 is_short만으로 분석하면 기업 identity와 투자방향을 동시에 틀릴 수 있다.

## Genworth MI Canada — 국가별 구조를 분리한 보험 Long

2009 글은 미국 mortgage insurance의 부실 이미지를 캐나다에 그대로 적용하면 안 된다고 봤다.

핵심 차이:
- borrower recourse
- bank-originated underwriting
- 상대적으로 보수적인 mortgage structure
- 제한된 경쟁구조
- 높은 ROE와 excess capital

2019 Genworth의 지분은 Brookfield에 **C$48.86/share**로 매각됐다. headline industry risk보다 contract structure를 본 것이 맞았다.

## Macquarie Infrastructure — 같은 회사, 세 개의 투자공식

### 2010~2014: Recovery / Dividend Growth
분석식:
**subsidiary FCF → debt paydown → cash lock-up 해제 → parent dividend → yield rerating**

이 구간은 강하게 성공했다.

### 2017: Yield Trap
원문은 약 7.6% dividend yield와 9% FCF yield를 floor로 봤다.

하지만 IMTT utilization이 급락하고 2018 quarterly dividend가 $1.44에서 $1.00으로 감소했다.

교훈:
**Dividend yield is not a floor when the dividend itself is variable.**

### 2019~2021: Liquidation
기존 recurring FCF model을 버리고 다음 식으로 바꿨다.

**Equity proceeds = asset sale values - debt - tax - transaction/manager fees**

실제:
- 2020 IMTT sale $2.67bn → $11/share special dividend
- 2021 Atlantic Aviation sale $4.475bn → $37.386817/unit distribution
- Hawaii asset sale process 지속

2017 실패 후 2019/2021 성공은 **같은 기업을 고집해서가 아니라 valuation framework를 바꿨기 때문**이다.

## Madison Square Garden — SOTP가 실제 증권으로 분리된 사례

2010 세 Long은 공통적으로:
- MSG Networks / RSN cash flow
- Knicks·Rangers trophy-franchise value
- Madison Square Garden venue value
를 분리했다.

실제 corporate actions:
- 2015: media(MSG Networks) vs sports/entertainment 분리
- 2020: sports(MSG Sports) vs entertainment(MSG Entertainment) 분리

즉 원래 SOTP의 valuation buckets가 후에 **실제 separate public securities**가 됐다.

정확한 total return은 distributed shares를 모두 포함해야 하며 단순 MSG ticker chart를 쓰면 안 된다.

## Batch 051 상위 교훈

1. **Ticker identity audit은 필수** — 같은 MIC라도 Genworth MI Canada와 Macquarie는 전혀 다른 기업이다.
2. 보험업은 국가별 mortgage contract와 recourse structure를 본다.
3. infrastructure holding은 consolidated EBITDA보다 cash upstreamability를 본다.
4. high dividend yield는 payout source가 흔들리면 floor가 아니라 trap이 된다.
5. 과거 FCF/share CAGR을 기계적으로 외삽하지 않는다.
6. 실패한 compounder가 좋은 liquidation stock으로 바뀔 수 있다.
7. strategic alternatives는 gross sale value가 아니라 debt·tax·fees 후 shareholder proceeds로 계산한다.
8. liquidation return은 price chart가 아니라 distribution calendar로 계산한다.
9. SOTP는 실제 spin/separation route가 있을 때 강해진다.
10. multiple spin이 있는 주식은 distributed securities를 모두 합산해 total return을 계산한다.

## 앱 / DB 반영

- Wrapper: analysis/batch_051_mic_msg_10.md
- Overlay: data/curated/batch_051_mic_msg_deep_v7.json
- Canonical source of truth: 위 10개 idea Markdown.
