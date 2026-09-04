# Batch 014 — T-Mobile US·Altice USA 10건

평가기준일: 2024-01-31

분석일: 2026-09-04

대상: T-Mobile US 7건·Altice USA 3건

## 결론부터

이번 배치는 **같은 통신 인프라·고정비 산업에서 운영 레버리지가 어떻게 equity에 정반대로 작동하는지**를 보여준다.

- **TMUS:** 낮은 가격과 Un-carrier가 net adds를 만들고, network·spectrum 투자로 churn이 내려간 뒤, Sprint의 2.5GHz와 중복망 제거가 EBITDA·FCF를 키웠다. 이후 buyback은 이미 개선된 FCF를 주당가치로 옮기는 마지막 단계였다.
- **ATUS:** broadband의 높은 margin과 cost cutting은 맞았지만, 고레버리지 상태에서 customer base와 EBITDA가 약해질 가능성을 낮게 봤다. 사업 안정성을 전제로 한 levered buyback은 EBITDA가 하락하자 equity cushion을 크게 훼손했다.

| 기업 | 건수 | 가장 강한 성공 | 가장 큰 실패 | 반복 학습 |
|---|---:|---|---|---|
| T-Mobile US | 7 | 2013 Un-carrier, 2018/2020 Sprint·spectrum | 특정 M&A 상대·timing 일부 오판 | 고정비 share gain을 churn→margin→FCF/share로 연결 |
| Altice USA | 3 | broadband/video margin 분해 자체 | 2019·2021 levered FCF/buyback 롱 | 높은 leverage에서는 EBITDA 안정성 확률이 핵심 변수 |

> 데이터 경고: 2015-04-06 TMUS 아이디어는 원 SQL `is_short=true`지만 본문 첫 문장이 **Buy TMUS**이고 전체 기대수익·촉매도 Long이다. 원본 flag는 감사추적용으로 보존하고 분석 방향은 Long으로 교정한다.

---

# Altice USA (ATUS) — 기업과 비즈니스

## 1. 무슨 기업인가

Altice USA는 Optimum과 과거 Suddenlink 지역에서 케이블 기반 broadband, video, voice, mobile 및 기업용 통신서비스를 제공하는 미국 유선통신 사업자다. 핵심 자산은 지역별 HFC·FTTH 망과 고객관계이며, broadband는 programming cost가 거의 없어 video보다 훨씬 높은 증분마진을 낼 수 있다. 그러나 이 기업의 주주경제성은 단순 broadband ARPU 성장보다 복잡하다. 높은 부채를 전제로 Cablevision·Suddenlink를 인수했고, 운영효율화 뒤에도 5x 안팎의 레버리지를 유지하면서 대규모 자사주 매입을 수행했다. 따라서 EBITDA가 조금만 하락하거나 CapEx·이자비용이 예상보다 높아져도 equity FCF가 급격히 압축되는 구조였다. 2017~2020년에는 cost cutting, broadband mix 개선, Lightpath 가치, levered buyback이 강한 주가상승 논리를 만들었지만, 2021년 이후 broadband 고객이 감소하고 fiber 투자와 경쟁비용이 커지면서 EBITDA·FCF가 하락했다. 높은 레버리지는 이 사업 악화를 equity에 증폭시켰다. 핵심 지표는 broadband customer relationships와 net adds, broadband ARPU, passings·FTTH penetration, Adjusted EBITDA margin, cash CapEx, FCF, net debt·interest expense, 자사주 평균매입가격과 주식수다.

## 2. 산업 가치사슬과 돈의 흐름

