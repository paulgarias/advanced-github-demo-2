import pytest
from hypothesis import given
from hypothesis import strategies as st

from statlite import iqr, percentile

finite = st.floats(min_value=-1e6, max_value=1e6, allow_nan=False)


def test_percentile_known_values() -> None:
    data = [1, 2, 3, 4, 5]
    assert percentile(data, 0) == 1.0
    assert percentile(data, 50) == 3.0
    assert percentile(data, 100) == 5.0
    assert percentile([1, 2, 3, 4], 25) == 1.75


def test_percentile_single_value() -> None:
    assert percentile([7], 30) == 7.0


@pytest.mark.parametrize("q", [-1, 100.1])
def test_percentile_invalid_q(q: float) -> None:
    with pytest.raises(ValueError, match="between 0 and 100"):
        percentile([1, 2, 3], q)


def test_iqr() -> None:
    assert iqr([1, 2, 3, 4, 5]) == 2.0


@given(st.lists(finite, min_size=1, max_size=50), st.floats(0, 100))
def test_percentile_within_bounds(data: list[float], q: float) -> None:
    assert min(data) <= percentile(data, q) <= max(data)
