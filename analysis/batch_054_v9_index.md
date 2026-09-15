# Batch 054 — Office Depot / Boca Resorts / Rosetta Stone — V9 Index

> Research as-of 2026-09-10. Batch 053 다음 10건이다. **10 idea = 10 canonical reports**이며 현재 첨부 SQL에 없는 description·성과값을 만들지 않았다.

## 0. 배치 결론

ODP 5건은 같은 declining retailer에서 `prior-margin forecasting→merger cost-out→services transformation→remaining-assets SOTP→bid 뒤 asset separation`으로 논지의 질이 어떻게 바뀌는지 보여준다. 2002 `RST`는 Rosetta Stone이 아니라 Boca Resorts이며 trophy asset sale로 성공했다. Rosetta Stone 4건은 CAC Short의 성공, cash/EV-Sales Long의 실패, 잘못된 FCF annualization, 그리고 Lexia라는 distinct asset proof의 성공을 비교한다.

## 1. Idea Units

| # | 날짜 | Raw ticker | 실제 회사 | raw→연구 방향 | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|---|
| 1 | 2007-12-27 | ODP | Office Depot, Inc. | Short→**Long** | 정상매출·margin·buyback 핵심 실패, 정확 수익률 미검증 | [70% drawdown·5% normalized margin Long](ideas/2007/2007-12-27_ODP_long.md) |
| 2 | 2014-04-05 | ODP | Office Depot, Inc. | Short→**Long** | self-help·target 성공, 최종 Staples 거래는 antitrust 실패·정확 수익률 미검증 | [OfficeMax cost-out·capacity shrink·$7.25 Long](ideas/2014/2014-04-05_ODP_long.md) |
| 3 | 2018-08-13 | ODP | Office Depot, Inc. | Short→**Long** | CompuCom transformation 실패·legacy value 일부 잔존, 정확 수익률 미검증 | [B2B/services transformation·high-teens FCF yield Long](ideas/2018/2018-08-13_ODP_long.md) |
| 4 | 2019-04-22 | ODP | Office Depot, Inc. | Short→**Long** | asset separation·salvage 방향 성공, full value·정확 수익률 미검증 | [B2B SOTP·23~25% FCFE yield·failed-M&A salvage Long](ideas/2019/2019-04-22_ODP_long.md) |
| 5 | 2021-01-19 | ODP | The ODP Corporation | Short→**Long** | CompuCom salvage 정확·asset actions 부분 성공, $80 완전실현 미검증 | [$40 bid 뒤 $80 asset-separation SOTP Long](ideas/2021/2021-01-19_ODP_long.md) |
| 6 | 2002-04-07 | RST | Boca Resorts, Inc. | Long→**Long** | $24 cash takeout로 asset·sale 논지 강한 성공, exact return은 null | [trophy-resort scarcity·$20.29 private-value Long](ideas/2002/2002-04-07_RST_boca_resorts_long.md) |
| 7 | 2010-01-04 | RST | Rosetta Stone Inc. | Short→**Short** | profitability 붕괴·$12 downside 방향 강한 성공, exact return은 null | [unit saturation·CAC inflation·AOV illusion Short](ideas/2010/2010-01-04_RST_short.md) |
| 8 | 2011-08-23 | RST | Rosetta Stone Inc. | Short→**Long** | SaaS 매출만 성장·consolidated economics와 $40 실패, exact return은 null | [0.55x EV/Sales·net cash·SaaS transition Long](ideas/2011/2011-08-23_RST_long.md) |
| 9 | 2013-03-25 | RST | Rosetta Stone Inc. | Short→**Long** | 2013 FCF forecast 강한 실패·Lexia capital allocation은 별도 성공, exact return은 null | [$7 cash·16% FCF yield·SaaS reset Long](ideas/2013/2013-03-25_RST_long.md) |
| 10 | 2018-09-08 | RST | Rosetta Stone Inc. | Short→**Long** | Lexia 성장과 $30 cash sale로 강한 성공, exact return은 null | [Lexia alone covers EV·$22~35 SOTP Long](ideas/2018/2018-09-08_RST_long.md) |

## 2. SQL / Entity / Direction Audit

