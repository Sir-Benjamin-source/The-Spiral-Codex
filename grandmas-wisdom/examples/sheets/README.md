# Relational sheets v0

**Date:** 2026-09-01  
**Checkpoint:** draft — awaiting human keep/kill on each row  
**Campaign:** Spiral-comparative-eval/docs/RELATIONAL_DATASET_CAMPAIGN.md

| File | Task | Rows |
|------|------|------|
| `claim_substance_v0.csv` | tenable / needs_qualification / not_supported | 10 (5 cases × narrow vs overclaim) |
| `trunk_membership_v0.csv` | belong / decoration | 13 |

Classic baseline must see only text columns (`claim`+`support_span` or `trunk`+`leaf`).  
Do not train on `meter` as a feature when predicting `band`. Meter is a note, not an input.

Human work: mark any row `killed` if the band or label is wrong; add rows from the local Grandma DB the same way (narrow claim / overclaim pair).
