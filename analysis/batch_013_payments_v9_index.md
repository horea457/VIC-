# Batch 013 — Payments V9 Index

> 기존 `analysis/batch_013_payments_10.md`와 `analysis/batch_013_payments_v2_deep.md`는 archive/reference로 유지한다.  
> V9에서는 **10개 VIC 아이디어를 각각 독립 canonical report**로 관리한다.

---

# 1. Canonical idea files

## Mastercard (MA) — 1건

| 날짜 | 파일 | 핵심 판정 |
|---|---|---|
| 2010-09-14 | [MA Long](ideas/2010/2010-09-14_MA_long.md) | 전설적 성공 — 12.3x EPS의 글로벌 network |

## Global Payments (GPN) — 1건

| 날짜 | 파일 | 핵심 판정 |
|---|---|---|
| 2012-11-06 | [GPN Long](ideas/2012/2012-11-06_GPN_long.md) | 매우 성공 — 보안사고 정상화 + 낮은 FCF multiple |

## PayPal (PYPL) — 3건

| 날짜 | 파일 | 핵심 판정 |
|---|---|---|
| 2016-09-06 | [PYPL Long](ideas/2016/2016-09-06_PYPL_long.md) | 성공 — eBay 분사 후 branded checkout + Venmo option |
| 2021-12-15 | [PYPL Long](ideas/2021/2021-12-15_PYPL_long.md) | 치명적 실패 — TPV 성장과 transaction economics 혼동 |
| 2022-06-28 | [PYPL Long](ideas/2022/2022-06-28_PYPL_long.md) | 초기 실패·장기 미판정 |

## Block / Square (SQ) — 5건

| 날짜 | 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2016-11-25 | Long | [SQ Long](ideas/2016/2016-11-25_SQ_long.md) | 매우 성공 — seller cohort + cheap option |
| 2018-07-02 | Short | [SQ Short](ideas/2018/2018-07-02_SQ_short.md) | 실패 — 큰 squeeze / terminal economics 오판 |
| 2019-06-19 | Long | [SQ Long](ideas/2019/2019-06-19_SQ_long.md) | 사업 적중·주가 부분 실패 |
| 2021-03-02 | Long | [SQ Long](ideas/2021/2021-03-02_SQ_long.md) | 치명적 실패 |
| 2021-06-05 | Long | [SQ Long](ideas/2021/2021-06-05_SQ_long.md) | 치명적 실패 |

---

# 2. Batch 013의 핵심 질문

결제주는 쉽게:

> **현금 → 전자결제 전환 → TPV/GPV 성장 → 주가 상승**

으로 단순화된다.

하지만 실제 주주가치 bridge는 훨씬 길다.

**Volume  
→ Mix  
→ Take rate  
→ Net revenue  
→ Transaction / contribution margin  
→ Opex  
→ SBC / dilution  
→ FCF/share**

가 핵심이다.

따라서:

> **Volume compounder가 아니라 주당 현금전환율 compounder인지 본다.**

---

# 3. Mastercard — 가장 깨끗한 Network Economics

Mastercard의 핵심은 은행처럼 신용위험을 직접 떠안는 구조가 아니라 network economics다.

2010 Long의 강점은 Durbin 규제가 interchange를 제한하더라도:

- Mastercard network fee pool
- cash-to-card migration
- switched transaction growth
- cross-border growth

이 모두 사라지는 것은 아니라고 구분한 것이다.

또 시작 valuation이 약 **12.3x EPS**로 낮았다.

실제 조정주가 기준:

**$20.54 → $449.23**

약 **+2,087%**, 배당 제외.

### 가장 중요한 교훈

> **Regulation이 payment chain의 어느 fee pool을 건드리는지 정확히 구분해야 한다.**

가맹점 총수수료를 Mastercard revenue로 보면 안 된다.

---

# 4. Global Payments — Network보다 Merchant Economics

GPN은 Mastercard와 달리 merchant acquiring / processing에 더 가깝다.

따라서 중요한 것은:

- merchant volume
- retention
- software attach
- ISO / partner economics
- M&A integration
- leverage

다.

2012 Long은 보안사고 뒤 약 10x FCF의 낮은 가격에서 샀다는 점이 강했다.

실제:

**$20.65 → $133.23**

약 **+545%**, 배당 제외.

다만 이후 GPN 같은 acquirer를 볼 때는 현금이 많다는 이유로 M&A를 공짜 option으로 보면 안 된다.

> **현금은 좋은 buyback의 재원이 될 수도 있고 비싼 인수의 재원이 될 수도 있다.**

---

# 5. PayPal — TPV와 Branded Economics를 분리

PayPal에서 가장 중요한 구분은:

## Branded checkout
PayPal button / wallet을 직접 이용하는 checkout.

상대적으로:
- 브랜드
- 소비자 trust
- merchant acceptance

를 monetization하기 때문에 높은 economics를 가질 수 있다.

## Unbranded processing
Braintree 등 merchant backend processing.

TPV는 크게 늘 수 있어도 take rate와 margin은 낮을 수 있다.

따라서:

**TPV growth ≠ PayPal economic growth**

다.

더 좋은 KPI는:

> **Transaction margin dollars**

이다.

---

# 6. PayPal 2016 vs 2021

## 2016 Long

$40.97에서 시작.

