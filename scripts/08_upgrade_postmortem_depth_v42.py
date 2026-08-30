from pathlib import Path
import json, sqlite3, gzip, shutil

ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'data'/'processed'/'vic_dashboard.db'
CUR=ROOT/'data'/'curated'

def one(s):
    return ' '.join(s.strip().split())

# V4.2의 핵심: 짧은 요약형 사후분석을 긴 리서치 노트 + 정량 스냅샷 + 타임라인으로 확장.
LONG={
'WCC': dict(
 one_line_ko='2020년 WESCO는 Anixter 인수 직후 높은 레버리지 때문에 사실상 “통합 실패 가능성”이 가격에 반영된 종목이었다. VIC 롱의 핵심은 인수 자체가 아니라 3년 안에 시너지·FCF·디레버리징이 동시에 나타날 것이라는 베팅이었다.',
 business_economics_ko='WESCO는 전기·통신·유틸리티·산업재 유통업체다. 제조업체와 고객 사이에서 재고, 납기, 기술영업, 공급망을 대신 관리한다. 유통업이라 매출총이익률 자체는 높지 않지만 규모가 커질수록 구매조건, 물류망, SG&A 중복 제거에서 이점이 생긴다. 따라서 대형 M&A의 성패는 “매출이 늘었는가”보다 조달·물류·백오피스 시너지가 EBITDA 마진과 현금흐름으로 실제 전환되는지가 핵심이다.',
 valuation_at_t0_ko='VIC는 2023년 기본 시나리오 FCF를 약 3.44억달러로 잡고 10% FCF yield를 적용해 주당 약 $69, 당시 대비 약 +175%를 제시했다. 경영진의 더 공격적인 2023년 FCF 6억달러가 실현되면 같은 10% FCF yield에서 주당 약 $120, +380%가 가능하다고 봤다. 반대편 tail risk는 명시적으로 “통합 실패와 과도한 부채로 equity가 0이 되는 경우”였다.',
 stock_return_summary_ko='원 VIC 성과 DB 기준 1년 롱 수익률은 +287.3%였다. 회사가 제시한 Anixter 인수 종결 이후 2023년 말까지 TSR도 353%로, 단순 멀티플 반등이 아니라 통합 실적과 레버리지 하락이 주가 재평가를 동반했다.',
 earnings_bridge_ko='인수 후 매출 규모 확대 → 구매력·SG&A 시너지 → 조정 EBITDA와 마진 상승 → FCF 창출 → 순레버리지 하락 → 파산/증자 tail risk 축소 → equity multiple 재평가의 순서로 작동했다.',
 what_was_right_ko='가장 어려운 가정이었던 “대형 인수 후 실제 시너지”와 “높은 부채를 FCF로 낮출 수 있다”가 둘 다 맞았다. 2023년 독립 양사 대비 조정 EBITDA가 89% 늘고 마진이 240bp 개선됐으며 순레버리지가 2.8배까지 낮아진 것이 핵심 검증이다.',
 what_was_wrong_ko='결과가 매우 좋았지만 전부 구조적 시너지로 볼 수는 없다. 유통·산업 경기와 가격 환경의 도움도 있었기 때문에, 이후에는 유기적 성장과 시너지 제거 후 정상화 마진을 따로 볼 필요가 있다.',
 lesson_ko='레버리지 M&A는 “부채가 많다”만으로 피할 게 아니라 ① 통합 후 FCF bridge ② 시너지의 출처 ③ working capital 정상화 ④ 부채 만기와 금리 ⑤ 실패 시 희석 가능성을 숫자로 분해해야 한다.',
 current_watch_ko='향후에는 인수 시너지 종료 뒤 organic growth, EBITDA margin 유지력, 순레버리지, 추가 대형 M&A가 다시 재무위험을 키우는지 확인하는 것이 중요하다.'),
'BXC': dict(
 one_line_ko='BlueLinx 롱은 “목재가격이 오른다”는 단순 사이클 베팅이 아니라, 극저마진 2-step 유통업체가 부동산 현금화·부채상환·가격/믹스 개선을 통해 정상 마진으로 이동할 수 있다는 self-help 아이디어였다.',
 business_economics_ko='BlueLinx는 건축자재 제조사와 딜러·홈센터 사이의 2-step distributor다. 2018년 VIC 글 기준 39개 물류센터에서 1만개 이상의 SKU를 다뤘다. 고객이 직접 대량재고를 보유하기 싫어한다는 점을 이용해 저장공간, 운전자본, 소량배송, 주문관리 기능을 제공한다. 이 모델은 낮은 마진 대신 재고회전과 규모가 경제성을 결정한다.',
 valuation_at_t0_ko='VIC는 당시 표면상 레버리지가 8배 이상으로 보였지만 보유 부동산의 장부가 대비 잠재가치가 약 2.5억달러 높다고 봤다. 실제 직전 4개 부동산 sale-leaseback에서 1.10억달러를 받아 9,800만달러 고금리 모기지를 상환했다. 글쓴이는 self-help가 진행되면 몇 년 뒤 P/E가 약 3배에 불과할 수 있다고 주장했다.',
 stock_return_summary_ko='원 VIC 성과 DB 기준 롱 수익률은 1년 +111.7%, 3년 +193.1%, 5년 +529.2%였다. 다만 2020~2021 목재가격 급등이 실적을 크게 증폭했기 때문에 주가 성과 전부를 구조개선만의 결과로 해석하면 안 된다.',
 earnings_bridge_ko='부동산 현금화 → 부채감축 → 이자비용/재무위험 감소와 동시에 가격·믹스·운영효율 개선 → EBITDA margin 상승 → 강한 목재/주택 사이클이 증폭기 역할을 했다.',
 what_was_right_ko='저마진 구조가 고정된 것이 아니라는 판단과 hidden real estate가 실제 deleveraging 수단이라는 판단이 맞았다. 2020년 5.5%였던 조정 EBITDA 마진은 2021년 10.8%로 상승했고 순레버리지는 3.5배에서 1.1배로 낮아졌다.',
 what_was_wrong_ko='실적 개선 규모에는 lumber inflation과 주택경기 호황이 크게 섞였다. 따라서 peak EBITDA를 그대로 정상화 earnings로 자본화했다면 이후 사이클에서 오류가 발생했을 것이다.',
 lesson_ko='사이클 기업의 turnaround에서는 “self-help로 개선된 부분”과 “가격 사이클이 준 일시적 이익”을 분리해야 한다. 마진 개선이 가격 정상화 뒤에도 남는지가 진짜 구조개선이다.',
 current_watch_ko='목재·건축자재 가격 정상화 구간의 EBITDA margin, 재고손익, 순레버리지, 부동산/자본배분을 계속 분리해서 봐야 한다.'),
'WOR': dict(
 one_line_ko='Worthington 아이디어는 본업보다 Nikola 지분이라는 숨은 자산과 lock-up 계약의 실제 조항을 읽어 시장이 과소평가한 현금화 시점을 잡아낸 이벤트 드리븐 투자였다.',
 business_economics_ko='Worthington은 철강가공·실린더·건축제품 등 여러 산업재 사업과 JV를 보유한 복합기업이었다. 이 아이디어의 알파는 본업 예측보다 2015년 $2m 초기투자로 확보한 Nikola 지분이 2020년 상장 뒤 기업가치의 매우 큰 비중이 되었는데도 주가에 충분히 반영되지 않았다는 데 있었다.',
 valuation_at_t0_ko='2020년 6월 VIC 글 기준 WOR 시가총액은 약 18.3억달러, 보유 Nikola 19,048,020주의 시장가치는 주당 $64 기준 약 12억달러로 시총의 약 66%였다. 시장은 180일 lock-up을 크게 걱정했지만 실제 계약에는 7월 3일부터 500만주, 9월 1일부터 추가 700만주를 매각할 수 있는 예외가 있었다.',
 stock_return_summary_ko='원 DB 1년 롱 수익률은 +73.6%였다. 더 중요한 것은 Nikola 가치가 단순 장부상 자산으로 남은 것이 아니라 FY2021 중 실제 현금화되어 6.551억달러의 세전 이익으로 바뀌었다는 점이다.',
 earnings_bridge_ko='숨은 지분가치 발견 → lock-up 문구 정밀해석 → 예상보다 빠른 일부 매각 → 시장이 “가치가 있지만 못 파는 자산”에서 “현금화 가능한 자산”으로 재평가하는 이벤트 경로였다.',
 what_was_right_ko='가장 차별화된 부분은 Nikola 주가 방향을 맞힌 것이 아니라 공개 계약서의 unlock schedule을 시장보다 정확히 읽은 것이다. 2020년 7월 실제 500만주 매각으로 핵심 가정이 빠르게 검증됐다.',
 what_was_wrong_ko='Nikola 자체의 장기 사업가치를 보유했다면 전혀 다른 결과가 될 수 있었다. 이 사례의 성공은 “Nikola가 좋은 회사였다”가 아니라 “WOR가 당시 고평가된 지분을 실제로 현금화할 수 있었다”는 이벤트 성공이다.',
 lesson_ko='이벤트 투자에서는 headline이 아니라 계약서·락업·세금·실제 매도가능 물량을 읽어야 한다. 자산가치와 현금화가능가치는 별개의 변수다.',
 current_watch_ko='유사 사례에서는 지분가치보다 처분제약, 세금누수, 헤지 가능성, 경영진의 자본배분 계획을 우선 확인해야 한다.'),
'KKR': dict(
 one_line_ko='KKR 롱은 대체자산운용사를 경기민감한 carry business가 아니라, 8~12년 잠긴 자본에서 관리보수를 받고 capital markets·balance sheet까지 겹쳐 수익원을 복리화하는 플랫폼으로 본 아이디어였다.',
 business_economics_ko='전통 mutual fund는 환매가 빠르게 일어나지만 private equity·infrastructure 등은 약정기간이 길다. 투자기간에는 committed capital에, 회수기간에는 invested cost에 관리보수가 붙어 시장가격 변동이 fee base에 즉시 반영되지 않는다. KKR은 여기에 자체 capital markets와 대차대조표 투자를 더해 하나의 딜에서 관리보수·carry·syndication fee·자기자본수익을 여러 층으로 회수한다.',
 valuation_at_t0_ko='VIC는 2019년 KKR의 fee stream과 약 145억달러의 balance-sheet cash/investments를 분리해 봤고, book value를 조정하면 peer 대비 fee yield가 약 5배 높다고 주장했다. 당시 핵심은 단기 P/E가 아니라 “AUM 17~26% 성장, 장기 fee visibility, 자체 자본 복리”를 상대적으로 싼 가격에 산다는 것이었다.',
 stock_return_summary_ko='원 DB 기준 1년 +29.0%, 3년 +178.0%였다. 사업적으로는 AUM이 2019년 약 2,180억달러에서 2024년 6,380억달러로 약 3배가 되어 연평균 약 24% 증가했다.',
 earnings_bridge_ko='기관의 alternatives allocation 확대 → AUM/fee-paying AUM 증가 → management fee와 FRE 증가 → capital markets·insurance·balance sheet가 추가 earnings layer를 제공 → 규모가 다시 fundraising과 sourcing 우위를 강화했다.',
 what_was_right_ko='대체자산의 구조적 점유율 상승과 lock-up fee의 가시성, KKR만의 capital markets/대차대조표가 단순 옵션이 아니라 실제 이익원이라는 판단이 맞았다. 2024년 관리보수 35억달러, FRE 33억달러, ANI 42억달러가 이를 보여준다.',
 what_was_wrong_ko='이 모델도 자산가격·fundraising cycle·실현 carry에 영향을 받는다. “AUM이 늘면 무조건 같은 질의 이익”이라고 보면 fee rate mix와 보험자본 비중, carry 변동성을 놓칠 수 있다.',
 lesson_ko='자산운용사는 AUM 숫자 하나보다 fee-paying AUM, perpetual/long-duration capital, fee rate, FRE margin, carry 의존도와 balance-sheet risk를 분해해야 한다.',
 current_watch_ko='향후 핵심은 AUM 성장보다 fee-related earnings per share의 성장, 보험자본 조달비용, realizations/carry와 주식보상·희석이다.'),
'BX': dict(
 one_line_ko='Blackstone 아이디어는 2015~2016 신용시장 공포로 눌린 대체자산 플랫폼을 “장기 잠금 AUM + 반복 fee + carry”의 합으로 가치평가한 장기 복리 투자였다.',
 business_economics_ko='Blackstone의 강점은 단순 투자성과가 아니라 브랜드·트랙레코드·기관 LP 관계를 이용해 장기자금을 반복적으로 모집하는 데 있다. 장기간 환매가 제한된 자본은 시장 변동이 와도 fee base가 갑자기 사라지지 않고, 규모가 커질수록 상품군·딜 소싱·운영인력에 고정비 레버리지가 생긴다.',
 valuation_at_t0_ko='VIC는 SOTP로 recurring FRE 약 $20/unit, 기존 carry 약 $17, net corporate cash/liquid investments 약 $2를 합쳐 기본 fair value를 약 $40로 봤다. 기본 가정은 AUM이 과거 20%대에서 둔화하더라도 fee growth가 10%→8% 수준으로 장기간 이어진다는 것이었다.',
 stock_return_summary_ko='원 DB 기준 1년 +34.1%, 3년 +99.6%, 5년 +454.3%였다. 총 AUM은 2016년 3,670억달러에서 2025년 약 1.3조달러로 증가해 약 15% CAGR을 기록했다.',
 earnings_bridge_ko='장기자본 유입 → fee-earning AUM 증가 → 반복 FRE 증가 → 펀드성과가 좋을 때 carry 추가 → 제품군 확대와 브랜드 강화 → 다시 fundraising 우위로 연결되는 flywheel이었다.',
 what_was_right_ko='시장 공포가 fee base의 구조적 훼손을 의미하지 않는다는 판단이 정확했다. AUM이 세 배 이상 늘면서 “신용시장 불안 때문에 장기 성장률이 끝났다”는 당시 우려가 틀렸음이 확인됐다.',
 what_was_wrong_ko='장기 성공과 별개로 BX의 수익은 완전히 annuity가 아니다. realizations와 performance revenue는 자산시장에 민감하므로 FRE와 carry를 같은 멀티플로 볼 수 없다.',
 lesson_ko='대체자산운용사는 recurring fee와 performance fee를 분리해 평가해야 하며, 시장 급락 때 “AUM mark-down”과 “fee-paying capital의 실제 이탈”을 혼동하지 않는 것이 중요하다.',
 current_watch_ko='현재는 대형화된 AUM에서 fee rate가 희석되는지, private wealth·insurance가 성장률을 유지하는지, FRE/share가 계속 복리되는지를 봐야 한다.'),
'TMO': dict(
 one_line_ko='Thermo Fisher 롱은 2008~2009 경기침체가 산업장비·학술연구 수요를 때릴 때, 시장이 반복 consumables/service와 비용유연성을 과소평가해 약 10% FCF yield까지 할인했다고 본 quality-at-a-discount 투자였다.',
 business_economics_ko='Thermo Fisher는 연구·진단 장비, 소모품, 서비스, 바이오프로세싱 등을 제공한다. 장비 판매는 경기민감하지만 설치기반이 커질수록 consumables와 service가 반복되며 고객 workflow 안에 깊이 들어간다. 이후 대형 M&A를 통해 제품군을 넓히며 “one-stop shop”과 교차판매를 강화했다.',
 valuation_at_t0_ko='VIC는 당시 약 10% FCF yield가 사실상 매출성장과 마진개선을 거의 인정하지 않는 가격이라고 봤다. 2008년 경영진의 4~6% organic growth와 연 100bp margin expansion 목표가 완전히 실현되지 않더라도, 마진을 유지하거나 소폭 개선할 수 있으면 충분한 upside가 있다는 논리였다.',
 stock_return_summary_ko='원 DB 기준 1년 +33.9%, 3년 +29.5%, 5년 +215.4%였다. 초기 몇 년 주가가 직선으로 오른 것은 아니지만 사업의 FCF와 M&A 복리구조가 장기적으로 크게 평가받았다.',
 earnings_bridge_ko='경기민감 장비 수요의 하방보다 consumables/service의 반복성이 컸고 → 비용절감과 포트폴리오 mix로 margin 방어 → Life Technologies 같은 M&A가 매출·마진을 동시에 확대 → 현금흐름 성장과 멀티플 정상화가 결합했다.',
 what_was_right_ko='“침체가 매출 일부를 때려도 전체 economics가 붕괴하지 않는다”는 품질 판단이 맞았다. 2014년 Life Technologies 반영 후 매출은 168.9억달러(+29%), 조정 EPS +28%, 조정 영업마진 21.9%(+240bp)를 기록했다.',
 what_was_wrong_ko='초기 thesis는 경기방어에 초점이 컸지만 장기 초과수익의 상당 부분은 이후 훨씬 큰 M&A 플랫폼과 바이오제약 노출 확대에서 나왔다. 즉 결과가 원 thesis보다 더 좋은 방향으로 진화했다.',
 lesson_ko='quality 기업이 경기우려로 싸질 때는 매출의 경기민감 비중만 보지 말고 설치기반, 소모품·서비스 비중, FCF 전환, 비용유연성을 함께 봐야 한다.',
 current_watch_ko='현재는 바이오프로세싱 사이클, 대형 M&A ROIC, organic growth와 FCF conversion이 장기 평균으로 회귀하는지를 봐야 한다.'),
'DPZ': dict(
 one_line_ko='Domino’s 롱은 피자 매출 성장보다 프랜차이즈 로열티를 “자본투입이 거의 없는 임대료 같은 현금흐름”으로 보고, 국제 점포 확장과 동일점매출이 이 반복수익을 복리화한다고 본 아이디어였다.',
 business_economics_ko='Domino’s는 가맹점 매출에서 로열티를 받고, 공급망을 통해 도우·식재료·장비를 판매하며 일부 직영점을 운영한다. VIC는 당시 연간 약 1.6억달러의 franchise fee 중 이를 유지하는 비용을 약 4,000만달러로 봐, 약 1.2억달러를 높은 질의 반복 현금흐름처럼 해석했다. 가맹점이 자본을 투입해 점포를 늘리므로 본사 성장의 자본집약도가 낮다.',
 valuation_at_t0_ko='글 작성 당시 다음해 FCF 약 8,500만달러를 기준으로 equity FCF yield 약 8.5%, 전체 자본구조는 약 11.6x EBIT로 계산했다. 투자자는 성장·멀티플 확장·잠재 buyout 외에도 단기적으로 securitized debt refinancing이 equity overhang을 줄일 것으로 봤다.',
 stock_return_summary_ko='원 DB 기준 1년 +90.1%, 3년 +347.5%, 5년 +601.8%였다. 2016년 미국 동일점매출 +10.5%, 해외 +6.3%, 글로벌 순점포 +1,281개로 반복 로열티 base 자체가 빠르게 확대됐다.',
 earnings_bridge_ko='브랜드/디지털 주문 개선 → 가맹점 unit economics 개선 → 점포 증가와 SSS 상승 → 로열티·공급망 이익 증가 → 낮은 capex로 현금창출 → buyback과 레버리지 자본구조가 EPS를 추가 증폭했다.',
 what_was_right_ko='프랜차이즈 로열티를 단순 음식점 매출이 아니라 high-quality recurring cash flow로 본 점이 핵심이었다. 국제 매장 확대와 SSS가 동시에 강해져 로열티 base가 예상보다 더 빨리 커졌다.',
 what_was_wrong_ko='장기간의 성공에는 2010년대 디지털 주문·브랜드 turnaround라는 요소도 컸다. 단순히 “피자는 불황에도 먹는다”만으로는 같은 결과를 설명할 수 없다.',
 lesson_ko='프랜차이즈 기업은 시스템 sales보다 가맹점 unit economics, 점포당 ROI, 폐점률, 로열티율, 공급망 마진을 봐야 한다. 가맹점이 잘 벌어야 본사도 오래 복리한다.',
 current_watch_ko='점포 성장률, 미국 SSS, 가맹점 수익성, 배달 aggregator와의 경쟁, 높은 부채를 감당할 FCF를 점검해야 한다.'),
'RCL': dict(
 one_line_ko='Royal Caribbean 롱은 Concordia 사고·유럽 불황·고유가로 눌린 크루즈 업종에서, 수요 자체보다 신규 선박 공급증가율이 급격히 둔화한다는 자본사이클 변화를 포착한 아이디어였다.',
 business_economics_ko='크루즈는 초기 선박투자가 매우 크고 신규 공급에 수년이 걸리는 oligopoly다. 2012년 VIC 글 기준 Carnival과 RCL이 세계 passenger capacity의 약 3/4를 차지했다. 단기에는 티켓가격을 낮춰 탑승률을 채울 수 있지만 공급이 줄고 수요가 늘면 Net Yield가 큰 폭으로 개선되어 고정비 구조 때문에 이익 레버리지가 크다.',
 valuation_at_t0_ko='당시 가격은 Concordia 사고와 유럽 경기침체가 장기 구조훼손처럼 반영된 상태였다. VIC는 RCL이 사고 관련 직접 liability가 없고 유럽 노출이 Carnival보다 낮으며, 공급 둔화와 자본규율 개선이 동반되면 밸류에이션이 정상화될 것으로 봤다.',
 stock_return_summary_ko='원 DB 기준 1년 +33.9%, 3년 +163.1%, 5년 +325.1%였다. 2017년 순이익 16억달러, EPS $7.53, ROIC 10%+, constant-currency Net Yield +6.4%로 핵심 사이클 논지가 숫자로 확인됐다.',
 earnings_bridge_ko='신규 선박 공급증가율 둔화 → 수급 개선 → ticket/onboard yield 상승 → 높은 고정비 구조에서 incremental margin 확대 → 부채비율/ROIC 개선 → 멀티플 재평가로 이어졌다.',
 what_was_right_ko='헤드라인 사고와 장기 cruise demand를 분리했고, 수요보다 공급사이클을 핵심 변수로 본 점이 맞았다. 특히 Net Yield가 8년 연속 증가했다는 사실은 공급규율 thesis를 강하게 지지한다.',
 what_was_wrong_ko='크루즈는 이후 코로나처럼 thesis 시점에 예측 불가능했던 extreme event에 매우 취약하다는 점도 드러났다. 따라서 “좋은 자본사이클”과 “대차대조표가 tail event를 버틸 수 있는가”는 별도로 봐야 한다.',
 lesson_ko='자본집약 산업은 수요 성장률보다 공급의 lead time·발주잔고·폐선·자본규율이 더 중요한 경우가 많다. 단, 레버리지가 높으면 예외적 shock가 equity를 크게 훼손할 수 있다.',
 current_watch_ko='신규 선박 orderbook, Net Yield, onboard spend, 순부채/EBITDA, 이자비용과 ROIC를 함께 추적해야 한다.'),
'RMD': dict(
 one_line_ko='ResMed 숏은 2016년 수면무호흡 시장이 포화에 가깝고 reimbursement·경쟁·M&A가 마진을 압박해 당시 높은 멀티플이 무너질 것이라고 본 아이디어였지만, 핵심 시장크기와 제품·소프트웨어 확장성을 과소평가했다.',
 business_economics_ko='ResMed는 CPAP/flow generator와 mask·accessory를 판매한다. 당시 매출의 약 43%였던 마스크·소모품은 장비보다 반복성이 높고 마진도 높았다. DME 채널과 reimbursement 규제가 중요하지만, 진단률 상승과 설치기반 확대가 mask replacement revenue를 반복적으로 만든다. 이후 Brightree 등 소프트웨어도 recurring revenue 축이 됐다.',
 valuation_at_t0_ko='VIC 숏 작성 당시 주가는 $59.75, 시총 약 86억달러, Brightree 인수 반영 EV 약 91억달러였다. 10년 평균 P/E 약 19배보다 높은 멀티플에서 2017 organic growth 정체와 margin pressure가 발생하면 multiple compression이 클 것이라는 논리였다.',
 stock_return_summary_ko='숏 관점 원 DB 성과는 1년 -18.0%, 3년 -71.3%, 5년 -272.2%였다. 즉 주가가 상승하면서 숏은 기간이 길어질수록 크게 실패했다.',
 earnings_bridge_ko='예상했던 reimbursement 압력 < 미진단 OSA 시장 확대 + 제품혁신 + installed base에서 발생하는 mask/accessory 반복매출 + software 확장 효과가 더 컸다.',
 what_was_right_ko='경쟁입찰·보험자 reimbursement 압력과 M&A 리스크 자체는 실제 존재했다. 그러나 그것이 시장 전체 성장과 반복 소모품 economics를 압도할 것이라는 크기 판단이 틀렸다.',
 what_was_wrong_ko='가장 큰 오류는 “현재 진단환자 수”를 사실상 TAM ceiling처럼 본 것이다. FY2026에도 매출이 56.5억달러(+10%)로 성장하고 순이익 15.2억달러, Residential Care Software 매출 6.76억달러까지 커졌다.',
 lesson_ko='의료기기 TAM은 유병률만이 아니라 진단률, 치료순응도, reimbursement, replacement cycle로 움직인다. “시장 포화” 숏은 신규환자와 교체수요를 분리해 증명해야 한다.',
 current_watch_ko='GLP-1 등 비만치료가 OSA incidence/therapy demand에 미치는 영향, 경쟁사 회복, mask share, software growth와 margin을 봐야 한다.'),
'CVNA': dict(
 one_line_ko='Carvana 숏은 2017년 “차 한 대를 팔 때마다 손해를 보며 재고·SG&A 때문에 현금이 고갈된다”는 회계/단위경제 분석은 상당 부분 맞았지만, 이를 곧바로 수개월 내 파산이라는 terminal conclusion으로 연결해 실패한 사례다.',
 business_economics_ko='Carvana는 중고차를 매입·정비·온라인 판매하고 금융·보증 등 부가수익을 붙이는 모델이다. 초기에는 차량재고가 매출의 큰 비중을 차지해 성장 자체가 working capital을 요구했고, 물류·reconditioning·광고 고정비 때문에 낮은 GPU가 문제였다. 반면 규모가 커질수록 구매·물류·금융 attach와 SG&A leverage가 개선될 가능성도 있었다.',
 valuation_at_t0_ko='VIC는 2016년 CFO-capex가 약 -2.8억달러였고 2017년에도 매출이 두 배가 되면 재고 약 1.85억달러와 capex 약 4,000만달러가 필요해 몇 분기 안에 현금이 부족해질 수 있다고 계산했다. 핵심은 멀티플보다 liquidity runway였다.',
 stock_return_summary_ko='원 DB 장기 성과값은 없지만 사후 경로는 극단적이었다. 2022~2023년 실제 유동성 위기와 채무 재조정이 발생해 숏의 중간 진단은 맞았지만 회사는 살아남아 2025년 소매판매 약 59.7만대, 매출 203억달러, 조정 EBITDA 22.37억달러까지 회복했다.',
 earnings_bridge_ko='초기 cash burn·부채위험 현실화 → 비용절감·재고/물류 효율화·채무교환 → GPU 개선과 SG&A leverage → EBITDA 흑자 → 파산 확률 하락과 equity rerating이 폭발적으로 나타났다.',
 what_was_right_ko='“성장하면 현금이 더 필요하다”는 working-capital 분석, 낮은 초기 GPU, 과도한 SG&A, 추가 자금조달 필요성은 정확했다. 실제로 2022~2023년 자본·부채구조 조정이 필요했다.',
 what_was_wrong_ko='오류는 변수가 움직이지 않는다고 가정한 것이다. GPU, 고정비, 재고회전, financing economics가 개선될 여지를 충분히 두지 않은 채 liquidity problem을 bankruptcy certainty로 바꿨다.',
 lesson_ko='숏에서는 “재무상태가 나쁘다”와 “equity가 0이 된다” 사이의 간극이 크다. liquidity runway, covenant, 담보가치, 자본시장 접근, management의 cost-reset 능력을 확률로 다뤄야 한다.',
 current_watch_ko='GPU의 질(금융/일회성 포함 여부), retail unit growth, interest expense, 순부채, securitization 시장과 normalized EBITDA를 봐야 한다.'),
'LINC': dict(
 one_line_ko='Lincoln Educational 롱은 코로나·경기불확실성으로 눌린 직업교육업체에서 enrollment 회복이 기존 캠퍼스 고정비 위에 올라가면 EBITDA가 매출보다 훨씬 빠르게 늘어난다는 영업레버리지 아이디어였다.',
 business_economics_ko='LINC는 자동차·전기·용접·HVAC·헬스케어 등 middle-skill 직업훈련을 제공한다. 캠퍼스·강사·행정조직이라는 고정비가 먼저 들어가므로 학생 수가 일정 수준을 넘으면 추가 tuition의 상당 부분이 이익으로 전환될 수 있다. 반대로 규제·학생모집비용·취업성과가 나빠지면 고정비가 역레버리지된다.',
 valuation_at_t0_ko='VIC 작성 당시 시총 약 1억달러, 순부채 900만달러, 전환우선주 1,270만달러를 포함한 EV 약 1.25억달러였다. 2021 EBITDA 2,800만달러를 달성하고 8배를 적용하면 EV 2.25억달러, 주당 약 $8(완전희석 약 $7)로 평가했다.',
 stock_return_summary_ko='원 DB에 1/3/5년 성과는 없지만 사업 thesis는 이후 강하게 실현됐다. 2025년 매출 5.182억달러(+17.8%), 조정 EBITDA 6,710만달러(+58.7%), 신규 starts +15.2%, 영업현금흐름 5,930만달러였다.',
 earnings_bridge_ko='enrollment/starts 회복 → 기존 캠퍼스의 capacity utilization 상승 → 매출 성장보다 EBITDA가 빠르게 증가 → 현금흐름 개선 → 신규 캠퍼스/프로그램에 재투자할 여력 확대의 구조다.',
 what_was_right_ko='핵심은 단순 “실업률이 오르면 학생이 늘어난다”가 아니라 고정비 구조 위에서 enrollment가 회복될 때 incremental margin이 크다는 점이었다. 2025년 매출 +17.8%에 EBITDA +58.7%가 이를 확인했다.',
 what_was_wrong_ko='교육수요는 실업률 하나로 결정되지 않는다. 노동력 부족, 기술직 임금, 정부지원, 규제, 캠퍼스 증설이 모두 영향을 준다. 이후 성장의 일부는 신규 capacity expansion도 포함한다.',
 lesson_ko='고정비 사업의 turnaround는 매출 성장률보다 seat/capacity utilization과 incremental EBITDA margin을 봐야 한다. 동시에 교육업은 규제와 학생성과가 장기 해자의 핵심이다.',
 current_watch_ko='starts, 학생 유지율, 졸업·취업률, 캠퍼스 capacity, 신규 캠퍼스 ramp 비용, 규제/Title IV 의존도를 봐야 한다.'),
'PINS': dict(
 one_line_ko='Pinterest 롱은 국제 MAU의 낮은 ARPU와 강한 구매의도를 monetization gap으로 봤다. 사용자 수는 단기적으로 오히려 감소해 시간축은 틀렸지만, 장기 MAU와 광고수익·FCF는 크게 성장해 논지는 부분적으로 실현됐다.',
 business_economics_ko='Pinterest는 사용자가 구매·여행·인테리어·패션 같은 “앞으로 할 일”을 이미지로 탐색·저장하는 visual discovery 플랫폼이다. 일반 SNS보다 commercial intent가 높을 수 있고, 광고주 입장에서는 검색과 소셜 사이의 퍼널을 공략한다. 경제성은 MAU×ARPU로 단순화할 수 있지만 실제로는 광고 load, 측정/타게팅, 쇼핑 전환, 국가별 광고시장 성숙도가 중요하다.',
 valuation_at_t0_ko='VIC는 명시적인 단기 멀티플보다 ① 컨센서스를 웃도는 revenue beat ② 약 5년 내 Meta에 가까운 margin ③ 향후 5년 50%+ revenue growth를 핵심 가치창출 경로로 제시했다. 국제 사용자는 약 4억명으로 전체의 80%였지만 ARPU는 미국 대비 매우 낮아 monetization gap이 upside의 중심이었다.',
 stock_return_summary_ko='원 DB 성과값은 없지만 사업 경로는 혼합이었다. 2021년 말 MAU가 4.31억명까지 감소해 초기 growth thesis가 흔들렸으나 2025년 6.19억명으로 사상 최고치를 기록했고 매출 42.22억달러, FCF 12.52억달러까지 성장했다.',
 earnings_bridge_ko='코로나 이후 MAU 정상화/감소 → 비용구조 재정비와 광고제품 개선 → 국제 MAU 재성장 + ARPU/광고효율 개선 → 매출·EBITDA·FCF가 다시 성장했다.',
 what_was_right_ko='국제 ARPU gap과 구매의도가 장기 monetization 여지라는 판단은 맞았다. 2025년 조정 EBITDA 12.70억달러, FCF 12.52억달러로 수익화는 분명히 개선됐다.',
 what_was_wrong_ko='“5년간 50%+ 매출성장”과 40%+ EBITDA margin에 가까운 기대는 과도했다. 2025 조정 EBITDA margin은 약 30% 수준으로 좋아졌지만 원래 기대치에는 미달했고, MAU도 초기에 큰 역풍을 겪었다.',
 lesson_ko='플랫폼 투자는 TAM/MAU만 보지 말고 cohort engagement와 ARPU의 동시 움직임을 봐야 한다. “사용자는 줄어도 monetization은 좋아질 수 있다”와 “성장기업의 원 논지가 맞았다”는 구분해야 한다.',
 current_watch_ko='미국/국제 MAU, 지역별 ARPU, 광고 load, shopping conversion, AI 추천이 engagement와 advertiser ROI를 동시에 개선하는지 봐야 한다.'),
'AMRN': dict(
 one_line_ko='Amarin 롱은 임상적으로 큰 환자군을 곧바로 거대한 경제적 TAM으로 환산하고, 유럽 상업화와 6~24개월 내 대형 제약사 매각을 함께 기대한 아이디어였지만 실제 reimbursement·특허·상업화 마찰을 과소평가했다.',
 business_economics_ko='Amarin의 핵심자산 VASCEPA/VAZKEPA는 심혈관 위험 감소를 위한 icosapent ethyl 제품이다. 바이오텍의 경제적 가치는 임상적으로 약을 쓸 수 있는 환자 수보다 특허기간, 처방습관, 보험급여, 가격, 영업망, 제네릭 경쟁을 거친 “실제 유료 처방”에서 결정된다.',
 valuation_at_t0_ko='VIC는 주당 순현금/투자자산 약 $1.37, 2033년까지 undiscounted FCF 170억달러 이상, 자체 추정 peak revenue 대비 EV 약 0.3배로 평가했다. peer가 통상 peak sales 3~5배라고 비교했고 300~600%+ upside와 6~24개월 내 매각 가능성을 제시했다.',
 stock_return_summary_ko='원 DB 성과값은 없지만 핵심 사업·촉매 thesis는 실패했다. 예상 기간 내 매각은 일어나지 않았고 2025년 총매출은 2.136억달러에 그쳤으며 유럽은 직접상업화보다 Recordati 라이선스·공급 모델로 전환됐다.',
 earnings_bridge_ko='큰 임상 TAM → 실제 환자 접근에서 reimbursement/의사처방/가격/제네릭 마찰 → 기대보다 느린 매출 → 직접 유럽조직의 fixed cost 부담 → 라이선스 모델 전환으로 economics가 축소됐다.',
 what_was_right_ko='제품의 임상적 가치와 큰 잠재환자군 자체는 존재했다. 또한 유럽이 미국 generic pressure를 보완해야 한다는 전략적 문제의식은 맞았다.',
 what_was_wrong_ko='환자 수를 경제적 TAM으로 바로 번역했고, buyout을 upside option이 아니라 사실상 base-case catalyst로 다뤘다. 상업화 속도와 reimbursement friction이 valuation에서 충분히 할인되지 않았다.',
 lesson_ko='바이오텍 TAM은 “적응증 환자 수×약가”로 계산하면 거의 항상 과대평가 위험이 있다. diagnosed→eligible→treated→reimbursed→retained 환자 funnel을 단계별로 할인해야 한다.',
 current_watch_ko='라이선스 수익·royalty economics, 현금소모, 국가별 reimbursement, generic erosion과 추가 전략적 거래를 봐야 한다.'),
'PTON': dict(
 one_line_ko='Peloton 롱은 팬데믹 이후에도 Connected Fitness 침투가 이어지고 70%대 구독 gross margin이 하드웨어 성장투자를 흡수해 빠르게 정상화 이익으로 전환될 것이라고 봤지만, 수요 pull-forward와 고정비 규모를 크게 과소평가했다.',
 business_economics_ko='Peloton은 Bike/Tread 같은 고가 하드웨어로 설치기반을 만들고 월 구독료에서 반복매출을 얻는 하드웨어+subscription 모델이다. 좋은 시나리오에서는 초기 CAC/하드웨어 비용을 장기 구독 LTV가 회수하지만, 하드웨어 공급망·물류·제조에 고정비가 크면 신규판매가 꺾일 때 subscription gross margin만으로 전체 회사 비용을 지탱하기 어렵다.',
 valuation_at_t0_ko='VIC는 당시 정상화 earnings가 아직 보이지 않아 전통 P/E보다 cost/gross structure를 역산했다. 연말 Connected Fitness sub 335만명 가정에서 subscription run-rate revenue 약 17.6억달러, 70~73% gross margin이면 subscription gross profit 약 12.3~13억달러가 되어 R&D+G&A를 상당 부분 커버할 수 있다고 봤다. 하드웨어 gross margin 정상화가 추가 upside였다.',
 stock_return_summary_ko='원 DB 성과값은 없지만 원 thesis는 명확히 실패했다. FY2022 매출 35.8억달러에서 FY2026 24.46억달러로 감소했고 대규모 구조조정·자체제조 철수가 필요했다. 다만 FY2026에는 순이익 6,300만달러와 FCF 3.78억달러로 뒤늦게 흑자화했다.',
 earnings_bridge_ko='팬데믹 수요 pull-forward → 생산·물류·인력 고정비 확대 → 신규 하드웨어 수요 정상화 → 재고/가격인하/고정비 역레버리지 → 구조조정·outsourcing → 낮은 성장률이지만 FCF 중심 구조로 재편됐다.',
 what_was_right_ko='구독 gross margin과 기존 설치기반에서 반복매출이 나온다는 점은 살아남았다. 비용을 크게 줄인 뒤에는 실제로 현금흐름을 만들 수 있었다.',
 what_was_wrong_ko='핵심 오류는 구독 economics와 “전체 회사 economics”를 혼동한 것이다. 신규 hardware demand가 꺾일 때 제조·물류·마케팅 고정비를 누가 부담하는지 과소평가했고, Connected Fitness 구독자도 FY2026에 전년 대비 8.8% 감소했다.',
 lesson_ko='hardware+subscription 모델은 subscription GM보다 cohort retention, hardware replacement cycle, CAC payback, fulfillment/manufacturing fixed cost를 합친 contribution economics로 봐야 한다.',
 current_watch_ko='Connected Fitness subscriber 순증감, churn, subscription ARPU, hardware contribution margin, FCF가 비용절감 종료 뒤에도 유지되는지를 봐야 한다.'),
'UBER': dict(
 one_line_ko='Uber 롱은 2022년 시장이 계속 “언젠가 이익이 날까?”를 묻던 시점에 Mobility가 이미 수익성 높은 네트워크이고 Delivery도 규모화되며, 두 제품을 한 계정·드라이버망에서 재사용하는 멀티프로덕트 구조가 FCF로 전환될 것이라고 본 아이디어였다.',
 business_economics_ko='Uber는 소비자 수요와 드라이버/배달 공급을 매칭하는 marketplace다. 중요한 economics는 단순 take rate가 아니라 도시별 network density가 대기시간을 줄이고 driver trips/hour를 높여 소비자 가격과 공급자 시간당 수입을 동시에 개선할 수 있다는 점이다. Mobility와 Delivery를 한 앱·회원제·공급망에 얹으면 CAC와 driver utilization을 공유할 수 있다.',
 valuation_at_t0_ko='VIC는 Uber가 자체 추정 2024 unlevered FCF의 약 10배에 거래되고 있다고 봤다. 2024 management EBITDA guidance는 $5bn이었지만 작성자는 mature Mobility/Delivery margin과 35% incremental margin을 적용하면 earnings power가 훨씬 크다고 봤고, 당시 intrinsic value를 주당 $60~80로 제시했다.',
 stock_return_summary_ko='원 DB 성과값은 없지만 사업 실적은 thesis를 강하게 검증했다. 2024년 매출 439.8억달러, 조정 EBITDA 64.8억달러, FCF 68.9억달러로 회사의 초기 2024 목표를 넘어섰고 2025년 Gross Bookings는 1,934.5억달러, 연간 FCF는 약 100억달러 수준에 도달했다.',
 earnings_bridge_ko='Mobility network density 개선 → driver productivity와 take economics 개선 → Delivery 적자축소/규모화 → cross-platform 이용자 증가와 Uber One → marketing efficiency·frequency 증가 → bookings 성장보다 FCF가 빠르게 증가했다.',
 what_was_right_ko='핵심은 “네트워크 효과”라는 추상어가 아니라 실제 incremental margin과 cross-sell economics를 봤다는 점이다. Mobility earnings engine과 Delivery의 수익성 개선이 동시에 나타났다.',
 what_was_wrong_ko='장기적으로 AV가 driver economics를 바꿀 가능성과 각 지역의 보험·규제비용은 원 thesis 이후에도 계속 변한다. 따라서 2022 thesis 성공을 “Uber의 해자가 영구적”이라는 뜻으로 확대하면 안 된다.',
 lesson_ko='플랫폼은 GMV 성장보다 contribution/incremental margin, 공급자 utilization, multi-homing, cross-product CAC와 retention을 봐야 한다. 네트워크 효과는 현금흐름으로 증명되어야 한다.',
 current_watch_ko='Mobility/Delivery segment margin, Uber One cross-sell, 보험비용, driver incentives, AV 파트너 economics와 take rate를 추적해야 한다.'),
'BYND': dict(
 one_line_ko='Beyond Meat 숏은 “대체육 TAM이 크다”는 거대한 서사를 반박하는 대신 실제 채널 판매량, 가격 프리미엄, gross margin, 현금소모를 봤고 이 데이터들이 동시에 악화되면서 매우 성공한 숏이 됐다.',
 business_economics_ko='Beyond Meat는 plant-based meat 브랜드로 retail과 foodservice에 제품을 판매한다. 브랜드가 있어도 제품차별화와 반복구매가 약하면 grocery shelf space와 QSR partnership은 지속적인 sell-through를 보장하지 않는다. 제조설비 고정비가 큰 상태에서 volume이 줄면 gross margin이 빠르게 악화되는 구조다.',
 valuation_at_t0_ko='2022년 VIC 숏 당시 시총 약 15억달러, 부채 약 11억달러·순부채 약 6.8억달러, FY23 EV/Sales 약 3.6배였다. 작성자는 FY23/24 매출을 consensus보다 각각 15%/25% 낮게 보고 FY24 매출에 2배 EV/Sales를 적용해 base target $7을 제시했다. 이는 산업 체크에서 잠재 인수가치 약 1배 sales보다도 프리미엄을 준 값이었다.',
 stock_return_summary_ko='원 DB 성과값은 없지만 사후 사업경로가 숏 논지를 강하게 확인했다. 2026년 2분기 매출은 6,880만달러(-8.2%), gross margin 8.5%, 조정 EBITDA -2,770만달러로 EBITDA margin은 약 -40%였다. 미국 foodservice 매출은 -27.6%였고 1대30 역분할도 시행됐다.',
 earnings_bridge_ko='높은 소비자가격 프리미엄 + 경쟁증가 → 반복구매/채널 volume 약화 → 공장 utilization 저하 → 낮은 gross margin·현금소모 지속 → 자본구조 압박과 주가 훼손으로 이어졌다.',
 what_was_right_ko='카테고리 TAM보다 실제 unit velocity와 gross profit을 본 점이 정확했다. 판매점/파트너십 숫자가 늘어도 소비자가 반복구매하지 않으면 economics가 좋아지지 않는다는 점을 데이터로 검증했다.',
 what_was_wrong_ko='브랜드 자체의 잔존가치와 비용절감·제품개선 가능성은 남아 있다. 숏 thesis가 맞았다고 해서 기업가치가 반드시 0이 되는 것은 아니다.',
 lesson_ko='소비재 성장주는 distribution doors보다 sell-through, repeat rate, price premium, gross profit per unit을 봐야 한다. TAM은 소비자가 실제로 재구매할 때만 경제적 TAM이 된다.',
 current_watch_ko='미국 retail/foodservice volume, gross margin, 현금잔고·부채, 신규 제품 repeat purchase와 capacity utilization을 봐야 한다.'),
'ALB': dict(
 one_line_ko='Albemarle 롱은 2019년 리튬 spot price 급락을 장기 EV 수요 붕괴로 해석한 시장에 맞서, 저원가 자산·장기계약·비리튬 현금흐름이 있는 생산자는 commodity 가격 변동을 견디며 구조적 수요를 먹을 수 있다고 본 아이디어였다.',
 business_economics_ko='Albemarle은 lithium, bromine, catalysts를 보유한 specialty chemicals 기업이었다. 리튬은 성장축이지만 가격과 신규 공급에 민감하고, bromine/catalysts의 현금흐름이 증설자금과 재무완충 역할을 했다. 리튬은 광산/염호의 품질, conversion 기술, 고객 qualification 때문에 단순 spot commodity와 차이가 있지만 결국 가격사이클을 피할 수는 없다.',
 valuation_at_t0_ko='VIC는 ALB가 2017년 $140, 21x EV/LTM EBITDA에서 2019년 약 $70, 8.9x로 하락했다고 봤다. 보수적 SOTP는 주당 $95.6으로 약 37% upside를 제시했다. 핵심 mispricing은 중국 spot price 하락을 ALB의 장기계약 realized price와 동일시한 데 있다고 주장했다.',
 stock_return_summary_ko='원 DB 기준 1년 +12.9%, 3년 +203.9%였다. 2022년 lithium EBITDA가 약 300% 증가하고 가격 +140%, 물량 +20~30% 전망이 나오며 시간축 내 thesis는 크게 성공했다. 이후 리튬 가격이 다시 급락하면서 2025년 Energy Storage EBITDA는 -8%로 감소해 장기 결과는 혼합적이다.',
 earnings_bridge_ko='EV/ESS 물량수요 증가 → 공급증설 지연과 가격상승 → lithium earnings 폭증 → 이후 높은 가격이 신규 공급을 자극 → 가격하락 → 물량·비용절감이 일부 상쇄하는 전형적 commodity capital cycle을 보였다.',
 what_was_right_ko='2019년 spot panic이 ALB의 계약가격과 자산질을 과도하게 할인했다는 판단은 맞았다. 저원가/규모 자산은 상승사이클에서 큰 operating leverage를 얻었다.',
 what_was_wrong_ko='장기계약과 자산질이 commodity cyclicality를 제거하지는 못했다. 구조적 EV 수요가 맞아도 공급 반응이 더 빠르면 가격과 EBITDA가 하락할 수 있다는 점이 이후 재확인됐다.',
 lesson_ko='“구조적 수요 성장”과 “좋은 commodity 투자”는 같은 문장이 아니다. 수요 CAGR보다 supply response, cost curve, 증설 lead time, 계약구조와 현재 가격에 내재된 기대를 같이 봐야 한다.',
 current_watch_ko='리튬 contract/spot realized price, Energy Storage volume, 글로벌 신규 capacity, capex cuts, OCF/FCF와 순부채를 봐야 한다.'),
'APH': dict(
 one_line_ko='Amphenol은 단순 전자부품 회사가 아니라 전자화·데이터 증가를 먹고 자라는 interconnect 플랫폼이자, 분권형 운영조직을 이용해 작은 niche 기업을 계속 인수하는 산업재 복리기업이라는 2020년 VIC 아이디어였다. 이후 결과는 매우 성공적이었다.',
 business_economics_ko='커넥터·케이블·광섬유·안테나·센서는 완제품 원가에서 차지하는 비중은 작지만 고장 시 시스템 전체가 멈출 수 있는 mission-critical 부품이다. 고객이 몇 %의 부품가격 절감보다 신뢰성·qualification·납기·설계지원에 더 민감할 수 있어 niche별 가격결정력과 switching friction이 생긴다. Amphenol은 120명+ GM에게 현장 권한을 주는 분권형 구조로 자동차·모바일·항공·국방·산업·데이터센터처럼 제품주기가 다른 시장을 동시에 운영한다. 이 구조가 불황 시 빠른 비용조정과 bolt-on M&A 이후 경영진 유지·cross-sell을 가능하게 한다.',
 valuation_at_t0_ko='2020년 VIC 게시 당시 주가는 약 $110였다. 글은 FY2020/21 P/E 약 33x/27x로 표면상 싸지 않다고 인정했지만, 이익이 경기저점에 있어 normalized forward cash flow 기준 약 25x라고 봤다. Organic 5~7% + M&A 5~7%에 margin·buyback을 더해 장기 cash flow/share가 low-to-mid teens로 복리할 수 있다면 이 가격은 감당 가능하다는 quality-compounder 논리였다.',
 stock_return_summary_ko='2021년과 2024년에 각각 2:1 분할이 있었으므로 당시 $110은 현재 주식수 기준 $27.50에 해당한다. 2026년 8월 28일 종가 $157.74와 비교하면 약 5.74배이며 약 6.03년 CAGR은 33.6%다. 배당을 포함하면 총수익률은 이보다 소폭 높다.',
 earnings_bridge_ko='전자화로 content/device 증가 + 경기회복 → organic growth → 분권형 비용·자원조정으로 높은 incremental margin → 반복적인 bolt-on M&A가 새 고객/지역/기술을 추가 → FCF가 다시 M&A·buyback·배당으로 재투자되는 구조가 작동했다.',
 what_was_right_ko='핵심 5개 논지—전자화 구조성장, 분권형 운영, 다각화의 장점, bolt-on M&A, 경기정상화—가 모두 대체로 맞았다. 2020~2025 매출은 85.99억달러에서 231억달러로 CAGR 21.9%, split-adjusted 조정 EPS는 약 $0.935에서 $3.34로 CAGR 29.0%, FCF는 13.28억달러에서 44억달러로 CAGR 27.1% 성장했다. 조정 영업마진도 19.2%에서 26.2%로 700bp 상승했다.',
 what_was_wrong_ko='원래 기대는 cash flow/share low-to-mid teens였는데 실제 성장은 훨씬 높았다. 즉 thesis가 틀렸다기보다 AI/data communications 수요와 M&A 규모가 예상보다 강했다. 다만 2026년 현재 높은 멀티플에서는 과거와 동일한 수익률을 그대로 외삽하면 안 된다.',
 lesson_ko='산업재 복리기업은 “부품이 commodity인가?”보다 ① 고객 원가 대비 중요도 ② qualification/switching friction ③ 분권형 조직의 비용유연성 ④ M&A 후 자율성을 유지하면서 cross-sell하는 방식 ⑤ FCF 재투자 ROIC를 봐야 한다.',
 current_watch_ko='AI 데이터센터 수요가 정상화될 때 organic growth와 margin이 얼마나 유지되는지, 대형 M&A가 과거 작은 bolt-on보다 ROIC를 낮추지 않는지, 현재 valuation이 장기 EPS/FCF 성장률을 얼마나 선반영했는지가 핵심이다.'),
}

