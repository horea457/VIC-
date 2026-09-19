# Advent Claymore Convertible Securities and Income Fund II (AGC) — 2016-01-17 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-19. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Advent Claymore Convertible Securities and Income Fund II / AGC |
| VIC 게시일 / 작성자 | 2016-01-17 / jcoviedo |
| 분석 증권 / 실제 방향 | NYSE:AGC leveraged closed-end-fund common shares / Long |
| 원 SQL 방향 | Short — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | NAV 대비 약 18.95% 할인 |
| 기대기간 | 1~3년 discount closure와 distributions |
| raw horizon audit | liquid marked portfolio, 월 $0.047 distribution, activist/tender·liquidation optionality |
| 최종 판정 | **강한 성공 — 할인 축소·tender·NAV merger 실현** |

> **결론:** 대부분 Level 1/2인 portfolio를 약 18.95% 할인에 산 thesis였다. FY2017 말 할인은 약 8%로 줄었고, 2017년 15% tender와 2018년 AVK NAV-for-NAV 합병이 이어졌다. 분배금의 return-of-capital과 leverage 위험을 감안해도 discount catalyst는 명확히 적중했다.

---

## 1. 회사는 정확히 무엇을 하는가

AGC는 convertible securities와 non-convertible income securities를 보유하고 covered calls를 병행한 leveraged closed-end fund였다. 보통주는 portfolio NAV에서 leverage와 비용을 부담한 residual claim이며, 거래가격은 NAV와 별개로 할인·할증된다. 따라서 수익은 underlying NAV, 분배금, 할인율 변화와 tender·합병 같은 구조적 촉매의 합이다.

`common return = NAV return + distributions + discount change - leverage/expense drag`; 분배금 중 return of capital과 NAV-for-NAV corporate action을 따로 기록한다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

NAV/share, market price, discount/premium, NAV·market total return, distribution composition, leverage ratio/cost, expense ratio, Level 1/2/3 mix, tender acceptance, merger ratio

---

## 2. 당시 상황과 시장이 가격에 넣은 것

AGC는 convertibles·high yield를 보유했지만 보통주는 NAV보다 약 18.95% 낮게 거래됐다. 월 $0.047 distribution은 약 11.4% headline yield를 제공했고, 투자자 activism·tender·liquidation이 discount를 닫을 선택지였다. investments가 net assets의 약 174.5%로 leverage가 높다는 점이 핵심 반대항이었다.

### Reverse expectations

시장은 credit-sensitive assets, expensive leverage, covered-call drag, management fee와 distribution 중 return of capital을 할인했다. 즉 19% discount가 공짜가 아니라 NAV 변동성과 지속적으로 소모될 수 있는 분배정책의 가격일 수 있었다.

---

## 3. 원문 투자논지 지도

### C1. 약 18.95% NAV discount — 강한 성공

**원문 주장**

liquid portfolio에 비해 market discount가 과도하다.

**경제적 메커니즘**

NAV가 유지되면 할인 19%→10%만으로 약 11% 가격 uplift가 생긴다.

**T0 근거**

원문 NAV·price와 mostly Level 1/2 holdings.

**숨은 가정**

NAV marks가 realizable하고 fees가 value를 소모하지 않는다.

**사전 반증조건**

NAV 하락과 discount 20%+ 고착이면 반증.

**실제 결과**

FY2017말 discount 약 8%.

**정량 gap**

약 11%p 축소.

**분석 오류 또는 제한**

point NAV의 credit beta를 작게 봤다.

**재사용 교훈**

discount와 NAV를 두 개의 독립 return driver로 기록한다.

### C2. NAV quality는 충분히 투명 — 성공

**원문 주장**

portfolio가 사모·Level 3가 아니라 marked securities 중심이다.

**경제적 메커니즘**

observable marks는 liquidation-value uncertainty를 줄인다.

**T0 근거**

Level 1/2 비중과 listed fixed-income holdings.

**숨은 가정**

marks가 stressed bid와 크게 다르지 않다.

**사전 반증조건**

Level 3·illiquid 비중 급증 시 반증.

**실제 결과**

tender와 merger가 NAV 근접 기준으로 실행됐다.

**정량 gap**

NAV conversion까지 검증.

**분석 오류 또는 제한**

market liquidity와 credit liquidity를 혼동할 수 있다.

**재사용 교훈**

valuation hierarchy와 position liquidity를 따로 본다.

### C3. 11.4% distribution carry — 부분 성공

**원문 주장**

월 $0.047가 waiting return을 제공한다.

**경제적 메커니즘**

현금분배가 discount catalyst를 기다리는 carry가 된다.

**T0 근거**

연환산 headline yield 약 11.4%.

**숨은 가정**

