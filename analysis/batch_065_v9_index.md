# Batch 065 — AerCap / Aerie Pharmaceuticals / Aeroméxico / AES V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. 아이디어 1건 = canonical Markdown 1개다.
> Research as-of 2026-09-18. 같은 회사도 entry date·price·risk state·horizon별로 분리했다.

## Canonical idea files

| # | 날짜 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2015-12-28 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2015/2015-12-28_AER_long.md) | 사업·BVPS 예측 성공 / 3년 stock thesis 실패 |
| 2 | 2017-07-14 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2017/2017-07-14_AER_long.md) | 메커니즘 성공 / COVID 포함 가격경로 혼합 |
| 3 | 2018-06-21 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2018/2018-06-21_AER_long.md) | 2020 horizon 실패 / franchise resilience 후행 확인 |
| 4 | 2019-02-06 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2019/2019-02-06_AER_long.md) | 강한 process 성공 / volatile price path |
| 5 | 2020-08-17 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2020/2020-08-17_AER_long.md) | 매우 강한 성공 — crisis implied loss 과도 |
| 6 | 2022-02-05 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2022/2022-02-05_AER_long.md) | 1Y 실패 / 장기 mechanism 회복 |
| 7 | 2016-02-11 | AERI | Short | Short | [Aerie Pharmaceuticals](ideas/2016/2016-02-11_AERI_short.md) | fundamental 일부 적중 / terminal Short 실패 |
| 8 | 2017-11-01 | Aeromex | Long | Long | [Grupo Aeroméxico](ideas/2017/2017-11-01_Aeromex_long.md) | 강한 실패 — Chapter 11 old equity near-wipeout |
| 9 | 2009-10-15 | AES | Long | Long | [The AES Corporation](ideas/2009/2009-10-15_AES_long.md) | 실패 — project-to-parent EPS bridge 미달 |
| 10 | 2020-09-18 | AES | Short | Long | [The AES Corporation](ideas/2020/2020-09-18_AES_long.md) | 강한 성공 — measurable catalysts 실현 |

## Entity / direction / duplicate audit

- AerCap 6건은 기존 Batch 010 중복 구조화 행을 제거하고 Batch 065를 정본으로 승격했다.
- AerCap 2014는 Batch 064에 남긴다. ILFC closing 전 thesis로 별도 idea unit이다.
- AERI는 실제 Short이며 terminal $15.25 cash consideration을 payoff anchor로 사용했다.
- Aeroméxico는 legacy common과 reorganized company를 분리하고 old equity <0.01% treatment를 우선했다.
- AES 2020은 raw Short지만 원문은 $32 target의 명백한 Long이다.

## 핵심 비교

1. AerCap 2015·2017은 book compounding을 맞혔어도 persistent discount와 COVID path 때문에 stock outcome이 약했다.
2. 2018 vintage는 contracted rent를 cash certainty로 과대평가해 2020 horizon이 실패했다.
3. 2019 vintage는 sources/uses와 covenant를 먼저 봐 extreme stress에서도 process가 유효했다.
4. 2020 vintage는 0.4x book가 요구한 impairment가 과도해 빠른 성공이었다.
5. 2022 vintage는 legal title과 physical recovery를 혼동해 Russia tail에 맞았고, 2023 회복은 delayed outcome이다.
6. AERI는 TAM을 맞히고도 M&A로 Short가 실패했고, Aeroméxico는 franchise가 살아도 old common은 사라졌다.
7. AES 2009는 MW→EPS bridge가 실패했지만 2020은 observable catalyst stack로 성공했다.

## 구조화 데이터

- data/curated/batch_065_aer_aeri_aeromex_aes_deep_v7.json: 10 postmortems, 60 claims, 50 metrics, 상세 timeline·sources.
- data/curated/batch_065_source_catalog.json: raw metadata source packet이며 production glob에는 포함되지 않는다.
- analysis/batch_065_aer_aeri_aeromex_aes_10.md: Streamlit wrapper.
