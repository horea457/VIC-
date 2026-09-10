# Batch 050 — McDermott / Mohawk Industries — V9 Index

> **Research as-of:** 2026-09-10. 첨부 `VIC_IDEAS(4).sql`의 원문 action/payoff와 repository 성과를 감사했다. **10 idea = 10 canonical reports**다.

## 0. 배치 결론

MDR은 동일한 오류가 security를 바꾸며 깊어졌다. 2013 common은 문제계약을 finite inventory로 오판했고, 2018 merger common은 그 turnaround 역량을 CB&I의 더 큰 계약부채에 외삽했다. 2018 notes는 security seniority를 높였지만 전사 liquidity와 recovery waterfall 대신 Chiyoda 단일 tail·common SOTP에 기대어 실패했다. MHK는 durable franchise가 맞아도 cycle entry·horizon·normalized margin이 틀리면 50%+ drawdown이 난다는 연속 실험이다.

## 1. Idea Units

| # | 날짜 | Ticker | raw→실제 방향 / Security | 사후 판정 | Canonical report |
|---:|---|---|---|---|---|
| 1 | 2013-10-14 | MDR | Long→**Long / Common equity** | 실패 — 반복 EAC 손실과 offshore downturn이 asset floor·정상화 clock을 깨뜨림 | [문제계약 burn-off·asset floor·$600m EBITDA 정상화 Long](ideas/2013/2013-10-14_MDR_long.md) |
| 2 | 2018-01-04 | MDR | Long→**Long / Common equity** | 강한 실패 — acquired project liabilities와 leverage가 synergy를 압도, 20개월 뒤 Chapter 11 | [CB&I scrubbed liabilities·$250m+ synergy·turnaround playbook Long](ideas/2018/2018-01-04_MDR_CBI_merger_long.md) |
| 3 | 2018-11-11 | MDR | Long→**Long / 10.625% senior unsecured notes due 2024** | 강한 실패 — liquidity·priority spiral로 par maturity 경로 소멸 | [87 가격·14% YTM의 2024 무담보채 money-good Long](ideas/2018/2018-11-11_MDR_2024_notes_long.md) |
| 4 | 2007-12-10 | MHK | Short→**Long / Common equity** | 실패 — quality는 맞았지만 cycle floor를 너무 일찍 선언; 1Y -54.5%, 5Y +3.8% | [duopoly·distribution·hard-surface mix와 10~11x FCF Long](ideas/2007/2007-12-10_MHK_long.md) |
| 5 | 2009-02-18 | MHK | Short→**Short / Common short + long CDS protection** | 기간 실패 — 1M short +19.5% 뒤 3M부터 급반전; CDS 성과 null | [earnings miss·junk downgrade·trade-down의 equity Short + CDS Long](ideas/2009/2009-02-18_MHK_short.md) |
| 6 | 2013-02-08 | MHK | Short→**Short / Common equity** | 강한 실패 — housing·hard-surface·M&A leverage를 과소평가; 5Y stock +155.3% | [low ROIC·peak tile margin·Marazzi overpayment의 MHK Short](ideas/2013/2013-02-08_MHK_short.md) |
| 7 | 2013-12-09 | MHK | Short→**Long / Common equity** | 부분 성공 — 1Y +11.8%로 +28% target 미달, 2~3Y 지연 달성 | [flooring lag·Marazzi synergy·hard-surface mix의 12M Long](ideas/2013/2013-12-09_MHK_long.md) |
| 8 | 2018-08-03 | MHK | Short→**Long / Common equity** | 실패 — transitory miss가 multi-year margin reset으로 이어져 2Y -57.5% | [2Q miss 과잉반응·capex roll-off·LVT ramp의 expectation-reset Long](ideas/2018/2018-08-03_MHK_long.md) |
| 9 | 2020-10-14 | MHK | Short→**Long / Common equity** | 강한 tactical 성공 — 6M +98.2%, 1Y +80.4%; 2Y에는 상승분 반납 | [housing catch-up·LVT share recapture·FX·legal discount의 tactical Long](ideas/2020/2020-10-14_MHK_long.md) |
| 10 | 2021-12-23 | MHK | Short→**Long / Common equity** | 강한 실패 — peak margin을 정상으로 보고 rate·housing regime 전환을 누락 | [15% EBIT margin·$26 EPS·LVT share의 $390 Long](ideas/2021/2021-12-23_MHK_long.md) |

## 2. Direction / Security Audit

- MDR 3건의 raw Long은 맞다. 단, 2018-11-11은 common이 아니라 **10.625% senior unsecured notes due 2024**다.
- MHK raw Short 7건 중 실제 Long은 2007-12, 2013-12, 2018-08, 2020-10, 2021-12의 5건이다.
- 실제 Short는 2009-02의 common Short + CDS Long과 2013-02 common Short 두 건뿐이다.

## 3. 투자논지의 누적 교정

### McDermott — backlog에서 recovery waterfall까지

1. Backlog 금액을 가치로 보지 말고 계약별 expected margin과 remaining cash-to-complete로 바꾼다.
2. 반복 charge는 개별 project가 아니라 bidding·EAC·execution process 문제일 수 있다.
3. 인수기업의 EBITDA보다 inherited fixed-price liability·negative working capital·LC를 먼저 산다.
4. Distress bond는 common 시가총액이 아니라 DIP→secured→priority→unsecured waterfall로 평가한다.

### Mohawk — franchise와 cycle을 분리

2007 Long은 moat는 맞고 cycle floor가 틀렸다. 2009 Short는 recession은 맞고 시장저점 timing이 틀렸다. 2013 Short는 hard-surface·M&A·operating leverage를 과소평가했고, 같은 해 Long은 방향은 맞지만 12개월 clock이 짧았다. 2018 Long은 capex roll-off를 ROIC inflection으로 오인했고, 2020 Long은 낮은 기대와 housing lag를 정확히 잡았다. 2021 Long은 peak margin을 정상 margin으로 썼다.

## 4. 배치 공통 교훈

1. **Backlog는 margin exposure다.** 계약가격에서 remaining cost·cash need를 뺀다.
2. **Management quality는 liability underwriting의 대체물이 아니다.**
3. **Good cyclical과 good entry는 다르다.** moat는 drawdown을 막지 않을 수 있다.
4. **Crisis short는 second derivative가 핵심이다.** bad news가 계속돼도 덜 나빠지면 먼저 오른다.
5. **Capex roll-off와 FCF inflection은 다르다.** utilization·yield·ROIC를 확인한다.
6. **Peak margin을 mean으로 쓰지 않는다.** rate·turnover·utilization의 regime-break state를 둔다.
7. **Target 조기 달성은 재-underwrite event다.** 2020 Long의 6M +98.2%와 2Y -6.6%가 이를 보여준다.
8. **성과는 security별이다.** CDS·bond recovery가 없으면 common price로 대체하지 않는다.

## 5. 데이터·앱 산출물

- DB payload: `data/curated/batch_050_mdr_mhk_deep_v7.json`
- Streamlit wrapper: `analysis/batch_050_mdr_mhk_10.md`
- SQL source packet: `data/curated/batch_050_source_packet.json`
- Builder: `scripts/50_build_batch_050_v9.py`

## 6. 검증 기준

10개 보고서 모두 0~12절, 6개 claim/100% weight, 5개 metric, 최소 6개 event와 원문+공식자료 source를 포함한다. Payload·문서·앱 popup의 entity, direction, security, verdict를 동일하게 유지한다.
