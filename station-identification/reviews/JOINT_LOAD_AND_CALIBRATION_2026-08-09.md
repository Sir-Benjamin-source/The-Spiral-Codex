# Joint Load + Calibration — 2026-08-09

## Static joint recognition
| Field | Class | resid | A−P |
|-------|-------|-------|-----|
| handshake | advance_ok | 0.135 | +0.412 |
| good | advance_ok | 0.185 | +0.282 |
| acceptable | STALL_ZONE | 0.285 | +0.090 |
| elevated | elevated_mix | 0.485 | −0.165 |
| stress | discontinuous | 0.785 | −0.300 |
| low_G_paradox | paradox_dom | 0.453 | −0.447 |
| low_C | STALL_ZONE | 0.315 | +0.014 |

## Recovery with STALL_ZONE-aware updates (24 max)
| Seed | cycles to advance_ok | STALL_ZONE seen |
|------|----------------------|-----------------|
| from_handshake | 1 | no |
| near_good | 2 | yes |
| from_low_C | 4 | yes |
| from_mid | 5 | yes |
| from_elevated | 6 | yes |
| from_low_G | 7 | no |
| from_stress | 10 | yes |

**7/7 reached** with stall-aware rule. Range **1–10** under this update law.

## Determinations
1. Dual-signal viability gate required (residual ∧ A−P)
2. STALL_ZONE is a real intermediate (A−P>0 while resid>0.20)
3. Recovery update must raise S/G in STALL_ZONE or elevated recovery stalls
4. cycles_to_advance_ok is a **range** (1–10 here), not one universal integer
5. advance_ok is a viable **pathway class** under explicit update rule
6. Classical comparative still deferred
