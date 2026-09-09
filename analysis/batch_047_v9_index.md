# Batch 047 — Brink's / CIT / KAR — V9 Index

> Research as-of 2026-09-09. 첨부 SQL 원문으로 10건의 entity·direction·security를 수동 감사했다.

## 0. 배치 결론

raw Short 8건 중 실제 Short는 0건이다. BCO는 COVID recovery common Long, CIT 2009는 senior-unsecured debt Long, 나머지는 common/merger Long이다. CIT는 `recovery→funding normalization→asset separation→strategic merger`, KAR는 `physical liquidity→deleveraging→spin→digital/perimeter reset`의 lifecycle로 읽는다.

## 1. Idea Units

| # | 날짜 | 실제 security/entity | raw→연구 방향 | 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2020-05-28 | The Brink's Company | Short→**Long** | 생존·정상화·장기 margin thesis 성공, exact return 미검증 | [COVID 정상화·route density·smart-safe Long](ideas/2020/2020-05-28_BCO_long.md) |
| 2 | 2009-07-28 | CIT Group — 5.6% 2011 senior unsecured notes | Short→**Long** | 70¢ 신규 notes+equity recovery로 성공 | [59에 산 senior unsecured recovery Long](ideas/2009/2009-07-28_CIT_senior_unsecured_long.md) |
| 3 | 2011-10-04 | CIT Group Inc. | Short→**Long** | deposit funding·capital return으로 성공 | [post-BK funding normalization Long](ideas/2011/2011-10-04_CIT_long.md) |
| 4 | 2016-03-03 | CIT Group Inc. | Short→**Long** | aircraft sale·simplification·최종 strategic exit로 성공 | [OneWest funding·aircraft separation·NOL Long](ideas/2016/2016-03-03_CIT_long.md) |
| 5 | 2020-10-19 | CIT Group Inc. / First Citizens merger claim | Short→**Long** | 합병 종결·synergy 실현으로 성공 | [0.062 FCNCA 교환비율의 merger/RemainCo Long](ideas/2020/2020-10-19_CIT_merger_long.md) |
| 6 | 2006-09-13 | KAR Auction Services / ADESA | Short→**Long** | takeout으로 성공 | [$29~35 ADESA normalization Long](ideas/2006/2006-09-13_KAR_long.md) |
| 7 | 2010-11-12 | KAR Auction Services / ADESA | Short→**Long** | business/deleveraging 성공, exact return 미검증 | [$500m FCF·deleveraging recovery Long](ideas/2010/2010-11-12_KAR_long.md) |
| 8 | 2018-08-01 | KAR Auction Services / ADESA | Short→**Long** | spin catalyst 성공, 장기 remainco 경로 혼합 | [IAA spin SOTP $83 Long](ideas/2018/2018-08-01_KAR_long.md) |
| 9 | 2019-03-04 | KAR Auction Services / ADESA | Long→**Long** | spin event 성공, exact return 미검증 | [IAA spin·양쪽 multiple unlock Long](ideas/2019/2019-03-04_KAR_long.md) |
| 10 | 2019-11-20 | KAR Auction Services / ADESA | Long→**Long** | digital 방향 적중, TradeRev timing·standalone target 혼합 | [$28~30 TradeRev turnaround Long](ideas/2019/2019-11-20_KAR_long.md) |

## 2. 공통 투자교훈

1. **Security가 기업보다 먼저다.** CIT 2009 common은 0이지만 senior debt는 recovery가 있었다.
2. **Funding normalization은 liability-side alpha다.** post-BK lender는 asset growth보다 조달비용이 중요하다.
3. **Spin 성공과 remainco 성공은 다르다.** IAA 분리 뒤 ADESA perimeter가 다시 바뀌었다.
4. **Digital cannibalization은 contribution으로 본다.** revenue/vehicle보다 conversion·cost-to-serve·stranded cost가 핵심이다.
5. **쇠퇴산업도 equity는 성장할 수 있다.** BCO는 volume 감소를 pricing·outsourcing·density로 상쇄했다.
6. **성과가 없으면 null이다.** corporate event를 임의 return으로 바꾸지 않는다.

## 3. 산출물

- Payload: `data/curated/batch_047_brinks_cit_kar_deep_v7.json`
- Wrapper: `analysis/batch_047_brinks_cit_kar_10.md`
- Builder: `scripts/47_build_batch_047_v9.py`
