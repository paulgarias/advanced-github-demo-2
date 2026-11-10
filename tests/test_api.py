import statlite


def test_public_api() -> None:
    assert isinstance(statlite.__version__, str)
    for name in statlite.__all__:
        assert hasattr(statlite, name)
