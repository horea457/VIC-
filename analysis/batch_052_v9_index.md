# Batch 052 — Madison Square Garden / New England Realty Associates V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 051 마지막 MSG 2010-12-22 이후, Batch 48~51 reviewed idea_id를 제외한 다음 10건.

## Canonical Idea Units

| # | 날짜 | Ticker | 실제 방향 | Canonical | 핵심 판정 |
|---:|---|---|---|---|---|
| 1 | 2012-12-17 | MSG | Long | [MSG 2012](ideas/2012/2012-12-17_MSG_long.md) | renovation 종료·FCF inflection 성공 방향 |
| 2 | 2014-08-04 | MSG | Long | [MSG 2014](ideas/2014/2014-08-04_MSG_long.md) | 2015 separation으로 강한 성공 |
| 3 | 2016-07-20 | MSG | Long | [MSG 2016](ideas/2016/2016-07-20_MSG_long.md) | post-spin earnings normalization 성공 방향 |
| 4 | 2018-11-20 | MSG | Long | [MSG 2018](ideas/2018/2018-11-20_MSG_long.md) | 2020 spin 성공 / COVID로 payoff 경로 혼합 |
| 5 | 2001-12-28 | NEN | Long | [NEN 2001](ideas/2001/2001-12-28_NEN_long.md) | 13%+ cap-rate entry, 강한 성공 방향 |
| 6 | 2002-12-28 | NEN | Long | [NEN 2002](ideas/2002/2002-12-28_NEN_long.md) | private-value gap 축소, 강한 성공 방향 |
| 7 | 2005-12-09 | NEN | Long | [NEN 2005](ideas/2005/2005-12-09_NEN_long.md) | 5Y -14.8%, cycle timing 실패 |
| 8 | 2007-02-27 | NEN | Long | [NEN 2007](ideas/2007/2007-02-27_NEN_long.md) | 3Y -40.8%, cap-rate peak 오판 |
| 9 | 2009-08-29 | NEN | Long | [NEN 2009](ideas/2009/2009-08-29_NEN_long.md) | 5Y +208.3%, 강한 성공 |
| 10 | 2011-06-30 | NEN | Long | [NEN 2011](ideas/2011/2011-06-30_NEN_long.md) | 3Y +134.8%, 강한 성공 |

## Queue / Metadata Note

source_true_unreviewed.json은 Batch 48 이후 reviewed status가 갱신되지 않아 MSG 2018 이후 이미 처리한 MUSA/MDR/MHK가 다시 나타난다.

Batch 052는:
1. Batch 051 마지막 idea 이후로 이동
2. Batch 048~051의 reviewed idea_id 40개를 제외
3. 남은 다음 10건

이라는 규칙으로 경계를 복원했다.

이번 10건은 raw direction과 실제 direction이 모두 Long으로 일치한다.

## Madison Square Garden — 같은 SOTP가 실제 securities로 바뀌는 과정

### 2012: FCF Inflection
핵심은 약 $1bn Garden renovation이 끝나며 capex가 급락하는 것이었다.

**Renovation completion → lower capex → higher FCF → capital-return / recap optionality**

### 2014: Media + Hidden Assets
RSN이 current price 대부분을 설명하고:
- Knicks/Rangers
- Garden / air rights
- Entertainment

를 공짜 또는 큰 할인에 얻는 구조였다.

2015 실제로 media와 sports/entertainment가 분리됐다.

### 2016: Post-spin accounting normalization
Media가 빠진 새 MSG를 분석하면서:
- termination expense
- standalone transition cost
- DTA
- depreciation
를 economic earnings로 재구성했다.

### 2018: Sports vs Entertainment
sports spin을 예상했고 실제 2020 MSG Sports / MSG Entertainment separation이 발생했다.

다만 COVID가 live entertainment를 타격했기 때문에:

**Catalyst correct ≠ path/return automatically correct**

라는 교훈이 남는다.

## New England Realty Associates — 같은 회사로 보는 cap-rate cycle 교과서

### 2001 / 2002
- implied cap rate 12.5~13.4%
- 낮은 leverage
- high occupancy
- 5.8x FCF / 6.6x AFFO

싼 asset + good operator였다.

### 2005
- implied cap 약 7.7%
- private-market cap 5~6%
- NAV $113

여전히 relative cheap했지만 absolute cap-rate margin of safety는 크게 줄었다.

SQL 결과:
- 1Y +0.9%
- 3Y -28.1%
- 5Y -14.8%

### 2007
- 5% cap rate base
- margin expansion
- activist unlock

가장 위험한 조합이었다.

SQL 결과:
- 1Y -11.8%
- 2Y -39.0%
- 3Y -40.8%

### 2009
GFC 이후:
- implied cap 8.1%
- 7% cap를 써도 NAV upside
- share count 이미 20%+ 감소
- long-term fixed mortgages

SQL 결과:
- 1Y +13.4%
- 3Y +73.6%
- 5Y +208.3%

### 2011
- core implied cap 약 8.6%
- JV hidden value
- Boston rental recovery
- buyback history

SQL 결과:
- 1Y +23.6%
- 3Y +134.8%

## 핵심 비교

| 시점 | Entry cap / framing | 3Y price-only | 판정 |
|---|---|---:|---|
| 2005 | 7.7%, market comps 5~6% | -28.1% | 실패 |
| 2007 | 5% cap + margin expansion | -40.8% | 강한 실패 |
| 2009 | 8.1% implied cap | +73.6% | 강한 성공 |
| 2011 | 8.6% core implied cap | +134.8% | 강한 성공 |

**회사 quality는 거의 같았고 starting yield가 달랐다.**

## NEN 가격 데이터 주의

NEN은 2012-01-03 Depositary Receipts를 3-for-1 forward split했다.

- 이전: 1 receipt = 1/10 Class A Unit
- 이후: 1 receipt = 1/30 Class A Unit

따라서 2001~2011 원문 nominal share prices를 2012 이후 price와 직접 비교하지 않는다.
SQL performance ratio는 split-adjusted series로 사용한다.

## Batch 052 상위 투자 교훈

1. SOTP는 실제 separation route가 있을 때 가장 강하다.
2. capex cliff는 earnings보다 FCF를 급격히 바꿀 수 있다.
3. post-spin 기업은 historical segment P&L을 standalone economics로 다시 만들어야 한다.
4. announced spin이 맞아도 macro shock이 payoff path를 망가뜨릴 수 있다.
5. **부동산주는 회사보다 entry cap rate가 중요할 수 있다.**
6. relative NAV discount와 absolute asset yield를 분리한다.
7. peer cap rates가 동시에 낮으면 relative cheapness는 안전마진이 아니다.
8. buyback은 NAV discount가 큰 real-estate microcap에서 강한 per-share compounding 도구다.
9. hard catalyst가 없어도 intrinsic value growth + share shrinkage가 있으면 시간이 catalyst가 될 수 있다.
10. 장기 DB는 split / distribution / spin을 corporate-action adjusted basis로 관리해야 한다.

## 앱 / DB 반영

- Wrapper: analysis/batch_052_msg_nen_10.md
- Overlay: data/curated/batch_052_msg_nen_deep_v7.json
- Canonical source of truth: 위 10개 idea Markdown.
