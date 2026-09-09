# Batch 054 — Office Depot / Boca Resorts / Rosetta Stone V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 053 마지막 ODP 2007-03-22 이후, 이미 reviewed된 idea_id를 제외한 다음 10건.
> **핵심 품질 이슈:** raw direction 오류 8건 + ticker/entity collision 1건.

---

## 1. Canonical Idea Units

| # | 날짜 | Raw ticker | Raw 회사 | Raw 방향 | 실제 투자대상 / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|---|
| 1 | 2007-12-27 | ODP | Office Depot | **Short** | Office Depot **Long** | [ODP 2007-12](ideas/2007/2007-12-27_ODP_long.md) | **강한 실패** — normalized margin trap |
| 2 | 2014-04-05 | ODP | Office Depot | **Short** | Office Depot **Long** | [ODP 2014](ideas/2014/2014-04-05_ODP_long.md) | **강한 전술 성공** — synergy/target 적중, 최종 merger는 FTC 차단 |
| 3 | 2018-08-13 | ODP | Office Depot | **Short** | Office Depot **Long** | [ODP 2018](ideas/2018/2018-08-13_ODP_long.md) | **운영 thesis 실패** — CompuCom transformation 붕괴 |
| 4 | 2019-04-22 | ODP | Office Depot | **Short** | Office Depot **Long** | [ODP 2019](ideas/2019/2019-04-22_ODP_long.md) | **성공 방향** — B2B SOTP / asset action |
| 5 | 2021-01-19 | ODP | Office Depot | **Short** | The ODP Corp. **Long** | [ODP 2021](ideas/2021/2021-01-19_ODP_long.md) | **부분 성공** — CompuCom salvage 적중, full $80 crystallization 미완 |
| 6 | 2002-04-07 | RST | **Rosetta Stone** | Long | **Boca Resorts Long** | [Boca Resorts 2002](ideas/2002/2002-04-07_RST_boca_resorts_long.md) | **강한 성공** — $12.85 → Blackstone $24 cash |
| 7 | 2010-01-04 | RST | Rosetta Stone | Short | Rosetta Stone **Short** | [RST 2010 Short](ideas/2010/2010-01-04_RST_short.md) | **강한 성공** — CAC/saturation 적중 |
| 8 | 2011-08-23 | RST | Rosetta Stone | **Short** | Rosetta Stone **Long** | [RST 2011 Long](ideas/2011/2011-08-23_RST_long.md) | **강한 실패** — EV/Sales·cash가 unit economics를 못 막음 |
| 9 | 2013-03-25 | RST | Rosetta Stone | **Short** | Rosetta Stone **Long** | [RST 2013 Long](ideas/2013/2013-03-25_RST_long.md) | **운영 thesis 실패** — $35m+ FCF 예상 vs actual -$0.9m |
| 10 | 2018-09-08 | RST | Rosetta Stone | **Short** | Rosetta Stone **Long** | [RST 2018 Long](ideas/2018/2018-09-08_RST_long.md) | **강한 성공** — Lexia SOTP → $30 cash takeout |

---

## 2. Metadata / Direction Audit

이번 batch는 raw metadata를 그대로 사용하면 분석 자체가 뒤집힌다.

### 방향 오류 8건

| Idea | Raw | 실제 | 원문 근거 |
|---|---|---|---|
| ODP 2007-12 | Short | **Long** | $13.60에서 $23~32 target / 70~135% upside |
| ODP 2014-04 | Short | **Long** | $7.25/share fair value |
| ODP 2018-08 | Short | **Long** | conservative case도 30%+ IRR |
| ODP 2019-04 | Short | **Long** | $2.40에서 23~25% FCFE yield / B2B SOTP |
| ODP 2021-01 | Short | **Long** | Staples $40 bid 이후에도 SOTP ~$80 |
| RST 2011-08 | Short | **Long** | “less than 50% of what business is worth”, target $40 |
| RST 2013-03 | Short | **Long** | target $23~25, downside $12 |
| RST 2018-09 | Short | **Long** | Lexia alone > current EV, 50~100%+ upside |

### 방향이 맞는 2건
- Boca Resorts 2002: raw Long = actual Long.
- Rosetta Stone 2010: raw Short = actual Short.

### Entity collision 1건
2002 ticker **RST**는 Rosetta Stone이 아니라 **Boca Resorts, Inc.**

따라서 raw table의 company_name은 원본 보존하되 canonical/overlay에서는 actual entity를 별도 교정한다.

---

# PART A — OFFICE DEPOT: 같은 저평가주에서 valuation framework가 어떻게 바뀌었나

