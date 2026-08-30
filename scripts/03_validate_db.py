import sqlite3, sys
p=sys.argv[1] if len(sys.argv)>1 else 'data/processed/vic_dashboard.db'
c=sqlite3.connect(p)
checks={'ideas_master':13656,'analysis':13656,'failure_patterns':55,'analytical_errors':15,'signal_taxonomy':12}
fail=False
for t,n in checks.items():
    got=c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'{t}: {got:,}')
    fail |= got != n
print('연도:', c.execute('SELECT MIN(year),MAX(year) FROM ideas_master').fetchone())
print('검증:', 'FAIL' if fail else 'OK')
raise SystemExit(1 if fail else 0)
