def fast_pow_recursive(base: int, power: int) -> int:
    if power == 0:
        return 1
    if power % 2 == 0:
        half = fast_pow_recursive(base, power // 2)
        return half * half
    return base * fast_pow_recursive(base, power - 1)



def fast_pow_iterative(base: int, power: int) -> int:
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base
        base *= base
        power //= 2
    return result


if __name__ == "__main__":
    print(fast_pow_recursive(2, 10))
    print(fast_pow_iterative(3, 7))
