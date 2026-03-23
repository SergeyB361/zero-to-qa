# Неделя 3, День 6 — Примеры

from pathlib import Path

base_dir = Path(__file__).parent
sample = base_dir / "sample.txt"

print("Base dir:", base_dir)
print("Name:", sample.name)
print("Stem:", sample.stem)
print("Suffix:", sample.suffix)
print("Parent:", sample.parent)
print("Exists:", sample.exists())

names = ["api", "ui", "db"]
for index, name in enumerate(names, start=1):
    print(index, name)

for left, right in zip([1, 2, 3], ["a", "b", "c"]):
    print(left, right)

print(any(score >= 90 for score in [70, 85, 95]))
print(all(score >= 60 for score in [70, 85, 95]))
