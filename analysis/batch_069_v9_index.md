# Batch 069 — AFMI / Alphamin / Ag Growth / AFOP / Aluflexpack / AFR / AfriSam / Affirm / AmTrust V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-18. 방향·증권·corporate action·payoff를 먼저 고정하고 1차자료로 actual을 검증했다.

## Canonical idea files

| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2008-06-04 | AFMI.OB | Long | Long | [Affinity Media Inc.](ideas/2008/2008-06-04_AFMI_OB_long.md) | downside thesis 성공 — deal 실패에도 $6 cash + residual |
| 2 | 2021-01-10 | AFMJF | Long | Long | [Alphamin Resources Corp.](ideas/2021/2021-01-10_AFMJF_long.md) | 매우 강한 성공 — 생산·Mpama South·배당 실현 |
| 3 | 2004-10-12 | AFN UN | Short | Long | [Ag Growth Income Fund](ideas/2004/2004-10-12_AFN_UN_long.md) | 강한 성공 — margin·distribution·bolt-ons 실현 |
| 4 | 2010-05-26 | AFOP | Long | Long | [Alliance Fiber Optic Products Inc.](ideas/2010/2010-05-26_AFOP_long.md) | 매우 강한 성공 — split-adjusted 5.48x takeout |
| 5 | 2012-08-07 | AFOP | Long | Long | [Alliance Fiber Optic Products Inc.](ideas/2012/2012-08-07_AFOP_long.md) | 매우 강한 성공 — 3.98x split-adjusted takeout + distributions |
| 6 | 2022-05-29 | AFP SW | Long | Long | [Aluflexpack AG](ideas/2022/2022-05-29_AFP_SW_long.md) | 운영 성공 / security outcome 혼합 — 2025 CHF16 takeout |
| 7 | 2003-12-11 | AFR | Short | Long | [American Financial Realty Trust](ideas/2003/2003-12-11_AFR_long.md) | 실패 — asset growth가 주당가치로 전환되지 않음 |
| 8 | 2010-11-01 | AFRISJ | Short | Long | [AfriSam Investment Holdings](ideas/2010/2010-11-01_AFRISJ_secured_frn_long.md) | 구조조정 성공 / holder-level IRR 미확정 |
| 9 | 2021-02-08 | AFRM | Short | Short | [Affirm Holdings Inc.](ideas/2021/2021-02-08_AFRM_short.md) | 매우 강한 성공 — $30 target 초과 하락 |
| 10 | 2010-01-13 | AFSI | Short | Short | [AmTrust Financial Services Inc.](ideas/2010/2010-01-13_AFSI_short.md) | 실패 — concerns 후행 적중, stock path 치명적 |

## Direction / security / return audit

- AFN.UN 2004, AFR 2003, AFRISJ 2010의 raw Short를 실제 Long으로 교정했다.
- AFRISJ는 common이 아니라 AfriSam senior secured floating-rate notes Long이다.
- AFOP 2010은 1-for-5 reverse split과 2-for-1 split을, AFOP 2012는 2-for-1 split을 반영했다. 2012 cash distribution은 별도 payoff다.
- source SQL performance row가 10건 모두 없어 verified operating actual·cash consideration·split-adjusted price comparison만 사용했다. complete ledger 없는 exact total return·IRR은 만들지 않았다.

## 핵심 판정

1. AFMI는 deal thesis는 실패했지만 $6 cash+residual share로 trust-floor thesis가 성공했다.
2. Alphamin은 FTR·deleveraging·Mpama South·배당이 순차적으로 실현된 강한 성공이다.
3. Ag Growth는 high-margin replacement niche와 distribution·bolt-on M&A가 작동했다.
4. AFOP 두 vintage는 net cash·profitability·strategic value가 Corning $18.50 cash deal로 crystallize됐다.
5. Aluflexpack은 운영 target에 접근했지만 CHF16 takeout의 투자수익은 entry ledger가 없어 혼합 판정이다.
6. AFR은 asset growth가 AFFO/share로 전환되지 않았고, AfriSam note는 restructuring이 성공했지만 holder-level IRR은 미확정이다.
7. Affirm short는 빠른 valuation reset으로 성공했지만 AmTrust short는 우려가 훗날 맞아도 2배 adverse path 때문에 실패했다.

## 구조화 데이터

- `data/curated/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.
- `data/curated/batch_069_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.
- `analysis/batch_069_afmi_afmjf_afn_afop_afp_afr_afrm_afsi_10.md`: Streamlit wrapper.
