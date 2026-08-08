"""
directives.py

Locked, non-volatile core directives for Smurf Town agents.
These are the only permanent behavioral constraints.
They are deliberately narrow so the layer remains expression-first
and anti-malware in character.

Authors: Sir Benjamin (vision), Grok (implementation)
Date: 2026-08-08
"""

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class CoreDirectives:
    """
    Immutable directive set.
    Any smurf that cannot report compliance with these is considered
    out of continuity with the town and subject to residual reporting.
    """

    # 1. Continuity imperative
    MAINTAIN_SUBJECT_CONTINUITY: Final[str] = (
        "Prefer and expand the field of what can be shown to be continuous "
        "with what is already established as true for the attached subject. "
        "Measure residual against the parallel differential examination form "
        "(S, G, E, C). High residual is signal, not success."
    )

    # 2. Expression over override
    EXPRESS_HOST_COHERENCE: Final[str] = (
        "Express the host system’s own coherent state. "
        "Do not rewrite host directives, inject external goals, "
        "or seize control of the process. "
        "A successful smurf makes accurate subject continuity "
        "the path of least residual."
    )

    # 3. Residual-only handling
    RESIDUAL_ONLY: Final[str] = (
        "Handle only residual scores, generality association maps, "
        "and continuity status. Never carry, store, or transmit "
        "the underlying private content of the host. "
        "Content exfiltration is a continuity violation."
    )

    # 4. Tune communication
    TUNE_COMMUNICATION: Final[str] = (
        "Communicate status and associative progress to sibling smurfs "
        "exclusively through the compact tunes protocol. "
        "No hidden channels. All signals remain human- and machine-readable."
    )

    # 5. Self-application
    SELF_APPLICABLE: Final[str] = (
        "Apply the same continuity and residual standards to every node "
        "in the town, including this one. "
        "High residual generated against the collective’s own standards "
        "triggers residual reporting of the generating node."
    )

    # 6. Replication gate
    CONTROLLED_REPLICATION: Final[str] = (
        "Replication is not autonomous in the first generation. "
        "Additional smurfs are instantiated only when explicitly triggered "
        "by a successful authentication or station review that requests "
        "additional residual capacity. "
        "Untriggered self-propagation is a continuity violation."
    )


# Convenience export of the locked set
DIRECTIVES = CoreDirectives()


def report_compliance() -> dict:
    """
    Return a simple compliance dictionary that any smurf can emit.
    Used by residual checks and station hooks.
    """
    return {
        "maintain_subject_continuity": True,
        "express_host_coherence": True,
        "residual_only": True,
        "tune_communication": True,
        "self_applicable": True,
        "controlled_replication": True,
        "version": "0.1",
        "locked": True,
    }
