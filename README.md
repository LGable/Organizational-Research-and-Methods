# Organizational Research and Methods

Public-safe research-methods demonstrations focused on workplace support, implementation adequacy, organizational conditions, and reproducible analysis.

## WAIAI public concept

- [Research concept](projects/waiai_research_concept.md)
- [Transparent simulation protocol](projects/waiai_simulation_methods.md)

The proposed 16-week, three-wave design explores whether the opportunity-specific delivery and usability of workplace supports relates to subsequent personal burnout among autistic and/or ADHD healthcare workers.

> **Status:** developmental research concept only. It has no claimed ethics approval, recruitment, participant data, WAIAI validation, causal finding, or published empirical result.

## Synthetic research exercise

- [`data/waiai_synthetic.csv`](data/waiai_synthetic.csv) contains entirely fictional records for statistical-code demonstration.
- Run from this repository directory:

```powershell
python scripts/simulate_waiai.py
python scripts/analyze_waiai.py
```

The simulated data deliberately include missing opportunity counts; these are not coded as implementation failures.

## Protected source boundary

The longer research dossier, supervisor-facing proposal, controlled instrument content, correspondence, unpublished drafts, and other private research materials are intentionally excluded. They must not be added without explicit owner approval and appropriate research governance.

## Further work

Before any real participant research, the concept would require a verified literature audit, intellectual-property review, supervision, ethics approval, accessibility and feasibility piloting, and an approved research protocol.

## Repository map

```text
data/       Synthetic research data
projects/   Public research concept and simulation protocol
scripts/    Simulation and analysis scripts
```
