def reverse_with_stack(items: list[int]) -> list[int]:
    stack: list[int] = []
    for item in items:
        stack.append(item)

    result: list[int] = []
    while stack:
        result.append(stack.pop())
    return result



def top_item(stack: list[int]) -> int | None:
    if not stack:
        return None
    return stack[-1]


if __name__ == "__main__":
    print(reverse_with_stack([1, 2, 3, 4]))
    print(top_item([10, 20, 30]))
    print(top_item([]))
