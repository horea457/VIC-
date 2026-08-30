import sqlite3,os,json,re,statistics,gzip,csv
from collections import Counter
from pathlib import Path
ROOT=str(Path(__file__).resolve().parents[1]); full=f'{ROOT}/data/raw/vic_full_local.db'; outp=f'{ROOT}/data/processed/vic_dashboard.db'
con=sqlite3.connect(full); 
if os.path.exists(outp): os.remove(outp)
out=sqlite3.connect(outp);out.execute('PRAGMA synchronous=OFF');out.execute('PRAGMA journal_mode=OFF')
out.executescript('''
CREATE TABLE ideas_master(idea_id TEXT PRIMARY KEY,date TEXT,year INTEGER,ticker TEXT,company_name TEXT,author TEXT,direction_ko TEXT,is_short INTEGER,contest_winner INTEGER,source_link TEXT,description_chars INTEGER,catalyst_chars INTEGER,narrative_tags_ko TEXT,idea_type_ko TEXT,horizon_raw TEXT,horizon_months INTEGER,performance_available INTEGER,perf_1m REAL,perf_3m REAL,perf_6m REAL,perf_1y REAL,perf_2y REAL,perf_3y REAL,perf_5y REAL,idea_return_1y REAL,idea_return_3y REAL,idea_return_5y REAL,auto_tag_status_ko TEXT);
CREATE TABLE analysis(idea_id TEXT PRIMARY KEY,company_description_ko TEXT,business_model_ko TEXT,industry_structure_ko TEXT,thesis_summary_ko TEXT,thesis_points_ko TEXT,key_assumptions_ko TEXT,falsifiers_ko TEXT,thesis_horizon_ko TEXT,catalyst_expected_ko TEXT,catalyst_outcome_ko TEXT,actual_development_ko TEXT,outcome_thesis_ko TEXT,outcome_business_ko TEXT,outcome_valuation_ko TEXT,outcome_stock_ko TEXT,outcome_current_ko TEXT,overall_verdict_ko TEXT,failure_domain_ko TEXT,failure_mechanism_ko TEXT,secondary_failure_patterns_ko TEXT,root_analytical_error_ko TEXT,transmission_mechanism_ko TEXT,first_contradictory_signal_ko TEXT,first_signal_date TEXT,knowable_at_t0_ko TEXT,avoidability_ko TEXT,counterfactual_question_ko TEXT,research_priority INTEGER,confidence REAL,analysis_status_ko TEXT DEFAULT '미분석',last_updated TEXT);
CREATE TABLE claims(claim_id TEXT PRIMARY KEY,idea_id TEXT NOT NULL,claim_order INTEGER,claim_type_ko TEXT,claim_ko TEXT,evidence_at_t0_ko TEXT,implicit_assumption_ko TEXT,falsifier_ko TEXT,leading_indicator_ko TEXT,expected_horizon_months INTEGER,outcome_ko TEXT,outcome_confidence REAL,review_status_ko TEXT DEFAULT '미검증');
CREATE TABLE failure_patterns(pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,domain_ko TEXT,mechanism_ko TEXT,definition_ko TEXT);
CREATE TABLE analytical_errors(error_id INTEGER PRIMARY KEY AUTOINCREMENT,error_ko TEXT,definition_ko TEXT);
CREATE TABLE signal_taxonomy(signal_id INTEGER PRIMARY KEY AUTOINCREMENT,signal_ko TEXT,category_ko TEXT,definition_ko TEXT);
CREATE TABLE dataset_stats(metric_ko TEXT PRIMARY KEY,value_text TEXT,value_num REAL);
''')
# concise but detailed taxonomies
failure_patterns=[
('수요','일시적 수요를 구조적 수요로 착각','일시적 수요를 장기 추세로 외삽'),('수요','시장규모(TAM) 과대추정','실제 지불의사보다 큰 시장규모를 사용'),('수요','침투율 선형 외삽','초기 침투율 속도가 지속된다고 가정'),('수요','고객 포화','핵심 고객군 포화'),('수요','고객 ROI 악화','고객 경제성 악화'),('수요','대체재에 의한 수요 잠식','대체 기술·채널의 침투'),
('공급','공급 반응 무시','높은 수익성이 증설을 유인'),('공급','증설 리드타임 오판','공급 증가 시점 오판'),('공급','저원가 공급자 신규 진입','산업 원가곡선 이동'),
('경쟁','신규 진입','진입장벽 과대평가'),('경쟁','기존 강자의 반격','기존 강자의 대응 과소평가'),('경쟁','수직통합','고객·공급자의 내재화'),('경쟁','탈중개화','중간 단계 제거'),('경쟁','멀티호밍','여러 플랫폼 동시 사용'),('경쟁','상품화','차별화 약화'),('경쟁','가격전쟁','가격 경쟁으로 수익성 악화'),('경쟁','기능 복제','핵심 기능 복제'),('경쟁','유통 상실','핵심 채널 의존성 현실화'),
('경제적 해자','전환비용 과대평가','실제 전환비용이 낮음'),('경제적 해자','네트워크 효과 과대평가','규모가 경쟁우위로 충분히 전환되지 않음'),('경제적 해자','브랜드 가치 과대평가','브랜드가 가격결정력으로 연결되지 않음'),('경제적 해자','규모의 경제 과대평가','규모 증가의 원가우위 부족'),('경제적 해자','데이터 우위 과대평가','데이터의 독점성·효용 부족'),
('가격','가격결정력 과대평가','가격 인상 시 이탈·물량 감소 과소평가'),('가격','가격-물량 탄력성 오판','수요 탄력성 추정 실패'),
('비용','영업레버리지 과대평가','성장이 마진 개선으로 연결되지 않음'),('비용','변동비를 고정비로 오인','매출과 함께 비용도 증가'),('비용','정상마진 과대추정','고점 마진을 정상으로 간주'),
('자본집약도','유지보수 투자 과소평가','유지 CAPEX 과소평가'),('자본집약도','운전자본 부담 과소평가','성장에 필요한 현금소요 과소평가'),
('경영진','경영진 내러티브 의존','외부 데이터보다 경영진 설명을 과도하게 신뢰'),('경영진','인센티브 오판','경영진과 주주 이해관계 일치 가정 실패'),
('자본배분','고점 M&A','고점에 비싼 인수'),('자본배분','저점 자본회수','침체기에 좋은 자본배분 기회 상실'),('자본배분','롤업 경제성 붕괴','인수 없는 유기적 경제성이 약함'),('자본배분','자사주 매입 가치훼손','고평가 구간 자사주 매입'),
('재무구조','레버리지 과소평가','부채가 변동성을 증폭'),('재무구조','유동성 착시','표면상 유동성과 실제 가용 현금 차이'),
('회계','조정이익 의존','반복 비용을 제외한 조정지표에 의존'),('회계','매출 인식 착시','매출과 현금경제성 불일치'),('회계','운전자본 현금흐름 착시','일시적 운전자본 유입을 FCF로 오인'),
('산업구조','가치사슬 협상력 이동','산업 수익풀과 협상력의 이동'),('산업구조','정적인 산업구조 가정','현재 산업구조가 유지된다고 가정'),
('기술','기술 대체','신기술이 기존 경제성 훼손'),('기술','기술 도입 속도 오판','도입 속도 과대·과소 추정'),
('규제','규제 보호 약화','규제 기반 진입장벽 약화'),('규제','규제 승인 실패·지연','핵심 승인·정책 실행 실패 또는 지연'),
('밸류에이션','멀티플 정상화 오판','역사적 멀티플 회귀 가정 실패'),('밸류에이션','성장과 가치 혼동','성장률 자체를 가치 근거로 사용'),('밸류에이션','고점 이익 자본화','사이클 고점 이익에 정상 멀티플 적용'),
('타이밍','논지는 맞지만 너무 이름','투자기간 내 실현 실패'),('타이밍','촉매 시점 오판','촉매가 예상보다 지연'),('이벤트','이벤트 미발생','핵심 이벤트 미발생'),('이벤트','조건 변경','이벤트 조건 악화'),('이벤트','규제·소송 변수','규제·법원 결과가 기대와 다름')]
errors=[('선형 외삽','최근 성장률·마진·점유율 추세가 계속된다고 가정'),('기준율 무시','유사 사례의 역사적 결과를 충분히 반영하지 않음'),('생존자 편향','성공 사례만 보고 실패 사례 배제'),('경영진 내러티브 의존','외부 데이터보다 경영진 설명을 과신'),('TAM 오류','거대한 시장규모를 실제 수익 잠재력과 동일시'),('단가와 가치 혼동','낮은 멀티플 자체를 저평가 근거로 사용'),('단위경제성 오독','CAC·LTV·churn·contribution margin 오판'),('영업레버리지 자동 가정','성장하면 비용률이 자동 하락한다고 가정'),('고점 마진 정상화 오류','비정상적 고마진을 정상으로 간주'),('일시적 비용우위를 해자로 오인','사이클 비용우위를 구조적 해자로 해석'),('공급반응 무시','고수익이 신규 공급을 유인하는 점 누락'),('고객 인센티브 무시','우회·멀티호밍·대체재 선택 유인 간과'),('경쟁자 인센티브 무시','경쟁자의 가격·투자 대응 유인 간과'),('정적 산업 분석','산업 구조와 가치사슬을 고정된 것으로 가정'),('주가 결과로 논지를 정당화','주가 상승과 원래 논지의 정확성을 동일시')]
sig=[('시장점유율','경쟁력','점유율 방향·증분 점유율'),('고객 유지율·이탈','수요','retention, churn, cohort'),('가격·물량','가격','ASP, 가격 인상률, volume elasticity'),('단위경제성','경제성','CAC, LTV, contribution margin'),('증분마진','비용','incremental margin, 영업레버리지'),('산업 공급·CAPEX','공급','capacity, 증설, 수주잔고, CAPEX'),('재고','공급·운전자본','inventory days, 채널재고'),('경쟁자 행동','경쟁','가격·CAPEX·신제품·수직통합·M&A'),('고객 행동','산업구조','멀티호밍, 내재화, 우회, 벤더 다변화'),('경영진 행동','경영진','가이던스, M&A, 자사주, 증자'),('현금전환','회계','FCF conversion, working capital, capex'),('규제·법원','규제','승인, 정책, 소송, 허가')]
out.executemany('INSERT INTO failure_patterns(domain_ko,mechanism_ko,definition_ko) VALUES (?,?,?)',failure_patterns)
out.executemany('INSERT INTO analytical_errors(error_ko,definition_ko) VALUES (?,?)',errors)
out.executemany('INSERT INTO signal_taxonomy(signal_ko,category_ko,definition_ko) VALUES (?,?,?)',sig)
# fast keyword map - any match only, first 16k chars
K=[('시장규모·TAM',[' tam ','total addressable market','addressable market']),('가격결정력',['pricing power','price increase']),('네트워크 효과',['network effect']),('영업레버리지',['operating leverage','margin expansion','incremental margin']),('저원가 사업자',['low-cost producer','low cost producer','cost advantage']),('산업 통합',['consolidation','consolidated','fragmented industry']),('경영진',['management',' ceo ','founder']),('자본배분',['capital allocation','buyback','repurchase','dividend']),('이벤트 드리븐',['spin-off','spinoff','tender offer','merger','acquisition','liquidation','asset sale','approval','lawsuit']),('경기·사이클',['cyclical',' cycle ','capacity','commodity']),('재무구조',['balance sheet','leverage','net debt']),('SOTP·자산가치',['sum of the parts','sotp',' nav ','asset value']),('턴어라운드',['turnaround','restructuring','cost cutting']),('회계·포렌식',['accounting','fraud','working capital']),('규제',['regulatory',' fda ',' fcc ','license']),('구조적 성장',['secular growth','structural growth']),('반복매출',['recurring revenue','subscription','retention','churn']),('M&A',['acquisition','merger']),('분할·스핀오프',['spin-off','spinoff','separation']),('자사주',['buyback','share repurchase']),('청산·자산매각',['liquidation','asset sale']),('공매도·과대평가',['overvalued','overvaluation','short thesis','unsustainable'])]
horizon_re=re.compile(r'\b(\d{1,2})(?:\s*(?:-|to|–|—)\s*(\d{1,2}))?\s*(months?|years?)\b',re.I)
def get_tags(txt):
    z=' '+(txt or '')[:16000].lower()+' '
    return [tag for tag,words in K if any(w in z for w in words)][:8]
