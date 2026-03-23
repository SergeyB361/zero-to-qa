# День 6 — Примеры: функции (продвинуто)

def greet(name, role="QA"):
    return f"Привет, {name}! Роль: {role}"


def total(*numbers):
    return sum(numbers)


def build_user(**data):
    return data


square = lambda x: x * x


print(greet("Sergey"))
print(greet("Sergey", "Automation Engineer"))

print(total(1, 2, 3))
print(total(10, 20, 30, 5))

print(build_user(name="Sergey", role="tester", active=True))

print(square(6))

items = [
    {"title": "Bug", "priority": 2},
    {"title": "Task", "priority": 1},
]
print(sorted(items, key=lambda item: item["priority"]))
