# Batch 043 — Level 3 / Nexstar V9 Index

> Batch 002 V9 규칙을 적용했다. **VIC 아이디어 1건 = canonical Markdown 1개**다.
> Research as-of 2026-09-09. raw 방향, 실제 증권, 회사 생존, 해당 security payoff를 분리했다.

## Canonical idea files

| 순서 | 게시일 | Ticker | 원 SQL | 실제 방향 | 파일 | 핵심 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2000-08-29 | LVLT | Short | Long | [2000-08-29 LVLT](ideas/2000/2000-08-29_LVLT_long.md) | 강한 실패 — 6개월 약 -70%, 자산가치가 equity를 보호하지 못함 |
| 2 | 2001-03-01 | LVLT | Short | Long | [2001-03-01 LVLT](ideas/2001/2001-03-01_LVLT_long.md) | 실패 — 싼 PP&E보다 cash burn·부채·공급과잉이 우선 |
| 3 | 2002-04-19 | LVLT | Short | Long | [2002-04-19 LVLT](ideas/2002/2002-04-19_LVLT_bonds_long.md) | 성공 — bankruptcy 회피·여러 2008/2010 채무 상환, exact issue IRR은 미검증 |
| 4 | 2003-03-17 | LVLT | Short | Long | [2003-03-17 LVLT](ideas/2003/2003-03-17_LVLT_bank_debt_long.md) | 강한 성공 — 2003년 facility 전액상환 |
| 5 | 2004-12-30 | LVLT | Short | Pair Long | [2004-12-30 LVLT](ideas/2004/2004-12-30_LVLT_convert_pair.md) | 성공 가능성 높음 — principal survival·dilution은 적중, exact pair IRR은 미검증 |
| 6 | 2007-11-11 | LVLT | Short | Long | [2007-11-11 LVLT](ideas/2007/2007-11-11_LVLT_long.md) | 실패 — integration 경고 현실화·2011 EBITDA forecast 대폭 미달 |
| 7 | 2011-10-11 | LVLT | Short | Long | [2011-10-11 LVLT](ideas/2011/2011-10-11_LVLT_long.md) | 혼합 — 2013 forecast 실패, 2014~17 delayed capital appreciation 성공 |
| 8 | 2017-07-29 | LVLT | Short | Long | [2017-07-29 LVLT](ideas/2017/2017-07-29_LVLT_merger_long.md) | 혼합 — 거래종결 성공, post-close $75~90·dividend thesis 실패 |
| 9 | 2005-12-20 | NXST | Short | Long | [2005-12-20 NXST](ideas/2005/2005-12-20_NXST_long.md) | 사업논지 성공·가격성과 미검증 |
| 10 | 2011-12-14 | NXST | Short | Long | [2011-12-14 NXST](ideas/2011/2011-12-14_NXST_long.md) | 강한 성공·촉매 경로 변경 |

## Direction / security audit

10건 모두 raw SQL은 Short지만 원문은 모두 매수 논지다. LVLT 2000·2001·2007·2011은 common Long, 2002는 복수 채권 Long, 2003은 senior secured bank debt Long, 2004는 convert Long/common Short pair, 2017은 merger Long과 post-close CTL hold다. NXST 두 건은 common Long이다.

## 핵심 판정

1. **LVLT 2000·2001 common:** fiber/IP 자산은 생존했지만 -70% 및 $81→약 $5 회고가 near-term Long을 강하게 반증했다. replacement cost는 common floor가 아니었다.
2. **LVLT 2002 bonds:** 회사가 파산을 피하고 여러 2008·2010 채무를 지급해 broad credit thesis는 성공했다. 원문이 단일 CUSIP을 고정하지 않아 exact 25~35% IRR은 미검증이다.
3. **LVLT 2003 bank debt:** 83에 산 $1.125bn senior secured facility는 2003년 전액상환돼 가장 깨끗한 성공 사례다.
4. **LVLT 2004 convert/common pair:** bond survival과 dilution은 적중했지만 tender·exchange·borrow ledger가 없어 exact pair IRR은 만들지 않았다.
5. **LVLT 2007 common:** 2011 EBITDA $958m은 $2.2bn forecast보다 약 56% 낮았고 2~3년 $9 target은 실패했다.
6. **LVLT 2011 common:** 2013 FCF $900m 기대 대비 실제 약 -$47m으로 timing은 실패했다. 2014~16 FCF와 2017 매각은 delayed thesis success다.
7. **LVLT 2017 merger:** 계약대가 수령은 성공했으나 post-close $75~90·dividend safety는 2019 cut과 2022 elimination으로 실패했다.
8. **NXST 2005·2011:** Batch 039 V9 정본을 그대로 재사용했다. 2005는 사업논지 성공·가격성과 미검증, 2011은 retransmission·M&A·deleveraging이 강하게 적중했다.

## 공통 분석식

`CNS revenue - access/network cost - SG&A - cash interest - capex - tax = common equity FCF`

Debt는 `enterprise recovery × seniority + coupon + tender/exchange consideration - purchase price`로 계산한다. Pair는 bond·short·option·borrow의 날짜별 cash flow를 합산한다.

## 상위 교훈

1. traffic·TAM·replacement cost보다 price-cost spread와 debt waterfall이 먼저다.
2. distress에서 좋은 company call보다 좋은 security selection이 더 높은 확률의 수익을 만든다.
3. EBITDA, FCF, dividend capacity는 같은 숫자가 아니다.
4. merger arb와 post-close long은 별도의 position·horizon·falsifier를 가져야 한다.
5. 정확한 CUSIP·borrow·cash-flow dates가 없으면 exact IRR을 만들지 않는다.

## 중복·정본 처리

- LVLT 2000·2001은 Batch 035의 짧은 구판을 이번 개별 V9 정본으로 승격했다.
- NXST 2005·2011은 Batch 039에 이미 완성된 V9 canonical 파일과 overlay row를 재사용해 내용 충돌을 막았다.

## 앱/DB 반영

- `analysis/batch_043_level3_nexstar_10.md`는 10개 canonical 파일을 불러오는 wrapper다.
- `data/curated/batch_043_level3_nexstar_deep_v7.json`은 V9 상세 overlay다.
