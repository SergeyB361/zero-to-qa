# Задание 1: build_query_log_entry
# Верни словарь с name/sql/artifact.
def build_query_log_entry(name: str, sql: str) -> dict:
    return {}


# Задание 2: redact_secret_values
# Верни строку sql без password/token значений.
def redact_secret_values(sql: str) -> str:
    return 'TODO'


# Задание 3: artifact_naming_rules
# Верни 3 правила именования SQL artifacts.
def artifact_naming_rules() -> list[str]:
    return ['TODO']


# Задание 4: explain_reproducibility
# Верни 3 тезиса, почему artifact должен быть воспроизводимым.
def explain_reproducibility() -> list[str]:
    return ['TODO']


# Задание 5: logging_fields
# Верни поля, которые полезно логировать рядом с query.
def logging_fields() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(artifact_naming_rules(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
