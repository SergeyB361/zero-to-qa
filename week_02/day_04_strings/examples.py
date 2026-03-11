# Неделя 2, День 4 — Примеры: строки

text = "  Hello, QA World!  "
print(len(text))
print(text.strip())
print(text.lower())
print(text.upper())

log = "ERROR 404 GET /api/users"
print("404" in log)
print(log.startswith("ERROR"))
print(log.endswith("users"))
print(log.find("GET"))

csv_line = "ann,bob,kate"
parts = csv_line.split(",")
print(parts)
print(" | ".join(parts))

name = "sergey"
print(name.title())
print(name.replace("gey", "gei"))
