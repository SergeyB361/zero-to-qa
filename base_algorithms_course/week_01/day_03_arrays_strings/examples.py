def reverse_string(text: str) -> str:
    result = ""
    for char in text:
        result = char + result
    return result


def sum_first_and_last(numbers: list[int]) -> int:
    return numbers[0] + numbers[-1]


def count_char(text: str, target: str) -> int:
    count = 0
    for char in text:
        if char == target:
            count += 1
    return count


if __name__ == "__main__":
    print(reverse_string("python"))
    print(sum_first_and_last([10, 20, 30, 40]))
    print(count_char("algorithm", "o"))
