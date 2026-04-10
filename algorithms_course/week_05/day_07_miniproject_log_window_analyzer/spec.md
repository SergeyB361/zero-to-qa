# ТЗ: Log Window Analyzer

Реализуй проект в `log_window_analyzer.py`.

## Что должно быть в MVP
1. `push_log(window, level)` - добавить лог в окно.
2. `count_level(window, level)` - посчитать, сколько раз уровень встречается в окне.
3. `snapshot(window)` - вернуть текущий список элементов окна.
4. `main()` - показать demo flow.

## Требования
- окно должно быть ограничено размером `k`;
- использовать `deque(maxlen=k)`;
- показать минимум 5 добавлений логов;
- показать, как окно вытесняет старые элементы.

## Пример допустимого вывода
```text
Window: ['INFO']
Window: ['INFO', 'ERROR']
Window: ['INFO', 'ERROR', 'WARNING']
Window: ['ERROR', 'WARNING', 'ERROR']
ERROR in window: 2
WARNING in window: 1
```

## Критерии готовности
- файл запускается без ошибок;
- логика окна реализована через `deque`;
- код разбит на функции;
- вывод читается без открытия кода.
