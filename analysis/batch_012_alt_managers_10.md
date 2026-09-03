# Batch 012 — Apollo·KKR·Blackstone 10건

평가기준일: 2024-01-31

분석일: 2026-09-03

대상: Apollo 5건·KKR 4건·Blackstone 1건

## 결론부터

이번 10건의 실제 방향은 **모두 Long**이며 10건 모두 2024-01-31 가격 기준 성공했다. 공통 승리공식은 ‘총 AUM이 크다’가 아니라 **오래 잠긴 fee-paying capital, 성장하는 FRE, 할인된 balance sheet와 carry option을 분리해 샀다**는 것이다. 가장 큰 장기 변화는 Apollo의 Athene, KKR의 Global Atlantic처럼 보험부채가 영구자본과 origination 수요를 제공한 점이다. 동시에 이는 asset-light 운용사에 신용·ALM·규제자본 위험을 더했으므로 같은 배수를 적용하면 안 된다.

| 기업 | 건수 | 가장 강한 성공 | 남는 핵심 위험 | 반복 학습 |
|---|---:|---|---|---|
| Apollo | 5 | Athene 영구자본·2022 합병·FRE/SRE 분리 | 보험 신용·ALM·복합기업 할인 | FRE와 SRE를 다른 자본비용으로 평가 |
| KKR | 4 | 순자산+FRE 하방, carry·신규전략 옵션 | balance sheet·보험 book의 회수 haircut | AUM보다 FPAUM·FRE/주·희석 확인 |
| Blackstone | 1 | SOTP·ENI·DDM 삼각검증 | 미실현 carry와 exit cycle | 분배와 실현수익으로 ENI 검증 |

> 데이터 경고: 원 SQL의 `is_short`는 10건 중 7건에서 실제 추천 방향과 반대다. Apollo 2014·2020·2021·2022, KKR 2016·2022, Blackstone 2014는 SQL상 Short지만 본문·기대수익·증권은 명백한 Long이다. 원본 flag는 감사추적용으로 보존하고 분석 방향만 교정했다. 또 2001~2007년 티커 APO는 **American Community Properties**로 현 Apollo와 다른 기업이어서 이 배치에서 제외했다.

---

# Apollo Global Management (APO) — 기업과 비즈니스

Apollo Global Management은 사모펀드 하나가 아니라 자산운용(Asset Management)과 Athene 중심의 퇴직연금·보험(Retirement Services)을 결합한 대체자산 플랫폼이다. 운용부문은 yield·hybrid·equity 전략에서 관리보수와 성과보수(carry)를 받고, Athene은 연금보험료와 재보험 부채를 장기 자금원으로 조달해 Apollo가 발굴한 투자등급 사모신용·asset-backed 자산 등에 투자한 스프레드를 번다. 따라서 돈 버는 구조는 ① fee-paying AUM×보수율에서 비용을 뺀 FRE, ② 보험자산 수익률에서 계약자 원가·헤지·운영비를 뺀 SRE, ③ 펀드 성과에서 발생하는 carry, ④ 대차대조표 투자수익이다. Athene은 환매가 거의 없는 영구자본과 대규모 origination 수요를 주지만, 상장주주가 단순 asset-light 운용사만 소유하는 것이 아니라 금리·신용·ALM·규제·보험자본 위험도 함께 부담한다. 핵심 지표는 총 AUM보다 fee-generating AUM, FRE margin, 순유입, origination, Athene spread·RBC와 신용손실, 주당 ANI 및 실제 자사주 상쇄다.

## 돈을 버는 구조

- 반복이익: fee-paying AUM × 보수율 − 보상·운영비 = FRE
- 성과이익: 펀드수익이 hurdle을 넘고 실제 회수될 때 carry 발생
- 자체자본: balance-sheet 투자수익과 신규전략 seed, 단 할인·세금·부채 필요
- 보험자본: APO의 Athene·KKR의 Global Atlantic은 장기자금과 spread를 제공하지만 신용·ALM·규제자본 위험 동반

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2014-06-22 | Short | Long | 가치투자형 대체운용사와 Athene 영구자본 롱 | $27대→$100.40; 가격만 약 +260%대, 분배 제외 | 매우 성공 |
| 2017-08-15 | Long | Long | Fund IX FRE step-up와 $42 SOTP 롱 | $29.53 월말 근사→$100.40; 가격 약 +240%, 분배 제외 | 매우 성공 |
| 2020-06-10 | Short | Long | look-through 10.7배와 Athene 옵션 롱 | $49.92 월말 근사→$100.40; 가격 약 +101%, 배당 제외 | 성공 |
| 2021-11-29 | Short | Long | Athene 합병 복잡성 할인과 $100+ 롱 | $70.78 월말→$100.40; 가격 약 +42%, 배당 제외 | 성공 |
| 2022-09-10 | Short | Long | FRE 20배·SRE 10배의 post-merger 롱 | $46.50 월말 근사→$100.40; 가격 약 +116%, 배당 제외 | 매우 성공 |

## 1. 2014-06-22 — 가치투자형 대체운용사와 Athene 영구자본 롱

### 원 투자논지

AUM $158bn 중 credit $101bn·PE $48bn·real estate $9bn인 Apollo를 ‘레버리지 바이아웃 한 종류’가 아니라 가치·distressed 철학의 다전략 운용사로 봤다. PE의 역사적 gross/net IRR 39%/26%, Athene의 약 $49bn 영구자본, sole-sponsored deal 역량이 장기 AUM·분배를 키운다고 주장했다. 보수적 펀드수익률(PE 15%·credit 6%·real estate 4%)에서도 연평균 incentive income $911m, management income $171m과 순투자자산 $5.62/주를 합산해 가격이 싸다고 봤다.

### 논지를 구성한 핵심 주장

#### 1. 운용성과 — 적중

**핵심 주장:** value/distressed 규율과 강한 PE track record가 재모금을 만든다.

**이 주장이 성립하려면:** 후속 빈티지가 벤치마크를 이기고 LP가 재약정

**사전 반증조건:** 두 빈티기 연속 저성과·fund size 축소

**실제 결과:** AUM과 flagship 규모가 장기 확대됐다.

#### 2. Athene 영구자본 — 적중

**핵심 주장:** $49bn Athene 자산이 안정적 credit fee base다.

**이 주장이 성립하려면:** 보험부채가 안정적이고 origination 수익이 자본비용을 상회

**사전 반증조건:** 해약·신용손실·자본부족으로 외부자본 필요

**실제 결과:** Athene은 완전 합병돼 SRE와 대규모 영구자본을 제공했다.

#### 3. 분배 경제성 — 부분~적중

**핵심 주장:** 보수적 수익률에서도 관리보수와 carry가 큰 현금분배를 만든다.

**이 주장이 성립하려면:** carry 실현과 FRE가 cycle 전체에서 현금화

**사전 반증조건:** 평가이익은 늘지만 실현·분배가 장기 부진

**실제 결과:** 분배는 변동했으나 이익·주가는 크게 증가했다.

#### 4. 싼 청구권 — 적중

**핵심 주장:** 전통운용사보다 빠른 성장·높은 margin인데 낮은 배수다.

**이 주장이 성립하려면:** AUM 증가가 주당 FRE/DE로 전환

**사전 반증조건:** 보상·희석이 성장 대부분 흡수

