from dataclasses import dataclass


@dataclass(slots=True)
class ProjectPayload:
    name: str
    status: str
    owner: str



def make_project(sequence: int, **overrides: object) -> ProjectPayload:
    payload = ProjectPayload(
        name=f'Project {sequence}',
        status='draft',
        owner=f'user-{sequence}',
    )
    for key, value in overrides.items():
        setattr(payload, key, value)
    return payload



def seed_backlog() -> list[ProjectPayload]:
    return [
        make_project(1, name='Portal', owner='anna'),
        make_project(2, name='Billing', status='active', owner='mila'),
    ]


if __name__ == '__main__':
    print('SEED ->', seed_backlog())
    print('FACTORY ->', make_project(3, status='archived', owner='nik'))
