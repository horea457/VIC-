# Batch 064 — AEP / Atlas / AEP Industries / Aeroplan / AerCap V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-18. 법인·거래소·통화·증권·방향을 먼저 고정하고 성과와 corporate action을 검증했다.

## Canonical idea files

| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2003-08-27 | AEP | Long | Long | [American Electric Power Company](ideas/2003/2003-08-27_AEP_american_electric_power_long.md) | 강한 성공 — regulatory cash·asset sales·EPS와 목표가격이 대체로 실현 |
| 2 | 2012-06-11 | AEP | Short | Long | [Anglo-Eastern Plantations Plc / AEP Plantations Plc](ideas/2012/2012-06-11_AEP_anglo_eastern_plantations_long.md) | 장기 성공 — 생산기반·순현금·순자산 compounding, SQL 성과행은 폐기 |
| 3 | 2020-01-28 | AEP.V | Long | Long | [Atlas Engineered Products Ltd.](ideas/2020/2020-01-28_AEP_atlas_engineered_products_long.md) | 지연 성공 — C$1 target는 달성, 2022 C$100m revenue는 38% 미달 |
| 4 | 2022-05-30 | AEP.V | Short | Long | [Atlas Engineered Products Ltd.](ideas/2022/2022-05-30_AEP_atlas_engineered_products_long.md) | 지연 성공 — C$1.50 price hit, C$17m EBIT annualization은 실패 |
| 5 | 2008-03-20 | AEPI | Long | Long | [AEP Industries Inc.](ideas/2008/2008-03-20_AEPI_long.md) | 장기 강한 성공 — 12개월 timing 혼합, 2017 $110 strategic value 검증 |
| 6 | 2009-10-12 | AEPI | Long | Long | [AEP Industries Inc.](ideas/2009/2009-10-12_AEPI_long.md) | 장기 성공 — Atlantis economics 적중, 1~2년 target timing 과도 |
| 7 | 2011-07-12 | AEPI | Long | Long | [AEP Industries Inc.](ideas/2011/2011-07-12_AEPI_long.md) | 강한 성공 — unit margin·buyback·strategic exit가 주당가치 검증 |
| 8 | 2014-07-09 | AEPI | Long | Long | [AEP Industries Inc.](ideas/2014/2014-07-09_AEPI_long.md) | 강한 성공 — stand-alone EPS는 거래로 미검증, $110 strategic value는 검증 |
| 9 | 2011-09-15 | AER CN | Long | Long | [Groupe Aeroplan Inc. / Aimia Inc.](ideas/2011/2011-09-15_AER_groupe_aeroplan_long.md) | 혼합 — 현금엔진은 유효, C$24 실패·anchor-partner tail 현실화 |
| 10 | 2014-01-27 | AER | Long | Long | [AerCap Holdings N.V.](ideas/2014/2014-01-27_AER_aercap_long.md) | 사업·EPS 성공 / 주가·multiple timing 실패 |

## Entity / direction / performance audit

- **AEP 2012:** American Electric Power가 아니라 LSE Anglo-Eastern Plantations(현재 AEP Plantations) Long이다. raw Short와 NYSE AEP 가격행은 보존하되 성과행은 폐기했다.
- **Atlas 2022:** raw Short지만 원문은 TSX-V:AEP common Long이다.
- **AER 2011:** NYSE AerCap이 아니라 Canadian Groupe Aeroplan/Aimia다. AerCap 가격행은 폐기했다.
- **AER 2014:** 실제 NYSE AerCap이며 SQL price-only ratios를 제한적으로 유지했다.
- **AEPI 네 건:** 같은 회사의 서로 다른 date-specific thesis다. 2017 merger consideration은 $110 cash 또는 2.5011 BERY shares, aggregate 50/50 proration이다.

## 핵심 판정

1. American Electric Power는 regulatory cash recovery·asset sale·EPS·$37 target가 대체로 맞은 강한 성공이다.
2. AEP Plantations는 EV/ha·tree-age thesis가 장기 net cash/NAV compounding으로 검증됐지만 SQL return은 wrong entity다.
3. Atlas 2020은 C$100m revenue가 38.1% 미달했고, Atlas 2022는 C$17m EBIT이 26.3% 미달했다. 두 price target는 뒤늦게 달성했다.
4. AEPI는 spread·buyback·distressed M&A·consolidation이 맞았으나 초기 단기 target와 2017 takeout을 섞지 않았다.
5. Aeroplan은 loyalty FCF를 맞혔지만 anchor-partner risk를 과소평가했고 C$24 target는 실패했다.
6. AerCap은 2016 EPS $5.50 예상 대비 $5.52로 적중했지만 2년 price-only -18.4%로 multiple thesis는 실패했다.

## 구조화 데이터

- `data/curated/batch_064_aep_atlas_aepi_aer_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 상세 timeline·sources.
- `data/curated/batch_064_source_catalog.json`: raw metadata·방향·ticker-collision 감사 source packet. 앱에는 직접 로드하지 않는다.
- `analysis/batch_064_aep_atlas_aepi_aer_10.md`: Streamlit wrapper.

## Batch 043 대비 보강점

- 각 아이디어를 같은 0–12장 구조로 통일했다.
- claim마다 T0 근거·숨은 가정·사전 반증조건·actual·정량 gap·오류·교훈을 기록했다.
- 회사/SEC 1차자료 URL과 각 자료가 검증하는 수치를 sources table에 남겼다.
- wrong-company return, corporate-action proration, delayed target와 operating forecast를 분리했다.
