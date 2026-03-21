TEST_GENERATION_TASKS = [
    "Сгенерируй pytest-тесты для функции normalize_email(email).",
    "Подготовь черновик API-теста на POST /users с проверкой status code и body.",
    "Напиши UI-тест логина с Page Object Model и explain assumptions.",
]


def show_test_generation_tasks() -> None:
    for task in TEST_GENERATION_TASKS:
        print(task)


if __name__ == "__main__":
    show_test_generation_tasks()
