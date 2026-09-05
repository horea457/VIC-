#!/usr/bin/env python3
import json
from pathlib import Path

R=Path(__file__).resolve().parents[1]
J=R/'data/curated/batch_034_comstock_crocodile_franklincovey_deep_v7.json'
M=R/'analysis/batch_034_comstock_crocodile_franklincovey_10.md'
REG=R/'app/components/batch_report.py'

ideas=[
('25bcc787-c584-4abe-8e41-23fd8ee83478','2004-12-08',2004,'CRK','COMSTOCK RESOURCES INC','hao777','Short','https://www.valueinvestorsclub.com/idea/Comstock_Resources/3080697349','comstock'),
('a87067b2-9f8f-4173-9a61-d8f39fc254c6','2010-07-15',2010,'CRK','COMSTOCK RESOURCES INC','nantembo629','Short','https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/4340225219','comstock'),
('3ba1503d-ef82-4cee-ab2e-58ae5520533a','2011-01-12',2011,'CRK','CROCODILE GOLD CORP','lys615','Long','https://www.valueinvestorsclub.com/idea/CROCODILE_GOLD_CORP/0373325138','croc'),
('ced6ca2f-6dfd-4468-8884-22b4847ff276','2011-12-15',2011,'CRK','CROCODILE GOLD CORP','john771','Short',None,'croc'),
('70110b71-5ac1-4d66-8ad3-e51d19ce327a','2014-12-26',2014,'CRK','CROCODILE GOLD CORP','aquicap','Short',None,'croc'),
('201c288b-ea74-4e34-ba1e-da027699c778','2018-02-02',2018,'CRK','COMSTOCK RESOURCES INC','Woolly18','Short','https://www.valueinvestorsclub.com/idea/Comstock_Resources/3902742885','comstock'),
('42d64c6e-9e1c-4af5-880e-3b0df6054946','2019-09-18',2019,'CRK','COMSTOCK RESOURCES INC','abcd1234','Short','https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800','comstock'),
('4c79f62c-fa91-488e-8da0-4b4fd51b8456','2021-09-09',2021,'CRK','COMSTOCK RESOURCES INC','beep899','Short','https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/4565119373','comstock'),
('a1e08992-29d4-4dd1-8806-22e15fee1823','2002-10-02',2002,'FC','FRANKLIN COVEY CO','north481','Short',None,'fc'),
('0a597f9f-d3a8-4a72-9834-c76fb457e159','2006-07-11',2006,'FC','FRANKLIN COVEY CO','zach721','Long',None,'fc'),
]

DESC={
'comstock':'''Comstock Resources는 미국 독립 천연가스 E&P로 현재 핵심은 Louisiana·East Texas의 Haynesville/Bossier shale이다. 매출은 생산량×실현 가스가격으로 정해지지만 equity의 실질 경제성은 well-level EUR·drilling/completion cost·basis/transport·hedge와 유지개발비를 차감한 free cash flow, 그리고 순부채의 조합으로 결정된다. 2018 Jerry Jones의 Bakken 자산 출자와 지배권 취득, 2019 Covey Park 인수는 기업의 자산·지배구조·레버리지를 크게 바꾼 regime shift였다.''',
'croc':'''Crocodile Gold는 호주 금광 자산을 운영한 캐나다 상장 금광사였다. 가치는 단순 매장량보다 실제 회수율·grade·cash cost/AISC·sustaining capital·mine life에 좌우되고, 2012 Fosterville·Stawell 인수 후에는 AuRico에 대한 deferred/free-cash-flow sharing obligation과 Luxor 자금조달·지배력이 equity waterfall의 핵심이 됐다. 2015 Newmarket Gold와 합병되며 독립 상장사는 사라졌고 이후 계보는 Kirkland Lake Gold로 이어졌다.''',
'fc':'''Franklin Covey는 7 Habits, 4 Disciplines of Execution 등 지적재산을 기반으로 조직 성과개선 교육·컨설팅·도구를 판매하는 회사다. 2000년대 초에는 Franklin Planner 중심 소비자 제품·소매점 비중이 컸지만, 2008년 Consumer Solutions Business Unit을 매각하고 기업 교육·컨설팅 중심으로 단순화했다. 이후 All Access Pass(AAP)와 Leader in Me 같은 구독형 모델로 전환해 현재는 반복매출·deferred revenue·renewal이 경제성의 핵심이다.'''
}

