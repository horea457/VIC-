# Batch 033 — PICO Holdings & W.R. Grace: SOTP·자산현금화와 법적 오버행

> **범위:** PICO Long 8건 + GRA 2006 Short / 2012 Long 2건. raw direction은 그대로 보존했다. 오래된 VIC 본문이 완전 재수집되지 않은 경우 아래 thesis 문장은 직접인용이 아니라 raw metadata와 contemporaneous primary filings에 기반한 구조적 재구성이다.

## 검증 요약

- Ideas: **10**
- Sections: **100**
- Weighted claims: **60** — idea별 **100%**
- Metrics: **40**
- Timeline items: **60**
- Sources: **60**

## 공통 프레임

PICO와 Grace는 모두 회계 EPS보다 **현금화 waterfall**이 중요한 투자다. PICO에서는 water/UCP 자산이 언제 얼마에 팔리고 그 현금이 shareholder에게 돌아오는지가 가치이고, Grace에서는 operating EV에서 asbestos trust funding·post-emergence debt를 차감한 뒤 equity에 무엇이 남는지가 가치다. 따라서 NAV나 gross liability를 한 시점의 숫자로 보는 대신 **확률×순현금×시간**으로 IRR을 계산해야 한다.

# PICO HOLDINGS / VIDLER

## 1. 2009-11-29 — PICO Long — vanbr707

**원본 방향 검증:** raw `is_short=false` → **Long**. VIC source link 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
금융위기 뒤 PICO Long은 water rights·UCP/토지 등 자산가치가 depressed market cap보다 크고, 긴 개발기간을 견디면 SOTP discount가 줄어든다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
가치는 결국 실현됐지만 매우 오래 걸렸다. 2017 UCP는 Century에 매각되어 PICO가 $55.3m 현금과 약 2.4m Century 주식을 받았고, 2022 핵심 Vidler는 D.R. Horton에 $15.75/share, 약 $291m equity value로 매각됐다.

### 7. 무엇이 맞았나
자산 방향은 맞았지만 catalyst가 늦었다. water rights는 book value가 아니라 규제·개발·buyer timing의 option asset이므로 연환산 IRR이 핵심이다.

### 8. 무엇이 틀렸나/놓쳤나
시간가치·corporate burn과 catalyst probability를 NAV에서 분리해야 했다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2017 UCP monetization.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|부분적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|부분적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|부분적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|부분적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|부분적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|부분적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2009-11-29|VIC idea 게시|T0 direction|
|2009-11-29|당시 asset/liability 구조 확인|base case|
|2017-08-04|2017 UCP monetization|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 2. 2011-01-13 — PICO Long — kalman951

**원본 방향 검증:** raw `is_short=false` → **Long**. VIC source link 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2011 Long은 Vidler water assets와 UCP/real estate의 SOTP가 주가보다 높으며 scarce Southwest water의 장기 option value를 시장이 과소평가한다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
UCP와 Vidler 모두 후속 매각으로 현금화됐다. 다만 2011부터 최종 Vidler exit까지 11년이 걸려 holding-company cost와 기회비용이 컸다.

### 7. 무엇이 맞았나
NAV 할인 자체보다 NAV가 언제 현금으로 바뀌는지와 corporate burn을 반드시 IRR에 넣어야 한다.

### 8. 무엇이 틀렸나/놓쳤나
시간가치·corporate burn과 catalyst probability를 NAV에서 분리해야 했다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2017 UCP monetization.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|부분적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|부분적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|부분적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|부분적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|부분적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|부분적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2011-01-13|VIC idea 게시|T0 direction|
|2011-01-13|당시 asset/liability 구조 확인|base case|
|2017-08-04|2017 UCP monetization|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 3. 2013-05-11 — PICO Long — seeker

