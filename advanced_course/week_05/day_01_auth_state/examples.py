def build_storage_state(role: str) -> dict[str, object]:
    return {
        "role": role,
        "cookies": [{"name": "session", "value": f"{role}-token"}],
    }


if __name__ == "__main__":
    print(build_storage_state("admin"))
