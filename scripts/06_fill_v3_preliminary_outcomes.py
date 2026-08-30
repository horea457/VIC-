import sqlite3, json
from pathlib import Path
from datetime import date
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'data'/'processed'/'vic_dashboard.db'
con=sqlite3.connect(DB);con.row_factory=sqlite3.Row
cur=con.cursor()

def tags(x):
    try:return json.loads(x or '[]')
    except:return []

def company_desc(I,P):
    ts=tags(I['narrative_tags_ko']); focus=', '.join(ts[:3]) if ts else '일반 가치평가'; sec=P['sector_ko'] if P else '기타/복합'
    return f'**{I["company_name"] or I["ticker"]}**는 VIC 원문상 **{sec}** 관련 기업으로 자동 분류했습니다. 이 아이디어는 기업 전체보다 **{focus}**에 초점을 두고 있습니다. 사업 분류는 원문 기반 자동 1차 분석이며 외부 사업자료 검증 전입니다.'

def business_text(I):
    ts=set(tags(I['narrative_tags_ko'])); pts=[]
    for k,v in [('반복매출','반복매출·고객유지'),('SOTP·자산가치','사업부·자산별 가치'),('경기·사이클','가격·가동률·공급사이클'),('재무구조','부채·현금흐름'),('가격결정력','가격-물량 탄력성')]:
        if k in ts:pts.append(v)
    if not pts:pts=['매출·마진·현금흐름·경쟁우위']
    return f'사업모델 검증에서는 **{" / ".join(pts[:3])}**가 핵심 경제성입니다. 원문에서 추출한 Claim과 반증조건을 함께 확인할 수 있습니다.'

def industry_text(I):
    ts=set(tags(I['narrative_tags_ko'])); pts=[]
    for k,v in [('네트워크 효과','멀티호밍·탈중개와 네트워크 수익화'),('산업 통합','시장집중도·신규진입·가격규율'),('경기·사이클','공급증설·재고·CAPEX'),('저원가 사업자','원가곡선과 신규 저원가 공급자'),('가격결정력','가격 인상 이후 물량·이탈')]:
        if k in ts:pts.append(v)
    if not pts:pts=['경쟁사 대응·고객 전환비용·가치사슬 협상력']
    return '산업구조 측면에서는 **'+' / '.join(pts[:3])+'**를 우선 확인해야 합니다.'

def thesis_summary(I,P):
    ts=tags(I['narrative_tags_ko']); focus=', '.join(ts[:4]) if ts else '밸류에이션과 사업 전망'; co=I['company_name'] or I['ticker']
    s=(f'작성자는 **{co}**가 시장에서 과소평가되어 있다고 보고, **{focus}**를 핵심 근거로 롱 아이디어를 제시했습니다.' if I['direction_ko']=='롱' else f'작성자는 **{co}**의 시장 기대가 과도하거나 구조적 위험이 충분히 반영되지 않았다고 보고, **{focus}**를 핵심 근거로 숏 아이디어를 제시했습니다.')
    if I['idea_type_ko']!='일반 투자논지':s+=f' 주요 가치 실현/확인 경로는 **{I["idea_type_ko"]}**로 분류됩니다.'
    if P and P['representative_return'] is not None:s+=f' 사후 {P["representative_horizon_ko"]} 방향조정 주가수익률은 {P["representative_return"]:+.1%}입니다.'
    return s

def stock_verdict(v):
    if v is None:return '미검증'
    if v>=.5:return '강한 성공'
    if v>=.1:return '성공'
    if v>-.1:return '혼합'
    if v>-.5:return '실패'
    return '강한 실패'

def outcome_stock(P):
    if not P or P['representative_return'] is None:return '미검증 — 기존 성과 데이터 없음'
    return f'자동 예비판정: {stock_verdict(P["representative_return"])} ({P["representative_horizon_ko"]} 방향조정 수익률 {P["representative_return"]:+.1%})'