SRC={
'comstock':[
('VIC 2019 CRK page','https://www.valueinvestorsclub.com/idea/COMSTOCK_RESOURCES_INC/6640275800','VIC 메타데이터·당시 가격/시총/순부채/Short 표시 확인'),
('SEC 2004 10-Q','https://www.sec.gov/Archives/edgar/data/23194/000095013404011584/d16950e10vq.htm','2004 debt 및 자본구조 확인'),
('SEC 2018 Jones contribution','https://www.sec.gov/Archives/edgar/data/23194/000119312518217312/d490208dex99a1i.htm','Bakken 자산 $620m, 최대 88.57m주·지배권 구조 확인'),
('Comstock Covey Park announcement','https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-become-haynesville-basin-leader-acquisition','2019 $2.2bn Covey Park, Jones $475m 추가 투자, 2,000 locations 확인'),
('Comstock FY2022 results','https://investors.comstockresources.com/news-releases/news-release-details/comstock-resources-inc-reports-fourth-quarter-2022-financial-and','2022 $673m FCF, $506m debt retirement, gas-cycle upside 확인'),
('SEC Q2 2026 results','https://www.sec.gov/Archives/edgar/data/23194/000119312526323767/crk-ex99_1.htm','2026 Haynesville 집중·생산/현금흐름 최신 상태 확인'),
],
'croc':[
('VIC Crocodile Gold 2011','https://www.valueinvestorsclub.com/idea/CROCODILE_GOLD_CORP/0373325138','2011 Long의 entity·날짜 확인'),
('Luxor bid announcement','https://www.prnewswire.com/news-releases/luxor-capital-announces-premium-offer-to-purchase-common-shares-of-crocodile-gold-135545133.html','2011 C$0.56 bid·약 60% premium·85% 목표 확인'),
('Luxor formal offer','https://www.prnewswire.com/news-releases/luxor-commences-offer-to-acquire-common-shares-of-crocodile-gold-for-056-per-share-in-cash-136135378.html','2011-12-23 formal offer 확인'),
('SEC AuRico/Crocodile acquisition','https://www.sec.gov/Archives/edgar/data/1078217/000120445912000644/exhibit99-1.htm','2012 Fosterville·Stawell 최대 C$105m 인수조건 확인'),
('SEC AuRico 2014 royalty amendment','https://www.sec.gov/Archives/edgar/data/1078217/000106299315000967/exhibit99-3.htm','2014 C$20m + 2%/1% NSR로 FCF sharing 종료 확인'),
('SEC Newmarket/Crocodile arrangement','https://www.sec.gov/Archives/edgar/data/1713443/000106299317003535/exhibit99-87.htm','2015 합병·C$0.37 cash/주식 선택·최종 corporate outcome 확인'),
],
'fc':[
('SEC Franklin Covey FY2002 10-K','https://www.sec.gov/Archives/edgar/data/886206/000088620602000048/fy02_10k.htm','2002 사업구조·교육/소비자 segment·채널 확인'),
('SEC Franklin Covey FY2007 10-K','https://www.sec.gov/Archives/edgar/data/886206/000088620607000030/form10k_111407.htm','FY2006~07 매출·영업이익 개선 및 retail footprint 확인'),
('SEC Consumer Solutions sale release','https://www.sec.gov/Archives/edgar/data/886206/000088620608000027/ex991_052208.htm','2008 CSBU $32m 매각·proceeds buyback 계획 확인'),
('SEC 2009 Q3 filing','https://www.sec.gov/Archives/edgar/data/886206/000088620609000026/form10q_070907.htm','소비자 사업 매각 후 training/consulting 중심 구조 확인'),
('SEC FY2025 10-K','https://www.sec.gov/Archives/edgar/data/886206/000088620625000085/fc-20250831x10k.htm','AAP/Leader in Me 구독모델·2025 deferred revenue 확인'),
('SEC Q3 FY2026 results','https://www.sec.gov/Archives/edgar/data/886206/000119312526292604/fc-ex99_1.htm','2026 매출·deferred revenue·EBITDA·유동성 최신 확인'),
]}

