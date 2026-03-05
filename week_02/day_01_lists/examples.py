# Неделя 2, День 1 — Примеры: списки

numbers = [10, 20, 30, 40]
print(numbers[0])      # 10
print(numbers[-1])     # 40
print(numbers[1:3])    # [20, 30]

numbers.append(50)
print(numbers)         # [10, 20, 30, 40, 50]

numbers.remove(20)
print(numbers)         # [10, 30, 40, 50]

last = numbers.pop()
print(last)            # 50
print(numbers)         # [10, 30, 40]

raw = [5, 1, 9, 3]
print(sorted(raw))     # [1, 3, 5, 9]
print(raw)             # [5, 1, 9, 3]
raw.sort(reverse=True)
print(raw)             # [9, 5, 3, 1]

# list comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

odd_squares = [x * x for x in range(1, 11) if x % 2 == 1]
print(odd_squares)
