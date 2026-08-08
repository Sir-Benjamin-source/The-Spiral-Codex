"""
test_float_export.py

Tests for residual → .float / .fsheet light export adapters.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from population.seed_smurfs.seed_example import create_seed_population
from hooks.auth_integration import batch_continuity_checks
from hooks.float_export import (
    residual_to_coherence_note,
    residual_to_float_designation,
    smurf_town_inventory_entry,
    export_residual_for_float_fsheet,
)
from hooks.station_hooks import residual_map_for_station


def test_coherence_note_shape():
    pop = create_seed_population()
    batch_continuity_checks(pop, 0.88, 0.82)
    rmap = residual_map_for_station(pop)
    note = residual_to_coherence_note(rmap)
    assert "timestamp" in note
    assert "note" in note
    assert "residual" in note["note"].lower() or "band" in note["note"].lower()
    print("PASS: coherence note shape")


def test_float_designation_shape():
    pop = create_seed_population()
    batch_continuity_checks(pop, 0.88, 0.82)
    rmap = residual_map_for_station(pop)
    des = residual_to_float_designation(rmap)
    assert des["target"]
    assert "residual band=" in des["designation"]
    assert "since" in des
    print("PASS: float designation shape")


def test_inventory_entry():
    entry = smurf_town_inventory_entry()
    assert entry["id"] == "smurf-town"
    assert entry["status"] == "active-foundation"
    print("PASS: inventory entry")


def test_full_export():
    pop = create_seed_population()
    batch_continuity_checks(pop, 0.90, 0.85)
    export = export_residual_for_float_fsheet(pop)
    assert "residual_map" in export
    assert "coherence_note" in export
    assert "float_designation" in export
    assert "inventory_entry" in export
    assert export["residual_map"]["baseline"]["band"] in (
        "strong", "good", "acceptable", "elevated", "discontinuous"
    )
    print("PASS: full float/fsheet export")


if __name__ == "__main__":
    test_coherence_note_shape()
    test_float_designation_shape()
    test_inventory_entry()
    test_full_export()
    print("\nAll float-export tests passed.")
