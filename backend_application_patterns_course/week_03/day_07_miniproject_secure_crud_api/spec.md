# Mini-Project Spec — Secure CRUD API

## Цель
Собрать маленький backend-service с auth, ролями, CRUD, partial update и soft delete.

## Что нужно реализовать
1. auth dependency по `X-API-Key`
2. actor roles: `viewer`, `manager`
3. endpoints:
   - `GET /health`
   - `GET /projects`
   - `GET /projects/{project_id}`
   - `POST /projects`
   - `PATCH /projects/{project_id}`
   - `DELETE /projects/{project_id}`
4. partial update для `PATCH`
5. soft delete для `DELETE`

## Контракты доступа
- missing/invalid API key -> `401`
- viewer может читать, но не может писать -> `403`
- manager может создавать, обновлять и удалять

## Контракты сущности
Поля проекта:
- `id`
- `name`
- `status`
- `is_deleted`

В обычных ответах `is_deleted` можно не возвращать, но soft delete должен реально влиять на поведение API.

## Ожидаемое поведение
### `GET /health`
- `200 OK`
- `{"status": "ok"}`

### `GET /projects`
- возвращает только не удалённые проекты

### `POST /projects`
- `201 Created`
- создаёт проект со статусом `draft`, если статус явно не передан

### `PATCH /projects/{project_id}`
- обновляет только переданные поля

### `DELETE /projects/{project_id}`
- делает soft delete
- `204 No Content`

## Критерий готовности
`run_smoke_checks()` проходит без ошибок.
