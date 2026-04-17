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


def main() -> None:
    try:
        import psycopg
    except ModuleNotFoundError:
        print("Install dependency: python -m pip install 'psycopg[binary]'")
        return

    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM users;')
            print('users_count =', cur.fetchone()[0])
            cur.execute('SELECT id, name FROM users ORDER BY id LIMIT 2;')
            print('first_users =', cur.fetchall())


if __name__ == '__main__':
    main()
