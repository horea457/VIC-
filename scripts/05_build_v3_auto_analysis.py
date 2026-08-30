import sqlite3, re, json, math, statistics, html, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
FULL = ROOT/'data'/'raw'/'vic_full_local.db'
DB = ROOT/'data'/'processed'/'vic_dashboard.db'

TAG_RULES = {
 '시장규모·TAM': [('total addressable market',4),('addressable market',3),(' tam ',4),('market opportunity',1)],
 '가격결정력': [('pricing power',4),('ability to raise price',4),('raise prices',3),('price increase',2),('pricing increases',2)],
 '네트워크 효과': [('network effect',5),('network effects',5),('two-sided network',5)],
 '영업레버리지': [('operating leverage',5),('incremental margin',4),('margin expansion',2),('fixed cost leverage',4)],
 '저원가 사업자': [('low-cost producer',5),('low cost producer',5),('cost advantage',3),('lowest cost',3)],
 '산업 통합': [('industry consolidation',5),('consolidated industry',4),('market consolidation',4),('fragmented industry',3),('fragmented market',2)],
 '경영진': [('great management',5),('excellent management',5),('strong management',4),('management incentives',5),('aligned management',5),('founder-led',5),('founder led',5),('insider ownership',4),('owner operator',5),('owner-operator',5)],
 '자본배분': [('capital allocation',5),('share repurchase',4),('stock repurchase',4),('buyback',3),('special dividend',4),('deleveraging',3),('return capital',3)],
 '경기·사이클': [('cyclical',3),('industry cycle',4),('commodity cycle',4),('capacity utilization',3),('supply cycle',4),('downcycle',4),('upcycle',4)],
 '재무구조': [('net debt',2),('debt maturity',4),('refinancing',4),('financial leverage',3),('leveraged balance sheet',4),('liquidity risk',5),('covenant',4)],
 'SOTP·자산가치': [('sum of the parts',5),('sotp',5),('net asset value',4),('asset value',2),('hidden asset',4)],
 '턴어라운드': [('turnaround',5),('restructuring',3),('cost cutting',2),('normalization',2),('normalized earnings',3)],
 '회계·포렌식': [('accounting fraud',5),('accounting issue',4),('restatement',5),('working capital',2),('cash conversion',3),('aggressive accounting',5),('forensic',5)],
 '규제': [('regulatory approval',4),('regulatory risk',4),(' fda ',4),(' fcc ',4),('license renewal',4),('regulatory change',4)],
 '구조적 성장': [('secular growth',5),('structural growth',5),('long-term growth',1)],
 '반복매출': [('recurring revenue',5),('subscription revenue',4),('retention rate',3),('customer retention',3),('churn',3)],
 'M&A': [('merger arbitrage',5),('acquisition target',4),('takeover',4),('sale process',4),('strategic acquisition',3)],
 '분할·스핀오프': [('spin-off',5),('spinoff',5),('spin off',5),('separation',2)],
 '자사주': [('share repurchase',5),('stock repurchase',5),('buyback',4)],
 '청산·자산매각': [('liquidation',5),('liquidate',4),('asset sale',4),('sale of assets',4),('wind down',4)],
 '공매도·과대평가': [('overvalued',5),('overvaluation',5),('short thesis',5),('unsustainable',2),('fraud',3)],
}

# Minimum score. High-frequency generic words require more evidence.
TAG_THRESHOLD = {k:4 for k in TAG_RULES}
TAG_THRESHOLD.update({'재무구조':4,'턴어라운드':4,'회계·포렌식':4,'경기·사이클':4,'산업 통합':4,'반복매출':4,'자본배분':4})