첨부 `VIC_IDEAS(4).sql`에는 `catalyst·companies·descriptions` COPY만 있고 `ideas·performance` data COPY는 없다. Batch 054의 catalyst는 10건 모두 확인됐지만 description은 **0건**이다. date·author·raw flag·원문 수치는 prior curated metadata로 낮은 provenance를 명시하고, 실제 결과는 SEC·FTC filings로 검증했다. exact return/IRR은 모두 null이다.

raw direction 오류는 8건이다. ODP 5건은 모두 상승 target/payoff의 Long이고, RST 2011·2013·2018도 Long이다. Rosetta Stone 2010만 raw Short=실제 Short다. 2002 ticker RST는 CIK·business·VIC link상 **Boca Resorts, Inc.**이며 Rosetta Stone mapping을 교정했다.

## 3. Office Depot — forecasting에서 asset proof로

| 시점 | 논지 | 핵심 검증 | 판정 |
|---|---|---|---|
| 2007-12 | 5% normalized margin | 2008 Retail $354.5m→-$29.2m | 실패 |
| 2014 | OfficeMax cost-out·capacity shrink | synergy $700m+·Staples $11 value | self-help 성공/FTC 실패 |
| 2018 | CompuCom services transformation | $1bn acquisition→최대 $305m sale | 실패 |
| 2019 | B2B SOTP·failed-M&A salvage | $40 proposal·B2B plan·CompuCom sale | 방향 성공 |
| 2021 | $40 bid 뒤 $80 four-leg SOTP | $300m salvage 정확·spin 취소 | 부분 성공 |

가장 중요한 진화는 `회사의 미래 margin 예측`에서 `실패해도 남는 자산과 실제 buyer price`로 이동한 것이다. decline company의 강한 thesis는 transformation이 아니라 downside asset proof에서 나왔다.

## 4. Boca Resorts — ticker 충돌과 private value

2002 RST는 Rosetta Stone이 아니다. Boca Resorts는 약 $12.85에서 tangible book $11.67, normalized cash $110m, $20.29 private value였고 2004 Blackstone affiliate가 $24 cash 계약을 제시했다. trophy location·control owner·unencumbered sale route가 depressed hotel earnings보다 중요했다. 다만 event anchor를 exact total return으로 바꾸지 않았다.

## 5. Rosetta Stone — unit economics가 narrative를 이긴다

| 시점 | 무엇을 봤나 | 결과 |
|---|---|---|
| 2010 Short | unit saturation·CAC +20~35%·AOV illusion | profitability collapse 적중 |
| 2011 Long | 0.55x sales·$115m cash·SaaS/TAM | revenue/margin forecast 실패 |
| 2013 Long | 4Q cash annualization·$35m FCF | actual -$0.9m, 실패 |
| 2018 Long | Lexia $60m bookings·good asset>EV | $30 Cambium sale, 성공 |

CAC·cohort economics를 본 2010 Short가 brand·cash·EV/Sales를 본 2011 Long보다 강했다. 2018에는 Lexia가 standalone buyer value를 가진 distinct asset이 되어 이전의 추상적 SaaS narrative와 달라졌다.

## 6. 공통 투자 교훈

1. ticker는 날짜별 entity·CIK로 resolve한다.
2. 주가 drawdown과 valuation safety margin은 다르다.
3. declining industry에서는 demand보다 cost/capacity 감소속도를 비교한다.
4. merger synergy와 antitrust completion probability를 분리한다.
5. transformation M&A는 revenue mix가 아니라 incremental ROIC로 본다.
6. failed acquisition은 sunk cost가 아니라 현재 third-party salvage로 평가한다.
7. EV/Sales·gross margin·cash는 나쁜 CAC를 막는 floor가 아니다.
8. seasonal Q4 FCF를 annualize하지 않는다.
9. good asset>EV는 corporate drag·tax·sale probability 후 검증한다.
10. corporate event와 filing price는 performance row가 아니므로 exact return은 null이다.

## 7. 산출물

- Payload: `data/curated/batch_054_odp_rst_deep_v7.json`
- Wrapper: `analysis/batch_054_odp_rst_10.md`
- Source packet: `data/curated/batch_054_source_packet.json`
- Builder: `scripts/54_build_batch_054_v9.py`
