# Batch 013 — Mastercard·Global Payments·PayPal·Block 10건

평가기준일: 2024-01-31

분석일: 2026-09-03

대상: Mastercard 1건·Global Payments 1건·PayPal 3건·Square/Block 5건

## 결론부터

같은 결제 성장 테마에서도 결과는 진입배수와 주주 귀속에 따라 극단적으로 갈렸다. **낮은 배수의 network·FCF를 산 2010 MA, 2012 GPN, 2016 PYPL, 2016 SQ는 성공**했고, 2021년 SQ·PYPL처럼 높은 성장 duration과 multiple을 동시에 요구한 롱은 사업이 성장해도 치명적으로 실패했다.

| 기업 | 건수 | 가장 강한 성공 | 가장 큰 실패 | 반복 학습 |
|---|---:|---|---|---|
| Mastercard | 1 | 전자결제·고정비 network를 12.3x EPS에 매수 | 뚜렷한 실패 없음 | interchange와 network fee의 귀속 분리 |
| Global Payments | 1 | 10x FCF·사건성 보안악재 정상화 | 예상한 매각촉매는 불발 | 순현금 option은 미래 M&A 위험과 함께 평가 |
| PayPal | 3 | 2016 5% FCF yield+Venmo 옵션 | 2021 35x EPS·20% duration | TPV보다 branded mix·transaction margin dollars |
| Block | 5 | 2016 CAC/payback 저가 진입 | 2021 두 롱 -70%대 | gross profit에서 SBC·M&A·희석 후 FCF/주로 연결 |

> 데이터 경고: 원 SQL `is_short`는 10건 중 4건이 틀렸다. Square 2016·2019·2021-03·2021-06 글은 SQL상 Short지만 본문과 기대수익은 Long이다. 2018-07 글만 실제 Short다. 원본 flag는 보존하고 분석 방향을 별도 저장했다.

---

# Mastercard (MA) — 기업과 비즈니스

Mastercard는 카드대출을 직접 해주는 은행이 아니라 전 세계 발급사·매입사·가맹점 사이에서 승인, 청산, 결제를 연결하는 양면 결제 네트워크다. 결제액에 연동되는 domestic assessment·cross-border assessment, 건수에 연동되는 transaction processing, 데이터·사기방지·컨설팅 등 value-added services에서 수익을 낸다. 고객 리베이트와 인센티브를 차감한 금액이 순매출이며, 카드 미수금의 신용손실은 주로 발급은행이 부담한다. 이미 깔린 네트워크에 거래가 추가될 때 비용 증가가 작아 높은 영업레버리지와 자본수익률이 발생한다. 핵심 지표는 gross dollar volume, switched transactions, cross-border volume, 순매출 대비 incentive, 영업이익률과 주식수다. 규제할인율(interchange)은 은행 수익이지만 규제·소송·대체결제는 Mastercard의 거래량과 가격에도 간접 영향을 준다.

## 돈을 버는 구조

- 결제액 기반 assessment와 cross-border fee
- 거래건수 기반 switching·processing
- fraud·data·consulting 등 value-added services
- 발급사·매입사 incentive와 규제·소송이 핵심 차감항목

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2010-09-14 | Long | Long | 12.3배 EPS의 글로벌 결제 네트워크 롱 | $20.54 조정가→$449.23; 약 +2,087%, 배당 제외 | 전설적 성공 |

## 1. 2010-09-14 — 12.3배 EPS의 글로벌 결제 네트워크 롱

### 원 투자논지

주가 $200에서 2011년 EPS $16.27의 12.3배, 순현금 제외 약 10배에 불과하다고 봤다. 944m장 카드·30.6m 가맹점·210개국을 연결하는 승인·청산·결제망은 분당 42,637건을 처리해도 건당 네트워크 비용이 약 2센트라 추가 거래의 margin이 높았다. 현금·수표에서 전자결제로 이동하는 구조적 성장, 유럽 SEPA debit 전환과 고정비 레버리지를 결합해 2012 EPS $19.31, 18개월 목표 $330을 제시했다. Durbin은 발급은행 interchange를 제한하지 Mastercard의 assessment·processing 수익을 직접 가격규제하는 것은 아니며 미국 debit은 매출 약 10%라고 분리했다.

### 논지를 구성한 핵심 주장

#### 1. 전자결제 전환 — 적중

**핵심 주장:** 현금·수표에서 카드로의 이동이 거래량을 장기간 키운다.

**이 주장이 성립하려면:** 소비지출보다 전자결제 침투율이 빠르게 상승

**사전 반증조건:** 결제량 성장 둔화가 3년 지속

**실제 결과:** 세계 GDV와 switched transactions가 장기 복리 성장했다.

#### 2. 고정비 네트워크 — 적중

**핵심 주장:** 건당 비용 약 2센트라 추가 거래가 높은 margin으로 전환된다.

**이 주장이 성립하려면:** 인센티브·기술비 증가가 거래매출보다 느림

**사전 반증조건:** 고객 incentive가 매출 증가를 모두 흡수

**실제 결과:** 2023 순이익률 약 45%로 economics가 입증됐다.

#### 3. Durbin 분리 — 적중

**핵심 주장:** interchange 규제는 issuer 수익과 MA network fee를 동일하게 훼손하지 않는다.

**이 주장이 성립하려면:** 규칙이 네트워크 가격 자체를 직접 제한하지 않음

**사전 반증조건:** 미국 debit volume·routing 상실이 전사이익을 크게 훼손

**실제 결과:** 영향은 관리됐고 글로벌 성장으로 상쇄됐다.

#### 4. 싼 진입 — 적중

**핵심 주장:** 2011 EPS 12.3배는 질과 성장 대비 과도한 할인이다.

**이 주장이 성립하려면:** EPS 복리와 자사주 매입이 주당가치로 귀속

**사전 반증조건:** 소송·규제로 정상 EPS가 영구 하락

**실제 결과:** 목표와 장기 가격을 압도적으로 초과했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 주가 $200에서 2011년 EPS $16.27의 12.3배, 순현금 제외 약 10배에 불과하다고 봤다. 944m장 카드·30.6m 가맹점·210개국을 연결하는 승인·청산·결제망은 분당 42,637건을 처리해도 건당 네트워크 비용이 약 2센트라 추가 거래의 margin이 높았다. 현금·수표에서 전자결제로 이동하는 구조적 성장, 유럽 SEPA debit 전환과 고정비 레버리지를 결합해 2012 EPS $19.31, 18개월 목표 $330을 제시했다. Durbin은 발급은행 interchange를 제한하지 Mastercard의 assessment·processing 수익을 직접 가격규제하는 것은 아니며 미국 debit은 매출 약 10%라고 분리했다. | 18개월 목표 $330은 2011년 중 달성했다. 10대1 분할을 반영한 게시월 가격 $20.54에서 2024-01 실제가격 $449.23으로 약 20.9배 상승했고 배당은 제외한 수치다. 2023년 순매출은 $25.1bn, 순이익 $11.2bn으로 성장했다. Durbin은 debit routing·은행 economics를 바꿨지만 글로벌 전자결제와 cross-border·서비스 확장을 막지 못했다. |
| 밸류에이션·청구권 | $19.31 FY12 EPS×15+$30~40 현금=$330(분할 전) | $20.54 조정가→$449.23; 약 +2,087%, 배당 제외 |
| 촉매·시간 | 2011년 EPS 성장과 $1bn 자사주 매입 | 첫 확인 2011-06-29 |
| 사전 반증 | 결제량 성장 둔화가 3년 지속 | 규제 대상을 issuer interchange와 network fee로 분리했고, 높은 ROIC를 회계상 margin이 아니라 네트워크의 낮은 증분비용과 연결했다. 단기 SEPA 수치보다 장기 cash-to-card 전환과 양면망의 가격력이 실제 성공의 주원인이었다. |

### 실제 전개와 투자 결론

18개월 목표 $330은 2011년 중 달성했다. 10대1 분할을 반영한 게시월 가격 $20.54에서 2024-01 실제가격 $449.23으로 약 20.9배 상승했고 배당은 제외한 수치다. 2023년 순매출은 $25.1bn, 순이익 $11.2bn으로 성장했다. Durbin은 debit routing·은행 economics를 바꿨지만 글로벌 전자결제와 cross-border·서비스 확장을 막지 못했다.

**종합판정: 전설적 성공.** 규제 대상을 issuer interchange와 network fee로 분리했고, 높은 ROIC를 회계상 margin이 아니라 네트워크의 낮은 증분비용과 연결했다. 단기 SEPA 수치보다 장기 cash-to-card 전환과 양면망의 가격력이 실제 성공의 주원인이었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입가 | $200 / 조정 $20.54 | $330 18개월 | $449.23 기준일 | 전설적 성공 |
| FY2012 EPS | $19.31 예상(분할 전) | 고정비 레버리지 | 장기 EPS 대폭 증가 | 적중 |
| FY2023 순매출 | 초기 네트워크 | 구조적 성장 | $25.1bn | 적중 |
| FY2023 순이익 | 고수익성 | 높은 incremental margin | $11.2bn | 적중 |

