from dataclasses import dataclass


@dataclass(slots=True)
class SchemaChangeRequest:
    description: str
    change_type: str
    nullable: bool = True
    default: str | None = None



def plan_schema_change(request: SchemaChangeRequest) -> list[str]:
    if request.change_type == 'add_column' and request.nullable:
        return ['add nullable column', 'deploy app that can read null values']

    if request.change_type == 'add_column' and not request.nullable:
        return [
            'add column as nullable or with safe default',
            'backfill existing rows',
            'add not-null constraint in a later step',
        ]

    if request.change_type == 'drop_column':
        return [
            'verify no code depends on the column',
            'deploy compatibility changes first',
            'drop column in a dedicated migration',
        ]

    return ['review manually']


if __name__ == '__main__':
    cases = [
        SchemaChangeRequest(description='add avatar_url', change_type='add_column', nullable=True),
        SchemaChangeRequest(description='add slug', change_type='add_column', nullable=False),
        SchemaChangeRequest(description='drop legacy_code', change_type='drop_column'),
    ]
    for case in cases:
        print(case.description, '->', plan_schema_change(case))
