# Обзор курсов и треков проекта

Этот документ даёт короткую карту всего репозитория: какие курсы есть, зачем они нужны, в каком порядке их проходить и какую роль они играют в общей программе.

Репозиторий уже не является одним линейным курсом. Сейчас это учебная программа из нескольких направлений:
- основной путь к `Junior QA Automation`;
- отдельная backend-линия;
- SQL-линия на `Postgres`;
- алгоритмические треки;
- инфраструктурные labs;
- legacy SQL-курсы на `SQLite`;
- pet project.

## Главная идея программы

Программа строится не только вокруг QA automation. Базовый маршрут даёт Python, тестирование, API/UI automation и портфолио. Дополнительные треки закрывают инженерные пробелы, которые часто встречаются в вакансиях и на собеседованиях:
- уверенный Python;
- SQL и базы данных;
- алгоритмы и структуры данных;
- FastAPI;
- ORM через SQLAlchemy;
- Docker и Postgres runtime;
- backend application structure;
- реальные API/backend workflows.

Поэтому проект можно проходить двумя способами.

Первый способ — как QA automation программу:
1. `base_course`
2. `postgres_base_sql_course`
3. `base_algorithms_course`
4. `advanced_course`
5. `postgres_sql_in_practice_course`
6. `pet_project`

Второй способ — как Python/backend-oriented программу:
1. `base_course`
2. `postgres_base_sql_course`
3. `fastapi_basics_course`
4. `sqlalchemy_basics_course`
5. `backend_application_patterns_course`
6. `pet_project`
7. `postgres_advanced_sql_course`
8. `base_algorithms_course`
9. `advanced_algorithms_course`

## Основной QA-путь

### `base_course`

Это главный стартовый курс проекта. Он рассчитан на движение с нуля или с фрагментарной базой.

Цель курса — довести студента до уровня, на котором он понимает Python, может писать автотесты, работать с API/UI, оформлять проект и объяснять свой код.

Курс покрывает:
- Python syntax и типы данных;
- функции, файлы, JSON, exceptions, logging;
- ООП;
- PyTest;
- API testing;
- UI testing через Playwright;
- SQL и инструменты;
- GitHub Actions;
- портфолио и резюме.

Роль в программе: обязательный фундамент. Даже если цель не QA, а backend, этот курс закрывает базовый Python и инженерную дисциплину.

### `advanced_course`

Это расширенный QA-трек после базового курса. Он нужен не для первого входа, а для усиления инженерного уровня.

Курс покрывает:
- advanced PyTest;
- test data engineering;
- advanced API testing;
- advanced UI testing;
- CI и test infrastructure;
- observability;
- security/performance basics;
- test strategy;
- requirements engineering;
- quality engineering.

Дополнительно внутри есть `bonus_advanced_python_oop`, который углубляет Python OOP через магические методы, descriptors, dataclasses, `__slots__` и богатую доменную модель.

Роль в программе: усилить QA automation до уровня, где студент думает не только тестами, но и архитектурой качества.

## Backend-линия

Backend-линия появилась как ответ на требования уровня `FastAPI + ORM + SQL + Git + Docker`. Она не заменяет QA-курс, а дополняет его.

### `fastapi_basics_course`

Курс закрывает базу FastAPI без смешивания с ORM и сложной инфраструктурой.

Курс покрывает:
- ASGI и роль FastAPI;
- routes и HTTP methods;
- path/query params;
- request body через Pydantic;
- response models;
- errors;
- dependencies;
- APIRouter;
- TestClient;
- auth headers;
- middleware и lifespan.

Практики устроены как scaffold с `run_checks()` или `run_smoke_checks()`. Это значит, что студент видит задание, пример ожидаемого результата и автоматический критерий готовности.

Роль в программе: дать framework-базу перед ORM и полноценным backend service.

### `fastapi_lab`

Это Docker runtime для FastAPI-практики.