케이블 broadband 한 고객의 월 요금에서 Altice는 지역망·고객서비스·판매·장비·전력·maintenance 비용을 부담한다. video는 여기에 방송사·스포츠 채널 programming fee가 크게 추가되므로 매출 비중에 비해 EBITDA·FCF 기여가 낮다. broadband는 programming cost가 없고 이미 깔린 망에서 속도 tier를 올릴 때 증분비용이 제한적이어서 높은 margin이 가능하다. 문제는 경쟁의 단위가 지역별이라는 점이다. Optimum은 Verizon Fios 등 fiber와 직접 경쟁하고, Suddenlink 지역도 AT&T·Frontier fiber와 fixed wireless가 확대될수록 과거의 사실상 독점도가 약해진다. 고객이 감소하면 높은 고정비를 남은 고객에게 분산해야 하므로 margin이 역으로 빠르게 나빠질 수 있다. 고레버리지 구조에서는 FCF의 사용처도 사업모델의 일부다. debt paydown 대신 자사주를 공격적으로 매입하면 주당가치는 사업이 안정적일 때 빠르게 늘지만, EBITDA가 하락하면 같은 전략이 refinancing risk와 equity tail risk를 키운다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Altice의 초기 강점은 지역망의 높은 진입장벽과 broadband의 높은 증분마진이었다. 그러나 cable moat는 절대적이지 않다. fiber overbuild와 fixed wireless는 기존 HFC 고객에게 실제 대체재를 제공하고, 가격인상으로 ARPU를 지키더라도 net adds가 음수이면 총 broadband revenue와 fixed-cost absorption이 약해진다. 또 다른 핵심은 “margin improvement가 moat인지 cost cutting인지”의 구분이다. 인수 후 중복비용 제거로 EBITDA margin이 급상승할 수 있지만, 서비스 품질·영업력·망 투자까지 줄이면 미래 churn과 capex catch-up을 앞당길 수 있다. 따라서 높은 EBITDA margin 그 자체가 경쟁우위의 증거가 아니며 고객수, NPS/서비스 품질, fiber penetration과 장기 maintenance capex를 함께 봐야 한다.

## 4. 돈을 버는 구조

- broadband ARPU×customer relationships가 핵심 고마진 매출
- video는 programming cost 때문에 매출 대비 FCF 기여가 낮음
- FTTH/HFC maintenance·sales·service·new-build cash capex 차감
- FCF에서 debt service와 buyback의 우선순위가 equity risk를 결정

## 5. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격/사업 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2017-11-15 | Long | Long | Broadband mix·cost cutting·deleveraging 롱 | $20.26→$2.44; -88.0%. 2019년 중 $30대는 일시 달성 | 단기 가격 부분 성공·구조적 실패 |
| 2019-05-08 | Long | Long | 10x FCF·levered buyback·fiber capex 정상화 롱 | $23.49→$2.44; -89.6% | 치명적 실패 |
| 2021-08-11 | Long | Long | 17% FCF yield·manageable debt·2025 compounding 롱 | $27.44→$2.44; -91.1% | 치명적 실패 |

---

## 1. 2017-11-15 — Broadband mix·cost cutting·deleveraging 롱

### 결론부터

**종합판정: 단기 가격 부분 성공·구조적 실패.** broadband가 video보다 훨씬 높은 경제성을 가진다는 산업분해는 맞았다. 그러나 cost cutting으로 높아진 margin을 지속 가능한 moat로 보고, 5x 안팎의 leverage에서 FCF가 자연스럽게 debt reduction으로 이어질 것이라고 가정한 것이 약점이었다. 실제 경영진은 자사주·배당 등 자본환원을 병행했고, 훗날 EBITDA가 하락하자 높은 부채가 equity downside를 증폭시켰다.

### 당시 VIC 원문은 무엇을 주장했나

IPO $30에서 $20.26까지 하락한 Altice USA를 2018E 8.25x EV/EBITDA, 약 10% FCF yield로 매수했다. Cablevision과 Suddenlink의 EBITDA가 2015년 약 $2.7bn에서 2017년 약 $4.0bn으로 증가했고, 추가 비용절감 약 $200m과 broadband의 높은 증분마진을 근거로 2018 EBITDA $4.4bn, 2019 $4.5~4.6bn을 예상했다. 연 $1.5bn 이상의 FCF를 쌓아 net debt가 $21.1bn에서 2019년 $18bn으로 감소하고, 9x EBITDA를 적용하면 $30~30.60 주가와 약 20% IRR이 가능하다는 논리였다.

### 원문의 밸류에이션 계산

원문의 가치평가 골격은 **2019 EBITDA $4.5~4.6bn, net debt $18bn, 9x EV/EBITDA → 약 $30.60**였다. 이 숫자를 사후에 단순 목표가 적중 여부로만 보지 않았다. 가입자·ARPU·EBITDA·CapEx·debt·share count가 어떤 순서로 equity value에 전달됐는지 다시 �M