eBay 분사 뒤에도 standalone business가 충분히 가치 있고 Venmo는 option에 가까웠다.

2017년 말 $73.62.

약 **+80%**.

핵심은 Venmo monetization을 완벽히 맞혀야만 valuation이 성립한 게 아니라는 점이다.

## 2021 Long

$185에서 40% 급락한 뒤 싸다고 판단.

하지만 높은 valuation은 여전히:
- 높은 TPV growth
- branded economics 유지
- engagement 증가

를 요구했다.

실제 2024-01 가격 $61.35.

약 **-66.8%**.

가장 큰 오류:

> **Volume growth를 margin-dollar growth로 간주**

한 것이다.

Braintree mix가 커지면 TPV headline은 견조해도 shareholder economics가 약해질 수 있다.

---

# 7. Block — Gross Profit과 FCF/share의 차이

Block은:
- Seller
- Cash App

의 두 생태계를 갖고 있다.

초기에는 매우 강한 optionality가 있었다.

## 2016 Long

$12.94 수준에서:
- Seller unit economics
- 낮은 CAC / 빠른 payback
- Cash App option

을 샀다.

3년 후 $69.12.

약 **+434%**.

이건 좋은 성장주 setup이다.

> **검증된 core economics + 싸게 받은 신사업 option**

---

# 8. Block 2018 Short — 비싸다는 것만으로 부족

2018 Short는:
- Clover competition
- Square Capital cyclicality
- valuation

우려가 있었다.

하지만 주가는 중간에 **$268.07**까지 상승했다.

Short 입장에서는 치명적인 path였다.

핵심 오류는:

**현재 낮은 terminal margin 가정  
→ 즉시 equity downside**

로 연결한 것이다.

Cash App network expansion과 Seller ecosystem이 계속 커지는 동안 valuation-only Short는 버티기 어려웠다.

---

# 9. Block 2021 Long — 사업성장과 주식수익의 분리

2021 Long들은 사업성장을 상당 부분 맞혔다.

하지만 주가는:

- 2021-03 진입 약 $227.05 → $65.01, 약 **-71.4%**
- 2021-06 진입 약 $243.80 → $65.01, 약 **-73.3%**

로 무너졌다.

왜냐하면 동시에:

- 높은 starting multiple
- 금리상승 / duration compression
- Afterpay M&A
- SBC
- diluted share count 증가
- 성장 기대 정상화

가 작동했기 때문이다.

따라서:

> **Gross profit growth ≠ FCF/share growth ≠ stock return**

세 단계를 반드시 분리한다.

---

# 10. Payments 가치사슬 비교

| 회사 | 주된 위치 | 핵심 장점 | 핵심 위험 |
|---|---|---|---|
| MA | Card network | network effect / operating leverage | incentives, regulation |
| GPN | Merchant acquiring | merchant relationships / software | competition, M&A, leverage |
| PYPL | Wallet + checkout + processing | branded acceptance / consumer trust | unbranded mix, take-rate pressure |
| SQ | Seller + consumer ecosystem | two-sided optionality | SBC, valuation, M&A, credit |

---

# 11. Batch 013의 대표 성공/실패 유형

## 성공 유형 1 — Low multiple + strong network

대표:
- Mastercard 2010

## 성공 유형 2 — Event shock + cheap FCF

대표:
- GPN 2012

## 성공 유형 3 — Core economics로 하방 + 신사업 option

대표:
- PayPal 2016
- Square 2016

## 실패 유형 1 — TPV를 shareholder earnings로 등치

대표:
- PayPal 2021

## 실패 유형 2 — Gross profit growth에서 dilution을 누락

대표:
- Block 2021

## 실패 유형 3 — High valuation 자체를 Short catalyst로 사용

대표:
- Square 2018 Short

---

# 12. Batch 013에서 추출되는 V9 원칙

### 원칙 1
**TPV / GPV / GDV growth ≠ shareholder value growth**

### 원칙 2
**Mix를 반드시 본다**

Branded와 unbranded는 같은 $1 volume이 아니다.

### 원칙 3
**Take rate보다 transaction margin dollars가 더 중요할 수 있다**

### 원칙 4
**Gross profit 성장과 FCF/share 성장을 분리**

SBC와 dilution을 차감한다.

### 원칙 5
**M&A growth ≠ accretion**

Afterpay처럼 주식발행과 integration cost를 포함한다.

### 원칙 6
**Low starting multiple에서 option을 사는 구조가 강하다**

MA 2010, PYPL 2016, SQ 2016.

### 원칙 7
**Valuation-only Short는 위험하다**

Operating KPI break와 catalyst가 필요하다.

### 원칙 8
**Payment chain의 정확한 fee pool을 식별한다**

Interchange, network fee, acquiring spread, wallet take rate를 섞지 않는다.

---

# 13. 향후 정밀 Return / Unit Economics Pass

향후 일괄 보강:

1. exact posting-date close
2. split-adjusted price
3. dividend-adjusted total return
4. MFE / MAE
5. Short borrow / dividend carry
6. target 최초 도달일
7. 실제 holding IRR
8. TPV / GPV / GDV CAGR
9. branded vs unbranded mix
10. transaction margin dollars
11. gross profit / share
12. SBC / revenue
13. diluted share count
14. FCF/share CAGR

**거래량 성장만 보고 투자성과를 성공으로 판정하지 않는다.**
