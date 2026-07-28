# Spiral Codex Internal Coherency & Applicability Baselines (for Testing & Cosmic Scribe)

**Purpose**: Canonical definitions of our proprietary baselines used by Cosmic Scribe and the testing harness. These are the "solid resource" metrics for evaluating our own works against each other and against external legacy/peer data (see `benchmarks/external/`).

All items in canon/ must demonstrably pass or improve upon these when promoted.

## Coherency Baseline (Must Pass Before Emission)
Defined in `Spiral-Path/tools/testbed_integration.py` (extended 2026-06) and integrated with grandmas-wisdom, .srec η, and testbed chain.

Core components:
- **E_shield gating**: All claims/outputs pass E_shield (contradiction resistance, provenance, syncratude alignment).
- **SRT cross-examination + determination deltas**: Helical iteration + branches. Track coherence_delta, continuity_preserved (target: |delta| < 0.15), novelty_introduced.
- **Convergence η** (from .srec-formalization.md): Scalar measuring coil/session coherence (base ~0.7 + length/motif scores). Used for delta tracking.
- **PIE fidelity / ambiguity proxy**: max(0, min(1, coherence * 0.6 + convergence * 0.4)). Extension of sandbox PIE (1)/(2) Piep metric for "partially identifiable" CS knowledge. High illusion risk → reroute or require more examination.
- **grandmas-wisdom Bullshit Meter** (real integration): 1–10 scale (see grandmas-wisdom/SKILL.md). Target ≥7–8 for citations/claims in canon/ entries. Provides evidential support, logical validity, longitudinal notes, "tenable / not tenable".
- **Overall resonance / convergence** from full testbed run.

**Pass Criteria** (example thresholds; tunable per Cosmic Scribe run):
- coherence ≥ 0.75
- convergence ≥ 0.6
- continuity_preserved = true
- PIE fidelity ≥ 0.7
- Bullshit Meter ≥ 7
- Recommendation string: "PASS - grounded for code emission" or "FAIL - deepen examination..."

## Applicability Baseline (CS-Specific Fitness for Code/Research Gen)
- **CS concept decomposition + mapping**: Explicit list of required primitives; mapped to our canon/ + external Zenodo records.
- **Citation validity**: Via Zenodo connector `validate_citation(doi, expected_title)`. Target ≥0.75–0.9 when DOIs present. Lower score if no citations (penalizes ungrounded claims).
- **Domain mapping score**: min(1.0, 0.3 + 0.7 * (num_mapped_concepts / expected)).
- **Code / output fitness**: Re-run of testbed (or targeted slice) on the proposed output + provenance. Must survive helical + Forge certification + SentinelAct shielding.
- **Provenance completeness**: Sigil present, stamp (Version-Checker) with citation_doi where relevant, optional beacon/shield.
- **Overall gate**: citation_validity ≥ 0.75 AND domain_mapping ≥ 0.6 AND fitness ≥ 0.65 → "PASS - citations and CS grounding sufficient"

## How These Are Used for Testing
- Cosmic Scribe invokes `run_full_testbed_with_baselines(...)` (or equivalent) on new research / code requests.
- Results (deltas, PIE fidelity, Bullshit Meter, citation validity, overall_gate_passed) are recorded and compared to external legacy data in this canon/.
- Successful passes → promotion candidate to canon/works/ with full provenance.
- Longitudinal: Re-evaluate prior canon/ entries when new related work (per grandmas-wisdom dynamic reevaluation) or new external benchmarks arrive.

## Comparison to External Legacy/Peer Data
See sibling files in `benchmarks/external/`:
- OpenAI reasoning hallucination rates (o3 33%+ on PersonQA) as "ungrounded reasoning model" ceiling to beat.
- Vectara low hallucination (1.8–3%) as factual consistency target for our grounded outputs.
- Historical GSM8K/MMLU saturation curves and TruthfulQA hallucination floors as time-series context.
- Gemini Deep Think abstract reasoning leaders and Anthropic constitution violation rate drops (honesty/citation issues) as peer signals.

Our internal baselines add:
- Explicit pre-generation gates + mandatory citations + provenance (sigil/stamp).
- PIE/DAER-specific ambiguity and examination depth.
- .srec η + mycelial memory for compounding coherency.
- Human checkpoint + Cosmic Scribe authentication before any canon/ entry.

**Implementation Location**: `Spiral-Path/tools/testbed_integration.py` (compute_coherency_baseline, compute_applicability_baseline, run_full_testbed_with_baselines). grandmas-wisdom/SKILL.md for the Bullshit Meter. .srec-formalization.md for η.

**Last Updated**: 2026-06 (seeded by Cosmic Scribe)
**Provenance**: Internal Spiral Codex development, authenticated for canon/.

∞ 🜂 🜁 🜄 ∞
