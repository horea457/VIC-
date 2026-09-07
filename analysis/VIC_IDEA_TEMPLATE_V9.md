# VIC Individual Idea Deep-Dive Template V9

> 목적: 한 VIC 아이디어를 처음 읽는 사람도 **당시 회사와 시장 상황 → 원문의 핵심 주장 → 당시 성립조건과 반증조건 → 실제로 일어난 사건 → 실제 투자수익 → 무엇을 맞히고 틀렸는지 → 재사용 가능한 투자 교훈**까지 한 파일에서 추적할 수 있게 한다.
>
> 작성 원칙: **같은 사실을 여러 섹션에서 다시 설명하지 않는다.** 사실은 최초 등장 섹션에 충분히 기록하고, 이후에는 해당 Claim ID / Event ID / 표를 참조한다. “회사 설명”, “원문 논지”, “사후 사건”, “판정”, “투자성과”를 서로 섞지 않는다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | |
| VIC 게시일 | YYYY-MM-DD |
| VIC 원문 링크 | |
| 작성자 | |
| Security | Common / Preferred / Bond / Option / Other |
| 방향 | Long / Short / Special Situation |
| 게시일 기준 진입가격 | |
| 당시 시가총액 / EV | |
| 원문 목표가격 | |
| 원문 기대수익률 | |
| 원문 목표기간 | |
| 핵심 촉매 | |
| 최종 상태 | 성공 / 실패 / 혼합 / 진행 중 |
| 데이터 검증 기준일 | YYYY-MM-DD |

### 가격 기준 규칙
- 게시일이 거래일이면 **게시일 종가**를 기본 진입가격으로 사용한다.
- 게시 시간이 장 마감 이후임이 명확하면 **다음 거래일 종가 또는 시가 중 하나를 DB 전체에 통일**한다.
- 휴장일이면 다음 거래일을 사용하고 반드시 표시한다.
- 수정주가 여부, 분할, 특별배당, spin-off, rights offering 등은 별도 조정한다.
- Short는 단순 Long CAGR을 뒤집지 않는다. **가격 Short return, 연환산 return, 최대 역행폭, borrow/carry**를 분리한다.

---

# 1. 회사는 정확히 무엇을 하는가

이 섹션의 목적은 투자논지를 말하는 것이 아니라, **처음 보는 사람이 손익계산서와 현금흐름이 어떻게 만들어지는지 이해하게 하는 것**이다.

## 1.1 고객과 제공 가치
- 실제 고객은 누구인가.
- 고객이 이 회사를 쓰는 이유는 무엇인가.
- 고객이 지불하는 금액은 무엇에 대한 대가인가.
- 대체재는 무엇인가.
- 구매 빈도, 계약기간, switching cost, mission-critical 여부를 설명한다.

## 1.2 산업 가치사슬과 회사의 위치
다음 흐름을 문장으로 설명한다.

**원재료/공급자 → 회사 → 유통/파트너 → 최종고객 → 결제자**

필수:
- 누구에게 돈을 받는가.
- 누구에게 가장 큰 비용을 지불하는가.
- 가격결정권은 누구에게 있는가.
- 공급자와 고객 중 어느 쪽이 더 강한가.
- 산업의 bottleneck이 무엇인가.

## 1.3 매출에서 FCF까지의 경제 엔진
매출액 숫자를 나열하지 말고 경제적 흐름을 설명한다.

**Volume × Price / Take rate → Revenue → Gross profit → S&M/R&D/G&A → EBIT/EBITDA → Capex/WC/Tax → FCF**

필수 질문:
- Volume 성장의 원천은 무엇인가.
- 가격 또는 take rate는 구조적으로 유지 가능한가.
- gross margin이 무엇에 의해 움직이는가.
- 성장 시 추가로 필요한 비용은 무엇인가.
- working capital이 성장에 현금을 공급하는가, 소모하는가.
- 유지보수 Capex와 성장 Capex를 구분할 수 있는가.
- 회계이익과 주주 FCF가 크게 다른 이유가 있는가.

## 1.4 단위경제성
사업에 맞는 최소 단위를 정의한다.

예:
- 고객 1명
- 주문 1건
- 매장 1개
- 항공기 1대
- 보험계약 1건
- 생산설비 1톤
- 가입자 1명
- 대출 1건

가능하면 다음을 산출한다.
- Revenue / unit
- Gross profit / unit
- CAC
- retention / churn
- contribution margin
- payback period
- incremental margin
- incremental ROIC

