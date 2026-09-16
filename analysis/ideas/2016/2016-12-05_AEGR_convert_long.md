# Aegerion Pharmaceuticals (AEGR) — 2016-12-05 VIC Convertible Long

> **Idea unit:** 이 게시일·증권 한 건만 분석한다. 같은 ticker의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-16. 원 SQL 방향은 Long이며, 실제 분석 증권은 common이 아니라 **Aegerion 2.0% senior unsecured convertible notes due 2019**다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Aegerion Pharmaceuticals / AEGR, merger 후 Novelion Therapeutics 산하 |
| VIC 게시일 / 작성자 | 2016-12-05 / offtherun |
| 분석 증권 / 실제 방향 | 2.0% senior unsecured convertible notes due 2019 / Long |
| 원 SQL 방향 | Long — 방향 일치 |
| 기준 진입가격 | mid-to-high 60s of par |
| 원문 기대수익 | YTM high teens, spread tightening 시 mid-80s |
| 핵심 T0 자산 | Juxtapid, Myalept, QLT091001/Zuretinol, pro forma cash 약 $119m |
| 실제 경로 | cash burn·추가 senior financing → 2019 Chapter 11 |
| Plan상 Class 6B estimated recovery | 약 **80.7%** |
| 최종 판정 | **security payoff는 부분 성공 가능 / operating·refinancing thesis 실패** |

> **결론:** 원문은 mid/high-60s에 거래되던 2% convert가 cash-flow breakeven과 신약 optionality로 mid-80s까지 rerate될 수 있다고 봤다. 실제 회사는 breakeven에 안착하지 못하고 2018년 secured bridge debt를 얹은 뒤 2019년 Chapter 11에 들어갔다. 다만 plan disclosure에서 convert가 포함된 Class 6B general unsecured claims의 estimated recovery는 약 80.7%였다. 따라서 **기업 turnaround는 실패했지만 entry가 60대였다면 claim recovery가 원금을 완전히 파괴한 구조는 아니었다.** 실제 분배시점·신주/신규 convert 가치가 없으므로 exact realized IRR은 확정하지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

Aegerion은 희귀질환 치료제를 개발·판매하던 바이오제약사다. 핵심 상업자산은 HoFH 치료제 **Juxtapid(lomitapide)**와 generalized lipodystrophy 치료제 **Myalept(metreleptin)**였다. 2016년 QLT와 결합해 Novelion Therapeutics 산하가 되면서 retinal disease 후보물질 QLT091001/Zuretinol도 포트폴리오에 추가됐다.

이 아이디어의 payoff는 common equity가 아니라 **subsidiary-level unsecured convertible claim**이다. 따라서 `drug sales - operating burn - secured/new-money claims = unsecured recovery pool`을 먼저 보고, 그 뒤에 convert의 coupon·par accretion·conversion optionality를 본다. parent의 현금이 자동으로 Aegerion noteholders에게 귀속되는 것도 아니다.

### 매 분기 볼 핵심 KPI

Juxtapid·Myalept revenue, operating cash burn, unrestricted/restricted cash, secured debt 추가, parent/sub structural subordination, maturity wall, Myalept value, pipeline progress, convert price/yield

---

## 2. 당시 상황과 시장이 가격에 넣은 것

2016년 11월 QLT와의 merger가 종결된 직후였다. 원문은 pro forma 연말 cash를 약 $119m로 보고, convert가 post-merger business를 약 $153m에 create한다고 계산했다. 현금을 모두 0으로 쳐도 약 $272m에 create한다는 논리였다.

그러나 이 bond는 parent guarantee나 lien이 없는 Aegerion의 senior unsecured obligation이었다. 원문도 intercompany loan과 향후 secured debt가 convert 위에 쌓일 수 있다는 점을 분명히 위험요인으로 적었다.

### Reverse expectations

가격이 60대라는 것은 단순히 rare-disease assets가 싸다는 뜻이 아니라 **2019년까지 현금이 남고, 추가 senior claims가 recovery를 잠식하지 않을 것**이라는 조건이 필요했다. bond의 cheapness는 EBITDA multiple이 아니라 legal waterfall과 burn-to-maturity의 함수였다.

