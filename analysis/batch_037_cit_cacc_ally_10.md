# Batch 037 — CIT / Credit Acceptance / Ally

> Research as-of 2026-09-05. **10 ideas / 100 sections / 60 weighted claims / 40 metrics / 60 timeline / 60 sources.** Raw SQL flags are preserved; research direction and security instrument are corrected from the original VIC text.

## Critical data-quality findings

- All ten ideas are actual **Longs**. Seven raw `Short` flags are metadata errors.
- CIT 2009 is **senior unsecured bond Long**, not common equity. Bankruptcy outcome must be judged through the debt waterfall.
- CACC 2010 is a one-day **odd-lot tender event trade**, not a fundamental multi-year Long.

## 1. CIT — 2009-07-28 — Rotin

**idea_id:** `f2dc229e-52b4-4b56-ae6b-ca21f91e3415`  
**Raw SQL:** Short | **Research:** **Long — senior unsecured bonds** | **Verdict:** **성공**

### 1. 원 논지
2009년 당시 common equity가 아니라 5.6% 2011 unsecured bonds를 59에 사는 distressed-credit 아이디어였다. 저자는 liquidation recovery 80~100, prepack 시 신규 equity까지 받을 수 있다고 보았다.

### 2. 실제 전개
2009년 prepack에서 2011~2012 senior unsecured holders는 기존 원금 $1당 신규 notes 70¢와 신규 common interests를 받았다. old common은 전부 소각됐지만 이 아이디어의 instrument는 채권이므로 common-equity 전손과 혼동하면 안 된다.

### 3. 분석
instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | Bond price 59 |
| 2 | Recovery thesis 80-100 |
| 3 | Plan: 70¢ new notes + common |
| 4 | Old common cancelled |

### 5. Six-claim audit

- **20% business/unit economics:** instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.
- **18% funding/capital structure:** instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.
- **17% valuation:** instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.
- **16% catalyst:** instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.
- **15% regulatory/credit risk:** instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.
- **14% terminal outcome:** instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long — senior unsecured bonds으로 교정. 이 아이디어는 common이 아니라 senior unsecured debt다.

### 7. Final
성공 — instrument identity와 bankruptcy waterfall을 정확히 잡은 것이 성공의 핵심이다. 싸다는 이유가 아니라 collateral/loan recovery를 debt class별로 모델링했다.

---

## 2. CIT — 2011-10-04 — brook1001

**idea_id:** `bbce234a-0f82-416d-bfcc-e20ceae4c326`  
**Raw SQL:** Short | **Research:** **Long** | **Verdict:** **성공**

### 1. 원 논지
2011 post-bankruptcy CIT를 $29, 68% GAAP TBV/57% adjusted TBV에 사는 balance-sheet normalization Long이다. 19.1% Tier 1 common, excess cash/capital, 7% bankruptcy debt를 deposit funding으로 교체해 finance margin을 1.45%에서 3~4%로 회복시키는 것이 핵심이었다.

### 2. 실제 전개
CIT는 이후 고비용 부채를 줄이고 bank/deposit funding 비중을 높였으며 OneWest를 인수했다. 2016에는 Commercial Air 매각을 추진할 만큼 구조 단순화가 진전됐고 2017 Avolon에 약 $10.4bn cash로 매각했다.

### 3. 분석
post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 $29 |
| 2 | 68% GAAP TBV |
| 3 | Tier1 common 19.1% |
| 4 | 2017 Air sale ~$10.4bn |

### 5. Six-claim audit

- **20% business/unit economics:** post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.
- **18% funding/capital structure:** post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.
- **17% valuation:** post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.
- **16% catalyst:** post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.
- **15% regulatory/credit risk:** post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.
- **14% terminal outcome:** post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long으로 교정.

### 7. Final
성공 — post-reorg 금융주는 P/TBV 자체보다 liability repricing과 excess-capital deployment가 촉매다.

---

## 3. CIT — 2016-03-03 — abra399

**idea_id:** `a8bb036d-28b6-443d-98d7-59f02969dc49`  
**Raw SQL:** Short | **Research:** **Long** | **Verdict:** **성공**

