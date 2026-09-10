# Weight Watchers International (WTW) — 2015-05-05 VIC Capital Structure Pair

> **Security audit:** raw SQL은 단순 Short로 저장했지만 실제 아이디어는 **common equity Short + Tranche B-1 1st-lien term loan Long**의 capital-structure pair trade.
> **Ticker-performance audit:** WTW raw price series는 후대 Willis Towers Watson ticker reuse로 오염되어 본 판정에 사용하지 않음.
> **Research as-of:** 2026-09-10.

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2015-05-05 / pistolpete |
| 실제 포지션 | **WTW common Short + B-1 term loan Long** |
| common 당시 가격 | 약 **$8.46** |
| B-1 loan 가격 | 약 **89** |
| B-1 principal | 약 **$292.3m** |
| B-1 maturity | **2016-04-02** |
| B-2 | 약 $2.1bn / 당시 distressed level |
| base expected return | 약 **52% / 12~18M** |
| 실제 loan outcome | **2016-04-01 cash로 전액 par 상환** |
| 실제 equity outcome | Oprah deal 이후 강한 squeeze / bankruptcy thesis 실패 |
| 최종 판정 | **credit leg 성공 / equity leg 실패 / pair thesis 실패** |

> **결론:** 이 아이디어는 단순 Weight Watchers Short가 아니라 “senior loan은 money-good, common은 option-like zero”라는 자본구조 상대가치 거래였다. 핵심 credit insight는 맞았다. 회사는 2016년 B-1을 현금으로 전액 상환했다. 그러나 equity가 bankruptcy로 가기 전에 Oprah가 2015-10 전략적 투자자로 들어오며 refinancing/narrative probability가 급변했다. **한 자본구조 안에서도 security별 thesis는 따로 관리해야 한다.**

---

## 1. 당시 회사 / 현금엔진

WTW의 두 profit pools:
1. Meetings
2. WeightWatchers.com / Digital

2011 이후:
- meeting attendance 하락
- product sales 감소
- online growth 둔화
- free apps / fitness trackers 침투
- 높은 leverage

가 겹쳤다.

### 원문이 본 핵심 operating deterioration
- attendance 2009 약 62% → 2015 약 48%
- product sales 2011 $442.7m → 2014 $298.0m
- organic revenue growth 2014 분기 -10%대
- online revenue growth도 음전환

---

## 2. 자본구조 논리

### Common Short
원문:
- overlevered
- B-2 distressed
- 2020 refinancing risk
- operating metrics deterioration
- bankruptcy 가능

### B-1 Long
- price 89
- maturity 11개월
- outstanding ~$292.3m
- cash + undrawn revolver가 충분
- senior position
- maturity가 B-2보다 훨씬 빠름

따라서:
**기업 전체가 나빠도 B-1은 상환될 수 있다.**

이것이 좋은 capital-structure insight였다.

---

## 3. 원문 payoff

Base:
- common Short 약 +35%
- B-1 pull-to-par / carry 약 +16.4%
- total 약 **+52%**

Bull-for-short:
- bankruptcy
- common near zero
- B-1 recovery / post-reorg value

---

## 4. 실제 타임라인

| 날짜 | 사건 |
|---|---|
| 2015-05-05 | pair trade 게시 |
| 2015-10-19 | Oprah Winfrey, 6.36m shares 매입 + options + board/strategic collaboration |
| 2015 Q4 | equity narrative 급반전 |
| 2016-04-01 | **Tranche B-1 잔액 $144.3m 현금으로 전액 상환** |
| 이후 | company turnaround / equity recovery |

---

## 5. Claim Map

### C1. B-1 is money-good — **강한 성공**
2016-04-01 par repayment으로 직접 확인.

### C2. common deteriorates further — **실패**
새 strategic catalyst가 equity optionality를 크게 재평가.

### C3. B-2 leverage creates bankruptcy path — 당시 유효했으나 결과적으로 실패
회사는 회생했고 bankruptcy는 오지 않았다.

### C4. digital competitors are structural threat — 부분 성공
위협 자체는 맞았지만 brand/capital/Oprah catalyst로 생존.

---

## 6. 가장 중요한 분석 오류

**Capital structure는 잘 읽었지만 equity의 positive optionality를 너무 낮게 평가했다.**

Common equity는:
- brand
- new sponsor
- celebrity/marketing
- equity injection
- refinancing

같은 out-of-model catalyst의 가치가 컸다.

---

## 7. 재사용 체크리스트

1. pair trade는 각 leg의 P&L을 따로 기록한다.
2. senior maturity wall과 junior maturity wall을 분리한다.
3. distressed loan이 par 상환 가능하다고 common Short가 자동으로 맞는 것은 아니다.
4. consumer brand equity에는 strategic sponsor optionality를 둔다.
5. capital-structure trade는 **net expected return**뿐 아니라 leg별 squeeze risk를 본다.

### 한 문장 교훈
> **같은 회사에서 senior credit는 정확히 맞히고 equity는 완전히 틀릴 수 있다. 자본구조 분석은 ‘기업 전망’이 아니라 각 청구권의 payoff를 따로 보는 작업이다.**

## 8. Sources

1. VIC original / uploaded SQL, 2015-05-05.
2. Oprah share purchase / collaboration: https://www.sec.gov/Archives/edgar/data/105319/000119312515346212/d59417d8k.htm
3. B-1 repayment: https://www.sec.gov/Archives/edgar/data/105319/000119312516527974/d165778d8k.htm
