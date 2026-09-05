# Batch 034 — CRK ticker collision: Comstock Resources / Crocodile Gold + Franklin Covey

> 범위: 10 ideas. raw DB의 CRK / Crocodile Gold 8건은 실제로 NYSE Comstock Resources와 TSX Crocodile Gold가 뒤섞인 entity 오류였다. VIC source URL·날짜·동시기 corporate event로 idea별 법인을 다시 식별했다. raw ticker와 is_short는 audit용으로 보존하되 curated company_name은 실제 법인으로 교정한다.

> 중요: 비로그인 VIC에서 전체 본문이 노출되지 않는 과거 글은 직접인용하지 않는다. 아래 원 논지는 raw metadata, 공개 VIC header, 동시기 SEC/기업 1차자료에 기반한 구조적 재구성이다. 원문이 없어서 payoff까지 확정할 수 없는 2011-12 Crocodile Gold raw Short는 성공/실패를 강제로 부여하지 않고 판정 제한으로 표시한다.

## 검증 요약

- Ideas: 10 = Comstock Resources 5 + Crocodile Gold 3 + Franklin Covey 2
- Sections: 100
- Weighted claims: 60 — idea별 100%
- Metrics: 40
- Timeline items: 60
- Sources: 60

## 데이터 품질 발견 — ticker는 entity key가 아니다

CRK는 서로 다른 시기·거래소에서 Comstock Resources와 Crocodile Gold가 사용했다. 기존 raw ETL은 ticker를 회사명에 단순 매핑하면서 Comstock 아이디어까지 Crocodile Gold로 오염시켰다. 앞으로 동일 ticker라도 source URL의 issuer name, exchange, date, CIK/SEDAR issuer, corporate event를 함께 써서 entity를 해소해야 한다. 이 오류를 고치지 않으면 기업별 사후분석과 성공/실패 패턴이 서로 다른 사업을 한 회사로 합치는 치명적 오류가 된다.

## 배치 공통 프레임

세 회사는 업종은 다르지만 공통점이 있다. headline metric이 equity cash flow와 다르다. Comstock의 reserve/production은 가스가격·decline·CapEx·debt를 거쳐야 하고, Crocodile의 ounces/resources는 grade·recovery·AISC·royalty·financing을 거쳐야 하며, Franklin Covey의 브랜드·매출은 legacy retail drag를 제거한 뒤 recurring training/subscription economics로 봐야 한다. 따라서 valuation은 단순 multiple보다 cash-flow waterfall과 경로의 확률을 먼저 모델링한다.

# COMSTOCK RESOURCES INC — NYSE CRK

## 1. 2004-12-08 — CRK Short — hao777

Entity / 방향 검증: curated company = COMSTOCK RESOURCES INC · raw direction = Short · raw is_short=true. VIC source link로 issuer를 직접 확인.

### 1. 무슨 기업인가
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다.

### 2. 산업 가치사슬과 돈의 흐름
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
경쟁우위는 low-cost Haynesville inventory와 Gulf Coast 접근성이지만 gas price·capital intensity가 이를 압도할 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자
2004 Comstock Short는 높은 commodity sensitivity와 인수·개발 중심 자본배분이 자산가치보다 부채를 빠르게 늘릴 수 있으며, reserve/NAV가 commodity price와 capital intensity를 충분히 반영하지 못한다는 논지로 재구성한다. raw source는 ticker CRK의 재사용 때문에 company_name을 Crocodile Gold로 잘못 매핑했다. VIC source/event/date를 기준으로 Comstock Resources로 교정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
2004년 중반 장기부채는 약 $324m였다. 회사는 이후 수차례 shale 개발·인수 사이클을 거치며 존속했고, 2018 Jones recapitalization과 2019 Covey Park 인수로 사실상 다른 규모·지배구조의 Haynesville gas producer가 됐다. 2026년에도 Haynesville 중심으로 운영 중이다.

### 7. 무엇이 맞았나
E&P의 NAV/레버리지 취약성 진단은 타당했지만 terminal failure로 이어지지 않았다. 자산·스폰서·자본구조가 계속 재편되므로 오래된 Short를 동일 법인의 정적 balance-sheet thesis로 유지하면 안 된다.

### 8. 무엇이 틀렸나/놓쳤나
commodity price path와 sponsor/refinancing optionality를 static leverage/NAV보다 작게 본 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: 부채보다 생산자산·자본조달 경로가 확대 (2008-12-31).

### 10. 재사용 가능한 교훈
E&P는 reserve/NAV를 그대로 equity value로 두지 않고, strip price별 well-level FCF에서 maintenance/growth CapEx와 순부채를 연결한다. sponsor capital·M&A·hedge는 별도 path 변수로 둔다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|commodity price·hedge|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|부분적중|
|2|well EUR·decline·unit cost|18%|unit economics 또는 asset quality가 예상보다 강함|부분적중|
|3|drilling CapEx·FCF|17%|FCF가 capital intensity를 흡수하며 개선|부분적중|
|4|debt·refinancing|16%|debt/refinancing runway가 충분히 연장|부분적중|
|5|asset/M&A·sponsor capital|15%|M&A/sponsor/segment-sale optionality가 실현|부분적중|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|부분적중|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|2004 debt ≈$324m|
|2|capital structure/catalyst|당시 공시/VIC 기준|2018 Jones 84% control|
|3|후속 operating outcome|당시 공시/VIC 기준|2019 Covey Park $2.2bn|
|4|최종/current outcome|당시 공시/VIC 기준|2026 Haynesville focus|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2004-12-08|VIC idea 게시|T0|
|2008-12-31|부채보다 생산자산·자본조달 경로가 확대|첫 핵심 반증/확인 신호|
|2018-08-14|Jones contribution/refinancing|자본구조 regime shift|
|2019-07-16|Covey Park acquisition close|Haynesville scale 확대|
|2022-12-31|record FCF/deleveraging year|commodity upside 확인|
|2026-06-30|Q2 2026 Haynesville update|현재 사업 지속|

### Primary-source audit

