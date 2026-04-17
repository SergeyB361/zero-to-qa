from __future__ import annotations

import os
from typing import Any

import psycopg


def get_connection_kwargs() -> dict[str, Any]:
    return {
        'host': os.getenv('PGHOST', 'localhost'),
        'port': int(os.getenv('PGPORT', '5432')),
        'dbname': os.getenv('PGDATABASE', 'zero_to_qa'),
        'user': os.getenv('PGUSER', 'postgres'),
        'password': os.getenv('PGPASSWORD', 'postgres'),
    }


def migration_record(name: str, applied: bool) -> dict:
    return {'name': name, 'applied': applied}


def main() -> None:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TEMP TABLE migration_demo_users (
                    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    name TEXT NOT NULL
                )
                """
            )
            cur.execute(
                "ALTER TABLE migration_demo_users ADD COLUMN squad TEXT DEFAULT 'core'"
            )
            cur.execute(
                """
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = 'migration_demo_users'
                  AND table_schema LIKE 'pg_temp_%'
                ORDER BY ordinal_position
                """
            )
            columns = [row[0] for row in cur.fetchall()]
            assert columns == ['id', 'name', 'squad']

            cur.execute(
                """
                CREATE TEMP TABLE schema_migrations (
                    migration_name TEXT PRIMARY KEY,
                    applied_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                )
                """
            )
            cur.execute(
                "INSERT INTO schema_migrations (migration_name) VALUES (%s)",
                ('001_add_squad_column',),
            )
            cur.execute("SELECT COUNT(*) FROM schema_migrations")
            assert cur.fetchone()[0] == 1

        assert migration_record('001_add_squad_column', True)['applied'] is True

    print('Real migration example passed against Postgres')


if __name__ == '__main__':
    main()
