def divisors(n: int) -> list[int]:
    result: list[int] = []
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            result.append(divisor)
            if divisor != n // divisor:
                result.append(n // divisor)
        divisor += 1
    return sorted(result)



def prime_factorization(n: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    print(divisors(36))
    print(prime_factorization(84))
