# Практика: use cases и user flows

QUESTIONS = {
    'task_1': 'Перечисли минимум три элемента, которые должны быть в user flow.',
    'task_2': 'Коротко объясни разницу между use case и user flow.',
    'task_3': 'Назови минимум три альтернативных пути для login или checkout flow.',
    'task_4': 'Опиши правило, как из flow извлекать тестовые идеи.',
}

ANSWERS: dict[str, object] = {
    'task_1': [],
    'task_2': '',
    'task_3': [],
    'task_4': '',
}

KEYWORDS = {
    'task_1': ['actor', 'goal'],
    'task_2': ['scenario', 'path'],
    'task_3': ['error', 'alternate'],
    'task_4': ['decision', 'transition'],
}

MIN_ITEMS = {
    'task_1': 3,
    'task_2': 0,
    'task_3': 3,
    'task_4': 0,
}

def as_text(value: object) -> str:
    if isinstance(value, list):
        return ' '.join(str(item) for item in value).lower()
    return str(value).lower()


def keyword_check(task_id: str) -> bool:
    text = as_text(ANSWERS[task_id])
    if not text.strip():
        return False
    if all(keyword in text for keyword in KEYWORDS[task_id]):
        return True
    return len(text.split()) >= max(6, len(KEYWORDS[task_id]) * 3)


def size_check(task_id: str) -> bool:
    expected = MIN_ITEMS[task_id]
    value = ANSWERS[task_id]
    if expected == 0:
        return True
    return isinstance(value, list) and len(value) >= expected


def run_checks() -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []
    for task_id in QUESTIONS:
        results.append((f'{task_id} keywords', keyword_check(task_id)))
        if MIN_ITEMS[task_id]:
            results.append((f'{task_id} size', size_check(task_id)))
    return results


if __name__ == '__main__':
    for task_id, prompt in QUESTIONS.items():
        print(f'[{task_id}] {prompt}')
        print('Current answer:', ANSWERS[task_id])
        print('Keyword check:', keyword_check(task_id))
        if MIN_ITEMS[task_id]:
            print('Size check:', size_check(task_id))
        print('---')
