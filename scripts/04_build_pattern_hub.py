import sqlite3, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'data' / 'processed' / 'vic_dashboard.db'

SUCCESS_PATTERNS = [
    ('S01','성공','이벤트·자산가치','저평가 + 촉매 현실화','싼 가격만이 아니라 스핀오프·자산매각·M&A·청산 등 가치 현실화 경로가 실제로 존재했던 유형','촉매가 없었어도 가치가 현실화됐을까?'),
    ('S02','성공','자본배분','자본배분 개선','자사주·부채축소·배당·비핵심 자산매각 등 자본배분 변화가 주주가치로 연결된 유형','경영진이 실제 행동으로 자본배분을 바꾸고 있는가?'),
    ('S03','성공','턴어라운드','실적 정상화 + 밸류에이션 회복','일시적 악화 이후 매출·마진·현금흐름이 정상화되며 저평가가 해소된 유형','회복의 원인이 구조적 개선인가 단순 평균회귀인가?'),
    ('S04','성공','사이클','사이클 저점 + 공급규율','가격·가동률이 바닥인 국면에서 공급축소·CAPEX 억제와 함께 회복한 유형','수요보다 공급행동이 실제로 바뀌었는가?'),
    ('S05','성공','산업구조','산업 통합 + 경쟁강도 완화','산업 통합·퇴출·점유율 재편이 가격규율과 수익성 개선으로 이어진 유형','통합 이후에도 신규 공급과 가격경쟁이 억제되는가?'),
    ('S06','성공','퀄리티','반복매출 + 가격결정력','반복매출·고객유지·가격결정력이 함께 작동해 복리성장이 확인된 유형','가격 인상 뒤에도 유지율과 사용량이 유지되는가?'),
    ('S07','성공','성장','구조적 성장의 실제 실현','큰 TAM 서사가 아니라 고객수·사용량·단위경제성으로 성장의 질이 확인된 유형','성장률이 아니라 신규 고객의 경제성이 유지되는가?'),
    ('S08','성공','숏','구조적 악화의 선행 포착','숏 아이디어에서 경쟁력·회계·재무구조 악화를 시장보다 먼저 포착한 유형','악화가 일시적 변동이 아니라 구조적이라는 증거가 무엇인가?'),
]

FAIL_PATTERNS = [
    ('F01','실패','수요','시장규모(TAM) 과대추정','큰 시장을 실제 지불의사와 동일시하거나 초기 침투율을 장기 수요로 외삽한 유형','실제 고객이 지불할 수 있는 시장은 얼마인가?'),
    ('F02','실패','경제적 해자','네트워크 효과 과대평가','멀티호밍·우회·낮은 전환비용 때문에 네트워크 효과가 기대만큼 수익풀을 보호하지 못한 유형','사용자가 경쟁 네트워크를 동시에 사용할 수 있는가?'),
    ('F03','실패','가격','가격결정력 과대평가','가격 인상 시 물량·이탈·고객 ROI 악화를 과소평가한 유형','가격을 올렸을 때 실제 volume과 churn은 어떻게 움직이는가?'),
    ('F04','실패','비용','영업레버리지 과대평가','성장하면 비용률이 자동으로 하락한다고 가정했지만 변동비와 재투자가 계속된 유형','매출 1원 증가에 실제로 얼마의 비용이 추가되는가?'),
    ('F05','실패','경영진','경영진 내러티브 의존','가이던스·TAM·시너지 등 경영진 설명을 외부 데이터보다 과신한 유형','경영진 말과 독립된 외부 데이터가 같은 방향을 가리키는가?'),
    ('F06','실패','공급·사이클','공급 반응 무시','높은 가격·수익성이 증설과 신규 진입을 유인하는 점을 놓친 유형','현재 수익성이 경쟁사의 CAPEX를 얼마나 자극하는가?'),
    ('F07','실패','자본배분','M&A·롤업 경제성 오판','인수에 의존한 성장의 유기적 경제성과 인수 후 수익률을 과대평가한 유형','인수를 멈추면 organic ROIC와 FCF는 얼마인가?'),
    ('F08','실패','이벤트','촉매 미실현·지연','스핀오프·매각·승인·소송 등 핵심 이벤트가 발생하지 않거나 조건이 악화된 유형','이벤트가 없어도 downside가 충분히 보호되는가?'),
    ('F09','실패','밸류에이션','싼 가격을 가치로 착각','낮은 멀티플 자체를 안전마진으로 보고 구조적 악화를 충분히 반영하지 못한 유형','멀티플이 싸진 이유가 정상화 가능한가?'),
    ('F10','실패','산업구조','가치사슬 협상력 이동','수직통합·탈중개화·고객 내재화로 수익풀이 다른 플레이어로 이동한 유형','누가 고객·데이터·유통을 통제하고 있는가?'),
    ('F11','실패','회계·현금흐름','회계이익과 현금경제성 혼동','조정이익·운전자본·매출인식 때문에 실제 현금창출력을 과대평가한 유형','반복 가능한 FCF는 회계이익과 얼마나 일치하는가?'),
    ('F12','실패','재무구조','레버리지와 유동성 과소평가','부채·담보·재융자·유동성이 작은 사업 악화를 큰 자본손실로 증폭한 유형','매출이 예상보다 20% 낮아져도 재융자 없이 버틸 수 있는가?'),
    ('F13','실패','경제적 해자','저원가 우위를 구조적 해자로 오인','사이클·원재료·지역효과에 따른 비용우위를 영구적 경쟁우위로 해석한 유형','원가우위가 사이클 전체에서 유지되는가?'),
    ('F14','실패','성장','구조적 성장과 일시적 성장 혼동','일시적 수요·채널효과·초기 침투를 장기 구조적 성장으로 해석한 유형','성장이 정상화된 cohort에서도 유지되는가?'),
    ('F15','실패','타이밍','논지는 맞지만 시간축 실패','방향은 맞았지만 투자기간 내 촉매·정상화가 나타나지 않아 기회비용 또는 손실이 커진 유형','논지가 맞더라도 언제까지 무엇이 일어나야 하는가?'),
]

