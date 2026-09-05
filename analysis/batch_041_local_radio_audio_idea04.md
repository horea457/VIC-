# ENTERCOM COMMUNICATIONS CORP (ETM) — 2018-07-23 VIC Short

**idea_id:** `3027530a-b943-4fe7-8fb5-ea719a6f9c0b`  
**원 SQL 방향:** Short  
**원문 검증 방향:** **Short**  
**분석 security:** ETM common equity short  
**종합 판정:** **강한 성공**

## 1. 결론부터

이 숏의 핵심은 CBS Radio 인수로 커진 headline EBITDA가 아니라 **debt-bearing capacity**였다. 원문은 ETM을 약 6.3x leverage, 10.5x 2018 EBITDA로 보고, legacy와 acquired stations 양쪽에서 광고 headwind가 심해지면 50% 이상의 downside가 가능하다고 봤다. 최종적으로 Audacy는 2024년 Chapter 11에서 약 $1.9bn의 funded debt를 약 $350m까지 줄여야 했으므로 구조적 thesis는 강하게 적중했다.

## 2. 원 투자논지

CBS Radio deal이 2017년 11월 닫힌 뒤 시장은 scale과 synergy를 강조했지만, 원 작성자는 early fact pattern이 revenue stabilization을 지지하지 않는다고 봤다. radio는 고정비 비중이 높기 때문에 low-single-digit revenue miss도 EBITDA와 leverage에 비선형적으로 전달된다. 따라서 높은 multiple과 높은 leverage가 동시에 존재하는 상황에서 equity는 debt claim의 얇은 residual이었다.

## 3. 사업과 돈의 흐름

라디오 방송은 제한된 spectrum과 지역 브랜드를 보유하지만 수익은 광고 inventory 판매에서 나온다. 비용의 상당 부분이 고정적이어서 광고단가·spot volume이 하락하면 incremental margin이 역으로 작동한다. M&A로 station 수가 늘어도 debt service는 계약적으로 고정되어 있으며, secular listener migration이 지속되면 cost synergy만으로는 자본구조를 방어하기 어렵다.

## 4. 핵심 가정

숏이 맞으려면 세 가지가 필요했다. 첫째 CBS Radio revenue가 빠르게 안정화되지 않아야 했다. 둘째 industry advertising weakness가 일시적 경기둔화가 아니라 구조적 성격을 가져야 했다. 셋째 cost synergy와 free cash flow가 debt를 충분히 빨리 줄이지 못해야 했다. 반대로 organic revenue가 성장 전환하고 leverage가 4x 이하로 빠르게 내려왔다면 숏은 깨졌을 것이다.

## 5. 실제 전개

2018년 Entercom net revenue는 인수효과로 $1.463bn까지 확대됐다. 그러나 이것은 organic 회복의 증거가 아니었다. 이후 회사는 digital audio와 podcasting 등으로 확장했지만 traditional radio advertising 압력과 부채부담이 누적됐다. Audacy는 2024년 1월 구조조정을 발표하면서 지난 수년간 traditional advertising market의 지속적 거시 압력과 누적 radio ad spending 감소를 직접 원인으로 들었고, 약 $1.6bn의 funded debt를 equitize해 총부채를 약 $1.9bn에서 $350m로 낮췄다.

## 6. 주장별 검증

**산업 headwind:** 적중. 회사 자체가 2024 restructuring 설명에서 장기간의 radio-ad decline을 지목했다.  
**CBS scale이 문제를 해결한다:** 실패. 매출규모는 커졌지만 leverage를 상쇄할 만큼 durable한 organic improvement가 나오지 않았다.  
**높은 leverage가 equity downside를 증폭한다:** 강하게 적중. 최종적으로 balance sheet 자체가 법원 절차를 통해 재구성됐다.  
**valuation:** 10.5x EBITDA는 당시 reported EBITDA보다 normalized debt capacity를 기준으로 봐야 했다는 교훈을 남겼다.

## 7. 핵심 수치

| 지표 | 값 | 의미 |
|---|---:|---|
| Thesis leverage | 6.3x | 원 VIC의 핵심 위험변수 |
| 2018 EBITDA multiple | 10.5x | 원 VIC valuation |
| 2018 net revenue | $1.463bn | CBS Radio 편입 후 규모 |
| 2024 funded-debt reduction | 약 80% | $1.9bn → $350m |

## 8. 촉매와 타임라인

- **2018-07-23** — VIC Short: 6.3x leverage, 50%+ downside 논지.
- **2018-12-31** — CBS Radio 편입 첫 full year; 매출은 인수효과로 크게 증가.
- **2021** — Audacy로 브랜드 전환, multi-platform audio 전략 강화.
- **2023** — 광고환경과 부채부담이 재무유연성을 압박.
- **2024-01-07** — prepackaged Chapter 11 및 $1.9bn→$350m 구조 발표.
- **2024-09-30** — restructuring 완료, 약 80% debt reduction.

## 9. 반증조건

CBS stations가 organic 성장으로 돌아서고, cost/revenue synergies가 recurring FCF로 나타나며, net leverage가 빠르게 4x 이하로 하락했다면 숏의 핵심은 무효였다. 따라서 유사 딜에서는 reported synergy가 아니라 **revenue sensitivity를 적용한 normalized EBITDA 대비 leverage**를 추적해야 한다.

## 10. 재사용 가능한 교훈

쇠퇴산업의 roll-up에서는 `EV/EBITDA`보다 `debt / stressed-normalized EBITDA`가 먼저다. acquisition accounting으로 커진 매출을 organic 회복으로 착각하면 안 된다. 산업 revenue pool 감소율과 interest burden을 합친 hurdle보다 synergy가 크지 않으면, 좋은 자산 인수도 common equity에는 나쁜 거래가 될 수 있다.

### 연구 메모

raw SQL `is_short=true`는 원문과 일치해 그대로 보존했다. SQL에 정밀 historical return이 없어 임의의 가격수익률은 만들지 않고, 회사의 확정 restructuring 결과를 중심으로 postmortem을 판정했다.

### Sources

- VIC 2018 ETM Short — SQL original description (public source link 미수록)
- [Entercom 2017 Form 10-K](https://www.sec.gov/Archives/edgar/data/1067837/000119312518085958/d548878d10k.htm)
- [Entercom 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1067837/000119312519054296/d712409d10k.htm)
- [CBS Radio merger close](https://www.sec.gov/Archives/edgar/data/813828/000119312517350719/d471182d8k.htm)
- [Audacy restructuring announcement](https://audacyinc.com/press/audacy-reaches-agreement-with-a-supermajority-of-its-debtholders-on-balance-sheet-deleveraging-transaction-that-will-equitize-over-80-of-the-companys-debt-and-establish-a-robust-capital-struc/)
- [Audacy restructuring completion](https://audacyinc.com/press/audacy-successfully-completes-financial-restructuring-emerges-as-a-growing-scaled-multi-platform-audio-leader-with-the-industrys-strongest-balance-sheet/)
