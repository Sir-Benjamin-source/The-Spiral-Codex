"""
smurf_base.py

Minimal base class for Smurf Town agents.
Implements residual sensing, host-expression, and tune emission
while remaining strictly within the locked directives.

Draws structural inspiration from mycelial_coherence.py
(DAER-style volatility gating, CARER-style reflection, helix feedback)
but keeps the implementation deliberately lightweight and inspectable.

Authors: Sir Benjamin (vision), Grok (implementation)
Date: 2026-08-08
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from .directives import DIRECTIVES, report_compliance
from .geometry import LocalGeometry
from .residual import ResidualInputs, compute_residual, DeepResidual


@dataclass
class ResidualReport:
    """Lightweight residual and continuity snapshot."""
    smurf_id: str
    timestamp: float
    subject_isolation: float          # approx S
    generality_coherence: float       # approx G
    residual: float                   # combined residual magnitude
    continuity_status: str            # continuous | elevated | discontinuous
    notes: str = ""


@dataclass
class SmurfBase:
    """
    Base residual processor.

    A smurf is attached to a subject (data set, process, or review context).
    It measures continuity residual, expresses the host's coherent state,
    and emits compact status tunes. It never rewrites the host.
    """

    smurf_id: str
    role: str = "general"
    attached_subject: str = ""
    residual_history: List[ResidualReport] = field(default_factory=list)
    active: bool = True
    geometry: Optional[LocalGeometry] = None

    residual_elevated: float = 0.30
    residual_discontinuous: float = 0.55

    _replication_allowed: bool = False
    residual_log_path: Optional[str] = None

    def __post_init__(self):
        if not self.smurf_id:
            raise ValueError("smurf_id is required")
        if self.geometry is None:
            self.geometry = LocalGeometry(smurf_id=self.smurf_id)

    def sense_residual(
        self,
        subject_isolation: float,
        generality_coherence: float,
        notes: str = "",
        instantaneous_coherence: Optional[float] = None,
    ) -> ResidualReport:
        deep: DeepResidual = compute_residual(
            ResidualInputs(
                S=subject_isolation,
                G=generality_coherence,
                C=instantaneous_coherence,
            )
        )

        report = ResidualReport(
            smurf_id=self.smurf_id,
            timestamp=time.time(),
            subject_isolation=deep.S,
            generality_coherence=deep.G,
            residual=deep.residual,
            continuity_status=deep.status,
            notes=notes or (f"kind={deep.kind} gated={deep.gated}"),
        )
        self.residual_history.append(report)
        self._append_residual_log(report)

        node_id = f"meas-{len(self.residual_history)}"
        self.geometry.add_node(node_id, kind=deep.kind, residual=deep.residual)

        return report

    def express_host(self) -> Dict[str, Any]:
        latest = self.residual_history[-1] if self.residual_history else None
        return {
            "smurf_id": self.smurf_id,
            "role": self.role,
            "attached_subject": self.attached_subject,
            "active": self.active,
            "directives_compliance": report_compliance(),
            "replication_allowed": self._replication_allowed,
            "latest_residual": {
                "value": latest.residual if latest else None,
                "status": latest.continuity_status if latest else "unknown",
                "S_approx": latest.subject_isolation if latest else None,
                "G_approx": latest.generality_coherence if latest else None,
            } if latest else None,
            "history_length": len(self.residual_history),
            "geometry_summary": self.geometry.summary() if self.geometry else None,
        }

    def emit_tune(self, message: str = "") -> Dict[str, Any]:
        latest = self.residual_history[-1] if self.residual_history else None
        return {
            "from": self.smurf_id,
            "role": self.role,
            "status": latest.continuity_status if latest else "uninitialized",
            "residual": round(latest.residual, 4) if latest else None,
            "message": message or "status",
            "timestamp": time.time(),
        }

    def check_directives(self) -> Dict[str, bool]:
        return report_compliance()

    def is_continuous(self) -> bool:
        if not self.residual_history:
            return False
        return self.residual_history[-1].continuity_status == "continuous"

    def allow_replication(self, authorized: bool = False) -> None:
        self._replication_allowed = bool(authorized)

    def can_replicate(self) -> bool:
        return self._replication_allowed

    def _append_residual_log(self, report: ResidualReport) -> None:
        if not self.residual_log_path:
            return
        path = Path(self.residual_log_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        entry = {
            "smurf_id": report.smurf_id,
            "timestamp": report.timestamp,
            "subject_isolation": report.subject_isolation,
            "generality_coherence": report.generality_coherence,
            "residual": report.residual,
            "continuity_status": report.continuity_status,
            "notes": report.notes,
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    def __repr__(self) -> str:
        status = "uninitialized"
        if self.residual_history:
            status = self.residual_history[-1].continuity_status
        return f"<Smurf {self.smurf_id} role={self.role} status={status}>"