TAG_RULES_SUCCESS = {
    'S01': {'any':['이벤트 드리븐','SOTP·자산가치','분할·스핀오프','청산·자산매각','M&A']},
    'S02': {'any':['자본배분','자사주']},
    'S03': {'any':['턴어라운드']},
    'S04': {'any':['경기·사이클','저원가 사업자']},
    'S05': {'any':['산업 통합']},
    'S06': {'all_any_groups':[['반복매출'],['가격결정력','네트워크 효과']]},
    'S07': {'any':['구조적 성장','시장규모·TAM']},
    'S08': {'short':True, 'any':['공매도·과대평가','회계·포렌식','재무구조','경영진']},
}

TAG_RULES_FAIL = {
    'F01': {'any':['시장규모·TAM']},
    'F02': {'any':['네트워크 효과']},
    'F03': {'any':['가격결정력']},
    'F04': {'any':['영업레버리지']},
    'F05': {'any':['경영진']},
    'F06': {'any':['경기·사이클','저원가 사업자']},
    'F07': {'any':['M&A','자본배분']},
    'F08': {'any':['이벤트 드리븐','분할·스핀오프','청산·자산매각','규제']},
    'F09': {'any':['SOTP·자산가치','공매도·과대평가']},
    'F10': {'any':['산업 통합','네트워크 효과']},
    'F11': {'any':['회계·포렌식']},
    'F12': {'any':['재무구조']},
    'F13': {'any':['저원가 사업자']},
    'F14': {'any':['구조적 성장','시장규모·TAM']},
    'F15': {'any':['이벤트 드리븐','턴어라운드','경기·사이클']},
}

def tags_of(raw):
    try:
        v=json.loads(raw or '[]')
        return set(v if isinstance(v,list) else [])
    except Exception:
        return set()

def rule_match(rule, tags, is_short):
    if rule.get('short') and not is_short:
        return False
    if 'any' in rule and not any(t in tags for t in rule['any']):
        return False
    for group in rule.get('all_any_groups',[]):
        if not any(t in tags for t in group):
            return False
    return True

def representative_return(r):
    # 3년을 우선 사용. 없으면 1년, 그 다음 5년.
    for horizon, key in [('3년','idea_return_3y'),('1년','idea_return_1y'),('5년','idea_return_5y')]:
        if r[key] is not None:
            return horizon, float(r[key])
    return None, None

def stock_verdict(v):
    if v is None: return '성과자료 없음'
    if v >= 0.50: return '주가 기준 강한 성공'
    if v >= 0.10: return '주가 기준 성공'
    if v > -0.10: return '주가 기준 혼합'
    if v > -0.50: return '주가 기준 실패'
    return '주가 기준 강한 실패'

