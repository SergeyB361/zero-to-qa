REVIEW_QUESTIONS = [
    "Какие реальные риски ты видишь в этом файле? Не пиши про стиль, если нет влияния на поведение.",
    "Какие тесты здесь явно отсутствуют и почему они важны?",
    "Что может вызывать этот stack trace? Назови гипотезы в порядке вероятности.",
    "Какие данные тебе нужны, чтобы сузить причину падения?",
]


def show_review_questions() -> None:
    for question in REVIEW_QUESTIONS:
        print(question)


if __name__ == "__main__":
    show_review_questions()
