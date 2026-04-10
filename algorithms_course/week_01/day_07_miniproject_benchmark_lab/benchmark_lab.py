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
    sizes = [1_000, 10_000]
    target = 999

    print('Benchmark Lab demo scaffold')
    print('Подготовь одинаковые данные для linear_contains и set_contains.')
    print('Ожидаемый demo flow:')
    print('1. Создать список и set для каждого размера.')
    print('2. Замерить linear_contains и set_contains на одном target.')
    print('3. Вывести отчёт по каждому n.')

    for size in sizes:
        items = list(range(size))
        items_set = set(items)
        print(f'=== n = {size} ===')
        print('linear_contains:', linear_contains(items, target))
        print('set_contains:', set_contains(items_set, target))
        print('average_linear:', measure_average(lambda: linear_contains(items, target), repeats=10))
        print('average_set:', measure_average(lambda: set_contains(items_set, target), repeats=10))

    print('Сверь финальный вывод с форматом из spec.md.')


if __name__ == "__main__":
    main()
