# День 5 — Практика: contract testing

EXPECTED_CONTRACT = {
    'required_fields': {'id', 'status', 'total'},
    'status_values': {'new', 'paid', 'cancelled'},
}


def has_required_fields(payload: dict[str, object]) -> bool:
    return False


def has_valid_status(payload: dict[str, object]) -> bool:
    return False


def explain_contract_drift() -> str:
    return ''


def run_checks() -> list[tuple[str, bool]]:
    good_payload = {'id': 1, 'status': 'paid', 'total': 100}
    missing_field = {'id': 1, 'status': 'paid'}
    bad_status = {'id': 1, 'status': 'refunded', 'total': 100}
    drift_text = explain_contract_drift().lower()
    return [
        ('required fields pass', has_required_fields(good_payload) is True),
        ('required fields fail on missing field', has_required_fields(missing_field) is False),
        ('valid status passes', has_valid_status(good_payload) is True),
        ('invalid status rejected', has_valid_status(bad_status) is False),
        ('drift mentions consumer', 'consumer' in drift_text),
        ('drift mentions broken integration', 'integration' in drift_text or 'лом' in drift_text),
    ]


if __name__ == '__main__':
    print('Собери минимальные contract checks:')
    for name, status in run_checks():
        print(f'{name}: {status}')
