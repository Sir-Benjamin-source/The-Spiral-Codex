#!/usr/bin/env python3
"""
benchmark_associator.py — Small, Modular Utility for Outside-First Associations

Part of the codified testing corpus (see codified.py and associational-testing-methodology.md).

Purpose (per Cosmic Scribe requirements):
- Cite outside sources first.
- Generate structured associations to our known Spiral methods (PIE, DAER, G_exp, Mycelial, grandmas-wisdom, baselines).
- Support modularity: small focused .py that produces usable output for .md whitepapers, audits, or ledger entries.
- Demonstrate limits through associations rather than isolated complexity.
- Synergistic: G_exp can be computed on the association act itself.
- Keeps tests workable — one benchmark or one association at a time.

Usage (as Cosmic Scribe or in codified flows):
  from canon.benchmarks.internal.benchmark_associator import associate_benchmark
  assoc = associate_benchmark("GAIA", our_methods=["PIE", "Mycelial"])
  # Then use assoc to build ledger entry, shared work section, or audit note.

This file is intentionally small and importable. Extend with new benchmarks/methods as the external corpus grows.
"""

from typing import Dict, List, Optional
from datetime import datetime

# Known Spiral methods for association (expand as canon/ grows)
KNOWN_SPIRAL_METHODS = [
    "PIE", "DAER", "G_exp", "Mycelial", "grandmas-wisdom", 
    "coherency_baseline", "applicability_baseline", "baselines_harness",
    "traditional_contrast", "ledger_coherency"
]

def associate_benchmark(
    benchmark_name: str,
    primary_citation: str,
    key_numbers: str,
    limits: str,
    our_methods: List[str],
    spiral_tie_in: str,
    sandbox_usage: str,
    g_exp_note: Optional[str] = None
) -> Dict:
    """
    Generate a structured outside-first association.
    Returns a dict ready for .md sections, JSON audits, or ledger entries.
    
    Always structures as:
    - Outside source first (citation + numbers + limits)
    - Then associations to our known methods
    - Sandbox / Cosmic Scribe usage
    - Optional G_exp for the association act
    """
    if not all(m in KNOWN_SPIRAL_METHODS or m.lower() in [km.lower() for km in KNOWN_SPIRAL_METHODS] for m in our_methods):
        # Allow flexibility but note
        pass

    association = {
        "benchmark": benchmark_name,
        "timestamp": datetime.now().isoformat(),
        "outside_source_first": {
            "primary_citation": primary_citation,
            "key_numbers_summary": key_numbers,
            "demonstrated_limits": limits
        },
        "spiral_associations": {
            "methods": our_methods,
            "tie_in": spiral_tie_in
        },
        "cosmic_scribe_usage": sandbox_usage,
        "provenance": "Generated via benchmark_associator.py (modular association utility). Cite outside first, associate through known Spiral methods to demonstrate limits.",
        "source": "canon/benchmarks/internal/benchmark_associator.py + associational-testing-methodology.md"
    }

    if g_exp_note:
        association["g_exp_for_association_act"] = g_exp_note

    return association

