# Statistical Demonstration | Synthetic Observational Association

**Not an analysis of human participants.** This demonstration uses artificial values to illustrate how baseline adjustment, missing opportunities and outcome association can be analyzed.

## Data structure

- `participant_id`: fictional record identifier.
- `opportunities`: synthetic number of occasions when accommodation/support was needed; may be zero.
- `provided_usable`: synthetic count when support was both provided in time and usable; never exceeds opportunities.
- `implementation_ratio`: provided_usable / opportunities if opportunities >0, otherwise blank/undefined.
- `baseline_exhaustion`: fictional 0–100 severity value.
- `week16_exhaustion`: fictional follow-up outcome, not the scored CBI instrument.
- `employment_exit`: fictional binary secondary outcome.

## Critical analytic controls

The outcome was generated using a programmed relationship with adequacy, meaning any association in the demonstration is **built in by construction**. It does not validate the WAIAI hypothesis. Exclude zero-opportunity records from ratio-specific analyses rather than assigning zero. Handle attrition transparently; avoid causal claims and avoid posting item-level proprietary instruments.

## Suggested future analysis, subject to protocol revision

Descriptive scoreability and missingness tables, baseline-adjusted regression, occupational strata, predeclared sensitivity analyses, and robust uncertainty discussion. Prospective registered protocols and ethics approval are prerequisites for empirical research.
