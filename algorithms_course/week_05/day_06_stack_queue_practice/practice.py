# Неделя 5, День 6 - Практика на stack и queue
#
# Задание 1:
# Реализуй undo_last(actions) через стек.
#
# Задание 2:
# Реализуй first_in_line(items) через очередь.
#
# Задание 3:
# Реализуй recent_k(items, k) через deque,
# которая возвращает последние k элементов.


def undo_last(actions: list[str]) -> str | None:
    return None



def first_in_line(items: list[str]) -> str | None:
    return None



def recent_k(items: list[int], k: int) -> list[int]:
    return []


if __name__ == "__main__":
    print(undo_last(["type", "copy", "paste"]))
    print(first_in_line(["req-1", "req-2", "req-3"]))
    print(recent_k([1, 2, 3, 4, 5], 3))
    print("Выбери правильную структуру: stack, queue или deque.")
