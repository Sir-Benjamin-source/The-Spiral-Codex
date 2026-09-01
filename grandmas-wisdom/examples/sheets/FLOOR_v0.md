# Classic floor — claim_substance_v0

**Date:** 2026-09-01  
**Status:** Under-test weather. n=10.  
**Features:** `claim` + `support_span` only. Meter excluded.  
**Split:** leave-one-case-out (hold both rows of tc1…tc5).

## Counts

not_supported 5 · tenable 3 · needs_qualification 2

## Results

| Arm | acc | macro-F1 | micro-F1 |
|-----|-----|----------|----------|
| majority (`not_supported`) | 0.500 | 0.222 | 0.500 |
| TF-IDF (1–2 gram) + logistic, balanced | 0.400 | 0.222 | 0.400 |

Per-row: the linear model mostly collapsed to `not_supported`. It missed every `tenable` except by accident on the wrong case. Majority won because half the sheet *is* the overclaim we planted.

## What this informs

1. A scope-pair design is the right *shape* and the wrong *balance* at n=10. Next sheet should not let overclaims be the mode, or should report paired accuracy (did it tell modest from overclaim *on the same paper*) as a first-class metric.
2. Two-step labeling (enough-info vs not, then support vs contradict) matches both SCIVER practice and Grandma better than one softmax over three bands.
3. This number is not complement. It is the floor discovering the sheet's own tilt.

## Cousin reminder

SCitance published mid-80s micro-F1 is a *different n, different evidence, different label construction*. Do not write it next to 0.40 as if they were siblings.
