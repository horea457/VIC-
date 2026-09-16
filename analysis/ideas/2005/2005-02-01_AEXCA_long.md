# Ampex Corporation (AEXCA) — 2005-02-01 VIC Long

> **Idea unit:** 2005-02-01 Ampex Corporation common equity Long.
> **Research as-of:** 2026-09-17. 원 SQL Long과 실제 방향이 일치한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Ampex Corporation / AEXCA |
| VIC 게시일 / 작성자 | 2005-02-01 / gearl1818 |
| 실제 방향 | Common equity Long |
| 당시 주가 경로 | 약 $4에서 $40대까지 급등 후 아이디어 제출 |
| fully diluted shares | 약 4m |
| 핵심 논지 | IP licensing + data-storage/DoD recorder + debt paydown |
| 원문 minimum EPS frame | 약 **$6.25 through 2014** |
| 원문 upside | licensing 확대 시 훨씬 높은 EPS/가치 |
| terminal outcome | **2008 Chapter 11, 기존 Class A common cancellation** |
| 최종 판정 | **강한 실패 — IP value가 debt waterfall 뒤 common을 보호하지 못함** |

> **결론:** 원문은 Ampex의 digital-imaging 특허 licensing과 data-storage business를 합쳐 높은 per-share earnings를 기대했다. 하지만 핵심 오류는 licensing cash flow를 **common에 귀속되는 durable annuity처럼 본 것**이었다. legacy business와 debt 부담, patent expiry/renewal risk가 equity보다 먼저 cash를 흡수했다. 2008년 Chapter 11 plan에서 기존 common은 취소됐고 주주에게는 equity distribution이 없었다. 일부 contingent payment rights가 남았지만 이는 원 common의 가치보존으로 보기 어렵다.

---

## 1. 회사는 정확히 무엇을 하는가

Ampex는 역사적으로 magnetic recording 기술기업이었고, 2000년대에는 두 축이 있었다.

1. **Licensing/IP:** digital still camera, image processing, recording 관련 특허 royalty.
2. **Data systems:** government/defense 및 specialized recording/storage systems.

원문은 licensing 수익이 높은 margin을 가지므로 debt를 빠르게 줄이고 common EPS가 크게 늘 수 있다고 봤다.

핵심 현금식은:

`royalty cash + data-systems operating profit - litigation/R&D - interest - debt repayment - capex = residual equity cash`

이다.

### 매 분기 볼 핵심 KPI

royalty revenue by patent family, patent expiry dates, licensee concentration, litigation outcomes, data-system bookings/backlog, cash interest, debt balance, unrestricted cash, FCF

---

## 2. 당시 상황과 시장이 가격에 넣은 것

Ampex 주가는 2004년 전후 약 $4에서 $40대까지 이미 크게 상승했다. 원문은 fully diluted shares가 약 4m에 불과해 licensing earnings가 per-share로 크게 증폭될 수 있다고 봤다.

핵심 bull case:

- current licensing agreements가 최소 $6.25/share 수준 earnings를 지지
- additional camera/electronics licensees가 붙으면 EPS $8~9 이상 가능
- licensing cash로 debt를 빠르게 축소
- specialty storage business에도 별도 가치

### Reverse expectations

이 thesis가 성립하려면 **royalty stream이 patent expiry 이후에도 재계약/신규특허로 이어지고**, litigation·debt service가 licensing cash를 잠식하지 않아야 했다.

---

## 3. 원문 투자논지 지도

### C1. licensing은 durable high-margin annuity다 — 실패

특정 핵심 특허의 만기와 license renewal 불확실성이 컸다. royalty stream은 bond-like cash flow가 아니었다.

### C2. minimum EPS ~$6.25가 장기간 유지된다 — 강한 실패

후속 business economics와 restructuring은 이 normalized EPS가 common에 지속 귀속되지 않았음을 보여준다.

### C3. licensing cash가 debt를 낮춰 equity convexity를 만든다 — 실패

debt burden과 legacy operating obligations가 계속 중요했고, 결국 enterprise value가 debt claims를 충분히 초과하지 못했다.

### C4. data-storage/DoD business가 downside를 보완한다 — 실패

specialized business 가치가 common을 보호할 만큼 충분하지 않았다.

### C5. IP monetization이 common holder에게 남는다 — 강한 실패

