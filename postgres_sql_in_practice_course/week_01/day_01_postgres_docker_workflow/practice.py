import subprocess
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parents[3] / 'postgres_lab'


def run(command: list[str]) -> str:
    completed = subprocess.run(command, capture_output=True, text=True, check=True, cwd=LAB_DIR)
    return completed.stdout.strip()


# Задание 1: show_compose_version
# Верни строку версии docker compose.
def show_compose_version() -> str:
    return run(['docker', 'compose', 'version'])


# Задание 2: show_compose_status
# Верни вывод docker compose ps.
def show_compose_status() -> str:
    return run(['docker', 'compose', 'ps'])


# Задание 3: show_running_containers
# Верни вывод docker ps.
def show_running_containers() -> str:
    return run(['docker', 'ps'])


# Задание 4: show_postgres_logs_tail
# Верни tail логов postgres_lab.
def show_postgres_logs_tail() -> str:
    return run(['docker', 'compose', 'logs', '--tail', '20', 'postgres'])


# Задание 5: explain_lab_structure
# Верни 3 строки с объяснением: compose, schema, seed.
def explain_lab_structure() -> list[str]:
    return [
        'docker-compose.yml поднимает единый Postgres runtime для всех новых SQL-курсов.',
        '001_schema.sql создаёт таблицы и базовые связи в zero_to_qa.',
        '002_seed.sql наполняет базу стабильными данными для практики и расследований.',
    ]


def run_checks() -> None:
    assert 'Docker Compose version' in show_compose_version()
    assert 'zero_to_qa_postgres' in show_compose_status()
    assert 'zero_to_qa_postgres' in show_running_containers()
    assert 'database system is ready to accept connections' in show_postgres_logs_tail().lower()
    assert len(explain_lab_structure()) == 3
    print('Live docker workflow checks passed.')


if __name__ == '__main__':
    run_checks()
