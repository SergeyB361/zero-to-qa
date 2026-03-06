# Неделя 2, День 2 — Примеры: кортежи

coords = (55.75, 37.62)
print(coords[0])
print(coords[1])

statuses = (200, 404, 500, 404)
print(len(statuses))
print(statuses.count(404))
print(statuses.index(500))

# проверка принадлежности
print(200 in statuses)
print(301 in statuses)

# unpacking
name, age, role = ("Sergey", 28, "QA")
print(name, age, role)

# один элемент
single = (42,)
print(type(single))