2008 restructuring에서 기존 common은 cancellation. Contingent payment rights가 일부 부여됐지만 기존 equity ownership은 사라졌다.

---

## 4. 당시 Valuation과 Payoff Structure

원문 접근은 대략:

`normalized licensing EPS × multiple + storage value - debt`

였다. 그러나 IP company에서 더 안전한 방식은:

`patent-by-patent remaining royalty PV - litigation/tax - debt claims + operating asset recovery`

로 equity residual을 계산하는 것이다.

### 핵심 위험

- 핵심특허 만기
- license renewal gap
- customer concentration
- litigation cost
- debt service
- tiny share count가 upside뿐 아니라 downside dilution/recap sensitivity도 증폭

---

## 5. 실제로 무슨 일이 일어났는가 — 사후 타임라인

| 날짜 | 사건 | 의미 |
|---|---|---|
| 2005-02-01 | VIC Long | IP royalty thesis |
| 2005~07 | licensing/operating volatility | annuity quality 의문 확대 |
| 2008-03-30 | Chapter 11 filing | capital structure 실패 |
| 2008 | plan confirmation | existing Class A common cancellation |
| 2008-10-03 | old common cancelled | terminal security outcome |

---

## 6. 실제 투자결과 — security outcome

source SQL에는 performance row가 없다. 하지만 terminal outcome은 명확하다. **기존 common은 plan에서 취소됐고 equity holder는 reorganized common distribution을 받지 못했다.**

일부 contingent payment rights는 향후 IP monetization이 특정 threshold를 넘을 때만 가치가 생기는 제한적 권리였으므로 기존 common의 성공적인 recovery로 분류하지 않는다.

---

## 7. Claim별 사후 판정

| Claim | Weight | 판정 | 핵심 gap |
|---|---:|---|---|
| durable licensing stream | 25% | 실패 | patent/renewal duration 과대평가 |
| $6.25 minimum EPS | 20% | 강한 실패 | durable common EPS 아님 |
| debt paydown | 20% | 실패 | restructuring 필요 |
| storage downside value | 15% | 실패 | debt waterfall 보호 못함 |
| additional licenses upside | 10% | 일부/불충분 | common protection 못함 |
| equity survival | 10% | 강한 실패 | cancelled |

---

## 8. 무엇이 실제 손실을 만들었는가

**duration mismatch**가 핵심이다. 시장은 royalty income을 높게 평가했지만 debt는 고정된 claim이고 IP cash flow는 만기·법률·license renewal에 따라 변했다. royalty가 줄면 enterprise value가 debt 아래로 빠르게 내려갈 수 있었다.

### Counterfactual

IP portfolio를 debt-free entity가 보유했다면 thesis의 일부는 유효했을 수 있다. 그러나 leveraged capital structure에서 common은 특허 duration을 틀리는 순간 가장 먼저 소멸하는 security였다.

---

## 9. 재사용 가능한 교훈

1. IP royalty는 계약·특허별 만기표를 만들어야 한다.
2. licensing EPS를 perpetual annuity처럼 multiple화하지 않는다.
3. debt가 있는 IP company는 enterprise recovery부터 계산한다.
4. tiny share count는 per-share upside만 강조하면 위험하다.
5. contingent rights는 common recovery와 구분한다.

---

## 10. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business/IP thesis | 실패 |
| Valuation thesis | 강한 실패 |
| Capital structure | 과소평가 |
| Security outcome | common cancelled |
| Thesis score | 2.0/10 |
| Process score | 9.5/10 |
| 종합 | **강한 실패 — IP cash flow가 debt 뒤 common을 보호하지 못함** |

### 한 문장 교훈

> 높은 royalty margin보다 먼저 봐야 할 것은 **그 royalty가 언제 끝나고, debt를 갚은 뒤 common에 얼마가 남는가**다.

---

## 11. Sources / Validation Notes

1. VIC original / uploaded SQL, 2005-02-01 — licensing/EPS/debt thesis.
2. Ampex SEC filings, 2005-2008 — debt, licensing and operating disclosures.
3. Ampex Chapter 11 plan / company releases, 2008 — existing common cancellation and contingent payment rights.

### 데이터 품질

- T0 thesis: **A**.
- terminal restructuring outcome: **A** — SEC/court/company releases.
- exact holding return: **미확정** — SQL performance row 없음; terminal cancellation을 decisive outcome으로 사용.
