# Неделя 2, День 6 — Примеры

from pathlib import Path


BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "example.txt"


print("Base dir:", BASE_DIR)
print("File path:", DATA_FILE)
print("Name:", DATA_FILE.name)
print("Stem:", DATA_FILE.stem)
print("Suffix:", DATA_FILE.suffix)
print("Parent:", DATA_FILE.parent)
print("Exists:", DATA_FILE.exists())