재사용 질문: **결제량 성장 둔화가 3년 지속**

## 2024-01-31 기준 기업 결론

2010 Mastercard 롱은 규제의 경제적 귀속을 정확히 분리하고 낮은 증분비용의 네트워크를 싼 배수에 산 전설적 성공이다. ‘전자결제 성장’만이 아니라 volume→EPS→주당가치 연결이 모두 맞았다.

## 주요 근거

- [Mastercard 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1141391/000114139124000022/ma-20231231.htm)
- [Mastercard 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/1141391/000119312511041182/d10k.htm)
- [Federal Reserve Final Rule on Debit Interchange](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20110629a.htm)
- [Mastercard historical prices](https://www.digrin.com/stocks/detail/MA/price)


---

# Global Payments (GPN) — 기업과 비즈니스

Global Payments는 Mastercard 같은 네트워크가 아니라 가맹점이 카드·디지털 결제를 받을 수 있도록 단말기, gateway, acquiring, POS·수직형 소프트웨어를 묶어 제공하는 merchant acquirer이자 issuer processor다. 매입 부문은 가맹점 수수료에서 카드 네트워크·발급사와 파트너 몫을 빼고 spread를 벌며, issuer 부문은 금융기관의 카드계정 처리량과 서비스 계약에서 반복수익을 얻는다. 2012년 논지의 핵심은 독립판매조직(ISO)이 낮은 고객획득비용과 신용위험 이전을 제공한다는 것이었지만, 그 대가로 residual 지급과 가격경쟁 때문에 margin이 낮았다. 이후 Heartland·TSYS·EVO 인수로 software-led payments가 커졌고 회사는 단순 소형 가맹점 매입사에서 복합 결제 플랫폼으로 바뀌었다. 핵심 지표는 adjusted net revenue, merchant/issuer segment margin, organic growth, integration synergy, 순부채와 주식수다. 대형 M&A가 FCF를 키워도 부채·무형자산·통합위험을 함께 보아야 한다.

## 돈을 버는 구조

- merchant acquiring spread와 POS·vertical software
- issuer processing의 장기계약·건수 수수료
- ISO residual·network fee·transaction loss 차감
- M&A synergy에서 이자·통합비용·주식수 차감

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2012-11-06 | Long | Long | 10배 FCF·buyback·보안사고 정상화 롱 | $20.65 조정가→$133.23; 약 +545%, 배당 제외 | 매우 성공 |

## 1. 2012-11-06 — 10배 FCF·buyback·보안사고 정상화 롱

### 원 투자논지

보안침해와 캐나다 가격경쟁으로 눌린 GPN을 약 10배 2013 FCF, 11배 P/E, 6배 EBITDA에 샀다. 미국 56%·캐나다 15%·유럽 22%·아시아 7%의 매출과 international EBITDA 45%를 가진 6위 미국 acquirer였다. $250m 순현금과 2.5배까지의 레버리지 여력을 이용하면 $600~700m을 추가 조달해 시가총액 약 20%를 매입할 수 있고, 캐나다 margin 안정과 보안사고 종결 뒤 14~15배 FCF인 $60~65로 재평가되거나 Fiserv·PE에 인수될 수 있다고 봤다.

### 논지를 구성한 핵심 주장

#### 1. 사건성 할인 — 적중

**핵심 주장:** 보안침해는 고객기반을 파괴하지 않는 일회성 평판 악재다.

**이 주장이 성립하려면:** network registration 유지·고객이탈 제한

**사전 반증조건:** 대형은행·ISO 계약 상실

**실제 결과:** 사업은 유지되고 가격이 정상화됐다.

#### 2. 캐나다 margin — 부분~적중

**핵심 주장:** 가격투명성 충격 뒤 경쟁이 합리화된다.

**이 주장이 성립하려면:** 재계약 가격과 비용조치로 margin 안정

**사전 반증조건:** Elavon 가격전쟁 장기화

**실제 결과:** 전사 수익성은 확대됐으나 이후 사업구조가 달라졌다.

#### 3. buyback 하방 — 부분

**핵심 주장:** $250m 순현금과 차입으로 시총 20% 매입 여력이 있다.

**이 주장이 성립하려면:** 매입이 낮은 가격에서 주식수를 실질 축소

**사전 반증조건:** M&A가 현금과 부채여력을 흡수

**실제 결과:** 자본은 결국 대형 인수에도 배분됐다.

#### 4. 인수·재평가 — 가격 적중·촉매 오판

**핵심 주장:** 14~15배 FCF 또는 전략적 매각으로 $60~65가 된다.

**이 주장이 성립하려면:** margin 회복과 cash conversion 확인

**사전 반증조건:** 독립존속하며 FCF 악화

**실제 결과:** 매각 없이도 목표와 장기 가격을 초과했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 보안침해와 캐나다 가격경쟁으로 눌린 GPN을 약 10배 2013 FCF, 11배 P/E, 6배 EBITDA에 샀다. 미국 56%·캐나다 15%·유럽 22%·아시아 7%의 매출과 international EBITDA 45%를 가진 6위 미국 acquirer였다. $250m 순현금과 2.5배까지의 레버리지 여력을 이용하면 $600~700m을 추가 조달해 시가총액 약 20%를 매입할 수 있고, 캐나다 margin 안정과 보안사고 종결 뒤 14~15배 FCF인 $60~65로 재평가되거나 Fiserv·PE에 인수될 수 있다고 봤다. | 분할조정 게시월 가격 $20.65에서 2024-01 $133.23으로 약 5.5배 상승했고 원문 $60~65 목표는 분할 전에 이미 달성됐다. 회사는 매각되지 않았지만 Heartland, TSYS, EVO를 인수해 merchant·issuer·software 플랫폼으로 커졌다. 2023 adjusted net revenue $8.67bn, adjusted operating income $3.87bn, adjusted EPS $10.42를 기록했다. 성공은 단기 보안사고 해소만이 아니라 업종 성장과 대규모 M&A에서 왔고, 초기 순현금 하방은 나중의 레버리지 위험으로 변했다. |
| 밸류에이션·청구권 | 10x FCF→14~15x, 목표 $60~65(분할 전) | $20.65 조정가→$133.23; 약 +545%, 배당 제외 |
| 촉매·시간 | 보안사고 처리와 캐나다 margin 안정 | 첫 확인 2013-07-29 |
| 사전 반증 | 대형은행·ISO 계약 상실 | 낮은 FCF 배수, 회복 가능한 사건성 악재, 자본배분 여력을 함께 본 것이 맞았다. 다만 ‘인수대상’은 실현되지 않았고, 결과적으로 GPN이 인수자가 되면서 원문이 예상하지 않은 통합·부채·무형자산 위험을 떠안았다. |

### 실제 전개와 투자 결론

분할조정 게시월 가격 $20.65에서 2024-01 $133.23으로 약 5.5배 상승했고 원문 $60~65 목표는 분할 전에 이미 달성됐다. 회사는 매각되지 않았지만 Heartland, TSYS, EVO를 인수해 merchant·issuer·software 플랫폼으로 커졌다. 2023 adjusted net revenue $8.67bn, adjusted operating income $3.87bn, adjusted EPS $10.42를 기록했다. 성공은 단기 보안사고 해소만이 아니라 업종 성장과 대규모 M&A에서 왔고, 초기 순현금 하방은 나중의 레버리지 위험으로 변했다.

**종합판정: 매우 성공.** 낮은 FCF 배수, 회복 가능한 사건성 악재, 자본배분 여력을 함께 본 것이 맞았다. 다만 ‘인수대상’은 실현되지 않았고, 결과적으로 GPN이 인수자가 되면서 원문이 예상하지 않은 통합·부채·무형자산 위험을 떠안았다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $43.25 / 조정 $20.65 | $60~65 | $133.23 | 매우 성공 |
| 2013 FCF 배수 | 약 10x | 14~15x | 목표 달성 | 적중 |
| FY2023 조정순매출 | 당시 소형 acquirer | secular+국제 성장 | $8.67bn | 초과 |
| FY2023 조정 EPS | 2013E 저평가 | 복리 증가 | $10.42 | 적중 |

재사용 질문: **대형은행·ISO 계약 상실**

## 2024-01-31 기준 기업 결론

2012 GPN 롱은 낮은 FCF 배수와 사건성 악재 회복을 잡아 매우 성공했다. 다만 예상한 전략적 매각 대신 회사가 연속 인수자가 됐으므로 오늘 같은 분석에서는 순현금·buyback 옵션을 대형 M&A·부채 위험과 동시에 써야 한다.

## 주요 근거

- [VIC Global Payments 2012-11-06 원문](https://www.valueinvestorsclub.com/idea/GLOBAL_PAYMENTS_INC/1158651909)
- [Global Payments FY2023 Results](https://investors.globalpayments.com/news-events/press-releases/detail/449/global-payments-reports-fourth-quarter-and-full-year-2023)
- [Global Payments 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/1123360/000119312513301303/d572603d10k.htm)
- [Global Payments and TSYS Merger Completion](https://investors.globalpayments.com/news-events/press-releases/detail/192/global-payments-and-tsys-complete-merger-of-equals)
- [Global Payments historical prices](https://www.digrin.com/stocks/detail/GPN/price)


---

# PayPal (PYPL) — 기업과 비즈니스

PayPal은 소비자 지갑과 가맹점 checkout을 연결하는 양면 디지털 결제 플랫폼이다. PayPal branded checkout과 Venmo·Braintree·PayPal Complete Payments, 해외송금·BNPL·merchant services를 제공한다. 총결제액(TPV)에 take rate를 적용한 거래매출과 신용·이자·기타 서비스 수익을 얻고, 카드 네트워크·은행에 주는 funding 비용, 거래손실·신용손실, 고객지원·기술·마케팅을 부담한다. ACH나 PayPal balance 자금원은 카드보다 싸지만 Braintree 같은 대형 비브랜드 처리는 take rate와 margin이 낮다. 따라서 TPV와 계정 수보다 branded checkout 성장, transactions per active, transaction margin dollars, funding mix, loss rate와 FCF/주가 중요하다. 소비자와 가맹점이 모두 있어 네트워크 효과가 존재하지만 Apple Pay·Shop Pay·카드 네트워크 토큰화와 대형가맹점 협상력이 checkout 점유율과 가격을 제한한다.

## 돈을 버는 구조

- branded checkout·Braintree·Venmo의 거래수익
- 카드/ACH/balance funding 비용 차감
- 신용·거래손실과 기술·support·마케팅 비용
- TPV보다 transaction margin dollars·FCF/주가 핵심

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2016-09-06 | Long | Long | eBay 분사 후 TPV·Venmo 옵션 롱 | $40.97→$73.62 2017년 말; +80%. 2024-01 $61.35 | 성공 |
| 2021-12-15 | Long | Long | 40% 급락 뒤 branded network 재가속 롱 | $185→$61.35; 약 -66.8% | 치명적 실패 |
| 2022-06-28 | Long | Long | 5.8% FCF yield의 profitable engagement 전환 롱 | $69.84→$61.35; 약 -12.2%, 3~5년 horizon 미도래 | 초기 실패·장기 미판정 |

## 1. 2016-09-06 — eBay 분사 후 TPV·Venmo 옵션 롱

### 원 투자논지

분사 직후 188m 소비자계정·14m 가맹점·2015년 4.9bn 거래를 가진 PayPal을 전자상거래 성장의 대표 청구권으로 봤다. take rate 2.8%는 대형가맹점·P2P mix 때문에 하락하더라도 ACH와 balance funding, 약 60% transaction gross margin, 고정비 레버리지가 이를 상쇄한다고 주장했다. Braintree의 Uber·Airbnb 고객과 Q2 $4bn, +140% 성장한 Venmo는 아직 거의 monetization되지 않은 옵션이었다. $2bn+ FCF, 약 5% EV/FCF yield에서 2018E EBITDA $3.6bn에 15배를 적용해 2017년 말 34% upside를 제시했다.

### 논지를 구성한 핵심 주장

#### 1. 전자상거래 TPV — 적중

**핵심 주장:** 온라인 침투와 checkout 편의가 TPV 20% 성장을 만든다.

**이 주장이 성립하려면:** PayPal checkout share와 merchant acceptance 유지

**사전 반증조건:** branded checkout 성장 한 자릿수 고착

**실제 결과:** 초기 수년 TPV와 매출이 빠르게 성장했다.

#### 2. funding economics — 부분

**핵심 주장:** ACH·balance mix와 고정비 레버리지가 take-rate 하락을 상쇄한다.

**이 주장이 성립하려면:** transaction expense 증가가 TPV보다 느림

**사전 반증조건:** Braintree/card mix로 transaction margin dollars 둔화

**실제 결과:** 장기에는 margin 압력이 커졌다.

#### 3. Venmo 옵션 — 부분~적중

**핵심 주장:** 빠른 P2P 성장 뒤 Pay with Venmo가 수익화된다.

**이 주장이 성립하려면:** commerce·card 이용이 높은 margin 수익으로 전환

**사전 반증조건:** 사용자는 늘어도 수익/사용자 정체

**실제 결과:** 수익화는 됐지만 원 기대보다 느리고 제한적이었다.

#### 4. 낮은 FCF 배수 — 적중

**핵심 주장:** 5% FCF yield에서 성장 옵션을 싸게 산다.

**이 주장이 성립하려면:** FCF/주 성장과 적정 자사주 매입

**사전 반증조건:** SBC·인수와 margin 하락이 FCF/주 상쇄

**실제 결과:** 목표기간 수익은 크게 달성했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 분사 직후 188m 소비자계정·14m 가맹점·2015년 4.9bn 거래를 가진 PayPal을 전자상거래 성장의 대표 청구권으로 봤다. take rate 2.8%는 대형가맹점·P2P mix 때문에 하락하더라도 ACH와 balance funding, 약 60% transaction gross margin, 고정비 레버리지가 이를 상쇄한다고 주장했다. Braintree의 Uber·Airbnb 고객과 Q2 $4bn, +140% 성장한 Venmo는 아직 거의 monetization되지 않은 옵션이었다. $2bn+ FCF, 약 5% EV/FCF yield에서 2018E EBITDA $3.6bn에 15배를 적용해 2017년 말 34% upside를 제시했다. | 게시월 $40.97에서 2017년 말 $73.62로 약 +80% 올라 목표기간과 목표수익을 초과했다. 2024-01에도 $61.35로 진입 대비 약 +50%였다. PayPal과 Braintree TPV는 크게 성장하고 Venmo도 대형 앱이 됐지만, 낮은-margin 비브랜드 처리 mix와 경쟁으로 take rate·transaction margin 압박이 현실화됐다. 초기 논지는 성공했으나 2021년 이후 같은 성장배수를 영구화할 수 있다는 의미는 아니다. |
| 밸류에이션·청구권 | 2018E EBITDA $3.6bn×15; 약 34% upside | $40.97→$73.62 2017년 말; +80%. 2024-01 $61.35 |
| 촉매·시간 | 2017년 TPV·Venmo 성장과 목표가 달성 | 첫 확인 2017-12-29 |
| 사전 반증 | branded checkout 성장 한 자릿수 고착 | 5% FCF yield로 하방을 두고 Braintree·Venmo를 옵션으로 산 구조가 좋았다. 정확한 부분은 전자상거래·TPV 성장이고, 부정확한 부분은 규모가 take-rate 하락을 자동으로 상쇄한다는 장기 가정이었다. |

### 실제 전개와 투자 결론

게시월 $40.97에서 2017년 말 $73.62로 약 +80% 올라 목표기간과 목표수익을 초과했다. 2024-01에도 $61.35로 진입 대비 약 +50%였다. PayPal과 Braintree TPV는 크게 성장하고 Venmo도 대형 앱이 됐지만, 낮은-margin 비브랜드 처리 mix와 경쟁으로 take rate·transaction margin 압박이 현실화됐다. 초기 논지는 성공했으나 2021년 이후 같은 성장배수를 영구화할 수 있다는 의미는 아니다.

**종합판정: 성공.** 5% FCF yield로 하방을 두고 Braintree·Venmo를 옵션으로 산 구조가 좋았다. 정확한 부분은 전자상거래·TPV 성장이고, 부정확한 부분은 규모가 take-rate 하락을 자동으로 상쇄한다는 장기 가정이었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $40.97 | 2017년 말 +34% | $73.62; +80% | 성공 |
| 계정 | 188m | 지속 증가 | 426m FY2023 | 적중 |
| FCF | >$2bn | 성장 | 2023 약 $4bn대 | 방향 적중 |
| take rate | 2.8%, 하락 예상 | 레버리지로 상쇄 | mix 압력 지속 | 부분 |

재사용 질문: **branded checkout 성장 한 자릿수 고착**

## 2. 2021-12-15 — 40% 급락 뒤 branded network 재가속 롱

### 원 투자논지

고점 대비 약 40% 하락한 $185에서 400m 소비자·35m 가맹점을 가진 branded 양면망의 moat가 훼손되지 않았다고 봤다. eBay headwind가 2022년 상반기에 끝나고 하반기 매출이 20%로 재가속하며 core branded FCF·매출이 3~5년 20% 성장한다고 주장했다. Venmo, BNPL, Super App, Amazon 결제, Paidy·GoPay 등은 추가 옵션이었다. FY2023 EPS $6.65에 35배를 적용한 2022년 말 $230, FY2026 이후에도 두 자릿수 성장을 놓는 DCF $315~330을 제시했다.

### 논지를 구성한 핵심 주장

#### 1. branded moat — 실패

**핵심 주장:** PayPal 브랜드 checkout이 3~5년 20% FCF 성장을 지킨다.

**이 주장이 성립하려면:** branded TPV가 시장과 함께 성장하고 margin 유지

**사전 반증조건:** 비브랜드만 성장·transaction margin dollars 둔화

**실제 결과:** Braintree mix가 커지고 branded 성장 우려가 확대됐다.

#### 2. eBay 이후 재가속 — 실패

**핵심 주장:** headwind 종료 뒤 2H22 매출이 20%로 회복된다.

**이 주장이 성립하려면:** ex-eBay 유기성장과 이용빈도 상승

**사전 반증조건:** 두 자릿수 초반 이하로 guidance 하락

**실제 결과:** 재가속 폭이 크게 미달했다.

#### 3. Venmo·Amazon — 실패

**핵심 주장:** Amazon acceptance가 Venmo 상거래 수익화를 연다.

**이 주장이 성립하려면:** merchant volume과 수익/사용자 증가

**사전 반증조건:** 파트너십 종료 또는 economics 미미

**실제 결과:** Amazon 결제는 2024-01 종료됐다.

#### 4. 35배 EPS — 치명적 실패

**핵심 주장:** 질 높은 네트워크에 FY23 EPS 35배가 합리적이다.

**이 주장이 성립하려면:** 20% EPS 성장 duration 가시화

**사전 반증조건:** 성장률·배수 동시 하락

**실제 결과:** 주가는 3분의 1 수준으로 하락했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 고점 대비 약 40% 하락한 $185에서 400m 소비자·35m 가맹점을 가진 branded 양면망의 moat가 훼손되지 않았다고 봤다. eBay headwind가 2022년 상반기에 끝나고 하반기 매출이 20%로 재가속하며 core branded FCF·매출이 3~5년 20% 성장한다고 주장했다. Venmo, BNPL, Super App, Amazon 결제, Paidy·GoPay 등은 추가 옵션이었다. FY2023 EPS $6.65에 35배를 적용한 2022년 말 $230, FY2026 이후에도 두 자릿수 성장을 놓는 DCF $315~330을 제시했다. | 2024-01 가격은 $61.35로 $185 대비 약 -67%였고 $230 목표는 실패했다. eBay 감소는 끝났지만 branded checkout이 기대만큼 재가속하지 않았고 성장의 더 큰 몫이 낮은-margin Braintree에서 나왔다. 회사는 2022년 750m 계정 목표를 사실상 철회했고 2023 active accounts는 426m로 2% 감소했다. Amazon의 Venmo 결제도 2024-01 종료됐다. TPV와 FCF는 남았지만 35배가 정당화될 growth duration은 사라졌다. |
| 밸류에이션·청구권 | FY23 EPS $6.65×35=$230; DCF $315~330 | $185→$61.35; 약 -66.8% |
| 촉매·시간 | 2022 Q4 계정목표 철회·성장 guidance reset | 첫 확인 2022-02-01 |
| 사전 반증 | 비브랜드만 성장·transaction margin dollars 둔화 | 일시적 eBay 기저효과를 구조적 checkout 경쟁과 분리하지 못했고, 거래량 증가를 고마진 branded economics로 환산했다. 35배 terminal multiple과 20% 성장, 여러 옵션을 동시에 요구해 안전마진이 없었다. |

### 실제 전개와 투자 결론

2024-01 가격은 $61.35로 $185 대비 약 -67%였고 $230 목표는 실패했다. eBay 감소는 끝났지만 branded checkout이 기대만큼 재가속하지 않았고 성장의 더 큰 몫이 낮은-margin Braintree에서 나왔다. 회사는 2022년 750m 계정 목표를 사실상 철회했고 2023 active accounts는 426m로 2% 감소했다. Amazon의 Venmo 결제도 2024-01 종료됐다. TPV와 FCF는 남았지만 35배가 정당화될 growth duration은 사라졌다.

**종합판정: 치명적 실패.** 일시적 eBay 기저효과를 구조적 checkout 경쟁과 분리하지 못했고, 거래량 증가를 고마진 branded economics로 환산했다. 35배 terminal multiple과 20% 성장, 여러 옵션을 동시에 요구해 안전마진이 없었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $185 | $230 2022년 말 | $61.35 | 치명적 실패 |
| active accounts | 400m | 750m 장기 목표 | 426m, 2023 -2% | 실패 |
| 매출 성장 | 2H22 20% | 재가속 | 2023 약 8% | 실패 |
| Amazon Venmo | 성장 옵션 | 상거래 확장 | 2024-01 종료 | 실패 |

재사용 질문: **비브랜드만 성장·transaction margin dollars 둔화**

## 3. 2022-06-28 — 5.8% FCF yield의 profitable engagement 전환 롱

### 원 투자논지

EV 약 $89bn, 약 $5bn FCF로 5.8% FCF yield, 17.7배 P/E, 12.3배 EV/EBITDA인 PayPal이 5년 평균 대비 약 50% 할인됐다고 봤다. 회사가 저품질 계정 유치에서 profitable engagement로 전환한 것은 올바른 reset이며, 마지막 eBay $200m 역풍이 Q2에 끝나면 두 자릿수 매출·이익 성장으로 돌아간다고 주장했다. CFO 이탈과 신뢰 훼손은 가격에 반영됐고 Venmo의 80m 사용자와 Amazon은 공짜 옵션, 보유기간 3~5년을 제시했다.

### 논지를 구성한 핵심 주장

#### 1. profitable engagement — 부분

**핵심 주장:** 저품질 계정 대신 활동·수익성에 집중하면 질이 좋아진다.

**이 주장이 성립하려면:** transactions/active와 margin dollars 증가

**사전 반증조건:** 계정감소와 branded 둔화가 비용절감보다 큼

**실제 결과:** 전략은 실행됐으나 성장 회복은 제한됐다.

#### 2. eBay 종료 — 실패

**핵심 주장:** 마지막 $200m 역풍 뒤 두 자릿수 성장이 재개된다.

**이 주장이 성립하려면:** ex-eBay branded revenue 재가속

**사전 반증조건:** 매출 성장 한 자릿수 지속

**실제 결과:** 2023 매출은 약 8% 성장에 그쳤다.

#### 3. Venmo 옵션 — 실패

**핵심 주장:** 80m 사용자와 Amazon이 저평가된 상거래 옵션이다.

**이 주장이 성립하려면:** 결제액·수익/사용자 증가

**사전 반증조건:** Amazon 계약 종료

**실제 결과:** Amazon 결제는 기준일 무렵 종료됐다.

#### 4. FCF 하방 — 부분~적중

**핵심 주장:** 5.8% FCF yield가 낮은 성장에서도 하방을 지킨다.

**이 주장이 성립하려면:** FCF/주 유지와 buyback 상쇄

**사전 반증조건:** transaction margin 훼손·과도한 SBC

**실제 결과:** 가격 하락은 제한적이었고 FCF는 남았다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | EV 약 $89bn, 약 $5bn FCF로 5.8% FCF yield, 17.7배 P/E, 12.3배 EV/EBITDA인 PayPal이 5년 평균 대비 약 50% 할인됐다고 봤다. 회사가 저품질 계정 유치에서 profitable engagement로 전환한 것은 올바른 reset이며, 마지막 eBay $200m 역풍이 Q2에 끝나면 두 자릿수 매출·이익 성장으로 돌아간다고 주장했다. CFO 이탈과 신뢰 훼손은 가격에 반영됐고 Venmo의 80m 사용자와 Amazon은 공짜 옵션, 보유기간 3~5년을 제시했다. | 게시월 $69.84에서 2024-01 $61.35로 약 -12%여서 기준일까지 가격은 실패했다. 3~5년 보유기간 중 19개월만 지난 시점이라 최종판정은 이르다. 계정수보다 engagement와 비용규율에 집중한 전환은 맞았고 FCF도 유지됐지만, 2023 매출 성장 약 8%와 active accounts -2%, branded margin 우려로 지속적 두 자릿수 성장 증거는 부족했다. Amazon Venmo 촉매도 종료됐다. |
| 밸류에이션·청구권 | $5bn FCF, 5.8% yield; 17.7x P/E | $69.84→$61.35; 약 -12.2%, 3~5년 horizon 미도래 |
| 촉매·시간 | 2022~23 active accounts 감소와 저성장 | 첫 확인 2023-02-09 |
| 사전 반증 | 계정감소와 branded 둔화가 비용절감보다 큼 | 2021 글보다 진입배수와 downside 규율이 훨씬 낫고 전략 reset도 맞았다. 그러나 과거 평균배수를 정상값으로 삼고 eBay 종료 뒤 재가속과 Venmo 촉매를 너무 빨리 확정했다. 기준일에는 초기 실패이며 장기 논지는 미판정이다. |

### 실제 전개와 투자 결론

게시월 $69.84에서 2024-01 $61.35로 약 -12%여서 기준일까지 가격은 실패했다. 3~5년 보유기간 중 19개월만 지난 시점이라 최종판정은 이르다. 계정수보다 engagement와 비용규율에 집중한 전환은 맞았고 FCF도 유지됐지만, 2023 매출 성장 약 8%와 active accounts -2%, branded margin 우려로 지속적 두 자릿수 성장 증거는 부족했다. Amazon Venmo 촉매도 종료됐다.

**종합판정: 초기 실패·장기 미판정.** 2021 글보다 진입배수와 downside 규율이 훨씬 낫고 전략 reset도 맞았다. 그러나 과거 평균배수를 정상값으로 삼고 eBay 종료 뒤 재가속과 Venmo 촉매를 너무 빨리 확정했다. 기준일에는 초기 실패이며 장기 논지는 미판정이다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $69.84 | 3~5년 복리 | $61.35 | 초기 실패 |
| FCF | 약 $5bn | 지속·성장 | 2023 약 $4bn대 | 부분 |
| active accounts | engagement 전환 | 질 개선 | 426m, -2% | 부분 |
| 매출 | 두 자릿수 | eBay 후 재가속 | 2023 약 8% | 미달 |

재사용 질문: **계정감소와 branded 둔화가 비용절감보다 큼**

## 2024-01-31 기준 기업 결론

2016 롱은 낮은 FCF 배수에서 Braintree·Venmo 옵션을 산 성공이지만 2021 롱은 같은 자산에 35배와 20% 성장 duration을 지불해 치명적으로 실패했다. 2022 롱은 valuation 규율이 개선됐으나 기준일 초기수익은 음수이고 3~5년 horizon은 미도래다.

## 주요 근거

- [VIC PayPal 2016-09-06 원문](https://www.valueinvestorsclub.com/idea/Paypal/8404072826)
- [PayPal FY2023 Results](https://newsroom.paypal-corp.com/2024-02-07-PayPal-Reports-Fourth-Quarter-and-Full-Year-2023-Results)
- [PayPal 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1633917/000163391724000023/pypl-20231231.htm)
- [PayPal and Amazon Enable Venmo](https://newsroom.paypal-corp.com/2021-11-08-PayPal-and-Amazon-to-Enable-Customers-to-Pay-with-Venmo-at-Checkout)
- [PayPal historical prices](https://www.digrin.com/stocks/detail/PYPL/price)
- [VIC PayPal 2021-12-15 원문](https://www.valueinvestorsclub.com/idea/PAYPAL_HOLDINGS_INC/7715148969)
- [VIC PayPal 2022-06-28 원문](https://www.valueinvestorsclub.com/idea/PAYPAL_HOLDINGS_INC/2318098394)


---

# Block / Square (SQ) — 기업과 비즈니스

Square에서 이름을 바꾼 Block은 두 생태계를 묶은 핀테크다. Square는 소상공인에게 카드수납, POS, 주문·인사·급여·마케팅 소프트웨어와 대출·즉시입금을 제공하고, Cash App은 개인에게 P2P, debit card, direct deposit, 주식·비트코인, 대출과 상거래 기능을 제공한다. Afterpay는 BNPL을 양쪽 생태계에 연결한다. Square는 GPV에 붙는 처리 spread와 소프트웨어 구독·금융서비스에서, Cash App은 Cash App Card interchange, instant transfer, bitcoin spread, 사업자 결제와 금융상품에서 gross profit을 번다. 비트코인 매출은 대부분 원가가 통과하므로 GAAP 매출보다 gross profit이 경제성을 잘 보여준다. 강점은 빠른 self-serve onboarding, 결제·소프트웨어 통합, 거래데이터 기반 underwriting과 Cash App의 social network다. 위험은 소상공인 경기민감도, fraud·credit loss, 경쟁, 낮은 GAAP 수익성, SBC·인수 주식발행과 창업자 지배구조다. 핵심 지표는 Square GPV·gross profit retention, Cash App monthly transacting actives·inflows·gross profit, 조정영업이익과 완전희석 주식수다.

## 돈을 버는 구조

- Square 처리 spread·software·seller banking
- Cash App Card interchange·instant transfer·bitcoin spread
- Afterpay BNPL·광고·merchant discovery
- gross profit에서 opex·SBC·credit loss·희석 차감

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 실제 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2016-11-25 | Short | Long | micro-merchant moat·40% margin 롱 | $12.94→$69.12 3년; +434%. 2024-01 $65.01 | 매우 성공 |
| 2018-07-02 | Short | Short | Clover 추월·Capital cyclicality 숏 | $64.65 게시월→$65.01; 거의 0%. 중간 최고 $268.07로 치명적 squeeze | 실패 |
| 2019-06-19 | Short | Long | seller cohort·Cash App 고성장 롱 | $72.53 게시월→$65.01; 약 -10.4%. 중간 큰 상승 후 반납 | 사업 적중·주가 부분 실패 |
| 2021-03-02 | Short | Long | GAAP 통과매출 제거 후 30% IRR 롱 | $227.05→$65.01; 약 -71.4% | 치명적 실패 |
| 2021-06-05 | Short | Long | Cash App 숨은 TPV·Boost monetization 롱 | $243.80→$65.01; 약 -73.3% | 치명적 실패 |

## 1. 2016-11-25 — micro-merchant moat·40% margin 롱

### 원 투자논지

SQL은 Short지만 본문은 명백한 Long이다. 5분 onboarding, $14 CAC 대 전통 acquirer $90~238, 12~15개월 payback과 낮은 fraud를 micro-merchant moat로 봤다. 큰 seller의 GPV가 55% 성장해 전체의 43%가 됐고 take rate도 안정돼 ‘상향이동 불가’ 숏 논지를 반박했다. 고객 2.5m이 10년 뒤 8m, 매출 20% CAGR, EBITDA margin 40%+, 2026 완전희석 484m주를 가정해 3년 base upside 90%, downside 20%, risk-adjusted IRR 20%를 제시했다.

### 논지를 구성한 핵심 주장

#### 1. CAC·payback — 적중

**핵심 주장:** $14 CAC와 12~15개월 payback이 micro seller economics를 만든다.

**이 주장이 성립하려면:** cohort gross profit retention과 낮은 loss

**사전 반증조건:** CAC 상승·12개월 후 cohort 수익 감소

**실제 결과:** seller ecosystem과 gross profit이 크게 성장했다.

#### 2. upmarket — 적중

**핵심 주장:** 큰 seller가 Square에 남아 GPV mix가 확대된다.

**이 주장이 성립하려면:** software/API가 복잡한 요구를 충족

**사전 반증조건:** take rate 급락·큰 seller churn

**실제 결과:** upmarket과 omnichannel가 실제 성장축이 됐다.

#### 3. 40% margin — 미판정~공격적

**핵심 주장:** 고정비 레버리지로 2026 EBITDA margin 40%+다.

**이 주장이 성립하려면:** gross profit보다 opex가 느리게 증가

**사전 반증조건:** SBC·신사업 투자로 margin 장기 미달

**실제 결과:** 2024 기준 아직 크게 미달하며 기한 미도래다.

#### 4. 희석 포함 upside — 초과 적중

**핵심 주장:** 100m주 희석을 넣어도 3년 90% upside다.

**이 주장이 성립하려면:** 매출 성장과 배수 방어

**사전 반증조건:** 경쟁·경기둔화로 성장/배수 동시 하락

**실제 결과:** 3년 가격은 약 5.3배가 됐다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | SQL은 Short지만 본문은 명백한 Long이다. 5분 onboarding, $14 CAC 대 전통 acquirer $90~238, 12~15개월 payback과 낮은 fraud를 micro-merchant moat로 봤다. 큰 seller의 GPV가 55% 성장해 전체의 43%가 됐고 take rate도 안정돼 ‘상향이동 불가’ 숏 논지를 반박했다. 고객 2.5m이 10년 뒤 8m, 매출 20% CAGR, EBITDA margin 40%+, 2026 완전희석 484m주를 가정해 3년 base upside 90%, downside 20%, risk-adjusted IRR 20%를 제시했다. | 게시월 $12.94에서 2019-11 $69.12로 3년 약 +434%, 2024-01 $65.01로 약 +402%였다. Square는 큰 seller·소프트웨어·금융으로 확대했고 Cash App이라는 원문에 작게 반영된 두 번째 엔진이 폭발적으로 성장했다. 다만 2026 40% EBITDA margin은 기준일 미도래이며, 2023에도 GAAP 수익성은 원 장기모델보다 낮았다. 성공은 margin 목표 정확성보다 낮은 진입가와 TAM·cohort economics에서 왔다. |
| 밸류에이션·청구권 | 2026 EPS 역산; 3년 -20%/+90%, risk-adjusted IRR +20% | $12.94→$69.12 3년; +434%. 2024-01 $65.01 |
| 촉매·시간 | 2017~19 큰 seller·Cash App 성장 | 첫 확인 2019-11-29 |
| 사전 반증 | CAC 상승·12개월 후 cohort 수익 감소 | CAC·payback·retention을 merchant cohort 단위로 본 것이 강했고 희석 100m주까지 모델링했다. 40% margin 같은 먼 terminal 가정은 불필요하게 공격적이었지만 낮은 가격이 오류를 흡수했다. |

### 실제 전개와 투자 결론

게시월 $12.94에서 2019-11 $69.12로 3년 약 +434%, 2024-01 $65.01로 약 +402%였다. Square는 큰 seller·소프트웨어·금융으로 확대했고 Cash App이라는 원문에 작게 반영된 두 번째 엔진이 폭발적으로 성장했다. 다만 2026 40% EBITDA margin은 기준일 미도래이며, 2023에도 GAAP 수익성은 원 장기모델보다 낮았다. 성공은 margin 목표 정확성보다 낮은 진입가와 TAM·cohort economics에서 왔다.

**종합판정: 매우 성공.** CAC·payback·retention을 merchant cohort 단위로 본 것이 강했고 희석 100m주까지 모델링했다. 40% margin 같은 먼 terminal 가정은 불필요하게 공격적이었지만 낮은 가격이 오류를 흡수했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $12.94 | 3년 +90% | $69.12 3년 | 매우 성공 |
| 큰 seller GPV | +55%, mix 43% | 지속 확대 | upmarket 지속 | 적중 |
| 매출 CAGR | 10년 20% | 장기 | gross profit 고성장 | 방향 적중 |
| EBITDA margin | 9% | 2026 40%+ | 기준일 미도래·GAAP 낮음 | 미판정 |

재사용 질문: **CAC 상승·12개월 후 cohort 수익 감소**

## 2. 2018-07-02 — Clover 추월·Capital cyclicality 숏

### 원 투자논지

$62에서 목표 $36, 약 40% 하락을 제시한 Short다. First Data의 Clover가 은행 distribution과 디지털 onboarding으로 50% 성장해 2020년 Square를 추월하고 core processing이 둔화된다고 봤다. 성장의 상당 부분이 Instant Deposit과 Square Capital 같은 경기민감 수익이며 은행이 Capital 대출매입을 중단하면 EBIT가 약 35% 감소한다고 추정했다. seller의 약 60%가 연매출 $125k 미만이라 침체에 취약하고, 20배 매출·68배 EBITDA인데 2018 stock compensation $215m이 EBITDA $245m과 비슷하며 주식수가 2016 360m에서 2018 480m으로 늘었다고 비판했다.

### 논지를 구성한 핵심 주장

#### 1. Clover 추월 — 실패

**핵심 주장:** Clover가 은행채널로 2020년 Square를 추월해 core를 둔화시킨다.

**이 주장이 성립하려면:** Clover 성장과 Square seller churn 동시 발생

**사전 반증조건:** 둘 다 성장·Square retention 유지

**실제 결과:** 경쟁은 강했지만 Square도 빠르게 성장했다.

#### 2. cyclical add-ons — 부분

**핵심 주장:** Instant Deposit·Capital이 고성장을 과장한다.

**이 주장이 성립하려면:** 침체 때 originations·fee와 EBIT 급감

**사전 반증조건:** Cash App·software가 손실 상쇄

**실제 결과:** 위험은 맞았지만 전체 thesis를 깨지 못했다.

#### 3. SBC 희석 — 적중

**핵심 주장:** 조정 EBITDA와 비슷한 SBC가 주주경제성을 훼손한다.

**이 주장이 성립하려면:** 완전희석 주식수 지속 급증

**사전 반증조건:** gross profit/주가 희석보다 빠르게 성장

**실제 결과:** 희석 우려는 이후에도 유효했다.

#### 4. $36 목표 — 실패

**핵심 주장:** 68배 EBITDA가 정상화되면 약 40% 하락한다.

**이 주장이 성립하려면:** core 성장 둔화가 빠르게 확인

**사전 반증조건:** 신사업으로 성장률·배수 유지

**실제 결과:** 기준일에도 진입가 수준, 중간 큰 손실이었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $62에서 목표 $36, 약 40% 하락을 제시한 Short다. First Data의 Clover가 은행 distribution과 디지털 onboarding으로 50% 성장해 2020년 Square를 추월하고 core processing이 둔화된다고 봤다. 성장의 상당 부분이 Instant Deposit과 Square Capital 같은 경기민감 수익이며 은행이 Capital 대출매입을 중단하면 EBIT가 약 35% 감소한다고 추정했다. seller의 약 60%가 연매출 $125k 미만이라 침체에 취약하고, 20배 매출·68배 EBITDA인데 2018 stock compensation $215m이 EBITDA $245m과 비슷하며 주식수가 2016 360m에서 2018 480m으로 늘었다고 비판했다. | 게시월 $64.65에서 2024-01 $65.01로 사실상 보합이라 고정 종착점에서도 수익이 없었고 $36 목표는 실패했다. 더 치명적인 것은 2018-09 $99, 2021-08 $268까지의 squeeze로 숏 보유경로가 감당하기 어려웠다는 점이다. Clover 경쟁, SBC, 소상공인 경기·대출 위험은 맞았고 2022년 이후 valuation이 압축됐지만 Cash App과 seller software라는 성장축을 과소평가했다. |
| 밸류에이션·청구권 | 20x sales·68x EBITDA→30x 2020 EPS $1.20=$36 | $64.65 게시월→$65.01; 거의 0%. 중간 최고 $268.07로 치명적 squeeze |
| 촉매·시간 | 2018~21 Cash App·gross profit 성장으로 숏 반증 | 첫 확인 2019-02-27 |
| 사전 반증 | 둘 다 성장·Square retention 유지 | SBC를 비용으로 보고 대출자금·경기민감도를 stress한 분석은 좋았다. 그러나 경쟁사의 빠른 성장만으로 Square의 절대성장이 멈춘다고 본 zero-sum 오류와 Cash App 누락 때문에 catalyst timing과 목표가가 틀렸다. |

### 실제 전개와 투자 결론

게시월 $64.65에서 2024-01 $65.01로 사실상 보합이라 고정 종착점에서도 수익이 없었고 $36 목표는 실패했다. 더 치명적인 것은 2018-09 $99, 2021-08 $268까지의 squeeze로 숏 보유경로가 감당하기 어려웠다는 점이다. Clover 경쟁, SBC, 소상공인 경기·대출 위험은 맞았고 2022년 이후 valuation이 압축됐지만 Cash App과 seller software라는 성장축을 과소평가했다.

**종합판정: 실패.** SBC를 비용으로 보고 대출자금·경기민감도를 stress한 분석은 좋았다. 그러나 경쟁사의 빠른 성장만으로 Square의 절대성장이 멈춘다고 본 zero-sum 오류와 Cash App 누락 때문에 catalyst timing과 목표가가 틀렸다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $62 / 월말 $64.65 | $36 | $65.01 | 실패 |
| 중간 최고 | 숏 | 하락 | $268.07 2021-08 | 치명적 경로 |
| SBC | $215m vs EBITDA $245m | 희석 부담 | 주식기준보상 지속 | 적중 |
| Clover | 50% 성장 | 2020 추월 | Square 절대성장 지속 | 인과 미달 |

재사용 질문: **둘 다 성장·Square retention 유지**

## 3. 2019-06-19 — seller cohort·Cash App 고성장 롱

### 원 투자논지

SQL은 Short지만 본문은 Long이다. seller 획득비용을 3~4분기에 회수하고 이후 cohort 매출이 커지는 높은 ROIC 구조, 5개국 소비지출 $9tn 대비 trailing GPV 약 $90bn의 침투여력, hardware·payments·payroll·CRM·Weebly를 묶은 ecosystem을 강조했다. Cash App은 2018년 7.5m MAU를 고객당 약 $21에 확보한 software checking account이며 전통은행보다 CAC가 낮다고 봤다. 장기 매출 25%, EBITDA margin 38%, terminal P/E 25배, 연 3% 희석과 FCF 전환을 넣어 $72.55에서 high-teens IRR을 기대했다.

### 논지를 구성한 핵심 주장

#### 1. seller cohort — 적중

**핵심 주장:** 3~4분기 payback 뒤 cohort 수익이 커진다.

**이 주장이 성립하려면:** gross profit retention>100%와 CAC 안정

**사전 반증조건:** upmarket CAC 급증·seller churn

**실제 결과:** seller gross profit과 제품침투가 확대됐다.

#### 2. Cash App — 적중

**핵심 주장:** $21 수준 CAC의 software checking account가 큰 두 번째 엔진이다.

**이 주장이 성립하려면:** MAU·inflows·수익/active 동시 증가

**사전 반증조건:** P2P 사용만 늘고 monetization 정체

**실제 결과:** 56m monthly transacting actives와 큰 gross profit을 만들었다.

#### 3. 38% margin — 실패~미판정

**핵심 주장:** 투자기가 끝나면 EBITDA margin 약 38%가 된다.

**이 주장이 성립하려면:** opex·SBC가 gross profit보다 느리게 증가

**사전 반증조건:** 신사업·조직비용·SBC가 계속 흡수

**실제 결과:** 2024 기준 원 장기 margin과 괴리가 컸다.

#### 4. high-teens IRR — 실패

**핵심 주장:** 25% 성장에서 3% 희석을 빼도 높은 수익이다.

**이 주장이 성립하려면:** terminal 25배와 FCF 전환

**사전 반증조건:** 배수압축·M&A 희석

**실제 결과:** 기준일 가격은 약 -10%였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | SQL은 Short지만 본문은 Long이다. seller 획득비용을 3~4분기에 회수하고 이후 cohort 매출이 커지는 높은 ROIC 구조, 5개국 소비지출 $9tn 대비 trailing GPV 약 $90bn의 침투여력, hardware·payments·payroll·CRM·Weebly를 묶은 ecosystem을 강조했다. Cash App은 2018년 7.5m MAU를 고객당 약 $21에 확보한 software checking account이며 전통은행보다 CAC가 낮다고 봤다. 장기 매출 25%, EBITDA margin 38%, terminal P/E 25배, 연 3% 희석과 FCF 전환을 넣어 $72.55에서 high-teens IRR을 기대했다. | Cash App과 seller gross profit은 크게 성장했고 2023 Block gross profit은 약 $7.5bn, GPV $227.7bn이 됐다. 하지만 2024-01 가격 $65.01은 진입가보다 약 -10%로 장기 주가결론은 기준일까지 실패했다. 2021년에는 3배 이상 올랐으나 이후 배수압축, 비용, SBC와 Afterpay 주식발행이 수익을 되돌렸다. 사업 질 통찰은 맞았지만 38% margin·25배 terminal과 실제 주당가치 사이 연결은 약했다. |
| 밸류에이션·청구권 | 25% 성장·38% EBITDA·25x terminal P/E·3% 희석으로 high-teens IRR | $72.53 게시월→$65.01; 약 -10.4%. 중간 큰 상승 후 반납 |
| 촉매·시간 | 2022 Afterpay 주식발행과 성장주 배수압축 | 첫 확인 2022-01-31 |
| 사전 반증 | upmarket CAC 급증·seller churn | cohort payback과 Cash App을 동시에 포착한 사업분석은 좋았다. 그러나 ‘회사가 투자 때문에 이익을 숨긴다’에서 ‘언젠가 높은 margin이 주주에게 귀속된다’로 넘어갈 때 비용·SBC·자본배분 검증이 부족했다. |

### 실제 전개와 투자 결론

Cash App과 seller gross profit은 크게 성장했고 2023 Block gross profit은 약 $7.5bn, GPV $227.7bn이 됐다. 하지만 2024-01 가격 $65.01은 진입가보다 약 -10%로 장기 주가결론은 기준일까지 실패했다. 2021년에는 3배 이상 올랐으나 이후 배수압축, 비용, SBC와 Afterpay 주식발행이 수익을 되돌렸다. 사업 질 통찰은 맞았지만 38% margin·25배 terminal과 실제 주당가치 사이 연결은 약했다.

**종합판정: 사업 적중·주가 부분 실패.** cohort payback과 Cash App을 동시에 포착한 사업분석은 좋았다. 그러나 ‘회사가 투자 때문에 이익을 숨긴다’에서 ‘언젠가 높은 margin이 주주에게 귀속된다’로 넘어갈 때 비용·SBC·자본배분 검증이 부족했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $72.55 | high-teens IRR | $65.01 | 부분 실패 |
| GPV | 약 $90bn TTM | $9tn TAM 침투 | $227.7bn FY2023 | 적중 |
| Cash App | 2018 7.5m MAU 추가 | 저비용 성장 | 56m monthly actives 2023-12 | 적중 |
| EBITDA margin | 장기 38% | FCF 전환 | 기준일 크게 미달 | 미달 |

재사용 질문: **upmarket CAC 급증·seller churn**

## 4. 2021-03-02 — GAAP 통과매출 제거 후 30% IRR 롱

### 원 투자논지

SQL은 Short지만 본문은 Long이다. 비트코인과 transaction pass-through를 제거하면 true net revenue가 약 $5bn이고 실제 배수는 headline 8배가 아니라 약 20배라고 정직하게 재구성했다. 그럼에도 seller·Cash App의 topline이 약 40% 성장하면 매년 약 10% multiple compression과 미미한 FCF를 감수해도 5년 IRR 약 30%라고 주장했다. Cash App instant deposit fee가 Fed 실시간결제로 압박받을 위험과, 더 현명한 투자자는 이미 8배 true net revenue·40배 정상수익에 샀다는 점도 인정했다.

### 논지를 구성한 핵심 주장

#### 1. economic revenue — 적중

**핵심 주장:** 비트코인·pass-through를 빼야 실제 매출과 배수가 보인다.

**이 주장이 성립하려면:** gross profit·net revenue 기준 비교

**사전 반증조건:** GAAP 성장률을 그대로 valuation에 사용

**실제 결과:** 분석 프레임은 정확했다.

#### 2. 40% 성장 — 실패

**핵심 주장:** seller와 Cash App이 장기간 약 40% topline 성장한다.

**이 주장이 성립하려면:** cohort·active·수익/active가 동시 성장

**사전 반증조건:** gross profit 성장 20%대로 감속

**실제 결과:** 2023 성장했지만 duration은 크게 미달했다.

#### 3. instant fee — 위험 적중·인과 제한

**핵심 주장:** Fed 실시간결제가 instant deposit 가격력을 압박할 수 있다.

**이 주장이 성립하려면:** 무료 즉시이체가 대체

**사전 반증조건:** 편의·network로 가격 유지

**실제 결과:** FedNow 출시는 됐지만 핵심 붕괴원인은 아니었다.

#### 4. 30% IRR — 치명적 실패

**핵심 주장:** 40% 성장에서 10% 배수압축을 빼면 30% IRR이다.

**이 주장이 성립하려면:** margin·주식수가 안정

**사전 반증조건:** SBC·Afterpay 발행·FCF 미전환

**실제 결과:** 약 -71%로 정반대였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | SQL은 Short지만 본문은 Long이다. 비트코인과 transaction pass-through를 제거하면 true net revenue가 약 $5bn이고 실제 배수는 headline 8배가 아니라 약 20배라고 정직하게 재구성했다. 그럼에도 seller·Cash App의 topline이 약 40% 성장하면 매년 약 10% multiple compression과 미미한 FCF를 감수해도 5년 IRR 약 30%라고 주장했다. Cash App instant deposit fee가 Fed 실시간결제로 압박받을 위험과, 더 현명한 투자자는 이미 8배 true net revenue·40배 정상수익에 샀다는 점도 인정했다. | 게시월 $227.05에서 2024-01 $65.01로 약 -71%였다. 사업 gross profit은 2023 약 $7.5bn까지 성장했으나 40% 성장 duration과 높은 출발배수가 동시에 유지되지 않았다. 2022년 Afterpay 인수로 113.6m주를 발행했고 종결시 공정가치는 $13.8bn이었다. SBC와 투자비용, 금리상승에 따른 multiple compression이 원 모델보다 훨씬 컸다. FedNow는 2023년 출시됐으나 주가 붕괴의 단일 원인은 아니었다. |
| 밸류에이션·청구권 | true net revenue 약 $5bn의 20x; 5년 IRR 약 30% | $227.05→$65.01; 약 -71.4% |
| 촉매·시간 | 2021-08 Afterpay 고가 주식거래 발표와 2022 배수압축 | 첫 확인 2021-08-02 |
| 사전 반증 | GAAP 성장률을 그대로 valuation에 사용 | GAAP 매출의 통과항목을 제거한 것은 정확했지만 20배 economic revenue가 이미 요구하는 성장률을 안전마진 없이 받아들였다. ‘성장 40%-배수압축 10%=IRR 30%’는 margin, FCF, 희석과 자본배분을 생략한 산술이었다. |

### 실제 전개와 투자 결론

게시월 $227.05에서 2024-01 $65.01로 약 -71%였다. 사업 gross profit은 2023 약 $7.5bn까지 성장했으나 40% 성장 duration과 높은 출발배수가 동시에 유지되지 않았다. 2022년 Afterpay 인수로 113.6m주를 발행했고 종결시 공정가치는 $13.8bn이었다. SBC와 투자비용, 금리상승에 따른 multiple compression이 원 모델보다 훨씬 컸다. FedNow는 2023년 출시됐으나 주가 붕괴의 단일 원인은 아니었다.

**종합판정: 치명적 실패.** GAAP 매출의 통과항목을 제거한 것은 정확했지만 20배 economic revenue가 이미 요구하는 성장률을 안전마진 없이 받아들였다. ‘성장 40%-배수압축 10%=IRR 30%’는 margin, FCF, 희석과 자본배분을 생략한 산술이었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $227.05 | 5년 IRR 30% | $65.01 | 치명적 실패 |
| true net revenue 배수 | 약 20x | 40% 성장 | 배수 급락 | 실패 |
| Afterpay 발행 | 미반영 | 주당가치 성장 | 113.6m주 발행 | 실패요인 |
| 2023 gross profit | 고성장 기대 | 40% 지속 | 약 $7.5bn·성장 25% | 부분 |

재사용 질문: **GAAP 성장률을 그대로 valuation에 사용**

## 5. 2021-06-05 — Cash App 숨은 TPV·Boost monetization 롱

### 원 투자논지

SQL은 Short지만 본문은 Long이다. 비트코인·transaction 비용을 제거하고 Cash App Card·Boost·Instant Transfer가 subscription revenue로 분류돼 TPV와 take rate 화면에서 빠지는 점을 조정하면 경제성이 시장 인식보다 좋다고 주장했다. 2025 Cash App MAU 130m, Cash Card 55m을 예상했고, Boost 사용이 Card 지출의 20%, take rate 7%가 되면 2025 Boost 매출 $5.1bn, Cardlytics 8배 gross profit에 $40bn 가치라고 계산했다. Marqeta 계약 만료 후 조건 개선, POS rollout과 engagement로 base case 5년 IRR 17%+를 제시했다.

### 논지를 구성한 핵심 주장

#### 1. 숨은 TPV — 부분~적중

**핵심 주장:** Cash Card·Boost·Instant Transfer를 넣으면 Cash App monetization이 더 크다.

**이 주장이 성립하려면:** 분류조정 volume이 실제 gross profit으로 반복

**사전 반증조건:** 내부거래·혜택비용 때문에 과대계상

**실제 결과:** Cash App gross profit의 실질가치는 확인됐다.

#### 2. 130m MAU — 경로 미달

**핵심 주장:** 2025 Cash App MAU 130m, Card 55m이다.

**이 주장이 성립하려면:** 사용자성장과 card attach 지속

**사전 반증조건:** MAU 60m 전후에서 감속

**실제 결과:** 2023-12 monthly actives 56m, Card actives 23m이었다.

#### 3. Boost $5.1bn — 실패

**핵심 주장:** Card spend 20%×7% take로 Boost가 거대 광고사업이 된다.

**이 주장이 성립하려면:** merchant 수요·할인 economics·사용률 검증

**사전 반증조건:** 혜택비용·낮은 이용률로 수익 제한

**실제 결과:** 별도 $5.1bn 수익화 근거가 나타나지 않았다.

#### 4. 17% IRR — 치명적 실패

**핵심 주장:** 회계왜곡 교정과 성장만으로 높은 장기수익이다.

**이 주장이 성립하려면:** FCF margin과 주식수 방어

**사전 반증조건:** SBC·M&A·배수압축

**실제 결과:** 기준일까지 약 -73%였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | SQL은 Short지만 본문은 Long이다. 비트코인·transaction 비용을 제거하고 Cash App Card·Boost·Instant Transfer가 subscription revenue로 분류돼 TPV와 take rate 화면에서 빠지는 점을 조정하면 경제성이 시장 인식보다 좋다고 주장했다. 2025 Cash App MAU 130m, Cash Card 55m을 예상했고, Boost 사용이 Card 지출의 20%, take rate 7%가 되면 2025 Boost 매출 $5.1bn, Cardlytics 8배 gross profit에 $40bn 가치라고 계산했다. Marqeta 계약 만료 후 조건 개선, POS rollout과 engagement로 base case 5년 IRR 17%+를 제시했다. | 게시월 $243.80에서 2024-01 $65.01로 약 -73%였다. Cash App은 2023-12 56m monthly transacting actives와 23m Cash App Card monthly actives를 기록해 큰 사업이 됐지만 2025 130m·55m으로 가는 경로와 Boost $5.1bn 별도 매출은 기준일까지 보이지 않았다. Block은 성장보다 조직 단순화·12,000명 cap과 수익성 회복을 우선했고, Afterpay 인수·SBC·배수압축이 주당가치를 훼손했다. |
| 밸류에이션·청구권 | Boost만 $40bn; base 5년 IRR 17%+ | $243.80→$65.01; 약 -73.3% |
| 촉매·시간 | 2022 성장 둔화·Afterpay 희석·수익성 우선 전환 | 첫 확인 2022-02-24 |
| 사전 반증 | 내부거래·혜택비용 때문에 과대계상 | 회계분류를 뜯어 Cash App의 숨은 monetized volume을 찾은 과정은 훌륭했다. 그러나 추정 TPV 위에 20% Boost 사용률, 7% take rate, peer 8배를 연쇄 적용해 option을 확정가치처럼 만들었고, 사용자와 gross profit을 주당 FCF로 연결하지 못했다. |

### 실제 전개와 투자 결론

게시월 $243.80에서 2024-01 $65.01로 약 -73%였다. Cash App은 2023-12 56m monthly transacting actives와 23m Cash App Card monthly actives를 기록해 큰 사업이 됐지만 2025 130m·55m으로 가는 경로와 Boost $5.1bn 별도 매출은 기준일까지 보이지 않았다. Block은 성장보다 조직 단순화·12,000명 cap과 수익성 회복을 우선했고, Afterpay 인수·SBC·배수압축이 주당가치를 훼손했다.

**종합판정: 치명적 실패.** 회계분류를 뜯어 Cash App의 숨은 monetized volume을 찾은 과정은 훌륭했다. 그러나 추정 TPV 위에 20% Boost 사용률, 7% take rate, peer 8배를 연쇄 적용해 option을 확정가치처럼 만들었고, 사용자와 gross profit을 주당 FCF로 연결하지 못했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격 | $243.80 | 5년 IRR 17%+ | $65.01 | 치명적 실패 |
| Cash App MAU | 2025 130m 예상 | 고성장 | 56m monthly actives 2023-12 | 미달 경로 |
| Cash Card | 2025 55m | attach 확대 | 23m monthly actives 2023-12 | 미달 경로 |
| Boost | $5.1bn 2025 매출 | $40bn 가치 | 별도 실현 근거 부족 | 실패 |

재사용 질문: **내부거래·혜택비용 때문에 과대계상**

## 2024-01-31 기준 기업 결론

2016 저가 롱은 cohort economics와 TAM이 맞아 매우 성공했다. 2018 숏은 SBC·대출위험은 맞았지만 Cash App을 놓쳐 실패했고, 2019 롱은 사업은 맞아도 주가가 부진했다. 2021 두 롱은 revenue quality를 잘 조정하고도 20배 경제매출·고성장·고마진·희석을 동시에 낙관해 치명적으로 실패했다.

## 주요 근거

- [Block Q4 2023 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1512673/000119312524042835/d718674dex991.htm)
- [Block 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1512673/000162828024006354/sq-20231231.htm)
- [Afterpay acquisition closing 10-Q](https://www.sec.gov/Archives/edgar/data/1512673/000162828022012707/sq-20220331.htm)
- [Square 2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/1512673/000151267319000003/a10-kfilingsquareinc2018.htm)
- [Block historical prices](https://www.digrin.com/stocks/detail/SQ/price)
- [VIC Block 2018-07-02 원문](https://www.valueinvestorsclub.com/idea/SQUARE_INC/3039475682)
- [VIC Block 2019-06-19 원문](https://www.valueinvestorsclub.com/idea/SQUARE_INC/4028226961)
- [VIC Block 2021-06-05 원문](https://www.valueinvestorsclub.com/idea/SQUARE_INC/1694644233)


---

# 배치 공통 패턴과 DB 학습 태그

| 패턴 | 성공 메커니즘 | 실패를 부르는 오용 |
|---|---|---|
| network economics | 거래 증가의 낮은 증분비용이 EPS·FCF/주로 연결 | 모든 wallet·acquirer를 같은 네트워크 moat로 평가 |
| FCF yield + option | 현 사업 현금흐름이 가격을 지지하고 신사업은 무료 | 아직 없는 monetization을 SOTP에 확정가치로 합산 |
| revenue quality | 통과매출을 제거해 gross profit·net revenue를 비교 | 배수를 고쳐 놓고도 높은 성장 duration을 무비판 수용 |
| cohort economics | CAC·payback·retention으로 재투자수익률 검증 | 회사 전체 opex·SBC·credit loss를 cohort 밖으로 방치 |
| dilution/capital allocation | buyback이 주당가치를 높일 때만 의미 | SBC·인수발행을 무시하고 조정 EBITDA만 평가 |
| timing path | 촉매와 반증조건이 보유가능성을 만든다 | 최종 valuation 정상화만 맞고 중간 squeeze를 무시 |

핵심 학습 태그: `payments_network`, `merchant_acquiring`, `digital_wallet`, `cash_app`, `branded_checkout`, `transaction_margin_dollars`, `revenue_quality`, `cohort_payback`, `multiple_duration`, `stock_compensation`, `acquisition_dilution`, `timing_path`.

# 데이터 품질·방법론

- 평가기준일은 2024-01-31로 고정했다. 2월 공개된 FY2023 자료는 2023-12-31 사업상태 확인에만 사용했고 그 이후 주가정보는 판정에 넣지 않았다.
- 가격은 원문 가격 또는 게시월 실가격과 2024-01 월말 실가격 비교다. Mastercard·GPN의 과거 분할은 조정했고 배당은 제외했다.
- 종합판정은 사업성장, 원인, valuation, 촉매·보유경로, 주가를 분리했다. 장기 horizon 미도래인 PayPal 2022는 초기 실패·장기 미판정으로 표시했다.
- gross profit이나 조정 EBITDA 성장만으로 성공 처리하지 않고 SBC·인수 주식발행·주식수와 FCF/주 귀속을 확인했다.