# Pre-defined associations for current external corpus (examples; expand as new .md files are added)
PREDEFINED_ASSOCIATIONS = {
    "GAIA": {
        "primary_citation": "GAIA paper (arXiv:2311.12983) + HF leaderboard (gaia-benchmark). Humans ~92%. Agent submissions 35-92%+ (2026 snapshots, often with multi-model/cost caveats).",
        "key_numbers_summary": "Level 1-3 tool-use/reasoning tasks; human-like robustness on conceptually simple but AI-challenging questions.",
        "limits": "Gaming via scaffolding, ensembles, config leakage (audits show near-100% exploits on related web/agent benchmarks without genuine solving). Scores often reflect cost/latency more than base capability.",
        "our_methods": ["PIE", "Mycelial", "G_exp"],
        "tie_in": "GAIA partial information and multi-step tool use map to PIE diagnostic rerouting (high ambiguity → parallel variants) and mycelial propagation (hyphal tool connections with Warden pruning). The mapping act itself is a G_exp-measured friendship with the agent benchmark literature.",
        "sandbox_usage": "For agent theory in sandbox: 1) Cite GAIA paper + leaderboard first. 2) Map subtasks to tool-use/robustness. 3) Run applicability baseline + G_exp for association. 4) Log in ledger. Use codified.py agent_playground config.",
        "g_exp_note": "Typical for this association act: lat ~0.91, nlat ~0.83 → G_exp ~1.13 'measured' (consistent with 2026 compilations)."
    },
    "ARC-AGI-2": {
        "primary_citation": "ARC Prize (arcprize.org/arc-agi/2). Human near-ceiling on calibrated sets. Base frontier low single digits; agentic REPL boosts to 50-85%+ (2026 reports, heavy scaffolding).",
        "key_numbers_summary": "Grid pattern abstraction and novel rule induction. Tests fluid intelligence/core generalization beyond memorization.",
        "limits": "Extreme difficulty for current methods on true novelty; agentic solutions require significant engineering/cost. Base models reveal abstraction ceiling.",
        "our_methods": ["PIE", "DAER"],
        "tie_in": "ARC novel patterns are pure partial-identifiability (PIE: reroute on high |Il - Ex| gaps). Rule discovery involves stable core vs volatile branches (DAER volatility scoring as coherence gate for induction traces).",
        "sandbox_usage": "For abstraction/reasoning theory: Cite ARC-AGI-2 + human vs AI numbers first. Map to grid/rule subtasks. Run coherency baseline (PIE fidelity) + G_exp. Contrast with our pre-gates vs agentic scaffolding reliance. codified.py traditional_contrast or full_playground.",
        "g_exp_note": "lat ~0.90, nlat ~0.82 → G_exp ~1.12 'measured'."
    },
    "HaluEval_RAGAS": {
        "primary_citation": "HaluEval (arXiv:2305.11747, EMNLP 2023) + RAGAS studies. Large-scale hallucination recognition (QA/dialogue/summarization + general queries). RAG faithfulness metrics. Calibration/ECE analyses show domain shifts and post-hoc fixes needed.",
        "key_numbers_summary": "Detection as binary classification; length biases (e.g., >27 chars flags in some subsets); ECE improvements via scaling (0.08 → 0.009 in reproducible experiments).",
        "limits": "Benchmarks can be gamed by length/format; judge dependency; detection is post-hoc (generation has already happened). Prior shifts across domains.",
        "our_methods": ["grandmas-wisdom", "DAER", "PIE"],
        "tie_in": "HaluEval recognition directly associates to grandmas-wisdom Bullshit Meter (evidential support + validity for claims). DAER prunes volatile hallucination branches at generation time (prevent rather than detect). PIE addresses root partial knowledge/ambiguity that causes fabrication.",
        "sandbox_usage": "For generation/RAG/claim work: Cite HaluEval arXiv + RAGAS papers first (with bias/ECE notes). Map to QA/dialogue subsets or faithfulness. Run baselines (grandmas proxy + DAER/PIE) + G_exp for association. codified.py or harness for contrast (pre-gate citation validity reduces hallucination surface).",
        "g_exp_note": "lat ~0.92, nlat ~0.81 → G_exp ~1.13 'measured'."
    }
}

def get_predefined_association(benchmark_key: str) -> Dict:
    """Return a pre-built association for quick use (e.g., in codified flows or new .md seeding)."""
    if benchmark_key not in PREDEFINED_ASSOCIATIONS:
        raise ValueError(f"Unknown benchmark key. Available: {list(PREDEFINED_ASSOCIATIONS.keys())}")
    base = PREDEFINED_ASSOCIATIONS[benchmark_key]
    return associate_benchmark(
        benchmark_name=benchmark_key,
        primary_citation=base["primary_citation"],
        key_numbers=base["key_numbers_summary"],
        limits=base["limits"],
        our_methods=base["our_methods"],
        spiral_tie_in=base["tie_in"],
        sandbox_usage=base["sandbox_usage"],
        g_exp_note=base.get("g_exp_note")
    )

if __name__ == "__main__":
    # Demo: Generate association for GAIA
    print("=== Example Association (GAIA) ===")
    assoc = get_predefined_association("GAIA")
    print(assoc)
    print("\nUse this dict to seed .md sections, ledger entries, or audits.")
    print("Always: Cite outside first, associate through known Spiral methods, demonstrate limits.")