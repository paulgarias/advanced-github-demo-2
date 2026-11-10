"""Descriptive statistics: measures of center and spread."""

from __future__ import annotations

import math
from collections import Counter
from collections.abc import Iterable

from statlite._validation import as_list


def mean(data: Iterable[float]) -> float:
    """Compute the arithmetic mean.

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain at least one value.

    Returns
    -------
    float
        The arithmetic mean.

    Raises
    ------
    ValueError
        If ``data`` is empty.

    Examples
    --------
    >>> mean([1, 2, 3, 4])
    2.5
    """
    values = as_list(data)
    return math.fsum(values) / len(values)


def median(data: Iterable[float]) -> float:
    """Compute the median.

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain at least one value.

    Returns
    -------
    float
        The middle value, or the mean of the two middle values.

    Raises
    ------
    ValueError
        If ``data`` is empty.

    Examples
    --------
    >>> median([3, 1, 2])
    2.0
    >>> median([4, 1, 3, 2])
    2.5
    """
    values = sorted(as_list(data))
    mid, odd = divmod(len(values), 2)
    if odd:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2


def mode(data: Iterable[float]) -> float:
    """Compute the most common value.

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain at least one value.

    Returns
    -------
    float
        The most frequent value. Ties are broken by the smallest value.

    Raises
    ------
    ValueError
        If ``data`` is empty.

    Examples
    --------
    >>> mode([1, 2, 2, 3])
    2.0
    >>> mode([1, 1, 2, 2])
    1.0
    """
    counts = Counter(as_list(data))
    top = max(counts.values())
    return min(value for value, count in counts.items() if count == top)


def variance(data: Iterable[float], ddof: int = 1) -> float:
    """Compute the variance.

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain more than ``ddof`` values.
    ddof : int, default 1
        Delta degrees of freedom. Use ``1`` for the sample variance and ``0``
        for the population variance.

    Returns
    -------
    float
        The variance.

    Raises
    ------
    ValueError
        If there are not more than ``ddof`` values, or ``ddof`` is negative.

    Examples
    --------
    >>> variance([1, 2, 3, 4])
    1.6666666666666667
    >>> variance([1, 2, 3, 4], ddof=0)
    1.25
    """
    if ddof < 0:
        raise ValueError("ddof must be non-negative")
    values = as_list(data, minimum=ddof + 1)
    center = mean(values)
    return math.fsum((x - center) ** 2 for x in values) / (len(values) - ddof)


def stdev(data: Iterable[float], ddof: int = 1) -> float:
    """Compute the standard deviation.

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain more than ``ddof`` values.
    ddof : int, default 1
        Delta degrees of freedom. See :func:`variance`.

    Returns
    -------
    float
        The standard deviation, the square root of :func:`variance`.

    Examples
    --------
    >>> stdev([2, 4, 4, 4, 5, 5, 7, 9], ddof=0)
    2.0
    """
    return math.sqrt(variance(data, ddof=ddof))


def geometric_mean(data: Iterable[float]) -> float:
    """Compute the geometric mean.

    Parameters
    ----------
    data : Iterable of float
        The input values. All values must be strictly positive.

    Returns
    -------
    float
        The geometric mean.

    Raises
    ------
    ValueError
        If ``data`` is empty or contains a non-positive value.

    Examples
    --------
    >>> round(geometric_mean([1, 4]), 6)
    2.0
    """
    values = as_list(data)
    if any(x <= 0 for x in values):
        raise ValueError("geometric mean requires strictly positive values")
    return math.exp(math.fsum(math.log(x) for x in values) / len(values))
