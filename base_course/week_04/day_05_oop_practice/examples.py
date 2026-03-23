# Неделя 4, День 5 — Примеры


class TestCase:
    def __init__(self, title: str, status: str = "draft") -> None:
        self.title = title
        self.status = status

    def mark_passed(self) -> None:
        self.status = "passed"


class BugReport:
    def __init__(self, summary: str, priority: str) -> None:
        self.summary = summary
        self.priority = priority

    def is_critical(self) -> bool:
        return self.priority == "critical"


if __name__ == "__main__":
    case = TestCase("Login with valid credentials")
    case.mark_passed()
    print(case.title, case.status)

    bug = BugReport("App crashes on submit", "critical")
    print(bug.is_critical())