## 1.5 경쟁우위와 산업 구조
- 주요 경쟁사와 차별점
- scale economy
- network effect
- switching cost
- 브랜드
- cost advantage
- distribution
- regulation/license
- data advantage
- 공급 제한
- 경쟁우위가 실제로 **가격, 점유율, retention, margin, ROIC** 중 어디에 나타나는지

“moat가 있다”라고 끝내지 않고 **재무 숫자로 어떻게 관찰되는지**까지 적는다.

## 1.6 자본집약도와 자본구조
- 순현금 / 순부채
- 주요 만기
- 변동금리/고정금리
- convertibles / preferred / earn-out / contingent consideration
- off-balance-sheet obligation
- 리스
- pension
- SBC
- 희석 가능 증권
- 인수에 필요한 반복적 자본

특히 Short, distressed, cyclical 아이디어는 이 섹션을 생략하지 않는다.

## 1.7 매 분기 볼 핵심 KPI
5~10개로 제한한다. 단순 매출·EPS가 아니라 **논지가 먼저 깨질 수 있는 leading indicator**를 우선한다.

---

# 2. 당시 상황과 시장이 가격에 넣고 있던 것

이 섹션은 “회사가 좋다/나쁘다”가 아니라 **왜 그 가격에서 아이디어가 존재했는가**를 설명한다.

## 2.1 게시 당시 상황
- 직전 1~3년 사업 변화
- 최근 실적
- 주가 흐름
- 산업 사이클
- 규제/금리/원자재/경쟁 변화
- 최근 M&A 또는 구조조정
- 시장이 주목한 사건

## 2.2 당시 시장의 지배적 내러티브
가능하면 당시 sell-side, 기업 가이던스, valuation multiple, 투자자 논리를 근거로 복원한다.

예:
- 시장은 몇 년 성장률을 기대했는가.
- margin 정상화를 얼마나 반영했는가.
- 어떤 TAM 또는 점유율을 전제했는가.
- cycle peak/trough를 정상상태로 착각했는가.
- 자산가치, liquidation value, optionality를 무시했는가.

## 2.3 가격이 암묵적으로 요구한 미래
Reverse DCF 또는 간단한 expectation bridge를 사용한다.

**현재 가격이 맞으려면 무엇이 몇 년 동안 어느 정도 지속되어야 하는가?**

최소 하나:
- 필요한 매출 CAGR
- 필요한 terminal margin
- 필요한 FCF margin
- 필요한 ROIC
- 필요한 market share
- 필요한 commodity price
- 필요한 loss ratio / spread / utilization

---

# 3. 원문 투자논지 지도

원문을 요약해서 다시 쓰는 것이 아니라 **검증 가능한 주장 단위로 분해**한다.

최소 6개 Claim을 권장하되, 억지로 숫자를 채우지 않는다.

| Claim ID | 원문 핵심 주장 | 작동 메커니즘 | 당시 근거 | 숨은 가정 | 사전 반증조건 |
|---|---|---|---|---|---|
| C1 | | | | | |
| C2 | | | | | |
| C3 | | | | | |
| C4 | | | | | |
| C5 | | | | | |
| C6 | | | | | |

## Claim 작성 규칙

각 Claim은 다음 5가지를 포함해야 한다.

### C1. [주장 제목]
**원문 주장**  
원문 작성자가 무엇을 믿었는지 정확히 설명한다.

**경제적 메커니즘**  
A가 변하면 왜 B가 변하고, 그것이 결국 FCF/주당가치에 어떻게 연결되는지 적는다.

**당시 확인 가능했던 근거**  
게시 당시 공시·산업 데이터·가격·경쟁 상황으로 검증한다. 사후 정보를 섞지 않는다.

**숨은 가정**  
논지가 맞으려면 사실상 참이어야 하지만 원문에서 충분히 드러나지 않은 가정을 적는다.

**사전 반증조건**  
게시 당시 투자자가 미리 정할 수 있었던 “이 수치/사건이 나오면 내 논지가 틀렸다고 인정한다”를 적는다.

> C2 이후 동일 형식을 반복한다.

---

# 4. 당시 Valuation과 Payoff Structure

## 4.1 원문의 가치평가
- 사용한 multiple / DCF / NAV / sum-of-parts / liquidation / replacement cost
- 목표가격
- 예상 기간
- 예상 upside/downside
- 핵심 가정

