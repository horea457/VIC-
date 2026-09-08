# Batch 039 — Nexstar / Sinclair V9 Index

> Batch 002 V9 규칙 적용: **VIC 아이디어 1건 = canonical Markdown 1개**.  
> 평가기준일 2024-01-31, 분석일 2026-09-08. 원문·SQL 방향·1차자료·가격경로를 분리 검증했다.

## Canonical idea files

| 게시일 | Ticker | 원 SQL | 실제 방향 | 상세 보고서 | 종합 판정 |
|---|---|---|---|---|---|
| 2005-12-20 | NXST | Short | Long | [2005-12-20 NXST](ideas/2005/2005-12-20_NXST_long.md) | 사업논지 성공·가격성과 미검증 |
| 2011-12-14 | NXST | Short | Long | [2011-12-14 NXST](ideas/2011/2011-12-14_NXST_long.md) | 강한 성공·촉매 경로 변경 |
| 2012-08-26 | NXST | Short | Long | [2012-08-26 NXST](ideas/2012/2012-08-26_NXST_long.md) | 강한 성공·목표범위 공격적 |
| 2016-01-29 | NXST | Short | Pair/Event | [2016-01-29 NXST](ideas/2016/2016-01-29_NXST_pair_event.md) | 구조 성공·CVR 가치 과대 |
| 2017-08-12 | NXST | Short | Long | [2017-08-12 NXST](ideas/2017/2017-08-12_NXST_long.md) | 강한 성공 |
| 2018-04-23 | NXST | Short | Long | [2018-04-23 NXST](ideas/2018/2018-04-23_NXST_long.md) | 강한 성공·직접 촉매 실패 |
| 2020-03-12 | NXST | Short | Long | [2020-03-12 NXST](ideas/2020/2020-03-12_NXST_long.md) | 매우 성공 |
| 2021-09-20 | NXST | Short | Long | [2021-09-20 NXST](ideas/2021/2021-09-20_NXST_long.md) | 성공·자본배분 질 저하 경고 |
| 2013-01-14 | SBGI | Short | Long | [2013-01-14 SBGI](ideas/2013/2013-01-14_SBGI_long.md) | 초기 강한 성공·장기 자본배분 경고 |
| 2015-08-16 | SBGI | Short | Long | [2015-08-16 SBGI](ideas/2015/2015-08-16_SBGI_long.md) | Core 성공·spectrum 논지 실패 |

## Direction audit

10건 중 SQL raw is_short가 모두 true지만 실제 방향은 NXST 2005·2011·2012·2017·2018·2020·2021과 SBGI 2013·2015가 Long이다. NXST 2016은 MEG Long 1주와 NXST Short 0.1249주를 결합한 CVR Pair/Event다. raw 값은 삭제하지 않고 감사추적용으로 보존했다.

## 배치 공통 결론

Nexstar의 반복 성공은 local TV가 단순 광고업이 아니라 net retrans와 격년 정치광고, 낮은 capex, post-synergy M&A를 결합한 levered FCF machine이었기 때문이다. 그러나 성공의 질은 시점마다 다르다. 2011년 sale catalyst는 실패하고 buyer 전환이 구했고, 2016년 CVR은 구조는 맞아도 payout을 과대평가했으며, 2021년 The CW는 과거 자본배분 능력의 영역외 extrapolation을 경고했다. Sinclair는 core broadcasting이 성공해도 spectrum option과 지배주주 자본배분이 별도로 실패할 수 있음을 보여준다.

## 공통 분석식

방송 보통주가치는 gross retrans가 아니라 net retrans profit, 정치년/비정치년 평균 core 광고, fully-taxed FCF, post-synergy M&A economics를 계산한 뒤 순부채·preferred와 자본배분을 차감해 본다. Pair/Event는 이 식과 분리해 계약상 CVR waterfall과 hedge cash flow로 계산한다.

## 반복 학습

1. 높은 leverage에서 valuation floor는 없다. liquidity·covenant·maturity가 floor보다 먼저다.
2. Strategic review의 실패가 곧 투자실패는 아니다. deal 없는 FCF carry가 충분하면 buyer 전환도 가능하다.
3. Gross retrans, reverse retrans, subscriber volume을 나누지 않으면 방송사 단위경제성을 과대평가한다.
4. 정치광고는 고마진이지만 격년 현금이므로 two-year average로만 terminal value를 만든다.
5. CVR·spectrum은 opening bid가 아니라 세후 순분배액과 지급단위·시간으로 가치화한다.
6. 좋은 core business와 좋은 지주회사 보통주는 다르다. FCF 사용처의 ROIC가 최종 귀속을 결정한다.

## 앱/DB 반영

- 기존 batch wrapper는 이 10개 canonical 파일을 순서대로 불러온다.
- curated JSON은 10 ideas_master + 10 postmortem + 60 Claim + metrics + timeline + sources를 자체 포함한다.
- Streamlit은 JSON overlay를 SQLite에 적용하므로 목록 선택 시 이 보고서와 같은 상세 데이터가 표시된다.
