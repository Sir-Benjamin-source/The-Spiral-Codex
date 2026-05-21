---
name: grandmas-wisdom
description: "An authentication framework for AI-assisted academic citation and reasoning. Evaluates citations using evidential support from related works, logical validity, and dynamic longitudinal validation. Produces actionable Bullshit Meter scores (1-10) with clear guidance on what is tenable."
version: 0.1
authors: Sir Benjamin & Grok
license: MIT + Spiral Mark
---

# Grandma’s Wisdom

**Primary Function**: Authenticate citations and claims for academic use by AI agents and human researchers, with emphasis on evidential substance over institutional prestige.

## Trigger Phrases

- "Use Grandma’s Wisdom"
- "Authenticate this citation"
- "Run Grandma’s Wisdom on [claim/citation]"
- "Evaluate this source with Grandma’s Wisdom"
- "Bullshit meter this"

## Core Capabilities

Grandma’s Wisdom provides structured authentication of academic citations and claims through a multi-pass helical process. It returns:

- A **Bullshit Meter** score (1–10) with actionable interpretation
- A structured breakdown of evidential support, logical consistency, contextual fidelity, provenance, and overclaim risk
- Explicit statements of what is **tenable** and what is **not tenable**
- Optional probability estimates on key sub-claims (when contextual foundation is sufficient)
- Support for **longitudinal reevaluation** as new related work appears

## Input

The skill accepts one of the following:

1. A citation string + the claim it is being used to support (recommended)
2. A citation string alone
3. A claim + source material (text excerpt or reference)

Example input:
```
Citation: "Long-term effects of X on cognitive flexibility in adults," Journal of Cognitive Science, 2023.
Claim being supported: "X causes lasting improvements in executive function across the general adult population."
```

## Output

Returns a structured diagnostic record containing:

- **Bullshit Meter** score (1–10)
- **Breakdown** with sub-scores
- **Tenable** / **Not tenable** statements
- **Recommended action** for an agent or researcher
- **Metadata** (provenance status, reevaluation eligibility, linked related works via Linkweaver)

The output is designed to be directly usable by other agents without requiring human interpretation.

## Bullshit Meter Scale (Actionable)

**1–2: Strong**  
Well-supported by related work. Minimal qualification needed.

**3–4: Solid with Minor Caveats**  
Core claims reasonably supported. Light qualification advised.

**5: Usable with Moderate Qualification**  
Significant gaps exist. Use only with clear caveats.

**6–7: Weak Foundation**  
Substantial problems with evidential support or fit. Strong caveats required; better sources recommended.

**8–9: High Risk**  
Significant misrepresentation, weak support, or overclaiming. Generally avoid or heavily revise.

**10: Not Tenable**  
Unsupported, contradictory, or fabricated. Do not use.

Full detailed descriptions and sub-score definitions are maintained in `architecture/bullshit-meter.md`.

## Integration Points

- Uses **Spiral Reasoning Tree (eml-enhanced)** for resonance and consistency evaluation
- Leverages **MAGIC** rectification logic for structured analysis
- Applies **Veritas Aegis** safeguards for objective grounding
- Uses **Version Checker** for provenance tracking
- Uses **Linkweaver** for mapping checked vs. unchecked conceptual connections and detecting longitudinal validation

## Dynamic Reevaluation

Grandma’s Wisdom supports reevaluation of previous assessments when new related work enters the network. Agents may request reevaluation of specific citations using Linkweaver-detected conceptual connections.

## Notes for Agents

- Always prioritize **evidential support from related works** over author/institutional prestige.
- Clearly distinguish between what the source itself supports and what is being inferred from it.
- When probability estimates are provided, they are only generated when sufficient contextual foundation exists.
- The framework is designed to improve over time as the surrounding literature develops.

## Related Documentation

- `architecture/overview.md`
- `architecture/bullshit-meter.md`
- `architecture/dynamic-reevaluation.md`
- White paper: https://zenodo.org/records/20330172

---

*Part of the Spiral Codex ecosystem.*