# AFH Financial Group Plc (AFHP LN) — 2020-12-13 VIC Long

> **Idea unit:** 이 게시일·법인·증권 한 건만 분석한다. 같은 ticker의 다른 회사와 같은 회사의 다른 게시물은 별도 canonical 파일이다.
> **Research as-of:** 2026-09-18. raw metadata와 실제 원문 방향, 회사 identity, security payoff를 분리했다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | AFH Financial Group Plc / AFHP LN |
| VIC 게시일 / 작성자 | 2020-12-13 / Hvitserk |
| 분석 증권 / 실제 방향 | AFH Financial Group AIM-listed common equity / Long |
| 원 SQL 방향 | Long — raw 값 보존, research layer에서 원문 방향을 별도 검증 |
| 기준 진입가격 | 약 330p |
| 기대기간 | 2~5년 earnings; takeout는 6개월 내 |
| raw horizon audit | 약 10x P/E; cash-flow normalization; fair value 500~600p |
| 최종 판정 | **강한 성공 — 330p→480p cash scheme** |

> **결론:** 약 330p와 10x P/E에서 500~600p fair value를 제시한 뒤, 2021-01 recommended bid 463p가 나왔고 2021-03 480p로 상향됐다. scheme은 2021-06 effective가 됐다. 480/330-1=45.5% 단순 price gain이며 배당·세금·정확 settlement를 포함한 IRR은 아니다.

---

## 1. 회사는 정확히 무엇을 하는가

AFH Financial Group은 영국 independent financial adviser 네트워크와 wealth platform을 운영했다. adviser recruitment·acquisition, recurring fee assets와 integration 뒤 cash conversion이 가치의 핵심이며 2021년 private-equity buyer가 현금으로 인수했다.

advisers × client assets × recurring fee rate - adviser payout - platform·central cost - acquisition/integration cash = FCF; cash consideration이 terminal payoff다.

### 가치사슬과 security payoff

매출·생산·자산가치와 common equity 수익을 같은 것으로 취급하지 않는다. 영업 현금에서 운전자본·세금·유지 및 성장 capex·cash interest를 차감하고, debt·minority·희석과 corporate-action 조건을 적용한 뒤 common의 payoff를 계산한다.

### 매 분기 볼 핵심 KPI

advisers, assets under management, recurring revenue, fee margin, acquisition price, integration cost, operating cash conversion, EPS, bidder consideration

---

## 2. 당시 상황과 시장이 가격에 넣은 것

IFA roll-up의 acquisition accounting과 cash-flow timing 때문에 earnings quality가 과소평가됐고 약 10x P/E, 330p에서 recurring advice economics와 500~600p value를 살 수 있다는 thesis였다.

### Reverse expectations

시장은 adviser retention, acquisition integration, regulatory liabilities, contingent consideration과 accounting profit의 낮은 cash conversion을 할인했다.

---

## 3. 원문 투자논지 지도

### C1. ~10x P/E cheapness — 성공

**원문 주장**

quality IFA가 약 10x P/E로 싸다.

**경제적 메커니즘**

recurring fees와 cash normalization이 higher multiple을 지지.

**T0 근거**

T0 valuation.

**숨은 가정**

earnings·cash conversion 유지.

**사전 반증조건**

profit collapse면 반증.

**실제 결과**

buyer가 480p control value를 지급.

**정량 gap**

entry 대비 +45.5%.

**분석 오류 또는 제한**

bid price가 standalone multiple을 직접 증명하진 않음.

**재사용 교훈**

standalone과 control value를 분리한다.

### C2. cash-flow normalization — 간접 성공

**원문 주장**

accounting timing 뒤 cash가 드러난다.

**경제적 메커니즘**

integration·deferred consideration 소멸.

**T0 근거**

recurring client revenue.

**숨은 가정**

adviser/client retention.

**사전 반증조건**

cash conversion 악화면 실패.

**실제 결과**

6개월 내 buyer diligence를 통과.

**정량 gap**

독립 장기 ledger 전에 takeout.

**분석 오류 또는 제한**

buyer 결정을 operating proof로 과대해석.

**재사용 교훈**

transaction outcome은 간접 검증으로 표기한다.

### C3. 500~600p fair value — 근접·하단 미달

