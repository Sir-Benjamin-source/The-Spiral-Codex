# G — Generality Expansion

**Six-Clause Meta-Standard Entry**  
**Version**: 0.1 (Locked 2026-08-04)  
**Status**: Accepted for use in the parallel differential examination form

---

### 1. Name & Symbol
Generality Expansion — \( G \)  
Range: \([0, 1]\), where 1 = maximal coherent expansion of associations around the isolated subject.

### 2. Operational Definition
\( G \) quantifies the breadth and internal coherence of the associative field that can be legitimately generated from a clearly isolated subject \( S \). High \( G \) means the subject supports a rich, non-contradictory web of related concepts, implications, or features; low \( G \) means the associative field is narrow, sparse, or internally inconsistent.

### 3. Measurement Protocol
Given a text or feature set whose dominant subject has already been isolated (i.e., \( S \) has been computed and the dominant subject identified):

1. Generate or retrieve the candidate associative set \( A \) around the dominant subject using one or more of:
   - Controlled synonym / hypernym expansion (WordNet, ConceptNet, or domain ontology)
   - Embedding neighborhood (top-\( k \) nearest neighbors in a fixed embedding space)
   - Explicit relational extraction (dependency paths, knowledge-graph edges, or co-occurrence above a threshold)
2. Score internal coherence of \( A \):
   - Average pairwise similarity (cosine or other) among members of \( A \), or
   - Normalized mutual information / clustering coefficient within \( A \).
3. Score coverage / breadth:
   - Normalized size of \( A \) relative to a reference maximum, or
   - Entropy of the distribution of association types.
4. Combine:
   \( G = \alpha \cdot \text{coherence} + (1 - \alpha) \cdot \text{breadth} \),
   with \( \alpha \) declared (default 0.6 favoring coherence).
5. Clamp to \([0, 1]\) and report both the value and the associative set used.

### 4. Reference / Classical Anchor
- Classical feature-expansion and constructive induction literature.
- Semantic relatedness and lexical expansion methods (WordNet-based, embedding-based).
- Diversity + coherence metrics used in query expansion and topic modelling evaluation.
- Mutual-information and clustering quality measures from the feature-selection and unsupervised learning literature.

### 5. Failure Modes & Edge Cases
- Subject is isolated but supports almost no legitimate associations → \( G \) near 0.
- Associations are numerous but mutually contradictory or low-similarity → coherence term collapses, \( G \) low.
- Over-generation of noise associations → breadth may rise while coherence falls; the weighted combination penalizes this.
- No embedding or ontology available → fall back to explicit co-occurrence or declare \( G \) unmeasurable and halt.

### 6. Relation Rules
- \( G \) is defined only after \( S \) has been established; it is not independent of subject isolation.
- In the parallel differential form, high \( G \) feeds the actionable trajectory; low \( G \) (especially low-coherence generality) feeds the paradox-containment trajectory.
- \( G \) may be correlated post-hoc with classical measures of feature-set diversity or with residual stability in qsc-stabilization, but such correlations are empirical.
- Material with very high \( S \) and very low \( G \) is flagged as “narrow but clear” — useful for precision tasks, limited for generative examination.

---

*Locked under the six-clause meta-standard. Ready for embodiment.*