def get_horizon(txt):
    m=horizon_re.search((txt or '')[:16000])
    if not m:return None,None
    a=int(m.group(1)); b=int(m.group(2)) if m.group(2) else a; avg=(a+b)/2
    months=round(avg*12) if m.group(3).lower().startswith('year') else round(avg)
    return m.group(0),months
def get_type(txt):
    z=(txt or '').lower()
    maps=[('인수합병·매각',['merger','acquisition','takeover','asset sale']),('분할·스핀오프',['spin-off','spinoff','separation']),('공개매수·자본환원',['tender offer','special dividend','share repurchase','buyback']),('청산·회수',['liquidation','wind down']),('규제·허가',['approval','regulatory','license','permit']),('소송·법원',['lawsuit','court','litigation','settlement']),('실적·가이던스',['earnings','guidance'])]
    for k,ws in maps:
        if any(w in z for w in ws):return k
    return '일반 투자논지'
q='''SELECT i.id,i.date,i.company_id,c.company_name,u.username,i.is_short,i.is_contest_winner,i.link,d.description,ca.catalysts,p.oneMonthPerf,p.threeMonthPerf,p.sixMonthPerf,p.oneYearPerf,p.twoYearPerf,p.threeYearPerf,p.fiveYearPerf FROM ideas i LEFT JOIN companies c ON c.ticker=i.company_id LEFT JOIN users u ON u.user_link=i.user_id LEFT JOIN descriptions d ON d.idea_id=i.id LEFT JOIN catalyst ca ON ca.idea_id=i.id LEFT JOIN performance p ON p.idea_id=i.id ORDER BY i.date'''
batch=[];ab=[];stats=Counter();tagc=Counter();lens=[];years=[]
for r in con.execute(q):
    iid,date,ticker,company,author,isshort,contest,link,desc,cat,p1m,p3m,p6m,p1y,p2y,p3y,p5y=r; year=int(date[:4]) if date else None
    txt=(desc or '')+'\n'+(cat or ''); tg=get_tags(txt); tagc.update(tg); hr,hm=get_horizon(txt); perf=int(any(x is not None for x in [p1m,p3m,p6m,p1y,p2y,p3y,p5y]))
    dr=lambda f:None if f is None else ((1-f) if isshort else (f-1))
    batch.append((iid,date,year,ticker,company,author,'숏' if isshort else '롱',isshort,contest,link,len(desc or ''),len(cat or ''),json.dumps(tg,ensure_ascii=False),get_type(cat or ''),hr,hm,perf,p1m,p3m,p6m,p1y,p2y,p3y,p5y,dr(p1y),dr(p3y),dr(p5y),'자동 1차 태깅'))
    ab.append((iid,'미분석'));stats['ideas']+=1;stats['desc']+=bool(desc);stats['cat']+=bool(cat);stats['perf']+=perf;stats['short']+=bool(isshort);stats['long']+=not bool(isshort);stats['contest']+=bool(contest);lens.append(len(desc or ''));years.append(year)
    if len(batch)>=3000:
        out.executemany('INSERT INTO ideas_master VALUES ('+','.join('?'*28)+')',batch);out.executemany('INSERT INTO analysis(idea_id,analysis_status_ko) VALUES (?,?)',ab);out.commit();batch=[];ab=[]
