def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            multiple = p * p
            while multiple <= limit:
                is_prime[multiple] = False
                multiple += p
        p += 1

    return [number for number in range(limit + 1) if is_prime[number]]


if __name__ == "__main__":
    print(sieve(30))
