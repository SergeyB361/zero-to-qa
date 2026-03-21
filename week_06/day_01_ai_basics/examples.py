AI_TOOLS = {
    "Codex": "Изменение кода, тестов и файлов в проекте",
    "Claude Code": "Анализ репозитория, объяснение структуры, подготовка правок",
    "ChatGPT": "Идеи, объяснения, черновики тест-кейсов и документации",
    "GitHub Copilot": "Автодополнение и быстрые шаблонные вставки в IDE",
}


def show_ai_tools() -> None:
    for tool, purpose in AI_TOOLS.items():
        print(f"{tool}: {purpose}")


if __name__ == "__main__":
    show_ai_tools()
