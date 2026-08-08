"""
auth_integration.py

Hooks so reciprocal authentication routines can call smurfs
as specialized residual processors.

Supports single-check, population batch, and multi-config
(handshake vs mapping) residual exercises. Smurfs report residual only;
they do not grant or deny access themselves.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from core.smurf_base import SmurfBase, ResidualReport
from core.residual import (
    ResidualInputs,
    multi_config_residual,
    aggregate_multi_config,
    compare_to_baselines,
)


def run_continuity_check(
    smurf: SmurfBase,
    subject_isolation: float,
    generality_coherence: float,
    notes: str = "auth continuity check",
    instantaneous_coherence: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Perform a single residual measurement and return a structured
    result suitable for an authentication decision layer.
    """
    report: ResidualReport = smurf.sense_residual(
        subject_isolation=subject_isolation,
        generality_coherence=generality_coherence,
        notes=notes,
        instantaneous_coherence=instantaneous_coherence,
    )
    return {
        "smurf_id": smurf.smurf_id,
        "role": smurf.role,
        "residual": report.residual,
        "status": report.continuity_status,
        "passed_continuity": report.continuity_status == "continuous",
        "baseline": compare_to_baselines(report.residual),
        "expression": smurf.express_host(),
        "tune": smurf.emit_tune("auth check complete"),
    }


def batch_continuity_checks(
    smurfs: List[SmurfBase],
    subject_isolation: float,
    generality_coherence: float,
    instantaneous_coherence: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Run the same continuity inputs across a small population and
    aggregate the residual picture.
    """
    results = [
        run_continuity_check(
            s,
            subject_isolation,
            generality_coherence,
            instantaneous_coherence=instantaneous_coherence,
        )
        for s in smurfs
    ]
    residuals = [r["residual"] for r in results]
    statuses = [r["status"] for r in results]
    mean_r = sum(residuals) / len(residuals) if residuals else 0.0
    return {
        "count": len(results),
        "mean_residual": mean_r,
        "all_continuous": all(s == "continuous" for s in statuses),
        "any_discontinuous": any(s == "discontinuous" for s in statuses),
        "baseline": compare_to_baselines(mean_r) if residuals else None,
        "details": results,
    }


def multi_config_auth_check(
    configs: Dict[str, ResidualInputs],
) -> Dict[str, Any]:
    """
    Multi-config residual check for reciprocal authentication.
    Handshake configs should stay continuous; mapping configs may vary.
    Returns aggregate + baseline comparison. Residual-only.
    """
    results = multi_config_residual(configs)
    agg = aggregate_multi_config(results)
    return {
        "mode": "multi_config",
        "aggregate": agg,
        "handshake_continuous": all(
            detail["status"] == "continuous"
            for name, detail in agg.get("by_config", {}).items()
            if name.startswith("handshake")
        ),
        "notes": "Residual-only multi-config auth check. No host content.",
    }
