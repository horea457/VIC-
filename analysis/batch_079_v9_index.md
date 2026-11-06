# Batch 079 — AIG / AIG Warrants / Aimia V9 Index

> **VIC 아이디어 1건 = canonical Markdown 1개.** Research as-of 2026-11-06, 가격 기준 2026-10-23.
> **Batch boundary:** Batch 078 마지막 AIFS 2021-10-28 다음의 SQL ticker/date/id 정렬 10건.

## Canonical idea files

| # | 게시일 | Ticker | 원 SQL | 실제 증권 / 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2007-04-09 | AIG | Short | NYSE:AIG common / Long | [American International Group](ideas/2007/2007-04-09_AIG_long.md) | 치명적 실패 — 2년 -98% |
| 2 | 2008-12-30 | AIG | Short | NYSE:AIG common / Short | [American International Group](ideas/2008/2008-12-30_AIG_short.md) | 전술적 강한 성공 — 7주 내 목표 달성, 장기 보유 시 실패 |
| 3 | 2011-06-19 | AIG | Short | NYSE:AIG common / Long | [American International Group](ideas/2011/2011-06-19_AIG_long.md) | 강한 성공 — 2년 +58%, 사업 비관도 적중 |
| 4 | 2012-05-15 | AIG | Short | NYSE:AIG common / Long | [American International Group](ideas/2012/2012-05-15_AIG_long.md) | 강한 성공 — $50 달성, 다만 보험 개선 목표는 실패 |
| 5 | 2013-11-06 | AIG | Short | NYSE:AIG common / Long | [American International Group](ideas/2013/2013-11-06_AIG_long.md) | 실패 — 자사주는 맞고 ROE·장부 성장은 틀림 |
| 6 | 2011-09-26 | AIG.WS | Short | AIG/WS 워런트 (행사가 $45, 만기 2021-01-19) / Long | [American International Group warrants](ideas/2011/2011-09-26_AIG_WS_warrant_long.md) | 중간 청산 매우 강한 성공 / 만기 보유 시 사실상 전손 |
| 7 | 2015-02-13 | AIG.WS | Short | AIG/WS 워런트 (만기 2021-01-19) / Long | [American International Group warrants](ideas/2015/2015-02-13_AIG_WS_warrant_long.md) | 실패 — 만기 계산가 약 $0.02 |
| 8 | 2018-11-18 | AIG.WS | Long | NYSE:AIG common / Long. SQL 티커는 AIG.WS지만 원문은 보통주 분석 | [American International Group](ideas/2018/2018-11-18_AIG_common_long.md) | 강한 성공 — 영업 적중, 다만 $70은 5.2년, 중간 -57% |
| 9 | 2013-05-08 | AIG/WS | Short | AIG/WS 워런트 (만기 2021-01-19) / Long | [American International Group warrants](ideas/2013/2013-05-08_AIG_WS_warrant_long.md) | 실패 — 만기 계산가 약 $0.02, 내재가치 고점도 +17% 수준 |
| 10 | 2013-11-26 | AIM | Long | TSX:AIM common / Long | [Aimia Inc.](ideas/2013/2013-11-26_AIM_aimia_long.md) | 치명적 실패 — 앵커 파트너 이탈, -86% |

## Metadata / security / return audit

- raw Short→실제 Long 7건: AIG 2007·2011·2012·2013, 워런트 2011·2013·2015. AIG 2008은 raw와 실제 모두 Short다.
- 증권 교정 1건: 2018-11-18은 티커가 AIG.WS지만 원문이 $42.94 보통주를 분석한다.
- 공개 VIC URL 2건 복구: 워런트 2011·2013. 게시 시각이 SQL과 일치한다.
- SQL 성과행 보유 5건은 Yahoo 분할 조정 종가와 대조해 방향·규모가 일치했다. 나머지 5건은 Yahoo 가격으로 계산했다.
- **워런트 일별 시가 미확보.** 시가 기록은 원문 $6.43, $19뿐이다. 그 외는 내재가치 하한이며 2015 진입가 약 $23은 원문 수익률 역산값(등급 D)이다.
- 만기 계산가 약 $0.02는 `1.067 × ($42.25 − $42.2282)`다. NYSE 거래는 2021-01-13에 정지되어 실제 정산 결과는 미확인이다.
- 2011 워런트 배당은 Yahoo adjusted close에 포함되지 않는다. AIG 2008 Short의 차입비용은 미확인이다.

## 핵심 판정

1. **2007 Long은 AIGFP를 분석 범위에 넣지 않았다.** 사업부 설명에 없었고 AA 등급을 강점으로만 봤다. 2년 -98.3%.
2. **2008 Short는 7주 만에 목표를 맞혔고 2년 보유면 -88.9%였다.** 손실은 맞혔지만 정부 재조정의 기저율을 낮게 봤다.
3. **2011·2012 Long의 수익원은 정부 물량 해소와 할인 자사주였다.** 합산비율 개선은 기여하지 않았다.
4. **2013 Long은 경영진의 목표 후퇴를 노이즈로 해석했다.** $80 도달까지 10.5년이 걸렸다.
5. **워런트 3건은 2021-01-19 종가 $42.25 대 행사가 $42.2282로 끝났다.** 2013·2015 글은 2021 말 BV로 2021-01 만기 가치를 계산했다. 9.5개월 뒤 보통주는 $61.08이었다.
6. **2018 보통주는 합산비율 111.4→90.1을 맞혔다.** 다만 '잃어도 조금'과 달리 2020-03 -57%였다.
7. **Aimia는 2020 계약을 기한 밖 위험으로 처리했다.** 발표 전 이미 -52%, 발표일 -63%, 현재 -86.3%다. 같은 회사의 2011 논지는 [별도 정본](ideas/2011/2011-09-15_AIMIA_long.md)에 있다.

## 구조화 데이터

- `data/curated/batch_079_aig_aigws_aim_deep_v7.json`: 10 postmortems, 40 sections, 60 weighted claims, 50 metrics, 80 timeline events, sources.
- `data/curated/batch_079_source_catalog.json`: raw metadata·SQL 성과행. 앱에 직접 로드하지 않는다.
- `analysis/batch_079_aig_aigws_aim_10.md`: Streamlit wrapper.
