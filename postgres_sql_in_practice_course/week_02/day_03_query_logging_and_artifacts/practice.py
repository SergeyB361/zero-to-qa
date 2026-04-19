import re


# Задание 1: build_query_log_entry
# Верни словарь с name/sql/artifact.
def build_query_log_entry(name: str, sql: str) -> dict:
    return {
        'name': name,
        'sql': sql,
        'artifact': f'artifacts/{name}.sql',
    }


# Задание 2: redact_secret_values
# Верни строку sql без password/token значений.
def redact_secret_values(sql: str) -> str:
    redacted = re.sub(r"(?i)(password\s*=\s*)'[^']*'", r"\1'***'", sql)
    redacted = re.sub(r"(?i)(token\s*=\s*)'[^']*'", r"\1'***'", redacted)
    return redacted


# Задание 3: artifact_naming_rules
# Верни 3 правила именования SQL artifacts.
def artifact_naming_rules() -> list[str]:
    return [
        'имя артефакта должно отражать цель запроса, а не случайное описание',
        'в имени лучше использовать ascii, snake_case и стабильный префикс или контекст',
        'один артефакт должен соответствовать одному воспроизводимому investigation step',
    ]


# Задание 4: explain_reproducibility
# Верни 3 тезиса, почему artifact должен быть воспроизводимым.
def explain_reproducibility() -> list[str]:
    return [
        'другой инженер должен суметь запустить тот же запрос без потери контекста',
        'воспроизводимость упрощает сравнение результатов между прогонами и средами',
        'артефакт полезен только если по нему можно повторно получить тот же сигнал',
    ]


# Задание 5: logging_fields
# Верни поля, которые полезно логировать рядом с query.
def logging_fields() -> list[str]:
    return ['query_name', 'executed_at', 'database_name', 'row_count', 'artifact_path']


def run_checks() -> None:
    item = build_query_log_entry('open_tasks_report', 'SELECT * FROM tasks;')
    assert item == {
        'name': 'open_tasks_report',
        'sql': 'SELECT * FROM tasks;',
        'artifact': 'artifacts/open_tasks_report.sql',
    }
    assert redact_secret_values("SELECT * FROM users WHERE password = 'secret' AND token = 'abc';") == (
        "SELECT * FROM users WHERE password = '***' AND token = '***';"
    )
    assert len(artifact_naming_rules()) == 3
    assert len(explain_reproducibility()) == 3
    assert logging_fields() == ['query_name', 'executed_at', 'database_name', 'row_count', 'artifact_path']
    print('Query logging practice checks passed.')


if __name__ == '__main__':
    run_checks()
