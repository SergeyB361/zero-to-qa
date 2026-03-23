def wait_until_done(statuses: list[str], pending: set[str], success: str) -> str:
    for status in statuses:
        if status == success:
            return success
        if status not in pending:
            return f'failed:{status}'
    return 'timeout'


if __name__ == '__main__':
    print(wait_until_done(['queued', 'running', 'done'], {'queued', 'running'}, 'done'))
    print(wait_until_done(['queued', 'running'], {'queued', 'running'}, 'done'))