- [VIC 2019 CRK page](https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800) — VIC 메타데이터·당시 가격/시총/순부채/Short 표시 확인
- [SEC 2004 10-Q](https://www.sec.gov/Archives/edgar/data/23194/000095013404011584/d16950e10vq.htm) — 2004 debt 및 자본구조 확인
- [SEC 2018 Jones contribution](https://www.sec.gov/Archives/edgar/data/23194/000119312518217312/d490208dex99a1i.htm) — Bakken 자산 $620m, 최대 88.57m주·지배권 구조 확인
- [Comstock Covey Park announcement](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-become-haynesville-basin-leader-acquisition) — 2019 $2.2bn Covey Park, Jones $475m 추가 투자, 2,000 locations 확인
- [Comstock FY2022 results](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-inc-reports-fourth-quarter-2022-financial-and) — 2022 $673m FCF, $506m debt retirement, gas-cycle upside 확인
- [SEC Q2 2026 results](https://www.sec.gov/Archives/edgar/data/23194/000119312526323767/crk-ex99_1.htm) — 2026 Haynesville 집중·생산/현금흐름 최신 상태 확인

## 2. 2010-07-15 — CRK Short — nantembo629

Entity / 방향 검증: curated company = COMSTOCK RESOURCES INC · raw direction = Short · raw is_short=true. VIC source link로 issuer를 직접 확인.

### 1. 무슨 기업인가
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다.

### 2. 산업 가치사슬과 돈의 흐름
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
경쟁우위는 low-cost Haynesville inventory와 Gulf Coast 접근성이지만 gas price·capital intensity가 이를 압도할 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자
2010 Comstock Short는 Haynesville 개발이 높은 decline과 지속 CapEx를 요구해 headline reserve growth가 equity FCF로 연결되지 않고, 약한 가스가격에서 레버리지와 negative FCF가 동시에 악화될 수 있다는 논지로 재구성한다. raw source는 ticker CRK의 재사용 때문에 company_name을 Crocodile Gold로 잘못 매핑했다. VIC source/event/date를 기준으로 Comstock Resources로 교정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
2010년 VIC 페이지 기준 주가는 $27.50, 약 47m주, 시총 약 $1.3bn, 순부채 약 $340m로 확인되는 사례다. 2011 Delaware Basin 인수 등 자본집약적 확장이 이어졌고 가스 약세는 실제 재무압력을 키웠다. 그러나 2018 대규모 sponsor recapitalization이 생존경로를 바꿨다.

### 7. 무엇이 맞았나
well decline·CapEx·gas price를 연결한 Short 프레임은 옳았지만 equity outcome은 sponsor capital과 자산재편에 크게 좌우됐다. credit/liquidity runway를 별도 확률변수로 둬야 했다.

### 8. 무엇이 틀렸나/놓쳤나
commodity price path와 sponsor/refinancing optionality를 static leverage/NAV보다 작게 본 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: 2011 인수로 projected leverage·CapEx 상승 (2011-12-05).

### 10. 재사용 가능한 교훈
E&P는 reserve/NAV를 그대로 equity value로 두지 않고, strip price별 well-level FCF에서 maintenance/growth CapEx와 순부채를 연결한다. sponsor capital·M&A·hedge는 별도 path 변수로 둔다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|commodity price·hedge|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|부분적중|
|2|well EUR·decline·unit cost|18%|unit economics 또는 asset quality가 예상보다 강함|부분적중|
|3|drilling CapEx·FCF|17%|FCF가 capital intensity를 흡수하며 개선|부분적중|
|4|debt·refinancing|16%|debt/refinancing runway가 충분히 연장|부분적중|
|5|asset/M&A·sponsor capital|15%|M&A/sponsor/segment-sale optionality가 실현|부분적중|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|부분적중|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|2010 price $27.50|
|2|capital structure/catalyst|당시 공시/VIC 기준|2010 net debt ≈$340m|
|3|후속 operating outcome|당시 공시/VIC 기준|2011 Delaware deal ≈$333m|
|4|최종/current outcome|당시 공시/VIC 기준|2018 sponsor recap|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2010-07-15|VIC idea 게시|T0|
|2011-12-05|2011 인수로 projected leverage·CapEx 상승|첫 핵심 반증/확인 신호|
|2018-08-14|Jones contribution/refinancing|자본구조 regime shift|
|2019-07-16|Covey Park acquisition close|Haynesville scale 확대|
|2022-12-31|record FCF/deleveraging year|commodity upside 확인|
|2026-06-30|Q2 2026 Haynesville update|현재 사업 지속|

### Primary-source audit

- [VIC 2019 CRK page](https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800) — VIC 메타데이터·당시 가격/시총/순부채/Short 표시 확인
- [SEC 2004 10-Q](https://www.sec.gov/Archives/edgar/data/23194/000095013404011584/d16950e10vq.htm) — 2004 debt 및 자본구조 확인
- [SEC 2018 Jones contribution](https://www.sec.gov/Archives/edgar/data/23194/000119312518217312/d490208dex99a1i.htm) — Bakken 자산 $620m, 최대 88.57m주·지배권 구조 확인
- [Comstock Covey Park announcement](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-become-haynesville-basin-leader-acquisition) — 2019 $2.2bn Covey Park, Jones $475m 추가 투자, 2,000 locations 확인
- [Comstock FY2022 results](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-inc-reports-fourth-quarter-2022-financial-and) — 2022 $673m FCF, $506m debt retirement, gas-cycle upside 확인
- [SEC Q2 2026 results](https://www.sec.gov/Archives/edgar/data/23194/000119312526323767/crk-ex99_1.htm) — 2026 Haynesville 집중·생산/현금흐름 최신 상태 확인

## 6. 2018-02-02 — CRK Short — Woolly18

Entity / 방향 검증: curated company = COMSTOCK RESOURCES INC · raw direction = Short · raw is_short=true. VIC source link로 issuer를 직접 확인.

### 1. 무슨 기업인가
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다.

### 2. 산업 가치사슬과 돈의 흐름
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
경쟁우위는 low-cost Haynesville inventory와 Gulf Coast 접근성이지만 gas price·capital intensity가 이를 압도할 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자
2018 Comstock Short는 높은 부채와 drilling cash burn을 가진 E&P에서 asset sale·refinancing만으로 common equity가 보전되기 어렵고, 구조조정 또는 대규모 dilution 위험이 크다는 event/capital-structure 논지로 재구성한다. raw source는 ticker CRK의 재사용 때문에 company_name을 Crocodile Gold로 잘못 매핑했다. VIC source/event/date를 기준으로 Comstock Resources로 교정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
불과 몇 달 뒤 Jerry Jones 계열은 약 $620m로 평가된 Bakken 자산을 출자하고 최대 88.57m 신주를 받아 pro forma 약 84.5%를 보유하는 거래에 합의했다. 8월 거래·refinancing이 닫히면서 기존 equity는 희석됐지만 동시에 유동성과 생존경로가 크게 개선됐다.

### 7. 무엇이 맞았나
희석·자본구조 리스크는 정확했으나 sponsor recapitalization이 distress를 equity extinction이 아니라 control transfer로 바꿨다. distressed E&P Short는 신규 외부자본의 option value를 반드시 모델링해야 한다.

### 8. 무엇이 틀렸나/놓쳤나
commodity price path와 sponsor/refinancing optionality를 static leverage/NAV보다 작게 본 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: Jones contribution agreement (2018-05-09).

### 10. 재사용 가능한 교훈
E&P는 reserve/NAV를 그대로 equity value로 두지 않고, strip price별 well-level FCF에서 maintenance/growth CapEx와 순부채를 연결한다. sponsor capital·M&A·hedge는 별도 path 변수로 둔다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|commodity price·hedge|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|부분적중|
|2|well EUR·decline·unit cost|18%|unit economics 또는 asset quality가 예상보다 강함|부분적중|
|3|drilling CapEx·FCF|17%|FCF가 capital intensity를 흡수하며 개선|부분적중|
|4|debt·refinancing|16%|debt/refinancing runway가 충분히 연장|부분적중|
|5|asset/M&A·sponsor capital|15%|M&A/sponsor/segment-sale optionality가 실현|부분적중|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|부분적중|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|Bakken value $620m|
|2|capital structure/catalyst|당시 공시/VIC 기준|new shares up to 88.57m|
|3|후속 operating outcome|당시 공시/VIC 기준|pro forma control 84.5%|
|4|최종/current outcome|당시 공시/VIC 기준|2018 new notes $850m|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2018-02-02|VIC idea 게시|T0|
|2018-05-09|Jones contribution agreement|첫 핵심 반증/확인 신호|
|2018-08-14|Jones contribution/refinancing|자본구조 regime shift|
|2019-07-16|Covey Park acquisition close|Haynesville scale 확대|
|2022-12-31|record FCF/deleveraging year|commodity upside 확인|
|2026-06-30|Q2 2026 Haynesville update|현재 사업 지속|

### Primary-source audit

- [VIC 2019 CRK page](https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800) — VIC 메타데이터·당시 가격/시총/순부채/Short 표시 확인
- [SEC 2004 10-Q](https://www.sec.gov/Archives/edgar/data/23194/000095013404011584/d16950e10vq.htm) — 2004 debt 및 자본구조 확인
- [SEC 2018 Jones contribution](https://www.sec.gov/Archives/edgar/data/23194/000119312518217312/d490208dex99a1i.htm) — Bakken 자산 $620m, 최대 88.57m주·지배권 구조 확인
- [Comstock Covey Park announcement](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-become-haynesville-basin-leader-acquisition) — 2019 $2.2bn Covey Park, Jones $475m 추가 투자, 2,000 locations 확인
- [Comstock FY2022 results](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-inc-reports-fourth-quarter-2022-financial-and) — 2022 $673m FCF, $506m debt retirement, gas-cycle upside 확인
- [SEC Q2 2026 results](https://www.sec.gov/Archives/edgar/data/23194/000119312526323767/crk-ex99_1.htm) — 2026 Haynesville 집중·생산/현금흐름 최신 상태 확인

## 7. 2019-09-18 — CRK Short — abcd1234

Entity / 방향 검증: curated company = COMSTOCK RESOURCES INC · raw direction = Short · raw is_short=true. VIC source link로 issuer를 직접 확인.

### 1. 무슨 기업인가
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다.

### 2. 산업 가치사슬과 돈의 흐름
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
경쟁우위는 low-cost Haynesville inventory와 Gulf Coast 접근성이지만 gas price·capital intensity가 이를 압도할 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자
2019 Comstock Short는 Covey Park 인수 후 약 $5.3bn TEV와 $2.73bn 순부채, 50%+ borrow cost가 보여주듯 leverage·control concentration·preferred dilution이 큰데 시장이 Haynesville scale synergy와 gas economics를 과대평가한다는 논지다. raw source는 ticker CRK의 재사용 때문에 company_name을 Crocodile Gold로 잘못 매핑했다. VIC source/event/date를 기준으로 Comstock Resources로 교정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
VIC 페이지는 $9.35, 시총 $2.627bn, 순부채 $2.732bn, TEV $5.332bn을 기록한다. 실제 Covey Park deal은 약 $2.2bn이었고 Jones는 $475m를 추가 투자했다. 이후 2021~22 gas price 급등으로 FCF가 폭발해 2022 FCF $673m, debt retirement $506m을 기록했다.

### 7. 무엇이 맞았나
leverage와 preferred/지배구조 위험은 실재했지만 commodity upside의 convexity를 놓쳤다. 높은 부채는 downside만 키우는 게 아니라 gas price 상승 시 equity beta도 폭발적으로 키웠다.

### 8. 무엇이 틀렸나/놓쳤나
commodity price path와 sponsor/refinancing optionality를 static leverage/NAV보다 작게 본 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: 2021 gas rally와 FCF inflection (2021-06-30).

### 10. 재사용 가능한 교훈
E&P는 reserve/NAV를 그대로 equity value로 두지 않고, strip price별 well-level FCF에서 maintenance/growth CapEx와 순부채를 연결한다. sponsor capital·M&A·hedge는 별도 path 변수로 둔다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|commodity price·hedge|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|적중|
|2|well EUR·decline·unit cost|18%|unit economics 또는 asset quality가 예상보다 강함|적중|
|3|drilling CapEx·FCF|17%|FCF가 capital intensity를 흡수하며 개선|적중|
|4|debt·refinancing|16%|debt/refinancing runway가 충분히 연장|오판|
|5|asset/M&A·sponsor capital|15%|M&A/sponsor/segment-sale optionality가 실현|오판|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|오판|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|VIC TEV $5.332bn|
|2|capital structure/catalyst|당시 공시/VIC 기준|VIC net debt $2.732bn|
|3|후속 operating outcome|당시 공시/VIC 기준|2019 deal $2.2bn|
|4|최종/current outcome|당시 공시/VIC 기준|2022 FCF $673m|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2019-09-18|VIC idea 게시|T0|
|2021-06-30|2021 gas rally와 FCF inflection|첫 핵심 반증/확인 신호|
|2018-08-14|Jones contribution/refinancing|자본구조 regime shift|
|2019-07-16|Covey Park acquisition close|Haynesville scale 확대|
|2022-12-31|record FCF/deleveraging year|commodity upside 확인|
|2026-06-30|Q2 2026 Haynesville update|현재 사업 지속|

### Primary-source audit

- [VIC 2019 CRK page](https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800) — VIC 메타데이터·당시 가격/시총/순부채/Short 표시 확인
- [SEC 2004 10-Q](https://www.sec.gov/Archives/edgar/data/23194/000095013404011584/d16950e10vq.htm) — 2004 debt 및 자본구조 확인
- [SEC 2018 Jones contribution](https://www.sec.gov/Archives/edgar/data/23194/000119312518217312/d490208dex99a1i.htm) — Bakken 자산 $620m, 최대 88.57m주·지배권 구조 확인
- [Comstock Covey Park announcement](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-become-haynesville-basin-leader-acquisition) — 2019 $2.2bn Covey Park, Jones $475m 추가 투자, 2,000 locations 확인
- [Comstock FY2022 results](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-inc-reports-fourth-quarter-2022-financial-and) — 2022 $673m FCF, $506m debt retirement, gas-cycle upside 확인
- [SEC Q2 2026 results](https://www.sec.gov/Archives/edgar/data/23194/000119312526323767/crk-ex99_1.htm) — 2026 Haynesville 집중·생산/현금흐름 최신 상태 확인

## 8. 2021-09-09 — CRK Short — beep899

Entity / 방향 검증: curated company = COMSTOCK RESOURCES INC · raw direction = Short · raw is_short=true. VIC source link로 issuer를 직접 확인.

### 1. 무슨 기업인가
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다.

### 2. 산업 가치사슬과 돈의 흐름
Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
경쟁우위는 low-cost Haynesville inventory와 Gulf Coast 접근성이지만 gas price·capital intensity가 이를 압도할 수 있다.

### 4. 당시 VIC 원문과 핵심 숫자
2021 Comstock Short는 주가 $7.65, 시총 약 $2.075bn 대비 순부채 약 $2.934bn인 고레버리지 gas producer에서 hedges·개발비·가스가격 정상화를 감안하면 당시 기대 FCF가 지속되기 어렵다는 논지로 재구성한다. raw source는 ticker CRK의 재사용 때문에 company_name을 Crocodile Gold로 잘못 매핑했다. VIC source/event/date를 기준으로 Comstock Resources로 교정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
2021 회사는 FCF $262m과 Q4 debt paydown $190m을 냈고, 2022에는 gas 가격 급등으로 FCF $673m, $506m debt retirement, 배당 재개까지 갔다. 이후 2023 가스가격 약세로 실현가격이 크게 내려가고 현금창출이 다시 둔화해 원래의 cyclicality 경고는 뒤늦게 나타났다. 2026년에도 회사는 Haynesville 개발을 지속한다.

### 7. 무엇이 맞았나
cycle-normalization 리스크는 맞았으나 12개월 horizon에서 2022 gas spike를 견디지 못한 타이밍 오류다. commodity Short는 장기 평균가격보다 hedge book·storage/LNG·supply response가 만드는 path를 먼저 모델링해야 한다.

### 8. 무엇이 틀렸나/놓쳤나
commodity price path와 sponsor/refinancing optionality를 static leverage/NAV보다 작게 본 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: 2022 record FCF/deleveraging (2022-12-31).

### 10. 재사용 가능한 교훈
E&P는 reserve/NAV를 그대로 equity value로 두지 않고, strip price별 well-level FCF에서 maintenance/growth CapEx와 순부채를 연결한다. sponsor capital·M&A·hedge는 별도 path 변수로 둔다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|commodity price·hedge|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|부분적중|
|2|well EUR·decline·unit cost|18%|unit economics 또는 asset quality가 예상보다 강함|부분적중|
|3|drilling CapEx·FCF|17%|FCF가 capital intensity를 흡수하며 개선|부분적중|
|4|debt·refinancing|16%|debt/refinancing runway가 충분히 연장|오판|
|5|asset/M&A·sponsor capital|15%|M&A/sponsor/segment-sale optionality가 실현|오판|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|오판|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|VIC price $7.65|
|2|capital structure/catalyst|당시 공시/VIC 기준|VIC net debt $2.934bn|
|3|후속 operating outcome|당시 공시/VIC 기준|2022 FCF $673m|
|4|최종/current outcome|당시 공시/VIC 기준|2023 avg gas $2.40/Mcf|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2021-09-09|VIC idea 게시|T0|
|2022-12-31|2022 record FCF/deleveraging|첫 핵심 반증/확인 신호|
|2018-08-14|Jones contribution/refinancing|자본구조 regime shift|
|2019-07-16|Covey Park acquisition close|Haynesville scale 확대|
|2022-12-31|record FCF/deleveraging year|commodity upside 확인|
|2026-06-30|Q2 2026 Haynesville update|현재 사업 지속|

### Primary-source audit

- [VIC 2019 CRK page](https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800) — VIC 메타데이터·당시 가격/시총/순부채/Short 표시 확인
- [SEC 2004 10-Q](https://www.sec.gov/Archives/edgar/data/23194/000095013404011584/d16950e10vq.htm) — 2004 debt 및 자본구조 확인
- [SEC 2018 Jones contribution](https://www.sec.gov/Archives/edgar/data/23194/000119312518217312/d490208dex99a1i.htm) — Bakken 자산 $620m, 최대 88.57m주·지배권 구조 확인
- [Comstock Covey Park announcement](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-become-haynesville-basin-leader-acquisition) — 2019 $2.2bn Covey Park, Jones $475m 추가 투자, 2,000 locations 확인
- [Comstock FY2022 results](https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-inc-reports-fourth-quarter-2022-financial-and) — 2022 $673m FCF, $506m debt retirement, gas-cycle upside 확인
- [SEC Q2 2026 results](https://www.sec.gov/Archives/edgar/data/23194/000119312526323767/crk-ex99_1.htm) — 2026 Haynesville 집중·생산/현금흐름 최신 상태 확인

# CROCODILE GOLD CORP — TSX CRK

## 3. 2011-01-12 — CRK Long — lys615

Entity / 방향 검증: curated company = CROCODILE GOLD CORP · raw direction = Long · raw is_short=false. VIC source link로 issuer를 직접 확인.

### 1. 무슨 기업인가
Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다.

### 2. 산업 가치사슬과 돈의 흐름
Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
광산의 경쟁력은 고정된 브랜드가 아니라 orebody quality·운영실행·자금조달 조건에 의해 바뀐다.

### 4. 당시 VIC 원문과 핵심 숫자
2011 Crocodile Gold Long은 호주 금광 포트폴리오의 생산 ramp와 금가격 환경이 개선되면 고정비 흡수와 mine cash flow가 빠르게 좋아지고, 당시 낮은 valuation이 재평가될 수 있다는 turnaround/asset-optionality 논지로 재구성한다. raw CRK는 TSX Crocodile Gold를 뜻한다. 동일 ticker의 NYSE Comstock Resources와 분리해 entity를 확정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
2011 운영경로는 매끄럽지 않았고 같은 해 12월 최대주주 Luxor가 C$0.56 현금 공개매수를 제안했다. 2012에는 Fosterville·Stawell을 최대 C$105m 조건으로 인수해 사업구조가 크게 변했고, 2015 Newmarket Gold와 합병됐다.

### 7. 무엇이 맞았나
광산자산 optionality와 M&A value는 실제로 존재했지만 standalone mine execution만으로 복리화된 사례가 아니다. financing·대주주 지배·deal waterfall이 thesis의 절반 이상이었다.

### 8. 무엇이 틀렸나/놓쳤나
운영자산 가치와 financing·royalty·M&A waterfall의 상호작용을 충분히 분리하지 못한 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: Luxor C$0.56 공개매수 제안 (2011-12-13).

### 10. 재사용 가능한 교훈
광산주는 resource ounce보다 grade×recovery×mine life×AISC×sustaining capital의 현금흐름을 먼저 보고, 대주주 financing·royalty·partial tender·merger consideration을 equity waterfall에 얹는다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|grade·recovery·production|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|부분적중|
|2|cash cost·sustaining CapEx|18%|unit economics 또는 asset quality가 예상보다 강함|부분적중|
|3|liquidity·financing|17%|FCF가 capital intensity를 흡수하며 개선|부분적중|
|4|Luxor/governance|16%|debt/refinancing runway가 충분히 연장|부분적중|
|5|M&A·royalty waterfall|15%|M&A/sponsor/segment-sale optionality가 실현|부분적중|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|부분적중|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|Luxor bid C$0.56|
|2|capital structure/catalyst|당시 공시/VIC 기준|bid premium ≈60%|
|3|후속 operating outcome|당시 공시/VIC 기준|2012 asset deal up to C$105m|
|4|최종/current outcome|당시 공시/VIC 기준|2015 merger cash option C$0.37|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2011-01-12|VIC idea 게시|T0|
|2011-12-13|Luxor C$0.56 공개매수 제안|첫 핵심 반증/확인 신호|
|2011-12-23|Luxor formal partial offer|지배구조 이벤트|
|2012-05-04|Fosterville/Stawell acquisition|자산구조 변화|
|2015-01-14|AuRico FCF sharing termination close|waterfall 단순화|
|2015-07-10|Newmarket combination complete|독립 상장 종료|

### Primary-source audit

- [VIC Crocodile Gold 2011](https://www.valueinvestorsclub.com/idea/CROCODILE_GOLD_CORP/0373325138) — 2011 Long의 entity·날짜 확인
- [Luxor bid announcement](https://www.prnewswire.com/news-releases/luxor-capital-announces-premium-offer-to-purchase-common-shares-of-crocodile-gold-135545133.html) — 2011 C$0.56 bid·약 60% premium·85% 목표 확인
- [Luxor formal offer](https://www.prnewswire.com/news-releases/luxor-commences-offer-to-acquire-common-shares-of-crocodile-gold-for-056-per-share-in-cash-136135378.html) — 2011-12-23 formal offer 확인
- [SEC AuRico/Crocodile acquisition](https://www.sec.gov/Archives/edgar/data/1078217/000120445912000644/exhibit99-1.htm) — 2012 Fosterville·Stawell 최대 C$105m 인수조건 확인
- [SEC AuRico 2014 royalty amendment](https://www.sec.gov/Archives/edgar/data/1078217/000106299315000967/exhibit99-3.htm) — 2014 C$20m + 2%/1% NSR로 FCF sharing 종료 확인
- [SEC Newmarket/Crocodile arrangement](https://www.sec.gov/Archives/edgar/data/1713443/000106299317003535/exhibit99-87.htm) — 2015 합병·C$0.37 cash/주식 선택·최종 corporate outcome 확인

## 4. 2011-12-15 — CRK Short — john771

Entity / 방향 검증: curated company = CROCODILE GOLD CORP · raw direction = Short · raw is_short=true. 원문 source link 부재로 동시기 event/metadata까지 교차검증.

### 1. 무슨 기업인가
Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다.

### 2. 산업 가치사슬과 돈의 흐름
Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
광산의 경쟁력은 고정된 브랜드가 아니라 orebody quality·운영실행·자금조달 조건에 의해 바뀐다.

### 4. 당시 VIC 원문과 핵심 숫자
2011-12 Crocodile Gold raw Short는 Luxor의 C$0.56 부분공개매수가 전체 주주에게 동일한 확정가치를 보장하지 않으며, 조건·proration·지배권 집중 뒤 minority stub의 가격이 다시 운영가치로 수렴할 수 있다는 event-driven Short로 구조적으로 재구성한다. 원문 본문 미확보로 세부 논지는 확정하지 않는다. raw CRK는 TSX Crocodile Gold를 뜻한다. 동일 ticker의 NYSE Comstock Resources와 분리해 entity를 확정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
Luxor는 12월 13일 최대 215.4m주를 C$0.56에 사서 기존 지분과 합쳐 약 85%를 목표로 한다고 발표했고 12월 23일 formal offer를 개시했다. 회사는 이후 독립 상장사로 계속 운영했고 2012 대형 광산 인수, 2015 Newmarket 합병으로 경로가 다시 바뀌었다.

### 7. 무엇이 맞았나
부분공개매수의 proration/stub-risk라는 구조적 포인트는 중요하지만, 원문이 없어 이 raw Short의 정확한 payoff와 entry를 재현할 수 없다. 방향성 성공/실패를 억지로 단정하지 않고 판정 제한으로 둔다.

### 8. 무엇이 틀렸나/놓쳤나
원문 미확보 때문에 payoff 정의까지 복원할 수 없어 success/failure 단정이 불가능하다.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: formal partial tender 개시 (2011-12-23).

### 10. 재사용 가능한 교훈
광산주는 resource ounce보다 grade×recovery×mine life×AISC×sustaining capital의 현금흐름을 먼저 보고, 대주주 financing·royalty·partial tender·merger consideration을 equity waterfall에 얹는다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|grade·recovery·production|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|판정 제한|
|2|cash cost·sustaining CapEx|18%|unit economics 또는 asset quality가 예상보다 강함|판정 제한|
|3|liquidity·financing|17%|FCF가 capital intensity를 흡수하며 개선|판정 제한|
|4|Luxor/governance|16%|debt/refinancing runway가 충분히 연장|판정 제한|
|5|M&A·royalty waterfall|15%|M&A/sponsor/segment-sale optionality가 실현|판정 제한|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|판정 제한|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|offer C$0.56|
|2|capital structure/catalyst|당시 공시/VIC 기준|up to 215.4m shares|
|3|후속 operating outcome|당시 공시/VIC 기준|target ownership ≈85%|
|4|최종/current outcome|당시 공시/VIC 기준|2015 independent listing ends|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2011-12-15|VIC idea 게시|T0|
|2011-12-23|formal partial tender 개시|첫 핵심 반증/확인 신호|
|2011-12-23|Luxor formal partial offer|지배구조 이벤트|
|2012-05-04|Fosterville/Stawell acquisition|자산구조 변화|
|2015-01-14|AuRico FCF sharing termination close|waterfall 단순화|
|2015-07-10|Newmarket combination complete|독립 상장 종료|

### Primary-source audit

- [VIC Crocodile Gold 2011](https://www.valueinvestorsclub.com/idea/CROCODILE_GOLD_CORP/0373325138) — 2011 Long의 entity·날짜 확인
- [Luxor bid announcement](https://www.prnewswire.com/news-releases/luxor-capital-announces-premium-offer-to-purchase-common-shares-of-crocodile-gold-135545133.html) — 2011 C$0.56 bid·약 60% premium·85% 목표 확인
- [Luxor formal offer](https://www.prnewswire.com/news-releases/luxor-commences-offer-to-acquire-common-shares-of-crocodile-gold-for-056-per-share-in-cash-136135378.html) — 2011-12-23 formal offer 확인
- [SEC AuRico/Crocodile acquisition](https://www.sec.gov/Archives/edgar/data/1078217/000120445912000644/exhibit99-1.htm) — 2012 Fosterville·Stawell 최대 C$105m 인수조건 확인
- [SEC AuRico 2014 royalty amendment](https://www.sec.gov/Archives/edgar/data/1078217/000106299315000967/exhibit99-3.htm) — 2014 C$20m + 2%/1% NSR로 FCF sharing 종료 확인
- [SEC Newmarket/Crocodile arrangement](https://www.sec.gov/Archives/edgar/data/1713443/000106299317003535/exhibit99-87.htm) — 2015 합병·C$0.37 cash/주식 선택·최종 corporate outcome 확인

## 5. 2014-12-26 — CRK Short — aquicap

Entity / 방향 검증: curated company = CROCODILE GOLD CORP · raw direction = Short · raw is_short=true. 원문 source link 부재로 동시기 event/metadata까지 교차검증.

### 1. 무슨 기업인가
Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다.

### 2. 산업 가치사슬과 돈의 흐름
Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
광산의 경쟁력은 고정된 브랜드가 아니라 orebody quality·운영실행·자금조달 조건에 의해 바뀐다.

### 4. 당시 VIC 원문과 핵심 숫자
2014-12 Crocodile Gold raw Short는 높은 금광 operational risk와 대주주/자본구조 복잡성, AuRico FCF-sharing obligation 때문에 headline gold exposure 대비 common equity가 불리하다는 논지로 재구성한다. entity는 날짜·M&A/자본배분 태그와 동시기 corporate events로 Crocodile Gold로 교정한다. raw CRK는 TSX Crocodile Gold를 뜻한다. 동일 ticker의 NYSE Comstock Resources와 분리해 entity를 확정.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
12월 22일 회사는 AuRico와 기존 FCF-sharing을 C$20m 현금 + Fosterville 2%/Stawell 1% NSR로 바꾸는 계약을 발표했다. 2015년 5월 Newmarket과 거래를 발표했고 Crocodile 주주는 C$0.37 현금 또는 주식 선택권을 받았으며 7월 합병이 완료됐다.

### 7. 무엇이 맞았나
liability와 governance 복잡성은 맞았지만 2015 strategic transaction이 late-2014 equity에 실현가치를 부여했다. raw directional Short 관점에서는 M&A optionality를 과소평가한 실패로 보는 편이 타당하다.

### 8. 무엇이 틀렸나/놓쳤나
운영자산 가치와 financing·royalty·M&A waterfall의 상호작용을 충분히 분리하지 못한 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: AuRico FCF-sharing 종료로 구조 단순화 (2014-12-22).

### 10. 재사용 가능한 교훈
광산주는 resource ounce보다 grade×recovery×mine life×AISC×sustaining capital의 현금흐름을 먼저 보고, 대주주 financing·royalty·partial tender·merger consideration을 equity waterfall에 얹는다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|grade·recovery·production|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|적중|
|2|cash cost·sustaining CapEx|18%|unit economics 또는 asset quality가 예상보다 강함|적중|
|3|liquidity·financing|17%|FCF가 capital intensity를 흡수하며 개선|적중|
|4|Luxor/governance|16%|debt/refinancing runway가 충분히 연장|오판|
|5|M&A·royalty waterfall|15%|M&A/sponsor/segment-sale optionality가 실현|오판|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|오판|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|C$20m termination payment|
|2|capital structure/catalyst|당시 공시/VIC 기준|Fosterville NSR 2%|
|3|후속 operating outcome|당시 공시/VIC 기준|Stawell NSR 1%|
|4|최종/current outcome|당시 공시/VIC 기준|2015 cash option C$0.37|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2014-12-26|VIC idea 게시|T0|
|2014-12-22|AuRico FCF-sharing 종료로 구조 단순화|첫 핵심 반증/확인 신호|
|2011-12-23|Luxor formal partial offer|지배구조 이벤트|
|2012-05-04|Fosterville/Stawell acquisition|자산구조 변화|
|2015-01-14|AuRico FCF sharing termination close|waterfall 단순화|
|2015-07-10|Newmarket combination complete|독립 상장 종료|

### Primary-source audit

- [VIC Crocodile Gold 2011](https://www.valueinvestorsclub.com/idea/CROCODILE_GOLD_CORP/0373325138) — 2011 Long의 entity·날짜 확인
- [Luxor bid announcement](https://www.prnewswire.com/news-releases/luxor-capital-announces-premium-offer-to-purchase-common-shares-of-crocodile-gold-135545133.html) — 2011 C$0.56 bid·약 60% premium·85% 목표 확인
- [Luxor formal offer](https://www.prnewswire.com/news-releases/luxor-commences-offer-to-acquire-common-shares-of-crocodile-gold-for-056-per-share-in-cash-136135378.html) — 2011-12-23 formal offer 확인
- [SEC AuRico/Crocodile acquisition](https://www.sec.gov/Archives/edgar/data/1078217/000120445912000644/exhibit99-1.htm) — 2012 Fosterville·Stawell 최대 C$105m 인수조건 확인
- [SEC AuRico 2014 royalty amendment](https://www.sec.gov/Archives/edgar/data/1078217/000106299315000967/exhibit99-3.htm) — 2014 C$20m + 2%/1% NSR로 FCF sharing 종료 확인
- [SEC Newmarket/Crocodile arrangement](https://www.sec.gov/Archives/edgar/data/1713443/000106299317003535/exhibit99-87.htm) — 2015 합병·C$0.37 cash/주식 선택·최종 corporate outcome 확인

# FRANKLIN COVEY CO — NYSE FC

## 9. 2002-10-02 — FC Short — north481

Entity / 방향 검증: curated company = FRANKLIN COVEY CO · raw direction = Short · raw is_short=true. 원문 source link 부재로 동시기 event/metadata까지 교차검증.

### 1. 무슨 기업인가
Franklin Covey는 7 Habits, 4 Disciplines of Execution 등 지적재산을 기반으로 조직 성과개선 교육·컨설팅·도구를 판매하는 회사다. 2000년대 초에는 Franklin Planner 중심 소비자 제품·소매점 비중이 컸지만, 2008년 Consumer Solutions Business Unit을 매각하고 기업 교육·컨설팅 중심으로 단순화했다. 이후 All Access Pass(AAP)와 Leader in Me 같은 구독형 모델로 전환해 현재는 반복매출·deferred revenue·renewal이 경제성의 핵심이다.

### 2. 산업 가치사슬과 돈의 흐름
Franklin Covey는 7 Habits, 4 Disciplines of Execution 등 지적재산을 기반으로 조직 성과개선 교육·컨설팅·도구를 판매하는 회사다. 2000년대 초에는 Franklin Planner 중심 소비자 제품·소매점 비중이 컸지만, 2008년 Consumer Solutions Business Unit을 매각하고 기업 교육·컨설팅 중심으로 단순화했다. 이후 All Access Pass(AAP)와 Leader in Me 같은 구독형 모델로 전환해 현재는 반복매출·deferred revenue·renewal이 경제성의 핵심이다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
지속 경쟁력은 브랜드 IP, 고객 조직 내 확산, facilitator ecosystem과 구독 renewal에서 나온다.

### 4. 당시 VIC 원문과 핵심 숫자
2002 Franklin Covey Short는 planner·retail 중심 소비자 사업의 매출하락과 높은 고정비가 유명 브랜드/IP의 질을 상쇄하고, turnaround가 지연될수록 자산가치와 현금이 소모된다는 논지로 재구성한다.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
회사는 2000년대 중반까지 retail/consumer 구조조정을 이어갔다. FY2007 매출은 $284.1m, 영업이익 $18.1m으로 FY2006 대비 개선됐고, 2008 소비자 사업을 Peterson Partners와 만든 별도법인에 $32m에 매각해 기업 교육·컨설팅 중심으로 재편했다. 장기적으로 회사는 존속하며 구독형 교육회사로 전환했다.

### 7. 무엇이 맞았나
초기 retail economics와 구조조정 필요성은 적중했지만 브랜드/IP의 재배치 가능성을 terminal decline로 보면 틀린다. 낮은 quality 사업부를 떼어낸 뒤 남는 core의 경제성을 별도 평가해야 한다.

### 8. 무엇이 틀렸나/놓쳤나
legacy retail과 durable IP/training core를 하나의 성장률로 합쳐 보는 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: FY2006~07 영업이익 회복 (2007-08-31).

### 10. 재사용 가능한 교훈
turnaround에서 전체 매출 추세보다 좋은 core와 나쁜 legacy segment를 분리한다. 매각·비용절감 후 남는 core의 반복매출·retention·incremental margin이 장기 가치의 핵심이다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|core training demand|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|부분적중|
|2|consumer/retail drag|18%|unit economics 또는 asset quality가 예상보다 강함|부분적중|
|3|gross margin·operating leverage|17%|FCF가 capital intensity를 흡수하며 개선|부분적중|
|4|cash·capital allocation|16%|debt/refinancing runway가 충분히 연장|부분적중|
|5|IP/recurring revenue quality|15%|M&A/sponsor/segment-sale optionality가 실현|부분적중|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|부분적중|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|FY2007 revenue $284.1m|
|2|capital structure/catalyst|당시 공시/VIC 기준|FY2007 op income $18.1m|
|3|후속 operating outcome|당시 공시/VIC 기준|2008 CSBU sale $32m|
|4|최종/current outcome|당시 공시/VIC 기준|2026 subscription-led|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2002-10-02|VIC idea 게시|T0|
|2007-08-31|FY2006~07 영업이익 회복|첫 핵심 반증/확인 신호|
|2007-08-31|FY2007 operating improvement|turnaround 진행|
|2008-05-22|Consumer Solutions sale announced|portfolio simplification|
|2008-07-07|CSBU sale completion documents|core training focus|
|2026-05-31|Q3 FY2026 subscription/deferred revenue update|현재 모델 확인|

### Primary-source audit

- [SEC Franklin Covey FY2002 10-K](https://www.sec.gov/Archives/edgar/data/886206/000088620602000048/fy02_10k.htm) — 2002 사업구조·교육/소비자 segment·채널 확인
- [SEC Franklin Covey FY2007 10-K](https://www.sec.gov/Archives/edgar/data/886206/000088620607000030/form10k_111407.htm) — FY2006~07 매출·영업이익 개선 및 retail footprint 확인
- [SEC Consumer Solutions sale release](https://www.sec.gov/Archives/edgar/data/886206/000088620608000027/ex991_052208.htm) — 2008 CSBU $32m 매각·proceeds buyback 계획 확인
- [SEC 2009 Q3 filing](https://www.sec.gov/Archives/edgar/data/886206/000088620609000026/form10q_070907.htm) — 소비자 사업 매각 후 training/consulting 중심 구조 확인
- [SEC FY2025 10-K](https://www.sec.gov/Archives/edgar/data/886206/000088620625000085/fc-20250831x10k.htm) — AAP/Leader in Me 구독모델·2025 deferred revenue 확인
- [SEC Q3 FY2026 results](https://www.sec.gov/Archives/edgar/data/886206/000119312526292604/fc-ex99_1.htm) — 2026 매출·deferred revenue·EBITDA·유동성 최신 확인

## 10. 2006-07-11 — FC Long — zach721

Entity / 방향 검증: curated company = FRANKLIN COVEY CO · raw direction = Long · raw is_short=false. 원문 source link 부재로 동시기 event/metadata까지 교차검증.

### 1. 무슨 기업인가
Franklin Covey는 7 Habits, 4 Disciplines of Execution 등 지적재산을 기반으로 조직 성과개선 교육·컨설팅·도구를 판매하는 회사다. 2000년대 초에는 Franklin Planner 중심 소비자 제품·소매점 비중이 컸지만, 2008년 Consumer Solutions Business Unit을 매각하고 기업 교육·컨설팅 중심으로 단순화했다. 이후 All Access Pass(AAP)와 Leader in Me 같은 구독형 모델로 전환해 현재는 반복매출·deferred revenue·renewal이 경제성의 핵심이다.

### 2. 산업 가치사슬과 돈의 흐름
Franklin Covey는 7 Habits, 4 Disciplines of Execution 등 지적재산을 기반으로 조직 성과개선 교육·컨설팅·도구를 판매하는 회사다. 2000년대 초에는 Franklin Planner 중심 소비자 제품·소매점 비중이 컸지만, 2008년 Consumer Solutions Business Unit을 매각하고 기업 교육·컨설팅 중심으로 단순화했다. 이후 All Access Pass(AAP)와 Leader in Me 같은 구독형 모델로 전환해 현재는 반복매출·deferred revenue·renewal이 경제성의 핵심이다. 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.

### 3. 경쟁우위·경쟁구도·핵심 지표
지속 경쟁력은 브랜드 IP, 고객 조직 내 확산, facilitator ecosystem과 구독 renewal에서 나온다.

### 4. 당시 VIC 원문과 핵심 숫자
2006 Franklin Covey Long은 구조조정으로 비용이 내려가고 training/consulting이 회복되는 가운데 소비자·부동산/기타 자산과 자본환원이 downside를 지지해, 낮은 기대에서 turnaround operating leverage가 발생한다는 논지로 재구성한다.

### 5. 밸류에이션과 기대수익의 연결
밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.

### 6. 실제 전개
FY2007 매출 $284.1m, 영업이익 $18.1m으로 FY2006 $14.0m 대비 개선됐다. 2008 소비자 사업을 $32m 현금에 매각하고 proceeds를 자사주 매입에 쓰겠다고 발표해 core를 교육/컨설팅으로 단순화했다. raw 성과는 1년 +41.4%, 3년 -4.7%, 5년 +75.9%다. 이후 AAP 구독모델로 진화했고 Q3 FY2026 deferred revenue는 $96m이었다.

### 7. 무엇이 맞았나
turnaround와 asset/capital-allocation catalyst는 실제로 작동했다. 다만 3년 수익률이 마이너스였다는 점은 실행경로가 매끄럽지 않았음을 보여준다. 긴 horizon과 core-business 재편을 견딘 경우 성공한 사례다.

### 8. 무엇이 틀렸나/놓쳤나
legacy retail과 durable IP/training core를 하나의 성장률로 합쳐 보는 오류.

### 9. 사전 반증조건과 첫 신호
사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: FY2007 operating improvement (2007-08-31).

### 10. 재사용 가능한 교훈
turnaround에서 전체 매출 추세보다 좋은 core와 나쁜 legacy segment를 분리한다. 매각·비용절감 후 남는 core의 반복매출·retention·incremental margin이 장기 가치의 핵심이다.

### Claim audit

|#|주장 축|Weight|사전 반증조건|판정|
|---:|---|---:|---|---|
|1|core training demand|20%|핵심 가격/수요 변수가 thesis 반대방향으로 지속|적중|
|2|consumer/retail drag|18%|unit economics 또는 asset quality가 예상보다 강함|적중|
|3|gross margin·operating leverage|17%|FCF가 capital intensity를 흡수하며 개선|적중|
|4|cash·capital allocation|16%|debt/refinancing runway가 충분히 연장|적중|
|5|IP/recurring revenue quality|15%|M&A/sponsor/segment-sale optionality가 실현|적중|
|6|valuation·반증규칙|14%|risk-adjusted IRR이 hurdle을 상회|적중|

### Metric audit

|#|Metric|T0 기준|Actual / 확인치|
|---:|---|---|---|
|1|T0/핵심 valuation|당시 공시/VIC 기준|1y return +41.4%|
|2|capital structure/catalyst|당시 공시/VIC 기준|3y return -4.7%|
|3|후속 operating outcome|당시 공시/VIC 기준|5y return +75.9%|
|4|최종/current outcome|당시 공시/VIC 기준|Q3 FY26 deferred revenue $96m|

### Timeline

|날짜|사건|의미|
|---|---|---|
|2006-07-11|VIC idea 게시|T0|
|2007-08-31|FY2007 operating improvement|첫 핵심 반증/확인 신호|
|2007-08-31|FY2007 operating improvement|turnaround 진행|
|2008-05-22|Consumer Solutions sale announced|portfolio simplification|
|2008-07-07|CSBU sale completion documents|core training focus|
|2026-05-31|Q3 FY2026 subscription/deferred revenue update|현재 모델 확인|

### Primary-source audit

- [SEC Franklin Covey FY2002 10-K](https://www.sec.gov/Archives/edgar/data/886206/000088620602000048/fy02_10k.htm) — 2002 사업구조·교육/소비자 segment·채널 확인
- [SEC Franklin Covey FY2007 10-K](https://www.sec.gov/Archives/edgar/data/886206/000088620607000030/form10k_111407.htm) — FY2006~07 매출·영업이익 개선 및 retail footprint 확인
- [SEC Consumer Solutions sale release](https://www.sec.gov/Archives/edgar/data/886206/000088620608000027/ex991_052208.htm) — 2008 CSBU $32m 매각·proceeds buyback 계획 확인
- [SEC 2009 Q3 filing](https://www.sec.gov/Archives/edgar/data/886206/000088620609000026/form10q_070907.htm) — 소비자 사업 매각 후 training/consulting 중심 구조 확인
- [SEC FY2025 10-K](https://www.sec.gov/Archives/edgar/data/886206/000088620625000085/fc-20250831x10k.htm) — AAP/Leader in Me 구독모델·2025 deferred revenue 확인
- [SEC Q3 FY2026 results](https://www.sec.gov/Archives/edgar/data/886206/000119312526292604/fc-ex99_1.htm) — 2026 매출·deferred revenue·EBITDA·유동성 최신 확인