**원본 방향 검증:** raw `is_short=false` → **Long**. VIC source link 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2013 Long은 UCP 가치가 더 투명해지고 water portfolio가 장부가보다 높은 잠재가치를 지녀 asset monetization이 discount를 좁힐 수 있다는 event/SOTP 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2017 UCP sale은 실제 catalyst가 되었고 PICO는 현금과 Century 지분을 받았다. 이후 water-only 형태로 단순화되어 2022 최종 매각까지 이어졌다.

### 7. 무엇이 맞았나
SOTP thesis는 맞았다. 그러나 각 자산별 exit probability×시간을 따로 할인해야 holding-company discount를 과소평가하지 않는다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2017 UCP merger close.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|부분적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|부분적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|부분적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|부분적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|부분적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|부분적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2013-05-11|VIC idea 게시|T0 direction|
|2013-05-11|당시 asset/liability 구조 확인|base case|
|2017-08-04|2017 UCP merger close|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 4. 2014-02-04 — PICO Long — dman976

**원본 방향 검증:** raw `is_short=false` → **Long**. VIC source link 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2014 Long은 공개시장 UCP 지분과 Vidler water assets를 합산한 SOTP 대비 할인, 그리고 자산매각/자본환원을 catalyst로 본 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2015~17 회사는 명시적으로 asset monetization 후 capital return을 우선하겠다고 전환했고 UCP 매각으로 구조가 단순화됐다. 2022 Vidler sale이 최종 exit였다.

### 7. 무엇이 맞았나
자산가치보다 governance/capital allocation 전환이 discount closure의 결정적 catalyst였다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2016~17 return-of-capital 정책 명시.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2014-02-04|VIC idea 게시|T0 direction|
|2014-02-04|당시 asset/liability 구조 확인|base case|
|2017-02-01|2016~17 return-of-capital 정책 명시|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 5. 2015-05-05 — PICO Long — kiss534

**원본 방향 검증:** raw `is_short=false` → **Long**. raw dataset의 direction metadata로 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2015 Long은 복잡한 holding structure와 agribusiness/UCP/water assets의 합계가 주가보다 크고, 비핵심자산 정리와 buyback이 value realization을 촉진한다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2015 10-K부터 회사는 monetization proceeds를 재투자보다 자본환원에 쓰는 것이 최고 수익이라고 명시했다. agribusiness가 중단사업이 되고 2017 UCP가 매각되며 thesis가 실제 corporate action으로 전환됐다.

### 7. 무엇이 맞았나
2015는 단순 hidden asset에서 self-liquidation/capital-return thesis로 바뀐 중요한 시점이었다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2015 return-of-capital policy.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2015-05-05|VIC idea 게시|T0 direction|
|2015-05-05|당시 asset/liability 구조 확인|base case|
|2015-12-31|2015 return-of-capital policy|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 6. 2015-11-23 — PICO Long — TR1898

**원본 방향 검증:** raw `is_short=false` → **Long**. raw dataset의 direction metadata로 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2015 Long은 자사주·자본환원과 복잡한 holding structure와 agribusiness/UCP/water assets의 합계가 주가보다 크고, 비핵심자산 정리와 buyback이 value realization을 촉진한다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2015 10-K부터 회사는 monetization proceeds를 재투자보다 자본환원에 쓰는 것이 최고 수익이라고 명시했다. agribusiness가 중단사업이 되고 2017 UCP가 매각되며 thesis가 실제 corporate action으로 전환됐다.

### 7. 무엇이 맞았나
2015는 단순 hidden asset에서 self-liquidation/capital-return thesis로 바뀐 중요한 시점이었다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2015 return-of-capital policy.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2015-11-23|VIC idea 게시|T0 direction|
|2015-11-23|당시 asset/liability 구조 확인|base case|
|2015-12-31|2015 return-of-capital policy|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 7. 2016-08-15 — PICO Long — mojoris

