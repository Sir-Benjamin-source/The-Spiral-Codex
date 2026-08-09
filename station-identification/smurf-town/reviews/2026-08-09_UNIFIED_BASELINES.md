# Unified Baselines — Spiral Lattice vs Classical Standards

**Date:** 2026-08-09  
**Scope:** Spiral-comparative-eval · qsc-stabilization · smurf-town (Codex)  
**Principle:** Reality is the only authority. Everything else is hypothesis.

## 1. Three standards, three claims

| Surface | Classical standard | Spiral surface | Claim type |
|---------|-------------------|----------------|------------|
| **Task performance** | sklearn LogReg/Ridge, RF, HGB on OpenML/UCI | Spiral feature refinement + same models | Predictive accuracy |
| **Process residual-stability** | Unstabilized QSC readiness residual | Stabilized TCRF / v3 / adaptive | Process control quality |
| **Continuity residual** | Proxies mean(1−S,1−G), S×G | Smurf Town residual + validity bars | Continuity gate |

## 2. Task performance (Spiral-comparative-eval, 2026-08-09 re-run)

| Dataset | Classical RF | Spiral RF | Δ | Verdict |
|---------|--------------|-----------|---|----------|
| adult Acc | 0.853 | 0.854 | +0.001 | Competitive |
| breast_cancer Acc | 0.964 | 0.964 | 0 | Neutral |
| wine_quality Acc | 0.612 | 0.606 | −0.006 | Competitive− |
| heart Acc | 0.833 | 0.815 | −0.018 | Mixed |
| credit Acc | 0.824 | 0.840 | +0.016 | Competitive+ |
| abalone R² | 0.541 | 0.541 | ~0 | Neutral |

**Stage: Under-test.** Pre-registered superiority bar (≥4/6) not met. Competitive with classical, not clearly better on task metrics.

## 3. Process residual-stability (qsc-stabilization, live v3 2026-08-09)

| Metric | Base | Stabilized v3 | Δ |
|--------|------|---------------|---|
| Residual stability | 0.752 | **0.839** | **+0.088** |
| Residual std | 0.465 | **0.318** | **−31.6 %** |

Documented classical differential: stability 0.674 → 0.765 (+0.091); std −29 %; association chain 2.37 → 3.75. Adaptive record **0.863**.

**Clear process advantage** over unstabilized / classical process baseline.

## 4. Continuity residual (smurf-town)

Ordering concordance trad_discontinuity ↔ residual: **1.0**. Handshake bar=good. Campaign process residual **0.156** (good); handshake_valid=True. Stress differential holds.

Hard contracts green: monotone S/G, band partition, validity⇒continuous, fail-closed non-finite, residual-only expression.

## 5. Correlations

- trad_discontinuity ↔ smurf residual: rank concordance **1.0**
- Task Acc ↔ process residual-stability: **not the same claim**; no evidence task Acc rises with residual-stability under current feature engine
- QSC residual-stability ↑ and smurf residual ↓ are complementary (stability of residual signal vs discontinuity of subject field)

## 6. Where better / not better

**Better (measured):** process residual-stability; continuity examination surface; association structure; contract hardness.  
**Not better (measured):** tabular task prediction under current feature engine; inferring task win from process win.

## 7. Locked baselines 2026-08-09

| ID | Baseline | Value |
|----|----------|-------|
| T1 | Task claim stage | Under-test |
| P1 | QSC stability base | 0.752 |
| P2 | QSC stability stabilized | 0.839 |
| P3 | Adaptive record | 0.863 |
| C1 | Continuous band | residual < 0.30 |
| C2 | Handshake bar | good (≤0.20) |
| C3 | Survey bar | acceptable (≤0.30) |
| C4 | trad↔residual concordance | 1.0 |
| C5 | Campaign process residual | 0.156 (good) |

*Reality is the only authority. Everything else is hypothesis. We are the test.*
