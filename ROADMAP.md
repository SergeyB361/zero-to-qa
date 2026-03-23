# 🐍 Junior QA Automation Engineer — базовый курс + расширенный трек

**Цель:** Python + PyTest + портфолио → Junior QA Automation Engineer
**Темп:** 4 часа в день | **Язык:** Русский

---

## НЕДЕЛЯ 1 — Python с нуля

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Настройка окружения    | venv, VS Code, Git init, структура проекта |
| 2 | Переменные и типы      | int, float, str, bool, None, type() |
| 3 | Условия                | if / elif / else, and / or / not |
| 4 | Циклы                  | for, while, range(), break, continue |
| 5 | Функции — основы       | def, параметры, return, scope |
| 6 | Функции — продвинуто   | *args, **kwargs, lambda, default args |
| 7 | **Мини-проект**        | Калькулятор с функциями и условиями |

---

## НЕДЕЛЯ 2 — Структуры данных

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Списки                 | list, индексы, срезы, append/remove/sort, list comprehension |
| 2 | Кортежи                | tuple, индексы, срезы, неизменяемость |
| 3 | Словари                | dict, get/keys/values/items, вложенные |
| 4 | Строки                 | f-строки, split/join/replace/strip |
| 5 | Файлы + JSON           | open/read/write, with, json.loads/dumps |
| 6 | Множества              | set, уникальность, add/remove, union/intersection |
| 7 | **Мини-проект**        | Парсер JSON-файла со статистикой |

---

