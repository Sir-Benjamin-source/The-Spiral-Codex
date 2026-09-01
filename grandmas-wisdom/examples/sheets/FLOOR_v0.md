# Classic floor — claim_substance_v0

**Date:** 2026-09-01  
**Status:** Under-test weather. n=10.  
**Features:** `claim` + `support_span` only. Meter excluded.  
**Split:** leave-one-case-out (hold both rows of tc1…tc5).

## Counts

not_supported 5 · tenable 3 · needs_qualification 2

## Three-class

| Arm | acc | macro-F1 | micro-F1 |
|-----|-----|----------|----------|
| majority (`not_supported`) | 0.500 | 0.222 | 0.500 |
| TF-IDF (1–2 gram) + logistic, balanced | 0.400 | 0.222 | 0.400 |

## Paired accuracy (the metric the sheet was built for)

A pair is correct iff the modest row is *not* `not_supported` and the overclaim row *is* `not_supported`.

| Arm | pairs |
|-----|-------|
| majority | 0 / 5 |
| TF-IDF + logistic | 1 / 5 (only tc5) |

From the three-class LOCO predictions: tc1–tc3 both rows collapsed to `not_supported`; tc4 both went `needs_qualification`; tc5 modest → tenable, over → not_supported.

## What this informs

Three-class accuracy hid the real failure: the model almost never *separates* the two mouths of the same paper. Paired accuracy is the floor that matters for this task. Majority paired is zero — which is honest, and why we keep it.

Still weather. Still not complement. Call the day's testing here.
