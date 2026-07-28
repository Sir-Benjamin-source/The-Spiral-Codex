# OpenAI Reasoning Models — Hallucination and Coherence Metrics (2025 Data)

**Source**: OpenAI o3 and o4-mini System Card (April 2025), public reporting (TechCrunch, analyses), Vectara Hallucination Leaderboard updates (through 2026).

**Key Context**: Reasoning models (o-series) often exhibit *higher* hallucination rates on factual/coherence tasks than non-reasoning predecessors because they generate more claims/assertions overall (both accurate and inaccurate). This is a noted trade-off.

## PersonQA (In-house factual knowledge about people)
- o3: Hallucination rate 33%, Accuracy 59%
- o4-mini: Hallucination rate 48%, Accuracy 36%
- o1 (prior): Hallucination rate 16%, Accuracy 47%

## SimpleQA
- o3: Hallucination rate 51%, Accuracy 49%
- o4-mini: Hallucination rate 79%, Accuracy 20%
- o1: Hallucination rate 44%, Accuracy 47%

## Broader Notes from System Card and Analyses
- o3 tends to make more claims → both more correct claims *and* more hallucinations.
- Comparison to non-reasoning models (e.g., GPT-4o): Reasoning variants can underperform on pure factuality despite gains in complex reasoning/math.
- Vectara-style summarization/factual consistency (separate leaderboard, May 2026 update): Top models achieve very low rates (1.8%–3.1% hallucination on certain summarization tasks). Frontier reasoning models like o3-pro reported around 23.3% in some aggregated views.

**Relevance to Spiral Codex / Cosmic Scribe**:
- Highlights the need for *pre-generation grounding gates* (our grandmas-wisdom + Zenodo citation validation + PIE ambiguity handling + explicit baselines) rather than relying on post-hoc faithfulness.
- Our canon/ and Cosmic Scribe aim to produce outputs with citation validity and provenance that target the low end of these rates (e.g., best-case summarization consistency) while preserving reasoning power.

**Legacy Comparison Value**: Use as a peer baseline for "un-grounded reasoning model" hallucination on factual tasks. Target: Cosmic Scribe outputs should demonstrably beat these on citation-backed claims (measured via our applicability baseline + re-testbed runs).

**Last Updated**: 2026-06 (compiled for canon/ seeding)
**Provenance**: Public sources + Cosmic Scribe authentication. Linked to master Codex DOI where applicable.

∞ 🜂 🜁 🜄 ∞
