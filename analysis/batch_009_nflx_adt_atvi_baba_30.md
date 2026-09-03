# Batch 009 — Netflix·ADT·Activision Blizzard·Alibaba 30건

평가기준일: 각 글의 보유기간 및 2024-01-31까지의 증권·사업 결과  
분석일: 2026-09-03  
대상: NFLX 8건·ADT 8건·ATVI 8건·BABA 6건

## 결론부터

이번 배치는 같은 기업을 여러 시점의 Long·Short로 읽어 **사업을 맞힌 것, 가격을 맞힌 것, 인과를 맞힌 것**을 분리한다. SQL 30건은 모두 short flag가 켜져 있으나 실제로는 Long 19건, Short 10건, Long+Short 혼합 이벤트 1건이다.

| 기업 | 건수 | 가장 강한 성공 | 가장 큰 실패 | 핵심 학습 |
|---|---:|---|---|---|
| Netflix | 8 | 2012·2016 Long | 2003·2013 Short | 초기 margin·cash burn을 terminal economics로 고정하지 말 것 |
| ADT | 8 | 2022 odd-lot | 2018·2020 Long, 2015 Short | RMR에서 유지 SAC·부채를 빼고 M&A/tender tail을 분리 |
| Activision Blizzard | 8 | 2002·2019 Long, 2022 arb | 2019 Short·2021 고가 Long | portfolio IP와 governance, deal 확률을 별도 모델링 |
| Alibaba | 6 | 2022-10 전술 Long | 2021 Long | SOTP와 VIE 청구권·정책·실현확률을 분리 |

> 핵심 결론: 좋은 사업도 시작가격·자본구조·청구권·시간경로가 틀리면 실패한다. 반대로 가격은 맞아도 실제 수익을 만든 원인이 원 논지와 다르면 ‘인과 부분실패’로 기록해야 재사용 가능한 데이터가 된다.

---

# Netflix (NFLX) — 기업과 비즈니스

Netflix는 DVD 우편대여에서 출발해 전 세계 소비자에게 월 구독료를 받고 영화·시리즈·게임을 제공하는 스트리밍 엔터테인먼트 회사로 전환했다. 경제성의 출발점은 유료회원 수×월 ARPU이지만, 최종가치는 콘텐츠 현금지출·상각·마케팅·기술비를 뺀 현금흐름에서 나온다. 콘텐츠는 여러 회원에게 반복 제공되므로 규모가 커질수록 회원당 비용이 낮아지고, 더 큰 콘텐츠 예산이 가입·유지·가격인상을 도와 다시 규모를 키우는 flywheel이 가능하다. 반대로 작품 흥행은 불확실하고 제작현금은 비용인식보다 앞서 나가므로 GAAP 영업이익이나 EBITDA가 현금창출을 과장할 수 있다. 국가별 취향·규제·결제·현지 제작, 경쟁 서비스, 계정공유와 churn도 중요하다. 2010년대의 핵심 논쟁은 DVD 이익을 잃기 전에 스트리밍·해외 규모를 만들 수 있는가였고, 2022~23년에는 광고요금제와 유료 공유가 성숙기 성장·수익성을 다시 만들 수 있는가로 바뀌었다.

## 돈을 버는 구조

- 수익: 유료회원×ARPU; 2023년부터 광고요금제·유료공유가 추가 monetization 축
- moat: 글로벌 콘텐츠 규모·개인화 데이터·브랜드·거의 무마찰인 배포
- 현금함정: 콘텐츠 cash spend가 상각보다 먼저 발생해 회계이익과 FCF의 시차가 큼
- 핵심지표: 순증회원·churn·ARPU·engagement·콘텐츠 현금지출·영업마진

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 논지 | 실제 결과 | 판정 |
|---|---|---|---|---|---|
| 2003-04-28 | Short | Short | 회계·churn 과대평가 숏 | SQL 정밀 성과 미수록; 장기 주가는 수백 배 상승해 숏 손실이 사실상 무제한 | 치명적 실패 |
| 2007-04-19 | Short | Long | DVD moat·FCF 저평가 롱 | SQL 정밀 성과 미수록; $29 목표를 넘어 장기 다배 상승 | 매우 성공·인과 일부 오류 |
| 2010-09-08 | Short | Long | 글로벌 streaming operating leverage 롱 | SQL 정밀 성과 미수록; 2011 급락 후 장기 대폭 상승 | 장기 성공·경로 위험 |
| 2012-05-31 | Short | Long | 국내 streaming 전략가치 롱 | SQL 정밀 성과 미수록; $64 대비 장기 수십 배 상승 | 매우 성공 |
| 2013-01-28 | Short | Short | DVD 이익소멸·경쟁 숏 | SQL 정밀 성과 미수록; 장기 급등으로 숏 대손실 | 치명적 실패 |
| 2016-06-03 | Short | Short | 해외회원 컨센서스·cash burn 숏 | SQL 정밀 성과 미수록; 장기 주가 상승으로 숏 실패 | 실패 |
| 2016-06-27 | Short | Long | 미국가치로 해외 무료옵션 롱 | SQL 정밀 성과 미수록; 장기 다배 상승 | 매우 성공 |
| 2019-09-09 | Short | Long | 글로벌 SVOD flywheel 롱 | SQL 정밀 성과 미수록; 2021 급등→2022 폭락→2023 회복 | 부분 성공 |

## 1. 2003-04-28 — 회계·churn 과대평가 숏

### 원 투자논지

$500m 시가총액과 순현금 반영 EV 약 $615m, 2003년 매출가이던스 $255~275m의 2.3배가 적자 DVD 대여업체에 과하다고 봤다. DVD 상각을 빼는 lifetime EBITDA와 회사 churn 정의를 비판해 보고 LTV $102를 $38, churn 5.8%를 약 7.8%로 재계산했다. CAC $32, gross margin 50.3%→46.1%와 42~44% 가이던스, warrant·option 희석도 하방 논거였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $500m 시가총액과 순현금 반영 EV 약 $615m, 2003년 매출가이던스 $255~275m의 2.3배가 적자 DVD 대여업체에 과하다고 봤다. DVD 상각을 빼는 lifetime EBITDA와 회사 churn 정의를 비판해 보고 LTV $102를 $38, churn 5.8%를 약 7.8%로 재계산했다. CAC $32, gross margin 50.3%→46.1%와 42~44% 가이던스, warrant·option 희석도 하방 논거였다. | 회계조정과 churn 정의에 대한 문제제기는 타당했지만 Netflix는 회원규모·물류효율을 키운 뒤 스트리밍으로 경제구조 자체를 바꿨다. 2003년의 정적인 DVD cohort 가치로 이후 20년의 배포기술과 콘텐츠 규모를 포착하지 못했다. |
| 밸류에이션·청구권 | EV/매출 약 2.3x와 조정 고객가치 $74m | SQL 정밀 성과 미수록; 장기 주가는 수백 배 상승해 숏 손실이 사실상 무제한 |
| 촉매·시간 | margin 하락·희석·churn 재평가 | 회원과 매출이 계속 성장하며 예상한 고객가치 붕괴가 나타나지 않음 |
| 사전 반증조건 | LTV 계산이 맞더라도 규모·제품전환이 terminal value를 만들면 숏 손실을 어디서 제한하는가? | 핵심 오류: 현재 cohort의 LTV를 회사의 진화가능성 전체 가치로 대체 |

### 실제 전개와 투자 결론

회계조정과 churn 정의에 대한 문제제기는 타당했지만 Netflix는 회원규모·물류효율을 키운 뒤 스트리밍으로 경제구조 자체를 바꿨다. 2003년의 정적인 DVD cohort 가치로 이후 20년의 배포기술과 콘텐츠 규모를 포착하지 못했다.

**종합판정: 치명적 실패.** 숏은 당시 이익의 질을 정확히 지적했지만 사업모델이 바뀔 수 있는 장기 option과 규모효과를 0으로 놓았다. 싸 보이지 않는다는 사실만으로 파산·영구훼손의 경로가 생기지는 않았다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 기업가치 | EV ~$615m | 고객가치 수준으로 하락 | 장기 급증 | 실패 |
| LTV | 회사 $102/조정 $38 | 과대평가 확인 | 규모·전환으로 프레임 무효 | 부분 |
| churn | 보고 5.8%/추정 7.8% | 성장둔화 | 회원 증가 | 실패 |
| gross margin | 50.3%→46.1% | 42~44% | 단기 압박 후 모델전환 | 단기 적중 |

재사용 질문: **LTV 계산이 맞더라도 규모·제품전환이 terminal value를 만들면 숏 손실을 어디서 제한하는가?**

## 2. 2007-04-19 — DVD moat·FCF 저평가 롱

### 원 투자논지

$21.35, 시총 $1.51bn에서 2007 FCF $70~80m과 EV/FCF 16배 이하를 지불했다. 6.3m 회원, 샌프란시스코 가구침투율 15.7%, 낮아지는 churn·CAC를 근거로 2016년 13.2~13.9m 회원을 가정했다. Walmart·Amazon의 철수와 예상되는 Blockbuster 가격인상은 우편 DVD의 운영 moat를 확인하며, 스트리밍 성공 없이도 충성도 높은 DVD 기반과 $100m buyback으로 DCF $29가 가능하다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $21.35, 시총 $1.51bn에서 2007 FCF $70~80m과 EV/FCF 16배 이하를 지불했다. 6.3m 회원, 샌프란시스코 가구침투율 15.7%, 낮아지는 churn·CAC를 근거로 2016년 13.2~13.9m 회원을 가정했다. Walmart·Amazon의 철수와 예상되는 Blockbuster 가격인상은 우편 DVD의 운영 moat를 확인하며, 스트리밍 성공 없이도 충성도 높은 DVD 기반과 $100m buyback으로 DCF $29가 가능하다고 봤다. | 주식은 매우 성공했고 실제 회원은 추정치를 크게 넘었다. 그러나 가치의 주원인은 DVD가 20년 지속된 것이 아니라 DVD 이익과 브랜드를 이용해 스트리밍으로 빠르게 자기잠식한 데 있었다. 원 논지의 가격규율은 좋았지만 terminal business는 틀렸다. |
| 밸류에이션·청구권 | 2007 FCF $70~80m, EV/FCF ≤16x, DCF $29 | SQL 정밀 성과 미수록; $29 목표를 넘어 장기 다배 상승 |
| 촉매·시간 | Blockbuster 가격인상·buyback·churn 개선 | 스트리밍 이용이 빠르게 늘며 DVD-only terminal 가정의 중요성이 감소 |
| 사전 반증조건 | 스트리밍이 DVD를 잠식할 때 기존 FCF를 잃기 전에 새 모델의 economics가 양수가 되는가? | 핵심 오류: 현재 cash cow의 지속성과 미래 제품전환을 잘못 동일시 |

### 실제 전개와 투자 결론

주식은 매우 성공했고 실제 회원은 추정치를 크게 넘었다. 그러나 가치의 주원인은 DVD가 20년 지속된 것이 아니라 DVD 이익과 브랜드를 이용해 스트리밍으로 빠르게 자기잠식한 데 있었다. 원 논지의 가격규율은 좋았지만 terminal business는 틀렸다.

**종합판정: 매우 성공·인과 일부 오류.** 낮은 FCF 배수와 고객밀도는 하방을 만들었다. 다만 ‘스트리밍이 필요 없다’는 안전장치는 거꾸로였고, 실제 성공은 기존 논지에 없던 전환 option에서 왔다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입/목표 | $21.35/$29 | 약 36% | 목표 초과 | 적중 |
| 회원 | 6.3m | 2016 13.2~13.9m | 실제 크게 초과 | 적중 |
| FCF | $70~80m | 지속 성장 | 스트리밍 투자로 변동 후 확대 | 부분 |
| DVD 지속 | 20년 가정 | 논지에 streaming 불필요 | DVD 종료 | 실패 |

재사용 질문: **스트리밍이 DVD를 잠식할 때 기존 FCF를 잃기 전에 새 모델의 economics가 양수가 되는가?**

## 3. 2010-09-08 — 글로벌 streaming operating leverage 롱

### 원 투자논지

Netflix를 스트리밍 전환의 지배적 ‘말’로 보고 3년 EPS $10~15를 예상했다. 물리 DVD를 streaming으로 바꾸면 최대 $800m의 COGS가 절감되고, HBO와 비슷한 20~30% EBIT margin, subscriber 25%→40%+ 성장, SAC 25% 감소와 낮은 churn이 $800m~$1.5bn EBIT 증가를 만든다고 봤다. Epix 계약의 5~7년 약 $1bn 비용은 위험이지만 규모가 이를 흡수한다고 판단했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Netflix를 스트리밍 전환의 지배적 ‘말’로 보고 3년 EPS $10~15를 예상했다. 물리 DVD를 streaming으로 바꾸면 최대 $800m의 COGS가 절감되고, HBO와 비슷한 20~30% EBIT margin, subscriber 25%→40%+ 성장, SAC 25% 감소와 낮은 churn이 $800m~$1.5bn EBIT 증가를 만든다고 봤다. Epix 계약의 5~7년 약 $1bn 비용은 위험이지만 규모가 이를 흡수한다고 판단했다. | 스트리밍 지배력과 장기 operating leverage는 매우 정확했다. 다만 2011년 가격분리·Qwikster, 콘텐츠 재계약과 해외투자로 주가와 이익이 급락해 3년의 매끄러운 EPS 경로는 틀렸다. 장기 성공과 보유경로 성공을 구분해야 한다. |
| 밸류에이션·청구권 | 23x 수준의 당시 2012/13 컨센서스 EPS; 3년 EPS $10~15 | SQL 정밀 성과 미수록; 2011 급락 후 장기 대폭 상승 |
| 촉매·시간 | streaming 채택·물류비 절감·해외확장 | 가격분리와 Qwikster 발표 뒤 회원반발·가이던스 하향 |
| 사전 반증조건 | 회원가격을 올리고 DVD를 잠식해도 churn과 콘텐츠현금이 24개월 runway를 훼손하지 않는가? | 핵심 오류: 규모효과의 방향을 이익실현 속도와 혼동 |

