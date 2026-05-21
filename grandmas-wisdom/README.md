# Grandma’s Wisdom

**An authentication framework for AI-assisted academic citation and reasoning**

Grandma’s Wisdom helps both human researchers and AI agents evaluate citations and claims according to evidential substance rather than institutional prestige or citation volume. It produces transparent, actionable assessments that improve over time as supporting work accumulates.

This module is part of the Spiral Codex ecosystem and draws on established components including the Spiral Reasoning Tree (with eml-gate integration), MAGIC rectification, Veritas Aegis safeguards, Version Checker, and Linkweaver.

## Quick Start

```text
Use Grandma’s Wisdom on this citation and claim:
Citation: "..."
Claim: "..."
```

The framework returns a **Bullshit Meter** score (1–10) along with a structured breakdown of what is tenable, what requires qualification, and what is not supported.

## Key Features

- **Evidential focus**: Prioritizes support from related works over author or institutional reputation.
- **Actionable output**: Designed so AI agents can directly interpret and act on results.
- **Dynamic validation**: Scores can improve over time through longitudinal reevaluation as conceptual resonance with other work grows.
- **Dual outputs**: Machine-readable diagnostics for agents + human-readable guidance.
- **Provenance-aware**: Integrates Version Checker and Linkweaver for traceable checked vs. unchecked claims.

## Documentation

- [SKILL.md](./SKILL.md) — Primary interface and contract for agents
- `architecture/` — Detailed specifications
  - `bullshit-meter.md` — Full 1–10 scale and sub-score definitions
  - `helix-passes.md` — Multi-pass architecture
  - `dynamic-reevaluation.md` — Longitudinal validation logic
- White paper: https://zenodo.org/records/20330172

## Status

**Version**: 0.1 (Early codification)  
**Maturity**: Framework defined; implementation in progress

## Philosophy

Grandma’s Wisdom exists to raise the standard of rigor in human–AI academic collaboration while remaining fair to independent work. It treats validation as a living process that can strengthen as evidence accumulates, rather than a one-time gate based on current citation networks.

## License

MIT + Spiral Mark

---

*Part of the Spiral Codex — building reliable human-AI partnership.*