원문 숫자가 모호하면 모호하다고 표시하고 임의로 보완한 숫자와 분리한다.

## 4.2 재구성한 정상화 가치
가능하면 다음 연결을 명시한다.

**산업 규모 → 회사 점유율 → 매출 → margin → 세후 영업이익 → reinvestment → FCF → EV → 순부채/기타 청구권 → 완전희석 Equity value → 주당가치**

## 4.3 시나리오 분석

| Case | 핵심 가정 | 영업 결과 | 가치 / 주가 | 게시가 대비 수익률 |
|---|---|---:|---:|---:|
| Bear | | | | |
| Base | | | | |
| Bull | | | | |

Short라면 명칭을 Short thesis / Middle / Adverse squeeze case로 바꿔도 된다.

## 4.4 촉매와 시간
- 촉매가 실제 가치변화를 만드는가, 단순히 시장의 인식을 바꾸는가.
- 촉매가 없으면 논지가 몇 년 지연될 수 있는가.
- refinance, maturity, covenant, trial, regulatory decision, earnings reset 등 **시간의 강제성**이 있는가.
- Short는 “비싸다” 외에 포지션이 살아 있는 동안 re-rating될 이유가 있는지 반드시 적는다.

## 4.5 포지션의 비대칭성
Long:
- 영구손실 위험
- 희석
- 레버리지
- downside floor
- optionality

Short:
- borrow availability / fee
- squeeze 가능성
- takeover risk
- strategic financing
- 최대 주가 역행 가능성
- 포지션 크기 제한
- 손절/재검토 rule

---

# 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

이 섹션은 **사실만 기록한다. 판정은 Section 7에서 한다.**

최소 6개 이상의 의미 있는 Event를 권장한다.

| Event ID | 날짜 | 실제 사건 | 핵심 수치 | 출처 |
|---|---|---|---:|---|
| E1 | | | | |
| E2 | | | | |
| E3 | | | | |
| E4 | | | | |
| E5 | | | | |
| E6 | | | | |

포함 후보:
- 분기 실적
- 가이던스 변경
- 경쟁사 진입/철수
- 제품 실패/성공
- 규제
- M&A
- 자산매각
- 증자/차입
- 파산/구조조정
- management change
- cycle reversal
- litigation
- capital return

### 실제 사업 추이
필요한 경우 핵심 시계열을 한 표에 모은다.

| 연도/분기 | Revenue/Volume | Margin | FCF | Net debt | 핵심 KPI |
|---|---:|---:|---:|---:|---:|
| | | | | | |

동일 숫자를 다른 섹션에서 다시 표로 만들지 않는다.

---

# 6. 실제 투자결과 — 가격 경로와 실현 가능 수익

## 6.1 진입
- 기준 진입가격:
- 날짜:
- Security:
- 방향:
- 가격 데이터 출처:
- corporate action 조정:

## 6.2 가격 경로

| 시점 | 날짜 | 가격 | Long/Short 단순 가격수익률 | 연환산 수익률 | 해석 |
|---|---|---:|---:|---:|---|
| 직후 | | | | | |
| 1개월 | | | | | |
| 6개월 | | | | | |
| 1년 | | | | | |
| 2년 | | | | | |
| 3년 | | | | | |
| 목표기간 종료 | | | | | |
| 최종 검증일 | | | | | |

모든 기간을 억지로 채울 필요는 없지만 **원문의 목표기간은 반드시 포함**한다.

## 6.3 경로위험
반드시 계산:
- MFE: Maximum Favorable Excursion
- MAE: Maximum Adverse Excursion
- 최고/최저 가격과 날짜
- thesis가 맞기 전 최대 역행폭
- 해당 역행폭에서 현실적으로 포지션 유지가 가능했는지

## 6.4 IRR / CAGR 판정

### Long
배당과 corporate action을 포함한 total return을 우선한다.

### Short
다음을 분리한다.
1. Short price return
2. 보유기간 연환산 return
3. borrow fee / dividend payment / carry
4. squeeze 및 margin path

단순히 “최종 주가가 0이 됐으니 성공”으로 판정하지 않는다.

## 6.5 Exit rule별 결과
원문에 명시적 exit가 있으면 그대로 사용한다. 없으면 다음을 분리해 보여준다.
- 목표가 도달 청산
- 원문 목표기간 종료
- 최초 명확한 thesis break
- terminal outcome까지 보유

