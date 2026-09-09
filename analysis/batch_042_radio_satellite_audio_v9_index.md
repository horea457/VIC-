# Batch 042 — Radio / Satellite Audio V9 Index

> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-09. 원문 방향과 실제 security direction을 분리하고 SEC·회사·CRB·FCC 1차자료로 검증했다.

## Canonical idea files

| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2013-09-12 | CMLS | Short | Long | [2013-09-12 CMLS](ideas/2013/2013-09-12_CMLS_long.md) | 강한 실패 — common equity가 두 차례 구조조정으로 훼손 |
| 2 | 2010-12-20 | SGA | Short | Long | [2010-12-20 SGA](ideas/2010/2010-12-20_SGA_long.md) | 가격 기준 강한 성공 — claim reconstruction 신뢰도 제한 |
| 3 | 2019-08-24 | SGA | Long | Long | [2019-08-24 SGA](ideas/2019/2019-08-24_SGA_long.md) | 혼합 — business 방어 성공, target·timing 실패 |
| 4 | 2022-07-14 | SGA | Long | Long | [2022-07-14 SGA](ideas/2022/2022-07-14_SGA_long.md) | 근접기간 부분 성공 — 배당 강함, 영업모델 미달 |
| 5 | 2012-01-05 | SALM | Long | Long | [2012-01-05 SALM](ideas/2012/2012-01-05_SALM_long.md) | 장기 실패 — 배당 일부 실현 후 $1 take-private |
| 6 | 2019-08-06 | SALM | Short | Long | [2019-08-06 SALM](ideas/2019/2019-08-06_SALM_long.md) | 강한 실패 — 배당 중단·delisting·$1 take-private |
| 7 | 2002-08-30 | XMSR | Short | Long | [2002-08-30 XMSR](ideas/2002/2002-08-30_XMSR_bond_long.md) | 강한 성공 — security selection 적중, exact realized IRR은 경로 의존 |
| 8 | 2006-12-31 | SIRI | Short | Short | [2006-12-31 SIRI](ideas/2006/2006-12-31_SIRI_short.md) | 혼합/실패 — 재무위험 적중, short payoff 미검증·merger가 경로 변경 |
| 9 | 2013-02-25 | SIRI | Short | Long | [2013-02-25 SIRI](ideas/2013/2013-02-25_SIRI_long.md) | 중기 사업·capital allocation 성공 — exact equity IRR 미검증 |
| 10 | 2017-04-25 | SIRI | Short | Short | [2017-04-25 SIRI](ideas/2017/2017-04-25_SIRI_short.md) | 24개월 실패 — catalyst 일부 적중, 구조적 약화는 늦게 발생 |

## Direction / security audit

Raw SQL은 CMLS 2013, SGA 2010, SALM 2019, XMSR 2002, SIRI 2006·2013·2017을 Short로 저장했다. 실제 원문은 CMLS·SGA 2010·SALM 2019·SIRI 2013이 common Long이며 XMSR 2002는 14% senior secured notes Long이다. SGA 2019·2022와 SALM 2012는 raw와 실제가 Long, SIRI 2006·2017만 실제 Short다.

## 핵심 판정

1. **CMLS 2013 Long:** Westwood One 자산은 생존했지만 common은 2017·2026 두 차례 Chapter 11을 거쳐 강한 실패다.
2. **SGA 2010 Long:** 원문 body는 누락됐지만 price-only 3년 +162.9%(연 38.01%), 5년 +130.4%(연 18.16%)로 성과는 강하다.
3. **SGA 2019 Long:** 순현금·pandemic 방어는 맞았으나 3년 +9.6%(연 3.10%)로 $50 target은 실패했다.
4. **SGA 2022 Long:** 2022 FCF는 forecast보다 30% 낮았지만 약 6개월 내 $4.50 dividend와 price-only +10.7%로 catalyst가 적중했다.
5. **SALM 2012·2019 Long:** block programming과 배당은 일시적이었고 2020 배당 중단, 2024 delisting/debt transaction, 2026 $1 take-private로 장기 실패했다.
6. **XMSR 2002 bond Long:** 2003 secured exchange와 2006 premium redemption으로 security selection이 강하게 적중했다. exact IRR은 tender·warrant 경로 부재로 만들지 않았다.
7. **SIRI 2006 Short:** standalone funding risk는 맞았지만 subscriber growth와 XM merger가 2007 path를 바꿨다.
8. **SIRI 2013 Long:** 2016~2018 EBITDA·FCF·margin과 대규모 buyback은 중기 논지를 확인했다. 10% subscriber CAGR은 과대였다.
9. **SIRI 2017 Short:** 15.5% royalty는 방향상 적중했지만 24개월 earnings path와 $2.50 target은 실패했다. subscriber decline은 2024~25에야 뚜렷했다.

## 공통 분석식

`subscriber/local-ad/block revenue - content·royalty·station cost - corporate cost - cash interest - capex - tax = common equity FCF`

채권은 `escrow coupon + exchange consideration + warrant/recovery - stripped purchase cost`로 따로 계산한다. Debt 감소는 organic paydown, asset-sale-funded exchange, court-driven equitization을 구분한다.

## 상위 교훈

1. radio license scarcity는 advertiser attention의 moat가 아니다.
2. 높은 FCF yield는 짧은 duration과 refinancing tail의 가격일 수 있다.
3. 순현금은 downside buffer지만 자동 rerating catalyst가 아니다.
4. 배당·debt paydown·성장투자는 같은 현금을 두 번 쓸 수 없다.
5. distress에서는 enterprise thesis보다 security waterfall이 더 중요하다.
6. secular short는 방향뿐 아니라 horizon 안의 earnings inflection이 필요하다.

## 앱/DB 반영

- `analysis/batch_042_radio_satellite_audio_10.md`는 10개 canonical 파일을 불러오는 wrapper다.
- `data/curated/batch_042_radio_satellite_audio_deep_v7.json`은 V9 상세 overlay다.
