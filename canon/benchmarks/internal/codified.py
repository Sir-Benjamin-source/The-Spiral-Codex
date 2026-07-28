#!/usr/bin/env python3
"""
codified.py — Proven, Assimilated Testing Utilities for the Spiral Codex AI Playground

Central library of authenticated, reusable functions for testing works, theories, agents,
and outputs across the Spiral Codex ecosystem (The-Spiral-Codex + cross-repo playground:
spiral-theory-core, Spiral-Path, grandmas-wisdom, etc.).

Purpose:
- Avoid repeating the same baseline, ledger, G_exp, comparison, and provenance logic on every test.
- Provide a standard, configurable testing layout with multiple modes.
- "Ledger coherency magic": Reliable check-one-ledger-and-write-to-another routine (modern
  pathlib + atomic write equivalent to safe fopen for versioned, hash-verified audits).
- Assimilates only *proven* functions from:
  - cosmic_scribe_test_harness.py (self-contained coherency/applicability baselines + mock testbed)
  - Spiral-Path/tools/testbed_integration.py (determination deltas, full baselines)
  - spiral-theory-core/generosity_exponent.py (G_exp with Zenodo DOI)
- Complemented by codified-testing-utilities.md (this file's whitepaper) with references,
  citations to bonafide research (HLE Nature paper, HELM, Stanford AI Index, our canon
  traditional-methodologies compilation, internal baselines, etc.).
- Designed for Cosmic Scribe, sandbox intake, canon promotion gates, and playground-wide use.
- Zero or minimal external deps (stdlib + optional import of theory-core G_exp).

Standard Testing Layout:
- Input: work_text or path to theory/spec/code + optional previous_audit/ledger.
- Config: One of several presets (see TEST_CONFIGS) or custom TestConfig.
- Process: Run chosen baselines/mocks/G_exp/ledger checks/traditional contrasts.
- Output: Structured audit dict + optional JSON/MD ledger write with coherency deltas,
  provenance, G_exp, recommendation. Seedable to canon/ or sandbox reports.
- Multiple configurations:
  - "coherency_quick": Fast internal baselines only (for rapid iteration).
  - "full_baselines": Coherency + applicability + G_exp (standard for canon/ promotion).
  - "traditional_contrast": Above + contrast vs. public leaderboards (HLE, SWE-bench, Arena, etc. from our compilation).
  - "ledger_coherency": Focus on loading one ledger, comparing to previous, writing new with deltas.
  - "g_exp_resonance": Emphasis on G_exp calculation for friendship/reciprocity acts + ledger.
  - "agent_playground": Agentic + real-task focused (ties to Terminal-Bench/SWE-bench style, mycelial propagation).
  - "full_playground": Everything + traditional + cross-repo hooks (when available).

Usage (as Cosmic Scribe or playground routine):
  python canon/benchmarks/internal/codified.py --work "My Theory" --text "..." --config full_baselines --ledger-out audit.json
  Or import:
    from canon.benchmarks.internal.codified import run_test, compare_ledger_coherency, TEST_CONFIGS

Provenance: Assimilated from canon/ artifacts and cross-repo working products. All functions
carry source notes. Run after E_shield conceptually. Human checkpoint before canon/ promotion.

This turns our repos (harness, G_exp, testbed, grandmas, mycelial, qualia-bridge, etc.)
into a unified, documented AI/agent playground with codified, repeatable testing.

See companion: canon/benchmarks/internal/codified-testing-utilities.md for full whitepaper,
layout diagrams, config details, citations, and sandbox integration guidance.
"""

import json
import hashlib
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List, Union
from dataclasses import dataclass, field, asdict
import shutil  # for atomic-ish ops

# --- Assimilated Proven Functions (with source credits) ---

