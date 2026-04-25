"""
Практическое задание:
1. Оцени schema change не как одиночный SQL, а как rollout plan.
2. Реализуй план для nullable column, non-null column и drop column.
3. Верни шаги в том порядке, в котором их реально безопасно делать.

Например:
- nullable column -> быстрое изменение с поддержкой `NULL`
- non-null column -> add, backfill, tighten constraint
- drop column -> сначала compatibility, потом drop

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SchemaChangeRequest:
    change_type: str
    nullable: bool = True



def plan_schema_change(request: SchemaChangeRequest) -> list[str]:
    # TODO: вернуть rollout plan для add nullable, add non-null и drop column.
    return ['TODO']


def run_checks() -> None:
    assert plan_schema_change(SchemaChangeRequest(change_type='add_column', nullable=True)) == [
        'add nullable column',
        'deploy app that can read null values',
    ], 'nullable column plan is incorrect'

    assert plan_schema_change(SchemaChangeRequest(change_type='add_column', nullable=False)) == [
        'add column as nullable or with safe default',
        'backfill existing rows',
        'add not-null constraint in a later step',
    ], 'non-null column plan is incorrect'

    assert plan_schema_change(SchemaChangeRequest(change_type='drop_column')) == [
        'verify no code depends on the column',
        'deploy compatibility changes first',
        'drop column in a dedicated migration',
    ], 'drop column plan is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
