class OrderBuilder:
    def __init__(self) -> None:
        self._data = {"amount": 100, "status": "new", "vip": False}

    def with_amount(self, amount: int) -> "OrderBuilder":
        self._data["amount"] = amount
        return self

    def with_status(self, status: str) -> "OrderBuilder":
        self._data["status"] = status
        return self

    def as_vip(self) -> "OrderBuilder":
        self._data["vip"] = True
        return self

    def build(self) -> dict[str, object]:
        return dict(self._data)


if __name__ == "__main__":
    print(OrderBuilder().with_amount(250).with_status("paid").as_vip().build())
