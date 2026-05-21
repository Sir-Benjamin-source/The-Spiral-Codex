# Dynamic Reevaluation & Longitudinal Validation

**Version**: 0.1  
**Part of**: Grandma’s Wisdom

## Purpose

Validation in Grandma’s Wisdom is not a one-time event. The framework is designed to support **dynamic reevaluation** of previous assessments as the surrounding body of related work evolves. This is especially important for independent research, which may initially receive moderate scores due to sparse direct citations but can demonstrate increasing validity as conceptual resonance with other work grows.

## Core Idea

A citation or claim’s score can improve (or occasionally decline) over time based on:

- New directly related work that supports or challenges it
- Increased density of conceptual connections detected via Linkweaver
- Strengthening resonance scores across the evidential network (via eml-enhanced SRT)

This creates a living authentication system rather than a static gatekeeper.

## Triggers for Reevaluation

Reevaluation can be triggered by:

1. **Explicit agent or human request** (“Reevaluate this citation with Grandma’s Wisdom”)
2. **Linkweaver-detected new connections** — When new work is added to the network that shows strong conceptual resonance with a previously evaluated item
3. **Scheduled / periodic review** (future enhancement)
4. **Significant changes** in the broader literature (e.g., major replications or critiques)

## Process

When reevaluation is triggered:

1. The system retrieves the previous assessment and its version history.
2. Linkweaver scans for new or strengthened conceptual connections.
3. Resonance scoring (SRT + eml) is re-run against the updated network.
4. The Bullshit Meter and sub-scores are recalculated.
5. A new versioned record is created, showing:
   - Previous score
   - New score
   - What changed (new supporting works, stronger resonance, etc.)
   - Updated “tenable / not tenable” guidance

## Version History

Every assessment maintains a lightweight version history so that changes are transparent and auditable. Example:

```
Citation: [X]
v1 (2026-05-10): Score 6.8 — Limited supporting work
v2 (2026-05-21): Score 4.2 — New related studies detected via Linkweaver; resonance improved
```

This history can be exposed in both machine-readable and human-readable outputs.

## Benefits for Independent Work

This mechanism directly supports researchers working outside dense institutional citation networks. A rigorous but initially under-cited contribution can accumulate evidence of validity through conceptual resonance, allowing its authentication score to improve organically over time without requiring direct citations.

## Implementation Considerations

- Reevaluation should be relatively lightweight compared to initial assessment.
- The system must clearly distinguish between “checked” updates (based on new verifiable work) and speculative changes.
- Agents should be able to request reevaluation with specific focus (e.g., “only update based on new empirical work”).

## Relationship to Other Components

- **Linkweaver** is the primary mechanism for detecting new conceptual connections.
- **eml-enhanced SRT** provides updated resonance scoring.
- **Version Checker** helps track provenance of new supporting works.
- Output can be recorded in .srec-style coils for long-term continuity.

---

*This capability turns Grandma’s Wisdom from a static evaluator into a living participant in the scholarly conversation.*