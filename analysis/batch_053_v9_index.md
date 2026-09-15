# Batch 053 — New England Realty / Owens Corning / Office Depot — V9 Index

> Research as-of 2026-09-10. Batch 052 다음 10건이다. **10 idea = 10 canonical reports**이며 현재 첨부 SQL에 없는 성과값은 모두 null 처리했다.

## 0. 배치 결론

이 배치는 같은 기업이라도 `법적 재편`, `cycle earnings`, `entry expectation`을 분리해야 한다는 사례다. NEN 2019는 NAV 할인 자체보다 rent reset과 discount buyback의 주당가치 복리이고, OC 7건은 2007 post-reorg timing 실패에서 2018 expectation reset까지 normalized earnings의 질이 어떻게 달라지는지를 보여준다. ODP는 2000 SOTP tactical Long과 2007 turnaround extrapolation 실패를 대비한다.

## 1. Idea Units

| # | 날짜 | 실제 회사 | raw→연구 방향 | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2019-01-15 | New England Realty Associates Limited Partnership | Long→**Long** | 사업·자본배분 방향 성공, 200%/정확 수익률 미검증 | [replacement-cost discount·rent reset·buyback compounder Long](ideas/2019/2019-01-15_NEN_long.md) |
| 2 | 2007-01-31 | Owens Corning | Long→**Long** | 재편 성공, housing-cycle timing 실패·정확 수익률 미검증 | [post-asbestos 재편·fresh-start discount Long](ideas/2007/2007-01-31_OC_long.md) |
| 3 | 2007-12-26 | Owens Corning | Long→**Long** | 심한 경로손실 뒤 정상화 방향 성공·정확 수익률 미검증 | [segment 정상마진·3.7x normalized EBITDA Long](ideas/2007/2007-12-26_OC_long.md) |
| 4 | 2013-03-14 | Owens Corning | Long→**Long** | 사업논지 강한 성공, 단기 target·정확 수익률 미검증 | [Roofing discipline·Insulation 흑자전환·$60 base Long](ideas/2013/2013-03-14_OC_long.md) |
| 5 | 2015-01-06 | Owens Corning | Short→**Long** | earnings 인과 일부만 적중·방향 성공, 정확 수익률 미검증 | [asphalt deflation·Roofing spread surprise Long](ideas/2015/2015-01-06_OC_long.md) |
| 6 | 2015-04-07 | Owens Corning | Long→**Long Update** | channel 방향·earnings 성공, realized-price 가정 부분 실패·정확 수익률 미검증 | [Roofing channel-check·asphalt flux Long update](ideas/2015/2015-04-07_OC_long_update.md) |
| 7 | 2017-05-12 | Owens Corning | Long→**Long** | 2017 사업·FCF 성공 뒤 peak-expectation 노출, 정확 수익률 미검증 | [three-segment normalization·10% FCF yield Long](ideas/2017/2017-05-12_OC_long.md) |
| 8 | 2018-12-12 | Owens Corning | Long→**Long** | earnings-resilience·expectation-reset 성공 방향, 정확 수익률 미검증 | [48% drawdown·8.5x normalized EPS Long](ideas/2018/2018-12-12_OC_long.md) |
| 9 | 2000-07-28 | Office Depot, Inc. | Short→**Long** | 사업회복·SOTP 방향 성공, 정확 수익률 미검증 | [BSG+International SOTP·Retail free-option Long](ideas/2000/2000-07-28_ODP_long.md) |
| 10 | 2007-03-22 | Office Depot, Inc. | Short→**Long** | 매출·margin·투자·buyback 핵심 실패, 정확 수익률 미검증 | [Odland turnaround 2단계·margin expansion Long](ideas/2007/2007-03-22_ODP_long.md) |

## 2. SQL / Direction / Security Audit