**실제 결과:** 주당가치와 가격이 크게 상승했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | AUM $158bn 중 credit $101bn·PE $48bn·real estate $9bn인 Apollo를 ‘레버리지 바이아웃 한 종류’가 아니라 가치·distressed 철학의 다전략 운용사로 봤다. PE의 역사적 gross/net IRR 39%/26%, Athene의 약 $49bn 영구자본, sole-sponsored deal 역량이 장기 AUM·분배를 키운다고 주장했다. 보수적 펀드수익률(PE 15%·credit 6%·real estate 4%)에서도 연평균 incentive income $911m, management income $171m과 순투자자산 $5.62/주를 합산해 가격이 싸다고 봤다. | Apollo는 2023년 말 AUM $651bn으로 당시의 네 배 이상이 됐고 Athene은 단순 제휴가 아니라 2022년 완전 합병돼 영구자본·origination 엔진이 됐다. 2024-01 월말 주가 $100.40은 2014년 6월 $27대 대비 약 3.6배이며 중간 분배금도 있었다. 다만 변동 배당과 carry에 의존한 원 계산보다 실제 성공은 보험·private credit 확대와 기업구조 단순화에서 더 크게 왔다. |
| 밸류에이션·청구권 | 순투자자산 $5.62/주+정상 incentive/management income SOTP | $27대→$100.40; 가격만 약 +260%대, 분배 제외 |
| 촉매·시간 | Athene AUM 성장과 신규 credit 자금유입 | 첫 확인 2015-02-27 |
| 사전 반증 | 두 빈티기 연속 저성과·fund size 축소 | 저평가된 관리보수·carry와 Athene의 전략가치를 함께 본 핵심 인과가 맞았다. 다만 Athene을 단순 asset-light AUM으로 본 시각은 합병 후 보험 대차대조표 위험을 충분히 반영하지 못했다. |

### 실제 전개와 투자 결론

Apollo는 2023년 말 AUM $651bn으로 당시의 네 배 이상이 됐고 Athene은 단순 제휴가 아니라 2022년 완전 합병돼 영구자본·origination 엔진이 됐다. 2024-01 월말 주가 $100.40은 2014년 6월 $27대 대비 약 3.6배이며 중간 분배금도 있었다. 다만 변동 배당과 carry에 의존한 원 계산보다 실제 성공은 보험·private credit 확대와 기업구조 단순화에서 더 크게 왔다.

**종합판정: 매우 성공.** 저평가된 관리보수·carry와 Athene의 전략가치를 함께 본 핵심 인과가 맞았다. 다만 Athene을 단순 asset-light AUM으로 본 시각은 합병 후 보험 대차대조표 위험을 충분히 반영하지 못했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| AUM | $158bn | 장기 성장 | $651bn FY2023 | 적중 |
| Athene AUM | 약 $49bn | 영구자본 확대 | 합병 후 핵심 SRE 엔진 | 적중 |
| 가격 | $27대 | 재평가+분배 | $100.40 | 매우 성공 |
| 구조 | LP·변동분배 | 인지도 개선 | C-corp·Athene 완전합병 | 초과 |

재사용 질문: **두 빈티기 연속 저성과·fund size 축소**

## 2. 2017-08-15 — Fund IX FRE step-up와 $42 SOTP 롱

### 원 투자논지

AUM $230bn+, fee-generating AUM $160bn+인 Apollo를 FRE·carry·순투자자산의 세 청구권으로 나눴다. 2018 after-tax FRE $1.50/주에 17배를 적용한 $25.50, cycle-average carry $2.28/주에 6배를 적용한 $13.70, 순자산 $2.78을 합쳐 목표 $42를 계산했다. Fund IX가 연 $200m management fee를 추가하고 incremental margin 80%를 낼 것과 Athene·AGER가 영구 fee base를 확대할 것을 촉매로 봤다.

### 논지를 구성한 핵심 주장

#### 1. Fund IX FRE — 적중

**핵심 주장:** 신규 flagship이 연 $200m fee와 80% incremental margin을 더한다.

**이 주장이 성립하려면:** 약정자금이 fee-paying period에 진입

**사전 반증조건:** 활성화 지연·fee offset·비용이 증가분 흡수

**실제 결과:** FRE 규모는 장기 크게 확대됐다.

#### 2. Athene/AGER — 적중

**핵심 주장:** 보험·재보험 자금이 장기 fee-generating AUM을 만든다.

**이 주장이 성립하려면:** 안정적 liabilities와 적정 spread

**사전 반증조건:** 보험자본 훼손·mandate 해지

**실제 결과:** Athene 완전합병과 보험 AUM 확대가 현실화됐다.

#### 3. carry 정상화 — 부분~적중

**핵심 주장:** cycle carry $2.28/주에 6배만 줘도 $13.70 가치다.

**이 주장이 성립하려면:** 성과와 realization이 cycle 내 현금화

**사전 반증조건:** 공모시장 폐쇄로 수년간 실현 부재

**실제 결과:** carry는 변동했지만 core valuation에 더해졌다.

#### 4. SOTP 하방 — 적중

**핵심 주장:** FRE만으로 가격 대부분을 방어하고 나머지는 낮게 산다.

**이 주장이 성립하려면:** 보수·비용·희석 후 주당 FRE 증가

**사전 반증조건:** 보상비와 주식증가가 FRE 성장 상쇄

**실제 결과:** 목표가와 장기 가격 모두 달성했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | AUM $230bn+, fee-generating AUM $160bn+인 Apollo를 FRE·carry·순투자자산의 세 청구권으로 나눴다. 2018 after-tax FRE $1.50/주에 17배를 적용한 $25.50, cycle-average carry $2.28/주에 6배를 적용한 $13.70, 순자산 $2.78을 합쳐 목표 $42를 계산했다. Fund IX가 연 $200m management fee를 추가하고 incremental margin 80%를 낼 것과 Athene·AGER가 영구 fee base를 확대할 것을 촉매로 봤다. | 목표 $42는 2020년에 넘어섰고 2024-01 월말 $100.40으로 진입가 대비 약 +240%였다. Apollo AUM은 $651bn까지 늘고 Athene 합병으로 영구자본 논지가 강화됐다. 다만 ‘Fund IX 한 건의 고증분 margin’보다 보험·private credit 확대와 구조개편이 장기 rerating의 더 큰 원인이었다. |
| 밸류에이션·청구권 | $25.50 FRE+$13.70 carry+$2.78 순자산=$42 | $29.53 월말 근사→$100.40; 가격 약 +240%, 분배 제외 |
| 촉매·시간 | Fund IX investment period 진입과 fee step-up | 첫 확인 2018-02-01 |
| 사전 반증 | 활성화 지연·fee offset·비용이 증가분 흡수 | FRE·carry·balance sheet를 분리한 SOTP와 fee 전환 스케줄이 좋았다. Athene concentration과 계약해지 위험을 명시한 점도 강점이다. 실제 보험 위험을 단순 fee asset보다 더 깊게 stress했으면 완성도가 높았다. |

### 실제 전개와 투자 결론

목표 $42는 2020년에 넘어섰고 2024-01 월말 $100.40으로 진입가 대비 약 +240%였다. Apollo AUM은 $651bn까지 늘고 Athene 합병으로 영구자본 논지가 강화됐다. 다만 ‘Fund IX 한 건의 고증분 margin’보다 보험·private credit 확대와 구조개편이 장기 rerating의 더 큰 원인이었다.

**종합판정: 매우 성공.** FRE·carry·balance sheet를 분리한 SOTP와 fee 전환 스케줄이 좋았다. Athene concentration과 계약해지 위험을 명시한 점도 강점이다. 실제 보험 위험을 단순 fee asset보다 더 깊게 stress했으면 완성도가 높았다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 목표가 | $42 | 중기 달성 | $100.40 종착 | 성공 |
| FGAUM | $160bn+ | Fund IX 증가 | 총 AUM $651bn | 적중 |
| Fund IX fee | $200m/년 | 80% 증분마진 | FRE 대폭 확대 | 방향 적중 |
| 가격 | $29.53 | +42% | $100.40 | 매우 성공 |

재사용 질문: **활성화 지연·fee offset·비용이 증가분 흡수**

## 3. 2020-06-10 — look-through 10.7배와 Athene 옵션 롱

### 원 투자논지

headline core P/E 약 26배가 아니라 FRE·carry·Athene을 분리하면 현재 look-through 10.7배, 5년 후 5.3배라고 주장했다. 2020 post-tax FRE $1.96/주가 5년 후 $3.94가 되고 25배를 받으면 $98.56, 누적배당 약 $14로 FRE만 연 18% 수익을 제시했다. carry 약 $2/주에 6배, Athene 35% 지분을 1배 장부가 약 $14/주로 더해 현재 SOTP $78, 5년 intrinsic $150을 계산했다.

### 논지를 구성한 핵심 주장

#### 1. FRE 복리 — 부분~적중

**핵심 주장:** post-tax FRE가 $1.96에서 5년 $3.94로 두 배가 된다.