CLAIM_LIBRARY = {
 '시장규모·TAM': ('시장규모·성장','실제 접근 가능한 시장과 침투율 확대가 장기 성장의 핵심 동력이라는 주장','시장규모가 실제 지불의사와 반복 수요로 연결된다','고객수·사용량·침투율이 예상보다 빠르게 둔화되거나 고객경제성이 악화되는가','고객수·침투율·코호트·고객 ROI'),
 '가격결정력': ('가격결정력','회사가 가격을 올려도 고객 이탈과 물량 감소가 제한적이라는 주장','제품·서비스 차별화가 가격 인상을 흡수한다','가격 인상 후 물량·유지율·고객 ROI가 악화되는가','ASP·물량·churn·gross margin'),
 '네트워크 효과': ('경제적 해자','네트워크가 커질수록 사용자 가치와 경쟁우위가 강화된다는 주장','멀티호밍과 우회가 제한되고 규모가 수익풀 보호로 이어진다','멀티호밍·탈중개·수직통합이 늘거나 take rate가 압박받는가','멀티호밍·점유율·take rate·고객/공급자 집중도'),
 '영업레버리지': ('수익성','매출 성장에 비해 비용 증가가 느려 마진이 확대된다는 주장','비용구조에 충분한 고정비 성격이 있다','증분비용이 계속 증가해 incremental margin이 낮아지는가','증분마진·판관비율·R&D율·FCF margin'),
 '저원가 사업자': ('원가우위','경쟁사 대비 낮은 원가구조가 사이클 전체에서 방어력을 제공한다는 주장','비용우위가 일시적 원재료·지역·사이클 효과가 아니다','원가곡선 이동이나 신규 저원가 공급자로 우위가 축소되는가','단위원가·원가곡선·가동률·CAPEX'),
 '산업 통합': ('산업구조','산업 통합과 퇴출이 경쟁강도를 낮추고 가격규율을 개선한다는 주장','통합 후 신규 진입과 증설이 제한된다','통합 이후에도 신규 공급·가격전쟁이 다시 나타나는가','시장점유율·신규진입·CAPEX·가격'),
 '경영진': ('경영진','경영진의 실행력·인센티브·자본배분 능력이 가치창출의 핵심이라는 주장','경영진의 말과 행동이 주주가치와 정렬되어 있다','가이던스 미달·고점 M&A·증자 등 행동이 내러티브와 어긋나는가','가이던스 적중률·M&A·자사주·내부자 거래'),
 '자본배분': ('자본배분','자사주·부채축소·배당·자산매각 등 자본배분이 주당가치를 높인다는 주장','경영진이 기대수익률에 따라 자본을 규율 있게 배분한다','고평가 자사주·고점 M&A·불필요한 CAPEX가 나타나는가','자사주 가격·M&A ROIC·순부채·CAPEX'),
 '경기·사이클': ('사이클','현재 수익성·가격이 사이클의 비정상 구간이며 정상화가 투자수익을 만든다는 주장','공급과 수요가 예상한 방향·속도로 정상화된다','증설·재고·수요가 예상보다 오래 악화되는가','가격·가동률·재고·capacity·CAPEX'),
 '재무구조': ('재무구조','부채와 유동성 구조가 투자논지의 upside/downside를 크게 좌우한다는 주장','현금흐름이 부채상환과 재융자를 충분히 감당한다','실적 악화 시 covenant·재융자·유동성 문제가 나타나는가','순부채·이자보상·만기·유동성·FCF'),
 'SOTP·자산가치': ('밸류에이션','보유 자산·사업부 가치의 합이 현재 시가총액을 의미 있게 상회한다는 주장','자산가치가 현실화 가능하고 holding discount가 영구적이지 않다','자산매각 가격·세금·부채·할인요인이 예상보다 불리한가','매각가·NAV·순부채·세금·holding discount'),
 '턴어라운드': ('턴어라운드','일시적 악화 이후 실적과 마진이 정상수준으로 회복된다는 주장','악화 원인이 구조적 경쟁력 훼손이 아니라 일시적 문제다','회복 없이 점유율·고객·마진이 계속 악화되는가','매출·마진·점유율·FCF·구조조정 진척'),
 '회계·포렌식': ('회계·현금흐름','보고이익과 실제 현금경제성 사이의 차이가 투자판단에 중요하다는 주장','회계상 수익성이 현금흐름으로 검증되거나 반대로 과장되어 있다','현금전환·운전자본·반복 조정항목이 주장과 반대로 움직이는가','FCF conversion·운전자본·조정항목·감사/재작성'),
 '규제': ('규제','규제 승인·보호·정책 변화가 사업가치 또는 촉매의 핵심이라는 주장','규제 결과와 시점이 논지에서 가정한 범위에 들어온다','승인 실패·조건 악화·정책 변경이 발생하는가','승인상태·조건·정책·법원결정'),
 '구조적 성장': ('구조적 성장','단기 경기보다 장기적인 구조 변화가 매출과 이익 성장을 지속시킨다는 주장','성장이 신규 고객의 건전한 단위경제성과 함께 지속된다','성장이 정상화된 코호트에서 둔화되고 CAC가 상승하는가','유기적 성장·고객수·사용량·CAC·retention'),
 '반복매출': ('반복매출','반복매출과 높은 유지율이 수익의 예측성과 장기 가치를 높인다는 주장','고객 유지와 사용량이 가격 인상·경기 변화에도 안정적이다','churn 상승·사용량 감소·갱신률 악화가 나타나는가','retention·churn·NRR·subscription mix'),
 'M&A': ('이벤트·M&A','인수합병 또는 매각이 가치 현실화의 핵심 경로라는 주장','거래가 예상한 조건과 시점으로 종결된다','거래 철회·가격 재협상·규제 지연이 발생하는가','거래확률·스프레드·승인·자금조달·조건'),
 '분할·스핀오프': ('이벤트·분할','분할·스핀오프로 숨겨진 가치가 분리되어 재평가된다는 주장','분할 후 각 사업의 독립가치가 비용·세금을 상회한다','분할 지연·비용 증가·독립사업 경쟁력 약화가 나타나는가','분할 일정·pro forma 비용·각 사업 valuation'),
 '자사주': ('자본환원','저평가 구간의 자사주 매입이 주당 내재가치를 높인다는 주장','매입가격이 내재가치보다 낮고 재무여력이 충분하다','고평가 매입·부채 증가·주식보상 상쇄가 발생하는가','평균매입가·주식수·SBC·순부채'),
 '청산·자산매각': ('이벤트·자산가치','자산매각·청산으로 숨겨진 가치가 현금으로 실현된다는 주장','매각가격과 비용·세금이 예상 범위에 들어온다','매각 실패·할인가 매각·비용/세금 증가가 나타나는가','매각가·순현금 유입·시점·잔여부채'),
 '공매도·과대평가': ('숏·과대평가','시장 기대가 지속가능하지 않거나 가치 대비 가격이 과도하다는 주장','실적·경쟁력·현금흐름이 시장 기대를 충족하지 못한다','기대 이상의 성장·마진·자본조달로 숏 논지가 무너지는가','실적 vs 컨센서스·FCF·밸류에이션·자본조달'),
}

