def worker_username(worker_id: int) -> str:
    return f"worker_{worker_id}_user"


if __name__ == "__main__":
    print(worker_username(3))
