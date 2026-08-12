# Spiral Path Variables — Operational Set v0.1
**Date:** 2026-08-12  
**Status:** Locked for residual testing  
**Companion specimen:** RT-2026-08-12-GH-001

All scores 0–10 unless noted. All procedures are re-runnable by independent parties from the same stage record.

---

## Core Formula (provisional combination weights)
\[
\text{Spiral Path} = \left( \frac{\text{TD}}{\text{RF}} \right) \times \text{TW} + (\text{CIR} \times \text{SC}) \pm (\text{AM} \times \text{DA})
\]
The arithmetic form remains provisional. Once the variables prove stable under further tests we will re-fit coefficients or rearrange for isolation. The operational definitions below are the priority.

---

## RF — Relevance Factor
**What it measures**  
Tightness of constraint to the declared Axest claim.

**Procedure**  
1. State Axest in one declarative sentence.  
2. Mark every active assertion: required (+1), compatible (0), diluting (–1).  
3. \( RF = 5 + 5 \times (\text{sum of marks} / n) \), clamp [1,10].

**Scale anchors**  
0/1 = fully diluting or contradictory; 5 = mixed; 10 = every element strictly required.

**Ambiguous language note**  
If an assertion’s relation to Axest is itself ambiguous, mark it 0 and raise an AM flag.

---

## TD — Tangent Depth
**What it measures**  
Volume of material not required by the Axest claim.

**Procedure**  
Classify each element: Core / Supportive / Derivative / Orthogonal.  
\( TD = 10 \times (\text{Derivative} + \text{Orthogonal}) / n \) (Derivative may be weighted 0.5).

**Scale anchors**  
0 = zero non-pertinent; 5 = half non-pertinent; 10 = all non-pertinent.

**External interaction**  
All unauthenticated external elements count as Orthogonal (or Derivative at most) and therefore raise TD.

---

## TW — Thematic Weight
**What it measures**  
Density of thematic necessity relative to the governing theme.

**Procedure**  
For each element: necessary (1.0), partial (0.5), none (0).  
\( TW = 10 \times (\text{sum} / n) \).

**Scale anchors**  
0 = no necessity; 5 = half necessary; 10 = every element necessary.

**Ambiguous language note**  
“Necessary” requires an explicit statement of why the theme collapses or weakens without the element.

---

## CIR — Conceptual Integration Rate
**What it measures**  
Actual reduction in independent conceptual pieces via explicit binding.

**Procedure**  
Count distinct elements before and after linking work.  
\( CIR = 10 \times (N_{\rm before} - N_{\rm after}) / N_{\rm before} \).

**Scale anchors**  
0 = no reduction; 5 = half bound; 10 = full collapse into coherent relations.

**Ambiguous language note**  
Mere co-occurrence or shared vocabulary does not count as binding.

---

## SC — Semantic Connection
**What it measures**  
Fraction of claimed pairs that carry an explicit, inspectable link.

**Procedure**  
For every pair the stage claims is related: explicit link = 1, otherwise 0.  
\( SC = 10 \times (\text{explicit pairs} / \text{claimed pairs}) \).

**Scale anchors**  
0 = no explicit links; 5 = half explicit; 10 = every claimed pair explicit.

**External interaction**  
Unauthenticated external elements cannot contribute positive SC.

---

## AM — Ambiguity Management
**What it measures**  
How explicitly ambiguities are named and either resolved by rule or carried as residual.

**Procedure**  
Score each ambiguity: named+ruled (1.0), named+resolved (0.8), vague (0.3), unacknowledged (0).  
\( AM = 10 \times (\text{sum} / A) \). If A = 0, AM = 10.

**Scale anchors**  
0 = unacknowledged; 5 = mixed quality; 10 = all named and ruled or deliberately carried.

**Ambiguous language guideline**  
Any sentence that admits multiple incompatible readings is an ambiguity and must be listed.

---

## DA — Dynamic Adjustment
**What it measures**  
Observable, residual-triggered changes to claims, weights, or thresholds.

**Procedure**  
Count opportunities (new residual or contradiction) and score actual adjustments (1.0 residual-triggered, 0.4 narrative, 0.0 none).  
\( DA = 10 \times (\text{sum} / \text{opportunities}) \).

**Scale anchors**  
0 = pressure present, no adjustment; 5 = partial updates; 10 = every opportunity produced reasoned change.

**Relation to other variables**  
High TD or low RF/TW that is *not* followed by adjustment lowers DA.

---

## External Link / Tangential Data Rule (hard constraint)
1. Tag all external elements `external`.  
2. They raise TD immediately.  
3. They cannot raise SC, CIR, or TW until authenticated (approved source, provenance check, or sovereign checkpoint).  
4. Failed or refused authentication → residual-report as discontinuous and discard from the integrated set.

---

## External Methodological Anchor
Boehm, B. W. (1986/1988). A Spiral Model of Software Development and Enhancement. *ACM SIGSOFT Software Engineering Notes* / *Computer*, 21(5), 61–72.

---

*Space deliberately left for the new. Current definitions + one iteration reserved.*
