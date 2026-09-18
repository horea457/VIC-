# Agribrands International (AGX) — 2000-09-21 VIC Long

> **Idea unit:** 2000-09-21 Agribrands International common equity Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short이고 company table은 Argan Inc.로 연결되지만, 원문 실제 회사는 **Agribrands International**, 실제 방향은 **Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 실제 회사 | **Agribrands International** |
| 당시 Ticker | AGX |
| SQL company mapping | **ARGAN INC — 오류** |
| VIC 게시일 / 작성자 | 2000-09-21 / gary9 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| implied 당시 가격 | 약 **$41** |
| private value | **$59.50/share** |
| market cap / book | 약 **$425m / $382m** |
| net cash | **>$150m** |
| TEV / EBITDA | 약 **$275m / $95m = 2.9x** |
| 핵심 catalyst | Ralcorp deal break + superior strategic buyer |
| actual buyer | **Cargill** |
| cash takeout | **$54.50/share** |
| deal value | 약 **$580m** |
| 최종 판정 | **강한 성공 — superior bidder가 2~3개월 내 가치 crystallize** |

> **결론:** SQL의 AGX는 현재 Argan Inc.에 매핑돼 있지만 2000년 original은 animal-feed maker **Agribrands International**이다. 원문은 Ralcorp merger가 저가 거래라 깨질 가능성이 높고, net cash와 global animal-nutrition franchise를 감안하면 $59.50 정도의 private value가 있다고 봤다. 실제 2000년 12월 Cargill이 **$54.50 cash/share**, 약 $580m에 인수하기로 합의하며 Ralcorp 거래를 깨뜨렸다. implied ~$41 entry 대비 약 +33%를 2~3개월 만에 crystallize한 강한 성공이다.

---

## 1. Company Mapping 교정

Agribrands는:
- Ralston Purina에서 1998 spin-off,
- Purina/Checkerboard animal-feed brands,
- international animal nutrition

회사였다.

현재 SQL의 AGX-to-Argan mapping은 ticker reuse로 인한 역사적 오류다.

---

## 2. 원문 투자논지

원문:
- market cap $425m
- book $382m
- net cash >$150m
- EBITDA ~$95m
- TEV/EBITDA ~2.9x
- private value $59.50
- Ralcorp terms too low

를 근거로 superior offer 가능성을 봤다.

---

## 3. Claim Map

### C1. Ralcorp deal이 깨질 수 있다 — **강한 성공**
Cargill offer 때문에 기존 Ralcorp merger가 종료됐다.

### C2. strategic buyer exists — **강한 성공**
Cargill이 animal nutrition scale/synergy를 인정했다.

### C3. private value near high-$50s — **매우 근접**
actual bid **$54.50**.

### C4. downside protected by cash/book — **성공**
높은 net cash와 low EV/EBITDA가 alternative-value anchor 역할.

### C5. catalyst timing — **강한 성공**
VIC post 약 2.5개월 뒤 Cargill deal 발표.

---

## 4. Payoff

원문의 45% upside to $59.50에서 implied current price를 역산하면 약 $41.

따라서:

**$54.50 / ~$41 - 1 ≈ +33%**

정확 purchase fill이 없으므로 approximate다.

---

## 5. 재사용 가능한 교훈

1. historical ticker는 date + legal entity로 검증한다.
2. signed merger라도 superior-bid optionality가 존재한다.
3. low EV/EBITDA + net cash는 strategic buyer의 downside anchor가 될 수 있다.
4. breakup fee를 alternative-bid economics에 포함한다.
5. private value estimate는 실제 strategic bid로 가장 강하게 검증된다.

---

## 6. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Company identification | SQL correction |
| Valuation | 강한 성공 |
| Catalyst | 강한 성공 |
| Strategic exit | 강한 성공 |
| Thesis score | 9.8/10 |
| Process score | 9.9/10 |
| 종합 | **강한 성공 — Cargill $54.50 cash, implied entry 대비 약 +33%** |

### 한 문장 교훈

> merger 상황에서 **현재 계약가가 아니라 회사가 다른 buyer에게 얼마의 전략적 가치가 있는지를 따로 계산하면 superior bid를 잡을 수 있다.**

---

## 7. Sources / Validation Notes

1. VIC original / uploaded SQL, 2000-09-21.
2. Cargill acquisition at $54.50 cash/share, ~$580m: https://www.latimes.com/archives/la-xpm-2000-dec-05-fi-61293-story.html
3. SEC merger proxy confirming $54.50/share cash: https://www.sec.gov/Archives/edgar/data/1047598/000095013801000014/0000950138-01-000014-0002.pdf

### 데이터 품질
- T0 thesis: **A**
- company identity/takeout: **A**
- implied entry return: **B**
