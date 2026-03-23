# День 3 — Практика: stateful scenarios

TRANSITIONS = {
    'new': {'pay': 'paid', 'cancel': 'cancelled'},
    'paid': {'refund': 'refunded'},
    'cancelled': {},
}


def next_state(current: str, event: str) -> str | None:
    return None


def is_allowed(current: str, event: str) -> bool:
    return False


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('new -> pay allowed', is_allowed('new', 'pay') is True),
        ('new -> pay to paid', next_state('new', 'pay') == 'paid'),
        ('paid -> refund allowed', is_allowed('paid', 'refund') is True),
        ('paid -> cancel forbidden', is_allowed('paid', 'cancel') is False),
        ('cancelled -> pay forbidden', next_state('cancelled', 'pay') is None),
    ]


if __name__ == '__main__':
    print('Опиши allowed и disallowed transitions:')
    for name, status in run_checks():
        print(f'{name}: {status}')
