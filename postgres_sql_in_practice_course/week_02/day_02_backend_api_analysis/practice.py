# Задание 1: slow_endpoints
# Верни список endpoint -> avg_latency.
def slow_endpoints(rows: list[dict]) -> list[str]:
    return []


# Задание 2: error_rate_by_release
# Верни release -> error_count.
def error_rate_by_release(rows: list[dict]) -> dict[str, int]:
    return {}


# Задание 3: critical_defects_by_release
# Верни release -> critical defects count.
def critical_defects_by_release(rows: list[dict]) -> dict[str, int]:
    return {}


# Задание 4: investigation_question_templates
# Верни 3 хороших backend investigation questions.
def investigation_question_templates() -> list[str]:
    return ['TODO']


# Задание 5: explain_operational_sql
# Верни 3 тезиса, чем operational SQL отличается от “учебного отчёта”.
def explain_operational_sql() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(investigation_question_templates(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
