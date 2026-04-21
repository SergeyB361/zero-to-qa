# Spec — Task API

## Обязательные endpoint'ы
- `GET /tasks`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `PATCH /tasks/{task_id}/status`
- `DELETE /tasks/{task_id}`

## Модель задачи
- `id`
- `title`
- `status`
- `assignee`
