# Batch 048 — KAR / Time Warner / Metals USA V9 Index

> **기준:** Batch 042 V9 format을 계승한다. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-09.
> **Direction audit:** source SQL의 is_short는 raw metadata로 보존하고, 실제 본문 security/direction은 별도 research layer에서 교정했다.

---

## Canonical Idea Units

| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2020-06-03 | KAR | Short | **Long** | [KAR 2020 Long](ideas/2020/2020-06-03_KAR_long.md) | survival 적중, +40% rerating 제한 |
| 2 | 2021-07-23 | KAR | Short | **Long** | [KAR 2021 Long](ideas/2021/2021-07-23_KAR_long.md) | digital thesis 일부 적중, asset-sale로 모델 경로 변경 |
| 3 | 2006-01-31 | TWX | Short | **LEAPS Long** | [TWX 2006 LEAPS](ideas/2006/2006-01-31_TWX_leaps_long.md) | corporate 방향은 맞고 option horizon 실패 |
| 4 | 2009-02-15 | TWX | Short | **Stub Long** | [TWX 2009 Stub](ideas/2009/2009-02-15_TWX_stub_long.md) | TWC/AOL separation 강한 성공 |
| 5 | 2013-07-24 | TWX | Short | **Long** | [TWX 2013 Long](ideas/2013/2013-07-24_TWX_long.md) | content scarcity·buyback·strategic value 성공 |
| 6 | 2015-01-28 | TWX | Short | **SOTP Long** | [TWX 2015 SOTP](ideas/2015/2015-01-28_TWX_sotp_long.md) | hidden asset + strategic scarcity 성공 |
| 7 | 2015-03-11 | TWX | Short | **Long** | [TWX 2015 Long](ideas/2015/2015-03-11_TWX_long.md) | $6 EPS 근접, 12M target은 지연 |
| 8 | 2015-12-10 | TWX | Short | **Short** | [TWX 2015 Short](ideas/2015/2015-12-10_TWX_short.md) | 산업은 맞고 security는 M&A로 강한 실패 |
| 9 | 2017-02-22 | TWX | Short | **Merger Arb Long** | [TWX 2017 Arb](ideas/2017/2017-02-22_TWX_merger_long.md) | deal close 성공, DOJ/duration 과소평가 |
| 10 | 2003-10-13 | MUSA | Long | **Metals USA Long** | [Metals USA 2003](ideas/2003/2003-10-13_MUSA_metalsusa_long.md) | post-BK turnaround, 2005 $22 cash exit |

---

## Direction / Entity Audit

이번 batch는 raw metadata quality issue가 매우 크다.

- **KAR 2건:** SQL은 모두 Short지만 원문은 Long.
- **TWX 7건:** 2015-12-10 secular thesis만 실제 Short. 나머지 6건은 Long/LEAPS/Stub/Merger Arb.
- **MUSA 2003:** raw Long은 맞지만 회사 identity가 Murphy USA가 아니라 **Metals USA**다.
- 따라서 raw ticker + is_short만으로 DB를 분석하면 10건 중 8건의 investment direction/entity context를 잘못 읽을 수 있다.

---

## 핵심 판정

### 1. KAR 2020 — survival trade와 rerating trade를 분리
$550m preferred financing은 liquidity tail risk를 실제로 줄였다. 거래량 회복도 맞았다. 그러나 SQL price series는 1Y +16.4%, 2Y +5.3%로 “easy +40%”에는 못 미쳤다.

### 2. KAR 2021 — marketplace thesis는 맞았지만 기업 perimeter가 바뀜
BacklotCars와 digital D2D는 전략 중심이 됐지만, 2022 ADESA U.S. physical auction business를 Carvana에 팔면서 2024 EBITDA/SOTP 모델의 비교대상이 사라졌다.

### 3. TWX 2006 — 좋은 기업가치 분석도 만기 짧은 option에서는 실패
TWC/AOL separation은 2009년에 일어났다. Jan-2008 calls는 그 시간을 기다릴 수 없었다.

