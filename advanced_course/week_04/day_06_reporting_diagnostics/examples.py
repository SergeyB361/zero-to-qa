def build_failure_report(method: str, url: str, status: int, body: dict[str, object]) -> dict[str, object]:
    return {
        "method": method,
        "url": url,
        "status": status,
        "body": body,
    }


if __name__ == "__main__":
    print(build_failure_report("POST", "/orders", 500, {"error": "db unavailable"}))
