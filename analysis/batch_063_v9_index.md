# Batch 063 — AEGR / AEL / AEN / AENA / AEO / AEOS V9 Index

> **Research as-of:** 2026-09-16. `VIC_IDEAS(5).sql` 기준 Batch 062 마지막 AEC 다음 10건이다. 10 ideas = 10 canonical reports.
> **핵심 감사:** raw direction correction 6건, security correction 1건(AEGR convert), SQL performance row 5건. 없는 수익률은 만들지 않았다.

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw | 실제 | Security | 최종 판정 | Thesis/Process | Canonical |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 2016-12-05 | AEGR | Long | **Long** | 2.0% senior unsecured convertible notes due 2019 | security payoff 부분 성공 가능 / operating·refinancing thesis 실패 | 6.3/9.3 | [AEGR 2016-12-05](ideas/2016/2016-12-05_AEGR_convert_long.md) |
| 2 | 2021-01-03 | AEL | Long | **Long** | Common stock | 강한 성공 — capital return과 strategic rerating 현실화 | 9.7/9.7 | [AEL 2021-01-03](ideas/2021/2021-01-03_AEL_long.md) |
| 3 | 2004-03-16 | AEN | Short | **Long** | Common stock | 강한 성공 — $19~20 base/upside가 $19.50 cash deal로 실현 | 9.8/9.6 | [AEN 2004-03-16](ideas/2004/2004-03-16_AEN_long.md) |
| 4 | 2015-03-27 | AENA | Short | **Long** | Common stock | 매우 강한 성공 — operating assumptions 상회·약 2x rerating | 9.8/9.8 | [AENA 2015-03-27](ideas/2015/2015-03-27_AENA_long.md) |
| 5 | 2007-11-02 | AEO | Short | **Long** | Common stock | 실패 — 장기 brand insight를 peak margin·macro/fashion risk가 압도 | 3.4/9.3 | [AEO 2007-11-02](ideas/2007/2007-11-02_AEO_long.md) |
| 6 | 2008-07-07 | AEO | Short | **Long** | Common stock | 부분/지연 성공 — turnaround 적중·GFC로 timing과 $26 path 지연 | 7.4/9.4 | [AEO 2008-07-07](ideas/2008/2008-07-07_AEO_long.md) |
| 7 | 2016-01-22 | AEO | Long | **Long** | Common stock | 성공 — Aerie·시장점유율·장기 rerating 적중, margin은 지연/미달 | 8.7/9.4 | [AEO 2016-01-22](ideas/2016/2016-01-22_AEO_long.md) |
| 8 | 2021-04-05 | AEO | Short | **Long** | Common stock | 실패 — business growth 적중에도 목표·분리·주가 가치실현 실패 | 3.8/9.5 | [AEO 2021-04-05](ideas/2021/2021-04-05_AEO_long.md) |
| 9 | 2000-06-14 | AEOS | Long | **Long** | Common stock | 강한 성공 — 운영 회복과 6~8개월 내 큰 폭 rerating | 9.2/9.3 | [AEOS 2000-06-14](ideas/2000/2000-06-14_AEOS_long.md) |
| 10 | 2005-12-11 | AEOS | Short | **Long** | Common stock | 강한 성공 — core 실적·buyback·주가 목표 적중, M+O는 실패 | 9.1/9.5 | [AEOS 2005-12-11](ideas/2005/2005-12-11_AEOS_long.md) |

## 2. 방향·증권·성과 데이터 감사

- **Raw Short → actual Long:** AEN 2004, AENA 2015, AEO 2007, AEO 2008, AEO 2021, AEOS 2005 — 총 6건.
- **Raw Long 일치:** AEGR 2016, AEL 2021, AEO 2016, AEOS 2000.
- **Security correction:** AEGR는 common이 아니라 2019년 만기 2.0% senior unsecured convertible note다. 기업 turnaround 실패와 note recovery를 분리했다.
- **SQL 성과 있음:** AEL과 AEO 4건. **없음:** AEGR, AEN, AENA, AEOS 2건. 후자는 거래가격·공식 TSR·split-adjusted 범위를 보조증거로 쓰되 exact daily return으로 위장하지 않았다.

## 3. 투자논지 구체화 — 무엇을 샀고 무엇이 실제 payoff를 만들었나

### 3.1 계약·거래가 할인율을 닫은 사례

**AEN 2004**는 극장 성장률을 맞히는 아이디어가 아니었다. 약 $15에서 no-growth DCF와 private-market multiple이 $19~20을 지지했고, Marquee가 $19.50 cash로 그 간극을 9개월 만에 닫았다. 투자자가 추적할 항목은 attendance 예측보다 buyer financing, lease/debt 차감 뒤 equity consideration, deal break 조건이었다.

**AEL 2021**은 단순 저P/B 보험 Long이 아니었다. `higher-yielding assets + reinsurance로 capital intensity 축소 + 낮은 가격의 buyback`이 주당가치를 키우는 구조였고, 23.9m주 매입과 Brookfield의 $56.50 인수가 두 단계의 가치실현을 완성했다. 저평가의 원인이 남아 있는지보다 excess capital이 실제 주주에게 이동하는지를 봐야 했다.

### 3.2 영업 레버리지가 수치로 검증된 사례

**AENA 2015**의 핵심 bridge는 `passengers × aeronautical yield + commercial spend/passenger - fixed cost - capex - interest`였다. 2018 traffic과 EBITDA가 원문 가정을 모두 상회했고 deleveraging이 equity duration을 확대했다. 규제 공항에서는 traffic만이 아니라 tariff, commercial yield, debt/EBITDA를 함께 봐야 한다.