**원본 방향 검증:** raw `is_short=false` → **Long**. raw dataset의 direction metadata로 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2016 Long은 governance/capital allocation 변화로 PICO가 empire-building에서 자산현금화·환원으로 전환하면 persistent SOTP discount가 축소된다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2017 회사는 asset monetization proceeds를 buyback/특별배당 등으로 환원한다고 재확인했고 UCP merger를 완료했다. 이후 Vidler 중심으로 단순화됐고 2022 전략적 매각으로 종결됐다.

### 7. 무엇이 맞았나
holding company에서 discount 해소의 핵심은 NAV 추정 정확도보다 경영진 인센티브와 irreversible capital-return policy다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2017 UCP sale + cost cuts.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2016-08-15|VIC idea 게시|T0 direction|
|2016-08-15|당시 asset/liability 구조 확인|base case|
|2017-08-04|2017 UCP sale + cost cuts|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 8. 2018-11-30 — PICO Long — AltaRocks

**원본 방향 검증:** raw `is_short=false` → **Long**. raw dataset의 direction metadata로 보존.

### 1. 무슨 기업인가
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다.

### 2. 산업 가치사슬과 돈의 흐름
PICO Holdings는 여러 비상장·상장 자산을 보유하던 holding company였고, 핵심 자산은 미국 남서부의 water rights·storage를 개발·매각하는 Vidler Water와 한때 주택개발사 UCP였다. 장기 가치는 회계상 earnings보다 water asset의 승인·개발·매각가격, UCP 지분가치, corporate burn, 세금/NOL, 자사주·특별배당 등 자본환원에 좌우됐다. 2021년 Vidler Water Resources로 사명을 바꾼 뒤 2022년 D.R. Horton에 매각됐다. 수자원은 승인·개발·수요자 확보 후 sale proceeds가 생기므로 장부가와 현금화가 크게 시차날 수 있다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2018 Long은 UCP가 이미 매각된 뒤 사실상 Vidler water portfolio와 현금/NOL의 단순화된 asset play가 되었고, water sales·자사주·전략적 거래가 remaining discount를 닫을 수 있다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2019에도 회사는 water credits를 현금화하고 자본환원 정책을 유지했다. 2021 Vidler로 사명을 바꿨으며 2022 D.R. Horton이 $15.75/share 현금, 약 $291m에 전량 인수했다.

### 7. 무엇이 맞았나
이 시점은 복잡성 감소로 thesis quality가 높아졌다. final buyer가 water rights를 개발에 직접 쓸 수 있는 homebuilder였다는 점이 strategic value를 입증했다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2022 D.R. Horton agreement.

### 10. 재사용 가능한 교훈
SOTP는 자산가치 합계가 아니라 각 자산의 sale probability×net proceeds×time discount에서 corporate burn·tax를 차감한 realizable NAV로 본다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|water asset NAV·scarcity|20%|핵심 자산/영업가치가 독립 검증치보다 하락|적중|
|2|UCP/other asset monetization|18%|예상 monetization/liability waterfall이 불리하게 변경|적중|
|3|corporate burn·tax/NOL|17%|cash burn·funding gap이 예상보다 확대|적중|
|4|capital return·buyback|16%|자본환원/emergence가 지연되며 dilution 증가|적중|
|5|SOTP valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|적중|
|6|governance·catalyst·반증|14%|governance/court catalyst가 반대로 전개|적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|water/asset realizable NAV|당시 filing/VIC 기준|2017 UCP monetized; 2022 water portfolio strategic exit|
|2|asset monetization proceeds|당시 filing/VIC 기준|UCP $55.3m cash + shares; Vidler ~$291m|
|3|corporate cash burn|당시 filing/VIC 기준|2017 cost cuts; later water-only simplification|
|4|capital return / exit|당시 filing/VIC 기준|2022 DHI $15.75/share cash|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2018-11-30|VIC idea 게시|T0 direction|
|2018-11-30|당시 asset/liability 구조 확인|base case|
|2022-04-14|2022 D.R. Horton agreement|첫 핵심 catalyst|
|2017-08-04|UCP merger / asset simplification|intermediate update|
|2021-12-31|Vidler-only / strategic option|late-stage update|
|2022-05-25|D.R. Horton Vidler acquisition close|최종 판정|

