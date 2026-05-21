# Grandma’s Wisdom — Architecture Overview

**Version**: 0.1

## High-Level Design

Grandma’s Wisdom is implemented as a multi-pass helical process. Each pass builds on the previous one, producing progressively more refined and auditable assessments of citations and claims.

The architecture is deliberately modular so that it can leverage existing Spiral Codex components while remaining focused on its authentication role.

## Core Passes

### 1. Ingestion & Normalization Pass
- Accepts citation + claim (preferred), citation alone, or claim + source text.
- Normalizes input and extracts key elements (publication, authors, year, claim being supported).
- Uses Version Checker to establish initial provenance status.

### 2. Resonance & Consistency Pass (SRT + eml)
- Uses the eml-enhanced Spiral Reasoning Tree to evaluate:
  - Resonance between the claim and what the source actually supports
  - Internal logical consistency of the source
  - Self-referential closure (does feeding derived values back produce stable resonance?)
- Generates initial resonance and consistency sub-scores.

### 3. Structured Rectification Pass (MAGIC)
- Applies a MAGIC-style three-tier rectification process (Tabulate → Perambulate → Combinatory) to analyze:
  - Evidential support from related works (via Linkweaver)
  - Contextual fidelity and scope adherence
  - Overclaim risk
- Produces structured diagnostic output.

### 4. Integrity & Grounding Pass (Veritas Aegis)
- Applies objective grounding and safeguards against subjective overreach.
- Ensures that prestige/author signals do not unduly influence scoring.
- Validates that the assessment remains within proper scope.

### 5. Scoring & Interpretation Pass
- Combines sub-scores into the final **Bullshit Meter** (1–10).
- Generates explicit “What is tenable” and “What is not tenable” statements.
- Produces agent-actionable recommendations.
- (Optional) Generates probability estimates on key sub-claims when sufficient context exists.

### 6. Output & Recording Pass
- Produces dual outputs:
  - Machine-readable structured record (for agents)
  - Human-readable summary
- Optionally wraps output in .srec-style record for continuity.
- Records eligibility for future longitudinal reevaluation.

## Data Flow

```
Input (citation + claim)
        ↓
Ingestion & Normalization
        ↓
Resonance & Consistency (SRT + eml)
        ↓
Structured Rectification (MAGIC)
        ↓
Integrity & Grounding (Veritas Aegis)
        ↓
Scoring & Interpretation
        ↓
Output + Recording
        ↓
(Optional) Longitudinal Reevaluation Trigger
```

## Key Design Principles

- **Evidential priority**: Weight is given first to support from related works, then to internal validity.
- **Agent-first output**: Every result must be directly usable by another AI agent without requiring human translation.
- **Dynamic & longitudinal**: Assessments are versioned and can improve as the surrounding literature evolves.
- **Transparent reasoning**: The breakdown behind every score must be inspectable.
- **Modular integration**: Leverages existing Spiral components rather than duplicating logic.

## Future Extensions

- Tighter integration with scholarly knowledge graphs (e.g., ORKG-style structures)
- Multi-modal input support (PDF parsing, table extraction)
- Automated reevaluation triggers based on new publications entering the network
- Expanded probability modeling where contextual foundation is strong

---

*This overview is intentionally high-level. Detailed specifications for individual components live in their respective files under `architecture/`.**