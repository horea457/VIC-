# Emmis Communications (EMMS) — 2010-07-19 VIC Short

> **Idea unit:** 이 게시일의 증권 한 건만 분석한다. 같은 ticker의 다른 VIC 게시물은 별도 파일이다.
> **Research as-of:** 2026-09-09. 사업·valuation·촉매·증권·가격경로를 분리해 판정한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Emmis Communications / EMMS |
| VIC 게시일 / 작성자 | 2010-07-19 / pfq783 |
| Security / 실제 방향 | EMMS Class A common equity / Short |
| 원 SQL 방향 | Short — raw 값 보존; 본문 research direction은 별도 교정 |
| 기준 진입가격 | $2.15 |
| 기대기간 | 2010-09-24 drop-dead까지 약 2개월 |
| raw horizon audit | DB parser 3년은 note maturity 문구 오인 가능성이 높아 판정 제외 |
| 최종 판정 | **강한 이벤트 성공·exact trade return 미검증** |

> **결론:** $2.40 take-private는 common tender와 preferred amendment/exchange가 연결돼 있었고 required preferred vote를 얻지 못하면 닫힐 수 없었다. 2010-09-09 회사는 proposed amendments가 requisite vote를 얻지 못했고 exchange와 tender가 종료됐다고 밝혔다. 9월 29일 merger도 공식 종료됐다. $2.15 Short의 핵심 catalyst는 정확히 실현됐지만 break-day 가격과 borrow를 복원하지 않아 exact profit은 만들지 않는다.

---

## 1. 회사는 정확히 무엇을 하는가

Emmis Communications는 New York·Los Angeles·Indianapolis 등 주요 시장의 radio station, 과거 TV·publishing, digital·emerging technology 자산을 보유했던 지배주주형 소형 미디어 회사다. Station 가치는 주파수 license, 지역 브랜드, audience, 광고관계를 묶은 현금흐름과 전략적 희소성에서 나오지만, minority common은 자산 자체가 아니라 debt·preferred·tax·transaction cost·지배주주의 처분 결정을 모두 지난 뒤의 residual claim이다.

경제 엔진은 `station-level BCF + publishing/events/other - corporate overhead - cash interest - capex - tax`이고, asset play의 common value는 `매각가능가치 × 실현확률 × 세후·시간할인 - debt - preferred/legal claims`다. 자산을 제값에 팔아도 새 인수에 재투자하거나 현금화가 수년 늦으면 nominal NAV와 주주 IRR은 크게 달라진다.

### 가치사슬과 common equity 청구권

광고주가 지불하는 gross revenue가 곧 주주현금은 아니다. Audience와 advertiser demand에서 station·platform 운영비, talent·sales 비용, corporate overhead, cash interest, capex, tax가 차례로 빠진다. Asset sale 아이디어는 여기에 preferred·transaction cost·control decision까지 통과해야 한다. 이 보고서는 매출 증가, EBITDA 증가, common value 증가를 같은 사건으로 취급하지 않는다.

### 매 분기 볼 핵심 KPI

station BCF, corporate overhead, cash interest, 순부채·preferred 청구액, covenant, 자산별 after-tax sale value, 매각대금 사용처, 완전희석 주식수, 지배주주와 minority holder의 경제적 일치

---

## 2. 당시 상황과 시장이 가격에 넣은 것

Capital structure는 약 $345m secured credit와 $141m preferred liquidation preference(2.81m주×$50)로 복잡했다. JS Acquisition은 common을 $2.40에 tender하는 동시에 6.25% cumulative preferred를 12% PIK subordinated notes로 교환하고 preferred terms를 고치려 했다. 원문은 반대 bloc 때문에 약 2/3 consent가 어렵고, $2.15에서 close 손실은 약 11.6%인 반면 break gain은 25~50%라고 봤다.

### Reverse expectations