def overall(P):
    if not P or P['representative_return'] is None:return '미검증'
    v=P['representative_return']
    if v>=.5:return '주가 기준 강한 성공 후보 — 논지 인과관계는 외부 검증 필요'
    if v>=.1:return '주가 기준 성공 후보 — 논지 인과관계는 외부 검증 필요'
    if v>-.1:return '혼합 후보 — 투자논지별 분해 검증 필요'
    if v>-.5:return '주가 기준 실패 후보 — 실패 메커니즘 외부 검증 필요'
    return '주가 기준 강한 실패 후보 — 실패 메커니즘 외부 검증 필요'

FAIL={
 'F01':('수요','시장규모(TAM) 과대추정','TAM 오류','시장 규모 → 침투율 기대 → 실제 지불의사/유지율 부족 → 성장 둔화','고객 유지율·이탈','높음','실제 고객이 지불할 수 있는 시장은 얼마인가?'),
 'F02':('경제적 해자','네트워크 효과 과대평가','고객 인센티브 무시','멀티호밍·우회 가능 → 네트워크 독점성 약화 → take rate·마진 압박','고객 행동','높음','사용자가 경쟁 네트워크를 동시에 사용할 수 있는가?'),
 'F03':('가격','가격결정력 과대평가','고객 인센티브 무시','가격 인상 → 물량·유지율 하락 → 예상 수익성 미달','가격·물량','높음','가격을 올렸을 때 실제 volume과 churn은 어떻게 움직이는가?'),
 'F04':('비용','영업레버리지 과대평가','영업레버리지 자동 가정','성장 → 재투자·변동비 동반 증가 → incremental margin 미달','증분마진','높음','매출 1원 증가에 실제로 얼마의 비용이 추가되는가?'),
 'F05':('경영진','경영진 내러티브 의존','경영진 내러티브 의존','경영진 가정 → 외부 데이터와 괴리 → 실행/가이던스 미달','경영진 행동','중간','경영진 말과 독립된 외부 데이터가 같은 방향을 가리키는가?'),
 'F06':('공급·사이클','공급 반응 무시','공급반응 무시','높은 수익성 → 증설·신규진입 → 가격·마진 정상화','산업 공급·CAPEX','높음','현재 수익성이 경쟁사의 CAPEX를 얼마나 자극하는가?'),
 'F07':('자본배분','M&A·롤업 경제성 오판','기준율 무시','인수 성장 → 유기적 경제성 약화/통합비용 → ROIC 하락','경영진 행동','중간','인수를 멈추면 organic ROIC와 FCF는 얼마인가?'),
 'F08':('이벤트','촉매 미실현·지연','기준율 무시','이벤트 확률·시점 오판 → 가치 현실화 지연/조건 악화','규제·법원','중간','이벤트가 없어도 downside가 충분히 보호되는가?'),
 'F09':('밸류에이션','싼 가격을 가치로 착각','단가와 가치 혼동','낮은 멀티플 → 구조적 악화 지속 → 재평가 실패','현금전환','중간','멀티플이 싸진 이유가 정상화 가능한가?'),
 'F10':('산업구조','가치사슬 협상력 이동','정적 산업 분석','수직통합·탈중개 → 협상력 이동 → 수익풀 축소','경쟁자 행동','높음','누가 고객·데이터·유통을 통제하고 있는가?'),
 'F11':('회계·현금흐름','회계이익과 현금경제성 혼동','단위경제성 오독','회계이익 → 낮은 현금전환/운전자본 부담 → 내재가치 과대평가','현금전환','높음','반복 가능한 FCF는 회계이익과 얼마나 일치하는가?'),
 'F12':('재무구조','레버리지와 유동성 과소평가','기준율 무시','작은 영업악화 → 부채/재융자 부담 → 자본손실 증폭','현금전환','높음','매출이 예상보다 20% 낮아져도 재융자 없이 버틸 수 있는가?'),
 'F13':('경제적 해자','저원가 우위를 구조적 해자로 오인','일시적 비용우위를 해자로 오인','사이클 비용우위 → 원가곡선 이동 → 경쟁우위 소멸','산업 공급·CAPEX','높음','원가우위가 사이클 전체에서 유지되는가?'),
 'F14':('성장','구조적 성장과 일시적 성장 혼동','선형 외삽','초기/일시적 성장 → 정상화 → 성장률·마진 동반 하락','고객 유지율·이탈','높음','성장이 정상화된 cohort에서도 유지되는가?'),
 'F15':('타이밍','논지는 맞지만 시간축 실패','기준율 무시','방향성은 맞아도 실현 시점 지연 → 기회비용/손실 확대','경영진 행동','중간','논지가 맞더라도 언제까지 무엇이 일어나야 하는가?')}

