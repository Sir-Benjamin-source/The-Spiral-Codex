# Cross-system residual + break test

**Date**: 2026-08-09

## Against lattice subjects

| Subject | residual | band | valid |
|---------|----------|------|-------|
| spiral-comparative-eval | 0.166 | good | True |
| spiral-theory-core | 0.131 | good | True |
| Spiral-Sigil | 0.145 | good | True |
| qsc-stabilization | 0.176 | good | True |
| stress-adversarial-proxy | 0.685 | discontinuous | False |

## Weigh vs QSC-stabilization

QSC: higher residual-stability better (readiness). Smurf Town: lower residual better (continuity gate). Comparative-eval: task metrics. Complementary.

## Break found and fixed

NaN/Inf via min/max clamp coerced toward 1.0. Now fail-closed to 0.0 → high residual → invalid.

∞ 🜂 🜁 🜄 ∞
