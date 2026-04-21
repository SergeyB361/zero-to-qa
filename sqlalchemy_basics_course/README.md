# SQLAlchemy Basics

**Цель:** закрыть ORM-gap между `postgres_base_sql_course`, `fastapi_basics_course` и реальным backend-кодом.
**Длительность:** `2 недели`
**Статус:** курс создан и заполнен по `week_01-week_02`.

## Для кого
- после `postgres_base_sql_course`;
- после `fastapi_basics_course` или параллельно с ним;
- перед первым backend pet project на `FastAPI + Postgres`.

## Что внутри
- `Engine`, `Session`, `Declarative Base`;
- модели, колонки, constraints, relationships;
- CRUD и session lifecycle;
- фильтрация, сортировка, `select`, `joinedload`, `selectinload`;
- repository/service layer поверх ORM;
- интеграция `FastAPI + SQLAlchemy Session`;
- вводный блок по Alembic и миграциям.

## Что не входит
- асинхронный SQLAlchemy;
- сложные production migration workflows;
- продвинутый query tuning;
- DDD/UoW в полном виде.

## Setup
Курс рассчитан на уже поднятый [postgres_lab](../postgres_lab/README.md).

```powershell
python -m pip install sqlalchemy "psycopg[binary]"
```

Если используешь локальный `.env`, можно переопределить `DATABASE_URL`.
По умолчанию примеры ожидают:

```text
postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa
```

## Как проходить
1. Прочитать `notes.md` и понять модель работы ORM, а не только синтаксис.
2. Запустить `examples.py` и посмотреть минимальный рабочий flow.
3. Затем делать `practice.py`.
4. Критерий готовности: `run_checks()` проходит без ошибок.
5. Для мини-проектов используется `run_smoke_checks()`.

## Недели
- `week_01/` — Core ORM
- `week_02/` — Applied ORM patterns