## 3. ODP 2007-12 — 가격이 70% 빠져도 정상화 이익이 틀리면 실패한다

### 당시 상황
- stock ~$13.60
- prior high >$46
- headline valuation: 8x 2006 EPS / <10x forward
- writer는 2008 slowdown을 지나 2009~10 margin recovery를 예상

### 원문 2009 model
- sales $16.5bn
- operating margin 5.0%
- EPS $1.94
- 12~15x → $23.25~29.06

### 원문 2010 model
- sales $17.325bn
- operating margin 5.2%
- EPS $2.17
- 12~15x → $26.03~32.53

### 실제
2008 North American Retail operating profit:
- 2007: **$354.5m**
- 2008: **-$29.2m**

즉 multiple이 아니라 denominator가 무너졌다.

### 실패식
**prior-cycle margin × low multiple → recession → negative operating leverage → EPS collapse**

### 교훈
주가가 70% 빠진 cyclical은 “싸졌다”가 아니라 **정상화 이익을 다시 만들어야 하는 회사**다.

---

## 4. ODP 2014 — 구조적 쇠퇴를 인정하고 supply shrink를 산 성공한 Long

2014 thesis는 2007과 완전히 달랐다.

더 이상:
> Office Depot의 옛 margin이 돌아온다

가 아니었다.

대신:
> **Office Depot + OfficeMax의 비용과 점포 capacity를 revenue보다 빠르게 줄일 수 있다**

였다.

### 핵심 논리
- $600m+ merger synergies
- store overlap 제거
- ODP 최대 450 stores closure 계획
- Staples 225 stores closure
- industry capacity 약 20% 축소 가능
- net cash
- Roland Smith execution

### 실제
- synergy outlook은 $700m+ run-rate로 상향
- 2014에 168 stores closure
- Staples가 2015 ODP에 **$11/share implied value** acquisition agreement 제시
- 원문 fair value $7.25를 크게 상회

### 그러나
FTC가 대형 B2B customer market의 경쟁저하를 이유로 deal을 막아 2016 merger는 무산.

### 판정
- self-help: **성공**
- original target: **성공**
- strategic merger catalyst: **실패**

### 교훈
**Secular decline ≠ 무조건 Short.**
수요 감소보다 공급 capacity가 더 빨리 줄어들면 한동안 earnings/share는 개선될 수 있다.

---

## 5. ODP 2018 — “Cheap retailer → Services company” transformation의 실패

### 원문 재정의
- Retail ~45%
- Business Solutions ~45%
- CompuCom ~10%

ODP는 retailer가 아니라:
**B2B + managed services + omnichannel platform**

이 되어야 한다는 thesis였다.

### 핵심 hidden assumption
2017 약 **$1bn에 인수한 CompuCom**이 transformation engine이 될 것.

### 실제
2018 Q4:
- CompuCom fair value cushion이 carrying value 대비 불과 **4%**

2019:
- CompuCom operating loss
- revenue/profitability shortfall

2021:
- CompuCom를 **최대 $305m**에 매각

### 실패식
**cheap legacy FCF + expensive “strategic” acquisition → low ROIC → value leakage**

### 가장 중요한 교훈
낮은 multiple의 legacy company가 M&A로 성장주가 되려 할 때는:
- sales mix
- TAM
- strategic fit

보다 **incremental ROIC**를 먼저 봐야 한다.

---

## 6. ODP 2019 — 실패한 growth acquisition을 버리자 thesis가 강해졌다

2019 writeup은 2018과 같은 ODP인데 논리가 더 좋아졌다.

### 2018
**CompuCom 성공 → services transformation**

### 2019
**CompuCom이 실패해도 B2B + retail cash flow만으로 싸다**

### 원문 valuation
- price ~$2.40 pre-split
- equity ~$1.3bn
- adjusted EV up to ~$1.685bn
- stress EBITDA ~$500m
- EV/EBITDA ~3.4x
- FCFE ~$300m → 23~25% yield

### B2B
- EBITDA ~$320m
- 7x → $2.24bn EV
- CompuCom/corporate drag 차감 후 equity value ~$3.10/share

### Retail
- ~$250m EBITDA
- current valuation에서 거의 free

### 실제 validation
- 2020: **1-for-10 reverse split**
- 2021: Staples $40 post-split offer = pre-split 약 **$4**
- 2019 $2.40 대비 약 +67%
- 2021: B2B separation 계획
- 2021: CompuCom 최대 $305m 매각

### 교훈
실패한 narrative를 defend하지 않고 **valuation framework를 바꾸는 것**이 중요하다.

---

## 7. ODP 2021 — bidder가 원하는 자산을 역산한 event-driven SOTP

