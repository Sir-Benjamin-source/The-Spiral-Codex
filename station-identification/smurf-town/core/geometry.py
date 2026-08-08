"""
geometry.py

Light structural mapping inspired by mycelial / mushroom configurations.
Provides a simple formal description of association structure
without introducing autonomous growth or override behavior.

This module is optional for basic residual work. It exists so that
a smurf can, if desired, describe its internal association geometry
in terms consistent with the earlier fungal-inspired experiments
and with mycelial_coherence.py.

Authors: Sir Benjamin (vision), Grok (implementation)
Date: 2026-08-08
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class AssociationNode:
    """Minimal node in a local association geometry."""
    node_id: str
    kind: str = "which"          # "that" (essential) or "which" (additive)
    residual_contribution: float = 0.0
    linked: List[str] = field(default_factory=list)


@dataclass
class LocalGeometry:
    """
    Compact description of a smurf's current association structure.
    Kept deliberately small and inspectable.
    """
    smurf_id: str
    nodes: Dict[str, AssociationNode] = field(default_factory=dict)
    center: Optional[str] = None          # essential ("that") node if present

    def add_node(self, node_id: str, kind: str = "which", residual: float = 0.0) -> None:
        self.nodes[node_id] = AssociationNode(
            node_id=node_id,
            kind=kind,
            residual_contribution=residual,
        )
        if kind == "that" and self.center is None:
            self.center = node_id

    def link(self, a: str, b: str) -> None:
        if a in self.nodes and b in self.nodes:
            if b not in self.nodes[a].linked:
                self.nodes[a].linked.append(b)
            if a not in self.nodes[b].linked:
                self.nodes[b].linked.append(a)

    def summary(self) -> Dict:
        that_count = sum(1 for n in self.nodes.values() if n.kind == "that")
        which_count = sum(1 for n in self.nodes.values() if n.kind == "which")
        avg_residual = (
            sum(n.residual_contribution for n in self.nodes.values()) / len(self.nodes)
            if self.nodes else 0.0
        )
        return {
            "smurf_id": self.smurf_id,
            "node_count": len(self.nodes),
            "that_nodes": that_count,
            "which_nodes": which_count,
            "center": self.center,
            "avg_residual_contribution": round(avg_residual, 4),
        }
