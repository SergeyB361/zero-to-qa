# День 5 — Практика: flaky tests

FLAKY_PATTERNS = [
    'sleep before assert',
    'shared mutable data between tests',
    'depends on external unstable service',
    'assert on eventually consistent state without wait',
]


def stabilization_actions() -> list[str]:
    return [
        'replace sleep with explicit wait',
        'isolate test data and accounts',
        'mock unstable dependency where appropriate',
    ]


def run_checks() -> list[tuple[str, bool]]:
    actions = ' '.join(stabilization_actions()).lower()
    return [
        ('sleep mentioned as flaky pattern', 'sleep before assert' in FLAKY_PATTERNS),
        ('shared state mentioned', any('shared' in item for item in FLAKY_PATTERNS)),
        ('explicit wait suggested', 'explicit wait' in actions),
        ('mock suggested', 'mock' in actions),
    ]


if __name__ == '__main__':
    print('Разбери flaky-паттерны и способы стабилизации:')
    for name, status in run_checks():
        print(f'{name}: {status}')
