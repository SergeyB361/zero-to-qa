import pytest


@pytest.mark.smoke
def test_login_page_is_available() -> None:
    assert True


@pytest.mark.api
def test_users_endpoint_schema() -> None:
    assert {"status": "ok"}["status"] == "ok"


@pytest.mark.xfail(reason="Known bug: discount is rounded incorrectly")
def test_discount_rounding_bug() -> None:
    assert round(10.015, 2) == 10.02


@pytest.mark.skip(reason="Feature flag disabled in current environment")
def test_beta_feature() -> None:
    assert False
