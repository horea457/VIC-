# Batch 045 — ePlus / Plus500 / Brink's — V9 Index

> **Research as-of:** 2026-09-09. 첨부 `VIC_IDEAS(4).sql`의 원문·metadata·성과를 기준으로 entity와 direction을 수동 교정했다.

## 0. 배치 결론

이번 10건의 핵심은 종목코드나 raw direction을 그대로 믿으면 투자판정이 뒤집힌다는 점이다. `PLUS`는 미국 ePlus와 영국 Plus500 두 회사가 충돌하고, raw Short 8건 중 실제 Short는 BCO 2014·2018 두 건뿐이다. BCO 성과 multiplier는 실제 Long/Short 방향으로 다시 부호를 계산했다.

## 1. Idea Units

| # | 날짜 | 실제 회사 | raw→연구 방향 | 성과 감사 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2008-06-09 | ePlus inc. | Long→**Long** | DB 없음 | [현금·TBV 할인과 filing/relisting의 마지막 구간을 산 Long](ideas/2008/2008-06-09_PLUS_eplus_long.md) |
| 2 | 2010-02-22 | ePlus inc. | Short→**Long** | DB 없음 | [non-recourse debt를 EV에서 제거한 balance-sheet Long](ideas/2010/2010-02-22_PLUS_eplus_long.md) |
| 3 | 2019-08-26 | Plus500 Ltd. | Short→**Long** | 후속 원문: 2Y 약 +150% total return | [ESMA 후 정상수익과 과도한 규제 공포를 산 contrarian Long](ideas/2019/2019-08-26_PLUS500_long.md) |
| 4 | 2021-09-03 | Plus500 Ltd. | Long→**Long** | DB 없음 | [기존 CFD cash cow와 Invest·US futures 옵션을 함께 산 Long](ideas/2021/2021-09-03_PLUS500_long.md) |
| 5 | 2007-02-12 | The Brink's Company | Short→**Long** | 1Y +3.8% / 3Y -27.4% / 5Y -26.2% | [보안물류+BHS SOTP와 activist value realization Long](ideas/2007/2007-02-12_BCO.md) |
| 6 | 2010-06-13 | The Brink's Company | Short→**Long** | 1Y +33.9% / 3Y +30.9% / 5Y +61.5% | [일시비용 뒤 7~7.5% margin·12.2% FCF yield 정상화 Long](ideas/2010/2010-06-13_BCO.md) |
| 7 | 2012-11-28 | The Brink's Company | Short→**Long** | 1Y +23.3% / 3Y +21.9% / 5Y +217.4% | [NA rationalization·LatAm hidden value·2014 FCF bridge Long](ideas/2012/2012-11-28_BCO.md) |
| 8 | 2014-02-07 | The Brink's Company | Short→**Short** | 1Y +17.5% / 3Y -48.6% / 5Y -151.2% | [13x forward EBIT에 완전한 turnaround가 반영됐다는 Short](ideas/2014/2014-02-07_BCO.md) |
| 9 | 2017-05-12 | The Brink's Company | Short→**Long** | 1Y +22.3% / 3Y -35.2% / 5Y -2.7% | [Doug Pertz 실행력과 peer margin gap closure Long](ideas/2017/2017-05-12_BCO.md) |
| 10 | 2018-05-17 | The Brink's Company | Short→**Short** | 1Y -11.2% / 3Y -17.0% / 5Y null | [완전한 turnaround·LatAm 19.3% margin 기대를 판 Short](ideas/2018/2018-05-17_BCO.md) |

## 2. 기업별 투자논지

### ePlus — balance sheet와 accounting edge

2008년은 cash/TBV와 filing·NASDAQ relisting을 결합한 event Long이고, 2010년은 lease-backed non-recourse notes 때문에 database EV가 $59m 과대계상되는 구조를 교정한 Long이다. 둘 다 사업 방향은 맞았지만 SQL performance row가 없어 exact return은 만들지 않았다.

### Plus500 — 규제 후 cohort economics와 capital return

2019년은 ESMA 이후 실제 네 분기의 AUAC·churn·EEA retail run-rate로 과도한 규제공포를 반박했고, 2년 후 원문이 배당 포함 약 150% 수익을 확인했다. 2021년은 core CFD의 6x P/E와 현금환원 위에 Invest·US futures 옵션을 얹었으나, 2년 double은 SQL price row가 없어 미확정이다.

### Brink's — 같은 기업, 서로 다른 expectations

2007 SOTP Long은 분리 촉매를 맞혔지만 common 장기수익은 부진했다. 2010 normalization Long과 2012 self-help/LatAm Long은 성과가 좋았고 특히 2012는 2년 -19% drawdown 뒤 5년 +217%였다. 2014 Short는 1년만 성공하고 regime change 뒤 큰 손실, 2017 Long은 1~2년 성공 뒤 COVID 경로로 소멸, 2018 Short는 2년 pandemic 수익을 thesis 성공으로 오인하면 안 된다.

## 3. 배치 공통 교훈

1. **Entity resolution이 valuation보다 먼저다.** ticker collision은 exchange·company name·원문 business description으로 해소한다.
2. **Direction은 action/payoff로 검증한다.** raw flag가 틀리면 return과 verdict 부호가 모두 뒤집힌다.
3. **Event 성공과 주식 성공은 다르다.** BHS spin이나 NASDAQ relisting이 일어나도 target price/IRR은 별도다.
4. **Margin gap은 사람과 기간의 함수다.** 현재 team의 실패를 영구 구조로 외삽한 2014 Short는 새 CEO 뒤 무너졌다.
5. **Short는 cover rule이 논지 일부다.** BCO 2014·2018처럼 horizon에 따라 +17%에서 -151%, +40%에서 -17%로 바뀐다.
6. **SQL 값이 없으면 비워 둔다.** 공시상 장기 기업성공을 특정 기간 투자수익으로 대체하지 않는다.

## 4. 데이터·앱 산출물

- DB payload: `data/curated/batch_045_eplus_plus500_brinks_deep_v7.json`
- Streamlit wrapper: `analysis/batch_045_eplus_plus500_brinks_10.md`
- 원문: `data/source_batch045/`
- Builder: `scripts/45_build_batch_045_v9.py`

## 5. 검증 기준

각 보고서는 0~12절, 6개 claim/100% weight, 5개 핵심 metric, 최소 6개 event, 원문+공식자료 source를 포함한다. Payload와 문서의 direction·return·verdict를 동일하게 유지한다.