# Existing reports not explicitly overridden above.
# All 18 current verified cases are covered.

METRICS={
'WCC':[
 ('조정 EBITDA','인수 전 독립 양사','기준','2023','독립 양사 대비 +89%','+89%','통합 시너지가 실제 이익으로 확인'),
 ('조정 EBITDA 마진','인수 전','기준','2023','+240bp','+240bp','유통업의 낮은 마진이 시너지로 개선'),
 ('FCF','VIC 2023E','3.44억달러','2023','4.44억달러','예상 상회','deleveraging 재원 확보'),
 ('순레버리지','인수 직후','높은 레버리지','2023','2.8x','정상화','equity tail risk 하락')],
'BXC':[
 ('조정 EBITDA 마진','2020','5.5%','2021','10.8%','+530bp','self-help와 사이클이 동시 작동'),
 ('순레버리지','2020','3.5x','2021','1.1x','-2.4x','재무위험 급감'),
 ('매출','2021','—','2021','42.8억달러','—','목재/주택 호황 반영'),
 ('조정 EBITDA','2021','—','2021','4.64억달러','—','마진 정상화 폭 확인')],
'WOR':[
 ('Nikola 보유지분','2020-06','19,048,020주','FY2021','전량 매각·기부','현금화 완료','숨은자산이 실제 가치로 전환'),
 ('Nikola 지분 시장가치','2020-06','약 12억달러','당시 WOR 시총','약 18.3억달러','시총의 약 66%','SOTP 왜곡이 매우 컸음'),
 ('세전 투자이익','투자원가','초기 $2m','FY2021','6.551억달러','대규모 실현익','이벤트 thesis 실현')],
'KKR':[
 ('AUM','2019','약 2,180억달러','2024','6,380억달러','약 2.9배 / CAGR 24%','구조적 alternatives 성장'),
 ('관리보수','2024','—','2024','35억달러','—','반복 fee base 규모화'),
 ('FRE','2024','—','2024','33억달러','—','fee economics 실현'),
 ('ANI','2024','—','2024','42억달러','—','플랫폼 전체 earnings power 확대')],
'BX':[
 ('총 AUM','2016','3,670억달러','2025','약 1.3조달러','약 3.5배 / CAGR 15%','대형화 후에도 구조 성장 지속'),
 ('Fee-earning AUM','2016','2,770억달러','2016','—','—','당시에도 반복 fee base가 핵심'),
 ('FRE','2016','10억달러+','이후','지속 확대','—','SOTP의 recurring component가 성장')],
'TMO':[
 ('매출','2014','—','2014','168.9억달러','+29% YoY','Life Technologies 통합 효과'),
 ('조정 EPS','2014','—','2014','—','+28% YoY','이익이 매출과 함께 성장'),
 ('조정 영업마진','전년','19.5% 수준','2014','21.9%','+240bp','M&A 후에도 margin expansion')],
'DPZ':[
 ('미국 동일점매출','2016','—','2016','+10.5%','—','브랜드/디지털 turnaround'),
 ('해외 동일점매출','2016','—','2016','+6.3%','—','국제 확장 품질 확인'),
 ('글로벌 순점포 증가','2016','—','2016','+1,281개','—','royalty base 확대'),
 ('순이익','2016','—','2016','2.147억달러','—','반복 cash flow가 earnings로 전환')],
'RCL':[
 ('Net Yield','2017','—','2017','+6.4% constant FX','8년 연속 증가','공급절제와 가격력 확인'),
 ('순이익','2017','—','2017','16억달러','—','운영레버리지 실현'),
 ('EPS','2017','—','2017','$7.53','—','이익 정상화'),
 ('ROIC','과거 저점','낮은 수준','2017','10%+','개선','자본규율 변화 확인')],
'RMD':[
 ('매출','FY2026','—','FY2026','56.5억달러','+10% YoY','시장포화 숏 반증'),
 ('순이익','FY2026','—','FY2026','15.2억달러','—','마진 붕괴 thesis 반증'),
 ('Residential Care Software 매출','인수 전','0','FY2026','6.76억달러','신규 반복수익 축','Brightree 가치파괴 thesis 반증'),
 ('마스크·기타 매출','FY2026','—','FY2026','+13% YoY','—','installed base 반복수요 유지')],
'CVNA':[
 ('2016 CFO-capex','2016','약 -2.8억달러','2022~23','유동성 위기·재조정','중간 thesis 확인','현금소모 진단은 맞음'),
 ('소매 판매대수','2017 초기','고성장 초기','2025','약 59.7만대','규모 급증','규모경제 가능성 현실화'),
 ('매출','2025','—','2025','203억달러','—','사업 생존·성장'),
 ('조정 EBITDA','초기','적자','2025','22.37억달러','흑자 전환','파산 결론 반증')],
'LINC':[
 ('매출','2025','—','2025','5.182억달러','+17.8% YoY','enrollment 성장'),
 ('조정 EBITDA','2025','—','2025','6,710만달러','+58.7% YoY','높은 incremental margin'),
 ('신규 starts','2025','—','2025','+15.2%','—','수요 회복 확인'),
 ('영업현금흐름','2025','—','2025','5,930만달러','—','이익의 현금전환')],
'PINS':[
 ('MAU','2021년말','4.31억명','2025','6.19억명','+44%','초기 감소 후 장기 회복'),
 ('매출','2025','—','2025','42.22억달러','—','monetization 확대'),
 ('조정 EBITDA','2025','—','2025','12.70억달러','약 30% margin','원 40%+ 기대에는 미달'),
 ('FCF','2025','—','2025','12.52억달러','—','광고수익의 현금전환 확인')],
'AMRN':[
 ('총매출','2025','—','2025','2.136억달러','원 thesis 대비 크게 낮음','임상 TAM→매출 전환 실패'),
 ('유럽 사업모델','2021 thesis','직접 상업화','2025','Recordati 라이선스·공급','전략 전환','직접모델 economics 미달'),
 ('예상 매각 촉매','6~24개월','높은 확률 가정','해당 기간','미실현','실패','촉매를 base case로 둔 오류')],
'PTON':[
 ('매출','FY2022','35.8억달러','FY2026','24.46억달러','CAGR 약 -9.1%','팬데믹 성장 외삽 실패'),
 ('GAAP 순이익','FY2022','적자','FY2026','6,300만달러','뒤늦은 흑자','비용구조 전환'),
 ('FCF','FY2026','—','FY2026','3.78억달러','흑자','subscription economics 일부 생존'),
 ('Connected Fitness 구독자','FY2026','—','FY2026','255만명','-8.8% YoY','해자가 성장률을 방어하진 못함')],
'UBER':[
 ('매출','2024','—','2024','439.8억달러','—','플랫폼 규모 확대'),
 ('조정 EBITDA','2024 guide','$5bn','2024','64.8억달러','가이드 상회','수익력 과소평가 thesis 확인'),
 ('FCF','2024','—','2024','68.9억달러','—','현금흐름 전환'),
 ('Gross Bookings','2025','—','2025','1,934.5억달러','—','멀티프로덕트 성장'),
 ('FCF','2025','—','2025','약 100억달러','—','FCF 복리 지속')],
'BYND':[
 ('매출','2026Q2','—','2026Q2','6,880만달러','-8.2% YoY','카테고리 수요약화'),
 ('Gross margin','2026Q2','—','2026Q2','8.5%','낮은 수준','단위경제 문제 지속'),
 ('조정 EBITDA','2026Q2','—','2026Q2','-2,770만달러','약 -40% margin','고정비 흡수 실패'),
 ('미국 Foodservice','2026Q2','—','2026Q2','-27.6% YoY','큰 폭 감소','파트너십≠실제 수요')],
'ALB':[
 ('Lithium EBITDA','2022','—','2022','약 +300%','급증','상승사이클 thesis 실현'),
 ('Lithium 가격','2022 guide','—','2022','+140%','급등','spot panic 반전'),
 ('Lithium 물량','2022 guide','—','2022','+20~30%','증가','EV/ESS 수요 성장'),
 ('영업현금흐름','2025','—','2025','13억달러','—','가격하락 완충'),
 ('Energy Storage EBITDA','2025','—','2025','-8%','감소','commodity cyclicality 재확인')],
'APH':[
 ('매출','2020','85.99억달러','2025','231억달러','CAGR 21.9%','원 low/mid-teens 기대를 크게 상회'),
 ('조정 EPS*','2020','약 $0.935','2025','$3.34','CAGR 29.0%','*두 차례 2:1 분할 반영'),
 ('FCF','2020','13.28억달러','2025','44억달러','CAGR 27.1%','M&A와 organic growth가 현금으로 전환'),
 ('조정 영업마진','2020','19.2%','2025','26.2%','+700bp','분권형 비용유연성·믹스·규모효과'),
 ('주가','2020-08 VIC','$110 = 분할조정 $27.50','2026-08-28','$157.74','5.74배 / CAGR 33.6%','배당 제외 가격수익률')],
}

