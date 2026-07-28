# Theory Review Package Template

Use this structure for any new theory (e.g., cw-spiral, MSS Protocol, or future additions) dropped into sandbox/grok-review/theories/.

Copy to a new dir like `theory_review_package_mss/` or `theory_review_package_cw-spiral/`, populate the numbered files with content from the raw theory, then run:

python ../review-configs/review_validator.py . --mss-mode

This ensures efficient review: core is delineated and concise, supporting claims separate, equivocations explicitly flagged (no equivocation in core), qualitative (Helix hand) associations included for comprehensiveness.

Once validated + MSS shell processed (see mss-shell/), verified items can reside in mss-shell/verified/ as the "inner shell" for station-identification high-value/verified formulas until monetization or iteration.

See standard_review_schema.json for full spec.

**Force Multiplier**: This config + validator + MSS shell keeps reviews safe (bias-free, quarantined scrutiny per MSS Protocol), effective (faster delineation of core vs claims/equivocation), and robust for the pipeline without heavy parallel/GPU load (pure file/structural processing).

The spiral never ends.
