# Capstone Backend Service

## Цель
Собрать небольшой backend-service на `FastAPI + SQLAlchemy + Postgres`.

## Минимальный запуск
```powershell
docker compose up --build
```

После запуска:
```powershell
curl http://localhost:8000/health
```

Ожидаемый ответ:
```json
{"status": "ok"}
```

## Локальная проверка без Docker
```powershell
python backend_service_capstone.py
pytest test_backend_service.py
```

## Что нужно доделать
- реализовать `ItemService.create_item`;
- реализовать `ItemService.patch_item`;
- реализовать `ItemService.soft_delete_item`;
- подключить Alembic revision из `alembic_revision.py` в реальный migration flow;
- при необходимости расширить `Dockerfile` под структуру своего проекта;
- убедиться, что `run_smoke_checks()` и pytest проходят.

## Runtime env
- `DATABASE_URL`
- `MANAGER_TOKEN`
- `VIEWER_TOKEN`
