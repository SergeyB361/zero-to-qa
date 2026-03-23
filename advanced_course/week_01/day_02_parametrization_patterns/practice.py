# День 2 — Практика: parametrization patterns

CASES = [
    ('smoke-login', 200, True),
    ('wrong-password', 401, False),
    ('blocked-user', 403, False),
]


def case_ids() -> list[str]:
    return [case[0] for case in CASES]


def passed_cases() -> list[str]:
    return [case_id for case_id, status, expected_ok in CASES if status == 200 and expected_ok]


def xfailed_cases() -> list[str]:
    return ['blocked-user']


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('case ids exist', case_ids() == ['smoke-login', 'wrong-password', 'blocked-user']),
        ('passed case filtered', passed_cases() == ['smoke-login']),
        ('xfail case declared', xfailed_cases() == ['blocked-user']),
    ]


if __name__ == '__main__':
    print('Отработай ids, выбор кейсов и идею xfail/marking:')
    for name, status in run_checks():
        print(f'{name}: {status}')
