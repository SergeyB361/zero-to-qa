# Неделя 1, День 6 - Практика на сложность
#
# Задание 1:
# Посмотри на функцию count_matches_bruteforce и подпиши её сложность.
#
# Задание 2:
# Реализуй более эффективную версию contains_duplicate(items).
#
# Задание 3:
# Коротко ответь в комментарии:
# когда list лучше, а когда set лучше для membership lookup?


def count_matches_bruteforce(left: list[int], right: list[int]) -> int:
    # TODO: O(?)
    count = 0
    for x in left:
        for y in right:
            if x == y:
                count += 1
    return count



def contains_duplicate(items: list[int]) -> bool:
    return False


if __name__ == "__main__":
    print(count_matches_bruteforce([1, 2, 3], [2, 3, 4]))
    print(contains_duplicate([1, 2, 3, 2]))
    print("Ожидается: count_matches_bruteforce = 2, contains_duplicate = True")
    print("Добавь оценку сложности и более эффективное решение.")
