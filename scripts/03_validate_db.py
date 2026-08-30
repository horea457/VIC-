import sqlite3, sys
p=sys.argv[1] if len(sys.argv)>1 else 'data/processed/vic_dashboard.db'
c=sqlite3.connect(p)
checks={'ideas_master':13656,'analysis':13656,'idea_auto_profile':13656,'failure_patterns':55,'analytical_errors':15,'signal_taxonomy':12,'pattern_catalog':23}
fail=False
for t,n in checks.items():
    got=c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'{t}: {got:,} / expected {n:,}')
    fail |= got != n
claims=c.execute('select count(*) from claims').fetchone()[0]
patterns=c.execute('select count(*) from idea_pattern_map').fetchone()[0]
auto=c.execute("select count(*) from analysis where analysis_status_ko='자동 예비분석'").fetchone()[0]
print(f'claims: {claims:,}')
print(f'pattern links: {patterns:,}')
print(f'auto analyses: {auto:,}')
print('연도:', c.execute('SELECT MIN(year),MAX(year) FROM ideas_master').fetchone())
print('integrity:', c.execute('PRAGMA integrity_check').fetchone()[0])
fail |= claims==0 or patterns==0 or auto!=13656
print('검증:', 'FAIL' if fail else 'OK')
raise SystemExit(1 if fail else 0)
