# Elevated Stall + Dual-Signal Differentiation — 2026-08-09

## Stall mechanics
Once A−P > 0, strong update polished only C/E. S frozen 0.76, G frozen 0.68 → residual floor ≈ 0.236 (r_S+r_G). STALL_ZONE = resid > 0.20 ∧ A−P > 0.

Stall break: prefer raising S (then G) in STALL_ZONE → advance_ok cycle 6.

## Dual-signal classes (enriched)
| Class | Definition |
|-------|------------|
| advance_ok | resid ≤ 0.20 ∧ A−P > 0 |
| STALL_ZONE | resid > 0.20 ∧ A−P > 0 |
| paradox_dom | A−P < −0.3 |
| discontinuous | resid > 0.55 |

Single-metric residual-only or A−P-only remains untenable.

## Classical floor (reference only)
classic/ RF Acc/R² as prior run. Classical = label-settlement. Does not report residual continuity, A−P, STALL_ZONE, handshake differential.

## Cross-check
Fail-closed, monotone, handshake differential hold. cycles_to_good schedule-tied. γ-controls-A−P untenable. Task contest still deferred.
