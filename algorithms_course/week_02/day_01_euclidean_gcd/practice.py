# Неделя 2, День 1 - Алгоритм Евклида (НОД)
#
# Задание 1:
# Реализуй gcd(a, b) через алгоритм Евклида.
#
# Задание 2:
# Реализуй lcm(a, b) через формулу:
# lcm(a, b) = abs(a * b) // gcd(a, b)
#
# Задание 3:
# Реализуй simplify_fraction(numerator, denominator),
# которая сокращает дробь.


def gcd(a: int, b: int) -> int:
    return -1



def lcm(a: int, b: int) -> int:
    return -1



def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    return numerator, denominator


if __name__ == "__main__":
    print(gcd(54, 24))
    print(lcm(12, 18))
    print(simplify_fraction(24, 36))
    print("Ожидается: gcd = 6, lcm = 36, simplify_fraction = (2, 3)")
    print("Реализуй числовые функции на базе НОД.")
