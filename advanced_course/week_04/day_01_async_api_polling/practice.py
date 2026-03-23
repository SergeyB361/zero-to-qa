# День 1 — Практика: async API и polling

def wait_until_done(statuses: list[str], pending: set[str], success: str) -> str:
    return ''


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('success reached', wait_until_done(['queued', 'running', 'done'], {'queued', 'running'}, 'done') == 'done'),
        ('failure returned immediately', wait_until_done(['queued', 'error', 'done'], {'queued', 'running'}, 'done') == 'failed:error'),
        ('timeout when success missing', wait_until_done(['queued', 'running'], {'queued', 'running'}, 'done') == 'timeout'),
    ]


if __name__ == '__main__':
    print('Реализуй polling helper:')
    for name, status in run_checks():
        print(f'{name}: {status}')
