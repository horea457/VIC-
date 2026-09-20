# Batch 077 — AdaptHealth / Ahern Rentals / Alliance Holdings GP / Armada Hoffler / Accredited Mortgage REIT Preferred / Aspen Insurance / American Home Mortgage V9 Index

> **기준:** Batch 043 이후 V9 원칙 유지. VIC 아이디어 1건 = canonical Markdown 1개.  
> **Research as-of:** 2026-09-20.  
> **Batch boundary:** Batch 076 마지막 **AHCO 2021-03-11** 이후 SQL의 ticker/date/id 정렬을 직접 파싱한 다음 10건.  
> **핵심 데이터 품질:** raw Short→actual Long **7건**(AHERN 2012, AHGP 2009/2012/2016, AHHAP 2012, AHL 2011, AHM 2007). Source SQL performance row는 **AHH 2015 한 건**만 존재. 이번 배치는 동일 `is_short=true`가 실제 Short(AHM 2005)와 다수 Long을 동시에 담고 있어, 방향값을 본문으로 재검증하는 것이 특히 중요하다.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 Security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2022-05-16 | AHCO | Long | **AdaptHealth Common Long** | [AHCO 2022](ideas/2022/2022-05-16_AHCO_adapthealth_long.md) | **강한 실패 — operations 일부 복구, M&A ROIC/per-share compounding 실패** |
| 2 | 2012-12-17 | AHERN | **Short** | **Ahern Rentals 2L Notes Long @65** | [Ahern](ideas/2012/2012-12-17_AHERN_ahern_rentals_second_lien_long.md) | **매우 강한 성공 — par + prepetition interest** |
| 3 | 2009-12-31 | AHGP | **Short** | **Alliance Holdings GP Long** | [AHGP 2009](ideas/2009/2009-12-31_AHGP_alliance_holdings_gp_long.md) | **강한 성공 — cost curve + high ROIC** |
| 4 | 2012-12-12 | AHGP | **Short** | **Alliance Holdings GP Long** | [AHGP 2012](ideas/2012/2012-12-12_AHGP_alliance_holdings_gp_long.md) | **강한 성공 — ILB thesis, late-2013 $60s exit** |
| 5 | 2016-04-06 | AHGP | **Short** | **Alliance Holdings GP Long** | [AHGP 2016](ideas/2016/2016-04-06_AHGP_alliance_holdings_gp_long.md) | **매우 강한 성공 — cut absorbed, low teens→~$28** |
| 6 | 2015-01-03 | AHH | Long | **Armada Hoffler Common Long** | [AHH](ideas/2015/2015-01-03_AHH_armada_hoffler_long.md) | **매우 강한 성공 — DB 5Y price +146%** |
| 7 | 2012-02-29 | AHHAP | **Short** | **Accredited Mortgage REIT Preferred Liquidation Long** | [AHHAP](ideas/2012/2012-02-29_AHHAP_accredited_mortgage_reit_preferred_long.md) | **강한 성공 — post-entry distributions ~$9.77 vs $6** |
| 8 | 2011-05-11 | AHL | **Short** | **Aspen Insurance Common Long** | [AHL](ideas/2011/2011-05-11_AHL_aspen_insurance_long.md) | **성공 — 0.77x BV rerating, later $42.75 takeout** |
| 9 | 2005-07-20 | AHM | Short | **American Home Mortgage Common Short** | [AHM 2005](ideas/2005/2005-07-20_AHM_american_home_mortgage_short.md) | **매우 강한 성공 — cash/funding fragility → bankruptcy** |
| 10 | 2007-03-15 | AHM | **Short** | **American Home Mortgage Common Long** | [AHM 2007](ideas/2007/2007-03-15_AHM_american_home_mortgage_long.md) | **catastrophic failure — Chapter 11 <5 months** |

---

# PART A — AdaptHealth: Turnaround 진단과 Capital Allocation은 별개다

## 2. AHCO 2022 Long

2022 글은 2021보다 process가 좋아졌다. 2020 organic decline과 M&A integration failure를 직접 추정했고 AeroCare 팀이 operations를 정상화할 수 있다고 봤다.

실제 2022~24 revenue/EBITDA는 개선됐지만:
- 2023 goodwill impairment **$830.8m**
- 2025 goodwill impairment **$128m**
- 2025 adjusted EBITDA **$616.7m**, 2024 $688.7m에서 감소
- 2026-09-18 stock **$5.71**

로 장기 M&A ROIC/per-share compounding은 실패했다.

### 핵심

> **turnaround를 맞혀도 acquisition economics를 틀리면 equity는 실패할 수 있다.**

---

# PART B — Ahern Rentals: Path보다 Recovery가 중요하다

## 3. AHERN 2012 Second-Lien Long @65

작성자는 second lien이 fulcrum이 되어 reorganized equity를 받을 수 있다고 봤다. 실제 plan은:
- old equity 100% retained by Ahern family
- second lien holders **par + pre-petition interest**
- other creditors 100% allowed claims

이었다.

65→100 alone = **+53.8%**, 약 반년 만의 cash recovery다.

### 핵심

> **distressed credit의 좋은 margin of safety는 특정 plan을 맞히는 게 아니라 여러 plan에서 매입가보다 recovery가 높다는 것이다.**

---

# PART C — AHGP 2009 / 2012 / 2016: 같은 회사, 세 개의 다른 가격

## 4. 2009 — Quality Commodity

