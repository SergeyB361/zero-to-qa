# FastAPI Basics, Week 1 Day 6 — dependencies и validation

## Зачем вообще нужен `Depends`
Как только в нескольких endpoint-ах начинает повторяться одна и та же логика, хочется не копировать её вручную.

Типичные примеры:
- чтение заголовка;
- auth pre-check;
- общие query defaults;
- получение сервиса или конфига.

Для таких случаев в FastAPI есть dependencies.

## Как правильно думать про dependency
Dependency — это не “магия framework-а”, а просто переиспользуемая функция, которую FastAPI вызывает до route или вместе с route.

Пример:
```python
def get_actor(x_actor: str | None = Header(default=None)) -> str:
    return x_actor or 'system'

@app.get('/events')
def list_events(actor: str = Depends(get_actor)):
    ...
```

Что происходит:
1. FastAPI понимает, что route зависит от `get_actor`;
2. вызывает dependency;
3. получает результат;
4. подставляет его в route-функцию.

## Что такое validation на этом уровне
Validation — это не только Pydantic request body.

FastAPI позволяет валидировать и другие типы входных данных:
- `Query(...)`
- `Path(...)`
- `Header(...)`

Например:
```python
limit: int = Query(default=10, ge=1, le=100)
```

Это означает:
- есть default;
- значение должно быть числом;
- число должно лежать в диапазоне `1..100`.

То есть контракт API становится явным прямо в сигнатуре функции.

## Когда dependency действительно полезна
Dependency полезна, если логика:
- повторяется;
- относится к HTTP/infrastructure слою;
- должна выполняться одинаково для нескольких endpoint-ов.

Примеры хорошего применения:
- получить текущего пользователя по заголовку;
- проверить token;
- прочитать common request metadata;
- вернуть общий service object.

## Когда dependency использовать не надо
Плохая идея — заталкивать в dependency всю бизнес-логику.

Например, если там уже:
- поиск по базе;
- сложные бизнес-правила;
- ветвление доменной логики;
- побочные эффекты без необходимости,

то это уже не dependency-level задача, а скорее service layer.

## Почему validation важна инженерно
Без validation route начинает защищаться вручную:
- проверять `limit > 0`;
- проверять, что заголовок не пуст;
- проверять типы и диапазоны.

Это быстро превращает endpoint в мусорный контейнер из проверок.

Хорошая validation держит контракт ближе ко входу и делает route чище.

## Где ошибаются чаще всего
- Кладут слишком много логики в dependency.
- Используют dependency там, где хватило бы обычной helper-функции.
- Забывают ограничивать `limit`, `offset`, `page` и похожие параметры.
- Путают infrastructure-level reuse и domain-level business logic.

## Что нужно вынести из урока
Перед практикой ты должен понимать:
1. зачем нужен `Depends`;
2. где проходит граница между dependency и service logic;
3. как `Query`, `Header` и другие инструменты делают контракт API более явным.
