# Time Warner (TWX) — 2006-01-31 VIC Jan-2008 LEAPS Long

> **Idea unit:** TWX common이 아니라 Jan-2008 $15 strike call의 payoff를 중심으로 본다.
> **Research as-of:** 2026-09-09.

---

## 0. Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Time Warner / TWX |
| 게시일 / 작성자 | 2006-01-31 / beech625 |
| 실제 증권 / 방향 | Jan-2008 $15 calls / **Long** |
| 원 SQL 방향 | **Short — metadata 오류** |
| 당시 common | 원문 $17.50 |
| option premium | 원문 $4.20 |
| breakeven | $19.20 at expiration |
| double / triple 조건 | common $23.40 / $27.60 |
| 최종 판정 | **실패 — underlying value-unlock보다 option clock이 빨랐다** |

> **결론:** Icahn 압력, $12.5bn buyback, TWC 가치분리, AOL 전략변경 등 자본배분/구조개편 방향은 상당 부분 이후 현실화됐다. 그러나 2007년 TWX 주가의 연중 high가 $23.15로 원문이 제시한 “double” threshold $23.40에도 못 미쳤고 2007년말 종가는 $16.51이었다. 장기 corporate thesis와 2년짜리 option payoff를 혼동한 사례다.

---

## 1. 회사와 증권

당시 Time Warner는 TWC, Turner/HBO, Warner Bros., AOL, Publishing을 한 지붕 아래 둔 conglomerate였다. 시장은 AOL dial-up decline, 전통광고 둔화, cable 경쟁, publishing 약화를 할인했다.

원문은 common을 직접 사는 대신 Jan-2008 $15 call을 $4.20에 사 leverage를 높였다. 이 증권의 현금 payoff는 매우 단순하다.

- expiration intrinsic = max(TWX price - $15, 0)
- 투자손익 = intrinsic - $4.20 premium
- breakeven = $19.20
- target은 주가 $23.40이면 약 2배, $27.60이면 약 3배

기업이 “언젠가” 가치가 드러나는 것과 옵션 만기 전 가치가 드러나는 것은 전혀 다른 문제다.

---

## 2. 당시 mispricing 가설

2002년 이후 비용절감·부채감축·사업합리화가 진행됐는데 주가는 이를 반영하지 않는다고 봤다. 핵심 촉매는:
1. $12.5bn share repurchase
2. TWC 16% float와 궁극적 separation
3. AOL access/advertising 재편
4. asset sales
5. Icahn의 activism
6. 낮은 implied volatility의 정상화

원문은 Icahn 측 SOTP $26~28이 공격적이지만 방향은 맞다고 봤다.

---

## 3. Claim Map

### C1. TWC 독립가치가 TWX discount를 줄인다 — 장기 성공, horizon 실패
TWC는 결국 2009년 완전 분리됐다. 그러나 Jan-2008 option에는 너무 늦었다.

### C2. buyback이 주당가치를 빠르게 올린다 — 부분 성공
대규모 repurchase는 실행됐지만 conglomerate discount와 AOL/미디어 우려를 2년 안에 충분히 이기지 못했다.

### C3. AOL의 광고/Google 관계가 access decline을 상쇄한다 — 실패/과대
AOL은 결국 2009년 별도 spin-off됐다. 이는 “좋은 성장자산으로 재평가”보다 “문제자산 분리”에 가까웠다.

### C4. traditional media sentiment mean reversion — 실패
2007년 이후 금융위기 전조와 미디어 구조변화가 multiple expansion을 막았다.

### C5. low volatility option은 싸다 — 실패
옵션가격이 싸 보여도 **catalyst timing distribution**이 만기 밖이면 zero/low payoff가 된다.

### C6. 2년 안에 $23.40~27.60 도달 — 실패
Time Warner 2007 annual report는 2007년 high $23.15, low $16.17, 12/31 close $16.51을 기록한다. 적어도 원문의 double threshold $23.40은 2007년에 달성되지 않았다.

---

## 4. Valuation과 option convexity

