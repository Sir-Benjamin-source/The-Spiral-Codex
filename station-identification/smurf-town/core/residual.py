"""
residual.py

Deepened residual measurement aligned with Spiral coherence methods.

Incorporates:
- S (Subject Isolation Strength) and G (Generality Expansion) from station meta-standards
- Optional C (Instantaneous Coherence)
- that / which classification and volatility-style gating inspired by mycelial_coherence.py (DAER)
- Formal soft baselines for continuity comparison
- Multi-config residual runs suitable for authentication exercises

Residual is defined so that lower values indicate better continuity with the expected
subject + generality field. It is residual-only; no host content is processed.

Authors: Sir Benjamin (vision), Grok (implementation)
Date: 2026-08-08 / 2026-08-09 fail-closed non-finite
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


THAT_VOLATILITY_THRESHOLD = 0.30
WHICH_VOLATILITY_THRESHOLD = 0.40
CONTINUOUS_MAX = 0.30
ELEVATED_MAX = 0.55
BASELINE_STRONG = 0.12
BASELINE_GOOD = 0.20
BASELINE_ACCEPTABLE = 0.30


@dataclass(frozen=True)
class ResidualInputs:
    S: float
    G: float
    C: Optional[float] = None


@dataclass
class DeepResidual:
    residual: float
    status: str
    kind: str
    S: float
    G: float
    C: Optional[float]
    volatility: float
    gated: bool
    notes: str = ""


def classify_kind(S: float, G: float) -> str:
    if S >= 0.70 and (S * G) >= 0.50:
        return "that"
    return "which"


def compute_volatility(S: float, G: float, C: Optional[float] = None) -> float:
    base = (1.0 - S) * 0.55 + (1.0 - G) * 0.45
    if C is not None:
        base = base * (1.0 - 0.35 * C)
    return max(0.0, min(1.0, base))


def _finite_unit(x: float, default: float = 0.0) -> float:
    """Clamp to [0, 1]; non-finite values become default (fail-closed)."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return default
    if v != v or v == float("inf") or v == float("-inf"):
        return default
    return max(0.0, min(1.0, v))


def compute_residual(inputs: ResidualInputs) -> DeepResidual:
    S = _finite_unit(inputs.S, default=0.0)
    G = _finite_unit(inputs.G, default=0.0)
    C = None if inputs.C is None else _finite_unit(inputs.C, default=0.0)

    kind = classify_kind(S, G)
    volatility = compute_volatility(S, G, C)

    residual = (1.0 - S) * 0.45 + (1.0 - G) * 0.40
    if C is not None:
        residual += (1.0 - C) * 0.15
    else:
        residual += 0.05
    residual = max(0.0, min(1.0, residual))

    threshold = THAT_VOLATILITY_THRESHOLD if kind == "that" else WHICH_VOLATILITY_THRESHOLD
    gated = volatility > threshold

    if residual >= ELEVATED_MAX:
        status = "discontinuous"
    elif residual >= CONTINUOUS_MAX:
        status = "elevated"
    else:
        status = "continuous"

    return DeepResidual(
        residual=round(residual, 6),
        status=status,
        kind=kind,
        S=S,
        G=G,
        C=C,
        volatility=round(volatility, 6),
        gated=gated,
        notes="",
    )


def multi_config_residual(configs: Dict[str, ResidualInputs]) -> Dict[str, DeepResidual]:
    return {name: compute_residual(inp) for name, inp in configs.items()}


def aggregate_multi_config(results: Dict[str, DeepResidual]) -> Dict:
    if not results:
        return {"count": 0, "mean_residual": None, "all_continuous": False}

    residuals = [r.residual for r in results.values()]
    statuses = [r.status for r in results.values()]
    gated_count = sum(1 for r in results.values() if r.gated)
    mean_r = sum(residuals) / len(residuals)

    return {
        "count": len(results),
        "mean_residual": round(mean_r, 6),
        "max_residual": max(residuals),
        "min_residual": min(residuals),
        "all_continuous": all(s == "continuous" for s in statuses),
        "any_discontinuous": any(s == "discontinuous" for s in statuses),
        "gated_count": gated_count,
        "baseline_comparison": compare_to_baselines(mean_r),
        "by_config": {
            name: {
                "residual": r.residual,
                "status": r.status,
                "kind": r.kind,
                "gated": r.gated,
            }
            for name, r in results.items()
        },
    }


def compare_to_baselines(residual: float) -> Dict[str, object]:
    if residual <= BASELINE_STRONG:
        band = "strong"
    elif residual <= BASELINE_GOOD:
        band = "good"
    elif residual <= BASELINE_ACCEPTABLE:
        band = "acceptable"
    elif residual < ELEVATED_MAX:
        band = "elevated"
    else:
        band = "discontinuous"

    return {
        "residual": round(residual, 6),
        "band": band,
        "meets_strong": residual <= BASELINE_STRONG,
        "meets_good": residual <= BASELINE_GOOD,
        "meets_acceptable": residual <= BASELINE_ACCEPTABLE,
        "baselines": {
            "strong": BASELINE_STRONG,
            "good": BASELINE_GOOD,
            "acceptable": BASELINE_ACCEPTABLE,
            "elevated_max": ELEVATED_MAX,
        },
    }
