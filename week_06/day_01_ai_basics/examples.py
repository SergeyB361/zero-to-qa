AI_TOOLS = {
    "Codex": "Исправить конкретный файл, добавить тест, выполнить проверку",
    "Claude Code": "Разобрать структуру репозитория и предложить план изменений",
    "ChatGPT": "Сгенерировать test cases, объяснить идею, улучшить промпт",
    "GitHub Copilot": "Быстро дописать шаблонный код внутри текущего файла",
}


def show_ai_tools() -> None:
    for tool, purpose in AI_TOOLS.items():
        print(f"{tool}: {purpose}")


if __name__ == "__main__":
    show_ai_tools()
