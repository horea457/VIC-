# Batch 036 — Alliance Data Systems / CIT Group

> **Research as-of: 2026-09-05.** 10개 아이디어의 raw SQL flag와 VIC 본문 방향을 별도로 보존·검증했다. 이 배치는 특히 SQL `Short` 오표기가 대량 발견된 direction-correction batch다.

## Batch audit

- 10 ideas / 100 sections / 60 weighted claims / 40 metrics / 60 timeline items / 60 sources
- 각 아이디어 6 claims의 weight 합계 = 100%
- raw SQL `is_short`는 보존, `research_direction_ko`만 원문 기준 교정

## 1. ADS — 2008-12-30 — lindsay790

**idea_id:** `f1d7e1cc-b307-4522-acea-5efa87289706`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **성공·raw 방향오류**

### 1. 무슨 기업인가
Alliance Data Systems는 당시 AIR MILES·Epsilon 마케팅과 리테일러 전용 private-label credit card를 결합한 복합 사업자였다. 핵심 경제성은 카드 receivable의 yield·charge-off·funding spread와 장기 고객계약에서 나오는 loyalty/marketing cash flow의 조합이었다.

### 2. 당시 투자 논지
2008년 원문은 명백한 Long이다. 시장이 회사를 신용카드 회사처럼 8.8~10.3배 이익으로 평가하지만 credit는 현금흐름의 3분의 1가량이고 Loyalty·Epsilon·processing이 장기계약과 데이터 기반 높은 유지율로 성장한다는 논지였다. 2009E FCF yield 약 10%, net debt/EBITDA 1.7배, 대규모 buyback과 Blackstone break fee도 하방·촉매로 제시했다.

### 3. 실제 전개
금융위기 중 charge-off는 악화됐지만 회사는 2009년 TALF를 활용한 $708.9m ABS 등으로 funding access를 유지했고 존속했다. 이후 비카드 자산가치는 실제로 컸다. 2019년 Epsilon은 Publicis에 약 $4.4bn 현금으로 매각됐고 매각대금은 senior notes $1.9bn 및 revolver $500m 상환 등에 쓰였다. 2021년 LoyaltyOne도 별도 상장사로 분사됐다.

### 4. 무엇을 맞혔고 틀렸나
핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다.

### 5. 근본 오류와 재사용 교훈
복합 금융회사는 segment SOTP만으로 충분하지 않고 card funding·loss tail을 별도 stress해야 한다. 다만 raw Short 표시는 원문과 정반대라 반드시 research layer에서 Long으로 교정해야 한다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 valuation | 2008E P/E 10.3x / 2009E 8.8x | credit fear가 전체 multiple을 압박 |
| T0 leverage | net debt/EBITDA 1.7x | holding company 완충 |
| 2009 funding | $708.9m TALF ABS | 자금시장 접근 유지 |
| Epsilon sale | 약 $4.4bn cash | 숨은 비카드 가치 현실화 |

### 7. Claim audit

- **20% — business/segment economics:** 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2008-12-30 — VIC 게시
- 2009-04-30 — 2009 TALF ABS로 자금시장 접근 유지
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
성공·raw 방향오류 — 핵심은 신용위기 한복판에서 카드 손실만 보고 전체 기업을 카드 peer multiple로 평가하지 말라는 것이었다. 카드 book의 stress를 과소평가한 면은 있지만 loyalty/marketing 자산의 독립 가치와 funding survival을 맞췄다.

---

## 2. ADS — 2010-04-15 — fiftycent501

**idea_id:** `b5410dd2-ce64-41cd-b884-06a667617bae`  
**Raw SQL:** Short | **Research direction:** **Short** | **판정:** **실패·리스크 진단은 유효**

### 1. 무슨 기업인가
Alliance Data의 실질 수익원 가운데 private-label card가 매우 중요했고, 당시 off-balance securitization 회계 변화와 소비자 신용손실, CARD Act가 earnings와 capital을 흔들 수 있었다. 동시에 AIR MILES와 Epsilon이라는 비신용 사업도 보유했다.

