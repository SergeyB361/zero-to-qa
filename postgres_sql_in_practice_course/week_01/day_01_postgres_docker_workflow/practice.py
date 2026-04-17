import subprocess


def run(command: list[str]) -> str:
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    return completed.stdout.strip()


# Задание 1: show_compose_version
# Верни строку версии docker compose.
def show_compose_version() -> str:
    return 'TODO'


# Задание 2: show_compose_status
# Верни вывод docker compose ps.
def show_compose_status() -> str:
    return 'TODO'


# Задание 3: show_running_containers
# Верни вывод docker ps.
def show_running_containers() -> str:
    return 'TODO'


# Задание 4: show_postgres_logs_tail
# Верни tail логов postgres_lab.
def show_postgres_logs_tail() -> str:
    return 'TODO'


# Задание 5: explain_lab_structure
# Верни 3 строки с объяснением: compose, schema, seed.
def explain_lab_structure() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(explain_lab_structure(), list)
    assert len(explain_lab_structure()) >= 1
    print('Scaffold checks passed. Реализуй функции и прогоняй их локально.')


if __name__ == '__main__':
    run_checks()
