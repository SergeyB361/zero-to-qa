from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventKey:
    event_type: str
    entity_id: str


class BaseModel:
    def __init__(self, **kwargs: object) -> None:
        super().__init__()


class TimestampMixin(BaseModel):
    def __init__(self, created_at: str, **kwargs: object) -> None:
        self.created_at = created_at
        super().__init__(**kwargs)


class SoftDeleteMixin(BaseModel):
    def __init__(self, is_deleted: bool = False, **kwargs: object) -> None:
        self.is_deleted = is_deleted
        super().__init__(**kwargs)


class TaskRecord(TimestampMixin, SoftDeleteMixin):
    def __init__(self, task_id: str, title: str, created_at: str, is_deleted: bool = False) -> None:
        self.task_id = task_id
        self.title = title
        super().__init__(created_at=created_at, is_deleted=is_deleted)


class SlotPoint:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    key = EventKey("task.created", "TASK-101")
    print("=== dataclass ===")
    print(key)
    print(EventKey("task.created", "TASK-101") == key)
    print()

    record = TaskRecord("TASK-101", "Fix login", "2026-04-13", is_deleted=False)
    print("=== multiple inheritance ===")
    print(record.task_id, record.title, record.created_at, record.is_deleted)
    print(TaskRecord.__mro__)
    print()

    point = SlotPoint(3, 5)
    print("=== __slots__ ===")
    print(point.x, point.y)
    try:
        point.color = "red"
    except AttributeError as error:
        print(error)