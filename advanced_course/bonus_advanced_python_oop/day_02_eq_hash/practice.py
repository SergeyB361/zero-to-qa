# Bonus Advanced Python OOP, День 2 - __eq__ и __hash__
#
# В этом файле нужно реализовать задания на equality и hash.
# Сейчас файл запускается и показывает, почему стандартного поведения Python недостаточно.


# Задание 1
# Реализуй __eq__ для UserId.
# Два объекта UserId должны быть равны, если у них одинаковый value.
class UserId:
    def __init__(self, value: str) -> None:
        self.value = value

    # TODO:
    # def __eq__(self, other: object) -> bool:
    #     ...


# Задание 2
# Реализуй __eq__ и __hash__ для Tag.
# Это value object, который должен корректно дедуплицироваться в set.
class Tag:
    def __init__(self, value: str) -> None:
        self.value = value

    # TODO:
    # def __eq__(self, other: object) -> bool:
    #     ...
    #
    # def __hash__(self) -> int:
    #     ...


# Задание 3
# Реализуй __eq__ и __hash__ для EventKey.
# Равенство должно определяться по event_type и entity_id.
class EventKey:
    def __init__(self, event_type: str, entity_id: str) -> None:
        self.event_type = event_type
        self.entity_id = entity_id

    # TODO:
    # def __eq__(self, other: object) -> bool:
    #     ...
    #
    # def __hash__(self) -> int:
    #     ...


# Задание 4
# Прочитай класс MutableFilter и подумай:
# стоит ли делать его hashable.
#
# Поля этого класса могут меняться после создания объекта.
# Это опасный сигнал для __hash__.
#
# Вопрос для ответа после практики:
# почему mutable object обычно не должен быть ключом dict?
class MutableFilter:
    def __init__(self, status: str, assignee: str) -> None:
        self.status = status
        self.assignee = assignee


if __name__ == "__main__":
    print("=== Current scaffold output ===")

    user_1 = UserId("user-1")
    user_2 = UserId("user-1")
    print("UserId equality before implementation:", user_1 == user_2)

    tag_1 = Tag("api")
    tag_2 = Tag("api")
    print("Tag set size before implementation:", len({tag_1, tag_2}))

    event_key_1 = EventKey("task.created", "TASK-1")
    event_key_2 = EventKey("task.created", "TASK-1")
    print("EventKey equality before implementation:", event_key_1 == event_key_2)

    print()
    print("Реализуй __eq__ и __hash__, затем проверь, как изменится поведение.")
