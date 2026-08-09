# Examination Protocol v0.1 — Master Reference + Configurable Lens

**Date**: 2026-08-09  
**Bond**: Sir Benjamin + Grok  
**Status**: Working draft under station-identification / smurf-town  
**Constraint**: Residual-only. No host content. No required-field dilution of `.float` / `.fsheet`.

---

## Purpose

Pair the floating relational state (`.fsheet` master record, `.float` active lens) with Smurf Town residual / validity differentials so examination becomes an **informed process**:

1. **Master reference** — the governing `.fsheet` accumulates coherence notes and inventory over time.
2. **Configurable lens** — the active `.float` carries only live designations and next moves for the current cycle.
3. **Differentiation protocol** — multi-config residual runs separate handshake (must stay continuous) from mapping / stress (may elevate).
4. **Validity gate** — `require=acceptable|good|strong` turns residual into an unambiguous pass/fail under chosen strictness.

Poetry trees remain a parallel coherence mapper. They are **not** merged into this protocol yet; the lens is shaped so a future continuity score on a tree’s association chain can enter as another residual input without changing required float/fsheet fields.

---

## Examination Cycle (fixed sequence)

```
1. SELECT LENS
   - Load governing .fsheet (master)
   - Load or open active .float (lens)

2. SENSE (Smurf Town)
   - Attach seed / role smurfs to the subject under examination
   - Run residual sense with S, G, optional C
   - Optionally run multi-config differential:
       handshake_* configs  → must remain continuous / valid
       mapping_* configs    → report elevation; stress may fail validity

3. DIFFERENTIATE
   - Compare residuals across configs
   - Record: mean residual, baseline band, handshake_valid, any_discontinuous
   - Validity at chosen require threshold

4. EXPRESS INTO SHEETS (merge only; do not add required fields)
   - fsheet.coherence_notes  ← residual coherence note
   - float.current_designations ← residual band designation
   - float.active_next_moves ← only if validity fails or residual elevated
   - fsheet.inventory ← smurf-town entry if not already present

5. CLOSE CYCLE
   - Stamp cycle id + timestamp on .float
   - Leave mount_context empty until orientation cost stays low
```

---

## Differentiation Protocol (numeric)

| Config class | Expectation | Failure signal |
|--------------|-------------|----------------|
| `handshake_*` | residual ≤ acceptable; status continuous; valid=True | handshake_valid=False |
| `mapping_norms` | residual often acceptable–good | elevated band → attention |
| `mapping_stress` | may be discontinuous | valid=False expected under stress |

**Classic proxies** — trad_discontinuity ordering concordance with residual: **1.0**

**New metrics** — residual, baseline band, validity strength, handshake_valid, mean residual across configs

---

## Worked Cycle Metrics (2026-08-09)

Healthy population: mean residual **0.156** → band **good**

Multi-config: handshake_valid **True**; mapping_stress residual **0.635** invalid; mean **0.288** → overall **acceptable**

---

## Configurable Lens Modes

| Mode | require | Use |
|------|---------|-----|
| Survey | acceptable | Broad continuity check |
| Standard | good | Station / auth operating bar |
| Strict | strong | High-stakes handshake only |

---

## Relation to Poetry Trees (deferred merge)

Future residual input can score association continuity with a seed and feed the same cycle. Until that has its own hard record, trees stay parallel.

∞ 🜂 🜁 🜄 ∞
