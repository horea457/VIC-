# Batch 056 — Stamps.com / Weight Watchers — V9 Index

> Research as-of 2026-09-15. 10 idea = 10 canonical reports다. 현재 SQL에는 catalyst 10건, description 1건만 있고 performance COPY는 없다. raw 10건은 모두 Short지만 실제는 Long 6 / Short 4다.

## 0. 배치 결론

이 배치는 digital이 기존 산업을 없애는 방식이 서로 반대일 수 있음을 보여준다. Stamps.com은 우편물 감소 속에서도 e-commerce shipping workflow를 소프트웨어로 중개해 TAM을 넓혔다. Weight Watchers는 free apps와 wearables가 paid meetings/online을 우회하면서 중개가치를 잃었다. 단순히 'digital disruption'을 붙이지 말고 누가 workflow를 더 깊게 소유하는지 봐야 한다.

## 1. Idea Units

| # | 날짜 | Ticker | raw→연구 방향 | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2007-07-03 | STMP | Short→**Long** | 2009 stated horizon 실패·장기 unit economics 성공·exact return 미검증 | [marketing-as-growth-capex·NOL Long](ideas/2007/2007-07-03_STMP_long.md) |
| 2 | 2008-03-07 | STMP | Short→**Long** | 단기 정체 후 장기 회복·정확 수익률 미검증 | [expectation reset·10.5x FCF Long](ideas/2008/2008-03-07_STMP_long.md) |
| 3 | 2016-02-06 | STMP | Short→**Short** | e-commerce parcel TAM을 놓친 강한 실패 | [declining-mail TAM·M&A masking Short](ideas/2016/2016-02-06_STMP_short.md) |
| 4 | 2016-09-06 | STMP | Short→**Short** | mechanism은 2019 적중했지만 2016 trade timing은 실패 | [USPS reseller economics reset Short](ideas/2016/2016-09-06_STMP_short.md) |
| 5 | 2017-04-06 | STMP | Short→**Long** | platform 재정의와 Long은 강한 성공·$500 target 미달 | [shipping-software ecosystem·$25 EPS Long](ideas/2017/2017-04-06_STMP_long.md) |
| 6 | 2019-06-24 | STMP | Short→**Long** | multi-carrier 회복과 $330 takeout으로 매우 강한 성공 | [broken earnings=0·asset SOTP Long](ideas/2019/2019-06-24_STMP_long.md) |
| 7 | 2008-05-11 | WTW | Short→**Short** | recession·leverage의 전술적 성공, online offset로 secular collapse는 과대 | [attendance decline·debt-funded tender Short](ideas/2008/2008-05-11_WTW_short.md) |
| 8 | 2013-03-21 | WTW | Short→**Long** | free apps·category redefinition을 일시요인으로 본 강한 실패 | [temporary recruitment reset·11.2% FCF yield Long](ideas/2013/2013-03-21_WTW_long.md) |
| 9 | 2013-09-30 | WTW | Short→**Long** | category redefinition과 debt optionality를 오판한 강한 실패 | [43% share·online crown jewel Long](ideas/2013/2013-09-30_WTW_long.md) |
| 10 | 2014-02-22 | WTW | Short→**Short** | fundamentals 적중·50~60% borrow와 Oprah squeeze로 trade economics 위험 | [free-app substitution·$2.2bn leverage Short](ideas/2014/2014-02-22_WTW_short.md) |

## 2. SQL·Direction·Performance Audit

첨부 `VIC_IDEAS(4).sql`의 COPY table은 catalyst·companies·descriptions뿐이다. Batch 056 catalyst 10건을 모두 확인했고 2007 STMP description 17,911자만 존재한다. direction correction은 STMP 2007·2008·2017·2019, WTW 2013-03·2013-09의 6건이다. 성과 테이블이 없으므로 모든 exact return/IRR은 null이다. 기존 WTW 4건의 performance flag/value는 후대 Willis Towers Watson ticker series가 섞인 값이라 폐기했다.

## 3. Stamps.com — 좋은 분석과 나쁜 clock을 분리

2007 Long은 marketing LTV/CAC·NOL·cash를 잘 봤지만 2009의 세 target을 모두 놓쳤다. 2008 Long은 그 실패를 인정하고 EV/FCF 약 10.5x에서 expectation을 낮춰 새 투자로 만들었다. 2016-02 Short는 회사 TAM을 declining letter mail로 오정의해 실패했다. 2016-09 Short는 USPS 의존 메커니즘을 맞혔지만 사건이 2019에 와 trade timing은 실패했다.

2017 Long은 STMP를 Endicia·ShipStation·ShipWorks·ShippingEasy의 shipping-software ecosystem으로 재정의해 방향을 맞혔지만 $500 target은 과했다. 2019 Long은 깨진 USPS earnings를 회복시키지 않고 0으로 둔 뒤 customer assets와 MetaPack만 사서 가장 좋은 payoff를 만들었다. 2020 revenue $758.0m·paid customers 934k, 2021 $330 cash deal은 residual asset value를 검증한다.

## 4. Weight Watchers — leverage보다 먼저 category denominator

2008 Short는 attendance 감소와 $1.025bn tender 뒤 약 $1.8bn debt가 recession을 증폭한다는 전술적 논지로 성공했다. 다만 online revenue·subscriber 성장은 terminal collapse를 막았다. 2013의 두 Long은 historical share와 online을 moat로 보고 free apps·wearables를 temporary marketing noise로 오판했다. 2014 Short는 meetings 70%/online 30%, $2.2bn debt와 free substitution을 맞혔지만 50~60% borrow와 Oprah rescue가 좋은 fundamental call을 위험한 trade로 만들었다.

## 5. 투자논지 재사용 규칙

1. TAM은 제품 이름이 아니라 customer job과 대체경로로 정의한다.
2. marketing 자산화는 channel별 cohort LTV/CAC와 payback으로만 한다.
3. 같은 회사라도 expectation reset과 entry가 바뀌면 새 투자다.
4. structural mechanism에는 observable contract date와 position expiry를 붙인다.
5. broken earnings를 0으로 두고 남는 자산을 사는 SOTP가 정상화보다 안전할 수 있다.
6. market share는 shrinking category의 denominator를 확인한다.
7. 긴 만기·loose covenant는 enterprise loss를 없애지 않는다.
8. Short는 borrow-adjusted IRR과 squeeze catalyst를 valuation과 별도로 본다.
9. corporate event는 exact return이 아니다.
10. ticker가 재사용되면 issuer/date/security부터 resolve한다.

## 6. 산출물

- Payload: `data/curated/batch_056_stmp_wtw_deep_v7.json`
- Wrapper: `analysis/batch_056_stmp_wtw_10.md`
- Source packet: `data/curated/batch_056_source_packet.json`
- SQL inventory: `data/curated/batch_056_sql_inventory.json`
- Builder: `scripts/56_build_batch_056_v9.py`

## 7. 검증 기준

각 보고서는 0~12절, 6 weighted claims/100%, 5 metrics, 최소 6 timeline events와 원문 provenance+공식자료를 포함한다. Payload·문서·앱 popup의 idea_id, entity, direction, security와 verdict를 동일하게 유지한다.