### 4. TWX 2009 — 좋은 stub trade
이미 예정된 TWC separation + cash transfer, 이후 AOL spin이 discount 해소를 직접 만들었다.

### 5. TWX 2013~2015 Long — OTT disruption의 반대편
OTT가 cable bundle을 약화시키는 동시에 premium content owner의 bargaining power와 buyer scarcity를 높일 수 있다는 thesis가 적중했다. Time Inc spin, HBO NOW, Fox bid, AT&T bid가 연속 검증했다.

### 6. TWX 2015 Short — 산업을 맞히고 주식을 틀린 사례
cord-cutting 방향은 훌륭했지만 strategic buyer risk를 충분히 가격화하지 못했다. AT&T bid가 short를 파괴했다.

### 7. TWX 2017 arb — probability는 맞고 duration은 틀림
deal은 닫혔으나 DOJ litigation으로 year-end 2017 close 가정이 깨졌다. merger arb IRR은 probability × duration × hedge carry의 함수다.

### 8. Metals USA — post-bankruptcy convexity
balance-sheet reset + new operator + working-capital release + cycle recovery가 겹쳤고 2005 Apollo $22 cash takeout으로 value가 crystallize됐다.

---

## Batch 048 공통 분석식

### Recovery / Turnaround
**Equity payoff ≈ survival probability improvement + normalized EBITDA recovery + capital allocation - dilution/leverage drag**

### Content / Media
**Equity value ≈ content cash earnings + bargaining-power duration + strategic scarcity - distribution disruption - debt**

### Event / Arb
**Expected IRR ≈ probability-weighted spread ÷ expected duration - hedge carry - break loss × failure probability**

### Post-bankruptcy
**Equity convexity ≈ deleveraged capital structure × working-capital release × operating-margin recovery × cycle**

---

## 상위 교훈

1. **raw direction을 믿지 않는다.** 본문 security를 직접 읽어야 한다.
2. **기업 thesis와 security thesis를 분리한다.** TWX 2006/2015 Short가 대표적이다.
3. **구조적 변화는 가치사슬별로 본다.** OTT는 distributor에는 위협이고 premium content owner에는 bargaining-power source일 수 있다.
4. **event에는 duration이 있다.** 맞는 deal도 늦게 닫히면 IRR은 크게 낮아진다.
5. **post-BK는 자산가치만 보지 않는다.** capital structure와 operator change가 equity convexity를 만든다.
6. **SOTP는 residual implied value를 본다.** “WB를 거의 공짜로 산다” 같은 역산이 핵심이다.
7. **M&A tail은 Short에서 핵심 변수다.** risk paragraph에 적는 것으로 끝내면 안 된다.
8. **기업 perimeter가 바뀌면 forecast를 새로 만든다.** asset sale 뒤 옛 EBITDA target을 그대로 평가하지 않는다.

---

## Batch 구성 / Source IDs

1. KAR — ffa62e3d-8c80-4064-b37b-f81dd52825cb
2. KAR — 7f2bf8af-02a4-4335-80de-5ab1a702a9ef
3. TWX — 34b54ac6-6f41-4576-845b-4cfa4bb30646
4. TWX — 87549b45-8bf7-49db-8f74-23a24e452452
5. TWX — 07fffa81-725d-4091-9244-200083076a49
6. TWX — 171d98eb-0b29-4b07-9074-359033065903
7. TWX — 92817617-f252-4c1a-9efc-0ba51eadfb06
8. TWX — 91c79f18-515f-4cbe-a4c3-cdf5d379c922
9. TWX — a32500d7-d85f-41a7-a66b-cba1ec17747e
10. MUSA / Metals USA — 5faa64ca-3af9-41b2-bfe0-b7377094617b

---

## 앱/DB 반영

Wrapper: [batch_048_kar_timewarner_metalsusa_10.md](batch_048_kar_timewarner_metalsusa_10.md)

Curated overlay: data/curated/batch_048_kar_timewarner_metalsusa_deep_v7.json

Canonical source of truth는 위 10개 idea Markdown이다.
