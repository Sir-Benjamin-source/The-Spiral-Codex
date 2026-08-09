from .smurf_base import SmurfBase, ResidualReport
from .directives import DIRECTIVES, report_compliance
from .geometry import LocalGeometry, AssociationNode
from .residual import (
    ResidualInputs,
    DeepResidual,
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
from .validity import (
    ValidityResult,
    assess_validity,
    assess_multi_config_validity,
    residual_to_validity,
)

__all__ = [
    "SmurfBase",
    "ResidualReport",
    "DIRECTIVES",
    "report_compliance",
    "LocalGeometry",
    "AssociationNode",
    "ResidualInputs",
    "DeepResidual",
    "compute_residual",
    "multi_config_residual",
    "aggregate_multi_config",
    "compare_to_baselines",
    "CONTINUOUS_MAX",
    "ELEVATED_MAX",
    "BASELINE_STRONG",
    "BASELINE_GOOD",
    "BASELINE_ACCEPTABLE",
    "ValidityResult",
    "assess_validity",
    "assess_multi_config_validity",
    "residual_to_validity",
]