---

## 3. 원문 투자논지 지도

### C1. AEGR 사업이 2017년 breakeven에 근접한다 — 실패

**원문 주장:** 비용절감과 Juxtapid/Myalept로 2017년 말 cash-flow breakeven/positive.

**경제적 메커니즘:** burn 감소 → maturity까지 liquidity runway 연장 → spread tightening.

**숨은 가정:** 약가·수요 압력과 compliance 비용이 안정되고 추가 rescue capital이 senior하지 않다.

**사전 반증조건:** 분기 burn 지속, secured borrowing 증가, 2019 maturity refinancing 불확실성 확대.

**실제 결과:** 2018년에도 debt·liquidity 압박이 심했고, 2019년 Chapter 11에 진입했다.

### C2. pro forma cash가 downside를 보호한다 — 실패/제한

현금은 시간이 흐르며 운영손실과 구조조정 비용에 소모됐다. 또한 subsidiary claim 관점에서는 parent-level cash를 동일하게 보아서는 안 됐다.

**재사용 교훈:** biotech distress의 cash는 liquidation value가 아니라 **burn rate와 법적 접근권을 차감한 runway**다.

### C3. Myalept/Juxtapid/Zuretinol asset value가 recovery를 만든다 — 부분 성공

회사는 파산했지만 unsecured class에 0이 아닌 상당한 value가 배정됐다. plan은 Class 6B estimated recovery를 약 80.7%로 제시했다. 다만 이는 plan estimate이며 최종 현금 IRR과 동일하지 않다.

### C4. bond가 mid-80s로 rerate될 수 있다 — 경로 실패

원문이 기대한 정상적 spread compression이 아니라 restructuring을 통해 value가 회수됐다. **가격목표에 도달했는지보다 어떤 경로로 payoff가 생겼는지가 다르다.**

### C5. unsecured layer가 추가 senior debt에 크게 훼손되지 않는다 — 실패

2018년 Aegerion은 $50m new-money secured first-lien term loans를 조달했고 일부 convert를 par에 retire하는 roll-up도 실행했다. 남은 unsecured noteholder의 구조적 위치는 2016년보다 나빠졌다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 단순 구조는 다음과 같다.

`entry 65~69 + 2% coupon + pull-to-par / maturity risk`

그러나 실제 distress 구조는:

`enterprise recovery - DIP/secured/bridge/intercompany senior claims = general unsecured recovery pool`

로 봐야 한다.

### 시나리오 분석

| 시나리오 | T0 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | burn 지속·senior layering | recovery < entry | 구조적으로 현실화 위험 확대 |
| Base | 2017 breakeven·spread tightening | mid-80s + coupon | 실패 |
| Bull | pipeline/asset monetization | par 이상/convert option | 미실현 |
| Restructuring actual | Chapter 11 | claim recovery | Class 6B estimated 80.7% |

### 핵심 수치

| 지표 | T0 | 실제/사후 | 판정 |
|---|---:|---:|---|
| Convert coupon | 2.0% | 2.0% senior unsecured | 일치 |
| Maturity | 2019-08-15 | maturity 전 Chapter 11 | 실패 |
| Entry | mid/high 60s | — | — |
| Target | mid-80s | 정상적 rerating 미확인 | 실패 |
| Class 6B plan recovery | — | ~80.7% estimate | 부분 보호 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2016-11-29 | Aegerion/QLT merger 완료 | Novelion 구조 출범 |
| 2016-12-05 | VIC convert Long | mid/high-60s entry |
| 2018-11 | secured bridge financing | unsecured recovery layer 악화 |
| 2019-05-20 | Aegerion Chapter 11 filing / RSA | 정상 refinancing thesis 실패 |
| 2019 | disclosure statement | Class 6B estimated recovery ~80.7% |
| 2019 | Amryt-led restructuring | creditors receive new securities/equity components |

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

회사가 파산했다는 사실만으로 이 convert를 0으로 판정하면 안 된다. 반대로 disclosure의 80.7%를 현금 80.7c recovery로 단순 대입해 realized IRR을 만들 수도 없다. distribution은 new convertible notes와 new common stock 등으로 구성됐고 지급시점·시장가치가 필요하다.

