# Batch 039 — Nexstar·Sinclair Local Broadcasting 10건
평가기준일: 각 VIC 게시일 이후 실제 사업·자본배분 전개

분석일: 2026-09-05

대상: Nexstar 8건 · Sinclair 2건
## 결론부터

이번 배치는 local broadcasting을 단순한 쇠퇴 광고업으로 보면 놓치는 것과, 반대로 retransmission growth만 보고 과대평가하기 쉬운 것을 동시에 보여준다.

- **Nexstar:** 2005년 이후 핵심 성공요인은 local ad 성장 그 자체가 아니라 retransmission consent의 현금화, scale-accretive station M&A, 빠른 synergy capture, deleveraging, 그리고 M&A runway가 줄어든 뒤 buyback으로 이어진 자본배분이었다. 2011·2012·2017·2018·2020·2021 Long의 경제적 방향은 대부분 맞았다.
- **2016 NXST/MEG:** common equity 방향이 아니라 `Long MEG / Short 0.1249 NXST`로 CVR을 분리한 event trade다. 거래는 종결됐고 CVR은 양(+)의 payout을 냈지만, 실제 payout은 원문의 $2~3 base case보다 낮아 계약 waterfall 추정의 중요성을 보여준다.
- **Sinclair:** 2013 Long의 retrans + M&A core thesis는 강하게 작동했다. 그러나 2015 Long에서 management의 약 $2bn spectrum optionality를 거의 그대로 받아들인 부분은 실제 $313m gross auction proceeds와 크게 어긋났다. core FCF와 규제 option을 분리해야 한다.

> **데이터 경고:** 이번 10건의 원 SQL `is_short`는 전부 `true`다. 그러나 원 VIC 본문 기준으로 NXST 7건과 SBGI 2건은 명백한 Long이고, 2016 NXST 1건은 MEG Long/NXST hedge pair다. raw flag는 감사추적을 위해 JSON에 `raw_is_short=true`로 보존하고 research layer에서만 교정했다.
>
> **entity 경고:** 원 DB의 SBGI company_name이 `Diamond Sports`로 잘못 연결돼 있다. 2013·2015 아이디어의 실제 issuer는 **Sinclair Broadcast Group**이다. raw DB는 손대지 않고 curated layer에서 수정했다.

## 배치 공통 프레임

지역방송사의 현금흐름은 대략 `core advertising + political advertising + distribution/retransmission + digital - station opex - network affiliation fees - corporate cost - cash interest - capex - cash taxes`로 볼 수 있다. 분석에서 가장 흔한 오류는 gross retrans revenue를 moat 자체로 보는 것이다. MVPD/virtual MVPD로부터 받는 distribution fee가 늘어도 broadcast network에 지급하는 reverse compensation/affiliation fee가 더 빨리 오르면 **net retrans economics**는 악화될 수 있다. 두 번째 오류는 election-year political revenue를 정상화하지 않고 FCF multiple에 넣는 것이다. 세 번째는 station M&A의 headline EBITDA multiple만 보고, divestiture·synergy·financing·regulatory cap을 반영한 incremental equity return을 보지 않는 것이다.

---

## 보고서 파일 구성

대용량 전송 안정성을 위해 상세 분석은 10개 part로 분리 저장한다. 앱 loader는 아래 part를 순서대로 이어 붙여 하나의 보고서로 렌더링한다.

<!-- batch_parts: batch_039_nexstar_sinclair_part01.md|batch_039_nexstar_sinclair_part02.md|batch_039_nexstar_sinclair_part03.md|batch_039_nexstar_sinclair_part04.md|batch_039_nexstar_sinclair_part05.md|batch_039_nexstar_sinclair_part06.md|batch_039_nexstar_sinclair_part07.md|batch_039_nexstar_sinclair_part08.md|batch_039_nexstar_sinclair_part09.md|batch_039_nexstar_sinclair_part10.md -->
