# Неделя 3, День 6 — Практика: pathlib и утилиты

from pathlib import Path

BASE_DIR = Path(__file__).parent

# Задание 1
# Создай переменную report_path, которая указывает на файл report.txt в папке урока.
# Выведи:
# - сам путь
# - имя файла
# - расширение


# Задание 2
# Создай список tools = ["pytest", "playwright", "requests"]
# Выведи его через enumerate(), начиная с 1.


# Задание 3
# Даны два списка:
# names = ["api", "ui", "db"]
# scores = [90, 85, 88]
# Выведи пары через zip().


# Задание 4
# Дан список scores = [70, 85, 95]
# Выведи:
# - результат any(score >= 90 for score in scores)
# - результат all(score >= 60 for score in scores)