Staples/Sycamore가 $40 cash offer를 제시한 뒤에도 Long.

### 원문 SOTP
| 자산 | 가치 |
|---|---:|
| Retail | ~$20/share |
| CompuCom | ~$6/share |
| B2B | ~$47/share |
| Cash | ~$7/share |
| **합계** | **~$80/share** |

### 특히 잘 맞은 부분
CompuCom:
- 원문 salvage value 약 **$300m**
- 실제 2021 sale: **up to $305m**

2017 $1bn purchase cost가 아니라 **당시 third-party sale value**를 쓴 것이 정확했다.

### 덜 맞은 부분
- B2B standalone spin은 발표됐지만 완결되지 않음
- 2022 회사는 common ownership 유지로 방향 변경
- full $80 crystallization은 확인되지 않음

### 교훈
**announced spin ≠ completed spin.**
event value는 단계별 probability를 적용해야 한다.

---

## 8. ODP 2007 → 2021 thesis 진화

| 시점 | 무엇을 샀나 | 핵심 valuation | 결과 |
|---|---|---|---|
| 2007 | old margin 회복 | P/E / normalized margin | **실패** |
| 2014 | merger cost-out | EBITDA + synergy | **성공** |
| 2018 | services transformation | FCF/LBO + CompuCom | **실패** |
| 2019 | 남는 자산 | B2B SOTP + FCFE yield | **성공 방향** |
| 2021 | asset separation | bidder/SOTP | **부분 성공** |

### 가장 중요한 변화

**Forecasting the company → valuing the assets**

로 갈수록 thesis가 강해졌다.

---

# PART B — RST: ticker collision + Rosetta Stone의 Long/Short 교과서

## 9. Boca Resorts 2002 — public earnings보다 private asset value

2002 RST는 Rosetta Stone이 아니다.

### 원문
- price $12.85
- tangible book $11.67
- normalized cash flow ~$110m
- 9x → enterprise value $990m
- debt $184.4m
- fair value **$20.29/share**
- normalized FCF cap rate ~13.6%

### asset
Boca Raton Resort & Club 등 South Florida trophy resorts.

### 실제
2004 Blackstone affiliate가 **$24/share cash**로 acquisition.

단순 price:
$12.85 → $24 = 약 **+86.8%**

### 성공식
**depressed public earnings + scarce trophy asset + private buyer control value**

---

## 10. Rosetta Stone 2010 Short — 가장 좋은 leading indicator는 CAC였다

### 시장 narrative
- premium brand
- TV marketing
- mall kiosks
- rapid growth
- language-learning TAM

### Short가 본 것
**Revenue = units × AOV**

그런데:
- unit growth 둔화
- bundle로 AOV 상승
- sales & marketing per customer 급증
- US consumer saturation

### 실제
Revenue:
- 2010 $258.9m
- 2011 $268.4m
- 2012 $273.2m

매출은 급락하지 않았다.

그러나 operating income:
- 2010 +$12.9m
- 2011 **-$28.4m**
- 2012 **-$6.0m**

2011 Q4 share low:
**$6.55**

원문 target $12를 크게 하회.

### 교훈
consumer growth stock의 peak는 revenue growth가 0이 될 때보다 **incremental CAC가 먼저 폭증할 때** 보일 수 있다.

---

## 11. Rosetta Stone 2011 Long — Short thesis를 뒤집었지만 unit economics는 안 바뀌었다

### Long 논리
- EV/Sales ~0.6x
- net cash ~$115m
- 80%+ gross margin
- international growth
- subscription mix 15% → 27%
- ReFLEX / TOTALe
- 2013 revenue $400~420m
- 15% EBITDA margin
- target $40

### 문제
2010 Short가 지적했던:
- CAC
- customer saturation
- S&M burden

이 개선됐다는 증거가 부족했다.

### 실제
subscription revenue는 늘었다.
하지만:
- 2011 operating loss **-$28.4m**
- Q4 share low **$6.55**

### 교훈
**High gross margin ≠ good unit economics.**
gross margin 아래 CAC가 크면 80% gross margin도 가치가 없다.

---

## 12. Rosetta Stone 2013 Long — FCF를 썼지만 annualization이 틀렸다

2011 실패 후 management change와 subscription transition을 근거로 다시 Long.

### 원문
- net cash ~$7/share
- 4Q12 FCF ~$22m
- 2013 FCF **$35m+**
- 2014 FCF **$45m+**
- target $23~25
- downside $12

### 실제
- FY2012 FCF $22.1m
- FY2013 FCF **-$0.9m**
- adjusted FCF $7.1m

