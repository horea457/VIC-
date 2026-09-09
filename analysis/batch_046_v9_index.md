# Batch 046 — Anthem / Athabasca Oil / Athene / CIT — V9 Index

> **Research as-of:** 2026-09-09. 첨부 `VIC_IDEAS(4).sql`의 원문을 기준으로 entity와 direction을 수동 교정했다. SQL performance row가 없는 10건의 수익률은 만들지 않았다.

## 0. 배치 결론

이번 배치는 데이터 정규화가 투자분석보다 먼저라는 대표 사례다. 원 ticker `ATH`는 2002 Anthem, 2011/2013 Athabasca Oil, 2017~2020 Athene Holding의 세 법인을 뜻한다. raw Short 9건 중 실제 Short는 2017 Athene 한 건뿐이며, 나머지는 원문 payoff가 모두 Long이다.

## 1. Idea Units

| # | 날짜 | 실제 회사 | raw→연구 방향 | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2001-01-16 | CIT Group Inc. | Short→**Long** | 두 달 내 Tyco takeout으로 강한 성공 | [5.7x normal EPS와 takeout asymmetry Long](ideas/2001/2001-01-16_CIT_long.md) |
| 2 | 2002-01-18 | Anthem, Inc. | Long→**Long** | 사업·전략 종착점 성공, SQL 가격성과는 미검증 | [demutualization 이후 margin·multiple 동시 정상화 Long](ideas/2002/2002-01-18_ANTHEM_long.md) |
| 3 | 2007-08-23 | CIT Group Inc. | Short→**Long** | wholesale funding collapse와 2009 bankruptcy로 대실패 | [1x book·6.5x earnings와 liquidity buffer Long](ideas/2007/2007-08-23_CIT_long.md) |
| 4 | 2008-05-02 | CIT Group Inc. | Short→**Long** | 단기 liquidity 판단·sale catalyst 실패, bankruptcy로 terminal 대실패 | [0.58x adjusted TBV와 $15~18 sale catalyst Long](ideas/2008/2008-05-02_CIT_long.md) |
| 5 | 2011-08-22 | Athabasca Oil Sands Corp. | Short→**Long** | put 가치 실현, long-duration NAV·equity rerating은 혼합 | [PetroChina put과 world-scale acreage의 비대칭 Long](ideas/2011/2011-08-22_ATHABASCA_OIL_long.md) |
| 6 | 2013-12-26 | Athabasca Oil Corp. | Short→**Long** | 핵심 put catalyst 성공, C$10~15 NAV의 지속성은 oil shock로 실패 | [C$1.32bn Dover put의 binary overhang 해소 Long](ideas/2013/2013-12-26_ATHABASCA_OIL_long.md) |
| 7 | 2017-05-02 | Athene Holding Ltd. | Short→**Short** | $33 target은 미달; 일부 de-rating 뒤 Long counter-pitch가 반증 | [1.6x book에 성장·Apollo 구조위험을 판 Athene Short](ideas/2017/2017-05-02_ATHENE_short.md) |
| 8 | 2018-09-09 | Athene Holding Ltd. | Short→**Long** | 1~2년 price path 실패, 합병까지 보유하면 business/terminal thesis 회복 | [1.1x book·7x earnings에서 2017 Short를 뒤집은 Long](ideas/2018/2018-09-09_ATHENE_long.md) |
| 9 | 2019-03-31 | Athene Holding Ltd. | Short→**Long** | $64 target과 strategic value가 합병 경로에서 실현된 성공 | [5x earnings·0.8x book에서 20% IRR을 산 Long](ideas/2019/2019-03-31_ATHENE_long.md) |
| 10 | 2020-09-09 | Athene Holding Ltd. | Short→**Long** | Apollo 합병으로 매우 성공한 event-plus-compounder Long | [0.7x book·5.2x earnings와 crisis deployment Long](ideas/2020/2020-09-09_ATHENE_long.md) |

## 2. 기업별 투자논지

### Anthem — margin과 network scale

2002 Long은 14x EPS와 4% 미만 margin에서 peer 수준 16x·5%로의 이중 정상화를 샀다. MLR·pricing·통합위험이 있었지만 2004 WellPoint 결합으로 전국 Blue 네트워크의 전략가치는 확인됐다.

### Athabasca — 계약상 cash와 개발 NAV를 분리

2011·2013 두 Long 모두 PetroChina put이 hard catalyst였다. put 현금화는 성공했지만 gross resource NAV는 capex·기술·승인·oil price·시간을 거쳐야 했다. 계약상 현금 성공을 C$20~22 또는 C$10~15의 지속적 equity value 성공으로 바꾸면 안 된다.

### Athene — 가격에 따라 Short에서 Long으로

2017 Short는 1.6x book premium의 압축을 맞혔으나 $33·40% downside는 실패했다. 2018 Long은 1~2년 path에서 손실, 2019·2020 Long은 5x earnings·0.8/0.7x book에서 capital survival과 Apollo 합병을 포착해 성공했다. 같은 business risk도 entry multiple과 capital buffer가 direction을 바꾼다.

### CIT — 자산가치보다 liability clock

2001 Long은 $20+에서 takeout accretion을 계산했고 두 달 뒤 Tyco 거래로 성공했다. 2007·2008 Long은 book·normalized EPS와 gross liquidity를 믿었지만 wholesale funding run을 놓쳐 2009 bankruptcy와 old common cancellation로 실패했다.

## 3. 배치 공통 교훈

1. **Ticker는 entity가 아니다.** 법인·exchange·날짜·business description으로 먼저 resolve한다.
2. **Direction은 raw flag가 아니라 payoff다.** target 상승·현금수취·rerating이면 Long이다.
3. **Cash/NAV/book는 common floor가 아니다.** timing, capex, funding, senior claims와 use-of-cash를 차감한다.
4. **Event 성공과 투자 성공을 분리한다.** put·합병·인수가 일어나도 exact return은 별도다.
5. **Funding은 lender P/E보다 앞선다.** gross lines가 아니라 가용성·담보·만기별 sources/uses를 본다.
6. **성과값이 없으면 null이다.** terminal event를 임의의 1/3/5년 수익률로 바꾸지 않는다.

## 4. 데이터·앱 산출물

- DB payload: `data/curated/batch_046_anthem_athabasca_athene_cit_deep_v7.json`
- Streamlit wrapper: `analysis/batch_046_anthem_athabasca_athene_cit_10.md`
- SQL source packet: `data/curated/batch_046_source_packet.json`
- Builder: `scripts/46_build_batch_046_v9.py`

## 5. 검증 기준

10개 보고서 모두 0~12절, 6개 claim/100% weight, 5개 metric, 최소 6개 event와 원문+공식자료 source를 포함한다. Payload·문서·앱 popup의 entity, direction, verdict를 동일하게 유지한다.
