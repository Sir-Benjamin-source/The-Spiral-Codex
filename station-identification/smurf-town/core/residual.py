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
Date: 2026-08-08
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


# ---------------------------------------------------------------------------
# Soft baselines (formalized for station / auth comparison)
# ---------------------------------------------------------------------------
# Align volatility thresholds with mycelial_coherence DAER style
THAT_VOLATILITY_THRESHOLD = 0.30
WHICH_VOLATILITY_THRESHOLD = 0.40

# Residual status bands — soft baselines for continuity work
CONTINUOUS_MAX = 0.30          # residual < this → continuous
ELEVATED_MAX = 0.55            # residual < this → elevated; else discontinuous

# Soft target bands for healthy spiralworks operation
BASELINE_STRONG = 0.12         # strong continuous target
BASELINE_GOOD = 0.20           # good continuous target
BASELINE_ACCEPTABLE = 0.30     # upper bound of continuous


@dataclass(frozen=True)
class ResidualInputs:
    """Inputs for a residual measurement. All values expected in [0, 1]."""
    S: float                          # Subject Isolation Strength
    G: float                          # Generality Expansion / coherence of associations
    C: Optional[float] = None         # Instantaneous Coherence (optional)


@dataclass
class DeepResidual:
    """Result of a deepened residual calculation."""
    residual: float
    status: str                       # continuous | elevated | discontinuous
    kind: str                         # that | which
    S: float
    G: float
    C: Optional[float]
    volatility: float
    gated: bool                       # True if volatility exceeded kind threshold
    notes: str = ""


def classify_kind(S: float, G: float) -> str:
    """
    Classify the measurement as 'that' (essential / high isolation)
    or 'which' (additive / more exploratory).

    High S tends toward 'that'; lower S or lower joint S*G tends toward 'which'.
    """
    if S >= 0.70 and (S * G) >= 0.50:
        return "that"
    return "which"


def compute_volatility(S: float, G: float, C: Optional[float] = None) -> float:
    """
    Simple volatility estimate.
    High when isolation is weak or generality is incoherent.
    Optional C reduces volatility when coherence is high.
    """
    base = (1.0 - S) * 0.55 + (1.0 - G) * 0.45
    if C is not None:
        base = base * (1.0 - 0.35 * C)
    return max(0.0, min(1.0, base))


def compute_residual(inputs: ResidualInputs) -> DeepResidual:
    """
    Core residual function.

    residual ≈ weighted discontinuity of the (S, G[, C]) field.
    Status bands (soft baselines):
      continuous   residual < CONTINUOUS_MAX (0.30)
      elevated     CONTINUOUS_MAX <= residual < ELEVATED_MAX (0.55)
      discontinuous residual >= ELEVATED_MAX
    """
    S = max(0.0, min(1.0, inputs.S))
    G = max(0.0, min(1.0, inputs.G))
    C = None if inputs.C is None else max(0.0, min(1.0, inputs.C))

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


def multi_config_residual(
    configs: Dict[str, ResidualInputs],
) -> Dict[str, DeepResidual]:
    """
    Run residual measurement across multiple named configurations.
    Useful for handshake (fixed) vs mapping (variable) authentication exercises.
    """
    return {name: compute_residual(inp) for name, inp in configs.items()}


def aggregate_multi_config(results: Dict[str, DeepResidual]) -> Dict:
    """Aggregate a multi-config residual run into a compact continuity picture."""
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
    """
    Compare a residual (or mean residual) against formal soft baselines.
    Returns a compact assessment usable in station reviews and auth decisions.
    """
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