Он нужен, чтобы запуск практики был воспроизводимым:
- одинаковые зависимости;
- один способ запуска;
- меньше проблем с локальным окружением.

Роль в программе: инфраструктурный помощник, не отдельный теоретический курс.

### `sqlalchemy_basics_course`

Курс закрывает ORM-слой между raw SQL и backend-кодом.

Курс покрывает:
- engine и session;
- declarative models;
- columns и constraints;
- CRUD lifecycle;
- relationships;
- select/filter/order patterns;
- transactions;
- loading strategies;
- repository/service pattern;
- FastAPI integration;
- Alembic introduction.

Роль в программе: научить связывать Python-объекты и таблицы базы без потери понимания SQL.

### `backend_application_patterns_course`

Это курс, который собирает отдельные backend-темы в нормальный service-oriented backend.

Курс покрывает:
- project layout;
- settings и env config;
- dependency boundaries;
- API error contracts;
- CRUD style;
- SQLAlchemy session patterns;
- Postgres integration;
- Alembic basics;
- schema evolution;
- auth, roles, permissions;
- filtering, sorting, pagination;
- partial update и soft delete;
- integration testing;
- seed data и factories;
- Docker Compose;
- CI basics;
- final backend capstone.

Главная ценность курса — не в новых инструментах, а в связке: route не должен знать всё, service не должен заниматься HTTP, repository не должен принимать бизнес-решения, настройки должны приходить из config/env.

Роль в программе: закрыть переход от "умею написать endpoint" к "умею собрать backend-приложение".

## SQL-линия на Postgres

Postgres-треки являются основным SQL-направлением. Старые SQLite-курсы сохранены для истории, но дальнейший основной путь построен вокруг Postgres.

### `postgres_lab`

Общее окружение Postgres для SQL-курсов и applied-практики.

Внутри:
- `docker-compose.yml`;
- init scripts;
- schema и seed data;
- инструкции запуска;
- reset workflow через `docker compose down -v`.

Роль в программе: дать одну живую базу для всех Postgres-треков.

### `postgres_base_sql_course`

Базовый pure SQL курс на Postgres.

Курс покрывает:
- setup и tooling;
- `SELECT`;
- `WHERE`, `ORDER BY`, `LIMIT`;
- `INSERT`, `UPDATE`, `DELETE`;
- `NULL`, `LIKE`, `IN`, `BETWEEN`;
- `DISTINCT`, aliases, functions;
- aggregates;
- `GROUP BY`, `HAVING`;
- `INNER JOIN`, `LEFT JOIN`, multi-join patterns;
- subqueries;
- `EXISTS` / `NOT EXISTS`;
- DDL;
- keys и constraints;
- Postgres types и identity;
- transactions;
- set operations;
- `CASE`, `COALESCE`, `NULLIF`;
- date/time queries;
- финальный analytical SQL report.

Курс pure SQL: в нём нет Python-обвязки. Студент работает с `.sql` файлами и живым Postgres.

Роль в программе: закрыть уверенное владение SQL на уровне junior/junior+.

### `postgres_advanced_sql_course`

Продвинутый pure SQL курс.

Курс покрывает:
- CTE;
- recursive CTE;
- window functions;
- ranking;
- `LEAD`, `LAG`, running totals;
- indexes;
- `EXPLAIN` и `EXPLAIN ANALYZE`;
- join optimization;
- query rewrites;
- SQL anti-patterns;
- ACID;
- isolation levels;
- locks;
- constraints и integrity;
- MVCC;
- views и materialized views;
- reporting queries;
- time series analytics;
- data quality queries;
- JSONB basics;
- final SQL investigation pack.

Роль в программе: вывести SQL за рамки учебных запросов и приблизить его к реальной работе с производительностью, расследованиями и сложной аналитикой.

### `postgres_sql_in_practice_course`

Applied SQL трек на Postgres.