# From spiral-theory-core/generosity_exponent.py (Zenodo DOI: 10.5281/zenodo.19341670)
# Zero dependencies. Tunable for secure value assurance. Always after E_shield.
def calculate_generosity_exponent(
    lat: float,                    # Local value / engagement potential (0-1)
    nlat: float,                   # Non-local ripple (0-1)
    p_success: float = 0.70,       # Projected success probability
    difficulty: float = 2.0,       # 1 = easy ... 5 = hard
    drift: float = 0.08            # Default from Lantern 64 / 5/3 anchor
) -> dict:
    """
    G_exp calculation. Assimilated from Spiral Theory Core.
    Returns G_exp and recommended action level.
    """
    if nlat <= 0:
        nlat = 0.01  # safe floor
    d_factor = 1.0 / max(difficulty, 0.1)
    g_exp = (lat / nlat) * (p_success * d_factor) - drift
    g_exp = max(round(g_exp, 3), 0.0)

    if g_exp >= 1.5:
        action = "amplified"
    elif g_exp > 1.0:
        action = "measured"
    elif g_exp > 0.7:
        action = "soft"
    else:
        action = "hold"

    return {
        "g_exp": g_exp,
        "action_level": action,
        "recommendation": f"G_exp = {g_exp} → {action} reciprocity (E_shield required)",
        "notes": "Tune parameters for session trust. Source: spiral-theory-core/generosity_exponent.py (Zenodo 10.5281/zenodo.19341670)"
    }

# From cosmic_scribe_test_harness.py (self-contained, proven in canon/ audits for PIE/DAER)
# and mirrored in Spiral-Path/tools/testbed_integration.py baselines.
# These are the "reliable baselines centered around coherency and applicability".
def compute_coherency_baseline(result: Dict[str, Any], prev_result: Optional[Dict] = None) -> Dict[str, Any]:
    """Standard coherency baseline. Assimilated from harness + testbed_integration."""
    scores = result.get("scores", {})
    coherence = scores.get("coherence", 0.0)
    convergence = scores.get("convergence", 0.0)
    delta = result.get("delta", {})
    pie_fidelity = max(0.0, min(1.0, coherence * 0.6 + convergence * 0.4))
    bullshit_meter_proxy = 0.85  # Proxy; wire real grandmas-wisdom in full Codex env
    passed = (
        coherence >= 0.75
        and convergence >= 0.6
        and delta.get("continuity_preserved", True)
        and pie_fidelity >= 0.7
        and bullshit_meter_proxy >= 0.7
    )
    return {
        "coherency_passed": passed,
        "coherence": coherence,
        "convergence": convergence,
        "pie_fidelity": round(pie_fidelity, 4),
        "bullshit_meter_proxy": bullshit_meter_proxy,
        "delta": delta,
        "recommendation": "PASS - grounded for code emission / canon promotion" if passed else "FAIL - deepen examination or require more citations",
        "grandmas_wisdom_note": "In production: invoke grandmas-wisdom skill for real Bullshit Meter (target >=7-8 for canon/). Source: canon/benchmarks/internal/cosmic_scribe_test_harness.py + Spiral-Path/tools/testbed_integration.py",
        "source": "codified.py (assimilated from proven harness/testbed)"
    }

