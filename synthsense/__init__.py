"""SynthSense: A novel reward function for REINVENT based on retrosynthetic analysis.

This package provides multiple scoring endpoints for molecular generation:
- SFScore: Synthesis feasibility score
- RRScore: Reference route similarity
- Route Popularity: Encourages diverse synthesis routes
- Fill-a-Plate: Promotes route diversity through bucketing
- Route Similarity: Measures synthesis route similarity
"""

__version__ = "1.0.0"
__author__ = "AZCollaboration"

from .comp_synthsense import synthsense
from .endpoints import (
    SFScore,
    RRScore,
    RoutePopularityEndpoint,
    FillaPlate,
    RouteSimilarityEndpoint,
    NumberOfReactionsEndpoint,
)
from .parameters import Parameters

__all__ = [
    "synthsense",
    "SFScore",
    "RRScore",
    "RoutePopularityEndpoint",
    "FillaPlate",
    "RouteSimilarityEndpoint",
    "NumberOfReactionsEndpoint",
    "Parameters",
]