# Load everything once: avoids ~100k SQLite round trips.
profiles={r['idea_id']:r for r in con.execute('select * from idea_auto_profile')}
claims=defaultdict(list)
for r in con.execute('select idea_id,claim_order,claim_ko,implicit_assumption_ko,falsifier_ko from claims order by idea_id,claim_order'):claims[r['idea_id']].append(r)
patterns=defaultdict(list)
for r in con.execute('''select m.idea_id,p.pattern_id,p.polarity_ko,p.pattern_name_ko,p.category_ko,p.counterfactual_question_ko,m.match_score from idea_pattern_map m join pattern_catalog p using(pattern_id) order by m.idea_id,m.match_score desc'''):patterns[r['idea_id']].append(r)

updates=[]; claim_updates=[]
for I in con.execute('select * from ideas_master'):
    iid=I['idea_id']; P=profiles.get(iid); C=claims.get(iid,[]); Pats=patterns.get(iid,[]); ret=P['representative_return'] if P else None
    thesis_pts='\n'.join(f'{j+1}. {x["claim_ko"]}' for j,x in enumerate(C[:6])) or '자동 Claim 미추출'
    assumptions='\n'.join(f'- {x["implicit_assumption_ko"]}' for x in C[:5]) or '정밀 Claim 추출 필요'
    falsifiers='\n'.join(f'- {x["falsifier_ko"]}' for x in C[:5]) or '정밀 Claim 추출 필요'
    fails=[p for p in Pats if p['polarity_ko']=='실패']; sec=', '.join(p['pattern_name_ko'] for p in fails[1:4]) if len(fails)>1 else None
    anatomy=FAIL.get(fails[0]['pattern_id']) if fails else (None,None,None,None,None,None,None)
    domain,mech,err,trans,sig,know,q=anatomy
    event_expected=f'원문 catalyst 기준 **{I["idea_type_ko"]}**' if I['idea_type_ko']!='일반 투자논지' else '특정 단일 이벤트보다 사업·밸류에이션 정상화가 중심인 아이디어'
    event_out='자동 판정 보류 — 실제 이벤트 발생 여부 외부 검증 필요' if I['idea_type_ko']!='일반 투자논지' else '해당 없음 또는 외부 검증 필요'
    valuation='자동 예비판정: 재평가/가치실현 성공 후보' if ret is not None and ret>=.1 else ('자동 예비판정: 가치함정·재평가 실패 후보' if ret is not None and ret<=-.1 else '혼합 또는 미검증')
    thesis='주가 결과와 정합적인 성공 후보 — 원래 Claim의 실제 성립 여부는 외부 검증 필요' if ret is not None and ret>=.1 else ('주가 결과와 정합적인 실패 후보 — 원래 Claim의 실제 실패 여부는 외부 검증 필요' if ret is not None and ret<=-.1 else '혼합/미검증')
    actual=(f'현재 DB에서 확인 가능한 사후정보는 {P["representative_horizon_ko"]} 방향조정 주가수익률 {ret:+.1%}입니다. ' if P and ret is not None else '현재 DB에 충분한 사후 주가정보가 없습니다. ')+'사업·산업·이벤트의 실제 전개는 별도 외부 검증값과 분리합니다.'
    priority=(25 if I['contest_winner'] else 0)+(min(45,int(abs(ret)*25)) if ret is not None else 0)+min(20,len(Pats)*4)+(10 if I['year'] and I['year']<=2020 else 0);priority=min(priority,100)
    conf=.82 if P and ret is not None and len(tags(I['narrative_tags_ko']))>=2 else (.68 if P and ret is not None else .48)
    updates.append((company_desc(I,P),business_text(I),industry_text(I),thesis_summary(I,P),thesis_pts,assumptions,falsifiers,(f'원문에서 추출된 예상기간: {I["horizon_raw"]}' if I['horizon_raw'] else '명시적 기간 미추출 — Claim별/이벤트별 검증 필요'),event_expected,event_out,actual,thesis,'외부 사업데이터 검증 필요',valuation,outcome_stock(P),'2026년 현재 상태 외부 검증 필요',overall(P),domain,mech,sec,err,trans,sig,None,know,('높음' if know=='높음' else '중간' if know=='중간' else None),q,priority,conf,'자동 예비분석',date.today().isoformat(),iid))
    cver='주가와 정합적 성공 후보' if ret is not None and ret>=.1 else ('주가와 정합적 실패 후보' if ret is not None and ret<=-.1 else '미검증/혼합')
    claim_updates.append((cver,.45 if ret is not None else None,'자동 예비분석',iid))

