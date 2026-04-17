# Задание 1: build_hypothesis
# Верни строку гипотезы расследования.
def build_hypothesis(problem: str) -> str:
    return 'TODO'


# Задание 2: investigation_tables
# Верни список таблиц, которые стоит проверить.
def investigation_tables() -> list[str]:
    return []


# Задание 3: focused_query_goal
# Верни одну фразу: что должен показать первый query.
def focused_query_goal() -> str:
    return 'TODO'


# Задание 4: investigation_workflow
# Верни 4 шага realistic QA investigation.
def investigation_workflow() -> list[str]:
    return ['TODO']


# Задание 5: explain_signal_vs_noise
# Верни 2-3 тезиса, как не утонуть в лишних данных.
def explain_signal_vs_noise() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(investigation_workflow(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
