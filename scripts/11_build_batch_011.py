#!/usr/bin/env python3
"""Build the reviewed Apple/Google Batch 011 report and V7 overlay."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASOF = "2024-01-31"
ANALYSIS_DATE = "2026-09-03"

APPLE_DESC = (
    "Apple은 기기 한 대를 파는 하드웨어 회사이면서 동시에 자체 반도체·운영체제·앱 유통·결제·클라우드·콘텐츠를 묶는 소비자 기술 플랫폼이다. "
    "iPhone·Mac·iPad·Wearables의 매출총이익과 App Store, 광고, iCloud, AppleCare, 결제·콘텐츠 구독의 반복 매출이 현금을 만든다. "
    "하드웨어의 설치기반이 개발자와 서비스 수요를 만들고, 더 많은 앱·액세서리·연동기능이 기기 전환비용과 고객생애가치를 높이는 양면 구조다. "
    "핵심 경제성은 단순 출하량보다 기기 ASP·매출총이익, 활성기기 수, 유료계정·서비스 ARPU, 유지율, 공급망 선급금과 자체칩의 원가·성능 우위에서 나온다. "
    "반대로 제품교체주기 장기화, 중국 공급·수요 집중, App Store 규제, 플랫폼 수수료 압력과 혁신 실패는 profit pool을 훼손한다. "
    "따라서 Apple을 볼 때는 당해 iPhone unit뿐 아니라 설치기반에서 반복 회수되는 현금과 그 현금의 자사주·R&D·공급망 재투자 수익률을 함께 봐야 한다."
)

GOOGLE_DESC = (
    "Google/Alphabet은 이용자의 검색·동영상·지도·웹 활동을 광고주의 성과형 수요와 연결하는 경매 기반 디지털 광고 플랫폼이다. "
    "Search와 YouTube 광고가 주 수익원이고, 광고주가 낸 금액에서 제휴 사이트·유통 파트너에 지급하는 TAC와 데이터센터·콘텐츠·인력비를 뺀 이익이 핵심이다. "
    "더 많은 검색은 의도 데이터와 알고리즘을 개선하고 더 높은 광고 ROI가 광고주 입찰을 늘리는 학습·규모의 순환을 만든다. Android와 Chrome은 직접 수익보다 검색 접근점을 지키는 배포자산이다. "
    "YouTube는 광고·구독, Google Cloud는 사용량·구독 수익을 만들며 2015년 이후 Other Bets와 분리해 자본배분을 드러냈다. "
    "핵심 위험은 검색 진입점의 앱·AI 전환, Apple 등에 지급하는 배포비, 개인정보 규제·반독점, 높은 SBC와 손실성 신규사업이다. "
    "검색의 현금창출력과 옵션가치를 구분하고 각 옵션의 실제 매출·이익·희석을 별도로 검증해야 한다."
)

APPLE_SOURCES = [
    ("VIC 원문", "Value Investors Club Apple 원문", "Value Investors Club", None, None, "당시 주장·가격·보유기간의 1차 자료"),
    ("공시", "Apple 2016 Form 10-K", "SEC", "2016-10-26", "https://www.sec.gov/Archives/edgar/data/320193/000162828016020309/a201610-k9242016.htm", "iPhone 둔화, Services, 현금흐름과 자사주 검증"),
    ("공시", "Apple 2018 Form 10-K", "SEC", "2018-11-05", "https://www.sec.gov/Archives/edgar/data/320193/000032019318000145/a10-k20189292018.htm", "2016 롱의 EPS·Services 목표 검증"),
    ("공시", "Apple 2023 Form 10-K", "SEC", "2023-11-03", "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm", "2024 기준 매출·이익·제품과 서비스 구조"),
    ("가격", "Apple historical prices", "Digrin", "2024-01-31", "https://www.digrin.com/stocks/detail/AAPL/price", "분할조정 월말 가격 교차검증"),
]

GOOGLE_SOURCES = [
    ("VIC 원문", "Value Investors Club Google 원문", "Value Investors Club", None, None, "당시 주장·가격·보유기간의 1차 자료"),
    ("공시", "Google 2009 Form 10-K", "SEC", "2010-02-12", "https://www.sec.gov/Archives/edgar/data/1288776/000119312510030774/d10k.htm", "검색광고와 현금창출 검증"),
    ("공시", "Google 2011 Form 10-K", "SEC", "2012-02-08", "https://www.sec.gov/Archives/edgar/data/1288776/000119312512025336/d260164d10k.htm", "2011 매출·영업현금·투자지출 검증"),
    ("공시", "Alphabet 2023 Form 10-K", "SEC", "2024-01-31", "https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm", "YouTube·Cloud·Search의 실제 규모와 수익성"),
    ("가격", "Alphabet historical prices", "Digrin", "2024-01-31", "https://www.digrin.com/stocks/detail/GOOG/price", "분할조정 월말 가격 교차검증"),
]


IDEAS = [
    dict(id="abd44259-b085-42b0-b70c-19b4a007d532", date="2000-12-22", ticker="AAPL", company="Apple", author="paul62", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/Apple_Computer/2049431324", dchars=5544, cchars=568,
         title="순현금에 가까운 Apple 턴어라운드 롱", security="보통주", verdict="초대형 성공", score=9.0, process=8.4,
         thesis="$14.44 주가 중 순현금·유가증권이 주당 $12.66이므로 영업사업은 약 $597m, 다음해 예상매출 $6bn의 0.10배에 불과하다고 봤다. PC 재고조정과 교육시장 부진은 일시적이며 충성고객·브랜드, Mac OS X, 신제품과 공급망 정상화가 현금소모 없이 회복을 만들 것이라는 롱이었다.",
         actual="2001년 PC 부진은 이어졌지만 순현금이 생존시간을 제공했고, iPod·Apple Store·iTunes 뒤 iPhone으로 사업 자체가 재창조됐다. 2000년 가격은 후속 분할을 반영하면 약 $0.26이며 2024-01-31 $184.40까지 가격만 약 700배가 됐다. 다만 성공의 대부분은 원문에 없던 디지털허브·모바일 플랫폼에서 왔다.",
         why="현금에 가까운 가격으로 옵션을 샀다는 하방규율이 탁월했다. 반면 기존 Mac 정상화만으로 미래 규모를 설명한 것은 아니므로 ‘가격 성공’과 ‘예측한 인과의 완전 적중’을 구분해야 한다.", root="저평가가 맞았지만 초과수익의 주된 원인은 미예측 신사업", first="2001년 iPod 출시와 직영점 확대로 PC 외 성장축 등장", first_date="2001-10-23",
         valuation="순현금 $12.66/주, 영업가치 $1.77/주·0.10x 매출", stock="분할조정 약 $0.26→$184.40, 가격수익 약 +71,000%", current="2023년 Apple은 매출 $383.3bn, 순이익 $97.0bn을 기록했고 Services가 성숙한 두 번째 이익축이 됐다.",
         claims=[
             ("자산 하방", "주가의 88%가 순현금·유가증권으로 덮인다.", "현금성 자산의 회수가능성과 낮은 부채", "분기 현금소모와 증권손실로 순현금이 주가의 60% 아래로 하락", "순현금은 downturn을 버틸 runway를 제공했다.", "적중"),
             ("Mac 정상화", "교육영업 재편·신제품·Mac OS X가 PC 매출을 회복시킨다.", "충성고객과 개발자 생태계 유지", "Mac unit·gross margin이 4개 분기 연속 악화", "Mac만의 정상화보다 iPod 이후 카테고리 확장이 결정적이었다.", "부분"),
             ("브랜드 옵션", "혁신·디자인 브랜드는 장부에 없는 가치다.", "브랜드가 새 카테고리 구매로 이전", "신제품이 기존 고객 밖에서 채택되지 않음", "iPod·iPhone·iPad로 브랜드 확장성이 입증됐다.", "적중"),
             ("자본배분", "$500m buyback은 경영진의 저평가 확신을 보여준다.", "현금이 가치파괴 M&A보다 주주에게 효율적으로 배분", "평균 $37.82의 고가매입 뒤 추가 현금소모", "초기 buyback 가격은 나빴지만 장기 현금창출이 이를 압도했다.", "부분"),
         ],
         metrics=[("주가/순현금", "$14.44/$12.66", "자산 하방", "$184.40 종착", "적중"), ("영업가치/매출", "0.10x", "정상화", "신사업으로 규모 급증", "매우 성공"), ("순현금", "$4.25bn", "보존", "생존자금 역할", "적중"), ("장기가격", "약 $0.26 조정", "상승", "$184.40", "초대형 성공")],
         timeline=[("2001-10-23", "iPod 공개", "Mac 정상화 외 새 성장옵션 현실화"), ("2003-04-28", "iTunes Music Store 출시", "기기·콘텐츠 생태계 형성"), ("2007-01-09", "iPhone 공개", "기업가치의 중심이 PC에서 모바일로 이동"), (ASOF, "평가기준일", "원 논지 대비 압도적 장기 성공")]),

    dict(id="e0bfeec8-f257-4df8-8200-55e3835c54ca", date="2003-04-22", ticker="AAPL", company="Apple", author="torico780", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/Apple_Computer/3176828218", dchars=4355, cchars=70,
         title="Universal Music 오해와 iTunes 옵션 롱", security="보통주", verdict="초대형 성공", score=9.4, process=9.0,
         thesis="$13.25에서 현금·증권 $4.526bn과 부채 $315m, 연간 정상 FCF 약 $200m을 근거로 ex-cash EV/FCF 3~4배라고 계산했다. FCF 15배와 현금을 더한 $19.70 가치, Vivendi Universal Music 인수확률 5% 미만, 4월 28일 5대 음반사 음악을 곡당 판매할 서비스가 더 합리적이라는 이벤트 롱이었다.",
         actual="Apple은 VUM을 사지 않았고 6일 뒤 iTunes Music Store를 출시했다. iPod·직영점·iTunes가 PC 바깥의 생태계를 만들면서 목표 $19.70은 빠르게 넘어섰다. 분할조정 약 $0.24에서 2024-01-31 $184.40으로 가격만 약 780배다. 이벤트 판단, 하방가치, 제품 옵션이 모두 맞았다.",
         why="소문을 그대로 할인하지 않고 인수의 전략적 합리성과 대체경로를 비교했다. 현금과 정상 FCF로 하방을 만들면서 iTunes 옵션에는 높은 값을 선반영하지 않아 촉매가 실패해도 손익비가 남았다.", root="중대한 오류 없음; 정상 FCF에 이자수익이 섞이는 점은 haircut 필요", first="2003년 4월 28일 VUM 인수 대신 iTunes Music Store 출시", first_date="2003-04-28",
         valuation="정상 FCF $200m×15 + 현금 - 부채 = $19.70/주", stock="분할조정 약 $0.24→$184.40, 가격수익 약 +77,800%", current="iTunes가 만든 계정·콘텐츠 관계는 App Store와 Services 경제성의 선행형태가 됐다.",
         claims=[
             ("현금 하방", "$4.526bn 현금·증권과 $315m 부채가 가격을 지지한다.", "현금이 본업손실로 빠르게 소진되지 않음", "연간 현금소모가 $500m 이상으로 확대", "대규모 순현금이 전략 전환시간을 줬다.", "적중"),
             ("정상 FCF", "연 $200m FCF와 ex-cash 3~4배는 과도한 할인이다.", "이자수익 제외 후에도 정상 영업현금 양수", "PC 손실로 정상 FCF가 장기간 음수", "당시 수익의 질 논쟁은 있었지만 곧 제품 mix가 개선됐다.", "부분~적중"),
             ("VUM 비인수", "한 음반사를 사는 것보다 5대 음반사의 유통창구가 전략적으로 낫다.", "레이블들이 디지털 유통에 참여", "Apple이 대형 콘텐츠 소유권을 직접 인수", "VUM 인수 없이 iTunes가 예정대로 출시됐다.", "정확히 적중"),
             ("iPod·리테일", "iPod 78,000대/분기와 직영점이 비PC 성장을 만든다.", "제품이 Windows 고객까지 확장", "iPod 성장 정체와 소매점 고정비 확대", "iPod와 리테일은 대규모 생태계의 입구가 됐다.", "적중"),
         ],
         metrics=[("현금·증권", "$4.526bn", "하방", "유동성 유지", "적중"), ("정상 FCF", "$200m", "지속", "후일 대폭 확대", "적중"), ("목표가", "$19.70", "약 +49%", "장기 대폭 초과", "성공"), ("장기가격", "약 $0.24 조정", "상승", "$184.40", "초대형 성공")],
         timeline=[("2003-04-28", "iTunes Music Store 출시", "핵심 이벤트 정확히 실현"), ("2003-10-15", "분기 흑자와 매출 19% 성장", "정상화 확인"), ("2007-01-09", "iPhone 공개", "생태계 옵션 확대"), (ASOF, "평가기준일", "목표와 장기 수익 모두 압도")]),

    dict(id="1f23707e-b4c5-46cc-b39c-11fa4e949b87", date="2011-05-02", ticker="AAPL", company="Apple", author="SBB", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/APPLE_INC/4584988920", dchars=25627, cchars=181,
         title="스마트폰·태블릿 규모와 생태계 롱", security="보통주", verdict="매우 성공", score=9.2, process=8.8,
         thesis="스마트폰·태블릿의 거대한 TAM, 부품 선급금과 공용부품의 규모우위, 하드웨어·소프트웨어 수직통합, 2억 카드계정과 개발자 경제, 전환비용을 핵심으로 제시했다. 2011년 3월 현금 $70/주·TTM EPS $21, 회계연도 말 $87/$27을 예상하고 bear 10배+현금 $357, neutral 15배+현금 $492, bull EPS $40~60·현금 $140로 $540~740 이상을 계산했다.",
         actual="iPhone·iPad 성장과 iOS 생태계, 부품구매력, 설치기반의 halo는 매우 정확했다. 목표범위는 후속 분할 전 기준으로 수년 안에 달성됐다. 다만 Jobs 부재 위험은 제품조직과 서비스 확장으로 완화됐고, 현금 자체의 가치보다 지속적 제품혁신·자사주·서비스가 장기수익을 만들었다.",
         why="TAM만이 아니라 공급자·개발자·소비자 사이의 피드백과 부품원가 우위를 연결했다. bear/base/bull의 EPS·현금을 분리한 것도 좋았다. 다만 ‘현금이 하방’이라는 논리는 해외현금 세금과 가치파괴 가능성을 더 할인했어야 한다.", root="현금 하방을 다소 과신했지만 생태계 인과는 정확", first="iPhone·iPad 출하와 앱 생태계가 예상대로 확대", first_date="2012-01-24",
         valuation="현금+10~20x EPS로 $280~740+ 시나리오", stock="분할조정 약 $12.4→$184.40, 가격수익 약 +1,390%", current="2024년 초 활성기기 기반은 22억대를 넘었고 하드웨어·서비스 결합이 유지됐다.",
         claims=[
             ("TAM", "스마트폰·태블릿은 Apple이 점유율을 잃어도 성장 가능한 시장이다.", "카테고리 성장과 지역·통신사 확대", "산업 unit 성장 둔화와 Apple unit 감소", "2010년대 모바일 컴퓨팅이 PC보다 큰 시장이 됐다.", "적중"),
             ("규모·공급망", "선급금·공용부품·대량구매가 원가와 출시속도 우위를 만든다.", "공급부족기에도 우선물량·원가우위 유지", "경쟁사가 동일부품을 더 싸게 조달", "규모와 자체칩이 마진·성능 차별화로 발전했다.", "적중"),
             ("생태계", "계정·앱·액세서리·기기연동이 고객과 개발자를 묶는다.", "개발자 수익과 유지율 상승", "Android 앱경제가 iOS를 구조적으로 추월", "iOS의 monetization과 설치기반이 장기 유지됐다.", "적중"),
             ("하방가치", "현금과 낮은 EPS 배수가 손실을 제한한다.", "현금이 주주에게 귀속되고 이익 지속", "해외현금 haircut·이익 급감", "하방은 작동했지만 핵심 성공은 earnings growth였다.", "부분"),
         ],
         metrics=[("현금/주", "$70", "$87→$140", "대폭 증가 후 환원", "적중"), ("TTM EPS", "$21", "$40~60", "목표범위 달성", "적중"), ("목표가", "$540~740+", "2~3년", "후속 분할 전 달성", "성공"), ("장기가격", "약 $12.4 조정", "상승", "$184.40", "매우 성공")],
         timeline=[("2011-10-05", "Steve Jobs 사망", "명시 위험 현실화에도 조직 지속"), ("2012-01-24", "기록적 iPhone·iPad 분기", "TAM·규모 논지 확인"), ("2014-06-09", "7대1 주식분할", "목표가격 비교시 조정 필요"), (ASOF, "평가기준일", "장기 생태계와 수익 확인")]),

    dict(id="4bb92a02-8578-49f8-99b1-43b851eb650d", date="2013-02-07", ticker="AAPL", company="Apple", author="murman", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/APPLE_INC/0752368248", dchars=15777, cchars=367,
         title="마진 정상화 스트레스와 현금환원 롱", security="보통주", verdict="매우 성공", score=9.0, process=9.3,
         thesis="$700에서 약 $450으로 하락한 Apple을 브랜드·생태계·공급망 moat가 남은 성숙기업으로 봤다. 하드웨어 premium과 2012년 44% gross margin이 낮아질 위험을 인정한 뒤 28% gross margin에서도 EPS 약 $30, $137bn 현금·주당 $145, ex-cash 약 10배라고 stress했다. 매출 10년 2% 성장만으로 $500, 정상 시 $600~800과 배당·자사주 확대를 기대했다.",
         actual="FY2013 gross margin은 약 37.6%로 2012년 43.9%에서 실제 하락했지만 28% stress까지 무너지지 않았다. 2013년 4월 Apple은 총 $100bn 환원과 $60bn buyback을 발표했다. iPhone·Services·자사주가 EPS를 키워 목표범위와 장기수익을 달성했다.",
         why="좋은 기업이라는 주장에 그치지 않고 마진 붕괴·해외현금 haircut·성장정체를 숫자로 넣었다. 실제 핵심 악재인 마진 정상화를 견딘 가격을 샀고, 자본환원이 per-share 가치를 현실화했다.", root="오류 제한적; 신제품 성공보다 보수적 stress에 의존", first="FY2013 gross margin 하락에도 FCF 유지와 대규모 자본환원 발표", first_date="2013-04-23",
         valuation="현금 $145/주, 28% gross margin EPS $30, ex-cash 약 10x", stock="분할조정 약 $16.1→$184.40, 가격수익 약 +1,048%", current="제품 매출 변동에도 Services와 대규모 buyback이 주당가치를 지지하는 구조가 정착했다.",
         claims=[
             ("moat 지속", "Jobs 이후에도 브랜드·생태계·공급구매력이 쉽게 사라지지 않는다.", "고객유지와 개발자·공급자 우위", "ASP·유지율·개발자 수익 동시 하락", "브랜드와 생태계는 2024까지 유지됐다.", "적중"),
             ("마진 stress", "gross margin 28%에서도 EPS $30으로 가격이 방어된다.", "판매량과 비용구조가 급격히 붕괴하지 않음", "28% 아래 하락과 매출 역성장", "마진은 37.6%로 정상화됐지만 stress보다 양호했다.", "적중"),
             ("현금 청구권", "$137bn 현금은 haircut 후에도 큰 주주가치다.", "배당·buyback으로 이전", "현금이 장기 방치되거나 M&A로 소진", "$100bn 환원 프로그램이 곧 발표됐다.", "적중"),
             ("저성장 가치", "10년 매출 2% 성장만으로도 $500 이상이다.", "FCF와 주당수 감소 지속", "마진·매출 동시 훼손", "매출과 FCF가 가정보다 크게 성장했다.", "적중"),
         ],
         metrics=[("gross margin", "43.9% FY2012", "stress 28%", "37.6% FY2013", "방어"), ("현금", "$137bn/$145주", "환원", "$100bn 프로그램", "적중"), ("목표가", "$600~800", "정상화", "달성", "성공"), ("장기가격", "약 $16.1 조정", "상승", "$184.40", "매우 성공")],
         timeline=[("2013-04-23", "$100bn 자본환원 발표", "현금 청구권 촉매 실현"), ("2013-09-28", "FY2013 gross margin 37.6%", "마진 하락을 견딤"), ("2014-06-09", "7대1 분할", "가격비교 조정"), (ASOF, "평가기준일", "장기 목표 대폭 초과")]),

    dict(id="4d868d97-7fb3-43ed-a835-f7407215efe3", date="2015-07-02", ticker="GOOG", company="Alphabet", author="miser861", source_short=1, direction="Long", link=None, dchars=23254, cchars=68,
         title="Search 저평가와 YouTube·Cloud 무료옵션 롱", security="Class C 보통주", verdict="매우 성공", score=9.5, process=9.2,
         thesis="$525에서 미납 해외현금세금 $7bn까지 뺀 NTM cash EPS 11배라고 봤다. Search는 최소 20배, 40%+ 성장하는 YouTube와 GCP는 더 높은 배수를 받아야 하며 YouTube만 매출 $6bn×5=$30bn으로 추정했다. Ruth Porat CFO가 공시·자본배분을 개선할 수 있고 2018 cash EPS $45, cash/share $231, 25배로 $1,353~1,436을 제시했다.",
         actual="한 달 뒤 Alphabet 지주구조가 발표됐고 2015년 10월 첫 대규모 자사주 승인이 뒤따랐다. 2023년 YouTube 광고매출은 약 $31.5bn, Cloud 매출은 약 $33.1bn이며 Cloud 영업이익은 $1.7bn으로 흑자 전환했다. 분할조정 약 $26.25에서 $141.80으로 약 5.4배가 됐다.",
         why="핵심 Search의 현금가치만으로 가격을 방어하고 YouTube·Cloud를 매출·성장률로 별도 표시했다. 촉매가 없어도 수익이 난다는 구조였는데 실제 공시·환원 촉매까지 실현됐다. 다만 SBC를 전액 add-back한 것은 경제적 비용을 과소평가했다.", root="SBC add-back과 1.5% 희석 가정은 과도했지만 핵심 가치에 치명적이지 않음", first="Alphabet 구조개편과 segment disclosure·buyback 발표", first_date="2015-08-10",
         valuation="ex-cash NTM cash EPS 11x; 2018 목표 $1,353~1,436", stock="분할조정 약 $26.25→$141.80, 가격수익 약 +440%", current="2023년 YouTube 광고 $31.5bn, Cloud $33.1bn·영업이익 $1.7bn으로 두 옵션이 실사업이 됐다.",
         claims=[
             ("Search 저평가", "높은 진입장벽·성장률의 Search가 ex-cash 11배다.", "검색점유·광고 ROI·margin 유지", "paid click과 query share 동시 하락", "Search는 2023년에도 최대 현금원이었다.", "적중"),
             ("YouTube 옵션", "매출 $6bn·40%+ 성장, 독립가치 $30bn 이상이다.", "영상시간과 광고·구독 monetization", "콘텐츠비가 매출보다 빨리 증가", "2023 광고매출만 약 $31.5bn으로 성장했다.", "적중"),
             ("Cloud 옵션", "GCP는 독립 시 Search보다 높은 성장배수를 받을 수 있다.", "규모 확대로 손실이 이익으로 전환", "성장 둔화에도 구조적 적자", "2023 매출 $33.1bn·영업이익 $1.7bn이 됐다.", "적중"),
             ("Porat 촉매", "새 CFO가 공시와 자본배분을 개선한다.", "segment 공개와 현금환원", "공시 불변·희석 지속", "Alphabet 분리공시와 buyback이 빠르게 실현됐다.", "적중"),
         ],
         metrics=[("ex-cash 배수", "11x NTM cash EPS", "20x+", "장기 rerating", "적중"), ("YouTube", "$6bn 매출 추정", "$30bn 가치", "$31.5bn 광고매출 2023", "초과"), ("Cloud", "40%+ 성장", "고배수 옵션", "$33.1bn·흑자", "적중"), ("장기가격", "$26.25 조정", "$67.7~71.8 조정 목표", "$141.80", "매우 성공")],
         timeline=[("2015-08-10", "Alphabet 지주구조 발표", "공시 촉매 실현"), ("2015-10-22", "첫 자사주 승인", "자본배분 촉매 실현"), ("2023-12-31", "Cloud 연간 흑자", "무료옵션의 경제성 확인"), (ASOF, "평가기준일", "목표·핵심 인과 모두 달성")]),

    dict(id="7fc96741-c87b-45f6-8942-d7397e97045c", date="2016-08-16", ticker="AAPL", company="Apple", author="rasputin998", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/APPLE_INC/4003116338", dchars=26590, cchars=315,
         title="iPhone trough·Services·buyback 롱", security="보통주", verdict="매우 성공", score=9.6, process=9.4,
         thesis="교체주기 연장과 보조금 축소의 어려운 iPhone 전환을 이미 통과했고, Wall Street가 Apple을 9배 EV/FCF의 낡은 하드웨어로 본다고 주장했다. 약 10억대 설치기반과 고마진 Services, Watch 등 초기제품, 연 5% 수준 주식수 감소로 FY2017 Services $28bn, 수년 내 EPS $12·FCF/주 $12, 목표 $150+를 제시했다.",
         actual="목표 $150(2020 분할 전)는 2017년 5월 도달했다. Services는 FY2016 약 $24.3bn에서 FY2018 약 $39.7bn으로 늘었고 FY2018 EPS는 당시 주식수 기준 약 $11.91로 $12 가정에 근접했다. 설치기반·서비스·자사주가 unit 정체를 상쇄한다는 인과가 정확했다.",
         why="cycle trough와 구조적 쇠퇴를 구분하고, iPhone 외 수익축과 per-share 계산을 명시했다. 단순 매출성장이 아니라 높은 margin Services와 주식수 감소가 EPS로 전달되는 경로까지 연결한 것이 강점이다.", root="Services 규제와 iPhone 의존을 과소평가했으나 핵심 오류는 제한적", first="2017년 Services 성장과 iPhone ASP 회복, 목표가 조기 도달", first_date="2017-05-01",
         valuation="9x EV/FCF, net cash $26/주, 목표 $150+", stock="분할조정 약 $27.3→$184.40, 가격수익 약 +575%", current="FY2023 Services 매출은 약 $85.2bn으로 2016년 논지의 두 번째 엔진이 현실화됐다.",
         claims=[
             ("cycle trough", "FY2016 iPhone 역성장은 교체주기·보조금 전환의 일시적 저점이다.", "설치기반 유지와 다음 cycle ASP 회복", "두 세대 연속 unit·ASP 동반 하락", "2017 이후 ASP와 매출이 회복됐다.", "적중"),
             ("Services", "10억대 설치기반이 고마진 반복매출을 만든다.", "유료계정·구매액이 기기보다 빠르게 성장", "Services 성장률·margin 급락", "FY2018 $39.7bn, FY2023 $85.2bn으로 확대됐다.", "적중"),
             ("신제품", "Watch·기타 제품은 초기라 추가 성장옵션이다.", "생태계 연동과 반복구매", "제품이 독립 수요를 만들지 못함", "Wearables가 의미 있는 카테고리가 됐다.", "적중"),
             ("buyback", "낮은 배수의 자사주가 EPS·FCF/주를 복리시킨다.", "FCF와 할인매입 지속", "고평가 매입·순현금 급감", "주식수 감소가 per-share 성장을 크게 보탰다.", "적중"),
         ],
         metrics=[("EV/FCF", "9x", "rerating", "목표 빠른 도달", "적중"), ("Services", "$24.3bn FY2016", "$28bn FY2017", "$39.7bn FY2018", "초과"), ("EPS", "cycle trough", "$12 수년내", "$11.91 FY2018", "근접"), ("장기가격", "$27.3 조정", "$37.5 조정 목표", "$184.40", "매우 성공")],
         timeline=[("2017-05-01", "$150 목표 도달", "valuation 촉매 실현"), ("2018-09-29", "Services $39.7bn", "두 번째 성장축 확인"), ("2020-08-31", "4대1 분할", "가격비교 조정"), (ASOF, "평가기준일", "per-share 복리 지속")]),

    dict(id="14556ae0-911d-4b4a-bf38-e09044713ff7", date="2017-01-23", ticker="AAPL", company="Apple", author="Bluegrass", source_short=1, direction="Short", link=None, dchars=30422, cchars=248,
         title="profit-pool 평균회귀와 느린 청산 숏", security="보통주 숏", verdict="치명적 실패", score=2.8, process=4.3,
         thesis="Apple을 혁신이 끝난 fast follower·고가 리테일러로 보고, 15~20% unit share로 스마트폰 산업이익 103.6%를 가져가는 상태는 평균회귀한다고 주장했다. Android 규모, Google·Facebook·Amazon의 서비스 계층이 폐쇄형 iOS를 약화시키고 중국·인도 가격경쟁과 Jobs 부재가 겹친다며 영업이 자본비용을 못 벌고 ‘느린 청산’ 중이라 평가했다. 당시 약 $120 대비 가치 $60을 제시했다.",
         actual="iPhone unit 성장 둔화와 중국 경쟁은 일부 맞았지만 ASP 상승, Services·Wearables, 10억대 이상 설치기반, 자체칩과 buyback이 이익·주당가치를 늘렸다. FY2023 Services는 $85.2bn, 2024년 초 활성기기는 22억대를 넘었다. 분할조정 약 $30에서 $184.40으로 올라 숏은 약 -515%의 가격 역행을 맞았다.",
         why="profit share 100% 초과를 곧바로 소멸로 해석하고 그 원인인 높은 ASP·수직통합·서비스 monetization을 분해하지 않았다. 특히 현금을 포함한 ‘주주자본’ 전체로 incremental ROIC를 계산해 무수익 현금이 영업수익률을 낮춘다는 순환오류를 만들었고 무형 R&D·생태계 재투자를 누락했다.", root="현금을 영업투하자본으로 보고 생태계의 무형 재투자·가격결정력을 누락", first="2017년 Services 23% 성장과 iPhone ASP·매출 회복", first_date="2017-11-03",
         valuation="청산·자기잠식 시나리오 가치 약 $54~60", stock="분할조정 약 $30→$184.40; 숏 가격손실 약 -515%", current="unit보다 설치기반·서비스·ASP가 이익을 결정했고 ‘느린 청산’과 반대로 per-share FCF가 확대됐다.",
         claims=[
             ("profit pool 평균회귀", "산업이익 103.6% 점유는 지속 불가능하다.", "경쟁사가 동등한 ASP·margin을 확보", "Apple ASP와 산업이익 점유가 유지", "점유는 변동했지만 절대이익은 Services·ASP로 유지됐다.", "인과 실패"),
             ("폐쇄생태계 붕괴", "Android와 인터넷 서비스가 iOS를 disintermediate한다.", "소비자 전환비용과 개발자 수익 약화", "활성기기·유료계정·Services 성장", "설치기반과 서비스가 오히려 확대됐다.", "실패"),
             ("낮은 incremental ROIC", "$125bn 자본 추가에도 이익증가가 작다.", "현금 포함 자본이 영업에 투입됨", "순현금 제외·무형투자 조정 ROIC가 높음", "측정분모가 잘못돼 경제적 ROIC를 과소평가했다.", "계산 오류"),
             ("$60 청산가치", "혁신 부재와 자기잠식으로 영업이익이 2021년까지 45% 감소한다.", "ASP·Services·buyback이 unit 감소를 못 막음", "EPS·FCF/주 증가", "영업이익·주가 모두 반대로 움직였다.", "치명적 실패"),
         ],
         metrics=[("산업 profit share", "103.6%", "평균회귀", "절대이익 유지", "오판"), ("목표가", "$60", "-50%", "분할 전 환산 $737.6", "실패"), ("Services", "$24.3bn FY2016", "moat 약화", "$85.2bn FY2023", "반증"), ("가격", "$30 조정", "하락", "$184.40", "치명적 실패")],
         timeline=[("2017-11-03", "FY2017 Services 23% 성장", "핵심 반증"), ("2018-09-29", "EPS·Services 확대", "청산 가정 추가 훼손"), ("2020-08-31", "4대1 분할", "가격비교 조정"), (ASOF, "평가기준일", "숏 thesis 파괴")]),

    dict(id="98c51824-0571-4de6-adc3-ebd5a9daab84", date="2020-08-30", ticker="AAPL", company="Apple", author="mip14", source_short=1, direction="Short", link=None, dchars=4947, cchars=281,
         title="34배 이익·App Store 규제·버블 숏", security="보통주 숏", verdict="실패", score=5.0, process=6.1,
         thesis="분할 전 약 $500·forward P/E 34배에서 스마트폰은 무성장이고 FY2015 EBIT $82bn을 FY2021~22에야 넘는다고 봤다. 세제와 buyback의 EPS tailwind가 약해졌고 $100bn buyback도 주식수를 4~5%만 줄인다. Epic 분쟁으로 App Store 수수료가 낮아지면 이익에 직격이며, 7% WACC·3% 영구성장·2023 매출 $330bn·EBIT margin 30% DCF도 TEV $1.9tn이라 30~40% 하락을 기대했다.",
         actual="2022년 금리·공급망 충격 때 일시적 drawdown은 있었지만 2024-01-31 $184.40(2020 분할조정 진입 약 $125)으로 약 47% 높았다. FY2023 매출 $383.3bn은 원문의 $330bn을 넘었고 Services와 높은 gross margin이 지속됐다. App Store 규제위험은 현실이었으나 현금흐름 훼손의 시기·크기가 숏 촉매가 되지 못했다.",
         why="밸류에이션과 규제 취약점은 유효했지만 ‘비싸다’와 ‘실적이 하향돼 주가가 지속 하락한다’ 사이의 촉매가 없었다. 높은 multiple이 설치기반의 질·저금리·서비스 mix를 반영하는 정도와 earnings upside를 별도 시나리오로 두지 않았다.", root="valuation-only 숏에 earnings·촉매·손실상한을 연결하지 못함", first="FY2021 EBIT와 매출이 예상보다 빠르게 사상최고 갱신", first_date="2021-10-28",
         valuation="34x forward P/E; DCF TEV $1.9tn", stock="분할조정 약 $125→$184.40; 숏 가격손실 약 -47%", current="규제는 계속되지만 2024 기준일까지 서비스·설치기반 현금흐름이 배수축소를 상쇄했다.",
         claims=[
             ("무성장", "스마트폰 포화로 Apple EBIT가 장기간 정체한다.", "Services·ASP가 unit 정체를 못 상쇄", "매출·EBIT가 2015 고점을 빠르게 초과", "FY2021 EBIT가 고점을 크게 넘었다.", "실패"),
             ("buyback 한계", "$100bn 매입도 주식수 4~5% 감소라 성장동력이 아니다.", "영업이익 정체와 고가매입", "FCF 성장과 반복매입", "buyback 단독이 아니라 earnings와 함께 per-share 가치를 높였다.", "부분"),
             ("App Store 규제", "수수료 인하는 거의 전액 이익감소다.", "정책변화가 큰 폭 take-rate 하락으로 연결", "소폭 변경·다른 Services 성장으로 흡수", "위험은 현실이나 2024까지 thesis 크기의 손실은 없었다.", "부분 적중"),
             ("배수축소", "34배는 역사적 범위를 벗어나 30~40% 하락한다.", "실적상향보다 discount-rate 충격이 큼", "EPS 상향과 질적 rerating", "2022 조정은 있었지만 종착가격은 더 높았다.", "실패"),
         ],
         metrics=[("forward P/E", "34x", "역사적 평균회귀", "높은 배수 지속", "실패"), ("2023 매출", "$330bn 가정", "DCF", "$383.3bn", "상향 반증"), ("App Store", "수수료 압력", "이익 직격", "위험 현실·손익 제한", "부분"), ("가격", "$125 조정", "30~40% 하락", "$184.40", "실패")],
         timeline=[("2021-10-28", "FY2021 사상최고 실적", "무성장 가정 반증"), ("2022-12-30", "금리충격 drawdown", "숏의 일시적 수익구간"), ("2023-11-03", "FY2023 Services 성장", "지속 하락 촉매 부재"), (ASOF, "평가기준일", "진입가보다 약 47% 상승")]),

    dict(id="c54f5c09-3939-4436-b6dc-3b752108c602", date="2009-01-06", ticker="GOOG", company="Alphabet", author="jna341", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/GOOGLE/4973683011", dchars=27655, cchars=229,
         title="Search 본업가치와 무료옵션 롱", security="보통주", verdict="초대형 성공", score=9.3, process=9.1,
         thesis="$328에서 순현금 조정 forward P/E 15.7배로 지배적 Search만으로도 가치가 있고 Display·Mobile/Local·YouTube·Apps·Android는 무료옵션이라고 봤다. 2008 총매출 약 $21.7bn·순매출 $15.7bn, 검색 비중 97%, 글로벌 query share 약 64%, 순매출 기준 EBIT margin 약 45%를 제시하며 경기침체에도 측정가능한 ROI의 검색광고가 견조하다고 주장했다.",
         actual="2009 경기침체에도 Google은 성장·현금창출을 유지했고 mobile 검색, Android, YouTube가 거대 플랫폼으로 발전했다. 2009년 1월 분할조정 월말가격 약 $8.36에서 2024-01-31 $141.80으로 약 17배가 됐다. Search floor와 무료옵션 프레임 모두 성공했다.",
         why="불황 민감도를 광고총액이 아니라 광고주의 측정가능한 ROI와 경매경제성으로 분석했다. 본업가치와 option을 분리해 옵션 실패에도 하방이 남았다. 다만 YouTube·mobile의 비용과 규제는 당시 충분히 가격화하지 않았다.", root="장기 규제·TAC와 옵션 투자비 과소평가; 핵심 논지는 정확", first="2009년 침체 중에도 매출·영업현금흐름 증가", first_date="2010-02-12",
         valuation="순현금 조정 15.7x forward EPS", stock="분할조정 $8.36→$141.80, 가격수익 약 +1,596%", current="Search는 여전히 핵심 이익원이고 YouTube·Cloud·Android가 배포와 성장축으로 현실화됐다.",
         claims=[
             ("Search moat", "데이터·알고리즘·광고주 경매가 winner-take-most 구조를 만든다.", "query share·광고 ROI 유지", "Bing 등 경쟁자가 share와 monetization 동시 추월", "검색 지배력과 margin이 장기 유지됐다.", "적중"),
             ("불황 회복력", "검색은 측정가능한 ROI라 전통광고보다 recession에 강하다.", "광고주가 성과형 예산을 우선 보존", "CPC·paid click 동시 급락", "2009년에도 매출과 현금이 성장했다.", "적중"),
             ("무료옵션", "YouTube·Mobile·Android 등은 현재가격에 거의 반영되지 않았다.", "사용량을 광고·배포로 monetization", "투자비만 누적되고 수익화 실패", "여러 옵션이 수십억달러 사업이 됐다.", "적중"),
             ("가격규율", "Search 단독가치가 현재 EV를 설명한다.", "본업 이익과 현금전환 지속", "검색 margin 구조적 하락", "낮은 진입배수가 장기 하방을 제공했다.", "적중"),
         ],
         metrics=[("forward P/E", "15.7x ex-cash", "Search floor", "장기 이익복리", "적중"), ("검색 비중", "매출 97%", "지배력 유지", "핵심 이익원 유지", "적중"), ("query share", "약 64%", "상승/유지", "global leader", "적중"), ("가격", "$8.36 조정", "상승", "$141.80", "초대형 성공")],
         timeline=[("2009-12-31", "침체기 실적 방어", "불황 가정 확인"), ("2010-02-12", "영업현금 $9.3bn 공시", "현금창출 확인"), ("2015-08-10", "Alphabet 개편", "옵션 분리 시작"), (ASOF, "평가기준일", "Search+옵션 모두 성공")]),

    dict(id="9745cc55-b68d-4107-b3ed-db15308f3d41", date="2011-06-01", ticker="GOOG", company="Alphabet", author="olivia08", source_short=1, direction="Long", link="https://www.valueinvestorsclub.com/idea/GOOGLE_INC/3254385460", dchars=4631, cchars=33,
         title="12.5배 EBIT의 검색 moat 롱", security="보통주", verdict="매우 성공", score=9.1, process=8.7,
         thesis="$525.60, 순현금 조정 EV $139.9bn에서 Q1 EBIT $2.796bn 연율의 12.5배를 지불한다고 계산했다. 매출 +27%, EBIT margin 33%, 이익의 100% 현금전환, 100%+ ROIC와 시장가치 20%의 순현금을 강조했다. 2013 EPS $40~45·현금 $200/주로 2~3년 목표 $875+, YouTube·Android를 무료옵션으로 봤다.",
         actual="검색광고와 mobile 전환, YouTube·Android는 성장했고 2013 목표 $875는 기간 안팎으로 달성됐다. 영업비 지출 변동성은 있었지만 2011 영업현금은 $14.6bn으로 확대됐다. 분할조정 약 $13에서 2024-01-31 $141.80으로 약 10.9배가 됐다.",
         why="Microsoft의 실제 손실을 대체비용 증거로 사용하고, 낮은 EV/EBIT·현금전환과 성장률을 연결했다. 당장 촉매가 없음을 인정하면서도 이익복리가 시간을 촉매로 만들었다. 반독점과 배포비 위험을 낮게 본 것은 약점이다.", root="반독점·mobile TAC와 경영진 지출위험 과소평가", first="2011 영업현금 $14.6bn과 검색 성장 지속", first_date="2012-02-08",
         valuation="12.5x EV/연율 EBIT; 2~3년 $875+", stock="분할조정 약 $13→$141.80, 가격수익 약 +990%", current="규제비용은 커졌지만 검색·YouTube·Cloud의 이익규모가 장기 valuation을 압도했다.",
         claims=[
             ("검색 moat", "수십억달러를 써도 Bing이 적자라는 사실이 moat를 증명한다.", "Google 품질·share·광고주 밀도 유지", "Bing이 수익성과 share를 빠르게 획득", "Search 지배력은 장기 유지됐다.", "적중"),
             ("영업 leverage", "27% 매출성장과 33% EBIT margin이 장기 EPS로 전환된다.", "지출증가가 매출보다 느려짐", "인력·TAC가 성장 전부 흡수", "분기 변동은 있었지만 절대이익은 크게 증가했다.", "적중"),
             ("현금·ROIC", "100% 현금전환·100%+ ROIC와 순현금이 하방이다.", "SBC·capex 조정 후에도 FCF 우수", "현금이 저수익 사업에 소진", "Other Bets 손실에도 Search 현금이 압도했다.", "적중"),
             ("옵션", "YouTube와 Android는 현재배수에 포함되지 않은 upside다.", "mobile·video 사용량 monetization", "앱 중심 인터넷이 검색을 대체", "두 플랫폼이 배포·광고자산이 됐다.", "적중"),
         ],
         metrics=[("EV/EBIT", "12.5x", "rerating", "장기 복리", "적중"), ("매출성장", "+27%", "지속", "규모 대폭 확대", "적중"), ("2013 목표", "$875+", "2~3년", "달성", "성공"), ("가격", "$13 조정", "상승", "$141.80", "매우 성공")],
         timeline=[("2012-02-08", "2011 영업현금 $14.6bn", "현금전환 확인"), ("2013-09-01", "원 목표가격대 도달", "기간가설 대체로 달성"), ("2015-08-10", "Alphabet 개편", "옵션 공시 개선"), (ASOF, "평가기준일", "장기 대폭 성공")]),
]


def sources_for(idea: dict) -> list[tuple]:
    base = list(APPLE_SOURCES if idea["ticker"] == "AAPL" else GOOGLE_SOURCES)
    base[0] = (*base[0][:4], idea["link"], base[0][5])
    if idea["date"] == "2003-04-22":
        base.append(("기업발표", "Apple Launches the iTunes Music Store", "Apple", "2003-04-28", "https://www.apple.com/newsroom/2003/04/28Apple-Launches-the-iTunes-Music-Store/", "VUM 비인수와 디지털 유통전략 확인"))
    if idea["date"] == "2013-02-07":
        base.append(("기업발표", "Apple More than Doubles Capital Return Program", "Apple", "2013-04-23", "https://www.apple.com/newsroom/2013/04/23Apple-More-than-Doubles-Capital-Return-Program/", "$100bn 환원·$60bn buyback 촉매 확인"))
    if idea["date"] == "2015-07-02":
        base.append(("기업발표", "Alphabet Founders' Letter 2015", "Alphabet", "2015-12-31", "https://abc.xyz/investor/founders-letters/2015/", "Alphabet 구조와 Google/Other Bets 분리 확인"))
    return base


def build_payload() -> dict:
    payload = {k: [] for k in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")}
    for idea in IDEAS:
        direction_ko = "숏" if idea["source_short"] else "롱"
        payload["ideas_master"].append({
            "idea_id": idea["id"], "date": idea["date"], "year": int(idea["date"][:4]), "ticker": idea["ticker"],
            "company_name": "APPLE INC " if idea["ticker"] == "AAPL" else "ALPHABET INC ", "author": idea["author"],
            "direction_ko": direction_ko, "is_short": idea["source_short"], "contest_winner": 0,
            "source_link": idea["link"], "description_chars": idea["dchars"], "catalyst_chars": idea["cchars"],
            "narrative_tags_ko": "원본 방향 교정; 심층검증", "idea_type_ko": "기업가치", "performance_available": 0,
            "auto_tag_status_ko": "수동 심층검증"
        })
        desc = APPLE_DESC if idea["ticker"] == "AAPL" else GOOGLE_DESC
        success = "valuation_discipline; business_model; ecosystem; capital_allocation" if "성공" in idea["verdict"] else "risk_identification"
        failure = "causal_attribution; opportunity_cost" if "성공" in idea["verdict"] else "valuation_only_short; catalyst_gap; ecosystem_misread; timing_path"
        analyst = f"원 SQL에는 source_is_short=true로 저장됐으나 본문·추천증권·목표수익상 실제 방향은 {idea['direction']}이다. 원본 flag는 보존하고 research_direction만 교정했다. 가격수익은 후속 주식분할을 조정한 근사치이며 배당은 제외했다."
        payload["postmortems"].append({
            "idea_id": idea["id"], "ticker": idea["ticker"], "research_direction_ko": idea["direction"],
            "company_description_ko": desc, "original_thesis_ko": idea["thesis"], "actual_development_ko": idea["actual"],
            "thesis_verdict_ko": idea["why"], "business_verdict_ko": idea["actual"],
            "catalyst_verdict_ko": idea["first"], "valuation_verdict_ko": idea["valuation"], "stock_verdict_ko": idea["stock"],
            "current_verdict_ko": idea["current"], "overall_verdict_ko": idea["verdict"], "why_ko": idea["why"],
            "success_pattern_ko": success, "failure_pattern_ko": failure, "root_error_ko": idea["root"],
            "first_signal_ko": idea["first"], "first_signal_date": idea["first_date"],
            "knowable_at_t0_ko": "원문의 숫자를 순현금·영업가치·per-share FCF로 재구성하고, unit·ASP·설치기반·서비스·SBC·자사주를 분리하면 당시에도 핵심 성립조건을 점검할 수 있었다.",
            "avoidability_ko": "중간~높음. 사업의 질과 주가방향, 현금과 영업투하자본, valuation과 촉매를 분리하고 사전 반증조건을 정하면 오류를 줄일 수 있었다.",
            "counterfactual_question_ko": idea["claims"][0][3], "analyst_note_ko": analyst,
            "corrected_return_1y": None, "corrected_return_3y": None, "corrected_return_5y": None,
            "confidence": 0.96 if idea["direction"] == "Long" else 0.94, "research_asof": ASOF, "research_status_ko": "외부검증 완료"
        })
        payload["meta"].append({
            "idea_id": idea["id"], "analysis_depth_ko": "기업·증권·논지·실제결과·인과오류·반증조건 심층분석",
            "report_version": "V7-detailed", "thesis_type_ko": idea["title"], "one_line_verdict_ko": idea["why"],
            "thesis_score": idea["score"], "process_score": idea["process"], "return_summary_ko": idea["stock"],
            "core_error_ko": idea["root"], "core_insight_ko": idea["claims"][0][4], "research_asof": ASOF
        })
        section_bodies = [
            desc,
            f"추천 증권은 {idea['security']}, 실제 방향은 {idea['direction']}이다. {idea['thesis']}",
            idea["actual"],
            f"종합판정은 {idea['verdict']}다. {idea['why']} 핵심 오류 또는 남는 한계는 ‘{idea['root']}’이다."
        ]
        for n, (title, body) in enumerate(zip(("기업과 돈 버는 구조", "원 투자논지", "실제 전개", "투자 결론과 학습"), section_bodies), 1):
            payload["sections"].append({"idea_id": idea["id"], "section_order": n, "section_title_ko": title, "section_body_ko": body})
        for n, claim in enumerate(idea["claims"], 1):
            title, original, assumption, falsifier, result, verdict = claim
            payload["claims"].append({
                "idea_id": idea["id"], "claim_order": n, "claim_title_ko": title, "thesis_weight_pct": 25,
                "original_claim_ko": original, "t0_evidence_ko": idea["thesis"], "key_assumption_ko": assumption,
                "ex_ante_falsifier_ko": falsifier, "actual_result_ko": result,
                "quantitative_gap_ko": idea["stock"] if n == 4 else idea["valuation"], "verdict_ko": verdict,
                "analytical_error_ko": idea["root"] if verdict not in {"적중", "정확히 적중", "초과"} else "중대한 오류 없음",
                "reusable_lesson_ko": f"{title}는 주장만 기록하지 말고 ‘{falsifier}’를 사전 체크해야 한다."
            })
        for n, metric in enumerate(idea["metrics"], 1):
            name, t0, expectation, actual, verdict = metric
            payload["metrics"].append({"idea_id": idea["id"], "metric_order": n, "metric_name_ko": name, "t0_value_ko": t0,
                "thesis_expectation_ko": expectation, "actual_value_ko": actual, "verdict_ko": verdict,
                "interpretation_ko": f"{name}: 당시 {t0}, 기대 {expectation}, 실제 {actual}."})
        for n, event in enumerate(idea["timeline"], 1):
            date, name, implication = event
            payload["timeline"].append({"idea_id": idea["id"], "event_order": n, "event_date_ko": date, "event_ko": name, "thesis_implication_ko": implication})
        for n, source in enumerate(sources_for(idea), 1):
            typ, title, publisher, date, url, evidence = source
            payload["sources"].append({"idea_id": idea["id"], "source_order": n, "source_type_ko": typ, "title_ko": title,
                "publisher": publisher, "source_date": date, "url": url, "evidence_ko": evidence})
    return payload


def company_report(company: str, ideas: list[dict]) -> str:
    desc = APPLE_DESC if company == "Apple" else GOOGLE_DESC
    ticker = "AAPL" if company == "Apple" else "GOOG"
    business = (
        "- 하드웨어 gross profit + 설치기반 기반 Services 반복매출\n- 기기·OS·앱·결제·자체칩의 수직통합과 전환비용\n- unit보다 ASP·gross margin·활성기기·Services ARPU·FCF/주가 중요\n- 중국 집중·교체주기·App Store 규제·자본배분이 핵심 위험"
        if company == "Apple" else
        "- 검색·동영상 이용의도를 광고주 경매와 연결해 CPC/CPM 수취\n- TAC·데이터센터·콘텐츠·SBC를 뺀 Search/YouTube 현금이 핵심\n- Android·Chrome은 검색 배포, Cloud는 사용량·구독 사업\n- 진입점 변화·반독점·개인정보·Other Bets 손실이 핵심 위험"
    )
    lines = [f"# {company} ({ticker}) — 기업과 비즈니스", "", desc, "", "## 돈을 버는 구조", "", business, "", "## 아이디어 전체 판정", "", "| 게시일 | 원 SQL | 실제 방향 | 추천 증권 | 핵심 논지 | 실제 결과 | 종합판정 |", "|---|---|---|---|---|---|---|"]
    for i in ideas:
        lines.append(f"| {i['date']} | Short | {i['direction']} | {i['security']} | {i['title']} | {i['stock']} | {i['verdict']} |")
    for number, idea in enumerate(ideas, 1):
        lines += ["", f"## {number}. {idea['date']} — {idea['title']}", "", f"**추천 증권·방향:** {idea['security']} {idea['direction']}", "", "### 원 투자논지", "", idea["thesis"], "", "### 논지를 구성한 핵심 주장", ""]
        for n, c in enumerate(idea["claims"], 1):
            lines += [f"#### {n}. {c[0]} — {c[5]}", "", f"**핵심 주장:** {c[1]}", "", f"**이 주장이 성립하려면:** {c[2]}", "", f"**사전 반증조건:** {c[3]}", "", f"**실제 결과:** {c[4]}", ""]
        lines += ["### 논지 구조와 검증", "", "| 축 | 당시 주장 | 실제 검증 |", "|---|---|---|",
                  f"| 사업·단위경제성 | {idea['thesis']} | {idea['actual']} |",
                  f"| 밸류에이션·청구권 | {idea['valuation']} | {idea['stock']} |",
                  f"| 촉매·시간 | {idea['first']} | 첫 확인일 {idea['first_date']} |",
                  f"| 사전 반증조건 | {idea['claims'][0][3]} | 핵심 오류: {idea['root']} |", "",
                  "### 실제 전개와 투자 결론", "", idea["actual"], "", f"**종합판정: {idea['verdict']}.** {idea['why']}", "", "### 핵심 수치", "", "| 지표 | 글 당시 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
        for m in idea["metrics"]:
            lines.append(f"| {m[0]} | {m[1]} | {m[2]} | {m[3]} | {m[4]} |")
        lines += ["", f"재사용 질문: **{idea['claims'][0][3]}**"]
    lines += ["", f"## {ASOF} 기준 기업 결론", ""]
    if company == "Apple":
        lines.append("Apple 사례는 같은 기업도 가격·시점·인과에 따라 정반대 결과가 난다는 점을 보여준다. 2000·2003년은 순현금 가격으로 미예측 혁신옵션을 샀고, 2011·2013·2016년은 TAM·생태계·Services·buyback을 점점 더 정확히 포착했다. 2017년 숏은 현금을 영업투하자본에 넣는 ROIC 오류와 unit 중심 사고로 치명적으로 실패했다. 2020년 숏은 valuation·규제 위험을 맞혔지만 실적 하향과 시간촉매가 없어 실패했다.")
    else:
        lines.append("세 Google 롱은 모두 Search 본업가치가 가격을 지지하고 YouTube·Android·Cloud를 무료 또는 저가 option으로 받는 구조였다. 2009년에는 recession 회복력, 2011년에는 moat와 현금전환, 2015년에는 숨은 사업과 자본배분 촉매가 중심이었다. 규제·TAC·SBC를 과소평가했지만 낮은 본업배수와 실제 옵션 monetization이 오류를 압도했다.")
    lines += ["", "## 주요 근거", ""]
    unique = []
    for idea in ideas:
        for s in sources_for(idea):
            if s[4] and (s[1], s[4]) not in unique: unique.append((s[1], s[4]))
    for title, url in unique:
        lines.append(f"- [{title}]({url})")
    return "\n".join(lines)


def build_report() -> str:
    apples = sorted((x for x in IDEAS if x["ticker"] == "AAPL"), key=lambda x: x["date"])
    googles = sorted((x for x in IDEAS if x["ticker"] == "GOOG"), key=lambda x: x["date"])
    head = f"""# Batch 011 — Apple·Google/Alphabet 10건

