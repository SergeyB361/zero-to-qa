from collections import deque


def undo_last(actions: list[str]) -> str | None:
    stack = actions[:]
    if not stack:
        return None
    return stack.pop()



def first_in_line(items: list[str]) -> str | None:
    queue = deque(items)
    if not queue:
        return None
    return queue.popleft()


if __name__ == "__main__":
    print(undo_last(["open", "edit", "save"]))
    print(first_in_line(["client-1", "client-2"]))
