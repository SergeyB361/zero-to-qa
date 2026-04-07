class PlainUserId:
    def __init__(self, value: str) -> None:
        self.value = value


class UserId:
    def __init__(self, value: str) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserId):
            return NotImplemented
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __repr__(self) -> str:
        return f"UserId(value={self.value!r})"


class EventKey:
    def __init__(self, event_type: str, entity_id: str) -> None:
        self.event_type = event_type
        self.entity_id = entity_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EventKey):
            return NotImplemented
        return (self.event_type, self.entity_id) == (other.event_type, other.entity_id)

    def __hash__(self) -> int:
        return hash((self.event_type, self.entity_id))

    def __repr__(self) -> str:
        return (
            f"EventKey(event_type={self.event_type!r}, "
            f"entity_id={self.entity_id!r})"
        )


if __name__ == "__main__":
    print("=== Without __eq__ ===")
    plain_1 = PlainUserId("user-1")
    plain_2 = PlainUserId("user-1")
    print(plain_1 == plain_2)
    print()

    print("=== With __eq__ and __hash__ ===")
    user_1 = UserId("user-1")
    user_2 = UserId("user-1")
    user_3 = UserId("user-2")
    print(user_1 == user_2)
    print(user_1 == user_3)
    print({user_1, user_2, user_3})
    print()

    print("=== Dict keys ===")
    counters = {
        EventKey("task.created", "TASK-1"): 3,
        EventKey("task.updated", "TASK-1"): 1,
    }
    print(counters[EventKey("task.created", "TASK-1")])
    print(counters)
