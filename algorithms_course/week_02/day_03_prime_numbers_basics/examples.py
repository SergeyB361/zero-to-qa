def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True



def count_primes(numbers: list[int]) -> int:
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count


if __name__ == "__main__":
    print(is_prime(29))
    print(is_prime(35))
    print(count_primes([2, 4, 5, 9, 11, 15]))
