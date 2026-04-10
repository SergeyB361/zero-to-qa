# Неделя 4, День 1 - dict и set как алгоритмический инструмент
#
# Задание 1:
# Реализуй has_duplicate(items).
#
# Задание 2:
# Реализуй unique_count(items) -> количество уникальных элементов.
#
# Задание 3:
# Реализуй index_by_name(users), где users - список словарей,
# а результат - dict вида name -> user.


def has_duplicate(items: list[int]) -> bool:
    return False



def unique_count(items: list[int]) -> int:
    return -1



def index_by_name(users: list[dict[str, str | int]]) -> dict[str, dict[str, str | int]]:
    return {}


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))
    print(unique_count([1, 1, 2, 3, 3]))
    print(index_by_name([{"name": "Ann", "age": 20}, {"name": "Bob", "age": 30}]))
    print("Реализуй задачи через dict и set.")
