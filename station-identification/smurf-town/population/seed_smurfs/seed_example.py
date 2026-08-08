"""
seed_example.py

Minimal first-generation seed instances.
These are illustrative only; they demonstrate role differentiation
while remaining fully compliant with the locked directives.
"""

from core.smurf_base import SmurfBase


def create_seed_population() -> list:
    """Return a small set of seed smurfs with distinct roles."""
    seeds = [
        SmurfBase(
            smurf_id="smurf-continuity-001",
            role="continuity",
            attached_subject="station-identification",
        ),
        SmurfBase(
            smurf_id="smurf-generality-001",
            role="generality",
            attached_subject="meta-standards-G",
        ),
        SmurfBase(
            smurf_id="smurf-station-001",
            role="station",
            attached_subject="floating-review-sheet",
        ),
    ]
    return seeds


if __name__ == "__main__":
    population = create_seed_population()
    for s in population:
        report = s.sense_residual(
            subject_isolation=0.82,
            generality_coherence=0.75,
            notes="seed initialization",
        )
        print(s)
        print("  residual:", report.residual, report.continuity_status)
        print("  tune:", s.emit_tune("seed ready"))
        print()