분배가 portfolio income·realized gain으로 충당된다.

**사전 반증조건**

ROC 확대·NAV erosion이면 약화.

**실제 결과**

분배는 지속됐지만 2015 distributions 일부는 ROC였다.

**정량 gap**

headline yield 전부가 economic return은 아님.

**분석 오류 또는 제한**

yield를 earning power로 등치했다.

**재사용 교훈**

NAV total return과 tax character를 같이 본다.

### C4. 15% tender optionality — 강한 성공

**원문 주장**

activism이 NAV 근접 tender를 유도할 수 있다.

**경제적 메커니즘**

일부 shares를 98% NAV에 매입하면 accepted holder payoff와 전체 discount anchor가 생긴다.

**T0 근거**

activist pressure와 board options.

**숨은 가정**

board가 action하고 shareholders가 참여한다.

**사전 반증조건**

tender 부재·deep haircut이면 실패.

**실제 결과**

2017 최대 15% tender, oversubscribed, 33% proration.

**정량 gap**

$6.4876·98% NAV.

**분석 오류 또는 제한**

15%를 전체 exit처럼 보면 안 된다.

**재사용 교훈**

size·proration·tax를 position cash-flow에 넣는다.

### C5. merger/liquidation option — 강한 성공

**원문 주장**

fund consolidation이 structural discount를 줄인다.

**경제적 메커니즘**

larger fund는 expense ratio와 liquidity를 개선하고 NAV-equivalent exchange를 제공한다.

**T0 근거**

small fund와 overlapping mandate.

**숨은 가정**

shareholder approval·tax-free NAV exchange가 가능하다.

**사전 반증조건**

dilutive exchange·vote failure면 반증.

**실제 결과**

2018 AGC가 AVK에 NAV-equivalent로 합병됐다.

**정량 gap**

AGC NAV $6.36, ratio 0.36302760.

**분석 오류 또는 제한**

합병 후 AVK discount는 남는다.

**재사용 교훈**

terminal event 뒤 successor discount까지 추적한다.

### C6. leverage는 감당 가능 — 부분 성공

**원문 주장**

leverage가 income과 recovery를 증폭한다.

**경제적 메커니즘**

asset return이 funding cost를 넘으면 common NAV가 더 빨리 증가한다.

**T0 근거**

investments 약 174.5% of net assets.

**숨은 가정**

credit loss와 rates가 동시 악화하지 않는다.

**사전 반증조건**

asset coverage·funding cost 악화면 반증.

**실제 결과**

horizon 내 fund는 tender·merger까지 유지됐다.

**정량 gap**

distress 없음; expense 부담은 존재.

**분석 오류 또는 제한**

upside amplifier만 강조했다.

**재사용 교훈**

leverage는 asset coverage와 downside NAV beta로 stress한다.

---

## 4. 당시 Valuation과 Payoff Structure

CEF common은 headline yield가 아니라 `NAV × (1-discount)`에서 시작한다. NAV return, distribution composition과 할인율 변화를 분리하고, tender는 accepted shares에만 98% NAV를 적용한다. merger는 market price가 아니라 aggregate NAV-equivalent exchange이므로 discount가 자동으로 전부 현금화되는 것은 아니다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | credit loss·leverage drag·discount 20%+ | distribution 포함 손실 | FY2016 NAV 약세만 일부 |
| Base | NAV 보합·discount 10% | carry+10%p closure | FY2017말 약 8% |
| Bull | tender·NAV merger | NAV 근접 realization | 2017 tender·2018 merger |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| T0 discount | ~18.95% | ~10% | FY2017말 ~8% | 강한 성공 |
| Distribution | $0.047/month | carry | 지속·ROC 포함 | 혼합 성공 |
| FY2017 market/NAV | closure 기대 | market>NAV | +21.79%/+14.03% | +7.76%p |
| Tender | activist option | 실행 | 15% @98% NAV | 강한 성공 |
| Merger | liquidation option | NAV 보존 | AGC NAV $6.36; ratio .36302760 | 성공 |

### 촉매와 시간

판정 horizon은 **1~3년 discount closure와 distributions**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2016-01-17 | VIC Long | ~18.95% discount |
| 2016-10-31 | FY2016 종료 | market +6.68%/NAV -0.65% |
| 2017-08-09 | 15% tender 개시 | 할인 catalyst |
| 2017-09-07 | tender 만료 | 초과청약 |
| 2017-09-12 | final results | $6.4876·98% NAV |
| 2017-10-31 | FY2017 종료 | discount ~8% |
| 2018-05-29 | AVK merger proxy | expense/liquidity rationale |
| 2018-08-27 | merger 완료 | NAV-equivalent AVK shares |

### 실제 사업·자본구조 추이

