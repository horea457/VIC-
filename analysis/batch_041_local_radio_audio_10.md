# Batch 041 — Local Radio / Audio: Townsquare, Entercom-Audacy, Emmis (10 ideas)

분석일: 2026-09-05  
대상: **TSQ 2022 1건 + ETM 4건 + EMMS 5건**  
검증 구조: **10 ideas / 100 sections / 60 weighted claims / 40 metrics / 60 timeline / 60 sources**

<!-- batch_parts: batch_041_local_radio_audio_idea01.md|batch_041_local_radio_audio_idea02.md|batch_041_local_radio_audio_idea03.md|batch_041_local_radio_audio_idea04.md|batch_041_local_radio_audio_idea05.md|batch_041_local_radio_audio_idea06.md|batch_041_local_radio_audio_idea07.md|batch_041_local_radio_audio_idea08.md|batch_041_local_radio_audio_idea09.md|batch_041_local_radio_audio_idea10.md -->

## 배치 결론

이번 배치는 같은 radio/local-media 자산을 두고 **낮은 FCF multiple, scale M&A, asset NAV, legal/event catalyst, digital transformation**이 언제 주주가치로 연결되고 언제 leverage에 흡수되는지를 비교한다.

가장 선명한 대비는 세 가지다.

1. **TSQ 2022 Long** — digital-first 전환 자체는 맞았다. 2022 digital이 매출·profit의 50%가 됐고 2025~2026에는 과반이 더 굳어졌다. 그러나 2024 digital $275m와 2.9x/46% IRR 같은 속도 가정은 과했다.
2. **ETM/Audacy** — 2017 scale-merger Long과 2020 COVID survival Long보다 2018 leverage Short가 장기 구조를 더 정확히 봤다. CBS Radio 규모를 얻었지만 2024 Chapter 11에서 약 $1.9bn debt를 $350m로 줄여야 했다.
3. **EMMS** — TV/station 매각, preferred vote, litigation 같은 event는 여러 번 실제로 맞았다. 그러나 asset NAV가 존재하는 것과 minority common이 장기간 compounding 하는 것은 달랐다. 2020 voluntary delisting은 governance/liquidity discount의 실체를 보여준다.

## 방향 오류 audit

이 10건은 raw SQL에서 모두 `Short`로 저장돼 있다. 원문 description을 security-level로 다시 확인한 결과 실제 방향은:

- **Long 8건:** TSQ 2022, ETM 2005/2017/2020, EMMS 2005/2012/2013/2014
- **Short 2건:** ETM 2018, EMMS 2010

원 raw flag는 수정하지 않았다. ETM 2020은 unsecured bond short를 optional hedge로 언급하지만 본문은 명시적으로 **ETM common stock 매수 추천**이다.

## 공통 교훈

**radio의 높은 FCF yield는 moat의 증거가 아니라 duration risk의 가격일 수 있다.** 반대로 digital mix shift나 asset monetization이 실제로 일어나도 leverage·governance·realization timing을 통과해야 common equity 수익이 된다. 따라서 향후 media 아이디어는 `organic revenue trend → normalized EBITDA → debt waterfall → asset realization probability → per-share capital allocation` 순서로 분석하는 것이 더 재사용 가능하다.