평가기준일: {ASOF}

분석일: {ANALYSIS_DATE}

대상: Apple 7건·Google/Alphabet 3건

## 결론부터

이번 10건은 **좋은 기업/나쁜 기업이라는 고정 라벨보다, 어느 가격에 어떤 청구권을 사고 어떤 인과를 전제로 했는지가 결과를 결정한다**는 사례다. Apple의 다섯 롱과 Google의 세 롱은 대체로 매우 성공했지만 성공 이유의 정확도는 다르다. Apple 2017 숏은 생태계와 ROIC를 잘못 측정해 치명적으로 실패했고, 2020 숏은 valuation·규제 위험은 포착했어도 실적하향 촉매가 없어 실패했다.

| 기업 | 건수 | 가장 강한 성공 | 가장 큰 실패 | 반복 학습 |
|---|---:|---|---|---|
| Apple | 7 | 2003 VUM 비인수·iTunes 롱, 2016 Services 롱 | 2017 느린 청산 숏 | unit·당기 margin과 설치기반·per-share FCF를 분리 |
| Google/Alphabet | 3 | 2009 Search floor+무료옵션, 2015 YouTube·Cloud | 치명적 실패 없음 | core 가치와 option을 분리해 option에 과지불하지 않기 |

> 데이터 경고: SQL은 10건 모두 `is_short=true`이나 원문상 실제 방향은 Apple 5 Long·2 Short, Google 3 Long이다. 원본 flag는 감사추적용으로 보존하고 research_direction만 교정했다. 장기가격은 후속 주식분할을 조정한 근사치이며 배당은 제외했다.

