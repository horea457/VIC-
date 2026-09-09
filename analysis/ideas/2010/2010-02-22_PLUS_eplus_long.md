# ePlus inc. (PLUS) — 2010-02-22 VIC Long

> **Idea unit:** 2010-02-22 게시물 한 건만 분석한다. 같은 ticker의 다른 entity·다른 시점과 섞지 않는다.
> **Research as-of:** 2026-09-09. SQL raw direction과 원문상 실제 direction, 사업결과와 투자수익을 분리한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | ePlus inc. / PLUS |
| Idea ID | `1f6793f5-26f0-44b5-bcd6-7a2c70ffe1f1` |
| 게시일 / 작성자 | 2010-02-22 / paddy788 |
| 원 SQL 방향 | Short |
| 원문 검증 방향 | **Long** |
| 기준가격/valuation anchor | $16 |
| 원 horizon | 수년 |
| 최종 판정 | **방향교정·회계해석·장기 사업논지 성공, 원 horizon 가격성과 미검증** |

> **결론:** SQL은 Short지만 원문 첫 문장이 ePlus 매수를 권한다. $16 가격, cash $9.59/share, TBV $19.51, FY10 EPS 약 $2와 수년 내 $3 EPS/$30+를 제시했다. 핵심 edge는 database가 lease-backed non-recourse notes를 corporate debt로 잡아 EV를 $59m 과대계상한다는 회계 교정이다. 결과적으로 **방향교정·회계해석·장기 사업논지 성공, 원 horizon 가격성과 미검증**.

---

## 1. 회사는 정확히 무엇을 하는가

ePlus는 기업·공공기관의 서버·네트워크·보안·클라우드 장비를 설계·조달·구축하는 VAR/IT services와 장비 금융·리스를 결합한다. 현금엔진은 `product gross profit + service gross profit + lease spread·residual recovery - 인력·판관비 - 운전자본 - 세금·capex`다. 따라서 총매출보다 gross profit dollars, service mix, 매출채권·재고 회전, lease credit와 recourse/non-recourse debt 구분이 중요하다.

### Common equity까지의 현금 waterfall

보고 EBITDA에서 restructuring·integration, maintenance/growth capex, 운전자본, pension/legacy cash, interest·tax를 차감한 뒤의 FCF가 주주가치다. 배수 비교 전에 회계상 debt의 recourse, 고객·지역 mix, 자본집약도와 희석을 같은 기준으로 맞춘다.

### 매 분기 확인할 KPI

- Organic/local-currency growth와 price·volume·mix
- Gross/segment margin과 route·customer unit economics
- EBITDA→CFO→FCF conversion
- Net debt, pension·legacy·regulatory cash claims
- Share count, dividend·buyback과 acquisition ROIC

---

## 2. 당시 상황과 시장이 가격에 넣은 것

SQL은 Short지만 원문 첫 문장이 ePlus 매수를 권한다. $16 가격, cash $9.59/share, TBV $19.51, FY10 EPS 약 $2와 수년 내 $3 EPS/$30+를 제시했다. 핵심 edge는 database가 lease-backed non-recourse notes를 corporate debt로 잡아 EV를 $59m 과대계상한다는 회계 교정이다.

### Reverse expectations

시장은 $16에 원문이 기회로 본 요소의 실패·지연 가능성을 상당 부분 반영했다. 핵심은 좋은 회사/나쁜 회사라는 서술이 아니라 원문 기대와 가격에 내재된 기대 중 어느 쪽이 실제 KPI에 가까웠는지다.

---

## 3. 원문 투자논지 지도

### C1. raw Short가 아니라 Long — 교정 성공

**원문 주장**

I am recommending the purchase라고 명시했다.

**경제적 메커니즘**

I am recommending the purchase라고 명시했다.라는 기대가 $16→$30+ payoff를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다.

**T0 근거**

$16→$30+ payoff

**숨은 가정**

