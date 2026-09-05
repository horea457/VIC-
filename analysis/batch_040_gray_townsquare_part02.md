# Gray Television — 2018-08-03 GTN VIC postmortem

<!-- idea:d1676bbe-336d-4469-ae76-99336672a57e -->

**Research direction:** Long  
**Raw SQL is_short:** `true`  
**Verdict:** 성공  
**Idea ID:** `d1676bbe-336d-4469-ae76-99336672a57e`

## 1. 결론부터
성공: 거래가 무산되지 않았고 synergy·scale 논리가 실적에 반영됐다. 다만 ‘좋은 인수’의 성공을 곧바로 ‘낮은 위험’으로 해석하면 안 됐다. 부채가 높은 구조는 이후 더 큰 M&A를 할 때 equity discount의 원인이 됐다.

## 2. 원 투자논지
2018년 Raycom 인수가 약 $3.55bn EV, year-1 synergy $80m, NOL 가치까지 감안한 7.5x 내외의 경제성으로 FCF/share를 크게 늘릴 것이라는 Long이었다. 높은 pro forma leverage는 인정하되, #1/#2 방송국 포트폴리오와 retrans 스케일이 이를 흡수한다고 봤다.

## 3. 사업과 돈의 흐름
Gray는 local/national 광고, 정치광고, retransmission/distribution, digital에서 현금을 만든다. 방송국 고정비가 높기 때문에 incremental retrans·political revenue의 현금전환율이 높지만 network reverse compensation과 부채이자까지 차감한 순 FCF를 봐야 한다.

## 4. 핵심 가정
순 retrans 성장과 정치광고 cycle cash가 인수 후 debt service를 충분히 커버하고, M&A synergies가 실제 FCF/share로 이어져야 한다. headline EBITDA가 아니라 leverage와 reverse retrans까지 함께 검증해야 한다.

## 5. 실제 전개
Raycom 거래는 실제로 완료되었고 2019년 1Q 매출은 Raycom 기여로 전년 대비 129% 증가했다. 2019년 3월 leverage ratio는 4.86x였지만 통합 후 기록적인 broadcast cash flow가 확인됐다. 원 DB 기준 3년 성과 배수는 약 1.50x로, 단기 변동성은 있었지만 thesis의 방향은 맞았다.

## 6. 주장별 검증
거래가 무산되지 않았고 synergy·scale 논리가 실적에 반영됐다. 다만 ‘좋은 인수’의 성공을 곧바로 ‘낮은 위험’으로 해석하면 안 됐다. 부채가 높은 구조는 이후 더 큰 M&A를 할 때 equity discount의 원인이 됐다. 원 DB의 사후 성과배수는 사업논지와 security outcome을 분리해서 판단하는 보조지표로만 사용했다.

## 7. 핵심 수치
Raycom enterprise value=3.547 USD bn; year-1 synergies=80 USD m; Q1 2019 revenue growth=129 percent; threeYearPerf=1.500986056330204 x

## 8. 촉매와 타임라인
2018-06-25 Raycom 인수 발표 → 2018-08-03 VIC Long 게시 → 2019-01-02 Raycom 거래 완료 → 2019-05-08 Q1 record results → 2020-12-31 정치광고 강세 연도 → 2022-12-31 부채 $6.455bn

## 9. 반증조건
Raycom 통합 비용이 $80m synergy를 장기간 상쇄하거나, 광고침체와 reverse retrans 상승 때문에 pro forma FCF/share accretion이 사라지면 실패였다.

## 10. 재사용 가능한 교훈
방송 M&A는 headline multiple보다 divestiture 후 purchase multiple, year-1 synergy의 성격, 그리고 2년 평균 FCF/순부채 감소를 추적해야 한다.

## Weighted claims
- **20% · direction** — raw SQL Short와 달리 실제 VIC 방향은 Long.
- **18% · thesis** — 2018년 Raycom 인수가 약 $3.55bn EV, year-1 synergy $80m, NOL 가치까지 감안한 7.5x 내외의 경제성으로 FCF/share를 크게 늘릴 것이라는 Long이었다. 높은 pro forma leverage는 인정하되, #1/#2 방송국 포트폴리오와 retrans 스케일이 이를 흡수한다고 봤다.
- **17% · development** — Raycom 거래는 실제로 완료되었고 2019년 1Q 매출은 Raycom 기여로 전년 대비 129% 증가했다. 2019년 3월 leverage ratio는 4.86x였지만 통합 후 기록적인 broadcast cash flow가 확인됐다. 원 DB 기준 3년 성과 배수는 약 1.50x로, 단기 변동성은 있었지만 thesis의 방향은 맞았다.
- **16% · verdict** — 거래가 무산되지 않았고 synergy·scale 논리가 실적에 반영됐다. 다만 ‘좋은 인수’의 성공을 곧바로 ‘낮은 위험’으로 해석하면 안 됐다. 부채가 높은 구조는 이후 더 큰 M&A를 할 때 equity discount의 원인이 됐다.
- **15% · falsification** — Raycom 통합 비용이 $80m synergy를 장기간 상쇄하거나, 광고침체와 reverse retrans 상승 때문에 pro forma FCF/share accretion이 사라지면 실패였다.
- **14% · lesson** — 방송 M&A는 headline multiple보다 divestiture 후 purchase multiple, year-1 synergy의 성격, 그리고 2년 평균 FCF/순부채 감소를 추적해야 한다.

## Metrics
| Metric | Value | Source note |
|---|---:|---|
| Raycom enterprise value | 3.547 USD bn | SEC |
| year-1 synergies | 80 USD m | SEC |
| Q1 2019 revenue growth | 129 percent | SEC |
| threeYearPerf | 1.500986056330204 x | raw SQL performance |

## Timeline
| Date | Event | Detail |
|---|---|---|
| 2018-06-25 | Raycom 인수 발표 | 약 $3.55bn EV |
| 2018-08-03 | VIC Long 게시 | FCF/share accretion thesis |
| 2019-01-02 | Raycom 거래 완료 | 통합 시작 |
| 2019-05-08 | Q1 record results | 매출 129% 증가 |
| 2020-12-31 | 정치광고 강세 연도 | cycle cash generation 확인 |
| 2022-12-31 | 부채 $6.455bn | 후속 M&A까지 포함한 leverage risk |

## Primary sources
1. [Gray 2014 investor materials / record FCF](https://www.sec.gov/Archives/edgar/data/43196/000119312515126296/d906196dex991.htm)
2. [Gray-Raycom transaction presentation](https://www.sec.gov/Archives/edgar/data/43196/000119312518201705/d792370dex992.htm)
3. [Gray Q1 2019 results](https://www.sec.gov/Archives/edgar/data/43196/000143774919009037/ex_143560.htm)
4. [Gray FY2020 earnings release](https://www.sec.gov/Archives/edgar/data/43196/000143774921004020/ex_229644.htm)
5. [Gray 2021 10-K](https://www.sec.gov/Archives/edgar/data/43196/000143774922004412/gtn20211231_10k.htm)
6. [Gray 2022 10-K](https://www.sec.gov/Archives/edgar/data/43196/000143774923004505/gtn20221231_10k.htm)

## 원문 메타데이터 보존
SQL의 raw `is_short` 값은 수정하지 않았다. 방향 오류가 있는 경우 research layer의 `research_direction_ko`만 Long으로 교정했다. 이 배치는 original description/catalyst를 방향 판정의 기준으로 사용하고, 사후검증은 SEC/회사 1차자료를 우선했다.
