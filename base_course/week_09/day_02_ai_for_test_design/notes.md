# Неделя 9, День 2 — AI для тест-дизайна

## Где AI особенно полезен
AI хорошо помогает на раннем этапе:
- набросать test cases
- предложить edge cases
- напомнить про негативные сценарии
- помочь с risk-based мышлением

## Что у него получается лучше всего
- быстро расширять список идей
- находить очевидные пропуски
- формировать черновик чеклиста

## Что он делает слабо
- не знает реальный продуктовый контекст
- может предлагать лишние и искусственные кейсы
- не отличает важное от второстепенного без хорошего промпта

## Практическое правило
Проси у AI не просто “дай тест-кейсы”, а:
- для какой функции
- с какими ограничениями
- какие риски важнее всего

## Как сделать задачу сильнее
Лучше брать не абстрактную функцию, а реальный код из курса.

Подходящие цели:
- функции из `base_course/week_01/day_07_miniproject_calculator`
- парсер из `base_course/week_02/day_07_miniproject_json_parser`
- методы из `base_course/week_04/day_07_miniproject_user_admin/solution_users_system.py`

## Хороший результат от AI
Полезный ответ на test design задачу обычно:
- разделяет позитивные, негативные и граничные кейсы
- не придумывает несуществующее поведение
- указывает рисковые зоны
- не подменяет тест-дизайн водой

## Официальные материалы
- [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [Anthropic Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [GitHub Copilot prompt engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [Общий список материалов недели](C:/Users/serge/zero-to-qa/base_course/week_09/references.md)

## Практика дня
Открой `practice.py` и потренируй формулировки промптов на реальных функциях курса.
