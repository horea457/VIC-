# Batch 021 — EchoStar·Iridium Satellite Communications 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: EchoStar 8건 · Iridium 2건

## 결론부터

이번 배치는 위성통신에서 **자산가치와 실제 network economics를 구분하는 법**을 본다.

- **EchoStar:** 2008~18 여러 Long은 cash·satellite·STB·spectrum·Hughes를 합친 SOTP에서 반복적으로 큰 upside를 찾았다. 일부 asset와 Hughes operating thesis는 맞았지만, asset monetization duration·satellite replacement CapEx·launch delay·LEO/FWA 경쟁 때문에 주가가 같은 속도로 따라오지 않았다. 특히 2019 Long의 'LEO는 5~20년 위협이 아니다'는 가정은 Starlink로 빠르게 반증됐다.
- **Iridium:** 2009년 같은 시점 Long과 Short가 정면충돌한다. Long은 global coverage·recurring service·M2M과 NEXT funding overhang 해소를 봤고, Short는 $2.7bn+ replacement cost와 handset competition을 봤다. 2010 Coface-backed financing 이후 장기 outcome은 Long 쪽을 강하게 지지했다.

> 데이터 경고: SATS 2008·2012·2019와 IRDM 2009 Long은 원 SQL `is_short=true`지만 실제 본문은 Long이다. 원 raw flag는 보존하고 research direction을 본문 기준으로 교정한다.

---

# ECHOSTAR CORP (SATS) — 기업과 비즈니스

## 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

## 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

## 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2008-02-08 | Short | Long | DISH spin SOTP·$63/$80 Long | 2008년 말 $12.05로 약 -62% 급락. 2013년 말 $40.29까지 회복했지만 원문의 $63~80은 정상적인 1~5년 horizon에서 미달. | 자산 통찰 일부 적중·가격/하방 치명적 실패 |
| 2010-08-12 | Long | Long | Cash-value orphan·$36~44 NAV Long | 2010말 $20.24, 2011말 $16.97, 2012말 $27.73, 2013말 $40.29. NAV 중간값은 약 3년 뒤 실현. | 성공·duration 길음 |
| 2012-02-13 | Short | Long | Hughes/JUPITER 1·$35/$50 Long | 2012말 $27.73, 2013말 $40.29. Base $35를 2년 안에 상회. | 매우 성공 |
| 2013-02-07 | Long | Long | JUPITER unit economics·16% FCF yield·$62 Long | 2013말 $40.29, 2014말 $42.54, 2017말 $48.54. $62 target은 미달. | 사업논지 적중·valuation/timing 실패 |
| 2016-09-07 | Long | Long | Core $60 + S-band $40 + M&A $20 optionality Long | 2017말 $48.54로 상승했지만 2018말 $29.76. Core $60과 bull $120은 미달. | 구조단순화 적중·옵션가치 과대 |
| 2018-03-21 | Long | Long | Hughes 8x EBITDA·JUPITER 2 FCF·$79 SOTP Long | 2018말 $29.76(-47%), 2019말 $43.31. $79.12 target 미달. | 사업 EBITDA 적중·주식 실패 |
| 2019-11-18 | Short | Long | Post-separation Hughes broadband·$60 Long | 2020말 $21.19, 2021말 $26.35, 2022말 $16.68. $60 target 실패. | 치명적 실패 |
| 2021-06-17 | Long | Long | 3.5x EV/EBITDA·JUPITER3 capacity·stealth buyback Long | 2021말 $26.35, 2022말 $16.68, 2023말 $16.57. 평가기준일까지 실패. | 저평가 논지보다 경쟁/launch duration이 압도 |

---

<!-- idea:64097a47-6d23-491d-9e1c-16c9ce272d23 -->
## 1. 2008-02-08 — DISH spin SOTP·$63/$80 Long

### 결론부터

**종합판정: 자산 통찰 일부 적중·가격/하방 치명적 실패.** SOTP 구성은 흥미로웠지만 'cash $12/share + profitable STB'를 사실상 zero downside로 해석한 것이 치명적이었다. 자산은 매각가격·세금·holding-company expense·새 투자·time discount를 거쳐야 equity cash가 된다. $1bn authorization도 실제 가치창출은 집행가격·속도·다른 capital needs에 달려 있다.

**주가·증권 결과:** 2008년 말 $12.05로 약 -62% 급락. 2013년 말 $40.29까지 회복했지만 원문의 $63~80은 정상적인 1~5년 horizon에서 미달.

**Thesis / Process 점수:** 4 / 4.5

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

### 5. 밸류에이션과 기대수익의 연결

90m shares, market cap $2.9bn, EV $1.85bn. Net cash $1.05bn, STB pre-tax profit $135m, satellites/FSS와 SlingMedia를 합산해 SOTP $5.7bn 또는 $63/share. $1bn buyback을 낮은 가격에 실행하면 $80+까지 가능하다고 봤다. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Spin dislocation — 부분 · 논지 비중 18%

**당시 주장**

신규 spin과 무IR 상태가 일시적 mispricing을 만든다.

**당시 근거**

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

**이 주장이 성립하려면**

사업가치 안정·투자자 discovery

**사전 반증조건**

구조복잡성/자본배분이 discount 지속

**실제 결과**

장기간 discount가 유지됐다.

**정량적 괴리**

주가 / $32 / $63 SOTP / $80+ bull / 2008말 $12.05; 2013말 $40.29

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Spin dislocation 가설은 '구조복잡성/자본배분이 discount 지속'를 사전 반증조건으로 저장한다.

#### 2. STB value — 부분 실패 · 논지 비중 18%

**당시 주장**

STB의 $135m pre-tax profit에 $3bn 가치가 합리적이다.

**당시 근거**

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

**이 주장이 성립하려면**

DISH 외 고객확장·낮은 capital intensity

**사전 반증조건**

customer concentration/기술 commoditization

**실제 결과**

자산가치는 있었지만 독립적으로 $3bn이 crystallize되진 않았다.

**정량적 괴리**

Net cash / $1.05bn / ~$12/share / downside floor / 주가가 cash/share 부근까지 하락

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

STB value 가설은 'customer concentration/기술 commoditization'를 사전 반증조건으로 저장한다.

#### 3. Satellite value — 부분 · 논지 비중 16%

**당시 주장**

위성/FSS를 $900m 이상 평가할 수 있다.

**당시 근거**

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

**이 주장이 성립하려면**

capacity 수요·utilization 상승

**사전 반증조건**

유휴 capacity와 CapEx 부담

**실제 결과**

FSS는 cash-generative였지만 전체 주가 floor는 못 됐다.

**정량적 괴리**

STB / $135m pre-tax / $3bn 가치 / 후일 DISH로 자산 이전

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Satellite value 가설은 '유휴 capacity와 CapEx 부담'를 사전 반증조건으로 저장한다.

#### 4. Cash floor — 실패 · 논지 비중 16%

**당시 주장**

$1.05bn net cash가 downside를 거의 없앤다.

**당시 근거**

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

**이 주장이 성립하려면**

현금이 주주에게 보존·배분

**사전 반증조건**

M&A/CapEx/기업비용으로 cash 사용

**실제 결과**

주가가 크게 하락해 floor 가정 실패.

**정량적 괴리**

Buyback / $1bn authorization / 주당가치 증폭 / authorization만으로 floor 형성 못함

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Cash floor 가설은 'M&A/CapEx/기업비용으로 cash 사용'를 사전 반증조건으로 저장한다.

#### 5. Buyback — 부분 실패 · 논지 비중 16%

**당시 주장**

$1bn buyback이 낮은 가격에서 큰 accretion을 만든다.

**당시 근거**

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

**이 주장이 성립하려면**

실제 대규모 집행·intrinsic value 이하

**사전 반증조건**

자본이 다른 전략자산에 투입

**실제 결과**

예상한 즉시 per-share accretion이 나타나지 않았다.

**정량적 괴리**

2008년 말 $12.05로 약 -62% 급락. 2013년 말 $40.29까지 회복했지만 원문의 $63~80은 정상적인 1~5년 horizon에서 미달.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Buyback 가설은 '자본이 다른 전략자산에 투입'를 사전 반증조건으로 저장한다.

#### 6. $63/$80 — 실패 · 논지 비중 16%

**당시 주장**

SOTP와 buyback으로 2배 이상 upside다.

**당시 근거**

DISH에서 새로 분사된 SATS가 IR도 하지 않고 연초 한산한 시점에 spin되어 시장의 관심이 거의 없다고 봤다. STB 기술사업을 $3bn, 위성/FSS $900m, SlingMedia $380m, 현금 $1.05bn 등으로 평가해 현재가보다 훨씬 높은 SOTP를 제시했다. Charlie Ergen이 경제적 지분 50%를 갖고 $1bn buyback 권한을 이용해 싸게 주식을 살 것이라는 capital-allocation optionality도 핵심이었다.

**이 주장이 성립하려면**

asset monetization과 discount closure

**사전 반증조건**

time/leakage/구조변화

**실제 결과**

정상 horizon 내 미달.

**정량적 괴리**

2008년 말 $12.05로 약 -62% 급락. 2013년 말 $40.29까지 회복했지만 원문의 $63~80은 정상적인 1~5년 horizon에서 미달.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

$63/$80 가설은 'time/leakage/구조변화'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

초기 자산 자체는 실재했고 일부는 이후 전략적 가치가 확인됐다. 그러나 2008 금융위기와 기업복잡성·자산 monetization duration 때문에 주가는 연말 $12.05까지 급락했다. 이후 Hughes 인수 등으로 회사구조 자체가 달라졌고 2013년 $40.29로 회복했어도 $63 SOTP에는 미달했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2008년 말 $12.05로 약 -62% 급락. 2013년 말 $40.29까지 회복했지만 원문의 $63~80은 정상적인 1~5년 horizon에서 미달. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

SOTP 구성은 흥미로웠지만 'cash $12/share + profitable STB'를 사실상 zero downside로 해석한 것이 치명적이었다. 자산은 매각가격·세금·holding-company expense·새 투자·time discount를 거쳐야 equity cash가 된다. $1bn authorization도 실제 가치창출은 집행가격·속도·다른 capital needs에 달려 있다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-12-31 — 연말 주가 $12.05로 내려가 원문의 'downside is nothing' 가정이 정면으로 반증됐다. 회피 가능성: 높음. SOTP discount가 닫히지 않는 동안 각 asset의 실제 cash conversion과 corporate spending을 재계산했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

자산 통찰 일부 적중·가격/하방 치명적 실패. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $32 | $63 SOTP / $80+ bull | 2008말 $12.05; 2013말 $40.29 | 실패 |
| Net cash | $1.05bn / ~$12/share | downside floor | 주가가 cash/share 부근까지 하락 | floor 실패 |
| STB | $135m pre-tax | $3bn 가치 | 후일 DISH로 자산 이전 | 가치 있었으나 crystallization 지연 |
| Buyback | $1bn authorization | 주당가치 증폭 | authorization만으로 floor 형성 못함 | 과대 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2008-02-08 | VIC 아이디어 게시 | DISH spin SOTP·$63/$80 Long |
| 2008-12-31 | 최초 핵심 검증·반증 신호 | 연말 주가 $12.05로 내려가 원문의 'downside is nothing' 가정이 정면으로 반증됐다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2008년 말 $12.05로 약 -62% 급락. 2013년 말 $40.29까지 회복했지만 원문의 $63~80은 정상적인 1~5년 horizon에서 미달. |

### Failure / Success Anatomy

