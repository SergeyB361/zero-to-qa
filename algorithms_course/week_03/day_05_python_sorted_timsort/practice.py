# Неделя 3, День 5 - Когда использовать built-in sorted()
#
# Задание 1:
# Реализуй sort_words_by_last_char(words).
#
# Задание 2:
# Реализуй sort_pairs_by_second(pairs).
#
# Задание 3:
# Реализуй sort_users_by_age_desc(users),
# где users - список словарей с ключами name и age.


def sort_words_by_last_char(words: list[str]) -> list[str]:
    return []



def sort_pairs_by_second(pairs: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return []



def sort_users_by_age_desc(users: list[dict[str, int | str]]) -> list[dict[str, int | str]]:
    return []


if __name__ == "__main__":
    print(sort_words_by_last_char(["api", "ui", "db", "automation"]))
    print(sort_pairs_by_second([("a", 3), ("b", 1), ("c", 2)]))
    print(sort_users_by_age_desc([{"name": "Ann", "age": 20}, {"name": "Bob", "age": 30}]))
    print("Используй built-in sorted() и key-функции.")
