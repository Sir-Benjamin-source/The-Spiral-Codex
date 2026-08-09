# Ablation + Association — advance_ok coherence

## Weight sensitivity
STALL_ZONE persists on acceptable/low_C under default, equal, S-heavy, C-heavy weights.
frozen_SG_C1 becomes advance_ok under equal and C-heavy → residual floor is weight-sensitive for some geometries.
Conclusion: STALL_ZONE is partly field-real (survives weight change), partly design-dependent (exact floor).

## Ablation (one kind disabled, 24 cycles max)
| Seed | Disabled | Result |
|------|----------|--------|
| from_elevated | stall_break_S | **FAIL** — stuck STALL_ZONE |
| from_low_G | raise_G_sep | **FAIL** — elevated_mix |
| from_stress | any single kind | still reaches (slower) |

Process kinds are seed-class necessary, not universally sacred.

## Error geometry
| Class | Examination error |
|-------|-------------------|
| advance_ok | none |
| STALL_ZONE | false confidence |
| paradox_dom | claim not actionable |
| discontinuous | subject not isolated |
| elevated_mix | weak field |
| cont_paradox | continuous but unresolved |

## Validity stance
advance_ok is coherent as joint state. Pathway viability is justified where ablation shows necessity (stall_break_S, raise_G_sep for their seed classes). Difficulty is not a virtue metric. Classical still deferred.