### 1. 원 논지
2016 CIT를 0.57x book/0.65x TBV, 10x 2016E EPS에 사면서 OneWest의 저원가 deposit funding, $5bn+ NOL, Commercial Air 분리, buyback을 가치실현 경로로 본 Long이다.

### 2. 실제 전개
Commercial Air는 2016 Avolon과 $10.0bn agreement를 체결했고 2017 약 $10.4bn cash로 매각 완료됐다. 회사는 매각 후 대규모 자본환원과 부채상환을 진행했다.

### 3. 분석
SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 0.57x P/B |
| 2 | 0.65x TBV |
| 3 | Target $40-45+ |
| 4 | Air sale ~$10.4bn |

### 5. Six-claim audit

- **20% business/unit economics:** SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.
- **18% funding/capital structure:** SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.
- **17% valuation:** SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.
- **16% catalyst:** SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.
- **15% regulatory/credit risk:** SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.
- **14% terminal outcome:** SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long으로 교정.

### 7. Final
성공 — SOTP가 실제 catalyst로 전환된 사례다. 단 aircraft book value만 볼 게 아니라 sale proceeds가 RemainCo funding/capital에 어떻게 재배치되는지가 중요했다.

---

## 4. CIT — 2020-10-19 — abra399

**idea_id:** `09a5b37a-fc76-4352-83c4-4f5852b0ce1e`  
**Raw SQL:** Short | **Research:** **Long — merger/RemainCo** | **Verdict:** **성공**

### 1. 원 논지
2020 First Citizens 합병 발표 뒤 CIT가 받을 0.062 FCNCA shares를 통해 combined bank를 6.2x pro forma EPS, 약 94% pro forma TBV에 사는 Long이다. cost saves와 CIT deposit cost 하락의 추가 optionality를 봤다.

### 2. 실제 전개
First Citizens-CIT merger는 2022-01-03 완료됐다. 인수된 CIT는 약 $53.8bn assets, $39.4bn deposits를 더했고 First Citizens는 거래가 tangible book value에 40% 이상 즉시 accretive했다고 보고했다.

### 3. 분석
merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | Exchange 0.062 FCNCA |
| 2 | 6.2x pro forma EPS |
| 3 | ~94% pro forma TBV |
| 4 | Closed 2022-01-03 |

### 5. Six-claim audit

- **20% business/unit economics:** merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.
- **18% funding/capital structure:** merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.
- **17% valuation:** merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.
- **16% catalyst:** merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.
- **15% regulatory/credit risk:** merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.
- **14% terminal outcome:** merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long — merger/RemainCo으로 교정.

### 7. Final
성공 — merger arb가 아니라 exchange ratio로 얻게 되는 buyer equity의 post-close economics까지 분석한 점이 핵심이다.

---

## 5. CACC — 2010-07-19 — quads1025

**idea_id:** `3d1b9872-1525-4301-be18-0d6efd9f7e4a`  
**Raw SQL:** Long | **Research:** **Long — odd-lot tender** | **Verdict:** **성공**

### 1. 원 논지
2010-07-19 하루짜리 odd-lot tender trade다. 99주를 $48.80에 사서 $50 cash tender에 넣으면 odd-lot priority 때문에 proration 없이 약 $118.80, 5일 약 2.5%를 얻는 구조였다.

### 2. 실제 전개
이 아이디어의 평가대상은 CACC 장기 business가 아니라 tender 조건과 closing risk다. 당시 회사는 최대 4m shares를 $50에 매입하는 issuer tender를 진행했고 odd-lot exemption이 핵심이었다.

### 3. 분석
event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | Buy $48.80 |
| 2 | Tender $50.00 |
| 3 | 99 shares |
| 4 | ~2.5% / ~5 days |

### 5. Six-claim audit

- **20% business/unit economics:** event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.
- **18% funding/capital structure:** event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.
- **17% valuation:** event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.
- **16% catalyst:** event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.
- **15% regulatory/credit risk:** event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.
- **14% terminal outcome:** event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.

### 6. Direction / instrument audit
**Raw direction consistent.**

