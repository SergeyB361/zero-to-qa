# День 2 — Примеры: переменные и типы данных

# --- Типы данных ---
age = 25              # int
price = 4.99          # float
name = "Sergey"       # str
is_qa = True          # bool
result = None         # NoneType

print(type(age))      # <class 'int'>
print(type(price))    # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_qa))    # <class 'bool'>
print(type(result))   # <class 'NoneType'>

# --- Арифметика ---
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.3333...
print(10 // 3)   # 3  (целая часть)
print(10 % 3)    # 1  (остаток)
print(2 ** 10)   # 1024

# --- Преобразование типов ---
x = "42"
print(type(x))        # <class 'str'>
x = int(x)
print(type(x))        # <class 'int'>

# --- f-строки ---
name = "Sergey"
weeks = 9
print(f"Привет, {name}! Курс рассчитан на {weeks} недель.")
print(f"2 в степени 10 = {2 ** 10}")
