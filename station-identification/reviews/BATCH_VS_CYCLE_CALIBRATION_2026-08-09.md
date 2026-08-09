# Batch vs Cycle Calibration — 2026-08-09

## Hypothesis
A single universal cycle count cannot quantify cohesion. Prefer a **batch count of relational processes** that must complete; cycles spent correlate with cost but are not the viability unit.

## Unit definitions tested

| Unit | Definition | Spread (7 seeds) |
|------|------------|------------------|
| **cycles** | timestep updates | 1–10, mean 5.0, stdev 3.06 |
| **timestep-batches** | 1 dual-signal unit per cycle | identical to cycles |
| **ops** | residual + A−P + class + update | 3–39, mean 19.0, stdev 12.22 |
| **type-batches** | distinct relational process *kinds* fired | **0–4, mean 1.7** |

## Process kinds (catalog)
- `recover_disc` — raise S/G/C from discontinuous
- `recover_elev` — raise S/G/C from elevated residual
- `stall_break_S` — raise S/G while A−P>0 and resid>0.20
- `raise_G_sep` — raise G when A−P≤0
- `polish` — C/E when already advance_ok-adjacent
- `none` — already advance_ok at seed

## Per-seed type composition
| Seed | cycles | type_batches | kinds |
|------|--------|--------------|-------|
| from_handshake | 1 | 0 | none |
| near_good | 2 | 1 | stall_break_S |
| from_low_C | 4 | 1 | stall_break_S |
| from_mid | 5 | 2 | recover_elev, stall_break_S |
| from_elevated | 6 | 2 | recover_elev, stall_break_S |
| from_low_G | 7 | 2 | raise_G_sep, recover_elev |
| from_stress | 10 | 4 | recover_disc, recover_elev, raise_G_sep, stall_break_S |

## Determinations
1. **Never a single universal cycle count** as viability metric — confirmed untenable
2. **Type-batch is the better viability unit**: which relational process kinds must complete
3. **Cycles correlate with validation cost** under a fixed update law — report as cost, not as definition of success
4. **advance_ok viability** = dual-signal class reachable after the required type-batch set for the seed class
5. Seed class implies expected type-batch set (stress needs more kinds than near_good)

## Provisional baseline language
- Do **not** say: “cohesion in N cycles”
- Do say: “advance_ok after completion of required relational process types {…}; cycles spent under rule R were K (cost)”