시장 spread는 closing probability를 높게 봤다. 그러나 payoff는 운영가치보다 계약 dependency에 달렸다. 조건변경 없이 2/3 vote를 얻을 확률, blocker가 이탈할 확률, buyer가 terms를 sweeten할 확률을 합쳐도 market implied close probability보다 낮다면 Short가 성립한다. 핵심은 opinion이 아니라 cap-table math였다.

---

## 3. 원문 투자논지 지도

### C1. preferred 2/3 consent가 필수다 — 성공

**원문 주장**

common tender는 preferred amendment 통과에 종속된다.

**경제적 메커니즘**

연결조건 하나의 실패가 전체 transaction을 막는다.

**T0 근거**

offer·merger 조건과 preferred cap table.

**숨은 가정**

waiver 없이 requisite vote가 유지된다.

**사전 반증조건**

buyer가 condition을 포기하거나 threshold를 확보하면 반증.

**실제 결과**

requisite vote 미달로 amendment·exchange·tender 종료.

**정량 gap**

직접 적중.

**분석 오류 또는 제한**

중대한 오류 없음.

**재사용 교훈**

모든 closing condition의 dependency graph를 만든다.

### C2. 반대 bloc이 거래를 막는다 — 성공

**원문 주장**

경제적으로 불리한 exchange에 preferred holders가 반대한다.

**경제적 메커니즘**

$50 liquidation·arrears를 낮은 조건의 PIK notes로 바꾸는 손실이 vote를 막는다.

**T0 근거**

preferred economics와 ownership.

**숨은 가정**

blocker가 충분히 결집한다.

**사전 반증조건**

lock-up 이탈·sweetener로 2/3 확보 시 반증.

**실제 결과**

vote가 실제 통과하지 못했다.

**정량 gap**

blocking thesis 확인.

**분석 오류 또는 제한**

exact holder votes는 별도 미복원.

**재사용 교훈**

blocker는 법적 권리와 경제적 유인을 함께 본다.

### C3. close downside는 약 11.6%다 — 성공

**원문 주장**

$2.15 Short가 $2.40 close 시 제한손실이다.

**경제적 메커니즘**

fixed deal price가 adverse payoff를 cap한다.

**T0 근거**

명시 offer price.

**숨은 가정**

price increase·borrow squeeze가 없다.

**사전 반증조건**

deal sweetening 또는 borrow cost 급등이면 cap 무효.

**실제 결과**

deal이 종료돼 close loss는 발생하지 않았다.

**정량 gap**

구조적 downside 미발생.

**분석 오류 또는 제한**

borrow와 sweetener tail은 남음.

**재사용 교훈**

deal cap은 financing·borrow tail을 포함한다.

### C4. break upside는 25~50%다 — 미검증

**원문 주장**

거래 무산 시 pre-deal value로 하락한다.

**경제적 메커니즘**

deal premium 제거와 weak capital structure가 가격을 낮춘다.

**T0 근거**

원문 downside appraisal.

**숨은 가정**

standalone value와 market liquidity가 유지된다.

**사전 반증조건**

break 후 가격이 $1.61 위에 머물면 low case 미달.

**실제 결과**

break-day price를 복원하지 못했다.

**정량 gap**

event 방향만 확인.

**분석 오류 또는 제한**

expected와 actual return 혼동 금지.

**재사용 교훈**

break price는 별도 시장데이터로 검증한다.

### C5. 9월 drop-dead가 빠른 촉매다 — 성공

**원문 주장**

vote failure 뒤 거래가 9월 말 종료된다.

**경제적 메커니즘**

짧은 calendar가 carry를 제한한다.

**T0 근거**

8월 meeting·9월 24일 date.

**숨은 가정**

연장·소송이 없다.

**사전 반증조건**

deal 연장 시 IRR 하락.

**실제 결과**

9월 29일 merger termination.

**정량 gap**

약 10주 내 실현.

**분석 오류 또는 제한**

며칠의 procedural lag만 존재.

**재사용 교훈**

event IRR은 legal milestones로 계산한다.

### C6. 운영사업 전망은 secondary다 — 성공

**원문 주장**

Short 성공은 radio EBITDA가 아니라 closing failure에 달렸다.

