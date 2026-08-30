"""V3 재생성 순서. 원본 local DB가 이미 존재하는 경우 02부터 실행하면 됩니다."""
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
steps=['02_build_dashboard_db.py','05_build_v3_auto_analysis.py','04_build_pattern_hub.py','06_fill_v3_preliminary_outcomes.py','03_validate_db.py']
for s in steps:
    print(f'\n=== {s} ===')
    subprocess.run([sys.executable,str(ROOT/'scripts'/s)],check=True)
print('\nV3 build complete')