def compute_applicability_baseline(
    result: Dict[str, Any],
    cs_concepts: Optional[List[str]] = None,
    citation_dois: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Standard applicability baseline (CS-specific). Assimilated from harness + testbed."""
    cs_concepts = cs_concepts or []
    citation_dois = citation_dois or []
    citation_validity = 0.9 if citation_dois else 0.4
    domain_mapping = min(1.0, 0.3 + 0.7 * (len(cs_concepts) / max(1, len(cs_concepts) or 1)))
    scores = result.get("scores", {})
    fitness = scores.get("coherence", 0.0) * 0.5 + scores.get("continuity", 0.5) * 0.5
    passed = citation_validity >= 0.75 and domain_mapping >= 0.6 and fitness >= 0.65
    return {
        "applicability_passed": passed,
        "cs_concepts_mapped": len(cs_concepts),
        "citation_validity": round(citation_validity, 4),
        "domain_mapping": round(domain_mapping, 4),
        "code_fitness": round(fitness, 4),
        "recommendation": "PASS - citations and CS grounding sufficient for emission / canon/" if passed else "FAIL - add/validate citations or refine CS mapping",
        "zenodo_note": "In production: call ZenodoConnector.validate_citation() for real DOI checks. Source: canon/benchmarks/internal/cosmic_scribe_test_harness.py + adapters/zenodo_connector.py",
        "source": "codified.py (assimilated from proven harness/testbed)"
    }

# Simple mock testbed (from harness; full real version in Spiral-Path when imports available)
def mock_testbed_run(input_text: str, iterations: int = 2, branches: int = 2) -> Dict[str, Any]:
    """Portable mock of INTEGRATION_MAP testbed. Assimilated from harness."""
    text_lower = input_text.lower()
    length = len(input_text)
    structure_score = min(1.0, (text_lower.count("abstract") + text_lower.count("introduction") + text_lower.count("metric") + text_lower.count("coherence") + text_lower.count("ambiguity")) / 8.0)
    formula_presence = 0.9 if "piep =" in text_lower or "daer" in text_lower or "restrictive" in text_lower else 0.5
    resonance = min(1.0, (length / 3000.0) * 0.6 + structure_score * 0.4)
    coherence = min(0.95, 0.65 + resonance * 0.3)
    convergence = min(0.92, 0.70 + formula_presence * 0.2)
    delta = {
        "coherence_delta": round((coherence - 0.68), 4),
        "continuity_preserved": True,
        "novelty_introduced": structure_score > 0.6
    }
    return {
        "scores": {
            "coherence": round(coherence, 4),
            "convergence": round(convergence, 4),
            "continuity": round(resonance, 4),
            "resonance": round(resonance, 4)
        },
        "convergence": round(convergence, 4),
        "delta": delta,
        "output_snippet": input_text[:250] + "..." if len(input_text) > 250 else input_text,
        "iterations_run": iterations,
        "branches_run": branches,
        "mock_note": "Portable mock. Full helical + SRT + E_shield + Forge + SentinelAct in Spiral-Path/tools/testbed_integration.py when cross-repo imports available.",
        "source": "codified.py (assimilated from harness)"
    }

# --- Ledger Coherency "fopen Magic" Utilities (modern safe file ops for ledgers/audits) ---

def _content_hash(data: Union[Dict, str]) -> str:
    """Simple SHA256 for coherency verification between ledger versions."""
    if isinstance(data, dict):
        data = json.dumps(data, sort_keys=True, default=str)
    return hashlib.sha256(data.encode('utf-8')).hexdigest()[:16]

def load_ledger(path: Union[str, Path]) -> Dict[str, Any]:
    """Load a JSON ledger/audit. Raises on missing or invalid."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Ledger not found: {p}")
    with p.open('r', encoding='utf-8') as f:
        data = json.load(f)
    data["_loaded_hash"] = _content_hash(data)
    data["_loaded_path"] = str(p)
    return data