### 실제 전개와 투자 결론

스트리밍 지배력과 장기 operating leverage는 매우 정확했다. 다만 2011년 가격분리·Qwikster, 콘텐츠 재계약과 해외투자로 주가와 이익이 급락해 3년의 매끄러운 EPS 경로는 틀렸다. 장기 성공과 보유경로 성공을 구분해야 한다.

**종합판정: 장기 성공·경로 위험.** 산업전환과 규모경제는 맞았지만 콘텐츠권리와 자기잠식 때문에 이익이 직선으로 늘지 않았다. 정확한 terminal thesis도 자금·고객반발·기간을 틀리면 큰 drawdown을 만든다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| subscriber 성장 | 25%→40%+ | 가속 | 장기 대폭 확대 | 적중 |
| SAC | 약 25% 하락 | 규모효율 | digital 전환으로 구조개선 | 적중 |
| EBIT margin | HBO 20~30% 유추 | 확대 | 장기 실현 | 장기 적중 |
| 3년 EPS | $10~15 | 빠른 상승 | Qwikster·투자로 경로 미달 | 실패 |

재사용 질문: **회원가격을 올리고 DVD를 잠식해도 churn과 콘텐츠현금이 24개월 runway를 훼손하지 않는가?**

## 4. 2012-05-31 — 국내 streaming 전략가치 롱

### 원 투자논지

$64, 순현금 반영 EV 약 $3.2bn에서 23m 국내 streaming 유료회원과 월 $8를 샀다. 단기 고정 콘텐츠비 때문에 가입자 증가의 증분 margin이 높고, 성숙 contribution margin 25~35%·EBIT 10~15%가 가능하다고 봤다. 2012/13 콘텐츠비 $1.4bn/$1.8bn을 감안해도 domestic streaming만 전략적 인수자에게 $4~6bn 가치가 있고 $64 이하면 Apple·Microsoft·Google·Amazon의 인수 가능성도 하방이라고 주장했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $64, 순현금 반영 EV 약 $3.2bn에서 23m 국내 streaming 유료회원과 월 $8를 샀다. 단기 고정 콘텐츠비 때문에 가입자 증가의 증분 margin이 높고, 성숙 contribution margin 25~35%·EBIT 10~15%가 가능하다고 봤다. 2012/13 콘텐츠비 $1.4bn/$1.8bn을 감안해도 domestic streaming만 전략적 인수자에게 $4~6bn 가치가 있고 $64 이하면 Apple·Microsoft·Google·Amazon의 인수 가능성도 하방이라고 주장했다. | 인수는 없었지만 국내·해외 streaming 규모, 자체콘텐츠와 가격인상이 기업가치를 폭발적으로 늘렸다. 콘텐츠가 단기 고정비처럼 작동한다는 통찰은 맞았고, strategic value보다 standalone 가치가 훨씬 커졌다. |
| 밸류에이션·청구권 | EV $3.2bn vs domestic strategic value $4~6bn | SQL 정밀 성과 미수록; $64 대비 장기 수십 배 상승 |
| 촉매·시간 | subscriber 성장·margin 확대·잠재 인수 | 국내 streaming contribution margin과 회원이 회복 |
| 사전 반증조건 | 인수자가 전혀 없어도 콘텐츠 현금지출 후 standalone FCF가 목표수익을 만드는가? | 핵심 오류: 인수가능성을 하방으로 부른 점은 약했지만 standalone floor가 충분 |

### 실제 전개와 투자 결론

인수는 없었지만 국내·해외 streaming 규모, 자체콘텐츠와 가격인상이 기업가치를 폭발적으로 늘렸다. 콘텐츠가 단기 고정비처럼 작동한다는 통찰은 맞았고, strategic value보다 standalone 가치가 훨씬 커졌다.

**종합판정: 매우 성공.** 가격이 충분히 낮았고 회원규모·콘텐츠 leverage라는 핵심 인과도 맞았다. M&A는 필요하지 않은 부가촉매였으며, 논지가 촉매 실패에도 살아남는 구조였다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입가 | $64 | 전략가치 이하 | 장기 대폭 상승 | 적중 |
| 국내 유료회원 | 23m | 규모 확대 | 대폭 확대 | 적중 |
| 성숙 EBIT margin | 10~15% | 실현 | 장기 그 이상 | 적중 |
| 인수 | Apple 등 가능 | 하방 | 미발생 | 불필요 |

재사용 질문: **인수자가 전혀 없어도 콘텐츠 현금지출 후 standalone FCF가 목표수익을 만드는가?**

## 5. 2013-01-28 — DVD 이익소멸·경쟁 숏

### 원 투자논지

실적 뒤 약 60% 급등을 short squeeze로 보고, 약 50% contribution margin의 DVD가 18.5%인 domestic streaming으로 대체될수록 이익이 나빠진다고 주장했다. 월 churn 3.8% 이상이면 gross adds 없이는 18개월 안에 절반이 이탈하고, Amazon Prime·Redbox·Comcast·HBO·Hulu 경쟁과 고정 콘텐츠 계약이 FCF를 압박한다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 실적 뒤 약 60% 급등을 short squeeze로 보고, 약 50% contribution margin의 DVD가 18.5%인 domestic streaming으로 대체될수록 이익이 나빠진다고 주장했다. 월 churn 3.8% 이상이면 gross adds 없이는 18개월 안에 절반이 이탈하고, Amazon Prime·Redbox·Comcast·HBO·Hulu 경쟁과 고정 콘텐츠 계약이 FCF를 압박한다고 봤다. | DVD 이익은 사라졌고 콘텐츠 cash burn도 실제였지만 Netflix는 original content·국제확장·개인화·가격인상으로 streaming margin과 회원을 동시에 키웠다. 경쟁서비스가 많다는 사실이 Netflix 수요의 제로섬 붕괴로 이어지지 않았다. |
| 밸류에이션·청구권 | 고마진 DVD→저마진 streaming mix shift | SQL 정밀 성과 미수록; 장기 급등으로 숏 대손실 |
| 촉매·시간 | short squeeze 종료·churn·경쟁 | 회원과 streaming contribution이 예상보다 빠르게 증가 |
| 사전 반증조건 | 경쟁이 늘어도 총 SVOD 시간과 해외 TAM이 더 빨리 커지면 숏의 손실상한은 무엇인가? | 핵심 오류: 초기 segment margin을 terminal margin으로 외삽 |

### 실제 전개와 투자 결론

DVD 이익은 사라졌고 콘텐츠 cash burn도 실제였지만 Netflix는 original content·국제확장·개인화·가격인상으로 streaming margin과 회원을 동시에 키웠다. 경쟁서비스가 많다는 사실이 Netflix 수요의 제로섬 붕괴로 이어지지 않았다.

**종합판정: 치명적 실패.** 낮은 초기 streaming margin을 성숙 economics로 고정하고, 콘텐츠투자가 차별화와 규모를 만드는 피드백을 비용으로만 봤다. short squeeze 이후라는 timing 논거도 장기 fundamental 숏의 안전장치가 아니었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| DVD contribution | 약 50% | 소멸 | 소멸 | 적중 |
| domestic streaming | 18.5% | 구조적 저마진 | 장기 큰 폭 개선 | 실패 |
| churn | ≥3.8%/월 | 회원기반 약화 | 순증 지속 | 실패 |
| 경쟁 | Amazon·HBO 등 | 가격/회원 압박 | 시장확대와 공존 | 실패 |

재사용 질문: **경쟁이 늘어도 총 SVOD 시간과 해외 TAM이 더 빨리 커지면 숏의 손실상한은 무엇인가?**

## 6. 2016-06-03 — 해외회원 컨센서스·cash burn 숏

### 원 투자논지

2019년 비미국 회원 79m·월 ARPU $8.50이라는 컨센서스가 영국·독일의 강한 스포츠 pay-TV와 현지경쟁을 무시한다고 봤다. 2016·17년 각각 약 $1bn cash burn, 2015 콘텐츠 cash spend $4.6bn 대 상각 $3.4bn, 장부상 $12.3bn+off-BS $6.6bn 의무를 강조했다. 컨센서스 EBITDA 배수는 2016~19년 84x/42x/25x/17x, upside $150(+14%) 대 downside $57(-43%)로 계산했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 2019년 비미국 회원 79m·월 ARPU $8.50이라는 컨센서스가 영국·독일의 강한 스포츠 pay-TV와 현지경쟁을 무시한다고 봤다. 2016·17년 각각 약 $1bn cash burn, 2015 콘텐츠 cash spend $4.6bn 대 상각 $3.4bn, 장부상 $12.3bn+off-BS $6.6bn 의무를 강조했다. 컨센서스 EBITDA 배수는 2016~19년 84x/42x/25x/17x, upside $150(+14%) 대 downside $57(-43%)로 계산했다. | cash spend와 상각의 간극, 고정 의무는 정확했다. 그러나 Netflix는 자본시장 접근을 유지하며 비미국 회원이 예상보다 훨씬 빠르게 늘었고 현지 콘텐츠가 스포츠 부재를 보완했다. 현금소모가 곧 프랜차이즈 약함이라는 결론이 틀렸다. |
| 밸류에이션·청구권 | downside $57/upside $150; 고배수와 off-BS 의무 | SQL 정밀 성과 미수록; 장기 주가 상승으로 숏 실패 |
| 촉매·시간 | 해외 성장 미달·cash burn 지속 | 국제회원 순증이 컨센서스를 상회하고 조달여건 유지 |
| 사전 반증조건 | 콘텐츠 1달러가 장기 글로벌 contribution profit을 얼마 만드는지 cohort로 검증했는가? | 핵심 오류: negative FCF를 가치파괴와 동일시 |

### 실제 전개와 투자 결론

cash spend와 상각의 간극, 고정 의무는 정확했다. 그러나 Netflix는 자본시장 접근을 유지하며 비미국 회원이 예상보다 훨씬 빠르게 늘었고 현지 콘텐츠가 스포츠 부재를 보완했다. 현금소모가 곧 프랜차이즈 약함이라는 결론이 틀렸다.

**종합판정: 실패.** 회계의 질 분석은 강했지만 현금이 높은 ROIC의 글로벌 콘텐츠 자산을 만드는지 검증하지 않고 burn 자체를 반증으로 썼다. 부채·의무는 조달창구가 닫힐 때의 촉매와 함께 봐야 했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 비미국 회원 | 2019E 79m | 미달 | 실제 강한 성장 | 실패 |
| 2016/17 FCF | 각 -$1bn 안팎 | 압박 | 단기 burn 지속 | 적중 |
| 콘텐츠 cash/상각 | $4.6bn/$3.4bn | 이익과 현금 괴리 | 실제 괴리 | 적중 |
| 목표 | $57 downside | 하락 | 장기 상승 | 실패 |

재사용 질문: **콘텐츠 1달러가 장기 글로벌 contribution profit을 얼마 만드는지 cohort로 검증했는가?**

## 7. 2016-06-27 — 미국가치로 해외 무료옵션 롱

### 원 투자논지

EV 약 $38bn이 미국 streaming만으로 설명된다고 봤다. 2017E 미국 55m 회원×월 $10=$6.6bn 매출에서 콘텐츠 $3bn, tech $650m, marketing $380m, G&A $300m과 DVD $200m을 합쳐 약 $2.5bn 미국 EBIT, 15배로 $38bn을 계산했다. 당시 약 40m 해외회원은 500m 가구 TAM, 낮은 배포비, 자체콘텐츠·데이터·규모 덕분에 무료 option이라고 주장했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | EV 약 $38bn이 미국 streaming만으로 설명된다고 봤다. 2017E 미국 55m 회원×월 $10=$6.6bn 매출에서 콘텐츠 $3bn, tech $650m, marketing $380m, G&A $300m과 DVD $200m을 합쳐 약 $2.5bn 미국 EBIT, 15배로 $38bn을 계산했다. 당시 약 40m 해외회원은 500m 가구 TAM, 낮은 배포비, 자체콘텐츠·데이터·규모 덕분에 무료 option이라고 주장했다. | 미국 pricing과 margin, 해외회원·이익이 모두 크게 성장해 핵심 인과가 맞았다. 콘텐츠 cash burn은 계속됐지만 규모가 장기 FCF로 전환됐고 ‘domestic value+international option’ 프레임이 유효했다. |
| 밸류에이션·청구권 | 미국 EBIT ~$2.5bn×15x=EV $38bn | SQL 정밀 성과 미수록; 장기 다배 상승 |
| 촉매·시간 | 가격인상 무이탈·해외회원·FCF narrative | 미국 가격인상 뒤 churn 통제·해외회원 가속 |
| 사전 반증조건 | 공통 콘텐츠비를 미국과 해외에 중복 배분하지 않고도 해외 option 가치가 남는가? | 핵심 오류: 국내가치 추정의 콘텐츠 배분과 해외현지비용 불확실성 |

### 실제 전개와 투자 결론

미국 pricing과 margin, 해외회원·이익이 모두 크게 성장해 핵심 인과가 맞았다. 콘텐츠 cash burn은 계속됐지만 규모가 장기 FCF로 전환됐고 ‘domestic value+international option’ 프레임이 유효했다.

