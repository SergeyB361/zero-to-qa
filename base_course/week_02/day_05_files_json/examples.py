# Неделя 2, День 5 — Примеры: файлы и JSON

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
TXT_PATH = BASE_DIR / "sample.txt"
JSON_PATH = BASE_DIR / "sample.json"

# Запись текста
with open(TXT_PATH, "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Чтение текста
with open(TXT_PATH, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Запись JSON
payload = {
    "name": "ann",
    "role": "tester",
    "active": True,
    "scores": [10, 8, 9],
}

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

# Чтение JSON
with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"], data["scores"])