**이 주장이 성립하려면:** FPAUM 성장과 margin·주당수 방어

**사전 반증조건:** FRE/주 CAGR이 한 자릿수로 하락

**실제 결과:** AUM·FRE가 증가했으나 5년치는 기준일 미도래다.

#### 2. Athene 가치 — 적중

**핵심 주장:** 35% 지분만 $14/주 이상이며 장부가가 복리한다.

**이 주장이 성립하려면:** 보험 spread·자본이 안정

**사전 반증조건:** 신용손실·ALM 문제로 장부가 훼손

**실제 결과:** 완전합병으로 전략가치는 입증됐다.

#### 3. 구조 촉매 — 적중

**핵심 주장:** C-corp·지수편입·보험거래가 discount를 줄인다.

**이 주장이 성립하려면:** 구조 단순화가 투자자층 확대

**사전 반증조건:** 합병이 오히려 conglomerate discount 확대

**실제 결과:** 합병과 단순화 뒤 가격이 재평가됐다.

#### 4. $150 장기값 — 미판정~부분

**핵심 주장:** FRE 25배와 Athene 복리로 5년 $150이다.

**이 주장이 성립하려면:** 여러 성장가정이 동시에 실현

**사전 반증조건:** 배수 정상화 또는 보험자본비용 상승

**실제 결과:** 2024-01에는 $100.40; 아직 미판정 구간이 남는다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | headline core P/E 약 26배가 아니라 FRE·carry·Athene을 분리하면 현재 look-through 10.7배, 5년 후 5.3배라고 주장했다. 2020 post-tax FRE $1.96/주가 5년 후 $3.94가 되고 25배를 받으면 $98.56, 누적배당 약 $14로 FRE만 연 18% 수익을 제시했다. carry 약 $2/주에 6배, Athene 35% 지분을 1배 장부가 약 $14/주로 더해 현재 SOTP $78, 5년 intrinsic $150을 계산했다. | 2020년 말 AUM은 $455.5bn이었고 2023년 말 $651bn으로 증가했다. Athene 합병은 지분 discount를 없애고 보험수익을 직접 귀속시켰으며 $78 목표는 2023년에, $100.40은 2024-01에 도달했다. 다만 2024 기준에서는 $150·5년 가설을 아직 판정할 수 없고, 합병 후 보험자본을 25배 FRE와 단순 합산하는 위험은 더 커졌다. |
| 밸류에이션·청구권 | 현재 $78 SOTP; 5년 FRE $98.56+배당+carry+Athene으로 $150 | $49.92 월말 근사→$100.40; 가격 약 +101%, 배당 제외 |
| 촉매·시간 | Athene 합병 발표로 지분·governance discount 축소 | 첫 확인 2021-03-08 |
| 사전 반증 | FRE/주 CAGR이 한 자릿수로 하락 | 코어 보수이익·carry·Athene을 분해해 이중계산을 줄이고 C-corp/합병 촉매를 포착했다. 다만 25배 FRE, AUM 두 배, Athene 장부가 복리라는 세 낙관가정을 동시에 적용해 장기 목표의 가시성은 원문보다 낮다. |

### 실제 전개와 투자 결론

2020년 말 AUM은 $455.5bn이었고 2023년 말 $651bn으로 증가했다. Athene 합병은 지분 discount를 없애고 보험수익을 직접 귀속시켰으며 $78 목표는 2023년에, $100.40은 2024-01에 도달했다. 다만 2024 기준에서는 $150·5년 가설을 아직 판정할 수 없고, 합병 후 보험자본을 25배 FRE와 단순 합산하는 위험은 더 커졌다.

**종합판정: 성공.** 코어 보수이익·carry·Athene을 분해해 이중계산을 줄이고 C-corp/합병 촉매를 포착했다. 다만 25배 FRE, AUM 두 배, Athene 장부가 복리라는 세 낙관가정을 동시에 적용해 장기 목표의 가시성은 원문보다 낮다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| AUM | $455.5bn FY2020 | 5년 두 배 | $651bn FY2023 | 진행 |
| 현재 목표 | $78 | +53% | 2023년 달성 | 성공 |
| 5년 목표 | $150 | 약 30% IRR | $100.40 기준일 | 미판정 |
| Athene | 35% 지분 | 1x book 이상 | 100% 합병 | 적중 |

재사용 질문: **FRE/주 CAGR이 한 자릿수로 하락**

## 4. 2021-11-29 — Athene 합병 복잡성 할인과 $100+ 롱

### 원 투자논지

Apollo $300bn+ AUM과 Athene $150bn+를 합치는 전액주식 거래가 2022년 1월 닫히면 복잡한 이중지배구조가 사라진다고 봤다. 경영진의 5년 normalized earnings 성장 약 13%와 누적 distributable FCF $15bn을 인용했고, pro forma recurring FRE를 $2.40/주로 계산했다. 1년 forward earnings $6에 KKR의 17배를 적용해 $100+ 목표, 배당·재투자 포함 약 20% 연수익을 주장했다.

### 논지를 구성한 핵심 주장

#### 1. 합병 종결 — 정확히 적중

**핵심 주장:** 2022년 1월 합병과 dual-share collapse가 discount를 없앤다.

**이 주장이 성립하려면:** 규제승인·주주승인·운영통합

**사전 반증조건:** 종결 지연 또는 교환비율 재협상

**실제 결과:** 예정대로 2022-01-01 완료됐다.

#### 2. 13% earnings — 적중

**핵심 주장:** normalized earnings가 5년 약 13% 성장한다.

**이 주장이 성립하려면:** FRE·SRE 동시 성장과 신용손실 억제

**사전 반증조건:** 보험손실로 SRE 감소

**실제 결과:** 2023년 관련이익 성장 25%+로 초기 경로는 강했다.

#### 3. $15bn FCF — 미판정

**핵심 주장:** 5년 누적 distributable FCF가 equity 가치로 귀속된다.

**이 주장이 성립하려면:** 재투자와 buyback의 높은 수익률

**사전 반증조건:** 보험 자본투입·SBC가 현금 대부분 흡수

**실제 결과:** 2024 기준 전체 5년은 미도래다.

#### 4. rerating — 적중

**핵심 주장:** $6 EPS에 KKR 17배로 $100+가 합리적이다.

**이 주장이 성립하려면:** 구조 단순화 후 peer multiple 접근

**사전 반증조건:** 보험 conglomerate discount 지속

**실제 결과:** $100.40으로 기준일까지 목표 달성했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | Apollo $300bn+ AUM과 Athene $150bn+를 합치는 전액주식 거래가 2022년 1월 닫히면 복잡한 이중지배구조가 사라진다고 봤다. 경영진의 5년 normalized earnings 성장 약 13%와 누적 distributable FCF $15bn을 인용했고, pro forma recurring FRE를 $2.40/주로 계산했다. 1년 forward earnings $6에 KKR의 17배를 적용해 $100+ 목표, 배당·재투자 포함 약 20% 연수익을 주장했다. | 합병은 2022-01-01 완료돼 핵심 이벤트가 정확히 실현됐다. Apollo는 2023년에 FRE와 SRE 합산 성장 25% 이상, AUM $651bn을 기록했고 주가는 2024-01 $100.40으로 원 목표에 도달했다. 다만 고정배당 $1.60은 높은 payout보다 재투자형 모델로의 전환이었고, 2022년 금리·신용 우려 중 큰 drawdown을 감수해야 했다. |
| 밸류에이션·청구권 | forward earnings $6×17=$102+; 약 40% upside | $70.78 월말→$100.40; 가격 약 +42%, 배당 제외 |
| 촉매·시간 | Apollo-Athene 합병 완료 | 첫 확인 2022-01-01 |
| 사전 반증 | 종결 지연 또는 교환비율 재협상 | 거래 종결, one-share-one-vote, earnings 결합과 상대배수 rerating을 구체적 일정에 연결했다. merger가 단순 multiple 이벤트가 아니라 보험 위험의 완전 인수라는 점을 stress했어야 하지만 2024 기준 투자결론은 성공이다. |

### 실제 전개와 투자 결론

