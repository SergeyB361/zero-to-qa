import pytest


@pytest.mark.parametrize(
    "total,is_vip,expected",
    [
        pytest.param(100, False, 100, id="regular"),
        pytest.param(100, True, 90, id="vip"),
        pytest.param(200, True, 180, id="vip-large"),
    ],
)
def test_discount(total: int, is_vip: bool, expected: int) -> None:
    actual = total - 10 if is_vip else total
    assert actual == expected


@pytest.mark.parametrize(
    "status,expected",
    [
        pytest.param("draft", False, id="draft-hidden"),
        pytest.param("published", True, id="published-visible", marks=pytest.mark.smoke),
    ],
)
def test_visibility(status: str, expected: bool) -> None:
    assert (status == "published") is expected