따라서 이 아이디어는 **enterprise thesis 실패 / claim-value preservation 부분 성공**으로 판정한다.

---

## 7. Claim별 사후 판정

| Claim | Weight | 판정 | 핵심 gap |
|---|---:|---|---|
| 2017 breakeven | 25% | 실패 | Chapter 11까지 liquidity stress 지속 |
| cash downside protection | 20% | 실패/제한 | burn·structural access를 과대평가 |
| asset recovery value | 20% | 부분 성공 | unsecured class에 의미 있는 recovery |
| mid-80s spread rerating | 20% | 실패 | 정상화 대신 restructuring |
| senior layering 제한 | 15% | 실패 | 2018 first-lien bridge 추가 |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

가장 중요한 driver는 신약 매출이 아니라 **2016년 entry discount와 2019년 restructuring waterfall**이었다. distress credit에서 company narrative보다 claim seniority·new-money priming·법적 entity가 최종 payoff를 더 직접적으로 결정했다.

### Counterfactual

같은 자산을 common으로 샀다면 결과가 어땠을까? existing equity는 restructuring에서 소멸한 반면 unsecured claim에는 estimated recovery가 남았다. 이 차이가 security selection의 가치다.

---

## 9. 분석 오류 유형과 최초 경고

원문은 senior unsecured라는 약점을 인식했지만 pro forma cash와 drug asset value를 다소 정적인 balance-sheet protection처럼 취급했다. 최초 경고는 **cash burn이 기대만큼 줄지 않는데 secured debt가 추가되는 순간**이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. biotech distress는 cash balance가 아니라 burn-to-maturity를 본다.
2. parent와 operating subsidiary의 cash·debt를 entity별로 분리한다.
3. unsecured convert는 향후 DIP·first-lien debt에 얼마나 primed될 수 있는지 본다.
4. plan estimated recovery와 realized cash IRR을 동일시하지 않는다.
5. 기업 파산과 채권 손실률은 별개의 질문이다.

### 지금 같은 아이디어를 다시 본다면

- exact principal outstanding
- entity-level cash
- secured/intercompany claims
- monthly burn
- maturity/refinancing source
- plan class treatment
- distribution-date market values

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 실패 |
| Valuation thesis | 부분 성공 가능 |
| Catalyst thesis | 정상화 catalyst 실패 |
| Timing / path | restructuring으로 경로 변경 |
| Security selection | common 대비 우월 |
| Thesis score | 6.3/10 |
| Process score | 9.3/10 |
| 종합 | **operating thesis 실패 / unsecured claim recovery는 의미 있게 남음** |

### 한 문장 교훈

> distress에서 ‘회사가 파산했는가’보다 ‘내 claim이 어느 entity에서 누구 뒤에 서 있는가’가 투자수익을 결정한다.

---

## 12. Sources / Validation Notes

1. VIC original / uploaded SQL, 2016-12-05 — T0 thesis, convert price, cash·asset assumptions.
2. [Novelion 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/827809/000082780919000005/nvln-12312018x10k.htm) — 2% notes due 2019, entity structure, liquidity and debt.
3. [Aegerion 2018 bridge financing 8-K](https://www.sec.gov/Archives/edgar/data/827809/000110465918066850/a18-39805_18k.htm) — new first-lien bridge and roll-up loans.
4. [Aegerion Chapter 11 / RSA 8-K](https://www.sec.gov/Archives/edgar/data/827809/000110465919030677/a19-10251_18k.htm) — May 20, 2019 filing and consenting noteholders.
5. [Aegerion Disclosure Statement](https://www.sec.gov/Archives/edgar/data/827809/000110465919040380/a19-12814_1ex10d2.htm) — Class 6B treatment and ~80.7% estimated recovery.

### 데이터 품질

- T0 원문·metadata: **A** — uploaded SQL 원문.
- capital structure / restructuring: **A** — SEC filings and court disclosure statement.
- realized return: **C/미확정** — distribution dates and security market values are not fully reconstructed; exact IRR을 만들지 않았다.
