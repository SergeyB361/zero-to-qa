ALLOWED_TRANSITIONS = {
    "new": {"paid", "cancelled"},
    "paid": {"refunded"},
    "cancelled": set(),
}


def can_transition(current: str, target: str) -> bool:
    return target in ALLOWED_TRANSITIONS.get(current, set())


if __name__ == "__main__":
    print(can_transition("new", "paid"))
    print(can_transition("paid", "cancelled"))
