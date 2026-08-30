# VIC 허구 반증 연구소

VIC 과거 투자 아이디어를 단순 수익률 백테스트가 아니라 **투자논지의 검증 가능성** 중심으로 재구성하는 Streamlit 프로젝트입니다.

## 현재 빌드

- 아이디어 **13,656건**
- 기간 **2000–2022년**
- 대시보드용 DB: `data/processed/vic_dashboard.db`
- 원문 전체 로컬 DB: `data/raw/vic_full_local.db` (기본 Git 제외)
- 화면과 분석 필드는 **한국어 중심**

## 핵심 철학

> 주가가 올랐다고 원래 투자논지가 맞았던 것은 아니다.

각 아이디어를 다음 순서로 저장합니다.

`기업 설명 → 당시 투자논지 → Claim → 가정 → Falsifier → 실제 전개 → Thesis/Event/Current 결과 → 실패 메커니즘 → 최초 반증 신호 → 당시 물었어야 할 질문`

## 실행

```bash
pip install -r requirements.txt
streamlit run app/Home.py
```

## 데이터 파일

- `vic_dashboard.db`: GitHub/Streamlit용 경량 DB. 메타데이터, 자동 1차 분류, 분석 스키마, 실패 taxonomy 포함
- `ideas_master.csv.gz`: 마스터 테이블의 휴대용 압축 CSV
- `vic_full_local.db`: 원문 description/catalyst까지 담은 연구용 DB. 공개 repo에는 기본 미포함

## 현재 분석 상태

메타데이터와 1차 자동 태깅은 전량 완료했습니다. `analysis` 및 `claims`의 성공/실패 정밀판정은 **의도적으로 미분석 상태**로 시작합니다. VIC 원문만 보고 사후 결과를 추정해 가짜 정답을 대량 생성하지 않기 위해서입니다. 이후 외부 사후 데이터와 연결해 `자동 예비판정 → 정밀검증 → 고신뢰` 순으로 채우는 구조입니다.

자세한 설명은 `docs/`를 참고하세요.
