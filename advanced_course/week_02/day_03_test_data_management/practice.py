# День 3 — Практика: test data management

BASELINE_USER = {
    'email': 'qa@example.com',
    'role': 'user',
    'active': True,
}

ROLE_DATASETS: dict[str, dict[str, object]] = {
    'admin': {},
    'blocked': {},
}

EDGE_TOTALS: list[int] = []


def build_user(**overrides: object) -> dict[str, object]:
    result = dict(BASELINE_USER)
    result.update(overrides)
    return result


def run_checks() -> list[tuple[str, bool]]:
    admin = build_user(**ROLE_DATASETS['admin'])
    blocked = build_user(**ROLE_DATASETS['blocked'])
    return [
        ('admin role', admin.get('role') == 'admin'),
        ('blocked inactive', blocked.get('active') is False),
        ('edge totals contain zero', 0 in EDGE_TOTALS),
        ('edge totals contain upper boundary', 10_000 in EDGE_TOTALS),
        ('edge totals contain invalid over limit', 10_001 in EDGE_TOTALS),
    ]


if __name__ == '__main__':
    print('Заполни reusable datasets и edge values:')
    for name, status in run_checks():
        print(f'{name}: {status}')
