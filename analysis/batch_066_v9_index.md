# Batch 066 — Aetna / AETC / Aether / Ampex / ADDvantage / AudioEye V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. 아이디어 1건 = canonical Markdown 1개다.
> Research as-of 2026-09-18. 방향·법인·증권·horizon과 terminal corporate action을 먼저 고정했다.

## Canonical idea files

| # | 날짜 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2000-06-02 | AET | Short | Long | [Aetna Inc.](ideas/2000/2000-06-02_AET_long.md) | 거래 촉매 성공 / $134 SOTP는 미검증·과도 |
| 2 | 2006-12-22 | AET | Long | Long | [Aetna Inc.](ideas/2006/2006-12-22_AET_long.md) | EPS 성공 / multiple·$65 target 실패 |
| 3 | 2009-01-16 | AET | Short | Long | [Aetna Inc.](ideas/2009/2009-01-16_AET_long.md) | near-term earnings 실패 / $44는 2011로 지연 |
| 4 | 2001-06-12 | AETC | Short | Long | [Applied Extrusion Technologies](ideas/2001/2001-06-12_AETC_long.md) | refinancing 성공 / earnings·common terminal 실패 |
| 5 | 2001-04-29 | AETH Corp | Long | Long | [Aether Systems](ideas/2001/2001-04-29_AETH_convert_long.md) | 강한 성공 — security selection과 par redemption |
| 6 | 2005-02-01 | AEXCA | Long | Long | [Ampex Corporation](ideas/2005/2005-02-01_AEXCA_long.md) | 강한 실패 — royalty를 common annuity로 오인 |
| 7 | 2010-09-02 | AEY | Long | Long | [ADDvantage Technologies Group](ideas/2010/2010-09-02_AEY_long.md) | tactical rerating 일부 성공 / durable thesis terminal 실패 |
| 8 | 2013-01-18 | AEY | Long | Long | [ADDvantage Technologies Group](ideas/2013/2013-01-18_AEY_long.md) | 부분 rerating / $4~5 미달 / 장기 floor 붕괴 |
| 9 | 2018-03-21 | AEY | Long | Long | [ADDvantage Technologies Group](ideas/2018/2018-03-21_AEY_long.md) | tactical peak 성공 / TBV convergence·durability 실패 |
| 10 | 2020-08-17 | AEYE | Long | Long | [AudioEye, Inc.](ideas/2020/2020-08-17_AEYE_long.md) | 초기 성장·가격 강한 성공 / 3~4년 매출 forecast 미달 |

## Entity / direction / security audit

- Aetna 2000·2009는 raw Short지만 원문은 breakup/crisis Long이다.
- Aether는 common이 아니라 6% convertible subordinated notes due 2005다. conversion보다 cash coverage·101.2% redemption이 payoff를 만들었다.
- AETC·Ampex의 기존 common은 각각 재편에서 취소됐다. refinancing·IP asset의 존재를 common recovery와 혼동하지 않는다.
- AEY 세 vintage는 같은 법인이지만 entry asset base·catalyst·horizon이 다른 date-specific ideas다.

## 핵심 비교

1. Aetna 2000은 signed breakup consideration이 실현됐지만 $134 bull SOTP를 거래성공으로 소급하지 않는다.
2. Aetna 2006은 EPS $3.83 대비 $3.93로 적중했어도 17x multiple과 $65 target는 실패했다.
3. Aetna 2009는 낮은 P/E의 E가 31.8% 무너졌다. 2011 target hit는 near-term thesis를 구제하지 않는다.
4. AETC는 refinancing이 성공해도 FY2002 EPS -$2.55와 common cancellation을 막지 못했다.
5. Aether convert는 issuer common보다 priority·maturity가 나은 security selection의 성공이다.
6. Ampex의 royalty는 debt·legacy burn 뒤 common까지 도달하지 않았고 CPR은 별도 claim이다.
7. AEY의 NCAV/TBV는 tactical rerating을 만들었지만 청산계획 없는 working-capital book는 2024 Chapter 7까지 녹았다.
8. AudioEye는 초기 MRR·GM·price catalyst가 맞았지만 FY2023 revenue는 $50m 예상보다 37.4% 낮았다.

## 구조화 데이터

- data/curated/batch_066_aetna_aetc_aether_ampex_aey_aeye_deep_v7.json: 10 postmortems, 60 claims, 50 metrics, 80 timeline events와 sources.
- data/curated/batch_066_source_catalog.json: raw metadata source packet이며 production glob에는 포함되지 않는다.
- analysis/batch_066_aetna_aetc_aether_ampex_aey_aeye_10.md: Streamlit wrapper.