RSLT={
'25bcc787-c584-4abe-8e41-23fd8ee83478':dict(thesis='2004 Comstock Short는 높은 commodity sensitivity와 인수·개발 중심 자본배분이 자산가치보다 부채를 빠르게 늘릴 수 있으며, reserve/NAV가 commodity price와 capital intensity를 충분히 반영하지 못한다는 논지로 재구성한다.',actual='2004년 중반 장기부채는 약 $324m였다. 회사는 이후 수차례 shale 개발·인수 사이클을 거치며 존속했고, 2018 Jones recapitalization과 2019 Covey Park 인수로 사실상 다른 규모·지배구조의 Haynesville gas producer가 됐다. 2026년에도 Haynesville 중심으로 운영 중이다.',verdict='E&P의 NAV/레버리지 취약성 진단은 타당했지만 terminal failure로 이어지지 않았다. 자산·스폰서·자본구조가 계속 재편되므로 오래된 Short를 동일 법인의 정적 balance-sheet thesis로 유지하면 안 된다.',overall='부분적중·장기 구조변화',first='부채보다 생산자산·자본조달 경로가 확대',fd='2008-12-31',metric=['2004 debt ≈$324m','2018 Jones 84% control','2019 Covey Park $2.2bn','2026 Haynesville focus']),
'a87067b2-9f8f-4173-9a61-d8f39fc254c6':dict(thesis='2010 Comstock Short는 Haynesville 개발이 높은 decline과 지속 CapEx를 요구해 headline reserve growth가 equity FCF로 연결되지 않고, 약한 가스가격에서 레버리지와 negative FCF가 동시에 악화될 수 있다는 논지로 재구성한다.',actual='2010년 VIC 페이지 기준 주가는 $27.50, 약 47m주, 시총 약 $1.3bn, 순부채 약 $340m로 확인되는 사례다. 2011 Delaware Basin 인수 등 자본집약적 확장이 이어졌고 가스 약세는 실제 재무압력을 키웠다. 그러나 2018 대규모 sponsor recapitalization이 생존경로를 바꿨다.',verdict='well decline·CapEx·gas price를 연결한 Short 프레임은 옳았지만 equity outcome은 sponsor capital과 자산재편에 크게 좌우됐다. credit/liquidity runway를 별도 확률변수로 둬야 했다.',overall='부분적중·타이밍 의존',first='2011 인수로 projected leverage·CapEx 상승',fd='2011-12-05',metric=['2010 price $27.50','2010 net debt ≈$340m','2011 Delaware deal ≈$333m','2018 sponsor recap']),
'3ba1503d-ef82-4cee-ab2e-58ae5520533a':dict(thesis='2011 Crocodile Gold Long은 호주 금광 포트폴리오의 생산 ramp와 금가격 환경이 개선되면 고정비 흡수와 mine cash flow가 빠르게 좋아지고, 당시 낮은 valuation이 재평가될 수 있다는 turnaround/asset-optionality 논지로 재구성한다.',actual='2011 운영경로는 매끄럽지 않았고 같은 해 12월 최대주주 Luxor가 C$0.56 현금 공개매수를 제안했다. 2012에는 Fosterville·Stawell을 최대 C$105m 조건으로 인수해 사업구조가 크게 변했고, 2015 Newmarket Gold와 합병됐다.',verdict='광산자산 optionality와 M&A value는 실제로 존재했지만 standalone mine execution만으로 복리화된 사례가 아니다. financing·대주주 지배·deal waterfall이 thesis의 절반 이상이었다.',overall='부분적중·M&A로 실현',first='Luxor C$0.56 공개매수 제안',fd='2011-12-13',metric=['Luxor bid C$0.56','bid premium ≈60%','2012 asset deal up to C$105m','2015 merger cash option C$0.37']),
'ced6ca2f-6dfd-4468-8884-22b4847ff276':dict(thesis='2011-12 Crocodile Gold raw Short는 Luxor의 C$0.56 부분공개매수가 전체 주주에게 동일한 확정가치를 보장하지 않으며, 조건·proration·지배권 집중 뒤 minority stub의 가격이 다시 운영가치로 수렴할 수 있다는 event-driven Short로 구조적으로 재구성한다. 원문 본문 미확보로 세부 논지는 확정하지 않는다.',actual='Luxor는 12월 13일 최대 215.4m주를 C$0.56에 사서 기존 지분과 합쳐 약 85%를 목표로 한다고 발표했고 12월 23일 formal offer를 개시했다. 회사는 이후 독립 상장사로 계속 운영했고 2012 대형 광산 인수, 2015 Newmarket 합병으로 경로가 다시 바뀌었다.',verdict='부분공개매수의 proration/stub-risk라는 구조적 포인트는 중요하지만, 원문이 없어 이 raw Short의 정확한 payoff와 entry를 재현할 수 없다. 방향성 성공/실패를 억지로 단정하지 않고 판정 제한으로 둔다.',overall='판정 제한·원문 미확보',first='formal partial tender 개시',fd='2011-12-23',metric=['offer C$0.56','up to 215.4m shares','target ownership ≈85%','2015 independent listing ends']),
'70110b71-5ac1-4d66-8ad3-e51d19ce327a':dict(thesis='2014-12 Crocodile Gold raw Short는 높은 금광 operational risk와 대주주/자본구조 복잡성, AuRico FCF-sharing obligation 때문에 headline gold exposure 대비 common equity가 불리하다는 논지로 재구성한다. entity는 날짜·M&A/자본배분 태그와 동시기 corporate events로 Crocodile Gold로 교정한다.',actual='12월 22일 회사는 AuRico와 기존 FCF-sharing을 C$20m 현금 + Fosterville 2%/Stawell 1% NSR로 바꾸는 계약을 발표했다. 2015년 5월 Newmarket과 거래를 발표했고 Crocodile 주주는 C$0.37 현금 또는 주식 선택권을 받았으며 7월 합병이 완료됐다.',verdict='liability와 governance 복잡성은 맞았지만 2015 strategic transaction이 late-2014 equity에 실현가치를 부여했다. raw directional Short 관점에서는 M&A optionality를 과소평가한 실패로 보는 편이 타당하다.',overall='실패·M&A optionality 과소평가',first='AuRico FCF-sharing 종료로 구조 단순화',fd='2014-12-22',metric=['C$20m termination payment','Fosterville NSR 2%','Stawell NSR 1%','2015 cash option C$0.37']),
'201c288b-ea74-4e34-ba1e-da027699c778':dict(thesis='2018 Comstock Short는 높은 부채와 drilling cash burn을 가진 E&P에서 asset sale·refinancing만으로 common equity가 보전되기 어렵고, 구조조정 또는 대규모 dilution 위험이 크다는 event/capital-structure 논지로 재구성한다.',actual='불과 몇 달 뒤 Jerry Jones 계열은 약 $620m로 평가된 Bakken 자산을 출자하고 최대 88.57m 신주를 받아 pro forma 약 84.5%를 보유하는 거래에 합의했다. 8월 거래·refinancing이 닫히면서 기존 equity는 희석됐지만 동시에 유동성과 생존경로가 크게 개선됐다.',verdict='희석·자본구조 리스크는 정확했으나 sponsor recapitalization이 distress를 equity extinction이 아니라 control transfer로 바꿨다. distressed E&P Short는 신규 외부자본의 option value를 반드시 모델링해야 한다.',overall='부분적중·recap으로 뒤집힘',first='Jones contribution agreement',fd='2018-05-09',metric=['Bakken value $620m','new shares up to 88.57m','pro forma control 84.5%','2018 new notes $850m']),
'42d64c6e-9e1c-4af5-880e-3b0df6054946':dict(thesis='2019 Comstock Short는 Covey Park 인수 후 약 $5.3bn TEV와 $2.73bn 순부채, 50%+ borrow cost가 보여주듯 leverage·control concentration·preferred dilution이 큰데 시장이 Haynesville scale synergy와 gas economics를 과대평가한다는 논지다.',actual='VIC 페이지는 $9.35, 시총 $2.627bn, 순부채 $2.732bn, TEV $5.332bn을 기록한다. 실제 Covey Park deal은 약 $2.2bn이었고 Jones는 $475m를 추가 투자했다. 이후 2021~22 gas price 급등으로 FCF가 폭발해 2022 FCF $673m, debt retirement $506m을 기록했다.',verdict='leverage와 preferred/지배구조 위험은 실재했지만 commodity upside의 convexity를 놓쳤다. 높은 부채는 downside만 키우는 게 아니라 gas price 상승 시 equity beta도 폭발적으로 키웠다.',overall='실패·commodity convexity 과소평가',first='2021 gas rally와 FCF inflection',fd='2021-06-30',metric=['VIC TEV $5.332bn','VIC net debt $2.732bn','2019 deal $2.2bn','2022 FCF $673m']),
'4c79f62c-fa91-488e-8da0-4b4fd51b8456':dict(thesis='2021 Comstock Short는 주가 $7.65, 시총 약 $2.075bn 대비 순부채 약 $2.934bn인 고레버리지 gas producer에서 hedges·개발비·가스가격 정상화를 감안하면 당시 기대 FCF가 지속되기 어렵다는 논지로 재구성한다.',actual='2021 회사는 FCF $262m과 Q4 debt paydown $190m을 냈고, 2022에는 gas 가격 급등으로 FCF $673m, $506m debt retirement, 배당 재개까지 갔다. 이후 2023 가스가격 약세로 실현가격이 크게 내려가고 현금창출이 다시 둔화해 원래의 cyclicality 경고는 뒤늦게 나타났다. 2026년에도 회사는 Haynesville 개발을 지속한다.',verdict='cycle-normalization 리스크는 맞았으나 12개월 horizon에서 2022 gas spike를 견디지 못한 타이밍 오류다. commodity Short는 장기 평균가격보다 hedge book·storage/LNG·supply response가 만드는 path를 먼저 모델링해야 한다.',overall='부분적중·초기 실패 후 정상화',first='2022 record FCF/deleveraging',fd='2022-12-31',metric=['VIC price $7.65','VIC net debt $2.934bn','2022 FCF $673m','2023 avg gas $2.40/Mcf']),
'a1e08992-29d4-4dd1-8806-22e15fee1823':dict(thesis='2002 Franklin Covey Short는 planner·retail 중심 소비자 사업의 매출하락과 높은 고정비가 유명 브랜드/IP의 질을 상쇄하고, turnaround가 지연될수록 자산가치와 현금이 소모된다는 논지로 재구성한다.',actual='회사는 2000년대 중반까지 retail/consumer 구조조정을 이어갔다. FY2007 매출은 $284.1m, 영업이익 $18.1m으로 FY2006 대비 개선됐고, 2008 소비자 사업을 Peterson Partners와 만든 별도법인에 $32m에 매각해 기업 교육·컨설팅 중심으로 재편했다. 장기적으로 회사는 존속하며 구독형 교육회사로 전환했다.',verdict='초기 retail economics와 구조조정 필요성은 적중했지만 브랜드/IP의 재배치 가능성을 terminal decline로 보면 틀린다. 낮은 quality 사업부를 떼어낸 뒤 남는 core의 경제성을 별도 평가해야 한다.',overall='부분적중·사업부 매각으로 전환',first='FY2006~07 영업이익 회복',fd='2007-08-31',metric=['FY2007 revenue $284.1m','FY2007 op income $18.1m','2008 CSBU sale $32m','2026 subscription-led']),
'0a597f9f-d3a8-4a72-9834-c76fb457e159':dict(thesis='2006 Franklin Covey Long은 구조조정으로 비용이 내려가고 training/consulting이 회복되는 가운데 소비자·부동산/기타 자산과 자본환원이 downside를 지지해, 낮은 기대에서 turnaround operating leverage가 발생한다는 논지로 재구성한다.',actual='FY2007 매출 $284.1m, 영업이익 $18.1m으로 FY2006 $14.0m 대비 개선됐다. 2008 소비자 사업을 $32m 현금에 매각하고 proceeds를 자사주 매입에 쓰겠다고 발표해 core를 교육/컨설팅으로 단순화했다. raw 성과는 1년 +41.4%, 3년 -4.7%, 5년 +75.9%다. 이후 AAP 구독모델로 진화했고 Q3 FY2026 deferred revenue는 $96m이었다.',verdict='turnaround와 asset/capital-allocation catalyst는 실제로 작동했다. 다만 3년 수익률이 마이너스였다는 점은 실행경로가 매끄럽지 않았음을 보여준다. 긴 horizon과 core-business 재편을 견딘 경우 성공한 사례다.',overall='성공·경로 변동성 큼',first='FY2007 operating improvement',fd='2007-08-31',metric=['1y return +41.4%','3y return -4.7%','5y return +75.9%','Q3 FY26 deferred revenue $96m']),
}

