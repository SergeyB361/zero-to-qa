def gcd_iterative(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a



def are_coprime(a: int, b: int) -> bool:
    return gcd_iterative(a, b) == 1



def reduce_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    divisor = gcd_iterative(numerator, denominator)
    return numerator // divisor, denominator // divisor


if __name__ == "__main__":
    print(gcd_iterative(48, 18))
    print(are_coprime(9, 28))
    print(reduce_fraction(42, 56))