FY2016 market return +6.68% 대 NAV -0.65%, FY2017 market +21.79% 대 NAV +14.03%로 discount closure가 추가 수익을 만들었다. 2017 tender는 AGC outstanding shares의 최대 15%를 98% NAV에 샀고 초과청약됐다. 2018-08-27 AGC holders는 AGC NAV $6.36당 AVK 0.36302760 shares를 받았다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

정확한 investor total-return ledger는 보유기간·재투자·tender 참여가 필요해 만들지 않는다. 다만 공식 fund return에서 FY2016·17 market return이 NAV return을 합계 약 15.1%p 상회했고, 할인은 약 18.95%에서 약 8%로 축소됐다. tender accepted portion은 98% NAV에 현금화됐다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 약 18.95% NAV discount | 20% | 강한 성공 | 약 11%p 축소. |
| C2 | NAV quality는 충분히 투명 | 18% | 성공 | NAV conversion까지 검증. |
| C3 | 11.4% distribution carry | 18% | 부분 성공 | headline yield 전부가 economic return은 아님. |
| C4 | 15% tender optionality | 16% | 강한 성공 | $6.4876·98% NAV. |
| C5 | merger/liquidation option | 16% | 강한 성공 | AGC NAV $6.36, ratio 0.36302760. |
| C6 | leverage는 감당 가능 | 12% | 부분 성공 | distress 없음; expense 부담은 존재. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

underlying credit만이 아니라 discount normalization이 수익의 핵심이었다. oversubscribed tender가 marginal liquidity를 제공했고 NAV-equivalent merger가 tiny-fund 구조비용을 줄였다. leverage와 ROC는 손실 가능성을 높였지만 catalyst가 먼저 작동했다.

### Counterfactual

NAV가 15% 하락하고 leverage cost가 올라가며 discount가 20%에 남아도 distribution과 tender probability를 합친 기대수익이 양수였는가?

---

## 9. 분석 오류 유형과 최초 경고

좋은 방향에도 headline 11.4% yield를 economic earning yield처럼 보일 위험이 있었다. tender 15%를 전 보유지분의 확정 exit로 간주하거나 leverage를 단순 upside amplifier로 보는 것도 오류다.

### 최초로 관찰 가능했던 경고신호

명확한 thesis break는 없었다. 사전 경고는 NAV 하락과 함께 distribution의 ROC 비중·leverage cost가 상승하고 discount가 20% 이상에 고착되는 조합이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

CEF는 headline yield보다 NAV quality·leverage·discount catalyst를 함께 산다.

### Lesson 2

distribution에서 income·gain·return of capital을 분리한다.

### Lesson 3

tender의 size·price·proration을 실제 payoff에 반영한다.

### Lesson 4

NAV-for-NAV merger와 market-price exit를 혼동하지 않는다.

### 지금 같은 아이디어를 다시 본다면

- NAV asset-level liquidity
- Level 1/2/3 mix
- distribution tax character
- leverage ratio·cost
- expense ratio
- activist standstill
- tender price·proration
- merger conversion ratio

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 성공 |
| Valuation thesis | 강한 성공 |
| Catalyst thesis | 강한 성공 |
| Security payoff | CEF common 적절 |
| Timing / path | 성공 |
| Thesis score | 9.2/10 |
| Process score | 8.8/10 |
| 종합 | **강한 성공 — 할인 축소·tender·NAV merger 실현** |

### 한 문장 교훈

> CEF는 headline yield보다 NAV quality·leverage·discount catalyst를 함께 산다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/ADVENT_CLAYMORE_CV_SECandIN_II/1392331342) — Value Investors Club / source SQL, 2016-01-17. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [AGC/AVK 2017 tender final results](https://www.sec.gov/Archives/edgar/data/1391461/000139146117000002/avkagctenderfinalresultspr.htm) — SEC / Guggenheim, 2017-09-12. AGC 15% tender, oversubscription, 33% proration과 $6.4876/98% NAV purchase price 검증.
3. [AGC/LCM-to-AVK merger proxy](https://www.sec.gov/Archives/edgar/data/1219120/000089180418000253/gug74131-497.htm) — SEC / Guggenheim, 2018-05-29. NAV-for-NAV merger 구조, expense-ratio savings와 shareholder vote 검증.
4. [AVK report and completed mergers](https://www.sec.gov/Archives/edgar/data/1219120/000089180419000224/gug76254-ncsr.htm) — SEC / Guggenheim, 2019. 2018-08-27 completion, AGC NAV $6.36과 AVK conversion ratio 0.36302760 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **B/C** — AGCO 2015·Alamos 2014는 source SQL price-only ratios, 그 외는 verified corporate action·official operating actual·제한적 market cross-check만 사용. complete dated ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Short**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