SECTOR_RULES = [
 ('보험',['insurance','underwriting','premium','loss ratio','policyholder']),
 ('은행·금융',['bank ','banking','deposit','loan portfolio','net interest margin','credit card']),
 ('결제·핀테크',['payment','merchant acquiring','fintech','transaction volume','card network']),
 ('소프트웨어·SaaS',['software','saas','license revenue','subscription software','enterprise software']),
 ('인터넷·플랫폼',['marketplace','platform','online marketplace','network effect','internet company']),
 ('광고·마케팅',['advertising','adtech','advertiser','publisher','marketing services']),
 ('반도체·전자',['semiconductor','chip','wafer','memory','fabless','electronics']),
 ('제약·바이오',['biotech','pharmaceutical','clinical trial','drug candidate','fda']),
 ('헬스케어 서비스',['hospital','healthcare services','medical device','diagnostic']),
 ('에너지·석유가스',['oil','natural gas','upstream','drilling','refinery','energy company']),
 ('광산·금속',['mining','mine ','copper','gold','coal','iron ore','steel']),
 ('화학·소재',['chemical','specialty chemicals','resin','polymer','materials']),
 ('산업재·기계',['industrial','machinery','equipment','manufacturing','aerospace components']),
 ('항공우주·방산',['satellite','aerospace','defense','aircraft','missile']),
 ('통신',['telecom','wireless','broadband','carrier','subscriber']),
 ('미디어·콘텐츠',['media','broadcast','cable network','television','publishing']),
 ('리테일·유통',['retail','store','retailer','e-commerce','ecommerce']),
 ('소비재·브랜드',['consumer brand','restaurant','beverage','apparel','food company']),
 ('자동차·모빌리티',['automotive','vehicle','car ','truck','mobility']),
 ('운송·물류',['shipping','airline','freight','logistics','railroad','transportation']),
 ('부동산·리츠',['real estate','reit','property','office building','hotel portfolio']),
 ('주택·건설',['homebuilder','housing','construction','building products']),
 ('유틸리티·인프라',['utility','electricity','power generation','infrastructure']),
 ('교육',['education','student','university','school','training']),
 ('비즈니스 서비스',['business services','outsourcing','staffing','consulting','services company']),
]