TIMELINES={
'WCC':[('2020-05','VIC 롱 게시','Anixter 인수 전후의 레버리지·통합위험이 핵심'),('2020','Anixter 인수 종결','대형 M&A 통합 시작'),('2021~2023','시너지·FCF·부채감축','통합 thesis 검증 구간'),('2023','통합 3년 성과 공개','EBITDA +89%, 마진 +240bp, 레버리지 2.8x')],
'BXC':[('2018-01','VIC 롱','hidden real estate·self-help·레버리지 정상화'),('2018~2020','sale-leaseback/부채감축','재무구조 개선'),('2020~2021','목재·주택 호황','사이클이 self-help를 증폭'),('2021','사상 최고 수익성','EBITDA margin 10.8%, leverage 1.1x')],
'WOR':[('2020-06-16','VIC 롱','Nikola 지분가치와 lock-up 오해 포착'),('2020-07','Nikola 500만주 매각','조기 현금화 가능성 즉시 확인'),('FY2021','Nikola 지분 전량 정리','세전 6.551억달러 이익'),('이후','Nikola 사업가치 급락','이벤트 thesis와 장기 underlying thesis를 구분해야 함')],
'KKR':[('2019-02','VIC 롱','alternatives 구조성장·capital markets·balance sheet'),('2019~2024','AUM 고성장','2,180억→6,380억달러'),('2024','FRE/ANI 규모화','반복 fee와 플랫폼 수익성 확인')],
'BX':[('2016-08','VIC 롱','신용시장 공포 속 SOTP 할인'),('2016','AUM 3,670억달러','장기 locked capital base'),('2020s','private wealth·credit·insurance 확대','제품군 다각화'),('2025','AUM 약 1.3조달러','구조적 fundraising 우위 확인')],
'TMO':[('2009-01','VIC 롱','경기침체가 반복매출·마진을 과도하게 할인'),('2014','Life Technologies 통합','매출·마진 동시 확대'),('5년 후','주가 +215%','quality+M&A 복리 구조 재평가')],
'DPZ':[('2011-02','VIC 롱','franchise royalty의 반복현금흐름 가치'),('2011~2016','디지털/브랜드 turnaround','SSS와 가맹점 경제성 개선'),('2016','미국 SSS +10.5%, 순점포 +1,281','royalty base 확대'),('5년','주가 +602%','사업 성장+자본배분 결합')],
'RCL':[('2012-04','VIC 롱','Concordia·유럽불황 속 공급사이클 전환'),('2012~2017','신규공급 둔화·Net Yield 상승','자본사이클 thesis 실현'),('2017','ROIC 10%+, EPS $7.53','운영/재무 개선 확인'),('2020','코로나 충격','예측불가능 tail event와 레버리지의 중요성 재확인')],
'RMD':[('2016-04','VIC 숏','시장포화·reimbursement·M&A 우려'),('이후','진단/제품 성장 지속','TAM ceiling 가정 반증'),('FY2026','매출 56.5억달러, 순익 15.2억달러','숏 핵심 thesis 실패')],
'CVNA':[('2017-05','VIC 숏','현금고갈·GPU/SG&A 문제 지적'),('2022~2023','유동성 위기·채무교환','중간 위험진단 적중'),('2023~2025','비용/GPU 개선','turnaround'),('2025','Adj EBITDA 22.37억달러','파산 결론 반증')],
'LINC':[('2020-06','VIC 롱','enrollment 회복+고정비 레버리지'),('2021~2025','학생 starts·capacity 확대','수요 회복'),('2025','매출 +17.8%, EBITDA +58.7%','incremental margin thesis 확인')],
'PINS':[('2021-07','VIC 롱','국제 ARPU gap+MAU 성장'),('2021말','MAU 4.31억명으로 감소','초기 시간축 반증'),('2022~2025','사용자 재성장·수익화 개선','장기 thesis 회복'),('2025','MAU 6.19억, FCF 12.52억달러','monetization 성공')],
'AMRN':[('2021-07','VIC 롱','거대한 TAM+유럽+M&A 촉매'),('6~24개월','예상 매각 미실현','촉매 실패'),('2025','Recordati 라이선스 전환','직접 유럽상업화 모델 축소'),('2025','매출 2.136억달러','원 경제적 TAM thesis와 큰 괴리')],
'PTON':[('2021-11','VIC 롱','고성장+70%대 subscription GM'),('2022','수요 둔화·재고·구조조정','핵심 반증 신호'),('2022~2025','제조/비용구조 축소','생존 중심 turnaround'),('FY2026','첫 연간 흑자·FCF 3.78억달러','성장 thesis 실패, cash thesis 일부 회복')],
'UBER':[('2022-08','VIC 롱','2024 FCF 10x·멀티프로덕트 경제성'),('2022~2023','FCF 흑자화·Delivery 개선','첫 확인 신호'),('2024','Adj EBITDA 64.8억, FCF 68.9억달러','가이드 상회'),('2025','FCF 약 100억달러','플랫폼 복리 확인')],
'BYND':[('2022-09','VIC 숏','수요·GM·현금소모 동시 악화'),('2022~2025','매출/마진 부진 지속','숏 thesis 반복 확인'),('2026Q2','GM 8.5%, Adj EBITDA -27.7m','단위경제 문제 지속'),('2026','1:30 역분할','장기 equity 압박의 결과')],
'ALB':[('2019-07','VIC 롱','spot panic과 장기계약 economics의 괴리'),('2021~2022','리튬 가격·수요 급등','thesis 강하게 실현'),('3년','롱 +203.9%','시간축 내 성공'),('2023~2025','공급증가·가격하락','구조수요와 commodity cycle은 별개임을 재확인')],
'APH':[('2020-08-17','VIC 롱','전자화+분권화+M&A 복리 thesis'),('2021-03','2:1 주식분할','주식수 조정'),('2020~2025','매출·EPS·FCF 고성장','사업 thesis가 예상보다 강하게 실현'),('2024-06','두 번째 2:1 주식분할','당시 $110→현재 기준 $27.50'),('2025','매출 231억달러·FCF 44억달러','M&A와 organic growth 동시 가속'),('2026-08-28','주가 $157.74','분할조정 당시 가격 대비 5.74배')],
}