ticker가 미국 ePlus다.

**사전 반증조건**

원문이 하락 payoff를 목표로 하면 반증.

**실제 결과**

본문·valuation·촉매가 모두 Long이다.

**판정과 재사용 교훈**

**교정 성공** — direction은 flag보다 action verb·payoff로 확정한다.

### C2. non-recourse debt가 EV를 $59m 과대계상 — 강한 성공

**원문 주장**

lease notes를 corporate funded debt처럼 보면 안 된다.

**경제적 메커니즘**

lease notes를 corporate funded debt처럼 보면 안 된다.라는 기대가 $168m reported vs $109m adjusted EV를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다.

**T0 근거**

$168m reported vs $109m adjusted EV

**숨은 가정**

채권자가 corporate asset에 청구할 수 없다.

**사전 반증조건**

representation/fraud recourse가 material하면 반증.

**실제 결과**

법적·경제적 분류는 타당했다.

**판정과 재사용 교훈**

**강한 성공** — EV debt는 recourse와 matched asset을 함께 감사한다.

### C3. cash 감소는 burn이 아니라 lease 투자 — 성공

**원문 주장**

$25m cash 감소는 lease book 확대로 설명된다.

**경제적 메커니즘**

$25m cash 감소는 lease book 확대로 설명된다.라는 기대가 net lease investment $34.3m→$66.2m를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다.

**T0 근거**

net lease investment $34.3m→$66.2m

**숨은 가정**

credit quality·spread·residual 회수가 양호하다.

**사전 반증조건**

loss rate·residual shortfall이 spread를 소진하면 반증.

**실제 결과**

financing은 수익엔진으로 존속했다.

**판정과 재사용 교훈**

**성공** — cash-flow 변동을 asset build와 operating loss로 분리한다.

### C4. VAR 회복으로 FY10 EPS 약 $2 — 장기 성공

**원문 주장**

Q4 $0.50로 연간 약 $2를 예상한다.

**경제적 메커니즘**

Q4 $0.50로 연간 약 $2를 예상한다.라는 기대가 $20m open orders·$10m deferred revenue를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다.

**T0 근거**

$20m open orders·$10m deferred revenue

**숨은 가정**

backlog가 gross profit과 cash로 전환된다.

**사전 반증조건**

orders 취소·margin compression이면 반증.

**실제 결과**

장기 technology earnings는 크게 성장했다.

**판정과 재사용 교훈**

**장기 성공** — 매출가시성을 gross margin과 conversion까지 연결한다.

### C5. $19.51 TBV가 liquidation support — 성공

**원문 주장**

price $16은 cash·WC·lease 중심 TBV 아래다.

**경제적 메커니즘**

price $16은 cash·WC·lease 중심 TBV 아래다.라는 기대가 cash $9.59/share·TBV $19.51를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다.

**T0 근거**

cash $9.59/share·TBV $19.51

**숨은 가정**

asset haircut과 corporate cost가 제한적이다.

**사전 반증조건**

claim-adjusted TBV가 price 아래면 반증.

**실제 결과**

기업은 장기 equity를 키웠다.

**판정과 재사용 교훈**

**성공** — TBV를 asset별 recovery rate로 재작성한다.

### C6. insider 50%가 capital return — 부분 성공

**원문 주장**

좋은 용처가 없으면 buyback/특별배당한다.

**경제적 메커니즘**

좋은 용처가 없으면 buyback/특별배당한다.라는 기대가 CEO 26%·insiders 50%+를 통해 earnings·FCF 또는 valuation gap으로 전환되는 구조다.

**T0 근거**

CEO 26%·insiders 50%+

**숨은 가정**

지배주주와 minority의 유동성·세금 선호가 같다.

**사전 반증조건**

현금유보·저수익 deal이면 반증.

**실제 결과**

장기 buyback은 있었으나 원 horizon payout은 미검증이다.

**판정과 재사용 교훈**

