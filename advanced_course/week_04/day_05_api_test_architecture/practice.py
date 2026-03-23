# День 5 — Практика: API test architecture

def layer_mapping() -> dict[str, str]:
    return {}


def run_checks() -> list[tuple[str, bool]]:
    mapping = {k: v.lower() for k, v in layer_mapping().items()}
    return [
        ('transport present', 'transport' in mapping),
        ('data present', 'data' in mapping),
        ('asserts present', 'asserts' in mapping),
        ('tests present', 'tests' in mapping),
        ('transport mentions requests/client', 'request' in mapping.get('transport', '') or 'client' in mapping.get('transport', '')),
        ('asserts mentions verification', 'assert' in mapping.get('asserts', '') or 'verify' in mapping.get('asserts', '')),
    ]


if __name__ == '__main__':
    print('Опиши responsibilities по слоям:')
    for name, status in run_checks():
        print(f'{name}: {status}')