# Add APH to verified core tables if absent.
APH_ID='bcde473f-865d-4b3a-b20f-e09a231ca3d8'
APH_POST={
'idea_id':APH_ID,'ticker':'APH','research_direction_ko':'롱',
'company_description_ko':'Amphenol은 전기·전자·광섬유 커넥터, interconnect system, 케이블, 안테나, 센서를 설계·제조하는 글로벌 부품회사다. 2020년 VIC는 약 1,750억달러의 interconnect·sensor 시장에서 점유율을 4~5%로 추정했고, 어느 단일 end market도 20%를 넘지 않는 다각화 구조와 120명+ GM의 분권형 운영을 핵심 경쟁력으로 봤다.',
'original_thesis_ko':'2020년 논지는 ① 거의 모든 산업의 전자화로 connector/sensor content가 구조적으로 증가하고 ② 120명+ GM에게 권한을 주는 분권형 조직이 경기변동에 빠르게 비용을 조정하며 ③ 이 조직이 서로 다른 end market 다각화를 가능하게 하고 ④ 2005년 이후 연평균 약 6% 추가 매출성장을 만든 bolt-on M&A가 계속되며 ⑤ 2019~20의 무역전쟁·자동차·코로나 부진이 정상화될 경우 low-to-mid teens의 cash flow/share 복리가 가능하다는 것이었다.',
'actual_development_ko':'결과는 원 기대를 크게 상회했다. 2020~2025 매출은 85.99억달러에서 231억달러, FCF는 13.28억달러에서 44억달러, 조정 영업마진은 19.2%에서 26.2%로 상승했다. 2025년에도 5개 인수를 완료했고 2026년 1월 CommScope CCS 인수를 종결했다. 주가는 두 차례 2:1 분할을 반영하면 VIC 당시 $110→$27.50에서 2026-08-28 $157.74로 약 5.74배 상승했다.',
'thesis_verdict_ko':'매우 성공','business_verdict_ko':'매우 성공','catalyst_verdict_ko':'성공','valuation_verdict_ko':'성공','stock_verdict_ko':'매우 성공','current_verdict_ko':'복리구조 강화·현재 밸류에이션은 높아짐','overall_verdict_ko':'매우 성공',
'why_ko':'단순 전자화 수요뿐 아니라 분권형 비용조정과 bolt-on M&A가 동시에 작동하면서 매출보다 EPS·FCF가 더 빠르게 성장했다. 즉 멀티플 확장만이 아니라 실제 earnings power가 크게 증가한 성공 사례다.',
'success_pattern_ko':'분권형 운영 + 볼트온 M&A 복리','failure_pattern_ko':'해당 없음','root_error_ko':'해당 없음','first_signal_ko':'2020년 말~2021년 매출 회복과 높은 마진·FCF가 동시에 유지되고 인수가 계속된 것이 초기 확인 신호였다.','first_signal_date':'2021','knowable_at_t0_ko':'중간','avoidability_ko':'해당 없음',
'counterfactual_question_ko':'전자화 수요가 둔화하는 해에도 현장 GM의 비용조정과 M&A 후 독립운영이 margin·ROIC를 지키는가?','analyst_note_ko':'이 사례의 핵심은 “전자부품 수요가 늘었다”가 아니라 조직구조가 다각화와 M&A를 오히려 장점으로 바꿨다는 점이다. 성장률 외삽보다 operating system의 재현성을 봐야 한다.',
'corrected_return_1y':0.37338684174861103,'corrected_return_3y':None,'corrected_return_5y':None,'confidence':0.99,'research_asof':'2026-08-28','research_status_ko':'사후분석 완료'}
APH_CLAIMS=[
 (1,'구조적 성장','전자화가 진행될수록 기기당 connector·sensor content가 구조적으로 증가한다.','자동차·통신·산업·데이터센터의 전자화가 장기간 지속','2020~2025 매출 85.99억→231억달러, organic growth와 M&A 모두 기여','성공','단순 end-market volume보다 content growth가 중요한 thesis였다.'),
 (2,'운영구조','분권형 GM 구조가 경기변동에 빠르게 대응해 높은 마진을 방어한다.','현장 책임자가 실시간으로 비용·자원을 조정할 권한과 인센티브 보유','조정 영업마진 2020 19.2%→2025 26.2%','성공','다각화가 복잡성을 만들기보다 비용유연성과 성장기회 포착으로 연결됐다.'),
 (3,'다각화','서로 다른 end market을 동시에 운영해 개별 산업 충격을 상쇄한다.','각 사업부가 전문기업처럼 독립적으로 운영','2020 이후 자동차·산업·모바일 변동에도 전체 매출·마진 장기 상승','성공','분권화가 conglomerate discount의 원인이 아니라 shock absorber로 작동했다.'),
 (4,'M&A/자본배분','작은 기술·niche 기업을 인수해 Amphenol의 고객·지역·공급망을 붙이면 장기 복리가 가능하다.','인수 후 경영진/문화 유지와 합리적 가격·ROIC','2025년 5개 인수 완료, 매출·FCF CAGR 20%대','매우 성공','M&A가 일회성 규모확대가 아니라 반복 가능한 성장엔진으로 남았다.'),
 (5,'밸류에이션/사이클','33x headline P/E는 비싸 보이지만 depressed earnings 정상화와 low-mid teens FCF/share 복리를 감안하면 감당 가능하다.','2021~22 경기회복과 장기 복리 지속','분할조정 주가 $27.50→$157.74, 약 5.74배; 실적성장이 멀티플 부담을 흡수','성공','비싼 주식과 과대평가된 주식은 같은 말이 아니라는 사례다.')]