**부분 성공** — ownership은 actual allocation record로 검증한다.

---

## 4. 당시 Valuation과 Payoff Structure

표면 EV는 equity $129m+debt $121m-cash $82m=$168m이지만 non-recourse notes $59m을 제외한 economic EV는 $109m이다. $16에서 cash 제외 P/E는 약 3.2x, TBV 대비 0.82x다. Direct-finance lease $107.6m의 약 60%인 $64.6m이 non-recourse였고, net economic lease investment는 2009-03 $34.3m에서 2009-12 $66.2m으로 늘어 cash 약 $25m 감소를 설명했다.

### 시나리오 구조

| 시나리오 | 조건 | payoff 해석 |
|---|---|---|
| Bear | 핵심 falsifier가 조기에 발생 | Long의 손실·duration 확대 |
| Base | 핵심 KPI가 원문 bridge의 절반 이상 달성 | valuation gap 일부 축소 |
| Bull | earnings/FCF 개선과 multiple·capital return 동시 실현 | 방향교정·회계해석·장기 사업논지 성공, 원 horizon 가격성과 미검증와 비교할 상단 |

### 핵심 수치 감사

| 지표 | T0 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Entry/cash | $16 / $9.59 | downside 지지 | 정확한 return 없음 | 미검증 |
| TBV/share | $19.51 | liquidation 이하 | 장기 equity 성장 | 성공 |
| reported/adjusted EV | $168m / $109m | debt 오류 해소 | 구조해석 유효 | 성공 |
| FY10 EPS | 약 $2 | 수년 내 $3 | 장기 earning power 확대 | 장기 성공 |
| Target | $30+ | 수년 | 달성일/IRR 미복원 | 미검증 |

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2009-03 | net lease investment $34.3m | cash 사용 시작 |
| 2009-12 | net lease investment $66.2m | $25m cash decline 설명 |
| 2010-02-22 | VIC Long | raw Short 교정 |
| 2010-03 | FY10 close | 약 $2 EPS 기대 |
| 2010s | VAR/services scale | 장기 thesis 확인 |
| 2025 | financing 사업 재편 | 원 cash engine 변화 |

### 실제 사업·자본구조

Company는 VAR와 financing을 계속 확장해 장기 earnings·book value를 크게 키웠다. 원문의 debt taxonomy와 cash-flow 해석은 높은 재사용 가치가 있다. 그러나 SQL에 performance가 없어 $16→$30+의 실제 달성일·IRR을 이 데이터만으로 확정하지 않는다.

---

## 6. 실제 투자결과 — 방향 교정과 가격 경로

performance row가 없다. 따라서 장기 기업성공을 투자수익으로 대체하지 않고 1/3/5년 corrected return을 null로 유지한다.

성과값은 SQL의 multiplier를 사용했다. Long은 `multiplier-1`, Short는 `1-multiplier`로 부호를 교정했다. Short 수익률은 borrow fee·배당·margin call·position resizing을 제외한 단순치이므로 실제 운용수익과 다를 수 있다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | Weight | 판정 | 재사용 교훈 |
|---|---|---:|---|---|
| C1 | raw Short가 아니라 Long | 20% | 교정 성공 | direction은 flag보다 action verb·payoff로 확정한다. |
| C2 | non-recourse debt가 EV를 $59m 과대계상 | 18% | 강한 성공 | EV debt는 recourse와 matched asset을 함께 감사한다. |
| C3 | cash 감소는 burn이 아니라 lease 투자 | 18% | 성공 | cash-flow 변동을 asset build와 operating loss로 분리한다. |
| C4 | VAR 회복으로 FY10 EPS 약 $2 | 16% | 장기 성공 | 매출가시성을 gross margin과 conversion까지 연결한다. |
| C5 | $19.51 TBV가 liquidation support | 16% | 성공 | TBV를 asset별 recovery rate로 재작성한다. |
| C6 | insider 50%가 capital return | 12% | 부분 성공 | ownership은 actual allocation record로 검증한다. |

