import pytest

@pytest.mark.smoke
def test_homepage_is_available() -> None:
    assert True

@pytest.mark.skip(reason="Фича еще не реализована")
def test_future_feature() -> None:
    assert False

@pytest.mark.xfail(reason="Известный дефект", strict=False)
def test_known_bug() -> None:
    assert 1 == 2
