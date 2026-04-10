# Неделя 5, День 5 - Симуляции на queue/deque
#
# Задание 1:
# Реализуй process_jobs(jobs) -> порядок обработки.
#
# Задание 2:
# Реализуй round_robin_twice(players),
# где очередь циклически сдвигается 2 раза.
#
# Задание 3:
# Реализуй serve_until_empty(items),
# которая возвращает количество обслуженных элементов.


def process_jobs(jobs: list[str]) -> list[str]:
    return []



def round_robin_twice(players: list[str]) -> list[str]:
    return []



def serve_until_empty(items: list[int]) -> int:
    return -1


if __name__ == "__main__":
    print(process_jobs(["a", "b", "c"]))
    print(round_robin_twice(["A", "B", "C", "D"]))
    print(serve_until_empty([1, 2, 3, 4]))
    print("Ожидается: process_jobs = ['a', 'b', 'c'], round_robin_twice = ['C', 'D', 'A', 'B'], serve_until_empty = 4")
    print("Реализуй симуляции на queue/deque.")
