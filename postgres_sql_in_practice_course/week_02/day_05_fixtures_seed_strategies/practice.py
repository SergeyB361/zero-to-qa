# Задание 1: classify_seed
# Верни текстовую классификацию seed strategy.
def classify_seed(kind: str) -> str:
    mapping = {
        'global': 'shared baseline dataset',
        'test': 'scenario-specific setup',
        'rollback': 'transaction-scoped data',
    }
    return mapping[kind]


# Задание 2: choose_global_seed_use_case
# Верни 2 случая, где оправдан глобальный seed.
def choose_global_seed_use_case() -> list[str]:
    return [
        'общий baseline для локальных SQL-уроков и demo-данных',
        'стабильный стенд для smoke-проверок и onboarding практики',
    ]


# Задание 3: choose_test_specific_seed_use_case
# Верни 2 случая, где нужен test-specific seed.
def choose_test_specific_seed_use_case() -> list[str]:
    return [
        'сценарий требует редкой комбинации статусов или edge-case данных',
        'тест должен создавать данные только под себя и не зависеть от общего seed',
    ]


# Задание 4: choose_rollback_use_case
# Верни 2 случая, где выгоден rollback setup.
def choose_rollback_use_case() -> list[str]:
    return [
        'интеграционный тест можно полностью обернуть в одну транзакцию',
        'нужно быстро очистить временные данные без явного cleanup SQL',
    ]


# Задание 5: explain_fixture_strategy
# Верни 3 тезиса, как выбирать fixture strategy.
def explain_fixture_strategy() -> list[str]:
    return [
        'если данные нужны многим сценариям и редко меняются, подходит global seed',
        'если сценарий узкий или конфликтный, нужен test-specific setup',
        'если окружение позволяет, rollback даёт самый дешёвый cleanup',
    ]


def run_checks() -> None:
    assert classify_seed('global') == 'shared baseline dataset'
    assert classify_seed('test') == 'scenario-specific setup'
    assert classify_seed('rollback') == 'transaction-scoped data'
    assert len(choose_global_seed_use_case()) == 2
    assert len(choose_test_specific_seed_use_case()) == 2
    assert len(choose_rollback_use_case()) == 2
    assert len(explain_fixture_strategy()) == 3
    print('Fixture/seed strategy practice checks passed.')


if __name__ == '__main__':
    run_checks()
