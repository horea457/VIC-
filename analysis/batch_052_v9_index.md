# Batch 052 — Madison Square Garden / New England Realty Associates — V9 Index

> Research as-of 2026-09-10. Batch 051 다음 10건이다. **10 idea = 10 canonical reports**이며 현 첨부 SQL로 확인되지 않는 성과값은 모두 null 처리했다.

## 0. 배치 결론

MSG 4건은 같은 SOTP가 `renovation capex cliff→2015 Media 분할→2020 Sports/Entertainment 분할→2023 Sphere 분할`로 실제 securities가 되는 과정이다. NEN 6건은 같은 operator·자산이어도 13% cap의 2001/02, 5~7% late-cycle 2005/07, 8%+ post-GFC 2009/11의 결과가 왜 달라지는지를 보여준다.

## 1. Idea Units

| # | 날짜 | 실제 회사 | 방향 | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2012-12-17 | The Madison Square Garden Company (pre-2015) | Long | 사업·분할경로 성공, $60/18개월 exact return 미검증 | [Garden capex cliff·FCF inflection·recap Long](ideas/2012/2012-12-17_MSG_long.md) |
| 2 | 2014-08-04 | The Madison Square Garden Company (pre-2015) | Long | 강한 사업·분할 성공, exact total return 미검증 | [RSN FCF+teams·air-rights SOTP Long](ideas/2014/2014-08-04_MSG_long.md) |
| 3 | 2016-07-20 | The Madison Square Garden Company (post-2015) | Long | 사업 정상화·후속분할 성공 방향, exact return 미검증 | [post-spin accounting normalization·$209 Long](ideas/2016/2016-07-20_MSG_long.md) |
| 4 | 2018-11-20 | The Madison Square Garden Company (post-2015) | Long | 분할 성공, entertainment payoff·timing 혼합, exact return 미검증 | [announced sports spin·$373 SOTP Long](ideas/2018/2018-11-20_MSG_long.md) |
| 5 | 2001-12-28 | New England Realty Associates Limited Partnership | Long | 사업·가치 방향 강한 성공, exact return 미검증 | [13.4% cap·5.8x FCF owner-operator Long](ideas/2001/2001-12-28_NEN_long.md) |
| 6 | 2002-12-28 | New England Realty Associates Limited Partnership | Long | 사업·private-value 방향 강한 성공, exact return 미검증 | [12.5~13% cap·6.6x AFFO Long](ideas/2002/2002-12-28_NEN_long.md) |
| 7 | 2005-12-09 | New England Realty Associates Limited Partnership | Long | 운영논지 부분 성공, 6% cap·cycle framing 실패 | [7.7% implied cap·$113 NAV Long](ideas/2005/2005-12-09_NEN_long.md) |
| 8 | 2007-02-27 | New England Realty Associates Limited Partnership | Long | 운영 단기 적중, cap-rate·activist 핵심 실패 | [5% cap·margin expansion·activist Long](ideas/2007/2007-02-27_NEN_long.md) |
| 9 | 2009-08-29 | New England Realty Associates Limited Partnership | Long | cycle·capital-allocation 강한 성공 방향, exact return 미검증 | [post-GFC 8.1% cap·buyback Long](ideas/2009/2009-08-29_NEN_long.md) |
| 10 | 2011-06-30 | New England Realty Associates Limited Partnership | Long | 사업·per-share compound 방향 강한 성공, exact return 미검증 | [8.6% core cap·JV·buyback compounder Long](ideas/2011/2011-06-30_NEN_long.md) |

## 2. SQL / Entity / Security Audit

첨부 `VIC_IDEAS(4).sql`에는 `catalyst·companies·descriptions` COPY만 있고 `ideas·performance` data COPY가 없다. 10건 모두 catalyst는 있으나 description은 7건만 존재한다. date·author·link는 기존 curated overlay와 대조했고, 기존 초안의 NEN 성과비율 4건은 provenance가 없어 폐기했다. 방향은 10건 모두 raw Long=실제 Long이다.

MSG 2012/14는 pre-2015 common으로 MSGN 잔존주식과 3:1 신 MSG를 함께 받아야 한다. MSG 2016/18은 post-2015 common으로 2020 1:1 MSGE를 더해야 한다. NEN은 2012 전 1/10 Unit receipt, 이후 1/30 Unit receipt다.

## 3. MSG — 투자논지의 진화

- **2012:** $1bn renovation이 끝나는 capex cliff와 $275m+ FCF를 샀다. $1bn debt buyback은 optional이었고 실제 unlock은 분할이었다.
- **2014:** RSN $4.6bn이 price를 지지하고 teams·venue·air rights $27/share가 upside였다. 2015 분할이 bucket을 직접 증권화했다.
- **2016:** carve-out -$114m loss에서 termination·reserve·DTA·transition cost를 조정해 ongoing $209를 만들었다. 핵심은 one-time 비용의 반복성 감사다.
- **2018:** announced spin은 맞았지만 Sphere를 $700m cost로 더한 가정은 틀렸다. 2020 COVID와 초과 capex 때문에 catalyst success와 payoff가 갈렸다.

## 4. NEN — 같은 회사, 다른 entry cap

| 시기 | T0 absolute yield | 핵심 risk/reward | 판정 |
|---|---|---|---|
| 2001/02 | 12.5~13.4% cap, 5.8~6.6x cash earnings | 낮은 leverage·운영복리 | 강한 성공 방향 |
| 2005 | 7.7% implied vs 5~6% private | relative cheap, absolute buffer 축소 | valuation 실패 |
| 2007 | 5% cap+margin expansion+activist | easy-credit peak 낙관 중첩 | 핵심 실패 |
| 2009/11 | 8.1~8.6% cap+buyback | refinancing survival·per-share compounding | 강한 성공 방향 |

## 5. 공통 투자 교훈

1. SOTP는 분배증권·교환비율·세금을 연결해야 투자수익이 된다.
2. capex cliff는 EBITDA보다 FCF를 더 빠르게 바꾼다.
3. carve-out add-back은 `비현금`이 아니라 `비반복`인지 3년으로 검사한다.
4. cost는 asset value가 아니다. 미완성 growth capex에는 completion·ROIC haircut이 필요하다.
5. 부동산 NAV discount와 absolute cap-rate safety margin을 분리한다.
6. peer cap가 동시에 낮으면 relative cheapness는 독립 안전마진이 아니다.
7. activist는 권한·자금·날짜가 있어야 catalyst다.
8. hard catalyst가 없어도 할인 buyback과 NAV/share 성장은 시간을 catalyst로 만든다.
9. business survival과 common return은 별도 판정한다.
10. 성과 테이블이 없으면 exact return은 null이다.

## 6. 산출물

- Payload: `data/curated/batch_052_msg_nen_deep_v7.json`
- Wrapper: `analysis/batch_052_msg_nen_10.md`
- Source packet: `data/curated/batch_052_source_packet.json`
- Builder: `scripts/52_build_batch_052_v9.py`
