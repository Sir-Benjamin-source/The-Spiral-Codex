"""
float_export.py

Light adapters so smurf residual maps can feed station .float / .fsheet
surfaces without diluting their required fields.

- residual observations → fsheet coherence_notes entries
- residual band → float current_designations style entries
- inventory hints for the smurf-town package itself

Keeps the float limitation rule: limited surface, no extra required fields.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from core.smurf_base import SmurfBase
from core.residual import compare_to_baselines
from hooks.station_hooks import residual_map_for_station


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def residual_to_coherence_note(
    residual_map: Dict[str, Any],
    context: str = "smurf residual snapshot",
) -> Dict[str, str]:
    """
    Produce one fsheet-compatible coherence_notes entry from a residual map.
    Residual-only; no host content.
    """
    mean_r = residual_map.get("mean_residual")
    baseline = residual_map.get("baseline") or {}
    band = baseline.get("band", "n/a")
    count = residual_map.get("smurf_count", 0)
    note = (
        f"{context}: {count} smurfs, mean residual={mean_r}, "
        f"baseline band={band}. Residual-only continuity record."
    )
    return {
        "timestamp": _now_iso(),
        "note": note,
    }


def residual_to_float_designation(
    residual_map: Dict[str, Any],
    target: str = "smurf-town residual continuity",
) -> Dict[str, str]:
    """
    Produce one float-compatible current_designations entry from a residual map.
    """
    baseline = residual_map.get("baseline") or {}
    band = baseline.get("band", "unknown")
    mean_r = residual_map.get("mean_residual")
    designation = f"residual band={band} (mean={mean_r})"
    return {
        "target": target,
        "designation": designation,
        "since": _now_iso(),
    }


def smurf_town_inventory_entry(
    path_or_ref: str = "station-identification/smurf-town/",
    status: str = "active-foundation",
) -> Dict[str, str]:
    """Inventory-style entry for an fsheet inventory list."""
    return {
        "id": "smurf-town",
        "path_or_ref": path_or_ref,
        "status": status,
        "last_touched": _now_iso(),
    }


def export_residual_for_float_fsheet(
    smurfs: List[SmurfBase],
    context: str = "station residual cycle",
) -> Dict[str, Any]:
    """
    One-shot export: residual map + coherence note + float designation
    + inventory hint. Ready to merge into existing .float / .fsheet bodies.
    """
    rmap = residual_map_for_station(smurfs)
    return {
        "residual_map": rmap,
        "coherence_note": residual_to_coherence_note(rmap, context=context),
        "float_designation": residual_to_float_designation(rmap),
        "inventory_entry": smurf_town_inventory_entry(),
        "notes": "Residual-only export. Merge into fsheet/float; do not expand required fields.",
    }