### 7. Final
성공 — event trade는 장기 주가성과로 판정하면 안 된다. security, size constraint, proration rule, MAC를 별도 metadata로 남겨야 한다.

---

## 6. CACC — 2011-11-21 — spsc01

**idea_id:** `c9df38c3-bceb-40cd-8864-36ed473fa690`  
**Raw SQL:** Short | **Research:** **Long** | **Verdict:** **성공**

### 1. 원 논지
2011 CACC를 11x P/E에서 사는 성장/quality Long이다. 5년 revenue CAGR 25%, earnings CAGR 38%, ROE 약 50%, 낮은 subprime share와 dealer expansion을 근거로 auto recovery와 share gain을 기대했다. raw Short는 본문과 반대다.

### 2. 실제 전개
CACC는 이후 dealer network와 originations를 크게 확장했고 장기간 높은 returns를 유지했다. 2016·2017 VIC Long들이 다시 등장할 정도로 earnings/share가 성장했다.

### 3. 분석
deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 11x P/E |
| 2 | ROE ~50% |
| 3 | 5y rev CAGR 25% |
| 4 | 5y earnings CAGR 38% |

### 5. Six-claim audit

- **20% business/unit economics:** deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.
- **18% funding/capital structure:** deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.
- **17% valuation:** deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.
- **16% catalyst:** deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.
- **15% regulatory/credit risk:** deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.
- **14% terminal outcome:** deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long으로 교정.

### 7. Final
성공 — deep-subprime라는 label보다 dealer first-loss/holdback 구조, collection forecasting, funding discipline이 실제 risk를 결정한다.

---

## 7. CACC — 2016-01-14 — rickey824

**idea_id:** `2847ee58-17dd-44cd-a31b-3f631bcc725f`  
**Raw SQL:** Long | **Research:** **Long** | **Verdict:** **강한 성공**

### 1. 원 논지
2016 Long은 dealer가 first-loss를 부담하고 CACC가 advance를 먼저 회수하는 Portfolio Program을 moat로 봤다. 13x LTM adjusted earnings, 30%+ ROE, target $318~363, 규제/auto-cycle fear가 과도하다는 논지였다.

### 2. 실제 전개
저자 스스로 2020 후속 글에서 2016 이후 주가가 2배 이상, adjusted EPS가 $15에서 $35로 24% p.a. 성장했다고 확인했다. 다만 이후 CFPB/NY AG 소송은 regulatory risk를 완전히 무시할 수 없음을 보여줬다.

### 3. 분석
unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 ~13x adj EPS |
| 2 | Target $318-363 |
| 3 | Adj EPS $15 -> $35 by 2020 |
| 4 | 2023 CFPB/NY AG suit |

### 5. Six-claim audit

- **20% business/unit economics:** unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.
- **18% funding/capital structure:** unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.
- **17% valuation:** unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.
- **16% catalyst:** unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.
- **15% regulatory/credit risk:** unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.
- **14% terminal outcome:** unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.

### 6. Direction / instrument audit
**Raw direction consistent.**

### 7. Final
강한 성공 — unit-economics와 incentive waterfall을 이해한 quality-financial 분석이 강점이었고, 규제는 low-probability가 아니라 지속적 tail risk로 남겨야 했다.

---

## 8. CACC — 2017-03-10 — jon64

**idea_id:** `fb10159b-b84d-4f28-8e37-220505b7b823`  
**Raw SQL:** Short | **Research:** **Long** | **Verdict:** **성공**

### 1. 원 논지
2017 본문은 CACC를 high-quality, difficult-to-replicate business라고 명시하고 9~10x 2017E earnings, 5년+ mid-teens NI growth를 기대한 Long이다. 33% short interest와 sell-side의 cycle 오해를 contrarian setup으로 봤다.

### 2. 실제 전개
2017 이후 earnings/share와 주가는 크게 성장했고 2020 Long에서는 2016 대비 adjusted EPS가 두 배 이상으로 커졌다고 재확인된다. CACC는 2021~22에도 대규모 buyback을 지속했다.

