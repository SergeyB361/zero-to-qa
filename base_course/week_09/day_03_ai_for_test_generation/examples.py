TEST_GENERATION_TASKS = [
    "Сгенерируй pytest-тесты для функции из base_course/week_01/day_07_miniproject_calculator/calculator.py и отдельно перечисли assumptions.",
    "Подготовь черновик тестов для метода has_permission() из solution_users_system.py.",
    "Сгенерируй тесты и отдельно скажи, что обязательно проверить вручную перед коммитом.",
]


def show_test_generation_tasks() -> None:
    for task in TEST_GENERATION_TASKS:
        print(task)


if __name__ == "__main__":
    show_test_generation_tasks()
