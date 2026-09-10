# Batch 051 — Genworth MI Canada / Macquarie Infrastructure / Madison Square Garden — V9 Index

> Research as-of 2026-09-10. 첨부 SQL의 원문·catalyst를 감사했다. **10 idea = 10 canonical reports**이며 없는 성과는 만들지 않았다.

## 0. 배치 결론

2009 `MIC`는 캐나다 mortgage insurer, 2010~2021 `MIC`는 미국 infrastructure holding company다. Macquarie는 2010~14 `자회사 FCF→debt paydown→cash unlock→배당→yield rerating`, 2017 `yield trap`, 2019~21 `asset sale→after-tax distribution`으로 프레임이 바뀐다. MSG는 2015·2020 분할로 media·sports·entertainment 세 증권이 된 SOTP 실험이다.

## 1. Idea Units

| # | 날짜 | 실제 회사 | raw→연구 방향 | 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2009-12-29 | Genworth MI Canada Inc. (현 Sagen MI Canada Inc.) | Short→**Long** | 장기 강한 성공 — C$48.86 control transaction | [캐나다 mortgage-insurance 구조·20%+ 자본복리 Long](ideas/2009/2009-12-29_MIC_genworth_canada_long.md) |
| 2 | 2010-06-03 | Macquarie Infrastructure Company LLC | Short→**Long** | 강한 성공 방향 — cash upstream·배당 정상화 | [ring-fenced debt·Atlantic cash-unlock·$28 Long](ideas/2010/2010-06-03_MIC_long.md) |
| 3 | 2012-03-28 | Macquarie Infrastructure Company LLC | Short→**Long** | 성공 — cash upstream과 배당개시 | [IMTT 분쟁·Atlantic lock-up 해제의 $50 Long](ideas/2012/2012-03-28_MIC_long.md) |
| 4 | 2014-01-13 | Macquarie Infrastructure Company LLC | Short→**Long** | 성공 — dividend growth·IMTT control rerating | [$3.75+ 배당·IMTT capex 정상화의 $70 Long](ideas/2014/2014-01-13_MIC_long.md) |
| 5 | 2017-10-04 | Macquarie Infrastructure Corporation | Short→**Long** | 강한 실패 — IMTT utilization shock·dividend cut | [7.6% yield·10% FCF growth의 $95 Long](ideas/2017/2017-10-04_MIC_long.md) |
| 6 | 2019-11-01 | Macquarie Infrastructure Corporation | Short→**Long** | 강한 성공 — 전 자산 매각·분배, clock 지연 | [$52~66 strategic-alternatives Long](ideas/2019/2019-11-01_MIC_strategic_alternatives_long.md) |
| 7 | 2021-04-16 | Macquarie Infrastructure Corporation / MIC LLC | Long→**Long** | 매우 성공 — 52일 내 $4.475bn deal·$37.386817 분배 | [Atlantic 6개월·tax-efficient liquidation Long](ideas/2021/2021-04-16_MIC_liquidation_long.md) |
| 8 | 2010-03-11 | The Madison Square Garden Company | Long→**Long** | 강한 SOTP 성공 — 2015·2020 분할 | [RSN cash+teams·Garden free option Long](ideas/2010/2010-03-11_MSG_long.md) |
| 9 | 2010-06-22 | The Madison Square Garden Company | Long→**Long** | 강한 성공 — core cash·분할 적중, LeBron 불필요 | [$30m RSN EBITDA·$23/$46 Long](ideas/2010/2010-06-22_MSG_long.md) |
| 10 | 2010-12-22 | The Madison Square Garden Company | Short→**Long** | 성공 방향 — FCF·SOTP 적중, 23% IRR 미검증 | [<10x pro-forma FCF·$37 Long](ideas/2010/2010-12-22_MSG_long.md) |

## 2. Entity / Direction Audit

10건 모두 실제 Long이다. raw Short 7건과 2009 MIC entity를 교정했다. 2019·2021 MIC는 asset-sale/liquidation distribution claim이며 MSG 성과는 2015 3:1·2020 1:1 successor shares를 이어야 한다.

## 3. 투자논지 누적 교정

Genworth는 housing 예측보다 recourse·은행 underwriting·capital이 핵심이었다. Macquarie는 자회사 FCF의 위치가 holdco dividend를 결정했고 2017 yield trap 이후 net sale proceeds로 전환해 성공했다. MSG는 RSN FCF를 downside, teams·venue를 option으로 둔 뒤 실제 분할로 검증됐다.

## 4. 공통 교훈

1. Ticker보다 법인·날짜가 먼저다.
2. 자회사 FCF와 holdco cash는 다르다.
3. 높은 yield는 cut 확률일 수 있다.
4. 실패한 compounder도 liquidation으로 다시 살 수 있다.
5. sale EV에서 debt·tax·fees를 뺀다.
6. SOTP의 최강 촉매는 실제 분할이다.
7. optional catalyst 실패에도 base가 살아야 한다.
8. 사건 성공과 exact return을 분리한다.

## 5. 산출물

- Payload: `data/curated/batch_051_mic_msg_deep_v7.json`
- Wrapper: `analysis/batch_051_mic_msg_10.md`
- Source packet: `data/curated/batch_051_source_packet.json`
- Builder: `scripts/51_build_batch_051_v9.py`
