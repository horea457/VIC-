# VIC Falsification DB — V11 Curated Only

외부자료로 검증한 VIC 심층 사후분석만 저장·표시하는 Streamlit 대시보드입니다.
자동 생성 분석, 짧은 초안, 미검증 후보는 production DB에 넣지 않습니다.

1. `Home.py` — 메인 현황/검색
2. `성공·실패 요인 분석` — 패턴 → 기업/아이디어 → 심층분석
3. `사후분석 DB` — 기업별 전체 심층 리포트

사후분석 DB는 상단의 아이디어 목록에서 행을 선택하면 같은 페이지 아래에
검토 완료된 `analysis/batch_*.md` 원문에서 기업 설명·돈 버는 구조·전체 판정표와
선택한 투자논지·실제 전개·핵심 수치·근거자료를 직접 추출해 표시합니다.
재무 수치의 `$` 기호는 Streamlit 수식 문법으로 오인되지 않도록 별도 처리합니다.

## 배포
압축을 풀고 **안의 파일/폴더 전체를 GitHub 저장소 루트에 업로드**합니다.
기존 `app/pages` 안의 예전 페이지 파일은 삭제하는 것을 권장합니다.

DB는 `data/processed/vic_dashboard.db.gz.part00`에 압축되어 있으며 앱 실행 시 자동
결합·압축해제합니다. 연구가 늘어 파일이 4MB를 넘으면 `part01`부터 자동으로 추가합니다.

## Curated-only 운영 원칙

- production DB의 `ideas_master`에는 심층분석 완료 아이디어만 남깁니다.
- `deep_analysis_*`와 `postmortems`가 분석의 유일한 source of truth입니다.
- 과거 자동 분석·자동 Claim·검증 대기열·자동 패턴 행은 모두 제거했습니다.
- 새 배치를 검증한 뒤 DB에 추가하고 GitHub `main`을 갱신하면 Streamlit도 재배포됩니다.
- 삭제 전 전체 데이터는 Git 이력의 V10 커밋에서 복구할 수 있습니다.

## V7 상세 사후분석 표준

상세 분석은 단순한 성공·실패 라벨이 아니라 다음 구조를 사용합니다.

1. 기업과 사업부별 비즈니스 모델·경제성
2. 원 VIC 논지와 당시 밸류에이션 산식
3. 핵심 주장의 가중치·숨은 가정·사전 반증조건
4. 실제 실적·주가·재무구조·촉매의 시계열
5. 주장별 적중 여부와 실제 결과의 인과 귀속
6. 최초 반대 신호, 회피 가능성, 재사용 가능한 학습 태그
7. 원문·SEC 공시·기업 발표 등 근거자료와 판단 연결

현재 production DB에는 외부자료로 검증한 심층 사후분석 149건만 있습니다.
Batch 001에서는 Farfetch의 2019년 숏과 2021년 롱 2건을 추가했습니다. 원 SQL에서
2021년 아이디어가 숏으로 잘못 저장된 문제는 원본값을 보존하고 분석 레이어에서
실제 방향을 롱으로 교정합니다.

Batch 002에서는 Hawaiian Electric Industries의 2008년·2010년 숏과 2020년 롱
3건을 같은 기업의 장기 사례로 분석했습니다. 가격결과와 논지·촉매·인과결과를 분리하고,
규제변화·신용사이클·배당지속성과 2023년 Maui 산불의 책임 꼬리위험을 비교했습니다.
2020년 아이디어 역시 원 SQL의 숏 표시를 본문에 맞춰 롱으로 교정했습니다.

Batch 003에서는 American Express의 금융위기 전후 롱 3건(2007년 4월, 2008년
6월, 2008년 12월)을 하나의 시계열 사례로 분석했습니다. 세 글 모두 SQL에는
숏으로 저장돼 있지만 본문상 실제 방향은 롱입니다. 2007년과 2008년 6월 글은
closed-loop 경쟁우위를 맞게 봤어도 신용·조달 충격의 결합과 경로를 과소평가했고,
2008년 12월 글은 TARP·은행지주회사 전환·비용절감이 만든 생존 다리를 포착했습니다.

Batch 004에서는 American Express의 2015년·2016년 Costco 이탈 롱과 2018년
anti-steering 대법원 판결 숏을 분석했습니다. 같은 franchise 롱도 사건 전 14x와
사건 후 10.6x의 결과가 크게 달랐고, 2018년 숏은 패소확률 90%의 이진 촉매가 실제
5대4 AXP 승소로 뒤집히면서 치명적으로 실패했습니다. 2015년·2016년 글의 SQL 숏
표시는 본문상 실제 롱으로 교정했습니다.

Batch 005에서는 American Express의 2020년 2월·10월 팬데믹 전후 롱과 2022년
rewards 경쟁 숏을 분석했습니다. 같은 quality 논지도 평시 15x 매수와 위기 후
stress-tested 매수의 가격경로가 크게 달랐습니다. 2022년 숏은 첫 6개월 가격은
맞았지만 rewards를 고객가치와 분리한 fee economics, 목표미달 촉매와 중기 결론은
실패했습니다. 이 배치로 SQL에 포함된 AXP 9건의 심층분석을 완료했습니다.

