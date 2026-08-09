# Float — Joint load + calibration determinations

```yaml
format: float
format_version: "0.1"
governing_fsheet: "station-identification/float/seeds/2026-08-09_ecosystem.fsheet.md"
cycle_stamp:
  id: "2026-08-09-joint-load-calibration"
  timestamp: "2026-08-09T18:45:00Z"
current_designations:
  - target: "dual-signal viability gate"
    designation: "required — resid≤0.20 ∧ A-P>0 for advance_ok; single-metric gates untenable"
    since: "2026-08-09T18:45:00Z"
  - target: "STALL_ZONE"
    designation: "resid>0.20 ∧ A-P>0 — must raise S/G; C-only polish incomplete"
    since: "2026-08-09T18:45:00Z"
  - target: "advance_ok pathway"
    designation: "viable recognition+recovery class under stall-aware update rule — cycles 1–10 seed-dependent"
    since: "2026-08-09T18:45:00Z"
  - target: "cycles_to_advance_ok"
    designation: "range not scalar — provisional band 1–10 under stall-aware rule"
    since: "2026-08-09T18:45:00Z"
  - target: "universal single cohesion cycle count"
    designation: "untenable without update-rule and seed class"
    since: "2026-08-09T18:45:00Z"
  - target: "classical comparative"
    designation: "deferred"
    since: "2026-08-09T17:45:00Z"
active_next_moves:
  - action: "Lock dual-signal class definitions as internal baseline"
    priority: 1
  - action: "Optional: VAAS S_i calibration on real variable set"
    priority: 2
  - action: "Hold classical comparison"
    priority: 3
mount_context:
  process_profile: joint-load-calibration
  classic_floor: true
  spiral_method_on_field: false
  residual_handshake_bar: good
  cause_oriented_float: true
```