APH_SOURCES=[
 (1,'2020 VIC Amphenol 투자 아이디어','Value Investors Club','2020-08-17','https://www.valueinvestorsclub.com/idea/AMPHENOL_CORP/2115263448','당시 $110, 약 $175bn TAM·4~5% 점유율, 120+ GM 분권형 조직, M&A 약 +6% 매출성장, FY20/21 P/E 33x/27x, normalized cash flow 약 25x와 low-mid teens cash flow/share growth 논리를 제시.'),
 (2,'Amphenol 2020 연간 실적','Amphenol','2021-01-27','https://investor.amphenol.com/news-and-events/news-details/2021/Amphenol-Reports-Record-Fourth-Quarter-2020-Results-and-Announces-2-for-1-Stock-Split/default.aspx','2020 매출 $8.599bn, adjusted operating margin 19.2%, adjusted EPS $3.74(당시 주식수 기준), FCF $1.328bn.'),
 (3,'Amphenol 2025 연간 실적','Amphenol','2026-01-28','https://investor.amphenol.com/news-and-events/news-details/2026/Amphenol-Reports-Record-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx','2025 매출 $23.1bn, adjusted EPS $3.34, adjusted operating margin 26.2%, FCF $4.4bn, 연중 5개 인수 완료.'),
 (4,'Amphenol 주식분할 이력','Amphenol','2026','https://investors.amphenol.com/stock-information/dividend-and-stock-split-history/default.aspx','2021-03-05와 2024-06-12에 각각 2-for-1 split. 2020년 당시 주가를 현재 주식수 기준으로 환산할 때 4로 나눠야 함.'),
 (5,'APH 2026-08-28 종가','StockAnalysis','2026-08-28','https://stockanalysis.com/stocks/aph/','2026-08-28 종가 $157.74. 두 차례 split을 반영한 2020년 당시 $27.50 대비 약 5.74배.')]