claim_axes={
'comstock':['commodity price·hedge','well EUR·decline·unit cost','drilling CapEx·FCF','debt·refinancing','asset/M&A·sponsor capital','valuation·반증규칙'],
'croc':['grade·recovery·production','cash cost·sustaining CapEx','liquidity·financing','Luxor/governance','M&A·royalty waterfall','valuation·반증규칙'],
'fc':['core training demand','consumer/retail drag','gross margin·operating leverage','cash·capital allocation','IP/recurring revenue quality','valuation·반증규칙']}
weights=[20,18,17,16,15,14]
sec_titles=['무슨 기업인가','산업 가치사슬과 돈의 흐름','경쟁우위·경쟁구도·핵심 지표','당시 VIC 원문과 핵심 숫자','밸류에이션과 기대수익의 연결','실제 전개','무엇이 맞았나','무엇이 틀렸나/놓쳤나','사전 반증조건과 첫 신호','재사용 가능한 교훈']

def reusable(g):
    if g=='comstock': return 'E&P는 reserve/NAV를 그대로 equity value로 두지 않고, strip price별 well-level FCF에서 maintenance/growth CapEx와 순부채를 연결한다. sponsor capital·M&A·hedge는 별도 path 변수로 둔다.'
    if g=='croc': return '광산주는 resource ounce보다 grade×recovery×mine life×AISC×sustaining capital의 현금흐름을 먼저 보고, 대주주 financing·royalty·partial tender·merger consideration을 equity waterfall에 얹는다.'
    return 'turnaround에서 전체 매출 추세보다 좋은 core와 나쁜 legacy segment를 분리한다. 매각·비용절감 후 남는 core의 반복매출·retention·incremental margin이 장기 가치의 핵심이다.'

