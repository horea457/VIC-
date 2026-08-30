"""V4 사후분석 완료 레이어를 기존 dashboard SQLite DB에 적재합니다.

기본 입력: data/curated/*.json
기본 DB: data/processed/vic_dashboard.db
배포본이 gzip만 있을 경우 먼저 압축을 해제한 DB에 실행하세요.
"""
from pathlib import Path
import argparse, json, sqlite3

ROOT=Path(__file__).resolve().parents[1]
CURATED=ROOT/'data'/'curated'

def load(name):
    return json.loads((CURATED/name).read_text(encoding='utf-8'))

def main(db_path):
    con=sqlite3.connect(db_path)
    c=con.cursor()
    c.executescript('''
    DROP TABLE IF EXISTS postmortems;
    CREATE TABLE postmortems (
      idea_id TEXT PRIMARY KEY,ticker TEXT,research_direction_ko TEXT,company_description_ko TEXT,
      original_thesis_ko TEXT,actual_development_ko TEXT,thesis_verdict_ko TEXT,business_verdict_ko TEXT,
      catalyst_verdict_ko TEXT,valuation_verdict_ko TEXT,stock_verdict_ko TEXT,current_verdict_ko TEXT,
      overall_verdict_ko TEXT,why_ko TEXT,success_pattern_ko TEXT,failure_pattern_ko TEXT,root_error_ko TEXT,
      first_signal_ko TEXT,first_signal_date TEXT,knowable_at_t0_ko TEXT,avoidability_ko TEXT,
      counterfactual_question_ko TEXT,analyst_note_ko TEXT,corrected_return_1y REAL,corrected_return_3y REAL,
      corrected_return_5y REAL,confidence REAL,research_asof TEXT,research_status_ko TEXT DEFAULT '사후분석 완료');
    CREATE INDEX idx_postmortems_ticker ON postmortems(ticker);
    CREATE INDEX idx_postmortems_verdict ON postmortems(overall_verdict_ko);

    DROP TABLE IF EXISTS postmortem_claims;
    CREATE TABLE postmortem_claims (id INTEGER PRIMARY KEY AUTOINCREMENT,idea_id TEXT,claim_order INTEGER,
      claim_type_ko TEXT,original_claim_ko TEXT,key_assumption_ko TEXT,actual_result_ko TEXT,verdict_ko TEXT,explanation_ko TEXT);
    CREATE INDEX idx_postmortem_claims_idea ON postmortem_claims(idea_id);

    DROP TABLE IF EXISTS postmortem_sources;
    CREATE TABLE postmortem_sources (id INTEGER PRIMARY KEY AUTOINCREMENT,idea_id TEXT,source_order INTEGER,
      title_ko TEXT,publisher TEXT,source_date TEXT,url TEXT,evidence_ko TEXT);
    CREATE INDEX idx_postmortem_sources_idea ON postmortem_sources(idea_id);

    DROP TABLE IF EXISTS verified_pattern_catalog;
    CREATE TABLE verified_pattern_catalog (pattern_id TEXT PRIMARY KEY,polarity_ko TEXT,category_ko TEXT,
      pattern_name_ko TEXT,definition_ko TEXT,counterfactual_question_ko TEXT);
    DROP TABLE IF EXISTS verified_pattern_map;
    CREATE TABLE verified_pattern_map (idea_id TEXT,pattern_id TEXT,is_primary INTEGER DEFAULT 1,PRIMARY KEY(idea_id,pattern_id));
    CREATE INDEX idx_verified_pattern_map_pattern ON verified_pattern_map(pattern_id);
    ''')

    posts=load('postmortems.json')
    for p in posts:
        keys=list(p.keys())
        c.execute(f"INSERT INTO postmortems ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",[p[k] for k in keys])
        c.execute('''UPDATE analysis SET company_description_ko=?,thesis_summary_ko=?,actual_development_ko=?,
                     outcome_thesis_ko=?,outcome_business_ko=?,catalyst_outcome_ko=?,outcome_valuation_ko=?,
                     outcome_stock_ko=?,outcome_current_ko=?,overall_verdict_ko=?,failure_mechanism_ko=?,
                     root_analytical_error_ko=?,first_contradictory_signal_ko=?,first_signal_date=?,knowable_at_t0_ko=?,
                     avoidability_ko=?,counterfactual_question_ko=?,confidence=?,analysis_status_ko='사후분석 완료',last_updated=?
                     WHERE idea_id=?''',(
            p['company_description_ko'],p['original_thesis_ko'],p['actual_development_ko'],p['thesis_verdict_ko'],
            p['business_verdict_ko'],p['catalyst_verdict_ko'],p['valuation_verdict_ko'],p['stock_verdict_ko'],
            p['current_verdict_ko'],p['overall_verdict_ko'],p['failure_pattern_ko'],p['root_error_ko'],p['first_signal_ko'],
            p['first_signal_date'],p['knowable_at_t0_ko'],p['avoidability_ko'],p['counterfactual_question_ko'],p['confidence'],
            p['research_asof'],p['idea_id']))

    for x in load('postmortem_claims.json'):
        c.execute('''INSERT INTO postmortem_claims(idea_id,claim_order,claim_type_ko,original_claim_ko,key_assumption_ko,actual_result_ko,verdict_ko,explanation_ko)
                     VALUES(?,?,?,?,?,?,?,?)''',(x['idea_id'],x['claim_order'],x['claim_type_ko'],x['original_claim_ko'],x['key_assumption_ko'],x['actual_result_ko'],x['verdict_ko'],x['explanation_ko']))
    for x in load('postmortem_sources.json'):
        c.execute('''INSERT INTO postmortem_sources(idea_id,source_order,title_ko,publisher,source_date,url,evidence_ko)
                     VALUES(?,?,?,?,?,?,?)''',(x['idea_id'],x['source_order'],x['title_ko'],x['publisher'],x['source_date'],x['url'],x['evidence_ko']))
    for x in load('verified_patterns.json'):
        c.execute('INSERT INTO verified_pattern_catalog VALUES(?,?,?,?,?,?)',(x['pattern_id'],x['polarity_ko'],x['category_ko'],x['pattern_name_ko'],x['definition_ko'],x['counterfactual_question_ko']))
    for x in load('verified_pattern_map.json'):
        c.execute('INSERT INTO verified_pattern_map VALUES(?,?,?)',(x['idea_id'],x['pattern_id'],x['is_primary']))
    con.commit()
    print('postmortems',c.execute('select count(*) from postmortems').fetchone()[0])
    print('claims',c.execute('select count(*) from postmortem_claims').fetchone()[0])
    print('sources',c.execute('select count(*) from postmortem_sources').fetchone()[0])
    print('integrity',c.execute('pragma integrity_check').fetchone()[0])
    con.close()

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--db',default=str(ROOT/'data'/'processed'/'vic_dashboard.db'))
    args=ap.parse_args()
    main(args.db)
