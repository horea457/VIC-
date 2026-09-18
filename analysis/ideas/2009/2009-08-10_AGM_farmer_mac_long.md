# Federal Agricultural Mortgage / Farmer Mac (AGM) — 2009-08-10 VIC Long

> **Idea unit:** 2009-08-10 Farmer Mac common equity Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 원문은 명백한 **Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Federal Agricultural Mortgage Corp. / AGM |
| VIC 게시일 / 작성자 | 2009-08-10 / carbone959 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 가격 수준 | 약 **$8** |
| 핵심 논지 | legacy toxic assets 정리 + core ag/rural finance earnings 정상화 |
| 원문 core annual earnings | **$15~20m** |
| 원문 implied equity value | **$150m+** |
| 2009 core earnings | 약 **$16.1m** |
| 2010 core earnings | 약 **$25.4m** |
| 2011 core earnings | 약 **$42.9m** |
| SQL 1Y | **+64.0%** |
| SQL 2Y | **+116.1%** |
| SQL 3Y | **+211.7%** |
| SQL 5Y | **+295.4%** |
| 최종 판정 | **매우 강한 성공 — toxic-assets reset 뒤 core earnings 정상화와 rerating** |

> **결론:** 원문은 Farmer Mac이 Fannie/Freddie preferreds와 Lehman exposure, ethanol lending 같은 비핵심 손실 때문에 2008 위기에서 망가졌지만, 핵심 농업·농촌금융 franchise 자체는 건전하다고 봤다. toxic assets를 털고 자본을 확충한 뒤 core earnings가 연 $15~20m만 회복해도 당시 시총 대비 큰 upside가 있다는 논리였다. 실제 core earnings는 2009 $16.1m, 2010 $25.4m, 2011 $42.9m으로 빠르게 증가했고 source DB 기준 5년 주가는 약 **+295%**였다.

---

## 1. 무엇이 망가졌던 것인가

2008 위기의 핵심은 core agricultural-credit franchise보다:
- Fannie/Freddie preferred securities,
- Lehman bonds,
- ethanol lending,
- capital impairment

이었다.

원문은 새 경영진, capital raise, bad-asset cleanup 이후 **core franchise와 crisis losses를 분리**했다.

---

## 2. Claim Map

### C1. core earnings $15~20m은 유지 가능 — **강한 성공**
2009 core earnings 약 $16.1m으로 원문 범위에 들어왔고 이후 훨씬 커졌다.

### C2. bad assets 제거 후 earnings visibility가 높아진다 — **성공**
2010~11 core earnings가 빠르게 성장했다.

### C3. 당시 market cap은 core franchise를 지나치게 낮게 평가 — **강한 성공**
1Y +64%, 2Y +116%, 5Y +295%.

### C4. rural utilities expansion — **성공 방향**
사업 범위가 농업 mortgage 외 rural infrastructure finance로 확대됐다.

### C5. capital survival — **강한 성공**
GSE-like platform이 정상 영업을 지속했다.

---

## 3. Source SQL Performance

| Horizon | Multiple | Return |
|---|---:|---:|
| 1W | 0.9112x | -8.9% |
| 2W | 1.0177x | +1.8% |
| 1M | 1.0047x | +0.5% |
| 3M | 1.1006x | +10.1% |
| 6M | 0.8343x | -16.6% |
| 1Y | 1.6401x | **+64.0%** |
| 2Y | 2.1607x | **+116.1%** |
| 3Y | 3.1169x | **+211.7%** |
| 5Y | 3.9538x | **+295.4%** |

---

## 4. Forecast vs Actual

| 지표 | 원문 | 실제 |
|---|---:|---:|
| core annual earnings | $15~20m | 2009 $16.1m |
| next normalization | gradual | 2010 $25.4m |
| further earning power | not fully underwritten | 2011 $42.9m |
| stock | high-teens worth | multi-year rerating far beyond |

원문은 오히려 earnings recovery의 크기를 보수적으로 봤다.

---

## 5. 무엇이 수익을 만들었는가

이번 case의 본질은:
1. **one-off toxic assets 제거**
2. **core credit franchise 생존**
3. **capital adequacy 회복**
4. **earnings normalization**
5. **multiple rerating**

이었다.

---

## 6. 재사용 가능한 교훈

1. 금융사 crisis에서 core franchise와 securities-loss book을 분리한다.
2. tangible capital reset 이후 normalized earnings를 다시 계산한다.
3. 비핵심 asset impairment는 이미 손실 처리됐으면 future earnings를 오히려 깨끗하게 만들 수 있다.
4. distress equity는 survival만 하면 denominator recovery가 매우 클 수 있다.
5. source DB performance가 있으면 narrative return보다 이를 우선한다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Core-franchise thesis | 강한 성공 |
| Earnings normalization | 매우 강한 성공 |
| Capital-survival thesis | 성공 |
| Security outcome | 매우 강한 성공 |
| Thesis score | 9.8/10 |
| Process score | 9.8/10 |
| 종합 | **매우 강한 성공 — 5Y +295.4%** |

### 한 문장 교훈

> crisis 금융주에서 최고의 Long은 **손실 난 자산이 아니라 손실을 털고도 남아 있는 core earnings engine을 사는 것**이다.

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2009-08-10.
2. Source SQL performance row.
3. Farmer Mac 2009–2011 filings / core-earnings disclosures.

### 데이터 품질
- T0 thesis: **A**
- source performance: **A within DB**
- core earnings: **A/B**
