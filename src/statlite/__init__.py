"""statlite: a small, dependency-free statistics library."""

from __future__ import annotations

from statlite.correlation import covariance, pearson
from statlite.descriptive import harmonic_mean, mean, median, mode, stdev, variance
from statlite.quantiles import iqr, percentile

try:
    from statlite._version import __version__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"

__all__ = [
    "__version__",
    "covariance",
    "harmonic_mean",
    "iqr",
    "mean",
    "median",
    "mode",
    "pearson",
    "percentile",
    "stdev",
    "variance",
]
