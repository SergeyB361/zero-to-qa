# FastAPI Lab

Единое Docker-окружение для [fastapi_basics_course](../fastapi_basics_course/README.md).

## Зачем нужен lab
- одинаковые версии `fastapi`, `httpx`, `pytest`, `uvicorn` у всех;
- один и тот же способ запуска практики;
- меньше шума от локального окружения.

## Что внутри
- `Dockerfile` — Python runtime для FastAPI-практики;
- `docker-compose.yml` — сервис `api` с примонтированным репозиторием;
- `requirements.txt` — минимальные зависимости для курса.

## Быстрый старт
```powershell
docker compose up -d --build
```

Проверка:
```powershell
docker compose ps
```

## Как запускать практику
Обычный день:
```powershell
docker compose exec api python fastapi_basics_course/week_01/day_04_request_body_pydantic/practice.py
```

Мини-проект:
```powershell
docker compose exec api python fastapi_basics_course/week_02/day_07_capstone_task_api/task_api.py
```

## Как запускать сервер руками
```powershell
docker compose exec api uvicorn fastapi_basics_course.week_02.day_07_capstone_task_api.task_api:app --host 0.0.0.0 --port 8000
```

После этого API будет доступен на `http://localhost:8000`.

## Reset
Если нужно пересобрать образ с нуля:
```powershell
docker compose down
docker compose up -d --build
```
