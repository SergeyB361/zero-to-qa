# Backend Application Patterns — ROADMAP

## Статус
- `week_01-week_04` заполнены материалами;
- курс собран целиком.

## Цель курса
Собрать из уже изученных блоков `FastAPI`, `SQLAlchemy`, `Postgres` и `Docker` нормальный backend-service уровня junior/junior+.

## Результат курса
После курса студент должен уметь:
- разложить backend на `routers / services / repositories / models / schemas / config`;
- подключить `FastAPI + SQLAlchemy + Postgres`;
- организовать миграции через Alembic;
- реализовать auth и role checks на базовом уровне;
- собрать CRUD с pagination/filtering/sorting;
- написать integration tests;
- завернуть сервис в `Docker Compose`.

## Неделя 1 — Application Structure
1. `day_01_project_layout_layers`
2. `day_02_settings_env_config`
3. `day_03_dependency_injection_boundaries`
4. `day_04_error_handling_api_contracts`
5. `day_05_crud_style_guidelines`
6. `day_06_structure_practice`
7. `day_07_miniproject_service_skeleton`

## Неделя 2 — Database and Migrations
1. `day_01_sqlalchemy_session_patterns`
2. `day_02_postgres_integration_patterns`
3. `day_03_alembic_basics`
4. `day_04_schema_evolution_cases`
5. `day_05_relationships_in_real_services`
6. `day_06_db_practice`
7. `day_07_miniproject_migrated_service`

## Неделя 3 — Auth, CRUD and Business Rules
1. `day_01_auth_basics_tokens_headers`
2. `day_02_password_hashing_user_model`
3. `day_03_roles_permissions`
4. `day_04_filter_sort_paginate`
5. `day_05_partial_update_soft_delete`
6. `day_06_business_rules_practice`
7. `day_07_miniproject_secure_crud_api`

## Неделя 4 — Testing, Delivery and Capstone
1. `day_01_test_db_strategy`
2. `day_02_integration_testing_fastapi_db`
3. `day_03_seed_data_and_factories`
4. `day_04_docker_compose_app_db`
5. `day_05_ci_basics_for_backend`
6. `day_06_capstone_prep`
7. `day_07_capstone_backend_service`