Batch 006에서는 Western Union의 2007~2017년 롱 5건과 숏 4건을 하나의 장기
사례로 분석했습니다. 거래량은 늘어도 건당 수익과 C2C margin이 하락한 실제
legacy economics, 디지털 전환, agent·규제 network, 자사주와 시작 valuation을
분리했습니다. 사업 악화를 맞힌 2012~13년 숏들이 낮은 기대·현금환원 때문에
큰 손실을 낸 반면, 일부 롱은 생존을 맞히고도 장기 복리 목표에는 미달했습니다.
SQL의 9건 전부 숏 표시는 본문에 맞춰 실제 롱 5건·숏 4건으로 교정했습니다.

Batch 007에서는 Chesapeake Energy의 2001~2021년 보통주 롱 6건, 보통주 숏
1건, 회사채 롱 2건을 자본구조 전체의 시계열로 분석했습니다. 좋은 셰일 자산의
gross NAV와 기존 주주의 잔여가치, 단기 유동성과 장기 지급능력을 분리했습니다.
2015년 2017채는 파산 전에 par로 상환돼 성공한 반면 2016년 2020채는 만기 직전
Chapter 11로 실패했고, 2021년 롱은 구 부채와 기존 equity가 제거된 재편회사를
매수해 1년 +62.0%, 2년 +115.5%를 기록했습니다. SQL 방향은 본문상 실제
보통주 롱 6건·회사채 롱 2건·보통주 숏 1건으로 교정했습니다.

Batch 008에서는 한 번에 30건을 분석했습니다. EZCORP 9건은 core pawn의
점포경제성과 payday·Finmart·online 확장의 자본배분을 분리했고, Spark Networks
9건은 JDate의 niche network와 반복 CAC·Zoosk 인수부채·2023년 구조조정을
연결했습니다. Nicholas Financial 9건은 지점 underwriting, book value, 신용손실,
funding runway와 2013년 주당 $16 매각계약의 발표·종료를 구분했습니다. Costco
3건은 같은 강한 membership flywheel에서도 2006·2015·2021년 시작 valuation에
따라 기대수익과 경로위험이 달라짐을 분석했습니다. 30건 모두 본문상 실제 방향은
보통주 Long이며, 원 SQL에서 Short로 저장된 12건은 분석 레이어에서 교정했습니다.

Batch 009에서는 Netflix 8건, ADT 8건, Activision Blizzard 8건, Alibaba 6건을
분석했습니다. Netflix는 DVD에서 글로벌 streaming으로 바뀌는 terminal economics와
콘텐츠 cash spend의 시간차를, ADT는 RMR에서 유지 SAC·부채를 차감한 equity FCF를
검증했습니다. Activision Blizzard는 portfolio IP·문화/지배구조와 Microsoft $95
인수의 standalone/merger-arb 성격을 분리했고, Alibaba는 commerce·Cloud·Ant SOTP와
VIE 청구권·정책·holding discount를 대조했습니다. 원 SQL의 30건 short 표시는 실제
Long 19건·Short 10건·혼합 이벤트 1건으로 분석 레이어에서 교정했습니다.

Batch 010에서는 Groupe Aeroplan/Aimia·AerCap 8건, Hertz 8건, Spirit Airlines
7건, General Motors 7건을 분석했습니다. 항공기·차량의 담보 및 book value와
stress value, cycle 정상화 이익과 현금유동성, 보통주·EETC 채권·워런트·콜옵션·
합병차익거래의 청구권을 분리했습니다. 특히 SQL의 2011년 AER 아이디어가 AerCap이
아닌 캐나다 Groupe Aeroplan인데도 미국 AER 가격과 결합된 entity 오류를 찾아
성과값을 무효 처리했습니다. 구 GM과 New GM, 파산 전후 Hertz도 별도 증권으로
판정했습니다.

## 연구 배치 적용

검토 가능한 상세 리서치는 `data/curated/*_deep_v7.json`에 저장합니다. 앱은 소형
curated DB를 푼 뒤 이 JSON 배치를 idempotent overlay로 적용합니다. 로컬 DB에 영구
반영하려면 다음 명령을 사용합니다.

```bash
python scripts/08_load_detailed_research.py
```

전체 장문 분석은 다음 파일에서 확인할 수 있습니다.

- `analysis/batch_001_farfetch.md`
- `analysis/batch_002_hawaiian_electric.md`
- `analysis/batch_003_american_express_gfc.md`
- `analysis/batch_004_american_express_costco_antitrust.md`
- `analysis/batch_005_american_express_pandemic_rewards.md`
- `analysis/batch_006_western_union_full_history.md`
- `analysis/batch_007_chesapeake_full_history.md`
- `analysis/batch_008_ezpw_lov_nick_cost_30.md`
- `analysis/batch_009_nflx_adt_atvi_baba_30.md`
- `analysis/batch_010_transport_capital_structure_30.md`
