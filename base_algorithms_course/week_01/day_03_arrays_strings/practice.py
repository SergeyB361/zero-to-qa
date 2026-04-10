# Неделя 1, День 3 - Массивы, списки и строки
#
# Задание 1:
# Напиши функцию middle_char(text), которая возвращает символ по центру строки.
# Если длина чётная, можно вернуть левый из двух центральных.
#
# Задание 2:
# Напиши функцию rotate_right(items), которая сдвигает список на 1 вправо.
# [1, 2, 3] -> [3, 1, 2]
#
# Задание 3:
# Напиши функцию count_vowels(text), которая считает гласные.


def middle_char(text: str) -> str:
    return "?"



def rotate_right(items: list[int]) -> list[int]:
    return []



def count_vowels(text: str) -> int:
    return -1


if __name__ == "__main__":
    print(middle_char("python"))
    print(rotate_right([1, 2, 3]))
    print(count_vowels("algorithm"))
    print("Ожидается: middle_char = 't', rotate_right = [3, 1, 2], count_vowels = 3")
    print("Замени временные ответы на реальную реализацию.")
