# Задание 1: build_test_task_payload
# Собери словарь для тестовой задачи.
def build_test_task_payload(task_id: int) -> dict:
    return {}


# Задание 2: collect_created_ids
# Верни список id, которые надо потом удалить.
def collect_created_ids(*ids: int) -> list[int]:
    return []


# Задание 3: cleanup_plan
# Верни 3 шага cleanup-плана.
def cleanup_plan() -> list[str]:
    return ['TODO']


# Задание 4: choose_seed_strategy
# Верни 3 тезиса: fixed seed, test-specific seed, rollback.
def choose_seed_strategy() -> list[str]:
    return ['TODO']


# Задание 5: explain_repeatability
# Верни 2-3 тезиса, почему repeatable seed важен.
def explain_repeatability() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(cleanup_plan(), list)
    assert isinstance(choose_seed_strategy(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
