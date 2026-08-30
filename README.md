# VIC 허구 반증 연구소 — V4.2

VIC의 과거 투자 아이디어를 **패턴 → 기업/아이디어 → 당시 Claim → 실제 사후전개 → 성공·실패 해부** 순서로 탐색하는 Streamlit 연구 대시보드입니다.

## V4.2의 가장 큰 변화

V3까지의 13,656건 자동 구조화 레이어 위에 **실제 사후분석 완료 레이어**를 추가했습니다.

- VIC 아이디어 전체: **13,656건**
- 자동 프로필: **13,656건**
- 자동 Claim: **32,571개**
- **실제 사후분석 완료: 18건**
- **사후검증 Claim: 56개**
- **후속 공시·SEC·IR 근거자료: 30개**
- 검증 완료 성공/실패/혼합 패턴: **18개**

사후분석 완료 사례는 주가만 보고 판정하지 않습니다. V4.2에서는 사용자가 기업 하나를 눌렀을 때 단순 요약이 아니라 **기업의 경제성 → 당시 밸류에이션 → Claim별 성립조건 → 실제 숫자 비교 → 시간축 → 잘 본 부분/틀린 부분 → 재사용할 투자 교훈**까지 읽을 수 있도록 심층화했습니다.

- 사후 정량 스냅샷: **71개**
- 사후 사건 타임라인: **70개**
- 심층 long-form 분석: **18건 전부**

`VIC 원문` → `실제 논지 방향 교정` → `핵심 Claim` → `당시 가정` → `후속 사업·재무·이벤트 데이터` → `Claim별 성공/실패` → `왜` → `최초 반증 신호` → `재사용할 질문`

## 중요: Long/Short 메타데이터 교정

원 SQL dump의 `is_short` 값이 일부 아이디어에서 실제 본문과 반대로 저장돼 있는 것을 발견했습니다. 예를 들어 WCC, TMO, BX, LINC, RCL, ALB, PTON, UBER 등은 원 메타데이터와 본문 방향이 불일치합니다.

V4의 **사후분석 완료 사례는 VIC 본문을 직접 읽어 `research_direction_ko`를 별도로 저장**하고, 성과도 이 교정 방향으로 계산합니다. 원본 필드는 보존합니다.

## 현재 사후분석 완료 예시

- WESCO — Anixter 통합·시너지·디레버리징
- BlueLinx — 셀프헬프 마진 개선·디레버리징
- Worthington — Nikola 숨은 자산·이벤트 가치 현실화
- KKR / Blackstone — 장기 잠금 자본과 AUM 복리
- Thermo Fisher — 고품질 기업의 일시적 멀티플 압축
- Domino's — 반복 로열티와 네트워크 확장
- Royal Caribbean — 이벤트 충격과 구조 훼손 구분
- ResMed — 시장 포화 숏 논지 실패
- Carvana — 위험은 맞췄지만 파산·시간축 단정 실패
- Lincoln Educational — 카운터사이클 + 영업레버리지
- Pinterest — 장기 monetization 성공, 단기 경로 혼합
- Amarin — TAM·상업화 실행 과대추정
- Peloton — 팬데믹 수요를 구조 성장으로 외삽
- Uber — 멀티프로덕트 플랫폼 + FCF 레버리지
- Beyond Meat — 구조적 수요 약화·단위경제 숏
- Albemarle — 구조 수요 성장과 가격사이클의 분리
- **Amphenol — 전자화 content growth + 분권형 운영 + 볼트온 M&A 복리**

## 주요 화면

1. **홈** — 검증 완료 패턴과 전체 corpus 탐색
2. **아이디어 탐색** — 회사/티커/작성자/연도별 검색
3. **기업·아이디어 분석** — 사후분석 완료 건은 검증 리포트를 우선 표시
4. **성공·실패 패턴** — `사후검증 완료 패턴`과 `자동 스크리닝 후보`를 별도 탭으로 분리
5. **투자논지 라이브러리** — 반복되는 VIC 서사 탐색
6. **반증 신호** — 무엇을 먼저 모니터링해야 하는가
7. **데이터 품질** — 자동분석과 정밀검증의 경계
8. **검증 우선순위** — 다음 사후분석 후보 큐
9. **사후분석 완료 사례** — 검증된 기업만 한 번에 탐색

테이블 행을 클릭하면 팝업으로 바로:

`무슨 기업인가 → 당시 VIC 논지 → 실제 전개 → 평가축별 판정 → Claim별 사후검증 → 패턴 → 반증 질문 → 근거자료`

을 확인할 수 있습니다.

## 데이터 구조

### 자동 탐색 레이어

- `ideas_master`
- `analysis`
- `claims`
- `pattern_catalog`
- `idea_pattern_map`

### V4.2 사후검증 레이어

- `postmortems` — 아이디어 단위 정밀 사후분석
- `postmortem_claims` — Claim별 실제 결과와 판정
- `postmortem_sources` — 후속 공시·SEC·IR 근거
- `postmortem_longform` — 사업 경제성·밸류에이션·잘 본 부분·틀린 부분·교훈
- `postmortem_metrics` — 당시 숫자와 사후 숫자의 정량 비교
- `postmortem_timeline` — 투자 아이디어 이후 주요 사건의 시간축
- `verified_pattern_catalog` — 검증 사례에서 확인한 성공/실패/혼합 패턴
- `verified_pattern_map` — 패턴 ↔ 검증 아이디어 연결

재현 가능한 curated 데이터는 `data/curated/`에 JSON으로도 저장합니다.

## 실행

```bash
pip install -r requirements.txt
streamlit run app/Home.py
```

Streamlit Community Cloud의 Main file path는 `app/Home.py`입니다.

## 배포 DB

`data/processed/vic_dashboard.db.gz`만 GitHub에 올리면 됩니다. 앱이 실행될 때 `/tmp`에 자동 해제합니다. 이전 버전의 `vic_dashboard.db`가 repo에 남아 있더라도 gzip V4 DB를 우선 사용합니다.

## 사후분석 레이어 재적재

로컬 DB를 새로 빌드한 경우:

```bash
python scripts/07_load_verified_postmortems.py --db data/processed/vic_dashboard.db
```

후 `vic_dashboard.db.gz`를 다시 만들면 됩니다.

## 해석 원칙

> **주가 성공 ≠ 투자논지 성공**

예를 들어 Carvana 숏은 자본집약성과 유동성 위험을 정확히 지적했지만, '수개월 내 파산'이라는 최종 결론과 시간축은 틀렸습니다. Peloton은 2026년 흑자로 돌아섰지만 2021년의 고성장·대규모 TAM 논지가 맞았다는 의미는 아닙니다.

V4.2는 이런 차이를 DB에 남기고, **왜** 그런 결과가 나왔는지를 숫자와 인과관계로 설명하는 것을 목표로 합니다.
