# Неделя 5, День 3 - Проверка скобок
#
# Задание 1:
# Реализуй is_balanced(text) для (), [], {}.
#
# Задание 2:
# Реализуй only_parentheses(text),
# которая возвращает строку только из скобочных символов.
#
# Задание 3:
# Реализуй has_empty_parentheses(text),
# которая проверяет, есть ли подстрока "()".


def is_balanced(text: str) -> bool:
    return False



def only_parentheses(text: str) -> str:
    return ""



def has_empty_parentheses(text: str) -> bool:
    return False


if __name__ == "__main__":
    print(is_balanced("{[()]}"))
    print(only_parentheses("a+(b*c)-{d/e}"))
    print(has_empty_parentheses("a + () + b"))
    print("Реализуй задачи на стек и проверку скобок.")
