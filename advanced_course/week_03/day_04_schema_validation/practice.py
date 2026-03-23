# День 4 — Практика: schema validation

ORDER_SCHEMA = {
    'required': {'id', 'status', 'total'},
    'status_values': {'new', 'paid', 'cancelled'},
}


def validate_order_schema(payload: dict[str, object]) -> bool:
    if not ORDER_SCHEMA['required'].issubset(payload):
        return False
    return False


def run_checks() -> list[tuple[str, bool]]:
    valid_payload = {'id': 1, 'status': 'paid', 'total': 100}
    missing_field = {'id': 1, 'status': 'paid'}
    invalid_enum = {'id': 1, 'status': 'refunded', 'total': 100}
    wrong_type = {'id': 1, 'status': 'paid', 'total': '100'}
    return [
        ('valid payload accepted', validate_order_schema(valid_payload) is True),
        ('missing field rejected', validate_order_schema(missing_field) is False),
        ('invalid enum rejected', validate_order_schema(invalid_enum) is False),
        ('wrong type rejected', validate_order_schema(wrong_type) is False),
    ]


if __name__ == '__main__':
    print('Добавь type и enum checks:')
    for name, status in run_checks():
        print(f'{name}: {status}')
