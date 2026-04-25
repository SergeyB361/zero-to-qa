# Mini-project: Service Skeleton

## Цель
Собрать минимальный backend-service skeleton для домена `users + tasks`.

Стек в этом дне:
- `FastAPI`
- in-memory repositories
- service layer
- settings object
- consistent error contracts

## Что должно быть в skeleton

### 1. Settings
Нужен объект настроек, где явно есть хотя бы:
- `app_name`
- `api_prefix`

### 2. Repositories
Нужны отдельные repositories:
- `UserRepository`
- `TaskRepository`

### 3. Services
Нужны отдельные services:
- `UserService`
- `TaskService`

### 4. Routes
Минимальные endpoint-ы:
- `GET /health`
- `GET /api/v1/users`
- `POST /api/v1/users`
- `GET /api/v1/tasks`
- `POST /api/v1/tasks`
- `GET /api/v1/tasks/{task_id}`

### 5. Error contract
Если задача не найдена, должен быть `404` с телом:
```json
{
  "detail": "task not found",
  "code": "task_not_found"
}
```

## Ожидаемый demo flow
1. `GET /health` -> `200`
2. `POST /api/v1/users` -> `201`
3. `POST /api/v1/tasks` -> `201`
4. `GET /api/v1/tasks` -> список с новой задачей
5. `GET /api/v1/tasks/{task_id}` -> конкретная задача
6. `GET /api/v1/tasks/999` -> `404`

## Критерии готовности
- `run_smoke_checks()` проходит без ошибок;
- route, service и repository читаются отдельно;
- create/list/get ведут себя предсказуемо;
- not-found error отдаётся в согласованном формате.
