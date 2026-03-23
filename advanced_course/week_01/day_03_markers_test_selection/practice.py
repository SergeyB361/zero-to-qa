# День 3 — Практика: markers и test selection

TESTS = {
    'test_login': {'markers': ['smoke', 'auth']},
    'test_refund': {'markers': ['regression', 'payments']},
    'test_report_export': {'markers': ['slow', 'reporting']},
}


def tests_with_marker(marker: str) -> list[str]:
    return sorted(name for name, meta in TESTS.items() if marker in meta['markers'])


def should_skip(test_name: str, environment: str) -> bool:
    return test_name == 'test_report_export' and environment == 'local'


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('smoke filtered', tests_with_marker('smoke') == ['test_login']),
        ('slow filtered', tests_with_marker('slow') == ['test_report_export']),
        ('skip local heavy test', should_skip('test_report_export', 'local') is True),
        ('do not skip smoke on ci', should_skip('test_login', 'ci') is False),
    ]


if __name__ == '__main__':
    print('Отработай маркеры, выборку и идею skip:')
    for name, status in run_checks():
        print(f'{name}: {status}')
