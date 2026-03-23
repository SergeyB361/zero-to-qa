class OrdersClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_order(self, order_id: int) -> tuple[str, int]:
        return f'{self.base_url}/orders/{order_id}', 200


def assert_ok(status_code: int) -> bool:
    return status_code == 200


if __name__ == '__main__':
    client = OrdersClient('https://api.example.com')
    url, status = client.get_order(1)
    print(url)
    print(assert_ok(status))
