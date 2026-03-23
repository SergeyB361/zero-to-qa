# День 2 — Практика: builder pattern

class TicketBuilder:
    def __init__(self) -> None:
        self._data = {
            'title': 'Untitled',
            'priority': 'medium',
            'tags': [],
            'assignee': 'qa-team',
        }

    def with_title(self, title: str) -> 'TicketBuilder':
        self._data['title'] = title
        return self

    def with_priority(self, priority: str) -> 'TicketBuilder':
        self._data['priority'] = priority
        return self

    def add_tag(self, tag: str) -> 'TicketBuilder':
        # Добавь tag без мутации shared list между объектами.
        return self

    def with_assignee(self, assignee: str) -> 'TicketBuilder':
        self._data['assignee'] = assignee
        return self

    def build(self) -> dict[str, object]:
        return {}


def run_checks() -> list[tuple[str, bool]]:
    ticket = (
        TicketBuilder()
        .with_title('Payment error')
        .with_priority('high')
        .add_tag('api')
        .with_assignee('sergey')
        .build()
    )
    return [
        ('title set', ticket.get('title') == 'Payment error'),
        ('priority set', ticket.get('priority') == 'high'),
        ('tag added', ticket.get('tags') == ['api']),
        ('assignee set', ticket.get('assignee') == 'sergey'),
    ]


if __name__ == '__main__':
    print('Собери builder и проверь цепочку вызовов:')
    for name, status in run_checks():
        print(f'{name}: {status}')
