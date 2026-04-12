# Путь с нуля до QA

Единая стартовая страница репозитория с курсами, дополнительными треками и pet project.

## Что есть в проекте
- `base_course/` — основной 12-недельный курс по Python, QA automation и портфолио.
- `advanced_course/` — расширенный QA-трек для более сильного инженерного уровня.
- `base_sql_course/` — базовый pure-SQL курс.
- `advanced_sql_course/` — продвинутый pure-SQL курс.
- `sql_in_practice_course/` — прикладной SQL-трек для Python, тестов и расследований.
- `base_algorithms_course/` — базовый курс по алгоритмам и структурам данных.
- `advanced_algorithms_course/` — продвинутый алгоритмический трек.
- `pet_project/` — отдельный проект для практики backend/API-мышления.

## Рекомендуемый порядок
1. `base_course`
2. `base_sql_course`
3. `base_algorithms_course`
4. `pet_project` как подготовка и проектирование
5. `advanced_course`
6. `advanced_sql_course`
7. `sql_in_practice_course`
8. `advanced_algorithms_course`

## Основной курс
**Для кого:** старт с нуля или после очень фрагментарной базы.
**Цель:** дойти до уровня Junior QA Automation Engineer.
**Длительность:** `12` недель.
**Что внутри:** Python, структуры данных, продвинутый Python, ООП, PyTest, API, UI, SQL, AI в тестировании, портфолио.

Ключевые недели:
- `base_course/week_01/` — Python с нуля
- `base_course/week_05/` — Основы тестирования + PyTest
- `base_course/week_06/` — Тестирование API
- `base_course/week_07/` — UI-тестирование (Playwright)
- `base_course/week_08/` — SQL + Инструменты
- `base_course/week_10/` — Портфолио + Резюме

Связанные файлы:
- `ROADMAP.md` — общий roadmap основного и расширенного QA-трека
- `base_course/` — материалы по дням

## Расширенный QA-курс
**Для кого:** после прохождения основного курса или при уже сильной базе.
**Цель:** перейти от junior-level практики к более зрелому инженерному подходу.
**Длительность:** `10` недель + bonus-блок по Advanced Python OOP.
**Что внутри:** advanced PyTest, test data engineering, advanced API/UI, CI, observability, test design, quality engineering.

Ключевые недели:
- `advanced_course/week_01/` — PyTest: продвинутый уровень
- `advanced_course/week_03/` — API: продвинутый уровень
- `advanced_course/week_05/` — UI: продвинутый уровень
- `advanced_course/week_09/` — Test Design и Requirements Engineering
- `advanced_course/week_10/` — Quality Engineering и системное мышление
- `advanced_course/bonus_advanced_python_oop/` — Bonus: Advanced Python OOP

Связанные файлы:
- `ROADMAP.md` — общий roadmap основного и расширенного QA-трека
- `advanced_course/` — материалы по дням

## Базовый SQL-курс
**Для кого:** после начального Python и первых данных/файлов.
**Цель:** собрать фундамент по чистому SQL без Python-слоя внутри уроков.
**Длительность:** `4` недели.
**Что внутри:** SELECT, фильтрация, JOIN, GROUP BY, HAVING, подзапросы, схема данных, set operations, CASE, date/time и composite queries.

Ключевые недели:
- `base_sql_course/week_01/` — SELECT и фильтрация
- `base_sql_course/week_02/` — Агрегации и JOINs
- `base_sql_course/week_03/` — Подзапросы и схема данных
- `base_sql_course/week_04/` — Чистый SQL: закрепление

Связанные файлы:
- `base_sql_course/README.md`
- `base_sql_course/ROADMAP.md`

## Продвинутый SQL-курс
**Для кого:** после базового SQL-трека.
**Цель:** перейти к advanced SQL без смешения с Python- и QA-интеграцией.
**Длительность:** `4` недели.
**Что внутри:** CTE, window functions, ranking, indexes, `EXPLAIN`, recursive CTE, pivot-like отчёты, time-series analytics, integrity и consistency.

Ключевые недели:
- `advanced_sql_course/week_01/` — Advanced querying
- `advanced_sql_course/week_02/` — Optimization and indexing
- `advanced_sql_course/week_03/` — Transactions and consistency
- `advanced_sql_course/week_04/` — Advanced SQL reporting

Связанные файлы:
- `advanced_sql_course/README.md`
- `advanced_sql_course/ROADMAP.md`

## SQL in Practice
**Для кого:** после базового SQL или параллельно с ним как applied-слой.
**Цель:** научиться использовать SQL в Python, тестах, миграциях и инженерных расследованиях.
**Длительность:** `1` неделя + bonus.
**Что внутри:** SQLite в Python, DB-checks, cleanup, migrations, debugging workflows, investigation toolkit.

Ключевые недели:
- `sql_in_practice_course/week_01/` — SQL в Python и тестах
- `sql_in_practice_course/bonus_backend_api_analysis/` — bonus: SQL для backend и API-анализа

Связанные файлы:
- `sql_in_practice_course/README.md`
- `sql_in_practice_course/ROADMAP.md`

## Базовый алгоритмический курс
**Для кого:** как параллельный фундаментальный трек после начального Python.
**Цель:** собрать базу по сложности, поиску, сортировкам, hash-based паттернам и очередям.
**Длительность:** `5` недель.
**Что внутри:** Big O, числовые алгоритмы, бинарный поиск, сортировки, dict/set, prefix sums, stack/queue/deque.

Ключевые недели:
- `base_algorithms_course/week_01/` — Введение в алгоритмы
- `base_algorithms_course/week_02/` — Числовые алгоритмы
- `base_algorithms_course/week_03/` — Поиск и сортировки
- `base_algorithms_course/week_04/` — Hash-based подходы
- `base_algorithms_course/week_05/` — Stack, Queue, Deque

Связанные файлы:
- `base_algorithms_course/README.md`
- `base_algorithms_course/ROADMAP.md`

## Продвинутый алгоритмический курс
**Для кого:** после базового алгоритмического трека.
**Цель:** перейти к рекурсии, связным структурам, деревьям, heap, графам и mixed problem solving.
**Длительность:** `3` недели.
**Что внутри:** recursion, divide and conquer, linked list, trees, heap, BFS/DFS, final toolkit.

Ключевые недели:
- `advanced_algorithms_course/week_01/` — Рекурсия, связные структуры и деревья
- `advanced_algorithms_course/week_02/` — Heap и графы
- `advanced_algorithms_course/week_03/` — Продвинутые паттерны и итоговый toolkit

Связанные файлы:
- `advanced_algorithms_course/README.md`
- `advanced_algorithms_course/ROADMAP.md`

## Pet Project
**Для кого:** после блока Python + API или параллельно как медленный проектный трек.
**Цель:** собрать MVP, который выглядит как реальный junior backend/API pet project.
**Что внутри:** два сервиса, события, timeline, roadmap реализации и синхронизация с курсом.

Связанные файлы:
- `pet_project/README.md`
- `pet_project/spec.md`
- `pet_project/ROADMAP.md`
- `pet_project/COURSE_ALIGNMENT.md`

## Формат материалов
Обычный учебный день обычно содержит:
```text
course_name/week_XX/
  day_XX_topic/
    notes.md
    examples.py
    practice.py
```

Мини-проектный день обычно содержит:
```text
course_name/week_XX/
  day_XX_miniproject_name/
    notes.md
    spec.md
    main_file.py
```

Некоторые уроки дополнительно включают `.txt`, `.json` и другие data-файлы для практики.

## Стек
Python 3.14 · PyTest · Requests · Playwright · SQLite · Allure · GitHub Actions
