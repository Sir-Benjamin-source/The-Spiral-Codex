# E — Etymological Descent

**Six-Clause Meta-Standard Entry**  
**Version**: 0.1 (Locked 2026-08-04)  
**Status**: Accepted for use in the parallel differential examination form

---

### 1. Name & Symbol
Etymological Descent — \( E \)  
Range: \([0, 1]\), where 1 = maximal recoverable depth and alignment of the subject’s root meanings with established scientific or classical usage.

### 2. Operational Definition
\( E \) quantifies how far, and how cleanly, the dominant subject can be traced to prior, publicly attested roots (etymological, technical, or domain-specific) that still constrain or illuminate its present meaning. High \( E \) means the subject rests on a recoverable lineage that an independent agent can verify; low \( E \) means the term is opaque, newly coined without declared lineage, or its historical/technical senses have been severed.

### 3. Measurement Protocol
Given a dominant subject already isolated by \( S \):

1. Retrieve candidate root or prior-sense records from one or more of:  
   - Standard etymological references (OED, American Heritage, Pokorny, Watkins, etc.)  
   - Domain technical glossaries or first-use citations in the relevant scientific literature  
   - Controlled vocabulary / ontology ancestors (MeSH, Gene Ontology, IEEE taxonomy, etc.) when the subject is technical  
2. Score depth:  
   - Number of recoverable prior stages or the temporal/semantic distance to the earliest attested relevant sense, normalized against a declared maximum.  
3. Score alignment:  
   - Degree to which the current usage remains consistent with, or is a documented specialization of, the recovered root sense(s). Inconsistency or radical semantic drift lowers the score.  
4. Combine:  
   \( E = \beta \cdot \text{depth} + (1 - \beta) \cdot \text{alignment} \),  
   with \( \beta \) declared (default 0.5).  
5. Clamp to \([0, 1]\). Report the value, the primary root(s) used, and any noted drift.

If no reliable root record can be located after declared sources are exhausted, \( E = 0 \) and the failure is logged.

### 4. Reference / Classical Anchor
- Historical linguistics and etymological methodology.  
- Technical terminology standardization practices (ISO, scientific first-use citation norms).  
- Ontology design and controlled-vocabulary principles (is-a / part-of hierarchies).  
- Semantic-change literature (widening, narrowing, amelioration, pejoration) as used in classical lexicography.

### 5. Failure Modes & Edge Cases
- No recoverable root or prior technical sense → \( E = 0 \).  
- Root exists but current usage has undergone unacknowledged radical drift → alignment collapses, \( E \) low.  
- Multiple competing etymologies of equal standing → report the range or take the most conservative (lowest) aligned value.  
- Purely stipulative or private coinage with no public lineage → \( E = 0 \).  
- Proper names or arbitrary labels → ordinarily \( E = 0 \) unless a documented technical or historical sense applies.

### 6. Relation Rules
- \( E \) is independent of \( G \) at definition time; a term may be deeply rooted yet support only narrow associations, or vice versa.  
- In the parallel differential form, \( E \) multiplies both trajectories: weak etymological grounding reduces the force of both actionable claim generation and paradox containment.  
- \( E \) may later be correlated with classical measures of term stability or with residual stability in continuous process models, but such correlations remain empirical.  
- Material with high \( S \) and near-zero \( E \) is flagged as “clear but unrooted” — usable for local precision work, fragile for long-term or cross-system examination.

---

*Locked under the six-clause meta-standard. Ready for embodiment.*
