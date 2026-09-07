# Batch 046 — V9 Index

## Scope
Batch 046 is complete as a **10-idea canonical V9 packet**. The SQL-derived `ATH` bucket was a ticker-collision set, not one company.

## Critical metadata corrections
1. **2002 ATH = Anthem, Inc.**, not Athene Holding.
2. **2011/2013 ATH = Athabasca Oil Sands / Athabasca Oil Corp.**
3. **2017–2020 ATH = Athene Holding Ltd.**
4. Therefore the raw `company_name = ATHENE HOLDING LTD` mapping is wrong for the first three ATH records.
5. Raw `is_short` is preserved as source metadata only; research direction stays provisional where the original body is not available.
6. CIT is treated as a capital-structure problem. Security type must be verified before exact return scoring.

## Canonical files

### Anthem
- [2002-01-18 Anthem](ideas/2002/2002-01-18_ANTHEM_long.md) — `4510e63f-516d-422c-ad0f-976c01c76690`

### Athabasca Oil
- [2011-08-22 Athabasca Oil Sands](ideas/2011/2011-08-22_ATHABASCA_OIL_short.md) — `a9e042a6-e212-41eb-b757-77e1c4aaf755`
- [2013-12-26 Athabasca Oil](ideas/2013/2013-12-26_ATHABASCA_OIL_short.md) — `147a6251-3aab-4a99-bfee-0685a093135d`

### Athene Holding
- [2017-05-02 Athene](ideas/2017/2017-05-02_ATHENE_short.md) — `1dacae0f-2738-4d5b-a79c-0623c39908e3`
- [2018-09-09 Athene](ideas/2018/2018-09-09_ATHENE_short.md) — `f87c02f1-769f-4e03-be72-e8e00574c7a5`
- [2019-03-31 Athene](ideas/2019/2019-03-31_ATHENE_short.md) — `cea526a6-864b-4eb5-a1f5-3ef84f9d1700`
- [2020-09-09 Athene](ideas/2020/2020-09-09_ATHENE_short.md) — `2cac07f8-87d1-484e-87b4-ab3523aa44da`

### CIT Group
- [2001-01-16 CIT](ideas/2001/2001-01-16_CIT_short.md) — `797e8f52-79b4-42f8-87c1-94123103ce3d`
- [2007-08-23 CIT](ideas/2007/2007-08-23_CIT_short.md) — `671b2431-63fc-4542-98c7-62bbcd9189a3`
- [2008-05-02 CIT](ideas/2008/2008-05-02_CIT_short.md) — `8530cf07-e131-4623-b20c-4b8cbcdd661a`

## Cross-idea lessons

### 1. Ticker is not entity
The largest data error in this batch is not valuation but identity. A single raw ticker `ATH` spans a health insurer, a Canadian oil developer and an annuity platform. Any downstream thesis, sector classification or return analysis is invalid unless entity mapping is fixed first.

### 2. Athabasca: NAV is not equity value until the funding bridge is modeled
Resource value must be converted through remaining capex, timing, oil-price assumptions, infrastructure, project sanction and dilution. Development time functions like leverage even when reported debt is modest.

### 3. Athene: P/B needs a capital-duration-credit bridge
Annuity economics require asset yield, liability cost, duration/hedging, realized credit losses, statutory capital, Apollo economics and capital allocation. Market stress can hurt marks while improving future reinvestment spreads, so mark risk and economic loss must be separated.

### 4. CIT: liquidity can kill equity before accounting solvency
For wholesale-funded lenders, the maturity ladder, collateral, secured/unsecured funding, ratings triggers and realizable asset value dominate P/E and reported book value. Security hierarchy can make the same enterprise thesis bullish for one tranche and bearish for another.

### 5. Hindsight discipline
CIT's 2009 bankruptcy, Athabasca's exposure to the later oil collapse, and Athene's eventual Apollo combination are useful terminal facts, but they do not by themselves prove a 2001/2007/2011/2017 trade was good. Final V9 scoring must still use the original horizon, security and entry price.

## Data-quality / remaining precision work
- Source packet: `data/curated/batch_046_source_packet.json`
- SQL inventory on current `main`: `data/curated/batch_046_sql_inventory.json`
- The current checked-out tree contains no `.sql` file; the packet is derived from prior SQL-extracted census/metadata.
- Exact T0 price, target, 1Y/3Y/5Y returns and IRR are intentionally not fabricated where the original VIC body/security is unavailable.
- When original descriptions are recovered, each provisional direction/security line should be upgraded to verified and the claim map should be rewritten against the author's actual wording.

## Status
**10/10 canonical files created. Entity collisions corrected. Batch 046 is usable as a research layer, with exact price/IRR and original-body claim wording marked as the remaining precision step.**
