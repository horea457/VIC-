# Batch 041 — Local Radio / Digital Audio V9 Index

> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-09. 원문 방향·기간·증권을 복원하고 SEC/회사 1차자료와 사후 사건을 교차검증했다.

## Canonical idea files

| 순서 | VIC 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2022-03-14 | TSQ | Short | Long | [2022-03-14 TSQ](ideas/2022/2022-03-14_TSQ_long.md) | 사업구조 성공·수익경로 실패/미검증 |
| 2 | 2005-11-28 | ETM | Short | Long | [2005-11-28 ETM](ideas/2005/2005-11-28_ETM_long.md) | 목표기간 가격 미검증·장기 사업논지 실패 |
| 3 | 2017-08-08 | ETM | Short | Long | [2017-08-08 ETM](ideas/2017/2017-08-08_ETM_long.md) | 명시기간 실패·장기 common 실패 |
| 4 | 2018-07-23 | ETM | Short | Short | [2018-07-23 ETM](ideas/2018/2018-07-23_ETM_short.md) | 구조적으로 강한 성공·정확한 실행 IRR 미검증 |
| 5 | 2020-03-15 | ETM | Short | Long | [2020-03-15 ETM](ideas/2020/2020-03-15_ETM_long.md) | 즉시 생존 성공·5년 common thesis 실패 |
| 6 | 2005-12-30 | EMMS | Short | Long | [2005-12-30 EMMS](ideas/2005/2005-12-30_EMMS_long.md) | asset-sale 이벤트 성공·residual compounding 실패 |
| 7 | 2010-07-19 | EMMS | Short | Short | [2010-07-19 EMMS](ideas/2010/2010-07-19_EMMS_short.md) | 강한 이벤트 성공·exact trade return 미검증 |
| 8 | 2012-10-08 | EMMS | Short | Long | [2012-10-08 EMMS](ideas/2012/2012-10-08_EMMS_long.md) | 이벤트 부분 성공·common payoff 미검증/혼합 |
| 9 | 2013-07-18 | EMMS | Short | Long | [2013-07-18 EMMS](ideas/2013/2013-07-18_EMMS_long.md) | 자산가치 부분 성공·common realization 지연/미흡 |
| 10 | 2014-10-30 | EMMS | Short | Long | [2014-10-30 EMMS](ideas/2014/2014-10-30_EMMS_long.md) | asset/legal claim 성공·3~4개월 equity payoff 실패/미검증 |

## Direction / horizon audit

10건 모두 raw SQL `is_short=true`다. 실제 원문은 Long 8건, Short 2건이다. ETM 2020은 common Long이 primary recommendation이고 unsecured-bond Short는 optional hedge다. Raw 값은 삭제하지 않고 V9 research layer에서만 방향과 security leg를 교정했다.

EMMS 2010의 raw 3년은 9월 drop-dead event와 모순되고, EMMS 2013의 raw 11년은 98.7FM lease-return 기간을 horizon으로 잘못 읽었을 가능성이 높다. 이 두 값은 판정에서 제외하고 계약상 event date 또는 ‘명시 없음’을 사용했다.

## 핵심 판정 교정

1. **TSQ 2022:** digital mix는 성공했지만 2024 Digital revenue는 $233.958m으로 $275m target 대비 14.9% 미달했고 Digital segment profit은 10.2% 감소했다.
2. **ETM 2005:** 12~18개월 가격성과는 미검증이다. 2024 Chapter 11은 짧은 horizon 수익률 대체값이 아니라 장기 FCF-duration thesis의 실패근거로만 썼다.
3. **ETM 2017:** $16.66·1년 target과 달리 2018-07 후속 Short의 $8.15가 기간 내 반증이었다.
4. **ETM 2018:** 구조적 Short는 적중했지만 Chapter 11까지 약 5.5년이므로 borrow-adjusted IRR은 별도 미검증이다.
5. **ETM 2020:** 단기 liquidity survival은 성공했어도 5년 common survival은 게시 후 약 46개월의 Chapter 11로 실패했다.
6. **EMMS 2005:** $394.9m tender는 $100m revolver+$300m notes로 조달한 levered recap이었다. 단순 share-count accretion으로 보지 않았다.
7. **EMMS 2010:** 2/3 preferred consent와 drop-dead date를 이용한 merger-break Short는 event 기준 강한 성공이다.
8. **EMMS 2012~2014:** 자산·법률가치는 존재했지만 $131m WBLS/WLIB acquisition과 $191.6m Credit Agreement, controller/time discount가 common payoff를 약화했다.

## Batch 041의 공통 분석식

`organic ad/digital contribution - fixed operating cost - corporate overhead - cash interest - maintenance capex - tax = common equity FCF`

Asset play는 여기에 `sale probability × after-tax proceeds × time discount - debt - preferred - control discount`를 적용한다. M&A는 headline revenue와 EBITDA multiple 대신 acquired/legacy organic trend, post-synergy after-interest FCF, debt paydown years를 본다.

## 상위 교훈

1. Digital mix 상승은 absolute revenue·segment profit 성장과 다르다.
2. Radio license scarcity는 advertiser attention의 moat가 아니다.
3. 높은 FCF yield는 declining annuity의 짧은 duration을 반영할 수 있다.
4. 위기 Long은 liquidity runway와 solvency runway를 분리한다.
5. Levered recap의 buyback accretion은 pro forma interest 뒤 FCF/share로 검증한다.
6. SOTP에는 corporate overhead·tax·realization probability·time·controller discount를 넣는다.
7. Merger-break Short는 closing threshold와 blocker의 경제적 유인을 수학으로 본다.

## 앱/DB 반영

- `analysis/batch_041_local_radio_audio_10.md`는 위 10개 canonical 파일을 불러오는 wrapper다.
- `data/curated/batch_041_local_radio_audio_deep_v7.json`은 V9 상세 overlay schema로 재작성했다.
- 기존 idea01~idea10 Markdown은 감사추적용 legacy 파일로 보존했다.
