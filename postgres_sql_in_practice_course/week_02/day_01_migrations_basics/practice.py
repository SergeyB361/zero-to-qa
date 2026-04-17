# Задание 1: create_migration_name
# Верни имя миграции.
def create_migration_name(seq: int, slug: str) -> str:
    return 'TODO'


# Задание 2: migration_table_columns
# Верни список колонок для schema_migrations.
def migration_table_columns() -> list[str]:
    return []


# Задание 3: explain_safe_migration_flow
# Верни 4 шага безопасного migration workflow.
def explain_safe_migration_flow() -> list[str]:
    return ['TODO']


# Задание 4: explain_rollback_need
# Верни 2-3 тезиса, когда нужен rollback plan.
def explain_rollback_need() -> list[str]:
    return ['TODO']


# Задание 5: migration_checklist
# Верни короткий checklist перед применением миграции.
def migration_checklist() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(explain_safe_migration_flow(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
