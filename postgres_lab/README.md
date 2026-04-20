# Postgres Lab

Общее окружение для новых Postgres-native SQL-курсов.

## Что внутри
- `docker-compose.yml` — локальный Postgres 16.
- `init/001_schema.sql` — базовая схема QA-домена.
- `init/002_seed.sql` — стартовые данные для примеров и практики.

## Быстрый старт
```powershell
docker compose up -d
```

Проверка готовности:
```powershell
docker compose ps
```

Подключение через `psql`:
```powershell
psql -h localhost -U postgres -d zero_to_qa
```

Базовые команды в `psql`:
```sql
\dt
SELECT * FROM users LIMIT 5;
```

Выполнение SQL-файла:
```powershell
psql -h localhost -U postgres -d zero_to_qa -f path\to\examples.sql
```

## Reset и re-init
Важно: файлы из `init/` выполняются только при первом создании volume.

Если ты изменил `001_schema.sql` или `002_seed.sql` и хочешь поднять базу заново с нуля, нужен полный reset volume:
```powershell
docker compose down -v
docker compose up -d
```

Когда это нужно:
- схема была изменена;
- seed-данные были изменены;
- локальная база ушла в состояние, которое уже не совпадает с курсом.

Когда это не нужно:
- ты просто перезапускаешь контейнер;
- схема и seed не менялись;
- тебе достаточно сохранить текущие данные в volume.

## Параметры по умолчанию
- host: `localhost`
- port: `5432`
- database: `zero_to_qa`
- user: `postgres`
- password: `postgres`

## Инструменты
Можно работать через:
- `psql`
- `DBeaver`
- `DataGrip`
- `PgAdmin`
