"""
Практическое задание:
1. Сформулируй readiness checklist для capstone backend-service.
2. Включи app structure, DB, auth, tests и compose runtime.
3. Верни checklist в виде явной структуры, а не свободного текста.

Например:
- `app_structure_defined: True`
- `db_model_defined: True`
- `auth_strategy_defined: True`
- `test_plan_defined: True`
- `compose_runtime_defined: True`

Критерий готовности: `run_checks()` проходит без ошибок.
"""


def build_capstone_readiness() -> dict[str, bool]:
    # TODO: вернуть readiness checklist для backend capstone.
    return {}



def run_checks() -> None:
    readiness = build_capstone_readiness()
    assert readiness == {
        'app_structure_defined': True,
        'db_model_defined': True,
        'auth_strategy_defined': True,
        'test_plan_defined': True,
        'compose_runtime_defined': True,
    }, 'capstone readiness checklist is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
