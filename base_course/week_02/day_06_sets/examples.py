# Неделя 2, День 6 — Примеры

numbers = {1, 2, 3, 3, 2}
print("Unique numbers:", numbers)

skills = {"python", "pytest"}
skills.add("api")
skills.discard("sql")
print("Skills:", skills)

backend = {"python", "sql", "docker"}
qa = {"python", "pytest", "sql"}

print("Union:", backend | qa)
print("Intersection:", backend & qa)
print("Difference:", qa - backend)
print("Has pytest:", "pytest" in qa)
