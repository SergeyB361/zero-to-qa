# Неделя 4, День 3 - Дедупликация и lookup-паттерны
#
# Задание 1:
# Реализуй deduplicate_preserve_order(items).
#
# Задание 2:
# Реализуй first_duplicate(items) -> первое значение,
# которое встретилось повторно, или None.
#
# Задание 3:
# Реализуй first_seen_indices(items),
# которая возвращает словарь item -> первый индекс.


def deduplicate_preserve_order(items: list[int]) -> list[int]:
    return []



def first_duplicate(items: list[int]) -> int | None:
    return None



def first_seen_indices(items: list[str]) -> dict[str, int]:
    return {}


if __name__ == "__main__":
    print(deduplicate_preserve_order([1, 2, 1, 3, 2, 4]))
    print(first_duplicate([5, 8, 3, 8, 9]))
    print(first_seen_indices(["a", "b", "a", "c"]))
    print("Ожидается: deduplicate_preserve_order = [1, 2, 3, 4], first_duplicate = 8, first_seen_indices = {'a': 0, 'b': 1, 'c': 3}")
    print("Реализуй дедупликацию и lookup-паттерны.")