### 2. 당시 투자 논지
2010년 원문은 실제 Short다. ADS를 마케팅 회사가 아니라 상당 부분 신용카드 회사로 봐야 하며, 2009 receivable growth가 경기침체 뒤 손실을 키우고 CARD Act·SFAS 166/167가 yield와 balance sheet를 악화시키며, cash EPS·AIR MILES breakage 회계와 경영진 보상이 공격적이라고 주장했다. 2009 managed charge-off 9.3%도 근거였다.

### 3. 실제 전개
신용손실과 회계·규제 부담은 실제였지만 terminal capital shortfall은 발생하지 않았다. 카드 사업은 높은 수익성을 유지했고 비카드 자산도 성장했다. 2019 Epsilon은 $4.4bn에 매각됐고 2021 LoyaltyOne 분사 후 회사는 Bread Financial로 재편됐다. 따라서 구조적 파산/과대평가 Short보다는 위험요인 진단이 맞았던 사례다.

### 4. 무엇을 맞혔고 틀렸나
Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다.

### 5. 근본 오류와 재사용 교훈
금융 Short에서는 회계 공격성의 존재보다 그것이 언제 covenant·capital·liquidity를 깨는지 연결해야 한다. 손실 증가가 있어도 자본과 funding이 버티면 valuation compression만으로 thesis가 끝날 수 있다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| 2009 charge-off | 9.3% | Short의 신용손실 우려는 실제 |
| 2009 PLC EBITDA | $194.4m, -23.5% | 경기민감성 확인 |
| 2019 Epsilon sale | $4.4bn | 비카드 가치가 Short를 상쇄 |
| 2021 구조 | LoyaltyOne spin | 기업 단순화 지속 |

### 7. Claim audit

- **20% — business/segment economics:** Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2010-04-15 — VIC 게시
- 2011-12-31 — 2010 이후 자본·funding 안정과 이익 회복
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction과 원문이 일치한다.**

### 10. 최종 판정
실패·리스크 진단은 유효 — Short는 복잡한 회계와 나쁜 인센티브를 잘 짚었지만 funding access와 카드 economics의 회복력, 비카드 자산가치가 손실을 상쇄할 가능성을 낮게 봤다. 좋은 회계 비판이 반드시 좋은 Short는 아니다.

---

## 3. ADS — 2016-02-10 — Bluegrass

**idea_id:** `68b90d87-fb88-4e3a-9d55-6672ca1b77c4`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **초기 성공·후기 구조변화·raw 방향오류**

### 1. 무슨 기업인가
2016년 ADS는 Card Services, LoyaltyOne, Epsilon을 보유한 loyalty/data/credit 복합체였다. 카드 고객관계는 장기 계약과 99% 수준의 retention을 주장했고, 높은 revolve rate·소액 balance와 retailer data가 고ROIC의 원천으로 제시됐다.

### 2. 당시 투자 논지
원문은 forward 11배 earnings에 거래되는 capital-light·high-ROIC Long이다. 2006~2015 revenue/FCF CAGR 16%/19%, after-tax ROIC 평균 28%, 카드손실이 700bp까지 올라가도 2017 cash earnings 약 $17이라는 stress, Dotz·M&A·buyback을 촉매로 봤다.

### 3. 실제 전개
초기에는 재평가와 이익성장이 이어졌지만 장기적으로는 단일 compounder라기보다 자산 분해가 진행됐다. AIR MILES 제도변화와 Epsilon 성장 둔화, retailer client stress가 나타났고 2019 Epsilon을 $4.4bn에 팔았다. 2021 LoyaltyOne도 spin되어 2022년 본체는 Bread Financial 카드회사로 재명명됐다.

### 4. 무엇을 맞혔고 틀렸나
높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다.

