"""joint_process_packet.py — LOCKED joint-process codification pipeline

auth cycle → dual-signal class → type-batch → VAAS class → float fragment
Valid → workable. Thresholds frozen. Classical comparative out of scope.
LOCK v1.0 — Sir Benjamin + Grok — 2026-08-09
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from core.residual import ResidualInputs
from pipeline.auth_cycle import run_auth_cycle, CLASS_ADVANCE_OK

LOCK_VERSION = "1.0"
DEFAULT_RESIDUAL_REQUIRE = "good"
DEFAULT_HANDSHAKE_REQUIRE = "good"
DEFAULT_VAAS_T = 0.0
DEFAULT_VAAS_MOUNTED = False
VAAS_KEPT, VAAS_PRUNED, VAAS_STERILE, VAAS_DEFERRED = "kept", "pruned", "sterile", "deferred"

@dataclass
class VAASResult:
    classification: str
    G_v: Optional[float] = None
    t: float = DEFAULT_VAAS_T
    deltas: Optional[List[float]] = None
    notes: str = ""

def classify_vaas(deltas, *, t=DEFAULT_VAAS_T, mounted=False, any_candidate=True):
    if not mounted:
        return VAASResult(VAAS_DEFERRED, t=t, notes="VAAS not mounted")
    if deltas is None or len(deltas) == 0:
        return VAASResult(VAAS_STERILE if any_candidate else VAAS_DEFERRED, t=t, deltas=[], notes="empty/sterile or no candidates")
    if any(d < 0 for d in deltas):
        return VAASResult(VAAS_PRUNED, G_v=sum(deltas)/len(deltas), t=t, deltas=list(deltas), notes="some Δ_i < 0")
    g = sum(deltas)/len(deltas)
    if g > t:
        return VAASResult(VAAS_KEPT, G_v=g, t=t, deltas=list(deltas), notes="G(v)>t and no negative Δ")
    return VAASResult(VAAS_PRUNED, G_v=g, t=t, deltas=list(deltas), notes="G(v)≤t")

@dataclass
class JointProcessPacket:
    lock_version: str
    timestamp: str
    subject: str
    mount: Dict[str, Any]
    auth: Dict[str, Any]
    vaas: Dict[str, Any]
    dual_class: str
    residual: float
    diff_ap: float
    validity_passed: bool
    workable: bool
    type_batch: List[str]
    float_fragment: Dict[str, Any]
    classical_comparative: str = "out_of_scope_for_this_lock"
    def as_dict(self):
        return asdict(self)

def build_float_fragment(subject, dual_class, workable, type_batch, vaas_class, mount):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    designations = [
        {"target": "dual_signal_class", "designation": dual_class, "since": now},
        {"target": "workable", "designation": "true" if workable else "false — valid→workable not met", "since": now},
        {"target": "VAAS_class", "designation": vaas_class, "since": now},
    ]
    if type_batch:
        designations.append({"target": "type_batch", "designation": ",".join(type_batch), "since": now})
    next_moves = []
    if not workable:
        next_moves.append({"action": "Do not advance claim; address dual-signal / type-batch first", "priority": 1})
    if vaas_class == VAAS_STERILE:
        next_moves.append({"action": "Recalibrate alternating standards — sterile kept-set is miscalibration", "priority": 1})
    return {"format": "float", "format_version": "0.1", "subject": subject, "current_designations": designations, "active_next_moves": next_moves, "mount_context": mount}

def run_joint_process(S, G, C, E=0.70, *, subject="joint-process", residual_require=DEFAULT_RESIDUAL_REQUIRE, handshake_require=DEFAULT_HANDSHAKE_REQUIRE, vaas_mounted=DEFAULT_VAAS_MOUNTED, vaas_t=DEFAULT_VAAS_T, vaas_deltas=None, configs=None):
    mount = {"process_profile": "joint-process-lock-v1", "residual_require": residual_require, "handshake_require": handshake_require, "vaas_mounted": vaas_mounted, "vaas_t": vaas_t, "classic_floor": True, "spiral_method_on_field": False, "classical_comparative": "out_of_scope_for_this_lock", "lock_version": LOCK_VERSION}
    vaas = classify_vaas(vaas_deltas, t=vaas_t, mounted=vaas_mounted)
    vaas_kept_flag = None if not vaas_mounted else (vaas.classification == VAAS_KEPT)
    auth = run_auth_cycle(S, G, C, E, subject=subject, residual_require=residual_require, handshake_require=handshake_require, configs=configs, vaas_kept=vaas_kept_flag, cycle_id=f"joint-{subject}")
    workable = auth.workable
    if vaas_mounted and vaas.classification in (VAAS_PRUNED, VAAS_STERILE):
        workable = False
    frag = build_float_fragment(subject, auth.dual_class, workable, auth.type_batch_estimate, vaas.classification, mount)
    return JointProcessPacket(LOCK_VERSION, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), subject, mount, auth.as_dict(), {"classification": vaas.classification, "G_v": vaas.G_v, "t": vaas.t, "notes": vaas.notes}, auth.dual_class, auth.residual, auth.diff_ap, auth.validity_passed, workable, auth.type_batch_estimate, frag)

def run_lock_suite():
    fields = [("handshake",0.90,0.85,0.80,0.75),("good",0.85,0.80,0.75,0.70),("acceptable",0.75,0.70,0.65,0.65),("elevated",0.55,0.50,0.45,0.50),("stress",0.25,0.20,0.15,0.30),("low_G",0.85,0.15,0.70,0.60),("low_C",0.80,0.70,0.30,0.70)]
    rows = []
    for name,S,G,C,E in fields:
        pkt = run_joint_process(S,G,C,E, subject=name, vaas_mounted=False)
        rows.append({"field": name, "dual_class": pkt.dual_class, "workable": pkt.workable, "vaas": pkt.vaas["classification"], "type_batch": pkt.type_batch})
    for label, deltas, expect_block in [("vaas_kept",[0.2,0.1,0.05], False),("vaas_pruned",[0.2,-0.1,0.05], True),("vaas_sterile",[], True)]:
        pkt = run_joint_process(0.90,0.85,0.80,0.75, subject=f"handshake_{label}", vaas_mounted=True, vaas_deltas=deltas)
        rows.append({"field": label, "dual_class": pkt.dual_class, "workable": pkt.workable, "vaas": pkt.vaas["classification"], "type_batch": pkt.type_batch})
    return rows

if __name__ == "__main__":
    print(f"=== Joint Process LOCK v{LOCK_VERSION} ===")
    for r in run_lock_suite():
        print(r)
    print("classical_comparative: out_of_scope_for_this_lock")
