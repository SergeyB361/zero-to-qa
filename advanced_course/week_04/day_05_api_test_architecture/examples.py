class OrdersClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def order_url(self, order_id: int) -> str:
        return f"{self.base_url}/orders/{order_id}"


def build_order_payload(total: int) -> dict[str, int]:
    return {"total": total}


if __name__ == "__main__":
    client = OrdersClient("https://api.example.com")
    print(client.order_url(10))
    print(build_order_payload(200))
