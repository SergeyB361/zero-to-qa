def show_set_operations() -> None:
    qa = {"python", "pytest", "sql"}
    auto = {"pytest", "playwright", "api"}
    print(qa | auto)
    print(qa & auto)
    print(qa - auto)
