# Bonus Advanced Python OOP, День 1 - __str__ и __repr__
#
# В этом файле нужно реализовать 4 задания.
# Файл специально сделан исполняемым: сейчас он запускается,
# а ты постепенно заменяешь TODO-реализации на нормальные методы.


# Задание 1
# Добавь __str__ для UserProfile.
# Ожидаемая идея:
# UserProfile("Sergey", "QA") -> "Sergey (QA)"
class UserProfile:
    def __init__(self, name: str, role: str) -> None:
        self.name = name
        self.role = role

    def __str__(self) -> str:
        return "<TODO: add __str__ for UserProfile>"


# Задание 2
# Добавь __repr__ для ApiRequest.
# Ожидаемая идея:
# ApiRequest(method='GET', path='/tasks')
class ApiRequest:
    def __init__(self, method: str, path: str) -> None:
        self.method = method
        self.path = path

    def __repr__(self) -> str:
        return "<TODO: add __repr__ for ApiRequest>"


# Задание 3
# Добавь и __str__, и __repr__ для BugReport.
#
# __str__:
# короткое человекочитаемое представление,
# например: BUG-17: Login button is disabled
#
# __repr__:
# более точное developer-представление,
# например:
# BugReport(bug_id='BUG-17', title='Login button is disabled', severity='high')
class BugReport:
    def __init__(self, bug_id: str, title: str, severity: str) -> None:
        self.bug_id = bug_id
        self.title = title
        self.severity = severity

    def __str__(self) -> str:
        return "<TODO: add __str__ for BugReport>"

    def __repr__(self) -> str:
        return "<TODO: add __repr__ for BugReport>"


# Задание 4
# Добавь и __str__, и __repr__ для DomainEvent.
#
# Требование:
# - __str__ должен быть коротким и читаемым
# - __repr__ должен быть полезным для отладки
# - не надо печатать огромный payload целиком
#
# Подумай, какие поля действительно нужны в repr.
class DomainEvent:
    def __init__(self, event_type: str, entity_id: str, payload_size: int) -> None:
        self.event_type = event_type
        self.entity_id = entity_id
        self.payload_size = payload_size

    def __str__(self) -> str:
        return "<TODO: add __str__ for DomainEvent>"

    def __repr__(self) -> str:
        return "<TODO: add __repr__ for DomainEvent>"


if __name__ == "__main__":
    user = UserProfile("Sergey", "QA")
    request = ApiRequest("GET", "/tasks")
    bug = BugReport("BUG-17", "Login button is disabled", "high")
    event = DomainEvent("task.created", "TASK-101", 256)

    print("=== Current scaffold output ===")
    print(user)
    print(repr(request))
    print(bug)
    print(repr(bug))
    print(event)
    print(repr(event))
    print()
    print("Реализуй TODO-методы и затем сравни вывод с условиями заданий.")