원문은 TWC에 8.5x EBITDA, 기타 segment SOTP를 적용해 common value를 $20대 중후반으로 봤다. 문제는 SOTP가 맞아도 market가 그 가치를 **만기 전** 인정해야 한다는 것이다.

LEAPS는 valuation gap을 leverage하는 대신 time value decay와 catalyst timing risk를 산다. 특히 conglomerate break-up이 board·tax·financing·regulatory 절차를 거치면 2년은 짧다.

---

## 5. 실제 타임라인

| 날짜 | 사건 | 의미 |
|---|---|---|
| 2006-01-31 | VIC LEAPS Long | Jan-2008 clock 시작 |
| 2006~07 | buyback·TWC public-market value visibility | 일부 촉매 |
| 2007 | TWX high $23.15 | double threshold $23.40 미달 |
| 2007-12-31 | TWX $16.51 | expiration 직전 weak |
| 2009-03 | TWC 완전 spin-off | 옳은 촉매, 너무 늦음 |
| 2009-12 | AOL spin-off | conglomerate simplification 완성 |

---

## 6. 투자결과

정확한 2008-01-18 option settlement와 중간 매도 여부가 원 DB에 없어 realized IRR을 만들지 않는다. 다만 2007년 연중 최고가가 $23.15라 원문의 “double/triple common threshold”를 달성하지 못했고 연말 $16.51은 $19.20 expiration breakeven 아래였다.

따라서 **security-level thesis는 실패**로 본다. 이후 2009년 TWC/AOL separation이 성공했다고 해서 expired/decayed option의 결과가 바뀌지는 않는다.

---

## 7. Claim Verdict

| Claim | Weight | 판정 |
|---|---:|---|
| TWC hidden value | 20% | 장기 성공 |
| buyback | 15% | 부분 성공 |
| AOL turnaround | 15% | 실패/분리 |
| sentiment rerating | 15% | 실패 |
| option cheapness | 15% | 실패 |
| $23.40~27.60 within horizon | 20% | 실패 |

---

## 8. 핵심 오류

**사업가치 duration과 증권 duration mismatch.** Activism, spin-off, asset sale은 방향을 맞혀도 일정이 미끄러지기 쉽다. 원문은 “2년이면 충분하다”는 부분을 valuation보다 약하게 검증했다.

---

## 9. 최초 경고

2007년 동안에도 주가가 $23.40 threshold를 넘지 못하고 연말 $16.51로 내려간 것이 가장 직접적인 경고다. 이 시점에는 remaining time value보다 corporate event calendar를 다시 계산했어야 했다.

---

## 10. 재사용 교훈

1. event-driven LEAPS는 SOTP보다 event calendar가 중요하다.
2. spin-off thesis는 board approval·record date·tax work·financing을 단계별로 둔다.
3. 좋은 장기 thesis라도 option은 실패할 수 있다.
4. “싼 volatility”와 “싼 option”은 동일하지 않다.

---

## 11. Scorecard

| 평가축 | 판정 |
|---|---|
| Business/SOTP insight | 7.5/10 |
| Catalyst direction | 7/10 |
| Timing | 2/10 |
| Security selection | 2/10 |
| Process | 7/10 |
| 종합 | **실패 — 맞는 corporate direction을 너무 짧은 option으로 샀다** |

### 한 문장 교훈
> event thesis의 duration이 불확실할수록 leverage보다 만기 선택이 먼저다.

---

## 12. Sources

1. VIC original / uploaded SQL, 2006-01-31.
2. Time Warner 2007 Annual Report / SEC: https://www.sec.gov/Archives/edgar/data/1105705/000095014408001291/g11419e10vk.htm
3. TWC spin-off disclosure: https://www.sec.gov/Archives/edgar/data/1105705/000095014409003643/g18170e10vq.htm
4. AOL spin-off disclosure: https://www.sec.gov/Archives/edgar/data/1395942/000119312509235507/dex991.htm

### 데이터 품질
Exact option expiration price와 trade exit는 미복원. 따라서 option IRR은 계산하지 않는다.
