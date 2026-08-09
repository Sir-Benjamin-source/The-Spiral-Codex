"""
test_validity.py

Unambiguous tests for validity-through-coherence.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.residual import ResidualInputs
from core.validity import (
    assess_validity,
    assess_multi_config_validity,
    residual_to_validity,
)
from core.residual import compute_residual


def test_strong_is_valid():
    v = assess_validity(0.92, 0.88, 0.90, require="acceptable")
    assert v.valid is True
    assert v.strength in ("strong", "good")
    assert v.status == "continuous"
    print("PASS: strong is valid")


def test_stress_is_invalid():
    v = assess_validity(0.30, 0.25, 0.20, require="acceptable")
    assert v.valid is False
    assert v.strength in ("weak", "invalid")
    print("PASS: stress is invalid")


def test_require_strong_stricter():
    v_acc = assess_validity(0.85, 0.80, 0.75, require="acceptable")
    v_str = assess_validity(0.85, 0.80, 0.75, require="strong")
    assert v_acc.valid is True
    assert v_str.valid is False
    print("PASS: require=strong is stricter")


def test_multi_config_handshake_validity():
    configs = {
        "handshake_A": ResidualInputs(0.90, 0.86, 0.88),
        "handshake_B": ResidualInputs(0.88, 0.84, 0.85),
        "mapping_stress": ResidualInputs(0.40, 0.35, 0.30),
    }
    result = assess_multi_config_validity(configs, require="acceptable")
    assert result["handshake_valid"] is True
    assert result["per_config"]["mapping_stress"]["valid"] is False
    assert result["any_discontinuous"] is True
    print("PASS: multi-config handshake validity")


def test_validity_is_residual_only():
    v = assess_validity(0.90, 0.85, 0.80)
    d = v.__dict__
    assert "content" not in d
    assert "private" not in str(d).lower()
    assert "residual" in d
    print("PASS: validity is residual-only")


def test_residual_to_validity_roundtrip():
    deep = compute_residual(ResidualInputs(0.91, 0.87, 0.85))
    v = residual_to_validity(deep, require="good")
    assert v.residual == deep.residual
    assert v.status == deep.status
    print("PASS: residual_to_validity roundtrip")


if __name__ == "__main__":
    test_strong_is_valid()
    test_stress_is_invalid()
    test_require_strong_stricter()
    test_multi_config_handshake_validity()
    test_validity_is_residual_only()
    test_residual_to_validity_roundtrip()
    print("\nAll validity tests passed.")
