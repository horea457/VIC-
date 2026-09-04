# Batch 014 — T-Mobile US·Altice USA 10건

평가기준일: 2024-01-31

분석일: 2026-09-04

대상: T-Mobile US 7건·Altice USA 3건

## 결론부터

이번 배치는 **같은 통신 인프라·고정비 산업에서 operating leverage와 capital structure가 equity에 정반대로 작동한 사례**를 비교한다.

- **T-Mobile US:** 가격·브랜드·network execution이 net adds와 churn 개선으로 이어졌고, Sprint의 2.5GHz spectrum과 중복망 제거가 EBITDA·FCF를 확장했다. 이후 buyback은 이미 좋아진 FCF를 주당가치로 옮기는 마지막 단계였다.
- **Altice USA:** broadband의 높은 증분마진과 cost cutting은 사실이었지만, 높은 leverage 상태에서 고객·EBITDA 안정성을 과신했다. levered buyback은 사업이 꺾이자 equity cushion을 빠르게 줄였다.

> 데이터 경고: 2015-04-06 TMUS 아이디어는 원 SQL `is_short=true`지만 본문상 실제 방향은 Long이다. 원본 flag는 감사추적용으로 보존하고 분석 방향만 Long으로 교정한다.

---

# ALTICE USA (ATUS) — 기업과 비즈니스

## 1. 무슨 기업인가

Altice USA는 Optimum과 과거 Suddenlink 지역에서 broadband, video, voice, mobile을 제공하는 유선통신 사업자다. broadband는 programming cost가 거의 없어 높은 증분마진을 낼 수 있지만 높은 부채와 고정비 때문에 고객·EBITDA 하락이 equity에 비선형적으로 전달된다. 핵심 지표는 broadband customers/net adds, ARPU, FTTH penetration, EBITDA margin, cash CapEx, FCF, net debt·interest, share count다.

## 2. 산업 가치사슬과 돈의 흐름

video의 programming fee와 달리 broadband는 이미 깔린 HFC/FTTH망에서 속도 tier를 올릴 때 증분비용이 제한적이다. 그러나 fiber overbuild·fixed wireless로 고객이 감소하면 fixed-cost absorption이 역으로 악화된다. FCF의 사용처가 debt paydown인지 levered buyback인지도 사업모델의 일부다.

## 3. 경쟁우위·경쟁구도·핵심 지표

초기 moat는 지역망 진입장벽과 broadband margin이었지만 fiber overbuild와 fixed wireless가 대체재를 만들었다. cost cutting으로 높아진 margin이 durable moat인지, 서비스·망 투자까지 줄여 미래 churn과 catch-up capex를 만든 것인지 구분해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격/사업 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2017-11-15 | Long | Long | Broadband mix·cost cutting·deleveraging 롱 | $20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성 | 단기 가격 부분 성공·구조적 실패 |
| 2019-05-08 | Long | Long | 10x FCF·levered buyback·fiber capex 정상화 롱 | $23.49→$2.44; -89.6% | 치명적 실패 |
| 2021-08-11 | Long | Long | 17% FCF yield·manageable debt·2025 compounding 롱 | $27.44→$2.44; -91.1% | 치명적 실패 |

---

## 1. 2017-11-15 — Broadband mix·cost cutting·deleveraging 롱

### 결론부터

**종합판정: 단기 가격 부분 성공·구조적 실패.** broadband/video margin 분해는 맞았지만 cost cutting으로 높아진 margin을 durable moat로 간주했고 5x 안팎 leverage에서 FCF가 자연스럽게 deleveraging으로 이어질 확률을 과대평가했다.

**주가·증권 결과:** $20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성

**Thesis / Process 점수:** 5 / 6

### 기업·산업 이해

#### 무슨 기업인가

Altice USA는 Optimum과 과거 Suddenlink 지역에서 broadband, video, voice, mobile을 제공하는 유선통신 사업자다. broadband는 programming cost가 거의 없어 높은 증분마진을 낼 수 있지만 높은 부채와 고정비 때문에 고객·EBITDA 하락이 equity에 비선형적으로 전달된다. 핵심 지표는 broadband customers/net adds, ARPU, FTTH penetration, EBITDA margin, cash CapEx, FCF, net debt·interest, share count다.

#### 산업 가치사슬과 돈의 흐름

video의 programming fee와 달리 broadband는 이미 깔린 HFC/FTTH망에서 속도 tier를 올릴 때 증분비용이 제한적이다. 그러나 fiber overbuild·fixed wireless로 고객이 감소하면 fixed-cost absorption이 역으로 악화된다. FCF의 사용처가 debt paydown인지 levered buyback인지도 사업모델의 일부다.

#### 경쟁우위·경쟁구도·핵심 지표

초기 moat는 지역망 진입장벽과 broadband margin이었지만 fiber overbuild와 fixed wireless가 대체재를 만들었다. cost cutting으로 높아진 margin이 durable moat인지, 서비스·망 투자까지 줄여 미래 churn과 catch-up capex를 만든 것인지 구분해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. 고객·broadband economics — 실패 또는 부분 · 비중 18%

**당시 주장**

broadband customer/ARPU가 FCF를 지지

**당시 근거**

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

**이 주장이 성립하려면**

고객수·ARPU 동시 안정

**사전 반증조건**

broadband 고객이 연속 감소

**실제 결과**

2019 EBITDA는 약 $4.27bn으로 기대에 못 미쳤고 FCF는 debt reduction보다 capital return에도 쓰였다. 이후 broadband 경쟁과 투자부담이 커졌고 2023 Adjusted EBITDA는 약 $3.61bn, FCF는 약 $0.12bn까지 감소했다.

**정량적 괴리**

2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

고객·broadband economics 가설은 'broadband 고객이 연속 감소'를 분기별 사전 반증조건으로 둔다.

#### 2. Margin durability — 실패 또는 부분 · 비중 18%

**당시 주장**

cost cutting과 mix 개선이 EBITDA를 유지

**당시 근거**

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

**이 주장이 성립하려면**

서비스 품질·경쟁력 유지

**사전 반증조건**

매출·고객 감소와 EBITDA margin 하락

**실제 결과**

2019 EBITDA는 약 $4.27bn으로 기대에 못 미쳤고 FCF는 debt reduction보다 capital return에도 쓰였다. 이후 broadband 경쟁과 투자부담이 커졌고 2023 Adjusted EBITDA는 약 $3.61bn, FCF는 약 $0.12bn까지 감소했다.

**정량적 괴리**

2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

Margin durability 가설은 '매출·고객 감소와 EBITDA margin 하락'를 분기별 사전 반증조건으로 둔다.

#### 3. CapEx normalization — 실패 또는 부분 · 비중 16%

**당시 주장**

fiber/network capex가 정상화

**당시 근거**

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

**이 주장이 성립하려면**

passings 완료 후 capex/revenue 하락

**사전 반증조건**

경쟁대응 투자 재가속

**실제 결과**

2019 EBITDA는 약 $4.27bn으로 기대에 못 미쳤고 FCF는 debt reduction보다 capital return에도 쓰였다. 이후 broadband 경쟁과 투자부담이 커졌고 2023 Adjusted EBITDA는 약 $3.61bn, FCF는 약 $0.12bn까지 감소했다.

**정량적 괴리**

2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

CapEx normalization 가설은 '경쟁대응 투자 재가속'를 분기별 사전 반증조건으로 둔다.

#### 4. Deleveraging/Buyback — 실패 또는 부분 · 비중 16%

**당시 주장**

FCF가 debt와 share count를 개선

**당시 근거**

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

**이 주장이 성립하려면**

정상 FCF 유지·refinancing 원활

**사전 반증조건**

FCF 감소 속 leverage 고착

**실제 결과**

2019 EBITDA는 약 $4.27bn으로 기대에 못 미쳤고 FCF는 debt reduction보다 capital return에도 쓰였다. 이후 broadband 경쟁과 투자부담이 커졌고 2023 Adjusted EBITDA는 약 $3.61bn, FCF는 약 $0.12bn까지 감소했다.

**정량적 괴리**

2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

Deleveraging/Buyback 가설은 'FCF 감소 속 leverage 고착'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 실패 또는 부분 · 비중 16%

**당시 주장**

사업이 2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60로 귀속

**당시 근거**

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업지표 대비 equity value 악화

**실제 결과**

$20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성

**정량적 괴리**

$20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

주당가치 귀속 가설은 '사업지표 대비 equity value 악화'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 실패 또는 부분 · 비중 16%

**당시 주장**

special dividend·capital return으로 높은 leverage가 유지가 thesis를 확인/반증

**당시 근거**

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. 추가 비용절감과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했고 연 $1.5bn 이상의 FCF로 net debt가 $21.1bn에서 $18bn까지 내려갈 것으로 봤다.

**이 주장이 성립하려면**

반증 시 즉시 재평가

**사전 반증조건**

목표가만 기다리며 반증 무시

**실제 결과**

$20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성

**정량적 괴리**

$20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

