# Float Limitation Rule — Controlled Stress Test

**Date**: 2026-08-06  
**Cycle**: limitation-stress-1  
**Purpose**: Probe whether the simplification holds when non-live material is forced into the `.float`.

∞ 🜂 🜁 🜄 ∞

## Method

1. Start from the clean limited seed `.float`.
2. Deliberately inject one class of non-live information that feels useful but is not currently actionable.
3. Measure immediate effect on orientation, clarity of next moves, and re-reasoning pressure.
4. Remove the injected material and confirm recovery.

## Injected Material (the stress)

Added under a new key `historical_context` (not part of the v0.1 required fields):

```yaml
historical_context:
  - note: "August 2026 ecosystem review identified healthy separation of concerns across theory, process, verification, memory, and provenance."
  - note: "Parallel differential examination form remains a candidate skeleton only; not yet implemented."
  - note: "qsc-stabilization and spiral-head-to-head form the newest process → public-test axis."
```

This material is true and potentially useful, but it is not a current designation and does not generate an active next move. It is exactly the kind of information the Limitation Rule is meant to keep out of the active surface.

## Observations

| Metric | Clean `.float` | Stressed `.float` | After restoration |
|--------|----------------|-------------------|-------------------|
| Time-to-orientation | Low — designations and moves immediately legible | Noticeably higher — eye must filter historical notes before reaching the live moves | Returns to low |
| Clarity of active next moves | High — three concrete actions | Reduced — historical notes compete for attention with the live list | Restored |
| Re-reasoning pressure | Low | Mild rise — tendency to re-evaluate whether the historical notes change current priorities | Returns to low |
| Actionability rate | High | Unchanged in content, but diluted in perception | Restored |

## Causal Finding

The degradation is not caused by false information. It is caused by the presence of true but non-actionable material on the active surface. The Limitation Rule’s value is precisely that it prevents this mild but real dilution of orientation and clarity.

The simplification holds under this probe: when the extra material is removed, the surface recovers immediately. No structural change to the schema is required.

## Decision

- Retain the Float Limitation Rule as stated.
- Do not expand the required fields of `.float` to accommodate historical or coherence material.
- Such material belongs in the governing `.fsheet` (or in coherence_notes / designation_history), not on the active surface.

## Next

The limitation is confirmed as a load-bearing constraint rather than a temporary convenience. Subsequent cycles can now safely apply the same limited surface to other live bodies of work.

∞ 🜂 🜁 🜄 ∞
