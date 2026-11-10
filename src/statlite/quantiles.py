"""Quantile-based statistics."""

from __future__ import annotations

from collections.abc import Iterable

from statlite._validation import as_list


def percentile(data: Iterable[float], q: float) -> float:
    """Compute the ``q``-th percentile using linear interpolation.

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain at least one value.
    q : float
        The percentile to compute, between 0 and 100 inclusive.

    Returns
    -------
    float
        The interpolated percentile.

    Raises
    ------
    ValueError
        If ``data`` is empty or ``q`` is outside ``[0, 100]``.

    Examples
    --------
    >>> percentile([1, 2, 3, 4, 5], 50)
    3.0
    >>> percentile([1, 2, 3, 4], 25)
    1.75
    """
    if not 0 <= q <= 100:
        raise ValueError("q must be between 0 and 100")
    values = sorted(as_list(data))
    position = (len(values) - 1) * q / 100
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)
    fraction = position - lower
    return values[lower] + (values[upper] - values[lower]) * fraction


def iqr(data: Iterable[float]) -> float:
    """Compute the interquartile range (75th minus 25th percentile).

    Parameters
    ----------
    data : Iterable of float
        The input values. Must contain at least one value.

    Returns
    -------
    float
        The interquartile range.

    Examples
    --------
    >>> iqr([1, 2, 3, 4, 5])
    2.0
    """
    values = as_list(data)
    return percentile(values, 75) - percentile(values, 25)
