# Batch 049 — Metals USA / Murphy USA / McDermott V9 Index

> **기준:** Batch 042/048 V9 규칙을 유지한다. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-09.
> **Batch boundary:** Batch 048의 Metals USA 2003 다음 SQL-derived queue 10건 = MUSA 6건 + MDR 4건.

## Canonical Idea Units

| # | 날짜 | Raw ticker | 실제 entity | Raw | 실제 방향 | Canonical | 판정 |
|---:|---|---|---|---|---|---|---|
| 1 | 2011-09-26 | MUSA | Metals USA | Short | **Long** | [Metals USA 2011](ideas/2011/2011-09-26_MUSA_metalsusa_long.md) | $9→$20.65 cash, 강한 성공 |
| 2 | 2013-09-27 | MUSA | Murphy USA | Short | **Long** | [Murphy USA 2013](ideas/2013/2013-09-27_MUSA_murphyusa_long.md) | 5Y +113.8%, 강한 성공 |
| 3 | 2017-07-14 | MUSA | Murphy USA | Short | Short | [MUSA 2017 Short](ideas/2017/2017-07-14_MUSA_short.md) | volume은 맞고 profit/share는 틀림 |
| 4 | 2018-06-27 | MUSA | Murphy USA | Short | Short | [MUSA 2018 Short](ideas/2018/2018-06-27_MUSA_short.md) | 6M 일부 성공 후 실패 |
| 5 | 2020-01-02 | MUSA | Murphy USA | Short | Short | [MUSA 2020 Short](ideas/2020/2020-01-02_MUSA_short.md) | 3M 성공, 1~3Y 강한 실패 |
| 6 | 2021-11-15 | MUSA | Murphy USA | Short | **Long** | [MUSA 2021 Long](ideas/2021/2021-11-15_MUSA_long.md) | 1Y +57.7%, 구조적 CPG 적중 |
| 7 | 2003-02-06 | MDR | McDermott | Long | Long | [MDR 2003](ideas/2003/2003-02-06_MDR_long.md) | SOTP 성공, catalyst 지연 |
| 8 | 2004-06-07 | MDR | McDermott | Long | Long | [MDR 2004](ideas/2004/2004-06-07_MDR_long.md) | BWXT/J.Ray SOTP 성공 |
| 9 | 2008-12-12 | MDR | McDermott | Short | **Long** | [MDR 2008](ideas/2008/2008-12-12_MDR_long.md) | crisis SOTP + spin 성공 방향 |
| 10 | 2012-01-27 | MDR | McDermott | Short | **Long** | [MDR 2012](ideas/2012/2012-01-27_MDR_long.md) | backlog-quality 오판, 실패 |

## Direction / Entity Audit

- `MUSA`는 동일 entity가 아니다.
  - 2003·2011: **Metals USA**
  - 2013 이후: **Murphy USA**
- 2011 Metals USA, 2013 Murphy USA, 2021 Murphy USA는 raw Short → actual Long.
- 2008·2012 McDermott도 raw Short → actual Long.
- Batch 49의 10건 중 5건은 SQL direction만 읽으면 결론이 반대로 뒤집힌다.

## Murphy USA 2013→2021 시계열에서 가장 중요한 논점

### Short들이 본 것
- gasoline gallons/store 구조적 감소
- EV penetration
- tobacco decline
- capex 증가
- RIN normalisation
- leverage + buyback

### 실제로 더 중요했던 것
- **fuel CPG의 구조적 상승**
- low-cost operator의 scale advantage
- merchandise contribution 증가
- high-return R&R / new stores
- QuickChek capability
- 대규모 share-count reduction

따라서 Murphy USA의 경제식은 단순히 `gallons growth`가 아니다.

**Owner earnings/share ≈ gallons × CPG + merchandise contribution - store cost - capex/interest, divided by shrinking share count**

2017·2018 Short는 gallons weakness를 상당히 잘 봤지만, CPG와 buyback이 이를 이길 가능성을 과소평가했다. 2021 Long은 바로 이 구조를 반대로 포착했다.

## McDermott 2003→2012 시계열에서 가장 중요한 논점

초기 아이디어는 **legal/SOTP complexity**에서 알파가 났다.
- B&W asbestos Chapter 11
- BWXT high-quality nuclear/government asset
- J. Ray distressed offshore contractor
- ring-fenced liabilities
- eventual separation

2003/2004에는 복잡성이 mispricing을 만들었고 B&W asbestos exit(2006), spin(2010)으로 value unlock이 실제 발생했다.

반면 2012에는 회사가 pure-play EPCI가 된 뒤 **backlog를 visibility로 해석한 것이 오류**였다. 2013에는 $4.8bn backlog가 있어도 9개 loss-making project와 큰 operating loss가 발생했다.

## Batch 049 상위 교훈

1. **Ticker identity audit은 valuation보다 먼저다.**
2. 수요량 감소 ≠ profit pool 감소. 공급자 pricing behavior를 같이 본다.
3. buyback은 EPS cosmetic이 아니라 낮은 가격에 반복되면 business-level ROIC와 동일하게 compounding한다.
4. service-center FCF에서는 working capital release와 recurring FCF를 분리한다.
5. E&C backlog는 asset이 아니라 아직 확정되지 않은 margin exposure다.
6. fixed-price contractor는 revenue보다 cost-to-complete revision history를 본다.
7. litigation/SOTP catalyst는 맞아도 duration이 길 수 있다.
8. same company라도 lifecycle에 따라 핵심 분석식이 완전히 바뀐다.

## 앱 / DB 반영

- Wrapper: `analysis/batch_049_musa_mdr_10.md`
- Overlay: `data/curated/batch_049_musa_mdr_deep_v7.json`
- Canonical source of truth: 위 10개 idea Markdown.
