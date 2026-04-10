class ListNode:
    def __init__(self, value: int, next: "ListNode | None" = None) -> None:
        self.value = value
        self.next = next



def middle_node(head: ListNode | None) -> ListNode | None:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    middle = middle_node(head)
    print(middle.value if middle else None)
