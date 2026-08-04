#!/usr/bin/env python3
"""
Parallel Differential Examination Form — Minimal Reference Implementation

Location: The-Spiral-Codex/station-identification/meta-standards/
Status: Thin, mountable reference. Not a full examination engine.

This module implements the fully grounded parallel differential form:

    dA/dt = S * G * E - λ_A * (1 - C)
    dP/dt = S * (1 - G) * E + λ_P * (1 - C)

subject to λ_A + λ_P = Λ.

All variables are defined under the six-clause meta-standard
(see sibling .md files in this folder). This file provides only the
core arithmetic so that other agents or surfaces (Builder, Elucidation,
head-to-head, etc.) can pull a clean, dependency-light implementation.

The AI uses the software; the software does not use the AI.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class DualRates:
    """Coupled damping rates under the boundedness constraint."""
    lambda_a: float
    lambda_p: float
    Lambda: float  # total responsiveness

    def __post_init__(self):
        if self.lambda_a < 0 or self.lambda_p < 0:
            raise ValueError("Damping rates must be non-negative")
        if abs((self.lambda_a + self.lambda_p) - self.Lambda) > 1e-9:
            raise ValueError("lambda_a + lambda_p must equal Lambda")

    @classmethod
    def from_balance(cls, Lambda: float = 0.30, gamma: float = 0.5) -> "DualRates":
        """Create rates from total responsiveness and balance parameter."""
        if not 0.0 <= gamma <= 1.0:
            raise ValueError("gamma must be in [0, 1]")
        if Lambda <= 0:
            raise ValueError("Lambda must be positive")
        return cls(
            lambda_a=gamma * Lambda,
            lambda_p=(1.0 - gamma) * Lambda,
            Lambda=Lambda,
        )


@dataclass
class ExaminationState:
    """Snapshot of the five grounded variables."""
    S: float  # Subject Isolation Strength [0, 1]
    G: float  # Generality Expansion [0, 1]
    E: float  # Etymological Descent [0, 1]
    C: float  # Instantaneous Coherence [0, 1]
    rates: DualRates

    def __post_init__(self):
        for name, val in [("S", self.S), ("G", self.G), ("E", self.E), ("C", self.C)]:
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"{name} must be in [0, 1], got {val}")


@dataclass
class TrajectoryResult:
    """Instantaneous rates and derived quantities."""
    dA_dt: float
    dP_dt: float
    sum_AP: float      # informativeness
    diff_AP: float     # separation quality (A - P)

    def as_dict(self):
        return {
            "dA/dt": self.dA_dt,
            "dP/dt": self.dP_dt,
            "A+P": self.sum_AP,
            "A-P": self.diff_AP,
        }


def compute_trajectories(state: ExaminationState) -> TrajectoryResult:
    """
    Compute the parallel differential trajectories.

    Actionable:   dA/dt = S * G * E - λ_A * (1 - C)
    Paradox:      dP/dt = S * (1 - G) * E + λ_P * (1 - C)
    """
    S, G, E, C = state.S, state.G, state.E, state.C
    la, lp = state.rates.lambda_a, state.rates.lambda_p

    dA = (S * G * E) - la * (1.0 - C)
    dP = (S * (1.0 - G) * E) + lp * (1.0 - C)

    return TrajectoryResult(
        dA_dt=dA,
        dP_dt=dP,
        sum_AP=dA + dP,
        diff_AP=dA - dP,
    )


def quick_eval(
    S: float,
    G: float,
    E: float,
    C: float,
    Lambda: float = 0.30,
    gamma: float = 0.5,
) -> TrajectoryResult:
    """Convenience wrapper with default dual-rate balance."""
    rates = DualRates.from_balance(Lambda=Lambda, gamma=gamma)
    state = ExaminationState(S=S, G=G, E=E, C=C, rates=rates)
    return compute_trajectories(state)


if __name__ == "__main__":
    # Minimal self-test / demonstration
    result = quick_eval(S=0.80, G=0.65, E=0.70, C=0.75)
    print("Parallel Differential — reference evaluation")
    print(f"  dA/dt (Actionable) : {result.dA_dt:.4f}")
    print(f"  dP/dt (Paradox)    : {result.dP_dt:.4f}")
    print(f"  A+P (informative)  : {result.sum_AP:.4f}")
    print(f"  A-P (separation)   : {result.diff_AP:.4f}")
