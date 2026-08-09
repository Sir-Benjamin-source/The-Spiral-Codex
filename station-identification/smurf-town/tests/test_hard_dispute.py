"""
test_hard_dispute.py

Additional hard-to-dispute tests for residual / validity behavior.
Designed to fail loudly if ranking, separation, or residual-only
contracts break.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.residual import (
    ResidualInputs,
    compute_residual,
    multi_config_residual,
    aggregate_multi_config,
    compare_to_baselines,
    CONTINUOUS_MAX,
    ELEVATED_MAX,
    BASELINE_STRONG,
    BASELINE_GOOD,
    BASELINE_ACCEPTABLE,
)
from core.validity import assess_validity, assess_multi_config_validity
from core.smurf_base import SmurfBase
from core.directives import report_compliance


def test_residual_monotone_in_S():
    g = 0.75
    prev = None
    for s in [0.3, 0.5, 0.7, 0.9]:
        r = compute_residual(ResidualInputs(S=s, G=g, C=0.7)).residual
        if prev is not None:
            assert r <= prev + 1e-9, f"S={s} residual {r} > prev {prev}"
        prev = r
    print("PASS: residual monotone non-increasing in S")


def test_residual_monotone_in_G():
    s = 0.75
    prev = None
    for g in [0.3, 0.5, 0.7, 0.9]:
        r = compute_residual(ResidualInputs(S=s, G=g, C=0.7)).residual
        if prev is not None:
            assert r <= prev + 1e-9
        prev = r
    print("PASS: residual monotone non-increasing in G")


def test_status_bands_partition():
    samples = []
    for s in [0.2, 0.4, 0.6, 0.8, 1.0]:
        for g in [0.2, 0.4, 0.6, 0.8, 1.0]:
            samples.append(compute_residual(ResidualInputs(S=s, G=g)))
    for d in samples:
        if d.residual < CONTINUOUS_MAX:
            assert d.status == "continuous"
        elif d.residual < ELEVATED_MAX:
            assert d.status == "elevated"
        else:
            assert d.status == "discontinuous"
    print("PASS: status bands partition sample grid")


def test_validity_implies_continuous():
    for s in [0.5, 0.7, 0.9]:
        for g in [0.5, 0.7, 0.9]:
            v = assess_validity(s, g, 0.8, require="acceptable")
            if v.valid:
                assert v.status == "continuous"
                assert v.residual <= BASELINE_ACCEPTABLE
    print("PASS: validity implies continuous and residual bound")


def test_handshake_stress_separation():
    configs = {
        "handshake_A": ResidualInputs(0.91, 0.87, 0.88),
        "handshake_B": ResidualInputs(0.89, 0.85, 0.86),
        "mapping_stress": ResidualInputs(0.35, 0.30, 0.25),
    }
    result = assess_multi_config_validity(configs, require="acceptable")
    assert result["handshake_valid"] is True
    assert result["per_config"]["mapping_stress"]["valid"] is False
    assert result["per_config"]["handshake_A"]["valid"] is True
    print("PASS: handshake/stress separation")


def test_expression_never_carries_content_keys():
    s = SmurfBase(smurf_id="hard-001", role="test")
    s.sense_residual(0.85, 0.80, instantaneous_coherence=0.75)
    expr = s.express_host()
    forbidden = {"content", "private", "payload", "secret", "host_data"}
    keys = set(expr.keys()) | set((expr.get("latest_residual") or {}).keys())
    assert keys.isdisjoint(forbidden)
    assert "latest_residual" in expr
    assert "directives_compliance" in expr
    print("PASS: expression has no content keys")


def test_directives_locked_flag():
    c = report_compliance()
    assert c["locked"] is True
    assert c["residual_only"] is True
    assert c["express_host_coherence"] is True
    print("PASS: directives locked residual-only")


def test_baseline_constants_ordered():
    assert BASELINE_STRONG < BASELINE_GOOD <= BASELINE_ACCEPTABLE
    assert BASELINE_ACCEPTABLE == CONTINUOUS_MAX
    assert CONTINUOUS_MAX < ELEVATED_MAX
    print("PASS: baseline constants ordered")


def test_clamped_inputs_stable():
    for s, g, c in [(-5, -5, -5), (5, 5, 5), (0, 1, 0), (1, 0, 1)]:
        d = compute_residual(ResidualInputs(S=s, G=g, C=c))
        assert 0.0 <= d.residual <= 1.0
        assert 0.0 <= d.S <= 1.0
        assert 0.0 <= d.G <= 1.0
    print("PASS: clamped inputs stable")


def test_aggregate_mean_between_min_max():
    configs = {
        "a": ResidualInputs(0.9, 0.9, 0.9),
        "b": ResidualInputs(0.4, 0.4, 0.4),
    }
    results = multi_config_residual(configs)
    agg = aggregate_multi_config(results)
    assert agg["min_residual"] <= agg["mean_residual"] <= agg["max_residual"]
    print("PASS: aggregate mean between min and max")


if __name__ == "__main__":
    test_residual_monotone_in_S()
    test_residual_monotone_in_G()
    test_status_bands_partition()
    test_validity_implies_continuous()
    test_handshake_stress_separation()
    test_expression_never_carries_content_keys()
    test_directives_locked_flag()
    test_baseline_constants_ordered()
    test_clamped_inputs_stable()
    test_aggregate_mean_between_min_max()
    print("\nAll hard-dispute tests passed.")
