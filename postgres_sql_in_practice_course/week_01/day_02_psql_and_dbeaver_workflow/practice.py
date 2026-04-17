# Задание 1: write_psql_connect_command
# Верни строку команды подключения к zero_to_qa.
def write_psql_connect_command() -> str:
    return 'TODO'


# Задание 2: write_list_tables_command
# Верни строку psql-команды для просмотра таблиц.
def write_list_tables_command() -> str:
    return 'TODO'


# Задание 3: write_describe_tasks_command
# Верни строку psql-команды для описания tasks.
def write_describe_tasks_command() -> str:
    return 'TODO'


# Задание 4: write_run_sql_file_command
# Верни строку psql-команды для выполнения sql-файла.
def write_run_sql_file_command() -> str:
    return 'TODO'


# Задание 5: compare_cli_vs_gui
# Верни 3 коротких тезиса: когда psql, когда DBeaver.
def compare_cli_vs_gui() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(compare_cli_vs_gui(), list)
    print('Scaffold checks passed. Заполни реальные команды и тезисы.')


if __name__ == '__main__':
    run_checks()
