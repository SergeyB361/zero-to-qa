class OrderBuilder:
    def __init__(self) -> None:
        self._data = {
            'total': 100,
            'status': 'new',
            'currency': 'RUB',
            'tags': [],
        }

    def with_total(self, total: int) -> 'OrderBuilder':
        self._data['total'] = total
        return self

    def with_status(self, status: str) -> 'OrderBuilder':
        self._data['status'] = status
        return self

    def add_tag(self, tag: str) -> 'OrderBuilder':
        self._data['tags'] = [*self._data['tags'], tag]
        return self

    def build(self) -> dict[str, object]:
        return dict(self._data)


if __name__ == '__main__':
    order = OrderBuilder().with_total(250).with_status('paid').add_tag('smoke').build()
    print(order)
