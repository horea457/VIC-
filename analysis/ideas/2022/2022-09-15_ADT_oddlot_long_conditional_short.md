# ADT Inc. (ADT) — 2022-09-15 VIC Odd-Lot Tender / Conditional Short

> **Security/direction audit:** raw SQL은 Short지만 실제 아이디어는 **A) 99-share odd-lot Long/tender + B) $9 접근 시 조건부 outright Short**의 event-driven two-leg idea.
> **Research as-of:** 2026-09-11.

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2022-09-15 / MadDog2020 |
| raw 방향 | Short |
| 실제 구조 | **Odd-lot Long + conditional Short** |
| tender price | **$9.00/share** |
| tender size | **133,333,333 shares / $1.2bn** |
| expiration | **2022-10-20** |
| Apollo commitment | 최소 tender 전량을 채울 수 있도록 backstop |
| odd-lot protection | **99주 이하 tender는 proration 우선권** |
| final result | tender oversubscribed, **odd lots accepted in full** |
| SQL underlying price | 1M +2.2%, 3M +21.1% |
| 최종 판정 | **Odd-lot leg 강한 성공 / conditional Short는 실행여부 불명, 실행했다면 불리** |

> **결론:** 이건 방향성 주식 아이디어가 아니라 tender mechanics 아이디어다. 99주를 매수해 $9에 tender하는 A-leg는 실제 최종 결과에서 odd lots가 전량 수락되며 정확히 실현됐다. 반면 tender 이후 returned shares의 매도압력을 노린 조건부 Short는 주가가 3개월 동안 오히려 상승했기 때문에 실제 진입했다면 좋지 않았다. **Event trade는 회사 전망이 아니라 문서의 priority rule을 읽는 투자**다.

---

## 1. 거래 구조

State Farm은 ADT에:
- 133,333,333 shares
- $9/share
- 총 **$1.2bn**

을 투자.

ADT는 같은 금액과 주식 수를 $9에 self-tender해 희석을 상쇄.

Apollo는 tender가 fully subscribed 되도록 최소 133,333,333 shares를 tender하기로 약정.

따라서 일반 주주는 oversubscription/proration risk가 매우 높았다.

---

## 2. A-leg — Odd-lot Long

원문:
> 99 shares를 사고 October 20 이전 tender.

Tender document는 **odd lot priority**를 명시.

즉 100주 미만을 보유하고 전량 tender하는 qualifying holder는 일반 proration 전에 우선 수락될 수 있었다.

### Actual
2022-10-26 final results:
- validly tendered: **732.1m shares**
- accepted: **133.333m shares**
- 일반적으로 pro rata
- **odd-lot tenders accepted in full**

따라서 A-leg의 legal/mechanical thesis는 강하게 성공.

정확한 수익은 개인 매수가격에 따라 달라지므로 고정 IRR은 산출하지 않는다.

---

## 3. B-leg — Conditional outright Short

원문은 주가가 $9에 접근하면 Short를 검토.

논리:
- Apollo owns ~67%
- tender는 Apollo liquidity event 성격
- 다른 기관도 tender 가능
- proration 후 돌려받은 shares가 시장에 나오면 sell pressure
- $9 tender price가 near-term upside를 제한

즉:
**tender expiration → returned shares → secondary selling pressure**
를 기대.

---

## 4. B-leg 실제 결과

SQL underlying price:
- 1M **+2.2%**
- 3M **+21.1%**

따라서 $9 부근에서 실제 Short를 실행했다면 초기 months의 price path는 불리했다.

다만 원문은 조건부 아이디어이고 실제 author execution 여부는 확인되지 않으므로 **실패한 실제 trade라고 단정하지 않는다.**

---

## 5. Claim Map

### C1. tender will be oversubscribed — **강한 성공**
732m+ tender vs 133m accepted.

### C2. odd lots avoid proration — **강한 성공**
공식 final results가 전량수락 확인.

### C3. Apollo uses tender for liquidity — **성공**
Apollo support agreement가 구조를 뒷받침.

### C4. returned shares create near-term pressure — **실패 방향**
3M underlying price는 오히려 +21%.

### C5. no meaningful upside near $9 — **실패/과도**
시장가격은 tender event 이후 $9를 넘을 수 있었다.

---

## 6. 왜 좋은 special-situation leg였나

A-leg는 operating forecast가 거의 필요 없다.

필요한 것은:
1. offer price
2. expiration
3. odd-lot definition
4. proration order
5. financing certainty
6. withdrawal rights

였다.

이는 business valuation보다 **contractual payoff**에 가깝다.

---

## 7. 재사용 체크리스트

1. odd-lot tender는 99/100-share definition을 원문으로 확인한다.
2. household/account aggregation rule을 확인한다.
3. tender price 대비 spread에서 commission/tax를 차감한다.
4. oversubscription이면 proration priority를 읽는다.
5. event Long과 post-event Short를 한 방향으로 저장하지 않는다.
6. conditional trade는 실제 trigger/entry 여부를 별도로 기록한다.

### 한 문장 교훈
> **기업을 예측하지 않아도 공시문서의 우선순위 조항 하나를 정확히 읽으면 작은 확정형 알파가 생길 수 있다.**

## 8. Sources

1. VIC original: https://www.valueinvestorsclub.com/idea/ADT_INC/7810567042
2. Offer to Purchase: https://www.sec.gov/Archives/edgar/data/1703056/000119312522242339/d304311dex99a1a.htm
3. Tender final results: https://www.sec.gov/Archives/edgar/data/1703056/000119312522269117/d372018dex99a5g.htm
