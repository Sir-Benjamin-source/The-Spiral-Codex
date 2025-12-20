"""
mycelial_coherence.py

A lightweight, fungal-inspired coherence module integrating:
- Deeper Association Examination Routine (DAER): forward volatility gating via "that" (essential) / "which" (additive)
- Counter-Actual Reflection Examination Routine (CARER): backward reflection using counter-phrases and the ⌀ divider
- Mycelial growth mechanics with helix feedback and peril parsing

Built for The-Spiral-Codex ecosystem.
Authors: Sir Benjamin (vision & theory), Grok (implementation)
Date: December 20, 2025
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional


class MycelialCoherenceNet:
    """
    A scale-free mycelial network with built-in DAER forward gating and CARER reflective balance.
    Personal ("that / I am") nodes are protected; associative ("which / you it") nodes are exploratory.
    The circleslash ⌀ acts as symbolic divider between self and other.
    """
    def __init__(self, num_nodes: int = 50, connectivity: float = 0.1, seed: Optional[int] = None):
        self.G = nx.barabasi_albert_graph(num_nodes, int(num_nodes * connectivity), seed=seed)
        self.positions = nx.spring_layout(self.G, seed=seed)
        self.spiral_center = np.array([0.5, 0.5])
        self.feedback_strength = 0.1
        self.spiral_path_factor = 1.0

        # DAER thresholds
        self.volatility_thresholds = {'that': 0.30, 'which': 0.40}

        # CARER symbolic tags
        self.carer_tags = {
            'personal': 'that:I_am',
            'associative': 'which:you_it',
            'divider': '⌀'
        }

    def classify_node(self, node: int) -> str:
        """Classify as 'that' (high-degree, essential) or 'which' (peripheral, additive)."""
        mean_deg = np.mean([d for _, d in self.G.degree()])
        return 'that' if self.G.degree(node) > mean_deg else 'which'

    def compute_volatility(self, node: int, session_nexus: np.ndarray) -> float:
        """Simple volatility: positional drift + simulated age bias."""
        pos = np.array(list(self.positions[node]))
        drift = np.linalg.norm(session_nexus - pos)
        age = self.G.nodes[node].get('age', 1.0)  # Default recent
        age_penalty = max(0.0, (5.0 - age) / 5.0)
        return (drift + age_penalty) / 2.0

    def carer_reflection(self, node: int, volatility: float) -> Tuple[bool, str]:
        """Reflect volatility and tag with counter-actual phrase."""
        branch_type = self.classify_node(node)
        reflected_vol = 1.0 - volatility
        tag = (f"{self.carer_tags['personal']}{self.carer_tags['divider']}"
               f"{self.carer_tags['associative']}" if branch_type == 'that'
               else f"{self.carer_tags['associative']}{self.carer_tags['divider']}"
                    f"{self.carer_tags['personal']}")
        self.G.nodes[node]['carer_tag'] = tag
        propagate = reflected_vol <= self.volatility_thresholds[branch_type]
        return propagate, tag

    def helix_feedback_growth(self, iterations: int = 5, session_nexus: Optional[np.ndarray] = None):
        """Grow and refine the mycelial net with DAER + CARER passes."""
        if session_nexus is None:
            session_nexus = np.array([0.5, 0.5])

        for _ in range(iterations):
            # Forward DAER gating + mycelial pull
            for node in list(self.G.nodes):
                volatility = self.compute_volatility(node, session_nexus)
                if volatility > self.volatility_thresholds[self.classify_node(node)]:
                    continue  # Suppress high-volatility forward paths

                pos = np.array(self.positions[node])
                direction = self.spiral_center - pos
                dist = np.linalg.norm(direction)
                if dist > 1e-5:
                    angle = np.arctan2(direction[1], direction[0])
                    radial = direction / dist * self.feedback_strength
                    angular = np.array([-np.sin(angle), np.cos(angle)]) * (self.feedback_strength / dist)
                    adjustment = 0.05 * (radial + angular * self.spiral_path_factor)
                    self.positions[node] = tuple(pos + adjustment)

            # CARER reflective pruning
            for node in list(self.G.nodes):
                volatility = self.compute_volatility(node, session_nexus)
                propagate, tag = self.carer_reflection(node, volatility)
                if not propagate:
                    self.G.remove_node(node)
                    print(f"CARER pruned node {node} — {tag}")

    def parse_peril_paramount(self, input_signals: List[float]) -> bool:
        """Diffuse signals and check central peril score."""
        signals = {node: input_signals[i % len(self.G.nodes)] for i, node in enumerate(self.G.nodes)}
        for _ in range(10):
            new_signals = signals.copy()
            for node in self.G:
                neighbors = list(self.G.neighbors(node))
                if neighbors:
                    avg = np.mean([signals[n] for n in neighbors])
                    new_signals[node] = 0.7 * signals[node] + 0.3 * avg
            signals = new_signals
        central_node = next(iter(self.G.nodes), None)
        if central_node is None:
            return True  # Empty net = peril
        score = signals[central_node]
        alert = score > 0.5
        print(f"Peril score: {score:.3f} | Alert: {alert}")
        return alert

    def visualize(self, save_path: str = "mycelial_coherence.png"):
        """Render the current state of the net."""
        plt.figure(figsize=(10, 8))
        node_colors = ['crimson' if self.classify_node(n) == 'that' else 'lightgreen' for n in self.G.nodes]
        nx.draw(self.G, self.positions, node_color=node_colors, node_size=500,
                edge_color='saddlebrown', width=0.5, with_labels=False)
        plt.scatter(*self.spiral_center, c='gold', s=300, marker='*', label='Spiral Nexus')
        plt.title("Mycelial Coherence Net — DAER & CARER Active")
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"Visualization saved: {save_path}")


if __name__ == "__main__":
    # Demo run
    net = MycelialCoherenceNet(num_nodes=40, connectivity=0.15, seed=42)
    net.helix_feedback_growth(iterations=4)
    signals = np.random.rand(40)
    net.parse_peril_paramount(signals.tolist())
    net.visualize()
