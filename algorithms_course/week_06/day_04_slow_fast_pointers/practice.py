# Неделя 6, День 4 - Slow/Fast pointers
#
# Задание 1:
# Реализуй middle_node(head).
#
# Задание 2:
# Реализуй list_length(head) обычным проходом.
#
# Задание 3:
# Ответь в комментарии:
# чем slow/fast pointers лучше полного подсчёта длины,
# если нужна только середина?


class ListNode:
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next



def middle_node(head: ListNode | None) -> ListNode | None:
    return None



def list_length(head: ListNode | None) -> int:
    return -1


if __name__ == "__main__":
    head = ListNode(10, ListNode(20, ListNode(30, ListNode(40))))
    middle = middle_node(head)
    print(middle.value if middle else None)
    print(list_length(head))
    print("Реализуй задачи на slow/fast pointers.")
