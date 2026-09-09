# Batch 044 — Nexstar / ePlus V9 Index

> 기존 Batch 039·035의 검증 데이터를 재사용하되, Batch 003 V9 규칙에 맞춰 **각 VIC 게시시점을 독립 Idea Unit**으로 분리했다.  
> Raw SQL direction은 감사추적용으로 보존하고, 실제 원문 security/direction은 research layer에서 교정한다.

## Canonical idea files

| VIC 게시일 | Ticker | Raw flag | 실제 방향 / Security | Canonical file | 핵심 판정 |
|---|---|---|---|---|---|
| 2012-08-26 | NXST | Short | **Long common** | [2012 NXST Long](ideas/2012/2012-08-26_NXST_long.md) | Newport synergy·scale economics 강한 성공 |
| 2016-01-29 | NXST / MEG | Short | **Long MEG / Short 0.1249 NXST pair** | [2016 MEG–NXST CVR Pair](ideas/2016/2016-01-29_NXST_MEG_pair_cvr.md) | CVR isolation 성공, payout waterfall 가치추정 과대 |
| 2017-08-12 | NXST | Short | **Long common** | [2017 NXST Long](ideas/2017/2017-08-12_NXST_long.md) | Media General 후 retrans·FCF·M&A thesis 강한 성공 |
| 2018-04-23 | NXST | Short | **Long common** | [2018 NXST Long](ideas/2018/2018-04-23_NXST_long.md) | 직접 규제촉매 실패, operator optionality로 강한 성공 |
| 2020-03-12 | NXST | Short | **Long common** | [2020 NXST Long](ideas/2020/2020-03-12_NXST_long.md) | COVID panic survival/valuation 매우 강한 성공 |
| 2021-09-20 | NXST | Short | **Long common** | [2021 NXST Long](ideas/2021/2021-09-20_NXST_long.md) | M&A→buyback compounding 전환 강한 성공 |
| 2002-06-04 | PLUS | Long | **ePlus Long common** | [2002 ePlus Long](ideas/2002/2002-06-04_PLUS_long.md) | book/cash survival thesis 성공, catalyst 지연 |
| 2004-12-23 | PLUS | Long | **ePlus Long common** | [2004 ePlus Long](ideas/2004/2004-12-23_PLUS_long.md) | 정상화 가치 적중, 법률·회계 duration 과소평가 |
| 2007-05-09 | PLUS | Short | **ePlus Long common** | [2007 May ePlus Long](ideas/2007/2007-05-09_PLUS_long.md) | raw 방향오류 교정, restatement/relisting thesis 성공 |
| 2007-11-14 | PLUS | Short | **ePlus Long common** | [2007 Nov ePlus Long](ideas/2007/2007-11-14_PLUS_long.md) | raw 방향오류 교정, relisting catalyst 적중 |

---

# 1. Batch 044에서 가장 중요한 데이터 교정

## 1.1 NXST raw direction

Batch 044의 NXST 6건은 원 SQL상 모두 `Short`로 저장돼 있지만 실제 VIC 원문 기준으로는:

- 2012: Long
- 2016: MEG Long / 0.1249 NXST Short hedge를 이용한 CVR pair
- 2017: Long
- 2018: Long
- 2020: Long
- 2021: Long

이다.

따라서 SQL direction만 사용하면 이 배치의 투자성과와 학습결론이 거의 반대로 뒤집힌다.

## 1.2 PLUS ticker collision과 direction

`PLUS`는 원 DB에서 entity collision이 있는 ticker다. Batch 044의 네 건은 모두 **미국 ePlus inc.** 아이디어다.

- 2002/2004는 raw Long = actual Long
- 2007-05/2007-11은 raw Short이지만 actual Long

다른 시기의 `PLUS`가 Plus500 Ltd.일 수 있으므로 ticker만으로 entity를 연결하면 안 된다.

---

# 2. Nexstar 6개 아이디어를 함께 보면 무엇이 보이는가

Nexstar의 장기 성공은 단순히 “지역 TV가 생각보다 안 망했다”가 아니다. 투자 메커니즘은 시기별로 바뀌었다.

### 2012 — M&A ROIIC

**Newport acquisition  
→ synergy  
→ effective purchase multiple 하락  
→ incremental FCF 증가  
→ leverage를 소화  
→ equity value 증가**

가 핵심이었다.

### 2016 — Security engineering

기업가치 방향성보다:

**MEG price - cash consideration - hedged NXST stock = implied CVR**

로 contingent claim을 분리했다. 여기서 가장 중요한 실수는 gross spectrum value와 실제 CVR holder payout을 혼동한 것이다.

### 2017 — Scale + net retrans

Media General 후 규모가 커졌지만 중요한 KPI는 gross retrans가 아니다.

**Net distribution contribution = retransmission revenue - network affiliation / reverse compensation**

이다.

### 2018 — Regulatory optionality

Sinclair–Tribune이라는 직접 촉매는 틀렸다. 그러나 Nexstar가 규제 outcome에 따라 Tribune을 직접 인수하는 대체경로를 실행했다.

따라서 특정 규제 이벤트 예측보다 **operator action tree**가 더 중요했다.

### 2020 — Survival probability

COVID panic에서는 정상 FCF multiple보다:

**contractual distribution cash + liquidity + debt maturity runway**

