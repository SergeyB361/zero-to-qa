# Дорожная карта реализации pet project

## Прогресс реализации

```
Этап 1    Каркас       ████████████████  100%
Этап 2    Task API     ████████████████  100%
Этап 3    Audit API    ████████████████  100%
Этап 4    Интеграция   ████████████████  100%
Этап 5    Timeline     ████████████████  100%
Этап 6    Финализация  ████████████████  100%
```

## Статус
MVP собран, протестирован и уже пригоден для показа как portfolio project.

Подтверждено:
- локальный запуск обоих сервисов;
- запуск через `docker compose`;
- `pytest` для `task_service` и `audit_timeline_service`;
- live flow `create -> status -> assignee -> delete -> timeline -> snapshot`.

---

## Выполненные этапы

### Этап 1 — Подготовка каркаса проекта
- [x] Создана структура папок проекта
- [x] Поднят `Task Service`
- [x] Поднят `Audit Timeline Service`
- [x] Добавлены health endpoint'ы
- [x] Проверен локальный запуск обоих сервисов

### Этап 2 — Базовый Task Service
- [x] Реализована модель `Task`
- [x] Настроен SQLite для `Task Service`
- [x] Сделан `POST /tasks`
- [x] Сделан `GET /tasks/{task_id}`
- [x] Сделан `GET /tasks`
- [x] Сделан `PATCH /tasks/{task_id}/status`
- [x] Сделан `PATCH /tasks/{task_id}/assignee`
- [x] Сделан `DELETE /tasks/{task_id}`

### Этап 3 — Audit Timeline Service
- [x] Реализована модель события
- [x] Настроен SQLite для `Audit Timeline Service`
- [x] Сделан `POST /events`
- [x] Сделан `GET /events`
- [x] Сделан `GET /events/{event_id}`
- [x] Обеспечено append-only хранение событий

### Этап 4 — Интеграция сервисов
- [x] `Task Service` формирует событие после действия
- [x] Событие отправляется по HTTP в `Audit Timeline Service`
- [x] Обработан базовый сценарий ошибки отправки через `502 Bad Gateway`
- [x] Проверена цепочка `действие -> событие -> сохранение`

### Этап 5 — Timeline и Snapshot
- [x] Сделан `GET /timeline/tasks/{task_id}`
- [x] Сделан `GET /timeline/users/{actor_id}`
- [x] Сделан `GET /snapshot/tasks/{task_id}`
- [x] Проверено восстановление состояния задачи по событиям

### Этап 6 — Тесты, README и demo flow
- [x] Написаны базовые тесты
- [x] Описан запуск проекта
- [x] Оформлен README
- [x] Подготовлен demo flow
- [x] Код доведён до состояния демонстрационного MVP
- [x] Добавлен Docker Compose для воспроизводимого запуска

---

## Post-MVP backlog
- вынести event publishing в outbox/retry-механику;
- перейти с SQLite на Postgres;
- добавить auth и actor extraction из запроса;
- добавить фильтрацию, пагинацию и сортировку;
- добавить integration tests поверх двух реально поднятых сервисов;
