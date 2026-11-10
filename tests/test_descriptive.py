import pytest
from hypothesis import given
from hypothesis import strategies as st

from statlite import harmonic_mean, mean, median, mode, stdev, variance

finite = st.floats(min_value=-1e6, max_value=1e6, allow_nan=False)
datasets = st.lists(finite, min_size=2, max_size=50)


def test_mean() -> None:
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd_and_even() -> None:
    assert median([3, 1, 2]) == 2.0
    assert median([4, 1, 3, 2]) == 2.5


def test_mode_breaks_ties_with_smallest() -> None:
    assert mode([2, 2, 1, 1, 3]) == 1.0


def test_variance_and_stdev() -> None:
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert variance(data, ddof=0) == 4.0
    assert stdev(data, ddof=0) == 2.0
    assert variance(data) == pytest.approx(32 / 7)


@pytest.mark.parametrize("func", [mean, median, mode])
def test_empty_input_raises(func: object) -> None:
    with pytest.raises(ValueError, match="at least 1 data point"):
        func([])  # type: ignore[operator]


def test_variance_needs_two_points() -> None:
    with pytest.raises(ValueError, match="at least 2 data points"):
        variance([1])


def test_variance_negative_ddof() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        variance([1, 2], ddof=-1)


def test_harmonic_mean() -> None:
    assert harmonic_mean([1, 4, 4]) == pytest.approx(2.0)


def test_harmonic_mean_rejects_non_positive() -> None:
    with pytest.raises(ValueError, match="strictly positive"):
        harmonic_mean([1, -1])


@given(datasets)
def test_mean_within_bounds(data: list[float]) -> None:
    assert min(data) - 1e-6 <= mean(data) <= max(data) + 1e-6


@given(datasets)
def test_median_within_bounds(data: list[float]) -> None:
    assert min(data) <= median(data) <= max(data)


@given(datasets)
def test_variance_non_negative(data: list[float]) -> None:
    assert variance(data) >= 0


@given(datasets, finite)
def test_variance_shift_invariant(data: list[float], shift: float) -> None:
    shifted = [x + shift for x in data]
    assert variance(shifted) == pytest.approx(variance(data), rel=1e-6, abs=1e-3)
