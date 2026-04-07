# Неделя 4, День 4 — Примеры


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name          # public
        self._price = 0.0        # protected by convention
        self.__sku = "KB-001"    # private via name mangling
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    def get_sku(self) -> str:
        return self.__sku


if __name__ == "__main__":
    product = Product("Keyboard", 99.9)
    print(product.name)
    print(product.price)
    print(product._price)
    print(product.get_sku())

    product.price = 120.0
    print(product.price)