합병은 2022-01-01 완료돼 핵심 이벤트가 정확히 실현됐다. Apollo는 2023년에 FRE와 SRE 합산 성장 25% 이상, AUM $651bn을 기록했고 주가는 2024-01 $100.40으로 원 목표에 도달했다. 다만 고정배당 $1.60은 높은 payout보다 재투자형 모델로의 전환이었고, 2022년 금리·신용 우려 중 큰 drawdown을 감수해야 했다.

**종합판정: 성공.** 거래 종결, one-share-one-vote, earnings 결합과 상대배수 rerating을 구체적 일정에 연결했다. merger가 단순 multiple 이벤트가 아니라 보험 위험의 완전 인수라는 점을 stress했어야 하지만 2024 기준 투자결론은 성공이다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| AUM | $300bn+ APO | Athene 결합 | $651bn FY2023 | 적중 |
| 합병 | 예정 | 2022-01 | 2022-01-01 완료 | 적중 |
| 목표가 | $100+ | 1년 forward | $100.40 기준일 | 성공 |
| 가격 | $70.78 | 약 +40% | $100.40 | 성공 |

재사용 질문: **종결 지연 또는 교환비율 재협상**

## 5. 2022-09-10 — FRE 20배·SRE 10배의 post-merger 롱

### 원 투자논지

합병 뒤 asset-light 운용사와 보험사가 섞여 회계가 복잡해지고 금리·credit 우려가 커진 때 약 10배 2022 EPS $5.50에 거래된다고 봤다. 시장이 SRE에 5~6배만 주고 있다고 역산했으며, 경영진 2026 EPS $9+만 달성해도 현 multiple에서 5년 12%+ IRR, FRE 20배와 SRE 10배를 적용하면 약 20% IRR이라고 주장했다. 3% 배당과 초과자본·buyback을 하방으로 제시했다.

### 논지를 구성한 핵심 주장

#### 1. FRE 성장 — 적중

**핵심 주장:** FRE가 장기 두 자릿수로 성장한다.

**이 주장이 성립하려면:** FPAUM·capital solutions 확대와 비용규율

**사전 반증조건:** 순유입 둔화·margin 압박

**실제 결과:** 2023 FRE가 강하게 성장했다.

#### 2. SRE 정상화 — 적중

**핵심 주장:** Athene spread earnings에 5~6배는 과도한 할인이다.

**이 주장이 성립하려면:** credit/ALM 손실 없이 spread 유지

**사전 반증조건:** 대규모 impairments·RBC 압박

**실제 결과:** 초기 실적은 강했고 multiple도 상승했다.

#### 3. 2026 EPS — 진행

**핵심 주장:** $9+ EPS 목표가 달성 가능하다.

**이 주장이 성립하려면:** origination·보험유입·운용보수 동반성장

**사전 반증조건:** 두 부문 중 하나가 구조적으로 정체

**실제 결과:** 기준일 현재 목표연도 미도래다.

#### 4. 낮은 가격 — 적중

**핵심 주장:** 10배 안팎 EPS와 3% 배당이 forecast risk를 보상한다.

**이 주장이 성립하려면:** earnings 하방 제한·자본건전성

**사전 반증조건:** 신용손실로 book와 earnings 동시훼손

**실제 결과:** 가격이 두 배 이상 상승했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | 합병 뒤 asset-light 운용사와 보험사가 섞여 회계가 복잡해지고 금리·credit 우려가 커진 때 약 10배 2022 EPS $5.50에 거래된다고 봤다. 시장이 SRE에 5~6배만 주고 있다고 역산했으며, 경영진 2026 EPS $9+만 달성해도 현 multiple에서 5년 12%+ IRR, FRE 20배와 SRE 10배를 적용하면 약 20% IRR이라고 주장했다. 3% 배당과 초과자본·buyback을 하방으로 제시했다. | 진입 시점의 공포 뒤 Apollo는 2023년 AUM $651bn, FRE+SRE 성장 25%+를 기록했고 주가는 $46.50에서 $100.40으로 약 116% 상승했다. 보험 spread와 origination 결합은 작동했다. 다만 기준일은 2026 목표 전이므로 $9 EPS와 5년 IRR 자체는 아직 완결 판정할 수 없다. |
| 밸류에이션·청구권 | 2026 EPS $9+; FRE 20x+SRE 10x에서 약 20% 5년 IRR | $46.50 월말 근사→$100.40; 가격 약 +116%, 배당 제외 |
| 촉매·시간 | 2023년 FRE·SRE 동시 성장과 대규모 유입 | 첫 확인 2024-02-08 |
| 사전 반증 | 순유입 둔화·margin 압박 | 복잡한 결합회사를 FRE와 SRE로 분리하고 보험이익에 더 낮은 배수를 준 점이 뛰어났다. 낮은 진입가격이 forecast 오차를 흡수했다. 초과자본이 무조건 buyback으로 귀속된다는 가정은 별도 검증이 필요하다. |

### 실제 전개와 투자 결론

진입 시점의 공포 뒤 Apollo는 2023년 AUM $651bn, FRE+SRE 성장 25%+를 기록했고 주가는 $46.50에서 $100.40으로 약 116% 상승했다. 보험 spread와 origination 결합은 작동했다. 다만 기준일은 2026 목표 전이므로 $9 EPS와 5년 IRR 자체는 아직 완결 판정할 수 없다.

**종합판정: 매우 성공.** 복잡한 결합회사를 FRE와 SRE로 분리하고 보험이익에 더 낮은 배수를 준 점이 뛰어났다. 낮은 진입가격이 forecast 오차를 흡수했다. 초과자본이 무조건 buyback으로 귀속된다는 가정은 별도 검증이 필요하다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2022 EPS | $5.50E | 지속 | 2023 ANI 성장 | 적중 |
| 2026 EPS | $9+ | 달성 | 목표연도 미도래 | 진행 |
| SRE 배수 | 5~6x implied | 10x 재평가 | 주가 rerating | 방향 적중 |
| 가격 | $46.50 | 12~20% IRR | $100.40 | 매우 성공 |

재사용 질문: **순유입 둔화·margin 압박**

## 2024-01-31 기준 기업 결론

Apollo 다섯 롱은 모두 성공했다. 초기 글들의 Athene 영구자본 통찰은 특히 정확했고, 2021~22 글은 합병과 FRE/SRE 분리를 촉매·배수에 직접 연결했다. 반복 오류는 보험자산을 단순 asset-light fee base로 보고 신용·ALM·규제자본을 충분히 할인하지 않은 것이다.

## 주요 근거

