# Задание 1: row_exists
# Реализуй helper: есть ли строка по key/value.
def row_exists(rows: list[dict], key: str, value: object) -> bool:
    return False


# Задание 2: count_rows
# Реализуй helper: количество строк.
def count_rows(rows: list[dict]) -> int:
    return -1


# Задание 3: get_scalar
# Возьми первое значение по ключу из первой строки.
def get_scalar(rows: list[dict], key: str):
    return None


# Задание 4: assert_task_created
# Проверь, что есть строка со status=open.
def assert_task_created(rows: list[dict]) -> None:
    pass


# Задание 5: explain_when_db_check_is_justified
# Верни 3 тезиса, когда DB-check оправдан.
def explain_when_db_check_is_justified() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(explain_when_db_check_is_justified(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
