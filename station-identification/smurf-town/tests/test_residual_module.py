"""
test_residual_module.py

Unit tests for the deepened residual calculation, multi-config aggregation,
baseline bands, and auth multi-config hook.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.residual import (
    ResidualInputs,
    compute_residual,
    multi_config_residual,
    aggregate_multi_config,
    classify_kind,
    compare_to_baselines,
)


def test_strong_continuous():
    r = compute_residual(ResidualInputs(S=0.92, G=0.88, C=0.90))
    assert r.status == "continuous"
    assert r.residual < 0.30
    assert r.kind == "that"
    assert r.gated is False
    print("PASS: strong continuous")


def test_discontinuous():
    r = compute_residual(ResidualInputs(S=0.30, G=0.25, C=0.20))
    assert r.status == "discontinuous"
    assert r.residual >= 0.55
    assert r.kind == "which"
    print("PASS: discontinuous")


def test_kind_classification():
    assert classify_kind(0.85, 0.80) == "that"
    assert classify_kind(0.50, 0.50) == "which"
    print("PASS: kind classification")


def test_C_improves_residual():
    without = compute_residual(ResidualInputs(S=0.80, G=0.75))
    with_c = compute_residual(ResidualInputs(S=0.80, G=0.75, C=0.90))
    assert with_c.residual < without.residual
    print("PASS: C improves residual")


def test_multi_config_aggregate():
    configs = {
        "h1": ResidualInputs(S=0.90, G=0.85, C=0.85),
        "m1": ResidualInputs(S=0.40, G=0.35, C=0.30),
    }
    results = multi_config_residual(configs)
    agg = aggregate_multi_config(results)
    assert agg["count"] == 2
    assert agg["any_discontinuous"] is True
    assert agg["all_continuous"] is False
    assert "h1" in agg["by_config"]
    assert "baseline_comparison" in agg
    print("PASS: multi-config aggregate")


def test_clamping():
    r = compute_residual(ResidualInputs(S=1.5, G=-0.2, C=2.0))
    assert 0.0 <= r.S <= 1.0
    assert 0.0 <= r.G <= 1.0
    assert 0.0 <= r.residual <= 1.0
    print("PASS: input clamping")


def test_baseline_bands():
    assert compare_to_baselines(0.10)["band"] == "strong"
    assert compare_to_baselines(0.18)["band"] == "good"
    assert compare_to_baselines(0.28)["band"] == "acceptable"
    assert compare_to_baselines(0.40)["band"] == "elevated"
    assert compare_to_baselines(0.60)["band"] == "discontinuous"
    print("PASS: baseline bands")


def test_multi_config_auth_hook():
    from hooks.auth_integration import multi_config_auth_check
    configs = {
        "handshake_A": ResidualInputs(S=0.90, G=0.86, C=0.88),
        "mapping_stress": ResidualInputs(S=0.40, G=0.35, C=0.30),
    }
    result = multi_config_auth_check(configs)
    assert result["handshake_continuous"] is True
    assert result["aggregate"]["any_discontinuous"] is True
    assert "baseline_comparison" in result["aggregate"]
    print("PASS: multi-config auth hook")


if __name__ == "__main__":
    test_strong_continuous()
    test_discontinuous()
    test_kind_classification()
    test_C_improves_residual()
    test_multi_config_aggregate()
    test_clamping()
    test_baseline_bands()
    test_multi_config_auth_hook()
    print("\nAll residual-module tests passed.")
