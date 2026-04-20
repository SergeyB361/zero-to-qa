# Postgres SQL in Practice

**Цель:** Научиться использовать Postgres в Python, тестах, миграциях, CI и инженерных расследованиях.
**Длительность:** `2 недели`
**Статус:** курс наполнен полностью по `week_01-week_02`.

## Общее правило
- Используй общее окружение из `postgres_lab/`.
- Старые `base_sql_course/`, `advanced_sql_course/` и `sql_in_practice_course/` остаются в репозитории как historical reference.

## Setup
Минимальные требования для applied-трека:
- поднятый `postgres_lab/`;
- Python с установленным драйвером `psycopg[binary]`.

Установка драйвера:
```powershell
python -m pip install "psycopg[binary]"
```

Быстрая проверка импорта:
```powershell
python -c "import psycopg; print(psycopg.__version__)"
```

Если нужен нестандартный connection setup, используй переменные окружения:
- `PGHOST`
- `PGPORT`
- `PGDATABASE`
- `PGUSER`
- `PGPASSWORD`

По умолчанию курс ожидает:
- host: `localhost`
- port: `5432`
- database: `zero_to_qa`
- user: `postgres`
- password: `postgres`

## Недели
- `week_01/` — Postgres в локальной и тестовой работе
- `week_02/` — Applied workflows вокруг Postgres

## Файлы
- `README.md` — обзор курса
- `ROADMAP.md` — план по неделям и дням