Курс покрывает:
- Docker workflow для Postgres;
- `psql` и DBeaver workflow;
- `psycopg`;
- DB checks in tests;
- test data setup/cleanup;
- debugging with `EXPLAIN`;
- DB checks toolkit;
- migrations basics;
- backend/API analysis;
- query logging and artifacts;
- realistic QA investigations;
- fixtures and seed strategies;
- CI database workflows;
- bug investigation capstone.

Роль в программе: показать, как SQL и Postgres используются не в изоляции, а в Python, тестах, backend debugging и CI.

## Алгоритмы и структуры данных

Алгоритмическая линия вынесена отдельно, чтобы не перегружать основной QA-курс, но дать сильный фундамент для Python-собеседований и общего инженерного мышления.

### `base_algorithms_course`

Базовый курс по алгоритмам и структурам данных.

Курс покрывает:
- что такое алгоритм;
- Big O;
- числовые алгоритмы;
- binary search;
- базовые сортировки;
- hash-based patterns;
- `dict` / `set`;
- prefix sums;
- stack, queue, deque;
- sliding window;
- two pointers;
- интервальные задачи.

Роль в программе: дать базу для решения типовых задач и понимания сложности.

### `advanced_algorithms_course`

Продвинутый алгоритмический курс.

Курс покрывает:
- recursion;
- divide and conquer;
- linked list;
- slow/fast pointers;
- trees;
- DFS по дереву;
- heap;
- graph representation;
- BFS/DFS;
- route finding;
- mixed review;
- final algorithmic toolkit.

Роль в программе: расширить алгоритмический фундамент до уровня, где студент понимает не только встроенные структуры Python, но и классические структуры и обходы.

## Legacy SQL-треки на SQLite

Старые SQL-треки сохранены для истории:
- `base_sql_course`;
- `advanced_sql_course`;
- `sql_in_practice_course`.

Они уже не являются основным SQL-путём. Их ценность сейчас:
- посмотреть старую версию курса;
- сравнить SQLite и Postgres подходы;
- иметь лёгкий вариант без Docker/Postgres, если окружение временно недоступно.

Основной актуальный путь — через `postgres_*`.

## Pet Project

### `pet_project`

Это отдельный практический проект, который закрепляет backend/API thinking.

Сейчас проект уже не пустой scaffold. В нём есть MVP из двух сервисов:
- `task_service`;
- `audit_timeline_service`.

Проект показывает:
- FastAPI service;
- SQLAlchemy data layer;
- service/repository style;
- доменные события;
- timeline;
- snapshot;
- Docker Compose runtime.

Роль в программе: связать учебные темы в демонстрируемый проект для портфолио.

## Как выбирать маршрут

Если цель — QA Automation:
1. `base_course`
2. `postgres_base_sql_course`
3. `base_algorithms_course`
4. `advanced_course`
5. `postgres_sql_in_practice_course`
6. `pet_project`

Если цель — Python backend junior:
1. `base_course`
2. `postgres_base_sql_course`
3. `fastapi_basics_course`
4. `sqlalchemy_basics_course`
5. `backend_application_patterns_course`
6. `pet_project`
7. `postgres_advanced_sql_course`

Если цель — усилить собеседования:
1. `base_course`
2. `base_algorithms_course`
3. `advanced_algorithms_course`
4. `postgres_base_sql_course`
5. `postgres_advanced_sql_course`

Если цель — не строить новые курсы, а учиться:
1. вернуться в текущий день `base_course`;
2. проходить материалы в порядке `notes -> examples -> practice`;
3. запускать self-check;
4. фиксировать прогресс небольшими коммитами.

## Общий вывод

Проект сейчас закрывает не один навык, а несколько связанных направлений:
- Python foundation;
- QA automation;
- SQL/Postgres;
- algorithms;
- FastAPI;
- SQLAlchemy;
- backend architecture;
- Docker runtime;
- pet project.

Главная ценность структуры в том, что треки можно проходить независимо, но вместе они собираются в сильный Python/QA/backend фундамент.
