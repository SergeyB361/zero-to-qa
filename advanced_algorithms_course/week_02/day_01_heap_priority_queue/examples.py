import heapq


def sorted_by_heap(items: list[int]) -> list[int]:
    heap = items[:]
    heapq.heapify(heap)
    result: list[int] = []
    while heap:
        result.append(heapq.heappop(heap))
    return result



def process_with_priority(tasks: list[tuple[int, str]]) -> list[str]:
    heap = tasks[:]
    heapq.heapify(heap)
    result: list[str] = []
    while heap:
        _, task_name = heapq.heappop(heap)
        result.append(task_name)
    return result


if __name__ == "__main__":
    print(sorted_by_heap([7, 2, 9, 1, 5]))
    print(process_with_priority([(2, "write"), (1, "fix"), (3, "deploy")]))