첨부 `VIC_IDEAS(4).sql`에는 `catalyst·companies·descriptions` COPY만 있고 `ideas·performance` data COPY는 없다. Batch 053의 catalyst는 10건 모두 있으나 description은 OC 2007-12 한 건(13,193자)뿐이다. 기존 overlay의 성과비율 8건은 provenance가 없어 모두 폐기했다. date·author·raw flag·source link는 prior curated metadata로 남기되 현재 attachment보다 낮은 등급으로 표시했다.

방향은 실제 payoff로 재감사했다. OC 2015-01은 2015-04 후속 글이 직접 Long thesis라고 명시하고, ODP 2000·2007은 purchase·상승 target을 제시하므로 raw Short→실제 Long이다. NEN 2019는 2012 split 이후 **Depositary Receipt=1/30 Class A Unit**이고 나머지는 common이다.

## 3. NEN — NAV discount보다 주당가치 복리

약 $53의 10~11% FCF yield, replacement cost/NAV 할인은 출발점이다. 장기 payoff는 `under-market rent reset→NOI 증가→NAV 아래 buyback→receipt당 ownership 증가`다. 반증은 cap-rate 하나가 아니라 occupancy·same-unit NOI·mortgage reset·repurchase 실행이다. 200%/10년 total return은 현 데이터로 미검증이다.

## 4. Owens Corning — 같은 company, 다른 expectation

| 시점 | 무엇을 샀나 | 핵심 오류/edge | 판정 |
|---|---|---|---|
| 2007-01 | asbestos 제거·fresh start | legal clean-up을 cycle bottom과 혼동 | timing 실패 |
| 2007-12 | $20.60·3.7x normalized EBITDA | segment margin을 재구축·GFC path 과소평가 | 장기 방향 성공 |
| 2013 | Roofing cash+Insulation 흑자전환 | dollar EBIT bridge | 사업 성공 |
| 2015-01/04 | asphalt deflation | cost 적중, flat selling price 실패 | causal 부분 성공 |
| 2017 | 세 segment 동시 정상화·10% FCF | 좋은 실적이 peak expectation일 수 있음 | 기간 사업 성공 |
| 2018-12 | 48% drawdown·8.5x normal EPS | 악재가 보인 뒤 낮아진 기대 | 강한 방향 성공 |

## 5. Office Depot — tactical SOTP와 turnaround 2단계

2000 Long은 BSG $1.0bn+International $1.3bn이 $1.9bn 시총을 설명하고 Retail $1.0bn을 option으로 둔 SOTP였다. 2001 International/Viking local-currency growth가 이를 지지했다. 2007 Long은 이미 달성한 cost-cutting margin을 150 신규매장·remodel·salesforce 투자와 buyback 뒤에도 외삽했다. 2008 Retail 영업이익 $354.5m→-$29.2m, BSD $220.1m→$119.8m으로 denominator가 붕괴했다.

## 6. 공통 투자 교훈

1. post-reorg legal clean-up은 earnings-cycle bottom이 아니다.
2. normalized multiple은 segment volume·price·utilization에서 다시 만든다.
3. 결과가 좋아도 price·cost·volume claim을 각각 사후검증한다.
4. channel check와 price letter는 realized invoice가 아니다.
5. 모든 segment 동시호전은 upside이자 peak-expectation 경고다.
6. cyclical FCF yield는 다음 downturn의 운전자본·capex로 stress한다.
7. SOTP에는 shared cost·lease·tax·working capital을 완전 배분한다.
8. turnaround 2단계는 과거 cost cut이 아니라 incremental investment ROIC다.
9. buyback은 downturn liquidity 이후에만 accretive하다.
10. performance COPY가 없으면 exact return은 null이다.

## 7. 산출물

- Payload: `data/curated/batch_053_nen_oc_odp_deep_v7.json`
- Wrapper: `analysis/batch_053_nen_oc_odp_10.md`
- Source packet: `data/curated/batch_053_source_packet.json`
- Builder: `scripts/53_build_batch_053_v9.py`
