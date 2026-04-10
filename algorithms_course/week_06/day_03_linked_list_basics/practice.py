# Неделя 6, День 3 - Linked List: база
#
# Задание 1:
# Реализуй класс ListNode.
#
# Задание 2:
# Реализуй build_list(values).
#
# Задание 3:
# Реализуй to_list(head).


class ListNode:
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next



def build_list(values: list[int]) -> ListNode | None:
    return None



def to_list(head: ListNode | None) -> list[int]:
    return []


if __name__ == "__main__":
    head = build_list([5, 6, 7])
    print(to_list(head))
    print("Ожидается: to_list(build_list([5, 6, 7])) = [5, 6, 7]")
    print("Реализуй базовые функции для linked list.")
