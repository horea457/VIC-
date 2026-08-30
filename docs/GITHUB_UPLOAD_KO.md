# GitHub 업로드 가이드

## 권장: 공개 저장소에는 경량 DB만

`data/processed/vic_dashboard.db`는 대시보드용 구조화 DB이며 원문 전체를 포함하지 않습니다. 기본 저장소에는 이 파일과 코드만 올리는 것을 권장합니다.

원문 전체가 들어간 `data/raw/vic_full_local.db`는 `.gitignore` 처리되어 있습니다. 연구용으로 로컬에 보관하세요.

## 원문 전체 DB를 GitHub에 꼭 보관해야 한다면

Git LFS를 사용하세요.

```bash
git lfs install
git lfs track "data/raw/*.db"
git lfs track "data/raw/*.gz"
git add .gitattributes
```

다만 원문 재배포 권리와 코드 라이선스는 별개의 문제이므로, 원문 전체가 들어간 저장소는 비공개로 두는 편을 권장합니다.
