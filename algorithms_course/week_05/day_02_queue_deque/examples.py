from collections import deque


def process_queue(items: list[str]) -> list[str]:
    queue = deque(items)
    result: list[str] = []
    while queue:
        result.append(queue.popleft())
    return result



def rotate_queue(items: list[int]) -> list[int]:
    queue = deque(items)
    queue.append(queue.popleft())
    return list(queue)


if __name__ == "__main__":
    print(process_queue(["api", "ui", "db"]))
    print(rotate_queue([1, 2, 3, 4]))
