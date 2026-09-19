# Batch 070 — AmTrust / AFT / Carl Zeiss / Afya / AGCO / Arctic Glacier / AUTO1 / Algoma V9 Index

> Batch 043의 장문 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-18. 방향·증권·corporate action·payoff를 먼저 고정하고 1차자료로 actual을 검증했다.

## Canonical idea files

| # | 게시일 | Ticker | 원 SQL | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2013-08-19 | AFSI | Short | Short | [AmTrust Financial Services Inc.](ideas/2013/2013-08-19_AFSI_short.md) | fundamental concern 부분 적중 / trade 실패에 가까움 |
| 2 | 2004-11-18 | AFT-U | Short | Long | [Advanced Fiber Technologies Income Fund](ideas/2004/2004-11-18_AFT_UN_long.md) | 실패 — C$3.00 takeout가 capital loss를 확정 |
| 3 | 2022-03-12 | AFX.GY | Long | Long | [Carl Zeiss Meditec AG](ideas/2022/2022-03-12_AFX_GY_long.md) | 강한 실패 — product moat 생존, earnings duration·multiple 붕괴 |
| 4 | 2022-01-13 | AFYA | Long | Long | [Afya Limited](ideas/2022/2022-01-13_AFYA_long.md) | 운영 성공 / stock rerating 실패 |
| 5 | 2003-01-13 | AG | Short | Short | [AGCO Corporation](ideas/2003/2003-01-13_AGCO_short.md) | 중기 부분 성공 / 장기 thesis 실패 |
| 6 | 2005-10-18 | AG | Short | Short | [AGCO Corporation](ideas/2005/2005-10-18_AGCO_short.md) | 강한 실패 — ag upcycle이 leverage·rate headwind를 압도 |
| 7 | 2009-08-27 | AG-U | Long | Long | [Arctic Glacier Income Fund](ideas/2009/2009-08-27_AG_UN_long.md) | 강한 실패 — refinancing failure와 CCAA가 equity를 훼손 |
| 8 | 2021-09-30 | AG1 | Short | Long | [AUTO1 Group SE](ideas/2021/2021-09-30_AG1_long.md) | 운영 성공 / 높은 entry의 stock 실패 |
| 9 | 2022-03-04 | AG1-ETR | Long | Long | [AUTO1 Group SE](ideas/2022/2022-03-04_AG1_ETR_long.md) | 부분 성공·진행 중 — entry rerating, 2027 volume target은 미도달 |
| 10 | 2003-02-28 | AGA CN | Long | Long | [Algoma Steel Inc. (legacy)](ideas/2003/2003-02-28_AGA_CN_algoma_long.md) | 매우 강한 성공 — C$56 cash takeout, 약 16.97x price multiple |

## Direction / security / return audit

- AFT-U 2004와 AG1 2021의 raw Short를 실제 Long으로 교정했다.
- AFT-U와 AG-U는 ordinary common이 아니라 Canadian income-trust units다.
- source SQL performance row가 10건 모두 없어 corporate-action cash·official operating actual·제한적 historical price comparison만 썼다.
- Arctic Glacier의 mixed-currency distributions와 AFSI/AFT/Algoma의 corporate actions는 complete dated ledger 없이 exact total return·IRR을 만들지 않았다.

## 핵심 판정

1. AmTrust short는 accounting 우려가 후행 적중했지만 약 2배 adverse path 때문에 trade 실패에 가깝다.
2. AFT와 Arctic Glacier는 yield·enterprise cash flow가 capital loss와 creditor priority를 막지 못했다.
3. Carl Zeiss는 product moat가 살아도 earnings duration·entry multiple이 무너지면 common이 실패함을 보여준다.
4. Afya는 operating success / stock rerating failure, AUTO1 두 vintage는 같은 business의 entry-price 차이를 보여준다.
5. AGCO 2003은 중기 partial win 뒤 장기 실패, 2005는 약 325% adverse로 명확한 short failure다.
6. Algoma는 post-bankruptcy balance-sheet reset과 deep discount가 C$56 cash takeout으로 crystallize된 강한 성공이다.

## 구조화 데이터

- `data/curated/batch_070_afsi_aft_afx_afya_ag_ag1_aga_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events와 sources.
- `data/curated/batch_070_source_catalog.json`: raw metadata source packet이며 production glob에는 포함되지 않는다.
- `analysis/batch_070_afsi_aft_afx_afya_ag_ag1_aga_10.md`: Streamlit wrapper.
