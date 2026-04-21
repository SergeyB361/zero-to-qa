# Путь с нуля до QA

Единая стартовая страница репозитория с курсами, дополнительными треками и pet project.

## Что есть в проекте
- `base_course/` — основной 12-недельный курс по Python, QA automation и портфолио.
- `advanced_course/` — расширенный QA-трек для более сильного инженерного уровня.
- `fastapi_basics_course/` — отдельный базовый backend-трек по FastAPI.
- `sqlalchemy_basics_course/` — отдельный базовый ORM-трек на SQLAlchemy.
- `fastapi_lab/` — Docker-окружение для FastAPI-практики.
- `postgres_lab/` — общее Postgres-окружение для новых SQL-курсов.
- `postgres_base_sql_course/` — новый базовый pure-SQL курс на Postgres.
- `postgres_advanced_sql_course/` — новый продвинутый pure-SQL курс на Postgres.
- `postgres_sql_in_practice_course/` — новый applied SQL-трек на Postgres.
- `base_sql_course/` — legacy SQLite pure-SQL курс, оставлен для истории.
- `advanced_sql_course/` — legacy SQLite advanced SQL курс, оставлен для истории.
- `sql_in_practice_course/` — legacy SQLite applied SQL курс, оставлен для истории.
- `base_algorithms_course/` — базовый курс по алгоритмам и структурам данных.
- `advanced_algorithms_course/` — продвинутый алгоритмический трек.
- `pet_project/` — отдельный проект для практики backend/API-мышления.

## Рекомендуемый порядок
1. `base_course`
2. `postgres_base_sql_course`
3. `base_algorithms_course`
4. `fastapi_basics_course`
5. `sqlalchemy_basics_course`
6. `pet_project` как подготовка и проектирование
7. `advanced_course`
8. `postgres_advanced_sql_course`
9. `postgres_sql_in_practice_course`
10. `advanced_algorithms_course`

Legacy SQL-треки на `SQLite` сохранены в репозитории отдельно и не удаляются, но основной путь дальше — через `Postgres`.

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


## FastAPI Basics
**Для кого:** после базового Python и до первого backend pet project.
**Цель:** отдельно закрыть framework-базу по FastAPI без смешивания с ORM.
**Длительность:** `2` недели.
**Что внутри:** routes, request/response models, dependencies, APIRouter, TestClient, auth headers, middleware, lifespan.

Ключевые недели:
- `fastapi_basics_course/week_01/` — Core FastAPI
- `fastapi_basics_course/week_02/` — Structure, testing and applied patterns

Связанные файлы:
- `fastapi_basics_course/README.md`
- `fastapi_basics_course/ROADMAP.md`

## SQLAlchemy Basics
**Для кого:** после базового Postgres SQL и после FastAPI basics.
**Цель:** закрыть ORM-слой между raw SQL и реальным backend-кодом.
**Длительность:** `2` недели.
**Что внутри:** engine/session/base, модели и relationships, CRUD, query patterns, repository/service layer, FastAPI integration, migrations intro.

Ключевые недели:
- `sqlalchemy_basics_course/week_01/` — Core ORM
- `sqlalchemy_basics_course/week_02/` — Applied ORM patterns

Связанные файлы:
- `sqlalchemy_basics_course/README.md`
- `sqlalchemy_basics_course/ROADMAP.md`

## Базовый SQL-курс (Postgres)
**Для кого:** после начального Python и первых данных/файлов.
**Цель:** собрать фундамент по чистому SQL уже на реальном Postgres runtime.
**Длительность:** `4` недели.
**Что внутри:** setup через `postgres_lab`, SELECT, фильтрация, JOIN, GROUP BY, HAVING, подзапросы, схема данных, set operations, CASE, date/time и Postgres-specific patterns.

Ключевые недели:
- `postgres_base_sql_course/week_01/` — Базовые запросы и изменения данных
- `postgres_base_sql_course/week_02/` — Агрегации и JOIN
- `postgres_base_sql_course/week_03/` — Подзапросы и схема данных
- `postgres_base_sql_course/week_04/` — Postgres-native SQL: закрепление

Связанные файлы:
- `postgres_lab/README.md`
- `postgres_base_sql_course/README.md`
- `postgres_base_sql_course/ROADMAP.md`

## Продвинутый SQL-курс (Postgres)
**Для кого:** после базового Postgres SQL-трека.
**Цель:** перейти к real-world SQL: планы выполнения, индексы, consistency, reporting и investigation.
**Длительность:** `4` недели.
**Что внутри:** CTE, recursive CTE, window functions, ranking, `EXPLAIN ANALYZE`, индексы, locks, MVCC, views, JSONB и investigation patterns.

Ключевые недели:
- `postgres_advanced_sql_course/week_01/` — CTE и аналитические функции
- `postgres_advanced_sql_course/week_02/` — Планы выполнения и индексы
- `postgres_advanced_sql_course/week_03/` — Transactions и consistency
- `postgres_advanced_sql_course/week_04/` — Reporting и investigation

Связанные файлы:
- `postgres_lab/README.md`
- `postgres_advanced_sql_course/README.md`
- `postgres_advanced_sql_course/ROADMAP.md`

## SQL in Practice (Postgres)
**Для кого:** после базового Postgres SQL или параллельно с ним как applied-слой.
**Цель:** научиться использовать Postgres в Python, тестах, миграциях, CI и инженерных расследованиях.
**Длительность:** `2` недели.
**Что внутри:** Docker workflow, `psql`, `DBeaver`, `psycopg`, DB-checks, setup/cleanup, migrations, debugging with `EXPLAIN`, backend/API analysis.

Ключевые недели:
- `postgres_sql_in_practice_course/week_01/` — Postgres в локальной и тестовой работе
- `postgres_sql_in_practice_course/week_02/` — Applied workflows вокруг Postgres

Связанные файлы:
- `postgres_lab/README.md`
- `postgres_sql_in_practice_course/README.md`
- `postgres_sql_in_practice_course/ROADMAP.md`

## Legacy SQL-треки (SQLite / history)
Старые SQL-курсы не удалены и остаются в репозитории как историческая версия:
- `base_sql_course/`
- `advanced_sql_course/`
- `sql_in_practice_course/`

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
Python- и QA-курсы обычно содержат:
```text
course_name/week_XX/
  day_XX_topic/
    notes.md
    examples.py
    practice.py
```

Мини-проектный день в Python- и QA-курсах обычно содержит:
```text
course_name/week_XX/
  day_XX_miniproject_name/
    notes.md
    spec.md
    main_file.py
```

Pure SQL-треки содержат SQL-native файлы без Python-обвязки:
```text
sql_course/week_XX/
  day_XX_topic/
    notes.md
    examples.sql
    practice.sql
```

Мини-проектный день в pure SQL-треках обычно содержит:
```text
sql_course/week_XX/
  day_XX_miniproject_name/
    notes.md
    spec.md
    main_file.sql
```

Некоторые уроки дополнительно включают `.txt`, `.json`, `.csv` и другие data-файлы для практики.

## Стек
Python 3.14 · FastAPI · PyTest · Requests · Playwright · Postgres · SQLite (legacy) · Allure · GitHub Actions
