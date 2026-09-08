# Batch 047 — V9 Index

## Scope

Batch 047 contains **10 canonical VIC idea files** selected from the SQL-derived unreviewed queue after Batches 043–046.

### 1. Brink's — remaining record
- [2020-05-28 BCO — direction pending](ideas/2020/2020-05-28_BCO_direction_pending.md)
- idea_id `d1cfc369-1bf6-491c-b398-13877c9d394d`
- Raw SQL: Short
- Research note: original body is not available in the current repository extraction, so direction is deliberately not overwritten.

### 2. CIT Group — remaining four records
- [2009-07-28 CIT senior unsecured debt Long](ideas/2009/2009-07-28_CIT_senior_unsecured_long.md)
- [2011-10-04 CIT — direction/security pending](ideas/2011/2011-10-04_CIT_direction_pending.md)
- [2016-03-03 CIT — direction/security pending](ideas/2016/2016-03-03_CIT_direction_pending.md)
- [2020-10-19 CIT — direction/security pending](ideas/2020/2020-10-19_CIT_direction_pending.md)

The 2009 record receives a research-layer correction: the investment should be analyzed as a **Long in CIT senior unsecured debt**, not as a common-equity Short. This distinction is central because the relevant payoff is restructuring recovery, not residual equity value.

### 3. KAR Auction Services — first five of seven records
- [2006-09-13 KAR — direction/security pending](ideas/2006/2006-09-13_KAR_direction_pending.md)
- [2010-11-12 KAR — direction/security pending](ideas/2010/2010-11-12_KAR_direction_pending.md)
- [2018-08-01 KAR — direction/security pending](ideas/2018/2018-08-01_KAR_direction_pending.md)
- [2019-03-04 KAR Long](ideas/2019/2019-03-04_KAR_long.md)
- [2019-11-20 KAR Long](ideas/2019/2019-11-20_KAR_long.md)

## Cross-idea research map

### CIT lifecycle
The useful way to read the CIT series is not as seven repetitions of 'cheap financial stock.' The investment problem changes across the cycle:

1. **2007–09:** liquidity, collateral, maturity ladder and claim priority dominate.
2. **2009 restructuring:** security selection determines outcome; enterprise distress does not imply zero senior-debt recovery.
3. **2011 onward:** funding transformation, legacy runoff and normalized ROTCE become the key variables.
4. **2016 onward:** bank deposit mix, portfolio simplification and capital return matter more than headline book value.
5. **2020:** reserve adequacy, stress TBV and strategic consolidation dominate.

This progression is a reusable framework for financial-company research: `liquidity survival → claim recovery → funding normalization → ROTCE → capital return / strategic value`.

### KAR lifecycle
KAR should be understood as a marketplace plus dealer-finance system rather than a simple auto-volume cyclical:

- physical auction network creates local liquidity and price discovery;
- off-lease and repossession supply drive inventory but not necessarily conversion;
- digital migration can both cannibalize physical revenue and improve cost-to-serve;
- ancillary services raise revenue and contribution per vehicle;
- dealer finance increases marketplace liquidity but adds credit risk;
- portfolio sales must be evaluated on **net proceeds to equity**, not gross headline value.

The most important transition metric is therefore not revenue growth but:

`transaction count × contribution per transaction × liquidity retention – stranded physical cost`.

## Batch-level lessons

1. **Security selection can dominate the business thesis.** CIT 2009 is the clearest example: a company can enter bankruptcy while senior unsecured debt still has an attractive expected recovery.
2. **Low P/B is not automatically cheap.** For post-restructuring financials, discount persistence depends on funding cost, normalized ROTCE and whether excess capital can actually be returned.
3. **Marketplace volume is not enough.** KAR requires conversion rate, buyer density, fee per vehicle, ancillary attach and digital cost-to-serve.
4. **Digital cannibalization can still create value.** Revenue per transaction may fall while contribution margin and incremental ROIC rise.
5. **Asset-sale headlines overstate shareholder value unless taxes, debt repayment and stranded costs are deducted.**
6. **Structural industry decline and equity decline are different propositions.** Brink's can offset lower cash volume with pricing, outsourcing penetration, route density and consolidation.

## Precision status

The canonical files intentionally distinguish three confidence levels:

- **Verified correction:** CIT 2009 senior unsecured Long.
- **Raw Long retained:** KAR 2019-03 and 2019-11.
- **Direction/security pending:** records where the current repository extraction lacks the original VIC body.

Exact T0 price, total-return series, realized/mark-to-market IRR, MFE/MAE and claim-specific exit values are not fabricated. They remain follow-up precision tasks where reliable historical market data or the original security terms are required.

## V9 rules retained

- Raw SQL metadata remains separate from research direction/security.
- One VIC idea = one canonical file.
- Company/business thesis, valuation thesis, balance-sheet thesis, catalyst/timing, security selection and final investment outcome are judged separately.
- Exact IRR is only inserted after verified entry and exit data.
