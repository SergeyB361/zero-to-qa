class Task:
    def __init__(self, task_id: str, title: str, status: str) -> None:
        self.task_id = task_id
        self.title = title
        self.status = status

    def __str__(self) -> str:
        return f"{self.task_id}: {self.title}"

    def __repr__(self) -> str:
        return (
            f"Task(task_id={self.task_id!r}, title={self.title!r}, "
            f"status={self.status!r})"
        )


class DomainEvent:
    def __init__(self, event_type: str, task_id: str, actor_id: str) -> None:
        self.event_type = event_type
        self.task_id = task_id
        self.actor_id = actor_id

    def __str__(self) -> str:
        return f"{self.event_type} for {self.task_id}"

    def __repr__(self) -> str:
        return (
            f"DomainEvent(event_type={self.event_type!r}, task_id={self.task_id!r}, "
            f"actor_id={self.actor_id!r})"
        )


if __name__ == "__main__":
    task = Task("TASK-101", "Fix login bug", "open")
    event = DomainEvent("task.created", "TASK-101", "user-42")

    print("=== print(task) uses __str__ ===")
    print(task)
    print()

    print("=== repr(task) uses __repr__ ===")
    print(repr(task))
    print()

    print("=== list uses __repr__ for elements ===")
    print([task])
    print()

    print("=== f-strings ===")
    print(f"Default: {task}")
    print(f"Debug: {task!r}")
    print()

    print("=== second object ===")
    print(event)
    print(repr(event))
    print([event])
