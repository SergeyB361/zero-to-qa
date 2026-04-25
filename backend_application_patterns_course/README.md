# Backend Application Patterns

**Цель:** собрать из `FastAPI`, `SQLAlchemy`, `Postgres` и `Docker` нормальный backend-service уровня junior/junior+.
**Длительность:** `4 недели`
**Статус:** `week_01-week_04` наполнены.

## Для кого
- после `fastapi_basics_course`;
- после `sqlalchemy_basics_course`;
- после `postgres_base_sql_course`;
- перед более серьёзным backend pet project.

## Что внутри
- структура backend-приложения: `routers / services / repositories / schemas / models / config`;
- настройки и env-переменные;
- session lifecycle, Postgres integration и schema evolution;
- Alembic и migration thinking;
- auth basics, roles, permissions;
- pagination, filtering, sorting, partial update, soft delete;
- integration testing, Docker Compose и basic CI;
- capstone на `FastAPI + SQLAlchemy + Postgres + Alembic`.

## Что не входит
- асинхронный стек `FastAPI + SQLAlchemy AsyncSession`;
- продвинутый security hardening;
- message brokers и event-driven architecture;
- production deployment в cloud.

## Пререквизиты
- [fastapi_basics_course](../fastapi_basics_course/README.md)
- [sqlalchemy_basics_course](../sqlalchemy_basics_course/README.md)
- [postgres_base_sql_course](../postgres_base_sql_course/README.md)
- [postgres_sql_in_practice_course](../postgres_sql_in_practice_course/README.md)

## Формат материалов
Обычные дни:
- `notes.md`
- `examples.py`
- `practice.py`

Мини-проектные дни:
- `notes.md`
- `spec.md`
- стартовый `.py`

## Недели
- `week_01/` — Application Structure
- `week_02/` — Database and Migrations
- `week_03/` — Auth, CRUD and Business Rules
- `week_04/` — Testing, Delivery and Capstone
