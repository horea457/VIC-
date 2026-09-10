# Batch 049 — Metals USA / Murphy USA / McDermott — V9 Index

> Research as-of 2026-09-10. 첨부 VIC_IDEAS(4).sql의 10개 catalyst와 5개 description을 확인하고, 원문 payoff·법인·security를 다시 감사했다. 성과값 5건만 실제 방향으로 교정했고 나머지는 null이다.

## 0. 배치 결론

동일 ticker MUSA는 2011 Metals USA와 2013 이후 Murphy USA라는 다른 법인이다. raw Short 8건 중 실제 Short는 Murphy USA 2017·2018·2020 세 건뿐이다. Metals USA 2011, Murphy USA 2013·2021, McDermott 2008·2012는 본문 payoff상 Long으로 교정했다. 이 배치의 중심 교훈은 volume decline과 profit-pool decline의 분리, buyback의 주당 복리, SOTP의 legal perimeter, backlog quantity와 margin quality의 분리다.

## 1. Idea Units

| # | 날짜 | 실제 회사/security | raw→연구 방향 | 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2011-09-26 | Metals USA Holdings Corp. (not Murphy USA) | Short→**Long** | 강한 성공 — 2013 Reliance $20.65 cash exit, 약 2.29x gross reference | [broken IPO·정상 EBITDA·FCF yield의 Metals USA Long](ideas/2011/2011-09-26_MUSA_metalsusa_long.md) |
| 2 | 2013-09-27 | Murphy USA Inc. | Short→**Long** | 강한 성공 — 1년 +33.9%, 3년 +80.5%, 5년 +113.8% price-only | [spin-off·Walmart adjacency·store growth와 buyback Long](ideas/2013/2013-09-27_MUSA_murphyusa_long.md) |
| 3 | 2017-07-14 | Murphy USA Inc. | Short→**Short** | 실패 — 1개월 +6.0% 후 1년 -9.2%, 5년 -265.9% simple short P&L | [same-store gallons·RIN·capex와 multiple compression Short](ideas/2017/2017-07-14_MUSA_short.md) |
| 4 | 2018-06-27 | Murphy USA Inc. | Short→**Short** | 실패 — 6개월 +6.5% 후 1년 -11.6%, 3년 -77.4% simple short P&L | [guidance cut·15 cpg·$350m EBITDA·6x multiple Short](ideas/2018/2018-06-27_MUSA_short.md) |
| 5 | 2020-01-02 | Murphy USA Inc. | Short→**Short** | 초기 trade 성공 / 중기 thesis 강한 실패 — 3개월 +27.1%, 3년 -143.2% simple Short | [dual melting ice cube·10~11x multiple·$85 Short](ideas/2020/2020-01-02_MUSA_short.md) |
| 6 | 2021-11-15 | Murphy USA Inc. | Short→**Long** | 강한 성공 — 6개월 +41.9%, 1년 +57.7% price-only | [structural CPG·QuickChek·20%+ IRR capex·buyback Long](ideas/2021/2021-11-15_MUSA_long.md) |
| 7 | 2003-02-06 | McDermott International, Inc. | Long→**Long** | 사업·SOTP 성공 / catalyst 심각한 지연 — exact return null | [asbestos ring-fence·J. Ray cleanup·BWXT SOTP Long](ideas/2003/2003-02-06_MDR_long.md) |
| 8 | 2004-06-07 | McDermott International, Inc. | Long→**Long** | SOTP 성공 / 2005~06 separation timing 실패 — exact return null | [BWXT alone covers market cap·J. Ray 무료·asbestos option Long](ideas/2004/2004-06-07_MDR_long.md) |
| 9 | 2008-12-12 | McDermott International, Inc. | Short→**Long** | 사업·catalyst 성공 방향 / exact return null | [crisis SOTP·net cash·government floor와 spin Long](ideas/2008/2008-12-12_MDR_long.md) |
| 10 | 2012-01-27 | McDermott International, Inc. | Short→**Long** | 실패 — backlog quality·cost-to-complete를 과소평가, exact return null | [isolated project miss·deepwater backlog·margin normalization Long](ideas/2012/2012-01-27_MDR_long.md) |

## 2. 기업별 lifecycle

### MUSA 2011 — Metals USA

약 $9 broken-IPO Long은 $170m 정상 EBITDA, 낮은 maintenance capex와 working-capital downside를 샀다. 2013 Reliance의 $20.65 cash acquisition으로 약 2.29x gross reference가 됐다. 이 결과는 Murphy USA와 연결하면 안 된다.

### MUSA 2013~2021 — Murphy USA

2013 spin Long은 unit growth·merchandise·capital allocation을 맞혔다. 2017·2018·2020 Short는 gallons·EV·tobacco headwind를 봤지만 fuel CPG, low-cost operator의 margin share, R&R/QuickChek과 buyback을 과소평가했다. 2020 Short는 COVID로 3개월 +27.1%를 벌 수 있었지만 fundamental thesis는 반대로 갔다. 2021 Long은 structural CPG와 owner earnings/share를 정확히 포착했다.

### MDR 2003~2012 — SOTP에서 pure-play EPCI까지

2003·2004 Long은 B&W asbestos ring-fence와 BWXT quality를 맞혔지만 2006 settlement, 2010 spin까지 duration을 과소평가했다. 2008 crisis Long은 government value와 spin을 포착했다. 반면 2012 pure-play Long은 산업수요와 backlog를 earnings visibility로 오인해 2013년말 9개 loss project를 놓쳤다.

## 3. 공통 투자교훈

1. **Ticker는 법인이 아니다.** 날짜·CIK·사업설명으로 MUSA entity를 먼저 resolve한다.
2. **Volume decline은 profit decline이 아니다.** gallons×CPG와 total fuel contribution dollars를 만든다.
3. **Buyback은 현금유출이자 분모 축소다.** 평균매입가·retired shares·leverage를 함께 본다.
4. **Working-capital release는 recurring FCF가 아니다.** downside liquidity와 earning power를 중복하지 않는다.
5. **Backlog는 margin exposure다.** EAC revision, change order, fixed-price 비중과 cash conversion을 먼저 본다.
6. **SOTP는 legal perimeter다.** ring-fence·guarantee·LC·tax·overhead 뒤 common residual만 더한다.
7. **Catalyst duration은 valuation 변수다.** event가 맞아도 6년 늦으면 원 IRR은 실패할 수 있다.
8. **성과가 없으면 null이다.** corporate outcome을 임의 1/3/5년 return으로 바꾸지 않는다.

## 4. 산출물

- Payload: data/curated/batch_049_musa_mdr_deep_v7.json
- Wrapper: analysis/batch_049_musa_mdr_10.md
- Source packet: data/curated/batch_049_source_packet.json
- Builder: scripts/49_build_batch_049_v9.py

## 5. 검증 기준

10개 독립 보고서 모두 0~12절, 6개 weighted claim/100%, 5개 metric, 최소 6개 timeline event, 원문과 공식자료 source를 포함한다. DB·index·popup의 entity, direction, verdict를 동일하게 유지한다.