- Illinois Basin low-cost position
- historical ROIC 30~50%+
- high-return growth capex

가 핵심이었다. 2010~13 thesis는 강하게 작동했다.

## 5. 2012 — Structural Share Shift

CAPP cost inflation + scrubbers + river transportation을 결합해 ILB share gain을 설명했다. 같은 작성자는 2016 follow-up에서 **late 2013 in the $60s**에 매도했다고 밝혔다.

## 6. 2016 — Distress Optionality

이번에는 high quality가 아니라 **27% indicated yield + low-teens price + gas mean reversion optionality**였다.

실제로 distribution cut은 발생했지만 2018 AHGP는 약 $28까지 회복했고 ARLP로 simplification되었다.

### 핵심

> **같은 기업도 2009에는 quality-at-reasonable-price, 2012에는 basin-share thesis, 2016에는 distressed optionality로 투자논지가 달라진다.**

---

# PART D — AHH / AHHAP / AHL: 세 종류의 Value Realization

## 7. AHH — NAV + Development Spread

Source DB:
- 1Y **+14.75%**
- 2Y **+71.63%**
- 3Y **+91.45%**
- 5Y **+146.04%**

8.8% implied cap rate와 internal development platform이 핵심이었다.

## 8. AHHAP — Liquidation Waterfall

$6 entry에서 remaining liquidation value를 $6.64~8.37로 봤다. 실제 plan-confirmation 이후 total distributions는 **$19.27/share**였고, VIC 이전 지급 약 $9.50을 빼면 post-entry distributions가 약 **$9.77/share**다.

## 9. AHL — Book Value Compounder

0.77x book에 book-value compounding을 샀고 2013~14 stock이 $40대로 rerate했다. 2019 Apollo가 **$42.75 cash/share**로 인수했다.

### 핵심

> **Value는 NAV rerating, liquidation cash, book compounding처럼 서로 다른 형태로 실현된다. 분석식도 각각 달라야 한다.**

---

# PART E — AHM 2005 Short vs 2007 Long: Asset Quality보다 Liability Structure

## 10. 2005 Short

2005 글은:
- reported earnings와 cash generation의 괴리
- dividend를 내부 현금으로 못 버는 구조
- securitization/accounting assumptions
- wholesale funding dependence

를 봤다.

2년 뒤 Chapter 11로 연결됐다.

## 11. 2007 Long

2007 글은:
- subprime 0.3%
- FICO 710
- LTV 75%
- 1.07x book
- 18.5% dividend yield
- many funding facilities

를 근거로 “subprime bathwater에 같이 버려진 baby”라고 봤다.

그러나 **2007-08-06 Chapter 11**, 게시 후 5개월도 안 됐다.

### 핵심

> **레버리지 금융사에서 asset credit quality가 좋아도 liability rollover가 끊기면 book value와 dividend yield는 보호막이 아니다.**

---

# PART F — Batch 077 재사용 분석식

### M&A Compounder

**Per-share value growth = organic FCF + M&A value creation - premium - integration cost - interest - dilution - impairment**

### Distressed Credit

**Expected recovery = Σ(state probability × recovery by state)**

### Commodity Quality

**Cycle-adjusted earning power = normalized volume × (price - sustainable delivered cost) - maintenance capex**

### REIT

**NAV return = starting NOI yield + NOI growth + development value - financing-cost change ± cap-rate rerating**

### Liquidation

**Remaining value/share = (cash + claims + assets - fees - taxes - litigation - prior distributions) / shares**

### Insurance

**Expected return ≈ BVPS growth + Δ(P/B) + dividend yield**

### Leveraged Financial

**Survival = collateral liquidity + rollover capacity - margin calls - cash needs**

---

# PART G — Batch 077 재사용 체크리스트

1. `is_short` raw field보다 원문 명시적 action을 우선한다.
2. M&A turnaround와 M&A ROIC를 분리한다.
3. distressed debt는 fulcrum label보다 recovery waterfall을 본다.
4. commodity low-cost producer는 low-volatility asset가 아니다.
5. 표시 distribution yield를 cycle-low FCF로 stress test한다.
6. REIT의 internal development organization을 별도 economic asset로 평가한다.
7. liquidation에서는 purchase date 이전 distributions를 반드시 차감한다.
8. 보험 P/B는 BVPS growth가 양수일 때만 의미가 있다.
9. financial company book value는 funding continuity가 있어야 실현 가능하다.
10. 여러 funding facility가 같은 collateral/market factor에 노출되면 진짜 diversification이 아니다.
11. asset quality와 liability liquidity가 충돌하면 단기적으로 liability가 이긴다.
12. 같은 회사라도 가격과 cycle이 바뀌면 thesis type을 새로 정의한다.

---

## 12. Batch 077 핵심 한 줄

> **이번 배치의 공통점은 ‘가치가 어디에 있느냐’보다 ‘그 가치가 어떤 경로로 주주·채권자에게 도달하느냐’다. Ahern은 equity가 아니라 par recovery로 성공했고, AHHAP는 liquidation cash로 성공했으며, AHM은 좋은 mortgage assets가 있어도 funding path가 끊겨 equity가 0이 됐다.**

## 13. 앱 / DB 반영

- Wrapper: `analysis/batch_077_ahco_ahern_ahgp_ahh_ahhap_ahl_ahm_10.md`
- Overlay: `data/curated/batch_077_ahco_ahern_ahgp_ahh_ahhap_ahl_ahm_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
