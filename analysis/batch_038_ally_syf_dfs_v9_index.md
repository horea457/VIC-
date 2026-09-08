# Batch 038 — Ally / Synchrony / Discover V9 Index

> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = Markdown 1개**가 canonical report다.  
> Research as-of 2026-09-08. 원문·1차자료·SQL 가격경로를 교차검증했다.

## Canonical idea files

| VIC 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |
|---|---|---|---|---|---|
| 2017-07-19 | ALLY | Long | Long | [2017-07-19 ALLY Long](ideas/2017/2017-07-19_ALLY_long.md) | 성공 |
| 2018-12-27 | ALLY | Long | Long | [2018-12-27 ALLY Long](ideas/2018/2018-12-27_ALLY_long.md) | 성공 |
| 2020-04-30 | ALLY | Long | Long | [2020-04-30 ALLY Long](ideas/2020/2020-04-30_ALLY_long.md) | 매우 성공 |
| 2022-08-31 | ALLY | Long | Long | [2022-08-31 ALLY Long](ideas/2022/2022-08-31_ALLY_long.md) | 혼합·초기 실패 |
| 2015-12-11 | SYF | Short | Long | [2015-12-11 SYF Long](ideas/2015/2015-12-11_SYF_long.md) | 부분 성공·moat 과대평가 |
| 2017-05-11 | SYF | Short | Long | [2017-05-11 SYF Long](ideas/2017/2017-05-11_SYF_long.md) | 혼합·목표수익 실패 |
| 2020-07-13 | SYF | Long | Long | [2020-07-13 SYF Long](ideas/2020/2020-07-13_SYF_long.md) | 강한 성공 |
| 2022-03-16 | SYF | Short | Long | [2022-03-16 SYF Long](ideas/2022/2022-03-16_SYF_long.md) | 혼합·시간축 실패 |
| 2014-07-15 | DFS | Long | Long | [2014-07-15 DFS Long](ideas/2014/2014-07-15_DFS_long.md) | 장기 부분 성공·초기 실패 |
| 2016-06-25 | DFS | Long | Long | [2016-06-25 DFS Long](ideas/2016/2016-06-25_DFS_long.md) | 장기 강한 성공 |

## Direction audit

10건 모두 실제 VIC 방향은 Long이다. SYF 2015·2017·2022의 raw `Short`는 본문 목표가, 기대수익, 보유공시와 모순되는 SQL metadata 오류다. 원본값은 삭제하지 않고 각 V9 파일에 감사추적용으로 남겼다.

## Batch 038의 공통 분석식

소비자금융의 지속가능 수익은 다음 순서로 본다.

`asset yield + fee/network income - normalized credit loss - deposit/wholesale funding cost - partner economics - operating/compliance cost = sustainable pretax return`

그 다음에 CET1과 필요한 성장자본을 차감해 실제 distributable earnings와 buyback capacity를 계산한다. 높은 표면 ROE, 낮은 P/E, 큰 allowance 중 하나만으로 싸다고 결론내리지 않는다.

## 상위 교훈

1. Ally 2017·2018·2020의 성공은 low P/TBV보다 funding mix와 stress 후 capital survival을 함께 본 데서 나왔다.
2. Ally 2022는 credit stress는 견뎠지만 deposit beta와 asset repricing lag를 과소평가했다.
3. Synchrony의 RSA는 실제 counter-cyclical buffer지만, Walmart·Gap은 긴 계약기간이 partner tail을 제거하지 못함을 보여줬다.
4. excess capital adjusted EPS는 환원기간·RWA growth·평균 buyback 가격을 넣지 않으면 IRR을 과장한다.
5. Discover network는 실제 전략가치가 있었지만 2014·2016 당시의 1년 목표와 2024 realization은 별도 판정해야 한다.
6. credit quality와 enterprise quality는 다르다. Discover의 product misclassification은 compliance loss를 별도 stress해야 함을 보여준다.

## 앱/DB 반영

- `analysis/batch_038_ally_syf_dfs_10.md`는 아래 10개 canonical 파일을 불러오는 V9 wrapper다.
- `data/curated/batch_038_ally_syf_dfs_deep_v7.json`은 최신 overlay schema로 재작성했다.
- Streamlit은 시작 시 이 JSON을 SQLite에 자동 overlay하므로 Claim·metrics·timeline·sources가 같은 내용으로 표시된다.