- [VIC Apollo 2014-06-22 원문](https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MANAGEMENT_LLC/6264557856)
- [Apollo 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1858681/000185868124000031/apo-20231231.htm)
- [Apollo Reports Fourth Quarter and Full Year 2023 Results](https://ir.apollo.com/news-events/press-releases/detail/486/apollo-reports-fourth-quarter-and-full-year-2023-results)
- [Apollo and Athene Announce Transaction Close](https://ir.apollo.com/news-events/press-releases/detail/28/apollo-and-athene-announce-transaction-close)
- [Apollo 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/1411494/000141149421000013/apo-20201231.htm)
- [Apollo historical prices](https://www.digrin.com/stocks/detail/APO/price)
- [VIC Apollo 2017-08-15 원문](https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MANAGEMENT_LLC/2870139803)
- [VIC Apollo 2021-11-29 원문](https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MGMT_INC/3123156096)
- [VIC Apollo 2022-09-10 원문](https://www.valueinvestorsclub.com/idea/APOLLO_GLOBAL_MGMT_INC/4366592262)


---

# KKR & Co. (KKR) — 기업과 비즈니스

KKR은 private equity에서 출발해 credit·real assets·infrastructure·capital markets·보험으로 확장한 글로벌 대체자산 운용사다. Asset Management는 장기·폐쇄형 또는 영구자본에 관리보수를 부과하고 성과가 hurdle을 넘으면 carry를 받는다. Capital Markets는 인수금융·신디케이션·자문에서 거래수수료를 벌며, 자체 대차대조표는 펀드와 공동투자하고 신규 전략을 seed한다. 2021년 편입한 Global Atlantic은 연금·생명보험 부채를 장기 투자자금으로 제공해 보험 spread earnings와 영구자본 AUM을 더했다. 경제성은 AUM 그 자체보다 FPAUM, 미투자 약정의 fee 전환, FRE margin, 실현 carry, balance-sheet NAV, 보험자산의 신용·duration 관리와 주당 희석에 달려 있다. 좋은 운용성과도 투자자가 높은 가격을 내거나 carry를 영구 반복수익으로 보거나 보험·연결회계 위험을 무시하면 낮은 주주수익으로 이어질 수 있다.

## 돈을 버는 구조

- 반복이익: fee-paying AUM × 보수율 − 보상·운영비 = FRE
- 성과이익: 펀드수익이 hurdle을 넘고 실제 회수될 때 carry 발생
- 자체자본: balance-sheet 투자수익과 신규전략 seed, 단 할인·세금·부채 필요
- 보험자본: APO의 Athene·KKR의 Global Atlantic은 장기자금과 spread를 제공하지만 신용·ALM·규제자본 위험 동반

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2015-01-27 | Long | Long | 대차대조표+반복보수 하방과 carry 무료옵션 롱 | $24.01 월말→$86.58; 가격 약 +261%, 분배 제외 | 매우 성공 |
| 2016-11-16 | Short | Long | 65% 순자산 하방과 12% FCF yield 롱 | $15.30 월말 근사→$86.58; 가격 약 +466%, 분배 제외 | 초대형 성공 |
| 2018-02-01 | Long | Long | $34 SOTP와 brand/LP inertia 롱 | $24.08 월말→$86.58; 가격 약 +260%, 분배 제외 | 매우 성공 |
| 2022-04-21 | Short | Long | $23.75 비FRE 가치와 15배 core FRE 롱 | $50.97 월말→$86.58; 가격 약 +70%, 배당 제외 | 성공 |

## 1. 2015-01-27 — 대차대조표+반복보수 하방과 carry 무료옵션 롱

### 원 투자논지

$96bn AUM의 KKR을 balance-sheet investments, 반복 fee earnings, carry의 세 부분으로 봤다. 자체 투자자산과 안정적 관리보수만으로 가격 대부분이 설명되고, 높은 장기성과·locked capital·신규전략 seed 능력이 AUM을 늘리며 carry와 성장에는 낮은 값을 지불한다는 롱이었다. 동종사 중 큰 balance sheet가 downside protection과 상품 확장의 전략자산이라는 점을 강조했다.

### 논지를 구성한 핵심 주장

#### 1. locked capital — 적중

**핵심 주장:** 장기약정 자본이 경기중에도 fee를 지킨다.

**이 주장이 성립하려면:** LP default·조기상환 없이 계약 유지

**사전 반증조건:** AUM 감소와 fee base 급락

**실제 결과:** FPAUM과 perpetual capital이 크게 성장했다.

#### 2. balance sheet — 부분~적중

**핵심 주장:** 큰 자체투자자산이 하방이자 신규전략 seed다.

**이 주장이 성립하려면:** NAV가 실현 가능하고 가치파괴 없음

**사전 반증조건:** 할인·부채·보상으로 주주 몫 축소

**실제 결과:** seed 기능은 맞았으나 보험 편입으로 복잡해졌다.

#### 3. carry option — 적중

**핵심 주장:** 현재가격은 성과보수를 거의 반영하지 않는다.

**이 주장이 성립하려면:** 펀드성과와 realization 지속

**사전 반증조건:** 성과악화·exit 폐쇄

**실제 결과:** 누적 carry가 큰 추가가치를 만들었다.

#### 4. AUM 성장 — 적중

**핵심 주장:** 브랜드·성과가 인접전략 재모금을 만든다.

**이 주장이 성립하려면:** 후속펀드 확대·신규전략 채택

**사전 반증조건:** LP 이탈·fund 축소

**실제 결과:** $96bn에서 $553bn으로 확대됐다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | $96bn AUM의 KKR을 balance-sheet investments, 반복 fee earnings, carry의 세 부분으로 봤다. 자체 투자자산과 안정적 관리보수만으로 가격 대부분이 설명되고, 높은 장기성과·locked capital·신규전략 seed 능력이 AUM을 늘리며 carry와 성장에는 낮은 값을 지불한다는 롱이었다. 동종사 중 큰 balance sheet가 downside protection과 상품 확장의 전략자산이라는 점을 강조했다. | KKR은 Global Atlantic과 credit·real assets 확장으로 2023년 AUM $553bn, FPAUM $446bn이 됐고 FRE $2.4bn을 기록했다. 2024-01 월말 $86.58로 $24 대비 약 3.6배이며 누적분배는 제외한 수치다. balance sheet는 가치와 성장 seed 역할을 했지만 보험 편입 뒤 단순 청산가치가 아니라 신용·ALM 위험을 포함한 운영자본이 됐다. |
| 밸류에이션·청구권 | 순투자자산+fee earnings이 가격 대부분; carry·성장 무료옵션 | $24.01 월말→$86.58; 가격 약 +261%, 분배 제외 |
| 촉매·시간 | AUM·관리보수 증가와 투자회수 | 첫 확인 2016-02-26 |
| 사전 반증 | AUM 감소와 fee base 급락 | 반복보수로 하방을 만들고 carry·신규전략을 upside로 둔 구조가 맞았다. 하지만 balance sheet의 시장가치는 할인과 보상·세금·보험자본을 빼야 주주 청구권이 된다는 점은 더 엄격히 봐야 했다. |

### 실제 전개와 투자 결론

KKR은 Global Atlantic과 credit·real assets 확장으로 2023년 AUM $553bn, FPAUM $446bn이 됐고 FRE $2.4bn을 기록했다. 2024-01 월말 $86.58로 $24 대비 약 3.6배이며 누적분배는 제외한 수치다. balance sheet는 가치와 성장 seed 역할을 했지만 보험 편입 뒤 단순 청산가치가 아니라 신용·ALM 위험을 포함한 운영자본이 됐다.

**종합판정: 매우 성공.** 반복보수로 하방을 만들고 carry·신규전략을 upside로 둔 구조가 맞았다. 하지만 balance sheet의 시장가치는 할인과 보상·세금·보험자본을 빼야 주주 청구권이 된다는 점은 더 엄격히 봐야 했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| AUM | $96bn | 장기 증가 | $553bn FY2023 | 적중 |
| FPAUM | 장기 locked | 반복보수 | $446bn FY2023 | 적중 |
| FRE | 가격 하방 | 증가 | $2.4bn FY2023 | 적중 |
| 가격 | $24.01 | 상승+분배 | $86.58 | 매우 성공 |

재사용 질문: **AUM 감소와 fee base 급락**

## 2. 2016-11-16 — 65% 순자산 하방과 12% FCF yield 롱

### 원 투자논지

$15 주가에서 순현금·투자자산 $9.75/주가 65%를 덮고 나머지 $5만 반복 fee business 값이라고 계산했다. 향후 FCF $1.85~2.10/주, EV $4.3bn/EBITDA $1.27bn=3.4배, 73% AUM의 8년 이상 lock-up, 아직 fee를 내지 않는 $20bn 약정을 근거로 carry와 AUM 성장·balance-sheet return을 거의 공짜로 샀다. 현재가치 최소 $20/주를 제시했다.

### 논지를 구성한 핵심 주장

#### 1. 순자산 하방 — 적중

**핵심 주장:** $9.75/주 순현금·투자가격이 주가 65%를 덮는다.

**이 주장이 성립하려면:** NAV 회수와 제한된 holdco 부채

**사전 반증조건:** NAV 30%+ 손상·주주비귀속

**실제 결과:** 장부·전략투자가치가 장기 커졌다.

#### 2. FRE 저평가 — 적중

**핵심 주장:** 잔여 EV는 3.4x EBITDA·12%+ FCF yield다.

**이 주장이 성립하려면:** 관리보수 증가가 주당현금으로 전환

**사전 반증조건:** 보상·SBC가 FCF 흡수

**실제 결과:** FRE $2.4bn으로 규모가 크게 증가했다.

#### 3. fee shadow — 적중

**핵심 주장:** $20bn 미수수 약정이 비용 적게 fee로 전환된다.

**이 주장이 성립하려면:** 투자기간 진입·deployment

**사전 반증조건:** 약정 취소·fee holiday

**실제 결과:** 2023에도 같은 fee-shadow가 $39bn 존재했다.

#### 4. 구조 촉매 — 적중

**핵심 주장:** 세제 명확화·C-corp가 discount를 줄인다.

**이 주장이 성립하려면:** 기관투자자 접근성·지수 적격성 확대

**사전 반증조건:** 세금비용이 rerating 상쇄

**실제 결과:** 2018 C-corp 전환 뒤 장기 rerating했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | $15 주가에서 순현금·투자자산 $9.75/주가 65%를 덮고 나머지 $5만 반복 fee business 값이라고 계산했다. 향후 FCF $1.85~2.10/주, EV $4.3bn/EBITDA $1.27bn=3.4배, 73% AUM의 8년 이상 lock-up, 아직 fee를 내지 않는 $20bn 약정을 근거로 carry와 AUM 성장·balance-sheet return을 거의 공짜로 샀다. 현재가치 최소 $20/주를 제시했다. | $20 목표는 빠르게 달성됐고 2024-01 $86.58로 진입가 대비 약 +466%였다. AUM $553bn·FPAUM $446bn, $39bn fee 미발생 약정, FRE $2.4bn으로 fee conversion 논지가 반복됐다. C-corp 전환과 Global Atlantic 편입도 투자자층과 영구자본을 확대했다. |
| 밸류에이션·청구권 | $9.75 순자산+$5 fee business; 최소 $20/주 | $15.30 월말 근사→$86.58; 가격 약 +466%, 분배 제외 |
| 촉매·시간 | North America XII fee 활성화와 AUM 성장 | 첫 확인 2017-02-09 |
| 사전 반증 | NAV 30%+ 손상·주주비귀속 | 순자산·FRE·carry를 분리하고 아직 fee를 내지 않는 약정의 시간표까지 본 것이 강했다. ‘순자산’은 즉시 현금화 가치가 아니며 세금·보상·할인을 적용해야 하지만 진입가격의 margin of safety가 그 오류를 충분히 흡수했다. |

### 실제 전개와 투자 결론

$20 목표는 빠르게 달성됐고 2024-01 $86.58로 진입가 대비 약 +466%였다. AUM $553bn·FPAUM $446bn, $39bn fee 미발생 약정, FRE $2.4bn으로 fee conversion 논지가 반복됐다. C-corp 전환과 Global Atlantic 편입도 투자자층과 영구자본을 확대했다.

**종합판정: 초대형 성공.** 순자산·FRE·carry를 분리하고 아직 fee를 내지 않는 약정의 시간표까지 본 것이 강했다. ‘순자산’은 즉시 현금화 가치가 아니며 세금·보상·할인을 적용해야 하지만 진입가격의 margin of safety가 그 오류를 충분히 흡수했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 순자산/주 | $9.75 | 하방 65% | BVPS $30.95 FY2023 | 적중 |
| FCF/주 | $1.85~2.10E | 12%+ yield | FRE/주 $2.68 FY2023 | 방향 적중 |
| 목표가 | $20+ | +33% | 대폭 초과 | 성공 |
| 가격 | $15.30 | 상승 | $86.58 | 초대형 성공 |

재사용 질문: **NAV 30%+ 손상·주주비귀속**

## 3. 2018-02-01 — $34 SOTP와 brand/LP inertia 롱

### 원 투자논지

SOTP $34/주로 약 40% upside를 제시했다. FPAUM $114bn의 management fee earnings와 할인한 book value만으로 현 가격을 설명해 carry를 거의 0으로 두었다. 2011년 이후 FPAUM +150%, book value/주 +60%, 누적분배 $7.75를 근거로 복리성을 보였다. 동시에 deal multiple 9.3배, 경쟁심화, realizations 변동, 비지배 구조를 지적하고 balance sheet 20%+ 손상 시 약 $3/주 하방을 stress했다.

### 논지를 구성한 핵심 주장

#### 1. fee floor — 적중

**핵심 주장:** FPAUM $114bn fee earnings과 할인 book만으로 가격을 설명한다.

**이 주장이 성립하려면:** fee margin·FPAUM 유지

**사전 반증조건:** fundraising 감소·비용급증

**실제 결과:** FPAUM은 $446bn으로 증가했다.

#### 2. carry 무료 — 적중

**핵심 주장:** carry를 0으로 둬도 40% upside다.

**이 주장이 성립하려면:** carry가 음의 가치가 아니고 clawback 제한

**사전 반증조건:** 성과보상·세금이 가치 상쇄

**실제 결과:** 실현성과가 추가 수익원이 됐다.

#### 3. 브랜드 inertia — 적중

**핵심 주장:** LP는 한 번의 나쁜 빈티지보다 긴 기록을 보고 재약정한다.

**이 주장이 성립하려면:** 상대성과·조직 안정

**사전 반증조건:** 핵심인력 이탈·연속 저성과

**실제 결과:** fundraising과 전략확장이 지속됐다.

#### 4. cycle stress — 적중

**핵심 주장:** 높은 9.3x deal multiple과 경쟁에도 book 손상은 약 $3다.

**이 주장이 성립하려면:** 레버리지·운영개선으로 손실 제한

**사전 반증조건:** 경기침체와 exit 폐쇄 동시발생

**실제 결과:** 2020·2022 변동은 있었지만 장기 thesis를 훼손하지 않았다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | SOTP $34/주로 약 40% upside를 제시했다. FPAUM $114bn의 management fee earnings와 할인한 book value만으로 현 가격을 설명해 carry를 거의 0으로 두었다. 2011년 이후 FPAUM +150%, book value/주 +60%, 누적분배 $7.75를 근거로 복리성을 보였다. 동시에 deal multiple 9.3배, 경쟁심화, realizations 변동, 비지배 구조를 지적하고 balance sheet 20%+ 손상 시 약 $3/주 하방을 stress했다. | $34 목표는 2019~20년에 넘어섰고 2024-01 $86.58로 약 +260%였다. FPAUM은 $446bn으로 약 네 배, perpetual capital은 $224bn으로 늘었다. Global Atlantic 인수로 영구자본 논지는 강화됐으나 보험과 전략보유지분 때문에 SOTP·GAAP가 더 복잡해졌다. |
| 밸류에이션·청구권 | management fee value+discounted book; SOTP $34, carry 0 | $24.08 월말→$86.58; 가격 약 +260%, 분배 제외 |
| 촉매·시간 | FPAUM 성장·C-corp 전환 | 첫 확인 2018-07-02 |
| 사전 반증 | fundraising 감소·비용급증 | carry를 0으로 두고도 upside가 남는 구조, book value stress, PE 업황 과열을 동시에 적은 process가 좋았다. 브랜드와 LP inertia는 실제로 강했지만 ‘6년은 안전’이 아니라 펀드성과와 fundraising lag를 계속 확인해야 한다. |

### 실제 전개와 투자 결론

$34 목표는 2019~20년에 넘어섰고 2024-01 $86.58로 약 +260%였다. FPAUM은 $446bn으로 약 네 배, perpetual capital은 $224bn으로 늘었다. Global Atlantic 인수로 영구자본 논지는 강화됐으나 보험과 전략보유지분 때문에 SOTP·GAAP가 더 복잡해졌다.

**종합판정: 매우 성공.** carry를 0으로 두고도 upside가 남는 구조, book value stress, PE 업황 과열을 동시에 적은 process가 좋았다. 브랜드와 LP inertia는 실제로 강했지만 ‘6년은 안전’이 아니라 펀드성과와 fundraising lag를 계속 확인해야 한다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| FPAUM | $114bn | 성장 | $446bn FY2023 | 적중 |
| SOTP | $34 | 약 +40% | 대폭 초과 | 성공 |
| 누적분배 | $7.75 since 2011 | 계속 | 추가 분배 | 적중 |
| 가격 | $24.08 | 상승 | $86.58 | 매우 성공 |

재사용 질문: **fundraising 감소·비용급증**

## 4. 2022-04-21 — $23.75 비FRE 가치와 15배 core FRE 롱

### 원 투자논지

$112bn dry powder(+67% YoY), 2004~20 organic AUM CAGR 19%, high-teens FRE 성장 전망을 근거로 장기 복리를 주장했다. 주가에서 net balance-sheet assets $13.25, 보험 $6.50, embedded carry $4.00, 합계 $23.75를 빼면 after-tax·after-SBC 2023 FRE $2.15가 약 15배에 불과하다고 계산했다. Global Atlantic의 장기부채와 KKR origination 결합, capital markets의 숨은 수익성을 강조했다.

### 논지를 구성한 핵심 주장

#### 1. FRE 복리 — 부분~적중

**핵심 주장:** high-teens FRE 성장과 15배 core valuation이 매력적이다.

**이 주장이 성립하려면:** organic FPAUM 성장·margin 유지

**사전 반증조건:** 순유입·FRE/주 한 자릿수

**실제 결과:** 2023 FRE는 10% 성장, 장기 방향은 유지됐다.

#### 2. 보험 시너지 — 적중

**핵심 주장:** Global Atlantic liabilities가 영구자본과 origination 수요를 만든다.

**이 주장이 성립하려면:** 보험 spread·자본건전성 유지

**사전 반증조건:** 신용·ALM 손실

**실제 결과:** perpetual capital $224bn, 잔여지분 인수로 강화됐다.

#### 3. 비FRE 가치 — 부분

**핵심 주장:** $23.75/주의 BS·보험·carry가 별도 청구권이다.

**이 주장이 성립하려면:** 중복 없이 세후 주주에게 귀속

**사전 반증조건:** 할인·부채·보상·실현지연

**실제 결과:** 가치는 존재하지만 액면합산보다 haircut이 필요하다.

#### 4. capital markets — 적중

**핵심 주장:** 거래·조달 플랫폼이 고ROE hidden gem이다.

**이 주장이 성립하려면:** KKR fund flow와 제3자 거래 지속

**사전 반증조건:** 딜 시장 장기폐쇄

**실제 결과:** 2023 transaction fee $578m으로 의미있는 이익축이었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | $112bn dry powder(+67% YoY), 2004~20 organic AUM CAGR 19%, high-teens FRE 성장 전망을 근거로 장기 복리를 주장했다. 주가에서 net balance-sheet assets $13.25, 보험 $6.50, embedded carry $4.00, 합계 $23.75를 빼면 after-tax·after-SBC 2023 FRE $2.15가 약 15배에 불과하다고 계산했다. Global Atlantic의 장기부채와 KKR origination 결합, capital markets의 숨은 수익성을 강조했다. | 2022년 금리충격으로 단기 하락했지만 2024-01 $86.58로 약 +70%였다. 2023 AUM $553bn, FPAUM $446bn, FRE $2.4bn/$2.68주, perpetual capital $224bn이 됐고 Global Atlantic 잔여 37% 인수도 2024-01-02 완료됐다. 반면 dry powder는 배치 시점보다 $99bn으로 낮아졌고 carry·보험·balance sheet를 액면 합산하는 valuation은 haircut이 필요하다. |
| 밸류에이션·청구권 | $23.75 비FRE 가치 차감 후 2023 after-SBC FRE $2.15의 15x | $50.97 월말→$86.58; 가격 약 +70%, 배당 제외 |
| 촉매·시간 | Global Atlantic 성장과 2023 FRE 증가 | 첫 확인 2024-01-02 |
| 사전 반증 | 순유입·FRE/주 한 자릿수 | after-SBC FRE와 비FRE 자산을 분리하고 보험·capital markets를 growth engine으로 본 방향이 맞았다. 다만 $23.75가 모두 독립적으로 회수 가능한 현금은 아니며 보험 book·carry에는 자본비용·실현·세금 할인이 필요하다. |

### 실제 전개와 투자 결론

2022년 금리충격으로 단기 하락했지만 2024-01 $86.58로 약 +70%였다. 2023 AUM $553bn, FPAUM $446bn, FRE $2.4bn/$2.68주, perpetual capital $224bn이 됐고 Global Atlantic 잔여 37% 인수도 2024-01-02 완료됐다. 반면 dry powder는 배치 시점보다 $99bn으로 낮아졌고 carry·보험·balance sheet를 액면 합산하는 valuation은 haircut이 필요하다.

**종합판정: 성공.** after-SBC FRE와 비FRE 자산을 분리하고 보험·capital markets를 growth engine으로 본 방향이 맞았다. 다만 $23.75가 모두 독립적으로 회수 가능한 현금은 아니며 보험 book·carry에는 자본비용·실현·세금 할인이 필요하다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| dry powder | $112bn | deployment+성장 | $99bn FY2023 | 부분 |
| FRE/주 | $2.15 2023E | high-teens 성장 | $2.68 FY2023 | 적중 |
| perpetual capital | 보험 편입 | 증가 | $224bn FY2023 | 적중 |
| 가격 | $50.97 | 장기 복리 | $86.58 | 성공 |

재사용 질문: **순유입·FRE/주 한 자릿수**

## 2024-01-31 기준 기업 결론

KKR 네 롱은 모두 성공했다. 순자산·FRE를 하방으로 두고 carry와 신규전략을 무료 또는 저가 option으로 산 구조가 반복됐다. Global Atlantic은 permanent capital 논지를 강화했지만 보험 book와 전략보유지분을 액면가로 SOTP에 넣어서는 안 된다.

## 주요 근거

- [VIC KKR 2015-01-27 원문](https://www.valueinvestorsclub.com/idea/KKR_and_CO_LP/3593801772)
- [KKR 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1404912/000140491224000005/kkr-20231231.htm)
- [KKR Fourth Quarter 2023 Financial Results](https://www.sec.gov/Archives/edgar/data/1404912/000140491224000002/q423earningsrelease_vf.htm)
- [KKR Completes Acquisition of Global Atlantic](https://ir.kkr.com/news-releases/news-release-details/kkr-completes-acquisition-global-atlantic)
- [KKR Acquires Remaining Stake in Global Atlantic](https://ir.kkr.com/news-releases/news-release-details/kkr-completes-acquisition-remaining-37-global-atlantic)
- [KKR historical prices](https://www.digrin.com/stocks/detail/KKR/price)
- [VIC KKR 2018-02-01 원문](https://www.valueinvestorsclub.com/idea/KKR_andamp%3B_CO_LP/6637431692)


---

# Blackstone (BX) — 기업과 비즈니스

Blackstone은 부동산·private equity·credit & insurance·infrastructure·secondaries·hedge-fund solutions를 운용하는 글로벌 대체자산 플랫폼이다. 관리보수는 장기 약정 또는 영구자본에 반복적으로 붙고, 투자성과가 기준을 넘으면 incentive fee와 carried interest가 발생한다. 운용자산 대부분은 고객자본이어서 전통 은행처럼 전액을 자체 조달하지 않지만, GP commitment·seed·보험 및 리테일 상품에는 시장·유동성 위험이 남는다. Blackstone의 핵심 flywheel은 우수한 실현성과→LP 재약정→더 큰 flagship·인접전략→보수·carry 증가이며, 개인자산가·보험 채널이 자금원을 넓힌다. 핵심 지표는 fee-earning AUM, FRE·DE, 실현가능 carry, 펀드수익률, 영구자본 비중, 순유입과 분배다. 특히 ENI에는 미실현 평가이익이 섞이므로 배당·현금전환과 분리해야 한다.

## 돈을 버는 구조

- 반복이익: fee-paying AUM × 보수율 − 보상·운영비 = FRE
- 성과이익: 펀드수익이 hurdle을 넘고 실제 회수될 때 carry 발생
- 자체자본: balance-sheet 투자수익과 신규전략 seed, 단 할인·세금·부채 필요
- 보험자본: APO의 Athene·KKR의 Global Atlantic은 장기자금과 spread를 제공하지만 신용·ALM·규제자본 위험 동반

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2014-07-18 | Short | Long | FRE·ENI·DDM 삼각검증 롱 | $33.84→$124.45; 가격 약 +268%, 대규모 분배 제외 | 매우 성공 |

## 1. 2014-07-18 — FRE·ENI·DDM 삼각검증 롱

### 원 투자논지

AUM $272bn, 2005~13 CAGR 23%, ENI/주 CAGR 13%인 Blackstone을 PE $66bn·Real Estate $83bn·BAAM $61bn·Credit $69bn·Advisory로 분해했다. 2015 management FRE $0.77에 18배를 적용한 $13.88와 carry·투자자산을 합친 SOTP $43.25, 2015 ENI 13배 $45.50, DDM $47.50의 세 방법으로 35~40% upside를 제시했다. 2014 예상 분배수익률 6.8%, 장기 11~12% ENI/DE 성장+5~6% yield로 약 17% 수익을 기대했다.

### 논지를 구성한 핵심 주장

#### 1. AUM flywheel — 적중

**핵심 주장:** 성과와 브랜드가 재모금·인접전략 확대를 만든다.

**이 주장이 성립하려면:** 상대성과·LP 재약정·인재 유지

**사전 반증조건:** flagship 축소·대규모 순유출

**실제 결과:** $272bn에서 $1tn+로 성장했다.

#### 2. FRE floor — 적중

**핵심 주장:** 2015 management FRE $0.77×18=$13.88이 안정적 가치축이다.

**이 주장이 성립하려면:** fee-earning AUM·margin 지속

**사전 반증조건:** 보수율 하락·비용 급증

**실제 결과:** FRE와 영구자본이 장기 확대됐다.

#### 3. carry/ENI — 부분~적중

**핵심 주장:** 성과실현이 11~12% ENI/DE 성장을 만든다.

**이 주장이 성립하려면:** exit 시장이 cycle 내 열리고 carry 현금화

**사전 반증조건:** 미실현가치 하락·realization 장기폐쇄

**실제 결과:** 직선은 아니지만 cycle 전체 현금화됐다.

#### 4. 분배+rerating — 적중

**핵심 주장:** 5~6% yield와 성장으로 약 17% 장기수익이다.

**이 주장이 성립하려면:** 분배가 earnings로 커버되고 성장 유지

**사전 반증조건:** 분배삭감·AUM 정체

**실제 결과:** 가격과 누적분배 모두 목표를 크게 넘었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·경제성 | AUM $272bn, 2005~13 CAGR 23%, ENI/주 CAGR 13%인 Blackstone을 PE $66bn·Real Estate $83bn·BAAM $61bn·Credit $69bn·Advisory로 분해했다. 2015 management FRE $0.77에 18배를 적용한 $13.88와 carry·투자자산을 합친 SOTP $43.25, 2015 ENI 13배 $45.50, DDM $47.50의 세 방법으로 35~40% upside를 제시했다. 2014 예상 분배수익률 6.8%, 장기 11~12% ENI/DE 성장+5~6% yield로 약 17% 수익을 기대했다. | Blackstone은 2023년 AUM $1tn을 넘겨 당시의 약 네 배가 됐고, 부동산·credit·보험·infrastructure·private wealth로 확장했다. 2024-01 실가격 $124.45로 진입가 대비 약 +268%이며 큰 누적분배를 제외한 가격수익이다. 2015 $43~47.5 목표는 달성됐다. 다만 ENI는 미실현 평가와 exit cycle에 민감해 매년 직선으로 성장하지 않았다. |
| 밸류에이션·청구권 | SOTP $43.25; 13x 2015 ENI $45.50; DDM $47.50; downside $25 | $33.84→$124.45; 가격 약 +268%, 대규모 분배 제외 |
| 촉매·시간 | 펀드성과·fundraising과 BCP carry catch-up | 첫 확인 2015-02-27 |
| 사전 반증 | flagship 축소·대규모 순유출 | FRE, ENI multiple, 배당현금흐름을 교차검증하고 downside $25까지 제시한 점이 가장 강하다. 성공의 핵심은 실제 AUM·FRE 복리였으며, 당시 6.8% 배당을 채권처럼 자본화하지 않고 carry·시장주기를 분리한 것이 유효했다. |

### 실제 전개와 투자 결론

Blackstone은 2023년 AUM $1tn을 넘겨 당시의 약 네 배가 됐고, 부동산·credit·보험·infrastructure·private wealth로 확장했다. 2024-01 실가격 $124.45로 진입가 대비 약 +268%이며 큰 누적분배를 제외한 가격수익이다. 2015 $43~47.5 목표는 달성됐다. 다만 ENI는 미실현 평가와 exit cycle에 민감해 매년 직선으로 성장하지 않았다.

**종합판정: 매우 성공.** FRE, ENI multiple, 배당현금흐름을 교차검증하고 downside $25까지 제시한 점이 가장 강하다. 성공의 핵심은 실제 AUM·FRE 복리였으며, 당시 6.8% 배당을 채권처럼 자본화하지 않고 carry·시장주기를 분리한 것이 유효했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| AUM | $272bn | 11~12% earnings 성장 | $1tn+ FY2023 | 적중 |
| 분배 yield | 6.8% 2014E | 5~6% 장기 | 변동분배 지속 | 부분~적중 |
| 목표가 | $43.25~47.50 | 35~40% | 달성 | 성공 |
| 가격 | $33.84 | 약 17% 장기 | $124.45 | 매우 성공 |

재사용 질문: **flagship 축소·대규모 순유출**

## 2024-01-31 기준 기업 결론

Blackstone 2014 롱은 AUM·FRE 복리와 분배를 정확히 잡아 매우 성공했다. 가장 좋은 점은 SOTP·ENI multiple·DDM을 교차검증하고 $25 downside까지 적은 것이다. ENI는 미실현 carry가 섞이는 만큼 직선형 EPS처럼 취급하지 않는 규율이 핵심이다.

## 주요 근거

- [VIC Blackstone 2014-07-18 원문](https://www.valueinvestorsclub.com/idea/BLACKSTONE_GROUP_LP/5974072490)
- [Blackstone 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393818/000139381824000010/bx-20231231.htm)
- [Blackstone Fourth Quarter and Full Year 2023 Results](https://www.blackstone.com/news/press/blackstone-reports-fourth-quarter-and-full-year-2023-earnings-results/)
- [Blackstone 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393818/000119312515064920/d856336d10k.htm)
- [Blackstone 2013 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393818/000119312514073756/d640229d10k.htm)
- [Blackstone historical prices](https://www.digrin.com/stocks/detail/BX/price)


---

# 배치 공통 패턴과 DB 학습 태그

| 패턴 | 성공 메커니즘 | 실패를 부르는 오용 |
|---|---|---|
| locked/permanent capital | 환매 압박이 낮아 fee visibility와 contrarian deployment 확보 | 보험부채 위험까지 asset-light로 착각 |
| FRE floor + carry option | 반복보수로 하방을 만들고 성과보수에 낮은 값만 지불 | carry를 정상 EPS처럼 고배수 적용 |
| fee shadow | 미수수 약정의 투자기간 진입이 비용 적은 성장 | deployment 지연·fee offset 무시 |
| balance-sheet SOTP | 현가격에서 숨은 투자자산·seed 능력 발견 | NAV를 세금·부채·보상·유동성 할인 없이 합산 |
| structure catalyst | C-corp·지배구조 단순화가 투자자층 확대 | 구조개편만으로 사업위험까지 사라진다고 가정 |

핵심 학습 태그: `alternative_asset_manager`, `fee_paying_aum`, `locked_capital`, `permanent_capital`, `fre_floor`, `carry_option`, `fee_shadow`, `insurance_spread`, `nav_haircut`, `sum_of_parts`, `structure_catalyst`, `forecast_stacking`.

# 데이터 품질·방법론

- 평가기준일은 2024-01-31로 고정했다. 2023 회계연도 결과가 기준일 뒤 발표됐더라도 2023-12-31 현재의 사업상태 확인에만 사용했다.
- 가격은 원문 가격 또는 게시월 실가격과 2024-01 월말을 비교한 근사치다. APO·KKR·BX는 과거 분배가 커서 **배당 제외 가격수익은 실제 총수익을 과소평가**한다.
- 판정은 주가방향, FRE·SRE·carry의 사업인과, valuation 청구권, 촉매·시간을 분리했다.
- 총 AUM 성장만으로 성공 처리하지 않고 FPAUM·FRE/주·영구자본·희석과 보험위험을 함께 확인했다.