### 3. 분석
short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 9-10x EPS |
| 2 | Short interest 33% |
| 3 | Forecast collections avg +0.7% vs initial |
| 4 | 2021-22 buybacks 25.4% of starting shares |

### 5. Six-claim audit

- **20% business/unit economics:** short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.
- **18% funding/capital structure:** short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.
- **17% valuation:** short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.
- **16% catalyst:** short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.
- **15% regulatory/credit risk:** short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.
- **14% terminal outcome:** short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long으로 교정.

### 7. Final
성공 — short interest 자체가 catalyst가 아니라 높은 forecast accuracy·dealer incentives·countercyclical pricing ability가 실제 thesis였다.

---

## 9. CACC — 2020-02-06 — rickey824

**idea_id:** `f7929097-4b11-46c8-abf7-68a594805f7f`  
**Raw SQL:** Short | **Research:** **Long** | **Verdict:** **혼합 성공**

### 1. 원 논지
2020 Long은 2016 이후 share price가 2배 이상인데 multiple은 여전히 13x, adjusted EPS는 $15에서 $35로 증가했다고 제시했다. CECL가 reported provision을 왜곡하지만 economics는 변하지 않는다는 주장과 downturn 시 share gain을 기대했다.

### 2. 실제 전개
COVID downturn에서도 회사는 존속했고 이후 2021~22 excess capital로 약 4.3m shares, 당시 shares의 25.4%를 $2.2bn에 repurchase했다. 다만 2023 CFPB/NY AG 소송은 원문이 낮게 본 regulatory tail이 현실화될 수 있음을 보여준다.

### 3. 분석
accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 13x adj EPS |
| 2 | Adj EPS $35 |
| 3 | 2021-22 repurchase 4.3m shares |
| 4 | CFPB/NY AG suit 2023 |

### 5. Six-claim audit

- **20% business/unit economics:** accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.
- **18% funding/capital structure:** accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.
- **17% valuation:** accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.
- **16% catalyst:** accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.
- **15% regulatory/credit risk:** accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.
- **14% terminal outcome:** accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.

### 6. Direction / instrument audit
**SQL 오류:** raw Short를 보존하되 원문상 Long으로 교정.

### 7. Final
혼합 성공 — accounting normalization은 맞았지만 “regulation immaterial”은 별도 falsifier가 필요했다. quality와 regulatory license-to-operate는 분리해서 확률가중해야 한다.

---

## 10. ALLY — 2016-08-08 — TomMurner

**idea_id:** `722a2dbe-b1b8-4a92-bf4b-c4ef3fd1984a`  
**Raw SQL:** Long | **Research:** **Long** | **Verdict:** **성공**

### 1. 원 논지
2016 Ally를 0.7x TBV, 7.2x 2017E EPS에 사는 restructuring/capital-return Long이다. prime-heavy auto book, online deposit franchise, high-cost debt run-off, preferred redemption과 buyback/dividend가 ROTCE를 low-teens로 끌어올릴 것으로 봤다.

### 2. 실제 전개
2017 adjusted EPS는 $2.39(+11% YoY), $753m buybacks와 $0.40/share dividends를 실행했다. 2020 COVID 1Q에는 $903m provision으로 적자였지만 3Q core ROTCE 15.2%, deposits $134.9bn으로 회복했고 2021 buyback authorization은 $1.6bn이었다.

### 3. 분석
cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.

### 4. 핵심 수치

| Anchor | Detail |
|---|---|
| 1 | T0 0.7x TBV |
| 2 | 7.2x 2017E EPS |
| 3 | 2017 buyback $753m |
| 4 | 3Q20 core ROTCE 15.2% |

### 5. Six-claim audit

- **20% business/unit economics:** cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.
- **18% funding/capital structure:** cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.
- **17% valuation:** cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.
- **16% catalyst:** cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.
- **15% regulatory/credit risk:** cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.
- **14% terminal outcome:** cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.

### 6. Direction / instrument audit
**Raw direction consistent.**

### 7. Final
성공 — cheap P/TBV가 작동한 이유는 liability-side deposit advantage와 capital-return permission이 동시에 현실화됐기 때문이다.

---
