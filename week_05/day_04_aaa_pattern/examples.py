def apply_discount(price: float, percent: float) -> float:
    return price - price * percent / 100


def test_apply_discount() -> None:
    # Arrange
    price = 200
    percent = 25

    # Act
    result = apply_discount(price, percent)

    # Assert
    assert result == 150