if batch:
    out.executemany('INSERT INTO ideas_master VALUES ('+','.join('?'*28)+')',batch);out.executemany('INSERT INTO analysis(idea_id,analysis_status_ko) VALUES (?,?)',ab);out.commit()
out.executemany('INSERT INTO dataset_stats VALUES (?,?,?)',[
('전체 아이디어',f"{stats['ideas']:,}",stats['ideas']),('본문 보유',f"{stats['desc']:,}",stats['desc']),('Catalyst 보유',f"{stats['cat']:,}",stats['cat']),('롱 아이디어',f"{stats['long']:,}",stats['long']),('숏 아이디어',f"{stats['short']:,}",stats['short']),('Contest Winner',f"{stats['contest']:,}",stats['contest']),('기존 성과데이터 보유',f"{stats['perf']:,}",stats['perf']),('본문 길이 중앙값',f"{int(statistics.median(lens)):,}",statistics.median(lens))])
out.executescript('''CREATE TABLE year_summary AS SELECT year,COUNT(*) ideas,SUM(CASE WHEN is_short=0 THEN 1 ELSE 0 END) long_ideas,SUM(CASE WHEN is_short=1 THEN 1 ELSE 0 END) short_ideas,SUM(contest_winner) contest_winners,SUM(performance_available) performance_covered FROM ideas_master GROUP BY year;CREATE TABLE tag_summary(tag_ko TEXT PRIMARY KEY,ideas INTEGER);CREATE INDEX idx_master_ticker ON ideas_master(ticker);CREATE INDEX idx_master_company ON ideas_master(company_name);CREATE INDEX idx_master_author ON ideas_master(author);CREATE INDEX idx_master_year ON ideas_master(year);''')
out.executemany('INSERT INTO tag_summary VALUES (?,?)',tagc.most_common());out.commit();out.close();con.close()
# csv gzip
c=sqlite3.connect(outp); gz=f'{ROOT}/data/processed/ideas_master.csv.gz'
with gzip.open(gz,'wt',encoding='utf-8',newline='') as f:
    cur=c.execute('SELECT * FROM ideas_master');w=csv.writer(f);w.writerow([x[0] for x in cur.description]);w.writerows(cur)
c.close()
print('DONE',dict(stats),'db_MB',os.path.getsize(outp)/1048576,'csv_gz_MB',os.path.getsize(gz)/1048576,'top_tags',tagc.most_common(12),'years',min(y for y in years if y),max(y for y in years if y))