**AEOS 2000**은 weather와 inventory clearance가 structural brand damage인지 구분하는 turnaround였다. BTS 이후 comps·margin이 회복되고 주가범위가 크게 올라 논지가 맞았다. **AEOS 2005**는 core FCF와 buyback만으로 base case를 세우고 Aerie·M+O를 option으로 둔 덕분에 M+O 실패에도 성공했다.

**AEO 2016**은 같은 retailer라도 entry expectation이 낮고 Aerie 실증 데이터가 있었다. Aerie comps와 장기 매출은 맞았고 5년 SQL price return은 +88.0%였다. 다만 10~12% consolidated margin은 즉시 실현되지 않아 성장옵션과 margin bridge를 분리해야 한다.

### 3.3 좋은 사업을 맞혔지만 주식을 잘못 산 사례

**AEO 2007**은 Aerie의 장기 잠재력은 맞혔지만 peak earnings와 fashion/macro drawdown을 과소평가해 1년 -50.2%였다. 장기 insight는 현재 inventory와 markdown의 손실을 상쇄하지 못했다.

**AEO 2021**은 Aerie와 AE reopening은 맞았지만 Aerie를 이미 독립회사처럼 평가했다. corporate cost, logistics, inventory와 실제 분리확률을 차감하지 않아 3개월 +23.5% 뒤 1년 -45.2%로 반전했다. segment quality와 security payoff는 분리해야 한다.

**AEO 2008**은 $13.24로 entry가 낮아졌고 fashion mean reversion도 맞았지만 GFC가 catalyst clock을 늘렸다. 5년 +66.2%는 성공이지만 6개월 -23.7%, 2년 -10.2%는 duration과 liquidity를 별도 underwriting해야 함을 보여준다.

### 3.4 기업가치와 security recovery가 다른 사례

**AEGR 2016 convert**는 operating thesis가 실패해 Chapter 11로 갔어도 mid/high-60s entry와 Class 6B 예상 회수율 80.7% 사이에 recovery cushion이 남았다. 반대로 신규 secured bridge가 위에 쌓이며 noteholder의 waterfall은 악화됐다. distressed security는 pipeline EV보다 burn, claim priority, new-money seniority가 먼저다.

## 4. 동일 회사 AEO/AEOS의 시간축 비교

| 아이디어 | Entry expectation | 핵심 edge | 최초 반증/검증 | 결과 |
|---|---|---|---|---|
| AEOS 2000 | 3x TEV/EBITDA·YTD -68% | temporary weather/inventory | BTS comps·margin 회복 | 강한 성공 |
| AEOS 2005 | 5.1x EV/EBITDA·순현금 | core FCF+buyback, options 무료 | FY2006 comps/EPS | 강한 성공 |
| AEO 2007 | 6.2x EBIT이나 peak margin | insider buy+Aerie | women's comps·markdown | 실패 |
| AEO 2008 | 이미 fashion miss 반영 | cash runway+mean reversion | GFC로 clock 연장 | 지연 성공 |
| AEO 2016 | 4.6x EBITDA | Aerie 실증+share gains | Aerie comp·margin | 성공 |
| AEO 2021 | 6x forward EBITDA·높은 기대 | SOTP+분리 option | $800m 목표·분리 부재 | 실패 |

같은 브랜드에서도 결과를 가른 것은 ‘Aerie가 좋은가’가 아니라 **entry에 얼마나 반영됐는지, core earnings가 peak인지, catalyst가 계약인지 추정인지, 버틸 시간과 현금이 있는지**였다.

## 5. 재사용 가능한 투자 체크리스트

1. raw direction과 실제 본문 방향을 먼저 대조한다.
2. common, convert, unsecured claim을 같은 payoff로 다루지 않는다.
3. 저 valuation에서는 peak/normalized earnings denominator를 먼저 재구축한다.
4. segment SOTP에는 corporate·stranded cost, tax와 transaction probability를 차감한다.
5. insurer의 excess capital은 buyback·reinsurance·배당으로 실제 이동하는지 본다.
6. retailer는 comps 하나보다 inventory, markdown, gross margin과 cash runway를 함께 본다.
7. 공항 같은 고정비 인프라는 volume과 ancillary yield, debt paydown을 연결한다.
8. optionality가 모두 0이어도 base case가 성립해야 한다.
9. 장기 사업통찰과 투자 horizon의 price path를 별도 채점한다.
10. SQL 성과가 없으면 official event와 범위를 exact return으로 바꾸지 않는다.

## 6. 배치 결론

Batch 063의 가장 강한 공통 교훈은 **좋은 자산보다 올바른 security·entry expectation·현금화 경로가 먼저**라는 점이다. AEN/AEL은 계약과 자본배분이, AENA/AEOS/AEO 2016은 실측 운영지표가 discount를 닫았다. AEO 2007/2021은 좋은 장기 브랜드 관찰에도 peak denominator와 미확정 catalyst 때문에 실패했다. AEGR는 기업 실패와 security recovery가 동시에 존재할 수 있음을 보여준다.

## 7. 산출물

- Payload: `data/curated/batch_063_aegr_ael_amc_aena_aeo_deep_v7.json`
- Wrapper: `analysis/batch_063_aegr_ael_amc_aena_aeo_10.md`
- Source packet: `data/curated/batch_063_source_packet.json`
- SQL inventory: `data/curated/batch_063_sql_inventory.json`
- Builder: `scripts/63_build_batch_063_v9.py`
