# Batch 071 — AGC / American General / Springleaf / AGCO / Argentex / Agrify / Alliance / Alamos V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-19. 회사 identity·증권·방향·corporate action을 먼저 교정하고 official filings로 actual을 검증했다.

## Canonical idea files

| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2016-01-17 | AGC | Short | Long | [Advent Claymore Convertible Securities and Income Fund II](ideas/2016/2016-01-17_AGC_closed_end_fund_long.md) | 강한 성공 — 할인 축소·tender·NAV merger 실현 |
| 2 | 2009-01-22 | AGC1 | Short | Long | [American General Finance Corporation](ideas/2009/2009-01-22_AGC1_american_general_finance_bonds_long.md) | 강한 성공 — issuer survival·strategic sale·refinancing |
| 3 | 2012-11-22 | AGC1 | Long | Long | [Springleaf Finance Corporation](ideas/2012/2012-11-22_AGC1_springleaf_6_90_2017_notes_long.md) | 매우 강한 성공 — exchange·repurchase·maturity 해결 |
| 4 | 2015-10-16 | AGCO | Long | Long | [AGCO Corporation](ideas/2015/2015-10-16_AGCO_long.md) | 강한 주가 성공 / 10% margin bull case 실패 |
| 5 | 2021-11-06 | AGFX | Long | Long | [Argentex Group Plc](ideas/2021/2021-11-06_AGFX_argentex_long.md) | 매우 강한 실패 — liquidity tail이 -97% terminal loss |
| 6 | 2021-05-28 | AGFY | Long | Long | [Agrify Corporation](ideas/2021/2021-05-28_AGFY_long.md) | 매우 강한 실패 — negative gross economics·cash burn·희석 |
| 7 | 2022-02-21 | AGFY | Long | Long | [Agrify Corporation](ideas/2022/2022-02-21_AGFY_long.md) | 매우 강한 실패 — negative gross economics·cash burn·희석 |
| 8 | 2000-08-29 | AGI | Short | Long | [Alliance Gaming Corporation](ideas/2000/2000-08-29_AGI_alliance_gaming_long.md) | 장기 매우 강한 성공 — Bally로 성장 후 $83.30 cash sale |
| 9 | 2014-03-31 | AGI | Long | Long | [Alamos Gold Inc.](ideas/2014/2014-03-31_AGI_alamos_gold_long.md) | 실패 — permit·production·horizon 미실현 |
| 10 | 2018-11-18 | AGI. | Long | Long | [Alamos Gold Inc.](ideas/2018/2018-11-18_AGI_alamos_gold_long.md) | 매우 강한 성공 — operational fix·reserve growth·target 초과 |

## Metadata / security / return audit

- AGC 2016, AGC1 2009, AGI 2000의 raw Short를 실제 Long으로 교정했다.
- AGC1 2009·2012는 common이 아니라 senior unsecured debt다.
- 2000 AGI는 Alamos Gold가 아니라 Alliance Gaming이며 2006 Bally Technologies로 사명이 바뀌었다.
- AGCO 2015·Alamos 2014만 source-DB performance row를 보존했다. 나머지는 complete ledger 없이 exact IRR을 만들지 않았다.
- Agrify는 2022·2023·2024 reverse splits가 누적 1-for-3,000이고 중간 dilution도 있어 nominal price comparison을 폐기했다.

## 핵심 판정

1. AGC는 liquid NAV discount가 약 19%에서 8%로 좁혀지고 15% tender·NAV merger까지 이어진 강한 성공이다.
2. AGF/Springleaf 두 credit는 equity가 아니라 maturity·seniority·refinancing을 산 성공 사례다.
3. AGCO는 주가와 cycle call은 성공했지만 10% operating-margin bull case는 실패했다.
4. Argentex는 low-capex와 low-liquidity-risk를 혼동해 2.49p rescue offer로 끝난 실패다.
5. Agrify 두 vintage는 headline cash·backlog·software optionality가 negative gross economics를 구하지 못했다.
6. AGI ticker는 Alliance/Bally 장기 성공, Alamos 2014 실패, Alamos 2018 강한 성공이라는 서로 다른 entity·mechanism을 담는다.

## 구조화 데이터

- `data/curated/batch_071_agc_agc1_agco_agfx_agfy_agi_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.
- `data/curated/batch_071_source_catalog.json`: raw metadata source packet이며 production payload glob에는 포함되지 않는다.
- `analysis/batch_071_agc_agc1_agco_agfx_agfy_agi_10.md`: Streamlit wrapper.
