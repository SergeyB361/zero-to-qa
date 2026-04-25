# Mini-Project — Migrated Service

## Зачем этот mini-project
На `week_01` сервис ещё мог жить на in-memory repository. Это было нормально для разговора про layers.

На `week_02` этого уже недостаточно. Теперь задача — перевести skeleton сервиса на настоящий data layer:
- settings с `database_url`;
- engine и session factory;
- SQLAlchemy models;
- repository поверх session;
- service с commit/rollback;
- FastAPI routes, которые работают через этот слой.

## Что здесь считается хорошим результатом
Хороший результат — это не просто "эндпоинты отвечают".

Нужно, чтобы в коде были видны правильные границы:
- config отдельно;
- ORM-модель отдельно;
- repository отдельно;
- service отдельно;
- router не коммитит сам.

## Почему здесь ещё не нужен полный production-stack
Это ещё не capstone курса. Здесь не требуется сразу делать:
- auth;
- pagination;
- integration test suite;
- Docker Compose.

Но data layer уже должен выглядеть как нормальный backend-срез, а не как временный прототип.

## Что полезно проверить самому
Перед тем как считать mini-project завершённым, полезно убедиться:
1. `POST /issues` создаёт запись через service и repository;
2. `GET /issues` читает данные из БД, а не из списка в памяти;
3. `GET /issues/{slug}` возвращает `404`, если записи нет;
4. duplicate slug не создаёт вторую запись и превращается в понятную доменную ошибку.
