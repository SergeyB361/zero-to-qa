def intercept_request(url: str, routes: dict[str, dict[str, object]]) -> dict[str, object] | None:
    for pattern, response in routes.items():
        if pattern in url:
            return response
    return None


if __name__ == "__main__":
    routes = {"/api/users": {"status": 200, "body": {"users": []}}}
    print(intercept_request("https://example.com/api/users", routes))
