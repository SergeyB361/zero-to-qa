AGENT_TASKS = [
    "Проверить, какие мини-проекты в репозитории незавершены.",
    "Подготовить каркас новой недели курса по заданной теме.",
    "Сделать обзор тестовой структуры проекта и назвать риски.",
]


def show_agent_tasks() -> None:
    for task in AGENT_TASKS:
        print(task)


if __name__ == "__main__":
    show_agent_tasks()
