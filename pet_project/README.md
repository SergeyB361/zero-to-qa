# Task Service + Audit Timeline

Pet project для портфолио Junior Python Developer.

## Статус
MVP реализован и проверен в двух режимах:
- unit/in-process через `pytest` и `TestClient`;
- live flow через два поднятых `uvicorn`-сервиса.

Проверенный бизнес-поток:

`create task -> publish event -> store event -> timeline -> snapshot`

## Идея проекта
Проект состоит из двух backend-сервисов:
- `Task Service` — управляет задачами;
- `Audit Timeline Service` — принимает доменные события и хранит историю изменений.

Цель проекта — показать не просто CRUD, а понятную цепочку изменений состояния:

`действие с задачей -> доменное событие -> аудит -> timeline -> snapshot`

## Почему проект полезен для портфолио
Проект демонстрирует:
- FastAPI;
- SQLAlchemy;
- SQLite;
- REST API;
- сервисный слой и слой репозиториев;
- межсервисное HTTP-взаимодействие;
- доменные события;
- аудит изменений;
- восстановление текущего состояния из event history.

## MVP-границы
В MVP входят:
- создание задачи;
- получение задачи;
- получение списка задач;
- смена статуса;
- смена исполнителя;
- удаление задачи;
- генерация событий в `Task Service`;
- приём и хранение событий в `Audit Timeline Service`;
- timeline по задаче;
- timeline по пользователю-инициатору;
- snapshot текущего состояния задачи.

Не входят в MVP:
- комментарии;
- изменение заголовка задачи;
- сложная авторизация;
- retry / outbox / брокеры сообщений;
- обязательный Docker-слой;
- production-ready observability.

## Архитектура MVP
Фиксированное решение для первой версии:
- `Task Service` — FastAPI + SQLAlchemy + SQLite;
- `Audit Timeline Service` — FastAPI + SQLAlchemy + SQLite;
- взаимодействие между сервисами — синхронный HTTP POST.

### Схема взаимодействия
```text
Client
  |
  v
Task Service
  |
  | POST /events
  v
Audit Timeline Service
```

## Реализованные endpoint'ы

### Task Service
- `GET /health`
- `POST /tasks`
- `GET /tasks`
- `GET /tasks/{task_id}`
- `PATCH /tasks/{task_id}/status`
- `PATCH /tasks/{task_id}/assignee`
- `DELETE /tasks/{task_id}?actor_id=...`

### Audit Timeline Service
- `GET /health`
- `POST /events`
- `GET /events`
- `GET /events/{event_id}`
- `GET /timeline/tasks/{task_id}`
- `GET /timeline/users/{actor_id}`
- `GET /snapshot/tasks/{task_id}`

## Локальный запуск

### 1. Установить зависимости
```powershell
venv\Scripts\python -m pip install -r pet_project\task_service\requirements.txt
venv\Scripts\python -m pip install -r pet_project\audit_timeline_service\requirements.txt
```

### 2. Поднять Audit Timeline Service
```powershell
venv\Scripts\python -m uvicorn pet_project.audit_timeline_service.app.main:app --host 127.0.0.1 --port 8001
```

### 3. Поднять Task Service
```powershell
venv\Scripts\python -m uvicorn pet_project.task_service.app.main:app --host 127.0.0.1 --port 8000
```

По умолчанию `Task Service` шлёт события в `http://127.0.0.1:8001`.

## Тесты
```powershell
venv\Scripts\python -m pytest pet_project\task_service\tests\test_task_api.py -q
venv\Scripts\python -m pytest pet_project\audit_timeline_service\tests\test_audit_api.py -q
```

## Demo flow
Минимальный сценарий показа проекта:
1. `POST /tasks`
2. `PATCH /tasks/{task_id}/status`
3. `PATCH /tasks/{task_id}/assignee`
4. `DELETE /tasks/{task_id}?actor_id=...`
5. `GET /timeline/tasks/{task_id}`
6. `GET /timeline/users/{actor_id}`
7. `GET /snapshot/tasks/{task_id}`

Именно этот flow уже был проверен live.

## Ограничения текущей версии
- SQLite используется для простоты MVP;
- публикация событий синхронная;
- при ошибке отправки события `Task Service` отвечает `502`, без retry/outbox;
- нет auth и прав доступа;
- нет пагинации и фильтрации списков.

## Структура проекта
```text
pet_project/
  README.md
  ROADMAP.md
  spec.md
  task_service/
    app/
    tests/
  audit_timeline_service/
    app/
    tests/
```

## Документы проекта
- [spec.md](spec.md) — scope MVP и критерии готовности
- [ROADMAP.md](ROADMAP.md) — статус реализации
- [COURSE_ALIGNMENT.md](COURSE_ALIGNMENT.md) — связь проекта с учебными треками

## Принцип реализации
- сначала делается законченный MVP;
- всё, что не входит в MVP, не раздувает первую версию;
- важнее завершённость и демонстрационная пригодность, чем лишняя архитектурная сложность.
