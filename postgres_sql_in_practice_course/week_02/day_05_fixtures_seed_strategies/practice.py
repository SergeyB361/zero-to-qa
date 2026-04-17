# Задание 1: classify_seed
# Верни текстовую классификацию seed strategy.
def classify_seed(kind: str) -> str:
    return 'TODO'


# Задание 2: choose_global_seed_use_case
# Верни 2 случая, где оправдан глобальный seed.
def choose_global_seed_use_case() -> list[str]:
    return ['TODO']


# Задание 3: choose_test_specific_seed_use_case
# Верни 2 случая, где нужен test-specific seed.
def choose_test_specific_seed_use_case() -> list[str]:
    return ['TODO']


# Задание 4: choose_rollback_use_case
# Верни 2 случая, где выгоден rollback setup.
def choose_rollback_use_case() -> list[str]:
    return ['TODO']


# Задание 5: explain_fixture_strategy
# Верни 3 тезиса, как выбирать fixture strategy.
def explain_fixture_strategy() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(explain_fixture_strategy(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
