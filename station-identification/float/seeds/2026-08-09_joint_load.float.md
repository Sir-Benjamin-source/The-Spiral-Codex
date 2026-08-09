# Float — Joint load determinations

**Style:** cause-oriented

```yaml
format: float
format_version: "0.1"
governing_fsheet: "station-identification/float/seeds/2026-08-09_ecosystem.fsheet.md"
cycle_stamp:
  id: "2026-08-09-joint-residual-parallel"
  timestamp: "2026-08-09T18:40:00Z"
current_designations:
  - target: "residual vs A-P"
    designation: "orthogonal signals — continuous residual does not imply A-P > 0"
    since: "2026-08-09T18:40:00Z"
  - target: "single-metric viability"
    designation: "untenable — residual-only or A-P-only insufficient under joint load"
    since: "2026-08-09T18:40:00Z"
  - target: "handshake → advance_ok"
    designation: "pathway pattern candidate (resid≤0.20 and A-P>0)"
    since: "2026-08-09T18:40:00Z"
  - target: "cycles_to_good ≈9"
    designation: "remains provisional — schedule-tied"
    since: "2026-08-09T18:40:00Z"
  - target: "classical comparative"
    designation: "still deferred"
    since: "2026-08-09T17:45:00Z"
active_next_moves:
  - action: "Retest advance_ok under examination-driven S/G/C updates"
    priority: 1
  - action: "Do not promote residual-only or A-P-only to viability gate"
    priority: 2
  - action: "Hold classical comparison until dual-signal pathway baselines dated"
    priority: 3
mount_context:
  process_profile: joint-residual-parallel
  classic_floor: true
  spiral_method_on_field: false
  cause_oriented_float: true
```
