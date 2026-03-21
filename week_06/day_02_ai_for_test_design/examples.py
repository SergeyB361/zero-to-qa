PROMPTS = [
    "Предложи позитивные, негативные и граничные тест-кейсы для функции is_adult(age).",
    "Составь risk-based checklist для логина с паролем и восстановлением доступа.",
    "Назови edge cases для API создания пользователя с обязательными полями.",
]


def show_prompts() -> None:
    for prompt in PROMPTS:
        print(prompt)


if __name__ == "__main__":
    show_prompts()