---

# 7. Claim별 사후 판정

여기에서 처음으로 Section 3의 주장과 Section 5의 실제 사건을 연결한다.  
**사건 자체는 반복 설명하지 않고 Event ID를 참조한다.**

| Claim ID | 판정 | 관련 Event | 최초 확인/반증 시점 | 왜 맞거나 틀렸나 | 당시 알 수 있었나 |
|---|---|---|---|---|---|
| C1 | 적중/부분/실패/미판정 | E1,E3 | | | |
| C2 | | | | | |
| C3 | | | | | |
| C4 | | | | | |
| C5 | | | | | |
| C6 | | | | | |

### 판정 기준
- **적중**: 메커니즘과 결과가 모두 대체로 맞음.
- **부분 적중**: 방향은 맞았으나 원인, 규모, 시점 중 중요한 부분이 틀림.
- **실패**: 핵심 메커니즘 또는 방향이 틀림.
- **미판정**: 아직 충분한 시간이 지나지 않았거나 데이터 부족.

“주가가 올랐으니 논지가 맞았다”는 판정을 금지한다.  
Business thesis와 Security return은 별개의 질문이다.

---

# 8. 무엇이 실제 수익을 만들거나 파괴했는가

Section 7이 개별 Claim 판정이라면 이 섹션은 **전체 결과의 인과관계 우선순위**를 정한다.

## 8.1 결과 기여도
중요도 순으로 3~7개를 정리한다.

예:
1. 본업 매출/수요
2. margin / unit economics
3. valuation multiple
4. 자본배분
5. 레버리지/자금조달
6. macro/cycle
7. 규제
8. 인수/매각
9. 예상하지 못한 외생사건

각 요소에 대해:
- 원문이 예상했는가.
- 예상했다면 중요도를 맞췄는가.
- 실제 equity return에 얼마나 중요했는가.

## 8.2 원문이 놓친 가장 중요한 변수
한두 개만 선정한다.  
사후적으로 일어난 모든 일을 나열하지 않는다.

## 8.3 반사실
다음 질문 중 중요한 것을 답한다.
- 이 한 사건이 없었다면 투자결과가 달라졌는가.
- valuation만 달랐어도 좋은 회사/나쁜 투자가 되었는가.
- leverage가 없었다면 equity가 생존했는가.
- 경영진의 자본배분이 달랐다면 사업논지는 맞았는가.
- macro/cycle이 평범했다면 원문 주장은 여전히 유효했는가.

---

# 9. 분석 오류의 유형

틀린 아이디어뿐 아니라 맞은 아이디어에도 적용한다.

해당되는 것만 선택:
- 산업구조 오판
- moat 과대/과소평가
- 가격결정력 오판
- TAM 외삽
- 평균회귀 무시
- cycle peak/trough 오판
- unit economics와 consolidated economics 혼동
- 회계이익과 FCF 혼동
- working capital 오판
- maintenance capex 과소추정
- dilution/SBC 무시
- leverage/refinancing 위험 무시
- M&A/capital allocation 위험 무시
- 규제 오판
- 경쟁자 대응 무시
- management incentive 오판
- valuation은 맞지만 timing 실패
- catalyst 부재
- 경로위험/position sizing 실패
- 좋은 회사와 좋은 주식 혼동
- terminal thesis와 investable setup 혼동

### 최초로 관찰 가능했던 경고신호
- 날짜
- 데이터
- 당시 투자자가 실제로 볼 수 있었는지
- 그 시점에 포지션을 줄이거나 닫았어야 했는지

---

# 10. 이 아이디어에서 추출할 수 있는 재사용 가능한 교훈

기업 고유 사실을 다시 요약하지 않는다.  
**다른 회사에도 적용할 수 있는 규칙**으로 변환한다.

예시 형식:

### Lesson 1 — [일반화된 규칙]
- 어떤 상황에서 유효한가
- 어떤 지표로 확인하는가
- 언제 예외가 생기는가

### Lesson 2 — [일반화된 규칙]
...

### 지금 같은 아이디어를 다시 본다면
- 반드시 먼저 확인할 5개 데이터
- 진입 전에 필요한 3개 조건
- 포지션을 줄일 3개 반증 신호

---

# 11. 최종 Scorecard