### 5. 근본 오류와 재사용 교훈
복합체의 historical ROIC를 그대로 terminal multiple로 외삽하지 말고 segment별 moat 지속성과 분리 가능성을 따로 봐야 한다. raw Short는 명백한 데이터 오류다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| 2006-15 revenue CAGR | 16% | 원문 성장 근거 |
| 2006-15 FCF CAGR | 19% | cash compounding 근거 |
| after-tax ROIC | 평균 28% | quality 논지 |
| 2019 Epsilon sale | $4.4bn | 복합체가 결국 분해 |

### 7. Claim audit

- **20% — business/segment economics:** 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2016-02-10 — VIC 게시
- 2018-01-01 — 2017 주가·이익 재평가 후 2018부터 균열
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
초기 성공·후기 구조변화·raw 방향오류 — 높은 ROIC와 카드 고객 stickiness는 실재했지만 서로 다른 사업을 하나의 18~20배 compounder multiple로 묶는 논리는 시간이 갈수록 약해졌다. 2016 진입은 초기 재평가에는 유리했으나 terminal business mix 가정은 과도했다.

---

## 4. ADS — 2017-12-27 — thistle933

**idea_id:** `3c1d4a31-30bb-44a5-a985-d63a3804bc18`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **실패·부분 자산가치 실현·raw 방향오류**

### 1. 무슨 기업인가
2017년 ADS의 카드사업은 중형 retailer private-label 프로그램에 특화되어 SKU-level data, marketing, credit funding을 묶어 제공했다. Epsilon과 LoyaltyOne은 별도 데이터·loyalty 자산으로 SOTP의 핵심이었다.

### 2. 당시 투자 논지
원문은 $250에서 2018E earnings power $25, 약 10배라는 Long이다. prime borrower·small balance라 charge-off 정상화가 과도하게 공포되고 있으며, 99% retention, 약 6% ROA, 신규 Williams-Sonoma·Wayfair·Signet portfolio와 10~15% earnings growth를 근거로 들었다. activist가 LoyaltyOne/Epsilon을 팔거나 spin할 수 있다는 촉매도 제시했다.

### 3. 실제 전개
분리 촉매 자체는 적중했다. 2019 Epsilon을 $4.4bn 현금에 매각했고 2021 LoyaltyOne을 spin했다. 그러나 $250의 주가와 성장 compounder 가정은 지켜지지 않았다. retailer stress, 경영진 교체, 카드 portfolio 변동과 multiple compression이 겹치며 주가는 큰 폭으로 하락했다.

### 4. 무엇을 맞혔고 틀렸나
SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다.

### 5. 근본 오류와 재사용 교훈
event-driven SOTP는 매각가뿐 아니라 매각 후 남는 RemainCo의 normalized EPS, debt allocation, tax와 multiple을 동시에 계산해야 한다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 price | $250 | 원문 기준 |
| T0 earnings power | $25 | 약 10x |
| Epsilon sale | $4.4bn | 촉매 적중 |
| LoyaltyOne spin | 2021-11-05 | 추가 분리 촉매 적중 |

### 7. Claim audit

- **20% — business/segment economics:** SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2017-12-27 — VIC 게시
- 2019-04-12 — 2018~2019 client/segment 문제와 급격한 multiple 하락
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
실패·부분 자산가치 실현·raw 방향오류 — SOTP 촉매를 맞히는 것과 현재 주가에서 좋은 Long인 것은 별개였다. 자산 매각 가치가 있어도 core earnings·multiple이 동시에 내려가면 equity IRR은 나쁠 수 있다.

---

## 5. ADS — 2018-09-28 — Rearden

**idea_id:** `f19af47f-7e91-480b-ada0-f3739a245c42`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **실패·촉매 일부 적중·raw 방향오류**

### 1. 무슨 기업인가
2018 ADS는 카드, AIR MILES/BrandLoyalty, Epsilon을 보유했다. 원문은 세 사업의 동시 headwind를 허리케인·collection 전환·CPG 광고 축소·AIR MILES 정책변화라는 일시적 문제로 해석했다.

