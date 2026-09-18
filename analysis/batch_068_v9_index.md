# Batch 068 — AFCE / AFFY / AF Gruppen / Atlas Financial / AFH Financial / Armstrong Flooring V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-18. raw direction, legal entity, exact security와 payoff를 먼저 고정하고 1차자료로 actual을 검증했다.

## Canonical idea files

| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2012-04-20 | AFCE | Short | Long | [AFC Enterprises Inc.](ideas/2012/2012-04-20_AFCE_long.md) | 매우 강한 성공 — 운영 추정 상회·2017 $79 cash |
| 2 | 2016-08-30 | AFFY | Short | Long | [Affymax Inc.](ideas/2016/2016-08-30_AFFY_long.md) | 실패 — value-unlocking transaction 장기 미실현 |
| 3 | 2021-10-11 | AFG NO | Long | Long | [AF Gruppen ASA](ideas/2021/2021-10-11_AFG_NO_long.md) | 부분 실패 — balance sheet·backlog 성공, 성장·margin 경로 미달 |
| 4 | 2012-06-05 | AFH | Long | Long | [Atlas Financial Holdings Inc.](ideas/2012/2012-06-05_AFH_long.md) | 강한 단기 성공 — premium·underwriting·book growth |
| 5 | 2013-09-22 | AFH | Long | Long | [Atlas Financial Holdings Inc.](ideas/2013/2013-09-22_AFH_long.md) | 부분 성공 — 가격·premium 강함, 2015 EPS/BV target 과대 |
| 6 | 2021-12-29 | AFHBL | Long | Long | [Atlas Financial Holdings Inc.](ideas/2021/2021-12-29_AFHBL_notes_long.md) | 교환 성공·최종 recovery 미확정 — 2024 credit deterioration |
| 7 | 2021-04-12 | AFHIF | Short | Long | [Atlas Financial Holdings Inc.](ideas/2021/2021-04-12_AFHIF_long.md) | 강한 실패 — secured debt가 common residual을 압도 |
| 8 | 2020-12-13 | AFHP LN | Long | Long | [AFH Financial Group Plc](ideas/2020/2020-12-13_AFHP_LN_long.md) | 강한 성공 — 330p→480p cash scheme |
| 9 | 2016-09-21 | AFI | Long | Long | [Armstrong Flooring Inc.](ideas/2016/2016-09-21_AFI_long.md) | 강한 실패 — EBITDA normalization 붕괴·2022 Chapter 11 |
| 10 | 2021-08-25 | AFI | Long | Long | [Armstrong Flooring Inc.](ideas/2021/2021-08-25_AFI_long.md) | 매우 강한 실패 — 약 8.5개월 내 Chapter 11 |

## Direction / security / return audit

- AFCE 2012, AFFY 2016, AFHIF 2021의 raw Short를 원문 payoff 기준 실제 Long으로 교정했다.
- AFHBL은 common이 아니라 $25 par의 6.625% senior unsecured notes due 2022다. 2022 exchange 뒤 6.625% cash/7.25% PIK notes due 2027이 됐다.
- Atlas 2012 entry $1.77는 2013 1-for-3 reverse split 뒤 $5.31 equivalent다.
- source SQL performance row가 10건 모두 없으므로 exact return을 생성하지 않았다. cash consideration, reported high, operating actual과 bankruptcy waterfall만 제한적으로 사용했다.

## 핵심 판정

1. AFCE는 FY2012 EPS·SSS·net openings가 모두 적중했고 2017 $79 cash deal로 장기 brand value도 실현됐다.
2. AFFY는 큰 NOL face value에도 profitable taxable income과 거래가 없으면 가치가 없다는 negative case다.
3. AF Gruppen은 backlog·cash·balance sheet는 강했지만 2024 revenue·margin path를 놓쳤다. quality와 valuation success를 분리했다.
4. Atlas 2012·2013 common은 초기 premium·book rerating이 성공했으나 2016 reserve strengthening이 growth의 tail을 드러냈다.
5. Atlas 2021 common과 AFHBL notes는 같은 issuer라도 payoff가 다르다. common은 2024 core-asset transfer로 실패했고 note recovery는 2027까지 미확정이다.
6. AFH Financial은 480p cash scheme으로 빠르게 성공했다. Armstrong 두 Long은 liquidity runway가 operating repair보다 짧아 Chapter 11로 끝났다.

## 구조화 데이터

- `data/curated/batch_068_afce_affy_afg_afh_afhp_afi_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.
- `data/curated/batch_068_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.
- `analysis/batch_068_afce_affy_afg_afh_afhp_afi_10.md`: Streamlit wrapper.
