# Batch 운영 인덱스

이 문서는 `analysis/`와 `data/curated/`의 운영 정본을 구분한다. Git 이력은 삭제된
구형 파일을 보존하므로 production 경로에는 현재 정본만 둔다.

## 상태

| 배치 | 상태 | 비고 |
|---|---|---|
| 001–034 | production deep | Batch 031–034 누락 meta 보완 |
| 035 | superseded | ePlus·Plus500·LVLT 10건 전부 Batch 043–045로 대체 |
| 036 | production deep | 중복 CIT 3건은 Batch 046 정본으로 이동 |
| 037 | production deep | 중복 CIT 4건은 Batch 047 정본으로 이동 |
| 038 | production deep | 누락 wrapper 복구 |
| 039 | superseded | NXST·SBGI 10건 전부 Batch 043·044·055로 대체 |
| 040–057 | production deep | 아이디어별 V9 정본 + wrapper |
| 058–062 | staging catalog | Markdown 정본은 보존, 구조화 deep payload는 미완성 |
| 063 | production deep | 완전한 postmortem·claim·metric·timeline·source 포함 |
| 064 | production deep | Batch 043 표준의 10개 장문 보고서·60 weighted claims·50 metrics·80 events·86 sources |
| 065 | production deep | Batch 043 표준의 10개 장문 보고서·60 weighted claims·50 metrics·80 events·73 sources |
| 066–073 | staging catalog | Markdown 정본은 보존, 구조화 deep payload는 미완성 |
| V8 fallback | production deep | 전용 Batch와 겹치지 않는 27건만 보존 |

## 파일 선택 규칙

1. 아이디어 본문은 `analysis/ideas/YYYY/*.md`가 정본이다.
2. `analysis/batch_*_10.md`는 정본 파일을 불러오는 wrapper다.
3. `analysis/batch_*_v9_index.md`는 배치 감사·탐색용이다.
4. 앱에는 `data/curated/*_deep_v7.json`만 적용한다.
5. `data/staging/*_catalog_v9.json`은 키 구조가 완성되기 전까지 앱에 적용하지 않는다.

검증 명령:

```bash
python scripts/validate_batch_repository.py
```
