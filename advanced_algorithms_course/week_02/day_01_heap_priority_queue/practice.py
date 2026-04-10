# Неделя 2, День 1 - Heap / Priority Queue
#
# Задание 1:
# Реализуй extract_all_sorted(items) через heapq.
#
# Задание 2:
# Реализуй smallest_two(items) -> два минимальных элемента.
#
# Задание 3:
# Реализуй process_tasks(tasks), где tasks - список пар
# (priority, name), и результат - порядок обработки.


import heapq



def extract_all_sorted(items: list[int]) -> list[int]:
    return []



def smallest_two(items: list[int]) -> list[int]:
    return []



def process_tasks(tasks: list[tuple[int, str]]) -> list[str]:
    return []


if __name__ == "__main__":
    print(extract_all_sorted([4, 1, 7, 2]))
    print(smallest_two([9, 3, 5, 1, 6]))
    print(process_tasks([(3, "deploy"), (1, "fix"), (2, "test")]))
    print("Ожидается: extract_all_sorted = [1, 2, 4, 7], smallest_two = [1, 3], process_tasks = ['fix', 'test', 'deploy']")
    print("Реализуй базовые задачи на heapq.")
