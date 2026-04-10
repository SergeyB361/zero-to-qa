# Неделя 3, День 5 - Смешанная практика
#
# Задание 1:
# Реализуй has_duplicate(items).
#
# Задание 2:
# Реализуй max_sum_window(items, k).
#
# Задание 3:
# Реализуй reachable(graph, start, target).
#
# Эти три задачи специально из разных паттернов.


from collections import deque



def has_duplicate(items: list[int]) -> bool:
    return False



def max_sum_window(items: list[int], k: int) -> int:
    return -1



def reachable(graph: dict[str, list[str]], start: str, target: str) -> bool:
    return False


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))
    print(max_sum_window([2, 1, 5, 1, 3, 2], 3))
    print(reachable({"A": ["B"], "B": ["C"], "C": []}, "A", "C"))
    print("Ожидается: has_duplicate = True, max_sum_window = 9, reachable = True")
    print("Реализуй mixed practice по разным паттернам.")
