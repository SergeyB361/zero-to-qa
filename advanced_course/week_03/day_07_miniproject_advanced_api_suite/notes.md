# API: продвинутый уровень, День 7 — Мини-проект: Advanced API suite

## Что это за день

Это мини-проект про зрелый API-suite, а не про набор несвязанных запросов.

Здесь нужно соединить:
- auth flows;
- retries и idempotency thinking;
- negative scenarios;
- schema и contract checks;
- controlled dependencies, если они нужны.

## Что здесь проверяется

Мини-проект проверяет, умеешь ли ты:
- строить API coverage слоями;
- отделять auth, contract, negative и stateful scenarios;
- оформлять suite так, чтобы его можно было расширять;
- объяснять, какой риск закрывает каждая группа тестов.

## Как правильно проходить

1. Сначала прочитай `spec.md`.
2. Затем выдели критичные API-risks.
3. Раздели будущий suite на смысловые слои.
4. Только после этого собирай тесты, helpers и checks.

## Что считается хорошим результатом

По сильному решению видно:
- где auth layer;
- где negative coverage;
- где contract/schema checks;
- как читается stateful lifecycle сущности;
- что suite не разваливается на случайный набор файлов.

## На что обратить внимание

- не смешивай transport helpers и business assertions;
- не ограничивайся status-code-only проверками;
- не делай contract checks декоративными;
- следи, чтобы каждый тестовый слой отвечал на свой тип риска.

## Что делать дальше

1. Открой [spec.md](/C:/Users/serge/zero-to-qa/advanced_course/week_03/day_07_miniproject_advanced_api_suite/spec.md).
2. Собери компактный, но объяснимый advanced API suite.
3. После выполнения проверь, можно ли по структуре проекта понять, какие риски он закрывает.