가중치는 100%이며, 방향·사업·valuation·catalyst·timing을 한 점수로 뭉개지 않고 별도로 판정했다.

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

headline EV 오류가 해소되고 lease investment가 earnings로 회수되며 VAR gross profit이 회복되는 것이 driver였다. 반면 현금은 전부 excess가 아니라 lease·working-capital에 재투자되는 운영자산이었다.

### Counterfactual

원문 방향을 반대로 두었을 때가 아니라, 핵심 catalyst를 제거하고도 $16에서 충분한 expected return이 남았는지를 묻는다. 남지 않으면 cheapness보다 event timing에 의존한 아이디어였다.

---

## 9. 분석 오류 유형과 최초 경고

좋은 회계 교정 뒤에도 $3 EPS의 시간표와 buyback/특별배당을 base case로 묶었고, insider concentration이 minority-friendly payout을 보장한다고 보았다.

### 최초 관찰 가능한 경고/반증

lease credit loss·residual recovery와 gross profit/CFO가 악화되거나, 현금이 낮은 ROIC lease growth에 계속 묶이면 반증이었다.

---

## 10. 재사용 가능한 교훈과 다음 분석 체크리스트

1. **Entity·direction audit:** raw Short와 실제 Long을 원문 action/payoff로 확정한다.
2. **Expectation bridge:** valuation 배수와 정상 margin을 수량·가격·원가·현금으로 연결한다.
3. **Catalyst clock:** event 성공 여부와 target price/IRR 성공을 분리한다.
4. **Security waterfall:** debt·pension·규제자본·분리비용을 common 앞에서 차감한다.
5. **Path risk:** 1/2/3/5년 결과가 다르면 사후에 가장 좋은 시점만 고르지 않는다.

### 다시 분석한다면

- 원문 수치와 공시 actual을 같은 통화·회계기준으로 맞춘다.
- 각 claim마다 분기 KPI, 날짜와 exit/cover rule을 둔다.
- 매출 성장과 FCF/share 증가를 분리한다.
- M&A·buyback은 발표가 아니라 실제 ROIC·net share count로 검증한다.

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Direction / entity | raw Short → research Long |
| Business thesis | 강한 성공 |
| Valuation thesis | 미검증 |
| Catalyst / timing | 방향교정·회계해석·장기 사업논지 성공, 원 horizon 가격성과 미검증 |
| Thesis score | 8.5/10 |
| Process score | 9.0/10 |
| Outcome-adjusted score | 8.5/10 |

### 한 문장 교훈

> direction은 flag보다 action verb·payoff로 확정한다.

---

## 12. Sources / Validation Notes

1. VIC source SQL original — Value Investors Club / supplied SQL, 2010-02-22. 원문 description·catalyst·작성자·raw direction·valuation 수치의 기준
2. [ePlus FY2009 Form 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — SEC / ePlus, 2009-06-16. filing 정상화·2008-09-03 NASDAQ 재상장과 당시 balance sheet 검증
3. [ePlus FY2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — SEC / ePlus, 2010-06. technology/financing segment와 recourse/non-recourse 구조 검증
4. [ePlus FY2025 results](https://www.eplus.com/who-we-are/investor-relations/press-releases/2025/05/eplus-reports-fourth-quarter-and-fiscal-year-2025-financial-results) — ePlus, 2025-05-22. 장기 technology/services scale와 financing mix 검증

### 데이터 품질

- 원문·metadata: **A/B** — 첨부 SQL description/catalyst와 공개 VIC link를 우선했다.
- 사업·공시: **A** — SEC 또는 회사 공식 보고서를 사용했다.
- 가격성과: **B/C** — SQL row 부재; 임의 수익률을 만들지 않음.
- 데이터 교정: ticker=PLUS, entity=ePlus inc., raw=Short, research=Long.
