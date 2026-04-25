# Capstone Spec — Backend Service

## Цель
Собрать законченный backend-service уровня junior/junior+ на базе материалов курса.

## Обязательные блоки
1. `FastAPI` приложение
2. `SQLAlchemy` модели и data layer
3. `settings/config`
4. auth dependency и role checks
5. CRUD endpoints
6. partial update или soft delete
7. tests
8. `docker compose` runtime
9. README с инструкцией запуска

## Минимальные endpoint-ы
- `GET /health`
- `GET /items`
- `GET /items/{item_id}`
- `POST /items`
- `PATCH /items/{item_id}`
- `DELETE /items/{item_id}`

## Контракты доступа
- missing/invalid credentials -> `401`
- insufficient permissions -> `403`

## Технические ожидания
- data layer не смешан с route
- service layer не смешан с auth dependency
- runtime-конфиг задаётся через settings/env
- проект можно поднять воспроизводимо

## Что не обязательно
- OAuth/OIDC
- async stack
- cloud deployment
- сложная observability platform

## Критерий готовности
1. `run_smoke_checks()` проходит без ошибок.
2. `test_backend_service.py` покрывает health, auth, create, patch и soft delete.
3. `docker-compose.yml` описывает `app + db` runtime.
4. `README.md` даёт понятный local runtime.
5. `alembic_revision.py` показывает migration outline для основной таблицы.