PATTERN_TO_ERROR = {
 'F01':('수요','시장규모(TAM) 과대추정','TAM 오류','시장 규모 → 침투율 기대 → 실제 지불의사/유지율 부족 → 성장 둔화','고객 유지율·이탈','실제 고객이 지불할 수 있는 시장은 얼마인가?'),
 'F02':('경제적 해자','네트워크 효과 과대평가','고객 인센티브 무시','멀티호밍·우회 가능 → 네트워크의 독점성 약화 → take rate/마진 압박','고객 행동','사용자가 경쟁 네트워크를 동시에 사용할 수 있는가?'),
 'F03':('가격','가격결정력 과대평가','고객 인센티브 무시','가격 인상 → 물량·유지율 하락 → 예상 수익성 미달','가격·물량','가격을 올렸을 때 실제 volume과 churn은 어떻게 움직이는가?'),
 'F04':('비용','영업레버리지 과대평가','영업레버리지 자동 가정','성장 → 재투자·변동비 동반 증가 → incremental margin 미달','증분마진','매출 1원 증가에 실제로 얼마의 비용이 추가되는가?'),
 'F05':('경영진','경영진 내러티브 의존','경영진 내러티브 의존','경영진 가정 → 외부 데이터와 괴리 → 가이던스/실행 미달','경영진 행동','경영진 말과 독립된 외부 데이터가 같은 방향을 가리키는가?'),
 'F06':('공급·사이클','공급 반응 무시','공급반응 무시','높은 수익성 → 증설/신규진입 → 가격·마진 정상화','산업 공급·CAPEX','현재 수익성이 경쟁사의 CAPEX를 얼마나 자극하는가?'),
 'F07':('자본배분','M&A·롤업 경제성 오판','기준율 무시','인수 성장 → 유기적 경제성 약화/통합비용 → ROIC 하락','경영진 행동','인수를 멈추면 organic ROIC와 FCF는 얼마인가?'),
 'F08':('이벤트','촉매 미실현·지연','기준율 무시','이벤트 확률·시점 오판 → 가치 현실화 지연/조건 악화','규제·법원','이벤트가 없어도 downside가 충분히 보호되는가?'),
 'F09':('밸류에이션','싼 가격을 가치로 착각','단가와 가치 혼동','낮은 멀티플 → 구조적 악화 지속 → 재평가 실패/추가 디레이팅','현금전환','멀티플이 싸진 이유가 정상화 가능한가?'),
 'F10':('산업구조','가치사슬 협상력 이동','정적 산업 분석','수직통합·탈중개 → 협상력 이동 → 수익풀 축소','경쟁자 행동','누가 고객·데이터·유통을 통제하고 있는가?'),
 'F11':('회계·현금흐름','회계이익과 현금경제성 혼동','단위경제성 오독','회계이익 → 낮은 현금전환/운전자본 부담 → 내재가치 과대평가','현금전환','반복 가능한 FCF는 회계이익과 얼마나 일치하는가?'),
 'F12':('재무구조','레버리지와 유동성 과소평가','기준율 무시','작은 영업악화 → 부채/재융자 부담 → 자본손실 증폭','현금전환','매출이 예상보다 20% 낮아져도 재융자 없이 버틸 수 있는가?'),
 'F13':('경제적 해자','저원가 우위를 구조적 해자로 오인','일시적 비용우위를 해자로 오인','사이클성 비용우위 → 원가곡선 이동 → 경쟁우위 소멸','산업 공급·CAPEX','원가우위가 사이클 전체에서 유지되는가?'),
 'F14':('성장','구조적 성장과 일시적 성장 혼동','선형 외삽','초기/일시적 성장 → 정상화 → 성장률·마진 동반 하락','고객 유지율·이탈','성장이 정상화된 cohort에서도 유지되는가?'),
 'F15':('타이밍','논지는 맞지만 시간축 실패','기준율 무시','방향성은 맞아도 실현 시점 지연 → 기회비용/손실 확대','경영진 행동','논지가 맞더라도 언제까지 무엇이 일어나야 하는가?'),
}

