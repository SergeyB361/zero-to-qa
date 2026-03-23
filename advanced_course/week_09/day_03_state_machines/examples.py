TRANSITIONS = {
    "new": {"pay": "paid", "cancel": "cancelled"},
    "paid": {"refund": "refunded"},
}


def next_state(current: str, event: str) -> str | None:
    return TRANSITIONS.get(current, {}).get(event)


if __name__ == "__main__":
    print(next_state("new", "pay"))