## НЕДЕЛЯ 3 — Продвинутый Python для QA

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Исключения             | try/except/else/finally, raise, типы ошибок |
| 2 | Декораторы — база      | decorator, wrapper, @syntax, *args/**kwargs |
| 3 | Type hints             | type hints, Optional, list[str], dict[str, int] |
| 4 | Регулярные выражения   | re.search, re.findall, шаблоны, группы |
| 5 | Logging                | logging, уровни логов, формат сообщений |
| 6 | pathlib и утилиты      | Path, exists, glob, удобная работа с файлами |
| 7 | **Мини-проект**        | CLI-утилита анализа тестовых артефактов |

---

## НЕДЕЛЯ 4 — ООП

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Классы и объекты       | class, __init__, self, атрибуты |
| 2 | Методы                 | @classmethod, @staticmethod, __str__ |
| 3 | Наследование           | super(), дочерние классы, переопределение |
| 4 | Инкапсуляция           | @property, приватные атрибуты |
| 5 | ООП на практике        | Проектирование классов для тестов |
| 6 | Модули и пакеты        | import, from/import, __init__.py |
| 7 | **Мини-проект**        | Система пользователей: классы User, Admin |

---

## НЕДЕЛЯ 5 — Основы тестирования + PyTest

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Теория тестирования    | unit/integration/e2e, пирамида тестов, баг-репорт |
| 2 | Первые тесты PyTest    | test_*.py, запуск pytest, структура файла |
| 3 | Assertions             | assert, pytest.raises, проверка типов |
| 4 | AAA-паттерн            | Arrange / Act / Assert, именование тестов |
| 5 | Фикстуры — основы      | @pytest.fixture, setup/teardown |
| 6 | Запуск и отчёты        | pytest -v / -k / --tb, Allure: шаги/статусы/история |
| 7 | **Мини-проект**        | Набор тестов для функций из Недели 1–2 |

---

## НЕДЕЛЯ 6 — Тестирование API

| # | Тема | Что изучаем |
|---|------|-------------|
| 1 | HTTP и REST          | методы, коды ответов, JSON, headers |
| 2 | requests             | GET, POST, params, json, headers |
| 3 | Первые API-тесты     | PyTest + requests, проверки статуса и тела |
| 4 | Валидация данных     | JSON schema, ключи, типы, вложенные объекты |
| 5 | API тест-фреймворк   | clients, endpoints, utils, config |
| 6 | Авторизация в API    | token, headers, auth flow |
| 7 | **Мини-проект**      | CRUD API tests для reqres.in |

---

## НЕДЕЛЯ 7 — UI-тестирование (Playwright)

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Основы Playwright      | Установка, первый тест, headless-режим |
| 2 | Локаторы               | CSS, XPath, text, role селекторы |
| 3 | Действия               | click, fill, navigate, hover, screenshot |
| 4 | Assertions             | expect(), видимость / текст / URL |
| 5 | Page Object Model      | Паттерн POM, BasePage, дочерние страницы |
| 6 | Playwright + PyTest    | pytest-playwright, фикстуры browser/page |
| 7 | **Мини-проект**        | UI-тесты публичного сайта с POM |

---

## НЕДЕЛЯ 8 — SQL + Инструменты

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | SQL — основы           | SELECT, WHERE, INSERT, UPDATE, DELETE |
| 2 | SQLite в Python        | sqlite3, cursor, fetchall, проверка БД в тестах |
| 3 | Allure — углублённо    | @allure.step, @allure.title, attach, severity |
| 4 | Git для QA             | branch, commit, push, pull request, .gitignore |
| 5 | GitHub workflows       | Issues, README, Markdown, оформление репозитория |
| 6 | Повторение и практика  | API-тесты + Allure-отчёты + проверка БД вместе |
| 7 | **Мини-проект**        | API-тесты с Allure-отчётами и проверкой SQLite |

---

## НЕДЕЛЯ 9 — AI в тестировании и разработке ПО

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | AI-инструменты и роли  | ChatGPT, Codex, Cursor, Copilot, где что применять |
| 2 | AI для тест-дизайна    | генерация тест-кейсов, граничные значения, чек-листы |
| 3 | AI для генерации тестов | unit/API/UI тесты с последующей верификацией |
| 4 | AI-агенты и workflows  | multi-step задачи, оркестрация, review loop |
| 5 | AI для review и debug  | анализ логов, ошибок, flaky-тестов |
| 6 | Безопасное использование AI | privacy, secrets, валидация ответов, hallucinations |
| 7 | **Мини-проект**        | AI-assisted QA workflow |

---

## НЕДЕЛЯ 10 — Портфолио + Резюме

| # | Тема | Что делаем |
|---|------|-----------|
| 1 | Архитектура проекта    | Структура фреймворка, README, планирование |
| 2 | Unit-тесты             | Тесты с моками, покрытие базовых функций |
| 3 | API-тесты              | Полный набор: фикстуры, параметризация, Allure |
| 4 | UI-тесты               | POM + интеграция с API-тестами |
| 5 | GitHub Actions         | CI/CD: автозапуск тестов при push |
| 6 | Оформление GitHub      | README с бейджами, документация |
| 7 | **Резюме**             | Junior QA резюме, описание проекта, LinkedIn |

---

## НЕДЕЛЯ 11 — PyTest продвинутый уровень

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Параметризация         | @pytest.mark.parametrize |
| 2 | Маркеры                | @pytest.mark, skip, xfail, pytest.ini |
| 3 | conftest.py            | Общие фикстуры, scope: function/class/module/session |
| 4 | Моки — основы          | unittest.mock, MagicMock, patch |
| 5 | Моки — практика        | side_effect, return_value, mock как декоратор |
| 6 | Структура проекта      | Папки тестов, pytest.ini, requirements.txt |
| 7 | **Мини-проект**        | Параметризованные тесты с фикстурами и моками |

---

## НЕДЕЛЯ 12 — Финализация портфолио

| # | Тема | Что делаем |
|---|------|-----------|
| 1 | Архитектура финального проекта | чистка структуры, модули, нейминг |
| 2 | Unit-тесты             | улучшение покрытия, рефакторинг тестов |
| 3 | API-тесты              | доведение CRUD и валидаций |
| 4 | UI-тесты               | полировка POM и стабильности |
| 5 | CI/CD                  | финализация GitHub Actions |
| 6 | README и документация  | инструкции запуска, описание проекта |
| 7 | Резюме и LinkedIn      | упаковка результатов курса и pet project |

---


---

## РАСШИРЕННЫЙ КУРС

### НЕДЕЛЯ 1 — PyTest: продвинутый уровень

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Advanced fixtures      | fixture composition, scope, yield, teardown |
| 2 | Parametrization patterns | data-driven tests, ids, indirect parametrization |
| 3 | Markers и test selection | custom markers, selective runs, grouping |
| 4 | Mocking deeper         | patch, side_effect, spy pattern, isolation |
| 5 | Flaky tests            | причины нестабильности, диагностика, стабилизация |
| 6 | pytest-xdist           | параллельный запуск, shared state, порядок выполнения |
| 7 | **Мини-проект**        | Устойчивый PyTest suite |

---

### НЕДЕЛЯ 2 — Test Data Engineering

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Factories              | фабрики объектов, переиспользуемые данные |
| 2 | Builder pattern        | пошаговая сборка тестовых сущностей |
| 3 | Test data management   | хранение, версии, наборы данных, test fixtures |
| 4 | Property-based testing | hypothesis, strategies, генерация по свойствам |
| 5 | Edge cases             | граничные значения, equivalence classes |
| 6 | Reusable datasets      | повторное использование данных между слоями тестов |
| 7 | **Мини-проект**        | Генерация и проверка тестовых данных |

---

### НЕДЕЛЯ 3 — API: продвинутый уровень

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Auth flows             | token, OAuth, JWT, refresh, expiry |
| 2 | Retries и idempotency  | retry logic, safe methods, backoff |
| 3 | Negative scenarios     | bad payloads, auth failures, boundary cases |
| 4 | Schema validation      | JSON schema, OpenAPI checks |
| 5 | Contract testing       | consumer/provider contracts, schema drift |
| 6 | Mock servers           | stub server, fake responses, isolation |
| 7 | **Мини-проект**        | Advanced API suite |

---

### НЕДЕЛЯ 4 — API: reliability и integration

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Async API и polling    | eventual consistency, wait loops, timeouts |
| 2 | Pagination и filtering | list endpoints, limits, ordering |
| 3 | Stateful scenarios     | цепочки запросов, зависимые состояния |
| 4 | Config и secrets       | env vars, secret handling, config layers |
| 5 | API test architecture  | clients, services, utils, config |
| 6 | Reporting и diagnostics | логи, артефакты, трассировка проблем |
| 7 | **Мини-проект**        | API framework with config layers |

---

### НЕДЕЛЯ 5 — UI: продвинутый уровень

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Auth state             | storage state, cookies, session reuse |
| 2 | Network interception   | route, mock, HAR, deterministic UI tests |
| 3 | Advanced waits         | race conditions, sync points, stability |
| 4 | Locator strategy       | устойчивые локаторы, anti-patterns |
| 5 | Page Object architecture | page components, reusable flows |
| 6 | Debugging UI failures  | traces, screenshots, video, logs |
| 7 | **Мини-проект**        | Stable UI suite |

---

### НЕДЕЛЯ 6 — UI: качество и масштабирование

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Visual regression      | snapshots, baseline, acceptable diffs |
| 2 | Accessibility basics   | a11y checks, roles, labels, keyboard paths |
| 3 | Cross-browser strategy | browser matrix, risk-based coverage |
| 4 | Test data in UI tests  | изоляция данных, состояние окружения |
| 5 | Parallel UI execution  | concurrency risks, test isolation |
| 6 | CI for UI tests        | selective runs, retries, artifacts |
| 7 | **Мини-проект**        | UI suite in CI |

---

### НЕДЕЛЯ 7 — Infrastructure for QA

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Docker for QA          | контейнеры, reproducible env, compose basics |
| 2 | docker-compose basics  | multi-service env, dependencies |
| 3 | CI pipelines           | matrix builds, caching, selective runs |
| 4 | Quality gates          | coverage thresholds, fail-fast rules |
| 5 | Observability          | logs, metrics, traces |
| 6 | Artifacts и reports    | screenshots, videos, logs, allure artifacts |
| 7 | **Мини-проект**        | CI-ready test environment |

---

### НЕДЕЛЯ 8 — Senior QA Engineering

| # | Тема | Ключевые понятия |
|---|------|-----------------|
| 1 | Security testing basics | OWASP mindset, auth risks, secrets |
| 2 | Performance testing basics | latency, throughput, smoke perf checks |
| 3 | Test strategy          | risk-based planning, scope, trade-offs |
| 4 | Risk-based testing     | приоритизация и глубина покрытия |
| 5 | Architecture review    | анализ тестовой архитектуры и техдолга |
| 6 | Capstone preparation   | планирование, scope, quality bar |
| 7 | **Capstone**           | Advanced QA project |

---
## 🎯 Итоговый портфолио-проект

**Репозиторий:** `qa-automation-portfolio`
**Стек:** Python 3.14 · PyTest · Requests · Playwright · SQLite · Allure · GitHub Actions

| Модуль | Содержание |
|--------|-----------|
| Unit-тесты  | Тесты с моками и фикстурами |
| API-тесты   | CRUD-тесты reqres.in с валидацией |
| UI-тесты    | Playwright + Page Object Model |
| CI/CD       | GitHub Actions, автозапуск тестов при push |
| Отчёты      | Allure: история, шаги, скриншоты |

---

## 📊 Прогресс

> Обновляется автоматически по результатам обучения

```
Неделя 1    Python   ████████████████  100%
Неделя 2    Python   ████████████████  100%
Неделя 3    Python   ███████████░░░░░  71%
Неделя 4    ООП      ░░░░░░░░░░░░░░░░  0%
Неделя 5    PyTest   ░░░░░░░░░░░░░░░░  0%
Неделя 6    API      ░░░░░░░░░░░░░░░░  0%
Неделя 7    UI       ░░░░░░░░░░░░░░░░  0%
Неделя 8    SQL+Tools░░░░░░░░░░░░░░░░  0%
Неделя 9    AI       ░░░░░░░░░░░░░░░░  0%
Неделя 10   Project  ░░░░░░░░░░░░░░░░  0%
Неделя 11   PyTest   ░░░░░░░░░░░░░░░░  0%
Неделя 12   Career   ░░░░░░░░░░░░░░░░  0%
```

---

## ✅ Дорожная карта по дням

### Неделя 1 — Python с нуля
- [x] День 1 — Настройка окружения
- [x] День 2 — Переменные и типы данных
- [x] День 3 — Условия
- [x] День 4 — Циклы
- [x] День 5 — Функции: основы
- [x] День 6 — Функции: продвинуто
- [x] День 7 — Мини-проект: Калькулятор

### Неделя 2 — Структуры данных
- [x] День 1 — Списки
- [x] День 2 — Кортежи
- [x] День 3 — Словари
- [x] День 4 — Строки
- [x] День 5 — Файлы + JSON
- [x] День 6 — Множества
- [x] День 7 — Мини-проект: Парсер JSON

### Неделя 3 — Продвинутый Python для QA
- [ ] День 1 — Исключения
- [x] День 2 — Декораторы: база
- [x] День 3 — Type hints
- [x] День 4 — Регулярные выражения
- [x] День 5 — Logging
- [x] День 6 — pathlib и утилиты
- [ ] День 7 — Мини-проект: CLI-анализатор артефактов

### Неделя 4 — ООП
- [ ] День 1 — Классы и объекты
- [ ] День 2 — Методы
- [ ] День 3 — Наследование
- [ ] День 4 — Инкапсуляция
- [ ] День 5 — ООП на практике
- [ ] День 6 — Модули и пакеты
- [ ] День 7 — Мини-проект: User / Admin

### Неделя 5 — Основы тестирования + PyTest
- [ ] День 1 — Теория тестирования
- [ ] День 2 — Первые тесты PyTest
- [ ] День 3 — Assertions
- [ ] День 4 — AAA-паттерн
- [ ] День 5 — Фикстуры: основы
- [ ] День 6 — Запуск и отчёты Allure
- [ ] День 7 — Мини-проект: тесты функций

### Неделя 6 — Тестирование API
- [ ] День 1 — HTTP и REST
- [ ] День 2 — requests
- [ ] День 3 — Первые API-тесты
- [ ] День 4 — Валидация данных
- [ ] День 5 — API тест-фреймворк
- [ ] День 6 — Авторизация в API
- [ ] День 7 — Мини-проект: CRUD reqres.in

### Неделя 7 — UI-тестирование (Playwright)
- [ ] День 1 — Основы Playwright
- [ ] День 2 — Локаторы
- [ ] День 3 — Действия
- [ ] День 4 — Assertions
- [ ] День 5 — Page Object Model
- [ ] День 6 — Playwright + PyTest
- [ ] День 7 — Мини-проект: UI-тесты с POM

### Неделя 8 — SQL + Инструменты
- [ ] День 1 — SQL: основы
- [ ] День 2 — SQLite в Python
- [ ] День 3 — Allure: углублённо
- [ ] День 4 — Git для QA
- [ ] День 5 — GitHub workflows
- [ ] День 6 — Повторение и практика
- [ ] День 7 — Мини-проект: API + Allure + SQLite

### НЕДЕЛЯ 9 — AI в тестировании и разработке ПО
- [ ] День 1 — AI-инструменты и роли
- [ ] День 2 — AI для тест-дизайна
- [ ] День 3 — AI для генерации тестов
- [ ] День 4 — AI-агенты и workflows
- [ ] День 5 — AI для review и debug
- [ ] День 6 — Безопасное использование AI
- [ ] День 7 — Мини-проект: AI-assisted QA workflow

### Неделя 10 — Портфолио + Резюме
- [ ] День 1 — Архитектура проекта
- [ ] День 2 — Unit-тесты
- [ ] День 3 — API-тесты
- [ ] День 4 — UI-тесты
- [ ] День 5 — GitHub Actions
- [ ] День 6 — Оформление GitHub
- [ ] День 7 — Резюме и LinkedIn

### Неделя 11 — PyTest продвинутый уровень
- [ ] День 1 — Параметризация
- [ ] День 2 — Маркеры
- [ ] День 3 — conftest.py
- [ ] День 4 — Моки: основы
- [ ] День 5 — Моки: практика
- [ ] День 6 — Структура проекта
- [ ] День 7 — Мини-проект: параметризация + моки

### Неделя 12 — Финализация портфолио
- [ ] День 1 — Архитектура финального проекта
- [ ] День 2 — Unit-тесты
- [ ] День 3 — API-тесты
- [ ] День 4 — UI-тесты
- [ ] День 5 — CI/CD
- [ ] День 6 — README и документация
- [ ] День 7 — Резюме и LinkedIn

---

*Старт → Неделя 1, День 1: Настройка окружения*

## 📊 Прогресс по расширенному курсу

> Обновляется автоматически по результатам обучения

```
Неделя 1    PyTest   ░░░░░░░░░░░░░░░░  0%
Неделя 2    Data     ░░░░░░░░░░░░░░░░  0%
Неделя 3    API      ░░░░░░░░░░░░░░░░  0%
Неделя 4    API      ░░░░░░░░░░░░░░░░  0%
Неделя 5    UI       ░░░░░░░░░░░░░░░░  0%
Неделя 6    UI       ░░░░░░░░░░░░░░░░  0%
Неделя 7    Infra    ░░░░░░░░░░░░░░░░  0%
Неделя 8    Senior   ░░░░░░░░░░░░░░░░  0%
```

---

## ✅ Дорожная карта по дням — Расширенный курс

### Неделя 1 — PyTest: продвинутый уровень
- [ ] День 1 — Advanced fixtures
- [ ] День 2 — Parametrization patterns
- [ ] День 3 — Markers и test selection
- [ ] День 4 — Mocking deeper
- [ ] День 5 — Flaky tests
- [ ] День 6 — pytest-xdist
- [ ] День 7 — Мини-проект: устойчивый PyTest suite

### Неделя 2 — Test Data Engineering
- [ ] День 1 — Factories
- [ ] День 2 — Builder pattern
- [ ] День 3 — Test data management
- [ ] День 4 — Property-based testing
- [ ] День 5 — Edge cases
- [ ] День 6 — Reusable datasets
- [ ] День 7 — Мини-проект: генерация и проверка тестовых данных

### Неделя 3 — API: продвинутый уровень
- [ ] День 1 — Auth flows
- [ ] День 2 — Retries и idempotency
- [ ] День 3 — Negative scenarios
- [ ] День 4 — Schema validation
- [ ] День 5 — Contract testing
- [ ] День 6 — Mock servers
- [ ] День 7 — Мини-проект: advanced API suite

### Неделя 4 — API: reliability и integration
- [ ] День 1 — Async API и polling
- [ ] День 2 — Pagination и filtering
- [ ] День 3 — Stateful scenarios
- [ ] День 4 — Config и secrets
- [ ] День 5 — API test architecture
- [ ] День 6 — Reporting и diagnostics
- [ ] День 7 — Мини-проект: API framework with config layers

### Неделя 5 — UI: продвинутый уровень
- [ ] День 1 — Auth state
- [ ] День 2 — Network interception
- [ ] День 3 — Advanced waits
- [ ] День 4 — Locator strategy
- [ ] День 5 — Page Object architecture
- [ ] День 6 — Debugging UI failures
- [ ] День 7 — Мини-проект: stable UI suite

### Неделя 6 — UI: качество и масштабирование
- [ ] День 1 — Visual regression
- [ ] День 2 — Accessibility basics
- [ ] День 3 — Cross-browser strategy
- [ ] День 4 — Test data in UI tests
- [ ] День 5 — Parallel UI execution
- [ ] День 6 — CI for UI tests
- [ ] День 7 — Мини-проект: UI suite in CI

### Неделя 7 — Infrastructure for QA
- [ ] День 1 — Docker for QA
- [ ] День 2 — docker-compose basics
- [ ] День 3 — CI pipelines
- [ ] День 4 — Quality gates
- [ ] День 5 — Observability
- [ ] День 6 — Artifacts и reports
- [ ] День 7 — Мини-проект: CI-ready test environment

### Неделя 8 — Senior QA Engineering
- [ ] День 1 — Security testing basics
- [ ] День 2 — Performance testing basics
- [ ] День 3 — Test strategy
- [ ] День 4 — Risk-based testing
- [ ] День 5 — Architecture review
- [ ] День 6 — Capstone preparation
- [ ] День 7 — Capstone project

