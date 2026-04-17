# Задание 1: write_psql_connect_command
# Верни строку команды подключения к zero_to_qa.
def write_psql_connect_command() -> str:
    return 'psql -h localhost -U postgres -d zero_to_qa'


# Задание 2: write_list_tables_command
# Верни строку psql-команды для просмотра таблиц.
def write_list_tables_command() -> str:
    return r'\dt'


# Задание 3: write_describe_tasks_command
# Верни строку psql-команды для описания tasks.
def write_describe_tasks_command() -> str:
    return r'\d tasks'


# Задание 4: write_run_sql_file_command
# Верни строку psql-команды для выполнения sql-файла.
def write_run_sql_file_command() -> str:
    return 'psql -h localhost -U postgres -d zero_to_qa -f postgres_lab/init/001_schema.sql'


# Задание 5: compare_cli_vs_gui
# Верни 3 коротких тезиса: когда psql, когда DBeaver.
def compare_cli_vs_gui() -> list[str]:
    return [
        'psql удобен для быстрых команд, проверки окружения и запуска sql-файлов.',
        'DBeaver удобнее для чтения схемы, табличного просмотра данных и ad-hoc анализа.',
        'CLI лучше для repeatable workflow, GUI лучше для визуальной навигации по данным.',
    ]


def run_checks() -> None:
    assert write_psql_connect_command() == 'psql -h localhost -U postgres -d zero_to_qa'
    assert write_list_tables_command() == r'\dt'
    assert write_describe_tasks_command() == r'\d tasks'
    assert '001_schema.sql' in write_run_sql_file_command()
    assert len(compare_cli_vs_gui()) == 3
    print('psql/DBeaver workflow checks passed.')


if __name__ == '__main__':
    run_checks()
