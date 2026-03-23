# День 6 — Практика: reusable datasets

USER_DATASETS: dict[str, dict[str, object]] = {
    'valid_user': {},
    'blocked_user': {},
}

ORDER_STATUSES: list[str] = []
VIP_CUSTOMER_TYPES: list[str] = []


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('valid_user has active true', USER_DATASETS['valid_user'].get('active') is True),
        ('blocked_user has active false', USER_DATASETS['blocked_user'].get('active') is False),
        ('statuses contain new', 'new' in ORDER_STATUSES),
        ('statuses contain paid', 'paid' in ORDER_STATUSES),
        ('statuses contain cancelled', 'cancelled' in ORDER_STATUSES),
        ('vip dataset not empty', len(VIP_CUSTOMER_TYPES) >= 1),
    ]


if __name__ == '__main__':
    print('Заполни reusable datasets:')
    for name, status in run_checks():
        print(f'{name}: {status}')
