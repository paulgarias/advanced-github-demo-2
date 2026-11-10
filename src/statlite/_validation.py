"""Input validation helpers shared across :mod:`statlite`."""

from __future__ import annotations

from collections.abc import Iterable


def as_list(data: Iterable[float], *, minimum: int = 1) -> list[float]:
    """Materialize ``data`` as a list and check it has enough points.

    Parameters
    ----------
    data : Iterable of float
        The input values.
    minimum : int, default 1
        The minimum number of data points required.

    Returns
    -------
    list of float
        The values as a list of floats.

    Raises
    ------
    ValueError
        If fewer than ``minimum`` values are supplied.
    """
    values = [float(x) for x in data]
    if len(values) < minimum:
        noun = "data point" if minimum == 1 else "data points"
        raise ValueError(f"at least {minimum} {noun} required, got {len(values)}")
    return values
