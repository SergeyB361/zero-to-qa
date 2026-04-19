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


# Задание 1: build_hypothesis
# Верни строку гипотезы расследования.
def build_hypothesis(problem: str) -> str:
    return f'Гипотеза: {problem} связано с рассинхроном между tasks и defects.'


# Задание 2: investigation_tables
# Верни список таблиц, которые стоит проверить.
def investigation_tables() -> list[str]:
    return ['tasks', 'defects', 'test_runs']


# Задание 3: focused_query_goal
# Верни одну фразу: что должен показать первый query.
def focused_query_goal() -> str:
    return 'Показать закрытые задачи, у которых ещё есть активные дефекты.'


# Задание 4: investigation_workflow
# Верни 4 шага realistic QA investigation.
def investigation_workflow() -> list[str]:
    return [
        'сформулировать наблюдаемый симптом и гипотезу',
        'выбрать минимальный набор связанных таблиц',
        'написать focused query, который даёт сигнал, а не всю историю',
        'зафиксировать findings и следующий инженерный шаг',
    ]


# Задание 5: explain_signal_vs_noise
# Верни 2-3 тезиса, как не утонуть в лишних данных.
def explain_signal_vs_noise() -> list[str]:
    return [
        'первый запрос должен отвечать на одну гипотезу, а не тащить все колонки сразу',
        'полезно ограничивать выборку только связанными статусами и сущностями',
        'каждый следующий query должен уточнять сигнал, а не дублировать шум',
    ]


def run_checks() -> None:
    assert 'Гипотеза:' in build_hypothesis('ошибка не попала в отчёт')
    assert investigation_tables() == ['tasks', 'defects', 'test_runs']
    assert focused_query_goal() == 'Показать закрытые задачи, у которых ещё есть активные дефекты.'
    assert len(investigation_workflow()) == 4
    assert 2 <= len(explain_signal_vs_noise()) <= 3

    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT COUNT(*)
                FROM tasks t
                JOIN defects d ON d.task_id = t.id
                WHERE t.status = 'closed'
                  AND d.status IN ('open', 'in_progress')
                """
            )
            assert cur.fetchone()[0] == 1
            cur.execute("SELECT COUNT(*) FROM tasks WHERE status = 'blocked'")
            assert cur.fetchone()[0] == 1

    print('Realistic investigation practice checks passed.')


if __name__ == '__main__':
    run_checks()
