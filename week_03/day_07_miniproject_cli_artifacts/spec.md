# ТЗ: CLI-анализатор тестовых артефактов

Реализуй в `artifact_cli.py`:

1. Данные
- Используй файл `artifacts.log` в папке проекта.
- Формат строк, например:

```text
INFO TestCase id=101 started
TEST PASSED id=101
WARNING Retry for id=102
TEST FAILED id=102
ERROR Timeout while processing id=102
INFO TestCase id=103 started
TEST PASSED id=103
```

2. Функции
- `read_lines(path)`
  - читает файл
  - возвращает список строк

- `count_errors(lines)`
  - возвращает количество строк с `ERROR`

- `count_passed(lines)`
  - возвращает количество строк с `TEST PASSED`

- `count_failed(lines)`
  - возвращает количество строк с `TEST FAILED`

- `extract_ids(lines)`
  - через regex достаёт все числовые `id`
  - возвращает список найденных id

3. Основной сценарий
- прочитать `artifacts.log`
- вывести:
  - `Total lines: <число>`
  - `Errors: <число>`
  - `Passed: <число>`
  - `Failed: <число>`
  - `IDs: <список id>`

4. Точка входа
- `if __name__ == "__main__":`
  - вызов `main()`

Опционально:
- вывести уникальные id отдельно.
