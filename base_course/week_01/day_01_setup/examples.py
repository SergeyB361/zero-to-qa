# День 1 — Примеры: проверка окружения

# ✅ Проверка версии Python
import sys
print("Python версия:", sys.version)
print("Путь к интерпретатору:", sys.executable)

# ✅ Проверка что мы в виртуальном окружении
import os
in_venv = sys.prefix != sys.base_prefix
print("Виртуальное окружение активно:", in_venv)

# ✅ Проверка текущей папки
print("Рабочая папка:", os.getcwd())

# ✅ Первая строка кода — традиция
print("Привет, путь с нуля до QA!")
