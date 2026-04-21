# FastAPI Basics

**Цель:** дать отдельный базовый трек по FastAPI без смешивания с ORM.
**Длительность:** `2 недели`
**Статус:** курс наполнен полностью по `week_01-week_02`.

## Для кого
- после базового Python;
- перед первым backend pet project;
- чтобы закрыть framework-gap отдельно от QA и SQL.

## Что внутри
- routes, params, request body, Pydantic;
- response_model, status codes, HTTPException;
- dependencies, APIRouter, project structure;
- service layer, in-memory repository;
- TestClient, auth header, middleware, CORS, lifespan;
- два мини-проекта.

## Что не входит
- ORM и БД-слой;
- Alembic и миграции;
- production deployment;
- сложная auth-модель.

## Setup
```powershell
python -m pip install fastapi uvicorn pytest httpx
```

## Docker-путь
Если не хочешь зависеть от локального `venv`, используй [fastapi_lab](../fastapi_lab/README.md):

```powershell
cd fastapi_lab
docker compose up -d --build
docker compose exec api python fastapi_basics_course/week_01/day_04_request_body_pydantic/practice.py
```

## Как проходить урок
1. Сначала читать `notes.md` и понять механизм, а не только синтаксис.
2. Затем открыть `examples.py` и посмотреть минимальный рабочий эталон.
3. Потом делать `practice.py`.
4. После решения запускать `practice.py` снова: встроенный `run_checks()` должен пройти без ошибок.

## Как понимать self-check
- Если `practice.py` падает, это нормально: значит задание ещё не доведено до правильного результата.
- Сообщение `Self-check failed: ...` показывает, что именно ещё не выполнено.
- В мини-проектах вместо `run_checks()` используются `run_smoke_checks()`.
- Для route-уроков основной критерий правильности — `status code`, JSON-ответ и error path.

## Где описано практическое задание
У каждого урока практическая часть сейчас читается так:
1. `notes.md` — объясняет механизм и границы темы.
2. `examples.py` — показывает минимальный эталон.
3. `practice.py` — это и есть задание. Его нужно дочинить так, чтобы `run_checks()` проходил без ошибок.

То есть формулировка задания находится в самом `practice.py` через:
- незавершённые места (`TODO`);
- ожидаемый контракт endpoint-ов;
- проверки внутри `run_checks()`.

Если нужно совсем короткое правило: **задание выполнено верно тогда, когда `practice.py` проходит полностью без `AssertionError`**.

## Недели
- `week_01/` — Core FastAPI
- `week_02/` — Structure, testing and applied patterns
