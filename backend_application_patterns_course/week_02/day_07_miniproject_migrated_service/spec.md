# Mini-Project Spec — Migrated Service

## Цель
Перевести маленький issue-service c in-memory skeleton на SQLAlchemy-backed runtime.

## Что нужно реализовать
1. `AppSettings` с `database_url`
2. `Issue` ORM model
3. `build_engine()` и `build_session_factory()`
4. `IssueRepository`
5. `IssueService`
6. FastAPI app с endpoint-ами:
   - `GET /health`
   - `GET /issues`
   - `GET /issues/{slug}`
   - `POST /issues`

## Контракты
### `GET /health`
- `200 OK`
- `{"status": "ok"}`

### `GET /issues`
- `200 OK`
- список issues

### `GET /issues/{slug}`
- `200 OK`, если issue существует
- `404`, если issue не найден

### `POST /issues`
- `201 Created`
- payload созданного issue
- `409`, если slug уже существует

## Модель issue
Минимальные поля:
- `id`
- `title`
- `slug`
- `status`

## Ожидаемая архитектура
- route работает через service
- service работает через repository
- repository работает через SQLAlchemy session
- commit/rollback живут в service layer

## Что не требуется
- auth
- pagination
- Docker Compose
- Alembic migrations

## Критерий готовности
`run_smoke_checks()` проходит без ошибок.