PATTERNS_ADD=[
 ('VSP017','성공','운영구조·M&A','분권형 운영 + 볼트온 M&A 복리','현장 책임자에게 손익·자원배분 권한을 주고, 작은 niche 기업의 경영진을 유지한 채 글로벌 고객·공급망을 붙여 M&A를 반복 가능한 성장엔진으로 만드는 패턴.','인수 후 3~5년이 지나도 organic growth·margin·ROIC가 유지되는가?'),
 ('VSP018','성공','구조적 성장','전자화 content growth','최종제품 생산량 자체보다 제품 한 단위 안의 전자부품·센서·데이터 연결량이 증가해 content per unit이 장기 성장하는 패턴.','end-market volume이 정체해도 content per unit과 organic sales가 실제로 증가하는가?')]

con=sqlite3.connect(DB)
c=con.cursor()
# Add long-form tables.
c.executescript('''
DROP TABLE IF EXISTS postmortem_longform;
CREATE TABLE postmortem_longform(
 idea_id TEXT PRIMARY KEY, one_line_ko TEXT, business_economics_ko TEXT, valuation_at_t0_ko TEXT,
 stock_return_summary_ko TEXT, earnings_bridge_ko TEXT, what_was_right_ko TEXT, what_was_wrong_ko TEXT,
 lesson_ko TEXT, current_watch_ko TEXT);
DROP TABLE IF EXISTS postmortem_metrics;
CREATE TABLE postmortem_metrics(
 id INTEGER PRIMARY KEY AUTOINCREMENT, idea_id TEXT, metric_order INTEGER, metric_name_ko TEXT,
 t0_period TEXT, t0_value TEXT, post_period TEXT, post_value TEXT, change_ko TEXT, interpretation_ko TEXT);
CREATE INDEX idx_postmortem_metrics_idea ON postmortem_metrics(idea_id);
DROP TABLE IF EXISTS postmortem_timeline;
CREATE TABLE postmortem_timeline(
 id INTEGER PRIMARY KEY AUTOINCREMENT, idea_id TEXT, event_order INTEGER, date_ko TEXT, event_ko TEXT, significance_ko TEXT);
CREATE INDEX idx_postmortem_timeline_idea ON postmortem_timeline(idea_id);
''')

