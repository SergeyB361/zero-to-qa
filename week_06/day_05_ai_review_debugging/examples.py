REVIEW_QUESTIONS = [
    "Какие риски ты видишь в этом коде?",
    "Какие тесты здесь явно отсутствуют?",
    "Что может вызывать этот stack trace?",
    "Назови 2-3 наиболее вероятные причины падения.",
]


def show_review_questions() -> None:
    for question in REVIEW_QUESTIONS:
        print(question)


if __name__ == "__main__":
    show_review_questions()
