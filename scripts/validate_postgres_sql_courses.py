from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPOSE_DIR = ROOT / "postgres_lab"
TARGET_DIRS = [
    ROOT / "postgres_base_sql_course",
    ROOT / "postgres_advanced_sql_course",
    ROOT / "postgres_sql_in_practice_course",
]
INIT_FILES = [
    COMPOSE_DIR / "init" / "001_schema.sql",
    COMPOSE_DIR / "init" / "002_seed.sql",
]


def run_command(
    args: list[str],
    *,
    cwd: Path | None = None,
    input_bytes: bytes | None = None,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        input=input_bytes,
        capture_output=capture_output,
        check=True,
    )


def docker_compose_up(compose_dir: Path) -> None:
    run_command(
        ["docker", "compose", "up", "-d"],
        cwd=compose_dir,
        capture_output=True,
    )


def wait_for_healthy(container_name: str, timeout_seconds: int) -> None:
    deadline = time.time() + timeout_seconds
    last_status = "unknown"
    while time.time() < deadline:
        result = subprocess.run(
            ["docker", "inspect", "-f", "{{.State.Health.Status}}", container_name],
            capture_output=True,
            check=False,
        )
        if result.returncode == 0:
            last_status = result.stdout.decode().strip()
            if last_status == "healthy":
                return
        time.sleep(2)

    raise RuntimeError(
        f"Container {container_name!r} did not become healthy within "
        f"{timeout_seconds} seconds. Last status: {last_status!r}."
    )


def discover_sql_files(paths: list[Path]) -> list[Path]:
    sql_files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".sql":
            sql_files.append(path)
            continue

        if path.is_dir():
            sql_files.extend(sorted(path.rglob("*.sql")))

    return sorted({file.resolve() for file in sql_files})


def psql_stdin(
    *,
    container_name: str,
    database: str,
    user: str,
    sql_bytes: bytes,
) -> None:
    run_command(
        [
            "docker",
            "exec",
            "-i",
            container_name,
            "psql",
            "-U",
            user,
            "-d",
            database,
            "-v",
            "ON_ERROR_STOP=1",
            "-f",
            "-",
        ],
        input_bytes=sql_bytes,
        capture_output=True,
    )


def recreate_validation_database(
    *,
    container_name: str,
    database: str,
    user: str,
) -> None:
    drop_sql = f"DROP DATABASE IF EXISTS {database} WITH (FORCE);".encode()
    create_sql = f"CREATE DATABASE {database};".encode()

    psql_stdin(
        container_name=container_name,
        database="postgres",
        user=user,
        sql_bytes=drop_sql,
    )
    psql_stdin(
        container_name=container_name,
        database="postgres",
        user=user,
        sql_bytes=create_sql,
    )


def bootstrap_database(
    *,
    container_name: str,
    database: str,
    user: str,
) -> None:
    for init_file in INIT_FILES:
        psql_stdin(
            container_name=container_name,
            database=database,
            user=user,
            sql_bytes=init_file.read_bytes(),
        )


def validate_sql_file(
    *,
    sql_file: Path,
    container_name: str,
    database: str,
    user: str,
) -> None:
    recreate_validation_database(
        container_name=container_name,
        database=database,
        user=user,
    )
    bootstrap_database(
        container_name=container_name,
        database=database,
        user=user,
    )
    psql_stdin(
        container_name=container_name,
        database=database,
        user=user,
        sql_bytes=sql_file.read_bytes(),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Postgres SQL course files against postgres_lab.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help=(
            "Optional files or directories to validate. "
            "Defaults to the Postgres SQL course directories."
        ),
    )
    parser.add_argument(
        "--container-name",
        default="zero_to_qa_postgres",
        help="Docker container name for postgres_lab.",
    )
    parser.add_argument(
        "--user",
        default="postgres",
        help="Database user to pass to psql.",
    )
    parser.add_argument(
        "--database",
        default="zero_to_qa_validation",
        help="Temporary database name used during validation.",
    )
    parser.add_argument(
        "--health-timeout-seconds",
        type=int,
        default=90,
        help="How long to wait for postgres_lab to become healthy.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_paths = [ROOT / path for path in args.paths] if args.paths else TARGET_DIRS
    sql_files = discover_sql_files(target_paths)

    if not sql_files:
        print("No SQL files found for validation.", file=sys.stderr)
        return 1

    print(f"Starting postgres_lab from {COMPOSE_DIR}")
    sys.stdout.flush()
    docker_compose_up(COMPOSE_DIR)
    wait_for_healthy(args.container_name, args.health_timeout_seconds)

    print(f"Discovered {len(sql_files)} SQL files.")
    sys.stdout.flush()
    for index, sql_file in enumerate(sql_files, start=1):
        relative_path = sql_file.relative_to(ROOT)
        print(f"[{index}/{len(sql_files)}] Validating {relative_path}")
        sys.stdout.flush()
        validate_sql_file(
            sql_file=sql_file,
            container_name=args.container_name,
            database=args.database,
            user=args.user,
        )

    print("Postgres SQL validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}: {exc.cmd}", file=sys.stderr)
        if exc.stdout:
            print(exc.stdout.decode(errors="replace"), file=sys.stderr)
        if exc.stderr:
            print(exc.stderr.decode(errors="replace"), file=sys.stderr)
        raise
