# Неделя 1, День 7 - Мини-проект: Benchmark Lab

import time


def linear_contains(items: list[int], target: int) -> bool:
    # TODO: реализуй линейный поиск
    return False



def set_contains(items_set: set[int], target: int) -> bool:
    # TODO: реализуй membership check через set
    return False



def measure_average(func, repeats: int = 1000) -> float:
    start = time.perf_counter()
    for _ in range(repeats):
        func()
    end = time.perf_counter()
    return (end - start) / repeats



def main() -> None:
    print("Реализуй benchmark_lab.py по условиям из spec.md")


if __name__ == "__main__":
    main()
