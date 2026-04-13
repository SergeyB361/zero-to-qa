from dataclasses import dataclass


class TaskId:
    def __init__(self, value: str) -> None:
        self.value = value

    # TODO:
    # def __str__(self) -> str:
    #     ...
    #
    # def __repr__(self) -> str:
    #     ...
    #
    # def __eq__(self, other: object) -> bool:
    #     ...
    #
    # def __hash__(self) -> int:
    #     ...


class NonEmptyString:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, "")

    def __set__(self, instance: object, value: str) -> None:
        # TODO:
        # cleaned = value.strip()
        # if not cleaned:
        #     raise ValueError(...)
        setattr(instance, self.storage_name, value)


class ChoiceField:
    def __init__(self, *allowed_values: str) -> None:
        self.allowed_values = set(allowed_values)

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: object, value: str) -> None:
        # TODO:
        # if value not in self.allowed_values:
        #     raise ValueError(...)
        setattr(instance, self.storage_name, value)


class TaskDraft:
    title = NonEmptyString()
    status = ChoiceField("draft", "active", "disabled")
    owner = NonEmptyString()

    def __init__(self, title: str, status: str, owner: str) -> None:
        self.title = title
        self.status = status
        self.owner = owner


class StatusTransitionValidator:
    def __init__(self) -> None:
        self.transitions = {
            "draft": {"active"},
            "active": {"disabled"},
            "disabled": {"active"},
        }

    def __call__(self, old_status: str, new_status: str) -> bool:
        # TODO:
        # return new_status in self.transitions.get(old_status, set())
        return False


class EventPayloadView:
    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload

    def __getattr__(self, name: str) -> object:
        # TODO:
        # if name in self.payload:
        #     return self.payload[name]
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")


class ToDictMixin:
    def to_dict(self) -> dict[str, object]:
        if hasattr(self, "__slots__"):
            return {slot: getattr(self, slot) for slot in self.__slots__}
        return dict(self.__dict__)


@dataclass(slots=True)
class TaskRecord(ToDictMixin):
    task_id: TaskId
    title: str
    status: str
    owner: str


def main() -> None:
    print("=== Rich domain model scaffold ===")

    task_id_1 = TaskId("TASK-101")
    task_id_2 = TaskId("TASK-101")
    print("TaskId equality:", task_id_1 == task_id_2)
    print("TaskId set size:", len({task_id_1, task_id_2}))

    draft = TaskDraft(" Fix login ", "draft", " Sergey ")
    print("Draft title:", draft.title)
    print("Draft status:", draft.status)
    print("Draft owner:", draft.owner)

    validator = StatusTransitionValidator()
    print("Transition draft -> active:", validator("draft", "active"))
    print("Transition draft -> disabled:", validator("draft", "disabled"))

    payload = EventPayloadView({"actor_id": "user-1", "reason": "manual change"})
    try:
        print("Payload actor_id:", payload.actor_id)
    except AttributeError as error:
        print("Payload actor_id failed:", error)

    record = TaskRecord(task_id_1, "Fix login", "active", "Sergey")
    print(record)
    print(record.to_dict())


if __name__ == "__main__":
    main()