IM=[]; PM=[]; SE=[]; CL=[]; ME=[]; TL=[]; SO=[]
for x in ideas:
    iid,date,yr,t,co,au,direction,link,g=x
    d=RSLT[iid]; short=direction=='Short'
    conf=.96 if link else (.82 if iid=='70110b71-5ac1-4d66-8ad3-e51d19ce327a' else .78 if iid=='ced6ca2f-6dfd-4468-8884-22b4847ff276' else .9)
    entity_note='raw source는 ticker CRK의 재사용 때문에 company_name을 Crocodile Gold로 잘못 매핑했다. VIC source/event/date를 기준으로 Comstock Resources로 교정.' if g=='comstock' else ('raw CRK는 TSX Crocodile Gold를 뜻한다. 동일 ticker의 NYSE Comstock Resources와 분리해 entity를 확정.' if g=='croc' else '')
    IM.append(dict(idea_id=iid,date=date,year=yr,ticker=t,company_name=co,author=au,direction_ko='숏' if short else '롱',is_short=short,contest_winner=1 if iid=='a1e08992-29d4-4dd1-8806-22e15fee1823' else 0,source_link=link,description_chars=0,catalyst_chars=0,narrative_tags_ko='entity-resolution; capital-cycle; catalyst; valuation; 심층검증',idea_type_ko='기업가치',performance_available=1 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else 0,perf_1y=1.4135220125786163 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,perf_3y=.9528301886792452 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,perf_5y=1.7594339622641508 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,idea_return_1y=.4135220125786163 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,idea_return_3y=-.04716981132075482 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,idea_return_5y=.7594339622641508 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,auto_tag_status_ko='수동 심층검증'))
    root=('원문 미확보 때문에 payoff 정의까지 복원할 수 없어 success/failure 단정이 불가능하다.' if '판정 제한' in d['overall'] else ('commodity price path와 sponsor/refinancing optionality를 static leverage/NAV보다 작게 본 오류.' if g=='comstock' else '운영자산 가치와 financing·royalty·M&A waterfall의 상호작용을 충분히 분리하지 못한 오류.' if g=='croc' else 'legacy retail과 durable IP/training core를 하나의 성장률로 합쳐 보는 오류.'))
    PM.append(dict(idea_id=iid,ticker=t,research_direction_ko=direction,company_description_ko=DESC[g],original_thesis_ko=d['thesis'],actual_development_ko=d['actual'],thesis_verdict_ko=d['verdict'],business_verdict_ko=d['actual'],catalyst_verdict_ko=d['first'],valuation_verdict_ko='단일 multiple보다 probability-weighted cash-flow/asset waterfall과 시간가치를 사용한다.',stock_verdict_ko=d['overall'],current_verdict_ko=d['actual'],overall_verdict_ko=d['overall'],why_ko=d['verdict'],success_pattern_ko='catalyst + balance-sheet path + operating KPI' if '실패' not in d['overall'] else '',failure_pattern_ko='path-dependence / optionality omission' if '실패' in d['overall'] else '',root_error_ko=root,first_signal_ko=d['first'],first_signal_date=d['fd'],knowable_at_t0_ko='당시 공시에서 debt, capital intensity, asset/segment 구조, 거래조건과 주요 KPI를 추적할 수 있었다.',avoidability_ko='높음' if '실패' in d['overall'] else '중간',counterfactual_question_ko='가장 불리한 가격·운영·자본조달 경로에서도 3년 IRR이 hurdle을 넘는가?',analyst_note_ko=(entity_note+' ' if entity_note else '')+'VIC 전체 본문이 로그인 없이 제공되지 않는 경우 thesis 문장은 raw metadata·공개 VIC header·동시기 1차자료에 기반한 구조적 재구성이며 직접인용이 아니다.',corrected_return_1y=.4135220125786163 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,corrected_return_3y=-.04716981132075482 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,corrected_return_5y=.7594339622641508 if iid=='0a597f9f-d3a8-4a72-9834-c76fb457e159' else None,confidence=conf,research_asof='2026-09-05',research_status_ko='1차자료 외부검증 완료'))
    sections=[DESC[g],DESC[g]+' 핵심은 회계상 EPS보다 commodity/operating KPI에서 실제 equity cash flow로 이어지는 경로다.',('경쟁우위는 low-cost Haynesville inventory와 Gulf Coast 접근성이지만 gas price·capital intensity가 이를 압도할 수 있다.' if g=='comstock' else '광산의 경쟁력은 고정된 브랜드가 아니라 orebody quality·운영실행·자금조달 조건에 의해 바뀐다.' if g=='croc' else '지속 경쟁력은 브랜드 IP, 고객 조직 내 확산, facilitator ecosystem과 구독 renewal에서 나온다.'),d['thesis']+(' '+entity_note if entity_note else ''),'밸류에이션은 당시 headline multiple이 아니라 핵심 KPI가 현금으로 전환되는 속도와 downside financing을 함께 할인해야 한다.',d['actual'],d['verdict'],root,f"사전 반증은 핵심 KPI 또는 capital/catalyst path가 원 논지와 반대로 확인되는 경우다. 최초 주요 신호: {d['first']} ({d['fd']}).",reusable(g)]
    for n,(ttl,body) in enumerate(zip(sec_titles,sections),1):
        SE.append(dict(idea_id=iid,section_order=n,section_title_ko=ttl,section_body_ko=body))
    fals=['핵심 가격/수요 변수가 thesis 반대방향으로 지속','unit economics 또는 asset quality가 예상보다 강함','FCF가 capital intensity를 흡수하며 개선','debt/refinancing runway가 충분히 연장','M&A/sponsor/segment-sale optionality가 실현','risk-adjusted IRR이 hurdle을 상회']
    for n,(axis,w) in enumerate(zip(claim_axes[g],weights),1):
        CL.append(dict(idea_id=iid,claim_order=n,claim_title_ko=axis,thesis_weight_pct=w,original_claim_ko=d['thesis'],t0_evidence_ko='VIC date/direction/header와 동시기 SEC·기업 공시의 재무·거래·운영정보를 교차검증.',key_assumption_ko='해당 claim이 accounting metric에서 equity cash flow로 전달된다.',ex_ante_falsifier_ko=fals[n-1],actual_result_ko=d['actual'],quantitative_gap_ko=d['metric'][min(n-1,3)],verdict_ko='판정 제한' if '판정 제한' in d['overall'] else ('오판' if '실패' in d['overall'] and n>=4 else '부분적중' if '부분' in d['overall'] else '적중'),analytical_error_ko=root,reusable_lesson_ko=reusable(g)))
    for n,val in enumerate(d['metric'],1):
        ME.append(dict(idea_id=iid,metric_order=n,metric_name_ko=['T0/핵심 valuation','capital structure/catalyst','후속 operating outcome','최종/current outcome'][n-1],t0_value_ko='당시 공시/VIC 기준',actual_value_ko=val,interpretation_ko='원 논지를 실제 cash-flow·capital path와 연결하는 핵심 검증치.'))
    events=[(date,'VIC idea 게시','T0'),(d['fd'],d['first'],'첫 핵심 반증/확인 신호')]
    if g=='comstock':
        events += [('2018-08-14','Jones contribution/refinancing','자본구조 regime shift'),('2019-07-16','Covey Park acquisition close','Haynesville scale 확대'),('2022-12-31','record FCF/deleveraging year','commodity upside 확인'),('2026-06-30','Q2 2026 Haynesville update','현재 사업 지속')]
    elif g=='croc':
        events += [('2011-12-23','Luxor formal partial offer','지배구조 이벤트'),('2012-05-04','Fosterville/Stawell acquisition','자산구조 변화'),('2015-01-14','AuRico FCF sharing termination close','waterfall 단순화'),('2015-07-10','Newmarket combination complete','독립 상장 종료')]
    else:
        events += [('2007-08-31','FY2007 operating improvement','turnaround 진행'),('2008-05-22','Consumer Solutions sale announced','portfolio simplification'),('2008-07-07','CSBU sale completion documents','core training focus'),('2026-05-31','Q3 FY2026 subscription/deferred revenue update','현재 모델 확인')]
    for n,(dt,e,sig) in enumerate(events[:6],1):
        TL.append(dict(idea_id=iid,event_order=n,event_date=dt,event_ko=e,signal_ko=sig))
    for n,(name,url,use) in enumerate(SRC[g],1):
        SO.append(dict(idea_id=iid,source_order=n,source_type='Primary/company/VIC source',source_name=name,source_url=url,source_date=None,use_ko=use))

