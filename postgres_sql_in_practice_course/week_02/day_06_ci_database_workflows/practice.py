# Задание 1: ci_steps
# Верни список шагов CI pipeline для базы.
def ci_steps() -> list[str]:
    return ['TODO']


# Задание 2: healthcheck_reason
# Верни 2-3 тезиса, почему healthcheck лучше sleep.
def healthcheck_reason() -> list[str]:
    return ['TODO']


# Задание 3: artifact_examples
# Верни примеры полезных artifacts для DB workflow.
def artifact_examples() -> list[str]:
    return ['TODO']


# Задание 4: failure_points
# Верни 3 частые точки падения CI database workflow.
def failure_points() -> list[str]:
    return ['TODO']


# Задание 5: explain_repeatable_pipeline
# Верни 3 тезиса, что делает pipeline repeatable.
def explain_repeatable_pipeline() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(ci_steps(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