PATTERN_TO_SUCCESS = {
 'S01':'저평가 상태에서 가치 현실화 촉매가 실제 투자수익으로 연결된 후보',
 'S02':'자본배분 개선이 주당가치 상승과 함께 나타난 후보',
 'S03':'실적 정상화와 재평가가 함께 나타난 턴어라운드 후보',
 'S04':'사이클 저점에서 공급규율과 회복이 맞물린 후보',
 'S05':'산업 통합 이후 경쟁강도 완화와 가치상승이 나타난 후보',
 'S06':'반복매출과 가격결정력이 장기 수익성으로 연결된 후보',
 'S07':'구조적 성장 논지가 실제 투자수익과 정합적으로 나타난 후보',
 'S08':'구조적 악화를 시장보다 먼저 포착한 숏 성공 후보',
}


def clean_text(t):
    if not t: return ''
    t = html.unescape(t).replace('\r',' ').replace('\n',' ')
    return re.sub(r'\s+',' ',t).strip()

def sentence_split(t):
    t=clean_text(t)
    # conservative sentence splitter
    parts=re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])',t)
    return [p.strip() for p in parts if 35 <= len(p.strip()) <= 700]

def tag_scores(desc, catalyst):
    # Thesis-heavy early text plus catalyst. Catalyst is weighted 1.5.
    d=' '+clean_text(desc[:18000]).lower()+' '
    c=' '+clean_text(catalyst[:6000]).lower()+' '
    scores={}
    for tag,rules in TAG_RULES.items():
        s=0
        for phrase,w in rules:
            n=d.count(phrase)
            nc=c.count(phrase)
            if n: s += min(n,3)*w
            if nc: s += min(nc,2)*w*1.5
        if s >= TAG_THRESHOLD[tag]: scores[tag]=round(s,1)
    # Explicit catalyst classification is itself evidence.
    cl=c
    if any(x in cl for x in ['spin-off','spinoff','spin off']): scores['분할·스핀오프']=max(scores.get('분할·스핀오프',0),8)
    if any(x in cl for x in ['liquidation','asset sale','sale of assets']): scores['청산·자산매각']=max(scores.get('청산·자산매각',0),8)
    if any(x in cl for x in ['merger','takeover','acquisition','transaction close','deal close']): scores['M&A']=max(scores.get('M&A',0),6)
    return scores

def sector_of(desc):
    z=' '+clean_text(desc[:10000]).lower()+' '
    best=('기타/복합',0)
    for sec,words in SECTOR_RULES:
        sc=sum(min(z.count(w),3) for w in words)
        if sc>best[1]: best=(sec,sc)
    return best[0]

def evidence_for_tag(desc,tag):
    rules=TAG_RULES.get(tag,[])
    sents=sentence_split(desc[:25000])
    ranked=[]
    for s in sents:
        sl=' '+s.lower()+' '
        score=sum(w*min(sl.count(p),2) for p,w in rules)
        # thesis verbs make evidence stronger
        score += 2*sum(1 for p in ['we believe','i believe','we think','i think','expect','should','upside','downside','fair value','worth'] if p in sl)
        if score>0: ranked.append((score,s))
    ranked.sort(key=lambda x:(-x[0],len(x[1])))
    return ranked[0][1] if ranked else ''

def general_evidence(desc,is_short):
    sents=sentence_split(desc[:10000])
    cues=['we believe','i believe','we think','i think','fair value','upside','downside','worth','opportunity','short opportunity']
    ranked=[]
    for s in sents:
        sl=s.lower(); sc=sum(2 for c in cues if c in sl)
        if is_short and any(x in sl for x in ['short','downside','overvalued']): sc+=3
        if not is_short and any(x in sl for x in ['upside','undervalued','cheap','worth']): sc+=3
        if sc: ranked.append((sc,s))
    ranked.sort(key=lambda x:(-x[0],len(x[1])))
    return ranked[0][1] if ranked else (sents[0] if sents else '')

