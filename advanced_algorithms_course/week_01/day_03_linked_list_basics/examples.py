class ListNode:
    def __init__(self, value: int, next: "ListNode | None" = None) -> None:
        self.value = value
        self.next = next



def build_list(values: list[int]) -> ListNode | None:
    head = None
    current = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head



def to_list(head: ListNode | None) -> list[int]:
    result: list[int] = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4])
    print(to_list(head))