촉매와 보유경로 가설은 '목표가만 기다리며 반증 무시'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2019 EBITDA는 약 $4.27bn으로 기대에 못 미쳤고 FCF는 debt reduction보다 capital return에도 쓰였다. 이후 broadband 경쟁과 투자부담이 커졌고 2023 Adjusted EBITDA는 약 $3.61bn, FCF는 약 $0.12bn까지 감소했다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

broadband/video margin 분해는 맞았지만 cost cutting으로 높아진 margin을 durable moat로 간주했고 5x 안팎 leverage에서 FCF가 자연스럽게 deleveraging으로 이어질 확률을 과대평가했다.

#### 최초 검증·반증 신호와 회피 가능성

2018-01-08 — special dividend·capital return으로 높은 leverage가 유지. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

단기 가격 부분 성공·구조적 실패. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $20.26 | $30.60 | $2.44 | 장기 실패 |
| EBITDA | 약 $4.0bn | 2019 $4.5~4.6bn | 2019 $4.27bn; 2023 $3.61bn | 미달→하락 |
| Net debt | $21.1bn | 2019 $18bn | 높은 레버리지 유지 | 실패 |
| FCF | $1.5bn+ | debt reduction | 2023 약 $0.12bn | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-11-15 | VIC 아이디어 게시 | Broadband mix·cost cutting·deleveraging 롱 |
| 2018-01-08 | special dividend·capital return으로 높은 leverage가 유지 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2019 EBITDA는 약 $4.27bn으로 기대에 못 미쳤고 FCF는 debt reduction보다 capital return에도 쓰였다. 이후 broadband 경쟁과 투자부담이 커졌고 2023 Adjusted EBITDA는 약 $3.61bn, FCF는 약 $0.12bn까지 감소했다. |
| 2024-01-31 | 고정 평가기준일 | $20.26→$2.44; -88.0%. 2019년 중 $30대 일시 달성 |

### Failure / Success Anatomy

- **근본 오류:** 높은 leverage에서 EBITDA 안정성 확률을 과대평가
- **최초 검증·반증 신호:** 2018-01-08 — special dividend·capital return으로 높은 leverage가 유지
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 높음. 고객·CapEx·EBITDA가 동시에 악화될 때 debt stress를 재계산할 수 있었다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** broadband_mix; asset_value; fcf_yield
- **실패·주의 패턴:** leverage; buyback_at_wrong_state; capex_underestimate; competitive_overbuild; timing_path

### 주요 근거자료