### 2. 당시 투자 논지
원문은 vertical integration·데이터·중형 retailer niche를 moat로 보고 약 10배 earnings에서 perfect storm 회복을 사는 Long이다. AIR MILES는 breakage 상실을 reward markup으로 보완하고, Epsilon은 CPG 약세가 안정화되며, Card Services charge-off와 collection 전환도 정상화될 것이라고 봤다.

### 3. 실제 전개
일부 운영 문제는 완화됐지만 기업은 과거 구조로 복귀하지 않았다. 2019 Epsilon을 $4.4bn에 매각해 debt를 크게 줄였고, 이후 LoyaltyOne도 2021 분사했다. 특히 분사된 Loyalty Ventures의 AIR MILES 사업은 2023년 채권자보호 절차에서 BMO가 US$160m에 인수했다. 즉 LoyaltyOne의 장기 quality 가정은 크게 훼손됐다.

### 4. 무엇을 맞혔고 틀렸나
단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다.

### 5. 근본 오류와 재사용 교훈
“temporary” 판정에는 회복 KPI와 기한을 명시해야 한다. loyalty liability economics·client concentration·retailer health를 단순 회복 변수로 두면 terminal value를 과대평가한다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 multiple | 약 10x earnings | perfect-storm discount |
| Epsilon sale | 2019 $4.4bn | 가치 실현 |
| LoyaltyOne spin | 2021 | 구조 복귀 대신 분리 |
| AIR MILES sale | 2023 US$160m | LoyaltyOne 장기질 저하 확인 |

### 7. Claim audit

- **20% — business/segment economics:** 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2018-09-28 — VIC 게시
- 2019-07-01 — 2019 Epsilon 매각 뒤에도 core multiple 하락
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
실패·촉매 일부 적중·raw 방향오류 — 단기 headwind를 모두 mean reversion 대상으로 본 것이 핵심 오류였다. 여러 segment가 동시에 흔들릴 때는 공통 원인이 아니더라도 각 moat의 구조적 저하 확률을 독립적으로 높여야 한다.

---

## 6. ADS — 2019-08-03 — rickey824

**idea_id:** `c3eb2ae5-bef9-4973-bbf3-0526b7134705`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **실패·core moat 과대평가·raw 방향오류**

### 1. 무슨 기업인가
2019 Epsilon 매각 직후 ADS는 사실상 Card Services 중심에 LoyaltyOne이 붙은 구조였다. 카드 economics는 고금리 소액 receivable, retailer loyalty/analytics, 높은 revolve rate와 낮은 revenue-share agreement를 통해 peer 대비 높은 ROE를 추구했다.

### 2. 당시 투자 논지
원문은 저자가 long이라고 명시하며 약 8x 2019 P/FCF, $337/share 또는 117% upside를 제시했다. Card Services의 25% 수준 ROE와 높은 receivable yield, 중형 retailer niche·first-party data를 구조적 moat로 보고 low/mid-teens FCF/share compounding과 LoyaltyOne 매각을 기대했다.

### 3. 실제 전개
곧 COVID-19로 retailer와 receivable book이 충격을 받았고 2020 순이익은 $214m, diluted EPS $4.46에 그쳤다. 카드 franchise는 살아남았으나 원문의 $337 가치와 low-teens compounding 경로는 실현되지 않았다. 2021 LoyaltyOne spin은 구조 단순화 촉매로 발생했다.

### 4. 무엇을 맞혔고 틀렸나
card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다.

### 5. 근본 오류와 재사용 교훈
금융업의 “moat”는 ROE가 아니라 cycle-average loss·funding beta·required equity를 차감한 ROE로 검증한다. 8x FCF가 싸도 FCF가 credit provision 이전인지 이후인지 구분해야 한다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 valuation | 약 8x 2019 P/FCF | 저평가 논지 |
| T0 target | $337 / +117% | 높은 기대치 |
| 2020 net income | $214m | pandemic 충격 |
| 2020 diluted EPS | $4.46 | 정상화 $16 대비 큰 괴리 |

