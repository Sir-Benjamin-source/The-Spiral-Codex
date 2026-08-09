# Float — stall + dual-signal

```yaml
format: float
format_version: "0.1"
governing_fsheet: "station-identification/float/seeds/2026-08-09_ecosystem.fsheet.md"
cycle_stamp:
  id: "2026-08-09-stall-dual-signal"
  timestamp: "2026-08-09T19:00:00Z"
current_designations:
  - target: "STALL_ZONE"
    designation: "resid > 0.20 ∧ A-P > 0 — S/G lag floors residual after separation recovers"
    since: "2026-08-09T19:00:00Z"
  - target: "update rules without STALL_ZONE clause"
    designation: "incomplete for elevated recovery"
    since: "2026-08-09T19:00:00Z"
  - target: "dual-signal definition"
    designation: "enriched with STALL_ZONE; advance_ok unchanged as resid≤0.20 ∧ A-P>0"
    since: "2026-08-09T19:00:00Z"
  - target: "classical RF metrics"
    designation: "floor reference only — label-settlement; not theory contest outcome"
    since: "2026-08-09T19:00:00Z"
  - target: "single universal cycles_to_X"
    designation: "untenable"
    since: "2026-08-09T18:50:00Z"
active_next_moves:
  - action: "Include STALL_ZONE branch in any recovery update rule before claiming recovery viability"
    priority: 1
  - action: "Keep classical numbers as floor reference; do not grade advance_ok by Acc"
    priority: 2
mount_context:
  process_profile: stall-dual-signal
  classic_floor: true
  spiral_method_on_field: false
  cause_oriented_float: true
```
