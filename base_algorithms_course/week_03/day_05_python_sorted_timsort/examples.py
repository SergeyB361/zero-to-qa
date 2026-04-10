def sort_by_length(words: list[str]) -> list[str]:
    return sorted(words, key=len)



def sort_tasks_by_priority(tasks: list[dict[str, int]]) -> list[dict[str, int]]:
    return sorted(tasks, key=lambda task: task["priority"])



def sort_numbers_desc(items: list[int]) -> list[int]:
    return sorted(items, reverse=True)


if __name__ == "__main__":
    print(sort_by_length(["api", "automation", "ui", "db"]))
    print(sort_numbers_desc([4, 1, 7, 2]))
    print(
        sort_tasks_by_priority(
            [
                {"id": 1, "priority": 3},
                {"id": 2, "priority": 1},
                {"id": 3, "priority": 2},
            ]
        )
    )
