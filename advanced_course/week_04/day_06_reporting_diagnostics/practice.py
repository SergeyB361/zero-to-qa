# День 6 — Практика: reporting и diagnostics

def diagnostic_record() -> dict[str, object]:
    return {}


def run_checks() -> list[tuple[str, bool]]:
    record = diagnostic_record()
    return [
        ('method present', 'method' in record),
        ('url present', 'url' in record),
        ('status code present', 'status_code' in record),
        ('trace id present', 'trace_id' in record),
        ('entity id present', 'entity_id' in record),
    ]


if __name__ == '__main__':
    print('Добавь базовый diagnostic payload:')
    for name, status in run_checks():
        print(f'{name}: {status}')