def rep_return(row,hm=None):
    opts=[(12,row['idea_return_1y'],'1년'),(36,row['idea_return_3y'],'3년'),(60,row['idea_return_5y'],'5년')]
    valid=[x for x in opts if x[1] is not None]
    if not valid:return None,None
    if hm: return min(valid,key=lambda x:abs(x[0]-hm))[1], min(valid,key=lambda x:abs(x[0]-hm))[2]
    # Prefer 3y, then 1y, then 5y
    for m,v,label in [opts[1],opts[0],opts[2]]:
        if v is not None:return v,label

def stock_verdict(v):
    if v is None:return '성과자료 없음'
    if v>=.50:return '강한 성공'
    if v>=.10:return '성공'
    if v>-.10:return '혼합'
    if v>-.50:return '실패'
    return '강한 실패'

def stock_sentence(v,h):
    if v is None:return '기존 데이터셋에 비교 가능한 주가 성과가 없어 주가 결과는 미검증입니다.'
    return f'VIC 포지션 방향을 반영한 {h} 수익률은 {v:+.1%}로, 주가 결과만 보면 **{stock_verdict(v)}**에 해당합니다. 이는 원래 투자논지의 진위와는 별도입니다.'

def idea_type(catalyst):
    z=clean_text(catalyst).lower()
    maps=[('분할·스핀오프',['spin-off','spinoff','spin off']),('청산·자산매각',['liquidation','asset sale','sale of assets']),('인수합병·매각',['merger','takeover','acquisition','transaction close']),('공개매수·자본환원',['tender offer','special dividend','share repurchase','buyback']),('규제·허가',['approval','regulatory','license','permit',' fcc ',' fda ']),('소송·법원',['lawsuit','court','litigation','settlement']),('실적·가이던스',['earnings','guidance'])]
    for k,ws in maps:
        if any(w in z for w in ws):return k
    return '일반 투자논지'

def thesis_summary(company,direction,tags,itype,ret,h):
    t=', '.join(tags[:4]) if tags else '밸류에이션과 사업 전망'
    if direction=='롱':
        core=f'작성자는 **{company}**가 시장에서 과소평가되어 있다고 보고, **{t}**를 핵심 근거로 롱 아이디어를 제시했습니다.'
    else:
        core=f'작성자는 **{company}**의 시장 기대가 과도하거나 구조적 위험이 충분히 반영되지 않았다고 보고, **{t}**를 핵심 근거로 숏 아이디어를 제시했습니다.'
    if itype!='일반 투자논지': core+=f' 가치 실현 또는 논지 확인의 주요 경로로 **{itype}**가 제시된 이벤트형 성격도 있습니다.'
    if ret is not None: core+=f' 사후 주가성과는 {h} 방향조정 기준 {ret:+.1%}입니다.'
    return core

def profile_text(company,sector,direction,tags):
    focus=', '.join(tags[:3]) if tags else '일반적인 가치평가'
    return f'**{company}**는 VIC 원문을 기준으로 **{sector}** 관련 기업으로 자동 분류했습니다. 해당 VIC 아이디어는 기업 전체 소개보다 **{focus}**에 특히 초점을 둡니다. 산업 분류와 아래 사업 설명은 자동 1차 분석이므로 정밀 검증 단계에서 보완할 수 있습니다.'

def business_text(sector,tags):
    tagset=set(tags)
    extra=[]
    if '반복매출' in tagset: extra.append('반복매출과 고객 유지 경제성')
    if 'SOTP·자산가치' in tagset: extra.append('사업부·자산별 가치')
    if '경기·사이클' in tagset: extra.append('가격·가동률·공급 사이클')
    if '재무구조' in tagset: extra.append('부채와 현금흐름의 비대칭성')
    if '이벤트 드리븐' in tagset or 'M&A' in tagset or '분할·스핀오프' in tagset: extra.append('이벤트 발생 시 가치 현실화 경로')
    focus=' / '.join(extra[:3]) if extra else '매출 성장, 수익성, 현금흐름과 경쟁우위'
    return f'{sector} 기업을 평가할 때 이 아이디어가 중점적으로 보는 경제성은 **{focus}**입니다.'

