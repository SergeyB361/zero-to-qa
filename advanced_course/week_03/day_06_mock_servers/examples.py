def stub_users_response(case: str) -> tuple[int, dict[str, object]]:
    if case == "success":
        return 200, {"users": [{"id": 1, "email": "qa@example.com"}]}
    if case == "unauthorized":
        return 401, {"error": "unauthorized"}
    if case == "timeout":
        raise TimeoutError("provider timeout")
    return 500, {"error": "unexpected case"}


if __name__ == "__main__":
    print(stub_users_response("success"))
