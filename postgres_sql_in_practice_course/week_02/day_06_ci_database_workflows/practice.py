import subprocess
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parents[3] / 'postgres_lab'


def run(command: list[str]) -> str:
    completed = subprocess.run(command, capture_output=True, text=True, check=True, cwd=LAB_DIR)
    return completed.stdout.strip()


# Задание 1: ci_steps
# Верни список шагов CI pipeline для базы.
def ci_steps() -> list[str]:
    return [
        'start postgres service',
        'wait for health',
        'apply schema and seed',
        'run checks',
        'collect artifacts',
    ]


# Задание 2: healthcheck_reason
# Верни 2-3 тезиса, почему healthcheck лучше sleep.
def healthcheck_reason() -> list[str]:
    return [
        'healthcheck проверяет готовность сервиса по факту, а не по предположению о времени запуска',
        'sleep делает pipeline хрупким: на медленной машине мало, на быстрой лишняя пауза',
        'healthcheck даёт явный сигнал, когда база ещё не готова принимать подключения',
    ]


# Задание 3: artifact_examples
# Верни примеры полезных artifacts для DB workflow.
def artifact_examples() -> list[str]:
    return ['query logs', 'migration output', 'investigation sql files']


# Задание 4: failure_points
# Верни 3 частые точки падения CI database workflow.
def failure_points() -> list[str]:
    return [
        'контейнер поднялся, но база ещё не healthy',
        'схема или seed не совпали с ожидаемой версией сервиса',
        'проверки зависят от нестабильных данных или несохранённых артефактов',
    ]


# Задание 5: explain_repeatable_pipeline
# Верни 3 тезиса, что делает pipeline repeatable.
def explain_repeatable_pipeline() -> list[str]:
    return [
        'фиксированная схема и seed дают стабильную базовую точку для прогона',
        'явные шаги запуска и healthcheck убирают случайность по времени старта',
        'артефакты и логи позволяют воспроизвести неудачный прогон локально',
    ]


def run_checks() -> None:
    assert ci_steps() == [
        'start postgres service',
        'wait for health',
        'apply schema and seed',
        'run checks',
        'collect artifacts',
    ]
    assert len(healthcheck_reason()) == 3
    assert artifact_examples() == ['query logs', 'migration output', 'investigation sql files']
    assert len(failure_points()) == 3
    assert len(explain_repeatable_pipeline()) == 3
    assert 'zero_to_qa_postgres' in run(['docker', 'compose', 'ps'])
    print('CI database workflow practice checks passed.')


if __name__ == '__main__':
    run_checks()
