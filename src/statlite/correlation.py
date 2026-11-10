"""Measures of association between two variables."""

from __future__ import annotations

import math
from collections.abc import Iterable

from statlite._validation import as_list
from statlite.descriptive import mean


def covariance(x: Iterable[float], y: Iterable[float], ddof: int = 1) -> float:
    """Compute the covariance of two equal-length samples.

    Parameters
    ----------
    x, y : Iterable of float
        The paired samples. Must have the same length, greater than ``ddof``.
    ddof : int, default 1
        Delta degrees of freedom. Use ``1`` for the sample covariance.

    Returns
    -------
    float
        The covariance.

    Raises
    ------
    ValueError
        If the samples differ in length or are too short.

    Examples
    --------
    >>> covariance([1, 2, 3], [2, 4, 6])
    2.0
    """
    xs = as_list(x, minimum=ddof + 1)
    ys = as_list(y, minimum=ddof + 1)
    if len(xs) != len(ys):
        raise ValueError("x and y must have the same length")
    mx, my = mean(xs), mean(ys)
    total = math.fsum((a - mx) * (b - my) for a, b in zip(xs, ys, strict=True))
    return total / (len(xs) - ddof)


def pearson(x: Iterable[float], y: Iterable[float]) -> float:
    """Compute the Pearson correlation coefficient.

    Parameters
    ----------
    x, y : Iterable of float
        The paired samples. Must have the same length, at least 2.

    Returns
    -------
    float
        The correlation, between -1 and 1.

    Raises
    ------
    ValueError
        If the samples differ in length, are too short, or either has zero
        variance.

    Examples
    --------
    >>> pearson([1, 2, 3], [2, 4, 6])
    1.0
    """
    xs = as_list(x, minimum=2)
    ys = as_list(y, minimum=2)
    if len(xs) != len(ys):
        raise ValueError("x and y must have the same length")
    mx, my = mean(xs), mean(ys)
    sxx = math.fsum((a - mx) ** 2 for a in xs)
    syy = math.fsum((b - my) ** 2 for b in ys)
    if sxx == 0 or syy == 0:
        raise ValueError("correlation is undefined for constant input")
    sxy = math.fsum((a - mx) * (b - my) for a, b in zip(xs, ys, strict=True))
    return max(-1.0, min(1.0, sxy / math.sqrt(sxx * syy)))
