# День 6 — Практика: mock servers

def scenarios_to_mock() -> list[str]:
    return []


def reasons_to_mock() -> list[str]:
    return []


def run_checks() -> list[tuple[str, bool]]:
    scenarios = ' '.join(scenarios_to_mock()).lower()
    reasons = ' '.join(reasons_to_mock()).lower()
    return [
        ('scenarios mention timeout', 'timeout' in scenarios),
        ('scenarios mention 5xx or error', '5xx' in scenarios or 'error' in scenarios),
        ('scenarios mention provider unavailable', 'unavailable' in scenarios or 'недоступ' in scenarios),
        ('reasons mention deterministic behavior', 'determin' in reasons or 'предсказ' in reasons),
        ('reasons mention external dependency', 'external' in reasons or 'внешн' in reasons),
        ('reasons mention cost or speed', 'speed' in reasons or 'быстр' in reasons or 'cost' in reasons),
    ]


if __name__ == '__main__':
    print('Опиши, какие сценарии и почему стоит мокать:')
    for name, status in run_checks():
        print(f'{name}: {status}')