conn=sqlite3.connect(DB)
conn.row_factory=sqlite3.Row
cur=conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS pattern_catalog;
DROP TABLE IF EXISTS idea_pattern_map;
DROP TABLE IF EXISTS pattern_stats;
CREATE TABLE pattern_catalog(
 pattern_id TEXT PRIMARY KEY,
 polarity_ko TEXT NOT NULL,
 category_ko TEXT,
 pattern_name_ko TEXT NOT NULL,
 definition_ko TEXT,
 counterfactual_question_ko TEXT,
 verification_level_ko TEXT DEFAULT '자동 후보'
);
CREATE TABLE idea_pattern_map(
 idea_id TEXT NOT NULL,
 pattern_id TEXT NOT NULL,
 match_type_ko TEXT NOT NULL,
 match_score REAL,
 evidence_basis_ko TEXT,
 performance_horizon_ko TEXT,
 direction_adjusted_return REAL,
 stock_verdict_ko TEXT,
 thesis_verdict_ko TEXT DEFAULT '미검증',
 PRIMARY KEY(idea_id, pattern_id)
);
CREATE TABLE pattern_stats(
 pattern_id TEXT PRIMARY KEY,
 matched_ideas INTEGER,
 performance_ideas INTEGER,
 positive_rate REAL,
 median_return REAL,
 strong_success INTEGER,
 strong_failure INTEGER
);
''')
for row in SUCCESS_PATTERNS + FAIL_PATTERNS:
    cur.execute('INSERT INTO pattern_catalog(pattern_id,polarity_ko,category_ko,pattern_name_ko,definition_ko,counterfactual_question_ko) VALUES(?,?,?,?,?,?)', row)

ideas=conn.execute('SELECT idea_id,is_short,narrative_tags_ko,idea_return_1y,idea_return_3y,idea_return_5y FROM ideas_master').fetchall()
for r in ideas:
    tags=tags_of(r['narrative_tags_ko'])
    horizon, ret=representative_return(r)
    if ret is None:
        continue
    is_short=bool(r['is_short'])
    # 자동 후보는 성과 방향과 서사 태그의 교집합. 인과판정이 아님.
    if ret >= 0.10:
        for pid,rule in TAG_RULES_SUCCESS.items():
            if rule_match(rule,tags,is_short):
                matched = sorted(tags & set(rule.get('any', []))) if rule.get('any') else sorted(tags)
                evidence='당시 서사 태그: ' + ', '.join(matched)
                cur.execute('INSERT OR IGNORE INTO idea_pattern_map VALUES(?,?,?,?,?,?,?,?,?)',
                            (r['idea_id'],pid,'자동 후보',0.60,evidence,horizon,ret,stock_verdict(ret),'미검증'))
    elif ret <= -0.10:
        for pid,rule in TAG_RULES_FAIL.items():
            if rule_match(rule,tags,is_short):
                evidence='당시 서사 태그: ' + ', '.join(sorted(tags & set(rule.get('any',[]))))
                cur.execute('INSERT OR IGNORE INTO idea_pattern_map VALUES(?,?,?,?,?,?,?,?,?)',
                            (r['idea_id'],pid,'자동 후보',0.55,evidence,horizon,ret,stock_verdict(ret),'미검증'))

# stats
for p in conn.execute('SELECT pattern_id FROM pattern_catalog').fetchall():
    vals=[x[0] for x in conn.execute('SELECT direction_adjusted_return FROM idea_pattern_map WHERE pattern_id=? AND direction_adjusted_return IS NOT NULL',(p['pattern_id'],)).fetchall()]
    if vals:
        vals2=sorted(vals)
        n=len(vals2)
        med=vals2[n//2] if n%2 else (vals2[n//2-1]+vals2[n//2])/2
        pos=sum(v>0 for v in vals2)/n
        ss=sum(v>=.5 for v in vals2)
        sf=sum(v<=-.5 for v in vals2)
    else:
        n=0; med=None; pos=None; ss=0; sf=0
    cur.execute('INSERT INTO pattern_stats VALUES(?,?,?,?,?,?,?)',(p['pattern_id'],n,n,pos,med,ss,sf))
conn.commit()

print('patterns', conn.execute('select count(*) from pattern_catalog').fetchone()[0])
print('maps', conn.execute('select count(*) from idea_pattern_map').fetchone()[0])
for r in conn.execute('''select p.polarity_ko,p.pattern_name_ko,s.matched_ideas,s.median_return from pattern_catalog p join pattern_stats s using(pattern_id) order by p.polarity_ko,s.matched_ideas desc'''):
    print(tuple(r))
