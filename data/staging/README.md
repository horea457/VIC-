# Staging batch catalogs

이 디렉터리는 아이디어 목록과 메타는 있으나 production deep schema의
`postmortems`, `sections`, `claims`, `metrics`, `timeline`, `sources`가 아직 완성되지
않은 배치를 보존한다.

파일명은 `*_catalog_v9.json`을 사용한다. 필수 배열과 가중치 검증을 통과한 뒤에만
`data/curated/*_deep_v7.json`으로 승격한다.

현재 staging 범위는 Batch 058–062와 068–076이다. Batch 064–067은 장문 보고서와
production deep schema 검증을 완료해 `data/curated/`로 승격했다. Batch 074–076은
아이디어 catalog만 있고 필수 production 배열이 없어 staging에 둔다.
