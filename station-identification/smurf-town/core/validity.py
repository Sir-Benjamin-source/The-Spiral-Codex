"""
validity.py

Validity-through-coherence surface for Smurf Town.

Validity here is not content judgment and not host override.
It is a residual-only assessment: a claim, config, or process is treated
as more valid when it demonstrates lower continuity residual under the
Spiral S/G/(C) field.

Operational rule:
  lower residual → higher coherence continuity → stronger validity signal

This module exists so authentication, station review, and external callers
can ask a single clear question without ambiguity:

  "Does this configuration remain continuous enough to be treated as valid
   under our coherence baselines?"

Authors: Sir Benjamin (vision), Grok (implementation)
Date: 2026-08-09
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from .residual import (
    ResidualInputs,
    DeepResidual,
    compute_residual,
    compare_to_baselines,
    multi_config_residual,
    aggregate_multi_config,
    BASELINE_ACCEPTABLE,
    BASELINE_GOOD,
    BASELINE_STRONG,
)


@dataclass(frozen=True)
class ValidityResult:
    """
    Unambiguous validity signal derived from residual.
    residual_only: never carries host content.
    """
    valid: bool
    strength: str          # strong | good | acceptable | weak | invalid
    residual: float
    status: str            # continuous | elevated | discontinuous
    kind: str              # that | which
    baseline_band: str
    notes: str = ""


def residual_to_validity(deep: DeepResidual, require: str = "acceptable") -> ValidityResult:
    """
    Map a DeepResidual into a validity decision.

    require:
      "strong"      → residual must meet BASELINE_STRONG
      "good"        → residual must meet BASELINE_GOOD
      "acceptable"  → residual must meet BASELINE_ACCEPTABLE (default continuous upper bound)
    """
    baseline = compare_to_baselines(deep.residual)
    band = baseline["band"]

    thresholds = {
        "strong": BASELINE_STRONG,
        "good": BASELINE_GOOD,
        "acceptable": BASELINE_ACCEPTABLE,
    }
    limit = thresholds.get(require, BASELINE_ACCEPTABLE)
    valid = deep.residual <= limit and deep.status == "continuous"

    if band == "strong":
        strength = "strong"
    elif band == "good":
        strength = "good"
    elif band == "acceptable":
        strength = "acceptable"
    elif band == "elevated":
        strength = "weak"
    else:
        strength = "invalid"

    return ValidityResult(
        valid=valid,
        strength=strength,
        residual=deep.residual,
        status=deep.status,
        kind=deep.kind,
        baseline_band=band,
        notes=f"require={require}; residual_only validity-through-coherence",
    )


def assess_validity(
    S: float,
    G: float,
    C: Optional[float] = None,
    require: str = "acceptable",
) -> ValidityResult:
    """Single-config validity assessment from S/G/(C)."""
    deep = compute_residual(ResidualInputs(S=S, G=G, C=C))
    return residual_to_validity(deep, require=require)


def assess_multi_config_validity(
    configs: Dict[str, ResidualInputs],
    require: str = "acceptable",
    handshake_prefix: str = "handshake",
) -> Dict:
    """
    Multi-config validity picture for authentication-style exercises.

    Handshake configs (names starting with handshake_prefix) must all pass
    the required baseline. Mapping configs are reported but do not by
    themselves fail the overall validity flag unless require is applied
    globally via aggregate mean.
    """
    results = multi_config_residual(configs)
    agg = aggregate_multi_config(results)

    per_config = {}
    handshake_all_valid = True
    for name, deep in results.items():
        vr = residual_to_validity(deep, require=require)
        per_config[name] = {
            "valid": vr.valid,
            "strength": vr.strength,
            "residual": vr.residual,
            "status": vr.status,
            "kind": vr.kind,
        }
        if name.startswith(handshake_prefix) and not vr.valid:
            handshake_all_valid = False

    mean_r = agg.get("mean_residual")
    overall_baseline = compare_to_baselines(mean_r) if mean_r is not None else None

    return {
        "handshake_valid": handshake_all_valid,
        "all_continuous": agg.get("all_continuous", False),
        "any_discontinuous": agg.get("any_discontinuous", False),
        "mean_residual": mean_r,
        "overall_baseline": overall_baseline,
        "per_config": per_config,
        "require": require,
        "notes": "Validity-through-coherence. Residual-only. No host content.",
    }