**원문 주장**

standalone value가 500~600p.

**경제적 메커니즘**

earnings normalization과 rerating.

**T0 근거**

explicit range.

**숨은 가정**

공개시장 또는 bidder가 value 인정.

**사전 반증조건**

cash bid <450p면 약화.

**실제 결과**

480p.

**정량 gap**

하단 -20p/-4%; 상단 -120p/-20%.

**분석 오류 또는 제한**

range가 control premium 포함 여부 모호.

**재사용 교훈**

standalone·control targets를 나눈다.

### C4. initial 463p bid — 강한 성공

**원문 주장**

external catalyst가 value를 닫을 수 있다.

**경제적 메커니즘**

buyer가 public discount를 현금화.

**T0 근거**

consolidation appeal.

**숨은 가정**

financing·board support.

**사전 반증조건**

deal 없음이면 option 0.

**실제 결과**

463p recommended offer.

**정량 gap**

entry 대비 +40.3%.

**분석 오류 또는 제한**

takeout을 base에 넣을 위험.

**재사용 교훈**

probability-weighted option으로 둔다.

### C5. 480p increased offer — 강한 성공

**원문 주장**

competitive/process pressure가 consideration을 높인다.

**경제적 메커니즘**

shareholder support 확보.

**T0 근거**

initial bid와 company value.

**숨은 가정**

bidder가 terms 개선.

**사전 반증조건**

463p 고정이면 추가 upside 없음.

**실제 결과**

480p로 17p 상향.

**정량 gap**

+3.7% vs initial.

**분석 오류 또는 제한**

작은 상향을 운영 alpha로 오인.

**재사용 교훈**

event return을 별도 ledger로 둔다.

### C6. scheme completion — 강한 성공

**원문 주장**

cash offer가 실제 종결된다.

**경제적 메커니즘**

vote·court·effective date 통과.

**T0 근거**

recommended scheme.

**숨은 가정**

conditions 충족.

**사전 반증조건**

vote/court failure면 반증.

**실제 결과**

2021-06 effective.

**정량 gap**

terminal cash payoff.

**분석 오류 또는 제한**

announcement price를 realized로 조기 간주.

**재사용 교훈**

effective date까지 completion risk를 추적한다.

---

## 4. 당시 Valuation과 Payoff Structure

500~600p는 entry 대비 51.5~81.8% upside였다. standalone earnings normalization이 base이고 takeout은 별도 option이어야 했다. 실제 480p bid는 원 target 하단보다 4% 낮지만 매우 짧은 시간에 현금화됐다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear | bid 없음·cash conversion 약화 | 10x earnings 정체 | 미발생 |
| Base | standalone normalization | 500p 부근 | takeout로 선반영 |
| Event | recommended cash bid | 480p cash | 실현 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry | 330p | 500~600p | 480p cash | +45.5% 단순 |
| P/E | 약 10x | rerating | control bid | 성공 |
| Initial bid | 없음 | optional | 463p | +40.3% vs entry |
| Revised bid | 463p | 상향 | 480p | +3.7% vs initial |
| Target gap | 500~600p | 하단 500p | 480p | 하단 -4.0% |

### 촉매와 시간

판정 horizon은 **2~5년 earnings; takeout는 6개월 내**다. 이후 corporate action은 terminal value 검증에는 쓰되 원 horizon의 실현수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2020-12-13 | VIC Long | 약 330p |
| 2021-01-25 | 463p recommended bid | catalyst |
| 2021-03-02 | bid 480p로 상향 | value 개선 |
| 2021-04 | scheme documents | 조건 구체화 |
| 2021-05 | shareholder process | event risk 감소 |
| 2021-06 | court sanction | 마지막 조건 |
| 2021-06 | scheme effective | cash payoff |
| 후속 | listing 종료 | terminal event |

### 실제 사업·자본구조 추이

Cortina Bidco/Flexpoint Ford는 2021-01 463p recommended cash offer를 제시했고 2021-03 consideration을 480p로 높였다. court sanction 뒤 2021-06 scheme이 effective가 되어 common은 cash consideration으로 종결됐다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