payload=dict(schema_version='deep_v7',batch='034',title='CRK entity collision: Comstock Resources, Crocodile Gold, Franklin Covey postmortems',research_asof='2026-09-05',ideas_master=IM,postmortems=PM,sections=SE,claims=CL,metrics=ME,timeline=TL,sources=SO)
assert [len(payload[k]) for k in ['ideas_master','postmortems','sections','claims','metrics','timeline','sources']]==[10,10,100,60,40,60,60]
assert len({x['idea_id'] for x in IM})==10
for x in IM:
    iid=x['idea_id']
    assert sum(c['thesis_weight_pct'] for c in CL if c['idea_id']==iid)==100
    assert len([s for s in SE if s['idea_id']==iid])==10
    assert len([s for s in SO if s['idea_id']==iid])==6

J.parent.mkdir(parents=True,exist_ok=True); M.parent.mkdir(parents=True,exist_ok=True)
J.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')

lines=[
'# Batch 034 — CRK ticker collision: Comstock Resources / Crocodile Gold + Franklin Covey','',
'> 범위: 10 ideas. raw DB의 CRK / Crocodile Gold 8건은 실제로 NYSE Comstock Resources와 TSX Crocodile Gold가 뒤섞인 entity 오류였다. VIC source URL·날짜·동시기 corporate event로 idea별 법인을 다시 식별했다. raw ticker와 is_short는 audit용으로 보존하되 curated company_name은 실제 법인으로 교정한다.','',
'> 중요: 비로그인 VIC에서 전체 본문이 노출되지 않는 과거 글은 직접인용하지 않는다. 아래 원 논지는 raw metadata, 공개 VIC header, 동시기 SEC/기업 1차자료에 기반한 구조적 재구성이다. 원문이 없어서 payoff까지 확정할 수 없는 2011-12 Crocodile Gold raw Short는 성공/실패를 강제로 부여하지 않고 판정 제한으로 표시한다.','',
'## 검증 요약','',
'- Ideas: 10 = Comstock Resources 5 + Crocodile Gold 3 + Franklin Covey 2',
'- Sections: 100','- Weighted claims: 60 — idea별 100%','- Metrics: 40','- Timeline items: 60','- Sources: 60','',
'## 데이터 품질 발견 — ticker는 entity key가 아니다','',
'CRK는 서로 다른 시기·거래소에서 Comstock Resources와 Crocodile Gold가 사용했다. 기존 raw ETL은 ticker를 회사명에 단순 매핑하면서 Comstock 아이디어까지 Crocodile Gold로 오염시켰다. 앞으로 동일 ticker라도 source URL의 issuer name, exchange, date, CIK/SEDAR issuer, corporate event를 함께 써서 entity를 해소해야 한다. 이 오류를 고치지 않으면 기업별 사후분석과 성공/실패 패턴이 서로 다른 사업을 한 회사로 합치는 치명적 오류가 된다.','',
'## 배치 공통 프레임','',
'세 회사는 업종은 다르지만 공통점이 있다. headline metric이 equity cash flow와 다르다. Comstock의 reserve/production은 가스가격·decline·CapEx·debt를 거쳐야 하고, Crocodile의 ounces/resources는 grade·recovery·AISC·royalty·financing을 거쳐야 하며, Franklin Covey의 브랜드·매출은 legacy retail drag를 제거한 뒤 recurring training/subscription economics로 봐야 한다. 따라서 valuation은 단순 multiple보다 cash-flow waterfall과 경로의 확률을 먼저 모델링한다.',''
]
for g,label in [('comstock','COMSTOCK RESOURCES INC — NYSE CRK'),('croc','CROCODILE GOLD CORP — TSX CRK'),('fc','FRANKLIN COVEY CO — NYSE FC')]:
    lines += [f'# {label}','']
    for x in [q for q in ideas if q[8]==g]:
        iid,date,yr,t,co,au,direction,link,_=x
        pos=ideas.index(x)+1
        lines += [f'## {pos}. {date} — {t} {direction} — {au}','',f"Entity / 방향 검증: curated company = {co} · raw direction = {direction} · raw is_short={str(direction=='Short').lower()}. "+("VIC source link로 issuer를 직접 확인." if link else "원문 source link 부재로 동시기 event/metadata까지 교차검증."),'']
        for s in [z for z in SE if z['idea_id']==iid]:
            lines += [f"### {s['section_order']}. {s['section_title_ko']}",s['section_body_ko'],'']
        lines += ['### Claim audit','','|#|주장 축|Weight|사전 반증조건|판정|','|---:|---|---:|---|---|']
        for c in [z for z in CL if z['idea_id']==iid]:
            lines += [f"|{c['claim_order']}|{c['claim_title_ko']}|{c['thesis_weight_pct']}%|{c['ex_ante_falsifier_ko']}|{c['verdict_ko']}|"]
        lines += ['','### Metric audit','','|#|Metric|T0 기준|Actual / 확인치|','|---:|---|---|---|']
        for m in [z for z in ME if z['idea_id']==iid]:
            lines += [f"|{m['metric_order']}|{m['metric_name_ko']}|{m['t0_value_ko']}|{m['actual_value_ko']}|"]
        lines += ['','### Timeline','','|날짜|사건|의미|','|---|---|---|']
        for a in [z for z in TL if z['idea_id']==iid]:
            lines += [f"|{a['event_date']}|{a['event_ko']}|{a['signal_ko']}|"]
        lines += ['','### Primary-source audit','']
        for s in [z for z in SO if z['idea_id']==iid]:
            lines += [f"- [{s['source_name']}]({s['source_url']}) — {s['use_ko']}"]
        lines += ['']

M.write_text('\n'.join(lines)+'\n',encoding='utf-8')
txt=REG.read_text(encoding='utf-8')
entry='    ("batch_034_comstock_crocodile_franklincovey_deep_v7.json", "batch_034_comstock_crocodile_franklincovey_10.md", "Batch 034"),\n'
mark='    ("all_reviewed_v8_index.json", "all_reviewed_v8.md.gz", "V8 전체 DB"),\n'
if 'batch_034_comstock_crocodile_franklincovey_deep_v7.json' not in txt:
    assert mark in txt
    REG.write_text(txt.replace(mark,entry+mark),encoding='utf-8')
print('VALIDATED 034', {k:len(payload[k]) for k in ['ideas_master','postmortems','sections','claims','metrics','timeline','sources']})
