def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)



def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True



def count_coprime_pairs(numbers: list[int]) -> int:
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if gcd(numbers[i], numbers[j]) == 1:
                count += 1
    return count


if __name__ == "__main__":
    print(count_coprime_pairs([2, 3, 4, 5]))
    print(is_prime(29))
