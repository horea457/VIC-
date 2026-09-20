# Accredited Mortgage Loan REIT Trust Preferred (AHHAP) — 2012-02-29 VIC Long

> **Idea unit:** 9.75% Series A Perpetual Cumulative Preferred Shares liquidation Long.  
> **Research as-of:** 2026-09-20. Source SQL `is_short=true`; original write-up is explicitly an **asset liquidation Long** and is corrected.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| Security | Accredited Mortgage Loan REIT Trust 9.75% Series A Preferred / AHHAP |
| VIC 게시일 / 작성자 | 2012-02-29 / GideonMagnus |
| 실제 방향 | **Long** |
| entry | 약 **$6.00/share** |
| original remaining liquidation value | **$6.64~$8.37/share** |
| upside estimated | **11%~40%** |
| key assets | LEND bankruptcy claims + mortgage securitization bonds/residuals |
| distributions before VIC date | 약 **$38.89m**, ~**$9.50/share** |
| total aggregate liquidation distributions by Dec-2016 | **$19.27/share** |
| estimated post-VIC distributions | 약 **$9.77/share** |
| price-only/cash recovery vs $6 entry | 약 **+62.8%** |
| 최종 판정 | **강한 성공 — actual remaining cash distributions exceeded original high-case** |

> **결론:** 이 글은 price chart가 아니라 **bankruptcy claims waterfall + residual cash flows**를 재구성한 liquidation underwriting이다. 2012-02-29 이후 받을 수 있는 remaining value를 $6.64~8.37로 봤는데, 최종 aggregate distribution $19.27/share에서 VIC 이전 두 차례 분배 약 $9.50/share를 빼면 이후 지급액은 약 **$9.77/share**다. $6 entry 대비 약 **+63%**로 original high case보다도 높았다.

---

## 1. 원문 투자논지

AHHAP는 listed operating company가 아니었고 common stock도 이미 extinguished됐다. 가치의 원천은 두 가지였다.

1. **Accredited Home Lenders (LEND) bankruptcy claims**
2. **mortgage securitization bonds and residual interests**

작성자는 2011-03-31 balance sheet, bankruptcy docket, tax refund, trust cash, residual payments를 한 줄씩 업데이트한 뒤 professional fees와 litigation cost를 차감했다.

이 방식은 liquidation security 분석의 정석에 가깝다.

---

## 2. 원문 계산

- total estimated value: **$65.715m~$73.165m**
- 이미 지급된 distributions: **$38.89m**
- remaining value: **$27.195m~$34.275m**
- preferred shares outstanding: **4.094m**
- remaining liquidation value: **$6.64~$8.37/share**
- recent price: **$6.00**

---

## 3. 실제 liquidation 결과

2014-10-21 회사는 partial liquidating distribution **$1.25/share**를 발표했고, 그 지급 후 plan-confirmation 이후 누적 distributions는 **$17.25/share**가 됐다.

2016-09-30에는 $1.96/share “final” distribution을 발표해 누적 **$19.21/share**가 되었고, 이후 비용이 예상보다 적어 2016-11-16 추가 **$0.07/share**를 발표했다.

최종 누적 distribution:

**$19.27/share**

VIC 글 시점 이전 두 distributions의 총액 $38.89m ÷ 4.094m ≈ **$9.50/share**이므로, 글 이후 받은 cash는 약:

**$19.27 - $9.50 = $9.77/share**

$6 entry 대비:

**$9.77 / $6 - 1 ≈ +62.8%**

---

## 4. 왜 성공했나

### ① Security-level claim mapping
회사 전체 EV가 아니라 preferred가 **어떤 estate claim을 얼마나 소유하는가**를 계산했다.

### ② 이미 현금화된 자산과 추정자산을 분리했다
세금환급·현금은 high confidence, mortgage residuals는 low confidence로 나눴다.

### ③ 이전 distributions를 valuation에서 차감했다
“누적 배당이 컸다”는 착시를 피하고 **신규 매수자가 앞으로 받을 돈만** 계산했다.

---

## 5. 재사용 가능한 Liquidation 식

**Remaining liquidation value/share = (cash + claim recoveries + realizable assets - fees - taxes - litigation - prior distributions) / remaining shares**

핵심은 total historical distribution이 아니라 **purchase date 이후 남은 waterfall**이다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Direction metadata | raw Short → **Long correction** |
| Claim mapping | 매우 성공 |
| Residual-asset conservatism | 성공 |
| Timing | 예상보다 느림 |
| Final recovery | 강한 성공 |
| Thesis score | **9.6/10** |
| Process score | **10/10** |

### 한 문장 교훈

> **liquidation 투자에서는 “회사에 얼마가 남나”보다 “내 security가 오늘 이후 waterfall에서 얼마를 받나”가 전부다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2012-02-29.
2. 2014 partial liquidation distribution: https://www.prnewswire.com/news-releases/accredited-mortgage-loan-reit-trust-adopts-plan-of-liquidation-and-declares-special-distribution-183494872.html
3. 2016 $1.96 distribution / aggregate $19.21: https://www.prnewswire.com/news-releases/accredited-mortgage-loan-reit-trust-declares-final-liquidating-distribution-300337085.html
4. 2016 additional $0.07 / aggregate $19.27: https://www.prnewswire.com/news-releases/accredited-mortgage-loan-reit-trust-declares-final-liquidating-distribution-300364633.html

### 데이터 품질
- T0 thesis: **A**
- company distributions: **A-/B+ (issuer press releases)**
- return calculation: **A-**, directly reconciled to share count and pre/post idea distributions
