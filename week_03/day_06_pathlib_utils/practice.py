# Неделя 3, День 6 — Практика: pathlib и утилиты

from pathlib import Path

BASE_DIR = Path(__file__).parent

# Задание 1
# Создай переменную report_path, которая указывает на файл report.txt в папке урока.
# Выведи:
# - сам путь
# - имя файла
# - расширение

report_path = BASE_DIR / "report.txt"

print(report_path)
print(report_path.name)
print(report_path.suffix)


# Задание 2
# Создай список tools = ["pytest", "playwright", "requests"]
# Выведи его через enumerate(), начиная с 1.

tools = ["pytest", "playwright", "requests"]

for index, tool in enumerate(tools, start=1):
    print(index, tool)



# Задание 3
# Даны два списка:
# names = ["api", "ui", "db"]
# scores = [90, 85, 88]
# Выведи пары через zip().

names = ["api", "ui", "db"]
scores = [90, 85, 88]

for x, y in zip(names, scores):
    print(x, y)

# Задание 4
# Дан список scores = [70, 85, 95]

# Выведи:
# - результат any(score >= 90 for score in scores)
# - результат all(score >= 60 for score in scores)

scores = [70, 85, 95]

print(any(score >= 90 for score in scores))
print(all(score >= 60 for score in scores))
