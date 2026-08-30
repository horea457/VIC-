# 데이터 사전

## `ideas_master`
VIC 아이디어 1건당 1행인 탐색용 마스터입니다.

- `idea_id`: 원 아이디어 고유 ID
- `date`, `year`: 게시 시점
- `ticker`, `company_name`, `author`: 기업/작성자 메타데이터
- `direction_ko`: 롱/숏
- `contest_winner`: Contest Winner 여부
- `narrative_tags_ko`: 원문 키워드 기반 1차 자동 태그(JSON)
- `idea_type_ko`: Catalyst 중심 이벤트 유형 1차 분류
- `horizon_raw`, `horizon_months`: 본문에서 탐지된 기간 표현
- `perf_*`: 원 데이터셋에 포함된 주가 배수
- `idea_return_*`: 롱/숏 방향을 반영한 단순 수익률. **최종 성과판정용이 아님**

## `analysis`
정밀 한국어 분석 결과 1건당 1행입니다. 핵심은 결과를 하나로 합치지 않는 것입니다.

- 기업 설명 / 사업모델 / 산업구조
- 당시 투자논지 / 핵심 가정 / 반증조건
- 실제 전개 / Catalyst 결과
- 투자논지 / 사업 / 밸류에이션 / 주가 / 현재 결과
- 실패 영역 / 실패 메커니즘 / 근본 분석 오류 / 전달 경로
- 최초 반증 신호 / 당시 인지 가능성 / 회피 가능성
- 가장 중요한 반증 질문

## `claims`
한 아이디어를 여러 개의 검증 가능한 명제로 분해합니다. `claim_type_ko`, `claim_ko`, `evidence_at_t0_ko`, `falsifier_ko`, `leading_indicator_ko`, `outcome_ko`가 핵심입니다.

## `failure_patterns`
실패를 `영역 → 구체적 메커니즘`으로 분류합니다. 단순히 “성장 둔화”가 아니라 무엇이 성장 둔화를 만들었는지를 저장합니다.

## `analytical_errors`
왜 투자자가 잘못 판단했는지에 대한 사고 오류입니다. 예: 선형 외삽, 공급반응 무시, 고객 인센티브 무시, 정적 산업 분석.

## `signal_taxonomy`
시장점유율, retention, 가격/물량, unit economics, 산업 CAPEX, 경쟁자 행동 등 **재무결과보다 앞서 나타날 수 있는 반증 신호**를 정의합니다.
