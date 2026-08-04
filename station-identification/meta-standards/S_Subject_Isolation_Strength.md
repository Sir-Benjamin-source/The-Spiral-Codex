# S — Subject Isolation Strength

**Six-Clause Meta-Standard Entry**  
**Version**: 0.1 (Locked 2026-08-04)  
**Status**: Accepted for use in the parallel differential examination form

---

### 1. Name & Symbol
Subject Isolation Strength — \( S \)  
Range: \([0, 1]\), where 1 = maximal isolation of a single, clear central claim.

### 2. Operational Definition
\( S \) quantifies how cleanly a given text or feature set concentrates its meaning onto one identifiable subject (claim, hypothesis, or target variable) rather than dispersing across multiple competing subjects. High \( S \) means a competent reader or algorithm can point to a single primary subject with high confidence; low \( S \) means the material is multi-focal, ambiguous, or subjectless.

### 3. Measurement Protocol
Given a candidate text \( T \) (or feature set \( F \)):

1. Extract the set of candidate subjects (claims, entities, or target variables) by any of the following classical methods (in order of preference when available):
   - Explicit claim markers or thesis statements
   - Named-entity or coreference chains with highest centrality
   - Topic-model or embedding cluster of highest average pairwise similarity to the rest of the document
2. Compute a concentration score:
   - Let \( p_i \) be the normalized weight (token mass, embedding centrality, or mutual-information share) of candidate subject \( i \).
   - \( S = \max_i p_i \) (simple concentration), or
   - \( S = 1 - H(p)/\log k \) where \( H \) is the entropy of the subject-weight distribution and \( k \) is the number of candidates (normalized entropy complement).
3. Clamp to \([0, 1]\).
4. Report both the numerical value and the identity of the dominant subject.

The protocol must be runnable by an independent agent given only \( T \) (or \( F \)) and a declared extraction method.

### 4. Reference / Classical Anchor
- Information-theoretic concentration / normalized entropy (standard in topic modelling and feature selection literature).
- Claim identification and argument mining (Stab & Gurevych, Lippi & Torroni, etc.).
- Centrality measures in dependency or semantic graphs (as used in classical summarization and keyphrase extraction).
- Mutual-information based feature relevance (Guyon & Elisseeff, *JMLR* 2003) when \( S \) is applied to a tabular feature set rather than free text.

### 5. Failure Modes & Edge Cases
- No identifiable subject → \( S = 0 \).
- Multiple subjects of equal weight → \( S \) approaches \( 1/k \) or low entropy-complement values.
- Pure noise or empty input → \( S = 0 \).
- Contested or shifting subject mid-text → report both global \( S \) and a local sliding-window series if the protocol is extended.

### 6. Relation Rules
- \( S \) is a required input to both trajectories of the parallel differential form.
- In spiral-head-to-head, \( S \) may be correlated with classical feature-importance concentration or with the clarity of the prediction target.
- \( S \) may be used as a pre-filter: material below a declared threshold (e.g., \( S < 0.4 \)) is flagged as insufficiently isolated for further examination.
- \( S \) is independent of \( G \), \( E \), and \( C \) at definition time; any observed correlations are empirical, not definitional.

---

*Locked under the six-clause meta-standard. Ready for embodiment.*