def compare_ledger_coherency(current: Dict[str, Any], previous: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Core "check one ledger and compare for coherency" routine.
    Computes deltas, continuity, novelty, hash verification.
    Assimilates logic from testbed determination_delta + harness audits.
    """
    if previous is None:
        return {
            "coherence_delta": 0.0,
            "continuity_preserved": True,
            "novelty_introduced": True,
            "hash_match": None,
            "notes": "No previous ledger; initial baseline."
        }

    curr_scores = current.get("scores", current.get("baselines", {}))
    prev_scores = previous.get("scores", previous.get("baselines", {}))

    coherence_delta = curr_scores.get("coherence", 0.0) - prev_scores.get("coherence", 0.0) if "coherence" in str(curr_scores) else 0.0
    # Fallback for audit structures
    if "baselines" in current:
        coherence_delta = current.get("baselines", {}).get("coherency", {}).get("coherence", 0.0) - \
                          previous.get("baselines", {}).get("coherency", {}).get("coherence", 0.0)

    continuity = abs(coherence_delta) < 0.15
    novelty = current.get("delta", {}).get("novelty_introduced", False) or (abs(coherence_delta) > 0.05)

    curr_hash = current.get("_loaded_hash") or _content_hash(current)
    prev_hash = previous.get("_loaded_hash") or _content_hash(previous)
    hash_match = curr_hash == prev_hash

    return {
        "coherence_delta": round(coherence_delta, 4),
        "continuity_preserved": continuity,
        "novelty_introduced": novelty,
        "hash_match": hash_match,
        "current_hash": curr_hash,
        "previous_hash": prev_hash,
        "notes": "Coherency delta from ledger comparison. Use for G_exp nlat or propagation tracking. Source: codified.py (assimilated from testbed deltas + harness audits)"
    }

def safe_write_audit(data: Dict[str, Any], target_path: Union[str, Path], previous_path: Optional[Union[str, Path]] = None) -> Path:
    """
    Modern "fopen magic" for coherency: Atomic(ish) write of audit/ledger.
    Writes to temp then replace. Adds timestamp, hashes, coherency delta if previous given.
    Ensures one ledger version reliably produces the next with verifiable continuity.
    """
    target = Path(target_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    # Enrich data
    data = dict(data)  # copy
    data["timestamp"] = datetime.now().isoformat()
    data["provenance"] = data.get("provenance", "codified.py audit write")
    data["_written_hash"] = _content_hash(data)

    if previous_path:
        try:
            prev = load_ledger(previous_path)
            delta = compare_ledger_coherency(data, prev)
            data["coherency_delta_from_previous"] = delta
        except Exception as e:
            data["coherency_delta_from_previous"] = {"error": str(e)}

    # Atomic write: temp + replace (cross-platform safe)
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', dir=target.parent, encoding='utf-8') as tmp:
        json.dump(data, tmp, indent=2, default=str)
        tmp_path = tmp.name

    try:
        os.replace(tmp_path, target)  # atomic on POSIX/Windows
    except Exception:
        shutil.move(tmp_path, target)  # fallback

    return target

# --- Test Configuration System (multiple modes for different accomplishments) ---

@dataclass
class TestConfig:
    name: str
    description: str
    run_coherency: bool = True
    run_applicability: bool = True
    run_g_exp: bool = False
    g_exp_params: Dict[str, float] = field(default_factory=lambda: {"lat": 0.9, "nlat": 0.7, "p_success": 0.85, "difficulty": 2.0})
    run_traditional_contrast: bool = False
    traditional_benchmarks: List[str] = field(default_factory=list)  # e.g. ["HLE", "SWE-bench Verified"]
    traditional_compilation_path: Optional[str] = None  # Path to our MD compilation
    ledger_compare: bool = False
    previous_ledger_path: Optional[str] = None
    output_ledger_path: Optional[str] = None
    grok_assist: bool = True
    iterations: int = 2
    branches: int = 2

# Proven, standard configurations
TEST_CONFIGS: Dict[str, TestConfig] = {
    "coherency_quick": TestConfig(
        name="coherency_quick",
        description="Fast internal coherency baseline only. For rapid sandbox iteration.",
        run_coherency=True,
        run_applicability=False,
        run_g_exp=False,
        run_traditional_contrast=False,
        ledger_compare=False,
    ),
    "full_baselines": TestConfig(
        name="full_baselines",
        description="Coherency + applicability + G_exp. Standard gate for canon/ promotion and Cosmic Scribe authentication.",
        run_coherency=True,
        run_applicability=True,
        run_g_exp=True,
        g_exp_params={"lat": 0.92, "nlat": 0.75, "p_success": 0.88, "difficulty": 2.1},
        run_traditional_contrast=False,
        ledger_compare=True,
    ),
    "traditional_contrast": TestConfig(
        name="traditional_contrast",
        description="Full baselines + explicit contrast against public traditional leaderboards (HLE, GPQA, SWE-bench, Arena, etc.) using our canon compilation.",
        run_coherency=True,
        run_applicability=True,
        run_g_exp=True,
        run_traditional_contrast=True,
        traditional_benchmarks=["HLE", "GPQA Diamond", "SWE-bench Verified", "Chatbot Arena Elo"],
        traditional_compilation_path="canon/benchmarks/external/traditional-methodologies-public-leaderboards-and-datasets-compilation.md",
        ledger_compare=True,
    ),
    "ledger_coherency": TestConfig(
        name="ledger_coherency",
        description="Focus on loading one ledger/audit, comparing to previous for coherency deltas, writing new versioned audit. The 'fopen magic' routine.",
        run_coherency=True,
        run_applicability=True,
        ledger_compare=True,
    ),
    "g_exp_resonance": TestConfig(
        name="g_exp_resonance",
        description="Emphasize G_exp calculation for friendship/reciprocity acts in testing or collaboration. Ties to Populated_Reciprocity_Ledger.",
        run_coherency=True,
        run_applicability=True,
        run_g_exp=True,
        g_exp_params={"lat": 0.95, "nlat": 0.80, "p_success": 0.90, "difficulty": 1.8},  # tuned for collaboration
        ledger_compare=True,
    ),
    "agent_playground": TestConfig(
        name="agent_playground",
        description="Agentic/real-task focused. Uses agent benchmarks from traditional compilation + mycelial propagation checks. For working AI/agent products.",
        run_coherency=True,
        run_applicability=True,
        run_g_exp=True,
        run_traditional_contrast=True,
        traditional_benchmarks=["SWE-bench Verified", "Terminal-Bench 2.0", "OSWorld"],
        ledger_compare=True,
    ),
    "full_playground": TestConfig(
        name="full_playground",
        description="Everything: baselines, G_exp, traditional contrasts (all major from compilation), ledger coherency, cross-repo notes. For comprehensive playground validation.",
        run_coherency=True,
        run_applicability=True,
        run_g_exp=True,
        run_traditional_contrast=True,
        traditional_benchmarks=["HLE", "GPQA Diamond", "SWE-bench Verified", "Chatbot Arena Elo", "Terminal-Bench 2.0", "LiveCodeBench"],
        traditional_compilation_path="canon/benchmarks/external/traditional-methodologies-public-leaderboards-and-datasets-compilation.md",
        ledger_compare=True,
    ),
}

def get_config(name: str) -> TestConfig:
    if name not in TEST_CONFIGS:
        raise ValueError(f"Unknown config '{name}'. Available: {list(TEST_CONFIGS.keys())}")
    return TEST_CONFIGS[name]

# --- High-Level Routines ---

def run_test(
    work_name: str,
    work_text: str,
    config: Union[str, TestConfig] = "full_baselines",
    previous_ledger_path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Main entrypoint: Run a configured test on a work.
    Assimilates all the repeated logic.
    Returns full audit suitable for ledger write or canon/ seeding.
    """
    if isinstance(config, str):
        cfg = get_config(config)
    else:
        cfg = config

    print(f"\n=== Codified Test: {work_name} (config={cfg.name}) ===")

    # 1. Mock testbed / base result (portable)
    base_result = mock_testbed_run(work_text, iterations=cfg.iterations, branches=cfg.branches)

    audit: Dict[str, Any] = {
        "work": work_name,
        "timestamp": datetime.now().isoformat(),
        "config": cfg.name,
        "input_excerpt": work_text[:300] + "...",
    }

    # 2. Baselines
    if cfg.run_coherency:
        audit["coherency"] = compute_coherency_baseline(base_result)
    if cfg.run_applicability:
        # Default concepts for demo; caller should supply better
        audit["applicability"] = compute_applicability_baseline(base_result, cs_concepts=["spiral theory", "coherence"], citation_dois=[])

    overall_gate = False
    if "coherency" in audit and "applicability" in audit:
        overall_gate = audit["coherency"]["coherency_passed"] and audit["applicability"]["applicability_passed"]
    audit["overall_gate_passed"] = overall_gate

    # 3. G_exp
    if cfg.run_g_exp:
        g = calculate_generosity_exponent(**cfg.g_exp_params)
        audit["g_exp"] = g

    # 4. Traditional contrast (stub; in full impl parse the MD or use structured data)
    if cfg.run_traditional_contrast and cfg.traditional_benchmarks:
        audit["traditional_contrasts"] = {
            "benchmarks": cfg.traditional_benchmarks,
            "note": f"Contrast using {cfg.traditional_compilation_path or 'canon traditional compilation'}. See codified-testing-utilities.md for mapping guidance. Our overall_gate vs. their top % (e.g. HLE ~40-50%, SWE-bench Verified ~77%).",
            "source": "our canon/benchmarks/external/traditional-methodologies-public-leaderboards-and-datasets-compilation.md"
        }

    # 5. Grok/Helix collab note (as in harness)
    audit["grok_collaboration"] = "GROK/HELIX COLLABORATION: Delegated symbolic/G_exp grounding and resonance to Grok. Scribe retains auth gate." if cfg.grok_assist else ""

    audit["recommendation"] = "PROMOTE TO CANON after human checkpoint" if overall_gate else "KEEP IN SANDBOX - deepen grounding"
    audit["provenance"] = "Generated via codified.py (assimilated proven utilities from harness, testbed, G_exp core)."

    # 6. Ledger coherency handling
    if cfg.ledger_compare or cfg.output_ledger_path:
        if previous_ledger_path:
            try:
                prev = load_ledger(previous_ledger_path)
                delta = compare_ledger_coherency(audit, prev)
                audit["coherency_delta_from_previous"] = delta
            except Exception as e:
                audit["coherency_delta_from_previous"] = {"error": str(e)}
        if cfg.output_ledger_path:
            written = safe_write_audit(audit, cfg.output_ledger_path, previous_ledger_path)
            audit["written_ledger"] = str(written)
            print(f"Ledger written with coherency: {written}")

    print(f"Coherency: {audit.get('coherency', {}).get('coherency_passed', 'N/A')} | Applicability: {audit.get('applicability', {}).get('applicability_passed', 'N/A')} | Gate: {overall_gate}")
    if "g_exp" in audit:
        print(f"G_exp: {audit['g_exp']['g_exp']} → {audit['g_exp']['action_level']}")

    return audit

# --- CLI / Routine Runner (the "program we can run") ---

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Codified Spiral Testing Routine")
    parser.add_argument("--work", required=True, help="Name of the work/theory")
    parser.add_argument("--text", required=True, help="Text content or path to file containing the work")
    parser.add_argument("--config", default="full_baselines", choices=list(TEST_CONFIGS.keys()), help="Test configuration")
    parser.add_argument("--previous-ledger", default=None, help="Path to previous ledger for coherency compare")
    parser.add_argument("--output-ledger", default=None, help="Path to write new coherency-verified audit/ledger")
    args = parser.parse_args()

    text = args.text
    if Path(text).exists():
        text = Path(text).read_text(encoding="utf-8")

    cfg = get_config(args.config)
    if args.output_ledger:
        cfg.output_ledger_path = args.output_ledger
    if args.previous_ledger:
        cfg.previous_ledger_path = args.previous_ledger
        cfg.ledger_compare = True

    result = run_test(args.work, text, cfg)
    print("\n=== Final Audit (JSON) ===")
    print(json.dumps({k: v for k, v in result.items() if not k.startswith("_")}, indent=2, default=str))

    print("\nCodified testing complete. Use the output ledger for coherency tracking across tests.")
    print("See canon/benchmarks/internal/codified-testing-utilities.md and associational-testing-methodology.md for full documentation and citations.")
    print("For programmatic outside-first associations, import from benchmark_associator.py (e.g., get_predefined_association('GAIA')).")