"""auth_cycle.py — Iterative Authentication Cycle (five gateways, valid → workable)
G1 residual · G2 parallel differential · G3 dual-signal · G4 multi-config · G5 VAAS optional
LOCK companion — Sir Benjamin + Grok — 2026-08-09
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple
from core.residual import ResidualInputs
from core.validity import assess_validity, assess_multi_config_validity

try:
    import importlib.util
    from pathlib import Path
    _here = Path(__file__).resolve()
    _candidates = [Path("/tmp/parallel_differential.py"), _here.parents[1]/"meta-standards"/"parallel_differential.py", _here.parents[2]/"meta-standards"/"parallel_differential.py"]
    quick_eval = None
    for _pd_path in _candidates:
        if _pd_path.exists():
            _spec = importlib.util.spec_from_file_location("parallel_differential", str(_pd_path))
            _pd = importlib.util.module_from_spec(_spec)
            _spec.loader.exec_module(_pd)
            quick_eval = _pd.quick_eval
            break
except Exception:
    quick_eval = None

CLASS_ADVANCE_OK, CLASS_STALL_ZONE, CLASS_PARADOX_DOM = "advance_ok", "STALL_ZONE", "paradox_dom"
CLASS_DISCONTINUOUS, CLASS_ELEVATED_MIX, CLASS_CONT_PARADOX = "discontinuous", "elevated_mix", "cont_paradox"

def dual_signal_class(residual, valid, diff_ap):
    if residual <= 0.20 and valid and diff_ap > 0: return CLASS_ADVANCE_OK
    if residual <= 0.20 and valid and diff_ap <= 0: return CLASS_CONT_PARADOX
    if residual > 0.55: return CLASS_DISCONTINUOUS
    if diff_ap < -0.3: return CLASS_PARADOX_DOM
    if diff_ap > 0 and residual > 0.20: return CLASS_STALL_ZONE
    return CLASS_ELEVATED_MIX

@dataclass
class GatewayResult:
    gateway: str
    passed: bool
    detail: Dict[str, Any] = field(default_factory=dict)
    notes: str = ""

@dataclass
class AuthCycleResult:
    cycle_id: str
    subject: str
    S: float
    G: float
    C: float
    E: float
    gateways: List[GatewayResult]
    dual_class: str
    residual: float
    diff_ap: float
    validity_passed: bool
    workable: bool
    type_batch_estimate: List[str]
    order: str = "valid_then_workable"
    def as_dict(self):
        return {"cycle_id": self.cycle_id, "subject": self.subject, "field": {"S": self.S, "G": self.G, "C": self.C, "E": self.E}, "dual_class": self.dual_class, "residual": self.residual, "diff_ap": self.diff_ap, "validity_passed": self.validity_passed, "workable": self.workable, "type_batch_estimate": self.type_batch_estimate, "order": self.order, "gateways": [{"gateway": g.gateway, "passed": g.passed, "detail": g.detail, "notes": g.notes} for g in self.gateways]}

def _estimate_type_batch(dual_class, residual, diff_ap):
    if dual_class == CLASS_ADVANCE_OK: return []
    kinds = []
    if residual > 0.55: kinds.append("recover_disc")
    if residual > 0.30: kinds.append("recover_elev")
    if diff_ap <= 0: kinds.append("raise_G_sep")
    if dual_class == CLASS_STALL_ZONE or (diff_ap > 0 and residual > 0.20): kinds.append("stall_break_S")
    return list(dict.fromkeys(kinds))

def run_auth_cycle(S, G, C, E=0.70, *, subject="station-auth", residual_require="good", handshake_require="good", configs=None, vaas_kept=None, cycle_id="auth-cycle"):
    gateways = []
    v = assess_validity(S, G, C, require=residual_require)
    g1_pass = bool(v.valid) and (v.residual <= 0.20 if residual_require == "good" else bool(v.valid))
    gateways.append(GatewayResult("G1_residual_continuity", g1_pass, {"residual": v.residual, "band": v.baseline_band, "strength": v.strength, "require": residual_require}, "Subject field continuous enough"))
    if quick_eval is None:
        diff_ap, g2_pass, g2_detail = 0.0, False, {"error": "parallel_differential not loaded"}
    else:
        traj = quick_eval(S, G, E, C)
        diff_ap, g2_pass, g2_detail = float(traj.diff_AP), True, {"dA_dt": traj.dA_dt, "dP_dt": traj.dP_dt, "diff_AP": float(traj.diff_AP), "sum_AP": traj.sum_AP}
    gateways.append(GatewayResult("G2_parallel_differential", g2_pass, g2_detail, "Claim vs paradox separation"))
    dclass = dual_signal_class(v.residual, bool(v.valid), diff_ap)
    gateways.append(GatewayResult("G3_dual_signal_class", dclass == CLASS_ADVANCE_OK, {"class": dclass, "residual": v.residual, "diff_AP": diff_ap}, "advance_ok = resid≤0.20 ∧ A−P>0"))
    if configs is None:
        configs = {"handshake_A": ResidualInputs(S, G, C), "handshake_B": ResidualInputs(max(0,S-0.02), max(0,G-0.03), max(0,C-0.03)), "mapping_norms": ResidualInputs(max(0,S-0.12), max(0,G-0.15), max(0,C-0.15))}
    multi = assess_multi_config_validity(configs, require=handshake_require)
    if isinstance(multi, dict):
        g4_pass = bool(multi.get("handshake_valid", multi.get("all_continuous", False)))
        g4_detail = {"handshake_valid": multi.get("handshake_valid"), "mean_residual": multi.get("mean_residual"), "require": handshake_require}
    else:
        g4_pass, g4_detail = False, {"raw": str(multi)}
    gateways.append(GatewayResult("G4_multi_config_handshake", g4_pass, g4_detail, "Cross-config continuity"))
    if vaas_kept is None:
        gateways.append(GatewayResult("G5_VAAS_intake", True, {"mounted": False}, "VAAS not mounted"))
    else:
        gateways.append(GatewayResult("G5_VAAS_intake", bool(vaas_kept), {"mounted": True, "kept": bool(vaas_kept)}, "Alternating-standards hygiene"))
    validity_passed = gateways[1].passed and dclass != CLASS_DISCONTINUOUS and (vaas_kept is None or bool(vaas_kept))
    workable = dclass == CLASS_ADVANCE_OK and (vaas_kept is None or bool(vaas_kept))
    return AuthCycleResult(cycle_id, subject, S, G, C, E, gateways, dclass, v.residual, diff_ap, validity_passed, workable, _estimate_type_batch(dclass, v.residual, diff_ap))
