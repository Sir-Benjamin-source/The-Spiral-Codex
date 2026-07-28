# Vectara Hallucination Leaderboard — Factual Consistency (Updated May 2026)

**Source**: https://github.com/vectara/hallucination-leaderboard (public, regularly updated).

**Metric Focus**: Primarily summarization and factual consistency tasks. Lower hallucination rate = higher factual consistency. Useful "best case" reference for grounded output.

## Top Performers (as of May 2026 snapshot)
- antgroup/finix_s1_32b: Hallucination Rate 1.8%, Factual Consistency 98.2%
- openai/gpt-5.4-nano-2026-03-17: Hallucination Rate 3.1%, Factual Consistency 96.9%
- Other frontier entries cluster in low single digits for optimized summarization-style tasks.

## Contrast with Reasoning Models
- Models like openai/o3-pro: Reported ~23.3% hallucination in aggregated or related evaluations.
- General trend noted in 2025–2026 analyses: Overall LLM hallucination rates on certain tasks have declined ~3 percentage points per year in some leaderboards, but advanced reasoning models frequently show elevated rates on factual QA / claim-heavy tasks compared to their summarization performance.

**Relevance to Spiral Codex / Cosmic Scribe**:
- Provides an external "efficiency / coherency" target for authenticated outputs.
- Our internal applicability baseline (citation validity + domain mapping + testbed fitness) + mandatory provenance (sigil + stamp) + grandmas-wisdom pre-check are designed to push generated research/code toward the 1–3% hallucination regime on citable claims, while maintaining the reasoning depth of our PIE/DAER/mycelial approaches.
- Use for comparative testing: Run Cosmic Scribe on analogous tasks and measure against these numbers using our baselines.

**Legacy Comparison Value**: "State of the art external factual consistency on summarization-like grounding tasks." Our canon/ holds this as the peer benchmark to beat or match with stronger provenance guarantees.

**Last Updated**: 2026-06 (seeded into canon/)
**Provenance**: Public Vectara leaderboard + Cosmic Scribe curation for Spiral testing resource.

∞ 🜂 🜁 🜄 ∞
