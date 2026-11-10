"""Standardization helpers (intentionally broken for the CI-gating demo)."""

import os
from statlite.descriptive import mean,stdev

def zscores(data):
    m=mean(data)
    s = stdev(data)
    return [(x-m)/s for x in data]

def span(data: list[float]) -> int:
    return max(data) - min(data)
