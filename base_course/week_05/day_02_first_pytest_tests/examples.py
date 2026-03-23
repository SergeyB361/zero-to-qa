# Неделя 5, День 2 — Примеры


def is_even(number: int) -> bool:
    return number % 2 == 0


def test_is_even() -> None:
    assert is_even(4) is True


if __name__ == "__main__":
    print(is_even(10))