**경제적 메커니즘**

contractual binary가 market beta를 압도한다.

**T0 근거**

구조화된 tender/exchange.

**숨은 가정**

event window 안에 business shock가 payoff를 바꾸지 않는다.

**사전 반증조건**

재무개선으로 standalone price가 급등하면 반증.

**실제 결과**

거래조건 실패가 결과를 결정했다.

**정량 gap**

driver attribution 적중.

**분석 오류 또는 제한**

중대한 오류 없음.

**재사용 교훈**

event trade는 핵심 risk factor만 남긴다.

---

## 4. 당시 Valuation과 Payoff Structure

Close loss는 ($2.40-$2.15)/$2.15 ≈ 11.6%다. Break gain 25~50%라면 break price는 약 $1.61~$1.08에 해당한다. Borrow와 시간가치를 빼기 전 기대값은 `P(break)×break gain - P(close)×11.6%`다. 25% gain 기준 손익분기 break probability는 약 31.7%, 50% 기준 약 18.8%다. 계약상 blocker가 이 확률보다 강하면 비대칭이다.

### 시나리오 분석

| 시나리오 | 핵심 가정 | 기대 payoff | 실제 대조 |
|---|---|---|---|
| Bear for Short | 2/3 consent·terms sweetening | 약 -11.6% before carry | 발생하지 않음 |
| Base | vote fail·tender 종료 | +25% 가정 | event 실현·가격 미복원 |
| Bull for Short | 급한 deal break | +50% 가정 | 가격 미복원 |

### 핵심 수치

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Short entry | $2.15 | break downside | exact cover 미복원 | event 성공 |
| Deal price | $2.40 | close loss | 약 11.6% | 정의됨 |
| Preferred threshold | 약 66.7% | 미달 | requisite vote 미달 | 성공 |
| Break-even probability | 31.7% / 18.8% | 25% / 50% gain case | deal break | 비대칭 |
| Drop-dead | 2010-09-24 | 빠른 종료 | 9월 29일 종료 | 성공 |

### 촉매와 시간

원문 기대기간은 **2010-09-24 drop-dead까지 약 2개월**다. 판정에서는 이 기간을 고정한다. 그 뒤의 corporate event는 장기 사업가설 검증에는 쓰되 원 horizon 수익률을 대체하지 않는다.

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2010-05-25 | Going-private agreement | $2.40 tender |
| 2010-07-19 | VIC Short | $2.15 |
| 2010-08 | preferred vote process | 핵심 condition |
| 2010-09-09 | vote 미달 | offer 종료 |
| 2010-09-24 | drop-dead | termination right |
| 2010-09-29 | merger 종료 | thesis 실현 |

### 실제 사업·자본구조 추이

2010-09-09 proposed preferred amendments가 required vote를 얻지 못했고, 그 조건에 묶인 exchange offer와 common tender도 종료됐다. 9월 24일 drop-dead date가 지났고 9월 29일 JS Parent가 merger agreement를 종료했다. Holders는 기존 Emmis shareholders로 남았다. 운영사업의 장기 결과와 무관하게 원 이벤트 thesis는 이 시점에 판정 가능했다.

---

## 6. 실제 투자결과 — 가격 경로와 실현 가능성

$2.15 entry와 $2.40 close cap은 복원됐지만 종료 직후 주가·borrow fee·실제 cover date는 없다. 따라서 원문이 말한 25~50% gain을 actual return으로 쓰지 않는다. 확정 가능한 것은 close condition 실패와 merger termination이다.

가격 데이터는 배당·세금·거래비용을 포함한 total return과 분리한다. 원 DB에 event-date series가 없으면 수익률·MFE·MAE를 추정해 채우지 않는다. Short는 borrow와 cover rule, event trade는 계약상 payout과 duration이 있어야 exact IRR을 계산한다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | preferred 2/3 consent가 필수다 | 20% | 성공 | 직접 적중. |
| C2 | 반대 bloc이 거래를 막는다 | 18% | 성공 | blocking thesis 확인. |
| C3 | close downside는 약 11.6%다 | 18% | 성공 | 구조적 downside 미발생. |
| C4 | break upside는 25~50%다 | 16% | 미검증 | event 방향만 확인. |
| C5 | 9월 drop-dead가 빠른 촉매다 | 16% | 성공 | 약 10주 내 실현. |
| C6 | 운영사업 전망은 secondary다 | 12% | 성공 | driver attribution 적중. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

