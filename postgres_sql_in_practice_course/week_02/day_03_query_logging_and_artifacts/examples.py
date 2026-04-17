def build_query_log_entry(name: str, sql: str) -> dict:
    return {'name': name, 'sql': sql, 'artifact': f'{name}.sql'}


def main() -> None:
    item = build_query_log_entry('open_tasks_report', 'SELECT * FROM tasks;')
    assert item['artifact'] == 'open_tasks_report.sql'
    print('Query logging example passed')


if __name__ == '__main__':
    main()
