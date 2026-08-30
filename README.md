# VIC Falsification DB — V6 Lean

Streamlit 배포 화면을 3개로 통합한 경량 버전입니다.

1. `Home.py` — 메인 현황/검색
2. `성공·실패 요인 분석` — 패턴 → 기업/아이디어 → 심층분석
3. `사후분석 DB` — 기업별 전체 심층 리포트

## 배포
압축을 풀고 **안의 파일/폴더 전체를 GitHub 저장소 루트에 업로드**합니다.
기존 `app/pages` 안의 예전 페이지 파일은 삭제하는 것을 권장합니다.

DB는 GitHub 웹 업로드 안정성을 위해 `data/processed/vic_dashboard.db.gz.part00~03`으로 분할되어 있습니다. 앱 실행 시 자동 결합/압축해제합니다.