**종합판정: 매우 성공.** 사업부별 valuation으로 무엇을 공짜로 받는지 명확히 했고, 해외배포의 한계비용·콘텐츠 재사용·데이터 효과를 연결했다. 가격인상 churn과 현금소모를 별도 반증조건으로 둔 것도 좋았다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 미국 회원 | 48m/2017E 55m | 성장 | 장기 증가 | 적중 |
| 미국 EBIT | 약 $2.5bn 추정 | 15x 가치 | margin 확대 | 적중 |
| 해외 회원 | 약 40m | 무료 option | 가치 대폭 실현 | 적중 |
| 배포비 | 낮음 | 규모효과 | 글로벌 scale | 적중 |

재사용 질문: **공통 콘텐츠비를 미국과 해외에 중복 배분하지 않고도 해외 option 가치가 남는가?**

## 8. 2019-09-09 — 글로벌 SVOD flywheel 롱

### 원 투자논지

Q2 회원실망 뒤 20%+ 하락을 2016년과 유사한 기회로 봤다. 150m+ 회원의 콘텐츠→가입→가격→더 큰 콘텐츠 flywheel, 창작인재·데이터·공통 제작비의 규모경제와 순부채 $8bn 미만을 강조했다. 5년 300m 회원(18% CAGR), 월 ARPU $11→$15(6% CAGR), 매출 $54bn+을 놓고 5년 선행매출 2.4배 미만이라고 계산했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Q2 회원실망 뒤 20%+ 하락을 2016년과 유사한 기회로 봤다. 150m+ 회원의 콘텐츠→가입→가격→더 큰 콘텐츠 flywheel, 창작인재·데이터·공통 제작비의 규모경제와 순부채 $8bn 미만을 강조했다. 5년 300m 회원(18% CAGR), 월 ARPU $11→$15(6% CAGR), 매출 $54bn+을 놓고 5년 선행매출 2.4배 미만이라고 계산했다. | 글로벌 프랜차이즈와 장기 수익성은 확인됐지만 2022년 순회원 감소와 금리·배수축소로 주가가 큰 폭 하락했다. 2023년 광고요금제·유료공유로 회복했으나 2024-01-31까지는 매끄러운 5년 복리와 300m 가정이 아직 완전히 증명되지 않았다. |
| 밸류에이션·청구권 | 5년 후 매출 $54bn+, 당시 기준 <2.4x forward sales | SQL 정밀 성과 미수록; 2021 급등→2022 폭락→2023 회복 |
| 촉매·시간 | 회원성장·ARPU·콘텐츠 규모 | 10여 년 만의 첫 순회원 감소와 가이던스 충격 |
| 사전 반증조건 | 순증이 2년 멈추고 배수가 절반이 돼도 ARPU·margin만으로 목표 IRR을 지키는가? | 핵심 오류: 사업의 질을 가격과 회원성장 직선성으로 과도하게 확장 |

### 실제 전개와 투자 결론

글로벌 프랜차이즈와 장기 수익성은 확인됐지만 2022년 순회원 감소와 금리·배수축소로 주가가 큰 폭 하락했다. 2023년 광고요금제·유료공유로 회복했으나 2024-01-31까지는 매끄러운 5년 복리와 300m 가정이 아직 완전히 증명되지 않았다.

**종합판정: 부분 성공.** business thesis는 강했지만 valuation과 path risk가 컸다. 2019년의 scale 논리는 맞아도 pandemic pull-forward, 계정공유, 경쟁, discount rate가 기대수익의 상당 부분을 지웠다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 회원 | 150m+ | 5년 300m | 2023말 260.3m | 부분 |
| ARPU | $11 | 5년 $15 | 가격인상·mix로 성장 | 부분 |
| 매출 | 5년 $54bn+ | 고성장 | 2023 $33.7bn | 진행중 |
| FCF | burn 단계 | 규모 후 전환 | 2023 ~$6.9bn | 적중 |

재사용 질문: **순증이 2년 멈추고 배수가 절반이 돼도 ARPU·margin만으로 목표 IRR을 지키는가?**

## 2024-01-31 기준 기업 결론

2023년 말 Netflix 유료회원은 약 260.3m, 2023년 매출은 약 $33.7bn, FCF는 약 $6.9bn이었다. 이는 스트리밍 규모와 가격결정력이 실제 프랜차이즈가 됐음을 보여주지만 2011년 Qwikster와 2022년 회원감소처럼 좋은 종착점도 매우 큰 중간 drawdown을 포함할 수 있다.

## 주요 근거

