# День 4 — Примеры: циклы

# --- for по списку ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# --- range ---
print("\nrange(5):")
for i in range(5):
    print(i, end=" ")    # 0 1 2 3 4

print("\nrange(1, 6):")
for i in range(1, 6):
    print(i, end=" ")    # 1 2 3 4 5

print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")    # 0 2 4 6 8

# --- while ---
print("\n\nwhile:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1

# --- break ---
print("\n\nbreak при i==5:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")    # 0 1 2 3 4

# --- continue ---
print("\n\ncontinue (только нечётные):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")    # 1 3 5 7 9

# --- enumerate ---
print("\n\nenumerate:")
statuses = [200, 404, 500]
for i, status in enumerate(statuses, start=1):
    print(f"{i}: {status}")

# --- накопление ---
print("\nСумма 1..10:")
total = 0
for i in range(1, 11):
    total += i
print(total)    # 55
