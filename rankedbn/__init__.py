"""
rankedbn: A library for building and validating ranked-node functions
in Bayesian Networks using formally verified mathematical implementations.

Modules:
- network: Base class for Bayesian network creation.
- functions: Mathematical aggregation functions.
- evaluation: Validation tools and pre-defined test scenarios.
- utils: Auxiliary tools (e.g., data loading).
"""

from . import network
from . import functions
from . import evaluation
from . import utils
from .genetic.genetic_algorithm import run_ga_optimization