- 1. VIC ALTICE USA 2017-11-15 원문 — Value Investors Club, 2017-11-15. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. Altice USA 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828020001613/atus-20191231.htm) — SEC, 2020-02-13. 사업·수치·가격 사후검증
- [3. Altice USA 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828021001975/atus-20201231.htm) — SEC, 2021-02-11. 사업·수치·가격 사후검증
- [4. Altice USA 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828022002873/atus-20211231.htm) — SEC, 2022-02-16. 사업·수치·가격 사후검증
- [5. Altice USA FY2022 Results](https://www.sec.gov/Archives/edgar/data/1702780/000162828023004565/a2022q4exhibit991.htm) — Altice USA/SEC, 2023-02-22. 사업·수치·가격 사후검증
- [6. Altice USA 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828024004863/atus-20231231.htm) — SEC, 2024-02-14. 사업·수치·가격 사후검증
- [7. Altice USA historical prices](https://www.digrin.com/stocks/detail/ATUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 2. 2019-05-08 — 10x FCF·levered buyback·fiber capex 정상화 롱

### 결론부터

**종합판정: 치명적 실패.** video 저마진·broadband 고마진이라는 분석은 맞았지만 broadband를 사실상 영구 성장자산으로 보고 fiber overbuild와 fixed wireless를 과소평가했다. levered buyback은 사업 악화 시 equity cushion을 줄였다.

**주가·증권 결과:** $23.49→$2.44; -89.6%

**Thesis / Process 점수:** 5 / 6

### 기업·산업 이해

#### 무슨 기업인가

Altice USA는 Optimum과 과거 Suddenlink 지역에서 broadband, video, voice, mobile을 제공하는 유선통신 사업자다. broadband는 programming cost가 거의 없어 높은 증분마진을 낼 수 있지만 높은 부채와 고정비 때문에 고객·EBITDA 하락이 equity에 비선형적으로 전달된다. 핵심 지표는 broadband customers/net adds, ARPU, FTTH penetration, EBITDA margin, cash CapEx, FCF, net debt·interest, share count다.

#### 산업 가치사슬과 돈의 흐름

video의 programming fee와 달리 broadband는 이미 깔린 HFC/FTTH망에서 속도 tier를 올릴 때 증분비용이 제한적이다. 그러나 fiber overbuild·fixed wireless로 고객이 감소하면 fixed-cost absorption이 역으로 악화된다. FCF의 사용처가 debt paydown인지 levered buyback인지도 사업모델의 일부다.

#### 경쟁우위·경쟁구도·핵심 지표

초기 moat는 지역망 진입장벽과 broadband margin이었지만 fiber overbuild와 fixed wireless가 대체재를 만들었다. cost cutting으로 높아진 margin이 durable moat인지, 서비스·망 투자까지 줄여 미래 churn과 catch-up capex를 만든 것인지 구분해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 2023 FCF/share 약 $4.24 ×10 = 약 $42. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. 고객·broadband economics — 실패 또는 부분 · 비중 18%

**당시 주장**

broadband customer/ARPU가 FCF를 지지

**당시 근거**

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

**이 주장이 성립하려면**

고객수·ARPU 동시 안정

**사전 반증조건**

broadband 고객이 연속 감소

**실제 결과**

2020년까지는 broadband와 FCF가 강했지만 2021~23 broadband 고객이 감소했고 2022 cash capex는 약 $1.91bn으로 급증했다. 2023 FCF는 약 $0.12bn으로 축소되어 원래의 FCF floor가 사라졌다.

**정량적 괴리**

2023 FCF/share 약 $4.24 ×10 = 약 $42

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

고객·broadband economics 가설은 'broadband 고객이 연속 감소'를 분기별 사전 반증조건으로 둔다.

#### 2. Margin durability — 실패 또는 부분 · 비중 18%

**당시 주장**

cost cutting과 mix 개선이 EBITDA를 유지

**당시 근거**

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

**이 주장이 성립하려면**

서비스 품질·경쟁력 유지

**사전 반증조건**

매출·고객 감소와 EBITDA margin 하락

**실제 결과**

2020년까지는 broadband와 FCF가 강했지만 2021~23 broadband 고객이 감소했고 2022 cash capex는 약 $1.91bn으로 급증했다. 2023 FCF는 약 $0.12bn으로 축소되어 원래의 FCF floor가 사라졌다.

**정량적 괴리**

2023 FCF/share 약 $4.24 ×10 = 약 $42

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

Margin durability 가설은 '매출·고객 감소와 EBITDA margin 하락'를 분기별 사전 반증조건으로 둔다.

#### 3. CapEx normalization — 실패 또는 부분 · 비중 16%

**당시 주장**

fiber/network capex가 정상화

**당시 근거**

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

**이 주장이 성립하려면**

passings 완료 후 capex/revenue 하락

**사전 반증조건**

경쟁대응 투자 재가속

**실제 결과**

2020년까지는 broadband와 FCF가 강했지만 2021~23 broadband 고객이 감소했고 2022 cash capex는 약 $1.91bn으로 급증했다. 2023 FCF는 약 $0.12bn으로 축소되어 원래의 FCF floor가 사라졌다.

**정량적 괴리**

2023 FCF/share 약 $4.24 ×10 = 약 $42

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

CapEx normalization 가설은 '경쟁대응 투자 재가속'를 분기별 사전 반증조건으로 둔다.

#### 4. Deleveraging/Buyback — 실패 또는 부분 · 비중 16%

**당시 주장**

FCF가 debt와 share count를 개선

**당시 근거**

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

**이 주장이 성립하려면**

정상 FCF 유지·refinancing 원활

**사전 반증조건**

FCF 감소 속 leverage 고착

**실제 결과**

2020년까지는 broadband와 FCF가 강했지만 2021~23 broadband 고객이 감소했고 2022 cash capex는 약 $1.91bn으로 급증했다. 2023 FCF는 약 $0.12bn으로 축소되어 원래의 FCF floor가 사라졌다.

**정량적 괴리**

2023 FCF/share 약 $4.24 ×10 = 약 $42

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

Deleveraging/Buyback 가설은 'FCF 감소 속 leverage 고착'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 실패 또는 부분 · 비중 16%

**당시 주장**

사업이 2023 FCF/share 약 $4.24 ×10 = 약 $42로 귀속

**당시 근거**

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업지표 대비 equity value 악화

**실제 결과**

$23.49→$2.44; -89.6%

**정량적 괴리**

$23.49→$2.44; -89.6%

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

주당가치 귀속 가설은 '사업지표 대비 equity value 악화'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 실패 또는 부분 · 비중 16%

**당시 주장**

고객 성장 회복을 위해 fiber·distribution 투자 확대 발표가 thesis를 확인/반증

**당시 근거**

약 9.5~10x 2019E equity FCF에 거래되는 ATUS가 연 $1.5bn 규모 levered buyback을 지속하면 2022년까지 80~120% upside, 18~25% IRR이 가능하다고 봤다. broadband 고객·ARPU 성장과 FTTH capex의 일시성을 핵심 전제로 뒀다.

**이 주장이 성립하려면**

반증 시 즉시 재평가

**사전 반증조건**

목표가만 기다리며 반증 무시

**실제 결과**

$23.49→$2.44; -89.6%

**정량적 괴리**

$23.49→$2.44; -89.6%

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

촉매와 보유경로 가설은 '목표가만 기다리며 반증 무시'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2020년까지는 broadband와 FCF가 강했지만 2021~23 broadband 고객이 감소했고 2022 cash capex는 약 $1.91bn으로 급증했다. 2023 FCF는 약 $0.12bn으로 축소되어 원래의 FCF floor가 사라졌다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $23.49→$2.44; -89.6%. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

video 저마진·broadband 고마진이라는 분석은 맞았지만 broadband를 사실상 영구 성장자산으로 보고 fiber overbuild와 fixed wireless를 과소평가했다. levered buyback은 사업 악화 시 equity cushion을 줄였다.

#### 최초 검증·반증 신호와 회피 가능성

2021-11-04 — 고객 성장 회복을 위해 fiber·distribution 투자 확대 발표. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

치명적 실패. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $23.49 | 2022 +80~120% | $2.44 | 치명적 실패 |
| Broadband customers | 2~4% 성장 기대 | 지속 증가 | 2021~23 감소 | 실패 |
| Cash CapEx | FTTH 약 $450m 일시 | 정상화 | 2022 $1.91bn; 2023 $1.70bn | 실패 |
| FCF | 약 $1.5bn대 | 2023 FCF/share $4.24 | 2023 약 $0.12bn | 치명적 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-05-08 | VIC 아이디어 게시 | 10x FCF·levered buyback·fiber capex 정상화 롱 |
| 2021-11-04 | 고객 성장 회복을 위해 fiber·distribution 투자 확대 발표 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2020년까지는 broadband와 FCF가 강했지만 2021~23 broadband 고객이 감소했고 2022 cash capex는 약 $1.91bn으로 급증했다. 2023 FCF는 약 $0.12bn으로 축소되어 원래의 FCF floor가 사라졌다. |
| 2024-01-31 | 고정 평가기준일 | $23.49→$2.44; -89.6% |

### Failure / Success Anatomy

- **근본 오류:** 높은 leverage에서 EBITDA 안정성 확률을 과대평가
- **최초 검증·반증 신호:** 2021-11-04 — 고객 성장 회복을 위해 fiber·distribution 투자 확대 발표
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 높음. 고객·CapEx·EBITDA가 동시에 악화될 때 debt stress를 재계산할 수 있었다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** broadband_mix; asset_value; fcf_yield
- **실패·주의 패턴:** leverage; buyback_at_wrong_state; capex_underestimate; competitive_overbuild; timing_path

### 주요 근거자료

- 1. VIC ALTICE USA 2019-05-08 원문 — Value Investors Club, 2019-05-08. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. Altice USA 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828020001613/atus-20191231.htm) — SEC, 2020-02-13. 사업·수치·가격 사후검증
- [3. Altice USA 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828021001975/atus-20201231.htm) — SEC, 2021-02-11. 사업·수치·가격 사후검증
- [4. Altice USA 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828022002873/atus-20211231.htm) — SEC, 2022-02-16. 사업·수치·가격 사후검증
- [5. Altice USA FY2022 Results](https://www.sec.gov/Archives/edgar/data/1702780/000162828023004565/a2022q4exhibit991.htm) — Altice USA/SEC, 2023-02-22. 사업·수치·가격 사후검증
- [6. Altice USA 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828024004863/atus-20231231.htm) — SEC, 2024-02-14. 사업·수치·가격 사후검증
- [7. Altice USA historical prices](https://www.digrin.com/stocks/detail/ATUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 3. 2021-08-11 — 17% FCF yield·manageable debt·2025 compounding 롱

### 결론부터

**종합판정: 치명적 실패.** 위험을 몰랐던 게 아니라 확률배분을 틀렸다. 높은 leverage에서 EBITDA 10~20% 하락이 equity에 비선형적으로 미치는 영향을 충분히 stress하지 않았다.

**주가·증권 결과:** $27.44→$2.44; -91.1%

**Thesis / Process 점수:** 5 / 6

### 기업·산업 이해

#### 무슨 기업인가

Altice USA는 Optimum과 과거 Suddenlink 지역에서 broadband, video, voice, mobile을 제공하는 유선통신 사업자다. broadband는 programming cost가 거의 없어 높은 증분마진을 낼 수 있지만 높은 부채와 고정비 때문에 고객·EBITDA 하락이 equity에 비선형적으로 전달된다. 핵심 지표는 broadband customers/net adds, ARPU, FTTH penetration, EBITDA margin, cash CapEx, FCF, net debt·interest, share count다.

#### 산업 가치사슬과 돈의 흐름

video의 programming fee와 달리 broadband는 이미 깔린 HFC/FTTH망에서 속도 tier를 올릴 때 증분비용이 제한적이다. 그러나 fiber overbuild·fixed wireless로 고객이 감소하면 fixed-cost absorption이 역으로 악화된다. FCF의 사용처가 debt paydown인지 levered buyback인지도 사업모델의 일부다.

#### 경쟁우위·경쟁구도·핵심 지표

초기 moat는 지역망 진입장벽과 broadband margin이었지만 fiber overbuild와 fixed wireless가 대체재를 만들었다. cost cutting으로 높아진 margin이 durable moat인지, 서비스·망 투자까지 줄여 미래 churn과 catch-up capex를 만든 것인지 구분해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 2025 9x EV/EBITDA, debt paydown+buyback → 15~16% CAGR. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. 고객·broadband economics — 실패 또는 부분 · 비중 18%

**당시 주장**

broadband customer/ARPU가 FCF를 지지

**당시 근거**

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

**이 주장이 성립하려면**

고객수·ARPU 동시 안정

**사전 반증조건**

broadband 고객이 연속 감소

**실제 결과**

2022 EBITDA는 전년 대비 12.7% 감소하고 cash capex는 55% 증가했다. 2023 EBITDA는 약 $3.61bn, FCF는 약 $0.12bn으로 더 내려갔다. 저자가 직접 정의했던 EBITDA decline+financing pressure의 toxic mix가 현실화됐다.

**정량적 괴리**

2025 9x EV/EBITDA, debt paydown+buyback → 15~16% CAGR

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

고객·broadband economics 가설은 'broadband 고객이 연속 감소'를 분기별 사전 반증조건으로 둔다.

#### 2. Margin durability — 실패 또는 부분 · 비중 18%

**당시 주장**

cost cutting과 mix 개선이 EBITDA를 유지

**당시 근거**

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

**이 주장이 성립하려면**

서비스 품질·경쟁력 유지

**사전 반증조건**

매출·고객 감소와 EBITDA margin 하락

**실제 결과**

2022 EBITDA는 전년 대비 12.7% 감소하고 cash capex는 55% 증가했다. 2023 EBITDA는 약 $3.61bn, FCF는 약 $0.12bn으로 더 내려갔다. 저자가 직접 정의했던 EBITDA decline+financing pressure의 toxic mix가 현실화됐다.

**정량적 괴리**

2025 9x EV/EBITDA, debt paydown+buyback → 15~16% CAGR

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

Margin durability 가설은 '매출·고객 감소와 EBITDA margin 하락'를 분기별 사전 반증조건으로 둔다.

#### 3. CapEx normalization — 실패 또는 부분 · 비중 16%

**당시 주장**

fiber/network capex가 정상화

**당시 근거**

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

**이 주장이 성립하려면**

passings 완료 후 capex/revenue 하락

**사전 반증조건**

경쟁대응 투자 재가속

**실제 결과**

2022 EBITDA는 전년 대비 12.7% 감소하고 cash capex는 55% 증가했다. 2023 EBITDA는 약 $3.61bn, FCF는 약 $0.12bn으로 더 내려갔다. 저자가 직접 정의했던 EBITDA decline+financing pressure의 toxic mix가 현실화됐다.

**정량적 괴리**

2025 9x EV/EBITDA, debt paydown+buyback → 15~16% CAGR

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

CapEx normalization 가설은 '경쟁대응 투자 재가속'를 분기별 사전 반증조건으로 둔다.

#### 4. Deleveraging/Buyback — 실패 또는 부분 · 비중 16%

**당시 주장**

FCF가 debt와 share count를 개선

**당시 근거**

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

**이 주장이 성립하려면**

정상 FCF 유지·refinancing 원활

**사전 반증조건**

FCF 감소 속 leverage 고착

**실제 결과**

2022 EBITDA는 전년 대비 12.7% 감소하고 cash capex는 55% 증가했다. 2023 EBITDA는 약 $3.61bn, FCF는 약 $0.12bn으로 더 내려갔다. 저자가 직접 정의했던 EBITDA decline+financing pressure의 toxic mix가 현실화됐다.

**정량적 괴리**

2025 9x EV/EBITDA, debt paydown+buyback → 15~16% CAGR

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

Deleveraging/Buyback 가설은 'FCF 감소 속 leverage 고착'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 실패 또는 부분 · 비중 16%

**당시 주장**

사업이 2025 9x EV/EBITDA, debt paydown+buyback → 15~16% CAGR로 귀속

**당시 근거**

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업지표 대비 equity value 악화

**실제 결과**

$27.44→$2.44; -91.1%

**정량적 괴리**

$27.44→$2.44; -91.1%

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

주당가치 귀속 가설은 '사업지표 대비 equity value 악화'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 실패 또는 부분 · 비중 16%

**당시 주장**

경영진이 broadband customer growth 회복과 투자 확대를 최우선으로 발표가 thesis를 확인/반증

**당시 근거**

약 9x EV/EBITDA와 10~12% levered FCF yield에서 revenue 1% CAGR·EBITDA 2~3% CAGR, broadband ARPU 성장과 FTTH savings를 예상했다. 2020 net debt 약 $27bn, leverage 6.1x는 연 $1.5bn FCF로 2025년 4x까지 낮출 수 있다고 봤다. 금리상승과 EBITDA 하락이 동시에 오면 toxic mix라고 적었지만 EBITDA 하락 확률을 매우 낮게 뒀다.

**이 주장이 성립하려면**

반증 시 즉시 재평가

**사전 반증조건**

목표가만 기다리며 반증 무시

**실제 결과**

$27.44→$2.44; -91.1%

**정량적 괴리**

$27.44→$2.44; -91.1%

**분석 오류·핵심**

경쟁·CapEx·leverage의 joint distribution 과소평가

**재사용할 교훈**

촉매와 보유경로 가설은 '목표가만 기다리며 반증 무시'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2022 EBITDA는 전년 대비 12.7% 감소하고 cash capex는 55% 증가했다. 2023 EBITDA는 약 $3.61bn, FCF는 약 $0.12bn으로 더 내려갔다. 저자가 직접 정의했던 EBITDA decline+financing pressure의 toxic mix가 현실화됐다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $27.44→$2.44; -91.1%. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

위험을 몰랐던 게 아니라 확률배분을 틀렸다. 높은 leverage에서 EBITDA 10~20% 하락이 equity에 비선형적으로 미치는 영향을 충분히 stress하지 않았다.

#### 최초 검증·반증 신호와 회피 가능성

2021-11-04 — 경영진이 broadband customer growth 회복과 투자 확대를 최우선으로 발표. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

치명적 실패. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $27.44 | 15~16% CAGR | $2.44 | 치명적 실패 |
| EBITDA | 약 $4.4bn | 2~3% CAGR | 2023 $3.61bn | 실패 |
| FCF | 약 $1.5bn | deleveraging | 2023 $0.12bn | 실패 |
| Debt/interest | manageable | leverage 4x 방향 | 높은 debt·interest 부담 지속 | 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-08-11 | VIC 아이디어 게시 | 17% FCF yield·manageable debt·2025 compounding 롱 |
| 2021-11-04 | 경영진이 broadband customer growth 회복과 투자 확대를 최우선으로 발표 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2022 EBITDA는 전년 대비 12.7% 감소하고 cash capex는 55% 증가했다. 2023 EBITDA는 약 $3.61bn, FCF는 약 $0.12bn으로 더 내려갔다. 저자가 직접 정의했던 EBITDA decline+financing pressure의 toxic mix가 현실화됐다. |
| 2024-01-31 | 고정 평가기준일 | $27.44→$2.44; -91.1% |

### Failure / Success Anatomy

- **근본 오류:** 높은 leverage에서 EBITDA 안정성 확률을 과대평가
- **최초 검증·반증 신호:** 2021-11-04 — 경영진이 broadband customer growth 회복과 투자 확대를 최우선으로 발표
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 높음. 고객·CapEx·EBITDA가 동시에 악화될 때 debt stress를 재계산할 수 있었다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** broadband_mix; asset_value; fcf_yield
- **실패·주의 패턴:** leverage; buyback_at_wrong_state; capex_underestimate; competitive_overbuild; timing_path

### 주요 근거자료

- 1. VIC ALTICE USA 2021-08-11 원문 — Value Investors Club, 2021-08-11. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. Altice USA 2019 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828020001613/atus-20191231.htm) — SEC, 2020-02-13. 사업·수치·가격 사후검증
- [3. Altice USA 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828021001975/atus-20201231.htm) — SEC, 2021-02-11. 사업·수치·가격 사후검증
- [4. Altice USA 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828022002873/atus-20211231.htm) — SEC, 2022-02-16. 사업·수치·가격 사후검증
- [5. Altice USA FY2022 Results](https://www.sec.gov/Archives/edgar/data/1702780/000162828023004565/a2022q4exhibit991.htm) — Altice USA/SEC, 2023-02-22. 사업·수치·가격 사후검증
- [6. Altice USA 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1702780/000162828024004863/atus-20231231.htm) — SEC, 2024-02-14. 사업·수치·가격 사후검증
- [7. Altice USA historical prices](https://www.digrin.com/stocks/detail/ATUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

# T-MOBILE US (TMUS) — 기업과 비즈니스

## 1. 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

## 2. 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

## 3. 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격/사업 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2013-12-09 | Long | Long | Un-carrier 가격전쟁·고정비 레버리지 롱 | $26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23 | 전설적 성공 |
| 2015-04-06 | Short | Long | DISH/Sprint M&A 옵션+organic growth 롱 | $33→$67.42 by 2017-05; +104%. 2024-01 $161.23 | 매우 성공·촉매는 지연/변형 |
| 2017-05-19 | Long | Long | $5.20+ 2020 FCF/share·market share compounding 롱 | $67.42→약 $107 by 2020-07; 2024-01 $161.23 | 매우 성공 |
| 2018-09-07 | Long | Long | Sprint deal or standalone buyback 모두 가능한 50%+ 롱 | $70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23 | 전설적 성공 |
| 2020-07-14 | Long | Long | Sprint synergy·2.5GHz·fixed wireless 롱 | 약 $106→2024-01 $161.23 (+52%) | 매우 성공 |
| 2021-08-06 | Long | Long | Rural/enterprise share gain·spectrum moat·$171 DCF 롱 | 약 $141→$161.23 by 2024-01; +14% 내외 | 사업 적중·가격 부분 성공·장기 미판정 |
| 2022-07-12 | Long | Long | $15~20 FCF/share·대규모 capital return 롱 | 약 $135→$161.23 by 2024-01; +19% | 매우 성공·장기 FCF 일부 미판정 |

---

## 1. 2013-12-09 — Un-carrier 가격전쟁·고정비 레버리지 롱

### 결론부터

**종합판정: 전설적 성공.** 산업 자체를 좋은 산업으로 착각하지 않고 낮은 ROIC에서 시작해 경쟁사의 높은 ARPU·dividend 구조가 가격 대응을 어렵게 하는 비대칭과 fixed-cost operating leverage를 정확히 봤다.

**주가·증권 결과:** $26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 2016 bear/base/bull 약 $17.29/$31.22/$56.84. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

2014~15 branded postpaid net adds가 급증하고 churn이 하락했다. 2015 service revenue와 Adjusted EBITDA가 강하게 성장했으며 2017 말 주가는 약 $63.51로 high case를 넘어섰다.

**정량적 괴리**

2016 bear/base/bull 약 $17.29/$31.22/$56.84

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

2014~15 branded postpaid net adds가 급증하고 churn이 하락했다. 2015 service revenue와 Adjusted EBITDA가 강하게 성장했으며 2017 말 주가는 약 $63.51로 high case를 넘어섰다.

**정량적 괴리**

2016 bear/base/bull 약 $17.29/$31.22/$56.84

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

2014~15 branded postpaid net adds가 급증하고 churn이 하락했다. 2015 service revenue와 Adjusted EBITDA가 강하게 성장했으며 2017 말 주가는 약 $63.51로 high case를 넘어섰다.

**정량적 괴리**

2016 bear/base/bull 약 $17.29/$31.22/$56.84

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

2014~15 branded postpaid net adds가 급증하고 churn이 하락했다. 2015 service revenue와 Adjusted EBITDA가 강하게 성장했으며 2017 말 주가는 약 $63.51로 high case를 넘어섰다.

**정량적 괴리**

2016 bear/base/bull 약 $17.29/$31.22/$56.84

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 2016 bear/base/bull 약 $17.29/$31.22/$56.84로 귀속

**당시 근거**

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

$26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23

**정량적 괴리**

$26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

2014 net adds 급증과 churn 개선 확인가 thesis를 확인/반증

**당시 근거**

MetroPCS 합병 직후 $26.50의 TMUS를 3~4년 롱으로 봤다. 단말보조금 분리와 낮은 가격으로 share gain을 만들고, 무선망의 높은 고정비 특성 때문에 incremental subscriber가 EBITDA margin과 ROIC를 개선한다는 논리였다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

$26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23

**정량적 괴리**

$26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2014~15 branded postpaid net adds가 급증하고 churn이 하락했다. 2015 service revenue와 Adjusted EBITDA가 강하게 성장했으며 2017 말 주가는 약 $63.51로 high case를 넘어섰다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

산업 자체를 좋은 산업으로 착각하지 않고 낮은 ROIC에서 시작해 경쟁사의 높은 ARPU·dividend 구조가 가격 대응을 어렵게 하는 비대칭과 fixed-cost operating leverage를 정확히 봤다.

#### 최초 검증·반증 신호와 회피 가능성

2015-02-19 — 2014 net adds 급증과 churn 개선 확인. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

전설적 성공. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $26.50 | bull $56.84 | $63.51 2017-12 | 전설적 성공 |
| Churn | 2013 1.69% | 하락 | 2015 1.39% | 적중 |
| Postpaid net adds | 2013 2.0m | 큰 폭 증가 | 2014 4.9m; 2015 4.5m | 적중 |
| EBITDA | 낮은 규모 | operating leverage | 2015 +31.2% | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2013-12-09 | VIC 아이디어 게시 | Un-carrier 가격전쟁·고정비 레버리지 롱 |
| 2015-02-19 | 2014 net adds 급증과 churn 개선 확인 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2014~15 branded postpaid net adds가 급증하고 churn이 하락했다. 2015 service revenue와 Adjusted EBITDA가 강하게 성장했으며 2017 말 주가는 약 $63.51로 high case를 넘어섰다. |
| 2024-01-31 | 고정 평가기준일 | $26.50→$63.51 by 2017-12; +140%. 2024-01 $161.23 |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2015-02-19 — 2014 net adds 급증과 churn 개선 확인
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2013-12-09 원문 — Value Investors Club, 2013-12-09. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 2. 2015-04-06 — DISH/Sprint M&A 옵션+organic growth 롱

### 결론부터

**종합판정: 매우 성공·촉매는 지연/변형.** M&A를 유일 thesis가 아니라 standalone share gain 위의 option으로 둔 점이 좋았다. 특정 buyer와 timing을 지나치게 확신한 부분은 틀렸다.

**주가·증권 결과:** $33→$67.42 by 2017-05; +104%. 2024-01 $161.23

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 $45+; historical 7.7x EV/EBITDA ≈ $46. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

DISH 인수는 발생하지 않았으나 2015 사업은 강하게 성장했고 주가는 2016년 $45를 넘고 2017년 5월 약 $67.42까지 상승했다. Sprint 거래는 2018년 발표되어 2020년 종결됐다.

**정량적 괴리**

$45+; historical 7.7x EV/EBITDA ≈ $46

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

DISH 인수는 발생하지 않았으나 2015 사업은 강하게 성장했고 주가는 2016년 $45를 넘고 2017년 5월 약 $67.42까지 상승했다. Sprint 거래는 2018년 발표되어 2020년 종결됐다.

**정량적 괴리**

$45+; historical 7.7x EV/EBITDA ≈ $46

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

DISH 인수는 발생하지 않았으나 2015 사업은 강하게 성장했고 주가는 2016년 $45를 넘고 2017년 5월 약 $67.42까지 상승했다. Sprint 거래는 2018년 발표되어 2020년 종결됐다.

**정량적 괴리**

$45+; historical 7.7x EV/EBITDA ≈ $46

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

DISH 인수는 발생하지 않았으나 2015 사업은 강하게 성장했고 주가는 2016년 $45를 넘고 2017년 5월 약 $67.42까지 상승했다. Sprint 거래는 2018년 발표되어 2020년 종결됐다.

**정량적 괴리**

$45+; historical 7.7x EV/EBITDA ≈ $46

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 $45+; historical 7.7x EV/EBITDA ≈ $46로 귀속

**당시 근거**

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

$33→$67.42 by 2017-05; +104%. 2024-01 $161.23

**정량적 괴리**

$33→$67.42 by 2017-05; +104%. 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

M&A 없이도 2015 net adds·EBITDA 강세 확인가 thesis를 확인/반증

**당시 근거**

원 SQL은 Short지만 본문 첫 문장은 Buy TMUS다. 약 $33에서 organic growth와 전략적 M&A를 합쳐 $45+를 제시했다. DISH가 spectrum 활용을 위해 인수할 가능성을 높게 봤지만 standalone Un-carrier·network 개선도 중요한 하방방어였다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

$33→$67.42 by 2017-05; +104%. 2024-01 $161.23

**정량적 괴리**

$33→$67.42 by 2017-05; +104%. 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

DISH 인수는 발생하지 않았으나 2015 사업은 강하게 성장했고 주가는 2016년 $45를 넘고 2017년 5월 약 $67.42까지 상승했다. Sprint 거래는 2018년 발표되어 2020년 종결됐다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $33→$67.42 by 2017-05; +104%. 2024-01 $161.23. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

M&A를 유일 thesis가 아니라 standalone share gain 위의 option으로 둔 점이 좋았다. 특정 buyer와 timing을 지나치게 확신한 부분은 틀렸다.

#### 최초 검증·반증 신호와 회피 가능성

2016-02-17 — M&A 없이도 2015 net adds·EBITDA 강세 확인. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

매우 성공·촉매는 지연/변형. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $33 | $45+ | $67.42 2017-05 | 성공 |
| Net adds | 강한 성장 기대 | 지속 | 2015 8.3m total | 적중 |
| EBITDA | 성장 기대 | operating leverage | 2015 +31.2% | 적중 |
| M&A | DISH/Sprint 가능 | DISH 우선 | DISH 불발; Sprint 후일 성사 | 촉매 변형 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2015-04-06 | VIC 아이디어 게시 | DISH/Sprint M&A 옵션+organic growth 롱 |
| 2016-02-17 | M&A 없이도 2015 net adds·EBITDA 강세 확인 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | DISH 인수는 발생하지 않았으나 2015 사업은 강하게 성장했고 주가는 2016년 $45를 넘고 2017년 5월 약 $67.42까지 상승했다. Sprint 거래는 2018년 발표되어 2020년 종결됐다. |
| 2024-01-31 | 고정 평가기준일 | $33→$67.42 by 2017-05; +104%. 2024-01 $161.23 |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2016-02-17 — M&A 없이도 2015 net adds·EBITDA 강세 확인
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2015-04-06 원문 — Value Investors Club, 2015-04-06. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 3. 2017-05-19 — $5.20+ 2020 FCF/share·market share compounding 롱

### 결론부터

**종합판정: 매우 성공.** M&A 없이 standalone FCF/share로 먼저 가치를 만든 점과 incumbent의 ARPU·dividend 구조가 가격대응을 제한한다는 분석이 강했다. cable wireless 위협은 다소 과소평가했다.

**주가·증권 결과:** $67.42→약 $107 by 2020-07; 2024-01 $161.23

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 2020 FCF/share $5.20+ ×20 = $104+. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

2017년에도 record customer growth와 EBITDA 확대가 이어졌고 Sprint 합병이 추가 upside를 만들었다. 2020년 중 $104 목표를 달성했다.

**정량적 괴리**

2020 FCF/share $5.20+ ×20 = $104+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

2017년에도 record customer growth와 EBITDA 확대가 이어졌고 Sprint 합병이 추가 upside를 만들었다. 2020년 중 $104 목표를 달성했다.

**정량적 괴리**

2020 FCF/share $5.20+ ×20 = $104+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

2017년에도 record customer growth와 EBITDA 확대가 이어졌고 Sprint 합병이 추가 upside를 만들었다. 2020년 중 $104 목표를 달성했다.

**정량적 괴리**

2020 FCF/share $5.20+ ×20 = $104+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

2017년에도 record customer growth와 EBITDA 확대가 이어졌고 Sprint 합병이 추가 upside를 만들었다. 2020년 중 $104 목표를 달성했다.

**정량적 괴리**

2020 FCF/share $5.20+ ×20 = $104+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 2020 FCF/share $5.20+ ×20 = $104+로 귀속

**당시 근거**

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

$67.42→약 $107 by 2020-07; 2024-01 $161.23

**정량적 괴리**

$67.42→약 $107 by 2020-07; 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

2017 customer growth·FCF·600MHz deployment 동시 확인가 thesis를 확인/반증

**당시 근거**

TMUS를 levered FCF growth로 정의하고 2020 FCF/share $5.20+에 20x를 적용해 $104+를 제시했다. network quality, 저가 subscription, Un-carrier, 600MHz spectrum이 share gain을 지속시킨다고 봤다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

$67.42→약 $107 by 2020-07; 2024-01 $161.23

**정량적 괴리**

$67.42→약 $107 by 2020-07; 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2017년에도 record customer growth와 EBITDA 확대가 이어졌고 Sprint 합병이 추가 upside를 만들었다. 2020년 중 $104 목표를 달성했다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $67.42→약 $107 by 2020-07; 2024-01 $161.23. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

M&A 없이 standalone FCF/share로 먼저 가치를 만든 점과 incumbent의 ARPU·dividend 구조가 가격대응을 제한한다는 분석이 강했다. cable wireless 위협은 다소 과소평가했다.

#### 최초 검증·반증 신호와 회피 가능성

2018-04-27 — 2017 customer growth·FCF·600MHz deployment 동시 확인. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

매우 성공. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $67.42 | $104+ | 약 $107 2020-07 | 성공 |
| Net adds | share gain 지속 | 업계 선도 | 2017 5.7m | 적중 |
| Service revenue | 성장 | 지속 | 2017 +8.3% | 적중 |
| EBITDA | scale leverage | 증가 | 2017 $11.2bn | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2017-05-19 | VIC 아이디어 게시 | $5.20+ 2020 FCF/share·market share compounding 롱 |
| 2018-04-27 | 2017 customer growth·FCF·600MHz deployment 동시 확인 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2017년에도 record customer growth와 EBITDA 확대가 이어졌고 Sprint 합병이 추가 upside를 만들었다. 2020년 중 $104 목표를 달성했다. |
| 2024-01-31 | 고정 평가기준일 | $67.42→약 $107 by 2020-07; 2024-01 $161.23 |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2018-04-27 — 2017 customer growth·FCF·600MHz deployment 동시 확인
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2017-05-19 원문 — Value Investors Club, 2017-05-19. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 4. 2018-09-07 — Sprint deal or standalone buyback 모두 가능한 50%+ 롱

### 결론부터

**종합판정: 전설적 성공.** M&A 승인확률 하나에 베팅하지 않고 deal/no-deal 두 상태 모두의 equity value를 모델링한 것이 탁월했다. churn×gross-add share로 terminal share를 생각한 프레임도 강했다.

**주가·증권 결과:** $70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 standalone 50%+ upside; deal case $95~130+; $6bn synergy. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

Sprint 합병은 2020년 종결됐고 run-rate synergy는 이후 $7.5bn으로 상향됐다. 2.5GHz가 5G mid-band의 핵심이 됐으며 주가는 2020년 말 약 $134.85까지 상승했다.

**정량적 괴리**

standalone 50%+ upside; deal case $95~130+; $6bn synergy

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

Sprint 합병은 2020년 종결됐고 run-rate synergy는 이후 $7.5bn으로 상향됐다. 2.5GHz가 5G mid-band의 핵심이 됐으며 주가는 2020년 말 약 $134.85까지 상승했다.

**정량적 괴리**

standalone 50%+ upside; deal case $95~130+; $6bn synergy

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

Sprint 합병은 2020년 종결됐고 run-rate synergy는 이후 $7.5bn으로 상향됐다. 2.5GHz가 5G mid-band의 핵심이 됐으며 주가는 2020년 말 약 $134.85까지 상승했다.

**정량적 괴리**

standalone 50%+ upside; deal case $95~130+; $6bn synergy

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

Sprint 합병은 2020년 종결됐고 run-rate synergy는 이후 $7.5bn으로 상향됐다. 2.5GHz가 5G mid-band의 핵심이 됐으며 주가는 2020년 말 약 $134.85까지 상승했다.

**정량적 괴리**

standalone 50%+ upside; deal case $95~130+; $6bn synergy

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 standalone 50%+ upside; deal case $95~130+; $6bn synergy로 귀속

**당시 근거**

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

$70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23

**정량적 괴리**

$70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

Sprint merger 종결가 thesis를 확인/반증

**당시 근거**

Sprint deal이 닫히면 $6bn synergy와 2.5GHz, 4→3 consolidation이 upside를 만들고 deal이 깨져도 $9bn buyback과 standalone 20% earnings algorithm이 하방을 지지한다고 봤다. postpaid share보다 gross adds와 churn을 통해 equilibrium share를 계산했다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

$70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23

**정량적 괴리**

$70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

Sprint 합병은 2020년 종결됐고 run-rate synergy는 이후 $7.5bn으로 상향됐다. 2.5GHz가 5G mid-band의 핵심이 됐으며 주가는 2020년 말 약 $134.85까지 상승했다.

#### 사업 결과와 가격 결과 분리

가격 결과는 $70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

M&A 승인확률 하나에 베팅하지 않고 deal/no-deal 두 상태 모두의 equity value를 모델링한 것이 탁월했다. churn×gross-add share로 terminal share를 생각한 프레임도 강했다.

#### 최초 검증·반증 신호와 회피 가능성

2020-04-01 — Sprint merger 종결. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

전설적 성공. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $70.18 | 50%+ | $134.85 2020-12 | 전설적 성공 |
| Synergy | $6bn | upside 가능 | $7.5bn run-rate | 강한 적중 |
| Postpaid share | 16~17% | 20%대 equilibrium | share gain 지속 | 적중 |
| 2.5GHz | deal option | network missing piece | 5G 핵심 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-09-07 | VIC 아이디어 게시 | Sprint deal or standalone buyback 모두 가능한 50%+ 롱 |
| 2020-04-01 | Sprint merger 종결 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | Sprint 합병은 2020년 종결됐고 run-rate synergy는 이후 $7.5bn으로 상향됐다. 2.5GHz가 5G mid-band의 핵심이 됐으며 주가는 2020년 말 약 $134.85까지 상승했다. |
| 2024-01-31 | 고정 평가기준일 | $70.18→$134.85 by 2020-12; +92%. 2024-01 $161.23 |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2020-04-01 — Sprint merger 종결
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2018-09-07 원문 — Value Investors Club, 2018-09-07. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 5. 2020-07-14 — Sprint synergy·2.5GHz·fixed wireless 롱

### 결론부터

**종합판정: 매우 성공.** M&A synergy를 tower decommission·avoided sites·SG&A처럼 물리적으로 검증 가능한 비용으로 분해하고 spectrum을 capacity·coverage·신사업 economics로 연결한 것이 강했다.

**주가·증권 결과:** 약 $106→2024-01 $161.23 (+52%)

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 $30bn PF EBITDA ×7~8x → $120~145; downside 약 $85. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

synergy run-rate는 $7.5bn으로 상향됐고 2023 Core Adjusted EBITDA 약 $29.1bn, FCF 약 $13.6bn을 기록했다. postpaid net adds와 churn이 강했고 HSI 고객은 약 4.8m으로 성장했다.

**정량적 괴리**

$30bn PF EBITDA ×7~8x → $120~145; downside 약 $85

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

synergy run-rate는 $7.5bn으로 상향됐고 2023 Core Adjusted EBITDA 약 $29.1bn, FCF 약 $13.6bn을 기록했다. postpaid net adds와 churn이 강했고 HSI 고객은 약 4.8m으로 성장했다.

**정량적 괴리**

$30bn PF EBITDA ×7~8x → $120~145; downside 약 $85

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

synergy run-rate는 $7.5bn으로 상향됐고 2023 Core Adjusted EBITDA 약 $29.1bn, FCF 약 $13.6bn을 기록했다. postpaid net adds와 churn이 강했고 HSI 고객은 약 4.8m으로 성장했다.

**정량적 괴리**

$30bn PF EBITDA ×7~8x → $120~145; downside 약 $85

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

synergy run-rate는 $7.5bn으로 상향됐고 2023 Core Adjusted EBITDA 약 $29.1bn, FCF 약 $13.6bn을 기록했다. postpaid net adds와 churn이 강했고 HSI 고객은 약 4.8m으로 성장했다.

**정량적 괴리**

$30bn PF EBITDA ×7~8x → $120~145; downside 약 $85

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 $30bn PF EBITDA ×7~8x → $120~145; downside 약 $85로 귀속

**당시 근거**

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

약 $106→2024-01 $161.23 (+52%)

**정량적 괴리**

약 $106→2024-01 $161.23 (+52%)

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

synergy NPV $43bn→$70bn+, run-rate $6bn→$7.5bn 상향가 thesis를 확인/반증

**당시 근거**

Sprint 합병 직후 combined 2019 EBITDA 약 $23.3bn에 $6bn+ cost synergy를 더해 약 $30bn EBITDA를 예상했다. 중복망 폐쇄의 물리적 cost synergy, 600MHz+2.5GHz spectrum, fixed wireless option을 핵심으로 봤다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

약 $106→2024-01 $161.23 (+52%)

**정량적 괴리**

약 $106→2024-01 $161.23 (+52%)

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

synergy run-rate는 $7.5bn으로 상향됐고 2023 Core Adjusted EBITDA 약 $29.1bn, FCF 약 $13.6bn을 기록했다. postpaid net adds와 churn이 강했고 HSI 고객은 약 4.8m으로 성장했다.

#### 사업 결과와 가격 결과 분리

가격 결과는 약 $106→2024-01 $161.23 (+52%). 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

M&A synergy를 tower decommission·avoided sites·SG&A처럼 물리적으로 검증 가능한 비용으로 분해하고 spectrum을 capacity·coverage·신사업 economics로 연결한 것이 강했다.

#### 최초 검증·반증 신호와 회피 가능성

2021-03-11 — synergy NPV $43bn→$70bn+, run-rate $6bn→$7.5bn 상향. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

매우 성공. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | 약 $106 | $120~145 | $161.23 | 성공 |
| Core EBITDA | $23.3bn base | $30bn | 2023 $29.1bn | 적중 |
| Synergy | $6bn | 더 크고 빠름 | $7.5bn | 강한 적중 |
| HSI customers | option | 유의미한 신사업 | 2023 4.8m | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-07-14 | VIC 아이디어 게시 | Sprint synergy·2.5GHz·fixed wireless 롱 |
| 2021-03-11 | synergy NPV $43bn→$70bn+, run-rate $6bn→$7.5bn 상향 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | synergy run-rate는 $7.5bn으로 상향됐고 2023 Core Adjusted EBITDA 약 $29.1bn, FCF 약 $13.6bn을 기록했다. postpaid net adds와 churn이 강했고 HSI 고객은 약 4.8m으로 성장했다. |
| 2024-01-31 | 고정 평가기준일 | 약 $106→2024-01 $161.23 (+52%) |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2021-03-11 — synergy NPV $43bn→$70bn+, run-rate $6bn→$7.5bn 상향
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2020-07-14 원문 — Value Investors Club, 2020-07-14. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 6. 2021-08-06 — Rural/enterprise share gain·spectrum moat·$171 DCF 롱

### 결론부터

**종합판정: 사업 적중·가격 부분 성공·장기 미판정.** spectrum, customer cohorts, rural/enterprise TAM, FWA, synergy와 buyback을 하나의 FCF/share 모델로 연결한 프로세스가 강하다. 장기 buyback 가격 가정은 path-dependent하다.

**주가·증권 결과:** 약 $141→$161.23 by 2024-01; +14% 내외

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 DCF $171; 5년 IRR 15%; 2026 FCF $20.9bn / $21.9 per share. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

2023 postpaid net adds 5.7m, phone churn 0.87%, HSI customers 4.8m을 기록했고 대규모 shareholder-return 프로그램이 시작됐다. 다만 5년 horizon과 2026 FCF/share는 2024-01 기준 미도래다.

**정량적 괴리**

DCF $171; 5년 IRR 15%; 2026 FCF $20.9bn / $21.9 per share

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

2023 postpaid net adds 5.7m, phone churn 0.87%, HSI customers 4.8m을 기록했고 대규모 shareholder-return 프로그램이 시작됐다. 다만 5년 horizon과 2026 FCF/share는 2024-01 기준 미도래다.

**정량적 괴리**

DCF $171; 5년 IRR 15%; 2026 FCF $20.9bn / $21.9 per share

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

2023 postpaid net adds 5.7m, phone churn 0.87%, HSI customers 4.8m을 기록했고 대규모 shareholder-return 프로그램이 시작됐다. 다만 5년 horizon과 2026 FCF/share는 2024-01 기준 미도래다.

**정량적 괴리**

DCF $171; 5년 IRR 15%; 2026 FCF $20.9bn / $21.9 per share

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

2023 postpaid net adds 5.7m, phone churn 0.87%, HSI customers 4.8m을 기록했고 대규모 shareholder-return 프로그램이 시작됐다. 다만 5년 horizon과 2026 FCF/share는 2024-01 기준 미도래다.

**정량적 괴리**

DCF $171; 5년 IRR 15%; 2026 FCF $20.9bn / $21.9 per share

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 DCF $171; 5년 IRR 15%; 2026 FCF $20.9bn / $21.9 per share로 귀속

**당시 근거**

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

약 $141→$161.23 by 2024-01; +14% 내외

**정량적 괴리**

약 $141→$161.23 by 2024-01; +14% 내외

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

$14bn share repurchase authorization가 thesis를 확인/반증

**당시 근거**

rural·enterprise의 낮은 점유율을 growth pool로 보고 spectrum 우위, $7.5bn synergy, fixed wireless, 향후 buyback을 FCF/share 모델로 연결했다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

약 $141→$161.23 by 2024-01; +14% 내외

**정량적 괴리**

약 $141→$161.23 by 2024-01; +14% 내외

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2023 postpaid net adds 5.7m, phone churn 0.87%, HSI customers 4.8m을 기록했고 대규모 shareholder-return 프로그램이 시작됐다. 다만 5년 horizon과 2026 FCF/share는 2024-01 기준 미도래다.

#### 사업 결과와 가격 결과 분리

가격 결과는 약 $141→$161.23 by 2024-01; +14% 내외. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

spectrum, customer cohorts, rural/enterprise TAM, FWA, synergy와 buyback을 하나의 FCF/share 모델로 연결한 프로세스가 강하다. 장기 buyback 가격 가정은 path-dependent하다.

#### 최초 검증·반증 신호와 회피 가능성

2022-09-08 — $14bn share repurchase authorization. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

사업 적중·가격 부분 성공·장기 미판정. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | 약 $141 | $171 | $161.23 | 부분 성공 |
| 2026 FCF | $20.9bn | 성장 | 2023 $13.6bn; horizon 미도래 | 진행중 |
| HSI | 초기 rollout | 고성장 | 2023 4.8m | 초과 |
| Capital return | 대규모 buyback | 주식수 축소 | $14bn+추가 프로그램 | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-08-06 | VIC 아이디어 게시 | Rural/enterprise share gain·spectrum moat·$171 DCF 롱 |
| 2022-09-08 | $14bn share repurchase authorization | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2023 postpaid net adds 5.7m, phone churn 0.87%, HSI customers 4.8m을 기록했고 대규모 shareholder-return 프로그램이 시작됐다. 다만 5년 horizon과 2026 FCF/share는 2024-01 기준 미도래다. |
| 2024-01-31 | 고정 평가기준일 | 약 $141→$161.23 by 2024-01; +14% 내외 |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2022-09-08 — $14bn share repurchase authorization
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2021-08-06 원문 — Value Investors Club, 2021-08-06. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

## 7. 2022-07-12 — $15~20 FCF/share·대규모 capital return 롱

### 결론부터

**종합판정: 매우 성공·장기 FCF 일부 미판정.** 이미 입증된 Sprint synergy에서 다음 단계인 cash conversion→buyback→share count로 thesis를 정확히 업데이트했다. $60bn 전체를 단기간 free-float squeeze로 환산한 부분은 공격적이었다.

**주가·증권 결과:** 약 $135→$161.23 by 2024-01; +19%

**Thesis / Process 점수:** 9 / 8.8

### 기업·산업 이해

#### 무슨 기업인가

T-Mobile US는 미국 전국 단위 무선통신 사업자다. 무선망은 spectrum·기지국·백홀에 선투자하고 여유용량에 추가 고객을 태울 때 증분마진이 높은 고정비 산업이다. Un-carrier 이후 가입자와 churn이 개선됐고 Sprint 인수 후 2.5GHz 중대역과 중복망 제거가 network quality·cost synergy·FCF를 동시에 바꿨다. 핵심 지표는 postpaid net adds, churn, ARPA/ARPU, spectrum·CapEx, EBITDA, FCF와 share count다.

#### 산업 가치사슬과 돈의 흐름

소비자 서비스료에서 tower·backhaul·network·sales·device subsidy 비용을 차감한다. 이미 구축된 망의 여유 capacity에 고객을 추가하면 높은 incremental contribution이 생기지만 트래픽이 추가 spectrum·sites를 요구하면 약해진다. Sprint 이후 중복 tower·backhaul·IT·retail 폐쇄가 물리적 synergy를 만들었다.

#### 경쟁우위·경쟁구도·핵심 지표

가격·브랜드·distribution·spectrum·network execution의 결합이 경쟁우위다. Verizon·AT&T는 기존 대규모 base에 같은 가격인하를 적용하면 EBITDA 훼손이 커 T-Mobile의 가격에 완전히 대응하기 어렵다는 비대칭이 있었다. Sprint 2.5GHz 이후에는 network quality가 churn·net adds·FWA로 연결되는지 검증해야 한다.

### 당시 VIC 투자논지와 밸류에이션

#### 당시 VIC 원문과 핵심 숫자

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

#### 밸류에이션과 기대수익의 연결

원 valuation bridge는 $15~20 FCF/share ÷ 8~10% yield → $150~200+. 가입자/ARPU→EBITDA→cash CapEx·interest→FCF→net debt·share count 순으로 equity value를 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Share gain·churn — 적중 · 비중 18%

**당시 주장**

가격·network 우위가 net adds/churn 개선

**당시 근거**

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

**이 주장이 성립하려면**

net adds 우위·churn 하락

**사전 반증조건**

gross adds 둔화·churn 상승

**실제 결과**

2022년 $14bn repurchase program, 2023년 추가 shareholder-return program이 승인됐고 2023 FCF는 약 $13.6bn으로 가이던스 상단을 달성했다. 2024-01 주가는 약 $161.23으로 18개월 목표 하단을 달성했다.

**정량적 괴리**

$15~20 FCF/share ÷ 8~10% yield → $150~200+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Share gain·churn 가설은 'gross adds 둔화·churn 상승'를 분기별 사전 반증조건으로 둔다.

#### 2. Spectrum/network — 적중 · 비중 18%

**당시 주장**

spectrum 투자가 quality·capacity로 수익화

**당시 근거**

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

**이 주장이 성립하려면**

deployment가 coverage/speed로 연결

**사전 반증조건**

경쟁사 parity·capex 폭증

**실제 결과**

2022년 $14bn repurchase program, 2023년 추가 shareholder-return program이 승인됐고 2023 FCF는 약 $13.6bn으로 가이던스 상단을 달성했다. 2024-01 주가는 약 $161.23으로 18개월 목표 하단을 달성했다.

**정량적 괴리**

$15~20 FCF/share ÷ 8~10% yield → $150~200+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Spectrum/network 가설은 '경쟁사 parity·capex 폭증'를 분기별 사전 반증조건으로 둔다.

#### 3. Fixed-cost leverage — 적중 · 비중 16%

**당시 주장**

share gain이 EBITDA/FCF로 연결

**당시 근거**

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

**이 주장이 성립하려면**

증분비용이 매출보다 느림

**사전 반증조건**

성장만큼 network cost 증가

**실제 결과**

2022년 $14bn repurchase program, 2023년 추가 shareholder-return program이 승인됐고 2023 FCF는 약 $13.6bn으로 가이던스 상단을 달성했다. 2024-01 주가는 약 $161.23으로 18개월 목표 하단을 달성했다.

**정량적 괴리**

$15~20 FCF/share ÷ 8~10% yield → $150~200+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Fixed-cost leverage 가설은 '성장만큼 network cost 증가'를 분기별 사전 반증조건으로 둔다.

#### 4. Capital allocation — 적중 · 비중 16%

**당시 주장**

FCF가 buyback/debt에 합리적으로 배분

**당시 근거**

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

**이 주장이 성립하려면**

적정가격 매입·balance sheet 유지

**사전 반증조건**

고가 buyback·debt 악화

**실제 결과**

2022년 $14bn repurchase program, 2023년 추가 shareholder-return program이 승인됐고 2023 FCF는 약 $13.6bn으로 가이던스 상단을 달성했다. 2024-01 주가는 약 $161.23으로 18개월 목표 하단을 달성했다.

**정량적 괴리**

$15~20 FCF/share ÷ 8~10% yield → $150~200+

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

Capital allocation 가설은 '고가 buyback·debt 악화'를 분기별 사전 반증조건으로 둔다.

#### 5. 주당가치 귀속 — 적중 · 비중 16%

**당시 주장**

사업이 $15~20 FCF/share ÷ 8~10% yield → $150~200+로 귀속

**당시 근거**

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

**이 주장이 성립하려면**

FCF/share 증가

**사전 반증조건**

사업성장에도 share value 정체

**실제 결과**

약 $135→$161.23 by 2024-01; +19%

**정량적 괴리**

약 $135→$161.23 by 2024-01; +19%

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

주당가치 귀속 가설은 '사업성장에도 share value 정체'를 분기별 사전 반증조건으로 둔다.

#### 6. 촉매와 보유경로 — 적중 또는 진행중 · 비중 16%

**당시 주장**

$14bn stock repurchase program 승인가 thesis를 확인/반증

**당시 근거**

Sprint integration 종료로 2022 $7.2~7.6bn FCF가 2023 $13~14bn, 2024 $17bn+으로 증가할 것으로 보고 $15~20 FCF/share와 대규모 capital return을 핵심 촉매로 제시했다.

**이 주장이 성립하려면**

촉매가 합리적 기간 내 발생

**사전 반증조건**

M&A/timing 오판이 thesis 전체를 지배

**실제 결과**

약 $135→$161.23 by 2024-01; +19%

**정량적 괴리**

약 $135→$161.23 by 2024-01; +19%

**분석 오류·핵심**

중대한 핵심 오류 없음; path-dependent 가정은 별도 관리

**재사용할 교훈**

촉매와 보유경로 가설은 'M&A/timing 오판이 thesis 전체를 지배'를 분기별 사전 반증조건으로 둔다.

### 실제 사업 전개와 가격 결과

#### 실제 사업의 시간순 전개

2022년 $14bn repurchase program, 2023년 추가 shareholder-return program이 승인됐고 2023 FCF는 약 $13.6bn으로 가이던스 상단을 달성했다. 2024-01 주가는 약 $161.23으로 18개월 목표 하단을 달성했다.

#### 사업 결과와 가격 결과 분리

가격 결과는 약 $135→$161.23 by 2024-01; +19%. 사업·촉매·valuation·capital structure·가격을 서로 다른 판정으로 저장한다.

#### 무엇을 잘 봤고 무엇을 놓쳤나

이미 입증된 Sprint synergy에서 다음 단계인 cash conversion→buyback→share count로 thesis를 정확히 업데이트했다. $60bn 전체를 단기간 free-float squeeze로 환산한 부분은 공격적이었다.

#### 최초 검증·반증 신호와 회피 가능성

2022-09-08 — $14bn stock repurchase program 승인. 이 시점에 고객·EBITDA·CapEx·debt·FCF/share를 재계산했어야 한다.

#### 최종 판정·반사실·재사용 교훈

매우 성공·장기 FCF 일부 미판정. 동일 산업에서 operating leverage와 capital structure를 항상 joint stress한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | 약 $135 | $150~200+ | $161.23 | 성공 |
| 2023 FCF | $13~14bn | inflection | $13.6bn | 적중 |
| Buyback | $60bn+ 장기구상 | 시작 | $14bn+후속 프로그램 | 적중 |
| HSI net adds | growth engine | 업계 선도 | 2023 2.1m | 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2022-07-12 | VIC 아이디어 게시 | $15~20 FCF/share·대규모 capital return 롱 |
| 2022-09-08 | $14bn stock repurchase program 승인 | 최초 핵심 검증·반증 신호 |
| 2021-12-31 | 중간 사업·자본구조 점검 | 고객·margin·CapEx·debt·share count 재검증 |
| 2022-12-31 | 금리·경쟁·capital allocation 점검 | 높은 leverage 또는 buyback의 equity 효과 확인 |
| 2023-12-31 | FY2023 사업상태 | 2022년 $14bn repurchase program, 2023년 추가 shareholder-return program이 승인됐고 2023 FCF는 약 $13.6bn으로 가이던스 상단을 달성했다. 2024-01 주가는 약 $161.23으로 18개월 목표 하단을 달성했다. |
| 2024-01-31 | 고정 평가기준일 | 약 $135→$161.23 by 2024-01; +19% |

### Failure / Success Anatomy

- **근본 오류:** 사업·spectrum·synergy를 FCF/share로 연결하면서 path-dependent 가정을 별도 관리
- **최초 검증·반증 신호:** 2022-09-08 — $14bn stock repurchase program 승인
- **당시 알 수 있었나:** 고객 순증·churn·ARPU·spectrum/FTTH·cash capex·net debt·interest·share count는 공개자료로 분기별 검증 가능
- **피할 수 있었나:** 중간. 핵심 thesis는 맞았지만 M&A 상대·timing과 buyback 가격은 별도 확률 관리가 필요했다.
- **반사실 질문:** 핵심 operating variable이 반대 방향으로 움직였다면 원 valuation이 유지되는가?
- **성공 패턴:** fixed_cost_operating_leverage; spectrum_capacity; physical_synergy; fcf_per_share; capital_return
- **실패·주의 패턴:** m_and_a_timing; competition_underestimate; multiple_path

### 주요 근거자료

- 1. VIC T-MOBILE US 2022-07-12 원문 — Value Investors Club, 2022-07-12. 원 SQL 설명문에서 당시 주장·수치·방향·촉매 보존
- [2. T-Mobile 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369915000010/tmus12312014form10-k.htm) — SEC, 2015-02-19. 사업·수치·가격 사후검증
- [3. T-Mobile 2015 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369916000073/tmus12312015form10-k.htm) — SEC, 2016-02-17. 사업·수치·가격 사후검증
- [4. T-Mobile 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369919000015/tmus12312018form10-k.htm) — SEC, 2019-02-07. 사업·수치·가격 사후검증
- [5. T-Mobile Q1 2021 Results and Merger Synergy Update](https://www.sec.gov/Archives/edgar/data/1283699/000128369921000087/ng_tmus03312021ex991.htm) — T-Mobile/SEC, 2021-05-04. 사업·수치·가격 사후검증
- [6. T-Mobile 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369923000016/tmus-20221231.htm) — SEC, 2023-02-14. 사업·수치·가격 사후검증
- [7. T-Mobile FY2023 Results](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000004/tmus12312023ex991.htm) — T-Mobile/SEC, 2024-01-25. 사업·수치·가격 사후검증
- [8. T-Mobile 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1283699/000128369924000008/tmus-20231231.htm) — SEC, 2024-02-02. 사업·수치·가격 사후검증
- [9. T-Mobile historical prices](https://www.digrin.com/stocks/detail/TMUS/price) — Digrin, 2024-01-31. 사업·수치·가격 사후검증


---

# 배치 공통 학습

- **고정비 산업의 operating leverage는 양방향이다.** 고객이 늘면 margin과 FCF가 빠르게 좋아지지만, 고객이 줄면 같은 구조가 역으로 작동한다.
- **레버리지 기업에서는 EBITDA 안정성의 확률분포가 valuation보다 중요할 수 있다.** 높은 FCF yield가 보여도 debt가 크면 EBITDA 10~20% 하락이 equity를 비선형적으로 훼손한다.
- **물리적 synergy가 가장 검증 가능하다.** TMUS의 tower decommission·spectrum consolidation처럼 비용이 실제로 사라지는 구조는 추상적 cross-sell보다 신뢰도가 높다.
- **자사주 매입은 사업이 좋아진 뒤의 귀속 수단이어야 한다.** ATUS처럼 사업 안정성을 전제로 한 levered buyback은 downside를 키울 수 있다.
