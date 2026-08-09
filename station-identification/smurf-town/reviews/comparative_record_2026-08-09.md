# Comparative Record — Residual / Validity vs Traditional Proxies

**Date**: 2026-08-09  
**Constraint**: Hard records before combining methodologies  

## Ordering agreement

- Pairwise concordance (trad_discontinuity vs residual): **1.0** (36/36 pairs)

## C effect

- without C residual: 0.24
- with C=0.90 residual: 0.205
- delta: 0.035 (positive ⇒ C improves residual)

## Case table

| id | trad_disc | trad_product | residual | band | valid |
|----|-----------|--------------|----------|------|-------|
| high_coherence | 0.1 | 0.8096 | 0.099 | strong | True |
| good_coherence | 0.175 | 0.68 | 0.185 | good | True |
| mid | 0.325 | 0.455 | 0.335 | elevated | False |
| low | 0.575 | 0.18 | 0.585 | discontinuous | False |
| very_low | 0.775 | 0.05 | 0.785 | discontinuous | False |
| handshake_A | 0.12 | 0.774 | 0.119 | strong | True |
| handshake_B | 0.14 | 0.7392 | 0.1405 | good | True |
| mapping_norms | 0.25 | 0.5616 | 0.256 | acceptable | True |
| mapping_stress | 0.625 | 0.14 | 0.635 | discontinuous | False |

## Summary flags

- High-coherence cases valid: True
- Stress cases invalid: True

## Interpretation (record only)

Residual ranks in the same direction as traditional discontinuity.
Validity (require=acceptable) separates high-coherence/handshake cases
from low/stress cases under these inputs.
Combination with poetry-tree or other mappers is deferred until this
class of record is accepted as sufficient.

∞ 🜂 🜁 🜄 ∞