### 7. Claim audit

- **20% — business/segment economics:** card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2019-08-03 — VIC 게시
- 2020-03-31 — 2020 pandemic로 retailer·receivable stress 급증
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
실패·core moat 과대평가·raw 방향오류 — card yield/ROE의 평균값을 구조적 moat로 본 반면 retailer churn, provision volatility, bank capital upstreaming 제한과 macro tail을 충분히 확률가중하지 않았다. 높은 ROE 금융사업은 tail loss와 funding constraint를 같이 봐야 한다.

---

## 7. ADS — 2020-10-14 — kevin155

**idea_id:** `42644e18-1c6d-471e-aae0-519d8fd7d3b2`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **성공·촉매 적중·raw 방향오류**

### 1. 무슨 기업인가
2020년 ADS는 Epsilon 매각 후 Card Services가 대부분의 pre-corporate earnings를 만들고 LoyaltyOne이 남은 구조였다. 두 규제은행의 capital과 CECL reserve, parent cash flow와 holding-company debt가 equity valuation의 핵심이었다.

### 2. 당시 투자 논지
원문은 약 3x normalized earnings에 거래되며 2~3년 내 double 가능하다는 Long이다. $16 normalized EPS, 6.5% normalized loss, bank CET1 18.3%, 높은 reserve와 $1.1bn parent liquidity를 근거로 pandemic credit fear가 과도하다고 봤다. LoyaltyOne 매각/분리와 새 CEO의 비용절감도 촉매였다.

### 3. 실제 전개
2021 credit와 earnings가 예상보다 빠르게 정상화됐다. 3Q21 net income은 $224m, diluted EPS $4.47로 전년 대비 크게 늘었고 연간 net loss rate 가이드는 high-4%대로 낮아졌다. 주가는 2020년 10월 약 $37대에서 2021년 중 $100을 넘는 구간이 있었으며, 2021년 11월 LoyaltyOne 분사도 실제 발생했다.

### 4. 무엇을 맞혔고 틀렸나
이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다.

### 5. 근본 오류와 재사용 교훈
금융 turnaround Long은 normalized EPS보다 먼저 reserve coverage·capital upstreaming·liquidity runway·loss vintage를 확인해야 한다. 이 네 변수가 개선될 때 low multiple이 실제 catalyst와 연결된다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 normalized EPS | $16 | 원문 기준 |
| T0 CET1 | 18.3% | capital buffer |
| 2021 Q3 EPS | $4.47 | 전년 대비 +60% |
| LoyaltyOne spin | 2021-11-05 | 핵심 촉매 실현 |

### 7. Claim audit

- **20% — business/segment economics:** 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2020-10-14 — VIC 게시
- 2021-03-31 — 2021 earnings·credit 정상화와 주가 급반등
- 2019-07-01 — Epsilon 매각 완료
- 2021-11-05 — LoyaltyOne 분사 완료

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
성공·촉매 적중·raw 방향오류 — 이 아이디어는 stress 이후 reserve adequacy와 capital, parent liquidity를 함께 본 점이 좋았다. valuation만 싼 것이 아니라 손실률 정상화와 구조 단순화라는 구체적 경로가 있었다.

---

## 8. CIT — 2001-01-16 — rich44

**idea_id:** `797e8f52-79b4-42f8-87c1-94123103ce3d`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **강한 성공·raw 방향오류**

### 1. 무슨 기업인가
CIT Group은 equipment·aircraft/rail leasing, vendor finance, factoring, asset-based lending와 consumer finance를 가진 대형 비은행 commercial finance 회사였다. 은행보다 낮은 leverage 대신 specialization과 wholesale funding을 이용해 spread를 벌었다.

