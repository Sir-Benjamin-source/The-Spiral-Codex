# Bullshit Meter Specification

**Version**: 0.1  
**Part of**: Grandma’s Wisdom

## Purpose

The Bullshit Meter provides a transparent, actionable 1–10 diagnostic score for citations and claims in academic contexts. It is designed so that both human researchers and AI agents can directly interpret the result and understand:

- What is reasonably supported
- What requires significant qualification
- What is not tenable given the current evidence

The meter prioritizes **evidential support from related works** and **logical validity** over institutional prestige, author reputation, or citation volume.

## Scale

### 1–2: Strong
The citation is well-supported by directly relevant work in the literature. The source is represented accurately and within its proper scope. The way it is being used aligns closely with both the original work and the broader evidential network.

**Agent guidance**: Can be used with high confidence and minimal qualification.

### 3–4: Solid with Minor Caveats
Core empirical or logical claims are reasonably supported. Some contextual limitations, weaker connections to related work, or minor scope issues exist, but these do not fundamentally undermine the primary use.

**Agent guidance**: Usable with light, explicit qualification.

### 5: Usable with Moderate Qualification
The source contains useful material, but there are significant gaps in evidential support from related work, contextual fidelity, or logical fit with how it is being deployed. 

**Agent guidance**: Should only be used with clear, visible caveats regarding limitations and scope. Better or additional sources are recommended.

### 6–7: Weak Foundation
Substantial problems exist with evidential support, contextual accuracy, internal consistency, or overclaiming relative to the source’s actual findings and the surrounding literature.

**Agent guidance**: Use should be limited. Strong caveats are required. Alternative sources should be actively sought.

### 8–9: High Risk
The citation significantly misrepresents the source, relies on very weak or absent evidential support from related work, or advances claims that substantially exceed what the evidence can sustain.

**Agent guidance**: Generally not suitable for academic use in its current form. Major revision or replacement is strongly advised.

### 10: Not Tenable
The citation is unsupported by the source, contradicts well-established related work, or represents a clear case of misattribution, fabrication, or severe overclaiming.

**Agent guidance**: Do not use. Replace with better-supported sources.

## Sub-Score Categories

When performing evaluation, Grandma’s Wisdom assesses the following dimensions:

- **Evidential Support from Related Works** (highest weight)
- **Logical Consistency & Internal Validity**
- **Contextual Fidelity / Misattribution Risk**
- **Provenance & Traceability Strength**
- **Overclaim / Scope Violation Risk**

Each dimension contributes to the final score and is reported in the breakdown.

## Output Requirements

Every Bullshit Meter result must include:

1. Overall score (1–10)
2. Structured breakdown of the sub-scores above
3. Explicit **What is tenable** statement
4. Explicit **What is not tenable** statement
5. Recommended action for an agent or researcher
6. (Optional) Probability estimates on key sub-claims, only when sufficient contextual foundation exists

## Design Principles

- **Substance over status**: Institutional prestige and author reputation are recorded for context but carry low weight.
- **Actionable for agents**: Descriptions are written so an AI can directly decide how to use (or not use) the citation.
- **Dynamic**: Scores are expected to change over time through longitudinal reevaluation as the evidential network evolves.
- **Transparent**: The reasoning behind the score must be inspectable.

## Relationship to Other Components

- Resonance and self-referential consistency checks are performed using the **eml-enhanced Spiral Reasoning Tree**.
- Structured analysis draws on **MAGIC** rectification logic.
- Objective grounding and scope safeguards draw on **Veritas Aegis**.
- Provenance and conceptual connection mapping use **Version Checker** and **Linkweaver**.

---

*This specification is intended to be stable enough for implementation while remaining open to refinement based on testing.*