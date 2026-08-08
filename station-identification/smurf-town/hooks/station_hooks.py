"""
station_hooks.py

Hooks that feed residual maps from smurfs into the station-identification
floating-sheet / review pipeline.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List

from core.smurf_base import SmurfBase
from core.residual import compare_to_baselines


def residual_map_for_station(smurfs: List[SmurfBase]) -> Dict[str, Any]:
    """
    Produce a compact residual map suitable for inclusion in a
    floating review sheet or station review packet.
    """
    entries = []
    for s in smurfs:
        expr = s.express_host()
        latest = expr.get("latest_residual") or {}
        residual_val = latest.get("value")
        entries.append({
            "smurf_id": s.smurf_id,
            "role": s.role,
            "attached_subject": s.attached_subject,
            "status": latest.get("status", "unknown"),
            "residual": residual_val,
            "S_approx": latest.get("S_approx"),
            "G_approx": latest.get("G_approx"),
            "history_length": expr.get("history_length", 0),
            "geometry": expr.get("geometry_summary"),
        })

    residuals = [e["residual"] for e in entries if e["residual"] is not None]
    mean_r = sum(residuals) / len(residuals) if residuals else None
    return {
        "generated_at": time.time(),
        "smurf_count": len(entries),
        "mean_residual": mean_r,
        "baseline": compare_to_baselines(mean_r) if mean_r is not None else None,
        "entries": entries,
        "notes": "Residual-only map. No host content included.",
    }


def station_review_snippet(smurfs: List[SmurfBase], context: str = "") -> str:
    """
    Return a short markdown snippet that can be dropped into a
    station review document.
    """
    rmap = residual_map_for_station(smurfs)
    baseline = rmap.get("baseline") or {}
    lines = [
        "### Smurf Town Residual Snapshot",
        f"Context: {context or 'station review'}",
        f"Active smurfs: {rmap['smurf_count']}",
        f"Mean residual: {rmap['mean_residual']}",
        f"Baseline band: {baseline.get('band', 'n/a')}",
        "",
        "| Smurf | Role | Status | Residual |",
        "|-------|------|--------|----------|",
    ]
    for e in rmap["entries"]:
        lines.append(
            f"| {e['smurf_id']} | {e['role']} | {e['status']} | {e['residual']} |"
        )
    lines.append("")
    lines.append("*Residual-only. Continuity collective record.*")
    return "\n".join(lines)
