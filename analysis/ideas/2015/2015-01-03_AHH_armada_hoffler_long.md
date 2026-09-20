# Armada Hoffler Properties (AHH) — 2015-01-03 VIC Long

> **Idea unit:** Armada Hoffler Properties common equity Long.  
> **Research as-of:** 2026-09-20. Source SQL Long and actual direction agree.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Armada Hoffler Properties / AHH |
| VIC 게시일 / 작성자 | 2015-01-03 / jhu2000 |
| actual direction | Long |
| next-day close in source DB | **$6.37054** |
| original dividend yield | **6.75%** |
| original implied cap rate | **8.8%** |
| estimated discount to fair value | **>20%** |
| portfolio mix | 약 40% office / 40% retail / 20% multifamily |
| key edge | internal construction + development platform |
| source DB 1Y / 2Y / 3Y / 5Y price factor | **+14.75% / +71.63% / +91.45% / +146.04%** |
| 2024 normalized FFO | **$1.29/share** |
| 2024 stabilized occupancy | **96.0%** |
| 최종 판정 | **매우 강한 성공 — cheap REIT + internal development economics가 장기간 실현** |

> **결론:** 원문은 단순히 high-yield REIT를 산 것이 아니라, **stabilized portfolio를 8.8% cap rate로 싸게 사고 자체 construction/development 조직이 개발이익을 내부화한다**는 구조를 샀다. source DB 기준 5년 price return만 약 +146%로, 배당을 제외해도 매우 강한 성공이다.

---

## 1. 원문 투자논지

AHH는 2013년 $11.50에 IPO한 뒤 큰 폭으로 할인되어 있었다. 글은 다음을 봤다.

- stabilized portfolio occupancy 95%+
- office / retail / multifamily의 diversification
- Mid-Atlantic 지역 exposure
- third-party construction business
- 자체 개발을 통해 **development cost와 stabilized market value의 spread**를 주주가 가져가는 구조
- 6.75% dividend yield
- 8.8% implied cap rate

즉 REIT NAV discount와 development platform value를 동시에 산 아이디어다.

---

## 2. Source DB Performance

Source SQL performance row는 이번 Batch 77에서 유일하게 존재한다.

| Horizon | factor | price return |
|---|---:|---:|
| 1W | 1.0444 | +4.44% |
| 1M | 1.1054 | +10.54% |
| 3M | 1.1138 | +11.38% |
| 6M | 1.0706 | +7.06% |
| 1Y | 1.1475 | **+14.75%** |
| 2Y | 1.7163 | **+71.63%** |
| 3Y | 1.9145 | **+91.45%** |
| 5Y | 2.4604 | **+146.04%** |

배당을 포함하지 않은 price factor라면 total return은 더 높다.

---

## 3. 장기 사업 검증

2024년 AHH는:
- normalized FFO **$118.9m / $1.29 per diluted share**
- stabilized portfolio occupancy **96.0%**
- property NOI **$171.0m**, +6.8%
- annual dividends declared **$0.82/share**, +5.8%

를 기록했다.

2025에는 higher-rate/deleveraging pressure로 normalized FFO가 $1.08/share로 낮아졌지만 stabilized occupancy는 95.3%로 유지됐다. 즉 original asset-quality thesis는 장기간 유효했고, 이후 금리와 capital structure가 새 변수로 들어왔다.

---

## 4. 왜 성공했나

### ① Entry cap rate가 margin of safety였다
8.8% implied cap rate는 좋은 occupancy를 가진 diversified portfolio 대비 높았다.

### ② Internal development가 hidden operating asset이었다
REIT를 단순 asset owner가 아니라 **land/development/construction → stabilized NOI** conversion machine으로 봤다.

### ③ 배당이 기다리는 비용을 낮췄다
rerating timing이 불확실해도 6%대 cash yield가 carry를 제공했다.

---

## 5. 재사용 가능한 REIT 식

**NAV return = starting NOI yield + same-store NOI growth + development value creation - financing cost change ± cap-rate rerating**

개발형 REIT는 추가로:

**Development spread = stabilized NOI / total development cost - market cap rate**

를 봐야 한다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| NAV discount thesis | 성공 |
| Development platform | 성공 |
| Dividend carry | 성공 |
| 1Y outcome | 성공 |
| 2~5Y outcome | 매우 강한 성공 |
| Thesis score | **9.5/10** |
| Process score | **9.9/10** |

### 한 문장 교훈

> **개발형 REIT는 cap rate만 보지 말고, 내부 조직이 개발원가를 stabilized NAV로 바꾸며 만드는 spread를 별도 사업으로 평가해야 한다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2015-01-03.
2. Source SQL performance row, idea_id `ac82ff51-c8fb-4c3e-b57e-e38d5bd9feaa`.
3. Armada Hoffler 2024 Annual Report: https://ir.armadahoffler.com/static-files/4205e942-fb15-4f46-bd7d-21c41426a882
4. 2025 Form 10-K / SEC: https://www.sec.gov/Archives/edgar/data/1569187/000156918726000021/ahh-20251231.htm

### 데이터 품질
- T0 thesis: **A**
- source performance: **A (database row)**
- company results: **A**
