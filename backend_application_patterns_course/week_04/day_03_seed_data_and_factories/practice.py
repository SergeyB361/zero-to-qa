"""
Практическое задание:
1. Реализуй детерминированную factory для ticket payload.
2. Реализуй seed set для стартового backlog.
3. Дай возможность точечно переопределять поля через overrides.

Например:
- `make_ticket(1)` -> `{'title': 'Ticket 1', 'status': 'new', 'owner': 'user-1'}`
- `make_ticket(2, status='done')` -> тот же payload, но со status=`done`
- `seed_backlog()` -> два предсказуемых tickets для стартового сценария

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass, asdict


@dataclass(slots=True)
class TicketPayload:
    title: str
    status: str
    owner: str



def make_ticket(sequence: int, **overrides: object) -> TicketPayload:
    # TODO: создать детерминированный payload и применить overrides.
    return TicketPayload(title='TODO', status='TODO', owner='TODO')



def seed_backlog() -> list[TicketPayload]:
    # TODO: вернуть два стартовых tickets для backlog.
    return []



def run_checks() -> None:
    assert asdict(make_ticket(1)) == {'title': 'Ticket 1', 'status': 'new', 'owner': 'user-1'}, 'default factory payload is incorrect'
    assert asdict(make_ticket(2, status='done')) == {'title': 'Ticket 2', 'status': 'done', 'owner': 'user-2'}, 'factory overrides are incorrect'
    assert [asdict(item) for item in seed_backlog()] == [
        {'title': 'Ticket 1', 'status': 'new', 'owner': 'user-1'},
        {'title': 'Ticket 2', 'status': 'in_progress', 'owner': 'lead-2'},
    ], 'seed backlog payload is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