### 핵심 오류
**seasonal Q4 cash flow를 normalized annual FCF로 외삽**

### 그러나 중요한 예외
2013 Rosetta Stone은 **Lexia를 약 $22.5m에 인수**했다.

이 acquisition은 훗날 company value를 바꾸는 최고의 asset이 된다.

### 교훈
좋은 capital allocation이 나중에 나왔다고 해서 **당시 FCF thesis가 맞았던 것은 아니다.**

---

## 13. Rosetta Stone 2018 Long — narrative가 아니라 distinct asset을 샀다

2018 writeup은 이전 Long들과 질적으로 달랐다.

### 회사 안의 세 자산
1. K-12 Literacy — **Lexia**
2. Enterprise & Education Language
3. Consumer Language

### Lexia
- 2018 bookings ~$60m
- growth 25%+
- 2020 target $100m
- steady-state margin 30~40%
- writer valuation 5~8x sales/bookings

### 핵심 구조
**Lexia alone > whole-company EV**

Lexia valuation:
약 **$22~35/share**

나머지 language businesses는 거의 free option.

### 실제
2019 Literacy revenue:
**$62.6m, +19%**

2020 Cambium/Veritas acquisition:
**$30/share cash**
equity value 약 **$792m**

### 판정
원문의 $22~35 valuation band 안에서 whole company가 실제 takeout.

---

## 14. Rosetta Stone 2010 → 2018: 무엇이 알파를 만들었나

| 시점 | 방향 | 핵심 근거 | 판정 |
|---|---|---|---|
| 2010 | Short | CAC 상승 / unit saturation | **강한 성공** |
| 2011 | Long | low EV/Sales / cash / brand / TAM | **강한 실패** |
| 2013 | Long | SaaS + FCF forecast | **실패** |
| 2018 | Long | Lexia standalone asset value | **강한 성공** |

### 정보의 질 순서

낮은 질:
**TAM → brand → gross margin → EV/Sales**

중간:
**management guidance → FCF forecast**

높은 질:
**CAC / cohort economics / distinct asset revenue / third-party sale value**

이 batch의 가장 큰 학습점이다.

---

# PART C — Cross-Batch Framework

## 15. ODP와 RST가 공통으로 보여주는 것

두 회사 모두 처음에는 “싸 보이는 회사”였다.

그러나 더 좋은 투자논지는 시간이 갈수록:

### ODP
company-level P/E
→ merger synergy
→ transformation narrative
→ **B2B asset SOTP**
→ **actual buyer / sale values**

### RST
growth story
→ low EV/Sales
→ SaaS/FCF forecast
→ **Lexia standalone economics**
→ **actual $30 takeout**

으로 바뀌었다.

즉 분석의 질이 높아지는 방향은:

> **Forecast-heavy → Asset / unit-economics heavy → External transaction proof**

였다.

---

## 16. BATCH 54 재사용 가능한 15개 체크리스트

1. raw Short/Long flag는 원문으로 반드시 감사한다.
2. ticker는 시대별 entity를 확인한다.
3. 주가 급락을 safety margin으로 착각하지 않는다.
4. cyclical P/E는 normalized denominator를 직접 만든다.
5. declining industry에서 demand 감소와 supply shrink를 같이 본다.
6. merger synergy는 실제 run-rate realization을 추적한다.
7. transformation M&A는 strategic fit보다 incremental ROIC를 본다.
8. failed acquisition은 purchase price가 아니라 current salvage value로 mark한다.
9. SOTP는 corporate cost, debt, tax leakage를 차감한다.
10. announced separation에는 completion probability를 적용한다.
11. reverse split 전후 nominal price를 직접 비교하지 않는다.
12. consumer growth는 revenue보다 CAC와 unit growth를 먼저 본다.
13. 80% gross margin도 S&M이 50%면 moat가 아닐 수 있다.
14. seasonal quarter FCF를 annualize하지 않는다.
15. 가장 강한 hidden-asset thesis는 **독립 business value가 whole EV를 덮고 실제 sale route가 있는 경우**다.

---

## 17. Batch 054 핵심 한 줄

> **좋은 투자논지는 시간이 갈수록 ‘회사가 잘될 것’이라는 예측에서 벗어나, 고객경제성·개별자산 가치·실제 매수자 가격처럼 외부 검증 가능한 숫자로 이동한다.**

---

## 18. 앱 / DB 반영

- Wrapper: `analysis/batch_054_odp_rst_10.md`
- Overlay: `data/curated/batch_054_odp_rst_deep_v7.json`
- Canonical source of truth: 위 10개 idea Markdown.
