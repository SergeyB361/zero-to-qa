def ears_when(trigger: str, system_response: str) -> str:
    return f"When {trigger}, the system shall {system_response}."


if __name__ == "__main__":
    print(ears_when("payment succeeds", "mark the order as paid"))
