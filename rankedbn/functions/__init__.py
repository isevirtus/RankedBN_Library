# functions/__init__.py
"""
Aggregation functions for ranked nodes in Bayesian Networks.

Includes:
- wmean
- wmin
- wmax
- mixminmax
- mix_and_transform_with_tnormal (mixture)
"""

from .wmean import wmean
from .wmin import wmin
from .wmax import wmax
from .mixminmax import mixminmax
from .mixture import mix_and_transform_with_tnormal

functions = {
    "WMEAN": wmean,
    "WMIN": wmin,
    "WMAX": wmax,
    "MIXMINMAX": mixminmax
}
