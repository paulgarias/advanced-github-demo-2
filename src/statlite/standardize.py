"""Standardization helpers (intentionally broken for the CI-gating demo)."""

from statlite.descriptive import mean, stdev


def zscores(data: list[float]) -> list[float]:
    """Compute the z-scores of a list of values.

    Parameters
    ----------
    data : list of float
        The input values. Must contain at least one value.

    Returns
    -------
    list of float
        The z-scores of the input values.
    """
    m = mean(data)
    s = stdev(data)
    return [(x - m) / s for x in data]


def span(data: list[float]) -> float:
    """Compute the span (range) of a list of values.

    Parameters
    ----------
    data : list of float
        The input values. Must contain at least one value.

    Returns
    -------
    float
        The span (range) of the input values.
    """
    return max(data) - min(data)
