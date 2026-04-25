"""
Практическое задание:
1. Оформи revision metadata для изменения схемы.
2. Составь upgrade steps для добавления колонки `priority` в таблицу `tickets`.
3. Сделай backfill существующих строк так, чтобы после миграции у всех записей была осмысленная priority.

Например:
- revision -> `2026042401_add_priority_to_tickets`
- down_revision -> `2026042400_create_tickets`
- upgrade steps -> `ALTER TABLE ...`, затем `UPDATE ...`
- после применения миграции строки должны выглядеть как `(1, 'Login fails', 'medium')`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import sqlite3


def build_revision_meta() -> dict[str, str]:
    # TODO: вернуть revision/down_revision/message для миграции priority.
    return {'revision': 'TODO', 'down_revision': 'TODO', 'message': 'TODO'}


def build_upgrade_steps() -> list[str]:
    # TODO: вернуть SQL steps для добавления priority и backfill существующих строк.
    return []


def show_columns(connection: sqlite3.Connection, table_name: str) -> list[str]:
    rows = connection.execute(f'PRAGMA table_info({table_name})').fetchall()
    return [row[1] for row in rows]


def run_checks() -> None:
    meta = build_revision_meta()
    assert meta == {
        'revision': '2026042401_add_priority_to_tickets',
        'down_revision': '2026042400_create_tickets',
        'message': 'add priority column to tickets',
    }, 'revision metadata is incorrect'

    steps = build_upgrade_steps()
    assert steps == [
        'ALTER TABLE tickets ADD COLUMN priority TEXT',
        "UPDATE tickets SET priority = 'medium' WHERE priority IS NULL",
    ], 'upgrade steps are incorrect'

    connection = sqlite3.connect(':memory:')
    connection.execute('CREATE TABLE tickets (id INTEGER PRIMARY KEY, title TEXT NOT NULL)')
    connection.execute("INSERT INTO tickets (title) VALUES ('Login fails'), ('Wrong total')")
    for step in steps:
        connection.execute(step)

    assert show_columns(connection, 'tickets') == ['id', 'title', 'priority'], 'priority column should be added after upgrade'
    assert connection.execute('SELECT id, title, priority FROM tickets ORDER BY id').fetchall() == [
        (1, 'Login fails', 'medium'),
        (2, 'Wrong total', 'medium'),
    ], 'backfill after migration is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
