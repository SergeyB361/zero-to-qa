import pytest

def is_even(number: int) -> bool:
    return number % 2 == 0

@pytest.mark.parametrize("value, expected", [(2, True), (3, False), (10, True)])
def test_is_even(value: int, expected: bool) -> None:
    assert is_even(value) is expected