def industry_text(tags):
    t=set(tags); pts=[]
    if '네트워크 효과' in t:pts.append('멀티호밍·탈중개 가능성과 네트워크의 수익화 여부')
    if '산업 통합' in t:pts.append('시장집중도와 신규진입 이후 가격규율')
    if '경기·사이클' in t:pts.append('공급증설·재고·CAPEX가 가격에 미치는 영향')
    if '저원가 사업자' in t:pts.append('원가곡선에서의 위치와 그 우위의 지속성')
    if '가격결정력' in t:pts.append('가격 인상과 물량·고객 이탈의 관계')
    if not pts:pts=['경쟁사 대응, 고객 전환비용, 신규 공급과 가치사슬 협상력']
    return '산업구조 검증의 핵심은 ' + ', '.join(pts[:3]) + '입니다.'

def pattern_rows(con,iid):
    return con.execute('''SELECT p.pattern_id,p.polarity_ko,p.category_ko,p.pattern_name_ko,p.definition_ko,p.counterfactual_question_ko,
                                 m.direction_adjusted_return,m.performance_horizon_ko,m.stock_verdict_ko,m.match_score
                          FROM idea_pattern_map m JOIN pattern_catalog p USING(pattern_id)
                          WHERE m.idea_id=? ORDER BY m.match_score DESC, ABS(COALESCE(m.direction_adjusted_return,0)) DESC''',(iid,)).fetchall()

full=sqlite3.connect(FULL); full.row_factory=sqlite3.Row
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
cur=con.cursor()

# Batch args: python script.py START END. START=0 initializes V3 tables.
start_idx=int(sys.argv[1]) if len(sys.argv)>1 else 0
end_idx=int(sys.argv[2]) if len(sys.argv)>2 else 13656

# Schema additions
cols={r['name'] for r in con.execute('pragma table_info(claims)')}
if 'source_excerpt_en' not in cols: cur.execute('ALTER TABLE claims ADD COLUMN source_excerpt_en TEXT')
if start_idx==0:
    cur.executescript('''
    DROP TABLE IF EXISTS idea_auto_profile;
    CREATE TABLE idea_auto_profile(
     idea_id TEXT PRIMARY KEY,
     sector_ko TEXT,
     tag_scores_json TEXT,
     representative_horizon_ko TEXT,
     representative_return REAL,
     stock_verdict_ko TEXT,
     source_thesis_excerpt_en TEXT,
     source_catalyst_excerpt_en TEXT,
     auto_verification_level_ko TEXT,
     external_verification_needed INTEGER DEFAULT 1
    );
    CREATE INDEX IF NOT EXISTS idx_profile_sector ON idea_auto_profile(sector_ko);
    ''')
    cur.execute('DELETE FROM claims')
    con.commit()
else:
    cur.execute('''CREATE TABLE IF NOT EXISTS idea_auto_profile(idea_id TEXT PRIMARY KEY,sector_ko TEXT,tag_scores_json TEXT,representative_horizon_ko TEXT,representative_return REAL,stock_verdict_ko TEXT,source_thesis_excerpt_en TEXT,source_catalyst_excerpt_en TEXT,auto_verification_level_ko TEXT,external_verification_needed INTEGER DEFAULT 1)''')

# Pull current master into dict
masters={r['idea_id']:r for r in con.execute('select * from ideas_master')}
q="""SELECT i.id,d.description,ca.catalysts FROM ideas i LEFT JOIN descriptions d ON d.idea_id=i.id LEFT JOIN catalyst ca ON ca.idea_id=i.id ORDER BY i.date,i.id LIMIT ? OFFSET ?"""
profiles=[]; claims=[]; tag_count=Counter(); sector_count=Counter(); update_master=[]

def evidence_map(desc, tags):
    if not tags:return {}
    sents=sentence_split(desc[:22000])
    best={t:(-1,'') for t in tags}
    for sent in sents:
        sl=' '+sent.lower()+' '
        thesis_bonus=2*sum(1 for p in ['we believe','i believe','we think','i think','expect','should','upside','downside','fair value','worth'] if p in sl)
        for tag in tags:
            sc=thesis_bonus + sum(w*min(sl.count(p),2) for p,w in TAG_RULES.get(tag,[]))
            if sc>best[tag][0]:best[tag]=(sc,sent)
    return {t:v[1] for t,v in best.items() if v[0]>0}

