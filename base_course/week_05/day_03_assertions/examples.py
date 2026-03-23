import pytest


def divide(a: int, b: int) -> float:
    return a / b


def test_divide_result() -> None:
    assert divide(8, 2) == 4


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
