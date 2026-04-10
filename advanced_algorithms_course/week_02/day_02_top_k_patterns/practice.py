# Неделя 2, День 2 - Top-K паттерны
#
# Задание 1:
# Реализуй top_k_largest(items, k).
#
# Задание 2:
# Реализуй top_k_smallest(items, k).
#
# Задание 3:
# Реализуй top_k_longest(words, k).


import heapq



def top_k_largest(items: list[int], k: int) -> list[int]:
    return []



def top_k_smallest(items: list[int], k: int) -> list[int]:
    return []



def top_k_longest(words: list[str], k: int) -> list[str]:
    return []


if __name__ == "__main__":
    print(top_k_largest([5, 1, 9, 3, 8], 2))
    print(top_k_smallest([5, 1, 9, 3, 8], 3))
    print(top_k_longest(["api", "ui", "automation", "db"], 2))
    print("Ожидается: top_k_largest = [9, 8], top_k_smallest = [1, 3, 5], top_k_longest = ['automation', 'api']")
    print("Реализуй top-k задачи через heapq.")
