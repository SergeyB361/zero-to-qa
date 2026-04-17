import subprocess
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parents[3] / 'postgres_lab'


def run(command: list[str]) -> str:
    completed = subprocess.run(command, capture_output=True, text=True, check=True, cwd=LAB_DIR)
    return completed.stdout.strip()


def main() -> None:
    print('Docker Compose version:')
    print(run(['docker', 'compose', 'version']))
    print('\nPostgres lab status:')
    print(run(['docker', 'compose', 'ps']))


if __name__ == '__main__':
    main()