| 항목 | 판정 | 한 줄 근거 |
|---|---|---|
| Business thesis | 적중/부분/실패 | |
| Industry thesis | | |
| Competitive thesis | | |
| Unit economics thesis | | |
| Valuation thesis | | |
| Catalyst thesis | | |
| Timing thesis | | |
| Capital allocation thesis | | |
| Balance-sheet thesis | | |
| Security selection | | |
| Position/path survivability | | |
| 최종 투자결과 | | |

### 한 문장 교훈
> 이 아이디어를 다시 한 문장으로 기억해야 한다면 무엇인가.

---

# 12. Sources / Validation Notes

## 12.1 Source hierarchy
가능하면 아래 순서로 사용한다.

1. 회사 10-K / 10-Q / 20-F / annual report / 공식 실적자료
2. SEC / 규제기관 / 법원 / 정부자료
3. 경쟁사 공식자료
4. 원 VIC 게시물
5. 당시 기사와 sell-side/industry 자료
6. 역사적 가격 데이터

## 12.2 검증되지 않은 항목
확인되지 않은 숫자를 사실처럼 쓰지 않는다.

| 항목 | 현재 사용값 | 문제 | 추가 검증 필요 |
|---|---:|---|---|
| | | | |

## 12.3 데이터 품질 표시
- **A:** 1차 공시/규제기관으로 직접 확인
- **B:** 신뢰할 만한 2차 자료와 교차검증
- **C:** 단일 2차 자료
- **D:** 추정치/근사치

---

# 작성 품질 기준

## 최소 밀도
아이디어마다 기계적으로 동일한 길이를 요구하지는 않지만, 일반적인 완성본은 다음 수준을 목표로 한다.

- 핵심 Claim: **6개 전후**
- 수치 검증: **최소 6개**
- 의미 있는 사후 Event: **최소 6개**
- 가격 검증 시점: **최소 5개 + 원문 목표기간**
- 1차 자료 중심 출처: **최소 5개**
- 기업 KPI: **5~10개**
- 반증조건: **각 핵심 Claim마다 1개 이상**
- MFE / MAE: **가능한 모든 상장주식 아이디어에서 필수**

분석의 길이는 내용에 따라 달라지되, **짧게 쓰기 위해 핵심 메커니즘을 생략하지 않는다.**

---

# 중복 방지 규칙 — 가장 중요

각 정보의 “정본 위치”를 아래처럼 고정한다.

| 정보 | 한 번만 자세히 쓰는 위치 |
|---|---|
| 회사 사업모델 | Section 1 |
| 당시 시장 기대 | Section 2 |
| 원문 주장/근거/가정 | Section 3 |
| 당시 valuation/payoff | Section 4 |
| 사후 실제 사건/실적 | Section 5 |
| 주가/IRR/경로 | Section 6 |
| 주장별 맞음/틀림 판정 | Section 7 |
| 전체 결과의 근본 원인 | Section 8 |
| 분석 프로세스 오류 | Section 9 |
| 다른 종목에 적용할 교훈 | Section 10 |
| 최종 압축 판정 | Section 11 |
| 출처/불확실성 | Section 12 |

### 금지
- Section 1에서 투자논지를 미리 설명
- 각 Claim에서 사후 결과까지 섞어 작성
- Section 5에서 “따라서 원문이 틀렸다”라고 판정
- Section 7에서 Section 5의 사건을 다시 장문 설명
- RECAP에서 이미 쓴 투자논지를 다시 서술
- 최종 주가만 보고 성공/실패 판정
- 회사 매출 성장과 주주 수익률을 동일시
- Short의 terminal outcome만 보고 실행 성공으로 판정

---

# 파일 운영 규칙

권장 파일 단위는 **VIC 아이디어 1개 = Markdown 1개**다.

권장 경로 예시:

`analysis/ideas/2019/2019-08-08_FTCH_short.md`

또는 기존 batch 번호를 유지해야 한다면:

`analysis/ideas/2019/batch_001_2019-08-08_FTCH_short.md`

같은 회사의 서로 다른 시점/논지는 **별도 파일**로 둔다.  
기업 단위가 아니라 **투자 의사결정 단위**가 기준이다.

예:
- 2009 CHK Short
- 2012 CHK Long
- 2020 CHK distressed

이들은 같은 회사라도 서로 다른 아이디어이므로 세 파일로 분리한다.

기존 30개 묶음 batch 파일은 원본/아카이브로 유지하고, 각 아이디어의 심층분석 파일을 정본으로 연결한다.