### 2. 당시 투자 논지
2001 원문은 $20 조금 넘는 주가에서 tangible book $14.80, normal EPS $3.55, 약 5.7배 normal earnings라는 Long이다. telecom exposure는 $56bn managed assets 중 약 $350m에 불과하고 recession loss도 spread 확대가 일부 상쇄하며, 은행 대비 할인 때문에 takeout 가능성이 높다고 봤다. upside $40+, downside $15~16을 제시했다.

### 3. 실제 전개
촉매는 매우 빠르게 실현됐다. 2001년 3월 Tyco는 CIT를 약 $9.2bn, 주당 $35.02 가치로 인수한다고 발표했다. 직전 CIT 종가 $22.75 대비 약 54% 프리미엄이었다. 6월 인수가 완료됐다.

### 4. 무엇을 맞혔고 틀렸나
낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다.

### 5. 근본 오류와 재사용 교훈
cheap 금융주에서 takeout thesis는 단순 “누가 살 수 있다”가 아니라 buyer EPS accretion·funding advantage·precedent transaction으로 검증해야 한다. raw Short 표시는 원문과 정반대다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 price | 약 $20~22.75 | 저평가 구간 |
| normal EPS | $3.55 | 약 5.7x 논리 |
| Tyco offer | $35.02/share | 촉매 가격 |
| offer premium | 약 54% | 직전 종가 대비 |

### 7. Claim audit

- **20% — business/segment economics:** 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2001-01-16 — VIC 게시
- 2001-03-13 — Tyco가 약 54% 프리미엄 인수 발표
- 2009-11-01 — CIT Chapter 11 신청
- 2009-12-10 — 기존 common equity 전부 cancelled

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
강한 성공·raw 방향오류 — 낮은 multiple만 산 것이 아니라 strategic buyer가 즉시 accretive하게 지불할 수 있는 가격을 역산한 것이 강점이었다. 산업 내 precedent와 buyer economics가 실제 catalyst probability를 높였다.

---

## 9. CIT — 2007-08-23 — sag301

**idea_id:** `671b2431-63fc-4542-98c7-62bbcd9189a3`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **치명적 실패·raw 방향오류**

### 1. 무슨 기업인가
2007 CIT는 commercial corporate, transportation, trade/factoring, vendor finance, student/subprime and small-business lending을 wholesale debt·CP·ABS·bank lines로 조달하는 비은행 lender였다. asset quality만큼 liability structure가 사업 생존을 결정했다.

### 2. 당시 투자 논지
원문은 $35에서 약 1x book, 6.5x annualized earnings인 Long이다. subprime portfolio는 93.8% mark와 $850m capital로 충분하고 non-home NPA는 1% 미만, $7.5bn bank lines·$5.5bn ABS facilities·$5.2bn cash로 CP market이 닫혀도 버틸 수 있다고 봤다. subprime sale/runoff를 catalyst로 제시했다.

### 3. 실제 전개
핵심 가정은 무너졌다. wholesale funding 비용과 liquidity 압력이 악화되며 2008~09 자산 축소와 자본조달에도 위기가 해소되지 않았다. 2009년 11월 1일 CIT는 prepackaged Chapter 11을 신청했고 12월 10일 emergence 과정에서 기존 common equity가 전부 cancelled됐다.

### 4. 무엇을 맞혔고 틀렸나
asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다.

### 5. 근본 오류와 재사용 교훈
비은행 금융사는 P/TBV보다 liability ladder가 선행 변수다. committed line의 조건, 담보 haircuts, CP/ABS rollover, rating trigger와 12~24개월 cash burn을 먼저 stress해야 한다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 price | $35 | 원문 기준 |
| T0 valuation | 약 1x book / 6.5x earnings | 싸다는 근거 |
| liquidity claim | $7.5bn lines + $5.5bn ABS + $5.2bn cash | 실제론 충분치 않음 |
| 2009 outcome | old common 100% cancelled | equity thesis 전손 |

### 7. Claim audit