480p/330p-1=45.5% 단순 gain이다. 약 6개월의 정확 purchase/settlement date, dividends와 tax가 없으므로 exact annualized IRR은 계산하지 않는다.

가격 series가 wrong entity이거나 corporate action·배당·통화가 완전히 복원되지 않으면 exact IRR·MFE·MAE를 만들지 않는다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | ~10x P/E cheapness | 20% | 성공 | entry 대비 +45.5%. |
| C2 | cash-flow normalization | 18% | 간접 성공 | 독립 장기 ledger 전에 takeout. |
| C3 | 500~600p fair value | 18% | 근접·하단 미달 | 하단 -20p/-4%; 상단 -120p/-20%. |
| C4 | initial 463p bid | 16% | 강한 성공 | entry 대비 +40.3%. |
| C5 | 480p increased offer | 16% | 강한 성공 | +3.7% vs initial. |
| C6 | scheme completion | 12% | 강한 성공 | terminal cash payoff. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

standalone recurring-fee franchise와 낮은 public valuation이 financial buyer의 integration·private ownership synergies와 결합해 빠른 cash catalyst를 만들었다.

### Counterfactual

bid가 없고 EPS가 10%만 성장하며 10x multiple이 유지돼도 330p에서 downside-adjusted return이 만족스러웠는가?

---

## 9. 분석 오류 유형과 최초 경고

결과는 좋았지만 bidder premium을 T0 earnings thesis의 정확한 적중으로 전부 돌리면 안 된다. standalone value와 control value를 분리해야 한다.

### 최초로 관찰 가능했던 경고신호

bid가 나온 뒤 핵심 risk는 운영이 아니라 scheme vote·court·financing 조건이었다. 480p 상향과 sanction으로 break risk가 줄었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

외부 cash bid는 intrinsic value의 강한 검증이지만 원 target와 consideration을 구분한다.

### Lesson 2

bid 발표 전 standalone downside가 견딜 수 있어야 한다.

### Lesson 3

가격수익과 배당·세금 포함 total return을 혼동하지 않는다.

### Lesson 4

scheme calendar와 break conditions를 추적한다.

### 지금 같은 아이디어를 다시 본다면

- advisers/AUM
- recurring fee mix
- integration cost
- cash conversion
- offer conditions
- scheme vote
- cash settlement

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | buyer가 franchise 확인 |
| Valuation thesis | target 하단 근접 |
| Catalyst thesis | cash bid 성공 |
| Security payoff | common 적절 |
| Timing / path | 6개월 내 성공 |
| Thesis score | 9.0/10 |
| Process score | 8.5/10 |
| 종합 | **강한 성공 — 330p→480p cash scheme** |

### 한 문장 교훈

> 외부 cash bid는 intrinsic value의 강한 검증이지만 원 target와 consideration을 구분한다.

---

## 12. Sources / Validation Notes

1. [VIC original idea](https://www.valueinvestorsclub.com/idea/AFH_Financial_Group/6482598516) — Value Investors Club / source SQL, 2020-12-13. T0 원문·작성자·증권·방향·valuation·catalyst 수치의 기준. 공개 URL이 없으면 uploaded SQL 본문을 사용했다.
2. [Increased recommended cash offer](https://shareprices.com/rns/increased-recommended-cash-offer-ddqvemypxlitszi/) — AFH / RNS mirror, 2021-03-02. 현금 offer가 463p에서 480p로 상향된 조건 검증.
3. [Court sanction and scheme timetable](https://www.lse.co.uk/rns/court-sanction-of-scheme-expected-scheme-timetable-z5daxunvun7f22r.html) — AFH / RNS mirror, 2021-06. court sanction과 scheme effective timetable 검증.

### 데이터 품질

- T0 원문·metadata: **A/B — source SQL 원문과 공개 VIC URL. 공개 URL이 없는 글은 source DB 본문 기준.**
- 사업·거래·자본구조: **A** — SEC·회사 1차자료 우선.
- 가격·수익률: **C/제한** — source SQL performance row가 없어 verified cash consideration·reported operating data·bankruptcy waterfall만 사용; complete ledger 없이는 total return·IRR을 만들지 않음.
- raw SQL direction은 **Long**, 실제 원문 방향은 **Long**다. raw 값은 덮어쓰지 않았다.
