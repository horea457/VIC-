# Batch 048 — KAR / Time Warner / Metals USA — V9 Index

> Research as-of 2026-09-10. 첨부 `VIC_IDEAS(4).sql`과 repository source metadata로 entity·direction·security를 감사했다. KAR 2건은 보존 price multiplier를 실제 Long 방향으로 교정했고, 나머지는 성과를 만들지 않았다.

## 0. 배치 결론

raw Short 9건 중 실제 Short는 TWX 2015-12 한 건뿐이다. KAR 2건은 recovery/digital Long, TWX는 LEAPS·stub·common·SOTP·Short·merger arb를 각각 독립 security로 나눴다. MUSA 2003은 Murphy USA가 아니라 Metals USA다. 이 배치의 핵심은 `좋은 기업가치 분석도 security duration이 틀리면 실패`, `산업 Short가 맞아도 M&A tail이면 손실`, `event probability와 duration은 별도`라는 점이다.

## 1. Idea Units

| # | 날짜 | 실제 security/entity | raw→연구 방향 | 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2020-06-03 | KAR Auction Services | Short→**Long** | 부분 성공 — survival·volume 회복은 적중, +40% rerating은 미달 | [preferred 자본·거래량 정상화·비용 reset Long](ideas/2020/2020-06-03_KAR_long.md) |
| 2 | 2021-07-23 | KAR Auction Services | Short→**Long** | 실패/경로변경 — digital 방향은 맞았지만 2024 forecast object가 소멸 | [digital wholesale marketplace·2024 SOTP Long](ideas/2021/2021-07-23_KAR_long.md) |
| 3 | 2006-01-31 | Time Warner Jan-2008 $15 calls | Short→**LEAPS Long** | 실패 — corporate 방향은 맞았지만 option clock이 먼저 만료 | [conglomerate unlock의 Jan-2008 LEAPS Long](ideas/2006/2006-01-31_TWX_leaps_long.md) |
| 4 | 2009-02-15 | Time Warner post-TWC content stub | Short→**Stub Long** | 강한 성공 — TWC·AOL separation이 연속 실행 | [$9.253bn cash transfer와 content stub Long](ideas/2009/2009-02-15_TWX_stub_long.md) |
| 5 | 2013-07-24 | Time Warner, Inc. | Short→**Long** | 성공 — 산업통찰·전략가치 적중, EPS magnitude는 과대 | [OTT content scarcity·buyback compounding Long](ideas/2013/2013-07-24_TWX_long.md) |
| 6 | 2015-01-28 | Time Warner, Inc. | Short→**SOTP Long** | 성공 — hidden asset·strategic scarcity 적중, HBO multiple은 공격적 | [HBO+Turner가 EV를 덮는 residual WB SOTP Long](ideas/2015/2015-01-28_TWX_sotp_long.md) |
| 7 | 2015-03-11 | Time Warner, Inc. | Short→**Long** | 부분 성공 — earnings power 적중, 12개월 $110은 지연 | [$6 EPS·buyback·strategic optionality Long](ideas/2015/2015-03-11_TWX_long.md) |
| 8 | 2015-12-10 | Time Warner, Inc. | Short→**Short** | 강한 실패 — 산업방향 일부 적중, M&A tail이 security를 파괴 | [linear cable terminal decline Short](ideas/2015/2015-12-10_TWX_short.md) |
| 9 | 2017-02-22 | Time Warner / AT&T merger claim | Short→**Merger Arb Long** | 성공 — deal close, regulatory simplicity·duration은 실패 | [AT&T cash-stock collar merger-arbitrage Long](ideas/2017/2017-02-22_TWX_merger_long.md) |
| 10 | 2003-10-13 | Metals USA, Inc. (not Murphy USA) | Long→**Long** | 강한 성공 — 2005 Apollo $22 cash exit, 약 3.1x gross | [post-bankruptcy 자산·운전자본·operator reset Long](ideas/2003/2003-10-13_MUSA_metalsusa_long.md) |

## 2. 기업별 lifecycle

### KAR — survival에서 digital perimeter로

2020 Long은 $550m preferred로 생존확률이 상승하는 trade였고 1년 +16.4%로 부분 성공했다. 2021 Long은 BacklotCars·commercial workflow를 맞게 봤지만 2022 ADESA U.S. 매각으로 2024 $585m EBITDA forecast object가 소멸했다.

### Time Warner — 같은 기업, 다른 security와 clock

2006 LEAPS는 TWC/AOL 분리 방향이 맞아도 만기 전에 오지 않아 실패했다. 2009 stub은 hard separation으로 성공했다. 2013~2015 Long은 content scarcity·buyback·strategic value를 포착했다. 2015 Short는 cord-cutting을 맞히고 AT&T bid로 크게 실패했으며 2017 arb는 close probability를 맞히고 DOJ/duration을 틀렸다.

### Metals USA — post-bankruptcy convexity

debt-to-equity reset, working-capital release, operator change와 steel cycle이 겹쳤고 2005 Apollo $22 cash exit로 약 3.1x gross outcome을 만들었다.

## 3. 공통 투자교훈

1. **기업 thesis와 security thesis를 분리한다.** LEAPS 만기는 corporate value를 기다려주지 않는다.
2. **산업 terminal value와 주식 경로는 다르다.** 희소 IP의 strategic buyer가 secular Short를 파괴할 수 있다.
3. **Merger arb는 probability×duration×hedge carry다.** 결국 닫혀도 annualized IRR은 실패할 수 있다.
4. **Forecast perimeter를 고정하지 않는다.** 핵심 자산 매각 뒤에는 옛 EBITDA/SOTP를 폐기한다.
5. **SOTP는 residual implied value를 본다.** debt·tax·overhead를 넣은 뒤 진짜 공짜인지 확인한다.
6. **Post-BK는 asset floor와 recurring FCF를 중복하지 않는다.**
7. **성과가 없으면 null이다.** corporate action을 임의 return으로 바꾸지 않는다.

## 4. 산출물

- Payload: `data/curated/batch_048_kar_timewarner_metalsusa_deep_v7.json`
- Wrapper: `analysis/batch_048_kar_timewarner_metalsusa_10.md`
- Source packet: `data/curated/batch_048_source_packet.json`
- Builder: `scripts/48_build_batch_048_v9.py`
