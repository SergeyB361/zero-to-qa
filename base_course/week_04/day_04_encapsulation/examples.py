# Неделя 4, День 4 — Примеры


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = 0.0
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value


if __name__ == "__main__":
    product = Product("Keyboard", 99.9)
    print(product.price)

    product.price = 120.0
    print(product.price)
