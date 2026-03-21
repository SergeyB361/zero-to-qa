# Неделя 6, День 5 — AI для review и debug

## Где AI особенно полезен
- первичный code review
- разбор traceback
- поиск подозрительных мест в коде
- анализ логов и гипотез о root cause

## Чем AI полезен в review
Он быстро:
- замечает дублирование
- ищет явные smell'ы
- предлагает тесты на пропущенные кейсы

## Но есть ограничения
- AI не всегда чувствует продуктовый контекст
- может назвать стиль проблемой там, где важнее поведение
- может пропустить скрытый баг

## Правильный режим работы
Использовать AI как первый фильтр, а не как финальное заключение.

## Что считать хорошим AI-review
Хороший ответ:
- называет конкретные риски
- ссылается на поведение кода
- отделяет баги от вкусовщины
- предлагает недостающие тесты

## Что считать слабым AI-review
- общие слова без привязки к коду
- советы в духе "улучшить читаемость"
- выдуманные проблемы, которых нет в проекте

## Официальные материалы
- [OpenAI Working with evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [GitHub Copilot best practices](https://docs.github.com/en/copilot/get-started/best-practices)
- [Общий список материалов недели](C:/Users/serge/zero-to-qa/week_06/references.md)

## Практика дня
Открой `practice.py` и потренируй AI-oriented review и debug на реальных учебных файлах курса.
