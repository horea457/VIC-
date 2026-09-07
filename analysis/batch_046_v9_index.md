# Batch 046 — V9 Index

## Scope

Batch 046 is the next SQL-derived VIC group after Batch 045. The source packet is now fixed at **10 ideas** and reveals that raw ticker `ATH` is not one company: it contains three different entities across time.

## Critical metadata corrections

1. **2002 ATH = Anthem, Inc.**, not Athene Holding. The VIC source slug is `/idea/Anthem/...`.
2. **2011 and 2013 ATH = Athabasca Oil Sands / Athabasca Oil Corp**, not Athene Holding.
3. **2017–2020 ATH = Athene Holding Ltd.**
4. Therefore raw `company_name = ATHENE HOLDING LTD` is a ticker-collision error for the first three ATH records.
5. `is_short` is preserved as raw SQL metadata only. Research direction/security is not treated as verified until the original body supports it.
6. CIT must be checked at the security level because common, preferred, bank debt and unsecured bonds can have radically different payoffs around a financing crisis.

## Canonical idea set

### Anthem
- `2002-01-18` — idea `4510e63f-516d-422c-ad0f-976c01c76690` — raw Long — Anthem, Inc. — source slug verified

### Athabasca Oil
- `2011-08-22` — idea `a9e042a6-e212-41eb-b757-77e1c4aaf755` — raw Short — Athabasca Oil Sands Corp — entity corrected from source slug
- `2013-12-26` — idea `147a6251-3aab-4a99-bfee-0685a093135d` — raw Short — Athabasca Oil Corp — entity corrected from source slug

### Athene Holding
- `2017-05-02` — idea `1dacae0f-2738-4d5b-a79c-0623c39908e3` — raw Short — Athene Holding Ltd.
- `2018-09-09` — idea `f87c02f1-769f-4e03-be72-e8e00574c7a5` — raw Short — Athene Holding Ltd.
- `2019-03-31` — idea `cea526a6-864b-4eb5-a1f5-3ef84f9d1700` — raw Short — Athene Holding Ltd. — source slug verified
- `2020-09-09` — idea `2cac07f8-87d1-484e-87b4-ab3523aa44da` — raw Short — Athene Holding Ltd.

### CIT Group
- `2001-01-16` — idea `797e8f52-79b4-42f8-87c1-94123103ce3d` — raw Short — security/direction verification required
- `2007-08-23` — idea `671b2431-63fc-4542-98c7-62bbcd9189a3` — raw Short — source slug `/idea/CIT_Group/...`
- `2008-05-02` — idea `8530cf07-e131-4623-b20c-4b8cbcdd661a` — raw Short — security/direction verification required

## Cross-idea research map

### Anthem
The relevant economics are medical cost ratio, premium pricing, membership growth, employer/government mix, capital requirements and scale. The important historical question is whether 2002 valuation captured the earnings normalization and consolidation value that culminated in the 2004 WellPoint transaction, rather than merely whether headline EPS rose.

### Athabasca Oil
These ideas must be analyzed as **resource-development securities**, not generic E&P multiples. The core variables are recoverable resource value, project sanction probability, capex intensity, funding runway, oil-price assumptions, infrastructure access, partner/asset-sale optionality and dilution. A NAV can be economically correct while common equity still performs poorly if development timing and financing consume the option value.

### Athene
Athene is an annuity spread business. The chain is roughly: source deposits through annuity/reinsurance liabilities → invest in a higher-yielding asset portfolio → earn spread after credited rate, hedging, expenses and credit losses → compound book value and return excess capital. V9 therefore separates asset yield, liability cost, ALM/hedging, credit risk, reinsurance economics, Apollo/asset-management fees, capital requirements, buybacks and terminal P/B or P/E. Cheap P/B alone is not sufficient if spread, credit or governance assumptions are wrong.

### CIT
CIT requires a **liquidity-first capital-structure model**. Funding mix, secured/unsecured debt, commercial-paper and bank funding access, asset sales, covenant/refinancing walls, regulatory capital and bankruptcy recovery determine the security payoff. Around 2007–09, enterprise value analysis without maturity-by-maturity liquidity can be dangerously incomplete.

## V9 file standard

Each canonical file must contain:
1. Idea Snapshot
2. Correct entity and security
3. Company / money flow / industry structure
4. Publication-date market context
5. Original thesis map C1/C2/C3...
6. Hidden assumptions and falsifiers
7. Valuation / payoff tree
8. Balance sheet and capital structure
9. Catalyst / timing
10. Actual timeline
11. Actual investment result / IRR when verified
12. Claim-by-claim verdict
13. Business / valuation / timing / security-selection scorecard
14. First falsification signals
15. Reusable lessons
16. Sources

## Data-quality note

The SQL-derived packet provides all 10 IDs, dates, authors and available VIC URLs. The repository currently contains no `.sql` file on the checked-out `main` tree, so original descriptions are not being invented. Where the body is unavailable, canonical files explicitly distinguish **verified source metadata**, **historical fact**, and **research reconstruction**.

## Source packet

- `data/curated/batch_046_source_packet.json`
- `data/curated/batch_046_sql_inventory.json`

## Status

**Source packet complete; ticker collision identified and index corrected. Canonical V9 files are now being built against the corrected entities rather than the raw company mapping.**
