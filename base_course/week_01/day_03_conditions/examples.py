# День 3 — Примеры: условия

# --- if / elif / else ---
score = 85

if score >= 90:
    print("Отлично")
elif score >= 70:
    print("Хорошо")       # выведет это
elif score >= 50:
    print("Удовлетворительно")
else:
    print("Не сдал")

# --- Операторы сравнения ---
print(10 > 5)      # True
print(10 == 10)    # True
print(10 != 5)     # True
print("a" < "b")   # True

# --- and / or / not ---
age = 25
has_experience = True

if age >= 18 and has_experience:
    print("Подходит на должность")

# --- in / not in ---
status = "active"
valid_statuses = ["active", "pending", "blocked"]

if status in valid_statuses:
    print(f"Статус '{status}' корректный")

# --- Тернарный оператор ---
score = 95
result = "PASS" if score >= 60 else "FAIL"
print(f"Результат: {result}")

# --- Truthiness ---
name = "Sergey"
empty_list = []

if name:
    print(f"Имя: {name}")

if not empty_list:
    print("Список пуст")

# --- match/case (Python 3.10+) ---
http_status = 404

match http_status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")    # выведет это
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Статус: {http_status}")