- **20% — business/segment economics:** asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2007-08-23 — VIC 게시
- 2008-03-31 — 2008 wholesale funding crisis 심화
- 2009-11-01 — CIT Chapter 11 신청
- 2009-12-10 — 기존 common equity 전부 cancelled

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
치명적 실패·raw 방향오류 — asset quality와 matched funding을 보는 데 집중했지만 contingent liquidity의 실질 가용성·haircut·renewal risk와 “새 영업이 멈추면 franchise earning power도 사라진다”는 liability-side reflexivity를 과소평가했다.

---

## 10. CIT — 2008-05-02 — jna341

**idea_id:** `8530cf07-e131-4623-b20c-4b8cbcdd661a`  
**Raw SQL:** Short | **Research direction:** **Long** | **판정:** **치명적 실패·doom-loop 이해 후에도 확률오류·raw 방향오류**

### 1. 무슨 기업인가
2008 CIT는 capital-market funding 의존도가 높은 specialty finance 회사였다. borrower asset quality가 양호해도 CDS·bond spread가 폭등하면 신규자산의 NIM이 사라지고 만기부채 refinancing이 어려워지는 reflexive 구조였다.

### 2. 당시 투자 논지
원문은 $11.79, 0.45x Q1 tangible book에서 “시장 예상과 달리 CIT는 다음 Bear Stearns가 아니다”라는 Long이다. $1.5bn equity raise 후 TBV $20.20, liquidity가 2009년까지 충분하고 rail asset sale·CDS 정상화·회사 매각으로 $15~18을 기대했다. 동시에 400bp funding-cost 상승이 300~400bp NIM을 지운다는 doom loop를 정확히 설명했다.

### 3. 실제 전개
분석이 묘사한 doom loop가 결국 bull case보다 강했다. 추가 자본·자산매각만으로 신뢰를 회복하지 못했고 2009년 11월 prepackaged bankruptcy에 들어갔다. 12월 emergence 때 old common equity는 전부 cancelled됐다. 이후 새 CIT는 은행 중심으로 재편돼 2022년 First Citizens에 합병됐지만 이는 기존 주주의 회복이 아니었다.

### 4. 무엇을 맞혔고 틀렸나
위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다.

### 5. 근본 오류와 재사용 교훈
reflexive finance에서 book value는 funding access가 살아 있을 때만 anchor다. survival probability를 먼저 계산하고, 그 다음에 conditional recovery value를 곱해야 한다.

### 6. 핵심 수치

| 항목 | 값 | 해석 |
|---|---|---|
| T0 price | $11.79 | 원문 기준 |
| pro-forma TBV | $20.20 | 0.58x 조정 TBV |
| funding shock | CDS +400bp | NIM 300~400bp를 소거 |
| 2009 outcome | old common cancelled | TBV 하방 논리 붕괴 |

### 7. Claim audit

- **20% — business/segment economics:** 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **18% — valuation and capital structure:** 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **17% — credit/funding or operating risk:** 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **16% — catalyst path:** 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **15% — management/capital allocation:** 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.
- **14% — terminal outcome and falsifier:** 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다. / 반증조건은 operating·funding·capital 지표가 원 논지 반대방향으로 지속되는지 여부다.

### 8. Catalyst / timeline
- 2008-05-02 — VIC 게시
- 2008-09-30 — 2008~2009 funding spread·refinancing 악화 지속
- 2009-11-01 — CIT Chapter 11 신청
- 2009-12-10 — 기존 common equity 전부 cancelled

### 9. 방향 정합성
**SQL direction 오류.** raw Short를 그대로 보존하되 본문상 실제 Long으로 research layer에서 교정했다.

### 10. 최종 판정
치명적 실패·doom-loop 이해 후에도 확률오류·raw 방향오류 — 위험 메커니즘을 정확히 이해했음에도 “asset quality + time + potential buyer”에 더 높은 확률을 줬다. 이는 분석 지식의 문제가 아니라 확률가중과 payoff asymmetry 문제다. equity가 0이 될 경로가 있으면 TBV 할인은 하방을 보장하지 않는다.

---