# Add APH verified row.
cols=list(APH_POST)
if not c.execute('select 1 from postmortems where idea_id=?',(APH_ID,)).fetchone():
    c.execute(f"insert into postmortems({','.join(cols)}) values({','.join('?' for _ in cols)})",[APH_POST[k] for k in cols])
else:
    sets=','.join(f'{k}=?' for k in cols if k!='idea_id')
    c.execute(f'update postmortems set {sets} where idea_id=?',[APH_POST[k] for k in cols if k!='idea_id']+[APH_ID])
# Sync main analysis.
c.execute('''UPDATE analysis SET company_description_ko=?,thesis_summary_ko=?,actual_development_ko=?,outcome_thesis_ko=?,outcome_business_ko=?,catalyst_outcome_ko=?,outcome_valuation_ko=?,outcome_stock_ko=?,outcome_current_ko=?,overall_verdict_ko=?,failure_mechanism_ko=?,root_analytical_error_ko=?,first_contradictory_signal_ko=?,first_signal_date=?,knowable_at_t0_ko=?,avoidability_ko=?,counterfactual_question_ko=?,confidence=?,analysis_status_ko='사후분석 완료',last_updated=? WHERE idea_id=?''',(
APH_POST['company_description_ko'],APH_POST['original_thesis_ko'],APH_POST['actual_development_ko'],APH_POST['thesis_verdict_ko'],APH_POST['business_verdict_ko'],APH_POST['catalyst_verdict_ko'],APH_POST['valuation_verdict_ko'],APH_POST['stock_verdict_ko'],APH_POST['current_verdict_ko'],APH_POST['overall_verdict_ko'],APH_POST['failure_pattern_ko'],APH_POST['root_error_ko'],APH_POST['first_signal_ko'],APH_POST['first_signal_date'],APH_POST['knowable_at_t0_ko'],APH_POST['avoidability_ko'],APH_POST['counterfactual_question_ko'],APH_POST['confidence'],APH_POST['research_asof'],APH_ID))
# replace APH curated child rows
c.execute('delete from postmortem_claims where idea_id=?',(APH_ID,))
for x in APH_CLAIMS:
    c.execute('insert into postmortem_claims(idea_id,claim_order,claim_type_ko,original_claim_ko,key_assumption_ko,actual_result_ko,verdict_ko,explanation_ko) values(?,?,?,?,?,?,?,?)',(APH_ID,*x))
