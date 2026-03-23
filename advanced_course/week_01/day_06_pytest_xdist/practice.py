# День 6 — Практика: pytest-xdist

SCENARIOS = {
    'read_only_search': 'safe',
    'checkout_with_shared_account': 'unsafe',
    'profile_edit_with_unique_user': 'safe',
    'delete_shared_order': 'unsafe',
}


def safe_for_parallel() -> list[str]:
    return sorted(name for name, state in SCENARIOS.items() if state == 'safe')


def unsafe_for_parallel() -> list[str]:
    return sorted(name for name, state in SCENARIOS.items() if state == 'unsafe')


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('safe list contains read only test', 'read_only_search' in safe_for_parallel()),
        ('safe list contains isolated user', 'profile_edit_with_unique_user' in safe_for_parallel()),
        ('unsafe list contains shared account case', 'checkout_with_shared_account' in unsafe_for_parallel()),
        ('unsafe list contains destructive case', 'delete_shared_order' in unsafe_for_parallel()),
    ]


if __name__ == '__main__':
    print('Определи, что безопасно запускать через xdist:')
    for name, status in run_checks():
        print(f'{name}: {status}')