수익기회는 radio 가치평가가 아니라 common tender가 preferred vote에 종속된 계약구조에서 나왔다. 제한된 close loss와 더 큰 break payoff, 두 달 남짓한 event calendar가 결합된 점이 좋았다.

### Counterfactual

Buyer가 preferred에 얼마를 더 제공하면 blocker가 2/3 threshold를 넘기고 Short 기대값이 음수가 되는가?

---

## 9. 분석 오류 유형과 최초 경고

성과판정에서 25~50% 기대 gain을 actual gain으로 바꾸면 안 된다. 3년 raw horizon도 event calendar와 모순되므로 제외했다.

### 최초로 관찰 가능했던 경고신호

반증은 preferred holders의 2/3 지지 또는 terms sweetening이다. 실제로는 2010-09-09 vote failure가 catalyst를 확정했다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

### Lesson 1

Merger-break Short는 valuation opinion보다 closing threshold와 blocking stake를 먼저 본다.

### Lesson 2

close loss·break gain·확률 손익분기점을 같은 표에 둔다.

### Lesson 3

원문 horizon parser보다 계약상 drop-dead date를 우선한다.

### 지금 같은 아이디어를 다시 본다면

- 필요 vote threshold
- blocker ownership
- 조건간 dependency
- sweetener capacity
- close loss
- break price
- borrow·drop-dead date

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 해당 없음 |
| Valuation thesis | 비대칭 성공 |
| Catalyst thesis | 강한 성공 |
| Timing / path | event 적중 |
| Security selection | common Short 적절 |
| Thesis score | 9.0/10 |
| Process score | 9.0/10 |
| 종합 | **강한 이벤트 성공·exact trade return 미검증** |

### 한 문장 교훈

> Merger-break Short는 valuation opinion보다 closing threshold와 blocking stake를 먼저 본다.

---

## 12. Sources / Validation Notes

1. VIC original text retained in source SQL — Value Investors Club / source SQL, 2010-07-19. 공개 URL이 저장되지 않은 원문 description·catalyst 복원.
2. [Emmis 2011 Form 10-K](https://www.sec.gov/Archives/edgar/data/783005/000095012311047715/c16797e10vk.htm) — SEC / Emmis, 2011-05-10. $2.40 tender, preferred amendment 실패, 거래 종료 검증.
3. [Emmis merger termination Form 8-K](https://www.sec.gov/Archives/edgar/data/783005/000095014210001475/form8k_092710.htm) — SEC / Emmis, 2010-09-29. 9월 24일 drop-dead 이후 merger termination 검증.
4. [Emmis 2016 Form 10-K](https://www.sec.gov/Archives/edgar/data/783005/000078300516000072/emms10k-2016.htm) — SEC / Emmis, 2016-05. preferred litigation의 2015 affirmation·settlement 검증.

### 데이터 품질

- 원문 방향·작성자·기간·excerpt: **A/B** — 원 source DB와 공개 VIC URL을 대조했다. 공개 URL이 없는 3건은 저장된 SQL 원문을 사용했다.
- 사업·거래·법원·자본구조: **A** — SEC와 회사 1차자료를 우선했다.
- 가격경로: **C 또는 미검증** — 원 DB에 있는 TSQ 단기 ratio와 원문에 명시된 가격만 사용했다. 그 밖의 exact total return·MFE·MAE는 만들지 않았다.
- 원 SQL `is_short=true`는 모든 아이디어에서 감사추적용으로 보존했다. 실제 Long/Short와 multi-leg hedge는 research layer에서 별도로 기록했다.
