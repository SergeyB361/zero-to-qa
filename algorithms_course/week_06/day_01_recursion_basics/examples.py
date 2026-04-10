def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)



def sum_to_n(n: int) -> int:
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)



def reverse_string(text: str) -> str:
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


if __name__ == "__main__":
    print(factorial(5))
    print(sum_to_n(5))
    print(reverse_string("tree"))