---
"""
    tail = """

---

# 배치 공통 패턴과 DB 학습 태그

| 패턴 | 성공/실패 메커니즘 | 적용 아이디어 |
|---|---|---|
| 순현금+옵션 | 본업을 낮게 사고 미예측 혁신의 upside를 보유 | Apple 2000·2003 |
| ecosystem economics | unit share보다 설치기반·ASP·서비스·개발자 monetization이 중요 | Apple 2011·2016, Google 전부 |
| stress valuation | margin 하락을 숫자로 넣고도 equity가 남는지 확인 | Apple 2013 |
| core+free option | Search 단독가치와 YouTube·Android·Cloud를 분리 | Google 2009·2011·2015 |
| ROIC denominator error | 무수익 현금을 영업투하자본에 넣으면 질 좋은 사업이 나빠 보임 | Apple 2017 Short |
| valuation-only short | 비싼 배수만으로는 하락의 크기·시기·손실상한이 정해지지 않음 | Apple 2020 Short |

핵심 학습 태그: `net_cash_option`, `ecosystem`, `installed_base`, `services_mix`, `unit_to_fcf`, `capital_return`, `core_plus_option`, `valuation_only_short`, `roic_denominator`, `catalyst_gap`, `timing_path`.

# 데이터 품질·방법론

- 평가기준일은 2024-01-31로 고정했다. 그 이후 실적과 가격은 판정에 사용하지 않았다.
- VIC 원문에 없는 정확한 1·3·5년 수익률을 만들지 않았다. 장기 종착가격은 공식 분할을 반영한 근사 비교로만 제시했다.
- 성공 판정은 주가방향, 사업인과, 밸류에이션, 촉매·시간을 분리했다. 장기 주가가 올라도 원문이 예측하지 않은 제품이 원인이면 인과 일부 오류로 남겼다.
- 회사 공시와 기업발표를 사업결과의 우선 근거로, 가격 데이터는 별도 역사자료로 교차검증했다.
"""
    return head + company_report("Apple", apples) + "\n\n---\n\n" + company_report("Alphabet", googles) + tail


def main() -> None:
    payload = build_payload()
    report = build_report()
    json_path = ROOT / "data" / "curated" / "batch_011_apple_google_deep_v7.json"
    md_path = ROOT / "analysis" / "batch_011_apple_google_10.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(report, encoding="utf-8")
    print({k: len(v) for k, v in payload.items()})
    print({"report_chars": len(report), "json": str(json_path), "markdown": str(md_path)})


if __name__ == "__main__":
    main()