for n,r in enumerate(full.execute(q,(end_idx-start_idx,start_idx)),start_idx+1):
    iid=r['id']; m=masters.get(iid)
    if not m:continue
    desc=r['description'] or ''; catalyst=r['catalysts'] or ''
    scores=tag_scores(desc,catalyst)
    tags=[k for k,v in sorted(scores.items(), key=lambda kv:(-kv[1],kv[0]))][:7]
    itype=idea_type(catalyst)
    if itype!='일반 투자논지' and itype!='실적·가이던스':
        if '이벤트 드리븐' not in tags: tags.append('이벤트 드리븐')
    tags=tags[:8]
    evmap=evidence_map(desc,[t for t in tags if t!='이벤트 드리븐'])
    tag_count.update(tags)
    sector=sector_of(desc); sector_count[sector]+=1
    ret,h=rep_return(m,m['horizon_months'])
    gen_ev=general_evidence(desc,bool(m['is_short']))
    profiles.append((iid,sector,json.dumps(scores,ensure_ascii=False),h,ret,stock_verdict(ret),gen_ev,clean_text(catalyst)[:1800],'자동 예비분석',1))
    update_master.append((json.dumps(tags,ensure_ascii=False),itype,'자동 V3 태깅',iid))
    for order,tag in enumerate(tags[:6],1):
        if tag=='이벤트 드리븐':
            ctype='이벤트'; ctext=f'{itype}의 실행 여부와 조건이 가치 현실화의 핵심이라는 주장'; ass='이벤트가 예상한 기간과 조건으로 발생한다'; fals='이벤트 취소·지연·조건 악화가 발생하는가'; lead='공식 일정·승인·거래조건·스프레드'; ev=clean_text(catalyst)[:1200]
        else:
            lib=CLAIM_LIBRARY.get(tag)
            if not lib:continue
            ctype,ctext,ass,fals,lead=lib; ev=evmap.get(tag,'')
        claims.append((f'{iid}:{order}',iid,order,ctype,ctext,'아래 VIC 원문 근거를 기반으로 자동 추출',ass,fals,lead,m['horizon_months'],None,None,'자동 예비분석',ev))
    if len(profiles)>=2000:
        cur.executemany('INSERT OR REPLACE INTO idea_auto_profile VALUES (?,?,?,?,?,?,?,?,?,?)',profiles)
        cur.executemany('UPDATE ideas_master SET narrative_tags_ko=?,idea_type_ko=?,auto_tag_status_ko=? WHERE idea_id=?',update_master)
        cur.executemany('''INSERT INTO claims(claim_id,idea_id,claim_order,claim_type_ko,claim_ko,evidence_at_t0_ko,implicit_assumption_ko,falsifier_ko,leading_indicator_ko,expected_horizon_months,outcome_ko,outcome_confidence,review_status_ko,source_excerpt_en) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',claims)
        con.commit(); profiles=[];claims=[];update_master=[]
        print('processed',n,flush=True)
if profiles:
    cur.executemany('INSERT OR REPLACE INTO idea_auto_profile VALUES (?,?,?,?,?,?,?,?,?,?)',profiles)
    cur.executemany('UPDATE ideas_master SET narrative_tags_ko=?,idea_type_ko=?,auto_tag_status_ko=? WHERE idea_id=?',update_master)
    cur.executemany('''INSERT INTO claims(claim_id,idea_id,claim_order,claim_type_ko,claim_ko,evidence_at_t0_ko,implicit_assumption_ko,falsifier_ko,leading_indicator_ko,expected_horizon_months,outcome_ko,outcome_confidence,review_status_ko,source_excerpt_en) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',claims)
    con.commit()

# Rebuild tag summary from all processed master rows so batches compose correctly.
all_tag_count=Counter()
for rr in con.execute('select narrative_tags_ko from ideas_master'):
    try: all_tag_count.update(json.loads(rr[0] or '[]'))
    except Exception: pass
cur.execute('DELETE FROM tag_summary')
cur.executemany('INSERT INTO tag_summary(tag_ko,ideas) VALUES (?,?)',all_tag_count.most_common())
con.commit()
print('batch',start_idx,end_idx,'profiles',con.execute('select count(*) from idea_auto_profile').fetchone()[0],'claims',con.execute('select count(*) from claims').fetchone()[0])
print('top tags',all_tag_count.most_common(15))
con.close();full.close()
