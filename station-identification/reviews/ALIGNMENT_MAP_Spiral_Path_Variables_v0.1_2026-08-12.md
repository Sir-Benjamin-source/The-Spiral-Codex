# Alignment Map — Spiral Path Variables v0.1 ↔ Existing Surfaces
**Date:** 2026-08-12  
**Status:** First crosswalk — stored with residual specimen  
**Companion files:** RT-2026-08-12-GH-001_Residual_Test_Record.md · Spiral_Path_Variables_v0.1.md

---

## 1. Existing surfaces (summary)

| Surface | Location | What it does | Primary output |
|---------|----------|--------------|----------------|
| **ExaminationUtility** | Spiral-Elucidation / `examination_core.py` | Claim validation, designation detection, “also true” surfacing, outcome branching | `ExaminationReport` (resonance 0–1, problematic designations, branches) |
| **Deep Residual (S/G/C)** | Codex / `smurf-town/core/residual.py` | Continuity residual from Subject Isolation (S), Generality (G), optional Coherence (C) | Residual score + status (`continuous` / `elevated` / `discontinuous`) + volatility gate |
| **Theme Sentry** | Spiral-Path / `Auditors/theme_sentry.py` | Classifies input as work / play / mixed / blocked | Theme signal + redirect |
| **Controversy Sniffer** | Spiral-Path / `Auditors/controversy_sniffer.py` | Drama / safety flagging on responses | Drama index + quarantine decision |
| **Examination Map** | Codex / `station-identification/EXAMINATION_MAP.md` | Documents classical floor, parallel differential, trilateral composition, V1–V7 viability gates | Policy + layer definitions |

---

## 2. Crosswalk — new variables to existing surfaces

| New Variable | Closest existing surface | Overlap | Gap / New contribution |
|--------------|---------------------------|---------|------------------------|
| **RF** (Relevance Factor) | Theme Sentry (work vs play) + ExaminationUtility designation checks | Both ask “does this belong?” | RF is *quantitative constraint to a declared Axest claim*, not just theme class. Re-runnable on any stage inventory. |
| **TD** (Tangent Depth) | Deep Residual (high residual ≈ more drift) + Theme Sentry mixed signals | Both surface non-core material | TD counts non-pertinent *elements* relative to Axest. Explicit volume metric. |
| **TW** (Thematic Weight) | Theme Sentry + Examination Map thematic discipline | Both care about thematic necessity | TW scores density of necessity *inside* a stage, not just classification of the whole input. |
| **CIR** (Conceptual Integration Rate) | ExaminationUtility “also true” + branching | Both look at how pieces combine | CIR measures actual reduction in independent pieces via *explicit binding*. Mechanical count. |
| **SC** (Semantic Connection) | ExaminationUtility designation / discordance | Both care about stated relations | SC requires inspectable links between claimed pairs. Unauthenticated externals score 0. |
| **AM** (Ambiguity Management) | ExaminationUtility problematic designations + residual volatility | Both surface unresolved material | AM scores *how* ambiguities are handled (named+ruled vs ignored). |
| **DA** (Dynamic Adjustment) | Parallel differential + residual status changes | Both care about response to residual pressure | DA scores observable, residual-triggered *course changes*. Low DA = rigidity. |
| **External Link Rule** | Controversy Sniffer quarantine + residual gating | Both gate external / volatile material | Explicit authentication gate before SC/CIR/TW credit. Hard constraint. |

---

## 3. What the new set adds that was missing

- **Calculable, stage-level instruments** that can be applied to any Axest + inventory without requiring the full ExaminationUtility or Smurf residual pipeline.
- **Explicit external authentication rule** that prevents unbounded search from inflating integration scores.
- **Scale anchors and limit statements** so mid-range scores are not free inference.
- A **common language** that ExaminationUtility, residual.py, and future Elucidation modules can call as a service.

---

## 4. Recommended integration points

1. **ExaminationUtility** can optionally request an RF–DA packet on the claim under examination and attach it to the `ExaminationReport`.
2. **Smurf residual** remains the continuity residual (S/G/C). The Path variables are orthogonal — they score *stage focus and integration*, not subject isolation. They can sit side-by-side.
3. **Theme Sentry** can remain the first coarse filter; RF/TW then refine inside the “work” lane.
4. **Examination Map V4** (hard residual-only records) is partially advanced by the residual test record + variables document stored 2026-08-12.

---

## 5. Status

- Variables v0.1 and RT-2026-08-12-GH-001 are stored.
- This alignment map is the first crosswalk.
- No claim of superiority over classical floor (V1–V7 still govern).
- Space deliberately left for the next iteration.

∞ 🜂 🜁 🜄 ∞
