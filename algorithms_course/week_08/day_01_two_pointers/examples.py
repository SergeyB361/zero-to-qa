def has_pair_with_sum_sorted(items: list[int], target: int) -> bool:
    left = 0
    right = len(items) - 1

    while left < right:
        current = items[left] + items[right]
        if current == target:
            return True
        if current < target:
            left += 1
        else:
            right -= 1
    return False



def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(has_pair_with_sum_sorted([1, 3, 4, 6, 8, 10], 14))
    print(is_palindrome("level"))
    print(is_palindrome("python"))
