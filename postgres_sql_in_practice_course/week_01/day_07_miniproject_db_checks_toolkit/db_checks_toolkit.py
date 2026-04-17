from __future__ import annotations

import os
from typing import Any


def get_connection_kwargs() -> dict[str, Any]:
    return {
        'host': os.getenv('PGHOST', 'localhost'),
        'port': int(os.getenv('PGPORT', '5432')),
        'dbname': os.getenv('PGDATABASE', 'zero_to_qa'),
        'user': os.getenv('PGUSER', 'postgres'),
        'password': os.getenv('PGPASSWORD', 'postgres'),
    }


def row_exists(conn, query: str) -> bool:
    raise NotImplementedError


def count_rows(conn, query: str) -> int:
    raise NotImplementedError


def get_scalar(conn, query: str):
    raise NotImplementedError


def status_distribution(conn, table_name: str, column_name: str) -> dict[str, int]:
    raise NotImplementedError


def main() -> None:
    try:
        import psycopg
    except ModuleNotFoundError:
        print("Install dependency: python -m pip install 'psycopg[binary]'")
        return

    with psycopg.connect(**get_connection_kwargs()) as conn:
        print('Toolkit demo scaffold against zero_to_qa')
        print("Implement row_exists/count_rows/get_scalar/status_distribution")


if __name__ == '__main__':
    main()