- **근본 오류:** 자산/EBITDA를 full-cycle CapEx·경쟁·launch duration·실현확률 없이 equity value로 직접 연결
- **최초 검증·반증 신호:** 2008-12-31 — 연말 주가 $12.05로 내려가 원문의 'downside is nothing' 가정이 정면으로 반증됐다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 높음. SOTP discount가 닫히지 않는 동안 각 asset의 실제 cash conversion과 corporate spending을 재계산했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2008-02-08 원문](https://www.valueinvestorsclub.com/idea/EchoStar_Corporation/1123662943) — Value Investors Club, 2008-02-08. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:31ceb984-9355-46ae-813a-ee7610074438 -->
## 2. 2010-08-12 — Cash-value orphan·$36~44 NAV Long

### 결론부터

**종합판정: 성공·duration 길음.** 2008 글보다 훨씬 나은 점은 cash-value 대비 operating assets의 implied value를 명확히 보여주고 valuation range를 제시한 것이다. 다만 near-cash NAV도 즉시 수렴하지 않았고 3년의 duration이 필요했다.

**주가·증권 결과:** 2010말 $20.24, 2011말 $16.97, 2012말 $27.73, 2013말 $40.29. NAV 중간값은 약 3년 뒤 실현.

**Thesis / Process 점수:** 6.8 / 7.4

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Cash·marketable investments 약 $1.526bn 또는 $17.92/share로 주가 대부분 설명. STB 4~6x EBITDA, FSS 7.5~8.5x EBITDA와 기타 assets를 합쳐 NAV $35.99~43.86, upside 94.5~137.1%. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Cash-backed valuation — 부분 적중 · 논지 비중 18%

**당시 주장**

주가가 cash/investments와 거의 같아 operating assets가 공짜다.

**당시 근거**

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

**이 주장이 성립하려면**

cash quality 유지

**사전 반증조건**

cash burn/M&A overpayment

**실제 결과**

Hughes M&A로 cash가 쓰였지만 기업가치가 살아남았다.

**정량적 괴리**

주가 / $18.50 / $35.99~43.86 / 2013말 $40.29

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Cash-backed valuation 가설은 'cash burn/M&A overpayment'를 사전 반증조건으로 저장한다.

#### 2. FSS value — 적중 · 논지 비중 18%

**당시 주장**

장기계약·유휴 capacity가 FSS upside를 만든다.

**당시 근거**

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

**이 주장이 성립하려면**

lease-up

**사전 반증조건**

capacity oversupply

**실제 결과**

FSS가 의미있는 cash generator로 지속.

**정량적 괴리**

Cash/investments / $1.526bn / $17.92 / 가격 대부분 커버 / 현금 기반 유지 후 전략투자

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

FSS value 가설은 'capacity oversupply'를 사전 반증조건으로 저장한다.

#### 3. STB value — 부분 · 논지 비중 16%

**당시 주장**

STB가 4~6x EBITDA의 독립가치를 갖는다.

**당시 근거**

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

**이 주장이 성립하려면**

customer demand 유지

**사전 반증조건**

DISH dependence

**실제 결과**

후일 DISH 관련 구조재편으로 standalone value가 복잡했다.

**정량적 괴리**

FSS EBITDA / LTM $244m 수준 / 7.5~8.5x / 위성서비스 가치 유지

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

STB value 가설은 'DISH dependence'를 사전 반증조건으로 저장한다.

#### 4. Sling optionality — 부분 · 논지 비중 16%

**당시 주장**

Sling은 valuation에 거의 공짜의 upside다.

**당시 근거**

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

**이 주장이 성립하려면**

consumer adoption

**사전 반증조건**

경쟁기술

**실제 결과**

전체 thesis의 핵심 value driver는 아니었다.

**정량적 괴리**

STB EBITDA / LTM $212m / 4~6x / 후일 구조변경

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Sling optionality 가설은 '경쟁기술'를 사전 반증조건으로 저장한다.

#### 5. Investor discovery — 적중·지연 · 논지 비중 16%

**당시 주장**

orphan status가 해소되면 NAV discount가 닫힌다.

**당시 근거**

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

**이 주장이 성립하려면**

coverage/catalyst 증가

**사전 반증조건**

permanent holding discount

**실제 결과**

3년 걸려 상당부분 수렴.

**정량적 괴리**

2010말 $20.24, 2011말 $16.97, 2012말 $27.73, 2013말 $40.29. NAV 중간값은 약 3년 뒤 실현.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Investor discovery 가설은 'permanent holding discount'를 사전 반증조건으로 저장한다.

#### 6. $36~44 NAV — 강한 적중 · 논지 비중 16%

**당시 주장**

보수적 segment multiples만으로 2배 가능.

**당시 근거**

2008 spin 이후 주가가 60%가량 떨어지고 투자자·sell-side coverage가 거의 없어 operating businesses를 공짜로 사는 상황이라고 봤다. STB·FSS의 cash earnings, fully/partly leased satellites, Sling와 국제 JV가 value를 만들고 cash가 하방을 지지한다고 주장했다.

**이 주장이 성립하려면**

assets 유지·no major leakage

**사전 반증조건**

corporate actions value destruction

**실제 결과**

2013 $40.29로 범위 도달.

**정량적 괴리**

2010말 $20.24, 2011말 $16.97, 2012말 $27.73, 2013말 $40.29. NAV 중간값은 약 3년 뒤 실현.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

$36~44 NAV 가설은 'corporate actions value destruction'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

단기적으로는 2011년에도 $16.97까지 내려가 value trap처럼 보였지만 2012 Hughes integration과 operating asset 가치가 재인식되면서 2013년 말 $40.29로 NAV 범위 안에 들어갔다. 다만 corporate structure 변화와 M&A가 원래 asset mix를 바꿨다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2010말 $20.24, 2011말 $16.97, 2012말 $27.73, 2013말 $40.29. NAV 중간값은 약 3년 뒤 실현. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

2008 글보다 훨씬 나은 점은 cash-value 대비 operating assets의 implied value를 명확히 보여주고 valuation range를 제시한 것이다. 다만 near-cash NAV도 즉시 수렴하지 않았고 3년의 duration이 필요했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-12-31 — 주가가 $27.73으로 회복하고 Hughes broadband가 새로운 핵심사업이 되면서 operating assets에 0보다 큰 가치가 붙기 시작했다. 회피 가능성: 해당 없음. 다만 expected IRR은 1년이 아니라 3년 duration으로 재계산해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

성공·duration 길음. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $18.50 | $35.99~43.86 | 2013말 $40.29 | 적중·지연 |
| Cash/investments | $1.526bn / $17.92 | 가격 대부분 커버 | 현금 기반 유지 후 전략투자 | 적중 |
| FSS EBITDA | LTM $244m 수준 | 7.5~8.5x | 위성서비스 가치 유지 | 방향 적중 |
| STB EBITDA | LTM $212m | 4~6x | 후일 구조변경 | 부분 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2010-08-12 | VIC 아이디어 게시 | Cash-value orphan·$36~44 NAV Long |
| 2012-12-31 | 최초 핵심 검증·반증 신호 | 주가가 $27.73으로 회복하고 Hughes broadband가 새로운 핵심사업이 되면서 operating assets에 0보다 큰 가치가 붙기 시작했다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2010말 $20.24, 2011말 $16.97, 2012말 $27.73, 2013말 $40.29. NAV 중간값은 약 3년 뒤 실현. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating mechanism과 binary funding risk를 구분
- **최초 검증·반증 신호:** 2012-12-31 — 주가가 $27.73으로 회복하고 Hughes broadband가 새로운 핵심사업이 되면서 operating assets에 0보다 큰 가치가 붙기 시작했다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 해당 없음. 다만 expected IRR은 1년이 아니라 3년 duration으로 재계산해야 했다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2010-08-12 원문](https://www.valueinvestorsclub.com/idea/ECHOSTAR_CORP/4710125426) — Value Investors Club, 2010-08-12. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:5e1b605a-7221-4802-9e28-557d720b83f3 -->
## 3. 2012-02-13 — Hughes/JUPITER 1·$35/$50 Long

### 결론부터

**종합판정: 매우 성공.** 이 글은 자산합산보다 acquisition 이후 실제 operating catalyst인 satellite capacity를 봤다는 점이 좋았다. 위성 broadband는 capacity가 차면 성장이 멈추고 새 위성에서 다시 뛰는 계단식 economics라는 점을 잘 포착했다.

**주가·증권 결과:** 2012말 $27.73, 2013말 $40.29. Base $35를 2년 안에 상회.

**Thesis / Process 점수:** 9 / 7.4

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Recommendation Buy, price $25, fair value $35+, bull $50, bear $18. Breakup example 약 $31.91, sell-side SOTP $40~50. Hughes acquisition과 JUPITER 1 ramp를 핵심 upside로 평가. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Hughes acquisition — 적중 · 논지 비중 18%

**당시 주장**

Hughes는 가치있는 broadband platform이다.

**당시 근거**

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

**이 주장이 성립하려면**

integration·distribution 안정

**사전 반증조건**

subscriber/ARPU 악화

**실제 결과**

핵심사업으로 자리잡았다.

**정량적 괴리**

주가 / $25 / $35+ / bull $50 / 2013말 $40.29

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Hughes acquisition 가설은 'subscriber/ARPU 악화'를 사전 반증조건으로 저장한다.

#### 2. JUPITER 1 — 적중 · 논지 비중 18%

**당시 주장**

신규 satellite capacity가 성장병목을 풀어준다.

**당시 근거**

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

**이 주장이 성립하려면**

launch/ramp 성공

**사전 반증조건**

launch delay·capacity monetization 실패

**실제 결과**

성장 catalyst가 됐다.

**정량적 괴리**

Bear / $18 / downside limited / 2012말 $27.73

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

JUPITER 1 가설은 'launch delay·capacity monetization 실패'를 사전 반증조건으로 저장한다.

#### 3. SOTP floor — 적중 · 논지 비중 16%

**당시 주장**

기존 satellite/Sling assets가 $25 하방을 제한한다.

**당시 근거**

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

**이 주장이 성립하려면**

asset value 유지

**사전 반증조건**

cash burn/leakage

**실제 결과**

해당 horizon에서 하방 제한.

**정량적 괴리**

Breakup / $31.91 / asset floor / 시장가치가 상회

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

SOTP floor 가설은 'cash burn/leakage'를 사전 반증조건으로 저장한다.

#### 4. Subscriber growth — 적중 · 논지 비중 16%

**당시 주장**

capacity 증가가 subscriber adds로 이어진다.

**당시 근거**

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

**이 주장이 성립하려면**

rural demand

**사전 반증조건**

terrestrial substitution

**실제 결과**

당시에는 성장했다.

**정량적 괴리**

Hughes / 신규 인수 / JUPITER 성장 / 핵심사업으로 성장

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Subscriber growth 가설은 'terrestrial substitution'를 사전 반증조건으로 저장한다.

#### 5. Valuation — 강한 적중 · 논지 비중 16%

**당시 주장**

$25는 bear에 가깝고 base $35 이상이다.

**당시 근거**

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

**이 주장이 성립하려면**

operating growth

**사전 반증조건**

multiple compression

**실제 결과**

2013 $40.29.

**정량적 괴리**

2012말 $27.73, 2013말 $40.29. Base $35를 2년 안에 상회.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Valuation 가설은 'multiple compression'를 사전 반증조건으로 저장한다.

#### 6. Bull $50 — 부분 · 논지 비중 16%

**당시 주장**

SOTP와 성장 모두 잘되면 $50 가능하다.

**당시 근거**

2011 Hughes 인수로 SATS가 consumer satellite broadband와 enterprise networking에 진입했고, JUPITER 1의 신규 capacity가 subscriber/ARPU 성장을 재가속할 것으로 봤다. 기존 satellite services·Sling 등의 option value까지 감안하면 $25는 bear와 가깝고 base $35 이상이라고 주장했다.

**이 주장이 성립하려면**

multiple/capacity 모두 강함

**사전 반증조건**

catalyst 일부 지연

**실제 결과**

해당 초기 horizon에서는 미달.

**정량적 괴리**

2012말 $27.73, 2013말 $40.29. Base $35를 2년 안에 상회.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Bull $50 가설은 'catalyst 일부 지연'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Hughes는 이후 EchoStar의 핵심사업이 됐고 broadband subscriber base가 확대됐다. 주가는 2013년 말 $40.29로 base를 넘어섰다. 다만 satellite broadband의 지속성은 훗날 LEO/FWA 경쟁으로 다시 시험받았다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2012말 $27.73, 2013말 $40.29. Base $35를 2년 안에 상회. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 자산합산보다 acquisition 이후 실제 operating catalyst인 satellite capacity를 봤다는 점이 좋았다. 위성 broadband는 capacity가 차면 성장이 멈추고 새 위성에서 다시 뛰는 계단식 economics라는 점을 잘 포착했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2013-02-01 — Hughes/JUPITER capacity ramp가 revenue·subscriber 성장으로 이어지면서 acquisition thesis가 검증되기 시작했다. 회피 가능성: 해당 없음. 다만 장기보유에서는 다음 satellite replacement와 경쟁기술을 새로 검증해야 했다.

### 10. 최종 판정·반사실·재사용 교훈

매우 성공. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $25 | $35+ / bull $50 | 2013말 $40.29 | base 성공 |
| Bear | $18 | downside limited | 2012말 $27.73 | 하방 미실현 |
| Breakup | $31.91 | asset floor | 시장가치가 상회 | 적중 |
| Hughes | 신규 인수 | JUPITER 성장 | 핵심사업으로 성장 | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2012-02-13 | VIC 아이디어 게시 | Hughes/JUPITER 1·$35/$50 Long |
| 2013-02-01 | 최초 핵심 검증·반증 신호 | Hughes/JUPITER capacity ramp가 revenue·subscriber 성장으로 이어지면서 acquisition thesis가 검증되기 시작했다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2012말 $27.73, 2013말 $40.29. Base $35를 2년 안에 상회. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating mechanism과 binary funding risk를 구분
- **최초 검증·반증 신호:** 2013-02-01 — Hughes/JUPITER capacity ramp가 revenue·subscriber 성장으로 이어지면서 acquisition thesis가 검증되기 시작했다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 해당 없음. 다만 장기보유에서는 다음 satellite replacement와 경쟁기술을 새로 검증해야 했다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2012-02-13 원문](https://www.valueinvestorsclub.com/idea/ECHOSTAR_CORP/1949495599) — Value Investors Club, 2012-02-13. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:c7ac6d42-41e4-4251-b4f9-ca8bbad8039d -->
## 4. 2013-02-07 — JUPITER unit economics·16% FCF yield·$62 Long

### 결론부터

**종합판정: 사업논지 적중·valuation/timing 실패.** 운영 unit economics는 좋았지만 satellite replacement CapEx를 '성장투자라서 제외 가능한 비용'처럼 다룬 부분이 valuation을 공격적으로 만들었다. 장기 satellite business에서는 세대교체 CapEx가 사실상 recurring economic cost다.

**주가·증권 결과:** 2013말 $40.29, 2014말 $42.54, 2017말 $48.54. $62 target은 미달.

**Thesis / Process 점수:** 6.8 / 7.4

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

2014 earnings 기준 약 16% FCF yield. Core earnings 10~12% 성장, DISH Mexico option 약 $7/share를 포함하고 10% FCF yield를 적용해 $62, 약 70% upside. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. JUPITER unit economics — 적중 · 논지 비중 18%

**당시 주장**

capacity가 채워질수록 incremental margin이 매우 높다.

**당시 근거**

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

**이 주장이 성립하려면**

subscriber demand

**사전 반증조건**

capacity idle

**실제 결과**

Hughes economics의 핵심으로 확인.

**정량적 괴리**

주가 / $36~37 / $62 / 2017말 $48.54

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

JUPITER unit economics 가설은 'capacity idle'를 사전 반증조건으로 저장한다.

#### 2. Fixed-cost leverage — 적중 · 논지 비중 18%

**당시 주장**

가입자 증가가 EBITDA를 빠르게 높인다.

**당시 근거**

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

**이 주장이 성립하려면**

network cost largely fixed

**사전 반증조건**

customer acquisition/opex 증가

**실제 결과**

EBITDA 성장에 기여.

**정량적 괴리**

FCF yield / ~16% 2014E / 10%로 rerating / 대규모 satellite CapEx 지속

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Fixed-cost leverage 가설은 'customer acquisition/opex 증가'를 사전 반증조건으로 저장한다.

#### 3. FCF conversion — 실패 · 논지 비중 16%

**당시 주장**

높은 EBITDA가 16% FCF yield로 이어진다.

**당시 근거**

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

**이 주장이 성립하려면**

next-gen capex를 growth로 분리 가능

**사전 반증조건**

replacement/growth capex 상시 반복

**실제 결과**

full-cycle FCF는 기대보다 낮았다.

**정량적 괴리**

Core growth / 10~12% / 지속 / Hughes 성장

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

FCF conversion 가설은 'replacement/growth capex 상시 반복'를 사전 반증조건으로 저장한다.

#### 4. Core 10~12% — 적중 · 논지 비중 16%

**당시 주장**

core earnings가 저두자릿수 성장한다.

**당시 근거**

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

**이 주장이 성립하려면**

capacity ramp

**사전 반증조건**

subscriber saturation

**실제 결과**

일정 기간 성장.

**정량적 괴리**

DISH Mexico / ~$7/share option / 추가 upside / 핵심 가치촉매 아님

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Core 10~12% 가설은 'subscriber saturation'를 사전 반증조건으로 저장한다.

#### 5. Mexico option — 부분 실패 · 논지 비중 16%

**당시 주장**

DISH Mexico가 $7/share 이상의 optionality다.

**당시 근거**

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

**이 주장이 성립하려면**

시장진입/가치현실화

**사전 반증조건**

사업가치 미미

**실제 결과**

중심 catalyst가 아니었다.

**정량적 괴리**

2013말 $40.29, 2014말 $42.54, 2017말 $48.54. $62 target은 미달.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Mexico option 가설은 '사업가치 미미'를 사전 반증조건으로 저장한다.

#### 6. $62 target — 실패 · 논지 비중 16%

**당시 주장**

10% FCF yield면 $62 가능하다.

**당시 근거**

JUPITER broadband subscriber의 incremental economics가 매우 좋아 기존 satellite capacity ramp가 EBITDA/FCF를 빠르게 높일 수 있다고 봤다. 높은 fixed-cost 위성망에서 가입자 증가가 높은 incremental margin을 만들며, DISH Mexico 등 옵션은 별도 upside라고 주장했다.

**이 주장이 성립하려면**

FCF quality·multiple

**사전 반증조건**

capital intensity discount

**실제 결과**

미달.

**정량적 괴리**

2013말 $40.29, 2014말 $42.54, 2017말 $48.54. $62 target은 미달.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

$62 target 가설은 'capital intensity discount'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Hughes broadband와 satellite capacity economics는 실제 중요한 earnings driver가 됐다. 그러나 satellite CapEx와 다음-generation capacity investment 때문에 reported EBITDA가 곧바로 높은 distributable FCF로 바뀌지는 않았고 주가는 수년간 $40대에 머물렀다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2013말 $40.29, 2014말 $42.54, 2017말 $48.54. $62 target은 미달. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

운영 unit economics는 좋았지만 satellite replacement CapEx를 '성장투자라서 제외 가능한 비용'처럼 다룬 부분이 valuation을 공격적으로 만들었다. 장기 satellite business에서는 세대교체 CapEx가 사실상 recurring economic cost다.

### 9. 최초 검증·반증 신호와 회피 가능성

2014-12-31 — 주가가 $42.54에 머물고 계속되는 위성투자로 16% FCF yield가 즉시 equity rerating으로 이어지지 않음이 드러났다. 회피 가능성: 높음. EBITDA와 pre-growth FCF 대신 full-cycle satellite replacement CapEx를 포함한 owner earnings를 계산했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

사업논지 적중·valuation/timing 실패. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $36~37 | $62 | 2017말 $48.54 | 실패 |
| FCF yield | ~16% 2014E | 10%로 rerating | 대규모 satellite CapEx 지속 | 과대 |
| Core growth | 10~12% | 지속 | Hughes 성장 | 방향 적중 |
| DISH Mexico | ~$7/share option | 추가 upside | 핵심 가치촉매 아님 | 부분 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2013-02-07 | VIC 아이디어 게시 | JUPITER unit economics·16% FCF yield·$62 Long |
| 2014-12-31 | 최초 핵심 검증·반증 신호 | 주가가 $42.54에 머물고 계속되는 위성투자로 16% FCF yield가 즉시 equity rerating으로 이어지지 않음이 드러났다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2013말 $40.29, 2014말 $42.54, 2017말 $48.54. $62 target은 미달. |

### Failure / Success Anatomy

- **근본 오류:** 자산/EBITDA를 full-cycle CapEx·경쟁·launch duration·실현확률 없이 equity value로 직접 연결
- **최초 검증·반증 신호:** 2014-12-31 — 주가가 $42.54에 머물고 계속되는 위성투자로 16% FCF yield가 즉시 equity rerating으로 이어지지 않음이 드러났다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 높음. EBITDA와 pre-growth FCF 대신 full-cycle satellite replacement CapEx를 포함한 owner earnings를 계산했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2013-02-07 원문](https://www.valueinvestorsclub.com/idea/ECHOSTAR_CORP/0402875861) — Value Investors Club, 2013-02-07. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:fe0f47a5-5050-4c58-a5e3-258b1ded93ef -->
## 5. 2016-09-07 — Core $60 + S-band $40 + M&A $20 optionality Long

### 결론부터

**종합판정: 구조단순화 적중·옵션가치 과대.** 복잡성 discount와 구조단순화 가능성은 잘 봤지만 option을 확률가중하지 않고 per-share value로 거의 직접 합산했다. spectrum은 license, network build, counterparties, regulation이 있어야 가치가 실현된다.

**주가·증권 결과:** 2017말 $48.54로 상승했지만 2018말 $29.76. Core $60과 bull $120은 미달.

**Thesis / Process 점수:** 6.8 / 7.4

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Core target 약 $60(50%+ upside), European S-band spectrum option 약 $40/share, M&A optionality 약 $20/share를 더해 bull-case ~$120. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. STB recovery — 판정불가/전제변경 · 논지 비중 18%

**당시 주장**

set-top-box decline이 바닥을 찍는다.

**당시 근거**

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

**이 주장이 성립하려면**

DISH demand 안정

**사전 반증조건**

continued secular decline

**실제 결과**

사업 자체가 DISH로 이전됐다.

**정량적 괴리**

Core target / ~$60 / 50%+ upside / 2017 $48.54, 2018 $29.76

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

STB recovery 가설은 'continued secular decline'를 사전 반증조건으로 저장한다.

#### 2. Hughes growth — 적중 · 논지 비중 18%

**당시 주장**

broadband/enterprise가 core를 성장시킨다.

**당시 근거**

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

**이 주장이 성립하려면**

capacity/demand

**사전 반증조건**

competition

**실제 결과**

주요 사업으로 성장.

**정량적 괴리**

S-band / ~$40/share option / value unlock / 빠른 crystallization 없음

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Hughes growth 가설은 'competition'를 사전 반증조건으로 저장한다.

#### 3. S-band value — 실패 · 논지 비중 16%

**당시 주장**

European S-band가 $40/share option이다.

**당시 근거**

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

**이 주장이 성립하려면**

commercialization/partner

**사전 반증조건**

spectrum remains stranded

**실제 결과**

빠른 가치현실화 없음.

**정량적 괴리**

M&A / ~$20/share option / strategic value / 구조변화는 있었으나 현금화 아님

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

S-band value 가설은 'spectrum remains stranded'를 사전 반증조건으로 저장한다.

#### 4. M&A optionality — 부분 · 논지 비중 16%

**당시 주장**

strategic transactions가 $20/share 추가가치다.

**당시 근거**

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

**이 주장이 성립하려면**

counterparty/action

**사전 반증조건**

no transaction

**실제 결과**

asset swap은 있었지만 주장한 incremental equity value와 다름.

**정량적 괴리**

STB / bottoming / core recovery / 2017 DISH로 이전

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

M&A optionality 가설은 'no transaction'를 사전 반증조건으로 저장한다.

#### 5. Structure simplification — 강한 적중 · 논지 비중 16%

**당시 주장**

복잡한 SATS 구조가 단순해질 수 있다.

**당시 근거**

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

**이 주장이 성립하려면**

Ergen capital actions

**사전 반증조건**

status quo

**실제 결과**

2017 asset swap.

**정량적 괴리**

2017말 $48.54로 상승했지만 2018말 $29.76. Core $60과 bull $120은 미달.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Structure simplification 가설은 'status quo'를 사전 반증조건으로 저장한다.

#### 6. $60/$120 — 실패 · 논지 비중 16%

**당시 주장**

core+options가 큰 rerating을 만든다.

**당시 근거**

set-top-box 사업이 바닥을 통과하고 satellite launch pipeline이 robust하며, Hughes의 broadband와 enterprise 사업이 성장한다고 봤다. 시장은 European S-band spectrum과 strategic M&A 가능성을 거의 0으로 평가해 숨은 option value가 크다고 주장했다.

**이 주장이 성립하려면**

options crystallize

**사전 반증조건**

time discount

**실제 결과**

미달.

**정량적 괴리**

2017말 $48.54로 상승했지만 2018말 $29.76. Core $60과 bull $120은 미달.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

$60/$120 가설은 'time discount'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2017 DISH와의 자산교환으로 set-top-box business가 DISH로 이전돼 회사가 Hughes/satellite communications 쪽으로 단순해졌다. 그러나 S-band spectrum과 M&A option이 원문처럼 큰 현금가치로 빠르게 crystallize되지 않았고 2018 주가는 $29.76으로 하락했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2017말 $48.54로 상승했지만 2018말 $29.76. Core $60과 bull $120은 미달. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

복잡성 discount와 구조단순화 가능성은 잘 봤지만 option을 확률가중하지 않고 per-share value로 거의 직접 합산했다. spectrum은 license, network build, counterparties, regulation이 있어야 가치가 실현된다.

### 9. 최초 검증·반증 신호와 회피 가능성

2017-02-28 — DISH와의 asset swap 발표로 구조단순화 thesis는 확인됐지만 동시에 원래 core asset mix가 바뀌어 $60/$120 SOTP를 재작성해야 했다. 회피 가능성: 높음. corporate action 직후 old SOTP를 폐기하고 residual Hughes economics로 다시 valuation했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

구조단순화 적중·옵션가치 과대. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Core target | ~$60 | 50%+ upside | 2017 $48.54, 2018 $29.76 | 미달 |
| S-band | ~$40/share option | value unlock | 빠른 crystallization 없음 | 실패 |
| M&A | ~$20/share option | strategic value | 구조변화는 있었으나 현금화 아님 | 부분 |
| STB | bottoming | core recovery | 2017 DISH로 이전 | 전제 변경 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-09-07 | VIC 아이디어 게시 | Core $60 + S-band $40 + M&A $20 optionality Long |
| 2017-02-28 | 최초 핵심 검증·반증 신호 | DISH와의 asset swap 발표로 구조단순화 thesis는 확인됐지만 동시에 원래 core asset mix가 바뀌어 $60/$120 SOTP를 재작성해야 했다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2017말 $48.54로 상승했지만 2018말 $29.76. Core $60과 bull $120은 미달. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating mechanism과 binary funding risk를 구분
- **최초 검증·반증 신호:** 2017-02-28 — DISH와의 asset swap 발표로 구조단순화 thesis는 확인됐지만 동시에 원래 core asset mix가 바뀌어 $60/$120 SOTP를 재작성해야 했다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 높음. corporate action 직후 old SOTP를 폐기하고 residual Hughes economics로 다시 valuation했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2016-09-07 원문](https://www.valueinvestorsclub.com/idea/ECHOSTAR_CORP/6909130868) — Value Investors Club, 2016-09-07. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:7f50f7e9-9283-4958-9ff9-2731c84bd0ec -->
## 6. 2018-03-21 — Hughes 8x EBITDA·JUPITER 2 FCF·$79 SOTP Long

### 결론부터

**종합판정: 사업 EBITDA 적중·주식 실패.** 이 사례는 '기업실적을 맞히는 것과 주가를 맞히는 것'의 좋은 분리다. 2018 EBITDA는 오히려 thesis보다 강했지만 시장은 capital intensity와 다음 capacity cycle, competitive risk에 낮은 multiple을 줬다.

**주가·증권 결과:** 2018말 $29.76(-47%), 2019말 $43.31. $79.12 target 미달.

**Thesis / Process 점수:** 6.8 / 7.4

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

### 5. 밸류에이션과 기대수익의 연결

SOTP $79.12, +40.3%. 2018E Hughes EBITDA 약 $650m ×8x; JUPITER 2 full-capacity annual EBITDA $280m+ 추정. OneWeb, S-band, JUPITER 3는 사실상 upside로 제외. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Hughes EBITDA — 적중 · 논지 비중 18%

**당시 주장**

Hughes earnings가 강하게 성장한다.

**당시 근거**

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

**이 주장이 성립하려면**

capacity fill

**사전 반증조건**

subscriber weakness

**실제 결과**

2018 operating outcome 강함.

**정량적 괴리**

주가 / $56.40 / $79.12 / 2018말 $29.76

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Hughes EBITDA 가설은 'subscriber weakness'를 사전 반증조건으로 저장한다.

#### 2. JUPITER 2 — 방향 적중 · 논지 비중 18%

**당시 주장**

JUPITER2가 $280m+ annual EBITDA capacity를 만든다.

**당시 근거**

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

**이 주장이 성립하려면**

utilization

**사전 반증조건**

competition/launch issues

**실제 결과**

capacity가 broadband growth를 지지.

**정량적 괴리**

2018 EBITDA / Hughes ~$650m 기반 / 성장 / consolidated $757m / ex items $834m

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

JUPITER 2 가설은 'competition/launch issues'를 사전 반증조건으로 저장한다.

#### 3. 8x multiple — 실패 · 논지 비중 16%

**당시 주장**

Hughes에 8x EBITDA가 보수적이다.

**당시 근거**

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

**이 주장이 성립하려면**

peer multiple 유지

**사전 반증조건**

capital intensity/competition discount

**실제 결과**

시장 multiple이 훨씬 낮아짐.

**정량적 괴리**

Broadband subs / 성장 / JUPITER 2 ramp / 2018 1.361m

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

8x multiple 가설은 'capital intensity/competition discount'를 사전 반증조건으로 저장한다.

#### 4. Optional assets — 부분 실패 · 논지 비중 16%

**당시 주장**

OneWeb/S-band/J3는 공짜 upside다.

**당시 근거**

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

**이 주장이 성립하려면**

option value nonnegative

**사전 반증조건**

cash burn/stranded capital

**실제 결과**

즉시 equity 가치로 이어지지 않음.

**정량적 괴리**

JUPITER 2 / $280m+ full-capacity EBITDA / 현금화 / capacity monetization 진행

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Optional assets 가설은 'cash burn/stranded capital'를 사전 반증조건으로 저장한다.

#### 5. Subscriber value — 부분 적중 · 논지 비중 16%

**당시 주장**

1m+ base가 recurring value를 만든다.

**당시 근거**

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

**이 주장이 성립하려면**

churn/ARPU 안정

**사전 반증조건**

terrestrial/LEO substitution

**실제 결과**

당시에는 성장했지만 후일 경쟁 심화.

**정량적 괴리**

2018말 $29.76(-47%), 2019말 $43.31. $79.12 target 미달.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Subscriber value 가설은 'terrestrial/LEO substitution'를 사전 반증조건으로 저장한다.

#### 6. $79.12 — 실패 · 논지 비중 16%

**당시 주장**

SOTP가 40% upside를 제공한다.

**당시 근거**

2017 asset swap 뒤 Hughes가 clearer core가 되었고, JUPITER 2 capacity ramp와 broadband subscriber growth가 EBITDA를 크게 높일 것이라고 봤다. Satellite broadband peers 대비 8x는 보수적이고 strategic spectrum/LEO stakes는 공짜 option으로 봤다.

**이 주장이 성립하려면**

multiple+execution

**사전 반증조건**

multiple compression

**실제 결과**

주가 반토막.

**정량적 괴리**

2018말 $29.76(-47%), 2019말 $43.31. $79.12 target 미달.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

$79.12 가설은 'multiple compression'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

2018 공식 실적은 revenue 약 $2.1bn, reported EBITDA $757m, investment loss/impairment 제외 EBITDA 약 $834m, Hughes broadband subscribers 1.361m으로 operating model은 상당히 강했다. 그런데 주가는 연말 $29.76으로 반토막났다. EBITDA가 맞아도 equity multiple·CapEx·future competitive risk가 별도라는 사례다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2018말 $29.76(-47%), 2019말 $43.31. $79.12 target 미달. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 사례는 '기업실적을 맞히는 것과 주가를 맞히는 것'의 좋은 분리다. 2018 EBITDA는 오히려 thesis보다 강했지만 시장은 capital intensity와 다음 capacity cycle, competitive risk에 낮은 multiple을 줬다.

### 9. 최초 검증·반증 신호와 회피 가능성

2018-12-31 — 좋은 EBITDA에도 주가가 $29.76으로 떨어져 8x multiple/주가 bridge가 실패했음이 명확해졌다. 회피 가능성: 높음. EBITDA forecast가 맞아도 multiple이 왜 축소되는지 satellite CapEx·competition·governance 관점에서 재검증했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

사업 EBITDA 적중·주식 실패. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $56.40 | $79.12 | 2018말 $29.76 | 실패 |
| 2018 EBITDA | Hughes ~$650m 기반 | 성장 | consolidated $757m / ex items $834m | 사업 적중 |
| Broadband subs | 성장 | JUPITER 2 ramp | 2018 1.361m | 적중 |
| JUPITER 2 | $280m+ full-capacity EBITDA | 현금화 | capacity monetization 진행 | 방향 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-03-21 | VIC 아이디어 게시 | Hughes 8x EBITDA·JUPITER 2 FCF·$79 SOTP Long |
| 2018-12-31 | 최초 핵심 검증·반증 신호 | 좋은 EBITDA에도 주가가 $29.76으로 떨어져 8x multiple/주가 bridge가 실패했음이 명확해졌다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2018말 $29.76(-47%), 2019말 $43.31. $79.12 target 미달. |

### Failure / Success Anatomy

- **근본 오류:** 자산/EBITDA를 full-cycle CapEx·경쟁·launch duration·실현확률 없이 equity value로 직접 연결
- **최초 검증·반증 신호:** 2018-12-31 — 좋은 EBITDA에도 주가가 $29.76으로 떨어져 8x multiple/주가 bridge가 실패했음이 명확해졌다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 높음. EBITDA forecast가 맞아도 multiple이 왜 축소되는지 satellite CapEx·competition·governance 관점에서 재검증했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2018-03-21 원문](https://www.valueinvestorsclub.com/idea/ECHOSTAR_CORP/5664178893) — Value Investors Club, 2018-03-21. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:bc87a11d-0403-49c7-89c9-99e3fa1c5d37 -->
## 7. 2019-11-18 — Post-separation Hughes broadband·$60 Long

### 결론부터

**종합판정: 치명적 실패.** 가장 큰 오류는 기술 substitute의 timeline을 '현재 economics가 안 좋아 보인다'는 이유로 5~20년 뒤로 밀어낸 것이다. 신규 경쟁자는 incumbent의 현재 unit economics를 복제할 필요 없이 다른 architecture·capital source로 진입할 수 있다. launch delay까지 겹쳐 capacity growth도 늦었다.

**주가·증권 결과:** 2020말 $21.19, 2021말 $26.35, 2022말 $16.68. $60 target 실패.

**Thesis / Process 점수:** 4 / 4.5

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

### 5. 밸류에이션과 기대수익의 연결

Hughes가 약 5.5~6x EBITDA로 peers 7~8x보다 할인됐다고 보고 2020말 약 $60, 대략 45% upside. Satellite investment 때문에 FCF가 2021 전까지 얇다는 점은 인정. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Post-separation clarity — 부분 · 논지 비중 18%

**당시 주장**

자산이전 뒤 Hughes quality가 더 잘 보인다.

**당시 근거**

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

**이 주장이 성립하려면**

core disclosure/earnings 안정

**사전 반증조건**

competition worsens

**실제 결과**

구조는 단순해졌으나 business challenge 확대.

**정량적 괴리**

주가 / $41~43 / ~$60 by YE2020 / 2020말 $21.19

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Post-separation clarity 가설은 'competition worsens'를 사전 반증조건으로 저장한다.

#### 2. Rural moat — 실패 · 논지 비중 18%

**당시 주장**

terrestrial 5G/FWA가 rural economics상 위협이 작다.

**당시 근거**

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

**이 주장이 성립하려면**

coverage economics 유지

**사전 반증조건**

FWA scale

**실제 결과**

FWA가 실제 대체재로 성장.

**정량적 괴리**

Multiple / 5.5~6x EBITDA / 7~8x / discount 확대/유지

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Rural moat 가설은 'FWA scale'를 사전 반증조건으로 저장한다.

#### 3. LEO threat — 치명적 실패 · 논지 비중 16%

**당시 주장**

consumer LEO 위협은 5~20년 멀다.

**당시 근거**

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

**이 주장이 성립하려면**

launch/cost/terminal constraints

**사전 반증조건**

상용서비스 빠른 확대

**실제 결과**

Starlink로 빠르게 반증.

**정량적 괴리**

JUPITER 3 / 2021/22 성장 catalyst / 적시 발사 / 2023 발사

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

LEO threat 가설은 '상용서비스 빠른 확대'를 사전 반증조건으로 저장한다.

#### 4. JUPITER3 timing — 실패 · 논지 비중 16%

**당시 주장**

다음 satellite가 성장 capacity를 제때 연다.

**당시 근거**

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

**이 주장이 성립하려면**

launch schedule 준수

**사전 반증조건**

delay

**실제 결과**

2023로 지연.

**정량적 괴리**

Competition / 5G/LEO 위협 낮음 / 5~20년 여유 / 2022 회사도 경쟁영향 인정

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

JUPITER3 timing 가설은 'delay'를 사전 반증조건으로 저장한다.

#### 5. Peer rerating — 실패 · 논지 비중 16%

**당시 주장**

5.5~6x가 7~8x로 정상화된다.

**당시 근거**

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

**이 주장이 성립하려면**

competitive profile peers와 유사

**사전 반증조건**

structural discount

**실제 결과**

미실현.

**정량적 괴리**

2020말 $21.19, 2021말 $26.35, 2022말 $16.68. $60 target 실패.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Peer rerating 가설은 'structural discount'를 사전 반증조건으로 저장한다.

#### 6. $60 target — 실패 · 논지 비중 16%

**당시 주장**

core Hughes만으로 45% upside다.

**당시 근거**

2019 DISH와의 자산이전으로 declining satellite-services 관련 business를 떼어내 Hughes broadband가 더 명확해졌고, rural broadband에는 5G가 경제적이지 않으며 LEO consumer satellite도 최소 5~20년 큰 위협이 아니라고 주장했다. JUPITER 3 launch가 다음 성장 capacity를 연다고 봤다.

**이 주장이 성립하려면**

capacity+multiple

**사전 반증조건**

competition+delay

**실제 결과**

실패.

**정량적 괴리**

2020말 $21.19, 2021말 $26.35, 2022말 $16.68. $60 target 실패.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

$60 target 가설은 'competition+delay'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

핵심 경쟁가정이 빠르게 틀렸다. Starlink가 2020년대 초 소비자 LEO broadband를 상용화했고 미국 fixed wireless도 빠르게 확장됐다. EchoStar 2022 annual letter는 rural U.S.에서 새로운 경쟁환경이 사업에 영향을 줬다고 명시했고 HughesNet Fusion으로 대응했다. JUPITER 3도 2021/22 기대보다 늦은 2023년에 발사됐다. 주가는 2020말 $21.19, 2022말 $16.68로 하락했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2020말 $21.19, 2021말 $26.35, 2022말 $16.68. $60 target 실패. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가장 큰 오류는 기술 substitute의 timeline을 '현재 economics가 안 좋아 보인다'는 이유로 5~20년 뒤로 밀어낸 것이다. 신규 경쟁자는 incumbent의 현재 unit economics를 복제할 필요 없이 다른 architecture·capital source로 진입할 수 있다. launch delay까지 겹쳐 capacity growth도 늦었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-10-27 — Starlink public beta가 현실화되면서 'LEO consumer threat는 매우 멀다'는 전제가 직접 반증되기 시작했다. 회피 가능성: 매우 높음. 경쟁상품의 실제 availability와 customer adoption을 확인한 즉시 7~8x peer multiple 가정을 폐기했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

치명적 실패. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $41~43 | ~$60 by YE2020 | 2020말 $21.19 | 치명적 실패 |
| Multiple | 5.5~6x EBITDA | 7~8x | discount 확대/유지 | 실패 |
| JUPITER 3 | 2021/22 성장 catalyst | 적시 발사 | 2023 발사 | 지연 |
| Competition | 5G/LEO 위협 낮음 | 5~20년 여유 | 2022 회사도 경쟁영향 인정 | 치명적 반증 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2019-11-18 | VIC 아이디어 게시 | Post-separation Hughes broadband·$60 Long |
| 2020-10-27 | 최초 핵심 검증·반증 신호 | Starlink public beta가 현실화되면서 'LEO consumer threat는 매우 멀다'는 전제가 직접 반증되기 시작했다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2020말 $21.19, 2021말 $26.35, 2022말 $16.68. $60 target 실패. |

### Failure / Success Anatomy

- **근본 오류:** 자산/EBITDA를 full-cycle CapEx·경쟁·launch duration·실현확률 없이 equity value로 직접 연결
- **최초 검증·반증 신호:** 2020-10-27 — Starlink public beta가 현실화되면서 'LEO consumer threat는 매우 멀다'는 전제가 직접 반증되기 시작했다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 매우 높음. 경쟁상품의 실제 availability와 customer adoption을 확인한 즉시 7~8x peer multiple 가정을 폐기했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- 1. VIC SATS 2019-11-18 원문 — Value Investors Club, 2019-11-18. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---

<!-- idea:587a12ad-fc82-44d3-8216-6ac1efb68bf4 -->
## 8. 2021-06-17 — 3.5x EV/EBITDA·JUPITER3 capacity·stealth buyback Long

### 결론부터

**종합판정: 저평가 논지보다 경쟁/launch duration이 압도.** Capacity constrained라는 진단만 보고 '새 capacity가 오면 과거 demand curve가 복원된다'고 가정했다. 공급병목이 해소되는 사이 경쟁환경이 바뀌면 이전 waitlist/demand는 그대로 돌아오지 않는다. 낮은 EV/EBITDA는 replacement CapEx와 strategic uncertainty를 반영할 수 있다.

**주가·증권 결과:** 2021말 $26.35, 2022말 $16.68, 2023말 $16.57. 평가기준일까지 실패.

**Thesis / Process 점수:** 6.8 / 7.4

### 1. 무슨 기업인가

EchoStar는 2008년 DISH Network에서 분사될 당시 set-top box(STB) 기술, SlingMedia, 위성 및 fixed satellite services(FSS), 암호화 JV, 전략투자와 대규모 현금을 보유한 복합 위성·미디어 기술 회사였다. 이후 회사의 실체는 여러 번 바뀌었다. 2011년 Hughes Communications를 인수하면서 소비자·기업용 위성 broadband가 중심이 됐고, 2017년 DISH와의 자산교환으로 set-top-box 관련 사업을 넘기면서 Hughes와 위성통신 중심으로 더 순수해졌다. 2019년에도 일부 DISH 관련 자산을 이전해 구조를 단순화했다. HughesNet은 대형 GEO 위성(JUPITER 계열)의 고정비를 먼저 투자한 뒤 가입자에게 월 broadband 요금을 받는 사업이므로 satellite capacity utilization, 가입자당 revenue, churn, 신규위성 launch timing이 economics를 좌우한다. GEO satellite는 발사 전 수년간 CapEx를 집행하고 launch 뒤 수년간 capacity를 판매해 투자금을 회수하는 장기 duration 사업이다. 2023년 JUPITER 3 발사와 2023년 말 DISH와의 합병으로 다시 기업구조가 크게 바뀌었다. 핵심 KPI는 Hughes broadband subscribers, ARPU, consumer/enterprise service revenue, satellite utilization, adjusted EBITDA, satellite CapEx와 launch schedule, FCF, net cash/debt, spectrum·strategic asset monetization이다.

### 2. 산업 가치사슬과 돈의 흐름

EchoStar의 가치사슬은 시기별로 다르다. 초기 STB는 DISH·방송사업자에게 하드웨어와 기술을 판매하고 상대적으로 낮은 투하자본으로 pre-tax profit을 냈다. FSS는 위성을 발사한 뒤 cable/telco/government/corporate customers에게 transponder capacity를 장기계약으로 임대해 높은 incremental margin을 얻는다. Hughes consumer broadband는 GEO satellite capacity를 가정·기업에 월 구독료로 판매하는데, 한 위성의 capacity가 차면 신규 subscriber를 받을 수 없어 launch 전후로 성장률이 계단식으로 움직인다. 그래서 EBITDA는 좋아 보여도 다음 위성의 제작·발사 CapEx가 먼저 나가 FCF가 얇을 수 있다. Spectrum·JV·strategic investments는 큰 optionality가 될 수 있지만, 실제 license·buyer·financing·regulatory path가 없으면 현금과 동일하게 더하면 안 된다.

### 3. 경쟁우위·경쟁구도·핵심 지표

EchoStar의 장점은 Charlie Ergen의 자본배분·위성산업 경험, Hughes의 distribution/ground network, GEO satellite capacity와 spectrum이었다. 그러나 경쟁구도는 크게 바뀌었다. 초기에는 rural broadband의 terrestrial 대체재가 약했지만 이후 fixed wireless와 Starlink 등 LEO constellation이 latency·speed·capacity 측면에서 강한 대체재가 됐다. 따라서 'rural에는 위성밖에 없다'는 가정은 시간이 지나며 약해졌다. 핵심은 장부상 위성·spectrum 가치가 아니라 해당 자산이 가입자·ARPU·FCF로 얼마나 빨리 변환되는지다.

### 4. 당시 VIC 원문과 핵심 숫자

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Equity/EV 약 $2.4bn, cash와 borrowings가 비슷하고 run-rate EBITDA $700m+라 약 3.5x EV/EBITDA. Q1 2021 revenue +4%, EBITDA +25%; JUPITER3 이후 100Mbps product와 subscriber growth를 기대. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Capacity constraint — 부분 실패 · 논지 비중 18%

**당시 주장**

subscriber slowdown은 demand가 아니라 capacity 부족이다.

**당시 근거**

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

**이 주장이 성립하려면**

waitlist/demand persists

**사전 반증조건**

competitive alternatives absorb demand

**실제 결과**

경쟁이 빠르게 대체.

**정량적 괴리**

EV/EBITDA / ~3.5x / rerating / 2022/23 주가 $16대

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Capacity constraint 가설은 'competitive alternatives absorb demand'를 사전 반증조건으로 저장한다.

#### 2. JUPITER3 — 실패 · 논지 비중 18%

**당시 주장**

새 위성이 growth를 재가속한다.

**당시 근거**

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

**이 주장이 성립하려면**

timely launch

**사전 반증조건**

delay

**실제 결과**

2023로 지연.

**정량적 괴리**

Q1 2021 / Revenue +4%, EBITDA +25% / momentum / capacity constrained

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

JUPITER3 가설은 'delay'를 사전 반증조건으로 저장한다.

#### 3. 3.5x cheap — 실패 · 논지 비중 16%

**당시 주장**

$700m+ EBITDA 대비 3.5x는 지나치게 싸다.

**당시 근거**

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

**이 주장이 성립하려면**

EBITDA durable/FCF conversion

**사전 반증조건**

competitive/capex discount

**실제 결과**

rerating 미실현.

**정량적 괴리**

JUPITER3 / late 2022 / 100Mbps/성장 / 2023 launch

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

3.5x cheap 가설은 'competitive/capex discount'를 사전 반증조건으로 저장한다.

#### 4. Buyback/insider — 부분 실패 · 논지 비중 16%

**당시 주장**

insider buying과 stealth buyback이 signal이다.

**당시 근거**

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

**이 주장이 성립하려면**

capital return persists

**사전 반증조건**

cash needed for capex

**실제 결과**

주가 성과를 방어 못함.

**정량적 괴리**

기업구조 / standalone SATS / value unlock / 2023-12 DISH merger

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Buyback/insider 가설은 'cash needed for capex'를 사전 반증조건으로 저장한다.

#### 5. Spectrum option — 실패 · 논지 비중 16%

**당시 주장**

S-band spin이 추가가치다.

**당시 근거**

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

**이 주장이 성립하려면**

transaction

**사전 반증조건**

no crystallization

**실제 결과**

핵심 payoff 아님.

**정량적 괴리**

2021말 $26.35, 2022말 $16.68, 2023말 $16.57. 평가기준일까지 실패.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Spectrum option 가설은 'no crystallization'를 사전 반증조건으로 저장한다.

#### 6. Standalone value — 실패 · 논지 비중 16%

**당시 주장**

Hughes standalone value가 주가에 반영된다.

**당시 근거**

JUPITER2가 capacity constrained라 subscriber growth가 막혔을 뿐 demand가 약한 것이 아니며, late-2022 JUPITER3가 병목을 풀어줄 것이라고 봤다. 높은 EBITDA 대비 저multiple, insider purchase와 stealth buyback, S-band spectrum spin optionality가 안전마진이라고 주장했다.

**이 주장이 성립하려면**

structure stable

**사전 반증조건**

DISH recombination

**실제 결과**

2023 merger로 thesis 종결.

**정량적 괴리**

2021말 $26.35, 2022말 $16.68, 2023말 $16.57. 평가기준일까지 실패.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Standalone value 가설은 'DISH recombination'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

JUPITER3 launch는 2023으로 늦어졌고 기다리는 동안 Starlink/FWA 경쟁이 강해졌다. 2022 EchoStar는 새로운 rural competition 영향을 공식적으로 언급했고 Fusion product를 도입했다. 2023 JUPITER3는 성공적으로 발사됐지만 그해 말 DISH와 합병이 완료돼 원 standalone thesis 자체가 사라졌다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2021말 $26.35, 2022말 $16.68, 2023말 $16.57. 평가기준일까지 실패. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

Capacity constrained라는 진단만 보고 '새 capacity가 오면 과거 demand curve가 복원된다'고 가정했다. 공급병목이 해소되는 사이 경쟁환경이 바뀌면 이전 waitlist/demand는 그대로 돌아오지 않는다. 낮은 EV/EBITDA는 replacement CapEx와 strategic uncertainty를 반영할 수 있다.

### 9. 최초 검증·반증 신호와 회피 가능성

2022-03-31 — JUPITER3 일정이 늦어지고 경쟁환경 악화가 뚜렷해져 late-2022 capacity-reset 가정이 약화됐다. 회피 가능성: 높음. launch delay 한 분기마다 market-share/competitive state를 새로 모델링했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

저평가 논지보다 경쟁/launch duration이 압도. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| EV/EBITDA | ~3.5x | rerating | 2022/23 주가 $16대 | 실패 |
| Q1 2021 | Revenue +4%, EBITDA +25% | momentum | capacity constrained | 초기 적중 |
| JUPITER3 | late 2022 | 100Mbps/성장 | 2023 launch | 지연 |
| 기업구조 | standalone SATS | value unlock | 2023-12 DISH merger | 전제변경 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-06-17 | VIC 아이디어 게시 | 3.5x EV/EBITDA·JUPITER3 capacity·stealth buyback Long |
| 2022-03-31 | 최초 핵심 검증·반증 신호 | JUPITER3 일정이 늦어지고 경쟁환경 악화가 뚜렷해져 late-2022 capacity-reset 가정이 약화됐다. |
| 2011-06-08 | Hughes acquisition | SATS가 satellite broadband 중심으로 이동 |
| 2017-02-28 | DISH asset swap | set-top-box 관련 자산을 이전해 구조 단순화 |
| 2023-07-28 | JUPITER 3 launch | 지연된 next-generation capacity가 실제 궤도 진입 |
| 2024-01-31 | 고정 평가기준일 | 2021말 $26.35, 2022말 $16.68, 2023말 $16.57. 평가기준일까지 실패. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating mechanism과 binary funding risk를 구분
- **최초 검증·반증 신호:** 2022-03-31 — JUPITER3 일정이 늦어지고 경쟁환경 악화가 뚜렷해져 late-2022 capacity-reset 가정이 약화됐다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 높음. launch delay 한 분기마다 market-share/competitive state를 새로 모델링했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** spin_dislocation; satellite_capacity_leverage; SOTP; asset_simplification
- **실패·주의 패턴:** asset_value_without_crystallization; replacement_capex; launch_delay; LEO_FWA_disruption; option_overvaluation

### 주요 근거자료

- [1. VIC SATS 2021-06-17 원문](https://www.valueinvestorsclub.com/idea/ECHOSTAR_CORP/0655709989) — Value Investors Club, 2021-06-17. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. EchoStar 2018 Results](https://www.sec.gov/Archives/edgar/data/1533758/000153375819000005/hssc123118ex-991.htm) — SEC / EchoStar, 2019-02-21. 2018 revenue 약 $2.1bn, EBITDA, Hughes broadband subscribers 1.361m 확인
- [3. EchoStar 2022 Annual Report / shareholder letter](https://www.sec.gov/Archives/edgar/data/1415404/000110465923032300/tm239414d1_ars.pdf) — SEC / EchoStar, 2023-03-08. rural U.S. 경쟁환경·HughesNet Fusion·JUPITER3 지연 확인
- [4. EchoStar and DISH merger announcement](https://www.sec.gov/Archives/edgar/data/1001082/000110465923088620/tm2323111d2_ex99-1.htm) — SEC, 2023-08-08. JUPITER3 successful launch와 DISH 재결합 발표
- [5. DISH 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1001082/000155837024004386/dish-20231231x10k.htm) — SEC, 2024-02-29. 2023-12-31 EchoStar/DISH merger completion 확인
- [6. EchoStar annual price history](https://devyara.com/en-us/nasdaq/sats/price-history/) — DevYara, 2024-01-31. 2008~2023 연말 가격경로 교차검증

---
# IRIDIUM COMMUNICATIONS INC (IRDM) — 기업과 비즈니스

## 1. 무슨 기업인가

Iridium Communications는 저궤도(LEO) 위성 constellation을 통해 전 세계 음성·데이터·IoT·항공·해상·정부 통신을 제공한다. 지상 셀룰러가 닿지 않는 바다·극지·사막·항공·원격산업 현장에서 연결성을 제공한다는 것이 핵심 customer job이다. 수익은 가입자 서비스료, U.S. government 계약, 장비판매와 engineering/support에서 나온다. 초기 Iridium이 파산했던 역사가 있어 2009년 SPAC 재상장 당시 시장은 다시 대규모 constellation 교체비용인 Iridium NEXT를 감당할 수 있는지에 큰 의문을 가졌다. 하지만 위성망이 구축된 뒤에는 추가 가입자의 service gross margin이 높고, IoT·maritime·aviation 등 소량 데이터 연결이 recurring revenue로 쌓이는 구조다. 핵심 KPI는 billable subscribers, service revenue mix, commercial vs government revenue, IoT subscribers, ARPU, service EBITDA margin, satellite replacement CapEx·financing, net leverage와 constellation life다.

## 2. 산업 가치사슬과 돈의 흐름

Iridium은 약 66기 operational LEO satellite constellation과 ground network를 유지하면서 users/device makers에게 global coverage를 판다. 장비판매는 단말기 margin을 만들지만 핵심 경제성은 recurring service revenue다. NEXT처럼 constellation 전체를 교체할 때는 수십억 달러 CapEx가 먼저 필요하므로 debt/agency-backed financing이 생존을 좌우한다. 한번 constellation과 financing이 확보되면 신규 IoT·voice/data subscribers는 상대적으로 낮은 incremental network cost로 recurring revenue를 추가할 수 있다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Iridium의 moat는 진정한 전지구 coverage, L-band spectrum, certified terminals/ecosystem, U.S. government relationship과 이미 구축된 constellation이다. 2009년 Short 논지처럼 Inmarsat handset pricing과 NEXT funding은 실제 위험이었다. 그러나 경쟁사가 단말기를 싸게 내는 것만으로 constellation coverage·mobility·government ecosystem을 복제하기 어렵다. 반대로 satellite business는 capital replacement cycle을 피할 수 없으므로 서비스 moat가 있어도 financing을 못 하면 equity가 훼손될 수 있다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2009-11-30 | Short | Long | Global LEO network·NEXT funding overhang Long | NEXT financing이 2010년 확보된 뒤 장기적으로 recurring service franchise가 크게 성장. 2023년 2.279m subscribers·$790.7m revenue까지 확대. | 장기 전설적 성공 |
| 2009-12-08 | Short | Short | NEXT funding·Inmarsat handset competition Short | 2010 NEXT financing 확보 후 장기 subscriber/service growth. Structural Short 실패. | 논점은 타당했으나 구조적 Short 실패 |

---

<!-- idea:e90bc650-4d2b-4cdf-8115-838df1ebc702 -->
## 1. 2009-11-30 — Global LEO network·NEXT funding overhang Long

### 결론부터

**종합판정: 장기 전설적 성공.** 과거 회사의 bankruptcy와 새 회사의 current unit economics를 분리하고, 가장 큰 binary risk를 NEXT funding이라고 명확히 지정한 것이 좋았다. 그 risk가 해소되는 순간 thesis confidence를 높일 수 있었다.

**주가·증권 결과:** NEXT financing이 2010년 확보된 뒤 장기적으로 recurring service franchise가 크게 성장. 2023년 2.279m subscribers·$790.7m revenue까지 확대.

**Thesis / Process 점수:** 9.5 / 9.2

### 1. 무슨 기업인가

Iridium Communications는 저궤도(LEO) 위성 constellation을 통해 전 세계 음성·데이터·IoT·항공·해상·정부 통신을 제공한다. 지상 셀룰러가 닿지 않는 바다·극지·사막·항공·원격산업 현장에서 연결성을 제공한다는 것이 핵심 customer job이다. 수익은 가입자 서비스료, U.S. government 계약, 장비판매와 engineering/support에서 나온다. 초기 Iridium이 파산했던 역사가 있어 2009년 SPAC 재상장 당시 시장은 다시 대규모 constellation 교체비용인 Iridium NEXT를 감당할 수 있는지에 큰 의문을 가졌다. 하지만 위성망이 구축된 뒤에는 추가 가입자의 service gross margin이 높고, IoT·maritime·aviation 등 소량 데이터 연결이 recurring revenue로 쌓이는 구조다. 핵심 KPI는 billable subscribers, service revenue mix, commercial vs government revenue, IoT subscribers, ARPU, service EBITDA margin, satellite replacement CapEx·financing, net leverage와 constellation life다.

### 2. 산업 가치사슬과 돈의 흐름

Iridium은 약 66기 operational LEO satellite constellation과 ground network를 유지하면서 users/device makers에게 global coverage를 판다. 장비판매는 단말기 margin을 만들지만 핵심 경제성은 recurring service revenue다. NEXT처럼 constellation 전체를 교체할 때는 수십억 달러 CapEx가 먼저 필요하므로 debt/agency-backed financing이 생존을 좌우한다. 한번 constellation과 financing이 확보되면 신규 IoT·voice/data subscribers는 상대적으로 낮은 incremental network cost로 recurring revenue를 추가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Iridium의 moat는 진정한 전지구 coverage, L-band spectrum, certified terminals/ecosystem, U.S. government relationship과 이미 구축된 constellation이다. 2009년 Short 논지처럼 Inmarsat handset pricing과 NEXT funding은 실제 위험이었다. 그러나 경쟁사가 단말기를 싸게 내는 것만으로 constellation coverage·mobility·government ecosystem을 복제하기 어렵다. 반대로 satellite business는 capital replacement cycle을 피할 수 없으므로 서비스 moat가 있어도 financing을 못 하면 equity가 훼손될 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

### 5. 밸류에이션과 기대수익의 연결

당시 약 5x EBITDA로 Inmarsat 약 9x 대비 큰 할인. NEXT funding overhang이 해소되면 peer rerating을 기대. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Global coverage — 강한 적중 · 논지 비중 18%

**당시 주장**

100% global coverage가 독특한 customer value다.

**당시 근거**

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

**이 주장이 성립하려면**

LEO network reliability

**사전 반증조건**

terrestrial/other satellite substitutes

**실제 결과**

해상·항공·IoT·government에서 지속 moat.

**정량적 괴리**

Valuation / ~5x EBITDA / peer ~9x rerating / 장기 franchise multiple 확대

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Global coverage 가설은 'terrestrial/other satellite substitutes'를 사전 반증조건으로 저장한다.

#### 2. Recurring service — 적중 · 논지 비중 18%

**당시 주장**

service mix가 equipment보다 더 중요한 recurring economics를 만든다.

**당시 근거**

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

**이 주장이 성립하려면**

subscriber growth

**사전 반증조건**

ARPU/retention collapse

**실제 결과**

2023 service 중심 모델 강화.

**정량적 괴리**

NEXT funding / $2.7bn+ 필요 / financing 확보 / 2010 $1.8bn Coface facility

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Recurring service 가설은 'ARPU/retention collapse'를 사전 반증조건으로 저장한다.

#### 3. M2M/data — 강한 적중 · 논지 비중 16%

**당시 주장**

M2M·data가 30%+ 성장 가능한 신규축이다.

**당시 근거**

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

**이 주장이 성립하려면**

device ecosystem

**사전 반증조건**

adoption stall

**실제 결과**

IoT 1.709m subs로 확대.

**정량적 괴리**

Subscribers / 초기 base / data/M2M 성장 / 2023 2.279m

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

M2M/data 가설은 'adoption stall'를 사전 반증조건으로 저장한다.

#### 4. Government — 적중 · 논지 비중 16%

**당시 주장**

U.S. government relationship이 안정성을 준다.

**당시 근거**

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

**이 주장이 성립하려면**

contract continuity

**사전 반증조건**

budget/customer loss

**실제 결과**

2023에도 정부 service/engineering 25% 규모.

**정량적 괴리**

2023 revenue / 초기 수억달러 규모 / 장기 scale / $790.7m

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Government 가설은 'budget/customer loss'를 사전 반증조건으로 저장한다.

#### 5. NEXT funding — 강한 적중 · 논지 비중 16%

**당시 주장**

가장 큰 overhang은 funding이며 해결 가능하다.

**당시 근거**

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

**이 주장이 성립하려면**

agency-backed credit

**사전 반증조건**

financing failure

**실제 결과**

2010 Coface facility 확보.

**정량적 괴리**

NEXT financing이 2010년 확보된 뒤 장기적으로 recurring service franchise가 크게 성장. 2023년 2.279m subscribers·$790.7m revenue까지 확대.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

NEXT funding 가설은 'financing failure'를 사전 반증조건으로 저장한다.

#### 6. Peer rerating — 적중 · 논지 비중 16%

**당시 주장**

funding 해소 후 5x→peer gap 축소가 가능하다.

**당시 근거**

Iridium의 과거 Chapter 11 stigma 때문에 시장이 현재 SPAC 상장 회사를 잘못 보고 있으며, 100% global coverage와 commercial/government customer base가 강한 recurring service economics를 만든다고 봤다. Commercial service 42%, U.S. government service 21%, equipment 37% mix였고 data/maritime/M2M이 30%+ 성장. 핵심 리스크는 $2.7bn+ NEXT constellation 교체 financing이었다.

**이 주장이 성립하려면**

execution

**사전 반증조건**

constellation failure

**실제 결과**

장기 가치 크게 상승.

**정량적 괴리**

NEXT financing이 2010년 확보된 뒤 장기적으로 recurring service franchise가 크게 성장. 2023년 2.279m subscribers·$790.7m revenue까지 확대.

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Peer rerating 가설은 'constellation failure'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

가장 중요한 funding risk가 2010년 프랑스 Coface 보증을 활용한 $1.8bn credit facility로 크게 해소됐다. 2023년 billable subscribers는 2.279m(+14%), revenue $790.7m(+10%), commercial service revenue $478.4m, IoT subscribers 1.709m까지 확대됐다. 장기 platform thesis가 강하게 적중했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 NEXT financing이 2010년 확보된 뒤 장기적으로 recurring service franchise가 크게 성장. 2023년 2.279m subscribers·$790.7m revenue까지 확대. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

과거 회사의 bankruptcy와 새 회사의 current unit economics를 분리하고, 가장 큰 binary risk를 NEXT funding이라고 명확히 지정한 것이 좋았다. 그 risk가 해소되는 순간 thesis confidence를 높일 수 있었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2010-10-25 — Coface 보증 $1.8bn financing close로 NEXT funding overhang이 구조적으로 낮아졌다. 회피 가능성: 해당 없음. 이후에는 constellation execution과 service adoption을 추적하면 됐다.

### 10. 최종 판정·반사실·재사용 교훈

장기 전설적 성공. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Valuation | ~5x EBITDA | peer ~9x rerating | 장기 franchise multiple 확대 | 강한 적중 |
| NEXT funding | $2.7bn+ 필요 | financing 확보 | 2010 $1.8bn Coface facility | 강한 적중 |
| Subscribers | 초기 base | data/M2M 성장 | 2023 2.279m | 강한 적중 |
| 2023 revenue | 초기 수억달러 규모 | 장기 scale | $790.7m | 강한 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2009-11-30 | VIC 아이디어 게시 | Global LEO network·NEXT funding overhang Long |
| 2010-10-25 | NEXT financing 결정 | Coface-backed financing이 funding tail을 낮춤 |
| 2019-01-11 | NEXT constellation deployment 완료 | replacement execution risk가 크게 해소 |
| 2023-12-31 | 장기 platform 결과 | 2.279m subscribers와 service 중심 economics 확인 |
| 2024-01-31 | 사업·증권 재평가 | 2009 thesis가 장기 outcome과 얼마나 일치했는지 판정 |
| 2024-01-31 | 고정 평가기준일 | NEXT financing이 2010년 확보된 뒤 장기적으로 recurring service franchise가 크게 성장. 2023년 2.279m subscribers·$790.7m revenue까지 확대. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 operating mechanism과 binary funding risk를 구분
- **최초 검증·반증 신호:** 2010-10-25 — Coface 보증 $1.8bn financing close로 NEXT funding overhang이 구조적으로 낮아졌다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 해당 없음. 이후에는 constellation execution과 service adoption을 추적하면 됐다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** global_network; recurring_service; IoT_scale; government_contract; financed_replacement
- **실패·주의 패턴:** funding_probability_error; equipment_overweight

### 주요 근거자료

- 1. VIC IRDM 2009-11-30 원문 — Value Investors Club, 2009-11-30. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Iridium NEXT financing / 2010 filing](https://www.sec.gov/Archives/edgar/data/1418819/000119312510241235/d8k.htm) — SEC, 2010-10-25. $1.8bn Coface-backed financing close 확인
- [3. Iridium 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/1418819/000114420413012838/v329740_10k.htm) — SEC, 2013-03-01. NEXT fixed-price contract·financing structure 확인
- [4. Iridium 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1418819/000141881924000008/irdm-20231231.htm) — SEC, 2024-02-15. 2023 subscribers 2.279m, revenue $790.7m, service mix·IoT 확인
- [5. Iridium historical price context](https://www.financecharts.com/stocks/IRDM/summary/price) — FinanceCharts, 2024-01-31. 2009~2024 가격경로 교차검증

---

<!-- idea:c1b5a902-d8f4-4cc8-bb82-0b59b3ba2446 -->
## 2. 2009-12-08 — NEXT funding·Inmarsat handset competition Short

### 결론부터

**종합판정: 논점은 타당했으나 구조적 Short 실패.** 당시 가장 취약한 financing point와 제품가격 격차를 정확히 찾았지만, equipment margin을 franchise economics의 중심으로 과대평가했다. 네트워크는 terminal ASP보다 global service coverage와 recurring subscription에서 가치가 커질 수 있었다.

**주가·증권 결과:** 2010 NEXT financing 확보 후 장기 subscriber/service growth. Structural Short 실패.

**Thesis / Process 점수:** 6.8 / 7.4

### 1. 무슨 기업인가

Iridium Communications는 저궤도(LEO) 위성 constellation을 통해 전 세계 음성·데이터·IoT·항공·해상·정부 통신을 제공한다. 지상 셀룰러가 닿지 않는 바다·극지·사막·항공·원격산업 현장에서 연결성을 제공한다는 것이 핵심 customer job이다. 수익은 가입자 서비스료, U.S. government 계약, 장비판매와 engineering/support에서 나온다. 초기 Iridium이 파산했던 역사가 있어 2009년 SPAC 재상장 당시 시장은 다시 대규모 constellation 교체비용인 Iridium NEXT를 감당할 수 있는지에 큰 의문을 가졌다. 하지만 위성망이 구축된 뒤에는 추가 가입자의 service gross margin이 높고, IoT·maritime·aviation 등 소량 데이터 연결이 recurring revenue로 쌓이는 구조다. 핵심 KPI는 billable subscribers, service revenue mix, commercial vs government revenue, IoT subscribers, ARPU, service EBITDA margin, satellite replacement CapEx·financing, net leverage와 constellation life다.

### 2. 산업 가치사슬과 돈의 흐름

Iridium은 약 66기 operational LEO satellite constellation과 ground network를 유지하면서 users/device makers에게 global coverage를 판다. 장비판매는 단말기 margin을 만들지만 핵심 경제성은 recurring service revenue다. NEXT처럼 constellation 전체를 교체할 때는 수십억 달러 CapEx가 먼저 필요하므로 debt/agency-backed financing이 생존을 좌우한다. 한번 constellation과 financing이 확보되면 신규 IoT·voice/data subscribers는 상대적으로 낮은 incremental network cost로 recurring revenue를 추가할 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Iridium의 moat는 진정한 전지구 coverage, L-band spectrum, certified terminals/ecosystem, U.S. government relationship과 이미 구축된 constellation이다. 2009년 Short 논지처럼 Inmarsat handset pricing과 NEXT funding은 실제 위험이었다. 그러나 경쟁사가 단말기를 싸게 내는 것만으로 constellation coverage·mobility·government ecosystem을 복제하기 어렵다. 반대로 satellite business는 capital replacement cycle을 피할 수 없으므로 서비스 moat가 있어도 financing을 못 하면 equity가 훼손될 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

NEXT 최소 $2.7bn과 2014 earliest launch, handset economics/competition을 근거로 current equity가 funding·margin risk를 과소평가한다고 봄. 사후에는 satellite/network assets → subscribers/utilization → EBITDA → replacement/growth CapEx → FCF → corporate action/financing → equity value 순으로 다시 연결했다.

### 투자논지를 구성한 핵심 주장

#### 1. Funding gap — 실패 · 논지 비중 18%

**당시 주장**

NEXT financing gap이 equity를 훼손한다.

**당시 근거**

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

**이 주장이 성립하려면**

capital markets closed

**사전 반증조건**

Coface/project finance unavailable

**실제 결과**

financing 확보.

**정량적 괴리**

NEXT / 최소 $2.7bn / funding crisis / 2010 $1.8bn credit + project finance

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Funding gap 가설은 'Coface/project finance unavailable'를 사전 반증조건으로 저장한다.

#### 2. Launch timing — 위험은 있었으나 생존 · 논지 비중 18%

**당시 주장**

2014 earliest NEXT launch가 긴 execution risk다.

**당시 근거**

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

**이 주장이 성립하려면**

legacy constellation deterioration

**사전 반증조건**

replacement execution

**실제 결과**

NEXT 구축 완료.

**정량적 괴리**

Handset / wholesale ~$1,000 / Inmarsat $500~600 pressure / service franchise가 더 중요해짐

**분석 오류·핵심**

핵심 causal chain이 실제 financing 또는 operating data로 확인됐다.

**재사용할 교훈**

Launch timing 가설은 'replacement execution'를 사전 반증조건으로 저장한다.

#### 3. Handset margin — 실패 · 논지 비중 16%

**당시 주장**

높은 handset margin이 경쟁에 취약하다.

**당시 근거**

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

**이 주장이 성립하려면**

equipment profit key

**사전 반증조건**

service mix grows

**실제 결과**

service가 더 핵심이 됐다.

**정량적 괴리**

Service mix / underweighted / margin pressure / 2023 commercial service $478.4m

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Handset margin 가설은 'service mix grows'를 사전 반증조건으로 저장한다.

#### 4. Inmarsat price — 실패 · 논지 비중 16%

**당시 주장**

저가 terminal이 Iridium share를 뺏는다.

**당시 근거**

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

**이 주장이 성립하려면**

coverage/function comparable

**사전 반증조건**

Iridium coverage premium persists

**실제 결과**

global niche 유지.

**정량적 괴리**

Subscribers / 성장 의문 / competitive erosion / 2023 2.279m

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Inmarsat price 가설은 'Iridium coverage premium persists'를 사전 반증조건으로 저장한다.

#### 5. Bankruptcy stigma — 실패 · 논지 비중 16%

**당시 주장**

과거 파산이 재발할 수 있다.

**당시 근거**

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

**이 주장이 성립하려면**

funding+margin shock

**사전 반증조건**

stable contracts

**실제 결과**

재발 안 함.

**정량적 괴리**

2010 NEXT financing 확보 후 장기 subscriber/service growth. Structural Short 실패.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Bankruptcy stigma 가설은 'stable contracts'를 사전 반증조건으로 저장한다.

#### 6. Short payoff — 실패 · 논지 비중 16%

**당시 주장**

funding/competition이 valuation collapse를 만든다.

**당시 근거**

SPAC로 재상장된 Iridium은 새 constellation에 최소 $2.7bn을 써야 하고 자금조달이 확정되지 않았다고 지적했다. EBITDA의 약 35%가 handset sales에서 나오며, Inmarsat이 $500~600 수준 단말기를 출시하면 Iridium의 wholesale ~$1,000/retail $1,200~1,500 handset margin이 압박받을 것이라고 봤다.

**이 주장이 성립하려면**

두 risk 동시 현실화

**사전 반증조건**

funding resolves

**실제 결과**

장기 구조적 실패.

**정량적 괴리**

2010 NEXT financing 확보 후 장기 subscriber/service growth. Structural Short 실패.

**분석 오류·핵심**

asset/EBITDA의 현재가치를 launch·competition·replacement CapEx의 state-dependent distribution 없이 주가로 연결했다.

**재사용할 교훈**

Short payoff 가설은 'funding resolves'를 사전 반증조건으로 저장한다.

### 6. 실제 사업의 시간순 전개

Risk identification은 맞았지만 outcome probability가 틀렸다. Iridium은 2010년 $1.8bn Coface-backed financing을 확보했고 NEXT constellation 구축을 완료했다. 장기 value는 handset margin보다 recurring service·IoT·government relationship에서 나왔다. 2023 subscribers 2.279m과 revenue $790.7m으로 확대됐다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2010 NEXT financing 확보 후 장기 subscriber/service growth. Structural Short 실패. Operating execution과 valuation multiple, launch/corporate-action 경로를 별도로 판정한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

당시 가장 취약한 financing point와 제품가격 격차를 정확히 찾았지만, equipment margin을 franchise economics의 중심으로 과대평가했다. 네트워크는 terminal ASP보다 global service coverage와 recurring subscription에서 가치가 커질 수 있었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2010-10-25 — Coface-backed financing close로 Short의 가장 중요한 bankruptcy/funding premise가 직접 반증됐다. 회피 가능성: 매우 높음. financing이 확보된 시점에 thesis를 폐기하거나 handset competition만 남은 작은 Short로 재평가했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

논점은 타당했으나 구조적 Short 실패. Satellite 투자에서는 EBITDA가 아니라 full-cycle replacement CapEx 후 owner earnings와 기술대체 속도를 우선한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| NEXT | 최소 $2.7bn | funding crisis | 2010 $1.8bn credit + project finance | 반증 |
| Handset | wholesale ~$1,000 | Inmarsat $500~600 pressure | service franchise가 더 중요해짐 | 과대 |
| Service mix | underweighted | margin pressure | 2023 commercial service $478.4m | Short 실패 |
| Subscribers | 성장 의문 | competitive erosion | 2023 2.279m | 반증 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2009-12-08 | VIC 아이디어 게시 | NEXT funding·Inmarsat handset competition Short |
| 2010-10-25 | NEXT financing 결정 | Coface-backed financing이 funding tail을 낮춤 |
| 2019-01-11 | NEXT constellation deployment 완료 | replacement execution risk가 크게 해소 |
| 2023-12-31 | 장기 platform 결과 | 2.279m subscribers와 service 중심 economics 확인 |
| 2024-01-31 | 사업·증권 재평가 | 2009 thesis가 장기 outcome과 얼마나 일치했는지 판정 |
| 2024-01-31 | 고정 평가기준일 | 2010 NEXT financing 확보 후 장기 subscriber/service growth. Structural Short 실패. |

### Failure / Success Anatomy

- **근본 오류:** 자산/EBITDA를 full-cycle CapEx·경쟁·launch duration·실현확률 없이 equity value로 직접 연결
- **최초 검증·반증 신호:** 2010-10-25 — Coface-backed financing close로 Short의 가장 중요한 bankruptcy/funding premise가 직접 반증됐다.
- **당시 알 수 있었나:** satellite launch schedule, capacity utilization, subscriber additions, service revenue, EBITDA, capital spending, financing terms, competitor service availability와 corporate actions는 공시로 추적 가능했다.
- **피할 수 있었나:** 매우 높음. financing이 확보된 시점에 thesis를 폐기하거나 handset competition만 남은 작은 Short로 재평가했어야 한다.
- **반사실 질문:** 위성/스펙트럼 자산가치가 높더라도 replacement CapEx·launch delay·새로운 network substitute를 반영한 full-cycle FCF와 실제 monetization probability는 얼마인가?
- **성공 패턴:** global_network; recurring_service; IoT_scale; government_contract; financed_replacement
- **실패·주의 패턴:** funding_probability_error; equipment_overweight

### 주요 근거자료

- 1. VIC IRDM 2009-12-08 원문 — Value Investors Club, 2009-12-08. 원 SQL description에서 당시 thesis·valuation·risk·방향 복원
- [2. Iridium NEXT financing / 2010 filing](https://www.sec.gov/Archives/edgar/data/1418819/000119312510241235/d8k.htm) — SEC, 2010-10-25. $1.8bn Coface-backed financing close 확인
- [3. Iridium 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/1418819/000114420413012838/v329740_10k.htm) — SEC, 2013-03-01. NEXT fixed-price contract·financing structure 확인
- [4. Iridium 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1418819/000141881924000008/irdm-20231231.htm) — SEC, 2024-02-15. 2023 subscribers 2.279m, revenue $790.7m, service mix·IoT 확인
- [5. Iridium historical price context](https://www.financecharts.com/stocks/IRDM/summary/price) — FinanceCharts, 2024-01-31. 2009~2024 가격경로 교차검증

---

# 배치 공통 학습

1. **Satellite EBITDA에는 replacement CapEx라는 숨은 경제적 비용이 있다.**
2. **SOTP 자산을 cash처럼 더하지 않는다.** Spectrum·satellite·JV는 buyer·regulation·tax·시간이 있어야 현금이 된다.
3. **Capacity-constrained demand는 새 capacity가 도착할 때까지 경쟁환경이 그대로라는 보장이 없다.**
4. **Launch delay는 단순 timing error가 아니다.** 경쟁사가 그 시간 동안 고객을 선점할 수 있다.
5. **기술대체의 base rate는 incumbent economics만 보고 판단하지 않는다.** Starlink처럼 다른 architecture가 cost curve를 바꿀 수 있다.
6. **Iridium 사례처럼 funding binary를 명확히 잡으면 이후 정보가 thesis probability를 크게 갱신할 수 있다.**
7. **Equipment margin보다 recurring network service가 장기 franchise의 본질일 수 있다.**
