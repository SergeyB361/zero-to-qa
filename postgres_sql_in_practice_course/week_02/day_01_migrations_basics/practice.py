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


# Задание 1: create_migration_name
# Верни имя миграции.
def create_migration_name(seq: int, slug: str) -> str:
    return f'{seq:03d}_{slug}.sql'


# Задание 2: migration_table_columns
# Верни список колонок для schema_migrations.
def migration_table_columns() -> list[str]:
    return ['migration_name', 'applied_at']


# Задание 3: explain_safe_migration_flow
# Верни 4 шага безопасного migration workflow.
def explain_safe_migration_flow() -> list[str]:
    return [
        'сначала проверить migration на dev или temp-схеме',
        'зафиксировать ожидаемое изменение схемы и rollback plan',
        'применить миграцию и проверить новую схему через information_schema',
        'сохранить запись о применении и только потом двигаться дальше',
    ]


# Задание 4: explain_rollback_need
# Верни 2-3 тезиса, когда нужен rollback plan.
def explain_rollback_need() -> list[str]:
    return [
        'когда миграция меняет схему или данные в прод-подобной среде',
        'когда откат сервиса без отката схемы оставит систему в несовместимом состоянии',
        'когда ошибка может обнаружиться только после применения DDL или backfill',
    ]


# Задание 5: migration_checklist
# Верни короткий checklist перед применением миграции.
def migration_checklist() -> list[str]:
    return [
        'migration name и порядок применения согласованы',
        'есть rollback plan или безопасный forward-fix путь',
        'известно, как проверить новую схему и данные после применения',
    ]


def run_checks() -> None:
    assert create_migration_name(1, 'add_squad_column') == '001_add_squad_column.sql'
    assert migration_table_columns() == ['migration_name', 'applied_at']
    assert len(explain_safe_migration_flow()) == 4
    assert 2 <= len(explain_rollback_need()) <= 3
    assert len(migration_checklist()) == 3

    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TEMP TABLE schema_migrations (
                    migration_name TEXT PRIMARY KEY,
                    applied_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                )
                """
            )
            cur.execute(
                """
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = 'schema_migrations'
                  AND table_schema LIKE 'pg_temp_%'
                ORDER BY ordinal_position
                """
            )
            columns = [row[0] for row in cur.fetchall()]
            assert columns == migration_table_columns()
            cur.execute(
                'INSERT INTO schema_migrations (migration_name) VALUES (%s)',
                (create_migration_name(1, 'add_squad_column'),),
            )
            cur.execute('SELECT COUNT(*) FROM schema_migrations')
            assert cur.fetchone()[0] == 1

    print('Migration practice checks passed.')


if __name__ == '__main__':
    run_checks()
