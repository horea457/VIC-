# Batch 067 — AEZS / AF / AFC / AFCE V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. 아이디어 1건 = canonical Markdown 1개다.
> Research as-of 2026-09-18. ticker보다 date+legal entity+security를 우선하고 exact return은 cash ledger가 있을 때만 계산했다.

## Canonical idea files

| # | 날짜 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2016-07-25 | AEZS | Long | Long | [Aeterna Zentaris Inc.](ideas/2016/2016-07-25_AEZS_long.md) | 혼합 — Zoptrex 실패, Macrilen 승인·license 성공 |
| 2 | 2004-01-09 | AF | Short | Long | [Astoria Financial Corporation](ideas/2004/2004-01-09_AF_astoria_long.md) | 실패 — additive EPS bridge 과대 |
| 3 | 2006-09-18 | AF | Short | Short | [Astoria Financial Corporation](ideas/2006/2006-09-18_AF_astoria_short.md) | 성공 — NIM·NII·EPS 압박 적중 |
| 4 | 2009-11-08 | AF | Long | Long | [AlarmForce Industries Inc.](ideas/2009/2009-11-08_AF_alarmforce_long.md) | 부분 성공 — recurring franchise 성공, growth 과대 |
| 5 | 2014-03-10 | AF | Short | Long | [AlarmForce Industries Inc.](ideas/2014/2014-03-10_AF_alarmforce_long.md) | 성공 — C$10.70→C$16 takeout |
| 6 | 2002-10-04 | AFC | Short | Long | [Allmerica Financial Corporation](ideas/2002/2002-10-04_AFC_allmerica_long.md) | 매우 강한 성공 — life uncertainty 해소·P&C rerating |
| 7 | 2008-12-29 | AFC | Long | Long | [Allied Capital Corporation](ideas/2008/2008-12-29_AFC_allied_capital_2047_notes_long.md) | 매우 강한 성공 — Ares assumption 후 par redemption |
| 8 | 2004-06-24 | AFCE | Long | Long | [AFC Enterprises Inc.](ideas/2004/2004-06-24_AFCE_long.md) | 강한 성공 — divestitures와 $12 special dividend |
| 9 | 2007-12-05 | AFCE | Short | Long | [AFC Enterprises Inc.](ideas/2007/2007-12-05_AFCE_long.md) | 지연 성공 — mechanism 적중, 2009 horizon 실패 |
| 10 | 2011-03-25 | AFCE | Short | Long | [AFC Enterprises Inc.](ideas/2011/2011-03-25_AFCE_long.md) | 매우 강한 성공 — EPS compounding·$79 takeout |

## Entity / direction / security audit

- AF 2004·2006은 Astoria Financial, AF 2009·2014는 AlarmForce Industries다.
- AFC 2002는 Allmerica Financial common, AFC 2008은 Allied Capital 6.875% senior unsecured notes due 2047이다.
- raw Short→실제 Long 교정은 Astoria 2004, AlarmForce 2014, Allmerica 2002, AFCE 2007·2011의 5건이다.
- Allied note는 $25 par의 35~36 cents, 즉 약 $8.75~9.00 entry다. common price와 섞지 않는다.

## 핵심 비교

1. AEZS는 Zoptrex가 실패했지만 Macrilen이 trial headline miss 뒤 FDA 승인·license에 성공했다. clinical·regulatory·commercial outcome을 분리한다.
2. Astoria 2004 Long은 refinancing benefit을 선형 합산해 EPS를 과대평가했고, 2006 Short는 asset/liability repricing mismatch를 정확히 잡았다.
3. AlarmForce 2009는 subscriber growth를 과대평가했지만 recurring franchise는 남았고, 2014는 운영개선보다 BCE의 strategic takeout이 payoff를 만들었다.
4. Allmerica는 negative life stub 제거로 P&C 가치가 드러났고, Allied note는 security priority와 Ares debt assumption이 par recovery를 만들었다.
5. AFCE는 2004 asset sale·special dividend, 2007 지연 turnaround, 2011 장기 compounding·$79 takeout으로 thesis stage가 진화했다.

## 구조화 데이터

- `data/curated/batch_067_aezs_af_afc_afce_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.
- `data/curated/batch_067_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.
- `analysis/batch_067_aezs_af_afc_afce_10.md`: Streamlit wrapper.
