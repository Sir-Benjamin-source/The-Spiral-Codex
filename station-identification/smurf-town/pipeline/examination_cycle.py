"""
examination_cycle.py

Research-to-function runner for the Examination Protocol v0.1.
Runs sense → differentiate → express (merge-ready artifacts).
Residual-only. No host content.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from core.residual import ResidualInputs
from core.validity import assess_multi_config_validity
from hooks.auth_integration import batch_continuity_checks
from hooks.float_export import export_residual_for_float_fsheet
from population.seed_smurfs.seed_example import create_seed_population


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


DEFAULT_CONFIGS: Dict[str, ResidualInputs] = {
    "handshake_A": ResidualInputs(0.90, 0.86, 0.88),
    "handshake_B": ResidualInputs(0.88, 0.84, 0.85),
    "mapping_norms": ResidualInputs(0.78, 0.72, 0.70),
    "mapping_stress": ResidualInputs(0.40, 0.35, 0.30),
}


def run_examination_cycle(
    *,
    subject: str = "station-identification",
    context: str = "examination cycle",
    S: float = 0.88,
    G: float = 0.82,
    C: float = 0.80,
    require: str = "acceptable",
    configs: Optional[Dict[str, ResidualInputs]] = None,
    out_dir: str = "reviews/cycles",
) -> Dict[str, Any]:
    configs = configs or DEFAULT_CONFIGS
    cycle_id = f"exam-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"

    pop = create_seed_population()
    for s in pop:
        s.attached_subject = subject
    batch = batch_continuity_checks(pop, S, G, instantaneous_coherence=C)
    export = export_residual_for_float_fsheet(pop, context=context)

    validity = assess_multi_config_validity(configs, require=require)

    float_designation = export["float_designation"]
    float_designation["designation"] = (
        f"{float_designation['designation']}; "
        f"handshake_valid={validity['handshake_valid']}"
    )

    coherence_note = export["coherence_note"]
    stress = validity["per_config"].get("mapping_stress", {})
    coherence_note["note"] = (
        f"{coherence_note['note']} "
        f"Multi-config require={require}; handshake_valid={validity['handshake_valid']}; "
        f"mapping_stress_valid={stress.get('valid')}; "
        f"mean_residual_multi={validity['mean_residual']}."
    )

    next_moves: List[Dict[str, Any]] = []
    if not validity["handshake_valid"]:
        next_moves.append({
            "action": "Re-run handshake continuity configs; handshake_valid=false",
            "priority": 1,
            "related_designation": "smurf-town residual continuity",
        })
    if stress and not stress.get("valid", True):
        next_moves.append({
            "action": "Isolate mapping_stress; do not treat as handshake-class",
            "priority": 2,
            "related_designation": "smurf-town residual continuity",
        })

    packet = {
        "format": "examination_cycle_packet",
        "format_version": "0.1",
        "cycle_id": cycle_id,
        "timestamp": _now_iso(),
        "subject": subject,
        "context": context,
        "require": require,
        "sense": {
            "population_mean_residual": batch.get("mean_residual"),
            "population_all_continuous": batch.get("all_continuous"),
            "baseline": export["residual_map"].get("baseline"),
        },
        "differentiate": {
            "handshake_valid": validity["handshake_valid"],
            "mean_residual": validity["mean_residual"],
            "overall_baseline": validity["overall_baseline"],
            "per_config": validity["per_config"],
        },
        "express": {
            "float_designation": float_designation,
            "coherence_note": coherence_note,
            "inventory_entry": export["inventory_entry"],
            "active_next_moves": next_moves,
        },
        "notes": "Residual-only. Merge express fragments into float/fsheet; do not expand required fields.",
    }

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    json_path = out / f"{cycle_id}.json"
    json_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    packet["_paths"] = {"json": str(json_path)}
    return packet