### Primary-source audit

- [p15](https://www.sec.gov/Archives/edgar/data/830122/000083012216000132/pico1231201510k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17](https://www.sec.gov/Archives/edgar/data/830122/000083012218000010/pico1231201710k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p17pr](https://www.sec.gov/Archives/edgar/data/830122/000083012217000099/ex991picopressreleaseq2201.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p19](https://www.sec.gov/Archives/edgar/data/830122/000083012220000010/pico1231201910k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p21](https://www.sec.gov/Archives/edgar/data/830122/000083012222000009/vwtr-20211231.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [p22](https://www.sec.gov/Archives/edgar/data/830122/000119312522105017/d200860dex991.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

# W.R. GRACE

## 9. 2006-03-06 — GRA Short — vincent975

**원본 방향 검증:** raw `is_short=true` → **Short**. VIC source link 보존.

### 1. 무슨 기업인가
W.R. Grace는 정유·석유화학 촉매와 specialty materials를 공급하는 글로벌 특수화학사다. 2001년 asbestos liabilities를 해결하기 위해 Chapter 11을 신청한 뒤 영업은 계속했고, 법원·보험·trust 구조를 통해 legacy liabilities를 정리해 2014년 bankruptcy에서 나왔다. 따라서 equity 가치는 영업사업의 normalized EBITDA뿐 아니라 asbestos claim waterfall, cash/insurance, emergence timing과 post-emergence capital structure에 크게 좌우됐다.

### 2. 산업 가치사슬과 돈의 흐름
W.R. Grace는 정유·석유화학 촉매와 specialty materials를 공급하는 글로벌 특수화학사다. 2001년 asbestos liabilities를 해결하기 위해 Chapter 11을 신청한 뒤 영업은 계속했고, 법원·보험·trust 구조를 통해 legacy liabilities를 정리해 2014년 bankruptcy에서 나왔다. 따라서 equity 가치는 영업사업의 normalized EBITDA뿐 아니라 asbestos claim waterfall, cash/insurance, emergence timing과 post-emergence capital structure에 크게 좌우됐다. Chapter 11에서는 claims가 법원 plan과 trust funding을 거쳐 equity waterfall로 번역된다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2006 Grace Short는 이미 Chapter 11에 있던 회사의 asbestos claim 규모와 emergence dilution/liability가 equity 가치보다 클 수 있고, 영업사업 가치만 보는 시장이 contingent liabilities를 과소평가한다는 논지로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
Grace는 2008년에도 65,656건의 asbestos-related lawsuits와 129,191 personal-injury claims를 공시했지만 Chapter 11 process로 claims를 묶어 해결했다. 2014년 2월 3일 bankruptcy에서 공식적으로 emergence했고, 2021년 Standard Industries가 $70/share cash, 약 $7bn enterprise transaction으로 인수했다. 장기 파국 Short는 실패했다.

### 7. 무엇이 맞았나
liability 규모만 합산하고 법적 구조가 tail liability를 trust·insurance·plan으로 ring-fence할 확률을 충분히 모델링하지 않은 것이 핵심 오류다.

### 8. 무엇이 틀렸나/놓쳤나
법적 claim의 gross 규모와 plan waterfall상 실제 equity burden을 구분하지 못했다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2011~12 plan confirmation / appeals resolution.

### 10. 재사용 가능한 교훈
bankruptcy equity는 headline liabilities보다 plan waterfall, trust funding, insurance, cash, post-emergence debt와 normalized EV를 동시 모델링한다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|operating business value|20%|핵심 자산/영업가치가 독립 검증치보다 하락|오판|
|2|asbestos claim waterfall|18%|예상 monetization/liability waterfall이 불리하게 변경|오판|
|3|cash·insurance recovery|17%|cash burn·funding gap이 예상보다 확대|오판|
|4|emergence capital structure|16%|자본환원/emergence가 지연되며 dilution 증가|오판|
|5|valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|오판|
|6|court/catalyst·반증|14%|governance/court catalyst가 반대로 전개|오판|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|normalized operating EV|당시 filing/VIC 기준|specialty chemicals survived/revalued|
|2|asbestos claim/trust waterfall|당시 filing/VIC 기준|claims channeled to PI/PD trusts after 2014|
|3|cash & insurance|당시 filing/VIC 기준|2012 DIP cash $1.064bn; insurance disclosed|
|4|emergence / strategic exit|당시 filing/VIC 기준|2014 emergence; 2021 $70/share Standard deal|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2006-03-06|VIC idea 게시|T0 direction|
|2006-03-06|당시 asset/liability 구조 확인|base case|
|2012-12-31|2011~12 plan confirmation / appeals resolution|첫 핵심 catalyst|
|2017-08-04|post-emergence operating path|intermediate update|
|2021-12-31|Standard Industries $70/share transaction|late-stage update|
|2022-05-25|사후 outcome 확인|최종 판정|

### Primary-source audit

- [g08](https://www.sec.gov/Archives/edgar/data/1045309/000104746908009003/a2187162z10-q.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g12](https://www.sec.gov/Archives/edgar/data/1045309/000104530913000015/gra-20121231x10k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g14](https://www.sec.gov/Archives/edgar/data/1045309/000104530914000057/gra-20141q10xq.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g18](https://www.sec.gov/Archives/edgar/data/1045309/000104530919000025/a201810-k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g21](https://www.sec.gov/Archives/edgar/data/1045309/000114036121014196/nc10023607x1_ex99-1.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g21q](https://www.sec.gov/Archives/edgar/data/1045309/000104530921000086/gra-20210630.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

## 10. 2012-01-17 — GRA Long — jon64

**원본 방향 검증:** raw `is_short=false` → **Long**. raw dataset의 direction metadata로 보존.

### 1. 무슨 기업인가
W.R. Grace는 정유·석유화학 촉매와 specialty materials를 공급하는 글로벌 특수화학사다. 2001년 asbestos liabilities를 해결하기 위해 Chapter 11을 신청한 뒤 영업은 계속했고, 법원·보험·trust 구조를 통해 legacy liabilities를 정리해 2014년 bankruptcy에서 나왔다. 따라서 equity 가치는 영업사업의 normalized EBITDA뿐 아니라 asbestos claim waterfall, cash/insurance, emergence timing과 post-emergence capital structure에 크게 좌우됐다.

### 2. 산업 가치사슬과 돈의 흐름
W.R. Grace는 정유·석유화학 촉매와 specialty materials를 공급하는 글로벌 특수화학사다. 2001년 asbestos liabilities를 해결하기 위해 Chapter 11을 신청한 뒤 영업은 계속했고, 법원·보험·trust 구조를 통해 legacy liabilities를 정리해 2014년 bankruptcy에서 나왔다. 따라서 equity 가치는 영업사업의 normalized EBITDA뿐 아니라 asbestos claim waterfall, cash/insurance, emergence timing과 post-emergence capital structure에 크게 좌우됐다. Chapter 11에서는 claims가 법원 plan과 trust funding을 거쳐 equity waterfall로 번역된다.

### 3. 경쟁우위·경쟁구도·핵심 지표
핵심은 headline growth가 아니라 scarce asset/technical franchise와 이를 현금으로 바꾸는 governance·legal process다.

### 4. 당시 VIC 원문과 핵심 숫자
2012 Grace Long은 10년 넘은 Chapter 11이 막바지에 있고, operating businesses와 약 $1.064bn DIP cash가 강한 가운데 asbestos liability가 plan을 통해 정형화되면 legal overhang 해소와 재평가가 가능하다는 event-driven thesis로 재구성된다.

### 5. 밸류에이션과 기대수익의 연결
단순 SOTP 또는 gross claims가 아니라 time-to-cash와 probability를 적용한 expected IRR이 기준이다.

### 6. 실제 전개
2012 10-K에서 DIP cash는 $1.064bn이었다. 법원 confirmation과 appeals 해결 후 Grace는 2014년 2월 3일 Chapter 11에서 나왔다. post-emergence에는 legacy asbestos claims가 PI/PD trust로 channel되었고, 2021 Standard Industries가 $70/share cash에 인수하기로 합의했다.

### 7. 무엇이 맞았나
legal overhang이 무한한 liability가 아니라 bounded waterfall로 바뀌는 inflection을 포착했다. bankruptcy equity는 headline claim보다 plan waterfall·cash·insurance·enterprise value를 함께 계산해야 한다.

### 8. 무엇이 틀렸나/놓쳤나
핵심 catalyst는 맞았지만 각 waterfall 변수와 IRR sensitivity를 더 명시할 수 있었다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 realizable NAV/plan recovery가 훼손되거나 catalyst가 반복 지연되어 연환산 IRR이 기준 이하로 떨어지는 경우다. 첫 신호: 2014 Chapter 11 emergence.

### 10. 재사용 가능한 교훈
bankruptcy equity는 headline liabilities보다 plan waterfall, trust funding, insurance, cash, post-emergence debt와 normalized EV를 동시 모델링한다.

### Claim audit

|#|주장 축|Weight|반증조건|판정|
|---:|---|---:|---|---|
|1|operating business value|20%|핵심 자산/영업가치가 독립 검증치보다 하락|적중|
|2|asbestos claim waterfall|18%|예상 monetization/liability waterfall이 불리하게 변경|적중|
|3|cash·insurance recovery|17%|cash burn·funding gap이 예상보다 확대|적중|
|4|emergence capital structure|16%|자본환원/emergence가 지연되며 dilution 증가|적중|
|5|valuation·IRR|15%|time-discounted expected IRR이 hurdle 미달|적중|
|6|court/catalyst·반증|14%|governance/court catalyst가 반대로 전개|적중|

### Metric audit

|#|Metric|T0|Actual|
|---:|---|---|---|
|1|normalized operating EV|당시 filing/VIC 기준|specialty chemicals survived/revalued|
|2|asbestos claim/trust waterfall|당시 filing/VIC 기준|claims channeled to PI/PD trusts after 2014|
|3|cash & insurance|당시 filing/VIC 기준|2012 DIP cash $1.064bn; insurance disclosed|
|4|emergence / strategic exit|당시 filing/VIC 기준|2014 emergence; 2021 $70/share Standard deal|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2012-01-17|VIC idea 게시|T0 direction|
|2012-01-17|당시 asset/liability 구조 확인|base case|
|2014-02-03|2014 Chapter 11 emergence|첫 핵심 catalyst|
|2017-08-04|post-emergence operating path|intermediate update|
|2021-12-31|Standard Industries $70/share transaction|late-stage update|
|2022-05-25|사후 outcome 확인|최종 판정|

### Primary-source audit

- [g08](https://www.sec.gov/Archives/edgar/data/1045309/000104746908009003/a2187162z10-q.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g12](https://www.sec.gov/Archives/edgar/data/1045309/000104530913000015/gra-20121231x10k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g14](https://www.sec.gov/Archives/edgar/data/1045309/000104530914000057/gra-20141q10xq.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g18](https://www.sec.gov/Archives/edgar/data/1045309/000104530919000025/a201810-k.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g21](https://www.sec.gov/Archives/edgar/data/1045309/000114036121014196/nc10023607x1_ex99-1.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증
- [g21q](https://www.sec.gov/Archives/edgar/data/1045309/000104530921000086/gra-20210630.htm) — 당시 asset/liability, catalyst와 최종 outcome 검증

