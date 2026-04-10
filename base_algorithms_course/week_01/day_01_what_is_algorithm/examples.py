def find_max(numbers: list[int]) -> int:
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max


def count_even(numbers: list[int]) -> int:
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def sum_positive(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total


if __name__ == "__main__":
    sample = [4, -2, 9, 0, 6, -1]
    print("max:", find_max(sample))
    print("even:", count_even(sample))
    print("sum_positive:", sum_positive(sample))