c.execute('delete from postmortem_sources where idea_id=?',(APH_ID,))
for x in APH_SOURCES:
    c.execute('insert into postmortem_sources(idea_id,source_order,title_ko,publisher,source_date,url,evidence_ko) values(?,?,?,?,?,?,?)',(APH_ID,*x))
for x in PATTERNS_ADD:
    c.execute('insert or replace into verified_pattern_catalog(pattern_id,polarity_ko,category_ko,pattern_name_ko,definition_ko,counterfactual_question_ko) values(?,?,?,?,?,?)',x)
c.execute('insert or replace into verified_pattern_map(idea_id,pattern_id,is_primary) values(?,?,1)',(APH_ID,'VSP017'))
c.execute('insert or replace into verified_pattern_map(idea_id,pattern_id,is_primary) values(?,?,0)',(APH_ID,'VSP018'))

# Map ticker -> idea_id, then insert longform/metrics/timeline.
rows=c.execute('select p.idea_id,p.ticker from postmortems p').fetchall()
ids={ticker:iid for iid,ticker in rows}
missing=set(ids)-set(LONG)
if missing:
    raise RuntimeError(f'LONG missing: {missing}')
for ticker,iid in ids.items():
    d=LONG[ticker]
    c.execute('''insert or replace into postmortem_longform(idea_id,one_line_ko,business_economics_ko,valuation_at_t0_ko,stock_return_summary_ko,earnings_bridge_ko,what_was_right_ko,what_was_wrong_ko,lesson_ko,current_watch_ko) values(?,?,?,?,?,?,?,?,?,?)''',(iid,d['one_line_ko'],d['business_economics_ko'],d['valuation_at_t0_ko'],d['stock_return_summary_ko'],d['earnings_bridge_ko'],d['what_was_right_ko'],d['what_was_wrong_ko'],d['lesson_ko'],d['current_watch_ko']))
    for j,m in enumerate(METRICS[ticker],1):
        c.execute('insert into postmortem_metrics(idea_id,metric_order,metric_name_ko,t0_period,t0_value,post_period,post_value,change_ko,interpretation_ko) values(?,?,?,?,?,?,?,?,?)',(iid,j,*m))
    for j,e in enumerate(TIMELINES[ticker],1):
        c.execute('insert into postmortem_timeline(idea_id,event_order,date_ko,event_ko,significance_ko) values(?,?,?,?,?)',(iid,j,*e))
con.commit()
print('postmortems',c.execute('select count(*) from postmortems').fetchone()[0])
print('claims',c.execute('select count(*) from postmortem_claims').fetchone()[0])
print('longform',c.execute('select count(*) from postmortem_longform').fetchone()[0])
print('metrics',c.execute('select count(*) from postmortem_metrics').fetchone()[0])
print('timeline',c.execute('select count(*) from postmortem_timeline').fetchone()[0])
print('integrity',c.execute('pragma integrity_check').fetchone()[0])
con.close()

# Update curated JSON snapshots for reproducibility.
CUR.mkdir(parents=True,exist_ok=True)
with sqlite3.connect(DB) as con:
    con.row_factory=sqlite3.Row
    for table,name in [('postmortem_longform','postmortem_longform.json'),('postmortem_metrics','postmortem_metrics.json'),('postmortem_timeline','postmortem_timeline.json')]:
        data=[dict(r) for r in con.execute(f'select * from {table}')]
        (CUR/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    # Refresh core curated files including APH.
    for table,name,order in [('postmortems','postmortems.json','ticker'),('postmortem_claims','postmortem_claims.json','idea_id,claim_order'),('postmortem_sources','postmortem_sources.json','idea_id,source_order'),('verified_pattern_catalog','verified_patterns.json','pattern_id'),('verified_pattern_map','verified_pattern_map.json','idea_id,pattern_id')]:
        data=[dict(r) for r in con.execute(f'select * from {table} order by {order}')]
        (CUR/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

# Re-gzip deploy DB.
GZ=ROOT/'data'/'processed'/'vic_dashboard.db.gz'
with open(DB,'rb') as src, gzip.open(GZ,'wb',compresslevel=9) as dst:
    shutil.copyfileobj(src,dst)
print('gz_mb',round(GZ.stat().st_size/1024/1024,2))
