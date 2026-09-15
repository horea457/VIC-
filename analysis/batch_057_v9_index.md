# Batch 057 — Weight Watchers / Asbury / ADA-ES — V9 Index

> Research as-of 2026-09-15. 10 idea = 10 canonical reports다. 현재 SQL에는 catalyst 10건과 description 3건만 있고 performance COPY는 없다. 실제 방향은 Long 9건과 capital-structure Pair 1건이다.

## 0. 배치 결론

이 배치의 공통점은 회사 이름이 아니라 **어떤 현금흐름을 어느 security로 소유하는가**가 결과를 갈랐다는 점이다. WTW B-1 loan은 같은 회사 common보다 먼저 cash를 받았고, ABG의 공포는 vehicle revenue보다 P&S/F&I와 관찰된 stress evidence로 판단해야 했으며, ADES의 refined-coal cash는 만기와 governance를 가진 계약 claim이었다.

## 1. Idea Units

| # | 날짜 | Ticker | raw→연구 방향 | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2015-05-05 | WTW | Short→**Pair** | B-1 성공·common Short 실패·pair 혼합/실패·exact return 미검증 | [common Short·B-1 first-lien loan Long pair](ideas/2015/2015-05-05_WTW_capital_structure_pair.md) |
| 2 | 2015-11-10 | WTW | Short→**Long** | 2016 target 실패·2017~18 사업논지 지연 성공·exact return 미검증 | [Oprah subscriber acquisition·fixed-cost leverage Long](ideas/2015/2015-11-10_WTW_long.md) |
| 3 | 2018-12-11 | WTW | Short→**Long** | 10개월 horizon 실패·retention/digital 논지 일부 성공 | [digital retention·customer-life extension Long](ideas/2018/2018-12-11_WTW_long.md) |
| 4 | 2008-04-24 | ABG | Short→**Long** | SAAR floor·단기 path 실패·장기 사업회복 | [P&S/F&I 방어력·14m SAAR recession Long](ideas/2008/2008-04-24_ABG_long.md) |
| 5 | 2010-03-12 | ABG | Short→**Long** | 사업·정상화 논지 강한 성공·exact return 미검증 | [관찰된 trough cost reset·$2.03 EPS Long](ideas/2010/2010-03-12_ABG_long.md) |
| 6 | 2020-02-18 | ABG | Short→**Long** | 극단적 COVID path 후 사업논지 성공·exact return 미검증 | [P&S resilience·Park Place accretion Long](ideas/2020/2020-02-18_ABG_long.md) |
| 7 | 2020-09-10 | ABG | Short→**Long** | 운영·valuation thesis 강한 성공·exact return 미검증 | [COVID stress-test 통과 후 8.5x EPS Long](ideas/2020/2020-09-10_ABG_long.md) |
| 8 | 2021-09-16 | ABG | Short→**Long** | scale execution 부분 성공·$20bn/$360 target 미달 | [$20bn scale·Clicklane·real estate rerating Long](ideas/2021/2021-09-16_ABG_long.md) |
| 9 | 2022-09-26 | ABG | Long→**Long** | durability 확인·revenue target 미달·장기 horizon 진행 중 | [dealer terminal-value fear·normalized FCF Long](ideas/2022/2022-09-26_ABG_long.md) |
| 10 | 2012-07-15 | ADES | Long→**Long** | 현금분배 논지 성공·governance/security path 혼합 | [Section 45 refined-coal distribution·MATS SOTP Long](ideas/2012/2012-07-15_ADES_long.md) |

## 2. SQL·Direction·Security·Performance Audit

첨부 `VIC_IDEAS(4).sql`의 COPY table은 catalyst·companies·descriptions뿐이다. catalyst 10건은 모두 확인했고 description은 WTW 2015-05 32,273자, WTW 2015-11 11,268자, ABG 2010 13,914자만 있다. raw Short→Long 단순 direction correction은 7건이다. WTW 2015-05는 단순 correction이 아니라 common Short+B-1 Long의 Pair/security correction이다. ABG 2022와 ADES는 raw Long이 맞다.

현재 attachment가 controls다. legacy overlay의 performance_available 9건을 모두 nullified했고, 그중 ABG numeric series 6건과 WTW ticker-reuse contamination flag 3건을 폐기했다. 따라서 정확한 1/3/5년 return, pair return과 IRR은 모두 null이다.

## 3. Weight Watchers — operating view보다 security map

2015-05 pair는 $301m cash+$50m revolver와 짧은 maturity를 근거로 B-1을 정확히 골랐지만, 그 상환가능성을 높이는 rescue가 common도 살릴 수 있다는 cross-catalyst를 놓쳤다. 2015-11 Long은 Oprah×subscriber operating leverage를 맞혔으나 YE2016 clock이 빨랐다. 2018 Long은 retention을 맞혔어도 gross additions·marketing miss가 revenue와 주가를 결정했다.

## 4. Asbury — 예측한 floor보다 관찰된 stress

2008 Long은 P&S/F&I 구조를 맞히고도 14m SAAR floor를 틀렸다. 2010 Long은 실제 10m대 SAAR에서 흑자로 돌아온 cost base를 관찰해 훨씬 강했다. 2020-02는 같은 economics를 사면서 COVID path를 겪었고, 2020-09는 stress가 이미 통과된 뒤 8.5x에 사 정보의 질이 가장 좋았다. 2021은 scale과 rerating을 겹쳐 target이 과했고, 2022는 terminal fear와 normalized FCF에 집중해 더 견고했지만 5~10년 horizon은 진행 중이다.

## 5. ADA-ES — cash entitlement와 상장 wrapper

Section 45 tonnage와 Tinuum distributions는 실재했고 2019 회사 발표상 distributions $73.9m, royalties $16.9m까지 확대됐다. 하지만 2011~14 material misstatement·internal-control failure와 filing 지연은 좋은 세제 economics를 나쁜 security path로 바꿀 수 있음을 보여줬다. 2021-12-31 만료가 정해진 asset은 terminal multiple보다 distribution calendar로 평가해야 한다.

## 6. 투자논지 재사용 규칙

1. 자본구조마다 maturity·priority·catalyst를 별도 claim으로 쓴다.
2. pair trade는 각 leg뿐 아니라 두 leg를 동시에 움직이는 rescue catalyst를 stress한다.
3. subscriber는 gross additions와 churn/retention을 분리한다.
4. macro floor를 예측하기보다 실제 stress에서 비용·liquidity 반응을 관찰한다.
5. dealer revenue가 아니라 P&S·F&I·SG&A와 owner FCF를 본다.
6. M&A revenue와 per-share FCF accretion을 구분한다.
7. 세제 cash claim은 eligibility·contract·JV·expiry·parent distribution 순으로 추적한다.
8. NPV와 상장 wrapper의 accounting/governance discount를 분리한다.
9. corporate event와 operating success는 exact return이 아니다.
10. performance table이 없으면 수익률은 null이다.

## 7. 산출물

- Payload: `data/curated/batch_057_wtw_abg_ades_deep_v7.json`
- Wrapper: `analysis/batch_057_wtw_abg_ades_10.md`
- Source packet: `data/curated/batch_057_source_packet.json`
- SQL inventory: `data/curated/batch_057_sql_inventory.json`
- Builder: `scripts/57_build_batch_057_v9.py`

## 8. 검증 기준

각 보고서는 0~12절, 6 weighted claims/100%, 5 metrics, 최소 6 timeline events와 원문 provenance+공식자료를 포함한다. Payload·문서·앱 popup의 idea_id, entity, direction, security와 verdict를 동일하게 유지한다.
