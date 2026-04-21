from dataclasses import dataclass


@dataclass
class ModelVersion:
    name: str
    columns: list[str]


def describe_change(old: ModelVersion, new: ModelVersion) -> dict[str, list[str]]:
    added = [column for column in new.columns if column not in old.columns]
    removed = [column for column in old.columns if column not in new.columns]
    return {'added': added, 'removed': removed}


def main() -> None:
    v1 = ModelVersion(name='task', columns=['id', 'title', 'status'])
    v2 = ModelVersion(name='task', columns=['id', 'title', 'status', 'assignee'])
    print('Schema diff ->', describe_change(v1, v2))
    print('Meaning -> this is where Alembic migration would be needed')


if __name__ == '__main__':
    main()