가 먼저였다. Survival이 확인된 뒤 low multiple이 equity convexity로 전환됐다.

### 2021 — Buyback compounding

M&A runway가 줄어든 뒤 growth engine이:

**enterprise FCF growth → share count reduction → FCF/share growth**

로 바뀌었다.

---

# 3. ePlus 4개 아이디어를 함께 보면 무엇이 보이는가

네 아이디어 모두 같은 회사를 샀지만 투자논지의 중심은 변했다.

### 2002 — surviving cheap asset

닷컴 붕괴 뒤에도 흑자를 유지하는 회사가 book value 이하에서 거래됐다. 핵심은 **survival + asset support**였다.

### 2004 — normalized earnings vs event risk

Cyberco·법률비용·accounting 이슈를 정상화하면 earnings power가 싸 보였다. 그러나 사건이 상장·유동성에 미치는 second-order effect가 과소평가됐다.

### 2007-05 — accounting overhang special situation

Hard book 약 $12.90과 eventual filing normalization을 샀다. 논지 방향은 맞았지만 실제로 두 달 뒤 NASDAQ delisting까지 가면서 time/liquidity risk가 현실화됐다.

### 2007-11 — 이미 delisted된 상태에서 catalyst 매수

약 $10 price vs TBV $15+, normalized EBITDA 약 $24.8m, 3.5~4.5x EV/EBITDA를 근거로 restatement와 relisting을 샀다. 2008-05 filings 완료, 2008-09 NASDAQ relisting으로 가장 구체적인 catalyst가 실제 발생했다.

---

# 4. Batch 044 공통 투자교훈

## A. 낮은 multiple은 원인이 다르다

Nexstar 2020의 낮은 multiple은 **cyclical survival fear**, ePlus 2007의 낮은 multiple은 **accounting/listing uncertainty**였다.

같은 4~5x valuation이라도 falsifier가 완전히 다르다.

## B. Asset value와 security value는 다르다

2016 CVR에서 spectrum gross value를 잘 맞혀도 세금·repack·계약 공제를 거쳐 holder에게 귀속되는 돈을 틀리면 security valuation은 틀린다.

## C. Growth engine은 lifecycle에 따라 바뀐다

Nexstar:

**retrans monetization → M&A synergy → deleveraging → 대형 consolidation → buyback**

으로 value creation engine이 바뀌었다.

과거의 성공요인을 그대로 외삽하는 대신 다음 자본배분 메커니즘을 찾아야 한다.

## D. Event direction과 event duration을 분리한다

ePlus에서 “공시가 정상화될 것”은 맞았지만 “곧 정상화될 것”은 별개의 주장이다. Delisting/OTC 기간의 자본구속과 유동성 비용은 실질적 투자비용이다.

## E. Gross KPI보다 주주에게 남는 KPI를 본다

- gross retrans → **net retrans contribution**
- gross spectrum proceeds → **net CVR payout**
- product revenue → **gross profit / FCF**
- enterprise FCF → **FCF/share**
- book value → **claim-adjusted realizable book**

으로 한 단계 아래 내려가야 한다.

---

# 5. 남아 있는 정밀화 과제

V9 canonical files에는 확인되지 않은 exact historical return을 억지로 넣지 않았다. 다음 데이터는 별도 가격감사 단계에서 추가한다.

1. 각 게시일의 정확한 거래가능 T0 종가/시가 규칙 통일
2. split/dividend-adjusted 1Y/3Y/5Y total return
3. NXST 각 Long의 일별 MFE/MAE
4. 2016 MEG/NXST pair의 hedge-adjusted realized IRR, borrow/dividend carry
5. ePlus delisting/OTC 구간의 실제 거래가격과 유동성 discount
6. ePlus recourse/non-recourse financing의 연도별 재구성
7. Nexstar gross retrans와 network affiliation fee의 동일기준 장기 시계열

---

# 6. Batch-level 결론

Batch 044의 가장 큰 교훈은 **“기업을 맞힌 것”과 “주주가치로 귀속되는 경로를 맞힌 것”을 분리해야 한다**는 점이다.

Nexstar의 경우 사업·M&A·자본배분의 단계별 전환을 잘 본 Long들이 강하게 성공했다. 반면 2016 CVR에서는 underlying spectrum value는 잘 맞혔지만 legal waterfall을 과대평가했다.

ePlus에서는 core business와 tangible value 판단은 대체로 맞았지만 accounting issue가 exchange access와 duration에 미치는 영향을 초기에 과소평가했다. 즉 **좋은 asset thesis도 security structure·liquidity·time이 틀리면 투자경험은 크게 달라질 수 있다.**

---

# 7. 앱 / DB 반영

- Streamlit wrapper: `analysis/batch_044_nexstar_eplus_10.md`
- Curated overlay: `data/curated/batch_044_nexstar_eplus_deep_v7.json`
- NXST 6건은 기존 심화분석을 재사용하되, MEG/NXST CVR 1건은 0~12 canonical 목차로 표준화했고 Batch 044 overlay에서 raw SQL 방향을 보존했다.
- ePlus 4건은 0~12 전체 섹션, 각 6개 weighted claim, 가치평가·사건일정·경고신호·재사용 규칙을 포함하는 canonical V9으로 확장했다.
