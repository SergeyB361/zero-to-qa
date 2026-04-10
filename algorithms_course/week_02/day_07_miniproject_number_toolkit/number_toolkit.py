# Неделя 2, День 7 - Мини-проект: Number Toolkit


def gcd(a: int, b: int) -> int:
    return -1


def is_prime(n: int) -> bool:
    return False


def sieve(limit: int) -> list[int]:
    return []


def prime_factorization(n: int) -> list[int]:
    return []


def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    return numerator, denominator


def main() -> None:
    print('Number Toolkit demo scaffold')
    print('Ожидается рабочий demo минимум для 5 функций из spec.md.')
    print('gcd(54, 24) ->', gcd(54, 24), '| expected: 6')
    print('is_prime(29) ->', is_prime(29), '| expected: True')
    print('sieve(20) ->', sieve(20), '| expected: [2, 3, 5, 7, 11, 13, 17, 19]')
    print('prime_factorization(90) ->', prime_factorization(90), '| expected: [2, 3, 3, 5]')
    print('simplify_fraction(24, 36) ->', simplify_fraction(24, 36), '| expected: (2, 3)')


if __name__ == "__main__":
    main()