cur.executemany('''UPDATE analysis SET company_description_ko=?,business_model_ko=?,industry_structure_ko=?,thesis_summary_ko=?,thesis_points_ko=?,key_assumptions_ko=?,falsifiers_ko=?,thesis_horizon_ko=?,catalyst_expected_ko=?,catalyst_outcome_ko=?,actual_development_ko=?,outcome_thesis_ko=?,outcome_business_ko=?,outcome_valuation_ko=?,outcome_stock_ko=?,outcome_current_ko=?,overall_verdict_ko=?,failure_domain_ko=?,failure_mechanism_ko=?,secondary_failure_patterns_ko=?,root_analytical_error_ko=?,transmission_mechanism_ko=?,first_contradictory_signal_ko=?,first_signal_date=?,knowable_at_t0_ko=?,avoidability_ko=?,counterfactual_question_ko=?,research_priority=?,confidence=?,analysis_status_ko=?,last_updated=? WHERE idea_id=?''',updates)
cur.executemany('UPDATE claims SET outcome_ko=?,outcome_confidence=?,review_status_ko=? WHERE idea_id=?',claim_updates)
cur.executescript('''
DROP TABLE IF EXISTS sector_summary;
CREATE TABLE sector_summary AS SELECT p.sector_ko,COUNT(*) ideas,SUM(CASE WHEN p.representative_return>=0.1 THEN 1 ELSE 0 END) success_candidates,SUM(CASE WHEN p.representative_return<=-0.1 THEN 1 ELSE 0 END) failure_candidates,AVG(p.representative_return) avg_direction_return FROM idea_auto_profile p GROUP BY p.sector_ko ORDER BY ideas DESC;
DROP TABLE IF EXISTS verification_queue;
CREATE TABLE verification_queue AS SELECT i.idea_id,i.date,i.ticker,i.company_name,i.author,i.direction_ko,i.contest_winner,a.research_priority,a.overall_verdict_ko,a.failure_mechanism_ko,a.analysis_status_ko,p.representative_horizon_ko,p.representative_return FROM ideas_master i JOIN analysis a USING(idea_id) LEFT JOIN idea_auto_profile p USING(idea_id) ORDER BY a.research_priority DESC,ABS(COALESCE(p.representative_return,0)) DESC;
''')
con.commit()
print('analysis',con.execute('select analysis_status_ko,count(*) from analysis group by 1').fetchall())
print('claims',con.execute('select count(*) from claims').fetchone()[0],'profiles',len(profiles),'pattern_cases',sum(len(v) for v in patterns.values()))
con.close()
