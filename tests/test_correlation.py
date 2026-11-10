import pytest
from hypothesis import given
from hypothesis import strategies as st

from statlite import covariance, pearson

finite = st.floats(min_value=-1e3, max_value=1e3, allow_nan=False)
pairs = st.lists(st.tuples(finite, finite), min_size=2, max_size=50)


def test_covariance() -> None:
    assert covariance([1, 2, 3], [2, 4, 6]) == 2.0


def test_pearson_perfect_correlation() -> None:
    assert pearson([1, 2, 3], [2, 4, 6]) == pytest.approx(1.0)
    assert pearson([1, 2, 3], [6, 4, 2]) == pytest.approx(-1.0)


def test_length_mismatch() -> None:
    with pytest.raises(ValueError, match="same length"):
        covariance([1, 2, 3], [1, 2])
    with pytest.raises(ValueError, match="same length"):
        pearson([1, 2, 3], [1, 2])


def test_pearson_constant_input() -> None:
    with pytest.raises(ValueError, match="constant"):
        pearson([1, 1, 1], [1, 2, 3])


@given(pairs)
def test_pearson_bounded(data: list[tuple[float, float]]) -> None:
    xs, ys = zip(*data, strict=True)
    try:
        r = pearson(xs, ys)
    except ValueError:
        return
    assert -1.0 <= r <= 1.0