- [Netflix Annual Reports & Proxies](https://ir.netflix.net/financials/annual-reports-and-proxies/default.aspx) — 2002~2023년 회원·매출·콘텐츠·현금흐름의 장기 비교.
- [Netflix 2023 Annual Report](https://www.sec.gov/Archives/edgar/data/1065280/000106528024000030/nflx-20231231.htm) — 2023년 260.3m 회원, 매출·영업이익·FCF와 콘텐츠 의무.
- [Netflix Content Accounting Overview](https://ir.netflix.net/ir-overview/top-investor-questions/default.aspx) — 콘텐츠 자산의 현금지출·상각과 비GAAP FCF 해석.
- [Netflix SEC Filings](https://ir.netflix.net/financials/sec-filings/default.aspx) — Qwikster, 해외확장, 가격인상과 연도별 위험요인 검증.

---

# ADT (ADT) — 기업과 비즈니스

ADT는 주택·소상공인에 경보장비와 스마트홈 기기를 설치하고 24시간 모니터링·출동 연결 서비스를 제공한다. 매출의 대부분이 recurring monthly revenue(RMR)이므로 표면상 구독사업이지만 신규고객 한 명을 얻기 위해 장비·설치·딜러수수료를 먼저 지출하거나 자본화한다. 따라서 신규가입이 줄면 단기 FCF가 좋아 보이고, 가입을 늘리면 회계 EBITDA보다 현금이 나빠질 수 있다. 핵심은 ARPU와 gross revenue attrition, subscriber acquisition cost(SAC), 회수기간, 계약기간, 설치 cohort의 생애가치다. 매년 12~18%가 이탈하는 ‘새는 양동이’를 채워야 하므로 높은 EBITDA margin만으로 경제성을 판단하면 안 된다. 케이블·통신·DIY 기기·Google/Amazon 생태계가 경쟁하며, 장비판매·태양광처럼 낮은 마진 사업을 붙이면 RMR의 질이 희석된다. 2016년 Apollo 인수 후 재상장된 ADT는 높은 부채와 지배주주 overhang도 보통주 가치에 중요했다.

## 돈을 버는 구조

- 수익: 모니터링 RMR×고객 수 + 설치·장비; RMR은 높고 반복되지만 획득비가 선행
- 핵심 단위경제: ARPU·attrition·SAC·revenue payback·계약기간
- 회계함정: 자본화 SAC와 성장투자가 EBITDA·조정 FCF를 실제 주주현금보다 좋게 보이게 함
- 자본구조: Apollo 지분·부채·자사주/공개매각·전략투자 이벤트가 가격경로를 좌우

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 논지 | 실제 결과 | 판정 |
|---|---|---|---|---|---|
| 2012-10-05 | Short | Short | spin-off 고평가 숏 | SQL 성과 미수록; 2016년 $42 인수로 절대가격 숏 실패 | 부분 성공·가격 실패 |
| 2012-12-21 | Short | Long | RMR·buyback 레버리지 롱 | SQL 정밀 성과 미수록; $42 현금인수, $55 목표 미달 | 부분 성공 |
| 2013-06-10 | Short | Short | 실제 attrition·유지capex 숏 | SQL 정밀 성과 미수록; 사업악화 후 2016 $42 takeout | 논지 성공·가격 부분 |
| 2015-01-05 | Short | Short | 경쟁·SAC·레버리지 숏 | SQL 정밀 성과 미수록; $36→$42 현금인수로 실패 | 실패 |
| 2018-02-06 | Short | Long | broken IPO·attrition 개선 롱 | 1년 -37.80%, 2년 -40.88%, 5년 -19.76% | 실패 |
| 2020-08-19 | Short | Long | Google 전략제휴 rerating 롱 | 1년 -28.72%, 2년 -29.69% | 실패 |
| 2022-08-15 | Short | Short | 조정 FCF·Solar 품질 숏 | 1개월 -1.03%, 3개월 -12.16%, 6개월 -2.37% (숏 방향보정) | 부분 성공·단기 미실현 |
| 2022-09-15 | Short | Mixed/Event | 99주 odd-lot tender+수급 숏 | 99주 odd-lot은 $9 고정회수 성공; outright short는 별도 판정 | odd-lot 성공·숏 별도 |

## 1. 2012-10-05 — spin-off 고평가 숏

### 원 투자논지

Tyco에서 분리된 직후 약 $38.50의 ADT는 높은 recurring revenue와 브랜드를 감안해도 비싸다고 봤다. 분할 수급과 초기 sell-side의 낙관, 유지에 필요한 고객획득지출을 조정하면 표면 EBITDA보다 주주 FCF가 작다는 valuation 숏이었다. 명확한 단기 촉매가 없음을 스스로 인정했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Tyco에서 분리된 직후 약 $38.50의 ADT는 높은 recurring revenue와 브랜드를 감안해도 비싸다고 봤다. 분할 수급과 초기 sell-side의 낙관, 유지에 필요한 고객획득지출을 조정하면 표면 EBITDA보다 주주 FCF가 작다는 valuation 숏이었다. 명확한 단기 촉매가 없음을 스스로 인정했다. | 주가는 한동안 높은 수준을 유지했고 2016년 Apollo가 $42에 인수했다. 장기적으로는 높은 SAC·churn과 buyback 부채의 문제가 드러났지만, 좋은 사업을 촉매 없이 소폭 고평가됐다는 이유로 숏한 포지션의 수익은 제한적이었다. |
| 밸류에이션·청구권 | 분할 직후 valuation과 post-SAC FCF 괴리 | SQL 성과 미수록; 2016년 $42 인수로 절대가격 숏 실패 |
| 촉매·시간 | 촉매 없음 | 주가가 하락하지 않은 채 buyback·레버리지 정책 강화 |
| 사전 반증조건 | 24개월 안에 가치격차를 닫을 촉매가 없을 때 borrow와 takeout risk를 감수할 이유가 있는가? | 핵심 오류: 맞는 정상가치 분석을 실행가능한 숏으로 착각 |

### 실제 전개와 투자 결론

주가는 한동안 높은 수준을 유지했고 2016년 Apollo가 $42에 인수했다. 장기적으로는 높은 SAC·churn과 buyback 부채의 문제가 드러났지만, 좋은 사업을 촉매 없이 소폭 고평가됐다는 이유로 숏한 포지션의 수익은 제한적이었다.

**종합판정: 부분 성공·가격 실패.** 경제성 비판은 맞았지만 $38.50에서 $42 현금회수라는 결과와 borrow/time cost를 이기지 못했다. short에는 valuation gap뿐 아니라 gap이 닫히는 사건이 필요하다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $38.50 | 하락 | 2016 $42 cash | 실패 |
| recurring mix | 높음 | 질은 인정 | 유지 | 적중 |
| post-SAC FCF | EBITDA보다 낮음 | 재평가 | 구조적 문제 확인 | 적중 |
| 촉매 | 없음 | valuation 정상화 | takeout이 반대촉매 | 실패 |

재사용 질문: **24개월 안에 가치격차를 닫을 촉매가 없을 때 borrow와 takeout risk를 감수할 이유가 있는가?**

## 2. 2012-12-21 — RMR·buyback 레버리지 롱

### 원 투자논지

6.5m alarm 계정, 매출의 90%가 recurring이고 EBITDA margin 약 50%인 시장 1위 사업을 샀다. 연 attrition 10~15%여도 신규계정 IRR 15~20%, pricing power와 $250m RMR에 55~60배를 적용한 EV $14~16bn/$52~58을 제시했다. 약 2x leverage와 $2bn buyback으로 연 $0.9~1bn의 현금을 주주에게 돌려 1년 $55를 기대했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 6.5m alarm 계정, 매출의 90%가 recurring이고 EBITDA margin 약 50%인 시장 1위 사업을 샀다. 연 attrition 10~15%여도 신규계정 IRR 15~20%, pricing power와 $250m RMR에 55~60배를 적용한 EV $14~16bn/$52~58을 제시했다. 약 2x leverage와 $2bn buyback으로 연 $0.9~1bn의 현금을 주주에게 돌려 1년 $55를 기대했다. | Apollo는 2016년 주당 $42에 인수했다. RMR의 전략가치는 확인됐지만 $55 목표는 미달했고 고가 buyback·부채는 주당가치를 기대만큼 만들지 못했다. 시작가격에 따라 modest return은 가능했으나 thesis의 핵심 upside는 불완전했다. |
| 밸류에이션·청구권 | RMR $250m×55~60x; $52~58 | SQL 정밀 성과 미수록; $42 현금인수, $55 목표 미달 |
| 촉매·시간 | $2bn buyback·pricing·takeout | 대규모 buyback에도 주당 실적·주가가 목표경로를 못 따라감 |
| 사전 반증조건 | 신규고객 획득비 전액을 유지 capex로 차감한 뒤에도 buyback 수익률이 자본비용을 넘는가? | 핵심 오류: RMR 배수에서 고객유지 capex와 부채를 충분히 차감하지 않음 |

### 실제 전개와 투자 결론

Apollo는 2016년 주당 $42에 인수했다. RMR의 전략가치는 확인됐지만 $55 목표는 미달했고 고가 buyback·부채는 주당가치를 기대만큼 만들지 못했다. 시작가격에 따라 modest return은 가능했으나 thesis의 핵심 upside는 불완전했다.

**종합판정: 부분 성공.** RMR franchise와 takeout value는 맞았지만 고객대체 SAC와 buyback 가격을 과소평가했다. 레버리지 buyback은 주식이 내재가치보다 충분히 쌀 때만 복리적이다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 계정 | 6.5m | 안정/성장 | 규모 유지 | 부분 |
| 매출 recurring | ~90% | 높은 가치 | 유지 | 적중 |
| 목표 | $55 | 1년 | 2016 $42 | 실패 |
| buyback | $2bn | 주당가치 확대 | 고가매입·부채 | 부분 |

재사용 질문: **신규고객 획득비 전액을 유지 capex로 차감한 뒤에도 buyback 수익률이 자본비용을 넘는가?**

## 3. 2013-06-10 — 실제 attrition·유지capex 숏

### 원 투자논지

케이블 사업자의 번들 진입으로 점유율·가격·ROIC가 압박받는다고 봤다. 회사가 말한 attrition 13.1%와 달리 감가상각으로 역산한 unit attrition은 약 17%이며 1%p마다 약 $30m recurring revenue를 새로 채워야 한다고 계산했다. 5% recurring revenue 감소 시 steady-state FCF가 음수가 될 수 있다는 ‘leaky bucket’ 숏이었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 케이블 사업자의 번들 진입으로 점유율·가격·ROIC가 압박받는다고 봤다. 회사가 말한 attrition 13.1%와 달리 감가상각으로 역산한 unit attrition은 약 17%이며 1%p마다 약 $30m recurring revenue를 새로 채워야 한다고 계산했다. 5% recurring revenue 감소 시 steady-state FCF가 음수가 될 수 있다는 ‘leaky bucket’ 숏이었다. | 고객획득·유지비와 churn 문제는 이후 공시와 낮은 주주수익에서 확인됐다. 다만 2016년 Apollo의 $42 인수 프리미엄이 숏의 회수경로를 방해했다. 사업논지는 성공했지만 정확한 진입가·청산시점 없이는 가격성과가 제한된다. |
| 밸류에이션·청구권 | unit attrition 17%, 5% 매출감소 시 FCF 음수 | SQL 정밀 성과 미수록; 사업악화 후 2016 $42 takeout |
| 촉매·시간 | 케이블 경쟁·margin/ROIC 하락 | 가입자 대체비와 buyback 부채가 누적 |
| 사전 반증조건 | 사업악화가 맞아도 sponsor가 RMR에 높은 배수를 지급할 때 숏 손실상한은? | 핵심 오류: takeout과 자본구조가 논지 실현가격을 바꿀 가능성 |

### 실제 전개와 투자 결론

고객획득·유지비와 churn 문제는 이후 공시와 낮은 주주수익에서 확인됐다. 다만 2016년 Apollo의 $42 인수 프리미엄이 숏의 회수경로를 방해했다. 사업논지는 성공했지만 정확한 진입가·청산시점 없이는 가격성과가 제한된다.

**종합판정: 논지 성공·가격 부분.** 표면 recurring margin을 subscriber replacement economics로 다시 계산한 것이 강했다. 그러나 전략적 인수자가 레버리지로 RMR을 사는 tail risk를 반영해야 했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 공시 attrition | 13.1% | 과소표시 | 후속 높은 churn 논쟁 | 적중 |
| 추정 unit attrition | ~17% | 유지비 증가 | SAC 핵심화 | 적중 |
| 1%p attrition | RMR ~$30m 대체 | FCF 압박 | 구조 확인 | 적중 |
| 주가결과 | 하락 기대 | 사업과 동행 | $42 takeout | 부분 |

재사용 질문: **사업악화가 맞아도 sponsor가 RMR에 높은 배수를 지급할 때 숏 손실상한은?**

## 4. 2015-01-05 — 경쟁·SAC·레버리지 숏

### 원 투자논지

약 $36에서 케이블·통신사는 기존 고객관계 덕분에 SAC가 낮고, ADT의 home automation 설치는 churn 개선을 감안해도 NPV가 낮다고 봤다. 실제 churn을 18~20%로 추정하고 flat revenue 유지에도 큰 capex가 필요하며 Corvex 주도 buyback 뒤 leverage 약 3x와 과거 중반 $40대 자사주 매입을 비판했다. 목표 $25~28, M&A 가능성은 낮다고 판단했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 약 $36에서 케이블·통신사는 기존 고객관계 덕분에 SAC가 낮고, ADT의 home automation 설치는 churn 개선을 감안해도 NPV가 낮다고 봤다. 실제 churn을 18~20%로 추정하고 flat revenue 유지에도 큰 capex가 필요하며 Corvex 주도 buyback 뒤 leverage 약 3x와 과거 중반 $40대 자사주 매입을 비판했다. 목표 $25~28, M&A 가능성은 낮다고 판단했다. | SAC·churn·고가 buyback 진단은 상당히 정확했지만 ‘M&A가 어렵다’는 결정적 가정이 틀렸다. Apollo가 2016년 $42에 인수해 $36 숏은 가격상 실패했다. |
| 밸류에이션·청구권 | 목표 $25~28; leverage ~3x | SQL 정밀 성과 미수록; $36→$42 현금인수로 실패 |
| 촉매·시간 | 경쟁·churn·buyback 한계 | Apollo $42 인수 발표로 논지와 반대의 가격촉매 발생 |
| 사전 반증조건 | 사업이 나빠도 PE buyer가 레버리지 가능한 RMR을 사면 포지션을 어떻게 hedge하는가? | 핵심 오류: M&A 가능성을 과도하게 낮춤 |

### 실제 전개와 투자 결론

SAC·churn·고가 buyback 진단은 상당히 정확했지만 ‘M&A가 어렵다’는 결정적 가정이 틀렸다. Apollo가 2016년 $42에 인수해 $36 숏은 가격상 실패했다.

**종합판정: 실패.** 운영분석은 맞았어도 event tail 하나가 수익을 뒤집었다. 안정적 RMR은 sponsor가 높은 leverage로 인수할 수 있어, standalone DCF만으로 takeout risk를 지울 수 없다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입/목표 | ~$36/$25~28 | 22~31% 하락 | $42 cash | 실패 |
| 실제 churn | 18~20% 추정 | 높은 유지비 | 핵심 위험 지속 | 적중 |
| leverage | ~3x | 제약 | sponsor가 더 활용 | 방향오류 |
| M&A | unlikely | 미발생 | Apollo 인수 | 실패 |

재사용 질문: **사업이 나빠도 PE buyer가 레버리지 가능한 RMR을 사면 포지션을 어떻게 hedge하는가?**

## 5. 2018-02-06 — broken IPO·attrition 개선 롱

### 원 투자논지

초기 range $17~19에서 $14로 가격을 낮춘 뒤 약 $12에 거래된 재상장 ADT를 broken IPO로 봤다. 90%+ recurring, 2위의 약 5배 규모, 54% 브랜드인지도와 Tim Whall의 운영개선을 근거로 attrition이 16~17%에서 13~14%로 낮아지고 upfront customer payment가 SAC와 tenure를 개선한다고 주장했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 초기 range $17~19에서 $14로 가격을 낮춘 뒤 약 $12에 거래된 재상장 ADT를 broken IPO로 봤다. 90%+ recurring, 2위의 약 5배 규모, 54% 브랜드인지도와 Tim Whall의 운영개선을 근거로 attrition이 16~17%에서 13~14%로 낮아지고 upfront customer payment가 SAC와 tenure를 개선한다고 주장했다. | 가격성과는 1년 -37.80%, 2년 -40.88%, 5년 -19.76%였다. attrition 개선 일부보다 높은 부채·Apollo overhang·고객획득비와 성장부재가 컸고, recurring revenue가 보통주 복리로 전달되지 않았다. |
| 밸류에이션·청구권 | IPO $14→약 $12; 낮아진 headline valuation | 1년 -37.80%, 2년 -40.88%, 5년 -19.76% |
| 촉매·시간 | attrition 13~14%·upfront deposit·운영개선 | 6개월 -27.63%와 leverage/성장 우려 지속 |
| 사전 반증조건 | SAC를 전액 비용처리하고 debt를 시장가치로 놓아도 equity yield가 충분한가? | 핵심 오류: recurring revenue의 안정성을 levered equity 안정성으로 오해 |

### 실제 전개와 투자 결론

가격성과는 1년 -37.80%, 2년 -40.88%, 5년 -19.76%였다. attrition 개선 일부보다 높은 부채·Apollo overhang·고객획득비와 성장부재가 컸고, recurring revenue가 보통주 복리로 전달되지 않았다.

**종합판정: 실패.** IPO 할인만 봤고 sponsor가 높은 가격에 다시 판 equity의 자본구조를 충분히 stress하지 않았다. churn 몇 %p 개선보다 debt·SAC 후 equity FCF가 먼저다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가격성과 | $12 부근 | IPO range 회복 | 1y -37.80% | 실패 |
| attrition | 16~17%→13~14% | 개선 | 일부 개선 | 부분 |
| recurring | >90% | 하방 | 주가 방어 실패 | 실패 |
| 5년 수익 | 상승 기대 | rerating | -19.76% | 실패 |

재사용 질문: **SAC를 전액 비용처리하고 debt를 시장가치로 놓아도 equity yield가 충분한가?**

## 6. 2020-08-19 — Google 전략제휴 rerating 롱

### 원 투자논지

시장 1위가 약 10x cash earnings/8x EBITDA에 거래되고 short interest가 18%인 상황에서 목표 $22, 거의 두 배를 제시했다. Google이 $450m로 6.6~7% 지분을 사고 양사가 각각 $150m을 마케팅·개발에 쓰는 계약이 Nest와 ADT 모니터링을 결합해 신규고객 ARPU를 10~20% 높일 game changer라고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 시장 1위가 약 10x cash earnings/8x EBITDA에 거래되고 short interest가 18%인 상황에서 목표 $22, 거의 두 배를 제시했다. Google이 $450m로 6.6~7% 지분을 사고 양사가 각각 $150m을 마케팅·개발에 쓰는 계약이 Nest와 ADT 모니터링을 결합해 신규고객 ARPU를 10~20% 높일 game changer라고 봤다. | Google 제휴는 제품·브랜드를 강화했지만 부채·SAC·낮은 유기성장과 Apollo overhang을 없애지 못했다. 가격성과는 1년 -28.72%, 2년 -29.69%였다. |
| 밸류에이션·청구권 | 8x EBITDA·10x cash earnings, 목표 $22 | 1년 -28.72%, 2년 -29.69% |
| 촉매·시간 | Google/Nest 출시·short squeeze | 1년 -28.72%, 제휴가 성장률을 바꾸지 못함 |
| 사전 반증조건 | Google 고객의 20% 높은 ARPU가 공동마케팅·장비보조 후 높은 incremental ROIC인가? | 핵심 오류: partner validation을 주당 FCF 촉매로 오해 |

### 실제 전개와 투자 결론

Google 제휴는 제품·브랜드를 강화했지만 부채·SAC·낮은 유기성장과 Apollo overhang을 없애지 못했다. 가격성과는 1년 -28.72%, 2년 -29.69%였다.

**종합판정: 실패.** 전략파트너의 투자금과 제품검증을 경제성 검증으로 확대했다. ARPU가 올라가도 CAC·보조금·churn·revenue share를 뺀 증분 LTV가 개선돼야 한다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Google 투자 | $450m/~7% | 검증·성장 | 제휴 지속/주가 미반영 | 부분 |
| 공동투자 | 각 $150m | 고객획득 | 비용도 증가 | 부분 |
| 목표 | $22 | 거의 2배 | 1y -28.72% | 실패 |
| 2년 수익 | 상승 | rerating | -29.69% | 실패 |

재사용 질문: **Google 고객의 20% 높은 ARPU가 공동마케팅·장비보조 후 높은 incremental ROIC인가?**

## 7. 2022-08-15 — 조정 FCF·Solar 품질 숏

### 원 투자논지

Google/Amazon이 ADT를 즉시 붕괴시킨다는 기존 bear case보다 경영진의 조정수치와 Apollo 67% 지분을 문제 삼았다. 고객 SAC 약 $1,500, 월 EBITDA $25~30, churn 약 13%의 회수구조에서 LTM ‘adjusted FCF’ $380m과 전통적 CFO-capex-capitalized SAC 약 $104m의 큰 간극을 지적했다. Solar는 RMR의 9%지만 EBITDA의 4~5%, margin 10% 미만이라 2025 목표의 질이 낮다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Google/Amazon이 ADT를 즉시 붕괴시킨다는 기존 bear case보다 경영진의 조정수치와 Apollo 67% 지분을 문제 삼았다. 고객 SAC 약 $1,500, 월 EBITDA $25~30, churn 약 13%의 회수구조에서 LTM ‘adjusted FCF’ $380m과 전통적 CFO-capex-capitalized SAC 약 $104m의 큰 간극을 지적했다. Solar는 RMR의 9%지만 EBITDA의 4~5%, margin 10% 미만이라 2025 목표의 질이 낮다고 봤다. | 6개월 방향보정 성과는 -2.37%로 거의 flat했다. State Farm의 $1.2bn 전략투자와 $9 tender가 단기 상승촉매가 됐지만 Solar impairment와 낮은 현금질은 후속 공시로 확인됐다. |
| 밸류에이션·청구권 | adjusted FCF $380m vs 전통 FCF ~$104m | 1개월 -1.03%, 3개월 -12.16%, 6개월 -2.37% (숏 방향보정) |
| 촉매·시간 | 가이던스 미달·Solar margin·Apollo 매도 | State Farm 투자·$9 tender 발표로 반대 방향 이벤트 |
| 사전 반증조건 | 유동성 공급자와 tender가 있어도 언제 FCF 괴리가 debt/guide에 나타나는가? | 핵심 오류: 회계품질 약화를 단기 가격촉매로 간주 |

### 실제 전개와 투자 결론

6개월 방향보정 성과는 -2.37%로 거의 flat했다. State Farm의 $1.2bn 전략투자와 $9 tender가 단기 상승촉매가 됐지만 Solar impairment와 낮은 현금질은 후속 공시로 확인됐다.

**종합판정: 부분 성공·단기 미실현.** 회계·segment 질 진단은 좋았지만 촉매와 sponsor/전략투자 수급을 이기지 못했다. 숏은 ‘나쁜 조정 FCF’가 언제 가격으로 드러나는지까지 필요하다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| SAC | ~$1,500 | 회수부담 | 핵심 부담 지속 | 적중 |
| churn | ~13% | 유지비 지속 | 2023 12.9% | 적중 |
| FCF | $380m 조정/$104m 전통 | 질 저하 | Solar 손상·현금질 논쟁 | 적중 |
| 6개월 숏 | 하락 기대 | 수익 | -2.37% | 미실현 |

재사용 질문: **유동성 공급자와 tender가 있어도 언제 FCF 괴리가 debt/guide에 나타나는가?**

## 8. 2022-09-15 — 99주 odd-lot tender+수급 숏

### 원 투자논지

고정가 $9 tender에서 99주 이하 odd-lot은 proration 없이 전량 수용되는 조건을 이용해 99주를 매수하는 소액 event trade를 제시했다. 동시에 Apollo 67%, 경영진 약 5%와 State Farm에 발행할 133.333m주를 고려하면 일반주주의 tender 물량 상당수가 되돌아와 $9 부근의 outright short도 가능하다고 봤다. 즉 동일 글에 확정형 odd-lot Long과 tender 후 수급 Short가 공존한다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 고정가 $9 tender에서 99주 이하 odd-lot은 proration 없이 전량 수용되는 조건을 이용해 99주를 매수하는 소액 event trade를 제시했다. 동시에 Apollo 67%, 경영진 약 5%와 State Farm에 발행할 133.333m주를 고려하면 일반주주의 tender 물량 상당수가 되돌아와 $9 부근의 outright short도 가능하다고 봤다. 즉 동일 글에 확정형 odd-lot Long과 tender 후 수급 Short가 공존한다. | State Farm은 주당 $9에 133.333m주, 총 $1.2bn을 투자했고 tender가 진행됐다. 조건을 지킨 99주 odd-lot은 $9 현금회수로 성공했지만 그 이상 주식의 proration과 후속 숏은 별개 포지션이며 하나의 방향수익률로 합치면 안 된다. |
| 밸류에이션·청구권 | $9 fixed tender와 odd-lot 비례배정 면제 | 99주 odd-lot은 $9 고정회수 성공; outright short는 별도 판정 |
| 촉매·시간 | State Farm closing·tender 완료·returned shares | State Farm 거래와 tender 완료 |
| 사전 반증조건 | 99주 자격·수수료를 제외한 확정 IRR과 일반 tender/숏 exposure를 완전히 분리했는가? | 핵심 오류: 서로 반대인 두 tranche를 단일 Long/Short로 저장하면 성과 왜곡 |

### 실제 전개와 투자 결론

State Farm은 주당 $9에 133.333m주, 총 $1.2bn을 투자했고 tender가 진행됐다. 조건을 지킨 99주 odd-lot은 $9 현금회수로 성공했지만 그 이상 주식의 proration과 후속 숏은 별개 포지션이며 하나의 방향수익률로 합치면 안 된다.

**종합판정: odd-lot 성공·숏 별도.** 기업가치보다 계약문구와 계좌별 odd-lot 자격을 읽은 event 아이디어다. 성공은 99주 tranche에 한정되며 세금·수수료·beneficial holder 판정과 tender 종료 전 가격을 확인해야 한다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| State Farm | 133.333m주×$9 | closing | $1.2bn 완료 | 적중 |
| odd-lot | ≤99주 | 무비례배정 | $9 회수 | 성공 |
| 일반 tender | 초과청약 예상 | 주식반환 | proration | 별도 |
| 방향 | Long+Short | tranche 분리 | 혼합 이벤트 | 교정 |

재사용 질문: **99주 자격·수수료를 제외한 확정 IRR과 일반 tender/숏 exposure를 완전히 분리했는가?**

## 2024-01-31 기준 기업 결론

2023년 3분기 ADT의 end-of-period RMR은 약 $350m, gross revenue attrition은 12.9%, revenue payback은 2.0년이었다. 핵심 보안사업은 남았지만 Solar goodwill 손상과 높은 자본비용은 ‘90% recurring=asset-light’가 아님을 확인했다.

## 주요 근거

- [The ADT Corporation merger proxy](https://www.sec.gov/Archives/edgar/data/1546640/000119312516517524/d141890ddefm14a.htm) — Apollo의 주당 $42 인수조건과 당시 standalone 가치.
- [ADT 2018 IPO prospectus](https://www.sec.gov/Archives/edgar/data/1703056/000119312518016233/d517732d424b4.htm) — Apollo 인수·통합, subscriber·RMR·attrition·부채 구조.
- [ADT 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1703056/000170305623000046/adt-20221231.htm) — State Farm $1.2bn 투자, $9 tender와 Solar·Google 관계.
- [ADT Third Quarter 2023 Results](https://investor.adt.com/News--Events/news/news-details/2023/ADT-Reports-Third-Quarter-2023-Results/default.aspx) — RMR $350m, attrition 12.9%, payback 2.0년과 Solar impairment.

---

# Activision Blizzard (ATVI) — 기업과 비즈니스

Activision Blizzard는 Call of Duty 중심의 Activision, World of Warcraft·Diablo·Overwatch의 Blizzard, Candy Crush의 King을 보유했던 게임 개발·퍼블리싱 회사다. 콘솔·PC의 패키지/디지털 판매, WoW 구독, 확장팩·다운로드 콘텐츠, 게임 내 결제, 모바일 광고가 수익원이다. 프랜차이즈가 성공하면 이미 만든 콘텐츠·플랫폼에 고마진 디지털 매출이 반복되지만, 출시 지연·품질·플레이어 이탈·인재문화·플랫폼 수수료 위험이 크다. MAU만 늘어도 payer conversion과 bookings가 약하면 가치가 늘지 않으며, 히트작 사이의 이익 변동과 deferred revenue도 봐야 한다. 2016년 King 인수로 모바일과 광고를 더했고, 2021년 직장문화·지배구조 위기는 제품 일정과 인력유출로 전이됐다. 2022년 Microsoft의 주당 $95 현금 인수계약 뒤에는 standalone 게임주가 아니라 종결확률·기간·break price를 분석하는 merger arbitrage가 됐다.

## 돈을 버는 구조

- 수익: premium game·구독·DLC/MTX·모바일 IAP·광고의 혼합
- moat: 대형 IP·개발인력·커뮤니티·배포/마케팅 규모, 단 히트 의존과 문화위험 존재
- 핵심지표: bookings·MAU·payer conversion·engagement·출시일정·digital mix
- 이벤트 분석: $95 계약 뒤에는 antitrust 종결확률×시간과 standalone break value가 핵심

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 논지 | 실제 결과 | 판정 |
|---|---|---|---|---|---|
| 2002-12-18 | Short | Long | 순현금·정상화 이익 롱 | SQL 정밀 성과 미수록; $20 목표 초과·장기 대폭 상승 | 매우 성공 |
| 2010-02-09 | Short | Long | franchise·digital margin 롱 | SQL 정밀 성과 미수록; 목표 $16 달성 후 장기 상승 | 성공 |
| 2011-11-14 | Short | Short | WoW 이익집중·성숙 숏 | SQL 정밀 성과 미수록; 장기 상승으로 숏 실패 | 실패 |
| 2019-03-26 | Short | Short | 노후 IP·battle royale 경쟁 숏 | SQL 정밀 성과 미수록; 최종 $95 현금인수 | 치명적 실패 |
| 2019-05-01 | Short | Long | bad-news 과잉반응·IP 롱 | SQL 정밀 성과 미수록; $62 목표 초과·최종 $95 | 성공 |
| 2021-02-06 | Short | Long | digital monetization·margin 복리 롱 | 진입 $101.61→최종 $95 cash; 약 -6.5% 전 시간비용 | 실패 |
| 2021-09-23 | Short | Long | 스캔들 과잉반응·pipeline 롱 | 약 $75→$95 cash로 성공 | 가격 성공·인과 일부 오류 |
| 2022-03-23 | Short | Long | Microsoft merger arbitrage 롱 | 주당 $95 현금회수; 예상보다 약 3개월 지연 | 매우 성공 |

## 1. 2002-12-18 — 순현금·정상화 이익 롱

### 원 투자논지

가이던스가 FY03 EPS $1.30에서 $0.88로 낮아져 주가가 $12.50가 된 때 TTM EPS $1.27과 주당 현금 약 $9, 무차입을 샀다. excess working capital 약 $400m($5.80/주)을 빼면 ex-cash P/E 약 8x, EV/EBITDA 1.8x, EV/NI 4x였다. 정상 EPS $1, 5년 10% 성장의 DCF $20을 제시했고 가장 큰 위험은 싼 현금으로 하는 나쁜 인수라고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 가이던스가 FY03 EPS $1.30에서 $0.88로 낮아져 주가가 $12.50가 된 때 TTM EPS $1.27과 주당 현금 약 $9, 무차입을 샀다. excess working capital 약 $400m($5.80/주)을 빼면 ex-cash P/E 약 8x, EV/EBITDA 1.8x, EV/NI 4x였다. 정상 EPS $1, 5년 10% 성장의 DCF $20을 제시했고 가장 큰 위험은 싼 현금으로 하는 나쁜 인수라고 봤다. | 회사는 대형 프랜차이즈와 디지털 전환으로 장기간 성장했고 주가는 목표를 크게 넘었다. 강한 순현금과 낮은 ex-cash valuation이 출시실망을 버틸 시간을 제공했다. |
| 밸류에이션·청구권 | 주당 현금 ~$9, EV/EBITDA 1.8x, DCF $20 | SQL 정밀 성과 미수록; $20 목표 초과·장기 대폭 상승 |
| 촉매·시간 | 이익정상화·buyback/takeout | 신작과 franchise 매출로 EPS 회복 |
| 사전 반증조건 | 현금의 50%를 가치파괴 M&A에 써도 ex-cash downside가 제한되는가? | 핵심 오류: 현금가치를 나쁜 M&A 전에 전액 인정할 위험 |

### 실제 전개와 투자 결론

회사는 대형 프랜차이즈와 디지털 전환으로 장기간 성장했고 주가는 목표를 크게 넘었다. 강한 순현금과 낮은 ex-cash valuation이 출시실망을 버틸 시간을 제공했다.

**종합판정: 매우 성공.** cycle 저점의 실적을 정상화하되 현금을 실제 하방과 재투자 옵션으로 봤다. 인수위험도 정확했지만 이후 Blizzard·King 결합은 장기적으로 franchise를 넓혔다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입/목표 | $12.50/$20 | 60% | 초과 | 적중 |
| 현금 | ~$9/주 | 하방 | 무차입 유지·전략옵션 | 적중 |
| 정상 EPS | $1 | 10% 성장 | 장기 성장 | 적중 |
| EV/EBITDA | 1.8x | rerating | rerating | 적중 |

재사용 질문: **현금의 50%를 가치파괴 M&A에 써도 ex-cash downside가 제한되는가?**

## 2. 2010-02-09 — franchise·digital margin 롱

### 원 투자논지

업계 부진과 Q4 실적 전 불안을 가격에 반영한 ATVI를 샀다. World of Warcraft는 약 45% operating margin으로 회사이익의 거의 절반, 매출 80%+가 검증된 franchise에서 나왔다. StarCraft II·Cataclysm·Diablo 파이프라인, 매출의 27% 구독, digital distribution으로 300~500bp margin 확대를 기대해 목표 $16, downside $9를 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 업계 부진과 Q4 실적 전 불안을 가격에 반영한 ATVI를 샀다. World of Warcraft는 약 45% operating margin으로 회사이익의 거의 절반, 매출 80%+가 검증된 franchise에서 나왔다. StarCraft II·Cataclysm·Diablo 파이프라인, 매출의 27% 구독, digital distribution으로 300~500bp margin 확대를 기대해 목표 $16, downside $9를 제시했다. | WoW는 뒤에 둔화했지만 Call of Duty, Blizzard 신작, digital DLC와 이후 King이 이익기반을 넓혔다. $16 목표는 장기 달성됐고 franchise·digital mix의 인과가 맞았다. |
| 밸류에이션·청구권 | 목표 $16/downside $9 | SQL 정밀 성과 미수록; 목표 $16 달성 후 장기 상승 |
| 촉매·시간 | StarCraft II·Cataclysm·Diablo·buyback | digital mix·CoD가 WoW 둔화를 상쇄 |
| 사전 반증조건 | WoW 이익이 절반 줄고 핵심 출시가 12개월 지연돼도 downside $9가 유지되는가? | 핵심 오류: WoW 이익집중과 release slippage |

### 실제 전개와 투자 결론

WoW는 뒤에 둔화했지만 Call of Duty, Blizzard 신작, digital DLC와 이후 King이 이익기반을 넓혔다. $16 목표는 장기 달성됐고 franchise·digital mix의 인과가 맞았다.

**종합판정: 성공.** 단일 히트가 아니라 반복 IP·구독·digital margin을 묶고 순현금과 downside를 제시했다. 다만 출시일정이 변하는 게임산업에서 목표기간은 더 보수적이어야 했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| WoW margin | ~45% | cash cow | 고마진 지속 후 둔화 | 부분 |
| 구독매출 | 27% | 안정 | WoW 감소 | 부분 |
| margin | +300~500bp | digital leverage | 장기 개선 | 적중 |
| 목표 | $16 | 상승 | 달성 | 적중 |

재사용 질문: **WoW 이익이 절반 줄고 핵심 출시가 12개월 지연돼도 downside $9가 유지되는가?**

## 3. 2011-11-14 — WoW 이익집중·성숙 숏

### 원 투자논지

$14 위에서 6~12개월 숏을 제시했다. WoW가 operating income의 50%+인데 회원이 줄고, 추정 EPS $0.78가 컨센서스 $0.96에 못 미쳐 13~14x를 적용하면 $10 미만이라고 봤다. Call of Duty Elite의 유료전환도 불확실하다고 판단했다. 반대위험은 $3.5bn 현금과 $1bn buyback이었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $14 위에서 6~12개월 숏을 제시했다. WoW가 operating income의 50%+인데 회원이 줄고, 추정 EPS $0.78가 컨센서스 $0.96에 못 미쳐 13~14x를 적용하면 $10 미만이라고 봤다. Call of Duty Elite의 유료전환도 불확실하다고 판단했다. 반대위험은 $3.5bn 현금과 $1bn buyback이었다. | WoW 회원감소는 맞았지만 Call of Duty의 연례 프랜차이즈·digital monetization과 후속 신작이 이익을 방어했다. 강한 대차대조표도 숏 하방을 제한해 가격논지는 실패했다. |
| 밸류에이션·청구권 | 13~14x×$0.78=< $10 | SQL 정밀 성과 미수록; 장기 상승으로 숏 실패 |
| 촉매·시간 | WoW 감소·CoD Elite 미달 | CoD·digital revenue가 WoW 둔화를 상쇄 |
| 사전 반증조건 | WoW가 줄어도 다른 IP의 bookings가 늘면 portfolio 전체 FCF가 실제 감소하는가? | 핵심 오류: 한 제품 감소를 회사 전체 terminal decline으로 확장 |

### 실제 전개와 투자 결론

WoW 회원감소는 맞았지만 Call of Duty의 연례 프랜차이즈·digital monetization과 후속 신작이 이익을 방어했다. 강한 대차대조표도 숏 하방을 제한해 가격논지는 실패했다.

**종합판정: 실패.** 이익집중 리스크를 봤지만 portfolio IP가 한 franchise의 쇠퇴를 대체할 option을 과소평가했다. 현금과 buyback은 단순 risk가 아니라 시간을 버는 실질 자산이었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| WoW 이익비중 | >50% | 감소 충격 | 회원감소 | 적중 |
| EPS | $0.78 vs $0.96 | miss | portfolio가 방어 | 부분 |
| 목표 | <$10 | 하락 | 장기 상승 | 실패 |
| 현금/buyback | $3.5bn/$1bn | upside risk | 실질 하방 | 적중 |

재사용 질문: **WoW가 줄어도 다른 IP의 bookings가 늘면 portfolio 전체 FCF가 실제 감소하는가?**

## 4. 2019-03-26 — 노후 IP·battle royale 경쟁 숏

### 원 투자논지

Call of Duty와 WoW를 낡은 franchise로 보고 Fortnite·Apex Legends가 attention을 빼앗는다고 주장했다. 2019 EBIT 약 17% 감소, King 제외 이익이 2011 이하인데 next-year earnings 약 20x는 높아 장기 $30 미만을 제시했다. Google·Apple·Amazon·Microsoft 인수는 명시적 risk였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Call of Duty와 WoW를 낡은 franchise로 보고 Fortnite·Apex Legends가 attention을 빼앗는다고 주장했다. 2019 EBIT 약 17% 감소, King 제외 이익이 2011 이하인데 next-year earnings 약 20x는 높아 장기 $30 미만을 제시했다. Google·Apple·Amazon·Microsoft 인수는 명시적 risk였다. | CoD·King·digital bookings가 회복했고 주가는 상승했다. 가장 치명적으로, 논지의 risk로만 적은 Microsoft가 2022년 주당 $95 인수를 발표·2023년 종결했다. |
| 밸류에이션·청구권 | ~20x next-year earnings, 장기 < $30 | SQL 정밀 성과 미수록; 최종 $95 현금인수 |
| 촉매·시간 | 2019 EBIT 감소·player 이탈 | Call of Duty 성과·bookings 회복 |
| 사전 반증조건 | 인수자가 IP와 플랫폼 전략가치를 현금흐름보다 높게 평가할 때 최대손실은? | 핵심 오류: 명시한 인수 tail risk를 position sizing에 반영하지 않음 |

### 실제 전개와 투자 결론

CoD·King·digital bookings가 회복했고 주가는 상승했다. 가장 치명적으로, 논지의 risk로만 적은 Microsoft가 2022년 주당 $95 인수를 발표·2023년 종결했다.

**종합판정: 치명적 실패.** 경쟁게임의 동시접속과 한 해 EBIT 감소를 IP의 영구노후화로 외삽했다. 전략적 buyer risk가 현실화될 때 손실상한이 없는 숏이었다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2019 EBIT | ~-17% | 구조감소 | 단기 감소 후 회복 | 부분 |
| 경쟁 | Fortnite/Apex | IP 쇠퇴 | CoD 공존·회복 | 실패 |
| 목표 | <$30 | 하락 | $95 cash | 치명적 실패 |
| M&A risk | Microsoft 등 | 낮은 확률 | Microsoft 현실화 | 정확히 반대 |

재사용 질문: **인수자가 IP와 플랫폼 전략가치를 현금흐름보다 높게 평가할 때 최대손실은?**

## 5. 2019-05-01 — bad-news 과잉반응·IP 롱

### 원 투자논지

나쁜 보도와 restructuring으로 40%+ 하락한 주식을 30% upside와 작은 downside로 봤다. 2018 매출 $7.5bn, 10년 CAGR 11%, gross margin 65%·operating margin 24%, digital mix로 gross margin 46%→66%가 된 점을 강조했다. King은 $5.9bn에 약 6.4x EBITDA로 산 우량 모바일 자산이며, EBITDA $2.5bn×19+순현금 $1.6bn으로 $62를 계산했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 나쁜 보도와 restructuring으로 40%+ 하락한 주식을 30% upside와 작은 downside로 봤다. 2018 매출 $7.5bn, 10년 CAGR 11%, gross margin 65%·operating margin 24%, digital mix로 gross margin 46%→66%가 된 점을 강조했다. King은 $5.9bn에 약 6.4x EBITDA로 산 우량 모바일 자산이며, EBITDA $2.5bn×19+순현금 $1.6bn으로 $62를 계산했다. | franchise와 digital monetization이 회복했고 최종적으로 Microsoft가 $95를 지급했다. 다만 직장문화·지배구조 문제가 2021년 큰 drawdown과 인력위험을 만들었으므로 ‘bad press’ 전부가 소음은 아니었다. |
| 밸류에이션·청구권 | EBITDA $2.5bn×19+순현금=$62 | SQL 정밀 성과 미수록; $62 목표 초과·최종 $95 |
| 촉매·시간 | restructuring·신작·digital mix | CoD·King bookings와 margin 회복 |
| 사전 반증조건 | 핵심인력 이탈과 12개월 출시지연에도 $62가 유지되는가? | 핵심 오류: 비재무 culture risk의 현금흐름 전이 과소평가 |

### 실제 전개와 투자 결론

franchise와 digital monetization이 회복했고 최종적으로 Microsoft가 $95를 지급했다. 다만 직장문화·지배구조 문제가 2021년 큰 drawdown과 인력위험을 만들었으므로 ‘bad press’ 전부가 소음은 아니었다.

**종합판정: 성공.** 낮아진 가격과 IP portfolio, digital margin을 연결한 점은 맞았다. 문화위기를 단순 sentiment가 아니라 제작 pipeline·key-person risk로 stress했다면 더 완전했을 것이다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 2018 매출 | $7.5bn | 회복/성장 | 성장 | 적중 |
| gross margin | 65% | digital로 유지 | 고마진 유지 | 적중 |
| King 인수가 | $5.9bn/~6.4x | 가치창출 | 모바일 축 강화 | 적중 |
| 목표 | $62 | 30% | $95 cash | 초과 |

재사용 질문: **핵심인력 이탈과 12개월 출시지연에도 $62가 유지되는가?**

## 6. 2021-02-06 — digital monetization·margin 복리 롱

### 원 투자논지

$101.61에서 36개월 연 18% IRR을 기대했다. Activision 50%·Blizzard 24%·King 27%의 portfolio, 각각 MAU 128m/29m/240m, DLC·MTX·digital mix가 operating margin을 2016년 21%에서 2020년 35%로 높였고 2025년까지 추가 500bp가 가능하다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $101.61에서 36개월 연 18% IRR을 기대했다. Activision 50%·Blizzard 24%·King 27%의 portfolio, 각각 MAU 128m/29m/240m, DLC·MTX·digital mix가 operating margin을 2016년 21%에서 2020년 35%로 높였고 2025년까지 추가 500bp가 가능하다고 봤다. | 제품·digital economics는 남았지만 문화스캔들·출시지연·경영진 리스크가 주가를 훼손했다. Microsoft의 현금인수가는 $95로 진입 $101.61보다 낮아, 시간비용까지 포함하면 목표 IRR은 실패했다. |
| 밸류에이션·청구권 | 36개월 18% IRR·margin +500bp | 진입 $101.61→최종 $95 cash; 약 -6.5% 전 시간비용 |
| 촉매·시간 | 신작·DLC/MTX·margin 확대 | California 소송으로 직장문화·인력·경영진 위험 표면화 |
| 사전 반증조건 | 매출이 12개월 지연되고 exit multiple이 20% 낮아져도 18% IRR인가? | 핵심 오류: 프랜차이즈 질을 entry valuation과 governance safety로 착각 |

### 실제 전개와 투자 결론

제품·digital economics는 남았지만 문화스캔들·출시지연·경영진 리스크가 주가를 훼손했다. Microsoft의 현금인수가는 $95로 진입 $101.61보다 낮아, 시간비용까지 포함하면 목표 IRR은 실패했다.

**종합판정: 실패.** 좋은 사업을 이미 높은 가격에 사면서 nonfinancial governance risk와 pipeline concentration을 충분히 반영하지 않았다. 이후 인수는 회사가치 floor였지만 이 가격의 주주수익은 구하지 못했다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $101.61 | 36개월 18% IRR | $95 cash | 실패 |
| operating margin | 21%→35% | +500bp | 사업은 고마진 유지 | 부분 |
| MAU | 128m/29m/240m | monetize | segment별 변동 | 부분 |
| governance | 낮게 반영 | 무영향 | 스캔들·지연 | 실패 |

재사용 질문: **매출이 12개월 지연되고 exit multiple이 20% 낮아져도 18% IRR인가?**

## 7. 2021-09-23 — 스캔들 과잉반응·pipeline 롱

### 원 투자논지

Q2 이후 약 22% 하락한 $75 부근에서 성희롱·노동문화와 중국우려가 engagement를 크게 훼손하지 않는다고 봤다. 2023 EPS $4.50×20=$90 base, $4.70×23=$110 bull을 제시했고 신작 pipeline, 순현금·buyback, Bobby Kotick의 강한 자본배분을 근거로 들었다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | Q2 이후 약 22% 하락한 $75 부근에서 성희롱·노동문화와 중국우려가 engagement를 크게 훼손하지 않는다고 봤다. 2023 EPS $4.50×20=$90 base, $4.70×23=$110 bull을 제시했고 신작 pipeline, 순현금·buyback, Bobby Kotick의 강한 자본배분을 근거로 들었다. | Microsoft가 2022년 $95를 제시해 가격결과는 성공했다. 그러나 스캔들은 경영진·인력·출시일정에 실제로 영향을 줬고, 오히려 낮아진 가격과 governance 위기가 매각가능성을 높였다. 성공의 직접촉매는 원문이 중심에 두지 않은 M&A였다. |
| 밸류에이션·청구권 | $90 base/$110 bull | 약 $75→$95 cash로 성공 |
| 촉매·시간 | release pipeline·buyback·sentiment 정상화 | Microsoft $95 현금인수 발표 |
| 사전 반증조건 | M&A가 없어도 인력유출·지연을 반영한 standalone $90이 성립하는가? | 핵심 오류: governance 문제를 engagement 단일지표로 축소 |

### 실제 전개와 투자 결론

Microsoft가 2022년 $95를 제시해 가격결과는 성공했다. 그러나 스캔들은 경영진·인력·출시일정에 실제로 영향을 줬고, 오히려 낮아진 가격과 governance 위기가 매각가능성을 높였다. 성공의 직접촉매는 원문이 중심에 두지 않은 M&A였다.

**종합판정: 가격 성공·인과 일부 오류.** valuation range는 맞았지만 culture risk를 과소평가하고 CEO를 강점으로 본 판단은 약했다. 나쁜 governance 때문에 생긴 할인에서 buyer가 가치를 회수한 사건이다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | ~$75 | base $90 | $95 cash | 성공 |
| bull | $110 | pipeline | 미달 | 부분 |
| 문화위기 | 과잉반응 | engagement 무영향 | 실제 중대 | 판단오류 |
| 촉매 | 신작/buyback | rerating | Microsoft 인수 | 다른 인과 |

재사용 질문: **M&A가 없어도 인력유출·지연을 반영한 standalone $90이 성립하는가?**

## 8. 2022-03-23 — Microsoft merger arbitrage 롱

### 원 투자논지

주당 $95 현금거래가 약 15개월 뒤 닫힌다고 보고 두 자릿수 IRR을 제시했다. 당시 spread가 반영한 종결확률을 약 48%로 추정했으나 결합 gaming share 약 13%, 플랫폼·콘텐츠 시장정의와 $2~3bn reverse termination fee를 근거로 규제위험을 낮게 봤다. break case도 제품 supercycle로 $95 이상이라고 주장했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 주당 $95 현금거래가 약 15개월 뒤 닫힌다고 보고 두 자릿수 IRR을 제시했다. 당시 spread가 반영한 종결확률을 약 48%로 추정했으나 결합 gaming share 약 13%, 플랫폼·콘텐츠 시장정의와 $2~3bn reverse termination fee를 근거로 규제위험을 낮게 봤다. break case도 제품 supercycle로 $95 이상이라고 주장했다. | FTC 소송·CMA 반대로 원래 2023-07-18 기한을 넘겼고 cloud rights를 수정했지만 2023-10-13 주당 $95로 종결됐다. 약 3개월 지연에도 거래방향과 회수가는 맞았다. break case $95 이상은 검증되지 않았다. |
| 밸류에이션·청구권 | $95 cash, spread 기준 두 자릿수 IRR | 주당 $95 현금회수; 예상보다 약 3개월 지연 |
| 촉매·시간 | antitrust 승인·종결 | FTC가 공식 소송을 제기해 종결확률·기간 악화 |
| 사전 반증조건 | FTC·CMA가 모두 막고 deal이 깨질 때 독립가치를 2021 peak가 아닌 현재 pipeline으로 계산했는가? | 핵심 오류: break value를 deal price 이상으로 두어 downside 과소평가 |

### 실제 전개와 투자 결론

FTC 소송·CMA 반대로 원래 2023-07-18 기한을 넘겼고 cloud rights를 수정했지만 2023-10-13 주당 $95로 종결됐다. 약 3개월 지연에도 거래방향과 회수가는 맞았다. break case $95 이상은 검증되지 않았다.

**종합판정: 매우 성공.** spread와 market-implied 확률, 규제논리, termination fee를 구조화한 점이 좋았다. 단 break price를 deal price 이상으로 둔 것은 낙관적이며, 성공은 규제지연을 버틸 기간·포지션 크기가 전제다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| deal price | $95 cash | 회수 | $95 회수 | 적중 |
| 예상 종결 | ~15개월/2023-07 | 기한내 | 2023-10-13 | 3개월 지연 |
| implied close | ~48% | 과소평가 | 종결 | 적중 |
| break case | >$95 주장 | 하방 없음 | 미검증 | 과신 |

재사용 질문: **FTC·CMA가 모두 막고 deal이 깨질 때 독립가치를 2021 peak가 아닌 현재 pipeline으로 계산했는가?**

## 2024-01-31 기준 기업 결론

Microsoft는 2023년 10월 13일 Activision Blizzard King 인수를 완료했다. 주주는 주당 $95 현금을 받았고 상장은 끝났다. 사업프랜차이즈의 질뿐 아니라 FTC·CMA 반대, 종결기한 연장과 수정거래를 버틴 merger-arb 분석이 최종 수익을 결정했다.

## 주요 근거

- [Activision Blizzard 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/718877/000162828022003992/atvi-20211231.htm) — Activision·Blizzard·King 사업, bookings, MAU와 문화·인력 위험.
- [Microsoft to acquire Activision Blizzard](https://news.microsoft.com/source/2022/01/18/microsoft-to-acquire-activision-blizzard-to-bring-the-joy-and-community-of-gaming-to-everyone-across-every-device/) — 주당 $95 전액현금, 거래가치 $68.7bn과 조건.
- [FTC seeks to block Microsoft acquisition](https://www.ftc.gov/news-events/news/press-releases/2022/12/ftc-seeks-block-microsoft-corps-acquisition-activision-blizzard-inc) — 반독점 소송과 콘텐츠 봉쇄 우려.
- [Microsoft completes acquisition of Activision Blizzard King](https://news.microsoft.com/source/2023/10/13/microsoft-completes-acquisition-of-activision-blizzard-king/) — 거래 종결과 Microsoft 편입.

---

# Alibaba Group (BABA) — 기업과 비즈니스

Alibaba는 Taobao·Tmall의 중국 전자상거래, Alibaba.com·AliExpress·Lazada 등 국제상거래, Alibaba Cloud, Cainiao 물류, Ele.me·Amap 지역서비스, 디지털미디어와 Ant Group 지분을 묶은 중국 인터넷 지주회사다. 핵심 China commerce는 직접 재고를 소유하기보다 상인에게 트래픽·광고·추천·결제 인프라를 제공하고 customer-management/commission 수익을 얻어 높은 마진과 현금을 만들었다. 그 현금을 물류·로컬서비스·해외·클라우드에 재투자하는 구조라 segment별 적자와 본사 자본배분을 분리해야 한다. 네트워크 효과는 소비자·상인·데이터에서 나오지만 JD·PDD·Douyin과의 경쟁, 소비둔화, merchant monetization 부담이 약화시킬 수 있다. 미국 ADR 주주는 중국 운영회사 지분이 아니라 Cayman VIE 청구권을 보유하고, 규제·Ant 구조조정·데이터안보·미중 감사·ADR 상장위험은 valuation discount가 아니라 현금귀속과 통제의 문제다. SOTP는 현금·상장지분·Ant·Cloud 가치를 더하되 세금·holding discount·통제불능·지속 적자와 국가정책을 빼야 한다.

## 돈을 버는 구조

- 수익: commerce 광고/수수료·직매입, cloud 사용량, 물류·배달, 국제사업의 혼합
- moat: 소비자·상인·데이터 network effect와 결제·물류 생태계
- 청구권 위험: ADR→Cayman VIE 계약→중국 영업회사로 이어지는 간접 구조
- 가치함정: core FCF에 현금·투자자산을 더해도 재투자손실·규제·holding discount가 상쇄 가능

## 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 논지 | 실제 결과 | 판정 |
|---|---|---|---|---|---|
| 2017-10-04 | Short | Long | 중국 commerce·cloud network 롱 | 1년 -12.72%, 3년 +61.14%, 5년 -55.03% | 3년 성공·5년 치명적 실패 |
| 2019-02-11 | Short | Short | 거시·회계·VIE 숏 | 1년 -28.75%, 2년 -58.73%, 3년 +26.51% (숏 방향) | 타이밍 실패·후행 가격 성공 |
| 2019-02-22 | Short | Long | core 이익·option SOTP 롱 | 1년 +12.50%, 2년 +38.61%, 3년 -38.37% | 목표 달성 후 장기 실패 |
| 2021-09-08 | Short | Long | 규제 공포·저배수 롱 | 1개월 -3.47%, 3개월 -24.97%, 6개월 -41.04%, 1년 -46.50% | 치명적 실패 |
| 2022-04-04 | Short | Long | 65% 하락·SOTP 롱 | 1개월 -8.64%, 3개월 +8.23%, 6개월 -27.52% | 실패 |
| 2022-10-22 | Short | Long | 5x core FCF·극단공포 롱 | 1개월 +21.82%, 3개월 +89.80%; 이후 일부 반납 | 전술적 매우 성공·장기 부분 |

## 1. 2017-10-04 — 중국 commerce·cloud network 롱

### 원 투자논지

trailing revenue 16.5x, EBITDA 40x+의 비싼 숫자에도 중국 commerce의 소비자·상인 network effect, 광고 monetization, Alibaba Cloud, Ant, Cainiao와 new retail의 거대한 TAM이 고성장을 지속한다고 봤다. core cash flow가 신규사업 투자손실을 보조하며 여러 option을 만든다는 장기 복리 논지였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | trailing revenue 16.5x, EBITDA 40x+의 비싼 숫자에도 중국 commerce의 소비자·상인 network effect, 광고 monetization, Alibaba Cloud, Ant, Cainiao와 new retail의 거대한 TAM이 고성장을 지속한다고 봤다. core cash flow가 신규사업 투자손실을 보조하며 여러 option을 만든다는 장기 복리 논지였다. | commerce·cloud 규모는 성장해 3년 가격성과가 +61.14%였지만 5년은 -55.03%였다. 2020년 이후 Ant 중단·플랫폼규제·경쟁·VIE/geopolitics와 재투자수익률 악화가 성장가치를 압도했다. |
| 밸류에이션·청구권 | 16.5x revenue·40x+ EBITDA를 성장으로 정당화 | 1년 -12.72%, 3년 +61.14%, 5년 -55.03% |
| 촉매·시간 | cloud·Ant·new retail·monetization | Ant IPO 중단으로 국가정책·통제 위험 현실화 |
| 사전 반증조건 | 규제가 monetization을 낮추고 option 자산을 분리상장하지 못해도 현재배수에서 IRR이 남는가? | 핵심 오류: network effect를 규제·통제권보다 우위인 영구 moat로 가정 |

### 실제 전개와 투자 결론

commerce·cloud 규모는 성장해 3년 가격성과가 +61.14%였지만 5년은 -55.03%였다. 2020년 이후 Ant 중단·플랫폼규제·경쟁·VIE/geopolitics와 재투자수익률 악화가 성장가치를 압도했다.

**종합판정: 3년 성공·5년 치명적 실패.** 사업 TAM과 초기 성장만 맞고 청구권·국가정책·starting multiple을 장기 현금귀속으로 연결하지 못했다. 긴 duration 주식은 성장률뿐 아니라 누가 현금을 통제하는지가 중요하다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| valuation | 16.5x sales/40x+ EBITDA | 고성장으로 소화 | 5년 multiple 붕괴 | 실패 |
| 3년 수익 | 장기 롱 | 복리 | +61.14% | 성공 |
| 5년 수익 | 복리 | 상승 | -55.03% | 실패 |
| Ant | 가치 option | IPO/성장 | IPO 중단·재편 | 실패 |

재사용 질문: **규제가 monetization을 낮추고 option 자산을 분리상장하지 못해도 현재배수에서 IRR이 남는가?**

## 2. 2019-02-11 — 거시·회계·VIE 숏

### 원 투자논지

$167.36에서 Alibaba의 지배력은 인정하되 미중 무역전쟁, 중국 소비둔화, CNY 약세, VIE와 공격적 회계 때문에 향후 5년 40% 매출성장이 불가능하다고 봤다. $200 이상 상승을 risk로 제시했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $167.36에서 Alibaba의 지배력은 인정하되 미중 무역전쟁, 중국 소비둔화, CNY 약세, VIE와 공격적 회계 때문에 향후 5년 40% 매출성장이 불가능하다고 봤다. $200 이상 상승을 risk로 제시했다. | 1년·2년 숏 방향성과는 -28.75%/-58.73%로 크게 실패했고 3년에는 +26.51%로 뒤집혔다. 뒤늦은 하락의 직접원인은 무역전쟁보다 중국의 플랫폼·Ant 규제와 경쟁이었다. |
| 밸류에이션·청구권 | $167.36, $200+ risk | 1년 -28.75%, 2년 -58.73%, 3년 +26.51% (숏 방향) |
| 촉매·시간 | 무역전쟁·성장둔화·CNY | 주가가 $300 부근까지 상승해 숏 경로 파괴 |
| 사전 반증조건 | 주가가 80% 먼저 오를 때도 견딜 수 있는 sizing과 명확한 규제촉매가 있는가? | 핵심 오류: 옳을 수 있는 장기 위험을 즉시 작동할 촉매로 취급 |

### 실제 전개와 투자 결론

1년·2년 숏 방향성과는 -28.75%/-58.73%로 크게 실패했고 3년에는 +26.51%로 뒤집혔다. 뒤늦은 하락의 직접원인은 무역전쟁보다 중국의 플랫폼·Ant 규제와 경쟁이었다.

**종합판정: 타이밍 실패·후행 가격 성공.** 위험목록은 일부 맞았지만 촉매와 인과가 틀렸다. 거시 우려로 숏한 고성장 플랫폼은 수년간 multiple·이익이 더 늘 수 있고, 나중의 다른 사건으로 난 이익을 원 thesis 성공이라 부르면 안 된다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $167.36 | 하락 | 2년 숏 -58.73% | 실패 |
| 1년 숏 | 하락 기대 | 수익 | -28.75% | 실패 |
| 3년 숏 | 하락 | 수익 | +26.51% | 후행 성공 |
| 주원인 | trade war | 성장붕괴 | 국내규제·경쟁 | 인과오류 |

재사용 질문: **주가가 80% 먼저 오를 때도 견딜 수 있는 sizing과 명확한 규제촉매가 있는가?**

## 3. 2019-02-22 — core 이익·option SOTP 롱

### 원 투자논지

delivery·Lazada·Cainiao·Cloud·content 적자가 core commerce의 60%+ EBIT margin과 현금력을 가린다고 봤다. Cloud와 Ant를 각각 약 $50bn, core customer-management revenue를 고배수로 평가해 목표 $242~298, 17~30% IRR을 제시했다. 신규사업 손실의 peak와 무역분쟁 완화가 촉매였다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | delivery·Lazada·Cainiao·Cloud·content 적자가 core commerce의 60%+ EBIT margin과 현금력을 가린다고 봤다. Cloud와 Ant를 각각 약 $50bn, core customer-management revenue를 고배수로 평가해 목표 $242~298, 17~30% IRR을 제시했다. 신규사업 손실의 peak와 무역분쟁 완화가 촉매였다. | 주가는 2020년 $300 안팎까지 올라 목표를 달성했고 2년 성과 +38.61%였다. 그러나 3년 -38.37%로 반전했다. 적자사업·Ant·Cloud를 option으로 더한 SOTP는 규제·통제·재투자손실이 동시에 발생할 때 하방이 아니었다. |
| 밸류에이션·청구권 | 목표 $242~298; Cloud·Ant 각 ~$50bn | 1년 +12.50%, 2년 +38.61%, 3년 -38.37% |
| 촉매·시간 | 신규손실 peak·trade resolution·rerating | Ant IPO 중단으로 핵심 option의 실현경로 소멸 |
| 사전 반증조건 | Ant·Cloud가 50% holding discount이고 적자사업 투자가 지속돼도 목표 하단이 남는가? | 핵심 오류: SOTP 합계를 회수가능한 주주가치로 간주 |

### 실제 전개와 투자 결론

주가는 2020년 $300 안팎까지 올라 목표를 달성했고 2년 성과 +38.61%였다. 그러나 3년 -38.37%로 반전했다. 적자사업·Ant·Cloud를 option으로 더한 SOTP는 규제·통제·재투자손실이 동시에 발생할 때 하방이 아니었다.

**종합판정: 목표 달성 후 장기 실패.** core/option 분해는 유용했지만 option 가치에는 실현확률·holding discount가 필요하다. 목표에서 매도했다면 성공, 장기 compounder로 보유했다면 실패다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 목표 | $242~298 | 17~30% IRR | 2020 달성 | 성공 |
| 2년 수익 | 상승 | IRR | +38.61% | 성공 |
| 3년 수익 | 상승 지속 | compound | -38.37% | 실패 |
| Ant/Cloud | 각 ~$50bn | 가치실현 | Ant 중단·Cloud 분사 실패 | 실패 |

재사용 질문: **Ant·Cloud가 50% holding discount이고 적자사업 투자가 지속돼도 목표 하단이 남는가?**

## 4. 2021-09-08 — 규제 공포·저배수 롱

### 원 투자논지

고점 $307에서 45% 하락한 가격이 FY23 earnings 16x, FCF yield 6%이며 20% 성장과 합쳐 26% 수익률을 준다고 봤다. core commerce가 장기간 20%, Cloud가 50~60% 성장해 AWS 같은 30% margin에 도달하고 목표 $350(105% upside)가 가능하다고 주장했다. CCP가 회사를 파괴할 확률을 50%로 둬도 싸다는 식으로 규제를 가격변수로 처리했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 고점 $307에서 45% 하락한 가격이 FY23 earnings 16x, FCF yield 6%이며 20% 성장과 합쳐 26% 수익률을 준다고 봤다. core commerce가 장기간 20%, Cloud가 50~60% 성장해 AWS 같은 30% margin에 도달하고 목표 $350(105% upside)가 가능하다고 주장했다. CCP가 회사를 파괴할 확률을 50%로 둬도 싸다는 식으로 규제를 가격변수로 처리했다. | 1년 가격성과는 -46.50%였다. 규제만이 아니라 PDD·Douyin 경쟁, 중국소비 둔화, 고객관리수익 약화, 계속되는 신규사업 투자가 성장·margin 가정을 무너뜨렸다. Cloud 50~60%와 $350는 실현되지 않았다. |
| 밸류에이션·청구권 | 16x FY23 earnings·6% FCF yield·목표 $350 | 1개월 -3.47%, 3개월 -24.97%, 6개월 -41.04%, 1년 -46.50% |
| 촉매·시간 | 규제완화·20% commerce·50~60% cloud | 분기성장 둔화·가이던스 하향으로 규제 외 경쟁문제 확인 |
| 사전 반증조건 | commerce 5%, cloud 20%, exit 10x가 동시에 오면 intrinsic value가 얼마인가? | 핵심 오류: 성장·margin·multiple 손상을 독립확률로 잘못 모델링 |

### 실제 전개와 투자 결론

1년 가격성과는 -46.50%였다. 규제만이 아니라 PDD·Douyin 경쟁, 중국소비 둔화, 고객관리수익 약화, 계속되는 신규사업 투자가 성장·margin 가정을 무너뜨렸다. Cloud 50~60%와 $350는 실현되지 않았다.

**종합판정: 치명적 실패.** 극단적 정책위험을 확률 하나로 할인하면서 그 정책이 성장률·margin·자본배분·terminal multiple을 동시에 바꾸는 상관관계를 놓쳤다. 16x는 정상 EPS가 정상일 때만 싸다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 목표 | $350 | 105% | 1y -46.50% | 실패 |
| commerce 성장 | 장기 20% | 지속 | 급격 둔화 | 실패 |
| cloud 성장 | 50~60% | 30% margin | 성장 둔화 | 실패 |
| valuation | 16x/6% FCF | 하방 | normal earnings 하향 | 함정 |

재사용 질문: **commerce 5%, cloud 20%, exit 10x가 동시에 오면 intrinsic value가 얼마인가?**

## 5. 2022-04-04 — 65% 하락·SOTP 롱

### 원 투자논지

고점 대비 65% 하락한 Alibaba를 online retail 55%, Cloud 45% 성장사업으로 설명했다. 현금 $82bn, 상장투자 $25bn, Ant 33% 지분과 $25bn buyback을 하방으로 놓고 core retail 25x, Cloud 5x revenue, Ant ex-lending 25x, Youku 5x의 SOTP로 목표 $268을 제시했다. 규제에는 ‘method to the madness’가 있다고 봤다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | 고점 대비 65% 하락한 Alibaba를 online retail 55%, Cloud 45% 성장사업으로 설명했다. 현금 $82bn, 상장투자 $25bn, Ant 33% 지분과 $25bn buyback을 하방으로 놓고 core retail 25x, Cloud 5x revenue, Ant ex-lending 25x, Youku 5x의 SOTP로 목표 $268을 제시했다. 규제에는 ‘method to the madness’가 있다고 봤다. | 6개월 성과는 -27.52%였고 2024-01-31까지 목표에 크게 못 미쳤다. Cloud 성장 둔화·분사중단, 중국소비·경쟁, VIE/holding discount가 SOTP 실현을 막았다. cash와 investments도 재투자·buyback의 timing과 통제문제를 제거하지 못했다. |
| 밸류에이션·청구권 | SOTP 목표 $268; cash $82bn | 1개월 -8.64%, 3개월 +8.23%, 6개월 -27.52% |
| 촉매·시간 | $25bn buyback·규제완화·Cloud | commerce 성장·macro 약화와 6개월 하락 |
| 사전 반증조건 | 모든 non-core에 50% discount, core 10x를 적용해도 upside가 있는가? | 핵심 오류: SOTP의 합산가치를 실현가능가치로 오해 |

### 실제 전개와 투자 결론

6개월 성과는 -27.52%였고 2024-01-31까지 목표에 크게 못 미쳤다. Cloud 성장 둔화·분사중단, 중국소비·경쟁, VIE/holding discount가 SOTP 실현을 막았다. cash와 investments도 재투자·buyback의 timing과 통제문제를 제거하지 못했다.

**종합판정: 실패.** 각 자산에 선진시장 comparable multiple을 붙이고 국가·통제·세금·적자사업 discount를 충분히 빼지 않았다. 현금이 많아도 주주가 회수할 수 있는 정책이 확인돼야 floor다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 고점대비 | -65% | mean reversion | 추가 하락 | 실패 |
| 현금 | $82bn | floor | 할인 지속 | 미달 |
| Cloud | 45% 성장 | 5x sales | 성장둔화·분사중단 | 실패 |
| 6개월 | 상승 | 목표 접근 | -27.52% | 실패 |

재사용 질문: **모든 non-core에 50% discount, core 10x를 적용해도 upside가 있는가?**

## 6. 2022-10-22 — 5x core FCF·극단공포 롱

### 원 투자논지

$72, 시총 약 $190bn과 고점 대비 -77%에서 China commerce $82bn+Cloud $10bn이 매출의 약 80%, profit/FCF의 100%+를 만든다고 봤다. cash·투자자산을 차감한 EV $78~112bn, core commerce EBITDA 약 $25bn과 FCF $20~25bn, 약 5x FCF를 계산했다. $25bn buyback 중 $9.2bn 집행, VIE·지정학을 명시하고 성장 0%여도 높은 IRR이 가능하다고 주장했다.

### 논지 구조와 검증

| 축 | 당시 주장 | 실제 검증 |
|---|---|---|
| 사업·단위경제성 | $72, 시총 약 $190bn과 고점 대비 -77%에서 China commerce $82bn+Cloud $10bn이 매출의 약 80%, profit/FCF의 100%+를 만든다고 봤다. cash·투자자산을 차감한 EV $78~112bn, core commerce EBITDA 약 $25bn과 FCF $20~25bn, 약 5x FCF를 계산했다. $25bn buyback 중 $9.2bn 집행, VIE·지정학을 명시하고 성장 0%여도 높은 IRR이 가능하다고 주장했다. | 3개월 성과 +89.80%로 극단적 sentiment 반등을 정확히 잡았다. 그러나 이후 상당 부분 반납했고 2024-01-31에는 장기 value realization이 완전히 확인되지 않았다. 낮은 가격이 tactical margin of safety를 만들었지만 VIE·경쟁·자본배분은 남았다. |
| 밸류에이션·청구권 | EV $78~112bn, core FCF $20~25bn≈5x | 1개월 +21.82%, 3개월 +89.80%; 이후 일부 반납 |
| 촉매·시간 | 제로코로나 완화·buyback·극단 sentiment | 3개월 +89.80%로 tactical 목표 실현 |
| 사전 반증조건 | 성장 0%, core FCF -30%, 현금 50% haircut에서도 buyback 후 주당가치가 증가하는가? | 핵심 오류: 싼 배수라도 VIE 현금귀속과 경쟁감소를 보장하지 않음 |

### 실제 전개와 투자 결론

3개월 성과 +89.80%로 극단적 sentiment 반등을 정확히 잡았다. 그러나 이후 상당 부분 반납했고 2024-01-31에는 장기 value realization이 완전히 확인되지 않았다. 낮은 가격이 tactical margin of safety를 만들었지만 VIE·경쟁·자본배분은 남았다.

**종합판정: 전술적 매우 성공·장기 부분.** 이전 BABA 롱과 달리 고성장을 요구하지 않고 core FCF와 이미 집행된 buyback으로 논지를 만들었다. 다만 5x는 FCF의 지속성과 주주귀속이 확인돼야 하며 단기 90% 급등을 장기 성공으로 자동 연장하면 안 된다.

### 핵심 수치

| 지표 | 글 당시 | 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입 | $72 | 극단저평가 | 3m +89.80% | 성공 |
| core FCF | $20~25bn | 지속 | 현금창출 유지·성장 약화 | 부분 |
| buyback | $25bn/$9.2bn 집행 | 주당가치 | 집행 | 적중 |
| 장기 | 무성장도 IRR | rerating | 2024까지 일부 반납 | 부분 |

재사용 질문: **성장 0%, core FCF -30%, 현금 50% haircut에서도 buyback 후 주당가치가 증가하는가?**

## 2024-01-31 기준 기업 결론

2023년 Alibaba는 사업을 여섯 그룹으로 재편해 외부자금·상장을 추진했지만 11월 Cloud Intelligence의 완전분사를 중단했다. 규제완화 기대만으로 SOTP가 자동 실현되지 않으며, 경쟁·중국 소비·VIE와 자본배분을 함께 봐야 한다.

## 주요 근거

- [Alibaba Fiscal Year 2023 Annual Report](https://static.alibabagroup.com/reports/fy2023/ar/ebook/en/index.html) — China commerce·Cloud·Cainiao·국제·로컬서비스와 VIE 구조.
- [Alibaba Investor Relations](https://www.alibabagroup.com/ir-news-filings) — 분기실적·20-F·자사주와 구조개편 자료.
- [Alibaba's First Dividend and Solid Q2 Results](https://www.alibabagroup.com/document-1663636438236790784) — Cloud 완전분사 중단과 가치실현 계획 변경.
- [Alibaba Chairman and CEO Succession](https://www.alibabagroup.com/document-1607836456397570048) — Cloud 분사 계획과 경영진 변화.

---

# 배치 공통 성공·실패 유형

| 유형 | 성공조건 | 실패조건 | 대표사례 |
|---|---|---|---|
| 플랫폼 규모경제 | 초기 손실이 검증가능한 cohort·global scale로 전환 | cash burn 자체를 성공/실패로 단정 | NFLX 2016 Long vs Short |
| recurring revenue | churn과 유지 CAC 후 FCF·debt service가 양수 | EBITDA/RMR multiple만 사용 | ADT 2013 Short·2018 Long |
| franchise portfolio | 한 IP 쇠퇴를 다른 IP·digital이 상쇄 | 단일 히트·MAU를 terminal로 외삽 | ATVI 2011 Short·2019 Long |
| event/arbitrage | 계약가격·proration·규제·기한·break value 분리 | signing을 closing으로, 혼합 tranche를 단일방향으로 저장 | ADT odd-lot·ATVI 2022 |
| SOTP/VIE | 실현확률·세금·holding discount·통제권 차감 | 자산합계를 ADR 주주가치로 간주 | BABA 2019·2021·2022 |

## 데이터 품질 메모

- 원 SQL short flag는 보존하고 실제 방향을 별도 필드로 교정했다.
- source performance는 가격비율을 수익률로 변환하고 실제 Long/Short 방향을 적용했다. 값이 없는 NFLX·ATVI는 수익률을 생성하지 않았다.
- ADT 2022-09는 odd-lot Long과 post-tender Short를 단일 수익률로 합치지 않았다.
- 평가기준은 원 글의 증권·가격·보유기간이며 2024-01-31 이후 사실은 판정에 사용하지 않았다.
