# Bonus Advanced Python OOP, День 3 - __call__ и callable objects
#
# В этом файле нужно реализовать задания на __call__.
# Сейчас scaffold запускается и показывает стартовое поведение.


# Задание 1
# Сделай EmailMasker callable object.
#
# Идея:
# masker("sergey@example.com") -> "sergey@***"
class EmailMasker:
    # TODO:
    # def __call__(self, email: str) -> str:
    #     ...
    pass


# Задание 2
# Сделай PriorityFilter callable object.
#
# Объект должен хранить priority в __init__,
# а затем проверять, подходит ли task под это значение.
class PriorityFilter:
    def __init__(self, priority: str) -> None:
        self.priority = priority

    # TODO:
    # def __call__(self, task: dict[str, str]) -> bool:
    #     ...


# Задание 3
# Сделай AttemptLimiter callable object.
#
# Объект должен хранить limit и количество вызовов.
# Каждый вызов увеличивает счётчик.
# Возвращай True, пока лимит не превышен, иначе False.
class AttemptLimiter:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.calls = 0

    # TODO:
    # def __call__(self) -> bool:
    #     ...


# Задание 4
# Ответь после практики:
# когда для класса лучше __call__, а когда обычный метод validate()/filter()/run()?


if __name__ == "__main__":
    print("=== Current scaffold output ===")

    print("EmailMasker is callable:", callable(EmailMasker()))

    high_filter = PriorityFilter("high")
    print("PriorityFilter is callable:", callable(high_filter))

    limiter = AttemptLimiter(2)
    print("AttemptLimiter is callable:", callable(limiter))

    print()
    print("Реализуй __call__ в классах и затем проверь поведение на примерах.")
