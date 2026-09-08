# Batch 040 — Gray / Townsquare V9 Index

> Batch 002 V9 규칙 적용: **VIC 아이디어 1건 = canonical Markdown 1개**.  
> 평가기준일 2024-01-31, 분석일 2026-09-08. 원문·SQL 방향·1차자료·가격경로를 분리 검증했다.

## Canonical idea files

| 게시일 | Ticker | 원 SQL | 실제 방향 | 상세 보고서 | 종합 판정 |
|---|---|---|---|---|---|
| 2014-04-18 | GTN | Long | Long | [2014-04-18 GTN](ideas/2014/2014-04-18_GTN_long.md) | 성공·중간 경로 위험 |
| 2018-08-03 | GTN | Short | Long | [2018-08-03 GTN](ideas/2018/2018-08-03_GTN_long.md) | 성공·레버리지 경고 |
| 2019-07-11 | GTN | Short | Long | [2019-07-11 GTN](ideas/2019/2019-07-11_GTN_long.md) | 사업논지 성공·보통주 실패 |
| 2020-11-05 | GTN | Long | Long | [2020-11-05 GTN](ideas/2020/2020-11-05_GTN_long.md) | 전술적 강한 성공·장기 반전 |
| 2021-11-19 | GTN | Short | Long | [2021-11-19 GTN](ideas/2021/2021-11-19_GTN_long.md) | 치명적 실패 |
| 2015-03-25 | TSQ | Long | Long | [2015-03-25 TSQ](ideas/2015/2015-03-25_TSQ_long.md) | 실패 |
| 2015-05-28 | TSQ | Long | Long | [2015-05-28 TSQ](ideas/2015/2015-05-28_TSQ_long.md) | 치명적 실패 |
| 2016-05-09 | TSQ | Short | Long | [2016-05-09 TSQ](ideas/2016/2016-05-09_TSQ_long.md) | 부분 성공·기간 불일치 |
| 2018-02-27 | TSQ | Long | Long | [2018-02-27 TSQ](ideas/2018/2018-02-27_TSQ_long.md) | 성공·1년 지연 |
| 2019-03-11 | TSQ | Long | Long | [2019-03-11 TSQ](ideas/2019/2019-03-11_TSQ_long.md) | 매우 성공 |

## Direction audit

10건 모두 본문상 Long이다. SQL raw가 Short로 저장된 GTN 2018·2019·2021과 TSQ 2016은 방향 metadata 오류이므로 실제 방향을 Long으로 교정하고 raw 값은 보존했다. 나머지 GTN 2014·2020, TSQ 2015 두 건·2018·2019는 raw와 본문이 일치한다.

## 배치 공통 결론

Gray의 2014·2018·2020 Long은 규제 후 남은 economics, accretive M&A, 이미 예약된 정치광고처럼 가까운 현금근거가 있어 성공했다. 2019 재매수와 2021 Long은 사업수치는 맞아도 높은 debt와 terminal multiple이 common equity 수익을 압도했다. Townsquare는 2015~2016 낮은 P/FCF와 owner-operator 서사가 실패했고, 2018 전략철회와 2019 숨은 디지털 자산처럼 행동·segment data가 확인된 뒤에야 성공했다.

## 공통 분석식

레버리지 미디어의 보통주 수익은 core FCF 성장만으로 결정되지 않는다. Normalized fully-taxed FCF에서 정치광고·NOL·일회 시너지를 분리하고, preferred 포함 순부채와 terminal EV multiple을 적용한 뒤 남는 equity를 본다. 디지털은 매출명이 아니라 고객·churn·gross margin·segment EBITDA로 검증한다.

## 반복 학습

1. 좋은 방송자산도 peak leverage에서 사면 나쁜 주식이 될 수 있다.
2. 이미 구현된 synergy는 새 upside가 아니라 현재 earnings base다.
3. 정치광고 event는 예약액과 증분마진을 계산하고 촉매 직후 exit rule을 정한다.
4. 쇠퇴산업의 낮은 P/FCF는 terminal decline와 fully-taxed cash를 빼면 value trap일 수 있다.
5. Owner-operator 서사는 사업별 post-deal ROIC와 실제 debt reduction으로만 검증한다.
6. 실패한 사업을 철수하는 전략 reset과 숨은 digital segment의 정량 disclosure는 강한 촉매가 될 수 있다.

## 앱/DB 반영

- 기존 batch wrapper는 이 10개 canonical 파일을 순서대로 불러온다.
- curated JSON은 10 ideas_master + 10 postmortem + 60 Claim + metrics + timeline + sources를 자체 포함한다.
- Streamlit은 JSON overlay를 SQLite에 적용하므로 목록 선택 시 이 보고서와 같은 상세 데이터가 표시된다.
