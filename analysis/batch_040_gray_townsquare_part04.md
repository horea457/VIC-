# Gray Television — 2020-11-05 GTN VIC postmortem

<!-- idea:c04d46ad-018a-4fc1-8064-600b88e01894 -->

**Research direction:** Long  
**Raw SQL is_short:** `false`  
**Verdict:** 강한 단기 성공  
**Idea ID:** `c04d46ad-018a-4fc1-8064-600b88e01894`

## 1. 결론부터
강한 단기 성공: 정치광고는 추정이 아니라 이미 계약되거나 수취된 물량 비중이 높아 near-term earnings visibility가 컸다. ‘일회성’이라는 이유만으로 현금가치를 무시한 시장의 오류를 이용한 사례다.

## 2. 원 투자논지
2020년 11월 대선 직후 Gray의 정치광고 수입이 기존 가이던스를 크게 상회하고 조지아 상원 결선이라는 추가 이벤트까지 열릴 수 있다는 단기 Long이었다. 기존 장기 thesis보다 이벤트성 cash windfall에 초점을 맞췄다.

## 3. 사업과 돈의 흐름
Gray는 local/national 광고, 정치광고, retransmission/distribution, digital에서 현금을 만든다. 방송국 고정비가 높기 때문에 incremental retrans·political revenue의 현금전환율이 높지만 network reverse compensation과 부채이자까지 차감한 순 FCF를 봐야 한다.

## 4. 핵심 가정
순 retrans 성장과 정치광고 cycle cash가 인수 후 debt service를 충분히 커버하고, M&A synergies가 실제 FCF/share로 이어져야 한다. headline EBITDA가 아니라 leverage와 reverse retrans까지 함께 검증해야 한다.

## 5. 실제 전개
Gray의 2020년 방송 매출은 $2.32bn, 총매출은 $2.381bn으로 2019 대비 증가했고 정치광고가 매우 강했다. 원 DB performance상 1년 성과 배수는 약 1.60x였다. 이후 2021년에는 Quincy·Meredith 인수로 회사가 다시 구조적으로 커졌다.

## 6. 주장별 검증
정치광고는 추정이 아니라 이미 계약되거나 수취된 물량 비중이 높아 near-term earnings visibility가 컸다. ‘일회성’이라는 이유만으로 현금가치를 무시한 시장의 오류를 이용한 사례다. 원 DB의 사후 성과배수는 사업논지와 security outcome을 분리해서 판단하는 보조지표로만 사용했다.

## 7. 핵심 수치
2020 total revenue=2.381 USD bn; 2020 broadcasting revenue=2.32 USD bn; oneYearPerf=1.5959422114947353 x; 2021 total revenue=2.413 USD bn

## 8. 촉매와 타임라인
2020-11-05 VIC Long 게시 → 2020-11-30 대선 광고 수취 구간 → 2021-01-05 Georgia Senate runoff → 2021-02-25 FY2020 실적 → 2021-08-02 Quincy 완료 → 2021-12-01 Meredith 완료

## 9. 반증조건
결선/정치광고 매출이 취소되거나 이미 주가에 완전히 반영되어 incremental FCF가 valuation gap을 만들지 못하면 실패였다.

## 10. 재사용 가능한 교훈
이벤트 광고는 반복가능 성장률로 외삽하면 안 되지만, 이미 계약된 incremental FCF를 0으로 평가하는 것도 오류다. cycle-adjusted base와 event cash를 분리해 가치화해야 한다.

## Weighted claims
- **20% · direction** — raw SQL과 실제 VIC 방향 모두 Long.
- **18% · thesis** — 2020년 11월 대선 직후 Gray의 정치광고 수입이 기존 가이던스를 크게 상회하고 조지아 상원 결선이라는 추가 이벤트까지 열릴 수 있다는 단기 Long이었다. 기존 장기 thesis보다 이벤트성 cash windfall에 초점을 맞췄다.
- **17% · development** — Gray의 2020년 방송 매출은 $2.32bn, 총매출은 $2.381bn으로 2019 대비 증가했고 정치광고가 매우 강했다. 원 DB performance상 1년 성과 배수는 약 1.60x였다. 이후 2021년에는 Quincy·Meredith 인수로 회사가 다시 구조적으로 커졌다.
- **16% · verdict** — 정치광고는 추정이 아니라 이미 계약되거나 수취된 물량 비중이 높아 near-term earnings visibility가 컸다. ‘일회성’이라는 이유만으로 현금가치를 무시한 시장의 오류를 이용한 사례다.
- **15% · falsification** — 결선/정치광고 매출이 취소되거나 이미 주가에 완전히 반영되어 incremental FCF가 valuation gap을 만들지 못하면 실패였다.
- **14% · lesson** — 이벤트 광고는 반복가능 성장률로 외삽하면 안 되지만, 이미 계약된 incremental FCF를 0으로 평가하는 것도 오류다. cycle-adjusted base와 event cash를 분리해 가치화해야 한다.

## Metrics
| Metric | Value | Source note |
|---|---:|---|
| 2020 total revenue | 2.381 USD bn | SEC |
| 2020 broadcasting revenue | 2.32 USD bn | SEC |
| oneYearPerf | 1.5959422114947353 x | raw SQL performance |
| 2021 total revenue | 2.413 USD bn | SEC |

## Timeline
| Date | Event | Detail |
|---|---|---|
| 2020-11-05 | VIC Long 게시 | 정치광고 beat와 GA runoff 옵션 |
| 2020-11-30 | 대선 광고 수취 구간 | 계약된 정치광고의 현금화 |
| 2021-01-05 | Georgia Senate runoff | 추가 정치광고 이벤트 |
| 2021-02-25 | FY2020 실적 | 매출 확대 확인 |
| 2021-08-02 | Quincy 완료 | 다시 M&A 모드 |
| 2021-12-01 | Meredith 완료 | 장기 thesis는 leverage 중심으로 전환 |

## Primary sources
1. [Gray 2014 investor materials / record FCF](https://www.sec.gov/Archives/edgar/data/43196/000119312515126296/d906196dex991.htm)
2. [Gray-Raycom transaction presentation](https://www.sec.gov/Archives/edgar/data/43196/000119312518201705/d792370dex992.htm)
3. [Gray Q1 2019 results](https://www.sec.gov/Archives/edgar/data/43196/000143774919009037/ex_143560.htm)
4. [Gray FY2020 earnings release](https://www.sec.gov/Archives/edgar/data/43196/000143774921004020/ex_229644.htm)
5. [Gray 2021 10-K](https://www.sec.gov/Archives/edgar/data/43196/000143774922004412/gtn20211231_10k.htm)
6. [Gray 2022 10-K](https://www.sec.gov/Archives/edgar/data/43196/000143774923004505/gtn20221231_10k.htm)

## 원문 메타데이터 보존
SQL의 raw `is_short` 값은 수정하지 않았다. 방향 오류가 있는 경우 research layer의 `research_direction_ko`만 Long으로 교정했다. 이 배치는 original description/catalyst를 방향 판정의 기준으로 사용하고, 사후검증은 SEC/회사 1차자료를 우선했다.
