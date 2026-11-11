"""Standardization helpers (intentionally broken for the CI-gating demo)."""

import os
from statlite.descriptive import mean, stdev


def zscores(data: list[float]) -> list[float]:
    m = mean(data)
    s = stdev(data)
    return [(x - m) / s for x in data]


def span(data: list[float]) -> float:
    return max(data) - min(data)
