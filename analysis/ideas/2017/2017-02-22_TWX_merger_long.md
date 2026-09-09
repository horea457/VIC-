# Time Warner (TWX) — 2017-02-22 VIC Merger Arbitrage Long

> **Idea unit:** AT&T/Time Warner cash-stock merger spread.
> **Research as-of:** 2026-09-09.

---

## 0. Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2017-02-22 / rhianik |
| 실제 방향 | **Merger Arbitrage Long** |
| 원 SQL 방향 | **Short — metadata 오류** |
| 원문 implied consideration | 약 $107.80 |
| spread | 약 12% absolute / 14% annualized, 2017-12-31 close 가정 |
| 추가 dividend | 3~4회 × $0.405, 약 1.8% |
| 최종 판정 | **성공 — deal은 닫혔지만 timing/규제 risk를 크게 과소평가** |

> **결론:** deal outcome은 성공했다. 하지만 원문이 “vertical deal이고 FCC license transfer도 핵심이 아니어서 높은 closing probability”라고 본 것과 달리 DOJ는 2017년 11월 소송으로 거래를 막으려 했다. 거래는 2018-06-14에야 끝났다. 즉 **direction은 맞고 annualized return forecast는 duration 때문에 악화**됐다.

---

## 1. 거래 구조

AT&T와 Time Warner는 2016-10-22 merger agreement를 체결했다.

- cash: $53.75
- stock: 약 $53.75 worth, collar 적용
- AT&T average price < $37.411: 1.437 shares
- > $41.349: 1.3 shares
- 중간 구간: $53.75 / average price
- TWX termination fee 약 $1.725bn
- AT&T termination fee $500m

원문 당시 T 주가로 consideration은 약 $107.80, spread 약 12%.

---

## 2. 원문 edge

시장은 세 가지를 할인한다고 봤다:
1. Trump administration의 공개 반대
2. deal size 때문에 arb capital 부족
3. AT&T short leg의 4.7% dividend carry

작성자는 vertical integration의 antitrust risk가 낮고, fail해도 TWX가 peer와 비슷한 valuation이라 downside가 제한적이라고 봤다.

---

## 3. Claim Map

### C1. deal은 높은 확률로 close — 성공
최종적으로 2018-06-14 완료됐다.

### C2. regulatory path는 상대적으로 단순 — 실패
DOJ는 2017-11-20 civil antitrust suit를 제기했다. 이것은 단순 delay가 아니라 실제 deal-break risk였다.

### C3. year-end 2017 close — 실패
실제 closing은 2018-06-14. duration은 약 5.5개월 더 길어졌다.

### C4. fail downside는 제한적 — 미검증
deal이 깨지지 않았으므로 counterfactual downside는 관찰되지 않았다. 당시 standalone asset quality는 높았지만 broad market/sector 움직임과 AT&T deal overhang을 함께 고려해야 했다.

### C5. collar mechanics는 hedge 가능 — 성공
최종적으로 TWX 각 주식은 $53.75 cash + 1.437 AT&T shares로 교환됐다.

### C6. dividend carry가 spread를 보완 — 성공
TWX shareholder는 closing 전 선언된 배당을 받았지만 exact arb IRR에는 T short dividend, borrow, financing cost도 함께 넣어야 한다.

---

## 4. Payoff 구조

원문 annualized 14%는 2017-12-31 close라는 duration 가정에 민감했다. Merger arb에서 동일한 absolute spread도 close가 6개월 밀리면 annualized IRR은 크게 내려간다.

또 stock collar 거래이므로 단순 “107.50 고정 cash deal”이 아니다. 최종 consideration은 실제로 $53.75 cash + 1.437 T shares였다.

---

## 5. 실제 타임라인

| 날짜 | 사건 |
|---|---|
| 2016-10-22 | merger agreement |
| 2017-02-22 | VIC arb Long |
| 2017-11-20 | DOJ lawsuit |
| 2018-03~06 | antitrust trial |
| 2018-06-12 | district court가 DOJ challenge 기각 |
| 2018-06-14 | acquisition 완료 |
| close | $53.75 cash + 1.437 T shares |

---

## 6. 투자결과

**deal leg는 성공**이다. 다만 원문이 예상한 2017년말보다 closing이 늦어졌고, DOJ suit 기간 spread volatility와 mark-to-market drawdown이 컸을 가능성이 높다. 원 DB에 hedge ratio, T short entry, dividends paid on short, financing cost가 없어 exact realized IRR은 계산하지 않는다.

---

## 7. Claim Verdict

| Claim | Weight | 판정 |
|---|---:|---|
| close probability high | 30% | 성공 |
| regulatory simplicity | 20% | 실패 |
| 2017 year-end close | 15% | 실패 |
| fail downside limited | 10% | 미검증 |
| collar mechanics | 15% | 성공 |
| dividend carry | 10% | 성공 |

---

## 8. 핵심 투자 교훈

이 아이디어의 가장 중요한 교훈은 **deal probability와 deal duration은 별개 변수**라는 것이다. 최종적으로 100% close해도 규제소송 때문에 annualized return과 risk-adjusted return은 원문보다 훨씬 나빠질 수 있다.

---

## 9. 최초 경고

2017-11-20 DOJ가 공식 소송을 제기한 순간이다. 이때 position은 “높은 확률의 routine vertical deal”에서 “법원 판결에 의존하는 litigated arb”로 바뀌었다. 동일 size를 유지하려면 payoff tree를 완전히 다시 써야 했다.

---

## 10. 재사용 체크리스트

- regulator jurisdiction과 정치발언을 분리
- lawsuit probability를 0이 아닌 explicit branch로 둠
- expected close date가 3/6/9개월 밀릴 때 IRR 계산
- stock collar hedge ratio와 dividend carry 계산
- deal break downside를 unaffected price 하나가 아니라 peer beta까지 반영

---

## 11. Scorecard

| 평가축 | 판정 |
|---|---|
| Deal direction | 9/10 |
| Regulatory analysis | 5/10 |
| Timing | 4/10 |
| Security mechanics | 8/10 |
| Process | 8/10 |
| 종합 | **성공 — deal close, 그러나 duration/DOJ risk 과소평가** |

### 한 문장 교훈
> merger arb에서 “결국 닫힌다”보다 더 중요한 질문은 “어떤 경로와 얼마나 긴 시간 후 닫히는가”다.

---

## 12. Sources

1. VIC original / uploaded SQL, 2017-02-22.
2. AT&T merger terms: https://www.sec.gov/Archives/edgar/data/732717/000119312516744400/d268996dex991.htm
3. DOJ complaint, 2017-11-20: https://www.justice.gov/archives/opa/pr/justice-department-challenges-attdirectv-s-acquisition-time-warner
4. AT&T closing consideration: https://www.sec.gov/Archives/edgar/data/732717/000119312518194502/d609728d8k.htm
5. AT&T stockholder guide: https://investors.att.com/stockholder-services/cost-basis-guide/worksheet/time-warner

### 데이터 품질
Deal terms/outcome A. Exact arb IRR 미복원.
