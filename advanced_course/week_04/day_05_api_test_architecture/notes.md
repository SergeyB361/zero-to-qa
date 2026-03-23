# API: reliability и integration, День 5 — API test architecture

## Зачем это нужно
- Небольшой набор API-тестов можно держать в одном файле, но зрелый проект требует слоёв.
- Client, service, builders и utils уменьшают дублирование.
- Архитектура напрямую влияет на поддерживаемость тестов.

## Что важно понять
- Transport layer, domain helpers и tests должны быть разделены.
- Auth headers и endpoint paths лучше выносить из тестов.
- Architecture должна уменьшать хаос, а не плодить бесполезные абстракции.

## Частые ошибки
- Raw requests по всем тестам.
- Одна giant utils.py на всё подряд.
- Преждевременная сложность без пользы.

## Практика дня
Открой practice.py и разложи API framework на слои.
