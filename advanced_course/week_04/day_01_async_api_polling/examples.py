def poll_status(statuses: list[str], final_status: str = "done") -> bool:
    for status in statuses:
        if status == final_status:
            return True
    return False


if __name__ == "__main__":
    print(poll_status(["queued", "processing", "done"]))
    print(poll_status(["queued", "processing"]))
