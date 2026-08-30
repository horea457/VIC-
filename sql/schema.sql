-- analysis
CREATE TABLE analysis(idea_id TEXT PRIMARY KEY,company_description_ko TEXT,business_model_ko TEXT,industry_structure_ko TEXT,thesis_summary_ko TEXT,thesis_points_ko TEXT,key_assumptions_ko TEXT,falsifiers_ko TEXT,thesis_horizon_ko TEXT,catalyst_expected_ko TEXT,catalyst_outcome_ko TEXT,actual_development_ko TEXT,outcome_thesis_ko TEXT,outcome_business_ko TEXT,outcome_valuation_ko TEXT,outcome_stock_ko TEXT,outcome_current_ko TEXT,overall_verdict_ko TEXT,failure_domain_ko TEXT,failure_mechanism_ko TEXT,secondary_failure_patterns_ko TEXT,root_analytical_error_ko TEXT,transmission_mechanism_ko TEXT,first_contradictory_signal_ko TEXT,first_signal_date TEXT,knowable_at_t0_ko TEXT,avoidability_ko TEXT,counterfactual_question_ko TEXT,research_priority INTEGER,confidence REAL,analysis_status_ko TEXT DEFAULT '미분석',last_updated TEXT);

-- analytical_errors
CREATE TABLE analytical_errors(error_id INTEGER PRIMARY KEY AUTOINCREMENT,error_ko TEXT,definition_ko TEXT);

-- claims
CREATE TABLE claims(claim_id TEXT PRIMARY KEY,idea_id TEXT NOT NULL,claim_order INTEGER,claim_type_ko TEXT,claim_ko TEXT,evidence_at_t0_ko TEXT,implicit_assumption_ko TEXT,falsifier_ko TEXT,leading_indicator_ko TEXT,expected_horizon_months INTEGER,outcome_ko TEXT,outcome_confidence REAL,review_status_ko TEXT DEFAULT '미검증');

-- dataset_stats
CREATE TABLE dataset_stats(metric_ko TEXT PRIMARY KEY,value_text TEXT,value_num REAL);

-- failure_patterns
CREATE TABLE failure_patterns(pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,domain_ko TEXT,mechanism_ko TEXT,definition_ko TEXT);

-- ideas_master
CREATE TABLE ideas_master(idea_id TEXT PRIMARY KEY,date TEXT,year INTEGER,ticker TEXT,company_name TEXT,author TEXT,direction_ko TEXT,is_short INTEGER,contest_winner INTEGER,source_link TEXT,description_chars INTEGER,catalyst_chars INTEGER,narrative_tags_ko TEXT,idea_type_ko TEXT,horizon_raw TEXT,horizon_months INTEGER,performance_available INTEGER,perf_1m REAL,perf_3m REAL,perf_6m REAL,perf_1y REAL,perf_2y REAL,perf_3y REAL,perf_5y REAL,idea_return_1y REAL,idea_return_3y REAL,idea_return_5y REAL,auto_tag_status_ko TEXT);

-- signal_taxonomy
CREATE TABLE signal_taxonomy(signal_id INTEGER PRIMARY KEY AUTOINCREMENT,signal_ko TEXT,category_ko TEXT,definition_ko TEXT);

-- sqlite_sequence
CREATE TABLE sqlite_sequence(name,seq);

-- tag_summary
CREATE TABLE tag_summary(tag_ko TEXT PRIMARY KEY,ideas INTEGER);

-- year_summary
CREATE TABLE year_summary(
  year INT,
  ideas,
  long_ideas,
  short_ideas,
  contest_winners,
  performance_covered
);

-- V2 pattern hub
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
